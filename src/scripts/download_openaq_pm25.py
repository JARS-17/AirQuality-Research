"""
=============================================================
 SKRIP OTOMATISASI: Unduh Data PM2.5 Bandung via OpenAQ API v3
 Sumber   : OpenAQ (https://openaq.org) — Data terbuka gratis
 Lokasi   : Kota Bandung (radius 30 km dari pusat kota)
 Periode  : 2020-01-01 s.d. 2024-12-31
 Output   : data/raw/openaq_pm25_bandung_2020_2024.csv
=============================================================
CARA PAKAI:
1. Daftar API Key gratis di: https://explore.openaq.org/register
2. Isi OPENAQ_API_KEY di bagian KONFIGURASI di bawah
3. Install library: pip install requests pandas
4. Jalankan: python src/scripts/download_openaq_pm25.py
"""

import os
import time
import requests
import pandas as pd
from datetime import datetime, timedelta

# ==============================================================
# KONFIGURASI — ISI API KEY GRATIS DARI OPENAQ
# ==============================================================
OPENAQ_API_KEY = "GANTI_DENGAN_API_KEY_OPENAQ"
# Daftar gratis di: https://explore.openaq.org/register
# ==============================================================

BANDUNG_LAT    = -6.9147
BANDUNG_LON    = 107.6098
RADIUS_KM      = 30         # radius pencarian sensor dari pusat Bandung
PARAMETER      = "pm25"
DATE_FROM      = "2020-01-01"
DATE_TO        = "2024-12-31"
OUTPUT_DIR     = "data/raw"
OUTPUT_FILE    = os.path.join(OUTPUT_DIR, "openaq_pm25_bandung_2020_2024.csv")

BASE_URL       = "https://api.openaq.org/v3"


def get_locations():
    """Cari semua sensor PM2.5 dalam radius Bandung."""
    url = f"{BASE_URL}/locations"
    params = {
        "coordinates": f"{BANDUNG_LAT},{BANDUNG_LON}",
        "radius": RADIUS_KM * 1000,  # API menerima meter
        "parameters_id": 2,           # 2 = pm25 di OpenAQ v3
        "limit": 100,
    }
    headers = {"X-API-Key": OPENAQ_API_KEY}
    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data.get("results", [])


def get_measurements(location_id, date_from, date_to):
    """Unduh data pengukuran dari satu sensor (location_id)."""
    url = f"{BASE_URL}/locations/{location_id}/measurements"
    params = {
        "date_from"    : f"{date_from}T00:00:00Z",
        "date_to"      : f"{date_to}T23:59:59Z",
        "parameters_id": 2,
        "limit"        : 10000,
    }
    headers = {"X-API-Key": OPENAQ_API_KEY}
    all_results = []
    page = 1

    while True:
        params["page"] = page
        try:
            r = requests.get(url, params=params, headers=headers, timeout=30)
            r.raise_for_status()
            results = r.json().get("results", [])
            if not results:
                break
            all_results.extend(results)
            if len(results) < 10000:
                break
            page += 1
            time.sleep(0.5)   # hormati rate-limit API
        except Exception as e:
            print(f"      Error: {e} — melewati halaman ini.")
            break

    return all_results


def download_openaq():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if OPENAQ_API_KEY == "GANTI_DENGAN_API_KEY_OPENAQ":
        print("=" * 60)
        print("ERROR: Anda belum mengisi OPENAQ_API_KEY!")
        print("Langkah:")
        print("1. Buka: https://explore.openaq.org/register")
        print("2. Daftar gratis dengan email kampus Anda")
        print("3. Salin API Key dari halaman profil Anda")
        print("4. Tempel di bagian KONFIGURASI skrip ini")
        print("=" * 60)
        return

    print("Mencari stasiun sensor PM2.5 di sekitar Bandung...")
    locations = get_locations()

    if not locations:
        print("⚠️  Tidak ada sensor PM2.5 yang ditemukan di OpenAQ untuk area Bandung.")
        print("   Coba gunakan sumber alternatif: IQAir atau data DLHK Bandung.")
        return

    print(f"✅ Ditemukan {len(locations)} sensor:")
    for loc in locations:
        print(f"   - ID {loc['id']}: {loc.get('name', 'N/A')} "
              f"({loc.get('country', {}).get('code', 'N/A')})")

    print()
    all_data = []
    for loc in locations:
        loc_id   = loc["id"]
        loc_name = loc.get("name", "Unknown")
        print(f"Mengunduh data dari sensor: {loc_name} (ID: {loc_id}) ...")

        measurements = get_measurements(loc_id, DATE_FROM, DATE_TO)
        if measurements:
            for m in measurements:
                all_data.append({
                    "datetime"   : m.get("date", {}).get("utc", ""),
                    "pm25_ugm3"  : m.get("value", None),
                    "unit"       : m.get("unit", "µg/m³"),
                    "sensor_id"  : loc_id,
                    "sensor_name": loc_name,
                    "latitude"   : loc.get("coordinates", {}).get("latitude"),
                    "longitude"  : loc.get("coordinates", {}).get("longitude"),
                })
            print(f"   ✅ {len(measurements):,} titik data diperoleh.")
        else:
            print(f"   ⚠️  Tidak ada data untuk sensor ini.")
        time.sleep(1)

    if not all_data:
        print("\n⚠️  Tidak ada data PM2.5 yang berhasil diunduh.")
        return

    df = pd.DataFrame(all_data)
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)

    # Hapus nilai negatif/tidak valid
    df = df[df["pm25_ugm3"] >= 0]

    df.to_csv(OUTPUT_FILE, index=False)

    print()
    print("=" * 60)
    print(f"✅ Data PM2.5 berhasil disimpan!")
    print(f"   File    : {OUTPUT_FILE}")
    print(f"   Jumlah  : {len(df):,} baris pengukuran")
    print(f"   Rentang : {df['datetime'].min()} s.d. {df['datetime'].max()}")
    print(f"   Rata-rata PM2.5: {df['pm25_ugm3'].mean():.2f} µg/m³")
    print()
    print("LANGKAH SELANJUTNYA:")
    print("   Jalankan: python src/scripts/preprocess_data.py")
    print("=" * 60)


if __name__ == "__main__":
    download_openaq()
