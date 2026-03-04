#!/usr/bin/env python3
"""Sprint 1: Stratified QRS correlation by condition."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# Paths
DATA_FILE = Path.home() / "Dropbox/ic/fda_results/report.xlsx"
OUTPUT_DIR = Path("reviews_data/deliverables")

# Load data
df = pd.read_excel(DATA_FILE)
df_clean = df.dropna(subset=['recorded_ECG_QRS', 'TAT_V'])

print(f"Total cases with QRS data: {len(df_clean)}")

# Stratify by condition
control = df_clean[df_clean['Condition'] == 'C']
hf = df_clean[df_clean['Condition'] == 'HF']

print(f"  Controls: {len(control)}")
print(f"  HF: {len(hf)}")

# Correlations - Overall
r_all, p_all = stats.pearsonr(df_clean['TAT_V'], df_clean['recorded_ECG_QRS'])
rho_all, p_rho_all = stats.spearmanr(df_clean['TAT_V'], df_clean['recorded_ECG_QRS'])

# Correlations - Control
r_ctrl, p_ctrl = stats.pearsonr(control['TAT_V'], control['recorded_ECG_QRS'])
rho_ctrl, p_rho_ctrl = stats.spearmanr(control['TAT_V'], control['recorded_ECG_QRS'])

# Correlations - HF
r_hf, p_hf = stats.pearsonr(hf['TAT_V'], hf['recorded_ECG_QRS'])
rho_hf, p_rho_hf = stats.spearmanr(hf['TAT_V'], hf['recorded_ECG_QRS'])

print(f"\n--- Overall (n={len(df_clean)}) ---")
print(f"Pearson r = {r_all:.3f}, p = {p_all:.4f}")
print(f"Spearman ρ = {rho_all:.3f}, p = {p_rho_all:.4f}")

print(f"\n--- Controls (n={len(control)}) ---")
print(f"Pearson r = {r_ctrl:.3f}, p = {p_ctrl:.4f}")
print(f"Spearman ρ = {rho_ctrl:.3f}, p = {p_rho_ctrl:.4f}")

print(f"\n--- HF (n={len(hf)}) ---")
print(f"Pearson r = {r_hf:.3f}, p = {p_hf:.4f}")
print(f"Spearman ρ = {rho_hf:.3f}, p = {p_rho_hf:.4f}")

# Plot - Stratified
fig, ax = plt.subplots(figsize=(7, 5))

# Control points
ax.scatter(control['TAT_V'], control['recorded_ECG_QRS'], 
           alpha=0.7, s=80, edgecolors='black', linewidth=0.5,
           color='blue', label=f'Control (n={len(control)})')

# HF points
ax.scatter(hf['TAT_V'], hf['recorded_ECG_QRS'], 
           alpha=0.7, s=80, edgecolors='black', linewidth=0.5,
           color='red', label=f'HF (n={len(hf)})')

# Regression lines
if len(control) > 2:
    slope_c, int_c, _, _, _ = stats.linregress(control['TAT_V'], control['recorded_ECG_QRS'])
    x_c = np.linspace(control['TAT_V'].min(), control['TAT_V'].max(), 100)
    ax.plot(x_c, slope_c * x_c + int_c, 'b--', linewidth=2, alpha=0.7)

if len(hf) > 2:
    slope_h, int_h, _, _, _ = stats.linregress(hf['TAT_V'], hf['recorded_ECG_QRS'])
    x_h = np.linspace(hf['TAT_V'].min(), hf['TAT_V'].max(), 100)
    ax.plot(x_h, slope_h * x_h + int_h, 'r--', linewidth=2, alpha=0.7)

# Annotations
ax.text(0.05, 0.95,
        f"Control: r = {r_ctrl:.3f} (p = {p_ctrl:.3f})\n"
        f"HF: r = {r_hf:.3f} (p = {p_hf:.3f})\n"
        f"Overall: r = {r_all:.3f} (p = {p_all:.3f})",
        transform=ax.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

ax.set_xlabel('Ventricular TAT (ms)', fontsize=12)
ax.set_ylabel('Recorded ECG QRS Duration (ms)', fontsize=12)
ax.set_title('TAT vs QRS: Stratified by Condition', fontsize=14)
ax.legend(loc='lower right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'sp1_supp_tat_qrs_stratified.pdf', dpi=300)
print(f"\nStratified plot saved to {OUTPUT_DIR / 'sp1_supp_tat_qrs_stratified.pdf'}")

# Save results
with open(OUTPUT_DIR / 'sp1_correlation_stratified.txt', 'w') as f:
    f.write("Stratified QRS vs TAT Correlation\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Overall (n={len(df_clean)}):\n")
    f.write(f"  Pearson r = {r_all:.4f} (p = {p_all:.6f})\n")
    f.write(f"  Spearman ρ = {rho_all:.4f} (p = {p_rho_all:.6f})\n\n")
    f.write(f"Controls (n={len(control)}):\n")
    f.write(f"  Pearson r = {r_ctrl:.4f} (p = {p_ctrl:.6f})\n")
    f.write(f"  Spearman ρ = {rho_ctrl:.4f} (p = {p_rho_ctrl:.6f})\n\n")
    f.write(f"HF (n={len(hf)}):\n")
    f.write(f"  Pearson r = {r_hf:.4f} (p = {p_hf:.6f})\n")
    f.write(f"  Spearman ρ = {rho_hf:.4f} (p = {p_rho_hf:.6f})\n")

print(f"Results saved to {OUTPUT_DIR / 'sp1_correlation_stratified.txt'}")