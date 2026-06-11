#!/usr/bin/env python3
"""
GRUT TOE Upload — Professional Book-Style PDF Generator
Uses reportlab with Georgia (body) and Menlo (code) fonts.
Run with: /Users/mpg/Library/Mobile\ Documents/com~apple~CloudDocs/Ryans\ Projects/GRUT-RAI-v2/uploads/pdf_venv/bin/python3.12 generate_pdf.py
"""

import re, sys, os, io
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate,
    Paragraph, Spacer, Table, TableStyle, PageBreak,
    Preformatted, HRFlowable, KeepTogether, CondPageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError

# ── Paths ──────────────────────────────────────────────────────────────────────
_HERE       = Path(__file__).parent
INPUT_MD    = _HERE / "GRUT_TOE_upload.md"
OUTPUT_PDF  = _HERE / "GRUT_TOE.pdf"
FIGURES_DIR = _HERE / "figures"

# Font name for inline math glyphs (set by register_fonts)
_MATH_FONT = "Times-Italic"   # safe fallback; overridden to DejaVuSerif-Italic

# Figure stub → PNG filename mapping
_FIGURE_PNGS = {
    1: "fig_01_two_scales.png",
    2: "fig_02_three_regimes.png",
    3: "fig_03_gate_r.png",
    4: "fig_04_cluster_schematic.png",
    5: "fig_05_cluster_scaling.png",
    6: "fig_06_modified_gravity.png",
    7: "fig_07_cmb_pk.png",
    8: "fig_08_mgcamb_prototype.png",
    9: "fig_09_open_ledger.png",
   10: "fig_10_grut_chain.png",
   11: "fig_11_schrodinger_inversion.png",
}

PAGE_W, PAGE_H = letter          # 8.5 × 11 inches
ML = 1.25 * inch                 # left margin (wider for book feel)
MR = 1.0  * inch
MT = 1.1  * inch
MB = 0.62 * inch
CONTENT_W = PAGE_W - ML - MR    # usable text width

# ── Colours ───────────────────────────────────────────────────────────────────
C_NAVY   = HexColor("#1a2744")
C_SLATE  = HexColor("#2c3e50")
C_GRAY6  = HexColor("#666666")
C_GRAY4  = HexColor("#444444")
C_BORDER = HexColor("#c0c8d4")
C_CODEBG = HexColor("#f6f7f9")
C_TBLHD  = HexColor("#1a2744")
C_TBLALT = HexColor("#eef1f6")
C_MATHBG = HexColor("#f0f4fa")
C_HR     = HexColor("#9ba8b7")
C_CAPFG  = HexColor("#3a3a3a")
C_LINK   = HexColor("#1a5276")

# ── Font registration ─────────────────────────────────────────────────────────
def register_fonts():
    font_reg = {}
    GEO = "/System/Library/Fonts/Supplemental/Georgia"
    try:
        pdfmetrics.registerFont(TTFont("Georgia",           GEO + ".ttf"))
        pdfmetrics.registerFont(TTFont("Georgia-Bold",      GEO + " Bold.ttf"))
        pdfmetrics.registerFont(TTFont("Georgia-Italic",    GEO + " Italic.ttf"))
        pdfmetrics.registerFont(TTFont("Georgia-BoldItalic",GEO + " Bold Italic.ttf"))
        pdfmetrics.registerFontFamily("Georgia",
            normal="Georgia", bold="Georgia-Bold",
            italic="Georgia-Italic", boldItalic="Georgia-BoldItalic")
        font_reg["body"]  = "Georgia"
        font_reg["bodyB"] = "Georgia-Bold"
        font_reg["bodyI"] = "Georgia-Italic"
        font_reg["bodyBI"]= "Georgia-BoldItalic"
        print("✓ Georgia fonts registered")
    except TTFError as e:
        print(f"  Georgia fallback to Times-Roman: {e}")
        font_reg["body"]  = "Times-Roman"
        font_reg["bodyB"] = "Times-Bold"
        font_reg["bodyI"] = "Times-Italic"
        font_reg["bodyBI"]= "Times-BoldItalic"

    try:
        pdfmetrics.registerFont(TTFont("Menlo",      "/System/Library/Fonts/Menlo.ttc", subfontIndex=0))
        pdfmetrics.registerFont(TTFont("Menlo-Bold", "/System/Library/Fonts/Menlo.ttc", subfontIndex=1))
        font_reg["mono"]  = "Menlo"
        font_reg["monoB"] = "Menlo-Bold"
        print("✓ Menlo fonts registered")
    except TTFError as e:
        print(f"  Menlo fallback to Courier: {e}")
        font_reg["mono"]  = "Courier"
        font_reg["monoB"] = "Courier-Bold"

    try:
        pdfmetrics.registerFont(TTFont("Palatino",      "/System/Library/Fonts/Palatino.ttc", subfontIndex=0))
        pdfmetrics.registerFont(TTFont("Palatino-Bold", "/System/Library/Fonts/Palatino.ttc", subfontIndex=2))
        font_reg["title"] = "Palatino-Bold"
        print("✓ Palatino fonts registered")
    except TTFError as e:
        font_reg["title"] = font_reg.get("bodyB", "Times-Bold")

    # ── DejaVuSerif for Unicode math glyphs (Greek, ∂, →, ×, ℏ, ² …) ──────────
    global _MATH_FONT
    _MPL_FONTS = "/usr/local/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf"
    # ── DejaVuSerif — Unicode math glyphs (covers most Georgia gaps) ─────────
    try:
        pdfmetrics.registerFont(TTFont("MathSerif",          f"{_MPL_FONTS}/DejaVuSerif.ttf"))
        pdfmetrics.registerFont(TTFont("MathSerif-Italic",   f"{_MPL_FONTS}/DejaVuSerif-Italic.ttf"))
        pdfmetrics.registerFont(TTFont("MathSerif-Bold",     f"{_MPL_FONTS}/DejaVuSerif-Bold.ttf"))
        pdfmetrics.registerFont(TTFont("MathSerif-BoldItalic", f"{_MPL_FONTS}/DejaVuSerif-BoldItalic.ttf"))
        pdfmetrics.registerFontFamily("MathSerif",
            normal="MathSerif", italic="MathSerif-Italic",
            bold="MathSerif-Bold", boldItalic="MathSerif-BoldItalic")
        _MATH_FONT = "MathSerif-Italic"
        font_reg["math"] = "MathSerif-Italic"
        print("✓ DejaVuSerif (MathSerif) fonts registered")
    except TTFError as e:
        print(f"  DejaVuSerif fallback: {e}")
        font_reg["math"] = "Times-Italic"

    # ── DejaVuSans — second-tier fallback for chars DejaVuSerif lacks ─────────
    try:
        pdfmetrics.registerFont(TTFont("MathSans",          f"{_MPL_FONTS}/DejaVuSans.ttf"))
        pdfmetrics.registerFont(TTFont("MathSans-Oblique",  f"{_MPL_FONTS}/DejaVuSans-Oblique.ttf"))
        pdfmetrics.registerFont(TTFont("MathSans-Bold",     f"{_MPL_FONTS}/DejaVuSans-Bold.ttf"))
        pdfmetrics.registerFont(TTFont("MathSans-BoldOblique", f"{_MPL_FONTS}/DejaVuSans-BoldOblique.ttf"))
        pdfmetrics.registerFontFamily("MathSans",
            normal="MathSans", italic="MathSans-Oblique",
            bold="MathSans-Bold", boldItalic="MathSans-BoldOblique")
        font_reg["mathsans"] = "MathSans"
        print("✓ DejaVuSans (MathSans) fonts registered")
    except TTFError as e:
        print(f"  DejaVuSans fallback: {e}")
        font_reg["mathsans"] = font_reg.get("math", "Helvetica")

    return font_reg

# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles(FR):
    S = {}
    B, BI, BB, BBI = FR["body"], FR["bodyI"], FR["bodyB"], FR["bodyBI"]
    M, MB = FR["mono"], FR["monoB"]
    T = FR["title"]

    S["body"]   = ParagraphStyle("Body", fontName=B,  fontSize=10.5, leading=15.5,
                                  spaceAfter=5, alignment=TA_JUSTIFY)
    S["h1"]     = ParagraphStyle("H1",   fontName=BB, fontSize=21, leading=26,
                                  spaceBefore=30, spaceAfter=12, textColor=C_NAVY,
                                  keepWithNext=1, alignment=TA_LEFT)
    S["h2"]     = ParagraphStyle("H2",   fontName=BB, fontSize=15, leading=20,
                                  spaceBefore=20, spaceAfter=7, textColor=C_NAVY,
                                  keepWithNext=1)
    S["h3"]     = ParagraphStyle("H3",   fontName=BB, fontSize=12.5, leading=17,
                                  spaceBefore=15, spaceAfter=5, textColor=C_SLATE,
                                  keepWithNext=1)
    S["h4"]     = ParagraphStyle("H4",   fontName=BB, fontSize=11, leading=15,
                                  spaceBefore=12, spaceAfter=4, textColor=C_SLATE,
                                  keepWithNext=1)
    S["caption"]= ParagraphStyle("Cap",  fontName=BI, fontSize=9.5, leading=13,
                                  spaceBefore=3, spaceAfter=10,
                                  leftIndent=20, rightIndent=20, textColor=C_CAPFG)
    S["bq"]     = ParagraphStyle("BQ",   fontName=BI, fontSize=10.5, leading=15,
                                  spaceBefore=5, spaceAfter=5,
                                  leftIndent=24, rightIndent=12, textColor=C_GRAY4)
    S["li"]     = ParagraphStyle("LI",   fontName=B,  fontSize=10.5, leading=15,
                                  spaceBefore=1, spaceAfter=1,
                                  leftIndent=20, firstLineIndent=-12)
    S["tbd"]    = ParagraphStyle("TBd",  fontName=B,  fontSize=9,  leading=12)
    S["tbh"]    = ParagraphStyle("TBh",  fontName=BB, fontSize=9,  leading=12,
                                  textColor=white)
    S["code"]   = ParagraphStyle("Code", fontName=M,  fontSize=7.5,leading=10.5)
    # Title page
    S["cvtitle"]= ParagraphStyle("CVT",  fontName=T,  fontSize=34, leading=42,
                                  alignment=TA_CENTER, textColor=C_NAVY, spaceAfter=18)
    S["cvsub"]  = ParagraphStyle("CVS",  fontName=BI, fontSize=18, leading=24,
                                  alignment=TA_CENTER, textColor=C_SLATE, spaceAfter=10)
    S["cvauth"] = ParagraphStyle("CVA",  fontName=B,  fontSize=13, leading=18,
                                  alignment=TA_CENTER, textColor=C_GRAY4, spaceAfter=6)
    S["cvsmall"]= ParagraphStyle("CVSm", fontName=BI, fontSize=10, leading=14,
                                  alignment=TA_CENTER, textColor=C_GRAY6)
    return S

# ── Chapter marker flowable ───────────────────────────────────────────────────
class ChapterMarker(Flowable):
    """Zero-height flowable that updates current_chapter[0] at draw time.

    Must be used instead of setting current_chapter[0] at parse time —
    parse-time assignment means the container holds the *last* chapter by
    the time any onPage callback fires, so every page header shows the
    final chapter name ("Back Matter", etc.).  Drawing happens page-by-page
    in document order, so the header is always correct.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def wrap(self, availWidth, availHeight):
        return 0, 0

    def draw(self):
        current_chapter[0] = self.name


# ── Document template with TOC hook ──────────────────────────────────────────
class GRUTDocTemplate(BaseDocTemplate):
    """BaseDocTemplate subclass that feeds headings into the TOC.

    afterFlowable is called after each flowable is placed on the page.
    Tracked entries:
      Level 0: ## Front Matter, ## Part I/II/III/IV, # Back Matter
      Level 1: ### front-matter subsections, # Chapter 1-14, # Appendix A-F
    The _in_front_matter flag activates on '## Front Matter' and clears
    on the first subsequent H2 (version-update headers) or any H1.
    """

    def __init__(self, *args, **kwargs):
        self._grut_toc = kwargs.pop('toc', None)
        self._in_front_matter = False
        super().__init__(*args, **kwargs)

    def afterFlowable(self, flowable):
        if self._grut_toc is None:
            return
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        try:
            text = flowable.getPlainText().strip()
        except Exception:
            return

        if style_name == 'H1':
            if text == 'GRUT':
                return   # skip the document-title H1 at top of markdown
            self._in_front_matter = False
            # "Back Matter" is a top-level section marker, not a numbered chapter
            level = 0 if text.startswith('Back Matter') else 1
            self._grut_toc.notify('TOCEntry', (level, text, self.page, None))
        elif style_name == 'H2':
            if text == 'Front Matter':
                # Front matter opens — emit level-0 header and arm H3 capture
                self._in_front_matter = True
                self._grut_toc.notify('TOCEntry', (0, text, self.page, None))
            elif text.startswith('Part'):
                # Part I / II / III / IV — top-level structural dividers
                self._in_front_matter = False
                self._grut_toc.notify('TOCEntry', (0, text, self.page, None))
            else:
                # Version-update headers (v8→v2, Gate R, v3 …) — end front matter
                self._in_front_matter = False
        elif style_name == 'H3':
            if self._in_front_matter:
                # Prologue, Predictions, Why Now?, Abstract
                self._grut_toc.notify('TOCEntry', (1, text, self.page, None))


# ── Page template with headers/footers ────────────────────────────────────────
current_chapter = [""]   # mutable container so onPage callbacks can update it

def header_footer(canvas, doc):
    canvas.saveState()
    pn = doc.page
    if pn > 3:
        # Header rule
        canvas.setStrokeColor(C_BORDER)
        canvas.setLineWidth(0.4)
        canvas.line(ML, PAGE_H - 0.72*inch, PAGE_W - MR, PAGE_H - 0.72*inch)
        canvas.setFont("Georgia-Italic", 8)
        canvas.setFillColor(C_GRAY6)
        chap = current_chapter[0][:72] if current_chapter[0] else ""
        # Left: chapter name
        canvas.drawString(ML, PAGE_H - 0.60*inch, chap)
        # Right: series title (constant)
        canvas.drawRightString(PAGE_W - MR, PAGE_H - 0.60*inch,
                               "Grand Responsive Universe Theory")
    # Footer: page number only (no rule)
    canvas.setFont("Georgia", 9)
    canvas.setFillColor(C_GRAY4)
    canvas.drawCentredString(PAGE_W/2, 0.28*inch, str(pn))
    canvas.restoreState()

def title_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Georgia", 9)
    canvas.setFillColor(C_GRAY6)
    canvas.drawCentredString(PAGE_W/2, 0.28*inch, str(doc.page))
    canvas.restoreState()

# ── XML helpers ───────────────────────────────────────────────────────────────
def esc(s):
    """Escape XML special characters."""
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# ── Font-fallback tables (checked against Georgia + DejaVu fonts) ─────────────
# Source: scanned GRUT_TOE_upload.md for every non-ASCII char, then tested each
# against Georgia.ttf, DejaVuSerif.ttf, DejaVuSans.ttf via pdfmetrics.
#
# Chars Georgia lacks AND DejaVuSerif lacks → need MathSans (DejaVuSans).
# Exactly 11 chars from the scan: ✓ ℋ ≪ ≫ ⚑ ∎ ≲ ≳ ① ② ③
_SANS_FALLBACK = frozenset('✓ℋ≪≫⚑∎≲≳①②③')
#
# Chars Georgia lacks BUT DejaVuSerif CAN render → use MathSerif.
# All 48 minus the 11 above = 37 chars.
_SERIF_FALLBACK = frozenset(
    '═→⁻ℏ█∝▼←┤║├○∇◻⟨⟩↔┼≡╗╚∼┬┴░◈◯⁺₊₋↑↓╔╝ℤ∈⊃'
    '⁰¹²³⁴⁵⁶⁷⁸⁹'   # remaining superscripts Georgia has missing
    '₀₁₂₃₄₅₆₇₈₉'   # subscript digits (Georgia confirmed missing some)
)
# Combined
_GEO_MISSING = _SERIF_FALLBACK | _SANS_FALLBACK

def _font_fallback(s):
    """Wrap Georgia-missing glyphs in the correct fallback font span.
    Walks already-XML-tagged markup, skipping tags and XML entities.
    DejaVuSerif (MathSerif) for most; DejaVuSans (MathSans) for the rest.
    """
    if not any(c in s for c in _GEO_MISSING):
        return s
    out = []
    i, n = 0, len(s)
    while i < n:
        c = s[i]
        if c == '<':
            j = s.find('>', i)
            end = j + 1 if j >= 0 else i + 1
            out.append(s[i:end]); i = end
        elif c == '&':
            j = s.find(';', i)
            end = j + 1 if j >= 0 else i + 1
            out.append(s[i:end]); i = end
        elif c in _GEO_MISSING:
            # Collect a run of missing chars — group by which font they need
            j = i
            font = 'MathSans' if c in _SANS_FALLBACK else 'MathSerif'
            while j < n and s[j] in _GEO_MISSING:
                # If the font bucket changes, close and reopen
                needed = 'MathSans' if s[j] in _SANS_FALLBACK else 'MathSerif'
                if needed != font:
                    break
                j += 1
            out.append(f'<font name="{font}">{s[i:j]}</font>')
            i = j
        else:
            out.append(c); i += 1
    return ''.join(out)

def inline(text):
    """Convert markdown inline markup to reportlab XML tags.
    Must operate on already-XML-escaped text except for the tag insertions.
    """
    # Escape first
    text = esc(text)

    # Bold-italic ***...***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold **...**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic *...* (not inside words)
    text = re.sub(r'(?<![a-zA-Z0-9_])\*([^*\n]+?)\*(?![a-zA-Z0-9_])', r'<i>\1</i>', text)
    # Inline code `...`
    text = re.sub(r'`([^`\n]+)`',
                  lambda m: f'<font name="Menlo" size="9" color="#444444">{esc(m.group(1))}</font>',
                  text)
    # Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)',
                  lambda m: f'<font color="{C_LINK.hexval()}">{m.group(1)}</font>',
                  text)
    # Inline math $...$ — convert LaTeX to Unicode, render in DejaVuSerif-Italic
    # so Greek letters and math symbols have proper glyphs (no square boxes)
    text = re.sub(r'(?<!\$)\$([^\$\n]+?)\$(?!\$)',
                  lambda m: (f'<font name="{_MATH_FONT}" size="10">'
                             f'{esc(latex_to_unicode(m.group(1)))}</font>'),
                  text)
    # Fallback: wrap any Georgia-missing glyphs that appear in raw body text
    text = _font_fallback(text)
    return text

# ── LaTeX → Unicode symbol map ────────────────────────────────────────────────
_LATEX_SYM = {
    # Greek lowercase
    r'\alpha':'α', r'\beta':'β', r'\gamma':'γ', r'\delta':'δ',
    r'\epsilon':'ε', r'\varepsilon':'ε', r'\zeta':'ζ', r'\eta':'η',
    r'\theta':'θ', r'\vartheta':'θ', r'\iota':'ι', r'\kappa':'κ',
    r'\lambda':'λ', r'\mu':'μ', r'\nu':'ν', r'\xi':'ξ',
    r'\pi':'π', r'\rho':'ρ', r'\sigma':'σ', r'\tau':'τ',
    r'\upsilon':'υ', r'\phi':'φ', r'\varphi':'φ', r'\chi':'χ',
    r'\psi':'ψ', r'\omega':'ω',
    # Greek uppercase
    r'\Gamma':'Γ', r'\Delta':'Δ', r'\Theta':'Θ', r'\Lambda':'Λ',
    r'\Xi':'Ξ', r'\Pi':'Π', r'\Sigma':'Σ', r'\Upsilon':'Υ',
    r'\Phi':'Φ', r'\Psi':'Ψ', r'\Omega':'Ω',
    # Operators / relations
    r'\times':'×', r'\cdot':'·', r'\pm':'±', r'\mp':'∓',
    r'\leq':'≤', r'\geq':'≥', r'\neq':'≠', r'\approx':'≈',
    r'\equiv':'≡', r'\propto':'∝', r'\sim':'∼', r'\simeq':'≃',
    r'\ll':'≪', r'\gg':'≫',
    r'\subset':'⊂', r'\supset':'⊃', r'\in':'∈', r'\notin':'∉',
    r'\cup':'∪', r'\cap':'∩',
    # Arrows
    r'\longrightarrow':'⟶', r'\rightarrow':'→', r'\leftarrow':'←',
    r'\Rightarrow':'⇒', r'\Leftarrow':'⇐', r'\leftrightarrow':'↔',
    r'\longleftarrow':'⟵', r'\Longrightarrow':'⟹',
    r'\to':'→', r'\mapsto':'↦', r'\implies':'⟹',
    # Misc math
    r'\infty':'∞', r'\partial':'∂', r'\nabla':'∇', r'\hbar':'ℏ',
    r'\ell':'ℓ', r'\forall':'∀', r'\exists':'∃', r'\emptyset':'∅',
    r'\int':'∫', r'\oint':'∮', r'\sum':'∑', r'\prod':'∏',
    r'\langle':'⟨', r'\rangle':'⟩',
    # Spacing (strip or replace with space)
    r'\quad':' ', r'\qquad':'  ', r'\,':'', r'\;':' ',
    r'\!':'', r'\:':' ', r'\ ':' ',
}

def latex_to_unicode(s):
    """Convert inline LaTeX math expression to readable Unicode text."""
    # Apply symbol map (longest first to avoid partial matches)
    for cmd, sym in sorted(_LATEX_SYM.items(), key=lambda x: -len(x[0])):
        s = s.replace(cmd, sym)
    # \frac{a}{b} → (a)/(b)  — handle up to two levels of nesting
    for _ in range(3):
        s = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', r'(\1)/(\2)', s)
    # \sqrt{x} → √(x)
    s = re.sub(r'\\sqrt\{([^{}]*)\}', r'√(\1)', s)
    s = re.sub(r'\\sqrt\s+(\S)', r'√\1', s)
    # Superscripts: ^{...} → use Unicode digits/letters where possible
    _sup = str.maketrans('0123456789+-n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ')
    def _sup_repl(m):
        t = m.group(1)
        return t.translate(_sup) if all(c in '0123456789+-n' for c in t) else f'^({t})'
    s = re.sub(r'\^\{([^{}]+)\}', _sup_repl, s)
    s = re.sub(r'\^([0-9])', lambda m: m.group(1).translate(_sup), s)
    # Subscripts: _{...} — keep as _(...) for readability
    s = re.sub(r'_\{([^{}]+)\}', r'_(\1)', s)
    # Strip font/style commands but keep their argument
    for cmd in (r'\mathrm', r'\mathbf', r'\mathit', r'\mathcal', r'\mathbb',
                r'\text', r'\rm', r'\bf', r'\operatorname', r'\hat',
                r'\vec', r'\bar', r'\tilde', r'\dot', r'\ddot',
                r'\left', r'\right', r'\big', r'\Big', r'\bigg',
                r'\overline', r'\underline', r'\widehat'):
        s = s.replace(cmd, '')
    # Remove remaining backslash commands
    s = re.sub(r'\\[a-zA-Z]+\*?', '', s)
    # Remove stray braces
    s = s.replace('{', '').replace('}', '')
    return s.strip()

# ── matplotlib equation image renderer ────────────────────────────────────────
_mpl_ready = [False]

def _ensure_mpl():
    if not _mpl_ready[0]:
        import matplotlib
        matplotlib.use('Agg')
        _mpl_ready[0] = True
    import matplotlib.pyplot as plt
    return plt

def _strip_wrapper(s, cmd):
    """Replace \\cmd{...} with just the inner content (handles one level of nesting)."""
    tag = cmd + '{'
    result = []
    i = 0
    while i < len(s):
        if s[i:i+len(tag)] == tag:
            depth = 1; j = i + len(tag)
            while j < len(s) and depth:
                if s[j] == '{': depth += 1
                elif s[j] == '}': depth -= 1
                j += 1
            result.append(s[i+len(tag):j-1])   # content only, no braces
            i = j
        else:
            result.append(s[i]); i += 1
    return ''.join(result)

def _remove_command(s, cmd):
    """Remove \\cmd{...} entirely (handles one level of nesting)."""
    tag = cmd + '{'
    result = []
    i = 0
    while i < len(s):
        if s[i:i+len(tag)] == tag:
            depth = 1; j = i + len(tag)
            while j < len(s) and depth:
                if s[j] == '{': depth += 1
                elif s[j] == '}': depth -= 1
                j += 1
            i = j   # skip entire \cmd{...}
        else:
            result.append(s[i]); i += 1
    return ''.join(result)

def _latex_preprocess(s):
    """Fix LaTeX commands unsupported by matplotlib mathtext."""
    s = re.sub(r'\\text\{',         r'\\mathrm{', s)
    s = re.sub(r'\\operatorname\{', r'\\mathrm{', s)
    s = re.sub(r'\\mathbb\{',       r'\\mathrm{', s)
    s = s.replace(r'\longrightarrow', r'\rightarrow')
    s = s.replace(r'\longleftarrow',  r'\leftarrow')
    s = s.replace(r'\Longrightarrow', r'\Rightarrow')
    s = re.sub(r'\\nonumber', '', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    # Remove alignment characters (&, \\)
    s = re.sub(r'(?<!\\)\\\\', ' ', s)   # \\ line-break → space
    s = s.replace('&', '')
    # Matplotlib mathtext can't combine ' (prime) with a subscript on the same
    # symbol — convert x'_n to x^{\prime}_n so the parser sees them separately.
    s = re.sub(r"'_", r"^{\\prime}_", s)
    # \bigl / \bigr are size hints — map to \left / \right which mathtext knows
    s = s.replace(r'\bigl', r'\left')
    s = s.replace(r'\bigr', r'\right')
    s = s.replace(r'\Bigl', r'\left')
    s = s.replace(r'\Bigr', r'\right')
    # \bigg / \Bigg size hints — strip prefix, leave the delimiter
    s = re.sub(r'\\[Bb]igg([([{])',  r'\\left\1',  s)
    s = re.sub(r'\\[Bb]igg([)\]}])', r'\\right\1', s)
    s = re.sub(r'\\[Bb]igg\|',       r'|',          s)
    # Spacing commands mathtext ignores or chokes on
    s = s.replace(r'\!', '')    # negative thin space
    s = s.replace(r'\;', r'\ ') # thick space → normal space
    # \tfrac → \frac  (matplotlib mathtext doesn't know \tfrac)
    s = s.replace(r'\tfrac', r'\frac')
    # \boxed{...} → content only  (matplotlib doesn't support \boxed)
    s = _strip_wrapper(s, r'\boxed')
    # \tag{...} → remove entirely
    s = _remove_command(s, r'\tag')
    return s

def _render_eq_image(latex, fontsize=13, dpi=150):
    """Render LaTeX string via matplotlib. Returns (BytesIO, w_pt, h_pt) or None."""
    s = _latex_preprocess(latex)
    expr = f'${s}$'
    try:
        plt = _ensure_mpl()
        fig = plt.figure(figsize=(0.1, 0.1))
        fig.patch.set_alpha(0)
        fig.text(0.5, 0.5, expr, fontsize=fontsize,
                 ha='center', va='center', usetex=False)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=dpi,
                    transparent=True, pad_inches=0.08)
        plt.close(fig)
        buf.seek(0)
        from PIL import Image as _PILImg
        iw, ih = _PILImg.open(buf).size
        buf.seek(0)
        return buf, iw / dpi * 72, ih / dpi * 72   # px → pt
    except Exception:
        return None

def render_display_eq(latex, flowables, S):
    """Render a display equation: tries matplotlib image, falls back to styled text."""
    from reportlab.platypus import Image as _RLImg
    result = _render_eq_image(latex)
    if result:
        buf, w_pt, h_pt = result
        if w_pt > CONTENT_W:
            scale = CONTENT_W / w_pt
            w_pt *= scale; h_pt *= scale
        img = _RLImg(buf, width=w_pt, height=h_pt)
        centering = Table([[img]], colWidths=[CONTENT_W],
                          style=TableStyle([
                              ('ALIGN',         (0,0),(-1,-1),'CENTER'),
                              ('TOPPADDING',    (0,0),(-1,-1), 2),
                              ('BOTTOMPADDING', (0,0),(-1,-1), 2),
                          ]))
        flowables.append(Spacer(1, 10))
        flowables.append(centering)
        flowables.append(Spacer(1, 10))
    else:
        # Fallback: styled code-like block
        mstyle = ParagraphStyle("MathDisp",
            fontName=S["code"].fontName, fontSize=9.5, leading=14,
            textColor=C_NAVY)
        pre = Preformatted(latex.strip(), mstyle)
        wrapper = Table([[pre]], colWidths=[CONTENT_W])
        wrapper.setStyle(TableStyle([
            ('BACKGROUND',    (0,0),(-1,-1), C_MATHBG),
            ('BOX',           (0,0),(-1,-1), 0.5, HexColor("#a0b0cc")),
            ('LEFTPADDING',   (0,0),(-1,-1), 14),
            ('RIGHTPADDING',  (0,0),(-1,-1), 14),
            ('TOPPADDING',    (0,0),(-1,-1), 10),
            ('BOTTOMPADDING', (0,0),(-1,-1), 10),
        ]))
        flowables.append(Spacer(1, 6))
        flowables.append(wrapper)
        flowables.append(Spacer(1, 6))

# ── Table renderer ────────────────────────────────────────────────────────────
def render_table(rows, alignments, S, flowables):
    if not rows:
        return
    hdr = rows[0]
    body = rows[1:] if len(rows) > 1 else []
    ncols = max(len(r) for r in rows) if rows else len(hdr)
    if ncols == 0:
        return

    # Font size scaled to column count to prevent overflow
    if ncols <= 2:
        fsize, leading = 9.5, 13.5
    elif ncols == 3:
        fsize, leading = 9.0, 13.0
    elif ncols == 4:
        fsize, leading = 8.5, 12.5
    else:                             # 5+ columns
        fsize, leading = 7.5, 11.0

    # Proportional column widths based on max content length in each column
    max_lens = []
    for ci in range(ncols):
        col_max = max((len(r[ci]) for r in rows if ci < len(r)), default=4)
        max_lens.append(max(col_max, 4))
    total_len = sum(max_lens) or 1
    MIN_F, MAX_F = 0.05, 0.45
    fracs = [max(MIN_F, min(MAX_F, v / total_len)) for v in max_lens]
    s = sum(fracs)
    col_widths = [CONTENT_W * f / s for f in fracs]

    # Enforce minimum column width to prevent extreme wrapping in narrow columns
    MIN_COL_W = 55.0   # pt — narrower than this causes too many wrapped lines
    if any(w < MIN_COL_W for w in col_widths):
        col_widths = [max(w, MIN_COL_W) for w in col_widths]
        # Renormalise to fit CONTENT_W
        total_w = sum(col_widths)
        if total_w > CONTENT_W:
            col_widths = [w * CONTENT_W / total_w for w in col_widths]

    # MAX_CELL: safety cap only — Paragraph wraps naturally at column width,
    # so this only exists to catch truly pathological single-cell content.
    # Previous values (250/380/550) were too small and truncated real content.
    MAX_CELL = 4000

    tbh_s = ParagraphStyle("_TBHx", fontName=S["tbh"].fontName,
                            fontSize=fsize, leading=leading, textColor=white)
    tbd_s = ParagraphStyle("_TBDx", fontName=S["tbd"].fontName,
                            fontSize=fsize, leading=leading)

    # Debug: print layout for tables with narrow columns
    min_w = min(col_widths)
    if min_w < 60 or ncols >= 5:
        print(f"  [TABLE] {ncols} cols, rows={len(rows)}, "
              f"min_col={min_w:.1f}pt, widths={[round(w,1) for w in col_widths]}, "
              f"MAX_CELL={MAX_CELL}, header={[str(c)[:20] for c in hdr[:3]]}")

    def cell(txt, style):
        txt = txt.strip()
        if len(txt) > MAX_CELL:
            txt = txt[:MAX_CELL] + "…"
        txt = re.sub(r'\*\*(.+?)\*\*', r'\1', txt)   # strip bold in cells
        try:
            return Paragraph(inline(txt), style)
        except Exception:
            return Paragraph(esc(txt[:200]), style)

    # Detect tables whose "header row" is actually a data row (first cell is a
    # plain integer like "28" or "33").  These are numbered-item tables that
    # lack a proper column-header row in the markdown source.  Rendering them
    # with a navy header would paint a data row dark blue.
    first_cell_text = hdr[0].strip() if hdr else ""
    has_real_header = not bool(re.match(r'^\d+$', first_cell_text))

    if has_real_header:
        tdata = [[cell(c, tbh_s) for c in (list(hdr) + [''] * ncols)[:ncols]]]
        for r in body:
            tdata.append([cell(c, tbd_s) for c in (list(r) + [''] * ncols)[:ncols]])
        ts = [
            ('BACKGROUND',    (0,0), (-1,0),  C_TBLHD),
            ('TEXTCOLOR',     (0,0), (-1,0),  white),
            ('ROWBACKGROUNDS',(0,1), (-1,-1), [white, C_TBLALT]),
        ]
    else:
        # No real header — render all rows as data rows with alternating shading
        tdata = []
        for r in rows:
            tdata.append([cell(c, tbd_s) for c in (list(r) + [''] * ncols)[:ncols]])
        ts = [
            ('ROWBACKGROUNDS',(0,0), (-1,-1), [white, C_TBLALT]),
        ]

    ts += [
        ('GRID',          (0,0), (-1,-1), 0.4, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 5),
        ('RIGHTPADDING',  (0,0), (-1,-1), 5),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]
    for i, al in enumerate((alignments or [])[:ncols]):
        ts.append(('ALIGN', (i,0),(i,-1), al))

    if ncols > 7:
        print(f"  [WIDE TABLE] {ncols} cols, rows={len(rows)}, header={hdr[:3]}")
    t = Table(tdata, colWidths=col_widths, repeatRows=1, splitByRow=True)
    t.setStyle(TableStyle(ts))
    flowables.append(Spacer(1, 6))
    flowables.append(t)
    flowables.append(Spacer(1, 8))

# ── Code block renderer ───────────────────────────────────────────────────────
def render_code(code_lines, flowables, S):
    text = '\n'.join(code_lines)
    pre = Preformatted(text, S["code"])
    wrapper = Table([[pre]], colWidths=[CONTENT_W])
    wrapper.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_CODEBG),
        ('BOX',        (0,0), (-1,-1), 0.5, C_BORDER),
        ('LEFTPADDING',(0,0), (-1,-1), 10),
        ('RIGHTPADDING',(0,0),(-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING',(0,0),(-1,-1), 8),
    ]))
    flowables.append(Spacer(1, 4))
    flowables.append(wrapper)
    flowables.append(Spacer(1, 4))

# ── Math block renderer (multi-line $$ fence) ─────────────────────────────────
def render_math(math_lines, flowables, S):
    # Join multi-line blocks and render as a single display equation
    latex = ' '.join(l.strip() for l in math_lines if l.strip())
    render_display_eq(latex, flowables, S)

# ── Main markdown parser / renderer ───────────────────────────────────────────
def parse_md(text, S):
    lines = text.split('\n')
    out = []
    i = 0
    in_code = False;  code_buf = []; code_lang = ''
    in_math = False;  math_buf = []
    in_table = False; tbl_rows = []; tbl_aligns = []; tbl_ncols = None
    in_list = False;  list_buf = []
    first_h1_seen = False

    def flush_table():
        nonlocal in_table, tbl_rows, tbl_aligns, tbl_ncols
        if tbl_rows:
            render_table(tbl_rows, tbl_aligns, S, out)
        in_table = False; tbl_rows = []; tbl_aligns = []; tbl_ncols = None

    def flush_list():
        nonlocal in_list, list_buf
        for item in list_buf:
            try:
                p = Paragraph('• ' + inline(item), S["li"])
            except Exception:
                p = Paragraph('• ' + esc(item), S["li"])
            out.append(p)
        list_buf = []; in_list = False

    while i < len(lines):
        line = lines[i]

        # ── Code fence ────────────────────────────────────────────────────────
        if line.strip().startswith('```'):
            if not in_code:
                flush_list(); flush_table()
                in_code = True
                code_lang = line.strip()[3:].strip()
                code_buf = []
            else:
                in_code = False
                # Check if this is an ASCII-art figure stub (first content line = '┌')
                first_content = next((l for l in code_buf if l.strip()), '')
                is_fig_stub   = first_content.strip().startswith('┌')
                embedded = False
                if is_fig_stub:
                    # Peek past blank lines for "*(Figure N: to be rendered...)*"
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    peek = lines[j].strip() if j < len(lines) else ''
                    fig_m = re.match(r'^\*\(Figure\s+(\d+):', peek)
                    if fig_m:
                        fig_num  = int(fig_m.group(1))
                        png_name = _FIGURE_PNGS.get(fig_num, '')
                        png_path = FIGURES_DIR / png_name
                        if png_name and png_path.exists():
                            # Run make_figures.py first if the PNG is stale or missing
                            from reportlab.platypus import Image as _RLImg
                            try:
                                # Measure natural size then scale to CONTENT_W
                                from PIL import Image as _PILImg
                                with _PILImg.open(png_path) as im:
                                    iw, ih = im.size
                                scale   = min(1.0, CONTENT_W / (iw * 72 / 200))
                                w_pt    = iw * 72 / 200 * scale
                                h_pt    = ih * 72 / 200 * scale
                                img = _RLImg(str(png_path), width=w_pt, height=h_pt)
                                centering = Table([[img]], colWidths=[CONTENT_W],
                                    style=TableStyle([
                                        ('ALIGN',  (0,0),(-1,-1),'CENTER'),
                                        ('TOPPADDING',    (0,0),(-1,-1), 6),
                                        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
                                    ]))
                                out.append(Spacer(1, 8))
                                out.append(centering)
                                out.append(Spacer(1, 4))
                                embedded = True
                                # Skip the "to be rendered" line (and any blank before it)
                                i = j + 1
                            except Exception as emb_err:
                                print(f"  Warning: could not embed fig {fig_num}: {emb_err}")
                if not embedded:
                    render_code(code_buf, out, S)
                    # If it was a fig stub but we couldn't embed, still skip "to be rendered"
                    if is_fig_stub:
                        j = i + 1
                        while j < len(lines) and not lines[j].strip():
                            j += 1
                        peek = lines[j].strip() if j < len(lines) else ''
                        if re.match(r'^\*\(Figure\s+\d+:', peek):
                            i = j + 1
                        else:
                            i += 1
                    else:
                        i += 1
                code_buf = []
                continue
            i += 1; continue
        if in_code:
            code_buf.append(line); i += 1; continue

        # ── Single-line display equation $$...$$ ─────────────────────────────
        stripped_pre = line.strip()
        if (stripped_pre.startswith('$$') and stripped_pre.endswith('$$')
                and len(stripped_pre) > 4):
            flush_list(); flush_table()
            latex = stripped_pre[2:-2].strip()
            render_display_eq(latex, out, S)
            i += 1; continue

        # ── Math fence $$ ─────────────────────────────────────────────────────
        if line.strip() == '$$':
            if not in_math:
                flush_list(); flush_table()
                in_math = True; math_buf = []
            else:
                in_math = False
                render_math(math_buf, out, S)
                math_buf = []
            i += 1; continue
        if in_math:
            math_buf.append(line); i += 1; continue

        # ── Page break div ────────────────────────────────────────────────────
        if 'page-break-before: always' in line:
            flush_list(); flush_table()
            out.append(PageBreak()); i += 1; continue

        # ── Skip HTML comments/divs ───────────────────────────────────────────
        stripped = line.strip()
        if stripped.startswith('<!--') or (stripped.startswith('<div') and 'page-break' not in stripped):
            i += 1; continue

        # ── Table row ─────────────────────────────────────────────────────────
        if stripped.startswith('|') and '|' in stripped[1:]:
            flush_list()
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            is_sep = all(re.match(r'^:?-{2,}:?$', c.strip()) for c in cells if c.strip())
            if is_sep:
                # Separator — record expected column count and alignment
                tbl_ncols = len(cells)
                aligns = []
                for c in cells:
                    c = c.strip()
                    if c.startswith(':') and c.endswith(':'):
                        aligns.append('CENTER')
                    elif c.endswith(':'):
                        aligns.append('RIGHT')
                    else:
                        aligns.append('LEFT')
                tbl_aligns = aligns
            else:
                in_table = True
                # Clamp rows with extra pipe chars in cell content back to expected width
                if tbl_ncols is None:
                    tbl_ncols = len(cells)   # first data row sets width
                if len(cells) > tbl_ncols:
                    merged = cells[:tbl_ncols - 1]
                    merged.append(' | '.join(cells[tbl_ncols - 1:]))
                    cells = merged
                tbl_rows.append(cells)
            i += 1; continue
        elif in_table:
            flush_table()

        # ── Horizontal rule ───────────────────────────────────────────────────
        if re.match(r'^-{3,}\s*$', stripped) or re.match(r'^\*{3,}\s*$', stripped):
            flush_list(); flush_table()
            out.append(HRFlowable(width="100%", thickness=0.5,
                                  color=C_HR, spaceBefore=8, spaceAfter=8))
            i += 1; continue

        # ── Headings ──────────────────────────────────────────────────────────
        hm = re.match(r'^(#{1,4})\s+(.*)', line)
        if hm:
            flush_list(); flush_table()
            lvl = len(hm.group(1))
            htxt = hm.group(2).strip()
            # Strip trailing #
            htxt = re.sub(r'\s+#+\s*$', '', htxt)
            # Chapter H1: page break comes from the CSS div in the markdown source.
            # We do NOT add a second PageBreak here — that caused blank pages.
            # Use ChapterMarker so the header updates at draw time (not parse time).
            if lvl == 1:
                first_h1_seen = True
                chap_name = re.sub(r'\*\*(.+?)\*\*', r'\1', htxt)[:60]
                out.append(ChapterMarker(chap_name))
            sk = f'h{min(lvl,4)}'
            try:
                p = Paragraph(inline(htxt), S[sk])
            except Exception:
                p = Paragraph(esc(htxt), S[sk])
            out.append(p)
            i += 1; continue

        # ── List item ─────────────────────────────────────────────────────────
        lm = re.match(r'^(\s{0,3})[-*+]\s+(.*)', line)
        nm = re.match(r'^(\s{0,3})\d+\.\s+(.*)', line)
        if lm or nm:
            m = lm or nm
            in_list = True
            list_buf.append(m.group(2))
            i += 1; continue
        elif in_list:
            # Continuation indent?
            if line.startswith('  ') and line.strip():
                list_buf[-1] += ' ' + line.strip()
                i += 1; continue
            flush_list()

        # ── Block quote ───────────────────────────────────────────────────────
        bqm = re.match(r'^>\s*(.*)', line)
        if bqm:
            try:
                p = Paragraph(inline(bqm.group(1)), S["bq"])
            except Exception:
                p = Paragraph(esc(bqm.group(1)), S["bq"])
            out.append(p); i += 1; continue

        # ── Figure caption (italic paragraph starting with *Figure) ───────────
        if re.match(r'^\*Figure\s+\d+', stripped):
            cap = stripped.strip('*')
            try:
                p = Paragraph(inline(cap), S["caption"])
            except Exception:
                p = Paragraph(esc(cap), S["caption"])
            out.append(p); i += 1; continue

        # ── Empty line ────────────────────────────────────────────────────────
        if not stripped:
            i += 1; continue

        # ── Paragraph: collect continuation lines ─────────────────────────────
        para = [line]
        j = i + 1
        while j < len(lines):
            nl = lines[j]
            nls = nl.strip()
            if not nls: break
            if re.match(r'^#{1,4}\s', nl): break
            if nls.startswith('|') and '|' in nls[1:]: break
            if nls.startswith('```'): break
            if nls == '$$': break
            if re.match(r'^[-*+]\s', nls) or re.match(r'^\d+\.\s', nls): break
            if re.match(r'^-{3,}\s*$', nls): break
            if 'page-break-before' in nl: break
            if nls.startswith('<!--'): break
            if re.match(r'^\*Figure\s+\d+', nls): break
            if re.match(r'^>\s', nl): break
            para.append(nl)
            j += 1

        ptxt = ' '.join(para)
        # Don't merge lines that already look like structured content
        try:
            p = Paragraph(inline(ptxt), S["body"])
        except Exception:
            # Strip all markup and try plain
            clean = re.sub(r'\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`[^`]+`', '', ptxt)
            try:
                p = Paragraph(esc(clean), S["body"])
            except Exception:
                p = Paragraph("(content omitted — markup parse error)", S["body"])
        out.append(p)
        i = j

    flush_list()
    flush_table()
    return out

# ── Cover page ────────────────────────────────────────────────────────────────
def cover_page(S):
    els = []
    els.append(Spacer(1, 1.5*inch))
    els.append(Paragraph("Grand Responsive Universe Theory", S["cvtitle"]))
    els.append(Spacer(1, 0.1*inch))
    els.append(HRFlowable(width="60%", thickness=1.5, color=C_NAVY,
                          hAlign='CENTER', spaceBefore=4, spaceAfter=16))
    els.append(Paragraph(
        "A Complete Candidate Theory of Everything<br/>"
        "from a Viscoelastic Gravitational Medium with Finite Bandwidth",
        S["cvsub"]))
    els.append(Spacer(1, 0.6*inch))
    els.append(Paragraph("Ryan Grover", S["cvauth"]))
    els.append(Spacer(1, 0.15*inch))
    els.append(Paragraph("June 2026  ·  Version 2.5", S["cvauth"]))
    els.append(Spacer(1, 0.8*inch))
    els.append(HRFlowable(width="40%", thickness=0.5, color=C_BORDER,
                          hAlign='CENTER', spaceBefore=4, spaceAfter=16))
    els.append(Paragraph(
        "GRUT-RAI Codebase: DOI 10.5281/zenodo.18993689<br/>"
        "2,951 tests · 113 registered claims · 37 corrections documented",
        S["cvsmall"]))
    els.append(Spacer(1, 0.2*inch))
    els.append(Paragraph(
        "Every claim traces to a tested function.<br/>"
        "Every failure, retraction, and honest negative is documented.<br/>"
        "Nothing is fitted away.",
        S["cvsmall"]))
    els.append(PageBreak())
    return els

# ── TOC page ──────────────────────────────────────────────────────────────────
def make_toc_page(S, toc):
    """Returns flowables for a Table of Contents page (heading + TOC + page break).
    Uses the Cover page template (title_footer only) so no running chapter header
    appears on the TOC page itself.
    """
    els = []
    els.append(Spacer(1, 0.5 * inch))
    toc_title_style = ParagraphStyle('TOCTitle',
        fontName=S["h1"].fontName, fontSize=18, leading=24,
        textColor=C_NAVY, spaceAfter=16, alignment=TA_LEFT)
    els.append(Paragraph("Table of Contents", toc_title_style))
    els.append(HRFlowable(width="100%", thickness=0.5, color=C_BORDER,
                          spaceBefore=0, spaceAfter=16))
    els.append(toc)
    els.append(PageBreak())
    return els


# ── Build document ─────────────────────────────────────────────────────────────
def build(md_path, out_path):
    print(f"Reading {md_path} …")
    text = md_path.read_text(encoding='utf-8')
    print(f"  {len(text.splitlines())} lines")

    FR = register_fonts()
    S  = make_styles(FR)

    # ── Table of Contents ─────────────────────────────────────────────────────
    B, BB = FR["body"], FR["bodyB"]
    toc = TableOfContents()
    toc.levelStyles = [
        # Level 0: Part dividers + Back Matter — navy bold, no indent
        ParagraphStyle('TOC0', fontName=BB, fontSize=11, leading=16,
                       textColor=C_NAVY, spaceBefore=10, spaceAfter=2),
        # Level 1: Chapters + Appendices — slate, indented 22pt
        ParagraphStyle('TOC1', fontName=B, fontSize=10.5, leading=15,
                       textColor=C_SLATE, leftIndent=22, spaceBefore=2, spaceAfter=2),
    ]

    doc = GRUTDocTemplate(
        str(out_path),
        toc=toc,
        pagesize=letter,
        leftMargin=ML, rightMargin=MR,
        topMargin=MT, bottomMargin=MB,
        title="Grand Responsive Universe Theory",
        author="Ryan Grover",
        subject="Candidate Theory of Everything — GRUT v2.5",
        creator="GRUT PDF Generator (reportlab)",
    )

    content_frame = Frame(ML, MB, CONTENT_W, PAGE_H - MT - MB,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0,
                          id='normal', showBoundary=0)
    title_frame   = Frame(ML, MB, CONTENT_W, PAGE_H - 0.75*inch - MB,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0,
                          id='title',  showBoundary=0)

    doc.addPageTemplates([
        PageTemplate(id='Cover',  frames=[title_frame],   onPage=title_footer),
        PageTemplate(id='Normal', frames=[content_frame], onPage=header_footer),
    ])

    print("Parsing markdown …")
    story = []
    # Page 1: cover (Cover template, title_footer only)
    story += cover_page(S)
    # Page 2: table of contents (still Cover template — no running chapter header)
    story += make_toc_page(S, toc)
    # Page 3+: body (Normal template with header/footer)
    from reportlab.platypus import NextPageTemplate
    story.append(NextPageTemplate('Normal'))

    # Parse and add body
    body_flowables = parse_md(text, S)
    story += body_flowables

    print(f"  {len(story)} flowables generated")
    print(f"Building PDF → {out_path} …")
    # multiBuild runs 2-3 passes so TOC page numbers converge
    doc.multiBuild(story)
    print(f"✓ Done.  Output: {out_path}")
    size_mb = out_path.stat().st_size / 1024**2
    print(f"  File size: {size_mb:.1f} MB")

if __name__ == "__main__":
    build(INPUT_MD, OUTPUT_PDF)
