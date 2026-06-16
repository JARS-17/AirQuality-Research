# Review Jurnal 15
**"SPATIO-TEMPORAL DYNAMICS OF EXTREME PM2.5 IN INDONESIA: A WEATHER-BASED HYBRID MODELING APPROACH"**
*Dwi Indriyati, et al. — Jurnal Meteorologi dan Geofisika, 2025*

---

### ✅ Kekuatan Utama

**Fokus Eksklusif pada Iklim Tropis**
Riset mengangkat kota-kota di Indonesia (Jakarta, Semarang, Malang) yang masih minim terekspos. Ini memberikan insight yang sangat spesifik untuk dinamika polusi di ekuator.

**Integrasi Data Cuaca ERA5**
Penggabungan data observasi in-situ beresolusi tinggi (hourly) dengan data cuaca grid *reanalysis* **ERA5** adalah manuver yang cerdas untuk mengatasi keterbatasan sensor lokal.

**Pemetaan Lag-Time**
Menggabungkan regresi linier dengan model pohon non-linear (**XGBoost**) yang mampu memetakan analisis *lag time* dan menyoroti efek tertundanya akumulasi polutan akibat cuaca stagnan.

---

### ⚠️ Kelemahan & Catatan Kritis

**Akurasi Model yang Sangat Moderat**
Akurasi R² untuk model prediktif tergolong sangat rendah (maksimal di sekitar **~0.53 dengan XGBoost** untuk Jakarta, bahkan hingga 0.37 untuk Malang). Ini membuat model kurang reliabel untuk sistem peringatan dini aktual.

**Kurangnya Parameter Antropogenik**
R² yang rendah menegaskan kelemahan bahwa menggunakan **parameter cuaca saja** sebagai prediktor PM2.5 sangat tidak memadai tanpa menyertakan elemen antropogenik spasial (data lalu lintas, variabel land-use, atau citra satelit AOD).

**Eksplorasi Fitur yang Dangkal**
Studi gagal membedah interpretasi interaksi antar fiturnya dan hanya puas menggunakan algoritma *feature importance* standar bawaan tree-based, tanpa visualisasi XAI lanjutan.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Major Revision** — Sangat membutuhkan injeksi parameter emisi/antropogenik dan teknik algoritma yang lebih dalam untuk mengangkat nilai akurasi R² secara signifikan.