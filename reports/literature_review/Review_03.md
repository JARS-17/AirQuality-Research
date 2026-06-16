## JURNAL 3
**"Air Quality Estimation Using LSTM and An Approach for Data Processing Techniques"**
*Ton-Thien, Nguyen, Le & Duong — MediaEval 2021, CEUR-WS*
---
### ✅ Kekuatan Utama
* **Pendekatan Preprocessing yang Praktis:** Penanganan **missing values** secara bertingkat menggunakan **mean imputation** lalu **XGBoost**.
* **Cakupan Multi-Negara:** Dataset mencakup tiga negara (Brunei, Singapura, Thailand).
* **Perbandingan Tiga Varian LSTM:** Membandingkan LSTM standar, **Bi-LSTM**, dan **Stacked LSTM**.

### ⚠️ Kelemahan & Catatan Kritis
* **Bukan Jurnal Utama:** Ini adalah paper workshop kompetisi, bukan artikel peer-review ketat.
* **Overfitting yang Parah:** Indikasi **overfitting** sangat serius (RMSE melonjak 3x lipat pada test set).
* **Tidak Ada Strategi Anti-Overfitting:** Tidak disebutkan penggunaan **dropout**, **early stopping**, atau **L2 regularization**.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐ |
| Kualitas Metodologi | ⭐⭐ |
| Kualitas Analisis | ⭐ |
| Generalisasi Temuan | ⭐⭐ |

**Rekomendasi:** Workshop Only