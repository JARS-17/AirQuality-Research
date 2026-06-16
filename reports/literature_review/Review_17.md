# Review Jurnal 17
**"Estimation of PM2.5 Concentration in DKI Jakarta from Sentinel-5P Imagery by Considering Meteorological Factors Using Random Forest Approach"**
*Rahmat Nur Rahman, Nur Mohammad Farda, and Ardhasena Sopaheluwakan — BIO Web of Conferences / ICoSIA, 2025*

---

### ✅ Kekuatan Utama

**Fusi Data Satelit dan Reanalisis**
Penelitian ini unggul dalam pemanfaatan data multi-sumber, mengintegrasikan data penginderaan jauh satelit **Sentinel-5P TropOMI** dengan data meteorologi (ERA5 Land) dalam rentang waktu yang cukup panjang (2021-2023).

**Pendekatan Regresi Spasial Non-Linear**
Penggunaan regresi spasial berbasis **Random Forest (RF)** sangat tepat untuk menangkap hubungan non-linear antar variabel lingkungan dari grid citra satelit ke titik pengukuran darat.

**Pemetaan Spasial Dinamis**
Model berhasil memetakan pola spasial secara visual ke dalam peta heat-map yang selaras dengan pergantian musim kemarau dan penghujan di Indonesia.

---

### ⚠️ Kelemahan & Catatan Kritis

**Validasi Stasiun Darat Sangat Terbatas**
Validasi spasial sangat terbatas karena hanya mengandalkan **8 stasiun pemantauan darat** di area metropolitan sebesar Jakarta. Titik sampel yang sedikit berisiko membuat model gagal menangkap variabilitas polusi mikro-lokal.

**Kehilangan Data Akibat Penghapusan Missing Values**
Penanganan *missing values* pada data satelit seringkali dilakukan dengan penghapusan baris (*drop rows*), menyebabkan kerugian informasi yang signifikan terutama saat tutupan awan sangat tebal.

**Kurangnya Benchmark Model**
Paper ini tidak membandingkan Random Forest dengan algoritma state-of-the-art lainnya (seperti XGBoost atau Deep Learning) dan kurang merinci teknik *hyperparameter tuning* yang digunakan, sehingga klaim RF sebagai "algoritma terbaik" kurang konklusif.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Perlu komparasi dengan model machine learning alternatif dan penjelasan limitasi dari imputasi awan pada citra satelit.