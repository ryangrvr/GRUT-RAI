"""
Appendix V-D --- Preferred Frame and Rest-State Ontology Audit
===============================================================
GRUT Vacuum Ontology Program --- Phase V-D

Determines the exact ontological and dynamical meaning of the preferred
frame and rest state. Separates substrate frame from matter frame,
constitutive rest from mechanical rest, and field dissipation from drag.

=== CORE ANALYSIS ===

SUBSTRATE FRAME vs MATTER FRAME:
  tau defines the constitutive rest frame of the scalar substrate: the
  frame where tau dPhi/dt + Phi = X takes its canonical form. This is
  the SUBSTRATE'S rest frame — the frame where dissipative relaxation
  is isotropic and the constitutive law is simplest.

  This does NOT automatically define the rest frame for MATTER or PROBES.
  U-F established: no canonized probe dynamics, no derived probe coupling.
  Without a matter-Phi coupling law, the substrate frame imposes nothing
  on matter motion. Matter could move at any velocity relative to the
  substrate frame — we simply have no law saying otherwise.

REST STATE:
  X=0 -> Phi->0: the zero-response constitutive rest state (V-B).
  This is the substrate's rest: the field quiesces. It is NOT universal
  mechanical rest. Nothing in GRUT forces matter to approach Phi=0.

MOVING SOURCE:
  If X(x,t) moves, Phi tracks with lag tau. The field develops a lagged
  wake/trail behind the source. This is CONSTITUTIVE RESPONSE, not drag
  on the source. The source imposes motion; Phi follows passively.
  There is no REACTION force from Phi back on the source (no coupling).

VACUUM DRAG:
  Drag = resistive force on a moving object from the medium. Requires:
  (a) object with canonized dynamics, (b) coupling to Phi, (c) back-reaction.
  ALL THREE are absent. U-F: no probe coupling. U-B: X has no dynamics.
  Drag is NOT licensed. The field dissipates — the source does not slow.

OBSERVABILITY:
  The preferred frame is physically meaningful: tau is a real timescale.
  But operational detection requires measurement apparatus coupled to Phi.
  Without probe dynamics (U-F), observability is CONDITIONAL: in principle
  yes (tau selects a frame), operationally not yet (no measurement law).
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 6
N_VD_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

PF_OPTIONS = frozenset({
    "constitutive_substrate_rest_frame_supported",
    "constitutive_frame_with_conditional_observables",
    "matter_rest_frame_not_licensed",
    "preferred_frame_status_unresolved",
})
RS_OPTIONS = frozenset({
    "zero_response_rest_state_supported_for_substrate",
    "substrate_rest_state_supported_but_matter_rest_unlicensed",
    "universal_rest_state_supported",
    "rest_state_status_unresolved",
})
DRAG_OPTIONS = frozenset({
    "no_vacuum_drag_claim_licensed",
    "phi_tracking_dissipation_only",
    "conditional_probe_drag_requires_new_postulates",
    "universal_vacuum_drag_supported",
})
OBS_OPTIONS = frozenset({
    "constitutive_observability_only",
    "source_tracking_asymmetry_conditionally_observable",
    "direct_rest_frame_observability_supported",
    "observability_not_resolved",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_VE",
    "stop_for_missing_rest_frame_boundary",
})
OVERALL_OPTIONS = frozenset({
    "preferred_rest_frame_is_constitutive_not_mechanical",
    "substrate_rest_state_supported_without_vacuum_drag",
    "rest_frame_ontology_partially_classified_under_strict_limits",
    "absolute_rest_mechanics_not_established",
})

VD_PF: str = "constitutive_substrate_rest_frame_supported"
VD_RS: str = "substrate_rest_state_supported_but_matter_rest_unlicensed"
VD_DRAG: str = "no_vacuum_drag_claim_licensed"
VD_OBS: str = "source_tracking_asymmetry_conditionally_observable"
VD_AUTH: str = "authorized_to_proceed_to_VE"
VD_OVERALL: str = "preferred_rest_frame_is_constitutive_not_mechanical"

VD_NONCLAIMS: List[str] = [
    "NOT_claiming_substrate_frame_therefore_matter_rest__"
    "constitutive_preferred_frame_does_not_define_matter_rest",
    "NOT_claiming_field_dissipation_therefore_drag__"
    "Phi_relaxation_does_not_resist_source_motion",
    "NOT_claiming_lagged_tracking_therefore_force_on_source__"
    "constitutive_wake_is_not_back_reaction",
    "NOT_claiming_preferred_frame_therefore_absolute_space__"
    "constitutive_rest_is_not_Newtonian_absolute_rest",
    "NOT_claiming_zero_response_therefore_universal_rest__"
    "substrate_quiescence_is_not_matter_stasis",
    "NOT_claiming_in_principle_observability_therefore_operational__"
    "tau_frame_selectivity_requires_measurement_apparatus",
    "NOT_claiming_source_tracking_asymmetry_therefore_aether_wind__"
    "wake_structure_is_constitutive_not_mechanical_resistance",
    "NOT_claiming_rest_frame_ontology_therefore_ontology_complete__"
    "V_D_classifies_one_aspect_not_entire_ontology",
]


@dataclass
class VDTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class VDEvidenceRow:
    candidate: str; structurally_supported: str; operationally_licensed: str
    strongest_label: str; what_licensed: str; what_not_licensed: str

@dataclass
class VDObstruction:
    rank: int; name: str; description: str

@dataclass
class VDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class VDPreferredFrameRestStateResult:
    valid: bool
    track_a_substrate_vs_matter: VDTrackResult
    track_b_rest_state: VDTrackResult
    track_c_moving_source: VDTrackResult
    track_d_drag: VDTrackResult
    track_e_observability: VDTrackResult
    track_f_firewall: VDTrackResult
    track_g_obstructions: List[VDObstruction]
    evidence_table: List[VDEvidenceRow]
    nonclaim_firewall: VDNonclaimFirewall
    preferred_frame_status: str; rest_state_status: str
    drag_status: str; observability_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> VDTrackResult:
    return VDTrackResult("A","substrate_vs_matter_frame",
        "Does tau frame define substrate rest or matter rest?",
        ["tau defines SUBSTRATE constitutive rest frame: canonical form of ODE.",
         "No canonized probe dynamics (U-F). No probe-Phi coupling derived.",
         "Without coupling law: substrate frame imposes nothing on matter.",
         "Matter could move at any velocity relative to substrate frame.",
         "SUBSTRATE REST FRAME: supported. MATTER REST FRAME: not licensed."],
        VD_PF, ["Substrate frame only; matter frame requires coupling law"])

def _track_b() -> VDTrackResult:
    return VDTrackResult("B","rest_state_ontology",
        "What does X=0, Phi=0 mean ontologically?",
        ["X=0 -> Phi->0: zero-response constitutive rest (V-B).",
         "This is the SUBSTRATE quiescing. Not universal mechanical rest.",
         "Nothing forces matter to approach Phi=0 or stop moving.",
         "Rest state: substrate only. Matter rest: unlicensed."],
        VD_RS, ["Substrate rest state; matter rest not implied"])

def _track_c() -> VDTrackResult:
    return VDTrackResult("C","moving_source",
        "What does a moving source imply?",
        ["Moving X -> Phi tracks with lag tau: lagged wake/trail behind source.",
         "This is CONSTITUTIVE RESPONSE, not drag on the source.",
         "The source imposes motion; Phi follows passively.",
         "No reaction force from Phi back on source (no coupling, U-F).",
         "Wake is constitutive pattern, not mechanical resistance."],
        "constitutive_tracking_no_back_reaction",
        ["Lagged wake is response, not drag"])

def _track_d() -> VDTrackResult:
    return VDTrackResult("D","vacuum_drag",
        "Is vacuum drag licensed?",
        ["DRAG requires: (a) object with dynamics, (b) coupling to Phi, (c) back-reaction.",
         "ALL THREE absent. U-F: no probe coupling. U-B: X has no dynamics.",
         "The field dissipates energy from the Phi response. The SOURCE does not slow.",
         "No vacuum drag, no inertial energy bleed, no aether wind resistance.",
         "DRAG IS NOT LICENSED."],
        VD_DRAG, ["No drag: no coupling, no back-reaction"])

def _track_e() -> VDTrackResult:
    return VDTrackResult("E","observability",
        "In what sense is the preferred frame observable?",
        ["tau is physical: it sets a real timescale. The frame IS selected.",
         "But: operational detection requires measurement apparatus coupled to Phi.",
         "Source-tracking asymmetry: a moving source creates a wake; this asymmetry "
         "is in principle observable IF you have a way to detect Phi.",
         "Without probe dynamics (U-F): observability is CONDITIONAL.",
         "In principle: yes (tau selects). Operationally: not yet (no measurement law)."],
        VD_OBS, ["Conditional observability via source-tracking asymmetry"])

def _track_f() -> VDTrackResult:
    return VDTrackResult("F","rest_frame_firewall",
        "What does V-D NOT license?",
        ["NOT: matter drag, absolute mechanical rest, aether wind, "
         "inertial energy bleed, universal velocity damping, "
         "Newtonian absolute space.",
         "STRONGEST SAFE: 'constitutive substrate rest frame with "
         "conditional observability via source-tracking asymmetry.'"],
        "firewall_secured",
        ["Constitutive rest ≠ mechanical rest ≠ drag ≠ absolute space"])

def _build_obstructions() -> List[VDObstruction]:
    return [
        VDObstruction(1,"no_canonized_probe_dynamics",
            "No matter/probe response to Phi is canonized (U-F)"),
        VDObstruction(2,"no_derived_coupling",
            "No force law between probes and Phi field (U-F)"),
        VDObstruction(3,"no_spatial_propagation",
            "No native spatial transport for drag to propagate (U-D)"),
        VDObstruction(4,"no_action_hamiltonian",
            "No variational structure to derive back-reaction (U-C)"),
        VDObstruction(5,"external_source_dependence",
            "X is input; no dynamics for source to be dragged"),
        VDObstruction(6,"constitutive_not_mechanical",
            "Substrate description is constitutive, not mechanical"),
    ]

def _build_evidence() -> List[VDEvidenceRow]:
    return [
        VDEvidenceRow("source_free_zero_state",
            "Yes (Phi->0)","Substrate rest only",
            "Constitutive rest state","Substrate quiescence",
            "Matter rest, universal stasis"),
        VDEvidenceRow("moving_source_tracking",
            "Yes (lagged wake)","Conditional (needs Phi detector)",
            "Source-tracking asymmetry","Wake/trail pattern",
            "Drag, back-reaction, aether wind"),
        VDEvidenceRow("substrate_preferred_frame",
            "Yes (tau selects)","Constitutive",
            "Constitutive rest frame","Substrate frame language",
            "Matter frame, absolute space"),
        VDEvidenceRow("matter_probe_rest",
            "Not supported (no coupling)","Not licensed",
            "N/A","Nothing","Any matter rest claim"),
        VDEvidenceRow("vacuum_drag_test",
            "Not supported","Not licensed",
            "N/A","Nothing","Drag, wind, energy bleed"),
        VDEvidenceRow("observability_test",
            "Conditional (in principle)","Via source asymmetry",
            "Conditional observability","In-principle detectability",
            "Operational measurement without apparatus law"),
    ]


def run_vd_preferred_frame_rest_state_audit() -> VDPreferredFrameRestStateResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e();tf=_track_f()
    obs=_build_obstructions();ev=_build_evidence()
    fw=VDNonclaimFirewall(VD_NONCLAIMS,N_VD_NONCLAIMS,True)

    key=[
        "CONSTITUTIVE SUBSTRATE REST FRAME: tau defines the substrate's canonical "
        "rest frame. This does NOT define matter rest (no probe coupling, U-F).",
        "SUBSTRATE REST STATE: X=0 -> Phi->0 is substrate quiescence, not "
        "universal mechanical rest. Nothing forces matter to stop.",
        "NO VACUUM DRAG: drag requires (a) object dynamics, (b) coupling, "
        "(c) back-reaction. All three absent. Field dissipates; source doesn't slow.",
        "MOVING SOURCE: creates lagged wake/trail. This is constitutive response, "
        "not mechanical resistance. No reaction force from Phi back on source.",
        "CONDITIONAL OBSERVABILITY: tau frame is physical and in-principle "
        "detectable via source-tracking asymmetry, but operational measurement "
        "requires apparatus law (not yet canonized).",
        "6 rest-frame obstructions: no probe dynamics, no coupling, no propagation, "
        "no action, source dependence, constitutive not mechanical.",
    ]

    allowed=[
        "Constitutive substrate rest frame: tau defines canonical frame of ODE",
        "Substrate rest state: Phi->0 when X=0 is substrate quiescence",
        "No vacuum drag licensed: no probe coupling, no back-reaction",
        "Moving source creates constitutive lagged wake, not mechanical resistance",
        "Source-tracking asymmetry conditionally observable in principle",
        "6 rest-frame obstructions documented (probe, coupling, propagation, action, source, constitutive)",
        "V-E authorized: rest-frame boundary established",
    ]

    forbidden=[
        "Substrate frame implies matter rest frame",
        "Field dissipation implies vacuum drag",
        "Lagged tracking implies force on source",
        "Preferred frame implies absolute space",
        "Zero response implies universal rest",
        "In-principle observability implies operational detection",
        "Source-tracking asymmetry implies aether wind",
    ]

    diagnostics: Dict[str,Any]={
        "substrate_rest_frame":True,
        "matter_rest_frame":False,
        "vacuum_drag_licensed":False,
        "back_reaction_present":False,
        "observability_conditional":True,
        "probe_dynamics_canonized":False,
        "n_obstructions":len(obs),
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_VD_NONCLAIMS,
    }

    result=VDPreferredFrameRestStateResult(
        True,ta,tb,tc,td,te,tf,obs,ev,fw,
        VD_PF,VD_RS,VD_DRAG,VD_OBS,VD_AUTH,VD_OVERALL,
        key,allowed,forbidden,VD_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:VDPreferredFrameRestStateResult)->None:
    if r.preferred_frame_status not in PF_OPTIONS:raise ValueError("pf")
    if r.rest_state_status not in RS_OPTIONS:raise ValueError("rs")
    if r.drag_status not in DRAG_OPTIONS:raise ValueError("drag")
    if r.observability_status not in OBS_OPTIONS:raise ValueError("obs")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_VD_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_CANDIDATES:raise ValueError("evidence")
    if len(r.track_g_obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["vacuum_drag_licensed"]:raise ValueError("drag False")
    if r.diagnostics["matter_rest_frame"]:raise ValueError("matter False")
    if r.diagnostics["back_reaction_present"]:raise ValueError("back False")


def _self_test()->bool:
    r=run_vd_preferred_frame_rest_state_audit()
    assert r.valid
    assert r.preferred_frame_status==VD_PF
    assert r.rest_state_status==VD_RS
    assert r.drag_status==VD_DRAG
    assert r.observability_status==VD_OBS
    assert r.authorization==VD_AUTH
    assert r.diagnostics["substrate_rest_frame"] is True
    assert r.diagnostics["vacuum_drag_licensed"] is False
    return True

if __name__=="__main__":
    _self_test();print("V-D passed.")
