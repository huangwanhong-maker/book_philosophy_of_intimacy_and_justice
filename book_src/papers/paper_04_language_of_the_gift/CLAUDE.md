# Paper IV — The Language of the Gift

**Full title:** The Language of the Gift in Intimate Relationships: Economics, Alienation, and Generative Justice
**Subtitle:** On the Gift as Love's Language, the Ledger It Is Read Into, and the Conditions under Which the Reading Becomes Alienation
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (plainnat)
**Build:** `make paper_04_language_of_the_gift` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
The gift is love's native language: an expressive act whose meaning is constituted by the relation it enacts, not by the object transferred. Economics has a developed literature on gift-giving (altruism, gift exchange, signaling, deadweight loss, crowding out, relational earmarking), but every theory renders the gift tractable by the same move — *interpreting* it into a transfer language whose semantics is a ledger. A semiotic/psychoanalytic layer says what is lost: following Saussure and Baudrillard the gift's value is positional *sign-value* fixed by its place in the relation's differential history, and following Lacan what it signifies is *desire* rather than need, so its functional excess (Waldfogel's "deadweight loss") is the signifying mechanism, not waste. Using elementary formal-language theory, the paper models intimate giving as a context-sensitive expressive language and the economic reading as a non-injective, context-forgetting interpretation map into a finite-state ledger language. *Alienation* is then characterized precisely as the contraction of generative practice onto the preimage of the ledger under "legibility pressure" — partners come to produce only what the interpretation can see. Two further harms follow: epistemic injustice (the map's kernel makes some contributions illegible/unnameable) and distributive misdescription (balance is the wrong functional for value that circulates generatively). After Eglash's generative justice, it proposes *recirculation depth* rather than bilateral balance as the justice functional, with implications for relational-data design.

## Structure
1. Introduction — thesis, placement in the series, four-step roadmap.
2. Economic theories of the gift — altruism (Becker), gift exchange (Akerlof/Fehr), signaling (Camerer/Prendergast), deadweight loss (Waldfogel), crowding out (Titmuss/Gneezy/Bénabou), relational earmarking (Zelizer); §2.7 "the shared move."
3. Semiotics of the gift — sign-value (Saussure/Baudrillard); the signified is desire (Lacan, Mauss's *hau*); what a ledger can record (referent without signifier).
4. Formal-linguistic account of alienation — definitions/propositions: expressive language, ledger language, interpretation map and its kernel, alienation as contraction onto the preimage, plus a scope remark.
5. Epistemic injustice — testimonial injustice as erasure, hermeneutical injustice as kernel-blindness.
6. From balance to recirculation: generative justice — Eglash; relation as generative unit; recirculation-depth definition + remark.
7. Implications — relational data and evidence-informed decisions (instrumentation imports a grammar; designing for the generative grammar).
8. Conclusion; Acknowledgements.

## Key concepts & coined terms
- **Ledger language** — finite-state, per-symbol-compositional, total balance semantics ($\beta$); always returns a number, never "meaningless."
- **Expressive language** — history-dependent, context-sensitive meaning function $\mu$ that does *not* factor through a per-symbol valuation.
- **Interpretation map** $h:\SE^{*}\to\SX^{*}$ — context-forgetting monoid homomorphism; its **kernel** ($\ker h$) is where the harm lives; $\varepsilon$-mapped acts are erased.
- **Alienation-as-preimage-contraction** — practice $L(G)$ converging onto $h^{-1}(\LX)$ under *legibility pressure*; grammar replacement, not commodification.
- **Sign-value / symbolic exchange** (Baudrillard); **desire** as the signified (Lacan); constitutive excess; metonymic presence of the giver (*hau*).
- **Generative justice / recirculation depth** $R(F)$ — share of generated value on cycles returning to the generating subgraph, recognition treated as a first-class flow.
- **Notation:** macros `\LE \LX` (expressive/ledger languages), `\SE \SX` (their alphabets), defined in the preamble.

## Local notes / quirks
- **natbib/bibtex (plainnat).** References were INLINE in a `thebibliography` block; now external `refs.bib` + `\bibliography{refs}`. Classic-BibTeX rules apply: no literal `@` in refs.bib comments; no author+editor in a single `@book`.
- Uses a `titlepage` environment for the cover and `amsthm` (`definition`/`proposition`/`remark` theorem environments).
- Cites the author's own `huang2026vow` (= Paper III) — the vow paper; the series diagnosis is drawn as parallel.
- XeLaTeX required (CJK epigraphs via `\zh`/`\cjkfont`, fontspec); loads `serendip-paper` style; `natbib` before `serendip-paper` (hyperref loads inside it).

## Files
- `paper_04_language_of_the_gift.tex` — main · `refs.bib` · `latexmkrc`
