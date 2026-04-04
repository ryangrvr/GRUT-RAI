"""
Appendix Y0 --- Quantum-Dynamical Closure and Sector-Interface Entry Inventory
================================================================================
GRUT Quantum-Dynamical Closure Program --- Phase Y0

Inventories all quantum-dynamical and sector-interface structures.
Book II LOCKED. Book III extensions are postulates. Appendix X closed
with operational probability layer but no quantum dynamics.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

ALLOWED_CLS = frozenset({
    "present_native","extension_established","operationally_supported_only",
    "constitutive_or_effective_only","absent_unbuilt",
    "blocked_by_structure","requires_new_postulates",
})

N_ITEMS: int = 30
N_Y0_NONCLAIMS: int = 8

Y0_INVENTORY: str = "quantum_dynamical_inventory_complete_and_bounded"
Y0_QUANTUM: str = "operational_probability_layer_present_but_dynamics_absent"
Y0_INTERFACE: str = "sector_interface_requirements_identified_but_unbuilt"

Y0_NONCLAIMS: List[str] = [
    "NOT_claiming_probability_layer_therefore_quantum_dynamics__"
    "Born_plus_outcome_does_not_imply_state_evolution_law",
    "NOT_claiming_Lindblad_extension_therefore_unitarity__"
    "open_system_evolution_is_not_unitary_dynamics",
    "NOT_claiming_propagation_therefore_quantum_field_theory__"
    "telegrapher_extension_is_not_QFT",
    "NOT_claiming_interface_requirements_therefore_integration__"
    "documenting_requirements_is_not_satisfying_them",
    "NOT_claiming_compatibility_therefore_sector_closure__"
    "compatible_sectors_may_still_be_disjoint",
    "NOT_claiming_response_functional_therefore_quantum_dynamics__"
    "auxiliary_packaging_is_not_physical_evolution",
    "NOT_claiming_dissipative_arrow_therefore_decoherence_mechanism__"
    "native_irreversibility_is_not_basis_selection",
    "NOT_claiming_inventory_therefore_quantum_completion__"
    "mapping_gaps_is_not_filling_them",
]


@dataclass
class Y0Item:
    item_id: str; item_name: str; classification: str
    what_established: str; what_absent: str; y_licensed: bool

@dataclass
class Y0QuantumDynamicalEntryResult:
    valid: bool; items: List[Y0Item]; n_items: int
    n_native: int; n_ext_est: int; n_operational: int; n_constitutive: int
    n_absent: int; n_blocked: int; n_postulate: int
    nonclaims: List[str]
    inventory_verdict: str; quantum_status_verdict: str; interface_verdict: str
    diagnostics: Dict[str, Any]


def _build_items() -> List[Y0Item]:
    return [
        Y0Item("Y1","state_representation","extension_established",
            "rho on C^2 (density matrix, Q-II.B)","Native quantum state",True),
        Y0Item("Y2","between_measurement_evolution","absent_unbuilt",
            "Nothing (unitarity absent, X-D)","State evolution law",True),
        Y0Item("Y3","unitary_generator","absent_unbuilt",
            "Nothing (no native H generating unitary)","Unitary U(t)",True),
        Y0Item("Y4","nonunitary_generator","extension_established",
            "Lindblad: drho/dt=-i[H,rho]+dissipator (Q-C extension)","Native nonunitary law",True),
        Y0Item("Y5","born_compatibility","extension_established",
            "Born map p(i)=Tr(rho Pi_i) (X-B)","Frequency derivation",True),
        Y0Item("Y6","update_compatibility","extension_established",
            "Epistemic update rho->Pi_i rho Pi_i/p(i) (X-C)","Collapse ontology",True),
        Y0Item("Y7","repeated_measurement_closure","operationally_supported_only",
            "Consistent via update rule (X-C)","Physical measurement model",True),
        Y0Item("Y8","apparatus_coupling","absent_unbuilt",
            "Nothing","Apparatus/detector model",True),
        Y0Item("Y9","decoherence_mechanism","constitutive_or_effective_only",
            "Lindblad off-diagonal suppression (Q-D extension)","Native mechanism",True),
        Y0Item("Y10","collapse_ontology","absent_unbuilt",
            "Nothing (update is epistemic)","Collapse mechanism",True),
        Y0Item("Y11","quantum_state_ontology","absent_unbuilt",
            "Nothing (rho is bookkeeping)","Ontology of psi/rho",True),
        Y0Item("Y12","response_functional_relevance","constitutive_or_effective_only",
            "S_eff[Phi,Phi_tilde] (W-C packaging)","Physical quantum dynamics",True),
        Y0Item("Y13","propagation_relevance","extension_established",
            "Telegrapher with speed v (W-B)","Native propagation",True),
        Y0Item("Y14","action_core_relevance","extension_established",
            "Undamped hyperbolic action (W-C)","Full damped action",True),
        Y0Item("Y15","damped_sector_nonunitary","constitutive_or_effective_only",
            "tau1 dPhi/dt term as dissipation (W-B)","Native nonunitary",True),
        Y0Item("Y16","time_ordering","absent_unbuilt",
            "Nothing","Time-ordered dynamics",True),
        Y0Item("Y17","normalization_preservation","extension_established",
            "Tr(rho)=1 preserved by Lindblad (Q-C)","Unitary norm preservation",True),
        Y0Item("Y18","sequential_measurement","operationally_supported_only",
            "Via iterated update (X-C)","Physical sequential measurement",True),
        Y0Item("Y19","multi_sector_integration","absent_unbuilt",
            "Nothing","Integration rule for sectors",True),
        Y0Item("Y20","gauge_integration","absent_unbuilt",
            "Nothing (gauge absent)","Gauge sector coupling",True),
        Y0Item("Y21","fermionic_integration","blocked_by_structure",
            "3-layer obstruction","Fermionic quantum integration",False),
        Y0Item("Y22","chemistry_integration","blocked_by_structure",
            "All bridge conditions unmet","Chemistry quantum integration",False),
        Y0Item("Y23","cosmology_integration","absent_unbuilt",
            "Nothing","Cosmological quantum dynamics",True),
        Y0Item("Y24","backreaction_interface","absent_unbuilt",
            "Test-probe only (W-D)","Self-consistent back-reaction",True),
        Y0Item("Y25","integrated_vs_attached","absent_unbuilt",
            "Nothing","Criterion for sector integration",True),
        Y0Item("Y26","completion_vs_operational","operationally_supported_only",
            "Operational layer only (X-D)","Full quantum completion",True),
        Y0Item("Y27","unitarity_axiom_need","requires_new_postulates",
            "Unitarity absent; would require new axiom","Unitarity",True),
        Y0Item("Y28","apparatus_axiom_need","requires_new_postulates",
            "Apparatus absent; would require new axiom","Apparatus theory",True),
        Y0Item("Y29","decoherence_axiom_need","requires_new_postulates",
            "Decoherence mechanism absent natively","Decoherence",True),
        Y0Item("Y30","integration_axiom_need","requires_new_postulates",
            "Sector integration rules absent","Integration criteria",True),
    ]


def run_y0_quantum_dynamical_closure_entry_inventory() -> Y0QuantumDynamicalEntryResult:
    items = _build_items()
    c = {cl: sum(1 for i in items if i.classification == cl) for cl in ALLOWED_CLS}
    diag: Dict[str, Any] = {"n_items": len(items),
        **{f"n_{k}": v for k, v in c.items()},
        "n_y_licensed": sum(1 for i in items if i.y_licensed),
        "unitarity_present": False, "apparatus_present": False,
        "between_measurement_evolution": False, "sector_integration": False}
    result = Y0QuantumDynamicalEntryResult(
        True, items, len(items),
        c.get("present_native",0), c.get("extension_established",0),
        c.get("operationally_supported_only",0), c.get("constitutive_or_effective_only",0),
        c.get("absent_unbuilt",0), c.get("blocked_by_structure",0),
        c.get("requires_new_postulates",0),
        Y0_NONCLAIMS, Y0_INVENTORY, Y0_QUANTUM, Y0_INTERFACE, diag)
    _validate(result); return result


def _validate(r: Y0QuantumDynamicalEntryResult) -> None:
    if len(r.items) != N_ITEMS: raise ValueError(f"Expected {N_ITEMS}")
    for i in r.items:
        if i.classification not in ALLOWED_CLS: raise ValueError(f"{i.item_id}")
    if len(r.nonclaims) != N_Y0_NONCLAIMS: raise ValueError("nc")
    total = r.n_native+r.n_ext_est+r.n_operational+r.n_constitutive+r.n_absent+r.n_blocked+r.n_postulate
    if total != r.n_items: raise ValueError(f"counts {total}!={r.n_items}")
    if r.diagnostics["unitarity_present"]: raise ValueError("unit False")
    if r.diagnostics["between_measurement_evolution"]: raise ValueError("evol False")


def _self_test() -> bool:
    r = run_y0_quantum_dynamical_closure_entry_inventory()
    assert r.valid and r.n_items == N_ITEMS
    assert r.inventory_verdict == Y0_INVENTORY
    assert r.quantum_status_verdict == Y0_QUANTUM
    assert r.interface_verdict == Y0_INTERFACE
    assert r.n_absent >= 9 and r.n_ext_est >= 7
    assert r.diagnostics["unitarity_present"] is False
    return True

if __name__ == "__main__":
    _self_test(); print("Y0 passed.")
