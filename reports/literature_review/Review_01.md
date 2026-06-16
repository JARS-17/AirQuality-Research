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