#!/usr/bin/env bash
# make_pdf.sh — typeset the GRUT public-record Markdown with LaTeX (XeLaTeX).
#
# Conversion only: the Markdown file is the single source of truth; no
# scientific content is generated or altered. Equations are typeset by LaTeX
# (unicode-math, Latin Modern Math); the PDF carries a hyperlinked table of
# contents with page numbers and PDF bookmarks (hyperref).
#
# Requirements: pandoc >= 3, XeLaTeX (TeX Live 2023+: texlive-xetex,
# texlive-latex-recommended, texlive-latex-extra, fonts-lmodern).
#
# Usage: ./make_pdf.sh [input.md] [output.pdf]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
IN="${1:-$HERE/../GRUT_Consolidated_Theory_PUBLIC_RECORD.md}"
OUT="${2:-$HERE/../GRUT_Consolidated_Theory_PUBLIC_RECORD.pdf}"
PANDOC="${PANDOC:-pandoc}"

"$PANDOC" "$IN" \
  --from=markdown+tex_math_dollars+pipe_tables-implicit_figures \
  --to=pdf \
  --pdf-engine=xelatex \
  --lua-filter="$HERE/grut_filter.lua" \
  --include-in-header="$HERE/grut_header.tex" \
  --toc --toc-depth=2 \
  --metadata=author:"D. Ryan Grover" \
  --metadata=date:"26 September 2026" \
  -V documentclass=article \
  -V papersize=a4 \
  -V fontsize=11pt \
  -V geometry:margin=22mm \
  -V mainfont="Latin Modern Roman" \
  -V sansfont="Latin Modern Sans" \
  -V monofont="Latin Modern Mono" \
  -V linkcolor=NavyBlue -V urlcolor=NavyBlue -V toccolor=black \
  -V colorlinks=true \
  -V toc-title="Contents" \
  -V linestretch=1.08 \
  --output="$OUT"
echo "wrote $OUT"
