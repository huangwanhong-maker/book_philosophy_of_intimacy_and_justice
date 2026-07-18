# CITATION_AUDIT

> Findings from merging the 27 per-paper `refs.bib` files into one master
> bibliography. Some of these are substantive scholarly errors: a citation key
> that resolves to the *wrong work* in some papers.
>
> Baseline: 3,672 entries → **764 unique keys**. Of the 327 keys used by more
> than one paper: 243 byte-identical, 34 differ only by which fields are
> present (safe union-merge), and **28 carry contradictory facts**.

## A. Key collisions — one key, two different works

The most serious class. The same `\cite{key}` resolves to a *different book or
article* depending on which paper you are reading. Each must be split into two
distinct keys, and the citing papers corrected.

| Key | Work A | Work B | Papers affected |
|-----|--------|--------|-----------------|
| `eglash2016generative` | *Of Marx and Makers: An Historical Perspective on Generative Justice*, Teknokultura 13(1), 245–269 | *An Introduction to Generative Justice*, Teknokultura 13(2), 369–404 | A: I · B: VIII, XXVII |
| `lacan1998` | *The Four Fundamental Concepts of Psychoanalysis* (**Seminar XI**) | *Encore* (**Seminar XX**), 1972–73 | A: V · B: IX, X, XI, XIII |
| `nussbaum2001` | *The Fragility of Goodness: Luck and Ethics in Greek Tragedy and Philosophy* | *Women and Human Development: The Capabilities Approach* | A: XI, XIII · B: XVIII, XIX, XX, XXI, XXIII |
| `geertz1973` | *Thick Description* (a **chapter**) | *The Interpretation of Cultures* (the **book**) | A: XI, XIII · B: XXIV |
| `simmel1950` | *Quantitative Aspects of the Group* (chapter) | *The Sociology of Georg Simmel* (book) | A: V · B: XXIV |

**Consequence:** in at least these cases a paper's reference list currently
prints a work its argument does not actually cite. This is not cosmetic.

## B. Self-citation drift — the author's own papers, miscited

Ground truth is the paper's own cover page, in this repository. Several papers
cite their siblings under titles those siblings do not have.

| Paper | Correct title (from its own cover) | Miscited as | In |
|-------|-----------------------------------|-------------|-----|
| **IX** | The Sustainability of Intimacy — *Poetic Generativity and Generative Justice* | "The Sustainability of Generative Relation: Geometric Phase, the Good Cycle…" | XXV |
| **XIII** | The Causality of the Non-Binding Vow — *On Trust, Promise, and the Generation of Expectation in the Absence of the Other's Sword* | "…Trust, Relational Divinity and the…" | XXV |
| **XV** | The Political Economy of Intimate Relations — *Toward a Theory of Generative Relational Wealth* | "Generative Relational Wealth: Redistribution, the Common and the Many-Body…" | XX, XXI, XXIII |

Also inconsistent: `paperix` year (2025 in ten papers, 2026 in XXIV) and
`wan2024grb` year (2024 in ten papers, 2025 in XXV).

**Resolution:** authoritative — taken from each paper's own title block. No
external verification needed.

## C. Edition conflicts — same work, different edition asserted

Both variants may name real editions; the series must simply pick one and use it
consistently. Under verification against sources.

| Key | Variant A | Variant B |
|-----|-----------|-----------|
| `sartre1943` | Philosophical Library, 1956 (IV–XXIII) | Washington Square Press, 1992 (VII) |
| `lacan1977xi` | W. W. Norton, 1978 (XXIV, XXVI, XXVII) | Hogarth Press, 1977 (XXV) |
| `lacan1992vii` | W. W. Norton (XXIV) | Routledge (XXV, XXVI, XXVII) |
| `hobbes1651` | Andrew Crooke, 1651 — the original (XIII) | Cambridge UP, 1996 — Tuck ed. (XX, XXI, XXIII) |
| `heidegger1962being` | Blackwell (I) | Harper & Row (VIII) |
| `folbre2001`, `murdoch1970` | trivial publisher-name variants | |

## D. Factual conflict — needs the source

| Key | Conflict |
|-----|----------|
| `eglash2016` | *An Introduction to Generative Justice*, Teknokultura 13(2). Pages **369–404** (in IV, V, XXIV, XXV, XXVI, XXVII) vs **369–388** (in IX, X, XI, XIII–XXIII). One is wrong. |

This is the series' single most-cited external source (19 occurrences), and it is
the framework the later half of the series is built on. Getting it right matters.

## E. Name / encoding damage

| Key | Problem |
|-----|---------|
| `zizek1989sublime` | author mangled to `v ziv zek slavoj` / `vzivzek slavoj` — broken Ž encoding |
| `tu1985` | Tu Weiming vs Tu Wei-ming; SUNY Press vs State University of New York Press |
| `berry1984` | Berry, Michael V. vs Berry, M. V. |
| `saussure1916course` | de Saussure, Ferdinand vs Saussure, Ferdinand de |
| `trevarthen1979` | typed as `@book`, `@article`, *and* `@incollection` across papers |
| `confucius_analects` | `@book` vs `@incollection` |

## Resolution

All of the above land in a single **`book_src/bib/master.bib`**; the per-paper
`refs.bib` files are retired. Class A additionally requires rewriting `\cite`
keys in the affected papers, since the fix is not "pick a variant" but "you cited
the wrong book."
