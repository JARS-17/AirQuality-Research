# Review Jurnal 04
**"Assessing Low-Cost Sensor for Characterizing Temporal Variation of PM2.5 in Bandung, Indonesia"**
*Kurniawati et al. — Kuwait Journal of Science, 2025*

---

### ✅ Kekuatan

**Relevansi Lokal yang Tinggi**
Penelitian ini mengisi celah yang nyata — evaluasi sensor **PurpleAir PA-II** untuk konteks Indonesia, khususnya Bandung, masih sangat terbatas. Data jangka panjang selama 12 bulan (Juni 2022–Mei 2023) memberikan cakupan yang mencakup satu siklus musim penuh (kemarau dan hujan), yang sangat berharga.

**Desain Co-Location yang Solid**
Penggunaan **SuperSASS** sebagai referensi yang memenuhi standar EPA FRM adalah pilihan yang tepat dan kredibel. Jarak co-location ±25 m dan prosedur QC yang terstruktur (threshold ±10 μg/m³ antar sensor a dan b) menunjukkan ketelitian metodologis yang baik.

**Analisis Temporal yang Komprehensif**
Paper ini tidak hanya melaporkan angka rata-rata, tapi juga menganalisis variasi **diurnal** (pola bimodal pagi-malam), variasi **mingguan** (weekday vs weekend), dan variasi **musiman** — semuanya disajikan dengan visualisasi yang informatif menggunakan boxplot dan time-series.

**Interpretasi Kontekstual yang Kaya**
Penulis berhasil mengaitkan temuan teknis dengan konteks lokal yang spesifik: puncak pagi jam 07.00 dikaitkan dengan jam sibuk kendaraan, puncak malam dengan suhu rendah dan kondisi udara yang stagnan, serta konsentrasi tinggi di musim kemarau dengan minimnya curah hujan. Ini membuat paper ini informatif tidak hanya bagi insinyur tapi juga bagi pembuat kebijakan.

**Tinjauan Literatur yang Memadai**
Paper ini dengan baik memposisikan dirinya dalam konteks studi PurpleAir global (Korea, Yunani, Uganda, Australia, AS), menunjukkan kesadaran yang baik terhadap literatur terkait.

---

### ⚠️ Kelemahan & Catatan Kritis

**Hanya Satu Lokasi Sampling**
Seluruh pengukuran dilakukan di satu titik — kawasan nuklir Tamansari, Bandung. Ini membatasi representasi spasial secara signifikan. Bandung memiliki topografi "cekungan" yang membuat distribusi polutan bervariasi antar wilayah, dan satu sensor tidak bisa mewakili keseluruhan kota.

**Gap Data September–November 2022**
Ada periode off selama 3 bulan akibat masalah teknis pada SuperSASS. Ini menyebabkan dataset tidak lengkap dan berpotensi bias terutama pada analisis musiman, karena periode tersebut mencakup transisi musim kemarau ke hujan yang penting.

**PA-II Overestimasi Konsisten 24%**
Meski diakui dan dibahas, overestimasi sebesar 24% adalah angka yang cukup besar untuk monitoring lingkungan regulasi. Paper ini tidak menyajikan persamaan koreksi spesifik untuk kondisi Bandung, padahal data selama 12 bulan sebenarnya cukup untuk membangun model koreksi lokal yang lebih akurat.

**Tidak Ada Analisis Source Apportionment**
Paper mengidentifikasi sumber PM2.5 secara kualitatif (kendaraan, industri, pembakaran biomassa), namun tidak melakukan analisis kuantitatif seperti **Positive Matrix Factorization (PMF)** atau receptor modeling untuk memverifikasi kontribusi masing-masing sumber. Padahal alat seperti SuperSASS sebenarnya dirancang juga untuk speciation analysis yang bisa mendukung source apportionment.

**Keterbatasan Sensor RH yang Serius Namun Kurang Ditindaklanjuti**
PA-II secara konsisten mencatat **RH (Kelembaban Relatif)** yang lebih rendah 2.59–35% dibanding referensi BPS. Ini adalah masalah serius karena RH mempengaruhi akurasi pengukuran PM2.5 optis. Meski dibahas, solusinya hanya disebutkan sebagai "future work" tanpa langkah konkret.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Accept dengan Minor Revision** — Ini adalah paper yang solid dan well-executed. Perbaikan utama yang disarankan adalah penyajian persamaan koreksi lokal untuk kondisi Bandung dan penambahan diskusi yang lebih kritis mengenai implikasi gap data September–November terhadap validitas analisis musiman.