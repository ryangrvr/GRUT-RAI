"""GRUT — Cosmic-history evolution of X = ωτ_0 with ω = H.

Investigation: COSMIC_X_CROSSOVER_INVESTIGATION.md.
Stage 2: forward derivation of X_cosmic(z) from the framework's
existing constitutive susceptibility χ(ω) = α/(1+(ωτ_0)²) under
the Stage-1 identification ω = H for cosmic-scale gravitational
dynamics.

SCOPE BOUNDARIES (load-bearing):

This module computes the framework's regime classification for ONE
specific case: atomic-scale test-particle perturbations of the
cosmic background, where ω = H dominates. It does NOT:
  - address T_c provenance (open negative #15 stays active)
  - propose Chapter 13 revisions
  - claim that X_cosmic crossover REPLACES T_c crossing as the
    cosmic-history mechanism
  - claim that atomic-scale perturbations are THE load-bearing
    mass class for cosmic-history regime evolution
  - downgrade any open negative

MASS-CLASS NARROWNESS: the framework's regime classification
X = max(ω, Λ_grav) × τ_0 depends on which mass class is asked
about. For atomic test particles, H dominates Λ_grav by ~10³⁸
across all cosmic epochs (H/Λ_grav at cosmic separation l = c/H
reduces to ℏc/(Gm²), redshift-independent). For stellar mass and
larger, Λ_grav dominates H by 76+ orders of magnitude — those
mass classes experience X ≫ 1 at all epochs, no crossover.
This module computes the atomic-scale reading specifically.
Whether atomic-scale physics is the load-bearing mass class for
cosmic-history regime evolution is a separate, unanswered question.

The deliverable is the X(z) curve and X = 1 crossing redshift for
atomic-scale perturbations under standard ΛCDM Friedmann dynamics,
with sensitivity to H_0 choice (Planck 67.4 vs framework 68.8).
The relationship to T_c or other cosmic-history features is
research-tier and not addressed here.

Methodology: standard cosmology Friedmann equations + the
framework's τ_0 = 41.9 Myr. The Friedmann part is not GRUT-specific;
the τ_0 is. The combination is a one-line calculation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from grut.foundation.constants import C as C_LIGHT, G, HBAR
from grut.foundation.closure_protocol import (
    H_0_IMPLIED_KM_S_MPC,
    MPC_IN_M,
    TAU_0_SEC,
)

# Test-mass scales for Λ_grav verification (Stage 3)
M_AMU_KG: float = 1.66053906660e-27           # atomic mass unit
M_SUN_KG: float = 1.989e30                     # solar mass
M_GALAXY_KG: float = 1e11 * M_SUN_KG           # ~Milky Way
M_CLUSTER_KG: float = 1e15 * M_SUN_KG          # ~Coma cluster scale


# ─────────────────────────────────────────────────────────────────────
# Cosmology parameters (Planck 2018 flat ΛCDM; framework-aligned)
# ─────────────────────────────────────────────────────────────────────

# H_0 sensitivity choices
H_0_PLANCK_KM_S_MPC: float = 67.4    # Planck 2018 base ΛCDM
H_0_FRAMEWORK_KM_S_MPC: float = H_0_IMPLIED_KM_S_MPC  # ≈ 68.8 from cosmic-baseline

# Density parameters (Planck 2018 baseline; framework imports Ω_m)
OMEGA_M: float = 0.311
OMEGA_R: float = 9.18e-5    # photons + 3 ν, today
# Ω_Λ enforced flat: 1 - Ω_m - Ω_r ≈ 0.689


def hubble_per_s(H_0_km_s_Mpc: float) -> float:
    """Convert H_0 from km/s/Mpc to s⁻¹."""
    return H_0_km_s_Mpc * 1000.0 / MPC_IN_M


# ─────────────────────────────────────────────────────────────────────
# Friedmann H(z) — standard ΛCDM
# ─────────────────────────────────────────────────────────────────────

def hubble_z(z: float, H_0_km_s_Mpc: float = H_0_PLANCK_KM_S_MPC,
            omega_m: float = OMEGA_M, omega_r: float = OMEGA_R) -> float:
    """H(z) [s⁻¹] in flat ΛCDM:

        H(z)² = H_0² × [Ω_r(1+z)⁴ + Ω_m(1+z)³ + Ω_Λ]

    where Ω_Λ = 1 - Ω_m - Ω_r (flatness)."""
    omega_lambda = 1.0 - omega_m - omega_r
    one_plus_z = 1.0 + z
    H_sq_factor = (
        omega_r * one_plus_z**4
        + omega_m * one_plus_z**3
        + omega_lambda
    )
    return hubble_per_s(H_0_km_s_Mpc) * math.sqrt(H_sq_factor)


def x_cosmic_z(z: float, H_0_km_s_Mpc: float = H_0_PLANCK_KM_S_MPC,
               omega_m: float = OMEGA_M, omega_r: float = OMEGA_R) -> float:
    """X_cosmic(z) = H(z) × τ_0 — the framework's cosmic-scale
    crystallinity parameter under the Stage-1 identification
    ω = H."""
    return hubble_z(z, H_0_km_s_Mpc, omega_m, omega_r) * TAU_0_SEC


# ─────────────────────────────────────────────────────────────────────
# Find the X = 1 crossing redshift
# ─────────────────────────────────────────────────────────────────────

def find_x_crossing_redshift(
    H_0_km_s_Mpc: float = H_0_PLANCK_KM_S_MPC,
    omega_m: float = OMEGA_M,
    omega_r: float = OMEGA_R,
    target_X: float = 1.0,
    z_min: float = 0.0,
    z_max: float = 3500.0,
    tolerance: float = 1e-6,
) -> float:
    """Bisection search for redshift where X_cosmic(z) = target_X.

    X_cosmic is monotonically increasing in z (H increases with z),
    so bisection is well-defined. Returns z such that
    X_cosmic(z) = target_X within tolerance."""
    f_min = x_cosmic_z(z_min, H_0_km_s_Mpc, omega_m, omega_r) - target_X
    f_max = x_cosmic_z(z_max, H_0_km_s_Mpc, omega_m, omega_r) - target_X
    if f_min * f_max > 0:
        # Crossing not in range; return the boundary
        return z_min if abs(f_min) < abs(f_max) else z_max

    lo, hi = z_min, z_max
    while hi - lo > tolerance:
        mid = 0.5 * (lo + hi)
        f_mid = x_cosmic_z(mid, H_0_km_s_Mpc, omega_m, omega_r) - target_X
        if f_mid * f_min < 0:
            hi = mid
        else:
            lo = mid
            f_min = f_mid
    return 0.5 * (lo + hi)


# ─────────────────────────────────────────────────────────────────────
# Per-epoch evaluation
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class EpochEntry:
    name: str
    z: float
    H_per_s: float
    X_cosmic: float
    regime: str


def regime_label(X: float) -> str:
    if X > 100:
        return "deep crystal (refractive enhancement strongly suppressed)"
    elif X > 1.0:
        return "crystal regime (refractive enhancement suppressed by factor ~1+X²)"
    elif X > 0.01:
        return "near-boundary fluid regime"
    else:
        return "deep fluid (full refractive enhancement)"


def evaluate_epochs(
    H_0_km_s_Mpc: float = H_0_PLANCK_KM_S_MPC,
    omega_m: float = OMEGA_M,
    omega_r: float = OMEGA_R,
) -> tuple[EpochEntry, ...]:
    """Evaluate X_cosmic at canonical cosmic epochs."""
    epochs: list[tuple[str, float]] = [
        ("today",                                0.0),
        ("z=1 (recent past)",                    1.0),
        ("z=10 (early structure formation)",     10.0),
        ("z=70 (rough X=1 estimate, matter-era)", 70.0),
        ("z=1100 (recombination)",               1100.0),
        ("z=3400 (matter-radiation equality)",   3400.0),
    ]
    out: list[EpochEntry] = []
    for name, z in epochs:
        H = hubble_z(z, H_0_km_s_Mpc, omega_m, omega_r)
        X = H * TAU_0_SEC
        out.append(EpochEntry(name, z, H, X, regime_label(X)))
    return tuple(out)


# ─────────────────────────────────────────────────────────────────────
# Stage 3 — Λ_grav vs H verification at cosmic scales
# ─────────────────────────────────────────────────────────────────────

def lambda_grav_at_cosmic_separation(mass_kg: float, H_per_s: float) -> float:
    """Λ_grav = G m² / (ℏ × l) evaluated at cosmic-scale separation
    l = c / H (Hubble length).

    Substituting l = c/H:
        Λ_grav = G m² H / (ℏ c)

    This is the body-pair decoherence rate between two bodies of mass m
    separated by the Hubble length at the relevant epoch."""
    return G * mass_kg**2 * H_per_s / (HBAR * C_LIGHT)


def H_over_lambda_grav(mass_kg: float, H_per_s: float) -> float:
    """Ratio H / Λ_grav at cosmic-scale separation l = c/H.

    KEY STRUCTURAL FACT: substituting l = c/H gives
        Λ_grav = G m² H / (ℏ c)
    so
        H / Λ_grav = ℏ c / (G m²)

    This is REDSHIFT-INDEPENDENT (doesn't depend on H). For fixed
    test-particle mass, the H >> Λ_grav comparison holds the same
    way at all cosmic epochs.
    """
    return HBAR * C_LIGHT / (G * mass_kg**2)


def verify_h_dominates_lambda_grav() -> dict:
    """Stage 3 verification: for cosmic-scale gravitational dynamics
    interpreted as the wave response of the background to test-
    particle perturbations, H dominates over Λ_grav.

    This computes the redshift-independent H/Λ_grav ratio for several
    representative mass scales:
      - Atomic test particle (m = AMU)
      - Stellar mass (M_sun)
      - Galactic mass (10^11 M_sun)
      - Cluster mass (10^15 M_sun)

    For COSMIC-SCALE DYNAMICS the appropriate "test mass" is small
    (atomic / stellar). For body-pair decoherence between large
    structures (galaxies, clusters), Λ_grav dominates H — but that's
    a DIFFERENT question (compact-object decoherence) than cosmic-
    history regime evolution.

    Per the framework's Ch 4 regime classification, cosmic dynamics
    use ω = H as the dominant rate. This Stage 3 verification confirms
    that for test-particle physics at cosmic scales, H >> Λ_grav. For
    compact-object decoherence at cosmic scales, Λ_grav can be larger
    than H — but compact-object decoherence isn't the rate driving
    cosmic-history regime evolution.
    """
    test_masses = {
        "atomic test particle (AMU)": M_AMU_KG,
        "stellar mass (M_sun)": M_SUN_KG,
        "galactic mass (10¹¹ M_sun)": M_GALAXY_KG,
        "cluster mass (10¹⁵ M_sun)": M_CLUSTER_KG,
    }

    results: list[dict] = []
    for name, m in test_masses.items():
        ratio = H_over_lambda_grav(m, H_per_s=1.0)  # H_per_s cancels — redshift-indep
        results.append({
            "object_class": name,
            "mass_kg": m,
            "H_over_Lambda_grav_redshift_indep": ratio,
            "H_dominates": ratio > 1.0,
            "log10_ratio": (
                math.log10(ratio) if ratio > 0 else float("-inf")
            ),
            "interpretation": (
                f"H >> Λ_grav by factor {ratio:.2e} — H clearly dominates"
                if ratio > 1e6 else
                f"H > Λ_grav but only by factor {ratio:.2e} — close call"
                if ratio > 1.0 else
                f"Λ_grav >> H by factor {1.0/ratio:.2e} — body-pair "
                f"decoherence dominates over Hubble rate at cosmic scales"
            ),
        })

    return {
        "structural_fact": (
            "H/Λ_grav at cosmic separation l = c/H reduces to "
            "ℏc/(Gm²), which is REDSHIFT-INDEPENDENT. The dominance "
            "of H over Λ_grav holds the same way at all cosmic "
            "epochs, depending only on the test-particle mass."
        ),
        "per_mass_class": results,
        "mass_class_dependence_finding": (
            "The framework's regime classification gives different "
            "X values for different mass classes at the same cosmic "
            "epoch. For atomic test particles (AMU): H/Λ_grav ≈ "
            "10³⁸, H dominates, X = H × τ_0 → crossing at z ≈ 71. "
            "For stellar mass and up: Λ_grav dominates H by 76+ "
            "orders → X ≫ 1 at all epochs, no crossover. "
            "Different mass classes experience different regime "
            "classifications at the same cosmic epoch. The X = 1 "
            "crossing in this calculation applies to atomic-scale "
            "perturbations specifically."
        ),
        "open_question_unaddressed": (
            "Whether atomic-scale perturbations are the load-bearing "
            "mass class for cosmic-history regime evolution is a "
            "SEPARATE QUESTION not answered by this calculation. "
            "Answering it would require deriving from framework "
            "infrastructure which mass class dominates the medium's "
            "wave-response physics at cosmic scales — research-tier "
            "work involving the bandwidth integral, multi-mode "
            "integration over the cosmological perturbation field, "
            "and the n_g(ω) covariance question (#9). This claim "
            "registers what was computed for one specific mass "
            "class; broader cosmic-history mechanism questions stay "
            "open."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Master attempt
# ─────────────────────────────────────────────────────────────────────

def cosmic_x_crossover_attempt() -> dict:
    """Full Stage-2 calculation: X_cosmic(z) under both H_0 values,
    epoch evaluation, X = 1 crossing redshift."""

    # H_0 sensitivity
    z_cross_planck = find_x_crossing_redshift(
        H_0_km_s_Mpc=H_0_PLANCK_KM_S_MPC,
    )
    z_cross_framework = find_x_crossing_redshift(
        H_0_km_s_Mpc=H_0_FRAMEWORK_KM_S_MPC,
    )

    # T at crossing (CMB temperature scaling: T ∝ (1+z))
    T_CMB_today = 2.7255  # K
    T_at_cross_planck = T_CMB_today * (1.0 + z_cross_planck)
    T_at_cross_framework = T_CMB_today * (1.0 + z_cross_framework)

    # Per-epoch evaluation under Planck cosmology
    epochs_planck = evaluate_epochs(H_0_km_s_Mpc=H_0_PLANCK_KM_S_MPC)

    # Stage 3 verification
    lambda_check = verify_h_dominates_lambda_grav()

    return {
        "scope_notice": (
            "Stage 2 of cosmic_x_crossover investigation. ONE "
            "specific framework prediction. Does NOT address T_c "
            "provenance, does NOT propose Ch 13 revisions, does NOT "
            "claim X_cosmic replaces T_c as the cosmic-history "
            "mechanism. See COSMIC_X_CROSSOVER_INVESTIGATION.md."
        ),
        "tau_0_sec": TAU_0_SEC,
        "H_0_choices": {
            "planck_2018": {
                "H_0_km_s_Mpc": H_0_PLANCK_KM_S_MPC,
                "X_at_z_0": x_cosmic_z(0.0, H_0_PLANCK_KM_S_MPC),
                "z_at_X_1": z_cross_planck,
                "T_at_X_1_K": T_at_cross_planck,
            },
            "framework_cosmic_baseline": {
                "H_0_km_s_Mpc": H_0_FRAMEWORK_KM_S_MPC,
                "X_at_z_0": x_cosmic_z(0.0, H_0_FRAMEWORK_KM_S_MPC),
                "z_at_X_1": z_cross_framework,
                "T_at_X_1_K": T_at_cross_framework,
            },
        },
        "epoch_evaluation_planck": [
            {
                "name": e.name,
                "z": e.z,
                "H_per_s": e.H_per_s,
                "X_cosmic": e.X_cosmic,
                "regime": e.regime,
            }
            for e in epochs_planck
        ],
        "qualitative_shape": (
            "X_cosmic(z) is monotonically increasing in z. "
            "Today X ≈ 0.003 (deep fluid). At recombination "
            "(z=1100) X ≈ tens (deep crystal). The X = 1 crossing "
            "occurs in the matter-dominated era at z ≈ 70 — "
            "post-recombination, in the structure-formation epoch."
        ),
        "stage_1_identification": (
            "ω = H for cosmic-scale gravitational dynamics, per "
            "Stage 1 of this investigation. Caveats around mode-by-"
            "mode ω_k = ck/a vs background H, conformal vs proper "
            "frequency, and multi-mode integration are all real and "
            "would matter for tighter analysis. This calculation "
            "uses the simplest Stage-1 identification."
        ),
        "stage_3_lambda_grav_verification": lambda_check,
    }


if __name__ == "__main__":
    result = cosmic_x_crossover_attempt()
    print("=" * 78)
    print("Cosmic X_cosmic = H × τ_0 evolution under Stage-1 ω = H")
    print("=" * 78)
    print()

    print(f"τ_0 = {TAU_0_SEC:.3e} s = 41.9 Myr (framework canonical)")
    print()

    for name, data in result["H_0_choices"].items():
        print(f"H_0 = {data['H_0_km_s_Mpc']} km/s/Mpc ({name}):")
        print(f"  X today (z=0):          {data['X_at_z_0']:.4f}")
        print(f"  z at X = 1:             {data['z_at_X_1']:.2f}")
        print(f"  T_CMB at X = 1:         {data['T_at_X_1_K']:.2f} K")
        print()

    print(f"{'epoch':<40} {'z':>10}  {'X_cosmic':>12}  {'regime':<55}")
    print("-" * 130)
    for e in result["epoch_evaluation_planck"]:
        print(f"{e['name']:<40} {e['z']:>10.2f}  {e['X_cosmic']:>12.3e}  {e['regime']:<55}")
    print()
    print("Qualitative shape:", result["qualitative_shape"])
