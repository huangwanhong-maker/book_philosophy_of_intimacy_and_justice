# Paper II — AI-Mediated Intimacy

**Full title:** The Justice and Ethics of AI-Mediated Intimacy
**Subtitle:** Alienation, Power, Exploitation, and the Limits of Instrumental Imputation
**Status:** working draft, June 2026 · **Bibliography:** biblatex/biber (authoryear, maxcitenames=2), csquotes
**Build:** `make paper_02_ai_mediated_intimacy` (from book_src/; WSL TeX Live — see ../../CLAUDE.md). Engine is XeLaTeX (CJK in footnotes/acknowledgments); chain is xelatex → biber → xelatex × 2.

## What it argues
The paper takes up an open question from Paper I (huang2025toward): even if an AI "tender tip" genuinely improves a relationship and deceives no one at delivery, is anything still wrong? It proceeds dialectically. Hegel supplies the thesis that mediation as such is innocent (love exists only through externalization); Marx supplies the antithesis that alienation is a defect of *process*, not product, realizing an ironic fourth-alienation (person estranged from person under the description of bringing them closer); the universalist grammar of law and Buddhist dependent origination supply the strongest pro-mediation thesis (instruments do not break causation; no act was ever unmediated). The synthesis is doctrinal: imputation through instruments holds by default, but a criterion-governed exception domain — modeled on *strictly personal acts* (höchstpersönliche Handlungen) — exists in which the imputation fiction never engages, because such acts admit no substitutable links. Intimate acts are then read as layered phenomena with an *allocative face* (scarce, budgetable attention) and a *constitutive face* (who attends); AI's specific danger is *distributive reduction*, optimizing the allocative face while silently substituting the constitutive one. An eliminative test removes capital entirely and shows the wrong survives every ownership configuration; generative-justice remedies return value to its generators; and the whole resolves into two wrongs with two remedies: misattribution (cured by transparency) and process alienation (not cured by consent, but bounded).

## Structure
- §1 Introduction — Cyrano's question; the tender tip; method, scope stipulations, twelve claimed contributions
- §2 Hegelian frame — Entäußerung vs Entfremdung; externalization-with-return as the live axis
- §3 Marxian antithesis — structural transplant (Jaeggi); fourfold alienation transposed; fragment on machines, fetishism, subsumption; consent does not waive structure
- §4 Universalist thesis — instrumentality doctrine, mediated sincerity, no-harm, the reductio (search engine / friend / Chapman's book); jurisdiction of imputation and its limit
- §5 Buddhist examination — dependent origination; non-self vs the metaphysics of alienation; the non-delegable core (sati, the raft); convergence as a finding
- §6 Synthesis — höchstpersönliche Handlungen anchor; the four criteria; two-layer architecture (grounds vs operationalization); dynamic criterion; two wrongs/two remedies; the self-built touchstone
- §7 Political economy of the cognitive budget — budget vs expenditure; layered phenomena; distributive reduction; reallocation/substitution/managerial migration; deflation of the gesture's value-form
- §8 Exploitation — eliminative test across commercial / single-builder / joint-builder; ownership-insensitive wrong; generative-justice program (four layers)
- §9 Power — architectural constitutionalization of intimacy; code as the home's law; weakness of subsequent consent; constitution as a verb
- §10 Feminist hearing — wages-for-housework debt; gendered mental load; redistribution vs counterfeit substitution; ethics of care as positive theory of the constitutive face
- §11 Implications — answer returned to Paper I; boundary of consent; dialectical reservation
- §12 Limitations (six) · §13 Conclusion · Acknowledgments & AI-disclosure

## Key concepts & coined terms
- **distributive reduction** — treating a layered act as exhausted by its allocative face; optimizing it so the constitutive face is silently substituted
- **höchstpersönliche Handlungen exception** — strictly-personal-acts category (BGB §1311/§2064, PRC art. 1049, JP *mibun kōi*) extended to intimate cognitive-caring acts; imputation fiction never engages
- **allocative vs constitutive face** — every intimate act laminates a transferable/budgetable face onto one where only *who* expends the attention matters
- **the four criteria** — object of mediation; provenance of data; direction of initiative (pulled means vs pushed noticing); attribution expectations
- **dynamic criterion** — externalization-with-return vs without (training wheels/raft vs prosthesis/fetter); derived 4× (Hegel, Buddhist raft, Braverman, generative recursion)
- **Taylorism of love** — managerial migration: the engine becomes the planning office of attention, separating conception from execution (Braverman)
- **deflation of the gesture's value-form** — zero-marginal-cost mediation collapses the socially-necessary attention time, deflating gestures as costly signals (Spence/Mauss/Marx)
- **fetishism of the gesture** — a labor chain occluded behind the lover's apparent intrinsic "thoughtfulness"; supply chain of thoughtfulness
- **ironic form of alienation** — estrangement of person from person enacted *in the name of* closeness
- **contextual integrity of attribution** — mirror of Nissenbaum: norms govern flow of authorship credit, not information
- **architectural constitutionalization of intimacy** — a self-built mediating layer is a unilaterally drafted constitution; third-dimensional power (Lukes) in the form of the good; subsequent consent is habitation, not authorship (Hume)
- **ownership-insensitive wrong** — the residue surviving the eliminative test; **uncredited co-generator** — the recipient, whose sediment generates the gesture's value

## Local notes / quirks
- biblatex/biber + csquotes; cites huang2025relational (Responding to the Crises, OSF) and huang2025toward (= Paper I, companion)
- manual cover/title page (converted from `\maketitle`): `\thispagestyle{empty}` + vfill-centered block + `\clearpage`, using `\coverrule`/`\coverfootnote` from `serendip-paper.sty`
- abstract is one very long paragraph; a <3000-char short version lives in ../../../socarxiv_submissions.txt
- house style: NO em-dashes in English prose; all unverified legal citations carry `>> VERIFY <<` flags (docket/pin cites in §6 footnotes still open)
- loads `serendip-paper` class package; custom `\term{}` macro (pink italic) for first-use term introductions; `\cjkfont` used for Chinese in two footnotes and the acknowledgments
- color scheme per author (2026-06-04): pale-pink page, deep-pink headings, gold subsubsections
- the paper is reflexively self-indicting: its own touchstone system was single-built, and AI assisted its drafting (disclosed in Acknowledgments under criterion four)

## Files
- `paper_02_ai_mediated_intimacy.tex` — main · `refs.bib` · `latexmkrc`
