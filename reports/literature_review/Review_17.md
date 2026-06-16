## JURNAL 17
**"Estimation of PM2.5 Concentration in DKI Jakarta from Sentinel-5P Imagery by Considering Meteorological Factors Using Random Forest Approach"**
*Rahmat Nur Rahman, Nur Mohammad Farda, and Ardhasena Sopaheluwakan — BIO Web of Conferences / ICoSIA, 2025*


### ✅ Kekuatan Utama
Penelitian ini unggul dalam pemanfaatan data multi-sumber, mengintegrasikan data penginderaan jauh dari satelit Sentinel-5P TropOMI dengan data meteorologi (ERA5 Land) dalam rentang waktu yang cukup panjang (2021-2023). Penggunaan regresi spasial berbasis Random Forest (RF) sangat tepat untuk menangkap hubungan non-linear antar variabel lingkungan. Model juga berhasil memetakan pola spasial yang selaras dengan musim kemarau dan penghujan di Indonesia.

### ⚠️ Kelemahan & Catatan Kritis
Validasi spasial sangat terbatas karena hanya mengandalkan 8 stasiun pemantauan darat di area metropolitan sebesar Jakarta, yang berisiko membuat model gagal menangkap variabilitas polusi mikro-lokal. Selain itu, paper ini tidak membandingkan Random Forest dengan algoritma *state-of-the-art* lainnya (seperti XGBoost atau Deep Learning) dan kurang merinci teknik *hyperparameter tuning* yang digunakan, sehingga klaim RF sebagai "algoritma terbaik" kurang kuat.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Perlu ditambahkan perbandingan dengan model machine learning lain dan penjelasan detail mengenai validasi spasial (keterbatasan stasiun darat).