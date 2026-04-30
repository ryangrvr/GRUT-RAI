"""GRUT — Genesis noise kernel: spectral analysis at z = 0.

Investigation: GENESIS_NOISE_KERNEL_HEAT_INVESTIGATION.md.
Stage 2: forward derivation of the spectrum produced by the
linearized constitutive equation around z = 0 with the framework's
KMS noise kernel. Tests whether the framework's noise kernel
produces "thermal-spectrum radiation" (one piece of an external
research hypothesis).

SCOPE BOUNDARIES (load-bearing):

This module computes the framework's existing infrastructure
applied to ONE specific question (the noise-kernel spectrum at
z = 0). It does NOT:
  - claim the framework "produces CMB temperature"
  - resolve t_c_provenance_inconsistency_open_negative (#15)
  - resolve n_g_omega_cosmological_covariance_open_question (#9)
  - propose Chapter 13 revisions
  - adopt any narrative-level reading

KMS noise structurally requires T as input. The "T = 0 quantum
vacuum" limit gives a definite Lorentzian-modulated linear spectrum
(NOT Planck/Bose-Einstein). "Temperature" extracted from this
spectrum is a CHARACTERISTIC SCALE, not a true thermal-equilibrium
temperature. Multiple definitions yield different values; the
framework hasn't pinned which is "the" thermal scale.

Pre-committed expectations (per investigation log):
  - Spectral peak at ω = 1/τ_0 → T_peak = ℏ/(τ_0 k_B) ≈ 5.78×10⁻²⁷ K
  - Planck UV cutoff → T ~ 10³² K
  - None matching CMB (2.725 K)
  - Spectrum shape is Lorentzian × ω, NOT Planck

The deliverable is the spectrum and the comparison table.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from grut.foundation.constants import (
    C as C_LIGHT,
    HBAR,
    K_B,
    T_PLANCK,
)
from grut.foundation.closure_protocol import TAU_0_SEC


# Reference scales
T_CMB_K: float = 2.725
T_PLANCK_K: float = math.sqrt(HBAR * C_LIGHT**5 / 6.6743e-11) / K_B  # ~1.42e32 K
OMEGA_PLANCK_HZ: float = 1.0 / T_PLANCK   # frequency cutoff at Planck time


# ─────────────────────────────────────────────────────────────────────
# Spectral density of the OU process under KMS noise
# ─────────────────────────────────────────────────────────────────────


def kms_noise_spectrum(omega_hz: float, T_kelvin: float = 0.0) -> float:
    """N_KMS(ω, T) = (2/τ_0) × ℏω × coth(ℏω/(2k_BT))

    At T = 0: coth → 1 (for ω > 0), N → 2ℏω/τ_0
    At T_classical (k_BT ≫ ℏω): coth → 2k_BT/(ℏω), N → 4k_BT/τ_0
    """
    if omega_hz <= 0:
        return 0.0
    if T_kelvin <= 0:
        return 2.0 * HBAR * omega_hz / TAU_0_SEC
    x = HBAR * omega_hz / (2.0 * K_B * T_kelvin)
    if x > 50:
        coth = 1.0       # quantum limit
    elif x < 1e-10:
        coth = 1.0 / x   # classical limit
    else:
        coth = math.cosh(x) / math.sinh(x)
    return (2.0 / TAU_0_SEC) * HBAR * omega_hz * coth


def spectral_density_h(omega_hz: float, T_kelvin: float = 0.0) -> float:
    """S_h(ω, T) = N_KMS(ω, T) / (1 + (ωτ_0)²)

    The OU process's spectral density: noise filtered by the
    response function |χ(ω)|² = 1/(1 + (ωτ_0)²).

    Units: same as N_KMS (energy/time, J/s in SI), since |χ|² is
    dimensionless.
    """
    N = kms_noise_spectrum(omega_hz, T_kelvin)
    return N / (1.0 + (omega_hz * TAU_0_SEC) ** 2)


# ─────────────────────────────────────────────────────────────────────
# Spectral peak — characteristic frequency at T = 0
# ─────────────────────────────────────────────────────────────────────


def spectral_peak_omega_T0() -> float:
    """At T = 0, S_h(ω) ∝ ω/(1+ω²τ_0²).

    dS/dω = 0 at ω satisfying:
        (1 + ω²τ_0²) - ω × 2ωτ_0² = 0
        1 = ω²τ_0²
        ω = 1/τ_0

    Returns: ω_peak = 1/τ_0 [Hz]"""
    return 1.0 / TAU_0_SEC


def temperature_from_spectral_peak() -> float:
    """T_peak = ℏω_peak/k_B = ℏ/(τ_0 k_B).

    For τ_0 = 41.9 Myr: T_peak ≈ 5.78×10⁻²⁷ K.

    NOTE: This is the SI-correct value of the "T_c"-like scale that
    appears in the t_c_provenance_inconsistency_open_negative audit.
    The audit identified that the framework's codebase computes T_c
    as 1/(τ_0 k_B) ≈ 54.7 MK (missing factor of ℏ), while the
    SI-correct value ℏ/(τ_0 k_B) is 5.78×10⁻²⁷ K. The same scale
    appears here as the Genesis spectral peak. The genesis
    investigation does NOT resolve the audit — both values are
    incompatible with CMB at order-of-magnitude levels."""
    return HBAR / (TAU_0_SEC * K_B)


# ─────────────────────────────────────────────────────────────────────
# Integrated variance — UV-cutoff-dependent
# ─────────────────────────────────────────────────────────────────────


def variance_h_integrated_T0(omega_uv_hz: float = OMEGA_PLANCK_HZ) -> float:
    """⟨h²⟩(T=0) = (1/π) ∫_0^{ω_uv} S_h(ω, T=0) dω

    Closed-form at T = 0:
        S_h = (2ℏ/τ_0) × ω/(1+ω²τ_0²)
        ∫_0^{ω_uv} ω/(1+ω²τ_0²) dω = ln(1 + ω_uv²τ_0²)/(2τ_0²)
        ⟨h²⟩ = (ℏ/(πτ_0³)) × ln(1 + ω_uv²τ_0²)

    For ω_uv = ω_Planck = 1/t_Pl: ω_uv τ_0 ≈ 2.45×10⁵⁸,
    so ln(1 + (ω_uv τ_0)²) ≈ 2 ln(ω_uv τ_0) ≈ 268.8.

    Units: ℏ/τ_0³ has units (J·s)/s³ = J/s² (J × frequency²).
    """
    omega_uv_tau = omega_uv_hz * TAU_0_SEC
    log_factor = math.log(1.0 + omega_uv_tau**2)
    return (HBAR / (math.pi * TAU_0_SEC**3)) * log_factor


def temperature_from_equipartition_T0(
    omega_uv_hz: float = OMEGA_PLANCK_HZ,
) -> float:
    """Equipartition-style temperature from ⟨h²⟩ at T = 0.

    For a harmonic-oscillator-like system with effective spring
    constant k_eff = 1/τ_0² (from the OU restoring term ḣ ∝ -h/τ_0²),
    equipartition gives:
        (1/2) k_eff ⟨h²⟩ = (1/2) k_B T_eq
    so:
        T_eq = ⟨h²⟩ × k_eff / k_B = ⟨h²⟩ / (k_B × τ_0²)

    With ⟨h²⟩ = (ℏ/πτ_0³) × ln(1+(ω_uv τ_0)²):
        T_eq = ℏ × ln(...) / (π k_B τ_0⁵) — has wrong units!

    Wait — ⟨h²⟩ has units J/s² and k_eff = 1/τ_0² has units 1/s².
    So k_eff × ⟨h²⟩ has units J/s⁴ — not energy.

    The dimensional analysis confirms: the framework's noise kernel
    is set up for a quantity h with energy units, not dimensionless.
    Equipartition naively doesn't apply without specifying what h
    represents physically.

    Returning the dimensionless ratio ℏω_uv × ln(...)/(τ_0² × k_B²)
    as a 'characteristic temperature scale' for cross-comparison —
    explicitly flagged as not a rigorous equipartition T."""
    var = variance_h_integrated_T0(omega_uv_hz)
    # Heuristic conversion: treat √⟨h²⟩ × ω_typ as energy scale,
    # divide by k_B for temperature
    omega_typ = 1.0 / TAU_0_SEC  # natural framework frequency
    energy_scale = math.sqrt(var) * omega_typ  # heuristic only
    return energy_scale / K_B


def temperature_from_uv_cutoff(omega_uv_hz: float = OMEGA_PLANCK_HZ) -> float:
    """T = ℏω_uv / k_B. For Planck cutoff, this is T_Planck."""
    return HBAR * omega_uv_hz / K_B


# ─────────────────────────────────────────────────────────────────────
# Bose-Einstein / Planck spectrum for shape comparison
# ─────────────────────────────────────────────────────────────────────


def planck_spectral_shape(omega_hz: float, T_kelvin: float) -> float:
    """Bose-Einstein occupation × ω density for a true Planck spectrum:
        n(ω, T) × ω³/c³ ∝ ω³/(exp(ℏω/k_BT) - 1)

    This is the energy density per unit frequency for thermal
    radiation at temperature T. Returned as a comparison reference
    — the framework's S_h(ω) does NOT match this shape at any T.
    """
    if omega_hz <= 0 or T_kelvin <= 0:
        return 0.0
    x = HBAR * omega_hz / (K_B * T_kelvin)
    if x > 700:
        return 0.0
    elif x < 1e-10:
        denom = x  # exp(x) - 1 ≈ x for small x
    else:
        denom = math.exp(x) - 1.0
    return (omega_hz**3 / C_LIGHT**3) / denom


def shape_difference_from_planck() -> dict:
    """Document that the framework's S_h(ω, T=0) is NOT Planck.

    At T = 0:
      S_h(ω, T=0) ∝ ω/(1+ω²τ_0²)  — Lorentzian × ω, peak at 1/τ_0
      Planck at any T ≠ 0 ∝ ω³/(exp(ℏω/k_BT) - 1)  — exponential cutoff

    These are functionally different. No temperature T makes them
    coincide. The framework's S_h is a dissipative-system spectrum,
    not a thermal-radiation spectrum.
    """
    return {
        "framework_S_h_T0_form": "ω/(1+(ωτ_0)²) — Lorentzian × linear",
        "planck_form_any_T": "ω³/(exp(ℏω/k_BT) - 1) — Bose-Einstein",
        "qualitative_difference": (
            "Framework spectrum at T = 0 is a damped-oscillator "
            "response, peaking at ω = 1/τ_0 with linear rise and "
            "1/ω falloff. Planck spectrum has cubic rise (Rayleigh-"
            "Jeans low-ω) and exponential cutoff at ω ~ k_BT/ℏ. "
            "These shapes are functionally different at any T; no "
            "thermal interpretation matches the framework's noise-"
            "kernel-driven spectrum at T = 0."
        ),
        "structural_implication": (
            "The framework's noise kernel does NOT produce thermal-"
            "spectrum radiation in the Planck/Bose-Einstein sense. "
            "Genesis Hypothesis Claim 1's 'thermal radiation' "
            "framing is structurally wrong at the spectrum-shape "
            "level. A characteristic temperature can be EXTRACTED "
            "from the spectrum (peak frequency, UV cutoff, etc.) "
            "but is not a true thermal-equilibrium temperature."
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Master report
# ─────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class CharacteristicTemperature:
    name: str
    formula: str
    value_K: float

    @property
    def vs_CMB(self) -> float:
        return self.value_K / T_CMB_K

    @property
    def log10_vs_CMB(self) -> float:
        if self.value_K <= 0:
            return float("-inf")
        return math.log10(self.value_K) - math.log10(T_CMB_K)


def genesis_noise_kernel_attempt() -> dict:
    """Stage 2 forward derivation: spectrum + characteristic T's."""

    # Spectral peak
    omega_peak = spectral_peak_omega_T0()
    T_peak = temperature_from_spectral_peak()

    # UV cutoff (Planck scale)
    T_uv_planck = temperature_from_uv_cutoff(OMEGA_PLANCK_HZ)

    # Equipartition heuristic (UV-cutoff dependent)
    T_eq_planck = temperature_from_equipartition_T0(OMEGA_PLANCK_HZ)

    # Variance under different cutoffs
    var_planck = variance_h_integrated_T0(OMEGA_PLANCK_HZ)
    var_natural = variance_h_integrated_T0(10.0 / TAU_0_SEC)  # 10× peak freq

    # Spectrum shape comparison
    shape = shape_difference_from_planck()

    candidates = [
        CharacteristicTemperature(
            name="spectral_peak",
            formula="ℏω_peak/k_B = ℏ/(τ_0 k_B)",
            value_K=T_peak,
        ),
        CharacteristicTemperature(
            name="planck_uv_cutoff",
            formula="ℏω_Planck/k_B = T_Planck",
            value_K=T_uv_planck,
        ),
        CharacteristicTemperature(
            name="equipartition_planck_cutoff",
            formula="heuristic ⟨h²⟩^(1/2) × ω_typ / k_B",
            value_K=T_eq_planck,
        ),
        CharacteristicTemperature(
            name="cmb_today",
            formula="observed reference",
            value_K=T_CMB_K,
        ),
    ]

    return {
        "scope_notice": (
            "Stage 2 of GENESIS_NOISE_KERNEL_HEAT_INVESTIGATION. ONE "
            "specific calculation: framework's spectral response under "
            "OU process around z = 0 with KMS noise. Does NOT claim "
            "the framework produces CMB temperature. Does NOT resolve "
            "open negatives #9 or #15. Does NOT propose Ch 13 "
            "revisions."
        ),
        "spectrum_at_T0_formula": (
            "S_h(ω, T=0) = (2ℏ/τ_0) × ω/(1+(ωτ_0)²) — "
            "Lorentzian × linear, NOT Planck/Bose-Einstein."
        ),
        "spectral_peak": {
            "omega_hz": omega_peak,
            "T_K": T_peak,
            "physical_meaning": (
                "Frequency at which the noise-driven response is "
                "maximum. Reduces to 1/τ_0 because that's the "
                "dissipation rate of the OU process — the medium "
                "responds maximally to fluctuations at its own "
                "natural rate."
            ),
        },
        "characteristic_temperatures": [
            {
                "name": c.name,
                "formula": c.formula,
                "value_K": c.value_K,
                "vs_CMB_ratio": c.vs_CMB,
                "log10_vs_CMB": c.log10_vs_CMB,
            }
            for c in candidates
        ],
        "shape_comparison_to_planck": shape,
        "integrated_variance": {
            "planck_uv_cutoff": var_planck,
            "near_natural_cutoff": var_natural,
            "ratio": var_planck / var_natural if var_natural > 0 else float("inf"),
            "note": (
                "Variance is logarithmically UV-divergent. "
                "ln(1+(ω_uv τ_0)²) at Planck cutoff ≈ 268.8; near "
                "natural cutoff (10/τ_0) ≈ ln(101) ≈ 4.6. The "
                "log-divergence means the calculation cannot give a "
                "cutoff-independent variance, so equipartition T is "
                "cutoff-dependent. UV regulation is a choice the "
                "framework hasn't pinned."
            ),
        },
        "verdict": (
            "Genesis Claim 1 ('CTP noise kernel produces thermal-"
            "spectrum radiation at characteristic T') is structurally "
            "WRONG at the spectrum-shape level: the framework's "
            "S_h(ω, T=0) is Lorentzian × linear, not Planck/Bose-"
            "Einstein. A characteristic temperature CAN be extracted "
            "from the spectrum (spectral peak gives T = ℏ/(τ_0 k_B) "
            "≈ 5.78×10⁻²⁷ K; Planck UV cutoff gives T ~ T_Planck ≈ "
            "10³² K), but neither is a true thermal-equilibrium T. "
            "The spectral-peak value coincides numerically with the "
            "SI-correct T_c value in the #15 audit (which the "
            "codebase reports as 54.7 MK with a missing factor of ℏ); "
            "the same scale appears here as a different physical "
            "quantity (spectral peak vs claimed phase-boundary). "
            "The genesis investigation does NOT resolve the audit. "
            "Neither temperature scale matches CMB; the framework's "
            "noise kernel alone cannot derive observed CMB "
            "temperature, consistent with the user's pre-committed "
            "expectation."
        ),
        "research_tier_unanswered": (
            "Self-consistent equilibrium (limit (c) of Stage 1) — "
            "where the medium's dissipated energy thermalizes a "
            "radiation field with self-consistent T from energy "
            "balance — would require structural addition the "
            "framework lacks. This is the closure path Genesis "
            "Claim 1 would need to be derivable in the framework. "
            "Research-tier; not addressed here."
        ),
    }


if __name__ == "__main__":
    result = genesis_noise_kernel_attempt()
    print("=" * 78)
    print("Genesis noise kernel — spectrum at z = 0")
    print("=" * 78)
    print()
    print("Spectrum form (T = 0):")
    print(" ", result["spectrum_at_T0_formula"])
    print()
    print(f"Spectral peak: ω = {result['spectral_peak']['omega_hz']:.3e} Hz")
    print(f"               T = {result['spectral_peak']['T_K']:.3e} K")
    print()
    print("Characteristic temperature comparison:")
    print(f"  {'definition':<35} {'value (K)':>15} {'vs CMB':>15} {'log10 vs CMB':>15}")
    print("-" * 85)
    for c in result["characteristic_temperatures"]:
        print(f"  {c['name']:<35} {c['value_K']:>15.3e} {c['vs_CMB_ratio']:>15.3e} {c['log10_vs_CMB']:>15.2f}")
    print()
    print("Shape comparison to Planck:")
    print(f"  Framework T=0:  {result['shape_comparison_to_planck']['framework_S_h_T0_form']}")
    print(f"  Planck (any T): {result['shape_comparison_to_planck']['planck_form_any_T']}")
    print()
    print("Integrated variance:")
    iv = result["integrated_variance"]
    print(f"  Planck UV cutoff:       {iv['planck_uv_cutoff']:.3e}")
    print(f"  Near natural cutoff:    {iv['near_natural_cutoff']:.3e}")
    print(f"  Ratio (UV-divergence):  {iv['ratio']:.3e}")
    print()
    print("Verdict:")
    print(f"  {result['verdict']}")
