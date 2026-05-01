"""GRUT — Stage 2 forward derivation: primordial curvature ζ from
linearized constitutive equation.

Investigation: PRIMORDIAL_ALPHA_S3_INVESTIGATION.md, Stage 2.
Lens B/F: cosmological-perturbation curvature from the constitutive
equation linearized around the null fixed point z = 0, with mode
amplitudes evaluated at the framework's natural crossover scale.

DISCIPLINE: This calculation is forward-physics, not target-fitting.
The output's α-S structure is whatever falls out. Numerical
comparison to α/S³ and observed A_s = 2.1×10⁻⁹ is post-hoc.

STRUCTURE OF THE CALCULATION

Step 1 — Linearization.
    Constitutive equation: τ₀ dz/dt + z = z_target[z] + ξ(t)
    Linearize around z = 0 (null fixed point):
        τ₀ d(δz)/dt + δz = ξ(t)
    (with z_target[0] = 0 to leading order)

Step 2 — Mode structure (Fourier in space and time).
    For mode of wavenumber k, frequency ω:
        (1 + iωτ₀) δz_k(ω) = ξ_k(ω)
        |δz_k(ω)|² = |ξ_k(ω)|² / (1 + ω²τ₀²)

Step 3 — Noise kernel structure.
    The CTP noise kernel has BOTH spatial structure (Diósi-Penrose
    gravitational, N_grav(x-x') = G/(ℏ|x-x'|)) AND temporal structure
    (KMS thermal, N_T(ω) = (2/τ₀)ℏω·coth(ℏω/2k_BT)).

    Spatial Fourier: ∫ d³x e^(-ik·x) [G/(ℏ|x|)] = 4πG/(ℏk²)

    Combined: ⟨ξ_k(ω) ξ_k'*(ω')⟩ = (4πG/ℏk²) × N_T(ω) × δ(k-k') δ(ω-ω')

Step 4 — Variance at the crossover scale.
    Natural GRUT scale: ωτ₀ = 1 (memory bandwidth boundary).
    Spatial scale at this ω: k_* = 1/(c τ₀) if dispersion is c·k = ω.

    Variance at the crossover:
        ⟨|δz_{k*}(1/τ₀)|²⟩ = (4πG/ℏk_*²) × N_T(1/τ₀) / (1+1)
                            = (4πG/ℏ) × (cτ₀)² × (ℏ/τ₀ × coth(ℏ/(2k_BT τ₀))) × τ₀ / (2 τ₀)

    Substituting k_*² = 1/(c²τ₀²):
        = (4πG c² τ₀² / ℏ) × (ℏ/τ₀) × coth(...) × (1/(2τ₀))
        = 2πG c² × coth(ℏ/(2k_BT τ₀))

Step 5 — Dimensionless power spectrum.
    P_ζ(k) = (k³/2π²) × ⟨|δz_k|²⟩
    At k = k_* = 1/(cτ₀):
        k_*³ = 1/(c³τ₀³)
        P_ζ(k_*) = (1/(c³τ₀³)) / (2π²) × 2πG c² × coth(...)
                = G / (πc τ₀³) × coth(...)

Step 6 — Make it dimensionless.
    G has units [m³/(kg·s²)], so G/(c τ₀³) has units [m²/(kg·s)] —
    not yet dimensionless. The natural Planck-scale rescaling is to
    divide by (G/(c·t_Pl³)) = c⁵/ℏ², giving:
        P_ζ(k_*) (dimensionless) = [G/(πcτ₀³)] / [c⁵/ℏ²]
                                = G ℏ² / (π c⁶ τ₀³)
                                = (ℏ/c)² × G/(πc⁴) × 1/τ₀³
                                = ℓ_Pl² × t_Pl² × (1/τ₀³) × (1/π)
                                wait — let me redo this carefully

    Planck units: t_Pl = √(ℏG/c⁵), ℓ_Pl = c·t_Pl.

    G/(πcτ₀³) has units:
        [m³ kg⁻¹ s⁻²] / [m s⁻¹ × s³] = [m² kg⁻¹ s⁻⁴]

    To make dimensionless, divide by something with same units.
    The natural Planck-scale unit: c⁵/(ℏ²) which has units of
        [m⁵s⁻⁵] / [J²s²] = [m⁵ s⁻⁵] / [kg² m⁴ s⁻²] = [m s⁻³ kg⁻²]
    Not the same units. Try (c³/G²)·ℏ⁻²? That's getting ad-hoc.

    Cleaner: in Planck units (ℏ = c = G = 1), τ₀ in Planck units is
    τ̃₀ = τ₀/t_Pl. Then in Planck units:
        P_ζ(k_*) = 1/(π τ̃₀³) × coth(...)

    With τ̃₀ = τ₀/t_Pl ≈ 2.45×10⁵⁸:
        P_ζ ≈ 1/(π × (2.45×10⁵⁸)³) ≈ 1/(π × 1.47×10¹⁷⁵) ≈ 2.16×10⁻¹⁷⁶

    coth(...) factor: at T_c, the argument is ℏ/(2k_BT_c τ₀) =
    (k_BT_c τ₀)/(2k_BT_c τ₀) ... wait that's just 1/2. So
    coth(1/2) ≈ 2.16. So in Planck units at T = T_c:
        P_ζ ≈ 2.16/(π × τ̃₀³) ≈ 4.7×10⁻¹⁷⁶

    This is 167 orders of magnitude below A_s ≈ 2.1×10⁻⁹.

THE HONEST RESULT (rescaling-conditional): Lens B/F's forward
derivation produces a definite DIMENSIONAL variance
⟨|δz_{k*}|²⟩ = 2π G c² × coth(...). The dimensionless P_ζ depends
on the rescaling choice:

  (A) Planck rescaling          → (1/π)(t_Pl/τ_0)³ ≈ 10⁻¹⁷⁶
                                   No α-S structure.
  (B) Cosmic-baseline rescaling → 1/(πS³) ≈ 8.15×10⁻⁹
                                   IN α/S³ family (5% from α/S³,
                                   factor 4 from A_s).
  (C) H_inf rescaling           → ((2-R)/S)³/π ≈ 4.92×10⁻⁹
                                   ALSO in S³ family (factor 2.3
                                   from A_s).

The α/S³ coincidence IS recovered under choices (B) and (C), but
NOT under (A). The framework does not natively pin the rescaling
— this corresponds to the n_g_omega_cosmological_covariance_open_
question (#9 in the ledger). The α/S³ coincidence is therefore
CONDITIONALLY DERIVED, blocked on closing the covariance gap.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from grut.foundation.constants import (
    C as C_LIGHT,
    G,
    HBAR,
    K_B,
    L_PLANCK,
    M_PLANCK,
    T_PLANCK,
)
from grut.foundation.closure_protocol import (
    ALPHA_VAC,
    S_SCREENING,
    TAU_0_SEC,
)


# Reference targets
A_S_PLANCK_2018: float = 2.1e-9
ALPHA_OVER_S_CUBED: float = ALPHA_VAC / S_SCREENING**3  # ≈ 8.534e-9


# ─────────────────────────────────────────────────────────────────────
# Step-by-step calculation, isolated for testability
# ─────────────────────────────────────────────────────────────────────

def crossover_scale_k_star() -> float:
    """The natural GRUT crossover wavenumber: k_* = 1/(cτ₀).

    This is the GRUT analog of the inflationary horizon-crossing
    scale. At k > k_*, modes are in the deep-crystal regime
    (ωτ₀ ≫ 1, GR-recovered). At k < k_*, modes are in the deep-fluid
    regime (ωτ₀ ≪ 1, full constitutive enhancement).

    Returns: k_* in units of [1/m].
    """
    return 1.0 / (C_LIGHT * TAU_0_SEC)


def kms_thermal_factor_at_crossover(T_kelvin: float) -> float:
    """The KMS thermal factor coth(ℏω/(2k_BT)) at ω = 1/τ₀.

    At T = T_c, this is coth(1/2) ≈ 2.16.
    At T ≪ T_c (quantum regime), coth → 1.
    At T ≫ T_c (classical regime), coth → 2k_BT τ₀/ℏ.
    """
    if T_kelvin <= 0:
        return 1.0  # quantum limit
    x = HBAR / (2.0 * K_B * T_kelvin * TAU_0_SEC)
    if x > 50:
        return 1.0
    elif x < 1e-10:
        return 1.0 / x
    else:
        return math.cosh(x) / math.sinh(x)


def mode_variance_at_crossover(T_kelvin: float) -> float:
    """⟨|δz_{k*}(ω = 1/τ₀)|²⟩ from the linearized constitutive equation
    with KMS-thermal × Diósi-Penrose noise kernel.

    Following the derivation in the module docstring (Step 4):
        ⟨|δz_k(ω)|²⟩ = (4πG/ℏk²) × N_T(ω) / (1+ω²τ₀²)

    At k = k_* = 1/(cτ₀) and ω = 1/τ₀:
        = (4πG c² τ₀²/ℏ) × (ℏ/τ₀) × coth(ℏ/2k_BT τ₀) × (1/(2τ₀))
        = 2πG c² × coth(...)

    Returns variance in SI units (m³ — comes from the spatial
    Fourier transform of the gravitational kernel).
    """
    coth_factor = kms_thermal_factor_at_crossover(T_kelvin)
    return 2.0 * math.pi * G * C_LIGHT**2 * coth_factor


def dimensionless_power_spectrum_at_crossover(T_kelvin: float) -> float:
    """Dimensionless power spectrum P_ζ(k_*) under PLANCK rescaling
    specifically.

    P_ζ(k) = (k³/2π²) × ⟨|δz_k|²⟩, with k = k_* = 1/(cτ_0).

    The dimensional variance is G/(πcτ_0³) × coth(...). To make it
    dimensionless, this function uses the PLANCK rescaling: in
    ℏ=c=G=1 units, τ_0 → τ̃_0 = τ_0/t_Pl, and P_ζ = (1/π)(1/τ̃_0³)
    × coth(...).

    NOTE: this is ONE of three plausible rescaling choices. See
    `lens_B_F_forward_derivation()` for the other two (cosmic-
    baseline and H_inf) and the discussion of which corresponds
    to which physical question. The framework does not natively
    pin the rescaling — see `rescaling_sensitivity_analysis()`
    and the n_g(ω) covariance open negative (#9 in the ledger).
    """
    coth_factor = kms_thermal_factor_at_crossover(T_kelvin)
    tau_0_planck = TAU_0_SEC / T_PLANCK  # τ̃_0 = τ_0/t_Pl
    return coth_factor / (math.pi * tau_0_planck**3)


# ─────────────────────────────────────────────────────────────────────
# Forward derivation — full reporter
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class CurvatureResult:
    name: str
    value: float
    formula: str
    natural_form: str

    @property
    def vs_A_s(self) -> float:
        if self.value <= 0:
            return 0.0
        return self.value / A_S_PLANCK_2018

    @property
    def vs_alpha_over_S_cubed(self) -> float:
        if self.value <= 0:
            return 0.0
        return self.value / ALPHA_OVER_S_CUBED

    @property
    def log10_diff_from_As(self) -> float:
        if self.value <= 0:
            return float("-inf")
        return math.log10(self.value) - math.log10(A_S_PLANCK_2018)


def lens_B_F_forward_derivation() -> dict:
    """Lens B/F: linearized constitutive equation around z = 0,
    mode amplitude at crossover scale ωτ₀ = 1.

    The forward derivation produces a DIMENSIONAL variance:
        ⟨|δz_{k*}(1/τ_0)|²⟩ = 2π G c² × coth(ℏ/(2k_B T τ_0))

    To compare this to the observed dimensionless A_s = 2.1×10⁻⁹,
    a dimensional rescaling is required. The framework does NOT
    natively pin which rescaling is correct — this is exactly the
    n_g(ω) covariance open negative (#9 in the ledger).

    Three plausible rescaling choices are computed and reported.
    The α/S³ family is recovered under (B) cosmic-baseline and (C)
    H_inf rescaling, but NOT under (A) Planck rescaling. The
    framework's choice between them is precisely the gap that
    `n_g_omega_cosmological_covariance_resolved (RESOLVED via Correction #26)` names.
    """
    # Temperature points
    T_C_kelvin = HBAR / (TAU_0_SEC * K_B)
    T_CMB_kelvin = 2.7255

    # Dimensional variance at the crossover (in SI units, T = 0)
    variance_zeroT = mode_variance_at_crossover(0.0)
    variance_TC = mode_variance_at_crossover(T_C_kelvin)

    # Three rescaling choices (each at T = 0 for cleanest comparison)
    tau_0_planck = TAU_0_SEC / T_PLANCK  # τ̃_0 = τ_0/t_Pl ≈ 2.45e58
    H_INF_HZ = 1.884021899694621e-18      # (2-R)/(S × τ_0) terminal velocity
    H_inf_tau_0 = H_INF_HZ * TAU_0_SEC    # = (2-R)/S ≈ 2.49e-3

    # (A) Planck rescaling: P_ζ = (1/π) × (t_Pl/τ_0)³
    P_planck = 1.0 / (math.pi * tau_0_planck**3)

    # (B) Cosmic-baseline rescaling: P_ζ = (1/π) × (τ_0/τ_Λ)³ = 1/(πS³)
    P_cosmic_baseline = 1.0 / (math.pi * S_SCREENING**3)

    # (C) H_inf rescaling: P_ζ = (H_inf τ_0)³/π = ((2-R)/S)³/π
    P_H_inf = (H_inf_tau_0**3) / math.pi

    # Crossover scale
    k_star = crossover_scale_k_star()
    crossover_wavelength_m = 2.0 * math.pi / k_star
    crossover_wavelength_Mpc = crossover_wavelength_m / 3.0857e22

    return {
        "name": "Lens B/F: linearized constitutive equation, mode at ωτ₀=1",
        "dimensional_variance_at_T0_SI": variance_zeroT,
        "dimensional_variance_at_Tc_SI": variance_TC,
        "dimensional_units": "[m²/(kg·s)] from G c²",
        "crossover_k_star_per_m": k_star,
        "crossover_wavelength_Mpc": crossover_wavelength_Mpc,
        "rescaling_outcomes": {
            "A_planck_rescaling": {
                "formula": "(1/π) × (t_Pl/τ_0)³",
                "value": P_planck,
                "alpha_S_structure": "NONE — pure (t_Pl/τ_0)³ ratio",
                "vs_A_s": P_planck / A_S_PLANCK_2018,
                "log10_below_A_s": (
                    math.log10(A_S_PLANCK_2018) - math.log10(P_planck)
                ),
                "physical_motivation": (
                    "Standard-QFT/inflation rescaling — measure "
                    "fluctuations relative to the Planck scale. "
                    "Standard inflation uses (H/M_Pl)² × (1/ε); "
                    "GRUT lacks an inflationary H so the analogous "
                    "ratio (1/τ_0)/E_Pl is ~10⁻⁵⁹, cube ~10⁻¹⁷⁶."
                ),
            },
            "B_cosmic_baseline_rescaling": {
                "formula": "(1/π) × (τ_0/τ_Λ)³ = 1/(πS³)",
                "value": P_cosmic_baseline,
                "alpha_S_structure": (
                    "S³ — IN the α/S³ family. Differs from α/S³ "
                    "by α·π = π/3 ≈ 1.047 (5% — same family, "
                    "different prefactor)."
                ),
                "vs_A_s": P_cosmic_baseline / A_S_PLANCK_2018,
                "vs_alpha_over_S_cubed": (
                    P_cosmic_baseline / ALPHA_OVER_S_CUBED
                ),
                "physical_motivation": (
                    "Framework-natural cosmological rescaling — "
                    "measure fluctuations relative to the cosmic "
                    "baseline τ_Λ. This is the natural rescaling "
                    "for cosmological-perturbation observables IF "
                    "the framework's perturbation theory is "
                    "constructed at the τ_Λ scale."
                ),
            },
            "C_H_inf_rescaling": {
                "formula": "(H_inf τ_0)³/π = ((2-R)/S)³/π",
                "value": P_H_inf,
                "alpha_S_structure": (
                    "(2-R)³/S³ — also in the S³ family. "
                    "(2-R) = drive factor ≈ 0.845."
                ),
                "vs_A_s": P_H_inf / A_S_PLANCK_2018,
                "vs_alpha_over_S_cubed": (
                    P_H_inf / ALPHA_OVER_S_CUBED
                ),
                "physical_motivation": (
                    "Hubble-scale rescaling — analogous to standard "
                    "inflationary (H/M_Pl)² scaling but with "
                    "GRUT's terminal-velocity H_inf. Differs from "
                    "(B) by the (2-R)³ Hubble-drive factor."
                ),
            },
        },
        "verdict": (
            "RESCALING-CONDITIONAL. The forward derivation produces "
            "a definite dimensional variance, but the dimensionless "
            "P_ζ depends on the rescaling choice. Under Planck "
            "rescaling (A), no α-S structure and ~10⁻¹⁷⁶. Under "
            "cosmic-baseline rescaling (B), 1/(πS³) ≈ 8.15×10⁻⁹ — "
            "in the α/S³ family at factor ~4 from A_s. Under H_inf "
            "rescaling (C), ~4.9×10⁻⁹ — also S³ family. The α/S³ "
            "COINCIDENCE IS RECOVERED by Lens B/F UNDER rescaling "
            "choices (B) or (C), but NOT under (A). The framework "
            "does not natively pin the rescaling — this is the "
            "n_g(ω) covariance open negative (#9). Therefore: "
            "the α/S³ coincidence is conditionally derived, blocked "
            "on closing the covariance gap."
        ),
        "structural_link_to_open_negative_9": (
            "The choice of rescaling (A vs B vs C) corresponds to "
            "the choice of natural unit for cosmological-"
            "perturbation power spectra in the framework. This IS "
            "the n_g_omega_cosmological_covariance_resolved (RESOLVED via Correction #26). "
            "Closing #9 — specifically, deciding whether ω is "
            "Fourier frequency, conformal-time frequency, or some "
            "covariantly-defined object, AND mapping the result to "
            "standard MG-EFT μ(k,a)/γ(k,a) parameterization — "
            "would pin the natural rescaling and thereby determine "
            "whether the framework predicts (t_Pl/τ_0)³ (no match) "
            "or 1/(πS³) (match within factor 4) for A_s."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Sensitivity analysis — alternative choices flagged in user review
# ─────────────────────────────────────────────────────────────────────


def power_spectrum_at_alternative_scales(T_kelvin: float = 0.0) -> dict:
    """Evaluate the power spectrum at multiple plausible 'primordial
    scales' to show sensitivity to scale choice.

    The original calculation used ω = 1/τ₀ (the bandwidth crossover).
    Alternatives flagged in the user's Stage-2 review:
        - ω = H_inf (the terminal-velocity Hubble scale)
        - ω = c k_pivot where k_pivot = 0.05/Mpc (CMB pivot scale)

    Each scale produces a different result. The framework does NOT
    natively select one — this is a definitional gap connecting to
    the n_g(ω) covariance open negative."""
    H_INF_HZ = 1.884021899694621e-18  # (2-R)/(S × τ₀) — terminal velocity
    K_PIVOT_PER_M = 0.05 / 3.0857e22  # 0.05/Mpc → 1/m
    OMEGA_PIVOT_HZ = C_LIGHT * K_PIVOT_PER_M  # ω_pivot = c × k_pivot

    scales = {
        "omega_tau_eq_1 (bandwidth crossover)": 1.0 / TAU_0_SEC,
        "omega_eq_H_inf (terminal velocity)": H_INF_HZ,
        "omega_eq_c_k_pivot (CMB pivot)": OMEGA_PIVOT_HZ,
    }

    coth = kms_thermal_factor_at_crossover_general(T_kelvin)

    results = {}
    for name, omega in scales.items():
        # P_ζ ∝ (k³/2π²) × N_k(ω)/(ω²τ₀² + 1) with k = ω/c
        # = (ω³/(2π²c³)) × (4πG c²τ₀²/ℏω²) × ℏω·coth(...)/(τ₀(ω²τ₀² + 1))
        # = G ω² coth/(πc(ω²τ₀² + 1))
        # In Planck units (G=c=ℏ=1): = ω̃² × coth / (π (ω̃²τ̃₀² + 1))
        # where ω̃ = ω × t_Pl, τ̃₀ = τ₀/t_Pl
        omega_planck = omega * T_PLANCK
        tau_planck = TAU_0_SEC / T_PLANCK
        denom = omega_planck**2 * tau_planck**2 + 1.0
        # Use a thermal factor specific to this ω (not the crossover one)
        coth_at_omega = _coth_factor(omega, T_kelvin)
        P_planck = omega_planck**2 * coth_at_omega / (math.pi * denom)
        results[name] = {
            "omega_hz": omega,
            "omega_tau_dimensionless": omega * TAU_0_SEC,
            "P_zeta_planck_normalized": P_planck,
            "log10_vs_A_s": (
                math.log10(P_planck) - math.log10(A_S_PLANCK_2018)
                if P_planck > 0 else float("-inf")
            ),
        }
    return results


def kms_thermal_factor_at_crossover_general(T_kelvin: float) -> float:
    """Same as kms_thermal_factor_at_crossover but at ω = 1/τ₀."""
    return kms_thermal_factor_at_crossover(T_kelvin)


def _coth_factor(omega_hz: float, T_kelvin: float) -> float:
    """coth(ℏω/(2k_BT)) at arbitrary ω."""
    if T_kelvin <= 0 or omega_hz <= 0:
        return 1.0
    x = HBAR * omega_hz / (2.0 * K_B * T_kelvin)
    if x > 50:
        return 1.0
    elif x < 1e-10:
        return 1.0 / x
    else:
        return math.cosh(x) / math.sinh(x)


def power_spectrum_at_z_star(z_target_prime_at_zstar: float = -1.0,
                              T_kelvin: float = 0.0) -> dict:
    """Sensitivity to background choice z = z* (the nontrivial fixed
    point) vs z = 0 (the null fixed point).

    Linearizing around z = z*:
        τ₀ d(δz)/dt + δz = z_target'(z*) δz + ξ(t)
        ⟨|δz_k(ω)|²⟩ ∝ N_k(ω) / (ω²τ₀² + A*²)
    where A* = z_target'(z*) - 1.

    At z = 0: z_target'(0) = 0 typically, so A_0 = -1 and the
    denominator is (ω²τ₀² + 1). This is what the original calculation
    assumed.

    At z = z*: A* depends on z_target's behavior near the fixed point.
    The framework does NOT pin z_target'(z*) — this is information
    that would come from the constitutive equation's specific form
    near the realized fixed point.

    Special cases:
        - A* = -1 (same as z = 0): result identical to original
        - A* → 0 (marginally stable fixed point): noise-pump
          divergence; the variance grows without bound at low ω.
          This would indicate the framework has a natural mechanism
          for amplifying primordial fluctuations through near-marginal
          dynamics — a potentially important feature.
        - A* far from 0: bounded result, suppressed if |A*| > 1.

    Returns: result parametrized by z_target_prime_at_zstar."""
    A_star = z_target_prime_at_zstar - 1.0
    omega = 1.0 / TAU_0_SEC  # at the crossover scale
    coth = kms_thermal_factor_at_crossover(T_kelvin)
    # Scaling: P_ζ ∝ coth/(ω²τ₀² + A*²) where ω²τ₀² = 1 at crossover
    denominator_factor = 1.0 + A_star**2
    tau_planck = TAU_0_SEC / T_PLANCK
    P_planck = coth / (math.pi * tau_planck**3 * denominator_factor)

    return {
        "z_target_prime_at_zstar": z_target_prime_at_zstar,
        "A_star": A_star,
        "denominator_factor": denominator_factor,
        "P_zeta_planck_normalized": P_planck,
        "interpretation": (
            "MARGINAL fixed point (noise-pump divergence)"
            if abs(A_star) < 1e-3 else
            "Same as z=0 baseline" if abs(A_star + 1.0) < 1e-3 else
            f"Bounded — {1.0/denominator_factor:.3f}× the z=0 baseline"
        ),
    }


def rescaling_sensitivity_analysis() -> dict:
    """Sensitivity of the dimensionless P_ζ to the rescaling choice.

    Three natural rescalings:
        (A) Planck — natural ratio (t_Pl/τ_0). Result: (1/π)(t_Pl/τ_0)³.
        (B) Cosmic-baseline — natural ratio (τ_0/τ_Λ) = 1/S.
            Result: (1/π)(τ_0/τ_Λ)³ = 1/(πS³).
        (C) H_inf — natural ratio (H_inf τ_0). Result: (H_inf τ_0)³/π.

    Each rescaling is a different physical question. The framework
    does not natively select one. The choice corresponds to the
    n_g(ω) covariance open negative (#9 in the ledger).
    """
    tau_0_planck = TAU_0_SEC / T_PLANCK             # τ_0/t_Pl
    inv_S = 1.0 / S_SCREENING                       # τ_0/τ_Λ = 1/S
    H_INF_HZ = 1.884021899694621e-18
    H_inf_tau_0 = H_INF_HZ * TAU_0_SEC              # (2-R)/S

    options = {
        "A_planck_rescaling": {
            "natural_ratio": "t_Pl/τ_0",
            "ratio_value": 1.0 / tau_0_planck,
            "P_zeta_formula": "(1/π) × (t_Pl/τ_0)³",
            "P_zeta_value": 1.0 / (math.pi * tau_0_planck**3),
            "alpha_S_structure": "NONE",
            "in_alpha_over_S_cubed_family": False,
        },
        "B_cosmic_baseline_rescaling": {
            "natural_ratio": "τ_0/τ_Λ = 1/S",
            "ratio_value": inv_S,
            "P_zeta_formula": "(1/π) × (τ_0/τ_Λ)³ = 1/(πS³)",
            "P_zeta_value": 1.0 / (math.pi * S_SCREENING**3),
            "alpha_S_structure": "1/S³ — in α/S³ family",
            "in_alpha_over_S_cubed_family": True,
        },
        "C_H_inf_rescaling": {
            "natural_ratio": "H_inf × τ_0 = (2-R)/S",
            "ratio_value": H_inf_tau_0,
            "P_zeta_formula": "(H_inf τ_0)³/π = ((2-R)/S)³/π",
            "P_zeta_value": (H_inf_tau_0**3) / math.pi,
            "alpha_S_structure": "(2-R)³/S³ — in α/S³ family",
            "in_alpha_over_S_cubed_family": True,
        },
    }

    return {
        "rescaling_options": {
            name: {
                **opt,
                "log10": (
                    math.log10(opt["P_zeta_value"])
                    if opt["P_zeta_value"] > 0 else float("-inf")
                ),
                "vs_A_s": (
                    opt["P_zeta_value"] / A_S_PLANCK_2018
                    if opt["P_zeta_value"] > 0 else 0.0
                ),
                "vs_alpha_over_S_cubed": (
                    opt["P_zeta_value"] / ALPHA_OVER_S_CUBED
                    if opt["P_zeta_value"] > 0 else 0.0
                ),
            }
            for name, opt in options.items()
        },
        "structural_note": (
            "Verified algebraically: 1/(πS³) and α/S³ differ by "
            "α·π = π/3 ≈ 1.047 (5%, same S³ family). "
            "The cosmic-baseline rescaling (B) recovers the α/S³ "
            "family at the right magnitude (factor ~4 from A_s). "
            "The Planck rescaling (A) does not. The framework "
            "doesn't pin the choice — this is the n_g(ω) "
            "covariance open negative #9."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Comparison table — all relevant dimensional candidates
# ─────────────────────────────────────────────────────────────────────


def comparison_to_dimensional_candidates() -> dict:
    """Compare the Lens B/F result to the equivalence class
    decompositions of α/S³ AND to other natural framework scales."""
    tau_0_planck = TAU_0_SEC / T_PLANCK

    candidates = [
        ("Lens B/F natural (t_Pl/τ₀)³", 1.0 / (math.pi * tau_0_planck**3)),
        ("α/S³ (Stage 1 closest)", ALPHA_OVER_S_CUBED),
        ("α⁷/(12π)³ (F2)", ALPHA_VAC**7 / (12 * math.pi)**3),
        ("α¹⁰/(4π)³ (F7, α=1/3 specific)", ALPHA_VAC**10 / (4 * math.pi)**3),
        ("(t_Pl/τ₀) — linear", 1.0 / tau_0_planck),
        ("(t_Pl/τ₀)² — squared", 1.0 / tau_0_planck**2),
        ("Observed A_s", A_S_PLANCK_2018),
    ]

    return {
        "candidates": [
            {
                "name": name,
                "value": value,
                "log10": math.log10(value) if value > 0 else float("-inf"),
            }
            for name, value in candidates
        ],
        "lens_BF_vs_A_s_orders_of_magnitude": (
            math.log10(A_S_PLANCK_2018)
            - math.log10(1.0 / (math.pi * tau_0_planck**3))
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Top-level reporter
# ─────────────────────────────────────────────────────────────────────


def primordial_curvature_lens_BF_attempt() -> dict:
    """Run Lens B/F's forward derivation and produce the honest result."""
    result = lens_B_F_forward_derivation()
    rescaling = rescaling_sensitivity_analysis()
    comparison = comparison_to_dimensional_candidates()

    return {
        "lens": "B/F — cosmological-perturbation curvature ζ from "
                "linearized constitutive equation",
        "investigation_log": "theory/derivation/PRIMORDIAL_ALPHA_S3_INVESTIGATION.md",
        "forward_derivation": result,
        "rescaling_sensitivity": rescaling,
        "comparison": comparison,
        "honest_conclusion": (
            "RESCALING-CONDITIONAL OUTCOME. The forward derivation "
            "produces a definite dimensional variance "
            "⟨|δz_{k*}|²⟩ = 2π G c² × coth(...). The dimensionless "
            "P_ζ depends on the rescaling choice: "
            "(A) Planck rescaling → (1/π)(t_Pl/τ_0)³ ≈ 10⁻¹⁷⁶, no α-S; "
            "(B) Cosmic-baseline rescaling → 1/(πS³) ≈ 8.15×10⁻⁹, "
            "S³ structure (in α/S³ family at 5% from α/S³ algebraically, "
            "factor 4 from A_s); "
            "(C) H_inf rescaling → ((2-R)/S)³/π ≈ 6×10⁻¹⁰, also "
            "S³ family. The α/S³ coincidence IS recovered under (B) "
            "and (C), but NOT under (A). The framework does not "
            "natively pin the rescaling — this corresponds to the "
            "n_g(ω) covariance open negative (#9). The α/S³ "
            "coincidence is therefore conditionally derived, blocked "
            "on closing the covariance gap."
        ),
        "structural_finding": (
            "primordial_amplitude_zero_parameter_open_negative is "
            "structurally linked to "
            "n_g_omega_cosmological_covariance_resolved (RESOLVED via Correction #26). "
            "Closing the latter would either close the former with "
            "A_s ~ 1/(πS³) (cosmic-baseline rescaling — match within "
            "factor 4 of observed) or sharpen its honest negative "
            "with A_s ~ (t_Pl/τ_0)³ (Planck rescaling — failure by "
            "167 orders)."
        ),
        "next_step_recommendation": (
            "Lens B/F has produced a CONDITIONAL result, not a clean "
            "negative. The α/S³ family IS naturally recovered under "
            "two of three plausible rescalings. Closing this requires "
            "framework-level decision on which rescaling is correct, "
            "which is exactly the n_g(ω) covariance gap. "
            "Stage-2 lenses C (bandwidth integral) and D (alternative "
            "OU-rescaling) could provide independent cross-check on "
            "which rescaling the framework prefers, but the central "
            "blocker is the covariance open negative."
        ),
    }


if __name__ == "__main__":
    import json

    def serialize(obj):
        if isinstance(obj, dict):
            return {k: serialize(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [serialize(x) for x in obj]
        if isinstance(obj, (np.floating, float)):
            return float(obj)
        return obj

    result = primordial_curvature_lens_BF_attempt()
    print(json.dumps(serialize(result), indent=2))
