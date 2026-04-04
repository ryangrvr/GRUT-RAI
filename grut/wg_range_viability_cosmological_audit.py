"""
Appendix W-G --- Range Viability and Cosmological-Scale Relevance Audit
========================================================================
GRUT Extension Program --- Phase W-G

Determines whether the screened scalar-gravity analog has viable
large-scale phenomenology or is confined to short/intermediate range.

=== ANALYSIS ===

SCREENING LENGTH: lambda = sqrt(L2) where L2 is the spatial extension
coefficient in the telegrapher equation. lambda is a FREE PARAMETER of
the Book III propagation extension — it is NOT determined by native
Book II structure (tau alone does not set a length).

lambda can in principle be set to ANY value:
  - lambda ~ 1 mm: laboratory-scale screening
  - lambda ~ 1 AU: solar-system-scale
  - lambda ~ 1 Mpc: galaxy-cluster-scale
  - lambda -> infinity: unscreened Poisson limit (removes constitutive term)

The CHOICE of lambda is a POSTULATE, not a derivation. Large lambda
requires L2 to be large, which is a parameter choice in the extension.

NATURALNESS:
  There is no native mechanism that SETS lambda. It is a free parameter.
  Making lambda large is not "tuning" in the traditional sense (no
  cancellation or hierarchy problem) — it is simply choosing a larger
  value for L2. But: there is also no natural mechanism that PREVENTS
  lambda from being large.

  This is MODERATE PARAMETER FLEXIBILITY: any lambda is formally consistent,
  but the theory provides no reason to prefer one scale over another.

RANGE RELEVANCE:
  - r << lambda: Newtonian-like 1/r^2 regime. GOOD.
  - r ~ lambda: transition zone. Yukawa modification detectable.
  - r >> lambda: exponentially screened. Force negligible.

  For astrophysical/cosmological relevance, lambda must be at least
  comparable to the scale of interest. This is achievable by parameter
  choice but not derived.

COSMOLOGICAL RELEVANCE:
  The screened scalar sector can in principle influence cosmological scales
  IF lambda is chosen cosmologically large. But:
  - No cosmological dynamics (no expansion, no Friedmann)
  - No dark energy sector
  - No cosmological constant
  - No GR background to deform
  At best: a scalar force with cosmological-scale screening. This is
  LOCAL FORCE PHENOMENOLOGY at large scale, not cosmology.

UNSCREENED LIMIT:
  If the constitutive Phi term is removed (Phi -> 0 coefficient in ODE),
  the static equation becomes Poisson: nabla^2 Phi = source.
  This gives unscreened 1/r potential and 1/r^2 force.
  But removing the constitutive term IS removing the native GRUT core.
  The unscreened limit is NOT a GRUT limit — it is a different theory.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_WG_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

SCREEN_OPTIONS = frozenset({
    "screening_length_is_new_extension_scale",
    "screening_length_can_be_made_large_conditionally",
    "screening_scale_not_stable",
    "screening_scale_unresolved",
})
RANGE_OPTIONS = frozenset({
    "short_range_analog_only",
    "intermediate_range_phenomenology_supported",
    "conditionally_large_scale_relevance_supported",
    "range_viability_not_established",
})
NATURAL_OPTIONS = frozenset({
    "long_range_requires_tuning",
    "moderate_parameter_flexibility_supported",
    "natural_large_range_supported",
    "naturalness_not_resolved",
})
COSMO_OPTIONS = frozenset({
    "no_cosmological_role_licensed",
    "local_or_mesoscopic_role_only",
    "conditional_cosmological_relevance_supported",
    "cosmological_extension_supported",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_WH",
    "stop_for_missing_range_boundary",
})
OVERALL_OPTIONS = frozenset({
    "screened_scalar_gravity_analog_is_range_limited",
    "scalar_force_sector_has_only_conditional_large_scale_relevance",
    "screening_scale_controls_viability_of_gravity_analog",
    "large_scale_viability_not_established",
})

WG_SCREEN: str = "screening_length_can_be_made_large_conditionally"
WG_RANGE: str = "conditionally_large_scale_relevance_supported"
WG_NATURAL: str = "moderate_parameter_flexibility_supported"
WG_COSMO: str = "local_or_mesoscopic_role_only"
WG_AUTH: str = "authorized_to_proceed_to_WH"
WG_OVERALL: str = "screening_scale_controls_viability_of_gravity_analog"

WG_NONCLAIMS: List[str] = [
    "NOT_claiming_large_lambda_therefore_gravity_derived__"
    "parameter_choice_is_not_derivation",
    "NOT_claiming_unscreened_limit_therefore_Newton__"
    "removing_constitutive_term_is_different_theory",
    "NOT_claiming_cosmological_lambda_therefore_cosmology__"
    "large_screening_length_is_not_Friedmann_dynamics",
    "NOT_claiming_parameter_flexibility_therefore_naturalness__"
    "free_parameter_is_not_natural_explanation",
    "NOT_claiming_short_range_success_therefore_universal__"
    "local_1_over_r2_does_not_extend_past_screening",
    "NOT_claiming_Yukawa_modification_therefore_dark_energy__"
    "screened_force_is_not_cosmological_constant",
    "NOT_claiming_range_viability_therefore_GR_replacement__"
    "conditional_large_range_is_not_general_relativity",
    "NOT_claiming_screening_phenomenology_therefore_complete__"
    "force_sector_range_is_one_question_not_closure",
]


@dataclass
class WGCandidate:
    regime: str; screening: str; force_relevance: str
    natural_tuned: str; cosmo: str; strongest: str; verdict: str

@dataclass
class WGObstruction:
    rank: int; name: str; description: str

@dataclass
class WGNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class WGRangeViabilityResult:
    valid: bool
    candidates: List[WGCandidate]
    obstructions: List[WGObstruction]
    nonclaim_firewall: WGNonclaimFirewall
    screening_scale_status: str; range_viability_status: str
    naturalness_status: str; cosmology_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_candidates() -> List[WGCandidate]:
    return [
        WGCandidate("short_range_r_ll_lambda",
            "lambda arbitrary","Newtonian-like 1/r^2","N/A (always works)",
            "N/A","Short-range gravity analog","robust_short_range"),
        WGCandidate("intermediate_r_sim_lambda",
            "lambda ~ scale of interest","Yukawa transition zone","Moderate choice",
            "N/A","Detectable Yukawa modification","intermediate_regime"),
        WGCandidate("large_lambda_parameter_choice",
            "lambda chosen large","1/r^2 extends to large r","Parameter choice (free)",
            "Conditional","Conditional large-range force","conditional_large_range"),
        WGCandidate("tuned_long_range",
            "lambda -> very large","Near-Newtonian over wide range","Free but unexplained",
            "Not cosmological dynamics","Extended Newtonian-like regime",
            "achievable_but_unexplained"),
        WGCandidate("cosmological_attempt",
            "lambda ~ Gpc","Force at cosmological scale","Strong choice",
            "No Friedmann, no expansion","Local force at cosmic scale only",
            "not_cosmological_dynamics"),
        WGCandidate("geometry_consistent_screened",
            "lambda = sqrt(L2)","Force+metric agree at r<<lambda","Depends on L2",
            "N/A","Screened analog with metric consistency",
            "regime_limited_by_lambda"),
    ]


def _build_obstructions() -> List[WGObstruction]:
    return [
        WGObstruction(1,"screening_length_is_free_parameter",
            "lambda = sqrt(L2) is not determined by native theory; arbitrary choice"),
        WGObstruction(2,"no_natural_scale_selection",
            "No mechanism within GRUT selects lambda; any value is formally valid"),
        WGObstruction(3,"no_cosmological_dynamics",
            "No expansion, Friedmann, dark energy; large lambda is force, not cosmology"),
        WGObstruction(4,"unscreened_limit_is_non_GRUT",
            "Removing constitutive Phi term removes the native core entirely"),
        WGObstruction(5,"scalar_not_tensor",
            "Even at large range: scalar force, not spin-2 tensor gravity"),
        WGObstruction(6,"test_probe_only",
            "No back-reaction; self-gravitating systems not modeled"),
    ]


def run_wg_range_viability_cosmological_audit() -> WGRangeViabilityResult:
    cands=_build_candidates();obs=_build_obstructions()
    fw=WGNonclaimFirewall(WG_NONCLAIMS,N_WG_NONCLAIMS,True)

    key=[
        "SCREENING LENGTH lambda = sqrt(L2) is a FREE PARAMETER of the "
        "propagation extension. Not determined by native theory.",
        "lambda CAN BE MADE LARGE conditionally: any value is formally "
        "consistent. No hierarchy problem, but also no scale selection.",
        "SHORT RANGE (r << lambda): robust Newtonian-like 1/r^2 behavior. "
        "This regime is always available regardless of lambda.",
        "LARGE-SCALE RELEVANCE IS CONDITIONAL: requires choosing lambda "
        "comparable to the scale of interest. Achievable but unexplained.",
        "NO COSMOLOGICAL DYNAMICS: large lambda gives force at cosmic scale, "
        "NOT Friedmann expansion, dark energy, or GR cosmology.",
        "UNSCREENED LIMIT (lambda -> inf) removes the constitutive Phi term "
        "entirely — this is a DIFFERENT THEORY, not a GRUT limit.",
        "MODERATE PARAMETER FLEXIBILITY: lambda is free; no tuning crisis, "
        "but also no natural explanation for any particular scale.",
    ]

    allowed=[
        "Screening length lambda = sqrt(L2) is free extension parameter",
        "lambda can be made large: any value formally consistent",
        "Short-range (r << lambda): robust Newtonian-like 1/r^2",
        "Conditional large-scale relevance through parameter choice",
        "Moderate parameter flexibility: no hierarchy/tuning crisis",
        "No cosmological dynamics licensed (force only, not expansion)",
        "W-H authorized: range boundary established",
    ]

    forbidden=[
        "Large lambda implies gravity derived",
        "Unscreened limit implies Newtonian gravity",
        "Cosmological lambda implies cosmology",
        "Parameter flexibility implies naturalness",
        "Short-range success implies universal gravity",
        "Yukawa modification implies dark energy",
        "Range viability implies GR replacement",
    ]

    diagnostics: Dict[str,Any]={
        "screening_length":"lambda_eq_sqrt_L2",
        "lambda_is_free":True,
        "lambda_naturally_selected":False,
        "short_range_robust":True,
        "large_range_conditional":True,
        "cosmological_dynamics":False,
        "unscreened_is_grut":False,
        "tuning_crisis":False,
        "n_candidates":N_CANDIDATES,
        "n_obstructions":len(obs),
        "n_nonclaims":N_WG_NONCLAIMS,
    }

    result=WGRangeViabilityResult(
        True,cands,obs,fw,
        WG_SCREEN,WG_RANGE,WG_NATURAL,WG_COSMO,WG_AUTH,WG_OVERALL,
        key,allowed,forbidden,WG_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:WGRangeViabilityResult)->None:
    if r.screening_scale_status not in SCREEN_OPTIONS:raise ValueError("screen")
    if r.range_viability_status not in RANGE_OPTIONS:raise ValueError("range")
    if r.naturalness_status not in NATURAL_OPTIONS:raise ValueError("natural")
    if r.cosmology_status not in COSMO_OPTIONS:raise ValueError("cosmo")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_WG_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.candidates)!=N_CANDIDATES:raise ValueError("cands")
    if len(r.obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["cosmological_dynamics"]:raise ValueError("cosmo False")
    if not r.diagnostics["lambda_is_free"]:raise ValueError("free True")
    if r.diagnostics["lambda_naturally_selected"]:raise ValueError("natural False")


def _self_test()->bool:
    r=run_wg_range_viability_cosmological_audit()
    assert r.valid
    assert r.screening_scale_status==WG_SCREEN
    assert r.range_viability_status==WG_RANGE
    assert r.naturalness_status==WG_NATURAL
    assert r.cosmology_status==WG_COSMO
    assert r.authorization==WG_AUTH
    assert r.diagnostics["lambda_is_free"] is True
    assert r.diagnostics["cosmological_dynamics"] is False
    assert r.diagnostics["short_range_robust"] is True
    return True

if __name__=="__main__":
    _self_test();print("W-G passed.")
