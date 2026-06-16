# Review Jurnal 02
**"A Comparison of LSTM and BiLSTM for Forecasting the Air Pollution Index and Meteorological Conditions in Jakarta"**
*Handhayani, Lewenusa, Herwindiati & Hendryli — Universitas Tarumanagara*

---

### ✅ Kekuatan

**Cakupan Data yang Luas**
Dataset mencakup **12 tahun (2010–2021)** dengan 4.383 sampel, jauh lebih panjang dibanding Jurnal 1. Ini memberikan dasar statistik yang lebih kuat untuk pelatihan model.

**Desain Eksperimen yang Menarik**
Membagi eksperimen ke dalam 6 skenario yang mencakup periode sebelum dan saat pandemi **Covid-19** adalah ide yang cerdas. Ini memberikan dimensi analisis tambahan yang relevan secara sosial.

**Multivariate Forecasting**
Tidak hanya memprediksi satu variabel, tapi mencakup **PM10, SO2, CO, O3, NO2**, suhu, kelembapan, curah hujan, durasi sinar matahari, dan kecepatan angin secara bersamaan. Cakupan yang komprehensif.

**Transparansi Evaluasi**
Tabel evaluasi metrik (**MAE, MSE, RMSE, CV**) disajikan lengkap untuk setiap variabel dan setiap periode, memudahkan pembaca melakukan verifikasi independen.

---

### ⚠️ Kelemahan & Catatan Kritis

**Kontribusi Ilmiah yang Lemah**
Ini adalah kelemahan terbesar. Kesimpulan utama adalah *"tidak ada perbedaan signifikan antara LSTM dan BiLSTM"* — yang secara ilmiah kurang memberikan insight baru. Jika hasilnya tidak berbeda, pertanyaannya menjadi: *mengapa penelitian ini perlu dilakukan?* Kontribusi novelty-nya perlu diperkuat.

**Arsitektur Model Terlalu Sederhana & Seragam**
Kedua model menggunakan konfigurasi yang hampir identik (128 dan 64 unit, dropout, dense layer, 50 epoch, Softmax). Tidak ada penjelasan mengapa hyperparameter ini dipilih, tidak ada proses tuning, dan tidak ada **ablation study**. Ini melemahkan validitas perbandingan.

**Penggunaan Softmax Tidak Tepat**
**Softmax** adalah fungsi aktivasi untuk klasifikasi multi-kelas, bukan untuk regresi time series. Penggunaan Softmax pada output layer untuk prediksi nilai kontinu seperti PM10 atau suhu adalah **kesalahan metodologis** yang serius dan perlu diklarifikasi atau dikoreksi.

**Analisis Covid-19 Tidak Mendalam**
Meski diklaim sebagai salah satu tujuan penelitian, analisis dampak Covid-19 terhadap polusi udara hanya bersifat deskriptif dan dangkal. Tidak ada uji kausalitas, tidak ada analisis policy (misalnya PSBB/lockdown vs penurunan polutan), dan tidak ada kutipan literatur Covid-19 dan kualitas udara yang relevan.

**Tidak Ada Penjelasan Preprocessing Data**
Tidak dijelaskan bagaimana data yang hilang (**missing values**) ditangani, apakah dilakukan normalisasi, dan bagaimana data multivariate diformat sebagai input model.

**Format Penulisan**
Paper ini terkesan seperti laporan konferensi yang terburu-buru. Diskusi sangat singkat, tidak ada tinjauan literatur yang memadai, dan tidak ada perbandingan yang bermakna dengan penelitian terdahulu.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Major Revision** — Perlu perbaikan substansial terutama pada justifikasi novelty, koreksi fungsi aktivasi, pendalaman analisis Covid-19, dan penjelasan metodologi yang lebih lengkap sebelum layak dipublikasikan.