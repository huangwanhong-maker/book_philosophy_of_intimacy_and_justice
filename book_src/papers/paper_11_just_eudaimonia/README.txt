Paper XI — A Just Eudaimonia: The Everyday Fabric of a Shared Life and the Praxis of Flourishing

BUILD (XeLaTeX required; uses fontspec + Noto Serif CJK SC + TeX Gyre Pagella):
    xelatex main.tex
    bibtex  main
    xelatex main.tex
    xelatex main.tex

FILES:
    main.tex            — master file (preamble, title, dedication, \input of all sections)
    refs.bib            — bibliography (BibTeX)
    sections/*.tex      — the section files, \input by main.tex in reading order

A single-file version (everything inlined, no \input dependencies) is provided
separately as Paper_XI_standalone.tex — easiest for arXiv/SSRN upload.

Fonts required: Noto Serif CJK SC (for Chinese), TeX Gyre Pagella (Latin).
