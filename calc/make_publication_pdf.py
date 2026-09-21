#!/usr/bin/env python3
"""Publication typesetter: GRUT_de_Sitter_Absorptive_Response_v1.0.md -> .pdf

Conversion-only tool (owner mandate): no scientific content is generated or
altered here; the Markdown is the single source. Layout: A4 physics-preprint
style, DejaVu Serif text with full Greek/math glyph coverage, running header
with short title + page number (from p.2), version footer, centered display
blocks for blockquoted equations, gridded tables, hanging-indent lists.
"""
import os
import re
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle,
                                HRFlowable)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PUB = os.path.join(ROOT, "GRUT_de_Sitter_Absorptive_Response_v1.0")
SRC = os.path.join(PUB, "GRUT_de_Sitter_Absorptive_Response_v1.0.md")
OUT = os.path.join(PUB, "GRUT_de_Sitter_Absorptive_Response_v1.0.pdf")

FDIR = ("/Library/Frameworks/Python.framework/Versions/3.15/lib/python3.15/"
        "site-packages/matplotlib/mpl-data/fonts/ttf")
pdfmetrics.registerFont(TTFont("Serif", os.path.join(FDIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("Serif-B", os.path.join(FDIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Serif-I", os.path.join(FDIR, "DejaVuSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Serif-BI", os.path.join(FDIR, "DejaVuSerif-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("Sans", os.path.join(FDIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Mono", os.path.join(FDIR, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-B",
                              italic="Serif-I", boldItalic="Serif-BI")

S = {
    "title": ParagraphStyle("title", fontName="Serif-B", fontSize=15.5,
                            leading=20, alignment=1, spaceAfter=10),
    "author": ParagraphStyle("author", fontName="Serif", fontSize=12,
                             leading=15, alignment=1, spaceAfter=4),
    "front": ParagraphStyle("front", fontName="Serif-I", fontSize=9.3,
                            leading=12.6, alignment=4, spaceBefore=5,
                            spaceAfter=5, leftIndent=16, rightIndent=16),
    "h2": ParagraphStyle("h2", fontName="Serif-B", fontSize=12.3,
                         leading=15.5, spaceBefore=13, spaceAfter=6,
                         keepWithNext=1),
    "body": ParagraphStyle("body", fontName="Serif", fontSize=9.8,
                           leading=13.4, alignment=4, spaceAfter=5.5),
    "eq": ParagraphStyle("eq", fontName="Serif", fontSize=10.4,
                         leading=14.5, alignment=1, spaceBefore=5,
                         spaceAfter=5),
    "bullet": ParagraphStyle("bullet", fontName="Serif", fontSize=9.8,
                             leading=13.2, alignment=4, leftIndent=16,
                             firstLineIndent=-9, spaceAfter=3.2),
    "numitem": ParagraphStyle("numitem", fontName="Serif", fontSize=9.8,
                              leading=13.2, alignment=4, leftIndent=17,
                              firstLineIndent=-13, spaceAfter=3.2),
    "tcell": ParagraphStyle("tcell", fontName="Serif", fontSize=8.3,
                            leading=10.6, alignment=0),
    "tcellh": ParagraphStyle("tcellh", fontName="Serif-B", fontSize=8.3,
                             leading=10.6, alignment=0),
}

def esc(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # glyph fallback: U+2272/U+2273 are absent from DejaVu Serif but
    # present in DejaVu Sans (coverage audited over the whole document)
    for ch in ("\u2272", "\u2273"):
        t = t.replace(ch, '<font face="Sans">%s</font>' % ch)
    return t

def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Mono" size="8.4">\1</font>', t)
    return t

SHORT = "Wigner-time structure of one-loop graviton dissipation in de Sitter space"
VERS = "v1.0 · September 21, 2026"

def on_page(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setFont("Sans", 7.6)
        canv.setFillColor(colors.Color(0.25, 0.25, 0.25))
        canv.drawString(20 * mm, A4[1] - 13 * mm, SHORT)
        canv.drawRightString(A4[0] - 20 * mm, A4[1] - 13 * mm, str(doc.page))
        canv.setLineWidth(0.4)
        canv.setStrokeColor(colors.Color(0.55, 0.55, 0.55))
        canv.line(20 * mm, A4[1] - 15 * mm, A4[0] - 20 * mm, A4[1] - 15 * mm)
    canv.setFont("Sans", 7.2)
    canv.setFillColor(colors.Color(0.4, 0.4, 0.4))
    canv.drawCentredString(A4[0] / 2, 11 * mm, VERS)
    canv.restoreState()

def build():
    lines = open(SRC).read().splitlines()
    flow = []
    i = 0
    para = []

    def flush():
        nonlocal para
        if para:
            txt = " ".join(para).strip()
            para = []
            if not txt:
                return
            m = re.match(r"^\*\*(Im Σ.*)\*\*$", txt)
            if m:  # standalone bold equation line -> display
                flow.append(Paragraph("<b>" + esc(m.group(1)) + "</b>", S["eq"]))
                return
            if re.match(r"^\*[^*].*\*$", txt) and "Version note" not in txt \
               and "Publication note" not in txt:
                flow.append(Paragraph(inline(txt), S["front"]))
                return
            flow.append(Paragraph(inline(txt), S["body"]))

    n = len(lines)
    while i < n:
        L = lines[i]
        if L.startswith("# "):
            flush()
            flow.append(Spacer(1, 16))
            flow.append(Paragraph(esc(L[2:]), S["title"]))
        elif L.strip() == "**D. Ryan Grover**":
            flush()
            flow.append(Paragraph("D. Ryan Grover", S["author"]))
            flow.append(Spacer(1, 2))
        elif L.startswith("## "):
            flush()
            flow.append(Paragraph(esc(L[3:]), S["h2"]))
        elif L.startswith("> "):
            flush()
            block = []
            while i < n and lines[i].startswith(">"):
                block.append(lines[i][1:].strip())
                i += 1
            i -= 1
            flow.append(Paragraph("<i>" + esc(" ".join(block)) + "</i>",
                                  S["eq"]))
        elif L.startswith("|"):
            flush()
            rows = []
            while i < n and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.match(r"^[-: ]+$", c) for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            data = [[Paragraph(inline(c), S["tcellh" if r == 0 else "tcell"])
                     for c in row] for r, row in enumerate(rows)]
            widths = None
            if len(rows[0]) == 3:
                widths = [15 * mm, 105 * mm, 46 * mm]   # 166mm < 168mm frame
            t = Table(data, colWidths=widths, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.4, colors.Color(0.6, 0.6, 0.6)),
                ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.93, 0.93, 0.93)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
            ]))
            flow.append(Spacer(1, 4))
            flow.append(t)
            flow.append(Spacer(1, 6))
        elif L.startswith("- "):
            flush()
            item = [L[2:]]
            i += 1
            while i < n and lines[i].startswith("  ") and lines[i].strip():
                item.append(lines[i].strip())
                i += 1
            i -= 1
            flow.append(Paragraph("•  " + inline(" ".join(item)), S["bullet"]))
        elif re.match(r"^\d+\. ", L):
            flush()
            m = re.match(r"^(\d+)\. (.*)$", L)
            item = [m.group(2)]
            i += 1
            while i < n and lines[i].startswith("   ") and lines[i].strip():
                item.append(lines[i].strip())
                i += 1
            i -= 1
            flow.append(Paragraph(f"{m.group(1)}.  " + inline(" ".join(item)),
                                  S["numitem"]))
        elif L.strip() == "---":
            flush()
            flow.append(Spacer(1, 4))
            flow.append(HRFlowable(width="30%", thickness=0.5,
                                   color=colors.Color(0.6, 0.6, 0.6),
                                   hAlign="CENTER", spaceBefore=4,
                                   spaceAfter=8))
        elif not L.strip():
            flush()
        else:
            para.append(L.strip())
        i += 1
    flush()

    doc = BaseDocTemplate(OUT, pagesize=A4,
                          leftMargin=21 * mm, rightMargin=21 * mm,
                          topMargin=20 * mm, bottomMargin=18 * mm,
                          title=SHORT, author="D. Ryan Grover")
    fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
               id="main")
    doc.addPageTemplates([PageTemplate(id="page", frames=[fr],
                                       onPage=on_page)])
    doc.build(flow)
    print("wrote", OUT)

if __name__ == "__main__":
    build()
