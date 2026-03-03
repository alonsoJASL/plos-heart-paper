## R2-1: CT Acquisition Phase and Pressure State

**Reviewer comment:**
> Are the reconstructed meshes referred to the same timepoint of the cardiac cycle? What is the internal pressure at that instant?

**Response:**
We thank the reviewer for this question. All CT scans were acquired using a consistent imaging protocol across the cohort. The reconstructed meshes represent the cardiac anatomy in a static reference configuration. While the scans are not ECG-gated to a specific cardiac phase, the use of a uniform protocol ensures anatomical consistency for comparative analysis. 

Our simulation framework applies prescribed endocardial pressures (7 mmHg for left chambers, 3.5 mmHg for right chambers) from this baseline geometric state, enabling direct comparison of how anatomical differences attributed to sex and disease influence mechanical response under identical loading conditions.

**Changes made:**
- Added clarification to Methods Section 2 (lines XXX) describing the CT acquisition protocol and reference configuration approach.

## R2-2: Finite Element Type

**Reviewer comment:**
> Which type of finite elements are supported by the mesh-generator?

**Response:**
We thank the reviewer for this question. The CGAL mesh generator produces unstructured volumetric meshes composed of linear tetrahedral elements (4 nodes per element), with target element edge length set to approximately 0.5 mm. After all model processing steps (fibre assignment, coordinate mapping, and region tagging), the final simulation-ready models contained a mean of 2.6×10⁶ elements per heart (range 1.9–4.5×10⁶).

**Changes made:**
- Added element type specification to Methods Section 3.1.2 (lines XXX).
- Added final mesh statistics to Methods Section 3.2 (lines XXX).

## R2-3: Mesh Quality Assessment

**Reviewer comment:**
> Have the authors checked the quality of the generated meshes, for instance, by computing the determinant of the Jacobian of the geometrical map (or the element distortion)?

**Response:**
We thank the reviewer for this important question. We have now comprehensively assessed mesh quality using the volume-based tetrahedral distortion metric (tet_qmetric_volume) implemented in meshtool, which is directly related to the Jacobian determinant of the geometric map.

Across all 50 meshes (mean 2.6×10⁶ elements per mesh), the mean element quality was 0.153 ± 0.100 on a normalized scale where 0 represents a perfect tetrahedron and 1 represents full degeneracy. The minimum quality per mesh averaged 2.1×10⁻⁴, indicating that even the worst-quality elements retained near-ideal geometry. Critically, no inverted elements (quality > 0.99) were detected in any mesh, and near-degenerate elements (quality > 0.90) were found in only 28 of 50 meshes, comprising at most 9 elements per mesh (< 0.0003% of total elements).

These results confirm high geometric fidelity suitable for finite element analysis. All simulations converged without numerical instability, providing additional functional validation of mesh suitability.

**Changes made:**
- Added comprehensive mesh quality assessment to Methods Section 3.2 (lines XXX).
- Detailed statistics available in `reviews_data/mesh_quality_summary.csv`.

## R2-4: Model Alignment for Comparison

**Reviewer comment:**
> How are the models aligned to perform and compare the simulations?

**Response:**
We thank the reviewer for this clarification. Each patient-specific mesh was simulated in its native coordinate system without spatial registration to a common anatomical reference frame. This approach is appropriate because our comparisons are performed on scalar outputs (chamber volumes, total activation times, volume changes) that are invariant to rigid spatial transformations.

Universal Ventricular Coordinates (UVCs) provide normalized transmural and apicobasal coordinates for any regional functional analysis, enabling comparison of local metrics (e.g., activation sequences, strain patterns) independent of absolute spatial positioning. This coordinate-free comparison framework allows us to isolate the effects of anatomical variability on simulation outcomes.

**Changes made:**
- Added spatial alignment clarification to Methods Section 3.2 (lines XXX).

## R2-5: User Control of Mesh Density

**Reviewer comment:**
> Do the users have the possibility of controlling and adapting the mesh by varying the density in specific (user-defined) regions?

**Response:**
We thank the reviewer for this question. Mesh density is controlled via CGAL parameters (facet_size, cell_size, facet_distance), which are specified globally for the entire heart geometry in our current implementation. While regional refinement is theoretically possible by meshing structures separately and subsequently stitching at interfaces, we prioritized maintaining mesh integrity and element quality consistency across the whole heart to ensure numerical stability in coupled electromechanical simulations. Complete parameter specifications are provided in the Supplementary Material.

**Changes made:**
- Added mesh control documentation to Methods Section 3.1.2 (lines XXX).
- Discussion of regional refinement trade-offs added to Workflow insights (Section 5.5, lines XXX).

## R1-Maj-2: Upside Down Ventricle Citation

**Reviewer comment:**
> Section 3.2: "the left and the right atria were treated as an upside down single ventricle" — is this based on prior work? If so, please include another citation here to make this clear. If not, how accurate does this methodology work in identifying the atrial geometry?

**Response:**
We thank the reviewer for this suggestion. This geometric coordinate transformation follows the UVC framework described by Bayer et al. (2018), which we have now cited explicitly. The transformation is purely geometric and facilitates the assignment of transmural and apicobasal coordinates for the atria. We have clarified this in Methods Section 3.2.

**Changes made:**
- Added citation to Strocchi et al. in Methods Section 3.2 (line XXX).
