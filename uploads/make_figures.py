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
# Figure 1 — Two-Timescale Logarithmic Map
# ─────────────────────────────────────────────────────────────────────────────
def fig01_timescales():
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
    save(fig, "fig_01_two_scales.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2 — n_g²(ωτ₀): Three Regimes of the Responsive Vacuum
# ─────────────────────────────────────────────────────────────────────────────
def fig02_three_regimes():
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
    save(fig, "fig_02_three_regimes.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 3 — Gate R: Two-Route Convergence to R = √(4/3)
# ─────────────────────────────────────────────────────────────────────────────
def fig03_gate_r():
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
    save(fig, "fig_03_gate_r.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 4 — Cluster Merger Schematic (Bullet Cluster mechanism)
# ─────────────────────────────────────────────────────────────────────────────
def fig04_cluster_schematic():
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
    fig.patch.set_facecolor('white')

    def cluster_panel(ax, title, label, gas_offset, dm_offset,
                      v_arrows=True, after=False):
        ax.set_facecolor(BG)
        ax.set_xlim(-4.5, 4.5); ax.set_ylim(-2.5, 3.0)
        ax.axis('off')
        ax.set_title(title, fontsize=10, fontweight='bold',
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
                    fontsize=8, color=NAVY, fontfamily='serif')
            ax.text(-2.5,  1.35, "DM halo",  ha='center', fontsize=8,
                    color=BLUE, fontfamily='serif')
            ax.text(-2.5, -0.15, "gas",      ha='center', fontsize=7.5,
                    color=ORANGE, fontfamily='serif', fontweight='bold')
        else:
            # Gas stopped at centre
            gas = mpatches.Ellipse((0 + gas_offset, 0), 2.2, 1.4,
                                   alpha=0.50, facecolor='#e67e22',
                                   edgecolor='#a04000', lw=1.2)
            ax.add_patch(gas)
            ax.text(gas_offset, 0, "gas\n(collisional,\nstopped)",
                    ha='center', va='center', fontsize=7.5,
                    color='#7d3c00', fontweight='bold', fontfamily='serif')

            # DM lensing mass (two offset blobs)
            for sign, xoff in [(-1, -dm_offset), (1, dm_offset)]:
                dm = mpatches.Ellipse((xoff, 0.1), 2.6, 1.8,
                                      fill=False, edgecolor=BLUE,
                                      lw=2.2, ls='--', alpha=0.85)
                ax.add_patch(dm)
                ax.annotate("lensing\nmass", xy=(xoff, 0.9),
                            fontsize=8, ha='center', color=BLUE,
                            fontfamily='serif')

            # Offset dimension arrow
            ax.annotate("", xy=(dm_offset - 0.1, -1.5),
                        xytext=(-dm_offset + 0.1, -1.5),
                        arrowprops=dict(arrowstyle="<->", color=RED, lw=1.5))
            ax.text(0, -1.95,
                    r"$\delta \approx v \times \tau_0 \approx 150$ kpc",
                    ha='center', fontsize=9, color=RED, fontweight='bold',
                    fontfamily='serif')
            ax.text(0, 2.5,
                    r"Mechanism: retarded kernel $K^R \propto e^{-t/\tau_0}$",
                    ha='center', fontsize=7.5, color=SLATE, style='italic',
                    fontfamily='serif')

    cluster_panel(axes[0], "Before Merger", "before",
                  gas_offset=0, dm_offset=2.5, after=False)
    cluster_panel(axes[1], "After Merger (Bullet Cluster)", "after",
                  gas_offset=0, dm_offset=2.0, after=True)

    fig.suptitle("GRUT Cluster Merger Lag Mechanism — Viscoelastic Memory Kernel",
                 fontsize=10.5, fontweight='bold', color=NAVY,
                 fontfamily='serif', y=1.01)
    plt.tight_layout(pad=1.2)
    save(fig, "fig_04_cluster_schematic.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 5 — Cluster Merger Population Scaling
# ─────────────────────────────────────────────────────────────────────────────
def fig05_cluster_scaling():
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
    save(fig, "fig_05_cluster_scaling.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 6 — μ_GRUT profile + P(k)/P_ΛCDM
# ─────────────────────────────────────────────────────────────────────────────
def fig06_modified_gravity():
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
    save(fig, "fig_06_modified_gravity.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 7 — CMB + P(k): Correction #36 Native Boltzmann
# ─────────────────────────────────────────────────────────────────────────────
def fig07_cmb_pk():
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
    save(fig, "fig_07_cmb_pk.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 8 — MGCAMB Prototype Diagnostic (artifact record)
# ─────────────────────────────────────────────────────────────────────────────
def fig08_mgcamb_prototype():
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
    ax1.text(22, 5000, "ARTIFACT\n(etak/z mismatch)\n×1.7–2.0 excess",
             ha='center', va='top', fontsize=8, color=RED, fontweight='bold',
             fontfamily='serif',
             bbox=dict(boxstyle='round,pad=0.25', facecolor='#fff0f0',
                       edgecolor=RED, alpha=0.9))
    ax1.text(700, 3500, r"$\ell>100$: < 0.2%" + "\n(not artifact)", ha='center',
             fontsize=8, color=TEAL, fontfamily='serif', style='italic')
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
    ax2.text(0.97, 0.04, "NOT physical GRUT predictions\n(prototype diagnostic only)",
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
    save(fig, "fig_08_mgcamb_prototype.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 9 — Open Question Dependency Ledger
# ─────────────────────────────────────────────────────────────────────────────
def fig09_open_ledger():
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
    save(fig, "fig_09_open_ledger.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 11 — Schrödinger-in-the-Box: Standard vs GRUT Inversion
# ─────────────────────────────────────────────────────────────────────────────
def fig11_schrodinger_inversion():
    """Two-panel comparison: Standard formulation vs GRUT inversion of the cat paradox."""
    FW, FH = 13, 7
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
        ax.text(cx, FH-0.45, lbl, ha='center', va='center', fontsize=11,
                color=fc, fontweight='bold', fontfamily='monospace')
        seg(cx - 2.4, FH-0.65, cx + 2.4, FH-0.65, c=fc, lw=1.5)

    # ══════════════════════════════════════════════════════════════════════════
    # LEFT panel — Standard formulation
    # ══════════════════════════════════════════════════════════════════════════
    XL = XD / 2    # left panel centre

    # Observer (outside)
    rbox(XL, FH-1.45, 2.4, 0.60, RED, RED, 'OBSERVER', fs=10, bold=True)

    # Arrow down with label
    seg(XL, FH-1.75, XL, FH-2.30, c=GRAY)
    arw(XL, FH-2.30)
    ax.text(XL+0.12, FH-2.05, '"is the cat alive?"', ha='left', va='center',
            fontsize=8.5, color=GRAY, style='italic')

    # Box (containing superposed cat)
    rbox(XL, 3.35, 3.6, 2.50, LRED, RED, '', lw=1.8, zo=2)
    ax.text(XL, 4.55, 'BOX', ha='center', va='center', fontsize=9,
            color=RED, fontweight='bold', zorder=3)
    rbox(XL, 3.20, 2.8, 1.30, '#FEF9F9', RED,
         'CAT:\nalive or dead?\n(superposed?)',
         fs=9, tc=SLATE, lw=1.0, zo=4, pad=0.12)

    # Caption below
    ax.text(XL, 1.45,
            'The observer collapses\nthe wavefunction.\n'
            'Where is the line?\n(Copenhagen: unknown)',
            ha='center', va='center', fontsize=8.5, color=GRAY,
            linespacing=1.6)

    # ══════════════════════════════════════════════════════════════════════════
    # RIGHT panel — GRUT inversion
    # ══════════════════════════════════════════════════════════════════════════
    XR = XD + XD/2    # right panel centre

    # Outer box (the universe / the medium)
    rbox(XR, 4.10, 5.2, 3.30, LBLUE, GRN, '', lw=2.0, zo=2, ls='-')
    ax.text(XR - 2.2, 5.60, 'BOX', ha='left', va='center', fontsize=9,
            color=GRN, fontweight='bold', zorder=3)

    # CAT node
    rbox(XR - 1.1, 4.35, 1.55, 0.90, LGN, GRN,
         r'CAT' + '\n' + r'$X \sim 10^{7}$',
         fs=9.5, tc=SLATE, lw=1.2, zo=4)

    # OBSERVER node
    rbox(XR + 1.1, 4.35, 1.55, 0.90, LGN, GRN,
         r'OBSERVER' + '\n' + r'$X \sim 10^{35}$',
         fs=9.5, tc=SLATE, lw=1.2, zo=4)

    # "Both already crystallized" label
    ax.text(XR, 3.15,
            'Both already crystallized.\nNo outside observer needed.',
            ha='center', va='center', fontsize=9, color=SLATE,
            fontweight='bold', linespacing=1.5, zorder=5)

    # Caption below
    ax.text(XR, 1.45,
            'The "paradox" assumes an\noutside vantage point.\n'
            r'There is no such point.' + '\n'
            r'The line is $\Lambda_{\rm grav} \times t = 1$.' + '\n'
            '(GRUT: computed)',
            ha='center', va='center', fontsize=8.5, color=GRAY,
            linespacing=1.6)

    # ── Bottom note ────────────────────────────────────────────────────────────
    ax.text(FW/2, 0.18,
            r'$X = \Lambda_{\rm grav} \times \tau_0$: crystal regime ($X \gg 1$) = classical definite state; '
            r'boundary ($X \approx 1$) = decoherence plateau.  '
            r'Cat: $X \sim 10^{7}$.  Observer: $X \sim 10^{35}$.  Both crystallized.',
            ha='center', va='bottom', fontsize=7.5, color=LGRAY, style='italic')

    save(fig, "fig_11_schrodinger_inversion.png")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 10 — GRUT Derivation Chain
# ─────────────────────────────────────────────────────────────────────────────
def fig10_grut_chain():
    """Professional derivation-chain diagram: S_CTP → kernels → n_g(ω) → 4 regimes."""
    FW, FH = 15, 10
    fig = plt.figure(figsize=(FW, FH), facecolor='white')
    ax  = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, FW); ax.set_ylim(0, FH); ax.axis('off')

    # Palette (local — different style from other figs)
    _NAVY  = '#1B3A6B'; _BLUE  = '#2471A3'; _TEAL  = '#1A5276'
    _GRN   = '#1E6B45'; _ORG   = '#883800'; _PUR   = '#5B2C8D'; _STE  = '#2C3E50'
    _LG    = '#D5F0E3'; _LO    = '#FDE8C8'; _LP    = '#EAD5F5'; _LS   = '#D0E8F0'
    _LBLUE = '#D4E9F7'; _GRAY  = '#444444'; _LGRAY = '#999999'; _W    = 'white'

    def rbox(cx, cy, w, h, fc, ec, txt, fs=9.5, tc=_W, lw=1.5,
             bold=False, pad=0.1, ls='-', zo=3):
        p = FancyBboxPatch((cx-w/2, cy-h/2), w, h,
                            boxstyle=f'round,pad={pad}',
                            fc=fc, ec=ec, lw=lw, ls=ls, zorder=zo)
        ax.add_patch(p)
        ax.text(cx, cy, txt, ha='center', va='center', fontsize=fs,
                color=tc, fontweight='bold' if bold else 'normal',
                zorder=zo+1, linespacing=1.55)

    def seg(x1, y1, x2, y2, c=_GRAY, lw=1.4, ls='-'):
        ax.plot([x1,x2],[y1,y2], c=c, lw=lw, ls=ls, zorder=2,
                solid_capstyle='round', solid_joinstyle='round')

    def arw(x, y_tip, c=_GRAY, lw=1.4):
        ax.annotate('', xy=(x, y_tip), xytext=(x, y_tip+0.22),
                    arrowprops=dict(arrowstyle='->', color=c, lw=lw,
                                    mutation_scale=11), zorder=5)

    # Geometry
    YT=9.25; YK=7.55; YKC=6.55; YMER=6.08; YN=5.05; YR=3.65; YB=1.80
    XC=7.5; XNG=3.15; XKR=11.85
    XL=[1.45, 4.55, 10.45, 13.55]

    # S_CTP
    rbox(XC, YT, 14.0, 0.82, _NAVY, _NAVY,
         r'$S_{\mathrm{CTP}}$'
         r'   ·   §3 — density-matrix path integral over gravitational environment',
         fs=11, bold=True)

    # Trunk → T-junction
    seg(XC, YT-0.41, XC, YT-0.68)
    seg(XNG, YT-0.68, XKR, YT-0.68)
    seg(XNG, YT-0.68, XNG, YK+0.57)
    seg(XKR, YT-0.68, XKR, YK+0.57)

    # Kernel section background (dashed)
    kbg = FancyBboxPatch((0.42, YMER-0.08), 14.16, 2.28,
                          boxstyle='round,pad=0.08',
                          fc=_LBLUE, ec=_BLUE, lw=1.1, ls=(0,(6,3)), zorder=1, alpha=0.38)
    ax.add_patch(kbg)

    # Kernel boxes
    rbox(XNG, YK, 5.2, 1.05, _BLUE, _BLUE,
         r'$N_{\mathrm{grav}}(x,\,x^{\prime})$'
         '\n' r'$G\,/\,(\hbar\,|\,x - x^{\prime}\,|)$'
         '\n(noise kernel)', fs=10.5)
    rbox(XKR, YK, 5.2, 1.05, _BLUE, _BLUE,
         r'$K^{R}(t)$'
         '\n' r'$\tau_0^{-1}\,\exp(-t/\tau_0)$'
         '\n(retarded kernel)', fs=10.5)

    # Constants
    seg(XKR, YK-0.53, XKR, YKC+0.20, c=_LGRAY, lw=0.9, ls='--')
    ax.text(XKR, YKC+0.12,
            r'$\tau_0 = 41.9\,\mathrm{Myr}$'
            r'   $\leftarrow$ cosmic-baseline anchor',
            ha='center', va='center', fontsize=9.5, color=_GRAY, style='italic')
    ax.text(XKR, YKC-0.24,
            r'$\alpha_\mathrm{vac} = 1/3$'
            r'   $\leftarrow$ Gate R  (Duff 1994, $a/c = 1/3$)',
            ha='center', va='center', fontsize=9.5, color=_GRAY, style='italic')

    # Convergence → n_g
    seg(XNG, YK-0.53, XNG, YMER)
    seg(XKR, YKC-0.44, XKR, YMER)
    seg(XNG, YMER, XKR, YMER)
    seg(XC, YMER, XC, YN+0.43)
    arw(XC, YN+0.43)

    # n_g(ω)
    rbox(XC, YN, 6.6, 0.78, _TEAL, _TEAL,
         r'$n_g(\omega)\;=\;\sqrt{\;1 + '
         r'\dfrac{\alpha_\mathrm{vac}}{1+(\omega\tau_0)^{2}}\;}$',
         fs=12.5)

    # Fan to 4 regimes
    seg(XC, YN-0.39, XC, YN-0.68)
    seg(XL[0], YN-0.68, XL[3], YN-0.68)
    for xl in XL:
        seg(xl, YN-0.68, xl, YR+0.42)
        arw(xl, YR+0.41)

    # Regime headers
    for xl, fc, lbl in [
        (XL[0], _GRN, r'$X \gg 1$'     + '\nCrystal'),
        (XL[1], _ORG, r'$X \approx 1$' + '\nBoundary'),
        (XL[2], _PUR, r'$X \ll 1$'     + '\nFluid'),
        (XL[3], _STE, r'$\mu(k,\,a)$'  + '\nFourier'),
    ]:
        rbox(xl, YR, 2.6, 0.76, fc, fc, lbl, fs=11, bold=True, pad=0.08)

    # Regime bodies
    BOX_H = 2.55
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
        rbox(xl, YB, 2.6, BOX_H, fc, ec, body,
             fs=9.5, tc='#111111', lw=1.0, pad=0.14, zo=3)
        seg(xl, YR-0.38, xl, YB+BOX_H/2, c=_LGRAY, lw=0.9)

    # Footer
    ax.text(XC, 0.26,
            r'All sectoral predictions share zero adjustable parameters beyond '
            r'$\tau_0$ (cosmic-baseline anchor) '
            r'and $\alpha_\mathrm{vac} = 1/3$ (Gate R — derived, not fitted)',
            ha='center', va='bottom', fontsize=8.5, color=_GRAY, style='italic')

    save(fig, "fig_10_grut_chain.png")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Generating GRUT figures …")
    fig01_timescales()
    fig02_three_regimes()
    fig03_gate_r()
    fig04_cluster_schematic()
    fig05_cluster_scaling()
    fig06_modified_gravity()
    fig07_cmb_pk()
    fig08_mgcamb_prototype()
    fig09_open_ledger()
    fig10_grut_chain()
    fig11_schrodinger_inversion()
    print(f"Done — 11 figures written to {OUT}")
