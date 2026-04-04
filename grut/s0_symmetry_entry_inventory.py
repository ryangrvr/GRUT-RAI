"""
Appendix S0 --- Symmetry Entry Inventory
=========================================
GRUT Symmetry Program --- Phase S0

Inventories all symmetry-relevant structures present in GRUT after
completion of Appendices A-R, classifying each by status and sector.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CAT_A: int = 4; N_CAT_B: int = 5; N_CAT_C: int = 4
N_CAT_D: int = 4; N_CAT_E: int = 6; N_TOTAL: int = 23
N_S0_NONCLAIMS: int = 8; N_HARD_RULES: int = 6
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

ALLOWED_STATES: frozenset = frozenset({
    "present", "absent", "blocked", "extension_ready", "effective_only",
})
ALLOWED_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})
ALLOWED_CATS: frozenset = frozenset({
    "A_native_scalar", "B_quantum_extension", "C_topological_extension",
    "D_blocked_absent", "E_sector_relations",
})

S0_VERDICT: str = "symmetry_entry_inventory_complete"

HARD_RULES: List[str] = [
    "prefer_blocked_over_aspirational",
    "prefer_extension_ready_over_ready_when_non_native",
    "preserve_fermionic_and_probability_boundaries",
    "do_not_treat_O3_as_native_scalar_canon",
    "do_not_treat_toy_algebra_as_full_symmetry_closure",
    "do_not_treat_exchange_results_as_statistics_closure",
]

S0_NONCLAIMS: List[str] = [
    "NOT_claiming_native_scalar_symmetries_therefore_gauge_theory__"
    "Z2_and_constitutive_invariance_are_not_gauge_structure",
    "NOT_claiming_extension_complex_structure_therefore_unitary_symmetry__"
    "J_postulation_is_MIP_not_native_U1_or_SU2",
    "NOT_claiming_O3_extension_therefore_native_target_space_symmetry__"
    "O3_is_MIP_not_derived_from_scalar_canon",
    "NOT_claiming_decoherence_basis_therefore_exact_symmetry__"
    "pointer_basis_selection_is_effective_not_exact_symmetry",
    "NOT_claiming_bosonic_exchange_therefore_full_statistics_symmetry__"
    "hard_core_exchange_is_not_Bose_Einstein_closure",
    "NOT_claiming_sector_comparison_therefore_unification__"
    "mapping_sectors_is_not_unifying_them",
    "NOT_claiming_blocked_fermionic_sector_softened__"
    "obstruction_unchanged_through_all_Q_and_R",
    "NOT_claiming_symmetry_inventory_therefore_Standard_Model__"
    "inventory_documents_current_state_not_particle_physics",
]

@dataclass
class S0Item:
    item_id: str; item_name: str; category: str; presence_state: str
    appendix_p_class: str; supporting_audit: str
    allowed_claim: str; forbidden_claim: str
    dependency_notes: List[str]; notes: List[str]

@dataclass
class S0CatSummary:
    category_label: str; n_items: int; item_ids: List[str]; description: str

@dataclass
class S0Readiness:
    all_documented: bool; ready_for_sb: bool; verdict: str; notes: List[str]

@dataclass
class S0SymmetryEntryResult:
    valid: bool; items: List[S0Item]; summaries: List[S0CatSummary]
    readiness: S0Readiness; n_total: int
    n_present: int; n_extension_ready: int; n_effective_only: int
    n_absent: int; n_blocked: int
    hard_rules: List[str]; nonclaims: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    inventory_verdict: str; diagnostics: Dict[str, Any]

def _cat_a() -> List[S0Item]:
    return [
        S0Item("A1","z2_phi_reflection","A_native_scalar","present","native_canon",
            "Appendix A/C","Z2 reflection Phi -> -Phi is native scalar symmetry",
            "Z2 reflection implies gauge symmetry",[],[]),
        S0Item("A2","constitutive_ode_invariance","A_native_scalar","present","native_canon",
            "Appendix A/C","Constitutive ODE form-invariance under parameter rescaling",
            "ODE invariance implies spacetime symmetry",[],[]),
        S0Item("A3","tau_scale_invariance","A_native_scalar","present","native_canon",
            "Appendix A","tau^2=3/2 as fixed canonical scale; scale selection not scale invariance",
            "tau scale implies continuous scale symmetry (it is fixed, not free)",[],[]),
        S0Item("A4","barrier_action_symmetry","A_native_scalar","present","native_canon",
            "Appendix B/C","Barrier action structure preserves constitutive form",
            "Barrier symmetry implies full action principle symmetry",[],[]),
    ]

def _cat_b() -> List[S0Item]:
    return [
        S0Item("B1","complex_structure_J","B_quantum_extension","extension_ready",
            "motivated_independent_postulation","Q-B.5",
            "J with J^2=-1: complex structure postulated (MIP)",
            "J derived from native scalar structure",[],[]),
        S0Item("B2","toy_su2_observable_algebra","B_quantum_extension","extension_ready",
            "motivated_but_unbuilt","Q-II.D",
            "su(2) toy algebra {sigma_z,sigma_x,sigma_y} at extension level",
            "su(2) is native GRUT observable algebra",[],[]),
        S0Item("B3","bosonic_exchange_symmetry","B_quantum_extension","extension_ready",
            "motivated_but_unbuilt","R-F",
            "Bosonic exchange with open-system tau caveat",
            "Exchange symmetry implies full BE statistics closure",[],[]),
        S0Item("B4","decoherence_basis_selection","B_quantum_extension","effective_only",
            "motivated_but_unbuilt","Q-D/Q-F",
            "Pointer-basis selection as effective symmetry-breaking (Phi_hat eigenstates preferred)",
            "Decoherence basis selection is exact symmetry",[],[]),
        S0Item("B5","interference_complementary_sector","B_quantum_extension","extension_ready",
            "motivated_but_unbuilt","Q-F",
            "Interference lives in sector complementary to constitutive observable",
            "Complementary sector implies full wave symmetry",[],[]),
    ]

def _cat_c() -> List[S0Item]:
    return [
        S0Item("C1","o3_target_space_symmetry","C_topological_extension","extension_ready",
            "motivated_independent_postulation","Appendix O",
            "O(3) sigma model: SO(3) target-space symmetry (MIP)",
            "O(3) is native GRUT symmetry",[],[]),
        S0Item("C2","topological_charge_pi2","C_topological_extension","extension_ready",
            "motivated_independent_postulation","Appendix O",
            "pi_2(S^2)=Z: integer winding-number conservation",
            "Topological charge implies particle number conservation",[],[]),
        S0Item("C3","skyrme_symmetry_inheritance","C_topological_extension","extension_ready",
            "motivated_but_unbuilt","Appendix N",
            "Skyrme L4 term preserves O(3) symmetry if added",
            "Skyrme symmetry is native or already built",[],[]),
        S0Item("C4","hopf_route_symmetry_relevance","C_topological_extension","absent",
            "compatible_but_ad_hoc","R-E",
            "Hopf fibration (SU(2)->S^2) would provide spinorial symmetry if built",
            "Hopf route available without new postulation",[],[]),
    ]

def _cat_d() -> List[S0Item]:
    return [
        S0Item("D1","fermionic_spinorial_symmetry","D_blocked_absent","blocked",
            "bounded_structural_result","Q0/R-E",
            "Fermionic/spinorial symmetry blocked by 3-layer obstruction",
            "Fermionic symmetry accessible without new structure",[],[]),
        S0Item("D2","statistics_symmetrization_closure","D_blocked_absent","absent",
            "compatible_but_ad_hoc","R-F",
            "Full BE/FD symmetrization absent (only hard-core exchange demonstrated)",
            "Statistics closure available from exchange results",[],[]),
        S0Item("D3","gauge_like_structure","D_blocked_absent","absent",
            "compatible_but_ad_hoc","None",
            "No gauge-like structure in current GRUT architecture",
            "Native gauge structure present",[],[]),
        S0Item("D4","chemistry_relevant_symmetry","D_blocked_absent","blocked",
            "bounded_structural_result","R-G",
            "Chemistry-relevant symmetry (shell filling, periodic table) blocked",
            "Chemistry symmetry accessible without fermions+binding",[],[]),
    ]

def _cat_e() -> List[S0Item]:
    return [
        S0Item("E1","scalar_to_o3_relation","E_sector_relations","extension_ready",
            "motivated_independent_postulation","Appendix O",
            "Scalar canon -> O(3) extension: MIP postulation required",
            "O(3) derived from scalar sector",[],[]),
        S0Item("E2","constitutive_to_complementary","E_sector_relations","extension_ready",
            "motivated_but_unbuilt","Q-F/Q-II.D",
            "Constitutive Phi_hat sector vs complementary (sigma_x) sector",
            "Sectors are unified",[],[]),
        S0Item("E3","bosonic_to_fermionic_boundary","E_sector_relations","blocked",
            "bounded_structural_result","R-E",
            "Bosonic route available; fermionic route blocked by 3-layer obstruction",
            "Bosonic results imply fermionic accessibility",[],[]),
        S0Item("E4","decoherence_to_interference","E_sector_relations","effective_only",
            "motivated_but_unbuilt","Q-F",
            "Decoherence-selected sector vs transient interference sector",
            "Sectors unified or interference is permanent",[],[]),
        S0Item("E5","excitation_to_matter","E_sector_relations","extension_ready",
            "motivated_but_unbuilt","Q-II.E/R-B",
            "Many-mode excitations -> matter scaffold (extension chain)",
            "Excitation grammar implies matter closure",[],[]),
        S0Item("E6","quantum_to_matter_classes","E_sector_relations","extension_ready",
            "bounded_structural_result","Q-II.G",
            "Quantum MBU/MIP floor inherited into matter R program",
            "Quantum classes promote in matter context",[],[]),
    ]

def run_s0_symmetry_entry_inventory() -> S0SymmetryEntryResult:
    cats = {"A":_cat_a(),"B":_cat_b(),"C":_cat_c(),"D":_cat_d(),"E":_cat_e()}
    all_items = []
    for v in cats.values():
        all_items.extend(v)
    summaries = [
        S0CatSummary("A_native_scalar",N_CAT_A,[i.item_id for i in cats["A"]],"Native scalar/constitutive symmetries"),
        S0CatSummary("B_quantum_extension",N_CAT_B,[i.item_id for i in cats["B"]],"Quantum-extension symmetries"),
        S0CatSummary("C_topological_extension",N_CAT_C,[i.item_id for i in cats["C"]],"Topological/extension symmetries"),
        S0CatSummary("D_blocked_absent",N_CAT_D,[i.item_id for i in cats["D"]],"Blocked/absent symmetry structures"),
        S0CatSummary("E_sector_relations",N_CAT_E,[i.item_id for i in cats["E"]],"Sector relation inventory"),
    ]
    c = {s:sum(1 for i in all_items if i.presence_state==s) for s in ALLOWED_STATES}
    readiness = S0Readiness(True,True,"ready_to_proceed_to_sa_and_sb",
        [f"All {N_TOTAL} items documented","Fermionic/probability boundaries preserved"])
    allowed = [
        f"All {N_TOTAL} symmetry-relevant items inventoried across 5 categories",
        "4 native scalar symmetries documented (Z2, ODE invariance, tau scale, barrier)",
        "5 quantum-extension symmetries at extension level (J, su(2), exchange, decoherence, interference)",
        "4 topological-extension symmetries (O(3), pi_2, Skyrme, Hopf route absent)",
        "4 blocked/absent items (fermionic, statistics closure, gauge, chemistry symmetry)",
        "6 sector relations mapped (scalar-O3, constitutive-complementary, bosonic-fermionic, etc.)",
        "S-A and S-B authorized to proceed",
    ]
    forbidden = [
        "Native scalar symmetries imply gauge theory",
        "Extension complex structure implies unitary symmetry group",
        "O(3) extension implies native target-space symmetry",
        "Decoherence basis implies exact symmetry",
        "Bosonic exchange implies statistics symmetry closure",
        "Sector comparison implies unification",
        "Symmetry inventory implies Standard Model",
    ]
    diag: Dict[str,Any] = {"n_total":len(all_items),"n_cats":5,
        "n_present":c.get("present",0),"n_extension_ready":c.get("extension_ready",0),
        "n_effective_only":c.get("effective_only",0),"n_absent":c.get("absent",0),
        "n_blocked":c.get("blocked",0),"n_nonclaims":N_S0_NONCLAIMS}
    result = S0SymmetryEntryResult(
        valid=True,items=all_items,summaries=summaries,readiness=readiness,
        n_total=len(all_items),n_present=c.get("present",0),
        n_extension_ready=c.get("extension_ready",0),n_effective_only=c.get("effective_only",0),
        n_absent=c.get("absent",0),n_blocked=c.get("blocked",0),
        hard_rules=HARD_RULES,nonclaims=S0_NONCLAIMS,
        allowed_claims=allowed,forbidden_claims=forbidden,
        inventory_verdict=S0_VERDICT,diagnostics=diag)
    _validate(result)
    return result

def _validate(r: S0SymmetryEntryResult) -> None:
    if len(r.items)!=N_TOTAL: raise ValueError(f"Expected {N_TOTAL}")
    for i in r.items:
        if i.presence_state not in ALLOWED_STATES: raise ValueError(f"{i.item_id} state")
        if i.appendix_p_class not in ALLOWED_P_CLASSES: raise ValueError(f"{i.item_id} class")
        if i.category not in ALLOWED_CATS: raise ValueError(f"{i.item_id} cat")
    if len(r.nonclaims)!=N_S0_NONCLAIMS: raise ValueError("nonclaims")
    if len(r.hard_rules)!=N_HARD_RULES: raise ValueError("rules")
    if len(r.allowed_claims)!=N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN: raise ValueError("forbidden")
    if not r.readiness.ready_for_sb: raise ValueError("readiness")
    ids=[i.item_id for i in r.items]
    if len(ids)!=len(set(ids)): raise ValueError("dup ids")

def _self_test() -> bool:
    r=run_s0_symmetry_entry_inventory()
    assert r.valid and r.n_total==N_TOTAL and r.inventory_verdict==S0_VERDICT
    return True

if __name__=="__main__":
    _self_test(); print("S0 passed.")
