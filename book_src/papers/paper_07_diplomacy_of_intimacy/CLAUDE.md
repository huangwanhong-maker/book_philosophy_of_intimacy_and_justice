# Paper VII — Diplomacy of Intimacy

**Full title:** Prolegomena to a Diplomacy of Intimate Relationships
**Subtitle:** A First Step toward Generalized Generative Relational Being
**Status:** working draft (programmatic survey) · **Bibliography:** natbib/bibtex (numbered, plainnat)
**Build:** `make paper_07_diplomacy_of_intimacy` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
This paper takes the series' relational ontology — subjects constituted in and through relation — and pushes it past the closed dyad of Papers I–VI to the *external relational field*: the parents, lineage, friends, and anonymous norms that surround a couple from the moment it forms. That commerce with the outside it calls **diplomacy**, and its central claim is that the field is not an optional addition to the dyad but a constitutive condition of it. The leap is from *second-order coupling* (two subjects constituting each other) to *higher-order coupling* (the dyad-as-unit coupling with external terms), which brings structurally new phenomena — triangles, being-watched-as-a-whole, nested mentalizing, value circulation. Crucially the diplomacy is usually **asymmetric**: before parents and lineage the dyad petitions an authority that holds history, resources, and the power of definition, so the work is closer to tribute/fealty than to a treaty between equals. The paper is explicitly a **programmatic map**, not a single argument: it reviews twelve theoretical frameworks, analyses how they couple, maps a roadmap of sub-papers, and grounds the abstractions in anonymized thick-description cases. Across it runs a geometric-phase / "Value Foam" formalism in which a season of diplomacy is a closed circuit whose **holonomy** (non-trivial on a tilted field) measures irreversible deformation and the unconserved leakage of value to the stronger party.

## Structure
Cover → epigraph → TOC, then: Intro (dyad → world; second- to higher-order coupling) → methodological self-examination (why *no* central phenomenon: phenomena are symmetric, finite, organized by coupling not a hub; the form self-referentially enacts the content) → the twelve frameworks, each with its own review table (§3) → method/apparatus (review, analysis, mapping, thick description; the stratal coordinates) → the two fields + coupling matrix (static map) → **the Real** (the unsymbolizable remainder; short by principle) → **the Symbolic I–IV** (power topology → rites as grammar / value as sign → double grammar of law and rite → political economy of value creation/circulation/extraction) → **the mechanism bridge** (higher-order mentalizing → cautious neural implementation → POMDP/game-theoretic decision) → **the phenomenal I–II** (the triad / first other beyond the dyad → network and field: gift, address, seating, absence, cross-cultural double ceremony) → **justice** (the knot of distributive/recognitive/hermeneutical registers) → conclusion (literature map + roadmap of the sub-series) → acknowledgements → references.

## Key concepts & coined terms
- **External relational field / "diplomacy"** — the dyad's structured, stakes-laden commerce with the surrounding network of others.
- **Generalized Generative Relational Being (GRB)** — the larger programme: relation as generative, extended from dyad to arbitrary order; this paper is its first step.
- **Second- vs. higher-order coupling** — mutual constitution of two subjects vs. of the dyad-as-unit with external terms.
- **Asymmetric diplomacy** — the field is tilted (axes of generation, gender, economy, cultural capital, information); the in-marrying party enters low; goodwill softens but cannot flatten the gradient.
- **Value Foam / geometric (Berry) phase / holonomy of value** — a diplomatic season as a closed circuit; non-trivial holonomy = irreversible change and unconserved value leaking down the gradient (formal interface, deferred to a dedicated paper).
- **Relational value** — a fourth value beyond use/exchange/sign value: value a thing has in *generating or confirming a relation*; non-transferable, non-priceable.
- **The rites (礼 / lǐ)** — the soft *grammar* of the Symbolic (combinatorics, generativity, grammaticality judgments); law is the *hard* grammar.
- **The third set of rites** — the generative hope: a cross-cultural dyad fashioning a shared grammar belonging to neither family; two failure modes (dominance-as-synthesis; rootless pastiche); left an open question.
- **The gaze** — neither pure Sartre (objectification) nor pure Levinas (ethical summons); it takes the moral character of the field it crosses (critical phenomenology, Ahmed's orientation).
- **Brideprice as recognition vs. commodification** — same act faces both ways; honor or purchase decided by structure and reading, not the transfer; recognition can itself be ideological.
- **The knot of justice** — distributive + recognitive + hermeneutical injustice are one structure; hermeneutical injustice disables contestation of the other two, tightest where the field is most unequal.

## Local notes / quirks
- **natbib/bibtex, NUMBERED.** Classic-BibTeX rules apply (no `@` inside refs.bib comments; no simultaneous author+editor in `@book`). Style `plainnat`, `[numbers,sort&compress]`.
- **No formal abstract** (it is a programmatic survey / prolegomenon) — a candidate abstract lives in `../../../socarxiv_submissions.txt`.
- **`simon1983` = Barry Simon** ("Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase", PRL 1983), cited beside `berry1984` for the geometric (Berry) phase. **NOT Herbert Simon — do not "correct" it.**
- XeLaTeX (`% !TEX program = xelatex`); CJK via `\zh{...}` (Noto Serif CJK SC) for occasional Chinese terms.
- Bespoke cover page (decorative `\coverrule`, "[Working Draft]" / "not for citation" notes); custom macros `\emc`/`\emb` (rose italic/bold emphasis), `\xref`/`\pinkref` (rose cross-refs), `\goldrule`, `\todo`, and the `casebox` environment for thick cases.
- Heavy use of `longtable` literature-review tables (four columns: source / contribution / significance / limitation) and two `landscape` tables (twelve-framework synoptic map; phenomenon×dimension coupling matrix). Eleven tables in all.
- Numerous `\todo{...}` markers flag deferrals to later sub-papers — these are intentional, not omissions to fix.

## Files
- `paper_07_diplomacy_of_intimacy.tex` — main · `refs.bib` · `latexmkrc` · `paper_07_diplomacy_of_intimacy.pdf` (build output)
