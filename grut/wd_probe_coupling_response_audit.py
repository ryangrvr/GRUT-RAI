"""
Appendix W-D --- Probe Coupling and Response Extension Audit
=============================================================
GRUT Extension Program --- Phase W-D

Determines the minimal probe-coupling postulate for the propagated sector.
Book II canon LOCKED. Coupling is explicit postulate, not native.

=== ANALYSIS ===

PROBE IDENTITY: A point test-source is minimal. O(3) defects provide
richer identity but require the O(3) extension. For minimality:
a pointlike probe with position q(t) and scalar charge alpha.

COUPLING: gradient coupling F = -alpha * grad(Phi)(q) is preferred.
  - 1 postulate: coupling constant alpha
  - 0 new fields
  - Probe EOM: m dv/dt = -alpha grad(Phi)(q) - eta v (with optional drag)
  - This couples probe to SPATIAL GRADIENTS of Phi, which now exist
    thanks to W-B propagation sector.
  - Direct Phi coupling (F ~ Phi) gives no directionality.
  - Refractive coupling works but is a higher-level redescription.

RESPONSE: Gradient coupling yields constitutive force-like response.
  - F = -alpha grad(Phi): probe accelerates down Phi gradients
  - In the propagated sector, Phi has genuine spatial structure
  - This is a CONSTITUTIVE FORCE, not derived from first principles
  - Analogous to: charged particle in electric field E = -grad(V)

BACK-REACTION: Test-probe limit preferred (no back-reaction initially).
  - Full back-reaction: probe sources Phi (modifies telegrapher RHS)
  - This is a SECOND postulate on top of the coupling
  - Minimal choice: test-probe limit (one-way coupling)
  - Back-reaction can be added later as explicit upgrade

GEOMETRY LEVERAGE: Gradient coupling naturally supports:
  - Geodesic-like redescription (if effective metric is defined)
  - Refractive trajectory interpretation
  - Constitutive clock/ruler distortion via Phi-dependent tau_eff
  Best downstream candidate for W-E geometry work.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_WD_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

PROBE_OPTIONS = frozenset({
    "point_probe_or_test_source_preferred",
    "topological_defect_probe_conditionally_preferred",
    "apparatus_coupling_preferred",
    "probe_identity_not_stable",
})
COUPLING_OPTIONS = frozenset({
    "direct_scalar_or_gradient_coupling_preferred",
    "refractive_descriptor_coupling_preferred",
    "response_functional_coupling_preferred",
    "no_minimal_coupling_class_identified",
})
RESPONSE_OPTIONS = frozenset({
    "constitutive_force_like_response_supported",
    "refractive_or_trajectory_response_supported",
    "inertial_shift_only_supported",
    "no_useful_probe_response_established",
})
BACK_OPTIONS = frozenset({
    "test_probe_limit_preferred",
    "one_way_source_response_preferred",
    "conditional_backreaction_extension_needed",
    "full_backreaction_already_required",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WE",
    "stop_for_missing_probe_boundary",
})
OVERALL_OPTIONS = frozenset({
    "minimal_probe_response_extension_identified_under_strict_postulate_accounting",
    "constitutive_probe_coupling_preferred_for_propagated_sector",
    "probe_response_possible_but_architecturally_costly",
    "probe_extension_not_yet_stable",
})

WD_PROBE: str = "point_probe_or_test_source_preferred"
WD_COUPLING: str = "direct_scalar_or_gradient_coupling_preferred"
WD_RESPONSE: str = "constitutive_force_like_response_supported"
WD_BACK: str = "test_probe_limit_preferred"
WD_AUTH: str = "authorized_to_proceed_to_WE"
WD_OVERALL: str = "minimal_probe_response_extension_identified_under_strict_postulate_accounting"

WD_NONCLAIMS: List[str] = [
    "NOT_claiming_gradient_coupling_therefore_gravity__"
    "F_eq_neg_alpha_grad_Phi_is_constitutive_not_gravitational",
    "NOT_claiming_probe_EOM_therefore_native_force_law__"
    "probe_response_is_explicit_postulate_not_derivation",
    "NOT_claiming_test_probe_therefore_matter_completion__"
    "point_probe_is_minimal_scaffolding_not_physical_matter",
    "NOT_claiming_gradient_descent_therefore_geodesic__"
    "constitutive_response_is_not_metric_geodesic",
    "NOT_claiming_scalar_coupling_therefore_gauge__"
    "alpha_grad_Phi_is_scalar_coupling_not_gauge_mediation",
    "NOT_claiming_no_backreaction_therefore_consistent__"
    "test_probe_limit_is_approximation_not_closure",
    "NOT_claiming_probe_coupling_therefore_electromagnetism__"
    "scalar_gradient_force_is_not_Coulomb_or_Lorentz",
    "NOT_claiming_coupling_postulate_therefore_derivation__"
    "every_new_coupling_is_explicit_assumption",
]


@dataclass
class WDCandidate:
    name: str; new_postulates: int; new_params: int; new_fields: int
    probe_eom: bool; geometry_leverage: str; strongest: str; verdict: str

@dataclass
class WDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WDProbeCouplingResult:
    valid: bool
    candidates: List[WDCandidate]
    n_candidates: int
    recommended: str
    nonclaim_firewall: WDNonclaimFirewall
    probe_identity_status: str; coupling_class_status: str
    response_status: str; backreaction_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WDCandidate]:
    return [
        WDCandidate("point_test_probe_gradient",
            1,1,0,True,"high_geodesic_refractive",
            "Constitutive gradient force","PREFERRED"),
        WDCandidate("o3_defect_probe",
            2,2,0,True,"high_topological_identity",
            "Defect-Phi gradient coupling","conditional_richer_identity"),
        WDCandidate("direct_phi_coupling",
            1,1,0,True,"low_no_directionality",
            "Scalar potential response","weak_no_gradient"),
        WDCandidate("refractive_descriptor",
            1,1,0,False,"medium_effective_index",
            "Effective index modulation","redescription_not_EOM"),
        WDCandidate("response_functional_coupling",
            2,2,1,True,"medium_formal_control",
            "Response-field mediated","nonnative_auxiliary"),
        WDCandidate("backreaction_upgrade",
            2,1,0,True,"high_self_consistent",
            "Full coupled system","deferred_to_later"),
    ]


def run_wd_probe_coupling_response_audit() -> WDProbeCouplingResult:
    cands=_build_candidates()
    fw=WDNonclaimFirewall(WD_NONCLAIMS,N_WD_NONCLAIMS,True)

    key=[
        "POINT TEST PROBE WITH GRADIENT COUPLING PREFERRED: "
        "F = -alpha grad(Phi)(q). One postulate (alpha), zero new fields.",
        "Probe EOM: m dv/dt = -alpha grad(Phi)(q). Constitutive force-like "
        "response in the propagated scalar sector.",
        "GRADIENT COUPLING exploits W-B spatial structure: Phi now has genuine "
        "spatial gradients from telegrapher propagation.",
        "TEST-PROBE LIMIT preferred initially: no back-reaction. "
        "Probe responds to Phi but does not modify it.",
        "GEOMETRY LEVERAGE HIGH: gradient coupling naturally supports "
        "geodesic-like redescription and refractive interpretation (W-E).",
        "O(3) DEFECT PROBE conditionally available: richer identity but "
        "higher postulate cost (requires O(3) extension).",
        "ALL COUPLING IS EXPLICIT POSTULATE. Not native. Not gravity. Not gauge.",
    ]

    allowed=[
        "Point test probe with gradient coupling: F=-alpha grad(Phi), 1 postulate",
        "Constitutive force-like probe response in propagated sector",
        "Test-probe limit: no back-reaction initially",
        "Gradient coupling exploits W-B spatial structure",
        "High geometry leverage for later W-E effective-geometry work",
        "O(3) defect probe conditionally available at higher cost",
        "W-E authorized: probe coupling established",
    ]

    forbidden=[
        "Gradient coupling implies gravity",
        "Probe EOM implies native force law",
        "Test probe implies matter completion",
        "Gradient descent implies geodesic",
        "Scalar coupling implies gauge mediation",
        "No back-reaction implies consistent closure",
        "Coupling postulate implies derivation",
    ]

    diagnostics: Dict[str,Any]={
        "preferred_coupling":"F=-alpha*grad(Phi)",
        "new_postulates":1,
        "new_parameters":1,
        "new_fields":0,
        "probe_has_eom":True,
        "backreaction":False,
        "geometry_leverage":"high",
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_WD_NONCLAIMS,
    }

    result=WDProbeCouplingResult(
        True,cands,N_CANDIDATES,
        "point_test_probe_gradient_coupling",
        fw,WD_PROBE,WD_COUPLING,WD_RESPONSE,WD_BACK,WD_AUTH,WD_OVERALL,
        key,allowed,forbidden,WD_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WDProbeCouplingResult)->None:
    if r.probe_identity_status not in PROBE_OPTIONS:raise ValueError("probe")
    if r.coupling_class_status not in COUPLING_OPTIONS:raise ValueError("coupling")
    if r.response_status not in RESPONSE_OPTIONS:raise ValueError("response")
    if r.backreaction_status not in BACK_OPTIONS:raise ValueError("back")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WD_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if r.diagnostics["new_postulates"]!=1:raise ValueError("postulates")
    if r.diagnostics["backreaction"]:raise ValueError("back False")


def _self_test()->bool:
    r=run_wd_probe_coupling_response_audit()
    assert r.valid
    assert r.probe_identity_status==WD_PROBE
    assert r.coupling_class_status==WD_COUPLING
    assert r.response_status==WD_RESPONSE
    assert r.backreaction_status==WD_BACK
    assert r.authorization==WD_AUTH
    assert r.diagnostics["new_postulates"]==1
    assert r.diagnostics["new_fields"]==0
    assert r.diagnostics["backreaction"] is False
    return True

if __name__=="__main__":
    _self_test();print("W-D passed.")
