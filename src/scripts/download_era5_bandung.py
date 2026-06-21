"""
=============================================================
 SKRIP: Unduh Data ERA5 Cekungan Bandung — Per 2 Bulan
 Strategi: 1 request = 2 bulan data (validated di CDS UI)
 Sumber  : Copernicus CDS — reanalysis-era5-single-levels
 Area    : Cekungan Bandung [N:-6.8, W:107.5, S:-7.05, E:107.75]
 Periode : 2020-2024 (30 request, masing-masing 2 bulan)
 Jam     : 24 jam/hari (00:00 - 23:00) — LENGKAP
 Variabel: 10 variabel (semua variabel asli + total_precipitation)
 Output  : data/raw/era5/era5_bandung_YYYY_MM-MM.zip
           data/raw/era5_bandung_2020_2024.csv (setelah digabung)
=============================================================
"""

import os
import sys
import glob
import zipfile
import calendar
import cdsapi
import numpy as np
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================
# KONFIGURASI
# ==============================================================
OUTPUT_DIR  = "data/raw"
ERA5_DIR    = os.path.join(OUTPUT_DIR, "era5")
OUTPUT_CSV  = os.path.join(OUTPUT_DIR, "era5_bandung_2022_2026.csv")

AREA        = [-6.80, 107.50, -7.05, 107.75]   # [N, W, S, E]
YEARS       = list(range(2022, 2027))

# SEMUA VARIABEL LENGKAP (tervalidasi 2 bulan di CDS UI)
VARIABLES = [
    "10m_u_component_of_wind",       # Angin U (m/s)
    "10m_v_component_of_wind",       # Angin V (m/s)
    "2m_dewpoint_temperature",       # Titik embun (K)
    "2m_temperature",                # Suhu udara (K)
    "surface_pressure",              # Tekanan permukaan (Pa)
    "boundary_layer_height",         # Tinggi lapisan batas (m)
    "total_column_ozone",            # Ozon kolom total
    "total_column_water_vapour",     # Uap air kolom (kg/m2)
    "total_cloud_cover",             # Tutupan awan (0-1)
    "total_precipitation",           # Curah hujan (m/jam)
]

# 24 jam per hari — LENGKAP
HOURS = [f"{h:02d}:00" for h in range(24)]

# Unduh per 2 bulan: pasangan bulan [(1,2), (3,4), (5,6), (7,8), (9,10), (11,12)]
MONTH_PAIRS = [(1,2), (3,4), (5,6), (7,8), (9,10), (11,12)]
# ==============================================================

DATASET = "reanalysis-era5-single-levels"


def get_days_in_pair(year, m1, m2):
    """Dapatkan semua hari dalam rentang 2 bulan."""
    days = set()
    for m in [m1, m2]:
        _, n = calendar.monthrange(year, m)
        for d in range(1, n + 1):
            days.add(f"{d:02d}")
    return sorted(days)


def make_request(year, m1, m2):
    days = get_days_in_pair(year, m1, m2)
    return {
        "product_type"   : ["reanalysis"],
        "variable"       : VARIABLES,
        "year"           : [str(year)],
        "month"          : [f"{m1:02d}", f"{m2:02d}"],
        "day"            : days,
        "time"           : HOURS,
        "data_format"    : "netcdf",
        "download_format": "zip",
        "area"           : AREA,
    }


def download_all():
    os.makedirs(ERA5_DIR, exist_ok=True)
    client     = cdsapi.Client()
    downloaded = []
    failed     = []

    total = len(YEARS) * len(MONTH_PAIRS)
    print("=" * 65)
    print(f"Memulai unduhan ERA5 Bandung: {total} batch (per 2 bulan)")
    print(f"Tahun    : {YEARS[0]} - {YEARS[-1]}")
    print(f"Variabel : {len(VARIABLES)} variabel (lengkap)")
    print(f"Jam      : 24 jam/hari")
    print(f"Estimasi : {total * 2} - {total * 5} menit total")
    print("=" * 65)

    for year in YEARS:
        for m1, m2 in MONTH_PAIRS:
            fname    = f"era5_bandung_{year}_{m1:02d}-{m2:02d}.zip"
            out_path = os.path.join(ERA5_DIR, fname)
            label    = f"{year} Bulan {m1:02d}-{m2:02d}"

            if os.path.exists(out_path):
                size_mb = os.path.getsize(out_path) / 1024 / 1024
                print(f"  {label}: sudah ada ({size_mb:.1f} MB), dilewati.")
                downloaded.append(out_path)
                continue

            print(f"  {label}: mengunduh...", end=" ", flush=True)
            try:
                req = make_request(year, m1, m2)
                client.retrieve(DATASET, req).download(out_path)
                size_mb = os.path.getsize(out_path) / 1024 / 1024
                print(f"OK ({size_mb:.1f} MB)")
                downloaded.append(out_path)
            except Exception as e:
                err = str(e).split("\n")[0]  # ambil baris pertama saja
                print(f"GAGAL — {err}")
                failed.append(label)

    print()
    print("=" * 65)
    print(f"[OK]   Berhasil : {len(downloaded)} dari {total} batch")
    if failed:
        print(f"[WARN] Gagal   : {len(failed)} batch")
        for f in failed:
            print(f"         - {f}")
    print("=" * 65)
    return len(downloaded) > 0


def convert_to_csv():
    """Gabungkan semua file ZIP/NC menjadi satu CSV bersih."""
    try:
        import xarray as xr
    except ImportError:
        print("[ERROR] Jalankan: pip install xarray netCDF4")
        return

    zip_files = sorted(glob.glob(os.path.join(ERA5_DIR, "*.zip")))
    if not zip_files:
        print("[ERROR] Tidak ada file ZIP di:", ERA5_DIR)
        return

    print(f"\n[STEP 2] Menggabungkan {len(zip_files)} file ZIP ke CSV...")
    extract_dir = os.path.join(ERA5_DIR, "_temp_nc")
    os.makedirs(extract_dir, exist_ok=True)

    nc_files = []
    for i, zf in enumerate(zip_files):
        with zipfile.ZipFile(zf, "r") as z:
            for member in z.namelist():
                if member.endswith(".nc"):
                    extracted_path = z.extract(member, extract_dir)
                    new_path = os.path.join(extract_dir, f"{i:03d}_{member}")
                    if os.path.exists(new_path):
                        os.remove(new_path)
                    os.rename(extracted_path, new_path)
                    nc_files.append(new_path)

    def drop_expver(ds):
        if "expver" in ds.variables:
            if "expver" in ds.dims:
                # Merge the expver=1 and expver=5 by taking the non-nan value
                ds = ds.mean(dim="expver", skipna=True)
            else:
                ds = ds.drop_vars("expver")
        return ds

    print(f"  Membaca {len(nc_files)} file NetCDF...", end=" ", flush=True)
    ds      = xr.open_mfdataset(nc_files, combine="by_coords", preprocess=drop_expver)
    ds_mean = ds.mean(dim=["latitude", "longitude"])
    df      = ds_mean.to_dataframe().reset_index()
    print("OK")

    # Konversi satuan
    if "t2m" in df.columns:
        df["suhu_2m_C"]        = df.pop("t2m") - 273.15
    if "d2m" in df.columns:
        df["titik_embun_C"]    = df.pop("d2m") - 273.15
    if "sp" in df.columns:
        df["tekanan_hPa"]      = df.pop("sp") / 100
    if "tp" in df.columns:
        df["curah_hujan_mm"]   = df.pop("tp") * 1000

    # Hitung kecepatan & arah angin
    if "u10" in df.columns and "v10" in df.columns:
        df["kecepatan_angin_kmh"] = np.sqrt(df["u10"]**2 + df["v10"]**2) * 3.6
        df["arah_angin_derajat"]  = np.degrees(np.arctan2(-df["u10"], -df["v10"])) % 360
        df.drop(columns=["u10", "v10"], inplace=True)

    # Hitung Kelembapan Relatif dari Suhu & Titik Embun
    if "suhu_2m_C" in df.columns and "titik_embun_C" in df.columns:
        T, Td = df["suhu_2m_C"], df["titik_embun_C"]
        df["kelembapan_persen"] = 100 * (
            np.exp((17.625 * Td) / (243.04 + Td)) /
            np.exp((17.625 * T)  / (243.04 + T))
        )

    # Rename
    rename = {
        "valid_time" : "waktu",
        "blh"        : "tinggi_lapisan_batas_m",
        "tcc"        : "tutupan_awan_01",
        "tco3"       : "ozon_kolom_kg_m2",
        "tcwv"       : "uap_air_kolom_kg_m2",
    }
    df.rename(columns=rename, inplace=True)
    df.sort_values("waktu", inplace=True)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

    print()
    print("=" * 65)
    print(f"[OK] CSV tersimpan            : {OUTPUT_CSV}")
    print(f"     Total baris              : {len(df):,} jam")
    print(f"     Kolom                    : {len(df.columns)}")
    if "suhu_2m_C"              in df.columns: print(f"     Suhu rata-rata           : {df['suhu_2m_C'].mean():.1f} C")
    if "kelembapan_persen"      in df.columns: print(f"     Kelembapan rata-rata      : {df['kelembapan_persen'].mean():.1f}%")
    if "kecepatan_angin_kmh"    in df.columns: print(f"     Angin rata-rata           : {df['kecepatan_angin_kmh'].mean():.1f} km/h")
    if "tinggi_lapisan_batas_m" in df.columns: print(f"     Lap. batas rata-rata      : {df['tinggi_lapisan_batas_m'].mean():.0f} m")
    if "curah_hujan_mm"         in df.columns: print(f"     Total curah hujan 5 tahun : {df['curah_hujan_mm'].sum():.0f} mm")
    print("=" * 65)
    print()
    print("SELESAI! Dataset cuaca ERA5 siap digunakan.")
    print("Langkah berikutnya: gabungkan dengan data PM2.5")
    print("  python src/scripts/preprocess_data.py")
    print("=" * 65)

    import shutil
    shutil.rmtree(extract_dir, ignore_errors=True)


if __name__ == "__main__":
    success = download_all()
    if success:
        convert_to_csv()
