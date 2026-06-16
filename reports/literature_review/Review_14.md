## JURNAL 14
**"A Unified Approach to Interpreting Model Predictions"**
*Scott M. Lundberg, Su-In Lee — Advances in Neural Information Processing Systems (NIPS), 2017*


### ✅ Kekuatan Utama
Paper fundamental dan revolusioner yang memperkenalkan *SHapley Additive exPlanations* (SHAP). Secara brilian menyatukan enam metode interpretasi XAI yang ada sebelumnya (termasuk LIME dan DeepLIFT). Menawarkan landasan teori sangat kuat dari *Game Theory* dengan memberikan kepastian jaminan untuk tiga properti krusial: *local accuracy*, *missingness*, dan *consistency*. Eksperimen studi secara tegas membuktikan metode ini jauh selaras dengan intuisi manusia dibandingkan *baseline*.

### ⚠️ Kelemahan & Catatan Kritis
Karena berupa literatur teoretis mendasar pada domain ilmu komputer, paper ini tidak spesifik pada *time-series* lingkungan. Pendekatan estimasi *model-agnostic* seperti KernelSHAP memiliki asumsi bahwa fitur prediktor bersifat independen (*feature independence*). Dalam konteks riil polusi udara, variabel meteorologi biasanya sangat berkorelasi (multikolinieritas). Asumsi independensi ini pada praktiknya berisiko mendistorsi kontribusi margin dan melahirkan nilai interpretasi yang terbias.

### 📊 Penilaian Keseluruhan
| Metrik | Nilai |
|||
| Relevansi Topik | ⭐⭐⭐⭐ |
| Kebaruan/Novelty | ⭐⭐⭐⭐⭐ |
| Kualitas Metodologi | ⭐⭐⭐⭐⭐ |
| Kualitas Analisis | ⭐⭐⭐⭐⭐ |
| Generalisasi Temuan | ⭐⭐⭐⭐⭐ |

**Rekomendasi: Accept** — Paper wajib dan menjadi dasar absolut secara teori apabila ingin mengadopsi konsep interpretasi XAI (SHAP) pada pemodelan AI.