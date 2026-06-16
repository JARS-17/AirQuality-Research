# Review Jurnal 14
**"A Unified Approach to Interpreting Model Predictions"**
*Scott M. Lundberg, Su-In Lee — Advances in Neural Information Processing Systems (NIPS), 2017*

---

### ✅ Kekuatan Utama

**Fondasi Revolusioner untuk XAI**
Paper fundamental yang memperkenalkan **SHapley Additive exPlanations (SHAP)**. Secara brilian menyatukan enam metode interpretasi XAI yang ada sebelumnya (termasuk LIME dan DeepLIFT) ke dalam satu kerangka kerja.

**Landasan Teoretis yang Sangat Kuat**
Menawarkan landasan teori matematika dari **Game Theory** dengan memberikan kepastian jaminan untuk tiga properti krusial: *local accuracy*, *missingness*, dan *consistency*.

**Validasi Eksperimental yang Jelas**
Eksperimen secara tegas membuktikan bahwa atribusi SHAP jauh selaras dengan intuisi kognitif manusia dibandingkan baseline *feature importance* bawaan algoritma.

---

### ⚠️ Kelemahan & Catatan Kritis

**Asumsi Feature Independence yang Rentan**
Pendekatan estimasi *model-agnostic* seperti **KernelSHAP** memiliki asumsi bahwa fitur prediktor bersifat independen. Dalam konteks riil polusi udara, variabel meteorologi biasanya sangat berkorelasi (multikolinieritas), sehingga asumsi independensi berisiko mendistorsi kontribusi margin.

**Kompleksitas Komputasi yang Tinggi**
Kalkulasi nilai Shapley yang presisi bersifat **NP-Hard**. Metode aproksimasi seringkali memakan resource komputasi yang sangat masif apabila diimplementasikan pada model deep learning dengan dataset time-series besar.

**Tidak Spesifik pada Domain Lingkungan**
Karena berupa literatur teoretis ilmu komputer murni, paper ini tidak memberikan pedoman adaptasi metrik SHAP untuk data yang memiliki temporal dependensi seperti polusi udara.

---

### 📊 Penilaian Keseluruhan

| Metrik | Nilai |
|---|---|
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Accept** — Paper wajib dan menjadi dasar absolut secara teori apabila ingin mengadopsi konsep interpretasi XAI (SHAP).