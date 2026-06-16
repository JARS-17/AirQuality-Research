# Review Jurnal 01
**"Improving the Forecast Accuracy of PM2.5 Using SETAR-Tree Method: Case Study in Jakarta, Indonesia"**
*Safira, Kuswanto & Ahsan — Atmosphere, 2025*

---

### ✅ Kekuatan

**Relevansi & Urgensi Topik**
Topik sangat relevan. Jakarta sebagai salah satu kota paling terpolusi di dunia menjadikan penelitian ini punya nilai praktis tinggi. Penulis berhasil membangun justifikasi yang kuat mengapa **PM2.5** perlu diperhatikan secara serius dari sisi kesehatan maupun kebijakan publik.

**Kebaruan Metode**
Penggunaan **SETAR-Tree** untuk prediksi PM2.5 adalah kontribusi yang genuinely baru. Sebelumnya SETAR-Tree baru diuji pada harga emas dan data morbiditas, sehingga aplikasinya pada kualitas udara memberikan nilai novelty yang jelas.

**Metodologi yang Terstruktur**
Alur metodologi cukup sistematis: uji stasioneritas → identifikasi **ARIMA** → pembangunan **LSTM** → pembangunan **SETAR-Tree** → evaluasi komparatif. Penggunaan **Terasvirta test** untuk membuktikan nonlinearitas data sebelum memilih model juga merupakan langkah yang tepat secara statistik.

**Hasil yang Jelas & Terukur**
Perbandingan **RMSE** dan **MAPE** antara dua model disajikan dengan rapi. SETAR-Tree unggul di semua skenario (in-sample RMSE 0.1691 vs LSTM 0.2038; out-sample RMSE 0.2159 vs 0.2399), dan penjelasan mengapa SETAR-Tree lebih baik secara konseptual juga diberikan.

---

### ⚠️ Kelemahan & Catatan Kritis

**Keterbatasan Data**
Data hanya berasal dari **satu stasiun monitoring (DKI4 - Lubang Buaya)** selama sekitar 23 bulan. Ini membatasi generalisasi temuan secara spasial maupun temporal. Jakarta memiliki 5 stasiun monitoring, dan pola polusi bisa berbeda signifikan antar wilayah.

**LSTM Belum Dioptimalkan Secara Maksimal**
Jumlah neuron hanya divariasikan dari 1–5, epoch hanya 50, dan arsitektur hanya menggunakan satu hidden layer. Tidak ada tuning lebih lanjut seperti **learning rate scheduling**, **regularization**, atau perbandingan dengan varian LSTM lain (misalnya **BiLSTM**). Ini membuat perbandingan terasa kurang adil bagi LSTM.

**Tidak Ada Variabel Eksogen**
PM2.5 sangat dipengaruhi faktor meteorologi (suhu, kelembapan, kecepatan angin) dan aktivitas manusia. Kedua model hanya menggunakan data univariat PM2.5. Memasukkan variabel eksogen kemungkinan akan meningkatkan akurasi keduanya secara signifikan.

**Periode Out-Sample Terlalu Pendek**
Out-sample hanya mencakup **30 hari (November 2023)**. Evaluasi pada periode yang sangat singkat ini tidak cukup untuk mengklaim keunggulan generalisasi secara meyakinkan.

**Tidak Ada Uji Signifikansi Statistik**
Perbedaan performa antar model tidak diuji secara statistik (misalnya **Diebold-Mariano test**). Selisih RMSE yang kecil mungkin tidak signifikan secara statistik.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Layak dipublikasikan dengan perbaikan pada kedalaman evaluasi model LSTM dan penambahan diskusi keterbatasan yang lebih jujur.