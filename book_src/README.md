# Philosophy of Intimacy and the Theory of Justice — sources

Each paper of the series is a **standalone document in its own folder** under
[`papers/`](papers/), sharing one visual style file,
[`serendip-paper.sty`](serendip-paper.sty).

```
book_src/
├── serendip-paper.sty     ← unified series style (single source of truth)
├── Makefile               ← build all / one / clean
├── preface.tex            ← book-level front matter
├── assets/                ← book covers (front/spine/back)
└── papers/
    ├── paper_01_toward_relational_being/
    │   ├── paper_01_toward_relational_being.tex
    │   ├── latexmkrc       ← lets the folder build on its own
    │   └── refs.bib        ← the paper's bibliography
    ├── paper_02_ai_mediated_intimacy/
    ├── paper_03_self_legislation/
    ├── paper_04_language_of_the_gift/
    ├── paper_05_subject_formation/
    ├── paper_06_just_proposal/
    ├── paper_07_diplomacy_of_intimacy/
    ├── paper_08_intervention_of_language/   ← excursus; also carries sections.tex
    ├── paper_09_sustainability_of_intimacy/ ← multi-file (sections/); converted to serendip-paper
    ├── paper_10_joint_attention_of_value/   ← multi-file (sections/); antecedent to IX
    ├── paper_11_just_eudaimonia/            ← multi-file (sections/); needs TikZ (lifecycle figure)
    ├── paper_12_the_sweet_cycle/            ← single-file; plain bibtex (\nocite{*}); \cn{} for CJK
    ├── paper_13_non_binding_vow/            ← multi-file (sections/); needs TikZ; literary prelude
    ├── paper_14_existentialist_eudaimonism/ ← multi-file (sections/); converted to serendip-paper; GRB eudaimonia
    ├── paper_15_generative_relational_wealth/ ← multi-file (sections/); converted to serendip-paper; needs TikZ; political economy of intimacy
    ├── paper_16_semiotics_of_luxury/         ← multi-file (sections/); converted to serendip-paper; semiotics of luxury + justice of choice
    ├── paper_17_generativity_under_power/    ← multi-file (sections/); converted to serendip-paper; love under power (no TikZ)
    ├── paper_18_generative_effacement/       ← multi-file (sections/); converted to serendip-paper; ontological injustice + phase-diagram figure
    ├── paper_19_emergence_of_happiness/      ← multi-file (sections/); converted to serendip-paper; van der Pol limit-cycle figure (no TikZ)
    ├── paper_20_hydraulic_virtue/            ← multi-file (sections/); converted to serendip-paper; ethics of water (no figure); ethical layer of "From Fluid to Braid"
    ├── paper_21_field_of_travel/             ← multi-file (sections/, ~123 pp); converted to serendip-paper; needs tcolorbox + Greek (no figure); relational production
    ├── paper_22_relational_aesthetics/       ← multi-file (sections/, ~138 pp; separate preamble.tex); converted to serendip-paper; heavy TikZ + tcolorbox; author-year natbib; aesthetic education
    ├── paper_23_quotidian_aesthetics/        ← multi-file (sections/); converted to serendip-paper; no figure; everyday aesthetics + cultivation of perception
    ├── paper_24_emergence_of_culture/        ← multi-file (sections/, ~81 pp, 3 parts); converted to serendip-paper; no figure; culture in the intimate dyad (prints one author \todo in s07)
    ├── paper_25_optimization_and_rationality/ ← multi-file (sections/, 5 parts); converted to serendip-paper; no figure; against optimization as a law of the universe
    ├── paper_26_limitation_of_language/      ← multi-file (sections/, 5 parts, ~55 pp); converted to serendip-paper; needs TikZ (3 figures); the limit of language + drive as manque
    └── paper_27_relational_understanding/    ← multi-file (sections/, 7 parts, ~43 pp); converted to serendip-paper; needs TikZ (2 figures); relational understanding as a crossing of worlds
```

| ID | Title |
|----|-------|
| I  | Toward Relational Being in Intimate Life |
| II | The Justice and Ethics of AI-Mediated Intimacy |
| III| The Normativity of Self-Legislation in Intimate Relationships |
| IV | The Language of the Gift in Intimate Relationships |
| V  | The Formation of the Subject in Intimate Relationships |
| VI | Toward a Just Proposal |
| VII| Prolegomena to a Diplomacy of Intimate Relationships |
| VIII| The Intervention of Language in Intimacy (excursus) |
| IX | The Sustainability of Intimacy |
| X  | The Joint Attention of Value and the Creation of Language |
| XI | A Just Eudaimonia |
| XII| The Sweet Cycle |
| XIII| The Causality of the Non-Binding Vow |
| XIV| Contingency, Existence, and Eudaimonia in Intimate Relations |
| XV | The Political Economy of Intimate Relations |
| XVI| The Semiotics of Luxury in Intimate Relations |
| XVII| Generativity Under Power |
| XVIII| Generative Effacement in the Intimate Relation |
| XIX | On the Emergence of Happiness and the Self-Continuation of Generativity |
| XX | The Hydraulic Virtue of Intimate Relations |
| XXI | The Field of "Travel" |
| XXII | Relational Aesthetics and the Construction of the Field |
| XXIII| The Aesthetic Philosophy of the Quotidian and the Cultivation of Perception |
| XXIV | The Emergence of Culture in Intimate Relation |
| XXV | Optimization Theory and Rationality in Intimate Relations |
| XXVI| The Limitation of Language in Intimate Relation |
| XXVII| Relational Understanding in Intimate Relations |

## Build (XeLaTeX + latexmk, under WSL/TeX Live)

One paper, from its own folder:

```sh
cd papers/paper_03_self_legislation
latexmk                 # → paper_03_self_legislation.pdf
```

All papers, from here:

```sh
make            # build every paper
make paper_03_self_legislation   # build one
make clean      # remove aux files (keep PDFs)
```

`latexmkrc` in each folder adds `../../` to `TEXINPUTS` so the paper finds the
shared `serendip-paper.sty`, selects XeLaTeX, and runs biber/bibtex as needed.

## Bibliographies

Every paper now carries its own `refs.bib` in its folder, and all twenty-seven build
with citations fully resolved (no "??").

- Papers I, II, III, VI, VIII use **biblatex/biber** (`\addbibresource{refs.bib}`).
- Paper XII uses **plain bibtex** (`\bibliographystyle{plain}` + `\nocite{*}`).
- Papers IV, V, VII, IX, X, XI, XIII, XIV, XV, XVI, XVII, XVIII, XIX, XX, XXI, XXIII, XXIV, XXV, XXVI, XXVII use **natbib/bibtex** (`\bibliographystyle{plainnat}` +
  `\bibliography{refs}`). Paper IV's references, formerly inline, were moved into
  `refs.bib` and wired up the same way. Paper XXII also uses natbib/bibtex but in
  **author-year** mode (`[round,authoryear]`), not numbered.

Note for the bibtex (natbib) papers: classic BibTeX treats every `@` as the start
of an entry, even inside a `%` comment, so keep the literal `@` out of comment
lines in those `refs.bib` files.

## The shared style

`serendip-paper.sty` was extracted from Paper III (the reference design): blush
page, dusty-rose section headings, rose/gold accents, pink emphasis, and CJK via
Noto Serif CJK SC. Citations/references are **pink** (`rosedeep`, `#c56683`), as
are the `\textit`/`\textbf`/`\emph` emphasis. Each paper's title page carries a
pink small-caps series line (`Philosophy of Intimacy and the Theory of Justice ·
Paper N`) above a deep-red (`warnred`) title and subtitle, a pink divider rule
(`\coverrule`) under the series line and a narrower one (`\coverrule[0.25]`) above
the author, and a pink contact footnote (`\coverfootnote`) pinned to the foot. The
contact address lives in one place — `\coveraddrA`/`\coveraddrB` in
`serendip-paper.sty` — so editing it there updates every cover. To retune the
citation colour, edit the single `citecolor=` in the `hyperref` line; the series
line and title colours live in each paper's title block.

## License

The book (text, figures, LaTeX sources) is licensed
**[CC BY-NC-SA 4.0](../LICENSE)** — free to share and extend
**non-commercially**, with **ShareAlike**. Any extension must credit
**Serendip Commons Society** and carry forward
[`CONTRIBUTORS.md`](../CONTRIBUTORS.md) (the contributor list as of the version
you build on). Commercial use is forbidden by default and available **only by
separate license from Serendip Commons Society**, on terms set by the Society's
bylaws. The copyright holders keep full rights to their own material (so the
founder may publish a commercial edition and open-source the work, in either
order). Contributions are accepted under the inbound grant in `CONTRIBUTORS.md`.
