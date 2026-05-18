PLOS Computational Biology — Manuscript Upload Package
PCOMPBIOL-D-25-02375R1
========================================================

Self-contained set of source + deliverables for the main
manuscript. Every file uses the PLOS file-inventory naming
convention; the .tex \includegraphics calls reference the
figure files in this folder by their bare name (no extension
or path), so the package compiles standalone.

CONTENTS
--------
  manuscript.tex                                Flattened single-file LaTeX source.
  myrefs.bib                                    Bibliography.
  Fig1.pdf / Fig1.tif    Pipeline / cohort overview (Intro).
  Fig2.pdf / Fig2.tif    Multi-stage segmentation (Methods).
  Fig3.pdf / Fig3.tif    Meshing process (Methods).
  Fig4.pdf / Fig4.tif    Model creation (Methods).
  Fig5.pdf / Fig5.tif    Validation volumes vs UKBB (Results).
  Fig6.pdf / Fig6.tif    Cohen's d effect sizes (Results).
  plos_manuscript-final_formatting.pdf            Compiled final-mode PDF.
  plos_manuscript-final_formattingtracked_changes.pdf
                                                Tracked-changes PDF (PLOS edits visible).

FILE NAME MAPPING (legacy -> PLOS upload name)
---------------------------------------------
  pics/fig1_graphical_abstract.pdf            -> Fig1
  pics/fig2_methods-segmentation.pdf          -> Fig2
  pics/fig3_methods-meshing.pdf               -> Fig3
  pics/fig4_methods-model-creation.pdf        -> Fig4
  pics/fig6_results-validation-volumes-improved.pdf -> Fig5
  pics/fig7_cohen-big-effects.pdf             -> Fig6
  pics/fig5_hearts2.pdf                       -> moved to supplement_package/ as S1_Fig

COMPILATION (sanity check)
--------------------------
  pdflatex manuscript
  bibtex   manuscript
  pdflatex manuscript
  pdflatex manuscript

pdflatex picks Fig*.pdf via \DeclareGraphicsExtensions default
order; the .tif siblings satisfy the PLOS file inventory.

NOTES
-----
- This .tex contains tracked changes via the `changes` package
  (id=PLOS author, violet markup). To produce the clean
  publication version, set \finaltrue in rerun_mode.tex or run
  ./rerunpdf.sh -f manuscript from the repo root.
- Author-name corrections (Christoph Augustin, Shahrokh
  Rahmani) need to be applied in Editorial Manager — see
  ../em_author_comments.txt and ../author_contributions_reply.txt.
