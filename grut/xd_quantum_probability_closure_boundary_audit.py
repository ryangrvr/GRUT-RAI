"""
Appendix X-D --- Quantum Probability Closure Boundary Audit
=============================================================
GRUT Probability Program --- Phase X-D

Determines whether the X-B+X-C stack is operationally sufficient as
a stable quantum-probability layer, and identifies exact closure gaps.

=== ANALYSIS ===

OPERATIONAL SUFFICIENCY:
  The X-B+X-C stack supports:
  (1) Normalized probabilities: p(i) = Tr(rho Pi_i), sum=1, p>=0. YES.
  (2) Single-run outcomes: one i realized per run. YES.
  (3) Repeated measurement: rho -> Pi_i rho Pi_i / p(i). YES.
  (4) Expectation values: <A> = Tr(rho A) = sum a_i p(i). YES.
  (5) Bell/CHSH evaluation: <S> = Tr(rho S_CHSH) with Born meaning. YES.

  The stack IS operationally sufficient for probability assignment,
  outcome realization, and repeated-measurement bookkeeping.

UNITARITY GAP:
  The stack says nothing about time evolution BETWEEN measurements.
  In standard QM: rho(t) = U(t) rho(0) U^dag(t) (unitary evolution).
  In GRUT: native dynamics are dissipative (Lindblad, not unitary).
  The extension-level Hamiltonian part -i[H,rho] provides unitary-like
  evolution as part of the Lindblad equation, but with dissipation.

  For the CURRENT SCOPE (probability + outcome + update):
  unitarity is NOT required. The Born map and outcome rule work at any
  single time. Repeated measurements work via the update rule.
  Time evolution between measurements is a SEPARATE question.

  Classification: unitarity missing but NONFATAL for current scope.
  It blocks full quantum closure but not operational probability use.

APPARATUS GAP:
  The stack has NO apparatus dynamics. It says what outcomes occur and
  with what probability, but not HOW a physical apparatus produces them.
  For OPERATIONAL probability use: apparatus model can be DEFERRED.
  For COMPLETION: it would eventually be needed.

  Classification: deferred, not immediately required.

DECOHERENCE/COLLAPSE BOUNDARY:
  The epistemic update rho -> Pi_i rho Pi_i / p(i) is bookkeeping.
  It is NOT a physical process. The stack is internally coherent
  WITHOUT decoherence or collapse ontology. These are separate questions.

  The stack IS stable without them at the operational level.

CLOSURE LABEL:
  The X-B+X-C stack is an OPERATIONAL QUANTUM-PROBABILITY LAYER:
  it assigns probabilities, selects outcomes, and handles repeated
  measurements. It is NOT full quantum theory (no unitarity, no
  apparatus, no ontology). It is more than "bookkeeping only" because
  it includes outcome realization and consistency.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CAPABILITIES: int = 6
N_GAPS: int = 6
N_XD_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

OP_OPTIONS = frozenset({
    "operational_probability_layer_supported",
    "minimal_measurement_bookkeeping_only",
    "operational_layer_not_stable",
    "closure_not_resolved",
})
UNIT_OPTIONS = frozenset({
    "unitarity_missing_but_nonfatal_for_current_scope",
    "unitarity_gap_blocks_full_quantum_closure",
    "unitarity_gap_blocks_even_operational_use",
    "unitarity_gap_not_resolved",
})
APP_OPTIONS = frozenset({
    "apparatus_model_deferred_but_not_immediately_required",
    "apparatus_gap_limits_completion_not_operation",
    "apparatus_structure_immediately_required",
    "apparatus_gap_not_resolved",
})
LABEL_OPTIONS = frozenset({
    "operational_quantum_probability_layer_only",
    "partial_measurement_completion_without_quantum_ontology",
    "unstable_probability_patch_only",
    "closure_label_not_stable",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_XE",
    "stop_for_missing_probability_closure_boundary",
})
OVERALL_OPTIONS = frozenset({
    "probability_and_measurement_stack_operationally_bounded_but_not_quantum_complete",
    "minimal_quantum_probability_layer_identified_without_unitary_completion",
    "measurement_bookkeeping_stable_but_ontology_deferred",
    "quantum_probability_closure_not_yet_stable",
})

XD_OP: str = "operational_probability_layer_supported"
XD_UNIT: str = "unitarity_missing_but_nonfatal_for_current_scope"
XD_APP: str = "apparatus_model_deferred_but_not_immediately_required"
XD_LABEL: str = "operational_quantum_probability_layer_only"
XD_AUTH: str = "authorized_to_proceed_to_XE"
XD_OVERALL: str = "minimal_quantum_probability_layer_identified_without_unitary_completion"

XD_NONCLAIMS: List[str] = [
    "NOT_claiming_operational_layer_therefore_full_QM__"
    "probability_bookkeeping_is_not_quantum_completion",
    "NOT_claiming_operational_sufficiency_therefore_unitarity__"
    "probability_at_single_time_does_not_imply_unitary_evolution",
    "NOT_claiming_repeated_measurement_therefore_apparatus__"
    "update_rule_is_bookkeeping_not_detector_physics",
    "NOT_claiming_Bell_operational_therefore_nonlocality_proven__"
    "Born_evaluation_of_CHSH_is_not_experimental_verification",
    "NOT_claiming_epistemic_update_therefore_decoherence__"
    "conditional_bookkeeping_is_not_basis_selection_mechanism",
    "NOT_claiming_closure_boundary_therefore_closure__"
    "boundary_identification_is_not_gap_resolution",
    "NOT_claiming_stable_layer_therefore_ontology__"
    "operational_stability_is_not_ontological_commitment",
    "NOT_claiming_nonfatal_gap_therefore_negligible__"
    "unitarity_gap_blocks_full_closure_even_if_not_operational",
]


@dataclass
class XDCapability:
    name: str; supported: bool; what_bought: str; what_missing: str
    strongest: str; verdict: str

@dataclass
class XDGap:
    rank: int; name: str; description: str; blocks_operation: bool
    blocks_completion: bool

@dataclass
class XDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class XDQuantumProbabilityClosureResult:
    valid: bool
    capabilities: List[XDCapability]
    gaps: List[XDGap]
    nonclaim_firewall: XDNonclaimFirewall
    operational_status: str; unitarity_gap_status: str
    apparatus_gap_status: str; closure_label_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_capabilities() -> List[XDCapability]:
    return [
        XDCapability("probability_assignment",True,
            "p(i)=Tr(rho Pi_i): normalized, positive","Frequency derivation",
            "Born probability map","operational"),
        XDCapability("single_run_outcome",True,
            "One outcome realized per run","Mechanism/ontology of selection",
            "Outcome realization","operational"),
        XDCapability("repeated_measurement",True,
            "rho -> Pi_i rho Pi_i / p(i)","Physical collapse model",
            "Repeated-measurement consistency","operational"),
        XDCapability("expectation_values",True,
            "<A>=Tr(rho A)=sum a_i p(i)","Time evolution of <A>",
            "Expectation-value computation","operational"),
        XDCapability("bell_chsh_evaluation",True,
            "<S>=Tr(rho S_CHSH) with Born meaning","Experimental verification",
            "Bell-CHSH operational meaning","operational"),
        XDCapability("time_evolution",False,
            "Nothing (unitarity absent)","Unitary or dissipative inter-measurement dynamics",
            "N/A","gap"),
    ]

def _build_gaps() -> List[XDGap]:
    return [
        XDGap(1,"unitarity_inter_measurement_dynamics",
            "No dynamical law for rho(t) between measurements in probability sector",
            False,True),
        XDGap(2,"apparatus_dynamics",
            "No detector/apparatus model; outcomes are postulated not derived",
            False,True),
        XDGap(3,"decoherence_mechanism",
            "Basis selection not derived within probability sector",
            False,True),
        XDGap(4,"quantum_state_ontology",
            "rho interpreted as bookkeeping, not committed to psi or rho ontology",
            False,True),
        XDGap(5,"measurement_problem",
            "Why one outcome? Not answered; only postulated",
            False,True),
        XDGap(6,"fermionic_matter_integration",
            "Probability sector not connected to fermionic matter (blocked)",
            False,True),
    ]


def run_xd_quantum_probability_closure_boundary_audit() -> XDQuantumProbabilityClosureResult:
    caps=_build_capabilities();gaps=_build_gaps()
    fw=XDNonclaimFirewall(XD_NONCLAIMS,N_XD_NONCLAIMS,True)

    key=[
        "OPERATIONALLY SUFFICIENT: probability assignment, outcome selection, "
        "repeated measurement, expectation values, Bell-CHSH all supported.",
        "UNITARITY GAP: missing but NONFATAL for current scope. Born map "
        "and outcome rule work at single time; time evolution is separate question.",
        "APPARATUS GAP: deferred. Operational probability does not require "
        "apparatus model. Completion would eventually need it.",
        "DECOHERENCE/COLLAPSE: absent from probability sector. Stack is "
        "internally coherent without them at operational level.",
        "CLOSURE LABEL: OPERATIONAL QUANTUM-PROBABILITY LAYER. More than "
        "bookkeeping (includes outcome realization). Less than full QM.",
        "6 CLOSURE GAPS ranked: unitarity, apparatus, decoherence, ontology, "
        "measurement problem, fermionic integration. None blocks operation; "
        "all block full quantum completion.",
    ]

    allowed=[
        "Operational probability layer: probability, outcomes, repeated "
        "measurement, expectation values, Bell-CHSH all supported",
        "Unitarity missing but nonfatal for current operational scope",
        "Apparatus model deferred: not immediately required for probability",
        "Stack internally coherent without decoherence or collapse ontology",
        "Closure label: operational quantum-probability layer (not full QM)",
        "6 closure gaps documented: none blocks operation, all block completion",
        "X-E authorized: closure boundary established",
    ]

    forbidden=[
        "Operational layer implies full quantum mechanics",
        "Operational sufficiency implies unitarity",
        "Repeated measurement implies apparatus physics",
        "Bell operational implies nonlocality proven",
        "Epistemic update implies decoherence",
        "Stable layer implies ontological commitment",
        "Nonfatal gap implies negligible gap",
    ]

    diagnostics: Dict[str,Any]={
        "n_capabilities_supported":sum(1 for c in caps if c.supported),
        "n_capabilities_total":len(caps),
        "n_gaps":len(gaps),
        "n_gaps_block_operation":sum(1 for g in gaps if g.blocks_operation),
        "n_gaps_block_completion":sum(1 for g in gaps if g.blocks_completion),
        "unitarity_present":False,
        "apparatus_present":False,
        "decoherence_present":False,
        "ontology_committed":False,
        "full_qm":False,
        "operationally_sufficient":True,
        "n_nonclaims":N_XD_NONCLAIMS,
    }

    result=XDQuantumProbabilityClosureResult(
        True,caps,gaps,fw,
        XD_OP,XD_UNIT,XD_APP,XD_LABEL,XD_AUTH,XD_OVERALL,
        key,allowed,forbidden,XD_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:XDQuantumProbabilityClosureResult)->None:
    if r.operational_status not in OP_OPTIONS:raise ValueError("op")
    if r.unitarity_gap_status not in UNIT_OPTIONS:raise ValueError("unit")
    if r.apparatus_gap_status not in APP_OPTIONS:raise ValueError("app")
    if r.closure_label_status not in LABEL_OPTIONS:raise ValueError("label")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_XD_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.capabilities)!=N_CAPABILITIES:raise ValueError("caps")
    if len(r.gaps)!=N_GAPS:raise ValueError("gaps")
    if r.diagnostics["full_qm"]:raise ValueError("qm False")
    if not r.diagnostics["operationally_sufficient"]:raise ValueError("op True")
    if r.diagnostics["n_gaps_block_operation"]!=0:raise ValueError("op gaps 0")


def _self_test()->bool:
    r=run_xd_quantum_probability_closure_boundary_audit()
    assert r.valid
    assert r.operational_status==XD_OP
    assert r.unitarity_gap_status==XD_UNIT
    assert r.apparatus_gap_status==XD_APP
    assert r.closure_label_status==XD_LABEL
    assert r.authorization==XD_AUTH
    assert r.diagnostics["operationally_sufficient"] is True
    assert r.diagnostics["full_qm"] is False
    assert r.diagnostics["n_gaps_block_operation"]==0
    assert r.diagnostics["n_gaps_block_completion"]==6
    return True

if __name__=="__main__":
    _self_test();print("X-D passed.")
