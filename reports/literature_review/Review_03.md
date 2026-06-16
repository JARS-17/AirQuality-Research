# Review Jurnal 03
**"Air Quality Estimation Using LSTM and An Approach for Data Processing Techniques"**
*Ton-Thien, Nguyen, Le & Duong — MediaEval 2021, CEUR-WS*

---

### ✅ Kekuatan

**Pendekatan Preprocessing yang Praktis**
Salah satu kontribusi menarik paper ini adalah penanganan **missing values** secara bertingkat — menggunakan **mean imputation** untuk fitur cuaca, lalu **XGBoost** untuk mengisi nilai PM10 yang hilang berdasarkan fitur cuaca. Pendekatan hierarkis ini lebih cerdas dibanding sekadar mengisi dengan mean atau menghapus data.

**Cakupan Multi-Negara**
Dataset mencakup tiga negara (Brunei, Singapura, Thailand) dengan karakteristik polusi yang berbeda. Ini memberikan nilai lebih dalam hal generalisasi dibanding studi single-site.

**Perbandingan Tiga Varian LSTM**
Meski terbatas pada dataset Brunei, penelitian ini setidaknya membandingkan **LSTM standar**, **Bi-LSTM**, dan **Stacked LSTM** secara bersamaan — memberikan gambaran perbandingan yang lebih komprehensif dari satu kerangka eksperimen.

---

### ⚠️ Kelemahan & Catatan Kritis

**Ini Bukan Jurnal — Ini Paper Workshop Kompetisi**
Ini adalah kelemahan struktural yang paling fundamental. Paper ini adalah submission untuk *MediaEval 2021 competition*, bukan artikel penelitian yang melalui proses peer-review ketat. Panjangnya hanya 3 halaman, yang jauh di bawah standar artikel ilmiah. Konteks ini penting untuk dipahami karena standar evaluasinya berbeda.

**Overfitting yang Parah & Tidak Dijelaskan dengan Baik**
Ini adalah masalah terbesar secara ilmiah. Pada validation set Brunei, Bi-LSTM mencapai RMSE 3.625, namun pada test set melonjak drastis menjadi 10.967 — hampir **3x lipat**. Untuk Singapura, dari 5.821 menjadi 10.248. Ini indikasi **overfitting** yang sangat serius. Sayangnya, penulis hanya menyebutnya singkat tanpa analisis mendalam mengenai penyebab dan solusinya.

**Tidak Ada Regularisasi atau Strategi Anti-Overfitting**
Tidak disebutkan penggunaan **dropout**, **early stopping**, **L2 regularization**, atau **cross-validation**. Dengan hanya 80/20 split tanpa validasi silang, risiko overfitting pada dataset yang tidak terlalu besar sangat tinggi.

**Analisis Hasil Sangat Dangkal**
Bagian "Results and Analysis" hanya terdiri dari beberapa paragraf singkat yang melaporkan angka tanpa memberikan analisis substansial. Tidak ada diskusi mengapa Thailand menghasilkan RMSE jauh lebih tinggi (10.624), tidak ada analisis pola kesalahan, dan tidak ada visualisasi prediksi vs aktual.

**Imputation XGBoost Tidak Divalidasi**
Meski ide penggunaan XGBoost untuk imputing PM10 cukup inovatif, tidak ada evaluasi akurasi imputation itu sendiri. Kualitas imputation secara langsung mempengaruhi kualitas training data, dan ini dibiarkan sebagai "black box".

**Eksperimen Tidak Lengkap**
Untuk Singapura dan Thailand, hanya Bi-LSTM yang diuji (dengan alasan keterbatasan waktu). Ini membuat perbandingan antar model menjadi tidak adil dan tidak konsisten secara metodologis.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Tidak layak sebagai jurnal ilmiah utama.** Sebagai paper workshop kompetisi, paper ini acceptable — tujuannya memang berbagi pendekatan, bukan mempublikasikan temuan definitif. Namun jika ingin dikembangkan menjadi artikel jurnal penuh, dibutuhkan ekspansi besar-besaran pada metodologi, analisis, dan penanganan overfitting.