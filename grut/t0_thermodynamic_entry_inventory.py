"""
Appendix T0 --- Thermodynamic Entry Inventory
===============================================
GRUT Thermodynamic Program --- Phase T0

Inventories all thermodynamic-relevant structures present in GRUT after
Appendix S, classifying each strictly. Does not construct thermodynamic
theory; identifies what is present, absent, and what later stages may test.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

ALLOWED_CLASSIFICATIONS = frozenset({
    "present_native", "present_but_limited", "absent_unbuilt",
    "blocked_by_structure", "extension_only", "requires_new_postulates",
})

N_INVENTORY_ITEMS: int = 20
N_T0_NONCLAIMS: int = 8

# Verdicts
T0_INVENTORY_VERDICT: str = "inventory_complete_and_bounded"
T0_NATIVE_CONTENT: str = "dissipation_and_time_asymmetry_present"
T0_STATISTICAL_FOUNDATION: str = "absent_and_not_assumable"

T0_NONCLAIMS: List[str] = [
    "NOT_claiming_dissipation_therefore_entropy__"
    "dissipation_is_energy_loss_not_entropy_production_without_derivation",
    "NOT_claiming_time_asymmetry_therefore_irreversibility__"
    "directional_evolution_is_not_proven_non_invertibility",
    "NOT_claiming_relaxation_therefore_temperature__"
    "tau_is_timescale_not_temperature_without_FDT_or_bath",
    "NOT_claiming_attractor_therefore_equilibrium__"
    "fixed_point_of_ODE_is_not_thermodynamic_equilibrium",
    "NOT_claiming_balance_law_therefore_conservation__"
    "open_system_balance_is_not_closed_system_conservation",
    "NOT_claiming_decoherence_therefore_statistical_mechanics__"
    "pointer_basis_selection_is_not_ensemble_theory",
    "NOT_claiming_energy_bookkeeping_therefore_free_energy__"
    "tracking_energy_flow_is_not_thermodynamic_potential",
    "NOT_claiming_open_system_therefore_bath_temperature__"
    "environment_interpretation_requires_new_postulate",
]


@dataclass
class T0InventoryItem:
    item_id: str; item_name: str; classification: str
    what_established: str; what_absent: str; t_licensed: bool
    notes: List[str]

@dataclass
class T0ThermodynamicEntryResult:
    valid: bool
    items: List[T0InventoryItem]
    n_items: int
    n_present_native: int; n_present_limited: int
    n_absent: int; n_blocked: int; n_extension: int; n_new_postulate: int
    nonclaims: List[str]
    inventory_verdict: str; native_content_verdict: str
    statistical_foundation_verdict: str
    diagnostics: Dict[str, Any]


def _build_inventory() -> List[T0InventoryItem]:
    return [
        T0InventoryItem("T1","dissipation","present_native",
            "tau dPhi/dt + Phi = X: energy leaves system through constitutive channel",
            "Quantitative dissipation rate as thermodynamic quantity",True,[]),
        T0InventoryItem("T2","arrow_of_time","present_native",
            "First-order ODE + dissipation define temporal direction",
            "Proof of non-invertibility; merely directional not proven irreversible",True,[]),
        T0InventoryItem("T3","irreversibility_candidate","present_but_limited",
            "Dissipative evolution is directional; candidate for irreversibility",
            "Formal proof that evolution is non-invertible / semigroup",True,
            ["Directionality established; formal irreversibility not yet proven"]),
        T0InventoryItem("T4","relaxation_timescale_tau","present_native",
            "tau^2=3/2: canonical relaxation timescale",
            "Identification of tau with temperature or thermal timescale",True,[]),
        T0InventoryItem("T5","balance_law_candidate","present_but_limited",
            "tau dPhi/dt + Phi = X is a balance/constitutive law",
            "Closed-form energy conservation; thermodynamic first law",True,[]),
        T0InventoryItem("T6","energy_like_bookkeeping","present_but_limited",
            "Energy flows through constitutive channel; trackable",
            "Conserved energy; thermodynamic internal energy U",True,
            ["Energy is DISSIPATED not conserved; bookkeeping not conservation"]),
        T0InventoryItem("T7","entropy_like_quantity","absent_unbuilt",
            "No entropy function S has been defined or derived",
            "Everything: no S, no dS, no dS/dt >= 0",True,
            ["T-B/C may test whether a monotone exists; not yet established"]),
        T0InventoryItem("T8","entropy_production_rate","absent_unbuilt",
            "No sigma = dS/dt has been established",
            "Everything: no production rate, no positivity proof",True,[]),
        T0InventoryItem("T9","temperature_like_quantity","absent_unbuilt",
            "No T has been defined or derived from tau",
            "Everything: no T, no 1/T = dS/dE, no FDT",True,
            ["tau is a timescale; temperature requires additional structure"]),
        T0InventoryItem("T10","equilibrium_concept","absent_unbuilt",
            "No thermodynamic equilibrium defined",
            "Equilibrium state, equilibrium conditions, zeroth law",True,
            ["Attractor/steady-state exists but is not thermodynamic equilibrium"]),
        T0InventoryItem("T11","steady_state_attractor","present_but_limited",
            "Constitutive ODE has fixed point Phi = X (for constant X)",
            "Thermodynamic equilibrium; detailed balance; maximum entropy state",True,
            ["Fixed point is mathematical attractor, not thermodynamic equilibrium"]),
        T0InventoryItem("T12","statistical_ensemble","absent_unbuilt",
            "No ensemble (micro/canonical/grand) defined",
            "Everything: no phase space, no measure, no partition function",False,
            ["Requires probability foundation (absent) and microscopic states"]),
        T0InventoryItem("T13","probability_foundation","blocked_by_structure",
            "Born rule absent (Q-II.F); diagnostic weights only",
            "Probability measure, frequency interpretation, ensemble weights",False,
            ["Blocked: cannot assume statistical mechanics without probability"]),
        T0InventoryItem("T14","hamiltonian_unitary_backbone","absent_unbuilt",
            "Native system is dissipative, not Hamiltonian",
            "Hamiltonian, Liouville theorem, symplectic structure",False,
            ["H_hop is extension-level; native dynamics are first-order dissipative"]),
        T0InventoryItem("T15","free_energy_potential","absent_unbuilt",
            "No F, G, or other thermodynamic potential defined",
            "Everything: no Legendre structure, no state functions",True,
            ["Requires energy + entropy + temperature: none established"]),
        T0InventoryItem("T16","bath_environment","requires_new_postulates",
            "No bath or environment explicitly defined",
            "Bath temperature, spectral density, system-bath coupling",True,
            ["Constitutive dissipation IMPLIES environment but does not SPECIFY it"]),
        T0InventoryItem("T17","nonequilibrium_status","present_native",
            "GRUT is natively a nonequilibrium open system",
            "Approach to equilibrium; NESS characterization",True,
            ["This IS the native character; not a deficiency"]),
        T0InventoryItem("T18","coarse_graining","absent_unbuilt",
            "No coarse-graining procedure defined",
            "Renormalization group, effective field theory, decimation",True,[]),
        T0InventoryItem("T19","reversibility_restoration","absent_unbuilt",
            "No mechanism to restore reversibility",
            "Microreversibility, detailed balance, Onsager reciprocal",True,
            ["Native T-breaking is structural; restoration would need new axiom"]),
        T0InventoryItem("T20","macroscopic_state_variables","present_but_limited",
            "Phi, <Phi_hat>, tau, decoherence rates: candidate state variables",
            "Complete thermodynamic state space; equations of state",True,
            ["Variables exist; their thermodynamic role is not yet assigned"]),
    ]


def run_t0_thermodynamic_entry_inventory() -> T0ThermodynamicEntryResult:
    items = _build_inventory()
    counts = {c: sum(1 for i in items if i.classification == c)
              for c in ALLOWED_CLASSIFICATIONS}
    diag: Dict[str, Any] = {
        "n_items": len(items), **{f"n_{k}": v for k, v in counts.items()},
        "n_t_licensed": sum(1 for i in items if i.t_licensed),
    }
    result = T0ThermodynamicEntryResult(
        valid=True, items=items, n_items=len(items),
        n_present_native=counts.get("present_native", 0),
        n_present_limited=counts.get("present_but_limited", 0),
        n_absent=counts.get("absent_unbuilt", 0),
        n_blocked=counts.get("blocked_by_structure", 0),
        n_extension=counts.get("extension_only", 0),
        n_new_postulate=counts.get("requires_new_postulates", 0),
        nonclaims=T0_NONCLAIMS,
        inventory_verdict=T0_INVENTORY_VERDICT,
        native_content_verdict=T0_NATIVE_CONTENT,
        statistical_foundation_verdict=T0_STATISTICAL_FOUNDATION,
        diagnostics=diag,
    )
    _validate(result); return result


def _validate(r: T0ThermodynamicEntryResult) -> None:
    if len(r.items) != N_INVENTORY_ITEMS:
        raise ValueError(f"Expected {N_INVENTORY_ITEMS} items")
    for i in r.items:
        if i.classification not in ALLOWED_CLASSIFICATIONS:
            raise ValueError(f"{i.item_id}: '{i.classification}' invalid")
    if len(r.nonclaims) != N_T0_NONCLAIMS:
        raise ValueError("nonclaims")
    total = (r.n_present_native + r.n_present_limited + r.n_absent +
             r.n_blocked + r.n_extension + r.n_new_postulate)
    if total != r.n_items:
        raise ValueError(f"counts {total} != {r.n_items}")


def _self_test() -> bool:
    r = run_t0_thermodynamic_entry_inventory()
    assert r.valid and r.n_items == N_INVENTORY_ITEMS
    assert r.inventory_verdict == T0_INVENTORY_VERDICT
    assert r.native_content_verdict == T0_NATIVE_CONTENT
    assert r.statistical_foundation_verdict == T0_STATISTICAL_FOUNDATION
    assert r.n_present_native >= 3  # dissipation, arrow, tau, nonequilibrium
    assert r.n_absent >= 7  # entropy, production, temperature, etc.
    return True


if __name__ == "__main__":
    _self_test(); print("T0 passed.")
