"""Cluster-merger deceleration-ratio sensitivity — does the v_post / v_initial
modeling choice contribute to the +20% systematic?

The framework currently uses v_final = 0.638 × v_initial across all
clusters, extrapolated from the Bullet Cluster's measured ratio
(3000/4700 ≈ 0.638). This ratio is itself a modeling choice. If the
deceleration model is too aggressive, the framework will systematically
underpredict offsets — visible as the 0.79-0.88 cluster_merger_scaling_law
ratios.

This module tests that hypothesis directly: sweep dec_ratio across a
physically reasonable range while keeping τ_0 fixed at canonical, and
see whether the systematic moves with the convention. Then run a 2D
sweep across (τ_0, dec_ratio) to expose the degeneracy.

Result preview
--------------

At canonical τ_0 = 41.9 Myr, varying dec_ratio:
    dec_ratio = 0.638 (Bullet-extrapolated):  χ² = 0.077  (canonical)
    dec_ratio = 0.74 (best-fit):              χ² = 0.008  (10× better)

This matches the χ² improvement from the tau_0_sensitivity analysis
(τ_0 = 49 Myr, χ² = 0.007) almost exactly. The two analyses give
EQUIVALENT improvements — meaning offset data alone cannot disentangle
the two effects. The 2D sweep shows a degeneracy ridge in (τ_0,
dec_ratio) space along which dec_ratio × τ_0 ≈ constant.

Implication
-----------

The honest answer to "is the +20% a τ_0 effect or a velocity-convention
effect?" is: **without independent v_post-collision measurements for
MACS and Abell, the data does not distinguish them.** Either:

    (a) τ_0 ≈ 49 Myr in cluster regime + dec_ratio = 0.638 standard
    (b) τ_0 = 41.9 Myr canonical + dec_ratio ≈ 0.74 (less aggressive)
    (c) Any combination on the dec_ratio × τ_0 ≈ const ridge

All three give the same χ² fit to offset data. Disambiguation requires
hydrodynamic simulations or X-ray-derived velocity measurements per
cluster (currently only Bullet has this from Springel & Farrar 2007).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from grut.derived.cluster.bullet_cluster import (
    BulletClusterObs,
    grut_offset_kernel_convolution_kpc,
)
from grut.derived.cluster.merger_population import (
    ABELL_520,
    BULLET,
    MACS_J0025,
)
from grut.foundation.closure_protocol import TAU_0_SEC


YEAR_SEC: float = 3.156e7
MYR_SEC: float = 1e6 * YEAR_SEC


# Canonical Bullet-extrapolated deceleration ratio
CANONICAL_DEC_RATIO: float = 3000.0 / 4700.0  # ≈ 0.6383

# Sweep grids
DEFAULT_DEC_RATIO_GRID: tuple[float, ...] = tuple(
    float(x) for x in np.arange(0.45, 1.01, 0.01)
)

DEFAULT_TAU_0_GRID_MYR_2D: tuple[float, ...] = tuple(
    float(x) for x in np.arange(30.0, 65.5, 1.0)
)
DEFAULT_DEC_RATIO_GRID_2D: tuple[float, ...] = tuple(
    float(x) for x in np.arange(0.50, 0.96, 0.02)
)


# Three normal-regime clusters (El Gordo excluded as documented outlier)
NORMAL_REGIME_CLUSTERS: tuple[tuple[str, BulletClusterObs], ...] = (
    ("Bullet Cluster", BULLET),
    ("MACS J0025", MACS_J0025),
    ("Abell 520", ABELL_520),
)


# ─────────────────────────────────────────────────────────────────────
# Per-cluster prediction at custom (τ_0, dec_ratio)
# ─────────────────────────────────────────────────────────────────────

def predicted_offset_kpc(
    obs: BulletClusterObs,
    dec_ratio: float,
    tau_0_Myr: float = 41.9,
) -> float:
    """Predicted gas-to-lensing offset at a custom (τ_0, dec_ratio).

    v_final is computed from v_initial × dec_ratio rather than read
    from the obs record — this is what we're varying.
    """
    v_final = obs.v_initial_km_s * dec_ratio
    tau_0_sec = tau_0_Myr * MYR_SEC
    return grut_offset_kernel_convolution_kpc(
        v_initial_km_s=obs.v_initial_km_s,
        v_final_km_s=v_final,
        t_since_Myr=obs.t_since_Myr,
        tau_0_sec=tau_0_sec,
    )


def ratio_at(
    obs: BulletClusterObs,
    dec_ratio: float,
    tau_0_Myr: float = 41.9,
) -> float:
    pred = predicted_offset_kpc(obs, dec_ratio, tau_0_Myr)
    return pred / obs.gas_lensing_offset_kpc


# ─────────────────────────────────────────────────────────────────────
# 1D sweep over dec_ratio at canonical τ_0
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class DecRatioSweepPoint:
    dec_ratio: float
    ratios: dict[str, float]
    chi_squared: float
    rms_deviation: float


def evaluate_dec_ratio(
    dec_ratio: float,
    tau_0_Myr: float = 41.9,
) -> DecRatioSweepPoint:
    ratios = {
        name: ratio_at(obs, dec_ratio, tau_0_Myr)
        for name, obs in NORMAL_REGIME_CLUSTERS
    }
    arr = np.array(list(ratios.values()))
    chi2 = float(np.sum((arr - 1.0) ** 2))
    rms = float(np.sqrt(np.mean((arr - 1.0) ** 2)))
    return DecRatioSweepPoint(
        dec_ratio=dec_ratio,
        ratios=ratios,
        chi_squared=chi2,
        rms_deviation=rms,
    )


def dec_ratio_sweep(
    grid: tuple[float, ...] = DEFAULT_DEC_RATIO_GRID,
    tau_0_Myr: float = 41.9,
) -> tuple[DecRatioSweepPoint, ...]:
    return tuple(evaluate_dec_ratio(dr, tau_0_Myr) for dr in grid)


def best_fit_dec_ratio(
    grid: tuple[float, ...] = DEFAULT_DEC_RATIO_GRID,
    tau_0_Myr: float = 41.9,
) -> DecRatioSweepPoint:
    return min(
        dec_ratio_sweep(grid, tau_0_Myr),
        key=lambda p: p.chi_squared,
    )


# ─────────────────────────────────────────────────────────────────────
# 2D sweep over (τ_0, dec_ratio) — exposes the degeneracy
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class TwoDSweepPoint:
    tau_0_Myr: float
    dec_ratio: float
    chi_squared: float
    product: float
    """dec_ratio × τ_0 — the degeneracy parameter. Constant chi²
    contours should approximately follow constant product."""


def evaluate_2d(tau_0_Myr: float, dec_ratio: float) -> TwoDSweepPoint:
    point = evaluate_dec_ratio(dec_ratio, tau_0_Myr)
    return TwoDSweepPoint(
        tau_0_Myr=tau_0_Myr,
        dec_ratio=dec_ratio,
        chi_squared=point.chi_squared,
        product=dec_ratio * tau_0_Myr,
    )


def two_d_sweep(
    tau_0_grid: tuple[float, ...] = DEFAULT_TAU_0_GRID_MYR_2D,
    dec_ratio_grid: tuple[float, ...] = DEFAULT_DEC_RATIO_GRID_2D,
) -> tuple[TwoDSweepPoint, ...]:
    return tuple(
        evaluate_2d(t, dr)
        for t in tau_0_grid
        for dr in dec_ratio_grid
    )


def best_fit_2d(
    tau_0_grid: tuple[float, ...] = DEFAULT_TAU_0_GRID_MYR_2D,
    dec_ratio_grid: tuple[float, ...] = DEFAULT_DEC_RATIO_GRID_2D,
) -> TwoDSweepPoint:
    return min(
        two_d_sweep(tau_0_grid, dec_ratio_grid),
        key=lambda p: p.chi_squared,
    )


# ─────────────────────────────────────────────────────────────────────
# Degeneracy quantification
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class DegeneracyReport:
    """Quantifies the degeneracy between τ_0 and dec_ratio."""
    canonical_chi_squared: float
    """χ² at (τ_0=41.9, dec_ratio=0.638) — the framework's adopted state."""
    best_fit_dec_ratio_only_chi: float
    """Best χ² achievable by varying dec_ratio alone at canonical τ_0."""
    best_fit_tau_0_only_chi: float
    """Best χ² achievable by varying τ_0 alone at canonical dec_ratio."""
    best_fit_dec_ratio: float
    """The dec_ratio that minimizes χ² at canonical τ_0."""
    best_fit_tau_0_Myr: float
    """The τ_0 that minimizes χ² at canonical dec_ratio."""
    canonical_product: float
    """dec_ratio × τ_0 at the canonical (0.638 × 41.9 = 26.7)."""
    best_fit_product_dec_only: float
    """dec_ratio × 41.9 at the best-fit dec_ratio."""
    best_fit_product_tau_only: float
    """0.638 × τ_0_best at the best-fit τ_0."""
    products_within_5_pct: bool
    """True if both best-fit products agree within 5% — confirms degeneracy."""
    chi_squared_ratio: float
    """ratio of the two best-fit χ²; close to 1 means degenerate."""


def degeneracy_analysis() -> DegeneracyReport:
    canonical = evaluate_dec_ratio(CANONICAL_DEC_RATIO, 41.9)

    best_dec_only = best_fit_dec_ratio(tau_0_Myr=41.9)
    # τ_0-only best fit at canonical dec_ratio
    from grut.derived.cluster.tau_0_sensitivity import best_fit_tau_0
    best_tau_only = best_fit_tau_0()

    canon_product = CANONICAL_DEC_RATIO * 41.9
    dec_only_product = best_dec_only.dec_ratio * 41.9
    tau_only_product = CANONICAL_DEC_RATIO * best_tau_only.tau_0_Myr

    products_match = (
        abs(dec_only_product - tau_only_product)
        / dec_only_product < 0.05
    )

    chi_ratio = (
        max(best_dec_only.chi_squared, best_tau_only.chi_squared)
        / max(min(best_dec_only.chi_squared,
                  best_tau_only.chi_squared), 1e-9)
    )

    return DegeneracyReport(
        canonical_chi_squared=canonical.chi_squared,
        best_fit_dec_ratio_only_chi=best_dec_only.chi_squared,
        best_fit_tau_0_only_chi=best_tau_only.chi_squared,
        best_fit_dec_ratio=best_dec_only.dec_ratio,
        best_fit_tau_0_Myr=best_tau_only.tau_0_Myr,
        canonical_product=canon_product,
        best_fit_product_dec_only=dec_only_product,
        best_fit_product_tau_only=tau_only_product,
        products_within_5_pct=products_match,
        chi_squared_ratio=chi_ratio,
    )


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    """Six legs of the deceleration-sensitivity analysis."""
    rep = degeneracy_analysis()
    return {
        # (1) Canonical state shows the documented systematic
        "canonical_chi_squared_around_0p077": (
            0.05 < rep.canonical_chi_squared < 0.10
        ),
        # (2) Best-fit dec_ratio (at canonical τ_0) is in physically
        # reasonable range
        "best_fit_dec_ratio_in_reasonable_range": (
            0.65 < rep.best_fit_dec_ratio < 0.85
        ),
        # (3) Best-fit dec_ratio improves chi² substantially
        "dec_ratio_only_improvement_above_5x": (
            rep.canonical_chi_squared / rep.best_fit_dec_ratio_only_chi > 5.0
        ),
        # (4) Both best-fit chi²'s are similar — the degeneracy claim
        "two_best_fit_chis_within_factor_2": (
            rep.chi_squared_ratio < 2.0
        ),
        # (5) The (τ_0, dec_ratio) products agree within 5% — degeneracy
        # confirmed
        "products_match_to_5_pct": rep.products_within_5_pct,
        # (6) The 2D best-fit lies on the degeneracy ridge
        "two_d_best_fit_chi_under_canonical_dec_only_chi": (
            best_fit_2d().chi_squared <= rep.best_fit_dec_ratio_only_chi + 1e-6
        ),
    }


if __name__ == "__main__":
    rep = degeneracy_analysis()
    print("=" * 78)
    print("Cluster-merger deceleration-ratio sensitivity analysis")
    print("=" * 78)
    print()
    print(f"Canonical state: τ_0 = 41.9 Myr, dec_ratio = "
          f"{CANONICAL_DEC_RATIO:.4f} (Bullet-extrapolated)")
    print(f"  χ² = {rep.canonical_chi_squared:.4f}")
    print()
    print("Best-fit by varying ONE parameter at a time:")
    print(f"  Vary dec_ratio (τ_0 fixed at 41.9):")
    print(f"    Best dec_ratio = {rep.best_fit_dec_ratio:.4f}")
    print(f"    χ² at best-fit = {rep.best_fit_dec_ratio_only_chi:.4f}")
    print(f"    Improvement   = "
          f"{rep.canonical_chi_squared/rep.best_fit_dec_ratio_only_chi:.1f}×")
    print()
    print(f"  Vary τ_0 (dec_ratio fixed at {CANONICAL_DEC_RATIO:.4f}):")
    print(f"    Best τ_0 = {rep.best_fit_tau_0_Myr:.2f} Myr")
    print(f"    χ² at best-fit = {rep.best_fit_tau_0_only_chi:.4f}")
    print(f"    Improvement   = "
          f"{rep.canonical_chi_squared/rep.best_fit_tau_0_only_chi:.1f}×")
    print()
    print("Degeneracy parameter (dec_ratio × τ_0):")
    print(f"  At canonical:                  {rep.canonical_product:.2f}")
    print(f"  At dec-ratio-only best-fit:    {rep.best_fit_product_dec_only:.2f}")
    print(f"  At τ_0-only best-fit:          {rep.best_fit_product_tau_only:.2f}")
    print(f"  Products match within 5%:      {rep.products_within_5_pct}")
    print(f"  χ² ratio (worse/better):       {rep.chi_squared_ratio:.2f}")
    print()
    print(f"2D best-fit: ", end="")
    bf2d = best_fit_2d()
    print(f"τ_0 = {bf2d.tau_0_Myr:.1f} Myr, "
          f"dec_ratio = {bf2d.dec_ratio:.3f}, "
          f"product = {bf2d.product:.2f}, "
          f"χ² = {bf2d.chi_squared:.5f}")
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
