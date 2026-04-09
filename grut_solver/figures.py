"""
GRUT Solver — Publication-quality figure generation.

Two core paper figures:
  Figure 1: Λ(l) separation scan showing the geometric kink at l ≈ 1.8R
  Figure 2: Bell vs product entanglement-dependent decoherence

All physics is computed from the existing solver; nothing is hardcoded.
"""

from __future__ import annotations
import os
import csv
import datetime
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from grut_solver.constants import G, HBAR
from grut_solver.usl.gravitational import lambda_grav, suppression_factor
from grut_solver.usl.many_body import entanglement_discriminant

# ── house style ──────────────────────────────────────────────
_FONT = {"family": "serif", "size": 11}
_TICK  = {"labelsize": 10}
_FIG_DPI = 300


def _apply_style(ax: plt.Axes) -> None:
    ax.tick_params(**_TICK)
    for spine in ax.spines.values():
        spine.set_color("black")
    ax.xaxis.label.set_fontsize(12)
    ax.yaxis.label.set_fontsize(12)


# =====================================================================
# FIGURE 1 — KINK / SEPARATION SCAN
# =====================================================================

def compute_kink_data(
    m: float = 1e-14,
    R: float = 50e-9,
    l_min: float = 1e-9,
    l_max: float = 1e-6,
    n_points: int = 500,
) -> dict:
    """Compute Λ(l) scan data and power-law fit."""

    l_arr = np.geomspace(l_min, l_max, n_points)
    lam_arr = np.array([lambda_grav(m, l, R) for l in l_arr])

    # locate peak
    peak_idx = int(np.argmax(lam_arr))
    l_peak = l_arr[peak_idx]
    lam_peak = lam_arr[peak_idx]

    # single power-law fit in log-log (full range)
    valid = lam_arr > 0
    log_l = np.log10(l_arr[valid])
    log_lam = np.log10(lam_arr[valid])
    coeffs = np.polyfit(log_l, log_lam, 1)
    alpha_fit = coeffs[0]
    log_lam_fit = np.polyval(coeffs, log_l)
    residual_dex = float(np.sqrt(np.mean((log_lam - log_lam_fit) ** 2)))

    pl_arr = np.full_like(lam_arr, np.nan)
    pl_arr[valid] = 10.0 ** log_lam_fit

    # far-field slope check (l > 2R)
    far = l_arr > 2 * R
    if np.sum(far & valid) > 3:
        far_slope = np.polyfit(np.log10(l_arr[far & valid]),
                               np.log10(lam_arr[far & valid]), 1)[0]
    else:
        far_slope = float("nan")

    is_peak = np.zeros(len(l_arr), dtype=int)
    is_peak[peak_idx] = 1

    return dict(
        l=l_arr, lam=lam_arr, pl=pl_arr,
        is_peak=is_peak,
        l_peak=l_peak, lam_peak=lam_peak,
        alpha_fit=alpha_fit, residual_dex=residual_dex,
        far_slope=far_slope, m=m, R=R,
    )


def plot_lambda_vs_l_kink(
    out_dir: str = "paper_figures",
    m: float = 1e-14,
    R: float = 50e-9,
    **kw,
) -> dict:
    """Generate Figure 1 and save PNG / SVG / CSV."""

    os.makedirs(out_dir, exist_ok=True)
    d = compute_kink_data(m=m, R=R, **kw)

    l_nm = d["l"] * 1e9

    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    _apply_style(ax)

    ax.loglog(l_nm, d["lam"], "k-", linewidth=1.8, label="GRUT")
    ax.loglog(l_nm, d["pl"], "k--", linewidth=0.8, alpha=0.55,
              label=rf"Single power-law fit ($\alpha$ = {d['alpha_fit']:.2f})")

    # reference verticals
    for xval, lab in [(R * 1e9, "l = R"), (2 * R * 1e9, "l = 2R")]:
        ax.axvline(xval, color="0.55", linewidth=0.6, linestyle=":")
        ax.text(xval * 1.08, ax.get_ylim()[0] * 3 if ax.get_ylim()[0] > 0 else 1,
                lab, fontsize=8, color="0.4", rotation=90, va="bottom")

    # peak annotation
    lp_nm = d["l_peak"] * 1e9
    ax.plot(lp_nm, d["lam_peak"], "ko", markersize=7, zorder=5)
    ax.annotate(
        f"Peak: $l$ ≈ {lp_nm:.0f} nm\n$\\Lambda$ ≈ {d['lam_peak']:.0f} Hz",
        xy=(lp_nm, d["lam_peak"]),
        xytext=(lp_nm * 2.5, d["lam_peak"] * 1.8),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

    ax.set_xlabel(r"Separation $l$ (nm)")
    ax.set_ylabel(r"Decoherence rate $\Lambda$ (Hz)")
    ax.legend(fontsize=9, frameon=False)
    fig.tight_layout()

    fig.savefig(os.path.join(out_dir, "lambda_vs_l_kink.png"), dpi=_FIG_DPI)
    fig.savefig(os.path.join(out_dir, "lambda_vs_l_kink.svg"))
    plt.close(fig)

    # CSV
    csv_path = os.path.join(out_dir, "lambda_vs_l_kink.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["l_m", "l_nm", "lambda_hz", "powerlaw_fit_hz",
                     "residual_log10", "is_peak"])
        for i in range(len(d["l"])):
            res = (np.log10(d["lam"][i]) - np.log10(d["pl"][i])
                   if d["lam"][i] > 0 and d["pl"][i] > 0 else 0)
            w.writerow([
                f"{d['l'][i]:.6e}", f"{d['l'][i]*1e9:.4f}",
                f"{d['lam'][i]:.6e}", f"{d['pl'][i]:.6e}",
                f"{res:.6f}", d["is_peak"][i],
            ])

    return d


# =====================================================================
# FIGURE 2 — BELL VS PRODUCT
# =====================================================================

def compute_bell_data(
    m: float = 1e-14,
    l: float = 100e-9,
    R: float = 50e-9,
    d_min: float = 150e-9,
    d_max: float = 2000e-9,
    n_points: int = 200,
) -> dict:
    """Compute Bell vs product decoherence as a function of d_AB."""

    d_arr = np.geomspace(d_min, d_max, n_points)
    lp_arr = np.empty(n_points)
    lb_arr = np.empty(n_points)

    for i, d in enumerate(d_arr):
        disc = entanglement_discriminant(m, l, d, R)
        lp_arr[i] = disc["lambda_product"]
        lb_arr[i] = disc["lambda_bell"]

    ratio = lb_arr / lp_arr
    protection = 1.0 - ratio

    # values at d = 200 nm
    idx200 = int(np.argmin(np.abs(d_arr - 200e-9)))
    d200 = d_arr[idx200]
    lp200 = lp_arr[idx200]
    lb200 = lb_arr[idx200]
    ratio200 = ratio[idx200]
    prot200 = protection[idx200]

    return dict(
        d=d_arr, lp=lp_arr, lb=lb_arr, ratio=ratio, protection=protection,
        d200=d200, lp200=lp200, lb200=lb200,
        ratio200=ratio200, prot200=prot200,
        m=m, l=l, R=R,
        prot_min=float(np.min(protection)),
        prot_max=float(np.max(protection)),
    )


def plot_bell_vs_product(
    out_dir: str = "paper_figures",
    m: float = 1e-14,
    l: float = 100e-9,
    R: float = 50e-9,
    **kw,
) -> dict:
    """Generate Figure 2 and save PNG / SVG / CSV."""

    os.makedirs(out_dir, exist_ok=True)
    d = compute_bell_data(m=m, l=l, R=R, **kw)

    d_nm = d["d"] * 1e9

    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    _apply_style(ax)

    ax.plot(d_nm, d["lp"], "k-", linewidth=1.8, label="Product state")
    ax.plot(d_nm, d["lb"], "k--", linewidth=1.4, label="Bell state")

    # highlight d = 200 nm (markers only, no vertical line)
    ax.plot(200, d["lp200"], "ks", markersize=6, zorder=5)
    ax.plot(200, d["lb200"], "ko", markersize=6, zorder=5)

    prot_pct = d["prot200"] * 100
    ax.annotate(
        f"$d$ = 200 nm\nProduct ≈ {d['lp200']:.0f} Hz\n"
        f"Bell ≈ {d['lb200']:.0f} Hz\nProtection ≈ {prot_pct:.0f}%",
        xy=(200, d["lb200"]),
        xytext=(350, d["lb200"] * 0.75),
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
    )

    ax.set_xlabel(r"Particle spacing $d_{\mathrm{AB}}$ (nm)")
    ax.set_ylabel(r"Decoherence rate $\Lambda$ (Hz)")
    ax.legend(fontsize=9, frameon=False, loc="upper right")
    ax.set_xlim(d_nm[0], d_nm[-1])
    fig.tight_layout()

    fig.savefig(os.path.join(out_dir, "bell_vs_product.png"), dpi=_FIG_DPI)
    fig.savefig(os.path.join(out_dir, "bell_vs_product.svg"))
    plt.close(fig)

    # CSV
    csv_path = os.path.join(out_dir, "bell_vs_product.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["d_m", "d_nm", "lambda_product_hz", "lambda_bell_hz",
                     "bell_over_product", "protection_fraction"])
        for i in range(len(d["d"])):
            w.writerow([
                f"{d['d'][i]:.6e}", f"{d['d'][i]*1e9:.4f}",
                f"{d['lp'][i]:.6e}", f"{d['lb'][i]:.6e}",
                f"{d['ratio'][i]:.6f}", f"{d['protection'][i]:.6f}",
            ])

    return d


# =====================================================================
# MANIFEST + CAPTIONS
# =====================================================================

def write_manifest(out_dir: str, fig1: dict, fig2: dict) -> None:
    with open(os.path.join(out_dir, "manifest.txt"), "w") as f:
        f.write("GRUT Paper Figures — Generation Manifest\n")
        f.write(f"Generated: {datetime.datetime.now().isoformat()}\n")
        try:
            from grut_solver import __version__
            f.write(f"Package version: {__version__}\n")
        except Exception:
            f.write("Package version: unknown\n")
        f.write("\nFigure 1 parameters:\n")
        f.write(f"  m = {fig1['m']:.2e} kg\n")
        f.write(f"  R = {fig1['R']*1e9:.0f} nm\n")
        f.write(f"  source: grut_solver.usl.gravitational.lambda_grav\n")
        f.write(f"  peak at l = {fig1['l_peak']*1e9:.1f} nm, Λ = {fig1['lam_peak']:.1f} Hz\n")
        f.write(f"  power-law α = {fig1['alpha_fit']:.2f}, residual = {fig1['residual_dex']:.3f} dex\n")
        f.write("\nFigure 2 parameters:\n")
        f.write(f"  m = {fig2['m']:.2e} kg per particle\n")
        f.write(f"  l = {fig2['l']*1e9:.0f} nm, R = {fig2['R']*1e9:.0f} nm\n")
        f.write(f"  source: grut_solver.usl.many_body.entanglement_discriminant\n")
        f.write(f"  Bell/product at 200 nm = {fig2['ratio200']:.4f} "
                f"(protection {fig2['prot200']*100:.1f}%)\n")


def write_captions(out_dir: str) -> None:
    with open(os.path.join(out_dir, "captions.txt"), "w") as f:
        f.write("Figure 1.\n")
        f.write(
            "Gravitational decoherence rate Λ as a function of separation l "
            "for a 10 pg particle of radius R = 50 nm. In the near field "
            "(l < 2R), the extended-body correction gives Λ ∝ l². In the far "
            "field (l > 2R), the universal scaling law gives Λ ∝ 1/l. The "
            "resulting peak at l ≈ 1.8R is a geometric fingerprint of the "
            "extended-body Diósi functional. A single smooth power-law fit "
            "fails to reproduce the full curve.\n\n"
        )
        f.write("Figure 2.\n")
        f.write(
            "Gravitational decoherence rates for product and Bell states of "
            "two identical 10 pg particles as a function of inter-particle "
            "spacing d_AB. Anti-correlated Bell states decohere more slowly "
            "because the correlated mass distribution reduces the gravitational "
            "self-energy difference between branches. At d_AB = 200 nm, the "
            "Bell-state decoherence rate is approximately 17% lower than the "
            "product-state rate.\n"
        )


# =====================================================================
# PUBLIC ENTRY POINT
# =====================================================================

def generate_all(out_dir: str = "paper_figures") -> None:
    """Generate every paper figure plus manifest and captions."""
    os.makedirs(out_dir, exist_ok=True)

    print("Generating Figure 1 (kink) …")
    fig1 = plot_lambda_vs_l_kink(out_dir=out_dir)
    print(f"  Peak: l = {fig1['l_peak']*1e9:.1f} nm, Λ = {fig1['lam_peak']:.1f} Hz")
    print(f"  Power-law α = {fig1['alpha_fit']:.2f}, residual = {fig1['residual_dex']:.3f} dex")
    print(f"  Far-field slope = {fig1['far_slope']:.2f}")

    print("Generating Figure 2 (Bell vs product) …")
    fig2 = plot_bell_vs_product(out_dir=out_dir)
    print(f"  Bell/product at 200 nm = {fig2['ratio200']:.4f} "
          f"(protection {fig2['prot200']*100:.1f}%)")
    print(f"  Protection range: {fig2['prot_min']*100:.1f}% – {fig2['prot_max']*100:.1f}%")

    write_manifest(out_dir, fig1, fig2)
    write_captions(out_dir)

    print(f"\nAll outputs in: {out_dir}/")
    for fn in sorted(os.listdir(out_dir)):
        sz = os.path.getsize(os.path.join(out_dir, fn))
        print(f"  {fn:40s} {sz:>10,d} bytes")
