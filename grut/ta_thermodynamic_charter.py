"""
Appendix T-A --- Thermodynamic Charter
========================================
GRUT Thermodynamic Program --- Phase T-A

Defines rules, prohibitions, mandatory distinctions, and admissible claim
structure for all later thermodynamic stages. Opens thermodynamics under
constraint; does not construct thermodynamic theory.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List

STAGES: List[str] = [
    "T0_thermodynamic_entry_inventory",
    "T-A_thermodynamic_charter",
    "T-B_irreversibility_and_semigroup_structure",
    "T-C_entropy_like_monotones_and_dissipation_functionals",
    "T-D_temperature_equilibrium_and_fluctuation_structure",
    "T-E_thermodynamic_ledger_and_handoff_to_U",
]
N_STAGES: int = 6
N_DISTINCTIONS: int = 10
N_RULES: int = 7
N_FFMS: int = 8
N_TA_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

FFM_NAMES: List[str] = [
    "entropy_from_dissipation_alone",
    "entropy_increase_from_time_asymmetry_alone",
    "temperature_from_tau_alone",
    "ensemble_without_probability",
    "free_energy_without_state_variables",
    "equilibrium_from_fixed_point_alone",
    "fluctuation_dissipation_without_derivation",
    "statistical_mechanics_from_decoherence",
]

TA_NONCLAIMS: List[str] = [
    "NOT_claiming_charter_constructs_thermodynamics__"
    "charter_defines_rules_not_results",
    "NOT_claiming_dissipation_is_thermodynamics__"
    "dissipation_is_prerequisite_not_completion",
    "NOT_claiming_irreversibility_proven__"
    "directionality_is_candidate_not_proof",
    "NOT_claiming_entropy_or_temperature_established__"
    "both_require_later_derivation_if_possible",
    "NOT_claiming_equilibrium_defined__"
    "attractor_is_not_thermodynamic_equilibrium",
    "NOT_claiming_statistical_mechanics_available__"
    "probability_foundation_absent",
    "NOT_claiming_stage_success_guaranteed__"
    "each_stage_may_yield_BSR",
    "NOT_claiming_authorization_implies_thermodynamic_closure__"
    "authorization_means_licensed_not_solved",
]

ALLOWED_CHARTER_VERDICTS = frozenset({
    "charter_defined_with_strict_prohibitions",
    "charter_incomplete",
})
CHARTER_VERDICT: str = "charter_defined_with_strict_prohibitions"
AUTH_VERDICT: str = "authorized_to_proceed_to_TB"
OVERALL_P: str = "thermodynamic_program_opened_under_strict_limits"


@dataclass
class TADistinction:
    distinction_id: str; left: str; right: str
    explanation: str; notes: List[str]

@dataclass
class TAStageDef:
    stage_id: str; stage_name: str; stage_index: int
    primary_question: str; success_type: str; notes: List[str]

@dataclass
class TARule:
    rule_id: str; statement: str; violation: str; notes: List[str]

@dataclass
class TAFFM:
    mode_id: str; name: str; description: str
    why_forbidden: str; notes: List[str]

@dataclass
class TANonclaims:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class TATBLicensed:
    licensed_tests: List[str]; notes: List[str]

@dataclass
class TACharter:
    valid: bool
    distinctions: List[TADistinction]
    stage_sequence: List[TAStageDef]
    rules: List[TARule]
    ffms: List[TAFFM]
    entry_nonclaims: TANonclaims
    tb_licensed: TATBLicensed
    charter_verdict: str; authorization_verdict: str
    overall_appendix_p: str
    key_findings: List[str]
    allowed_claims: List[str]; forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _distinctions() -> List[TADistinction]:
    return [
        TADistinction("D1","dissipation","thermodynamics",
            "Dissipation is energy loss to environment; thermodynamics is a "
            "complete framework with state functions, potentials, and laws.",[]),
        TADistinction("D2","time_asymmetry","irreversibility",
            "Time asymmetry is directional evolution; irreversibility is "
            "proven non-invertibility of the dynamical map.",[]),
        TADistinction("D3","irreversibility","entropy_increase",
            "Irreversibility is a dynamical property; entropy increase is a "
            "thermodynamic law requiring defined entropy function.",[]),
        TADistinction("D4","relaxation_scale","temperature",
            "tau is a relaxation timescale; temperature requires FDT, bath "
            "structure, or equilibrium characterization.",[]),
        TADistinction("D5","balance_law","conservation_law",
            "Balance law tracks flow through open system; conservation law "
            "requires closed system with Noether symmetry.",[]),
        TADistinction("D6","late_time_relaxation","equilibrium",
            "Relaxation to fixed point is dynamical; equilibrium is "
            "thermodynamic state with defined state functions.",[]),
        TADistinction("D7","entropy_like_monotone","thermodynamic_entropy",
            "A monotone under evolution is mathematical; thermodynamic entropy "
            "requires S(E,V,...) with derivatives giving T, P, etc.",[]),
        TADistinction("D8","effective_analogy","native_derivation",
            "Effective analogy maps GRUT structures to known forms; native "
            "derivation proves the structure from GRUT axioms.",[]),
        TADistinction("D9","nonequilibrium_description","statistical_mechanics",
            "Nonequilibrium description tracks dissipative dynamics; statistical "
            "mechanics requires ensemble, measure, and probability.",[]),
        TADistinction("D10","state_function_language","phenomenological_monotonicity",
            "State functions are exact differentials with Legendre structure; "
            "phenomenological monotonicity is observed decrease without state function.",[]),
    ]


def _stages() -> List[TAStageDef]:
    return [
        TAStageDef("T0","Thermodynamic entry inventory",0,
            "What thermodynamic-relevant structures are present?",
            "success",[]),
        TAStageDef("T-A","Thermodynamic charter",1,
            "What rules govern thermodynamic claims?",
            "success",[]),
        TAStageDef("T-B","Irreversibility and semigroup structure",2,
            "Is native dissipative evolution genuinely irreversible?",
            "extension_level_outcome",
            ["Tests: semigroup property, non-invertibility, recoverability"]),
        TAStageDef("T-C","Entropy-like monotones and dissipation functionals",3,
            "Does a monotonically decreasing/increasing functional exist?",
            "extension_level_outcome",
            ["Tests: Lyapunov candidates, dissipation functionals, H-theorem analogs"]),
        TAStageDef("T-D","Temperature, equilibrium, and fluctuation structure",4,
            "Can temperature-like or equilibrium-like structure be defined?",
            "extension_level_outcome",
            ["Tests: FDT candidates, bath interpretation, equilibrium conditions"]),
        TAStageDef("T-E","Thermodynamic ledger and handoff to U",5,
            "Final thermodynamic map and inheritance for Appendix U.",
            "bounded_negative_result",
            ["Synthesizes T-B through T-D; produces handoff"]),
    ]


def _rules() -> List[TARule]:
    return [
        TARule("T-R1","Every thermodynamic claim carries Appendix P class.",
            "undisciplined_claim",[]),
        TARule("T-R2","Entropy claims require defined S with derivation.",
            "entropy_without_derivation",[]),
        TARule("T-R3","Temperature claims require FDT, bath, or equilibrium link.",
            "temperature_without_foundation",[]),
        TARule("T-R4","Equilibrium claims require thermodynamic state functions.",
            "equilibrium_without_state_functions",[]),
        TARule("T-R5","Statistical claims require probability foundation.",
            "statistics_without_probability",[]),
        TARule("T-R6","All 10 mandatory distinctions must be maintained.",
            "distinction_collapse",[]),
        TARule("T-R7","S-E locked classes persist into T.",
            "retroactive_promotion",[]),
    ]


def _ffms() -> List[TAFFM]:
    return [
        TAFFM("FFM-T.1","entropy_from_dissipation_alone",
            "Claiming entropy S from dissipation without deriving S.",
            "Dissipation is energy loss; entropy requires state function.",[]),
        TAFFM("FFM-T.2","entropy_increase_from_time_asymmetry_alone",
            "Claiming dS/dt >= 0 from directional evolution.",
            "Time asymmetry is necessary but not sufficient for entropy increase.",[]),
        TAFFM("FFM-T.3","temperature_from_tau_alone",
            "Claiming T ~ 1/tau or T ~ tau without FDT or bath.",
            "tau is timescale; T requires thermodynamic foundation.",[]),
        TAFFM("FFM-T.4","ensemble_without_probability",
            "Assuming micro/canonical ensemble without Born rule.",
            "Ensemble theory requires probability measure (absent).",[]),
        TAFFM("FFM-T.5","free_energy_without_state_variables",
            "Claiming F = U - TS without defined U, T, S.",
            "All three prerequisites absent or unbuilt.",[]),
        TAFFM("FFM-T.6","equilibrium_from_fixed_point_alone",
            "Claiming thermodynamic equilibrium from ODE fixed point.",
            "Fixed point is dynamical attractor, not thermodynamic equilibrium.",[]),
        TAFFM("FFM-T.7","fluctuation_dissipation_without_derivation",
            "Assuming FDT without deriving it from GRUT dynamics.",
            "FDT relates fluctuations to dissipation; requires explicit proof.",[]),
        TAFFM("FFM-T.8","statistical_mechanics_from_decoherence",
            "Claiming statistical mechanics from decoherence/pointer basis.",
            "Decoherence selects basis; does not provide ensemble or probability.",[]),
    ]


def run_ta_thermodynamic_charter() -> TACharter:
    dist = _distinctions(); stg = _stages()
    rul = _rules(); ffm = _ffms()
    nc = TANonclaims(TA_NONCLAIMS, N_TA_NONCLAIMS, True)
    tb = TATBLicensed(
        ["test_semigroup_property_of_dissipative_evolution",
         "test_non_invertibility_of_constitutive_map",
         "test_recoverability_or_lack_thereof",
         "test_whether_time_asymmetry_constitutes_irreversibility"],
        ["T-B scope is strictly: irreversibility and semigroup structure"])

    key = [
        "10 mandatory distinctions defined separating dissipation from "
        "thermodynamics at every level",
        "7 discipline rules for thermodynamic claims",
        "8 forbidden failure modes preventing overclaiming",
        "Statistical foundation confirmed ABSENT and NOT ASSUMABLE",
        "T-B licensed to test: semigroup, non-invertibility, recoverability",
        "Thermodynamic program opens under strict prohibitions, not assumptions",
        "Every thermodynamic claim must be derived, not inferred from analogy",
    ]

    allowed = [
        "Dissipation and time asymmetry are present as native thermodynamic "
        "prerequisites (not thermodynamic results)",
        "10 mandatory distinctions established between analogous concepts",
        "8 forbidden failure modes prevent entropy/temperature/ensemble overclaiming",
        "Statistical/ensemble foundation confirmed absent and not assumable "
        "(Born rule absent from Q-II.F)",
        "Thermodynamic program charter defined with strict prohibitions",
        "T-B licensed: irreversibility, semigroup, non-invertibility, recoverability",
        "Appendix T opens under constraint, not assumption",
    ]

    forbidden = [
        "Dissipation implies entropy",
        "Time asymmetry implies entropy increase",
        "Relaxation timescale implies temperature",
        "Fixed-point attractor implies thermodynamic equilibrium",
        "Decoherence implies statistical mechanics",
        "Balance law implies conservation law",
        "Charter opening implies thermodynamic closure",
    ]

    diag: Dict[str, Any] = {
        "n_stages": N_STAGES, "n_distinctions": N_DISTINCTIONS,
        "n_rules": N_RULES, "n_ffms": N_FFMS,
        "n_nonclaims": N_TA_NONCLAIMS, "n_tb_licensed": len(tb.licensed_tests),
    }

    result = TACharter(
        True, dist, stg, rul, ffm, nc, tb,
        CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
        key, allowed, forbidden, diag,
    )
    _validate(result); return result


def _validate(r: TACharter) -> None:
    if len(r.distinctions) != N_DISTINCTIONS: raise ValueError("distinctions")
    if len(r.stage_sequence) != N_STAGES: raise ValueError("stages")
    for i, s in enumerate(r.stage_sequence):
        if s.stage_index != i: raise ValueError(f"stage index {s.stage_id}")
    if len(r.rules) != N_RULES: raise ValueError("rules")
    if len(r.ffms) != N_FFMS: raise ValueError("ffms")
    names = [f.name for f in r.ffms]
    for n in FFM_NAMES:
        if n not in names: raise ValueError(f"missing ffm {n}")
    if r.entry_nonclaims.n_nonclaims != N_TA_NONCLAIMS: raise ValueError("nonclaims")
    if not r.entry_nonclaims.all_registered: raise ValueError("registered")
    if r.charter_verdict not in ALLOWED_CHARTER_VERDICTS: raise ValueError("charter verdict")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")


def _self_test() -> bool:
    r = run_ta_thermodynamic_charter()
    assert r.valid
    assert r.charter_verdict == CHARTER_VERDICT
    assert r.authorization_verdict == AUTH_VERDICT
    assert r.overall_appendix_p == OVERALL_P
    assert len(r.distinctions) == N_DISTINCTIONS
    assert len(r.ffms) == N_FFMS
    return True


if __name__ == "__main__":
    _self_test(); print("T-A passed.")
