"""Route C (nonlocal metric back-reaction) deficit assessment.

Tests whether Route C — the nonlocal retarded action parent for the
memory sector — can generate the missing 1/r^2 support identified
in Phase 6C.  Route C uses kernel K(s) = (1/tau)exp(-s/tau)Theta(s),
whose Markov property reduces the nonlocal stress-functional to a
local auxiliary scalar field.

PRINCIPAL RESULTS:

  Result 1 — Route C Effective Energy Density:
    The Markov reduction gives T^Phi as a standard minimally-coupled scalar.
    The kinetic energy density is epsilon_RC(r) = (1/2)(Phi_dot)^2 where
    Phi_dot = A_crit * M / (tau * r^2).  At A_crit = 1.062 this gives
    epsilon_RC ~ 0.0940/r^4 — PURE 1/r^4, no 1/r^2 component.

  Result 2 — Deficit Ratio Profile:
    The ratio epsilon_RC / epsilon_min ranges from ~1.07 at R_eq
    (where Component A dominates) to ~0.76 at r=1 (where Component B
    dominates).  Route C overcovers the core while undercovering
    intermediate radii — a shape mismatch, not an amplitude problem.

  Result 3 — Four Insufficiency Chains:
    Chain 1: Markov reduction forecloses independent 1/r^2 from kinetics
    Chain 2: Self-healing eliminates lapse correction at equilibrium
    Chain 3: Candidate potential (inherited quadratic ansatz) gives 1/r^4
    Chain 4: Spatial gradient in current reduced background gives 1/r^6

  Result 4 — Loophole Catalog:
    Five loopholes documented with severity assessment.  Each represents
    a pathway that could bypass the insufficiency but lies outside the
    tested Markov-exponential-kernel regime.

  Result 5 — Provisional Candidate Ranking Update:
    Route C: INSUFFICIENT within Markov reduction (downgraded)
    Route B: PROVISIONAL (different obstruction: ghost mode)

  Result 6 — Classification:
    route_c_insufficient_within_markov_reduction

SELF-CONTAINED: Depends only on math, numpy.  No grut/ cross-imports.
"""

from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


# ================================================================
# Constants — canonical GRUT parameters (from metric_deficit.py)
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
MASS_COEFF = 2.0 * math.pi * M_EXT ** 2 / (TAU_CANONICAL ** 2)

# Route C specific
A_CRIT = PHASE6B_A_CRIT_NATURAL
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
# epsilon_RC coefficient: (A_crit^2 * M^2) / (2 * tau^2)
EPSILON_RC_COEFF = A_CRIT ** 2 * RHO_EQ_COEFF
# = 1.062^2 * 0.0833 ≈ 0.0940
COMP_B_COEFF = 1.0 / (8.0 * math.pi)   # ≈ 0.03979


# ================================================================
# Assumptions — explicitly documented
# ================================================================

ROUTE_C_ASSUMPTIONS = [
    "1. The Route C stress-energy is evaluated in the Markov-reduced "
    "auxiliary-field representation with exponential kernel K(s) = "
    "(1/tau)exp(-s/tau)Theta(s).  This is the ONLY kernel for which "
    "the Markov property holds.",

    "2. The effective T^Phi_{ab} is the standard minimally-coupled scalar "
    "form: nabla_a Phi nabla_b Phi - g_{ab}[(1/2)(nabla Phi)^2 + V(Phi) "
    "- Phi X/tau].  (From nonlocal_stress.py, the Markov property "
    "absorbs history into current Phi, making T^Phi local.)",

    "3. The equilibrium field profile is Phi_eq = X_eq = M/r^2, sourced "
    "by X = m/r^2.  At equilibrium the memory field tracks its source "
    "(force balance).",

    "4. The deficit is evaluated at static equilibrium, where the metric "
    "deficit is defined (Phase 6C).  Transient dynamical effects during "
    "relaxation are cataloged as Loophole 4.",

    "5. The potential V(Phi) = Phi^2/(2*tau^2) is a tested inherited "
    "candidate ansatz from Route A / shared closure.  It is NOT intrinsic "
    "to Route C.  Other potentials are cataloged as part of Loophole 5.",
]


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. The Markov reduction applies ONLY to the exponential kernel "
    "K(s) = (1/tau)exp(-s/tau)Theta(s).  Non-exponential kernels may "
    "produce genuinely nonlocal T^Phi_history that could include 1/r^2 "
    "terms (Loophole 1).",

    "2. The insufficiency is evaluated at STATIC EQUILIBRIUM where the "
    "metric deficit is defined.  Transient dynamical effects during "
    "relaxation are not assessed here (Loophole 4).",

    "3. The classification 'route_c_insufficient_within_markov_reduction' "
    "applies within the tested Markov-exponential-kernel pathway.  It is "
    "NOT a general no-go for Route C.",

    "4. The full covariant metric variation of the nonlocal action has "
    "NOT been computed in closed form (nonlocal_stress.py).  Closed-form "
    "terms could in principle alter the energy density profile (Loophole 2).",

    "5. Nonlinear lapse effects beyond first order in Psi have not been "
    "computed.  The self-healing result is first-order in the lapse "
    "correction analysis (Loophole 3).",

    "6. A modified source X that differs from M/r^2 could produce "
    "Phi_dot ~ 1/r, giving epsilon ~ 1/r^2.  This requires non-standard "
    "sourcing that has not been tested within the GRUT framework "
    "(Loophole 5).",

    "7. The potential V(Phi) = Phi^2/(2*tau^2) is a tested inherited "
    "candidate ansatz from Route A / shared closure.  It is NOT intrinsic "
    "to Route C.  Other potentials could yield different equilibrium "
    "energy density profiles.",

    "8. The spatial-gradient scaling analysis is performed in the current "
    "reduced radial background and is NOT a full covariant gradient-sector "
    "derivation.  Full covariant gradients nabla_a Phi would include "
    "metric factors that modify the radial profile.",

    "9. The provisional ranking update is a classification tool, NOT a "
    "prediction.  Rankings may change with new theoretical input or "
    "computational results.",

    "10. The integrated deficit (radial integral of epsilon_min - epsilon_RC "
    "where positive) depends on grid resolution and integration domain "
    "boundaries.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class RouteCParams:
    """Parameters for the Route C deficit assessment."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S
    R_min: float = 0.05
    n_r: int = 500
    A_crit: float = A_CRIT


@dataclass
class RouteCEnergyProfile:
    """Route C effective energy density compared to epsilon_min."""
    r: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_RC: np.ndarray = field(default_factory=lambda: np.array([]))
    epsilon_min: np.ndarray = field(default_factory=lambda: np.array([]))
    component_A: np.ndarray = field(default_factory=lambda: np.array([]))
    component_B: np.ndarray = field(default_factory=lambda: np.array([]))
    deficit_ratio: np.ndarray = field(default_factory=lambda: np.array([]))
    ratio_at_R_eq: float = 0.0
    ratio_at_r1: float = 0.0
    ratio_min: float = 0.0
    ratio_max: float = 0.0
    epsilon_RC_coeff: float = 0.0
    covers_component_A: bool = False
    covers_component_B: bool = False
    integrated_shortfall: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class InsufficiencyChain:
    """A single insufficiency argument chain."""
    chain_number: int = 0
    chain_name: str = ""
    premise: str = ""
    mechanism: str = ""
    conclusion: str = ""
    scaling_law: str = ""
    provides_1r2: bool = False
    is_formal: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class InsufficiencyAssessment:
    """Aggregate assessment of the four insufficiency chains."""
    chains: List[InsufficiencyChain] = field(default_factory=list)
    n_chains: int = 0
    all_chains_consistent: bool = False
    any_chain_provides_1r2: bool = False
    overall_insufficient: bool = False
    is_general_no_go: bool = False
    classification_string: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class LapseCorrectionAtEquilibrium:
    """Self-healing analysis: lapse correction magnitude at equilibrium."""
    X_eq_at_R_eq: float = 0.0
    Phi_eq_at_R_eq: float = 0.0
    source_X_minus_Phi: float = 0.0
    delta_Phi_lapse: float = 0.0
    self_healing_holds: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class PotentialSectorAnalysis:
    """Analysis of V(Phi) contribution at equilibrium.

    The potential tested here is a candidate inherited ansatz from
    Route A / shared closure, NOT intrinsic to Route C.
    """
    V_form: str = "Phi^2 / (2*tau^2)"
    Phi_eq_scaling: str = "M/r^2"
    V_scaling: str = "M^2/(2*tau^2*r^4) = 1/r^4"
    provides_1r2: bool = False
    V_at_R_eq: float = 0.0
    is_intrinsic_route_c: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class SpatialGradientAnalysis:
    """Analysis of spatial gradient contribution at equilibrium.

    Evaluated in the current reduced radial background, NOT a full
    covariant gradient-sector derivation.
    """
    dPhi_dr_scaling: str = "-2M/r^3"
    gradient_sq_scaling: str = "4M^2/r^6 = 1/r^6"
    provides_1r2: bool = False
    gradient_sq_at_R_eq: float = 0.0
    evaluated_in_reduced_background: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class Loophole:
    """A documented loophole in the insufficiency argument."""
    loophole_number: int = 0
    name: str = ""
    description: str = ""
    mechanism: str = ""
    could_provide_1r2: bool = False
    severity: str = ""
    requires_beyond_markov: bool = False
    requires_beyond_equilibrium: bool = False
    tested_within_module: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class LoopholeCatalog:
    """Catalog of all documented loopholes."""
    loopholes: List[Loophole] = field(default_factory=list)
    n_loopholes: int = 0
    n_high_severity: int = 0
    n_medium_severity: int = 0
    n_low_severity: int = 0
    any_tested: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class ProvisionalCandidateRankingUpdate:
    """Provisional ranking update after Route C assessment.

    This is a classification tool, not a prediction.  Route C is
    downgraded within the tested Markov pathway but remains alive
    through documented loopholes.
    """
    route_c_status: str = ""
    route_c_previous_status: str = ""
    route_c_downgraded: bool = False
    route_b_status: str = ""
    route_b_obstruction: str = ""
    route_a_status: str = ""
    is_provisional: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteCClassification:
    """Final classification of the Route C deficit assessment."""
    classification: str = ""
    route_c_provides_component_A: bool = False
    route_c_provides_component_B: bool = False
    overall_insufficient_within_markov: bool = False
    is_general_no_go: bool = False
    shape_mismatch_description: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteCDeficitResult:
    """Master result for the Route C deficit assessment."""
    valid: bool = False
    params: RouteCParams = field(default_factory=RouteCParams)
    energy_profile: Optional[RouteCEnergyProfile] = None
    insufficiency_assessment: Optional[InsufficiencyAssessment] = None
    lapse_correction: Optional[LapseCorrectionAtEquilibrium] = None
    potential_sector: Optional[PotentialSectorAnalysis] = None
    spatial_gradient: Optional[SpatialGradientAnalysis] = None
    loophole_catalog: Optional[LoopholeCatalog] = None
    provisional_ranking: Optional[ProvisionalCandidateRankingUpdate] = None
    classification: Optional[RouteCClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Radial grid and baseline
# ================================================================

def make_radial_grid(params: RouteCParams) -> np.ndarray:
    """Create log-spaced radial grid from R_ext down to R_min."""
    r_min = max(params.R_min, params.R_eq * 0.8)
    log_r = np.linspace(math.log(params.R_ext), math.log(r_min), params.n_r)
    return np.exp(log_r)


def compute_static_mass(
    r: np.ndarray, params: RouteCParams,
) -> np.ndarray:
    """Compute linearized static mass profile.

    m(r) = M + (2*pi*M^2 / tau^2) * (1/r - 1/R_ext)
    """
    M = params.M
    tau2 = params.tau ** 2
    coeff = 2.0 * math.pi * M * M / tau2
    return M + coeff * (1.0 / r - 1.0 / params.R_ext)


def compute_equilibrium_density(
    r: np.ndarray, params: RouteCParams,
) -> np.ndarray:
    """Compute equilibrium energy density rho_eq = -M^2 / (2*tau^2*r^4)."""
    M = params.M
    tau2 = params.tau ** 2
    return -M * M / (2.0 * tau2 * r ** 4)


def _integrate_sigma(
    r: np.ndarray, epsilon: np.ndarray,
) -> np.ndarray:
    """Compute Sigma(r) = integral from r to R_ext of 4*pi*r'^2 * epsilon(r') dr'.

    r is sorted R_ext -> R_min (decreasing).  Sigma(R_ext) = 0,
    and Sigma grows as we integrate inward.
    """
    n = len(r)
    Sigma = np.zeros(n)
    integrand = 4.0 * math.pi * r * r * epsilon
    for i in range(1, n):
        dr = r[i] - r[i - 1]  # negative
        Sigma[i] = Sigma[i - 1] - 0.5 * (integrand[i] + integrand[i - 1]) * dr
    return Sigma


# ================================================================
# Level 2: Route C energy profile
# ================================================================

def compute_route_c_energy_profile(
    params: RouteCParams,
) -> RouteCEnergyProfile:
    """Build the Route C effective energy density and compare to epsilon_min.

    Route C (Markov reduction) gives T^Phi as a standard minimally-coupled
    scalar.  The dominant kinetic energy density is:

        epsilon_RC(r) = (1/2) * (Phi_dot)^2
                      = (A_crit^2 * M^2) / (2 * tau^2 * r^4)

    This is PURE 1/r^4 — no 1/r^2 component.

    Compare to epsilon_min(r) = |rho_eq(r)| + 1/(8*pi*r^2), restricted
    to the deficit region (where delta > 0).
    """
    r = make_radial_grid(params)
    m = compute_static_mass(r, params)
    rho_eq = compute_equilibrium_density(r, params)
    delta = m - r / 2.0
    deficit_mask = delta > 0

    # Route C energy density: pure 1/r^4
    eps_rc_coeff = params.A_crit ** 2 * params.M ** 2 / (2.0 * params.tau ** 2)
    epsilon_RC = eps_rc_coeff / r ** 4

    # Minimal source from Phase 6C, restricted to deficit region
    component_A_full = np.abs(rho_eq)          # = M^2/(2*tau^2*r^4)
    component_B_full = 1.0 / (8.0 * math.pi * r ** 2)
    component_A = np.where(deficit_mask, component_A_full, 0.0)
    component_B = np.where(deficit_mask, component_B_full, 0.0)
    epsilon_min = component_A + component_B

    # Deficit ratio: epsilon_RC / epsilon_min (where epsilon_min > 0)
    safe_min = np.where(epsilon_min > 0, epsilon_min, 1.0)
    deficit_ratio = np.where(epsilon_min > 0, epsilon_RC / safe_min, 0.0)

    # Evaluate at key radii
    r_rev = r[::-1]

    def _interp(arr, r_target):
        return float(np.interp(r_target, r_rev, arr[::-1]))

    ratio_at_R_eq = _interp(deficit_ratio, params.R_eq)
    ratio_at_r1 = _interp(deficit_ratio, 1.0)

    # Ratio range (only where epsilon_min > 0)
    valid = epsilon_min > 0
    if np.any(valid):
        ratio_min = float(np.min(deficit_ratio[valid]))
        ratio_max = float(np.max(deficit_ratio[valid]))
    else:
        ratio_min, ratio_max = 0.0, 0.0

    # Component coverage
    covers_A = params.A_crit ** 2 > 1.0   # A_crit > 1 means overcovering A
    covers_B = False                        # No 1/r^2 term in epsilon_RC

    # Integrated shortfall: integral of max(0, epsilon_min - epsilon_RC) * 4*pi*r^2 dr
    shortfall = np.maximum(0.0, epsilon_min - epsilon_RC)
    integrand = shortfall * 4.0 * math.pi * r * r
    integrated = 0.0
    for i in range(1, len(r)):
        dr = r[i] - r[i - 1]
        integrated += abs(0.5 * (integrand[i] + integrand[i - 1]) * dr)

    return RouteCEnergyProfile(
        r=r,
        epsilon_RC=epsilon_RC,
        epsilon_min=epsilon_min,
        component_A=component_A,
        component_B=component_B,
        deficit_ratio=deficit_ratio,
        ratio_at_R_eq=ratio_at_R_eq,
        ratio_at_r1=ratio_at_r1,
        ratio_min=ratio_min,
        ratio_max=ratio_max,
        epsilon_RC_coeff=eps_rc_coeff,
        covers_component_A=covers_A,
        covers_component_B=covers_B,
        integrated_shortfall=integrated,
        notes=[
            f"epsilon_RC_coeff = A_crit^2 * M^2/(2*tau^2) = {eps_rc_coeff:.6f}",
            f"Ratio at R_eq = {ratio_at_R_eq:.4f} (overcovering)",
            f"Ratio at r=1 = {ratio_at_r1:.4f} (undercovering)",
            "Route C is pure 1/r^4: covers Component A, NOT Component B",
            (
                "Shape mismatch: Route C's 1/r^4 support is too concentrated — "
                "it oversupplies the core while undersupplying intermediate radii, "
                "which is exactly the wrong shape to replace Component B.  "
                "The failure is one of shape, not amplitude."
            ),
        ],
    )


# ================================================================
# Level 3: Insufficiency chains
# ================================================================

def evaluate_chain_1_markov_kinetic(
    params: RouteCParams,
) -> InsufficiencyChain:
    """Chain 1: Markov reduction forecloses independent 1/r^2 from kinetics.

    Exponential kernel => Markov property => T^Phi_history = 0
    => T^Phi = standard minimally-coupled scalar
    => kinetic energy epsilon = (1/2)(Phi_dot)^2
    => Phi_dot sourced by X = M/r^2 gives Phi_dot ~ M/(tau*r^2)
    => epsilon ~ M^2/(2*tau^2*r^4) = 1/r^4 ONLY

    The square of any 1/r^n field is 1/r^{2n}.  The minimum n for
    Phi_dot to yield epsilon ~ 1/r^2 is n=1 (i.e. Phi_dot ~ 1/r).
    But X = M/r^2 sources Phi_dot ~ 1/r^2, NOT 1/r.
    """
    # Numerical verification
    coeff = params.A_crit ** 2 * params.M ** 2 / (2.0 * params.tau ** 2)
    r_test = np.array([params.R_eq, 0.5, 1.0, 1.5])
    eps_RC = coeff / r_test ** 4
    # Verify pure 1/r^4 scaling: eps * r^4 should be constant
    product = eps_RC * r_test ** 4
    is_pure_r4 = float(np.std(product) / np.mean(product)) < 1e-10

    return InsufficiencyChain(
        chain_number=1,
        chain_name="markov_kinetic_scaling",
        premise=(
            "The exponential kernel K(s) = (1/tau)exp(-s/tau)Theta(s) has the "
            "Markov property: T^Phi_history is absorbed into the current Phi, "
            "making T^Phi a local function of (Phi, X, g)."
        ),
        mechanism=(
            "The local T^Phi is the standard minimally-coupled scalar form.  "
            "The dominant kinetic energy density is epsilon = (1/2)(Phi_dot)^2.  "
            "Since Phi_dot is sourced by X = M/r^2, the natural profile gives "
            "Phi_dot ~ A_crit * M/(tau * r^2), so epsilon ~ A_crit^2 * M^2 / "
            "(2 * tau^2 * r^4).  This is pure 1/r^4.  "
            f"Verified: eps * r^4 constant to {np.std(product)/np.mean(product):.1e} "
            f"relative deviation."
        ),
        conclusion=(
            "The Markov-reduced kinetic energy density scales as 1/r^4 at all "
            "tested radii.  No independent 1/r^2 component is generated.  "
            "To get epsilon ~ 1/r^2 from (Phi_dot)^2, one would need "
            "Phi_dot ~ 1/r, but the source X = M/r^2 yields Phi_dot ~ 1/r^2."
        ),
        scaling_law="1/r^4",
        provides_1r2=False,
        is_formal=True,
        notes=[
            f"epsilon_RC_coeff = {coeff:.6f}",
            f"Pure 1/r^4 verified: {is_pure_r4}",
            "This chain is the strongest: it is algebraic, not numerical",
        ],
    )


def evaluate_chain_2_self_healing(
    params: RouteCParams,
) -> InsufficiencyChain:
    """Chain 2: Self-healing eliminates lapse correction at equilibrium.

    The metric deficit is a static equilibrium property.
    At equilibrium: X = Phi => lapse correction source = Psi*(X - Phi) = 0
    => delta_Phi = 0 => no additional energy density.
    """
    # Compute X and Phi at equilibrium
    m_R_eq = params.M + MASS_COEFF * (1.0 / params.R_eq - 1.0 / params.R_ext)
    X_eq = m_R_eq / params.R_eq ** 2
    Phi_eq = X_eq  # at equilibrium, memory field tracks source

    source = X_eq - Phi_eq  # = 0 exactly

    return InsufficiencyChain(
        chain_number=2,
        chain_name="self_healing_lapse",
        premise=(
            "The lapse correction ODE is: "
            "tau * d(delta_Phi)/dt + delta_Phi = Psi * (X - Phi).  "
            "At equilibrium, the memory field tracks its source: "
            "M_drive = a_grav, so X = Phi."
        ),
        mechanism=(
            f"At equilibrium: X_eq = Phi_eq = {X_eq:.4f} at R_eq.  "
            f"Source term Psi*(X - Phi) = Psi*{source:.1e} = 0.  "
            "The correction ODE has only the decaying solution "
            "delta_Phi ~ exp(-t/tau) -> 0.  This holds for ANY value of Psi.  "
            "The metric deficit is defined at equilibrium, exactly where "
            "the lapse correction vanishes."
        ),
        conclusion=(
            "Self-healing eliminates the lapse correction at equilibrium.  "
            "The lapse channel adds ZERO energy density where the metric "
            "deficit exists.  The correction is maximal during the transient "
            "approach, not at the endpoint where f < 0."
        ),
        scaling_law="0",
        provides_1r2=False,
        is_formal=True,
        notes=[
            f"X_eq at R_eq = {X_eq:.4f}",
            f"Phi_eq at R_eq = {Phi_eq:.4f}",
            f"Source X - Phi = {source:.1e}",
            "Self-healing is proven at first order (nonlinear = Loophole 3)",
        ],
    )


def evaluate_chain_3_candidate_potential(
    params: RouteCParams,
) -> InsufficiencyChain:
    """Chain 3: Candidate potential V(Phi) ~ 1/r^4 at equilibrium.

    The tested potential V(Phi) = Phi^2/(2*tau^2) is a candidate inherited
    ansatz from Route A / shared closure.  It is NOT intrinsic to Route C.
    At equilibrium Phi_eq = M/r^2, so V ~ M^2/(2*tau^2*r^4) = 1/r^4.
    """
    # Numerical evaluation at R_eq
    Phi_eq_at_R_eq = params.M / params.R_eq ** 2
    V_at_R_eq = Phi_eq_at_R_eq ** 2 / (2.0 * params.tau ** 2)

    # Verify 1/r^4 scaling
    r_test = np.array([params.R_eq, 0.5, 1.0, 1.5])
    Phi_eq = params.M / r_test ** 2
    V_arr = Phi_eq ** 2 / (2.0 * params.tau ** 2)
    product = V_arr * r_test ** 4
    is_pure_r4 = float(np.std(product) / np.mean(product)) < 1e-10

    return InsufficiencyChain(
        chain_number=3,
        chain_name="candidate_potential_scaling",
        premise=(
            "The tested potential V(Phi) = Phi^2/(2*tau^2) is a candidate "
            "inherited ansatz from Route A / shared closure.  It is NOT "
            "an intrinsic or unique Route C potential.  At equilibrium, "
            "Phi_eq = X_eq = M/r^2."
        ),
        mechanism=(
            f"V(Phi_eq) = (M/r^2)^2 / (2*tau^2) = M^2/(2*tau^2*r^4).  "
            f"At R_eq: V = {V_at_R_eq:.4f}.  "
            f"Verified pure 1/r^4 scaling: {is_pure_r4}.  "
            "The potential energy density scales as 1/r^4, adding to "
            "Component A but NOT providing Component B."
        ),
        conclusion=(
            "Within the candidate quadratic potential ansatz, V(Phi) "
            "contributes only 1/r^4 energy density at equilibrium.  "
            "No 1/r^2 component.  This chain tests the currently inherited "
            "potential; it is not a unique or intrinsic Route C potential."
        ),
        scaling_law="1/r^4",
        provides_1r2=False,
        is_formal=True,
        notes=[
            f"V_at_R_eq = {V_at_R_eq:.4f}",
            f"Pure 1/r^4 verified: {is_pure_r4}",
            "NOT intrinsic to Route C — inherited candidate ansatz",
        ],
    )


def evaluate_chain_4_spatial_gradient(
    params: RouteCParams,
) -> InsufficiencyChain:
    """Chain 4: Spatial gradient (nabla_r Phi)^2 ~ 1/r^6 in reduced background.

    At equilibrium: Phi_eq = M/r^2, so dPhi/dr = -2M/r^3.
    (dPhi/dr)^2 = 4M^2/r^6 => 1/r^6.
    Even steeper than 1/r^4; does not help with 1/r^2.

    This is evaluated in the current reduced radial background, NOT
    a full covariant gradient-sector derivation.
    """
    # Numerical evaluation at R_eq
    dPhi_dr_at_R_eq = -2.0 * params.M / params.R_eq ** 3
    grad_sq_at_R_eq = dPhi_dr_at_R_eq ** 2

    # Verify 1/r^6 scaling
    r_test = np.array([params.R_eq, 0.5, 1.0, 1.5])
    dPhi_dr = -2.0 * params.M / r_test ** 3
    grad_sq = dPhi_dr ** 2
    product = grad_sq * r_test ** 6
    is_pure_r6 = float(np.std(product) / np.mean(product)) < 1e-10

    return InsufficiencyChain(
        chain_number=4,
        chain_name="spatial_gradient_scaling",
        premise=(
            "At equilibrium Phi_eq = M/r^2.  The spatial gradient is "
            "dPhi/dr = -2M/r^3.  The gradient-squared term in T^Phi is "
            "(1/2)(dPhi/dr)^2 = 2M^2/r^6."
        ),
        mechanism=(
            f"(dPhi/dr)^2 at R_eq = {grad_sq_at_R_eq:.2f}.  "
            f"Verified pure 1/r^6 scaling: {is_pure_r6}.  "
            "The spatial gradient energy density scales as 1/r^6, "
            "which is even STEEPER than the 1/r^4 kinetic contribution.  "
            "It concentrates energy even more at small r."
        ),
        conclusion=(
            "The spatial gradient contributes 1/r^6 energy density in the "
            "current reduced radial background.  This is steeper than 1/r^4 "
            "and does not provide 1/r^2 intermediate-radius support.  "
            "This analysis is NOT a full covariant gradient-sector derivation."
        ),
        scaling_law="1/r^6",
        provides_1r2=False,
        is_formal=True,
        notes=[
            f"gradient_sq_at_R_eq = {grad_sq_at_R_eq:.2f}",
            f"Pure 1/r^6 verified: {is_pure_r6}",
            "Evaluated in current reduced background, not full covariant",
        ],
    )


def assess_insufficiency(
    params: RouteCParams,
) -> InsufficiencyAssessment:
    """Evaluate all four insufficiency chains and aggregate."""
    chain1 = evaluate_chain_1_markov_kinetic(params)
    chain2 = evaluate_chain_2_self_healing(params)
    chain3 = evaluate_chain_3_candidate_potential(params)
    chain4 = evaluate_chain_4_spatial_gradient(params)

    chains = [chain1, chain2, chain3, chain4]
    any_provides = any(c.provides_1r2 for c in chains)
    all_consistent = all(not c.provides_1r2 for c in chains)

    classification = "route_c_insufficient_within_markov_reduction"

    return InsufficiencyAssessment(
        chains=chains,
        n_chains=4,
        all_chains_consistent=all_consistent,
        any_chain_provides_1r2=any_provides,
        overall_insufficient=not any_provides,
        is_general_no_go=False,
        classification_string=classification,
        notes=[
            "All four chains return provides_1r2 = False",
            "Chain 1 (kinetic: 1/r^4) is the strongest structural argument",
            "Chain 2 (self-healing: source=0) is an exact result at equilibrium",
            "Chain 3 (potential: 1/r^4) tests inherited ansatz, not intrinsic",
            "Chain 4 (gradient: 1/r^6) is steeper, making things worse",
            "This is NOT a general no-go — 5 loopholes are documented",
        ],
    )


# ================================================================
# Level 3b: Detailed sub-analyses
# ================================================================

def compute_lapse_correction_at_equilibrium(
    params: RouteCParams,
) -> LapseCorrectionAtEquilibrium:
    """Compute lapse correction magnitude at equilibrium.

    At equilibrium: X_eq = M/R_eq^2, Phi_eq = X_eq
    Source = Psi * (X - Phi) = 0
    Therefore delta_Phi_lapse = 0 (self-healing).
    """
    m_R_eq = params.M + MASS_COEFF * (1.0 / params.R_eq - 1.0 / params.R_ext)
    X_eq = m_R_eq / params.R_eq ** 2
    Phi_eq = X_eq

    return LapseCorrectionAtEquilibrium(
        X_eq_at_R_eq=X_eq,
        Phi_eq_at_R_eq=Phi_eq,
        source_X_minus_Phi=X_eq - Phi_eq,
        delta_Phi_lapse=0.0,
        self_healing_holds=True,
        notes=[
            f"X_eq at R_eq = {X_eq:.4f}",
            f"Phi_eq at R_eq = {Phi_eq:.4f}",
            f"X - Phi = {X_eq - Phi_eq:.1e} (identically zero at equilibrium)",
            "Self-healing is proven at first order in lapse correction",
            "Nonlinear lapse effects remain open (Loophole 3)",
        ],
    )


def analyze_potential_sector(
    params: RouteCParams,
) -> PotentialSectorAnalysis:
    """Analyze V(Phi) contribution scaling at equilibrium.

    V(Phi) = Phi^2/(2*tau^2), Phi_eq = M/r^2
    V_eq(r) = M^2/(2*tau^2*r^4) => 1/r^4
    """
    Phi_eq_at_R_eq = params.M / params.R_eq ** 2
    V_at_R_eq = Phi_eq_at_R_eq ** 2 / (2.0 * params.tau ** 2)

    return PotentialSectorAnalysis(
        V_form="Phi^2 / (2*tau^2)",
        Phi_eq_scaling="M/r^2",
        V_scaling="M^2/(2*tau^2*r^4) = 1/r^4",
        provides_1r2=False,
        V_at_R_eq=V_at_R_eq,
        is_intrinsic_route_c=False,
        notes=[
            f"V(Phi_eq) at R_eq = {V_at_R_eq:.4f}",
            "V scales as 1/r^4 — same as kinetic, adds to Component A",
            "This is a tested inherited candidate ansatz, NOT intrinsic to Route C",
            "Other potentials could yield different scaling (Loophole 5 extension)",
        ],
    )


def analyze_spatial_gradient(
    params: RouteCParams,
) -> SpatialGradientAnalysis:
    """Analyze (nabla_r Phi)^2 scaling at equilibrium.

    dPhi/dr = d(M/r^2)/dr = -2M/r^3
    (dPhi/dr)^2 = 4M^2/r^6 => 1/r^6

    Evaluated in the current reduced radial background.
    """
    dPhi_dr = -2.0 * params.M / params.R_eq ** 3
    grad_sq = dPhi_dr ** 2

    return SpatialGradientAnalysis(
        dPhi_dr_scaling="-2M/r^3",
        gradient_sq_scaling="4M^2/r^6 = 1/r^6",
        provides_1r2=False,
        gradient_sq_at_R_eq=grad_sq,
        evaluated_in_reduced_background=True,
        notes=[
            f"(dPhi/dr)^2 at R_eq = {grad_sq:.2f}",
            "1/r^6 is steeper than 1/r^4 — concentrates even more at core",
            "Evaluated in current reduced radial background",
            "Full covariant gradient includes metric factors (not computed)",
        ],
    )


# ================================================================
# Level 4: Loophole catalog
# ================================================================

def catalog_loopholes() -> LoopholeCatalog:
    """Catalog the five documented loopholes with severity assessment.

    Severity criteria:
      high:   could plausibly provide 1/r^2 through identified mechanism
      medium: theoretically possible but requires substantial new physics
      low:    unlikely to change the conclusion
    """
    loopholes = [
        Loophole(
            loophole_number=1,
            name="non_exponential_kernel",
            description=(
                "Non-exponential kernel breaks the Markov property.  "
                "T^Phi_history would be genuinely nonlocal and could include "
                "1/r^2 terms not captured by the auxiliary-field reduction."
            ),
            mechanism=(
                "For K(s) != (1/tau)exp(-s/tau), the retarded integral "
                "does NOT reduce to a first-order ODE.  The stress-functional "
                "retains explicit dependence on the metric history, potentially "
                "generating energy density with different radial structure."
            ),
            could_provide_1r2=True,
            severity="high",
            requires_beyond_markov=True,
            requires_beyond_equilibrium=False,
            tested_within_module=False,
            notes=[
                "This is the most fundamental loophole",
                "The exponential kernel is special (unique Markov property)",
                "Power-law, Gaussian, or other kernels remain untested",
            ],
        ),
        Loophole(
            loophole_number=2,
            name="full_covariant_metric_variation",
            description=(
                "The full covariant metric variation delta S_nonlocal / "
                "delta g^{mu nu} has NOT been computed in closed form.  "
                "The variation has 5 distinct contributions (volume, source, "
                "kernel, proper time, observer flow)."
            ),
            mechanism=(
                "The obstruction (from nonlocal_stress.py): the integrand "
                "and integration domain both depend on g; variational calculus "
                "of nonlocal functionals where the kernel depends on the metric.  "
                "Closed-form terms could alter the energy density profile."
            ),
            could_provide_1r2=True,
            severity="medium",
            requires_beyond_markov=False,
            requires_beyond_equilibrium=False,
            tested_within_module=False,
            notes=[
                "5 distinct contributions to the metric variation",
                "Even for exponential kernel, the full variation may "
                "differ from the auxiliary-field local reduction",
                "This is flagged as open in nonlocal_stress.py Section C",
            ],
        ),
        Loophole(
            loophole_number=3,
            name="nonlinear_lapse_effects",
            description=(
                "The self-healing analysis (Chain 2) is first-order in the "
                "lapse perturbation Psi.  Nonlinear lapse effects O(Psi^2) "
                "or beyond could generate residual corrections at equilibrium."
            ),
            mechanism=(
                "At strong field (C=3, Psi ~ O(1)), higher-order terms in "
                "Psi could modify the source term.  The perturbative expansion "
                "may break down near the equilibrium endpoint."
            ),
            could_provide_1r2=True,
            severity="low",
            requires_beyond_markov=False,
            requires_beyond_equilibrium=False,
            tested_within_module=False,
            notes=[
                "Self-healing is exact at first order (source vanishes)",
                "Nonlinear corrections would require Psi^2*(X-Phi) or "
                "Psi*d(X-Phi)/dt terms, which may also vanish at equilibrium",
                "Severity is low because equilibrium X=Phi is a structural identity",
            ],
        ),
        Loophole(
            loophole_number=4,
            name="off_equilibrium_transient_effects",
            description=(
                "The metric deficit is defined at static equilibrium.  "
                "During the transient approach to equilibrium, kinetic "
                "processing could alter the mass profile baseline."
            ),
            mechanism=(
                "If transient processing redistributes mass before reaching "
                "equilibrium, the final static mass profile could differ from "
                "the Phase 6 linearized result.  This would change delta(r) "
                "and therefore epsilon_min."
            ),
            could_provide_1r2=True,
            severity="medium",
            requires_beyond_markov=False,
            requires_beyond_equilibrium=True,
            tested_within_module=False,
            notes=[
                "Phase 6C assumes static equilibrium baseline (Assumption 4)",
                "Transient kinetic processing was explored in Phase 6B "
                "but found insufficient within tested amplitudes",
                "Self-consistent dynamical evolution could change baseline",
            ],
        ),
        Loophole(
            loophole_number=5,
            name="modified_source_law",
            description=(
                "The current source is X = M/r^2, yielding Phi_dot ~ 1/r^2 "
                "and epsilon ~ 1/r^4.  A modified source X ~ M/r (shallower) "
                "would give Phi_dot ~ 1/r and epsilon ~ 1/r^2."
            ),
            mechanism=(
                "If the gravitational source law were modified (e.g. through "
                "curvature-scalar coupling, R*Phi terms, or non-standard "
                "sourcing), the natural profile of Phi_dot could shift from "
                "1/r^2 to 1/r, producing the missing 1/r^2 energy density."
            ),
            could_provide_1r2=True,
            severity="high",
            requires_beyond_markov=False,
            requires_beyond_equilibrium=False,
            tested_within_module=False,
            notes=[
                "Requires non-standard sourcing: X != M/r^2",
                "This includes curvature-scalar coupling (R*Phi)",
                "Also includes modified metric ansatz for the interior",
                "Currently no GRUT module provides X ~ 1/r sourcing",
            ],
        ),
    ]

    n_high = sum(1 for lp in loopholes if lp.severity == "high")
    n_med = sum(1 for lp in loopholes if lp.severity == "medium")
    n_low = sum(1 for lp in loopholes if lp.severity == "low")
    any_tested = any(lp.tested_within_module for lp in loopholes)

    return LoopholeCatalog(
        loopholes=loopholes,
        n_loopholes=len(loopholes),
        n_high_severity=n_high,
        n_medium_severity=n_med,
        n_low_severity=n_low,
        any_tested=any_tested,
        notes=[
            f"{n_high} high-severity, {n_med} medium-severity, {n_low} low-severity",
            "None are tested within this module — each requires new physics or computation",
            "High-severity loopholes could plausibly provide 1/r^2 support",
            "Route C remains alive through these loopholes despite the insufficiency",
        ],
    )


# ================================================================
# Level 5: Ranking and classification
# ================================================================

def build_provisional_candidate_ranking() -> ProvisionalCandidateRankingUpdate:
    """Build the provisional candidate-sector ranking update.

    Route C: insufficient_within_markov_reduction (downgraded)
    Route B: provisional (ghost mode obstruction, gravity coupling)
    Route A: conditional_partial_closure (from Phase VII)
    """
    return ProvisionalCandidateRankingUpdate(
        route_c_status="insufficient_within_markov_reduction",
        route_c_previous_status="highest_structural_plausibility",
        route_c_downgraded=True,
        route_b_status="provisional",
        route_b_obstruction=(
            "Ghost mode grows at rate phi/tau (golden ratio); "
            "gravity coupling in doubled-metric sector underdetermined"
        ),
        route_a_status="conditional_partial_closure",
        is_provisional=True,
        notes=[
            "Route C downgraded from 'highest structural plausibility' "
            "to 'insufficient within Markov reduction'",
            "Route C remains alive through 5 documented loopholes "
            "(2 high-severity, 2 medium, 1 low)",
            "Route B remains provisional — different obstruction class "
            "(ghost/coupling), not tested against 1/r^2 requirement",
            "Route A conditional on potential ansatz and overdamped limit",
            "This is a provisional ranking update, not a final determination",
        ],
    )


def classify_route_c_deficit(
    energy_profile: RouteCEnergyProfile,
    insufficiency: InsufficiencyAssessment,
    loopholes: LoopholeCatalog,
) -> RouteCClassification:
    """Determine the final Route C classification."""
    return RouteCClassification(
        classification="route_c_insufficient_within_markov_reduction",
        route_c_provides_component_A=energy_profile.covers_component_A,
        route_c_provides_component_B=energy_profile.covers_component_B,
        overall_insufficient_within_markov=insufficiency.overall_insufficient,
        is_general_no_go=False,
        shape_mismatch_description=(
            "Route C's effective 1/r^4 support is too concentrated: "
            "it oversupplies the core (ratio > 1 at R_eq) while "
            "undersupplying intermediate radii (ratio ~ 0.76 at r=1).  "
            "The failure is one of shape, not amplitude.  "
            f"Deficit ratio ranges from {energy_profile.ratio_min:.3f} "
            f"to {energy_profile.ratio_max:.3f}."
        ),
        notes=[
            f"Covers Component A: {energy_profile.covers_component_A}",
            f"Covers Component B: {energy_profile.covers_component_B}",
            f"Overall insufficient within Markov: {insufficiency.overall_insufficient}",
            f"Is general no-go: False",
            f"Loopholes: {loopholes.n_loopholes} documented "
            f"({loopholes.n_high_severity} high severity)",
        ],
    )


# ================================================================
# Master analysis function
# ================================================================

def compute_route_c_deficit_assessment(
    params: Optional[RouteCParams] = None,
    do_energy_profile: bool = True,
    do_insufficiency: bool = True,
    do_lapse: bool = True,
    do_potential: bool = True,
    do_spatial_gradient: bool = True,
    do_loopholes: bool = True,
    do_ranking: bool = True,
    do_classification: bool = True,
) -> RouteCDeficitResult:
    """Master function: Route C deficit assessment.

    Tests whether Route C (nonlocal metric back-reaction) can generate
    the missing 1/r^2 support identified in Phase 6C.

    Within the tested Markov-reduced exponential-kernel pathway, Route C
    reproduces only the existing 1/r^4-type support structure and fails
    to generate an independent 1/r^2-type component.
    """
    if params is None:
        params = RouteCParams()

    result = RouteCDeficitResult(
        params=params,
        nonclaims=NONCLAIMS,
        assumptions=ROUTE_C_ASSUMPTIONS,
    )

    # Level 2: Energy profile
    energy = None
    if do_energy_profile:
        energy = compute_route_c_energy_profile(params)
        result.energy_profile = energy

    # Level 3: Insufficiency chains
    insuff = None
    if do_insufficiency:
        insuff = assess_insufficiency(params)
        result.insufficiency_assessment = insuff

    # Level 3b: Detailed sub-analyses
    if do_lapse:
        result.lapse_correction = compute_lapse_correction_at_equilibrium(params)

    if do_potential:
        result.potential_sector = analyze_potential_sector(params)

    if do_spatial_gradient:
        result.spatial_gradient = analyze_spatial_gradient(params)

    # Level 4: Loopholes
    loopholes = None
    if do_loopholes:
        loopholes = catalog_loopholes()
        result.loophole_catalog = loopholes

    # Level 5: Ranking and classification
    if do_ranking:
        result.provisional_ranking = build_provisional_candidate_ranking()

    if do_classification and energy is not None and insuff is not None and loopholes is not None:
        result.classification = classify_route_c_deficit(energy, insuff, loopholes)

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def route_c_result_to_dict(result: RouteCDeficitResult) -> Dict[str, Any]:
    """Serialize the master result to a dictionary."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "params": {
            "r_s": result.params.r_s,
            "M": result.params.M,
            "R_eq": result.params.R_eq,
            "tau": result.params.tau,
            "R_ext": result.params.R_ext,
            "n_r": result.params.n_r,
            "A_crit": result.params.A_crit,
        },
    }

    if result.energy_profile:
        ep = result.energy_profile
        d["energy_profile"] = {
            "epsilon_RC_coeff": ep.epsilon_RC_coeff,
            "ratio_at_R_eq": ep.ratio_at_R_eq,
            "ratio_at_r1": ep.ratio_at_r1,
            "ratio_min": ep.ratio_min,
            "ratio_max": ep.ratio_max,
            "covers_component_A": ep.covers_component_A,
            "covers_component_B": ep.covers_component_B,
            "integrated_shortfall": ep.integrated_shortfall,
        }

    if result.insufficiency_assessment:
        ia = result.insufficiency_assessment
        d["insufficiency_assessment"] = {
            "n_chains": ia.n_chains,
            "all_chains_consistent": ia.all_chains_consistent,
            "any_chain_provides_1r2": ia.any_chain_provides_1r2,
            "overall_insufficient": ia.overall_insufficient,
            "is_general_no_go": ia.is_general_no_go,
            "classification_string": ia.classification_string,
            "chains": [
                {
                    "chain_number": c.chain_number,
                    "chain_name": c.chain_name,
                    "scaling_law": c.scaling_law,
                    "provides_1r2": c.provides_1r2,
                }
                for c in ia.chains
            ],
        }

    if result.lapse_correction:
        lc = result.lapse_correction
        d["lapse_correction"] = {
            "X_eq_at_R_eq": lc.X_eq_at_R_eq,
            "Phi_eq_at_R_eq": lc.Phi_eq_at_R_eq,
            "source_X_minus_Phi": lc.source_X_minus_Phi,
            "delta_Phi_lapse": lc.delta_Phi_lapse,
            "self_healing_holds": lc.self_healing_holds,
        }

    if result.potential_sector:
        ps = result.potential_sector
        d["potential_sector"] = {
            "V_form": ps.V_form,
            "V_scaling": ps.V_scaling,
            "provides_1r2": ps.provides_1r2,
            "V_at_R_eq": ps.V_at_R_eq,
            "is_intrinsic_route_c": ps.is_intrinsic_route_c,
        }

    if result.spatial_gradient:
        sg = result.spatial_gradient
        d["spatial_gradient"] = {
            "gradient_sq_scaling": sg.gradient_sq_scaling,
            "provides_1r2": sg.provides_1r2,
            "gradient_sq_at_R_eq": sg.gradient_sq_at_R_eq,
            "evaluated_in_reduced_background": sg.evaluated_in_reduced_background,
        }

    if result.loophole_catalog:
        lpc = result.loophole_catalog
        d["loophole_catalog"] = {
            "n_loopholes": lpc.n_loopholes,
            "n_high_severity": lpc.n_high_severity,
            "n_medium_severity": lpc.n_medium_severity,
            "n_low_severity": lpc.n_low_severity,
            "any_tested": lpc.any_tested,
            "loopholes": [
                {
                    "number": lp.loophole_number,
                    "name": lp.name,
                    "severity": lp.severity,
                    "could_provide_1r2": lp.could_provide_1r2,
                    "requires_beyond_markov": lp.requires_beyond_markov,
                    "tested_within_module": lp.tested_within_module,
                }
                for lp in lpc.loopholes
            ],
        }

    if result.provisional_ranking:
        pr = result.provisional_ranking
        d["provisional_ranking"] = {
            "route_c_status": pr.route_c_status,
            "route_c_previous_status": pr.route_c_previous_status,
            "route_c_downgraded": pr.route_c_downgraded,
            "route_b_status": pr.route_b_status,
            "route_b_obstruction": pr.route_b_obstruction,
            "route_a_status": pr.route_a_status,
            "is_provisional": pr.is_provisional,
        }

    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "route_c_provides_component_A": cl.route_c_provides_component_A,
            "route_c_provides_component_B": cl.route_c_provides_component_B,
            "overall_insufficient_within_markov": cl.overall_insufficient_within_markov,
            "is_general_no_go": cl.is_general_no_go,
            "shape_mismatch_description": cl.shape_mismatch_description,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
