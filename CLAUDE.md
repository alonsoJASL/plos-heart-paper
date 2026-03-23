# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

LaTeX repository for PLOS Computational Biology paper (PCOMPBIOL-D-25-02375):
**"Assessing the Importance of Sex and Disease-Specific Anatomy in Electrophysiology and Mechanical Simulations with a Newly Developed Public Virtual Cohort of Four-Chamber Heart Models"**

## Build Commands

```bash
./rerunpdf.sh manuscript          # draft mode (shows tracked changes)
./rerunpdf.sh -f manuscript       # final mode (clean text only)
./rerunpdf.sh -d manuscript       # debug mode (interactive, stops on errors)
./rerunpdf.sh supplement_main     # supplementary material
./rerunpdf.sh -f supplement_main  # supplementary, final mode
```

The script runs: `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`.

Convert figures to PLOS-compliant TIFF (300 dpi, LZW compressed):
```bash
./process_figs.sh pics   # outputs to pics_formatted/
```

## Document Trees

Two parallel working trees (both use `\input{preamble_shared}`):

1. **`manuscript.tex` / `supplement_main.tex`** — current PLOS-format working files.
2. **`rootfile.tex`** — legacy file with custom article class (not actively used).
3. **`submission_no_figs.tex`** — submission variant without inline figures.

## Key Files

- [preamble_shared.tex](preamble_shared.tex) — shared packages and macros. Contains `\iffinal` toggle, simulation output macros (`\TAT`, `\VOL`, `\deltaVol`), and clinical group abbreviations (`\Ctl`, `\HF`, `\HFN`, `\HFW`).
- [sections/](sections/) — content sections: `intro_bis`, `materials`, `methods`, `results_final`, `discussion_final`, `conclusion`.
- [sections/supp/](sections/supp/) — supplementary item files (see naming convention below).
- [myrefs.bib](myrefs.bib) — bibliography. Style: `plos2025.bst`.

## Draft/Final Mode

`\iffinal` controls the `changes` package. Draft shows markup color-coded by author: `R1`=blue, `R2`=orange, `R3`=teal, `MR`=magenta, `ED`=brown. Final suppresses all markup. Toggle via `-f` flag, which injects `\finaltrue` via `-usepretex`.

## Supplementary Naming Convention

Files use the type-indexed PLOS scheme, not sequential numbering.

File name pattern: `s_{type}{n}_{description}.tex`

| PLOS label | File | `\label` key |
|---|---|---|
| S1 Fig | `s_fig1_tat_qrs.tex` | `fig:s1-tat-qrs` |
| S2 Fig | `s_fig2_correlation_heatmap.tex` | `fig:s2-correlation-heatmap` |
| S3 Fig | `s_fig3_mesh_quality.tex` | `fig:s3-mesh-quality-dist` |
| S1 Table | `s_tab1_geometric.tex` | `tab:s1-geometric-characteristics` |
| S2 Table | `s_tab2_cgal_params.tex` | `tab:s2-cgal-params` |
| S3 Table | `s_tab3_labels.tex` | `tab:s3-labels` |
| S1 Text | `s_text1_boundary_conditions.tex` | (no float label) |
| S1–S6 Data | external CSV/data files | no LaTeX labels |

`s_posthoc_comparisons.tex` is **orphaned** — not `\input`-ed in `supplement_main.tex`, no S-number yet. Would be S4 Table if added. Do not assign it a label or include it without explicit instruction.

## Cross-References Between Documents

`xr` package enables bidirectional cross-referencing:
- `manuscript.tex` has `\externaldocument{supplement_main}`
- `supplement_main.tex` has `\externaldocument{manuscript}`

Both `.aux` files must exist before cross-refs resolve — normal two-pass behaviour; run `./rerunpdf.sh` twice if refs appear as `??` on first build.

## PLOS Submission Requirements

- Submission must be a **single flat `.tex` file** (no `\input` commands).
- Figures uploaded separately as TIFF/EPS at 300–600 dpi, max 10 MB each.
- Use `Fig` (not `Figure`) for in-text figure citations.
- Bibliography style: `plos2025.bst`.

## Session Context

The following items were in-progress as of 2026-03-23 and may still need attention:

1. **Stale heading in `s_text1_boundary_conditions.tex`** — the `\subsection*{}` heading still reads "S4 Mechanics Simulation Boundary Conditions". The "S4" prefix is from the old sequential scheme and should be removed or corrected.

2. **Compile not yet verified** — the full rename + label + ref changes from the last session have not been tested. Run `./rerunpdf.sh manuscript` and `./rerunpdf.sh supplement_main` to confirm no broken references before the next submission step.

3. **Response letter** (`reviews_data/final_response_letter.txt`) uses old sequential labels in its preamble (line 5) and E3 response (line 24). User intended to fix this manually in Word — no LaTeX changes needed.
