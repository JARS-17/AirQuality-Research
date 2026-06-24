# Penjelasan Kode: Fase 2 (Preprocessing & Feature Engineering)

Dokumen ini berisi penjelasan detail baris per baris mengenai alur kerja dan logika kode di dalam Jupyter Notebook `02_Preprocessing_FeatureEngineering.ipynb`. 

Fase ini mengubah dataset *raw* menjadi matriks angka murni yang siap ditelan oleh algoritma Jaringan Saraf Tiruan (*Deep Learning/LSTM*). Metodologi ini merujuk pada *best-practices* di berbagai literatur jurnal akademik prediksi kualitas udara.

## 1. Import dan Load Data
Kode memuat data hasil *merge* versi 3 (`merged_pm25_era5v3.csv`) yang telah dipastikan berwujud *time-series* kontinu sebanyak 9.480 baris (Nov 2022 - Nov 2023). 

## 2. Imputasi Nilai Kosong (Handling Missing Values)
* **Konsep:** Model LSTM tidak dapat dilatih jika ada satu sel pun yang bernilai `NaN` (Not a Number).
* **Kode:** `df['pm25'].interpolate(method='time')`
* **Penjelasan Matematis:** Metode ini melarang keras penggunaan `Mean` (rata-rata) untuk mengisi kekosongan, karena akan menghancurkan pola alami siang-malam PM2.5. Interpolasi akan menarik "garis lurus" yang masuk akal antara data terakhir sebelum sensor mati, dengan data pertama saat sensor hidup kembali.

## 3. Feature Engineering (Ekstraksi Fitur)
Ini adalah langkah paling krusial untuk meningkatkan tingkat akurasi (RMSE) secara drastis.

### A. Fitur Temporal Ekstrak
Kode mengekstrak angka `hour` (0-23), `day_of_week` (0-6), dan `month` (1-12) dari struktur *Datetime*. Kemudian, kode membuat fitur penanda biner `is_dry_season` (1 jika Juni-September, 0 jika lainnya).

### B. Cyclical Encoding (Transformasi Sinus/Cosinus)
* **Masalah:** Algoritma menganggap perbedaan jarak matematis antara jam 23 dan jam 0 adalah 23. Padahal, jarak waktunya hanya 1 jam.
* **Kode:** Menggunakan rumus Trigonometri Numpy (`np.sin` dan `np.cos`).
* **Hasil:** Waktu dibengkokkan menjadi bentuk lingkaran. Jam diproyeksikan ke sumbu X dan Y pada grafik kartesius, sehingga LSTM akan paham bahwa jam 23 dan jam 0 letaknya berdekatan.

### C. Lagged Features (Fitur Historis)
* **Konsep:** Menurut penelitian, faktor yang paling kuat memprediksi polusi jam ini adalah tingkat polusi satu jam yang lalu.
* **Kode:**
  * `df['pm25'].shift(1)` → Membuat variabel Lag T-1 (satu jam yang lalu).
  * `df['pm25'].shift(24)` → Membuat variabel Lag T-24 (jam yang sama, sehari yang lalu).
* Karena proses *shift* (geser turun) ini akan menyisakan 24 baris teratas dengan status kosong (karena tidak ada sejarah sebelumnya), kode menggunakan `dropna()` untuk membuang 24 jam pertama.

## 4. Chronological Train-Test Split (Pembagian Data)
* **Konsep Time-Series:** Kita **DILARANG KERAS** membagi data train dan test secara acak (*random_state*). Menguji masa lalu menggunakan pola dari masa depan adalah kecurangan akademis (*Data Leakage*).
* **Kode:** Membagi data 80% pertama berdasarkan baris waktu (`iloc[:train_size]`) sebagai data Latih (Training) dan 20% terakhir sebagai data Uji (Testing).

## 5. Scaling (Normalisasi MinMaxScaler)
* **Konsep Deep Learning:** Sel memori LSTM diatur oleh *gate* yang menggunakan fungsi aktivasi *Sigmoid* (skala 0 ke 1) dan *Tanh* (skala -1 ke 1). Jika ada fitur bernilai 900 (tekanan udara), *gate* LSTM akan jenuh (*saturated*) dan model akan berhenti belajar (*Vanishing Gradient*).
* **Kode:** Menggunakan `MinMaxScaler(feature_range=(0,1))` dari Scikit-Learn.
* **Aturan Penting:**
  1. `fit_transform` HANYA boleh dikenakan pada data *Training* (Model belajar mendeteksi nilai Min dan Max).
  2. Data *Testing* HANYA boleh dikenakan `transform` (Data diubah berdasarkan memori batas Min/Max dari data *Training* tadi). Hal ini mencegah model "mengintip" data masa depan.
* **Penyimpanan Scaler:** Model scaler *Target* (`scaler_y`) wajib disimpan dengan ekstensi `.pkl`. Nanti saat evaluasi akhir, prediksi LSTM yang keluar masih dalam wujud pecahan 0 sampai 1. Kita butuh `scaler_y` untuk membaliknya (Inversi) menjadi ukuran mikrogram per meter kubik (ug/m3) asli menggunakan `inverse_transform()`.

## 6. Penyimpanan File Akhir
Data yang telah tersusun rapi diekspor menjadi dua file (`train_scaled.csv` dan `test_scaled.csv`) dan siap dimasukkan ke dalam arsitektur PyTorch/Keras/XGBoost.
