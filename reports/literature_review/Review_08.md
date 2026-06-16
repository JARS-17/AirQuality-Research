## JURNAL 8
**"Air Quality Prediction and Ranking Assessment Based on Bootstrap-XGBoost Algorithm and Ordinal Classification Models"**
*Jingnan Yang, Yuzhu Tian, Chun Ho Wu — Atmosphere, 2024*


### ✅ Kekuatan Utama
Pendekatannya sangat praktikal dengan menyertakan interval kepercayaan prediksi 95% melalui pendekatan Bootstrap-XGBoost, sehingga tidak sekadar bergantung pada prakiraan *single-point*. Selain itu, paper ini memadukan pemodelan kontinu untuk nilai indeks polusi (AQI) dengan pemodelan klasifikasi ordinal (Ordinal Logit dan Probit) untuk penilaian peringkat AQI, memberikan landasan yang kokoh bagi pembuatan kebijakan.

### ⚠️ Kelemahan & Catatan Kritis
Penelitian ini rawan terhadap *overfitting* musiman karena hanya menggunakan data satu tahun (Oktober 2022–September 2023) untuk satu kota spesifik (Xi'an). Lebih kritis lagi, kinerja baseline deep learning (seperti LSTM dan CNN) dalam studi ini dilaporkan sangat buruk dibandingkan model *tree-based*. Hal ini mengindikasikan kemungkinan absennya *hyperparameter tuning* yang memadai pada baseline tersebut, membuat komparasinya terasa kurang adil.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
| : | : |
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi: Minor Revision** — Eksperimen perlu diperluas dengan rentang data multi-tahun, dan performa baseline Deep Learning perlu ditinjau ulang agar komparasinya lebih valid.