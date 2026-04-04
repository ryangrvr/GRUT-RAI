"""
Appendix X-A --- Probability, Measurement, and Quantum-Completion Charter
==========================================================================
GRUT Probability Program --- Phase X-A
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "X0_probability_measurement_entry_inventory",
    "X-A_probability_measurement_charter",
    "X-B_born_rule_postulation_and_minimal_measurement",
    "X-C_outcome_selection_and_state_update",
    "X-D_quantum_probability_closure_boundary",
    "X-E_final_probability_ledger_and_handoff",
]
N_STAGES: int = 6; N_DISTINCTIONS: int = 12; N_RULES: int = 8
N_FFMS: int = 8; N_XA_NONCLAIMS: int = 8; N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "born_from_qubit_notation",
    "probability_from_response_functional",
    "wavefunction_from_auxiliary_field",
    "collapse_from_dissipation",
    "unitarity_from_undamped_core",
    "quantum_completion_from_compatibility",
    "measurement_from_decoherence_alone",
    "frequency_from_diagnostic_weights",
]

XA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_derives_probability__charter_defines_rules",
    "NOT_claiming_observable_algebra_implies_Born__algebra_is_grammar_not_axiom",
    "NOT_claiming_decoherence_implies_measurement__basis_selection_is_not_outcome",
    "NOT_claiming_qubit_implies_quantum__extension_grammar_is_not_QM",
    "NOT_claiming_compatibility_implies_completion__layered_is_not_integrated",
    "NOT_claiming_response_functional_implies_wavefunction__auxiliary_is_not_psi",
    "NOT_claiming_stage_success_guaranteed__each_may_yield_BSR",
    "NOT_claiming_authorization_implies_quantum_closure__licensed_not_solved",
]

CHARTER_VERDICT: str = "charter_defined_with_strict_anti_retroactive_rules"
AUTH_VERDICT: str = "authorized_to_proceed_to_XB"
OVERALL_P: str = "probability_program_opened_under_strict_limits"
ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})


@dataclass
class XADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class XAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; notes: List[str]

@dataclass
class XARule:
    rule_id: str; statement: str; violation: str

@dataclass
class XAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class XANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class XACharter:
    valid: bool
    distinctions: List[XADistinction]
    stage_sequence: List[XAStageDef]
    rules: List[XARule]; ffms: List[XAFFM]
    entry_nonclaims: XANonclaims
    charter_verdict: str; authorization_verdict: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[XADistinction]:
    return [
        XADistinction("D1","observable_algebra","born_rule","Algebra is grammar; Born is probability axiom"),
        XADistinction("D2","amplitude","probability","Amplitude is complex number; probability is real frequency"),
        XADistinction("D3","state_variable","quantum_state","Classical state var != quantum state with superposition"),
        XADistinction("D4","response_functional","wavefunction","Auxiliary packaging != physical psi"),
        XADistinction("D5","interference_structure","measurement_theory","Cross terms != outcome selection"),
        XADistinction("D6","ensemble_language","intrinsic_probability","Repetition assumption != fundamental randomness"),
        XADistinction("D7","decoherence","collapse","Basis selection != outcome selection"),
        XADistinction("D8","frequency_fit","probabilistic_derivation","Fitting data != deriving probability law"),
        XADistinction("D9","auxiliary_formalism","ontology","Mathematical tool != physical claim"),
        XADistinction("D10","quantum_compatibility","quantum_completion","Compatible grammar != full QM"),
        XADistinction("D11","minimal_postulate","native_recovery","New axiom != native consequence"),
        XADistinction("D12","measurement_model","full_quantum_theory","Measurement postulate != complete QM"),
    ]

def _stages() -> List[XAStageDef]:
    return [
        XAStageDef("X0","Probability entry inventory",0,"What probability structures exist?",[]),
        XAStageDef("X-A","Probability charter",1,"What rules govern probability claims?",[]),
        XAStageDef("X-B","Born rule postulation",2,
            "Can Born rule be adopted as MIP and what does it enable?",
            ["Smallest probability postulate; already identified as PX1"]),
        XAStageDef("X-C","Outcome selection and state update",3,
            "Can outcome selection or collapse be formulated?",
            ["Requires Born rule from X-B as prerequisite"]),
        XAStageDef("X-D","Quantum probability closure boundary",4,
            "What quantum probability structure is now available?",
            ["Synthesizes X-B and X-C"]),
        XAStageDef("X-E","Final probability ledger and handoff",5,
            "Close X with final probability status.",[]),
    ]

def _rules() -> List[XARule]:
    return [
        XARule("X-R1","Every probability claim carries explicit classification.","undisciplined_claim"),
        XARule("X-R2","Born rule must be explicitly postulated, not smuggled.","born_smuggling"),
        XARule("X-R3","Measurement postulate must be separate from decoherence.","decoherence_as_measurement"),
        XARule("X-R4","All 12 mandatory distinctions maintained.","distinction_collapse"),
        XARule("X-R5","Response functional is auxiliary, not wavefunction.","auxiliary_as_psi"),
        XARule("X-R6","Book II and III locked classes persist.","retroactive_promotion"),
        XARule("X-R7","Compatibility with quantum language != quantum completion.","compatibility_as_completion"),
        XARule("X-R8","New axioms labeled as postulates, not discoveries.","postulate_as_discovery"),
    ]

def _ffms() -> List[XAFFM]:
    return [
        XAFFM("FFM-X.1","born_from_qubit_notation","Inferring Born from qubit notation alone.",
            "Born is an axiom, not a consequence of C^2 algebra"),
        XAFFM("FFM-X.2","probability_from_response_functional","Inferring probability from S_eff packaging.",
            "Response functional is auxiliary mathematical tool"),
        XAFFM("FFM-X.3","wavefunction_from_auxiliary_field","Calling Phi_tilde a wavefunction.",
            "Phi_tilde is nonnative response field"),
        XAFFM("FFM-X.4","collapse_from_dissipation","Inferring collapse from Lindblad decay.",
            "Decoherence selects basis; collapse selects outcome"),
        XAFFM("FFM-X.5","unitarity_from_undamped_core","Inferring unitarity from undamped action.",
            "Undamped core is a limit; full system is dissipative"),
        XAFFM("FFM-X.6","quantum_completion_from_compatibility","Inferring QM from compatible grammar.",
            "Compatible extension != complete quantum theory"),
        XAFFM("FFM-X.7","measurement_from_decoherence_alone","Inferring measurement from basis selection.",
            "Basis selection != outcome selection"),
        XAFFM("FFM-X.8","frequency_from_diagnostic_weights","Treating rho_nn as frequencies without Born.",
            "Diagnostic weights require Born axiom for frequency interpretation"),
    ]


def run_xa_probability_measurement_charter() -> XACharter:
    dist=_distinctions();stg=_stages();rul=_rules();ffm=_ffms()
    nc=XANonclaims(XA_NONCLAIMS,N_XA_NONCLAIMS,True)

    key=[
        "12 mandatory distinctions: algebra!=Born, amplitude!=probability, "
        "decoherence!=collapse, response!=psi, compatibility!=completion, etc.",
        "8 rules: Born must be explicit postulate, measurement != decoherence, "
        "auxiliary != psi, new axioms labeled as postulates.",
        "8 FFMs: Born from notation, probability from S_eff, collapse from "
        "dissipation, unitarity from undamped core, completion from compatibility.",
        "Observable grammar EXISTS at extension level (su(2), C^2, density matrix). "
        "Probability and measurement are ABSENT.",
        "X-B licensed: Born rule postulation as MIP (PX1, smallest axiom, no new DOF).",
        "Probability program opens under strict anti-retroactive discipline.",
    ]

    allowed=[
        "Observable grammar present at extension level (su(2), C^2, rho)",
        "12 mandatory distinctions between quantum-looking and quantum-complete",
        "8 FFMs prevent probability/measurement overclaiming",
        "Born rule and measurement postulate require explicit new axioms",
        "X-B licensed: Born rule MIP postulation (PX1)",
        "Book II and III classes locked immutably",
        "Probability program opened under strict limits",
    ]

    forbidden=[
        "Observable algebra implies Born rule",
        "Response functional implies wavefunction",
        "Decoherence implies measurement",
        "Qubit notation implies quantum mechanics",
        "Compatibility implies quantum completion",
        "Diagnostic weights imply frequencies",
        "Authorization implies quantum closure",
    ]

    diag: Dict[str,Any]={"n_stages":N_STAGES,"n_distinctions":N_DISTINCTIONS,
        "n_rules":N_RULES,"n_ffms":N_FFMS,"n_nonclaims":N_XA_NONCLAIMS,
        "born_present":False,"measurement_present":False}

    result=XACharter(True,dist,stg,rul,ffm,nc,
        CHARTER_VERDICT,AUTH_VERDICT,OVERALL_P,key,allowed,forbidden,diag)
    _validate(result);return result


def _validate(r:XACharter)->None:
    if len(r.distinctions)!=N_DISTINCTIONS:raise ValueError("dist")
    if len(r.stage_sequence)!=N_STAGES:raise ValueError("stages")
    for i,s in enumerate(r.stage_sequence):
        if s.stage_index!=i:raise ValueError(f"stage {s.stage_id}")
    if len(r.rules)!=N_RULES:raise ValueError("rules")
    if len(r.ffms)!=N_FFMS:raise ValueError("ffms")
    names=[f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names:raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims!=N_XA_NONCLAIMS:raise ValueError("nc")
    if not r.entry_nonclaims.all_registered:raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS:raise ValueError("charter")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if r.diagnostics["born_present"]:raise ValueError("born False")


def _self_test()->bool:
    r=run_xa_probability_measurement_charter()
    assert r.valid and r.charter_verdict==CHARTER_VERDICT
    assert r.authorization_verdict==AUTH_VERDICT
    assert r.overall_appendix_p==OVERALL_P
    assert len(r.distinctions)==N_DISTINCTIONS
    assert r.diagnostics["born_present"] is False
    return True

if __name__=="__main__":
    _self_test();print("X-A passed.")
