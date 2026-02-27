# Sprint 3 Diagnostic Guide: Abstract + Introduction Issues

## ABSTRACT - Issue 1: Missing anatomical focus (R1-Maj-1)

**Current opening line:**
```
This work presents a study on how sex and disease can influence cardiac 
electrophysiology and mechanics using a virtual cohort of four-chamber 
heart models.
```

**What R1 sees as the problem:**
The sentence doesn't clarify that you're studying *anatomical differences* attributed to sex/disease, not all physiological differences. A reader could think you're studying hormonal effects, genetic differences, or other non-anatomical factors.

**R1's exact suggestion:**
```
This work presents a study on how differences in cardiac anatomy attributed 
to sex and disease can influence cardiac electrophysiology and mechanics 
using a virtual cohort of four-chamber heart models.
```

**Your task:**
- [X] Find this sentence in your LaTeX abstract
- [X] Insert "differences in cardiac anatomy attributed to" between "how" and "sex"
- [X] This is a 5-word insertion, not a rewrite

**Why it matters:**
Your study uses identical simulation parameters across all models, so the only thing varying is geometry. If the abstract doesn't say this upfront, readers will expect parameter variation too.

---

## INTRODUCTION - Issue 2: Last paragraph is unnecessary (R3-Maj-1)

**Current last paragraph before Section 2:**
```
The aim of this study is to develop a workflow for creating hearts,
apply the workflow to create a new open source sex balanced control and
disease cohort, and test the impact of sex and disease differences in
anatomy on reference simulations. Figure [1] provides an overview of the
pipeline and the resulting cohort.
```

**What R3 sees as the problem:**
This paragraph is redundant. You've already described the workflow and cohort in the paragraph immediately before it (the one starting "In this study, we present CEMRG Heartbuilder..."). The aims are implicit from that description.

**Your options:**

**Option A (DELETE):** Remove this paragraph entirely.
- Pro: Cleanest fix
- Con: Some journals like explicit aims statements

**Option B (COMPRESS):** Reduce to 1 sentence and merge with previous paragraph.
```
Figure 1 provides an overview of the workflow and resulting cohort.
```

**Your task:**
- [x] Locate this paragraph in your intro LaTeX file (probably `sections/intro_bis.tex`)
- [x] Decide: delete entirely OR compress to 1 sentence
- [x] If compressing, remove the "The aim of this study..." framing

**Why it matters:**
R3 says "last paragraph is not needed" — this is the easiest fix on the entire list.

---

## INTRODUCTION - Issue 3: Second-to-last paragraph has too much methodology (R3-Maj-1)

**Current second-to-last paragraph (the one starting "In this study, we present CEMRG Heartbuilder..."):**
```
In this study, we present CEMRG Heartbuilder, a Python-based library
designed to systematically generate patient-specific, four-chamber heart
models from clinical computerised tomography (CT) data. Our workflow
integrates custom image analysis routines with wrappers for external
tools, building upon the reproducible and user-friendly CemrgApp
platform. We applied the workflow to a new cohort of 50 patients
(balanced by sex), classified into three clinical groups: controls
(n=26), heart failure with narrow QRS (n=12), and heart failure with
wide QRS (n=12). For each case, models were created from a CT scan to a
simulation-ready mesh with fibres, and subsequently used to run
benchmark electrophysiological and mechanical simulations. The
simulations demonstrated the feasibility and robustness of the approach,
and, through the use of uniform material properties, isolated the impact
of disease and sex differences in anatomy on reference mechanical and
electro physiological simulations.
```

**What R3 sees as the problem:**
This paragraph contains:
1. ❌ Sample size numbers (n=26, n=12, n=12) — too detailed for intro
2. ❌ Methodology detail ("custom image analysis routines with wrappers", "CT scan to simulation-ready mesh with fibres") — belongs in Methods
3. ❌ Tense inconsistency: "we present" (present tense) → "We applied" (past tense) → "demonstrated" (past tense)

**Your task - Part A: Remove sample size numbers**
- [X] Find: "controls (n=26), heart failure with narrow QRS (n=12), and heart failure with wide QRS (n=12)"
- [X] Change to: "controls, heart failure with narrow QRS, and heart failure with wide QRS"
- [X] Or even simpler: "healthy controls and two heart failure subtypes (narrow and wide QRS)"

**Your task - Part B: Remove methodology detail**
- [X] Identify which details are methods vs. high-level description
  
  **Keep (high-level):**
  - "Python-based library for patient-specific four-chamber heart models"
  - "CT data"
  - "cohort of 50 patients balanced by sex"
  - "benchmark simulations to isolate anatomical effects"
  
  **Move to Methods (technical detail):**
  - "custom image analysis routines with wrappers for external tools"
  - "from a CT scan to a simulation-ready mesh with fibres"
  - These belong in Section 3 (Methods)

**Your task - Part C: Fix tense inconsistency**
- [X] Choose ONE tense for the entire paragraph
  - Either: all present ("In this study, we present... we apply... we run...")
  - Or: all past ("In this study, we presented... we applied... we ran...")
  
  **Recommendation:** Use past tense for completed work.
  
**Example rewrite (for reference, not the answer):**
```
In this study, we developed CEMRG Heartbuilder, a Python-based library 
for generating patient-specific, four-chamber heart models from clinical 
CT data. We applied this workflow to a cohort of 50 patients balanced by 
sex, including healthy controls and two heart failure subtypes. Benchmark 
simulations with uniform material properties isolated the impact of 
anatomical differences attributed to sex and disease on cardiac 
electrophysiology and mechanics.
```

**Word count:** Current = 119 words. Target = ~60 words.

---

## ABSTRACT - Issue 4: Verify no contradiction with de-escalated Discussion (cross-check after Sprint 7)

**What this means:**
In Sprint 7, you'll rewrite parts of the Discussion to de-escalate claims about validation and causality. This Sprint 3 task is a **forward-check**:

**Current abstract language to watch:**
- "isolated the impact of disease and sex differences in anatomy" ← Good, already cautious
- "support the inclusion of multiple heart anatomical models" ← Good, not overclaiming

**Language to AVOID adding (don't fix what isn't broken):**
- ❌ "validates the cohort for in-silico trials"
- ❌ "demonstrates that anatomy causes hemodynamic differences in HF"
- ❌ "provides a ready-to-use ISCT platform"

**Your task:**
- [ ] After completing Sprint 7 Discussion rewrite, re-read your abstract
- [ ] Check: does abstract claim anything stronger than Discussion supports?
- [ ] If yes, soften the abstract wording to match Discussion

This is a **post-Sprint-7 check**, not an action item for now.

---

## SUMMARY CHECKLIST FOR YOUR TEX FILES

### Abstract (`plos_latex_template.tex` or wherever abstract lives):
- [X] Line 1: Insert "differences in cardiac anatomy attributed to" after "how"
- [ ] No other changes needed right now (will cross-check after Sprint 7)

### Introduction (`sections/intro_bis.tex` or similar):
- [X] LAST paragraph: Delete entirely OR compress to 1 sentence about Figure 1
- [X] SECOND-TO-LAST paragraph:
  - [X] Remove "(n=26)", "(n=12)", "(n=12)" sample sizes
  - [X] Remove "custom image analysis routines with wrappers" detail
  - [X] Remove "from a CT scan to a simulation-ready mesh with fibres" detail
  - [X] Fix tense: make entire paragraph consistently past tense
  - [X] Target: reduce from ~119 words to ~60 words

