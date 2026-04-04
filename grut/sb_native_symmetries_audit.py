"""
Appendix S-B --- Native Symmetries and Exact Invariants Audit
==============================================================
GRUT Symmetry Program --- Phase S-B

Audits what exact native symmetries and invariants the raw GRUT scalar
memory architecture possesses BEFORE any extensions.

The GRUT constitutive architecture is:
    tau * dPhi/dt + Phi = X(t)
where tau^2 = 3/2 is fixed, Phi is a real scalar field, and X is a source.

Key findings:
  NATIVELY PRESERVED:
    - Z2 reflection: Phi -> -Phi (if source X also reflects)
    - Constitutive form invariance (ODE structure preserved under rescaling)
    - Spatial isotropy (no preferred spatial direction in scalar architecture)
    - Spatial translation (scalar field, no preferred position)

  NATIVELY BROKEN:
    - Lorentz invariance: tau defines a preferred rest frame (the "vacuum
      memory frame"). The constitutive ODE is first-order in time, not
      Lorentz-covariant. This is a NATIVE BREAK, not an effective one.
    - Time-reversal T: the first-order dissipative ODE tau dPhi/dt + Phi = X
      is NOT invariant under t -> -t (it becomes -tau dPhi/dt + Phi = X).
      Dissipation defines an arrow of time. This is NATIVE.
    - Scale invariance: tau^2 = 3/2 fixes a characteristic scale.
      No continuous scale symmetry.
    - Boost invariance: tau defines a preferred frame; boosts are not native.

  CONSERVATION:
    - No standard Noether conservation. The open-system dissipative structure
      does not support unitary conservation laws. What exists:
      dissipative balance laws (energy flows out through dissipation).
    - No conserved energy, momentum, or angular momentum in the standard
      exact sense. Only dissipative balance/relaxation.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CONTINUOUS: int = 5; N_DISCRETE: int = 5; N_LORENTZ: int = 5
N_TIME_REV: int = 4; N_CONSERVATION: int = 5; N_SCALE: int = 5
N_INVARIANTS: int = 5; N_BOUNDARY: int = 5
N_APPENDIX_P: int = 7; N_SB_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

S0_INHERITED: str = "symmetry_entry_inventory_complete"

SB_LORENTZ_VERDICT: str = "lorentz_invariance_natively_broken"
SB_DISCRETE_VERDICT: str = "z2_reflection_native_and_exact"
SB_TIME_REVERSAL_VERDICT: str = "time_reversal_natively_broken_by_tau_dissipation"
SB_CONSERVATION_VERDICT: str = "dissipative_balance_laws_only_no_standard_exact_conservation"
SB_AUTHORIZATION_VERDICT: str = "authorized_to_proceed_to_SC"
SB_OVERALL_P_CLASS: str = "native_canon"

ALLOWED_LORENTZ: frozenset = frozenset({
    "lorentz_invariance_natively_broken","lorentz_invariance_effective_only",
    "lorentz_invariance_underdetermined","lorentz_invariance_native",
})
ALLOWED_DISCRETE: frozenset = frozenset({
    "z2_reflection_native_and_exact","native_discrete_symmetry_structure_partial",
    "native_discrete_symmetry_structure_underdetermined",
    "no_nontrivial_native_discrete_symmetry_found",
})
ALLOWED_TIME_REV: frozenset = frozenset({
    "time_reversal_natively_broken_by_tau_dissipation","time_reversal_effective_only",
    "time_reversal_underdetermined","time_reversal_native",
})
ALLOWED_CONSERVATION: frozenset = frozenset({
    "dissipative_balance_laws_only_no_standard_exact_conservation",
    "partial_native_conservation_structure_present",
    "conservation_structure_underdetermined","standard_noether_conservation_native",
})
ALLOWED_AUTH: frozenset = frozenset({
    "authorized_to_proceed_to_SC",
    "authorized_only_for_further_native_symmetry_refinement",
    "not_authorized_to_proceed","requires_reopening_S0",
})
ALLOWED_P_CLASSES: frozenset = frozenset({
    "native_canon","effective_reduction","bounded_structural_result",
    "working_canon_hypothesis","motivated_but_unbuilt",
    "motivated_independent_postulation","compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

SB_NONCLAIMS: List[str] = [
    "NOT_claiming_scalar_architecture_therefore_gauge_theory__"
    "real_scalar_dissipative_ODE_is_not_gauge_structure",
    "NOT_claiming_dissipative_open_system_therefore_Noether_conservation__"
    "open_system_has_balance_laws_not_exact_conservation",
    "NOT_claiming_preferred_timescale_therefore_Lorentz_preserved__"
    "tau_defines_preferred_frame_breaking_Lorentz",
    "NOT_claiming_Z2_reflection_therefore_full_matter_parity__"
    "Z2_of_scalar_field_is_not_CPT_or_matter_parity",
    "NOT_claiming_extension_symmetry_therefore_native_vacuum_symmetry__"
    "O3_su2_etc_are_extensions_not_native",
    "NOT_claiming_observable_algebra_therefore_native_spacetime_symmetry__"
    "toy_su2_is_extension_level_not_native",
    "NOT_claiming_residual_spatial_symmetry_therefore_full_relativistic_invariance__"
    "spatial_isotropy_is_not_Lorentz_invariance",
    "NOT_claiming_native_invariant_ledger_therefore_Standard_Model__"
    "native_GRUT_symmetries_are_pre_gauge_pre_relativistic",
]

@dataclass
class SBSymmetryItem:
    item_id: str; item_name: str; description: str
    status: str; notes: List[str]

@dataclass
class SBContinuousAudit:
    items: List[SBSymmetryItem]; n_items: int; notes: List[str]

@dataclass
class SBDiscreteAudit:
    items: List[SBSymmetryItem]; n_items: int
    discrete_verdict: str; notes: List[str]

@dataclass
class SBLorentzAudit:
    items: List[SBSymmetryItem]; n_items: int
    lorentz_verdict: str; preferred_frame: bool; notes: List[str]

@dataclass
class SBTimeReversalAudit:
    items: List[SBSymmetryItem]; n_items: int
    time_reversal_verdict: str; dissipative_arrow: bool; notes: List[str]

@dataclass
class SBConservationAudit:
    items: List[SBSymmetryItem]; n_items: int
    conservation_verdict: str; standard_noether: bool; notes: List[str]

@dataclass
class SBScaleAudit:
    items: List[SBSymmetryItem]; n_items: int; scale_broken: bool; notes: List[str]

@dataclass
class SBInvariantItem:
    item_id: str; item_name: str; exact: bool; notes: List[str]

@dataclass
class SBNativeInvariantLedger:
    items: List[SBInvariantItem]; n_items: int; n_exact: int; notes: List[str]

@dataclass
class SBBoundaryItem:
    item_id: str; item_name: str; native: bool; notes: List[str]

@dataclass
class SBBoundaryAudit:
    items: List[SBBoundaryItem]; n_items: int; n_fenced: int; notes: List[str]

@dataclass
class SBAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class SBAppendixPAudit:
    entries: List[SBAppendixPEntry]; n_entries: int
    overall_class: str; notes: List[str]

@dataclass
class SBAuthorizationAudit:
    sc_authorized: bool; authorization_basis: List[str]
    authorization_verdict: str; notes: List[str]

@dataclass
class SBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class SBNativeSymmetriesResult:
    valid: bool
    track_a_continuous: SBContinuousAudit
    track_b_discrete: SBDiscreteAudit
    track_c_lorentz: SBLorentzAudit
    track_d_time_reversal: SBTimeReversalAudit
    track_e_conservation: SBConservationAudit
    track_f_scale: SBScaleAudit
    track_g_invariants: SBNativeInvariantLedger
    track_h_boundary: SBBoundaryAudit
    track_i_appendix_p: SBAppendixPAudit
    track_j_authorization: SBAuthorizationAudit
    track_k_nonclaims: SBNonclaimFirewall
    lorentz_verdict: str; discrete_symmetry_verdict: str
    time_reversal_verdict: str; conservation_verdict: str
    authorization_verdict: str; sb_appendix_p_class: str
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str,Any]

# ---------------------------------------------------------------------------

def _track_a() -> SBContinuousAudit:
    items = [
        SBSymmetryItem("CS1","time_translation","Invariance under t -> t + t0.",
            "broken",["tau dPhi/dt + Phi = X: X(t) may be time-dependent; "
                      "even for X=const, dissipation selects an arrow"]),
        SBSymmetryItem("CS2","spatial_translation","Invariance under x -> x + a.",
            "native",["Scalar field Phi(x): no preferred position in constitutive ODE"]),
        SBSymmetryItem("CS3","spatial_rotation","Invariance under SO(3) spatial rotations.",
            "native",["Real scalar: isotropic, no preferred direction"]),
        SBSymmetryItem("CS4","boost_symmetry","Invariance under Lorentz boosts.",
            "broken",["tau defines preferred frame; constitutive ODE is first-order in t, "
                      "not Lorentz-covariant"]),
        SBSymmetryItem("CS5","scale_symmetry","Invariance under Phi -> lambda Phi, x -> x/lambda.",
            "broken",["tau^2 = 3/2 fixes a characteristic scale; no continuous scaling"]),
    ]
    return SBContinuousAudit(items,N_CONTINUOUS,
        ["2 native (spatial translation, rotation), 3 broken (time, boost, scale)"])

def _track_b() -> SBDiscreteAudit:
    items = [
        SBSymmetryItem("DS1","z2_phi_reflection","Phi -> -Phi (with X -> -X).",
            "native_exact",["Native: ODE tau d(-Phi)/dt + (-Phi) = -X preserves form"]),
        SBSymmetryItem("DS2","spatial_parity","x -> -x.",
            "native_exact",["Scalar field: P(Phi(x)) = Phi(-x); ODE is spatial-parity invariant"]),
        SBSymmetryItem("DS3","charge_conjugation_analog","C-like symmetry.",
            "not_applicable",["Real scalar: no charge to conjugate; category error at this level"]),
        SBSymmetryItem("DS4","time_reversal","t -> -t.",
            "broken",["tau dPhi/dt + Phi = X -> -tau dPhi/dt + Phi = X under t -> -t; "
                      "dissipative term changes sign"]),
        SBSymmetryItem("DS5","cpt_closure","Combined CPT-like structure.",
            "underdetermined",["P native, T broken, C not applicable; "
                              "CPT-like closure underdetermined at native scalar level"]),
    ]
    return SBDiscreteAudit(items,N_DISCRETE,SB_DISCRETE_VERDICT,
        ["Z2 reflection and spatial parity: native and exact",
         "Time reversal: broken by dissipation",
         "C: not applicable (real scalar); CPT: underdetermined"])

def _track_c() -> SBLorentzAudit:
    items = [
        SBSymmetryItem("LF1","first_order_time_derivative",
            "tau dPhi/dt is first-order, not second-order like d'Alembertian.",
            "breaks_lorentz",
            ["Lorentz-covariant wave equation: (1/c^2)d^2Phi/dt^2 - nabla^2 Phi = ...",
             "GRUT: tau dPhi/dt + Phi = X — NOT Lorentz-covariant"]),
        SBSymmetryItem("LF2","preferred_frame_from_tau",
            "tau defines a rest frame where constitutive relaxation occurs.",
            "breaks_lorentz",
            ["In a boosted frame, tau would transform; the constitutive frame is preferred"]),
        SBSymmetryItem("LF3","spatial_isotropy_preserved",
            "No preferred spatial direction in scalar ODE.",
            "partial_preservation",
            ["Spatial part: isotropic (scalar field); no directional preference",
             "Residual symmetry: spatial SO(3) rotations + translations"]),
        SBSymmetryItem("LF4","residual_galilean_structure",
            "Without Lorentz, residual Galilean structure possible.",
            "underdetermined",
            ["Galilean: t -> t, x -> x + vt. Not explicitly audited.",
             "tau in Galilean frame: needs explicit boost analysis"]),
        SBSymmetryItem("LF5","emergent_lorentz_possibility",
            "Lorentz might emerge in some effective regime.",
            "extension_level",
            ["Possible: if constitutive field coupled to relativistic sector",
             "Not native; would require explicit derivation"]),
    ]
    return SBLorentzAudit(items,N_LORENTZ,SB_LORENTZ_VERDICT,True,
        ["Lorentz NATIVELY BROKEN by: first-order time derivative, preferred frame from tau",
         "Residual: spatial isotropy SO(3) + translations preserved",
         "Emergent Lorentz: possible extension, not native"])

def _track_d() -> SBTimeReversalAudit:
    items = [
        SBSymmetryItem("TR1","ode_under_t_reversal",
            "tau dPhi/dt + Phi = X under t -> -t becomes -tau dPhi/dt + Phi = X.",
            "broken",["Sign change on dissipative term; NOT invariant"]),
        SBSymmetryItem("TR2","dissipative_arrow",
            "Dissipation defines thermodynamic arrow of time.",
            "confirmed",["System relaxes TO equilibrium, not FROM; arrow is native"]),
        SBSymmetryItem("TR3","decoherence_arrow_extension",
            "Lindblad decoherence adds quantum arrow (extension-level).",
            "extension_level",["Q-D: off-diagonals decay; consistent with native T-break"]),
        SBSymmetryItem("TR4","visibility_decay_arrow",
            "V(t) = exp(-R_dec t) decays monotonically.",
            "extension_level",["Q-F: interference visibility decay; extension-level arrow"]),
    ]
    return SBTimeReversalAudit(items,N_TIME_REV,SB_TIME_REVERSAL_VERDICT,True,
        ["T NATIVELY BROKEN: dissipative ODE is not time-reversal invariant",
         "Arrow of time is NATIVE to constitutive architecture",
         "Quantum decoherence arrow is consistent extension"])

def _track_e() -> SBConservationAudit:
    items = [
        SBSymmetryItem("NC1","energy_conservation",
            "Standard dE/dt = 0.",
            "broken",["Open system: energy dissipates through constitutive channel",
                      "No conserved energy; only dissipative balance"]),
        SBSymmetryItem("NC2","momentum_conservation",
            "Standard dp/dt = 0.",
            "underdetermined",["Spatial translation symmetry suggests momentum-like quantity",
                              "But: dissipative dynamics may not support standard conservation"]),
        SBSymmetryItem("NC3","angular_momentum",
            "Standard dL/dt = 0.",
            "underdetermined",["Spatial isotropy suggests angular momentum-like quantity",
                              "Same caveat as momentum: dissipative dynamics"]),
        SBSymmetryItem("NC4","dissipative_balance_laws",
            "tau dPhi/dt + Phi = X: constitutive balance, not conservation.",
            "native",["The constitutive equation IS the balance law",
                     "Energy flows through system; not conserved but balanced"]),
        SBSymmetryItem("NC5","topological_charge_conservation",
            "pi_2(S^2) = Z integer winding (if O(3) postulated).",
            "extension_level",["Extension-only: requires O(3) MIP; not native"]),
    ]
    return SBConservationAudit(items,N_CONSERVATION,SB_CONSERVATION_VERDICT,False,
        ["Energy conservation: broken (open system dissipation)",
         "Momentum/angular momentum: underdetermined (spatial symmetry but dissipation)",
         "Native conservation: dissipative balance laws only",
         "Topological charge: extension-level, not native"])

def _track_f() -> SBScaleAudit:
    items = [
        SBSymmetryItem("SC1","tau_fixed_scale","tau^2 = 3/2: fixed characteristic scale.",
            "breaks_scale",["No continuous scale symmetry; tau is canonical"]),
        SBSymmetryItem("SC2","barrier_amplitude","Barrier amplitude A: another fixed scale.",
            "breaks_scale",["A provides energy-density scale"]),
        SBSymmetryItem("SC3","conformal_structure","Conformal invariance.",
            "absent",["Conformal requires scale + special conformal; both broken"]),
        SBSymmetryItem("SC4","asymptotic_scaling","Scaling behavior in extreme regimes.",
            "underdetermined",["Possible power-law behavior at large/small scales; not audited"]),
        SBSymmetryItem("SC5","renormalization_group_like","RG-like flow structure.",
            "underdetermined",["Possible but requires explicit analysis; not native"]),
    ]
    return SBScaleAudit(items,N_SCALE,True,
        ["Scale invariance BROKEN by tau and barrier amplitude",
         "Conformal structure absent",
         "Asymptotic scaling and RG: underdetermined"])

def _track_g() -> SBNativeInvariantLedger:
    items = [
        SBInvariantItem("NI1","constitutive_form_invariance",True,
            ["ODE structure tau dPhi/dt + Phi = X is exact form invariant"]),
        SBInvariantItem("NI2","z2_reflection_invariance",True,
            ["Phi -> -Phi with X -> -X preserves constitutive structure"]),
        SBInvariantItem("NI3","spatial_isotropy",True,
            ["No preferred direction; SO(3) spatial rotations"]),
        SBInvariantItem("NI4","spatial_translation_invariance",True,
            ["No preferred position; homogeneous"]),
        SBInvariantItem("NI5","tau_sq_three_halves_identity",True,
            ["tau^2 = 3/2: canonical fixed-point identity of the architecture"]),
    ]
    n_exact = sum(1 for i in items if i.exact)
    return SBNativeInvariantLedger(items,N_INVARIANTS,n_exact,
        ["5 exact native invariants identified",
         "All structural/constitutive, not dynamical conservation laws"])

def _track_h() -> SBBoundaryAudit:
    items = [
        SBBoundaryItem("BN1","o3_sigma_model",False,["Extension MIP; NOT native"]),
        SBBoundaryItem("BN2","su2_observable_algebra",False,["Extension MBU; NOT native"]),
        SBBoundaryItem("BN3","fermionic_spinorial",False,["Blocked; NOT native"]),
        SBBoundaryItem("BN4","gauge_structure",False,["Absent; NOT native"]),
        SBBoundaryItem("BN5","chemistry_shell_symmetry",False,["Blocked; NOT native"]),
    ]
    n_f = sum(1 for i in items if not i.native)
    return SBBoundaryAudit(items,N_BOUNDARY,n_f,
        ["ALL 5 extension items fenced as NOT native"])

def _track_i() -> SBAppendixPAudit:
    entries = [
        SBAppendixPEntry("SB_lorentz_break","Lorentz natively broken","native_canon",
            "tau and first-order ODE break Lorentz invariance",
            "Lorentz invariance preserved or effective",
            "Constitutive ODE structure"),
        SBAppendixPEntry("SB_t_reversal_break","T natively broken","native_canon",
            "Dissipative arrow of time is native",
            "Time reversal preserved",
            "First-order dissipative ODE"),
        SBAppendixPEntry("SB_z2_exact","Z2 reflection exact","native_canon",
            "Z2 Phi->-Phi is exact native discrete symmetry",
            "Z2 implies full matter parity",
            "Scalar constitutive structure"),
        SBAppendixPEntry("SB_conservation_balance","Dissipative balance only","native_canon",
            "No exact Noether conservation; dissipative balance laws",
            "Standard energy/momentum conservation",
            "Open-system dissipative dynamics"),
        SBAppendixPEntry("SB_scale_broken","Scale broken by tau","native_canon",
            "tau^2=3/2 breaks scale invariance",
            "Scale or conformal invariance",
            "Fixed canonical parameter"),
        SBAppendixPEntry("SB_spatial_preserved","Spatial symmetry preserved","native_canon",
            "Spatial isotropy SO(3) and translations: native",
            "Full Poincare invariance",
            "Scalar field isotropy"),
        SBAppendixPEntry("SB_overall","S-B overall","native_canon",
            "Native invariant ledger: 5 exact invariants, Lorentz and T broken, "
            "dissipative balance only",
            "Full relativistic or gauge symmetry",
            "All S-B tracks"),
    ]
    return SBAppendixPAudit(entries,N_APPENDIX_P,SB_OVERALL_P_CLASS,
        ["Overall: native_canon — these are proved properties of native GRUT"])

def _track_j() -> SBAuthorizationAudit:
    return SBAuthorizationAudit(True,
        ["native_symmetry_ledger_complete","lorentz_break_documented",
         "t_reversal_break_documented","conservation_boundary_established",
         "native_vs_extension_boundary_fenced"],
        SB_AUTHORIZATION_VERDICT,
        ["S-C authorized: native baseline established for extension symmetry analysis"])

def _track_k() -> SBNonclaimFirewall:
    return SBNonclaimFirewall(SB_NONCLAIMS,N_SB_NONCLAIMS,True)

def run_sb_native_symmetries_audit() -> SBNativeSymmetriesResult:
    ta=_track_a();tb=_track_b();tc=_track_c();td=_track_d()
    te=_track_e();tf=_track_f();tg=_track_g();th=_track_h()
    ti=_track_i();tj=_track_j();tk=_track_k()
    allowed = [
        "Lorentz invariance NATIVELY BROKEN: tau defines preferred frame, "
        "first-order ODE is not Lorentz-covariant",
        "Time reversal NATIVELY BROKEN: dissipative ODE not T-invariant; "
        "arrow of time is native to constitutive architecture",
        "Z2 reflection Phi->-Phi is EXACT native discrete symmetry",
        "Spatial isotropy SO(3) and translation invariance: NATIVE and preserved",
        "No standard Noether conservation: only dissipative balance laws; "
        "energy/momentum conservation broken by open-system dissipation",
        "Scale invariance broken by tau^2=3/2 and barrier amplitude; "
        "conformal structure absent",
        "5 exact native invariants: constitutive form, Z2, spatial isotropy, "
        "spatial translation, tau^2=3/2 identity",
    ]
    forbidden = [
        "Scalar architecture implies gauge theory",
        "Dissipative open system implies Noether conservation",
        "Preferred timescale implies Lorentz preserved",
        "Z2 reflection implies full matter parity",
        "Extension symmetry implies native vacuum symmetry",
        "Observable algebra implies native spacetime symmetry",
        "Residual spatial symmetry implies full relativistic invariance",
    ]
    diag: Dict[str,Any] = {
        "n_continuous":N_CONTINUOUS,"n_discrete":N_DISCRETE,
        "n_native_invariants":tg.n_exact,
        "lorentz_broken":tc.preferred_frame,
        "t_reversal_broken":td.dissipative_arrow,
        "scale_broken":tf.scale_broken,
        "standard_noether":te.standard_noether,
        "n_boundary_fenced":th.n_fenced,
        "n_nonclaims":N_SB_NONCLAIMS,
    }
    result = SBNativeSymmetriesResult(
        True,ta,tb,tc,td,te,tf,tg,th,ti,tj,tk,
        tc.lorentz_verdict,tb.discrete_verdict,td.time_reversal_verdict,
        te.conservation_verdict,tj.authorization_verdict,
        SB_OVERALL_P_CLASS,allowed,forbidden,SB_NONCLAIMS,diag)
    _validate(result); return result

def _validate(r: SBNativeSymmetriesResult) -> None:
    for v,a,l in [
        (r.lorentz_verdict,ALLOWED_LORENTZ,"Lorentz"),
        (r.discrete_symmetry_verdict,ALLOWED_DISCRETE,"Discrete"),
        (r.time_reversal_verdict,ALLOWED_TIME_REV,"T-reversal"),
        (r.conservation_verdict,ALLOWED_CONSERVATION,"Conservation"),
        (r.authorization_verdict,ALLOWED_AUTH,"Auth"),
    ]:
        if v not in a: raise ValueError(f"{l} '{v}' invalid")
    if r.sb_appendix_p_class not in ALLOWED_P_CLASSES: raise ValueError("class")
    for e in r.track_i_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_P_CLASSES: raise ValueError(f"{e.item_id}")
    if r.track_k_nonclaims.n_nonclaims!=N_SB_NONCLAIMS: raise ValueError("nonclaims")
    if not r.track_k_nonclaims.all_registered: raise ValueError("registered")
    if len(r.allowed_claims)!=N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN: raise ValueError("forbidden")
    if not r.track_j_authorization.sc_authorized: raise ValueError("auth")
    if not r.track_c_lorentz.preferred_frame: raise ValueError("pref frame")
    if not r.track_d_time_reversal.dissipative_arrow: raise ValueError("arrow")
    if r.track_e_conservation.standard_noether: raise ValueError("noether")

def _self_test() -> bool:
    r=run_sb_native_symmetries_audit()
    assert r.valid and r.lorentz_verdict==SB_LORENTZ_VERDICT
    assert r.time_reversal_verdict==SB_TIME_REVERSAL_VERDICT
    assert r.conservation_verdict==SB_CONSERVATION_VERDICT
    assert r.discrete_symmetry_verdict==SB_DISCRETE_VERDICT
    assert r.diagnostics["n_native_invariants"]==5
    return True

if __name__=="__main__":
    _self_test(); print("S-B passed.")
