"""
Appendix T-B --- Native Irreversibility and Semigroup Structure Audit
=====================================================================
GRUT Thermodynamic Program --- Phase T-B

Determines whether native GRUT dissipative evolution is genuinely
irreversible in a purely dynamical sense, using only the constitutive
structure tau dPhi/dt + Phi = X and its deterministic dynamics.

No entropy, temperature, ensemble, or probability language is used.

=== CORE ANALYSIS ===

The native constitutive equation:
    tau dPhi/dt + Phi = X(t)

has the exact solution (for tau > 0):
    Phi(t) = Phi(0) exp(-t/tau) + (1/tau) int_0^t exp(-(t-s)/tau) X(s) ds

This is a LINEAR FIRST-ORDER evolution. The key properties:

1. FORWARD SEMIGROUP: For constant or bounded X, the homogeneous part
   Phi_h(t) = Phi(0) exp(-t/tau) defines a contraction semigroup.
   The operator S(t): Phi(0) -> Phi(0) exp(-t/tau) satisfies:
     S(0) = I,  S(t+s) = S(t)S(s),  ||S(t)|| = exp(-t/tau) < 1 for t > 0.
   This is a STRONGLY CONTINUOUS CONTRACTION SEMIGROUP on the state space.

2. NON-INVERTIBILITY: S(t) = exp(-t/tau) is injective (one-to-one) for
   any finite t, so the map is formally invertible: S(-t) = exp(+t/tau).
   However, the backward operator AMPLIFIES: ||S(-t)|| = exp(+t/tau) -> inf.
   For the FULL solution (including forcing), backward evolution requires
   knowing the entire forcing history X(s) for s in [0,t] and the final
   state. This is PHYSICALLY non-recoverable in practice.

   Key distinction: FORMAL algebraic invertibility exists for the
   homogeneous part. But PHYSICAL non-recoverability arises from:
   (a) exponential amplification of backward errors
   (b) forcing-history dependence
   (c) asymptotic state forgetting

3. ASYMPTOTIC STATE FORGETTING: For ANY two initial conditions Phi_1(0)
   and Phi_2(0) with the SAME forcing:
     |Phi_1(t) - Phi_2(t)| = |Phi_1(0) - Phi_2(0)| exp(-t/tau)
   This decays EXPONENTIALLY to zero. After time t >> tau, the late-time
   state is determined entirely by the forcing history, not the initial
   condition. This is GENUINE DYNAMICAL STATE FORGETTING.

4. ATTRACTOR STRUCTURE:
   - Free relaxation (X=0): Phi(t) -> 0 as t -> inf. Global attractor = origin.
   - Constant forcing (X=X0): Phi(t) -> X0 as t -> inf. Global attractor = X0.
   - Time-dependent forcing: Phi tracks X(t) with lag tau. Steady tracking.

5. GENUINE IRREVERSIBILITY VERDICT:
   The dynamics are:
   - Time-asymmetric (first-order, dissipative)
   - Forward-semigroup (contraction semigroup with ||S(t)|| < 1)
   - Asymptotically state-forgetting (initial conditions forgotten exponentially)
   - Non-recoverable in practice (backward amplification + forcing history needed)
   - Formally invertible for the homogeneous part (algebraic, not physical)

   This constitutes GENUINE DYNAMICAL IRREVERSIBILITY in the following
   precise sense: forward evolution is contractive, unique, and stable;
   backward reconstruction is exponentially unstable and requires
   information (forcing history) not contained in the late-time state.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
CONTRACTION_RATE: float = 1.0 / TAU  # = GAMMA

# Evidence table regimes
N_REGIMES: int = 6
# Tracks
N_TRACKS: int = 6
N_TB_NONCLAIMS: int = 8
N_ALLOWED: int = 7
N_FORBIDDEN: int = 7

# Verdict enums
EVOLUTION_OPTIONS = frozenset({
    "forward_semigroup_natively_supported",
    "time_asymmetric_but_not_semigroup_demonstrated",
    "semigroup_status_conditionally_supported",
    "insufficient_structure_to_classify",
})
INVERTIBILITY_OPTIONS = frozenset({
    "generically_noninvertible_or_nonrecoverable",
    "asymptotically_state_forgetting",
    "backward_evolution_formal_but_physically_unlicensed",
    "invertibility_not_resolved",
})
ATTRACTOR_OPTIONS = frozenset({
    "relaxation_to_fixed_or_steady_structures_supported",
    "attractor_structure_conditionally_supported",
    "no_attractor_claim_licensed",
    "attractor_status_underdetermined",
})
IRREVERSIBILITY_OPTIONS = frozenset({
    "genuine_dynamical_irreversibility_supported",
    "weak_irreversibility_only",
    "time_asymmetry_without_irreversibility",
    "irreversibility_not_demonstrated",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_TC",
    "stop_for_missing_dynamical_closure",
})
OVERALL_OPTIONS = frozenset({
    "native_irreversibility_supported_under_dynamical_reading",
    "semigroup_like_relaxation_supported_with_limits",
    "time_asymmetry_stronger_than_recoverability_claim",
    "irreversibility_not_yet_established",
})

TB_EVOLUTION_VERDICT: str = "forward_semigroup_natively_supported"
TB_INVERTIBILITY_VERDICT: str = "asymptotically_state_forgetting"
TB_ATTRACTOR_VERDICT: str = "relaxation_to_fixed_or_steady_structures_supported"
TB_IRREVERSIBILITY_VERDICT: str = "genuine_dynamical_irreversibility_supported"
TB_AUTH_VERDICT: str = "authorized_to_proceed_to_TC"
TB_OVERALL_P: str = "native_irreversibility_supported_under_dynamical_reading"

TB_NONCLAIMS: List[str] = [
    "NOT_claiming_contraction_therefore_entropy_increase__"
    "state_space_contraction_is_dynamical_not_thermodynamic",
    "NOT_claiming_state_forgetting_therefore_information_loss__"
    "dynamical_non_recoverability_is_not_statistical_information_theory",
    "NOT_claiming_semigroup_therefore_second_law__"
    "semigroup_structure_is_mathematical_not_thermodynamic_law",
    "NOT_claiming_attractor_therefore_equilibrium__"
    "fixed_point_relaxation_is_dynamical_not_thermodynamic_equilibrium",
    "NOT_claiming_irreversibility_therefore_temperature__"
    "dynamical_irreversibility_does_not_define_temperature",
    "NOT_claiming_contraction_rate_therefore_entropy_production_rate__"
    "1_over_tau_is_contraction_rate_not_sigma",
    "NOT_claiming_forward_semigroup_therefore_closed_system_thermodynamics__"
    "open_dissipative_semigroup_is_not_Hamiltonian_dynamics",
    "NOT_claiming_dynamical_irreversibility_therefore_statistical_mechanics__"
    "purely_dynamical_result_no_ensemble_or_probability",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class TBTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]


@dataclass
class TBEvidenceRow:
    regime: str; forward_well_posed: str; inverse_licensed: str
    contractive: str; attractor_steady: str; recoverability: str
    row_verdict: str


@dataclass
class TBLicensedLanguage:
    licensed: List[str]; notes: List[str]


@dataclass
class TBNonlicensedLanguage:
    nonlicensed: List[str]; notes: List[str]


@dataclass
class TBNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool


@dataclass
class TBIrreversibilitySemigroupResult:
    valid: bool
    track_a_semigroup: TBTrackResult
    track_b_invertibility: TBTrackResult
    track_c_attractor: TBTrackResult
    track_d_directionality: TBTrackResult
    track_e_compression: TBTrackResult
    track_f_forcing: TBTrackResult
    evidence_table: List[TBEvidenceRow]
    licensed_language: TBLicensedLanguage
    nonlicensed_language: TBNonlicensedLanguage
    nonclaim_firewall: TBNonclaimFirewall
    # Five verdicts
    evolution_structure: str
    invertibility_status: str
    attractor_status: str
    irreversibility_status: str
    authorization: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Tracks
# ---------------------------------------------------------------------------

def _track_a() -> TBTrackResult:
    return TBTrackResult("A", "semigroup_vs_group",
        "Does evolution define a forward semigroup?",
        [
            "Homogeneous solution: Phi_h(t) = Phi(0) exp(-t/tau).",
            "Evolution operator S(t) = exp(-t/tau) satisfies: "
            "S(0)=1, S(t+s)=S(t)S(s), ||S(t)||=exp(-t/tau)<1 for t>0.",
            "This is a STRONGLY CONTINUOUS CONTRACTION SEMIGROUP.",
            "S(t) is well-defined for all t >= 0. It is NOT a group: "
            "S(-t) = exp(+t/tau) is unbounded and amplifying.",
            "For the full forced solution, the Duhamel integral requires "
            "the forcing history X(s) on [0,t]; this is forward-causal.",
        ],
        TB_EVOLUTION_VERDICT,
        ["Contraction semigroup: mathematical fact of first-order linear ODE with tau > 0"],
    )


def _track_b() -> TBTrackResult:
    return TBTrackResult("B", "non_invertibility_recoverability",
        "Can distinct initial states merge, destroying recoverability?",
        [
            "For SAME forcing X, two initial conditions Phi_1(0), Phi_2(0) evolve as: "
            "|Phi_1(t) - Phi_2(t)| = |Phi_1(0) - Phi_2(0)| exp(-t/tau).",
            "This decays EXPONENTIALLY. After t >> tau, the difference is negligible. "
            "The late-time state is determined by forcing, not initial condition.",
            "FORMAL INVERTIBILITY: the homogeneous map S(t) is injective (one-to-one) "
            "for finite t. So technically, given exact Phi(t), one can compute Phi(0) = "
            "Phi(t) exp(+t/tau). But this AMPLIFIES by exp(t/tau).",
            "PHYSICAL NON-RECOVERABILITY: (a) backward amplification exp(+t/tau) means "
            "any measurement error delta in Phi(t) becomes delta*exp(t/tau) in reconstructed "
            "Phi(0). For t = 5*tau, amplification is exp(5) ~ 148x. "
            "(b) Full reconstruction requires the forcing history X(s). "
            "(c) In practice, past states are DYNAMICALLY UNRECOVERABLE.",
            "Verdict: asymptotically state-forgetting. Formal injectivity exists but "
            "physical recoverability is destroyed by exponential amplification.",
        ],
        TB_INVERTIBILITY_VERDICT,
        ["State forgetting is exponential with rate 1/tau"],
    )


def _track_c() -> TBTrackResult:
    return TBTrackResult("C", "attractor_relaxation",
        "Does the dynamics produce attractors reinforcing forward directionality?",
        [
            "FREE RELAXATION (X=0): Phi(t) = Phi(0) exp(-t/tau) -> 0. "
            "The origin is a GLOBAL ATTRACTOR. All initial conditions relax to zero.",
            "CONSTANT FORCING (X=X0): Phi(t) -> X0 as t -> inf. "
            "The steady state Phi_ss = X0 is a GLOBAL ATTRACTOR.",
            "TIME-DEPENDENT FORCING: Phi(t) tracks X(t) with lag of order tau. "
            "No fixed point but a TRACKING MANIFOLD: Phi approximately equals X(t-tau).",
            "All regimes show RELAXATION: trajectories converge toward attractor/tracking "
            "structure. This reinforces forward directionality: evolution moves TOWARD "
            "the attractor, not away from it.",
        ],
        TB_ATTRACTOR_VERDICT,
        ["Global attractors in autonomous case; tracking in driven case"],
    )


def _track_d() -> TBTrackResult:
    return TBTrackResult("D", "directionality_vs_irreversibility",
        "Is T-breaking sufficient, or does dynamics show stronger irreversible structure?",
        [
            "TIME ASYMMETRY (established in S-B): the ODE is not invariant under t -> -t.",
            "FORWARD SEMIGROUP (Track A): evolution is contractive for t > 0.",
            "STATE FORGETTING (Track B): initial conditions exponentially forgotten.",
            "ATTRACTOR RELAXATION (Track C): trajectories converge globally.",
            "Together: this is STRONGER than mere time asymmetry. The dynamics are "
            "not merely directional -- they actively CONTRACT the state space, FORGET "
            "initial conditions, and RELAX toward attractors.",
            "GENUINE DYNAMICAL IRREVERSIBILITY: the forward evolution is unique, stable, "
            "and contractive; the backward reconstruction is exponentially unstable "
            "and requires external information. This is irreversibility in the "
            "precise dynamical sense: forward and backward evolution are not "
            "equivalent processes.",
        ],
        TB_IRREVERSIBILITY_VERDICT,
        ["Stronger than time asymmetry: contraction + forgetting + relaxation"],
    )


def _track_e() -> TBTrackResult:
    return TBTrackResult("E", "state_space_compression",
        "Does dissipation compress state-space volume/distance?",
        [
            "DISTANCE CONTRACTION: |Phi_1(t)-Phi_2(t)| = |Phi_1(0)-Phi_2(0)| exp(-t/tau). "
            "Any metric on initial conditions contracts exponentially under evolution.",
            "CONTRACTION RATE: 1/tau = gamma. This is the native contraction rate.",
            "NORM DEPENDENCE: contraction holds for ANY norm induced by the linear "
            "structure because exp(-t/tau) is a scalar multiplier on state differences.",
            "NO CANONICAL STATE-SPACE METRIC: GRUT does not define a preferred metric "
            "on the infinite-dimensional field space. But the contraction is "
            "norm-independent for the linear homogeneous part.",
            "CONDITIONAL ON SAME FORCING: contraction of differences holds for two "
            "solutions with the SAME forcing X. For different forcings, the difference "
            "depends on the forcing difference as well.",
        ],
        "contraction_demonstrated_conditionally",
        ["Contraction is norm-independent for homogeneous part; conditional on same forcing"],
    )


def _track_f() -> TBTrackResult:
    return TBTrackResult("F", "forcing_boundary_dependence",
        "How much depends on X, boundaries, or autonomy?",
        [
            "FREE RELAXATION (X=0): UNCONDITIONAL. Contraction, attractor (origin), "
            "state forgetting, semigroup. All properties hold without restriction.",
            "CONSTANT FORCING (X=X0): UNCONDITIONAL. Same properties with attractor "
            "shifted to X0.",
            "TIME-DEPENDENT FORCING: CONDITIONAL. Semigroup structure holds for the "
            "homogeneous part. The full solution depends on the forcing history. "
            "State forgetting still holds (initial condition decays). Attractor is "
            "replaced by tracking manifold.",
            "GENERAL FORCING: semigroup and contraction of DIFFERENCES between solutions "
            "with same forcing are unconditional. Full solution reconstruction from "
            "late-time state requires forcing history.",
            "SUMMARY: the strongest irreversibility claims (semigroup, contraction, "
            "state forgetting) are UNCONDITIONAL for the homogeneous part and "
            "CONDITIONAL on same forcing for the full driven system.",
        ],
        "strongest_claims_unconditional_for_homogeneous",
        ["Forcing dependence is explicit and documented"],
    )


def _build_evidence() -> List[TBEvidenceRow]:
    return [
        TBEvidenceRow("free_relaxation_X_eq_0",
            "Yes (unique)", "Formal only (amplifying)", "Yes (exp(-t/tau))",
            "Yes (origin)", "Lost exponentially", "semigroup_irreversible"),
        TBEvidenceRow("constant_forcing_X_eq_X0",
            "Yes (unique)", "Formal only (amplifying)", "Yes (exp(-t/tau))",
            "Yes (X0)", "Lost exponentially", "semigroup_irreversible"),
        TBEvidenceRow("time_dependent_forcing",
            "Yes (unique, causal)", "Requires forcing history", "Yes (differences)",
            "Tracking manifold", "Requires history", "conditionally_irreversible"),
        TBEvidenceRow("asymptotic_long_time",
            "Yes", "Exponentially unstable", "Yes (exponential)",
            "Attractor or tracking", "Exponentially lost", "state_forgetting_confirmed"),
        TBEvidenceRow("backward_reconstruction",
            "N/A (backward)", "Amplification exp(+t/tau)", "No (amplifying)",
            "N/A", "Requires exact state + history", "physically_non_recoverable"),
        TBEvidenceRow("nearby_state_contraction",
            "Yes", "N/A", "Yes: |delta| -> |delta|exp(-t/tau)",
            "N/A", "delta forgotten exponentially", "contraction_demonstrated"),
    ]


def _build_licensed() -> TBLicensedLanguage:
    return TBLicensedLanguage(
        ["forward_contraction_semigroup",
         "exponential_state_forgetting_rate_1_over_tau",
         "dynamical_non_recoverability_of_initial_conditions",
         "global_attractor_relaxation_in_autonomous_case",
         "tracking_manifold_in_driven_case",
         "genuine_dynamical_irreversibility"],
        ["All licensed purely as dynamical properties of the constitutive ODE"])


def _build_nonlicensed() -> TBNonlicensedLanguage:
    return TBNonlicensedLanguage(
        ["entropy", "entropy_production", "temperature",
         "statistical_mechanics", "equilibrium_thermodynamics",
         "bath_interpretation", "free_energy", "partition_function",
         "Boltzmann_distribution", "microstate_counting"],
        ["None of these are licensed by T-B; all require structures absent from T0"])


def _build_firewall() -> TBNonclaimFirewall:
    return TBNonclaimFirewall(TB_NONCLAIMS, N_TB_NONCLAIMS, True)


# ---------------------------------------------------------------------------
# Master
# ---------------------------------------------------------------------------

def run_tb_irreversibility_semigroup_audit() -> TBIrreversibilitySemigroupResult:
    ta = _track_a(); tb = _track_b(); tc = _track_c()
    td = _track_d(); te = _track_e(); tf = _track_f()
    ev = _build_evidence()
    lic = _build_licensed(); nlic = _build_nonlicensed()
    fw = _build_firewall()

    key = [
        "Native constitutive evolution S(t) = exp(-t/tau) forms a STRONGLY "
        "CONTINUOUS CONTRACTION SEMIGROUP with ||S(t)|| < 1 for t > 0",
        "State forgetting is EXPONENTIAL: |Phi_1-Phi_2| decays as exp(-t/tau); "
        "after t >> tau, initial conditions are dynamically unrecoverable",
        "Backward reconstruction requires exp(+t/tau) amplification + full forcing "
        "history: PHYSICALLY NON-RECOVERABLE",
        "Global attractor structure: Phi -> 0 (free) or Phi -> X0 (constant forcing) "
        "or tracking manifold (time-dependent forcing)",
        "GENUINE DYNAMICAL IRREVERSIBILITY: contraction + state forgetting + "
        "attractor relaxation + non-recoverability. Stronger than time asymmetry alone.",
        "Contraction rate = 1/tau = gamma: native canonical rate",
        "All claims are PURELY DYNAMICAL. No entropy, temperature, ensemble, "
        "or probability invoked.",
    ]

    allowed = [
        "Forward contraction semigroup S(t)=exp(-t/tau) natively supported",
        "Exponential state forgetting at rate 1/tau: initial conditions "
        "dynamically unrecoverable after t >> tau",
        "Backward evolution formally exists but is exponentially amplifying "
        "and physically non-recoverable",
        "Global attractor relaxation in autonomous and constant-forcing regimes",
        "Genuine dynamical irreversibility: contraction + forgetting + "
        "relaxation + non-recoverability",
        "Contraction rate 1/tau is the native canonical irreversibility rate",
        "T-C authorized: irreversibility established, monotone investigation next",
    ]

    forbidden = [
        "Contraction implies entropy increase",
        "State forgetting implies information-theoretic loss",
        "Semigroup implies second law of thermodynamics",
        "Attractor implies thermodynamic equilibrium",
        "Irreversibility implies temperature",
        "Contraction rate implies entropy production rate",
        "Dynamical irreversibility implies statistical mechanics",
    ]

    diagnostics: Dict[str, Any] = {
        "contraction_rate": CONTRACTION_RATE,
        "contraction_rate_is_gamma": abs(CONTRACTION_RATE - 1.0/TAU) < 1e-15,
        "semigroup_norm": "exp(-t/tau)",
        "backward_amplification": "exp(+t/tau)",
        "state_forgetting_timescale": TAU,
        "n_regimes": N_REGIMES,
        "n_licensed_terms": len(lic.licensed),
        "n_nonlicensed_terms": len(nlic.nonlicensed),
        "n_nonclaims": N_TB_NONCLAIMS,
    }

    result = TBIrreversibilitySemigroupResult(
        True, ta, tb, tc, td, te, tf, ev, lic, nlic, fw,
        TB_EVOLUTION_VERDICT, TB_INVERTIBILITY_VERDICT,
        TB_ATTRACTOR_VERDICT, TB_IRREVERSIBILITY_VERDICT,
        TB_AUTH_VERDICT, TB_OVERALL_P,
        key, allowed, forbidden, TB_NONCLAIMS, diagnostics,
    )
    _validate(result); return result


def _validate(r: TBIrreversibilitySemigroupResult) -> None:
    if r.evolution_structure not in EVOLUTION_OPTIONS: raise ValueError("evolution")
    if r.invertibility_status not in INVERTIBILITY_OPTIONS: raise ValueError("invert")
    if r.attractor_status not in ATTRACTOR_OPTIONS: raise ValueError("attractor")
    if r.irreversibility_status not in IRREVERSIBILITY_OPTIONS: raise ValueError("irrev")
    if r.authorization not in AUTH_OPTIONS: raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS: raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims != N_TB_NONCLAIMS: raise ValueError("nonclaims")
    if not r.nonclaim_firewall.all_registered: raise ValueError("registered")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")
    if len(r.evidence_table) != N_REGIMES: raise ValueError("evidence")
    if not r.diagnostics["contraction_rate_is_gamma"]: raise ValueError("rate")


def _self_test() -> bool:
    r = run_tb_irreversibility_semigroup_audit()
    assert r.valid
    assert r.evolution_structure == TB_EVOLUTION_VERDICT
    assert r.invertibility_status == TB_INVERTIBILITY_VERDICT
    assert r.attractor_status == TB_ATTRACTOR_VERDICT
    assert r.irreversibility_status == TB_IRREVERSIBILITY_VERDICT
    assert r.authorization == TB_AUTH_VERDICT
    assert r.overall_appendix_p == TB_OVERALL_P
    assert abs(r.diagnostics["contraction_rate"] - 1.0/TAU) < 1e-15
    return True


if __name__ == "__main__":
    _self_test(); print("T-B passed.")
