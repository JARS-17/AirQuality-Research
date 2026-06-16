import os

out_dir = r"D:\Kuliah Praktik\KP BRIN\reports\literature_review"
os.makedirs(out_dir, exist_ok=True)

data = {
    7: """# Review Jurnal 07
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
""",

    8: """# Review Jurnal 08
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
""",

    9: """# Review Jurnal 09
**"Application of CNN-LSTM Algorithm for PM2.5 Concentration Forecasting in the Beijing-Tianjin-Hebei Metropolitan Area"**
*Su, Li, Liu, Guo, Huang & Hu — Atmosphere, 2023*

---

### ✅ Kekuatan

**Cakupan Spasial yang Signifikan**
Menggunakan data dari 10 kota sekaligus dalam satu kawasan metropolitan (Beijing-Tianjin-Hebei) adalah keunggulan utama paper ini. Berbeda dengan mayoritas penelitian yang hanya fokus pada satu kota, pendekatan multi-kota ini secara langsung menjawab kritik umum tentang keterbatasan generalisasi spasial model. Uji validasi silang antar tahun (2021 vs 2022) semakin memperkuat klaim transferabilitas model.

**Integrasi Precipitable Water Vapor (PWV) sebagai Inovasi Input**
Memasukkan ERA5-PWV sebagai variabel tambahan di luar faktor meteorologi konvensional adalah kontribusi yang terdiferensiasi dan dilandasi justifikasi ilmiah yang memadai. Analisis korelasi Spearman antara PWV dan PM2.5 di setiap kota dilakukan secara sistematis sebelum model dibangun — ini adalah contoh pendekatan yang *data-driven* dan tidak ad hoc.

**Desain Eksperimen yang Kontekstual dan Relevan**
Memfokuskan periode prediksi pada Hari Nasional Tiongkok (National Day) adalah keputusan yang cerdas secara kontekstual. Periode ini memiliki karakteristik polusi yang khas akibat lonjakan pergerakan manusia dan kendaraan, sehingga memberikan tantangan prediksi yang lebih realistis dibanding periode biasa. Ini membuat paper memiliki relevansi kebijakan yang konkret.

**Analisis Korelasi yang Menyeluruh**
Tabel korelasi Spearman antara PM2.5 dengan polutan lain dan faktor meteorologi untuk 10 kota disajikan secara lengkap dan disertai interpretasi yang kontekstual per kota. Penulis menjelaskan mengapa korelasi beberapa variabel berbeda antar kota (misalnya SO2 negatif di Beijing), yang menunjukkan pemahaman yang baik terhadap mekanisme atmosferik lokal.

**Transparansi Arsitektur dan Hyperparameter**
Tabel parameter CNN-LSTM beserta rentang penyesuaiannya (Tabel 3) disajikan secara eksplisit. Penggunaan Batch Normalization dan fungsi aktivasi ReLU untuk mencegah vanishing gradient juga didokumentasikan dengan baik.

---

### ⚠️ Kelemahan & Catatan Kritis

**Periode Training yang Sangat Pendek dan Sangat Spesifik**
Ini adalah kelemahan terbesar. Model dilatih hanya menggunakan data satu bulan (September 2021/2022) dan divalidasi pada 7 hari pertama Oktober. Dengan window training hanya 720 jam, model tidak pernah "melihat" pola musiman lain (musim dingin Beijing terkenal dengan episode polusi parah). Klaim tentang kemampuan generalisasi model terasa berlebihan mengingat keterbatasan ini.

**Baseline Pembanding yang Terlalu Lemah**
Model CNN-LSTM hanya dibandingkan dengan LSTM dan BPNN. Tidak ada perbandingan dengan model yang lebih kompetitif seperti Transformer, GRU, atau model hybrid lain. Dalam era 2023 ketika paper ini terbit, klaim keunggulan tanpa membandingkan dengan arsitektur yang lebih modern terasa kurang meyakinkan.

**MAPE yang Tinggi Sebagai Indikasi Keterbatasan**
Rata-rata MAPE CNN-LSTM masih mencapai 35.31% untuk 2022 dan 25% untuk 2021. Untuk prediksi 168 jam (7 hari) ke depan nilai ini mungkin wajar, namun paper tidak mendiskusikan batas praktis kelayakan prediksi — kapan model ini cukup akurat untuk benar-benar digunakan dalam pengambilan keputusan kebijakan?

**Inkonsistensi Performa di Tangshan**
Di Tangshan, MAPE CNN-LSTM (46.14%) justru lebih buruk dari LSTM (31.59%). Penulis mengakui ini dan memberikan saran agar prediksi di Tangshan dibatasi maksimal 120 jam, namun tidak ada penjelasan mendalam mengapa CNN-LSTM gagal di kota ini. Apakah ada karakteristik polusi industrial Tangshan yang tidak dapat ditangkap CNN?

**Tidak Ada Feature Importance Analysis**
Dengan 11+ variabel input per kota yang berbeda-beda, sangat relevan untuk mengetahui variabel mana yang paling berkontribusi pada prediksi di masing-masing kota. Tidak adanya analisis seperti SHAP atau permutation importance membuat model menjadi *black box* yang sulit diinterpretasi oleh pengambil kebijakan.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Paper ini memiliki desain eksperimen yang kuat dan kontribusi spasial yang jelas. Perbaikan pada diskusi keterbatasan temporal data training, penambahan baseline model yang lebih kompetitif, dan analisis feature importance akan memperkuat signifikansi kontribusinya secara substansial.
""",

    10: """# Review Jurnal 10
**"Statistical and Machine Learning Models for Air Quality: A Systematic Review of Methods and Challenges"**
*Ballesteros Peinado, Guarda, Herrera-Vidal, Minnaard & Coronado-Hernández — Algorithms, 2025*

---

### ✅ Kekuatan

**Cakupan Corpus yang Sangat Luas**
Menganalisis 412 artikel peer-reviewed dari 2016–2025 menggunakan protokol PRISMA 2020 adalah skala yang substansial. Proses filtering berlapis (dari 258.035 dokumen awal hingga 412 artikel final) didokumentasikan secara transparan dengan flowchart yang jelas, memenuhi standar reprodusibilitas systematic review modern.

**Pendekatan Bibliometrik yang Inovatif**
Penggunaan analisis "science tree" dengan tiga level hierarki (Roots/Classics, Trunk/Structural, Leaves/Perspectives) dan visualisasi jaringan co-citation menggunakan Gephi adalah pendekatan yang memberikan perspektif epistemologis yang lebih kaya dibanding systematic review konvensional. Ini membantu pembaca memahami evolusi dan kematangan bidang ini secara lebih intuitif.

**Identifikasi Kesenjangan Geografis yang Penting**
Temuan bahwa 73.2% studi terkonsentrasi di Asia sementara Amerika Latin hanya 1.03% dan Afrika 5.15% adalah kontribusi yang sangat berharga untuk agenda penelitian global. Kesenjangan ini memiliki implikasi nyata karena kedua wilayah tersebut justru menghadapi tantangan kualitas udara yang serius namun kekurangan model prediktif yang kontekstual.

**Sistematisasi Variabel dan Metrik yang Komprehensif**
Mengidentifikasi 1.177 variabel prediktor dan 307 metrik evaluasi dari seluruh korpus memberikan peta yang sangat berguna tentang praktik komunitas peneliti. Temuan bahwa CO adalah variabel terbanyak digunakan (35%) dan RMSE/MSE mendominasi metrik evaluasi membuka diskusi penting tentang standardisasi metodologi.

**Tiga Research Questions yang Terstruktur dengan Baik**
Pembagian menjadi RQ1 (faktor yang memengaruhi kualitas udara), RQ2 (perbandingan ML vs statistik), dan RQ3 (tantangan implementasi) memberikan kerangka analisis yang koheren. Framework perbandingan model di Tabel 2 (Challenges vs Opportunities) juga menjadi referensi yang actionable bagi peneliti berikutnya.

---

### ⚠️ Kelemahan & Catatan Kritis

**Dominasi Akurasi atas Interpretabilitas dalam Analisis**
Paper ini mengidentifikasi bahwa 70.8% studi hanya fokus pada akurasi sementara interpretabilitas hanya 20.8% — namun ironisnya, paper ini sendiri tidak sepenuhnya melampaui masalah tersebut. Analisis perbandingan performa model (Bagian 3.4) hanya berdasarkan 24 studi yang eksplisit membandingkan keduanya, sehingga representativitasnya terbatas.

**Definisi "Hybrid Model" yang Tidak Konsisten**
Paper mengkategorikan CNN-LSTM sebagai "hybrid or advanced model" terpisah dari kategori ML, namun dalam literatur yang dianalisis CNN-LSTM juga muncul di kategori ML (8 entri di Figure 5 dan 7 entri di Figure 6). Tumpang tindih kategorisasi ini mengurangi kejelasan taksonomi model yang disajikan.

**Analisis Kuantitatif Perbandingan ML vs Statistik yang Dangkal**
Meskipun RQ2 bertanya tentang perbandingan akurasi ML dan model statistik, paper hanya mampu menganalisis 24 studi yang secara eksplisit membandingkan keduanya (hanya ~5.8% dari 412 artikel). Tidak ada meta-analisis kuantitatif seperti effect size atau pooled performance metrics. Kesimpulan bahwa "ML outperforms statistical models" menjadi generalisasi yang kurang dapat diverifikasi secara ketat.

**Tidak Ada Analisis Temporal Tren Performa Model**
Meskipun paper mencatat pertumbuhan publikasi dari 2 artikel (2016) hingga 106 artikel (2024), tidak ada analisis apakah akurasi model juga membaik secara konsisten seiring waktu. Pertanyaan "apakah semakin baru semakin akurat?" tidak dijawab, padahal ini sangat relevan untuk memposisikan arah penelitian.

**Batasan Lingkup yang Tidak Disebutkan di Awal**
Paper mengecualikan studi dari konteks pertambangan terbuka (open-cast mining) dengan alasan fokus pada lingkungan ambient. Namun, pengecualian ini baru disebutkan di bagian Quality Assessment (Seksi 2.4), bukan di bagian Introduction atau Methodology awal. Ini bisa menyesatkan pembaca yang tidak membaca paper secara menyeluruh.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Kontribusi untuk Agenda Riset | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Minor Revision / Accept** — Paper ini adalah kontribusi bernilai tinggi sebagai referensi landasan (*landmark reference*) bagi peneliti di bidang prediksi kualitas udara. Kelemahannya terletak pada analisis komparatif yang kurang mendalam secara kuantitatif. Penambahan meta-analisis performa dan klarifikasi kategorisasi model akan meningkatkan kekuatan kontribusinya secara signifikan.
"""
}

for idx, content in data.items():
    filename = f"Review_{idx:02d}.md"
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Updated full text for {filename}")

print("Selesai memulihkan teks penuh untuk Jurnal 7-10!")
