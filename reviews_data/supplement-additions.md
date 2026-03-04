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
- [ ] Table of CGAL parameters used:
  - [ ] `facet_size` value (target: ~0.5 mm)
  - [ ] `cell_size` value (target: ~0.5 mm)
  - [ ] `facet_distance` value
  - [ ] `facet_angle` (if used)
  - [ ] `cell_radius_edge_ratio` (if used)
- [ ] Brief description of each parameter's effect on mesh quality/density
- [ ] Note that parameters are applied globally, not regionally

**Format suggestion:** Supplementary Table or Supplementary Methods section

**Current status in Supp Material:** [ ] Not verified yet

---

## 2. Mechanical Simulation Boundary Conditions

**Promised in:** 
- Main manuscript Methods Section 3.3 (pre-existing reference)

**Location in manuscript:**
- Methods Section 3.3: "Mechanics simulations were run with the same boundary conditions as the work by~\cite{strocchi2023_cell}, which can be consulted in the Supplementary Material."

**What must be included:**
- [ ] Description of pericardial boundary conditions
- [ ] Robin boundary condition parameters (if applicable)
- [ ] Base constraints (epicardial/basal plane)
- [ ] Any displacement or force boundary conditions applied

**Current status in Supp Material:** [~] May already exist - VERIFY

---

## 3. Mesh Quality Statistics (NEW - Sprint 0/4)

**Promised in:**
- Sprint 4, Task 3 (R2-3): Mesh quality assessment response

**Location in manuscript:**
- Response letter: "Detailed statistics available in `reviews_data/mesh_quality_summary.csv`"
- Not explicitly promised in manuscript text, but would strengthen it

**What could be included (OPTIONAL):**
- [ ] Supplementary Table: Full mesh quality statistics per case (50 rows)
  - Columns: mesh_id, n_elements, min_quality, max_quality, mean_quality, stddev, n_inverted, n_degenerate
- [ ] Supplementary Figure: Histogram of mean element quality distribution across cohort
- [ ] Brief methods description of meshtool quality metric

**Current status:** [ ] Data exists in `reviews_data/mesh_quality_summary.csv`, needs formatting for supplement

**Decision needed:** Include as supplementary material or keep as repository data?

---

## 4. Complete List of 37 Mesh Labels

**Promised in:**
- Main manuscript Methods Section 3.1.1 (pre-existing reference)

**Location in manuscript:**
- Methods Section 3.1.1: "A table of the labels is provided in the Supplementary material."

**What must be included:**
- [ ] Table listing all 37 anatomical labels
- [ ] Label ID number
- [ ] Anatomical structure name
- [ ] Structure type (myocardium, blood pool, valve plane, vessel)

**Current status in Supp Material:** [~] May already exist - VERIFY

---

## 5. Statistical Analysis Results (Pre-existing)

**Location in manuscript:**
- Various references throughout Results section

**What should be included:**
- [ ] Full ANOVA tables
- [ ] Complete pairwise comparison results
- [ ] Effect size tables (may already be in main manuscript)
- [ ] Raw data or summary statistics tables

**Current status:** [~] Likely already included - VERIFY completeness

---

## VERIFICATION CHECKLIST

Before final submission, check your current Supplementary Material document against this list:

### Critical (Promised explicitly in Sprint 4):
- [ ] CGAL parameters table (Tasks 2 & 5)
- [ ] Boundary conditions description (pre-existing, verify present)

### Important (Promised in main manuscript):
- [ ] 37-label table (Section 3.1.1)
- [ ] Statistical analysis details (Results section)

### Optional but Recommended:
- [ ] Mesh quality statistics table
- [ ] Mesh quality histogram figure

---

## CURRENT SUPPLEMENTARY MATERIAL STRUCTURE

From your project tree, you currently have:
```
supplementary/
├── classic_anova_results.xlsx
├── classic_posthoc_results.xlsx
├── PCOMPBIOL-S-25-02911_amendments.pdf
└── summary_table.xlsx
```

**Action items:**
1. Check if `PCOMPBIOL-S-25-02911_amendments.pdf` is your Supplementary Material document
2. Verify which of the above items are already covered
3. Add missing items before final submission

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

\paragraph{S1 Table. CGAL Meshing Parameters.}
Complete specification of Computational Geometry Algorithm Library parameters 
used for volumetric mesh generation.

\paragraph{S2 Table. Complete Mesh Label Specification.}
List of all 37 anatomical labels assigned during the segmentation and 
mesh generation process.

\paragraph{S3 Table. Mesh Quality Statistics.}
Per-model element quality metrics for all 50 hearts in the cohort, assessed 
using the tet_qmetric_volume metric.

\paragraph{S4 Methods. Mechanical Simulation Boundary Conditions.}
Detailed specification of pericardial constraints and boundary conditions 
applied in passive inflation simulations.

[Add others as needed]
```

## 6. TAT-QRS Correlation Analysis (NEW - Sprint 1)

**Promised in:**
- Methods Section 3.3: "...Supplementary Figure~S1"

**What must be included:**
- [x] Supplementary Figure S1: Stratified scatter plot (COMPLETE)
- [ ] Add legend for S1 Figure after References in main manuscript

**Current status:** Figure ready, legend text needed