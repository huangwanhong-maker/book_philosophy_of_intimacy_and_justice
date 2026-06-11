#!/usr/bin/env bash
# One-pass XeLaTeX smoke test for each paper (no biber; bib may be absent).
# Catches structural/preamble breakage from the style refactor.
cd "$(dirname "$0")" || exit 1
for d in papers/*/; do
  slug=$(basename "$d")
  ( cd "$d" && TEXINPUTS=../../: timeout 240 xelatex -interaction=nonstopmode -halt-on-error "$slug.tex" >/dev/null 2>&1 )
  rc=$?
  if [ $rc -eq 0 ] && [ -f "$d/$slug.pdf" ]; then
    pages=$(cd "$d" && grep -aoE "Output written.*\(([0-9]+) page" "$slug.log" | grep -oE "[0-9]+ page" | head -1)
    echo "PASS  $slug   ($pages)"
  else
    echo "FAIL(rc=$rc)  $slug"
    (cd "$d" && grep -m5 "^!" "$slug.log" 2>/dev/null | sed 's/^/        /')
  fi
done
