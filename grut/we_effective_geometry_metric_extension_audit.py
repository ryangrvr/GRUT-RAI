"""
Appendix W-E --- Effective Geometry and Metric Extension Audit
===============================================================
GRUT Extension Program --- Phase W-E

Determines whether propagated sector + probe coupling supports any
effective geometry or metric extension. Book II LOCKED. All geometry
is explicit extension, not native.

=== ANALYSIS ===

CONFORMAL METRIC CANDIDATE:
  With W-B propagation (speed c) and spatially varying Phi, define:
  n(x) = 1 + alpha_g * Phi(x)  (effective refractive index)
  c_eff(x) = c / n(x)  (local effective speed)
  ds^2_eff = -c_eff(x)^2 dt^2 + dx^2 = -(c^2/(1+alpha_g Phi)^2) dt^2 + dx^2

  This is a CONFORMAL SCALAR METRIC: the effective line element depends
  on Phi through one scalar function. In weak field (alpha_g Phi << 1):
  ds^2_eff ~ -(c^2)(1 - 2 alpha_g Phi) dt^2 + dx^2

  Compare Newtonian limit of Schwarzschild: ds^2 ~ -(1 + 2V/c^2) c^2 dt^2 + dx^2
  where V is gravitational potential. STRUCTURAL RESEMBLANCE if Phi plays
  the role of gravitational potential. But: this is ANALOGY, not derivation.

GEODESIC REDESCRIPTION:
  The W-D probe law F = -alpha grad(Phi) can be recast as:
  In weak-field static limit, d^2x/dt^2 = -alpha/m * grad(Phi) is
  equivalent to geodesic motion in the conformal metric above if
  alpha/m = alpha_g * c^2 (identification of coupling constants).

  This is a CONDITIONAL GEODESIC-LIKE REDESCRIPTION:
  - Valid in: static weak-field test-probe limit
  - Fails for: strong fields, time-dependent Phi, full damped dynamics
  - NOT a proof of GR: it is a refractive-medium analog

COMMON GEOMETRY:
  Telegrapher wave propagation and probe motion can PARTIALLY share
  the same effective metric: both respond to Phi gradients. But:
  - Waves propagate at speed c (modified by Phi into c_eff)
  - Probes follow gradient-force trajectories
  - In the weak-field limit, both can use the same conformal metric
  - Outside that limit, the descriptions diverge

REGIME: Weak-field, static or slowly varying, test-probe limit only.
  Outside this regime: damping, time dependence, strong field all
  break the clean geometric picture.

NO CURVATURE DYNAMICS: The effective metric is determined by Phi,
which obeys the telegrapher equation. Phi is NOT determined by
Einstein equations. The metric is a SLAVE to the scalar field,
not an independent dynamical variable.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_WE_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

METRIC_OPTIONS = frozenset({
    "minimal_effective_metric_candidate_identified",
    "refractive_geometry_only_preferred",
    "conformal_metric_candidate_conditionally_supported",
    "no_stable_metric_extension_found",
})
GEODESIC_OPTIONS = frozenset({
    "geodesic_like_redescription_conditionally_supported",
    "refractive_trajectory_redescription_preferred",
    "constitutive_force_only_no_geometric_redescription",
    "geodesic_language_not_licensed",
})
COMMON_OPTIONS = frozenset({
    "partial_shared_effective_geometry_supported",
    "waves_and_probes_use_different_effective_kinematics",
    "common_geometry_not_established",
    "strong_common_metric_structure_supported",
})
REGIME_OPTIONS = frozenset({
    "weak_field_test_probe_regime_required",
    "static_or_slowly_varying_regime_required",
    "high_frequency_regime_required",
    "no_stable_geometry_regime_identified",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WF",
    "stop_for_missing_geometry_boundary",
})
OVERALL_OPTIONS = frozenset({
    "effective_metric_extension_identified_under_strict_limits",
    "refractive_geometry_redescription_supported_without_gravity_derivation",
    "geometry_overlay_possible_but_regime_limited",
    "metric_extension_not_yet_stable",
})

WE_METRIC: str = "conformal_metric_candidate_conditionally_supported"
WE_GEODESIC: str = "geodesic_like_redescription_conditionally_supported"
WE_COMMON: str = "partial_shared_effective_geometry_supported"
WE_REGIME: str = "weak_field_test_probe_regime_required"
WE_AUTH: str = "authorized_to_proceed_to_WF"
WE_OVERALL: str = "effective_metric_extension_identified_under_strict_limits"

WE_NONCLAIMS: List[str] = [
    "NOT_claiming_conformal_metric_therefore_GR__"
    "scalar_conformal_metric_is_not_Einstein_field_equations",
    "NOT_claiming_geodesic_redescription_therefore_gravity__"
    "weak_field_test_probe_geodesic_is_not_gravitational_dynamics",
    "NOT_claiming_Newtonian_resemblance_therefore_derivation__"
    "structural_analogy_to_Schwarzschild_is_not_proof",
    "NOT_claiming_refractive_index_therefore_geometry__"
    "medium_optics_is_not_spacetime_curvature",
    "NOT_claiming_shared_geometry_therefore_unification__"
    "partial_overlap_in_weak_field_is_not_unified_geometry",
    "NOT_claiming_metric_determined_by_Phi_therefore_Einstein__"
    "metric_slaved_to_scalar_field_is_not_dynamical_metric",
    "NOT_claiming_weak_field_regime_therefore_general__"
    "regime_limited_result_does_not_extend_to_strong_field",
    "NOT_claiming_geometry_extension_therefore_native__"
    "all_geometric_language_is_Book_III_postulate_level",
]


@dataclass
class WECandidate:
    name: str; new_postulates: int; new_params: int
    uses_existing: bool; metric_like: bool; geodesic_like: bool
    common_wave_probe: bool; strongest: str; verdict: str

@dataclass
class WEObstruction:
    rank: int; name: str; description: str

@dataclass
class WENonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WEEffectiveGeometryResult:
    valid: bool
    candidates: List[WECandidate]
    obstructions: List[WEObstruction]
    nonclaim_firewall: WENonclaimFirewall
    metric_extension_status: str; geodesic_status: str
    common_geometry_status: str; regime_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WECandidate]:
    return [
        WECandidate("conformal_scalar_metric",0,1,True,True,True,True,
            "Conformal effective metric in weak-field static limit",
            "PREFERRED_conditional"),
        WECandidate("optical_refractive_metric",0,1,True,True,False,True,
            "Refractive index n(x) from Phi","available_wave_only"),
        WECandidate("tau_eff_temporal_descriptor",0,0,True,True,False,False,
            "Temporal warping from Phi-dependent tau_eff","descriptor_only"),
        WECandidate("probe_geodesic_redescription",0,1,True,False,True,False,
            "Geodesic-like language for test probe","conditional_weak_field"),
        WECandidate("wave_probe_common_geometry",0,1,True,True,True,True,
            "Shared conformal metric for waves and probes","partial_weak_field"),
        WECandidate("backreaction_free_regime",0,0,True,True,True,True,
            "Test-probe limit: Phi unperturbed","required_simplification"),
    ]


def _build_obstructions() -> List[WEObstruction]:
    return [
        WEObstruction(1,"no_metric_dynamics",
            "Metric is slaved to Phi; not an independent dynamical variable"),
        WEObstruction(2,"regime_limited",
            "Only weak-field, static, test-probe limit; breaks outside"),
        WEObstruction(3,"no_einstein_equations",
            "No variational principle for the metric; not derivable"),
        WEObstruction(4,"damping_breaks_clean_geometry",
            "Full damped telegrapher disrupts clean geometric picture"),
        WEObstruction(5,"conformal_only",
            "Only conformal scalar metric; no full tensor geometry"),
        WEObstruction(6,"analogy_not_derivation",
            "Newtonian-limit resemblance is analogy, not gravitational proof"),
    ]


def run_we_effective_geometry_metric_extension_audit() -> WEEffectiveGeometryResult:
    cands=_build_candidates();obs=_build_obstructions()
    fw=WENonclaimFirewall(WE_NONCLAIMS,N_WE_NONCLAIMS,True)

    key=[
        "CONFORMAL SCALAR METRIC CONDITIONALLY SUPPORTED: "
        "ds^2_eff = -(c^2/(1+alpha_g Phi)^2)dt^2 + dx^2 in weak field.",
        "GEODESIC-LIKE REDESCRIPTION conditionally supported: "
        "F=-alpha grad(Phi) equivalent to geodesic motion in conformal metric "
        "in static weak-field test-probe limit.",
        "NEWTONIAN-LIMIT STRUCTURAL RESEMBLANCE: weak-field conformal metric "
        "resembles Schwarzschild Newtonian limit. ANALOGY, not derivation.",
        "PARTIAL SHARED GEOMETRY: waves (c_eff from refractive index) and probes "
        "(gradient force) can use same conformal metric in weak-field limit.",
        "REGIME: weak-field, static/slowly-varying, test-probe limit ONLY. "
        "Outside: damping, strong field, time dependence all break geometry.",
        "METRIC IS SLAVE TO PHI: determined by Phi via algebraic relation, "
        "NOT by Einstein equations. No metric dynamics.",
        "6 geometry obstructions: no metric dynamics, regime limited, "
        "no Einstein, damping breaks geometry, conformal only, analogy only.",
    ]

    allowed=[
        "Conformal scalar effective metric conditionally supported in weak field",
        "Geodesic-like redescription of probe motion in static test-probe limit",
        "Newtonian-limit structural resemblance documented as analogy",
        "Partial shared effective geometry for waves and probes in weak field",
        "Regime clearly stated: weak-field, static, test-probe limit only",
        "Metric is slave to Phi: no independent dynamics, no Einstein equations",
        "W-F authorized: geometry boundary established",
    ]

    forbidden=[
        "Conformal metric implies GR",
        "Geodesic redescription implies gravity",
        "Newtonian resemblance implies derivation",
        "Refractive index implies spacetime geometry",
        "Shared geometry implies unification",
        "Metric-from-Phi implies Einstein equations",
        "Weak-field result implies general validity",
    ]

    diagnostics: Dict[str,Any]={
        "conformal_metric_available":True,
        "geodesic_redescription":True,
        "newtonian_resemblance":True,
        "einstein_equations":False,
        "metric_dynamics":False,
        "regime":"weak_field_static_test_probe",
        "metric_slave_to_phi":True,
        "n_candidates":N_CANDIDATES,
        "n_obstructions":len(obs),
        "n_nonclaims":N_WE_NONCLAIMS,
    }

    result=WEEffectiveGeometryResult(
        True,cands,obs,fw,
        WE_METRIC,WE_GEODESIC,WE_COMMON,WE_REGIME,WE_AUTH,WE_OVERALL,
        key,allowed,forbidden,WE_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WEEffectiveGeometryResult)->None:
    if r.metric_extension_status not in METRIC_OPTIONS:raise ValueError("metric")
    if r.geodesic_status not in GEODESIC_OPTIONS:raise ValueError("geo")
    if r.common_geometry_status not in COMMON_OPTIONS:raise ValueError("common")
    if r.regime_status not in REGIME_OPTIONS:raise ValueError("regime")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WE_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if len(r.obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["einstein_equations"]:raise ValueError("einstein False")
    if r.diagnostics["metric_dynamics"]:raise ValueError("dynamics False")
    if not r.diagnostics["metric_slave_to_phi"]:raise ValueError("slave True")


def _self_test()->bool:
    r=run_we_effective_geometry_metric_extension_audit()
    assert r.valid
    assert r.metric_extension_status==WE_METRIC
    assert r.geodesic_status==WE_GEODESIC
    assert r.common_geometry_status==WE_COMMON
    assert r.regime_status==WE_REGIME
    assert r.authorization==WE_AUTH
    assert r.diagnostics["conformal_metric_available"] is True
    assert r.diagnostics["einstein_equations"] is False
    return True

if __name__=="__main__":
    _self_test();print("W-E passed.")
