# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LaTeX repository for a PLOS Computational Biology paper:
**"Assessing the Importance of Sex and Disease-Specific Anatomy in Electrophysiology and Mechanical Simulations with a Newly Developed Public Virtual Cohort of Four-Chamber Heart Models"**

## Build Commands

Compile the main manuscript (draft mode, shows tracked changes):
```bash
./rerunpdf.sh manuscript
```

Compile in final mode (hides tracked changes, clean text):
```bash
./rerunpdf.sh -f manuscript
```

Compile in debug mode (interactive, stops on errors):
```bash
./rerunpdf.sh -d manuscript
```

Compile the supplementary material:
```bash
./rerunpdf.sh supplement_main
./rerunpdf.sh -f supplement_main   # final mode
```

The script runs: `pdflatex` → `bibtex` → `pdflatex` → `pdflatex` in sequence.

Convert figures to PLOS-compliant TIFF format (300 dpi, LZW compressed):
```bash
./process_figs.sh pics
# Outputs to pics_formatted/
```

## Repository Structure

There are **two parallel document trees**:

1. **`manuscript.tex` / `supplement_main.tex`** — Current working files (PLOS template format). These use a shared preamble via `\input{preamble_shared}`.

2. **`rootfile.tex`** — Legacy working file (custom article class). Inputs from `sections/`.

3. **`plos_latex_template.tex`** — PLOS official template file (for submission preparation).

4. **`submission_no_figs.tex`** — Submission variant without inline figures.

### Key files

- [preamble_shared.tex](preamble_shared.tex) — Shared packages and macros for both `manuscript.tex` and `supplement_main.tex`. Contains the `\iffinal` toggle for the `changes` package (draft vs final mode), simulation output macros (`\TAT`, `\VOL`, `\deltaVol`), and clinical group abbreviations (`\Ctl`, `\HF`, `\HFN`, `\HFW`).
- [sections/](sections/) — Content sections included via `\input`: `intro_bis`, `materials`, `methods`, `results_final`, `discussion_final`, `conclusion`, `supplementary_material`.
- [sections_no_figs/](sections_no_figs/) — Parallel section files without figures (for the no-figs submission variant).
- [myrefs.bib](myrefs.bib) — Main bibliography file.
- [plos2025.bst](plos2025.bst) — PLOS 2025 bibliography style.
- [docsettings/footer.tex](docsettings/footer.tex) — Bibliography call (used by `rootfile.tex`).
- [pics/](pics/) — Source figures (PDF/EPS format).
- [pics_formatted/](pics_formatted/) — PLOS-submission-ready figures (TIFF, 300 dpi).
- [vector/](vector/) — Editable vector source files (.idraw format).

## Draft/Final Mode

The `\iffinal` boolean controls how the `changes` package renders tracked changes:
- **Draft** (default): shows additions, deletions, and comments color-coded by reviewer author (`R1`=blue, `R2`=orange, `R3`=teal, `MR`=magenta, `ED`=brown).
- **Final**: suppresses all markup; only accepted text is shown.

Toggle by passing `-f` to `rerunpdf.sh`, which injects `\finaltrue` via `-usepretex`.

## PLOS Submission Requirements

- The submission must be a **single flat `.tex` file** (no `\input` commands).
- Figures must be uploaded separately as TIFF/EPS at 300–600 dpi, max 10 MB each.
- Use `Fig` (not `Figure`) for figure citations.
- Bibliography style: `plos2025.bst`.
