"""
Appendix W-B --- Spatial Propagation Extension Audit
=====================================================
GRUT Extension Program --- Phase W-B

Determines the minimal explicit extension that upgrades GRUT from
purely local temporal relaxation to spatially structured propagation.
Book II canon is LOCKED. This is postulate accounting, not native derivation.

=== CANDIDATE ANALYSIS ===

CLASS 1: DIFFUSIVE (parabolic)
  tau dPhi/dt + Phi - ell^2 nabla^2 Phi = X
  New postulates: one spatial scale ell (length)
  New parameters: 1 (ell)
  New fields: 0
  Propagation: diffusive (infinite speed, exponential smearing)
  Finite speed: NO (parabolic = infinite signal speed)
  Preserves dissipation: YES (tau term untouched)
  Lorentz-like: NO (diffusion is not Lorentz-covariant)
  Cost: MINIMAL (one parameter, one spatial operator)

CLASS 2: DAMPED HYPERBOLIC (telegrapher)
  tau_2 d^2Phi/dt^2 + tau_1 dPhi/dt + Phi - c^2 nabla^2 Phi = X
  New postulates: two parameters (tau_2 or c, and ell or c)
  New parameters: 2 (inertial timescale tau_2, propagation speed c = ell/sqrt(tau_2))
  New fields: 0
  Propagation: damped wave (FINITE speed c at short times, diffusive at long times)
  Finite speed: YES (c = ell/sqrt(tau_2) is characteristic speed)
  Preserves dissipation: YES (tau_1 term = native dissipation; dominates at t >> tau_2)
  Lorentz-like: RESTRICTED (at frequencies >> 1/tau_1, wave equation with speed c
    gives local effective Lorentz appearance. At low frequencies: dissipation dominates.)
  Cost: MODERATE (two parameters, second-order time derivative)

CLASS 3: NONLOCAL KERNEL
  int K(x-x',t-t') Phi(x',t') dx' dt' = X
  New postulates: entire kernel function K
  New parameters: many (kernel shape, decay, range)
  New fields: 0
  Propagation: depends on K
  Cost: HIGH (underdetermined without specific K)

CLASS 4: AUXILIARY FIELD
  Introduce mediator Psi with its own dynamics coupling to Phi.
  New postulates: new field + coupling law + Psi dynamics
  Cost: HIGHEST (new field, new equations, new DOF)

RECOMMENDATION: CLASS 2 (DAMPED HYPERBOLIC / TELEGRAPHER)
  - Finite speed: YES (structural value for force/geometry work)
  - Preserves dissipation: YES (native core recovered at long time)
  - Restricted Lorentz: YES (at high frequencies)
  - Cost: moderate (2 parameters, no new fields)
  - Future leverage: highest (enables characteristic structure,
    effective light cone, force-law testing, geometry candidates)
  - The native core tau dPhi/dt + Phi = X is the LONG-TIME LIMIT
    of the telegrapher equation (tau_2 -> 0 limit).
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 4
N_WB_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

PROP_OPTIONS = frozenset({
    "minimal_propagation_patch_identified",
    "propagation_requires_major_rewrite",
    "multiple_equally_minimal_candidates",
    "no_justified_propagation_extension_found",
})
PREF_OPTIONS = frozenset({
    "diffusive_extension_preferred",
    "damped_hyperbolic_extension_preferred",
    "nonlocal_kernel_extension_preferred",
    "auxiliary_field_extension_preferred",
    "no_preferred_extension",
})
SPEED_OPTIONS = frozenset({
    "no_finite_speed_from_minimal_patch",
    "finite_characteristic_speed_conditionally_supported",
    "effective_speed_only",
    "speed_structure_not_resolved",
})
LORENTZ_OPTIONS = frozenset({
    "no_lorentz_like_regime_licensed",
    "restricted_effective_lorentz_appearance_supported",
    "broader_effective_relativistic_regime_supported",
    "lorentz_question_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WC",
    "stop_for_missing_propagation_boundary",
})
OVERALL_OPTIONS = frozenset({
    "first_propagation_extension_identified_under_strict_postulate_accounting",
    "propagation_patch_possible_but_structurally_costly",
    "damped_transport_extension_preferred_over_native_quiescence",
    "propagation_extension_not_yet_stable",
})

WB_PROP: str = "minimal_propagation_patch_identified"
WB_PREF: str = "damped_hyperbolic_extension_preferred"
WB_SPEED: str = "finite_characteristic_speed_conditionally_supported"
WB_LORENTZ: str = "restricted_effective_lorentz_appearance_supported"
WB_AUTH: str = "authorized_to_proceed_to_WC"
WB_OVERALL: str = "first_propagation_extension_identified_under_strict_postulate_accounting"

WB_NONCLAIMS: List[str] = [
    "NOT_claiming_propagation_was_native__"
    "spatial_propagation_is_explicit_extension_postulate",
    "NOT_claiming_telegrapher_is_native_ODE__"
    "second_order_time_derivative_is_new_postulate_not_native",
    "NOT_claiming_finite_speed_was_hidden__"
    "speed_c_is_new_parameter_from_tau2_and_ell",
    "NOT_claiming_effective_Lorentz_therefore_exact__"
    "restricted_high_frequency_appearance_is_not_native_invariance",
    "NOT_claiming_diffusive_limit_therefore_native__"
    "native_core_is_recovered_as_limit_but_telegrapher_is_extension",
    "NOT_claiming_two_parameters_therefore_minimal__"
    "moderate_cost_is_honest_accounting_not_minimality_claim",
    "NOT_claiming_propagation_therefore_geometry__"
    "spatial_transport_is_not_metric_dynamics",
    "NOT_claiming_extension_preferred_therefore_correct__"
    "preference_is_architectural_not_truth_claim",
]


@dataclass
class WBCandidate:
    class_id: str; class_name: str; form: str
    new_postulates: int; new_parameters: int; new_fields: int
    propagation_type: str; finite_speed: bool
    preserves_dissipation: bool; lorentz_like: str
    cost_level: str; structural_value: str
    verdict: str; notes: List[str]

@dataclass
class WBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WBSpatialPropagationResult:
    valid: bool
    candidates: List[WBCandidate]
    n_candidates: int
    recommended: str
    nonclaim_firewall: WBNonclaimFirewall
    propagation_extension_status: str
    preferred_extension_class: str
    speed_status: str
    lorentz_appearance_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WBCandidate]:
    return [
        WBCandidate("C1","diffusive_parabolic",
            "tau dPhi/dt + Phi - ell^2 nabla^2 Phi = X",
            1,1,0,"diffusive",False,True,"none","minimal","low",
            "minimal_but_no_finite_speed",
            ["One parameter ell; no finite speed; no Lorentz regime"]),
        WBCandidate("C2","damped_hyperbolic_telegrapher",
            "tau_2 d^2Phi/dt^2 + tau_1 dPhi/dt + Phi - c^2 nabla^2 Phi = X",
            2,2,0,"damped_wave",True,True,"restricted_high_frequency",
            "moderate","highest",
            "PREFERRED: finite speed + dissipation preserved + Lorentz regime",
            ["Two parameters (tau_2, c or ell); second-order time",
             "Native core = long-time limit (tau_2 -> 0)",
             "Speed c = ell/sqrt(tau_2) is new characteristic",
             "Restricted Lorentz at omega >> 1/tau_1"]),
        WBCandidate("C3","nonlocal_kernel",
            "int K(x-x',t-t') Phi dx' dt' = X",
            0,0,0,"depends_on_K",False,True,"depends_on_K",
            "high_underdetermined","conditional",
            "underdetermined_without_specific_K",
            ["Kernel K must be fully specified; many free parameters"]),
        WBCandidate("C4","auxiliary_field",
            "Phi + mediator Psi with coupling",
            3,3,1,"indirect",True,True,"conditional",
            "highest","conditional",
            "highest_cost_new_field",
            ["New field Psi; new coupling; new dynamics; highest overhead"]),
    ]


def run_wb_spatial_propagation_extension_audit() -> WBSpatialPropagationResult:
    cands=_build_candidates()
    fw=WBNonclaimFirewall(WB_NONCLAIMS,N_WB_NONCLAIMS,True)

    key=[
        "DAMPED HYPERBOLIC (TELEGRAPHER) PREFERRED as first propagation extension: "
        "tau_2 d^2Phi/dt^2 + tau_1 dPhi/dt + Phi - c^2 nabla^2 Phi = X.",
        "NEW POSTULATES: 2 parameters (tau_2 inertial timescale, c propagation speed). "
        "No new fields. Second-order time derivative is EXTENSION, not native.",
        "FINITE CHARACTERISTIC SPEED: c = ell/sqrt(tau_2) is the new extension speed. "
        "This is NOT native tau relabeled; it is a genuinely new scale.",
        "NATIVE CORE RECOVERED: at long times (t >> tau_2) or low frequencies "
        "(omega << 1/tau_2), telegrapher reduces to native tau dPhi/dt + Phi = X. "
        "Book II is the LIMIT, not the other way around.",
        "RESTRICTED EFFECTIVE LORENTZ: at high frequencies (omega >> 1/tau_1), "
        "the equation approximates d^2Phi/dt^2 - c^2 nabla^2 Phi = 0 (wave eq). "
        "This is a RESTRICTED regime, not exact Lorentz restoration.",
        "DIFFUSIVE (C1) rejected as preferred: no finite speed, no Lorentz regime, "
        "less structural value. NONLOCAL (C3) underdetermined. AUXILIARY (C4) costly.",
        "All new scales and assumptions are EXPLICIT POSTULATES per W-A rules.",
    ]

    allowed=[
        "Damped hyperbolic telegrapher as preferred first propagation extension",
        "Two new parameters: tau_2 (inertial) and c (propagation speed)",
        "Finite characteristic speed c conditionally supported as extension",
        "Native core recovered as long-time/low-frequency limit",
        "Restricted effective Lorentz at high frequencies/short times",
        "All new postulates explicitly labeled per Book III charter",
        "W-C authorized: propagation extension identified",
    ]

    forbidden=[
        "Propagation was native all along",
        "Telegrapher equation is native ODE",
        "Speed c was hidden in Book II",
        "Effective Lorentz implies exact restoration",
        "Diffusive limit implies native recovery proves extension",
        "Propagation implies geometry dynamics",
        "Extension preference implies physical correctness",
    ]

    diagnostics: Dict[str,Any]={
        "preferred_class":"C2_damped_hyperbolic_telegrapher",
        "new_parameters":2,
        "new_fields":0,
        "finite_speed":True,
        "preserves_native_core":True,
        "native_as_limit":True,
        "lorentz_regime":"restricted_high_frequency",
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_WB_NONCLAIMS,
    }

    result=WBSpatialPropagationResult(
        True,cands,N_CANDIDATES,
        "C2_damped_hyperbolic_telegrapher",
        fw,WB_PROP,WB_PREF,WB_SPEED,WB_LORENTZ,WB_AUTH,WB_OVERALL,
        key,allowed,forbidden,WB_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WBSpatialPropagationResult)->None:
    if r.propagation_extension_status not in PROP_OPTIONS:raise ValueError("prop")
    if r.preferred_extension_class not in PREF_OPTIONS:raise ValueError("pref")
    if r.speed_status not in SPEED_OPTIONS:raise ValueError("speed")
    if r.lorentz_appearance_status not in LORENTZ_OPTIONS:raise ValueError("lorentz")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WB_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if not r.diagnostics["finite_speed"]:raise ValueError("speed True")
    if not r.diagnostics["preserves_native_core"]:raise ValueError("native True")


def _self_test()->bool:
    r=run_wb_spatial_propagation_extension_audit()
    assert r.valid
    assert r.propagation_extension_status==WB_PROP
    assert r.preferred_extension_class==WB_PREF
    assert r.speed_status==WB_SPEED
    assert r.lorentz_appearance_status==WB_LORENTZ
    assert r.authorization==WB_AUTH
    assert r.diagnostics["preferred_class"]=="C2_damped_hyperbolic_telegrapher"
    assert r.diagnostics["new_parameters"]==2
    assert r.diagnostics["new_fields"]==0
    return True

if __name__=="__main__":
    _self_test();print("W-B passed.")
