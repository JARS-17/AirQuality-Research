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

Proyek ini merupakan penelitian Kerja Praktik (KP) di BRIN yang berfokus pada pengembangan model prediksi dan analisis kualitas udara berbasis pendekatan data science dan machine learning. Penelitian ini berfokus pada wilayah Indonesia (khususnya Jawa Barat/Cekungan Bandung) dengan memanfaatkan data sensor darat dan data reanalisis satelit.

**Polutan yang dikaji:** PM2.5  
**Metode utama:** Machine Learning, Deep Learning (LSTM), Explainable AI (SHAP)  
**Periode data:** 2022–2023 (1 Tahun Siklus Penuh, Resolusi Per Jam)

---

## 🗂️ Struktur Proyek

```
KP-BRIN-AirQuality/
│
├── 📁 data/
│   ├── raw/            # Data mentah dari sumber asli (ERA5, sensor in-situ)
│   └── processed/      # Data yang sudah dibersihkan, normalisasi, fitur waktu
│
├── 📁 notebooks/
│   └── PM25_Prediction_Bandung_Full.ipynb  # File Terpadu (EDA hingga SHAP)
│
├── 📁 reports/
│   ├── figures/            # Grafik & visualisasi hasil
│   ├── literature_review/  # Dokumen literature review & gap analysis
│   └── presentations/      # Slide presentasi
│
├── 📁 references/
│   ├── papers/         # Paper jurnal referensi pendukung (PDF)
│   └── notes/          # Catatan teknis & Draf Naskah Jurnal (JMG BMKG)
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
# Buat virtual environment
python -m venv venv

# Aktivasi (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Menjalankan Kode Utama
Buka aplikasi VSCode atau Jupyter Notebook Anda. Navigasikan ke dalam folder `notebooks/` lalu buka file tunggal **`PM25_Prediction_Bandung_Full.ipynb`**. 
Seluruh pemodelan dari tahap pembersihan data hingga pembuatan plot interpretasi (SHAP) dapat langsung dijalankan secara berurutan.

---

## 📊 Data Sources

| Sumber Data | Tipe | Status |
|-------------|------|--------|
| ECMWF Copernicus (ERA5) | Meteorologi Reanalisis (Angin, Suhu, Hujan, dll) | ✅ Selesai |
| Sensor PurpleAir | Kualitas Udara In-Situ (PM2.5) Cekungan Bandung | ✅ Selesai |

---

## 🧪 Metode & Model

### Fase 1 — Baseline Models
- [x] Random Forest Tuned (Hyperparameter GridSearch)
- [x] XGBoost Tuned (Hyperparameter GridSearch)

### Fase 2 — Deep Learning Models
- [x] Stacked LSTM (Long Short-Term Memory)
- [x] Bi-LSTM (Bidirectional LSTM)

### Fase 3 — Explainability
- [x] SHAP Values Analysis (Model Kausalitas & Pengaruh Fitur)
- [x] Ekstraksi Fitur Cuaca vs Polutan Masa Lalu

---

## 📈 Metrik Evaluasi

| Metrik | Deskripsi |
|--------|-----------|
| **RMSE** | Root Mean Square Error |
| **MAE** | Mean Absolute Error |
| **R²** | Coefficient of Determination |

---

## 📚 Literature Review

Dokumen *critical review* 22 jurnal Q1/Q2 Scopus beserta *Gap Analysis* tersedia di folder [`reports/literature_review/`](./reports/literature_review/).

**Jurnal utama yang menjadi Benchmark:**
- Atmospheric Environment (Elsevier, Q1)
- Atmosphere (MDPI, Q2)
- Science of the Total Environment (Elsevier, Q1)

**Target Publikasi Proyek Saat Ini:**
- **Jurnal Meteorologi dan Geofisika (JMG) - Puslitbang BMKG (SINTA 2)**

---

## 🗓️ Timeline Penelitian

| Fase Penelitian | Status |
|-----------|--------|
| Literature review & Gap analysis | ✅ Selesai |
| Akuisisi & Preprocessing data | ✅ Selesai |
| Feature engineering & Baseline model | ✅ Selesai |
| Model Deep Learning (LSTM, BiLSTM) | ✅ Selesai |
| XAI & Interpretasi kausalitas (SHAP) | ✅ Selesai |
| Penulisan naskah Jurnal Publikasi | 🔄 Sedang Berjalan |

---

## 📝 Cara Berkontribusi

Proyek ini adalah bagian dari penelitian Kerja Praktik. Segala bentuk diskusi dan masukan dapat disampaikan melalui menu [Issues](../../issues).

---

## 📜 Lisensi

Proyek ini dibuat secara khusus untuk keperluan akademik dan penelitian. © 2026 Ginda Fajar Riadi Marpaung — ITERA × BRIN.

---

## 📬 Kontak

- **GitHub:** [@JARS-17](https://github.com/JARS-17)
- **Email:** ginda.123450103@student.itera.ac.id  
- **Institusi:** Institut Teknologi Sumatera (ITERA)  
- **Instansi Riset:** Badan Riset dan Inovasi Nasional (BRIN)
