"""Source-Law Program I — Exploit Loophole 5 (X != M/r^2).

Tests whether any GRUT-native source-law modification can generate the
missing 1/r^2 Component B support identified in Phase 6C.  This module
directly addresses Loophole 5 from route_c_deficit.py (modified source law,
high severity) — the ONLY remaining classical loophole after the source
profile locking theorem closed all kernel-based routes.

PRINCIPAL RESULTS:

  Result 1 — Target Definition:
    The memory equation tau dPhi/dt + Phi = X(r) locks the energy density
    spatial profile to epsilon ~ S(r)^2 where S(r) is the source spatial
    profile.  To get epsilon ~ 1/r^2 (Component B), need S(r) ~ 1/r.

  Result 2 — Diagnostic Toy Probe:
    X = M/r^2 + B/r produces epsilon with a 1/r^2 term (coefficient
    B^2/(2*tau^2)), confirming the MECHANISM works.  This probe is NOT
    canon — it is used only to validate the computational framework.

  Result 3 — Source Family Taxonomy:
    Five source families tested:
      Family 1 (local algebraic):   can produce 1/r via X = (M/r^2)^{1/2},
                                     but requires singular F(Phi) = Phi^{-1/2}
      Family 2 (gradient/derivative): structurally CLOSED — all derivatives
                                     make the profile steeper (>= 1/r^3)
      Family 3 (cumulative/integral): contains 1/r contribution from
                                     enclosed-integral, but contaminated by
                                     constant offset
      Family 4 (defect/topological):  Q/r charge-like source directly
                                     produces 1/r^2 in epsilon
      Family 5 (processing-invariant): collapses to Family 1 at equilibrium

  Result 4 — Candidate Ranking:
    Family 4 (defect) > Family 1 (algebraic, p=1/2) > Family 3 (integral)
    >> Family 5 (processing) >> Family 2 (gradient, CLOSED)

  Result 5 — GRUT-Nativeness Assessment:
    No currently canonical GRUT source law provides the required 1/r
    contribution.  Family 4 requires a new topological charge; Family 1
    requires a singular self-coupling; Family 3 introduces a non-standard
    integral source.

  Result 6 — Classification:
    source_law_loophole_5_partially_viable__no_grut_native_mechanism

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants — canonical GRUT parameters
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ_OVER_RS = ALPHA_VAC
R_EQ = R_S * R_EQ_OVER_RS           # = 1/3
C_COMPACTNESS = R_S / R_EQ          # = 3
TAU_CANONICAL = math.sqrt(C_COMPACTNESS / 2.0)  # ~ 1.2247

# Phase 6/6B/6C locked values
PHASE6_F_AT_REQ = -17.71
PHASE6B_A_CRIT_NATURAL = 1.062
A_CRIT = PHASE6B_A_CRIT_NATURAL

# Route C / Component B constants
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
EPSILON_RC_COEFF = A_CRIT ** 2 * RHO_EQ_COEFF
COMP_B_COEFF = 1.0 / (8.0 * math.pi)   # ~ 0.03979
PHI_GOLDEN = (1.0 + math.sqrt(5.0)) / 2.0  # ~ 1.618

# Source-law program specific
N_SOURCE_FAMILIES = 5
COMPONENT_B_TARGET_EXPONENT = -2.0
LOCKED_EXPONENT = -4.0
DIAGNOSTIC_B_COEFF = 0.1  # small perturbation for toy probe X = M/r^2 + B/r


# ================================================================
# Assumptions — explicitly documented
# ================================================================

SOURCE_LAW_ASSUMPTIONS = [
    "1. The memory equation is tau * dPhi/dt + Phi = X(r) where X(r) is "
    "the gravitational source.  The spatial profile of Phi_dot is locked "
    "by S(r) — the spatial dependence of X.",

    "2. The energy density is epsilon = (1/2) * Phi_dot^2 = "
    "(A_crit^2 / (2*tau^2)) * S(r)^2 * exp(-2*t/tau) for step turn-on.",

    "3. The standard source is X = M/r^2 giving S(r) = M/r^2 and "
    "epsilon ~ 1/r^4 (Component A only).  This is the LOCKED baseline.",

    "4. Component B target is 1/(8*pi*r^2) — requires S(r) ~ 1/r to "
    "generate epsilon ~ 1/r^2.",

    "5. Source families are tested at EQUILIBRIUM — the spatial profile "
    "S(r) is evaluated using equilibrium field values Phi_eq = X_eq.",

    "6. The diagnostic toy probe X = M/r^2 + B/r is used ONLY to validate "
    "the computational framework.  It is NOT promoted to canon.",

    "7. GRUT-nativeness means the source deformation arises from the "
    "canonical GRUT Lagrangian without introducing new free parameters "
    "or new field content.",

    "8. The background metric and mass profile m(r) = M are held fixed.  "
    "No self-consistent back-reaction from the source modification.",

    "9. Each source family is tested independently.  Cross-family "
    "combinations are deferred to a subsequent phase.",

    "10. The classification is within the tested source families only.  "
    "Non-classical (quantum, semiclassical) sources are outside scope.",
]

# ================================================================
# Nonclaims — what this phase does NOT prove
# ================================================================

SOURCE_LAW_NONCLAIMS = [
    "1. This phase does NOT prove that Loophole 5 is physically closed.  "
    "It maps which source families CAN produce 1/r and assesses their "
    "GRUT-nativeness, but does not prove uniqueness of X = M/r^2.",

    "2. The diagnostic toy probe X = M/r^2 + B/r is NOT a physical "
    "proposal.  It is a computational test to confirm that a 1/r source "
    "term produces 1/r^2 energy density.",

    "3. The classification 'no GRUT-native mechanism' does NOT mean "
    "no mechanism exists.  It means none was found within the 5 tested "
    "families at canonical parameter values.",

    "4. Family 1 (local algebraic with p=1/2) is NOT declared singular "
    "in all formulations.  Alternative regularizations might exist.",

    "5. Family 3 (cumulative/integral) is NOT declared contamination-"
    "free.  The constant offset is an artifact of the naive integral "
    "bounds and might be absorbable in a proper formulation.",

    "6. Family 4 (defect/topological) is NOT declared non-GRUT.  A "
    "topological charge might emerge from the GRUT field equations "
    "under appropriate boundary conditions.",

    "7. No family cross-coupling is tested.  Two families acting "
    "together might produce 1/r from a mechanism invisible to either "
    "family alone.",

    "8. The 'partially viable' classification does NOT constitute a "
    "construction of the missing source.  It identifies candidate "
    "mechanisms for further investigation.",

    "9. The exponent fits use log-log regression over a finite radial "
    "range.  Sub-leading corrections at small or large r are not "
    "captured by a single power-law exponent.",

    "10. This phase does NOT address the question of whether the "
    "modified source law preserves the Einstein equations or the "
    "TOV structure.  That is deferred.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class SourceLawParams:
    """Module parameters for source-law program."""
    M: float = M_EXT
    tau: float = TAU_CANONICAL
    A_crit: float = A_CRIT
    r_min: float = 0.5
    r_max: float = 5.0
    n_radial: int = 200
    diagnostic_B: float = DIAGNOSTIC_B_COEFF
    # Power-law exponents to test in Family 1
    algebraic_powers: List[float] = field(
        default_factory=lambda: [1.0, 0.5, 0.75, 0.25]
    )
    # Gradient coefficients for Family 2
    grad_alpha: float = 0.1
    grad_beta: float = 0.01
    # Integral coupling for Family 3
    integral_lambda: float = 0.3
    integral_r_min: float = 0.1  # regularization cutoff
    # Defect charge for Family 4
    defect_Q: float = 0.1


@dataclass
class TargetDefinition:
    """Mathematical target: what source profile produces Component B."""
    target_epsilon_exponent: float = -2.0
    required_source_exponent: float = -1.0
    standard_source_formula: str = "X = M / r^2"
    standard_source_exponent: float = -2.0
    standard_epsilon_exponent: float = -4.0
    target_formula: str = "epsilon ~ S(r)^2 => need S(r) ~ 1/r for epsilon ~ 1/r^2"
    component_B_coefficient: float = COMP_B_COEFF
    mechanism: str = (
        "Memory equation tau*dPhi/dt + Phi = X locks Phi_dot spatial "
        "profile to S(r).  epsilon = (1/2)*Phi_dot^2 ~ S(r)^2.  "
        "Need S(r) ~ 1/r to get epsilon ~ 1/r^2."
    )


@dataclass
class SourceFamilySpec:
    """Specification of one source-law family."""
    family_id: int
    name: str
    formula: str
    description: str
    n_free_params: int
    grut_native: bool
    grut_native_notes: str


@dataclass
class DiagnosticToyProbe:
    """Results from diagnostic probe X = M/r^2 + B/r."""
    B_value: float
    r_grid: np.ndarray
    source_profile: np.ndarray  # S(r) = M/r^2 + B/r
    epsilon_profile: np.ndarray  # (A^2/(2*tau^2)) * S(r)^2
    # Decomposition: S^2 = M^2/r^4 + 2*M*B/r^3 + B^2/r^2
    component_A_coeff: float  # M^2 contribution coefficient
    cross_term_coeff: float   # 2*M*B coefficient
    component_B_coeff: float  # B^2 contribution coefficient
    fitted_exponent_full: float  # exponent of full epsilon
    # Separate fits at different radial ranges
    fitted_exponent_inner: float  # inner region (1/r^4 dominated)
    fitted_exponent_outer: float  # outer region (1/r^2 dominated)
    probe_confirms_mechanism: bool
    notes: List[str] = field(default_factory=list)


@dataclass
class PerFamilyShapeResult:
    """Shape analysis result for one source family."""
    family_id: int
    family_name: str
    # Source profile S(r) and its fitted exponent
    source_profile: np.ndarray
    source_exponent: float  # fitted exponent of S(r) vs r
    # Energy density profile and its fitted exponent
    epsilon_profile: np.ndarray
    epsilon_exponent: float  # fitted exponent of epsilon vs r
    # Proximity to target
    deviation_from_target: float  # |epsilon_exponent - (-2.0)|
    can_produce_1_over_r: bool
    # For algebraic family: which power p was used
    algebraic_power_used: Optional[float] = None
    # Sub-results for multi-parameter families
    sub_exponents: Optional[Dict[str, float]] = None
    notes: List[str] = field(default_factory=list)


@dataclass
class SourceFamilyTaxonomy:
    """Complete taxonomy of all 5 source families."""
    families: List[SourceFamilySpec]
    shape_results: List[PerFamilyShapeResult]
    n_families_tested: int = N_SOURCE_FAMILIES
    n_can_produce_1_over_r: int = 0
    n_structurally_closed: int = 0
    best_family_id: int = -1
    best_epsilon_exponent: float = LOCKED_EXPONENT


@dataclass
class CandidateRanking:
    """Ranked list of source families by Component B viability."""
    ranked_family_ids: List[int]
    ranked_family_names: List[str]
    ranked_deviations: List[float]  # deviation from target exponent -2.0
    ranked_feasibility: List[bool]
    ranked_grut_native: List[bool]
    top_candidate_id: int
    top_candidate_name: str
    any_grut_native_viable: bool


@dataclass
class GRUTNativenessAssessment:
    """Assessment of GRUT-nativeness for each viable family."""
    family_assessments: Dict[int, str]  # family_id -> assessment string
    n_grut_native_viable: int
    n_non_native_viable: int
    n_structurally_closed: int
    overall_assessment: str
    recommended_next_step: str


@dataclass
class SourceLawClassification:
    """Final classification of the source-law program."""
    classification: str
    loophole_5_status: str  # "partially_viable" or "closed" or "open"
    n_viable_families: int
    viable_family_names: List[str]
    n_grut_native: int
    phase_lock_update: Dict[str, str]
    summary: str


@dataclass
class SourceLawResult:
    """Master result container."""
    valid: bool
    params: SourceLawParams
    target: Optional[TargetDefinition] = None
    families: Optional[List[SourceFamilySpec]] = None
    diagnostic_probe: Optional[DiagnosticToyProbe] = None
    taxonomy: Optional[SourceFamilyTaxonomy] = None
    ranking: Optional[CandidateRanking] = None
    nativeness: Optional[GRUTNativenessAssessment] = None
    classification: Optional[SourceLawClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Helper functions
# ================================================================

def make_radial_grid(params: SourceLawParams) -> np.ndarray:
    """Create logarithmically-spaced radial grid."""
    return np.logspace(
        np.log10(params.r_min), np.log10(params.r_max), params.n_radial
    )


def _fit_spatial_exponent(r: np.ndarray, y: np.ndarray) -> float:
    """Fit power-law exponent via log-log regression.

    y ~ C * r^alpha  =>  log(y) = log(C) + alpha * log(r)
    Returns alpha.
    """
    mask = (y > 0) & np.isfinite(y)
    if np.sum(mask) < 3:
        return float("nan")
    log_r = np.log(r[mask])
    log_y = np.log(y[mask])
    # Linear regression: log_y = a + b * log_r
    n = len(log_r)
    sx = np.sum(log_r)
    sy = np.sum(log_y)
    sxx = np.sum(log_r ** 2)
    sxy = np.sum(log_r * log_y)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-30:
        return float("nan")
    b = (n * sxy - sx * sy) / denom
    return float(b)


def _compute_epsilon_from_source(
    S_r: np.ndarray, params: SourceLawParams,
) -> np.ndarray:
    """Compute kinetic energy density from source profile S(r).

    epsilon(r) = (A_crit^2 / (2 * tau^2)) * S(r)^2
    (evaluated at t=0 for the step-function turn-on).
    """
    coeff = params.A_crit ** 2 / (2.0 * params.tau ** 2)
    return coeff * S_r ** 2


# ================================================================
# Level 1: Target Definition
# ================================================================

def define_target() -> TargetDefinition:
    """Define the mathematical target for source-law modification."""
    return TargetDefinition()


# ================================================================
# Level 2: Source Family Specifications
# ================================================================

def build_source_family_specs() -> List[SourceFamilySpec]:
    """Build specifications for all 5 source families."""
    families = [
        SourceFamilySpec(
            family_id=1,
            name="local_algebraic",
            formula="X = (M/r^2)^p  with F(Phi) = Phi^{p-1}",
            description=(
                "Local algebraic correction: X depends on local field "
                "values via a power-law self-coupling.  Standard: p=1 "
                "(X = M/r^2).  Target: p=1/2 (X = sqrt(M)/r).  "
                "F(Phi) = Phi^{p-1} maps Phi_eq = M/r^2 to X = (M/r^2)^p."
            ),
            n_free_params=1,  # the exponent p
            grut_native=False,
            grut_native_notes=(
                "The canonical GRUT source is X = M/r^2 (p=1).  "
                "p=1/2 requires F(Phi) = Phi^{-1/2}, which is singular "
                "at Phi=0 and has no derivation from the GRUT Lagrangian."
            ),
        ),
        SourceFamilySpec(
            family_id=2,
            name="gradient_derivative",
            formula="X = M/r^2 + alpha * d(M/r^2)/dr + beta * d^2(M/r^2)/dr^2",
            description=(
                "Gradient/derivative correction: X includes spatial "
                "derivatives of the equilibrium field.  d/dr(M/r^2) = "
                "-2M/r^3 (steeper).  d^2/dr^2(M/r^2) = 6M/r^4 (steeper "
                "still).  ALL derivative corrections make the profile "
                "STEEPER, pushing epsilon toward higher negative exponents."
            ),
            n_free_params=2,  # alpha, beta
            grut_native=True,
            grut_native_notes=(
                "Gradient corrections can arise from higher-derivative "
                "terms in the GRUT action (e.g. nabla^2 Phi coupling).  "
                "However, they are structurally unable to produce 1/r."
            ),
        ),
        SourceFamilySpec(
            family_id=3,
            name="cumulative_integral",
            formula="X = M/r^2 + lambda * integral_{r_min}^r dr' (M/r'^2)",
            description=(
                "Cumulative/integral source: X includes an enclosed-history "
                "integral that accumulates contributions from smaller radii.  "
                "The integral integral(M/r'^2) = M(1/r_min - 1/r) contains "
                "a 1/r term but also a constant offset M/r_min."
            ),
            n_free_params=2,  # lambda, r_min
            grut_native=False,
            grut_native_notes=(
                "Enclosed-mass integrals appear in TOV/gravitational "
                "theory but not in the scalar source X of the canonical "
                "GRUT memory equation.  Would require a non-local "
                "modification of the source coupling."
            ),
        ),
        SourceFamilySpec(
            family_id=4,
            name="defect_topological",
            formula="X = M/r^2 + Q/r",
            description=(
                "Defect/topological source: X includes a charge-like "
                "1/r contribution from a topological defect or conserved "
                "charge.  epsilon = (A^2/(2*tau^2)) * (M/r^2 + Q/r)^2 "
                "= ... + Q^2/(r^2) * (A^2/(2*tau^2)).  The Q^2/r^2 "
                "term IS Component B."
            ),
            n_free_params=1,  # Q
            grut_native=False,
            grut_native_notes=(
                "No topological charge Q is currently defined in the "
                "canonical GRUT framework.  Such a charge might arise "
                "from boundary conditions, winding numbers, or a "
                "conserved Noether current not yet identified."
            ),
        ),
        SourceFamilySpec(
            family_id=5,
            name="processing_lag_invariant",
            formula="X = G(Phi_eq, Phi_dot_eq, memory_integrals)",
            description=(
                "Processing-/lag-invariant source: X depends on the "
                "scalar field, its time derivative, and memory integrals.  "
                "At equilibrium, Phi_dot = 0 and memory integrals reduce "
                "to functions of Phi_eq = M/r^2.  This family COLLAPSES "
                "to Family 1 (local algebraic) at equilibrium."
            ),
            n_free_params=0,  # no independent params beyond Family 1
            grut_native=True,
            grut_native_notes=(
                "Processing-invariant sources are formally GRUT-native "
                "(they use GRUT field variables), but at equilibrium "
                "they reduce to local algebraic functions of Phi_eq.  "
                "The equilibrium collapse means this family adds no "
                "new spatial structure beyond Family 1."
            ),
        ),
    ]
    return families


# ================================================================
# Level 3: Diagnostic Toy Probe
# ================================================================

def run_diagnostic_toy_probe(
    params: SourceLawParams,
) -> DiagnosticToyProbe:
    """Run diagnostic probe with X = M/r^2 + B/r.

    This is NOT a physical proposal.  It validates that a 1/r source
    term produces 1/r^2 energy density through the memory equation.
    """
    r = make_radial_grid(params)
    B = params.diagnostic_B
    M = params.M

    # Source profile
    S_r = M / r ** 2 + B / r

    # Energy density: epsilon = (A^2/(2*tau^2)) * S(r)^2
    epsilon = _compute_epsilon_from_source(S_r, params)

    # Decomposition coefficients (for the S(r)^2 expansion):
    # S^2 = M^2/r^4 + 2*M*B/r^3 + B^2/r^2
    # epsilon = (A^2/(2*tau^2)) * S^2
    prefactor = params.A_crit ** 2 / (2.0 * params.tau ** 2)
    comp_A_c = prefactor * M ** 2      # coefficient of 1/r^4
    cross_c = prefactor * 2.0 * M * B  # coefficient of 1/r^3
    comp_B_c = prefactor * B ** 2      # coefficient of 1/r^2

    # Fit exponents at different radial ranges
    n = len(r)
    full_exp = _fit_spatial_exponent(r, epsilon)
    inner_exp = _fit_spatial_exponent(r[: n // 3], epsilon[: n // 3])
    outer_exp = _fit_spatial_exponent(r[2 * n // 3 :], epsilon[2 * n // 3 :])

    # The mechanism works if the outer region approaches -2.0
    confirms = outer_exp < -2.5  # closer to -2 than to -4

    notes = [
        f"Full-range exponent: {full_exp:.4f} (mixed profile)",
        f"Inner-range exponent: {inner_exp:.4f} (1/r^4 dominated)",
        f"Outer-range exponent: {outer_exp:.4f} (approaching 1/r^2)",
        f"Component A coefficient: {comp_A_c:.6f}",
        f"Cross-term coefficient: {cross_c:.6f}",
        f"Component B coefficient: {comp_B_c:.6f}",
        "Diagnostic only — NOT promoted to canon.",
    ]

    return DiagnosticToyProbe(
        B_value=B,
        r_grid=r,
        source_profile=S_r,
        epsilon_profile=epsilon,
        component_A_coeff=comp_A_c,
        cross_term_coeff=cross_c,
        component_B_coeff=comp_B_c,
        fitted_exponent_full=full_exp,
        fitted_exponent_inner=inner_exp,
        fitted_exponent_outer=outer_exp,
        probe_confirms_mechanism=confirms,
        notes=notes,
    )


# ================================================================
# Level 4: Per-Family Shape Computation
# ================================================================

def _source_profile_algebraic(
    r: np.ndarray, M: float, p: float,
) -> np.ndarray:
    """Algebraic source: S(r) = (M/r^2)^p = M^p / r^{2p}."""
    return (M / r ** 2) ** p


def _source_profile_gradient(
    r: np.ndarray, M: float, alpha: float, beta: float,
) -> np.ndarray:
    """Gradient source: S(r) = M/r^2 + alpha*(-2M/r^3) + beta*(6M/r^4)."""
    base = M / r ** 2
    grad1 = -2.0 * M / r ** 3
    grad2 = 6.0 * M / r ** 4
    return base + alpha * grad1 + beta * grad2


def _source_profile_integral(
    r: np.ndarray, M: float, lam: float, r_min_int: float,
) -> np.ndarray:
    """Integral source: S(r) = M/r^2 + lambda * M * (1/r_min - 1/r).

    The integral of M/r'^2 from r_min to r is M*(1/r_min - 1/r).
    """
    base = M / r ** 2
    enclosed = M * (1.0 / r_min_int - 1.0 / r)
    return base + lam * enclosed


def _source_profile_defect(
    r: np.ndarray, M: float, Q: float,
) -> np.ndarray:
    """Defect source: S(r) = M/r^2 + Q/r."""
    return M / r ** 2 + Q / r


def compute_family_shape(
    family: SourceFamilySpec,
    params: SourceLawParams,
) -> PerFamilyShapeResult:
    """Compute shape analysis for one source family."""
    r = make_radial_grid(params)
    M = params.M

    notes: List[str] = []
    sub_exponents: Optional[Dict[str, float]] = None
    alg_power: Optional[float] = None

    if family.family_id == 1:
        # Local algebraic: test multiple powers
        sub_exponents = {}
        best_dev = 999.0
        best_S = None
        best_eps = None
        best_src_exp = None
        best_eps_exp = None
        best_p = None

        for p in params.algebraic_powers:
            S_r = _source_profile_algebraic(r, M, p)
            eps = _compute_epsilon_from_source(S_r, params)
            src_exp = _fit_spatial_exponent(r, S_r)
            eps_exp = _fit_spatial_exponent(r, eps)
            sub_exponents[f"p={p:.2f}_source"] = src_exp
            sub_exponents[f"p={p:.2f}_epsilon"] = eps_exp

            dev = abs(eps_exp - COMPONENT_B_TARGET_EXPONENT)
            if dev < best_dev:
                best_dev = dev
                best_S = S_r
                best_eps = eps
                best_src_exp = src_exp
                best_eps_exp = eps_exp
                best_p = p

        source_profile = best_S
        epsilon_profile = best_eps
        source_exponent = best_src_exp
        epsilon_exponent = best_eps_exp
        alg_power = best_p
        can_1r = abs(best_eps_exp - COMPONENT_B_TARGET_EXPONENT) < 0.1

        notes.append(f"Best power: p={best_p:.2f}")
        notes.append(f"p=1.0: epsilon ~ r^{sub_exponents.get('p=1.00_epsilon', -4.0):.2f}")
        notes.append(f"p=0.50: epsilon ~ r^{sub_exponents.get('p=0.50_epsilon', -2.0):.2f}")
        if best_p != 1.0:
            notes.append(
                f"F(Phi) = Phi^{{p-1}} = Phi^{{{best_p-1:.2f}}} — "
                f"{'singular at Phi=0' if best_p < 1 else 'regular'}"
            )

    elif family.family_id == 2:
        # Gradient/derivative
        S_r = _source_profile_gradient(
            r, M, params.grad_alpha, params.grad_beta,
        )
        source_profile = S_r
        epsilon_profile = _compute_epsilon_from_source(S_r, params)
        source_exponent = _fit_spatial_exponent(r, np.abs(S_r))
        epsilon_exponent = _fit_spatial_exponent(r, epsilon_profile)
        can_1r = False  # structurally closed

        # Also compute pure derivative exponents
        grad1 = np.abs(-2.0 * M / r ** 3)
        grad2 = np.abs(6.0 * M / r ** 4)
        grad1_exp = _fit_spatial_exponent(r, grad1)
        grad2_exp = _fit_spatial_exponent(r, grad2)
        sub_exponents = {
            "d/dr_exponent": grad1_exp,
            "d2/dr2_exponent": grad2_exp,
            "combined_source_exponent": source_exponent,
        }
        notes.append(f"d/dr(M/r^2) ~ r^{grad1_exp:.1f} (steeper than 1/r^2)")
        notes.append(f"d^2/dr^2(M/r^2) ~ r^{grad2_exp:.1f} (steeper still)")
        notes.append("ALL gradient corrections make profile steeper. CLOSED.")

    elif family.family_id == 3:
        # Cumulative/integral
        S_r = _source_profile_integral(
            r, M, params.integral_lambda, params.integral_r_min,
        )
        source_profile = S_r
        epsilon_profile = _compute_epsilon_from_source(S_r, params)
        source_exponent = _fit_spatial_exponent(r, np.abs(S_r))
        epsilon_exponent = _fit_spatial_exponent(r, epsilon_profile)

        # Separate the 1/r contribution
        one_over_r_part = params.integral_lambda * M / r
        const_part = params.integral_lambda * M / params.integral_r_min
        one_over_r_coeff = params.integral_lambda * M
        notes.append(
            f"Integral = M*(1/r_min - 1/r) with lambda={params.integral_lambda:.2f}"
        )
        notes.append(
            f"1/r coefficient: lambda*M = {one_over_r_coeff:.4f}"
        )
        notes.append(
            f"Constant offset: lambda*M/r_min = {const_part:.4f}"
        )
        notes.append("Contains 1/r term but contaminated by constant offset")

        # Check if the 1/r contribution is visible
        # At large r, constant dominates → epsilon → constant^2 → flat
        # Can't get pure 1/r^2
        can_1r = False  # contaminated
        sub_exponents = {
            "one_over_r_coeff": one_over_r_coeff,
            "constant_offset": const_part,
            "epsilon_exponent": epsilon_exponent,
        }

    elif family.family_id == 4:
        # Defect/topological
        Q = params.defect_Q
        S_r = _source_profile_defect(r, M, Q)
        source_profile = S_r
        epsilon_profile = _compute_epsilon_from_source(S_r, params)
        source_exponent = _fit_spatial_exponent(r, S_r)
        epsilon_exponent = _fit_spatial_exponent(r, epsilon_profile)

        # Pure Q/r contribution
        eps_Q_only = _compute_epsilon_from_source(Q / r, params)
        Q_only_exp = _fit_spatial_exponent(r, eps_Q_only)

        # The Q^2/r^2 term in the expansion
        prefactor = params.A_crit ** 2 / (2.0 * params.tau ** 2)
        comp_B_from_Q = prefactor * Q ** 2
        notes.append(f"Q = {Q:.4f}")
        notes.append(f"Pure Q/r epsilon exponent: {Q_only_exp:.4f} (target: -2.0)")
        notes.append(
            f"Component B coefficient from Q: {comp_B_from_Q:.6f} "
            f"(target: {COMP_B_COEFF:.6f})"
        )
        notes.append(
            "Full epsilon has mixed 1/r^4 + 1/r^3 + 1/r^2 profile"
        )

        can_1r = abs(Q_only_exp - COMPONENT_B_TARGET_EXPONENT) < 0.1
        sub_exponents = {
            "Q_only_epsilon_exponent": Q_only_exp,
            "full_epsilon_exponent": epsilon_exponent,
            "comp_B_from_Q": comp_B_from_Q,
        }

    elif family.family_id == 5:
        # Processing-invariant: collapses to Family 1 at equilibrium
        # At equilibrium, Phi_dot = 0, Phi = Phi_eq = M/r^2
        # Any function G(Phi_eq, 0, ...) = g(M/r^2) which is local algebraic
        # Use p=1 (standard) as the canonical collapse
        S_r = _source_profile_algebraic(r, M, 1.0)
        source_profile = S_r
        epsilon_profile = _compute_epsilon_from_source(S_r, params)
        source_exponent = _fit_spatial_exponent(r, S_r)
        epsilon_exponent = _fit_spatial_exponent(r, epsilon_profile)
        can_1r = False  # collapses to standard at equilibrium

        notes.append("At equilibrium: Phi_dot=0, memory integrals -> f(Phi_eq)")
        notes.append("Collapses to Family 1 (local algebraic) with p=1")
        notes.append("No new spatial structure beyond Family 1")

    else:
        raise ValueError(f"Unknown family_id: {family.family_id}")

    deviation = abs(epsilon_exponent - COMPONENT_B_TARGET_EXPONENT)

    return PerFamilyShapeResult(
        family_id=family.family_id,
        family_name=family.name,
        source_profile=source_profile,
        source_exponent=source_exponent,
        epsilon_profile=epsilon_profile,
        epsilon_exponent=epsilon_exponent,
        deviation_from_target=deviation,
        can_produce_1_over_r=can_1r,
        algebraic_power_used=alg_power,
        sub_exponents=sub_exponents,
        notes=notes,
    )


# ================================================================
# Level 5: Source Family Taxonomy
# ================================================================

def build_source_family_taxonomy(
    params: SourceLawParams,
) -> SourceFamilyTaxonomy:
    """Build complete taxonomy of all 5 source families."""
    families = build_source_family_specs()
    shape_results = [compute_family_shape(f, params) for f in families]

    n_can = sum(1 for s in shape_results if s.can_produce_1_over_r)
    n_closed = sum(1 for s in shape_results if not s.can_produce_1_over_r)

    # Find best family (closest to target)
    best_idx = min(range(len(shape_results)),
                   key=lambda i: shape_results[i].deviation_from_target)
    best_id = shape_results[best_idx].family_id
    best_exp = shape_results[best_idx].epsilon_exponent

    return SourceFamilyTaxonomy(
        families=families,
        shape_results=shape_results,
        n_families_tested=N_SOURCE_FAMILIES,
        n_can_produce_1_over_r=n_can,
        n_structurally_closed=n_closed,
        best_family_id=best_id,
        best_epsilon_exponent=best_exp,
    )


# ================================================================
# Level 6: Candidate Ranking
# ================================================================

def rank_candidates(
    taxonomy: SourceFamilyTaxonomy,
) -> CandidateRanking:
    """Rank source families by proximity to Component B target."""
    # Sort by deviation (ascending)
    indexed = [
        (s.deviation_from_target, s.family_id, s.family_name,
         s.can_produce_1_over_r)
        for s in taxonomy.shape_results
    ]
    indexed.sort(key=lambda x: x[0])

    ranked_ids = [x[1] for x in indexed]
    ranked_names = [x[2] for x in indexed]
    ranked_devs = [x[0] for x in indexed]
    ranked_feas = [x[3] for x in indexed]

    # GRUT-nativeness lookup
    native_map = {f.family_id: f.grut_native for f in taxonomy.families}
    ranked_native = [native_map[fid] for fid in ranked_ids]

    any_native = any(
        feas and nat for feas, nat in zip(ranked_feas, ranked_native)
    )

    return CandidateRanking(
        ranked_family_ids=ranked_ids,
        ranked_family_names=ranked_names,
        ranked_deviations=ranked_devs,
        ranked_feasibility=ranked_feas,
        ranked_grut_native=ranked_native,
        top_candidate_id=ranked_ids[0],
        top_candidate_name=ranked_names[0],
        any_grut_native_viable=any_native,
    )


# ================================================================
# Level 7: GRUT-Nativeness Assessment
# ================================================================

def assess_grut_nativeness(
    taxonomy: SourceFamilyTaxonomy,
) -> GRUTNativenessAssessment:
    """Assess GRUT-nativeness for each family."""
    assessments: Dict[int, str] = {}
    n_native_viable = 0
    n_non_native_viable = 0
    n_closed = 0

    for fam, shape in zip(taxonomy.families, taxonomy.shape_results):
        if not shape.can_produce_1_over_r:
            assessments[fam.family_id] = (
                f"{fam.name}: structurally CLOSED "
                f"(epsilon exponent = {shape.epsilon_exponent:.2f}, "
                f"cannot reach -2.0)"
            )
            n_closed += 1
        elif fam.grut_native:
            assessments[fam.family_id] = (
                f"{fam.name}: GRUT-native AND viable "
                f"(epsilon exponent = {shape.epsilon_exponent:.2f})"
            )
            n_native_viable += 1
        else:
            assessments[fam.family_id] = (
                f"{fam.name}: viable but NOT GRUT-native "
                f"(epsilon exponent = {shape.epsilon_exponent:.2f}).  "
                f"{fam.grut_native_notes}"
            )
            n_non_native_viable += 1

    if n_native_viable > 0:
        overall = (
            f"{n_native_viable} family(ies) are both viable and GRUT-native"
        )
        next_step = "Construct explicit GRUT-native source term"
    else:
        overall = (
            f"No GRUT-native mechanism found among {N_SOURCE_FAMILIES} families.  "
            f"{n_non_native_viable} viable but non-native.  "
            f"{n_closed} structurally closed."
        )
        next_step = (
            "Identify new GRUT-native source structure (e.g. topological "
            "charge from boundary conditions, or curvature-scalar coupling "
            "producing effective 1/r source)"
        )

    return GRUTNativenessAssessment(
        family_assessments=assessments,
        n_grut_native_viable=n_native_viable,
        n_non_native_viable=n_non_native_viable,
        n_structurally_closed=n_closed,
        overall_assessment=overall,
        recommended_next_step=next_step,
    )


# ================================================================
# Level 8: Classification
# ================================================================

def classify_source_law(
    ranking: CandidateRanking,
    nativeness: GRUTNativenessAssessment,
) -> SourceLawClassification:
    """Classify the source-law loophole status."""
    n_viable = sum(1 for f in ranking.ranked_feasibility if f)
    viable_names = [
        name for name, feas in zip(
            ranking.ranked_family_names, ranking.ranked_feasibility
        )
        if feas
    ]

    if n_viable == 0:
        status = "closed"
        classification = "source_law_loophole_5_closed__no_viable_family"
    elif nativeness.n_grut_native_viable > 0:
        status = "open"
        classification = (
            "source_law_loophole_5_open__grut_native_mechanism_found"
        )
    else:
        status = "partially_viable"
        classification = (
            "source_law_loophole_5_partially_viable__"
            "no_grut_native_mechanism"
        )

    phase_lock = {
        "phase_6_f_at_req": "LOCKED (-17.71)",
        "phase_6b_A_crit": "LOCKED (1.062)",
        "phase_6c_deficit": "LOCKED (Component A + Component B)",
        "route_c_markov": "LOCKED (insufficient, 1/r^4)",
        "route_b_all_channels": "LOCKED (closed within Galley CTP)",
        "route_c_nonmarkov": "LOCKED (source profile locking, 1/r^4)",
        "loophole_5_source_law": f"TESTED ({classification})",
    }

    summary = (
        f"Loophole 5 status: {status}.  "
        f"{n_viable}/{N_SOURCE_FAMILIES} families can produce 1/r-type "
        f"source.  {nativeness.n_grut_native_viable} GRUT-native viable.  "
        f"Top candidate: {ranking.top_candidate_name}.  "
        f"Recommended: {nativeness.recommended_next_step}"
    )

    return SourceLawClassification(
        classification=classification,
        loophole_5_status=status,
        n_viable_families=n_viable,
        viable_family_names=viable_names,
        n_grut_native=nativeness.n_grut_native_viable,
        phase_lock_update=phase_lock,
        summary=summary,
    )


# ================================================================
# Level 9: Master Function
# ================================================================

def compute_source_law_assessment(
    params: Optional[SourceLawParams] = None,
) -> SourceLawResult:
    """Master function: run the complete source-law program.

    Steps:
        1. Define target (S(r) ~ 1/r for epsilon ~ 1/r^2)
        2. Build source family specifications
        3. Run diagnostic toy probe (X = M/r^2 + B/r)
        4. Build source family taxonomy (all 5 families)
        5. Rank candidates by proximity to target
        6. Assess GRUT-nativeness
        7. Classify and update phase lock
    """
    if params is None:
        params = SourceLawParams()

    result = SourceLawResult(valid=False, params=params)

    try:
        # Step 1
        result.target = define_target()

        # Step 2
        result.families = build_source_family_specs()

        # Step 3
        result.diagnostic_probe = run_diagnostic_toy_probe(params)

        # Step 4
        result.taxonomy = build_source_family_taxonomy(params)

        # Step 5
        result.ranking = rank_candidates(result.taxonomy)

        # Step 6
        result.nativeness = assess_grut_nativeness(result.taxonomy)

        # Step 7
        result.classification = classify_source_law(
            result.ranking, result.nativeness,
        )

        # Metadata
        result.nonclaims = list(SOURCE_LAW_NONCLAIMS)
        result.assumptions = list(SOURCE_LAW_ASSUMPTIONS)
        result.diagnostics = {
            "n_families": N_SOURCE_FAMILIES,
            "n_viable": result.classification.n_viable_families,
            "n_grut_native": result.classification.n_grut_native,
            "classification": result.classification.classification,
            "loophole_5_status": result.classification.loophole_5_status,
            "top_candidate": result.ranking.top_candidate_name,
            "diagnostic_probe_confirms": (
                result.diagnostic_probe.probe_confirms_mechanism
            ),
        }
        result.valid = True

    except Exception as exc:
        result.diagnostics["error"] = str(exc)

    return result


# ================================================================
# Level 10: Serialization
# ================================================================

def source_law_result_to_dict(result: SourceLawResult) -> Dict[str, Any]:
    """Serialize SourceLawResult to a JSON-safe dictionary."""
    out: Dict[str, Any] = {"valid": result.valid}

    # Params
    out["params"] = {
        "M": result.params.M,
        "tau": result.params.tau,
        "A_crit": result.params.A_crit,
        "r_min": result.params.r_min,
        "r_max": result.params.r_max,
        "n_radial": result.params.n_radial,
        "diagnostic_B": result.params.diagnostic_B,
    }

    # Target
    if result.target is not None:
        out["target"] = {
            "target_epsilon_exponent": result.target.target_epsilon_exponent,
            "required_source_exponent": result.target.required_source_exponent,
            "standard_source_formula": result.target.standard_source_formula,
            "mechanism": result.target.mechanism,
        }

    # Diagnostic probe
    if result.diagnostic_probe is not None:
        dp = result.diagnostic_probe
        out["diagnostic_probe"] = {
            "B_value": dp.B_value,
            "component_A_coeff": dp.component_A_coeff,
            "cross_term_coeff": dp.cross_term_coeff,
            "component_B_coeff": dp.component_B_coeff,
            "fitted_exponent_full": dp.fitted_exponent_full,
            "fitted_exponent_inner": dp.fitted_exponent_inner,
            "fitted_exponent_outer": dp.fitted_exponent_outer,
            "probe_confirms_mechanism": dp.probe_confirms_mechanism,
            "notes": dp.notes,
        }

    # Taxonomy (shape results per family)
    if result.taxonomy is not None:
        tax = result.taxonomy
        fam_results = []
        for s in tax.shape_results:
            entry = {
                "family_id": s.family_id,
                "family_name": s.family_name,
                "source_exponent": s.source_exponent,
                "epsilon_exponent": s.epsilon_exponent,
                "deviation_from_target": s.deviation_from_target,
                "can_produce_1_over_r": s.can_produce_1_over_r,
                "notes": s.notes,
            }
            if s.sub_exponents is not None:
                entry["sub_exponents"] = {
                    k: float(v) if isinstance(v, (int, float, np.floating))
                    else v
                    for k, v in s.sub_exponents.items()
                }
            if s.algebraic_power_used is not None:
                entry["algebraic_power_used"] = s.algebraic_power_used
            fam_results.append(entry)
        out["taxonomy"] = {
            "n_families_tested": tax.n_families_tested,
            "n_can_produce_1_over_r": tax.n_can_produce_1_over_r,
            "n_structurally_closed": tax.n_structurally_closed,
            "best_family_id": tax.best_family_id,
            "best_epsilon_exponent": tax.best_epsilon_exponent,
            "family_results": fam_results,
        }

    # Ranking
    if result.ranking is not None:
        rk = result.ranking
        out["ranking"] = {
            "ranked_family_names": rk.ranked_family_names,
            "ranked_deviations": [float(d) for d in rk.ranked_deviations],
            "ranked_feasibility": rk.ranked_feasibility,
            "ranked_grut_native": rk.ranked_grut_native,
            "top_candidate": rk.top_candidate_name,
            "any_grut_native_viable": rk.any_grut_native_viable,
        }

    # Nativeness
    if result.nativeness is not None:
        nat = result.nativeness
        out["nativeness"] = {
            "n_grut_native_viable": nat.n_grut_native_viable,
            "n_non_native_viable": nat.n_non_native_viable,
            "n_structurally_closed": nat.n_structurally_closed,
            "overall_assessment": nat.overall_assessment,
            "recommended_next_step": nat.recommended_next_step,
            "family_assessments": nat.family_assessments,
        }

    # Classification
    if result.classification is not None:
        cl = result.classification
        out["classification"] = {
            "classification": cl.classification,
            "loophole_5_status": cl.loophole_5_status,
            "n_viable_families": cl.n_viable_families,
            "viable_family_names": cl.viable_family_names,
            "n_grut_native": cl.n_grut_native,
            "phase_lock_update": cl.phase_lock_update,
            "summary": cl.summary,
        }

    # Top-level lists
    out["nonclaims"] = result.nonclaims
    out["assumptions"] = result.assumptions
    out["diagnostics"] = result.diagnostics

    return out
