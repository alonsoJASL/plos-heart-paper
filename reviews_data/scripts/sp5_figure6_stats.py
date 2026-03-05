#!/usr/bin/env python3
"""Calculate percentages for Figure 6 annotations."""

import pandas as pd
from pathlib import Path

# Load data
DATA_FILE = Path.home() / "Dropbox/ic/fda_results/report.xlsx"
df = pd.read_excel(DATA_FILE)

# UKBB reference ranges (from Petersen 2017, manuscript line 232-234)
# These are 95% prediction intervals
UKBB_RANGES = {
    'Male_LV': (109, 218),
    'Female_LV': (88, 161),
    'Male_RV': (132, 277),  # Check manuscript for exact values
    'Female_RV': (98, 195),  # Check manuscript for exact values
}

def calc_percentages(group_df, vol_col, range_tuple):
    """Calculate % inside reference range."""
    in_range = group_df[
        (group_df[vol_col] >= range_tuple[0]) & 
        (group_df[vol_col] <= range_tuple[1])
    ]
    total = len(group_df.dropna(subset=[vol_col]))
    pct = (len(in_range) / total * 100) if total > 0 else 0
    return len(in_range), total, pct

# Separate by sex and condition
male_c = df[(df['Sex'] == 'M') & (df['Condition'] == 'C')]
male_hf = df[(df['Sex'] == 'M') & (df['Condition'] == 'HF')]
female_c = df[(df['Sex'] == 'F') & (df['Condition'] == 'C')]
female_hf = df[(df['Sex'] == 'F') & (df['Condition'] == 'HF')]

print("=" * 70)
print("FIGURE 6 ANNOTATION TEXT")
print("=" * 70)

# LV Males
in_c, tot_c, pct_c = calc_percentages(male_c, 'Vol_LV', UKBB_RANGES['Male_LV'])
in_hf, tot_hf, pct_hf = calc_percentages(male_hf, 'Vol_LV', UKBB_RANGES['Male_LV'])
print(f"\nLV Males Panel:")
print(f"  Control: {in_c}/{tot_c} ({pct_c:.0f}%) within range")
print(f"  HF: {in_hf}/{tot_hf} ({pct_hf:.0f}%) within range")

# LV Females
in_c, tot_c, pct_c = calc_percentages(female_c, 'Vol_LV', UKBB_RANGES['Female_LV'])
in_hf, tot_hf, pct_hf = calc_percentages(female_hf, 'Vol_LV', UKBB_RANGES['Female_LV'])
print(f"\nLV Females Panel:")
print(f"  Control: {in_c}/{tot_c} ({pct_c:.0f}%) within range")
print(f"  HF: {in_hf}/{tot_hf} ({pct_hf:.0f}%) within range")

# RV Males
in_c, tot_c, pct_c = calc_percentages(male_c, 'Vol_RV', UKBB_RANGES['Male_RV'])
in_hf, tot_hf, pct_hf = calc_percentages(male_hf, 'Vol_RV', UKBB_RANGES['Male_RV'])
print(f"\nRV Males Panel:")
print(f"  Control: {in_c}/{tot_c} ({pct_c:.0f}%) within range")
print(f"  HF: {in_hf}/{tot_hf} ({pct_hf:.0f}%) within range")

# RV Females
in_c, tot_c, pct_c = calc_percentages(female_c, 'Vol_RV', UKBB_RANGES['Female_RV'])
in_hf, tot_hf, pct_hf = calc_percentages(female_hf, 'Vol_RV', UKBB_RANGES['Female_RV'])
print(f"\nRV Females Panel:")
print(f"  Control: {in_c}/{tot_c} ({pct_c:.0f}%) within range")
print(f"  HF: {in_hf}/{tot_hf} ({pct_hf:.0f}%) within range")

print("\n" + "=" * 70)
print("Add these as text annotations in each panel of Figure 6")
print("=" * 70)