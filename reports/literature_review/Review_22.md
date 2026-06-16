## JURNAL 22
**"Air quality prediction from images in Indonesia: enhancing model explainability through visual explanation with AQI-net and grad-CAM"**
*Muhammad Labib Alauddin, Novanto Yudistira, and Muhammad Arif Rahman — Environmental Data Science, 2025*


### ✅ Kekuatan Utama
Sangat inovatif. Penelitian ini beralih dari sensor perangkat keras tradisional ke prediksi AQI berbasis ekstraksi fitur gambar (*computer vision*). Model CNN khusus yang dinamakan "AQI-Net" sangat efisien dan mampu mencapai akurasi 99.81% dengan jumlah parameter yang jauh lebih sedikit dari VGG16. Penggunaan Grad-CAM untuk *Explainable AI* sangat brilian untuk menyingkap "kotak hitam" dari CNN. Dataset berupa 11.000 citra juga tersedia untuk publik.

### ⚠️ Kelemahan & Catatan Kritis
Analisis Grad-CAM secara paradoks membongkar kelemahan model: pada kelas "Good", model ternyata lebih berfokus pada struktur buatan manusia (seperti gedung) dibandingkan pada kejernihan langit. Ini mengindikasikan adanya *shortcut learning* atau bias pada dataset (model menghafal lokasi gedung alih-alih kondisi udara). Selain itu, metodologi ini lumpuh pada malam hari karena hanya dilatih menggunakan gambar siang hari.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Pendekatannya sangat brilian, namun perlu ditambahkan pembahasan mitigasi terkait fenomena *shortcut learning* dan saran integrasi metode penanganan citra rendah cahaya (malam hari).