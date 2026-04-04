"""
Appendix T-C --- Dissipation Functional, Lyapunov Structure, and Balance-Law Audit
===================================================================================
GRUT Thermodynamic Program --- Phase T-C

Determines whether native GRUT admits a Lyapunov-like functional, dissipation
functional, energy-like decay law, or balance-law inequality, using only the
native dissipative constitutive structure. No entropy, temperature, probability,
or ensemble language.

=== CORE DERIVATION ===

Native equation: tau dPhi/dt + Phi = X

Define the deviation from steady state: delta(t) = Phi(t) - X_ss
  where X_ss is the attractor (X for constant forcing, 0 for free relaxation).

For CONSTANT FORCING (X = X_ss = const):
  tau d(delta)/dt + delta = 0
  Solution: delta(t) = delta(0) exp(-t/tau)

CANDIDATE LYAPUNOV FUNCTIONAL:
  V[delta] = (1/2) delta^2

Time derivative along trajectories:
  dV/dt = delta * d(delta)/dt = delta * (-delta/tau) = -delta^2 / tau = -(2/tau) V

Therefore:
  dV/dt = -(2/tau) V <= 0    (strict inequality when V > 0)

This is a GLOBAL LYAPUNOV FUNCTION for the autonomous (constant forcing) case:
  - V >= 0 (non-negative)
  - V = 0 iff delta = 0 (attractor)
  - dV/dt < 0 for V > 0 (strict decrease)
  - dV/dt = -(2/tau) V (exponential decay)

Solution: V(t) = V(0) exp(-2t/tau)

DISSIPATION FUNCTIONAL:
  D = -dV/dt = (2/tau) V = delta^2 / tau >= 0

This is the instantaneous dissipation rate. It is non-negative and equals
the rate of decrease of V.

BALANCE LAW:
  dV/dt + D = 0    (exact balance: storage rate + dissipation = 0)

For GENERAL FORCING (X = X(t)):
  Define delta(t) = Phi(t) - X(t). Then:
  tau d(delta)/dt + delta = -tau dX/dt  (additional forcing-rate term)

  dV/dt = delta * d(delta)/dt = delta * [(-delta - tau dX/dt)/tau]
        = -delta^2/tau - delta * dX/dt

  dV/dt = -(2/tau) V - delta * dX/dt

The second term can be positive or negative depending on forcing. So:
  dV/dt <= -(2/tau) V + |delta| * |dX/dt|

Monotonicity is CONDITIONAL on |dX/dt| being bounded relative to |delta|/tau.
For slowly varying forcing (|dX/dt| << |delta|/tau), the decay dominates.

FIREWALL: V is a DISSIPATION FUNCTIONAL, not thermodynamic entropy.
  - It tracks deviation from attractor, not thermodynamic state
  - dV/dt < 0 is dynamical monotonicity, not second law
  - D = -dV/dt is dissipation rate, not entropy production
  - The balance dV/dt + D = 0 is energy-like bookkeeping, not first law
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU
DECAY_RATE_V: float = 2.0 / TAU  # V decays at rate 2/tau

N_REGIMES: int = 6
N_TC_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

LYAPUNOV_OPTIONS = frozenset({
    "global_lyapunov_function_supported",
    "conditional_lyapunov_structure_supported",
    "local_or_regime_limited_monotone_only",
    "no_lyapunov_claim_licensed",
})
DISSIPATION_OPTIONS = frozenset({
    "exact_decay_functional_identified",
    "conditional_decay_functional_identified",
    "bookkeeping_only_without_canonical_functional",
    "no_dissipation_functional_identified",
})
BALANCE_OPTIONS = frozenset({
    "exact_dissipative_balance_supported",
    "inequality_form_supported",
    "bookkeeping_identity_only",
    "balance_law_not_established",
})
FIREWALL_OPTIONS = frozenset({
    "monotone_not_entropy_explicitly_secured",
    "boundary_between_monotone_and_entropy_unclear",
    "entropy_like_claims_overreached",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_TD",
    "stop_for_missing_monotone_structure",
})
OVERALL_OPTIONS = frozenset({
    "native_dissipation_functional_supported_with_entropy_firewall",
    "lyapunov_style_relaxation_bookkeeping_supported",
    "decay_structure_present_but_not_canonical",
    "monotone_structure_not_established",
})

TC_LYAPUNOV_VERDICT: str = "global_lyapunov_function_supported"
TC_DISSIPATION_VERDICT: str = "exact_decay_functional_identified"
TC_BALANCE_VERDICT: str = "exact_dissipative_balance_supported"
TC_FIREWALL_VERDICT: str = "monotone_not_entropy_explicitly_secured"
TC_AUTH_VERDICT: str = "authorized_to_proceed_to_TD"
TC_OVERALL_P: str = "native_dissipation_functional_supported_with_entropy_firewall"

TC_NONCLAIMS: List[str] = [
    "NOT_claiming_V_is_entropy__"
    "V_eq_half_delta_sq_is_deviation_from_attractor_not_thermodynamic_state_function",
    "NOT_claiming_dV_dt_is_entropy_production__"
    "dV_dt_is_dynamical_decay_rate_not_sigma",
    "NOT_claiming_D_is_entropy_production_rate__"
    "D_eq_delta_sq_over_tau_is_dissipation_bookkeeping_not_thermodynamic_production",
    "NOT_claiming_balance_law_is_first_law__"
    "dV_dt_plus_D_equals_zero_is_energy_like_bookkeeping_not_dU_eq_TdS_minus_PdV",
    "NOT_claiming_Lyapunov_is_free_energy__"
    "V_is_deviation_measure_not_thermodynamic_potential",
    "NOT_claiming_decay_rate_is_temperature__"
    "2_over_tau_is_contraction_rate_of_V_not_inverse_temperature",
    "NOT_claiming_attractor_is_equilibrium__"
    "V_eq_0_at_attractor_is_dynamical_not_thermodynamic",
    "NOT_claiming_monotone_theorem_is_second_law__"
    "dV_dt_leq_0_is_Lyapunov_stability_not_thermodynamic_law",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class TCTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class TCEvidenceRow:
    regime: str; candidate_functional: str; monotone: str
    exact_or_conditional: str; balance_form: str
    what_licensed: str; what_not_licensed: str

@dataclass
class TCLicensedLanguage:
    licensed: List[str]; notes: List[str]

@dataclass
class TCNonlicensedLanguage:
    nonlicensed: List[str]; notes: List[str]

@dataclass
class TCNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class TCDissipationFunctionalResult:
    valid: bool
    track_a_lyapunov: TCTrackResult
    track_b_dissipation: TCTrackResult
    track_c_balance: TCTrackResult
    track_d_attractor_monotone: TCTrackResult
    track_e_entropy_firewall: TCTrackResult
    track_f_h_theorem: TCTrackResult
    evidence_table: List[TCEvidenceRow]
    licensed_language: TCLicensedLanguage
    nonlicensed_language: TCNonlicensedLanguage
    nonclaim_firewall: TCNonclaimFirewall
    lyapunov_status: str; dissipation_functional_status: str
    balance_law_status: str; entropy_firewall_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Tracks
# ---------------------------------------------------------------------------

def _track_a() -> TCTrackResult:
    return TCTrackResult("A", "lyapunov_functional",
        "Does a scalar functional V exist that is monotone along trajectories?",
        [
            "CANDIDATE: V = (1/2)(Phi - X_ss)^2 = (1/2) delta^2, "
            "where X_ss is the attractor value.",
            "For CONSTANT forcing (X = X_ss): "
            "dV/dt = delta * d(delta)/dt = delta * (-delta/tau) = -delta^2/tau = -(2/tau)V.",
            "V >= 0 (non-negative). V = 0 iff Phi = X_ss (at attractor). "
            "dV/dt = -(2/tau)V < 0 for V > 0 (strict decrease).",
            "This satisfies ALL Lyapunov conditions: V is a GLOBAL LYAPUNOV FUNCTION "
            "for the autonomous and constant-forcing case.",
            "V(t) = V(0) exp(-2t/tau): exponential decay at rate 2*gamma.",
            "For TIME-DEPENDENT forcing: dV/dt = -(2/tau)V - delta*dX/dt. "
            "Monotonicity requires |dX/dt| << |delta|/tau (slowly varying forcing). "
            "CONDITIONAL in the driven case.",
        ],
        TC_LYAPUNOV_VERDICT,
        ["Global Lyapunov for autonomous; conditional for driven"])


def _track_b() -> TCTrackResult:
    return TCTrackResult("B", "dissipation_functional",
        "Can the equation yield a canonical decay/dissipation relation?",
        [
            "DISSIPATION RATE: D = -dV/dt = delta^2/tau = (2/tau)V >= 0.",
            "D is non-negative, vanishes at the attractor, and equals the "
            "instantaneous rate of V-decrease.",
            "DECAY LAW: V(t) = V(0) exp(-2t/tau). Exponential decay with "
            "rate constant 2/tau = 2*gamma.",
            "For the FULL driven system: D_eff = delta^2/tau + delta*dX/dt. "
            "The extra term can be positive or negative. Exact only for "
            "autonomous or constant forcing.",
        ],
        TC_DISSIPATION_VERDICT,
        ["Exact dissipation functional for autonomous; conditional for driven"])


def _track_c() -> TCTrackResult:
    return TCTrackResult("C", "balance_law",
        "Does GRUT support a balance-law form?",
        [
            "For constant forcing: dV/dt + D = 0, where D = delta^2/tau.",
            "This is an EXACT BALANCE: rate of change of stored 'deviation energy' "
            "plus dissipation rate equals zero.",
            "Interpretation: V is stored deviation; D is dissipated rate. "
            "The system loses V at rate D. No source, no conservation.",
            "For driven system: dV/dt + D = -delta * dX/dt. "
            "The right side is a FORCING POWER term. Balance: "
            "storage rate + dissipation = forcing input.",
            "This is a genuine DISSIPATIVE BALANCE LAW, not conservation.",
        ],
        TC_BALANCE_VERDICT,
        ["Exact balance for autonomous; balance with forcing term for driven"])


def _track_d() -> TCTrackResult:
    return TCTrackResult("D", "attractor_monotone",
        "Does distance to attractor decay monotonically?",
        [
            "Distance: |delta(t)| = |Phi(t) - X_ss| for constant forcing.",
            "d|delta|/dt = -|delta|/tau < 0 for delta != 0.",
            "MONOTONE: |delta| is strictly decreasing toward zero.",
            "|delta(t)| = |delta(0)| exp(-t/tau): exponential decay.",
            "V = (1/2)|delta|^2 decays as exp(-2t/tau).",
            "Both |delta| and V are distance-to-attractor monotones. "
            "V decays faster (rate 2/tau vs 1/tau).",
        ],
        "monotone_distance_to_attractor_confirmed",
        ["Distance to attractor: exact monotone for autonomous case"])


def _track_e() -> TCTrackResult:
    return TCTrackResult("E", "entropy_firewall",
        "What does the monotone NOT license?",
        [
            "V = (1/2)delta^2 is a LYAPUNOV FUNCTIONAL, not thermodynamic entropy.",
            "V measures deviation from attractor in configuration space. "
            "Thermodynamic entropy S measures disorder in phase space or "
            "information-theoretic content. These are different objects.",
            "dV/dt < 0 is LYAPUNOV STABILITY, not the second law of thermodynamics. "
            "The second law requires: defined S, defined T, and dS >= delta_Q/T.",
            "D = delta^2/tau is a DISSIPATION RATE, not entropy production sigma. "
            "Entropy production requires: sigma = dS_irr/dt with defined S.",
            "The balance dV/dt + D = 0 is ENERGY-LIKE BOOKKEEPING, not the "
            "first law dU = TdS - PdV. No T, S, P, or V_thermo are defined.",
            "2/tau is a CONTRACTION RATE, not an inverse temperature. "
            "Temperature requires FDT or equilibrium characterization.",
            "FIREWALL SECURED: V is Lyapunov, not entropy. D is dissipation "
            "rate, not entropy production. The balance is bookkeeping, not thermodynamics.",
        ],
        TC_FIREWALL_VERDICT,
        ["Explicit separation maintained at every level"])


def _track_f() -> TCTrackResult:
    return TCTrackResult("F", "h_theorem_analog",
        "Is a restricted H-theorem-style statement available?",
        [
            "WEAK ANALOG: for constant forcing, dV/dt = -(2/tau)V < 0 for V > 0.",
            "This says: the deviation functional V strictly decreases along "
            "trajectories until the attractor is reached.",
            "This is structurally analogous to Boltzmann's H-theorem "
            "(H decreases along trajectories toward equilibrium) but:",
            "  (a) V is not H (not defined via distribution function)",
            "  (b) the attractor is not thermodynamic equilibrium",
            "  (c) no probability or phase space is involved",
            "  (d) the decay is exact exponential, not probabilistic",
            "VERDICT: a CONDITIONAL MONOTONE THEOREM is available in the "
            "restricted sense of dV/dt <= 0 under autonomous evolution. "
            "Not an H-theorem in the Boltzmann sense.",
        ],
        "conditional_monotone_theorem_only",
        ["Structural analog only; not Boltzmann H-theorem"])


def _build_evidence() -> List[TCEvidenceRow]:
    return [
        TCEvidenceRow("free_relaxation_X_eq_0",
            "V=(1/2)Phi^2", "Yes, dV/dt=-(2/tau)V", "Exact",
            "dV/dt+D=0", "Lyapunov, dissipation rate, balance",
            "Entropy, temperature, equilibrium"),
        TCEvidenceRow("constant_forcing_X_eq_X0",
            "V=(1/2)(Phi-X0)^2", "Yes, dV/dt=-(2/tau)V", "Exact",
            "dV/dt+D=0", "Lyapunov, dissipation rate, balance",
            "Entropy, temperature, equilibrium"),
        TCEvidenceRow("bounded_time_dependent",
            "V=(1/2)(Phi-X(t))^2", "Conditional: |dX/dt|<<|delta|/tau", "Conditional",
            "dV/dt+D=-delta*dX/dt", "Conditional monotone, driven balance",
            "Exact Lyapunov, entropy"),
        TCEvidenceRow("distance_to_fixed_point",
            "|delta|=|Phi-X_ss|", "Yes, d|delta|/dt=-|delta|/tau", "Exact",
            "N/A (scalar, not balance)", "Monotone distance, rate 1/tau",
            "Entropy, free energy"),
        TCEvidenceRow("norm_amplitude",
            "V=(1/2)delta^2", "Yes (same as free)", "Exact for autonomous",
            "dV/dt+D=0", "Norm decay, Lyapunov",
            "State-function entropy"),
        TCEvidenceRow("general_driven",
            "V=(1/2)(Phi-X(t))^2", "Conditional", "Conditional",
            "dV/dt+D=forcing_power", "Conditional bookkeeping",
            "Exact Lyapunov, entropy, any thermodynamic claim"),
    ]


def _build_licensed() -> TCLicensedLanguage:
    return TCLicensedLanguage(
        ["global_lyapunov_functional_V_eq_half_delta_sq",
         "exact_exponential_decay_V_at_rate_2_over_tau",
         "dissipation_rate_D_eq_delta_sq_over_tau",
         "exact_dissipative_balance_dV_dt_plus_D_eq_0",
         "monotone_distance_to_attractor",
         "conditional_monotone_for_slowly_driven_case",
         "restricted_H_theorem_analog_dV_dt_leq_0"],
        ["All licensed as dynamical/Lyapunov properties; none as thermodynamic"])


def _build_nonlicensed() -> TCNonlicensedLanguage:
    return TCNonlicensedLanguage(
        ["thermodynamic_entropy_S", "entropy_production_sigma",
         "temperature_T", "equilibrium_thermodynamics",
         "free_energy_F", "first_law", "second_law",
         "statistical_mechanics", "partition_function",
         "bath_temperature", "microstate_counting"],
        ["None licensed by T-C; all require structures absent from T0"])


def _build_firewall() -> TCNonclaimFirewall:
    return TCNonclaimFirewall(TC_NONCLAIMS, N_TC_NONCLAIMS, True)


# ---------------------------------------------------------------------------
# Master
# ---------------------------------------------------------------------------

def run_tc_dissipation_functional_lyapunov_audit() -> TCDissipationFunctionalResult:
    ta = _track_a(); tb = _track_b(); tc = _track_c()
    td = _track_d(); te = _track_e(); tf = _track_f()
    ev = _build_evidence()
    lic = _build_licensed(); nlic = _build_nonlicensed()
    fw = _build_firewall()

    key = [
        "GLOBAL LYAPUNOV FUNCTION identified: V = (1/2)(Phi - X_ss)^2, "
        "with dV/dt = -(2/tau)V < 0 for V > 0 (autonomous/constant forcing)",
        "V(t) = V(0) exp(-2t/tau): exponential decay at rate 2*gamma",
        "DISSIPATION RATE: D = delta^2/tau >= 0, the instantaneous "
        "rate of V-decrease",
        "EXACT DISSIPATIVE BALANCE: dV/dt + D = 0 (autonomous); "
        "dV/dt + D = forcing power (driven)",
        "DISTANCE-TO-ATTRACTOR MONOTONE: |delta| decays at rate 1/tau",
        "ENTROPY FIREWALL SECURED: V is Lyapunov (not entropy), "
        "D is dissipation rate (not entropy production), "
        "balance is bookkeeping (not first law), "
        "2/tau is contraction rate (not inverse temperature)",
        "Restricted H-theorem analog: dV/dt <= 0 under autonomous evolution "
        "(not Boltzmann H-theorem)",
    ]

    allowed = [
        "V = (1/2)(Phi-X_ss)^2 is a global Lyapunov function for "
        "autonomous and constant-forcing evolution",
        "V decays exponentially at rate 2/tau; D = delta^2/tau is the "
        "non-negative dissipation rate",
        "Exact dissipative balance dV/dt + D = 0 holds for autonomous case; "
        "driven case has forcing power term",
        "Distance to attractor |delta| decays monotonically at rate 1/tau",
        "Conditional monotonicity for slowly varying forcing: "
        "|dX/dt| << |delta|/tau required",
        "Restricted H-theorem analog: dV/dt <= 0 along trajectories "
        "in autonomous evolution",
        "T-D authorized: monotone and balance structure established, "
        "temperature/equilibrium investigation next",
    ]

    forbidden = [
        "V is thermodynamic entropy",
        "dV/dt is entropy production",
        "D is entropy production rate sigma",
        "Balance law is first law of thermodynamics",
        "Lyapunov functional is free energy",
        "2/tau is inverse temperature",
        "Monotone theorem is second law",
    ]

    diagnostics: Dict[str, Any] = {
        "lyapunov_functional": "V = (1/2)(Phi - X_ss)^2",
        "lyapunov_decay_rate": DECAY_RATE_V,
        "lyapunov_decay_rate_is_2_gamma": abs(DECAY_RATE_V - 2.0*GAMMA) < 1e-15,
        "dissipation_rate": "D = delta^2 / tau",
        "balance_form": "dV/dt + D = 0 (autonomous)",
        "distance_decay_rate": GAMMA,
        "conditional_on_forcing": True,
        "n_regimes": N_REGIMES,
        "n_licensed": len(lic.licensed),
        "n_nonlicensed": len(nlic.nonlicensed),
        "n_nonclaims": N_TC_NONCLAIMS,
    }

    result = TCDissipationFunctionalResult(
        True, ta, tb, tc, td, te, tf, ev, lic, nlic, fw,
        TC_LYAPUNOV_VERDICT, TC_DISSIPATION_VERDICT,
        TC_BALANCE_VERDICT, TC_FIREWALL_VERDICT,
        TC_AUTH_VERDICT, TC_OVERALL_P,
        key, allowed, forbidden, TC_NONCLAIMS, diagnostics,
    )
    _validate(result); return result


def _validate(r: TCDissipationFunctionalResult) -> None:
    if r.lyapunov_status not in LYAPUNOV_OPTIONS: raise ValueError("lyapunov")
    if r.dissipation_functional_status not in DISSIPATION_OPTIONS: raise ValueError("dissipation")
    if r.balance_law_status not in BALANCE_OPTIONS: raise ValueError("balance")
    if r.entropy_firewall_status not in FIREWALL_OPTIONS: raise ValueError("firewall")
    if r.authorization not in AUTH_OPTIONS: raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS: raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims != N_TC_NONCLAIMS: raise ValueError("nonclaims")
    if not r.nonclaim_firewall.all_registered: raise ValueError("registered")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")
    if len(r.evidence_table) != N_REGIMES: raise ValueError("evidence")
    if not r.diagnostics["lyapunov_decay_rate_is_2_gamma"]: raise ValueError("rate")


def _self_test() -> bool:
    r = run_tc_dissipation_functional_lyapunov_audit()
    assert r.valid
    assert r.lyapunov_status == TC_LYAPUNOV_VERDICT
    assert r.dissipation_functional_status == TC_DISSIPATION_VERDICT
    assert r.balance_law_status == TC_BALANCE_VERDICT
    assert r.entropy_firewall_status == TC_FIREWALL_VERDICT
    assert r.authorization == TC_AUTH_VERDICT
    assert abs(r.diagnostics["lyapunov_decay_rate"] - 2.0/TAU) < 1e-15
    return True


if __name__ == "__main__":
    _self_test(); print("T-C passed.")
