# Sprint 4: Methods Expansion - Technical Clarifications (90 min)

**Goal:** Add missing technical details to Methods section that R2 explicitly asked for. These are factual additions, not rewrites.

**Addresses:** R2-1, R2-2, R2-3 (writing up), R2-4, R2-5, R1-Maj-2

**Prerequisites:** Sprint 0 must be complete (you need the mesh stats from `sprint0_mesh_quality_stats.txt`)

---

## Task 1: CT Acquisition Phase and Pressure State (R2-1)

**What R2 asked:**
> "Are the reconstructed meshes referred to the same timepoint of the cardiac cycle? What is the internal pressure at that instant?"

**Where this goes:** Section 3.1 or beginning of Section 2 (Study Population)

### Subtasks:

- [ ] **Find CT acquisition documentation**
  - [X] Check DICOM headers from one sample scan (if you have access)
  - Done, non-gated CTs
  
- [ ] **Determine cardiac phase**
  - [ ] Most likely: end-diastolic (minimal ventricular volume)
  - [ ] Alternative: end-systolic (maximal contraction)
  - [ ] Confirm: ECG-gated? Retrospective reconstruction?

- [ ] **Determine pressure at that phase**
  - End-diastolic typical values:
    - [ ] LV: ~5-10 mmHg (passive filling)
    - [ ] RV: ~3-5 mmHg
    - [ ] LA/RA: ~5-8 mmHg
  - End-systolic typical values:
    - [ ] LV: ~120 mmHg (peak contraction)
    - [ ] RV: ~25 mmHg
  - [ ] If unknown: state "unloaded reference configuration"

### What to write:

**Option A (if you know the phase):**
```latex
\added[id=SL]{All CT scans were acquired at end-diastole (minimal 
ventricular volume) using ECG-gated retrospective reconstruction. At 
this phase, intracavitary pressures are minimal (LV $\sim$5--10~mmHg, 
RV $\sim$3--5~mmHg), representing an approximately unloaded reference 
configuration for the myocardium.}
```

**Option B (if phase is uncertain):**
```latex
\added[id=SL]{All CT scans represent a static reference configuration 
of the cardiac anatomy. Meshes were reconstructed from the same cardiac 
phase for each patient to ensure consistency. The reference state 
represents minimal mechanical loading prior to simulation of passive 
inflation.}
```

**Location:** Add to Section 2 (Study Population) right after describing the CT scans, OR add to beginning of Section 3.1 before segmentation.

- [ ] Insert text with tracked changes
- [ ] Verify statement is accurate (don't guess if uncertain)

---

## Task 2: Finite Element Type Specification (R2-2)

**What R2 asked:**
> "Which type of finite elements are supported by the mesh-generator?"

**Where this goes:** Section 3.1.2 "Conversion to Mesh"

### Subtasks:

- [ ] **Confirm element type from your CARP simulation logs**
  ```bash
  grep -i "element type\|tetrahedra" /path/to/simulation.log | head -5
  ```
  Or check meshtool output (you already know this: linear tetrahedra, 4 nodes)

- [ ] **Get element size statistics** (if not already in sprint0_mesh_quality_stats.txt)
  ```bash
  # If you have edge length data from meshtool:
  meshtool query meshdata -msh=output_mesh -metric=edge_lengths
  ```
  Or extract from your mesh_quality_summary.csv if you calculated it

- [ ] **Record CGAL target resolution**
  - Check your CGAL parameters file or Supplementary Material
  - Typical: cell_size = 0.5 mm, facet_size = 0.5 mm

### What to write:

```latex
\added[id=SL]{The CGAL mesher generates unstructured volumetric meshes 
composed of linear tetrahedral elements (4 nodes per element). Target 
element edge length was set to $\sim$0.5~mm via the \texttt{cell\_size} 
parameter (see Supplementary Material for complete CGAL configuration). 
Final meshes contained a mean of $2.6 \times 10^6$ elements per heart 
(range $1.9$--$4.5 \times 10^6$).}
```

**Location:** Add to Section 3.1.2 right after describing the CGAL meshing step, before the mesh quality paragraph you already added.

- [ ] Insert text with tracked changes
- [ ] Cross-reference Supplementary Material where CGAL parameters are detailed

---

## Task 3: Mesh Quality Write-Up (R2-3)

**Status:** ✅ ALREADY DONE in our previous session

- [x] Text drafted and ready to insert at end of Section 3.2
- [ ] **Action for this sprint:** Actually insert it into your LaTeX file
- [ ] Compile and verify citation to meshtool [32] resolves

**No new work needed** — just execution of the snippet I already gave you.

---

## Task 4: Spatial Alignment Protocol (R2-4)

**What R2 asked:**
> "How are the models aligned to perform and compare the simulations?"

**Where this goes:** Section 3.2 or Section 3.3 (before describing simulations)

### Subtasks:

- [ ] **Clarify alignment approach**
  - Your models: each simulated in **native coordinate system** (no rigid registration)
  - Comparison: done on **scalar outputs** (volumes, activation times) which are alignment-invariant
  - UVCs provide **normalized functional coordinates** for regional analysis

- [ ] **Confirm this is accurate**
  - [ ] Did you perform any spatial registration/alignment between anatomies?
  - [ ] If NO: document that each mesh uses its own coordinate system
  - [ ] If YES: document the registration method

### What to write:

```latex
\added[id=SL]{Each patient-specific mesh was simulated in its native 
coordinate system without spatial registration to a common anatomical 
reference frame. Comparisons between models were performed on scalar 
outputs (chamber volumes, total activation times) that are invariant 
to rigid transformations. Universal Ventricular Coordinates 
(UVCs)~\cite{bayer2018} provide normalized transmural and apicobasal 
coordinates for regional functional analysis independent of absolute 
spatial positioning.}
```

**Location:** Add to Section 3.2 (after describing UVCs) OR at the beginning of Section 3.3 (before describing simulation setup).

- [ ] Insert text with tracked changes
- [ ] Verify Bayer citation exists (should be reference 33 in your manuscript)

---

## Task 5: User Mesh Control Documentation (R2-5)

**What R2 asked:**
> "Do the users have the possibility of controlling and adapting the mesh by varying the density in specific (user-defined) regions?"

**Where this goes:** Section 3.1.2 "Conversion to Mesh"

### Subtasks:

- [ ] **Check your Supplementary Material**
  - [ ] Locate where CGAL parameters are documented
  - [ ] Verify which parameters control mesh density (facet_size, cell_size, etc.)

- [ ] **Determine regional control capability**
  - CGAL: Can users specify different cell_size values for different regions?
  - Typically: YES via region-specific refinement in CGAL configuration

### What to write:

```latex
\added[id=SL]{Mesh density can be controlled via CGAL parameters 
(\texttt{facet\_size}, \texttt{cell\_size}, \texttt{facet\_distance}) 
either globally or on a per-region basis, allowing users to refine 
specific anatomical structures as needed. Complete parameter 
specifications are provided in Supplementary Material Section~X.}
```

**Location:** Add to Section 3.1.2 right after describing the CGAL meshing tool, OR as a final sentence in that paragraph.

- [ ] Insert text with tracked changes
- [ ] Add forward reference to correct Supplementary section number

---

## Task 6: "Upside Down Ventricle" Citation (R1-Maj-2)

**What R1 asked:**
> "Section 3.2: 'the left and the right atria were treated as an upside down single ventricle' — is this based on prior work? If so, please include another citation here to make this clear."

**Where this goes:** Section 3.2, the sentence describing UVC calculation for atria

### Subtasks:

- [ ] **Find the sentence in your LaTeX**
  - Look for: "left and right atria were treated as an upside down single ventricle"
  - Or similar wording about atrial UVC calculation

- [ ] **Identify the correct citation**
  - Bayer 2018 UVC paper (already in your references as [33])
  - This describes the coordinate transformation approach

### What to write:

**Current text (approximately):**
```latex
Additionally to the ventricles, UVCs are also calculated for the atria, 
to provide a system of coordinates defined on the volumetric mesh that 
facilitated the assignment of different tags within the mesh, and of 
boundary conditions for the pericardium. To achieve this, the left and 
the right atria were treated as an upside down single ventricle, with 
the apex manually placed between the two right pulmonary veins and 
behind the superior vena cava, respectively.
```

**Add citation:**
```latex
Additionally to the ventricles, UVCs are also calculated for the atria, 
to provide a system of coordinates defined on the volumetric mesh that 
facilitated the assignment of different tags within the mesh, and of 
boundary conditions for the pericardium. To achieve this, the left and 
the right atria were treated as an upside down single ventricle\added[id=SL]{, 
following the coordinate transformation approach described by~\cite{bayer2018}}, 
with the apex manually placed between the two right pulmonary veins and 
behind the superior vena cava, respectively.
```

**Alternative (if you want to clarify it's a geometric transformation, not physiological):**
```latex
\replaced[id=SL]{This geometric coordinate transformation, adapted from 
the ventricular UVC framework~\cite{bayer2018}, facilitates}{To achieve this, 
the left and the right atria were treated as an upside down single ventricle, 
with the apex manually placed...}
```

- [ ] Insert citation with tracked changes
- [ ] Verify Bayer 2018 citation exists in myrefs.bib

---

## Task 7: Compile and Cross-Check

After inserting all additions:

- [ ] **Compile with tracked changes visible**
  ```bash
  # Make sure preamble has:
  \usepackage[draft]{changes}
  
  pdflatex rootfile.tex
  bibtex rootfile
  pdflatex rootfile.tex
  pdflatex rootfile.tex
  ```

- [ ] **Verify all additions appear in blue**
  - Section 2 or 3.1: CT phase text
  - Section 3.1.2: FEM type, user control, CGAL details
  - Section 3.2: Mesh quality paragraph (from last session)
  - Section 3.2: Upside down ventricle citation
  - Section 3.2 or 3.3: Spatial alignment text

- [ ] **Check all cross-references work**
  - [ ] Bayer 2018 citation [33]
  - [ ] Neic 2020 meshtool citation [32]
  - [ ] Supplementary Material section reference

- [ ] **Verify no new compilation errors**

---

## Sprint 4 Deliverables

At the end of this sprint, you should have:

1. **Updated Methods section** with all R2 technical questions answered
2. **Tracked changes PDF** showing what was added (for review response)
3. **Updated `sprint0_mesh_quality_stats.txt`** with any new info from Tasks 1-2
4. **Git commit:**
   ```bash
   git add sections/methods.tex
   git commit -m "Sprint 4: Methods technical clarifications (R2-1 through R2-5, R1-Maj-2)"
   ```

---

## Time Breakdown (90 min total)

- Task 1 (CT phase): 15 min (10 min research, 5 min writing)
- Task 2 (FEM type): 10 min (5 min confirm, 5 min writing)
- Task 3 (Mesh quality): 5 min (already drafted, just insert)
- Task 4 (Alignment): 10 min (writing only)
- Task 5 (User control): 10 min (check Supp Material, write)
- Task 6 (Citation): 5 min (find sentence, add citation)
- Task 7 (Compile/check): 15 min
- **Buffer:** 20 min (for unexpected issues)

---

## Red Flags / When to Stop and Ask

**STOP if:**
- You cannot find documentation of CT acquisition phase (don't guess)
- Supplementary Material doesn't document CGAL parameters (need to add that first)
- Any insertion breaks compilation (check incrementally)

**ASK if:**
- Uncertain whether to put CT phase in Section 2 vs Section 3.1
- Unsure if spatial alignment description is accurate for your workflow
- Can't find the "upside down ventricle" sentence in your LaTeX

---

## What You're NOT Doing

- ❌ Rewriting existing Methods text (only surgical additions)
- ❌ Running new analyses (Sprint 0 data is sufficient)
- ❌ Adding new figures (that's Sprint 5)
- ❌ Changing Results or Discussion (those are later sprints)

This is **pure documentation** of technical details R2 needs to assess your methods credibility.