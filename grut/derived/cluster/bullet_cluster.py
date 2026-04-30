"""Bullet Cluster — memory-kernel offset calculation.

Apply GRUT's constitutive memory kernel to cluster-collision geometry.
The Bullet Cluster (1E 0657-558) is Track VII's primary cluster-scale
falsifier: in the standard CDM picture the gas-lensing offset is
attributed to a separate collisionless DM component; in GRUT, no such
component exists — the offset arises from the retarded gravitational
response of the responsive vacuum to the gas's own (decelerating) mass
distribution.

What's distinct between the two interpretations
-----------------------------------------------

Both pictures agree on KINEMATIC observables:
    cluster-to-cluster separation today = v_initial × t_since_pericenter
                                        ≈ 4700 km/s × 150 Myr
                                        ≈ 720 kpc
This is just kinematics — any theory predicts it.

GRUT-SPECIFIC prediction is the gas-to-LENSING offset WITHIN each
cluster — i.e. the spatial separation between the X-ray gas peak
(where the matter is now) and the lensing peak (where the
gravitational potential currently has its maximum):

    δ_GRUT = ⟨x_gas⟩_K(now) − x_gas(now)

where ⟨·⟩_K is the convolution with K(t) = (1/τ_0) exp(−t/τ_0).
For a uniformly-moving point mass v, this gives δ_GRUT = −v × τ_0
(lensing peak is τ_0 of motion BEHIND the current gas position).

Observation: gas-to-lensing offset ~150 kpc per cluster (Clowe et al.
2006, Markevitch et al. 2002). GRUT prediction: 129-200 kpc depending
on which velocity (post-collision v_final ≈ 3000 km/s or pre-collision
v_initial ≈ 4700 km/s) is used. The full memory-kernel convolution
with a piecewise-linear deceleration profile gives a value in this
band.

References
----------
- D. Clowe et al., "A direct empirical proof of the existence of dark
  matter," ApJ Letters 648 (2006) L109. arXiv:astro-ph/0608407.
- M. Markevitch et al., "A Textbook Example of a Bow Shock in the
  Merging Galaxy Cluster 1E 0657-56," ApJ 567 (2002) L27.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from grut.foundation.closure_protocol import TAU_0_SEC


# ─────────────────────────────────────────────────────────────────────
# Unit conversions and observational data
# ─────────────────────────────────────────────────────────────────────

YEAR_SEC: float = 3.156e7
KPC_M: float = 3.086e19
KM_M: float = 1.0e3


@dataclass(frozen=True)
class BulletClusterObs:
    """Observed parameters for the Bullet Cluster (1E 0657-558).

    Sources: Clowe et al. 2006, Markevitch et al. 2002.
    """
    v_initial_km_s: float = 4700.0     # pre-collision relative velocity
    v_final_km_s:   float = 3000.0     # post-collision (gas slowed by ram pressure)
    t_since_Myr:    float = 150.0      # time since pericenter
    gas_lensing_offset_kpc:    float = 150.0  # per-cluster gas-to-lensing offset
    cluster_cluster_separation_kpc: float = 720.0  # ≈ v_initial × t_since
    notes: str = (
        "Bullet Cluster (1E 0657-558); Clowe et al. 2006, "
        "Markevitch et al. 2002. Per-cluster gas-to-lensing offset "
        "is the GRUT-specific falsifier. Cluster-to-cluster "
        "separation is kinematic and agnostic to the gravity theory."
    )


BULLET_OBS: BulletClusterObs = BulletClusterObs()


# ─────────────────────────────────────────────────────────────────────
# Kinematic baseline (independent of GRUT)
# ─────────────────────────────────────────────────────────────────────

def kinematic_cluster_separation_m(
    v_km_s: float = BULLET_OBS.v_initial_km_s,
    t_since_Myr: float = BULLET_OBS.t_since_Myr,
) -> float:
    """v × t_since_pericenter — the cluster-to-cluster separation today.

    Independent of GRUT; reproduced by any theory. Returns metres.
    """
    return v_km_s * KM_M * t_since_Myr * 1e6 * YEAR_SEC


def kinematic_cluster_separation_kpc(**kwargs) -> float:
    return kinematic_cluster_separation_m(**kwargs) / KPC_M


# ─────────────────────────────────────────────────────────────────────
# Simple GRUT prediction: leading-order memory-kernel offset
# ─────────────────────────────────────────────────────────────────────

def grut_offset_simple_m(
    v_km_s: float,
    tau_0_sec: float = TAU_0_SEC,
) -> float:
    """v × τ_0 — leading-order GRUT prediction for gas-to-lensing offset.

    Derivation: for a uniformly moving point mass at velocity v, the
    kernel-convolved position is

        ⟨x⟩_K = (1/τ_0) ∫_0^∞ exp(−s/τ_0) (x − v·s) ds = x − v·τ_0

    so the lensing peak sits v×τ_0 BEHIND the current mass position.
    """
    return v_km_s * KM_M * tau_0_sec


def grut_offset_simple_kpc(v_km_s: float, **kwargs) -> float:
    return grut_offset_simple_m(v_km_s, **kwargs) / KPC_M


# ─────────────────────────────────────────────────────────────────────
# Full memory-kernel convolution with deceleration profile
# ─────────────────────────────────────────────────────────────────────

def gas_trajectory(
    t_offset_sec: float,
    v_initial_m_s: float,
    v_final_m_s: float,
    t_since_pericenter_sec: float,
    t_collision_sec: float = 30.0 * 1e6 * YEAR_SEC,  # ~30 Myr gas-crossing
) -> float:
    """1D gas position (in metres) at time t_offset (now − t_offset).

    Convention: t_offset_sec ≥ 0 is time INTO THE PAST. Returns the
    gas's x-coordinate relative to its current position (so x(0) = 0).

    Piecewise-linear velocity profile:
        - Pre-collision  (t in past > t_since_pericenter):     v_initial
        - During collision (t in past in [t_since_pericenter, t_since_pericenter + t_collision]):
            linear deceleration from v_initial → v_final
        - Post-collision (t in past < t_since_pericenter):     v_final
    """
    if t_offset_sec < 0:
        return 0.0

    t_pp = t_since_pericenter_sec  # time-into-past at pericenter
    t_coll = t_collision_sec

    if t_offset_sec <= t_pp:
        # Post-collision regime: gas moving at v_final from now back to pericenter
        # Position relative to now (where gas is now at x=0):
        # x_gas(now − s) = +v_final × s   (gas was AHEAD of its current spot in the past)
        return v_final_m_s * t_offset_sec

    if t_offset_sec <= t_pp + t_coll:
        # During-collision regime: linear deceleration
        # Position at pericenter: v_final × t_pp
        # Velocity ramping linearly with τ from v_initial back to v_final
        s_in_collision = t_offset_sec - t_pp  # 0 → t_coll
        # Velocity in past was higher than v_final by linear ramp
        # v(s) at s_in_collision = v_final + (v_initial − v_final) × (s_in_collision / t_coll)
        # Position contribution: integrate v(s') ds' from 0 to s_in_collision
        v_diff = v_initial_m_s - v_final_m_s
        x_during = v_final_m_s * s_in_collision + 0.5 * v_diff * s_in_collision**2 / t_coll
        return v_final_m_s * t_pp + x_during

    # Pre-collision: gas moving at v_initial back through time
    s_pre = t_offset_sec - (t_pp + t_coll)
    x_at_collision_start = (
        v_final_m_s * t_pp
        + v_final_m_s * t_coll
        + 0.5 * (v_initial_m_s - v_final_m_s) * t_coll
    )
    return x_at_collision_start + v_initial_m_s * s_pre


def grut_offset_kernel_convolution_m(
    v_initial_km_s: float = BULLET_OBS.v_initial_km_s,
    v_final_km_s:   float = BULLET_OBS.v_final_km_s,
    t_since_Myr:    float = BULLET_OBS.t_since_Myr,
    tau_0_sec:      float = TAU_0_SEC,
    t_collision_Myr: float = 30.0,
    n_samples:      int = 4000,
    s_max_factor:   float = 30.0,  # integrate out to 30 × τ_0
) -> float:
    """Full memory-kernel convolution of the gas trajectory.

        x_lensing = (1/τ_0) ∫_0^∞ exp(−s/τ_0) x_gas(now − s) ds

    where x_gas(now − s) is the piecewise-linear deceleration model.
    Returns x_lensing − x_gas(now) = x_lensing (since x_gas(now) = 0).

    Numerical integration uses a uniform grid over [0, s_max], where
    s_max = s_max_factor × τ_0. The exponential weight ensures the
    tail beyond ~10 τ_0 contributes negligibly.
    """
    v_i = v_initial_km_s * KM_M
    v_f = v_final_km_s * KM_M
    t_pp = t_since_Myr * 1e6 * YEAR_SEC
    t_coll = t_collision_Myr * 1e6 * YEAR_SEC

    s_max = s_max_factor * tau_0_sec
    s_grid = np.linspace(0.0, s_max, n_samples)
    ds = s_grid[1] - s_grid[0]
    weights = np.exp(-s_grid / tau_0_sec) / tau_0_sec

    x_vals = np.array([
        gas_trajectory(s, v_i, v_f, t_pp, t_coll)
        for s in s_grid
    ])
    integrand = weights * x_vals
    return float(np.trapezoid(integrand, dx=ds))


def grut_offset_kernel_convolution_kpc(**kwargs) -> float:
    return grut_offset_kernel_convolution_m(**kwargs) / KPC_M


# ─────────────────────────────────────────────────────────────────────
# Reporting
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class BulletClusterReport:
    grut_simple_v_initial_kpc: float
    grut_simple_v_final_kpc: float
    grut_kernel_convolution_kpc: float
    kinematic_separation_kpc: float
    obs_gas_lensing_kpc: float
    obs_cluster_separation_kpc: float
    grut_in_observation_band: bool
    kinematic_matches_observation: bool


def bullet_cluster_report(
    obs: BulletClusterObs = BULLET_OBS,
    tau_0_sec: float = TAU_0_SEC,
) -> BulletClusterReport:
    """Assemble all four numerical predictions and the comparison verdicts."""
    grut_simple_v_initial = grut_offset_simple_kpc(obs.v_initial_km_s, tau_0_sec=tau_0_sec)
    grut_simple_v_final = grut_offset_simple_kpc(obs.v_final_km_s, tau_0_sec=tau_0_sec)
    grut_full = grut_offset_kernel_convolution_kpc(
        v_initial_km_s=obs.v_initial_km_s,
        v_final_km_s=obs.v_final_km_s,
        t_since_Myr=obs.t_since_Myr,
        tau_0_sec=tau_0_sec,
    )
    kinematic = kinematic_cluster_separation_kpc(
        v_km_s=obs.v_initial_km_s,
        t_since_Myr=obs.t_since_Myr,
    )

    # GRUT prediction is "in band" if the kernel convolution is within
    # factor 2 of the observed gas-lensing offset (~150 kpc).
    band_lo = 0.5 * obs.gas_lensing_offset_kpc
    band_hi = 2.0 * obs.gas_lensing_offset_kpc
    in_band = band_lo <= grut_full <= band_hi

    # Kinematic separation matches obs to within 5%.
    kinematic_match = (
        abs(kinematic - obs.cluster_cluster_separation_kpc)
        / obs.cluster_cluster_separation_kpc
    ) < 0.05

    return BulletClusterReport(
        grut_simple_v_initial_kpc=grut_simple_v_initial,
        grut_simple_v_final_kpc=grut_simple_v_final,
        grut_kernel_convolution_kpc=grut_full,
        kinematic_separation_kpc=kinematic,
        obs_gas_lensing_kpc=obs.gas_lensing_offset_kpc,
        obs_cluster_separation_kpc=obs.cluster_cluster_separation_kpc,
        grut_in_observation_band=in_band,
        kinematic_matches_observation=kinematic_match,
    )


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    """Five legs of the Bullet Cluster prediction:

    (1) Simple v_final × τ_0 estimate is order ~130 kpc
    (2) Simple v_initial × τ_0 estimate is order ~200 kpc
    (3) Full kernel convolution is in the 100-300 kpc band
        (within factor 2 of observed ~150 kpc)
    (4) Kinematic v_initial × t_since reproduces observed
        cluster-cluster separation ~720 kpc
    (5) Full kernel convolution is bracketed by simple estimates
        (v_final × τ_0 ≤ kernel ≤ v_initial × τ_0 — the kernel
        averages over the velocity history)
    """
    rep = bullet_cluster_report()
    return {
        "simple_v_final_around_130_kpc": (
            100 < rep.grut_simple_v_final_kpc < 160
        ),
        "simple_v_initial_around_200_kpc": (
            150 < rep.grut_simple_v_initial_kpc < 250
        ),
        "kernel_convolution_in_observation_band": rep.grut_in_observation_band,
        "kinematic_separation_matches_720_kpc": rep.kinematic_matches_observation,
        "kernel_bracketed_by_simple_estimates": (
            rep.grut_simple_v_final_kpc - 1.0
            <= rep.grut_kernel_convolution_kpc
            <= rep.grut_simple_v_initial_kpc + 1.0
        ),
    }


if __name__ == "__main__":
    rep = bullet_cluster_report()
    print("=" * 72)
    print("Bullet Cluster — GRUT memory-kernel prediction")
    print("=" * 72)
    print()
    print("INPUTS (from Clowe et al. 2006, Markevitch et al. 2002):")
    print(f"  v_initial          = {BULLET_OBS.v_initial_km_s:>6.0f} km/s")
    print(f"  v_final            = {BULLET_OBS.v_final_km_s:>6.0f} km/s (gas after ram-pressure)")
    print(f"  t_since_pericenter = {BULLET_OBS.t_since_Myr:>6.0f} Myr")
    print(f"  τ_0                = {TAU_0_SEC / (1e6 * YEAR_SEC):>6.1f} Myr")
    print()
    print("GRUT PREDICTIONS:")
    print(f"  Simple v_final × τ_0:               {rep.grut_simple_v_final_kpc:>6.1f} kpc")
    print(f"  Simple v_initial × τ_0:             {rep.grut_simple_v_initial_kpc:>6.1f} kpc")
    print(f"  FULL KERNEL CONVOLUTION:            {rep.grut_kernel_convolution_kpc:>6.1f} kpc  ← framework prediction")
    print()
    print("KINEMATIC BASELINE (independent of GRUT):")
    print(f"  v_initial × t_since:                {rep.kinematic_separation_kpc:>6.1f} kpc")
    print()
    print("OBSERVATION:")
    print(f"  Gas-to-lensing offset (per cluster): {rep.obs_gas_lensing_kpc:>6.0f} kpc  ← GRUT-specific test")
    print(f"  Cluster-to-cluster separation:       {rep.obs_cluster_separation_kpc:>6.0f} kpc  (kinematic)")
    print()
    print("VERDICT:")
    print(f"  GRUT in observation band (factor 2): {rep.grut_in_observation_band}")
    print(f"  Kinematic separation matches:        {rep.kinematic_matches_observation}")
    print()
    print("Verify:")
    for k, v in verify().items():
        mark = "PASS" if v else "FAIL"
        print(f"  [{mark}] {k}")
