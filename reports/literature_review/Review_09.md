# Review Jurnal 09
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