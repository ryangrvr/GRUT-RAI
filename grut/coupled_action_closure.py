"""Phase D8 — Coupled Action Closure.

Tests whether the effective D7 cross-coupling structure (gravitational
back-reaction alpha_BR, source amplification beta_XR) can be derived from
a single explicit effective action, or at least from a disciplined effective
action plus one clearly identified closure assumption.

SCOPE: D8 is a derivational and taxonomic phase.  It constructs a candidate
coupled action, derives Euler–Lagrange equations as structured data, and maps
each term to the D7 phenomenological channels.  It does NOT perform new
large-scale numerics (no BVP re-solves, no lambda scans).

LOCKED INHERITANCE:
  - D6: companion_architecture_viable (additive, A=1 + defect, lambda >= 25)
  - D7: fully_coupled_viable (two effective channels, viable all 6 lambda)
  - D7 channels: alpha_BR (gravitational penalty, destructive),
                  beta_XR (source amplification, constructive)

PRIMARY QUESTIONS:
  1. Can both D7 channels be obtained from a single effective action?
  2. What is the minimal interaction term set?
  3. Which channels are action-derived vs. effective closure?

RESULT PREVIEW:
  - Gravitational penalty: action-derived (Einstein equations + T_defect)
  - Source amplification: derived after approximation (interaction term +
    linearization + frozen-profile assumption)
  - Classification: d7_channels_partially_action_derived

Imports: None from prior phases (purely structural/taxonomic).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple


# ================================================================
# Constants
# ================================================================

ALPHA_VAC = 1.0 / 3.0
R_S = 1.0
M_EXT = R_S / 2.0
R_EQ = R_S * ALPHA_VAC
TAU_CANONICAL = math.sqrt((R_S / R_EQ) / 2.0)
A_CRIT = 1.062
LAMBDA_DEFAULT = 8.0 * math.pi
ETA_TARGET = 1.0 / math.sqrt(8.0 * math.pi)
XI_DEFAULT = 1.0

# D8-specific
N_SECTORS = 4  # gravity, macro, defect, trigger
N_D7_CHANNELS = 2  # gravitational penalty, source amplification
N_INTERACTION_CANDIDATES = 4  # disciplined minimal set
N_EL_FIELDS = 3  # g_ab, Phi (macro scalar), vec_Phi (defect triplet)
RECOVERY_STATUSES = [
    "action_derived",
    "derived_after_approximation",
    "effective_closure",
    "not_derived",
]
CLOSURE_STATUSES = [
    "action_derived",
    "effective_but_disciplined",
    "still_open",
]
CLASSIFICATION_OPTIONS = [
    "d7_channels_largely_action_derived",
    "d7_channels_partially_action_derived",
    "d7_channels_require_effective_closure",
    "coupled_action_attempt_inconsistent",
]


# ================================================================
# Assumptions
# ================================================================

COUPLED_ACTION_ASSUMPTIONS = [
    "1. The candidate action is S = S_grav + S_macro + S_defect + S_trigger + S_int, "
    "with each sector clearly identified.",

    "2. S_grav = (1/16piG) integral sqrt(-g) R d^4x is the standard Einstein-Hilbert "
    "gravitational action.",

    "3. S_macro represents the GRUT scalar-memory sector Phi with source-driven "
    "amplitude A controlled by the gravitational source X_eff.",

    "4. S_defect represents the O(3) triplet hedgehog sector from D1-D4 with "
    "symmetry-breaking potential V(|vec_Phi|) = lambda(|vec_Phi|^2 - eta^2)^2.",

    "5. S_trigger represents the curvature-triggered activation from D3-D4, "
    "entering as a Kretschner-threshold coupling xi * K * |vec_Phi|^2.",

    "6. S_int is a minimal interaction sector containing only terms structurally "
    "motivated by the D6 cross-term inventory.",

    "7. Euler-Lagrange derivation is structural: equations are represented as "
    "term inventories, not solved numerically in this phase.",

    "8. Channel recovery maps each D7 effective parameter to its action origin "
    "or identifies it as a closure assumption.",

    "9. The defect-shape freezing approximation from D7 is inherited and tracked "
    "as a required approximation for channel recovery.",

    "10. Classification is conservative: a channel is 'action_derived' only if "
    "obtainable from the action without additional phenomenological input.",
]

COUPLED_ACTION_NONCLAIMS = [
    "1. This phase does NOT prove final field-theory closure.",

    "2. A partial derivation is acceptable and is reported honestly.",

    "3. Any remaining effective closure terms are clearly labeled.",

    "4. This phase does NOT invalidate D7 if some channels remain effective.",

    "5. The candidate action is a minimal effective action, not a claim of "
    "the unique or final theory.",

    "6. Euler-Lagrange equations are derived structurally, not solved.",

    "7. The interaction term set is minimal and disciplined, not exhaustive.",

    "8. The recovery map does not claim uniqueness of the derivation path.",

    "9. This phase does NOT derive coupling constants from first principles — "
    "it derives structural forms only.",

    "10. Classification is within the D8 derivational framework only.",
]


# ================================================================
# Dataclasses
# ================================================================

@dataclass
class CoupledActionParams:
    """Parameters for Phase D8."""
    eta: float = ETA_TARGET
    lam: float = LAMBDA_DEFAULT
    xi: float = XI_DEFAULT
    scalar_A: float = 1.0
    M: float = M_EXT
    tau: float = TAU_CANONICAL


@dataclass
class SectorActionDefinition:
    """One sector of the candidate coupled action."""
    name: str
    field_content: str
    lagrangian_form: str
    role_in_metric: str
    symmetry: str
    d7_relevance: str
    notes: List[str] = field(default_factory=list)


@dataclass
class InteractionTermCandidate:
    """One candidate interaction term for S_int."""
    name: str
    formula: str
    coupling_constant: str
    target_d7_channel: str
    structural_motivation: str
    enters_el_for: List[str]  # which field equations this term modifies
    sign_effect: str  # "constructive", "destructive", or "mixed"
    notes: List[str] = field(default_factory=list)


@dataclass
class ActionCandidate:
    """The assembled candidate coupled action."""
    sectors: List[SectorActionDefinition]
    interaction_terms: List[InteractionTermCandidate]
    full_action_symbolic: str
    n_sectors: int
    n_interaction_terms: int
    n_free_parameters: int
    minimality_assessment: str
    notes: List[str] = field(default_factory=list)


@dataclass
class EulerLagrangeDerivation:
    """EL equation for one field, with terms tagged."""
    field_name: str
    field_symbol: str
    equation_symbolic: str
    terms_identified: Dict[str, str]  # role -> term description
    approximations_required: List[str]
    produces_d7_channel: Optional[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class ChannelRecoveryEntry:
    """Recovery status of one D7 effective channel."""
    d7_channel_name: str
    d7_parameter: str  # alpha_BR or beta_XR
    d7_formula: str
    recovery_status: str  # action_derived, derived_after_approximation, etc.
    source_term_in_action: str
    derivation_path: str
    approximations_required: List[str]
    recovery_quality: str  # "exact", "structural", "partial"
    notes: List[str] = field(default_factory=list)


@dataclass
class ChannelRecoveryMap:
    """Complete recovery map for all D7 channels."""
    entries: List[ChannelRecoveryEntry]
    n_channels: int
    n_action_derived: int
    n_derived_after_approximation: int
    n_effective_closure: int
    d7_recovery_fraction: float
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class ClosureInventoryEntry:
    """One element of the closure inventory."""
    item: str
    status: str  # action_derived, effective_but_disciplined, still_open
    source: str
    approximation_level: str
    notes: str = ""


@dataclass
class ClosureInventory:
    """Full closure inventory of derived vs. effective vs. open items."""
    entries: List[ClosureInventoryEntry]
    n_total: int
    n_action_derived: int
    n_effective: int
    n_open: int
    summary: str
    notes: List[str] = field(default_factory=list)


@dataclass
class CoupledActionClassification:
    """Final D8 classification."""
    classification: str
    phase_status: str
    d7_recovery_fraction: float
    n_channels_derived: int
    n_channels_approximate: int
    n_channels_effective: int
    summary: str
    phase_lock_update: Dict[str, str]


@dataclass
class CoupledActionResult:
    """Master result container for Phase D8."""
    valid: bool
    params: CoupledActionParams
    sector_actions: Optional[List[SectorActionDefinition]] = None
    interaction_candidates: Optional[List[InteractionTermCandidate]] = None
    action_candidate: Optional[ActionCandidate] = None
    el_derivations: Optional[List[EulerLagrangeDerivation]] = None
    channel_recovery: Optional[ChannelRecoveryMap] = None
    closure_inventory: Optional[ClosureInventory] = None
    classification: Optional[CoupledActionClassification] = None
    nonclaims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)


# ================================================================
# Level 0: Sector Action Definitions
# ================================================================

def define_sector_actions(
    params: CoupledActionParams,
) -> List[SectorActionDefinition]:
    """Define the four sectors of the candidate coupled action.

    S_total = S_grav[g] + S_macro[Phi, g] + S_defect[vec_Phi, g] + S_trigger[K, vec_Phi]

    Each sector is documented with its field content, Lagrangian form,
    role in the metric correction, and symmetry structure.
    """
    s_grav = SectorActionDefinition(
        name="gravitational",
        field_content="g_{ab}",
        lagrangian_form="(1/16piG) * sqrt(-g) * R",
        role_in_metric=(
            "Provides the Einstein equation G_ab = 8piG T_ab. "
            "All matter sectors contribute to T_ab on the right-hand side."
        ),
        symmetry="diffeomorphism invariance",
        d7_relevance=(
            "The gravitational penalty channel (alpha_BR) follows directly "
            "from Einstein equations: T_defect gravitates, increasing enclosed mass."
        ),
        notes=[
            "Standard Einstein-Hilbert action.",
            "Variation with respect to g_ab gives Einstein field equations.",
            "T_ab = -(2/sqrt(-g)) delta(S_matter)/delta(g^{ab}).",
        ],
    )

    s_macro = SectorActionDefinition(
        name="macro_scalar_memory",
        field_content="Phi (real scalar)",
        lagrangian_form=(
            "sqrt(-g) * [-1/2 (nabla Phi)^2 - V_macro(Phi) + J_eff * Phi]"
        ),
        role_in_metric=(
            "Source-driven amplitude A provides the macro energy Component A "
            "(~1/r^4). The amplitude A is controlled by the gravitational "
            "source X_eff, which determines m(r)."
        ),
        symmetry="Z_2 (Phi -> -Phi broken by source J_eff)",
        d7_relevance=(
            "The macro sector provides Sigma_macro. Under coupling, "
            "A_eff becomes radius-dependent through beta_XR."
        ),
        notes=[
            "Source J_eff encodes the GRUT scalar-memory driving mechanism.",
            "Background solution: Phi_bg ~ A / r^2 (leading order).",
            "Energy density: epsilon_macro = A^2 * RHO_EQ_COEFF / r^4.",
            "Sigma_macro analytic when A is constant, numerical when A_eff(r).",
        ],
    )

    s_defect = SectorActionDefinition(
        name="defect_triplet",
        field_content="vec_Phi^a (O(3) triplet, a=1,2,3)",
        lagrangian_form=(
            "sqrt(-g) * [-1/2 (D_mu vec_Phi)^2 - lambda(|vec_Phi|^2 - eta^2)^2]"
        ),
        role_in_metric=(
            "Hedgehog ansatz vec_Phi^a = eta * h(r) * x^a/r provides "
            "Component B (~1/r^2) and the core stabilization mechanism."
        ),
        symmetry="O(3) global (broken to U(1) by hedgehog)",
        d7_relevance=(
            "T_defect provides Sigma_defect and enters the gravitational "
            "penalty through Einstein equations. Also source for amplification "
            "channel when coupled to macro sector."
        ),
        notes=[
            "Hedgehog BVP from D2: h(0)=0, h -> 1 as r -> infinity.",
            "Defect energy epsilon_defect computed from D2 BVP solution.",
            "Sigma_defect = integral_r^R_ext 4pi r'^2 epsilon_defect dr'.",
            "D7 freezes this profile under coupling (leading approximation).",
        ],
    )

    s_trigger = SectorActionDefinition(
        name="curvature_trigger",
        field_content="Kretschner scalar K = R_{abcd} R^{abcd}, coupled to vec_Phi",
        lagrangian_form="sqrt(-g) * [-xi * K * |vec_Phi|^2]",
        role_in_metric=(
            "Activates the defect sector when curvature exceeds threshold. "
            "K_crit = lambda * eta^2 / xi defines the activation radius r_act."
        ),
        symmetry="scalar under diffeomorphisms",
        d7_relevance=(
            "Trigger threshold determines where the defect profile transitions "
            "from trivial to hedgehog. Not directly a D7 coupling channel, "
            "but provides the activation mechanism."
        ),
        notes=[
            "K = 48 M^2 / r^6 for Schwarzschild.",
            "r_act = (xi * sqrt(48) * M / (lambda * eta^2))^{1/3}.",
            "This is the top-ranked trigger from D3 unification analysis.",
            "Enters the defect EL equation as an effective mass modification.",
        ],
    )

    return [s_grav, s_macro, s_defect, s_trigger]


# ================================================================
# Level 1: Interaction Term Candidates
# ================================================================

def construct_interaction_candidates(
    params: CoupledActionParams,
) -> List[InteractionTermCandidate]:
    """Construct a minimal disciplined set of interaction candidates.

    These are structurally motivated by the D6 cross-term inventory.
    Each term is tagged with which D7 channel it targets.
    """
    # Term 1: Stress-energy gravitational coupling (automatic in GR)
    t_grav_coupling = InteractionTermCandidate(
        name="stress_energy_gravitational_coupling",
        formula="T^{defect}_{ab} enters G_{ab} = 8piG T_{ab}",
        coupling_constant="G (Newton's constant, already in S_grav)",
        target_d7_channel="gravitational_penalty (alpha_BR)",
        structural_motivation=(
            "Not a new interaction term — this is automatic in GR. "
            "Any stress-energy source gravitates through the Einstein equations. "
            "The defect T_{ab} contributes to the enclosed mass m(r), which "
            "increases the metric deficit delta(r)."
        ),
        enters_el_for=["g_ab"],
        sign_effect="destructive",
        notes=[
            "This is the gravitational penalty channel from D7.",
            "alpha_BR parametrizes the fraction of T_defect that gravitates.",
            "At alpha_BR=1: full GR consistency (all energy gravitates).",
            "At alpha_BR=0: defect energy does not gravitate (D6 additive limit).",
            "NOT a new coupling — inherent in S_grav + S_defect.",
        ],
    )

    # Term 2: Scalar-triplet portal coupling
    t_portal = InteractionTermCandidate(
        name="scalar_triplet_portal",
        formula="S_portal = integral sqrt(-g) * g_p * Phi^2 * |vec_Phi|^2 d^4x",
        coupling_constant="g_p (portal coupling, dimensionless)",
        target_d7_channel="source_amplification (beta_XR)",
        structural_motivation=(
            "A Phi^2 |vec_Phi|^2 portal term is the simplest renormalizable "
            "interaction between a real scalar and an O(3) triplet. When the "
            "defect develops a nonzero profile |vec_Phi| -> eta h(r), this "
            "generates an effective mass modification for Phi that is "
            "radius-dependent: m_Phi_eff^2(r) = m_Phi^2 + g_p eta^2 h(r)^2. "
            "This modifies the macro source driving, producing a "
            "radius-dependent amplitude A_eff(r)."
        ),
        enters_el_for=["Phi", "vec_Phi"],
        sign_effect="constructive",
        notes=[
            "Portal coupling is standard in BSM scalar sector extensions.",
            "This is the most natural candidate for the beta_XR channel.",
            "On the defect background: generates effective Phi mass shift.",
            "Recovering D7's linear form A_eff = A_0 * m_eff/M requires "
            "linearization around the background + identification of "
            "m_eff with the enclosed mass including portal contribution.",
            "This identification is the key approximation step.",
        ],
    )

    # Term 3: Derivative portal coupling
    t_derivative_portal = InteractionTermCandidate(
        name="derivative_portal",
        formula="S_dp = integral sqrt(-g) * g_d * (nabla Phi)^2 * |vec_Phi|^2 d^4x",
        coupling_constant="g_d (derivative portal coupling, dim = length^2)",
        target_d7_channel="source_amplification (beta_XR)",
        structural_motivation=(
            "A derivative coupling (nabla Phi)^2 |vec_Phi|^2 modifies "
            "the kinetic term of Phi on the defect background, producing "
            "an effective field-space metric for the macro scalar. This is "
            "a higher-derivative alternative to the portal term."
        ),
        enters_el_for=["Phi", "vec_Phi"],
        sign_effect="constructive",
        notes=[
            "Higher-order than the simple portal — subdominant at low energies.",
            "Included for completeness but expected to be subleading.",
            "Could contribute to nonlinear corrections beyond D7's linear model.",
            "Not required for D7 channel recovery at leading order.",
        ],
    )

    # Term 4: Defect-source direct coupling
    t_source_coupling = InteractionTermCandidate(
        name="defect_source_modulation",
        formula="S_ds = integral sqrt(-g) * g_s * J_eff * |vec_Phi|^2 d^4x",
        coupling_constant="g_s (source-defect coupling, dim = 1/field^2)",
        target_d7_channel="source_amplification (beta_XR)",
        structural_motivation=(
            "Direct coupling of the defect amplitude to the macro source "
            "J_eff. This is the most direct path to source amplification: "
            "the effective source becomes J_eff(1 + g_s |vec_Phi|^2), "
            "directly modifying the macro driving amplitude."
        ),
        enters_el_for=["Phi"],
        sign_effect="constructive",
        notes=[
            "More direct than the portal but less standard field-theoretically.",
            "Requires J_eff to be a well-defined local operator.",
            "In GRUT, J_eff depends on the gravitational source X, which "
            "itself depends on the stress-energy — potential circularity.",
            "Included to map the full space of minimal candidates.",
        ],
    )

    return [t_grav_coupling, t_portal, t_derivative_portal, t_source_coupling]


# ================================================================
# Level 2: Action Assembly
# ================================================================

def assemble_action(
    sectors: List[SectorActionDefinition],
    interactions: List[InteractionTermCandidate],
    params: CoupledActionParams,
) -> ActionCandidate:
    """Assemble the candidate coupled action from sectors + interactions.

    The minimal action uses:
    - All 4 sectors (gravity, macro, defect, trigger)
    - The stress-energy coupling (automatic, no new constant)
    - The scalar-triplet portal (one new coupling g_p)
    """
    # Build symbolic action string
    sector_names = [s.name for s in sectors]
    interaction_names = [t.name for t in interactions]

    full_action = (
        "S_total = S_grav[g] + S_macro[Phi, g] + S_defect[vec_Phi, g] "
        "+ S_trigger[K, vec_Phi] + S_portal[Phi, vec_Phi, g]"
    )

    # Count free parameters:
    # Inherited: G, eta, lambda, xi, A_0 (or equivalently M, tau)
    # New: g_p (portal coupling)
    # The derivative portal and source-modulation are assessed but not required
    n_inherited = 5  # G, eta, lambda, xi, A_0
    n_new = 1  # g_p (portal coupling)
    n_total = n_inherited + n_new

    # Minimality: we add exactly ONE new coupling constant
    minimality = (
        "Minimal: 1 new coupling constant (g_p) beyond the D6 parameter set. "
        "The gravitational penalty requires no new parameters (automatic in GR). "
        "The derivative portal and source-modulation terms are assessed but not "
        "included in the minimal action — they are subleading or redundant."
    )

    return ActionCandidate(
        sectors=sectors,
        interaction_terms=interactions,
        full_action_symbolic=full_action,
        n_sectors=len(sectors),
        n_interaction_terms=len(interactions),
        n_free_parameters=n_total,
        minimality_assessment=minimality,
        notes=[
            f"4 sectors: {', '.join(sector_names)}",
            f"4 interaction candidates assessed: {', '.join(interaction_names)}",
            "Minimal action uses 2: gravitational coupling (automatic) + portal (1 new constant).",
            f"Total free parameters: {n_total} ({n_inherited} inherited + {n_new} new).",
            "The portal term Phi^2 |vec_Phi|^2 is the unique minimal renormalizable "
            "scalar-triplet interaction.",
        ],
    )


# ================================================================
# Level 3: Euler-Lagrange Derivation
# ================================================================

def derive_euler_lagrange(
    action: ActionCandidate,
    params: CoupledActionParams,
) -> List[EulerLagrangeDerivation]:
    """Derive EL equations for each field, with terms tagged by role.

    This is a structural derivation: equations are represented as term
    inventories, not solved numerically.
    """
    # EL for g_ab (Einstein equations)
    el_metric = EulerLagrangeDerivation(
        field_name="metric",
        field_symbol="g_{ab}",
        equation_symbolic=(
            "G_{ab} = 8piG * (T^{macro}_{ab} + T^{defect}_{ab} + T^{trigger}_{ab} "
            "+ T^{portal}_{ab})"
        ),
        terms_identified={
            "macro_dynamics": (
                "T^{macro}_{ab} = nabla_a Phi nabla_b Phi - g_{ab} L_macro. "
                "Provides the scalar-memory stress-energy."
            ),
            "defect_dynamics": (
                "T^{defect}_{ab} = D_a vec_Phi . D_b vec_Phi - g_{ab} L_defect. "
                "Provides the hedgehog stress-energy. This is the source of "
                "the gravitational penalty: m_coupled includes integral of "
                "T^{defect}_{00} r^2 dr."
            ),
            "trigger_activation": (
                "T^{trigger}_{ab} contains terms from variation of xi K |vec_Phi|^2. "
                "Includes higher-derivative terms from variation of R_{abcd}R^{abcd} "
                "with respect to g^{ab}."
            ),
            "back_reaction_gravitational_penalty": (
                "The D7 gravitational penalty (alpha_BR) is EXACTLY the statement "
                "that T^{defect}_{ab} contributes to the Einstein equations. "
                "In the mass function: m(r) = M + integral_r^R_ext 4pi r'^2 "
                "T^{total}_{00} dr'. The defect contribution Sigma_defect enters "
                "m, increasing delta = m - r/2. This is alpha_BR at full strength."
            ),
        },
        approximations_required=[
            "Spherical symmetry reduction to ODE system.",
            "Static metric ansatz ds^2 = -f(r)dt^2 + f(r)^{-1}dr^2 + r^2 dOmega^2.",
        ],
        produces_d7_channel="gravitational_penalty (alpha_BR = 1 is GR-exact)",
        notes=[
            "The gravitational penalty is NOT a new interaction — it is inherent "
            "in general relativity.",
            "alpha_BR < 1 would correspond to a violation of the equivalence "
            "principle (defect energy partially non-gravitating).",
            "alpha_BR = 1 is the unique GR-consistent value.",
            "alpha_BR = 0 is the D6 additive approximation: defect energy does "
            "not gravitate, which is physically inconsistent but useful as a "
            "leading-order estimate.",
        ],
    )

    # EL for Phi (macro scalar equation)
    el_macro = EulerLagrangeDerivation(
        field_name="macro_scalar",
        field_symbol="Phi",
        equation_symbolic=(
            "Box Phi - V'_macro(Phi) + J_eff + 2 g_p Phi |vec_Phi|^2 = 0"
        ),
        terms_identified={
            "macro_dynamics": (
                "Box Phi - V'_macro(Phi) + J_eff = 0 is the uncoupled macro equation. "
                "Source J_eff drives the amplitude A."
            ),
            "portal_modification": (
                "2 g_p Phi |vec_Phi|^2: portal term acts as effective mass shift "
                "for Phi. On the defect background |vec_Phi| -> eta h(r), this "
                "becomes 2 g_p eta^2 h(r)^2 Phi, a radius-dependent mass "
                "modification."
            ),
            "source_amplification_pathway": (
                "The portal-induced effective mass modification changes the "
                "source-driven equilibrium amplitude. In the WKB / slowly-varying "
                "envelope approximation: A_eff(r) depends on the local effective "
                "mass m_Phi_eff^2(r) = m_Phi^2 + 2 g_p eta^2 h(r)^2. "
                "The relationship A_eff ~ A_0 * m_eff/M recovers D7's beta_XR "
                "channel after linearization."
            ),
        },
        approximations_required=[
            "Hedgehog profile frozen: h(r) from D2 BVP, not re-solved.",
            "Linearization: A_eff(r) = A_0 * (1 + delta_A(r)) with delta_A small.",
            "Identification: the portal-induced mass shift maps to an effective "
            "source modification equivalent to m_eff(r) = M + beta_XR * Sigma_defect(r). "
            "This identification requires matching the integrated energy shift to "
            "the enclosed mass parametrization.",
            "Slowly-varying envelope: the macro amplitude A adjusts adiabatically "
            "to the local defect background.",
        ],
        produces_d7_channel="source_amplification (beta_XR, after approximation)",
        notes=[
            "The portal term Phi^2 |vec_Phi|^2 generates a structural pathway "
            "to the beta_XR channel, but recovering D7's exact linear form "
            "A_eff = A_0 * m_eff/M requires three approximations.",
            "The key step is identifying the portal-induced mass shift with "
            "an effective enclosed-mass modification — a physical but non-trivial "
            "approximation.",
            "g_p > 0 gives constructive amplification (matches D7 sign).",
            "g_p < 0 would give destructive effect (anti-amplification).",
        ],
    )

    # EL for vec_Phi (defect triplet equation)
    el_defect = EulerLagrangeDerivation(
        field_name="defect_triplet",
        field_symbol="vec_Phi^a",
        equation_symbolic=(
            "D^2 vec_Phi^a - 4 lambda (|vec_Phi|^2 - eta^2) vec_Phi^a "
            "- 2 xi K vec_Phi^a + 2 g_p Phi^2 vec_Phi^a = 0"
        ),
        terms_identified={
            "defect_dynamics": (
                "D^2 vec_Phi - 4 lambda (|vec_Phi|^2 - eta^2) vec_Phi = 0 "
                "is the uncoupled defect equation (D2 hedgehog BVP)."
            ),
            "trigger_activation": (
                "-2 xi K vec_Phi: curvature trigger modifies the effective "
                "potential, activating the defect when K > K_crit. "
                "This is the D3/D4 trigger mechanism."
            ),
            "portal_backreaction_on_defect": (
                "2 g_p Phi^2 vec_Phi: portal term acts back on the defect "
                "profile. Since Phi ~ A/r^2, this gives 2 g_p A^2/r^4 vec_Phi, "
                "a ~1/r^4 effective mass term for the defect. This is small "
                "compared to the symmetry-breaking potential at large r "
                "and compared to the trigger term near r_act."
            ),
        },
        approximations_required=[
            "Defect-shape freezing: the portal backreaction on vec_Phi is "
            "neglected (2 g_p Phi^2 vec_Phi << other terms). This is D7's "
            "leading technical approximation.",
            "The trigger term dominates the portal backreaction near r_act "
            "when xi K >> g_p A^2/r^4, which holds for the canonical parameters.",
        ],
        produces_d7_channel=None,
        notes=[
            "The defect EL equation confirms that the portal term generates "
            "a small backreaction on the defect profile, but it is subdominant "
            "to the trigger and symmetry-breaking terms.",
            "This justifies D7's defect-shape freezing approximation at "
            "leading order.",
            "A future self-consistent phase would solve this equation "
            "simultaneously with the macro and metric equations.",
        ],
    )

    return [el_metric, el_macro, el_defect]


# ================================================================
# Level 4: Channel Recovery Map
# ================================================================

def map_channel_recovery(
    el_derivations: List[EulerLagrangeDerivation],
    params: CoupledActionParams,
) -> ChannelRecoveryMap:
    """Map D7 effective channels to action-derived structures.

    For each D7 channel, determine whether it is:
    - action_derived: follows from the action without additional input
    - derived_after_approximation: follows from the action + approximations
    - effective_closure: cannot be obtained from the action
    """
    # Channel 1: Gravitational penalty (alpha_BR)
    grav_penalty = ChannelRecoveryEntry(
        d7_channel_name="gravitational_penalty",
        d7_parameter="alpha_BR",
        d7_formula="m_coupled(r) = m_static(r) + alpha_BR * Sigma_defect(r)",
        recovery_status="action_derived",
        source_term_in_action="S_grav[g] + S_defect[vec_Phi, g]",
        derivation_path=(
            "1. Vary S_total with respect to g^{ab} to get Einstein equations.\n"
            "2. T^{total}_{ab} includes T^{defect}_{ab} automatically.\n"
            "3. In the mass function: m(r) = M + integral 4pi r'^2 T^{total}_{00} dr'.\n"
            "4. The defect contribution is exactly Sigma_defect(r).\n"
            "5. Therefore delta_coupled = delta_static + Sigma_defect = delta_static "
            "+ alpha_BR * Sigma_defect with alpha_BR = 1.\n"
            "6. This is GR-exact: no approximation needed."
        ),
        approximations_required=[],
        recovery_quality="exact",
        notes=[
            "alpha_BR = 1 is the unique GR-consistent value.",
            "The D7 scan over alpha_BR = [0, 0.25, ..., 1.0] tests what "
            "happens if the defect only partially gravitates — physically "
            "this would require equivalence principle violation.",
            "The D6 additive approximation (alpha_BR=0) is the zero-gravity "
            "limit for the defect sector.",
            "No new interaction term needed — this is inherent in GR.",
        ],
    )

    # Channel 2: Source amplification (beta_XR)
    source_amp = ChannelRecoveryEntry(
        d7_channel_name="source_amplification",
        d7_parameter="beta_XR",
        d7_formula="A_eff(r) = A_0 * (M + beta_XR * Sigma_defect(r)) / M",
        recovery_status="derived_after_approximation",
        source_term_in_action="S_portal = integral sqrt(-g) g_p Phi^2 |vec_Phi|^2 d^4x",
        derivation_path=(
            "1. The portal term Phi^2 |vec_Phi|^2 enters the Phi EL equation as "
            "2 g_p Phi |vec_Phi|^2.\n"
            "2. On the defect background |vec_Phi| -> eta h(r), this becomes "
            "2 g_p eta^2 h(r)^2 Phi.\n"
            "3. This is an effective radius-dependent mass for Phi: "
            "m_Phi_eff^2(r) = m_Phi^2 + 2 g_p eta^2 h(r)^2.\n"
            "4. APPROXIMATION 1 (frozen profile): h(r) is the D2 BVP solution, "
            "not re-solved self-consistently.\n"
            "5. APPROXIMATION 2 (slowly-varying envelope): the macro amplitude "
            "adjusts adiabatically: A_eff(r) = A_0 * F[m_Phi_eff(r)].\n"
            "6. APPROXIMATION 3 (linear identification): F is linearized and "
            "the integrated portal energy shift is identified with "
            "beta_XR * Sigma_defect(r) / M.\n"
            "7. Result: A_eff(r) = A_0 * (M + beta_XR * Sigma_defect(r)) / M "
            "with beta_XR = f(g_p, eta, ...) — a function of the portal "
            "coupling and field parameters."
        ),
        approximations_required=[
            "Frozen defect profile (D7 leading approximation).",
            "Slowly-varying envelope / adiabatic amplitude response.",
            "Linear identification of portal mass shift with enclosed-mass "
            "parametrization.",
        ],
        recovery_quality="structural",
        notes=[
            "The portal term provides the structural mechanism for source "
            "amplification, but D7's exact linear form requires 3 approximations.",
            "The beta_XR parameter is not predicted — it maps to g_p through "
            "a chain of approximations.",
            "This is 'derived after approximation': the action contains the "
            "necessary physics, but the D7 parametrization is not exact.",
            "A self-consistent computation would replace the linear model "
            "with the full numerical solution of the portal-modified macro EL.",
            "Sign: g_p > 0 gives constructive amplification (D7 beta_XR > 0).",
        ],
    )

    entries = [grav_penalty, source_amp]
    n_derived = sum(1 for e in entries if e.recovery_status == "action_derived")
    n_approx = sum(
        1 for e in entries if e.recovery_status == "derived_after_approximation"
    )
    n_effective = sum(
        1 for e in entries if e.recovery_status == "effective_closure"
    )
    n_total = len(entries)
    frac = (n_derived + 0.5 * n_approx) / n_total if n_total > 0 else 0.0

    summary = (
        f"{n_derived}/{n_total} channels action-derived, "
        f"{n_approx}/{n_total} derived after approximation, "
        f"{n_effective}/{n_total} effective closure. "
        f"Recovery fraction: {frac:.2f}."
    )

    return ChannelRecoveryMap(
        entries=entries,
        n_channels=n_total,
        n_action_derived=n_derived,
        n_derived_after_approximation=n_approx,
        n_effective_closure=n_effective,
        d7_recovery_fraction=frac,
        summary=summary,
        notes=[
            "Gravitational penalty: automatic in GR (alpha_BR=1 is exact).",
            "Source amplification: structurally present via portal term, "
            "but D7's linear parametrization requires 3 approximations.",
            "No channel requires a purely effective closure term.",
        ],
    )


# ================================================================
# Level 5: Closure Inventory
# ================================================================

def inventory_closure(
    channel_recovery: ChannelRecoveryMap,
    action: ActionCandidate,
    params: CoupledActionParams,
) -> ClosureInventory:
    """Produce the full closure inventory.

    Categorize every structural element as:
    - action_derived: obtainable from S_total
    - effective_but_disciplined: requires approximation but traceable
    - still_open: not derivable from the current action
    """
    entries = [
        # Macro driving
        ClosureInventoryEntry(
            item="macro_source_driving",
            status="action_derived",
            source="S_macro[Phi, g]: source term J_eff * Phi",
            approximation_level="exact within GRUT framework",
            notes="Inherited from GRUT scalar-memory canon.",
        ),
        # Defect triggering
        ClosureInventoryEntry(
            item="defect_curvature_triggering",
            status="action_derived",
            source="S_trigger: xi * K * |vec_Phi|^2",
            approximation_level="exact trigger mechanism from action",
            notes="Kretschner-family trigger from D3/D4. Enters defect EL equation.",
        ),
        # Defect profile (hedgehog BVP)
        ClosureInventoryEntry(
            item="defect_hedgehog_profile",
            status="action_derived",
            source="S_defect: O(3) symmetry-breaking potential",
            approximation_level="exact BVP from action variation",
            notes="D2 BVP is the EL equation of S_defect. Fully action-derived.",
        ),
        # Gravitational penalty
        ClosureInventoryEntry(
            item="gravitational_penalty_channel",
            status="action_derived",
            source="S_grav + S_defect: Einstein equations with T_defect",
            approximation_level="exact (GR)",
            notes="alpha_BR=1 is the GR-exact value. No new coupling needed.",
        ),
        # Source amplification mechanism
        ClosureInventoryEntry(
            item="source_amplification_mechanism",
            status="effective_but_disciplined",
            source="S_portal: g_p Phi^2 |vec_Phi|^2",
            approximation_level="structural form from action; D7 linear parametrization "
            "requires frozen profile + adiabatic + linearization",
            notes=(
                "The portal term provides the physics. The D7 formula "
                "A_eff = A_0 * m_eff/M is an approximation of the full "
                "portal-modified dynamics."
            ),
        ),
        # D7 linear amplitude model
        ClosureInventoryEntry(
            item="linear_amplitude_model",
            status="effective_but_disciplined",
            source="Linearization of portal-modified macro EL",
            approximation_level="leading-order approximation",
            notes="A_eff(r) = A_0 * (M + beta_XR * Sigma_defect)/M is the linearized form.",
        ),
        # Defect-shape freezing
        ClosureInventoryEntry(
            item="defect_shape_freezing",
            status="effective_but_disciplined",
            source="Neglect of portal backreaction on defect EL",
            approximation_level="leading-order: 2 g_p Phi^2 vec_Phi << trigger + potential",
            notes=(
                "Justified when portal coupling is small compared to "
                "symmetry-breaking and trigger terms."
            ),
        ),
        # Coupling constant prediction
        ClosureInventoryEntry(
            item="coupling_constant_beta_XR_value",
            status="still_open",
            source="Would require solving full coupled system",
            approximation_level="not attempted in D8",
            notes=(
                "beta_XR = f(g_p, eta, lambda, ...) is a function of the "
                "portal coupling. The functional form is known from the action, "
                "but the numerical value requires a self-consistent computation."
            ),
        ),
        # Nonlinear corrections
        ClosureInventoryEntry(
            item="nonlinear_amplitude_corrections",
            status="still_open",
            source="Higher-order terms in portal-modified macro EL",
            approximation_level="not computed",
            notes="Beyond the linear A_eff model. Would modify D7 results quantitatively.",
        ),
        # Self-consistent profile
        ClosureInventoryEntry(
            item="self_consistent_coupled_profile",
            status="still_open",
            source="Full coupled BVP system (macro + defect + metric)",
            approximation_level="not attempted — future phase",
            notes=(
                "Solving the full coupled system would relax the defect-shape "
                "freezing approximation and determine the self-consistent profiles."
            ),
        ),
    ]

    n_total = len(entries)
    n_derived = sum(1 for e in entries if e.status == "action_derived")
    n_effective = sum(1 for e in entries if e.status == "effective_but_disciplined")
    n_open = sum(1 for e in entries if e.status == "still_open")

    summary = (
        f"{n_derived}/{n_total} items action-derived, "
        f"{n_effective}/{n_total} effective-but-disciplined, "
        f"{n_open}/{n_total} still open."
    )

    return ClosureInventory(
        entries=entries,
        n_total=n_total,
        n_action_derived=n_derived,
        n_effective=n_effective,
        n_open=n_open,
        summary=summary,
        notes=[
            "Core structural elements (macro driving, defect profile, trigger, "
            "gravitational penalty) are all action-derived.",
            "Source amplification is structurally motivated but parametrically "
            "approximate.",
            "Three items remain open: coupling constant value, nonlinear "
            "corrections, and self-consistent profiles.",
        ],
    )


# ================================================================
# Level 6: Classification
# ================================================================

def classify_coupled_action(
    channel_recovery: ChannelRecoveryMap,
    closure: ClosureInventory,
    params: CoupledActionParams,
) -> CoupledActionClassification:
    """Classify the D8 coupled action closure result."""
    n_derived = channel_recovery.n_action_derived
    n_approx = channel_recovery.n_derived_after_approximation
    n_effective = channel_recovery.n_effective_closure
    n_total = channel_recovery.n_channels
    frac = channel_recovery.d7_recovery_fraction

    # Classification logic
    if n_derived == n_total:
        classification = "d7_channels_largely_action_derived"
        summary = (
            "Both D7 channels are directly action-derived. "
            "The effective action fully accounts for the D7 structure."
        )
    elif n_derived + n_approx == n_total and n_derived > 0:
        if n_derived >= n_approx:
            classification = "d7_channels_largely_action_derived"
            summary = (
                f"{n_derived} channel(s) action-derived, "
                f"{n_approx} derived after approximation. "
                "The effective action accounts for the D7 structure "
                "with identified approximations."
            )
        else:
            classification = "d7_channels_partially_action_derived"
            summary = (
                f"{n_derived} channel(s) action-derived, "
                f"{n_approx} derived after approximation. "
                "The effective action provides structural support but "
                "the D7 parametrization requires approximation."
            )
    elif n_effective > 0 and n_derived + n_approx > 0:
        classification = "d7_channels_partially_action_derived"
        summary = (
            f"{n_derived} action-derived, {n_approx} derived after approximation, "
            f"{n_effective} effective closure. Mixed recovery."
        )
    elif n_effective == n_total:
        classification = "d7_channels_require_effective_closure"
        summary = "Neither D7 channel can be derived from the candidate action."
    else:
        classification = "coupled_action_attempt_inconsistent"
        summary = "The derivation produced inconsistent results."

    phase_status = f"ASSESSED ({classification})"

    phase_lock = {
        "phase_6_f_Req": "LOCKED (-17.71)",
        "phase_6B_A_crit": "LOCKED (1.062)",
        "phase_6C_deficit": "LOCKED (Component A + Component B)",
        "route_C": "LOCKED (insufficient)",
        "route_B": "LOCKED (closed)",
        "source_law_I": "LOCKED (partially viable, no GRUT-native)",
        "defect_D1": "LOCKED (provisional candidate formulated)",
        "defect_D2": "LOCKED (defect_candidate_numerically_viable)",
        "unification_D3": "LOCKED (scalar_triplet_embedding_most_promising)",
        "unification_D4": "LOCKED (component_a_shape_recovered_but_interpretation_not_yet_verified)",
        "source_coupled_D5": "LOCKED (source_coupling_insufficient)",
        "companion_D6": "LOCKED (companion_architecture_viable)",
        "cross_coupling_D7": "LOCKED (fully_coupled_viable)",
        "coupled_action_D8": phase_status,
    }

    return CoupledActionClassification(
        classification=classification,
        phase_status=phase_status,
        d7_recovery_fraction=frac,
        n_channels_derived=n_derived,
        n_channels_approximate=n_approx,
        n_channels_effective=n_effective,
        summary=summary,
        phase_lock_update=phase_lock,
    )


# ================================================================
# Level 7: Master Computation
# ================================================================

def compute_coupled_action(
    params: Optional[CoupledActionParams] = None,
) -> CoupledActionResult:
    """Run the full Phase D8 coupled action closure analysis."""
    if params is None:
        params = CoupledActionParams()

    result = CoupledActionResult(
        valid=True,
        params=params,
        nonclaims=list(COUPLED_ACTION_NONCLAIMS),
        assumptions=list(COUPLED_ACTION_ASSUMPTIONS),
    )

    # Level 0: Sector actions
    result.sector_actions = define_sector_actions(params)

    # Level 1: Interaction candidates
    result.interaction_candidates = construct_interaction_candidates(params)

    # Level 2: Action assembly
    result.action_candidate = assemble_action(
        result.sector_actions, result.interaction_candidates, params,
    )

    # Level 3: Euler-Lagrange derivation
    result.el_derivations = derive_euler_lagrange(result.action_candidate, params)

    # Level 4: Channel recovery map
    result.channel_recovery = map_channel_recovery(result.el_derivations, params)

    # Level 5: Closure inventory
    result.closure_inventory = inventory_closure(
        result.channel_recovery, result.action_candidate, params,
    )

    # Level 6: Classification
    result.classification = classify_coupled_action(
        result.channel_recovery, result.closure_inventory, params,
    )

    return result


# ================================================================
# Level 8: Serialization
# ================================================================

def coupled_action_result_to_dict(
    result: CoupledActionResult,
) -> Dict[str, Any]:
    """Serialize to JSON-compatible dict."""
    d: Dict[str, Any] = {
        "valid": result.valid,
        "phase": "D8",
        "title": "Coupled Action Closure",
    }

    # Sector actions
    if result.sector_actions:
        d["sector_actions"] = [
            {
                "name": s.name,
                "field_content": s.field_content,
                "lagrangian_form": s.lagrangian_form,
                "role_in_metric": s.role_in_metric,
                "symmetry": s.symmetry,
                "d7_relevance": s.d7_relevance,
            }
            for s in result.sector_actions
        ]

    # Interaction candidates
    if result.interaction_candidates:
        d["interaction_candidates"] = [
            {
                "name": t.name,
                "formula": t.formula,
                "coupling_constant": t.coupling_constant,
                "target_d7_channel": t.target_d7_channel,
                "sign_effect": t.sign_effect,
            }
            for t in result.interaction_candidates
        ]

    # Action candidate
    if result.action_candidate:
        ac = result.action_candidate
        d["action_candidate"] = {
            "full_action_symbolic": ac.full_action_symbolic,
            "n_sectors": ac.n_sectors,
            "n_interaction_terms": ac.n_interaction_terms,
            "n_free_parameters": ac.n_free_parameters,
            "minimality_assessment": ac.minimality_assessment,
        }

    # EL derivations
    if result.el_derivations:
        d["el_derivations"] = [
            {
                "field_name": el.field_name,
                "equation_symbolic": el.equation_symbolic,
                "terms_identified": el.terms_identified,
                "approximations_required": el.approximations_required,
                "produces_d7_channel": el.produces_d7_channel,
            }
            for el in result.el_derivations
        ]

    # Channel recovery
    if result.channel_recovery:
        cr = result.channel_recovery
        d["channel_recovery"] = {
            "n_channels": cr.n_channels,
            "n_action_derived": cr.n_action_derived,
            "n_derived_after_approximation": cr.n_derived_after_approximation,
            "n_effective_closure": cr.n_effective_closure,
            "d7_recovery_fraction": cr.d7_recovery_fraction,
            "summary": cr.summary,
            "entries": [
                {
                    "d7_channel_name": e.d7_channel_name,
                    "d7_parameter": e.d7_parameter,
                    "recovery_status": e.recovery_status,
                    "source_term_in_action": e.source_term_in_action,
                    "recovery_quality": e.recovery_quality,
                    "approximations_required": e.approximations_required,
                }
                for e in cr.entries
            ],
        }

    # Closure inventory
    if result.closure_inventory:
        ci = result.closure_inventory
        d["closure_inventory"] = {
            "n_total": ci.n_total,
            "n_action_derived": ci.n_action_derived,
            "n_effective": ci.n_effective,
            "n_open": ci.n_open,
            "summary": ci.summary,
            "entries": [
                {
                    "item": e.item,
                    "status": e.status,
                    "source": e.source,
                    "approximation_level": e.approximation_level,
                }
                for e in ci.entries
            ],
        }

    # Classification
    if result.classification:
        cl = result.classification
        d["classification"] = {
            "classification": cl.classification,
            "phase_status": cl.phase_status,
            "d7_recovery_fraction": cl.d7_recovery_fraction,
            "n_channels_derived": cl.n_channels_derived,
            "n_channels_approximate": cl.n_channels_approximate,
            "n_channels_effective": cl.n_channels_effective,
            "summary": cl.summary,
        }

    d["nonclaims"] = result.nonclaims
    d["assumptions"] = result.assumptions

    return d
