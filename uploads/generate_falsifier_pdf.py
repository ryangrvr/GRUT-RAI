#!/usr/bin/env python3
"""
Generate GRUT_FALSIFIER_PAPER.pdf from GRUT_FALSIFIER_PAPER_upload.md.
Reuses the full generate_pdf.py rendering engine.  Figures 6, 7, 8 (fσ₈,
S₈, CMB ISW) are already in the base _FIGURE_PNGS dict.

Run from the uploads/ directory:
    pdf_venv/bin/python3.12 generate_falsifier_pdf.py
"""

from pathlib import Path
import sys

_HERE = Path(__file__).parent
sys.path.insert(0, str(_HERE))

import generate_pdf

INPUT  = _HERE / "GRUT_FALSIFIER_PAPER_upload.md"
OUTPUT = _HERE / "GRUT_FALSIFIER_PAPER.pdf"

if __name__ == "__main__":
    print(f"Building {OUTPUT.name} from {INPUT.name} ...")
    generate_pdf.build(INPUT, OUTPUT)
    print("Done.")
