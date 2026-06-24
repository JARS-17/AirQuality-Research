# Penjelasan Kode: Fase 4 (Pemodelan Deep Learning LSTM)

Dokumen ini adalah ringkasan metodologis mengenai arsitektur LSTM (*Long Short-Term Memory*) yang kita kembangkan menggunakan *framework* Keras/TensorFlow. Penjelasan ini dirancang untuk membantu Anda menjawab pertanyaan dosen saat sidang.

## 1. Transformasi Data (2D ke 3D Sliding Window)
* **Masalah:** Model klasik seperti XGBoost menerima data berbentuk tabel 2D biasa (Baris x Kolom). Namun, LSTM membutuhkan data yang memiliki dimensi "Sejarah Waktu".
* **Solusi Kode:** Kita membuat fungsi `create_sequences(df, time_steps=24)`.
* **Penjelasan Matematis:** Jika kita memiliki 15 fitur (Suhu, Arah Angin, dll), fungsi ini akan memotong data menjadi "balok-balok" 3D berukuran `[24, 15]`. Artinya, untuk menebak PM2.5 di masa depan, LSTM diberi memori mundur ke belakang sebanyak 24 jam dengan 15 fitur pendukung. Format 3D ini sangat wajib di Keras (`[samples, timesteps, features]`).

## 2. Arsitektur Jaringan Saraf Tiruan (Deep Learning)
Jaringan yang kita bangun berbentuk **Sequential** (Lurus berlapis-lapis):

1. **Layer LSTM Pertama (64 Unit/Neuron):**
   * Berfungsi sebagai mata pertama yang melihat seluruh urutan waktu 24 jam.
   * Parameter `return_sequences=True` memaksa layer ini untuk tidak langsung menyimpulkan, melainkan meneruskan seluruh memori 24 jam tersebut ke layer berikutnya.
2. **Layer Dropout (0.2):**
   * Ini adalah teknik regulerisasi yang krusial. 
   * **Analogi:** Jika seorang murid belajar dengan membaca buku yang sama terus-menerus, dia akan menghafal letak jawaban, bukan memahami konsepnya (*Overfitting*). Dropout "memaksa tutup mata" 20% neuron secara acak setiap detiknya, memaksa neuron lain untuk belajar mengenali pola PM2.5 secara mandiri.
3. **Layer LSTM Kedua (32 Unit/Neuron):**
   * Bertugas mengambil kesimpulan (*bottleneck*) dari layer pertama.
   * `return_sequences=False` karena layer ini adalah ujung dari proses membaca waktu. Ia hanya akan mengeluarkan satu vektor intisari dari 24 jam tersebut.
4. **Dense Layer (1 Unit):**
   * Layer Output (Keluaran). Hanya memiliki 1 saraf karena tugas kita adalah Regresi (menebak 1 angka desimal konsentrasi PM2.5, bukan menebak kelas klasifikasi).

## 3. Kompilasi & Pengaman Training
* **Optimizer `Adam`:** Varian algoritma *Stochastic Gradient Descent* (SGD) yang bisa menyesuaikan kecepatan belajarnya (*learning rate*) sendiri. Sangat stabil.
* **Loss `Mean Squared Error` (MSE):** Saat LSTM salah menebak, tingkat kesalahannya dikuadratkan agar model "kapok" dan belajar lebih agresif menghindari *error* besar.
* **Early Stopping (`patience=10`):** Jika kita memaksa LSTM belajar 50 putaran (*epochs*), belum tentu di putaran ke-50 dia jadi tambah pintar. Terkadang di putaran ke-20 dia sudah kelelahan (akurasi malah turun). *Early Stopping* akan mendeteksi ini dan otomatis menghentikan *training* jika dalam 10 putaran terakhir akurasinya tidak membaik sama sekali. Ini menghemat jam kerja komputer Anda.

## 4. Inversi Skala & Evaluasi
* Sama seperti di Fase 3, nilai tebakan LSTM adalah pecahan (misal: 0.15).
* Kita memanggil `scaler_y.inverse_transform` untuk membesarkannya kembali menjadi, misal, $25 \mu g/m^3$.
* Baru setelah itu diukur RMSE, MAE, dan $R^2$-nya untuk dibandingkan dengan skor Random Forest secara *fair* (adil).

## 5. Ekspor Model `.keras`
* Model LSTM beserta seluruh miliaran bobot sarafnya yang sudah lulus *training* disimpan dalam format terbaru TensorFlow: `.keras`.
* Dengan file ini, kita tidak perlu membuang waktu mengulang *training* jika besok ingin memprediksi data cuaca baru, atau (seperti yang akan kita lakukan di Fase 5) membongkar isi otak modelnya menggunakan SHAP.
