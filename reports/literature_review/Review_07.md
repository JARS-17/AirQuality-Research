# Review Jurnal 07
**"Long Short-Term Memory Neural Network for Air Pollutant Concentration Predictions: Method Development and Evaluation"**
*Li, Peng, Yao, Cui, Hu, You & Chi — Environmental Pollution, 2017*

---

### ✅ Kekuatan

**Kontribusi Teknis yang Jelas dan Signifikan**
Ini adalah salah satu paper pertama yang mengaplikasikan LSTM untuk prediksi konsentrasi polutan udara secara *real-value* (bukan sekadar klasifikasi ranking). Penulis secara eksplisit menyatakan bahwa sebelumnya LSTM baru digunakan untuk klasifikasi risiko polusi, bukan prediksi nilai aktual — sehingga novelty-nya kuat dan terdokumentasi dengan baik.

**Integrasi Korelasi Spatiotemporal**
Keputusan menggunakan data dari 12 stasiun monitoring secara bersamaan sebagai input adalah kontribusi metodologis yang cerdas. Analisis korelasi Pearson antar stasiun (semua di atas 0.82) dan analisis autokorelasi temporal digunakan secara tepat untuk membenarkan desain arsitektur model — ini adalah contoh metodologi yang *data-driven*, bukan asumsi semata.

**Penggunaan Auxiliary Data yang Terstruktur**
Memasukkan data meteorologi (suhu, kelembapan, kecepatan angin, visibilitas) dan time stamp (bulan, jam) menggunakan one-hot encoding merupakan langkah yang tepat dan terbukti meningkatkan performa. Perbandingan LSTM vs LSTME (dengan dan tanpa auxiliary data) memberikan ablation study yang informatif.

**Perbandingan Model yang Komprehensif**
Enam model dibandingkan: LSTME, LSTM NN, STDL, TDNN, ARMA, dan SVR — mencakup spektrum dari model statistik klasik hingga deep learning. Ini memberikan konteks yang memadai untuk menilai keunggulan model yang diusulkan.

**Prediksi Multiscale yang Realistis**
Framework prediksi 1–24 jam ke depan dengan model terpisah per rentang waktu adalah kontribusi praktis yang valuable. Penulis juga jujur bahwa performa menurun untuk prediksi jangka panjang (MAPE 1-jam: 11.93% vs 13–24 jam: 31.47%) — kejujuran ini justru memperkuat kredibilitas paper.

---

### ⚠️ Kelemahan & Catatan Kritis

**Keterbatasan Geografis**
Data hanya berasal dari satu kota (Beijing). Mengingat klaim paper adalah *general framework* untuk prediksi polutan udara, validasi pada kota lain dengan karakteristik polusi berbeda (misalnya kota industri, kota pesisir) akan memperkuat generalisasi.

**Penanganan Missing Values yang Terlalu Sederhana**
Linear interpolation digunakan untuk mengisi missing values pada dataset 12 stasiun selama lebih dari 2 tahun. Untuk data polutan yang bisa berfluktuasi drastis dalam hitungan jam, interpolasi linear bisa menghasilkan nilai yang sangat tidak representatif terutama saat episode polusi tinggi.

**Hyperparameter Search yang Belum Optimal**
Meski menggunakan random search dengan 5-fold cross-validation, kandidat jumlah node yang diuji hanya 5 nilai {600, 800, 1000, 1400, 2000} dan hanya satu konfigurasi arsitektur (2 LSTM layer + 1 FC) yang dieksplorasi. Tidak ada justifikasi mengapa arsitektur yang lebih dalam atau lebih dangkal tidak dicoba.

**Tidak Ada Uji Signifikansi Statistik**
Perbedaan performa antar model (misalnya LSTME MAPE 11.93% vs LSTM NN 15.84%) tidak diuji secara statistik. Tanpa uji seperti Diebold-Mariano atau paling tidak confidence interval dari metrik, klaim keunggulan model sulit diverifikasi secara rigorous.

**Konteks Temporal Terbatas**
Data mencakup Januari 2014 – Mei 2016, yang berarti tidak merepresentasikan variasi multi-year yang lebih panjang. Pola musiman Beijing yang khas (episode polusi parah di musim dingin) mungkin tidak terwakili secara merata dalam split 80/20 yang bersifat random.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Accept / Minor Revision** — Paper ini adalah kontribusi yang solid dan pionir di bidangnya. Meski ada beberapa kelemahan metodologis minor, kebaruan dan kualitas analisis secara keseluruhan sudah memenuhi standar publikasi jurnal Q1 seperti *Environmental Pollution*.