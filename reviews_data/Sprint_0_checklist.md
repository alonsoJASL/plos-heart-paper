# Sprint 0: Mesh Statistics Collection (30 min)

**Goal:** Collect technical mesh quality metrics required to answer Reviewer 2's questions before writing any Methods text.

**Addresses:** R2-1, R2-2, R2-3 (data collection only)

**Why this is Sprint 0:** These numbers gate Sprint 4 (Methods rewrite). If Jacobian stats are problematic, you need to know NOW before drafting the response.

**Calculate and record:**
- [X] Task 1: Jacobian statistics collected ✓ (meshtool volume metric)
- [X] Task 2: FEM type confirmed (need to add: linear tetrahedra)
- [ ] Task 3: Cardiac cycle phase (still need CT metadata)
- [ ] Task 4: Spatial alignment protocol (document UVC approach)
- [X] Task 5: User mesh control (CGAL parameters documented in Supp)
- [ ] Task 6: Geometry validation (if Dice scores exist, add them)

---

## Checklist

### Task 1: Jacobian Determinant Statistics

**What R2 wants:** Evidence that mesh quality was checked via Jacobian determinant or element distortion metrics.

**What you need:**
- [X] Locate output mesh files from pipeline (`.elem`, `.pts`, `.lon` or similar format)
- [X] Determine mesh format compatibility with quality tools

**Code/Tools:**
- [X] Check if meshtool has Jacobian calculation built-in (`meshtool query quality`)

**Output:** Create `mesh_quality_stats.txt` in repo with:

---

### Task 2: Finite Element Type Confirmation

**What R2 wants:** Which type of finite elements are supported by the mesh-generator?

**What you need:**
- [ ] Check CGAL meshing output format
  ```bash
  # Look at one mesh file header
  head -20 /path/to/output_mesh.elem
  ```
- [ ] Confirm element type from meshtool documentation or mesh file structure
  - Linear tetrahedra (4 nodes per element)?
  - Quadratic tetrahedra (10 nodes per element)?
  - Other?

- [ ] Check CARP simulation logs for element type confirmation
  ```bash
  grep -i "element" /path/to/simulation.log | head -5
  ```

- [ ] Record typical element edge length statistics
  ```bash
  # If meshtool has this:
  meshtool query meshdata -msh=output_mesh -metric=edge_lengths
  ```
  Or calculate from mesh coordinates:
  - [ ] Mean edge length: X.X mm
  - [ ] Min edge length: Y.Y mm  
  - [ ] Max edge length: Z.Z mm

**Output:** Add to `mesh_quality_stats.txt`:
```
Finite Element Type:
  Type: Linear tetrahedral elements
  Nodes per element: 4
  
Element Size:
  Mean edge length: X.XX ± Y.YY mm
  Min: Z.ZZ mm
  Max: W.WW mm
  Target resolution: 0.5 mm (from CGAL parameters)
```

---

### Task 3: Cardiac Cycle Phase Confirmation

**What R2 wants:** Are the reconstructed meshes referred to the same timepoint of the cardiac cycle? What is the internal pressure at that instant?

**What you need:**
- [ ] Check CT scan acquisition protocol documentation
  - [ ] Locate DICOM headers or scan metadata
  - [ ] Confirm acquisition phase: end-diastolic / end-systolic / other
  - [ ] Record trigger method: ECG-gated? Retrospective? Prospective?

- [ ] Check if phase is documented in UK Biobank imaging protocol
  ```bash
  # Search your notes/documentation
  grep -i "cardiac phase\|diastole\|systole" /path/to/ukbb_protocol.pdf
  ```

- [ ] Determine internal pressure at that phase
  - [ ] End-diastolic: ~5-10 mmHg LV, ~3-5 mmHg RV (passive filling, minimal pressure)
  - [ ] End-systolic: ~120 mmHg LV, ~25 mmHg RV (peak contraction)
  - [ ] If unknown: state "unloaded reference configuration, minimal ventricular pressure"

**Output:** Add to `mesh_quality_stats.txt`:
```
CT Acquisition Phase:
  Timepoint: End-diastolic (minimal ventricular volume)
  Trigger method: [ECG-gated / other]
  Internal pressure: ~5-10 mmHg LV, ~3-5 mmHg RV (passive filling)
  
Mesh Alignment:
  All meshes reconstructed from same cardiac phase
  No spatial alignment required (each anatomy uses intrinsic coordinate system)
```

---

### Task 4: Mesh Spatial Alignment Protocol

**What R2 wants:** How are the models aligned to perform and compare the simulations?

**What you need:**
- [ ] Confirm whether meshes were spatially registered to a common coordinate system
  - [ ] If YES: document registration method (landmark-based? image registration?)
  - [ ] If NO: document that each simulation uses the anatomy's native coordinate system

- [ ] Check if UVC (Universal Ventricular Coordinates) provide implicit alignment
  - [ ] UVCs create normalized coordinates (apex=0, base=1) independent of absolute position
  - [ ] This allows functional comparison without rigid spatial alignment

**Output:** Add to `mesh_quality_stats.txt`:
```
Spatial Alignment:
  Method: None - each anatomy simulated in native coordinate system
  Comparison basis: Universal Ventricular Coordinates (UVCs) provide 
                    normalized functional coordinates for regional analysis
  Statistical comparison: Performed on scalar outputs (volumes, activation times)
                         which are alignment-invariant
```

---

### Task 5: User Mesh Control Documentation

**What R2 wants:** Do users have the possibility of controlling and adapting the mesh by varying the density in specific (user-defined) regions?

**What you need:**
- [ ] Review CGAL parameters in Supplementary Material
- [ ] Identify which parameters control mesh density:
  - [ ] Facet angle
  - [ ] Facet size
  - [ ] Facet distance
  - [ ] Cell size
  - [ ] Cell radius-edge ratio

- [ ] Document whether parameters can be set regionally or only globally

**Output:** Add to `mesh_quality_stats.txt`:
```
User Mesh Control:
  Global refinement: Yes via CGAL parameters (facet_size, cell_size)
  Regional refinement: Yes via facet_size and cell_size targets in user-defined regions
  Parameter location: Detailed in Supplementary Material Section X
  Typical settings used: facet_size=0.5mm, cell_size=0.5mm (see Supp. Table SX)
```

---

### Task 6: Geometry Validation Against Clinical Images (if available)

**What R2 wants:** Have the authors assessed the quality of the reconstructed geometry compared to the clinical images?

**What you need (if metrics exist):**
- [ ] Check if segmentation validation was performed during pipeline development
  - [ ] Dice coefficient between auto-segmentation and manual?
  - [ ] Surface-to-surface distance metrics?
  - [ ] Volume comparison?

- [ ] If validation exists: extract metrics and add to file
- [ ] If validation doesn't exist: document as future work and note qualitative assessment was done

**Output:** Add to `mesh_quality_stats.txt`:
```
Geometry Validation:
  Method: [Dice coefficient / surface distance / qualitative review]
  Metrics: [If available: Dice = 0.XX ± 0.YY for chamber X]
  
  If not available:
  Method: Qualitative visual inspection during segmentation post-processing
  Quality control: Manual correction of anatomically implausible regions
  Note: Quantitative validation against manual segmentation planned for future work
```

---

## Final Deliverable

- [ ] Create and commit `mesh_quality_stats.txt` to repo
  ```bash
  git add mesh_quality_stats.txt
  git commit -m "Sprint 0: Mesh quality statistics for R2 response"
  ```

- [ ] Review numbers with critical eye:
  - [ ] Are any Jacobian values suspiciously low/high?
  - [ ] Do inverted elements exceed 1%? (If yes, flag for discussion)
  - [ ] Are element sizes consistent with target resolution?

- [ ] If numbers are problematic:
  - [ ] Document honestly in the file
  - [ ] Note correction attempts made
  - [ ] Plan Sprint 4 Methods text to acknowledge limitations

---

## Time Estimate

- **If tools exist:** 20-30 minutes (run scripts, collect output)
- **If tools need creation:** 60-90 minutes (write Jacobian calculator, validate)
- **Fallback:** If Jacobian calculation proves difficult, document what quality checks WERE performed (visual inspection, simulation convergence) and commit to implementing formal metrics in future pipeline versions

---

## Red Flags

**STOP and reassess if:**
- More than 5% of elements are inverted across the cohort
- Mean Jacobian is below 0.3 (indicates highly distorted elements)
- You cannot locate the output meshes from the pipeline

In these cases, the response strategy changes from "here are our metrics" to "here's why we're confident despite not having formal Jacobian analysis" (simulation convergence, qualitative inspection, clinical plausibility of results).

---

## Next Step

Once `mesh_quality_stats.txt` is committed, you can proceed to Sprints 1-2 (parallel track) or Sprint 3-4 (writing track). The numbers from this file will be copy-pasted directly into the Methods section during Sprint 4.