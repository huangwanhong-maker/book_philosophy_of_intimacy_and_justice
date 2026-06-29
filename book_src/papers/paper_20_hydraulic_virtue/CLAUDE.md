# Paper XX — The Hydraulic Virtue of Intimate Relations

**Full title:** The Hydraulic Virtue of Intimate Relations: On the Ethics of Water
**Subtitle:** On the Ethics of Water
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 142 entries)
**Build:** `make paper_20_hydraulic_virtue` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
An ethics of intimate relations built from the Daoist figure of **water** — 上善若水, "the highest good is like water" (*Daodejing* ch.8). It asks what it is, concretely and between two people, for love to **benefit without contending**, to **seek the lowly place**, and to **remain unfilled**. The decisive move is to read the water-virtues **structurally, not as self-cultivation**: not an ascent toward a selfless or quasi-divine condition, but properties of how value, power, and desire are *arranged* in a generative relation. Its resources are therefore drawn less from the contemplative traditions than from **political economy, game theory, political philosophy, feminist ethics, Kantian ethics, and psychoanalysis** (the contemplative reading is one voice among many, not the frame).

A doctrinal survey organised around the water-virtues — non-contention, benefiting the ten thousand things, dwelling in the lowly place, formlessness, non-fullness — shows each is both affirmed and opposed, and isolates **five standing challenges**: non-contention is irrational (game theory); it is suicidal absent an enforced structure (Hobbes); dwelling-below is slave morality (Nietzsche); taking the receiver's shape dissolves the subject (feminism, psychoanalysis); formlessness is lawlessness (Kant). The last is answered in place by reading the water-good as an **imperfect duty** (lawful yet without fixed form), using Kant's own resources. The **dialectical core** answers the rest in two clusters: against self-dissolution and slave morality, the water-good is not formless yielding but **chosen good** — water takes the vessel's shape (utmost softness) yet wears through stone and breaches dykes (utmost hardness), so a **rigid lower bound** distinguishes the generative lowly place from mere collapse; against irrationality and suicide, the water-good never demanded the **abolition of power**, only the shaping of an ineliminable asymmetry so its **surplus is returned rather than retained** (following the formal companion). A practice chapter carries each virtue into the conduct of an actual relation, pairing every good with the vice it most easily becomes, and closing on the limit of all such guidance: **the good cannot be made into a procedure**.

## Companion paper (formal layer)
This is the **ethical upper / "translation" layer** of the author's formal companion **Huang (2026), "From Fluid to Braid"** (Knowledge Commons, DOI 10.17613/j9kjd-vce60; cite key `wan2026braid`). The companion's formalism is used as a **settled foundation and translated, not rebuilt**: non-contention ↔ the vanishing of appropriative (gradient) transport in the **holonomy** that carries surplus; the good vs bad lowly place ↔ the **solenoidal vs gradient** parts of the power force; renewal ↔ avoidance of dynamical **solidification**; and the **non-substitutable particularity of *this* relation** ↔ the local "flesh" that topological protection, by construction, cannot reach. The water-good is the **water-phase of the dark virtue** (玄德, ch.51): the companion's non-possessive generativity given an ethical and practical body.

## Structure (sections/ \input by main, in reading order)
s01 From the Hydraulics of Value to the Ethics of Water → s02 The Ethics of the Water-Virtues: A Doctrinal Survey → s03 The Generativity of Non-Contention → s04 The Political Economy of the Lowly Place → s05 The Dialectical Core: Water-Good, Not Formlessness → s06 Non-Fullness and Renewal → s07 The Practice of the Water-Virtue (each good paired with its vice) → s08 Watershed: From the Dyad to the Basin → s09 Formal Expression: The Translation Layer → s10 Directed Fissures (the anti-envoi) → s11 Acknowledgements.

## Key concepts & coined terms
- **The water-good / hydraulic virtue (上善若水)** — the water-virtues read structurally as an arrangement of value, power, and desire in a generative relation, not as self-cultivation.
- **Chosen good, not formless yielding** — water takes the vessel's shape yet wears stone; a **rigid lower bound** separates the generative lowly place from collapse (answers slave-morality / self-dissolution).
- **Shaping, not abolishing, power** — the surplus of an ineliminable asymmetry is **returned rather than retained** (answers the irrationality / suicide charges).
- **The water-good as imperfect duty** — lawful yet without fixed form (Kantian answer to "formlessness is lawlessness").
- **Non-contention / the lowly place / non-fullness** — translated formally to vanishing gradient transport in holonomy; solenoidal vs gradient power force; avoidance of solidification.
- **The non-substitutable "flesh" of this relation** — the local particularity topological protection cannot reach (the philosophy-of-intimacy crux).
- **The dark virtue (玄德)** — non-possessive generativity ("generating yet not possessing"); the water-good is its water-phase.
- Cross-links: ethical layer of `wan2026braid`; extends **Paper XVII** (power), **Paper XV** (political economy / surplus), **Paper IX** (holonomy), **Paper XVIII** (non-determination).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; **142** entries). Two classic-BibTeX faults in the shipped `refs.bib` were fixed on deploy (same base as XIX): a **repeated key** `wang2021delayed` (duplicate removed) and `whitehead1978` carrying both `author`+`editor` (editor folded into `note`). `trevarthen1979` (@article) and `adorno1991` (@incollection) keep `editor` legitimately.
- **No figure, no TikZ.** `graphicx`/`caption` are loaded (harmless; kept from the source) but unused.
- Multi-file: body in `sections/` (11 files + `abstract.tex`), `\input` by the main tex; the source zip also shipped `_test_group*.out` files (discarded on deploy) and a `main.pdf` (rebuilt).
- **Converted to the shared style** from the bespoke preamble (Pagella + own palette) to `\usepackage{serendip-paper}` + the unified cover (pink scshape series line, `warnred` title, `\coverrule`×2, `\coverfootnote`). Twin Laozi epigraphs (ch.8, ch.51) and a bilingual dedication. Macros: `\holo`, **`\Shan`** (`\operatorname{善}`, the water-good predicate), **`\fpow`**, `\zh`/`\cjk`, `\emc`/`\emb`, `claim`/`casebox`, `\goldrule`, the `Y` column.

## Files
- `paper_20_hydraulic_virtue.tex` — main (preamble, cover, twin epigraphs, dedication, abstract, `\input` of sections, bibliography)
- `sections/` — 11 body files + `abstract.tex` · `refs.bib` (142) · `latexmkrc`
