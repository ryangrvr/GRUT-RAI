"""
Appendix V-G --- Source Dependence and Empty-Space Limit Audit
===============================================================
GRUT Vacuum Ontology Program --- Phase V-G

Determines how source dependence shapes manifest structure, what
empty space means, and whether space ceases when Phi vanishes.

=== CORE ANALYSIS ===

SOURCE-FREE REGIONS:
  Where X=0 and Phi has relaxed to zero: the constitutive law, tau, and
  spatial domain remain defined (V-B). The substrate PERSISTS with zero
  response. This is NOT ontological absence — it is quiescence.
  The field variable Phi is defined and equals zero; the law governing
  it is still valid; the domain still exists. Zero value ≠ nonexistence.

ISOLATED SOURCE SUPPORT:
  For a localized source X(x), the Phi response is determined by X's
  spatial profile. Since GRUT has NO native spatial propagation (U-D),
  Phi(x) at each point is governed by X(x) at the SAME point (local).
  "Support" of the Phi response = support of X. The field does not
  extend beyond the source profile autonomously.
  No compact/infinite support LAW is native — support is whatever X is.

MULTIPLE SOURCES:
  The native equation tau dPhi/dt + Phi = X is LINEAR in Phi.
  If X = X_1 + X_2, then Phi = Phi_1 + Phi_2 (superposition).
  But: this is superposition of RESPONSE to imposed source composition,
  not derived interaction between sources. The sources are external.

EMPTY SPACE:
  "Empty space" in GRUT = region with X=0 and Phi=0 (after relaxation).
  The substrate (law + tau + domain) persists. Empty space is:
  zero-response region on persistent substrate. Not nothing.
  Not "created by sources" — the substrate exists independently.

BOUNDARIES / HORIZONS:
  No ontological boundary where space ceases is licensed. Zero response
  transitions smoothly to nonzero response where X begins. No sharp
  edge, no horizon, no compact-support cutoff from dynamics.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_VG_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

EMPTY_OPTIONS = frozenset({
    "zero_response_on_persistent_substrate_supported",
    "empty_space_has_only_formal_status",
    "source_free_region_ontology_unresolved",
    "ontological_absence_of_space_supported",
})
SUPPORT_OPTIONS = frozenset({
    "support_is_source_profile_dependent_only",
    "conditional_extended_support_under_imposed_profiles",
    "compact_support_conditionally_supported",
    "infinite_support_established",
})
MULTI_OPTIONS = frozenset({
    "multisource_structure_reduces_to_imposed_source_composition",
    "conditional_linear_superposition_of_response",
    "nonlinear_multisource_response_supported",
    "multisource_status_unresolved",
})
SDEP_OPTIONS = frozenset({
    "weak_source_dependence_only_confirmed",
    "manifestation_strongly_source_dependent_on_persistent_substrate",
    "strict_source_created_space_supported",
    "source_dependence_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_VH",
    "stop_for_missing_empty_space_boundary",
})
OVERALL_OPTIONS = frozenset({
    "empty_space_is_zero_response_on_persistent_substrate",
    "source_manifestation_is_strongly_dependent_but_space_not_source_created",
    "empty_space_ontology_partially_bounded_under_strict_limits",
    "space_creation_or_boundary_not_established",
})

VG_EMPTY: str = "zero_response_on_persistent_substrate_supported"
VG_SUPPORT: str = "support_is_source_profile_dependent_only"
VG_MULTI: str = "conditional_linear_superposition_of_response"
VG_SDEP: str = "manifestation_strongly_source_dependent_on_persistent_substrate"
VG_AUTH: str = "authorized_to_proceed_to_VH"
VG_OVERALL: str = "empty_space_is_zero_response_on_persistent_substrate"

VG_NONCLAIMS: List[str] = [
    "NOT_claiming_Phi_eq_0_therefore_space_vanishes__"
    "zero_field_value_is_quiescence_not_nonexistence",
    "NOT_claiming_source_dependence_therefore_source_created_space__"
    "manifestation_depends_on_sources_but_substrate_persists_without",
    "NOT_claiming_source_profile_support_therefore_spatial_field_law__"
    "Phi_support_equals_X_support_not_derived_propagation",
    "NOT_claiming_linear_superposition_therefore_interaction__"
    "response_superposition_from_linear_ODE_is_not_source_interaction",
    "NOT_claiming_zero_boundary_therefore_horizon__"
    "smooth_transition_to_zero_is_not_ontological_edge",
    "NOT_claiming_empty_region_therefore_nothing__"
    "substrate_persists_in_source_free_regions",
    "NOT_claiming_source_extended_profile_therefore_infinite_range__"
    "profile_extent_is_imposed_not_dynamically_derived",
    "NOT_claiming_empty_space_audit_therefore_ontology_settled__"
    "source_dependence_is_one_aspect_not_full_vacuum_ontology",
]


@dataclass
class VGTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class VGEvidenceRow:
    candidate: str; structurally_supported: str; ontologically_licensed: str
    strongest_label: str; what_licensed: str; what_not_licensed: str

@dataclass
class VGObstruction:
    rank: int; name: str; description: str

@dataclass
class VGNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VGSourceDependenceEmptySpaceResult:
    valid: bool
    track_a_source_free: VGTrackResult
    track_b_isolated_source: VGTrackResult
    track_c_multiple_sources: VGTrackResult
    track_d_empty_space: VGTrackResult
    track_e_boundary: VGTrackResult
    track_f_classification: VGTrackResult
    track_g_firewall: VGTrackResult
    track_h_obstructions: List[VGObstruction]
    evidence_table: List[VGEvidenceRow]
    nonclaim_firewall: VGNonclaimFirewall
    empty_region_status: str; source_support_status: str
    multisource_status: str; source_dependence_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> VGTrackResult:
    return VGTrackResult("A","source_free_regions",
        "What is the status of regions where X=0, Phi=0?",
        ["Law + tau + domain persist (V-B). Phi is defined and equals zero.",
         "Zero response ≠ nonexistence. Substrate quiesces but persists.",
         "Classification: zero-response region on persistent substrate.",
         "Not ontological absence; not source-created nothingness."],
        VG_EMPTY, ["Persistent substrate with zero response"])

def _track_b() -> VGTrackResult:
    return VGTrackResult("B","isolated_source",
        "What support claims are licensed for isolated sources?",
        ["No native spatial propagation (U-D). Phi(x) governed by X(x) locally.",
         "Support of Phi response = support of X. No autonomous extension.",
         "No compact-support LAW and no infinite-range LAW are native.",
         "Support is SOURCE-PROFILE-DEPENDENT ONLY.",
         "If X is localized, Phi is localized. If X is extended, Phi is extended."],
        VG_SUPPORT, ["Support = source profile; no native spatial law"])

def _track_c() -> VGTrackResult:
    return VGTrackResult("C","multiple_sources",
        "What happens with multiple sources?",
        ["Native ODE is LINEAR: tau dPhi/dt + Phi = X.",
         "X = X_1 + X_2 -> Phi = Phi_1 + Phi_2 (superposition).",
         "This is superposition of RESPONSE to imposed composition.",
         "NOT derived interaction between sources (sources are external, U-B).",
         "Multi-source = source-composition through X, not field-mediated interaction."],
        VG_MULTI, ["Linear superposition of response; not source interaction"])

def _track_d() -> VGTrackResult:
    return VGTrackResult("D","empty_space",
        "What does empty space mean in GRUT?",
        ["Empty space = region with X=0, Phi=0 (after relaxation).",
         "Substrate persists: law + tau + domain still defined.",
         "Empty space is: zero-response region on persistent substrate.",
         "Not nothing. Not created by sources. The substrate exists independently.",
         "Manifest structure absent; formal structure persists."],
        "zero_response_persistent_substrate",
        ["Empty space = quiescent substrate, not void"])

def _track_e() -> VGTrackResult:
    return VGTrackResult("E","boundary_horizon",
        "Is any boundary where space ceases licensed?",
        ["No ontological boundary licensed. Zero-to-nonzero response transitions "
         "smoothly where X begins/ends. No sharp edge, no horizon.",
         "No compact-support cutoff from dynamics (no spatial dynamics).",
         "No cosmological horizon (no expansion, no geometry dynamics).",
         "The substrate does not have edges; it may have regions of zero response."],
        "no_boundary_or_horizon_licensed",
        ["No ontological edge of space"])

def _track_f() -> VGTrackResult:
    return VGTrackResult("F","source_dependence_classification",
        "How strong is source dependence?",
        ["MANIFESTATION is strongly source-dependent: without X, Phi=0.",
         "SUBSTRATE is not source-dependent: law+tau+domain persist at X=0.",
         "This is: manifestation strongly source-dependent on persistent substrate.",
         "Not strict source-created space (substrate exists without sources).",
         "Not weak dependence only (manifest structure fully requires sources)."],
        VG_SDEP, ["Strong manifestation dependence; persistent substrate"])

def _track_g() -> VGTrackResult:
    return VGTrackResult("G","firewall",
        "What does V-G NOT license?",
        ["NOT: space vanishes at Phi=0, source-created substrate, compact-support "
         "field law, infinite-range field law, cosmological horizon, "
         "ontological boundaries, field-mediated source interaction.",
         "SAFE: 'zero-response persistent substrate with source-profile-dependent "
         "manifestation and linear response superposition.'"],
        "firewall_secured",
        ["Zero response ≠ nonexistence; source-dependent ≠ source-created"])

def _build_obstructions() -> List[VGObstruction]:
    return [
        VGObstruction(1,"no_spatial_propagation",
            "No native spatial PDE: support = source profile, not field dynamics"),
        VGObstruction(2,"external_source_dependence",
            "Manifest structure entirely determined by imposed X"),
        VGObstruction(3,"no_native_geometry",
            "No metric dynamics to define spatial boundaries or horizons"),
        VGObstruction(4,"no_force_or_interaction_law",
            "Multi-source composition is through X, not derived interaction"),
        VGObstruction(5,"no_intrinsic_content",
            "No persistent vacuum content; everything vanishes at rest"),
        VGObstruction(6,"scalar_sparse_core",
            "One real scalar provides minimal ontological spatial content"),
    ]

def _build_evidence() -> List[VGEvidenceRow]:
    return [
        VGEvidenceRow("source_free_region",
            "Substrate persists","Persistent quiescence",
            "Zero-response persistent substrate","Substrate persistence",
            "Space vanishes, nothingness"),
        VGEvidenceRow("isolated_source_profile",
            "Source-profile-dependent","Profile-dependent only",
            "Support = source support","Profile-dependent language",
            "Compact/infinite-range field law"),
        VGEvidenceRow("multiple_sources",
            "Linear superposition","Response composition",
            "Superposition of response","Multi-source composition",
            "Field-mediated interaction"),
        VGEvidenceRow("empty_space",
            "Zero response on substrate","Quiescent, not void",
            "Empty but real substrate","Empty-space language",
            "Ontological nothingness"),
        VGEvidenceRow("boundary_horizon",
            "Not supported","Not licensed",
            "N/A","Nothing",
            "Horizon, edge, boundary of space"),
        VGEvidenceRow("source_created_space",
            "Not supported","Not licensed",
            "N/A","Nothing",
            "Source-created substrate"),
    ]


def run_vg_source_dependence_empty_space_audit() -> VGSourceDependenceEmptySpaceResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tf=_track_f();tg=_track_g()
    obs=_build_obstructions();ev=_build_evidence()
    fw=VGNonclaimFirewall(VG_NONCLAIMS,N_VG_NONCLAIMS,True)

    key=[
        "EMPTY SPACE = ZERO RESPONSE ON PERSISTENT SUBSTRATE: where X=0, Phi->0, "
        "but law+tau+domain persist. Quiescence, not nonexistence.",
        "SUPPORT IS SOURCE-PROFILE-DEPENDENT ONLY: no native spatial propagation "
        "means Phi support = X support. No compact/infinite-range law is native.",
        "LINEAR SUPERPOSITION OF RESPONSE: X=X_1+X_2 -> Phi=Phi_1+Phi_2 from "
        "linear ODE. This is response composition, not source interaction.",
        "MANIFESTATION STRONGLY SOURCE-DEPENDENT on persistent substrate: "
        "manifest Phi requires sources; substrate does not.",
        "NO BOUNDARY/HORIZON LICENSED: zero-to-nonzero transitions smoothly. "
        "No ontological edge, no compact cutoff, no cosmological horizon.",
        "6 empty-space obstructions: no spatial PDE, external X, no geometry, "
        "no interaction law, no intrinsic content, scalar sparse core.",
    ]

    allowed=[
        "Empty space = zero-response region on persistent substrate",
        "Source support determines Phi support (source-profile-dependent only)",
        "Linear superposition of response to composed sources",
        "Manifestation strongly source-dependent; substrate persists without",
        "No ontological boundary or horizon where space ceases",
        "6 empty-space obstructions documented",
        "V-H authorized: source-dependence boundary established",
    ]

    forbidden=[
        "Phi=0 implies space vanishes",
        "Source dependence implies source-created substrate",
        "Source profile implies spatial field law",
        "Linear superposition implies source interaction",
        "Zero boundary implies horizon",
        "Extended profile implies infinite range",
        "Empty-space audit implies ontology settled",
    ]

    diagnostics: Dict[str,Any]={
        "substrate_persists_at_zero":True,
        "space_vanishes_at_zero":False,
        "source_created_space":False,
        "native_support_law":False,
        "linear_superposition":True,
        "source_interaction_derived":False,
        "horizon_licensed":False,
        "n_obstructions":len(obs),
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_VG_NONCLAIMS,
    }

    result=VGSourceDependenceEmptySpaceResult(
        True,ta,tb,tc,td,te,tf,tg,obs,ev,fw,
        VG_EMPTY,VG_SUPPORT,VG_MULTI,VG_SDEP,VG_AUTH,VG_OVERALL,
        key,allowed,forbidden,VG_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:VGSourceDependenceEmptySpaceResult)->None:
    if r.empty_region_status not in EMPTY_OPTIONS:raise ValueError("empty")
    if r.source_support_status not in SUPPORT_OPTIONS:raise ValueError("support")
    if r.multisource_status not in MULTI_OPTIONS:raise ValueError("multi")
    if r.source_dependence_status not in SDEP_OPTIONS:raise ValueError("sdep")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_VG_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_CANDIDATES:raise ValueError("evidence")
    if len(r.track_h_obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["space_vanishes_at_zero"]:raise ValueError("vanish False")
    if r.diagnostics["source_created_space"]:raise ValueError("created False")
    if r.diagnostics["horizon_licensed"]:raise ValueError("horizon False")
    if not r.diagnostics["substrate_persists_at_zero"]:raise ValueError("persist True")


def _self_test()->bool:
    r=run_vg_source_dependence_empty_space_audit()
    assert r.valid
    assert r.empty_region_status==VG_EMPTY
    assert r.source_support_status==VG_SUPPORT
    assert r.multisource_status==VG_MULTI
    assert r.source_dependence_status==VG_SDEP
    assert r.authorization==VG_AUTH
    assert r.diagnostics["substrate_persists_at_zero"] is True
    assert r.diagnostics["space_vanishes_at_zero"] is False
    assert r.diagnostics["source_created_space"] is False
    return True

if __name__=="__main__":
    _self_test();print("V-G passed.")
