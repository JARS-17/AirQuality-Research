## JURNAL 7
**"Long short-term memory neural network for air pollutant concentration predictions: Method development and evaluation"**
*Xiang Li, Ling Peng, Xiaojing Yao, Shaolong Cui, Yuan Hu, Chengzeng You, Tianhe Chi — Environmental Pollution, 2017*


### ✅ Kekuatan Utama
Model LSTME yang diusulkan berhasil memodelkan korelasi spasial-temporal secara efektif dengan mengintegrasikan data historis dari 12 stasiun pemantauan sekaligus. Penggunaan data tambahan seperti data meteorologi (suhu, kelembapan, angin, visibilitas) dan data "time stamp" (bulan dan jam berformat *one-hot encoding*) terbukti secara signifikan meningkatkan kinerja ekstraksi fitur berjangka panjang dibandingkan model dangkal (seperti ARMA, SVR) atau LSTM tradisional.

### ⚠️ Kelemahan & Catatan Kritis
Dataset yang digunakan (2014-2016) sudah cukup usang, sehingga polanya mungkin tidak lagi merepresentasikan kondisi emisi modern. Selain itu, model ini tidak menggunakan mekanisme konvolusi (CNN) secara eksplisit untuk spasial, melainkan hanya menumpuk input stasiun (*stacked inputs*), yang kurang optimal secara struktural. Tingkat kesalahan prediksi (MAPE) juga terlihat membengkak drastis (hingga 31.47%) pada horizon prakiraan yang lebih panjang (13–24 jam).

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
| : | : |
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Accept** — Merupakan paper fundamental yang kuat pada zamannya dengan metodologi yang solid, validasi komparatif yang baik, dan ablasi fitur yang jelas.