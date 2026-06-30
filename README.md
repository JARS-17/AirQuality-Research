# 🌫️ Air Quality Research — KP BRIN 2026
### Prediksi Konsentrasi PM2.5 di Cekungan Bandung Menggunakan Deep Learning dan Explainable AI

> **Peneliti:** Ginda Fajar Riadi Marpaung  
> **Program Studi:** Sains Data — Institut Teknologi Sumatera (ITERA)  
> **Institusi:** Badan Riset dan Inovasi Nasional (BRIN)  
> **Pembimbing:** Rumadi, S.T., M.T.  
> **Topik:** Fundamental AI dan Machine Learning untuk Analisis Kualitas Udara  
> **Tahun:** 2026

---

## 📌 Deskripsi Proyek

Proyek ini merupakan penelitian Kerja Praktik (KP) di BRIN yang bertujuan untuk membangun model prediksi konsentrasi PM2.5 di kawasan Cekungan Bandung menggunakan pendekatan Machine Learning dan Deep Learning, serta menganalisis faktor-faktor meteorologi yang paling berpengaruh terhadap polusi udara menggunakan metode Explainable AI (SHAP).

**Polutan yang dikaji:** PM2.5 (Particulate Matter ≤ 2.5 µm)  
**Wilayah studi:** Cekungan Bandung, Jawa Barat, Indonesia  
**Periode data:** November 2022 – November 2023 (1 siklus musiman penuh, resolusi per jam)  
**Jumlah observasi:** ±8.760 titik data (*hourly*)

---

## 📊 Sumber Data

| Sumber Data | Deskripsi | Format |
|-------------|-----------|--------|
| **Sensor PurpleAir** | Konsentrasi PM2.5 per jam dari sensor *low-cost* di Cekungan Bandung | CSV (`hourly_all_sensors.csv`) |
| **ECMWF Copernicus ERA5** | Data reanalisis meteorologi (suhu, kelembapan, kecepatan angin, curah hujan, tekanan udara, tutupan awan, tinggi lapisan batas atmosfer) | CSV (`era5_bandung_2022_2026.csv`) |

---

## 🗂️ Struktur Proyek

```
AirQuality-Research/
│
├── 📁 data/
│   ├── raw/                # Dataset mentah (sensor PM2.5 & ERA5 meteorologi)
│   └── processed/          # Hasil preprocessing (train/val/test scaled, scaler)
│
├── 📁 notebooks/
│   ├── 01_exploratory/
│   │   └── 01_EDA_PM25_ERA5.ipynb              # Eksplorasi & visualisasi data
│   ├── 02_preprocessing/
│   │   └── 02_Preprocessing_FeatureEngineering.ipynb  # Pembersihan, feature engineering, split data
│   ├── 03_modeling/
│   │   ├── 03_Baseline_Models.ipynb            # Random Forest & XGBoost + GridSearch tuning
│   │   └── 04_LSTM_Model.ipynb                 # LSTM & BiLSTM + GridSearch tuning
│   ├── 04_interpretation/
│   │   └── 05_SHAP_Interpretation_LSTM.ipynb   # Analisis SHAP (feature importance & kausalitas)
│   └── PM25_Prediction_Bandung_Full.ipynb      # Notebook gabungan (seluruh pipeline dalam 1 file)
│
├── 📁 references/
│   ├── papers/             # 22 paper jurnal referensi (PDF, Q1/Q2 Scopus)
│   └── notes/              # Catatan teknis, penjelasan variabel, draf jurnal
│
├── 📁 reports/
│   ├── figures/            # Flowchart penelitian & grafik hasil
│   ├── literature_review/  # Critical review 22 jurnal (format markdown)
│   └── presentations/      # Slide presentasi & pemetaan literatur
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/JARS-17/AirQuality-Research.git
cd AirQuality-Research
```

### 2. Setup Environment
```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
```

### 3. Menjalankan Kode
Buka folder ini di VSCode atau Jupyter Notebook, lalu jalankan notebook secara berurutan mulai dari `01_EDA` hingga `05_SHAP`, atau langsung buka file gabungan `PM25_Prediction_Bandung_Full.ipynb` di folder `notebooks/`.

---

## 🧪 Metode & Pipeline

### Fase 1 — Eksplorasi Data (EDA)
- [x] Analisis distribusi dan tren musiman PM2.5
- [x] Korelasi PM2.5 dengan parameter meteorologi ERA5
- [x] Identifikasi pola diurnal (harian) dan musiman (kemarau vs hujan)

### Fase 2 — Preprocessing & Feature Engineering
- [x] Penanganan *missing values* (imputasi interpolasi)
- [x] Pembuatan fitur lag (1 jam, 24 jam) untuk autokorelasi PM2.5
- [x] *Cyclical encoding* waktu (sin/cos untuk jam dan bulan)
- [x] Penanda musim kemarau (`is_dry_season`)
- [x] Normalisasi MinMaxScaler & pembagian data kronologis 70/10/20

### Fase 3 — Baseline Models (Machine Learning Klasik)
- [x] Random Forest — Default & Tuned (GridSearchCV)
- [x] XGBoost — Default & Tuned (GridSearchCV)

### Fase 4 — Deep Learning Models
- [x] Stacked LSTM — Default (Early Stopping) & Tuned (Grid Search Manual)
- [x] Bidirectional LSTM — Default (Early Stopping) & Tuned (Grid Search Manual)
- [x] Transformasi *Sliding Window* 24 jam (Tensor 3D)

### Fase 5 — Explainable AI (Interpretasi Kausalitas)
- [x] SHAP KernelExplainer pada model DL terbaik
- [x] Peringkat signifikansi fitur meteorologi terhadap PM2.5
- [x] Analisis kontribusi relatif (%) setiap variabel prediktor

---

## 📈 Metrik Evaluasi

| Metrik | Deskripsi |
|--------|-----------|
| **RMSE** | Root Mean Square Error — mengukur rata-rata deviasi prediksi |
| **MAE** | Mean Absolute Error — rata-rata kesalahan absolut |
| **R²** | Coefficient of Determination — proporsi variansi yang dijelaskan model |

---

## 📚 Literature Review

Critical review terhadap **22 jurnal** Q1/Q2 Scopus & SINTA tersedia di folder [`reports/literature_review/`](./reports/literature_review/).

**Jurnal referensi utama:**
- Atmosphere (MDPI, Q2 Scopus)
- Science of the Total Environment (Elsevier, Q1 Scopus)
- Aerosol and Air Quality Research (Q2 Scopus)
- Environmental Pollution (Elsevier, Q1 Scopus)

**Target publikasi:**
- Jurnal Meteorologi dan Geofisika (JMG) — Puslitbang BMKG (SINTA 2, Gratis)

---

## 🗓️ Progress Penelitian

| Fase | Aktivitas | Status |
|------|-----------|--------|
| 1 | Literature review & Gap analysis (22 jurnal) | ✅ Selesai |
| 2 | Akuisisi data sensor PM2.5 & ERA5 meteorologi | ✅ Selesai |
| 3 | Preprocessing, feature engineering, split data | ✅ Selesai |
| 4 | Baseline model (RF & XGBoost) + GridSearch tuning | ✅ Selesai |
| 5 | Deep Learning (LSTM & BiLSTM) + GridSearch tuning | ✅ Selesai |
| 6 | Interpretasi SHAP & analisis kausalitas fitur | ✅ Selesai |
| 7 | Penulisan naskah jurnal publikasi (JMG BMKG) | 🔄 Sedang berjalan |

---

## 📜 Lisensi

Proyek ini dibuat untuk keperluan akademik dan penelitian.  
© 2026 Ginda Fajar Riadi Marpaung — ITERA × BRIN.

---

## 📬 Kontak

- **GitHub:** [@JARS-17](https://github.com/JARS-17)
- **Email:** ginda.123450103@student.itera.ac.id
- **Institusi:** Institut Teknologi Sumatera (ITERA)
- **Instansi Riset:** Badan Riset dan Inovasi Nasional (BRIN)
