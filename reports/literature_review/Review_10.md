# Review Jurnal 10
**"Statistical and Machine Learning Models for Air Quality: A Systematic Review of Methods and Challenges"**
*Ballesteros Peinado, Guarda, Herrera-Vidal, Minnaard & Coronado-Hernández — Algorithms, 2025*

---

### ✅ Kekuatan

**Cakupan Corpus yang Sangat Luas**
Menganalisis 412 artikel peer-reviewed dari 2016–2025 menggunakan protokol PRISMA 2020 adalah skala yang substansial. Proses filtering berlapis (dari 258.035 dokumen awal hingga 412 artikel final) didokumentasikan secara transparan dengan flowchart yang jelas, memenuhi standar reprodusibilitas systematic review modern.

**Pendekatan Bibliometrik yang Inovatif**
Penggunaan analisis "science tree" dengan tiga level hierarki (Roots/Classics, Trunk/Structural, Leaves/Perspectives) dan visualisasi jaringan co-citation menggunakan Gephi adalah pendekatan yang memberikan perspektif epistemologis yang lebih kaya dibanding systematic review konvensional. Ini membantu pembaca memahami evolusi dan kematangan bidang ini secara lebih intuitif.

**Identifikasi Kesenjangan Geografis yang Penting**
Temuan bahwa 73.2% studi terkonsentrasi di Asia sementara Amerika Latin hanya 1.03% dan Afrika 5.15% adalah kontribusi yang sangat berharga untuk agenda penelitian global. Kesenjangan ini memiliki implikasi nyata karena kedua wilayah tersebut justru menghadapi tantangan kualitas udara yang serius namun kekurangan model prediktif yang kontekstual.

**Sistematisasi Variabel dan Metrik yang Komprehensif**
Mengidentifikasi 1.177 variabel prediktor dan 307 metrik evaluasi dari seluruh korpus memberikan peta yang sangat berguna tentang praktik komunitas peneliti. Temuan bahwa CO adalah variabel terbanyak digunakan (35%) dan RMSE/MSE mendominasi metrik evaluasi membuka diskusi penting tentang standardisasi metodologi.

**Tiga Research Questions yang Terstruktur dengan Baik**
Pembagian menjadi RQ1 (faktor yang memengaruhi kualitas udara), RQ2 (perbandingan ML vs statistik), dan RQ3 (tantangan implementasi) memberikan kerangka analisis yang koheren. Framework perbandingan model di Tabel 2 (Challenges vs Opportunities) juga menjadi referensi yang actionable bagi peneliti berikutnya.

---

### ⚠️ Kelemahan & Catatan Kritis

**Dominasi Akurasi atas Interpretabilitas dalam Analisis**
Paper ini mengidentifikasi bahwa 70.8% studi hanya fokus pada akurasi sementara interpretabilitas hanya 20.8% — namun ironisnya, paper ini sendiri tidak sepenuhnya melampaui masalah tersebut. Analisis perbandingan performa model (Bagian 3.4) hanya berdasarkan 24 studi yang eksplisit membandingkan keduanya, sehingga representativitasnya terbatas.

**Definisi "Hybrid Model" yang Tidak Konsisten**
Paper mengkategorikan CNN-LSTM sebagai "hybrid or advanced model" terpisah dari kategori ML, namun dalam literatur yang dianalisis CNN-LSTM juga muncul di kategori ML (8 entri di Figure 5 dan 7 entri di Figure 6). Tumpang tindih kategorisasi ini mengurangi kejelasan taksonomi model yang disajikan.

**Analisis Kuantitatif Perbandingan ML vs Statistik yang Dangkal**
Meskipun RQ2 bertanya tentang perbandingan akurasi ML dan model statistik, paper hanya mampu menganalisis 24 studi yang secara eksplisit membandingkan keduanya (hanya ~5.8% dari 412 artikel). Tidak ada meta-analisis kuantitatif seperti effect size atau pooled performance metrics. Kesimpulan bahwa "ML outperforms statistical models" menjadi generalisasi yang kurang dapat diverifikasi secara ketat.

**Tidak Ada Analisis Temporal Tren Performa Model**
Meskipun paper mencatat pertumbuhan publikasi dari 2 artikel (2016) hingga 106 artikel (2024), tidak ada analisis apakah akurasi model juga membaik secara konsisten seiring waktu. Pertanyaan "apakah semakin baru semakin akurat?" tidak dijawab, padahal ini sangat relevan untuk memposisikan arah penelitian.

**Batasan Lingkup yang Tidak Disebutkan di Awal**
Paper mengecualikan studi dari konteks pertambangan terbuka (open-cast mining) dengan alasan fokus pada lingkungan ambient. Namun, pengecualian ini baru disebutkan di bagian Quality Assessment (Seksi 2.4), bukan di bagian Introduction atau Methodology awal. Ini bisa menyesatkan pembaca yang tidak membaca paper secara menyeluruh.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Kontribusi untuk Agenda Riset | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Minor Revision / Accept** — Paper ini adalah kontribusi bernilai tinggi sebagai referensi landasan (*landmark reference*) bagi peneliti di bidang prediksi kualitas udara. Kelemahannya terletak pada analisis komparatif yang kurang mendalam secara kuantitatif. Penambahan meta-analisis performa dan klarifikasi kategorisasi model akan meningkatkan kekuatan kontribusinya secara signifikan.