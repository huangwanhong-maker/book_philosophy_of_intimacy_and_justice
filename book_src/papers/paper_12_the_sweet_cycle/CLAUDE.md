# Paper XII — The Sweet Cycle

**Full title:** The Sweet Cycle (甜之循环的认识与正义实践论 — 神经科学、精神分析与政治经济学的讨论)
**Series line:** Philosophy of Intimacy and the Theory of Justice, Paper XII
**Status:** working draft, 2026 · **Bibliography:** plain bibtex (numbered `plain.bst`, `\nocite{*}`; 31 entries)
**Build:** `make paper_12_the_sweet_cycle` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
Occasioned by a Ginza magazine cover that declared **「甘いは正義」** (*sweetness is justice*), the paper takes that proposition as its starting point, not its target. *Amai* (sweetness / indulgence) names, in intimate life, a **cycle that seems to harm no one and benefit everyone inside it**: a firm sells, the indulged feels cared for, the indulger feels needed, the bond tightens, and the tighter bond returns as a willingness to buy again — a closed loop with a real surplus of satisfaction. The question: on what grounds, and under what conditions, is such a cycle **genuinely good** rather than a **forged closure** that sustains its inner surplus by **extraction across its outer edge**?

Method is **polyphonic** (the series' signature): several incommensurable frameworks — **psychoanalysis, neuroscience, the ethics of care, political economy, feminist theory** — are set before the same phenomenon, each saying what it can and cannot see, **none permitted to adjudicate the others**. A **psychoanalytic foundation** (reconstructed in full from the author's prior Chinese work on **lack**, the **objet a**, and **the cute as a mediation of lack**) supplies the structural diagram. The **political economy of *amai*** — where capital does not merely serve a pre-existing desire but **produces and reproduces the desire itself** and extracts a surplus from that reproduction — gets the most sustained treatment, because there the difference between a genuine and a forged cycle becomes **measurable**. It closes not on a verdict but on a **plurality of practices** (just, ethical, eudaimonic, co-creative) by which a sweet cycle can keep its value within itself and return it to those who make it, **with no one reduced to fuel** — and on the honest remainder that judging always turns on *where the cycle's edge is drawn*, an act performed from somewhere, with no view from nowhere.

## Key concepts & coined terms
- **Sweetness is justice (甘いは正義)** — the slogan whose grammar (an identity claim) pre-closes the very question justice exists to keep open; the occasion of the paper.
- **Amai / the sweet cycle** — the self-reinforcing loop of indulgence, care, and consumption in intimate life.
- **Forged holonomy** (vs **genuine/positive holonomy**) — the central distinction (carried from Papers IX/VII): a loop that *displays* the increment of a positive holonomy but did not generate it internally, having imported it from outside the path while presenting itself as closed. The whole question reduces to *generated or forged*.
- **The cute as a mediation of lack** — the cute/sweet object as a stand-in mediating the *objet a* (the unsymbolisable cause of desire).
- **Political economy of amai** — capital producing/reproducing desire and extracting surplus from its reproduction; where genuine-vs-forged becomes measurable.
- **The edge of the cycle / "no one as fuel"** — justice as a claim about the *whole*: who is counted, where the costs come to rest, what reproduces the sweetness unseen.
- **Plural conclusions** — no framework owns the verdict; the honest form is conclusions in the plural (cf. Papers VIII, X, XI).
- Cross-links: Paper IX (holonomy; good vs vicious circle; generative justice), Paper IV (the gift; value; Eglash's generative justice — acknowledged), Paper VII (geometric phase, political economy), the author's prior Chinese work on lack / objet a / the cute.

## Local notes / quirks
- **SINGLE-FILE** paper (unlike IX/X/XI's `sections/`): everything is in `paper_12_the_sweet_cycle.tex`.
- **Bibliography is plain bibtex**, not natbib: `\bibliographystyle{plain}` + `\bibliography{refs}` + **`\nocite{*}`** (all 31 entries print whether or not cited). Uses plain `\cite{...}`. classic-BibTeX rules apply (no `@` in comments — clean).
- The upstream bib was `references.bib`; **renamed to `refs.bib`** and `\bibliography{references}`→`\bibliography{refs}` to match the series.
- **Converted to the shared style** from a distinct bespoke preamble (TeX Gyre Pagella; own palette `deeprose/rose/gold/ink/blushground`; `fancyhdr` running header; `\maketitle`). Now `\usepackage{serendip-paper}` + the unified cover (pink series line, deep-red title + CJK subtitles, `\coverrule`×2, `\coverfootnote`). The body's own colours are **mapped into the series palette**: `deeprose`→`rosedeep`, `blushground`→`pageblush`; `rose`/`gold`/`ink` come from serendip-paper. `fancyhdr` running header was dropped (no series paper uses one). CJK via **`\cn{...}`** (not `\zh`), built on serendip's `\cjkfont`.
- House rule for this paper: **no em-dashes** (commas/colons/semicolons).
- A prebuilt `The_Sweet_Cycle_Paper_XII.pdf` shipped in the zip; **not** kept (we rebuild from source).

## Files
- `paper_12_the_sweet_cycle.tex` — the whole paper (preamble, cover, abstract, all sections, bibliography) · `refs.bib` (31, plain bibtex) · `latexmkrc` · `README.txt` (upstream build notes)
