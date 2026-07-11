Paper XXIV — The Emergence of Culture in Intimate Relation
The Three-Register Dialectic of the Relational Real
Philosophy of Intimacy and the Theory of Justice

BUILD
-----
Engine: XeLaTeX (required — uses fontspec with TeX Gyre Pagella + Noto Serif CJK SC)

  xelatex main
  bibtex  main
  xelatex main
  xelatex main

FONTS REQUIRED
--------------
  TeX Gyre Pagella   (body)
  Noto Serif CJK SC  (Chinese glyphs in glosses, epigraph, dedication, envoi)

STRUCTURE
---------
  main.tex            preamble, title page, epigraph, dedication, abstract,
                      TOC, and \input of all sections in three parts
  refs.bib            bibliography (all entries verified)
  sections/           one file per section

NOTE ON FILE NAMES
------------------
  The family-ethos section was added as section 27 (a bridge into Part Three).
  For that reason two files carry the s27 prefix:
     s27_familyethos.tex  -> printed as section 27 (Family Ethos, jiafeng)
     s27_production.tex   -> printed as section 28 (The Production of Culture)
  and s28..s32 print as sections 29..33. The \input order in main.tex is
  authoritative; section numbers are generated automatically by LaTeX.

OPEN ITEM
---------
  sections/s07_chinese.tex contains one \todo marking the classical-Chinese
  material (liyue, daosheng/ziran, the sense of hua vs. mere change) left for
  the author to supply or verify. The \todo will print in the PDF until filled
  or removed.
