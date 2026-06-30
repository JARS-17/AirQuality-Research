# Penjelasan Kode: Fase 1 (Exploratory Data Analysis - EDA)

Dokumen ini berisi penjelasan detail baris per baris mengenai alur kerja dan logika kode di dalam Jupyter Notebook `01_EDA_PM25_ERA5.ipynb`.

## 1. Import dan Load Data
Kode dimulai dengan mengimpor library standar (`pandas`, `matplotlib`, `numpy`).
* **Data ERA5 (Satelit):** Dimuat dari `era5_bandung_2022_2026.csv`. Waktu diatur sebagai *index* agar memudahkan pemrosesan time-series. Kolom `number` dihapus karena nilainya konstan 0.
* **Data PM2.5 (Sensor):** Dimuat dari `hourly_all_sensors.csv`. Waktu diubah (*convert*) ke zona waktu WIB (`Asia/Jakarta`) agar sinkron dengan jam lokal saat menganalisis pola diurnal.

## 2. Pemilihan Sensor Utama
Terdapat dua sensor di wilayah Bandung (ID: `121867` dan `238875`).
* Kode memisahkan data menjadi dua *dataframe* berdasarkan `sensor_id`.
* **Keputusan:** Sensor `121867` dipilih karena memiliki data yang jauh lebih lengkap (~16.500 baris) dibandingkan sensor kedua yang baru aktif di tahun 2025.

## 3. Deteksi Outlier (IQR Method)
Setelah sensor utama dipilih, kode membersihkan data dari pencilan (*outliers*) ekstrem.
* Digunakan metode **Interquartile Range (IQR)**. 
* Batas atas (*upper bound*) dihitung. Nilai PM2.5 yang melewati batas ini (misalnya karena sensor *glitch* atau error pembacaan yang tidak wajar) dihapus dari dataset (`pm25_clean`) agar tidak merusak korelasi matematis.

## 4. Visualisasi Time-Series dan Distribusi (ERA5)
* **Histogram:** Digunakan untuk melihat bentuk distribusi 11 variabel cuaca (seperti suhu, arah angin, tekanan). 
* **Time-Series Plot:** Dibuat untuk 6 variabel kunci dengan menandai area musim kemarau (Juni-September) menggunakan blok warna kuning. Hal ini membuktikan bahwa cuaca di Bandung bersifat musiman/siklik.

## 5. Pola Diurnal dan Musiman (PM2.5)
* **Pola Diurnal (Per Jam):** Data dikelompokkan berdasarkan kolom `hour` (`groupby('hour')`). Ditemukan bahwa PM2.5 memuncak di pagi hari (06:00-08:00) dan malam hari (18:00-23:00) yang bertepatan dengan jam sibuk lalu lintas.
* **Pola Musiman (Per Bulan):** Data dikelompokkan berdasarkan kolom `month`. Kode membuktikan konsentrasi PM2.5 rata-rata jauh lebih tinggi di bulan-bulan kemarau (Juni-September) dibandingkan bulan hujan.

## 6. PENGGABUNGAN DATA (MERGE) — *Revisi Penting*
Bagian ini mengalami perbaikan kritis untuk menyesuaikan dengan kebutuhan model *Long Short-Term Memory* (LSTM).

**Masalah Awal:**
Jika kita menggunakan metode `how='inner'` biasa saat *join*, pandas akan membuang baris waktu di mana sensor PM2.5 mati. Akibatnya, waktu "melompat" dan merusak kontinuitas time-series.

**Kode yang Diperbaiki:**
```python
# MENGGUNAKAN 'how=right' AGAR WAKTU KONTINU
merged = pm25_clean[['pm25']].join(era5, how='right')
merged = merged.sort_index().loc['2022-11-01':'2023-11-30']
```
**Penjelasan Logika Revisi:**
1. **`how='right'`**: Karena data `era5` ada di posisi kanan (`.join(era5)`), parameter ini memaksa hasil *merge* untuk mempertahankan 100% *timeline* milik ERA5. Karena ERA5 tidak memiliki data kosong dari jam ke jam, *timeline* hasil gabungannya dipastikan **Sempurna dan Kontinu**.
2. Jika ada jam di mana sensor PM2.5 mati, Pandas akan mengisinya dengan nilai `NaN` (Kosong). 
3. **`.loc['2022-11-01':'2023-11-30']`**: Memotong data tepat menjadi periode 12 bulan yang berkesinambungan tanpa gap raksasa. Menghasilkan total tepat **9.480 baris** (jumlah jam selama 1 tahun plus 1 bulan).

## 7. Analisis Korelasi Pearson
Menggunakan `merged.corr()`, kode mengukur kekuatan hubungan antara cuaca dan PM2.5. Pandas secara otomatis mengabaikan nilai `NaN` saat menghitung korelasi, sehingga hasilnya akurat. Variabel dengan korelasi terkuat divisualisasikan dalam bentuk *Heatmap*.
