"""
=============================================================
 SKRIP: Unduh Data Cuaca BMKG Bandung via Meteostat (WMO ID)
 Sumber  : Meteostat — menggunakan kode WMO stasiun resmi BMKG
 Stasiun : Husein Sastranegara, Bandung (WMO: 96781, ICAO: WICC)
 Elevasi : 812 mdpl | Koordinat: -6.902, 107.576
 Periode : 2020-01-01 s.d. 2024-12-31
 Output  : data/raw/bmkg_bandung_hourly_2020_2024.csv
           data/raw/bmkg_bandung_daily_2020_2024.csv
=============================================================
CARA PAKAI:
  python src/scripts/download_bmkg_meteostat.py
=============================================================
"""

import os
import sys
from datetime import datetime

import pandas as pd
from meteostat import hourly as ms_hourly, daily as ms_daily
from meteostat import config as ms_config

sys.stdout.reconfigure(encoding="utf-8")

# ==============================================================
# KONFIGURASI
# ==============================================================
# Kode WMO resmi BMKG Bandung (Husein Sastranegara)
WMO_STATION_ID = "96781"

PERIOD_START   = datetime(2020, 1, 1)
PERIOD_END     = datetime(2024, 12, 31)

OUTPUT_DIR     = "data/raw"
OUTPUT_HOURLY  = os.path.join(OUTPUT_DIR, "bmkg_bandung_hourly_2020_2024.csv")
OUTPUT_DAILY   = os.path.join(OUTPUT_DIR, "bmkg_bandung_daily_2020_2024.csv")

# Izinkan request data panjang (> 3 tahun)
ms_config.block_large_requests = False
# ==============================================================

RENAME_HOURLY = {
    "temp" : "suhu_2m_C",
    "dwpt" : "titik_embun_C",
    "rhum" : "kelembapan_persen",
    "prcp" : "curah_hujan_mm",
    "snow" : "salju_mm",
    "wdir" : "arah_angin_derajat",
    "wspd" : "kecepatan_angin_kmh",
    "wpgt" : "angin_kencang_kmh",
    "pres" : "tekanan_hPa",
    "tsun" : "durasi_matahari_min",
    "coco" : "kode_cuaca",
}

RENAME_DAILY = {
    "tavg" : "suhu_rata_C",
    "tmin" : "suhu_min_C",
    "tmax" : "suhu_maks_C",
    "prcp" : "curah_hujan_mm",
    "snow" : "salju_mm",
    "wdir" : "arah_angin_derajat",
    "wspd" : "kecepatan_angin_kmh",
    "wpgt" : "angin_kencang_kmh",
    "pres" : "tekanan_hPa",
    "tsun" : "durasi_matahari_min",
}


def safe_fetch(ts):
    """Aman memanggil fetch() — kembalikan DataFrame kosong jika None."""
    if ts is None:
        return pd.DataFrame()
    result = ts.fetch()
    return result if result is not None else pd.DataFrame()


def download():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 60)
    print("Mengunduh data BMKG Bandung via Meteostat")
    print(f"Stasiun : WMO {WMO_STATION_ID} — Husein Sastranegara, Bandung")
    print(f"Periode : {PERIOD_START.date()} s.d. {PERIOD_END.date()}")
    print("=" * 60)

    # ---- DATA PER JAM — unduh per tahun agar stabil ----
    print("\n[1/2] Data per JAM (Hourly)...")
    frames_hourly = []
    for year in range(2020, 2025):
        y_start = datetime(year, 1, 1)
        y_end   = datetime(year, 12, 31, 23, 59)
        print(f"  Tahun {year}...", end=" ", flush=True)
        try:
            ts = ms_hourly(WMO_STATION_ID, y_start, y_end)
            df = safe_fetch(ts)
            if not df.empty:
                frames_hourly.append(df)
                pct = df["temp"].notna().mean() * 100
                print(f"OK — {len(df):,} baris ({pct:.0f}% terisi)")
            else:
                print("KOSONG")
        except Exception as e:
            print(f"ERROR: {e}")

    if frames_hourly:
        df_hourly = pd.concat(frames_hourly)
        df_hourly = df_hourly.rename(columns=RENAME_HOURLY)
        df_hourly.to_csv(OUTPUT_HOURLY, encoding="utf-8")
        n         = len(df_hourly)
        pct_suhu  = df_hourly["suhu_2m_C"].notna().mean() * 100
        print(f"\n  [SAVED] {OUTPUT_HOURLY}")
        print(f"  Total   : {n:,} jam | Kelengkapan: {pct_suhu:.1f}%")
    else:
        print("\n  [WARN] Tidak ada data hourly dari stasiun WMO 96781.")
        print("         Kemungkinan Meteostat belum memiliki data historis stasiun ini.")

    # ---- DATA HARIAN ----
    print("\n[2/2] Data HARIAN (Daily)...")
    try:
        ts_daily = ms_daily(WMO_STATION_ID, PERIOD_START, PERIOD_END)
        df_daily = safe_fetch(ts_daily)
    except Exception as e:
        print(f"  ERROR: {e}")
        df_daily = pd.DataFrame()

    if not df_daily.empty:
        df_daily = df_daily.rename(columns=RENAME_DAILY)
        df_daily.to_csv(OUTPUT_DAILY, encoding="utf-8")
        n        = len(df_daily)
        pct_suhu = df_daily["suhu_rata_C"].notna().mean() * 100
        print(f"  [SAVED] {OUTPUT_DAILY}")
        print(f"  Total   : {n:,} hari | Kelengkapan: {pct_suhu:.1f}%")

        # Statistik ringkas
        print()
        print("  --- Statistik Ringkas ---")
        if "suhu_rata_C" in df_daily.columns:
            print(f"  Suhu rata-rata   : {df_daily['suhu_rata_C'].mean():.1f} C")
        if "curah_hujan_mm" in df_daily.columns:
            print(f"  Hujan total      : {df_daily['curah_hujan_mm'].sum():.0f} mm/5thn")
        if "kecepatan_angin_kmh" in df_daily.columns:
            print(f"  Angin rata-rata  : {df_daily['kecepatan_angin_kmh'].mean():.1f} km/h")
    else:
        print("  [WARN] Data daily juga kosong.")
        print("         Stasiun WMO 96781 mungkin belum terintegrasi di Meteostat.")
        print("         Saran: gunakan Open-Meteo sebagai alternatif (ERA5 reanalysis).")
        print("         Jalankan: python src/scripts/download_cuaca_openmeteo.py")

    print()
    print("=" * 60)
    print("SELESAI.")
    print("=" * 60)


if __name__ == "__main__":
    download()
