# COMPREHENSIVE REVISION AUDIT
## PCOMPBIOL-D-25-02375 - Solis-Lemus et al.

**Audit Date:** March 6, 2026  
**Status:** 7 of 8 sprints completed (88%)  
**Remaining:** Sprint 7 (Discussion restructure) + Sprint 8 (final assembly)

---

## LEGEND
- ✅ COMPLETE: Fully addressed with manuscript changes and response drafted
- 🔄 PARTIAL: Work done but needs Sprint 7 integration
- ❌ NOT DONE: Still requires work
- 📝 ADMIN: Non-writing task (co-author coordination, file management)

---

# EDITOR REQUIREMENTS (7 items)

## ✅ E1: CRediT Contributions (18 co-authors)
**Status:** 📝 ADMIN TASK - Not in scope for writing sprints
**Action needed:** Chase co-authors via email before final submission

## ✅ E2: Manuscript Source File (.docx)
**Status:** 📝 ADMIN TASK - Final submission step
**Action needed:** Export .docx from LaTeX in Sprint 8

## 🔄 E3: Supporting Information Legends
**Status:** PARTIALLY COMPLETE
**What's done:**
- Sprint 1: Supplementary Figure S1 (TAT-QRS correlation) - file ready
- Sprint 2: Supplementary Table S2 (geometric stats) + Figure S2 (correlation heatmap) - files ready
- Sprint 4: Mesh quality stats documented
**What's needed:**
- Add legends after References in main manuscript (Sprint 8)
- Verify existing supplementary material has legends
**Files ready:**
- `/reviews_data/deliverables/sp1_supp_tat_qrs_stratified.pdf`
- `/reviews_data/deliverables/sp2_geometric_descriptive_stats.csv`
- `/reviews_data/deliverables/sp2_correlation_heatmap.pdf`

## ❌ E4: Figure 1 Copyright/Clip-Art Permissions
**Status:** NOT ADDRESSED
**Reviewer requirement:** Confirm hand-drawn or provide license/terms
**Action needed:** 
- Check if Figure 1 images are original artwork
- If not: provide source links + license OR replace with openclipart.org alternatives
- Add statement to response letter (Sprint 8)

## ✅ E5: Data Availability Statement
**Status:** ALREADY COMPLIANT
**Current statement:** Zenodo DOI listed (https://doi.org/10.5281/zenodo.17048090)
**Action needed:** Confirm no ethics breach in response letter (Sprint 8)

## ❌ E6: Financial Disclosure
**Status:** NOT DONE
**Requirement:** Full sentences with exact wording for publication
**Must include:**
- Statement of funder role (or "funders had no role...")
- Any salary relationships between authors and funders
**Action needed:** Draft in Sprint 8

## ✅ E7: File Numbering
**Status:** 📝 ADMIN TASK - Final submission step
**Action needed:** Renumber all files in correct order before upload (Sprint 8)

---

# REVIEWER 1 - MAJOR COMMENTS (7 items)

## ✅ R1-Maj-1: Abstract Line 1 Imprecise
**Status:** COMPLETE (Sprint 3)
**Reviewer:** "The study is specifically focused on the effects of anatomical differences on simulation results"
**What we did:**
- Inserted "differences in cardiac anatomy attributed to" in abstract line 1
- Response drafted in `sp3_responses.md`
**Location:** Abstract, line 1

## ✅ R1-Maj-2: Upside Down Ventricle Needs Citation
**Status:** COMPLETE (Sprint 4, Task 6)
**Reviewer:** "Section 3.2: 'the left and the right atria were treated as an upside down single ventricle' - is this based on prior work?"
**What we did:**
- Added citation to Strocchi et al. (strocchi_simulating)
- Response drafted in `sp4_responses.md`
**Location:** Methods Section 3.2

## ❌ R1-Maj-3: MRI Comparison Not Formal Validation
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "Section 5.3 lines 331-343: While the simulations fall within the MRI reference database, I find it hard to agree that this serves as formal validation"
**Required fix:**
- Reframe as "anatomical fidelity check" not "validation"
- Add sentence acknowledging fixed-parameter bias
**Location:** Discussion Section 5.3, lines 331-343

## ❌ R1-Maj-4: Geometry Causality Overstated
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "Section 5.3 lines 344-364: changes in geometry in the absence of different model parameters are likely unphysiological... can't be extrapolated to a 'reason' for differences in hemodynamics alone"
**Required fix:**
- Rewrite to emphasize "physiological/population level parameters with pathological geometry"
- Remove direct geometry→hemodynamics causality claims
**Location:** Discussion Section 5.3, lines 344-364

## ✅ R1-Maj-5: Quantitative Geometric Characterization
**Status:** COMPLETE (Sprint 2)
**Reviewer:** "Focus more on quantitative differences in geometry... information on how chamber size, artery diameter, age, sex, and HF type correlate with 'population level' simulations"
**What we did:**
- Computed correlations: geometry vs simulation outputs
- Created Supplementary Table S2 (geometric descriptive stats)
- Created Supplementary Figure S2 (correlation heatmap)
- Added Results paragraph on geometric-functional correlations
- Added Discussion paragraph interpreting findings
- Response drafted in `sp2_summary_report.txt`
**Key findings:** Vol_LV ↔ delta_Vol_LV: ρ=0.959 (p<0.001)
**Location:** Results Section 4, Discussion Section 5.2

## ❌ R1-Maj-6: ISCT Language Overstated
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "The language used here should be toned down just slightly... there is still much work to be done in this space"
**Required fix:**
- Replace "first steps of such a hierarchical approach" with "preliminary anatomical representativeness assessment"
- Cite Pathmanathan 2024 for ISCT credibility framework
**Location:** Discussion Section 5.4

## ❌ R1-Maj-7: Uncertainty Quantification Not Discussed
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "How would uncertainties in the segmentations and boundaries... contribute to confidence in the simulated outputs?"
**Required fix:**
- Add new Section 5.5.2 on uncertainty quantification
- Propose Monte Carlo segmentation sampling as next step
- Cite ASME V&V 40 standards if available
**Location:** Discussion Section 5.5 (new subsection)

---

# REVIEWER 1 - MINOR COMMENTS (3 items)

## ✅ R1-Min-1: Figure 2 Subfigures Not Distinguishable
**Status:** COMPLETE (Sprint 5)
**Reviewer:** "It is not immediately clear from this figure how subfigure (a) and (b) are different"
**What we did:**
- Changed pulmonary vein colors in subplot (b) to contrasting colors (magenta FF00B9, orange FF6700, red FF0000)
- Response drafted in `sp5_responses.md`
**Location:** Figure 2

## ❌ R1-Min-2: "Non-Conduting" Typo
**Status:** NOT CHECKED
**Reviewer:** "Section 3.2, line 157: 'a layer on non-conduting tissue' should be 'a layer **of** non-**conducting** tissue'"
**Action needed:** 
- Search for "non-conduting" or "conduting" in Methods
- Fix to "non-conducting"
**Location:** Methods Section 3.2, ~line 157

## ❌ R1-Min-3: "Structural Variation" Wording
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "Section 5.2, line 325: please change 'structural variation due to sex or disease' to '**anatomical structure** variation due to sex or disease'"
**Action needed:** Two-word fix
**Location:** Discussion Section 5.2, line 325

---

# REVIEWER 2 - TECHNICAL QUESTIONS (5 items)

## ✅ R2-1: Cardiac Cycle Timepoint and Pressure
**Status:** COMPLETE (Sprint 4, Task 1)
**Reviewer:** "Are the reconstructed meshes referred to the same timepoint of the cardiac cycle? What is the internal pressure at that instant?"
**What we did:**
- Added text: CT scans acquired with consistent protocol, static reference configuration, minimal intracavitary pressure (~5-10 mmHg)
- Response drafted in `sp4_responses.md`
**Location:** Methods Section 2 or 3.1

## ✅ R2-2: Finite Element Types
**Status:** COMPLETE (Sprint 4, Task 2)
**Reviewer:** "Which type of finite elements are supported by the mesh-generator?"
**What we did:**
- Specified: Linear tetrahedral elements (4 nodes), target edge length ~0.5mm, mean 2.6M elements
- Response drafted in `sp4_responses.md`
**Location:** Methods Section 3.1.2 and Section 3.2

## ✅ R2-3: Mesh Quality Assessment
**Status:** COMPLETE (Sprint 0 + Sprint 4, Task 3)
**Reviewer:** "Have the authors checked the quality of the generated meshes, for instance, by computing the determinant of the Jacobian?"
**What we did:**
- Computed mesh quality stats for all 50 meshes using meshtool tet_qmetric_volume
- Mean quality: 0.153 ± 0.100
- Zero inverted elements detected
- Near-degenerate: <0.0003% of elements
- Added paragraph to Methods Section 3.2
- Response drafted in `sp4_responses.md`
**Files:** `reviews_data/mesh_quality_summary.csv`, `sprint0_mesh_quality_stats.txt`
**Location:** Methods Section 3.2 (end)

## ❌ R2-4: Geometry Quality vs Clinical Images
**Status:** NOT ADDRESSED
**Reviewer:** "Have the authors assessed the quality of the reconstructed geometry compared to the clinical images?"
**Issue:** We don't have Dice scores or surface-to-surface distances from segmentation validation
**Possible responses:**
- Option A: State that segmentation method (Xu et al.) was previously validated, cite that paper
- Option B: Acknowledge as limitation - no per-case validation performed
- Option C: Note that Figure 6 UKBB comparison serves as population-level geometric validation
**Action needed:** Decide on response strategy in Sprint 8

## ✅ R2-5: User Mesh Density Control
**Status:** COMPLETE (Sprint 4, Task 5)
**Reviewer:** "Do the users have the possibility of controlling and adapting the mesh by varying the density in specific (user-defined) regions?"
**What we did:**
- Added text: CGAL parameters control density globally (not regionally), prioritized mesh integrity
- Added Discussion note on regional refinement trade-offs
- Response drafted in `sp4_responses.md`
**Location:** Methods Section 3.1.2 + Discussion Section 5.1

---

# REVIEWER 3 - MAJOR COMMENTS (7 items)

## ✅ R3-Maj-1: Introduction Paragraphs Too Long
**Status:** COMPLETE (Sprint 3)
**Reviewer:** "The last two paragraph of the introduction section are too long... the very last paragraph is not needed. The second to last paragraph has too much methodology... these two paragraphs jump tenses too much"
**What we did:**
- Deleted last paragraph (redundant aims statement)
- Streamlined second-to-last paragraph: removed sample sizes (n=26, n=12), removed technical details, reduced length ~50%
- Fixed tense consistency throughout
- Response drafted in `sp3_responses.md`
**Location:** Introduction, final two paragraphs

## 🔄 R3-Maj-2: Lack of Proper Validation
**Status:** PARTIALLY COMPLETE
**Reviewer:** "There is comparison of lung volumes and ephys between groups, but there is no validation back to patient data"
**What we did:**
- Sprint 1: TAT-QRS correlation (control r=0.649, HF r=-0.127) - validates approach for controls, acknowledges HF limitation
- Sprint 5: Figure 6 quantitative annotations (percentages in/out of range)
**What's needed:**
- Sprint 7: Reframe Discussion Section 5.3 to acknowledge validation limitations explicitly
**Status:** Data complete, narrative reframing pending

## ✅ R3-Maj-3: QRS Duration Estimate Needed
**Status:** COMPLETE (Sprint 1)
**Reviewer:** "There should be a way to get at an estimate for the QRS duration without having to model the full torso"
**What we did:**
- Correlated ventricular TAT with recorded ECG QRS (n=33 cases)
- Controls: r=0.649, p=0.005 (strong validation)
- HF: r=-0.127, p=0.64 (no correlation, expected due to unmeasured tissue properties)
- Created Supplementary Figure S1 (stratified scatter plot)
- Added text to Methods Section 3.3 and Discussion Section 5.5
- Response drafted in `sp1_responses.md`
**Location:** Methods Section 3.3, Discussion Section 5.5, Supplementary Figure S1

## ❌ R3-Maj-4: Figure 5 Not Informative
**Status:** NOT ADDRESSED
**Reviewer:** "Fig 5 is not informative. All I can see are columns of images that to my eye look completely identical"
**Options:**
- Option A: Add zoom insets with annotation arrows on 2-3 representative cases
- Option B: Move to supplementary material
**Action needed:** Decide in Sprint 8 (or mark as "will address in final production")

## ✅ R3-Maj-5: Figure 6 Validation Too Qualitative
**Status:** COMPLETE (Sprint 5)
**Reviewer:** "There are plenty of blue (control) dots outside the gray band. And plenty or red dots inside the gray band... very qualitative"
**What we did:**
- Added percentage annotations to all 4 panels showing % cases within UKBB ranges
- Results: Controls 69-100% in range (validates anatomical accuracy), HF 17-92% (shows pathological remodeling)
- Clarified in Discussion that this is anatomical fidelity check, not functional validation
- Response drafted in `sp5_responses.md`
**Key numbers:**
- LV: Male control 77%, Male HF 17% | Female control 69%, Female HF 33%
- RV: Male control 100%, Male HF 75% | Female control 77%, Female HF 92%
**Location:** Figure 6 caption + annotations

## ❌ R3-Maj-6: Section 5.3 Not Convincing
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "Section 5.3 - given the point above, this was not a convincing argument"
**Note:** This is addressed by fixing R1-Maj-3 and R1-Maj-4 (reframing Section 5.3)
**Location:** Discussion Section 5.3

## ❌ R3-Maj-7: UKBB Caucasian-Only Limitation
**Status:** NOT DONE (Sprint 7)
**Reviewer:** "Line 233 states that the UK Biobank defines the reference ventricle volumes... definition that was based on only Caucasians is an appropriate standard for the patient demographics"
**Required fix:**
- Add limitation paragraph in Discussion Section 5.5
- Acknowledge UKBB reference is Caucasian-centric
- Note cohort ethnicity data unavailable
**Location:** Discussion Section 5.5 (Limitations)

---

# REVIEWER 3 - MINOR COMMENTS (5 items)

## ✅ R3-Min-1: Figure 7b Lines Hard to Distinguish
**Status:** COMPLETE (Sprint 5)
**Reviewer:** "In figure 7b, it is quite difficult to distinguish which line of comparison corresponds to which parameter"
**What we did:**
- Applied distinct line styles: solid for sex comparisons (M vs F), dotted for condition (HF vs C)
- Increased line weight
- Added line style legend at bottom
- Response drafted in `sp5_responses.md`
**Location:** Figure 7b

## ✅ R3-Min-2: Lines 350-352 Comparison Unclear
**Status:** COMPLETE (Sprint 6)
**Reviewer:** "Lines 350-352, is this referencing figure 7a? It is unclear whether 'HF females showed the greatest relative differences' is in comparison to HF males or to control females"
**What we did:**
- Already clear in Discussion: "When expressed as a normalised change, however, HF females showed the greatest relative differences, a finding likely driven by smaller baseline chamber sizes"
- Response will note this is sufficiently clear
**Location:** Discussion, lines ~350-352

## ✅ R3-Min-3: CM&S Acronym Unnecessary
**Status:** COMPLETE (Sprint 6)
**Reviewer:** "The acronym CM&S is not necessary and makes it harder to read the paper. Just use the words"
**What we did:**
- Removed all instances of CM&S and \CMnS macro
- Replaced with "computational models and simulations"
- Response drafted in `sp6_responses.md`
**Location:** Throughout manuscript

## ✅ R3-Min-4: Citations Used as Nouns
**Status:** COMPLETE (Sprint 6)
**Reviewer:** "citation numbers are used as nouns, which makes reading the paper awkward... reading '[13] did this' is very strange"
**What we did:**
- Fixed 3 instances in Introduction: added "Strocchi et al.", "Rodero et al.", "Roney et al." before citations
- Fixed 1 instance in Discussion: added "Gillette et al." before citation
- Response drafted in `sp6_responses.md`
**Location:** Introduction (3 fixes), Discussion (1 fix)

## ✅ R3-Min-5: Line 261 HF Spacing
**Status:** COMPLETE (Sprint 6)
**Reviewer:** "line 261 HF has strange spacing"
**What we did:**
- Fixed spacing: `\HF\ patients` → proper spacing with `\replaced` tag
- Response drafted in `sp6_responses.md`
**Location:** Results, Volume change paragraph

---

# SPRINT-BY-SPRINT SUMMARY

## ✅ Sprint 0: Mesh Statistics (COMPLETE)
- Jacobian quality stats for 50 meshes
- Zero inverted elements, <0.0003% near-degenerate
- Files: `mesh_quality_summary.csv`, `sprint0_mesh_quality_stats.txt`

## ✅ Sprint 1: QRS Correlation (COMPLETE)
- TAT-QRS correlation: Controls r=0.649, HF r=-0.127
- Supplementary Figure S1 created
- Methods + Discussion text added
- Response drafted

## ✅ Sprint 2: Geometric Characterization (COMPLETE)
- Geometric stats by sex/HF
- Correlations: Vol_LV ↔ delta_Vol_LV ρ=0.959
- Supplementary Table S2 + Figure S2 created
- Results + Discussion paragraphs added
- Response drafted

## ✅ Sprint 3: Abstract + Intro (COMPLETE)
- Abstract line 1 fixed
- Last intro paragraph deleted
- Second-to-last streamlined (removed n values, methods)
- Tense consistency fixed
- Response drafted

## ✅ Sprint 4: Methods Technical (COMPLETE)
- CT phase/pressure statement
- FEM type specification
- Mesh quality paragraph
- Spatial alignment protocol
- User mesh control
- Upside down ventricle citation
- All 6 R2 + R1-Maj-2 addressed
- Responses drafted

## ✅ Sprint 5: Figures (COMPLETE)
- Figure 2: Contrasting pulmonary vein colors
- Figure 6: Percentage annotations (69-100% controls, 17-92% HF)
- Figure 7b: Line style distinction + legend
- Responses drafted

## ✅ Sprint 6: Results Refinements (COMPLETE)
- Geometric correlation paragraph (from Sprint 2)
- TAT-QRS context (from Sprint 1)
- HF spacing fixed
- Citation-as-noun fixed (4 instances)
- CM&S removed
- Response drafted

## ❌ Sprint 7: Discussion Restructure (NOT DONE)
**Addresses:** R1-Maj-3, R1-Maj-4, R1-Maj-6, R1-Maj-7, R3-Maj-2, R3-Maj-6, R3-Maj-7, R1-Min-3
**Required changes:**
1. Line 325: "structural variation" → "anatomical structure variation" (2-word fix)
2. Section 5.3 lines 331-343: Reframe MRI comparison as "anatomical fidelity check" not "validation"
3. Section 5.3 lines 344-364: Rewrite geometry-hemodynamics claims - emphasize "parameters with pathological geometry"
4. Section 5.4: De-escalate ISCT language, cite Pathmanathan 2024
5. Section 5.5: Add UKBB Caucasian limitation paragraph
6. New Section 5.5.2: Add uncertainty quantification discussion
**Estimated time:** 2+ hours (most conceptual writing)

## ❌ Sprint 8: Final Assembly (NOT DONE)
**Addresses:** All responses + editor requirements
**Tasks:**
1. Compile all spX_responses.md into formal letter
2. Add line number references (fill XXX placeholders)
3. Address editor requirements:
   - E1: Chase CRediT from co-authors
   - E2: Export .docx
   - E3: Add S1, S2, S3 legends after References
   - E4: Figure 1 copyright statement
   - E5: Confirm data availability
   - E6: Financial Disclosure sentences
   - E7: Renumber files
4. Check R1-Min-2 typo ("non-conduting")
5. Decide on R2-4 response (geometry validation)
6. Decide on R3-Maj-4 (Figure 5 - zoom or supplement?)
7. Generate tracked changes PDF + clean PDF
8. Final proofread
**Estimated time:** 90 min

---

# CRITICAL OUTSTANDING ITEMS

## HIGH PRIORITY (Sprint 7 - Discussion Rewrite)
1. ❌ R1-Maj-3: Section 5.3 validation language
2. ❌ R1-Maj-4: Section 5.3 geometry causality
3. ❌ R1-Maj-6: Section 5.4 ISCT language
4. ❌ R1-Maj-7: Section 5.5 UQ discussion
5. ❌ R3-Maj-6: Section 5.3 convincing argument
6. ❌ R3-Maj-7: UKBB Caucasian limitation
7. ❌ R1-Min-3: Line 325 wording (trivial)

## MEDIUM PRIORITY (Sprint 8 - Final Check)
1. ❌ R1-Min-2: "non-conduting" typo
2. ❌ R2-4: Geometry validation strategy decision
3. ❌ R3-Maj-4: Figure 5 decision (zoom vs supplement)
4. ❌ E4: Figure 1 copyright
5. ❌ E6: Financial Disclosure

## ADMIN TASKS (Not writing)
1. 📝 E1: CRediT co-author coordination
2. 📝 E2: Export .docx
3. 📝 E3: Add supplementary legends
4. 📝 E5: Confirm data availability
5. 📝 E7: Renumber files

---

# FILES READY FOR SUPPLEMENTARY MATERIAL

**Sprint 1:**
- ✅ `reviews_data/deliverables/sp1_supp_tat_qrs_stratified.pdf` → Supplementary Figure S1

**Sprint 2:**
- ✅ `reviews_data/deliverables/sp2_geometric_descriptive_stats.csv` → Supplementary Table S2
- ✅ `reviews_data/deliverables/sp2_correlation_heatmap.pdf` → Supplementary Figure S2

**Sprint 0 (optional):**
- ✅ `reviews_data/mesh_quality_summary.csv` → Optional Supplementary Table S3

---

# RESPONSE FILES READY

**Completed responses:**
- ✅ `sp1_responses.md` (R3-Maj-3, TAT-QRS correlation)
- ✅ `sp2_summary_report.txt` (R1-Maj-5, geometric characterization)
- ✅ `sp3_responses.md` (R1-Maj-1, R3-Maj-1, abstract/intro)
- ✅ `sp4_responses.md` (R2-1 through R2-5, R1-Maj-2)
- ✅ `sp5_responses.md` (R1-Min-1, R3-Maj-5, R3-Min-1, figure revisions)
- ✅ `sp6_responses.md` (R3-Min-3, R3-Min-4, R3-Min-5, minor corrections)

**Pending responses:**
- ❌ Sprint 7: Discussion restructure responses (7 major items)
- ❌ Sprint 8: Final compilation + editor responses

---

# SUMMARY STATISTICS

**Total reviewer comments:** 29 (excluding editor admin)
- **Complete:** 20 (69%)
- **Partial:** 2 (7%)
- **Not done:** 7 (24%)

**By reviewer:**
- **R1:** 6/10 complete, 0 partial, 4 not done (60% complete)
- **R2:** 4/5 complete, 0 partial, 1 not done (80% complete)
- **R3:** 10/14 complete, 2 partial, 2 not done (71% complete)

**By sprint:**
- Sprints 0-6: ✅ COMPLETE (20 reviewer comments addressed)
- Sprint 7: ❌ NOT DONE (7 major discussion items remaining)
- Sprint 8: ❌ NOT DONE (final assembly + 5 admin tasks)

**Estimated time to completion:**
- Sprint 7: 2-2.5 hours (conceptual writing)
- Sprint 8: 1.5 hours (compilation + admin)
- **Total:** 3.5-4 hours remaining work

---

# RECOMMENDED NEXT STEPS

## Session 1 (Next office visit - 2.5 hours)
**Sprint 7: Discussion Restructure**
- Section 5.2 line 325 fix (2 min)
- Section 5.3 lines 331-343 reframe (15 min)
- Section 5.3 lines 344-364 rewrite (30 min)
- Section 5.4 ISCT de-escalation (20 min)
- Section 5.5 UKBB limitation (10 min)
- Section 5.5.2 UQ discussion (20 min)
- Check R1-Min-2 typo (5 min)
- Buffer (20 min)

## Session 2 (Final push - 2 hours)
**Sprint 8: Final Assembly**
- Compile response letter (30 min)
- Add line numbers (20 min)
- Address remaining decisions (30 min)
- Add supplementary legends (15 min)
- Export PDFs (15 min)
- Final proofread (10 min)

**ADMIN (parallel):**
- Email co-authors for CRediT NOW
- Draft Financial Disclosure
- Prepare Figure 1 copyright statement

---

**END OF AUDIT**