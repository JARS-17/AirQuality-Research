# Catatan Teknis: Penjelasan Alur Penelitian
## Prediksi PM2.5 di Cekungan Bandung Menggunakan LSTM dengan Interpretasi SHAP
**Kerja Praktik — PRSDI BRIN 2026 | Ginda Fajar Riadi Marpaung**

---

## Daftar Isi
1. [Definisi Masalah](#1-definisi-masalah)
2. [Pengumpulan Data](#2-pengumpulan-data)
3. [Exploratory Data Analysis EDA](#3-exploratory-data-analysis-eda)
4. [Pra-pemrosesan Data](#4-pra-pemrosesan-data)
5. [Pemodelan Baseline](#5-pemodelan-baseline)
6. [Pemodelan LSTM Deep Learning](#6-pemodelan-lstm-deep-learning)
7. [Evaluasi dan Perbandingan](#7-evaluasi-dan-perbandingan)
8. [Interpretasi Model SHAP](#8-interpretasi-model-shap)

---

## 1. Definisi Masalah

### Permasalahan
Kualitas udara di Cekungan Bandung merupakan isu lingkungan yang serius. Topografi cekungan yang dikelilingi pegunungan menyebabkan polutan, khususnya PM2.5 (partikel berdiameter < 2.5 mikrometer), sulit terdispersi secara vertikal dan horizontal sehingga mudah terakumulasi di permukaan.

Meskipun model Deep Learning seperti LSTM terbukti akurat dalam memprediksi data deret waktu, model ini dikritik karena sifatnya yang **Black-Box**: mampu menghasilkan angka prediksi yang tepat, namun tidak dapat menjelaskan mengapa prediksi tersebut dihasilkan. Padahal, pengambil kebijakan lingkungan tidak hanya membutuhkan angka prediksi, melainkan juga pemahaman kausal mengenai faktor meteorologi apa yang memicu lonjakan polusi.

### Celah Riset (Research Gap)
Riset prediksi kualitas udara menggunakan Machine Learning di Indonesia masih sangat terpusat di Jakarta dan Yogyakarta, dan mayoritas berhenti pada angka akurasi (RMSE, MAE) tanpa interpretasi kausalitas. Penelitian khusus untuk wilayah topografi cekungan (seperti Cekungan Bandung) dengan pendekatan Explainable AI (XAI) masih sangat terbatas dalam literatur lokal.

### Pertanyaan Penelitian
1. Bagaimana kinerja arsitektur Stacked LSTM dalam memprediksi konsentrasi PM2.5 per jam di Cekungan Bandung berdasarkan variabel meteorologi ERA5?
2. Seberapa besar perbedaan akurasi antara Stacked LSTM dengan Random Forest dan XGBoost berdasarkan metrik RMSE, MAE, dan R-squared?
3. Variabel meteorologi apa saja yang berkontribusi signifikan terhadap fluktuasi PM2.5 berdasarkan analisis SHAP?

---

## 2. Pengumpulan Data

### 2.1 Data Target (Y): PM2.5 — OpenAQ
- **Sumber:** Platform OpenAQ (open-source air quality data)
- **Sensor Utama:** ID 121867, berlokasi di wilayah Cekungan Bandung
- **Sensor Pembanding:** ID 238875 (digunakan sementara untuk validasi)
- **Resolusi Waktu:** Per jam (hourly)
- **Periode:** November 2022 - November 2023
- **Satuan:** ug/m3 (mikrogram per meter kubik)
- **Alasan Memilih Sensor 121867:** Jumlah data lebih lengkap (~16.500 vs ~8.500 titik data) dan periode observasi lebih panjang

### 2.2 Data Fitur (X): Meteorologi ERA5 — ECMWF
- **Sumber:** ERA5 Hourly Reanalysis, Copernicus Climate Data Store (CDS)
- **Resolusi Spasial:** ~31 km (interpolasi ke titik koordinat Bandung)
- **Resolusi Waktu:** Per jam (hourly)
- **Periode:** November 2022 - November 2023

Variabel yang digunakan:

| No | Variabel | Kolom | Satuan | Relevansi Fisika |
|----|----------|-------|--------|-----------------|
| 1 | Tinggi Lapisan Batas Atmosfer | tinggi_lapisan_batas_m | Meter | Ruang vertikal dispersi polutan |
| 2 | Kolom Ozon | ozon_kolom_kg_m2 | kg/m2 | Reaksi kimia atmosfer |
| 3 | Uap Air Kolom | uap_air_kolom_kg_m2 | kg/m2 | Beban kelembapan total atmosfer |
| 4 | Tutupan Awan | tutupan_awan_01 | 0-1 | Radiasi matahari dan konveksi |
| 5 | Suhu Udara (2m) | suhu_2m_C | Celcius | Konveksi termal dan dispersi |
| 6 | Titik Embun | titik_embun_C | Celcius | Kelembapan absolut udara |
| 7 | Tekanan Udara | tekanan_hPa | hPa | Stabilitas atmosfer |
| 8 | Curah Hujan | curah_hujan_mm | mm | Wet deposition (pencuci polutan) |
| 9 | Kecepatan Angin | kecepatan_angin_kmh | km/jam | Dispersi horizontal polutan |
| 10 | Arah Angin | arah_angin_derajat | Derajat | Asal massa udara |
| 11 | Kelembapan Relatif | kelembapan_persen | % | PM2.5 bersifat higroskopis |

---

## 3. Exploratory Data Analysis (EDA)

**Notebook:** notebooks/01_exploratory/01_EDA_PM25_ERA5.ipynb

### 3.1 Perbandingan Dua Sensor
Sensor 121867 dipilih karena data lebih lengkap (~16.500 titik data vs ~8.500 di Sensor 238875).

### 3.2 Deteksi Outlier (Metode IQR)
- Batas bawah: max(0, Q1 - 1.5 x IQR)
- Batas atas: Q3 + 1.5 x IQR
- Data outlier tetap di-imputasi (tidak dihapus) untuk menjaga kontinuitas temporal.

### 3.3 Pola Diurnal (Per Jam)
PM2.5 memuncak dua kali dalam sehari:
- **Pagi (06:00-08:00 WIB):** Jam sibuk + lapisan batas atmosfer masih rendah
- **Malam (18:00-23:00 WIB):** Aktivitas malam + lapisan batas mengempis setelah matahari terbenam

### 3.4 Pola Musiman (Per Bulan)
PM2.5 secara konsisten lebih tinggi pada musim kemarau (Juni-September) karena:
1. Tidak ada curah hujan sebagai pencuci alami polutan
2. Lapisan batas atmosfer lebih rendah di musim kemarau
3. Arah angin membawa massa udara dari wilayah padat

### 3.5 Korelasi ERA5 vs PM2.5
Korelasi Pearson dihitung antara setiap variabel ERA5 dan PM2.5 untuk mengetahui variabel cuaca mana yang paling berpengaruh sebelum memasuki tahap pemodelan.

---

## 4. Pra-pemrosesan Data

**Notebook:** notebooks/02_preprocessing/02_Preprocessing_FeatureEngineering.ipynb

### 4.1 Penanganan Data Hilang
- **Metode:** Interpolasi Linear berbasis Waktu: df['pm25'].interpolate(method='time')
- **Alasan:** Data time-series tidak boleh diisi dengan rata-rata global karena akan merusak tren temporal
- **Hasil:** 0 missing values setelah interpolasi

### 4.2 Feature Engineering

**a. Enkoding Waktu Siklik:**
Jam 23:00 dan 00:00 sebenarnya berjarak 1 jam, bukan 23. Enkoding sinus/cosinus menyelesaikan masalah ini:
```
hour_sin  = sin(jam  x 2*pi/24)
hour_cos  = cos(jam  x 2*pi/24)
month_sin = sin((bulan-1) x 2*pi/12)
month_cos = cos((bulan-1) x 2*pi/12)
```

**b. Variabel Musim Biner:**
```
is_dry_season = 1 jika bulan termasuk Juni-September (Kemarau)
              = 0 untuk bulan lainnya (Hujan)
```

**c. Fitur Historis (Lag Features):**
```
pm25_lag_1h  = PM2.5 satu jam sebelumnya (T-1)
pm25_lag_24h = PM2.5 dua puluh empat jam sebelumnya (T-24)
```
24 baris pertama di-drop karena menghasilkan NaN akibat operasi shift.

### 4.3 Train-Test Split (Kronologis)
- **Dilarang:** Pengacakan random karena menyebabkan data leakage dari masa depan ke masa lalu
- **Rasio:** 80% Latih / 20% Uji secara berurutan waktu
- **Training:** Nov 2022 - Sep 2023
- **Testing:** Sep 2023 - Nov 2023

### 4.4 Normalisasi MinMax
- Rentang output: [0, 1]
- Aturan: Scaler di-fit HANYA pada data Training, lalu di-transform ke data Testing
- Disimpan: scaler_X.pkl dan scaler_y.pkl untuk inversi prediksi ke ug/m3

### 4.5 Transformasi Tensor 3D (Sliding Window)
LSTM membutuhkan input 3D: [Jumlah Sampel, Jendela Waktu, Jumlah Fitur]
- TIME_STEPS = 24 jam
- Untuk prediksi jam ke-25, model diberi 24 jam data sebelumnya sebagai konteks
- Hasil: X_train shape = (N_train, 24, 20)

---

## 5. Pemodelan Baseline

**Notebook:** notebooks/03_modeling/03_Baseline_Models.ipynb

### Model 1: Random Forest Regressor
- **Konfigurasi:** 100 estimators, random_state=42
- **Hasil:** RMSE = 7.69 ug/m3 | MAE = 4.67 ug/m3 | R2 = 0.7563

### Model 2: XGBoost Regressor
- **Konfigurasi:** 100 estimators, learning_rate=0.1, max_depth=6
- **Hasil:** RMSE = 9.07 ug/m3 | MAE = 5.75 ug/m3 | R2 = 0.6606

### Catatan Evaluasi
Semua metrik dihitung setelah inversi skala (0-1 kembali ke ug/m3) menggunakan scaler_y.inverse_transform().

---

## 6. Pemodelan LSTM (Deep Learning)

**Notebook:** notebooks/03_modeling/04_LSTM_Model.ipynb

### Arsitektur Stacked LSTM

```
Input         : (24 jam, 20 fitur)
LSTM Layer 1  : 64 unit, return_sequences=True
Dropout       : 0.2
LSTM Layer 2  : 32 unit, return_sequences=False
Dropout       : 0.2
Dense Output  : 1 unit (prediksi PM2.5 t+1)
```

### Konfigurasi Training
| Parameter | Nilai |
|-----------|-------|
| Optimizer | Adam (lr=0.001) |
| Loss | Mean Squared Error |
| Epochs maks | 50 |
| Batch Size | 32 |
| Validation Split | 10% dari data latih |
| Early Stopping | patience=10, monitor val_loss |

### Mengapa LSTM Lebih Cocok dari RF/XGBoost?
LSTM memiliki mekanisme gerbang memori (input gate, forget gate, output gate) yang memungkinkannya secara selektif mengingat informasi dari masa lalu yang jauh. RF dan XGBoost tidak memiliki memori temporal ini.

### Hasil Evaluasi Final
| Metrik | Nilai |
|--------|-------|
| RMSE | 7.08 ug/m3 |
| MAE | 4.34 ug/m3 |
| R-squared | 0.7957 |

---

## 7. Evaluasi dan Perbandingan

### Tabel Komparatif Akhir

| Model | RMSE (ug/m3) | MAE (ug/m3) | R-squared |
|-------|-------------|------------|-----------|
| XGBoost | 9.07 | 5.75 | 0.6606 |
| Random Forest | 7.69 | 4.67 | 0.7563 |
| Stacked LSTM (Usulan) | 7.08 | 4.34 | 0.7957 |

### Interpretasi Metrik
- **RMSE 7.08:** Model rata-rata meleset plus minus 7.08 ug/m3 dari nilai aktual. Sensitif terhadap lonjakan besar.
- **MAE 4.34:** Prediksi rata-rata meleset plus minus 4.34 ug/m3. Lebih robust terhadap outlier.
- **R-squared 0.80:** Model menjelaskan 80% variansi pola naik-turun PM2.5. Sisa 20% umumnya adalah lonjakan ekstrem mendadak yang tidak tertangkap.

---

## 8. Interpretasi Model (SHAP)

**Notebook:** notebooks/04_interpretation/05_SHAP_Interpretation_LSTM.ipynb

### Mengapa SHAP?
SHAP (SHapley Additive Explanations) didasarkan pada Shapley Value dari Teori Permainan. SHAP mengalokasikan kredit kontribusi setiap fitur secara adil dan memenuhi tiga sifat matematis:
1. **Local Accuracy:** Total SHAP semua fitur = prediksi model - base value
2. **Missingness:** Fitur tidak berpengaruh mendapat SHAP = 0
3. **Consistency:** Fitur lebih berpengaruh tidak akan mendapat SHAP lebih kecil

### Mengapa KernelExplainer?
- DeepExplainer: Bug get_session di TensorFlow 2.15+
- GradientExplainer: Tidak kompatibel Keras 3
- **KernelExplainer:** Model-agnostic, bekerja untuk sembarang fungsi prediksi. DIPILIH.

### Fungsi Wrapper 2D ke 3D
KernelExplainer hanya menerima data 2D, tetapi LSTM butuh 3D. Solusi: fungsi wrapper.

```python
def lstm_predict_wrapper(x_2d_flat):
    x_3d = x_2d_flat.reshape(-1, TIME_STEPS, N_fitur)
    return model.predict(x_3d, verbose=0).flatten()
```

### Hasil SHAP Global (Beeswarm Plot)
Tiga fitur paling dominan:
1. **tinggi_lapisan_batas_m:** Faktor paling dominan. Lapisan batas rendah = polutan terjebak = PM2.5 naik. Konsisten dengan fisika atmosfer.
2. **pm25_lag_1h:** Autokorelasi temporal kuat. Kondisi polusi jam lalu adalah prediktor terkuat kondisi sekarang.
3. **kelembapan_persen:** PM2.5 bersifat higroskopis. Kelembapan mempengaruhi konsentrasi secara non-linear.

### Rumus Additivitas SHAP
```
Prediksi(x) = Base Value + Jumlah SHAP_i(x) untuk semua fitur i
```
Di mana Base Value adalah rata-rata prediksi model pada seluruh data background.

---

## Ringkasan Alur Teknis

```
Data Mentah (PM2.5 OpenAQ + ERA5 ECMWF)
        |
[EDA] Analisis distribusi, pola diurnal, musiman, korelasi
        |
[Preprocessing] Interpolasi -> Feature Engineering -> MinMax -> Sliding Window 24h
        |
[Baseline] Random Forest RMSE 7.69 | XGBoost RMSE 9.07
        |
[LSTM Stacked 2-Layer 64-32 unit] -> RMSE 7.08 | MAE 4.34 | R2 0.80
        |
[SHAP KernelExplainer] -> Tinggi Lapisan Batas dan Lag PM2.5 = Faktor Dominan
        |
[Kesimpulan] Model akurat + Faktor cuaca pendorong teridentifikasi secara kausal
```

---
*Dokumen ini merangkum seluruh proses teknis berdasarkan notebook yang telah dikerjakan selama Kerja Praktik di PRSDI BRIN, 2026.*
