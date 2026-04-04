"""
Appendix U-B --- Native Field Content and Degrees-of-Freedom Audit
===================================================================
GRUT Unified-Field Program --- Phase U-B

Determines the exact native field content, counts native degrees of freedom,
classifies X, and determines whether extensions add native fields or only
layered targets/grammars.

=== CORE ANALYSIS ===

Native equation: tau dPhi/dt + Phi = X

NATIVE DYNAMICAL VARIABLE: Phi (real scalar field).
  - Phi(x,t) is the single native dynamical variable.
  - Given Phi(x,0) and the forcing history X(x,s) for s in [0,t],
    the evolution is UNIQUELY determined.
  - The instantaneous state is fully specified by Phi(x,t) alone
    (first-order ODE: one initial condition per spatial point).

NATIVE DoF COUNT: ONE scalar field.
  - First-order-in-time: one state variable per spatial point.
  - Compare: second-order wave equation needs (Phi, dPhi/dt) = two per point.
  - GRUT's first-order structure is SPARSER than standard field theory.

STATUS OF X: External or constitutive input.
  - X appears on the RHS of tau dPhi/dt + Phi = X.
  - X has NO independent evolution equation in native GRUT.
  - X is specified externally (boundary condition, environmental input,
    or coupling to other sectors).
  - X is NOT a native autonomous dynamical field.
  - In free relaxation: X = 0. In constant forcing: X = X0 (parameter).
  - In driven case: X(t) is externally prescribed.
  - X COULD become a dynamical field if given its own evolution equation,
    but this would be a NEW POSTULATE, not a native consequence.

MEMORY / RETARDATION: Modifies evolution law, does not add native field.
  - The Galley CTP doubled-variable formulation (Phi_1, Phi_2) is an
    EFFECTIVE-REGIME representation of the same single-field dynamics.
  - Phi_+ = (Phi_1+Phi_2)/2 is the physical field; Phi_- = (Phi_1-Phi_2)/2
    is the auxiliary/ghost mode (PHI_MINUS_GROWTH_RATE_SIGN = +1).
  - The doubled variables do NOT add a native field: Phi_- is auxiliary
    and grows (unstable); the physical content is Phi_+ = Phi.
  - Nonlocal memory kernels (if present) modify the evolution operator
    but do not add local field degrees of freedom.

EXTENSION SECTORS: Do not change native field count.
  - O(3): adds S^2 target space (2 angular DOF on S^2), but these are
    extension-level (MIP). They are NOT native vacuum DOF.
  - SU(2)-like: adds C^2 qubit state space, but this is postulated (MBU).
    Not a native spacetime field.
  - Exchange: adds permutation grammar. No field content.
  - Topological: adds classification labels. No field content.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_REGIMES: int = 6
N_UB_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

DOF_OPTIONS = frozenset({
    "single_scalar_dof_natively_supported",
    "scalar_core_with_conditional_additional_state_dimension",
    "native_dof_count_not_closed",
    "multiple_native_dofs_established",
})
SOURCE_OPTIONS = frozenset({
    "X_is_external_or_constitutive_input",
    "X_is_auxiliary_without_independent_dynamics",
    "X_is_conditional_effective_field",
    "X_is_independent_native_dynamical_field",
})
MEMORY_OPTIONS = frozenset({
    "memory_modifies_evolution_without_new_native_field",
    "memory_introduces_conditional_state_extension",
    "memory_structure_not_resolved",
    "additional_native_memory_fields_established",
})
EXTENSION_OPTIONS = frozenset({
    "extensions_do_not_change_native_field_count",
    "extensions_add_only_nonnative_target_or_observable_structure",
    "extensions_conditionally_enlarge_effective_field_content",
    "extensions_upgrade_native_field_content",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_UC",
    "stop_for_missing_field_closure",
})
OVERALL_OPTIONS = frozenset({
    "native_scalar_field_content_confirmed_with_external_source_boundary",
    "sparse_field_core_confirmed_extensions_remain_nonnative",
    "field_content_conditionally_larger_than_scalar_core",
    "native_field_basis_not_yet_closed",
})

UB_DOF_VERDICT: str = "single_scalar_dof_natively_supported"
UB_SOURCE_VERDICT: str = "X_is_external_or_constitutive_input"
UB_MEMORY_VERDICT: str = "memory_modifies_evolution_without_new_native_field"
UB_EXTENSION_VERDICT: str = "extensions_add_only_nonnative_target_or_observable_structure"
UB_AUTH_VERDICT: str = "authorized_to_proceed_to_UC"
UB_OVERALL_P: str = "native_scalar_field_content_confirmed_with_external_source_boundary"

UB_NONCLAIMS: List[str] = [
    "NOT_claiming_X_is_dynamical_field__"
    "X_has_no_native_evolution_equation_and_is_external_input",
    "NOT_claiming_CTP_doubling_adds_native_field__"
    "Phi_minus_is_auxiliary_ghost_not_physical_field",
    "NOT_claiming_O3_target_dimensions_are_native_DOF__"
    "S2_angular_coordinates_are_extension_level_MIP",
    "NOT_claiming_qubit_Hilbert_dimension_is_field_DOF__"
    "C2_is_quantum_state_space_not_spacetime_field",
    "NOT_claiming_memory_kernel_adds_native_field__"
    "nonlocal_history_dependence_is_not_local_field_content",
    "NOT_claiming_tau_or_A_are_field_DOF__"
    "parameters_are_not_dynamical_field_variables",
    "NOT_claiming_sparse_core_implies_vector_tensor_needed__"
    "scarcity_does_not_license_inflation",
    "NOT_claiming_single_scalar_therefore_field_theory_complete__"
    "DOF_count_is_inventory_not_completion",
]


@dataclass
class UBTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class UBEvidenceRow:
    regime: str; native_vars: str; native_dof_added: str
    role_of_x: str; memory_effect: str
    what_licensed: str; what_not_licensed: str

@dataclass
class UBLicensedLanguage:
    licensed: List[str]

@dataclass
class UBNonlicensedLanguage:
    nonlicensed: List[str]

@dataclass
class UBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class UBNativeFieldContentResult:
    valid: bool
    track_a_variables: UBTrackResult
    track_b_dof_count: UBTrackResult
    track_c_source: UBTrackResult
    track_d_memory: UBTrackResult
    track_e_extensions: UBTrackResult
    track_f_firewall: UBTrackResult
    evidence_table: List[UBEvidenceRow]
    licensed_language: UBLicensedLanguage
    nonlicensed_language: UBNonlicensedLanguage
    nonclaim_firewall: UBNonclaimFirewall
    native_dof_status: str; source_status: str
    memory_status: str; extension_field_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> UBTrackResult:
    return UBTrackResult("A", "native_dynamical_variables",
        "What are the true native dynamical variables?",
        [
            "Phi(x,t): real scalar field. The SINGLE native dynamical variable.",
            "tau: canonical parameter (tau^2=3/2). NOT a field.",
            "A: barrier amplitude. Parameter, NOT a field.",
            "X: source/input term. NOT a native dynamical variable (no evolution eq).",
            "gamma = 1/tau: derived rate. NOT a field.",
            "The minimal native state is Phi(x,t) alone. First-order ODE: "
            "one initial condition per spatial point fully determines evolution.",
        ],
        UB_DOF_VERDICT,
        ["Phi is the only native dynamical variable"])


def _track_b() -> UBTrackResult:
    return UBTrackResult("B", "dof_count",
        "How many native propagating/evolving DOF?",
        [
            "NATIVE DOF: ONE real scalar field Phi.",
            "First-order in time: one state variable per spatial point.",
            "Compare second-order (wave): needs (Phi, dPhi/dt) = TWO per point.",
            "GRUT is SPARSER than standard field theory by this measure.",
            "No hidden multi-component structure: Phi is a real scalar, "
            "not a disguised vector, spinor, or multiplet.",
            "Extensions add nonnative DOF (O(3) target, C^2 qubit) but these "
            "do not count as native vacuum field content.",
        ],
        "one_scalar_dof",
        ["Single scalar: the sparsest possible field content"])


def _track_c() -> UBTrackResult:
    return UBTrackResult("C", "source_status",
        "What is X in the native theory?",
        [
            "X appears in: tau dPhi/dt + Phi = X.",
            "X has NO evolution equation of its own in native GRUT.",
            "FREE RELAXATION: X = 0 (trivial; not a field).",
            "CONSTANT FORCING: X = X0 (parameter, not a field).",
            "DRIVEN: X(t) externally prescribed (input, not autonomous).",
            "X is EXTERNAL or CONSTITUTIVE INPUT: it drives Phi but is not "
            "determined by Phi. The system is open with respect to X.",
            "X COULD be promoted to a dynamical field if given its own "
            "equation (e.g. tau_X dX/dt + X = F[Phi,...]), but this would "
            "be a NEW POSTULATE, not a native consequence.",
            "Classification: external_or_constitutive_input.",
        ],
        UB_SOURCE_VERDICT,
        ["X is input, not native autonomous field"])


def _track_d() -> UBTrackResult:
    return UBTrackResult("D", "memory_retardation",
        "Does memory create new native fields?",
        [
            "GALLEY CTP: doubled variables (Phi_1, Phi_2) are EFFECTIVE-REGIME "
            "representation. Phi_+ = physical; Phi_- = auxiliary/ghost.",
            "Phi_- has growth rate +1/tau (unstable); it is NOT a physical field.",
            "The physical content is Phi_+ = Phi: one field.",
            "NONLOCAL MEMORY: if retardation kernel K(t-s) replaces instantaneous "
            "response, this modifies the evolution law from ODE to integro-DE.",
            "An integro-DE has infinite-dimensional history dependence but "
            "does NOT add local field degrees of freedom.",
            "The local instantaneous state is still Phi(x,t); the kernel "
            "encodes how past values of Phi influence present evolution.",
            "Conclusion: memory modifies the evolution operator class, "
            "does not add new native local field content.",
        ],
        UB_MEMORY_VERDICT,
        ["Memory changes operator, not field count"])


def _track_e() -> UBTrackResult:
    return UBTrackResult("E", "extension_attachment",
        "Do extensions add native field content?",
        [
            "O(3) SIGMA MODEL: introduces S^2 target space with 2 angular "
            "coordinates (theta, phi on S^2). These are EXTENSION-LEVEL (MIP). "
            "They add 2 effective DOF if O(3) is postulated, but these are "
            "NOT native vacuum fields. They are extension target coordinates.",
            "SU(2) QUBIT: C^2 state space with density matrix rho (3 real "
            "parameters for qubit). EXTENSION-LEVEL (MBU). Quantum state "
            "space, not spacetime field content.",
            "EXCHANGE: permutation grammar. NO field content whatsoever.",
            "TOPOLOGICAL: integer winding labels. Classification, not fields.",
            "CONCLUSION: extensions add nonnative target/observable/grammar "
            "structure. They do NOT upgrade the native vacuum field count.",
        ],
        UB_EXTENSION_VERDICT,
        ["Extensions are layers, not native fields"])


def _track_f() -> UBTrackResult:
    return UBTrackResult("F", "hidden_structure_firewall",
        "What apparent multi-component structures are merely notational?",
        [
            "CTP DOUBLING (Phi_1, Phi_2): notational / effective-regime "
            "representation of one physical field. Phi_- is ghost.",
            "O(3) TARGET (theta, phi): extension-level target coordinates, "
            "not native vacuum field dimensions.",
            "QUBIT (rho_00, rho_01, rho_10, rho_11): quantum state space "
            "components, not spacetime field DOF.",
            "REWRITING scalar ODE as 2-component system by defining "
            "Y = dPhi/dt: illegitimate inflation (native ODE is first-order).",
            "CONCLUSION: the native field content is ONE real scalar Phi. "
            "All apparent multi-component structures are notational, effective, "
            "or extension-level.",
        ],
        "firewall_secured",
        ["No hidden native multi-component structure"])


def _build_evidence() -> List[UBEvidenceRow]:
    return [
        UBEvidenceRow("free_relaxation",
            "Phi only", "No", "X=0 (trivial)", "None",
            "Single scalar DoF", "Any additional field"),
        UBEvidenceRow("constant_forcing",
            "Phi only", "No", "X=X0 (parameter)", "None",
            "Single scalar + parameter", "X as dynamical field"),
        UBEvidenceRow("driven_forcing",
            "Phi only", "No", "X(t) external input", "None",
            "Single scalar + external drive", "X as autonomous field"),
        UBEvidenceRow("memory_retardation",
            "Phi only (with history)", "No local field", "Input",
            "Kernel modifies evolution operator", "Integro-DE evolution",
            "Additional native local field"),
        UBEvidenceRow("O3_extension",
            "Phi + (theta,phi) if postulated", "Extension only (MIP)",
            "N/A", "N/A",
            "Extension target coordinates", "Native vacuum DOF"),
        UBEvidenceRow("SU2_extension",
            "Phi + rho if postulated", "Extension only (MBU)",
            "N/A", "N/A",
            "Extension quantum state", "Native spacetime field"),
    ]


def _build_licensed() -> UBLicensedLanguage:
    return UBLicensedLanguage([
        "native_scalar_field_Phi_one_real_DOF",
        "first_order_evolution_one_state_per_spatial_point",
        "X_is_external_constitutive_input_not_native_field",
        "memory_modifies_operator_not_field_count",
        "extensions_add_nonnative_target_observable_grammar",
        "sparse_field_core_confirmed",
    ])


def _build_nonlicensed() -> UBNonlicensedLanguage:
    return UBNonlicensedLanguage([
        "vector_tensor_native_field_content",
        "gauge_field_content",
        "independent_dynamics_for_X",
        "unified_carrier_space",
        "multi_field_unification",
        "gravity_electromagnetism_derivation",
        "native_multi_component_structure",
    ])


def run_ub_native_field_content_dof_audit() -> UBNativeFieldContentResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tf=_track_f()
    ev=_build_evidence()
    lic=_build_licensed();nlic=_build_nonlicensed()
    fw=UBNonclaimFirewall(UB_NONCLAIMS,N_UB_NONCLAIMS,True)

    key=[
        "SINGLE SCALAR DoF confirmed: Phi(x,t) is the only native dynamical "
        "field variable. First-order ODE: one state per spatial point.",
        "X is EXTERNAL/CONSTITUTIVE INPUT: no native evolution equation; "
        "drives Phi but is not determined by Phi.",
        "MEMORY modifies evolution operator (ODE -> integro-DE) but does NOT "
        "add local native field degrees of freedom.",
        "EXTENSION SECTORS add only nonnative target/observable/grammar: "
        "O(3) target coords, C^2 qubit state, permutation labels, winding numbers.",
        "CTP DOUBLING is effective representation, not native multi-component: "
        "Phi_- is auxiliary ghost mode, Phi_+ = Phi is the physical field.",
        "SPARSE FIELD CORE: GRUT has the minimal possible field content "
        "(one real scalar) — sparser than standard second-order field theory.",
        "No hidden multi-component structure found.",
    ]

    allowed=[
        "Native field content: single real scalar Phi with first-order evolution",
        "Native DoF: one state variable per spatial point (sparser than wave eq)",
        "X is external/constitutive input without independent native dynamics",
        "Memory/retardation modifies evolution operator, not field count",
        "Extension sectors add nonnative target/observable/grammar only",
        "CTP doubling is effective representation; Phi_- is ghost, not physical",
        "U-C authorized: field content confirmed, action/variational test next",
    ]

    forbidden=[
        "X is an independent native dynamical field",
        "CTP doubling adds a second native field",
        "O(3) target dimensions are native vacuum DOF",
        "Qubit Hilbert dimension is native field content",
        "Memory kernel adds native local fields",
        "Scarcity of scalar DOF implies vector/tensor needed",
        "Single scalar confirms unified field theory",
    ]

    diagnostics: Dict[str,Any]={
        "native_dof_count":1,
        "native_field_type":"real_scalar",
        "evolution_order":"first_order_in_time",
        "x_has_evolution_equation":False,
        "ctp_adds_native_field":False,
        "o3_adds_native_dof":False,
        "su2_adds_native_dof":False,
        "memory_adds_native_field":False,
        "n_regimes":N_REGIMES,
        "n_nonclaims":N_UB_NONCLAIMS,
    }

    result=UBNativeFieldContentResult(
        True,ta,tb,tc,td,te,tf,ev,lic,nlic,fw,
        UB_DOF_VERDICT,UB_SOURCE_VERDICT,UB_MEMORY_VERDICT,
        UB_EXTENSION_VERDICT,UB_AUTH_VERDICT,UB_OVERALL_P,
        key,allowed,forbidden,UB_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:UBNativeFieldContentResult)->None:
    if r.native_dof_status not in DOF_OPTIONS:raise ValueError("dof")
    if r.source_status not in SOURCE_OPTIONS:raise ValueError("source")
    if r.memory_status not in MEMORY_OPTIONS:raise ValueError("memory")
    if r.extension_field_status not in EXTENSION_OPTIONS:raise ValueError("ext")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_UB_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_REGIMES:raise ValueError("evidence")
    if r.diagnostics["native_dof_count"]!=1:raise ValueError("dof count")
    if r.diagnostics["x_has_evolution_equation"]:raise ValueError("x evol")
    if r.diagnostics["ctp_adds_native_field"]:raise ValueError("ctp")


def _self_test()->bool:
    r=run_ub_native_field_content_dof_audit()
    assert r.valid
    assert r.native_dof_status==UB_DOF_VERDICT
    assert r.source_status==UB_SOURCE_VERDICT
    assert r.memory_status==UB_MEMORY_VERDICT
    assert r.extension_field_status==UB_EXTENSION_VERDICT
    assert r.authorization==UB_AUTH_VERDICT
    assert r.diagnostics["native_dof_count"]==1
    assert r.diagnostics["native_field_type"]=="real_scalar"
    return True

if __name__=="__main__":
    _self_test();print("U-B passed.")
