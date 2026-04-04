"""
Appendix V0 --- Vacuum Ontology Entry Inventory
=================================================
GRUT Vacuum Ontology Program --- Phase V0

Inventories all vacuum/background/medium-relevant structures present in
GRUT after Appendices S, T, and U. Appendix V begins with a sparse scalar
dissipative substrate that supports constitutive descriptors but not geometry,
gauge structure, thermal completion, or unified field closure.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

ALLOWED_CLASSIFICATIONS = frozenset({
    "present_native", "present_but_limited", "constitutive_or_effective_only",
    "extension_only", "absent_unbuilt", "blocked_by_structure",
    "requires_new_postulates",
})

N_ITEMS: int = 25
N_V0_NONCLAIMS: int = 8

V0_INVENTORY: str = "inventory_complete_and_bounded"
V0_VACUUM: str = "scalar_dissipative_vacuum_present"
V0_SOURCE: str = "source_boundary_present_but_ontological_role_unresolved"

V0_NONCLAIMS: List[str] = [
    "NOT_claiming_scalar_substrate_therefore_aether__"
    "scalar_dissipative_vacuum_is_not_automatically_luminiferous_aether",
    "NOT_claiming_preferred_frame_therefore_absolute_space__"
    "tau_preferred_structure_is_constitutive_not_Newtonian_absolute",
    "NOT_claiming_dissipation_therefore_thermal_bath__"
    "irreversible_dynamics_is_not_bath_temperature",
    "NOT_claiming_metric_descriptor_therefore_geometry__"
    "constitutive_reparameterization_is_not_spacetime_ontology",
    "NOT_claiming_vacuum_persistence_therefore_substance__"
    "Phi_eq_0_may_be_trivial_not_substantive",
    "NOT_claiming_source_dependence_therefore_relational_ontology__"
    "X_boundary_must_be_audited_not_assumed_relational",
    "NOT_claiming_extension_overlays_therefore_vacuum_structure__"
    "O3_su2_etc_are_nonnative_layers_not_vacuum_character",
    "NOT_claiming_inventory_therefore_ontology_complete__"
    "inventory_documents_entry_not_conclusion",
]


@dataclass
class V0Item:
    item_id: str; item_name: str; classification: str
    what_established: str; what_absent: str; v_licensed: bool

@dataclass
class V0VacuumOntologyEntryResult:
    valid: bool; items: List[V0Item]; n_items: int
    n_native: int; n_limited: int; n_constitutive: int; n_extension: int
    n_absent: int; n_blocked: int; n_postulate: int
    nonclaims: List[str]
    inventory_verdict: str; vacuum_verdict: str; source_verdict: str
    diagnostics: Dict[str, Any]


def _build_items() -> List[V0Item]:
    return [
        V0Item("V1","scalar_vacuum_substrate","present_native",
            "Real scalar Phi with tau constitutive ODE","Ontological classification",True),
        V0Item("V2","tau_preferred_structure","present_native",
            "tau^2=3/2: preferred relaxation timescale","Whether tau is ontological or bookkeeping",True),
        V0Item("V3","preferred_rest_frame","present_native",
            "tau defines preferred frame (S-B)","Whether frame is ontological or constitutive",True),
        V0Item("V4","dissipation_arrow","present_native",
            "Irreversible dissipative temporal orientation","Whether arrow is fundamental or emergent",True),
        V0Item("V5","local_relaxation","present_native",
            "Pointwise relaxation toward source/attractor","Whether this constitutes vacuum dynamics",True),
        V0Item("V6","source_boundary_X","present_native",
            "X is external/constitutive input (U-B)","Ontological role of X; what IS X",True),
        V0Item("V7","vacuum_at_X_eq_0","present_but_limited",
            "When X=0: Phi->0 by relaxation","Whether Phi=0 is vacuum, ground state, or trivial",True),
        V0Item("V8","ground_state_candidate","present_but_limited",
            "Phi=0 (X=0) or Phi=X_ss (constant X) as rest state","Whether rest state is ground state",True),
        V0Item("V9","background_status","present_but_limited",
            "Phi provides a background on which extensions layer","Whether background is ontological",True),
        V0Item("V10","medium_substrate_status","present_but_limited",
            "Scalar field acts as medium for constitutive response","Whether medium is substance or formalism",True),
        V0Item("V11","relational_status","absent_unbuilt",
            "Not audited; X=0 limit not yet ontologically classified","Relational interpretation",True),
        V0Item("V12","geometry_based_vacuum","absent_unbuilt",
            "No native geometry dynamics (U-E/U-H)","Everything: metric vacuum, geometric ontology",True),
        V0Item("V13","quantum_vacuum_fluctuation","blocked_by_structure",
            "Born/probability absent; no quantum vacuum","Quantum fluctuation vacuum",False),
        V0Item("V14","thermal_bath_vacuum","absent_unbuilt",
            "No temperature, no bath (T-D/T-E)","Thermal vacuum interpretation",True),
        V0Item("V15","aether_comparison","present_but_limited",
            "Scalar medium + preferred frame: structural resemblance to aether",
            "Whether resemblance = identity",True),
        V0Item("V16","constitutive_metric_descriptor","constitutive_or_effective_only",
            "ds^2_eff conditional on Phi (U-E)","Geometry dynamics",True),
        V0Item("V17","constitutive_force_response","constitutive_or_effective_only",
            "Gradient/medium force conditional on probe postulate (U-F)","Derived force law",True),
        V0Item("V18","matter_dependence_spatial","constitutive_or_effective_only",
            "Spatial Phi structure from X (source)","Autonomous spatial structure",True),
        V0Item("V19","observer_measurement_distortion","constitutive_or_effective_only",
            "Phi-sensitive apparatus gives distorted intervals (U-E)","Real spacetime warping",True),
        V0Item("V20","substance_density_stress","absent_unbuilt",
            "No density, stress, or substance language licensed","Everything",True),
        V0Item("V21","memory_ontological_role","present_but_limited",
            "Temporal retardation modifies operator (U-B)","Whether memory is ontological feature of vacuum",True),
        V0Item("V22","empty_space_meaning","present_but_limited",
            "X=0 -> Phi->0: candidate for empty space","Whether Phi=0 = empty space or degenerate vacuum",True),
        V0Item("V23","vacuum_autonomy","present_but_limited",
            "Free relaxation is autonomous (X=0); driven case needs X","Whether vacuum is source-independent",True),
        V0Item("V24","extension_compatibility","present_native",
            "Extensions layer on native vacuum without contradiction","Whether overlays change vacuum ontology",True),
        V0Item("V25","new_ontology_postulates","requires_new_postulates",
            "Substance, bath, geometry, quantum vacuum: all need postulates","Ontological completion",True),
    ]


def run_v0_vacuum_ontology_entry_inventory() -> V0VacuumOntologyEntryResult:
    items = _build_items()
    c = {cl: sum(1 for i in items if i.classification == cl) for cl in ALLOWED_CLASSIFICATIONS}
    diag: Dict[str, Any] = {"n_items": len(items),
        **{f"n_{k}": v for k, v in c.items()},
        "n_v_licensed": sum(1 for i in items if i.v_licensed)}
    result = V0VacuumOntologyEntryResult(
        True, items, len(items),
        c.get("present_native",0), c.get("present_but_limited",0),
        c.get("constitutive_or_effective_only",0), c.get("extension_only",0),
        c.get("absent_unbuilt",0), c.get("blocked_by_structure",0),
        c.get("requires_new_postulates",0),
        V0_NONCLAIMS, V0_INVENTORY, V0_VACUUM, V0_SOURCE, diag)
    _validate(result); return result


def _validate(r: V0VacuumOntologyEntryResult) -> None:
    if len(r.items) != N_ITEMS: raise ValueError(f"Expected {N_ITEMS}")
    for i in r.items:
        if i.classification not in ALLOWED_CLASSIFICATIONS: raise ValueError(f"{i.item_id}")
    if len(r.nonclaims) != N_V0_NONCLAIMS: raise ValueError("nc")
    total = r.n_native+r.n_limited+r.n_constitutive+r.n_extension+r.n_absent+r.n_blocked+r.n_postulate
    if total != r.n_items: raise ValueError(f"counts {total}!={r.n_items}")


def _self_test() -> bool:
    r = run_v0_vacuum_ontology_entry_inventory()
    assert r.valid and r.n_items == N_ITEMS
    assert r.inventory_verdict == V0_INVENTORY
    assert r.vacuum_verdict == V0_VACUUM
    assert r.source_verdict == V0_SOURCE
    assert r.n_native >= 6
    return True

if __name__ == "__main__":
    _self_test(); print("V0 passed.")
