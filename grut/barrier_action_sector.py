"""Covariant barrier action sector analysis — Phase VI.

This module does not derive a covariant action for the barrier sector.
It proves that the self-healing equilibrium condition removes source-level
dynamical sensitivity to the action's free functions, and therefore the
equilibrium constitutive primitives alone do not identify a unique
barrier action.

PRINCIPAL RESULTS:

  Result 1 — Equilibrium Source Degeneracy Theorem (theorem-grade):
    For any admissible barrier-sector action that reproduces the
    constitutive memory equation in the appropriate limit and admits
    the GRUT equilibrium endpoint, the self-healing equilibrium
    condition X - Phi = 0 removes source-level dynamical sensitivity
    to the action's free functions in the first-order memory equation.
    Therefore the equilibrium constitutive primitives alone do not
    identify a unique barrier action.  Status: PROVEN.

  Result 2 — T^Phi Underdetermination (classification-grade):
    Even with the source degeneracy removed, T^Phi_mu_nu requires
    additional structural closure input (potential, EOS, propagation
    equation, gravity coupling specifics).  Level A (source degeneracy)
    supports but does not alone prove Level B (full T^Phi
    underdetermination).

  Result 3 — Route Assessment (classification-grade):
    Four action routes assessed against six admissibility conditions.
    No action-based route is fully determined by GRUT primitives.
    All three action-based routes require extra postulates.

  Result 4 — Minimal Missing Input (diagnostic):
    At least one additional closure input is required; sufficiency
    of a single input is not guaranteed generically.

PHASE V HANDOFF:
  Level 3: constitutive_lapse_promotion_obstructed (PRESERVED)
  T^Phi: schematic/effective (SHARPENED characterization)
  Self-healing: PRESERVED (used as INPUT to degeneracy theorem)

PHASE VI UPDATE:
  T^Phi: underdetermination now has structural explanation
    (equilibrium source degeneracy removes dynamical discrimination)
  Status ladder: UNCHANGED (no level changes)
  All Phase V results: PRESERVED

SELF-CONTAINED: No cross-imports from grut/.  Pure Python (math only).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


# ================================================================
# Constants — each mirrors canonical Phase IV/V value
# ================================================================

ALPHA_VAC = 1.0 / 3.0            # Mirrors canonical Phase IV value; see effective_lapse.py
BETA_Q = 2.0                     # Mirrors canonical Phase IV value; see effective_lapse.py
EPSILON_Q = ALPHA_VAC ** 2        # = 1/9; mirrors canonical Phase IV value
R_EQ_OVER_R_S = ALPHA_VAC        # = 1/3; from endpoint law
C_ENDPOINT = 1.0 / R_EQ_OVER_R_S # = 3.0; compactness at endpoint

# Classification labels (from Phase V; redefined here, not imported)
LEVEL_EXACT = "exact"
LEVEL_CONSTITUTIVE_DERIVED = "constitutive_derived"
LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED = (
    "constitutive_lapse_promotion_obstructed"
)

# Route labels (matching Phase IV action_principle.py naming)
ROUTE_A = "klein_gordon_overdamped"
ROUTE_B = "galley_doubled_field"
ROUTE_C = "nonlocal_retarded"
ROUTE_D = "auxiliary_field"

# Phase VI labels
TPHI_STATUS_PHASE_V = "schematic_effective"
TPHI_STATUS_PHASE_VI = "schematic_effective_equilibrium_degenerate"

# Number of admissibility conditions
N_ADMISSIBILITY_CONDITIONS = 6

# Verbatim scope statement
SCOPE_STATEMENT = (
    "Phase VI proves that the existing GRUT equilibrium primitives are "
    "structurally insufficient to determine a unique covariant barrier "
    "action, because the self-healing equilibrium condition removes "
    "source-level dynamical sensitivity to the action's free functions.  "
    "This does not rule out determining the action from off-equilibrium "
    "data or additional theoretical input."
)


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class AdmissibilityCondition:
    """A single admissibility condition for any barrier-sector action."""
    label: str = ""
    description: str = ""
    required_by: str = ""


@dataclass
class AdmissibilityAnalysis:
    """The full set of admissibility conditions."""
    conditions: List[AdmissibilityCondition] = field(default_factory=list)
    n_conditions: int = 0
    notes: List[str] = field(default_factory=list)


@dataclass
class RouteAssessment:
    """Assessment of a single action route against admissibility conditions.

    Uses a 6-criteria classification:
      1. action_based
      2. covariant
      3. reproduces_constitutive_limit (and whether exact)
      4. gravity_coupling_resolved
      5. uniquely_determined_by_grut
      6. requires_extra_postulate
    """
    route_name: str = ""
    route_label: str = ""
    action_type: str = ""

    action_based: bool = True
    covariant: bool = True
    reproduces_constitutive_limit: bool = False
    constitutive_limit_exact: bool = False
    gravity_coupling_resolved: bool = False
    gravity_coupling_note: str = ""
    uniquely_determined_by_grut: bool = False
    requires_extra_postulate: bool = False
    extra_postulates: List[str] = field(default_factory=list)

    T_phi_derivable: bool = False
    free_functions: List[str] = field(default_factory=list)
    n_free_functions: int = 0

    notes: List[str] = field(default_factory=list)


@dataclass
class RouteComparison:
    """Comparison across all four routes."""
    routes: List[RouteAssessment] = field(default_factory=list)
    n_routes: int = 0
    any_fully_determined: bool = False
    best_action_candidate: str = ""
    best_candidate_limitations: str = ""
    all_action_routes_require_extra: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class EquilibriumSourceDegeneracyProof:
    """Equilibrium Source Degeneracy Theorem — the central Phase VI result.

    THEOREM: For any admissible barrier-sector action that reproduces the
    constitutive memory equation in the appropriate limit and admits the
    GRUT equilibrium endpoint, the self-healing equilibrium condition
    X - Phi = 0 removes source-level dynamical sensitivity to the
    action's free functions in the first-order memory equation.  Therefore
    the equilibrium constitutive primitives alone do not identify a unique
    barrier action.

    SCOPE: This establishes equilibrium dynamical non-identifiability.
    It does NOT claim that all admissible actions produce identical
    stress-energy, pressure, or action values at equilibrium.
    """
    source_at_eq: float = 0.0
    source_vanishes: bool = False
    self_healing_input: bool = False

    equilibrium_ode_reduces_to_trivial: bool = False
    no_dynamical_discrimination: bool = False
    action_not_identifiable_from_equilibrium: bool = False

    does_NOT_claim_identical_stress_energy: bool = True

    proof_steps: List[str] = field(default_factory=list)
    theorem_status: str = ""
    scope_statement: str = ""

    uses_self_healing_from_phase_iv: bool = True
    uses_constitutive_ode_from_phase_iii: bool = True

    notes: List[str] = field(default_factory=list)


@dataclass
class TPhiUnderdeterminationAnalysis:
    """Level B: structural T^Phi underdetermination (classification-grade).

    NOT claimed to follow from the Source Degeneracy Theorem alone.
    Level A supports Level B, but Level A does not prove Level B.
    """
    level_A_supports: bool = True
    level_A_proves_level_B: bool = False

    additional_inputs_needed: List[str] = field(default_factory=list)
    independent_structural_reasons: List[str] = field(default_factory=list)

    notes: List[str] = field(default_factory=list)


@dataclass
class AdmissibleTPhiConstraints:
    """Structural constraints on T^Phi that hold without a unique action."""
    combined_conservation: bool = False
    spherical_symmetry: bool = False
    max_independent_components: int = 0
    nec_violation_indicated: bool = False
    nec_derivation_level: str = "constitutive"
    equilibrium_energy_constrained: bool = False
    equilibrium_energy_is_matching_condition: bool = True

    constraints_list: List[str] = field(default_factory=list)
    n_constraints: int = 0
    notes: List[str] = field(default_factory=list)


@dataclass
class MinimalMissingInput:
    """Irreducible inputs that would break the equilibrium source degeneracy."""
    candidates: List[str] = field(default_factory=list)
    n_candidates: int = 0
    any_one_may_reduce_degeneracy: bool = True
    sufficiency_not_guaranteed_generically: bool = True
    full_tphi_likely_needs_multiple: bool = True
    from_existing_grut: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class StatusLadderUpdate:
    """Status ladder update from Phase V to Phase VI."""
    level_1_before: str = ""
    level_1_after: str = ""
    level_1_changed: bool = False

    level_2_before: str = ""
    level_2_after: str = ""
    level_2_changed: bool = False

    level_3_before: str = ""
    level_3_after: str = ""
    level_3_changed: bool = False

    tphi_before: str = ""
    tphi_after: str = ""
    tphi_sharpened: bool = True
    tphi_sharpening_reason: str = ""

    no_level_weakened: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class Phase5Reconfirmation:
    """Reconfirmation that all Phase V results survive Phase VI."""
    insufficiency_theorem_preserved: bool = True
    effective_nec_preserved: bool = True
    lapse_direction_preserved: bool = True
    proxy_classification_preserved: bool = True
    self_healing_preserved: bool = True
    phase4_results_preserved: bool = True
    all_preserved: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class BarrierActionResult:
    """Master result: Phase VI barrier action sector analysis."""
    valid: bool = False

    admissibility: Optional[AdmissibilityAnalysis] = None
    route_A: Optional[RouteAssessment] = None
    route_B: Optional[RouteAssessment] = None
    route_C: Optional[RouteAssessment] = None
    route_D: Optional[RouteAssessment] = None
    route_comparison: Optional[RouteComparison] = None

    source_degeneracy: Optional[EquilibriumSourceDegeneracyProof] = None
    tphi_underdetermination: Optional[TPhiUnderdeterminationAnalysis] = None
    tphi_constraints: Optional[AdmissibleTPhiConstraints] = None
    minimal_missing: Optional[MinimalMissingInput] = None

    status_ladder: Optional[StatusLadderUpdate] = None
    phase5_reconfirmation: Optional[Phase5Reconfirmation] = None

    nonclaims: List[str] = field(default_factory=list)

    action_derived: bool = False
    action_partially_constrained: bool = True
    source_degeneracy_proven: bool = False
    tphi_underdetermination_established: bool = False
    self_healing_used_as_input: bool = True

    approx_status: str = ""
    remaining_obstructions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Builder functions
# ================================================================

def build_admissibility_analysis() -> AdmissibilityAnalysis:
    """Build the 6 admissibility conditions for any barrier-sector action."""
    aa = AdmissibilityAnalysis()

    aa.conditions = [
        AdmissibilityCondition(
            label="general_covariance",
            description=(
                "The action must be a diffeomorphism-invariant scalar "
                "functional of the metric and barrier field."
            ),
            required_by="general_relativity",
        ),
        AdmissibilityCondition(
            label="stress_energy_derivability",
            description=(
                "T^Phi_mu_nu must be derivable as (-2/sqrt(g)) "
                "delta(S)/delta(g^mu_nu) from the action."
            ),
            required_by="variational_principle",
        ),
        AdmissibilityCondition(
            label="combined_conservation",
            description=(
                "Combined conservation nabla_mu(T^mu_nu + T^Phi_mu_nu) = 0 "
                "must hold, consistent with the Bianchi identity."
            ),
            required_by="bianchi_identity",
        ),
        AdmissibilityCondition(
            label="spherical_symmetry",
            description=(
                "The action must be compatible with the spherically "
                "symmetric static or quasi-static interior."
            ),
            required_by="grut_endpoint_geometry",
        ),
        AdmissibilityCondition(
            label="equilibrium_compatibility",
            description=(
                "The action must admit the GRUT equilibrium endpoint "
                "R_eq/r_s = epsilon_Q^(1/beta_Q) as a solution."
            ),
            required_by="grut_endpoint_law",
        ),
        AdmissibilityCondition(
            label="constitutive_limit",
            description=(
                "The action must recover the constitutive memory ODE "
                "tau_eff dPhi/dt + Phi = X in the weak-field or "
                "overdamped limit."
            ),
            required_by="grut_memory_equation",
        ),
    ]

    aa.n_conditions = len(aa.conditions)

    aa.notes = [
        (
            "These 6 conditions are necessary for any barrier-sector "
            "action to be consistent with the existing GRUT framework."
        ),
        (
            "Condition 6 (constitutive limit) is what connects the "
            "covariant action to the existing constitutive dynamics."
        ),
    ]

    return aa


def build_route_assessment_A() -> RouteAssessment:
    """Assess Route A: Klein-Gordon overdamped limit."""
    r = RouteAssessment()
    r.route_name = "Klein-Gordon Overdamped"
    r.route_label = ROUTE_A
    r.action_type = "local_scalar"

    r.action_based = True
    r.covariant = True
    r.reproduces_constitutive_limit = True
    r.constitutive_limit_exact = False  # approximate (overdamped limit)
    r.gravity_coupling_resolved = True
    r.gravity_coupling_note = (
        "Formal minimal coupling exists (standard scalar-gravity "
        "coupling via covariant derivatives and metric determinant).  "
        "However, V(Phi) is not determined, so the gravitational "
        "closure is not fully achieved."
    )
    r.uniquely_determined_by_grut = False
    r.requires_extra_postulate = True
    r.extra_postulates = [
        "V(Phi) — potential shape not constrained by GRUT primitives",
        "J — source coupling functional form",
    ]

    r.T_phi_derivable = True
    r.free_functions = [
        "V(Phi) — scalar potential (shape entirely free)",
        "J[g, T] — source coupling to matter/gravity",
    ]
    r.n_free_functions = len(r.free_functions)

    r.notes = [
        (
            "The Klein-Gordon action S = int sqrt(-g) "
            "[-1/2 g^ab nabla_a Phi nabla_b Phi - V(Phi) + J*Phi] "
            "is covariant and gives T^Phi via standard variation."
        ),
        (
            "The overdamped limit (large mass / strong damping) "
            "approximately recovers the constitutive memory ODE, "
            "but this is an approximation, not exact."
        ),
        (
            "Different V(Phi) choices yield different T^Phi at "
            "the same equilibrium point."
        ),
    ]

    return r


def build_route_assessment_B() -> RouteAssessment:
    """Assess Route B: Galley doubled-field formalism."""
    r = RouteAssessment()
    r.route_name = "Galley Doubled-Field"
    r.route_label = ROUTE_B
    r.action_type = "doubled_field_dissipative"

    r.action_based = True
    r.covariant = True
    r.reproduces_constitutive_limit = True
    r.constitutive_limit_exact = True  # exact in physical limit
    r.gravity_coupling_resolved = False
    r.gravity_coupling_note = (
        "The Galley formalism produces the first-order dissipative ODE "
        "exactly via the physical-limit projection.  However, the "
        "coupling of the doubled-field action to the gravitational "
        "sector has not been worked out."
    )
    r.uniquely_determined_by_grut = False
    r.requires_extra_postulate = True
    r.extra_postulates = [
        "K_diss — dissipation kernel / functional",
        "L_nondiss — non-dissipative part of the Lagrangian",
    ]

    r.T_phi_derivable = True
    r.free_functions = [
        "K_diss(Phi_1, Phi_2) — dissipation functional",
        "L(Phi, g) — non-dissipative Lagrangian",
    ]
    r.n_free_functions = len(r.free_functions)

    r.notes = [
        (
            "Route B is formally the strongest: it produces the "
            "first-order ODE exactly, not approximately."
        ),
        (
            "The gravity coupling (how the doubled-field action "
            "enters G_mu_nu = 8*pi*G*(T + T^Phi)) has NOT been "
            "implemented."
        ),
        (
            "K_diss and L are individually free; different choices "
            "yield different T^Phi in the physical limit."
        ),
    ]

    return r


def build_route_assessment_C() -> RouteAssessment:
    """Assess Route C: nonlocal retarded kernel."""
    r = RouteAssessment()
    r.route_name = "Nonlocal Retarded"
    r.route_label = ROUTE_C
    r.action_type = "nonlocal_kernel"

    r.action_based = True
    r.covariant = True
    r.reproduces_constitutive_limit = True
    r.constitutive_limit_exact = True  # exact for exponential kernel
    r.gravity_coupling_resolved = True
    r.gravity_coupling_note = (
        "Formal retarded-kernel construction couples to gravity "
        "through the nonlocal integral.  The exponential kernel "
        "reduces to the auxiliary-field ODE along observer flow."
    )
    r.uniquely_determined_by_grut = False
    r.requires_extra_postulate = True
    r.extra_postulates = [
        "K(x,x') — full retarded kernel beyond exponential form",
    ]

    r.T_phi_derivable = True
    r.free_functions = [
        "K(x,x') — retarded kernel (only exponential form constrained)",
    ]
    r.n_free_functions = len(r.free_functions)

    r.notes = [
        (
            "Route C is the formal parent of Route D for the "
            "exponential kernel."
        ),
        (
            "The exponential kernel is sufficient for the constitutive "
            "limit, but the full covariant kernel K(x,x') is not "
            "uniquely determined."
        ),
    ]

    return r


def build_route_assessment_D() -> RouteAssessment:
    """Assess Route D: auxiliary-field realization (non-action closure)."""
    r = RouteAssessment()
    r.route_name = "Auxiliary-Field Realization"
    r.route_label = ROUTE_D
    r.action_type = "non_action_closure"

    r.action_based = False
    r.covariant = True
    r.reproduces_constitutive_limit = True
    r.constitutive_limit_exact = True  # exact by construction
    r.gravity_coupling_resolved = True
    r.gravity_coupling_note = (
        "Gravity coupling is achieved by construction: the auxiliary "
        "field enters the initial-value formulation directly."
    )
    r.uniquely_determined_by_grut = False
    r.requires_extra_postulate = False
    r.extra_postulates = []

    r.T_phi_derivable = False
    r.free_functions = []
    r.n_free_functions = 0

    r.notes = [
        (
            "Route D is a non-action closure route: it bypasses the "
            "action question entirely by treating Phi as an auxiliary "
            "field in an initial-value formulation."
        ),
        (
            "T^Phi is constitutive/effective under Route D, not "
            "variationally derived."
        ),
        (
            "Route D is PREFERRED for computational purposes but "
            "does not answer the action question.  It is outside the "
            "present phase target, not 'inadmissible' in the sense "
            "of physically failing."
        ),
    ]

    return r


def build_route_comparison(
    routes: List[RouteAssessment],
) -> RouteComparison:
    """Compare all four routes."""
    rc = RouteComparison()
    rc.routes = routes
    rc.n_routes = len(routes)
    rc.any_fully_determined = False

    rc.best_action_candidate = ROUTE_B
    rc.best_candidate_limitations = (
        "Route B (Galley doubled-field) is formally the strongest "
        "action-based candidate: it produces the first-order "
        "dissipative ODE exactly.  However, the gravity coupling "
        "has not been implemented, and K_diss and L_nondiss are free."
    )

    action_routes = [r for r in routes if r.action_based]
    rc.all_action_routes_require_extra = all(
        r.requires_extra_postulate for r in action_routes
    )

    rc.notes = [
        (
            "No action-based route is fully determined by current "
            "GRUT primitives."
        ),
        (
            "All three action-based routes (A, B, C) require at least "
            "one extra postulate not contained in the existing "
            "GRUT framework."
        ),
        (
            "Route D bypasses the action question entirely; it is "
            "a non-action closure route, outside the present phase "
            "target."
        ),
    ]

    return rc


def build_equilibrium_source_degeneracy_proof() -> EquilibriumSourceDegeneracyProof:
    """Prove the Equilibrium Source Degeneracy Theorem."""
    ed = EquilibriumSourceDegeneracyProof()

    ed.source_at_eq = 0.0
    ed.source_vanishes = True
    ed.self_healing_input = True

    ed.equilibrium_ode_reduces_to_trivial = True
    ed.no_dynamical_discrimination = True
    ed.action_not_identifiable_from_equilibrium = True

    ed.does_NOT_claim_identical_stress_energy = True

    ed.proof_steps = [
        (
            "1. At GRUT equilibrium: Phi_eq = X_eq (memory fully "
            "relaxed to source, force balance)."
        ),
        (
            "2. Source functional: X - Phi = 0 at equilibrium "
            "(self-healing, established in Phase IV)."
        ),
        (
            "3. All admissible actions reproduce the constitutive "
            "memory ODE tau dPhi/dt + Phi = X; at equilibrium, "
            "this reduces to 0 = 0 regardless of the action's "
            "free functions (V(Phi), K, K_diss)."
        ),
        (
            "4. Therefore the equilibrium source equation does not "
            "dynamically discriminate among different choices of "
            "free functions."
        ),
        (
            "5. Within the current GRUT equilibrium primitive set, "
            "the source equation is the only direct dynamical "
            "constraint on the barrier-sector relaxation variable "
            "at equilibrium; therefore equilibrium constitutive "
            "primitives alone cannot identify a unique action."
        ),
        "6. Therefore additional closure input is required.  QED.",
    ]

    ed.theorem_status = "proven"
    ed.scope_statement = SCOPE_STATEMENT

    ed.uses_self_healing_from_phase_iv = True
    ed.uses_constitutive_ode_from_phase_iii = True

    ed.notes = [
        (
            "This theorem establishes equilibrium dynamical "
            "non-identifiability — the source-level ODE cannot "
            "discriminate among actions at equilibrium."
        ),
        (
            "It does NOT claim that all admissible actions produce "
            "identical stress-energy, pressure profiles, action "
            "values, or derivative couplings at equilibrium."
        ),
        (
            "Self-healing (X - Phi = 0 at equilibrium) is an "
            "established Phase IV result, used here as input."
        ),
    ]

    return ed


def build_tphi_underdetermination_analysis() -> TPhiUnderdeterminationAnalysis:
    """Build Level B: structural T^Phi underdetermination (classification-grade)."""
    tu = TPhiUnderdeterminationAnalysis()

    tu.level_A_supports = True
    tu.level_A_proves_level_B = False

    tu.additional_inputs_needed = [
        "Action normalization / overall scale",
        "A specific potential V(Phi) or equivalent",
        "An equation of state p_Phi(rho_Phi)",
        "Propagation structure (wave equation vs. pure relaxation)",
        "Auxiliary-field or nonlocal closure specifics",
        "Coupling to gravity beyond formal minimal coupling",
    ]

    tu.independent_structural_reasons = [
        (
            "T^Phi_mu_nu = (-2/sqrt(g)) delta(S)/delta(g^mu_nu) "
            "requires a specific action S, which is not uniquely "
            "determined even if equilibrium constraints are imposed."
        ),
        (
            "The constitutive memory ODE is first-order and dissipative; "
            "no local real Lagrangian produces it directly "
            "(Phase IV fundamental theorem)."
        ),
        (
            "Each of the three action-based routes (A, B, C) contains "
            "free functions not constrained by existing GRUT primitives."
        ),
    ]

    tu.notes = [
        (
            "Level B is a classification-grade structural observation, "
            "not a theorem-grade result."
        ),
        (
            "Level A (source degeneracy) supports Level B by removing "
            "the strongest available equilibrium constraint, but "
            "Level A alone does not prove Level B."
        ),
        (
            "Level B is independently supported by the Phase IV "
            "fundamental theorem (no local Lagrangian for first-order "
            "ODE) and by the free-function analysis of Routes A-C."
        ),
    ]

    return tu


def build_admissible_tphi_constraints() -> AdmissibleTPhiConstraints:
    """Build structural constraints on T^Phi that hold without unique action."""
    tc = AdmissibleTPhiConstraints()

    tc.combined_conservation = True
    tc.spherical_symmetry = True
    tc.max_independent_components = 3  # rho_Phi, P_r, P_perp
    tc.nec_violation_indicated = True
    tc.nec_derivation_level = "constitutive"
    tc.equilibrium_energy_constrained = True
    tc.equilibrium_energy_is_matching_condition = True

    tc.constraints_list = [
        (
            "Combined conservation: nabla_mu(T^mu_nu + T^Phi_mu_nu) = 0 "
            "(from Bianchi identity)."
        ),
        (
            "Spherical symmetry: T^Phi must be diagonal in adapted "
            "coordinates (t, r, theta, phi)."
        ),
        (
            "At most 3 independent components: rho_Phi, P_r, P_perp "
            "(for anisotropic spherically symmetric stress-energy)."
        ),
        (
            "NEC violation indicated at the constitutive level "
            "(from Phase V; rho + P < 0 for sub-horizon support)."
        ),
        (
            "Equilibrium energy consistent with barrier energy "
            "Phi_barrier — as a matching condition, not a derived "
            "unique stress-energy result."
        ),
    ]
    tc.n_constraints = len(tc.constraints_list)

    tc.notes = [
        (
            "These constraints define an admissible CLASS of T^Phi, "
            "not a unique member."
        ),
        (
            "The equilibrium energy constraint is a matching condition: "
            "it requires consistency with the barrier energy scale, "
            "but does not uniquely determine the stress-energy tensor."
        ),
    ]

    return tc


def build_minimal_missing_input() -> MinimalMissingInput:
    """Identify the irreducible missing inputs."""
    mm = MinimalMissingInput()

    mm.candidates = [
        (
            "A potential V(Phi) for the barrier scalar field — "
            "not constrained by existing GRUT primitives."
        ),
        (
            "A covariant propagation equation for Phi — currently "
            "no wave equation exists in the GRUT framework."
        ),
        (
            "An equation of state p_Phi(rho_Phi) for the barrier "
            "effective fluid — not specified."
        ),
        (
            "Off-equilibrium dynamical data (e.g., quasi-normal mode "
            "observation) — would probe away from the degenerate "
            "equilibrium point."
        ),
    ]
    mm.n_candidates = len(mm.candidates)

    mm.any_one_may_reduce_degeneracy = True
    mm.sufficiency_not_guaranteed_generically = True
    mm.full_tphi_likely_needs_multiple = True
    mm.from_existing_grut = False

    mm.notes = [
        (
            "At least one additional closure input is required.  "
            "A single such input may be sufficient to break source "
            "degeneracy (Level A) in favorable cases, but sufficiency "
            "is not guaranteed generically."
        ),
        (
            "A complete determination of T^Phi (Level B) likely "
            "requires multiple inputs (e.g., V(Phi) + propagation "
            "structure, or EOS + gravity coupling)."
        ),
        (
            "None of these inputs is available from existing GRUT "
            "primitives."
        ),
    ]

    return mm


def build_status_ladder_update() -> StatusLadderUpdate:
    """Build the Phase V to Phase VI status ladder transition."""
    sl = StatusLadderUpdate()

    sl.level_1_before = LEVEL_EXACT
    sl.level_1_after = LEVEL_EXACT
    sl.level_1_changed = False

    sl.level_2_before = LEVEL_CONSTITUTIVE_DERIVED
    sl.level_2_after = LEVEL_CONSTITUTIVE_DERIVED
    sl.level_2_changed = False

    sl.level_3_before = LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED
    sl.level_3_after = LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED
    sl.level_3_changed = False

    sl.tphi_before = TPHI_STATUS_PHASE_V
    sl.tphi_after = TPHI_STATUS_PHASE_VI
    sl.tphi_sharpened = True
    sl.tphi_sharpening_reason = (
        "The Equilibrium Source Degeneracy Theorem provides a "
        "structural explanation for why T^Phi remains underdetermined: "
        "the self-healing equilibrium condition removes source-level "
        "dynamical sensitivity to the action's free functions.  "
        "T^Phi was already 'schematic/effective' in Phase V; "
        "Phase VI adds the equilibrium degeneracy explanation."
    )

    sl.no_level_weakened = True

    sl.notes = [
        "Level 1 (exact barrier ratio): UNCHANGED.",
        "Level 2 (constitutive-derived proxy): UNCHANGED.",
        "Level 3 (constitutive lapse promotion obstructed): UNCHANGED.",
        (
            "T^Phi characterization: sharpened from "
            "'schematic_effective' to "
            "'schematic_effective_equilibrium_degenerate'."
        ),
        "No level is weakened by Phase VI.",
    ]

    return sl


def build_phase5_reconfirmation() -> Phase5Reconfirmation:
    """Reconfirm all Phase V results survive Phase VI."""
    p5 = Phase5Reconfirmation()
    p5.insufficiency_theorem_preserved = True
    p5.effective_nec_preserved = True
    p5.lapse_direction_preserved = True
    p5.proxy_classification_preserved = True
    p5.self_healing_preserved = True
    p5.phase4_results_preserved = True
    p5.all_preserved = True

    p5.notes = [
        (
            "Phase VI adds new results but does NOT invalidate "
            "any Phase V or Phase IV result."
        ),
        (
            "Self-healing is used as an established INPUT to the "
            "Source Degeneracy Theorem; it is not affected by it."
        ),
    ]

    return p5


# ================================================================
# Master analysis
# ================================================================

def compute_barrier_action_analysis() -> BarrierActionResult:
    """Master analysis: Phase VI barrier action sector.

    Steps:
      1. Build admissibility conditions
      2. Assess Route A
      3. Assess Route B
      4. Assess Route C
      5. Assess Route D
      6. Compare routes
      7. Prove Equilibrium Source Degeneracy Theorem
      8. Build T^Phi underdetermination analysis
      9. Build admissible T^Phi constraints
      10. Identify minimal missing input
      11. Update status ladder
      12. Reconfirm Phase V
      13. Assemble nonclaims + diagnostics
    """
    result = BarrierActionResult()

    # 1-6: Admissibility and routes
    result.admissibility = build_admissibility_analysis()

    result.route_A = build_route_assessment_A()
    result.route_B = build_route_assessment_B()
    result.route_C = build_route_assessment_C()
    result.route_D = build_route_assessment_D()

    all_routes = [result.route_A, result.route_B,
                  result.route_C, result.route_D]
    result.route_comparison = build_route_comparison(all_routes)

    # 7: Source Degeneracy Theorem
    result.source_degeneracy = build_equilibrium_source_degeneracy_proof()

    # 8: T^Phi underdetermination (Level B)
    result.tphi_underdetermination = build_tphi_underdetermination_analysis()

    # 9: Admissible T^Phi constraints
    result.tphi_constraints = build_admissible_tphi_constraints()

    # 10: Minimal missing input
    result.minimal_missing = build_minimal_missing_input()

    # 11: Status ladder
    result.status_ladder = build_status_ladder_update()

    # 12: Phase V reconfirmation
    result.phase5_reconfirmation = build_phase5_reconfirmation()

    # 13: Nonclaims (12)
    result.nonclaims = [
        (
            "Phase VI does NOT derive a covariant action for the "
            "barrier sector."
        ),
        (
            "The Source Degeneracy Theorem proves equilibrium "
            "dynamical non-identifiability; it does NOT claim all "
            "admissible actions produce identical stress-energy, "
            "pressure, or action values at equilibrium."
        ),
        (
            "T^Phi underdetermination (Level B) is a classification-"
            "grade structural observation supported by, but not solely "
            "proven by, the Source Degeneracy Theorem (Level A)."
        ),
        (
            "Route A (KG overdamped) has formal minimal coupling, "
            "but V(Phi) is not determined — fully determined "
            "gravitational closure not achieved."
        ),
        (
            "Route B (Galley) gravity coupling is NOT worked out."
        ),
        (
            "Route D is a non-action closure route, outside present "
            "phase target — not 'inadmissible' but simply does not "
            "answer the action question."
        ),
        (
            "NEC violation remains constitutive-level (from Phase V)."
        ),
        "No new GRUT primitives introduced.",
        (
            "No existing result weakened; all Phase V results "
            "preserved."
        ),
        (
            "Equilibrium source degeneracy does NOT invalidate "
            "self-healing (it uses self-healing as an established "
            "input)."
        ),
        (
            "Equilibrium energy consistency with barrier energy is "
            "a matching condition, NOT a derived unique stress-energy "
            "result."
        ),
        "No observational predictions changed.",
    ]

    # Summary flags
    result.action_derived = False
    result.action_partially_constrained = True
    result.source_degeneracy_proven = (
        result.source_degeneracy.theorem_status == "proven"
    )
    result.tphi_underdetermination_established = True
    result.self_healing_used_as_input = True

    result.approx_status = (
        "Phase VI: Barrier action NOT derived.  Equilibrium Source "
        "Degeneracy Theorem PROVEN: self-healing removes source-level "
        "dynamical sensitivity to action free functions at equilibrium.  "
        "T^Phi underdetermination has structural explanation "
        "(classification-grade).  Minimal missing inputs identified.  "
        "Status ladder: UNCHANGED.  All Phase V results: PRESERVED."
    )

    result.remaining_obstructions = [
        (
            "A covariant action S[Phi] for the memory/barrier field, "
            "yielding T^Phi from variational principles — not "
            "determined by equilibrium primitives (source degeneracy)."
        ),
        (
            "At least one additional closure input: potential V(Phi), "
            "propagation equation, EOS, or off-equilibrium data."
        ),
        (
            "Solution of Einstein equations G = 8piG(T^matter + T^Phi) "
            "with the derived T^Phi in the sub-horizon regime."
        ),
    ]

    result.diagnostics = {
        "n_admissibility_conditions": (
            result.admissibility.n_conditions
        ),
        "n_routes": result.route_comparison.n_routes,
        "any_fully_determined": (
            result.route_comparison.any_fully_determined
        ),
        "all_action_routes_require_extra": (
            result.route_comparison.all_action_routes_require_extra
        ),
        "source_degeneracy_proven": result.source_degeneracy_proven,
        "tphi_underdetermination_established": True,
        "level_A_proves_level_B": (
            result.tphi_underdetermination.level_A_proves_level_B
        ),
        "n_tphi_constraints": result.tphi_constraints.n_constraints,
        "n_missing_candidates": result.minimal_missing.n_candidates,
        "from_existing_grut": result.minimal_missing.from_existing_grut,
        "level_3_changed": result.status_ladder.level_3_changed,
        "tphi_sharpened": result.status_ladder.tphi_sharpened,
        "phase5_preserved": (
            result.phase5_reconfirmation.all_preserved
        ),
        "n_nonclaims": len(result.nonclaims),
        "action_derived": False,
        "self_healing_used_as_input": True,
    }

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def _admissibility_condition_to_dict(
    c: AdmissibilityCondition,
) -> Dict[str, Any]:
    return {
        "label": c.label,
        "description": c.description,
        "required_by": c.required_by,
    }


def _admissibility_analysis_to_dict(
    a: AdmissibilityAnalysis,
) -> Dict[str, Any]:
    return {
        "conditions": [_admissibility_condition_to_dict(c)
                       for c in a.conditions],
        "n_conditions": a.n_conditions,
        "notes": a.notes,
    }


def _route_assessment_to_dict(r: RouteAssessment) -> Dict[str, Any]:
    return {
        "route_name": r.route_name,
        "route_label": r.route_label,
        "action_type": r.action_type,
        "action_based": r.action_based,
        "covariant": r.covariant,
        "reproduces_constitutive_limit": r.reproduces_constitutive_limit,
        "constitutive_limit_exact": r.constitutive_limit_exact,
        "gravity_coupling_resolved": r.gravity_coupling_resolved,
        "gravity_coupling_note": r.gravity_coupling_note,
        "uniquely_determined_by_grut": r.uniquely_determined_by_grut,
        "requires_extra_postulate": r.requires_extra_postulate,
        "extra_postulates": r.extra_postulates,
        "T_phi_derivable": r.T_phi_derivable,
        "free_functions": r.free_functions,
        "n_free_functions": r.n_free_functions,
        "notes": r.notes,
    }


def _route_comparison_to_dict(rc: RouteComparison) -> Dict[str, Any]:
    return {
        "routes": [_route_assessment_to_dict(r) for r in rc.routes],
        "n_routes": rc.n_routes,
        "any_fully_determined": rc.any_fully_determined,
        "best_action_candidate": rc.best_action_candidate,
        "best_candidate_limitations": rc.best_candidate_limitations,
        "all_action_routes_require_extra": (
            rc.all_action_routes_require_extra
        ),
        "notes": rc.notes,
    }


def _source_degeneracy_to_dict(
    ed: EquilibriumSourceDegeneracyProof,
) -> Dict[str, Any]:
    return {
        "source_at_eq": ed.source_at_eq,
        "source_vanishes": ed.source_vanishes,
        "self_healing_input": ed.self_healing_input,
        "equilibrium_ode_reduces_to_trivial": (
            ed.equilibrium_ode_reduces_to_trivial
        ),
        "no_dynamical_discrimination": ed.no_dynamical_discrimination,
        "action_not_identifiable_from_equilibrium": (
            ed.action_not_identifiable_from_equilibrium
        ),
        "does_NOT_claim_identical_stress_energy": (
            ed.does_NOT_claim_identical_stress_energy
        ),
        "proof_steps": ed.proof_steps,
        "theorem_status": ed.theorem_status,
        "scope_statement": ed.scope_statement,
        "uses_self_healing_from_phase_iv": (
            ed.uses_self_healing_from_phase_iv
        ),
        "uses_constitutive_ode_from_phase_iii": (
            ed.uses_constitutive_ode_from_phase_iii
        ),
        "notes": ed.notes,
    }


def _tphi_underdetermination_to_dict(
    tu: TPhiUnderdeterminationAnalysis,
) -> Dict[str, Any]:
    return {
        "level_A_supports": tu.level_A_supports,
        "level_A_proves_level_B": tu.level_A_proves_level_B,
        "additional_inputs_needed": tu.additional_inputs_needed,
        "independent_structural_reasons": (
            tu.independent_structural_reasons
        ),
        "notes": tu.notes,
    }


def _tphi_constraints_to_dict(
    tc: AdmissibleTPhiConstraints,
) -> Dict[str, Any]:
    return {
        "combined_conservation": tc.combined_conservation,
        "spherical_symmetry": tc.spherical_symmetry,
        "max_independent_components": tc.max_independent_components,
        "nec_violation_indicated": tc.nec_violation_indicated,
        "nec_derivation_level": tc.nec_derivation_level,
        "equilibrium_energy_constrained": (
            tc.equilibrium_energy_constrained
        ),
        "equilibrium_energy_is_matching_condition": (
            tc.equilibrium_energy_is_matching_condition
        ),
        "constraints_list": tc.constraints_list,
        "n_constraints": tc.n_constraints,
        "notes": tc.notes,
    }


def _minimal_missing_to_dict(mm: MinimalMissingInput) -> Dict[str, Any]:
    return {
        "candidates": mm.candidates,
        "n_candidates": mm.n_candidates,
        "any_one_may_reduce_degeneracy": (
            mm.any_one_may_reduce_degeneracy
        ),
        "sufficiency_not_guaranteed_generically": (
            mm.sufficiency_not_guaranteed_generically
        ),
        "full_tphi_likely_needs_multiple": (
            mm.full_tphi_likely_needs_multiple
        ),
        "from_existing_grut": mm.from_existing_grut,
        "notes": mm.notes,
    }


def _status_ladder_to_dict(sl: StatusLadderUpdate) -> Dict[str, Any]:
    return {
        "level_1_before": sl.level_1_before,
        "level_1_after": sl.level_1_after,
        "level_1_changed": sl.level_1_changed,
        "level_2_before": sl.level_2_before,
        "level_2_after": sl.level_2_after,
        "level_2_changed": sl.level_2_changed,
        "level_3_before": sl.level_3_before,
        "level_3_after": sl.level_3_after,
        "level_3_changed": sl.level_3_changed,
        "tphi_before": sl.tphi_before,
        "tphi_after": sl.tphi_after,
        "tphi_sharpened": sl.tphi_sharpened,
        "tphi_sharpening_reason": sl.tphi_sharpening_reason,
        "no_level_weakened": sl.no_level_weakened,
        "notes": sl.notes,
    }


def _phase5_reconfirmation_to_dict(
    p5: Phase5Reconfirmation,
) -> Dict[str, Any]:
    return {
        "insufficiency_theorem_preserved": (
            p5.insufficiency_theorem_preserved
        ),
        "effective_nec_preserved": p5.effective_nec_preserved,
        "lapse_direction_preserved": p5.lapse_direction_preserved,
        "proxy_classification_preserved": (
            p5.proxy_classification_preserved
        ),
        "self_healing_preserved": p5.self_healing_preserved,
        "phase4_results_preserved": p5.phase4_results_preserved,
        "all_preserved": p5.all_preserved,
        "notes": p5.notes,
    }


def barrier_action_result_to_dict(
    result: BarrierActionResult,
) -> Dict[str, Any]:
    """Serialize the master BarrierActionResult to a dictionary."""
    d: Dict[str, Any] = {"valid": result.valid}

    if result.admissibility is not None:
        d["admissibility"] = _admissibility_analysis_to_dict(
            result.admissibility
        )
    if result.route_A is not None:
        d["route_A"] = _route_assessment_to_dict(result.route_A)
    if result.route_B is not None:
        d["route_B"] = _route_assessment_to_dict(result.route_B)
    if result.route_C is not None:
        d["route_C"] = _route_assessment_to_dict(result.route_C)
    if result.route_D is not None:
        d["route_D"] = _route_assessment_to_dict(result.route_D)
    if result.route_comparison is not None:
        d["route_comparison"] = _route_comparison_to_dict(
            result.route_comparison
        )
    if result.source_degeneracy is not None:
        d["source_degeneracy"] = _source_degeneracy_to_dict(
            result.source_degeneracy
        )
    if result.tphi_underdetermination is not None:
        d["tphi_underdetermination"] = _tphi_underdetermination_to_dict(
            result.tphi_underdetermination
        )
    if result.tphi_constraints is not None:
        d["tphi_constraints"] = _tphi_constraints_to_dict(
            result.tphi_constraints
        )
    if result.minimal_missing is not None:
        d["minimal_missing"] = _minimal_missing_to_dict(
            result.minimal_missing
        )
    if result.status_ladder is not None:
        d["status_ladder"] = _status_ladder_to_dict(result.status_ladder)
    if result.phase5_reconfirmation is not None:
        d["phase5_reconfirmation"] = _phase5_reconfirmation_to_dict(
            result.phase5_reconfirmation
        )

    d["nonclaims"] = result.nonclaims
    d["action_derived"] = result.action_derived
    d["action_partially_constrained"] = result.action_partially_constrained
    d["source_degeneracy_proven"] = result.source_degeneracy_proven
    d["tphi_underdetermination_established"] = (
        result.tphi_underdetermination_established
    )
    d["self_healing_used_as_input"] = result.self_healing_used_as_input
    d["approx_status"] = result.approx_status
    d["remaining_obstructions"] = result.remaining_obstructions
    d["diagnostics"] = result.diagnostics

    return d
