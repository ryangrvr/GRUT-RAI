#!/usr/bin/env python3.12
"""Generate the GRUT ToE v3 PDF.

Interactive: PDF outline/bookmarks (sidebar navigation) + a clickable Table of
Contents with page numbers, and a dedicated title page. Reuses the proven v2
rendering machinery (fonts, tables, code, equations, inline markup, headers)
from generate_pdf.py; only the doc template (interactivity), the title page, and
a small markdown preprocessor are new.

Run:  uploads/pdf_venv/bin/python3.12 uploads/generate_pdf_v3.py
"""
import re
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    Frame, PageTemplate, Paragraph, Spacer, PageBreak, HRFlowable, NextPageTemplate,
    Image as RLImage, Table as RLTable, TableStyle as RLTableStyle, KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.enums import TA_CENTER

import generate_pdf as g   # reuse the v2 rendering machinery


# ── Figure embedding: render markdown images ![caption](path) ─────────────────
_IMG_RE = re.compile(r'^!\[(.*?)\]\((.+?)\)\s*$')
_fig_counter = [0]


def _figure_caption_style(S):
    return ParagraphStyle('FigCap', parent=S["caption"], alignment=TA_CENTER,
                          leftIndent=10, rightIndent=10, fontSize=9, leading=12,
                          spaceBefore=2, spaceAfter=12)


def parse_md_with_images(body: str, S):
    """Like g.parse_md, but renders standalone `![caption](path)` lines as centered,
    auto-numbered figures (with caption) instead of literal text."""
    from PIL import Image as PILImage
    cap_style = _figure_caption_style(S)
    out, buf = [], []

    def flush():
        if buf:
            out.extend(g.parse_md('\n'.join(buf), S))
            buf.clear()

    for ln in body.split('\n'):
        m = _IMG_RE.match(ln.strip())
        if not m:
            buf.append(ln)
            continue
        flush()
        caption, rel = m.group(1), m.group(2)
        path = HERE / rel
        if not path.exists():
            buf.append(f"*(missing figure: {rel})*")
            continue
        with PILImage.open(path) as im:
            iw, ih = im.size
        w = min(g.CONTENT_W * 0.84, iw * 72 / 200.0)   # px@200dpi → pt, ≤84% width
        h = w * ih / iw
        _fig_counter[0] += 1
        img = RLImage(str(path), width=w, height=h)
        block = [RLTable([[img]], colWidths=[g.CONTENT_W],
                         style=RLTableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                             ('TOPPADDING', (0, 0), (-1, -1), 10),
                                             ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))]
        if caption:
            block.append(Paragraph(g._font_fallback(g.esc(f"Figure {_fig_counter[0]}.  ")) +
                                   g.inline(caption), cap_style))
        out.append(KeepTogether(block))
    flush()
    return out

HERE       = Path(__file__).resolve().parent
INPUT_MD   = HERE / "GRUT_TOE_V3_upload.md"
OUTPUT_PDF = HERE / "GRUT_TOE_V3.1.pdf"


# ──────────────────────────────────────────────────────────────────────────────
# Rendering fixes for v3 — patch the shared machinery at runtime (generate_pdf.py
# stays byte-identical; the v2 artifact is frozen).
# ──────────────────────────────────────────────────────────────────────────────

# (a) Glyphs Georgia lacks that DejaVuSerif has, but that weren't in the fallback
#     table: superscript parens ⁽ ⁾ (from "K⁽²⁾") and ∩ (from "Q ∩ F ∩ D").
g._SERIF_FALLBACK = g._SERIF_FALLBACK | frozenset('⁽⁾∩')
g._GEO_MISSING    = g._SERIF_FALLBACK | g._SANS_FALLBACK

# (b) Display equations ($$…$$): matplotlib mathtext can't parse raw unicode Greek
#     or unicode sub/superscripts, so it fails and the renderer falls back to raw
#     LaTeX text (the "broken equation" symptom). Convert unicode → LaTeX first.
_UNI2TEX = {
    'α': r'\alpha ', 'β': r'\beta ', 'γ': r'\gamma ', 'δ': r'\delta ',
    'ε': r'\epsilon ', 'ζ': r'\zeta ', 'η': r'\eta ', 'θ': r'\theta ',
    'ι': r'\iota ', 'κ': r'\kappa ', 'λ': r'\lambda ', 'μ': r'\mu ',
    'ν': r'\nu ', 'ξ': r'\xi ', 'π': r'\pi ', 'ρ': r'\rho ', 'σ': r'\sigma ',
    'τ': r'\tau ', 'υ': r'\upsilon ', 'φ': r'\phi ', 'χ': r'\chi ',
    'ψ': r'\psi ', 'ω': r'\omega ',
    'Γ': r'\Gamma ', 'Δ': r'\Delta ', 'Θ': r'\Theta ', 'Λ': r'\Lambda ',
    'Ξ': r'\Xi ', 'Π': r'\Pi ', 'Σ': r'\Sigma ', 'Φ': r'\Phi ',
    'Ψ': r'\Psi ', 'Ω': r'\Omega ',
    '∇': r'\nabla ', '∂': r'\partial ', '∝': r'\propto ', '×': r'\times ',
    '·': r'\cdot ', '≈': r'\approx ', '≪': r'\ll ', '≫': r'\gg ',
    '≤': r'\leq ', '≥': r'\geq ', '≠': r'\neq ', '∞': r'\infty ',
    '∈': r'\in ', '∩': r'\cap ', '∪': r'\cup ', '→': r'\rightarrow ',
    '⟨': r'\langle ', '⟩': r'\rangle ', 'ℏ': r'\hbar ', '−': '-', '√': r'\sqrt',
}
_SUBD = {chr(0x2080 + i): str(i) for i in range(10)}   # ₀..₉
_SUPD = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6',
         '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '-', '⁽': '(', '⁾': ')'}


def _uni_to_tex(s: str) -> str:
    s = re.sub('[' + ''.join(_SUBD) + ']+',
               lambda m: '_{' + ''.join(_SUBD[c] for c in m.group()) + '}', s)
    s = re.sub('[' + ''.join(re.escape(k) for k in _SUPD) + ']+',
               lambda m: '^{' + ''.join(_SUPD[c] for c in m.group()) + '}', s)
    for u, t in _UNI2TEX.items():
        s = s.replace(u, t)
    return s


_orig_latex_preprocess = g._latex_preprocess
g._latex_preprocess = lambda s: _orig_latex_preprocess(_uni_to_tex(s))


# ──────────────────────────────────────────────────────────────────────────────
# Preprocess the reader-edition markdown for the v2 parser:
#   • drop the title block (the title page reproduces it); start at the
#     "How to read this book" box,
#   • promote headings so the parser's chapter machinery applies:
#       ##  (chapter)    -> #   (H1: chapter styling + running header)
#       ### (subsection) -> ##  (H2)
#   • inject a page break before every chapter so each starts on a fresh page.
# ──────────────────────────────────────────────────────────────────────────────
def preprocess(text: str) -> str:
    lines = text.split('\n')
    start = next((i for i, l in enumerate(lines)
                  if l.strip().startswith('> **How to read')), 0)
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

    # Merge each run of consecutive blockquote lines into ONE line, so a
    # hard-wrapped multi-line callout renders as a single bq paragraph with
    # uniform leading. (g.parse_md makes one spaced paragraph per `>` line,
    # which otherwise puts a gap between every wrapped line of a callout.)
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
# Interactive document template: TOC entries + PDF outline (bookmarks).
# Chapters are H1 (post-promotion), subsections are H2.
# ──────────────────────────────────────────────────────────────────────────────
class GRUTDocTemplateV3(g.GRUTDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._key_n = 0

    def beforeDocument(self):
        # multiBuild reuses this instance across passes; reset the key counter
        # each pass so bookmark/TOC keys are deterministic (ch1..chN every pass)
        # and the TOC actually converges.
        self._key_n = 0

    def afterFlowable(self, flowable):
        # Repaint the running header on chapter-opening pages (the onPage hook
        # fires before flowables are drawn, so it carries the prior chapter).
        if isinstance(flowable, g.ChapterMarker) and self.page > 2:
            c = self.canv
            c.saveState()
            # Fully white-out the LEFT header band (the onPage hook painted the
            # PREVIOUS chapter title here). The rect must clear the title's full
            # glyph height — ascenders to descenders — or the old title pokes out
            # above the new one. Stay left of the right-aligned series title and
            # above the header rule (at 0.72in).
            c.setFillColor(white)
            c.rect(g.ML - 4, g.PAGE_H - 0.715 * inch,
                   (g.PAGE_W - g.MR - g.ML) * 0.66, 0.205 * inch, fill=1, stroke=0)
            c.setFont("Georgia-Italic", 8)
            c.setFillColor(g.C_GRAY6)
            c.drawString(g.ML, g.PAGE_H - 0.60 * inch, flowable.name[:72])
            c.restoreState()

        if self._grut_toc is None or not isinstance(flowable, Paragraph):
            return
        try:
            text = flowable.getPlainText().strip()
        except Exception:
            return
        name = flowable.style.name
        if name == 'H1':                       # chapter
            self._key_n += 1
            key = f'ch{self._key_n}'
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=0, closed=False)
            # Printed TOC: chapters only (keeps it to one page, so page numbers
            # converge — no boundary-flip oscillation across passes).
            self._grut_toc.notify('TOCEntry', (0, text, self.page, key))
        elif name == 'H2':                     # subsection
            self._key_n += 1
            key = f'sec{self._key_n}'
            self.canv.bookmarkPage(key)
            # Subsections appear both in the interactive sidebar outline and,
            # indented at level 1, in the printed TOC. Keys are deterministic
            # (reset each pass in beforeDocument), so multiBuild converges even
            # though the TOC now spans multiple pages.
            self.canv.addOutlineEntry(text, key, level=1, closed=True)
            self._grut_toc.notify('TOCEntry', (1, text, self.page, key))


# ──────────────────────────────────────────────────────────────────────────────
# Title page
# ──────────────────────────────────────────────────────────────────────────────
def cover_page_v3(S):
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
        Spacer(1, 1.5 * inch),
        Paragraph("Grand Responsive Universe Theory", S["cvtitle"]),
        Spacer(1, 0.1 * inch),
        HRFlowable(width="60%", thickness=1.5, color=g.C_NAVY,
                   hAlign='CENTER', spaceBefore=4, spaceAfter=16),
        Paragraph("A Candidate Theory of Everything<br/>"
                  "from a Viscoelastic Gravitational Medium with Finite Memory",
                  S["cvsub"]),
        Spacer(1, 0.6 * inch),
        Paragraph("D. Ryan Grover", S["cvauth"]),
        Spacer(1, 0.15 * inch),
        Paragraph(ff("June 2026  ·  GRUT ToE v3.1  ·  Candidate Framework"), S["cvauth"]),
        Spacer(1, 0.8 * inch),
        HRFlowable(width="40%", thickness=0.5, color=g.C_BORDER,
                   hAlign='CENTER', spaceBefore=4, spaceAfter=16),
        Paragraph(ff(links), S["cvsmall"]),
        Spacer(1, 0.2 * inch),
        Paragraph(ff(
            "116 registered claims  ·  3,227 passing tests  ·  28 open negatives documented<br/>"
            "Every claim is marked at the tier it earned.  Every negative is documented.  "
            "Nothing is fitted away."), S["cvsmall"]),
        PageBreak(),
    ]
    return els


# ──────────────────────────────────────────────────────────────────────────────
# Build
# ──────────────────────────────────────────────────────────────────────────────
def build_v3(md_path: Path = INPUT_MD, out_path: Path = OUTPUT_PDF):
    print(f"Reading {md_path.name} …")
    text = md_path.read_text(encoding='utf-8')
    body = preprocess(text)
    print(f"  {len(text.splitlines())} lines → {len(body.splitlines())} after preprocess")

    FR = g.register_fonts()
    S  = g.make_styles(FR)
    B, BB = FR["body"], FR["bodyB"]

    toc = TableOfContents()
    toc.dotsMinLevel = 0   # dotted leaders to page numbers at every level
    toc.levelStyles = [
        ParagraphStyle('TOC0', fontName=BB, fontSize=11.5, leading=18,
                       textColor=g.C_NAVY, spaceBefore=11, spaceAfter=2),
        ParagraphStyle('TOC1', fontName=B, fontSize=10, leading=14,
                       textColor=g.C_SLATE, leftIndent=20, spaceBefore=1, spaceAfter=1),
    ]

    doc = GRUTDocTemplateV3(
        str(out_path),
        toc=toc,
        pagesize=letter,
        leftMargin=g.ML, rightMargin=g.MR, topMargin=g.MT, bottomMargin=g.MB,
        title="Grand Responsive Universe Theory — GRUT ToE v3.1",
        author="D. Ryan Grover",
        subject="GRUT v3 — a constraint-defined candidate Theory of Everything",
        creator="GRUT PDF Generator v3 (reportlab)",
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
    story += cover_page_v3(S)             # page 1: title page
    story += g.make_toc_page(S, toc)      # page 2: clickable TOC
    story.append(NextPageTemplate('Normal'))
    _fig_counter[0] = 0
    story += parse_md_with_images(body, S)   # page 3+: body (with embedded figures)

    print(f"  {len(story)} flowables")
    print(f"Building (multiBuild for TOC convergence) → {out_path.name} …")
    doc.multiBuild(story)
    mb = out_path.stat().st_size / 1024**2
    print(f"✓ Done.  {out_path}  ({mb:.2f} MB)")
    return toc


if __name__ == "__main__":
    build_v3()
