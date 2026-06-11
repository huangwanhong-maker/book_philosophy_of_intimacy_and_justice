# Paper III — Self-Legislation in Intimate Relationships

**Full title:** The Normativity of Self-Legislation in Intimate Relationships: Freedom, Morality, and Justice
**Subtitle:** On a Lover's Vow, the Rights-Order It Institutes, and the Conditions under Which It Becomes Domination
**Status:** working draft, 2026 · **Bibliography:** biblatex/biber (authoryear)
**Build:** `make paper_03_self_legislation` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
A lover legislates himself an unconditional law — *whatever happens, however she feels, I will keep loving her* — and the paper subjects this vow to a three-layered normative analysis. On **freedom**: the vow is exemplary Kantian autonomy, but Kant's apparatus (the fact of reason, the noumenal self) cannot say *when* a self-legislation is free; a compatibilist, reasons-responsive criterion can, and on it the vow's freedom is conditional on remaining responsive to the beloved as a source of reasons. On **morality**: the vow is admirable as constancy, but its *content* (what "loving her" means) is fixed unilaterally, in tension with the responsiveness the philosophy of love takes as constitutive. On **justice**: republican non-domination plus a Hohfeldian analysis of the rights-order a vow institutes show that a unilaterally legislated law over a two-person life cannot be just — justice is modal, resting on each party's retained standing to contest the terms. A structuralist/feminist section argues the legislating "self" is itself constituted by a historically gendered order, so a sincere vow can reproduce subordination; a social-reproduction section draws the line between a legitimate rights-order and **exploitation** (appropriation of unrecognized relational labour masked as love). Against the objection that recognition can itself be ideological, the operative criterion is **live contestability**, not de facto endorsement. The conclusion is a micro/macro **isomorphism**: a lover's vow and a political economy share a structure — the standing of any law over a shared life rests not on the legislator's purity but on the other's modally robust standing to answer.

## Structure
1. Introduction — the vow, its puzzle, the layered thesis, and the isomorphism; method and scope.
2. Kantian self-legislation — autonomy vs heteronomy; the fact of reason; the noumenal refuge; Korsgaard's half-step.
3. When is self-legislation free? — Frankfurt and Fischer/Ravizza; reasons-responsiveness applied to the vow; the shared "hole" (which reasons, whose standing).
4. The moral layer — vow as constancy; the first crack (form silent on content; responsive love vs imposition).
5. The justice layer — procedure cannot certify content; non-domination (Pettit's benevolent master); three vectors (immunization against voice, non-reciprocity, definitional capture).
6. The vow as a rights-order — Hohfeldian positions; the wrong is monopolized second-order constituent power; order vs imposition of order.
7. The constituted subject — Althusser/Lacan (subject as effect); Pateman/Okin/Young (gendered subordination); not collapsing into determinism.
8. Rights-order or exploitation? — formal structure of exploitation; social reproduction (Federici, Hochschild, Fraser); the line.
9. The objection from ideological recognition — Honneth, Khader/adaptive preferences; contestability not endorsement; Ricoeur's proper distance; the honest residue.
10. The vow re-grounded — relational co-legislation; from self- to co-legislation; generative justice.
11. Conclusion — the isomorphism of the vow and the order.

## Key concepts & coined terms
- **self-legislation** — the will binding itself to a self-authored maxim (Kantian autonomy).
- **reasons-responsiveness** — compatibilist freedom criterion (Fischer/Ravizza guidance control); historicist about mechanism ownership.
- **non-domination** — republican (Pettit); domination is *modal* — exposure to arbitrary interference at another's discretion, even if benign.
- **benevolent master** — the lover whose good treatment is granted by disposition, not secured by the other's standing.
- **Hohfeldian rights-order** — claim/duty, privilege/no-right, power/liability, immunity/disability; the wrong sits at the *second order* (constituent power).
- **three vectors** — immunization against voice, non-reciprocity, definitional capture.
- **constituted subject** — the legislating "self" as effect of a gendered order, not origin.
- **expropriation vs exploitation** — social-reproduction distinction; relational/care labour recoded as natural devotion.
- **the vow as exploitation** — appropriation of unrecognized relational labour under an ideology presenting it as love.
- **ideological recognition** — recognition (and sincere endorsement) that coexists with and cements domination.
- **live contestability** — the operative justice criterion: a modally robust, efficacious standing to contest, not de facto endorsement.
- **proper distance** (Ricoeur) — the separateness that keeps contestability live.
- **co-legislation / generative justice** — reconstructed vow; justice as keeping open each party's ongoing self-formation.

## Local notes / quirks
- biblatex/biber, authoryear (`style=authoryear, sorting=nyt, maxcitenames=2`). Run biber, not bibtex.
- **This paper is the reference design for `serendip-paper.sty`** — keep its cover/dedication/style as the canonical template; the shared `.sty` was extracted from it.
- `singer1991nature` → Singer, *The Nature of Love* Vol. 1 (Chicago, 1984), despite the cite key year.
- No `sections.tex` — the whole paper is in the one `.tex` file. Uses `\cjkfont` for Chinese (诗经 / 毛诗序 epigraphs, closing line); requires XeLaTeX.
- Custom commands from the `.sty`: `\coverrule`, `\coverfootnote`; colors `rosedeep`, `warnred`, `ink`, `lightgold`.

## Files
- `paper_03_self_legislation.tex` — main · `refs.bib` · `latexmkrc`
