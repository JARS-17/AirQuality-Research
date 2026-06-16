# Review Jurnal 21
**"A Framework for Air Pollution Monitoring in Smart Cities by Using IoT and Smart Sensors"**
*Arshad Ali — Informatica, 2022*

---

### ✅ Kekuatan Utama

**Desain Arsitektur Multi-Layer Konseptual**
Paper merancang konsep arsitektur yang komprehensif bagi pemantauan polusi udara berbasis **Internet of Things (IoT)** skala kota cerdas (*smart city*).

**Pilihan Protokol Komunikasi Efisien**
Pendefinisian standar perangkat keras yang terintegrasi secara spesifik dengan protokol pengiriman data rendah daya (**ZigBee**) menuntaskan problem kendala umur baterai pada instalasi sensor terpencil.

---

### ⚠️ Kelemahan & Catatan Kritis

**Ketiadaan Implementasi Fisik Sama Sekali**
Studi ini terkurung penuh pada ranah simulasi teoretis. **Sama sekali tidak ada purwarupa fisik (*hardware prototype*)** yang dibangun di lapangan untuk divalidasi keandalannya di ruang terbuka.

**Validasi Data yang Nihil**
Tanpa pengujian empiris, paper gagal memberikan kepastian akurasi pembacaan polutan, latensi transmisi jaringan saat padat data, rasio *packet loss*, maupun efisiensi konsumsi daya aktual.

**Pustaka Referensi yang Mulai Usang**
Sebagian besar referensi teknologi komputasi mikrokontroler yang diajukan sudah tertinggal zaman jika disandingkan dengan standar perangkat Edge-AI (*micro-NPU*) masa kini.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Reject / Major Revision** — Membutuhkan pengadaan dan eksperimentasi *hardware* purwarupa nyata yang menghasilkan data lapangan untuk membuktikan *framework* teoretis yang diajukan.