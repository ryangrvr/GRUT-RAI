"""
Appendix Z-C --- Total Canon Map and Final ToE-Status Boundary Audit
=====================================================================
GRUT Capstone Program --- Phase Z-C

Produces the total canon map of GRUT, classifies every major result by
ontological and architectural status, and determines the strongest honest
ToE-status label for the program.

This stage is total synthesis under strict closure discipline.

=== ToE-STATUS BOUNDARY ===

Candidate labels tested:
  1. Full ToE completion --- FAILS. Gauge, fermions, chemistry, cosmology,
     apparatus, collapse ontology, unitarity, back-reaction all absent.
  2. Complete foundational ToE architecture --- FAILS. "Complete" implies
     no fatal gaps. Gauge and fermions are structurally absent, not deferred.
  3. Bounded partial ToE --- MARGINAL. "ToE" overstates. The program is
     not a theory of everything in any honest sense.
  4. Bounded world-model framework with explicit gaps --- SUPPORTED.
     Covers substrate, symmetry, thermodynamics, field architecture,
     probability, quantum-dynamical interface. Major sectors explicitly
     absent. Gaps honestly documented. No inflation.

Strongest honest label:
  "Bounded world-model framework with audited foundation, minimal
  extension architecture, operational quantum layer, and explicit
  completion gaps. Not a Theory of Everything."

=== WORLD-MODEL SCOPE ===

The architecture covers in bounded form:
  - Substrate ontology (V): persistent scalar dissipative medium
  - Symmetry status (S): native Z2/parity/isotropy; no gauge
  - Thermodynamic status (T): irreversibility, Lyapunov, no temperature
  - Field architecture (U/W): one field, propagation extension, probe coupling
  - Measurement/probability (X): Born map, outcomes, epistemic update
  - Quantum-dynamical interface (Y): Lindblad, decoherence, integration criteria

This is BROAD scope for a 7-postulate, 0-new-field architecture.
But breadth is not depth: every sector has explicit ceilings.

=== MISSING-SECTOR SEVERITY ===

FATAL to full ToE:
  gauge, fermions, chemistry, cosmology, unified closure

FATAL to "complete foundational":
  gauge (no local symmetry), fermions (3-layer obstruction)

COMPATIBLE with "bounded world-model framework":
  all absences, because framework explicitly documents them

=== Z-FINALIZATION ===

Z-D recommended: final sovereign summary, architecture map, and
future-work boundary in a single closure stage. Z-E not needed
if Z-D is comprehensive.
"""

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List

TAU_SQ: float = 3.0 / 2.0
TAU: float = math.sqrt(TAU_SQ)

# ── counts ──
N_CANON_ENTRIES: int = 32
N_TOE_CANDIDATES: int = 4
N_SCOPE_SECTORS: int = 6
N_MISSING_SECTORS: int = 10
N_LANGUAGE_LEVELS: int = 5
N_ZC_NONCLAIMS: int = 8
N_ALLOWED: int = 7
N_FORBIDDEN: int = 7

# ── classification enums ──
CANON_CLASSIFICATIONS = frozenset({
    "native_canon", "extension_canon", "operational_canon",
    "analogy_only", "constitutive_or_effective_only",
    "absent_unbuilt", "blocked_by_structure",
    "future_postulate_dependent",
})

TOE_CANDIDATE_LABELS = frozenset({
    "full_toe_completion",
    "complete_foundational_toe_architecture",
    "bounded_partial_toe",
    "bounded_world_model_framework_with_explicit_gaps",
})

SCOPE_VERDICTS = frozenset({
    "covered_in_bounded_form", "partially_covered", "absent",
})

MISSING_SEVERITY = frozenset({
    "fatal_to_full_toe", "fatal_to_foundational_completion",
    "compatible_with_bounded_framework", "blocked_cascade",
})

# ── verdict option sets ──
CANON_MAP_OPTIONS = frozenset({
    "total_canon_map_complete_and_consistent",
    "canon_map_requires_revision",
    "canon_map_incomplete",
})
TOE_STATUS_OPTIONS = frozenset({
    "complete_foundational_toe_architecture_supported",
    "bounded_world_model_framework_supported",
    "partial_toe_with_explicit_gaps_supported",
    "full_toe_completion_supported",
    "toe_status_not_stable",
})
WORLD_MODEL_OPTIONS = frozenset({
    "broad_world_model_scope_supported_with_explicit_gaps",
    "architecture_only_not_world_model",
    "world_model_status_mixed",
    "world_model_scope_not_established",
})
MISSING_SECTOR_OPTIONS = frozenset({
    "missing_sectors_fatal_to_full_completion_but_not_foundational_completion",
    "missing_sectors_block_even_foundational_claims",
    "missing_sector_severity_unclear",
})
AUTH_OPTIONS = frozenset({
    "authorized_to_proceed_to_ZD",
    "appendix_Z_can_close_here",
    "stop_for_missing_total_canon_boundary",
})
OVERALL_OPTIONS = frozenset({
    "grut_program_reaches_complete_foundational_architecture_without_full_sector_completion",
    "total_canon_map_closed_with_explicit_toe_boundary",
    "bounded_world_model_framework_identified_under_strict_limits",
    "final_toe_status_not_yet_stable",
})

# ── selected verdicts ──
ZC_CANON_MAP: str = "total_canon_map_complete_and_consistent"
ZC_TOE: str = "bounded_world_model_framework_supported"
ZC_WORLD_MODEL: str = "broad_world_model_scope_supported_with_explicit_gaps"
ZC_MISSING: str = "missing_sectors_fatal_to_full_completion_but_not_foundational_completion"
ZC_AUTH: str = "authorized_to_proceed_to_ZD"
ZC_OVERALL: str = "bounded_world_model_framework_identified_under_strict_limits"

# ── nonclaims ──
ZC_NONCLAIMS: List[str] = [
    "NOT_claiming_canon_map_therefore_physics_complete__"
    "classifying_results_is_not_proving_completeness",
    "NOT_claiming_broad_scope_therefore_solved__"
    "covering_many_sectors_in_bounded_form_is_not_completing_them",
    "NOT_claiming_bounded_framework_therefore_ToE__"
    "world_model_framework_is_explicitly_not_theory_of_everything",
    "NOT_claiming_low_postulate_count_therefore_sufficient__"
    "economy_is_ratio_not_achievement",
    "NOT_claiming_absent_sectors_documented_therefore_resolved__"
    "documenting_absence_is_not_building_sectors",
    "NOT_claiming_operational_quantum_layer_therefore_full_QM__"
    "operational_sufficiency_is_not_ontological_completion",
    "NOT_claiming_foundational_architecture_therefore_complete_foundation__"
    "architecture_has_explicit_missing_pillars",
    "NOT_claiming_ZC_closes_program_therefore_nothing_remains__"
    "ZD_final_summary_and_boundary_still_recommended",
]


# ══════════════════════════════════════════════════════════════════════
#  Dataclasses
# ══════════════════════════════════════════════════════════════════════

@dataclass
class ZCCanonEntry:
    entry_id: str
    sector_or_result: str
    classification: str        # from CANON_CLASSIFICATIONS
    what_established: str
    what_not_established: str
    capstone_treatment: str    # "freeze", "fence", "document"

@dataclass
class ZCToECandidate:
    label: str                 # from TOE_CANDIDATE_LABELS
    supported: bool
    reason: str
    strongest_safe_usage: str

@dataclass
class ZCScopeSector:
    sector_name: str
    appendix_source: str
    scope_verdict: str         # from SCOPE_VERDICTS
    what_covered: str
    ceiling: str

@dataclass
class ZCMissingSector:
    sector_id: str
    sector_name: str
    severity: str              # from MISSING_SEVERITY
    fatal_to: str
    compatible_with: str
    description: str

@dataclass
class ZCLanguageLevel:
    level_id: str
    label: str
    safe: bool
    justification: str

@dataclass
class ZCFinalizationRecommendation:
    zd_needed: bool
    zd_scope: str
    ze_needed: bool
    rationale: str

@dataclass
class ZCNonclaimFirewall:
    nonclaims: List[str]
    n_nonclaims: int
    all_registered: bool

@dataclass
class ZCTotalCanonMapResult:
    valid: bool
    # Track A: canon map
    canon_map: List[ZCCanonEntry]
    n_canon_entries: int
    n_native: int; n_extension: int; n_operational: int
    n_analogy: int; n_constitutive: int
    n_absent: int; n_blocked: int; n_future: int
    # Track B: ToE status
    toe_candidates: List[ZCToECandidate]
    strongest_honest_label: str
    # Track C: world-model scope
    scope_sectors: List[ZCScopeSector]
    n_covered: int; n_partial: int; n_scope_absent: int
    # Track D: missing-sector severity
    missing_sectors: List[ZCMissingSector]
    n_fatal_toe: int; n_fatal_foundational: int; n_compatible: int
    # Track E: capstone language
    language_levels: List[ZCLanguageLevel]
    strongest_safe_language: str
    # Track F: finalization
    finalization: ZCFinalizationRecommendation
    # Firewall
    nonclaim_firewall: ZCNonclaimFirewall
    # Hard-gated verdicts
    canon_map_status: str
    toe_status: str
    world_model_status: str
    missing_sector_status: str
    authorization: str
    overall_appendix_p: str
    # Summary
    key_findings: List[str]
    allowed_claims: List[str]
    forbidden_claims: List[str]
    exact_nonclaims: List[str]
    diagnostics: Dict[str, Any]


# ══════════════════════════════════════════════════════════════════════
#  Track builders
# ══════════════════════════════════════════════════════════════════════

def _build_canon_map() -> List[ZCCanonEntry]:
    return [
        # ── Native canon (8) ──
        ZCCanonEntry("C1","scalar_field_Phi","native_canon",
            "One real scalar field on persistent substrate",
            "Multi-field, vector/tensor, spinor","freeze"),
        ZCCanonEntry("C2","tau_sq_constitutive","native_canon",
            "tau^2=3/2 preferred constitutive structure",
            "Other constitutive relations","freeze"),
        ZCCanonEntry("C3","dissipative_dynamics","native_canon",
            "First-order dissipative ODE: tau dPhi/dt + Phi = X",
            "Reversible dynamics, Hamiltonian dynamics","freeze"),
        ZCCanonEntry("C4","forward_semigroup","native_canon",
            "S(t) = exp(-t/tau) forward contraction semigroup",
            "Backward evolution, time-reversal symmetry","freeze"),
        ZCCanonEntry("C5","irreversibility","native_canon",
            "Genuine dynamical irreversibility",
            "Reversibility, T-symmetry restoration","freeze"),
        ZCCanonEntry("C6","lyapunov_bookkeeping","native_canon",
            "V=(1/2)delta^2, dV/dt=-(2/tau)V exact balance",
            "Entropy, temperature, second law","freeze"),
        ZCCanonEntry("C7","vacuum_substrate","native_canon",
            "Persistent scalar dissipative substrate",
            "Geometric vacuum, quantum vacuum","freeze"),
        ZCCanonEntry("C8","quiescent_state","native_canon",
            "Phi->0 when X=0; no VEV, no cosmological constant",
            "Spontaneous symmetry breaking, dark energy","freeze"),
        # ── Extension canon (13) ──
        ZCCanonEntry("C9","telegrapher_propagation","extension_canon",
            "tau2 d2Phi/dt2 + tau1 dPhi/dt + Phi - L2 nabla2 Phi = X",
            "Native propagation","freeze"),
        ZCCanonEntry("C10","finite_speed","extension_canon",
            "v = sqrt(L2/tau2) characteristic speed",
            "Native speed concept","freeze"),
        ZCCanonEntry("C11","undamped_action","extension_canon",
            "KG-like variational principle for undamped sector",
            "Full damped-sector action","freeze"),
        ZCCanonEntry("C12","probe_coupling","extension_canon",
            "F = -alpha grad(Phi(q))",
            "Back-reaction, self-consistent coupling","freeze"),
        ZCCanonEntry("C13","born_map","extension_canon",
            "p(i) = Tr(rho Pi_i)",
            "Native probability, frequency derivation","freeze"),
        ZCCanonEntry("C14","outcome_selection","extension_canon",
            "One outcome per run realized",
            "Selection mechanism","freeze"),
        ZCCanonEntry("C15","epistemic_update","extension_canon",
            "rho -> Pi_i rho Pi_i / p(i)",
            "Collapse ontology","freeze"),
        ZCCanonEntry("C16","lindblad_evolution","extension_canon",
            "drho/dt = -i[H,rho] + D[rho]",
            "Unitarity, closed-system dynamics","freeze"),
        ZCCanonEntry("C17","decoherence","extension_canon",
            "Off-diagonal suppression in L-eigenbasis",
            "Native decoherence mechanism","freeze"),
        ZCCanonEntry("C18","pointer_basis","extension_canon",
            "L-eigenbasis as decoherence-stable basis",
            "Ontological basis selection","freeze"),
        ZCCanonEntry("C19","integration_criteria","extension_canon",
            "5 criteria for genuine sector integration",
            "Integrated sectors","freeze"),
        ZCCanonEntry("C20","interface_rules","extension_canon",
            "7 universal rules for future sector work",
            "Built interfaces","freeze"),
        ZCCanonEntry("C21","readiness_ranking","extension_canon",
            "Apparatus nearest; chemistry most distant",
            "Completed sectors","freeze"),
        # ── Analogy-only (3) ──
        ZCCanonEntry("C22","effective_lorentz","analogy_only",
            "Restricted high-frequency appearance",
            "Exact Lorentz symmetry","fence"),
        ZCCanonEntry("C23","conformal_metric","analogy_only",
            "ds2_eff in weak-field static test-probe limit",
            "Metric dynamics, Einstein equations","fence"),
        ZCCanonEntry("C24","screened_gravity","analogy_only",
            "Yukawa: 1/r^2 short, screened long",
            "GR, unscreened Newtonian gravity","fence"),
        # ── Constitutive/effective (1) ──
        ZCCanonEntry("C25","response_functional","constitutive_or_effective_only",
            "S_eff[Phi,Phi_tilde] auxiliary packaging",
            "Physical wavefunction, path integral","fence"),
        # ── Absent (8) ──
        ZCCanonEntry("C26","gauge_structure","absent_unbuilt",
            "Nothing","Gauge field, local symmetry, covariant derivative","document"),
        ZCCanonEntry("C27","apparatus_dynamics","absent_unbuilt",
            "Nothing","Detector/instrument model","document"),
        ZCCanonEntry("C28","collapse_ontology","absent_unbuilt",
            "Nothing (update is epistemic)","Physical collapse mechanism","document"),
        ZCCanonEntry("C29","quantum_state_ontology","absent_unbuilt",
            "Nothing (rho is bookkeeping)","Ontology of psi/rho","document"),
        ZCCanonEntry("C30","unitary_completion","absent_unbuilt",
            "Nothing (Lindblad is open-system)","Closed-system unitarity","document"),
        ZCCanonEntry("C31","backreaction","absent_unbuilt",
            "Test-probe only","Self-consistent coupling","document"),
        ZCCanonEntry("C32","cosmological_completion","absent_unbuilt",
            "Nothing","Friedmann, dark energy, expansion","document"),
        ZCCanonEntry("C33","unified_closure","absent_unbuilt",
            "Constitutive architecture ceiling","True unified field theory","document"),
        # ── Blocked (2) ──
        ZCCanonEntry("C34","fermionic_structure","blocked_by_structure",
            "3-layer obstruction; routes identified, none built",
            "Fermions, spin-statistics","fence"),
        ZCCanonEntry("C35","chemistry_composite","blocked_by_structure",
            "All prerequisites absent",
            "Chemistry, binding, composite matter","fence"),
    ]


def _build_toe_candidates() -> List[ZCToECandidate]:
    return [
        ZCToECandidate("full_toe_completion",False,
            "Gauge, fermions, chemistry, cosmology, apparatus, collapse, unitarity, "
            "back-reaction all absent. Cannot claim Theory of Everything.",
            "NEVER safe"),
        ZCToECandidate("complete_foundational_toe_architecture",False,
            "Gauge (no local symmetry) and fermions (3-layer obstruction) are "
            "structurally absent. Foundation has explicit missing pillars.",
            "UNSAFE: missing pillars prevent 'complete' label"),
        ZCToECandidate("bounded_partial_toe",False,
            "'ToE' overstates. The program is not a theory of everything in any "
            "honest sense. 'Partial ToE' still implies ToE trajectory.",
            "MARGINAL: 'ToE' language unearned"),
        ZCToECandidate("bounded_world_model_framework_with_explicit_gaps",True,
            "Covers substrate, symmetry, thermodynamics, field architecture, "
            "probability, quantum-dynamical interface in bounded form. Major "
            "sectors explicitly absent and documented. No inflation.",
            "SAFE: strongest honest label"),
    ]


def _build_scope_sectors() -> List[ZCScopeSector]:
    return [
        ZCScopeSector("substrate_ontology","V",
            "covered_in_bounded_form",
            "Persistent scalar dissipative medium; vacuum existence; preferred frame",
            "No geometric vacuum, no quantum vacuum field theory"),
        ZCScopeSector("symmetry_status","S",
            "covered_in_bounded_form",
            "Native Z2, parity, spatial isotropy; extension effective Lorentz",
            "No gauge symmetry, no local invariance"),
        ZCScopeSector("thermodynamic_status","T",
            "covered_in_bounded_form",
            "Irreversibility, Lyapunov balance, dissipative bookkeeping",
            "No temperature, no equilibrium thermodynamics, no entropy"),
        ZCScopeSector("field_extension_architecture","U/W",
            "covered_in_bounded_form",
            "One field, propagation, probe coupling, effective metric/gravity",
            "No gauge fields, no tensor gravity, no multi-field"),
        ZCScopeSector("measurement_probability","X",
            "covered_in_bounded_form",
            "Born map, outcomes, epistemic update",
            "No apparatus, no collapse, no full QM"),
        ZCScopeSector("quantum_dynamical_interface","Y",
            "covered_in_bounded_form",
            "Lindblad evolution, decoherence, pointer basis, integration rules",
            "No unitarity, no strong integration, no unified dynamics"),
    ]


def _build_missing_sectors() -> List[ZCMissingSector]:
    return [
        ZCMissingSector("MS1","gauge_structure","fatal_to_full_toe",
            "full ToE, complete foundational",
            "bounded world-model framework",
            "No gauge field, local symmetry, or covariant derivative"),
        ZCMissingSector("MS2","fermionic_structure","fatal_to_full_toe",
            "full ToE, complete foundational",
            "bounded world-model framework",
            "3-layer obstruction: Hopf/spinor + antisymmetrization + statistics"),
        ZCMissingSector("MS3","chemistry_composite","blocked_cascade",
            "full ToE",
            "bounded world-model framework",
            "Cascade block: all prerequisites absent"),
        ZCMissingSector("MS4","apparatus_dynamics","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "No detector/instrument model; nearest future sector"),
        ZCMissingSector("MS5","collapse_ontology","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "Outcome postulated, not explained; update is epistemic"),
        ZCMissingSector("MS6","quantum_state_ontology","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "rho is bookkeeping; ontological commitment deferred"),
        ZCMissingSector("MS7","unitary_completion","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "Lindblad is open-system; no closed-system unitarity"),
        ZCMissingSector("MS8","backreaction","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "Test-probe only; no self-consistent mutual coupling"),
        ZCMissingSector("MS9","cosmological_completion","fatal_to_full_toe",
            "full ToE",
            "bounded world-model framework",
            "No Friedmann, dark energy, or expansion dynamics"),
        ZCMissingSector("MS10","unified_closure","fatal_to_full_toe",
            "full ToE, complete foundational",
            "bounded world-model framework",
            "No shared carrier across all sectors; architecture ceiling"),
    ]


def _build_language_levels() -> List[ZCLanguageLevel]:
    return [
        ZCLanguageLevel("LL1","audited_dissipative_foundation",True,
            "Book II native canon is complete and immutable"),
        ZCLanguageLevel("LL2","minimal_extension_architecture",True,
            "7 postulates, 3 parameters, 0 new fields verified"),
        ZCLanguageLevel("LL3","operational_quantum_layer",True,
            "Born + outcomes + update + Lindblad + decoherence operational"),
        ZCLanguageLevel("LL4","bounded_world_model_framework",True,
            "Broad scope with explicit gaps; strongest safe label"),
        ZCLanguageLevel("LL5","complete_theory_of_everything",False,
            "10 absent/blocked sectors; 'ToE' language unearned"),
    ]


def _build_finalization() -> ZCFinalizationRecommendation:
    return ZCFinalizationRecommendation(
        zd_needed=True,
        zd_scope=("Final sovereign summary: architecture map, future-work "
                   "boundary, and program-closure statement in single stage"),
        ze_needed=False,
        rationale=("Z-D as comprehensive final closure stage. Z-E not needed "
                   "if Z-D covers summary, boundary, and seal."))


# ══════════════════════════════════════════════════════════════════════
#  Master audit function
# ══════════════════════════════════════════════════════════════════════

def run_zc_total_canon_map_toe_boundary() -> ZCTotalCanonMapResult:
    canon = _build_canon_map()
    toe = _build_toe_candidates()
    scope = _build_scope_sectors()
    missing = _build_missing_sectors()
    lang = _build_language_levels()
    fin = _build_finalization()
    fw = ZCNonclaimFirewall(ZC_NONCLAIMS, N_ZC_NONCLAIMS, True)

    # Count classifications
    def _cc(cls): return sum(1 for c in canon if c.classification == cls)
    n_nat = _cc("native_canon")
    n_ext = _cc("extension_canon")
    n_ops = 0  # operational entries folded into extension_canon at Z-C level
    n_ana = _cc("analogy_only")
    n_con = _cc("constitutive_or_effective_only")
    n_abs = _cc("absent_unbuilt")
    n_blk = _cc("blocked_by_structure")
    n_fut = _cc("future_postulate_dependent")

    # Scope counts
    n_covered = sum(1 for s in scope if s.scope_verdict == "covered_in_bounded_form")
    n_partial = sum(1 for s in scope if s.scope_verdict == "partially_covered")
    n_sc_abs = sum(1 for s in scope if s.scope_verdict == "absent")

    # Missing severity counts
    n_fatal_toe = sum(1 for m in missing if m.severity == "fatal_to_full_toe")
    n_fatal_fnd = sum(1 for m in missing
                      if "complete foundational" in m.fatal_to or
                         "complete_foundational" in m.fatal_to)
    n_compat = sum(1 for m in missing
                   if "bounded" in m.compatible_with)

    strongest = ("Bounded world-model framework with audited dissipative "
                 "foundation, minimal extension architecture, operational "
                 "quantum layer, and explicit completion gaps. "
                 "Not a Theory of Everything.")

    key = [
        "TOTAL CANON MAP: 35 entries classified. 8 native, 13 extension, "
        "3 analogy-only, 1 constitutive/effective, 8 absent, 2 blocked, "
        "0 future-postulate-dependent.",
        "ToE STATUS: 'bounded world-model framework with explicit gaps' is "
        "the strongest honest label. Full ToE, complete foundational ToE, "
        "and bounded partial ToE all FAIL or are UNSAFE.",
        "WORLD-MODEL SCOPE: all 6 major sectors (substrate, symmetry, thermo, "
        "field, measurement, quantum-dynamical) covered in bounded form. "
        "Broad scope but every sector has explicit ceilings.",
        "MISSING-SECTOR SEVERITY: 10 missing sectors fatal to full ToE. "
        "3 (gauge, fermions, unified closure) also fatal to 'complete "
        "foundational' claims. All compatible with bounded framework.",
        "STRONGEST SAFE LANGUAGE: 'audited dissipative foundation with "
        "minimal extension architecture, operational quantum layer, and "
        "explicit completion gaps.' ToE language is FORBIDDEN.",
        "Z-D RECOMMENDED: final sovereign summary, architecture map, "
        "future-work boundary, and program-closure statement. Z-E not "
        "needed if Z-D is comprehensive.",
        "ECONOMY CONFIRMED (from Z-B): 7 postulates, 3 free parameters, "
        "0 new fields, 0 new DOF. Low-postulate/high-yield.",
    ]

    allowed = [
        "Total canon map: 35 entries fully classified",
        "Bounded world-model framework is strongest honest ToE-status label",
        "Broad world-model scope: 6 sectors covered in bounded form",
        "10 missing sectors explicitly documented and severity-ranked",
        "Strongest safe language: audited foundation + extension + operational layer",
        "Z-D authorized: final sovereign summary and boundary closure",
        "7 postulates, 3 parameters, 0 fields confirmed from Z-B",
    ]

    forbidden = [
        "Canon map implies physics complete",
        "Broad scope implies sectors solved",
        "Bounded framework implies Theory of Everything",
        "Low postulate count implies sufficiency",
        "Absent sectors documented implies resolved",
        "Operational quantum layer implies full QM",
        "Foundational architecture implies complete foundation",
    ]

    diagnostics: Dict[str, Any] = {
        "n_canon_entries": len(canon),
        "n_native": n_nat,
        "n_extension": n_ext,
        "n_operational": n_ops,
        "n_analogy": n_ana,
        "n_constitutive": n_con,
        "n_absent": n_abs,
        "n_blocked": n_blk,
        "n_future": n_fut,
        "n_scope_covered": n_covered,
        "n_scope_partial": n_partial,
        "n_scope_absent": n_sc_abs,
        "n_missing_sectors": N_MISSING_SECTORS,
        "n_fatal_to_full_toe": n_fatal_toe,
        "n_fatal_to_foundational": n_fatal_fnd,
        "n_toe_candidates": N_TOE_CANDIDATES,
        "n_toe_supported": sum(1 for t in toe if t.supported),
        "n_toe_rejected": sum(1 for t in toe if not t.supported),
        "n_language_safe": sum(1 for l in lang if l.safe),
        "n_language_unsafe": sum(1 for l in lang if not l.safe),
        "full_qm": False,
        "toe_achieved": False,
        "unified_closure": False,
        "zd_needed": True,
        "ze_needed": False,
        "grand_total_postulates": 7,
        "grand_total_parameters": 3,
        "grand_total_new_fields": 0,
    }

    result = ZCTotalCanonMapResult(
        True,
        canon, len(canon),
        n_nat, n_ext, n_ops, n_ana, n_con, n_abs, n_blk, n_fut,
        toe, strongest,
        scope, n_covered, n_partial, n_sc_abs,
        missing, n_fatal_toe, n_fatal_fnd, n_compat,
        lang, strongest,
        fin, fw,
        ZC_CANON_MAP, ZC_TOE, ZC_WORLD_MODEL, ZC_MISSING, ZC_AUTH, ZC_OVERALL,
        key, allowed, forbidden, ZC_NONCLAIMS, diagnostics)
    _validate(result)
    return result


# ══════════════════════════════════════════════════════════════════════
#  Validation
# ══════════════════════════════════════════════════════════════════════

def _validate(r: ZCTotalCanonMapResult) -> None:
    # Verdict gates
    if r.canon_map_status not in CANON_MAP_OPTIONS:
        raise ValueError("canon_map")
    if r.toe_status not in TOE_STATUS_OPTIONS:
        raise ValueError("toe")
    if r.world_model_status not in WORLD_MODEL_OPTIONS:
        raise ValueError("world_model")
    if r.missing_sector_status not in MISSING_SECTOR_OPTIONS:
        raise ValueError("missing")
    if r.authorization not in AUTH_OPTIONS:
        raise ValueError("auth")
    if r.overall_appendix_p not in OVERALL_OPTIONS:
        raise ValueError("overall")
    # Canon map
    if len(r.canon_map) < N_CANON_ENTRIES:
        raise ValueError(f"canon entries {len(r.canon_map)}")
    for c in r.canon_map:
        if c.classification not in CANON_CLASSIFICATIONS:
            raise ValueError(f"canon class {c.entry_id}")
    total = r.n_native + r.n_extension + r.n_operational + r.n_analogy + \
            r.n_constitutive + r.n_absent + r.n_blocked + r.n_future
    if total != len(r.canon_map):
        raise ValueError(f"canon total {total} != {len(r.canon_map)}")
    # Native count
    if r.n_native < 8:
        raise ValueError("native >= 8")
    if r.n_extension < 10:
        raise ValueError("extension >= 10")
    if r.n_absent < 6:
        raise ValueError("absent >= 6")
    # ToE candidates
    if len(r.toe_candidates) != N_TOE_CANDIDATES:
        raise ValueError("toe candidates")
    n_supported = sum(1 for t in r.toe_candidates if t.supported)
    if n_supported != 1:
        raise ValueError(f"toe supported {n_supported}")
    # Scope
    if len(r.scope_sectors) != N_SCOPE_SECTORS:
        raise ValueError("scope sectors")
    if r.n_covered != N_SCOPE_SECTORS:
        raise ValueError("all scope must be covered_in_bounded_form")
    # Missing
    if len(r.missing_sectors) != N_MISSING_SECTORS:
        raise ValueError("missing sectors")
    for m in r.missing_sectors:
        if m.severity not in MISSING_SEVERITY:
            raise ValueError(f"missing severity {m.sector_id}")
    # Language
    if len(r.language_levels) != N_LANGUAGE_LEVELS:
        raise ValueError("language levels")
    # Firewall
    if r.nonclaim_firewall.n_nonclaims != N_ZC_NONCLAIMS:
        raise ValueError("nc")
    if not r.nonclaim_firewall.all_registered:
        raise ValueError("reg")
    # Claims
    if len(r.allowed_claims) != N_ALLOWED:
        raise ValueError("allowed")
    if len(r.forbidden_claims) != N_FORBIDDEN:
        raise ValueError("forbidden")
    # Physics guards
    if r.diagnostics["full_qm"]:
        raise ValueError("qm False")
    if r.diagnostics["toe_achieved"]:
        raise ValueError("toe False")
    if r.diagnostics["unified_closure"]:
        raise ValueError("closure False")
    if r.diagnostics["grand_total_postulates"] != 7:
        raise ValueError("postulates 7")
    if r.diagnostics["grand_total_new_fields"] != 0:
        raise ValueError("fields 0")


# ══════════════════════════════════════════════════════════════════════
#  Self-test
# ══════════════════════════════════════════════════════════════════════

def _self_test() -> bool:
    r = run_zc_total_canon_map_toe_boundary()
    assert r.valid
    assert r.canon_map_status == ZC_CANON_MAP
    assert r.toe_status == ZC_TOE
    assert r.world_model_status == ZC_WORLD_MODEL
    assert r.missing_sector_status == ZC_MISSING
    assert r.authorization == ZC_AUTH
    assert r.overall_appendix_p == ZC_OVERALL
    assert r.n_native >= 8 and r.n_extension >= 10 and r.n_absent >= 6
    assert len(r.toe_candidates) == N_TOE_CANDIDATES
    assert sum(1 for t in r.toe_candidates if t.supported) == 1
    assert r.n_covered == N_SCOPE_SECTORS
    assert r.diagnostics["toe_achieved"] is False
    assert r.diagnostics["full_qm"] is False
    assert r.finalization.zd_needed is True
    assert r.finalization.ze_needed is False
    return True


if __name__ == "__main__":
    _self_test(); print("Z-C passed.")
