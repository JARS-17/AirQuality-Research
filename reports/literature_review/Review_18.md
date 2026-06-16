# Review Jurnal 18
**"Analysis Correlation of Meteorological Factors with PM2.5 Concentrations in Forecasting Air Quality of The City of Jakarta"**
*Ade Ayu Oktaviana, Abdu Fadli Assomadi, and Joni Hermana — IOP Conf. Series: Earth and Environmental Science, 2025*

---

### ✅ Kekuatan Utama

**Analisis Korelasi Spearman yang Solid**
Penelitian ini menggunakan analisis korelasi **Spearman** yang sangat sesuai untuk mendeteksi hubungan non-linear monotonik antara faktor meteorologi (hujan, suhu, kelembaban, angin) dengan polutan.

**Adopsi Data Reanalisis ECMWF EAC4**
Penggunaan basis data reanalisis atmosfer dari satelit memberikan dimensi spasial yang baik dan menutupi blank-spot data observasi dari 5 stasiun stasioner Jakarta selama rentang waktu 2022-2023.

---

### ⚠️ Kelemahan & Catatan Kritis

**Indikasi Overfitting yang Fatal pada MLR**
Kelemahan paling fatal ada pada hasil pemodelan **Multiple Linear Regression (MLR)** yang mengklaim nilai determinasi **(R²) sebesar 0.99**. Nilai ini sangat tidak realistis dan tidak wajar untuk regresi linear sederhana pada data polusi udara yang *chaotic*, murni mengindikasikan adanya *overfitting* ekstrem atau *data leakage* dalam pemrosesan data latih.

**RMSE Tetap Tinggi Meski R² Sempurna**
Kecurigaan kesalahan metodologis diperburuk dengan pelaporan nilai kesalahan aktual (RMSE) yang masih berada di kisaran 22.95 µg/m³ meskipun R²-nya diklaim nyaris sempurna. 

**Model yang Terlalu Sederhana**
MLR gagal memetakan kompleksitas anomali atmosferik. Penggunaan algoritma linear klasik tidak lagi mampu bersaing dengan ML modern berbasis *tree* atau deep learning.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Major Revision** — Model regresi linear memiliki kesalahan indikasi overfitting yang sangat parah; wajib dievaluasi dan digantikan model machine learning non-linear.