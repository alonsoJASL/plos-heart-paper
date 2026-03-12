# Supplementary Material Promises Tracker

This document tracks all commitments made to include information in Supplementary Material during manuscript revision.

---

## STATUS KEY
- [ ] Not started
- [x] Complete
- [~] Partially complete / needs verification

---

## 1. CGAL Meshing Parameters

**Promised in:** 
- Sprint 4, Task 2 (R2-2): FEM type specification
- Sprint 4, Task 5 (R2-5): User mesh control

**Location in manuscript:**
- Methods Section 3.1.2: "Complete parameter specifications are provided in the Supplementary Material"
- Methods Section 3.1.2: "...specified globally for the entire heart geometry. Complete parameter specifications are provided in the Supplementary Material."

**What must be included:**
- [x] Table of CGAL parameters used:
  - [x] `facet_size` value (target: ~0.5 mm)
  - [x] `cell_size` value (target: ~0.5 mm)
  - [x] `facet_distance` value
  - [x] `facet_angle` (if used)
  - [x] `cell_radius_edge_ratio` (if used)
- [x] Brief description of each parameter's effect on mesh quality/density
- [x] Note that parameters are applied globally, not regionally

**Format suggestion:** Supplementary Table or Supplementary Methods section

**Current status in Supp Material:** [x] Complete — `sections/supp/s4_cgal_params.tex`, legend in `manuscript.tex`

---

## 2. Mechanical Simulation Boundary Conditions

**Promised in:** 
- Main manuscript Methods Section 3.3 (pre-existing reference)

**Location in manuscript:**
- Methods Section 3.3: "Mechanics simulations were run with the same boundary conditions as the work by~\cite{strocchi2023_cell}, which can be consulted in the Supplementary Material."

**What must be included:**
- [x] Description of pericardial boundary conditions
- [x] Robin boundary condition parameters (if applicable)
- [x] Base constraints (epicardial/basal plane)
- [x] Any displacement or force boundary conditions applied

**Current status in Supp Material:** [x] Complete — `sections/supp/s6_boundary_conditions.tex`, legend in `manuscript.tex`

---

## 3. Mesh Quality Statistics (NEW - Sprint 0/4)

**Promised in:**
- Sprint 4, Task 3 (R2-3): Mesh quality assessment response

**Location in manuscript:**
- Response letter: "Detailed statistics available in `reviews_data/mesh_quality_summary.csv`"
- Not explicitly promised in manuscript text, but would strengthen it

**What could be included (OPTIONAL):**
- [x] Supplementary Table: Full mesh quality statistics per case (50 rows) — submitted as S8 Data file instead of rendered table
  - Columns: mesh_id, n_elements, min_quality, max_quality, mean_quality, stddev, n_inverted, n_degenerate
- [x] Supplementary Figure: Histogram of mean element quality distribution across cohort — S7 Figure in supplement PDF
- [x] Brief methods description of meshtool quality metric — in `s7_mesh_quality.tex`

**Current status:** [x] Complete — S7 Fig in `supplement_main.tex`; table commented out (`\iffalse`); raw data as `supplementary/S8_Data_mesh_quality.csv`; legends in `manuscript.tex`

**Decision:** Figure in supplement PDF (S7); full per-model data submitted as S8 Data file.

---

## 4. Complete List of 37 Mesh Labels

**Promised in:**
- Main manuscript Methods Section 3.1.1 (pre-existing reference)

**Location in manuscript:**
- Methods Section 3.1.1: "A table of the labels is provided in the Supplementary material."

**What must be included:**
- [x] Table listing all 37 anatomical labels
- [x] Label ID number
- [x] Anatomical structure name
- [x] Structure type (myocardium, blood pool, valve plane, vessel)

**Current status in Supp Material:** [x] Complete — `sections/supp/s5_labels.tex`, legend in `manuscript.tex`

---

## 5. Statistical Analysis Results (Pre-existing)

**Location in manuscript:**
- Various references throughout Results section

**What should be included:**
- [x] Full ANOVA tables — `supplementary/S10_Data_anova.xlsx`
- [x] Complete pairwise comparison results — `supplementary/S11_Data_posthoc.xlsx`
- [x] Effect size tables — included in S11 Data (Cohen's d, CI)
- [x] Raw data or summary statistics tables — `supplementary/S9_Data_summary.xlsx`, `S12_Data_geometric_stats.csv`

**Current status:** [x] Complete — S9–S13 Data files in `supplementary/`, legends in `manuscript.tex`

---

## 6. TAT-QRS Correlation Analysis (NEW - Sprint 1)

**Promised in:**
- Sprint 1: Methods Section 3.3
- Sprint 1: Discussion Section 5.5

**Location in manuscript:**
- Methods Section 3.3: "...Supplementary Figure~S1"
- Results/Discussion references to stratified correlation

**What must be included:**
- [x] Supplementary Figure S1: Stratified scatter plot (TAT vs QRS by condition) - COMPLETE
  - File: `reviews_data/deliverables/sp1_supp_tat_qrs_stratified.pdf`
- [x] Legend for S1 Figure added to `manuscript.tex` (Supporting Information section)

**Figure caption template:**
```
Supplementary Figure S1. Correlation between simulated ventricular total 
activation time (TAT) and recorded ECG QRS duration, stratified by condition.

In control hearts (blue, n=17), TAT showed a strong positive correlation with 
QRS duration (Pearson r = 0.649, p = 0.005), indicating that anatomical 
variability alone can predict conduction time in healthy myocardium when using 
uniform electrophysiological parameters. In heart failure patients (red, n=16), 
no correlation was observed (r = -0.127, p = 0.64), reflecting that pathological 
conduction delays (fibrosis, scar, conduction blocks) are not captured by 
anatomy alone and would require patient-specific tissue property calibration.
```

**Current status:** [x] Figure complete, [x] legend added to `manuscript.tex`

---

## 7. Geometric Characterization Analysis (NEW - Sprint 2)

**Promised in:**
- Sprint 2: Results Section 4
- Sprint 2: Discussion Section 5.2

**Location in manuscript:**
- Results Section 4: "Supplementary Table~S2" and "Supplementary Figure~S2"
- Discussion Section 5.2: References to geometric-functional correlations

**What must be included:**

### Supplementary Table S2: Geometric Characteristics
- [x] Data file ready: `reviews_data/deliverables/sp2_geometric_descriptive_stats.csv` - COMPLETE
- [x] Formatted as supplementary table — `sections/supp/s2_geometric_table.tex`; raw data also as `supplementary/S12_Data_geometric_stats.csv`
- [x] Legend added to `manuscript.tex`

**Table caption template:**
```
Supplementary Table S2. Geometric characteristics stratified by sex and 
heart failure status.

Mean ± SD reported for age (years), chamber volumes (mL), and total mesh 
elements (millions). Heart failure patients showed increased chamber volumes 
across all chambers, particularly pronounced in males. Mesh element counts 
scaled with anatomical size, reflecting the adaptive meshing algorithm.
```

### Supplementary Figure S2: Correlation Heatmap
- [x] Figure ready: `reviews_data/deliverables/sp2_correlation_heatmap.pdf` - COMPLETE
- [x] Legend added to `manuscript.tex`; raw correlation data also as `supplementary/S13_Data_correlation.csv`

**Current status:** [x] Both files complete, [x] legends added to `manuscript.tex`

---

## VERIFICATION CHECKLIST

Before final submission, check your current Supplementary Material document against this list:

### Critical (Promised explicitly in revisions):
- [x] CGAL parameters table (Sprint 4, Tasks 2 & 5) — S4 Table
- [x] Boundary conditions description (pre-existing) — S6 Methods
- [x] TAT-QRS correlation figure (Sprint 1) — S1 Figure
- [x] Geometric characteristics table (Sprint 2) — S2 Table
- [x] Correlation heatmap (Sprint 2) — S3 Figure

### Important (Promised in main manuscript):
- [x] 37-label table (Section 3.1.1) — S5 Table
- [x] Statistical analysis details (Results section) — S10–S11 Data

### Optional but Recommended:
- [x] Mesh quality statistics table — submitted as S8 Data (CSV) instead of rendered table
- [x] Mesh quality histogram figure — S7 Figure

---

## FILES READY FOR SUPPLEMENTARY MATERIAL

**Sprint 1 deliverables:**
- ✅ `reviews_data/deliverables/sp1_supp_tat_qrs_stratified.pdf` → S1 Figure (in supplement PDF)

**Sprint 2 deliverables:**
- ✅ `reviews_data/deliverables/sp2_geometric_descriptive_stats.csv` → S2 Table (in supplement PDF) + S12 Data
- ✅ `reviews_data/deliverables/sp2_correlation_heatmap.pdf` → S3 Figure (in supplement PDF)
- ✅ `reviews_data/deliverables/sp2_correlation_results.csv` → S13 Data

**Sprint 0 deliverables:**
- ✅ `reviews_data/mesh_quality_summary.csv` → S7 Figure (in supplement PDF) + S8 Data

---

## CURRENT SUPPLEMENTARY MATERIAL STRUCTURE

```
supplementary/
├── PCOMPBIOL-S-25-02911_amendments.pdf   ← revision amendments letter, NOT a SI file
├── classic_anova_results.xlsx            ← original (kept for reference)
├── classic_posthoc_results.xlsx          ← original (kept for reference)
├── summary_table.xlsx                    ← original (kept for reference)
├── S8_Data_mesh_quality.csv
├── S9_Data_summary.xlsx
├── S10_Data_anova.xlsx
├── S11_Data_posthoc.xlsx
├── S12_Data_geometric_stats.csv
└── S13_Data_correlation.csv
```

**Note:** Submit only S8–S13 files plus the supplement PDF. Do not submit originals or the amendments PDF.

---

## NOTES

- The Editor also requires: "Supporting Information legends missing after references" (Editor requirement E3)
- Make sure each supplementary file has a proper legend in the main manuscript after the References section

---

## TIMELINE

- **Sprint 4 completion:** Promises made, not yet fulfilled
- **Before Sprint 8 (Response Letter):** Verify all supplementary material is complete
- **Final submission:** Include legends in main manuscript after References

---

## TEMPLATE FOR SUPPLEMENTARY LEGENDS (to add after References)

```latex
\section*{Supporting Information}

\paragraph{S1 Figure. Correlation between simulated ventricular activation time and recorded ECG QRS duration.}
Stratified scatter plot showing relationship between total activation time (TAT) 
and QRS duration in control (blue, n=17) and heart failure (red, n=16) patients. 
Control hearts showed strong correlation (Pearson r = 0.649, p = 0.005), validating 
TAT as a QRS surrogate when anatomical variability dominates. Heart failure patients 
showed no correlation (r = -0.127, p = 0.64), consistent with unmeasured pathological 
tissue properties (fibrosis, conduction blocks).

\paragraph{S2 Table. Geometric characteristics stratified by sex and heart failure status.}
Mean ± SD for age (years), chamber volumes (mL), and mesh elements (millions). 
Heart failure patients exhibited increased volumes across all chambers, most 
pronounced in males. Mesh element counts scaled with anatomical size.

\paragraph{S3 Figure. Correlation matrix between geometric variables and simulation outputs.}
Spearman correlation coefficients (ρ) between geometric metrics (chamber volumes, 
mesh size, age) and simulation outputs (activation times, volume changes). Strong 
positive correlations indicate geometry predicts function under standardized parameters. 
All shown correlations significant at p < 0.05.

\paragraph{S4 Table. CGAL meshing parameters.}
Complete specification of Computational Geometry Algorithm Library parameters 
used for volumetric mesh generation, including facet\_size, cell\_size, and 
facet\_distance values.

\paragraph{S5 Table. Complete mesh label specification.}
List of all 37 anatomical labels assigned during segmentation and mesh generation, 
including label ID, anatomical structure name, and structure type.

\paragraph{S6 Methods. Mechanical simulation boundary conditions.}
Detailed specification of pericardial constraints and boundary conditions 
applied in passive inflation simulations.

% Optional - if including mesh quality data:
\paragraph{S7 Table. Mesh quality statistics (OPTIONAL).}
Per-model element quality metrics for all 50 hearts assessed using tet\_qmetric\_volume, 
including mean quality, standard deviation, and counts of inverted/degenerate elements.
```

**Status:** [x] Template implemented — S1–S13 legends are live in `manuscript.tex`.
S7–S13 entries were added 2026-03-12.