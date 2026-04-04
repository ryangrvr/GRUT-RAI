"""
Appendix X0 --- Probability, Measurement, and Quantum-Completion Entry Inventory
==================================================================================
GRUT Probability Program --- Phase X0

Inventories all probability/measurement/quantum-relevant structures.
Book II LOCKED. Book III extensions are postulates, not native.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

ALLOWED_CLS = frozenset({
    "present_native","present_but_limited","extension_only",
    "constitutive_or_effective_only","absent_unbuilt",
    "blocked_by_structure","requires_new_postulates",
})

N_ITEMS: int = 25
N_X0_NONCLAIMS: int = 8

X0_INVENTORY: str = "probability_inventory_complete_and_bounded"
X0_QUANTUM: str = "observable_grammar_present_but_probability_absent"
X0_POSTULATE: str = "born_and_measurement_require_explicit_postulates"

X0_NONCLAIMS: List[str] = [
    "NOT_claiming_observable_algebra_therefore_quantum_mechanics__"
    "su2_grammar_on_C2_is_not_full_quantum_theory",
    "NOT_claiming_response_functional_therefore_wavefunction__"
    "Phi_tilde_packaging_is_auxiliary_not_psi",
    "NOT_claiming_decoherence_therefore_measurement__"
    "off_diagonal_suppression_is_not_outcome_selection",
    "NOT_claiming_interference_like_structure_therefore_probabilities__"
    "cross_terms_require_Born_for_frequency_interpretation",
    "NOT_claiming_qubit_notation_therefore_Born_rule__"
    "density_matrix_formalism_does_not_contain_probability_axiom",
    "NOT_claiming_diagnostic_weights_therefore_probabilities__"
    "rho_nn_is_bookkeeping_without_Born",
    "NOT_claiming_extension_compatibility_therefore_quantum_completion__"
    "compatible_grammar_is_not_measurement_theory",
    "NOT_claiming_inventory_therefore_probability_derived__"
    "inventory_documents_absence_not_presence",
]


@dataclass
class X0Item:
    item_id: str; item_name: str; classification: str
    what_established: str; what_absent: str; x_licensed: bool

@dataclass
class X0ProbabilityEntryResult:
    valid: bool; items: List[X0Item]; n_items: int
    n_native: int; n_limited: int; n_extension: int; n_constitutive: int
    n_absent: int; n_blocked: int; n_postulate: int
    nonclaims: List[str]
    inventory_verdict: str; quantum_content_verdict: str; postulate_verdict: str
    diagnostics: Dict[str, Any]


def _build_items() -> List[X0Item]:
    return [
        X0Item("X1","state_variable_candidate","extension_only",
            "Density matrix rho on C^2 (Q-II.B extension)","Native quantum state",True),
        X0Item("X2","observable_algebra","extension_only",
            "su(2) on C^2 qubit (Q-II.D MBU)","Native or gauge algebra",True),
        X0Item("X3","hilbert_space_structure","extension_only",
            "C^2 qubit, C^4 composite (Q-II.B/C)","Native Hilbert space",True),
        X0Item("X4","complex_amplitude","extension_only",
            "J with J^2=-1 (Q-B.5 MIP)","Native complex structure",True),
        X0Item("X5","born_probability_map","absent_unbuilt",
            "Nothing (Q-II.F: identified as PX1 MIP but not adopted)","P(n)=Tr(rho P_n)",True),
        X0Item("X6","measurement_postulate","absent_unbuilt",
            "Nothing","Measurement axiom",True),
        X0Item("X7","outcome_rule","absent_unbuilt",
            "Nothing (Q-D: all 4 mechanisms absent)","Single-outcome selection",True),
        X0Item("X8","state_update_collapse","absent_unbuilt",
            "Nothing","Collapse or update rule",True),
        X0Item("X9","ensemble_interpretation","absent_unbuilt",
            "Nothing (T0: blocked by probability absence)","Ensemble theory",False),
        X0Item("X10","frequency_interpretation","absent_unbuilt",
            "Nothing","Frequency-to-probability bridge",True),
        X0Item("X11","decoherence_candidate","extension_only",
            "Lindblad off-diagonal suppression (Q-D MBU)","Native decoherence",True),
        X0Item("X12","response_functional","constitutive_or_effective_only",
            "S_eff[Phi,Phi_tilde] (W-C nonnative packaging)","Physical wavefunction",True),
        X0Item("X13","norm_unitarity","extension_only",
            "Trace preservation in Lindblad (open-system)","Closed-system unitarity",True),
        X0Item("X14","hamiltonian_generator","extension_only",
            "H in Lindblad: -i[H,rho] (Q-C extension)","Native Hamiltonian",True),
        X0Item("X15","normalization_rule","extension_only",
            "Tr(rho)=1 in density-matrix formalism","Probabilistic normalization",True),
        X0Item("X16","interference_capable","extension_only",
            "Transient interference V(t)=exp(-R_dec t) (Q-F MBU)","Born-interpreted interference",True),
        X0Item("X17","qubit_extension","extension_only",
            "C^2 qubit with sigma_z,sigma_x,sigma_y (Q-II.D)","Native quantum system",True),
        X0Item("X18","exchange_statistical","extension_only",
            "Bosonic exchange with tau caveat (R-F MBU)","Full BE/FD statistics",True),
        X0Item("X19","o3_defect_measurement","extension_only",
            "Defect classification provides probe identity (R-B)","Measurement on defects",True),
        X0Item("X20","propagation_probabilistic","constitutive_or_effective_only",
            "Telegrapher propagation (W-B): modes can carry statistics","Probabilistic field theory",True),
        X0Item("X21","test_probe_regime","constitutive_or_effective_only",
            "Probe response F=-alpha grad(Phi) (W-D)","Probe measurement theory",True),
        X0Item("X22","classical_vs_intrinsic","absent_unbuilt",
            "Not distinguished: no probability to classify","Classical vs quantum probability",True),
        X0Item("X23","apparatus_coupling","absent_unbuilt",
            "Nothing","Measurement apparatus dynamics",True),
        X0Item("X24","pointer_readout","extension_only",
            "Pointer basis from Lindblad decoherence (Q-D)","Operational readout",True),
        X0Item("X25","new_axioms_needed","requires_new_postulates",
            "Born rule + measurement postulate identified as MIP candidates","Quantum completion",True),
    ]


def run_x0_probability_measurement_entry_inventory() -> X0ProbabilityEntryResult:
    items = _build_items()
    c = {cl: sum(1 for i in items if i.classification == cl) for cl in ALLOWED_CLS}
    diag: Dict[str, Any] = {"n_items": len(items),
        **{f"n_{k}": v for k, v in c.items()},
        "n_x_licensed": sum(1 for i in items if i.x_licensed),
        "born_rule_present": False, "measurement_postulate_present": False}
    result = X0ProbabilityEntryResult(
        True, items, len(items),
        c.get("present_native",0), c.get("present_but_limited",0),
        c.get("extension_only",0), c.get("constitutive_or_effective_only",0),
        c.get("absent_unbuilt",0), c.get("blocked_by_structure",0),
        c.get("requires_new_postulates",0),
        X0_NONCLAIMS, X0_INVENTORY, X0_QUANTUM, X0_POSTULATE, diag)
    _validate(result); return result


def _validate(r: X0ProbabilityEntryResult) -> None:
    if len(r.items) != N_ITEMS: raise ValueError(f"Expected {N_ITEMS}")
    for i in r.items:
        if i.classification not in ALLOWED_CLS: raise ValueError(f"{i.item_id}")
    if len(r.nonclaims) != N_X0_NONCLAIMS: raise ValueError("nc")
    total = r.n_native+r.n_limited+r.n_extension+r.n_constitutive+r.n_absent+r.n_blocked+r.n_postulate
    if total != r.n_items: raise ValueError(f"counts {total}!={r.n_items}")
    if r.diagnostics["born_rule_present"]: raise ValueError("born False")


def _self_test() -> bool:
    r = run_x0_probability_measurement_entry_inventory()
    assert r.valid and r.n_items == N_ITEMS
    assert r.inventory_verdict == X0_INVENTORY
    assert r.quantum_content_verdict == X0_QUANTUM
    assert r.postulate_verdict == X0_POSTULATE
    assert r.n_extension >= 12 and r.n_absent >= 6
    assert r.diagnostics["born_rule_present"] is False
    return True

if __name__ == "__main__":
    _self_test(); print("X0 passed.")
