# Paper VI — Toward a Just Proposal

**Full title:** Toward a Just Proposal: Epistemic Injustice Theory and the Practice of Intimate-Relationship Proposals
**Subtitle:** On the Marriage Proposal as a High-Stakes Decision, and the Conditions under Which Its Staging Wrongs the One It Asks
**Status:** working draft, 2026 (theory-core installment) · **Bibliography:** biblatex/biber (authoryear)
**Build:** `make paper_06_just_proposal` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
A marriage proposal is, beneath its romance, a request to make a high-stakes, contract-like, transformative (Paul) decision. The conventional staging — the engineered emotional peak, the immediate-answer script, the asymmetry of information and preparation between the parties — can compromise the asked party's epistemic agency *even absent any ill will or identity-based prejudice*. The paper explicitly *declines to coin a new kind of epistemic injustice*: the wrong is better named by a framework already in hand. It reads the proposal through Catala (2025)'s pluralist account of epistemic agency, locating the difficulty in the *self-to-self* (self-interpretive) axis and in the *hermeneutical* (not testimonial) register, as a situational impediment to *epistemic empowerment* at a transformative threshold. As a theory-core installment it verifies the post-Fricker literature and maps the case onto Catala's categories, deferring the constructive "epistemically just proposal" to the full body.

## Structure
- §1 Orientation — what the installment is/is not; the deliberate refusal to mint a term; the reflexive constraint (claims discharged only by being *enacted with* the other).
- §2 The field, verified — Fricker's two forms (and why neither fits); Dotson (testimonial smothering, contributory); Pohlhaus Jr. (willful hermeneutical ignorance); Medina (resistance, kept for the constructive half); the gaslighting literature as indispensable contrast; then Catala's framework expounded in detail (§2.6 / `sec:catala`).
- §3 The jurisprudence of the proposal — the proposal as a quasi-contractual consent-act read across competing theories of justice: four conditions of valid consent (the shared floor); Rawlsian/procedural; autonomy-based/Kantian; republican non-domination; Marxian/social-reproduction; Pateman's contract critique (met, answered only partially); relational autonomy & care; the Confucian 礼义 register; convergence/divergence.
- §3.x (continues) The mapping — proposal as transformative threshold; the self-to-self axis; why hermeneutical not testimonial; how the three situational conditions impede self-interpretation; where the analysis stops (two honest limits); what the body will build.

Note: the prompt's expected `sec:mapping` mapping arc lives as subsections trailing §3 (jurisprudence) in the current source, not as a separate top-level §4. This is the verification + framework installment; the diagnostic and constructive body is not yet written.

## Key concepts & coined terms
- **epistemically just proposal** — the deferred constructive ideal: a proposal structured to *empower* the proposee's self-interpretation at the threshold.
- **self-to-self vs self-to-others intelligibility** — Catala's two axes; the wrong sits on the self-to-self (self-interpretive) axis, not credibility.
- **hermeneutical (vs testimonial) difficulty** — the register of the case: conditions of sense-making, not deflated credibility of testimony.
- **epistemic empowerment** (vs hermeneutical domination) — Catala's enabling/enlarging of self-interpretation across a transformative threshold; the constructive vocabulary.
- **the three situational conditions** — affective saturation; temporal compression / immediate-answer script; informational asymmetry.
- **the ring re-grounded** — from "seal of a concluded bargain" to "token and waiting" (信物者，待也，非约之封也).
- **deferred-commitment mechanism** — a remedy decoupling the affective moment from the binding answer.
- **four conditions of valid consent** — capacity, disclosure, understanding, voluntariness; standard *scales with the stakes*.

## Local notes / quirks
- biblatex/biber (authoryear, sorting=nyt, maxcitenames=2); `\addbibresource{refs.bib}`.
- Cover carries an extra italic line: "Theory-core installment: literature verification and the framework it applies".
- Uses `serendip-paper.sty`; custom `keydef` environment; CJK via `\cjkfont`; cover colors (warnred, rosedeep, ink).
- Leans on Catala (2025), Dotson, Pohlhaus Jr., Medina, the gaslighting literature (Abramson, Spear, Stark, Podosky, Ruíz), Paul (transformative), Pateman, and the consent/bioethics literature — all verified to 2025.
- Carries forward republican and Marxian lines from Paper III; relational re-grounding from Papers III & V.
- Acknowledgements disclose AI assistance for literature verification, structuring, and prose.

## Files
- `paper_06_just_proposal.tex` — main · `refs.bib` · `latexmkrc`
