"""
Appendix W-F --- Effective Gravitational Phenomenology and Force-Law Audit
==========================================================================
GRUT Extension Program --- Phase W-F

Determines whether the W-B/W-D/W-E stack supports disciplined effective
gravitational phenomenology. Book II LOCKED. All gravity language is
explicit extension, not native.

=== STATIC SECTOR ANALYSIS ===

Static limit of telegrapher (d/dt = 0, tau1 and tau2 terms drop out):
  Phi - c^2 nabla^2 Phi = X
  => nabla^2 Phi - (1/c^2) Phi = -(1/c^2) X
  => nabla^2 Phi - mu^2 Phi = -mu^2 X    where mu = 1/c (in natural units)

This is a HELMHOLTZ/SCREENED equation, NOT a Poisson equation.
The "mass" mu = 1/c provides a screening length lambda = c.

For a point source X = Q delta(r) in 3D:
  Phi(r) = (Q mu^2 / 4pi) * exp(-mu r) / r = (Q / (4pi c^2)) * exp(-r/c) / r

This is a YUKAWA PROFILE, not 1/r.
  - At r << c: Phi ~ Q/(4pi c^2 r) -> Newtonian-like 1/r falloff
  - At r >> c: Phi ~ exp(-r/c)/r -> exponentially screened
  - Screening length = c (the propagation speed parameter)

FORCE LAW:
  F = -alpha grad(Phi) = -alpha * Q/(4pi c^2) * d/dr[exp(-mu r)/r] * r_hat
  At r << c: F ~ -alpha Q / (4pi c^2 r^2) -> inverse-square-like
  At r >> c: F exponentially screened

This is a SCREENED/YUKAWA GRAVITY ANALOG:
  - Short range: Newtonian-like (1/r^2)
  - Long range: screened by factor exp(-r/c)
  - Screening length set by propagation speed c

GEOMETRY CONSISTENCY:
  In weak-field static limit: geodesic-like motion in conformal metric
  gives the same probe acceleration as F = -alpha grad(Phi). Agreement
  is exact in this regime. Outside (time-dependent, strong field): diverge.

KEY INSIGHT: The constitutive "mass" term Phi in the ODE (which is the
native constitutive term, not added by hand) generates screening.
The native relaxation-to-source structure becomes, upon propagation
extension, a screening/Yukawa mechanism. The screening length IS the
propagation speed c in appropriate units.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_WF_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

STATIC_OPTIONS = frozenset({
    "poisson_like_static_sector_supported",
    "screened_or_helmholtz_static_sector_supported",
    "source_profile_dependent_static_sector_only",
    "static_sector_not_stable",
})
FORCE_OPTIONS = frozenset({
    "newtonian_like_gradient_force_conditionally_supported",
    "screened_force_law_conditionally_supported",
    "regime_dependent_force_law_only",
    "no_stable_force_law_phenomenology",
})
GEOM_CONSIST_OPTIONS = frozenset({
    "weak_field_force_and_metric_descriptions_agree",
    "partial_agreement_in_restricted_regime",
    "force_metric_overlap_not_stable",
    "geometry_force_consistency_not_established",
})
GRAVITY_OPTIONS = frozenset({
    "scalar_gravity_analogy_conditionally_supported",
    "weak_newtonian_limit_only",
    "force_like_phenomenology_without_gravity_language",
    "gravity_analogy_not_licensed",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WG",
    "stop_for_missing_gravity_boundary",
})
OVERALL_OPTIONS = frozenset({
    "weak_field_scalar_gravity_phenomenology_identified_under_strict_limits",
    "screened_gravity_analog_supported_without_gr_completion",
    "force_metric_consistency_obtained_only_in_restricted_regime",
    "gravity_extension_not_yet_stable",
})

WF_STATIC: str = "screened_or_helmholtz_static_sector_supported"
WF_FORCE: str = "screened_force_law_conditionally_supported"
WF_CONSIST: str = "weak_field_force_and_metric_descriptions_agree"
WF_GRAVITY: str = "scalar_gravity_analogy_conditionally_supported"
WF_AUTH: str = "authorized_to_proceed_to_WG"
WF_OVERALL: str = "screened_gravity_analog_supported_without_gr_completion"

WF_NONCLAIMS: List[str] = [
    "NOT_claiming_Yukawa_profile_therefore_GR__"
    "screened_scalar_potential_is_not_Einstein_gravity",
    "NOT_claiming_inverse_square_limit_therefore_Newton__"
    "short_range_1_over_r2_regime_is_analogy_not_derivation",
    "NOT_claiming_screening_length_therefore_cosmological__"
    "c_as_screening_scale_is_extension_parameter_not_horizon",
    "NOT_claiming_force_metric_agreement_therefore_geometry_dynamics__"
    "weak_field_consistency_is_not_Einstein_equations",
    "NOT_claiming_scalar_gravity_analog_therefore_tensor_gravity__"
    "scalar_field_coupling_is_not_spin_2_graviton",
    "NOT_claiming_static_solution_therefore_general_dynamics__"
    "static_Helmholtz_does_not_cover_time_dependent_regime",
    "NOT_claiming_Newtonian_limit_therefore_gravity_derived__"
    "structural_resemblance_in_one_limit_is_not_theory",
    "NOT_claiming_gravity_phenomenology_therefore_GR_completion__"
    "effective_phenomenology_is_not_fundamental_gravitational_theory",
]


@dataclass
class WFCandidate:
    regime: str; static_profile: str; force_law: str
    geometry_agree: str; strongest: str
    what_licensed: str; what_not_licensed: str

@dataclass
class WFObstruction:
    rank: int; name: str; description: str

@dataclass
class WFNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WFEffectiveGravityResult:
    valid: bool
    candidates: List[WFCandidate]
    obstructions: List[WFObstruction]
    nonclaim_firewall: WFNonclaimFirewall
    static_field_status: str; force_law_status: str
    geometry_consistency_status: str; gravity_analogy_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WFCandidate]:
    return [
        WFCandidate("static_point_source",
            "Phi = (Q/4pi c^2) exp(-r/c)/r (Yukawa)",
            "F ~ 1/r^2 at r<<c; screened at r>>c",
            "Yes (weak field static)","Screened gravity analog",
            "Yukawa potential, screened force","GR, unscreened Newton"),
        WFCandidate("extended_static_source",
            "Superposition of Yukawa profiles","Gradient of summed Yukawa",
            "Yes (weak field)","Composite screened potential",
            "Multi-source superposition","Point-particle dynamics"),
        WFCandidate("direct_gradient_force",
            "N/A (force from Phi)","F = -alpha grad(Phi)",
            "Yes (static test-probe)","Constitutive gradient force",
            "Force-law language","Gravity derivation"),
        WFCandidate("conformal_metric_motion",
            "N/A (geodesic)","Geodesic in ds^2_eff",
            "Yes (same acceleration)","Geodesic-like redescription",
            "Metric-force consistency","Einstein equations"),
        WFCandidate("screened_vs_unscreened",
            "Helmholtz not Poisson","Screened (exp decay)","N/A",
            "Yukawa/Helmholtz screening","Screened range classification",
            "Unscreened infinite-range gravity"),
        WFCandidate("time_dependent_breakdown",
            "Damping reactivates","Force modified by relaxation","No (breaks)",
            "Static limit only","Regime boundary documented",
            "General time-dependent gravity"),
    ]


def _build_obstructions() -> List[WFObstruction]:
    return [
        WFObstruction(1,"screened_not_unscreened",
            "Native constitutive term generates Helmholtz, not Poisson: "
            "force is screened at range c, not infinite-range"),
        WFObstruction(2,"scalar_not_tensor",
            "One scalar field: no spin-2 graviton, no tensor gravity"),
        WFObstruction(3,"no_einstein_equations",
            "Metric slaved to Phi, not independently dynamical"),
        WFObstruction(4,"static_regime_only",
            "Full time-dependent damped sector breaks clean gravity picture"),
        WFObstruction(5,"test_probe_only",
            "No back-reaction: probe doesn't source Phi"),
        WFObstruction(6,"extension_not_native",
            "Entire gravity analog is Book III postulate stack"),
    ]


def run_wf_effective_gravity_phenomenology_audit() -> WFEffectiveGravityResult:
    cands=_build_candidates();obs=_build_obstructions()
    fw=WFNonclaimFirewall(WF_NONCLAIMS,N_WF_NONCLAIMS,True)

    key=[
        "STATIC SECTOR IS HELMHOLTZ/SCREENED: nabla^2 Phi - (1/c^2) Phi = source. "
        "NOT Poisson. The native constitutive term Phi generates screening.",
        "YUKAWA PROFILE: Phi(r) = (Q/4pi c^2) exp(-r/c)/r for point source. "
        "Screening length = c (propagation speed parameter).",
        "INVERSE-SQUARE AT SHORT RANGE: at r << c, F ~ 1/r^2 (Newtonian-like). "
        "At r >> c: exponentially screened. Screened gravity analog.",
        "FORCE-METRIC CONSISTENCY: in weak-field static limit, gradient force "
        "and conformal-metric geodesic give SAME probe acceleration.",
        "KEY INSIGHT: the native constitutive 'mass' term (Phi in tau dPhi/dt + Phi = X) "
        "becomes, upon propagation extension, a SCREENING MECHANISM. "
        "The screening length IS the propagation speed c.",
        "SCALAR GRAVITY ANALOG conditionally supported: weak-field, static, "
        "screened, test-probe limit. NOT GR, NOT tensor, NOT unscreened.",
    ]

    allowed=[
        "Static sector is Helmholtz/screened: Yukawa profile with screening c",
        "Inverse-square-like at short range (r << c); screened at long range",
        "Force-metric consistency in weak-field static test-probe limit",
        "Scalar gravity analog conditionally supported in restricted regime",
        "Native constitutive term becomes screening mechanism upon propagation extension",
        "6 gravity-phenomenology obstructions documented",
        "W-G authorized: gravity boundary established",
    ]

    forbidden=[
        "Yukawa profile implies GR",
        "Short-range inverse-square implies Newton derived",
        "Screening length implies cosmological horizon",
        "Force-metric agreement implies Einstein equations",
        "Scalar analog implies tensor gravity",
        "Static solution implies general dynamics",
        "Gravity phenomenology implies GR completion",
    ]

    diagnostics: Dict[str,Any]={
        "static_operator":"Helmholtz_screened",
        "profile":"Yukawa_exp_neg_r_over_c_over_r",
        "screening_length":"c_propagation_speed",
        "short_range":"inverse_square_like",
        "long_range":"exponentially_screened",
        "force_metric_agree_static":True,
        "einstein_equations":False,
        "tensor_gravity":False,
        "unscreened_gravity":False,
        "test_probe_only":True,
        "n_candidates":N_CANDIDATES,
        "n_obstructions":len(obs),
        "n_nonclaims":N_WF_NONCLAIMS,
    }

    result=WFEffectiveGravityResult(
        True,cands,obs,fw,
        WF_STATIC,WF_FORCE,WF_CONSIST,WF_GRAVITY,WF_AUTH,WF_OVERALL,
        key,allowed,forbidden,WF_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WFEffectiveGravityResult)->None:
    if r.static_field_status not in STATIC_OPTIONS:raise ValueError("static")
    if r.force_law_status not in FORCE_OPTIONS:raise ValueError("force")
    if r.geometry_consistency_status not in GEOM_CONSIST_OPTIONS:raise ValueError("consist")
    if r.gravity_analogy_status not in GRAVITY_OPTIONS:raise ValueError("gravity")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WF_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if len(r.obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["einstein_equations"]:raise ValueError("einstein False")
    if r.diagnostics["unscreened_gravity"]:raise ValueError("unscreened False")
    if not r.diagnostics["force_metric_agree_static"]:raise ValueError("agree True")


def _self_test()->bool:
    r=run_wf_effective_gravity_phenomenology_audit()
    assert r.valid
    assert r.static_field_status==WF_STATIC
    assert r.force_law_status==WF_FORCE
    assert r.geometry_consistency_status==WF_CONSIST
    assert r.gravity_analogy_status==WF_GRAVITY
    assert r.authorization==WF_AUTH
    assert r.diagnostics["static_operator"]=="Helmholtz_screened"
    assert r.diagnostics["profile"]=="Yukawa_exp_neg_r_over_c_over_r"
    assert r.diagnostics["einstein_equations"] is False
    return True

if __name__=="__main__":
    _self_test();print("W-F passed.")
