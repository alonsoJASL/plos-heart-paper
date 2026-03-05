## R1-Maj-5: Quantitative Geometric Characterization

**Reviewer comment:**
> I feel that this article could really provide some foundational insight by 
> focusing more on quantitative differences in geometry with sex and HF type, 
> and then linking this to what is observed in the simulated outputs. For 
> instance, information on how chamber size, artery diameter, age, sex, and HF 
> type correlate with "population level" simulations using a common set of 
> parameters might be more useful...

**Response:**
We thank the reviewer for this excellent suggestion. We have now performed a 
comprehensive geometric characterization analysis, stratifying chamber volumes, 
mesh element counts, and age by sex and heart failure status (Supplementary 
Table S2). 

We computed Spearman correlations between all geometric variables and simulation 
outputs, identifying strong relationships between anatomy and function 
(Supplementary Figure S2). Key findings include:

- Chamber volume strongly predicted volume change during inflation (ρ = 0.96 for 
  LV, p < 0.001), indicating anatomical size dominates mechanical response under 
  uniform material properties.
- Mesh element count (reflecting anatomical size) strongly correlated with 
  activation times (ρ = 0.87 for right ventricle, p < 0.001), consistent with 
  path length governing conduction duration.
- Cross-chamber correlations emerged (e.g., RV volume predicting LV activation 
  time, ρ = 0.81), demonstrating whole-heart anatomical coupling.

These correlations validate our parameter standardization approach for isolating 
anatomical effects, while also clarifying that patient-specific predictions would 
require tissue property calibration.

**Changes made:**
- Added Supplementary Table S2: Geometric characteristics by sex/condition.
- Added Supplementary Figure S2: Correlation heatmap (geometry vs simulation).
- Added Results paragraph on geometric-functional correlations (lines XXX-XXX).
- Added Discussion paragraph interpreting these findings (lines XXX-XXX).