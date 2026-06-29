# Paper XVII — Generativity Under Power

**Full title:** Generativity Under Power: Trust, Asymmetry, and Estrangement in Intimate Relations
**Subtitle:** On the Conditions of Relational Flourishing in a Field of Power
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (numbered, plainnat; 54 entries)
**Build:** `make paper_17_generativity_under_power` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
**How does love fare under power?** The series has theorised intimacy as a generative-relational process (GRB) — a coupling out of which value is *generated, not extracted* — but, in effect, in a clearing. This paper confronts the fact that intimate relation unfolds in a **field of asymmetries** that can deform, capture, freeze, or shatter that generativity. It is built on three questions in an **ascending logic — creation, preservation, liberation**, each answered by a different body of theory but all bearing on one object, **love** (the dynamics of the *real* between two subjects, the part of the bond that circles the unsymbolisable and cannot be counted, traded, or managed):

- **How does love create a world?** — the GRB account (taken as established), plus an **etiology of breakdown into estrangement** (すれ違い, *surechigai*).
- **How is love not destroyed by power?** — a reconstruction of **International Relations** theory: strip the realist assumption that an anarchic field's currency is relative power, and recover IR's deeper object — how **opaque subjects build trust and order under uncertainty without a central authority**.
- **How does love become free within history?** — a **dialectical historical materialism** holding material conditions together with the relative autonomy of the symbolic/affective life they shape.

The intimate relation is a **two-level system**: the *end* is the dynamics of love (a process of the real, unmeasurable/unexchangeable); the *means* is the symbolic order of **power** (calculable, strategic). The means serve the end but intrinsically tend to damage it — hence the central claim: power and wealth can protect the **conditions** under which love occurs but cannot produce love, **a political economy of conditions, never of love.** **Trust** is the interface crossing both levels and the variable deciding whether an asymmetry becomes generative or frozen. Two further claims: **estrangement** is, in the first instance, a *necessary moment* of the bond's self-maintenance (perfect concordance = equilibrium = dead); and power can neither eliminate itself nor be eliminated — the only viable course is to generate a continual **counter-force that keeps power from solidifying**. Hence the summit: **a generative relation does not oppose power; it opposes the freezing of power** — the political appearance of the ontological law by which desire withholds itself from total symbolisation in order to stay alive.

## Structure (sections/ \input by main, in reading order)
s01 introduction → s02 symptomatology → s03 encoding (mismatch) → s04 prediction (unattributable prediction error) → s05 phase (arrest of phase) → s06 ir (IR reconstruction) → s07 conditions (political economy of conditions) → s08 practices (inventory + teleological filter) → s09 balance (generative balance — negative summit) → s10 asymmetry (generative asymmetry — positive summit) → s11 histmat (dialectical-materialist history) → s12 dissipation (dissipative structure) → s13 return (return and the spiral) → s14 rose (dormancy) → s15 praxis (praxis of the two axes) → s16 conclusions (+ envoi).

## Key concepts & coined terms
- **Political economy of conditions (never of love)** — power/wealth protect the *conditions* of love but cannot produce love; the central claim.
- **Two-level system (end / means)** — love (the real, uncountable) as end; power (the symbolic, strategic) as means that serves yet tends to damage it.
- **Trust as the interface** — the variable crossing both levels, deciding whether asymmetry is *generative* or *frozen* (extends Paper XIII).
- **Estrangement / すれ違い (surechigai)** — passing one another without meeting; a *necessary moment* of self-maintenance, not mere malfunction (equilibrium = death).
- **"Opposes the freezing of power"** — a generative relation doesn't oppose power as such but its *solidification*; generate a continual counter-force.
- **Generative balance / generative asymmetry** — the negative and positive "summits" (§9–§10).
- **IR reconstruction** — trust and order among opaque subjects under anarchy, against realist relative-power.
- Cross-links: **Paper XIII** (trust), **Paper IX** (holonomic criterion), **Papers XIV–XVI** (political economy), the **mother paper** (GRB), Paper II (alienation/power), Paper III (self-legislation).

## Local notes / quirks
- **natbib/bibtex, NUMBERED** (`[numbers,sort&compress]`, `plainnat`; 54 entries). classic-BibTeX rules apply (no `@` in refs.bib comments — clean).
- **No TikZ** (unlike XI/XIII). Multi-file: body in `sections/` (16 files + `abstract.tex`), `\input` by the main tex.
- **Converted to the shared style** from the bespoke preamble (Pagella + own palette) to `\usepackage{serendip-paper}` + the unified cover (pink scshape series line, `warnred` title, `\coverrule`×2, `\coverfootnote`). The zip shipped **no `latexmkrc`** (added on deploy) and a `Paper_XVII_draft.pdf` (discarded; rebuilt). `OUTLINE.md` (planning doc) and `README.md` kept in the folder. Paper-specific macros: `\holo`, `\zh`/`\cjk`, `\emc`/`\emb`, `claim`/`casebox`, `\goldrule`, the `Y` column.
- Uses Japanese すれ違い and a Laozi (Daodejing ch.40) epigraph.

## Files
- `paper_17_generativity_under_power.tex` — main (preamble, cover, epigraph, dedication, abstract, `\input` of sections, bibliography)
- `sections/` — 16 body files + `abstract.tex` · `refs.bib` (54) · `latexmkrc` · `README.md` + `OUTLINE.md` (upstream notes)
