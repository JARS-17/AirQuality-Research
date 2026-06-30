# Prediksi PM2.5 di Cekungan Bandung Menggunakan Deep Learning LSTM

Yth. Bapak Rumadi,S.T.,M.T

Bersama folder ini, saya melampirkan seluruh kode (*source code*) dan dataset dari penelitian Kerja Praktik saya terkait pemodelan PM2.5 di kawasan Cekungan Bandung. 

Untuk memudahkan proses *review* dan evaluasi, semua tahapan terpisah (mulai dari *Exploratory Data Analysis*, *Preprocessing*, pelatihan model Baseline dan LSTM, hingga interpretasi metrik SHAP) telah saya satukan ke dalam satu file Jupyter Notebook tunggal.

## Panduan Menjalankan Kode secara Lokal

Apabila Bapak ingin menjalankan atau memverifikasi kode ini secara langsung melalui VSCode atau Jupyter Notebook di komputer lokal, Bapak/Ibu dapat mengikuti langkah-langkah berikut:

**1. Persiapan Dataset**
Pastikan file dataset mentah (`merged_pm25_era5v3.csv`) sudah diletakkan di dalam direktori `data/raw/`.

**2. Instalasi Pustaka (Library)**
Buka terminal/CMD di lokasi folder utama ini, lalu jalankan perintah berikut untuk memastikan semua *library* Python yang dibutuhkan sudah terinstal:
```bash
pip install -r requirements.txt
```

**3. Eksekusi Notebook**
- Silakan buka file `PM25_Prediction_Bandung.ipynb` yang ada di dalam folder `notebooks/`.
- Kode ini sudah dimodifikasi dari versi awalnya (yang berbasis Google Colab) menjadi versi lokal. Seluruh pembacaan data kini menggunakan *relative path*, sehingga Bapak/Ibu tidak perlu mengubah baris kode apa pun.
- Bapak/Ibu cukup menekan tombol **Run All** atau mengeksekusi *cell* secara berurutan dari atas ke bawah. Model Deep Learning akan dilatih secara otomatis dan grafiknya akan langsung muncul.

## Penjelasan Struktur Folder
*   **`data/`** : Direktori untuk dataset mentah (`raw`) dan hasil ekstraksi fitur (`processed`).
*   **`notebooks/`** : Berisi *script* utama berformat `.ipynb`.
*   **`models/`** : Folder tujuan tempat model terbaik (berformat `.keras` dan `.pkl`) akan disimpan secara otomatis setelah kode selesai dieksekusi.

Terima kasih banyak atas waktu, arahan, dan bimbingan yang Bapak berikan selama pelaksanaan Kerja Praktik ini.

Hormat saya,


**Ginda Fajar Riadi Marpaung**
