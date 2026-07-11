# Paper XXV — Optimization Theory and Rationality in Intimate Relations

**Full title:** Optimization Theory and Rationality in Intimate Relations (《亲密关系中的优化理论与理性》)
**Subtitle:** On the Limits of Optimization as a Law of the Universe
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 27 entries)
**Build:** `make paper_25_optimization_and_rationality` (from book_src/; WSL TeX Live — see ../../CLAUDE.md). ~42 pp, 15 sections in five parts.

## What it argues
**Optimization is not a law of the universe**, and morality and the manner of being of intimate relation are not, *in their structure*, optimization problems. The paper keeps two movements strictly apart. The **first is a formal proof, carrying no value judgment**, that intimate relation furnishes **no well-defined optimization problem** — via **four impossibilities**, each striking a distinct precondition, any one of which leaves maximization undefined:
1. **Non-structurability of value** — the *drive*, which any complete objective must include, resists representation as a term.
2. **Relationality of value** — value is generated within the relation and exists only there, so no external standpoint could fix the objective (the absent quantifier).
3. **Incommensurability** — to price certain goods is to **betray rather than mismeasure** them.
4. **Constitution of the subject** — the subject is constituted *within* the relation, so the optimizer the model presupposes is a product of the very process it is meant to stand outside of.

The **second movement takes that result as given and criticizes imposing the frame anyway**: to optimize where no optimization problem exists converts a value that should **circulate** into one that can be **settled and drawn off** — the *extractive computation* named by the theory of **generative justice**; it is a **symptom of the crisis of the symbolic** and of a life-world habituated to the logic of capital (a local, historical operation projected onto the cosmos as its law); and it **mistakes the kind of thing morality is**, since an optimizing practice, even a successful one, may fail as an ethics — **the optimal and the good are orthogonal**. The paper then **recovers a rationality that responds rather than maximizes** — described through **response, attunement, and the sustaining of generation** — and raises **wuwei (non-action) as the highest rationality**. It **closes in polyphony, refusing to name a new master objective**, since to do so would reinstate the frame; that refusal is the paper's positive claim, **enacted in its form**.

## Structure (five parts; sections/ \input by main)
**I — Optimization as a Worldview:** s01 Introduction: An Operation Mistaken for a Law · s02 The Formal Anatomy of an Optimization Problem · s03 The Genealogy of Optimizationism. **II — Four Impossibilities:** s04 The Non-Structurability of Value · s05 The Relationality of Value and the Absent Quantifier · s06 Incommensurability · s07 The Constitution of the Subject. **III — The Cost of Optimizationism:** s08 The Damage to Generativity · s09 Optimizationism as a Symptom of Modernity · s10 Optimizing Practice Is Not Ethical Practice. **IV — A Non-Optimizing Relational Rationality:** s11 Rationality Is Not Optimization: Reclaiming the Word · s12 The Form of Relational Rationality · s13 Non-Action as the Highest Rationality. **V — Close:** s14 The Polyphonic Conclusion · s15 Envoi: A Promise That Is Not Optimized · s16 Acknowledgements.

## Key concepts & coined terms
- **Optimizationism** — the projection of optimization (a local, historical operation) onto the cosmos as its law; the paper's target.
- **The four impossibilities** — non-structurability (the drive), relationality (no external quantifier), incommensurability (pricing as betrayal), subject-constitution (the optimizer is an output, not an input); each independently voids the maximization operation.
- **The optimal and the good are orthogonal** — an optimizing practice, even successful, may fail as an ethics; optimizing practice is not ethical practice.
- **Extractive computation** — optimizing where no optimization problem exists converts circulating value into settled, drawable-off value (drawing on generative justice).
- **Non-optimizing relational rationality** — a rationality that *responds* rather than maximizes: response, attunement, the sustaining of generation.
- **Wuwei (非-action) as the highest rationality** — non-action / non-forcing as the paper's positive form of reason.
- **Polyphonic refusal** — declining to name a new master objective (which would reinstate the frame) is itself the positive claim, enacted in the paper's form.
- Cross-links: sharpens the series' standing critique of **"efficiency as terminal value"** (NGO/CLAUDE.md §15); extends **generative justice** / extractive computation (Papers II, IV), the **drive** and the Real (Papers VIII, XXIV), incommensurable/relational value (Papers IV, XV, XVI), and **wuwei** (Paper XX, the ethics of water).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; **27** entries — a fresh, paper-specific bib). Clean: no duplicate keys, no `@`-in-comments, no `@book` author+editor conflicts (`anderson1993value` is author-only).
- **No figure, no TikZ.** `graphicx`/`caption` loaded (kept from source) but unused. Uses `\part*` for the five parts (added to ToC manually). Math macros **`\argmax`/`\argmin`** (no `\holo` this paper).
- Multi-file: body in `sections/` (16 files incl. `s16_acknowledgements`) + `abstract.tex`, `\input` by the main tex.
- **Converted to the shared style** from the bespoke preamble (Pagella + own palette) to `\usepackage{serendip-paper}` + the unified cover (pink scshape series line, `warnred` title — manual `\\` removed — italic subtitle, `\coverrule`×2, `\coverfootnote`; the source's foot repeated the series line). Carries an explicit **AI-usage statement** on the abstract page. Epigraph 有价值不生于度量 … 能权万物之权，未尝有也 (the author). **Anonymous** dedication ("For her / 致她", "whom I have never once weighed for whether she was worth it"). Macros: `\argmax`/`\argmin`, `\zh`/`\cjk`, `\emc`/`\emb`, `claim`/`casebox`, `\goldrule`, the `Y` column.

## Files
- `paper_25_optimization_and_rationality.tex` — main (cover, epigraph, dedication, abstract + AI statement, ToC, `\part*` × 5, `\input` of sections, bibliography)
- `sections/` — 16 body files + `abstract.tex` · `refs.bib` (27) · `latexmkrc`
