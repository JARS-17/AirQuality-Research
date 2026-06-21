"""
=============================================================
 SKRIP: Unduh Data Cuaca Bandung via Open-Meteo API
 Sumber  : Open-Meteo (https://open-meteo.com) — GRATIS, tanpa API key!
           Data berbasis ERA5 reanalysis resolusi tinggi (9km)
 Periode : 2020-01-01 s.d. 2024-12-31
 Output  : data/raw/openmeteo_cuaca_bandung_2020_2024.csv
=============================================================
CARA PAKAI:
  pip install openmeteo-requests requests-cache retry-requests pandas
  python src/scripts/download_cuaca_openmeteo.py
=============================================================
"""

import os
import sys
import requests
import pandas as pd
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================
# KONFIGURASI
# ==============================================================
BANDUNG_LAT  = -6.9147
BANDUNG_LON  = 107.6098

DATE_START   = "2020-01-01"
DATE_END     = "2024-12-31"

OUTPUT_DIR   = "data/raw"
OUTPUT_FILE  = os.path.join(OUTPUT_DIR, "openmeteo_cuaca_bandung_2020_2024.csv")

# Variabel cuaca yang diunduh (format Open-Meteo)
HOURLY_VARS = [
    "temperature_2m",                # Suhu udara 2m (C)
    "relative_humidity_2m",          # Kelembapan relatif (%)
    "dew_point_2m",                  # Titik embun (C)
    "precipitation",                 # Curah hujan (mm)
    "wind_speed_10m",                # Kecepatan angin 10m (km/h)
    "wind_direction_10m",            # Arah angin (derajat)
    "surface_pressure",              # Tekanan permukaan (hPa)
    "boundary_layer_height",         # Ketinggian lapisan batas (m) — penting untuk inversi suhu!
    "shortwave_radiation",           # Radiasi surya (W/m2)
    "cloud_cover",                   # Tutupan awan (%)
    "visibility",                    # Jarak pandang (m)
]
# ==============================================================


def download_openmeteo():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("Mengunduh data cuaca Bandung via Open-Meteo (ERA5)...")
    print(f"Koordinat : {BANDUNG_LAT}, {BANDUNG_LON}")
    print(f"Periode   : {DATE_START} s.d. {DATE_END}")
    print(f"Variabel  : {len(HOURLY_VARS)} variabel meteorologi")
    print("=" * 60)

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude"        : BANDUNG_LAT,
        "longitude"       : BANDUNG_LON,
        "start_date"      : DATE_START,
        "end_date"        : DATE_END,
        "hourly"          : ",".join(HOURLY_VARS),
        "timezone"        : "Asia/Jakarta",
        "wind_speed_unit" : "kmh",
        "precipitation_unit": "mm",
    }

    print("Menghubungi server Open-Meteo...", end=" ", flush=True)
    try:
        response = requests.get(url, params=params, timeout=120)
        response.raise_for_status()
        data = response.json()
        print("OK")
    except requests.exceptions.Timeout:
        print("TIMEOUT — coba jalankan ulang skrip ini.")
        return
    except requests.exceptions.RequestException as e:
        print(f"ERROR koneksi: {e}")
        return

    # Konversi ke DataFrame
    print("Memproses data...", end=" ", flush=True)
    hourly = data.get("hourly", {})
    if not hourly:
        print("ERROR: Tidak ada data dalam respons API.")
        return

    df = pd.DataFrame({"waktu": pd.to_datetime(hourly["time"])})
    rename_map = {
        "temperature_2m"         : "suhu_2m_C",
        "relative_humidity_2m"   : "kelembapan_persen",
        "dew_point_2m"           : "titik_embun_C",
        "precipitation"          : "curah_hujan_mm",
        "wind_speed_10m"         : "kecepatan_angin_kmh",
        "wind_direction_10m"     : "arah_angin_derajat",
        "surface_pressure"       : "tekanan_hPa",
        "boundary_layer_height"  : "tinggi_lapisan_batas_m",
        "shortwave_radiation"    : "radiasi_surya_Wm2",
        "cloud_cover"            : "tutupan_awan_persen",
        "visibility"             : "jarak_pandang_m",
    }
    for var in HOURLY_VARS:
        if var in hourly:
            col_name = rename_map.get(var, var)
            df[col_name] = hourly[var]

    df = df.set_index("waktu")

    # Simpan ke CSV
    df.to_csv(OUTPUT_FILE, encoding="utf-8")
    print("OK")

    # Statistik ringkas
    n_rows    = len(df)
    pct_suhu  = df["suhu_2m_C"].notna().mean() * 100
    rata_suhu = df["suhu_2m_C"].mean()
    rata_rh   = df["kelembapan_persen"].mean()
    rata_wind = df["kecepatan_angin_kmh"].mean()

    print()
    print("=" * 60)
    print(f"[OK] Data tersimpan : {OUTPUT_FILE}")
    print(f"     Total baris    : {n_rows:,} jam ({n_rows//24} hari)")
    print(f"     Kelengkapan    : {pct_suhu:.1f}%")
    print()
    print("     --- Statistik Ringkas Bandung 2020-2024 ---")
    print(f"     Rata-rata Suhu         : {rata_suhu:.1f} C")
    print(f"     Rata-rata Kelembapan   : {rata_rh:.1f}%")
    print(f"     Rata-rata Kec. Angin   : {rata_wind:.1f} km/h")
    print("=" * 60)
    print()
    print("LANGKAH SELANJUTNYA:")
    print("  Dapatkan data PM2.5 dari OpenAQ (butuh API key gratis)")
    print("  Daftar di: https://explore.openaq.org/register")
    print("  Lalu jalankan: python src/scripts/download_openaq_pm25.py")
    print("=" * 60)


if __name__ == "__main__":
    download_openmeteo()
