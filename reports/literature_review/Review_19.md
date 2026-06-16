## JURNAL 19
**"Sistem Prediksi Kualitas Udara Menggunakan Algoritma Long Short-Term Memory (LSTM)"**
*Muhammad Zaki Wicaksono, Ledy Elsera Astrianty — TIN: Terapan Informatika Nusantara, 2025*


### ✅ Kekuatan Utama
Penerapan *Deep Learning* (LSTM) sangat relevan dan terbukti efektif untuk data *time-series* polusi udara. Proses prapemrosesan data dilakukan dengan rapi, termasuk penanganan *missing values* melalui interpolasi linear dan normalisasi. Kekuatan utama penelitian ini adalah hilirisasinya, yaitu pengembangan purwarupa aplikasi GUI (*Graphical User Interface*) yang menjadikannya aplikatif untuk sistem peringatan dini.

### ⚠️ Kelemahan & Catatan Kritis
Dataset hanya berasal dari satu wilayah (Kota Yogyakarta), sehingga model tidak memiliki kemampuan generalisasi spasial. Secara performa, prediksi parameter *Hydrocarbon* (HC) memiliki MAE yang lebih besar dari MAD, menandakan model gagal mempelajari variansi alami dari parameter HC tersebut (*underfitting* pada fitur spesifik). Tidak ada komparasi dengan model time-series baseline seperti ARIMA atau GRU.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Perlu menyertakan analisis lebih dalam mengapa model gagal pada prediksi HC dan membandingkan kinerja LSTM dengan model prediksi baseline lainnya.