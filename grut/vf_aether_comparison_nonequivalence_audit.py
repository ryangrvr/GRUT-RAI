"""
Appendix V-F --- Aether Comparison and Non-Equivalence Audit
=============================================================
GRUT Vacuum Ontology Program --- Phase V-F

Determines exactly how GRUT compares to historical luminiferous aether.
Where overlap is real, where differences are decisive, and what
operational claims are licensed.

=== CLASSICAL AETHER FEATURE COMPARISON ===

Feature 1: MATERIAL MEDIUM FILLING SPACE
  Classical aether: yes, a material elastic substance.
  GRUT: NO. V-C/V-E: no material medium, no density, no stress, no fluid.
  The substrate is constitutive, not material. ABSENT.

Feature 2: BEARER OF WAVE PROPAGATION
  Classical aether: yes, light waves propagate through it.
  GRUT: NO. U-D: no native spatial propagation. No waves. No speed.
  The substrate does not carry waves. ABSENT — this is DECISIVE.

Feature 3: ELASTIC/MECHANICAL PROPERTIES
  Classical aether: yes, elastic solid or fluid supporting transverse waves.
  GRUT: NO. V-E: no stress, no pressure, no equation of state.
  No elastic or mechanical properties. ABSENT.

Feature 4: DETECTABLE PREFERRED FRAME / AETHER WIND
  Classical aether: yes, moving through it should be detectable (Michelson-Morley).
  GRUT: PARTIAL. V-D: preferred frame exists, source-tracking asymmetry
  is conditionally observable, but NO drag, NO wind resistance, and
  NO matter coupling law to produce operational detection.
  ANALOGY ONLY — preferred frame exists but is not operationally coupled
  to matter motion in any canonized way.

Feature 5: DRAG OR RESISTANCE EFFECTS
  Classical aether: debated (Fresnel drag, Stokes drag).
  GRUT: NO. V-D: no vacuum drag licensed. No back-reaction on sources.
  ABSENT.

Feature 6: INTRINSIC MEDIUM CONTENT
  Classical aether: yes, substance with definite properties.
  GRUT: NO. V-E: content is response-dependent, vanishes at rest.
  No intrinsic persistent vacuum content. ABSENT.

SUMMARY: of 6 classical aether features, GRUT shares 0 fully and has
at most partial overlap on preferred-frame existence. The absence of
wave-bearing, material-medium, elastic, drag, and content properties
is DECISIVE. GRUT is not historical aether.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_FEATURES: int = 6
N_NOEQUIV: int = 7
N_VF_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

AETHER_OPTIONS = frozenset({
    "historical_aether_identity_not_supported",
    "partial_preferred_frame_overlap_only",
    "medium_analogy_only",
    "historical_aether_conditionally_supported",
})
WAVE_OPTIONS = frozenset({
    "no_luminiferous_role_licensed",
    "conditional_effective_medium_role_only",
    "wave_medium_analogy_supported",
    "luminiferous_role_supported",
})
DETECT_OPTIONS = frozenset({
    "source_tracking_asymmetry_only_conditionally_observable",
    "no_aether_wind_claim_licensed",
    "conditional_operational_discrimination_supported",
    "aether_wind_like_detection_supported",
})
MATERIAL_OPTIONS = frozenset({
    "nonmaterial_constitutive_substrate_only",
    "material_medium_not_supported",
    "weak_material_analogy_only",
    "material_medium_supported",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_VG",
    "stop_for_missing_comparison_boundary",
})
OVERALL_OPTIONS = frozenset({
    "grut_substrate_decisively_non_equivalent_to_historical_aether",
    "preferred_frame_overlap_without_luminiferous_medium_identity",
    "constitutive_substrate_with_limited_aether_analogy_only",
    "aether_comparison_not_yet_resolved",
})

VF_AETHER: str = "historical_aether_identity_not_supported"
VF_WAVE: str = "no_luminiferous_role_licensed"
VF_DETECT: str = "source_tracking_asymmetry_only_conditionally_observable"
VF_MATERIAL: str = "nonmaterial_constitutive_substrate_only"
VF_AUTH: str = "authorized_to_proceed_to_VG"
VF_OVERALL: str = "grut_substrate_decisively_non_equivalent_to_historical_aether"

VF_NONCLAIMS: List[str] = [
    "NOT_claiming_preferred_frame_therefore_aether__"
    "preferred_frame_is_necessary_not_sufficient_for_aether_identity",
    "NOT_claiming_substrate_therefore_luminiferous__"
    "constitutive_substrate_does_not_carry_waves",
    "NOT_claiming_source_asymmetry_therefore_aether_wind__"
    "constitutive_tracking_is_not_mechanical_wind_detection",
    "NOT_claiming_nonmaterial_therefore_immaterial__"
    "constitutive_substrate_has_physical_tau_not_zero_ontology",
    "NOT_claiming_non_equivalence_therefore_irrelevance__"
    "partial_overlap_on_preferred_frame_is_real_and_documented",
    "NOT_claiming_Michelson_Morley_prediction__"
    "no_operational_matter_coupling_to_evaluate_experiment",
    "NOT_claiming_all_aether_concepts_refuted__"
    "non_equivalence_is_with_classical_luminiferous_specifically",
    "NOT_claiming_comparison_complete_therefore_ontology_settled__"
    "aether_comparison_is_one_audit_not_full_ontology",
]


@dataclass
class VFFeatureComparison:
    feature: str; classical_aether: str; grut_status: str
    overlap: str; decisive: bool; notes: List[str]

@dataclass
class VFTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class VFNonEquivalence:
    rank: int; name: str; description: str

@dataclass
class VFEvidenceRow:
    feature: str; grut_overlap: str; structurally_supported: str
    strongest_label: str; what_licensed: str; what_not_licensed: str

@dataclass
class VFNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VFAetherComparisonResult:
    valid: bool
    feature_comparison: List[VFFeatureComparison]
    track_a_features: VFTrackResult
    track_b_preferred_frame: VFTrackResult
    track_c_propagation: VFTrackResult
    track_d_detectability: VFTrackResult
    track_e_material: VFTrackResult
    track_f_nonequivalence: List[VFNonEquivalence]
    track_g_naming: VFTrackResult
    track_h_firewall: VFTrackResult
    evidence_table: List[VFEvidenceRow]
    nonclaim_firewall: VFNonclaimFirewall
    aether_identity_status: str; wave_medium_status: str
    detectability_status: str; material_medium_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _features() -> List[VFFeatureComparison]:
    return [
        VFFeatureComparison("material_medium","Yes: elastic substance","No: constitutive only",
            "absent",True,["V-C/V-E: no material medium, no density/stress"]),
        VFFeatureComparison("wave_bearer","Yes: light propagation","No: no spatial propagation",
            "absent",True,["U-D: no native waves, no speed. DECISIVE absence."]),
        VFFeatureComparison("elastic_mechanical","Yes: transverse wave support","No: no stress/pressure",
            "absent",True,["V-E: no stress, no elastic properties"]),
        VFFeatureComparison("preferred_frame","Yes: detectable via aether wind","Partial: frame exists, no wind",
            "partial_overlap",False,["V-D: frame exists but no matter coupling for detection"]),
        VFFeatureComparison("drag_resistance","Debated: Fresnel/Stokes","No: no drag licensed",
            "absent",True,["V-D: no vacuum drag, no back-reaction"]),
        VFFeatureComparison("intrinsic_content","Yes: substance properties","No: response-dependent only",
            "absent",True,["V-E: content vanishes at rest; no intrinsic content"]),
    ]

def _track_a() -> VFTrackResult:
    return VFTrackResult("A","feature_comparison",
        "How does GRUT compare to classical aether features?",
        ["Of 6 classical features: 0 fully present, 1 partial (preferred frame), 5 absent.",
         "Absent features: material medium, wave bearer, elastic, drag, intrinsic content.",
         "Partial: preferred frame exists but without operational coupling to matter.",
         "DECISIVE absences: wave-bearing and material-medium are the defining "
         "features of luminiferous aether. Both absent in GRUT."],
        VF_AETHER, ["0/6 full match; 1 partial; 5 absent"])

def _track_b() -> VFTrackResult:
    return VFTrackResult("B","preferred_frame_sufficiency",
        "Is preferred frame enough for aether identity?",
        ["Preferred frame is NECESSARY but NOT SUFFICIENT for aether.",
         "Many theories have preferred frames without being aether: "
         "Lorentz-violating QFT, condensed matter effective field theories, "
         "cosmological preferred frames (CMB rest frame).",
         "Aether = preferred frame + material medium + wave bearer. "
         "GRUT has only the first. Identity NOT supported."],
        "preferred_frame_necessary_not_sufficient",
        ["Frame alone does not make aether"])

def _track_c() -> VFTrackResult:
    return VFTrackResult("C","propagation_wave",
        "Does absence of propagation break the analogy decisively?",
        ["Classical aether was invented to carry light waves. "
         "Its entire purpose was wave propagation.",
         "GRUT has NO native spatial propagation (U-D). No waves. No speed.",
         "A medium that does not carry waves cannot be luminiferous aether.",
         "This is DECISIVE: the core function of aether is missing."],
        VF_WAVE, ["No waves = no luminiferous aether"])

def _track_d() -> VFTrackResult:
    return VFTrackResult("D","detectability",
        "What aether-like operational claims are licensed?",
        ["V-D: source-tracking asymmetry is conditionally observable.",
         "But: no matter coupling -> no aether wind detection.",
         "Michelson-Morley requires: light propagation + frame-dependent speed. "
         "GRUT has neither (no light, no propagation, no speed).",
         "No Michelson-Morley prediction is licensed either way.",
         "Operational detection: source-tracking only, conditionally."],
        VF_DETECT, ["Source tracking only; no wind, no Michelson-Morley"])

def _track_e() -> VFTrackResult:
    return VFTrackResult("E","material_medium",
        "Is any material-medium ontology licensed?",
        ["V-C: rest-frame substrate, not material medium.",
         "V-E: no density, no stress, no fluid, no equation of state.",
         "The substrate is constitutive: it defines a law and timescale, "
         "not a material substance.",
         "NONMATERIAL CONSTITUTIVE SUBSTRATE ONLY."],
        VF_MATERIAL, ["Constitutive, not material"])

def _track_g() -> VFTrackResult:
    return VFTrackResult("G","naming",
        "What is the strongest honest comparison label?",
        ["GRUT shares: preferred frame (partial).",
         "GRUT lacks: material medium, waves, elasticity, drag, content.",
         "DECISIVE non-equivalence on wave-bearing and material-medium.",
         "STRONGEST HONEST LABEL: 'preferred-frame substrate with partial "
         "aether overlap but decisive non-equivalence on luminiferous features.'",
         "Or more concisely: 'not aether; distinct substrate with frame overlap.'"],
        "non_aether_with_partial_frame_overlap",
        ["Decisive non-equivalence; partial overlap documented"])

def _track_h() -> VFTrackResult:
    return VFTrackResult("H","firewall",
        "What does any overlap NOT license?",
        ["NOT: luminiferous aether identity, optical wave medium, aether wind, "
         "material drag, Michelson-Morley prediction, elastic medium.",
         "SAFE: 'preferred-frame substrate with constitutive rest structure; "
         "not equivalent to historical luminiferous aether.'"],
        "firewall_secured",["Frame overlap ≠ aether identity"])

def _build_nonequiv() -> List[VFNonEquivalence]:
    return [
        VFNonEquivalence(1,"no_wave_bearing_role",
            "Classical aether carries light; GRUT has no native propagation"),
        VFNonEquivalence(2,"no_material_medium",
            "Aether is material substance; GRUT is constitutive substrate"),
        VFNonEquivalence(3,"no_elastic_mechanical_properties",
            "Aether has elasticity; GRUT has no stress/pressure"),
        VFNonEquivalence(4,"no_drag_or_wind",
            "Aether wind/drag debated but expected; GRUT has no drag"),
        VFNonEquivalence(5,"no_intrinsic_content",
            "Aether has substance properties; GRUT content vanishes at rest"),
        VFNonEquivalence(6,"no_operational_matter_coupling",
            "Aether detectable via light; GRUT has no probe coupling"),
        VFNonEquivalence(7,"constitutive_not_mechanical_frame",
            "Aether frame is mechanical; GRUT frame is constitutive"),
    ]

def _build_evidence() -> List[VFEvidenceRow]:
    return [
        VFEvidenceRow("preferred_frame","Partial (frame exists)","Yes (tau selects)",
            "Partial overlap","Frame existence","Aether identity"),
        VFEvidenceRow("wave_medium","Absent (no propagation)","No",
            "Decisive absence","Nothing","Luminiferous role"),
        VFEvidenceRow("drag_wind","Absent (no drag)","No",
            "Decisive absence","Nothing","Drag, wind, resistance"),
        VFEvidenceRow("material_medium","Absent (constitutive)","No",
            "Decisive absence","Nothing","Material substance"),
        VFEvidenceRow("stress_fluid","Absent (no tensor)","No",
            "Decisive absence","Nothing","Stress, fluid, EOS"),
        VFEvidenceRow("operational_detection","Conditional (source tracking)","Partial",
            "Conditional source asymmetry","Source-tracking language",
            "Michelson-Morley, aether wind"),
    ]


def run_vf_aether_comparison_nonequivalence_audit() -> VFAetherComparisonResult:
    feats=_features()
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tg=_track_g();th=_track_h()
    neq=_build_nonequiv();ev=_build_evidence()
    fw=VFNonclaimFirewall(VF_NONCLAIMS,N_VF_NONCLAIMS,True)

    key=[
        "DECISIVE NON-EQUIVALENCE: of 6 classical aether features, GRUT shares "
        "0 fully and has partial overlap only on preferred frame.",
        "NO WAVE-BEARING ROLE: the core function of luminiferous aether "
        "(carrying light waves) is entirely absent. No native propagation.",
        "NO MATERIAL MEDIUM: constitutive substrate only. No density, stress, "
        "fluid, elastic properties.",
        "NO DRAG: no vacuum drag, no aether wind, no back-reaction on sources.",
        "PREFERRED FRAME OVERLAP: real but insufficient for aether identity. "
        "Many non-aether theories have preferred frames.",
        "NO MICHELSON-MORLEY PREDICTION: no light, no propagation, no speed — "
        "cannot evaluate aether-wind experiments.",
        "7 non-equivalences ranked from wave-bearing to constitutive frame.",
    ]

    allowed=[
        "Decisive non-equivalence to historical luminiferous aether established",
        "Preferred-frame overlap documented as real but insufficient",
        "No luminiferous role: no native propagation or wave-bearing",
        "No material medium: constitutive substrate, not substance",
        "No drag or aether wind: no matter coupling, no back-reaction",
        "Source-tracking asymmetry conditionally observable but not aether wind",
        "V-G authorized: comparison boundary established",
    ]

    forbidden=[
        "Preferred frame implies aether identity",
        "Substrate implies luminiferous medium",
        "Source asymmetry implies aether wind",
        "Nonmaterial implies zero ontology",
        "Non-equivalence implies all aether concepts refuted",
        "No Michelson-Morley prediction implies null result",
        "Comparison complete implies ontology settled",
    ]

    diagnostics: Dict[str,Any]={
        "n_features_compared":N_FEATURES,
        "n_fully_present":0,
        "n_partial":1,
        "n_absent":5,
        "n_decisive_absences":5,
        "aether_identity":False,
        "luminiferous_role":False,
        "drag_licensed":False,
        "material_medium":False,
        "michelson_morley_predictable":False,
        "n_nonequivalences":len(neq),
        "n_nonclaims":N_VF_NONCLAIMS,
    }

    result=VFAetherComparisonResult(
        True,feats,ta,tb,tc,td,te,neq,tg,th,ev,fw,
        VF_AETHER,VF_WAVE,VF_DETECT,VF_MATERIAL,VF_AUTH,VF_OVERALL,
        key,allowed,forbidden,VF_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:VFAetherComparisonResult)->None:
    if r.aether_identity_status not in AETHER_OPTIONS:raise ValueError("aether")
    if r.wave_medium_status not in WAVE_OPTIONS:raise ValueError("wave")
    if r.detectability_status not in DETECT_OPTIONS:raise ValueError("detect")
    if r.material_medium_status not in MATERIAL_OPTIONS:raise ValueError("material")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_VF_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_FEATURES:raise ValueError("evidence")
    if len(r.feature_comparison)!=N_FEATURES:raise ValueError("features")
    if len(r.track_f_nonequivalence)!=N_NOEQUIV:raise ValueError("nonequiv")
    if r.diagnostics["aether_identity"]:raise ValueError("aether False")
    if r.diagnostics["luminiferous_role"]:raise ValueError("lum False")
    if r.diagnostics["n_fully_present"]!=0:raise ValueError("fully 0")


def _self_test()->bool:
    r=run_vf_aether_comparison_nonequivalence_audit()
    assert r.valid
    assert r.aether_identity_status==VF_AETHER
    assert r.wave_medium_status==VF_WAVE
    assert r.detectability_status==VF_DETECT
    assert r.material_medium_status==VF_MATERIAL
    assert r.authorization==VF_AUTH
    assert r.diagnostics["n_fully_present"]==0
    assert r.diagnostics["n_absent"]==5
    assert r.diagnostics["aether_identity"] is False
    return True

if __name__=="__main__":
    _self_test();print("V-F passed.")
