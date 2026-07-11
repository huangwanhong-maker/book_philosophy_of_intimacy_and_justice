# CLAUDE.md — Philosophy of Intimacy and the Theory of Justice (paper series)

> Project-level working guide for humans and AI assistants editing this open
> book. It **supplements** the workspace-root `NGO/CLAUDE.md` (general NGO
> conventions) with what is specific to this paper series. Read this before
> touching the LaTeX. Each paper folder also has its own short `CLAUDE.md`.

## 1. What this project is

An open book: a growing series of philosophy papers on intimate life, relational
being, and justice, stewarded by **Serendip Commons Society**. Eight papers so
far (I–VIII); **more will be added** — treat every convention here as a template
for the next paper, not a fixed list.

The series develops an integrative theory of justice for intimacy from a
deliberately wide theoretical range (political economy, ethics, justice theory,
relational ontology, psychoanalysis, linguistics, feminist theory, even
theoretical physics / field theory and algebraic topology). Its method is
**polyphonic**: no single framework is treated as exhausting a relational truth;
each paper breaks the symmetry onto one framework, pushes it hard, and marks its
partiality (Paper VIII §"The Poetics of Truth" makes this method explicit).

## 2. Repository layout

```
philosophy_of_intimacy_and_justice/   ← git repo root (remote: book_philosophy_…)
├── README.md            ← public landing page + contribution approach
├── LICENSE              ← CC BY-NC-SA 4.0 + attribution + commercial-by-permission
├── CONTRIBUTORS.md      ← carry-forward contributor list + inbound CLA
├── CLAUDE.md            ← this file
├── socarxiv_submissions.txt ← plaintext titles/abstracts/keywords for SocArXiv
├── papers/              ← published PDFs (SSRN/OSF versions); untracked by git
└── book_src/            ← LaTeX sources (the actual book)
    ├── serendip-paper.sty   ← shared style (single source of truth)
    ├── Makefile             ← build all / one / collect PDFs
    ├── preface.tex, assets/ ← book-level matter, covers
    ├── pdfs/                ← collected compiled PDFs (gitignored; built by `make`)
    └── papers/paper_NN_slug/
        ├── paper_NN_slug.tex   ← main source
        ├── sections.tex        ← only some papers (\input from main; e.g. VIII)
        ├── refs.bib            ← bibliography
        ├── latexmkrc           ← lets the folder build standalone
        └── CLAUDE.md           ← per-paper notes
```

## 3. Build (WSL TeX Live — there is no native Windows TeX here)

From `book_src/`, via WSL: `wsl bash -c "cd /mnt/c/.../book_src && make"`.

- `make` → build every paper, then copy PDFs into `book_src/pdfs/`.
- `make paper_NN_slug` → build one (and refresh its `pdfs/` copy).
- `make clean` / `make cleanall` → remove aux (cleanall also clears PDFs).
- Engine: XeLaTeX + biber/bibtex via `latexmk` (needs Noto Serif CJK SC).
- **Gotcha 1:** each `latexmkrc` must use `@default_files = (...)`, NOT
  `\@default_files` — the leading backslash errors on TeX Live 2023.
- **Gotcha 2 (bibtex papers only):** classic BibTeX reads `@` even inside `%`
  comments, so keep literal `@` out of comment lines in those `refs.bib`; and a
  `@book` may not carry both `author` and `editor` (fold editor into `note`).
- **WSL quoting:** Git-Bash → `wsl bash -c "..."` mangles `$?`/variables and
  `\$(...)`. For loops or captured exit codes, write a `.sh` and run
  `wsl bash script.sh` instead of inlining.

## 4. Shared style (`serendip-paper.sty`)

Every paper does `\documentclass[11pt,a4paper]{article}` then
`\usepackage{serendip-paper}`. The style provides (edit once, all papers follow):

- Palette: pale-pink page (`pageblush`), **deep-red titles** (`warnred`),
  **pink** everything else — section headings, emphasis, and citations are
  `rosedeep`. `\textit`/`\textbf`/`\emph` are auto-recoloured pink; `citecolor`
  is pink (set in the one `hyperref` line).
- **Covers are uniform.** Each title page: pink small-caps series line
  (`Philosophy of Intimacy and the Theory of Justice · Paper N`) →
  `\coverrule` (wide) → deep-red title → deep-red italic subtitle →
  `\coverrule[0.25]` (narrow) → author/email/date → `\coverfootnote` (contact,
  pinned to the foot). **Do not hard-wrap titles with `\\`** — let them wrap.
- **Contact** is a single source of truth: `\coveraddrA`/`\coveraddrB` in
  `serendip-paper.sty`. Edit there and every cover updates.
- `\blfootnote` = marker-less footnote (anchors to the page foot, used for the
  contact block, works even on `titlepage`/`\maketitle` pages).

## 5. Bibliographies

Every paper carries its own `refs.bib`; all build with citations resolved.

- **biblatex/biber** (`\usepackage[...]{biblatex}`, `\addbibresource`):
  Papers **I, II, III, VI, VIII**.
- **natbib/bibtex** (`\bibliographystyle{plainnat}`, `\bibliography{refs}`):
  Papers **IV, V, VII**.
- **No fabricated citations.** For anything not canonical and certain,
  web-verify title/venue/volume/pages/year; if still unconfirmable, keep known
  fields and add `note = {>> VERIFY <<}`. Translated classics: `translator` +
  `origyear` + modern edition (biblatex) / encode in `note` + correct `year`
  (bibtex).

## 6. In-series cross-reference keys (author's own works)

- `huang2025relational` → *Responding to the Crises of Symbol and Subject in
  Modernity* (OSF, doi 10.17605/OSF.IO/5R6CD).
- `huang2025toward` → **Paper I** (Toward Relational Being in Intimate Life).
- `huang2026vow` → **Paper III** (self-legislation / the lover's vow).

## 7. House writing conventions

- Honour the relational frame (no substantialist "individuals who then enter
  relations"); see NGO/CLAUDE.md §3–§4, §15.
- Disclose AI assistance in each paper's Acknowledgements; mark
  unreviewed AI-substantive insertions with `<!-- ai-draft -->`.
- Some papers avoid em-dashes in English prose (commas/colons/semicolons).
- Keep CJK quotations in `\cjkfont`.

## 8. License & contribution model

CC BY-NC-SA 4.0 (free, non-commercial, ShareAlike). Required attribution:
credit Serendip Commons Society **and** carry forward `CONTRIBUTORS.md`.
Commercial use only by separate license from the Society. Contributions accepted
under the inbound CLA in `CONTRIBUTORS.md` (public CC license **+** a
non-exclusive commercial grant to the Society). Copyright holders keep full
rights to their own material (founder may publish commercially and open-source,
either order). Full terms: `LICENSE`.

## 9. Adding a new paper (checklist)

1. `book_src/papers/paper_NN_slug/` with `paper_NN_slug.tex`, `latexmkrc`
   (`@default_files = ('paper_NN_slug.tex')`), `refs.bib`, and a `CLAUDE.md`
   (copy an existing paper's, adjust).
2. `\usepackage{serendip-paper}`; pick the bibliography backend (§5); build the
   cover from the canonical template (§4) — series line, `\coverrule`×2,
   deep-red title (no `\\`), `\coverfootnote`.
3. `make paper_NN_slug` until it builds with **0 undefined citations**.
4. **Collect the PDF into `book_src/pdfs/`** — `make paper_NN_slug` already refreshes
   its `pdfs/` copy (or run `make pdfs`). Do this for every new/changed paper;
   `pdfs/` is the canonical local PDF set. (Confirm the cover matches the series:
   pink scshape series line, `warnred` title, `\coverrule`×2, `\coverfootnote`.)
5. Update: the paper index below, `README.md` table, `.proj` `documents:`, and
   `socarxiv_submissions.txt` (title/subtitle/abstract/keywords, plaintext).
6. **Website**: copy the PDF to the repo-root `papers/paper-N.pdf` (the `.proj`
   `documents:` path), then rebuild the site data — `node ngo_projects/scripts/build_projects.mjs`
   (regenerates `projects-data.js` + the `intimacy-philosophy` page; OSS upload +
   Cloudflare purge stay manual).

## 10. Paper index (and per-paper quirks)

| # | Folder / title | Bib | Local notes |
|---|---|---|---|
| I | `paper_01_toward_relational_being` — Toward Relational Being in Intimate Life | biblatex | family-app case study; cites `huang2025relational` |
| II | `paper_02_ai_mediated_intimacy` — The Justice and Ethics of AI-Mediated Intimacy | biblatex | uses `csquotes`; manual cover page (was `\maketitle`); abstract is long — short version in `socarxiv_submissions.txt` |
| III | `paper_03_self_legislation` — The Normativity of Self-Legislation | biblatex | the reference design `serendip-paper.sty` was extracted from; `singer1991nature` resolved to Vol. 1 (Chicago 1984) |
| IV | `paper_04_language_of_the_gift` — The Language of the Gift | natbib | refs were **inline**, converted to `refs.bib` + `\bibliography{refs}`; uses `titlepage` + `amsthm` |
| V | `paper_05_subject_formation` — The Formation of the Subject | natbib | `titlepage` with twin epigraphs; abstract moved to **its own page** so the contact foot pins correctly |
| VI | `paper_06_just_proposal` — Toward a Just Proposal | biblatex | extra "Theory-core installment" line on cover; epistemic-injustice (Catala 2025) |
| VII | `paper_07_diplomacy_of_intimacy` — Prolegomena to a Diplomacy | natbib (numbered) | **no formal abstract** (programmatic survey — see `socarxiv_submissions.txt`); bespoke cover; `simon1983` = **Barry** Simon (Berry phase), not Herbert |
| VIII | `paper_08_intervention_of_language` — The Intervention of Language (excursus) | biblatex | uses `sections.tex` (`\input`) + `\verseline`; §"The Poem as a Generative Grammar, and the Poetics of Truth" (`sec:grammar`) connects to Paper IV (formal language) and Paper VII (phase) |
| IX | `paper_09_sustainability_of_intimacy` — The Sustainability of Intimacy | natbib (numbered) | multi-file (`sections/`, 20 files); **converted** from a bespoke preamble (Pagella) to `serendip-paper`; geometric-phase axiom of sustainability; macros `\holo`/`\zh`/`claim`/`casebox` |
| X | `paper_10_joint_attention_of_value` — The Joint Attention of Value and the Creation of Language | natbib (numbered) | multi-file (`sections/`, 18 files); converted (Pagella→`serendip-paper`); antecedent to IX; quantum-structured grammar + political economy as symmetry-broken phases; same macro set; zip's `Paper_X_standalone.tex` not deployed |
| XI | `paper_11_just_eudaimonia` — A Just Eudaimonia | natbib (numbered) | multi-file (`sections/`, 27 files); converted (Pagella→`serendip-paper`); **needs TikZ** (lifecycle figure); empirical praxis of the good relation as a value cycle; POMDP/free-energy appraisal; justice-as-skewness; largest refs.bib (126) |
| XII | `paper_12_the_sweet_cycle` — The Sweet Cycle | **plain** bibtex (`\nocite{*}`) | **single-file**; converted (bespoke palette + fancyhdr → `serendip-paper`, colours mapped); `\cn{}` for CJK; bib `references.bib`→`refs.bib`; amai / "sweetness is justice" / forged holonomy; polyphonic (psychoanalysis, neuroscience, care, political economy, feminism) |
| XIII | `paper_13_non_binding_vow` — The Causality of the Non-Binding Vow | natbib (numbered) | multi-file (`sections/`, 17 files incl. literary `prelude`); converted (Pagella→`serendip-paper`); **needs TikZ**; trust-as-precision (3 coupled channels) / promissory estoppel / holonomy + open-quantum-system; "descent of a relational divinity"; largest refs.bib (140) |
| XIV | `paper_14_existentialist_eudaimonism` — Contingency, Existence, and Eudaimonia in Intimate Relations | natbib (numbered) | multi-file (`sections/`, 17 files incl. prelude/epigraph/dedication); converted (Pagella→`serendip-paper`); GRB reconstruction of eudaimonia; co-evolution / Kuramoto / hyperscanning / STDP analogy; hermeneutics of 11 happiness concepts; ma·en / ren / ubuntu; macros `\holo`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XV | `paper_15_generative_relational_wealth` — The Political Economy of Intimate Relations | natbib (numbered) | multi-file (`sections/`, 17 files incl. prelude/epigraph/dedication); converted (Pagella→`serendip-paper`); **needs TikZ** (self-generating-cycle figure, empty placeholder); Generative Relational Wealth — wealth owned by the "between" that use augments not depletes; happiness-jar case study (Peirce/Benjamin/Lacan/relational STDP); extends XIV (eudaimonics) & IX (generativity) into political economy; macros `\holo`/`\GRW`/`\Lag`/`\zh`/`\emc`/`\emb`/`claim`/`openquestion` |
| XVI | `paper_16_semiotics_of_luxury` — The Semiotics of Luxury in Intimate Relations | natbib (numbered) | multi-file (`sections/`, 13 files incl. prelude/epigraph/dedication); converted (Pagella→`serendip-paper`); **no TikZ**; relational luxury = coupling degree (κ) between object and a subject's spatiotemporal structure; three doctrines (nature/art, Baudrillard sign-exchange, relational); fourfold orthogonal classification; justice theory of choice (subject-embedding misrecognition / equivalent agency / selection justice); extends XV (political economy); macros `\GRW`/`\coup`/`\zh`/`\emc`/`\emb`/`claim`/`openquestion` |
| XVII | `paper_17_generativity_under_power` — Generativity Under Power | natbib (numbered) | multi-file (`sections/`, 16 files); converted (Pagella→`serendip-paper`); **no TikZ**; how love fares under power — two-level system (love = end/real, power = means/symbolic), "political economy of conditions, never of love"; trust as the interface; estrangement (すれ違い *surechigai*) as a necessary moment; IR reconstruction + dialectical historical materialism + dissipative structure; "a generative relation opposes the freezing of power"; extends XIII (trust), IX (holonomy), XIV–XVI |
| XVIII | `paper_18_generative_effacement` — Generative Effacement in the Intimate Relation | natbib (numbered) | multi-file (`sections/`, 8 files); converted (Pagella→`serendip-paper`); **has a figure** (`figures/phase_diagram.png`, graphicx+caption); generative effacement as *ontological* injustice (vs distributive/recognitive/constitutive) — a harm through devotion not domination; coupled phase-oscillator criterion (threshold from frequency-difference, depth from force-asymmetry; equal force still effaces by half); remedy = *decouple* not decelerate; generative reticence (relinquish goal/meaning/problems); macros `\holo`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XIX | `paper_19_emergence_of_happiness` — On the Emergence of Happiness and the Self-Continuation of Generativity | natbib (numbered) | multi-file (`sections/`, 12 files + abstract); converted (Pagella→`serendip-paper`); **has a figure** (`figures/limit_cycle.png`, van der Pol phase portrait from `phase_diagram.py` — rewritten numpy-only RK4; graphicx+caption; no TikZ); the plain, shared happiness of "nothing happens yet full" as *emergence* (not state/event) of a generative relation continuing itself; symbolic–real gap lived as lack vs **fullness** (happiness = fullness mode); happiness as **hermeneutic**, the dynamical only a *background manifold*; shared happiness = **resonance not merger**; three silences (obligation/restraint/needlessness); refs.bib fixed (dup `wang2021delayed`, whitehead author+editor); macros `\holo`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XX | `paper_20_hydraulic_virtue` — The Hydraulic Virtue of Intimate Relations (On the Ethics of Water) | natbib (numbered) | multi-file (`sections/`, 11 files + abstract); converted (Pagella→`serendip-paper`); no figure / no TikZ (graphicx kept, unused); an ethics of intimacy from Daoist **water** (上善若水), read *structurally* not as self-cultivation; five water-virtues vs five challenges (game theory / Hobbes / Nietzsche / feminism-psychoanalysis / Kant→imperfect duty); water-good = **chosen good not formless yielding** (rigid lower bound) + **shape power so surplus is returned not retained**; **ethical "translation layer" of formal companion `wan2026braid`** ("From Fluid to Braid", Knowledge Commons) — holonomy / solenoidal-vs-gradient / the non-substitutable "flesh"; water-phase of the dark virtue (玄德); refs.bib fixed (same dup `wang2021delayed`, whitehead author+editor); macros `\holo`/`\Shan`/`\fpow`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XXI | `paper_21_field_of_travel` — The Field of "Travel" (Spaciousness, Contingency, and the Generation of the Relational Subject) | natbib (numbered) | **largest paper (~123 pp)**; multi-file (`sections/`, 16 files + abstract); converted (Pagella→`serendip-paper`); no figure but **needs `tcolorbox`** (definitionbox/recapbox) + a `thesis` env + **Greek** (`\el`/`\grk`=DejaVu Serif) + tablehead colour + tabularx `Y`/`L`; shared **travel** as a *concrete universal* → a general theory of **relational production**; four movements (phenomenological: spaciousness 虚 / self-presence of relational dynamics; political-economic: experience = relational wealth, retelling reproduces it; aesthetic: antinomy of taste via 3 Lacanian registers, creation=co-creation, aesthetic education; ethical: **principle of subject-preservation** + 求同存异); generalized travel / generative openness; refs.bib fixed (whitehead author+editor) + a malformed `\citep` (stray prose) in s08; macros `\holo`/`\zh`/`\el`/`\emc`/`\emb`/`\lrhead`/`claim`/`casebox`/`thesis`/`definitionbox`/`recapbox` |
| XXII | `paper_22_relational_aesthetics` — Relational Aesthetics and the Construction of the Field (Toward an Aesthetic Education of Relational Life) | **natbib author-year** (round) | **largest paper (~138 pp)**; **only paper with a separate `preamble.tex`**; multi-file (`sections/`, 25 numbered + s0_abstract, in 5 parts); converted (bespoke `\maketitle` + own palette → `serendip-paper` + unified cover); no figure but **heavy TikZ** (chainbox/stepnode/facenode) + `tcolorbox` (claimbox/casebox) + makecell/tabularx + Greek (`\el`); sequel to XXI — field-construction as the object of an **aesthetic education of the everyday**; concept **relational aesthetics** (beauty = coupling *event* between subjects); four-step model **perception→reception→sharing→reproduction** = smallest good cycle, a holonomy returning to its *root* not origin; generative dialectical materialism; orthogonality guard (sensibility ⊥ justice); terminus **unifies the series's fields**; kept palette `deeprose`/`goldenrod`/`casebg`/`blush`; macros `\emc`/`\emb`/`\term`/`\thd`/`\el`/`\xref`/`claim`/`casebox` |
| XXIII | `paper_23_quotidian_aesthetics` — The Aesthetic Philosophy of the Quotidian and the Cultivation of Perception (《日常的美学哲学与美育》) | natbib (numbered) | multi-file (`sections/`, 15 files + abstract); converted (Pagella→`serendip-paper`); no figure / no TikZ (graphicx kept, unused); sibling to XXII — an **aesthetics of the everyday** → a theory of **aesthetic education**; perception is *generated not given* (esp. between two perceivers on a shared world); **generative relational aesthetic education** (4 faces; contra Schiller's individualism; relational/individual spiral; beauty & ethics one root); three spines (generation / body — perceptual plasticity / justice — **distribution of the sensible** as neglected injustice); **four models of everyday practice** (basic cycle / silence-reception / leaving of emptiness / iterative symbolic refinement); refs.bib fixed (dup `wang2021delayed`; whitehead + **bohme2017** author+editor); macros `\holo`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XXIV | `paper_24_emergence_of_culture` — The Emergence of Culture in Intimate Relation (《亲密关系中的文化涌现》) | natbib (numbered) | **large (~81 pp, 33 sections, 3 parts)**; multi-file; converted (Pagella→`serendip-paper`); no figure / no TikZ; takes up **XXIII's first fissure**; central thesis **three-register dialectic of the relational Real** (culture = a generation that doesn't close: dialectical exteriorization across the 3 Lacanian registers under material constraint; Real given a *relational* form); **five dyad mechanisms** (vacant big Other / double interweaving of drive / high-density sedimentation / register configuration / fragility); family ethos (家风) case; capital's **capture-as-decoherence** of the bond; **five own theses** (non-transferability / vacancy / capture-as-decoherence / counter-power criterion / real-anchoring); fresh 37-entry refs.bib (translated-classics author+editor = warnings only, left as-is); **⚠ prints one author `\todo`** in s07 (classical-Chinese material, deliberately unasserted); explicit AI-usage statement; macros `\holo`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XXV | `paper_25_optimization_and_rationality` — Optimization Theory and Rationality in Intimate Relations (《亲密关系中的优化理论与理性》) | natbib (numbered) | multi-file (`sections/`, 16 files + abstract, 5 parts, ~42 pp); converted (Pagella→`serendip-paper`); no figure / no TikZ; math macros **`\argmax`/`\argmin`** (no `\holo`); **optimization is not a law of the universe** — a *formal* proof (no value judgment) that intimate relation is not a well-defined optimization problem via **four impossibilities** (non-structurability of value/drive · relationality → absent quantifier · incommensurability = betrayal not mismeasure · subject-constitution → the optimizer is an output); then a *normative* critique (**extractive computation**; symptom of the symbolic crisis + capital; **optimal ⊥ good**); then a **non-optimizing relational rationality** (response/attunement/sustaining) + **wuwei**; closes in **polyphonic refusal** of a new master objective; sharpens the series' anti-"efficiency-as-terminal-value" critique; clean 27-entry bib; explicit AI-usage statement; macros `\argmax`/`\argmin`/`\zh`/`\emc`/`\emb`/`claim`/`casebox` |
| XXVI | `paper_26_limitation_of_language` — The Limitation of Language in Intimate Relation (Drive as the Phenomenology of Manque) | natbib (numbered) | multi-file (`sections/`, 23 files + abstract, 5 parts, ~55 pp); converted (Pagella→`serendip-paper`); **needs TikZ** (3 figures: the gap / drive circling / two faces) + `float`, no `\includegraphics`; companion to **Paper VIII**; thesis **the limit of language is generative** — across six dimensions (existence/maintenance/value/ethics/justice/evolution) a core language cannot reach; **drive = the phenomenology of *manque*** (the symbolic–Real gap), two faces that are one; **drive circles, desire slides**; the thought experiment that **closure would extinguish** them (non-closure = condition of persistence); generativity in poem / ethics-without-possession / justice-that-guards; coalgebra + **Mori–Zwanzig** co-structure heuristic; 32-entry bib (Lacan/Derrida `@book` author+editor = warnings only); **concise** AI-usage statement (series standard); §-numbering diverges from file stems (`s15b`, `s18c`, `s18b`); macros `\zh`/`\emc`/`\emb`/`claim`/`casebox`/`\xref` |
| XXVII | `paper_27_relational_understanding` — Relational Understanding in Intimate Relations (The Generative Relational Epistemology in the Domain of Intimacy) | natbib (numbered) | multi-file (`sections/`, 21 files + abstract, 7 parts, ~43 pp); converted (Pagella→`serendip-paper`); **needs TikZ** (2 figures) + `float`, one booktabs table; applies a companion **generative relational epistemology** to intimacy — understanding as a **crossing of symbolic worlds**; *functional case* (trust / shared value / conflict / well-being; two characters = relational + generative) → *normative case* (**legitimacy without correctness**; efficient **possession** counterfeits understanding; ethical legitimacy across traditions; non-possession + generative justice) → *special problem* (**the wager, not the rehearsal**; cultivation-field ≠ exercise-field) → *practice* (capacities not a procedure: **throwing a generative thing** / non-intervention / preservation; **non-possession** throughout, else refined extraction) → *dialectic* (**the unsymbolizable remainder sustains the bond**; a full crossing would end it — extends **XXVI**); 45-entry bib (Lacan/Derrida/Kant/Aristotle `@book` author+editor = warnings); **concise** AI-usage statement; two `s11_*`/`s16b` §-stem divergence; macros `\zh`/`\emc`/`\emb`/`claim`/`casebox`/`\xref` |

## 11. Pointers

- `README.md`, `LICENSE`, `CONTRIBUTORS.md` — public-facing.
- `book_src/README.md` — build details.
- `../../../CLAUDE.md` (NGO root) — workspace-wide conventions.
- Memory: `build-latex-paper-series` and the project memories index this work.
