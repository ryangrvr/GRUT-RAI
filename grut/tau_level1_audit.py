"""GRUT Appendix G — Level-1 τ Reduction Derivation and Justification Audit.

QUESTION BEING ANSWERED
-----------------------
When does local gravitational reduction activate, and why?

The Level-1 rule is:
    τ_base = τ₀ · t_dyn / (t_dyn + τ₀)

where:
    t_dyn = sqrt(R³ / (2GM))    (local Newtonian free-fall timescale)
    τ₀ = 1.3225×10¹⁵ s          (global Phase I cosmological anchor)

This rule is currently implemented as a mode switch `local_tau_mode = "tier0"`
in collapse.py. This module determines:
  (a) whether the formula has a derivational basis,
  (b) what the natural activation criterion is,
  (c) whether the mode switch can be replaced by a deterministic condition.

STRUCTURAL IDENTITY CONNECTION
-------------------------------
The structural identity ω₀·τ = 1 (locked in interior_pde.py) requires τ = τ_local,
not τ₀. For astrophysical BH masses, t_dyn(R_eq) << τ₀, so:

    τ_local ≈ t_dyn(R_eq)

And it can be shown algebraically:

    ω₀ · t_dyn(R_eq) = sqrt(β_Q · GM / R_eq³) · sqrt(R_eq³ / (2GM))
                     = sqrt(β_Q / 2) = 1    (exactly, for β_Q = 2)

So the structural identity ω₀·τ = 1 is DERIVED from β_Q = 2 and τ ≈ t_dyn.
The Level-1 rule is the necessary condition for this identity to hold physically.

THREE DERIVATION ROUTES
-----------------------
Route A — Parallel-rate (competing channels):
    The formula τ_local = τ₀·t_dyn/(τ₀+t_dyn) is equivalent to a parallel
    rate sum: 1/τ_local = 1/τ₀ + 1/t_dyn.
    Physical motivation: the cosmological bath (rate 1/τ₀) and the local
    dynamical channel (rate 1/t_dyn) both contribute to relaxation, with
    total rate = sum of rates.
    Verdict: PARTIALLY_VIABLE — motivates the formula; the local channel
    requires a causality argument, not derived from GRUT field equations.

Route B — Covariant reduction:
    The GRUT field equation τ_eff u^α ∇_α Φ + Φ = X contains τ_eff.
    If τ_eff = τ_local is the correct covariant form in the collapsing regime,
    this would derive the Level-1 rule. But this requires the interior covariant
    metric, which is a missing closure (PHASE_III_C_COVARIANT_CLOSURE.md).
    Verdict: CLOSED — requires unresolved covariant interior solution.

Route C — Structural consistency retroactive:
    τ_local is the UNIQUE closure that makes ω₀·τ = 1 hold for astrophysical
    masses. This is verifiable algebraically. But it is a consistency argument,
    not a derivation: the structural identity was derived USING τ_local, so
    showing τ_local is required for it is circular.
    Verdict: CONSISTENCY_ARGUMENT_NOT_DERIVATION.

ACTIVATION CRITERION
--------------------
The Level-1 rule should activate when:
    t_dyn < τ₀
which is equivalent to:
    R < R_cross = (2GM · τ₀²)^(1/3)

For astrophysical masses (e.g., 30 M_sun), R_cross >> r_s >> R_eq.
This means Level-1 ALWAYS activates for any realistic BH radius.

EXECUTIVE DETERMINATION
-----------------------
The Level-1 rule is a `structurally_motivated_heuristic_not_derived`.
  - It is ALGEBRAICALLY CORRECT for all astrophysical masses.
  - The mode switch `local_tau_mode` should be "tier0" for astrophysical physics;
    "off" is only valid for cosmological parameter ranges (R > R_cross).
  - Covariant derivation remains BLOCKED by the missing interior metric closure.
  - A deterministic (non-covariant) activation criterion EXISTS:
    t_dyn < τ₀ ⟺ R < R_cross = (2GM·τ₀²)^(1/3).

WHAT THIS MODULE DOES NOT CLAIM:
  - Does NOT claim the Level-1 rule is covariant.
  - Does NOT claim a derivation from GRUT field equations exists.
  - Does NOT claim the mode switch is obsolete (it is still needed for testing).
  - Does NOT claim the causality argument is a proof.
  - Does NOT upgrade any prior appendix classification.

LOCKED INHERITANCE:
  - Appendix E: locally_consistent_globally_underdetermined UNCHANGED.
  - Appendix F: tau_symbolically_conflated_but_rescuable UNCHANGED.
  - Appendix D: thermodynamic_sector_partially_consistent UNCHANGED.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# ================================================================
# Physical Constants (SI)
# ================================================================

G_SI = 6.674e-11           # m³ kg⁻¹ s⁻²
C_SI = 299_792_458.0       # m/s
HBAR_SI = 1.054571817e-34  # J·s
K_B = 1.380649e-23         # J/K

# ================================================================
# Canonical GRUT Parameters (locked)
# ================================================================

TAU_0_S = 1.3225e15          # s — global Phase I anchor
ALPHA_VAC = 1.0 / 3.0        # dimensionless
BETA_Q = 2.0                 # dimensionless
EPSILON_Q = ALPHA_VAC ** 2   # = 1/9
R_EQ_OVER_RS = EPSILON_Q ** (1.0 / BETA_Q)   # = 1/3

M_SUN_KG = 1.989e30
M_REF_KG = 30.0 * M_SUN_KG   # reference: 30 M_sun

# Expected structural identity value (locked)
OMEGA_0_TAU_IDENTITY = 1.0

# ================================================================
# Forbidden classification strings (guard)
# ================================================================

_FORBIDDEN_CLASSIFICATIONS = {
    "level1_covariant",
    "level1_derived_from_action",
    "level1_derived_from_field_equations",
    "mode_switch_obsolete",
    "tau_local_equals_tau0",
    "structural_identity_not_needed",
}


# ================================================================
# Data Structures
# ================================================================

@dataclass
class Level1TimescalePoint:
    """τ-family values at a single radius R for a given mass M."""
    label: str
    R_m: float
    M_kg: float

    # Timescales
    tau0_s: float = 0.0
    t_dyn_s: float = 0.0
    tau_local_s: float = 0.0

    # Ratios
    t_dyn_over_tau0: float = 0.0           # < 1 → Level-1 regime
    tau_local_over_tau0: float = 0.0       # ≈ t_dyn/τ₀ when t_dyn << τ₀
    tau_local_over_tdyn: float = 0.0       # ≈ 1.0 when t_dyn << τ₀

    # Mode
    in_level1_regime: bool = False         # t_dyn < τ₀?

    # If this is the equilibrium point: structural identity
    is_equilibrium: bool = False
    omega_0_rad_per_s: float = 0.0
    omega_0_times_tau_local: float = 0.0   # target: 1.0
    omega_0_times_tau0: float = 0.0        # expected >> 1 for astrophysical masses
    omega_0_times_tdyn: float = 0.0        # expected = 1.0 (algebraically exact)


@dataclass
class ParallelRateAnalysis:
    """Route A: Parallel-rate (competing channels) analysis."""
    # Formula verification
    tau_local_formula: str = "tau0 * t_dyn / (tau0 + t_dyn)"
    parallel_rate_formula: str = "1/tau_local = 1/tau0 + 1/t_dyn"
    formulas_equivalent: bool = True   # always true by algebra

    # Physical motivation
    channel_global: str = "Cosmological bath relaxation at rate 1/τ₀"
    channel_local: str = "Local dynamical decoherence at rate 1/t_dyn"
    causality_argument: str = (
        "Memory cannot faithfully integrate gravitational drive over "
        "timescales longer than t_dyn: the drive changes on this scale. "
        "When t_dyn << τ₀, the local channel dominates and τ_local ≈ t_dyn."
    )

    # Status
    formula_derivable_from_parallel_rate: bool = True
    local_channel_derivable_from_grut: bool = False
    verdict: str = ""
    verdict_reason: str = ""


@dataclass
class CovariantReductionAnalysis:
    """Route B: Attempt to derive Level-1 rule from covariant field equations."""
    field_equation: str = "τ_eff u^α ∇_α Φ + Φ = X[g, T]"
    target_formula: str = "τ_eff = τ₀·t_dyn/(τ₀+t_dyn)"

    # What is needed
    requires_interior_metric: bool = True
    requires_covariant_tau_eff: bool = True

    # Status of prerequisites
    interior_metric_available: bool = False
    interior_metric_status: str = "MISSING CLOSURE — see PHASE_III_C_COVARIANT_CLOSURE.md"
    covariant_tau_eff_status: str = (
        "Unknown — τ_eff appears in the field equation but its covariant form "
        "is not specified. It reduces to τ₀/(1+(ωτ₀)²) in the cosmological "
        "regime but the interior form requires the metric."
    )

    verdict: str = "CLOSED"
    verdict_reason: str = (
        "The covariant reduction requires the interior metric, which is a "
        "missing closure. No covariant derivation of the Level-1 formula "
        "is possible without first resolving PHASE_III_C_COVARIANT_CLOSURE."
    )


@dataclass
class StructuralConsistencyAnalysis:
    """Route C: Retroactive structural consistency argument."""
    # The claim
    claim: str = (
        "τ_local is the unique closure that makes ω₀·τ = 1 hold for "
        "all astrophysical masses. This provides a structural justification."
    )

    # Algebraic check
    omega_0_times_tdyn_exact: float = 0.0   # should be exactly 1.0 for β_Q=2
    omega_0_times_tau_local_at_ref: float = 0.0  # should be ≈ 1.0 for large masses

    # Circular reasoning flag
    is_circular: bool = True
    circularity_description: str = (
        "The structural identity ω₀·τ = 1 was derived IN interior_pde.py "
        "using τ = τ_local. Showing that τ_local is required for the identity "
        "to hold cannot be an independent derivation of τ_local — it is a "
        "consistency check, not a proof."
    )

    verdict: str = "CONSISTENCY_ARGUMENT_NOT_DERIVATION"


@dataclass
class ActivationCriterionAnalysis:
    """Analysis of the natural activation criterion for the Level-1 rule."""
    # Criterion
    criterion_formula: str = "t_dyn < τ₀   ⟺   R < R_cross"
    crossover_formula: str = "R_cross = (2GM · τ₀²)^(1/3)"

    # Numerical values at reference mass (30 M_sun)
    M_ref_kg: float = M_REF_KG
    tau0_s: float = TAU_0_S
    R_cross_m: float = 0.0       # crossover radius (m)
    R_cross_over_rs: float = 0.0 # R_cross / r_s
    r_s_m: float = 0.0
    R_eq_m: float = 0.0

    # Is R_eq inside Level-1 regime?
    R_eq_in_level1: bool = False
    t_dyn_at_Req: float = 0.0
    t_dyn_at_Req_over_tau0: float = 0.0

    # Astrophysical universality
    astrophysical_always_level1: bool = False
    universality_argument: str = ""

    # Is the criterion covariant?
    criterion_is_covariant: bool = False
    criterion_is_deterministic: bool = True


@dataclass
class Level1AuditResult:
    """Master result from Appendix G — Level-1 τ Rule Derivation Audit."""
    # Timescale profiles
    timescale_points: List[Level1TimescalePoint] = field(default_factory=list)

    # Derivation routes
    route_a_parallel_rate: ParallelRateAnalysis = field(
        default_factory=ParallelRateAnalysis
    )
    route_b_covariant: CovariantReductionAnalysis = field(
        default_factory=CovariantReductionAnalysis
    )
    route_c_consistency: StructuralConsistencyAnalysis = field(
        default_factory=StructuralConsistencyAnalysis
    )

    # Activation criterion
    activation_criterion: ActivationCriterionAnalysis = field(
        default_factory=ActivationCriterionAnalysis
    )

    # Executive determination
    executive_determination: str = ""
    determination_explanation: str = ""

    # Consequence for mode switch
    mode_switch_recommendation: str = ""
    covariant_criterion_available: bool = False

    # Safe/unsafe claims
    safe_claims: List[str] = field(default_factory=list)
    unsafe_claims: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)
    missing_closures: List[str] = field(default_factory=list)

    # Locked inheritance
    appendix_e_classification: str = "locally_consistent_globally_underdetermined"
    appendix_f_classification: str = "tau_symbolically_conflated_but_rescuable"

    valid: bool = False

    def assert_no_unsupported_claims(self) -> None:
        """Guard against forbidden classification strings."""
        for forbidden in _FORBIDDEN_CLASSIFICATIONS:
            if forbidden in self.executive_determination:
                raise AssertionError(
                    f"Forbidden classification '{forbidden}' found in "
                    f"executive_determination. "
                    f"Appendix G must not claim a covariant or action-derived "
                    f"result for the Level-1 τ rule."
                )


# ================================================================
# Computation Helpers
# ================================================================

def compute_t_dyn(R_m: float, M_kg: float) -> float:
    """Local Newtonian free-fall timescale: t_dyn = sqrt(R³ / (2GM))."""
    return math.sqrt(R_m ** 3 / (2.0 * G_SI * M_kg))


def compute_tau_local(tau0_s: float, t_dyn_s: float) -> float:
    """Level-1 reduction: τ_local = τ₀ · t_dyn / (τ₀ + t_dyn)."""
    return tau0_s * t_dyn_s / (tau0_s + t_dyn_s)


def compute_omega_0(beta_Q: float, M_kg: float, R_eq_m: float) -> float:
    """Barrier restoring frequency: ω₀ = sqrt(β_Q · GM / R_eq³)."""
    return math.sqrt(beta_Q * G_SI * M_kg / R_eq_m ** 3)


def compute_R_cross(M_kg: float, tau0_s: float) -> float:
    """Activation crossover radius: R_cross = (2GM · τ₀²)^(1/3)."""
    return (2.0 * G_SI * M_kg * tau0_s ** 2) ** (1.0 / 3.0)


# ================================================================
# Timescale Profile Builder
# ================================================================

def build_timescale_profile(
    M_kg: float = M_REF_KG,
    tau0_s: float = TAU_0_S,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> List[Level1TimescalePoint]:
    """Build the τ-family profile at key radii for a given mass.

    Evaluated at:
    - R_0 = 100 · r_s: far from horizon (start of collapse)
    - R = r_s: Schwarzschild radius
    - R_eq = r_s/3: GRUT equilibrium endpoint
    """
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    R_eq = R_EQ_OVER_RS * r_s   # = r_s / 3
    omega_0 = compute_omega_0(beta_Q, M_kg, R_eq)

    radii = [
        ("R_0 = 100·r_s (far exterior)", 100.0 * r_s, False),
        ("r_s (Schwarzschild radius)", r_s, False),
        ("R_eq = r_s/3 (GRUT endpoint)", R_eq, True),
    ]

    points = []
    for label, R, is_eq in radii:
        t_dyn = compute_t_dyn(R, M_kg)
        tau_local = compute_tau_local(tau0_s, t_dyn)

        pt = Level1TimescalePoint(
            label=label,
            R_m=R,
            M_kg=M_kg,
            tau0_s=tau0_s,
            t_dyn_s=t_dyn,
            tau_local_s=tau_local,
            t_dyn_over_tau0=t_dyn / tau0_s,
            tau_local_over_tau0=tau_local / tau0_s,
            tau_local_over_tdyn=tau_local / t_dyn if t_dyn > 0 else 0.0,
            in_level1_regime=(t_dyn < tau0_s),
            is_equilibrium=is_eq,
        )

        if is_eq:
            pt.omega_0_rad_per_s = omega_0
            pt.omega_0_times_tau_local = omega_0 * tau_local
            pt.omega_0_times_tau0 = omega_0 * tau0_s
            pt.omega_0_times_tdyn = omega_0 * t_dyn

        points.append(pt)

    return points


# ================================================================
# Route A: Parallel-Rate Analysis
# ================================================================

def build_parallel_rate_analysis() -> ParallelRateAnalysis:
    """Route A: Analyse the parallel-rate (competing-channels) justification."""
    result = ParallelRateAnalysis()

    # Verify algebraic equivalence
    tau0 = 1.0   # normalized
    tdyn = 0.7   # arbitrary test value
    tau_from_formula = tau0 * tdyn / (tau0 + tdyn)
    rate_sum = 1.0 / tau0 + 1.0 / tdyn
    tau_from_rate = 1.0 / rate_sum
    result.formulas_equivalent = abs(tau_from_formula - tau_from_rate) < 1e-12

    result.verdict = "PARTIALLY_VIABLE"
    result.verdict_reason = (
        "The parallel-rate formula 1/τ_local = 1/τ₀ + 1/t_dyn is algebraically "
        "equivalent to the Level-1 rule and provides physical motivation: two "
        "competing relaxation channels (cosmological bath at rate 1/τ₀, local "
        "dynamical decoherence at rate 1/t_dyn) give total rate = sum of rates. "
        "The local channel is motivated by the causality argument that memory "
        "cannot faithfully integrate over timescales longer than t_dyn. "
        "HOWEVER: the local channel is not derived from GRUT field equations — "
        "it is a physically motivated heuristic. A full derivation would require "
        "showing that the GRUT constitutive equation τ_eff u^α∇_α Φ + Φ = X "
        "generates a local rate 1/t_dyn in the strong-field regime."
    )

    return result


# ================================================================
# Route B: Covariant Reduction Analysis
# ================================================================

def build_covariant_reduction_analysis() -> CovariantReductionAnalysis:
    """Route B: Assess the covariant reduction derivation attempt."""
    result = CovariantReductionAnalysis()
    # All values set in the dataclass defaults — nothing can be computed here
    # without the missing interior metric.
    return result


# ================================================================
# Route C: Structural Consistency Analysis
# ================================================================

def build_structural_consistency_analysis(
    M_kg: float = M_REF_KG,
    tau0_s: float = TAU_0_S,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> StructuralConsistencyAnalysis:
    """Route C: Structural consistency check.

    ω₀·t_dyn(R_eq) = sqrt(β_Q/2) = 1 (exact for β_Q=2).
    ω₀·τ_local(R_eq) ≈ 1.0 for t_dyn(R_eq) << τ₀.
    """
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    R_eq = R_EQ_OVER_RS * r_s
    omega_0 = compute_omega_0(beta_Q, M_kg, R_eq)
    t_dyn_eq = compute_t_dyn(R_eq, M_kg)
    tau_local_eq = compute_tau_local(tau0_s, t_dyn_eq)

    result = StructuralConsistencyAnalysis(
        omega_0_times_tdyn_exact=omega_0 * t_dyn_eq,
        omega_0_times_tau_local_at_ref=omega_0 * tau_local_eq,
    )
    return result


# ================================================================
# Activation Criterion Analysis
# ================================================================

def build_activation_criterion(
    M_kg: float = M_REF_KG,
    tau0_s: float = TAU_0_S,
    epsilon_Q: float = EPSILON_Q,
) -> ActivationCriterionAnalysis:
    """Determine the natural activation criterion for the Level-1 rule."""
    r_s = 2.0 * G_SI * M_kg / C_SI ** 2
    R_eq = R_EQ_OVER_RS * r_s
    R_cross = compute_R_cross(M_kg, tau0_s)
    t_dyn_eq = compute_t_dyn(R_eq, M_kg)

    result = ActivationCriterionAnalysis(
        M_ref_kg=M_kg,
        tau0_s=tau0_s,
        R_cross_m=R_cross,
        R_cross_over_rs=R_cross / r_s,
        r_s_m=r_s,
        R_eq_m=R_eq,
        R_eq_in_level1=(R_eq < R_cross),
        t_dyn_at_Req=t_dyn_eq,
        t_dyn_at_Req_over_tau0=t_dyn_eq / tau0_s,
        astrophysical_always_level1=(R_cross > r_s),
        universality_argument=(
            f"For M = {M_kg/M_SUN_KG:.0f} M_sun: "
            f"R_cross = {R_cross:.3e} m, "
            f"r_s = {r_s:.3e} m. "
            f"R_cross / r_s = {R_cross/r_s:.3e}. "
            f"Since R_cross >> r_s >> R_eq for all astrophysical masses, "
            f"the Level-1 criterion t_dyn < τ₀ is always satisfied for "
            f"any realistic BH radius. The mode switch 'local_tau_mode=off' "
            f"is non-physical for astrophysical applications."
        ),
        criterion_is_covariant=False,
        criterion_is_deterministic=True,
    )

    return result


# ================================================================
# Master Audit Runner
# ================================================================

def run_level1_audit(
    M_kg: float = M_REF_KG,
    tau0_s: float = TAU_0_S,
    beta_Q: float = BETA_Q,
    epsilon_Q: float = EPSILON_Q,
) -> Level1AuditResult:
    """Run the complete Level-1 τ rule derivation audit.

    Parameters
    ----------
    M_kg : float
        Reference mass (default: 30 M_sun).
    tau0_s : float
        Global cosmological memory timescale (s).
    beta_Q : float
        Barrier exponent (canon: 2).
    epsilon_Q : float
        Barrier amplitude (canon: 1/9).

    Returns
    -------
    Level1AuditResult
        Full audit result with derivation route verdicts and
        the executive determination.
    """
    result = Level1AuditResult()

    # Build timescale profile
    result.timescale_points = build_timescale_profile(M_kg, tau0_s, beta_Q, epsilon_Q)

    # Route A
    result.route_a_parallel_rate = build_parallel_rate_analysis()

    # Route B
    result.route_b_covariant = build_covariant_reduction_analysis()

    # Route C
    result.route_c_consistency = build_structural_consistency_analysis(
        M_kg, tau0_s, beta_Q, epsilon_Q
    )

    # Activation criterion
    result.activation_criterion = build_activation_criterion(M_kg, tau0_s, epsilon_Q)

    # Executive determination
    result.executive_determination = "structurally_motivated_heuristic_not_derived"
    result.determination_explanation = (
        "The Level-1 τ rule τ_local = τ₀·t_dyn/(τ₀+t_dyn) is physically "
        "motivated by the parallel-rate argument (Route A) and algebraically "
        "consistent with the structural identity ω₀·τ = 1 (Route C). It is "
        "NOT derived from GRUT field equations (Route B is CLOSED). The formula "
        "is correct for all astrophysical masses because t_dyn << τ₀ everywhere "
        "inside R_cross >> r_s. A deterministic activation criterion exists: "
        "t_dyn < τ₀ ⟺ R < R_cross = (2GM·τ₀²)^(1/3). This criterion is "
        "non-covariant but deterministic — it can replace the manual mode "
        "switch for astrophysical physics. Covariant derivation remains BLOCKED "
        "pending the interior metric closure."
    )

    # Mode switch recommendation
    result.mode_switch_recommendation = (
        "For all astrophysical BH masses: always use local_tau_mode='tier0'. "
        "The criterion t_dyn < τ₀ is satisfied at every realistic radius. "
        "local_tau_mode='off' is only valid for: (a) code validation tests, "
        "(b) hypothetical masses where R > R_cross (no known astrophysical example). "
        "The mode switch can in principle be replaced by the deterministic condition "
        "t_dyn < τ₀, but this is not covariant."
    )

    result.covariant_criterion_available = False

    # Safe claims
    result.safe_claims = [
        "τ_local = τ₀·t_dyn/(τ₀+t_dyn) is algebraically equivalent to a "
        "parallel-rate sum: 1/τ_local = 1/τ₀ + 1/t_dyn.",

        "For all astrophysical BH masses, t_dyn(R_eq) << τ₀, so "
        "τ_local ≈ t_dyn(R_eq) to high accuracy.",

        "ω₀·t_dyn(R_eq) = 1 exactly (algebraic identity from β_Q=2 and "
        "R_eq = r_s·ε_Q^(1/β_Q) = r_s/3), independent of mass.",

        "ω₀·τ_local(R_eq) ≈ 1.0 for astrophysical masses (relative error "
        "≈ t_dyn/τ₀ ~ 10⁻¹⁹ for 30 M_sun).",

        "The Level-1 rule is a NECESSARY CONDITION for ω₀·τ = 1 to hold "
        "with physical validity (using τ_local, not τ₀).",

        "A deterministic activation criterion exists: Level-1 activates when "
        "t_dyn < τ₀, i.e., R < R_cross = (2GM·τ₀²)^(1/3).",

        "For 30 M_sun: R_cross >> r_s, so Level-1 ALWAYS activates for any "
        "astrophysically realistic BH radius.",
    ]

    # Unsafe claims
    result.unsafe_claims = [
        "The Level-1 rule is derived from GRUT field equations.",
        "The Level-1 rule is covariant.",
        "The causality argument for the local channel is a proof.",
        "The structural consistency argument (Route C) is an independent derivation.",
        "local_tau_mode='off' is the correct default for astrophysical physics.",
    ]

    # Nonclaims
    result.nonclaims = [
        "This module does NOT derive the Level-1 rule from a variational principle.",
        "This module does NOT claim the mode switch is obsolete.",
        "This module does NOT prove that the local dynamical channel exists in GRUT.",
        "This module does NOT upgrade any prior appendix classification.",
    ]

    # Missing closures
    result.missing_closures = [
        "Covariant interior metric — needed for Route B (PHASE_III_C_COVARIANT_CLOSURE.md).",
        "Derivation of local dynamical relaxation channel from GRUT field equations.",
        "Proof that ω_local = 1/t_dyn is the correct local frequency in the "
        "covariant GRUT constitutive equation.",
    ]

    result.valid = True

    # Forbidden claim guard
    result.assert_no_unsupported_claims()

    return result


# ================================================================
# Convenience: Summary String
# ================================================================

def summary_string(result: Level1AuditResult) -> str:
    """Return a human-readable summary of the Level-1 audit."""
    eq_pt = next((p for p in result.timescale_points if p.is_equilibrium), None)
    ac = result.activation_criterion

    lines = [
        "=== APPENDIX G: LEVEL-1 τ RULE AUDIT SUMMARY ===",
        "",
        f"Executive determination: {result.executive_determination}",
        "",
        "--- Timescales at equilibrium (R_eq = r_s/3) ---",
    ]

    if eq_pt is not None:
        lines += [
            f"  τ₀          = {eq_pt.tau0_s:.4e} s",
            f"  t_dyn(R_eq) = {eq_pt.t_dyn_s:.4e} s",
            f"  τ_local     = {eq_pt.tau_local_s:.4e} s",
            f"  t_dyn/τ₀    = {eq_pt.t_dyn_over_tau0:.4e}  (Level-1 regime: {eq_pt.in_level1_regime})",
            f"  ω₀·t_dyn    = {eq_pt.omega_0_times_tdyn:.6f}  (target: 1.0)",
            f"  ω₀·τ_local  = {eq_pt.omega_0_times_tau_local:.6f}  (target: 1.0)",
            f"  ω₀·τ₀       = {eq_pt.omega_0_times_tau0:.4e}  (expected >> 1)",
        ]

    lines += [
        "",
        "--- Activation Criterion ---",
        f"  t_dyn < τ₀  ⟺  R < R_cross",
        f"  R_cross = {ac.R_cross_m:.4e} m  =  {ac.R_cross_over_rs:.4e} × r_s",
        f"  r_s     = {ac.r_s_m:.4e} m",
        f"  R_eq always inside Level-1 regime: {ac.R_eq_in_level1}",
        f"  Astrophysical universality: {ac.astrophysical_always_level1}",
        "",
        "--- Derivation Routes ---",
        f"  Route A (parallel-rate):     {result.route_a_parallel_rate.verdict}",
        f"  Route B (covariant reduction): {result.route_b_covariant.verdict}",
        f"  Route C (structural consistency): {result.route_c_consistency.verdict}",
        "",
        "--- Mode Switch ---",
        result.mode_switch_recommendation,
        "",
        "--- Inherited Classifications (unchanged) ---",
        f"  Appendix E: {result.appendix_e_classification}",
        f"  Appendix F: {result.appendix_f_classification}",
    ]

    return "\n".join(lines)
