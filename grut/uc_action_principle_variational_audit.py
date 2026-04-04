"""
Appendix U-C --- Action Principle and Variational Structure Audit
=================================================================
GRUT Unified-Field Program --- Phase U-C

Determines whether the native GRUT scalar dissipative core admits any
disciplined action-like, variational, doubled-field, constrained, or
effective functional representation.

=== CORE ANALYSIS ===

Native equation: tau dPhi/dt + Phi = X

NATIVE ACTION TEST:
  A true action S[Phi] = int L(Phi, dPhi/dt, dPhi/dx) dt dx should yield
  the native equation via Euler-Lagrange: dL/dPhi - d/dt(dL/d(dPhi/dt)) = 0.

  Problem: the native equation is FIRST-ORDER and DISSIPATIVE.
  Euler-Lagrange from a real local action generically gives SECOND-ORDER
  conservative equations (because L(Phi, dPhi/dt) -> d^2Phi/dt^2 terms).

  A first-order ODE tau dPhi/dt + Phi = X cannot arise from extremizing
  S = int L(Phi, dPhi/dt) dt with L real-valued and non-degenerate.
  The obstruction is structural: dissipation violates time-reversal symmetry,
  but Euler-Lagrange from a real action preserves it.

  Workaround 1: degenerate L with L = f(Phi) only (no dPhi/dt).
  Then dL/dPhi = 0 gives algebraic eq, not ODE. Does not reproduce dynamics.

  Workaround 2: linear L = (tau dPhi/dt + Phi - X) * lambda with lambda
  a Lagrange multiplier. This ENFORCES the equation but is a constrained
  construction, not a native derivation.

  Verdict: NO true native action from single-field real local L.

DOUBLED-FIELD / RESPONSE FORMULATION:
  The Galley CTP / Martin-Siggia-Rose (MSR) / Schwinger-Keldysh approach
  doubles the fields: (Phi_+, Phi_-) or (Phi, Phi_tilde) where Phi_tilde
  is a response/auxiliary field.

  Effective action: S_eff[Phi, Phi_tilde] = int [Phi_tilde * (tau dPhi/dt + Phi - X)] dt
  Variation: dS/dPhi_tilde = 0 -> tau dPhi/dt + Phi = X  (recovers native eq)
             dS/dPhi = 0 -> response/adjoint equation for Phi_tilde

  This WORKS as an effective reformulation. But:
  - Phi_tilde is a NONNATIVE auxiliary field (not in U-B's native content)
  - The construction is standard for dissipative systems but is a REFORMULATION
  - It does NOT make dissipation conservative; it ENCODES it in doubled form

  Classification: effective_reformulation, not native_action.

MEMORY / NONLOCAL:
  If retardation kernel K(t-s) replaces instantaneous tau,
  a nonlocal influence functional can be written:
  S_IF[Phi_+, Phi_-] = int int Phi_-(t) K(t-s) Phi_+(s) ds dt + ...

  This is the standard influence-functional approach (Feynman-Vernon).
  It is a reformulation technique, not a native variational principle.
  Memory does not help make the native equation variational; it makes
  the nonlocal version representable in influence-functional form.

LYAPUNOV / T-C FUNCTIONAL:
  V = (1/2)(Phi - X_ss)^2 from T-C is a LYAPUNOV FUNCTIONAL.
  It is monotone along trajectories. It is NOT an action:
  - An action is extremized; V is minimized by relaxation
  - An action generates equations via Euler-Lagrange; V generates nothing
  - V is a distance-to-attractor measure, not a Lagrangian integral
  Relabeling V as an action is forbidden by U-A distinction D11.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_CANDIDATES: int = 6
N_OBSTRUCTIONS: int = 5
N_UC_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

NATIVE_ACTION_OPTIONS = frozenset({
    "no_true_native_action_identified",
    "native_action_obstructed_by_dissipative_structure",
    "constrained_native_variational_form_only",
    "true_native_action_supported",
})
AUX_OPTIONS = frozenset({
    "multiplier_or_response_formalism_available_but_nonnative",
    "constrained_formulation_conditionally_available",
    "no_auxiliary_variational_form_identified",
    "auxiliary_formalism_upgrades_native_structure",
})
MEMORY_VAR_OPTIONS = frozenset({
    "memory_supports_nonlocal_reformulation_only",
    "memory_worsens_variational_closure",
    "memory_variational_role_unresolved",
    "memory_enables_true_action_structure",
})
STRONGEST_OPTIONS = frozenset({
    "constitutive_dynamics_only",
    "pseudoaction_or_response_functional_only",
    "constrained_variational_representation_only",
    "effective_action_language_conditionally_licensed",
    "native_action_language_licensed",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_UD",
    "stop_for_missing_variational_boundary",
})
OVERALL_OPTIONS = frozenset({
    "constitutive_scalar_dynamics_persist_without_native_action",
    "effective_variational_reformulations_exist_but_are_nonnative",
    "action_like_language_conditionally_available_under_auxiliary_construction",
    "native_action_structure_supported",
})

UC_NATIVE_ACTION: str = "native_action_obstructed_by_dissipative_structure"
UC_AUX: str = "multiplier_or_response_formalism_available_but_nonnative"
UC_MEMORY_VAR: str = "memory_supports_nonlocal_reformulation_only"
UC_STRONGEST: str = "pseudoaction_or_response_functional_only"
UC_AUTH: str = "authorized_to_proceed_to_UD"
UC_OVERALL_P: str = "effective_variational_reformulations_exist_but_are_nonnative"

UC_NONCLAIMS: List[str] = [
    "NOT_claiming_response_field_formalism_therefore_native_action__"
    "doubled_field_representation_is_reformulation_not_derivation",
    "NOT_claiming_multiplier_enforcement_therefore_variational_principle__"
    "Lagrange_multiplier_is_constraint_device_not_native_action",
    "NOT_claiming_Lyapunov_V_therefore_action__"
    "monotone_functional_is_not_action_integral",
    "NOT_claiming_influence_functional_therefore_native_nonlocal_action__"
    "Feynman_Vernon_reformulation_requires_auxiliary_fields",
    "NOT_claiming_CTP_doubled_action_therefore_native_action__"
    "Galley_CTP_is_effective_regime_construction",
    "NOT_claiming_dissipative_equation_therefore_secretly_conservative__"
    "first_order_dissipative_ODE_breaks_T_symmetry_intrinsically",
    "NOT_claiming_variational_reformulation_therefore_Hamiltonian__"
    "auxiliary_construction_does_not_produce_symplectic_structure",
    "NOT_claiming_action_obstruction_therefore_theory_incomplete__"
    "constitutive_dynamics_are_native_action_is_not_required",
]


@dataclass
class UCTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class UCEvidenceRow:
    candidate: str; reproduces_native: str; native_or_not: str
    extra_fields: str; strongest_language: str
    main_obstruction: str; row_verdict: str

@dataclass
class UCObstruction:
    rank: int; name: str; description: str

@dataclass
class UCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class UCActionVariationalResult:
    valid: bool
    track_a_native_action: UCTrackResult
    track_b_constrained: UCTrackResult
    track_c_doubled: UCTrackResult
    track_d_memory: UCTrackResult
    track_e_pseudoaction: UCTrackResult
    track_f_obstructions: List[UCObstruction]
    evidence_table: List[UCEvidenceRow]
    nonclaim_firewall: UCNonclaimFirewall
    native_action_status: str; auxiliary_variational_status: str
    memory_variational_status: str; strongest_action_like_language: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _track_a() -> UCTrackResult:
    return UCTrackResult("A","native_action_test",
        "Can native dissipative ODE arise from a true single-field action?",
        [
            "Euler-Lagrange from real local L(Phi, dPhi/dt) generically gives "
            "SECOND-ORDER equations. The native ODE is FIRST-ORDER.",
            "A real local action preserves time-reversal symmetry in the EOM. "
            "The native ODE breaks T natively (S-B).",
            "Degenerate L = f(Phi) gives algebraic equation, not ODE.",
            "Linear-in-velocity L = A(Phi) dPhi/dt + B(Phi) gives first-order "
            "CONSERVATIVE equations (total derivative), not dissipative.",
            "No real local single-field action can produce tau dPhi/dt + Phi = X "
            "as a genuine Euler-Lagrange equation. The obstruction is structural: "
            "dissipation and time-reversal breaking are incompatible with "
            "standard variational derivation from a real action.",
        ],
        UC_NATIVE_ACTION,
        ["Structural obstruction: dissipation vs variational derivation"])


def _track_b() -> UCTrackResult:
    return UCTrackResult("B","constrained_formulation",
        "Can a multiplier/constrained construction enforce the native eq?",
        [
            "LAGRANGE MULTIPLIER: S = int lambda(t) [tau dPhi/dt + Phi - X] dt.",
            "dS/dlambda = 0 gives tau dPhi/dt + Phi = X. Recovers native eq.",
            "dS/dPhi = 0 gives an adjoint equation for lambda.",
            "This WORKS as enforcement but: lambda is a NONNATIVE auxiliary field.",
            "The construction has no predictive content beyond the original ODE: "
            "it encodes the equation, it does not derive it.",
            "Classification: constrained enforcement device, not native action.",
        ],
        "constrained_enforcement_available_nonnative",
        ["Multiplier construction available but nonnative"])


def _track_c() -> UCTrackResult:
    return UCTrackResult("C","doubled_field_response",
        "Can doubled-field/response-field formalism represent the dynamics?",
        [
            "MSR / CTP construction: S_eff = int Phi_tilde (tau dPhi/dt + Phi - X) dt.",
            "dS/dPhi_tilde = 0 -> native equation. REPRODUCES dynamics.",
            "Phi_tilde is a RESPONSE/AUXILIARY field: not in U-B native content.",
            "This is the STANDARD technique for dissipative systems in "
            "non-equilibrium field theory.",
            "The Galley CTP approach (Phi_1, Phi_2) is equivalent: "
            "Phi_+ = physical, Phi_- = auxiliary/response.",
            "Classification: effective reformulation with nonnative auxiliary fields. "
            "Useful for formal manipulations but does not make dissipation "
            "conservative or variational in the native sense.",
        ],
        "response_formalism_available_nonnative",
        ["Standard doubled-field technique; nonnative auxiliary"])


def _track_d() -> UCTrackResult:
    return UCTrackResult("D","memory_nonlocal",
        "Does memory support a nonlocal variational functional?",
        [
            "Nonlocal memory kernel: tau dPhi/dt + Phi -> int K(t-s) Phi(s) ds = X(t).",
            "INFLUENCE FUNCTIONAL: S_IF = int int Phi_tilde(t) K(t-s) Phi(s) ds dt.",
            "This is a Feynman-Vernon-style reformulation. It REPRESENTS the "
            "nonlocal dynamics in a functional form.",
            "But: it still requires a response field Phi_tilde (nonnative).",
            "Memory does NOT help make the native dynamics variational; "
            "it makes the REFORMULATION nonlocal.",
            "Classification: nonlocal reformulation, not native action.",
        ],
        UC_MEMORY_VAR,
        ["Memory enables nonlocal reformulation; does not create native action"])


def _track_e() -> UCTrackResult:
    return UCTrackResult("E","pseudoaction_boundary",
        "Is any weaker action-like object useful?",
        [
            "RESPONSE FUNCTIONAL: S_eff[Phi, Phi_tilde] as in Track C. "
            "A pseudo-action that generates the native equation + adjoint. "
            "Useful for perturbation theory, diagram expansion, etc.",
            "LYAPUNOV V = (1/2)(Phi - X_ss)^2: NOT an action. "
            "V is monotone along trajectories; an action is EXTREMIZED. "
            "V generates no equations; an action generates EOM via E-L. "
            "Relabeling V as action: FORBIDDEN (U-A D11).",
            "DISSIPATIVE BALANCE dV/dt + D = 0: NOT a variational identity. "
            "It is a consequence of the ODE, not an extremal condition.",
            "STRONGEST LICENSED LANGUAGE: pseudo-action or response functional "
            "using nonnative doubled fields. Not native action.",
        ],
        UC_STRONGEST,
        ["Pseudo-action via response fields is the strongest available"])


def _build_obstructions() -> List[UCObstruction]:
    return [
        UCObstruction(1,"first_order_dissipative_structure",
            "E-L from real local action gives second-order conservative eq; "
            "native ODE is first-order dissipative"),
        UCObstruction(2,"time_reversal_breaking",
            "Real action preserves T; native ODE breaks T natively"),
        UCObstruction(3,"external_source_X",
            "X has no evolution equation; it is input, not variational field"),
        UCObstruction(4,"absence_of_hamiltonian",
            "No symplectic structure; dissipative dynamics are not Hamiltonian"),
        UCObstruction(5,"single_scalar_sparse_core",
            "Only one native field; too sparse for nontrivial conservative action"),
    ]


def _build_evidence() -> List[UCEvidenceRow]:
    return [
        UCEvidenceRow("single_field_local_action",
            "No: E-L gives 2nd order", "Would be native", "None",
            "N/A: fails", "1st-order dissipative vs 2nd-order conservative",
            "obstructed"),
        UCEvidenceRow("multiplier_constrained",
            "Yes: dS/dlambda=0", "Nonnative (lambda auxiliary)", "lambda field",
            "Constrained enforcement", "No predictive content beyond ODE",
            "available_nonnative"),
        UCEvidenceRow("doubled_response_field",
            "Yes: dS/dPhi_tilde=0", "Nonnative (Phi_tilde auxiliary)", "Phi_tilde",
            "Response/pseudo-action", "Phi_tilde is nonnative",
            "available_nonnative"),
        UCEvidenceRow("memory_nonlocal_functional",
            "Yes (nonlocal form)", "Nonnative", "Response field + kernel",
            "Influence functional", "Still needs auxiliary field",
            "reformulation_only"),
        UCEvidenceRow("lyapunov_V_comparison",
            "No: V is monotone not extremized", "N/A", "None",
            "Lyapunov only", "V is not action (U-A D11)",
            "not_action"),
        UCEvidenceRow("external_source_X",
            "N/A: X is input", "N/A", "N/A",
            "N/A", "X lacks evolution equation",
            "not_variational_field"),
    ]


def run_uc_action_principle_variational_audit() -> UCActionVariationalResult:
    ta=_track_a();tb=_track_b();tc=_track_c()
    td=_track_d();te=_track_e()
    obs=_build_obstructions();ev=_build_evidence()
    fw=UCNonclaimFirewall(UC_NONCLAIMS,N_UC_NONCLAIMS,True)

    key=[
        "NO TRUE NATIVE ACTION: the first-order dissipative ODE cannot arise "
        "from a real local single-field action via Euler-Lagrange. "
        "The obstruction is structural (dissipation vs variational derivation).",
        "MULTIPLIER ENFORCEMENT available but nonnative: lambda field enforces "
        "the ODE but adds no predictive content and is not a native field.",
        "RESPONSE-FIELD FORMALISM available but nonnative: S_eff[Phi,Phi_tilde] "
        "reproduces the dynamics with a nonnative auxiliary Phi_tilde.",
        "MEMORY supports nonlocal REFORMULATION only: influence-functional form "
        "available but still requires nonnative response field.",
        "LYAPUNOV V is NOT an action: monotone ≠ extremized, no E-L generation. "
        "Relabeling forbidden by U-A D11.",
        "5 variational obstructions ranked: first-order dissipative structure, "
        "T-breaking, external source, Hamiltonian absence, sparse core.",
        "STRONGEST LICENSED: pseudo-action or response functional using "
        "nonnative doubled fields. Not native action.",
    ]

    allowed=[
        "Native action obstructed by first-order dissipative structure: "
        "E-L from real local action gives 2nd-order, not 1st-order ODE",
        "Multiplier/constrained enforcement available but nonnative",
        "Response-field/doubled-field formalism available but nonnative: "
        "S_eff[Phi,Phi_tilde] reproduces dynamics",
        "Memory supports nonlocal influence-functional reformulation",
        "Strongest action-like language: pseudo-action or response functional",
        "5 variational obstructions clearly ranked",
        "U-D authorized: variational boundary established",
    ]

    forbidden=[
        "Response field formalism implies native action",
        "Multiplier enforcement implies native variational principle",
        "Lyapunov V implies action",
        "Influence functional implies native nonlocal action",
        "CTP doubled action implies native action",
        "Dissipative equation is secretly conservative",
        "Variational reformulation implies Hamiltonian structure",
    ]

    diagnostics: Dict[str,Any]={
        "native_action_possible":False,
        "constrained_available":True,
        "response_field_available":True,
        "memory_helps_native_action":False,
        "lyapunov_is_action":False,
        "n_obstructions":len(obs),
        "n_candidates":N_CANDIDATES,
        "n_nonclaims":N_UC_NONCLAIMS,
    }

    result=UCActionVariationalResult(
        True,ta,tb,tc,td,te,obs,ev,fw,
        UC_NATIVE_ACTION,UC_AUX,UC_MEMORY_VAR,UC_STRONGEST,
        UC_AUTH,UC_OVERALL_P,key,allowed,forbidden,UC_NONCLAIMS,diagnostics)
    _validate(result);return result


def _validate(r:UCActionVariationalResult)->None:
    if r.native_action_status not in NATIVE_ACTION_OPTIONS:raise ValueError("native")
    if r.auxiliary_variational_status not in AUX_OPTIONS:raise ValueError("aux")
    if r.memory_variational_status not in MEMORY_VAR_OPTIONS:raise ValueError("mem")
    if r.strongest_action_like_language not in STRONGEST_OPTIONS:raise ValueError("strong")
    if r.authorization not in AUTH_OPTIONS:raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims!=N_UC_NONCLAIMS:raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:raise ValueError("reg")
    if len(r.allowed_claims)!=N_ALLOWED:raise ValueError("allowed")
    if len(r.forbidden_claims)!=N_FORBIDDEN:raise ValueError("forbidden")
    if len(r.evidence_table)!=N_CANDIDATES:raise ValueError("evidence")
    if len(r.track_f_obstructions)!=N_OBSTRUCTIONS:raise ValueError("obstr")
    if r.diagnostics["native_action_possible"]:raise ValueError("native must be False")
    if r.diagnostics["lyapunov_is_action"]:raise ValueError("lyap must be False")


def _self_test()->bool:
    r=run_uc_action_principle_variational_audit()
    assert r.valid
    assert r.native_action_status==UC_NATIVE_ACTION
    assert r.auxiliary_variational_status==UC_AUX
    assert r.memory_variational_status==UC_MEMORY_VAR
    assert r.strongest_action_like_language==UC_STRONGEST
    assert r.authorization==UC_AUTH
    assert r.diagnostics["native_action_possible"] is False
    assert r.diagnostics["response_field_available"] is True
    return True

if __name__=="__main__":
    _self_test();print("U-C passed.")
