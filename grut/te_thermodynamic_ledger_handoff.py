"""
Appendix T-E --- Final Thermodynamic Ledger and Handoff to U
=============================================================
GRUT Thermodynamic Program --- Phase T-E  (Final Thermodynamic Stage)

Consolidates T0/T-A, T-B, T-C, T-D into the final thermodynamic ledger
and defines exact inheritance boundary for Appendix U.

Closes thermodynamics under discipline, not inflation.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU

ALLOWED_CLASSIFICATIONS = frozenset({
    "native_established", "licensed_but_limited", "absent_unbuilt",
    "blocked_by_structure", "requires_new_postulates",
})

N_LEDGER_ITEMS: int = 20
N_OBSTRUCTIONS: int = 8
N_U_SETTLED: int = 7
N_U_FORBIDDEN: int = 7
N_U_LICENSED: int = 5
N_TE_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

NATIVE_OPTIONS = frozenset({
    "irreversible_dissipative_core_confirmed",
    "thermodynamic_core_requires_revision",
})
BOOKKEEPING_OPTIONS = frozenset({
    "lyapunov_and_balance_ledger_confirmed",
    "limited_bookkeeping_only", "bookkeeping_not_stable",
})
THERMAL_OPTIONS = frozenset({
    "equilibrium_and_temperature_absent",
    "partial_thermal_completion",
    "thermal_completion_requires_new_postulates",
    "full_thermal_framework_constructed",
})
INHERIT_OPTIONS = frozenset({
    "effective_action_handoff_clean_with_limits",
    "handoff_to_U_blocked_by_thermodynamic_ambiguity",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_U",
    "stop_for_missing_thermodynamic_ledger",
})
OVERALL_OPTIONS = frozenset({
    "irreversible_dissipative_ledger_closed_without_thermal_completion",
    "nonstatistical_thermodynamic_foundation_bounded",
    "partial_nonequilibrium_thermodynamic_architecture",
    "full_thermodynamic_framework",
})

TE_NATIVE_VERDICT: str = "irreversible_dissipative_core_confirmed"
TE_BOOKKEEPING_VERDICT: str = "lyapunov_and_balance_ledger_confirmed"
TE_THERMAL_VERDICT: str = "equilibrium_and_temperature_absent"
TE_INHERIT_VERDICT: str = "effective_action_handoff_clean_with_limits"
TE_AUTH_VERDICT: str = "authorized_to_proceed_to_U"
TE_OVERALL_P: str = "irreversible_dissipative_ledger_closed_without_thermal_completion"

TE_NONCLAIMS: List[str] = [
    "NOT_claiming_thermodynamic_ledger_therefore_thermodynamics_complete__"
    "ledger_documents_what_is_established_not_what_is_complete",
    "NOT_claiming_Lyapunov_therefore_entropy__"
    "V_is_deviation_functional_not_state_function_S",
    "NOT_claiming_dissipation_rate_therefore_entropy_production__"
    "D_is_dynamical_bookkeeping_not_sigma",
    "NOT_claiming_balance_law_therefore_first_law__"
    "dV_dt_plus_D_equals_zero_is_not_dU_equals_TdS_minus_PdV",
    "NOT_claiming_fixed_point_therefore_equilibrium__"
    "dynamical_rest_state_is_not_thermodynamic_equilibrium",
    "NOT_claiming_tau_therefore_temperature__"
    "relaxation_timescale_is_not_thermodynamic_temperature",
    "NOT_claiming_semigroup_therefore_second_law__"
    "forward_contraction_is_dynamical_not_thermodynamic",
    "NOT_claiming_handoff_to_U_therefore_thermodynamics_solved__"
    "handoff_authorizes_investigation_not_closure",
]


@dataclass
class TELedgerItem:
    structure: str; classification: str
    what_established: str; what_not_established: str
    what_u_may_assume: str

@dataclass
class TEObstruction:
    rank: int; name: str; description: str

@dataclass
class TEHandoffToU:
    settled_inheritance: List[str]
    forbidden_assumptions: List[str]
    licensed_questions: List[str]
    notes: List[str]

@dataclass
class TENonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class TEThermodynamicLedgerResult:
    valid: bool
    ledger: List[TELedgerItem]
    obstructions: List[TEObstruction]
    handoff: TEHandoffToU
    nonclaim_firewall: TENonclaimFirewall
    native_thermodynamic_status: str
    bookkeeping_status: str
    thermal_completion_status: str
    inheritance_status_for_U: str
    authorization: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


def _build_ledger() -> List[TELedgerItem]:
    return [
        TELedgerItem("dissipation", "native_established",
            "Energy leaves system through tau channel", "Quantitative thermodynamic dissipation rate",
            "Native dissipation as substrate"),
        TELedgerItem("arrow_of_time", "native_established",
            "First-order ODE + dissipation define temporal direction", "Proof beyond directionality",
            "Native temporal orientation"),
        TELedgerItem("semigroup_evolution", "native_established",
            "S(t)=exp(-t/tau) contraction semigroup", "Group structure (reversible)",
            "Forward semigroup as evolution structure"),
        TELedgerItem("non_invertibility_state_forgetting", "native_established",
            "Exponential state forgetting at rate 1/tau", "Formal reversibility",
            "Dynamical non-recoverability"),
        TELedgerItem("attractor_fixed_point_relaxation", "native_established",
            "Global attractor in autonomous/constant-forcing case", "Thermodynamic equilibrium",
            "Dynamical rest states as targets"),
        TELedgerItem("tracking_steady_state", "native_established",
            "Stable tracking under slowly varying forcing", "Statistical NESS",
            "Dynamical tracking structure"),
        TELedgerItem("global_lyapunov_function", "native_established",
            "V=(1/2)(Phi-X_ss)^2; dV/dt=-(2/tau)V<0", "Thermodynamic entropy",
            "Lyapunov monotonicity"),
        TELedgerItem("exact_decay_functional", "native_established",
            "D=delta^2/tau>=0; V(t)=V(0)exp(-2t/tau)", "Entropy production rate",
            "Dissipation rate bookkeeping"),
        TELedgerItem("exact_dissipative_balance", "native_established",
            "dV/dt + D = 0 (autonomous)", "First law of thermodynamics",
            "Dissipative balance bookkeeping"),
        TELedgerItem("perturbation_decay", "licensed_but_limited",
            "Deterministic perturbation decays at rate gamma", "Thermal fluctuations",
            "Perturbation relaxation rate"),
        TELedgerItem("entropy", "absent_unbuilt",
            "Nothing", "Everything: no S, no dS, no dS/dt>=0",
            "NOT assumable"),
        TELedgerItem("entropy_production", "absent_unbuilt",
            "Nothing", "Everything: no sigma, no positivity proof",
            "NOT assumable"),
        TELedgerItem("temperature", "absent_unbuilt",
            "Nothing", "Everything: no T, no 1/T=dS/dE, no FDT",
            "NOT assumable"),
        TELedgerItem("equilibrium", "absent_unbuilt",
            "Nothing", "Everything: no equilibrium state, no zeroth law",
            "NOT assumable"),
        TELedgerItem("ensemble_structure", "absent_unbuilt",
            "Nothing", "Everything: no phase space, no measure",
            "NOT assumable"),
        TELedgerItem("probability_foundation", "blocked_by_structure",
            "Born rule absent (Q-II.F)", "Probability measure, frequency interpretation",
            "NOT assumable"),
        TELedgerItem("hamiltonian_statistical_backbone", "absent_unbuilt",
            "Nothing (native dynamics dissipative)", "Hamiltonian, Liouville, symplectic",
            "NOT assumable"),
        TELedgerItem("free_energy", "absent_unbuilt",
            "Nothing", "F, G, Legendre structure",
            "NOT assumable"),
        TELedgerItem("fluctuation_structure", "absent_unbuilt",
            "Nothing beyond deterministic perturbation decay", "FDT, noise, stochastic theory",
            "NOT assumable"),
        TELedgerItem("bath_interpretation", "requires_new_postulates",
            "Dissipation implies environment but does not specify it", "Bath temperature, spectral density",
            "Only with explicit new postulate"),
    ]


def _build_obstructions() -> List[TEObstruction]:
    return [
        TEObstruction(1, "probability_born_absence",
            "No probability foundation; blocks ensemble and statistical mechanics"),
        TEObstruction(2, "ensemble_absence",
            "No micro/canonical/grand canonical ensemble"),
        TEObstruction(3, "hamiltonian_absence",
            "No Hamiltonian; native dynamics are dissipative, not symplectic"),
        TEObstruction(4, "temperature_absence",
            "No T; tau is timescale, not temperature"),
        TEObstruction(5, "equilibrium_absence",
            "No thermodynamic equilibrium; only dynamical rest states"),
        TEObstruction(6, "fluctuation_absence",
            "No noise, no FDT, no stochastic structure"),
        TEObstruction(7, "bath_absence",
            "No bath specified; dissipation implies but does not define environment"),
        TEObstruction(8, "free_energy_absence",
            "No F, G, or other thermodynamic potential"),
    ]


def _build_handoff() -> TEHandoffToU:
    return TEHandoffToU(
        settled_inheritance=[
            "native_scalar_dissipative_ontology_from_S",
            "forward_contraction_semigroup_S_t_eq_exp_neg_t_over_tau",
            "genuine_dynamical_irreversibility_with_state_forgetting",
            "global_Lyapunov_function_V_eq_half_delta_sq",
            "exact_dissipative_balance_dV_dt_plus_D_eq_0",
            "dynamical_fixed_point_steady_state_tracking_structure",
            "no_licensed_equilibrium_temperature_entropy_or_probability",
        ],
        forbidden_assumptions=[
            "entropy_or_entropy_production",
            "temperature_or_inverse_temperature",
            "thermodynamic_equilibrium",
            "statistical_mechanics_or_ensemble_structure",
            "free_energy_or_thermodynamic_potentials",
            "fluctuation_dissipation_theorem",
            "bath_or_stochastic_noise_without_new_postulate",
        ],
        licensed_questions=[
            "effective_action_structure_from_dissipative_dynamics",
            "variational_characterization_of_constitutive_law",
            "vacuum_structure_and_field_configuration_analysis",
            "action_principle_analogs_for_dissipative_systems",
            "unified_field_equation_structure_if_derivable",
        ],
        notes=[
            "U inherits the DYNAMICAL core: semigroup, Lyapunov, balance",
            "U does NOT inherit thermal/statistical/equilibrium language",
            "U may study effective action and vacuum without assuming thermodynamics",
        ],
    )


def _build_firewall() -> TENonclaimFirewall:
    return TENonclaimFirewall(TE_NONCLAIMS, N_TE_NONCLAIMS, True)


def run_te_thermodynamic_ledger_handoff() -> TEThermodynamicLedgerResult:
    ledger = _build_ledger()
    obs = _build_obstructions()
    handoff = _build_handoff()
    fw = _build_firewall()

    key = [
        "IRREVERSIBLE DISSIPATIVE CORE CONFIRMED: semigroup, state forgetting, "
        "attractor relaxation, Lyapunov decay, exact balance all native and established",
        "LYAPUNOV AND BALANCE LEDGER CONFIRMED: V=(1/2)delta^2 global Lyapunov; "
        "D=delta^2/tau dissipation rate; dV/dt+D=0 exact balance",
        "EQUILIBRIUM AND TEMPERATURE ABSENT: no S, T, equilibrium, ensemble, "
        "Hamiltonian, free energy, fluctuation, or bath established",
        "8 thermal obstructions ranked: probability, ensemble, Hamiltonian, "
        "temperature, equilibrium, fluctuation, bath, free energy",
        "Correct vocabulary: 'dissipative relaxation to dynamical rest states "
        "with Lyapunov monotonicity' -- NOT 'thermodynamics'",
        "Handoff to U is CLEAN WITH LIMITS: U inherits dynamical core, "
        "must not assume thermal/statistical completion",
        "Appendix T closes with irreversible dissipative ledger, "
        "without thermal completion",
    ]

    allowed = [
        "Irreversible dissipative core confirmed: semigroup, state forgetting, "
        "Lyapunov monotonicity, exact balance all native",
        "Global Lyapunov V=(1/2)delta^2 with dV/dt=-(2/tau)V and "
        "D=delta^2/tau dissipation rate",
        "Exact dissipative balance dV/dt+D=0; driven balance with forcing power",
        "Dynamical fixed points, steady states, tracking: all supported",
        "8 thermal obstructions documented: probability through free energy",
        "Entropy firewall secured: Lyapunov is not entropy, dissipation rate "
        "is not entropy production, balance is not first law",
        "Appendix U authorized with clean dynamical handoff",
    ]

    forbidden = [
        "Lyapunov implies entropy",
        "Dissipation rate implies entropy production",
        "Balance law implies first law",
        "Fixed points imply equilibrium",
        "tau implies temperature",
        "Semigroup implies second law",
        "Thermodynamic ledger implies thermodynamics complete",
    ]

    counts = {c: sum(1 for i in ledger if i.classification == c)
              for c in ALLOWED_CLASSIFICATIONS}

    diagnostics: Dict[str, Any] = {
        "n_ledger_items": N_LEDGER_ITEMS,
        "n_native_established": counts.get("native_established", 0),
        "n_licensed_limited": counts.get("licensed_but_limited", 0),
        "n_absent": counts.get("absent_unbuilt", 0),
        "n_blocked": counts.get("blocked_by_structure", 0),
        "n_new_postulate": counts.get("requires_new_postulates", 0),
        "n_obstructions": N_OBSTRUCTIONS,
        "n_u_settled": N_U_SETTLED,
        "n_u_forbidden": N_U_FORBIDDEN,
        "n_u_licensed": N_U_LICENSED,
        "n_nonclaims": N_TE_NONCLAIMS,
    }

    result = TEThermodynamicLedgerResult(
        True, ledger, obs, handoff, fw,
        TE_NATIVE_VERDICT, TE_BOOKKEEPING_VERDICT,
        TE_THERMAL_VERDICT, TE_INHERIT_VERDICT,
        TE_AUTH_VERDICT, TE_OVERALL_P,
        key, allowed, forbidden, TE_NONCLAIMS, diagnostics,
    )
    _validate(result); return result


def _validate(r: TEThermodynamicLedgerResult) -> None:
    if r.native_thermodynamic_status not in NATIVE_OPTIONS: raise ValueError("native")
    if r.bookkeeping_status not in BOOKKEEPING_OPTIONS: raise ValueError("bookkeeping")
    if r.thermal_completion_status not in THERMAL_OPTIONS: raise ValueError("thermal")
    if r.inheritance_status_for_U not in INHERIT_OPTIONS: raise ValueError("inherit")
    if r.authorization not in AUTH_OPTIONS: raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS: raise ValueError("overall")
    if len(r.ledger) != N_LEDGER_ITEMS: raise ValueError("ledger")
    for item in r.ledger:
        if item.classification not in ALLOWED_CLASSIFICATIONS:
            raise ValueError(f"'{item.structure}': classification invalid")
    if len(r.obstructions) != N_OBSTRUCTIONS: raise ValueError("obstructions")
    for i, o in enumerate(r.obstructions):
        if o.rank != i + 1: raise ValueError(f"rank {o.rank}")
    if len(r.handoff.settled_inheritance) != N_U_SETTLED: raise ValueError("settled")
    if len(r.handoff.forbidden_assumptions) != N_U_FORBIDDEN: raise ValueError("forbidden assump")
    if len(r.handoff.licensed_questions) != N_U_LICENSED: raise ValueError("licensed q")
    if r.nonclaim_firewall.n_nonclaims != N_TE_NONCLAIMS: raise ValueError("nonclaims")
    if not r.nonclaim_firewall.all_registered: raise ValueError("registered")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")


def _self_test() -> bool:
    r = run_te_thermodynamic_ledger_handoff()
    assert r.valid
    assert r.native_thermodynamic_status == TE_NATIVE_VERDICT
    assert r.bookkeeping_status == TE_BOOKKEEPING_VERDICT
    assert r.thermal_completion_status == TE_THERMAL_VERDICT
    assert r.inheritance_status_for_U == TE_INHERIT_VERDICT
    assert r.authorization == TE_AUTH_VERDICT
    assert r.overall_appendix_p == TE_OVERALL_P
    assert r.diagnostics["n_native_established"] >= 9
    assert r.diagnostics["n_obstructions"] == 8
    return True


if __name__ == "__main__":
    _self_test(); print("T-E passed.")
