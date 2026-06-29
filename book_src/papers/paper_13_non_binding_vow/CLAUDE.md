# Paper XIII — The Causality of the Non-Binding Vow

**Full title:** The Causality of the Non-Binding Vow: On Trust, Promise, and the Generation of Expectation in the Absence of the Other's Sword
**Subtitle:** On the Mechanism by which a Promise without Force Generates Trust, the Translation of Sincerity across the Borders of Epistemology, and the Descent of a Relational Divinity
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 140 entries — the largest in the series)
**Build:** `make paper_13_non_binding_vow` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
How can a promise that carries **no enforcing force** — a vow, a betrothal document, a memorandum of understanding — nonetheless generate **real, well-founded trust**? From a **symptomatology** of the contemporary condition (the apparatus of assurance proliferates at every scale while the trust it secures grows scarcer), it **diagnoses** the failure as a mistake about **causation**: taking *force* (the mechanical cause) for the cause of an effect — trust — that is in fact **inferential and free**. Through the philosophy of law it traces the migration of the anchor of legal validity **from force toward trust** (recorded at law's technical edge in **promissory estoppel**), arguing the inferential cause is a different kind of thing: it **addresses a free being as free**.

Its central contribution is a **mechanism**: *trust is the precision a receiver's generative model assigns to the prediction that a promise will be kept*, generated through **three coupled channels** — a **structural prior**, a **high-fidelity self-committing likelihood**, and a **wagered prior** — whose **multiplicative coupling** makes genuine trust **robust where any single channel is forgeable**. It gives this a **geometric reading** (holonomy) and, for relational trust, a **structural reading in open quantum-system dynamics**; states the **criterion of justice** distinguishing genuine trust from forged; develops a theory of the **translation of sincerity across incommensurable epistemologies**; and, in a **historical-materialist** register, reconceives the optimisation of the juridical as the **decentralisation of enforcement**. At its summit it claims that the **self-legislation, self-adjudication, and self-keeping** of a subject who binds himself without recourse is the **descent of a relational divinity** — so the non-binding vow is the *purer* realisation of what a promise is. It ends in **plural conclusions**, refusing in its own form the synthesis its thesis forbids.

## Structure (sections/ \input by main, in reading order)
prelude (literary entry) → intro → symptomatology → diagnosis → jurisprudence → freedom → mechanism → holonomy → justice → relational → translation → judicial → praxis → conclusions → envoi → acknowledgements.

## Key concepts & coined terms
- **The non-binding vow** — a promise with no enforcing sword behind it (vow / betrothal / MOU); the paper's object.
- **Inferential cause vs mechanical cause** — trust is caused inferentially (by a free being reading another as free), not mechanically (by force); mistaking the two is the diagnosed error.
- **Trust as precision** — trust = the precision a receiver's generative model assigns to "the promise will be kept" (predictive-processing / free-energy reading).
- **Three coupled channels** — structural prior · self-committing likelihood · wagered prior; **multiplicative coupling** → robust where any single channel is forgeable.
- **Promissory estoppel** — the law's own record of validity migrating from force to trust.
- **Holonomy reading** + **open quantum-system dynamics** — geometric and structural models of (relational) trust (cf. Papers VII/IX/XI).
- **Genuine vs forged trust** — the criterion of justice (cf. Paper XII's forged holonomy).
- **Translation of sincerity** — across incommensurable epistemologies.
- **Decentralisation of enforcement** — historical-materialist reading of "optimising the juridical".
- **Descent of a relational divinity** — self-legislation + self-adjudication + self-keeping without recourse as the purer realisation of the promise.
- Cross-links: Paper III (self-legislation / the lover's vow), Paper VI (the proposal; epistemic agency), Papers IX/XI (holonomy; genuine vs forged), Paper XII (forged vs genuine cycle), Paper X (the free being; is–ought).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; **140 entries — largest refs.bib in the series**). classic-BibTeX rules apply (no `@` in refs.bib comments — clean).
- **TikZ** required (diagrams): converted preamble adds `\usepackage{tikz}` + `\usetikzlibrary{arrows.meta,positioning,calc,decorations.pathmorphing}` (like Paper XI).
- **Multi-file:** body in `sections/` (16 files + `abstract.tex`), `\input` by the main tex; a literary **`prelude`** is `\input` before the body.
- **Converted to the shared style** from the bespoke preamble (Pagella + own palette) to `\usepackage{serendip-paper}` + the unified cover. Paper-specific macros kept: `\holo`, `\zh`/`\cjk`, `\emc`/`\emb`, `\goldrule`, `\todo`, `\xref`/`\pinkref`, `claim`/`casebox`; tables via `tabularx`/`ragged2e` + the `Y` column. Heavy math (precision / open-system dynamics) uses serendip's `amsmath`/`amssymb`.

## Files
- `paper_13_non_binding_vow.tex` — main (preamble, cover, epigraph, dedication, abstract, prelude, `\input` of sections, bibliography)
- `sections/` — 16 body files + `prelude.tex` + `abstract.tex` · `refs.bib` (140) · `latexmkrc`
