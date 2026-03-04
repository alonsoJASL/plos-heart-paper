## R3-Maj-3: QRS Duration Surrogate

**Reviewer comment:**
> There should be a way to get at an estimate for the QRS duration without 
> having to model the full torso. This is really needed to allow the work to 
> be validated against physiological data.

**Response:**
We thank the reviewer for this suggestion. We have now performed a correlation 
analysis between simulated ventricular total activation time (TAT) and recorded 
ECG QRS duration in the subset of cases with available ECG data (n=33 of 50).

In control hearts, TAT showed a strong positive correlation with QRS duration 
(Pearson r = 0.649, p = 0.005), demonstrating that TAT serves as a valid 
surrogate for QRS duration when anatomical variability is the primary driver of 
conduction differences. This validates our approach for the control cohort.

In heart failure patients, no correlation was observed (r = -0.127, p = 0.64). 
This is consistent with the known influence of pathological tissue properties 
(fibrosis, scar, conduction blocks) that are not represented in our standardized 
parameter set. This finding reinforces that our study isolates anatomical effects 
specifically, and highlights the need for patient-specific tissue property 
calibration to predict QRS in diseased hearts.

**Changes made:**
- Added TAT-QRS correlation analysis to Results (lines XXX).
- Added limitation discussion to Section 5.5 (lines XXX).
- Added Supplementary Figure S1 showing stratified correlation.