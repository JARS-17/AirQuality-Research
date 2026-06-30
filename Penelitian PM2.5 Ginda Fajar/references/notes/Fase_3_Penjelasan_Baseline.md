# Penjelasan Kode: Fase 3 (Pemodelan Baseline XGBoost & Random Forest)

Dokumen ini berisi penjelasan detail baris per baris mengenai alur kerja dan logika kode di dalam Jupyter Notebook `03_Baseline_Models.ipynb`. 

Tujuan fase ini adalah membangun metrik dasar (pijakan) menggunakan algoritma *Machine Learning* klasik yang sangat kuat (Ensemble Trees). Performa model di fase ini akan dijadikan ajang pembuktian bahwa model Deep Learning (LSTM) di Fase 4 nanti bisa mengalahkan performa algoritma klasik ini.

## 1. Load Data Processed & Scaler
* **Konsep:** Data yang dibaca adalah data *train* dan *test* berskala (0 hingga 1) hasil ekspor dari Fase 2.
* **Kode:** 
  ```python
  train_scaled = pd.read_csv('train_scaled.csv')
  scaler_y = joblib.load('scaler_y.pkl')
  ```
* **Penjelasan:** Target pemodelan kita adalah variabel `pm25` (sumbu y), dan sisanya (cuaca, waktu, lag) adalah fitur input (sumbu X). Kita sangat membutuhkan `scaler_y` di dalam memori (*load*) untuk nanti mengonversi hasil tebakan prediksi AI dari format (0.01 - 0.99) kembali menjadi angka konsentrasi asli (misal: 45 $\mu g/m^3$).

## 2. Inversi Prediksi & Metrik Evaluasi
* **Konsep:** Prediksi AI tidak bisa langsung diuji akurasinya. Jika AI memprediksi "0.4", dan nilai aslinya "0.5", *error*-nya "0.1". Angka ini tidak bermakna secara fisis bagi ilmuwan atmosfer.
* **Kode:** `scaler_y.inverse_transform(y_pred_scaled)`
* **Penjelasan Matematis:** Ini membalikkan rumus *MinMaxScaler* agar angka 0.4 tadi berubah menjadi misal $35 \mu g/m^3$.
* Setelah kembali ke satuan aslinya, kita menghitung 3 metrik akademis wajib:
  1. **RMSE (Root Mean Squared Error):** Semakin besar kesalahan tebakan AI, penalti matematisnya semakin tinggi (karena dikuadratkan). Metrik utama standar Scopus.
  2. **MAE (Mean Absolute Error):** Kesalahan tebakan rata-rata (jika aktual 50 dan prediksi 45, MAE = 5).
  3. **R-Squared ($R^2$):** Skala kecocokan pola dari 0.0 sampai 1.0 (semakin mendekati 1.0 semakin sempurna prediksinya).

## 3. Melatih Random Forest (RF)
* **Konsep:** Model ini menumbuhkan 100 pohon keputusan (*decision trees*) yang saling berdiskusi untuk menebak angka PM2.5.
* **Kode:** `RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)`
* **Penjelasan Parameter:**
  * `n_estimators=100`: Jumlah pohon (100 sudah cukup untuk menstabilkan prediksi).
  * `n_jobs=-1`: Memerintahkan laptop Anda untuk menggunakan seluruh *core* prosesor yang tersedia agar proses *training* berlangsung sangat cepat (paralel).

## 4. Melatih XGBoost
* **Konsep:** Singkatan dari *Extreme Gradient Boosting*. Mirip dengan RF, tapi alih-alih pohon berdiskusi bersama, XGBoost menumbuhkan pohon secara berurutan. Pohon ke-2 akan fokus memperbaiki kebodohan (error) dari Pohon ke-1.
* **Kode:** `xgb.XGBRegressor(learning_rate=0.1, max_depth=6)`
* **Penjelasan Parameter:**
  * `learning_rate=0.1`: Seberapa cepat model belajar. Jika terlalu cepat (1.0) model akan "nabrak" pola halus. Jika terlalu lambat (0.01) *training* akan lama.
  * `max_depth=6`: Tingkat kedalaman pohon. Angka 6 membatasi agar pohon tidak terlalu rumit (mencegah *Overfitting* / menghafal data *training*).

## 5. Visualisasi Hasil (Time-Series)
* **Konsep:** Model prediksi *Time-Series* tidak cukup dievaluasi dengan angka tunggal (RMSE/R2). Kita harus **melihat** apakah grafik tebakan model (*predicted*) sejalan dengan lekukan grafik aslinya (*actual*).
* **Kode:** Membuat plot data *Aktual* (hitam solid), *Random Forest* (biru putus-putus), dan *XGBoost* (merah). Hanya divisualisasikan 14 hari pertama agar garisnya jelas tidak bertumpuk-tumpuk.

## 6. Menyimpan Model (*Save Model*)
* **Konsep:** Setelah laptop Anda bekerja keras menemukan pola matematis di dalam XGBoost, pola "otak" itu harus disimpan.
* **Kode:** `xgb_model.save_model('xgb_baseline.json')`
* **Alasan:** Pada Fase 5 nanti, kita akan melakukan analisis Interpretasi SHAP (menjelaskan mengapa XGBoost memprediksi angka tertentu). Untuk menghemat waktu, di Fase 5 kita tinggal memanggil (`load`) file `.json` ini tanpa harus melatih modelnya dari awal lagi.
