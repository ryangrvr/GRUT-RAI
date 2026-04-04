"""
Appendix Y-A --- Quantum-Dynamical Closure and Sector-Interface Charter
========================================================================
GRUT Quantum-Dynamical Closure Program --- Phase Y-A
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "Y0_quantum_dynamical_closure_entry_inventory",
    "Y-A_quantum_dynamical_closure_charter",
    "Y-B_between_measurement_evolution_postulate",
    "Y-C_decoherence_and_basis_selection_closure",
    "Y-D_sector_integration_criteria_and_interface_rules",
    "Y-E_final_quantum_dynamical_ledger_and_program_closure",
]
N_STAGES: int = 6; N_DISTINCTIONS: int = 15; N_RULES: int = 8
N_FFMS: int = 8; N_YA_NONCLAIMS: int = 8; N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "unitarity_from_probability",
    "quantum_dynamics_from_born_rule",
    "decoherence_from_dissipation",
    "collapse_from_epistemic_update",
    "apparatus_from_projector_grammar",
    "sector_integration_from_compatibility",
    "quantum_completion_from_architecture",
    "dynamics_from_measurement_only",
]

YA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_derives_dynamics__charter_defines_rules",
    "NOT_claiming_probability_layer_implies_evolution__separate_question",
    "NOT_claiming_Lindblad_implies_unitarity__open_system_not_closed",
    "NOT_claiming_compatibility_implies_integration__separate_test",
    "NOT_claiming_hyperbolic_action_implies_quantum_dynamics__extension_not_QM",
    "NOT_claiming_interface_rules_imply_interfaces_built__rules_govern_future",
    "NOT_claiming_stage_success_guaranteed__each_may_yield_BSR",
    "NOT_claiming_Y_closure_implies_physics_closure__final_architecture_not_final_physics",
]

CHARTER_VERDICT: str = "charter_defined_with_strict_closure_and_interface_firewall"
AUTH_VERDICT: str = "authorized_to_proceed_to_YB"
OVERALL_P: str = "quantum_dynamical_closure_program_opened_under_strict_limits"
ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})


@dataclass
class YADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class YAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; notes: List[str]

@dataclass
class YARule:
    rule_id: str; statement: str; violation: str

@dataclass
class YAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class YANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class YACharter:
    valid: bool
    distinctions: List[YADistinction]
    stage_sequence: List[YAStageDef]
    rules: List[YARule]; ffms: List[YAFFM]
    entry_nonclaims: YANonclaims
    charter_verdict: str; authorization_verdict: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[YADistinction]:
    return [
        YADistinction("D1","probability_layer","full_quantum_dynamics",
            "Born map != state-evolution law"),
        YADistinction("D2","outcome_rule","evolution_law",
            "Outcome selection != between-measurement dynamics"),
        YADistinction("D3","epistemic_update","collapse_ontology",
            "Bookkeeping update != physical state change"),
        YADistinction("D4","operational_consistency","ontological_completion",
            "Works in practice != settled in theory"),
        YADistinction("D5","hyperbolic_action_core","unitary_quantum_theory",
            "Extension action != quantum Hamiltonian"),
        YADistinction("D6","response_functional","physical_quantum_dynamics",
            "Auxiliary packaging != dynamical evolution"),
        YADistinction("D7","dissipation","decoherence",
            "Energy loss != basis selection"),
        YADistinction("D8","compatibility","integration",
            "No contradiction != shared dynamics/closure"),
        YADistinction("D9","integrated_sector","attached_patch",
            "Common dynamics != separate overlay"),
        YADistinction("D10","sequential_measurements","apparatus_theory",
            "Iterated update != detector model"),
        YADistinction("D11","extension_interface","closure",
            "Hook for future work != solved sector"),
        YADistinction("D12","minimal_postulate","derivation",
            "New axiom != consequence"),
        YADistinction("D13","dynamic_law","measurement_law",
            "Time evolution != outcome assignment"),
        YADistinction("D14","state_label","state_ontology",
            "rho as bookkeeping != rho as reality"),
        YADistinction("D15","large_architecture","completion",
            "Many appendices != solved physics"),
    ]

def _stages() -> List[YAStageDef]:
    return [
        YAStageDef("Y0","Quantum-dynamical entry inventory",0,
            "What dynamical/interface structures exist?",[]),
        YAStageDef("Y-A","Quantum-dynamical charter",1,
            "What rules govern closure/interface work?",[]),
        YAStageDef("Y-B","Between-measurement evolution",2,
            "Can a state-evolution postulate be added?",
            ["Lindblad candidate; unitary/nonunitary comparison"]),
        YAStageDef("Y-C","Decoherence and basis-selection closure",3,
            "Can decoherence be placed on firmer footing?",
            ["Requires Y-B evolution law"]),
        YAStageDef("Y-D","Sector integration criteria",4,
            "What rules must future sectors satisfy?",
            ["Interface requirements for gauge, fermions, chemistry, cosmology"]),
        YAStageDef("Y-E","Final quantum-dynamical ledger",5,
            "Close Y with final dynamical and interface status.",
            ["Program closure stage"]),
    ]

def _rules() -> List[YARule]:
    return [
        YARule("Y-R1","Every dynamical/interface claim carries classification.","undisciplined_claim"),
        YARule("Y-R2","Evolution law must be explicitly postulated.","evolution_smuggling"),
        YARule("Y-R3","Integration requires shared dynamics, not just compatibility.","compatibility_as_integration"),
        YARule("Y-R4","All 15 mandatory distinctions maintained.","distinction_collapse"),
        YARule("Y-R5","Dissipation is not decoherence without derivation.","dissipation_as_decoherence"),
        YARule("Y-R6","Book II/III/X locked classes persist.","retroactive_promotion"),
        YARule("Y-R7","Operational sufficiency is not ontological completion.","operational_as_complete"),
        YARule("Y-R8","Future sector hooks are not solved sectors.","hook_as_closure"),
    ]

def _ffms() -> List[YAFFM]:
    return [
        YAFFM("FFM-Y.1","unitarity_from_probability",
            "Inferring unitary evolution from Born probabilities.",
            "Born is outcome weight; unitarity is dynamical symmetry"),
        YAFFM("FFM-Y.2","quantum_dynamics_from_born_rule",
            "Inferring quantum dynamics from the Born map alone.",
            "Probability assignment != state-evolution law"),
        YAFFM("FFM-Y.3","decoherence_from_dissipation",
            "Equating native dissipation with quantum decoherence.",
            "Dissipation is energy loss; decoherence is basis selection"),
        YAFFM("FFM-Y.4","collapse_from_epistemic_update",
            "Inferring physical collapse from bookkeeping update.",
            "Epistemic conditioning is agnostic about physical change"),
        YAFFM("FFM-Y.5","apparatus_from_projector_grammar",
            "Inferring detector physics from projector mathematics.",
            "Projectors define outcome spaces, not physical detectors"),
        YAFFM("FFM-Y.6","sector_integration_from_compatibility",
            "Calling compatible coexistence 'integrated sector.'",
            "Integration requires shared dynamics and closure"),
        YAFFM("FFM-Y.7","quantum_completion_from_architecture",
            "Declaring QM complete because many appendices exist.",
            "Architecture is scaffolding; completion is derivation"),
        YAFFM("FFM-Y.8","dynamics_from_measurement_only",
            "Inferring time evolution from measurement rules alone.",
            "Measurement is at-a-time; dynamics is between-times"),
    ]


def run_ya_quantum_dynamical_closure_charter() -> YACharter:
    dist=_distinctions();stg=_stages();rul=_rules();ffm=_ffms()
    nc=YANonclaims(YA_NONCLAIMS,N_YA_NONCLAIMS,True)

    key=[
        "15 mandatory distinctions: probability!=dynamics, outcome!=evolution, "
        "epistemic!=collapse, operational!=ontological, action!=unitary, "
        "response!=dynamics, dissipation!=decoherence, compatibility!=integration, etc.",
        "8 rules: evolution must be postulated, integration requires shared dynamics, "
        "dissipation!=decoherence, operational!=complete, hooks!=closure.",
        "8 FFMs: unitarity from probability, dynamics from Born, decoherence from "
        "dissipation, collapse from update, apparatus from projectors, "
        "integration from compatibility, completion from architecture, "
        "dynamics from measurement.",
        "Operational probability layer EXISTS (X closed). True quantum dynamics "
        "and sector integration remain ABSENT.",
        "Y-B licensed: between-measurement evolution postulate.",
        "Y is the FINAL substantive architecture appendix.",
    ]

    allowed=[
        "Operational probability layer present (X-B/X-C/X-D confirmed)",
        "15 mandatory distinctions between operational and dynamical/complete",
        "8 FFMs prevent dynamics/integration overclaiming",
        "Evolution law requires explicit new postulate (not native or from X stack)",
        "Y-B licensed: between-measurement evolution postulate candidates",
        "Sector integration requires shared dynamics, not just compatibility",
        "Y program opened under strict closure and interface firewall",
    ]

    forbidden=[
        "Probability layer implies quantum dynamics",
        "Born rule implies state evolution",
        "Dissipation implies decoherence",
        "Epistemic update implies collapse",
        "Projector grammar implies apparatus",
        "Compatibility implies integration",
        "Architecture implies completion",
    ]

    diag: Dict[str,Any]={"n_stages":N_STAGES,"n_distinctions":N_DISTINCTIONS,
        "n_rules":N_RULES,"n_ffms":N_FFMS,"n_nonclaims":N_YA_NONCLAIMS,
        "unitarity_present":False,"evolution_law_present":False,
        "sector_integration_present":False}

    result=YACharter(True,dist,stg,rul,ffm,nc,
        CHARTER_VERDICT,AUTH_VERDICT,OVERALL_P,key,allowed,forbidden,diag)
    _validate(result);return result


def _validate(r:YACharter)->None:
    if len(r.distinctions)!=N_DISTINCTIONS:raise ValueError("dist")
    if len(r.stage_sequence)!=N_STAGES:raise ValueError("stages")
    for i,s in enumerate(r.stage_sequence):
        if s.stage_index!=i:raise ValueError(f"stage {s.stage_id}")
    if len(r.rules)!=N_RULES:raise ValueError("rules")
    if len(r.ffms)!=N_FFMS:raise ValueError("ffms")
    names=[f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names:raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims!=N_YA_NONCLAIMS:raise ValueError("nc")
    if not r.entry_nonclaims.all_registered:raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS:raise ValueError("charter")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if r.diagnostics["unitarity_present"]:raise ValueError("unit False")


def _self_test()->bool:
    r=run_ya_quantum_dynamical_closure_charter()
    assert r.valid and r.charter_verdict==CHARTER_VERDICT
    assert r.authorization_verdict==AUTH_VERDICT
    assert r.overall_appendix_p==OVERALL_P
    assert len(r.distinctions)==N_DISTINCTIONS
    assert r.diagnostics["unitarity_present"] is False
    return True

if __name__=="__main__":
    _self_test();print("Y-A passed.")
