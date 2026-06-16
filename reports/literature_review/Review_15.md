## JURNAL 15
**"SPATIO-TEMPORAL DYNAMICS OF EXTREME PM2.5 IN INDONESIA: A WEATHER-BASED HYBRID MODELING APPROACH"**
*Dwi Indriyati, et al. — Jurnal Meteorologi dan Geofisika, 2025*


### ✅ Kekuatan Utama
Fokus riset mengangkat kota-kota tropis di Indonesia (Kemayoran, Semarang, Malang) yang masih minim terekspos dalam domain ini. Integrasi data observasi in-situ beresolusi tinggi (hourly) dengan data cuaca grid *reanalysis* ERA5 adalah manuver yang sangat tepat. Studi ini menggabungkan regresi linier dengan model pohon non-linear (RF, XGBoost) yang mampu memetakan analisis *lag time* dan menyoroti efek kondisi meteorologi yang stagnan.

### ⚠️ Kelemahan & Catatan Kritis
Akurasi R² untuk model prediktif tergolong sangat moderat dan rendah (maksimal di sekitar ~0.53 dengan XGBoost untuk Jakarta, bahkan hingga 0.37 untuk Malang). Hal ini menegaskan kelemahan bahwa menggunakan parameter cuaca *saja* sebagai prediktor PM2.5 sangat tidak memadai tanpa menyertakan elemen antropogenik spasial (data lalu lintas, variabel *land-use*, atau AOD). Selain itu, studi gagal membedah interpretasi interaksi antar fiturnya dan hanya puas menggunakan *feature importance* standar bawaan algoritma tanpa metrik analisis lanjut.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Major Revision** — Model sangat membutuhkan injeksi parameter non-meteorologis dan teknik Deep Learning untuk mengangkat akurasi agar layak menjadi sistem peringatan dini.