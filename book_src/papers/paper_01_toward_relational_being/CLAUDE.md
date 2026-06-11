# Paper I — Toward Relational Being in Intimate Life

**Full title:** Toward Relational Being in Intimate Life: Integrative Justice and an Ethics of Dialectical-Positivist Practice
**Subtitle:** A Family-and-Relationship Management Application as a Case Study
**Status:** working draft, 2026 · **Bibliography:** biblatex/biber (authoryear)
**Build:** `make paper_01_toward_relational_being` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
Positivist, evidence-based software increasingly mediates intimate partnership, and its default logic — measurement and optimization — is often corrosive to the very thing it would serve. The paper asks, as a question in normative philosophy rather than empirical or design research, how such technology ought to be governed if its aim is *relational flourishing*: the sustaining of a relationship understood (after relational ontology) as ontologically prior to the individuals it relates. It makes four kinds of claim: (1) *normative* — an **integrative-justice** framework that assigns ~14 ethical/epistemic traditions each the questions it is competent to answer, resolving conflicts by a defended *lexical ordering of jurisdictions*, not by averaging; (2) *practical* — an **ethics of dialectical-positivist practice** that warrants measurement differentially, site by site, by whether a phenomenon is partly constituted by *not* being measured; (3) *engineering* — a real ~two-dozen-module application built by the author instantiates the framework in software; (4) *diagnostic* — it names wrongs specific to intimate computing, chiefly *proxy epistemic injustice* and the opposition of structural efficiency vs. relational development. Limits are explicit: mediation's deepest harms can be reduced but never eliminated, the adjudication is judgement with no algorithm, and the evidence is a single author-designed case (existence proof, not data).

## Structure
- **§1 Introduction** (`sec:intro`) — the normative gap; three guiding questions (foundations, integration, the absent other); lists seven contributions.
- **§2 Relational Being in Intimate Partnership** (`sec:relational-being`) — lineage; the ontological ground (relationality, generative presence, AI as *pseudo-presence*); restricts the relational thesis to intimate partnership via three features (non-role-defined, voluntary vulnerability, the constitutive unsaid) and their vulnerability to mediation.
- **§3 An Integrative-Justice Framework** (`sec:frameworks`) — one subsection per tradition, each given a *competence* and a *limit*: dialectics, evidentialism, epistemic injustice, positivism/anti-positivism, structuralist psychoanalysis, deontology, care ethics, Confucian-Daoist restraint, capability approach, developmental psychology, eudaimonia, generative justice, data ethics, recognition (Levinas/Honneth).
- **§4 The Argument for Integration** (`sec:integration-argument`) — integration as a *division of jurisdictional labour* (Table `tab:jurisdictions`), conflicts resolved *lexically*; defends why this is not eclecticism.
- **§5 An Ethics of Dialectical-Positivist Practice** (`sec:dialectic`) — the per-site measurement test; never finally settled.
- **§6 Case Study** (`sec:casestudy`) — modules as worked verdicts: persistent design rationale, joint ledger, household management, love journal, health/growth, AI-as-witness, shared calendar, co-presence/co-creation, "seeing the world together", "grace for two", "our journey" (deliberate absence of AI), "happiness savings jar".
- **§7 The Absent Other** (`sec:absent-other`) — the app is built for a partner unaware it exists; treated as a limiting case that tests and generalizes the framework.
- **§8 Limitations** (`sec:limitations`) — internal tensions (dialectical adjudication, efficiency vs. development, AI alienation, mediated process/open dialectic, secrecy, deliberate memory) then methodological limits.
- **§9 Related Work** (`sec:related`) · **§10 Conclusion** (`sec:conclusion`) · Acknowledgements · Appendix A: Note on the System's Construction (`sec:appendix-technical`).

## Key concepts & coined terms
- **Integrative justice** — coordinated exercise of several normative competences, none sovereign, ordered by a defended *division of jurisdictional labour*.
- **Ethics of dialectical-positivist practice** — measurement adjudicated phenomenon-by-phenomenon; legitimate when measuring leaves the phenomenon the same, refused when the phenomenon is partly constituted by being unmeasured.
- **Relational being / generative presence / pseudo-presence** — from the author's prior work; presence enacts vs. representation abstracts; an AI layer manifests within the symbolic only.
- **Proxy epistemic injustice** (`sec:calendar`) — the paper's own coinage: *misattribution of an act of knowing*; a system performs the cognitive/attentive labour the relation's meaning requires of a person, so another misreads its source. A third variant beyond Fricker's testimonial/hermeneutical pair.
- **Structural efficiency vs. relational development** — the standing, possibly irreducible opposition (`sec:limitations`).
- **Generative field** — the positive design aim (furnish a space, then withdraw, *wu wei*), grounded in eudaimonia and judged by the capability criterion.
- **Witness vs. advisor** — the load-bearing AI design distinction (`sec:witness`); the system accepts the witness's risk (irrelevance) over the advisor's (paternalism).

## Local notes / quirks
- biblatex/biber; cites `huang2025relational` (Responding to the Crises of Symbol and Subject in Modernity, OSF) as the prior relational-ontology source.
- `\documentclass[11pt,a4paper]{article}` + `\usepackage{serendip-paper}`; **XeLaTeX** required (CJK throughout — dedication, journal sample, acknowledgements use `\cjkfont`).
- Cover/dedication are hand-built after `\begin{document}` (not a generic cover macro): series line "Philosophy of Intimacy and the Theory of Justice · Paper I", `\coverrule`, `\coverfootnote`, color names `rosedeep`/`warnred`/`ink`/`lightgold`/`gold` from the style.
- `\TODO{}` macro is defined (gold text) — grep for stray TODOs before shipping.
- Two display tables via `longtable`/`table` (`tab:jurisdictions`, `tab:household`); a pseudocode `quote` block for iterative-deepening exploration.
- Author email in cover: `huangwanhong@serendip.ngo`.

## Files
- `paper_01_toward_relational_being.tex` — main · `refs.bib` — bibliography · `latexmkrc`
