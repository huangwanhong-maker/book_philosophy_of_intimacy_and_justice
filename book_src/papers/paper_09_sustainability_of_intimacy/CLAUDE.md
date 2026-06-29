# Paper IX — The Sustainability of Intimacy

**Full title:** The Sustainability of Intimacy: Poetic Generativity and Generative Justice
**Subtitle:** On the Good and the Vicious Circle, the Geometry of Sublimation, and a Eudaimonics of the Relational Field
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 26 entries)
**Build:** `make paper_09_sustainability_of_intimacy` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
Where the earlier papers asked how a relation *begins*, this one asks how it does **not end** — under what conditions a generative bond reproduces itself across time. The problem: *self-continuation is morally indifferent* — capital, a rose, and a parasitic bond all continue themselves no less than love does — so Eglash's recursive return of value is necessary but not sufficient. The paper supplies the missing temporal dimension with an **axiom of sustainability cast in the language of geometric phase**: the *vicious cycle* is a circle of **zero holonomy** (returns unchanged), the *good cycle* is a **spiral that returns to its root while sublimating** (non-zero holonomy). It then asks how, through signs, such a spiral can be fostered, and argues that the **appropriate (non-possessive) poem** — the interpretive cycle that generates real value without seizing it — is the form of the good circle. Hence its constructive thesis: **generative justice in the intimate domain is necessarily poetic**. A eudaimonics of the relational *field*, the perception and co-creation of relational value, securing the return under asymmetry, and the gift as a threshold phenomenon complete the account.

## Structure (sections/ \input by main, in reading order)
§1 Prelude (the rose in the garden) → §2 Thesis (generativity takes its own continuation as its end) → §3 Antithesis (self-continuation is morally indifferent) → §4 Synthesis (the axiom of sustainability; geometric phase) → §5 Epistemology (the diagnosis of curvature) → §6 Praxis (the strategy of no-strategy / 无为) → §7 Semiotics (the poem as paradigm) → §8 Poeticity does not guarantee the good → §9 The non-possessive poem → §10 Legislation as a flow (contract, morality, self-legislation) → §11 Eudaimonics (the field) → §12 The perception of relational value → §13 Cultivation of the field & co-creation of value → §14 Securing the return (legislative practice under asymmetry) → §15 The gift (threshold across the three registers) → §16 Conclusions → Envoi (how to think of that rose) → Acknowledgements → Appendix A (geometric phase, technical sketch / SFM).

## Key concepts & coined terms
- **Sustainability of intimacy** — the temporal question: under what conditions a generative bond reproduces itself across time.
- **The good vs. the vicious circle** — geometric-phase reading: zero-holonomy circle (returns unchanged, mere self-continuation) vs. a spiral that returns to its root while sublimating (non-zero holonomy).
- **Axiom of sustainability** — the missing temporal supplement to Eglash's recursive return of value (necessary but not sufficient).
- **The appropriate / non-possessive poem** — the interpretive cycle that generates real value without possessing it (生而不有); the form of the good circle.
- **Generative justice is poetic** — in the intimate domain, sustaining unalienated value is structurally the poem's mode.
- **Eudaimonics of the field** — flourishing read at the level of the relational field, not the isolated subject.
- **Relational value** — value a thing/act has in generating or confirming a relation; its perception, cultivation, and co-creation.
- **Securing the return under asymmetry** — legislative practice when the field is tilted (cf. Paper VII).
- Cross-links: Paper VIII (poetic generativity), Paper IV (generative justice / Eglash / the gift), Paper VII (geometric phase / holonomy), Paper III (self-legislation), Paper V (relational value, attention).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`). classic-BibTeX rules apply (no `@` in refs.bib comments; no author+editor in `@book`). refs.bib is already clean.
- **Multi-file:** body is in `sections/` (20 files), `\input` by the main tex in reading order; abstract is `sections/abstract.tex`.
- **Converted to the shared style:** originally shipped with a bespoke preamble (TeX Gyre Pagella + its own palette); now `\usepackage{serendip-paper}` + the unified cover (pink series line, deep-red title, `\coverrule`×2, `\coverfootnote`). Paper-specific macros kept: `\holo` (geometric phase), `\zh`/`\cjk` (CJK), `\emc`/`\emb`, `\goldrule`, `\todo`, `\xref`/`\pinkref`, and the `claim` / `casebox` environments; tables via `tabularx`/`pdflscape`/`ragged2e` + the `Y` column.
- `\todo{...}` markers are intentional deferrals, not omissions to fix.
- The original `README.txt` (build notes) is kept in the folder for reference.

## Files
- `paper_09_sustainability_of_intimacy.tex` — main (preamble, cover, epigraph, dedication, abstract, `\input` of sections, bibliography)
- `sections/` — 20 body files (+ `abstract.tex`) · `refs.bib` · `latexmkrc` · `README.txt` (upstream build notes)
