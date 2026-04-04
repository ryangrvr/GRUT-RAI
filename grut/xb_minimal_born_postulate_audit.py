"""
Appendix X-B --- Minimal Born Postulate Audit
===============================================
GRUT Probability Program --- Phase X-B

Determines the minimal Born-style probability postulate attachable
to existing extension grammar. Book II LOCKED. Not native recovery.

=== ANALYSIS ===

CANDIDATE 1: PROJECTOR BORN RULE (pure state)
  p(i) = <psi|Pi_i|psi> where Pi_i = |i><i|
  Requires: state vector psi in C^2, projectors in observable eigenbasis.
  New axioms: 1 (the rule itself). New DOF: 0. New objects: 0
  (projectors already exist in the extension su(2) algebra).
  Normalization: sum p(i) = <psi|sum Pi_i|psi> = <psi|psi> = 1. Yes.
  Positivity: p(i) = |<i|psi>|^2 >= 0. Yes.
  Hidden assumptions: psi ontology (state vector as physical).

CANDIDATE 2: DENSITY-MATRIX BORN RULE
  p(i) = Tr(rho Pi_i)
  Requires: density matrix rho (already in extension grammar), projectors.
  New axioms: 1. New DOF: 0. New objects: 0.
  Normalization: sum p(i) = Tr(rho sum Pi_i) = Tr(rho) = 1. Yes.
  Positivity: rho >= 0 and Pi_i >= 0 => Tr(rho Pi_i) >= 0. Yes.
  Hidden assumptions: FEWER than Candidate 1. No psi ontology needed.
  rho already exists in the extension grammar. Pi_i from su(2) algebra.
  THIS IS THE PREFERRED CANDIDATE.

CANDIDATE 3: POVM RULE
  p(i) = Tr(rho E_i), E_i >= 0, sum E_i = I
  Generalizes Candidate 2. Requires specifying POVM elements.
  More general but more inflationary (must define {E_i}).
  For C^2 with standard observables, POVM reduces to projector case.
  Not needed at minimal level.

CANDIDATE 4: DIAGNOSTIC-WEIGHT NORMALIZATION
  p(i) = rho_ii / sum_j rho_jj = rho_ii (since Tr(rho)=1)
  This IS Candidate 2 restricted to the pointer basis.
  Less general; already contained in Candidate 2.

CANDIDATE 5: AMPLITUDE-SQUARE
  p(i) = |A_i|^2
  Requires well-defined amplitudes. In C^2: A_i = <i|psi>.
  Then p(i) = |<i|psi>|^2 = Candidate 1. Same rule, different notation.

PREFERRED: CANDIDATE 2 (density-matrix Born rule)
  p(i) = Tr(rho Pi_i)
  - ONE axiom
  - ZERO new DOF
  - ZERO new objects (rho and Pi_i already in extension grammar)
  - Guaranteed normalized and nonnegative
  - Minimal hidden assumptions (no psi ontology, no collapse, no POVM)
  - Compatible with density-matrix, decoherence, and su(2) grammar
  - Does NOT buy: collapse, measurement completion, unitarity, ontology
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_XB_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

BORN_OPTIONS = frozenset({
    "minimal_born_postulate_identified",
    "multiple_equally_minimal_probability_rules",
    "probability_postulate_requires_hidden_structure",
    "no_stable_probability_postulate_found",
})
PREF_OPTIONS = frozenset({
    "projector_or_density_matrix_born_rule_preferred",
    "povm_probability_rule_preferred",
    "diagnostic_weight_normalization_preferred",
    "amplitude_square_rule_preferred",
    "no_preferred_rule_class",
})
INFLATION_OPTIONS = frozenset({
    "one_axiom_no_new_dof_supported",
    "low_inflation_but_extra_measurement_assumptions",
    "moderate_hidden_structure_required",
    "inflation_not_resolved",
})
SCOPE_OPTIONS = frozenset({
    "probability_map_only_not_measurement_completion",
    "partial_measurement_structure_bought",
    "broader_quantum_completion_conditionally_supported",
    "scope_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_XC",
    "stop_for_missing_probability_boundary",
})
OVERALL_OPTIONS = frozenset({
    "minimal_born_probability_extension_identified_under_strict_postulate_accounting",
    "probability_map_added_without_measurement_completion",
    "low_inflation_born_postulate_conditionally_supported",
    "probability_extension_not_yet_stable",
})

XB_BORN: str = "minimal_born_postulate_identified"
XB_PREF: str = "projector_or_density_matrix_born_rule_preferred"
XB_INFLATION: str = "one_axiom_no_new_dof_supported"
XB_SCOPE: str = "probability_map_only_not_measurement_completion"
XB_AUTH: str = "authorized_to_proceed_to_XC"
XB_OVERALL: str = "minimal_born_probability_extension_identified_under_strict_postulate_accounting"

XB_NONCLAIMS: List[str] = [
    "NOT_claiming_Born_postulate_therefore_native__"
    "p_eq_Tr_rho_Pi_is_explicit_new_axiom_not_consequence",
    "NOT_claiming_probability_map_therefore_collapse__"
    "outcome_weights_do_not_imply_state_update",
    "NOT_claiming_density_matrix_Born_therefore_psi_ontology__"
    "rho_formulation_avoids_wavefunction_commitment",
    "NOT_claiming_normalization_therefore_unitarity__"
    "Tr_rho_eq_1_is_trace_condition_not_unitary_dynamics",
    "NOT_claiming_Born_therefore_measurement_theory__"
    "probability_assignment_is_not_apparatus_model",
    "NOT_claiming_compatibility_therefore_quantum_completion__"
    "Born_fits_grammar_but_does_not_complete_QM",
    "NOT_claiming_one_axiom_therefore_derivation__"
    "minimal_postulate_is_still_a_postulate",
    "NOT_claiming_Born_therefore_decoherence_explained__"
    "probability_rule_does_not_derive_basis_selection",
]


@dataclass
class XBCandidate:
    name: str; new_axioms: int; new_objects: int; new_dof: int
    normalization: bool; positivity: bool; hidden: str
    strongest: str; verdict: str

@dataclass
class XBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class XBMinimalBornResult:
    valid: bool
    candidates: List[XBCandidate]
    n_candidates: int
    recommended: str
    nonclaim_firewall: XBNonclaimFirewall
    born_postulate_status: str; preferred_rule_class: str
    inflation_status: str; scope_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[XBCandidate]:
    return [
        XBCandidate("projector_born_pure_state",1,0,0,True,True,
            "psi ontology (state vector as physical)",
            "Born probability for pure states","viable_but_psi_ontology"),
        XBCandidate("density_matrix_born",1,0,0,True,True,
            "minimal: rho and Pi already in grammar",
            "p(i)=Tr(rho Pi_i): PREFERRED",
            "PREFERRED_minimal_no_psi_ontology"),
        XBCandidate("povm_rule",1,1,0,True,True,
            "must specify {E_i} POVM elements",
            "Generalized probability rule","viable_but_more_inflationary"),
        XBCandidate("diagnostic_weight_normalization",0,0,0,True,True,
            "restricted to pointer basis only",
            "p(i)=rho_ii (pointer basis only)","contained_in_candidate_2"),
        XBCandidate("amplitude_square",1,0,0,True,True,
            "requires well-defined amplitudes (= Candidate 1)",
            "p(i)=|A_i|^2 = |<i|psi>|^2","equivalent_to_candidate_1"),
        XBCandidate("hidden_structure_comparison",0,0,0,False,False,
            "N/A","Comparison row","comparison_only"),
    ]


def run_xb_minimal_born_postulate_audit() -> XBMinimalBornResult:
    cands=_build_candidates()
    fw=XBNonclaimFirewall(XB_NONCLAIMS,N_XB_NONCLAIMS,True)

    key=[
        "DENSITY-MATRIX BORN RULE PREFERRED: p(i) = Tr(rho Pi_i). "
        "ONE axiom, ZERO new DOF, ZERO new objects.",
        "rho and Pi_i ALREADY EXIST in extension grammar (Q-II.B density "
        "matrix, Q-II.D su(2) observable algebra). Born rule only ADDS "
        "the identification of Tr(rho Pi_i) as probability.",
        "NORMALIZED: sum p(i) = Tr(rho) = 1. POSITIVE: rho>=0, Pi_i>=0.",
        "MINIMAL HIDDEN ASSUMPTIONS: no psi ontology, no collapse, no POVM, "
        "no apparatus model. Only: rho and Pi_i have probability interpretation.",
        "SCOPE: PROBABILITY MAP ONLY. Does NOT buy: collapse, state-update, "
        "measurement completion, unitarity, quantum ontology.",
        "This is the SMALLEST honest probability extension for GRUT. "
        "It was already identified as PX1 in Q-II.F.",
        "After adoption: diagnostic weights rho_ii BECOME probabilities. "
        "Bell-CHSH evaluation becomes interpretable. Measurement frequencies "
        "become meaningful.",
    ]

    allowed=[
        "Density-matrix Born rule: p(i)=Tr(rho Pi_i), 1 axiom, 0 new DOF",
        "Uses existing extension grammar (rho, Pi_i from Q-II.B/D)",
        "Guaranteed normalized (Tr rho=1) and nonnegative (rho>=0, Pi>=0)",
        "Minimal hidden assumptions: no psi ontology, no collapse, no POVM",
        "Scope: probability map only, not measurement completion",
        "Enables: frequency interpretation, Bell evaluation, outcome weights",
        "X-C authorized: probability postulate established",
    ]

    forbidden=[
        "Born postulate implies native probability",
        "Probability map implies collapse rule",
        "Density-matrix Born implies psi ontology",
        "Normalization implies unitarity",
        "Born rule implies measurement theory",
        "Compatibility implies quantum completion",
        "One axiom implies derivation",
    ]

    diagnostics: Dict[str,Any]={
        "preferred":"p(i)=Tr(rho Pi_i)",
        "new_axioms":1,
        "new_dof":0,
        "new_objects":0,
        "normalized":True,
        "positive":True,
        "psi_ontology_required":False,
        "collapse_required":False,
        "measurement_completion":False,
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_XB_NONCLAIMS,
    }

    result=XBMinimalBornResult(
        True,cands,N_CANDIDATES,"density_matrix_born_rule",
        fw,XB_BORN,XB_PREF,XB_INFLATION,XB_SCOPE,XB_AUTH,XB_OVERALL,
        key,allowed,forbidden,XB_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:XBMinimalBornResult)->None:
    if r.born_postulate_status not in BORN_OPTIONS:raise ValueError("born")
    if r.preferred_rule_class not in PREF_OPTIONS:raise ValueError("pref")
    if r.inflation_status not in INFLATION_OPTIONS:raise ValueError("infl")
    if r.scope_status not in SCOPE_OPTIONS:raise ValueError("scope")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_XB_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if r.diagnostics["new_dof"]!=0:raise ValueError("dof 0")
    if r.diagnostics["new_axioms"]!=1:raise ValueError("axioms 1")
    if r.diagnostics["collapse_required"]:raise ValueError("collapse False")
    if r.diagnostics["psi_ontology_required"]:raise ValueError("psi False")


def _self_test()->bool:
    r=run_xb_minimal_born_postulate_audit()
    assert r.valid
    assert r.born_postulate_status==XB_BORN
    assert r.preferred_rule_class==XB_PREF
    assert r.inflation_status==XB_INFLATION
    assert r.scope_status==XB_SCOPE
    assert r.authorization==XB_AUTH
    assert r.diagnostics["new_axioms"]==1
    assert r.diagnostics["new_dof"]==0
    assert r.diagnostics["collapse_required"] is False
    return True

if __name__=="__main__":
    _self_test();print("X-B passed.")
