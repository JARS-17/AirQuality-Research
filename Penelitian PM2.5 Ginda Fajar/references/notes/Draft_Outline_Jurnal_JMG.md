# DRAF JURNAL - JMG BMKG
*(Jurnal Meteorologi dan Geofisika)*

---
**Ketentuan Format JMG BMKG:**
*   **Panjang Artikel:** 3.000 - 4.000 Kata
*   **Font:** Times New Roman 10pt, Spasi Tunggal
*   **Plagiasi & AI:** < 15% Similarity, < 30% AI Detection
*   **Struktur Standar:** IMRaD (Introduction, Methods, Results, and Discussion)

---

## 1. TITLE (Judul)
**Usulan Judul:** Spatio-Temporal Prediction of PM2.5 in the Bandung Basin Using Bidirectional LSTM and SHAP Analysis
*(Prediksi Spasial-Temporal PM2.5 di Cekungan Bandung Menggunakan Bidirectional LSTM dan Analisis SHAP)*

## 2. ABSTRACT (Abstrak)
*(Ditulis paling akhir. Maksimal 250 kata. Memuat intisari Latar Belakang, Tujuan, Metode, Hasil Utama RMSE, dan Kesimpulan).*
**Keywords:** PM2.5, Bandung Basin, Deep Learning, BiLSTM, Explainable AI, SHAP

## 3. INTRODUCTION (Pendahuluan)
*(Target Kata: ~600 kata)*
*   **Paragraf 1 (Konteks Global & Lokal):** Bahaya PM2.5 secara global dan mengapa letak geografis/topografi cekungan (seperti Bandung) membuat polusi terperangkap.
*   **Paragraf 2 (Peran Meteorologi):** Bagaimana faktor cuaca (hujan, angin, suhu, lapisan batas atmosfer/BLH) mempengaruhi pergerakan PM2.5, terutama di daerah iklim tropis dengan siklus musim kemarau dan hujan (Kutip Jurnal: Cholianawati et al.).
*   **Paragraf 3 (Gap Penelitian):** Mayoritas riset tentang ML/DL untuk PM2.5 dilakukan di luar wilayah tropis (China/AS). Di Indonesia, pemodelan kualitas udara yang menggabungkan LSTM dengan analisis interpretasi kausal (SHAP) terhadap data meteorologi bersolusi tinggi (ERA5) masih sangat terbatas (Kutip Jurnal: Houdou et al., Yang et al.).
*   **Paragraf 4 (Tujuan & Kebaruan):** Penelitian ini bertujuan mengaplikasikan model Stacked LSTM dan BiLSTM untuk prediksi PM2.5 di Cekungan Bandung, serta menggunakan *SHapley Additive exPlanations* (SHAP) untuk membongkar "kotak hitam" AI dan mencari tahu parameter meteorologi mana yang paling dominan.

## 4. MATERIALS AND METHODS (Materi dan Metode)
*(Target Kata: ~800 kata)*
*   **4.1. Data Acquitision (Akuisisi Data):**
    *   Lokasi studi: Cekungan Bandung.
    *   Dataset 1: Observasi PM2.5 in-situ (Sensor) dengan resolusi per jam (1 Tahun: Nov 2022 - Nov 2023). Alasan 1 tahun: kontinuitas dan kelengkapan musiman.
    *   Dataset 2: Data reanalisis cuaca satelit ECMWF Copernicus ERA5.
*   **4.2. Data Preprocessing (Prapemrosesan):**
    *   Pembersihan data (*missing values* imputasi).
    *   Pembuatan fitur waktu (Cyclical Encoding: *hour_sin*, *month_sin*) dan fitur musim kemarau (*is_dry_season*).
    *   Transformasi jendela waktu (*Sliding Window* 24-jam) untuk input ke dalam Deep Learning.
*   **4.3. Model Architecture (Arsitektur Model):**
    *   Penjelasan matematis/arsitektur LSTM dan Bidirectional LSTM (BiLSTM).
    *   Penjelasan skema pembagian data secara kronologis (*Chronological Split*): 70% Train, 10% Validasi (untuk *Early Stopping*), 20% Test.
*   **4.4. SHAP Interpretation (Interpretasi SHAP):**
    *   Bagaimana *KernelExplainer* digunakan untuk mendapatkan nilai Shapley dari prediksi terbaik.

## 5. RESULTS AND DISCUSSION (Hasil dan Pembahasan)
*(Target Kata: ~1.500 kata)*
*   **5.1. Data Exploration Results (Hasil Eksplorasi):**
    *   (Grafik) Tren musiman PM2.5. PM2.5 memuncak di musim kemarau (Juli-Agustus) dan turun di musim hujan.
*   **5.2. Prediction Performance (Kinerja Prediksi):**
    *   (Tabel) Perbandingan metrik RMSE, MAE, R² antara Random Forest, XGBoost, LSTM, dan BiLSTM.
    *   Pembahasan mengapa BiLSTM/LSTM unggul menangkap pola sekuensial dibandingkan Baseline.
    *   (Grafik) Plot garis prediksi vs aktual (2 Minggu Pertama Data Test).
*   **5.3. Interpretability with SHAP (Interpretasi Kausalitas):**
    *   (Grafik) SHAP Summary Plot / Bar Plot.
    *   **Diskusi Kritis:** Pembahasan hasil SHAP. Mengapa variabel *Boundary Layer Height* dan *Kecepatan Angin* menjadi variabel meteorologi penentu yang mendispersi polutan dari cekungan. Pembahasan efek *wash-out* dari curah hujan.

## 6. CONCLUSION (Kesimpulan)
*(Target Kata: ~300 kata)*
*   Menjawab tujuan: Model BiLSTM berhasil memprediksi PM2.5 dengan akurasi tertinggi (RMSE = ...).
*   Kesimpulan analitik: Model interpretasi membuktikan secara empiris bahwa selain polusi masa lalu, tinggi lapisan batas atmosfer dan fenomena kemarau adalah pendorong utama stagnasi PM2.5 di Bandung.
*   Keterbatasan: Tidak ada metrik emisi lalu lintas/pabrik secara langsung.
*   Saran studi lanjutan.

## 7. ACKNOWLEDGMENTS (Ucapan Terima Kasih)
*(Opsional: Kepada BRIN dan Dosen Pembimbing)*

## 8. REFERENCES (Daftar Pustaka)
*(Format: APA/IEEE sesuai template, minimal 20 referensi di mana 80% berasal dari 5 tahun terakhir).*
