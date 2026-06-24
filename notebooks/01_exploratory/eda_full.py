"""
=============================================================
FASE 1: EXPLORATORY DATA ANALYSIS (EDA)
Prediksi PM2.5 di Cekungan Bandung (LSTM + SHAP)
Kerja Praktik - BRIN 2026
=============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Konfigurasi Plotting
# ============================================================
plt.rcParams.update({
    'figure.figsize': (14, 6),
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'figure.dpi': 120,
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
})

OUTPUT_DIR = r'D:\Kuliah Praktik\KP BRIN\reports\eda_plots'
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
# 1. LOAD DATA
# ============================================================
print("=" * 60)
print("FASE 1: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ERA5
era5 = pd.read_csv(r'D:\Kuliah Praktik\KP BRIN\data\raw\era5_bandung_2022_2026.csv')
era5['waktu'] = pd.to_datetime(era5['waktu'])
era5 = era5.drop(columns=['number'])  # kolom konstan 0, tidak berguna
era5 = era5.set_index('waktu')

# Sensor PM2.5
sensor = pd.read_csv(r'D:\Kuliah Praktik\KP BRIN\data\raw\hourly_all_sensors.csv')
sensor['datetime'] = pd.to_datetime(sensor['datetime'], utc=True)
sensor['datetime'] = sensor['datetime'].dt.tz_convert('Asia/Jakarta')

print(f"\n[1] ERA5 Data:")
print(f"    Shape     : {era5.shape}")
print(f"    Periode   : {era5.index.min()} → {era5.index.max()}")
print(f"    Missing   : {era5.isnull().sum().sum()} (NOLADA!)")
print(f"    Variabel  : {list(era5.columns)}")

print(f"\n[2] Sensor PM2.5 Data:")
print(f"    Shape     : {sensor.shape}")
print(f"    Periode   : {sensor['datetime'].min()} → {sensor['datetime'].max()}")
print(f"    Sensor ID : {sensor['sensor_id'].unique()}")
print(f"    Missing   : humidity={sensor['humidity'].isnull().sum()}, "
      f"temperature={sensor['temperature'].isnull().sum()}, "
      f"pm2.5_alt={sensor['pm2.5_alt'].isnull().sum()}")

# ============================================================
# 2. EDA SENSOR PM2.5 — PERBANDINGAN DUA SENSOR
# ============================================================
print("\n" + "=" * 60)
print("EDA 1: PERBANDINGAN DUA SENSOR PM2.5")
print("=" * 60)

sensor_121867 = sensor[sensor['sensor_id'] == 121867].copy()
sensor_238875 = sensor[sensor['sensor_id'] == 238875].copy()

print(f"\nSensor 121867: {len(sensor_121867)} data points")
print(f"  PM2.5 (alt) — Mean: {sensor_121867['pm2.5_alt'].mean():.2f}, "
      f"Median: {sensor_121867['pm2.5_alt'].median():.2f}, "
      f"Max: {sensor_121867['pm2.5_alt'].max():.2f}")

print(f"\nSensor 238875: {len(sensor_238875)} data points")
print(f"  PM2.5 (alt) — Mean: {sensor_238875['pm2.5_alt'].mean():.2f}, "
      f"Median: {sensor_238875['pm2.5_alt'].median():.2f}, "
      f"Max: {sensor_238875['pm2.5_alt'].max():.2f}")

# Plot perbandingan dua sensor
fig, axes = plt.subplots(2, 1, figsize=(16, 8), sharex=True)
fig.suptitle('Perbandingan Time-Series PM2.5 Dua Sensor di Bandung', fontsize=16, fontweight='bold')

axes[0].plot(sensor_121867['datetime'], sensor_121867['pm2.5_alt'], 
             color='#066CF4', linewidth=0.5, alpha=0.7)
axes[0].set_ylabel('PM2.5 (µg/m³)')
axes[0].set_title('Sensor 121867 (Utama)')
axes[0].axhline(y=15, color='orange', linestyle='--', linewidth=1.5, label='Batas WHO (15 µg/m³)')
axes[0].axhline(y=55, color='red', linestyle='--', linewidth=1.5, label='Batas KLHK (55 µg/m³)')
axes[0].legend(loc='upper right')
axes[0].set_ylim(0, max(200, sensor_121867['pm2.5_alt'].quantile(0.99)*1.2))

axes[1].plot(sensor_238875['datetime'], sensor_238875['pm2.5_alt'],
             color='#FF6B35', linewidth=0.5, alpha=0.7)
axes[1].set_ylabel('PM2.5 (µg/m³)')
axes[1].set_title('Sensor 238875 (Pembanding)')
axes[1].axhline(y=15, color='orange', linestyle='--', linewidth=1.5, label='Batas WHO (15 µg/m³)')
axes[1].axhline(y=55, color='red', linestyle='--', linewidth=1.5, label='Batas KLHK (55 µg/m³)')
axes[1].legend(loc='upper right')
axes[1].set_ylim(0, max(200, sensor_238875['pm2.5_alt'].quantile(0.99)*1.2))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '01_perbandingan_dua_sensor.png'))
plt.close()
print("\n✅ Plot disimpan: 01_perbandingan_dua_sensor.png")

# ============================================================
# 3. FILTER SENSOR UTAMA (121867) & DETEKSI ANOMALI
# ============================================================
print("\n" + "=" * 60)
print("EDA 2: ANALISIS SENSOR UTAMA (121867)")
print("=" * 60)

# Gunakan sensor utama
pm25 = sensor_121867[['datetime', 'pm2.5_alt', 'humidity', 'temperature', 'pressure']].copy()
pm25 = pm25.rename(columns={'pm2.5_alt': 'pm25'})
pm25 = pm25.set_index('datetime')
pm25.index = pm25.index.tz_localize(None)  # hapus timezone info agar bisa merge

# Deteksi anomali / outlier
Q1 = pm25['pm25'].quantile(0.25)
Q3 = pm25['pm25'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = max(0, Q1 - 1.5 * IQR)
upper_bound = Q3 + 1.5 * IQR
outliers = pm25[(pm25['pm25'] < lower_bound) | (pm25['pm25'] > upper_bound)]

print(f"\nSensor 121867 — Statistik Deskriptif:")
print(f"  Q1       : {Q1:.2f}")
print(f"  Q3       : {Q3:.2f}")
print(f"  IQR      : {IQR:.2f}")
print(f"  Batas atas: {upper_bound:.2f}")
print(f"  Outlier  : {len(outliers)} data points ({len(outliers)/len(pm25)*100:.1f}%)")

# Cek data bermasalah (temperature > 200 dll)
temp_anomaly = pm25[pm25['temperature'] > 100]
pressure_anomaly = pm25[pm25['pressure'] < 0]
print(f"\n⚠️  Anomali Suhu (>100°F) : {len(temp_anomaly)} data points")
print(f"⚠️  Anomali Tekanan (<0)  : {len(pressure_anomaly)} data points")

# ============================================================
# 4. EDA ERA5 — DISTRIBUSI 11 VARIABEL METEOROLOGI
# ============================================================
print("\n" + "=" * 60)
print("EDA 3: DISTRIBUSI VARIABEL ERA5")
print("=" * 60)

era5_vars = [
    'tinggi_lapisan_batas_m', 'ozon_kolom_kg_m2', 'uap_air_kolom_kg_m2',
    'tutupan_awan_01', 'suhu_2m_C', 'titik_embun_C',
    'tekanan_hPa', 'curah_hujan_mm', 'kecepatan_angin_kmh',
    'arah_angin_derajat', 'kelembapan_persen'
]

fig, axes = plt.subplots(3, 4, figsize=(20, 12))
fig.suptitle('Distribusi 11 Variabel Meteorologi ERA5 — Bandung (2022-2026)', 
             fontsize=16, fontweight='bold')

for i, var in enumerate(era5_vars):
    ax = axes[i // 4, i % 4]
    era5[var].hist(bins=50, ax=ax, color='#066CF4', alpha=0.7, edgecolor='white')
    ax.set_title(var.replace('_', ' ').title(), fontsize=10)
    ax.tick_params(labelsize=8)

# Hapus subplot kosong (posisi 3,3)
axes[2, 3].axis('off')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '02_distribusi_era5.png'))
plt.close()
print("✅ Plot disimpan: 02_distribusi_era5.png")

# ============================================================
# 5. TIME-SERIES ERA5 — VARIABEL KUNCI
# ============================================================
key_vars = ['suhu_2m_C', 'kelembapan_persen', 'curah_hujan_mm', 
            'kecepatan_angin_kmh', 'tinggi_lapisan_batas_m', 'tutupan_awan_01']

fig, axes = plt.subplots(len(key_vars), 1, figsize=(16, 18), sharex=True)
fig.suptitle('Time-Series 6 Variabel Kunci ERA5 — Bandung (2022-2026)', 
             fontsize=16, fontweight='bold')

colors = ['#E63946', '#457B9D', '#2A9D8F', '#E9C46A', '#F4A261', '#264653']

for i, var in enumerate(key_vars):
    # Resample harian untuk visualisasi yang lebih bersih
    daily = era5[var].resample('D').mean()
    axes[i].plot(daily.index, daily.values, color=colors[i], linewidth=0.8, alpha=0.8)
    axes[i].set_ylabel(var.replace('_', '\n'), fontsize=9)
    axes[i].grid(True, alpha=0.3)
    
    # Tandai musim kemarau (Jun-Sep)
    for year in range(2022, 2027):
        try:
            start = pd.Timestamp(f'{year}-06-01')
            end = pd.Timestamp(f'{year}-09-30')
            axes[i].axvspan(start, end, alpha=0.1, color='orange', label='Kemarau' if year==2022 else '')
        except:
            pass

axes[0].legend(loc='upper right')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '03_timeseries_era5_kunci.png'))
plt.close()
print("✅ Plot disimpan: 03_timeseries_era5_kunci.png")

# ============================================================
# 6. POLA DIURNAL PM2.5 (JAM PER JAM)
# ============================================================
print("\n" + "=" * 60)
print("EDA 4: POLA DIURNAL PM2.5 (PER JAM)")
print("=" * 60)

pm25_clean = pm25[pm25['pm25'] < upper_bound].copy()  # tanpa outlier
pm25_clean['hour'] = pm25_clean.index.hour

hourly_stats = pm25_clean.groupby('hour')['pm25'].agg(['mean', 'median', 'std'])

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(hourly_stats.index, hourly_stats['mean'], color='#066CF4', alpha=0.7, label='Rata-rata')
ax.plot(hourly_stats.index, hourly_stats['median'], color='#FF6B35', linewidth=2.5, 
        marker='o', markersize=6, label='Median')
ax.axhline(y=15, color='red', linestyle='--', linewidth=1.5, label='Batas WHO (15 µg/m³)')
ax.axvspan(6, 8, alpha=0.15, color='red', label='Jam Sibuk Pagi')
ax.axvspan(18, 23, alpha=0.15, color='orange', label='Jam Sibuk Malam')
ax.set_xlabel('Jam (WIB)')
ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
ax.set_title('Pola Diurnal PM2.5 di Bandung — Sensor 121867', fontweight='bold')
ax.set_xticks(range(24))
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '04_pola_diurnal_pm25.png'))
plt.close()

print(f"\nJam dengan PM2.5 tertinggi : {hourly_stats['mean'].idxmax()}:00 "
      f"({hourly_stats['mean'].max():.2f} µg/m³)")
print(f"Jam dengan PM2.5 terendah  : {hourly_stats['mean'].idxmin()}:00 "
      f"({hourly_stats['mean'].min():.2f} µg/m³)")
print("✅ Plot disimpan: 04_pola_diurnal_pm25.png")

# ============================================================
# 7. POLA MUSIMAN PM2.5 (BULANAN)
# ============================================================
print("\n" + "=" * 60)
print("EDA 5: POLA MUSIMAN PM2.5 (PER BULAN)")
print("=" * 60)

pm25_clean['month'] = pm25_clean.index.month
monthly_stats = pm25_clean.groupby('month')['pm25'].agg(['mean', 'median', 'std'])

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun',
               'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(monthly_stats.index, monthly_stats['mean'], color='#066CF4', alpha=0.7)

# Warnai musim kemarau berbeda
for i, bar in enumerate(bars):
    if monthly_stats.index[i] in [6, 7, 8, 9]:  # Jun-Sep = Kemarau
        bar.set_color('#E63946')
        bar.set_alpha(0.8)

ax.axhline(y=15, color='red', linestyle='--', linewidth=1.5, label='Batas WHO (15 µg/m³)')
ax.set_xlabel('Bulan')
ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
ax.set_title('Pola Musiman PM2.5 — Kemarau vs Hujan di Bandung', fontweight='bold')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(month_names)
ax.legend()
ax.grid(True, alpha=0.3)

# Anotasi
ax.annotate('Musim Kemarau\n(Jun-Sep)', 
            xy=(7.5, monthly_stats.loc[6:9, 'mean'].max()),
            xytext=(10, monthly_stats['mean'].max() * 1.1),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=11, color='red', fontweight='bold')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '05_pola_musiman_pm25.png'))
plt.close()

kemarau_mean = pm25_clean[pm25_clean['month'].isin([6,7,8,9])]['pm25'].mean()
hujan_mean = pm25_clean[pm25_clean['month'].isin([12,1,2,3])]['pm25'].mean()
print(f"\nRata-rata PM2.5 Musim Kemarau (Jun-Sep)  : {kemarau_mean:.2f} µg/m³")
print(f"Rata-rata PM2.5 Musim Hujan (Des-Mar)     : {hujan_mean:.2f} µg/m³")
print(f"Peningkatan saat Kemarau                  : {((kemarau_mean/hujan_mean)-1)*100:.1f}%")
print("✅ Plot disimpan: 05_pola_musiman_pm25.png")

# ============================================================
# 8. KORELASI ERA5 vs PM2.5 (Overlap Periode)
# ============================================================
print("\n" + "=" * 60)
print("EDA 6: KORELASI ERA5 vs PM2.5")
print("=" * 60)

# Merge pada timestamp yang overlap
merged = pm25_clean[['pm25']].join(era5, how='inner')
print(f"\nData yang overlap (merged): {len(merged)} baris")
print(f"Periode overlap: {merged.index.min()} → {merged.index.max()}")

# Hitung korelasi
corr = merged.corr()['pm25'].drop('pm25').sort_values(ascending=False)
print(f"\nKorelasi setiap variabel ERA5 terhadap PM2.5:")
for var, val in corr.items():
    direction = "↑" if val > 0 else "↓"
    strength = "KUAT" if abs(val) > 0.3 else "SEDANG" if abs(val) > 0.15 else "LEMAH"
    print(f"  {direction} {var:30s}: {val:+.4f} ({strength})")

# Plot Heatmap Korelasi
fig, ax = plt.subplots(figsize=(12, 10))
corr_matrix = merged.corr()

# Manual heatmap
im = ax.imshow(corr_matrix.values, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_yticks(range(len(corr_matrix.columns)))

short_labels = [c.replace('_', '\n')[:20] for c in corr_matrix.columns]
ax.set_xticklabels(short_labels, rotation=45, ha='right', fontsize=8)
ax.set_yticklabels(short_labels, fontsize=8)

# Annotate values
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        val = corr_matrix.iloc[i, j]
        color = 'white' if abs(val) > 0.5 else 'black'
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', fontsize=7, color=color)

plt.colorbar(im, ax=ax, label='Koefisien Korelasi Pearson')
ax.set_title('Matriks Korelasi: PM2.5 vs Variabel Meteorologi ERA5', fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '06_korelasi_heatmap.png'))
plt.close()
print("\n✅ Plot disimpan: 06_korelasi_heatmap.png")

# ============================================================
# 9. SCATTER PLOT VARIABEL TERPENTING vs PM2.5
# ============================================================
top_vars = corr.head(3).index.tolist() + corr.tail(3).index.tolist()
# Ambil 6 variabel teratas (3 positif + 3 negatif)

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Scatter Plot: Top-6 Variabel ERA5 vs PM2.5', fontsize=16, fontweight='bold')

for i, var in enumerate(top_vars):
    ax = axes[i // 3, i % 3]
    r = merged[var].corr(merged['pm25'])
    ax.scatter(merged[var], merged['pm25'], alpha=0.1, s=5, color='#066CF4')
    ax.set_xlabel(var.replace('_', ' '))
    ax.set_ylabel('PM2.5 (µg/m³)')
    ax.set_title(f'r = {r:.3f}', fontsize=11)
    ax.grid(True, alpha=0.3)

    # Trend line
    z = np.polyfit(merged[var].dropna(), merged.loc[merged[var].dropna().index, 'pm25'], 1)
    p = np.poly1d(z)
    x_range = np.linspace(merged[var].min(), merged[var].max(), 100)
    ax.plot(x_range, p(x_range), color='red', linewidth=2, linestyle='--')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '07_scatter_top6_era5_vs_pm25.png'))
plt.close()
print("✅ Plot disimpan: 07_scatter_top6_era5_vs_pm25.png")

# ============================================================
# 10. RINGKASAN AKHIR EDA
# ============================================================
print("\n" + "=" * 60)
print("📊 RINGKASAN HASIL EDA")
print("=" * 60)

print(f"""
┌─────────────────────────────────────────────────────────────┐
│                    DATA ERA5                                │
├─────────────────────────────────────────────────────────────┤
│  Total data       : {era5.shape[0]:,} baris (per jam)             │
│  Variabel         : {len(era5_vars)} variabel cuaca                     │
│  Periode          : Jan 2022 — Mei 2026                     │
│  Missing values   : 0 (SEMPURNA!)                           │
├─────────────────────────────────────────────────────────────┤
│                    DATA SENSOR PM2.5                         │
├─────────────────────────────────────────────────────────────┤
│  Sensor utama     : 121867 ({len(sensor_121867):,} data points)         │
│  Sensor cadangan  : 238875 ({len(sensor_238875):,} data points)          │
│  Periode          : Nov 2022 — Mei 2026                     │
│  Missing humidity : {sensor_121867['humidity'].isnull().sum():,} baris                          │
│  Outlier PM2.5    : {len(outliers):,} baris ({len(outliers)/len(pm25)*100:.1f}%)                     │
├─────────────────────────────────────────────────────────────┤
│                    DATA OVERLAP (MERGED)                     │
├─────────────────────────────────────────────────────────────┤
│  Total merged     : {len(merged):,} baris (siap dimodelkan)       │
│  Periode overlap  : {str(merged.index.min())[:10]} → {str(merged.index.max())[:10]}             │
├─────────────────────────────────────────────────────────────┤
│                    TEMUAN KUNCI                              │
├─────────────────────────────────────────────────────────────┤
│  PM2.5 rata-rata  : {pm25_clean['pm25'].mean():.2f} µg/m³ (> WHO 15 µg/m³!)     │
│  PM2.5 kemarau    : {kemarau_mean:.2f} µg/m³                           │
│  PM2.5 hujan      : {hujan_mean:.2f} µg/m³                           │
│  Jam puncak       : {hourly_stats['mean'].idxmax()}:00 WIB                              │
│  Korelasi terkuat : {corr.index[0][:28]:28s} (r={corr.iloc[0]:+.3f}) │
│  Korelasi terlemah: {corr.index[-1][:28]:28s} (r={corr.iloc[-1]:+.3f}) │
└─────────────────────────────────────────────────────────────┘
""")

print(f"\n🎯 KEPUTUSAN UNTUK FASE SELANJUTNYA:")
print(f"   1. Gunakan HANYA sensor 121867 (data lebih lengkap & stabil)")
print(f"   2. ERA5 tidak memiliki missing values → siap digunakan langsung")
print(f"   3. Data overlap {len(merged):,} baris sudah cukup untuk pelatihan LSTM")
print(f"   4. Perlu imputasi/interpolasi untuk {sensor_121867['humidity'].isnull().sum()} baris missing di sensor lokal")
print(f"\n📁 Semua plot telah disimpan di: {OUTPUT_DIR}")
print("=" * 60)
