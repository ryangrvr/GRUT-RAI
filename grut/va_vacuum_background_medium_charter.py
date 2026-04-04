"""
Appendix V-A --- Vacuum, Background, and Medium Charter
=========================================================
GRUT Vacuum Ontology Program --- Phase V-A

Defines rules, prohibitions, mandatory distinctions, and admissible
ontology claim structure for all later V stages.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "V0_vacuum_ontology_entry_inventory",
    "V-A_vacuum_background_medium_charter",
    "V-B_vacuum_existence_and_ground_state",
    "V-C_background_vs_medium_vs_relational",
    "V-D_preferred_frame_and_rest_state_ontology",
    "V-E_vacuum_density_stress_substrate_content",
    "V-F_aether_comparison_and_non_equivalence",
    "V-G_source_dependence_and_empty_space_limit",
    "V-H_final_vacuum_ontology_ledger_and_handoff",
]
N_STAGES: int = 9
N_DISTINCTIONS: int = 12
N_RULES: int = 8
N_FFMS: int = 8
N_VA_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "aether_from_preferred_frame_alone",
    "absolute_space_from_tau",
    "quantum_vacuum_from_scalar_substrate",
    "geometry_from_constitutive_descriptor",
    "thermal_bath_from_dissipation",
    "relational_ontology_from_source_dependence",
    "substance_from_field_persistence",
    "nonexistence_from_zero_field_value",
]

VA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_settles_ontology__"
    "charter_defines_rules_not_conclusions",
    "NOT_claiming_vacuum_identified_therefore_vacuum_understood__"
    "scalar_substrate_is_entry_condition_not_interpretation",
    "NOT_claiming_aether_or_anti_aether__"
    "comparison_requires_audit_not_assumption",
    "NOT_claiming_relational_or_substantival__"
    "ontological_category_requires_V_B_through_V_G",
    "NOT_claiming_source_boundary_therefore_ontology_settled__"
    "X_role_requires_dedicated_audit",
    "NOT_claiming_constitutive_descriptors_therefore_real_geometry__"
    "metric_like_language_is_not_spacetime_ontology",
    "NOT_claiming_stage_success_guaranteed__"
    "each_stage_may_yield_BSR",
    "NOT_claiming_authorization_implies_ontology_closure__"
    "authorization_means_licensed_not_solved",
]

CHARTER_VERDICT: str = "charter_defined_with_strict_ontology_firewall"
AUTH_VERDICT: str = "authorized_to_proceed_to_VB"
OVERALL_P: str = "scalar_dissipative_substrate_identified_ontology_not_yet_closed"

ALLOWED_CHARTER_VERDICTS = frozenset({CHARTER_VERDICT, "charter_incomplete"})


@dataclass
class VADistinction:
    dist_id: str; left: str; right: str; explanation: str

@dataclass
class VAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; success_type: str; notes: List[str]

@dataclass
class VARule:
    rule_id: str; statement: str; violation: str

@dataclass
class VAFFM:
    mode_id: str; name: str; description: str; why_forbidden: str

@dataclass
class VANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VAVBLicensed:
    licensed_tests: List[str]

@dataclass
class VACharter:
    valid: bool
    distinctions: List[VADistinction]
    stage_sequence: List[VAStageDef]
    rules: List[VARule]
    ffms: List[VAFFM]
    entry_nonclaims: VANonclaims
    vb_licensed: VAVBLicensed
    charter_verdict: str; authorization_verdict: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[VADistinction]:
    return [
        VADistinction("D1","vacuum","medium","Vacuum is absence; medium is substance. Different categories."),
        VADistinction("D2","medium","substrate","Medium carries waves; substrate supports existence. Not same."),
        VADistinction("D3","substrate","matter","Substrate underlies; matter populates. Distinct roles."),
        VADistinction("D4","background","geometry","Background is arena; geometry is dynamics. Not equivalent."),
        VADistinction("D5","preferred_frame","spacetime_metric","Constitutive frame ≠ geometric frame."),
        VADistinction("D6","dissipative_vacuum","thermal_bath","Dissipation ≠ heat bath (no T, no ensemble)."),
        VADistinction("D7","scalar_substrate","quantum_vacuum","Classical scalar ≠ QFT vacuum fluctuations."),
        VADistinction("D8","constitutive_descriptor","ontology","Useful redescription ≠ ontological claim."),
        VADistinction("D9","source_free_vacuum","source_driven_response","X=0 state ≠ X≠0 response pattern."),
        VADistinction("D10","ground_state","zero_field_value","Lowest energy ≠ Phi=0 necessarily."),
        VADistinction("D11","aether_analogy","licensed_identity","Resemblance ≠ equivalence."),
        VADistinction("D12","measurement_distortion","spacetime_warping","Apparatus effect ≠ manifold curvature."),
    ]


def _stages() -> List[VAStageDef]:
    return [
        VAStageDef("V0","Vacuum ontology entry inventory",0,
            "What vacuum structures exist?","success",[]),
        VAStageDef("V-A","Vacuum charter",1,
            "What governs ontology claims?","success",[]),
        VAStageDef("V-B","Vacuum existence and ground state",2,
            "Does vacuum exist when X=0? What is ground state?",
            "extension_level_outcome",["First substantive V stage"]),
        VAStageDef("V-C","Background vs medium vs relational",3,
            "Is GRUT background, medium, relational, or hybrid?",
            "extension_level_outcome",[]),
        VAStageDef("V-D","Preferred frame and rest-state ontology",4,
            "What is the ontological meaning of tau and preferred frame?",
            "extension_level_outcome",[]),
        VAStageDef("V-E","Vacuum density, stress, substrate content",5,
            "Does the vacuum have substance-like properties?",
            "extension_level_outcome",[]),
        VAStageDef("V-F","Aether comparison and non-equivalence",6,
            "How does GRUT vacuum compare to historical aether?",
            "bounded_negative_result",[]),
        VAStageDef("V-G","Source dependence and empty-space limit",7,
            "Does space persist without sources?",
            "extension_level_outcome",[]),
        VAStageDef("V-H","Final vacuum ontology ledger and handoff",8,
            "Close V with final ontology status.",
            "bounded_negative_result",[]),
    ]


def _rules() -> List[VARule]:
    return [
        VARule("V-R1","Every ontology claim carries classification.","undisciplined_claim"),
        VARule("V-R2","Aether claims require explicit comparison audit.","aether_by_assumption"),
        VARule("V-R3","Substance claims require density/stress evidence.","substance_by_rhetoric"),
        VARule("V-R4","Relational claims require X=0 limit audit.","relational_by_assumption"),
        VARule("V-R5","Geometry claims require metric dynamics.","geometry_from_descriptor"),
        VARule("V-R6","All 12 mandatory distinctions maintained.","distinction_collapse"),
        VARule("V-R7","S/T/U locked classes persist into V.","retroactive_promotion"),
        VARule("V-R8","Ontology conclusions require positive audit, not default.","ontology_by_default"),
    ]


def _ffms() -> List[VAFFM]:
    return [
        VAFFM("FFM-V.1","aether_from_preferred_frame_alone",
            "Claiming aether identity from preferred tau frame.",
            "Preferred frame is necessary but not sufficient for aether."),
        VAFFM("FFM-V.2","absolute_space_from_tau",
            "Equating tau preferred frame with Newtonian absolute space.",
            "Constitutive timescale is not absolute space."),
        VAFFM("FFM-V.3","quantum_vacuum_from_scalar_substrate",
            "Equating classical scalar medium with quantum vacuum.",
            "No Born rule, no quantum fluctuations, no pair creation."),
        VAFFM("FFM-V.4","geometry_from_constitutive_descriptor",
            "Equating metric-like descriptor with geometric ontology.",
            "Constitutive reparameterization is not spacetime structure."),
        VAFFM("FFM-V.5","thermal_bath_from_dissipation",
            "Equating native dissipation with thermal bath.",
            "No temperature, no ensemble, no fluctuation-dissipation."),
        VAFFM("FFM-V.6","relational_ontology_from_source_dependence",
            "Assuming relational ontology from X-dependence without X=0 audit.",
            "Source dependence is structural; relational is philosophical."),
        VAFFM("FFM-V.7","substance_from_field_persistence",
            "Calling vacuum 'substance' because Phi persists.",
            "Persistence of field value is not substance without density/stress."),
        VAFFM("FFM-V.8","nonexistence_from_zero_field_value",
            "Claiming space doesn't exist when Phi=0.",
            "Zero field value may be degenerate state, not nonexistence."),
    ]


def run_va_vacuum_background_medium_charter() -> VACharter:
    dist=_distinctions();stg=_stages();rul=_rules();ffm=_ffms()
    nc=VANonclaims(VA_NONCLAIMS,N_VA_NONCLAIMS,True)
    vb=VAVBLicensed([
        "test_vacuum_existence_at_X_eq_0",
        "test_ground_state_status_of_Phi_eq_0",
        "test_whether_Phi_eq_0_is_trivial_physical_or_regime",
        "test_whether_vacuum_persists_without_sources",
    ])

    key=[
        "12 mandatory distinctions: vacuum≠medium, medium≠substrate, "
        "substrate≠matter, background≠geometry, etc.",
        "8 rules: aether requires audit, substance requires evidence, "
        "relational requires X=0 limit, ontology requires positive result",
        "8 forbidden failure modes: aether from frame, absolute space from tau, "
        "quantum vacuum from scalar, geometry from descriptor, etc.",
        "V-B licensed: vacuum at X=0, ground state, Phi=0 status, persistence",
        "Ontology is OPEN: not settled by charter, only bounded by rules",
        "Scalar dissipative substrate identified; ontology not yet closed",
    ]

    allowed=[
        "Scalar dissipative vacuum/substrate present as native entry condition",
        "12 mandatory ontology distinctions established",
        "8 forbidden failure modes prevent premature ontological commitment",
        "Source boundary (X role) present but ontological role unresolved",
        "Aether comparison is a legitimate audit target, not a default identity",
        "V-B licensed: vacuum existence, ground state, Phi=0, source independence",
        "Vacuum ontology program opens under strict firewall",
    ]

    forbidden=[
        "Preferred frame implies aether",
        "tau implies absolute space",
        "Scalar substrate implies quantum vacuum",
        "Constitutive descriptor implies geometry",
        "Dissipation implies thermal bath",
        "Source dependence implies relational ontology",
        "Field persistence implies substance",
    ]

    diag: Dict[str,Any]={"n_stages":N_STAGES,"n_distinctions":N_DISTINCTIONS,
        "n_rules":N_RULES,"n_ffms":N_FFMS,"n_nonclaims":N_VA_NONCLAIMS,
        "n_vb_licensed":len(vb.licensed_tests)}

    result=VACharter(True,dist,stg,rul,ffm,nc,vb,
        CHARTER_VERDICT,AUTH_VERDICT,OVERALL_P,key,allowed,forbidden,diag)
    _validate(result);return result


def _validate(r:VACharter)->None:
    if len(r.distinctions)!=N_DISTINCTIONS:raise ValueError("dist")
    if len(r.stage_sequence)!=N_STAGES:raise ValueError("stages")
    for i,s in enumerate(r.stage_sequence):
        if s.stage_index!=i:raise ValueError(f"stage {s.stage_id}")
    if len(r.rules)!=N_RULES:raise ValueError("rules")
    if len(r.ffms)!=N_FFMS:raise ValueError("ffms")
    names=[f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names:raise ValueError(f"missing {n}")
    if r.entry_nonclaims.n_nonclaims!=N_VA_NONCLAIMS:raise ValueError("nc")
    if not r.entry_nonclaims.all_registered:raise ValueError("reg")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS:raise ValueError("charter")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")


def _self_test()->bool:
    r=run_va_vacuum_background_medium_charter()
    assert r.valid and r.charter_verdict==CHARTER_VERDICT
    assert r.authorization_verdict==AUTH_VERDICT
    assert r.overall_appendix_p==OVERALL_P
    assert len(r.distinctions)==N_DISTINCTIONS
    assert len(r.ffms)==N_FFMS
    return True

if __name__=="__main__":
    _self_test();print("V-A passed.")
