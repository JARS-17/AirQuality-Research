# 🌫️ Air Quality Research — KP BRIN 2026
### Prediksi Kualitas Udara berbasis Machine Learning & Data Science

> **Peneliti:** Ginda Fajar Riadi Marpaung  
> **Program Studi:** Sains Data — Institut Teknologi Sumatera (ITERA)  
> **Institusi:** Badan Riset dan Inovasi Nasional (BRIN)  
> **Pembimbing:** Rumadi, S.T., M.T.  
> **Topik:** Fundamental AI dan Machine Learning untuk Analisis Kualitas Udara  
> **Tahun:** 2026

---

## 📌 Deskripsi Proyek

Proyek ini merupakan penelitian Kerja Praktik (KP) di BRIN yang berfokus pada pengembangan model prediksi dan analisis kualitas udara berbasis pendekatan data science dan machine learning. Penelitian ini berfokus pada wilayah Indonesia (khususnya Jawa Barat/Bandung) dengan memanfaatkan data sensor dan satelit.

**Polutan yang dikaji:** PM2.5, PM10, AQI komposit  
**Metode utama:** Machine Learning, Deep Learning (LSTM), Explainable AI (SHAP)  
**Periode data:** 2019–2025

---

## 🗂️ Struktur Proyek

```
KP-BRIN-AirQuality/
│
├── 📁 data/
│   ├── raw/            # Data mentah dari sumber asli (BMKG, KLHK, sensor)
│   ├── processed/      # Data yang sudah dibersihkan & diproses
│   └── external/       # Data eksternal (satelit, cuaca, dll.)
│
├── 📁 notebooks/
│   ├── 01_exploratory/     # Eksplorasi & visualisasi awal data
│   ├── 02_preprocessing/   # Pembersihan, normalisasi, feature engineering
│   ├── 03_modeling/        # Pengembangan & training model ML/DL
│   └── 04_evaluation/      # Evaluasi, perbandingan model, XAI
│
├── 📁 src/
│   ├── data/           # Script pengumpulan & loading data
│   ├── features/       # Feature engineering & selection
│   ├── models/         # Implementasi model ML/DL
│   └── visualization/  # Fungsi plotting & visualisasi
│
├── 📁 reports/
│   ├── figures/            # Grafik & visualisasi hasil
│   ├── literature_review/  # Dokumen literature review & gap analysis
│   └── presentations/      # Slide presentasi
│
├── 📁 references/
│   ├── papers/         # Paper jurnal referensi (PDF)
│   └── notes/          # Catatan & ringkasan bacaan
│
├── 📁 config/          # File konfigurasi model & pipeline
├── 📁 docs/            # Dokumentasi teknis proyek
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 CHANGELOG.md
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
# Buat virtual environment
python -m venv venv

# Aktivasi (Windows)
venv\Scripts\activate

# Aktivasi (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Jalankan Notebook Eksplorasi
```bash
jupyter notebook notebooks/01_exploratory/
```

---

## 📊 Data Sources

| Sumber Data | Tipe | URL / Akses | Status |
|-------------|------|-------------|--------|
| BMKG Open Data | Meteorologi | bmkg.go.id | 🔄 Dalam proses |
| KLHK AQMS | Kualitas udara stasiun | iku.menlhk.go.id | 🔄 Dalam proses |
| NASA FIRMS | Data titik api/kebakaran | firms.modaps.eosdis.nasa.gov | 🔄 Dalam proses |
| Sentinel-5P (ESA) | Citra satelit NO₂, AQI | Copernicus Hub | 🔄 Dalam proses |
| OpenAQ | Sensor kualitas udara terbuka | openaq.org/api | 🔄 Dalam proses |

---

## 🧪 Metode & Model

### Fase 1 — Baseline Models
- [ ] Linear Regression
- [ ] Random Forest
- [ ] XGBoost / LightGBM

### Fase 2 — Deep Learning Models
- [ ] LSTM (Long Short-Term Memory)
- [ ] Bi-LSTM
- [ ] CNN-LSTM Hybrid

### Fase 3 — Explainability
- [ ] SHAP Values Analysis
- [ ] Feature Importance
- [ ] LIME Interpretation

---

## 📈 Metrik Evaluasi

| Metrik | Deskripsi |
|--------|-----------|
| **RMSE** | Root Mean Square Error |
| **MAE** | Mean Absolute Error |
| **R²** | Coefficient of Determination |
| **MAPE** | Mean Absolute Percentage Error |

---

## 📚 Literature Review

Dokumen literature review lengkap tersedia di [`reports/literature_review/`](./reports/literature_review/).

**Template yang digunakan:** `Template_LitReview_GapAnalysis_AirQuality.docx`  
**Status:** 🔄 Dalam pengerjaan (target: ≥ 20 paper)

**Jurnal utama yang dikaji:**
- Atmospheric Environment (Elsevier, Q1)
- Atmosphere (MDPI, Q2)
- Science of the Total Environment (Elsevier, Q1)
- IEEE Access (Q2)

---

## 🗓️ Timeline Penelitian

| Minggu | Aktivitas | Status |
|--------|-----------|--------|
| Minggu 1–2 | Literature review & gap analysis | 🔄 Berjalan |
| Minggu 3–4 | Pengumpulan & preprocessing data | ⏳ Belum mulai |
| Minggu 5–6 | Feature engineering & baseline model | ⏳ Belum mulai |
| Minggu 7–8 | Deep learning model (LSTM, hybrid) | ⏳ Belum mulai |
| Minggu 9–10 | XAI & interpretasi hasil | ⏳ Belum mulai |
| Minggu 11–12 | Penulisan laporan & presentasi akhir | ⏳ Belum mulai |

---

## 📝 Cara Berkontribusi

Proyek ini adalah proyek penelitian pribadi. Saran dan diskusi dapat disampaikan melalui [Issues](../../issues).

---

## 📜 Lisensi

Proyek ini untuk keperluan akademik dan penelitian. © 2026 Ginda Fajar Riadi Marpaung — ITERA × BRIN.

---

## 📬 Kontak

- **GitHub:** [@JARS-17](https://github.com/JARS-17)
- **Email:** ginda.123450103@student.itera.ac.id  
- **Institusi:** Institut Teknologi Sumatera (ITERA)  
- **Laboratorium:** Badan Riset dan Inovasi Nasional (BRIN)
