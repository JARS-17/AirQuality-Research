# Review Jurnal 05
**"Shapley Additive Explanations Interpretation of the XGBoost Model in Predicting Air Quality in Jakarta"**
*Iffadah, Trimono & Prasetya — Jurnal Riset Informatika, Vol.7 No.3, Juni 2025 (SINTA 4)*

---

### ✅ Kekuatan

**Integrasi XAI yang Tepat Sasaran**
Ini kekuatan utama paper ini. Menggabungkan **XGBoost** dengan **SHAP** untuk prediksi PM2.5 adalah pilihan yang logis dan relevan. Selama ini banyak penelitian di Indonesia hanya fokus pada akurasi prediksi tanpa peduli *mengapa* model membuat keputusan tersebut. Paper ini menjawab kebutuhan interpretabilitas (**Explainable AI**) yang selama ini menjadi gap di literatur kualitas udara Indonesia.

**Performa Model yang Kuat**
**MAPE 4.44%** masuk kategori "Accurate" (< 10%) dan unggul dari semua pembanding: Hybrid ARIMA-ANN (13.6%), LSTM (8.07%), dan Ordinary Kriging (19.5%). Ini bukan klaim kosong — ada tabel komparasi yang transparan dan dapat diverifikasi.

**Preprocessing yang Dipikirkan dengan Baik**
Penggunaan **KNN Imputer (K=5)** untuk missing values jauh lebih tepat dibanding mean/median imputation, terutama untuk data polutan yang memiliki korelasi kompleks antar variabel. Pilihan **winsorizing** untuk outlier juga bijak — mempertahankan jumlah data sekaligus meredam distorsi ekstrem.

**Grid Search + Cross-Validation 10-Fold**
Hyperparameter tuning dilakukan secara sistematis dan tidak asal tebak. Penggunaan **10-fold CV** mengurangi risiko overfitting dan meningkatkan validitas generalisasi model.

**Insight SHAP yang Bermakna**
Temuan bahwa PM10 memiliki *saturation effect* terhadap PM2.5 (terlihat dari **SHAP Dependence Plot**) dan bahwa interaksi PM10–O3 mempengaruhi prediksi secara non-linear adalah insight yang genuinely berguna untuk kebijakan publik — bukan hanya angka akurasi.

---

### ⚠️ Kelemahan & Catatan Kritis

**Data Hanya dari Satu Kota, Lima Stasiun**
Dataset mencakup 5 SPKU di DKI Jakarta 2021–2024. Meski lebih baik dari paper 1 (satu stasiun), generalisasi ke kota lain di Indonesia — termasuk Bandung — tidak dapat dilakukan secara langsung. Paper ini sendiri mengakui ini di bagian saran, tapi tidak mendiskusikan implikasinya secara mendalam.

**Target Variabel Membingungkan**
Paper mengklaim memprediksi "kualitas udara" secara umum, namun target model sebenarnya hanya PM2.5. Variabel lain (SO2, CO, O3, NO2) hanya berperan sebagai *fitur input*, bukan target prediksi. Ini perlu dikomunikasikan lebih jelas di judul dan abstrak agar tidak menyesatkan pembaca.

**Tidak Ada Analisis Temporal / Seasonality**
Data mencakup Januari 2021 – Mei 2024, periode yang melewati pandemi Covid-19 dan berbagai peristiwa khusus (kebakaran hutan, musim hujan-kemarau). Tidak ada analisis bagaimana pola musiman atau event khusus mempengaruhi performa model. Ini adalah celah analisis yang signifikan.

**Split Data Tidak Konsisten Secara Logis**
Ada tiga skenario split: 90:10, 80:20, 70:30. Namun paper menggunakan 90:10 sebagai hasil terbaik karena MAPE-nya terendah. Ini bermasalah — 10% testing data berarti hanya ~477 data poin untuk evaluasi. Performa terbaik di split terkecil bisa jadi indikasi model **overfitting** pada training set yang sangat besar, bukan bukti generalisasi yang baik.

**Evaluasi Tunggal: MAPE Saja**
Di bagian hasil utama, hanya MAPE yang dijadikan acuan keunggulan. Padahal paper sendiri menyebutkan MSE, RMSE, dan R² — namun nilai-nilai ini tidak ditampilkan di tabel komparasi antar model. Tanpa R², kita tidak tahu seberapa baik model menangkap variansi data secara keseluruhan.

**Tidak Ada Baseline Sederhana**
Tidak ada perbandingan dengan model sederhana seperti Linear Regression atau Moving Average sebagai *sanity check*. Kita tidak tahu apakah XGBoost benar-benar memberikan nilai tambah dibanding pendekatan trivial.

**Akreditasi SINTA 4**
Ini catatan penting untuk Anda sebagai peneliti: jurnal ini terakreditasi SINTA 4, bukan Scopus atau SINTA 1/2. Untuk tesis atau publikasi yang diperhitungkan secara internasional, ini perlu diperhatikan. Namun sebagai *referensi literatur lokal* dan bukti bahwa penelitian XGBoost+SHAP untuk AQI Jakarta sudah ada, paper ini tetap relevan.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai | Catatan |
|---|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ | XGBoost + SHAP + Jakarta, sangat dekat dengan gap Anda |
| Kebaruan / Novelty | ⭐⭐⭐⭐ | XAI untuk AQI di Indonesia masih sangat jarang |
| Kualitas Metodologi | ⭐⭐⭐ | KNN imputer dan grid search bagus, tapi split data bermasalah |
| Kualitas Analisis | ⭐⭐⭐⭐ | SHAP insightful, tapi evaluasi metrik kurang lengkap |
| Generalisasi Temuan | ⭐⭐ | Hanya Jakarta, tidak bisa langsung ditransfer ke Bandung |

**Rekomendasi: Minor Revision**