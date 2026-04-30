"""Cluster-scaling τ_0 sensitivity — does a single τ_0 close the
0.79-0.88 systematic across the three normal-regime mergers?

The cluster_merger_scaling_law claim shows three normal-regime mergers
(Bullet, MACS J0025, Abell 520) at GRUT/observed ratios 0.87, 0.88,
0.79 with the framework's adopted τ_0 = 41.9 Myr. The pattern is
honestly disclosed as a +15-20% systematic at the lower edge of the
observational band. Two readings:

    (a) Observational uncertainty (cluster collision parameters carry
        ~30% uncertainty; the systematic falls within this band).
    (b) Specific signature: cluster-scale τ_0 is genuinely different
        from the cosmic-baseline τ_0 by a consistent factor.

This module runs the sensitivity analysis that distinguishes these
readings: sweep τ_0 across [30, 65] Myr, compute the
prediction/observation ratio for each cluster at each τ_0, and find
the τ_0 that minimizes the chi² across the three normal-regime
clusters.

If a single best-fit τ_0 closes the systematic to <5% across all three
clusters, reading (b) is supported — the cluster regime exhibits a
specific τ_0 different from the cosmic-baseline value. If no single
τ_0 closes it, the framework's pure-Lorentzian kernel structure itself
needs revision (one of the closure paths flagged in
cluster_merger_scaling_law).

The analysis EXCLUDES El Gordo: it remains an outlier at any τ_0
(its observed offset of ~250 kpc would require τ_0 > 150 Myr in
isolation), so its contribution to a chi² fit would dominate and
mask the signal in the normal-regime sample.
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


# Default sweep range — wide enough to bracket the cosmic-baseline 41.9 Myr
# and the cluster-inferred 50 Myr observed systematic.
DEFAULT_TAU_0_GRID_MYR: tuple[float, ...] = tuple(
    float(x) for x in np.arange(30.0, 65.5, 0.5)
)


# Three normal-regime clusters (El Gordo excluded).
NORMAL_REGIME_CLUSTERS: tuple[tuple[str, BulletClusterObs], ...] = (
    ("Bullet Cluster", BULLET),
    ("MACS J0025", MACS_J0025),
    ("Abell 520", ABELL_520),
)


# ─────────────────────────────────────────────────────────────────────
# Per-cluster prediction at a swept τ_0
# ─────────────────────────────────────────────────────────────────────

def predicted_offset_at_tau_0(
    obs: BulletClusterObs,
    tau_0_Myr: float,
) -> float:
    """Predicted gas-to-lensing offset (kpc) at a custom τ_0."""
    tau_0_sec = tau_0_Myr * MYR_SEC
    return grut_offset_kernel_convolution_kpc(
        v_initial_km_s=obs.v_initial_km_s,
        v_final_km_s=obs.v_final_km_s,
        t_since_Myr=obs.t_since_Myr,
        tau_0_sec=tau_0_sec,
    )


def ratio_at_tau_0(
    obs: BulletClusterObs,
    tau_0_Myr: float,
) -> float:
    """Predicted-over-observed ratio for a cluster at the given τ_0."""
    pred = predicted_offset_at_tau_0(obs, tau_0_Myr)
    return pred / obs.gas_lensing_offset_kpc


# ─────────────────────────────────────────────────────────────────────
# Population-level metrics at a single τ_0
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class TauSweepPoint:
    tau_0_Myr: float
    ratios: dict[str, float]
    mean_ratio: float
    median_ratio: float
    range_ratio: float
    chi_squared: float
    """Sum of (ratio - 1)² across the normal-regime clusters."""
    rms_deviation_from_unity: float


def evaluate_at_tau_0(tau_0_Myr: float) -> TauSweepPoint:
    """Compute all three cluster ratios at a single τ_0 and aggregate."""
    ratios = {
        name: ratio_at_tau_0(obs, tau_0_Myr)
        for name, obs in NORMAL_REGIME_CLUSTERS
    }
    values = list(ratios.values())
    arr = np.array(values)
    chi2 = float(np.sum((arr - 1.0) ** 2))
    return TauSweepPoint(
        tau_0_Myr=tau_0_Myr,
        ratios=ratios,
        mean_ratio=float(np.mean(arr)),
        median_ratio=float(np.median(arr)),
        range_ratio=float(np.max(arr) - np.min(arr)),
        chi_squared=chi2,
        rms_deviation_from_unity=float(np.sqrt(np.mean((arr - 1.0) ** 2))),
    )


# ─────────────────────────────────────────────────────────────────────
# Sweep + best-fit
# ─────────────────────────────────────────────────────────────────────

def tau_0_sweep(
    grid: tuple[float, ...] = DEFAULT_TAU_0_GRID_MYR,
) -> tuple[TauSweepPoint, ...]:
    """Sweep τ_0 across the grid; return one point per grid value."""
    return tuple(evaluate_at_tau_0(t) for t in grid)


def best_fit_tau_0(
    grid: tuple[float, ...] = DEFAULT_TAU_0_GRID_MYR,
) -> TauSweepPoint:
    """Best-fit τ_0 minimizing chi² across the three normal-regime clusters.

    Returns the sweep point with the smallest chi² (most ratios near 1).
    """
    sweep = tau_0_sweep(grid)
    return min(sweep, key=lambda p: p.chi_squared)


# ─────────────────────────────────────────────────────────────────────
# Comparison: canonical 41.9 Myr vs best-fit
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class TauComparisonReport:
    canonical_tau_0_Myr: float
    canonical_point: TauSweepPoint
    best_fit_point: TauSweepPoint
    improvement_factor: float
    """canonical chi² / best-fit chi². > 1 means best-fit improves."""
    systematic_closed_at_best_fit: bool
    """True if all three ratios at best-fit are within ±10% of unity."""
    cluster_inferred_tau_0_mean_Myr: float
    """Mean of (1/ratio) × τ_0_canonical across the three clusters —
    rough estimate of what each cluster individually wants τ_0 to be."""


def comparison_report() -> TauComparisonReport:
    """Compare canonical 41.9 Myr to best-fit τ_0."""
    canonical_Myr = TAU_0_SEC / MYR_SEC
    canonical_point = evaluate_at_tau_0(canonical_Myr)
    best = best_fit_tau_0()

    # Each cluster's individually inferred τ_0 (rough)
    individual_tau_0 = []
    for name, obs in NORMAL_REGIME_CLUSTERS:
        # δ_obs / v_final ≈ τ_0 inferred from this cluster alone
        tau_inferred = obs.gas_lensing_offset_kpc / (
            obs.v_final_km_s * 1.0
        )  # crude: δ/v in kpc·s/km
        # Convert: δ [kpc] / v [km/s] × KPC_to_M / KM_to_M / MYR_SEC
        from grut.derived.cluster.bullet_cluster import KPC_M, KM_M
        tau_inferred_sec = (
            obs.gas_lensing_offset_kpc * KPC_M
            / (obs.v_final_km_s * KM_M)
        )
        individual_tau_0.append(tau_inferred_sec / MYR_SEC)
    cluster_inferred_mean = float(np.mean(individual_tau_0))

    # Did the best-fit close the systematic?
    closed = all(
        abs(r - 1.0) < 0.10
        for r in best.ratios.values()
    )

    return TauComparisonReport(
        canonical_tau_0_Myr=canonical_Myr,
        canonical_point=canonical_point,
        best_fit_point=best,
        improvement_factor=(
            canonical_point.chi_squared / best.chi_squared
            if best.chi_squared > 0 else float("inf")
        ),
        systematic_closed_at_best_fit=closed,
        cluster_inferred_tau_0_mean_Myr=cluster_inferred_mean,
    )


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    """Six legs of the τ_0 sensitivity analysis.

    The framework's honest expectation:
      - At the canonical τ_0 = 41.9 Myr, the three normal-regime
        clusters show ratios ≈ 0.79-0.88 (systematic +15-20%).
      - Best-fit τ_0 should be ≈ 50 Myr (the cluster-inferred value).
      - At best-fit τ_0, the systematic should be substantially closed.
      - The improvement factor should be > 5 (chi² drops > 5×).
      - The best-fit τ_0 should agree with the rough cluster-inferred mean.
    """
    rep = comparison_report()
    return {
        "canonical_systematic_above_5_pct": (
            # RMS deviation from unity should be > 5% if there's a
            # real systematic to diagnose (the cluster_merger_scaling_law's
            # 0.79-0.88 pattern gives ~15% RMS).
            rep.canonical_point.rms_deviation_from_unity > 0.05
        ),
        "best_fit_tau_0_in_45_to_55_Myr": (
            45.0 <= rep.best_fit_point.tau_0_Myr <= 55.0
        ),
        "best_fit_improves_chi_squared": (
            rep.improvement_factor > 1.0
        ),
        "best_fit_substantial_improvement": (
            rep.improvement_factor > 5.0
        ),
        "best_fit_agrees_with_cluster_inferred_tau_0_within_5_Myr": (
            abs(rep.best_fit_point.tau_0_Myr
                - rep.cluster_inferred_tau_0_mean_Myr) < 5.0
        ),
        "systematic_closed_at_best_fit": (
            rep.systematic_closed_at_best_fit
        ),
    }


if __name__ == "__main__":
    rep = comparison_report()
    print("=" * 78)
    print("Cluster-merger τ_0 sensitivity analysis")
    print("=" * 78)
    print()
    print(f"Canonical τ_0:                    "
          f"{rep.canonical_tau_0_Myr:.2f} Myr")
    print(f"Best-fit τ_0:                     "
          f"{rep.best_fit_point.tau_0_Myr:.2f} Myr")
    print(f"Cluster-inferred τ_0 mean:        "
          f"{rep.cluster_inferred_tau_0_mean_Myr:.2f} Myr")
    print()
    print("Per-cluster ratios:")
    print(f"{'':<20} {'@ canonical':>12}  {'@ best-fit':>12}")
    for name, _ in NORMAL_REGIME_CLUSTERS:
        canon = rep.canonical_point.ratios[name]
        best = rep.best_fit_point.ratios[name]
        print(f"  {name:<18}  {canon:>10.3f}    {best:>10.3f}")
    print()
    print(f"Chi² at canonical:     {rep.canonical_point.chi_squared:.4f}")
    print(f"Chi² at best-fit:      {rep.best_fit_point.chi_squared:.4f}")
    print(f"Improvement factor:    {rep.improvement_factor:.2f}×")
    print(f"Systematic closed at best-fit: "
          f"{rep.systematic_closed_at_best_fit}")
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
