# Review Jurnal 06
**"Deep Learning for Air Quality Forecasts: a Review"**
*Liao, Zhu, Wu, Pan, Tang & Wang — Current Pollution Reports, Springer, 2020*

---

### ✅ Kekuatan

**Ini adalah Paper Fondasi yang Wajib Anda Baca**
Sebagai pembimbing, saya tekankan ini: paper review dari Springer ini adalah *roadmap* terbaik untuk memahami lanskap **deep learning** dalam prediksi kualitas udara. Diterbitkan oleh Chinese Academy of Sciences, ini bukan paper biasa — ini adalah karya dari institusi riset atmosfer terkemuka di dunia.

**Cakupan Arsitektur yang Komprehensif**
Paper ini memetakan seluruh ekosistem deep learning untuk AQI: **RNN, LSTM, GRU** (temporal), **CNN, SAE, DBN** (spasial), hingga **STDL/CNN-LSTM/CNN-GRU** (spatiotemporal). Ini memberi Anda kerangka konseptual yang solid untuk memilih metode yang tepat.

**Lima Domain Aplikasi yang Dipetakan dengan Jelas**
Review ini tidak hanya membahas prediksi — tapi juga: (1) data gap filling, (2) inversi data satelit, (3) speedup CTM, (4) prediksi spatiotemporal, dan (5) estimasi sumber emisi. Ini membuka wawasan bahwa prediksi AQI hanyalah satu bagian dari ekosistem yang jauh lebih luas.

**Identifikasi Tantangan Masa Depan yang Masih Relevan**
Meski ditulis 2020, tantangan yang diidentifikasi paper ini sebagian besar masih valid di 2025: tidak ada benchmark dataset standar, **black-box problem**, kurangnya studi jangka panjang (>7 hari), dan belum adanya integrasi komprehensif antara DL dan CTM.

**Pembanding Tradisional yang Jujur**
Paper ini tidak membesar-besarkan deep learning. Ia secara fair menjelaskan keterbatasan CTM dan metode statistik klasik (ARIMA, MLR), kemudian menunjukkan di mana DL dapat memberikan nilai tambah nyata.

---

### ⚠️ Kelemahan & Catatan Kritis

**Sudah 5 Tahun — Beberapa Bagian Sudah Outdated**
Ini ditulis 2020, sebelum era **Transformer** dan **Attention mechanism** mendominasi riset DL. Tidak ada pembahasan tentang model berbasis Transformer (Informer, PatchTST, iTransformer) yang kini menjadi state-of-the-art untuk time series. Untuk Anda, ini sekaligus peluang: gap antara review 2020 dan kondisi 2025 adalah area penelitian yang sangat aktif.

**Tidak Ada Studi dari Asia Tenggara**
Hampir semua paper yang dirujuk berasal dari Cina, Korea, Amerika, dan Eropa. Indonesia, Filipina, Thailand — tidak ada satu pun. Ini adalah konfirmasi eksplisit dari gap geografis yang menjadi positioning penelitian Anda.

**Tidak Ada Perbandingan Kuantitatif Antar Model**
Sebagai review paper, tidak ada tabel meta-analisis yang membandingkan RMSE atau MAE antar studi secara terstandar. Pembaca harus membaca satu per satu paper yang dirujuk untuk membandingkan performa model. Ini kelemahan umum review non-systematic, tapi tetap perlu dicatat.

**Aspek Low-Cost Sensor Tidak Dibahas**
Paper ini fokus pada stasiun pemantauan resmi dan data satelit. Potensi **low-cost sensor** (PurpleAir, SDS011, dll.) untuk densifikasi jaringan pemantauan — yang sangat relevan di negara berkembang seperti Indonesia — tidak disentuh sama sekali.

---

### 📊 Penilaian Keseluruhan

| Aspek | Nilai | Catatan |
|---|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ | Fondasi wajib untuk siapapun yang meneliti DL+AQI |
| Kebaruan / Novelty | ⭐⭐⭐ | Tinggi saat terbit 2020, kini sebagian sudah terlampaui |
| Kualitas Metodologi | ⭐⭐⭐⭐ | Sistematis, taksonomi arsitektur jelas |
| Kualitas Analisis | ⭐⭐⭐⭐ | Prospek dan tantangan diidentifikasi dengan tajam |
| Generalisasi Temuan | ⭐⭐ | Tidak ada konteks Asia Tenggara sama sekali |

**Rekomendasi: Accept**