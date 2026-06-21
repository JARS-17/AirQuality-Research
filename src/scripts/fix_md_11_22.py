import os

out_dir = r"D:\Kuliah Praktik\KP BRIN\reports\literature_review"
os.makedirs(out_dir, exist_ok=True)

data = {
    11: """# Review Jurnal 11
**"Statistical and Machine Learning Models for Air Quality: A Systematic Review of Methods and Challenges"**
*Ballesteros Peinado, Guarda, Herrera-Vidal, Minnaard & Coronado-Hernández — Algorithms, 2025*

---

### ✅ Kekuatan Utama

**Cakupan Corpus yang Sangat Luas**
Menganalisis **412 artikel** peer-reviewed dari 2016–2025 menggunakan protokol PRISMA 2020 adalah skala yang substansial. Proses filtering berlapis (dari 258.035 dokumen awal) didokumentasikan secara transparan.

**Pendekatan Bibliometrik yang Inovatif**
Penggunaan analisis "science tree" dan visualisasi jaringan co-citation menggunakan **Gephi** memberikan perspektif epistemologis yang lebih kaya dibanding systematic review konvensional.

**Identifikasi Kesenjangan Geografis yang Penting**
Temuan bahwa **73.2% studi terkonsentrasi di Asia** sementara Amerika Latin hanya 1.03% dan Afrika 5.15% adalah kontribusi yang sangat berharga untuk agenda penelitian global.

**Sistematisasi Variabel dan Metrik yang Komprehensif**
Mengidentifikasi 1.177 variabel prediktor. Temuan bahwa **CO adalah variabel terbanyak digunakan (35%)** dan RMSE/MSE mendominasi metrik evaluasi membuka diskusi penting tentang standardisasi.

---

### ⚠️ Kelemahan & Catatan Kritis

**Dominasi Akurasi atas Interpretabilitas dalam Analisis**
Paper mengidentifikasi bahwa **70.8% studi hanya fokus pada akurasi** sementara interpretabilitas hanya 20.8%. Namun ironisnya, paper ini sendiri tidak mendalami evaluasi interpretabilitas secara teknis.

**Definisi "Hybrid Model" yang Tidak Konsisten**
Paper mengkategorikan **CNN-LSTM** sebagai "hybrid model" terpisah dari kategori ML, namun dalam literatur yang dianalisis CNN-LSTM juga muncul di kategori ML, menyebabkan tumpang tindih taksonomi.

**Analisis Kuantitatif yang Dangkal**
Analisis perbandingan akurasi ML vs model statistik hanya didasarkan pada 24 studi eksplisit (hanya ~5.8% dari korpus). Tidak ada meta-analisis kuantitatif seperti **pooled performance metrics**, sehingga kesimpulan terasa kurang rigid.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Accept** — Paper SLR komprehensif berstandar tinggi yang sangat berharga sebagai landasan roadmap riset kualitas udara.
""",

    12: """# Review Jurnal 12
**"Interpretable Machine Learning Approaches for Forecasting and Predicting Air Pollution: A Systematic Review"**
*Anass Houdou, et al. — Aerosol and Air Quality Research, 2024*

---

### ✅ Kekuatan Utama

**Metodologi Tinjauan yang Komprehensif**
Mengulas **56 studi secara mendetail** tentang model prediksi polusi udara berbasis machine learning interpretabel. Artikel ini mengkategorikan metode ke dalam *model-agnostic*, *model-specific*, dan *hybrid* dengan apik.

**Fokus Eksklusif pada Explainable AI (XAI)**
Memberikan gambaran jelas dan mendalam mengenai keunggulan **SHAP, PDP, dan LRP** dalam membuka "black-box" model prediksi, yang selama ini jarang disentuh oleh review kualitas udara lainnya.

---

### ⚠️ Kelemahan & Catatan Kritis

**Absennya Eksperimen Analisis Kausal**
Kebanyakan literatur yang ditinjau hanya fokus pada interpretasi visual dari model, tanpa mendalami eksperimen analisis kausal secara langsung untuk memverifikasi temuan XAI tersebut secara fisika atmosfer.

**Kelemahan Penanganan Multikolinieritas**
Ulasan tidak banyak memberikan kritikan tajam pada bagaimana model-model yang direview menangani fitur multikolinier (seperti suhu dan kelembapan yang sering berkorelasi kuat), yang dapat mendistorsi nilai SHAP.

**Bias Geografis Publikasi**
Generalisasi lemah karena mayoritas studi didominasi oleh paper dari China (50%) dan AS (10%), sementara literatur untuk wilayah dengan kondisi meteorologis yang berbeda (tropis/Afrika) sangat minim.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Accept** — Sangat relevan sebagai referensi komprehensif mengenai penerapan metrik interpretability (XAI) dalam prediksi polusi udara.
""",

    13: """# Review Jurnal 13
**"Interpretable machine learning framework for air quality prediction in Istanbul using Shapley additive explanations (SHAP)"**
*Enes Birinci, et al. — Stochastic Environmental Research and Risk Assessment, 2026*

---

### ✅ Kekuatan Utama

**Kerangka Komparatif yang Kokoh**
Melibatkan **7 algoritma Machine Learning berbeda** (XGBoost, Extra Trees, dll) dipadukan dengan optimalisasi hyperparameter Bayesian, menghasilkan pipeline pemodelan yang sangat kuat secara teknis.

**Pemecahan Data Spasial-Temporal yang Tepat**
Pendekatan memisahkan data berdasarkan karakteristik spasial (**urban vs rural**) dan temporal (**musim dingin vs musim panas**) sangat tepat untuk menangkap dinamika iklim lokal yang kompleks di Istanbul.

**Integrasi SHAP yang Elegan**
Model ini berhasil menggunakan **SHAP** untuk menjelaskan peran spesifik dari kondisi meteorologis dalam peningkatan polusi udara secara gamblang per lokasi.

---

### ⚠️ Kelemahan & Catatan Kritis

**Overfitting pada Data Musim Panas Pedesaan**
Terdapat bukti **overfitting** pada model pedesaan (rural Arnavutköy) di musim panas di mana kinerja prediksi untuk PM10 menurun drastis (test R²=0.61) meskipun proses latihannya menghasilkan performa baik.

**Kurangnya Variabel Antropogenik**
Model ini murni mengandalkan input meteorologi dan belum menginjeksi metrik emisi antropogenik atau tata guna lahan, yang berpotensi menjadi penyebab utama penurunan akurasi tersebut.

**Validasi SHAP yang Kurang**
Hasil interpretasi SHAP hanya ditampilkan secara visual namun tidak divalidasi lebih lanjut melalui pengujian **ablation study** untuk membuktikan bahwa fitur terpenting memang krusial bagi model.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Butuh perbaikan terkait overfitting di kawasan pedesaan saat musim panas serta validasi empiris hasil atribusi SHAP.
""",

    14: """# Review Jurnal 14
**"A Unified Approach to Interpreting Model Predictions"**
*Scott M. Lundberg, Su-In Lee — Advances in Neural Information Processing Systems (NIPS), 2017*

---

### ✅ Kekuatan Utama

**Fondasi Revolusioner untuk XAI**
Paper fundamental yang memperkenalkan **SHapley Additive exPlanations (SHAP)**. Secara brilian menyatukan enam metode interpretasi XAI yang ada sebelumnya (termasuk LIME dan DeepLIFT) ke dalam satu kerangka kerja.

**Landasan Teoretis yang Sangat Kuat**
Menawarkan landasan teori matematika dari **Game Theory** dengan memberikan kepastian jaminan untuk tiga properti krusial: *local accuracy*, *missingness*, dan *consistency*.

**Validasi Eksperimental yang Jelas**
Eksperimen secara tegas membuktikan bahwa atribusi SHAP jauh selaras dengan intuisi kognitif manusia dibandingkan baseline *feature importance* bawaan algoritma.

---

### ⚠️ Kelemahan & Catatan Kritis

**Asumsi Feature Independence yang Rentan**
Pendekatan estimasi *model-agnostic* seperti **KernelSHAP** memiliki asumsi bahwa fitur prediktor bersifat independen. Dalam konteks riil polusi udara, variabel meteorologi biasanya sangat berkorelasi (multikolinieritas), sehingga asumsi independensi berisiko mendistorsi kontribusi margin.

**Kompleksitas Komputasi yang Tinggi**
Kalkulasi nilai Shapley yang presisi bersifat **NP-Hard**. Metode aproksimasi seringkali memakan resource komputasi yang sangat masif apabila diimplementasikan pada model deep learning dengan dataset time-series besar.

**Tidak Spesifik pada Domain Lingkungan**
Karena berupa literatur teoretis ilmu komputer murni, paper ini tidak memberikan pedoman adaptasi metrik SHAP untuk data yang memiliki temporal dependensi seperti polusi udara.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Accept** — Paper wajib dan menjadi dasar absolut secara teori apabila ingin mengadopsi konsep interpretasi XAI (SHAP).
""",

    15: """# Review Jurnal 15
**"SPATIO-TEMPORAL DYNAMICS OF EXTREME PM2.5 IN INDONESIA: A WEATHER-BASED HYBRID MODELING APPROACH"**
*Dwi Indriyati, et al. — Jurnal Meteorologi dan Geofisika, 2025*

---

### ✅ Kekuatan Utama

**Fokus Eksklusif pada Iklim Tropis**
Riset mengangkat kota-kota di Indonesia (Jakarta, Semarang, Malang) yang masih minim terekspos. Ini memberikan insight yang sangat spesifik untuk dinamika polusi di ekuator.

**Integrasi Data Cuaca ERA5**
Penggabungan data observasi in-situ beresolusi tinggi (hourly) dengan data cuaca grid *reanalysis* **ERA5** adalah manuver yang cerdas untuk mengatasi keterbatasan sensor lokal.

**Pemetaan Lag-Time**
Menggabungkan regresi linier dengan model pohon non-linear (**XGBoost**) yang mampu memetakan analisis *lag time* dan menyoroti efek tertundanya akumulasi polutan akibat cuaca stagnan.

---

### ⚠️ Kelemahan & Catatan Kritis

**Akurasi Model yang Sangat Moderat**
Akurasi R² untuk model prediktif tergolong sangat rendah (maksimal di sekitar **~0.53 dengan XGBoost** untuk Jakarta, bahkan hingga 0.37 untuk Malang). Ini membuat model kurang reliabel untuk sistem peringatan dini aktual.

**Kurangnya Parameter Antropogenik**
R² yang rendah menegaskan kelemahan bahwa menggunakan **parameter cuaca saja** sebagai prediktor PM2.5 sangat tidak memadai tanpa menyertakan elemen antropogenik spasial (data lalu lintas, variabel land-use, atau citra satelit AOD).

**Eksplorasi Fitur yang Dangkal**
Studi gagal membedah interpretasi interaksi antar fiturnya dan hanya puas menggunakan algoritma *feature importance* standar bawaan tree-based, tanpa visualisasi XAI lanjutan.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Major Revision** — Sangat membutuhkan injeksi parameter emisi/antropogenik dan teknik algoritma yang lebih dalam untuk mengangkat nilai akurasi R² secara signifikan.
""",

    16: """# Review Jurnal 16
**"Diurnal and Daily Variations of PM2.5 and its Multiple-Wavelet Coherence with Meteorological Variables in Indonesia"**
*Nani Cholianawati, et al. — Aerosol and Air Quality Research, 2024*

---

### ✅ Kekuatan Utama

**Penerapan Analisis Multiple Wavelet Coherence (MWC)**
Menerapkan metode **MWC** orisinal untuk menganalisis hubungan non-stasioner frekuensi waktu (time-frequency) polutan dengan kombinasi parameter iklim kompleks secara spasial di 7 kota Indonesia.

**Penggunaan Trajektori HYSPLIT**
Menambahkan model **HYSPLIT** (Hybrid Single-Particle Lagrangian Integrated Trajectory) trajektori mundur dengan sangat meyakinkan untuk membuktikan kausalitas arah angin pembawa asap kebakaran lahan gambut di Pontianak.

**Korelasi Iklim Terpadu**
Membuktikan bahwa kombinasi Suhu + Kelembapan + Angin + Hujan secara sinergis menyetir akumulasi PM2.5 secara diurnal.

---

### ⚠️ Kelemahan & Catatan Kritis

**Durasi Data Sangat Terbatas (Hanya 1 Tahun)**
Analisis sangat terbatas pada data observasi dalam kurun 1 tahun penuh, yaitu tahun 2021. Pola pergerakan tahun 2021 sangat rentan terdistorsi dengan kebijakan anomali spesifik (seperti restriksi *lockdown* pandemi **COVID-19**).

**Risiko Edge Effects pada Wavelet**
Ekstraksi siklus temporal gelombang yang panjang dari *wavelet* menggunakan durasi data yang pendek berisiko tinggi mengalami bias di ujung rentang (**edge effects**), sehingga tidak bisa menjadi baseline generalisasi iklim jangka panjang.

**Mengabaikan Dinamika Emisi Kendaraan**
Meskipun mampu melacak emisi gambut lintas wilayah, studi ini kurang mengkalibrasi lonjakan emisi antropogenik lokal harian (seperti jam masuk kerja).

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Batasan dataset durasi tunggal (2021) memerlukan adopsi data multi-tahun untuk menghilangkan bias aktivitas restriksi pandemi.
""",

    17: """# Review Jurnal 17
**"Estimation of PM2.5 Concentration in DKI Jakarta from Sentinel-5P Imagery by Considering Meteorological Factors Using Random Forest Approach"**
*Rahmat Nur Rahman, Nur Mohammad Farda, and Ardhasena Sopaheluwakan — BIO Web of Conferences / ICoSIA, 2025*

---

### ✅ Kekuatan Utama

**Fusi Data Satelit dan Reanalisis**
Penelitian ini unggul dalam pemanfaatan data multi-sumber, mengintegrasikan data penginderaan jauh satelit **Sentinel-5P TropOMI** dengan data meteorologi (ERA5 Land) dalam rentang waktu yang cukup panjang (2021-2023).

**Pendekatan Regresi Spasial Non-Linear**
Penggunaan regresi spasial berbasis **Random Forest (RF)** sangat tepat untuk menangkap hubungan non-linear antar variabel lingkungan dari grid citra satelit ke titik pengukuran darat.

**Pemetaan Spasial Dinamis**
Model berhasil memetakan pola spasial secara visual ke dalam peta heat-map yang selaras dengan pergantian musim kemarau dan penghujan di Indonesia.

---

### ⚠️ Kelemahan & Catatan Kritis

**Validasi Stasiun Darat Sangat Terbatas**
Validasi spasial sangat terbatas karena hanya mengandalkan **8 stasiun pemantauan darat** di area metropolitan sebesar Jakarta. Titik sampel yang sedikit berisiko membuat model gagal menangkap variabilitas polusi mikro-lokal.

**Kehilangan Data Akibat Penghapusan Missing Values**
Penanganan *missing values* pada data satelit seringkali dilakukan dengan penghapusan baris (*drop rows*), menyebabkan kerugian informasi yang signifikan terutama saat tutupan awan sangat tebal.

**Kurangnya Benchmark Model**
Paper ini tidak membandingkan Random Forest dengan algoritma state-of-the-art lainnya (seperti XGBoost atau Deep Learning) dan kurang merinci teknik *hyperparameter tuning* yang digunakan, sehingga klaim RF sebagai "algoritma terbaik" kurang konklusif.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Perlu komparasi dengan model machine learning alternatif dan penjelasan limitasi dari imputasi awan pada citra satelit.
""",

    18: """# Review Jurnal 18
**"Analysis Correlation of Meteorological Factors with PM2.5 Concentrations in Forecasting Air Quality of The City of Jakarta"**
*Ade Ayu Oktaviana, Abdu Fadli Assomadi, and Joni Hermana — IOP Conf. Series: Earth and Environmental Science, 2025*

---

### ✅ Kekuatan Utama

**Analisis Korelasi Spearman yang Solid**
Penelitian ini menggunakan analisis korelasi **Spearman** yang sangat sesuai untuk mendeteksi hubungan non-linear monotonik antara faktor meteorologi (hujan, suhu, kelembaban, angin) dengan polutan.

**Adopsi Data Reanalisis ECMWF EAC4**
Penggunaan basis data reanalisis atmosfer dari satelit memberikan dimensi spasial yang baik dan menutupi blank-spot data observasi dari 5 stasiun stasioner Jakarta selama rentang waktu 2022-2023.

---

### ⚠️ Kelemahan & Catatan Kritis

**Indikasi Overfitting yang Fatal pada MLR**
Kelemahan paling fatal ada pada hasil pemodelan **Multiple Linear Regression (MLR)** yang mengklaim nilai determinasi **(R²) sebesar 0.99**. Nilai ini sangat tidak realistis dan tidak wajar untuk regresi linear sederhana pada data polusi udara yang *chaotic*, murni mengindikasikan adanya *overfitting* ekstrem atau *data leakage* dalam pemrosesan data latih.

**RMSE Tetap Tinggi Meski R² Sempurna**
Kecurigaan kesalahan metodologis diperburuk dengan pelaporan nilai kesalahan aktual (RMSE) yang masih berada di kisaran 22.95 µg/m³ meskipun R²-nya diklaim nyaris sempurna. 

**Model yang Terlalu Sederhana**
MLR gagal memetakan kompleksitas anomali atmosferik. Penggunaan algoritma linear klasik tidak lagi mampu bersaing dengan ML modern berbasis *tree* atau deep learning.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Major Revision** — Model regresi linear memiliki kesalahan indikasi overfitting yang sangat parah; wajib dievaluasi dan digantikan model machine learning non-linear.
""",

    19: """# Review Jurnal 19
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
""",

    20: """# Review Jurnal 20
**"Machine learning for air quality prediction and data analysis: Review on recent advancements, challenges, and outlooks"**
*Manal Karmoude, et al. — Science of the Total Environment, 2025*

---

### ✅ Kekuatan Utama

**Tinjauan Pustaka Sangat Holistik**
Merupakan **Systematic Literature Review** berskala masif yang mengurai anatomi 78 jurnal elit terbaru (2017-2024). Pengkategorian arsitektur sangat tertata menjadi: *non-neural*, *deep learning*, dan *hybrid spatiotemporal models*.

**Analisis Multidimensi Selain Akurasi**
Keunggulan esensial paper ini adalah analisisnya yang melampaui sekadar metrik error; ia mengkritisi **efisiensi komputasi**, penanganan *class imbalance* kejadian polusi langka, hingga isu implementasi komputasi awan pada node sensor IoT *real-time*.

**Pemaparan Roadmap XAI yang Tajam**
Mengadvokasi secara ekstensif kewajiban integrasi metodologi **Explainable AI** sebagai syarat mutlak perancangan algoritma ramah regulasi pemerintah.

---

### ⚠️ Kelemahan & Catatan Kritis

**Ketiadaan Benchmarking Kuantitatif Head-to-Head**
Karena berstatus makalah ulasan, tidak dilakukan *quantitative benchmarking* secara langsung pada *open dataset* seragam untuk mendemonstrasikan keunggulan model-model canggih tersebut secara objektif di lab yang sama.

**Diskusi Reinforcement Learning yang Dangkal**
Pengenalan terhadap aplikasi **Reinforcement Learning** (RL) untuk perancangan agen pengontrol kebijakan emisi dirasa terlalu singkat proporsinya jika dibandingkan dengan porsi *Supervised Learning*.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Accept** — Ulasan literatur tingkat tinggi (*high-impact*) yang menyediakan *roadmap* krusial bagi peneliti domain kecerdasan buatan lingkungan.
""",

    21: """# Review Jurnal 21
**"A Framework for Air Pollution Monitoring in Smart Cities by Using IoT and Smart Sensors"**
*Arshad Ali — Informatica, 2022*

---

### ✅ Kekuatan Utama

**Desain Arsitektur Multi-Layer Konseptual**
Paper merancang konsep arsitektur yang komprehensif bagi pemantauan polusi udara berbasis **Internet of Things (IoT)** skala kota cerdas (*smart city*).

**Pilihan Protokol Komunikasi Efisien**
Pendefinisian standar perangkat keras yang terintegrasi secara spesifik dengan protokol pengiriman data rendah daya (**ZigBee**) menuntaskan problem kendala umur baterai pada instalasi sensor terpencil.

---

### ⚠️ Kelemahan & Catatan Kritis

**Ketiadaan Implementasi Fisik Sama Sekali**
Studi ini terkurung penuh pada ranah simulasi teoretis. **Sama sekali tidak ada purwarupa fisik (*hardware prototype*)** yang dibangun di lapangan untuk divalidasi keandalannya di ruang terbuka.

**Validasi Data yang Nihil**
Tanpa pengujian empiris, paper gagal memberikan kepastian akurasi pembacaan polutan, latensi transmisi jaringan saat padat data, rasio *packet loss*, maupun efisiensi konsumsi daya aktual.

**Pustaka Referensi yang Mulai Usang**
Sebagian besar referensi teknologi komputasi mikrokontroler yang diajukan sudah tertinggal zaman jika disandingkan dengan standar perangkat Edge-AI (*micro-NPU*) masa kini.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Reject / Major Revision** — Membutuhkan pengadaan dan eksperimentasi *hardware* purwarupa nyata yang menghasilkan data lapangan untuk membuktikan *framework* teoretis yang diajukan.
""",

    22: """# Review Jurnal 22
**"Air quality prediction from images in Indonesia: enhancing model explainability through visual explanation with AQI-net and grad-CAM"**
*Muhammad Labib Alauddin, Novanto Yudistira, and Muhammad Arif Rahman — Environmental Data Science, 2025*

---

### ✅ Kekuatan Utama

**Pergeseran Paradigma Data: Computer Vision**
Sangat inovatif. Penelitian ini meninggalkan sensor fisika kimia tradisional dan beralih mengestimasi tingkat AQI lewat ektraksi filter kabut gambar kamera *smartphone* dengan metode **Computer Vision**.

**Optimalisasi Arsitektur AQI-Net**
Mendesain arsitektur CNN khusus (**AQI-Net**) yang efisien, mampu mereduksi parameter drastis dari baseline VGG-16, namun secara presisi mengamankan akurasi hingga **99.81%** pada dataset 11.000 citra terbuka di Jawa.

**Kecemerlangan XAI berbasis Visual (Grad-CAM)**
Penerapan algoritma **Grad-CAM** (*Gradient-weighted Class Activation Mapping*) sebagai teknik *Explainable AI* sangat brilian untuk menerangi area piksel mana yang dijadikan dasar pengambilan keputusan oleh CNN.

---

### ⚠️ Kelemahan & Catatan Kritis

**Fenomena Shortcut Learning Terbongkar XAI**
Peta aktivasi visual (Grad-CAM) justru secara tidak sengaja menyingkap kelemahan kognitif model: model terbukti melakukan **shortcut learning**. Pada klasifikasi kondisi "Good/Baik", jaringan saraf ternyata justru mendeteksi piksel objek "struktur gedung/tepian atap" alih-alih mengukur visibilitas kejernihan langit secara murni.

**Ketidakmampuan Analisis Tanpa Cahaya Matahari**
Metodologi ekstraksi ketebalan kabut optis ini secara inheren **lumpuh total di malam hari** karena murni dilatih atas dataset siang berpencahayaan cerah.

**Bias Klasifikasi Gambar Statis**
Algoritma belum kebal terhadap bias citra sekunder (misal: asap kendaraan lokal instan, flare matahari) yang dapat mencemari klasifikasi kelas tingkat polusi udara makro.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Pendekatannya sangat futuristik, namun sangat krusial untuk melatih ulang pembobotan citra langit dan mitigasi kebergantungan pola geometris objek non-langit (*shortcut learning*).
"""
}

for idx, content in data.items():
    filename = f"Review_{idx:02d}.md"
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Updated expanded deep review text for {filename}")

print("Selesai memulihkan dan memperdalam teks untuk Jurnal 11-22!")
