# Paper V — The Formation of the Subject

**Full title:** The Formation of the Subject in Intimate Relationships
**Subtitle:** The Other, Joint Attention, and the Economy of Attention
**Status:** working draft, 2026 · **Bibliography:** natbib/bibtex (plainnat, [round])
**Build:** `make paper_05_subject_formation` (from book_src/; WSL TeX Live — see ../../CLAUDE.md).

## What it argues
The subject of intimate life is not a pre-given entity that enters relation but is formed and continuously sustained through a single mechanism: the presence of the other and the practice of joint attention (the recursive, mutually open triangle of self, other, shared object). Part One assembles the theoretical ground, organizing accounts of the relational subject by *type of constitutive mechanism* — mirror (Cooley, Mead, Winnicott, Lacan), triadic (developmental joint attention; Davidson's triangulation), and symbolic (Vygotsky, Saussure, Althusser, Butler) — with the enactivist correction demoting theory-of-mind to a derivative competence. Part Two argues the triadic mechanism is the *missing middle term* between mirror and symbol, offers a layered reconciliation of Lacan and Tomasello, and answers a Levinasian difficulty: the dyad's first third party is the shared object (the world). Part Three transfers the mechanism to adult intimacy under a no-overclaim discipline, proposing the *reflexive triangle* (the relation itself as shared object) whose limit form is care: holding the triangle open for an other whom incapacity has silenced. Part Four develops the consequences — the attention economy as a *parasite* on the triadic structure (the feed as *pseudo-shared object*), the symbolic order as standing distributor of attention (*virtual fourth vertex*), *attentional alienation* and *attentional autonomy*, a Hohfeldian *no-claim-right* to attention replaced by imperfect duty + Murdochian virtue + a structural criterion of attentional justice, and finally the new category **constitutive injustice**.

## Structure
- §1 Introduction — the question of the intimate subject; Mechanism Thesis; method and no-overclaim discipline.
- §2 Survey — three types of constitutive mechanism (mirror / triadic / symbolic); theory-of-mind and the enactivist correction; Gergen distinguished.
- §3 The Thesis — triadic as missing middle (Hinge Thesis); formal Def. of joint attention; layered Lacan–Tomasello reconciliation; the first third (Levinas answered).
- §4 Transfer to adult intimacy — what does not transfer (Simmel); Transfer Thesis; reflexive triangle; presence with acknowledged gap; care and the held-open triangle.
- §5 Political economy of attention — scarcity/capture; parasite thesis and pseudo-shared objects; attention as ur-gift; three arenas of competition (rigged contest); regenerative circuit / sustainability criterion.
- §6 Symbolic order as distributor — virtual fourth vertex; attentional alienation; attentional autonomy (re-authoring the script).
- §7 Rights structure — against a claim-right (Hohfeld); imperfect duty + structural criterion; gendered distribution of triangle-maintenance labor (distributional clause).
- §8 Constitutive injustice — two bridges (transcendental, fiduciary); category defined; scope and addressees.
- §9 Objections and replies; §10 Conclusion; Acknowledgements; bibliography.

## Key concepts & coined terms
- **Joint attention** — formalized (Def.): mutual attending to a shared object *and* to the other's attending, mutually open; relational, non-delegable, fragile.
- **Reflexive triangle** — mature intimate joint attention takes the relation itself ("we") as its shared object; spiral, not vicious regress.
- **Pseudo-shared object** — an object soliciting the phenomenology of shared attention while failing the joint-attention conditions (mutuality failure, or personalized variants with no common *x*); the algorithmic feed.
- **Virtual fourth vertex** — the symbolic order as standing pre-distributor of salience inside every adult triangle.
- **Attentional alienation** — attending executed under a salience script one cannot appropriate (Jaeggi).
- **Attentional autonomy** — a couple's joint re-authorship of its local law of salience; self-legislation continued by attentional means.
- **Constitutive injustice** — systematic degradation of a person's access to/participation in the mechanisms of subject formation, upstream of distributive, recognition, and epistemic injustice.
- Other load-bearing terms: Mechanism / Hinge / Transfer / Parasite / No-Claim / Fourth Vertex Theses; presence with acknowledged gap; attention as ur-gift; net-regenerative circuit; held-open triangle.

## Local notes / quirks
- **natbib/bibtex (plainnat).** classic-BibTeX rules apply (no `@` in refs.bib comments; no author+editor in @book). Custom theorem-like envs: `defn`, `prop`, `crit`, `objection`, `reply`.
- Cover: `titlepage` env with twin epigraphs (Simone Weil; 《诗经·唐风·绸缪》); **abstract is on its own page (p.2)** so the contact footnote (`\coverfootnote`) pins on p.1 — keep that structure. Uses `\zh{}` for CJK (closing epigraph and acknowledgements).
- Loads `serendip-paper.sty`; `natbib` must precede it (hyperref loads inside). Series cross-references Papers III and IV throughout; companion AI-mediated-intimacy paper flagged as future work.

## Files
- `paper_05_subject_formation.tex` — main · `refs.bib` · `latexmkrc`
