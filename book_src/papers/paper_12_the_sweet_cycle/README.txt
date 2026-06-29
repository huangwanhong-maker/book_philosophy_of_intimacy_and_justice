The Sweet Cycle (Paper XII)
Philosophy of Intimacy and the Theory of Justice

FILES
  The_Sweet_Cycle_Paper_XII.tex   main document (uses external .bib)
  references.bib                  BibTeX bibliography (31 entries, all verified)

COMPILATION
  Requires XeLaTeX and the fonts "TeX Gyre Pagella" and "Noto Serif CJK SC".
  Build sequence (the document uses \nocite{*}, so all .bib entries print
  whether or not they are cited in the prose):

      xelatex The_Sweet_Cycle_Paper_XII
      bibtex  The_Sweet_Cycle_Paper_XII
      xelatex The_Sweet_Cycle_Paper_XII
      xelatex The_Sweet_Cycle_Paper_XII

NOTES
  - Bibliography style is "plain". Titles are double-braced in the .bib to
    preserve capitalization; translators are folded into note fields because
    plain.bst does not support a translator field.
  - To cite a work inline, use \cite{key} with the keys defined in references.bib
    (e.g. \cite{doi}, \cite{ngai}, \cite{eglash}).
