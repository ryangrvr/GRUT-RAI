"""
Appendix Z-A --- Final Sovereign Ledger Charter
=================================================
GRUT Capstone Program --- Phase Z-A

Defines the rules, distinctions, forbidden failure modes, and stage
sequence for the capstone Z ledger. No new physics. Pure discipline
and closure governance.

=== 12 MANDATORY DISTINCTIONS ===

MD1.  inventory vs. physics: cataloguing structures != proving theorems
MD2.  architecture vs. completion: many appendices != solved physics
MD3.  native vs. extension: Book II immutable core != postulated overlay
MD4.  operational sufficiency vs. ontological completion
MD5.  attachment vs. integration: one-way link != shared dynamics
MD6.  absence vs. impossibility: unbuilt != permanently blocked
MD7.  blocked-by-structure vs. impossible-in-principle
MD8.  scaffolding vs. building: criteria/rules != sectors/closure
MD9.  discipline vs. discovery: honest ledger != theory of everything
MD10. closure vs. truth: program ends != physics settled
MD11. extension stack vs. native canon: 7 postulated != 0 derived
MD12. explicit gap vs. failure: documenting what's missing != failing

=== CAPSTONE STAGE SEQUENCE ===

Z0: Total Program Entry Inventory (32 items, 8 classifications)
Z-A: Final Sovereign Ledger Charter (this stage)
Z-B: Cumulative Postulate and Parameter Accounting
Z-C: Final Sector Status and Gap Classification
Z-D: Program Boundary and Future Scope
Z-E: Final Sovereign Closure Ledger

=== RULES ===

ZR1: Every entry carries Appendix P classification
ZR2: Native and extension layers remain cleanly separated
ZR3: All 12 mandatory distinctions maintained throughout Z
ZR4: Absent and blocked sectors documented, not hidden
ZR5: No retroactive promotion of extension to native
ZR6: Cumulative counts match Z0 inventory exactly
ZR7: Final ledger is honest accounting, not claim of completeness
ZR8: Program closure is structural, not epistemic

=== 8 FORBIDDEN FAILURE MODES ===

FFM-Z.1: inventory_as_physics --- cataloguing != proving
FFM-Z.2: architecture_as_completion --- many stages != solved
FFM-Z.3: extension_as_native --- 7 postulates != 0 derived
FFM-Z.4: absence_as_failure --- unbuilt != disproved
FFM-Z.5: closure_as_truth --- program ends != physics settled
FFM-Z.6: scaffolding_as_building --- rules != sectors
FFM-Z.7: attachment_as_integration --- one-way != shared dynamics
FFM-Z.8: discipline_as_discovery --- ledger != ToE
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

STAGES: List[str] = [
    "Z0_total_program_entry_inventory",
    "Z-A_final_sovereign_ledger_charter",
    "Z-B_cumulative_postulate_parameter_accounting",
    "Z-C_final_sector_status_gap_classification",
    "Z-D_program_boundary_and_future_scope",
    "Z-E_final_sovereign_closure_ledger",
]
N_STAGES: int = 6
N_DISTINCTIONS: int = 12
N_RULES: int = 8
N_FFMS: int = 8
N_ZA_NONCLAIMS: int = 8
N_ALLOWED: int = 7
N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "inventory_as_physics",
    "architecture_as_completion",
    "extension_as_native",
    "absence_as_failure",
    "closure_as_truth",
    "scaffolding_as_building",
    "attachment_as_integration",
    "discipline_as_discovery",
]

ZA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_therefore_physics__"
    "charter_defines_rules_not_reality",
    "NOT_claiming_inventory_therefore_complete__"
    "cataloguing_is_not_proving",
    "NOT_claiming_capstone_therefore_ToE__"
    "closure_ledger_is_honest_accounting",
    "NOT_claiming_architecture_therefore_settled__"
    "many_appendices_is_not_solved_physics",
    "NOT_claiming_absent_therefore_impossible__"
    "unbuilt_is_current_state_not_permanent",
    "NOT_claiming_extension_stack_therefore_native__"
    "7_postulated_axioms_are_not_derived",
    "NOT_claiming_closure_therefore_truth__"
    "program_ending_is_not_physics_ending",
    "NOT_claiming_discipline_therefore_discovery__"
    "honest_ledger_is_not_theory_of_everything",
]

CHARTER_VERDICT: str = "sovereign_ledger_charter_defined_with_strict_closure_firewall"
AUTH_VERDICT: str = "authorized_to_proceed_to_ZB"
OVERALL_P: str = "capstone_program_opened_under_strict_closure_discipline"
ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})
ALLOWED_AUTH_VERDICTS = frozenset({AUTH_VERDICT, "stop_for_missing_charter_boundary"})
ALLOWED_OVERALL_VERDICTS = frozenset({
    "capstone_program_opened_under_strict_closure_discipline",
    "capstone_program_opened_with_partial_charter",
    "capstone_charter_not_yet_stable",
})


@dataclass
class ZADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class ZAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; notes: List[str]

@dataclass
class ZARule:
    rule_id: str; statement: str; violation: str

@dataclass
class ZAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class ZANonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class ZASovereignLedgerCharterResult:
    valid: bool
    distinctions: List[ZADistinction]
    stage_sequence: List[ZAStageDef]
    rules: List[ZARule]
    ffms: List[ZAFFM]
    nonclaim_firewall: ZANonclaimFirewall
    charter_verdict: str; authorization_verdict: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[ZADistinction]:
    return [
        ZADistinction("MD1","inventory","physics",
            "Cataloguing structures is not proving theorems"),
        ZADistinction("MD2","architecture","completion",
            "Many appendices is not solved physics"),
        ZADistinction("MD3","native","extension",
            "Book II immutable core is not postulated overlay"),
        ZADistinction("MD4","operational_sufficiency","ontological_completion",
            "Works in practice is not settled in theory"),
        ZADistinction("MD5","attachment","integration",
            "One-way postulate link is not shared dynamics"),
        ZADistinction("MD6","absence","impossibility",
            "Unbuilt sector is not permanently blocked sector"),
        ZADistinction("MD7","blocked_by_structure","impossible_in_principle",
            "Current obstruction is not proof of impossibility"),
        ZADistinction("MD8","scaffolding","building",
            "Criteria and rules are not sectors and closure"),
        ZADistinction("MD9","discipline","discovery",
            "Honest ledger is not theory of everything"),
        ZADistinction("MD10","closure","truth",
            "Program ending is not physics settled"),
        ZADistinction("MD11","extension_stack","native_canon",
            "7 postulated axioms are not 0 derived axioms"),
        ZADistinction("MD12","explicit_gap","failure",
            "Documenting what is missing is not failing"),
    ]


def _stages() -> List[ZAStageDef]:
    return [
        ZAStageDef("Z0","Total Program Entry Inventory",0,
            "What structures exist across the entire GRUT program?",[]),
        ZAStageDef("Z-A","Final Sovereign Ledger Charter",1,
            "What rules govern capstone closure?",
            ["This stage: distinctions, rules, FFMs"]),
        ZAStageDef("Z-B","Cumulative Postulate and Parameter Accounting",2,
            "Exact count of all postulates, parameters, and fields?",
            ["7 extensions, 3 parameters, 0 new fields"]),
        ZAStageDef("Z-C","Final Sector Status and Gap Classification",3,
            "What is established, absent, and blocked?",
            ["Per-sector ledger with Appendix P classification"]),
        ZAStageDef("Z-D","Program Boundary and Future Scope",4,
            "Where does the GRUT program end and future work begin?",
            ["Boundary between program closure and open physics"]),
        ZAStageDef("Z-E","Final Sovereign Closure Ledger",5,
            "Close the entire GRUT program with honest accounting.",
            ["Terminal stage: no further appendices"]),
    ]


def _rules() -> List[ZARule]:
    return [
        ZARule("ZR1","Every entry carries Appendix P classification.",
            "undisciplined_entry"),
        ZARule("ZR2","Native and extension layers remain cleanly separated.",
            "layer_collapse"),
        ZARule("ZR3","All 12 mandatory distinctions maintained throughout Z.",
            "distinction_collapse"),
        ZARule("ZR4","Absent and blocked sectors documented, not hidden.",
            "gap_concealment"),
        ZARule("ZR5","No retroactive promotion of extension to native.",
            "retroactive_nativity"),
        ZARule("ZR6","Cumulative counts match Z0 inventory exactly.",
            "count_mismatch"),
        ZARule("ZR7","Final ledger is honest accounting, not completeness claim.",
            "completeness_smuggling"),
        ZARule("ZR8","Program closure is structural, not epistemic.",
            "epistemic_overclaim"),
    ]


def _ffms() -> List[ZAFFM]:
    return [
        ZAFFM("FFM-Z.1","inventory_as_physics",
            "Treating catalogue as proof.",
            "Cataloguing structures is not proving theorems"),
        ZAFFM("FFM-Z.2","architecture_as_completion",
            "Treating many stages as solved physics.",
            "Architecture is scaffolding; completion is derivation"),
        ZAFFM("FFM-Z.3","extension_as_native",
            "Treating 7 postulated axioms as if derived from core.",
            "Extension postulates are explicit, not native"),
        ZAFFM("FFM-Z.4","absence_as_failure",
            "Treating unbuilt sectors as program failure.",
            "Documenting what is missing is honest, not failure"),
        ZAFFM("FFM-Z.5","closure_as_truth",
            "Treating program ending as physics settled.",
            "Program closure is structural bookkeeping"),
        ZAFFM("FFM-Z.6","scaffolding_as_building",
            "Treating criteria/rules as if sectors are built.",
            "Integration criteria are not integrated sectors"),
        ZAFFM("FFM-Z.7","attachment_as_integration",
            "Treating one-way attachment as full integration.",
            "Attachment is weaker than shared dynamics/closure"),
        ZAFFM("FFM-Z.8","discipline_as_discovery",
            "Treating honest ledger as theory of everything.",
            "Discipline documents architecture, not discovers physics"),
    ]


def run_za_sovereign_ledger_charter() -> ZASovereignLedgerCharterResult:
    dist = _distinctions(); stg = _stages()
    rul = _rules(); ffm = _ffms()
    nc = ZANonclaimFirewall(ZA_NONCLAIMS, N_ZA_NONCLAIMS, True)

    key = [
        "12 MANDATORY DISTINCTIONS: inventory!=physics, architecture!=completion, "
        "native!=extension, operational!=ontological, attachment!=integration, "
        "absence!=impossibility, blocked!=impossible, scaffolding!=building, "
        "discipline!=discovery, closure!=truth, extension!=native, gap!=failure.",
        "8 RULES: P-classification required, layers separated, distinctions "
        "maintained, gaps documented, no retroactive promotion, counts match "
        "inventory, honest accounting, structural closure.",
        "8 FFMs: inventory_as_physics, architecture_as_completion, "
        "extension_as_native, absence_as_failure, closure_as_truth, "
        "scaffolding_as_building, attachment_as_integration, "
        "discipline_as_discovery.",
        "6-STAGE SEQUENCE: Z0 inventory -> Z-A charter -> Z-B postulate "
        "accounting -> Z-C sector status -> Z-D boundary/scope -> Z-E "
        "final sovereign closure.",
        "GRAND TOTALS from Z0: 32 items, 8 native, 13 extension, 3 analogy, "
        "1 constitutive, 8 absent, 2 blocked, 0 future-postulate.",
        "CAPSTONE IS HONEST ACCOUNTING: not theory of everything, not "
        "completeness claim, not physics settled. Discipline, not discovery.",
    ]

    allowed = [
        "12 mandatory distinctions defined and enforced for capstone",
        "8 rules governing honest closure and anti-inflation discipline",
        "8 FFMs preventing overclaiming from inventory/architecture/closure",
        "6-stage capstone sequence: Z0 through Z-E",
        "Grand totals: 7 extensions, 3 parameters, 0 new fields",
        "Absent and blocked sectors explicitly documented, not hidden",
        "Z-B authorized: postulate/parameter accounting next",
    ]

    forbidden = [
        "Inventory implies physics proved",
        "Architecture implies completion achieved",
        "Extension stack implies native derivation",
        "Absence implies program failure",
        "Closure implies truth settled",
        "Scaffolding implies building complete",
        "Discipline implies discovery made",
    ]

    diagnostics: Dict[str, Any] = {
        "n_stages": N_STAGES,
        "n_distinctions": N_DISTINCTIONS,
        "n_rules": N_RULES,
        "n_ffms": N_FFMS,
        "n_nonclaims": N_ZA_NONCLAIMS,
        "grand_total_items": 32,
        "grand_total_extensions": 7,
        "grand_total_parameters": 3,
        "grand_total_new_fields": 0,
        "full_qm": False,
        "unified_closure": False,
        "toe_status": False,
    }

    result = ZASovereignLedgerCharterResult(
        True, dist, stg, rul, ffm, nc,
        CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
        key, allowed, forbidden, ZA_NONCLAIMS, diagnostics)
    _validate(result); return result


def _validate(r: ZASovereignLedgerCharterResult) -> None:
    if len(r.distinctions) != N_DISTINCTIONS: raise ValueError("dist")
    if len(r.stage_sequence) != N_STAGES: raise ValueError("stages")
    for i, s in enumerate(r.stage_sequence):
        if s.stage_index != i: raise ValueError(f"stage {s.stage_id}")
    if len(r.rules) != N_RULES: raise ValueError("rules")
    if len(r.ffms) != N_FFMS: raise ValueError("ffms")
    names = [f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names: raise ValueError(f"missing {n}")
    if r.nonclaim_firewall.n_nonclaims != N_ZA_NONCLAIMS: raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered: raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS: raise ValueError("charter")
    if r.authorization_verdict not in ALLOWED_AUTH_VERDICTS: raise ValueError("auth")
    if r.overall_appendix_p not in ALLOWED_OVERALL_VERDICTS: raise ValueError("overall")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")
    if len(r.exact_nonclaims) != N_ZA_NONCLAIMS: raise ValueError("nonclaims")
    if r.diagnostics["full_qm"]: raise ValueError("qm False")
    if r.diagnostics["unified_closure"]: raise ValueError("closure False")
    if r.diagnostics["toe_status"]: raise ValueError("toe False")
    if r.diagnostics["grand_total_extensions"] != 7: raise ValueError("ext 7")


def _self_test() -> bool:
    r = run_za_sovereign_ledger_charter()
    assert r.valid and r.charter_verdict == CHARTER_VERDICT
    assert r.authorization_verdict == AUTH_VERDICT
    assert r.overall_appendix_p == OVERALL_P
    assert len(r.distinctions) == N_DISTINCTIONS
    assert len(r.stage_sequence) == N_STAGES
    assert len(r.rules) == N_RULES
    assert len(r.ffms) == N_FFMS
    assert r.diagnostics["full_qm"] is False
    assert r.diagnostics["toe_status"] is False
    assert r.diagnostics["grand_total_extensions"] == 7
    return True

if __name__ == "__main__":
    _self_test(); print("Z-A passed.")
