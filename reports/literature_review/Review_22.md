# Review Jurnal 22
**"Air quality prediction from images in Indonesia: enhancing model explainability through visual explanation with AQI-net and grad-CAM"**
*Muhammad Labib Alauddin, Novanto Yudistira, and Muhammad Arif Rahman — Environmental Data Science, 2025*

---

### ✅ Kekuatan Utama

**Pergeseran Paradigma Data: Computer Vision**
Sangat inovatif. Penelitian ini meninggalkan sensor fisika kimia tradisional dan beralih mengestimasi tingkat AQI lewat ektraksi filter kabut gambar kamera *smartphone* dengan metode **Computer Vision**.

**Optimalisasi Arsitektur AQI-Net**
Mendesain arsitektur CNN khusus (**AQI-Net**) yang efisien, mampu mereduksi parameter drastis dari baseline VGG-16, namun secara presisi mengamankan akurasi hingga **99.81%** pada dataset 11.000 citra terbuka di Jawa.

**Kecemerlangan XAI berbasis Visual (Grad-CAM)**
Penerapan algoritma **Grad-CAM** (*Gradient-weighted Class Activation Mapping*) sebagai teknik *Explainable AI* sangat brilian untuk menerangi area piksel mana yang dijadikan dasar pengambilan keputusan oleh CNN.

---

### ⚠️ Kelemahan & Catatan Kritis

**Fenomena Shortcut Learning Terbongkar XAI**
Peta aktivasi visual (Grad-CAM) justru secara tidak sengaja menyingkap kelemahan kognitif model: model terbukti melakukan **shortcut learning**. Pada klasifikasi kondisi "Good/Baik", jaringan saraf ternyata justru mendeteksi piksel objek "struktur gedung/tepian atap" alih-alih mengukur visibilitas kejernihan langit secara murni.

**Ketidakmampuan Analisis Tanpa Cahaya Matahari**
Metodologi ekstraksi ketebalan kabut optis ini secara inheren **lumpuh total di malam hari** karena murni dilatih atas dataset siang berpencahayaan cerah.

**Bias Klasifikasi Gambar Statis**
Algoritma belum kebal terhadap bias citra sekunder (misal: asap kendaraan lokal instan, flare matahari) yang dapat mencemari klasifikasi kelas tingkat polusi udara makro.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Pendekatannya sangat futuristik, namun sangat krusial untuk melatih ulang pembobotan citra langit dan mitigasi kebergantungan pola geometris objek non-langit (*shortcut learning*).