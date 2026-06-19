#!/usr/bin/env python3.12
"""Render PDF pages to PNG for visual verification — the clean, OS-independent way.

Uses pypdfium2 (Google's PDFium, a self-contained wheel with no system deps), so
it works on macOS 12 where Homebrew's poppler/pdftoppm cannot be built.

Install (once):  uploads/pdf_venv/bin/python3.12 -m pip install pypdfium2
Usage:           uploads/pdf_venv/bin/python3.12 uploads/render_pages.py FILE.pdf 2 8 13 17
                 (no page args → renders all pages). PNGs land in /tmp/<stem>_pNN.png
"""
import sys
from pathlib import Path

import pypdfium2 as pdfium


def render(pdf_path, pages=None, scale=2.0, outdir="/tmp"):
    pdf = pdfium.PdfDocument(str(pdf_path))
    n = len(pdf)
    pages = pages or range(1, n + 1)
    stem = Path(pdf_path).stem
    out = []
    for p in pages:
        if not (1 <= p <= n):
            print(f"  skip page {p} (out of range 1..{n})")
            continue
        path = f"{outdir}/{stem}_p{p:02d}.png"
        pdf[p - 1].render(scale=scale).to_pil().save(path)
        out.append(path)
        print(f"  page {p:>3} -> {path}")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: render_pages.py FILE.pdf [page ...]")
    f = sys.argv[1]
    pgs = [int(x) for x in sys.argv[2:]] or None
    print(f"Rendering {f} ({len(pdfium.PdfDocument(f))} pages)…")
    render(f, pgs)
