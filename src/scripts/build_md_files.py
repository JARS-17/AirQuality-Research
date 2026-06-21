import os
import re

# Direktori tujuan
out_dir = r"D:\Kuliah Praktik\KP BRIN\reports\literature_review"
os.makedirs(out_dir, exist_ok=True)

# Data Jurnal 1-6 (Hardcoded dari input user)
jurnal_1_6 = """
## JURNAL 1
**"Improving the Forecast Accuracy of PM2.5 Using SETAR-Tree Method: Case Study in Jakarta, Indonesia"**
*Safira, Kuswanto & Ahsan — Atmosphere, 2025*
---
### ✅ Kekuatan Utama
* **Relevansi & Urgensi Topik:** Topik sangat relevan. Jakarta sebagai salah satu kota paling terpolusi di dunia menjadikan penelitian ini punya nilai praktis tinggi.
* **Kebaruan Metode:** Penggunaan **SETAR-Tree** untuk prediksi PM2.5 adalah kontribusi yang genuinely baru.
* **Metodologi yang Terstruktur:** Alur metodologi cukup sistematis: uji **stasioneritas** → identifikasi **ARIMA** → pembangunan **LSTM** → pembangunan **SETAR-Tree** → evaluasi komparatif.
* **Hasil yang Jelas & Terukur:** Perbandingan **RMSE** dan **MAPE** antara dua model disajikan dengan rapi.

### ⚠️ Kelemahan & Catatan Kritis
* **Keterbatasan Data:** Data hanya berasal dari **satu stasiun monitoring** selama sekitar 23 bulan.
* **LSTM Belum Dioptimalkan:** Tidak ada tuning lebih lanjut seperti **learning rate scheduling**, **regularization**, atau perbandingan dengan varian LSTM lain.
* **Tidak Ada Variabel Eksogen:** Kedua model hanya menggunakan data univariat PM2.5 tanpa faktor meteorologi.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi:** Minor Revision

===
## JURNAL 2
**"A Comparison of LSTM and BiLSTM for Forecasting the Air Pollution Index and Meteorological Conditions in Jakarta"**
*Handhayani, Lewenusa, Herwindiati & Hendryli — Universitas Tarumanagara*
---
### ✅ Kekuatan Utama
* **Cakupan Data yang Luas:** Dataset mencakup **12 tahun (2010–2021)** dengan 4.383 sampel.
* **Desain Eksperimen yang Menarik:** Membagi eksperimen ke dalam skenario sebelum dan saat pandemi **Covid-19**.
* **Multivariate Forecasting:** Mencakup PM10, SO2, CO, O3, NO2, suhu, kelembapan, dll secara bersamaan.

### ⚠️ Kelemahan & Catatan Kritis
* **Kontribusi Ilmiah yang Lemah:** Kesimpulan utama tidak ada perbedaan signifikan antara **LSTM** dan **BiLSTM**.
* **Arsitektur Model Terlalu Sederhana:** Tidak ada proses tuning dan tidak ada **ablation study**.
* **Penggunaan Softmax Tidak Tepat:** Penggunaan **Softmax** pada output layer untuk prediksi nilai kontinu adalah **kesalahan metodologis** serius.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi:** Major Revision

===
## JURNAL 3
**"Air Quality Estimation Using LSTM and An Approach for Data Processing Techniques"**
*Ton-Thien, Nguyen, Le & Duong — MediaEval 2021, CEUR-WS*
---
### ✅ Kekuatan Utama
* **Pendekatan Preprocessing yang Praktis:** Penanganan **missing values** secara bertingkat menggunakan **mean imputation** lalu **XGBoost**.
* **Cakupan Multi-Negara:** Dataset mencakup tiga negara (Brunei, Singapura, Thailand).
* **Perbandingan Tiga Varian LSTM:** Membandingkan LSTM standar, **Bi-LSTM**, dan **Stacked LSTM**.

### ⚠️ Kelemahan & Catatan Kritis
* **Bukan Jurnal Utama:** Ini adalah paper workshop kompetisi, bukan artikel peer-review ketat.
* **Overfitting yang Parah:** Indikasi **overfitting** sangat serius (RMSE melonjak 3x lipat pada test set).
* **Tidak Ada Strategi Anti-Overfitting:** Tidak disebutkan penggunaan **dropout**, **early stopping**, atau **L2 regularization**.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi:** Workshop Only

===
## JURNAL 4
**"Assessing Low-Cost Sensor for Characterizing Temporal Variation of PM2.5 in Bandung, Indonesia"**
*Kurniawati et al. — Kuwait Journal of Science, 2025*
---
### ✅ Kekuatan Utama
* **Relevansi Lokal yang Tinggi:** Evaluasi sensor **PurpleAir PA-II** untuk konteks Indonesia (Bandung) selama 12 bulan penuh.
* **Desain Co-Location yang Solid:** Penggunaan **SuperSASS** sebagai referensi standar EPA.
* **Analisis Temporal yang Komprehensif:** Menganalisis variasi **diurnal**, mingguan, dan musiman.

### ⚠️ Kelemahan & Catatan Kritis
* **Hanya Satu Lokasi Sampling:** Membatasi representasi spasial secara signifikan.
* **PA-II Overestimasi Konsisten 24%:** Angka overestimasi cukup besar tanpa persamaan koreksi spesifik lokal.
* **Keterbatasan Sensor RH:** Sensor konsisten mencatat kelembaban (RH) lebih rendah dari referensi BPS.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi:** Minor Revision

===
## JURNAL 5
**"Shapley Additive Explanations Interpretation of the XGBoost Model in Predicting Air Quality in Jakarta"**
*Iffadah, Trimono & Prasetya — Jurnal Riset Informatika, 2025*
---
### ✅ Kekuatan Utama
* **Integrasi XAI yang Tepat Sasaran:** Menggabungkan **XGBoost** dengan **SHAP** untuk menjawab kebutuhan interpretabilitas (*explainability*).
* **Performa Model yang Kuat:** MAPE **4.44%** sangat akurat mengalahkan LSTM.
* **Preprocessing yang Dipikirkan dengan Baik:** Penggunaan **KNN Imputer** jauh lebih tepat dibanding mean imputation.

### ⚠️ Kelemahan & Catatan Kritis
* **Data Hanya Satu Kota:** Generalisasi ke kota lain tidak dapat dilakukan langsung.
* **Target Variabel Membingungkan:** Model memprediksi PM2.5 tapi diklaim memprediksi kualitas udara keseluruhan.
* **Split Data Tidak Konsisten:** Mengandalkan **90:10** split yang rentan overfitting tanpa R-squared score.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi:** Minor Revision

===
## JURNAL 6
**"Deep Learning for Air Quality Forecasts: a Review"**
*Liao, Zhu, Wu, Pan, Tang & Wang — Current Pollution Reports, Springer, 2020*
---
### ✅ Kekuatan Utama
* **Paper Fondasi Wajib:** Roadmap terbaik untuk memahami lanskap **deep learning** dalam prediksi kualitas udara.
* **Cakupan Arsitektur yang Komprehensif:** Memetakan ekosistem DL: **RNN, LSTM, CNN, SAE, STDL**.
* **Identifikasi Tantangan:** Mengidentifikasi masalah **black-box** dan ketiadaan dataset standar.

### ⚠️ Kelemahan & Catatan Kritis
* **Sedikit Outdated (2020):** Tidak ada pembahasan tentang model berbasis **Transformer** atau *Attention mechanism*.
* **Tidak Ada Studi dari Asia Tenggara:** Menunjukkan kesenjangan geografis yang besar (didominasi China/US).
* **Aspek Low-Cost Sensor Tidak Dibahas:** Fokus murni pada stasiun pemantauan resmi dan satelit.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi:** Accept
"""

def write_journal(idx, title, content):
    filename = f"Review_{idx:02d}.md"
    path = os.path.join(out_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {filename}")

# Parse Jurnal 1-6
blocks = jurnal_1_6.split("===")
for block in blocks:
    if "## JURNAL" in block:
        idx_match = re.search(r"## JURNAL\s+(\d+)", block)
        if idx_match:
            idx = int(idx_match.group(1))
            write_journal(idx, f"Jurnal {idx}", block)

# Parse Jurnal 7-11 dan 12-22 dari artifacts
artifact_dir = r"C:\Users\ginda fajar\.gemini\antigravity\brain\d3759a5a-0707-4d2d-8e31-eb0a26f53461"
files_to_read = ["Ulasan_Kritis_7_11.md", "Ulasan_Kritis_12_22.md"]

for fname in files_to_read:
    fpath = os.path.join(artifact_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Split by ## JURNAL
        chunks = content.split("## JURNAL")
        for chunk in chunks[1:]: # skip preamble
            chunk = "## JURNAL" + chunk
            idx_match = re.search(r"## JURNAL\s+(\d+)", chunk)
            if idx_match:
                idx = int(idx_match.group(1))
                # Bersihkan separator markdown ---
                chunk = chunk.replace("---", "").strip()
                # Ganti ✅ Kekuatan dengan ✅ Kekuatan Utama
                chunk = chunk.replace("### ✅ Kekuatan", "### ✅ Kekuatan Utama")
                write_journal(idx, f"Jurnal {idx}", chunk)

print("Semua 22 file MD berhasil di-generate!")
