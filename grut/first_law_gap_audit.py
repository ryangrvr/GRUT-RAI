"""GRUT Appendix I — First-Law Gap Audit.

QUESTION BEING ANSWERED
-----------------------
The first-law ratio R = k_B·T_diss·(dS/dM)/c² = 2π√3/9 ≈ 1.209 ≠ 1.

Three candidate resolutions:
  (a) Revise the entropy proxy
  (b) Revise the temperature
  (c) Add a missing work / memory term

This module evaluates all three and delivers verdicts.

RESULT PREVIEW
--------------
  (a) Entropy revision: STRUCTURALLY_POSSIBLE — the required entropy
      S_correct = S_eq / R has the same M² scaling as S_eq but lacks
      a GRUT-native geometric motivation.

  (b) Temperature revision: VIABLE — T_1stlaw = T_diss/R = 9·T_Hawking
      is the unique temperature for which the first law holds exactly
      with S_eq. It is accessible without quantum-state input but requires
      importing T_Hawking, which is not GRUT-native.
      Alternatively: T_1stlaw can be expressed entirely in GRUT quantities as
      T_1stlaw = (3c²·ε_Q^(1/β_Q)) / (2·k_B·τ_Schwarz) where
      τ_Schwarz = r_s/c is the Schwarzschild light-crossing time.

  (c) Missing work term: CLOSED — the barrier potential at equilibrium is
      V_Q(R_eq) = −GM/r_s = −c²/2, which is independent of M.
      For any quasi-static change δM, dV_Q/dM = 0: the barrier does
      zero work. The memory sector is dissipative at equilibrium (V=0),
      so no memory work term exists either. Option (c) is eliminated.

DEEPER RESULT
-------------
The gap is structural. It is determined by a single dimensionless number:

  R = 4π√3 / (3Q)   where Q = β_Q/α_vac

Any revision must change either Q or the mass scaling of entropy.
No GRUT parameter currently bridges the two without external input.

WHAT THIS MODULE DOES NOT CLAIM:
  - Does NOT prove T_1stlaw is the correct temperature.
  - Does NOT prove the entropy proxy is wrong.
  - Does NOT resolve any Appendix C blocker.
  - Does NOT upgrade any prior classification.

LOCKED INHERITANCE:
  - Appendix D: thermodynamic_sector_partially_consistent UNCHANGED.
  - Appendix E: locally_consistent_globally_underdetermined UNCHANGED.
  - Appendix H: temperature_selectable_conditionally_not_uniquely UNCHANGED.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

# ================================================================
# Physical Constants (SI)
# ================================================================

G_SI = 6.674e-11
C_SI = 299_792_458.0
HBAR_SI = 1.054571817e-34
K_B = 1.380649e-23
L_PLANCK = math.sqrt(HBAR_SI * G_SI / C_SI ** 3)

# ================================================================
# Canonical GRUT Parameters (locked)
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
EPSILON_Q = ALPHA_VAC ** 2       # = 1/9
R_EQ_OVER_RS = EPSILON_Q ** (1.0 / BETA_Q)   # = 1/3
Q_CANONICAL = BETA_Q / ALPHA_VAC             # = 6.0

M_SUN_KG = 1.989e30
M_REF_KG = 30.0 * M_SUN_KG

# The gap factor (from Appendix H)
R_GAP = 4.0 * math.pi * math.sqrt(3.0) / (3.0 * Q_CANONICAL)  # ≈ 1.209

# ================================================================
# Forbidden classification strings
# ================================================================

_FORBIDDEN_CLASSIFICATIONS = {
    "gap_closed",
    "first_law_proven",
    "work_term_found",
    "entropy_derived",
    "temperature_proven",
    "appendix_c_resolved",
}


# ================================================================
# Data Structures
# ================================================================

@dataclass
class BarrierWorkAnalysis:
    """Analysis of the barrier work contribution at the GRUT endpoint."""
    # Barrier potential at R_eq
    V_Q_formula: str = (
        "V_Q(R_eq) = -GM * epsilon_Q * r_s^beta_Q / "
        "((1+beta_Q) * R_eq^(1+beta_Q))"
    )
    V_Q_simplified: str = "V_Q(R_eq) = -GM/r_s = -c²/2"
    V_Q_value_over_c_sq: float = -0.5   # = -c²/2, dimensionless ratio

    # Mass independence
    is_M_independent: bool = True
    proof: str = (
        "V_Q(R_eq) = -GM * (1/9) * r_s² / (3 * (r_s/3)³) "
        "= -GM * (r_s²/9) / (r_s³/9) = -GM/r_s = -c²/2. "
        "Since r_s = 2GM/c², -GM/r_s = -c²/2 independent of M."
    )

    # Work for δM
    delta_V_Q_over_delta_M: float = 0.0   # exactly 0
    barrier_work_contribution: str = "ZERO"

    # Memory sector work
    memory_work_at_equilibrium: str = (
        "At equilibrium V=0, the memory ODE is dM_drive/dt = 0 "
        "(M_drive = a_grav). No dissipative work is done at V=0. "
        "Memory work is zero at the endpoint."
    )
    memory_work_contribution: str = "ZERO"

    # Verdict
    verdict: str = "CLOSED"
    verdict_reason: str = (
        "Both the barrier potential and the memory sector contribute "
        "zero work at the GRUT equilibrium endpoint for quasi-static "
        "mass changes. Option (c) — missing work term — is eliminated."
    )


@dataclass
class EntropyRevisionAnalysis:
    """Analysis of what entropy revision would close the gap."""
    # Current entropy
    S_current_formula: str = "S_eq = pi * R_eq^2 / l_P^2"
    S_current_mass_scaling: str = "S_eq ∝ M^2"

    # Required entropy for T_dissipation to satisfy first law exactly
    S_required_formula: str = "S_correct = S_eq / R = S_eq * 9/(2*pi*sqrt(3))"
    S_required_over_S_current: float = 0.0   # = 1/R ≈ 0.827
    S_required_mass_scaling: str = "S_correct ∝ M^2"

    # Geometric interpretation
    effective_radius_formula: str = "S_correct = pi * R_eff^2 / l_P^2"
    R_eff_over_R_eq: float = 0.0   # = 1/sqrt(R) ≈ 0.909

    # Is there a GRUT-native reason?
    grut_native_motivation: bool = False
    grut_native_description: str = (
        "S_correct = S_eq/R ≈ 0.827 × S_eq corresponds to an effective "
        "radius R_eff ≈ 0.909 × R_eq. There is no GRUT-native geometric "
        "quantity that equals 0.909 × R_eq. The factor 1/√R = √(9/(2π√3)) "
        "does not simplify in terms of α_vac, β_Q, ε_Q, or Q."
    )

    # Alternative: entropy at the Schwarzschild radius
    S_horizon_formula: str = "S_horizon = pi * r_s^2 / l_P^2 = 9 * S_eq"
    T_from_S_horizon: str = "T_Hawking (too cold by factor 9)"

    # Mass scaling requirement
    mass_scaling_change_needed: bool = False
    mass_scaling_verdict: str = (
        "The required entropy S_correct has the SAME mass scaling (M^2) "
        "as S_eq — only the coefficient differs. No change in mass scaling "
        "is needed. The revision is purely a multiplicative factor 1/R."
    )

    verdict: str = "STRUCTURALLY_POSSIBLE_NO_GRUT_MOTIVATION"


@dataclass
class TemperatureRevisionAnalysis:
    """Analysis of what temperature revision would close the gap."""
    # T_1stlaw
    T_1stlaw_formula: str = "T_1stlaw = c^2 / (k_B * dS/dM) = 9 * T_Hawking"
    T_1stlaw_over_T_diss: float = 0.0   # = 1/R ≈ 0.827

    # Can T_1stlaw be expressed without importing T_Hawking?
    T_1stlaw_in_grut_terms: str = ""
    T_1stlaw_grut_native: bool = False

    # Relation to other temperature candidates
    T_1stlaw_vs_T_structural: str = ""
    T_1stlaw_vs_T_dissipation: str = ""

    # What changes in GRUT if T_1stlaw is the "correct" temperature?
    consequence_if_T_1stlaw_correct: str = (
        "If T_1stlaw is correct: (1) T_dissipation is wrong by factor R ≈ 1.21. "
        "(2) T_structural is wrong by factor R*Q ≈ 7.26. "
        "(3) The FDT noise floor becomes S(0) = 2k_B*T_1stlaw*tau_local "
        "= 2*(c²/(k_B*dS/dM))*(1/ω₀)*k_B/k_B = 2c²/(ω₀*dS_dM*c²)... "
        "i.e., S(0) = 2/(ω₀*(dS/dM)) — a specific mass-dependent prediction. "
        "(4) The Q-factor interpretation changes: Q would not equal "
        "β_Q/α_vac = 6 from a thermal perspective, only from the PDE perspective."
    )

    # Can we express T_1stlaw without T_Hawking?
    grut_expression: str = (
        "T_1stlaw = 9*ℏ*c³/(8π*G*M*k_B). This CAN be expressed in GRUT "
        "quantities: with r_s = 2GM/c², τ_Schwarz = r_s/c = 2GM/c³ "
        "(Schwarzschild light-crossing time), "
        "T_1stlaw = 9*ℏ/(4π*k_B*τ_Schwarz). "
        "This does not use T_Hawking directly, but τ_Schwarz = 2GM/c³ "
        "is the same parameter as in T_Hawking = ℏc³/(8πGMk_B) = ℏ/(4π*k_B*τ_Schwarz). "
        "T_1stlaw = 9*T_Hawking = 9*ℏ/(4π*k_B*τ_Schwarz). "
        "T_Hawking and T_1stlaw differ only by the factor 9 = (r_s/R_eq)² = 1/R_EQ_OVER_RS²."
    )

    verdict: str = "VIABLE_NO_NEW_GRUT_STRUCTURE"


@dataclass
class GapStructureAnalysis:
    """Analysis of the structural origin of the gap R = 4π√3/(3Q)."""
    R_gap: float = R_GAP
    R_gap_formula: str = "R = 4*pi*sqrt(3) / (3*Q) = 2*pi*sqrt(3)/9"
    R_gap_depends_on: List[str] = field(default_factory=lambda: [
        "Q = beta_Q / alpha_vac  (GRUT-locked)",
        "R_eq/r_s = epsilon_Q^(1/beta_Q) = 1/3  (GRUT-locked)",
        "The area law S ∝ R^2  (from the Bekenstein-Hawking area proxy)",
    ])
    R_gap_independent_of: List[str] = field(default_factory=lambda: [
        "Mass M",
        "Physical constants G, ℏ, c, k_B individually",
        "The specific Lorentzian damping form (only Q matters)",
    ])

    # Can R = 1 be achieved by modifying GRUT parameters?
    R_equals_one_requires: str = (
        "R = 1 would require Q = 4π√3/3 ≈ 7.26. "
        "With current β_Q = 2: this would need α_vac = β_Q/Q_needed = 2/7.26 ≈ 0.276, "
        "different from α_vac = 1/3 ≈ 0.333. "
        "Alternatively: with α_vac = 1/3 and R = 1, β_Q would need to be "
        "β_Q = Q_needed × α_vac = 7.26/3 ≈ 2.42, different from β_Q = 2. "
        "Neither is consistent with the locked endpoint law R_eq/r_s = 1/3."
    )

    # Could a different entropy exponent (S ∝ R^n) close the gap?
    entropy_exponent_for_R_one: str = (
        "If S ∝ R^n (not R^2), then dS/dM ∝ M^(n-1) × G^(n/2). "
        "For n = 3/2 (volumetric-like): dS/dM ∝ M^(1/2). "
        "Then T = c²/dS_dM ∝ M^(-1/2) (faster cooling than T_Hawking ∝ M^(-1)). "
        "This would change the mass scaling and close the gap only for specific M. "
        "There is no GRUT quantity that motivates S ∝ R^(3/2)."
    )

    # Bottom line
    gap_origin: str = (
        "R = 4π√3/(3Q) arises from the combination of: "
        "(i) T_dissipation uses Q = 6 (barrier damping ratio), "
        "(ii) S_eq uses R_eq = r_s/3 (area ratio = 1/9 of horizon area). "
        "These two constraints — one from the mode damping, one from the "
        "endpoint geometry — are independent GRUT results that do not "
        "jointly satisfy the first law. The factor 4π√3 comes from "
        "expressing ω₀ = sqrt(2GM/R_eq³) = 3√3c³/(2GM) in terms of M."
    )


@dataclass
class FirstLawGapResult:
    """Master result from the first-law gap audit."""
    # The gap
    R_gap: float = R_GAP
    R_gap_formula: str = "R = 2*pi*sqrt(3)/9 ≈ 1.209"
    R_gap_mass_independent: bool = True

    # Three option verdicts
    option_a_entropy: EntropyRevisionAnalysis = field(
        default_factory=EntropyRevisionAnalysis
    )
    option_b_temperature: TemperatureRevisionAnalysis = field(
        default_factory=TemperatureRevisionAnalysis
    )
    option_c_work: BarrierWorkAnalysis = field(
        default_factory=BarrierWorkAnalysis
    )

    # Gap structure
    gap_structure: GapStructureAnalysis = field(
        default_factory=GapStructureAnalysis
    )

    # Executive determination
    executive_determination: str = ""
    determination_explanation: str = ""

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)

    # Inherited classifications
    appendix_d_classification: str = "thermodynamic_sector_partially_consistent"
    appendix_e_classification: str = "locally_consistent_globally_underdetermined"
    appendix_h_classification: str = "temperature_selectable_conditionally_not_uniquely"

    valid: bool = False

    def assert_no_unsupported_claims(self) -> None:
        for forbidden in _FORBIDDEN_CLASSIFICATIONS:
            if forbidden in self.executive_determination:
                raise AssertionError(
                    f"Forbidden classification '{forbidden}' in "
                    f"executive_determination."
                )


# ================================================================
# Computation Helpers
# ================================================================

def compute_barrier_potential_at_Req(
    M_kg: float,
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> float:
    """Compute V_Q(R_eq) in units of c² (should be -0.5, M-independent).

    The barrier potential:
        V_Q(R) = -GM * epsilon_Q * r_s^beta_Q / ((1+beta_Q) * R^(1+beta_Q))

    At R_eq = r_s * epsilon_Q^(1/beta_Q):
        epsilon_Q * (r_s/R_eq)^beta_Q = 1  (by definition of R_eq)
        V_Q(R_eq) = -GM / ((1+beta_Q) * R_eq)

    Returns
    -------
    float
        V_Q(R_eq) / c² (dimensionless). Expected: -1/(1+beta_Q) × (r_s/R_eq)
    """
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    R_eq = r_s * epsilon_Q ** (1.0 / beta_Q)

    # V_Q(R_eq) = -GM * epsilon_Q * r_s^beta_Q / ((1+beta_Q) * R_eq^(1+beta_Q))
    numerator = G_SI * M_kg * epsilon_Q * r_s ** beta_Q
    denominator = (1.0 + beta_Q) * R_eq ** (1.0 + beta_Q)

    V_Q = -numerator / denominator
    return V_Q / C_SI ** 2


def compute_barrier_potential_simplified(
    M_kg: float,
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> float:
    """Simplified form: V_Q(R_eq) = -GM/r_s = -c²/2 → should return -0.5.

    At R_eq, epsilon_Q * (r_s/R_eq)^beta_Q = 1, so:
        V_Q(R_eq) = -GM * (1/((1+beta_Q)*R_eq))
                  = -GM / ((1+beta_Q) * r_s * epsilon_Q^(1/beta_Q))
    """
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    # V_Q(R_eq) = -GM/r_s for beta_Q = 2 (where (1+beta_Q)*epsilon_Q^(1/beta_Q) = 3*(1/3) = 1)
    # General formula: V_Q(R_eq) = -GM / ((1+beta_Q) * R_eq)
    R_eq = r_s * epsilon_Q ** (1.0 / beta_Q)
    V_Q = -G_SI * M_kg / ((1.0 + beta_Q) * R_eq)
    return V_Q / C_SI ** 2


def verify_V_Q_mass_independence(
    masses_solar: List[float] = None,
    alpha_vac: float = ALPHA_VAC,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> Dict[str, float]:
    """Verify that V_Q(R_eq)/c² is the same for all masses.

    Returns dict: {M_solar: V_Q_ratio} for each mass.
    """
    if masses_solar is None:
        masses_solar = [10.0, 30.0, 100.0, 1e6]

    results = {}
    for M_solar in masses_solar:
        M_kg = M_solar * M_SUN_KG
        v = compute_barrier_potential_at_Req(M_kg, alpha_vac, beta_Q, epsilon_Q)
        results[M_solar] = v
    return results


def compute_V_Q_exact_ratio(
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> float:
    """Compute V_Q(R_eq)/c² exactly from parameters alone.

    V_Q(R_eq) = -GM/((1+beta_Q)*R_eq) = -GM/((1+beta_Q)*r_s*epsilon_Q^(1/beta_Q))
    V_Q/c² = -1/(2*(1+beta_Q)*epsilon_Q^(1/beta_Q))

    For beta_Q=2, epsilon_Q=1/9: = -1/(2*3*(1/3)) = -1/2 ✓
    """
    R_eq_over_rs = epsilon_Q ** (1.0 / beta_Q)
    # V_Q(R_eq) = -GM/((1+beta_Q)*R_eq) and r_s = 2GM/c²
    # V_Q/c² = -GM/(c² * (1+beta_Q)*R_eq) = -r_s/(2*(1+beta_Q)*R_eq)
    #        = -1/(2*(1+beta_Q)*R_eq_over_rs)
    return -1.0 / (2.0 * (1.0 + beta_Q) * R_eq_over_rs)


def compute_required_entropy_ratio(R_gap: float = R_GAP) -> float:
    """The entropy ratio S_correct/S_eq required to close the gap.

    For T_dissipation to satisfy the first law: S_correct = S_eq/R.
    Returns S_correct/S_eq = 1/R.
    """
    return 1.0 / R_gap


def compute_effective_radius_ratio(R_gap: float = R_GAP) -> float:
    """The effective radius ratio R_eff/R_eq for the required entropy.

    S_correct = pi * R_eff^2 / l_P^2  where R_eff = R_eq/sqrt(R).
    Returns R_eff/R_eq = 1/sqrt(R).
    """
    return 1.0 / math.sqrt(R_gap)


def compute_T_1stlaw_over_T_diss(R_gap: float = R_GAP) -> float:
    """T_1stlaw/T_dissipation = 1/R (the temperature revision factor)."""
    return 1.0 / R_gap


def compute_R_gap_for_exact_R_one(
    R_eq_over_rs: float = R_EQ_OVER_RS,
) -> float:
    """Compute what Q would be needed for R = 1 (gap closed by Q revision).

    R = 4π√3/(3Q) = 1 → Q_needed = 4π√3/3.
    """
    return 4.0 * math.pi * math.sqrt(3.0) / 3.0


def compute_alpha_needed_for_R_one(
    beta_Q: float = BETA_Q,
) -> float:
    """Compute α_vac needed for R = 1 (with beta_Q = 2).

    Q = beta_Q/alpha_vac → alpha_vac = beta_Q/Q_needed.
    """
    Q_needed = compute_R_gap_for_exact_R_one()
    return beta_Q / Q_needed


# ================================================================
# Option Builders
# ================================================================

def build_barrier_work_analysis(
    M_kg: float = M_REF_KG,
) -> BarrierWorkAnalysis:
    """Build the barrier work analysis."""
    # Verify V_Q is M-independent
    v_ratio = compute_barrier_potential_at_Req(M_kg)
    return BarrierWorkAnalysis(
        V_Q_value_over_c_sq=v_ratio,
        delta_V_Q_over_delta_M=0.0,
    )


def build_entropy_revision_analysis(
    R_gap: float = R_GAP,
) -> EntropyRevisionAnalysis:
    """Build the entropy revision analysis."""
    s_ratio = compute_required_entropy_ratio(R_gap)
    r_eff_ratio = compute_effective_radius_ratio(R_gap)
    return EntropyRevisionAnalysis(
        S_required_over_S_current=s_ratio,
        R_eff_over_R_eq=r_eff_ratio,
    )


def build_temperature_revision_analysis(
    M_kg: float = M_REF_KG,
    R_gap: float = R_GAP,
) -> TemperatureRevisionAnalysis:
    """Build the temperature revision analysis."""
    T_1stlaw_over_T_diss = compute_T_1stlaw_over_T_diss(R_gap)

    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    omega_0 = math.sqrt(BETA_Q * G_SI * M_kg / (R_EQ_OVER_RS * r_s) ** 3)
    T_struct = HBAR_SI * omega_0 / K_B
    T_1stlaw_over_T_struct = T_1stlaw_over_T_diss / Q_CANONICAL

    return TemperatureRevisionAnalysis(
        T_1stlaw_over_T_diss=T_1stlaw_over_T_diss,
        T_1stlaw_in_grut_terms=(
            f"T_1stlaw = 9*T_Hawking = 9*ℏ/(4π*k_B*τ_Schwarz) "
            f"where τ_Schwarz = r_s/c = 2GM/c³. "
            f"For 30 M_sun: T_1stlaw ≈ "
            f"{9 * HBAR_SI * C_SI**3 / (8*math.pi*G_SI*M_kg*K_B):.4e} K."
        ),
        T_1stlaw_grut_native=False,   # r_s/c is Schwarzschild, same as T_H
        T_1stlaw_vs_T_structural=(
            f"T_1stlaw/T_structural = {T_1stlaw_over_T_struct:.4f} "
            f"= 1/(R*Q) = 9/(2π√3×Q)"
        ),
        T_1stlaw_vs_T_dissipation=(
            f"T_1stlaw/T_dissipation = {T_1stlaw_over_T_diss:.4f} = 1/R"
        ),
    )


def build_gap_structure(R_gap: float = R_GAP) -> GapStructureAnalysis:
    """Build the gap structure analysis."""
    Q_for_R_one = compute_R_gap_for_exact_R_one()
    alpha_for_R_one = compute_alpha_needed_for_R_one()
    return GapStructureAnalysis(
        R_gap=R_gap,
        R_equals_one_requires=(
            f"R = 1 requires Q = 4π√3/3 ≈ {Q_for_R_one:.4f}. "
            f"With β_Q = 2: α_vac = β_Q/Q = 2/{Q_for_R_one:.4f} ≈ {alpha_for_R_one:.4f} "
            f"(current α_vac = 1/3 ≈ 0.333). "
            f"Gap cannot be closed by adjusting GRUT parameters without "
            f"violating the locked endpoint law R_eq/r_s = 1/3."
        ),
    )


# ================================================================
# Master Audit Runner
# ================================================================

def run_first_law_gap_audit(
    M_kg: float = M_REF_KG,
) -> FirstLawGapResult:
    """Run the complete first-law gap audit.

    Parameters
    ----------
    M_kg : float
        Reference mass (default: 30 M_sun).

    Returns
    -------
    FirstLawGapResult
        Full audit result with option verdicts and executive determination.
    """
    result = FirstLawGapResult(R_gap=R_GAP)

    # Option (c): barrier work
    result.option_c_work = build_barrier_work_analysis(M_kg)

    # Option (a): entropy revision
    result.option_a_entropy = build_entropy_revision_analysis()

    # Option (b): temperature revision
    result.option_b_temperature = build_temperature_revision_analysis(M_kg)

    # Gap structure
    result.gap_structure = build_gap_structure()

    # Executive determination
    result.executive_determination = "gap_structural_no_external_free_parameter"
    result.determination_explanation = (
        "The first-law gap R = 2π√3/9 ≈ 1.209 is structural. "
        "Option (c) — missing work term — is CLOSED: the barrier potential "
        "V_Q(R_eq) = −c²/2 is M-independent (dV_Q/dM = 0), and memory "
        "does no work at V = 0. "
        "Option (a) — entropy revision — is STRUCTURALLY_POSSIBLE but requires "
        "S_correct = S_eq/R, a constant rescaling with no GRUT-native motivation. "
        "Option (b) — temperature revision — is VIABLE: T_1stlaw = T_diss/R = "
        "9·T_Hawking closes the gap exactly with S_eq, but T_1stlaw is not a "
        "GRUT-native quantity (it equals 9 times the imported Hawking temperature). "
        "No GRUT parameter can be adjusted to close the gap without violating "
        "the locked endpoint law: R = 1 would require α_vac ≈ 0.276 "
        "(current: 1/3 ≈ 0.333) or β_Q ≈ 2.42 (current: 2). "
        "The gap is a permanent feature of the current GRUT thermodynamic sector "
        "until either the temperature selection or entropy proxy is resolved."
    )

    # Safe claims
    result.safe_claims = [
        "V_Q(R_eq) = −c²/2 exactly, independent of mass (proven algebraically "
        "from ε_Q·(r_s/R_eq)^β_Q = 1).",

        "The barrier does zero thermodynamic work for quasi-static mass changes: "
        "dV_Q/dM = 0.",

        "The memory sector does zero work at the equilibrium endpoint (V = 0).",

        "Option (c) — missing work term — is eliminated. The gap persists "
        "even with a complete barrier + memory work accounting.",

        "Option (a) — entropy revision — closes the gap with S_correct = S_eq/R, "
        "but 1/√R is not a GRUT-native geometric ratio.",

        "Option (b) — temperature revision — closes the gap with T_1stlaw = 9·T_H. "
        "T_1stlaw = 9·T_Hawking is expressible without T_H as "
        "9·ℏ/(4π·k_B·τ_Schwarz), but τ_Schwarz = r_s/c is the same parameter "
        "as in T_Hawking.",

        "R = 1 (exact first law with T_diss and S_eq) would require α_vac ≈ 0.276 "
        "or β_Q ≈ 2.42, incompatible with the locked endpoint law.",
    ]

    result.unsafe_claims = [
        "The gap is due to a missing physical term.",
        "Revising the entropy to S_eq/R is GRUT-motivated.",
        "T_1stlaw = 9·T_Hawking is GRUT-native (it imports the Schwarzschild structure).",
        "The gap closes with current GRUT parameters.",
    ]

    result.nonclaims = [
        "This module does NOT close the first-law gap.",
        "This module does NOT identify the correct temperature.",
        "This module does NOT prove the area-law entropy is wrong.",
        "This module does NOT upgrade any prior classification.",
    ]

    result.valid = True
    result.assert_no_unsupported_claims()
    return result


# ================================================================
# Convenience: Summary String
# ================================================================

def summary_string(result: FirstLawGapResult) -> str:
    """Return a human-readable summary."""
    bw = result.option_c_work
    ea = result.option_a_entropy
    tr = result.option_b_temperature

    lines = [
        "=== APPENDIX I: FIRST-LAW GAP AUDIT SUMMARY ===",
        "",
        f"Gap: R = {result.R_gap:.6f} = 2π√3/9 (mass-independent, ≠ 1)",
        "",
        "--- Option (c): Missing Work Term ---",
        f"  V_Q(R_eq)/c² = {bw.V_Q_value_over_c_sq:.6f}  (expected -0.5)",
        f"  dV_Q/dM = {bw.delta_V_Q_over_delta_M:.4f}",
        f"  Verdict: {bw.verdict}",
        "",
        "--- Option (a): Entropy Revision ---",
        f"  S_correct/S_eq = {ea.S_required_over_S_current:.6f} = 1/R",
        f"  R_eff/R_eq = {ea.R_eff_over_R_eq:.6f} = 1/√R",
        f"  GRUT-native motivation: {ea.grut_native_motivation}",
        f"  Verdict: {ea.verdict}",
        "",
        "--- Option (b): Temperature Revision ---",
        f"  T_1stlaw/T_diss = {tr.T_1stlaw_over_T_diss:.6f} = 1/R",
        f"  T_1stlaw is GRUT-native: {tr.T_1stlaw_grut_native}",
        f"  Verdict: {tr.verdict}",
        "",
        "--- Gap Structure ---",
        f"  R = 4π√3/(3Q), Q = {Q_CANONICAL:.1f}",
        f"  α_vac needed for R=1: {compute_alpha_needed_for_R_one():.4f} "
        f"(current: {ALPHA_VAC:.4f})",
        "",
        f"Executive: {result.executive_determination}",
        "",
        "--- Inherited Classifications (unchanged) ---",
        f"  Appendix D: {result.appendix_d_classification}",
        f"  Appendix E: {result.appendix_e_classification}",
        f"  Appendix H: {result.appendix_h_classification}",
    ]

    return "\n".join(lines)
