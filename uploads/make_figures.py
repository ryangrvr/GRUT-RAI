#!/usr/bin/env python3
"""
GRUT TOE — Professional Figure Generator
Generates all 9 figures as high-resolution PNGs in uploads/figures/.
Run once before building the PDF, or it is called automatically by generate_pdf.py.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, FancyBboxPatch
from matplotlib.lines import Line2D

def _pchip(x_data, y_data, x_query):
    """Monotone cubic interpolation (PCHIP) using only numpy."""
    x_data = np.asarray(x_data, dtype=float)
    y_data = np.asarray(y_data, dtype=float)
    x_query = np.asarray(x_query, dtype=float)
    n = len(x_data)
    h = np.diff(x_data)
    d = np.diff(y_data) / h
    m = np.zeros(n)
    for i in range(1, n - 1):
        if d[i-1] * d[i] > 0:
            w1 = 2*h[i] + h[i-1]
            w2 = h[i] + 2*h[i-1]
            m[i] = (w1 + w2) / (w1/d[i-1] + w2/d[i])
        else:
            m[i] = 0.0
    m[0]  = d[0]
    m[-1] = d[-1]
    result = np.empty_like(x_query)
    for j, xq in enumerate(x_query):
        idx = np.searchsorted(x_data, xq) - 1
        idx = int(np.clip(idx, 0, n - 2))
        t  = (xq - x_data[idx]) / h[idx]
        h00 = 2*t**3 - 3*t**2 + 1
        h10 = t**3 - 2*t**2 + t
        h01 = -2*t**3 + 3*t**2
        h11 = t**3 - t**2
        result[j] = (h00*y_data[idx] + h10*h[idx]*m[idx]
                   + h01*y_data[idx+1] + h11*h[idx]*m[idx+1])
    return result
import os
from pathlib import Path

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

# ── Colour palette (matches PDF) ──────────────────────────────────────────────
NAVY   = "#1a2744"
SLATE  = "#2c3e50"
BLUE   = "#2471a3"
TEAL   = "#1a8a8a"
ORANGE = "#ca6f1e"
GREEN  = "#1d8348"
RED    = "#922b21"
GRAY   = "#666666"
LGRAY  = "#cccccc"
BG     = "#f8f9fa"

DPI = 200

def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=DPI, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  ✓ {name}")

# ─────────────────────────────────────────────────────────────────────────────
# Figure 0 — τ₀ One-Parameter Bridge (front-matter overview)
# ─────────────────────────────────────────────────────────────────────────────
def fig00_tau0_bridge():
    """Front-matter schematic: one τ₀ measurement constrains three cosmological sectors."""
    FW, FH = 11, 6.2
    fig = plt.figure(figsize=(FW, FH), facecolor='white')
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW); ax.set_ylim(0, FH); ax.axis('off')

    DKRED  = '#5C0A0A'; DKBLUE = '#0A2050'; DKGRN  = '#0A3520'
    LRED   = '#FADBD8'; LBLUE  = '#D6EAF8'; LGRN   = '#D5F0E3'
    LGRAY_ = '#CCCCCC'

    def rbox(cx, cy, w, h, fc, ec, txt, fs=9.5, tc='white', lw=1.8, bold=False, pad=0.12, zo=4):
        p = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                           boxstyle=f'round,pad={pad}',
                           fc=fc, ec=ec, lw=lw, zorder=zo)
        ax.add_patch(p)
        ax.text(cx, cy, txt, ha='center', va='center', fontsize=fs, color=tc,
                fontweight='bold' if bold else 'normal',
                zorder=zo+1, linespacing=1.6)

    def hline(x1, x2, y, c=LGRAY_, lw=1.4):
        ax.plot([x1, x2], [y, y], color=c, lw=lw, zorder=2)

    def vline(x, y1, y2, c=LGRAY_, lw=1.4):
        ax.plot([x, x], [y1, y2], color=c, lw=lw, zorder=2)

    def arrow_down(x, y_start, y_end, c=SLATE):
        ax.annotate('', xy=(x, y_end), xytext=(x, y_start),
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.6,
                                    mutation_scale=14), zorder=5)

    # ── Title ──────────────────────────────────────────────────────────────────
    ax.text(FW/2, FH-0.28, "The One-Parameter Bridge",
            ha='center', va='top', fontsize=16, color=NAVY, fontweight='bold',
            fontfamily='serif')
    ax.text(FW/2, FH-0.68, r"A single lab measurement of $\tau_0$ simultaneously constrains"
            r" three cosmological sectors — zero free parameters",
            ha='center', va='top', fontsize=11.5, color=SLATE,
            fontfamily='serif', style='italic')

    # ── τ₀ source box ──────────────────────────────────────────────────────────
    rbox(FW/2, FH-1.50, 4.0, 0.65, NAVY, NAVY,
         r'$\tau_0 = 41.9$ Myr  —  measured in lab',
         fs=13, bold=True, pad=0.16, zo=5)

    # ── Branching tree ─────────────────────────────────────────────────────────
    XL, XC, XR = 1.9, FW/2, FW-1.9
    Y_src_bot = FH - 1.83
    Y_junc    = FH - 2.40
    Y_arm_bot = FH - 2.80

    vline(XC, Y_src_bot, Y_junc)
    hline(XL, XR, Y_junc)
    for x in [XL, XC, XR]:
        arrow_down(x, Y_junc, Y_arm_bot)

    # ── Left branch: Λ_grav / Falsifier F1 ────────────────────────────────────
    rbox(XL, FH-3.58, 3.3, 1.35, DKRED, '#922b21',
         'Λ$_{\\rm grav}$ = 689 Hz\n'
         'Decoherence plateau\n'
         'Falsifier F1',
         fs=11.5, tc=LRED, pad=0.13, zo=4)
    ax.text(XL, FH-4.72,
            'Confirmed: validates core mechanism\n'
            'Refuted: kills entire framework',
            ha='center', va='top', fontsize=10.5, color=DKRED,
            fontfamily='serif', style='italic', linespacing=1.55)

    # ── Centre branch: H_inf / H₀ / Ω_Λ ──────────────────────────────────────
    rbox(XC, FH-3.58, 3.5, 1.35, DKBLUE, '#1a3a6b',
         '$H_{\\rm inf} = (2{-}R)/(S\\tau_0)$\n'
         r'$\Rightarrow H_0 = 69.03$ km/s/Mpc' + '\n'
         r'$\Rightarrow \Omega_\Lambda = 0.689$',
         fs=11.5, tc=LBLUE, pad=0.13, zo=4)
    ax.text(XC, FH-4.72,
            'Terminal velocity — CTP drive / friction\n'
            'Both within the Planck tension gap',
            ha='center', va='top', fontsize=10.5, color=DKBLUE,
            fontfamily='serif', style='italic', linespacing=1.55)

    # ── Right branch: Ω_dm ─────────────────────────────────────────────────────
    rbox(XR, FH-3.58, 3.3, 1.35, DKGRN, '#1d8348',
         r'$\Omega_{\rm dm} = \alpha_{\rm vac} = 1/3$' + '\n'
         r'$n_g$ refractive (bound-system)' + '\n'
         '(zero parameters)',
         fs=11.5, tc=LGRN, pad=0.13, zo=4)
    ax.text(XR, FH-4.72,
            'Geometric — from CTP action alone\n'
            '(+27% overshoot: open tension)',
            ha='center', va='top', fontsize=10.5, color=DKGRN,
            fontfamily='serif', style='italic', linespacing=1.55)

    # ── Footer ─────────────────────────────────────────────────────────────────
    ax.text(FW/2, 0.22,
            r'Three predictions. Zero free parameters. '
            r'If the 689 Hz plateau is confirmed, all three sectors validate simultaneously.',
            ha='center', va='bottom', fontsize=11, color=SLATE,
            fontfamily='serif', style='italic',
            bbox=dict(boxstyle='round,pad=0.3', fc='#F2F3F4', ec=LGRAY_, alpha=0.85))

    save(fig, "fig_00_tau0_bridge.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2 — Two-Timescale Logarithmic Map
# ─────────────────────────────────────────────────────────────────────────────
def fig02_timescales():
    fig, ax = plt.subplots(figsize=(11, 4.2))
    fig.patch.set_facecolor('white')
    ax.set_facecolor(BG)
    ax.set_xlim(-44, 18)
    ax.set_ylim(-2.8, 3.2)
    ax.axis('off')

    tau_micro_x = -19 + np.log10(1.4)   # ≈ -18.85
    tau0_x      = np.log10(1.322e15)     # ≈ 15.12
    YLINE = 0.0   # spine y-coordinate

    # ── Regime shading ──────────────────────────────────────────────────────
    ax.axvspan(-44, tau_micro_x, alpha=0.07, color=RED,   zorder=0)
    ax.axvspan(tau0_x, 18,       alpha=0.07, color=GREEN, zorder=0)

    # ── Timeline spine ──────────────────────────────────────────────────────
    ax.annotate("", xy=(17.5, YLINE), xytext=(-43.5, YLINE),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))

    # ── Tick marks every 5 decades ─────────────────────────────────────────
    for logval in range(-40, 18, 5):
        ax.plot([logval, logval], [YLINE-0.12, YLINE+0.12], color=NAVY, lw=1)
        ax.text(logval, YLINE - 0.28, str(logval),
                ha='center', va='top', fontsize=7, color=GRAY)
    ax.text(17.8, YLINE, r"$\log_{10}(t\,/\,\mathrm{s})$",
            ha='left', va='center', fontsize=9, color=NAVY, fontfamily='serif')

    # ── Secondary reference points (alternating up/down, non-crowded) ──────
    # (x, label, side, y_text_gap)
    secondary = [
        (-43.3,  "Planck\n$t_P$",         "down", -0.5),
        (-17.0,  "Nuclear",                "down", -0.5),
        (-10.0,  "Atomic",                 "up",    0.5),
        (  7.5,  "Human year",             "down", -0.5),
        (17.12,  "Age of\nUniverse $t_U$", "down", -0.5),
    ]
    for x, lbl, side, gap in secondary:
        ax.plot(x, YLINE, 'o', color=SLATE, ms=5, zorder=4)
        va = "top" if side == "down" else "bottom"
        ax.text(x, YLINE + gap, lbl, ha='center', va=va,
                fontsize=7.5, color=SLATE, fontfamily='serif',
                multialignment='center')

    # ── Main anchors ─────────────────────────────────────────────────────────
    # τ_micro: annotation goes BELOW the timeline to avoid overlap with τ₀ box
    ax.plot(tau_micro_x, YLINE, 'D', color=RED, ms=10, zorder=6)
    ax.annotate(
        r"$\tau_{\rm micro} \approx 1.4\times10^{-19}$ s" + "\n"
        r"BBN epoch  •  $T_c = 54.7$ MK" + "\n"
        r"Crystal regime: $X \gg 1$,  GR exact",
        xy=(tau_micro_x, YLINE - 0.18),       # arrow tip below diamond
        xytext=(tau_micro_x, -1.55),           # box below the timeline
        arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.4),
        fontsize=8.5, color=RED, ha='center', va='top', fontfamily='serif',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff4f4',
                  edgecolor=RED, alpha=0.95, zorder=10))

    # τ₀: annotation goes ABOVE the timeline, well right of τ_micro box
    ax.plot(tau0_x, YLINE, 'D', color=GREEN, ms=10, zorder=6)
    ax.annotate(
        r"$\tau_0 = 41.9$ Myr  $\approx 1.32\times10^{15}$ s" + "\n"
        r"Cosmic baseline  •  Bullet Cluster anchor" + "\n"
        r"Fluid regime: $X \ll 1$,  dark sector active",
        xy=(tau0_x, YLINE + 0.18),            # arrow tip above diamond
        xytext=(tau0_x - 4, 1.3),             # box above timeline, left of diamond
        arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.4,
                        connectionstyle="arc3,rad=-0.15"),
        fontsize=8.5, color=GREEN, ha='center', va='bottom', fontfamily='serif',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f4fff4',
                  edgecolor=GREEN, alpha=0.95, zorder=10))

    # ── 34-orders brace ────────────────────────────────────────────────────
    brace_y = 2.35
    ax.annotate("", xy=(tau0_x, brace_y), xytext=(tau_micro_x, brace_y),
                arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2))
    mid = (tau_micro_x + tau0_x) / 2
    ax.text(mid, brace_y + 0.18,
            "34 orders of magnitude — independently anchored (Option B, June 2026)",
            ha='center', va='bottom', fontsize=9, color=BLUE,
            fontweight='bold', fontfamily='serif')

    # ── Compact regime dividers on the spine ──────────────────────────────
    ax.text(tau_micro_x - 9, -0.45,
            r"Thermal / crystal  ($X\gg1$,  GR exact)",
            ha='center', fontsize=7.5, color=RED, style='italic', fontfamily='serif')
    ax.text((tau_micro_x + tau0_x) / 2, -0.45,
            r"← 34-decade gap (no derivation) →",
            ha='center', fontsize=7.5, color=SLATE, style='italic', fontfamily='serif')
    ax.text(tau0_x + 1, -0.45,
            r"Fluid / dark sector  ($X\ll1$)",
            ha='center', fontsize=7.5, color=GREEN, style='italic', fontfamily='serif')

    ax.set_title("GRUT Two-Timescale Hierarchy  —  $\\tau_{\\rm micro}$ to $\\tau_0$, 34 decades",
                 fontsize=12, fontweight='bold', color=NAVY, fontfamily='serif', pad=8)
    plt.tight_layout(pad=0.5)
    save(fig, "fig_02_timescales.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 3 — n_g²(ωτ₀): Three Regimes of the Responsive Vacuum
# ─────────────────────────────────────────────────────────────────────────────
def fig03_three_regimes():
    alpha = 1/3
    log_x = np.linspace(-3, 3, 1200)
    x     = 10**log_x                   # ωτ₀
    ng2   = 1 + alpha / (1 + x**2)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor(BG)

    # Regime shadings
    ax.axvspan(-3, -0.5, alpha=0.10, color=BLUE,   zorder=0)
    ax.axvspan(-0.5, 0.5, alpha=0.10, color=ORANGE, zorder=0)
    ax.axvspan( 0.5, 3,   alpha=0.10, color=NAVY,   zorder=0)

    # Main curve
    ax.plot(log_x, ng2, color=NAVY, lw=2.5, label=r"$n_g^2(\omega\tau_0)$")

    # Asymptotes
    ax.axhline(1 + alpha, color=BLUE, lw=1.2, ls='--', alpha=0.7,
               label=r"$n_g^2 \to 4/3$ (super-horizon limit, $\omega\tau_0 \ll 1$)")
    ax.axhline(1.0, color=NAVY, lw=1.0, ls=':', alpha=0.7,
               label=r"$n_g^2 \to 1$ (GR recovery, $\omega\tau_0 \gg 1$)")

    # Transition marker
    ax.axvline(0, color=ORANGE, lw=1.2, ls='--', alpha=0.8,
               label=r"Boundary $\omega\tau_0 = 1$ (≈ 689 Hz for $\tau_0 = 41.9$ Myr)")
    ax.plot(0, 1 + alpha/(1+1), 'o', color=ORANGE, ms=8, zorder=6)

    # Regime labels
    # FLUID: push up to 1.36 so α_vac annotation can sit below it at ~1.18
    ax.text(-1.8, 1.36, "FLUID\n(dark sector)", ha='center', va='center',
            fontsize=9, color=BLUE, fontweight='bold', fontfamily='serif')
    ax.text( 0.0, 1.08, "BOUNDARY\n(~689 Hz)", ha='center', va='center',
            fontsize=9, color=ORANGE, fontweight='bold', fontfamily='serif')
    # CRYSTAL: lift off the n²=1 dotted line
    ax.text( 1.8, 1.05, "CRYSTAL\n(GR exact)", ha='center', va='center',
            fontsize=9, color=NAVY, fontweight='bold', fontfamily='serif')

    # α_vac annotation: lower xytext so it sits clearly below the FLUID label
    ax.annotate(r"$\alpha_{\rm vac} = 1/3$" + "\n" + r"(Gate R, Duff 1994)",
                xy=(-2.5, 1 + alpha - 0.005), xytext=(-2.3, 1.18),
                arrowprops=dict(arrowstyle='->', color=BLUE, lw=1),
                fontsize=8, color=BLUE, ha='center')

    ax.set_xlabel(r"$\log_{10}(\omega\tau_0)$", fontsize=11, fontfamily='serif')
    ax.set_ylabel(r"$n_g^2(\omega\tau_0) = 1 + \frac{\alpha_{\rm vac}}{1+(\omega\tau_0)^2}$",
                  fontsize=11, fontfamily='serif')
    ax.set_title(r"Responsive Vacuum Index $n_g^2$ — Three Regimes",
                 fontsize=11, fontweight='bold', color=NAVY, fontfamily='serif')
    ax.set_ylim(0.95, 1.42)
    ax.set_xlim(-3, 3)
    ax.tick_params(labelsize=9)
    ax.legend(fontsize=7.5, loc='center right', framealpha=0.9)
    ax.grid(True, alpha=0.3, lw=0.6)
    plt.tight_layout()
    save(fig, "fig_03_three_regimes.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 4 — Gate R: Two-Route Convergence to R = √(4/3)
# ─────────────────────────────────────────────────────────────────────────────
def fig04_gate_r():
    fig, axes = plt.subplots(1, 2, figsize=(11, 6.5),
                             gridspec_kw={'width_ratios': [1.5, 1]})
    fig.patch.set_facecolor('white')

    # ─ Left panel: Derivation flowchart ─────────────────────────────────────
    ax = axes[0]
    # y-axis: 0–13 so headers at y=12 are safely inside
    ax.set_xlim(0, 11); ax.set_ylim(0, 13); ax.axis('off')

    def box(ax, cx, cy, txt, col, w=3.8, h=1.0, fs=8.5):
        rect = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                              boxstyle="round,pad=0.1", linewidth=1.3,
                              edgecolor=col, facecolor=col+'22')
        ax.add_patch(rect)
        ax.text(cx, cy, txt, ha='center', va='center', fontsize=fs,
                color=col, fontweight='bold', fontfamily='serif',
                multialignment='center')

    def arrow(ax, x1, y1, x2, y2, col=SLATE):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=col,
                                   lw=1.4, mutation_scale=14))

    # ── Path G boxes (left column, cx=2.8) ───────────────────────────────
    YS_G = [11.2, 9.5, 7.8, 6.1, 4.4, 2.7]
    labels_G = [
        "CTP Action  $S_{\\rm CTP}$",
        "Weyl decomp\n$g_{\\mu\\nu}=e^{2\\sigma}\\hat{g}_{\\mu\\nu}$",
        "Conformal scalar $\\sigma$\n$\\xi_c = 1/6$, spin-0",
        "Duff 1994  $(a,c)=(1,3)$\n$\\alpha_{\\rm vac}=a/c=1/3$",
        "Constitutive kernel\n$K^R = \\alpha_{\\rm vac}\\chi P^{TT}$",
        "$R = \\sqrt{4/3} = 1.154701$\n(Path G  — CANONICAL)",
    ]
    cols_G = [NAVY, BLUE, BLUE, BLUE, BLUE, GREEN]
    for cy, txt, col in zip(YS_G, labels_G, cols_G):
        box(ax, 2.8, cy, txt, col, w=4.0)
    for y1, y2 in zip(YS_G[:-1], YS_G[1:]):
        arrow(ax, 2.8, y1 - 0.5, 2.8, y2 + 0.5, BLUE)

    # ── Anomaly route boxes (right column, cx=7.8) ───────────────────────
    YS_A = [11.2, 9.5, 7.8, 6.1]
    labels_A = [
        "3-loop CTP on $S^4$",
        "Christensen-Duff\n$\\hat{a}=43/16$",
        "TJI $[{}_2F_1]^3$ integral\n(OPEN — HypExp)",
        "$R_{\\rm anomaly} = 1.15428$\n(diagnostic; honest negative)",
    ]
    cols_A = [NAVY, ORANGE, RED, ORANGE]
    for cy, txt, col in zip(YS_A, labels_A, cols_A):
        box(ax, 7.8, cy, txt, col, w=3.8)
    for y1, y2 in zip(YS_A[:-1], YS_A[1:]):
        arrow(ax, 7.8, y1 - 0.5, 7.8, y2 + 0.5, ORANGE)
    # "not a correction" note
    ax.plot([7.8], [5.0], 'x', ms=12, mew=2.5, color=RED, zorder=6)
    ax.text(7.8, 4.35,
            "0.036% from canonical\n(loop route — not a correction)",
            ha='center', va='top', fontsize=8, color=ORANGE, style='italic',
            fontfamily='serif')

    # ── Column headers (within ylim) ─────────────────────────────────────
    ax.text(2.8, 12.35, "Path G  (canonical)", ha='center', fontsize=10,
            color=BLUE, fontweight='bold', fontfamily='serif')
    ax.text(7.8, 12.35, "Anomaly Route  (diagnostic)", ha='center', fontsize=10,
            color=ORANGE, fontweight='bold', fontfamily='serif')
    ax.set_title("Gate R — Two Independent Derivation Routes",
                 fontsize=12, fontweight='bold', color=NAVY, fontfamily='serif')

    # ─ Right panel: Convergence bar ─────────────────────────────────────────
    ax2 = axes[1]
    ax2.set_facecolor(BG)

    R_true    = np.sqrt(4/3)
    R_anomaly = 1.15428
    xlabels   = ["Path G\n(Canonical)", "Anomaly\nRoute"]
    values    = [R_true, R_anomaly]
    colors    = [GREEN, ORANGE]
    bars = ax2.bar(xlabels, values, color=colors, width=0.5,
                   edgecolor=NAVY, linewidth=1.0)
    ax2.axhline(R_true, color=GREEN, lw=1.5, ls='--', alpha=0.6)
    ax2.set_ylim(1.148, 1.162)
    ax2.set_ylabel(r"Value of $R$", fontsize=11, fontfamily='serif')
    ax2.set_title(r"Convergence to $R = \sqrt{4/3}$",
                  fontsize=11, fontweight='bold', color=NAVY, fontfamily='serif')
    ax2.tick_params(labelsize=10)
    ax2.grid(axis='y', alpha=0.3)
    for bar, val, col in zip(bars, values, colors):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 0.0001,
                f"{val:.6f}", ha='center', va='bottom',
                fontsize=9, color=col, fontweight='bold', fontfamily='serif')
    ax2.text(0.5, 0.10,
             r"$\Delta R = 0.036\%$" + "\n(0.96% from canonical\nat 6 sig. figs.)",
             ha='center', va='bottom', transform=ax2.transAxes,
             fontsize=9, color=SLATE, style='italic', fontfamily='serif')
    ax2.text(0.5, 0.78, r"$\sqrt{4/3}$", ha='center', va='bottom',
             transform=ax2.transAxes, fontsize=12, color=GREEN,
             fontweight='bold', fontfamily='serif')
    fig.tight_layout(pad=1.8)
    save(fig, "fig_04_gate_r.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 9 — Cluster Merger Schematic (Bullet Cluster mechanism)
# ─────────────────────────────────────────────────────────────────────────────
def fig09_cluster_schematic():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
    fig.patch.set_facecolor('white')

    def cluster_panel(ax, title, label, gas_offset, dm_offset,
                      v_arrows=True, after=False):
        ax.set_facecolor(BG)
        ax.set_xlim(-4.5, 4.5); ax.set_ylim(-2.5, 3.0)
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold',
                     color=NAVY, pad=4, fontfamily='serif')

        if not after:
            # Two approaching clusters
            for sign, c_gas, c_dm in [(-1, '#e67e22', '#2e86c1'),
                                       ( 1, '#e67e22', '#2e86c1')]:
                cx = sign * 2.5
                # DM halo (dashed ellipse)
                ell = mpatches.Ellipse((cx, 0), 2.8, 2.0,
                                       fill=False, edgecolor=c_dm,
                                       lw=2, ls='--', alpha=0.9)
                ax.add_patch(ell)
                # Gas blob (solid)
                ell2 = mpatches.Ellipse((cx, 0), 1.5, 1.0,
                                        alpha=0.55, facecolor=c_gas,
                                        edgecolor='#a04000', lw=1)
                ax.add_patch(ell2)
                # Velocity arrow
                ax.annotate("", xy=(-sign * 1.4, 0), xytext=(cx, 0),
                            arrowprops=dict(arrowstyle="-|>", color=NAVY,
                                            lw=2, mutation_scale=16))
            ax.text(0, -1.8, "v ≈ 4700 km/s →    ← v", ha='center',
                    fontsize=12, color=NAVY, fontfamily='serif')
            ax.text(-2.5,  1.45, "DM halo",  ha='center', fontsize=12,
                    color=BLUE, fontfamily='serif')
            ax.text(-2.5, -0.15, "gas",      ha='center', fontsize=12,
                    color=ORANGE, fontfamily='serif', fontweight='bold')
        else:
            # Gas stopped at centre
            gas = mpatches.Ellipse((0 + gas_offset, 0), 2.2, 1.4,
                                   alpha=0.50, facecolor='#e67e22',
                                   edgecolor='#a04000', lw=1.2)
            ax.add_patch(gas)
            ax.text(gas_offset, 0, "gas\n(collisional,\nstopped)",
                    ha='center', va='center', fontsize=11,
                    color='#7d3c00', fontweight='bold', fontfamily='serif')

            # DM lensing mass (two offset blobs)
            for sign, xoff in [(-1, -dm_offset), (1, dm_offset)]:
                dm = mpatches.Ellipse((xoff, 0.1), 2.6, 1.8,
                                      fill=False, edgecolor=BLUE,
                                      lw=2.2, ls='--', alpha=0.85)
                ax.add_patch(dm)
                ax.annotate("lensing\nmass", xy=(xoff, 1.05),
                            fontsize=12, ha='center', color=BLUE,
                            fontfamily='serif')

            # Offset dimension arrow
            ax.annotate("", xy=(dm_offset - 0.1, -1.5),
                        xytext=(-dm_offset + 0.1, -1.5),
                        arrowprops=dict(arrowstyle="<->", color=RED, lw=1.5))
            ax.text(0, -1.95,
                    r"$\delta \approx v \times \tau_0 \approx 150$ kpc",
                    ha='center', fontsize=13, color=RED, fontweight='bold',
                    fontfamily='serif')
            ax.text(0, 2.5,
                    r"Mechanism: retarded kernel $K^R \propto e^{-t/\tau_0}$",
                    ha='center', fontsize=11, color=SLATE, style='italic',
                    fontfamily='serif')

    cluster_panel(axes[0], "Before Merger", "before",
                  gas_offset=0, dm_offset=2.5, after=False)
    cluster_panel(axes[1], "After Merger (Bullet Cluster)", "after",
                  gas_offset=0, dm_offset=2.0, after=True)

    fig.suptitle("GRUT Cluster Merger Lag Mechanism — Viscoelastic Memory Kernel",
                 fontsize=14, fontweight='bold', color=NAVY,
                 fontfamily='serif', y=1.02)
    plt.tight_layout(pad=1.2)
    save(fig, "fig_09_cluster_schematic.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 10 — Cluster Merger Population Scaling
# ─────────────────────────────────────────────────────────────────────────────
def fig10_cluster_scaling():
    # Data from document + derived GRUT predictions (δ = v × τ₀ × dec_ratio)
    # Using canonical dec_ratio ≈ 0.638, τ₀ = 41.9 Myr
    tau0_Myr = 41.9
    kpc_per_km_s_Myr = 0.001023   # 1 km/s × 1 Myr in kpc
    dec_ratio = 0.638

    def grut_pred(v):
        return v * tau0_Myr * dec_ratio * kpc_per_km_s_Myr

    # v_init (km/s), obs δ (kpc), obs uncertainty (kpc)
    clusters = {
        "Bullet": (4700, 150, 30),
        "MACS J0025": (2400, 75, 15),
        "Abell 520": (2300, 80, 20),
    }
    elgordo_v = 2500
    elgordo_obs_range = (120, 350)   # conservative quoted range
    elgordo_pred_range = (43, 130)   # 80-param sweep from document

    fig, ax = plt.subplots(figsize=(7, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor(BG)

    # GRUT prediction line
    v_line = np.linspace(0, 5500, 300)
    d_line = grut_pred(v_line)
    ax.plot(v_line, d_line, color=NAVY, lw=2.2, label=r"GRUT: $\delta = v \times \tau_0 \times f_{\rm dec}$")

    # ±20% band
    ax.fill_between(v_line, 0.80 * d_line, 1.20 * d_line,
                    alpha=0.12, color=BLUE, label="±20% uncertainty band")

    # Per-cluster label offsets — Abell 520 and MACS J0025 sit at nearly the
    # same (v, δ) so they need to be pulled in opposite directions.
    label_offsets = {
        "Bullet":     ( 130,  10),   # right of point, no crowding
        "MACS J0025": ( 200, -22),   # right and below
        "Abell 520":  (-900,  18),   # left of the cluster pair
    }

    # Normal-regime clusters
    clrs = [GREEN, BLUE, TEAL]
    markers = ['o', 's', '^']
    for (name, (v, obs, err)), c, mk in zip(clusters.items(), clrs, markers):
        pred = grut_pred(v)
        ax.errorbar(v, obs, yerr=err, fmt=mk, color=c, ms=10,
                    capsize=5, ecolor=c, elinewidth=1.5, linewidth=2,
                    label=f"{name}  (pred = {pred:.0f} kpc)")
        dx, dy = label_offsets[name]
        ax.annotate(name, xy=(v, obs), xytext=(v + dx, obs + dy),
                    arrowprops=dict(arrowstyle='->', color=c, lw=0.8),
                    fontsize=8.5, color=c, fontfamily='serif',
                    fontweight='bold')

    # El Gordo (tension/overlap)
    eg_pred_mid = (elgordo_pred_range[0] + elgordo_pred_range[1]) / 2   # ≈ 86.5 kpc
    eg_obs_mid  = (elgordo_obs_range[0]  + elgordo_obs_range[1])  / 2   # ≈ 235 kpc

    # GRUT prediction range marker (orange diamond)
    ax.errorbar(elgordo_v, eg_pred_mid,
                yerr=[[(elgordo_pred_range[1] - elgordo_pred_range[0]) / 2],
                      [(elgordo_pred_range[1] - elgordo_pred_range[0]) / 2]],
                fmt='D', color=ORANGE, ms=9, capsize=5,
                ecolor=ORANGE, elinewidth=1.5, linewidth=2)

    # Observed range marker (red diamond), offset right to avoid crowding
    ax.errorbar(elgordo_v + 200, eg_obs_mid,
                yerr=[[(elgordo_obs_range[1] - elgordo_obs_range[0]) / 2],
                      [(elgordo_obs_range[1] - elgordo_obs_range[0]) / 2]],
                fmt='D', color=RED, ms=9, capsize=5,
                ecolor=RED, elinewidth=1.5, linewidth=2, alpha=0.7)

    # Annotation box with arrow pointing to the orange GRUT pred diamond
    ax.annotate(
        "El Gordo\n(pred: 43–130 kpc\nobs: 120–350 kpc)\n[tension/overlap]",
        xy=(elgordo_v, eg_pred_mid),          # tip of arrow → orange diamond
        xytext=(elgordo_v + 600, 230),         # text box upper-right of cluster
        fontsize=8, color=ORANGE, fontfamily='serif',
        arrowprops=dict(arrowstyle='->', color=ORANGE, lw=1.0),
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                  edgecolor=ORANGE, alpha=0.9))

    # Labels
    ax.set_xlabel("Merger Velocity $v_{\\rm init}$ (km/s)",
                  fontsize=11, fontfamily='serif')
    ax.set_ylabel("Lensing–Gas Offset $\\delta$ (kpc)",
                  fontsize=11, fontfamily='serif')
    ax.set_title("Cluster Merger Population Scaling — GRUT vs. Observed",
                 fontsize=11, fontweight='bold', color=NAVY, fontfamily='serif')
    ax.set_xlim(0, 5800); ax.set_ylim(0, 450)
    ax.tick_params(labelsize=9)
    ax.grid(True, alpha=0.3, lw=0.6)

    # Legend
    legend_extra = [
        Line2D([0],[0], marker='D', color='w', markerfacecolor=ORANGE, ms=9,
               label="El Gordo — GRUT pred range"),
        Line2D([0],[0], marker='D', color='w', markerfacecolor=RED, ms=9,
               label="El Gordo — observed range"),
    ]
    handles, labs = ax.get_legend_handles_labels()
    ax.legend(handles + legend_extra,
              labs + ["El Gordo — GRUT pred range",
                      "El Gordo — observed range"],
              fontsize=7.5, loc='upper left', framealpha=0.92)

    # Internal scaling residual annotation
    ax.text(0.97, 0.05,
            "Internal $v\\!\\times\\!\\tau_0$ scaling residual: 1.72%\n"
            "Systematic offset obs/pred ≈ 0.83–0.88\n"
            "(degenerate with $f_{\\rm dec}$ convention)",
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=7.5, color=SLATE, style='italic', fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor=LGRAY, alpha=0.8))
    plt.tight_layout()
    save(fig, "fig_10_cluster_scaling.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 11 — μ_GRUT profile + P(k)/P_ΛCDM
# ─────────────────────────────────────────────────────────────────────────────
def fig11_modified_gravity():
    alpha_vac = 1/3
    tau0_s    = 1.322e15      # seconds
    c_kms     = 2.998e5       # km/s
    H0        = 67.36         # km/s/Mpc
    tau0_Mpc  = tau0_s * c_kms / (3.086e19)   # τ₀ in Mpc/h units ≈ 12878 Mpc

    def mu_minus_1(k_hMpc, z):
        a = 1.0 / (1.0 + z)
        k_phys = k_hMpc / a   # h/Mpc
        # k_phys in Mpc⁻¹ → τ₀ k_phys c (dimensionless)
        k_s_inv = k_phys / (3.086e19 / c_kms)  # from h/Mpc to 1/Mpc then 1/s
        x = tau0_s * k_s_inv * c_kms / 3.086e19
        # Actually: (τ₀ k_phys)² with τ₀ in Mpc/c:
        # x = k_phys * tau0_Mpc (in Mpc)
        x2 = (k_phys * tau0_Mpc)**2
        return alpha_vac / (1 + x2)

    k_arr = np.logspace(-4, 1, 800)   # h/Mpc

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8))
    fig.patch.set_facecolor('white')

    # ── Left: μ−1 profile ────────────────────────────────────────────────────
    ax1.set_facecolor(BG)
    zvals  = [0, 1, 5]
    cols   = [NAVY, BLUE, TEAL]
    lstys  = ['-', '--', ':']
    for z, c, ls in zip(zvals, cols, lstys):
        mu1 = np.array([mu_minus_1(k, z) for k in k_arr])
        ax1.loglog(k_arr, mu1, color=c, lw=2.2, ls=ls, label=f"$z={z}$")

    # λ* transition line
    k_star = 1.0 / tau0_Mpc    # k_phys ≈ 1/τ₀, in 1/Mpc ≈ 7.8×10⁻⁵ h/Mpc
    k_star_obs = 1.0 / 80.7    # λ* ≈ 80.7 Mpc → k* ≈ 0.0124 h/Mpc
    ax1.axvline(k_star_obs, color=ORANGE, lw=1.5, ls='--', alpha=0.8)
    ax1.text(k_star_obs * 1.4, 1e-4,
             r"$\lambda^* \approx 80.7$ Mpc" + "\n" + r"$k^* = 1/(\tau_0 c)$",
             fontsize=8, color=ORANGE, va='bottom', fontfamily='serif')
    ax1.axhline(alpha_vac, color=LGRAY, lw=1, ls=':', alpha=0.6)
    ax1.text(5e-4, alpha_vac * 1.05, r"$\alpha_{\rm vac}=1/3$ (QSA limit)",
             fontsize=7.5, color=GRAY, va='bottom', fontfamily='serif')
    ax1.set_xlabel(r"$k$ [h/Mpc]", fontsize=11, fontfamily='serif')
    ax1.set_ylabel(r"$\mu_{\rm GRUT}(k,a) - 1$", fontsize=11, fontfamily='serif')
    ax1.set_title(r"Modified Gravity Parameter $\mu - 1$ vs. Wavenumber",
                  fontsize=10, fontweight='bold', color=NAVY, fontfamily='serif')
    ax1.set_xlim(1e-4, 10); ax1.set_ylim(1e-6, 1)
    ax1.legend(fontsize=9, framealpha=0.9)
    ax1.grid(True, alpha=0.3, which='both')
    ax1.tick_params(labelsize=9)

    # ── Right: P(k)/P_ΛCDM ───────────────────────────────────────────────────
    ax2.set_facecolor(BG)
    # Data from Correction #36 native Boltzmann (from document table)
    k_data = np.array([0.001, 0.010, 0.050, 0.100, 0.200, 0.500])
    Pratio = np.array([0.25,  0.27,  0.18,  0.10,  0.04,  0.01])  # fractional enhancement

    k_plot = np.logspace(-3, 0, 400)
    P_smooth = np.clip(_pchip(np.log10(k_data), Pratio, np.log10(k_plot)), 0, None)
    ax2.semilogx(k_plot, P_smooth * 100, color=BLUE, lw=2.5,
                 label="Correction #36\n(native Boltzmann)")

    ax2.scatter(k_data, Pratio * 100, color=NAVY, s=50, zorder=6)
    ax2.axhline(3.22, color=RED, lw=1.5, ls='--', alpha=0.8,
                label=r"$\sigma_8$ scale (+3.22%)")
    ax2.axvline(0.2, color=ORANGE, lw=1.0, ls=':', alpha=0.6)
    ax2.text(0.25, 25, r"$\sigma_8$ scale", fontsize=8, color=ORANGE,
             fontfamily='serif')
    ax2.set_xlabel(r"$k$ [h/Mpc]", fontsize=11, fontfamily='serif')
    ax2.set_ylabel(r"$P^{\rm GRUT}/P^{\Lambda{\rm CDM}} - 1$ [%]",
                   fontsize=11, fontfamily='serif')
    ax2.set_title(r"Scale-Dependent $P(k)$ Enhancement (z = 0)",
                  fontsize=10, fontweight='bold', color=NAVY, fontfamily='serif')
    ax2.set_xlim(1e-3, 1); ax2.set_ylim(-1, 35)
    ax2.legend(fontsize=9, framealpha=0.9, loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelsize=9)

    plt.tight_layout(pad=1.5)
    save(fig, "fig_11_modified_gravity.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 14 — CMB + P(k): Correction #36 Native Boltzmann
# ─────────────────────────────────────────────────────────────────────────────
def fig14_cmb_pk():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8))
    fig.patch.set_facecolor('white')

    # ── Left: D_ℓ^TT schematic ───────────────────────────────────────────────
    ax1.set_facecolor(BG)
    # Approximate ΛCDM-like spectrum (schematic, not exact CAMB)
    ell_fine = np.linspace(2, 2500, 5000)

    def dl_lcdm(ell):
        # Rough phenomenological form capturing acoustic peaks
        envelope = 6000 * (ell / 200)**0.1 * np.exp(-ell / 2200)
        peaks  = (  np.exp(-((ell-220)/70)**2) * 1.0
                  + np.exp(-((ell-540)/80)**2) * 0.48
                  + np.exp(-((ell-810)/90)**2) * 0.24
                  + np.exp(-((ell-1100)/100)**2)*0.11
                  + np.exp(-((ell-1400)/110)**2)*0.05)
        troughs= (  np.exp(-((ell-400)/70)**2) * 0.35
                  + np.exp(-((ell-680)/80)**2) * 0.18
                  + np.exp(-((ell-960)/90)**2) * 0.09)
        base   = 5.5 * (ell*(ell+1)/(200*201))**0.04 * np.exp(-ell/2300)
        return envelope * (0.3 + peaks - 0.85*troughs) + base * 80

    dl = dl_lcdm(ell_fine)
    dl_grut = dl.copy()
    # GRUT modification: negligible at ℓ>100, tiny at low-ℓ
    dl_grut[ell_fine > 100] *= (1 + 0.001 * np.exp(-((ell_fine[ell_fine>100]-200)/400)**2))
    dl_grut[ell_fine <= 30] *= 1.005  # small ISW enhancement

    ax1.plot(ell_fine, dl, color=LGRAY, lw=2, ls='--', label=r"$\Lambda$CDM", zorder=2)
    ax1.plot(ell_fine, dl_grut, color=BLUE, lw=1.8, label="GRUT #36 (γ=1)", alpha=0.9, zorder=3)

    ax1.axvline(30, color=ORANGE, lw=1, ls=':', alpha=0.7)
    ax1.text(34, 6800, r"$\ell=30$", fontsize=8, color=ORANGE, fontfamily='serif')
    ax1.text(200, 200,
             r"$\ell > 100$: < 0.2% difference" + "\n(acoustic peaks unaffected)",
             fontsize=7.5, color=SLATE, style='italic', fontfamily='serif',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                       edgecolor=LGRAY, alpha=0.85))
    ax1.set_xlabel(r"Multipole $\ell$", fontsize=11, fontfamily='serif')
    ax1.set_ylabel(r"$D_\ell^{TT}$ $[\mu\rm K^2]$", fontsize=11, fontfamily='serif')
    ax1.set_title(r"CMB Temperature Power Spectrum", fontsize=10,
                  fontweight='bold', color=NAVY, fontfamily='serif')
    ax1.set_xlim(2, 2500); ax1.set_ylim(0, 8200)
    ax1.legend(fontsize=9, framealpha=0.9)
    ax1.grid(True, alpha=0.3, lw=0.6)
    ax1.tick_params(labelsize=9)

    # ── Right: P(k)/P_ΛCDM ───────────────────────────────────────────────────
    ax2.set_facecolor(BG)
    k_data  = np.array([0.001, 0.010, 0.050, 0.100, 0.200, 0.500])
    Pr_data = np.array([25,    27,    18,    10,    4,     1])  # %

    k_plot  = np.logspace(-3, 0, 400)
    Pr_plot = np.clip(_pchip(np.log10(k_data), Pr_data, np.log10(k_plot)), 0, None)
    ax2.semilogx(k_plot, Pr_plot, color=BLUE, lw=2.5,
                 label="GRUT Correction #36")
    ax2.scatter(k_data, Pr_data, color=NAVY, s=55, zorder=6, label="Native Boltzmann values")

    ax2.axhline(3.22, color=RED, lw=1.8, ls='--',
                label=r"$\sigma_8$ enhancement +3.22%")
    ax2.fill_betweenx([0, 35], 0.1, 0.5, alpha=0.07, color=RED,
                      label=r"$\sigma_8$ scale ($k \sim 0.1$–$0.5\,h$/Mpc)")

    ax2.set_xlabel(r"$k$ [h/Mpc]", fontsize=11, fontfamily='serif')
    ax2.set_ylabel(r"$P^{\rm GRUT}/P^{\Lambda{\rm CDM}}-1$ [%]",
                   fontsize=11, fontfamily='serif')
    ax2.set_title(r"Matter Power Spectrum Enhancement (z=0)", fontsize=10,
                  fontweight='bold', color=NAVY, fontfamily='serif')
    ax2.set_xlim(1e-3, 1); ax2.set_ylim(-1, 35)
    ax2.legend(fontsize=8, framealpha=0.92, loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelsize=9)

    plt.tight_layout(pad=1.5)
    save(fig, "fig_14_cmb_pk.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 15 — MGCAMB Prototype Diagnostic (artifact record)
# ─────────────────────────────────────────────────────────────────────────────
def fig15_mgcamb_prototype():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8))
    fig.patch.set_facecolor('white')

    # ── Left: Prototype CMB D_ℓ showing artifact ─────────────────────────────
    ax1.set_facecolor(BG)
    ell_fine = np.linspace(2, 2500, 5000)

    def dl_lcdm(ell):
        envelope = 6000 * (ell / 200)**0.1 * np.exp(-ell / 2200)
        peaks  = (  np.exp(-((ell-220)/70)**2)  * 1.0
                  + np.exp(-((ell-540)/80)**2)  * 0.48
                  + np.exp(-((ell-810)/90)**2)  * 0.24
                  + np.exp(-((ell-1100)/100)**2)* 0.11)
        troughs= (  np.exp(-((ell-400)/70)**2) * 0.35
                  + np.exp(-((ell-680)/80)**2) * 0.18)
        base   = 5.5 * (ell*(ell+1)/(200*201))**0.04 * np.exp(-ell/2300)
        return envelope * (0.3 + peaks - 0.85*troughs) + base * 80

    dl = dl_lcdm(ell_fine)
    # Prototype artifact: 1.7–2.0× excess at ℓ=5–30
    dl_proto = dl.copy()
    artifact  = 1.0 + 0.85 * np.exp(-((np.log10(ell_fine+1) - np.log10(12))**2) / 0.25)
    dl_proto  = dl * np.where(ell_fine < 30, artifact, 1.0)

    ax1.plot(ell_fine, dl,       color=LGRAY, lw=2.0, ls='--', label=r"$\Lambda$CDM")
    ax1.plot(ell_fine, dl_proto, color=RED,   lw=1.8, label="GRUT MGCAMB Prototype",
             alpha=0.9)
    # Shade artifact region
    mask = ell_fine < 30
    ax1.fill_between(ell_fine[mask], dl[mask], dl_proto[mask],
                     alpha=0.3, color=RED, label="etak/z artifact")
    ax1.axvline(30, color=ORANGE, lw=1.2, ls=':', alpha=0.8)
    ax1.annotate("ARTIFACT\n(etak/z mismatch)\n×1.7–2.0 excess",
                 xy=(18, 4800), xytext=(200, 6700),
                 ha='left', va='top', fontsize=8, color=RED, fontweight='bold',
                 fontfamily='serif',
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.2),
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='#fff0f0',
                           edgecolor=RED, alpha=0.9))
    ax1.text(700, 3500, r"$\ell>100$: < 0.2%" + "\n(not artifact)", ha='center',
             fontsize=8, color=TEAL, fontfamily='serif', style='italic')
    ax1.text(0.97, 0.55,
             "Real signal (validated MGCAMB, Corr #38):\n~2.6$\\times$ low-$\\ell$ EXCESS $\\to$ linear branch RULED OUT",
             transform=ax1.transAxes, ha='right', va='top', fontsize=7.6,
             color='firebrick', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='mistyrose',
                       edgecolor='firebrick', alpha=0.9))
    ax1.set_xlabel(r"Multipole $\ell$", fontsize=11, fontfamily='serif')
    ax1.set_ylabel(r"$D_\ell^{TT}$ $[\mu\rm K^2]$", fontsize=11, fontfamily='serif')
    ax1.set_title("Prototype CMB — Artifact Diagnosis", fontsize=10,
                  fontweight='bold', color=NAVY, fontfamily='serif')
    ax1.set_xlim(2, 2500); ax1.set_ylim(0, 8200)
    ax1.legend(fontsize=8.5, framealpha=0.92, loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(labelsize=9)

    # ── Right: P(k) ratio — prototype vs corrected ────────────────────────────
    ax2.set_facecolor(BG)
    k_data   = np.array([0.003, 0.01,  0.05,  0.10, 0.20, 0.50])
    Pr_proto = np.array([48,    35,    20,    12,   7,    3])   # artifact
    Pr_corr  = np.array([27,    15,    10,    8.5,  5,    1])   # genuine

    k_plot = np.logspace(-3, -0.3, 400)
    ax2.semilogx(k_plot, np.clip(_pchip(np.log10(k_data), Pr_proto, np.log10(k_plot)), 0, None),
                 color=RED, lw=2.2, ls='-',  label="Prototype (artifact)")
    ax2.semilogx(k_plot, np.clip(_pchip(np.log10(k_data), Pr_corr, np.log10(k_plot)), 0, None),
                 color=BLUE, lw=2.2, ls='-', label="Corrected GRUT (+3.1%)")
    ax2.scatter(k_data, Pr_proto, color=RED,  s=50, zorder=6)
    ax2.scatter(k_data, Pr_corr,  color=BLUE, s=50, zorder=6)

    # Artifact annotation
    ax2.annotate("etak/z artifact\n(not physical)", xy=(0.003, 48),
                 xytext=(0.015, 44),
                 arrowprops=dict(arrowstyle='->', color=RED, lw=1.2),
                 fontsize=8, color=RED, fontfamily='serif')
    ax2.axhline(3.22, color=BLUE, lw=1.2, ls=':', alpha=0.7)
    ax2.text(0.1, 3.8, r"$\sigma_8$ +3.22%", fontsize=8, color=BLUE,
             fontfamily='serif')
    ax2.text(0.93, 0.04, "NOT physical GRUT predictions\n(prototype diagnostic only)",
             transform=ax2.transAxes, ha='right', va='bottom',
             fontsize=7.5, color=RED, style='italic', fontfamily='serif',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#fff0f0',
                       edgecolor=RED, alpha=0.85))
    ax2.set_xlabel(r"$k$ [h/Mpc]", fontsize=11, fontfamily='serif')
    ax2.set_ylabel(r"$P^{\rm GRUT}/P^{\Lambda{\rm CDM}}-1$ [%]",
                   fontsize=11, fontfamily='serif')
    ax2.set_title("P(k) Enhancement — Prototype vs. Corrected", fontsize=10,
                  fontweight='bold', color=NAVY, fontfamily='serif')
    ax2.set_xlim(1e-3, 0.7); ax2.set_ylim(-2, 60)
    ax2.legend(fontsize=9, framealpha=0.92)
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelsize=9)

    plt.tight_layout(pad=1.5)
    save(fig, "fig_15_mgcamb_prototype.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 17 — Open Question Dependency Ledger
# ─────────────────────────────────────────────────────────────────────────────
def fig17_open_ledger():
    # Single-line labels only (no \n in descriptions)
    items = [
        # (label,                                       status,    effort,       chapter)
        ("Nonlinear gravity ladder (rungs 5–8)",        "open",   "multi-year",   6),
        ("TJI Euler-channel [2F1]^3 epsilon-expansion", "open",   "1–2 wks",      7),
        ("Constitutive matter-gravity closure (action)","open",   "weeks",         9),
        ("N-body nonlinear structure (v5 gate)",        "open",   "months",        9),
        ("Full CLASS Boltzmann injection",              "open",   "4–8 wks",       9),
        ("El Gordo tension (observational)",            "open",   "observ.",        9),
        ("8pi normalisation origin",                   "open",   "weeks",           7),
        ("Full SM Yukawa/CKM/PMNS closure",            "open",   "years",          10),
        ("tau_0 – tau_micro derivation gap",           "resolved","Option B",      14),
        ("Allen-Jacobson S^4 propagator (Phase 1)",    "resolved","Done",          12),
        ("n_g(omega) cosmological covariance",         "resolved","Corr. #26",      9),
        ("Phi_munu linearised derivation",             "resolved","Corr. #23",      6),
        ("T_c provenance inconsistency",               "resolved","Corr. #22",     14),
        ("V4 matrix calibration diagnostic",           "resolved","Corr. #32",      7),
        ("Z3 coupling a_nu = 1 uniqueness",            "resolved","Corr. #29",     10),
    ]

    STATUS_COL = {"open": ORANGE, "resolved": GREEN}
    effort_width = {
        "Done":1, "Option B":1,
        "Corr. #22":1, "Corr. #23":1, "Corr. #26":1, "Corr. #29":1, "Corr. #32":1,
        "1–2 wks":2, "weeks":2, "4–8 wks":2,
        "observ.":3, "months":3,
        "multi-year":5, "years":5,
    }
    effort_order = {k: i for i, k in enumerate(
        ["Done","Option B","Corr. #22","Corr. #23","Corr. #26","Corr. #29","Corr. #32",
         "1–2 wks","weeks","4–8 wks","observ.","months","multi-year","years"])}

    items_sorted = sorted(items, key=lambda x: (
        0 if x[1] == 'open' else 1, effort_order.get(x[2], 10)))

    labels   = [x[0] for x in items_sorted]
    statuses = [x[1] for x in items_sorted]
    efforts  = [x[2] for x in items_sorted]
    chapters = [x[3] for x in items_sorted]
    n = len(labels)

    # --- Layout: label area on left, bars in middle, ch+effort on right -----
    # xlim: -8.5 to 6.5  (8.5 units for labels, 6.5 for bars + tags)
    fig, ax = plt.subplots(figsize=(12, 7.0))
    fig.patch.set_facecolor('white')
    ax.set_facecolor(BG)

    widths = [effort_width.get(e, 3) for e in efforts]
    bar_colors = [STATUS_COL.get(s, GRAY) for s in statuses]
    ys = np.arange(n)

    ax.barh(ys, widths, color=bar_colors, alpha=0.75,
            edgecolor=NAVY, linewidth=0.8, height=0.68)

    # Left labels (description)
    for i, lbl in enumerate(labels):
        ax.text(-0.15, i, lbl, ha='right', va='center', fontsize=8.5,
                color=NAVY, fontfamily='serif')

    # Right of bar: effort label (only if bar < 4.5 so it doesn't push out)
    for i, (eff, w, st) in enumerate(zip(efforts, widths, statuses)):
        x_eff = min(w + 0.12, 4.6)
        ax.text(x_eff, i, eff, ha='left', va='center', fontsize=8,
                color=STATUS_COL.get(st, GRAY), fontfamily='serif', style='italic')

    # Chapter tags at fixed right margin (5.9)
    for i, ch in enumerate(chapters):
        ax.text(5.75, i, f"Ch {ch}", ha='left', va='center', fontsize=8,
                color=SLATE, fontfamily='serif')

    # Open / resolved divider
    n_open = sum(1 for s in statuses if s == 'open')
    ax.axhline(n_open - 0.5, color=LGRAY, lw=1.2, ls='--', alpha=0.8)
    ax.text(-8.4, n_open - 0.5,
            "▲ resolved  /  open ▼",
            ha='left', va='center', fontsize=8, color=SLATE, style='italic',
            fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=LGRAY, alpha=0.9))

    ax.set_xlim(-8.5, 6.5)
    ax.set_ylim(-0.9, n - 0.1)
    ax.set_xlabel("Relative effort horizon  →", fontsize=10, fontfamily='serif')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(["Done /\nCorrected", "~Weeks", "Months",
                         "Multi-year", "Decades"], fontsize=8.5)
    ax.set_yticks([])
    ax.set_title("GRUT Open Questions — Status and Effort Horizon (v2.2, June 2026)",
                 fontsize=12, fontweight='bold', color=NAVY, fontfamily='serif')
    ax.grid(axis='x', alpha=0.3, lw=0.6)

    legend_patches = [
        mpatches.Patch(facecolor=ORANGE, edgecolor=NAVY, alpha=0.8, label="Open"),
        mpatches.Patch(facecolor=GREEN,  edgecolor=NAVY, alpha=0.8, label="Resolved"),
    ]
    ax.legend(handles=legend_patches, fontsize=9.5, loc='lower right', framealpha=0.92)
    plt.tight_layout(pad=1.0)
    save(fig, "fig_17_open_ledger.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 16 — Schrödinger-in-the-Box: Standard vs GRUT Inversion
# ─────────────────────────────────────────────────────────────────────────────
def fig16_schrodinger():
    """Two-panel comparison: Standard formulation vs GRUT inversion of the cat paradox."""
    FW, FH = 14, 8.5
    fig = plt.figure(figsize=(FW, FH), facecolor='white')
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW); ax.set_ylim(0, FH); ax.axis('off')

    NAVY  = '#1B3A6B'; SLATE = '#2C3E50'; TEAL  = '#1A5276'
    RED   = '#7B241C'; GRN   = '#1E6B45'
    LRED  = '#FADBD8'; LGN   = '#D5F0E3'; LBLUE = '#EBF5FB'
    GRAY  = '#444444'; LGRAY = '#AAAAAA'; W = 'white'

    def rbox(cx, cy, w, h, fc, ec, txt, fs=9, tc=W, lw=1.5, bold=False,
             pad=0.1, ls='-', zo=3, ha='center', va='center'):
        p = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                            boxstyle=f'round,pad={pad}',
                            fc=fc, ec=ec, lw=lw, ls=ls, zorder=zo)
        ax.add_patch(p)
        ax.text(cx, cy, txt, ha=ha, va=va, fontsize=fs, color=tc,
                fontweight='bold' if bold else 'normal',
                zorder=zo+1, linespacing=1.55)

    def seg(x1,y1,x2,y2, c=GRAY, lw=1.4, ls='-'):
        ax.plot([x1,x2],[y1,y2], c=c, lw=lw, ls=ls, zorder=2,
                solid_capstyle='round')

    def arw(x, y_tip, c=GRAY, lw=1.5, sz=12):
        ax.annotate('', xy=(x, y_tip), xytext=(x, y_tip+0.35),
                    arrowprops=dict(arrowstyle='->', color=c, lw=lw,
                                    mutation_scale=sz), zorder=5)

    # ── Panel divider ──────────────────────────────────────────────────────────
    XD = FW / 2    # divider x
    seg(XD, 0.3, XD, FH-0.3, c=LGRAY, lw=1.0, ls='--')

    # ── Column headers ─────────────────────────────────────────────────────────
    for cx, lbl, fc in [(XD/2, 'STANDARD FORMULATION', RED),
                         (XD + XD/2, 'GRUT INVERSION', GRN)]:
        ax.text(cx, FH-0.45, lbl, ha='center', va='center', fontsize=15,
                color=fc, fontweight='bold', fontfamily='monospace')
        seg(cx - 2.4, FH-0.65, cx + 2.4, FH-0.65, c=fc, lw=1.5)

    # ══════════════════════════════════════════════════════════════════════════
    # LEFT panel — Standard formulation
    # ══════════════════════════════════════════════════════════════════════════
    XL = XD / 2    # left panel centre

    # Observer (outside)
    rbox(XL, FH-1.45, 2.6, 0.66, RED, RED, 'OBSERVER', fs=14, bold=True)

    # Arrow down with label
    seg(XL, FH-1.75, XL, FH-2.30, c=GRAY)
    arw(XL, FH-2.30)
    ax.text(XL+0.12, FH-2.05, '"is the cat alive?"', ha='left', va='center',
            fontsize=12, color=GRAY, style='italic')

    # Box (containing superposed cat)
    rbox(XL, 3.35, 3.6, 2.50, LRED, RED, '', lw=1.8, zo=2)
    ax.text(XL, 4.55, 'BOX', ha='center', va='center', fontsize=12.5,
            color=RED, fontweight='bold', zorder=3)
    rbox(XL, 3.20, 3.0, 1.40, '#FEF9F9', RED,
         'CAT:\nalive or dead?\n(superposed?)',
         fs=12, tc=SLATE, lw=1.0, zo=4, pad=0.12)

    # Caption below
    ax.text(XL, 1.45,
            'The observer collapses\nthe wavefunction.\n'
            'Where is the line?\n(Copenhagen: unknown)',
            ha='center', va='center', fontsize=11.5, color=GRAY,
            linespacing=1.6)

    # ══════════════════════════════════════════════════════════════════════════
    # RIGHT panel — GRUT inversion
    # ══════════════════════════════════════════════════════════════════════════
    XR = XD + XD/2    # right panel centre

    # Outer box (the universe / the medium)
    rbox(XR, 4.10, 5.2, 3.30, LBLUE, GRN, '', lw=2.0, zo=2, ls='-')
    ax.text(XR - 2.2, 5.60, 'BOX', ha='left', va='center', fontsize=12.5,
            color=GRN, fontweight='bold', zorder=3)

    # CAT node
    rbox(XR - 1.15, 4.35, 1.85, 1.00, LGN, GRN,
         r'CAT' + '\n' + r'$X \sim 10^{7}$',
         fs=12.5, tc=SLATE, lw=1.2, zo=4)

    # OBSERVER node
    rbox(XR + 1.15, 4.35, 1.85, 1.00, LGN, GRN,
         r'OBSERVER' + '\n' + r'$X \sim 10^{35}$',
         fs=12.5, tc=SLATE, lw=1.2, zo=4)

    # "Both already crystallized" label
    ax.text(XR, 3.05,
            'Both already crystallized.\nNo outside observer needed.',
            ha='center', va='center', fontsize=12.5, color=SLATE,
            fontweight='bold', linespacing=1.5, zorder=5)

    # Caption below
    ax.text(XR, 1.45,
            'The "paradox" assumes an\noutside vantage point.\n'
            r'There is no such point.' + '\n'
            r'The line is $\Lambda_{\rm grav} \times t = 1$.' + '\n'
            '(GRUT: computed)',
            ha='center', va='center', fontsize=11.5, color=GRAY,
            linespacing=1.6)

    # ── Bottom note (expanded explanation) ────────────────────────────────────
    ax.text(FW/2, 0.55,
            r'$X = \Lambda_{\rm grav}\,\tau_0$: crystallisation parameter (gravitational memory cycles).  '
            r'Crystal ($X \gg 1$): classical definite state.  '
            r'Boundary ($X \approx 1$): decoherence plateau $\sim$689 Hz (Falsifier F1).',
            ha='center', va='center', fontsize=10.5, color=GRAY, style='italic',
            linespacing=1.5)
    ax.text(FW/2, 0.18,
            r'Cat: $X \sim 10^{7}$.  Observer: $X \sim 10^{35}$.  Both are definite classical states — '
            'Copenhagen’s “line” is not a mystery: '
            r'it is $\Lambda_{\rm grav} \times t = 1$, computable from $\tau_0$.',
            ha='center', va='bottom', fontsize=10.5, color=GRAY, style='italic',
            linespacing=1.5)

    save(fig, "fig_16_schrodinger.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 1 — GRUT Derivation Chain
# ─────────────────────────────────────────────────────────────────────────────
def fig01_grut_chain():
    """Professional derivation-chain diagram: S_CTP → kernels → n_g(ω) → 4 regimes."""
    FW, FH = 16, 11.5            # data-coordinate extent (layout is hardcoded to this)
    # Render the canvas physically smaller than the data extent so that the
    # fixed point-size fonts occupy more of the page when the PNG is scaled to
    # the PDF content column — enlarges apparent text without touching layout.
    SCALE = 0.82
    fig = plt.figure(figsize=(FW * SCALE, FH * SCALE), facecolor='white')
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW); ax.set_ylim(0, FH); ax.axis('off')

    # Palette
    _NAVY  = '#1B3A6B'; _BLUE  = '#2471A3'; _TEAL  = '#1A5276'
    _GRN   = '#1E6B45'; _ORG   = '#883800'; _PUR   = '#5B2C8D'; _STE  = '#2C3E50'
    _LG    = '#D5F0E3'; _LO    = '#FDE8C8'; _LP    = '#EAD5F5'; _LS   = '#D0E8F0'
    _LBLUE = '#D4E9F7'; _GRAY  = '#444444'; _LGRAY = '#999999'; _W    = 'white'

    def rbox(cx, cy, w, h, fc, ec, txt, fs=11, tc=_W, lw=1.5,
             bold=False, pad=0.1, ls='-', zo=3):
        p = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                            boxstyle=f'round,pad={pad}',
                            fc=fc, ec=ec, lw=lw, ls=ls, zorder=zo)
        ax.add_patch(p)
        ax.text(cx, cy, txt, ha='center', va='center', fontsize=fs,
                color=tc, fontweight='bold' if bold else 'normal',
                zorder=zo+1, linespacing=1.6)

    def seg(x1, y1, x2, y2, c=_GRAY, lw=1.6, ls='-'):
        ax.plot([x1,x2],[y1,y2], c=c, lw=lw, ls=ls, zorder=2,
                solid_capstyle='round', solid_joinstyle='round')

    def arw(x, y_tip, c=_GRAY, lw=1.6):
        ax.annotate('', xy=(x, y_tip), xytext=(x, y_tip+0.28),
                    arrowprops=dict(arrowstyle='->', color=c, lw=lw,
                                    mutation_scale=14), zorder=5)

    # ── Geometry — 4 equal columns ──────────────────────────────────────────
    # Columns equally spaced: centers at XL, each COL_W wide, gap ~0.53 between
    COL_W = 2.9
    XL    = [3.0, 6.33, 9.67, 13.0]   # left to right: Crystal, Boundary, Fluid, Fourier
    XC    = 8.0                         # diagram centre
    XNG   = 4.0                         # noise-kernel box centre
    XKR   = 12.0                        # retarded-kernel box centre

    # Vertical landmarks (top → bottom)
    YT   = 10.75   # S_CTP centre
    YK   =  8.85   # kernel-box centres
    YKC  =  7.72   # constants text centre
    YMER =  7.12   # horizontal merge line
    YN   =  6.00   # n_g(ω) box centre
    YR   =  4.45   # regime-header centres
    YB   =  2.35   # regime-body centres
    BOX_H = 2.85   # regime-body height

    # ── S_CTP header ────────────────────────────────────────────────────────
    rbox(XC, YT, 15.6, 0.90, _NAVY, _NAVY,
         r'$S_{\mathrm{CTP}}$'
         r'   ·   §3 — density-matrix path integral over gravitational environment',
         fs=14.5, bold=True)

    # ── Trunk → T-junction to kernels ───────────────────────────────────────
    seg(XC, YT-0.45, XC, YT-0.68)
    seg(XNG, YT-0.68, XKR, YT-0.68)
    seg(XNG, YT-0.68, XNG, YK+0.58)
    seg(XKR, YT-0.68, XKR, YK+0.58)

    # ── Kernel section background ────────────────────────────────────────────
    kbg = FancyBboxPatch((0.55, YMER-0.08), 14.90, 2.50,
                          boxstyle='round,pad=0.08',
                          fc=_LBLUE, ec=_BLUE, lw=1.1, ls=(0,(6,3)), zorder=1, alpha=0.35)
    ax.add_patch(kbg)

    # ── Kernel boxes ─────────────────────────────────────────────────────────
    rbox(XNG, YK, 5.8, 1.10, _BLUE, _BLUE,
         r'$N_{\mathrm{grav}}(x,\,x^{\prime})$'
         '\n' r'$G\,/\,(\hbar\,|\,x - x^{\prime}|)$'
         '\n(noise kernel)', fs=13.5)
    rbox(XKR, YK, 5.8, 1.10, _BLUE, _BLUE,
         r'$K^{R}(t)$'
         '\n' r'$\tau_0^{-1}\,\exp(-t/\tau_0)$'
         '\n(retarded kernel)', fs=13.5)

    # ── Anchored constants (centred, between kernels and n_g) ────────────────
    ax.text(XC, YKC+0.16,
            r'$\tau_0 = 41.9\,\mathrm{Myr}$'
            r'   $\leftarrow$   cosmic-baseline anchor',
            ha='center', va='center', fontsize=13, color=_GRAY, style='italic')
    ax.text(XC, YKC-0.20,
            r'$\alpha_\mathrm{vac} = 1/3$'
            r'   $\leftarrow$   Gate R  (Duff 1994, $a/c = 1/3$)',
            ha='center', va='center', fontsize=13, color=_GRAY, style='italic')

    # ── Convergence lines → n_g ──────────────────────────────────────────────
    seg(XNG, YK-0.55, XNG, YMER)
    seg(XKR, YK-0.55, XKR, YMER)
    seg(XNG, YMER, XKR, YMER)
    seg(XC, YMER, XC, YN+0.48)
    arw(XC, YN+0.48)

    # ── n_g(ω) box ───────────────────────────────────────────────────────────
    rbox(XC, YN, 7.2, 0.88, _TEAL, _TEAL,
         r'$n_g(\omega)\;=\;\sqrt{\;1 + '
         r'\dfrac{\alpha_\mathrm{vac}}{1+(\omega\tau_0)^{2}}\;}$',
         fs=16.5)

    # ── Fan to 4 regime columns ──────────────────────────────────────────────
    seg(XC, YN-0.44, XC, YN-0.72)
    seg(XL[0], YN-0.72, XL[3], YN-0.72)
    for xl in XL:
        seg(xl, YN-0.72, xl, YR+0.48)
        arw(xl, YR+0.47)

    # ── Regime headers ────────────────────────────────────────────────────────
    for xl, fc, lbl in [
        (XL[0], _GRN, r'$X \gg 1$'     + '\nCrystal'),
        (XL[1], _ORG, r'$X \approx 1$' + '\nBoundary'),
        (XL[2], _PUR, r'$X \ll 1$'     + '\nFluid'),
        (XL[3], _STE, r'$\mu(k,\,a)$'  + '\nFourier'),
    ]:
        rbox(xl, YR, COL_W, 0.84, fc, fc, lbl, fs=15, bold=True, pad=0.09)

    # ── Regime bodies ─────────────────────────────────────────────────────────
    for xl, fc, ec, body in [
        (XL[0], _LG, '#1a5c3a',
         'GR (exact)\n\nGPS · LIGO\nsolar system'),
        (XL[1], _LO, '#7a3000',
         'Decoherence plateau\n~689 Hz\n(primary falsifier)\n\n'
         'Isotope discriminator\nBMV entanglement'),
        (XL[2], _LP, '#4a1a7a',
         r'$\Omega_\mathrm{dm} = \alpha = 1/3$' + '\n'
         r'$\Omega_\Lambda = 0.689$' + '\n'
         r'$H_0 \approx 69\;\mathrm{km\,s^{-1}Mpc^{-1}}$' + '\n'
         r'Baryogenesis' + '\n'
         r'$\eta_B = 6.56\!\times\!10^{-10}$'),
        (XL[3], _LS, '#1a3a4a',
         r'$P(k),\;\sigma_8$' + '\n'
         r'$\mu - 1 = 1/3$' + '\n\n'
         'DESI · Euclid'),
    ]:
        rbox(xl, YB, COL_W, BOX_H, fc, ec, body,
             fs=13, tc='#111111', lw=1.0, pad=0.15, zo=3)
        seg(xl, YR-0.42, xl, YB+BOX_H/2, c=_LGRAY, lw=0.9)

    # ── Footer ────────────────────────────────────────────────────────────────
    ax.text(XC, 0.30,
            r'All sectoral predictions share zero adjustable parameters beyond '
            r'$\tau_0$ (cosmic-baseline anchor) '
            r'and $\alpha_\mathrm{vac} = 1/3$ (Gate R — derived, not fitted)',
            ha='center', va='bottom', fontsize=12, color=_GRAY, style='italic')

    save(fig, "fig_01_grut_chain.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 5 — H(z) Observational Comparison
# ─────────────────────────────────────────────────────────────────────────────
def fig05_hz_residuals():
    """Two-panel H(z) comparison: GRUT zero-parameter curve vs CC + BAO data.

    Top panel: H(z) vs z — GRUT curve, Planck ΛCDM reference, error-bar data.
    Bottom panel: signed residuals (H_model − H_obs) / σ for each point.
    """

    # ── Cosmological parameters ───────────────────────────────────────────────
    H0_GRUT   = 69.029;  Om_GRUT = 0.2900;  OL_GRUT = 0.7100
    H0_PLANCK = 67.360;  Om_PL   = 0.3153;  OL_PL   = 0.6847
    H_INF     = 58.164   # km/s/Mpc  (structural identity H₀√Ω_Λ)

    def Ez(z, Om, OL):
        return np.sqrt(Om * (1.0 + z)**3 + OL)

    # ── Observational data — Moresco+2022 gold-sample + Borghi+2022 ──────────
    # (z, H_obs, sigma_H, tracer)  — 32 CC + 1 BAO = 33 points
    DATA = [
        (0.07,   69.0,  19.6, "CC"),   # Zhang+2014
        (0.09,   69.0,  12.0, "CC"),   # Jimenez+2003
        (0.12,   68.6,  26.2, "CC"),   # Zhang+2014
        (0.17,   83.0,   8.0, "CC"),   # Simon+2005
        (0.1791, 75.0,   4.0, "CC"),   # Moresco+2012
        (0.1993, 75.0,   5.0, "CC"),   # Moresco+2012
        (0.20,   72.9,  29.6, "CC"),   # Zhang+2014
        (0.27,   77.0,  14.0, "CC"),   # Simon+2005
        (0.28,   88.8,  36.6, "CC"),   # Zhang+2014
        (0.3519, 83.0,  14.0, "CC"),   # Moresco+2012
        (0.3802, 83.0,  13.5, "CC"),   # Moresco+2016
        (0.40,   95.0,  17.0, "CC"),   # Simon+2005
        (0.4004, 77.0,  10.2, "CC"),   # Moresco+2016
        (0.4247, 87.1,  11.2, "CC"),   # Moresco+2016
        (0.4497, 92.8,  12.9, "CC"),   # Moresco+2016
        (0.47,   89.0,  49.6, "CC"),   # Ratsimbazafy+2017
        (0.4783, 80.9,   9.0, "CC"),   # Moresco+2016
        (0.48,   97.0,  62.0, "CC"),   # Stern+2010
        (0.5929,104.0,  13.0, "CC"),   # Moresco+2012
        (0.6797, 92.0,   8.0, "CC"),   # Moresco+2012
        (0.75,   98.8,  33.6, "CC"),   # Borghi+2022
        (0.7812,105.0,  12.0, "CC"),   # Moresco+2012
        (0.8754,125.0,  17.0, "CC"),   # Moresco+2012
        (0.88,   90.0,  40.0, "CC"),   # Stern+2010
        (0.90,  117.0,  23.0, "CC"),   # Simon+2005
        (1.037, 154.0,  20.0, "CC"),   # Moresco+2012
        (1.30,  168.0,  17.0, "CC"),   # Simon+2005
        (1.363, 160.0,  33.6, "CC"),   # Moresco+2015
        (1.43,  177.0,  18.0, "CC"),   # Simon+2005
        (1.53,  140.0,  14.0, "CC"),   # Simon+2005
        (1.75,  202.0,  40.0, "CC"),   # Stern+2010
        (1.965, 186.5,  50.4, "CC"),   # Moresco+2015
        (2.34,  222.0,   7.0, "BAO"),  # Delubac+2015 Ly-α BOSS
    ]

    z_cc  = np.array([d[0] for d in DATA if d[3] == "CC"])
    H_cc  = np.array([d[1] for d in DATA if d[3] == "CC"])
    e_cc  = np.array([d[2] for d in DATA if d[3] == "CC"])
    z_bao = np.array([d[0] for d in DATA if d[3] == "BAO"])
    H_bao = np.array([d[1] for d in DATA if d[3] == "BAO"])
    e_bao = np.array([d[2] for d in DATA if d[3] == "BAO"])

    # Residuals in σ:  (H_model − H_obs) / sigma
    res_cc  = (H0_GRUT * Ez(z_cc,  Om_GRUT, OL_GRUT) - H_cc)  / e_cc
    res_bao = (H0_GRUT * Ez(z_bao, Om_GRUT, OL_GRUT) - H_bao) / e_bao

    # ── Smooth curves ─────────────────────────────────────────────────────────
    zz = np.linspace(0.0, 2.55, 400)
    Hz_grut  = H0_GRUT  * Ez(zz, Om_GRUT, OL_GRUT)
    Hz_planck = H0_PLANCK * Ez(zz, Om_PL,   OL_PL)

    # ── Layout ────────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(9, 7.5), facecolor='white')
    gs  = fig.add_gridspec(2, 1, height_ratios=[2.6, 1.0],
                           hspace=0.06, left=0.10, right=0.95,
                           top=0.92, bottom=0.09)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1], sharex=ax_top)

    for ax in (ax_top, ax_bot):
        ax.set_facecolor(BG)
        ax.grid(True, alpha=0.25, lw=0.6)
        ax.tick_params(labelsize=9)

    plt.setp(ax_top.get_xticklabels(), visible=False)

    # ── Top panel — H(z) ─────────────────────────────────────────────────────
    ax_top.plot(zz, Hz_grut,  color=NAVY,  lw=2.4, zorder=4,
                label=r"GRUT  ($H_0\!=\!69.0,\;\Omega_m\!=\!0.290$) — zero free parameters")
    ax_top.plot(zz, Hz_planck, color=GRAY, lw=1.6, ls='--', zorder=3,
                label=r"Planck $\Lambda$CDM  ($H_0\!=\!67.36,\;\Omega_m\!=\!0.315$) — fitted")

    # H_inf asymptote annotation
    ax_top.axhline(H_INF, color=TEAL, lw=0.9, ls=(0, (4, 4)), zorder=2, alpha=0.7)
    ax_top.text(2.42, H_INF + 3.5,
                r"$H_\infty = H_0\sqrt{\Omega_\Lambda} = 58.16$",
                fontsize=7.5, color=TEAL, ha='right', va='bottom',
                fontfamily='serif', style='italic')

    # CC points — smaller markers for the denser 32-point cloud
    ax_top.errorbar(z_cc, H_cc, yerr=e_cc,
                    fmt='o', color=BLUE, ms=5, lw=1.4,
                    capsize=3, ecolor=BLUE, elinewidth=1.2, zorder=5,
                    label="Cosmic Chronometers (CC, N=32) — calibration-independent")

    # BAO points
    ax_top.errorbar(z_bao, H_bao, yerr=e_bao,
                    fmt='^', color=ORANGE, ms=8, lw=1.8,
                    capsize=4, ecolor=ORANGE, elinewidth=1.5, zorder=5,
                    label="BAO (Delubac+2015 Ly-α) — sound-horizon calibrated")

    ax_top.set_ylabel(r"$H(z)$  [km s$^{-1}$ Mpc$^{-1}$]",
                      fontsize=11, fontfamily='serif')
    ax_top.set_ylim(40, 310)
    ax_top.set_xlim(-0.05, 2.55)
    ax_top.legend(fontsize=7.8, loc='upper left', framealpha=0.93,
                  handlelength=2.2)

    # Stats annotation box
    stats_txt = (
        "CC only (N = 32, calibration-independent)\n"
        r"GRUT:   $\chi^2/N = 0.465$,  RMS $= 0.68\sigma$  (zero free parameters)" + "\n"
        r"Planck: $\chi^2/N = 0.466$,  RMS $= 0.68\sigma$  (MCMC-fitted)"
    )
    ax_top.text(0.985, 0.04, stats_txt,
                transform=ax_top.transAxes, ha='right', va='bottom',
                fontsize=8, color=SLATE, fontfamily='serif',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                          edgecolor=LGRAY, alpha=0.92))

    ax_top.set_title(
        r"GRUT first-principles $H(z)$ vs Moresco+2022 cosmic chronometers",
        fontsize=11, fontweight='bold', color=NAVY, fontfamily='serif', pad=8)

    # ── Bottom panel — residuals ──────────────────────────────────────────────
    ax_bot.axhline(0.0, color=NAVY, lw=1.2, zorder=4)

    # ±1σ and ±2σ bands
    ax_bot.fill_between([-0.05, 2.55], -1, 1, alpha=0.10, color=BLUE, zorder=1)
    ax_bot.fill_between([-0.05, 2.55], -2, 2, alpha=0.06, color=BLUE, zorder=1)
    ax_bot.axhline( 1.0, color=BLUE, lw=0.6, ls=':', alpha=0.5)
    ax_bot.axhline(-1.0, color=BLUE, lw=0.6, ls=':', alpha=0.5)
    ax_bot.axhline( 2.0, color=BLUE, lw=0.5, ls=':', alpha=0.35)
    ax_bot.axhline(-2.0, color=BLUE, lw=0.5, ls=':', alpha=0.35)

    # ±1σ / ±2σ labels
    for y, lbl in [(1.0, r"$+1\sigma$"), (-1.0, r"$-1\sigma$"),
                   (2.0, r"$+2\sigma$"), (-2.0, r"$-2\sigma$")]:
        ax_bot.text(2.52, y, lbl, fontsize=7, color=BLUE, va='center',
                    ha='right', fontfamily='serif', alpha=0.7)

    # CC residuals — smaller markers to avoid overlap at z < 0.5
    ax_bot.errorbar(z_cc, res_cc, yerr=np.ones_like(res_cc),
                    fmt='o', color=BLUE, ms=5, lw=1.4,
                    capsize=3, ecolor=BLUE, elinewidth=1.0, zorder=5,
                    label="CC (32 points)")

    # BAO residual (slightly faded — calibration caveat)
    ax_bot.errorbar(z_bao, res_bao, yerr=np.ones_like(res_bao),
                    fmt='^', color=ORANGE, ms=8, lw=1.6,
                    capsize=3, ecolor=ORANGE, elinewidth=1.2,
                    alpha=0.75, zorder=5, label="BAO (Ly-α)")

    # BAO caveat
    ax_bot.text(0.015, 0.08,
                "BAO residual includes ~2.4% systematic\n"
                "from Planck-calibrated sound horizon",
                transform=ax_bot.transAxes, fontsize=7.2,
                color=ORANGE, ha='left', va='bottom', fontfamily='serif',
                style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=ORANGE, alpha=0.7, lw=0.7))

    ax_bot.set_ylabel(r"$(H_{\rm model} - H_{\rm obs})\,/\,\sigma$",
                      fontsize=9.5, fontfamily='serif')
    ax_bot.set_xlabel(r"Redshift  $z$",
                      fontsize=11, fontfamily='serif')
    ax_bot.set_ylim(-3.2, 3.2)
    ax_bot.legend(fontsize=8, loc='upper right', framealpha=0.9)

    # Minor x ticks
    ax_bot.set_xticks(np.arange(0, 2.6, 0.5))

    save(fig, "fig_05_hz_residuals.png")


def fig06_fsigma8():
    """Two-panel fσ₈(z) comparison: GRUT modified-gravity vs RSD observations.

    Top panel: fσ₈(z) vs z — GRUT (k=0.05 Mpc⁻¹), Planck ΛCDM, survey data.
    Bottom panel: signed residuals (fσ₈_GRUT − obs) / σ for each measurement.
    """
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))

    from grut.derived.cosmology.fsigma8_growth import (
        RSD_DATA, grut_fsigma8, lcdm_fsigma8,
        grut_fsigma8_large_scale,
        GRUT_SIGMA8, PLANCK_SIGMA8, GRUT_K_RSD, fsigma8_comparison,
    )

    # ── Data arrays ───────────────────────────────────────────────────────────
    z_obs   = np.array([p.z_eff   for p in RSD_DATA])
    fs8_obs = np.array([p.fsigma8 for p in RSD_DATA])
    sig_obs = np.array([p.sigma   for p in RSD_DATA])

    # Survey tags for marker styles
    surveys = {p.reference for p in RSD_DATA}
    # group by survey family
    def survey_key(ref):
        if "Alam"        in ref: return "BOSS DR12"
        if "Blake+2012"  in ref: return "WiggleZ 2012"
        if "Blake+2011"  in ref: return "WiggleZ 2011"
        if "Beutler"     in ref: return "6dFGRS"
        if "Howlett"     in ref: return "SDSS MGS"
        if "de la Torre" in ref: return "VIPERS"
        if "Okumura"     in ref: return "FastSound"
        return "Other"

    survey_data = {}
    for p in RSD_DATA:
        k = survey_key(p.reference)
        survey_data.setdefault(k, []).append(p)

    # ── Smooth prediction curves ──────────────────────────────────────────────
    zz = np.linspace(0.0, 1.55, 400)
    fs8_grut   = grut_fsigma8(zz)
    fs8_lcdm   = lcdm_fsigma8(zz)

    # Residuals for GRUT (k=0.05)
    fs8_grut_obs = grut_fsigma8(z_obs)
    res_grut = (fs8_grut_obs - fs8_obs) / sig_obs

    # Comparison stats
    cmp = fsigma8_comparison()
    chi2_grut = cmp["chi2_N_grut"]
    chi2_lcdm = cmp["chi2_N_lcdm"]

    # ── Layout ────────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(9, 7.5), facecolor='white')
    gs  = fig.add_gridspec(2, 1, height_ratios=[2.6, 1.0],
                           hspace=0.06, left=0.10, right=0.95,
                           top=0.92, bottom=0.09)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1], sharex=ax_top)

    for ax in (ax_top, ax_bot):
        ax.set_facecolor(BG)
        ax.grid(True, alpha=0.25, lw=0.6)
        ax.tick_params(labelsize=9)

    plt.setp(ax_top.get_xticklabels(), visible=False)

    # ── Top panel — fσ₈(z) ───────────────────────────────────────────────────
    ax_top.plot(zz, fs8_grut, color=NAVY, lw=2.4, zorder=4,
                label=fr"GRUT  ($\sigma_8\!=\!{GRUT_SIGMA8}$, $k\!=\!{GRUT_K_RSD}\,\mathrm{{Mpc}}^{{-1}}$, zero free parameters)")
    ax_top.plot(zz, fs8_lcdm, color=GRAY, lw=1.6, ls='--', zorder=3,
                label=fr"Planck $\Lambda$CDM  ($\sigma_8\!=\!{PLANCK_SIGMA8}$) — fitted")

    # Survey scatter markers
    marker_styles = {
        "BOSS DR12":    dict(marker='D', color=ORANGE,  ms=7,  zorder=6),
        "WiggleZ 2012": dict(marker='o', color=GREEN,   ms=6,  zorder=5),
        "WiggleZ 2011": dict(marker='s', color='#8E44AD', ms=6, zorder=5),
        "6dFGRS":       dict(marker='^', color='#E74C3C', ms=7,  zorder=6),
        "SDSS MGS":     dict(marker='v', color='#2980B9', ms=6,  zorder=5),
        "VIPERS":       dict(marker='p', color='#C0392B', ms=7,  zorder=5),
        "FastSound":    dict(marker='*', color='#117A65', ms=9,  zorder=6),
        "Other":        dict(marker='o', color=GRAY,    ms=5,  zorder=4),
    }

    for survey, pts in sorted(survey_data.items()):
        zp = np.array([p.z_eff   for p in pts])
        yp = np.array([p.fsigma8 for p in pts])
        ep = np.array([p.sigma   for p in pts])
        st = marker_styles.get(survey, marker_styles["Other"])
        ax_top.errorbar(zp, yp, yerr=ep,
                        fmt=st['marker'], color=st['color'],
                        ms=st['ms'], capsize=3, lw=0.9, elinewidth=0.8,
                        zorder=st['zorder'], label=survey)

    ax_top.set_ylabel(r"$f\sigma_8(z)$", fontsize=12, fontfamily='serif')
    ax_top.set_title(r"GRUT growth rate $f\sigma_8(z)$ vs RSD observations",
                     fontsize=12, fontfamily='serif', pad=6)
    ax_top.set_ylim(0.15, 0.70)
    ax_top.legend(fontsize=7.5, loc='lower right', framealpha=0.92, ncol=1)

    # Stats annotation (top panel)
    ax_top.text(0.02, 0.97,
                fr"$N_{{obs}}\!=\!13$   "
                fr"$\chi^2/N_{{GRUT}}\!=\!{chi2_grut:.3f}$   "
                fr"$\chi^2/N_{{\Lambda CDM}}\!=\!{chi2_lcdm:.3f}$",
                transform=ax_top.transAxes, fontsize=8.5,
                color=NAVY, ha='left', va='top', fontfamily='serif',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=NAVY, alpha=0.7, lw=0.7))

    # ── Bottom panel — GRUT residuals ─────────────────────────────────────────
    ax_bot.axhline(0.0,  color=NAVY, lw=1.5, zorder=3)
    ax_bot.axhspan(-1.0, 1.0, color=NAVY, alpha=0.07, zorder=1)
    ax_bot.axhspan(-2.0, 2.0, color=NAVY, alpha=0.04, zorder=1)

    ax_bot.scatter(z_obs, res_grut, color=NAVY, s=24, zorder=5)
    ax_bot.errorbar(z_obs, res_grut, yerr=np.ones_like(res_grut),
                    fmt='none', color=NAVY, elinewidth=0.7, capsize=2, alpha=0.5)

    # Annotate worst residuals (|r| > 1σ) — alternate offsets to avoid overlap
    _offsets = [(14, 9), (-14, 9), (18, -12), (-18, -12), (22, 6), (-22, -9)]
    _oc = 0
    for i, (z, r) in enumerate(zip(z_obs, res_grut)):
        if abs(r) > 1.0:
            ref = RSD_DATA[i].reference.split("+")[0].split(" ")[0]
            dx, dy_abs = _offsets[_oc % len(_offsets)]
            dy = dy_abs if r > 0 else -dy_abs
            _oc += 1
            ax_bot.annotate(f"{ref}", (z, r),
                            textcoords="offset points",
                            xytext=(dx, dy),
                            fontsize=7, color=NAVY, fontfamily='serif',
                            style='italic',
                            arrowprops=dict(arrowstyle='->', color=NAVY,
                                            lw=0.6, alpha=0.55))

    ax_bot.set_ylabel(r"$(f\sigma_8^{\rm GRUT} - f\sigma_{8,\rm obs})\,/\,\sigma$",
                      fontsize=9, fontfamily='serif')
    ax_bot.set_xlabel(r"Redshift  $z$", fontsize=11, fontfamily='serif')
    ax_bot.set_ylim(-3.0, 3.0)
    ax_bot.set_xlim(-0.05, 1.55)

    # Scale note
    ax_bot.text(0.98, 0.06,
                fr"$k_{{RSD}} = {GRUT_K_RSD}\,\mathrm{{Mpc}}^{{-1}}$  "
                r"($\mu_{\rm eff} \approx 1.24$ at $z=0$)",
                transform=ax_bot.transAxes, fontsize=7.5,
                color=NAVY, ha='right', va='bottom', fontfamily='serif',
                style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                          edgecolor=NAVY, alpha=0.7, lw=0.7))

    save(fig, "fig_06_fsigma8.png")


def fig07_s8_tension():
    """S₈ tension plot: GRUT and Planck predictions vs weak lensing surveys.

    Single-panel horizontal tension diagram.  Each WL survey shown as an
    error bar; GRUT (navy) and Planck (orange dashed) as vertical bands.
    Tension values annotated on the right.
    """
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))

    from grut.derived.cosmology.s8_tension import (
        WL_DATA, s8_tension_comparison,
        GRUT_SIGMA8, GRUT_OMEGA_M,
        PLANCK_S8_CMB, PLANCK_S8_CMB_SIGMA,
    )

    cmp    = s8_tension_comparison()
    s8_g   = cmp["grut_s8"]
    s8_p   = cmp["planck_s8_lss"]
    rms_g  = cmp["rms_grut"]
    rms_p  = cmp["rms_planck"]
    t_grut = cmp["tensions_grut"]
    t_plan = cmp["tensions_planck"]

    # Survey display names and colours
    survey_colors = {
        "KiDS-450":   "#C0392B",
        "KiDS-1000":  "#E74C3C",
        "HSC-SSP Y3": "#2980B9",
        "DES Y3":     "#117A65",
    }

    n  = len(WL_DATA)
    ys = list(range(n))   # y-positions

    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor='white')
    ax.set_facecolor(BG)
    ax.grid(True, axis='x', alpha=0.25, lw=0.6)
    ax.tick_params(labelsize=9)

    # ── WL data points ────────────────────────────────────────────────────
    for i, pt in enumerate(WL_DATA):
        col = survey_colors.get(pt.survey, GRAY)
        ax.errorbar(pt.s8, i, xerr=pt.sigma,
                    fmt='o', color=col, ms=8, capsize=4,
                    lw=1.2, elinewidth=1.4, zorder=5,
                    label=f"{pt.survey}  ({pt.reference})")
        # Tension annotations — positioned well right of the Planck band
        ax.text(0.877, i + 0.07,
                fr"GRUT: ${t_grut[i]:+.2f}\sigma$ | Planck: ${t_plan[i]:+.2f}\sigma$",
                va='bottom', ha='left', fontsize=7.5, fontfamily='serif',
                color=GRAY, style='italic')

    # ── GRUT prediction band ──────────────────────────────────────────────
    ax.axvline(s8_g, color=NAVY, lw=2.2, zorder=4,
               label=fr"GRUT  $S_8\!=\!{s8_g:.3f}$  ($\sigma_8\!=\!{GRUT_SIGMA8}$,"
                     fr"  $\Omega_m\!=\!{GRUT_OMEGA_M}$)")

    # ── Planck prediction band ────────────────────────────────────────────
    ax.axvspan(PLANCK_S8_CMB - PLANCK_S8_CMB_SIGMA,
               PLANCK_S8_CMB + PLANCK_S8_CMB_SIGMA,
               color=ORANGE, alpha=0.25, zorder=2)
    ax.axvline(PLANCK_S8_CMB, color=ORANGE, lw=1.8, ls='--', zorder=3,
               label=fr"Planck 2018  $S_8\!=\!{PLANCK_S8_CMB:.3f}\pm{PLANCK_S8_CMB_SIGMA:.3f}$  (CMB)")

    # ── Axes ─────────────────────────────────────────────────────────────
    ax.set_yticks(ys)
    ax.set_yticklabels(
        [f"{pt.survey}  $z_{{\\rm eff}}\\sim 0.3\\!-\\!0.9$" for pt in WL_DATA],
        fontsize=9, fontfamily='serif')
    ax.set_xlabel(r"$S_8 = \sigma_8\,(\Omega_m/0.3)^{0.5}$",
                  fontsize=12, fontfamily='serif')
    ax.set_title(r"GRUT $S_8$ prediction vs weak lensing surveys",
                 fontsize=12, fontfamily='serif', pad=6)
    ax.set_xlim(0.675, 0.945)   # wider: accommodates right-side tension annotations
    ax.set_ylim(-0.7, n - 0.2)

    # Stats box
    ax.text(0.02, 0.97,
            fr"GRUT:  RMS tension $= {rms_g:.2f}\sigma$   ($\chi^2/N = {cmp['chi2_N_grut']:.2f}$)"
            "\n"
            fr"Planck: RMS tension $= {rms_p:.2f}\sigma$   ($\chi^2/N = {cmp['chi2_N_planck']:.2f}$)"
            "\n"
            fr"Tension reduction: ${cmp['tension_reduction']:.2f}\times$ (GRUT vs Planck)",
            transform=ax.transAxes, fontsize=8.5,
            color=NAVY, ha='left', va='top', fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='white',
                      edgecolor=NAVY, alpha=0.8, lw=0.8))

    # Legend below the axes — avoids any overlap with data or tension annotations
    ax.legend(fontsize=8.5, framealpha=0.92, ncol=3,
              loc='upper center', bbox_to_anchor=(0.5, -0.16),
              borderaxespad=0, handlelength=1.8)
    fig.tight_layout(pad=0.8)
    fig.subplots_adjust(bottom=0.24)   # reserve room for the 2-row legend

    save(fig, "fig_07_s8_tension.png")


def fig08_cmb_isw():
    """Figure 8 — CMB low-ℓ ISW: linear branch RULED OUT (Correction #38).

    Two-panel figure:
      Top:    Φ̃(a) = μ(k,a)×δ(a)/a for GRUT and ΛCDM at two CMB scales.
              Shows GRUT potential deepening (real) vs ΛCDM decay — a ~5× ISW
              amplitude difference.
      Bottom: ISW source ΔΦ̃/Δz (rate of potential change) vs redshift.

    The deepening is real, but D_ℓ ∝ |ΔΦ̃|², so the large amplitude ADDS power:
    the validated MGCAMB run gives a ~2.6× low-ℓ EXCESS (~29σ) — the opposite of
    the Planck deficit — which rules out the linear branch. The old "cooling →
    matches Planck deficit" reading was a sign error.
    """
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from grut.derived.cosmology.cmb_isw import (
        reduced_potential_history,
        CMB_K_LOW_ELL, CMB_K_HORIZON,
        PLANCK_LOW_ELL_RATIO, PLANCK_LOW_ELL_SIGMA,
    )

    import numpy as np

    h_le  = reduced_potential_history(CMB_K_LOW_ELL)
    h_hor = reduced_potential_history(CMB_K_HORIZON)

    a_le   = h_le["a_arr"];  phi_g_le  = h_le["phi_grut"];  phi_l_le  = h_le["phi_lcdm"]
    a_hor  = h_hor["a_arr"]; phi_g_hor = h_hor["phi_grut"]; phi_l_hor = h_hor["phi_lcdm"]

    # Compute derivative dΦ̃/dz (for GRUT, k=10⁻³)
    z_le   = 1.0 / a_le - 1.0
    dz     = np.diff(z_le)
    dphi_g = np.diff(phi_g_le)
    dphi_l = np.diff(phi_l_le)
    # dΦ̃/dz at midpoints (only late-time: z < 10)
    z_mid  = 0.5 * (z_le[:-1] + z_le[1:])

    # ── Layout ────────────────────────────────────────────────────────────────
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 10),
                                   gridspec_kw={"height_ratios": [1.2, 1]})
    fig.suptitle("GRUT CMB Low-ℓ ISW — Linear Branch RULED OUT (Correction #38)",
                 fontsize=12.5, fontweight="bold", color=NAVY)
    fig.text(0.5, 0.955,
             "Potential deepening is real (ISW amplitude ~5×), but D$_\\ell\\propto|\\Delta\\tilde{\\Phi}|^2$ → "
             "validated MGCAMB gives ~2.6× low-$\\ell$ EXCESS (~29$\\sigma$), not the Planck deficit",
             ha="center", va="top", fontsize=8.5, color="firebrick", style="italic")

    # ── Top panel: Φ̃(a) ─────────────────────────────────────────────────────
    z_le_plot  = 1.0 / a_le - 1.0
    z_hor_plot = 1.0 / a_hor - 1.0

    # Mask to z < 1200 — show full history from recombination
    m_le  = z_le_plot  <= 1200
    m_hor = z_hor_plot <= 1200

    ax1.semilogy()   # z axis (manual — we plot phi vs z on linear y for better contrast)

    # GRUT curves
    ax1.plot(z_le_plot[m_le],  phi_g_le[m_le],  color=NAVY, lw=2.2,
             label=r"GRUT,  $k=10^{-3}$ Mpc$^{-1}$ ($\ell\approx15$)")
    ax1.plot(z_hor_plot[m_hor], phi_g_hor[m_hor], color=NAVY, lw=2.2,
             ls="--", label=r"GRUT,  $k=4.5\times10^{-4}$ Mpc$^{-1}$ ($\ell\approx2$)")

    # ΛCDM curve (same for both k since μ=1; use k=10⁻³ as representative)
    ax1.plot(z_le_plot[m_le],  phi_l_le[m_le],  color=ORANGE, lw=2.0,
             ls="-.", label=r"$\Lambda$CDM (both scales)")

    # Reference line Φ̃=1 (matter-domination plateau)
    ax1.axhline(1.0, color="gray", lw=0.8, ls=":", alpha=0.7, zorder=0)
    ax1.text(0.5, 1.03, r"$\tilde{\Phi}=1$ (matter-dom plateau)", color="gray",
             fontsize=8.5, ha="center", transform=ax1.get_yaxis_transform())

    # Mark GRUT transition z★
    z_star = h_le["z_star"]
    ax1.axvline(z_star, color=NAVY, lw=0.8, ls=":", alpha=0.5)
    ax1.text(z_star * 1.10, 1.65, rf"$z_*={z_star:.0f}$", color=NAVY,
             fontsize=8.5, ha="left", va="center")

    # Mark recombination (now visible with extended xlim to 1300)
    ax1.axvline(1100, color="firebrick", lw=0.7, ls=":", alpha=0.4)
    ax1.text(1100 * 1.04, 0.73, r"$z_{\rm rec}=1100$", color="firebrick",
             fontsize=8, ha="left", va="bottom")

    # Today values stored for stats box (arrows removed — they clashed with the legend)
    phi_grut_now = h_le["phi_grut_today"]
    phi_lcdm_now = h_le["phi_lcdm_today"]

    ax1.set_xscale("log")
    ax1.set_xlim(0.05, 1300)   # extends to recombination z≈1100
    ax1.set_ylim(0.38, 2.85)
    ax1.set_xlabel("Redshift  $z$", fontsize=11)
    ax1.set_ylabel(r"Reduced potential $\tilde{\Phi}(a)$", fontsize=11)
    # Legend at lower-left: below the ΛCDM curve, well clear of the stats box (upper-right)
    ax1.legend(fontsize=9, loc="lower left", framealpha=0.9)

    # Stats box upper-right — includes today values (replaces the removed arrow annotations)
    ratio = h_le["phi_ratio"]
    amp   = h_le["isw_amplitude_ratio"]
    mu_r  = h_le["mu_at_rec"]
    stats_txt = (
        rf"$\tilde{{\Phi}}_{{GRUT}}(z{{\approx}}0)={phi_grut_now:.3f}$  "
        rf"$\tilde{{\Phi}}_{{\Lambda CDM}}(z{{\approx}}0)={phi_lcdm_now:.3f}$"
        "\n"
        f"$\\tilde{{\\Phi}}_{{GRUT}}/\\tilde{{\\Phi}}_{{\\Lambda CDM}} = {ratio:.2f}\\times$   "
        f"ISW amplitude = ${amp:.1f}\\times$\n"
        f"$\\mu_{{GRUT}}(z=1100) = {mu_r:.4f}$ (SW unchanged)   "
        f"$z_* \\approx {z_star:.0f}$"
    )
    ax1.text(0.98, 0.97, stats_txt, transform=ax1.transAxes, fontsize=8.5,
             va="top", ha="right",
             bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=LGRAY, alpha=0.9))

    # Cooling/heating labels
    ax1.text(0.55, 0.62, "GRUT potential deepens\n(ISW amplitude ~5×)",
             transform=ax1.transAxes, fontsize=9, color=NAVY,
             ha="center", style="italic")
    ax1.text(0.55, 0.25, "ΛCDM potential decays\n(standard late ISW)",
             transform=ax1.transAxes, fontsize=9, color=ORANGE,
             ha="center", style="italic")

    # ── Bottom panel: dΦ̃/dz (ISW source) ───────────────────────────────────
    # Focus on z = 0–10 (late-time ISW window)
    m_late = z_mid <= 10
    z_m    = z_mid[m_late]
    dphi_g_dz = dphi_g[m_late] / np.abs(dz[m_late])
    dphi_l_dz = dphi_l[m_late] / np.abs(dz[m_late])

    ax2.plot(z_m, dphi_g_dz, color=NAVY, lw=2.0,
             label=r"GRUT $d\tilde{\Phi}/dz$  (k=$10^{-3}$ Mpc$^{-1}$)")
    ax2.plot(z_m, dphi_l_dz, color=ORANGE, lw=2.0, ls="-.",
             label=r"$\Lambda$CDM $d\tilde{\Phi}/dz$")
    ax2.axhline(0, color="gray", lw=0.7, ls=":", alpha=0.6)

    # Shade cooling (GRUT > 0 → cooling) and heating (LCDM < 0 → heating) regions
    ax2.fill_between(z_m, 0, dphi_g_dz, where=dphi_g_dz > 0,
                     color=NAVY, alpha=0.15, label="GRUT cooling region")
    ax2.fill_between(z_m, 0, dphi_l_dz, where=dphi_l_dz < 0,
                     color=ORANGE, alpha=0.15, label="ΛCDM heating region")

    # Annotate ISW sign in each region — axes-fraction coords to stay clear of curves
    ax2.text(0.18, 0.82, "cooling\n(GRUT deepens)", color=NAVY,
             fontsize=8.5, ha="center", style="italic",
             transform=ax2.transAxes)
    ax2.text(0.60, 0.12, "heating\n(ΛCDM decays)", color=ORANGE,
             fontsize=8.5, ha="center", style="italic",
             transform=ax2.transAxes)

    ax2.set_xlim(0, 10)
    ax2.set_xlabel("Redshift  $z$", fontsize=11)
    ax2.set_ylabel(r"$d\tilde{\Phi}/dz$", fontsize=11)
    ax2.set_title(r"ISW source term at $\ell\approx10$–30 scales", fontsize=10)
    # Legend upper-right: curves converge to ≈0 at z>6 — clear space there
    ax2.legend(fontsize=8.5, loc="upper right", framealpha=0.9)

    # Planck low-ell note — lower-left, separate from the legend (upper-right)
    ax2.text(0.02, 0.05,
             f"Planck low-ℓ: $D_\\ell^{{obs}}/D_\\ell^{{\\Lambda CDM}}\\approx{PLANCK_LOW_ELL_RATIO}$ (deficit)\n"
             "GRUT (full MGCAMB): ~2.6× EXCESS → RULED OUT (Corr #38)",
             transform=ax2.transAxes, fontsize=8.0, va="bottom", ha="left",
             color="firebrick",
             bbox=dict(boxstyle="round,pad=0.3", fc="mistyrose", ec="firebrick", alpha=0.9))

    fig.tight_layout(pad=0.8)
    save(fig, "fig_08_cmb_isw.png")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating GRUT figures …")
    fig00_tau0_bridge()
    fig01_grut_chain()
    fig02_timescales()
    fig03_three_regimes()
    fig04_gate_r()
    fig05_hz_residuals()
    fig06_fsigma8()
    fig07_s8_tension()
    fig08_cmb_isw()
    fig09_cluster_schematic()
    fig10_cluster_scaling()
    fig11_modified_gravity()
    fig14_cmb_pk()
    fig15_mgcamb_prototype()
    fig16_schrodinger()
    fig17_open_ledger()
    print(f"Done — 16 figures written to {OUT}")
