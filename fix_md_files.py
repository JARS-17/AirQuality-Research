import os

out_dir = r"D:\Kuliah Praktik\KP BRIN\reports\literature_review"
os.makedirs(out_dir, exist_ok=True)

# FULL TEXT FOR JURNAL 1 TO 6
data = {
    1: """# Review Jurnal 01
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
""",

    2: """# Review Jurnal 02
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
""",

    3: """# Review Jurnal 03
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
""",

    4: """# Review Jurnal 04
**"Assessing Low-Cost Sensor for Characterizing Temporal Variation of PM2.5 in Bandung, Indonesia"**
*Kurniawati et al. — Kuwait Journal of Science, 2025*

---

### ✅ Kekuatan

**Relevansi Lokal yang Tinggi**
Penelitian ini mengisi celah yang nyata — evaluasi sensor **PurpleAir PA-II** untuk konteks Indonesia, khususnya Bandung, masih sangat terbatas. Data jangka panjang selama 12 bulan (Juni 2022–Mei 2023) memberikan cakupan yang mencakup satu siklus musim penuh (kemarau dan hujan), yang sangat berharga.

**Desain Co-Location yang Solid**
Penggunaan **SuperSASS** sebagai referensi yang memenuhi standar EPA FRM adalah pilihan yang tepat dan kredibel. Jarak co-location ±25 m dan prosedur QC yang terstruktur (threshold ±10 μg/m³ antar sensor a dan b) menunjukkan ketelitian metodologis yang baik.

**Analisis Temporal yang Komprehensif**
Paper ini tidak hanya melaporkan angka rata-rata, tapi juga menganalisis variasi **diurnal** (pola bimodal pagi-malam), variasi **mingguan** (weekday vs weekend), dan variasi **musiman** — semuanya disajikan dengan visualisasi yang informatif menggunakan boxplot dan time-series.

**Interpretasi Kontekstual yang Kaya**
Penulis berhasil mengaitkan temuan teknis dengan konteks lokal yang spesifik: puncak pagi jam 07.00 dikaitkan dengan jam sibuk kendaraan, puncak malam dengan suhu rendah dan kondisi udara yang stagnan, serta konsentrasi tinggi di musim kemarau dengan minimnya curah hujan. Ini membuat paper ini informatif tidak hanya bagi insinyur tapi juga bagi pembuat kebijakan.

**Tinjauan Literatur yang Memadai**
Paper ini dengan baik memposisikan dirinya dalam konteks studi PurpleAir global (Korea, Yunani, Uganda, Australia, AS), menunjukkan kesadaran yang baik terhadap literatur terkait.

---

### ⚠️ Kelemahan & Catatan Kritis

**Hanya Satu Lokasi Sampling**
Seluruh pengukuran dilakukan di satu titik — kawasan nuklir Tamansari, Bandung. Ini membatasi representasi spasial secara signifikan. Bandung memiliki topografi "cekungan" yang membuat distribusi polutan bervariasi antar wilayah, dan satu sensor tidak bisa mewakili keseluruhan kota.

**Gap Data September–November 2022**
Ada periode off selama 3 bulan akibat masalah teknis pada SuperSASS. Ini menyebabkan dataset tidak lengkap dan berpotensi bias terutama pada analisis musiman, karena periode tersebut mencakup transisi musim kemarau ke hujan yang penting.

**PA-II Overestimasi Konsisten 24%**
Meski diakui dan dibahas, overestimasi sebesar 24% adalah angka yang cukup besar untuk monitoring lingkungan regulasi. Paper ini tidak menyajikan persamaan koreksi spesifik untuk kondisi Bandung, padahal data selama 12 bulan sebenarnya cukup untuk membangun model koreksi lokal yang lebih akurat.

**Tidak Ada Analisis Source Apportionment**
Paper mengidentifikasi sumber PM2.5 secara kualitatif (kendaraan, industri, pembakaran biomassa), namun tidak melakukan analisis kuantitatif seperti **Positive Matrix Factorization (PMF)** atau receptor modeling untuk memverifikasi kontribusi masing-masing sumber. Padahal alat seperti SuperSASS sebenarnya dirancang juga untuk speciation analysis yang bisa mendukung source apportionment.

**Keterbatasan Sensor RH yang Serius Namun Kurang Ditindaklanjuti**
PA-II secara konsisten mencatat **RH (Kelembaban Relatif)** yang lebih rendah 2.59–35% dibanding referensi BPS. Ini adalah masalah serius karena RH mempengaruhi akurasi pengukuran PM2.5 optis. Meski dibahas, solusinya hanya disebutkan sebagai "future work" tanpa langkah konkret.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Accept dengan Minor Revision** — Ini adalah paper yang solid dan well-executed. Perbaikan utama yang disarankan adalah penyajian persamaan koreksi lokal untuk kondisi Bandung dan penambahan diskusi yang lebih kritis mengenai implikasi gap data September–November terhadap validitas analisis musiman.
""",

    5: """# Review Jurnal 05
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
""",

    6: """# Review Jurnal 06
**"Deep Learning for Air Quality Forecasts: a Review"**
*Liao, Zhu, Wu, Pan, Tang & Wang — Current Pollution Reports, Springer, 2020*

---

### ✅ Kekuatan

**Ini adalah Paper Fondasi yang Wajib Anda Baca**
Sebagai pembimbing, saya tekankan ini: paper review dari Springer ini adalah *roadmap* terbaik untuk memahami lanskap **deep learning** dalam prediksi kualitas udara. Diterbitkan oleh Chinese Academy of Sciences, ini bukan paper biasa — ini adalah karya dari institusi riset atmosfer terkemuka di dunia.

**Cakupan Arsitektur yang Komprehensif**
Paper ini memetakan seluruh ekosistem deep learning untuk AQI: **RNN, LSTM, GRU** (temporal), **CNN, SAE, DBN** (spasial), hingga **STDL/CNN-LSTM/CNN-GRU** (spatiotemporal). Ini memberi Anda kerangka konseptual yang solid untuk memilih metode yang tepat.

**Lima Domain Aplikasi yang Dipetakan dengan Jelas**
Review ini tidak hanya membahas prediksi — tapi juga: (1) data gap filling, (2) inversi data satelit, (3) speedup CTM, (4) prediksi spatiotemporal, dan (5) estimasi sumber emisi. Ini membuka wawasan bahwa prediksi AQI hanyalah satu bagian dari ekosistem yang jauh lebih luas.

**Identifikasi Tantangan Masa Depan yang Masih Relevan**
Meski ditulis 2020, tantangan yang diidentifikasi paper ini sebagian besar masih valid di 2025: tidak ada benchmark dataset standar, **black-box problem**, kurangnya studi jangka panjang (>7 hari), dan belum adanya integrasi komprehensif antara DL dan CTM.

**Pembanding Tradisional yang Jujur**
Paper ini tidak membesar-besarkan deep learning. Ia secara fair menjelaskan keterbatasan CTM dan metode statistik klasik (ARIMA, MLR), kemudian menunjukkan di mana DL dapat memberikan nilai tambah nyata.

---

### ⚠️ Kelemahan & Catatan Kritis

**Sudah 5 Tahun — Beberapa Bagian Sudah Outdated**
Ini ditulis 2020, sebelum era **Transformer** dan **Attention mechanism** mendominasi riset DL. Tidak ada pembahasan tentang model berbasis Transformer (Informer, PatchTST, iTransformer) yang kini menjadi state-of-the-art untuk time series. Untuk Anda, ini sekaligus peluang: gap antara review 2020 dan kondisi 2025 adalah area penelitian yang sangat aktif.

**Tidak Ada Studi dari Asia Tenggara**
Hampir semua paper yang dirujuk berasal dari Cina, Korea, Amerika, dan Eropa. Indonesia, Filipina, Thailand — tidak ada satu pun. Ini adalah konfirmasi eksplisit dari gap geografis yang menjadi positioning penelitian Anda.

**Tidak Ada Perbandingan Kuantitatif Antar Model**
Sebagai review paper, tidak ada tabel meta-analisis yang membandingkan RMSE atau MAE antar studi secara terstandar. Pembaca harus membaca satu per satu paper yang dirujuk untuk membandingkan performa model. Ini kelemahan umum review non-systematic, tapi tetap perlu dicatat.

**Aspek Low-Cost Sensor Tidak Dibahas**
Paper ini fokus pada stasiun pemantauan resmi dan data satelit. Potensi **low-cost sensor** (PurpleAir, SDS011, dll.) untuk densifikasi jaringan pemantauan — yang sangat relevan di negara berkembang seperti Indonesia — tidak disentuh sama sekali.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai | Catatan |
|---|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ | Fondasi wajib untuk siapapun yang meneliti DL+AQI |
| Kebaruan / Novelty | ⭐⭐⭐ | Tinggi saat terbit 2020, kini sebagian sudah terlampaui |
| Kualitas Metodologi | ⭐⭐⭐⭐ | Sistematis, taksonomi arsitektur jelas |
| Kualitas Analisis | ⭐⭐⭐⭐ | Prospek dan tantangan diidentifikasi dengan tajam |
| Generalisasi Temuan | ⭐⭐ | Tidak ada konteks Asia Tenggara sama sekali |

**Rekomendasi: Accept**
"""
}

for idx, content in data.items():
    filename = f"Review_{idx:02d}.md"
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Updated full text for {filename}")

print("Selesai memulihkan teks penuh untuk Jurnal 1-6!")
