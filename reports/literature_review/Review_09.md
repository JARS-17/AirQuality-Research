## JURNAL 9
**"Application of CNN-LSTM Algorithm for PM2.5 Concentration Forecasting in the Beijing-Tianjin-Hebei Metropolitan Area"**
*Yuxuan Su, Junyu Li, Lilong Liu, Xi Guo, Liangke Huang, Mingyun Hu — Atmosphere, 2023*


### ✅ Kekuatan Utama
Paper ini secara inovatif memasukkan fitur meteorologi spesifik yaitu *Precipitable Water Vapor* (PWV) yang dikombinasikan dengan arsitektur CNN-LSTM untuk mengekstraksi korelasi spasial-temporal di 10 kota metropolitan. Fokus studinya juga terarah secara unik pada prediksi kualitas udara di masa krusial berlibur (*National Day holiday*), yang memiliki anomali dinamika lalu lintas dan aktivitas masyarakat.

### ⚠️ Kelemahan & Catatan Kritis
Validasi eksperimen sangat sempit dan dipertanyakan reliabilitasnya karena hanya diuji pada rentang waktu 7 hari (1-7 Oktober 2021/2022). Jumlah data pengujian yang terlalu sedikit ini membuat model sangat rentan terhadap *overfitting* pada pola cuaca sesaat. Analisis perbandingan juga minim, hanya membandingkan model dengan LSTM murni dan BPNN, mengabaikan algoritma *state-of-the-art* lainnya.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
| : | : |
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Major Revision** — Meskipun ide dasarnya menarik, dataset pengujian yang hanya berdurasi satu minggu tidak cukup untuk mengevaluasi ketahanan dan reliabilitas model deret waktu.