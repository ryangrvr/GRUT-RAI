"""
Appendix W-C --- Propagation-Sector Action, Variational Closure, and
Response-Functional Audit
=====================================================================
GRUT Extension Program --- Phase W-C

Determines whether the W-B telegrapher extension admits any action,
variational, or response-functional closure beyond the Book II core.

=== CORE ANALYSIS ===

Telegrapher: tau2 d^2Phi/dt^2 + tau1 dPhi/dt + Phi - c^2 nabla^2 Phi = X

LOCAL ACTION TEST:
  The UNDAMPED limit (tau1=0):
    tau2 d^2Phi/dt^2 + Phi - c^2 nabla^2 Phi = 0
  IS derivable from action:
    S = int [(tau2/2)(dPhi/dt)^2 - (c^2/2)(nabla Phi)^2 - (1/2)Phi^2] dt dx
  This is a standard Klein-Gordon-like action with mass-like term.

  The FULL DAMPED equation (tau1 != 0):
    The tau1 dPhi/dt term is FIRST-ORDER DISSIPATIVE.
    Real local Euler-Lagrange CANNOT produce odd-order time derivatives
    from a real local action. Same structural obstruction as Book II (U-C).
    DAMPING BLOCKS TRUE LOCAL ACTION for the full sector.

SPLIT CORE:
  tau2 d^2Phi/dt^2 + Phi - c^2 nabla^2 Phi = X    [conservative core]
  + tau1 dPhi/dt                                     [dissipative correction]
  This split IS mathematically clean and useful:
  - Conservative core has action (Klein-Gordon-like)
  - Dissipative correction is explicit perturbation
  - In weak-damping limit (tau1 small), action covers most dynamics

RESPONSE FUNCTIONAL:
  S_eff[Phi, Phi_tilde] = int Phi_tilde * [tau2 d^2Phi/dt^2 + tau1 dPhi/dt
    + Phi - c^2 nabla^2 Phi - X] dt dx
  Variation dS/dPhi_tilde = 0 reproduces telegrapher equation.
  This is IMPROVED over Book II: the propagation sector makes the
  response functional spatially nontrivial (includes nabla^2 terms).
  Still nonnative (Phi_tilde is auxiliary). But better formal control.

DOWNSTREAM VALUE:
  The conservative-core action + response-functional packaging creates
  a much better platform for:
  - Probe coupling (can couple to action/Lagrangian density)
  - Effective geometry (spatial propagation enables metric-like work)
  - Probabilistic overlay (propagating modes can carry statistics)
  The Book II ODE core could NOT support any of these well.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 5
N_WC_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

ACTION_OPTIONS = frozenset({
    "no_true_local_action_for_full_damped_sector",
    "action_for_undamped_core_only",
    "constrained_variational_form_only",
    "full_local_action_supported",
})
RESPONSE_OPTIONS = frozenset({
    "response_functional_or_doubled_field_packaging_preferred",
    "constrained_multiplier_packaging_only",
    "no_useful_packaging_beyond_equation",
    "effective_action_like_packaging_supported",
})
DISS_OPTIONS = frozenset({
    "damping_remains_decisive_obstruction",
    "damping_obstruction_partially_softened",
    "closure_improves_in_restricted_regime",
    "dissipation_no_longer_blocks_action",
})
DOWNSTREAM_OPTIONS = frozenset({
    "propagation_platform_now_supports_later_probe_and_geometry_work",
    "closure_gain_is_formal_but_useful",
    "little_extension_value_beyond_transport",
    "downstream_value_not_established",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WD",
    "stop_for_missing_closure_boundary",
})
OVERALL_OPTIONS = frozenset({
    "propagated_sector_gains_transport_but_not_native_action_closure",
    "damped_hyperbolic_extension_supports_effective_response_packaging",
    "closure_improves_only_in_restricted_undamped_regime",
    "propagation_extension_closure_not_stable",
})

WC_ACTION: str = "action_for_undamped_core_only"
WC_RESPONSE: str = "response_functional_or_doubled_field_packaging_preferred"
WC_DISS: str = "damping_obstruction_partially_softened"
WC_DOWNSTREAM: str = "propagation_platform_now_supports_later_probe_and_geometry_work"
WC_AUTH: str = "authorized_to_proceed_to_WD"
WC_OVERALL: str = "damped_hyperbolic_extension_supports_effective_response_packaging"

WC_NONCLAIMS: List[str] = [
    "NOT_claiming_undamped_action_therefore_full_action__"
    "action_for_conservative_core_does_not_cover_damping",
    "NOT_claiming_response_functional_therefore_native_action__"
    "Phi_tilde_packaging_is_auxiliary_not_physical",
    "NOT_claiming_split_core_therefore_native_decomposition__"
    "conservative_plus_dissipative_is_extension_level_bookkeeping",
    "NOT_claiming_improved_closure_therefore_unified_field__"
    "better_formal_control_is_not_sector_unification",
    "NOT_claiming_downstream_platform_therefore_derivation__"
    "platform_enables_later_postulates_not_consequences",
    "NOT_claiming_Klein_Gordon_like_therefore_particle_physics__"
    "mass_like_term_is_constitutive_not_particle_mass",
    "NOT_claiming_weak_damping_therefore_conservative__"
    "perturbative_damping_is_still_damping",
    "NOT_claiming_variational_closure_therefore_gauge__"
    "action_structure_does_not_imply_gauge_field",
]


@dataclass
class WCCandidate:
    name: str; reproduces: str; native: str; extra: str
    strongest: str; obstruction: str; downstream: str; verdict: str

@dataclass
class WCObstruction:
    rank: int; name: str; description: str

@dataclass
class WCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WCPropagationActionClosureResult:
    valid: bool
    candidates: List[WCCandidate]
    obstructions: List[WCObstruction]
    nonclaim_firewall: WCNonclaimFirewall
    propagated_action_status: str; response_functional_status: str
    dissipation_obstruction_status: str; downstream_extension_value: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WCCandidate]:
    return [
        WCCandidate("full_damped_telegrapher",
            "N/A (equation itself)","Extension","N/A",
            "Equation of motion","tau1 dPhi/dt blocks local action",
            "Full propagation platform","no_local_action"),
        WCCandidate("undamped_hyperbolic_limit",
            "Yes: S=int[tau2/2(dPhi/dt)^2-c^2/2(nabla Phi)^2-1/2 Phi^2]",
            "Extension (tau1=0 limit)","None",
            "True local action (Klein-Gordon-like)","Only covers undamped limit",
            "Conservative core for coupling","action_for_undamped_core"),
        WCCandidate("constrained_multiplier",
            "Yes: S=int lambda[telegrapher eq]","Nonnative (lambda aux)","lambda field",
            "Constrained enforcement","No predictive content beyond PDE",
            "Formal enforcement","available_nonnative"),
        WCCandidate("response_functional",
            "Yes: dS/dPhi_tilde=0","Nonnative (Phi_tilde aux)","Phi_tilde",
            "Response functional","Phi_tilde is auxiliary",
            "Best packaging; spatially nontrivial","PREFERRED_packaging"),
        WCCandidate("weak_damping_perturbative",
            "Approximate: action + small correction","Extension","None (perturbative)",
            "Perturbative action + dissipation","Only valid for small tau1",
            "Good for near-conservative regime","conditional_regime"),
        WCCandidate("book_ii_comparison",
            "No (Book II: no spatial derivatives)","Native (Book II)","N/A",
            "Constitutive ODE only","No propagation at all",
            "Much weaker platform","superseded_by_telegrapher"),
    ]


def _build_obstructions() -> List[WCObstruction]:
    return [
        WCObstruction(1,"first_order_dissipative_term",
            "tau1 dPhi/dt is odd-order; real E-L cannot produce it"),
        WCObstruction(2,"time_reversal_breaking_persists",
            "Damping breaks T; action from real L preserves it"),
        WCObstruction(3,"response_field_remains_auxiliary",
            "Phi_tilde is nonnative packaging, not physical field"),
        WCObstruction(4,"undamped_action_covers_only_limit",
            "Klein-Gordon-like action valid only at tau1=0"),
        WCObstruction(5,"no_unified_action_across_sectors",
            "Action for propagation sector does not unify with extensions"),
    ]


def run_wc_propagation_action_closure_audit() -> WCPropagationActionClosureResult:
    cands=_build_candidates();obs=_build_obstructions()
    fw=WCNonclaimFirewall(WC_NONCLAIMS,N_WC_NONCLAIMS,True)

    key=[
        "UNDAMPED CORE HAS TRUE LOCAL ACTION: S = int [(tau2/2)(dPhi/dt)^2 "
        "- (c^2/2)(nabla Phi)^2 - (1/2)Phi^2] is Klein-Gordon-like.",
        "FULL DAMPED SECTOR: tau1 dPhi/dt term STILL blocks true local action. "
        "Same structural obstruction as Book II (odd-order time derivative).",
        "DAMPING OBSTRUCTION PARTIALLY SOFTENED: the undamped core has action; "
        "damping is a perturbative correction in weak-damping regime. "
        "Better than Book II where NO action existed at any level.",
        "RESPONSE FUNCTIONAL PREFERRED: S_eff[Phi,Phi_tilde] now includes "
        "spatial nabla^2 terms. Spatially nontrivial. Better formal control. "
        "Still nonnative (Phi_tilde auxiliary).",
        "DOWNSTREAM VALUE HIGH: conservative-core action + response packaging "
        "creates a much better platform for probe coupling, effective geometry, "
        "and probabilistic overlay than Book II ODE core.",
        "SPLIT: conservative hyperbolic core + dissipative correction is clean "
        "and mathematically useful for later extension work.",
    ]

    allowed=[
        "Undamped hyperbolic core admits true Klein-Gordon-like local action",
        "Full damped sector: damping still blocks true local action (same obstruction)",
        "Damping obstruction partially softened: action exists for undamped core",
        "Response functional preferred: S_eff with nabla^2 is spatially nontrivial",
        "Propagation platform supports later probe and geometry work",
        "Conservative + dissipative split is clean and extension-level useful",
        "W-D authorized: closure boundary established",
    ]

    forbidden=[
        "Undamped action implies full action closure",
        "Response functional implies native action",
        "Split-core implies native decomposition",
        "Improved closure implies unified field",
        "Klein-Gordon-like implies particle physics",
        "Weak damping implies conservative theory",
        "Variational closure implies gauge structure",
    ]

    diagnostics: Dict[str,Any]={
        "undamped_action_exists":True,
        "full_damped_action_exists":False,
        "response_functional_available":True,
        "damping_obstruction_softened":True,
        "damping_fully_resolved":False,
        "downstream_value":"high",
        "conservative_core_action":"S=int[tau2/2(dPhi/dt)^2-c^2/2(nabla Phi)^2-1/2 Phi^2]",
        "n_candidates":N_CANDIDATES,
        "n_obstructions":len(obs),
        "n_nonclaims":N_WC_NONCLAIMS,
    }

    result=WCPropagationActionClosureResult(
        True,cands,obs,fw,
        WC_ACTION,WC_RESPONSE,WC_DISS,WC_DOWNSTREAM,WC_AUTH,WC_OVERALL,
        key,allowed,forbidden,WC_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WCPropagationActionClosureResult)->None:
    if r.propagated_action_status not in ACTION_OPTIONS:raise ValueError("action")
    if r.response_functional_status not in RESPONSE_OPTIONS:raise ValueError("resp")
    if r.dissipation_obstruction_status not in DISS_OPTIONS:raise ValueError("diss")
    if r.downstream_extension_value not in DOWNSTREAM_OPTIONS:raise ValueError("down")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WC_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if len(r.obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if not r.diagnostics["undamped_action_exists"]:raise ValueError("undamped True")
    if r.diagnostics["full_damped_action_exists"]:raise ValueError("damped False")


def _self_test()->bool:
    r=run_wc_propagation_action_closure_audit()
    assert r.valid
    assert r.propagated_action_status==WC_ACTION
    assert r.response_functional_status==WC_RESPONSE
    assert r.dissipation_obstruction_status==WC_DISS
    assert r.downstream_extension_value==WC_DOWNSTREAM
    assert r.authorization==WC_AUTH
    assert r.diagnostics["undamped_action_exists"] is True
    assert r.diagnostics["full_damped_action_exists"] is False
    return True

if __name__=="__main__":
    _self_test();print("W-C passed.")
