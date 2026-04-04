"""
Appendix U0 --- Unified-Field Entry Inventory
===============================================
GRUT Unified-Field Program --- Phase U0

Inventories all field/action/geometry-relevant structures present in GRUT
after Appendices S and T. Appendix U begins with a confirmed dissipative
scalar field ontology and exact irreversible bookkeeping, but no licensed
action principle, gauge completion, thermal completion, or sector unification.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

ALLOWED_CLASSIFICATIONS = frozenset({
    "present_native", "present_but_limited", "extension_only",
    "emergent_candidate", "absent_unbuilt", "blocked_by_structure",
    "requires_new_postulates",
})

N_ITEMS: int = 25
N_U0_NONCLAIMS: int = 8

U0_INVENTORY_VERDICT: str = "inventory_complete_and_bounded"
U0_FIELD_CONTENT: str = "scalar_constitutive_core_present"
U0_ACTION_STATUS: str = "action_principle_absent_or_unestablished"
U0_GEOMETRY_STATUS: str = "effective_geometry_candidates_may_be_tested"
U0_AUTH: str = "authorized_to_proceed_to_UB"

U0_NONCLAIMS: List[str] = [
    "NOT_claiming_scalar_ODE_therefore_action_principle__"
    "constitutive_evolution_is_not_Euler_Lagrange_derivation",
    "NOT_claiming_dissipative_balance_therefore_Lagrangian__"
    "dV_dt_plus_D_eq_0_is_bookkeeping_not_variational_extremum",
    "NOT_claiming_O3_defect_therefore_gauge_field__"
    "topological_sigma_model_is_not_gauge_theory",
    "NOT_claiming_su2_algebra_therefore_gauge_symmetry__"
    "qubit_observable_algebra_is_internal_global_not_local_gauge",
    "NOT_claiming_tau_preferred_frame_therefore_metric_dynamics__"
    "preferred_timescale_is_not_spacetime_curvature",
    "NOT_claiming_propagation_lag_therefore_geometry__"
    "finite_response_time_is_not_metric_or_connection",
    "NOT_claiming_layered_sectors_therefore_unified_field__"
    "coexistence_is_not_unification",
    "NOT_claiming_field_inventory_therefore_field_theory_complete__"
    "inventory_documents_starting_point_not_completion",
]


@dataclass
class U0Item:
    item_id: str; item_name: str; classification: str
    what_established: str; what_absent: str; u_licensed: bool

@dataclass
class U0UnifiedFieldEntryResult:
    valid: bool; items: List[U0Item]; n_items: int
    n_native: int; n_limited: int; n_extension: int; n_emergent: int
    n_absent: int; n_blocked: int; n_postulate: int
    nonclaims: List[str]
    inventory_verdict: str; field_content_verdict: str
    action_status_verdict: str; geometry_status_verdict: str
    auth_verdict: str
    diagnostics: Dict[str, Any]


def _build_items() -> List[U0Item]:
    return [
        U0Item("U1","native_scalar_field","present_native",
            "Real scalar Phi with constitutive ODE","Quantum or relativistic field",True),
        U0Item("U2","tau_constitutive_structure","present_native",
            "tau^2=3/2; tau dPhi/dt + Phi = X","Temperature or thermal role for tau",True),
        U0Item("U3","first_order_dissipative_evolution","present_native",
            "First-order in time; dissipative; irreversible","Second-order / wave / Lorentz-covariant",True),
        U0Item("U4","memory_retardation_structure","present_but_limited",
            "tau introduces finite response lag; Galley CTP doubled vars in effective regime",
            "Full nonlocal kernel or memory functional",True),
        U0Item("U5","o3_extension_field","extension_only",
            "O(3) sigma model: S^2 target space (MIP)","Native derivation; gauge structure",True),
        U0Item("U6","topological_defect_sector","extension_only",
            "pi_2(S^2)=Z winding; defect classification","Dynamical stability without Skyrme",True),
        U0Item("U7","su2_observable_algebra","extension_only",
            "Toy su(2) on C^2 qubit (MBU)","Gauge field; spacetime symmetry",True),
        U0Item("U8","exchange_statistical_overlay","extension_only",
            "Bosonic exchange with tau caveat (MBU)","Full BE/FD statistics",True),
        U0Item("U9","gauge_fields","absent_unbuilt",
            "Nothing","Everything: no A_mu, F_mu_nu, covariant derivative",True),
        U0Item("U10","fermionic_field","blocked_by_structure",
            "3-layer obstruction; routes identified","Any fermionic field content",False),
        U0Item("U11","born_probability","blocked_by_structure",
            "Born rule absent; MIP route identified","Probability measure",False),
        U0Item("U12","chemistry_composite","blocked_by_structure",
            "All 6 bridge conditions unmet","Any chemistry/composite closure",False),
        U0Item("U13","action_principle","absent_unbuilt",
            "No action S[Phi] from which constitutive ODE follows variationally",
            "Euler-Lagrange derivation of tau dPhi/dt + Phi = X",True),
        U0Item("U14","variational_structure","emergent_candidate",
            "CTP/Galley doubled-variable action exists in effective regime",
            "True fundamental action; native variational principle",True),
        U0Item("U15","hamiltonian_structure","absent_unbuilt",
            "Nothing native (dissipative, not symplectic)",
            "Phase space, Poisson brackets, Hamilton's equations",True),
        U0Item("U16","lagrangian_density","absent_unbuilt",
            "No L(Phi, dPhi) from which ODE is derived",
            "L with Euler-Lagrange yielding constitutive law",True),
        U0Item("U17","effective_propagation","emergent_candidate",
            "Constitutive response has characteristic timescale tau; "
            "perturbations propagate diffusively not wave-like",
            "Wave propagation; light cone; causal structure",True),
        U0Item("U18","metric_like_structure","emergent_candidate",
            "Spatial isotropy + tau preferred frame suggest effective metric background",
            "Dynamical metric; Einstein equations; spacetime curvature",True),
        U0Item("U19","connection_curvature","absent_unbuilt",
            "Nothing","Connection, Christoffel, Riemann, Ricci",True),
        U0Item("U20","force_law_candidate","emergent_candidate",
            "Constitutive response + topological defect interaction could yield "
            "effective force law",
            "Derived force law; Newton/Coulomb analog",True),
        U0Item("U21","coupling_constants","present_but_limited",
            "tau (or gamma=1/tau) as canonical rate; barrier amplitude A",
            "Full set of coupling constants for field theory",True),
        U0Item("U22","unified_carrier","absent_unbuilt",
            "No common carrier across sectors (R, S^2, C^2, C^4)",
            "Shared state space for all sectors",True),
        U0Item("U23","common_master_equation","absent_unbuilt",
            "Constitutive ODE + Lindblad + H_hop coexist separately",
            "Single evolution equation for all sectors",True),
        U0Item("U24","effective_geometric_description","emergent_candidate",
            "Spatial isotropy + preferred frame = candidate for effective geometry",
            "Derived geometric dynamics",True),
        U0Item("U25","macroscopic_field_theory","emergent_candidate",
            "Constitutive field with dissipation, defects, observables: "
            "candidate for macroscopic effective field description",
            "Microscopic or fundamental field theory",True),
    ]


def run_u0_unified_field_entry_inventory() -> U0UnifiedFieldEntryResult:
    items = _build_items()
    c = {cl: sum(1 for i in items if i.classification == cl) for cl in ALLOWED_CLASSIFICATIONS}
    diag: Dict[str, Any] = {"n_items": len(items), **{f"n_{k}": v for k, v in c.items()},
        "n_u_licensed": sum(1 for i in items if i.u_licensed)}
    result = U0UnifiedFieldEntryResult(
        True, items, len(items),
        c.get("present_native",0), c.get("present_but_limited",0),
        c.get("extension_only",0), c.get("emergent_candidate",0),
        c.get("absent_unbuilt",0), c.get("blocked_by_structure",0),
        c.get("requires_new_postulates",0),
        U0_NONCLAIMS, U0_INVENTORY_VERDICT, U0_FIELD_CONTENT,
        U0_ACTION_STATUS, U0_GEOMETRY_STATUS, U0_AUTH, diag)
    _validate(result); return result


def _validate(r: U0UnifiedFieldEntryResult) -> None:
    if len(r.items) != N_ITEMS: raise ValueError(f"Expected {N_ITEMS}")
    for i in r.items:
        if i.classification not in ALLOWED_CLASSIFICATIONS: raise ValueError(f"{i.item_id}")
    if len(r.nonclaims) != N_U0_NONCLAIMS: raise ValueError("nonclaims")
    total = r.n_native+r.n_limited+r.n_extension+r.n_emergent+r.n_absent+r.n_blocked+r.n_postulate
    if total != r.n_items: raise ValueError(f"counts {total}!={r.n_items}")


def _self_test() -> bool:
    r = run_u0_unified_field_entry_inventory()
    assert r.valid and r.n_items == N_ITEMS
    assert r.inventory_verdict == U0_INVENTORY_VERDICT
    assert r.field_content_verdict == U0_FIELD_CONTENT
    assert r.action_status_verdict == U0_ACTION_STATUS
    assert r.n_native >= 3 and r.n_absent >= 6 and r.n_emergent >= 5
    return True

if __name__ == "__main__":
    _self_test(); print("U0 passed.")
