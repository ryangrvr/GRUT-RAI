#!/usr/bin/env python3.12
"""
make_figures_v4.py — figure set for GRUT ToE v4, "The Emergence of Everything"
Reader Edition (author: D. Ryan Grover).

Produces three print-ready PNGs into figures_v4/:
  fig1_emergence_ladder.png  — the signature emergence ladder (Q -> ... -> reflexive close)
  fig2_abc_boundary.png      — the Category A / B / C decisive-test boundary scorecard
  fig3_tier_legend.png       — the five-tier boundary legend as a visual key

All content is faithful to theory/GRUT_V4_SPINE.md and the banked docs. Nothing is
invented or inflated; tiers and verdicts are taken verbatim from the spine.

Run with the pdf_venv interpreter:
  uploads/pdf_venv/bin/python3.12 uploads/make_figures_v4.py
"""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.lines import Line2D

# ----------------------------------------------------------------------------- #
# Shared professional palette + style
# ----------------------------------------------------------------------------- #
HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "figures_v4")
os.makedirs(OUTDIR, exist_ok=True)

DPI = 200

# Tier palette (canonical, consistent across all three figures)
C_DERIVED     = "#2e7d4f"   # green  — DERIVED
C_HOSTED      = "#2f6fb0"   # blue   — HOSTED (received boundary condition)
C_HOSTED_AMB  = "#c98a1e"   # amber  — HOSTED matter-content seam accent (Category B)
C_FORBIDDEN   = "#b23b3b"   # red    — FORBIDDEN-BY-THEOREM
C_OPEN        = "#7a8189"   # gray   — OPEN
C_CONJECTURAL = "#7a52a8"   # violet — CONJECTURAL

# Neutrals
INK      = "#1c2330"   # primary text
SUBINK   = "#566072"   # secondary text
PANEL    = "#f4f6f8"   # light panel fill
PANEL_ED = "#d6dbe2"   # panel edge
PAGE     = "#ffffff"   # page background
RULE     = "#c2c9d2"   # thin rules

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": INK,
    "figure.facecolor": PAGE,
    "savefig.facecolor": PAGE,
})


def _tint(hex_color, frac=0.86):
    """Lighten a hex color toward white by `frac` (0=color, 1=white)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    r = int(r + (255 - r) * frac)
    g = int(g + (255 - g) * frac)
    b = int(b + (255 - b) * frac)
    return f"#{r:02x}{g:02x}{b:02x}"


def _footer(ax, text, size=6.8):
    ax.text(0.5, 0.012, text, transform=ax.figure.transFigure,
            ha="center", va="bottom", fontsize=size, color=SUBINK, style="italic")


# ============================================================================= #
# FIGURE 1 — The emergence ladder (signature visual)
# ============================================================================= #
def fig1_emergence_ladder():
    # Rungs: (name, one-word gloss) — bottom (floor) to top.
    rungs = [
        ("Q",               "arrow"),       # the in-in causal arrow
        ("F(t)",            "substrate"),   # the pre-responsive KMS bath
        ("Responsiveness",  "memory"),      # the emergence event
        ("Vacuum",          "medium"),      # the responsive vacuum
        ("Physics",         "law"),         # sectors as regimes of one law
        ("Complexity",      "structure"),   # stars, life, mind
        ("Observation",     "reflection"),  # observers = crystallized medium
    ]
    n = len(rungs)

    fig, ax = plt.subplots(figsize=(6.8, 9.4))
    ax.set_xlim(-1.1, 10)
    ax.set_ylim(0, 12.6)
    ax.axis("off")

    # Title block
    ax.text(5.6, 12.30, "The Emergence Ladder",
            ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(5.6, 11.88, "the universe's own order of emergence",
            ha="center", va="center", fontsize=9.5, color=SUBINK, style="italic")

    # Geometry: ascending stepped flow (boxes carry name + centered gloss line)
    box_w, box_h = 4.2, 1.02
    x_left, x_step = 2.0, 0.46
    y0, dy = 0.85, 1.42

    # color ramp: floor (derived/foundational) -> warm reflective top
    ramp = [C_DERIVED, C_DERIVED, C_DERIVED, C_HOSTED, C_HOSTED,
            C_CONJECTURAL, C_CONJECTURAL]

    centers = []
    for i, (name, gloss) in enumerate(rungs):
        x = x_left + i * x_step
        y = y0 + i * dy
        col = ramp[i]
        face = _tint(col, 0.84)
        box = FancyBboxPatch((x, y), box_w, box_h,
                             boxstyle="round,pad=0.02,rounding_size=0.14",
                             linewidth=1.7, edgecolor=col, facecolor=face,
                             mutation_aspect=1.0, zorder=3)
        ax.add_patch(box)
        cx = x + box_w / 2
        centers.append((cx, y + box_h, y))  # center-x, top-y, bottom-y

        ax.text(cx, y + box_h * 0.62, name, ha="center", va="center",
                fontsize=14.0, fontweight="bold", color=INK, zorder=4)
        ax.text(cx, y + box_h * 0.26, gloss, ha="center", va="center",
                fontsize=9.5, color=col, style="italic", zorder=4)

    # Ascending arrows between consecutive rungs
    for i in range(n - 1):
        cx0, top0, _ = centers[i]
        cx1, _, bot1 = centers[i + 1]
        arr = FancyArrowPatch((cx0, top0 + 0.02), (cx1, bot1 - 0.02),
                              arrowstyle="-|>", mutation_scale=16,
                              linewidth=1.9, color=INK, zorder=2,
                              shrinkA=0, shrinkB=0)
        ax.add_patch(arr)

    y_top_center = y0 + (n - 1) * dy + box_h / 2
    y_bot_center = y0 + box_h / 2
    cx_top = centers[-1][0]
    cx_bot = centers[0][0]

    # Reflexive return arrow: from the top rung's left edge, curving down the
    # left margin back to the floor (Q) — the universe turns back on itself.
    reflex = FancyArrowPatch(
        (cx_top - box_w / 2 - 0.05, y_top_center),
        (cx_bot - box_w / 2 - 0.05, y_bot_center),
        connectionstyle="arc3,rad=0.42",
        arrowstyle="-|>", mutation_scale=18, linewidth=2.0,
        color=C_CONJECTURAL, linestyle=(0, (6, 4)), zorder=2,
        shrinkA=8, shrinkB=8)
    ax.add_patch(reflex)
    ax.text(-0.55, (y_top_center + y_bot_center) / 2,
            "The universe turns back\nto study what it is made of",
            ha="center", va="center", fontsize=8.4, color=C_CONJECTURAL,
            style="italic", rotation=90, linespacing=2.6, zorder=4)

    # Reflexive-close banner — sits in the clear band between subtitle and top rung
    top_y = y0 + (n - 1) * dy + box_h
    ax.text(cx_top, top_y + 0.62,
            "→  the universe discovers responsiveness",
            ha="center", va="center", fontsize=11.0, fontweight="bold",
            color=C_CONJECTURAL, zorder=4)

    _footer(ax, "GRUT ToE v4 — The Emergence of Everything  |  D. Ryan Grover  |  "
                "Q → F(t) → Responsiveness → Vacuum → Physics "
                "→ Complexity → Observation")

    out = os.path.join(OUTDIR, "fig1_emergence_ladder.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    return out


# ============================================================================= #
# FIGURE 2 — The Category A / B / C decisive-test boundary
# ============================================================================= #
def fig2_abc_boundary():
    fig, ax = plt.subplots(figsize=(9.4, 6.8))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 21)
    ax.axis("off")

    ax.text(15.0, 20.4, "The Boundary of the Spine",
            ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(15.0, 19.6,
            "the decisive-test scorecard — what responsiveness reaches, hosts, and where it stops",
            ha="center", va="center", fontsize=9.3, color=SUBINK, style="italic")

    # Column geometry
    col_w, gap = 9.0, 0.6
    x0 = 0.5
    cols = [x0, x0 + col_w + gap, x0 + 2 * (col_w + gap)]
    col_top, col_bot = 18.4, 1.2

    headers = [
        ("CATEGORY A", "On the Ladder", "responsiveness ORGANIZES it", C_DERIVED),
        ("CATEGORY B", "Hosted Matter-Content", "off-ladder — received, not organized", C_HOSTED_AMB),
        ("CATEGORY C", "Observer & Meta", "conjectural / open", C_CONJECTURAL),
    ]

    # Cell content: (label, verdict, accent color)
    colA = [
        ("Dark Energy",          "ORGANIZED",            C_DERIVED),
        ("Hierarchy (existence)", "ORGANIZED",           C_DERIVED),
        ("α = 1/3",         "ORGANIZED (value adopted)", C_DERIVED),
        ("Dark Matter",          "ORGANIZED — substrate-resident in F(t)", C_HOSTED),
        ("Quantum Gravity",      "PARTIAL (response derived,\ngeometry hosted)", C_FORBIDDEN),
    ]
    colB = [
        ("Neutrinos / Flavor",   "CONTAINER-SEAM",       C_HOSTED_AMB),
        ("Baryogenesis",         "CONTAINER-SEAM (weaker)", C_HOSTED_AMB),
        ("Coupling Unification", "untested through the lens\n(likely CONTAINER-SEAM)", C_OPEN),
    ]
    colC = [
        ("Consciousness",        "CONJECTURAL hook",     C_CONJECTURAL),
        ("Information",          "OPEN (arrow derived)", C_OPEN),
        ("Mathematics",          "conjectural slot",     C_CONJECTURAL),
    ]
    columns = [colA, colB, colC]

    for ci, (x) in enumerate(cols):
        cat, name, tag, accent = headers[ci]
        # outer region panel
        ax.add_patch(Rectangle((x, col_bot), col_w, col_top - col_bot,
                               facecolor=_tint(accent, 0.93), edgecolor=accent,
                               linewidth=1.6, zorder=1))
        # header band
        hb_h = 1.9
        ax.add_patch(Rectangle((x, col_top - hb_h), col_w, hb_h,
                               facecolor=accent, edgecolor=accent,
                               linewidth=0, zorder=2))
        ax.text(x + col_w / 2, col_top - 0.62, cat, ha="center", va="center",
                fontsize=12.5, fontweight="bold", color="white", zorder=3)
        ax.text(x + col_w / 2, col_top - 1.30, name, ha="center", va="center",
                fontsize=9.2, color="white", zorder=3)
        ax.text(x + col_w / 2, col_top - hb_h - 0.45, tag, ha="center", va="center",
                fontsize=8.0, color=accent, style="italic", zorder=3)

        # cells
        cells = columns[ci]
        cell_area_top = col_top - hb_h - 0.95
        cell_area_bot = col_bot + 0.35
        nrows = len(cells)
        cell_h = (cell_area_top - cell_area_bot) / nrows
        pad = 0.16
        for ri, (label, verdict, vcol) in enumerate(cells):
            cy_top = cell_area_top - ri * cell_h
            box = FancyBboxPatch((x + 0.35, cy_top - cell_h + pad),
                                 col_w - 0.70, cell_h - 2 * pad,
                                 boxstyle="round,pad=0.02,rounding_size=0.10",
                                 linewidth=1.3, edgecolor=vcol,
                                 facecolor="white", zorder=3)
            ax.add_patch(box)
            cyc = cy_top - cell_h / 2
            ax.text(x + 0.70, cyc + 0.34, label, ha="left", va="center",
                    fontsize=10.5, fontweight="bold", color=INK, zorder=4)
            # verdict swatch + text
            ax.add_patch(Rectangle((x + 0.70, cyc - 0.66), 0.34, 0.34,
                                   facecolor=vcol, edgecolor="none", zorder=4))
            ax.text(x + 1.18, cyc - 0.49, verdict, ha="left", va="center",
                    fontsize=8.1, color=vcol, zorder=4, linespacing=0.95)

    # The boundary line between A (reaches) and B/C (off-ladder)
    bx = cols[1] - gap / 2
    ax.add_line(Line2D([bx, bx], [col_bot - 0.1, col_top + 0.1],
                       color=INK, linewidth=2.4, linestyle=(0, (6, 3)), zorder=5))
    ax.text(bx, col_bot - 0.62, "the edge of the spine",
            ha="center", va="top", fontsize=8.2, color=INK, style="italic",
            fontweight="bold", zorder=5)

    _footer(ax, "Verdicts verbatim from GRUT_V4_SPINE.md Part IV · A = on-ladder "
                "(organized) · B = hosted SM matter-content (off-ladder) · "
                "C = observer/meta")

    out = os.path.join(OUTDIR, "fig2_abc_boundary.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    return out


# ============================================================================= #
# FIGURE 3 — The five-tier boundary legend (visual key)
# ============================================================================= #
def fig3_tier_legend():
    tiers = [
        ("DERIVED", C_DERIVED,
         "GRUT makes it from its own structure (zero / low free parameters).",
         "μ_linear = 1  —  the Pᵀᵀ projector\ntheorem (~32σ ISW)"),
        ("HOSTED", C_HOSTED,
         "GRUT receives it as a boundary condition it does not generate.",
         "Dark matter  —  substrate-resident\nin F(t), not external"),
        ("FORBIDDEN-BY-THEOREM", C_FORBIDDEN,
         "GRUT rules it out from its own axioms.",
         "Hierarchy magnitude  —  a 2nd\npropagating vacuum pole forbidden"),
        ("OPEN", C_OPEN,
         "No mechanism yet, but attackable.",
         "The α = 1/3 antecedent  —  the\nIR-carrier identification"),
        ("CONJECTURAL", C_CONJECTURAL,
         "A structural hook only — far from derivation.",
         "Consciousness  —  the in-in self-comparison\nhook, not a theory of mind"),
    ]

    fig, ax = plt.subplots(figsize=(9.6, 6.0))
    ax.set_xlim(0, 30)
    ax.set_ylim(-0.9, 16.5)
    ax.axis("off")

    ax.text(15.0, 15.8, "The Boundary Legend — Five Tiers",
            ha="center", va="center", fontsize=15.5, fontweight="bold", color=INK)
    ax.text(15.0, 15.05,
            "Every emergence event carries exactly one tier; the honesty is the boundary",
            ha="center", va="center", fontsize=9.5, color=SUBINK, style="italic")

    # column geometry
    x_panel_l, x_panel_r = 0.6, 29.4
    sw_x = 1.0                 # swatch left
    sw = 2.2                   # swatch width
    text_x = 4.3              # tier name / meaning left edge
    div_x = 16.5              # vertical divider between legend and example
    ex_x = 16.9               # example column left edge
    ex_c = (ex_x + x_panel_r) / 2   # example column center (examples centered here)

    # header for the example column
    ax.text(ex_c, 14.35, "canonical example", ha="center", va="bottom",
            fontsize=8.4, color=SUBINK, style="italic")

    row_top, row_bot = 13.9, 0.9
    n = len(tiers)
    row_h = (row_top - row_bot) / n
    pad = 0.22

    for i, (name, col, meaning, example) in enumerate(tiers):
        y_top = row_top - i * row_h
        yc = y_top - row_h / 2
        # row panel
        box = FancyBboxPatch((x_panel_l, y_top - row_h + pad),
                             x_panel_r - x_panel_l, row_h - 2 * pad,
                             boxstyle="round,pad=0.02,rounding_size=0.10",
                             linewidth=1.2, edgecolor=PANEL_ED,
                             facecolor=_tint(col, 0.95), zorder=2)
        ax.add_patch(box)
        # color swatch
        ax.add_patch(FancyBboxPatch((sw_x, y_top - row_h + pad + 0.18),
                                    sw, row_h - 2 * pad - 0.36,
                                    boxstyle="round,pad=0.01,rounding_size=0.08",
                                    linewidth=1.4, edgecolor=col,
                                    facecolor=col, zorder=3))
        # vertical divider inside the row
        ax.add_line(Line2D([div_x, div_x],
                           [y_top - row_h + pad + 0.18, y_top - pad - 0.18],
                           color=PANEL_ED, linewidth=1.0, zorder=3))
        # tier name
        ax.text(text_x, yc + 0.40, name, ha="left", va="center",
                fontsize=11.5, fontweight="bold", color=col, zorder=3)
        # meaning
        ax.text(text_x, yc - 0.38, meaning, ha="left", va="center",
                fontsize=8.4, color=SUBINK, zorder=3)
        # canonical example, centered in its own column (wrapped to two lines)
        ax.text(ex_c, yc, example, ha="center", va="center",
                fontsize=8.8, color=INK, style="italic", linespacing=1.2, zorder=3)

    # divider note: split-tier seams
    ax.text(15.0, 0.02,
            "Several events are split-tier seams [SPLIT]: a mechanism DERIVED on an anchored input\n"
            "— the split is the honest content, never collapsed upward.",
            ha="center", va="center", fontsize=10.0, color=SUBINK, style="italic",
            linespacing=1.3)

    _footer(ax, "GRUT ToE v4 reader legend (5 tiers) over the machine registry "
                "(6 tiers, 121 claims) — GRUT_V4_SPINE.md", size=9.2)

    out = os.path.join(OUTDIR, "fig3_tier_legend.png")
    fig.savefig(out, dpi=DPI, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    return out


if __name__ == "__main__":
    outs = [fig1_emergence_ladder(), fig2_abc_boundary(), fig3_tier_legend()]
    for p in outs:
        print("wrote", p)
