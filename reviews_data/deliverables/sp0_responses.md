## Draft Response to Reviewer 2 Question 3
We thank the reviewer for this important question. We have now assessed 
mesh quality comprehensively using the volume-based tetrahedral distortion 
metric (tet_qmetric_volume) implemented in meshtool, which is directly 
related to the Jacobian determinant of the geometric map. 

Across all 50 meshes (mean 2.6×10⁶ elements per mesh), the mean element 
quality was 0.153 ± 0.100 on a normalised scale where 0 represents a 
perfect tetrahedron and 1 represents full degeneracy. The minimum quality 
per mesh averaged 2.1×10⁻⁴, indicating that even the worst-quality elements 
retained near-ideal geometry. Critically, no inverted elements (quality > 
0.99) were detected in any mesh, and near-degenerate elements (quality > 
0.90) were found in only 28 of 50 meshes, comprising at most 9 elements 
per mesh (< 0.0003% of total elements).

These results confirm that the meshes are of high geometric quality. All 
simulations converged without numerical instability, providing additional 
functional validation of mesh suitability. We have added these metrics to 
Methods Section 3.1.2 (lines XXX-XXX).