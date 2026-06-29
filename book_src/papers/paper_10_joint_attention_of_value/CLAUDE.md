# Paper X — The Joint Attention of Value and the Creation of Language

**Full title:** The Joint Attention of Value and the Creation of Language: A Relational Dynamical Grammar
**Subtitle:** On the Co-Perception of What Has No Name Yet, the Reflexive Generation of the Subject, and the Practice of a Good That Cannot Be Guaranteed
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 54 entries)
**Build:** `make paper_10_joint_attention_of_value` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
This is the **antecedent** to Paper IX. Where IX asked whether a generative cycle is *good* and *sustainable*, Paper X asks the prior question: **how relation and value are constituted at all** — how a value *not yet named* comes to be, and how the language by which a bond subsists is *made*. It proceeds **in order of grounding**:

1. **Phenomenology** — the pre-theoretical datum: two persons co-apprehend a value generated between them and not yet symbolised.
2. **Ontology** — derived from that datum: relation as the being of a generative system, grammar as the manifestation of its dynamics, value as its phenomenon; the phenomenon **reflexively reconfigures** the dynamics that produce it, and **the subject is generated within the cycle it generates**.
3. **Formal epistemologies (admitted only thereafter)** — (a) a **quantum-structural relational grammar**, used strictly as an *epistemic model, not a physical hypothesis*: co-apprehension is a **participatory measurement that generates rather than registers** its value; and (b), symmetrically, the **political-economic** thesis that the circulation of value reconfigures the subject who creates it — **alienation and self-realisation as the negative and positive phase of one reflexive cycle**, distinguished by the sign of an independently definable **reproduction surplus**.

These are **symmetry-broken phases of one abstract structure** that no framework possesses externally; their plurality is presented as the method **dialectical materialism requires of a totality not yet complete**, not as eclecticism. It concludes in **praxis** (not the construction of a grammar but the **cultivation of a field** within which a grammar admits continual *joint reconfiguration*) and **ethics**: **no finite subject can guarantee the goodness of its own practice** — one that could would have crossed the **is–ought gap** and become the infinite reason the series denies; that impossibility is what makes the good *ethics rather than calculation*, an *unfinished process rather than a possessible state*.

## Structure (sections/ \input by main, in reading order)
intro (Introduction) → litreview (background & theoretical frameworks) → s0_registers (the three registers as coupled systems) → s1_phenomenology (phenomenology of nameless co-generation) → s2_structure (the structure of the phenomenon) → s3_ontology (relation, grammar, value) → s4_grammar (Epistemology I: the quantum-structured grammar) → s_modelling (the formal-modelling dilemma) → s5_political (Epistemology II: value rewrites the subject) → s6_breaking (symmetry-breaking and how we know the mother-structure) → s7_praxis (cultivating a generative field) → s_field_matter (the matter of the field) → s_exploitation (exploitation in symbolic generation) → s8_keystone (the good that cannot be guaranteed; Hume) → s9_conclusions → s10_envoi → s11_ack → appendixA (geometric phase, technical sketch).

> The `% §N` numbers in the main file's `\input` list are **upstream-inconsistent** (e.g. two "§5"/"§6"); the authoritative numbering comes from the `\section` commands in the files. Cosmetic only — left as received.

## Key concepts & coined terms
- **Joint attention of value** — two subjects co-apprehending a value generated between them and not yet symbolised (cf. Paper V's joint attention; here the shared object is an *unnamed value*).
- **Relational dynamical grammar** — grammar as the manifestation of a generative system's dynamics, not a static code.
- **Reflexive generation of the subject** — the subject is produced within the very cycle it produces (the phenomenon reconfigures its own dynamics).
- **Participatory measurement** — co-apprehension *generates* rather than registers value (quantum-structural model, epistemic not physical).
- **Alienation / self-realisation as ± phase** — negative vs positive phase of one reflexive cycle, distinguished by the sign of a reproduction surplus (geometric-phase reading; cf. Papers VII, IX).
- **Symmetry-breaking of one mother-structure** — the quantum-grammatical and political-economic accounts are symmetry-broken phases of a single structure no framework owns; plurality as dialectical-materialist method (cf. Paper VIII's "poetics of truth").
- **Cultivation of the field** (praxis) — fostering conditions for continual *joint* reconfiguration of the grammar, not legislating a grammar.
- **The good that cannot be guaranteed** — the is–ought gap (Hume): a finite subject cannot guarantee its own practice is good; that limit constitutes ethics.
- Cross-links: **Paper IX** (successor question: good/sustainable), Paper V (joint attention, subject formation), Paper VIII (generativity, symmetry-breaking), Paper IV (value/gift, formal grammar), Paper VII (geometric phase, political economy of the field), Paper III (self-legislation).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; 54 entries). classic-BibTeX rules apply (no `@` in refs.bib comments — already clean; no author+editor in `@book`).
- **Multi-file:** body in `sections/` (18 files + `abstract.tex`), `\input` by the main tex in reading order.
- **Converted to the shared style:** originally shipped with a bespoke preamble (TeX Gyre Pagella + own palette); now `\usepackage{serendip-paper}` + the unified cover (pink series line, deep-red title, `\coverrule`×2, `\coverfootnote`). Paper-specific macros kept: `\holo`, `\zh`/`\cjk`, `\emc`/`\emb`, `\goldrule`, `\todo`, `\xref`/`\pinkref`, `claim`/`casebox`; tables via `tabularx`/`ragged2e` + the `Y` column. Heavy math (quantum-structured grammar) uses serendip's `amsmath`/`amssymb`.
- The zip also contained `Paper_X_standalone.tex` (a single-file, all-inlined version); **not deployed** — the series uses the multi-file form.
- `\todo{...}` markers are intentional deferrals.

## Files
- `paper_10_joint_attention_of_value.tex` — main (preamble, cover, epigraph, dedication, abstract, `\input` of sections, bibliography)
- `sections/` — 18 body files (+ `abstract.tex`) · `refs.bib` (54) · `latexmkrc`
