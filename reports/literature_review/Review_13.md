## JURNAL 13
**"Interpretable machine learning framework for air quality prediction in Istanbul using Shapley additive explanations (SHAP)"**
*Enes Birinci, et al. — Stochastic Environmental Research and Risk Assessment, 2026*


### ✅ Kekuatan Utama
Penggunaan kerangka kerja pemodelan komparatif yang kokoh dengan melibatkan 7 algoritma Machine Learning berbeda (XGBoost, Extra Trees, dll) dan optimalisasi hyperparameter Bayesian. Pendekatan memisahkan data berdasarkan karakteristik spasial (urban, rural) dan temporal (musim dingin, musim panas) sangat tepat. Model ini secara elegan mengintegrasikan SHAP untuk menjelaskan peran spesifik dari kondisi meteorologis dalam peningkatan polusi udara secara gamblang per lokasi.

### ⚠️ Kelemahan & Catatan Kritis
Terdapat bukti overfitting pada model pedesaan (rural Arnavutköy) di musim panas di mana kinerja prediksi untuk PM10 menurun drastis (test R²=0.61) meskipun proses latihannya menghasilkan performa baik. Model ini juga murni mengandalkan input meteorologi dan belum menginjeksi metrik emisi antropogenik atau tata guna lahan yang berpotensi mengatasi penurunan akurasi tersebut. Selain itu, hasil interpretasi SHAP tidak divalidasi lebih lanjut melalui pengujian *ablation*.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Butuh investigasi dan perbaikan mengenai penurunan performa model (*overfitting*) di kawasan pedesaan saat musim panas serta validasi empiris hasil SHAP.