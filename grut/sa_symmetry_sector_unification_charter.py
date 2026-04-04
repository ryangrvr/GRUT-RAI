"""
Appendix S-A --- Symmetry and Sector-Unification Charter
=========================================================
GRUT Symmetry Program --- Phase S-A
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "S0_symmetry_entry_inventory",
    "S-A_symmetry_and_sector_unification_charter",
    "S-B_native_symmetries_and_exact_invariants",
    "S-C_extension_level_and_emergent_symmetries",
    "S-D_sector_breaking_and_incompatibility_map",
    "S-E_unified_sector_ledger_and_handoff_to_T",
]
N_STAGES: int = 6

ALLOWED_SUCCESS: frozenset = frozenset({
    "success","partial_success","bounded_negative_result","extension_level_outcome",
})
RULE_IDS: List[str] = ["S-R1","S-R2","S-R3","S-R4","S-R5","S-R6","S-R7"]
N_RULES: int = 7
FFM_NAMES: List[str] = [
    "extension_sector_as_native_symmetry",
    "o3_as_scalar_canon",
    "interference_sector_as_full_wave_symmetry",
    "bosonic_route_as_universal_matter_symmetry",
    "route_inventory_as_unification",
    "blocked_fermionic_sector_as_softened_by_analogy",
    "effective_basis_selection_as_exact_symmetry",
    "symmetry_map_as_standard_model_closure",
]
N_FFMS: int = 8
N_SA_NONCLAIMS: int = 8

SA_NONCLAIMS: List[str] = [
    "NOT_claiming_symmetry_program_will_derive_gauge_theory__"
    "S_maps_existing_symmetries_not_derives_new_ones",
    "NOT_claiming_charter_constitutes_symmetry_derivation__"
    "charter_defines_grammar_not_results",
    "NOT_claiming_stage_success_guaranteed__"
    "each_stage_may_yield_BSR",
    "NOT_claiming_O3_is_native_symmetry__"
    "O3_is_MIP_extension_not_scalar_canon",
    "NOT_claiming_sector_comparison_is_unification__"
    "mapping_relations_is_not_unifying_sectors",
    "NOT_claiming_quantum_Q_classes_promoted_by_S_context__"
    "Q_and_R_Appendix_P_classes_locked",
    "NOT_claiming_fermionic_obstruction_dissolved_by_symmetry_analysis__"
    "3_layer_block_unchanged",
    "NOT_claiming_authorization_implies_symmetry_closure__"
    "authorization_means_ready_not_solved",
]

ALLOWED_CHARTER_VERDICTS: frozenset = frozenset({
    "symmetry_program_authorized_and_staged",
    "symmetry_program_blocked__prerequisites_not_met",
})
CHARTER_VERDICT: str = "symmetry_program_authorized_and_staged"
ALLOWED_P_CLASSES: frozenset = frozenset({
    "native_canon","effective_reduction","bounded_structural_result",
    "working_canon_hypothesis","motivated_but_unbuilt",
    "motivated_independent_postulation","compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

@dataclass
class SAProgramObjective:
    statement: str; scope: str; not_in_scope: List[str]
    preconditions: List[str]; preconditions_met: bool

@dataclass
class SAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; success_criterion_type: str
    success_description: str; appendix_p_expected: str
    depends_on: List[str]; notes: List[str]

@dataclass
class SASuccessCriteria:
    success: str; partial: str; bsr: str; extension: str

@dataclass
class SARule:
    rule_id: str; statement: str; violation: str; tests_for: str; notes: List[str]

@dataclass
class SAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str
    related: str; notes: List[str]

@dataclass
class SANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class SACharter:
    valid: bool; objective: SAProgramObjective
    stage_sequence: List[SAStageDef]; success_criteria: SASuccessCriteria
    rules: List[SARule]; ffms: List[SAFFM]
    entry_nonclaims: SANonclaims; s0_linked: bool
    charter_verdict: str; diagnostics: Dict[str,Any]

def _obj() -> SAProgramObjective:
    return SAProgramObjective(
        "Appendix S maps all symmetry-relevant structures in GRUT, classifies "
        "exact vs effective vs extension-level symmetries, maps sector transitions, "
        "and determines what unification claims are justified before thermodynamics "
        "and effective action appendices.",
        "Four investigative stages (S-B through S-E) governed by Appendix P discipline.",
        ["Deriving gauge theory","Deriving Standard Model","Deriving full symmetry breaking",
         "Promoting extension sectors to native canon","Reopening Q/R audits",
         "Treating sector comparison as unification"],
        ["Q Part I/II complete","R program complete as pre-chemistry ledger",
         "S0 inventory complete","Appendix P taxonomy operational"],
        True)

def _stages() -> List[SAStageDef]:
    return [
        SAStageDef("S0","Symmetry entry inventory",0,
            "What symmetry structures exist after A-R?","success",
            "All items inventoried","bounded_structural_result",["R-G_closure"],[]),
        SAStageDef("S-A","Symmetry charter",1,
            "What governs symmetry work?","success",
            "Charter staged","bounded_structural_result",["S0"],[]),
        SAStageDef("S-B","Native symmetries and exact invariants",2,
            "What exact symmetries does native GRUT possess?","extension_level_outcome",
            "Native symmetries classified","native_canon",["S-A"],
            ["First substantive stage; may find native_canon results"]),
        SAStageDef("S-C","Extension-level and emergent symmetries",3,
            "What symmetries emerge from extensions (Q,O(3),etc)?","extension_level_outcome",
            "Extension symmetries classified","motivated_but_unbuilt",["S-B"],
            ["Builds on S-B native results"]),
        SAStageDef("S-D","Sector breaking and incompatibility map",4,
            "Where do sectors break symmetry or become incompatible?","extension_level_outcome",
            "Breaking/incompatibility mapped","bounded_structural_result",["S-B","S-C"],
            ["Critical for understanding what CANNOT unify"]),
        SAStageDef("S-E","Unified sector ledger and handoff to T",5,
            "What is the final symmetry ledger for Appendix T?","extension_level_outcome",
            "Sector ledger produced; T entry conditions","bounded_structural_result",
            ["S-B","S-C","S-D"],["Final S stage; produces handoff to T"]),
    ]

def _criteria() -> SASuccessCriteria:
    return SASuccessCriteria(
        "Symmetry structure demonstrated within Appendix P discipline.",
        "Some symmetry sub-structures established, others underdetermined.",
        "Symmetry proved absent/broken (valid BSR outcome).",
        "Requires extension postulation (MIP/MBU).")

def _rules() -> List[SARule]:
    return [
        SARule("S-R1","Every symmetry claim carries Appendix P class.",
            "undisciplined_claim","classification",[]),
        SARule("S-R2","No native_canon unless derived from GRUT first principles.",
            "usefulness_as_nativity","nativity",[]),
        SARule("S-R3","New structure requires MIP minimum.",
            "unbuilt_as_solved","DOF accounting",[]),
        SARule("S-R4","Bounded negatives preserved as BSR.",
            "obstruction_demotion","obstruction preservation",[]),
        SARule("S-R5","Effective_reduction must state regime.",
            "regime_as_universal","regime qualification",[]),
        SARule("S-R6","Q and R Appendix P classes LOCKED in S.",
            "retroactive_promotion","class immutability",[]),
        SARule("S-R7","Extension sectors do not automatically inherit native symmetry status.",
            "extension_as_native_symmetry","extension discipline",[]),
    ]

def _ffms() -> List[SAFFM]:
    return [
        SAFFM("FFM-S.1","extension_sector_as_native_symmetry",
            "Treating extension-level sector as native symmetry.",
            "Extension sectors (O(3), J, tensor product) are postulated, not native.",
            "Q-B.5,O,Q-II.B",[]),
        SAFFM("FFM-S.2","o3_as_scalar_canon",
            "Treating O(3) target-space symmetry as native scalar canon.",
            "O(3) is MIP; scalar GRUT is real scalar field, not sigma model.",
            "Appendix O",[]),
        SAFFM("FFM-S.3","interference_sector_as_full_wave_symmetry",
            "Treating transient interference as full wave symmetry.",
            "Interference is transient (Q-F); not a permanent symmetry.",
            "Q-F",[]),
        SAFFM("FFM-S.4","bosonic_route_as_universal_matter_symmetry",
            "Treating bosonic exchange as universal matter symmetry.",
            "Fermionic route blocked; bosonic exchange is partial, not universal.",
            "R-E,R-F",[]),
        SAFFM("FFM-S.5","route_inventory_as_unification",
            "Treating identification of routes as sector unification.",
            "Routes are maps, not bridges.",
            "R-E",[]),
        SAFFM("FFM-S.6","blocked_fermionic_sector_as_softened_by_analogy",
            "Claiming fermionic obstruction softened by symmetry analogy.",
            "3-layer obstruction requires new topology, not analogy.",
            "Q0,R-E",[]),
        SAFFM("FFM-S.7","effective_basis_selection_as_exact_symmetry",
            "Treating decoherence basis selection as exact symmetry.",
            "Pointer basis is effective (regime-dependent), not exact.",
            "Q-D",[]),
        SAFFM("FFM-S.8","symmetry_map_as_standard_model_closure",
            "Treating GRUT symmetry map as Standard Model derivation.",
            "GRUT has no gauge fields, no SM gauge group, no Higgs mechanism.",
            "None",[]),
    ]

def _nonclaims() -> SANonclaims:
    return SANonclaims(SA_NONCLAIMS,N_SA_NONCLAIMS,True)

def run_sa_symmetry_sector_unification_charter() -> SACharter:
    obj=_obj(); stg=_stages(); crit=_criteria()
    rul=_rules(); ffm=_ffms(); nc=_nonclaims()
    diag: Dict[str,Any] = {"n_stages":N_STAGES,"n_rules":N_RULES,
        "n_ffms":N_FFMS,"n_nonclaims":N_SA_NONCLAIMS,
        "preconditions_met":obj.preconditions_met,
        "first_substantive":"S-B","final_stage":"S-E"}
    r = SACharter(True,obj,stg,crit,rul,ffm,nc,True,CHARTER_VERDICT,diag)
    _validate_sa(r); return r

def _validate_sa(r: SACharter) -> None:
    if len(r.stage_sequence)!=N_STAGES: raise ValueError("stages")
    for i,s in enumerate(r.stage_sequence):
        if s.stage_index!=i: raise ValueError(f"stage {s.stage_id} index")
    if len(r.rules)!=N_RULES: raise ValueError("rules")
    if len(r.ffms)!=N_FFMS: raise ValueError("ffms")
    names=[f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names: raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims!=N_SA_NONCLAIMS: raise ValueError("nonclaims")
    if not r.entry_nonclaims.all_registered: raise ValueError("registered")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS: raise ValueError("verdict")
    if not r.objective.preconditions_met: raise ValueError("preconditions")
    if not r.s0_linked: raise ValueError("s0 link")

def _self_test() -> bool:
    r=run_sa_symmetry_sector_unification_charter()
    assert r.valid and r.charter_verdict==CHARTER_VERDICT
    return True

if __name__=="__main__":
    _self_test(); print("S-A passed.")
