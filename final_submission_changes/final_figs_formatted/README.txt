PLOS Computational Biology — Final Figure File Inventory
PCOMPBIOL-D-25-02375R1
==========================================================

This folder holds the figures renamed to the PLOS file-inventory
convention (Fig1.tif, S1_Fig.tif, ...). The numbering reflects
the post-FTC manuscript, in which the cohort overview figure
(previously Fig 5 in the main text) has been relocated to the
supplement as S1 Fig per reviewer request.

MAIN MANUSCRIPT FIGURES
-----------------------
  Fig1.tif  <-  pics_formatted/fig1_graphical_abstract.tif
                (Heartbuilder pipeline / cohort overview, Intro)
  Fig2.tif  <-  pics_formatted/fig2_methods-segmentation.tif
  Fig3.tif  <-  pics_formatted/fig3_methods-meshing.tif
  Fig4.tif  <-  pics_formatted/fig4_methods-model-creation.tif
  Fig5.tif  <-  pics_formatted/fig6_results-validation-volumes-improved.tif
                (was Fig 6 before fig:hearts moved to supplement)
  Fig6.tif  <-  pics_formatted/fig7_cohen-big-effects.tif
                (was Fig 7 before fig:hearts moved to supplement)

SUPPORTING INFORMATION FIGURES
------------------------------
  S1_Fig.tif <- pics_formatted/fig5_hearts2.tif
                (Whole-heart cohort reconstructions; moved from main)
  S2_Fig.tif <- pics/sp1_supp_tat_qrs_stratified.pdf
                (re-rasterised here at 300 dpi LZW)
  S3_Fig.tif <- pics/sp2_correlation_heatmap.pdf
                (re-rasterised here at 300 dpi LZW)
  S4_Fig.tif <- pics/sp0_supp_mesh_quality_dist.pdf
                (re-rasterised here at 300 dpi LZW)

OTHER SUPPORTING INFORMATION (not in this folder)
-------------------------------------------------
The following live in supplementary/ at the project root and are
already PLOS-compliant filenames:

  S1_Data_mesh_quality.csv
  S2_Data_summary.xlsx
  S3_Data_anova.xlsx
  S4_Data_posthoc.xlsx
  S5_Data_geometric_stats.csv
  S6_Data_correlation.csv

(PLOS guidance says the file-inventory entry should be exactly
"S1_Data.xlsx" etc.; the descriptive suffixes above identify the
content of each data file. Either upload as-is and rely on the
file-inventory descriptions, or rename to bare S1_Data.* etc.
before upload.)

S1 Tables and S1 Text are embedded in plos_supplement.pdf
(single SI deliverable, per the FTC instructions).

NOTES
-----
- File specs: TIFF, 300 dpi, LZW compression, 8-bit depth, max
  2250x2625 px. Generated via process_figs.sh for main figs;
  re-generated with the same magick invocation for the SI figs.
- Both Christoph Augustin and Shahrokh Rahmani name corrections
  are flagged in em_author_comments.txt and the separate
  author_contributions_reply.txt email.
