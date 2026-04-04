"""
Appendix U-A --- Unified-Field and Effective-Action Charter
============================================================
GRUT Unified-Field Program --- Phase U-A

Defines rules, prohibitions, mandatory distinctions, and admissible
claim structure for all later U stages. Opens unified-field analysis
under constraint.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "U0_unified_field_entry_inventory",
    "U-A_unified_field_and_effective_action_charter",
    "U-B_native_field_content_and_degrees_of_freedom",
    "U-C_action_principle_and_variational_structure",
    "U-D_effective_kinematics_and_propagation",
    "U-E_emergent_geometry_and_metric_like_structure",
    "U-F_effective_coupling_and_force_law",
    "U-G_sector_integration_and_unified_field_status",
    "U-H_final_unified_field_ledger_and_handoff_to_V",
]
N_STAGES: int = 9
N_DISTINCTIONS: int = 12
N_RULES: int = 8
N_FFMS: int = 8
N_UA_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "action_from_ode_existence",
    "hamiltonian_from_formal_manipulation",
    "gauge_from_internal_algebra",
    "einstein_hilbert_from_metric_language",
    "maxwell_from_topological_charge",
    "curvature_from_dissipation_lag",
    "unified_field_from_layer_coexistence",
    "exact_lorentz_from_emergent_appearance",
]

UA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_constructs_field_theory__"
    "charter_defines_rules_not_results",
    "NOT_claiming_field_content_known_before_audit__"
    "U_B_must_determine_native_DOF",
    "NOT_claiming_action_available__"
    "action_status_is_absent_or_unestablished",
    "NOT_claiming_geometry_licensed__"
    "effective_geometry_is_candidate_only",
    "NOT_claiming_unification_possible__"
    "sectors_are_layered_not_unified",
    "NOT_claiming_gauge_or_GR_recoverable__"
    "both_absent_from_all_prior_audits",
    "NOT_claiming_stage_success_guaranteed__"
    "each_stage_may_yield_BSR",
    "NOT_claiming_authorization_implies_field_theory_closure__"
    "authorization_means_licensed_not_solved",
]

CHARTER_VERDICT: str = "charter_defined_with_strict_prohibitions"
AUTH_VERDICT: str = "authorized_to_proceed_to_UB"
OVERALL_P: str = "unified_field_program_opened_under_strict_limits"

ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})


@dataclass
class UADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class UAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; success_type: str; notes: List[str]

@dataclass
class UARule:
    rule_id: str; statement: str; violation: str

@dataclass
class UAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class UANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class UAUBLicensed:
    licensed_tests: List[str]

@dataclass
class UACharter:
    valid: bool
    distinctions: List[UADistinction]
    stage_sequence: List[UAStageDef]
    rules: List[UARule]
    ffms: List[UAFFM]
    entry_nonclaims: UANonclaims
    ub_licensed: UAUBLicensed
    charter_verdict: str; authorization_verdict: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[UADistinction]:
    return [
        UADistinction("D1","constitutive_evolution","action_principle",
            "ODE existence does not imply variational derivation"),
        UADistinction("D2","dissipative_balance","euler_lagrange",
            "dV/dt+D=0 is bookkeeping, not extremal condition"),
        UADistinction("D3","scalar_field_ontology","unified_field_theory",
            "Having a scalar field is not having a unified field theory"),
        UADistinction("D4","effective_description","native_derivation",
            "Effective fit is not fundamental derivation"),
        UADistinction("D5","effective_kinematics","spacetime_geometry",
            "Propagation characteristics are not metric dynamics"),
        UADistinction("D6","metric_like_analogy","metric_dynamics",
            "Resembling a metric is not having dynamical geometry"),
        UADistinction("D7","force_law_fit","force_law_derivation",
            "Fitting data is not deriving a force law from first principles"),
        UADistinction("D8","internal_algebra","gauge_field",
            "Observable algebra is not gauge redundancy"),
        UADistinction("D9","topological_matter_scaffold","genuine_matter",
            "Defect classification is not particle physics"),
        UADistinction("D10","emergent_lorentz","exact_covariance",
            "Restricted-regime appearance is not fundamental invariance"),
        UADistinction("D11","pseudo_action","true_action",
            "Generating functional is not fundamental action"),
        UADistinction("D12","coherent_layering","unification",
            "Compatible coexistence is not unified framework"),
    ]


def _stages() -> List[UAStageDef]:
    return [
        UAStageDef("U0","Unified-field entry inventory",0,
            "What field/action structures exist?","success",[]),
        UAStageDef("U-A","Unified-field charter",1,
            "What governs unified-field claims?","success",[]),
        UAStageDef("U-B","Native field content and DOF",2,
            "What are the actual native field degrees of freedom?",
            "extension_level_outcome",
            ["First substantive U stage"]),
        UAStageDef("U-C","Action principle and variational structure",3,
            "Does GRUT admit an action or only constitutive evolution?",
            "extension_level_outcome",[]),
        UAStageDef("U-D","Effective kinematics and propagation",4,
            "What propagation structure exists?","extension_level_outcome",[]),
        UAStageDef("U-E","Emergent geometry / metric-like structure",5,
            "Is any effective geometric description licensed?",
            "extension_level_outcome",[]),
        UAStageDef("U-F","Effective coupling and force-law",6,
            "Are GR-like or other force-law analogs derivable?",
            "extension_level_outcome",[]),
        UAStageDef("U-G","Sector integration and unified-field status",7,
            "Do sectors share any common field/action framework?",
            "extension_level_outcome",[]),
        UAStageDef("U-H","Final unified-field ledger and handoff to V",8,
            "Close U and define what vacuum ontology may inherit.",
            "bounded_negative_result",[]),
    ]


def _rules() -> List[UARule]:
    return [
        UARule("U-R1","Every field/action claim carries Appendix P class.",
            "undisciplined_claim"),
        UARule("U-R2","Action claims require variational derivation.",
            "action_without_derivation"),
        UARule("U-R3","Geometry claims require metric + dynamics.",
            "geometry_without_dynamics"),
        UARule("U-R4","Force-law claims require derivation not fit.",
            "fit_as_derivation"),
        UARule("U-R5","Gauge claims require local symmetry + gauge field.",
            "gauge_without_field"),
        UARule("U-R6","All 12 mandatory distinctions must be maintained.",
            "distinction_collapse"),
        UARule("U-R7","S and T locked classes persist into U.",
            "retroactive_promotion"),
        UARule("U-R8","Unified-field claims require shared carrier + dynamics + closure.",
            "unification_without_closure"),
    ]


def _ffms() -> List[UAFFM]:
    return [
        UAFFM("FFM-U.1","action_from_ode_existence",
            "Inferring action from ODE existence.",
            "ODE existence is necessary not sufficient for action principle"),
        UAFFM("FFM-U.2","hamiltonian_from_formal_manipulation",
            "Inferring Hamiltonian from formal rearrangement.",
            "Dissipative systems generically lack Hamiltonian structure"),
        UAFFM("FFM-U.3","gauge_from_internal_algebra",
            "Inferring gauge fields from su(2) observable algebra.",
            "Observable algebra is internal/global, not local gauge"),
        UAFFM("FFM-U.4","einstein_hilbert_from_metric_language",
            "Inferring GR from metric-like language alone.",
            "Metric-like resemblance is not Einstein field equations"),
        UAFFM("FFM-U.5","maxwell_from_topological_charge",
            "Inferring Maxwell equations from topological charge.",
            "Topological charge conservation is not gauge field dynamics"),
        UAFFM("FFM-U.6","curvature_from_dissipation_lag",
            "Inferring spacetime curvature from dissipation or lag.",
            "Finite response time is not Riemannian curvature"),
        UAFFM("FFM-U.7","unified_field_from_layer_coexistence",
            "Inferring unified field theory from layered sectors.",
            "Coexistence without shared carrier/dynamics/closure is not unification"),
        UAFFM("FFM-U.8","exact_lorentz_from_emergent_appearance",
            "Inferring exact Lorentz from restricted regime.",
            "Emergent appearance is regime-limited, not exact restoration"),
    ]


def run_ua_unified_field_charter() -> UACharter:
    dist = _distinctions(); stg = _stages()
    rul = _rules(); ffm = _ffms()
    nc = UANonclaims(UA_NONCLAIMS, N_UA_NONCLAIMS, True)
    ub = UAUBLicensed([
        "identify_native_field_variables_and_degrees_of_freedom",
        "test_constitutive_vs_field_theoretic_formulation",
        "determine_whether_scalar_core_exhausts_native_content",
        "determine_how_extension_sectors_attach_to_native_carrier",
    ])

    key = [
        "12 mandatory distinctions: constitutive!=action, balance!=Euler-Lagrange, "
        "scalar!=unified, effective!=native, kinematics!=geometry, etc.",
        "8 discipline rules including shared-carrier requirement for unification",
        "8 forbidden failure modes: action from ODE, Hamiltonian from manipulation, "
        "gauge from algebra, GR from metric language, etc.",
        "Action principle status: ABSENT or unestablished (CTP/Galley is effective-regime)",
        "Geometry status: candidates may be TESTED but nothing established",
        "U-B licensed: native DOF, constitutive vs field-theoretic, extension attachment",
    ]

    allowed = [
        "Native scalar constitutive core present with tau, dissipation, irreversibility",
        "12 mandatory distinctions established between field-theory concepts",
        "8 forbidden failure modes prevent action/gauge/GR/unification overclaiming",
        "Action principle absent or unestablished; CTP is effective-regime only",
        "Effective geometry candidates identified for later testing",
        "U-B licensed: native DOF, formulation type, extension attachment",
        "Unified-field program opens under strict limits",
    ]

    forbidden = [
        "ODE implies action principle",
        "Formal manipulation implies Hamiltonian",
        "Internal algebra implies gauge fields",
        "Metric-like language implies GR",
        "Topological charge implies Maxwell equations",
        "Dissipation lag implies spacetime curvature",
        "Layer coexistence implies unified field theory",
    ]

    diag: Dict[str, Any] = {
        "n_stages": N_STAGES, "n_distinctions": N_DISTINCTIONS,
        "n_rules": N_RULES, "n_ffms": N_FFMS,
        "n_nonclaims": N_UA_NONCLAIMS,
        "n_ub_licensed": len(ub.licensed_tests),
    }

    result = UACharter(
        True, dist, stg, rul, ffm, nc, ub,
        CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
        key, allowed, forbidden, diag)
    _validate(result); return result


def _validate(r: UACharter) -> None:
    if len(r.distinctions) != N_DISTINCTIONS: raise ValueError("dist")
    if len(r.stage_sequence) != N_STAGES: raise ValueError("stages")
    for i, s in enumerate(r.stage_sequence):
        if s.stage_index != i: raise ValueError(f"stage {s.stage_id}")
    if len(r.rules) != N_RULES: raise ValueError("rules")
    if len(r.ffms) != N_FFMS: raise ValueError("ffms")
    names = [f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names: raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims != N_UA_NONCLAIMS: raise ValueError("nonclaims")
    if not r.entry_nonclaims.all_registered: raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS: raise ValueError("charter")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")


def _self_test() -> bool:
    r = run_ua_unified_field_charter()
    assert r.valid
    assert r.charter_verdict == CHARTER_VERDICT
    assert r.authorization_verdict == AUTH_VERDICT
    assert r.overall_appendix_p == OVERALL_P
    assert len(r.distinctions) == N_DISTINCTIONS
    assert len(r.ffms) == N_FFMS
    return True

if __name__ == "__main__":
    _self_test(); print("U-A passed.")
