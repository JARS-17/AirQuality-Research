# Penjelasan Kode: Fase 5 (Explainable AI / SHAP)

Dokumen ini menjelaskan alur logika di balik *notebook* `05_SHAP_Interpretation_LSTM.ipynb`. Di fase ini, kita membuka "Kotak Hitam" (Black Box) model Deep Learning kita dan mengungkap alasan rasional di balik setiap angkanya.

## 1. Tantangan Arsitektur 3D
* **Masalah:** Algoritma SHAP standar biasanya dirancang untuk data berbentuk tabel datar (2D). Namun, input model LSTM kita berbentuk "balok" 3D: `[Sampel, Waktu(24 Jam), Fitur(15)]`.
* **Solusi Kode:** Kita menggunakan `shap.GradientExplainer`. Ini adalah turunan SHAP khusus yang mendeteksi perubahan nilai pada tingkat *neuron* TensorFlow.

## 2. Pengambilan Sampel (Sampling)
* Menjalankan SHAP untuk membedah puluhan ribu data LSTM akan membuat RAM laptop kepenuhan (*Crash*). 
* Kita menggunakan pendekatan sampling akademik:
  1. **Background Sample:** Mengambil 100 baris acak dari data `Train`. Ini berfungsi sebagai titik nol (*baseline*). "Jika cuaca normal seperti 100 hari ini, PM2.5 harusnya sekian".
  2. **Test Sample:** Mengambil 200 baris acak dari data `Test`. Ini adalah "pasien" yang akan dibedah alasannya.

## 3. Meratakan Waktu (Flattening)
* Output dari `explainer.shap_values(test_sample)` adalah matriks 3D tebal. Ini berarti SHAP mengeluarkan penjelasan per-jam: "Di jam T-24 suhu mendorong polusi naik, tapi di jam T-10 angin mendorong polusi turun".
* Menjelaskan 24 variabel untuk setiap 15 fitur (Total 360 garis penjelasan) akan membuat grafik tak bisa dibaca.
* **Solusi Kode:** Kita menggunakan `np.mean(shap_values_3d, axis=1)`.
* **Makna:** Kita merata-ratakan impak setiap fitur selama 24 jam terakhir. Jadi kesimpulannya menjadi global: "Secara rata-rata dalam sehari terakhir, fitur Angin memiliki efek sekian".

## 4. Visualisasi (Summary Plot Beeswarm)
* **Cara Membaca Grafik Beeswarm SHAP:**
  * **Sumbu Y:** Daftar variabel cuaca/historis, disusun berdasarkan ranking kepentingannya. Variabel teratas adalah yang paling sering menjadi "Tersangka Utama" perubahan PM2.5.
  * **Sumbu X (SHAP Value):** Jika titik jatuh di sisi Kanan (positif), berarti faktor tersebut membuat polusi PM2.5 NAIK. Jika di Kiri (negatif), ia membuat polusi TURUN.
  * **Warna:** Merah berarti nilai aslinya Tinggi (Misal Kecepatan Angin sangat kencang). Biru berarti nilai aslinya Rendah.
  * **Contoh Bacaan:** Jika titik Kecepatan Angin berwarna MERAH dan berada di sebelah KIRI sumbu X, artinya: *"Saat angin kencang (Merah), konsentrasi polusi udara menurun (Kiri)"*. Ini sangat logis secara fisika atmosfer!

## 5. Visualisasi (Dependence Plot)
* Digunakan untuk membuktikan adanya hubungan *Non-Linear*.
* Misalnya pada Suhu (`suhu_2m_C`): Apakah semakin panas selalu semakin kotor udaranya? Terkadang suhu tinggi memecah polusi (lapisan batas naik), namun terkadang memicu fotokimia ozon yang memperparah polusi sekunder.
* Grafik ini membuktikan bahwa Jaringan Saraf LSTM berhasil menangkap kerumitan fisika tersebut melampaui regresi linear konvensional.
