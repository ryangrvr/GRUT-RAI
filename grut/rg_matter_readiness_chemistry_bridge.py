"""
Appendix R-G --- Matter-Readiness to Chemistry Bridge
=====================================================
GRUT Matter Program --- Phase R-G  (Final Matter Stage)

Produces the final matter ledger: what GRUT matter has achieved, what
remains extension-level or blocked, what chemistry would require, and
whether a chemistry/life bridge can be opened honestly.

Final matter ledger summary:
  ACHIEVED (at extension level):
    - Bosonic localization (shell + topological + excitation forms)
    - Bosonic persistence (attractor + shell + topological charge)
    - Bosonic composite configurations (tensor product grammar)
    - Bosonic exchange structure (with open-system tau caveat)
    - Pre-atomic grammar (formal description language)
    - Fermionic route inventory (3 routes identified, none built)
    - Matter interpretation scaffold (requires explicit postulates)

  NOT ACHIEVED:
    - Stable bosonic objecthood (Derrick obstruction, Skyrme MBU)
    - Bosonic bound structure (no binding mechanism)
    - Fermionic matter (3-layer obstruction unchanged)
    - Probability-complete interpretation (Born rule absent)
    - Particle ontology (no Fock space, no identity, no dispersion)
    - Shell/exclusion structure (requires fermions)
    - Chemistry prerequisites (requires all of the above)

  MINIMUM CHEMISTRY BRIDGE CONDITIONS:
    1. Stable bosonic objects (Skyrme or equivalent stabilizer)
    2. Binding mechanism (attractive interaction + discrete spectrum)
    3. Fermionic extension (Hopf or spinor route built)
    4. Exclusion/statistics closure (antisymmetrization postulate)
    5. Probability postulate (Born rule MIP)
    6. Shell-structure readiness (from fermions + exclusion + binding)
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

N_MATTER_INVENTORY_ITEMS: int = 10
N_CHEMISTRY_PREREQS: int = 6
N_BOSONIC_LIMIT_CHECKS: int = 5
N_FERMIONIC_LIMIT_CHECKS: int = 4
N_PROBABILITY_CHECKS: int = 4
N_BRIDGE_CONDITIONS: int = 6
N_READINESS_DOMAINS: int = 6
N_APPENDIX_P_ENTRIES: int = 7
N_RG_NONCLAIMS: int = 8
N_ALLOWED_CLAIMS: int = 7
N_FORBIDDEN_CLAIMS: int = 7

RF_INHERITED: str = "authorized_to_proceed_to_RG"

RG_BOSONIC_VERDICT: str = "bosonic_matter_scaffold_established"
RG_FERMIONIC_VERDICT: str = "fermionic_matter_blocked_but_route_inventory_complete"
RG_CHEMISTRY_BOUNDARY_VERDICT: str = "chemistry_boundary_precisely_mapped"
RG_BRIDGE_CONDITION_VERDICT: str = "minimum_chemistry_bridge_conditions_identified"
RG_FINAL_MATTER_VERDICT: str = "matter_program_complete_as_pre_chemistry_ledger"
RG_OVERALL_APPENDIX_P_CLASS: str = "bounded_structural_result"

ALLOWED_BOSONIC_VERDICTS: frozenset = frozenset({
    "bosonic_matter_scaffold_established",
    "bosonic_matter_extension_ready_only",
    "bosonic_matter_still_precondition_only",
    "bosonic_matter_blocked",
})
ALLOWED_FERMIONIC_VERDICTS: frozenset = frozenset({
    "fermionic_matter_blocked_but_route_inventory_complete",
    "fermionic_matter_extension_route_only",
    "fermionic_matter_precondition_map_complete",
    "fermionic_matter_not_yet_actionable",
})
ALLOWED_CHEMISTRY_VERDICTS: frozenset = frozenset({
    "chemistry_requires_additional_stability_statistics_probability_closure",
    "chemistry_preconditions_mostly_blocked",
    "chemistry_boundary_precisely_mapped",
    "chemistry_bridge_not_yet_honest",
})
ALLOWED_BRIDGE_VERDICTS: frozenset = frozenset({
    "minimum_chemistry_bridge_conditions_identified",
    "bridge_conditions_structurally_plausible_but_unbuilt",
    "bridge_conditions_underdetermined",
    "no_coherent_bridge_conditions_yet",
})
ALLOWED_FINAL_VERDICTS: frozenset = frozenset({
    "matter_program_complete_as_pre_chemistry_ledger",
    "matter_program_sufficient_only_for_pre_chemistry_scaffolding",
    "matter_program_not_yet_sufficient_for_bridge",
    "matter_program_requires_further_refinement",
})
ALLOWED_APPENDIX_P_CLASSES: frozenset = frozenset({
    "native_canon", "effective_reduction", "bounded_structural_result",
    "working_canon_hypothesis", "motivated_but_unbuilt",
    "motivated_independent_postulation", "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})
ALLOWED_READINESS_LEVELS: frozenset = frozenset({
    "ready", "extension_ready", "precondition_only", "blocked",
})

RG_NONCLAIMS: List[str] = [
    "NOT_claiming_pre_atomic_grammar_therefore_chemistry__"
    "formal_composition_language_is_not_chemistry",
    "NOT_claiming_bosonic_exchange_therefore_chemistry__"
    "hard_core_boson_exchange_is_not_chemical_bonding",
    "NOT_claiming_composite_configurations_therefore_molecules__"
    "correlated_excitations_are_not_molecular_structure",
    "NOT_claiming_fermionic_route_inventory_therefore_exclusion_solved__"
    "identifying_routes_is_not_building_them",
    "NOT_claiming_diagnostic_weights_therefore_chemical_probabilities__"
    "Born_rule_absent_means_no_chemical_prediction",
    "NOT_claiming_extension_ready_matter_therefore_chemistry_ready_universe__"
    "extension_level_scaffolding_is_not_chemistry_closure",
    "NOT_claiming_matter_ledger_therefore_life_readiness__"
    "matter_is_one_prerequisite_for_life_not_life_itself",
    "NOT_claiming_bridge_conditions_identified_therefore_bridge_crossed__"
    "mapping_the_bridge_is_not_crossing_it",
]


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class RGMatterInventoryItem:
    item_id: str; item_name: str; status: str; source: str; notes: List[str]

@dataclass
class RGMatterInventory:
    items: List[RGMatterInventoryItem]; n_items: int
    n_achieved: int; n_extension: int; n_precondition: int; n_blocked: int
    notes: List[str]

@dataclass
class RGChemistryPrereq:
    prereq_id: str; prereq_name: str; status: str; notes: List[str]

@dataclass
class RGChemistryPrereqAudit:
    prereqs: List[RGChemistryPrereq]; n_prereqs: int
    n_met: int; n_unmet: int; notes: List[str]

@dataclass
class RGBosonicLimitCheck:
    check_id: str; check_name: str; result: str; notes: List[str]

@dataclass
class RGBosonicChemistryLimitAudit:
    checks: List[RGBosonicLimitCheck]; n_checks: int
    chemistry_from_bosons_alone: bool; notes: List[str]

@dataclass
class RGFermionicLimitCheck:
    check_id: str; check_name: str; result: str; notes: List[str]

@dataclass
class RGFermionicChemistryLimitAudit:
    checks: List[RGFermionicLimitCheck]; n_checks: int
    notes: List[str]

@dataclass
class RGProbabilityCheck:
    check_id: str; check_name: str; result: str; notes: List[str]

@dataclass
class RGProbabilityChemistryAudit:
    checks: List[RGProbabilityCheck]; n_checks: int
    born_required_for_chemistry: bool; notes: List[str]

@dataclass
class RGBridgeCondition:
    condition_id: str; condition_name: str; description: str
    currently_met: bool; notes: List[str]

@dataclass
class RGBridgeConditionAudit:
    conditions: List[RGBridgeCondition]; n_conditions: int
    n_met: int; n_unmet: int; bridge_condition_verdict: str; notes: List[str]

@dataclass
class RGReadinessEntry:
    domain: str; readiness_level: str; notes: str

@dataclass
class RGReadinessTable:
    entries: List[RGReadinessEntry]; n_entries: int

@dataclass
class RGAppendixPEntry:
    item_id: str; item_name: str; appendix_p_class: str
    allowed_claim: str; forbidden_claim: str; dependency: str

@dataclass
class RGAppendixPAudit:
    entries: List[RGAppendixPEntry]; n_entries: int
    overall_class: str; no_native_canon: bool; notes: List[str]

@dataclass
class RGNonclaimFirewall:
    nonclaims: List[str]; n_nonclaims: int; all_registered: bool

@dataclass
class RGMatterReadinessChemistryBridgeResult:
    valid: bool
    track_a_inventory: RGMatterInventory
    track_b_chemistry_prereqs: RGChemistryPrereqAudit
    track_c_bosonic_limit: RGBosonicChemistryLimitAudit
    track_d_fermionic_limit: RGFermionicChemistryLimitAudit
    track_e_probability: RGProbabilityChemistryAudit
    track_f_bridge: RGBridgeConditionAudit
    track_g_readiness: RGReadinessTable
    track_h_appendix_p: RGAppendixPAudit
    track_i_nonclaims: RGNonclaimFirewall
    bosonic_matter_verdict: str; fermionic_matter_verdict: str
    chemistry_boundary_verdict: str; bridge_condition_verdict: str
    final_matter_verdict: str
    rg_appendix_p_class: str
    allowed_claims: List[str]; forbidden_claims: List[str]
    exact_nonclaims: List[str]; diagnostics: Dict[str, Any]


# ---------------------------------------------------------------------------
# Track builders
# ---------------------------------------------------------------------------

def _build_track_a() -> RGMatterInventory:
    items = [
        RGMatterInventoryItem("MI1", "bosonic_localization", "extension_ready",
            "R-B", ["Shell + topological + excitation localization forms"]),
        RGMatterInventoryItem("MI2", "bosonic_persistence", "extension_ready",
            "R-B", ["Attractor + shell + topological charge persistence"]),
        RGMatterInventoryItem("MI3", "bosonic_objecthood", "precondition_only",
            "R-B", ["Structurally plausible but unbuilt; stability gap"]),
        RGMatterInventoryItem("MI4", "bosonic_stabilization", "precondition_only",
            "R-C", ["No native stabilizer; Skyrme MBU; metastability only"]),
        RGMatterInventoryItem("MI5", "bosonic_composite", "extension_ready",
            "R-D", ["Composite configurations extension-ready; no binding"]),
        RGMatterInventoryItem("MI6", "bosonic_binding", "blocked",
            "R-D", ["No true binding criterion found"]),
        RGMatterInventoryItem("MI7", "pre_atomic_grammar", "extension_ready",
            "R-D", ["Formal pre-atomic language available"]),
        RGMatterInventoryItem("MI8", "bosonic_exchange", "extension_ready",
            "R-F", ["Exchange structure demonstrated with open-system caveats"]),
        RGMatterInventoryItem("MI9", "fermionic_matter", "blocked",
            "R-E", ["3-layer obstruction unchanged; route inventory complete"]),
        RGMatterInventoryItem("MI10", "matter_interpretation", "precondition_only",
            "R-F", ["Scaffolded; requires explicit probability postulate"]),
    ]
    n_a = sum(1 for i in items if i.status == "achieved")
    n_e = sum(1 for i in items if i.status == "extension_ready")
    n_p = sum(1 for i in items if i.status == "precondition_only")
    n_b = sum(1 for i in items if i.status == "blocked")
    return RGMatterInventory(
        items=items, n_items=N_MATTER_INVENTORY_ITEMS,
        n_achieved=n_a, n_extension=n_e, n_precondition=n_p, n_blocked=n_b,
        notes=[f"{n_a} achieved, {n_e} extension-ready, {n_p} precondition, {n_b} blocked",
               "5 extension-ready (localization, persistence, composite, grammar, exchange)",
               "3 precondition (objecthood, stabilization, interpretation)",
               "2 blocked (binding, fermionic)"],
    )


def _build_track_b() -> RGChemistryPrereqAudit:
    prereqs = [
        RGChemistryPrereq("CP1", "stable_objecthood",
            "not_met", ["R-C: no native stabilizer; Skyrme MBU"]),
        RGChemistryPrereq("CP2", "stable_bound_structures",
            "not_met", ["R-D: no binding mechanism"]),
        RGChemistryPrereq("CP3", "fermionic_exclusion_statistics",
            "not_met", ["R-E: 3-layer obstruction unchanged"]),
        RGChemistryPrereq("CP4", "probability_complete_interpretation",
            "not_met", ["Q-II.F: Born rule absent"]),
        RGChemistryPrereq("CP5", "shell_orbital_organization",
            "not_met", ["Requires fermions + exclusion + binding: all absent"]),
        RGChemistryPrereq("CP6", "multi_constituent_stable_matter",
            "not_met", ["Requires stable objects + binding + statistics: all absent/blocked"]),
    ]
    n_met = sum(1 for p in prereqs if p.status == "met")
    n_unmet = sum(1 for p in prereqs if p.status == "not_met")
    return RGChemistryPrereqAudit(
        prereqs=prereqs, n_prereqs=N_CHEMISTRY_PREREQS,
        n_met=n_met, n_unmet=n_unmet,
        notes=["ALL 6 chemistry prerequisites NOT MET",
               "Chemistry requires: stability + binding + fermions + probability + "
               "shells + multi-constituent matter",
               "NONE of these are established in current GRUT matter program"],
    )


def _build_track_c() -> RGBosonicChemistryLimitAudit:
    checks = [
        RGBosonicLimitCheck("BL1", "bosonic_localization_available",
            "available", ["Extension-level localization forms"]),
        RGBosonicLimitCheck("BL2", "bosonic_composite_grammar",
            "available", ["Tensor product composition"]),
        RGBosonicLimitCheck("BL3", "bosonic_exchange_structure",
            "available", ["Hard-core boson exchange with tau caveat"]),
        RGBosonicLimitCheck("BL4", "no_shell_exclusion_from_bosons",
            "blocked", ["Shell filling requires Pauli exclusion = fermions"]),
        RGBosonicLimitCheck("BL5", "chemistry_from_bosons_alone",
            "blocked", ["Chemistry requires fermions for electron shells; "
                        "bosons alone cannot produce periodic-table chemistry"]),
    ]
    return RGBosonicChemistryLimitAudit(
        checks=checks, n_checks=N_BOSONIC_LIMIT_CHECKS,
        chemistry_from_bosons_alone=False,
        notes=["Bosonic matter provides: localization, composition, exchange",
               "Bosonic matter CANNOT provide: shell/exclusion chemistry",
               "Chemistry from bosons alone: BLOCKED"],
    )


def _build_track_d() -> RGFermionicChemistryLimitAudit:
    checks = [
        RGFermionicLimitCheck("FL1", "exclusion_absent",
            "blocked", ["No Pauli exclusion; no shell filling"]),
        RGFermionicLimitCheck("FL2", "shell_structure_absent",
            "blocked", ["Requires exclusion + binding"]),
        RGFermionicLimitCheck("FL3", "chemistry_statistics_absent",
            "blocked", ["No FD statistics; no spin-statistics theorem"]),
        RGFermionicLimitCheck("FL4", "fermionic_routes_inventory_only",
            "routes_documented", ["ER1 Hopf, ER2 spinor, ER3 Grassmann: none built"]),
    ]
    return RGFermionicChemistryLimitAudit(
        checks=checks, n_checks=N_FERMIONIC_LIMIT_CHECKS,
        notes=["3 blocked (exclusion, shells, statistics), 1 routes documented",
               "Fermionic matter needed for chemistry but entirely blocked"],
    )


def _build_track_e() -> RGProbabilityChemistryAudit:
    checks = [
        RGProbabilityCheck("PC1", "diagnostic_weights_only",
            "confirmed", ["Q-II.F boundary inherited"]),
        RGProbabilityCheck("PC2", "chemical_prediction_needs_born",
            "confirmed", ["Reaction rates, bond energies, spectra: all need Born rule"]),
        RGProbabilityCheck("PC3", "statistical_mechanics_needs_born",
            "confirmed", ["Partition functions, equilibrium: need probability"]),
        RGProbabilityCheck("PC4", "born_extension_identified",
            "confirmed", ["Q-II.F PX1: Born rule as MIP; route exists"]),
    ]
    return RGProbabilityChemistryAudit(
        checks=checks, n_checks=N_PROBABILITY_CHECKS,
        born_required_for_chemistry=True,
        notes=["All chemical predictions require Born rule",
               "Born rule identified as MIP extension route but not adopted"],
    )


def _build_track_f() -> RGBridgeConditionAudit:
    conditions = [
        RGBridgeCondition("BC1", "stable_bosonic_objects",
            "Skyrme L4 or equivalent stabilizer built.", False,
            ["Appendix N: MBU; R-C: no native stabilizer"]),
        RGBridgeCondition("BC2", "binding_mechanism",
            "Attractive interaction + discrete energy spectrum.", False,
            ["R-D: no binding criterion found"]),
        RGBridgeCondition("BC3", "fermionic_extension_built",
            "One of ER1/ER2/ER3 built and validated.", False,
            ["R-E: routes identified, none built"]),
        RGBridgeCondition("BC4", "exclusion_statistics_closure",
            "Antisymmetrization postulate + FD statistics.", False,
            ["R-E/R-F: blocked without fermionic extension"]),
        RGBridgeCondition("BC5", "probability_postulate",
            "Born rule adopted as MIP or derived.", False,
            ["Q-II.F: route identified; not adopted"]),
        RGBridgeCondition("BC6", "shell_structure_readiness",
            "Fermions + exclusion + binding = shell filling.", False,
            ["Requires BC1-BC5 as prerequisites"]),
    ]
    n_met = sum(1 for c in conditions if c.currently_met)
    n_unmet = sum(1 for c in conditions if not c.currently_met)
    return RGBridgeConditionAudit(
        conditions=conditions, n_conditions=N_BRIDGE_CONDITIONS,
        n_met=n_met, n_unmet=n_unmet,
        bridge_condition_verdict=RG_BRIDGE_CONDITION_VERDICT,
        notes=["ALL 6 bridge conditions NOT MET",
               "Bridge conditions are IDENTIFIED but not SATISFIED",
               "Each is a specific, actionable requirement",
               "Smallest path: BC5 (Born postulate) -> BC1 (Skyrme) -> BC2 (binding) "
               "-> BC3 (fermionic) -> BC4 (statistics) -> BC6 (shells)"],
    )


def _build_track_g() -> RGReadinessTable:
    entries = [
        RGReadinessEntry("bosonic_matter_ontology", "extension_ready",
            "Localization + persistence + exchange; no stability/binding"),
        RGReadinessEntry("bosonic_bound_matter", "precondition_only",
            "Composite grammar but no binding or stability"),
        RGReadinessEntry("fermionic_matter", "blocked",
            "3-layer obstruction; routes identified, none built"),
        RGReadinessEntry("pre_atomic_structure", "extension_ready",
            "Formal grammar; no physical pre-atomic structure"),
        RGReadinessEntry("chemistry_prerequisites", "blocked",
            "All 6 prerequisites unmet"),
        RGReadinessEntry("chemistry_bridge", "precondition_only",
            "Bridge conditions identified but not satisfied"),
    ]
    return RGReadinessTable(entries=entries, n_entries=N_READINESS_DOMAINS)


def _build_track_h() -> RGAppendixPAudit:
    entries = [
        RGAppendixPEntry("RG_matter_inventory", "Final matter inventory",
            "bounded_structural_result",
            "10-item matter inventory: 5 extension, 3 precondition, 2 blocked",
            "Matter inventory implies matter closure",
            "R-B through R-F"),
        RGAppendixPEntry("RG_chemistry_prereqs", "Chemistry prerequisites",
            "bounded_structural_result",
            "All 6 chemistry prerequisites documented as not met",
            "Some chemistry prerequisites met",
            "R-B through R-F; standard chemistry requirements"),
        RGAppendixPEntry("RG_bosonic_scaffold", "Bosonic matter scaffold",
            "motivated_but_unbuilt",
            "Bosonic scaffold: localization + exchange + composite grammar",
            "Bosonic scaffold implies bosonic matter closure",
            "R-B, R-D, R-F"),
        RGAppendixPEntry("RG_fermionic_block", "Fermionic block with routes",
            "bounded_structural_result",
            "Fermionic matter blocked; 3 extension routes inventoried",
            "Routes imply fermionic matter available",
            "R-E; Q0 3-layer obstruction"),
        RGAppendixPEntry("RG_bridge_conditions", "Bridge conditions",
            "bounded_structural_result",
            "6 minimum chemistry bridge conditions identified, none met",
            "Bridge conditions imply bridge crossable",
            "R-B through R-F synthesis"),
        RGAppendixPEntry("RG_probability_gap", "Probability gap for chemistry",
            "bounded_structural_result",
            "Born rule required for all chemical predictions",
            "Chemical predictions possible without Born rule",
            "Q-II.F"),
        RGAppendixPEntry("RG_overall", "R-G overall",
            "bounded_structural_result",
            "Matter program complete as pre-chemistry ledger",
            "Matter program or chemistry achieved",
            "All R tracks"),
    ]
    return RGAppendixPAudit(
        entries=entries, n_entries=N_APPENDIX_P_ENTRIES,
        overall_class=RG_OVERALL_APPENDIX_P_CLASS,
        no_native_canon=True,
        notes=["5 BSR (documented boundaries), 1 MBU (bosonic scaffold), 1 BSR (overall)"],
    )


def _build_track_i() -> RGNonclaimFirewall:
    return RGNonclaimFirewall(
        nonclaims=RG_NONCLAIMS, n_nonclaims=N_RG_NONCLAIMS,
        all_registered=True,
    )


# ---------------------------------------------------------------------------
# Master audit
# ---------------------------------------------------------------------------

def run_rg_matter_readiness_chemistry_bridge() -> RGMatterReadinessChemistryBridgeResult:
    ta = _build_track_a(); tb = _build_track_b(); tc = _build_track_c()
    td = _build_track_d(); te = _build_track_e(); tf = _build_track_f()
    tg = _build_track_g(); th = _build_track_h(); ti = _build_track_i()

    allowed_claims: List[str] = [
        "Final matter inventory: 10 items classified (0 achieved, "
        "5 extension-ready, 3 precondition, 2 blocked)",
        "Bosonic matter scaffold established: localization, persistence, "
        "composite grammar, exchange structure all at extension level",
        "Fermionic matter blocked with complete route inventory: 3-layer "
        "obstruction unchanged; Hopf, spinor, Grassmann routes identified",
        "All 6 chemistry prerequisites precisely documented as not met: "
        "stability, binding, fermions, probability, shells, multi-constituent",
        "6 minimum chemistry bridge conditions identified: each specific "
        "and actionable; none currently satisfied",
        "Chemistry from bosons alone is blocked: shell/exclusion chemistry "
        "requires fermionic statistics",
        "Matter program complete as pre-chemistry ledger: honest foundation "
        "for future chemistry/life work with no false claims",
    ]
    forbidden_claims: List[str] = [
        "Pre-atomic grammar implies chemistry",
        "Bosonic exchange implies chemistry",
        "Composite configurations imply molecules",
        "Fermionic route inventory implies exclusion solved",
        "Diagnostic weights imply chemical probabilities",
        "Extension-ready matter implies chemistry-ready universe",
        "Matter ledger implies life-readiness",
    ]
    diagnostics: Dict[str, Any] = {
        "n_matter_items": N_MATTER_INVENTORY_ITEMS,
        "n_achieved": ta.n_achieved,
        "n_extension": ta.n_extension,
        "n_precondition": ta.n_precondition,
        "n_blocked": ta.n_blocked,
        "n_chemistry_prereqs": N_CHEMISTRY_PREREQS,
        "n_prereqs_met": tb.n_met,
        "n_prereqs_unmet": tb.n_unmet,
        "chemistry_from_bosons_alone": tc.chemistry_from_bosons_alone,
        "born_required_for_chemistry": te.born_required_for_chemistry,
        "n_bridge_conditions": N_BRIDGE_CONDITIONS,
        "n_bridge_met": tf.n_met,
        "n_bridge_unmet": tf.n_unmet,
        "n_nonclaims": N_RG_NONCLAIMS,
    }

    result = RGMatterReadinessChemistryBridgeResult(
        valid=True,
        track_a_inventory=ta, track_b_chemistry_prereqs=tb,
        track_c_bosonic_limit=tc, track_d_fermionic_limit=td,
        track_e_probability=te, track_f_bridge=tf,
        track_g_readiness=tg, track_h_appendix_p=th,
        track_i_nonclaims=ti,
        bosonic_matter_verdict=RG_BOSONIC_VERDICT,
        fermionic_matter_verdict=RG_FERMIONIC_VERDICT,
        chemistry_boundary_verdict=RG_CHEMISTRY_BOUNDARY_VERDICT,
        bridge_condition_verdict=tf.bridge_condition_verdict,
        final_matter_verdict=RG_FINAL_MATTER_VERDICT,
        rg_appendix_p_class=RG_OVERALL_APPENDIX_P_CLASS,
        allowed_claims=allowed_claims, forbidden_claims=forbidden_claims,
        exact_nonclaims=RG_NONCLAIMS, diagnostics=diagnostics,
    )
    validate_rg_result(result)
    return result


def validate_rg_result(result: RGMatterReadinessChemistryBridgeResult) -> None:
    checks = [
        (result.bosonic_matter_verdict, ALLOWED_BOSONIC_VERDICTS, "Bosonic"),
        (result.fermionic_matter_verdict, ALLOWED_FERMIONIC_VERDICTS, "Fermionic"),
        (result.chemistry_boundary_verdict, ALLOWED_CHEMISTRY_VERDICTS, "Chemistry"),
        (result.bridge_condition_verdict, ALLOWED_BRIDGE_VERDICTS, "Bridge"),
        (result.final_matter_verdict, ALLOWED_FINAL_VERDICTS, "Final"),
    ]
    for v, a, l in checks:
        if v not in a:
            raise ValueError(f"{l} verdict '{v}' not in allowed")
    if result.rg_appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
        raise ValueError("Overall class invalid")
    for e in result.track_h_appendix_p.entries:
        if e.appendix_p_class not in ALLOWED_APPENDIX_P_CLASSES:
            raise ValueError(f"Entry '{e.item_id}' class invalid")
    if result.track_i_nonclaims.n_nonclaims != N_RG_NONCLAIMS:
        raise ValueError("Nonclaim count mismatch")
    if not result.track_i_nonclaims.all_registered:
        raise ValueError("Nonclaims not registered")
    if len(result.allowed_claims) != N_ALLOWED_CLAIMS:
        raise ValueError(f"Expected {N_ALLOWED_CLAIMS} allowed claims")
    if len(result.forbidden_claims) != N_FORBIDDEN_CLAIMS:
        raise ValueError(f"Expected {N_FORBIDDEN_CLAIMS} forbidden claims")
    if not result.track_h_appendix_p.no_native_canon:
        raise ValueError("no_native_canon must be True")
    if result.track_c_bosonic_limit.chemistry_from_bosons_alone:
        raise ValueError("chemistry_from_bosons_alone must be False")
    if not result.track_e_probability.born_required_for_chemistry:
        raise ValueError("born_required must be True")
    if result.track_b_chemistry_prereqs.n_met != 0:
        raise ValueError("n_prereqs_met must be 0")
    if result.track_f_bridge.n_met != 0:
        raise ValueError("n_bridge_met must be 0")
    for e in result.track_g_readiness.entries:
        if e.readiness_level not in ALLOWED_READINESS_LEVELS:
            raise ValueError(f"Readiness '{e.domain}' level invalid")


def _self_test() -> bool:
    r = run_rg_matter_readiness_chemistry_bridge()
    assert r.valid is True
    assert r.bosonic_matter_verdict == RG_BOSONIC_VERDICT
    assert r.fermionic_matter_verdict == RG_FERMIONIC_VERDICT
    assert r.chemistry_boundary_verdict == RG_CHEMISTRY_BOUNDARY_VERDICT
    assert r.bridge_condition_verdict == RG_BRIDGE_CONDITION_VERDICT
    assert r.final_matter_verdict == RG_FINAL_MATTER_VERDICT
    assert r.diagnostics["n_prereqs_met"] == 0
    assert r.diagnostics["n_bridge_met"] == 0
    assert r.diagnostics["chemistry_from_bosons_alone"] is False
    return True


if __name__ == "__main__":
    _self_test()
    print("R-G self-test passed.")
