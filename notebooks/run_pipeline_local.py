"""
Script untuk menjalankan seluruh pipeline prediksi PM2.5 secara lokal.
Tahapan:
  1. Preprocessing & Feature Engineering
  2. Baseline Models (RF & XGBoost + GridSearch)
  3. Deep Learning (LSTM & BiLSTM + Tuning) — dikurangi kombinasi untuk CPU
  4. Evaluasi & Visualisasi
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import os
import time
import joblib
import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(PROJECT_DIR, 'data', 'raw')
DATA_PROC = os.path.join(PROJECT_DIR, 'data', 'processed')
MODEL_DIR = os.path.join(PROJECT_DIR, 'models')
FIG_DIR = os.path.join(PROJECT_DIR, 'reports', 'figures')

os.makedirs(DATA_PROC, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# FASE 1: PREPROCESSING & FEATURE ENGINEERING
# ============================================================
print("=" * 65)
print("FASE 1: PREPROCESSING & FEATURE ENGINEERING")
print("=" * 65)

data_path = os.path.join(DATA_RAW, 'merged_pm25_era5v3.csv')
df = pd.read_csv(data_path, index_col=0, parse_dates=True)
print(f"Data loaded: {df.shape} | Periode: {df.index.min()} -> {df.index.max()}")

# 1a. Missing values
missing_pct = (df.isnull().sum() / len(df) * 100)
print(f"\nMissing values sebelum imputasi:")
print(missing_pct[missing_pct > 0])
df = df.interpolate(method='time').ffill().bfill()
print(f"Missing setelah imputasi: {df.isnull().sum().sum()}")

# 1b. Outlier handling (IQR Clipping)
print("\n--- Outlier Handling (IQR Clipping) ---")
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
for col in numeric_cols:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    n_out = ((df[col] < lower) | (df[col] > upper)).sum()
    if n_out > 0:
        df[col] = df[col].clip(lower=lower, upper=upper)
        print(f"  {col}: {n_out} outlier di-clip")

# 1c. Feature Engineering
print("\n--- Feature Engineering ---")
# Lag features
df['pm25_lag_1h'] = df['pm25'].shift(1)
df['pm25_lag_24h'] = df['pm25'].shift(24)

# Cyclical time features
df['hour_sin'] = np.sin(2 * np.pi * df.index.hour / 24)
df['hour_cos'] = np.cos(2 * np.pi * df.index.hour / 24)
df['month_sin'] = np.sin(2 * np.pi * df.index.month / 12)
df['month_cos'] = np.cos(2 * np.pi * df.index.month / 12)
df['dow_sin'] = np.sin(2 * np.pi * df.index.dayofweek / 7)
df['dow_cos'] = np.cos(2 * np.pi * df.index.dayofweek / 7)

# Musim kemarau
df['is_dry_season'] = df.index.month.isin([6, 7, 8, 9]).astype(int)

df = df.dropna()
print(f"Shape akhir: {df.shape}")
print(f"Fitur: {list(df.columns)}")

# 1d. Train/Val/Test Split (70/10/20 kronologis)
n = len(df)
train_end = int(n * 0.7)
val_end = int(n * 0.8)

train_df = df.iloc[:train_end]
val_df = df.iloc[train_end:val_end]
test_df = df.iloc[val_end:]
print(f"\nSplit kronologis:")
print(f"  Train : {train_df.shape} | {train_df.index[0]} -> {train_df.index[-1]}")
print(f"  Val   : {val_df.shape}  | {val_df.index[0]} -> {val_df.index[-1]}")
print(f"  Test  : {test_df.shape} | {test_df.index[0]} -> {test_df.index[-1]}")

# 1e. Scaling
target_col = 'pm25'
feature_cols = [c for c in df.columns if c != target_col]

scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

train_X_s = pd.DataFrame(scaler_X.fit_transform(train_df[feature_cols]), columns=feature_cols, index=train_df.index)
val_X_s = pd.DataFrame(scaler_X.transform(val_df[feature_cols]), columns=feature_cols, index=val_df.index)
test_X_s = pd.DataFrame(scaler_X.transform(test_df[feature_cols]), columns=feature_cols, index=test_df.index)

train_y_s = scaler_y.fit_transform(train_df[[target_col]])
val_y_s = scaler_y.transform(val_df[[target_col]])
test_y_s = scaler_y.transform(test_df[[target_col]])

# Gabung kembali untuk simpan
train_scaled = train_X_s.copy(); train_scaled[target_col] = train_y_s
val_scaled = val_X_s.copy(); val_scaled[target_col] = val_y_s
test_scaled = test_X_s.copy(); test_scaled[target_col] = test_y_s

train_scaled.to_csv(os.path.join(DATA_PROC, 'train_scaled.csv'))
val_scaled.to_csv(os.path.join(DATA_PROC, 'val_scaled.csv'))
test_scaled.to_csv(os.path.join(DATA_PROC, 'test_scaled.csv'))
joblib.dump(scaler_X, os.path.join(DATA_PROC, 'scaler_X.pkl'))
joblib.dump(scaler_y, os.path.join(DATA_PROC, 'scaler_y.pkl'))
print("\n[OK] Data processed disimpan.")

# Siapkan array untuk ML
X_train = train_X_s.values; y_train = train_y_s.flatten()
X_val = val_X_s.values; y_val = val_y_s.flatten()
X_test = test_X_s.values; y_test = test_y_s.flatten()

# ============================================================
# FASE 2: BASELINE MODELS (RF & XGBoost + GridSearch)
# ============================================================
print("\n" + "=" * 65)
print("FASE 2: BASELINE MODELS")
print("=" * 65)

def evaluate_model(name, y_true_s, y_pred_s):
    y_true = scaler_y.inverse_transform(y_true_s.reshape(-1, 1)).flatten()
    y_pred = scaler_y.inverse_transform(y_pred_s.reshape(-1, 1)).flatten()
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"  {name}: RMSE={rmse:.4f} | MAE={mae:.4f} | R²={r2:.4f}")
    return {'name': name, 'rmse': rmse, 'mae': mae, 'r2': r2, 'y_true': y_true, 'y_pred': y_pred}

# --- RF Default ---
print("\n[RF Default]")
rf_def = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf_def.fit(X_train, y_train)
rf_def_result = evaluate_model("RF Default (Test)", y_test, rf_def.predict(X_test))

# --- RF GridSearch ---
print("\n[RF GridSearch Tuning]")
rf_params = [
    {'n_estimators': n, 'max_depth': d, 'min_samples_split': s}
    for n in [100, 200, 300]
    for d in [10, 15, 20, None]
    for s in [2, 5]
]
best_rf_rmse, best_rf_params, best_rf_model = float('inf'), {}, None
for i, p in enumerate(rf_params):
    model = RandomForestRegressor(**p, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    pred_val = model.predict(X_val)
    val_inv = scaler_y.inverse_transform(y_val.reshape(-1, 1)).flatten()
    pred_inv = scaler_y.inverse_transform(pred_val.reshape(-1, 1)).flatten()
    rmse = np.sqrt(mean_squared_error(val_inv, pred_inv))
    if rmse < best_rf_rmse:
        best_rf_rmse = rmse
        best_rf_params = p
        best_rf_model = model
    if (i+1) % 8 == 0:
        print(f"  {i+1}/{len(rf_params)} kombinasi selesai...")

print(f"  Best RF params: {best_rf_params} | Val RMSE: {best_rf_rmse:.4f}")
rf_tuned_result = evaluate_model("RF Tuned (Test)", y_test, best_rf_model.predict(X_test))

# --- XGBoost Default ---
print("\n[XGBoost Default]")
xgb_def = XGBRegressor(n_estimators=100, random_state=42, verbosity=0)
xgb_def.fit(X_train, y_train)
xgb_def_result = evaluate_model("XGB Default (Test)", y_test, xgb_def.predict(X_test))

# --- XGBoost GridSearch ---
print("\n[XGBoost GridSearch Tuning]")
xgb_params = [
    {'n_estimators': n, 'max_depth': d, 'learning_rate': lr}
    for n in [100, 200, 300]
    for d in [5, 7, 10]
    for lr in [0.01, 0.05, 0.1]
]
best_xgb_rmse, best_xgb_params, best_xgb_model = float('inf'), {}, None
for i, p in enumerate(xgb_params):
    model = XGBRegressor(**p, random_state=42, verbosity=0)
    model.fit(X_train, y_train)
    pred_val = model.predict(X_val)
    val_inv = scaler_y.inverse_transform(y_val.reshape(-1, 1)).flatten()
    pred_inv = scaler_y.inverse_transform(pred_val.reshape(-1, 1)).flatten()
    rmse = np.sqrt(mean_squared_error(val_inv, pred_inv))
    if rmse < best_xgb_rmse:
        best_xgb_rmse = rmse
        best_xgb_params = p
        best_xgb_model = model
    if (i+1) % 9 == 0:
        print(f"  {i+1}/{len(xgb_params)} kombinasi selesai...")

print(f"  Best XGB params: {best_xgb_params} | Val RMSE: {best_xgb_rmse:.4f}")
xgb_tuned_result = evaluate_model("XGB Tuned (Test)", y_test, best_xgb_model.predict(X_test))

# Simpan model baseline
joblib.dump(best_rf_model, os.path.join(MODEL_DIR, 'best_rf_model.pkl'))
joblib.dump(best_xgb_model, os.path.join(MODEL_DIR, 'best_xgb_model.pkl'))
print("\n[OK] Baseline models disimpan.")

# ============================================================
# FASE 3: DEEP LEARNING (LSTM & BiLSTM)
# ============================================================
print("\n" + "=" * 65)
print("FASE 3: DEEP LEARNING (LSTM & BiLSTM)")
print("=" * 65)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout, Input
from tensorflow.keras.callbacks import EarlyStopping

# Sliding Window 24 jam
TIME_STEPS = 24
def create_sequences(data_df, target_col, time_steps=24):
    X, y = [], []
    arr = data_df.values
    tidx = data_df.columns.get_loc(target_col)
    for i in range(len(arr) - time_steps):
        X.append(arr[i:(i + time_steps)])
        y.append(arr[i + time_steps, tidx])
    return np.array(X), np.array(y)

X_train_seq, y_train_seq = create_sequences(train_scaled, target_col, TIME_STEPS)
X_val_seq, y_val_seq = create_sequences(val_scaled, target_col, TIME_STEPS)
X_test_seq, y_test_seq = create_sequences(test_scaled, target_col, TIME_STEPS)
n_features = X_train_seq.shape[2]
print(f"Tensor shapes: Train={X_train_seq.shape}, Val={X_val_seq.shape}, Test={X_test_seq.shape}")

def evaluate_dl(name, model, X_seq, y_seq):
    y_pred_s = model.predict(X_seq, verbose=0)
    y_true = scaler_y.inverse_transform(y_seq.reshape(-1, 1)).flatten()
    y_pred = scaler_y.inverse_transform(y_pred_s).flatten()
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    print(f"  {name}: RMSE={rmse:.4f} | MAE={mae:.4f} | R²={r2:.4f}")
    return {'name': name, 'rmse': rmse, 'mae': mae, 'r2': r2, 'y_true': y_true, 'y_pred': y_pred}

# --- LSTM Default ---
print("\n[LSTM Default] Training...")
es = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1)
lstm_def = Sequential([
    Input(shape=(TIME_STEPS, n_features)),
    LSTM(64, return_sequences=True), Dropout(0.2),
    LSTM(32, return_sequences=False), Dropout(0.2),
    Dense(1)
])
lstm_def.compile(optimizer='adam', loss='mse')
t0 = time.time()
lstm_def.fit(X_train_seq, y_train_seq, epochs=50, batch_size=32,
             validation_data=(X_val_seq, y_val_seq), callbacks=[es], verbose=1)
print(f"  Training LSTM selesai ({time.time()-t0:.0f}s)")
lstm_def_result = evaluate_dl("LSTM Default (Test)", lstm_def, X_test_seq, y_test_seq)

# --- BiLSTM Default ---
print("\n[BiLSTM Default] Training...")
es2 = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True, verbose=1)
bilstm_def = Sequential([
    Input(shape=(TIME_STEPS, n_features)),
    Bidirectional(LSTM(64, return_sequences=True)), Dropout(0.2),
    Bidirectional(LSTM(32, return_sequences=False)), Dropout(0.2),
    Dense(1)
])
bilstm_def.compile(optimizer='adam', loss='mse')
t0 = time.time()
bilstm_def.fit(X_train_seq, y_train_seq, epochs=50, batch_size=32,
               validation_data=(X_val_seq, y_val_seq), callbacks=[es2], verbose=1)
print(f"  Training BiLSTM selesai ({time.time()-t0:.0f}s)")
bilstm_def_result = evaluate_dl("BiLSTM Default (Test)", bilstm_def, X_test_seq, y_test_seq)

# --- Grid Search Tuning (dikurangi untuk CPU) ---
print("\n[Grid Search Tuning — LSTM & BiLSTM]")
from itertools import product
param_grid_dl = {
    'units': [32, 64, 128],
    'dropout': [0.1, 0.2, 0.3],
    'batch_size': [32, 64]
}
combos = list(product(param_grid_dl['units'], param_grid_dl['dropout'], param_grid_dl['batch_size']))
print(f"Total kombinasi per arsitektur: {len(combos)}")

def grid_search_dl(arch_name, build_fn):
    best_rmse, best_params, best_model = float('inf'), {}, None
    results = []
    for idx, (units, dropout, batch) in enumerate(combos):
        print(f"  [{idx+1}/{len(combos)}] {arch_name} units={units}, drop={dropout}, batch={batch}", end=' ')
        tf.keras.backend.clear_session()
        model = build_fn(units, dropout)
        es_t = EarlyStopping(monitor='val_loss', patience=7, restore_best_weights=True, verbose=0)
        model.fit(X_train_seq, y_train_seq, epochs=50, batch_size=batch,
                  validation_data=(X_val_seq, y_val_seq), callbacks=[es_t], verbose=0)
        yp = model.predict(X_val_seq, verbose=0)
        vi = scaler_y.inverse_transform(y_val_seq.reshape(-1, 1)).flatten()
        pi = scaler_y.inverse_transform(yp).flatten()
        rmse = np.sqrt(mean_squared_error(vi, pi))
        print(f"-> Val RMSE: {rmse:.4f}")
        results.append({'units': units, 'dropout': dropout, 'batch_size': batch, 'val_rmse': rmse})
        if rmse < best_rmse:
            best_rmse, best_params, best_model = rmse, {'units': units, 'dropout': dropout, 'batch_size': batch}, model
    return best_rmse, best_params, best_model, results

def build_lstm_gs(units, dropout):
    m = Sequential([Input(shape=(TIME_STEPS, n_features)),
        LSTM(units, return_sequences=True), Dropout(dropout),
        LSTM(units//2, return_sequences=False), Dropout(dropout), Dense(1)])
    m.compile(optimizer='adam', loss='mse'); return m

def build_bilstm_gs(units, dropout):
    m = Sequential([Input(shape=(TIME_STEPS, n_features)),
        Bidirectional(LSTM(units, return_sequences=True)), Dropout(dropout),
        Bidirectional(LSTM(units//2, return_sequences=False)), Dropout(dropout), Dense(1)])
    m.compile(optimizer='adam', loss='mse'); return m

print("\n--- LSTM Tuning ---")
lstm_best_rmse, lstm_best_params, lstm_best_model, lstm_gs_results = grid_search_dl("LSTM", build_lstm_gs)
print(f"\n  LSTM Best: {lstm_best_params} | Val RMSE: {lstm_best_rmse:.4f}")

print("\n--- BiLSTM Tuning ---")
bilstm_best_rmse, bilstm_best_params, bilstm_best_model, bilstm_gs_results = grid_search_dl("BiLSTM", build_bilstm_gs)
print(f"\n  BiLSTM Best: {bilstm_best_params} | Val RMSE: {bilstm_best_rmse:.4f}")

# Evaluasi Tuned pada Test
lstm_tuned_result = evaluate_dl("LSTM Tuned (Test)", lstm_best_model, X_test_seq, y_test_seq)
bilstm_tuned_result = evaluate_dl("BiLSTM Tuned (Test)", bilstm_best_model, X_test_seq, y_test_seq)

# Simpan model
lstm_best_model.save(os.path.join(MODEL_DIR, 'lstm_model.keras'))
bilstm_best_model.save(os.path.join(MODEL_DIR, 'bilstm_model.keras'))

# Tentukan pemenang akhir DL
all_dl = [
    ('LSTM Default', lstm_def_result, lstm_def),
    ('LSTM Tuned', lstm_tuned_result, lstm_best_model),
    ('BiLSTM Default', bilstm_def_result, bilstm_def),
    ('BiLSTM Tuned', bilstm_tuned_result, bilstm_best_model)
]
dl_winner = min(all_dl, key=lambda x: x[1]['rmse'])
dl_winner[2].save(os.path.join(MODEL_DIR, 'best_dl_model.keras'))
joblib.dump({'model_name': dl_winner[0], 'rmse': dl_winner[1]['rmse'],
             'mae': dl_winner[1]['mae'], 'r2': dl_winner[1]['r2']},
            os.path.join(MODEL_DIR, 'best_dl_info.pkl'))
print(f"\n>> Pemenang DL: {dl_winner[0]} (RMSE={dl_winner[1]['rmse']:.4f})")

# ============================================================
# FASE 4: TABEL PERBANDINGAN AKHIR & VISUALISASI
# ============================================================
print("\n" + "=" * 65)
print("FASE 4: TABEL PERBANDINGAN AKHIR")
print("=" * 65)

all_results = [rf_def_result, rf_tuned_result, xgb_def_result, xgb_tuned_result,
               lstm_def_result, lstm_tuned_result, bilstm_def_result, bilstm_tuned_result]

comp_df = pd.DataFrame([{'Model': r['name'], 'RMSE': r['rmse'], 'MAE': r['mae'], 'R²': r['r2']} for r in all_results])
comp_df = comp_df.sort_values('RMSE')
print("\n" + comp_df.to_string(index=False))
comp_df.to_csv(os.path.join(DATA_PROC, 'model_comparison.csv'), index=False)

# --- Visualisasi: Bar Chart Perbandingan RMSE ---
fig, ax = plt.subplots(figsize=(12, 6))
colors = ['#2ecc71' if 'Tuned' in m else '#95a5a6' for m in comp_df['Model']]
bars = ax.barh(comp_df['Model'], comp_df['RMSE'], color=colors, edgecolor='black', linewidth=0.5)
ax.set_xlabel('RMSE (µg/m³)', fontsize=12, fontweight='bold')
ax.set_ylabel('Model', fontsize=12, fontweight='bold')
ax.set_title('Perbandingan RMSE Seluruh Model (Test Set)', fontsize=14, fontweight='bold')
ax.invert_yaxis()
for bar, val in zip(bars, comp_df['RMSE']):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f'{val:.2f}', va='center', fontsize=10)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'model_comparison_rmse.png'), dpi=150, bbox_inches='tight')
plt.close()
print("[OK] Grafik perbandingan RMSE disimpan.")

# --- Visualisasi: Prediksi vs Aktual (model terbaik keseluruhan) ---
overall_winner = min(all_results, key=lambda x: x['rmse'])
subset = min(336, len(overall_winner['y_true']))
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(range(subset), overall_winner['y_true'][:subset], label='Aktual PM2.5', color='black', linewidth=2)
ax.plot(range(subset), overall_winner['y_pred'][:subset], label=f"Prediksi ({overall_winner['name']})", color='crimson', alpha=0.8, linestyle='--')
ax.set_xlabel('Jam ke-', fontsize=12, fontweight='bold')
ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)', fontsize=12, fontweight='bold')
ax.set_title(f"Prediksi vs Aktual — {overall_winner['name']} (14 Hari Pertama Test Set)", fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'prediction_vs_actual.png'), dpi=150, bbox_inches='tight')
plt.close()
print("[OK] Grafik Prediksi vs Aktual disimpan.")

# --- Visualisasi: Scatter Plot (Kalibrasi Model) ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(overall_winner['y_true'], overall_winner['y_pred'], alpha=0.3, s=10, color='steelblue')
lims = [min(overall_winner['y_true'].min(), overall_winner['y_pred'].min()),
        max(overall_winner['y_true'].max(), overall_winner['y_pred'].max())]
ax.plot(lims, lims, 'r--', linewidth=2, label='Garis Ideal (y=x)')
ax.set_xlabel('PM2.5 Aktual (µg/m³)', fontsize=12, fontweight='bold')
ax.set_ylabel('PM2.5 Prediksi (µg/m³)', fontsize=12, fontweight='bold')
ax.set_title(f"Scatter Plot Kalibrasi — {overall_winner['name']}", fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, 'scatter_calibration.png'), dpi=150, bbox_inches='tight')
plt.close()
print("[OK] Scatter plot kalibrasi disimpan.")

print("\n" + "=" * 65)
print("SELURUH PIPELINE SELESAI!")
print(f"Pemenang: {overall_winner['name']} | RMSE={overall_winner['rmse']:.4f}")
print("=" * 65)
