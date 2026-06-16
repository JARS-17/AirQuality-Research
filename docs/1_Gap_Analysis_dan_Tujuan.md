# GAP ANALYSIS DAN TUJUAN PENELITIAN

Bagian ini dirumuskan berdasarkan tinjauan literatur sistematis terhadap 22 jurnal nasional dan internasional mengenai penerapan *Machine Learning* dan *Deep Learning* dalam memprediksi kualitas udara (PM2.5). Berdasarkan kajian tersebut, ditemukan tiga celah penelitian (*research gap*) utama yang menjadi landasan kuat urgensi penelitian ini:

## 1. Analisis Kesenjangan Penelitian (*Gap Analysis*)

### A. Kesenjangan Geografis dan Topografis (*Geographical Gap*)
Tinjauan literatur menunjukkan dominasi penelitian prediksi kualitas udara yang berpusat di wilayah subtropis (seperti Tiongkok dan Eropa) serta wilayah dataran rendah atau pesisir (seperti DKI Jakarta, Indonesia). Jurnal-jurnal referensi (seperti Jurnal 1, 2, 5, 17, 18) yang berlokasi di Indonesia hampir secara eksklusif memfokuskan pemodelan di Jakarta. 

Sangat minim penelitian yang memodelkan kualitas udara di wilayah beriklim hujan tropis dengan bentuk topografi cekungan (*basin*), seperti **Bandung**. Topografi mangkuk/cekungan secara fisik memicu fenomena inversi suhu dan secara drastis mengubah bagaimana parameter meteorologi (kecepatan angin dan kelembapan) berinteraksi dengan emisi antropogenik. Model AI yang berkinerja tinggi di daerah dataran terbuka sering kali gagal menangkap pola akumulasi polutan spesifik di wilayah cekungan, sehingga menciptakan celah kebutuhan yang mendesak akan model spesifik-lokasi.

### B. Kesenjangan Metodologis: Krisis *Black-Box* (*Methodological Gap*)
Perkembangan arsitektur kecerdasan buatan, khususnya *Machine Learning* tingkat lanjut (seperti XGBoost) dan *Deep Learning* (seperti LSTM), telah terbukti memberikan tingkat akurasi prediksi polutan yang sangat tinggi melebihi regresi statistik klasik (Ballesteros Peinado et al., 2025; Karmoude et al., 2025). 

Namun, studi-studi mutakhir menyoroti bahwa >70% dari pemodelan berkinerja tinggi tersebut memiliki kelemahan fatal berupa sifat *black-box* (kotak hitam). Algoritma tersebut tidak memiliki tingkat interpretabilitas untuk menjelaskan alasan fisika dan relasi fitur di balik tebakan akhirnya. Sementara untuk kepentingan pengambilan kebijakan lingkungan pemerintah, transparansi (*explainability*) sama pentingnya dengan akurasi. Pengadopsian metode **Explainable AI (XAI)**, khususnya metode *SHapley Additive exPlanations (SHAP)* untuk prediksi PM2.5 iklim tropis masih sangat jarang dieksplorasi secara mendalam.

### C. Kesenjangan Fusi Data (*Data Integration Gap*)
Mayoritas penelitian masa lalu cenderung menggunakan hanya satu jenis sumber data (data polutan univariat dari satu stasiun) yang berakibat pada kegagalan model menangkap anomali ekstrem (Safira et al., 2025). Mengatasi hal tersebut membutuhkan pendekatan fusi data, yaitu menggabungkan pengukuran polutan lokal dengan data meteorologi reanalisis satelit berskala makro (seperti data ERA5 dari ECMWF). Sinergi fusi data ini belum banyak dikawinkan dengan arsitektur hibrida XAI di ranah studi kualitas udara Indonesia.

---

## 2. Tujuan Penelitian (*Research Objectives*)

Berdasarkan ketiga kesenjangan penelitian di atas, maka penelitian ini ditetapkan dengan tiga tujuan utama:

1. **Membedah Pengaruh Cuaca pada Topografi Cekungan:**
   Menganalisis pengaruh spesifik dari parameter meteorologi (seperti suhu, kelembapan relatif, kecepatan angin, dan curah hujan dari dataset ERA5) terhadap fluktuasi konsentrasi PM2.5 di topografi cekungan tropis (Kota Bandung).
   
2. **Pengembangan Pemodelan Prediktif:**
   Mengembangkan dan membandingkan kinerja model prediktif berbasis *Machine Learning* (seperti *XGBoost* atau algoritma *tree-based* lainnya) dalam memprediksi tingkat PM2.5 historis yang terekam pada sensor kualitas udara (*low-cost sensor* / data stasiun pantau). Tujuan ini juga mengevaluasi performa akurasi model menggunakan metrik standar seperti RMSE, MAE, dan koefisien determinasi (R²).

3. **Penerapan Interpretabilitas Model (XAI):**
   Menerapkan dan memvalidasi metode *Explainable AI* (XAI) melalui pendekatan **SHAP (*SHapley Additive exPlanations*)** guna membuka sifat *black-box* model AI. Tujuan ini bermaksud untuk menghasilkan visualisasi *feature importance* dan *SHAP dependence plot* yang secara transparan dapat membuktikan kuantitas kontribusi masing-masing variabel cuaca terhadap perburukan indeks kualitas udara (PM2.5) secara harfiah.

---
*Dokumen ini siap disalin-tempel ke dalam Latar Belakang Proposal atau Bab 1 Tesis Anda.*
