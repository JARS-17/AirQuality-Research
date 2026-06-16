# Review Jurnal 08
**"Air Quality Prediction and Ranking Assessment Based on Bootstrap-XGBoost Algorithm and Ordinal Classification Models"**
*Yang, Tian & Wu — Atmosphere, 2024*

---

### ✅ Kekuatan

**Dual Framework yang Komplementer**
Paper ini dengan cerdas memisahkan dua tugas yang berbeda namun saling melengkapi: prediksi nilai AQI (regresi) dan prediksi peringkat AQI (klasifikasi ordinal). Pendekatan dual ini memberikan informasi yang lebih lengkap bagi pengambil kebijakan dibanding paper yang hanya melakukan salah satunya.

**Inovasi Bootstrap-XGBoost**
Menggabungkan Bootstrap resampling dengan XGBoost untuk menghasilkan *prediction interval* (bukan hanya titik prediksi) adalah kontribusi metodologis yang praktis dan berguna. Dalam konteks kebijakan publik, memiliki interval kepercayaan 95% jauh lebih actionable daripada hanya nilai prediksi tunggal.

**Analisis Musiman yang Informatif**
Analisis persentase kualitas udara per musim menggunakan stacked plot memberikan gambaran kontekstual yang baik tentang pola polusi Xi'an sepanjang tahun, dan penjelasan tentang temperature inversion di musim dingin menunjukkan pemahaman yang baik terhadap mekanisme polusi.

**Model Ordinal yang Tepat Secara Statistik**
Penggunaan ordinal logit dan ordinal probit regression untuk memprediksi peringkat AQI (yang secara inheren bersifat ordinal, bukan nominal) adalah pilihan yang statistik yang benar. Banyak paper mengabaikan sifat ordinal dari peringkat kualitas udara dan menggunakan klasifikasi biasa — paper ini tidak membuat kesalahan itu.

**Transparansi Hasil Prediksi**
Tabel prediksi 15 hari ke depan dengan nilai aktual, nilai prediksi, standar deviasi, dan interval kepercayaan disajikan secara lengkap dan memudahkan verifikasi independen.

---

### ⚠️ Kelemahan & Catatan Kritis

**Data Hanya Satu Tahun — Sangat Terbatas**
Ini adalah kelemahan terbesar paper ini. Hanya satu tahun data (Oktober 2022 – September 2023) yang digunakan. Ini sangat rentan terhadap bias tahun spesifik: jika tahun 2022–2023 kebetulan adalah tahun dengan pola polusi yang tidak tipikal, seluruh model bisa menjadi tidak representatif.

**Anomali Serius pada Performa LSTM**
Dari Tabel 2, LSTM menghasilkan MAPE 38.11% dan R² hanya 0.2235 — jauh lebih buruk dari semua model lain termasuk SVR (R² 0.7611). Ini adalah hasil yang sangat mencurigakan dan tidak dijelaskan sama sekali oleh penulis. Kemungkinan besar ada masalah pada implementasi LSTM (arsitektur tidak tepat, insufficient training, atau data tidak dinormalisasi dengan benar). Ketiadaan diskusi tentang anomali ini merupakan kelemahan analitis yang serius.

**Klaim Akurasi 100% yang Meragukan**
Paper mengklaim bahwa prediksi peringkat AQI untuk 15 hari ke depan (1–15 Oktober 2023) memiliki akurasi 100% menggunakan kedua model ordinal. Klaim ini perlu dicermati dengan skeptis: periode 15 hari adalah sampel yang sangat kecil, dan periode Oktober biasanya memiliki kualitas udara yang relatif baik dan stabil di Xi'an. Akurasi 100% pada 15 sampel tidak bisa dianggap sebagai bukti performa model yang kuat.

**Variabel Input yang Bermasalah Secara Konseptual**
Model menggunakan konsentrasi PM2.5, PM10, SO2, NO2, O3, dan CO sebagai prediktor untuk memprediksi AQI. Namun AQI itu sendiri *dihitung dari* konsentrasi keenam polutan ini (sesuai persamaan (1) di paper itu sendiri). Ini menciptakan masalah konseptual yang serius: model pada dasarnya memprediksi output dari inputnya sendiri. Prediksi akan sangat akurat secara artifisial karena hubungannya hampir deterministic.

**Tidak Ada Variabel Meteorologi**
Berbeda dengan Jurnal 3 yang memasukkan data meteorologi sebagai auxiliary input, paper ini hanya menggunakan konsentrasi polutan. Faktor seperti suhu, kelembapan, kecepatan angin, dan tekanan udara diketahui memiliki pengaruh signifikan terhadap fluktuasi AQI, namun tidak diikutsertakan sama sekali.

**Tinjauan Literatur yang Kurang Mendalam**
Meski paper diterbitkan tahun 2024, pembahasan terhadap perkembangan terkini seperti model Transformer, attention mechanism, atau graph neural network untuk prediksi kualitas udara hampir tidak ada. Ini membuat positioning kontribusi paper terasa kurang kuat.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Major Revision** — Ide dual framework dan Bootstrap-XGBoost menarik, namun anomali performa LSTM yang tidak dijelaskan, masalah konseptual pada variabel input, dan klaim akurasi 100% yang perlu diverifikasi lebih dalam membuat paper ini membutuhkan revisi substansial sebelum layak dipublikasikan dalam bentuk saat ini.