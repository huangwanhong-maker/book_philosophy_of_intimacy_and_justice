# Philosophy of Intimacy and the Theory of Justice — paper series build.
#
# Each paper lives in its own folder under papers/ and builds independently;
# all share ../serendip-paper.sty (one source of truth for the visual style).
#
#   make            build every paper, then collect the PDFs into pdfs/
#   make build      build every paper (PDF stays in its own folder)
#   make <id>       build one, e.g.  make paper_03_self_legislation
#   make pdfs       copy each built PDF into pdfs/ (builds nothing)
#   make clean      remove aux files (keep PDFs)
#   make cleanall   remove aux files and PDFs (in folders and in pdfs/)
#
# Requires XeLaTeX + latexmk (run under WSL/TeX Live here). Each paper carries
# its own refs.bib; without it, citations resolve to "??".

PAPERS := $(notdir $(wildcard papers/*))
PDFDIR := pdfs

.PHONY: all build pdfs clean cleanall $(PAPERS)

all: build pdfs

build:
	@for d in papers/*/; do echo "==> $$d"; ( cd "$$d" && latexmk ) || exit 1; done

# Collect each paper's PDF into pdfs/ (keeps the folder-based filenames).
pdfs:
	@mkdir -p $(PDFDIR)
	@for d in papers/*/; do \
	  slug=$$(basename "$$d"); \
	  if [ -f "$$d/$$slug.pdf" ]; then cp -f "$$d/$$slug.pdf" "$(PDFDIR)/$$slug.pdf"; echo "  -> $(PDFDIR)/$$slug.pdf"; \
	  else echo "  !! missing $$d$$slug.pdf (build it first)"; fi; \
	done

clean:
	@for d in papers/*/; do ( cd "$$d" && latexmk -c ); done

cleanall:
	@for d in papers/*/; do ( cd "$$d" && latexmk -C ); done
	@rm -f $(PDFDIR)/*.pdf

# Build a single paper and refresh its copy in pdfs/.
$(PAPERS):
	@cd papers/$@ && latexmk
	@mkdir -p $(PDFDIR) && cp -f papers/$@/$@.pdf $(PDFDIR)/$@.pdf && echo "  -> $(PDFDIR)/$@.pdf"
