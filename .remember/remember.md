# Handoff

## State
Table of Contents implemented in `uploads/generate_pdf.py`. `GRUTDocTemplate(BaseDocTemplate)` subclass with `afterFlowable` feeds H1 chapters/appendices (level 1) and H2 "Part …" dividers (level 0) into a `TableOfContents` flowable. TOC page sits on page 2 (Cover template, no header). Uses `doc.multiBuild(story)`. PDF rebuilt: 1659 flowables, 3.0 MB.

## Next
1. H(z) residuals integration — run v2 H(z) solver against real observational data; V7 source at `_archive_GRUT-RAI-v3-Sovereign-2026-05-07/grut/hubble_tension_metrics.py`
2. QNM/LIGO modules — held pending BH interior WP1-WP3 physics; revisit if that's ported to v2

## Context
DO NOT push to GitHub. Use python3.12 only (python3 = 3.15.0a2, lacks numpy). Pipeline from `uploads/`: `python3.12 make_figures.py && pdf_venv/bin/python3.12 generate_pdf.py`. V7 archive read-only at `/Users/mpg/Downloads/_archive_GRUT-RAI-v3-Sovereign-2026-05-07/`.
