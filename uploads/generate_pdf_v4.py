#!/usr/bin/env python3.12
"""Generate the GRUT ToE v4 PDF — "The Emergence of Everything".

Reader edition: PDF outline/bookmarks (sidebar navigation) + a clickable Table
of Contents with page numbers, a dedicated title page, embedded figures, and
per-section spec boxes (markdown `>` callouts → boxed). Reuses the proven v2/v3
rendering machinery (fonts, tables, code, equations, inline markup, headers,
figure embedding) from generate_pdf.py / generate_pdf_v3.py; only the input,
title page, metadata, and the preprocess start-anchor differ.

Run:  uploads/pdf_venv/bin/python3.12 uploads/generate_pdf_v4.py
"""
import re
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import white, HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    Frame, PageTemplate, Paragraph, Spacer, PageBreak, HRFlowable, NextPageTemplate,
    KeepTogether, Image as RLImage, Table as RLTable, TableStyle as RLTableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

import generate_pdf as g          # reuse the v2 rendering machinery
import generate_pdf_v3 as g3      # reuse the v3 figure embedding + unicode→tex + template

HERE       = Path(__file__).resolve().parent
INPUT_MD   = HERE / "GRUT_TOE_V4_upload.md"
OUTPUT_PDF = HERE / "GRUT_TOE_V4.pdf"

# The v3 module already installed: the serif-fallback glyph additions, the
# unicode→LaTeX display-equation fix, and the figure machinery. Reuse them and
# keep figure paths resolving relative to uploads/ (HERE).
g3.HERE = HERE


def parse_md_v4(body: str, S):
    """Like g.parse_md, but (a) renders standalone `![caption](path)` lines as
    centered, auto-numbered figures, and (b) renders each `>` callout (the
    preprocess merges every spec box / overclaim flag / verdict into ONE `>`
    line) as a boxed paragraph wrapped in KeepTogether — so a box never splits
    across a page (no broken borders). Everything else falls through to g.parse_md."""
    from PIL import Image as PILImage
    cap_style = g3._figure_caption_style(S)
    out, buf = [], []

    def flush():
        if buf:
            out.extend(g.parse_md('\n'.join(buf), S))
            buf.clear()

    for ln in body.split('\n'):
        s = ln.strip()

        m = g3._IMG_RE.match(s)
        if m:                                   # ── figure ──
            flush()
            caption, rel = m.group(1), m.group(2)
            path = HERE / rel
            if not path.exists():
                buf.append(f"*(missing figure: {rel})*")
                continue
            with PILImage.open(path) as im:
                iw, ih = im.size
            w = min(g.CONTENT_W * 0.84, iw * 72 / 200.0)
            h = w * ih / iw
            g3._fig_counter[0] += 1
            img = RLImage(str(path), width=w, height=h)
            block = [RLTable([[img]], colWidths=[g.CONTENT_W],
                             style=RLTableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                                 ('TOPPADDING', (0, 0), (-1, -1), 10),
                                                 ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))]
            if caption:
                block.append(Paragraph(
                    g._font_fallback(g.esc(f"Figure {g3._fig_counter[0]}.  ")) +
                    g.inline(caption), cap_style))
            out.append(KeepTogether(block))
            continue

        if s.startswith('>') and s.strip() != '>':   # ── boxed callout ──
            flush()
            content = re.sub(r'^>\s?', '', s)
            try:
                para = Paragraph(g.inline(content), S["bq"])
            except Exception:
                para = Paragraph(g.esc(content), S["bq"])
            out.append(KeepTogether([para]))
            continue

        buf.append(ln)

    flush()
    return out


# ──────────────────────────────────────────────────────────────────────────────
# Preprocess: drop the front-matter title block (the cover reproduces it), start
# the body at the Abstract; promote headings so the chapter machinery applies;
# page-break before every chapter; merge multi-line `>` callouts into one bq.
# ──────────────────────────────────────────────────────────────────────────────
_BODY_START = re.compile(r'^(\*\*Abstract\.|##\s+(Abstract|The thesis)\b)', re.IGNORECASE)


def preprocess(text: str) -> str:
    lines = text.split('\n')
    start = next((i for i, l in enumerate(lines) if _BODY_START.match(l.strip())), 0)
    out = []
    for l in lines[start:]:
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m:
            new_hl = max(1, len(m.group(1)) - 1)
            if new_hl == 1:                       # a chapter — break to a new page
                out.append('<div style="page-break-before: always"></div>')
            out.append('#' * new_hl + ' ' + m.group(2))
        else:
            out.append(l)

    # Merge each run of consecutive blockquote lines into ONE line (uniform
    # leading for hard-wrapped callouts / spec boxes).
    merged, buf = [], []

    def _flush():
        if buf:
            merged.append('> ' + ' '.join(
                re.sub(r'^>\s?', '', b).rstrip() for b in buf))
            buf.clear()

    for l in out:
        s = l.lstrip()
        if s.startswith('>') and s.strip() != '>':
            buf.append(l)
        else:
            _flush()
            merged.append(l)
    _flush()
    return '\n'.join(merged)


# ──────────────────────────────────────────────────────────────────────────────
# Title page
# ──────────────────────────────────────────────────────────────────────────────
def cover_page_v4(S):
    ff = g._font_fallback
    LC = "#2C3E73"   # link colour
    links = (
        'GRUT Research:  '
        f'<link href="https://www.zenodo.org/communities/GRUT" color="{LC}">'
        'www.zenodo.org/communities/GRUT</link><br/>'
        'GRUT-RAI Codebase:  '
        f'<link href="https://doi.org/10.5281/zenodo.18993689" color="{LC}">'
        'DOI 10.5281/zenodo.18993689</link><br/>'
        'GRUT-RAI Repository:  '
        f'<link href="https://github.com/ryangrvr/GRUT-RAI" color="{LC}">'
        'www.github.com/ryangrvr/GRUT-RAI</link>'
    )
    els = [
        Spacer(1, 1.35 * inch),
        Paragraph("Grand Responsive Universe Theory", S["cvtitle"]),
        Spacer(1, 0.1 * inch),
        HRFlowable(width="60%", thickness=1.5, color=g.C_NAVY,
                   hAlign='CENTER', spaceBefore=4, spaceAfter=16),
        Paragraph("The Emergence of Everything<br/>"
                  "A Candidate Theory of Everything Organized Around "
                  "the Emergence of Responsiveness",
                  S["cvsub"]),
        Spacer(1, 0.55 * inch),
        Paragraph("D. Ryan Grover", S["cvauth"]),
        Spacer(1, 0.15 * inch),
        Paragraph(ff("June 2026  ·  GRUT ToE v4  ·  Candidate Framework · Reader Edition"),
                  S["cvauth"]),
        Spacer(1, 0.7 * inch),
        HRFlowable(width="40%", thickness=0.5, color=g.C_BORDER,
                   hAlign='CENTER', spaceBefore=4, spaceAfter=16),
        Paragraph(ff(links), S["cvsmall"]),
        Spacer(1, 0.2 * inch),
        Paragraph(ff(
            "121 registered claims  ·  six tiers, machine-checked  ·  "
            "28 open negatives documented<br/>"
            "Every claim is marked at the tier it earned.  Every negative is documented.  "
            "Nothing is fitted away."), S["cvsmall"]),
        PageBreak(),
    ]
    return els


# ──────────────────────────────────────────────────────────────────────────────
# Build
# ──────────────────────────────────────────────────────────────────────────────
def build_v4(md_path: Path = INPUT_MD, out_path: Path = OUTPUT_PDF):
    print(f"Reading {md_path.name} …")
    text = md_path.read_text(encoding='utf-8')
    body = preprocess(text)
    print(f"  {len(text.splitlines())} lines → {len(body.splitlines())} after preprocess")

    FR = g.register_fonts()
    S  = g.make_styles(FR)
    B, BB = FR["body"], FR["bodyB"]

    # v4: upgrade blockquote callouts to true boxes (light fill + thin border) so
    # the per-section spec boxes read as boxed callouts, not just indented text.
    # Every `>` callout (spec boxes, overclaim flags, decisive-test verdicts) gets it.
    S["bq"].backColor     = HexColor("#f5f7fb")
    S["bq"].borderColor   = HexColor("#9fb0cc")
    S["bq"].borderWidth   = 0.6
    S["bq"].borderPadding = 8
    S["bq"].leftIndent    = 14
    S["bq"].rightIndent   = 10
    S["bq"].spaceBefore   = 9
    S["bq"].spaceAfter    = 9
    S["bq"].leading       = 15.5

    toc = TableOfContents()
    toc.dotsMinLevel = 0
    toc.levelStyles = [
        ParagraphStyle('TOC0', fontName=BB, fontSize=11.5, leading=18,
                       textColor=g.C_NAVY, spaceBefore=11, spaceAfter=2),
        ParagraphStyle('TOC1', fontName=B, fontSize=10, leading=14,
                       textColor=g.C_SLATE, leftIndent=20, spaceBefore=1, spaceAfter=1),
    ]

    doc = g3.GRUTDocTemplateV3(
        str(out_path),
        toc=toc,
        pagesize=letter,
        leftMargin=g.ML, rightMargin=g.MR, topMargin=g.MT, bottomMargin=g.MB,
        title="Grand Responsive Universe Theory — GRUT ToE v4 (The Emergence of Everything)",
        author="D. Ryan Grover",
        subject="GRUT v4 — a candidate Theory of Everything organized around the emergence of responsiveness",
        creator="GRUT PDF Generator v4 (reportlab)",
    )

    content_frame = Frame(g.ML, g.MB, g.CONTENT_W, g.PAGE_H - g.MT - g.MB,
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                          id='normal', showBoundary=0)
    title_frame   = Frame(g.ML, g.MB, g.CONTENT_W, g.PAGE_H - 0.75 * inch - g.MB,
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
                          id='title', showBoundary=0)
    doc.addPageTemplates([
        PageTemplate(id='Cover',  frames=[title_frame],   onPage=g.title_footer),
        PageTemplate(id='Normal', frames=[content_frame], onPage=g.header_footer),
    ])

    print("Assembling story …")
    story = []
    story += cover_page_v4(S)             # page 1: title page
    story += g.make_toc_page(S, toc)      # page 2: clickable TOC
    story.append(NextPageTemplate('Normal'))
    g3._fig_counter[0] = 0
    story += parse_md_v4(body, S)   # page 3+: body (figures + boxed callouts, KeepTogether)

    print(f"  {len(story)} flowables")
    print(f"Building (multiBuild for TOC convergence) → {out_path.name} …")
    doc.multiBuild(story)
    mb = out_path.stat().st_size / 1024**2
    print(f"✓ Done.  {out_path}  ({mb:.2f} MB)")
    return toc


if __name__ == "__main__":
    build_v4()
