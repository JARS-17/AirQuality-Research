## JURNAL 18
**"Analysis Correlation of Meteorological Factors with PM2.5 Concentrations in Forecasting Air Quality of The City of Jakarta"**
*Ade Ayu Oktaviana, Abdu Fadli Assomadi, and Joni Hermana — IOP Conf. Series: Earth and Environmental Science, 2025*


### ✅ Kekuatan Utama
Penelitian ini menggunakan analisis korelasi Spearman yang sangat sesuai untuk mendeteksi hubungan non-linear monotonik antara faktor meteorologi (curah hujan, suhu, kelembaban, angin) dengan kualitas udara. Penggunaan data reanalisis atmosfer ECMWF EAC4 juga memberikan dimensi spasial yang baik untuk melengkapi data stasiun darat.

### ⚠️ Kelemahan & Catatan Kritis
Kelemahan paling fatal ada pada hasil pemodelan Multiple Linear Regression (MLR) yang mengklaim nilai determinasi (R²) sebesar 0.99. Nilai ini sangat tidak realistis untuk regresi linear sederhana pada data polusi udara yang kompleks dan fluktuatif, mengindikasikan adanya *overfitting* parah atau *data leakage*. Hal ini diperburuk dengan nilai RMSE yang masih cukup tinggi (22.95) meskipun R²-nya nyaris sempurna. Selain itu, model hanya divalidasi pada 4 titik pemantauan.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Major Revision** — Model regresi linear berganda memiliki indikasi overfitting yang sangat parah. Metodologi prediksi perlu dievaluasi ulang secara fundamental.