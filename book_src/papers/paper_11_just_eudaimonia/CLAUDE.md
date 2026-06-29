# Paper XI — A Just Eudaimonia

**Full title:** A Just Eudaimonia: The Everyday Fabric of a Shared Life and the Praxis of Flourishing
**Subtitle:** On the Cultivation of Habit and Household, the Unfolding of Each Within a Common Field, and a Flourishing That Justice Constitutes
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 126 entries)
**Build:** `make paper_11_just_eudaimonia` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
The **empirical praxis** companion to Paper X. Where X held (in the abstract) that a good relation is *cultivated as a field, not constructed as a structure*, that the field's matter is the everyday sensory/habitual fabric of a shared life, and that a good field meets two conditions — the **eudaimonic** and the **just**, the just *constituting* rather than merely constraining the eudaimonic — Paper XI asks how a shared life is in fact **cognised, practised, assessed, and sustained** across its course. It takes that course as a **cycle** and makes the cycle its primary object: cognition → practice → evaluation → reflection → renewed cognition, turning from a relation's beginning, through marriage, into its later years. The cycle is a **real dynamical cycle** (not a linear sequence of stages): its persistence is the condition of the relation's existence, so the cycle's cessation is not a relation at rest but a relation **extinguished**.

Five frameworks for the cognition/practice of flourishing — **positivist, evidentialist, normative, virtue-theoretic, phenomenological** — are treated not as rival theories of one measurable object but as the **symmetry-broken phases** (in Paper X's sense) of an object no framework owns; the paper traverses the moments of the cycle, drawing the apt framework into each. A cognitive/computational basis grounds the whole: **appraisal**, before it is explicit measurement, is continuous and largely unconscious **inference on the partially observable state** of a relation, in an unsymbolised value — formalised as **belief-updating of a decision process whose objective is itself revised by its running** (the decision-theoretic form of "no fixed meta-value-grammar"). On the **free-energy** reading, continual appraisal is the activity by which a relation holds itself in existence; its cessation begins extinction.

Three commitments run through it: (1) an **operational concession** — where it must assess, it restricts to value as a structured, **assessable proxy**, openly noting the proxy is *not* the transversal, irreducible value of the prior papers (the first deliberate adoption of an incomplete value — discharge of the prior result, not its abandonment); (2) **justice as a statistical signature** — a relation's distribution of returned value, relative to a **coupling-based baseline**, has a **skewness** by which the exploitation of one party *within an apparently satisfying relation* becomes visible where aggregate satisfaction hides it (justice rendered as a testable hypothesis about the symmetry of a return distribution, modelled as a **branching process** on the relational network); (3) the cycle **accumulates a phase** (holonomy, per Paper IX), its regime fixed by two independent questions — does it persist? and, if so, what **sign of phase**? — giving three regimes: the **flourishing spiral** (persists, +phase), the **catastrophic cycle** (persists, −phase), and **extinction** (ceases), the passages between them **bifurcations**. **Justice is the internal condition of the flourishing spiral, not a constraint on it**: a severely skewed return distribution cannot accumulate positive phase for the party consigned to its low-return tail. It ends in **plural conclusions**, not synthesis: flourishing is *cultivated not constructed, assessed in proxy not possessed, sustained as an open spiral not secured as a state*.

## Structure (sections/ \input by main, in reading order)
intro → fig_lifecycle (TikZ diagram) → background → philosophy → dynsys (dynamical systems) → appraisal → cycle → matrix → cognition → practice → evaluation (\inputs ev_survey, ev_instruments, ev_operational) → reflection → recognition → regimes → case → crosscultural → foundational → objections → conclusions → envoi → acknowledgements → **\appendix** → notation → appendix.

## Key concepts & coined terms
- **The value cycle** — cognition/practice/evaluation/reflection as a self-sustaining dynamical cycle; its persistence *is* the relation's existence.
- **Appraisal as inference (POMDP / free energy)** — relation-maintenance as continuous belief-updating on a partially observable state, objective revised by its own running; cessation = extinction.
- **Operational concession (the assessable proxy)** — deliberately adopting an incomplete, symbolisable proxy for the irreducible value, with the gap marked (a first in the series).
- **Justice as skewness** — exploitation made visible as asymmetry of the return distribution against a coupling baseline (branching-process model); aggregate satisfaction can conceal it.
- **Three regimes (phase × persistence)** — flourishing spiral (+phase), catastrophic cycle (−phase), extinction; transitions as bifurcations.
- **Justice constitutes the eudaimonic** — not a constraint: a skewed return distribution cannot yield positive phase for the low-return party.
- **Five frameworks as symmetry-broken phases** — positivist / evidentialist / normative / virtue-theoretic / phenomenological (cf. Paper X's "no framework owns the whole").
- Cross-links: **Paper X** (prior: cultivation of the field, the good that cannot be guaranteed), Paper IX (sustainability, holonomy/phase, good vs vicious circle), Paper VI (epistemic injustice; the *just*), Paper V (joint attention, appraisal), Paper VII (geometric phase, political economy).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; 126 entries — the largest bibliography in the series). classic-BibTeX rules apply (no `@` in refs.bib comments — clean; no author+editor in `@book`).
- **TikZ** is required (the `fig_lifecycle` diagram): the converted preamble adds `\usepackage{tikz}` + `\usetikzlibrary{arrows.meta,positioning,calc,decorations.pathmorphing}` — this is the first series paper to need TikZ.
- **Multi-file:** body in `sections/` (27 files), `\input` by the main tex; `evaluation.tex` further `\input`s `ev_survey`/`ev_instruments`/`ev_operational`; `notation`/`appendix` come after `\appendix`.
- **Converted to the shared style:** originally a bespoke preamble (Pagella + own palette); now `\usepackage{serendip-paper}` + the unified cover. Paper-specific macros kept: `\holo`, `\zh`/`\cjk`, `\emc`/`\emb`, `\goldrule`, `\todo`, `\xref`/`\pinkref`, `claim`/`casebox`; tables via `tabularx`/`ragged2e` + the `Y` column.
- A single-file `Paper_XI_standalone.tex` exists upstream (for arXiv/SSRN); **not** in this zip and **not** deployed — the series uses the multi-file form.

## Files
- `paper_11_just_eudaimonia.tex` — main (preamble, cover, epigraph, dedication, abstract, `\input` of sections + appendix, bibliography)
- `sections/` — 26 body files (+ `abstract.tex`; incl. `fig_lifecycle.tex` and the `ev_*` evaluation sub-files) · `refs.bib` (126) · `latexmkrc` · `README.txt` (upstream build notes)
