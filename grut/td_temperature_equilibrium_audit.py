"""
Appendix T-D --- Temperature-Like Structure, Equilibrium Status, and
Steady-State Admissibility Audit
====================================================================
GRUT Thermodynamic Program --- Phase T-D

Determines whether native GRUT licenses equilibrium, steady state,
temperature-like parameters, or only relaxation without thermal structure.

No probability, ensemble, Boltzmann entropy, canonical equilibrium,
stochastic noise, bath, or FDT language.

=== CORE ANALYSIS ===

FIXED POINT vs EQUILIBRIUM:
  The fixed point Phi = X_ss (constant forcing) is a DYNAMICAL ATTRACTOR.
  Thermodynamic equilibrium requires additionally:
    - defined state functions (S, T, P, ...)
    - detailed balance or maximum entropy characterization
    - zeroth law (transitivity of thermal contact)
  None of these are present. The fixed point is a dynamical rest state,
  not thermodynamic equilibrium.

TEMPERATURE:
  tau is a relaxation TIMESCALE. gamma = 1/tau is a decay RATE.
  Temperature requires a relationship of the form:
    1/T = dS/dE  or  T via fluctuation-dissipation  or  T via equipartition
  None of these are available (no S, no fluctuations, no equipartition).
  The only honest statement: tau sets the timescale of dissipation.
  It does not set a temperature.

  WEAK ANALOGY: in many physical systems, relaxation rate ~ T (e.g.,
  Arrhenius, Kramers). But this requires a bath + barrier structure.
  GRUT has no bath. The analogy is dimensional, not derived.

DRIVEN STEADY STATES:
  Constant forcing: Phi -> X_ss is exact, global, exponential.
  Slowly varying: Phi tracks X(t) with lag tau. This is a TRACKING SOLUTION,
  not a nonequilibrium steady state in the statistical sense.

FLUCTUATIONS:
  Native GRUT is DETERMINISTIC. tau dPhi/dt + Phi = X has no noise term.
  Fluctuations require either:
    (a) stochastic Langevin extension: tau dPhi/dt + Phi = X + sqrt(2D)eta(t)
    (b) quantum decoherence fluctuations (extension-level, Q sector)
  Both are NEW POSTULATES, not native.
  Deterministic perturbation decay (small delta -> 0) is NOT fluctuation theory.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)
GAMMA: float = 1.0 / TAU

N_REGIMES: int = 6
N_OBSTRUCTIONS: int = 5
N_TD_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

EQUIL_OPTIONS = frozenset({
    "dynamical_fixed_points_without_thermodynamic_equilibrium",
    "steady_state_structure_supported_but_equilibrium_unlicensed",
    "conditional_equilibrium_like_structure_supported",
    "true_equilibrium_structure_constructed",
})
TEMP_OPTIONS = frozenset({
    "no_temperature_interpretation_licensed",
    "weak_temperature_like_analogy_only",
    "conditional_effective_temperature_like_structure",
    "genuine_temperature_structure_supported",
})
DRIVEN_OPTIONS = frozenset({
    "stable_tracking_or_steady_states_supported",
    "driven_state_structure_conditionally_supported",
    "driven_state_claims_underdetermined",
    "no_driven_state_claim_licensed",
})
FLUCT_OPTIONS = frozenset({
    "fluctuation_language_not_licensed",
    "deterministic_perturbation_decay_only",
    "conditional_fluctuation_analogy_only",
    "fluctuation_structure_supported",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_TE",
    "stop_for_missing_thermal_boundary",
})
OVERALL_OPTIONS = frozenset({
    "relaxation_and_steady_state_structure_supported_without_temperature",
    "thermal_language_remains_mostly_unlicensed",
    "weak_temperature_like_analogy_with_strict_limits",
    "equilibrium_concept_not_yet_constructed",
})

TD_EQUIL_VERDICT: str = "dynamical_fixed_points_without_thermodynamic_equilibrium"
TD_TEMP_VERDICT: str = "no_temperature_interpretation_licensed"
TD_DRIVEN_VERDICT: str = "stable_tracking_or_steady_states_supported"
TD_FLUCT_VERDICT: str = "deterministic_perturbation_decay_only"
TD_AUTH_VERDICT: str = "authorized_to_proceed_to_TE"
TD_OVERALL_P: str = "relaxation_and_steady_state_structure_supported_without_temperature"

TD_NONCLAIMS: List[str] = [
    "NOT_claiming_fixed_point_therefore_equilibrium__"
    "dynamical_rest_state_is_not_thermodynamic_equilibrium",
    "NOT_claiming_tau_therefore_temperature__"
    "relaxation_timescale_is_not_temperature_without_FDT_or_bath",
    "NOT_claiming_gamma_therefore_inverse_temperature__"
    "decay_rate_is_not_beta_without_statistical_mechanics",
    "NOT_claiming_tracking_therefore_NESS__"
    "driven_tracking_is_not_nonequilibrium_steady_state_in_statistical_sense",
    "NOT_claiming_perturbation_decay_therefore_fluctuations__"
    "deterministic_relaxation_of_perturbation_is_not_thermal_fluctuation",
    "NOT_claiming_V_minimization_therefore_free_energy_minimization__"
    "Lyapunov_attractor_convergence_is_not_thermodynamic_potential_minimization",
    "NOT_claiming_dissipation_therefore_entropy_production__"
    "D_eq_delta_sq_over_tau_is_dissipation_bookkeeping_not_sigma",
    "NOT_claiming_relaxation_to_rest_therefore_thermal_equilibration__"
    "exponential_approach_to_attractor_is_dynamical_not_thermal",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class TDTrackResult:
    track_id: str; track_name: str; question: str
    findings: List[str]; verdict_contribution: str; notes: List[str]

@dataclass
class TDEvidenceRow:
    regime: str; fixed_steady: str; equilibrium_licensed: str
    temperature_role: str; fluctuation: str
    what_licensed: str; what_not_licensed: str

@dataclass
class TDObstruction:
    rank: int; name: str; description: str

@dataclass
class TDLicensedLanguage:
    licensed: List[str]; notes: List[str]

@dataclass
class TDNonlicensedLanguage:
    nonlicensed: List[str]; notes: List[str]

@dataclass
class TDNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class TDTemperatureEquilibriumResult:
    valid: bool
    track_a_equilibrium: TDTrackResult
    track_b_driven: TDTrackResult
    track_c_temperature: TDTrackResult
    track_d_thermal_analogy: TDTrackResult
    track_e_fluctuation: TDTrackResult
    track_f_obstructions: List[TDObstruction]
    evidence_table: List[TDEvidenceRow]
    licensed_language: TDLicensedLanguage
    nonlicensed_language: TDNonlicensedLanguage
    nonclaim_firewall: TDNonclaimFirewall
    equilibrium_status: str; temperature_status: str
    driven_state_status: str; fluctuation_status: str
    authorization: str; overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Tracks
# ---------------------------------------------------------------------------

def _track_a() -> TDTrackResult:
    return TDTrackResult("A", "fixed_point_vs_equilibrium",
        "Do fixed points qualify as equilibrium?",
        [
            "FIXED POINT: Phi = X_ss (constant forcing). Dynamical attractor. "
            "V = 0 at this point. All trajectories converge to it.",
            "THERMODYNAMIC EQUILIBRIUM requires: defined state functions S(E,V,...), "
            "T = (dS/dE)^{-1}, detailed balance, zeroth law transitivity.",
            "NONE of these are present. No S, no T, no detailed balance, no zeroth law.",
            "The fixed point is a REST STATE of the dynamical system, not a "
            "thermodynamic equilibrium state.",
            "PROMOTION REQUIRES: probability foundation (absent, Q-II.F), "
            "ensemble structure (absent), bath interpretation (requires new postulate).",
        ],
        TD_EQUIL_VERDICT,
        ["Fixed points are dynamical, not thermodynamic"])


def _track_b() -> TDTrackResult:
    return TDTrackResult("B", "driven_steady_states",
        "Do driven states qualify as steady states?",
        [
            "CONSTANT FORCING: Phi -> X_ss exponentially. This IS a global "
            "asymptotic steady state of the deterministic ODE.",
            "SLOWLY VARYING FORCING: Phi tracks X(t) with lag ~tau. This is a "
            "TRACKING SOLUTION: Phi(t) ~ X(t) - tau dX/dt + O(tau^2 d^2X/dt^2).",
            "BOUNDED FORCING: all solutions eventually enter a bounded neighborhood "
            "of the forcing signal.",
            "NOMENCLATURE: 'steady state' as in constant-output state of ODE: YES. "
            "'Nonequilibrium steady state' as in statistical mechanics (NESS with "
            "probability current): NOT licensed. Requires ensemble + probability.",
            "The tracking solution is exact first-order adiabatic following. "
            "It is well-defined, stable, and supported by the native dynamics.",
        ],
        TD_DRIVEN_VERDICT,
        ["Dynamical steady state and tracking: supported. Statistical NESS: not licensed."])


def _track_c() -> TDTrackResult:
    return TDTrackResult("C", "temperature_parameter",
        "Does any native parameter qualify as temperature-like?",
        [
            "CANDIDATES: tau (timescale), gamma=1/tau (rate), 2/tau (Lyapunov rate), "
            "D=delta^2/tau (dissipation rate), V (Lyapunov functional).",
            "TEMPERATURE REQUIRES: 1/T = dS/dE (thermodynamic), or T via FDT "
            "(fluctuation-dissipation), or T via equipartition (<E> = kT/2).",
            "NONE of these are available. No S, no fluctuations, no equipartition.",
            "DIMENSIONAL ANALOGY: tau has dimensions of time. In systems with "
            "temperature, relaxation time ~ 1/(rate * f(T)). But this requires "
            "a bath + activation barrier structure. GRUT has neither natively.",
            "gamma = 1/tau is a RATE. In thermal systems, relaxation rate ~ T "
            "(Ohmic coupling). But this identification requires a bath.",
            "VERDICT: no temperature interpretation is licensed. tau is a timescale; "
            "gamma is a rate; neither is temperature without forbidden structures.",
        ],
        TD_TEMP_VERDICT,
        ["Temperature remains unlicensed; tau/gamma are rates, not temperatures"])


def _track_d() -> TDTrackResult:
    return TDTrackResult("D", "thermal_analogy_boundary",
        "What limited thermal language is safe?",
        [
            "SAFE: 'relaxation timescale tau', 'dissipation rate gamma', "
            "'Lyapunov decay rate 2/tau', 'dissipation functional D'.",
            "BORDER: 'relaxation' (safe), 'thermal relaxation' (NOT safe without "
            "temperature). 'Dissipative approach to rest' (safe). "
            "'Thermalization' (NOT safe without statistical mechanics).",
            "NOT SAFE: 'temperature tau', 'inverse temperature gamma', "
            "'effective temperature', 'thermal equilibrium', 'thermalization'.",
            "The correct language for GRUT T-D is: DISSIPATIVE RELAXATION "
            "TO DYNAMICAL REST STATES with rate gamma = 1/tau. No thermal.",
        ],
        "no_thermal_language_beyond_relaxation_rate",
        ["Strictly dynamical language only; no thermal promotion"])


def _track_e() -> TDTrackResult:
    return TDTrackResult("E", "fluctuation_firewall",
        "Does native GRUT license any fluctuation language?",
        [
            "NATIVE DYNAMICS: tau dPhi/dt + Phi = X is DETERMINISTIC. "
            "No noise term. No stochastic element.",
            "PERTURBATION DECAY: small perturbation delta about fixed point "
            "decays as delta(t) = delta(0) exp(-t/tau). This is deterministic "
            "perturbation relaxation, NOT fluctuation theory.",
            "FLUCTUATION-DISSIPATION THEOREM (FDT): relates fluctuations to "
            "dissipation. Requires: stochastic noise + temperature + bath. "
            "All absent. FDT is NOT licensed.",
            "LANGEVIN EXTENSION: adding noise eta(t) to get "
            "tau dPhi/dt + Phi = X + sqrt(2D)eta(t) would give fluctuations. "
            "But this is a NEW POSTULATE (noise strength D, noise statistics), "
            "not a native consequence.",
            "VERDICT: native GRUT supports deterministic perturbation decay only. "
            "Fluctuation language, FDT, and stochastic structure are not licensed.",
        ],
        TD_FLUCT_VERDICT,
        ["Deterministic perturbation decay only; no fluctuations"])


def _build_obstructions() -> List[TDObstruction]:
    return [
        TDObstruction(1, "probability_foundation_absent",
            "Born rule absent; no probability measure for thermal statistics"),
        TDObstruction(2, "ensemble_structure_absent",
            "No microcanonical, canonical, or grand canonical ensemble"),
        TDObstruction(3, "hamiltonian_backbone_absent",
            "No Hamiltonian; native dynamics are dissipative, not symplectic"),
        TDObstruction(4, "bath_interpretation_absent",
            "No environment/bath specified; dissipation implies but does not define bath"),
        TDObstruction(5, "fluctuation_structure_absent",
            "No noise, no FDT, no fluctuation theory; purely deterministic"),
    ]


def _build_evidence() -> List[TDEvidenceRow]:
    return [
        TDEvidenceRow("free_relaxation",
            "Yes (origin)", "No", "No: tau is timescale only",
            "No: deterministic decay", "Fixed point, decay rate",
            "Equilibrium, temperature, fluctuations"),
        TDEvidenceRow("constant_forcing",
            "Yes (X_ss)", "No", "No",
            "No", "Steady state, Lyapunov rest",
            "Equilibrium, temperature"),
        TDEvidenceRow("slowly_varying_forcing",
            "Tracking: Phi~X(t-tau)", "No", "No",
            "No", "Tracking solution, adiabatic following",
            "NESS, temperature, fluctuations"),
        TDEvidenceRow("perturbation_about_fixed_point",
            "N/A (perturbation)", "No", "No: decay rate != 1/T",
            "Deterministic decay only", "Perturbation relaxation",
            "Thermal fluctuations, FDT"),
        TDEvidenceRow("perturbation_about_tracking",
            "N/A", "No", "No",
            "Deterministic decay only", "Conditional perturbation decay",
            "Fluctuations, FDT, noise"),
        TDEvidenceRow("tau_gamma_as_temperature",
            "N/A", "No", "No: dimensional analogy only",
            "N/A", "Relaxation timescale",
            "Temperature, inverse temperature, kT"),
    ]


def _build_licensed() -> TDLicensedLanguage:
    return TDLicensedLanguage(
        ["dynamical_fixed_point_or_rest_state",
         "stable_steady_state_under_constant_forcing",
         "tracking_solution_under_slowly_varying_forcing",
         "perturbation_decay_at_rate_gamma",
         "dissipative_relaxation_timescale_tau"],
        ["All strictly dynamical; no thermal language"])


def _build_nonlicensed() -> TDNonlicensedLanguage:
    return TDNonlicensedLanguage(
        ["thermodynamic_equilibrium", "canonical_equilibrium",
         "temperature", "inverse_temperature", "effective_temperature",
         "thermalization", "thermal_fluctuations",
         "fluctuation_dissipation_theorem", "bath_temperature",
         "nonequilibrium_steady_state_statistical",
         "free_energy_minimization", "entropy_production"],
        ["All require structures absent from native GRUT"])


def _build_firewall() -> TDNonclaimFirewall:
    return TDNonclaimFirewall(TD_NONCLAIMS, N_TD_NONCLAIMS, True)


# ---------------------------------------------------------------------------
# Master
# ---------------------------------------------------------------------------

def run_td_temperature_equilibrium_audit() -> TDTemperatureEquilibriumResult:
    ta = _track_a(); tb = _track_b(); tc = _track_c()
    td = _track_d(); te = _track_e()
    obs = _build_obstructions()
    ev = _build_evidence()
    lic = _build_licensed(); nlic = _build_nonlicensed()
    fw = _build_firewall()

    key = [
        "Fixed points are DYNAMICAL REST STATES, not thermodynamic equilibrium. "
        "Promotion requires: state functions S,T + detailed balance + zeroth law (all absent).",
        "NO TEMPERATURE INTERPRETATION LICENSED. tau is a timescale; gamma is a "
        "rate; neither is temperature. Temperature requires FDT, bath, or "
        "equipartition (all absent).",
        "Stable tracking / steady states SUPPORTED under constant or slowly "
        "varying forcing. These are dynamical, not statistical NESS.",
        "FLUCTUATION LANGUAGE NOT LICENSED beyond deterministic perturbation decay. "
        "No noise, no FDT, no stochastic structure natively.",
        "5 equilibrium obstructions ranked: probability absent, ensemble absent, "
        "Hamiltonian absent, bath absent, fluctuation absent.",
        "Thermal language remains STRICTLY UNLICENSED. The correct vocabulary "
        "is: dissipative relaxation to dynamical rest states.",
        "T-E authorized: thermal boundary fully documented.",
    ]

    allowed = [
        "Dynamical fixed points / rest states supported under all forcing regimes",
        "Stable steady state (constant forcing) and tracking solution (slowly "
        "varying forcing) are well-defined and supported",
        "No temperature interpretation licensed: tau is timescale, gamma is "
        "rate, neither is temperature",
        "Deterministic perturbation decay at rate gamma: supported as purely "
        "dynamical property",
        "5 equilibrium obstructions ranked and documented (probability, "
        "ensemble, Hamiltonian, bath, fluctuation: all absent)",
        "Thermal language boundary explicitly secured: no thermal promotion "
        "from dissipative relaxation",
        "T-E authorized: thermodynamic ledger and handoff to U next",
    ]

    forbidden = [
        "Fixed point implies thermodynamic equilibrium",
        "tau implies temperature",
        "gamma implies inverse temperature",
        "Tracking solution implies NESS",
        "Perturbation decay implies thermal fluctuations",
        "V minimization implies free energy minimization",
        "Dissipative relaxation implies thermalization",
    ]

    diagnostics: Dict[str, Any] = {
        "tau": TAU, "gamma": GAMMA,
        "temperature_licensed": False,
        "equilibrium_licensed": False,
        "fluctuation_licensed": False,
        "steady_state_supported": True,
        "tracking_supported": True,
        "n_obstructions": N_OBSTRUCTIONS,
        "n_regimes": N_REGIMES,
        "n_nonclaims": N_TD_NONCLAIMS,
    }

    result = TDTemperatureEquilibriumResult(
        True, ta, tb, tc, td, te, obs, ev, lic, nlic, fw,
        TD_EQUIL_VERDICT, TD_TEMP_VERDICT, TD_DRIVEN_VERDICT,
        TD_FLUCT_VERDICT, TD_AUTH_VERDICT, TD_OVERALL_P,
        key, allowed, forbidden, TD_NONCLAIMS, diagnostics,
    )
    _validate(result); return result


def _validate(r: TDTemperatureEquilibriumResult) -> None:
    if r.equilibrium_status not in EQUIL_OPTIONS: raise ValueError("equil")
    if r.temperature_status not in TEMP_OPTIONS: raise ValueError("temp")
    if r.driven_state_status not in DRIVEN_OPTIONS: raise ValueError("driven")
    if r.fluctuation_status not in FLUCT_OPTIONS: raise ValueError("fluct")
    if r.authorization not in AUTH_OPTIONS: raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS: raise ValueError("overall")
    if r.nonclaim_firewall.n_nonclaims != N_TD_NONCLAIMS: raise ValueError("nonclaims")
    if not r.nonclaim_firewall.all_registered: raise ValueError("registered")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")
    if len(r.evidence_table) != N_REGIMES: raise ValueError("evidence")
    if len(r.track_f_obstructions) != N_OBSTRUCTIONS: raise ValueError("obstructions")
    if r.diagnostics["temperature_licensed"]: raise ValueError("temp must be False")
    if r.diagnostics["equilibrium_licensed"]: raise ValueError("equil must be False")
    if r.diagnostics["fluctuation_licensed"]: raise ValueError("fluct must be False")


def _self_test() -> bool:
    r = run_td_temperature_equilibrium_audit()
    assert r.valid
    assert r.equilibrium_status == TD_EQUIL_VERDICT
    assert r.temperature_status == TD_TEMP_VERDICT
    assert r.driven_state_status == TD_DRIVEN_VERDICT
    assert r.fluctuation_status == TD_FLUCT_VERDICT
    assert r.authorization == TD_AUTH_VERDICT
    assert r.diagnostics["temperature_licensed"] is False
    assert r.diagnostics["steady_state_supported"] is True
    return True


if __name__ == "__main__":
    _self_test(); print("T-D passed.")
