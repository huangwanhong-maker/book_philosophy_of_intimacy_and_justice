# REVISION SUMMARY — The 27-Paper Series into Three Volumes

> Top-level summary of the whole revision. Detail lives in `BOOK_PLAN.md`
> (architecture + decisions), `REVISION_TRACKER.md` (per-paper objective status),
> `CITATION_AUDIT.md` / `CITATION_RESOLUTIONS.md` (bibliography), and the three
> `VOLUME_{I,II,III}_FINDINGS.md` (substantive, advisory).

## 1. What was delivered

**Three volumes that compile as books**, from the 27 standalone papers, without
disturbing the individually-published papers:

| Volume | Papers | Title | ~Pages |
|--------|--------|-------|--------|
| I | I–IX | Relational Being, the Subject, and the Word | 668 |
| II | X–XVIII | Generativity, Value, and Power | 1174 |
| III | XIX–XXVII | Happiness, Ethics, Aesthetics, and Culture | 1244 |

Build: `cd book_src && make books` (or a single volume from `book_src/volumes/`).
All three build with **0 undefined citations, 0 undefined references, 0 stray
`\todo`, 0 label collisions**.

## 2. The objective layer (applied directly)

Everything here is done and committed.

- **Bibliography unified.** All 27 papers converted to one backend (biblatex +
  biber); 3,672 bib entries merged into one deduplicated `bib/master.bib` (764).
  This was the hard prerequisite: biblatex and natbib cannot coexist in one
  document, and each volume spanned both.
- **28 contested citations resolved.** An independent verification pass checked
  every one against an authoritative source (URLs in `CITATION_RESOLUTIONS.md`).
  Real errors fixed: `eglash2016` had the wrong page range across a dozen papers;
  one key (`eglash2016generative`) pointed at two different Eglash articles;
  `nussbaum2001` named two different books (split); several self-citations were
  wrong (paper XV was cited under a wholly wrong title in three papers); paper V
  cited Lacan's *Encore* for a Seminar XI dictum.
- **Chapter-ization infrastructure.** `serendip-book.sty` (book counterpart of
  the paper style), `serendip-macros.sty` (every paper macro harvested verbatim),
  a `content.tex` split so each paper's body is shared by its standalone build and
  its chapter, and 1,642 labels namespaced so a `\ref` can't leak between papers.
- **All 11 stray `\todo`s cleared** (paper VII's 8; XX/XXI acks; XXIV's classical
  note converted to a plain editorial note preserving the author's reticence).
- **Collisions the single-document context exposed**, all fixed: a column-type
  clash, a duplicate label, and `\MakeUppercase` mangling colour names in headings.

## 3. The substantive layer (advisory — nothing applied to arguments)

Nine-per-volume close reads, in the three `VOLUME_*_FINDINGS.md`. These are
**observations for the author to judge**, each with a concrete suggestion. The
reads converged on a small number of series-wide patterns:

### A. The formal apparatus is the series' signature and its biggest liability
The geometric-phase/holonomy, quantum-grammar, Bayesian/free-energy, Kuramoto,
Helmholtz, coalgebra/Mori–Zwanzig devices are almost always introduced with the
grammar of a theorem, then either concede they are unmeasurable/heuristic or turn
out to re-encode a conclusion already reached in prose. **Several are not merely
decorative but technically wrong:**
- XIII — adiabatic Berry-phase transport *is* externally driven, inverting the
  paper's genuine/forged (endogenous/pumped) mapping.
- XIV — the Kuramoto K_c phase transition does not exist for two oscillators.
- XVII — "static equality = thermodynamic equilibrium" inverts entropy (perfect
  concordance is low-entropy/ordered, not maximum-entropy).
- XVIII — the headline "effacement = ½" is an artifact of the normalizing
  definition, not a result.
- XI — "justice = skewness" is degenerate on the dyad (a third moment of two
  points).
- XV — the formal apparatus is inert; its central figure is a *blank* TikZ box and
  its Lagrangian macro is unused.

The reassuring corollary the reviewers repeated: **the philosophical arguments
generally survive deletion of the math.** So the fix is framing, not surgery.

> **Recommended single decision, series-wide:** adopt one consistent stance —
> either mark the formalism as *regulative/heuristic notation* (cheapest; costs
> nothing argued; several papers already do this in their honesty-clauses) or
> commit to it as a *genuine model* (supply the missing structure and fix the
> physics in the promised "Value Foam"/`wan2026braid` paper, and cite that paper
> with a real key). Paper XXV (which argues optimization does not apply to
> intimacy) makes this decision *urgent*: it must reconcile with the series' own
> variational models (XI, XIII) or the book reads as internally at odds.

### B. "Confirmation by convergence" is treated as evidence but is non-falsifiable
Many papers present N frameworks/traditions converging on the thesis as strong
evidence (XIV's four cultures, XIII's "three lines," XI's five frameworks, XIX's
"the breadth is the proof," XXII's four inversions). A thesis as capacious as
relational ontology is confirmed by anything relational; and a structure the
author *imposed* (the "form enacts the content" move, in I, VIII, IX, XXII) cannot
confirm that the structure tracks reality. **Fix:** downgrade "evidence/
convergence/proof" to "coherence across registers"; let at least one interlocutor
*resist* and revise in response.

### C. Length is often not earned — redundancy engines
Especially Volume III (XXI ~123pp, XXII ~138pp, XXIV): a per-section template run
4×, series-standard criteria re-derived 4–5×, and a triple-statement habit
(prose → `\claim` box → casebox → recap). De-duplication is the highest-value
revision available — commonly 20–35 pp per paper with no argumentative loss.

### D. Deferred/imported cores presented as achievements
VI, VII, IX defer their formal/constructive payload to unwritten sequels while
writing them up in the indicative (VI reads as a preface to an absent paper); XX
and XXVII rest their normative core on uncited companion works; several papers use
the holonomy criterion as a verdict-maker with no local content. **Fix:** fold the
sequel in, reframe as an avowed prolegomenon (the VII solution), or give each
imported criterion one self-contained operational sentence.

### E. Individual load-bearing gaps (highest-value per paper)
A single most-important item per paper is marked in each findings file — e.g.
I's secret-app inconsistency, II's stipulated "yield consists in who attended,"
III's self→co-legislation equivocation, V's Lacan/Tomasello partition, XXIV's
"relational Real" vs Lacan's *pas de rapport*, the two closers' identical endings.

## 4. What remains for the author

1. **Decide the formalism stance** (§3.A) — the one decision that most changes the
   series' reception.
2. **Per-paper substantive items** — work through the three findings files; each
   item is advisory with a concrete suggestion.
3. **A few open objective items** needing author input, not mechanical fixes:
   paper VI's installment framing (write the body or reframe as prolegomenon);
   XV's blank figure + unused Lagrangian; XVII's placeholder footnotes and 19-vs-16
   etiology count; XX's `wan2026braid` key; XXIII's missing XXII cross-reference;
   scholarly acknowledgements in XX/XXI; year-finalization for the self-citations.
4. **Optional book apparatus** not yet built: a general introduction, per-volume
   introductions, a consolidated index. (The preface, per-volume title pages, TOCs,
   running heads, and per-chapter reference lists are in place.)

## 5. Working notes

- Branch: `books/three-volumes`. Each phase committed separately.
- Regenerate derived artifacts: `python3 tools/merge_bib.py` (master.bib),
  `python3 tools/split_content.py` (content.tex), `python3 tools/find_todos.py`
  (the `make todo-check` gate). `content.tex` is derived from each paper's
  standalone source — regenerate after editing a paper.
- The standalone papers still build individually (verified) and share `master.bib`.
