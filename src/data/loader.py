"""
src/data/loader.py
Modul untuk loading dan pengumpulan data kualitas udara dari berbagai sumber.
"""

import pandas as pd
import numpy as np
import requests
from pathlib import Path

# Path root project
ROOT_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DATA_DIR = ROOT_DIR / "data" / "processed"
EXTERNAL_DATA_DIR = ROOT_DIR / "data" / "external"


def load_local_csv(filename: str, folder: str = "raw") -> pd.DataFrame:
    """
    Load data CSV dari folder lokal.

    Args:
        filename: Nama file CSV
        folder: Subfolder di dalam data/ ('raw', 'processed', 'external')

    Returns:
        DataFrame pandas
    """
    folder_map = {
        "raw": RAW_DATA_DIR,
        "processed": PROCESSED_DATA_DIR,
        "external": EXTERNAL_DATA_DIR,
    }
    path = folder_map[folder] / filename
    print(f"[INFO] Loading data dari: {path}")
    return pd.read_csv(path, parse_dates=True)


def fetch_openaq(city: str = "Bandung", parameter: str = "pm25", limit: int = 1000) -> pd.DataFrame:
    """
    Ambil data kualitas udara dari OpenAQ API (gratis, open source).

    Args:
        city: Nama kota (default: Bandung)
        parameter: Parameter polutan ('pm25', 'pm10', 'no2', 'o3', 'co', 'so2')
        limit: Jumlah data yang diambil

    Returns:
        DataFrame hasil query OpenAQ

    Referensi: https://api.openaq.org/v2/
    """
    url = "https://api.openaq.org/v2/measurements"
    params = {
        "city": city,
        "parameter": parameter,
        "limit": limit,
        "order_by": "datetime",
        "sort": "desc",
    }

    print(f"[INFO] Fetching data dari OpenAQ: kota={city}, parameter={parameter}")
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise ConnectionError(f"[ERROR] Gagal ambil data OpenAQ. Status: {response.status_code}")

    data = response.json()
    results = data.get("results", [])
    df = pd.json_normalize(results)
    print(f"[INFO] Berhasil mengambil {len(df)} data dari OpenAQ")
    return df


def load_bmkg_data(filepath: str) -> pd.DataFrame:
    """
    Load dan standarisasi data cuaca dari BMKG.
    Format BMKG umumnya CSV dengan header tidak standar.

    Args:
        filepath: Path ke file CSV BMKG

    Returns:
        DataFrame dengan kolom yang sudah distandarisasi
    """
    df = pd.read_csv(filepath, skiprows=7, encoding="latin-1")  # BMKG biasa punya header rows

    # Rename kolom umum BMKG
    rename_map = {
        "Tanggal": "date",
        "Tn": "temp_min",
        "Tx": "temp_max",
        "Tavg": "temp_avg",
        "RH_avg": "humidity_avg",
        "RR": "rainfall",
        "ss": "sunshine_hours",
        "ff_avg": "wind_speed_avg",
        "ddd_x": "wind_direction",
        "ff_x": "wind_speed_max",
    }
    df = df.rename(columns=rename_map)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df


def load_klhk_aqi(filepath: str) -> pd.DataFrame:
    """
    Load data AQI dari KLHK (Kementerian Lingkungan Hidup dan Kehutanan).
    Data ISPU (Indeks Standar Pencemar Udara) dari stasiun monitoring resmi.

    Args:
        filepath: Path ke file data KLHK

    Returns:
        DataFrame dengan data AQI terstandarisasi
    """
    df = pd.read_excel(filepath)

    # Kolom standar ISPU
    expected_cols = ["Tanggal", "PM10", "PM25", "SO2", "CO", "O3", "NO2", "ISPU", "Kategori"]
    df.columns = [col.strip() for col in df.columns]

    rename_map = {
        "Tanggal": "date",
        "PM10": "pm10",
        "PM25": "pm25",
        "SO2": "so2",
        "CO": "co",
        "O3": "o3",
        "NO2": "no2",
        "ISPU": "aqi",
        "Kategori": "category",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df


if __name__ == "__main__":
    # Quick test
    print("Data loader siap digunakan.")
    print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")
    print(f"PROCESSED_DATA_DIR: {PROCESSED_DATA_DIR}")
