"""Testing EOS / Potential Closure from beta_Q — Phase VII.

This module does not derive an equation of state for the barrier sector
from beta_Q.  It establishes that beta_Q is a compactness-dependent barrier
steepness exponent, NOT an EOS exponent, and that its conditional mapping
to w_Phi and V(Phi) exists ONLY under specific assumptions (KG Route A,
canonical kinetic term, isotropy).

PRINCIPAL RESULTS:

  Result 1 — EOS Admissibility Assessment (classification-grade):
    beta_Q can be conditionally mapped to an EOS parameter, but only under
    the perfect-fluid isotropy assumption AND the KG Route A potential
    ansatz.  The collapse sector is anisotropic, blocking a single-w_Phi
    interpretation.  Classification: admissible_but_nonunique.

  Result 2 — Conditional Mapping Sequence (diagnostic):
    The sequence beta_Q -> omega_0^2 -> m^2 -> V(Phi) -> w_Phi exists but
    each step beyond omega_0^2 = beta_Q * omega_g^2 requires additional
    assumptions.  Only step 1 is EXACT.  Step 5 is a terminal anisotropy
    block, not a forward derivation step.

  Result 3 — Anisotropy Block (classification-grade):
    The collapse sector requires (w_r, w_perp), not a single w_Phi.
    The cosmological sector is isotropic (single w_Phi sufficient).

  Result 4 — Candidate Scalar Potential (conditional):
    V(Phi) = Phi^2/(2 tau^2) is the KG Route A candidate, conditional
    on the mass-term identification m^2 = 1/tau^2.  It is NOT unique
    and NOT derived from beta_Q alone.

  Result 5 — Degeneracy Reduction Assessment (classification-grade):
    V(Phi) reduces Route A free functions (V fixed, J still free) but
    does NOT break degeneracy for Routes B, C, or generically.
    Classification: partially_closing.

  Result 6 — NEC Compatibility (classification-grade, Route A isotropic only):
    w_Phi = -1 at equilibrium implies rho + p = 0 (NEC-saturating),
    compatible with but not contradicting Phase V NEC indication.
    This check applies only to the isotropic Route A candidate closure
    and is NOT a full anisotropic collapse-sector NEC analysis.

  Result 7 — Lapse Impact (diagnostic):
    The EOS/potential closure does NOT improve lapse determination.
    Phase V obstruction persists: T^Phi remains constitutive/effective.

PHASE VI HANDOFF:
  T^Phi: schematic_effective_equilibrium_degenerate (PRESERVED)
  Status ladder: ALL LEVELS UNCHANGED
  All Phase VI results: PRESERVED

PHASE VII UPDATE:
  EOS closure from beta_Q: admissible_but_nonunique
  Degeneracy: partially reduced within Route A, NOT broken
  Lapse: UNCHANGED (obstruction persists)
  No level changed, no level weakened

SELF-CONTAINED: No cross-imports from grut/.  Pure Python (math, json, enum).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any


# ================================================================
# Constants — each mirrors canonical values
# ================================================================

ALPHA_VAC = 1.0 / 3.0
BETA_Q = 2.0
EPSILON_Q = ALPHA_VAC ** 2          # = 1/9
R_EQ_OVER_R_S = ALPHA_VAC          # = 1/3
C_ENDPOINT = 1.0 / R_EQ_OVER_R_S   # = 3.0

# Classification labels (from Phase V/VI, redefined here)
LEVEL_EXACT = "exact"
LEVEL_CONSTITUTIVE_DERIVED = "constitutive_derived"
LEVEL_CONSTITUTIVE_LAPSE_PROMOTION_OBSTRUCTED = (
    "constitutive_lapse_promotion_obstructed"
)

# Route labels
ROUTE_A = "klein_gordon_overdamped"
ROUTE_B = "galley_doubled_field"
ROUTE_C = "nonlocal_retarded"
ROUTE_D = "auxiliary_field"

# T^Phi status (unchanged from Phase VI)
TPHI_STATUS_PHASE_VI = "schematic_effective_equilibrium_degenerate"
TPHI_STATUS_PHASE_VII = "schematic_effective_equilibrium_degenerate"

# Phase VII scope statement
SCOPE_STATEMENT = (
    "Phase VII establishes that beta_Q is a barrier steepness exponent, "
    "not an EOS exponent.  A conditional mapping to w_Phi and V(Phi) "
    "exists only under specific assumptions (KG Route A, canonical kinetic "
    "term, isotropy).  This partially reduces Route A degeneracy but does "
    "not break the full degeneracy established in Phase VI."
)


# ================================================================
# Closure Classification Enum
# ================================================================

class ClosureClassification(str, Enum):
    """Classification of the EOS/potential closure attempt."""
    NOT_ADMISSIBLE = "not_admissible"
    ADMISSIBLE_BUT_NONUNIQUE = "admissible_but_nonunique"
    PARTIALLY_CLOSING = "partially_closing"
    FULLY_CLOSING = "fully_closing"
    INCOMPATIBLE_WITH_PHASE_V = "incompatible_with_phase_v"
    UNRESOLVED = "unresolved"


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class EOSAdmissibilityTest:
    """Can beta_Q be interpreted as an EOS parameter?

    ANSWER: Conditionally yes, under stated assumptions, but it is
    fundamentally a barrier steepness exponent, not an EOS exponent.
    """
    beta_Q_is_eos_exponent: bool = False
    beta_Q_is_stiffness_exponent: bool = True
    requires_perfect_fluid: bool = True
    requires_isotropy: bool = True
    anisotropy_required_for_collapse: bool = True
    single_w_sufficient: bool = False
    single_w_sufficient_for_cosmo: bool = True
    conditional_mapping_exists: bool = True
    assumptions_for_mapping: List[str] = field(default_factory=list)

    omega_0_sq_exact: bool = True
    omega_0_sq_value: float = 0.0
    omega_g_sq_value: float = 0.0

    classification: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class ConditionalMappingStep:
    """A single step in the conditional mapping sequence."""
    step_number: int = 0
    step_name: str = ""
    input_quantity: str = ""
    output_quantity: str = ""
    formula: str = ""
    assumption_required: str = ""
    is_exact: bool = False
    is_route_specific: bool = False
    route_if_specific: str = ""
    is_terminal_block: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class ConditionalMappingSequence:
    """The beta_Q -> omega_0 -> m^2 -> V -> w mapping-and-block sequence.

    This is NOT a fully forward derivation chain.  Step 5 is a terminal
    anisotropy block (a constraint on single-w closure), not another
    derivation step.
    """
    steps: List[ConditionalMappingStep] = field(default_factory=list)
    n_steps: int = 0
    n_exact_observations: int = 0
    n_conditional_forward: int = 0
    n_route_specific: int = 0
    sequence_is_fully_exact: bool = False
    first_non_exact_step: int = 0
    has_terminal_anisotropy_block: bool = True

    # Conditionality flags (for public API return)
    is_conditional: bool = True
    requires_route_a: bool = True
    requires_isotropy: bool = True
    valid_for_collapse: bool = False
    unique: bool = False

    notes: List[str] = field(default_factory=list)


@dataclass
class AnisotropyAnalysis:
    """Whether the barrier sector is isotropic or anisotropic."""
    cosmo_sector_isotropic: bool = True
    cosmo_single_w_sufficient: bool = True
    collapse_sector_anisotropic: bool = True
    collapse_needs_wr_and_wperp: bool = True
    single_w_insufficient_for_collapse: bool = True

    cosmo_tphi_form: str = ""
    collapse_tphi_form: str = ""
    anisotropy_source: str = ""
    isotropy_source: str = ""

    notes: List[str] = field(default_factory=list)


@dataclass
class CandidateScalarPotential:
    """V(Phi) candidate from the KG Route A mass-term identification.

    NOT derived from beta_Q alone.  Requires Route A/KG identification,
    canonical kinetic structure, and mass-term identification m^2 = 1/tau^2.
    """
    form: str = ""
    origin: str = ""
    is_unique: bool = False
    is_route_specific: bool = True
    route: str = ""
    not_from_beta_Q_alone: bool = True
    additional_identifications: List[str] = field(default_factory=list)

    m_squared: float = 0.0
    tau_eff_used: float = 0.0

    free_functions_remaining: List[str] = field(default_factory=list)
    free_functions_removed: List[str] = field(default_factory=list)
    n_free_before: int = 0
    n_free_after: int = 0

    w_at_equilibrium: float = 0.0
    w_at_equilibrium_scope: str = ""
    rho_plus_p_at_equilibrium: float = 0.0

    other_admissible_V_forms: List[str] = field(default_factory=list)

    notes: List[str] = field(default_factory=list)
    nonclaims: List[str] = field(default_factory=list)


@dataclass
class DegeneracyReductionAssessment:
    """Does specifying V(Phi) break the Phase VI degeneracy?"""
    reduces_route_a: bool = True
    reduces_route_b: bool = False
    reduces_route_c: bool = False
    reduces_route_d_not_applicable: bool = True
    fully_breaks_degeneracy: bool = False

    route_a_free_before: int = 0
    route_a_free_after: int = 0
    route_b_free_before: int = 0
    route_b_free_after: int = 0
    route_c_free_before: int = 0
    route_c_free_after: int = 0

    closure_classification: str = ""
    closure_enum: ClosureClassification = ClosureClassification.PARTIALLY_CLOSING

    source_degeneracy_broken: bool = False
    source_degeneracy_reason: str = ""

    notes: List[str] = field(default_factory=list)


@dataclass
class NECCompatibilityCheck:
    """Compatibility of w_Phi = -1 with Phase V NEC indication.

    SCOPE: This NEC check applies ONLY to the isotropic Route A
    candidate closure.  It does NOT constitute a full anisotropic
    collapse-sector NEC analysis (which would require separate
    rho + p_r and rho + p_perp conditions).
    """
    w_at_equilibrium: float = 0.0
    rho_plus_p_at_equilibrium: float = 0.0

    nec_marginal_at_equilibrium: bool = True
    nec_violation_from_phase_v: bool = True
    phase_v_nec_is_constitutive: bool = True

    candidate_v_compatible_with_nec: bool = True
    no_conflict: bool = True

    rho_plus_p_sign: str = ""
    interpretation: str = ""

    scope_is_isotropic_route_a_only: bool = True
    not_full_collapse_nec_analysis: bool = True

    notes: List[str] = field(default_factory=list)


@dataclass
class LapseImpactAssessment:
    """Does the EOS/potential closure improve lapse determination?"""
    improves_lapse_determination: bool = False
    obstruction_lifted: bool = False
    phase_v_obstruction_unchanged: bool = True

    reason_no_improvement: str = ""
    tphi_still_constitutive: bool = True
    specific_v_does_not_resolve_metric: bool = True

    notes: List[str] = field(default_factory=list)


@dataclass
class Phase6Reconfirmation:
    """All Phase VI results survive Phase VII."""
    source_degeneracy_preserved: bool = True
    tphi_underdetermination_preserved: bool = True
    route_assessment_preserved: bool = True
    admissibility_preserved: bool = True
    status_ladder_preserved: bool = True
    phase5_results_preserved: bool = True
    all_preserved: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class StatusLadderUpdate:
    """Status ladder update from Phase VI to Phase VII."""
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
    tphi_changed: bool = False

    eos_closure_status: str = ""
    degeneracy_status: str = ""

    no_level_weakened: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class EOSPotentialResult:
    """Master result: Phase VII EOS / Potential Closure from beta_Q."""
    valid: bool = False

    eos_admissibility: Optional[EOSAdmissibilityTest] = None
    conditional_sequence: Optional[ConditionalMappingSequence] = None
    anisotropy: Optional[AnisotropyAnalysis] = None
    candidate_potential: Optional[CandidateScalarPotential] = None
    degeneracy_assessment: Optional[DegeneracyReductionAssessment] = None
    nec_compatibility: Optional[NECCompatibilityCheck] = None
    lapse_impact: Optional[LapseImpactAssessment] = None

    phase6_reconfirmation: Optional[Phase6Reconfirmation] = None
    status_ladder: Optional[StatusLadderUpdate] = None

    nonclaims: List[str] = field(default_factory=list)

    closure_classification: str = ""
    closure_enum: ClosureClassification = ClosureClassification.UNRESOLVED

    approx_status: str = ""
    remaining_obstructions: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Builder functions
# ================================================================

def build_eos_admissibility_test(
    beta_Q: float = BETA_Q,
    alpha_vac: float = ALPHA_VAC,
) -> EOSAdmissibilityTest:
    """Test whether beta_Q is interpretable as an EOS scaling exponent."""
    ea = EOSAdmissibilityTest()

    ea.beta_Q_is_eos_exponent = False
    ea.beta_Q_is_stiffness_exponent = True
    ea.requires_perfect_fluid = True
    ea.requires_isotropy = True
    ea.anisotropy_required_for_collapse = True
    ea.single_w_sufficient = False
    ea.single_w_sufficient_for_cosmo = True
    ea.conditional_mapping_exists = True

    # omega_0^2 = beta_Q * omega_g^2  (EXACT, from field_equations.py:450)
    # Using a representative omega_g^2 = 1.0 for structural verification
    ea.omega_g_sq_value = 1.0
    ea.omega_0_sq_value = beta_Q * ea.omega_g_sq_value
    ea.omega_0_sq_exact = True

    ea.assumptions_for_mapping = [
        (
            "KG Route A identification: the barrier natural frequency "
            "omega_0 is identified with the KG mass parameter via "
            "m^2 = omega_0^2 = beta_Q * omega_g^2."
        ),
        (
            "Canonical kinetic structure: the scalar field has "
            "standard kinetic term -(1/2) g^ab nabla_a Phi nabla_b Phi."
        ),
        (
            "Mass-term identification: V(Phi) = m^2 Phi^2 / 2 = "
            "Phi^2 / (2 tau^2) from the KG mass term."
        ),
        (
            "Isotropy: the effective EOS w_Phi = p/rho requires "
            "isotropic pressure (valid for cosmo, NOT for collapse)."
        ),
        (
            "Equilibrium evaluation: w_Phi is computed at the "
            "equilibrium point Phi = X, where dPhi/dt = 0."
        ),
    ]

    ea.classification = ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value

    ea.notes = [
        (
            "beta_Q enters the barrier dynamics through the endpoint "
            "law R_eq/r_s = epsilon_Q^(1/beta_Q) and the natural "
            "frequency omega_0^2 = beta_Q * omega_g^2.  These are "
            "barrier-geometry relations, not EOS relations."
        ),
        (
            "The mapping to an EOS parameter is CONDITIONAL on the "
            "KG Route A identification and isotropy assumptions."
        ),
        (
            "The collapse sector is anisotropic (p_r != p_t), so a "
            "single w_Phi is structurally insufficient there."
        ),
    ]

    return ea


def build_conditional_mapping_sequence(
    beta_Q: float = BETA_Q,
    alpha_vac: float = ALPHA_VAC,
) -> ConditionalMappingSequence:
    """Build the conditional mapping-and-block sequence."""
    seq = ConditionalMappingSequence()

    # Step 1: beta_Q -> omega_0^2 (EXACT)
    s1 = ConditionalMappingStep(
        step_number=1,
        step_name="barrier_frequency",
        input_quantity="beta_Q",
        output_quantity="omega_0^2",
        formula="omega_0^2 = beta_Q * omega_g^2",
        assumption_required="none",
        is_exact=True,
        is_route_specific=False,
        route_if_specific="",
        is_terminal_block=False,
        notes=[
            "EXACT: from barrier restoring force analysis.",
            "Source: field_equations.py:450, action_principle.py:663.",
        ],
    )

    # Step 2: omega_0^2 -> m^2 (CONDITIONAL, Route A)
    s2 = ConditionalMappingStep(
        step_number=2,
        step_name="kg_mass_identification",
        input_quantity="omega_0^2",
        output_quantity="m^2 = 1/tau^2",
        formula="m^2 = omega_0^2 (identified with KG mass parameter)",
        assumption_required=(
            "KG Route A: the barrier natural frequency is identified "
            "with the scalar field mass."
        ),
        is_exact=False,
        is_route_specific=True,
        route_if_specific=ROUTE_A,
        is_terminal_block=False,
        notes=[
            "CONDITIONAL: Route A specific.",
            "The identification omega_0 = m is an assumption, not derived.",
        ],
    )

    # Step 3: m^2 -> V(Phi) (CONDITIONAL, Route A)
    s3 = ConditionalMappingStep(
        step_number=3,
        step_name="potential_construction",
        input_quantity="m^2",
        output_quantity="V(Phi) = m^2 Phi^2 / 2",
        formula="V(Phi) = Phi^2 / (2 tau^2)",
        assumption_required=(
            "Canonical KG mass term: the potential is purely quadratic."
        ),
        is_exact=False,
        is_route_specific=True,
        route_if_specific=ROUTE_A,
        is_terminal_block=False,
        notes=[
            "CONDITIONAL: assumes canonical quadratic potential.",
            "Other potential forms (Phi^4, etc.) are equally compatible.",
        ],
    )

    # Step 4: V(Phi) -> w_Phi at equilibrium (CONDITIONAL)
    s4 = ConditionalMappingStep(
        step_number=4,
        step_name="equilibrium_eos",
        input_quantity="V(Phi) + canonical kinetic",
        output_quantity="w_Phi = -1 at equilibrium",
        formula=(
            "w_Phi = p_Phi / rho_Phi = -1 at Phi = X (steady state)"
        ),
        assumption_required=(
            "Isotropy (perfect-fluid form) and evaluation at "
            "equilibrium Phi = X."
        ),
        is_exact=False,
        is_route_specific=True,
        route_if_specific=ROUTE_A,
        is_terminal_block=False,
        notes=[
            "CONDITIONAL: requires isotropy AND equilibrium.",
            "Valid for cosmological sector; NOT for collapse.",
            "Source: galley_memory.py:426-428, 601.",
        ],
    )

    # Step 5: Anisotropy block (EXACT observation — terminal block)
    s5 = ConditionalMappingStep(
        step_number=5,
        step_name="anisotropy_block",
        input_quantity="single w_Phi",
        output_quantity="BLOCKED for collapse sector",
        formula="T^Phi = diag(-rho, p_r, p_t, p_t) with p_r != p_t",
        assumption_required="none (this is an exact structural observation)",
        is_exact=True,
        is_route_specific=False,
        route_if_specific="",
        is_terminal_block=True,
        notes=[
            "EXACT observation: collapse sector is anisotropic.",
            "A single w_Phi cannot close the collapse sector.",
            "Source: memory_tensor.py:56-58, 264, 320-330.",
            "This is a constraint/block, NOT a derivation step.",
        ],
    )

    seq.steps = [s1, s2, s3, s4, s5]
    seq.n_steps = 5
    seq.n_exact_observations = 2     # steps 1, 5
    seq.n_conditional_forward = 3    # steps 2, 3, 4
    seq.n_route_specific = 3         # steps 2, 3, 4
    seq.sequence_is_fully_exact = False
    seq.first_non_exact_step = 2
    seq.has_terminal_anisotropy_block = True

    seq.is_conditional = True
    seq.requires_route_a = True
    seq.requires_isotropy = True
    seq.valid_for_collapse = False
    seq.unique = False

    seq.notes = [
        (
            "This is a conditional mapping-and-block sequence, NOT a "
            "fully forward derivation chain."
        ),
        (
            "Step 1 (beta_Q -> omega_0^2) is the only exact forward "
            "step.  Steps 2-4 each introduce additional assumptions."
        ),
        (
            "Step 5 is a terminal anisotropy block: it constrains "
            "single-w closure, not another derivation step."
        ),
    ]

    return seq


def build_anisotropy_analysis() -> AnisotropyAnalysis:
    """Analyze whether barrier sector is isotropic or anisotropic."""
    aa = AnisotropyAnalysis()

    aa.cosmo_sector_isotropic = True
    aa.cosmo_single_w_sufficient = True
    aa.collapse_sector_anisotropic = True
    aa.collapse_needs_wr_and_wperp = True
    aa.single_w_insufficient_for_collapse = True

    aa.cosmo_tphi_form = (
        "T^Phi_mu_nu = (rho_Phi + p_Phi) u_mu u_nu + p_Phi g_mu_nu "
        "(perfect fluid, isotropic)"
    )
    aa.collapse_tphi_form = (
        "T^Phi_mu_nu = diag(-rho_Phi, p_r, p_t, p_t) "
        "(anisotropic, p_r != p_t in general)"
    )
    aa.anisotropy_source = (
        "memory_tensor.py lines 56-58, 264, 320-330, 349"
    )
    aa.isotropy_source = "memory_tensor.py lines 53-54"

    aa.notes = [
        (
            "The cosmological (FRW) sector is isotropic: T^Phi takes "
            "perfect-fluid form.  A single w_Phi is sufficient."
        ),
        (
            "The collapse (spherical) sector is anisotropic: radial "
            "and tangential pressures differ (p_r != p_t).  A single "
            "w_Phi is NOT sufficient; one needs (w_r, w_perp)."
        ),
        (
            "This anisotropy is a hard structural block on any "
            "single-w_Phi EOS closure for the collapse sector."
        ),
    ]

    return aa


def build_candidate_scalar_potential(
    beta_Q: float = BETA_Q,
    tau_eff: float = 1.0,
) -> CandidateScalarPotential:
    """Build candidate V(Phi) from KG Route A mass-term identification."""
    cp = CandidateScalarPotential()

    cp.form = "V(Phi) = Phi^2 / (2 tau_eff^2)"
    cp.origin = "KG mass term m^2 = 1/tau_eff^2"
    cp.is_unique = False
    cp.is_route_specific = True
    cp.route = ROUTE_A
    cp.not_from_beta_Q_alone = True

    cp.additional_identifications = [
        "Route A / Klein-Gordon overdamped identification",
        "Canonical kinetic structure: -(1/2) g^ab nabla_a Phi nabla_b Phi",
        "Mass-term identification: m^2 = 1/tau_eff^2",
    ]

    if tau_eff > 0:
        cp.m_squared = 1.0 / (tau_eff ** 2)
    cp.tau_eff_used = tau_eff

    cp.free_functions_removed = [
        "V(Phi) — scalar potential (was: shape entirely free; now: "
        "fixed to Phi^2/(2 tau^2))"
    ]
    cp.free_functions_remaining = [
        "J[g, T] — source coupling functional form (still free)"
    ]
    cp.n_free_before = 2   # V, J
    cp.n_free_after = 1    # J

    cp.w_at_equilibrium = -1.0
    cp.w_at_equilibrium_scope = (
        "Under isotropic Route A canonical-scalar equilibrium "
        "interpretation only — NOT a general barrier-sector statement."
    )
    cp.rho_plus_p_at_equilibrium = 0.0

    cp.other_admissible_V_forms = [
        "V(Phi) = lambda Phi^4 / 4 (quartic self-interaction)",
        "V(Phi) = m^2 Phi^2 / 2 + lambda Phi^4 / 4 (polynomial)",
        "V(Phi) = V_0 (1 - exp(-Phi/Phi_0))^2 (non-polynomial)",
        "V(Phi) = V_0 cosh(Phi/Phi_0) - 1 (hyperbolic)",
    ]

    cp.notes = [
        (
            "V(Phi) = Phi^2/(2 tau^2) is the simplest KG mass-term "
            "potential.  Source: galley_memory.py:392, 422, 478."
        ),
        (
            "This potential is NOT derived from beta_Q alone.  It "
            "requires the additional Route A/KG identification, "
            "canonical kinetic structure, and mass-term identification."
        ),
        (
            "Other V(Phi) forms are equally compatible with the "
            "existing GRUT constraints.  Source: galley_memory.py:612."
        ),
    ]

    cp.nonclaims = [
        "V(Phi) is one admissible potential; it is NOT unique.",
        (
            "Different V(Phi) choices give different T^Phi and "
            "different equilibrium EOS."
        ),
        (
            "The candidate is Route A specific; Routes B and C have "
            "different free-function structures."
        ),
    ]

    return cp


def build_degeneracy_reduction_assessment() -> DegeneracyReductionAssessment:
    """Assess whether V(Phi) breaks the Phase VI degeneracy."""
    dr = DegeneracyReductionAssessment()

    dr.reduces_route_a = True
    dr.reduces_route_b = False
    dr.reduces_route_c = False
    dr.reduces_route_d_not_applicable = True
    dr.fully_breaks_degeneracy = False

    dr.route_a_free_before = 2   # V, J
    dr.route_a_free_after = 1    # J
    dr.route_b_free_before = 2   # K_diss, L
    dr.route_b_free_after = 2    # unchanged
    dr.route_c_free_before = 1   # kernel
    dr.route_c_free_after = 1    # unchanged

    dr.closure_classification = ClosureClassification.PARTIALLY_CLOSING.value
    dr.closure_enum = ClosureClassification.PARTIALLY_CLOSING

    dr.source_degeneracy_broken = False
    dr.source_degeneracy_reason = (
        "The equilibrium source degeneracy (Phase VI) is NOT broken "
        "by specifying V(Phi).  The source equation 0 = 0 at "
        "equilibrium holds regardless of V because self-healing "
        "(X - Phi = 0) makes the source term vanish independent of "
        "the action's free functions."
    )

    dr.notes = [
        (
            "Specifying V(Phi) = Phi^2/(2 tau^2) reduces Route A "
            "from 2 free functions (V, J) to 1 (J)."
        ),
        (
            "Routes B and C are NOT affected: their free functions "
            "(K_diss/L and kernel K) are independent of V."
        ),
        (
            "The Phase VI equilibrium source degeneracy is NOT "
            "broken because the source equation trivializes at "
            "equilibrium regardless of V."
        ),
        (
            "Classification: partially_closing — the degeneracy is "
            "reduced within Route A but not eliminated."
        ),
    ]

    return dr


def build_nec_compatibility_check() -> NECCompatibilityCheck:
    """Check NEC compatibility of w_Phi = -1 (Route A isotropic only)."""
    nc = NECCompatibilityCheck()

    nc.w_at_equilibrium = -1.0
    nc.rho_plus_p_at_equilibrium = 0.0

    nc.nec_marginal_at_equilibrium = True
    nc.nec_violation_from_phase_v = True
    nc.phase_v_nec_is_constitutive = True

    nc.candidate_v_compatible_with_nec = True
    nc.no_conflict = True

    nc.rho_plus_p_sign = "zero_at_equilibrium"
    nc.interpretation = (
        "NEC-saturating: rho + p = 0 at equilibrium.  This is "
        "marginally on the NEC boundary, neither violating nor "
        "satisfying it with a definite sign."
    )

    nc.scope_is_isotropic_route_a_only = True
    nc.not_full_collapse_nec_analysis = True

    nc.notes = [
        (
            "w_Phi = -1 implies rho + p = 0 at equilibrium (de Sitter-like).  "
            "This is NEC-saturating, not NEC-violating."
        ),
        (
            "Phase V indicated NEC violation at the constitutive level "
            "for sub-horizon barrier support.  w = -1 at equilibrium "
            "does not conflict with this: the violation can occur "
            "off-equilibrium or through anisotropic components."
        ),
        (
            "SCOPE: This NEC check applies ONLY to the isotropic "
            "Route A candidate closure.  It does NOT constitute a "
            "full anisotropic collapse-sector NEC analysis, which "
            "would require separate rho + p_r and rho + p_perp "
            "conditions."
        ),
    ]

    return nc


def build_lapse_impact_assessment() -> LapseImpactAssessment:
    """Assess whether EOS/potential closure improves lapse."""
    la = LapseImpactAssessment()

    la.improves_lapse_determination = False
    la.obstruction_lifted = False
    la.phase_v_obstruction_unchanged = True

    la.reason_no_improvement = (
        "The Phase V lapse obstruction (A_eff < 0 for every finite "
        "beta_Q > 0) is structural: it stems from T^Phi being "
        "constitutive/effective rather than Lagrangian-derived.  "
        "Specifying V(Phi) for Route A does not change this because: "
        "(1) T^Phi remains constitutive in the existing framework, "
        "(2) V(Phi) alone does not determine a complete coupled "
        "Einstein-scalar system, and (3) the source coupling J "
        "remains free."
    )
    la.tphi_still_constitutive = True
    la.specific_v_does_not_resolve_metric = True

    la.notes = [
        (
            "The Phase V obstruction is about T^Phi being "
            "schematic/effective (not Lagrangian-derived from a "
            "coupled action).  Specifying V does not resolve this."
        ),
        (
            "Even with V(Phi) = Phi^2/(2 tau^2), the full interior "
            "metric requires solving G_ab = 8piG(T_matter + T^Phi) "
            "with a fully specified T^Phi, which is still not available."
        ),
    ]

    return la


def build_phase6_reconfirmation() -> Phase6Reconfirmation:
    """Reconfirm all Phase VI results survive Phase VII."""
    p6 = Phase6Reconfirmation()
    p6.source_degeneracy_preserved = True
    p6.tphi_underdetermination_preserved = True
    p6.route_assessment_preserved = True
    p6.admissibility_preserved = True
    p6.status_ladder_preserved = True
    p6.phase5_results_preserved = True
    p6.all_preserved = True

    p6.notes = [
        (
            "Phase VII adds new classification results but does NOT "
            "invalidate any Phase VI or Phase V result."
        ),
        (
            "The equilibrium source degeneracy theorem is PRESERVED: "
            "specifying V does not break the source equation degeneracy."
        ),
    ]

    return p6


def build_status_ladder_update() -> StatusLadderUpdate:
    """Build the Phase VI to Phase VII status ladder transition."""
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

    sl.tphi_before = TPHI_STATUS_PHASE_VI
    sl.tphi_after = TPHI_STATUS_PHASE_VII
    sl.tphi_changed = False  # already sharpened in Phase VI

    sl.eos_closure_status = ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
    sl.degeneracy_status = ClosureClassification.PARTIALLY_CLOSING.value

    sl.no_level_weakened = True

    sl.notes = [
        "Level 1 (exact barrier ratio): UNCHANGED.",
        "Level 2 (constitutive-derived proxy): UNCHANGED.",
        "Level 3 (constitutive lapse promotion obstructed): UNCHANGED.",
        (
            "T^Phi characterization: UNCHANGED (already sharpened "
            "in Phase VI to 'schematic_effective_equilibrium_degenerate')."
        ),
        "No level is weakened by Phase VII.",
        (
            "New Phase VII sub-classifications: eos_closure = "
            "admissible_but_nonunique, degeneracy = partially_closing."
        ),
    ]

    return sl


# ================================================================
# Public API functions (matching spec)
# ================================================================

def test_eos_admissibility_from_beta(
    beta_Q: float = BETA_Q,
    alpha_vac: float = ALPHA_VAC,
) -> EOSAdmissibilityTest:
    """Test whether beta_Q is interpretable as an EOS scaling exponent."""
    return build_eos_admissibility_test(beta_Q, alpha_vac)


def assess_conditional_eos_from_beta(
    beta_Q: float = BETA_Q,
    alpha_vac: float = ALPHA_VAC,
) -> ConditionalMappingSequence:
    """Assess the conditional mapping from beta_Q to w_Phi.

    This is a conditional inference, NOT a derivation.  The return
    object carries explicit conditionality flags:
      is_conditional=True, requires_route_a=True,
      requires_isotropy=True, valid_for_collapse=False, unique=False.
    """
    return build_conditional_mapping_sequence(beta_Q, alpha_vac)


def assess_degeneracy_reduction() -> DegeneracyReductionAssessment:
    """Assess whether V(Phi) breaks the Phase VI degeneracy."""
    return build_degeneracy_reduction_assessment()


def assess_lapse_impact() -> LapseImpactAssessment:
    """Assess whether EOS/potential closure improves lapse."""
    return build_lapse_impact_assessment()


# ================================================================
# Master analysis
# ================================================================

def compute_eos_potential_analysis(
    beta_Q: float = BETA_Q,
    alpha_vac: float = ALPHA_VAC,
    tau_eff: float = 1.0,
) -> EOSPotentialResult:
    """Master analysis: Phase VII EOS / Potential Closure from beta_Q.

    Steps:
      1. Test EOS admissibility
      2. Build conditional mapping sequence
      3. Analyze anisotropy
      4. Build candidate scalar potential
      5. Assess degeneracy reduction
      6. Check NEC compatibility
      7. Assess lapse impact
      8. Reconfirm Phase VI
      9. Update status ladder
      10. Assemble nonclaims (>= 15)
      11. Set classification
      12. Populate diagnostics
    """
    result = EOSPotentialResult()

    # 1-9: Build all sub-results
    result.eos_admissibility = build_eos_admissibility_test(beta_Q, alpha_vac)
    result.conditional_sequence = build_conditional_mapping_sequence(
        beta_Q, alpha_vac
    )
    result.anisotropy = build_anisotropy_analysis()
    result.candidate_potential = build_candidate_scalar_potential(
        beta_Q, tau_eff
    )
    result.degeneracy_assessment = build_degeneracy_reduction_assessment()
    result.nec_compatibility = build_nec_compatibility_check()
    result.lapse_impact = build_lapse_impact_assessment()
    result.phase6_reconfirmation = build_phase6_reconfirmation()
    result.status_ladder = build_status_ladder_update()

    # 10: Nonclaims (>= 15)
    result.nonclaims = [
        (
            "Phase VII does NOT derive an equation of state for the "
            "barrier sector from beta_Q."
        ),
        (
            "beta_Q is a compactness-dependent barrier steepness "
            "exponent, NOT an EOS exponent."
        ),
        (
            "The conditional mapping beta_Q -> w_Phi exists ONLY "
            "under KG Route A + canonical kinetic term + isotropy."
        ),
        (
            "The collapse sector is anisotropic: T^Phi = "
            "diag(-rho, p_r, p_t, p_t); a single w_Phi is "
            "insufficient for the collapse sector."
        ),
        (
            "V(Phi) = Phi^2/(2 tau^2) is one admissible potential "
            "choice; it is NOT unique."
        ),
        (
            "Other V(Phi) forms (quartic, polynomial, non-polynomial) "
            "are equally compatible with existing GRUT constraints."
        ),
        (
            "V(Phi) reduces Route A free functions (V fixed, J still "
            "free) but does NOT break the full degeneracy."
        ),
        (
            "Routes B and C are NOT affected by specifying V(Phi)."
        ),
        (
            "The equilibrium source degeneracy (Phase VI) is NOT "
            "broken by specifying V: the source equation 0 = 0 at "
            "equilibrium holds regardless of V."
        ),
        (
            "w_Phi = -1 at equilibrium is NEC-saturating (rho + p = 0), "
            "compatible with Phase V NEC indication.  This NEC check "
            "applies only to the isotropic Route A candidate, NOT a "
            "full anisotropic collapse-sector NEC analysis."
        ),
        (
            "The candidate V(Phi) is NOT derived from beta_Q alone; "
            "it requires the additional Route A/KG identification, "
            "canonical kinetic structure, and mass-term identification "
            "m^2 = 1/tau^2."
        ),
        (
            "The EOS/potential closure does NOT improve lapse "
            "determination; the Phase V obstruction persists."
        ),
        (
            "No Phase VI result is weakened or invalidated."
        ),
        (
            "No observational predictions are changed."
        ),
        (
            "Classification: admissible_but_nonunique (EOS mapping) "
            "and partially_closing (degeneracy reduction)."
        ),
    ]

    # 11: Classification
    result.closure_classification = (
        ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
    )
    result.closure_enum = ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE

    # 12: Diagnostics and summary
    result.approx_status = (
        "Phase VII: beta_Q is a barrier steepness exponent, NOT an "
        "EOS exponent.  Conditional mapping to w_Phi and V(Phi) exists "
        "under Route A + isotropy + canonical KG assumptions.  "
        "Collapse sector is anisotropic (single w insufficient).  "
        "V(Phi) partially reduces Route A degeneracy (2 -> 1 free "
        "functions), does NOT break full degeneracy.  Lapse obstruction "
        "UNCHANGED.  All Phase VI results: PRESERVED."
    )

    result.remaining_obstructions = [
        (
            "A unique covariant action for the barrier sector — "
            "not determined even with V(Phi) specified."
        ),
        (
            "The source coupling J[g, T] — still free within Route A."
        ),
        (
            "Anisotropic closure for the collapse sector — single "
            "w_Phi insufficient; needs (w_r, w_perp)."
        ),
        (
            "Full T^Phi from coupled Einstein-scalar system — "
            "requires complete action + gravity coupling."
        ),
    ]

    result.diagnostics = {
        "beta_Q_is_eos_exponent": False,
        "beta_Q_is_stiffness_exponent": True,
        "conditional_mapping_exists": True,
        "n_mapping_steps": result.conditional_sequence.n_steps,
        "n_exact_observations": (
            result.conditional_sequence.n_exact_observations
        ),
        "n_conditional_forward": (
            result.conditional_sequence.n_conditional_forward
        ),
        "has_terminal_anisotropy_block": True,
        "collapse_anisotropic": True,
        "single_w_sufficient": False,
        "v_phi_unique": False,
        "v_phi_route_specific": True,
        "not_from_beta_Q_alone": True,
        "route_a_free_before": 2,
        "route_a_free_after": 1,
        "fully_breaks_degeneracy": False,
        "source_degeneracy_broken": False,
        "w_at_equilibrium": -1.0,
        "nec_marginal": True,
        "nec_scope_isotropic_route_a_only": True,
        "improves_lapse": False,
        "phase6_preserved": True,
        "closure_classification": (
            ClosureClassification.ADMISSIBLE_BUT_NONUNIQUE.value
        ),
        "degeneracy_classification": (
            ClosureClassification.PARTIALLY_CLOSING.value
        ),
        "n_nonclaims": len(result.nonclaims),
    }

    result.valid = True
    return result


# ================================================================
# Serialization
# ================================================================

def _eos_admissibility_to_dict(ea: EOSAdmissibilityTest) -> Dict[str, Any]:
    return {
        "beta_Q_is_eos_exponent": ea.beta_Q_is_eos_exponent,
        "beta_Q_is_stiffness_exponent": ea.beta_Q_is_stiffness_exponent,
        "requires_perfect_fluid": ea.requires_perfect_fluid,
        "requires_isotropy": ea.requires_isotropy,
        "anisotropy_required_for_collapse": (
            ea.anisotropy_required_for_collapse
        ),
        "single_w_sufficient": ea.single_w_sufficient,
        "single_w_sufficient_for_cosmo": ea.single_w_sufficient_for_cosmo,
        "conditional_mapping_exists": ea.conditional_mapping_exists,
        "assumptions_for_mapping": ea.assumptions_for_mapping,
        "omega_0_sq_exact": ea.omega_0_sq_exact,
        "omega_0_sq_value": ea.omega_0_sq_value,
        "classification": ea.classification,
        "notes": ea.notes,
    }


def _mapping_step_to_dict(s: ConditionalMappingStep) -> Dict[str, Any]:
    return {
        "step_number": s.step_number,
        "step_name": s.step_name,
        "input_quantity": s.input_quantity,
        "output_quantity": s.output_quantity,
        "formula": s.formula,
        "assumption_required": s.assumption_required,
        "is_exact": s.is_exact,
        "is_route_specific": s.is_route_specific,
        "route_if_specific": s.route_if_specific,
        "is_terminal_block": s.is_terminal_block,
        "notes": s.notes,
    }


def _mapping_sequence_to_dict(
    seq: ConditionalMappingSequence,
) -> Dict[str, Any]:
    return {
        "steps": [_mapping_step_to_dict(s) for s in seq.steps],
        "n_steps": seq.n_steps,
        "n_exact_observations": seq.n_exact_observations,
        "n_conditional_forward": seq.n_conditional_forward,
        "sequence_is_fully_exact": seq.sequence_is_fully_exact,
        "first_non_exact_step": seq.first_non_exact_step,
        "has_terminal_anisotropy_block": seq.has_terminal_anisotropy_block,
        "is_conditional": seq.is_conditional,
        "requires_route_a": seq.requires_route_a,
        "requires_isotropy": seq.requires_isotropy,
        "valid_for_collapse": seq.valid_for_collapse,
        "unique": seq.unique,
        "notes": seq.notes,
    }


def _anisotropy_to_dict(aa: AnisotropyAnalysis) -> Dict[str, Any]:
    return {
        "cosmo_sector_isotropic": aa.cosmo_sector_isotropic,
        "cosmo_single_w_sufficient": aa.cosmo_single_w_sufficient,
        "collapse_sector_anisotropic": aa.collapse_sector_anisotropic,
        "collapse_needs_wr_and_wperp": aa.collapse_needs_wr_and_wperp,
        "single_w_insufficient_for_collapse": (
            aa.single_w_insufficient_for_collapse
        ),
        "cosmo_tphi_form": aa.cosmo_tphi_form,
        "collapse_tphi_form": aa.collapse_tphi_form,
        "notes": aa.notes,
    }


def _candidate_potential_to_dict(
    cp: CandidateScalarPotential,
) -> Dict[str, Any]:
    return {
        "form": cp.form,
        "origin": cp.origin,
        "is_unique": cp.is_unique,
        "is_route_specific": cp.is_route_specific,
        "route": cp.route,
        "not_from_beta_Q_alone": cp.not_from_beta_Q_alone,
        "additional_identifications": cp.additional_identifications,
        "m_squared": cp.m_squared,
        "n_free_before": cp.n_free_before,
        "n_free_after": cp.n_free_after,
        "w_at_equilibrium": cp.w_at_equilibrium,
        "w_at_equilibrium_scope": cp.w_at_equilibrium_scope,
        "rho_plus_p_at_equilibrium": cp.rho_plus_p_at_equilibrium,
        "other_admissible_V_forms": cp.other_admissible_V_forms,
        "notes": cp.notes,
        "nonclaims": cp.nonclaims,
    }


def _degeneracy_to_dict(
    dr: DegeneracyReductionAssessment,
) -> Dict[str, Any]:
    return {
        "reduces_route_a": dr.reduces_route_a,
        "reduces_route_b": dr.reduces_route_b,
        "reduces_route_c": dr.reduces_route_c,
        "fully_breaks_degeneracy": dr.fully_breaks_degeneracy,
        "route_a_free_before": dr.route_a_free_before,
        "route_a_free_after": dr.route_a_free_after,
        "route_b_free_before": dr.route_b_free_before,
        "route_b_free_after": dr.route_b_free_after,
        "route_c_free_before": dr.route_c_free_before,
        "route_c_free_after": dr.route_c_free_after,
        "closure_classification": dr.closure_classification,
        "source_degeneracy_broken": dr.source_degeneracy_broken,
        "source_degeneracy_reason": dr.source_degeneracy_reason,
        "notes": dr.notes,
    }


def _nec_to_dict(nc: NECCompatibilityCheck) -> Dict[str, Any]:
    return {
        "w_at_equilibrium": nc.w_at_equilibrium,
        "rho_plus_p_at_equilibrium": nc.rho_plus_p_at_equilibrium,
        "nec_marginal_at_equilibrium": nc.nec_marginal_at_equilibrium,
        "no_conflict": nc.no_conflict,
        "scope_is_isotropic_route_a_only": (
            nc.scope_is_isotropic_route_a_only
        ),
        "not_full_collapse_nec_analysis": nc.not_full_collapse_nec_analysis,
        "interpretation": nc.interpretation,
        "notes": nc.notes,
    }


def _lapse_to_dict(la: LapseImpactAssessment) -> Dict[str, Any]:
    return {
        "improves_lapse_determination": la.improves_lapse_determination,
        "obstruction_lifted": la.obstruction_lifted,
        "phase_v_obstruction_unchanged": la.phase_v_obstruction_unchanged,
        "reason_no_improvement": la.reason_no_improvement,
        "tphi_still_constitutive": la.tphi_still_constitutive,
        "notes": la.notes,
    }


def _phase6_reconfirmation_to_dict(
    p6: Phase6Reconfirmation,
) -> Dict[str, Any]:
    return {
        "source_degeneracy_preserved": p6.source_degeneracy_preserved,
        "tphi_underdetermination_preserved": (
            p6.tphi_underdetermination_preserved
        ),
        "route_assessment_preserved": p6.route_assessment_preserved,
        "all_preserved": p6.all_preserved,
        "notes": p6.notes,
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
        "tphi_changed": sl.tphi_changed,
        "eos_closure_status": sl.eos_closure_status,
        "degeneracy_status": sl.degeneracy_status,
        "no_level_weakened": sl.no_level_weakened,
        "notes": sl.notes,
    }


def eos_potential_result_to_dict(
    result: EOSPotentialResult,
) -> Dict[str, Any]:
    """Serialize the master EOSPotentialResult to a dictionary."""
    d: Dict[str, Any] = {"valid": result.valid}

    if result.eos_admissibility is not None:
        d["eos_admissibility"] = _eos_admissibility_to_dict(
            result.eos_admissibility
        )
    if result.conditional_sequence is not None:
        d["conditional_sequence"] = _mapping_sequence_to_dict(
            result.conditional_sequence
        )
    if result.anisotropy is not None:
        d["anisotropy"] = _anisotropy_to_dict(result.anisotropy)
    if result.candidate_potential is not None:
        d["candidate_potential"] = _candidate_potential_to_dict(
            result.candidate_potential
        )
    if result.degeneracy_assessment is not None:
        d["degeneracy_assessment"] = _degeneracy_to_dict(
            result.degeneracy_assessment
        )
    if result.nec_compatibility is not None:
        d["nec_compatibility"] = _nec_to_dict(result.nec_compatibility)
    if result.lapse_impact is not None:
        d["lapse_impact"] = _lapse_to_dict(result.lapse_impact)
    if result.phase6_reconfirmation is not None:
        d["phase6_reconfirmation"] = _phase6_reconfirmation_to_dict(
            result.phase6_reconfirmation
        )
    if result.status_ladder is not None:
        d["status_ladder"] = _status_ladder_to_dict(result.status_ladder)

    d["nonclaims"] = result.nonclaims
    d["closure_classification"] = result.closure_classification
    d["approx_status"] = result.approx_status
    d["remaining_obstructions"] = result.remaining_obstructions
    d["diagnostics"] = result.diagnostics

    return d
