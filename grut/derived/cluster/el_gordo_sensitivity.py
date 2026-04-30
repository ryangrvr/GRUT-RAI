"""El Gordo sensitivity analysis — does observation uncertainty close
the factor-3.5 outlier?

El Gordo (ACT-CL J0102-4915) was tagged as a factor-3.5 outlier in the
cluster_merger_scaling_law claim using a specific parameter combination
(v_initial = 2500 km/s, t_since = 110 Myr, dec_ratio = 0.638) and a
specific lensing-offset measurement (250 kpc). But each of those inputs
has substantial published uncertainty:

    Collision velocity v_initial:    2000 - 3500 km/s
    Time since pericenter:            70 - 300 Myr
    Deceleration ratio:               0.5 - 0.85 (uncertain due to mass
                                      asymmetry — different from Bullet)
    Gas-to-lensing offset (per clump): 120 - 600 kpc (depends heavily
                                      on lensing reconstruction method)

Why the offset measurement is uncertain
---------------------------------------

1. **Off-axis collision geometry.** El Gordo is NOT a head-on collision
   like Bullet. Off-axis projections give different "observed offsets"
   depending on viewing angle.

2. **Multi-component substructure.** El Gordo has 4+ identifiable
   subclumps. The "gas peak" and "lensing peak" definitions depend on
   which substructures you track.

3. **Methodology spread.** Strong lensing, weak lensing, combined
   SL+WL, and free-form reconstructions give different peak locations:
       - Jee et al. 2014 (parametric SL+WL): NW clump 600 kpc, SE 300
       - Diego et al. 2023 (free-form): different peak structure
       - Some analyses give per-substructure offsets ~100-150 kpc

4. **High redshift (z=0.87).** Lensing measurements at high z have
   larger uncertainties from source-plane constraints.

5. **Mass asymmetry.** Bullet's ~10:1 mass ratio justifies the dec_ratio
   = 0.638 extrapolation. El Gordo's ~3:1 mass ratio has different
   collision dynamics — both clusters slow down, not just the bullet.

Sensitivity result
------------------

When the framework's prediction is computed across the FULL published
parameter space, the predicted offset ranges from 43 kpc (most-aggressive
parameters) to 131 kpc (least-aggressive parameters). For comparison,
the observed offset published range is 120-600 kpc. The two ranges
OVERLAP at the lower end:

    GRUT best-case prediction:  130 kpc
    Observed lower bound:       120-150 kpc

In that overlap, El Gordo would be consistent with the framework at
ratio ~0.9-1.1 — comparable to the other normal-regime mergers.

Conversely, if the true offset is in the upper part of the observation
range (250-600 kpc), even maximally-favorable parameters leave a
factor 2-5 deviation. The framework's kernel model would need
revision OR there are real off-axis / multi-component effects not
captured.

Honest framing: **El Gordo's deviation is not definitively a framework
problem.** It could be (a) observation uncertainty placing the true
offset at the lower published range, (b) parameter uncertainty placing
v_initial / t_since / dec_ratio at favorable values, OR (c) genuine
extra physics (off-axis projection, multi-component dynamics) the
framework's simple kernel doesn't capture. The data does not
discriminate among (a), (b), and (c).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from grut.derived.cluster.bullet_cluster import (
    BulletClusterObs,
    grut_offset_kernel_convolution_kpc,
)
from grut.foundation.closure_protocol import TAU_0_SEC


YEAR_SEC: float = 3.156e7
MYR_SEC: float = 1e6 * YEAR_SEC


# ─────────────────────────────────────────────────────────────────────
# Published parameter ranges for El Gordo
# ─────────────────────────────────────────────────────────────────────

V_INITIAL_RANGE_KM_S: tuple[float, ...] = (2000, 2500, 3000, 3500)
"""Pre-collision velocity range from Menanteau 2012 / Jee 2014.
Lower bound conservative; upper bound from hydrodynamic simulations
of the inferred collision energetics."""

T_SINCE_RANGE_MYR: tuple[float, ...] = (70, 110, 150, 200, 300)
"""Time since pericenter range; varies by dynamical model. Off-axis
geometry makes this less constrained than for Bullet."""

DEC_RATIO_RANGE: tuple[float, ...] = (0.50, 0.638, 0.75, 0.85)
"""Deceleration ratio v_post / v_initial. Bullet's measured 0.638 is
not necessarily applicable to El Gordo's different mass-ratio merger.
The wider range reflects this asymmetry uncertainty."""

OBSERVED_OFFSET_RANGE_KPC: tuple[float, ...] = (
    120, 150, 200, 250, 300, 400, 600
)
"""Published lensing-offset range. Lower values from individual sub-
cluster centroids; upper values from Jee et al. 2014 NW clump (which
includes off-axis projection effects)."""

CANONICAL_OBSERVED_KPC: float = 250.0
"""The value used in cluster_merger_scaling_law's outlier flag."""


# ─────────────────────────────────────────────────────────────────────
# Sensitivity sweep
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class ElGordoPrediction:
    v_initial: float
    t_since: float
    dec_ratio: float
    v_post: float
    predicted_kpc: float
    is_canonical: bool


def predict_at_params(
    v_initial: float,
    t_since: float,
    dec_ratio: float,
) -> ElGordoPrediction:
    """Run the kernel convolution at given (v_initial, t_since, dec_ratio)."""
    v_post = v_initial * dec_ratio
    pred = grut_offset_kernel_convolution_kpc(
        v_initial_km_s=v_initial,
        v_final_km_s=v_post,
        t_since_Myr=t_since,
    )
    is_canonical = (
        abs(v_initial - 2500) < 1e-6
        and abs(t_since - 110) < 1e-6
        and abs(dec_ratio - 0.638) < 1e-3
    )
    return ElGordoPrediction(
        v_initial=v_initial,
        t_since=t_since,
        dec_ratio=dec_ratio,
        v_post=v_post,
        predicted_kpc=pred,
        is_canonical=is_canonical,
    )


def parameter_sweep() -> tuple[ElGordoPrediction, ...]:
    """All (v_initial, t_since, dec_ratio) combinations from published ranges."""
    return tuple(
        predict_at_params(v, t, d)
        for v in V_INITIAL_RANGE_KM_S
        for t in T_SINCE_RANGE_MYR
        for d in DEC_RATIO_RANGE
    )


# ─────────────────────────────────────────────────────────────────────
# Statistics
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class SensitivityReport:
    n_parameter_combinations: int
    canonical_prediction_kpc: float
    """Prediction at v=2500, t=110, dec=0.638 — the value that gave
    the factor-3.5 outlier flag."""
    min_prediction_kpc: float
    """Most aggressive parameters (lowest predicted offset)."""
    max_prediction_kpc: float
    """Most favorable parameters (highest predicted offset)."""
    median_prediction_kpc: float
    obs_lower_bound_kpc: float
    """Lower bound of published observed-offset range (120 kpc)."""
    obs_upper_bound_kpc: float
    """Upper bound (600 kpc, Jee NW clump)."""
    overlaps_with_obs_range: bool
    """True if any prediction in the parameter sweep falls within the
    observed-offset published range."""
    consistent_at_obs_lower_bound: bool
    """True if max-prediction matches obs lower bound within factor 1.5
    (consistent with the other 3 normal-regime mergers' typical ratio)."""


def sensitivity_report() -> SensitivityReport:
    sweep = parameter_sweep()
    preds = sorted(p.predicted_kpc for p in sweep)
    canonical = next(p for p in sweep if p.is_canonical)
    obs_lo = min(OBSERVED_OFFSET_RANGE_KPC)
    obs_hi = max(OBSERVED_OFFSET_RANGE_KPC)
    overlap = any(obs_lo <= p <= obs_hi for p in preds)
    # "Consistent at lower bound" if the max prediction is within factor
    # 1.5 of the lower observed bound (which would put El Gordo's ratio
    # comparable to the other normal-regime mergers' 0.79-0.88)
    consistent = (
        max(preds) >= obs_lo / 1.5
        and max(preds) <= obs_lo * 1.5
    )
    return SensitivityReport(
        n_parameter_combinations=len(sweep),
        canonical_prediction_kpc=canonical.predicted_kpc,
        min_prediction_kpc=min(preds),
        max_prediction_kpc=max(preds),
        median_prediction_kpc=preds[len(preds) // 2],
        obs_lower_bound_kpc=obs_lo,
        obs_upper_bound_kpc=obs_hi,
        overlaps_with_obs_range=overlap,
        consistent_at_obs_lower_bound=consistent,
    )


def best_case_match() -> tuple[ElGordoPrediction, float]:
    """Return (best prediction, observed offset value that matches it).

    The "best case" is the parameter combination giving the maximum
    predicted offset; the observed offset that would close the
    systematic at ratio ~1 is approximately equal to that prediction.
    """
    sweep = parameter_sweep()
    best = max(sweep, key=lambda p: p.predicted_kpc)
    return best, best.predicted_kpc


# ─────────────────────────────────────────────────────────────────────
# Closure analysis: which observed offset values bring framework into
# agreement at each parameter combination?
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class ClosureScenario:
    description: str
    observed_offset_assumed_kpc: float
    canonical_ratio: float
    best_case_ratio: float
    interpretation: str


def closure_scenarios() -> tuple[ClosureScenario, ...]:
    """Several scenarios for how El Gordo's apparent factor-3.5 deviation
    could resolve."""
    rep = sensitivity_report()
    canon = rep.canonical_prediction_kpc
    best = rep.max_prediction_kpc

    return (
        ClosureScenario(
            description="Canonical (v=2500, t=110, dec=0.638), obs=250 kpc",
            observed_offset_assumed_kpc=250.0,
            canonical_ratio=canon / 250.0,
            best_case_ratio=best / 250.0,
            interpretation=(
                "Original outlier framing. Even with most-favorable "
                "parameters, ratio = 0.52 — factor 2 below."
            ),
        ),
        ClosureScenario(
            description="Lower observed bound (120 kpc, individual subclump centroids)",
            observed_offset_assumed_kpc=120.0,
            canonical_ratio=canon / 120.0,
            best_case_ratio=best / 120.0,
            interpretation=(
                "If true offset is at lower published range (consistent "
                "with some non-parametric reconstructions), "
                "best-case ratio ~1.09 — fully consistent."
            ),
        ),
        ClosureScenario(
            description="Mid-low observed (150 kpc)",
            observed_offset_assumed_kpc=150.0,
            canonical_ratio=canon / 150.0,
            best_case_ratio=best / 150.0,
            interpretation=(
                "Best-case ratio ~0.87 — same as Bullet, MACS, Abell 520. "
                "Framework consistent."
            ),
        ),
        ClosureScenario(
            description="Jee 2014 NW clump (600 kpc)",
            observed_offset_assumed_kpc=600.0,
            canonical_ratio=canon / 600.0,
            best_case_ratio=best / 600.0,
            interpretation=(
                "If true offset is at upper published range, best-case "
                "ratio ~0.22 — factor 4-5 deviation. Framework has a "
                "real problem at this offset value, OR off-axis "
                "projection effects inflate the measured offset."
            ),
        ),
    )


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    rep = sensitivity_report()
    return {
        "sweep_covers_at_least_60_combinations": (
            rep.n_parameter_combinations >= 60
        ),
        "canonical_prediction_around_70_kpc": (
            65 < rep.canonical_prediction_kpc < 80
        ),
        "max_prediction_above_120_kpc": (
            rep.max_prediction_kpc > 120
        ),
        "prediction_range_overlaps_obs_range": (
            rep.overlaps_with_obs_range
        ),
        "consistent_at_lower_obs_bound": (
            rep.consistent_at_obs_lower_bound
        ),
        "best_case_within_factor_1p5_of_obs_lower_bound": (
            rep.max_prediction_kpc / rep.obs_lower_bound_kpc < 1.5
            and rep.max_prediction_kpc / rep.obs_lower_bound_kpc > 0.66
        ),
    }


if __name__ == "__main__":
    rep = sensitivity_report()
    print("=" * 78)
    print("El Gordo sensitivity analysis — does observation uncertainty close")
    print("                                  the factor-3.5 outlier?")
    print("=" * 78)
    print()
    print(f"Parameter combinations swept: {rep.n_parameter_combinations}")
    print(f"  v_initial range:   {min(V_INITIAL_RANGE_KM_S)} - "
          f"{max(V_INITIAL_RANGE_KM_S)} km/s")
    print(f"  t_since range:     {min(T_SINCE_RANGE_MYR)} - "
          f"{max(T_SINCE_RANGE_MYR)} Myr")
    print(f"  dec_ratio range:   {min(DEC_RATIO_RANGE)} - "
          f"{max(DEC_RATIO_RANGE)}")
    print()
    print(f"GRUT predicted offset:")
    print(f"  Min (most aggressive params):  {rep.min_prediction_kpc:.1f} kpc")
    print(f"  Canonical (v=2500/t=110/d=0.638): {rep.canonical_prediction_kpc:.1f} kpc")
    print(f"  Max (most favorable params):   {rep.max_prediction_kpc:.1f} kpc")
    print()
    print(f"Observed offset published range:  "
          f"{rep.obs_lower_bound_kpc:.0f} - {rep.obs_upper_bound_kpc:.0f} kpc")
    print(f"Prediction range overlaps obs range: "
          f"{rep.overlaps_with_obs_range}")
    print()
    print("Closure scenarios:")
    print(f"{'Scenario':<60} {'canon':>7} {'best':>7}")
    print("-" * 78)
    for s in closure_scenarios():
        print(f"  {s.description:<58} {s.canonical_ratio:>7.3f} {s.best_case_ratio:>7.3f}")
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
