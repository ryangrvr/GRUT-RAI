"""
Appendix U-D --- Effective Kinematics and Characteristic Propagation Audit
==========================================================================
GRUT Unified-Field Program --- Phase U-D

Determines what propagation and kinematic structure is licensed by the
native GRUT scalar dissipative core. No metric, gauge, or wave-equation
language unless actually derived.

=== CORE ANALYSIS ===

Native equation: tau dPhi/dt + Phi = X

This is a FIRST-ORDER-IN-TIME equation. As written, it contains NO spatial
derivatives. Therefore:

1. NATIVE SPATIAL PROPAGATION: ABSENT in the core ODE.
   The equation tau dPhi(x,t)/dt + Phi(x,t) = X(x,t) couples Phi at point x
   only to X at the same point x. Phi at point x does NOT affect Phi at x'.
   There is NO native spatial coupling operator (no nabla^2, no gradient terms).

2. SPATIAL TRANSPORT requires ADDITIONAL STRUCTURE:
   - Diffusion: add -D nabla^2 Phi -> parabolic PDE
   - Wave: add -c^2 nabla^2 Phi + tau d^2Phi/dt^2 -> hyperbolic PDE (telegraph eq)
   - Advection: add -v dot grad Phi -> first-order transport
   All of these are NEW CONSTITUTIVE POSTULATES, not native consequences.

3. WHAT THE NATIVE EQUATION DOES SUPPORT:
   - LOCAL relaxation: Phi(x,t) -> X(x,t) at each point x independently
   - SOURCE TRACKING: if X(x,t) moves spatially, Phi tracks it with lag tau
   - RETARDED RESPONSE: Phi(x,t) = integral of exp(-(t-s)/tau) X(x,s)/tau ds
   The "motion" is entirely in the SOURCE X, not in the field Phi.

4. FINITE SPEED: NO native speed.
   tau is a TIMESCALE, not a speed. tau has dimensions of time; speed has
   dimensions of length/time. Converting tau to a speed requires a length
   scale, which is not natively specified.
   If a length scale L is added (e.g., from Skyrme radius, shell radius, or
   spatial gradient term), then v_eff ~ L/tau is an EFFECTIVE speed.
   But this requires extra structure: it is not native.

5. MEMORY / RETARDATION:
   If a nonlocal kernel K(x-x',t-s) replaces X or the constitutive law,
   then spatial nonlocality CAN introduce effective transport.
   But K must be specified as a NEW POSTULATE; it is not native.
   The Galley CTP retardation is TEMPORAL, not spatial.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_REGIMES: int = 6
N_OBSTRUCTIONS: int = 5
N_UD_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

KIN_OPTIONS = frozenset({
    "local_relaxation_only_natively_supported",
    "local_relaxation_with_conditional_spatial_response",
    "effective_propagation_structure_conditionally_supported",
    "true_native_characteristic_propagation_supported",
})
PROP_OPTIONS = frozenset({
    "no_independent_propagating_mode_licensed",
    "retarded_source_response_dominant",
    "diffusive_or_kernel_smeared_transport_supported",
    "wave_like_or_hyperbolic_regime_conditionally_supported",
})
SPEED_OPTIONS = frozenset({
    "no_native_speed_concept_beyond_rate",
    "finite_speed_requires_extra_constitutive_structure",
    "conditional_effective_speed_supported",
    "native_characteristic_speed_established",
})
MEM_KIN_OPTIONS = frozenset({
    "memory_alters_response_without_new_transport_mode",
    "memory_supports_retarded_nonlocal_response",
    "memory_conditionally_supports_effective_transport",
    "memory_generates_native_propagating_sector",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_UE",
    "stop_for_missing_kinematic_boundary",
})
OVERALL_OPTIONS = frozenset({
    "dissipative_scalar_kinematics_bounded_without_native_wave_structure",
    "retarded_response_kinematics_supported_under_strict_limits",
    "conditional_effective_transport_structure_identified",
    "native_propagation_structure_established",
})

UD_KIN: str = "local_relaxation_only_natively_supported"
UD_PROP: str = "no_independent_propagating_mode_licensed"
UD_SPEED: str = "no_native_speed_concept_beyond_rate"
UD_MEM_KIN: str = "memory_alters_response_without_new_transport_mode"
UD_AUTH: str = "authorized_to_proceed_to_UE"
UD_OVERALL: str = "dissipative_scalar_kinematics_bounded_without_native_wave_structure"

UD_NONCLAIMS: List[str] = [
    "NOT_claiming_local_relaxation_therefore_spatial_propagation__"
    "point_wise_relaxation_involves_no_spatial_coupling",
    "NOT_claiming_source_tracking_therefore_autonomous_transport__"
    "Phi_follows_X_motion_but_Phi_itself_has_no_spatial_dynamics",
    "NOT_claiming_tau_therefore_speed__"
    "tau_has_dimension_time_not_length_per_time",
    "NOT_claiming_retarded_response_therefore_light_cone__"
    "temporal_retardation_is_not_spatial_causal_structure",
    "NOT_claiming_memory_kernel_therefore_wave_propagation__"
    "nonlocal_temporal_response_is_not_hyperbolic_wave_equation",
    "NOT_claiming_effective_speed_without_length_scale__"
    "v_eff_eq_L_over_tau_requires_independent_L",
    "NOT_claiming_kinematic_structure_therefore_geometry__"
    "transport_language_is_not_metric_dynamics",
    "NOT_claiming_absence_of_propagation_therefore_theory_incomplete__"
    "local_relaxation_is_the_native_kinematic_character",
]


@dataclass
class UDTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class UDEvidenceRow:
    regime: str; spatial_propagation: str; prop_type: str
    finite_speed: str; dominant_mechanism: str
    what_licensed: str; what_not_licensed: str

@dataclass
class UDObstruction:
    rank: int; name: str; description: str

@dataclass
class UDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class UDEffectiveKinematicsResult:
    valid: bool
    track_a_local_vs_spatial: UDTrackResult
    track_b_characteristic: UDTrackResult
    track_c_speed: UDTrackResult
    track_d_memory_kin: UDTrackResult
    track_e_forcing: UDTrackResult
    track_f_firewall: UDTrackResult
    evidence_table: List[UDEvidenceRow]
    obstructions: List[UDObstruction]
    nonclaim_firewall: UDNonclaimFirewall
    native_kinematics_status: str; propagation_type_status: str
    finite_speed_status: str; memory_kinematics_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> UDTrackResult:
    return UDTrackResult("A","local_vs_spatial",
        "Does native GRUT support spatial propagation or only local relaxation?",
        [
            "The native ODE tau dPhi(x,t)/dt + Phi(x,t) = X(x,t) contains "
            "NO spatial derivatives. No nabla^2, no gradient, no Laplacian.",
            "Phi at point x is coupled only to X at the SAME point x. "
            "Phi at x does NOT influence Phi at x' for x != x'.",
            "Spatial coupling requires ADDITIONAL constitutive structure: "
            "diffusion (nabla^2), wave (c^2 nabla^2), advection (v*grad).",
            "All such additions are NEW POSTULATES, not native consequences.",
            "Verdict: LOCAL RELAXATION ONLY natively supported.",
        ],
        UD_KIN,
        ["No spatial derivatives in native equation"])


def _track_b() -> UDTrackResult:
    return UDTrackResult("B","characteristic_type",
        "What type of propagation, if any, exists?",
        [
            "Native: no spatial coupling -> no characteristics, no fronts, "
            "no wave cones. Only local exponential relaxation.",
            "If DIFFUSION added (nabla^2 Phi): parabolic, infinite speed smearing.",
            "If WAVE added (c^2 nabla^2 + inertia): telegraph equation, finite "
            "speed c, but this requires second-order time derivative + spatial term.",
            "Native alone: NO independent propagating mode. The field relaxes "
            "locally toward its source; it does not propagate autonomously.",
        ],
        UD_PROP,
        ["No propagation without spatial constitutive additions"])


def _track_c() -> UDTrackResult:
    return UDTrackResult("C","finite_speed",
        "Is any finite speed or causal cone licensed?",
        [
            "tau has dimensions [time]. Speed has dimensions [length/time].",
            "Converting tau to speed requires an INDEPENDENT length scale L.",
            "Candidate lengths: Skyrme radius (MBU), shell radius (Appendix M), "
            "gradient scale. All are extension-level or require new postulates.",
            "v_eff = L/tau would be an effective speed IF L is specified. "
            "But L is not natively specified.",
            "Verdict: NO native speed concept beyond the relaxation rate 1/tau.",
        ],
        UD_SPEED,
        ["tau is timescale, not speed; speed needs length scale"])


def _track_d() -> UDTrackResult:
    return UDTrackResult("D","memory_kinematics",
        "What does memory/retardation do to kinematics?",
        [
            "Native memory (Galley CTP): TEMPORAL retardation. "
            "Phi(t) depends on X(s) for s < t via kernel exp(-(t-s)/tau)/tau.",
            "This is temporal nonlocality, NOT spatial nonlocality.",
            "If a SPATIAL kernel K(x-x') is added: spatial nonlocal response. "
            "But this requires specifying K, which is a NEW POSTULATE.",
            "Native temporal memory does NOT create spatial transport. "
            "It smooths the temporal response but does not move information spatially.",
            "Verdict: memory alters temporal response without new transport mode.",
        ],
        UD_MEM_KIN,
        ["Temporal memory ≠ spatial transport"])


def _track_e() -> UDTrackResult:
    return UDTrackResult("E","forcing_transport",
        "How much kinematic appearance comes from X rather than Phi?",
        [
            "SOURCE TRACKING: if X(x,t) has spatial structure that moves, "
            "Phi(x,t) tracks it with lag tau. The 'motion' is in X, not Phi.",
            "FREE RELAXATION (X=0): Phi -> 0 locally. No spatial structure.",
            "CONSTANT (X=X0): Phi -> X0 locally. No propagation.",
            "MOVING SOURCE: Phi follows source with lag. APPARENT propagation "
            "is source-driven, not autonomous field transport.",
            "When X is removed: ALL spatial structure vanishes. "
            "No autonomous spatial propagation survives.",
        ],
        "source_tracking_not_autonomous_propagation",
        ["'Motion' of Phi is really motion of X"])


def _track_f() -> UDTrackResult:
    return UDTrackResult("F","kinematic_firewall",
        "What language is licensed vs forbidden?",
        [
            "LICENSED: local dissipative relaxation, retarded temporal response, "
            "source tracking with lag tau, relaxation rate 1/tau.",
            "CONDITIONAL: effective speed v_eff = L/tau IF length scale L specified; "
            "spatial transport IF spatial constitutive terms added.",
            "FORBIDDEN without derivation: wave equation, Lorentz cone, metric "
            "propagation, characteristic curves/fronts, gauge-boson transport, "
            "gravitational wave analog, relativistic signal structure.",
        ],
        "firewall_secured",
        ["Strict separation maintained"])


def _build_evidence() -> List[UDEvidenceRow]:
    return [
        UDEvidenceRow("free_relaxation",
            "No (Phi->0 locally)", "None", "No",
            "Exponential decay", "Local relaxation rate 1/tau",
            "Spatial propagation, speed, wave structure"),
        UDEvidenceRow("constant_forcing",
            "No (Phi->X0 locally)", "None", "No",
            "Local attractor", "Steady-state relaxation",
            "Any propagation claim"),
        UDEvidenceRow("spatially_varying_X",
            "Source-imposed only", "Source tracking", "No native speed",
            "Phi follows X(x) pointwise", "Source-driven spatial structure",
            "Autonomous propagation"),
        UDEvidenceRow("moving_source",
            "Apparent (from X motion)", "Source tracking", "Source speed, not field speed",
            "Phi lags moving source by tau", "Retarded source tracking",
            "Autonomous wave propagation"),
        UDEvidenceRow("memory_retardation",
            "No (temporal only)", "Temporal smoothing", "No",
            "Exponential temporal kernel", "Retarded temporal response",
            "Spatial transport from memory alone"),
        UDEvidenceRow("no_source_autonomous",
            "No", "None", "No",
            "Relaxation to zero", "Pure local decay",
            "Any spatial structure without source"),
    ]


def _build_obstructions() -> List[UDObstruction]:
    return [
        UDObstruction(1,"no_spatial_derivatives_in_native_equation",
            "tau dPhi/dt + Phi = X has no nabla^2, no gradient, no spatial coupling"),
        UDObstruction(2,"tau_is_timescale_not_speed",
            "Speed requires length/time; tau provides only time"),
        UDObstruction(3,"memory_is_temporal_not_spatial",
            "Galley CTP and retardation kernels are temporal nonlocality"),
        UDObstruction(4,"source_tracking_is_not_autonomous_transport",
            "Phi follows X; spatial structure vanishes when X is removed"),
        UDObstruction(5,"spatial_structure_requires_new_postulates",
            "Diffusion, wave, advection terms are constitutive additions"),
    ]


def run_ud_effective_kinematics_propagation_audit() -> UDEffectiveKinematicsResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tf=_track_f()
    ev=_build_evidence();obs=_build_obstructions()
    fw=UDNonclaimFirewall(UD_NONCLAIMS,N_UD_NONCLAIMS,True)

    key=[
        "NO NATIVE SPATIAL PROPAGATION: the native ODE has no spatial derivatives. "
        "Phi at x does not influence Phi at x'. Only local temporal relaxation.",
        "NO INDEPENDENT PROPAGATING MODE: without spatial constitutive additions, "
        "the field relaxes locally but does not transport spatially.",
        "NO NATIVE SPEED CONCEPT: tau is timescale [T], not speed [L/T]. "
        "Speed requires an independent length scale (not natively specified).",
        "MEMORY IS TEMPORAL, NOT SPATIAL: retardation kernels smooth temporal "
        "response but do not create spatial transport.",
        "SOURCE TRACKING IS NOT PROPAGATION: Phi follows moving X with lag tau; "
        "apparent spatial structure vanishes when X is removed.",
        "5 kinematic obstructions: no spatial derivatives, tau≠speed, "
        "temporal memory, source tracking, spatial terms need new postulates.",
        "Local dissipative relaxation IS the native kinematic character.",
    ]

    allowed=[
        "Native kinematics: local dissipative relaxation only; Phi relaxes "
        "pointwise toward X with timescale tau",
        "No independent propagating mode in native dynamics",
        "tau is a relaxation rate, not a speed; speed requires length scale L",
        "Memory alters temporal response without creating spatial transport",
        "Source tracking: Phi follows X(x,t) with lag; not autonomous propagation",
        "5 kinematic obstructions documented and ranked",
        "U-E authorized: kinematic boundary established",
    ]

    forbidden=[
        "Local relaxation implies spatial propagation",
        "Source tracking implies autonomous transport",
        "tau implies speed",
        "Retarded response implies light cone",
        "Memory kernel implies wave propagation",
        "Absence of propagation implies theory incomplete",
        "Kinematic structure implies metric dynamics",
    ]

    diagnostics: Dict[str,Any]={
        "native_spatial_derivatives":False,
        "native_speed_concept":False,
        "spatial_memory":False,
        "autonomous_spatial_propagation":False,
        "source_tracking_supported":True,
        "local_relaxation_supported":True,
        "n_obstructions":len(obs),
        "n_regimes":N_REGIMES,
        "n_nonclaims":N_UD_NONCLAIMS,
    }

    result=UDEffectiveKinematicsResult(
        True,ta,tb,tc,td,te,tf,ev,obs,fw,
        UD_KIN,UD_PROP,UD_SPEED,UD_MEM_KIN,UD_AUTH,UD_OVERALL,
        key,allowed,forbidden,UD_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:UDEffectiveKinematicsResult)->None:
    if r.native_kinematics_status not in KIN_OPTIONS:raise ValueError("kin")
    if r.propagation_type_status not in PROP_OPTIONS:raise ValueError("prop")
    if r.finite_speed_status not in SPEED_OPTIONS:raise ValueError("speed")
    if r.memory_kinematics_status not in MEM_KIN_OPTIONS:raise ValueError("mem")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_UD_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_REGIMES:raise ValueError("evidence")
    if len(r.obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["native_spatial_derivatives"]:raise ValueError("spatial must be False")
    if r.diagnostics["native_speed_concept"]:raise ValueError("speed must be False")
    if r.diagnostics["autonomous_spatial_propagation"]:raise ValueError("prop must be False")


def _self_test()->bool:
    r=run_ud_effective_kinematics_propagation_audit()
    assert r.valid
    assert r.native_kinematics_status==UD_KIN
    assert r.propagation_type_status==UD_PROP
    assert r.finite_speed_status==UD_SPEED
    assert r.memory_kinematics_status==UD_MEM_KIN
    assert r.authorization==UD_AUTH
    assert r.diagnostics["local_relaxation_supported"] is True
    assert r.diagnostics["autonomous_spatial_propagation"] is False
    return True

if __name__=="__main__":
    _self_test();print("U-D passed.")
