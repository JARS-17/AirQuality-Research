# Review Jurnal 19
**"Sistem Prediksi Kualitas Udara Menggunakan Algoritma Long Short-Term Memory (LSTM)"**
*Muhammad Zaki Wicaksono, Ledy Elsera Astrianty — TIN: Terapan Informatika Nusantara, 2025*

---

### ✅ Kekuatan Utama

**Relevansi Arsitektur Deep Learning**
Penerapan arsitektur **LSTM** sangat relevan dan secara empiris terbukti tangguh memecahkan masalah dependensi data *time-series* polusi udara di rentang waktu panjang.

**Hilirisasi Produk Berbasis GUI**
Kekuatan utama yang membedakan penelitian ini adalah fokus hilirisasinya, yaitu keberhasilan pengembang membangun purwarupa aplikasi **Graphical User Interface (GUI)** yang merubah hasil prediksi algoritma kompleks menjadi sistem peringatan yang bisa dioperasikan pengguna awam.

**Prepemrosesan Standar yang Rapi**
Proses prapemrosesan data polutan historis DLH Yogyakarta (2022-2024) dieksekusi dengan baik, memanfaatkan interpolasi linier untuk *missing values* dan *MinMaxScaler* agar konvergensi gradient stabil.

---

### ⚠️ Kelemahan & Catatan Kritis

**Generalisasi Spasial yang Tidak Ada**
Dataset sepenuhnya terkunci pada satu lokus geografis eksklusif (Kota Yogyakarta), tidak ada uji validasi silang pada stasiun berkarakteristik beda, sehingga generalisasi spasialnya nihil.

**Underfitting pada Fitur Spesifik (Hidrokarbon)**
Secara metrik performa, prediksi khusus untuk parameter Hidrokarbon (HC) memiliki MAE yang lebih besar dari standar *Mean Absolute Deviation* (MAD), menegaskan bahwa model **gagal beradaptasi** dan *underfit* terhadap pola sebaran gas HC.

**Sistem Belum *Live-Time***
Meskipun memiliki GUI, sistem inferensinya tidak terhubung dengan *live API stream*, melainkan tetap menggunakan *batch processing* manual, mengurangi utilitas *early-warning*.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Penulis wajib menyertakan diagnosis *error analysis* mengapa LSTM gagal pada parameter HC, serta menyediakan perbandingan dengan *baseline* (ARIMA).