PLOS Computational Biology — Supplement Upload Package
PCOMPBIOL-D-25-02375R1
========================================================

Self-contained set of source + deliverables for the
Supporting Information. Every file uses the PLOS file-inventory
naming convention; the .tex \includegraphics calls reference
the figure files in this folder by their bare name, so the
package compiles standalone.

CONTENTS
--------
  supplement.tex                              Flattened single-file LaTeX source.
  myrefs.bib                                  Bibliography (cites resolve here).
  S1_Fig.pdf / S1_Fig.tif    Whole-heart cohort reconstructions
                             (moved from main per reviewer).
  S2_Fig.pdf / S2_Fig.tif    TAT-QRS correlation, stratified by condition.
  S3_Fig.pdf / S3_Fig.tif    Geometry-output correlation matrix.
  S4_Fig.pdf / S4_Fig.tif    Mesh quality distribution.
  S1_Data_mesh_quality.csv   Per-model mesh quality statistics (all 50 hearts).
  S2_Data_summary.xlsx       Summary stats for geometric/simulation outputs.
  S3_Data_anova.xlsx         ANOVA results for all outputs.
  S4_Data_posthoc.xlsx       Pairwise post-hoc comparisons (FDR-corrected).
  S5_Data_geometric_stats.csv  Descriptive statistics by group.
  S6_Data_correlation.csv    Spearman correlations between geometric and
                             simulation variables.
  plos_supplement_final_formatting.pdf
                             Compiled final-mode SI PDF (the single
                             SI deliverable per FTC choice; embeds
                             S1 Table, S2 Table, S3 Table, S1 Text).

FILE NAME MAPPING (legacy -> PLOS upload name)
---------------------------------------------
  pics/fig5_hearts2.pdf                  -> S1_Fig  (moved from main manuscript)
  pics/sp1_supp_tat_qrs_stratified.pdf   -> S2_Fig  (was S1 Fig before reorder)
  pics/sp2_correlation_heatmap.pdf       -> S3_Fig  (was S2 Fig before reorder)
  pics/sp0_supp_mesh_quality_dist.pdf    -> S4_Fig  (was S3 Fig before reorder)

  S Tables and S1 Text are embedded in plos_supplement_final_formatting.pdf;
  components inside that PDF are labelled "Table A in S1 Text"
  style per PLOS guidance for combined-SI PDFs.

COMPILATION (sanity check)
--------------------------
  pdflatex supplement
  bibtex   supplement
  pdflatex supplement
  pdflatex supplement

pdflatex picks the PDF figs; the .tif siblings satisfy the
PLOS file inventory.

NOTES
-----
- supplement.tex uses \externaldocument{manuscript} and
  \externaldocument{sections/methods}; cross-references to
  main-manuscript labels will compile to "??" when building the
  package standalone (it doesn't have the main aux files).
  This is harmless for the typesetters; the final PDF in this
  folder was built against the full project where refs resolve.
