"""
Appendix W0 --- Extension Entry Inventory
==========================================
GRUT Extension Program --- Phase W0  (Book III Opening)

Inventories the 10 missing structures from Book II, ranks them by
dependency, architectural priority, minimality, inflation risk, and
compatibility with the native foundation.

Book II closed with a persistent scalar dissipative substrate.
Book III adds structure. Book III may not reclassify extensions as native.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List
import math

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_EXTENSIONS: int = 10
N_W0_NONCLAIMS: int = 8
N_ALLOWED: int = 7; N_FORBIDDEN: int = 7

W0_VERDICT: str = "extension_inventory_complete_and_ranked"

W0_NONCLAIMS: List[str] = [
    "NOT_claiming_extension_inventory_therefore_extensions_built__"
    "inventory_ranks_what_is_missing_not_what_is_derived",
    "NOT_claiming_dependency_ranking_therefore_derivation_order__"
    "priority_is_architectural_not_physics_determined",
    "NOT_claiming_minimal_extension_therefore_easy__"
    "minimal_postulate_burden_is_not_zero_burden",
    "NOT_claiming_Book_III_opening_therefore_Book_II_revised__"
    "Book_II_native_canon_is_locked_and_immutable",
    "NOT_claiming_compatibility_therefore_integration__"
    "compatible_extension_is_not_unified_sector",
    "NOT_claiming_first_extension_therefore_most_important__"
    "architectural_priority_is_not_physical_importance",
    "NOT_claiming_ranked_list_therefore_program_complete__"
    "ranking_is_entry_condition_not_closure",
    "NOT_claiming_extension_possible_therefore_extension_correct__"
    "coherent_postulation_is_not_physical_truth",
]


@dataclass
class W0ExtensionItem:
    rank: int
    extension_name: str
    description: str
    dependencies: List[str]
    n_dependencies: int
    minimal_postulate: str
    inflation_risk: str  # "low", "medium", "high"
    book2_compatible: bool
    architectural_priority: str  # "foundational", "structural", "completion"
    notes: List[str]


@dataclass
class W0ExtensionEntryResult:
    valid: bool
    extensions: List[W0ExtensionItem]
    n_extensions: int
    recommended_first: str
    dependency_layers: List[List[str]]
    nonclaims: List[str]
    inventory_verdict: str
    key_findings: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    diagnostics: Dict[str, Any]


def _build_extensions() -> List[W0ExtensionItem]:
    return [
        W0ExtensionItem(1, "propagation_sector",
            "Spatial PDE: diffusion, wave, or advection terms added to constitutive ODE.",
            [], 0,
            "Add spatial derivative operator (nabla^2 or equivalent) to native ODE",
            "medium", True, "foundational",
            ["Unlocks: speed concept, spatial transport, characteristic structure",
             "Minimal: one spatial operator term",
             "Risk: smuggling in Lorentz covariance prematurely"]),
        W0ExtensionItem(2, "action_completion",
            "Variational principle: doubled-field or constrained action made explicit.",
            ["propagation_sector"], 1,
            "Adopt response-field S_eff[Phi,Phi_tilde] with spatial sector",
            "medium", True, "foundational",
            ["Requires propagation for nontrivial spatial action",
             "Response-field formalism already identified (U-C) but nonnative",
             "Risk: treating auxiliary action as fundamental"]),
        W0ExtensionItem(3, "born_probability",
            "Born rule: P(n) = Tr(rho P_n) as MIP postulate.",
            [], 0,
            "One axiom: P(n) = Tr(rho P_n)",
            "low", True, "foundational",
            ["Smallest postulate burden of all extensions",
             "Unlocks: statistical interpretation, Bell evaluation, measurement",
             "No new DOF required",
             "Already identified as PX1 in Q-II.F"]),
        W0ExtensionItem(4, "probe_coupling",
            "Matter-Phi coupling law with back-reaction.",
            ["propagation_sector"], 1,
            "Postulate coupling: F = -alpha grad(Phi) + back-reaction term",
            "high", True, "structural",
            ["Requires spatial gradients (propagation sector)",
             "Risk: smuggling in gravity or electromagnetism",
             "Unlocks: force-law testing, vacuum drag investigation"]),
        W0ExtensionItem(5, "geometry_dynamics",
            "Effective metric + dynamics: metric from Phi + propagation.",
            ["propagation_sector", "action_completion"], 2,
            "Derive effective metric from Phi field + spatial structure",
            "high", True, "structural",
            ["Requires propagation + action to define metric dynamics",
             "Risk: false GR recovery",
             "Highest inflation risk of all extensions"]),
        W0ExtensionItem(6, "gauge_structure",
            "Gauge fields, local symmetry, covariant derivatives.",
            ["propagation_sector", "action_completion"], 2,
            "Postulate gauge field A_mu with local symmetry + coupling",
            "high", True, "structural",
            ["Requires spatial sector + action for gauge field dynamics",
             "Risk: importing Standard Model by postulate",
             "Most alien to native scalar dissipative ontology"]),
        W0ExtensionItem(7, "fermionic_matter",
            "Spinorial structure via Hopf, spinor, or Grassmann route.",
            ["gauge_structure", "born_probability"], 2,
            "Postulate spinor field or Hopf term (ER1/ER2 from R-E)",
            "medium", True, "completion",
            ["Requires gauge-like structure for spinor coupling",
             "Requires probability for fermionic statistics",
             "3-layer obstruction (Q0) must be explicitly overcome"]),
        W0ExtensionItem(8, "chemistry_composite",
            "Stable objects + binding + statistics + shell structure.",
            ["fermionic_matter", "probe_coupling", "born_probability"], 3,
            "Multiple postulates: stability + binding + exclusion + probability",
            "high", True, "completion",
            ["Highest dependency count",
             "Requires nearly all other extensions as prerequisites",
             "Risk: declaring chemistry 'derived' from postulate chain"]),
        W0ExtensionItem(9, "cosmological_content",
            "Vacuum energy, dark energy, cosmological constant.",
            ["propagation_sector", "geometry_dynamics"], 2,
            "Postulate vacuum energy density or cosmological term",
            "high", True, "completion",
            ["Requires geometry dynamics for cosmological meaning",
             "Risk: importing Lambda without derivation"]),
        W0ExtensionItem(10, "quantum_thermal_vacuum",
            "Fluctuations, zero-point, bath structure, FDT.",
            ["born_probability", "action_completion"], 2,
            "Postulate noise term + bath spectral density + FDT",
            "medium", True, "completion",
            ["Requires probability for fluctuation interpretation",
             "Requires action for fluctuation-dissipation structure",
             "Langevin extension already identified conceptually"]),
    ]


def run_w0_extension_entry_inventory() -> W0ExtensionEntryResult:
    exts = _build_extensions()

    # Dependency layers
    layer_0 = [e.extension_name for e in exts if e.n_dependencies == 0]
    layer_1 = [e.extension_name for e in exts if e.n_dependencies == 1]
    layer_2 = [e.extension_name for e in exts if e.n_dependencies == 2]
    layer_3 = [e.extension_name for e in exts if e.n_dependencies == 3]
    layers = [layer_0, layer_1, layer_2, layer_3]

    key = [
        "10 MISSING STRUCTURES ranked by dependency depth and priority.",
        "LAYER 0 (no dependencies): propagation_sector, born_probability. "
        "These can be built first, independently.",
        "LAYER 1 (1 dependency): action_completion, probe_coupling. "
        "Require propagation sector.",
        "LAYER 2 (2 dependencies): geometry_dynamics, gauge_structure, "
        "fermionic_matter, cosmological_content, quantum_thermal_vacuum.",
        "LAYER 3 (3 dependencies): chemistry_composite. Highest burden.",
        "RECOMMENDED FIRST: born_probability (smallest postulate: one axiom, "
        "no new DOF, already identified as PX1) AND/OR propagation_sector "
        "(unlocks spatial transport, most structural value).",
        "Book II canon is LOCKED. Extensions are POSTULATES, not native facts.",
    ]

    allowed = [
        "10 missing structures inventoried and ranked by dependency",
        "4 dependency layers identified: 0-dependency through 3-dependency",
        "born_probability has smallest postulate burden (one axiom, no new DOF)",
        "propagation_sector unlocks most downstream extensions",
        "All extensions are compatible with Book II native canon",
        "Dependency structure is architectural, not physics-determined",
        "W-A authorized: extension charter next",
    ]

    forbidden = [
        "Extension inventory implies extensions built",
        "Dependency ranking implies derivation order",
        "Minimal postulate implies easy or automatic",
        "Book III opening implies Book II revised",
        "Compatibility implies integration",
        "First extension implies most important",
        "Extension possible implies extension correct",
    ]

    diagnostics: Dict[str, Any] = {
        "n_extensions": N_EXTENSIONS,
        "n_layer_0": len(layer_0),
        "n_layer_1": len(layer_1),
        "n_layer_2": len(layer_2),
        "n_layer_3": len(layer_3),
        "smallest_postulate": "born_probability",
        "most_structural": "propagation_sector",
        "highest_risk": "geometry_dynamics",
        "highest_dependency": "chemistry_composite",
        "all_book2_compatible": all(e.book2_compatible for e in exts),
        "n_nonclaims": N_W0_NONCLAIMS,
    }

    result = W0ExtensionEntryResult(
        True, exts, N_EXTENSIONS,
        "born_probability_or_propagation_sector",
        layers, W0_NONCLAIMS, W0_VERDICT,
        key, allowed, forbidden, diagnostics)
    _validate(result); return result


def _validate(r: W0ExtensionEntryResult) -> None:
    if len(r.extensions) != N_EXTENSIONS: raise ValueError("ext count")
    for i, e in enumerate(r.extensions):
        if e.rank != i + 1: raise ValueError(f"rank {e.rank}")
    if len(r.nonclaims) != N_W0_NONCLAIMS: raise ValueError("nc")
    if len(r.allowed_claims) != N_ALLOWED: raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN: raise ValueError("forbidden")
    if not r.diagnostics["all_book2_compatible"]: raise ValueError("compat")


def _self_test() -> bool:
    r = run_w0_extension_entry_inventory()
    assert r.valid and r.n_extensions == N_EXTENSIONS
    assert r.inventory_verdict == W0_VERDICT
    assert r.diagnostics["all_book2_compatible"] is True
    assert r.diagnostics["smallest_postulate"] == "born_probability"
    return True

if __name__ == "__main__":
    _self_test(); print("W0 passed.")
