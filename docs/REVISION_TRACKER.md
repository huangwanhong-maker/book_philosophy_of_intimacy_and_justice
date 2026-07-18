# REVISION_TRACKER

> Every paper in the series is a **draft**. Each is checked and revised before it
> is compiled into a volume. This file is the working record of that pass.
> Plan and architecture: [`BOOK_PLAN.md`](BOOK_PLAN.md).

## Status legend

| Mark | Meaning |
|------|---------|
| `—` | not started |
| `WIP` | revision in progress |
| `REV` | revised; awaiting author review |
| `OK` | author-approved, book-ready |

## What "revised" means (the per-paper checklist)

A paper is not marked `REV` until all of the following are done.

1. **Argument** — read end to end. Claims actually supported; no gaps, no
   circularity; conclusions follow. Weak sections flagged or strengthened.
2. **Consistency with the series** — terminology and notation match the rest of
   the series (`holonomy`, generative justice, relational being, the Lacanian
   registers). Cross-references to other papers are real and correct.
3. **Redundancy** — the series repeats itself across papers. Cuts proposed where
   a passage restates another paper without adding to it.
4. **Citations** — every citation checked against the source. No fabricated or
   guessed fields (`CLAUDE.md` §5). Conflicting keys reconciled into
   `bib/master.bib`.
5. **Formal content** — the mathematics/formalism (holonomy, phase, POMDP,
   Kuramoto, coalgebra) is stated correctly and does not over-claim. Where a
   formalism is a *metaphor*, it says so.
6. **Build** — compiles standalone **and** as a chapter, 0 undefined citations,
   0 undefined references, no stray `\todo` in the output.
7. **AI disclosure** — the Acknowledgements carry the series-standard AI-usage
   statement (`CLAUDE.md` §7).

## Volume I — Papers I–IX

Objective-fix status of the "fix layer." `bib OK` = all citations resolve
against the verified master.bib.

| # | Paper | pp | Objective fixes | Notes |
|---|-------|----|-----------------|-------|
| I | Toward Relational Being in Intimate Life | 53 | bib OK | anchor paper; cites eglash2016generative (now correct: *Of Marx and Makers*) |
| II | The Justice and Ethics of AI-Mediated Intimacy | 43 | bib OK | long abstract |
| III | The Normativity of Self-Legislation | 26 | bib OK | reference design for the style |
| IV | The Language of the Gift | 15 | bib OK | shortest paper (4.8k) — **flag: is it complete?** |
| V | The Formation of the Subject | 36 | **FIXED** | lacan1998→lacan1977xi (was citing Encore for the Seminar XI gaze dictum) |
| VI | Toward a Just Proposal | 19 | **FIXED** | 3 broken `sec:mapping` refs — label added to the mapping subsection |
| VII | Prolegomena to a Diplomacy | 53 | **FIXED** | 8 `\todo` resolved (1→footnote, 7 removed), 2 malformed table refs fixed |
| VIII | The Intervention of Language (excursus) | 32 | bib OK | companion to XXVI (Vol III) — cross-volume ref |
| IX | The Sustainability of Intimacy | 74 | bib OK | eglash2016 page range corrected (369–404) via override |

**Citations:** 25 of 28 contested keys resolved (18 source-verified + 7
normalized) into `bib/overrides.bib`; see `CITATION_RESOLUTIONS.md`. All Volume I
citations now resolve to verified data. Remaining 5 provisional (`nussbaum2001`
split + 4 self-citations) are cited only by Volume II/III papers.

## Volume II — Papers X–XVIII

Objective-fix status. Volume II builds clean (1174 pp, 0 undefined cites/refs/todos).

| # | Paper | pp | Objective fixes | Notes |
|---|-------|----|-----------------|-------|
| X | The Joint Attention of Value | 62 | bib OK | antecedent to IX |
| XI | A Just Eudaimonia | 82 | **FIXED** | nussbaum2001→nussbaum1986fragility (Fragility of Goodness) |
| XII | The Sweet Cycle | 48 | bib OK | `\nocite` list made explicit (was `\nocite{*}`) |
| XIII | The Causality of the Non-Binding Vow | 77 | bib OK | 140-entry bib |
| XIV | Contingency, Existence, and Eudaimonia | 97 | bib OK | note: "GRB" = Generative Relational Being, not gamma-ray-burst |
| XV | The Political Economy of Intimate Relations | 97 | bib OK · **open** | **blank TikZ figure** (empty `tikzpicture` in s4); **`\Lag`/Lagrangian macro defined-but-unused** — author decision needed |
| XVI | The Semiotics of Luxury | 58 | bib OK | extends XV |
| XVII | Generativity Under Power | 67 | bib OK · **open** | **§8 footnotes lack citekeys** (placeholder refs); **etiology total stated as both 19 and 16**; "cause N" refs point to a list never shown — author to reconcile |
| XVIII | Generative Effacement | 36 | **FIXED** | nussbaum2001→nussbaum2000women (Women and Human Development); figure `phase_diagram.png` |

**Self-citations reconciled** (author-authoritative, from each paper's cover):
`paperix`/`paperxiii`/`paperxv` titles corrected (paper XV was cited under a wholly
wrong title in XX/XXI/XXIII); `wan2024grb` title fixed (year flagged for
finalization). `nussbaum2001` split into `nussbaum1986fragility` + `nussbaum2000women`
and citing papers repointed. All in `bib/overrides.bib`.

## Volume III — Papers XIX–XXVII

| # | Paper | pp | words | bib | Status | Known issues / notes |
|---|-------|----|-------|-----|--------|----------------------|
| XIX | On the Emergence of Happiness | 53 | 20.0k | natbib | — | figure from `phase_diagram.py` |
| XX | The Hydraulic Virtue (Ethics of Water) | 39 | 18.1k | natbib | — | companion `wan2026braid` — verify it is citable |
| XXI | The Field of "Travel" | 123 | 64.3k | natbib | — | 2nd largest; needs `tcolorbox`, Greek |
| XXII | Relational Aesthetics | 138 | 73.8k | natbib | — | **largest**; only paper with its own `preamble.tex`; heavy TikZ |
| XXIII | The Aesthetic Philosophy of the Quotidian | 55 | 26.3k | natbib | — | sibling to XXII |
| XXIV | The Emergence of Culture | 81 | 40.9k | natbib | — | **prints a `\todo` into the PDF** (`s07_chinese.tex`) |
| XXV | Optimization Theory and Rationality | 42 | 21.5k | natbib | — | clean 27-entry bib |
| XXVI | The Limitation of Language | 55 | 25.4k | natbib | — | companion to VIII (different volume — check cross-refs) |
| XXVII | Relational Understanding | 43 | 20.4k | natbib | — | extends XXVI |

## Cross-cutting issues (affect many papers)

| Issue | Scope | Status |
|-------|-------|--------|
| natbib → biblatex conversion (21 papers + XII) | corpus-wide | **DONE** — all 27 on biblatex/biber; 1,161 `\citep`→`\parencite`, 141 `\citet`→`\textcite`, 14 `\citealp`→`\cite` |
| Unified `master.bib` (764 entries, deduplicated) | corpus-wide | **DONE (provisional)** — 736 merged clean; 28 contested keys flagged `>> PROVISIONAL <<`, pending source verification |
| 28 contested bib keys (see CITATION_AUDIT.md) | corpus-wide | **OPEN** — source-verification agent hit session limit; not yet reconciled |
| Macro collisions: `\zh`,`\term`,`\el`,`\emc`,`\emb`,`\xref`,`\claim` | corpus-wide | **DONE** — harvested verbatim into `serendip-macros.sty`; first-definition-wins, conflicts logged |
| Column-type collision `Y` (p{3.1cm} vs tabularx X) | XXI vs 16 others | **DONE** — XXI's stretch column renamed `Z` |
| Label collisions across papers (`sec:intro`, `sec:conclusion`…) | corpus-wide | **DONE** — 1,642 labels namespaced `pNN:`; 1,879 refs rewritten |
| Cross-paper references written as prose (`\pinkref{Paper~XV}`) | VII, IX, X, XIV–XVIII | **OPEN** — these are not real `\ref`s; should become proper cross-refs or citations |
| Redundancy between papers (the series restates itself) | corpus-wide | — |

## Unresolved `\todo` in the manuscript (book build gate: `make todo-check`)

The book build turns any stray `\todo` into a visible red marker + warning; none
may remain in a shipped volume. **11 found:**

| Paper | Count | Notes |
|-------|-------|-------|
| VII | 8 | working-titles, deferred tables, "confirm precise Eglash entry", Value-Foam notation alignment |
| XX | 1 | acknowledgements to be completed by author |
| XXI | 1 | acknowledgements to be completed by author |
| XXIV | 1 | classical-Chinese material deliberately left unasserted (`s07_chinese.tex`) |

## Other build-surfaced defects

| Paper | Defect | Status |
|-------|--------|--------|
| VI | 3 `\ref{sec:mapping}` to a section that does not exist in this installment (deferred to "the full paper") | **OPEN** — needs author decision: add the section or rephrase |
| VII | `\ref{Table~\ref{tab:frameworks}}` — nested/malformed refs; `tab:frameworks`, `tab:matrix` undefined | **OPEN** |
| IX | duplicate `\label{sec:return}` (two sections) | **DONE** — subsection relabelled `sec:returnroot` |

## Baseline (2026-07-12)

All 27 papers build: **0 undefined citations**, ~1,604 pages, ~747k words.
Commit: `05ba8ff` (Add Papers XXI–XXVII to the series).
Working branch: `books/three-volumes`.
