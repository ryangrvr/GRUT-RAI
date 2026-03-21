"""Route B mixed g_+ * g_- cross-coupling channel analysis.

Phase Absolute Final Classical Pass — determines whether the surviving mixed
g_+ * g_- cross-coupling channel can induce effective support compatible with
the missing 1/r^2-type Component B, or whether the classical frontier closes
with this channel insufficient within the tested framework.

PRINCIPAL RESULTS (three-part answer):

  A. The surviving mixed quadratic structure is delta^2 S_EH(h_+, h_-) — the
     Lichnerowicz bilinear form.  This is the ONLY quadratic term in S_1 - S_2
     after CTP antisymmetry kills the diagonal h_-^2.

  B. The mixed channel is sourced by the ghost scalar Phi_-.  The source chain
     IC -> Phi_- -> T_tilde -> h_- -> h_+ correction propagates IC-dependence,
     ghost contamination, CTP-killing, and projection-killing at every step.

  C. The four pathologies (IC-dependent, ghost-sourced, CTP-killed, projection-
     killed) jointly render the mixed channel non-promotable to a clean physical
     Component B mechanism within the tested perturbative Galley framework.

EXECUTIVE RESULT:
  This phase closes the final tested classical Route B residue within the
  perturbative Galley CTP framework.  The mixed channel is insufficient for
  Component B.  All tested classical Route B channels are now classified.

CLASSIFICATION:
  mixed_channel_insufficient_within_tested_galley_framework

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
A_CRIT = PHASE6B_A_CRIT_NATURAL
RHO_EQ_COEFF = M_EXT ** 2 / (2.0 * TAU_CANONICAL ** 2)
EPSILON_RC_COEFF = A_CRIT ** 2 * RHO_EQ_COEFF
COMP_B_COEFF = 1.0 / (8.0 * math.pi)

# Route B ghost sector (from route_b_component_b.py)
PHI_GOLDEN = (1.0 + math.sqrt(5.0)) / 2.0  # ~ 1.618

# CTP antisymmetry (from route_b_gminus_energy.py)
CTP_ANTISYMMETRY_ORDER = 2  # the diagonal quadratic order that is killed

# Mixed channel
N_IC_PROFILES = 2  # number of IC profiles tested for shape analysis
COMPONENT_B_SCALING = -2.0  # the target power-law exponent for Component B (1/r^2)


# ================================================================
# Assumptions — explicitly documented
# ================================================================

MIXED_ASSUMPTIONS = [
    "1. The doubled-metric action is S_grav = (1/16*pi*G) * integral "
    "[sqrt(-g_1)*R_1 - sqrt(-g_2)*R_2] d^4x.  This is the Galley CTP "
    "gravitational action for the doubled-metric system.",

    "2. The +/- decomposition: g_+ = (g_1 + g_2)/2, g_- = g_1 - g_2 "
    "(standard CTP variables).  So g_1 = g_+ + g_-/2, g_2 = g_+ - g_-/2.",

    "3. The background is the static spherically symmetric equilibrium "
    "with Phi_eq = X_eq = M/r^2.  This is the same background as Routes B and C.",

    "4. Perturbative analysis: h_+ = delta g_+ (physical metric perturbation), "
    "h_- = g_- (metric difference).  Both are treated as small perturbations "
    "around the background metric.",

    "5. The surviving mixed quadratic structure is delta^2 S_EH(h_+, h_-) "
    "(diagonal h_-^2 absent by CTP antisymmetry, established in g_- energy phase).",

    "6. The scalar difference sector: Phi_- grows at rate phi/tau with "
    "IC-dependent spatial profile f(r) (established in route_b_component_b.py). "
    "phi = golden ratio ~ 1.618.",

    "7. The scalar difference stress-energy T_tilde_mu_nu is bilinear in "
    "Phi_eq and Phi_- at leading order.  T_tilde = partial_mu Phi_eq * "
    "partial_nu Phi_- + partial_mu Phi_- * partial_nu Phi_eq - g_mu_nu "
    "[partial^a Phi_eq * partial_a Phi_- + m^2 Phi_eq * Phi_-].",

    "8. The h_- EOM is the linearized Einstein equation G_hat(h_-) = "
    "-16*pi*G * T_tilde_mu_nu[Phi_-], sourced by the scalar difference "
    "stress-energy.  This is a standard inhomogeneous Lichnerowicz equation.",

    "9. The CTP boundary condition requires Phi_-(t_final) = 0 and "
    "h_-(t_final) = 0.  This is fundamental to the Galley variational "
    "principle — without it the EOM derivation does not close.",

    "10. Component B requires a geometric (IC-independent) 1/r^2-type "
    "radial support profile.  An IC-dependent profile cannot serve as "
    "a universal geometric closure mechanism.",
]


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. This phase does NOT prove Route B physically incorrect in full "
    "generality.  It closes the tested classical Route B residue within "
    "the Galley CTP framework at perturbative order.",

    "2. A formal mixed coupling is not automatically a physical support "
    "term.  Here the mixed channel is explicitly shown to be ghost-sourced, "
    "IC-dependent, CTP-killed, and projection-killed.",

    "3. Pre-projection structure is not automatically usable post-projection. "
    "The mixed channel exists only pre-projection and vanishes entirely "
    "in the physical limit.",

    "4. Gauge sensitivity: the linearized Einstein equation involves gauge "
    "choices.  The IC-dependence and projection-killing results are "
    "gauge-independent, but the detailed form of h_- may be gauge-dependent.",

    "5. Failure here closes only the tested classical Route B residue, not "
    "all conceivable classical mechanisms (e.g., non-Galley constructions, "
    "higher-order effects, non-perturbative mechanisms).",

    "6. The explicit tensor structure of h_- has NOT been solved in closed "
    "form.  The analysis derives the source chain structurally and verifies "
    "IC-dependence numerically.",

    "7. The 'integration out' of h_- is a structural EOM-level argument, "
    "not a path-integral integration.  We use the h_- equation of motion "
    "to express h_- in terms of sources, then substitute into the h_+ "
    "equation to identify the effective correction.",

    "8. The IC-dependence result relies on Phi_- being IC-dependent, "
    "established in route_b_component_b.py.  This phase inherits that result.",

    "9. The ghost characterization of Phi_- (wrong-sign kinetic) was "
    "established in galley_truncation.py.  This phase inherits that result.",

    "10. Non-perturbative effects, if they exist, are outside the scope "
    "of this linearized analysis.  The classical frontier is closed only "
    "within the tested perturbative Galley framework.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class RouteBMixedParams:
    """Parameters for the mixed g_+ * g_- channel analysis."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S
    R_min: float = 0.05
    n_r: int = 500
    A_crit: float = A_CRIT
    phi_golden: float = PHI_GOLDEN
    # Effective mass squared for the scalar field: m^2 = 1/tau^2
    m_squared: float = 1.0 / (TAU_CANONICAL ** 2)


@dataclass
class MixedChannelDefinition:
    """Defines the mixed g_+ * g_- cross-coupling object.

    The mixed term delta^2 S_EH(h_+, h_-) is the Lichnerowicz bilinear form:
      (1/16*pi*G) * integral h_+^{mu nu} * G_hat_{mu nu, alpha beta} *
      h_-^{alpha beta} d^4x

    It is the ONLY surviving quadratic term in S_1 - S_2 at second order.
    """
    object_name: str = ""
    is_bilinear: bool = False
    is_self_adjoint: bool = False
    is_only_surviving_quadratic: bool = False
    diagonal_h_minus_squared_absent: bool = False
    diagonal_h_plus_squared_cancelled: bool = False
    linear_in_h_plus: bool = False
    linear_in_h_minus: bool = False
    perturbative_order: int = 0
    background_description: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class MixedQuadraticStructure:
    """Derivation of the surviving mixed quadratic structure.

    From the Taylor expansion of S_1 - S_2 around background:
    - delta^2 S(eta_1, eta_1) - delta^2 S(eta_2, eta_2) = 2 * delta^2 S(h_+, h_-)
    """
    mixed_term_survives: bool = False
    analytical_coefficient: float = 0.0  # should be 2.0
    numerical_verification_passed: bool = False
    numerical_verification_max_residual: float = 0.0
    is_self_adjoint: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class InducedSourceAnalysis:
    """Analysis of the source chain: Phi_- -> T_tilde -> h_- -> h_+ correction.

    The h_- equation of motion is:
      G_hat(h_-) = -16*pi*G * T_tilde_mu_nu[Phi_-]

    where T_tilde is the scalar difference stress-energy.
    """
    source_chain_identified: bool = False
    h_minus_eom_is_linearized_einstein: bool = False
    source_is_t_tilde_phi_minus: bool = False
    t_tilde_is_bilinear_in_phi_eq_phi_minus: bool = False
    is_ghost_sourced: bool = False
    is_ic_dependent: bool = False
    is_time_dependent: bool = False
    time_growth_exponent: float = 0.0  # 2*phi/tau
    # Computed T_tilde profiles for two IC profiles
    profile_1_label: str = ""
    profile_1_dominant_scaling_large_r: float = 0.0
    profile_1_dominant_scaling_small_r: float = 0.0
    profile_2_label: str = ""
    profile_2_dominant_scaling_large_r: float = 0.0
    profile_2_dominant_scaling_small_r: float = 0.0
    profiles_differ: bool = False
    structural_ic_dependence_argument: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class ShapeCompatibility:
    """Radial shape analysis for Component B compatibility.

    Tests whether the induced effective source has 1/r^2 scaling
    compatible with Component B.
    """
    is_ic_dependent: bool = False
    matches_component_b: bool = False
    radial_profiles_differ: bool = False
    profile_1_best_fit_exponent: float = 0.0
    profile_2_best_fit_exponent: float = 0.0
    component_b_exponent: float = COMPONENT_B_SCALING
    structural_argument: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class MixedProjectionSensitivity:
    """Projection and CTP boundary sensitivity analysis."""
    survives_physical_limit: bool = True
    survives_ctp_boundary: bool = True
    is_pre_projection_only: bool = False
    physical_limit_argument: str = ""
    ctp_boundary_argument: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class MixedPhysicalAdmissibility:
    """Physical admissibility assessment.

    Four pathology channels are tested.  They jointly render the mixed channel
    non-promotable to a clean physical Component B mechanism within the tested
    perturbative Galley framework.
    """
    is_physically_admissible: bool = True
    n_pathology_channels: int = 0
    jointly_disqualifying: bool = False
    pathology_ic_dependent: bool = False
    pathology_ghost_sourced: bool = False
    pathology_ctp_killed: bool = False
    pathology_projection_killed: bool = False
    admissibility_scope: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBMixedClassification:
    """Final classification with full Route B status update."""
    classification: str = ""
    # Route B channel statuses (all 5 tested channels)
    post_projection_status: str = ""
    phi_minus_status: str = ""
    s_diss_status: str = ""
    gminus_diagonal_status: str = ""
    gminus_mixed_status: str = ""
    # Key booleans
    route_b_classical_channels_closed: bool = False
    all_tested_channels_classified: bool = False
    framework_scope: str = ""
    recommended_next: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBMixedResult:
    """Master result for the mixed g_+ * g_- channel analysis."""
    valid: bool = False
    params: RouteBMixedParams = field(default_factory=RouteBMixedParams)
    definition: Optional[MixedChannelDefinition] = None
    quadratic_structure: Optional[MixedQuadraticStructure] = None
    induced_source: Optional[InducedSourceAnalysis] = None
    shape: Optional[ShapeCompatibility] = None
    projection: Optional[MixedProjectionSensitivity] = None
    admissibility: Optional[MixedPhysicalAdmissibility] = None
    classification: Optional[RouteBMixedClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Radial grid and baseline
# ================================================================

def make_radial_grid(params: RouteBMixedParams) -> np.ndarray:
    """Create log-spaced radial grid from R_ext down to R_min."""
    r_min = max(params.R_min, params.R_eq * 0.8)
    log_r = np.linspace(math.log(params.R_ext), math.log(r_min), params.n_r)
    return np.exp(log_r)


def compute_equilibrium_density(
    r: np.ndarray, params: RouteBMixedParams,
) -> np.ndarray:
    """Compute equilibrium energy density rho_eq = -M^2 / (2*tau^2*r^4)."""
    M = params.M
    tau2 = params.tau ** 2
    return -M * M / (2.0 * tau2 * r ** 4)


# ================================================================
# Level 2: Mixed Channel Definition
# ================================================================

def define_mixed_channel(
    params: RouteBMixedParams,
) -> MixedChannelDefinition:
    """Define the mixed g_+ * g_- cross-coupling object.

    The doubled-metric action expanded around background g_bar:
        g_1 = g_bar + h_+ + h_-/2
        g_2 = g_bar + h_+ - h_-/2

    S_1 - S_2 = S_EH[g_bar + eta_1] - S_EH[g_bar + eta_2]

    where eta_1 = h_+ + h_-/2, eta_2 = h_+ - h_-/2.

    At second order:
        (1/2)[delta^2 S(eta_1, eta_1) - delta^2 S(eta_2, eta_2)]
        = (1/2)[2 * delta^2 S(h_+, h_-)]
        = delta^2 S(h_+, h_-)

    This is the ONLY surviving quadratic term because:
    - delta^2 S(h_+, h_+) cancels between the two copies
    - delta^2 S(h_-, h_-) cancels by CTP antisymmetry (established in g_- energy phase)
    """
    return MixedChannelDefinition(
        object_name="delta^2_S_EH(h_+, h_-)",
        is_bilinear=True,
        is_self_adjoint=True,
        is_only_surviving_quadratic=True,
        diagonal_h_minus_squared_absent=True,
        diagonal_h_plus_squared_cancelled=True,
        linear_in_h_plus=True,
        linear_in_h_minus=True,
        perturbative_order=2,
        background_description=(
            "Static spherically symmetric equilibrium with Phi_eq = M/r^2"
        ),
        notes=[
            "Mixed term delta^2 S_EH(h_+, h_-) is the Lichnerowicz bilinear form",
            "Bilinear: linear in h_+ AND linear in h_-",
            "Self-adjoint: delta^2 S(h_+, h_-) = delta^2 S(h_-, h_+)",
            "ONLY surviving quadratic term in S_1 - S_2 at second order",
            "Diagonal h_-^2: absent by CTP antisymmetry (g_- energy phase)",
            "Diagonal h_+^2: cancels between the two copies",
            "Perturbative order: 2 (second variation of Einstein-Hilbert)",
        ],
    )


# ================================================================
# Level 3: Mixed Quadratic Structure
# ================================================================

def derive_mixed_quadratic_structure(
    params: RouteBMixedParams,
) -> MixedQuadraticStructure:
    """Derive the surviving mixed quadratic structure.

    Using bilinearity:
        delta^2 S(eta_1, eta_1) = delta^2 S(h_+ + h_-/2, h_+ + h_-/2)
            = delta^2 S(h_+, h_+) + delta^2 S(h_+, h_-) + (1/4) delta^2 S(h_-, h_-)

        delta^2 S(eta_2, eta_2) = delta^2 S(h_+ - h_-/2, h_+ - h_-/2)
            = delta^2 S(h_+, h_+) - delta^2 S(h_+, h_-) + (1/4) delta^2 S(h_-, h_-)

    Difference:
        delta^2 S(eta_1, eta_1) - delta^2 S(eta_2, eta_2) = 2 * delta^2 S(h_+, h_-)

    The coefficient 2 is exact (from bilinearity of the second variation).

    NUMERICAL VERIFICATION:
    Using scalar model f(x) = x^4 to verify the mixed term.
    For f(a + delta + eps/2) - f(a + delta - eps/2), the mixed term
    proportional to delta * eps should have coefficient 12*a^2.

    f(a + delta + eps/2) = (a + delta + eps/2)^4
    f(a + delta - eps/2) = (a + delta - eps/2)^4

    Difference expanded:
        = 4*(a+delta)^3 * eps + (1/24)*24*eps^3
        = 4*(a^3 + 3*a^2*delta + 3*a*delta^2 + delta^3)*eps + eps^3

    The mixed term (linear in delta, linear in eps): 12*a^2 * delta * eps
    """
    # Analytical coefficient: the factor 2 from the bilinear expansion
    analytical_coefficient = 2.0

    # --- Numerical verification ---
    # For f(x) = x^4:
    # f(a + d + e/2) - f(a + d - e/2) = 4*(a+d)^3 * e + e^3
    # The mixed term (proportional to d*e) = 12*a^2*d*e
    # Extract this numerically by:
    #   diff(d, e) = f(a+d+e/2) - f(a+d-e/2)
    #   mixed_part = (diff(d, e) - diff(0, e)) / d  [at small d]
    #   expected_mixed_coefficient = 12*a^2 for the linear-in-e part

    a_test = 2.0
    eps_test = 1e-4
    delta_test = 1e-4

    # Full difference at (delta, eps)
    f_p_full = (a_test + delta_test + eps_test / 2.0) ** 4
    f_m_full = (a_test + delta_test - eps_test / 2.0) ** 4
    diff_full = f_p_full - f_m_full

    # Pure eps difference (delta = 0)
    f_p_pure = (a_test + eps_test / 2.0) ** 4
    f_m_pure = (a_test - eps_test / 2.0) ** 4
    diff_pure = f_p_pure - f_m_pure

    # Extract the delta-dependent part
    delta_dependent = diff_full - diff_pure

    # At leading order in delta, this should be 12*a^2 * delta * eps
    expected_mixed = 12.0 * a_test ** 2 * delta_test * eps_test
    residual = abs(delta_dependent - expected_mixed)
    rel_residual = residual / abs(expected_mixed) if abs(expected_mixed) > 1e-30 else 0.0

    numerical_passed = bool(rel_residual < 1e-4)

    return MixedQuadraticStructure(
        mixed_term_survives=True,
        analytical_coefficient=analytical_coefficient,
        numerical_verification_passed=numerical_passed,
        numerical_verification_max_residual=rel_residual,
        is_self_adjoint=True,
        notes=[
            "Mixed term survives: delta^2 S(eta_1,eta_1) - delta^2 S(eta_2,eta_2) "
            "= 2 * delta^2 S(h_+, h_-)",
            f"Analytical coefficient: {analytical_coefficient} (exact, from bilinearity)",
            f"Numerical verification: scalar model f(x)=x^4, a={a_test}",
            f"Expected mixed coefficient: 12*a^2 = {12.0 * a_test**2}",
            f"Numerical residual: {rel_residual:.2e}",
            f"Verification passed: {numerical_passed}",
            "Self-adjoint: delta^2 S(h_+, h_-) = delta^2 S(h_-, h_+)",
        ],
    )


# ================================================================
# Level 4: Induced Source Analysis
# ================================================================

def compute_t_tilde_radial(
    r: np.ndarray,
    phi_eq: np.ndarray,
    dphi_eq_dr: np.ndarray,
    f_profile: np.ndarray,
    df_dr: np.ndarray,
    m_squared: float,
) -> np.ndarray:
    """Compute the radial proxy for the scalar difference stress-energy.

    T_tilde(r) ~ Phi'_eq(r) * f'(r) + m^2 * Phi_eq(r) * f(r)

    This is a simplified radial proxy for the full T_tilde_mu_nu tensor,
    capturing the radial dependence of the induced source.
    The gradient-gradient term and the mass term are the two dominant
    contributions in the static, spherically symmetric sector.
    """
    return dphi_eq_dr * df_dr + m_squared * phi_eq * f_profile


def analyze_induced_source(
    params: RouteBMixedParams,
) -> InducedSourceAnalysis:
    """Analyze the source chain: IC -> Phi_- -> T_tilde -> h_- -> h_+ correction.

    The h_- equation of motion:
        G_hat(h_-) = -16*pi*G * T_tilde_mu_nu[Phi_-]

    where T_tilde is the scalar difference stress-energy:
        T_tilde_mu_nu = partial_mu Phi_eq * partial_nu Phi_-
                      + partial_mu Phi_- * partial_nu Phi_eq
                      - g_mu_nu [partial^a Phi_eq * partial_a Phi_-
                                 + m^2 * Phi_eq * Phi_-]

    This is bilinear in Phi_eq and Phi_-.

    Because Phi_- = A * exp(phi*t/tau) * f(r), and f(r) is an arbitrary
    IC-dependent spatial profile, T_tilde inherits this IC dependence.

    GENERAL STRUCTURAL ARGUMENT:
    Because T_tilde_mu_nu is bilinear in Phi_eq and Phi_-, and Phi_- carries
    an arbitrary IC-dependent spatial profile f(r), the induced mixed-channel
    support cannot define a unique geometric 1/r^2-type Component B term
    independently of initial data.  The formula
        T_tilde(r) ~ Phi'_eq(r) * f'(r) + m^2 * Phi_eq(r) * f(r)
    shows that different f(r) produce different T_tilde(r).  This is a
    structural consequence of the bilinear dependence on f(r), not an
    artifact of the two test profiles chosen.

    We verify this with two concrete IC profiles as numerical illustrations.
    """
    r = make_radial_grid(params)
    M = params.M
    m_sq = params.m_squared

    # Equilibrium scalar field
    phi_eq = M / r ** 2
    dphi_eq_dr = -2.0 * M / r ** 3

    # --- Profile 1: f(r) = 1/r ---
    f1 = 1.0 / r
    df1_dr = -1.0 / r ** 2
    t_tilde_1 = compute_t_tilde_radial(r, phi_eq, dphi_eq_dr, f1, df1_dr, m_sq)

    # --- Profile 2: f(r) = 1/r^2 ---
    f2 = 1.0 / r ** 2
    df2_dr = -2.0 / r ** 3
    t_tilde_2 = compute_t_tilde_radial(r, phi_eq, dphi_eq_dr, f2, df2_dr, m_sq)

    # Compute dominant scaling exponents via log-log regression at large r
    # Use the outer half of the grid (large r region)
    n_outer = params.n_r // 4
    r_outer = r[:n_outer]
    log_r_outer = np.log(r_outer)

    # Profile 1 large-r scaling
    t1_outer = np.abs(t_tilde_1[:n_outer])
    mask1 = t1_outer > 0
    if np.sum(mask1) > 2:
        log_t1 = np.log(t1_outer[mask1])
        lr1 = log_r_outer[mask1]
        slope1_large = float(np.polyfit(lr1, log_t1, 1)[0])
    else:
        slope1_large = -3.0  # fallback

    # Profile 2 large-r scaling
    t2_outer = np.abs(t_tilde_2[:n_outer])
    mask2 = t2_outer > 0
    if np.sum(mask2) > 2:
        log_t2 = np.log(t2_outer[mask2])
        lr2 = log_r_outer[mask2]
        slope2_large = float(np.polyfit(lr2, log_t2, 1)[0])
    else:
        slope2_large = -4.0  # fallback

    # Small-r scaling (inner quarter of grid)
    n_inner = params.n_r // 4
    r_inner = r[-n_inner:]
    log_r_inner = np.log(r_inner)

    # Profile 1 small-r scaling
    t1_inner = np.abs(t_tilde_1[-n_inner:])
    mask1i = t1_inner > 0
    if np.sum(mask1i) > 2:
        log_t1i = np.log(t1_inner[mask1i])
        lr1i = log_r_inner[mask1i]
        slope1_small = float(np.polyfit(lr1i, log_t1i, 1)[0])
    else:
        slope1_small = -5.0

    # Profile 2 small-r scaling
    t2_inner = np.abs(t_tilde_2[-n_inner:])
    mask2i = t2_inner > 0
    if np.sum(mask2i) > 2:
        log_t2i = np.log(t2_inner[mask2i])
        lr2i = log_r_inner[mask2i]
        slope2_small = float(np.polyfit(lr2i, log_t2i, 1)[0])
    else:
        slope2_small = -6.0

    # Do the profiles differ?
    profiles_differ = bool(abs(slope1_large - slope2_large) > 0.3)

    # Time growth exponent: Phi_- grows as exp(phi*t/tau),
    # T_tilde ~ Phi_eq * Phi_-, so grows as exp(phi*t/tau)
    # (bilinear in Phi_eq which is static and Phi_- which grows)
    time_growth = params.phi_golden / params.tau

    structural_arg = (
        "Because T_tilde is bilinear in Phi_eq and Phi_-, and Phi_- carries "
        "an arbitrary IC-dependent spatial profile f(r), the induced mixed-channel "
        "support cannot define a unique geometric 1/r^2-type Component B term "
        "independently of initial data.  The formula "
        "T_tilde(r) ~ Phi'_eq(r)*f'(r) + m^2*Phi_eq(r)*f(r) shows that "
        "different f(r) produce different T_tilde(r).  This is a structural "
        "consequence of the bilinear dependence on f(r)."
    )

    return InducedSourceAnalysis(
        source_chain_identified=True,
        h_minus_eom_is_linearized_einstein=True,
        source_is_t_tilde_phi_minus=True,
        t_tilde_is_bilinear_in_phi_eq_phi_minus=True,
        is_ghost_sourced=True,
        is_ic_dependent=True,
        is_time_dependent=True,
        time_growth_exponent=time_growth,
        profile_1_label="f(r) = 1/r",
        profile_1_dominant_scaling_large_r=slope1_large,
        profile_1_dominant_scaling_small_r=slope1_small,
        profile_2_label="f(r) = 1/r^2",
        profile_2_dominant_scaling_large_r=slope2_large,
        profile_2_dominant_scaling_small_r=slope2_small,
        profiles_differ=profiles_differ,
        structural_ic_dependence_argument=structural_arg,
        notes=[
            "Source chain: IC -> Phi_- -> T_tilde -> h_- -> h_+ correction",
            "h_- EOM: G_hat(h_-) = -16*pi*G * T_tilde[Phi_-]",
            "T_tilde is bilinear in Phi_eq and Phi_-",
            f"Profile 1 (f=1/r): large-r scaling ~ r^{slope1_large:.1f}, "
            f"small-r scaling ~ r^{slope1_small:.1f}",
            f"Profile 2 (f=1/r^2): large-r scaling ~ r^{slope2_large:.1f}, "
            f"small-r scaling ~ r^{slope2_small:.1f}",
            f"Profiles differ: {profiles_differ}",
            "Ghost-sourced: Phi_- has wrong-sign kinetic energy",
            f"Time-dependent: grows as exp({time_growth:.4f} * t)",
        ],
    )


# ================================================================
# Level 5: Shape Compatibility
# ================================================================

def assess_shape_compatibility(
    params: RouteBMixedParams,
) -> ShapeCompatibility:
    """Assess shape compatibility with Component B (1/r^2).

    The induced effective source has a radial profile that depends on
    the IC-dependent spatial profile f(r) of Phi_-.  Different ICs give
    different shapes.  Neither matches pure 1/r^2.

    STRUCTURAL ARGUMENT (not resting on two examples alone):
    T_tilde(r) ~ Phi'_eq(r)*f'(r) + m^2*Phi_eq(r)*f(r)
    is bilinear in f(r).  Since f(r) is arbitrary (IC-dependent), T_tilde
    cannot define a unique geometric 1/r^2 Component B term independently
    of initial data.  The two test profiles are numerical illustrations of
    this structural fact.
    """
    r = make_radial_grid(params)
    M = params.M
    m_sq = params.m_squared

    phi_eq = M / r ** 2
    dphi_eq_dr = -2.0 * M / r ** 3

    # Profile 1: f(r) = 1/r
    f1 = 1.0 / r
    df1_dr = -1.0 / r ** 2
    t1 = compute_t_tilde_radial(r, phi_eq, dphi_eq_dr, f1, df1_dr, m_sq)

    # Profile 2: f(r) = 1/r^2
    f2 = 1.0 / r ** 2
    df2_dr = -2.0 / r ** 3
    t2 = compute_t_tilde_radial(r, phi_eq, dphi_eq_dr, f2, df2_dr, m_sq)

    # Best-fit power-law exponent (over full grid)
    log_r = np.log(r)

    t1_abs = np.abs(t1)
    mask1 = t1_abs > 0
    if np.sum(mask1) > 2:
        fit1 = float(np.polyfit(log_r[mask1], np.log(t1_abs[mask1]), 1)[0])
    else:
        fit1 = -3.0

    t2_abs = np.abs(t2)
    mask2 = t2_abs > 0
    if np.sum(mask2) > 2:
        fit2 = float(np.polyfit(log_r[mask2], np.log(t2_abs[mask2]), 1)[0])
    else:
        fit2 = -4.0

    # Neither matches Component B exponent (-2.0)
    matches_b = bool(
        abs(fit1 - COMPONENT_B_SCALING) < 0.5
        and abs(fit2 - COMPONENT_B_SCALING) < 0.5
    )
    profiles_differ = bool(abs(fit1 - fit2) > 0.3)
    is_ic_dep = profiles_differ  # different ICs -> different shapes -> IC-dependent

    structural = (
        "Because T_tilde is bilinear in Phi_eq and Phi_-, and Phi_- carries "
        "an arbitrary IC-dependent spatial profile f(r), the induced effective "
        "source cannot define a unique geometric 1/r^2-type Component B term "
        "independently of initial data.  Different f(r) produce different "
        "T_tilde(r) — this is structural, not an artifact of the two test profiles."
    )

    return ShapeCompatibility(
        is_ic_dependent=is_ic_dep,
        matches_component_b=matches_b,
        radial_profiles_differ=profiles_differ,
        profile_1_best_fit_exponent=fit1,
        profile_2_best_fit_exponent=fit2,
        component_b_exponent=COMPONENT_B_SCALING,
        structural_argument=structural,
        notes=[
            f"Profile 1 (f=1/r): best-fit exponent = {fit1:.2f}",
            f"Profile 2 (f=1/r^2): best-fit exponent = {fit2:.2f}",
            f"Component B target exponent = {COMPONENT_B_SCALING}",
            f"Profiles differ: {profiles_differ}",
            f"Matches Component B: {matches_b}",
            f"IC-dependent: {is_ic_dep}",
            "Structural argument: bilinear dependence on arbitrary f(r) "
            "prevents unique geometric 1/r^2 closure",
        ],
    )


# ================================================================
# Level 6: Projection Sensitivity
# ================================================================

def assess_mixed_projection_sensitivity(
    params: RouteBMixedParams,
) -> MixedProjectionSensitivity:
    """Assess projection and CTP boundary sensitivity.

    PHYSICAL LIMIT (Phi_- -> 0, h_- -> 0):
    In the physical limit, Phi_- = 0.  Therefore T_tilde = 0.
    Therefore h_- = 0 (no source).  Therefore the mixed coupling
    delta^2 S(h_+, h_-) = 0.  The entire mixed contribution vanishes.

    CTP BOUNDARY (Phi_-(t_final) = 0):
    The CTP boundary condition requires Phi_-(t_final) = 0.
    This implies T_tilde(t_final) = 0, h_-(t_final) = 0, and the
    mixed contribution vanishes at the final time.

    The mixed channel exists only as pre-projection formal structure.
    """
    return MixedProjectionSensitivity(
        survives_physical_limit=False,
        survives_ctp_boundary=False,
        is_pre_projection_only=True,
        physical_limit_argument=(
            "Phi_- -> 0 implies T_tilde -> 0 implies h_- -> 0 implies "
            "delta^2 S(h_+, h_-) = 0.  Entire mixed contribution vanishes "
            "in the physical limit."
        ),
        ctp_boundary_argument=(
            "Phi_-(t_final) = 0 (CTP boundary condition) implies "
            "T_tilde(t_final) = 0, h_-(t_final) = 0.  Mixed contribution "
            "vanishes at the final time."
        ),
        notes=[
            "Physical limit: Phi_- -> 0 => T_tilde -> 0 => h_- -> 0 => "
            "mixed contribution = 0",
            "CTP boundary: Phi_-(t_final) = 0 => h_-(t_final) = 0",
            "Mixed channel exists only as pre-projection formal structure",
            "Both killing mechanisms are structural (follow from the "
            "formalism itself, not from specific parameter choices)",
        ],
    )


# ================================================================
# Level 7: Physical Admissibility
# ================================================================

def assess_mixed_physical_admissibility(
    params: RouteBMixedParams,
) -> MixedPhysicalAdmissibility:
    """Assess physical admissibility of the mixed channel.

    FOUR PATHOLOGY CHANNELS:

    1. IC-DEPENDENT: The spatial profile of the effective source depends on
       the IC-dependent spatial profile f(r) of Phi_-.  Because T_tilde is
       bilinear in Phi_eq and Phi_-, and Phi_- carries an arbitrary f(r),
       the induced support cannot define a unique geometric 1/r^2 Component B.

    2. GHOST-SOURCED: Phi_- has wrong-sign kinetic energy (scalar ghost,
       established in galley_truncation.py).  The mixed-channel source chain
       inherits this ghost character.

    3. CTP-KILLED: Phi_-(t_final) = 0 by the CTP boundary condition.
       This forces h_-(t_final) = 0 and kills the mixed contribution at
       the final time.

    4. PROJECTION-KILLED: In the physical limit Phi_- -> 0, h_- -> 0.
       The entire mixed contribution vanishes in the physical metric.

    These four pathologies jointly render the mixed channel non-promotable
    to a clean physical Component B mechanism within the tested perturbative
    Galley framework.
    """
    return MixedPhysicalAdmissibility(
        is_physically_admissible=False,
        n_pathology_channels=4,
        jointly_disqualifying=True,
        pathology_ic_dependent=True,
        pathology_ghost_sourced=True,
        pathology_ctp_killed=True,
        pathology_projection_killed=True,
        admissibility_scope=(
            "within_tested_perturbative_galley_framework"
        ),
        notes=[
            "IC-dependent: T_tilde depends on arbitrary f(r) of Phi_-; "
            "cannot define unique geometric 1/r^2 Component B",
            "Ghost-sourced: Phi_- has wrong-sign kinetic (scalar ghost)",
            "CTP-killed: Phi_-(t_final) = 0 forces h_-(t_final) = 0",
            "Projection-killed: Phi_- -> 0 implies entire mixed contribution -> 0",
            "Four pathologies JOINTLY render the mixed channel non-promotable "
            "to clean physical Component B within tested framework",
            "Scope: tested perturbative Galley CTP framework",
        ],
    )


# ================================================================
# Level 8: Classification
# ================================================================

def classify_mixed_channel(
    params: RouteBMixedParams,
) -> RouteBMixedClassification:
    """Classify the mixed channel result and update full Route B status.

    CLASSIFICATION:
      mixed_channel_insufficient_within_tested_galley_framework

    This closes the final tested classical Route B residue within the
    perturbative Galley CTP framework.

    Full Route B status (all 5 tested channels now classified):
    - Post-projection T^Phi: insufficient (pure 1/r^4) — UNCHANGED
    - Phi_-: pathological (ghost, IC-dependent, CTP-killed) — UNCHANGED
    - S_diss: vanishes in physical limit — UNCHANGED
    - g_- standalone diagonal: absent (CTP antisymmetry) — UNCHANGED
    - g_- mixed g_+ * g_-: insufficient within tested framework — NEW: CLOSED
    """
    return RouteBMixedClassification(
        classification=(
            "mixed_channel_insufficient_within_tested_galley_framework"
        ),
        post_projection_status="insufficient",
        phi_minus_status="pathological",
        s_diss_status="vanishes",
        gminus_diagonal_status="absent",
        gminus_mixed_status="insufficient_within_tested_framework",
        route_b_classical_channels_closed=True,
        all_tested_channels_classified=True,
        framework_scope="perturbative_galley_ctp_framework",
        recommended_next=(
            "Tested classical frontier closed.  Remaining avenues would "
            "require non-perturbative, non-Galley, or non-classical extensions."
        ),
        notes=[
            "Classification: mixed_channel_insufficient_within_tested_galley_framework",
            "Mixed channel is jointly disqualified by 4 pathologies: "
            "IC-dependent, ghost-sourced, CTP-killed, projection-killed",
            "All 5 tested classical Route B channels are now classified",
            "Route B classical frontier closed within tested framework",
            "Framework scope: perturbative Galley CTP framework",
            "Residue progression: 'full g_- sector uncomputed' -> "
            "'mixed channel only' -> 'mixed channel insufficient'",
            "Non-perturbative, non-Galley, or non-classical mechanisms "
            "remain outside the tested scope",
        ],
    )


# ================================================================
# Master function
# ================================================================

def compute_route_b_mixed_channel_assessment(
    params: Optional[RouteBMixedParams] = None,
) -> RouteBMixedResult:
    """Master computation: mixed g_+ * g_- channel analysis.

    Executes all analysis levels:
    1. Grid & baseline
    2. Mixed channel definition
    3. Mixed quadratic structure (Taylor expansion + numerical verification)
    4. Induced source analysis (source chain + IC-dependence)
    5. Shape compatibility (radial profiles + Component B comparison)
    6. Projection sensitivity (physical limit + CTP boundary)
    7. Physical admissibility (four pathology channels)
    8. Classification

    Returns the master result with all sub-results.
    """
    if params is None:
        params = RouteBMixedParams()

    # Level 2: Definition
    defn = define_mixed_channel(params)

    # Level 3: Quadratic Structure
    quad = derive_mixed_quadratic_structure(params)

    # Level 4: Induced Source
    source = analyze_induced_source(params)

    # Level 5: Shape Compatibility
    shape = assess_shape_compatibility(params)

    # Level 6: Projection Sensitivity
    proj = assess_mixed_projection_sensitivity(params)

    # Level 7: Physical Admissibility
    admis = assess_mixed_physical_admissibility(params)

    # Level 8: Classification
    cl = classify_mixed_channel(params)

    # Diagnostics
    diagnostics = {
        "mixed_term_survives": quad.mixed_term_survives,
        "analytical_coefficient": quad.analytical_coefficient,
        "numerical_verification_passed": quad.numerical_verification_passed,
        "numerical_verification_residual": quad.numerical_verification_max_residual,
        "profiles_differ": source.profiles_differ,
        "profile_1_scaling_large_r": source.profile_1_dominant_scaling_large_r,
        "profile_2_scaling_large_r": source.profile_2_dominant_scaling_large_r,
        "is_ic_dependent": source.is_ic_dependent,
        "is_ghost_sourced": source.is_ghost_sourced,
        "survives_physical_limit": proj.survives_physical_limit,
        "survives_ctp_boundary": proj.survives_ctp_boundary,
        "is_physically_admissible": admis.is_physically_admissible,
        "n_pathology_channels": admis.n_pathology_channels,
        "jointly_disqualifying": admis.jointly_disqualifying,
        "route_b_classical_channels_closed": cl.route_b_classical_channels_closed,
        "all_tested_channels_classified": cl.all_tested_channels_classified,
    }

    return RouteBMixedResult(
        valid=True,
        params=params,
        definition=defn,
        quadratic_structure=quad,
        induced_source=source,
        shape=shape,
        projection=proj,
        admissibility=admis,
        classification=cl,
        nonclaims=list(NONCLAIMS),
        assumptions=list(MIXED_ASSUMPTIONS),
        diagnostics=diagnostics,
    )


# ================================================================
# Serialization
# ================================================================

def route_b_mixed_result_to_dict(result: RouteBMixedResult) -> Dict[str, Any]:
    """Serialize RouteBMixedResult to a dictionary."""
    d: Dict[str, Any] = {}
    d["valid"] = result.valid

    # Definition
    defn = result.definition
    d["definition"] = {
        "object_name": defn.object_name,
        "is_bilinear": defn.is_bilinear,
        "is_self_adjoint": defn.is_self_adjoint,
        "is_only_surviving_quadratic": defn.is_only_surviving_quadratic,
        "diagonal_h_minus_squared_absent": defn.diagonal_h_minus_squared_absent,
        "perturbative_order": defn.perturbative_order,
    }

    # Quadratic Structure
    qs = result.quadratic_structure
    d["quadratic_structure"] = {
        "mixed_term_survives": qs.mixed_term_survives,
        "analytical_coefficient": qs.analytical_coefficient,
        "numerical_verification_passed": qs.numerical_verification_passed,
        "is_self_adjoint": qs.is_self_adjoint,
    }

    # Induced Source
    src = result.induced_source
    d["induced_source"] = {
        "source_chain_identified": src.source_chain_identified,
        "is_ghost_sourced": src.is_ghost_sourced,
        "is_ic_dependent": src.is_ic_dependent,
        "is_time_dependent": src.is_time_dependent,
        "profiles_differ": src.profiles_differ,
        "profile_1_scaling_large_r": src.profile_1_dominant_scaling_large_r,
        "profile_2_scaling_large_r": src.profile_2_dominant_scaling_large_r,
    }

    # Shape
    shp = result.shape
    d["shape"] = {
        "is_ic_dependent": shp.is_ic_dependent,
        "matches_component_b": shp.matches_component_b,
        "radial_profiles_differ": shp.radial_profiles_differ,
        "profile_1_best_fit_exponent": shp.profile_1_best_fit_exponent,
        "profile_2_best_fit_exponent": shp.profile_2_best_fit_exponent,
    }

    # Projection
    pr = result.projection
    d["projection"] = {
        "survives_physical_limit": pr.survives_physical_limit,
        "survives_ctp_boundary": pr.survives_ctp_boundary,
        "is_pre_projection_only": pr.is_pre_projection_only,
    }

    # Admissibility
    ad = result.admissibility
    d["admissibility"] = {
        "is_physically_admissible": ad.is_physically_admissible,
        "n_pathology_channels": ad.n_pathology_channels,
        "jointly_disqualifying": ad.jointly_disqualifying,
        "pathology_ic_dependent": ad.pathology_ic_dependent,
        "pathology_ghost_sourced": ad.pathology_ghost_sourced,
        "pathology_ctp_killed": ad.pathology_ctp_killed,
        "pathology_projection_killed": ad.pathology_projection_killed,
    }

    # Classification
    cl = result.classification
    d["classification"] = {
        "classification": cl.classification,
        "post_projection_status": cl.post_projection_status,
        "phi_minus_status": cl.phi_minus_status,
        "s_diss_status": cl.s_diss_status,
        "gminus_diagonal_status": cl.gminus_diagonal_status,
        "gminus_mixed_status": cl.gminus_mixed_status,
        "route_b_classical_channels_closed": cl.route_b_classical_channels_closed,
        "all_tested_channels_classified": cl.all_tested_channels_classified,
        "framework_scope": cl.framework_scope,
    }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions
    d["diagnostics"] = result.diagnostics

    return d
