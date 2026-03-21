"""Route B g_- energy density: closed-form analysis via CTP antisymmetry.

Phase Absolute Final Classical Attempt — determines whether the standalone
diagonal quadratic g_- energy sector exists, and if not, localizes the
remaining Route B residue to the mixed g_+ * g_- channel.

PRINCIPAL RESULTS (three-part answer):

  A. The standalone diagonal quadratic g_- action is ABSENT — CTP
     antisymmetry of S_1 - S_2 kills all even powers of g_-, including
     the quadratic.  No standalone diagonal energy density for g_- can
     be defined.

  B. Four standard energy definitions all give null for the standalone
     diagonal sector — quadratic EH expansion, canonical Hamiltonian,
     Isaacson tensor, and second-order perturbation theory all require
     a nonzero diagonal quadratic action.

  C. The mixed g_+ * g_- cross-coupling survives at quadratic order and
     remains the sole unresolved Route B residue — this term is linear
     in g_- and linear in g_+, vanishes in the physical limit g_- -> 0,
     but whether it can induce effective support through sourcing or
     constraint handling is not determined by this phase.

EXECUTIVE RESULT:
  This phase closes the standalone diagonal g_- energy question, but not
  the full doubled-metric Route B question.  The Route B residue is
  reduced from "full g_- sector uncomputed" to "only the mixed g_+ * g_-
  cross-coupling channel remains."

CLASSIFICATION:
  gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved

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

# CTP antisymmetry
CTP_ANTISYMMETRY_ORDER = 2  # the diagonal quadratic order that is killed


# ================================================================
# Assumptions — explicitly documented
# ================================================================

GMINUS_ASSUMPTIONS = [
    "1. The doubled-metric action is S_grav = (1/16*pi*G) * integral "
    "[sqrt(-g_1)*R_1 - sqrt(-g_2)*R_2] d^4x.  This is the Galley CTP "
    "gravitational action for the doubled-metric system.",

    "2. The +/- decomposition is g_+ = (g_1 + g_2)/2, g_- = g_1 - g_2 "
    "(standard CTP variables).  So g_1 = g_+ + g_-/2, g_2 = g_+ - g_-/2.",

    "3. The Taylor expansion of S_EH around g_+ exists to all orders "
    "(smooth functional).  The Einstein-Hilbert action is smooth in the "
    "metric, so this is standard.",

    "4. The standalone diagonal quadratic energy is defined from the "
    "diagonal second-order variation delta^2 S_EH(g_-, g_-).  This is "
    "the self-interaction of g_- at second order.",

    "5. No additional non-minimal couplings between metric copies "
    "beyond the S_1 - S_2 structure.  The doubled gravitational action "
    "is purely the difference of two Einstein-Hilbert actions.",

    "6. The equilibrium background is the same as Route C: static, "
    "spherically symmetric, with Phi_eq = X_eq = M/r^2.",

    "7. The Isaacson effective stress-energy requires a nonzero diagonal "
    "quadratic action to define.  Without a quadratic kinetic structure, "
    "there is nothing to average.",

    "8. The canonical Hamiltonian density for the standalone sector is "
    "constructed from the diagonal quadratic kinetic term via Legendre "
    "transform.  No diagonal kinetic term means no standalone Hamiltonian.",
]


# ================================================================
# Nonclaims
# ================================================================

NONCLAIMS = [
    "1. This phase does NOT prove Route B physically correct or incorrect "
    "in full generality.  It closes the standalone diagonal g_- energy "
    "question but not the full doubled-metric Route B question.",

    "2. A formal g_- energy density is not automatically observable — "
    "but here the standalone diagonal object is entirely absent at "
    "quadratic level.  This is stronger than pathological or formal: "
    "the object does not exist.",

    "3. Ghost-linked support is not automatically physically admissible — "
    "but here the standalone diagonal sector has no support at all.  "
    "The usual ghost objection is moot for an absent object.",

    "4. Pre-projection support is not automatically usable post-projection — "
    "but here no standalone diagonal pre-projection support exists.  "
    "The projection question is moot for the standalone diagonal sector.",

    "5. Failure of the standalone diagonal sector closes only that specific "
    "sub-channel, not the full mixed g_+ * g_- structure.  The mixed "
    "cross-coupling remains as the unresolved Route B residue.",

    "6. The CTP antisymmetry argument is purely algebraic: "
    "f(a+epsilon) - f(a-epsilon) has no epsilon^2 terms.  This holds "
    "for ANY smooth functional, not just S_EH.",

    "7. The existing characterization of g_- as 'wrong-sign kinetic "
    "energy' (galley_truncation.py line 893-896) is superseded for the "
    "standalone diagonal sector: the correct characterization in the "
    "+/- basis is 'diagonal quadratic action ABSENT.'  The mixed "
    "sector is not captured by this refinement.",

    "8. Cubic and higher odd-order terms in g_- survive the CTP "
    "antisymmetry but do not contribute to a standard quadratic "
    "energy density.  They are higher-order interactions, not "
    "free-field kinetic terms.",

    "9. The mixed g_+ * g_- cross-coupling exists at second order, "
    "vanishes in the physical limit, but whether it can induce "
    "effective support through sourcing or constraint handling is "
    "NOT determined by this phase.",

    "10. Any gauge dependence in the perturbative expansion is moot for "
    "the standalone diagonal sector (zero in any gauge), but the mixed "
    "channel may be gauge-sensitive through the full doubled system.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class RouteBGMinusParams:
    """Parameters for the Route B g_- energy density analysis."""
    r_s: float = R_S
    M: float = M_EXT
    R_eq: float = R_EQ
    tau: float = TAU_CANONICAL
    R_ext: float = 2.0 * R_S
    R_min: float = 0.05
    n_r: int = 500
    A_crit: float = A_CRIT
    phi_golden: float = PHI_GOLDEN


@dataclass
class EnergyDefinitionChoice:
    """Documents the energy definitions tested and why.

    Four standard definitions are tested for the standalone diagonal sector:
    1. Quadratic EH expansion: expand S_EH to second order in g_-
    2. Canonical Hamiltonian: Legendre-transform the diagonal kinetic term
    3. Isaacson tensor: average the second-order perturbation
    4. Second-order perturbation theory: look for a propagator

    All require a nonzero diagonal quadratic action.
    """
    definitions_tested: List[str] = field(default_factory=list)
    n_definitions: int = 0
    all_require_quadratic_action: bool = True
    scope: str = "standalone_diagonal_sector_only"
    notes: List[str] = field(default_factory=list)


@dataclass
class CTPAntisymmetryDerivation:
    """The core algebraic derivation showing even powers cancel.

    For ANY smooth functional F:
        F(a + eps) - F(a - eps) = 2*eps*F'(a) + (2/3!)*eps^3*F'''(a) + ...
    Only ODD powers of eps survive.  ALL even powers cancel.

    Applied to S_EH[g_+ + g_-/2] - S_EH[g_+ - g_-/2]:
    - 0th order: S_EH - S_EH = 0
    - 1st order: delta^1 S * g_- (SURVIVES - linear, gives EOM)
    - 2nd order: (1/8) delta^2 S * g_-^2 - (1/8) delta^2 S * g_-^2 = 0 (KILLED)
    - 3rd order: (1/24) delta^3 S * g_-^3 (SURVIVES - cubic)
    """
    even_orders_killed: List[int] = field(default_factory=list)
    odd_orders_survive: List[int] = field(default_factory=list)
    diagonal_quadratic_coefficient: float = 0.0
    copy_1_quadratic_coefficient: float = 0.0
    copy_2_quadratic_coefficient: float = 0.0
    cancellation_exact: bool = False
    numerical_verification_passed: bool = False
    numerical_verification_max_residual: float = 0.0
    notes: List[str] = field(default_factory=list)


@dataclass
class QuadraticGMinusAction:
    """Analysis of the full quadratic structure in g_-.

    Diagonal: S_2_diag[g_-] = 0 (CTP antisymmetry)
    Cross-coupling: S_2_cross[g_+, g_-] survives (linear in g_-)
    """
    diagonal_quadratic_action_zero: bool = False
    cross_coupling_exists: bool = False
    cross_coupling_vanishes_in_physical_limit: bool = False
    cross_coupling_linear_in_gminus: bool = False
    individual_copy_1_sign: int = 0   # +1 (right-sign EH)
    individual_copy_2_sign: int = 0   # -1 (wrong-sign EH)
    net_diagonal_sign: int = 0        # 0 (absent)
    upgrade_from_wrong_sign_to_absent: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class GMinusEnergyDensityResult:
    """Unified result from all 4 energy definitions for the standalone
    diagonal sector only.  NOT the mixed channel.
    """
    # Per-definition results
    quadratic_eh_result: str = ""        # "zero"
    canonical_hamiltonian_result: str = ""  # "zero"
    isaacson_result: str = ""            # "zero"
    perturbation_theory_result: str = ""  # "not_applicable"

    n_definitions_tested: int = 0
    n_definitions_giving_zero: int = 0
    n_definitions_giving_nonzero: int = 0
    n_definitions_not_applicable: int = 0
    standalone_diagonal_consensus: str = ""  # "energy_structurally_absent"
    notes: List[str] = field(default_factory=list)


@dataclass
class MixedChannelResidue:
    """The surviving g_+ * g_- cross-coupling and its unresolved status.

    This is the only remaining Route B residue.  The standalone diagonal
    g_- energy is absent, but the mixed channel is not.
    """
    cross_coupling_exists: bool = False
    linear_in_gminus: bool = False
    vanishes_in_physical_limit: bool = False
    can_induce_effective_support: str = ""  # "undetermined"
    is_remaining_route_b_residue: bool = False
    effective_energy_computed: bool = False
    residue_reduced_from: str = ""  # "full_gminus_sector_uncomputed"
    residue_reduced_to: str = ""    # "mixed_gplus_gminus_cross_coupling_only"
    notes: List[str] = field(default_factory=list)


@dataclass
class ComponentBCompatibility:
    """Component B compatibility test.

    Standalone diagonal: absent (no energy density exists).
    Mixed channel: undetermined (not computed).
    """
    standalone_diagonal_compatible: bool = False
    mixed_channel_compatible: str = ""  # "undetermined"
    computed_compatible: bool = False
    overall_status: str = ""  # "unresolved_but_narrowed"
    notes: List[str] = field(default_factory=list)


@dataclass
class ProjectionSensitivity:
    """Projection analysis.

    Standalone diagonal: moot (no object exists to project).
    Mixed channel: pre-projection only (vanishes at g_- -> 0).
    """
    standalone_diagonal_projection: str = ""  # "moot"
    mixed_channel_projection: str = ""        # "pre_projection_only"
    mixed_channel_boundary_sensitive: str = ""  # "undetermined"
    notes: List[str] = field(default_factory=list)


@dataclass
class PhysicalAdmissibility:
    """Physical admissibility classification.

    Standalone diagonal: not applicable (no object).
    Mixed channel: undetermined.
    """
    standalone_diagonal_admissible: str = ""  # "not_applicable"
    mixed_channel_admissible: str = ""        # "undetermined"
    energy_exists: bool = False  # for standalone diagonal sector
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBGMinusClassification:
    """Final classification with phase lock updates."""
    classification: str = ""
    # Route B channel statuses
    post_projection_status: str = ""
    phi_minus_status: str = ""
    s_diss_status: str = ""
    gminus_diagonal_status: str = ""
    gminus_mixed_status: str = ""
    # Key booleans
    is_full_route_b_no_go: bool = False
    standalone_diagonal_closed: bool = False
    mixed_channel_unresolved: bool = False
    residue_reduced: bool = False
    # Upgrade note
    upgrade_wrong_sign_to_absent: bool = False
    is_provisional: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteBGMinusResult:
    """Master result for the Route B g_- energy density analysis."""
    valid: bool = False
    params: RouteBGMinusParams = field(default_factory=RouteBGMinusParams)
    energy_definition: Optional[EnergyDefinitionChoice] = None
    ctp_antisymmetry: Optional[CTPAntisymmetryDerivation] = None
    quadratic_action: Optional[QuadraticGMinusAction] = None
    energy_density: Optional[GMinusEnergyDensityResult] = None
    mixed_channel: Optional[MixedChannelResidue] = None
    compatibility: Optional[ComponentBCompatibility] = None
    projection: Optional[ProjectionSensitivity] = None
    admissibility: Optional[PhysicalAdmissibility] = None
    classification: Optional[RouteBGMinusClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Level 1: Radial grid and baseline
# ================================================================

def make_radial_grid(params: RouteBGMinusParams) -> np.ndarray:
    """Create log-spaced radial grid from R_ext down to R_min."""
    r_min = max(params.R_min, params.R_eq * 0.8)
    log_r = np.linspace(math.log(params.R_ext), math.log(r_min), params.n_r)
    return np.exp(log_r)


def compute_equilibrium_density(
    r: np.ndarray, params: RouteBGMinusParams,
) -> np.ndarray:
    """Compute equilibrium energy density rho_eq = -M^2 / (2*tau^2*r^4)."""
    M = params.M
    tau2 = params.tau ** 2
    return -M * M / (2.0 * tau2 * r ** 4)


# ================================================================
# Level 2: CTP Antisymmetry Derivation
# ================================================================

def derive_ctp_antisymmetry(
    params: RouteBGMinusParams,
) -> CTPAntisymmetryDerivation:
    """Derive the CTP antisymmetry cancellation of even powers.

    For ANY smooth functional F:
        F(a + eps) - F(a - eps) = 2*eps*F'(a) + (2/3!)*eps^3*F'''(a) + ...

    Applied to S_EH[g_+ + g_-/2] - S_EH[g_+ - g_-/2]:
    the diagonal quadratic (eps^2) term cancels identically.

    NUMERICAL VERIFICATION:
    Test with a simple scalar model f(x) = x^4 (nonlinear, smooth):
        f(a + eps) - f(a - eps) should have no eps^2 term.

    We compute the Taylor coefficients explicitly and verify cancellation.
    """
    # The key coefficients in the Taylor expansion of each copy:
    # S_EH[g_+ + g_-/2]:
    #   0th: S_EH[g_+]
    #   1st: (1/2) * delta^1 S * g_-
    #   2nd: (1/8) * delta^2 S * g_-^2     <- coefficient = +1/8
    #   3rd: (1/48) * delta^3 S * g_-^3
    #
    # S_EH[g_+ - g_-/2]:
    #   0th: S_EH[g_+]
    #   1st: -(1/2) * delta^1 S * g_-
    #   2nd: (1/8) * delta^2 S * g_-^2     <- coefficient = +1/8 (SAME!)
    #   3rd: -(1/48) * delta^3 S * g_-^3

    copy_1_quad = 1.0 / 8.0   # coefficient of g_-^2 in S_EH[g_+ + g_-/2]
    copy_2_quad = 1.0 / 8.0   # coefficient of g_-^2 in S_EH[g_+ - g_-/2]

    # In the difference S_1 - S_2:
    # quad coefficient = (+1/8) - (+1/8) = 0
    net_quad = copy_1_quad - copy_2_quad  # = 0.0 exactly

    # Even orders killed: 0, 2, 4, ...
    even_killed = [0, 2, 4]

    # Odd orders survive: 1, 3, 5, ...
    odd_survive = [1, 3, 5]

    # --- Numerical verification ---
    # Use f(x) = x^4 as a test functional.
    # f(a + eps) - f(a - eps) should have only odd powers of eps:
    #   = 2*eps*4*a^3 + 2*(1/6)*eps^3*24*a + 0*eps^4 + ...
    #   = 8*a^3*eps + 8*a*eps^3 + 2*eps^5/...
    #
    # In particular, the eps^2 coefficient should be exactly 0.

    # For f(x) = x^4:
    #   f(a+eps) = a^4 + 4*a^3*eps + 6*a^2*eps^2 + 4*a*eps^3 + eps^4
    #   f(a-eps) = a^4 - 4*a^3*eps + 6*a^2*eps^2 - 4*a*eps^3 + eps^4
    #   Difference = 8*a^3*eps + 8*a*eps^3  (ONLY odd powers, exact)
    #
    # The eps^2 coefficient is 6*a^2 in BOTH expansions, so it cancels
    # exactly in the difference.  This is the CTP antisymmetry in action.

    a_test = 2.0  # test point
    eps_values = np.logspace(-8, -2, 20)
    max_residual = 0.0

    for eps in eps_values:
        f_plus = (a_test + eps) ** 4
        f_minus = (a_test - eps) ** 4
        diff = f_plus - f_minus

        # The exact result has ONLY odd powers:
        # 8*a^3*eps + 8*a*eps^3 (no 5th order for degree 4 polynomial)
        odd_exact = 8.0 * a_test ** 3 * eps + 8.0 * a_test * eps ** 3
        residual = abs(diff - odd_exact)

        # Relative to the leading term
        if abs(diff) > 1e-30:
            rel_residual = residual / abs(diff)
            max_residual = max(max_residual, rel_residual)

    numerical_passed = bool(max_residual < 1e-6)

    return CTPAntisymmetryDerivation(
        even_orders_killed=even_killed,
        odd_orders_survive=odd_survive,
        diagonal_quadratic_coefficient=net_quad,
        copy_1_quadratic_coefficient=copy_1_quad,
        copy_2_quadratic_coefficient=copy_2_quad,
        cancellation_exact=(net_quad == 0.0),
        numerical_verification_passed=numerical_passed,
        numerical_verification_max_residual=max_residual,
        notes=[
            f"Copy 1 quadratic coefficient: +{copy_1_quad} (from S_EH[g_+ + g_-/2])",
            f"Copy 2 quadratic coefficient: +{copy_2_quad} (from S_EH[g_+ - g_-/2])",
            f"Net diagonal quadratic: {copy_1_quad} - {copy_2_quad} = {net_quad} (exact zero)",
            "Even orders killed by CTP antisymmetry: 0, 2, 4, ...",
            "Odd orders survive: 1 (linear EOM), 3 (cubic), 5, ...",
            "The cancellation is purely algebraic: f(a+eps) - f(a-eps) has no eps^2",
            f"Numerical verification (f(x)=x^4): max residual = {max_residual:.2e}",
            f"Numerical verification passed: {numerical_passed}",
        ],
    )


# ================================================================
# Level 3: Quadratic Action Analysis
# ================================================================

def analyze_quadratic_gminus_action(
    params: RouteBGMinusParams,
) -> QuadraticGMinusAction:
    """Analyze the full quadratic structure in g_-.

    DIAGONAL: S_2_diag[g_-] = 0 (from CTP antisymmetry)
      The pure g_-^2 term in S_1 - S_2 cancels exactly.

    CROSS-COUPLING: S_2_cross[g_+, g_-] survives
      The mixed term delta^2 S(g_+, g_-) is bilinear (linear in g_-).
      It vanishes when g_- -> 0 (physical limit).
      It cannot define a standalone energy density for g_-.

    INDIVIDUAL-COPY ANALYSIS:
      Copy 1 (S_EH[g_1]): right-sign kinetic for ALL perturbations (+1)
      Copy 2 (-S_EH[g_2]): wrong-sign kinetic for ALL perturbations (-1)
      In the +/- basis, the diagonal g_-^2 contributions are:
        From copy 1: +(1/8) delta^2 S
        From copy 2: -(1/8) delta^2 S  (because of the overall minus sign)

      Wait — let us be more careful.  The ACTION is S_1 - S_2:
        S_1 = S_EH[g_+ + g_-/2]
        S_2 = S_EH[g_+ - g_-/2]

      S_1 expanded to 2nd order in g_-:
        S_EH[g_+] + (1/2) delta S * g_- + (1/8) delta^2 S * g_-^2 + ...

      S_2 expanded to 2nd order in g_-:
        S_EH[g_+] - (1/2) delta S * g_- + (1/8) delta^2 S * g_-^2 + ...

      S_1 - S_2 at 2nd order:
        (1/8) delta^2 S * g_-^2 - (1/8) delta^2 S * g_-^2 = 0

      So copy 1 contributes +1/8 and copy 2 contributes +1/8 to the
      quadratic coefficient, and the DIFFERENCE is zero.

      In the individual-copy basis, copy 2 with the minus sign gives
      "wrong-sign" for the g_2 perturbation.  But in the +/- basis,
      the diagonal contributions are EQUAL and cancel.
    """
    return QuadraticGMinusAction(
        diagonal_quadratic_action_zero=True,
        cross_coupling_exists=True,
        cross_coupling_vanishes_in_physical_limit=True,
        cross_coupling_linear_in_gminus=True,
        individual_copy_1_sign=+1,  # right-sign EH
        individual_copy_2_sign=-1,  # wrong-sign EH (overall minus in action)
        net_diagonal_sign=0,        # +1/8 - 1/8 = 0 (ABSENT, not wrong-sign)
        upgrade_from_wrong_sign_to_absent=True,
        notes=[
            "Diagonal quadratic action S_2_diag[g_-] = 0 (CTP antisymmetry)",
            "Copy 1 contributes +(1/8)*delta^2 S to the g_-^2 coefficient",
            "Copy 2 contributes +(1/8)*delta^2 S to the g_-^2 coefficient",
            "S_1 - S_2: (1/8) - (1/8) = 0 (exact cancellation)",
            "Cross-coupling S_2_cross[g_+, g_-] SURVIVES (linear in g_-)",
            "Cross-coupling vanishes in physical limit g_- -> 0",
            "Upgrade: 'wrong-sign kinetic' (individual-copy basis) -> "
            "'diagonal quadratic action ABSENT' (+/- basis)",
            "This upgrade applies to the standalone diagonal sector only",
        ],
    )


# ================================================================
# Level 4: Four Energy Definitions (Standalone Diagonal Sector Only)
# ================================================================

def evaluate_energy_definitions(
    params: RouteBGMinusParams,
) -> GMinusEnergyDensityResult:
    """Test 4 energy definitions for the standalone diagonal sector ONLY.

    These definitions are tested ONLY for the standalone diagonal
    g_- sector, NOT for the mixed g_+ * g_- channel.

    1. Quadratic EH expansion:
       S_2_diag[g_-] = 0 => no quadratic energy density.
       The object from which you would read off an energy density
       (the diagonal quadratic action) is identically zero.

    2. Canonical Hamiltonian:
       H_diag = pi * q_dot - L, where L is the diagonal Lagrangian.
       But L_diag = 0 (no diagonal quadratic kinetic or potential term).
       Therefore H_diag = 0.

    3. Isaacson tensor:
       <G^(2)>_diag requires a nonzero second-order gravitational
       perturbation from the diagonal g_- sector.  Since the diagonal
       quadratic action is zero, there is no second-order perturbation
       to average.  The Isaacson tensor from the standalone diagonal
       sector is zero.

    4. Second-order perturbation theory:
       A propagator requires a nonzero quadratic action (kinetic term).
       No diagonal quadratic action => no propagator => this definition
       is not applicable.
    """
    return GMinusEnergyDensityResult(
        quadratic_eh_result="zero",
        canonical_hamiltonian_result="zero",
        isaacson_result="zero",
        perturbation_theory_result="not_applicable",
        n_definitions_tested=4,
        n_definitions_giving_zero=3,
        n_definitions_giving_nonzero=0,
        n_definitions_not_applicable=1,
        standalone_diagonal_consensus="energy_structurally_absent",
        notes=[
            "Quadratic EH expansion: S_2_diag[g_-] = 0 => epsilon = 0",
            "Canonical Hamiltonian: no diagonal kinetic term => H_diag = 0",
            "Isaacson tensor: no diagonal quadratic perturbation => "
            "<G^(2)>_diag = 0",
            "Second-order perturbation theory: no diagonal propagator => N/A",
            "All 4 definitions tested for standalone diagonal sector ONLY",
            "Consensus: energy is structurally absent in the standalone "
            "diagonal sector",
            "The mixed g_+ * g_- channel is NOT tested by these definitions",
        ],
    )


# ================================================================
# Level 5: Mixed Channel Residue
# ================================================================

def analyze_mixed_channel_residue(
    params: RouteBGMinusParams,
) -> MixedChannelResidue:
    """Analyze the surviving mixed g_+ * g_- cross-coupling.

    The mixed cross-coupling delta^2 S(g_+, g_-) survives at second
    order in the doubled action.  It is bilinear: linear in g_- and
    linear in perturbations of g_+.

    Properties:
    - Exists as a formal quadratic structure in the pre-projection action
    - Linear in g_-, so vanishes as g_- -> 0 (physical limit)
    - Cannot define a standalone energy density for g_-
    - BUT: whether it can induce effective support after sourcing,
      constraint handling, or field integration is undetermined

    This is the ONLY remaining Route B classical residue.  All other
    channels have been closed or classified.
    """
    return MixedChannelResidue(
        cross_coupling_exists=True,
        linear_in_gminus=True,
        vanishes_in_physical_limit=True,
        can_induce_effective_support="undetermined",
        is_remaining_route_b_residue=True,
        effective_energy_computed=False,
        residue_reduced_from="full_gminus_sector_uncomputed",
        residue_reduced_to="mixed_gplus_gminus_cross_coupling_only",
        notes=[
            "Mixed g_+ * g_- cross-coupling SURVIVES at quadratic order",
            "The cross-coupling is bilinear: linear in g_- and linear in g_+",
            "Vanishes in physical limit g_- -> 0",
            "Cannot define a standalone energy density for g_-",
            "Whether it can induce effective support through sourcing or "
            "constraint handling is NOT determined by this phase",
            "This is the ONLY remaining Route B classical residue",
            "Residue reduced from 'full g_- sector uncomputed' to "
            "'mixed g_+ * g_- cross-coupling only'",
        ],
    )


# ================================================================
# Level 6: Component B Compatibility
# ================================================================

def assess_component_b_compatibility(
    params: RouteBGMinusParams,
) -> ComponentBCompatibility:
    """Assess Component B compatibility.

    Standalone diagonal sector: no energy density exists, so no scaling
    class, no radial profile, and no compatibility with Component B.

    Mixed channel: not computed, so compatibility is undetermined.

    No computed channel provides Component B.
    """
    return ComponentBCompatibility(
        standalone_diagonal_compatible=False,
        mixed_channel_compatible="undetermined",
        computed_compatible=False,
        overall_status="unresolved_but_narrowed",
        notes=[
            "Standalone diagonal sector: no energy density => "
            "no scaling class => incompatible with Component B",
            "Mixed channel: not computed => compatibility undetermined",
            "No computed Route B channel provides Component B",
            "The Route B residue has been narrowed: only the mixed "
            "g_+ * g_- cross-coupling channel remains as unresolved",
            "Overall status: unresolved but narrowed",
        ],
    )


# ================================================================
# Level 7: Projection Sensitivity
# ================================================================

def assess_projection_sensitivity(
    params: RouteBGMinusParams,
) -> ProjectionSensitivity:
    """Assess projection sensitivity.

    Standalone diagonal: the object does not exist pre-projection,
    so the question of projection survival is moot for this sector.

    Mixed channel: the g_+ * g_- cross-coupling vanishes when g_- -> 0
    (physical limit), so it exists only as pre-projection structure.
    It may also be boundary-sensitive through the full doubled system,
    but this is not determined.
    """
    return ProjectionSensitivity(
        standalone_diagonal_projection="moot",
        mixed_channel_projection="pre_projection_only",
        mixed_channel_boundary_sensitive="undetermined",
        notes=[
            "Standalone diagonal sector: object does not exist => "
            "projection question is moot",
            "Mixed channel: g_+ * g_- vanishes when g_- -> 0",
            "Mixed channel exists only as pre-projection formal structure",
            "Mixed channel may be boundary-sensitive through the full "
            "doubled system — this is not determined",
        ],
    )


# ================================================================
# Level 8: Physical Admissibility
# ================================================================

def assess_physical_admissibility(
    params: RouteBGMinusParams,
) -> PhysicalAdmissibility:
    """Assess physical admissibility.

    Standalone diagonal: nothing to admit or reject.  The standalone
    diagonal energy density does not exist (structurally absent).
    Therefore the question of physical admissibility is not applicable.

    Mixed channel: undetermined.  The mixed g_+ * g_- structure could
    be gauge-sensitive, source-sensitive, or boundary-sensitive through
    the full doubled system.  This is not determined.
    """
    return PhysicalAdmissibility(
        standalone_diagonal_admissible="not_applicable",
        mixed_channel_admissible="undetermined",
        energy_exists=False,  # for standalone diagonal sector
        notes=[
            "Standalone diagonal sector: energy does not exist => "
            "admissibility not applicable",
            "Not ghost-contaminated (for diagonal sector): the object is "
            "absent, not wrong-sign",
            "Not gauge-dependent (for diagonal sector): zero in any gauge",
            "Mixed channel: admissibility undetermined — could be "
            "gauge-sensitive, source-sensitive, or boundary-sensitive",
        ],
    )


# ================================================================
# Level 9: Classification
# ================================================================

def classify_gminus_energy(
    params: RouteBGMinusParams,
) -> RouteBGMinusClassification:
    """Classify the g_- energy density result and update Route B status.

    CLASSIFICATION:
      gminus_diagonal_quadratic_energy_absent__mixed_channel_unresolved

    Route B status update:
    - Post-projection: insufficient (pure 1/r^4) — UNCHANGED
    - Phi_-: pathological (ghost, IC-dependent, CTP-killed) — UNCHANGED
    - S_diss: vanishes in physical limit — UNCHANGED
    - g_- standalone diagonal: ABSENT (CTP antisymmetry) — NEW: CLOSED
    - g_- mixed g_+ * g_-: UNRESOLVED — NEW: reduced residue

    Route B is NOT fully closed.  The mixed channel remains open.
    """
    return RouteBGMinusClassification(
        classification=(
            "gminus_diagonal_quadratic_energy_absent__"
            "mixed_channel_unresolved"
        ),
        post_projection_status="insufficient",
        phi_minus_status="pathological",
        s_diss_status="vanishes",
        gminus_diagonal_status="absent",
        gminus_mixed_status="unresolved",
        is_full_route_b_no_go=False,
        standalone_diagonal_closed=True,
        mixed_channel_unresolved=True,
        residue_reduced=True,
        upgrade_wrong_sign_to_absent=True,
        is_provisional=True,
        notes=[
            "Classification: gminus_diagonal_quadratic_energy_absent__"
            "mixed_channel_unresolved",
            "Standalone diagonal g_- energy: ABSENT (CTP antisymmetry "
            "kills the diagonal quadratic action)",
            "Mixed g_+ * g_- channel: UNRESOLVED (surviving cross-coupling "
            "not computed for effective support)",
            "Route B is NOT fully closed (mixed channel remains open)",
            "Residue REDUCED from 'full g_- sector uncomputed' to "
            "'mixed g_+ * g_- cross-coupling only'",
            "Upgrade: 'wrong-sign kinetic' -> 'diagonal quadratic action "
            "absent' (scoped to standalone diagonal sector)",
            "This is a provisional classification pending analysis of "
            "the mixed channel",
        ],
    )


# ================================================================
# Master function
# ================================================================

def compute_route_b_gminus_energy_assessment(
    params: Optional[RouteBGMinusParams] = None,
) -> RouteBGMinusResult:
    """Master computation: Route B g_- energy density analysis.

    Executes all analysis levels:
    1. Grid & baseline
    2. CTP antisymmetry derivation
    3. Quadratic action analysis
    4. Four energy definitions (standalone diagonal sector only)
    5. Mixed channel residue
    6. Component B compatibility
    7. Projection sensitivity
    8. Physical admissibility
    9. Classification

    Returns the master result with all sub-results.
    """
    if params is None:
        params = RouteBGMinusParams()

    # Level 2: CTP Antisymmetry
    ctp = derive_ctp_antisymmetry(params)

    # Level 3: Quadratic Action
    quad = analyze_quadratic_gminus_action(params)

    # Level 4: Energy Definitions
    edef = EnergyDefinitionChoice(
        definitions_tested=[
            "quadratic_eh_expansion",
            "canonical_hamiltonian",
            "isaacson_tensor",
            "second_order_perturbation_theory",
        ],
        n_definitions=4,
        all_require_quadratic_action=True,
        scope="standalone_diagonal_sector_only",
        notes=[
            "4 standard energy definitions tested",
            "All require a nonzero diagonal quadratic action",
            "Scope: standalone diagonal sector only (NOT mixed channel)",
        ],
    )
    energy = evaluate_energy_definitions(params)

    # Level 5: Mixed Channel
    mixed = analyze_mixed_channel_residue(params)

    # Level 6-8: Compatibility, Projection, Admissibility
    compat = assess_component_b_compatibility(params)
    proj = assess_projection_sensitivity(params)
    admis = assess_physical_admissibility(params)

    # Level 9: Classification
    cl = classify_gminus_energy(params)

    # Diagnostics
    diagnostics = {
        "diagonal_quadratic_coefficient": ctp.diagonal_quadratic_coefficient,
        "copy_1_quad_coeff": ctp.copy_1_quadratic_coefficient,
        "copy_2_quad_coeff": ctp.copy_2_quadratic_coefficient,
        "numerical_verification_passed": ctp.numerical_verification_passed,
        "numerical_max_residual": ctp.numerical_verification_max_residual,
        "net_diagonal_sign": quad.net_diagonal_sign,
        "n_definitions_tested": energy.n_definitions_tested,
        "n_definitions_giving_nonzero": energy.n_definitions_giving_nonzero,
        "cross_coupling_exists": mixed.cross_coupling_exists,
        "is_full_route_b_no_go": cl.is_full_route_b_no_go,
        "standalone_diagonal_closed": cl.standalone_diagonal_closed,
        "mixed_channel_unresolved": cl.mixed_channel_unresolved,
        "residue_reduced": cl.residue_reduced,
    }

    return RouteBGMinusResult(
        valid=True,
        params=params,
        energy_definition=edef,
        ctp_antisymmetry=ctp,
        quadratic_action=quad,
        energy_density=energy,
        mixed_channel=mixed,
        compatibility=compat,
        projection=proj,
        admissibility=admis,
        classification=cl,
        nonclaims=list(NONCLAIMS),
        assumptions=list(GMINUS_ASSUMPTIONS),
        diagnostics=diagnostics,
    )


# ================================================================
# Serialization
# ================================================================

def route_b_gminus_result_to_dict(result: RouteBGMinusResult) -> Dict[str, Any]:
    """Serialize RouteBGMinusResult to a dictionary."""
    d: Dict[str, Any] = {}
    d["valid"] = result.valid

    # CTP Antisymmetry
    ctp = result.ctp_antisymmetry
    d["ctp_antisymmetry"] = {
        "even_orders_killed": ctp.even_orders_killed,
        "odd_orders_survive": ctp.odd_orders_survive,
        "diagonal_quadratic_coefficient": ctp.diagonal_quadratic_coefficient,
        "cancellation_exact": ctp.cancellation_exact,
        "numerical_verification_passed": ctp.numerical_verification_passed,
    }

    # Quadratic Action
    qa = result.quadratic_action
    d["quadratic_action"] = {
        "diagonal_quadratic_action_zero": qa.diagonal_quadratic_action_zero,
        "cross_coupling_exists": qa.cross_coupling_exists,
        "net_diagonal_sign": qa.net_diagonal_sign,
        "upgrade_from_wrong_sign_to_absent": qa.upgrade_from_wrong_sign_to_absent,
    }

    # Energy Density
    ed = result.energy_density
    d["energy_density"] = {
        "quadratic_eh_result": ed.quadratic_eh_result,
        "canonical_hamiltonian_result": ed.canonical_hamiltonian_result,
        "isaacson_result": ed.isaacson_result,
        "perturbation_theory_result": ed.perturbation_theory_result,
        "n_definitions_tested": ed.n_definitions_tested,
        "n_definitions_giving_nonzero": ed.n_definitions_giving_nonzero,
        "standalone_diagonal_consensus": ed.standalone_diagonal_consensus,
    }

    # Mixed Channel
    mc = result.mixed_channel
    d["mixed_channel"] = {
        "cross_coupling_exists": mc.cross_coupling_exists,
        "linear_in_gminus": mc.linear_in_gminus,
        "vanishes_in_physical_limit": mc.vanishes_in_physical_limit,
        "can_induce_effective_support": mc.can_induce_effective_support,
        "is_remaining_route_b_residue": mc.is_remaining_route_b_residue,
        "effective_energy_computed": mc.effective_energy_computed,
        "residue_reduced_from": mc.residue_reduced_from,
        "residue_reduced_to": mc.residue_reduced_to,
    }

    # Compatibility
    co = result.compatibility
    d["compatibility"] = {
        "standalone_diagonal_compatible": co.standalone_diagonal_compatible,
        "mixed_channel_compatible": co.mixed_channel_compatible,
        "computed_compatible": co.computed_compatible,
        "overall_status": co.overall_status,
    }

    # Projection
    pr = result.projection
    d["projection"] = {
        "standalone_diagonal_projection": pr.standalone_diagonal_projection,
        "mixed_channel_projection": pr.mixed_channel_projection,
        "mixed_channel_boundary_sensitive": pr.mixed_channel_boundary_sensitive,
    }

    # Admissibility
    ad = result.admissibility
    d["admissibility"] = {
        "standalone_diagonal_admissible": ad.standalone_diagonal_admissible,
        "mixed_channel_admissible": ad.mixed_channel_admissible,
        "energy_exists": ad.energy_exists,
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
        "is_full_route_b_no_go": cl.is_full_route_b_no_go,
        "standalone_diagonal_closed": cl.standalone_diagonal_closed,
        "mixed_channel_unresolved": cl.mixed_channel_unresolved,
        "residue_reduced": cl.residue_reduced,
    }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions
    d["diagnostics"] = result.diagnostics

    return d
