# Penjelasan Lengkap Variabel (Fitur) Pemodelan PM2.5

Dokumen ini menjelaskan daftar variabel (fitur) yang digunakan sebagai *input* (prediktor) untuk melatih model Machine Learning dan Deep Learning (LSTM) dalam memprediksi konsentrasi PM2.5 di Cekungan Bandung.

Variabel-variabel ini terbagi menjadi tiga kategori utama: **Riwayat Polutan (Lag)**, **Parameter Meteorologi (ERA5)**, dan **Penanda Waktu (Temporal)**.

---

## 1. Kelompok Variabel Riwayat Polutan (*Lagged PM2.5*)

Polusi udara bersifat kumulatif. Konsentrasi PM2.5 pada jam ini sangat bergantung pada konsentrasi di jam-jam sebelumnya karena partikel tidak langsung hilang tertiup angin (terutama di daerah cekungan yang sirkulasi udaranya tertutup).

*   **`pm25` (dalam konteks 3D LSTM):** Karena LSTM membaca data secara sekuensial (*sliding window* 24 jam), model melihat rentetan nilai PM2.5 aktual dari 24 jam terakhir secara berurutan. Ini sering kali menjadi faktor prediktif paling dominan.
*   **`pm25_lag_1h` (Autokorelasi Jangka Pendek):** Nilai konsentrasi PM2.5 persis 1 jam yang lalu. Sangat krusial karena perubahan PM2.5 biasanya terjadi secara gradual, tidak melompat tiba-tiba. Jika 1 jam lalu polusinya buruk, kemungkinan besar jam ini masih buruk.
*   **`pm25_lag_24h` (Pola Diurnal / Harian):** Nilai konsentrasi PM2.5 persis di jam yang sama pada 1 hari (24 jam) sebelumnya. Ini menangkap rutinitas aktivitas manusia (antropogenik) seperti jam sibuk lalu lintas pagi atau aktivitas pabrik yang berulang setiap hari.

---

## 2. Kelompok Variabel Meteorologi (Data Reanalisis Copernicus ERA5)

Cuaca adalah faktor yang mengendalikan bagaimana emisi polusi menyebar atau justru terperangkap.

*   **`tinggi_lapisan_batas_m` (*Boundary Layer Height* - BLH):** 
    Ini adalah variabel cuaca paling kritis untuk PM2.5. BLH adalah ketinggian "atap" tak kasat mata (lapisan pencampuran atmosfer) di atas permukaan tanah. 
    *   **Hubungan:** Berbanding terbalik (Negatif). Ketika BLH rendah (biasanya malam hari atau suhu dingin), "atap" atmosfer turun. Polutan terjebak di volume udara yang sempit dekat permukaan, menyebabkan konsentrasi PM2.5 melonjak drastis (fenomena inversi).
*   **`suhu_2m_C` (*Temperature*):**
    Suhu udara pada ketinggian 2 meter. Suhu mempengaruhi pergerakan udara vertikal (konveksi). Udara panas akan naik membawa polutan ke atas atmosfer, sehingga suhu yang hangat biasanya membantu menurunkan PM2.5 di permukaan tanah.
*   **`kelembapan_persen` (*Relative Humidity*):**
    Kelembapan udara. Kelembapan tinggi memicu fenomena higroskopis, di mana partikel debu halus mengikat uap air, bertambah massanya, dan terakumulasi di udara. Namun jika terlalu tinggi hingga menjadi hujan, efeknya akan terbalik.
*   **`kecepatan_angin_kmh` (*Wind Speed*):**
    Berfungsi sebagai "kipas raksasa" yang meniup polutan. 
    *   **Hubungan:** Berbanding terbalik. Angin yang kencang akan mendispersi (menyebarkan) polusi ke wilayah lain sehingga angka PM2.5 turun. Angin lambat di kawasan topografi cekungan menyebabkan "stagnasi polusi".
*   **`arah_angin_derajat` (*Wind Direction*):**
    Menunjukkan dari mana polutan terbawa (misal: apakah angin membawa polusi dari kawasan industri di wilayah barat menuju stasiun sensor).
*   **`curah_hujan_mm` (*Total Precipitation*):**
    Hujan bertindak sebagai pencuci alami udara (*wash-out effect*). Rintik hujan akan menabrak partikel PM2.5 dan menjatuhkannya ke tanah, membersihkan udara secara signifikan.
*   **`tekanan_hPa` (*Surface Pressure*):**
    Tekanan udara tinggi (*High Pressure System*) cenderung membuat udara diam dan stabil, yang menjebak polutan. Sebaliknya, tekanan rendah memicu angin kencang dan cuaca bergolak yang membubarkan polutan.
*   **`tutupan_awan_01` (*Cloud Cover*):**
    Proporsi langit yang tertutup awan (0 = cerah, 1 = tertutup penuh awan). Berpengaruh pada radiasi matahari yang menembus tanah (berkaitan dengan suhu dan reaksi kimia fotokimia pembentuk partikel sekunder).

---

## 3. Kelompok Variabel Penanda Waktu (*Temporal Features*)

Model AI tidak mengerti arti "Jam 23:00" dan "Jam 00:00" secara kalender; secara matematis selisih angkanya adalah 23, padahal jarak waktunya hanya 1 jam. Oleh karena itu, kita memanipulasi waktu menjadi bentuk gelombang trigonometri (*Cyclical Encoding*).

*   **`hour_sin` dan `hour_cos`:** 
    Representasi gelombang sinus dan kosinus dari siklus 24 jam harian. Ini membantu model memahami bahwa siklus aktivitas harian itu berputar layaknya jam dinding (pukul 23 bersambung dengan pukul 00).
*   **`month_sin` dan `month_cos`:**
    Representasi siklus 12 bulan kalender. Membantu model mengidentifikasi transisi pergerakan bulan sepanjang tahun.
*   **`is_dry_season`:**
    Fitur penanda (biner). Bernilai **1** jika bulan berada di musim kemarau (Juni - September) dan **0** jika musim hujan. Fitur ini sengaja dibuat khusus (*domain knowledge*) karena kondisi cuaca di Indonesia didikte sangat kuat oleh fenomena dua musim ini, di mana PM2.5 terbukti jauh lebih pekat saat musim kemarau (debu kering & tidak ada efek *wash-out* curah hujan).
