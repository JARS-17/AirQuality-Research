## JURNAL 10
**"A Hybrid Spatiotemporal Deep Model Based on CNN and LSTM for Air Pollution Prediction"**
*Stefan Tsokov, Milena Lazarova, Adelina Aleksieva-Petrova — Sustainability, 2022*


### ✅ Kekuatan Utama
Metodologi ini memecahkan masalah pencarian topologi manual dengan memanfaatkan Algoritma Genetika (GA) untuk mengotomatisasi seleksi fitur input dan melakukan *hyperparameter tuning* pada arsitektur CNN-LSTM. Model ini juga mengusulkan strategi imputasi data yang hilang (*missing values*) secara canggih dengan teknik hybrid antara interpolasi linier dan nilai rata-rata musiman historis.

### ⚠️ Kelemahan & Catatan Kritis
Metode representasi spasial memetakan stasiun lingkungan terdekat ke dalam gambar matriks (2D pixel representation) untuk dikonvolusi. Pendekatan ini rentan menghasilkan representasi spasial yang renggang (*sparse*) dan kaku; penggunaan arsitektur *Graph Neural Network* (GNN) mungkin akan jauh lebih efektif. Tingginya beban komputasi GA juga membuat penulis hanya membatasi pengujian pada 3 stasiun saja.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
| : | : |
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Kombinasi Algoritma Genetika dengan deep learning merupakan kontribusi solid, namun keterbatasan pengujian pada sedikit stasiun membatasi klaim konklusifnya.