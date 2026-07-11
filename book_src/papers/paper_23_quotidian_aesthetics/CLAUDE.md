# Paper XXIII — The Aesthetic Philosophy of the Quotidian and the Cultivation of Perception

**Full title:** The Aesthetic Philosophy of the Quotidian and the Cultivation of Perception (《日常的美学哲学与美育》)
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 182 entries)
**Build:** `make paper_23_quotidian_aesthetics` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
An **aesthetics of the everyday** and, on its basis, a **theory of aesthetic education**. The guiding claim: everyday aesthetic perception — small in amplitude, prone to **go dead through habituation** — is **generated rather than given**, coming to be in the relation between a perceiver and what is perceived and, in the cases that matter most, **between two perceivers turned together toward a shared world**. From this it proposes **generative relational aesthetic education**, one thesis with **four faces**: (1) beauty is generated within a relational structure; (2) an education in beauty must therefore cultivate the **relation, not only the individual** — marking it off from the individualist tradition from **Schiller** onward; (3) the relational and the individual stand in a **spiral dialectic** in which neither is prior; (4) aesthetic generation carries an **ethical valence at its root**, so beauty and ethics share a single source rather than being joined by a later moral rule.

The argument runs in **three spines — generation, the body, and justice**: across phenomenology, cognitive science, psychoanalysis, and the political economy of the senses it argues **perception constructs a world under a prior frame**; it gives this empirical ground in the **neuroscience of perceptual plasticity**; and, through **the distribution of the sensible** (Rancière), it shows the **uneven distribution of perceptual capacity is a neglected injustice**. On this ground it offers, as a preliminary and openly revisable contribution, **four models of everyday aesthetic practice**, each with its theoretical descent made explicit: (a) a **basic generative cycle**; (b) a **reflective variant beginning in silence**, where reception suspends private judgement; (c) **the leaving of emptiness**, a field in which contingency may generate of itself; and (d) an **iterative symbolic refinement** modelled on evolution without a fitness function. It closes not in synthesis but in **directed fissures**, the first pointing toward the emergence of culture in intimate relation.

## Structure (sections/ \input by main, in reading order)
s01 Introduction → s02 The Phenomenology and Diagnostics of the Everyday → s03 The Generation of Perception: Several Schools → s04 The Symbolic Order and Its Two Fates → s05 Value, Perception, and Circulation → s06 The Philosophy of the Body → s07 The Neural Plasticity of Perception → s08 The Convergence of the Schools: Toward Generative Relational Aesthetic Education → s09 Aesthetic Education: From Tradition to the Relational → s10 The Design of Space and Perception → s11 The Theory and Existing Forms of Everyday Practice → s12 A Typology of Everyday Aesthetic Practice → s13 The Distribution of the Sensible → s14 The Ethical Limits of Aesthetic Education → s15 Directed Fissures (anti-envoi).

## Key concepts & coined terms
- **Generative relational aesthetic education** — the central thesis: beauty is generated within a relational structure, so an education in beauty must cultivate the relation, not only the individual.
- **Perception is generated, not given** — everyday aesthetic perception comes to be in the relation between perceiver and perceived, and above all between two perceivers turned toward a shared world.
- **The four faces** — relational generation of beauty; cultivate-the-relation (contra Schiller's individualism); the relational/individual spiral dialectic; the shared root of beauty and ethics.
- **Three spines** — generation (perception constructs a world under a prior frame), the body (perceptual plasticity as empirical ground), justice (the distribution of the sensible).
- **The distribution of the sensible** — after Rancière: the uneven distribution of perceptual capacity is a neglected injustice.
- **The four models of everyday practice** — basic generative cycle; reflective variant beginning in silence; the leaving of emptiness (contingency generates of itself); iterative symbolic refinement (evolution without a fitness function).
- **The symbolic and its two fates** — the fork by which the symbolic either deadens or renews perception.
- Cross-links: close sibling of **Paper XXII** (relational aesthetics / aesthetic education) and **Paper XXI** (the field); the "leaving of emptiness" echoes XXI's spaciousness (虚); the good cycle / holonomy of **Paper IX**; the first fissure points toward the emergence of culture in intimate relation.

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; **182** entries). On deploy, three classic-BibTeX faults in the shipped `refs.bib` were fixed: the recurring duplicate key `wang2021delayed` (removed); and **two** `@book` entries carrying both `author`+`editor` — `whitehead1978` and `bohme2017` (editors folded into `note`). (`saito2017` is author-only; `tomasello2008`/`barthes2005`/`marx1844` carry no editor — all fine.)
- **No figure, no TikZ.** `graphicx`/`caption` loaded (kept from source) but unused.
- Multi-file: body in `sections/` (15 files + `abstract.tex`), `\input` by the main tex; the source zip shipped a `main.pdf` (rebuilt) and an `OUTLINE.md` (kept).
- **Converted to the shared style** from the bespoke preamble (Pagella + own palette) to `\usepackage{serendip-paper}` + the unified cover (pink scshape series line, `warnred` title — manual `\\` removed — `\coverrule`×2, `\coverfootnote`; the source's foot had repeated the series line). Epigraphs: 大道至简，大美在常 + 一期一会 (the way of tea). **Anonymous** dedication ("For her / 致她", "who taught me to see the light in ordinary days"). Macros: `\holo`, `\zh`/`\cjk`, `\emc`/`\emb`, `claim`/`casebox`, `\goldrule`, the `Y` column.

## Files
- `paper_23_quotidian_aesthetics.tex` — main (cover, epigraph, dedication, abstract, `\input` of sections, bibliography)
- `sections/` — 15 body files + `abstract.tex` · `refs.bib` (182) · `latexmkrc` · `OUTLINE.md` (upstream notes)
