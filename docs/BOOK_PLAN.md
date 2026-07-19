# BOOK_PLAN — Three Volumes

> The plan of record for turning the 27-paper series into three volumes.
> Decisions here are settled; the per-paper work is tracked in
> [`REVISION_TRACKER.md`](REVISION_TRACKER.md).

## 1. Decisions (settled)

| # | Decision | Chosen | Why |
|---|----------|--------|-----|
| D1 | Volume division | **Sequential, 9 / 9 / 9** — I–IX, X–XVIII, XIX–XXVII | Honours the order in which the thought actually developed. The series is a record of an inquiry, and the inquiry moved in this order. |
| D2 | Revision depth | **Full check-and-revise of every paper.** All 27 are drafts. | Author's instruction: nothing is final; each paper is checked and revised before it is compiled into a book. |
| D3 | Book form | **True book**, not a bound collection | Each paper becomes a chapter: continuous pagination, running heads, unified TOC, one deduplicated bibliography. Not 9 stapled preprints. |
| D4 | Bibliography backend | **biblatex + biber**, unified across all 27 | *Forced* by D3 — see §3. Also handles translated classics (`translator`/`origyear`) that bibtex mangles. |
| D5 | Reference lists | **Per-chapter**, via biblatex `refsection` | Each paper keeps its own reference list, as a collected-papers volume should; a consolidated bibliography can still be printed per volume. |
| D6 | Trim size | **B5 (176×250mm)** | Academic-monograph standard (Japan/ISO); its larger text block keeps a 1000+ page work bindable and near print-on-demand limits. A5 was too thick (Vol II/III ~1200pp); 6×9″ packs less. |
| D7 | Front matter | **Designed covers** (`assets/cover_front_vol*.pdf`, `cover_back_book.pdf`) + a single-page **Foreword** (book dedication) + the series **Preface** (Vol I) | Real-book covers, not a text title page. Author name on the cover; no organization/email/date. "Serendip Commons Society" removed per author. |
| D8 | 致辞 / 致谢 | Each chapter carries its **致辞 (Dedication)** as an independent `\section*` and keeps its **致谢 (Acknowledgements)** | The standalone papers' full-page dedications become sections in the book; papers that fold the dedication into the acknowledgements keep it there. |

## 2. The three volumes

Sequential division. Word/page counts are from the baseline build (2026-07-12).

### Volume I — Papers I–IX  (~156k words, ~351 pp)
| # | Paper |
|---|-------|
| I | Toward Relational Being in Intimate Life |
| II | The Justice and Ethics of AI-Mediated Intimacy |
| III | The Normativity of Self-Legislation in Intimate Relationships |
| IV | The Language of the Gift in Intimate Relationships |
| V | The Formation of the Subject in Intimate Relationships |
| VI | Toward a Just Proposal |
| VII | Prolegomena to a Diplomacy of Intimate Relationships |
| VIII | The Intervention of Language in Intimacy (excursus) |
| IX | The Sustainability of Intimacy |

### Volume II — Papers X–XVIII  (~281k words, ~624 pp)
| # | Paper |
|---|-------|
| X | The Joint Attention of Value and the Creation of Language |
| XI | A Just Eudaimonia |
| XII | The Sweet Cycle |
| XIII | The Causality of the Non-Binding Vow |
| XIV | Contingency, Existence, and Eudaimonia in Intimate Relations |
| XV | The Political Economy of Intimate Relations |
| XVI | The Semiotics of Luxury in Intimate Relations |
| XVII | Generativity Under Power |
| XVIII | Generative Effacement in the Intimate Relation |

### Volume III — Papers XIX–XXVII  (~311k words, ~629 pp)
| # | Paper |
|---|-------|
| XIX | On the Emergence of Happiness and the Self-Continuation of Generativity |
| XX | The Hydraulic Virtue of Intimate Relations |
| XXI | The Field of "Travel" |
| XXII | Relational Aesthetics and the Construction of the Field |
| XXIII | The Aesthetic Philosophy of the Quotidian and the Cultivation of Perception |
| XXIV | The Emergence of Culture in Intimate Relation |
| XXV | Optimization Theory and Rationality in Intimate Relations |
| XXVI | The Limitation of Language in Intimate Relation |
| XXVII | Relational Understanding in Intimate Relations |

## 3. Why the bibliography must be unified (D4)

This is not a preference; it is a hard constraint.

- Papers **I, II, III, VI, VIII** use `biblatex` + biber.
- Papers **IV, V, VII, IX–XI, XIII–XXVII** use `natbib` + bibtex.
- Paper **XII** uses plain bibtex with `\nocite{*}`.

`biblatex` and `natbib` **cannot be loaded in the same LaTeX document**. Volume I
alone spans both groups (I–III, VI, VIII are biblatex; IV, V, VII, IX are
natbib). So no volume can compile until one backend wins. We unify on
`biblatex` + biber (D4).

## 4. Citation conflicts to reconcile

The 27 `refs.bib` files hold **3,672 entries collapsing to 764 unique keys**.
Of the 327 keys used by more than one paper:

- **243** are byte-identical everywhere — safe to merge automatically.
- **84 carry conflicting variants** — the same key asserting different facts.
  These are citation errors and must be resolved against the actual sources.

Example (`eglash2016`, *An Introduction to Generative Justice*, Teknokultura 13(2)):

| Papers | pages |
|--------|-------|
| IV, XXIV, and others | `369--404` |
| IX | `369--388` |

One of these is wrong. `CLAUDE.md` §5 forbids unverified citations, so each of
the 84 is checked against the source, not silently deduplicated by picking the
majority.

Resolution lands in a single `book_src/bib/master.bib`; per-paper `refs.bib`
files are retired in favour of it.

## 5. Build architecture

Each paper keeps a **standalone** build (they are published individually on
SSRN/OSF and must not stop building), while also being includable as a chapter.
Achieved by splitting each paper in two:

```
book_src/
├── bib/master.bib             ← one deduplicated bibliography (764 entries)
├── serendip-paper.sty         ← shared style, standalone papers (unchanged role)
├── serendip-book.sty          ← NEW: book preamble = union of all paper packages
│                                 + the unified macro set
├── papers/paper_NN_slug/
│   ├── paper_NN_slug.tex      ← standalone: preamble + cover + \input{content} + bib
│   └── content.tex            ← NEW: the body alone — no preamble, no title page
└── volumes/
    ├── volume_1.tex           ← book class; \chapter per paper + \input{../papers/…/content}
    ├── volume_2.tex
    └── volume_3.tex
```

Both paths read the same `content.tex`, so a paper can never drift between its
standalone and its in-book form.

### Structural facts that make this safe
- **No paper uses `\part`.** Top level everywhere is `\section`, which sits
  correctly under `\chapter` in the `book` class. No heading demotion needed.
- Package set across all 27 is a clean union (fontspec, tikz, graphicx, caption,
  tabularx, ragged2e, float, csquotes, epigraph, makecell, amsthm, pdflscape).

### Macros to unify in `serendip-book.sty`
Most are already identical across papers (`\emc`, `\emb`, `\xref`, `\goldrule`).
Genuine conflicts, to be settled once:

| Macro | Conflict | Resolution |
|-------|----------|------------|
| `\zh` | `{\cjkfont #1}` vs `{\cjk #1}` | one CJK font command |
| `\term` | II: `\textit{\textcolor{pinkitalic}{#1}}` vs XXII: `{\color{rose}\itshape #1}` | one definition |
| `\el` | XXI: `{\grk #1}` vs XXII: `{\greekfont #1}` | one Greek font command |
| `\arraystretch` | 5 numeric values | set per table, not globally |

## 6. Order of work

1. **Infrastructure** — master bib; natbib→biblatex conversion; `content.tex`
   split; `serendip-book.sty`; volume masters that compile.
2. **Revision** — the careful check-and-revise pass over each of the 27 drafts
   (see `REVISION_TRACKER.md`). This is the substance of the work.
3. **Compile** — build and proof the three volumes.

Infrastructure comes first so that revision happens against a book that already
builds, and every revised paper can be seen in its final form immediately.

## 7. Known defects (from the baseline build, 2026-07-12)

All 27 papers build with **0 undefined citations**. Open defects:

- **Paper VI** — 3 broken `\ref`s to a nonexistent label `sec:mapping`.
- **Paper XXIV** — prints an author `\todo` note into the PDF (`s07_chinese.tex`),
  flagging classical-Chinese material the author deliberately left unasserted.
- **84 conflicting bib keys** (§4).
