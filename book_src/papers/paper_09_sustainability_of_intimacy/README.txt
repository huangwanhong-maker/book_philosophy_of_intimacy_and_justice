Paper IX — "The Sustainability of Intimacy"
LaTeX source package
============================================

FILES
  main.tex            Master file (preamble, title page, dedication, abstract,
                      keywords, \input of all sections, bibliography).
  refs.bib            Bibliography (26 entries, BibTeX).
  sections/           Section source files, \input by main.tex in reading order:
                        abstract.tex
                        s0_prelude.tex        (§1 Prelude: The Rose in the Garden)
                        s1_thesis.tex         (§2 Thesis)
                        s2_antithesis.tex     (§3 Antithesis)
                        s3_synthesis.tex      (§4 Synthesis: geometric phase)
                        s4_epistemology.tex   (§5 Epistemology)
                        s5_praxis.tex         (§6 Praxis: wu wei)
                        s6_semiotics.tex      (§7 Semiotics: the poem)
                        s7_turn.tex           (§8 Poeticity does not guarantee the good)
                        s8_core.tex           (§9 The non-possessive poem)
                        s8b_contract.tex      (§10 Legislation as a flow)
                        s9_eudaimonia.tex     (§11 Eudaimonics: the field)
                        s11_perception.tex    (§12 Perception of relational value)
                        s12_cocreation.tex    (§13 Cultivation & co-creation)
                        s13_return.tex        (§14 Securing the return)
                        s14_gift.tex          (§15 The gift)
                        s10_conclusions.tex   (§16 Conclusions; incl. §16.1)
                        s15_envoi.tex         (Envoi: How to Think of That Rose)
                        s16_ack.tex           (Acknowledgements)
                        appendixA.tex         (Appendix A: geometric phase, SFM)

REQUIREMENTS
  - XeLaTeX (uses fontspec / xeCJK).
  - Fonts: TeX Gyre Pagella (Latin body); Noto Serif CJK SC (Chinese, via \zh{}).
    Install both before compiling, or substitute in the preamble of main.tex.
  - Packages: fontspec, xeCJK, natbib, xcolor, amsmath, amssymb, geometry,
    titlesec, enumitem, etc. (all standard TeX Live).

BUILD  (manual passes — latexmk under-iterates the cross-references)
    xelatex main
    bibtex  main
    xelatex main
    xelatex main

  Produces main.pdf (68 pp).
