const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageNumber, PageBreak, Header, Footer, VerticalAlign
} = require('docx');
const fs = require('fs');
const path = require('path');

// ─── COLOR PALETTE ─────────────────────────────────────────
const BLUE_DARK   = "1F4E79";
const BLUE_MED    = "2E75B6";
const BLUE_LIGHT  = "D6E4F0";
const BLUE_XLIGHT = "EBF3FB";
const TEAL        = "1D6A72";
const TEAL_LIGHT  = "D4EEF0";
const AMBER       = "7B5E00";
const AMBER_LIGHT = "FFF3CD";
const GREEN_DARK  = "1E5631";
const GREEN_LIGHT = "D4EDDA";
const RED_DARK    = "7B1A1A";
const RED_LIGHT   = "FDEAEA";
const GRAY_DARK   = "404040";
const GRAY_MED    = "666666";
const GRAY_LIGHT  = "F2F2F2";
const WHITE       = "FFFFFF";

// ─── BORDER HELPERS ────────────────────────────────────────
const border = (color = "CCCCCC", size = 4) => ({ style: BorderStyle.SINGLE, size, color });
const noBorder = () => ({ style: BorderStyle.NONE, size: 0, color: "FFFFFF" });
const allBorders = (c, s = 4) => ({ top: border(c, s), bottom: border(c, s), left: border(c, s), right: border(c, s) });
const noBorders = () => ({ top: noBorder(), bottom: noBorder(), left: noBorder(), right: noBorder() });

// ─── TEXT HELPERS ──────────────────────────────────────────
const run = (text, opts = {}) => new TextRun({ text, font: "Arial", ...opts });
const bold = (text, size = 22, color = GRAY_DARK) => run(text, { bold: true, size, color });
const normal = (text, size = 20, color = GRAY_DARK) => run(text, { size, color });
const italic = (text, size = 20, color = GRAY_MED) => run(text, { italics: true, size, color });
const muted = (text) => run(text, { size: 18, color: GRAY_MED });

const para = (children, opts = {}) => new Paragraph({ children: Array.isArray(children) ? children : [children], spacing: { after: 120 }, ...opts });
const h1 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [run(text, { bold: true, size: 28, color: WHITE })],
  shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
  spacing: { before: 240, after: 0 },
  indent: { left: 200, right: 200 },
  border: { bottom: border(BLUE_MED, 8) },
});
const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  children: [run(text, { bold: true, size: 24, color: WHITE })],
  shading: { fill: BLUE_MED, type: ShadingType.CLEAR },
  spacing: { before: 300, after: 120 },
  indent: { left: 160 },
});
const h3 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_3,
  children: [run(text, { bold: true, size: 22, color: BLUE_DARK })],
  border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BLUE_LIGHT, space: 2 } },
  spacing: { before: 240, after: 100 },
});
const h4 = (text) => new Paragraph({
  children: [run(text, { bold: true, size: 20, color: TEAL })],
  spacing: { before: 160, after: 60 },
});

const bullet = (text, level = 0) => new Paragraph({
  numbering: { reference: "bullets", level },
  children: [normal(text)],
  spacing: { after: 80 },
});
const numbered = (text, level = 0) => new Paragraph({
  numbering: { reference: "numbers", level },
  children: [normal(text)],
  spacing: { after: 80 },
});

const spacer = (after = 160) => new Paragraph({ children: [run("")], spacing: { after } });
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

// ─── CALLOUT BOX (highlight note) ─────────────────────────
const callout = (label, text, fillColor, textColor) => {
  const CONTENT_W = 9360;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [
      new TableRow({ children: [
        new TableCell({
          width: { size: CONTENT_W, type: WidthType.DXA },
          shading: { fill: fillColor, type: ShadingType.CLEAR },
          borders: { top: border(textColor, 16), bottom: noBorder(), left: noBorder(), right: noBorder() },
          margins: { top: 120, bottom: 120, left: 200, right: 200 },
          children: [
            new Paragraph({ children: [run(label, { bold: true, size: 20, color: textColor })], spacing: { after: 60 } }),
            new Paragraph({ children: [normal(text, 20, GRAY_DARK)], spacing: { after: 0 } }),
          ]
        })
      ]})
    ]
  });
};

// ─── COLORED SECTION HEADER TABLE ─────────────────────────
const sectionTag = (number, title, color) => {
  const CONTENT_W = 9360;
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [900, 8460],
    rows: [
      new TableRow({ children: [
        new TableCell({
          width: { size: 900, type: WidthType.DXA },
          shading: { fill: color, type: ShadingType.CLEAR },
          borders: noBorders(),
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run(number, { bold: true, size: 28, color: WHITE })] })]
        }),
        new TableCell({
          width: { size: 8460, type: WidthType.DXA },
          shading: { fill: "F8FBFF", type: ShadingType.CLEAR },
          borders: { top: border(color, 4), bottom: border(color, 4), left: noBorder(), right: border(color, 4) },
          margins: { top: 80, bottom: 80, left: 200, right: 120 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ children: [run(title, { bold: true, size: 24, color: BLUE_DARK })] })]
        }),
      ]})
    ]
  });
};

// ─── STANDARD TABLE BUILDER ────────────────────────────────
const buildTable = (headers, rows, colWidths) => {
  const totalW = colWidths.reduce((a, b) => a + b, 0);
  const headerRow = new TableRow({
    tableHeader: true,
    children: headers.map((h, i) => new TableCell({
      width: { size: colWidths[i], type: WidthType.DXA },
      shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
      borders: allBorders("3A6EA8", 4),
      margins: { top: 80, bottom: 80, left: 120, right: 120 },
      children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run(h, { bold: true, size: 18, color: WHITE })] })]
    }))
  });

  const dataRows = rows.map((row, ri) => new TableRow({
    children: row.map((cell, ci) => {
      const isEven = ri % 2 === 0;
      const isHighlight = typeof cell === 'object' && cell.highlight;
      const text = typeof cell === 'object' ? cell.text : cell;
      const fillColor = isHighlight ? AMBER_LIGHT : (isEven ? WHITE : GRAY_LIGHT);
      return new TableCell({
        width: { size: colWidths[ci], type: WidthType.DXA },
        shading: { fill: fillColor, type: ShadingType.CLEAR },
        borders: allBorders("CCCCCC", 3),
        margins: { top: 60, bottom: 60, left: 120, right: 120 },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ children: [normal(text, 18)] })]
      });
    })
  }));

  return new Table({
    width: { size: totalW, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [headerRow, ...dataRows]
  });
};

// ─── GAP MATRIX TABLE ─────────────────────────────────────
const gapMatrix = () => {
  const CONTENT_W = 9360;
  const cols = [2800, 1320, 1320, 1320, 1320, 1280];
  const aspects = ["Variabel Polutan", "Metode ML/DL", "Cakupan Spasial", "Data Sensor", "Konteks Lokal"];
  const studies = [
    ["Smith et al. (2023)", "PM2.5, PM10", "LSTM, GRU", "Global", "Komersial", "Tidak ada"],
    ["Zhang et al. (2024)", "PM2.5 saja", "Random Forest", "Cina", "Stasiun resmi", "Tidak ada"],
    ["Ali et al. (2023)", "PM2.5, O3, NO2", "XGBoost", "Asia Selatan", "Low-cost", "Sebagian"],
    ["Kumar et al. (2024)", "PM2.5, CO", "CNN-LSTM", "India", "IoT sensor", "Tidak ada"],
    ["[Penelitian Anda]", { text: "PM2.5, PM10, AQI", highlight: true }, { text: "Hybrid DL + XAI", highlight: true }, { text: "Indonesia/Jawa Barat", highlight: true }, { text: "Low-cost + satelit", highlight: true }, { text: "Penuh (Bandung)", highlight: true }],
  ];

  const headerCells = ["Studi / Peneliti", ...aspects].map((h, i) => new TableCell({
    width: { size: cols[i], type: WidthType.DXA },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    borders: allBorders("3A6EA8", 4),
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [run(h, { bold: true, size: 17, color: WHITE })] })]
  }));

  const dataRows = studies.map((row, ri) => {
    const isYours = ri === studies.length - 1;
    return new TableRow({
      children: row.map((cell, ci) => {
        const text = typeof cell === 'object' ? cell.text : cell;
        const highlight = typeof cell === 'object' && cell.highlight;
        const fill = isYours ? (highlight ? GREEN_LIGHT : BLUE_XLIGHT) : (ri % 2 === 0 ? WHITE : GRAY_LIGHT);
        return new TableCell({
          width: { size: cols[ci], type: WidthType.DXA },
          shading: { fill, type: ShadingType.CLEAR },
          borders: allBorders("CCCCCC", 3),
          margins: { top: 60, bottom: 60, left: 100, right: 100 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            children: [run(text, { bold: isYours, size: 17, color: isYours ? BLUE_DARK : GRAY_DARK })],
            alignment: ci === 0 ? AlignmentType.LEFT : AlignmentType.CENTER
          })]
        });
      })
    });
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: cols,
    rows: [new TableRow({ tableHeader: true, children: headerCells }), ...dataRows]
  });
};

// ─── COVER PAGE ───────────────────────────────────────────
const coverPage = () => [
  spacer(1200),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 0 },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    border: { top: border(BLUE_MED, 20) },
    indent: { left: -200, right: -200 },
    children: [run("", { size: 8 })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0 },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    children: [run("TEMPLATE", { bold: true, size: 22, color: "AED6F1", allCaps: true })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0 },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    children: [run("Literature Review & Gap Analysis", { bold: true, size: 40, color: WHITE })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 0 },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    children: [run("Penelitian Kualitas Udara berbasis Data Science", { italics: true, size: 26, color: "AED6F1" })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 0, after: 0 },
    shading: { fill: BLUE_DARK, type: ShadingType.CLEAR },
    border: { bottom: border(BLUE_MED, 20) },
    indent: { left: -200, right: -200 },
    children: [run("", { size: 12 })]
  }),
  spacer(400),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 80 },
    children: [run("Disusun oleh:", { size: 20, color: GRAY_MED })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 60 },
    border: { bottom: border(BLUE_LIGHT, 4) },
    children: [run("[Nama Peneliti]", { bold: true, size: 28, color: BLUE_DARK })]
  }),
  spacer(80),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [muted("[Program Studi / Institusi]")] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [muted("[Email Peneliti]")] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [muted("Tahun: [YYYY]")] }),
  spacer(200),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 40 },
    shading: { fill: TEAL_LIGHT, type: ShadingType.CLEAR },
    children: [run("Topik Penelitian: [Judul Topik / Judul Sementara Penelitian]", { bold: true, size: 22, color: TEAL })]
  }),
  spacer(200),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 0 },
    children: [run("Pembimbing:", { size: 20, color: GRAY_MED })]
  }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [bold("[Nama Pembimbing]", 22, BLUE_DARK)] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 0 }, children: [muted("[Institusi Pembimbing]")] }),
  pageBreak()
];

// ─── DOCUMENT BODY ────────────────────────────────────────
const body = [

  // ── PETUNJUK PENGGUNAAN ────────────────────────────────
  sectionTag("!", "Petunjuk Penggunaan Template", AMBER),
  spacer(80),
  callout(
    "Cara menggunakan template ini",
    "Ganti semua teks di dalam [ kurung siku ] dengan konten penelitian Anda. Setiap bagian sudah dirancang sebagai panduan terstruktur — Anda cukup mengisi informasi yang relevan sesuai topik dan literatur yang Anda temukan.",
    AMBER_LIGHT, AMBER
  ),
  spacer(80),
  h4("Bagian yang WAJIB diisi:"),
  bullet("Identitas peneliti dan judul penelitian (halaman cover)"),
  bullet("Fokus dan ruang lingkup kajian (Bagian 1)"),
  bullet("Minimal 20 paper untuk tabel sintesis (Bagian 3)"),
  bullet("Gap analysis yang jelas dan terukur (Bagian 4)"),
  bullet("Keyword search strategy yang spesifik (Bagian 2)"),
  spacer(160),

  // ── BAGIAN 1 ──────────────────────────────────────────
  sectionTag("1", "Identifikasi Fokus Penelitian", BLUE_DARK),
  spacer(80),
  h3("1.1 Latar Belakang Singkat"),
  para([normal("Tuliskan 1–2 paragraf yang menjelaskan mengapa topik ini penting dan relevan. Fokuskan pada urgensi masalah dari sisi data science dan kualitas udara.")]),
  para([
    italic("Contoh: Kualitas udara di kota-kota besar Indonesia, khususnya Bandung, menunjukkan fluktuasi yang signifikan akibat pertumbuhan industri dan mobilitas kendaraan bermotor. Pendekatan data science berbasis machine learning menawarkan potensi prediksi AQI yang lebih akurat dan real-time dibanding metode konvensional. Namun, riset di konteks Indonesia masih sangat terbatas...")
  ]),
  spacer(80),

  h3("1.2 Pertanyaan Penelitian Awal"),
  callout(
    "Rumuskan 2–3 pertanyaan penelitian di sini",
    "[RQ1] Algoritma machine learning apa yang paling efektif untuk memprediksi AQI berbasis data sensor low-cost di Bandung?\n[RQ2] Faktor meteorologi apa yang paling berpengaruh terhadap konsentrasi PM2.5 di Jawa Barat?\n[RQ3] Bagaimana explainability (XAI) dapat meningkatkan interpretasi model prediksi AQI?",
    BLUE_XLIGHT, BLUE_MED
  ),
  spacer(80),

  h3("1.3 Scope dan Batasan Kajian"),
  spacer(40),
  buildTable(
    ["Dimensi", "Cakupan dalam Kajian Ini", "Alasan/Catatan"],
    [
      ["Periode literatur", "2019 – 2025", "Fokus pada perkembangan terkini ML untuk AQI"],
      ["Polutan utama", "PM2.5, PM10, AQI komposit", "Paling relevan di konteks urban Indonesia"],
      ["Pendekatan metode", "Machine learning, deep learning, hybrid", "Sesuai tren riset global"],
      ["Wilayah studi", "Indonesia dan Asia Tenggara (prioritas)", "Gap utama dalam literatur global"],
      ["Bahasa publikasi", "Inggris dan Indonesia", "Akses ke Scopus dan Sinta"],
      ["Tipe sensor", "Low-cost sensor + stasiun resmi", "Relevan untuk kondisi Indonesia"],
    ],
    [2800, 3200, 3360]
  ),
  spacer(160),

  // ── BAGIAN 2 ──────────────────────────────────────────
  sectionTag("2", "Strategi Pencarian Literatur (Search Strategy)", TEAL),
  spacer(80),
  h3("2.1 Database yang Digunakan"),
  buildTable(
    ["Database", "URL / Akses", "Keunggulan", "Jumlah Paper Ditemukan"],
    [
      ["Scopus", "scopus.com", "Q1–Q4 terverifikasi, filter canggih", "[...]"],
      ["Web of Science", "webofscience.com", "Impact Factor, JCR quartile", "[...]"],
      ["Google Scholar", "scholar.google.com", "Cakupan luas, termasuk grey literature", "[...]"],
      ["Semantic Scholar", "semanticscholar.org", "AI-powered, citation graph", "[...]"],
      ["IEEE Xplore", "ieeexplore.ieee.org", "Konferensi & jurnal teknik/komputasi", "[...]"],
      ["PubMed/PMC", "pubmed.ncbi.nlm.nih.gov", "Kesehatan lingkungan, epidemiologi", "[...]"],
    ],
    [2000, 2500, 3100, 1760]
  ),
  spacer(120),

  h3("2.2 Keyword Search String"),
  callout(
    "String pencarian utama (gunakan di semua database)",
    '("air quality" OR "AQI" OR "PM2.5" OR "PM10") AND ("machine learning" OR "deep learning" OR "prediction" OR "forecasting") AND ("Indonesia" OR "Southeast Asia" OR "urban")',
    BLUE_XLIGHT, BLUE_MED
  ),
  spacer(80),
  h4("Variasi keyword berdasarkan subtopik:"),
  buildTable(
    ["Subtopik", "Keyword Tambahan", "Operator"],
    [
      ["Model prediksi", '"LSTM" OR "XGBoost" OR "Random Forest" OR "CNN" OR "transformer"', 'AND dengan string utama'],
      ["Low-cost sensor", '"low-cost sensor" OR "PurpleAir" OR "IoT sensor" OR "sensor calibration"', 'AND dengan string utama'],
      ["Explainability", '"XAI" OR "SHAP" OR "LIME" OR "explainable AI" OR "interpretable"', 'AND dengan ML + AQI'],
      ["Kesehatan", '"health impact" OR "respiratory" OR "cardiovascular" OR "mortality"', 'AND PM2.5 Indonesia'],
      ["Remote sensing", '"satellite" OR "MODIS" OR "Sentinel-5P" OR "remote sensing"', 'AND air quality prediction'],
    ],
    [2200, 5000, 2160]
  ),
  spacer(120),

  h3("2.3 Kriteria Inklusi dan Eksklusi (PRISMA)"),
  spacer(40),
  buildTable(
    ["Kriteria", "Inklusi \u2713", "Eksklusi \u2717"],
    [
      ["Tahun publikasi", "2019–2025", "Sebelum 2015 (kecuali paper seminal)"],
      ["Bahasa", "Inggris, Indonesia", "Bahasa lain tanpa terjemahan"],
      ["Jenis publikasi", "Jurnal Q1–Q3, konferensi terindeks Scopus", "Blog, laporan teknis tidak terindeks"],
      ["Topik", "ML/DL untuk prediksi/klasifikasi AQI, PM2.5", "Polusi air, tanah, noise — tidak relevan"],
      ["Data", "Dataset nyata (real-world)", "Hanya data sintetis"],
      ["Metrik evaluasi", "Menyertakan MSE/RMSE/MAE/R\u00b2 atau akurasi", "Tidak ada evaluasi kuantitatif"],
    ],
    [2400, 3480, 3480]
  ),
  spacer(160),

  // ── BAGIAN 3 ──────────────────────────────────────────
  sectionTag("3", "Sintesis Literatur", BLUE_DARK),
  spacer(80),
  h3("3.1 Tabel Sintesis Paper"),
  para([italic("Isi tabel berikut untuk setiap paper yang Anda baca. Target minimal 20 paper. Tambah baris sesuai kebutuhan.")]),
  spacer(60),
  buildTable(
    ["No", "Penulis & Tahun", "Judul (singkat)", "Metode Utama", "Dataset / Lokasi", "Polutan", "Hasil Terbaik", "Kelebihan", "Kekurangan / Limitasi"],
    [
      ["1", "Zhang et al. (2024)", "[Judul singkat]", "LSTM + Attention", "Beijing, Cina (2019–2022)", "PM2.5", "RMSE: 12.3 \u03bcg/m\u00b3", "Akurasi tinggi", "Tidak ada XAI, tidak ada konteks lokal"],
      ["2", "[Penulis] ([Tahun])", "[Judul singkat]", "[Metode]", "[Dataset & Lokasi]", "[Polutan]", "[Hasil]", "[Kelebihan]", "[Kekurangan]"],
      ["3", "[Penulis] ([Tahun])", "[Judul singkat]", "[Metode]", "[Dataset & Lokasi]", "[Polutan]", "[Hasil]", "[Kelebihan]", "[Kekurangan]"],
      ["4", "[Penulis] ([Tahun])", "[Judul singkat]", "[Metode]", "[Dataset & Lokasi]", "[Polutan]", "[Hasil]", "[Kelebihan]", "[Kekurangan]"],
      ["5", "[Penulis] ([Tahun])", "[Judul singkat]", "[Metode]", "[Dataset & Lokasi]", "[Polutan]", "[Hasil]", "[Kelebihan]", "[Kekurangan]"],
    ],
    [380, 1400, 1800, 1400, 1400, 700, 1200, 1200, 1880]
  ),
  spacer(80),
  callout("Catatan Pengisian", "Kolom 'Kekurangan / Limitasi' adalah yang paling penting — dari sinilah Anda mengidentifikasi GAP penelitian. Catat secara spesifik: apakah modelnya tidak interpretable? Datanya tidak real-time? Tidak ada validasi di Asia Tenggara?", AMBER_LIGHT, AMBER),
  spacer(120),

  h3("3.2 Tren Metode Machine Learning (Ringkasan)"),
  spacer(60),
  buildTable(
    ["Kelompok Metode", "Contoh Algoritma", "Kelebihan Utama", "Kelemahan Umum", "Frekuensi dalam Literatur"],
    [
      ["Classical ML", "Random Forest, XGBoost, SVM, KNN", "Interpretable, efisien", "Kurang tangkap pola temporal", "Sangat tinggi"],
      ["Deep Learning", "LSTM, GRU, BiLSTM", "Pola sekuensial temporal", "Black-box, data intensif", "Tinggi"],
      ["CNN-based", "1D-CNN, CNN-LSTM hybrid", "Pola spasial + temporal", "Kompleks, komputasi berat", "Sedang"],
      ["Transformer", "Attention, BERT-based, Informer", "Long-range dependency", "Resource intensif", "Meningkat (2022–)"],
      ["Explainable AI", "SHAP, LIME, Grad-CAM", "Interpretable, trustworthy", "Overhead komputasi", "Baru berkembang"],
      ["Hybrid", "CNN-LSTM, XGB+LSTM, ensemble", "Tangkap multi-aspek", "Tuning kompleks", "Meningkat"],
    ],
    [2000, 2200, 2000, 2000, 1160]
  ),
  spacer(160),

  // ── BAGIAN 4 ──────────────────────────────────────────
  sectionTag("4", "Gap Analysis", BLUE_DARK),
  spacer(80),
  callout(
    "Definisi GAP Penelitian",
    "Gap adalah ketidakcukupan atau ketidakhadiran dalam literatur yang ada — bisa berupa metode yang belum dicoba, konteks yang belum diteliti, data yang belum digunakan, atau pertanyaan yang belum terjawab. Gap yang baik harus: (1) dapat dibuktikan dari literatur, (2) relevan secara ilmiah, dan (3) dapat diatasi dengan sumber daya yang Anda miliki.",
    BLUE_XLIGHT, BLUE_MED
  ),
  spacer(100),

  h3("4.1 Matriks Gap (Posisi Penelitian Anda)"),
  para([italic("Tabel ini memperlihatkan di mana penelitian Anda mengisi celah yang belum dijangkau studi sebelumnya.")]),
  spacer(60),
  gapMatrix(),
  spacer(80),
  para([italic("Baris terakhir (baris hijau) adalah posisi penelitian Anda. Sesuaikan dengan rencana riset yang akan Anda lakukan.")]),
  spacer(120),

  h3("4.2 Identifikasi Gap Spesifik"),
  spacer(60),
  buildTable(
    ["No", "Jenis Gap", "Deskripsi Gap", "Bukti dari Literatur", "Relevansi untuk Penelitian Anda", "Prioritas"],
    [
      ["G1", "Gap Geografis / Kontekstual", "Mayoritas studi prediksi AQI dilakukan di Cina, India, atau Eropa. Hampir tidak ada studi yang secara khusus menganalisis AQI berbasis ML di Jawa Barat / Bandung.", '"Only a few studies have been conducted in Southeast Asian cities..." (Smith et al., 2023)', "Sangat relevan — penelitian Anda dapat menjadi studi pionir di konteks Bandung.", "TINGGI"],
      ["G2", "Gap Metode (Explainability)", 'Sebagian besar model prediksi AQI masih bersifat "black-box". Studi yang mengintegrasikan XAI (SHAP/LIME) untuk interpretasi model AQI di negara berkembang masih sangat sedikit.', '"Few studies address model interpretability in AQI prediction..." (Ali et al., 2023)', "Mengintegrasikan SHAP/LIME ke model Anda akan menjadi kontribusi metodologis yang kuat.", "TINGGI"],
      ["G3", "Gap Data (Low-cost Sensor)", "Banyak studi menggunakan stasiun pemantauan resmi yang mahal dan terbatas distribusinya. Penggunaan dan kalibrasi low-cost sensor (PurpleAir, dll.) di Indonesia belum banyak diteliti.", '"Low-cost sensor calibration in tropical environments remains understudied..." (2024)', "Menggunakan dan mengkalibrasi low-cost sensor akan membuka opsi data yang lebih kaya.", "SEDANG"],
      ["G4", "Gap Integrasi Data", "Sangat sedikit studi yang mengintegrasikan data polutan, meteorologi, data satelit, DAN data mobilitas kendaraan secara bersamaan untuk prediksi AQI.", '"Multi-source data fusion for AQI is still limited..." (Kumar, 2024)', "Integrasi multi-sumber dapat meningkatkan akurasi model secara signifikan.", "SEDANG"],
      ["G5", "Gap Temporal (Real-time)", "Sebagian besar model berfokus pada prediksi harian atau jam-jaman, tetapi prediksi real-time dengan latensi rendah untuk peringatan dini masih jarang.", '"Real-time AQI warning systems based on ML are scarce..." (2023)', "Sistem early-warning berbasis ML berpotensi sebagai kontribusi aplikatif.", "RENDAH-SEDANG"],
    ],
    [380, 1600, 2800, 2000, 1580, 1000]
  ),
  spacer(120),

  h3("4.3 Novelty / Kebaruan Penelitian Anda"),
  callout(
    "Formulasikan kebaruan Anda di sini",
    "Penelitian ini memberikan kontribusi baru berupa:\n[1] Studi pertama yang membandingkan kinerja algoritma ML/DL untuk prediksi AQI secara khusus di wilayah Bandung, Jawa Barat.\n[2] Integrasi pendekatan Explainable AI (SHAP) untuk mengidentifikasi faktor dominan polutan di konteks iklim tropis Indonesia.\n[3] Pemanfaatan data low-cost sensor yang dikalibrasi bersama data stasiun resmi untuk meningkatkan densitas spasial data pelatihan.",
    GREEN_LIGHT, GREEN_DARK
  ),
  spacer(160),

  // ── BAGIAN 5 ──────────────────────────────────────────
  sectionTag("5", "Kerangka Konseptual & Posisi Penelitian", TEAL),
  spacer(80),
  h3("5.1 Peta Tema Literatur"),
  para([italic("Gambarkan atau deskripsikan peta tema (concept map) dari literatur yang Anda baca. Anda dapat menyisipkan gambar di sini.")]),
  spacer(80),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 120 },
    border: { top: border(GRAY_LIGHT, 4), bottom: border(GRAY_LIGHT, 4), left: border(GRAY_LIGHT, 4), right: border(GRAY_LIGHT, 4) },
    children: [run("[Sisipkan concept map / diagram tema di sini — contoh: XMind, VOSviewer, atau Connected Papers]", { italics: true, size: 18, color: GRAY_MED })]
  }),
  spacer(80),
  h3("5.2 Kerangka Teoritis Penelitian"),
  buildTable(
    ["Komponen", "Deskripsi", "Sumber / Referensi"],
    [
      ["Input Data", "[Variabel input: PM2.5, PM10, NO\u2082, CO, suhu, kelembaban, kecepatan angin, dll.]", "[Sesuaikan dengan dataset Anda]"],
      ["Preprocessing", "[Normalisasi, imputasi missing values, feature engineering]", "[Literatur metodologi]"],
      ["Model ML/DL", "[Arsitektur utama yang akan digunakan: LSTM, XGBoost, CNN, hybrid, dll.]", "[Paper benchmark]"],
      ["Explainability", "[SHAP / LIME / Grad-CAM untuk interpretasi]", "[Lundberg & Lee, 2017]"],
      ["Output", "[Prediksi AQI kategori / nilai numerik]", "[Standar ISPU/AQI]"],
      ["Evaluasi", "[RMSE, MAE, R\u00b2, akurasi klasifikasi]", "[Standar metrik ML]"],
    ],
    [2200, 4500, 2660]
  ),
  spacer(160),

  // ── BAGIAN 6 ──────────────────────────────────────────
  sectionTag("6", "Sintesis Temuan & Implikasi", BLUE_DARK),
  spacer(80),
  h3("6.1 Temuan Utama dari Literatur"),
  para([normal("Tulis ringkasan naratif dari apa yang Anda pelajari dari literatur. Jawab pertanyaan berikut:")]),
  bullet("Metode apa yang paling sering digunakan dan mengapa?"),
  bullet("Dataset apa yang paling umum dan apa kekurangannya?"),
  bullet("Apa yang menjadi tantangan utama dalam riset prediksi AQI?"),
  bullet("Bagaimana tren penelitian berkembang dari 2019 hingga 2025?"),
  spacer(80),
  callout(
    "Tulis sintesis narasi Anda di sini",
    "Berdasarkan kajian terhadap [N] paper, ditemukan bahwa... [Tuliskan 2–3 paragraf narasi sintesis berdasarkan bacaan Anda]",
    BLUE_XLIGHT, BLUE_MED
  ),
  spacer(100),

  h3("6.2 Implikasi untuk Penelitian Anda"),
  buildTable(
    ["Temuan dari Literatur", "Implikasi untuk Desain Penelitian Anda"],
    [
      ["Random Forest dan XGBoost dominan di klasifikasi AQI dengan akurasi tinggi", "Jadikan RF dan XGBoost sebagai baseline; bandingkan dengan LSTM sebagai model deep learning"],
      ["Kalibrasi sensor penting untuk akurasi data PM2.5 di lapangan", "Lakukan co-location study antara low-cost sensor dengan alat standar sebelum training"],
      ["Variabel meteorologi (angin, kelembaban) sangat berpengaruh terhadap AQI", "Sertakan minimal 5 variabel meteorologi dalam feature set"],
      ["Studi Asia Tenggara sangat langka dalam literatur global", "Manfaatkan ini sebagai positioning paper — kontribusi regional yang kuat"],
      ["XAI meningkatkan kepercayaan model di kalangan pembuat kebijakan", "Integrasikan SHAP values sebagai bagian dari analisis hasil"],
    ],
    [4200, 5160]
  ),
  spacer(160),

  // ── BAGIAN 7 ──────────────────────────────────────────
  sectionTag("7", "Rencana Lanjutan & Checklist", TEAL),
  spacer(80),
  h3("7.1 Rencana Lanjutan Pencarian Literatur"),
  buildTable(
    ["Minggu", "Target Aktivitas", "Jurnal / Database Target", "Status"],
    [
      ["Minggu 1–2", "Cari paper dengan keyword utama, baca abstract, pilih 30 paper relevan", "Scopus, WoS, Google Scholar", "[ ] Selesai"],
      ["Minggu 3–4", "Full-text reading 20 paper terpilih, isi tabel sintesis (Bagian 3)", "ScienceDirect, IEEE Xplore", "[ ] Selesai"],
      ["Minggu 5", "Identifikasi gap dan formulasikan novelty", "Semua database", "[ ] Selesai"],
      ["Minggu 6", "Tulis narasi literature review (draft)", "—", "[ ] Selesai"],
      ["Minggu 7", "Revisi, tambah referensi, finalisasi kerangka konseptual", "—", "[ ] Selesai"],
      ["Minggu 8", "Konsultasi dengan pembimbing, revisi akhir", "—", "[ ] Selesai"],
    ],
    [1400, 3400, 2800, 1560]
  ),
  spacer(100),

  h3("7.2 Checklist Kelengkapan Literature Review"),
  spacer(40),
  callout(
    "Centang semua poin berikut sebelum menyerahkan ke pembimbing",
    "[ ] Minimal 20 paper sudah dibaca dan dimasukkan ke tabel sintesis\n[ ] Keyword search terdokumentasi dengan jelas\n[ ] Gap analysis dengan minimal 3 gap yang dibuktikan dari literatur\n[ ] Novelty / kebaruan penelitian sudah dirumuskan dengan spesifik\n[ ] Semua referensi mengikuti format sitasi yang konsisten (APA/IEEE)\n[ ] Tidak ada paper sebelum 2015 kecuali paper seminal/foundational\n[ ] Matriks gap sudah diisi dengan posisi penelitian Anda\n[ ] Draft narasi sudah ditulis (minimal 1.500 kata)",
    GREEN_LIGHT, GREEN_DARK
  ),
  spacer(160),

  // ── DAFTAR PUSTAKA ────────────────────────────────────
  sectionTag("R", "Daftar Pustaka (References)", GRAY_DARK),
  spacer(80),
  callout(
    "Format referensi",
    "Gunakan format APA 7th Edition atau IEEE sesuai kebijakan institusi Anda. Contoh APA:\nZhang, X., Liu, Y., & Wang, J. (2024). Deep learning approaches for PM2.5 prediction in urban areas. Atmospheric Environment, 285, 119–134. https://doi.org/10.1016/xxxx\n\nGunakan tools: Zotero (gratis), Mendeley, atau Endnote untuk manajemen referensi otomatis.",
    BLUE_XLIGHT, BLUE_MED
  ),
  spacer(80),
  para([normal("1. [Penulis, A., & Penulis, B. (Tahun). Judul artikel. Nama Jurnal, volume(nomor), halaman. DOI]", 20, GRAY_MED)]),
  para([normal("2. [Penulis, A. (Tahun). Judul artikel. Nama Jurnal, volume(nomor), halaman. DOI]", 20, GRAY_MED)]),
  para([normal("3. [Tambahkan referensi sesuai paper yang Anda baca...]", 20, GRAY_MED)]),
  spacer(200),
];

// ─── ASSEMBLE DOCUMENT ────────────────────────────────────
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } }, run: { font: "Arial", size: 20 } } },
          { level: 1, format: LevelFormat.BULLET, text: "\u25e6", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 1080, hanging: 360 } }, run: { font: "Arial", size: 20 } } },
        ]
      },
      {
        reference: "numbers",
        levels: [
          { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
            style: { paragraph: { indent: { left: 720, hanging: 360 } }, run: { font: "Arial", size: 20 } } },
        ]
      },
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 20, color: GRAY_DARK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, font: "Arial", color: WHITE },
        paragraph: { spacing: { before: 240, after: 0 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial", color: WHITE },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 22, bold: true, font: "Arial", color: BLUE_DARK },
        paragraph: { spacing: { before: 200, after: 80 }, outlineLevel: 2 } },
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1134, right: 1134, bottom: 1134, left: 1134 }
      }
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            children: [
              run("Template Literature Review & Gap Analysis \u2014 Kualitas Udara & Data Science", { size: 16, color: GRAY_MED, italics: true }),
              run("  |  ", { size: 16, color: GRAY_LIGHT }),
              run("[Nama Peneliti] \u2014 [Tahun]", { size: 16, color: GRAY_MED }),
            ],
            border: { bottom: border(BLUE_MED, 4) },
            spacing: { after: 0 }
          })
        ]
      })
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            children: [
              run("Halaman ", { size: 16, color: GRAY_MED }),
              new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: GRAY_MED }),
              run(" dari ", { size: 16, color: GRAY_MED }),
              new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: GRAY_MED }),
              run("   |   Template oleh: Pembimbing Peneliti \u2014 Dibuat dengan Panduan Data Science", { size: 16, color: GRAY_MED, italics: true }),
            ],
            alignment: AlignmentType.CENTER,
            border: { top: border(BLUE_LIGHT, 4) },
            spacing: { before: 0 }
          })
        ]
      })
    },
    children: [
      ...coverPage(),
      ...body,
    ]
  }]
});

// ─── OUTPUT ───────────────────────────────────────────────
const outputPath = path.join(__dirname, "Template_LitReview_GapAnalysis_AirQuality.docx");

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log("✅ Berhasil dibuat: " + outputPath);
}).catch(err => {
  console.error("❌ Error:", err.message);
});
