# Review Jurnal 13
**"Interpretable machine learning framework for air quality prediction in Istanbul using Shapley additive explanations (SHAP)"**
*Enes Birinci, et al. — Stochastic Environmental Research and Risk Assessment, 2026*

---

### ✅ Kekuatan Utama

**Kerangka Komparatif yang Kokoh**
Melibatkan **7 algoritma Machine Learning berbeda** (XGBoost, Extra Trees, dll) dipadukan dengan optimalisasi hyperparameter Bayesian, menghasilkan pipeline pemodelan yang sangat kuat secara teknis.

**Pemecahan Data Spasial-Temporal yang Tepat**
Pendekatan memisahkan data berdasarkan karakteristik spasial (**urban vs rural**) dan temporal (**musim dingin vs musim panas**) sangat tepat untuk menangkap dinamika iklim lokal yang kompleks di Istanbul.

**Integrasi SHAP yang Elegan**
Model ini berhasil menggunakan **SHAP** untuk menjelaskan peran spesifik dari kondisi meteorologis dalam peningkatan polusi udara secara gamblang per lokasi.

---

### ⚠️ Kelemahan & Catatan Kritis

**Overfitting pada Data Musim Panas Pedesaan**
Terdapat bukti **overfitting** pada model pedesaan (rural Arnavutköy) di musim panas di mana kinerja prediksi untuk PM10 menurun drastis (test R²=0.61) meskipun proses latihannya menghasilkan performa baik.

**Kurangnya Variabel Antropogenik**
Model ini murni mengandalkan input meteorologi dan belum menginjeksi metrik emisi antropogenik atau tata guna lahan, yang berpotensi menjadi penyebab utama penurunan akurasi tersebut.

**Validasi SHAP yang Kurang**
Hasil interpretasi SHAP hanya ditampilkan secara visual namun tidak divalidasi lebih lanjut melalui pengujian **ablation study** untuk membuktikan bahwa fitur terpenting memang krusial bagi model.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐ |

**Rekomendasi: Minor Revision** — Butuh perbaikan terkait overfitting di kawasan pedesaan saat musim panas serta validasi empiris hasil atribusi SHAP.