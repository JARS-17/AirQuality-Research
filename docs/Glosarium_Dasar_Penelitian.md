# Glosarium dan Konsep Dasar Penelitian
*Dokumen ini disusun khusus agar Anda dapat menguasai istilah-istilah dasar (fundamental) dari nol hingga mahir terkait penelitian AI dan Kualitas Udara.*

---

## 🌍 BAGIAN 1: LINGKUNGAN & KUALITAS UDARA

### 1. PM2.5 (Particulate Matter 2.5)
Debu atau partikel melayang di udara yang ukurannya sangat kecil, yaitu kurang dari 2,5 mikrometer (sekitar 30x lebih kecil dari diameter rambut manusia). 
*   **Kenapa bahaya?** Ukurannya yang super kecil membuatnya bisa menembus masker biasa, masuk jauh ke dalam paru-paru, dan bahkan menyusup ke aliran darah.
*   **Sumbernya:** Asap knalpot kendaraan, asap pabrik, pembakaran sampah, dan kebakaran hutan.

### 2. AQI / ISPU (Air Quality Index / Indeks Standar Pencemar Udara)
Angka standar yang digunakan oleh pemerintah seluruh dunia untuk melaporkan seberapa kotor udara saat ini. Biasanya dinilai dengan warna: Hijau (Baik), Kuning (Sedang), Merah (Tidak Sehat), Ungu/Hitam (Berbahaya).

### 3. Inversi Suhu (*Temperature Inversion*)
Normalnya, semakin tinggi kita naik ke gunung, udara semakin dingin (udara panas dari kota akan terbang naik ke atas membawa polusi). **Inversi Suhu** adalah kejadian terbalik: lapisan udara dingin justru berada di bawah dan terjebak oleh lapisan udara hangat di atasnya (seperti tutup panci). Akibatnya, polusi knalpot dari kota tidak bisa terbang ke atas dan menumpuk di permukaan tanah.

### 4. Topografi Cekungan (*Basin Topography*)
Bentuk daratan yang menyerupai mangkuk, dikelilingi oleh pegunungan di sisi-sisinya. **Bandung** adalah contoh sempurna. Bentuk mangkuk ini membuat angin sulit bertiup kencang untuk menyapu polusi, membuat Bandung sangat rentan terhadap *Inversi Suhu*.

### 5. Parameter Meteorologi (ERA5)
Faktor-faktor cuaca yang sangat mempengaruhi pergerakan polusi:
*   **Suhu (Temperature):** Udara panas membuat partikel lebih mudah menyebar.
*   **Kelembapan Relatif (Relative Humidity / RH):** Banyaknya uap air di udara. Kelembapan tinggi bisa membuat partikel debu menyerap air, menggumpal, dan turun ke tanah.
*   **Kecepatan Angin (Wind Speed):** Penyapu alami polusi. Angin kencang = polusi bersih.
*   **ERA5:** Ini adalah nama *database* cuaca raksasa global buatan Eropa. Peneliti sering men-download data cuaca historis dari sini jika stasiun BMKG lokal tidak lengkap.

---

## 🤖 BAGIAN 2: KECERDASAN BUATAN (AI) & MACHINE LEARNING

### 6. Machine Learning (ML)
Cabang dari AI di mana kita TIDAK memprogram aturan secara manual (misal: *if suhu dingin then polusi tinggi*). Sebaliknya, kita memberikan **ribuan data historis** ke komputer, dan membiarkan komputer belajar sendiri menemukan pola rahasia di dalam data tersebut.

### 7. Deep Learning (DL)
Versi *Machine Learning* yang lebih canggih dan dalam, terinspirasi dari struktur jaringan saraf otak manusia (*Neural Networks*). Sangat hebat untuk memecahkan pola data yang sangat rumit, tapi kelemahannya ia sangat *Black-Box*.

### 8. Model *Black-Box* (Kotak Hitam)
Istilah sindiran untuk algoritma AI yang sangat akurat dalam menebak jawaban, TAPI tidak bisa menjelaskan logikanya. AI hanya menerima *Input*, melakukan proses misterius di dalam kotak hitam, lalu mengeluarkan *Output*.

### 9. Algoritma LSTM (*Long Short-Term Memory*)
Algoritma AI (berbasis *Deep Learning*) yang sangat jenius dalam "mengingat masa lalu". Sangat cocok untuk data rentang waktu (*time-series*) seperti cuaca dan saham, karena ia ingat bahwa polusi hari ini sangat dipengaruhi oleh polusi kemarin dan dua hari yang lalu.

### 10. Algoritma XGBoost (*Extreme Gradient Boosting*)
Salah satu algoritma *Machine Learning* paling juara (sering memenangkan kompetisi dunia). Bekerja dengan cara membuat ratusan "Pohon Keputusan" (*Decision Trees*) kecil-kecilan, lalu menggabungkan semuanya untuk membuat tebakan yang super akurat dan sangat cepat.

---

## 💡 BAGIAN 3: EXPLAINABLE AI (XAI)

### 11. XAI (*Explainable Artificial Intelligence*)
Teknologi "pembuka kotak hitam". Ini adalah sekumpulan alat bantu yang dipasang ke tubuh AI agar AI tersebut bisa ngobrol dan menjelaskan alasannya mengambil sebuah keputusan kepada manusia.

### 12. SHAP (*SHapley Additive exPlanations*)
Metode XAI yang paling populer dan diakui dunia akademis saat ini. Diambil dari teori permainan ekonomi (*Game Theory*). 
*   **Cara kerjanya:** SHAP menghitung dengan adil seberapa besar *saham* atau *kontribusi* setiap variabel (misal: suhu 30%, angin 50%, macet 20%) dalam menghasilkan prediksi polusi hari ini.

### 13. Feature Importance (Pentingnya Fitur)
Grafik batang sederhana yang dihasilkan oleh AI untuk memberi tahu kita urutan juara: variabel apa yang paling berpengaruh terhadap polusi? (Misal: 1. Kecepatan Angin, 2. Suhu, 3. Kelembapan).

---

## 📊 BAGIAN 4: METRIK EVALUASI (CARA MENILAI RAPOR AI)

*Saat AI sudah selesai belajar, kita harus mengujinya/memberinya ujian. Ini adalah nilai rapornya:*

### 14. RMSE (*Root Mean Square Error*)
Rata-rata kesalahan tebakan AI dalam satuan aslinya. 
*   *Contoh:* Jika nilai aktual PM2.5 adalah 50, dan AI menebak 55. Berarti ia salah 5 poin. Semakin **KECIL** RMSE, semakin **PINTAR** AI tersebut.

### 15. MAPE (*Mean Absolute Percentage Error*)
Mirip RMSE, tapi ini dalam bentuk persentase (%).
*   *Contoh:* MAPE 5% berarti tebakan AI rata-rata hanya meleset 5% dari kenyataan. Jika MAPE di bawah 10%, AI dianggap sangat akurat.

### 16. R² (R-Squared / Koefisien Determinasi)
Skala nilai dari 0 sampai 1 (atau 0% sampai 100%) yang menunjukkan seberapa jago AI menangkap variasi/pola data.
*   *Contoh:* R² = 0.85 artinya AI Anda bisa menjelaskan 85% kejadian di dunia nyata dengan benar. Semakin mendekati angka **1**, semakin **SEMPURNA**.

### 17. Overfitting (Terlalu Menghafal)
Penyakit AI paling umum. AI terlalu jenius saat ujian latihan (karena dia menghafal kunci jawaban/data training), tapi saat diberi soal ujian sungguhan (data baru di dunia nyata), nilainya hancur lebur.

### 18. Underfitting (Kurang Belajar)
Kebalikan *overfitting*. AI terlalu bodoh atau datanya kurang banyak, sehingga di ujian latihan pun nilainya sudah jelek.
