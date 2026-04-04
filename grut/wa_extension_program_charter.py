"""
Appendix W-A --- Extension Program Charter
============================================
GRUT Extension Program --- Phase W-A  (Book III Charter)

Defines rules under which future extension sectors may be introduced.
Book III adds structure to Book II's native foundation.
Book III may not reclassify extensions as native.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "W0_extension_entry_inventory",
    "W-A_extension_program_charter",
    "W-B_spatial_propagation_extension",
    "W-C_born_probability_extension",
    "W-D_action_and_variational_completion",
    "W-E_probe_coupling_and_force_structure",
    "W-F_effective_geometry_and_metric_extension",
    "W-G_gauge_and_fermionic_extension_boundary",
    "W-H_book_III_extension_ledger_and_closure",
]
N_STAGES: int = 9
N_DISTINCTIONS: int = 6
N_RULES: int = 8
N_FFMS: int = 8
N_WA_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "extension_retroactively_declared_native",
    "postulate_chain_declared_derivation",
    "effective_patch_declared_true_closure",
    "minimal_extension_declared_complete_sector",
    "auxiliary_formalism_declared_physical",
    "phenomenological_fit_declared_structural",
    "compatible_extension_declared_unified",
    "book_iii_declared_book_ii_revision",
]

WA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_builds_extensions__"
    "charter_defines_rules_not_constructions",
    "NOT_claiming_roadmap_is_derivation_order__"
    "architectural_priority_is_not_physics_necessity",
    "NOT_claiming_extension_possible_therefore_correct__"
    "coherent_postulation_is_not_physical_truth",
    "NOT_claiming_Book_III_revises_Book_II__"
    "native_canon_is_locked_and_immutable",
    "NOT_claiming_minimal_extension_therefore_sufficient__"
    "one_postulate_may_not_close_the_sector",
    "NOT_claiming_dependency_ranking_therefore_unique__"
    "multiple_valid_construction_orders_may_exist",
    "NOT_claiming_stage_success_guaranteed__"
    "each_extension_may_yield_BSR_or_failure",
    "NOT_claiming_authorization_implies_extension_success__"
    "authorization_means_licensed_not_built",
]

CHARTER_VERDICT: str = "charter_defined_with_anti_retroactive_rules"
AUTH_VERDICT: str = "authorized_to_proceed_to_WB"
OVERALL_P: str = "book_iii_extension_program_opened_under_strict_limits"

ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})


@dataclass
class WADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class WAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; notes: List[str]

@dataclass
class WARule:
    rule_id: str; statement: str; violation: str

@dataclass
class WAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class WANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WACharter:
    valid: bool
    distinctions: List[WADistinction]
    stage_sequence: List[WAStageDef]
    rules: List[WARule]
    ffms: List[WAFFM]
    entry_nonclaims: WANonclaims
    charter_verdict: str; authorization_verdict: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[WADistinction]:
    return [
        WADistinction("D1","native_fact","explicit_postulate",
            "Native facts are locked in Book II. Extensions are new postulates."),
        WADistinction("D2","compatible_extension","integrated_sector",
            "Compatible = no contradiction. Integrated = shared dynamics/closure."),
        WADistinction("D3","effective_patch","true_closure",
            "Patch fixes one regime. Closure solves the sector structurally."),
        WADistinction("D4","minimal_extension","ontology_rewrite",
            "Minimal adds one postulate. Rewrite changes the foundation."),
        WADistinction("D5","auxiliary_formalism","physical_sector",
            "Formalism is a tool. Sector is a physical claim."),
        WADistinction("D6","phenomenological_fit","structural_derivation",
            "Fit matches data. Derivation follows from axioms."),
    ]


def _stages() -> List[WAStageDef]:
    return [
        WAStageDef("W0","Extension entry inventory",0,
            "What is missing and how does it rank?",[]),
        WAStageDef("W-A","Extension program charter",1,
            "What rules govern extension work?",[]),
        WAStageDef("W-B","Spatial propagation extension",2,
            "Can a spatial operator be added minimally and coherently?",
            ["Layer-0 foundational; unlocks propagation, speed, characteristics"]),
        WAStageDef("W-C","Born probability extension",3,
            "Can Born rule be adopted as MIP and what does it enable?",
            ["Layer-0 foundational; unlocks statistics, Bell, measurement"]),
        WAStageDef("W-D","Action and variational completion",4,
            "Can an action be constructed with propagation sector?",
            ["Layer-1; requires W-B propagation"]),
        WAStageDef("W-E","Probe coupling and force structure",5,
            "Can probe-Phi coupling be postulated coherently?",
            ["Layer-1; requires W-B propagation"]),
        WAStageDef("W-F","Effective geometry and metric extension",6,
            "Can effective geometry be constructed from propagation + action?",
            ["Layer-2; requires W-B + W-D"]),
        WAStageDef("W-G","Gauge and fermionic extension boundary",7,
            "What is the minimal boundary for gauge/fermionic extensions?",
            ["Layer-2; maps requirements without building"]),
        WAStageDef("W-H","Book III extension ledger and closure",8,
            "Close Book III with final extension ledger.",
            ["Final stage; synthesizes W-B through W-G"]),
    ]


def _rules() -> List[WARule]:
    return [
        WARule("W-R1","Every extension carries explicit postulate label.",
            "unlabeled_extension"),
        WARule("W-R2","No extension may be retroactively declared native.",
            "retroactive_nativity"),
        WARule("W-R3","Each extension states its minimal postulate burden.",
            "hidden_postulate"),
        WARule("W-R4","Postulate chains are not derivations.",
            "chain_as_derivation"),
        WARule("W-R5","Effective patches are not true closure.",
            "patch_as_closure"),
        WARule("W-R6","Compatible extension is not unified sector.",
            "compatibility_as_unification"),
        WARule("W-R7","All 6 mandatory distinctions maintained.",
            "distinction_collapse"),
        WARule("W-R8","Book II locked classes persist immutably.",
            "book_ii_revision"),
    ]


def _ffms() -> List[WAFFM]:
    return [
        WAFFM("FFM-W.1","extension_retroactively_declared_native",
            "Declaring an extension native after the fact.",
            "Book II native canon is immutable."),
        WAFFM("FFM-W.2","postulate_chain_declared_derivation",
            "Claiming a chain of postulates is a derivation.",
            "Each link is a new assumption, not a consequence."),
        WAFFM("FFM-W.3","effective_patch_declared_true_closure",
            "Claiming a regime-limited fix closes the sector.",
            "Patches work in one regime; closure works in all."),
        WAFFM("FFM-W.4","minimal_extension_declared_complete_sector",
            "Claiming one postulate completes a sector.",
            "Minimal may be necessary but rarely sufficient."),
        WAFFM("FFM-W.5","auxiliary_formalism_declared_physical",
            "Treating mathematical convenience as physical claim.",
            "Response fields, multipliers, etc. are tools."),
        WAFFM("FFM-W.6","phenomenological_fit_declared_structural",
            "Treating data fitting as structural derivation.",
            "Fitting is matching; derivation is proving."),
        WAFFM("FFM-W.7","compatible_extension_declared_unified",
            "Calling compatible coexistence 'unification.'",
            "No shared carrier/dynamics/closure = no unification."),
        WAFFM("FFM-W.8","book_iii_declared_book_ii_revision",
            "Using Book III results to revise Book II verdicts.",
            "Book II is closed and immutable."),
    ]


def run_wa_extension_program_charter() -> WACharter:
    dist=_distinctions();stg=_stages();rul=_rules();ffm=_ffms()
    nc=WANonclaims(WA_NONCLAIMS,N_WA_NONCLAIMS,True)

    key=[
        "6 mandatory distinctions: native≠postulate, compatible≠integrated, "
        "patch≠closure, minimal≠rewrite, auxiliary≠physical, fit≠derivation.",
        "8 rules: every extension labeled, no retroactive nativity, "
        "minimal postulate stated, chains≠derivation, patches≠closure, "
        "compatible≠unified, distinctions maintained, Book II immutable.",
        "8 forbidden failure modes: retroactive nativity, chain-as-derivation, "
        "patch-as-closure, minimal-as-complete, auxiliary-as-physical, "
        "fit-as-structural, compatible-as-unified, Book III revising Book II.",
        "9-stage sequence: W0 through W-H.",
        "Recommended first extensions: born_probability (smallest postulate) "
        "and propagation_sector (most structural value).",
        "Book II canon LOCKED and IMMUTABLE throughout Book III.",
    ]

    allowed=[
        "6 mandatory distinctions established for extension work",
        "8 rules prevent retroactive nativity, false derivation, and "
        "compatibility-as-unification",
        "8 forbidden failure modes registered",
        "9-stage roadmap from inventory through closure",
        "Recommended: born_probability and propagation_sector as first extensions",
        "Book II native canon locked throughout Book III",
        "W-B authorized: spatial propagation extension first",
    ]

    forbidden=[
        "Charter builds extensions",
        "Roadmap implies derivation order",
        "Extension possible implies correct",
        "Book III revises Book II",
        "Minimal extension implies sufficient",
        "Dependency ranking implies unique order",
        "Authorization implies extension success",
    ]

    diag: Dict[str,Any]={"n_stages":N_STAGES,"n_distinctions":N_DISTINCTIONS,
        "n_rules":N_RULES,"n_ffms":N_FFMS,"n_nonclaims":N_WA_NONCLAIMS,
        "recommended_first":"born_probability_and_propagation_sector",
        "book_ii_status":"locked_immutable"}

    result=WACharter(True,dist,stg,rul,ffm,nc,
        CHARTER_VERDICT,AUTH_VERDICT,OVERALL_P,key,allowed,forbidden,diag)
    _validate(result);return result


def _validate(r:WACharter)->None:
    if len(r.distinctions)!=N_DISTINCTIONS:raise ValueError("dist")
    if len(r.stage_sequence)!=N_STAGES:raise ValueError("stages")
    for i,s in enumerate(r.stage_sequence):
        if s.stage_index!=i:raise ValueError(f"stage {s.stage_id}")
    if len(r.rules)!=N_RULES:raise ValueError("rules")
    if len(r.ffms)!=N_FFMS:raise ValueError("ffms")
    names=[f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names:raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims!=N_WA_NONCLAIMS:raise ValueError("nc")
    if not r.entry_nonclaims.all_registered:raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS:raise ValueError("charter")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")


def _self_test()->bool:
    r=run_wa_extension_program_charter()
    assert r.valid and r.charter_verdict==CHARTER_VERDICT
    assert r.authorization_verdict==AUTH_VERDICT
    assert r.overall_appendix_p==OVERALL_P
    assert len(r.distinctions)==N_DISTINCTIONS
    assert len(r.ffms)==N_FFMS
    return True

if __name__=="__main__":
    _self_test();print("W-A passed.")
