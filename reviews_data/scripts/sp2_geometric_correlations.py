#!/usr/bin/env python3
"""Sprint 2: Geometric characterization and correlation analysis."""

import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
DATA_FILE = Path.home() / "Dropbox/ic/fda_results/report.xlsx"
OUTPUT_DIR = Path("reviews_data/deliverables")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_excel(DATA_FILE)
print(f"Total cases: {len(df)}")

# Add total volumes for convenience
df['Vol_Total_V'] = df['Vol_LV'] + df['Vol_RV']
df['Vol_Total_A'] = df['Vol_LA'] + df['Vol_RA']
df['N_Total'] = df['N_Ventricles'] + df['N_Atria']

# Separate by sex and condition
male = df[df['Sex'] == 'M']
female = df[df['Sex'] == 'F']
control = df[df['Condition'] == 'C']
hf = df[df['Condition'] == 'HF']

print(f"Male: {len(male)}, Female: {len(female)}")
print(f"Control: {len(control)}, HF: {len(hf)}")

# =============================================================================
# PART 1: Descriptive Statistics Table
# =============================================================================

def compute_stats(group, label):
    """Compute mean ± SD for geometric variables."""
    return {
        'Group': label,
        'n': len(group),
        'Age': f"{group['Age'].mean():.1f} ± {group['Age'].std():.1f}",
        'Vol_LV': f"{group['Vol_LV'].mean():.1f} ± {group['Vol_LV'].std():.1f}",
        'Vol_RV': f"{group['Vol_RV'].mean():.1f} ± {group['Vol_RV'].std():.1f}",
        'Vol_LA': f"{group['Vol_LA'].mean():.1f} ± {group['Vol_LA'].std():.1f}",
        'Vol_RA': f"{group['Vol_RA'].mean():.1f} ± {group['Vol_RA'].std():.1f}",
        'N_elements': f"{group['N_Total'].mean()/1e6:.2f} ± {group['N_Total'].std()/1e6:.2f}",
    }

# Compute stats for each group
groups = [
    (male[male['Condition'] == 'C'], 'Male Control'),
    (male[male['Condition'] == 'HF'], 'Male HF'),
    (female[female['Condition'] == 'C'], 'Female Control'),
    (female[female['Condition'] == 'HF'], 'Female HF'),
]

stats_table = pd.DataFrame([compute_stats(g, label) for g, label in groups])
print("\n=== Descriptive Statistics ===")
print(stats_table.to_string(index=False))

# Save table
stats_table.to_csv(OUTPUT_DIR / 'sp2_geometric_descriptive_stats.csv', index=False)
print(f"\nDescriptive stats saved to {OUTPUT_DIR / 'sp2_geometric_descriptive_stats.csv'}")

# =============================================================================
# PART 2: Correlation Analysis
# =============================================================================

# Select geometric and simulation variables
geometric_vars = ['Age', 'Vol_LV', 'Vol_RV', 'Vol_LA', 'Vol_RA', 'N_Total']
simulation_vars = ['TAT_LV', 'TAT_RV', 'TAT_V', 'TAT_LA', 'delta_Vol_LV', 'delta_Vol_RV']

# Compute Spearman correlations (handles non-normal distributions better)
correlations = []

for geom_var in geometric_vars:
    for sim_var in simulation_vars:
        # Remove NaN pairs
        clean = df[[geom_var, sim_var]].dropna()
        if len(clean) < 10:  # Need minimum sample size
            continue
        
        rho, p = stats.spearmanr(clean[geom_var], clean[sim_var])
        correlations.append({
            'Geometric': geom_var,
            'Simulation': sim_var,
            'Spearman_rho': rho,
            'p_value': p,
            'n': len(clean),
            'Significant': '***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else ''
        })

corr_df = pd.DataFrame(correlations)
corr_df = corr_df.sort_values('p_value')

print("\n=== Top 10 Strongest Correlations ===")
print(corr_df.head(10).to_string(index=False))

# Save full correlation table
corr_df.to_csv(OUTPUT_DIR / 'sp2_correlation_results.csv', index=False)
print(f"\nFull correlation table saved to {OUTPUT_DIR / 'sp2_correlation_results.csv'}")

# =============================================================================
# PART 3: Correlation Heatmap
# =============================================================================

# Create correlation matrix for heatmap
geom_sim_data = df[geometric_vars + simulation_vars].dropna()
corr_matrix = geom_sim_data.corr(method='spearman')

# Extract only geometric vs simulation block
corr_subset = corr_matrix.loc[geometric_vars, simulation_vars]

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_subset, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, vmin=-1, vmax=1, ax=ax,
            cbar_kws={'label': 'Spearman ρ'})
ax.set_xlabel('Simulation Outputs', fontsize=12)
ax.set_ylabel('Geometric Variables', fontsize=12)
ax.set_title('Correlation: Geometry vs Simulation Outputs', fontsize=14)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'sp2_correlation_heatmap.pdf', dpi=300)
print(f"\nHeatmap saved to {OUTPUT_DIR / 'sp2_correlation_heatmap.pdf'}")

# =============================================================================
# PART 4: Stratified Analysis (Sex and HF)
# =============================================================================

print("\n=== Stratified Correlations (Vol_LV vs TAT_LV) ===")

for group, label in [(control, 'Control'), (hf, 'HF'), (male, 'Male'), (female, 'Female')]:
    clean = group[['Vol_LV', 'TAT_LV']].dropna()
    if len(clean) >= 5:
        rho, p = stats.spearmanr(clean['Vol_LV'], clean['TAT_LV'])
        print(f"{label:15} (n={len(clean):2}): ρ={rho:6.3f}, p={p:.4f}")

# =============================================================================
# PART 5: Summary Report
# =============================================================================

with open(OUTPUT_DIR / 'sp2_summary_report.txt', 'w') as f:
    f.write("Sprint 2: Geometric Characterization Summary\n")
    f.write("=" * 70 + "\n\n")
    
    f.write("DESCRIPTIVE STATISTICS\n")
    f.write("-" * 70 + "\n")
    f.write(stats_table.to_string(index=False))
    f.write("\n\n")
    
    f.write("TOP CORRELATIONS (p < 0.05)\n")
    f.write("-" * 70 + "\n")
    sig_corr = corr_df[corr_df['p_value'] < 0.05]
    f.write(sig_corr.to_string(index=False))
    f.write("\n\n")
    
    f.write("KEY FINDINGS\n")
    f.write("-" * 70 + "\n")
    f.write(f"- Total correlations tested: {len(corr_df)}\n")
    f.write(f"- Significant correlations (p<0.05): {len(sig_corr)}\n")
    f.write(f"- Strongest correlation: {corr_df.iloc[0]['Geometric']} vs ")
    f.write(f"{corr_df.iloc[0]['Simulation']} (ρ={corr_df.iloc[0]['Spearman_rho']:.3f})\n")

print(f"\nSummary report saved to {OUTPUT_DIR / 'sp2_summary_report.txt'}")
print("\n=== Sprint 2 Analysis Complete ===")