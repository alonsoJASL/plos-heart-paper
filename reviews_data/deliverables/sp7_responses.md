# Sprint 7 Responses: Discussion Restructure

---

## R1-Min-2, R1-Min-3: Minor Editorial Corrections

**Reviewer comments:**
> R1-Min-2: Section 3.2, line 157: "a layer on non-conduting tissue" should be "a layer of non-conducting tissue"
> R1-Min-3: Section 5.2, line 325: "structural variation" should be "anatomical structure variation"

**Response:**
We thank the reviewer for these corrections. Both typographical errors have been fixed.

**Changes made:**
- Methods Section 3.2, line XXX: Corrected "non-conduting" → "non-conducting"
- Discussion Section 5.2, line XXX: Corrected "structural variation" → "anatomical structure variation"

---

## R1-Maj-3: MRI Comparison Not Formal Validation

**Reviewer comment:**
> Section 5.3 lines 331-343: While the simulations fall within the MRI reference database, I find it hard to agree that this serves as formal validation. Since the model parameters have been set the same for both sex and heart failure types, the simulated volumes are biased towards these "generalized" parameters.

**Response:**
We thank the reviewer for this important clarification. We have reframed the UKBB comparison as an "anatomical fidelity check" rather than functional validation. We now explicitly state that because mechanical simulations used uniform material properties, the observed volumes represent anatomical structure rather than patient-specific functional state. This comparison validates our reconstruction pipeline's ability to capture population-level anatomical distributions, not patient-specific hemodynamic function.

**Changes made:**
- Discussion Section 5.3, lines XXX-XXX: Replaced "validation" with "anatomical fidelity check," added explicit statement about uniform material properties limiting functional interpretation.

---

## R1-Maj-4: Geometry Causality Overstated

**Reviewer comment:**
> Section 5.3 lines 344-364: While I agree that the effect of geometry is definitely influential, as shown here, I don't believe that this indicates geometry as a definitive factor in altering hemodynamics with HF... changes in geometry in the absence of different model parameters are likely unphysiological in comparison to subject-specific data.

**Response:**
We thank the reviewer for this critical feedback. We have substantially revised this paragraph to eliminate causality claims and reframe our findings appropriately. The revised text emphasizes that we applied "population-level material properties to pathological geometries" rather than claiming geometry alone drives hemodynamic changes. We now explicitly state that individual patient predictions would require tissue-specific parameter calibration, while our results demonstrate that population-level simulations with anatomically accurate models can reproduce group-level clinical patterns.

**Changes made:**
- Discussion Section 5.3, lines XXX-XXX: Complete paragraph rewrite removing geometry-to-hemodynamics causality language, emphasizing "population-level parameters with pathological geometry" framing, adding explicit statement that patient-specific predictions require tissue property calibration.

---

## R1-Maj-6: ISCT Language Overstated

**Reviewer comment:**
> Section 5.4: I think the authors need to be careful in stating that the study is "the first steps of such a hierarchical approach, by assessing cohort representativeness..." The cohort itself, though, does not represent cardiac function at the level needed for an ISCT... the language used here should be toned down just slightly to make it clear that there is still much work to be done in this space.

**Response:**
We thank the reviewer for this important perspective. We have revised Section 5.4 to replace "first steps of such a hierarchical approach" with "preliminary assessment of anatomical representativeness." We now explicitly acknowledge that full validation for in silico clinical trials would require additional hierarchical evaluation steps, including patient-specific functional validation, uncertainty quantification, and context-specific device or drug interaction studies. We have cited Pathmanathan et al. (2024) to provide the appropriate ISCT credibility framework.

**Changes made:**
- Discussion Section 5.4, lines XXX-XXX: De-escalated ISCT language, added explicit acknowledgment of required future validation steps, cited Pathmanathan 2024 credibility framework.

---

## R3-Maj-2, R3-Maj-6: Lack of Validation

**Reviewer comments:**
> R3-Maj-2: The main issue with the paper is lack of proper validation. There is comparison of lung volumes and ephys between groups, but there is no validation back to patient data.
> R3-Maj-6: Section 5.3 - given the point above, this was not a convincing argument.

**Response:**
We thank the reviewer for this feedback. We have addressed this concern through multiple revisions:

1. **Anatomical validation reframed (R1-Maj-3 response):** Section 5.3 now explicitly describes the UKBB comparison as an "anatomical fidelity check" rather than functional validation, acknowledging the limitations of uniform parameters.

2. **QRS surrogate validation added (Sprint 1):** We correlated simulated ventricular TAT with recorded ECG QRS duration (n=33 cases). In control hearts, strong correlation (r=0.649, p=0.005) validates TAT as a QRS surrogate when anatomical variability dominates. In HF patients, no correlation (r=-0.127, p=0.64) reflects unmeasured pathological tissue properties, which we acknowledge as a limitation.

3. **Quantitative Figure 6 improvements (Sprint 5):** Added percentage annotations showing 69-100% of controls within UKBB ranges (validates anatomical accuracy) versus 17-92% of HF cases (shows expected pathological remodeling).

Together, these revisions acknowledge validation limitations while demonstrating that our approach successfully isolates anatomical effects and captures population-level patterns.

**Changes made:**
- Discussion Section 5.3: Complete reframe as described in R1-Maj-3 response
- Methods Section 3.3 + Discussion Section 5.5: TAT-QRS validation analysis and limitation acknowledgment
- Figure 6: Quantitative percentage annotations

---

## R3-Maj-7: UKBB Caucasian-Only Limitation

**Reviewer comment:**
> Line 233 states that the UK Biobank defines the reference ventricle volumes. It is unclear whether this definition that was based on only Caucasians is an appropriate standard for the patient demographics in this study.

**Response:**
We thank the reviewer for raising this important limitation. We have added a paragraph to the Limitations section (5.5) explicitly acknowledging that the UKBB reference ranges were derived from a predominantly Caucasian population, which may limit generalizability across diverse ethnic backgrounds. We note that our cohort lacks systematic ethnicity data, preventing stratified analysis, and propose that future work should incorporate ethnicity-specific reference ranges or population-matched controls.

**Changes made:**
- Discussion Section 5.5 (Limitations): Added new paragraph on UKBB Caucasian-centric reference range limitation, lines XXX-XXX.

---

## R1-Maj-7: Uncertainty Quantification Discussion

**Reviewer comment:**
> Section 5.5 and 5.5.1 (general): Since this article shows that anatomical differences with fixed parameters leads to statistically significant differences in simulation results, I believe the authors should discuss the role of uncertainty quantification a bit more here. How would uncertainties in the segmentations and boundaries of the cardiac and vascular geometries contribute to confidence in the simulated outputs? Given this advanced workflow (which we desperately need in our community), it seems like the next necessary step is addressing uncertainty in model geometry, and quantifying this at the forefront.

**Response:**
We thank the reviewer for this excellent suggestion. We have added a new Section 5.5.2 on Uncertainty Quantification to address this important topic. We acknowledge that while our prior work has assessed reproducibility for left atrial models (Solís-Lemus et al., 2023), whole-heart models present substantially greater complexity with four chambers, multiple vessel junctions, and valve planes that may amplify uncertainty propagation.

We propose a Monte Carlo sampling approach to quantify reconstruction uncertainty, involving systematic perturbation of myocardial boundaries within image resolution bounds (±1-2mm) and ensemble simulation to establish confidence intervals on predicted activation times and mechanical responses. This methodology aligns with verification, validation, and uncertainty quantification (VVUQ) frameworks increasingly adopted for computational model credibility assessment in regulatory contexts.

We frame this as a critical next step that would extend our prior single-chamber reproducibility analysis to the multi-chamber whole-heart case, strengthening the credibility of virtual cohorts for in silico clinical trial applications.

**Changes made:**
- Added new Discussion Section 5.5.2 "Uncertainty Quantification" (lines XXX-XXX), proposing Monte Carlo UQ methodology and citing our prior reproducibility work and VVUQ frameworks.