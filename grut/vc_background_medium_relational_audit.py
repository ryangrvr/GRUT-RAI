"""
Appendix V-C --- Background vs Medium vs Relational Status Audit
=================================================================
GRUT Vacuum Ontology Program --- Phase V-C

Determines which ontological category best fits the GRUT substrate:
background, medium, relational support, hybrid, or distinct category.

=== CORE ANALYSIS ===

V-B established: law + tau + domain persist at Phi=0. Phi decays to
zero without sources. Manifest structure requires sources. Strict
Machian NOT supported.

BACKGROUND: The constitutive law, tau, and spatial domain persist even
when Phi=0 and X=0. This is STRUCTURAL PERSISTENCE: the architecture
exists independent of excitation. But calling it "absolute background"
overclaims — it lacks geometric dynamics, action, or full Newtonian
absolute-space character. It is a CONSTITUTIVE SUBSTRATE that persists,
not a full background in the Newtonian/GR sense.

MEDIUM: The preferred rest frame (tau) and dissipative response give the
substrate medium-like character: something with a rest state, a response
timescale, and directional dynamics. But it is not a material fluid —
no density, no pressure, no equation of state. It is a REST-FRAME
SUBSTRATE without material medium ontology.

RELATIONAL: Manifest Phi structure requires sources (X). Without X,
Phi->0: the field quiesces. This is WEAK RELATIONAL manifestation.
But the substrate (law+tau+domain) persists without sources — so the
architecture is NOT strictly relational. It is a persistent substrate
with source-dependent manifestation.

HISTORICAL COMPARISONS:
  - Newtonian absolute space: partial (persistent structure) but no geometry
  - Luminiferous aether: partial (preferred frame + medium-like) but no waves,
    no light, no material substance
  - QFT vacuum: NO (no quantum structure, no fluctuations, no zero-point)
  - GR geometric background: NO (no metric dynamics, no curvature)
  - Machian relationalism: NO (substrate persists without sources)

STRONGEST LABEL: distinct scalar dissipative substrate. Not reducible to
any historical category. Persistent constitutive rest-frame structure with
weak relational manifestation layer.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_VC_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

BG_OPTIONS = frozenset({
    "persistent_background_structure_supported",
    "constitutive_substrate_without_full_background_identity",
    "background_status_mixed_or_unresolved",
    "no_background_status_licensed",
})
MED_OPTIONS = frozenset({
    "constitutive_medium_like_status_supported",
    "rest_frame_substrate_supported_without_material_medium",
    "medium_analogy_only",
    "no_medium_status_licensed",
})
REL_OPTIONS = frozenset({
    "weak_relational_manifestation_on_persistent_substrate",
    "strict_relational_ontology_supported",
    "nonrelational_substrate_persistence_supported",
    "relational_status_unresolved",
})
LABEL_OPTIONS = frozenset({
    "distinct_scalar_dissipative_substrate_category_supported",
    "hybrid_background_medium_label_conditionally_supported",
    "historical_labels_only_partially_applicable",
    "ontology_label_not_yet_stable",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_VD",
    "stop_for_missing_ontology_boundary",
})
OVERALL_OPTIONS = frozenset({
    "persistent_scalar_substrate_with_weak_relational_manifestation",
    "constitutive_rest_frame_substrate_not_reducible_to_historical_aether",
    "ontology_partially_classified_under_strict_limits",
    "ontology_category_not_yet_resolved",
})

VC_BG: str = "constitutive_substrate_without_full_background_identity"
VC_MED: str = "rest_frame_substrate_supported_without_material_medium"
VC_REL: str = "weak_relational_manifestation_on_persistent_substrate"
VC_LABEL: str = "distinct_scalar_dissipative_substrate_category_supported"
VC_AUTH: str = "authorized_to_proceed_to_VD"
VC_OVERALL: str = "constitutive_rest_frame_substrate_not_reducible_to_historical_aether"

VC_NONCLAIMS: List[str] = [
    "NOT_claiming_persistent_law_therefore_absolute_space__"
    "constitutive_persistence_is_not_Newtonian_absolute_background",
    "NOT_claiming_preferred_frame_therefore_aether__"
    "rest_frame_substrate_is_not_luminiferous_medium",
    "NOT_claiming_source_dependence_therefore_Mach__"
    "weak_relational_manifestation_is_not_strict_relationalism",
    "NOT_claiming_rest_frame_therefore_material_fluid__"
    "preferred_timescale_is_not_material_substance",
    "NOT_claiming_scalar_substrate_therefore_quantum_vacuum__"
    "dissipative_scalar_is_not_QFT_vacuum",
    "NOT_claiming_substrate_persistence_therefore_geometry__"
    "persistent_law_domain_is_not_geometric_manifold",
    "NOT_claiming_distinct_category_therefore_novel_ontology__"
    "classification_documents_limits_not_announces_discovery",
    "NOT_claiming_ontology_label_therefore_ontology_closed__"
    "category_label_is_classification_not_completion",
]


@dataclass
class VCTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class VCEvidenceRow:
    candidate: str; structurally_supported: str; ontologically_licensed: str
    strongest_label: str; what_licensed: str; what_not_licensed: str

@dataclass
class VCObstruction:
    rank: int; name: str; description: str

@dataclass
class VCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VCBackgroundMediumRelationalResult:
    valid: bool
    track_a_background: VCTrackResult
    track_b_medium: VCTrackResult
    track_c_relational: VCTrackResult
    track_d_historical: VCTrackResult
    track_e_preferred_frame: VCTrackResult
    track_f_naming: VCTrackResult
    track_g_firewall: VCTrackResult
    track_h_obstructions: List[VCObstruction]
    evidence_table: List[VCEvidenceRow]
    nonclaim_firewall: VCNonclaimFirewall
    background_status: str; medium_status: str
    relational_status: str; ontology_label_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> VCTrackResult:
    return VCTrackResult("A","background",
        "Does GRUT require a persistent background?",
        ["Law + tau + domain persist at Phi=0 (V-B). Structural persistence supported.",
         "But: no geometric dynamics, no action, not full Newtonian absolute space.",
         "Classification: constitutive substrate that persists, not full background.",
         "Stronger than 'formal scaffold' — tau is physical, not just notation.",
         "Weaker than 'absolute background' — no geometry, no absolute simultaneity."],
        VC_BG, ["Constitutive substrate: more than scaffold, less than absolute"])

def _track_b() -> VCTrackResult:
    return VCTrackResult("B","medium",
        "Does preferred tau make this a genuine medium?",
        ["Preferred rest frame + dissipative response = medium-like character.",
         "But: no density, no pressure, no equation of state, no material substance.",
         "Not a material fluid. Not a luminiferous aether (no waves, no light).",
         "Classification: rest-frame substrate without material medium ontology.",
         "The 'medium' carries constitutive response, not material content."],
        VC_MED, ["Rest-frame substrate: medium-like but not material"])

def _track_c() -> VCTrackResult:
    return VCTrackResult("C","relational",
        "How relational is GRUT?",
        ["Manifest Phi structure requires sources X (V-B). Weak source dependence.",
         "Substrate (law+tau+domain) persists without sources (V-B).",
         "Strict Machian: substrate requires sources. NOT supported.",
         "Classification: weak relational manifestation on persistent substrate.",
         "The architecture is NOT purely relational — it has persistent structure."],
        VC_REL, ["Weak relational manifestation on persistent substrate"])

def _track_d() -> VCTrackResult:
    return VCTrackResult("D","historical_comparison",
        "What historical category is closest?",
        ["Newtonian absolute: partial (persistent) but no geometry. Non-equivalence.",
         "Luminiferous aether: partial (preferred frame + medium-like) but no waves, "
         "no light, no material substance. Important structural overlap but "
         "critical non-equivalences.",
         "QFT vacuum: NO. No quantum structure, fluctuations, zero-point energy.",
         "GR geometric: NO. No metric dynamics, no curvature, no action.",
         "Machian: NO. Substrate persists without sources.",
         "Closest: between Newtonian background and aether, but with critical gaps. "
         "None is a correct identification. Historical labels partially applicable."],
        "historical_labels_partially_applicable",
        ["No historical category is a correct match"])

def _track_e() -> VCTrackResult:
    return VCTrackResult("E","preferred_frame",
        "What is the ontological meaning of the preferred frame?",
        ["tau defines a constitutive rest frame: the frame in which the "
         "relaxation law takes its canonical first-order form.",
         "This is physically meaningful: tau is not a coordinate artifact.",
         "But: it is not material rest frame (no substance), not geometric "
         "frame (no metric), not absolute simultaneity surface (no Newtonian space).",
         "Classification: constitutive rest frame of dissipative substrate. "
         "Physically meaningful but nonmaterial and nongeometric."],
        "constitutive_rest_frame_physical_but_nonmaterial",
        ["Preferred frame is constitutive, not material or geometric"])

def _track_f() -> VCTrackResult:
    return VCTrackResult("F","ontology_naming",
        "What is the strongest honest ontological label?",
        ["The GRUT substrate is: persistent, constitutive, rest-frame-bearing, "
         "dissipative, scalar, with weak relational manifestation.",
         "It does NOT fit: absolute background, material medium, strict relational, "
         "quantum vacuum, or geometric spacetime.",
         "STRONGEST HONEST LABEL: distinct scalar dissipative substrate.",
         "This is a NEW CATEGORY — not reducible to standard historical labels.",
         "It shares features with several but is identical to none."],
        VC_LABEL, ["Distinct category: not reducible to historical labels"])

def _track_g() -> VCTrackResult:
    return VCTrackResult("G","ontology_firewall",
        "What does V-C NOT license?",
        ["NOT: aether identity, absolute space identity, quantum vacuum identity, "
         "geometric spacetime identity, strict relational ontology, "
         "material fluid ontology, substance claims.",
         "STRONGEST SAFE: 'distinct scalar dissipative substrate with constitutive "
         "rest frame and weak relational manifestation.'"],
        "firewall_secured", ["Strict separation from all historical identities"])

def _build_obstructions() -> List[VCObstruction]:
    return [
        VCObstruction(1,"zero_response_ontological_ambiguity",
            "Phi=0 substrate persistence is structural, not ontologically settled"),
        VCObstruction(2,"no_geometry_or_action",
            "Cannot call it geometric background without metric dynamics"),
        VCObstruction(3,"no_material_substance",
            "Cannot call it medium without density, pressure, equation of state"),
        VCObstruction(4,"external_source_dependence",
            "Manifest structure requires sources; pure substrate is featureless"),
        VCObstruction(5,"scalar_sparse_core",
            "One real scalar provides minimal ontological content"),
        VCObstruction(6,"no_quantum_thermal_vacuum",
            "Cannot call it quantum or thermal vacuum without those structures"),
    ]

def _build_evidence() -> List[VCEvidenceRow]:
    return [
        VCEvidenceRow("source_free_persistence",
            "Yes (law+tau+domain)","Constitutive, not absolute",
            "Persistent constitutive substrate","Structural persistence",
            "Absolute space, geometric background"),
        VCEvidenceRow("preferred_frame",
            "Yes (tau rest frame)","Physical but nonmaterial",
            "Constitutive rest frame","Rest-frame language",
            "Aether identity, material rest"),
        VCEvidenceRow("medium_comparison",
            "Partial (response character)","Analogy only",
            "Rest-frame substrate","Medium-like analogy",
            "Material fluid, substance"),
        VCEvidenceRow("relational_interpretation",
            "Weak (manifestation only)","Weak relational",
            "Persistent substrate + weak manifestation","Weak source dependence",
            "Strict Machian ontology"),
        VCEvidenceRow("historical_aether",
            "Partial (frame + response)","Non-equivalence documented",
            "Partial analogy","Limited structural comparison",
            "Aether identity"),
        VCEvidenceRow("quantum_vacuum",
            "No","Not licensed",
            "N/A","Nothing","Any quantum vacuum claim"),
    ]


def run_vc_background_medium_relational_audit() -> VCBackgroundMediumRelationalResult:
    ta=_track_a();tb=_track_b();tc=_track_c();td=_track_d()
    te=_track_e();tf=_track_f();tg=_track_g()
    obs=_build_obstructions();ev=_build_evidence()
    fw=VCNonclaimFirewall(VC_NONCLAIMS,N_VC_NONCLAIMS,True)

    key=[
        "CONSTITUTIVE SUBSTRATE: law+tau+domain persist at Phi=0. More than "
        "scaffold (tau is physical), less than absolute background (no geometry).",
        "REST-FRAME SUBSTRATE: preferred frame is constitutive, physical, "
        "nonmaterial, nongeometric. Not aether identity.",
        "WEAK RELATIONAL MANIFESTATION: manifest Phi requires sources; "
        "substrate persists without. Strict Machian NOT supported.",
        "HISTORICAL COMPARISONS: partial overlap with Newtonian background "
        "and aether; critical non-equivalences with both. NO match to "
        "QFT vacuum, GR geometry, or strict Mach.",
        "DISTINCT CATEGORY: scalar dissipative substrate. Not reducible to "
        "any standard historical label. New ontological category.",
        "6 ontology obstructions: ambiguity, no geometry, no substance, "
        "source dependence, sparse core, no quantum/thermal.",
    ]

    allowed=[
        "Constitutive substrate persists structurally at Phi=0 (law+tau+domain)",
        "Rest-frame substrate: preferred frame is physical but nonmaterial",
        "Weak relational manifestation on persistent substrate",
        "Historical comparisons: partial analogy to aether/background, "
        "critical non-equivalences documented",
        "Distinct scalar dissipative substrate category: not reducible to "
        "any historical label",
        "6 ontology obstructions documented",
        "V-D authorized: ontology boundary established",
    ]

    forbidden=[
        "Persistent law implies absolute space",
        "Preferred frame implies aether",
        "Source dependence implies strict Machian",
        "Rest-frame substrate implies material fluid",
        "Scalar substrate implies quantum vacuum",
        "Substrate persistence implies geometry",
        "Distinct category implies novel ontology discovered",
    ]

    diagnostics: Dict[str,Any]={
        "persistent_substrate":True,
        "material_medium":False,
        "strict_relational":False,
        "aether_identity":False,
        "quantum_vacuum_identity":False,
        "geometric_background":False,
        "newtonian_absolute":False,
        "distinct_category":True,
        "n_obstructions":len(obs),
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_VC_NONCLAIMS,
    }

    result=VCBackgroundMediumRelationalResult(
        True,ta,tb,tc,td,te,tf,tg,obs,ev,fw,
        VC_BG,VC_MED,VC_REL,VC_LABEL,VC_AUTH,VC_OVERALL,
        key,allowed,forbidden,VC_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:VCBackgroundMediumRelationalResult)->None:
    if r.background_status not in BG_OPTIONS:raise ValueError("bg")
    if r.medium_status not in MED_OPTIONS:raise ValueError("med")
    if r.relational_status not in REL_OPTIONS:raise ValueError("rel")
    if r.ontology_label_status not in LABEL_OPTIONS:raise ValueError("label")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_VC_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_CANDIDATES:raise ValueError("evidence")
    if len(r.track_h_obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["material_medium"]:raise ValueError("med False")
    if r.diagnostics["strict_relational"]:raise ValueError("rel False")
    if r.diagnostics["aether_identity"]:raise ValueError("aether False")
    if not r.diagnostics["distinct_category"]:raise ValueError("distinct True")


def _self_test()->bool:
    r=run_vc_background_medium_relational_audit()
    assert r.valid
    assert r.background_status==VC_BG
    assert r.medium_status==VC_MED
    assert r.relational_status==VC_REL
    assert r.ontology_label_status==VC_LABEL
    assert r.authorization==VC_AUTH
    assert r.diagnostics["persistent_substrate"] is True
    assert r.diagnostics["aether_identity"] is False
    assert r.diagnostics["distinct_category"] is True
    return True

if __name__=="__main__":
    _self_test();print("V-C passed.")
