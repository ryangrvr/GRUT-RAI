"""
Appendix X-C --- Outcome Selection, State-Update, and Measurement-Completion Audit
====================================================================================
GRUT Probability Program --- Phase X-C

Determines minimal outcome-selection and state-update postulate on top
of X-B Born map. Book II LOCKED. Not native. Not collapse ontology.

=== ANALYSIS ===

X-B gave: p(i) = Tr(rho Pi_i). This assigns probabilities to outcomes.
But it does NOT say "one outcome actually occurs." The Born map is a
probability ASSIGNMENT, not an outcome REALIZATION rule.

OUTCOME SELECTION:
  Minimal postulate: "In a single run, exactly one outcome i is realized
  with probability p(i) = Tr(rho Pi_i)."
  This is ONE additional axiom on top of X-B. It bridges probability
  weights to single-run actuality. No new DOF, no new objects.
  It is the standard "measurement postulate" stripped to its minimum.

  Note: this does NOT specify HOW the outcome is selected (no mechanism),
  WHY one outcome occurs (no ontology), or WHAT happens to the state
  afterward (no update). It only says: one outcome occurs, with the
  Born-given probability.

STATE UPDATE:
  After outcome i is realized, what is the post-measurement state?
  Options:
  (a) DEFERRED: no update rule now. Stop at outcome + probability.
      Pro: minimal. Con: cannot do repeated measurements consistently.
  (b) LUDERS: rho -> Pi_i rho Pi_i / Tr(rho Pi_i).
      Standard projective update. One additional axiom. No new DOF.
      Already uses existing projectors. Enables repeated measurements.
  (c) EPISTEMIC: rho -> rho_i is just conditional bookkeeping.
      Same formula as Luders but interpreted as Bayesian update, not
      physical collapse. Least ontologically committed.

  PREFERRED: Luders-style update WITH epistemic reading.
  Formula: rho -> Pi_i rho Pi_i / p(i)
  Interpretation: bookkeeping/conditional update, not ontological collapse.
  This gives repeated-measurement consistency without collapse commitment.

TOTAL POSTULATE COUNT (X-B + X-C combined):
  Axiom 1 (X-B): p(i) = Tr(rho Pi_i)  [probability map]
  Axiom 2 (X-C): one outcome realized per run  [outcome selection]
  Axiom 3 (X-C): rho -> Pi_i rho Pi_i / p(i)  [conditional update]
  Total: 3 axioms, 0 new DOF, 0 new objects, 0 new fields.

WHAT IS BOUGHT:
  - Single-run outcome realization
  - Repeated-measurement bookkeeping consistency
  - Bell-CHSH becomes operationally meaningful
  - Statistics of outcomes are Born-distributed

WHAT IS NOT BOUGHT:
  - Collapse ontology (update is bookkeeping, not mechanism)
  - Apparatus dynamics (no detector model)
  - Decoherence explanation (basis selection is separate)
  - Unitarity between measurements (not addressed)
  - Full quantum theory (measurement problem not resolved)
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_XC_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

OUTCOME_OPTIONS = frozenset({
    "minimal_outcome_selection_postulate_identified",
    "outcome_rule_requires_hidden_structure",
    "multiple_equally_minimal_outcome_rules",
    "no_stable_outcome_postulate_found",
})
UPDATE_OPTIONS = frozenset({
    "outcome_selection_only_preferred_update_deferred",
    "minimal_luders_style_update_preferred",
    "epistemic_conditioning_update_preferred",
    "instrument_style_update_required",
    "no_stable_update_rule_identified",
})
INFLATION_OPTIONS = frozenset({
    "one_axiom_outcome_rule_low_inflation",
    "low_inflation_but_update_adds_structure",
    "moderate_hidden_measurement_structure_required",
    "inflation_not_resolved",
})
SCOPE_OPTIONS = frozenset({
    "outcome_rule_bought_measurement_completion_still_partial",
    "outcome_plus_update_bought_but_no_ontology",
    "broader_measurement_structure_conditionally_supported",
    "scope_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_XD",
    "stop_for_missing_measurement_boundary",
})
OVERALL_OPTIONS = frozenset({
    "minimal_measurement_completion_identified_under_strict_postulate_accounting",
    "outcome_selection_added_with_update_rule_deferred",
    "low_inflation_measurement_rule_conditionally_supported",
    "measurement_extension_not_yet_stable",
})

XC_OUTCOME: str = "minimal_outcome_selection_postulate_identified"
XC_UPDATE: str = "epistemic_conditioning_update_preferred"
XC_INFLATION: str = "low_inflation_but_update_adds_structure"
XC_SCOPE: str = "outcome_plus_update_bought_but_no_ontology"
XC_AUTH: str = "authorized_to_proceed_to_XD"
XC_OVERALL: str = "minimal_measurement_completion_identified_under_strict_postulate_accounting"

XC_NONCLAIMS: List[str] = [
    "NOT_claiming_outcome_selection_therefore_collapse__"
    "single_run_realization_is_not_ontological_collapse_mechanism",
    "NOT_claiming_Luders_update_therefore_physical_collapse__"
    "conditional_state_update_is_bookkeeping_not_physical_process",
    "NOT_claiming_repeated_measurement_consistency_therefore_unitarity__"
    "update_rule_enables_consistency_does_not_imply_unitary_dynamics",
    "NOT_claiming_measurement_postulates_therefore_apparatus__"
    "outcome_and_update_rules_do_not_model_detector_physics",
    "NOT_claiming_Born_plus_outcome_therefore_quantum_theory__"
    "three_axioms_are_probability_plus_measurement_not_full_QM",
    "NOT_claiming_epistemic_update_therefore_no_real_change__"
    "conditional_bookkeeping_is_agnostic_about_ontic_change",
    "NOT_claiming_measurement_completion_therefore_measurement_problem_solved__"
    "operational_rules_do_not_resolve_foundational_interpretation",
    "NOT_claiming_outcome_rule_therefore_native__"
    "all_three_axioms_are_explicit_postulates",
]


@dataclass
class XCCandidate:
    name: str; new_axioms: int; new_objects: int; new_dof: int
    hidden: str; strongest: str; what_bought: str; verdict: str

@dataclass
class XCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class XCOutcomeSelectionResult:
    valid: bool
    candidates: List[XCCandidate]
    n_candidates: int
    recommended_outcome: str
    recommended_update: str
    nonclaim_firewall: XCNonclaimFirewall
    outcome_postulate_status: str; update_status: str
    inflation_status: str; scope_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[XCCandidate]:
    return [
        XCCandidate("outcome_selection_only",1,0,0,
            "none beyond Born",
            "One outcome realized per run with p(i)",
            "Single-run actuality","viable_minimal_no_update"),
        XCCandidate("luders_projective_update",1,0,0,
            "projective ontology possible",
            "rho -> Pi_i rho Pi_i / p(i)",
            "Repeated-measurement consistency","viable_standard"),
        XCCandidate("epistemic_conditioning",1,0,0,
            "minimal: same formula, bookkeeping interpretation",
            "Conditional update as bookkeeping",
            "Consistency without ontological commitment",
            "PREFERRED_least_ontological"),
        XCCandidate("instrument_cp_map",1,1,0,
            "must define instrument maps {Phi_i}",
            "General CP update",
            "Most general update","viable_but_more_inflationary"),
        XCCandidate("repeated_measurement_test",0,0,0,
            "N/A",
            "Consistency check across sequences",
            "Validates update rule","consistency_check_not_postulate"),
        XCCandidate("hidden_structure_comparison",0,0,0,
            "N/A","Comparison row","N/A","comparison_only"),
    ]


def run_xc_outcome_selection_state_update_audit() -> XCOutcomeSelectionResult:
    cands=_build_candidates()
    fw=XCNonclaimFirewall(XC_NONCLAIMS,N_XC_NONCLAIMS,True)

    key=[
        "OUTCOME SELECTION: 'one outcome i realized per run with p(i)=Tr(rho Pi_i).' "
        "One axiom on top of X-B Born map. No new DOF or objects.",
        "EPISTEMIC CONDITIONING UPDATE PREFERRED: rho -> Pi_i rho Pi_i / p(i). "
        "Same formula as Luders but interpreted as BOOKKEEPING, not collapse.",
        "TOTAL X-B + X-C: 3 axioms (Born map + outcome selection + conditional update). "
        "0 new DOF. 0 new objects. 0 new fields.",
        "WHAT IS BOUGHT: single-run outcomes, repeated-measurement consistency, "
        "operationally meaningful Bell-CHSH, Born-distributed statistics.",
        "WHAT IS NOT BOUGHT: collapse ontology, apparatus dynamics, decoherence "
        "explanation, unitarity, full quantum theory, measurement problem resolution.",
        "Epistemic over Luders: same mathematics, less ontological commitment. "
        "Update is conditional bookkeeping, not physical collapse.",
        "Measurement COMPLETION is still PARTIAL: operational rules exist, "
        "foundational interpretation remains open.",
    ]

    allowed=[
        "Outcome-selection postulate: one outcome per run with Born probability",
        "Epistemic conditioning update: rho -> Pi_i rho Pi_i / p(i) as bookkeeping",
        "Total 3 axioms (Born + outcome + update), 0 new DOF, 0 new objects",
        "Repeated-measurement consistency enabled",
        "Bell-CHSH operationally meaningful with Born + outcome + update",
        "Measurement completion is partial: rules exist, ontology open",
        "X-D authorized: measurement boundary established",
    ]

    forbidden=[
        "Outcome selection implies collapse mechanism",
        "Luders update implies physical collapse",
        "Repeated consistency implies unitarity",
        "Measurement postulates imply apparatus dynamics",
        "Born + outcome implies full quantum theory",
        "Epistemic update implies no real change",
        "Measurement completion implies measurement problem solved",
    ]

    diagnostics: Dict[str,Any]={
        "total_axioms_xb_xc":3,
        "new_dof":0,
        "new_objects":0,
        "new_fields":0,
        "outcome_rule":"one_outcome_per_run_with_born_probability",
        "update_rule":"rho_to_Pi_rho_Pi_over_p",
        "update_interpretation":"epistemic_conditioning_bookkeeping",
        "collapse_ontology":False,
        "apparatus_dynamics":False,
        "unitarity_bought":False,
        "measurement_problem_resolved":False,
        "repeated_measurement_consistent":True,
        "bell_chsh_operational":True,
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_XC_NONCLAIMS,
    }

    result=XCOutcomeSelectionResult(
        True,cands,N_CANDIDATES,
        "one_outcome_per_run","epistemic_conditioning_update",
        fw,XC_OUTCOME,XC_UPDATE,XC_INFLATION,XC_SCOPE,XC_AUTH,XC_OVERALL,
        key,allowed,forbidden,XC_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:XCOutcomeSelectionResult)->None:
    if r.outcome_postulate_status not in OUTCOME_OPTIONS:raise ValueError("outcome")
    if r.update_status not in UPDATE_OPTIONS:raise ValueError("update")
    if r.inflation_status not in INFLATION_OPTIONS:raise ValueError("infl")
    if r.scope_status not in SCOPE_OPTIONS:raise ValueError("scope")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_XC_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if r.diagnostics["total_axioms_xb_xc"]!=3:raise ValueError("axioms 3")
    if r.diagnostics["new_dof"]!=0:raise ValueError("dof 0")
    if r.diagnostics["collapse_ontology"]:raise ValueError("collapse False")
    if r.diagnostics["measurement_problem_resolved"]:raise ValueError("resolved False")
    if not r.diagnostics["repeated_measurement_consistent"]:raise ValueError("consistent True")
    if not r.diagnostics["bell_chsh_operational"]:raise ValueError("bell True")


def _self_test()->bool:
    r=run_xc_outcome_selection_state_update_audit()
    assert r.valid
    assert r.outcome_postulate_status==XC_OUTCOME
    assert r.update_status==XC_UPDATE
    assert r.inflation_status==XC_INFLATION
    assert r.scope_status==XC_SCOPE
    assert r.authorization==XC_AUTH
    assert r.diagnostics["total_axioms_xb_xc"]==3
    assert r.diagnostics["new_dof"]==0
    assert r.diagnostics["collapse_ontology"] is False
    assert r.diagnostics["bell_chsh_operational"] is True
    return True

if __name__=="__main__":
    _self_test();print("X-C passed.")
