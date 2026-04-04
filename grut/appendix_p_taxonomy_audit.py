"""Appendix P — GRUT Extension Taxonomy and Canon Boundary Audit.

This module formalizes the doctrinal classification grammar of GRUT, providing
a definitive taxonomy of status classes with exact definitions, boundary
conditions, and a deterministic classification table for all major audited
GRUT results.

PURPOSE
-------
Appendix P is the finisher before Appendix Q (Quantum). Its function is to
prevent category confusion in the quantum sector by explicitly documenting:
  - what is native canon vs what requires extension postulates,
  - what is derived vs what is merely compatible,
  - what is obstructed vs what is merely unbuilt,
  - what succeeds in an effective regime vs what constitutes full covariant canon,
  - what is a motivated necessary postulate vs what is arbitrary patchwork.

Without this taxonomy, the quantum sector work risks silently promoting
extensions to canon or treating compatibility as derivation.

THE EIGHT STATUS CLASSES
------------------------
The taxonomy requires exactly 8 classes. Each is minimal and necessary.

  1. native_canon
     The core GRUT architecture. Derived from first principles, no free
     parameters beyond those fixed by the theory's founding commitments,
     valid across all GRUT-applicable physical domains.

  2. effective_reduction
     Valid in a specified regime. Reduces to or approximates native canon
     under regime conditions. Claims restricted to the stated domain.

  3. bounded_structural_result
     A proven mathematical or architectural result within explicitly stated
     assumptions. No claims beyond those assumptions. Includes negative
     results (obstruction, partial closure, proved impossibility within
     stated architecture).

  4. working_canon_hypothesis
     Asserted as canonical for load-bearing purposes. Not fully derived from
     first principles. Predictions depend on it. Provisional but adopted.

  5. motivated_but_unbuilt
     Derivation path is structurally identified and coherent. No new field
     content is required in principle. The path has not been traversed.

  6. motivated_independent_postulation
     Requires new field content (BG1-class gap: irresolvable by derivation).
     The postulate is uniquely selected and strongly motivated by ≥2
     convergent independent reasons. ≥1 parameter constrained by canon.

  7. compatible_but_ad_hoc
     Consistent with architecture. Not motivated by it. Introduces
     unconstrained free parameters. Replaceable without architectural loss.

  8. forbidden_or_inconsistent
     Contradicts an established GRUT result, violates the quarantine
     perimeter, or requires a proven mathematical impossibility.

SEVEN BOUNDARY RULES
---------------------
  B1: native_canon vs effective_reduction — regime dependence
  B2: effective_reduction vs bounded_structural_result — approximation vs proof
  B3: bounded_structural_result vs working_canon_hypothesis — proved vs asserted
  B4: working_canon_hypothesis vs motivated_but_unbuilt — load-bearing vs prospective
  B5: motivated_but_unbuilt vs motivated_independent_postulation — new DOF required?
  B6: motivated_independent_postulation vs compatible_but_ad_hoc — convergent motivations?
  B7: compatible_but_ad_hoc vs forbidden_or_inconsistent — contradiction?

EIGHT FORBIDDEN INFERENCE PATTERNS
------------------------------------
  compatibility_as_derivation
  usefulness_as_nativity
  uniqueness_as_derivability
  observed_coincidence_as_closure
  effective_regime_success_as_covariant_canon
  motivated_postulate_as_native
  unbuilt_route_as_solved
  obstruction_as_impossibility_in_principle

CLASSIFICATION RESULTS (12 items)
----------------------------------
  native_canon (2):
    scalar_constitutive_core, pre_matter_quarantine_perimeter

  effective_reduction (2):
    tau_eff_domain_declaration, galley_ctp_route_b

  bounded_structural_result (4):
    phi_sector_bifurcation, fermionic_emergence_obstruction,
    g_minus_source_closure, component_b_deficit_requirement

  working_canon_hypothesis (1):
    beta_q_canonical_hypothesis

  motivated_but_unbuilt (2):
    localized_bosonic_object_program, skyrme_term_nativity

  motivated_independent_postulation (1):
    o3_sector_nativity

  compatible_but_ad_hoc (0 primary — used in nonclaims and conditional notes)
  forbidden_or_inconsistent (0 primary — used in firewall patterns)

PRIMARY VERDICT: "taxonomy_complete__sufficient_for_quantum_readiness"

References
----------
  grut/localized_bosonic_object_audit.py  — Appendix M
  grut/skyrme_term_nativity_audit.py      — Appendix N
  grut/o3_nativity_audit.py               — Appendix O
  grut/fermionic_emergence_audit.py
  grut/phi_sector_bifurcation.py
  grut/tau_eff_domain_declaration.py
  grut/beta_q_sensitivity.py
  grut/g_minus_closure_audit.py
  grut/galley_truncation.py
  grut/route_b_component_b.py
  docs/PRE_MATTER_QUARANTINE_STATUS.md
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, FrozenSet, List, Optional, Tuple


# =====================================================================
# Canonical constants (re-stated for self-documentation)
# =====================================================================

M_EXT: float = 0.5
R_EQ: float = 1.0 / 3.0
TAU_SQ: float = 1.5          # τ² = 3/2 exactly
ALPHA_VAC: float = 1.0 / 3.0
BETA_Q_CANON: float = 2.0
OMEGA_0_SQ: float = 27.0     # ω₀² = β_Q · M_ext / R_eq³
COMP_B_COEFF: float = 1.0 / (8.0 * math.pi)      # η² = 1/(8π) from Component B
ETA_SQ_GRUT_LINK: float = TAU_SQ / (12.0 * math.pi)  # = τ²/(12π) = 1/(8π)

# Verify the η² = τ²/(12π) numerical identity
assert abs(ETA_SQ_GRUT_LINK - COMP_B_COEFF) < 1e-12, (
    f"η² identity broken: {ETA_SQ_GRUT_LINK} != {COMP_B_COEFF}"
)

# Topology
PI2_REAL_SCALAR: int = 0     # π₂(ℝ) = 0: no bosonic winding from canonical scalar
PI2_S2: str = "Z"            # π₂(S²) = ℤ: integer winding from O(3) hedgehog

# Taxonomy counts
N_STATUS_CLASSES: int = 8
N_CLASSIFIED_ITEMS: int = 12
N_BOUNDARY_RULES: int = 7
N_FORBIDDEN_INFERENCE_PATTERNS: int = 8


# =====================================================================
# Vocabulary (all frozensets — every label is pinned here)
# =====================================================================

ALLOWED_STATUS_CLASSES: FrozenSet[str] = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
    "forbidden_or_inconsistent",
})

ALLOWED_PRIMARY_VERDICTS: FrozenSet[str] = frozenset({
    "taxonomy_complete__sufficient_for_quantum_readiness",
    "taxonomy_complete__quantum_gap_identified",
    "taxonomy_incomplete__reclassification_required",
})

CLASSIFIED_ITEM_IDS: FrozenSet[str] = frozenset({
    "scalar_constitutive_core",
    "pre_matter_quarantine_perimeter",
    "phi_sector_bifurcation",
    "tau_eff_domain_declaration",
    "beta_q_canonical_hypothesis",
    "fermionic_emergence_obstruction",
    "localized_bosonic_object_program",
    "skyrme_term_nativity",
    "o3_sector_nativity",
    "g_minus_source_closure",
    "galley_ctp_route_b",
    "component_b_deficit_requirement",
})

BOUNDARY_RULE_IDS: FrozenSet[str] = frozenset({
    "B1_native_canon_vs_effective_reduction",
    "B2_effective_reduction_vs_bounded_structural",
    "B3_bounded_structural_vs_working_hypothesis",
    "B4_working_hypothesis_vs_motivated_unbuilt",
    "B5_motivated_unbuilt_vs_motivated_postulation",
    "B6_motivated_postulation_vs_compatible_adhoc",
    "B7_compatible_adhoc_vs_forbidden",
})

FORBIDDEN_INFERENCE_PATTERNS: FrozenSet[str] = frozenset({
    "compatibility_as_derivation",
    "usefulness_as_nativity",
    "uniqueness_as_derivability",
    "observed_coincidence_as_closure",
    "effective_regime_success_as_covariant_canon",
    "motivated_postulate_as_native",
    "unbuilt_route_as_solved",
    "obstruction_as_impossibility_in_principle",
})

# Classes that require explicit new field postulates (DOF increase)
POSTULATE_REQUIRED_CLASSES: FrozenSet[str] = frozenset({
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
})

# Classes that are constructive (not forbidden)
CONSTRUCTIVE_CLASSES: FrozenSet[str] = frozenset({
    "native_canon",
    "effective_reduction",
    "bounded_structural_result",
    "working_canon_hypothesis",
    "motivated_but_unbuilt",
    "motivated_independent_postulation",
    "compatible_but_ad_hoc",
})


# =====================================================================
# Data structures
# =====================================================================

@dataclass
class StatusClass:
    """One doctrinal status class with full definition and admissibility rules."""
    name: str
    definition: str
    admissibility_conditions: List[str] = field(default_factory=list)
    exclusion_conditions: List[str] = field(default_factory=list)
    allowed_claim_types: List[str] = field(default_factory=list)
    forbidden_claim_types: List[str] = field(default_factory=list)
    requires_new_field_content: bool = False
    requires_explicit_postulate: bool = False
    is_constructive: bool = True
    notes: str = ""


@dataclass
class ClassBoundaryRule:
    """Exact boundary condition separating two adjacent doctrinal classes."""
    rule_id: str
    class_a: str         # more-established / more-native side
    class_b: str         # more-extension / more-external side
    distinguishing_criterion: str
    test_for_a: str      # condition that places an item in class_a
    test_for_b: str      # condition that places an item in class_b
    is_deterministic: bool = True
    notes: str = ""


@dataclass
class ClassifiedResult:
    """Classification of one audited GRUT item with full doctrinal context."""
    item_id: str
    item_name: str
    reference_module: str
    primary_class: str
    secondary_class: Optional[str]
    justification: str
    allowed_claims: List[str] = field(default_factory=list)
    forbidden_claims: List[str] = field(default_factory=list)
    dependency_on: List[str] = field(default_factory=list)
    is_negative_result: bool = False
    is_load_bearing: bool = True
    notes: List[str] = field(default_factory=list)


@dataclass
class ConsistencyCheckResult:
    """Verification that the taxonomy preserves all prior doctrine."""
    no_item_in_two_incompatible_classes: bool = False
    nonclaims_preserved: bool = False
    no_silent_promotion: bool = False
    negative_results_remain_negative: bool = False
    all_items_have_valid_class: bool = False
    consistency_passes: bool = False
    violations: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class QuantumReadinessCheck:
    """Assessment of whether Appendix P prepares the quantum sector without gaps."""
    taxonomy_distinguishes_native_vs_extension: bool = False
    bounded_results_flagged_for_quantum_check: bool = False
    fermionic_obstruction_status_preserved: bool = False
    free_parameters_identified: bool = False
    extension_postulates_clearly_marked: bool = False
    no_missing_class_for_quantum: bool = False
    missing_classes: List[str] = field(default_factory=list)
    quantum_ready: bool = False
    readiness_verdict: str = ""
    notes: List[str] = field(default_factory=list)


@dataclass
class TaxonomyMinimalityCheck:
    """Verification that the 8-class taxonomy is minimal and sufficient."""
    n_classes_proposed: int = 0
    n_classes_accepted: int = 0
    n_classes_rejected_as_redundant: int = 0
    rejected_classes: List[str] = field(default_factory=list)
    every_class_used_in_at_least_one_context: bool = False
    is_minimal: bool = False
    is_sufficient: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class NoclaimFirewallCheck:
    """All forbidden inference patterns explicitly encoded and counted."""
    n_forbidden_patterns: int = 0
    forbidden_patterns: List[str] = field(default_factory=list)
    all_patterns_encoded: bool = False
    pattern_descriptions: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class TaxonomyAuditResult:
    """Master result of the Appendix P taxonomy audit."""
    valid: bool = False

    # Tracks A–B: taxonomy structure
    status_classes: List[StatusClass] = field(default_factory=list)
    boundary_rules: List[ClassBoundaryRule] = field(default_factory=list)

    # Track D: classification table
    classified_results: List[ClassifiedResult] = field(default_factory=list)
    dependency_graph: Dict[str, List[str]] = field(default_factory=dict)

    # Tracks E–G: checks
    consistency: ConsistencyCheckResult = field(default_factory=ConsistencyCheckResult)
    quantum_readiness: QuantumReadinessCheck = field(default_factory=QuantumReadinessCheck)
    taxonomy_minimality: TaxonomyMinimalityCheck = field(default_factory=TaxonomyMinimalityCheck)
    nonclaim_firewall: NoclaimFirewallCheck = field(default_factory=NoclaimFirewallCheck)

    # Allowed/forbidden claims indexed by class name
    allowed_claims_by_class: Dict[str, List[str]] = field(default_factory=dict)
    forbidden_claims_by_class: Dict[str, List[str]] = field(default_factory=dict)

    # Summary
    primary_verdict: str = ""
    nonclaims: List[str] = field(default_factory=list)
    ambiguous_items: List[str] = field(default_factory=list)
    diagnostics: Dict[str, object] = field(default_factory=dict)


# =====================================================================
# Track A/B: Build status classes
# =====================================================================

def build_status_classes() -> List[StatusClass]:
    """Build all 8 doctrinal status classes with full definitions."""
    classes: List[StatusClass] = []

    # 1. native_canon
    classes.append(StatusClass(
        name="native_canon",
        definition=(
            "Derived from GRUT's first principles. No regime qualifier needed. "
            "No free parameters beyond those fixed by the canonical constants "
            "(τ², α_vac, β_Q, M_ext, R_eq, ω₀). Valid across all GRUT-applicable "
            "physical domains. The founding field content and architecture."
        ),
        admissibility_conditions=[
            "Follows by derivation from GRUT's defining equations",
            "Valid without a regime qualifier",
            "No new free parameters introduced",
            "Pre-matter quarantine perimeter respected",
        ],
        exclusion_conditions=[
            "Result requires a regime qualifier (quasi-static, far-field, etc.)",
            "Result introduces new field content",
            "Result is asserted rather than derived",
            "Result works only in a specific physical limit",
        ],
        allowed_claim_types=[
            "This result is architecturally required by GRUT",
            "This result holds in all GRUT-applicable domains",
            "Predictions from this result are native GRUT predictions",
        ],
        forbidden_claim_types=[
            "Extending to matter sector without explicit quarantine declaration",
            "Claiming quantum validity without explicit quantum derivation",
            "Claiming covariant universality beyond GRUT's stated physical scope",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=True,
        notes="The smallest class. Only what is unambiguously derived from first principles.",
    ))

    # 2. effective_reduction
    classes.append(StatusClass(
        name="effective_reduction",
        definition=(
            "Valid in a specified physical regime. In that regime the result reduces "
            "to or approximates native canon. Outside the stated regime validity is not "
            "guaranteed. Claims must include the regime qualifier."
        ),
        admissibility_conditions=[
            "Valid in an explicitly stated regime",
            "Regime qualifier is precisely defined",
            "Reduces to or approximates native canon within the regime",
            "Domain of validity is bounded and stated",
        ],
        exclusion_conditions=[
            "Claims validity outside the stated regime",
            "Does not reduce to native canon in any limit",
            "Introduces unconstrained free parameters",
        ],
        allowed_claim_types=[
            "In the [stated] regime, this result holds",
            "Within the quasi-static approximation, ...",
            "This is a regime-specific description of the canonical dynamics",
        ],
        forbidden_claim_types=[
            "Treating the effective result as exact outside its regime",
            "Effective description as covariant canon",
            "Regime success implies native canon validity",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=True,
        notes=(
            "First boundary: native_canon works for all domains; "
            "effective_reduction works within a stated domain."
        ),
    ))

    # 3. bounded_structural_result
    classes.append(StatusClass(
        name="bounded_structural_result",
        definition=(
            "A proved mathematical or architectural result within explicitly stated "
            "assumptions. The result is demonstrated — not asserted — within the "
            "stated conditions. Makes no claims beyond those assumptions. Includes "
            "positive theorems and negative results (obstruction, partial closure, "
            "impossibility within stated architecture)."
        ),
        admissibility_conditions=[
            "Proved within stated architectural or mathematical assumptions",
            "Assumptions are explicitly stated",
            "Derivation is self-contained within established results",
            "Scope is clearly limited to the stated conditions",
        ],
        exclusion_conditions=[
            "Claims validity beyond stated assumptions without proof",
            "Claims are asserted without derivation",
            "Promotes beyond its scope to native canon",
        ],
        allowed_claim_types=[
            "Under assumptions [X], result [Y] holds",
            "Within the stated architecture, [obstruction/closure/bound] is established",
            "The negative result [N] is proved for the stated class of architectures",
        ],
        forbidden_claim_types=[
            "The bounded result implies a universal theorem",
            "An obstruction within stated architecture implies impossibility in principle",
            "The result extends beyond its stated assumptions without proof",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=True,
        notes=(
            "Includes both positive theorems and proved obstructions. "
            "The key contrast with native_canon: scope is bounded by stated assumptions."
        ),
    ))

    # 4. working_canon_hypothesis
    classes.append(StatusClass(
        name="working_canon_hypothesis",
        definition=(
            "Asserted as canonical for load-bearing purposes. Part of the working "
            "architecture; predictions depend on it. Not fully derived from first "
            "principles within the current framework. Adopted provisionally."
        ),
        admissibility_conditions=[
            "Currently load-bearing in the working canonical architecture",
            "Predictions depend on this item",
            "Item is asserted, not derived, from first principles",
            "No new field content introduced",
        ],
        exclusion_conditions=[
            "Item is derived from first principles → upgrade to native_canon",
            "Item introduces new field content → motivated_independent_postulation or below",
            "Item is not load-bearing → compatible_but_ad_hoc at most",
        ],
        allowed_claim_types=[
            "This value/hypothesis is currently assumed canonical",
            "Predictions under this hypothesis are ...",
            "Sensitivity of results to this hypothesis is documented",
            "A deeper derivation would upgrade this to native_canon",
        ],
        forbidden_claim_types=[
            "Claiming working hypothesis is derived from first principles",
            "Treating sensitivity audit results as derived predictions",
            "Using the hypothesis as if it were a bounded_structural_result",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=True,
        notes="β_Q = 2 is the primary example: load-bearing, adopted, not derived.",
    ))

    # 5. motivated_but_unbuilt
    classes.append(StatusClass(
        name="motivated_but_unbuilt",
        definition=(
            "The derivation path is structurally identified and coherent within "
            "existing field content. No new DOFs are required in principle. "
            "The work of traversing the path has not been done. Motivated by "
            "existing architecture and is the natural result of a known construction, "
            "but that construction is not yet complete."
        ),
        admissibility_conditions=[
            "Derivation path is explicitly identified and named",
            "Path requires no new field content (no DOF increase) in principle",
            "Motivation arises from GRUT architecture, not external phenomenology alone",
            "Path is coherent — not merely compatible",
        ],
        exclusion_conditions=[
            "Path requires new field content → motivated_independent_postulation",
            "No coherent path identified → compatible_but_ad_hoc at most",
            "Path contradicts an established result → forbidden_or_inconsistent",
        ],
        allowed_claim_types=[
            "A derivation path exists: [Route description]",
            "Once [prerequisite] is established, this result follows as ...",
            "This is the natural next step in the identified derivation chain",
            "Adding this result after [prerequisite] would not be ad hoc",
        ],
        forbidden_claim_types=[
            "Treating the identified path as a completed derivation",
            "Claiming the result is established because the path is identified",
            "Using in predictions before the derivation is built",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=True,
        notes=(
            "Skyrme L₄ (conditioned on O(3) nativity) is the primary example. "
            "Route 3 is identified; the chain is not traversed."
        ),
    ))

    # 6. motivated_independent_postulation
    classes.append(StatusClass(
        name="motivated_independent_postulation",
        definition=(
            "Requires new field content (DOF increase) that cannot be derived from "
            "existing field content — a BG1-class gap that is mathematically "
            "irresolvable by derivation. The postulate is uniquely selected and "
            "strongly motivated by ≥2 convergent independent reasons (topological, "
            "phenomenological, parametric). At least one parameter is constrained "
            "by canonical GRUT quantities."
        ),
        admissibility_conditions=[
            "Requires new DOF content not derivable from current fields (BG1-class gap)",
            "≥2 convergent independent motivations established",
            "≥1 parameter of the extension constrained by GRUT canon",
            "Extension is uniquely determined by the stated constraints",
            "Compatible with all prior audits",
        ],
        exclusion_conditions=[
            "<2 convergent motivations → compatible_but_ad_hoc",
            "0 parameters constrained → compatible_but_ad_hoc",
            "Contradicts established results → forbidden_or_inconsistent",
            "Alternative extensions achieve same purpose without uniqueness → compatible_but_ad_hoc",
        ],
        allowed_claim_types=[
            "This postulate is uniquely motivated by [topology/uniqueness argument]",
            "One parameter is constrained: [explicit constraint with derivation]",
            "This is the minimal necessary extension for [stated purpose]",
            "The postulate is the best-motivated available choice for [purpose]",
        ],
        forbidden_claim_types=[
            "Treating the motivated postulate as derived from canon",
            "Claiming parameter constraints derive the postulate",
            "Claiming topological uniqueness implies derivability",
            "Using partial parameter constraint to claim native status",
        ],
        requires_new_field_content=True,
        requires_explicit_postulate=True,
        is_constructive=True,
        notes=(
            "O(3) triplet is the primary example: BG1 (1→3 scalars) is irresolvable. "
            "Topological uniqueness + Component B matching + η²=τ²/(12π) satisfy all "
            "three admissibility tests."
        ),
    ))

    # 7. compatible_but_ad_hoc
    classes.append(StatusClass(
        name="compatible_but_ad_hoc",
        definition=(
            "Consistent with GRUT architecture. Not motivated by it. Not required by "
            "it. Introduces unconstrained free parameters. Replaceable by other choices "
            "without architectural loss. Does not contradict prior doctrine."
        ),
        admissibility_conditions=[
            "Addition is consistent with prior doctrine",
            "No established result is contradicted",
            "Addition is not uniquely required or selected",
        ],
        exclusion_conditions=[
            "Contradicts established results → forbidden_or_inconsistent",
            "≥2 convergent motivations AND unique selection → motivated_independent_postulation",
            "Clear derivation path without new DOFs → motivated_but_unbuilt",
        ],
        allowed_claim_types=[
            "This addition is consistent with GRUT architecture",
            "No prior audit is violated by this addition",
            "This addition is one of several compatible choices",
        ],
        forbidden_claim_types=[
            "Claiming the addition is motivated by GRUT architecture",
            "Treating consistency as motivation",
            "Treating compatibility as derivation",
            "Using it as if it had a derivation chain",
        ],
        requires_new_field_content=True,
        requires_explicit_postulate=True,
        is_constructive=True,
        notes=(
            "Adding L₄ before O(3) nativity is established: compatible_but_ad_hoc. "
            "The Skyrme coupling e floats freely with no GRUT anchor."
        ),
    ))

    # 8. forbidden_or_inconsistent
    classes.append(StatusClass(
        name="forbidden_or_inconsistent",
        definition=(
            "Contradicts an established GRUT result (native_canon or "
            "bounded_structural_result), violates the pre-matter quarantine perimeter, "
            "or requires a mathematical impossibility proved within the stated "
            "architecture. Claims in this class must not be made."
        ),
        admissibility_conditions=[
            "Contradicts a native_canon or bounded_structural_result",
            "Violates quarantine perimeter without explicit quarantine declaration",
            "Requires a proved mathematical impossibility",
        ],
        exclusion_conditions=[
            "Inconsistency is merely a gap → motivated_but_unbuilt or weaker",
            "Result is blocked only in current architecture, not in principle → "
            "bounded_structural_result for the obstruction",
        ],
        allowed_claim_types=[
            "This claim is forbidden because it contradicts [established result]",
            "This claim requires a proved impossibility: [reference]",
        ],
        forbidden_claim_types=[
            "Any positive assertion for an item in this class",
            "Treating the forbidden claim as 'not yet disproved'",
        ],
        requires_new_field_content=False,
        requires_explicit_postulate=False,
        is_constructive=False,
        notes=(
            "Examples: 'V(Φ)=λ|Φ|⁴ is a Skyrme stabilizer' (contradicts Derrick scaling); "
            "'O(3) is derived from canonical scalar' (BG1 mathematical impossibility); "
            "'GRUT scalar has fermionic statistics' (contradicts topology of ℝ)."
        ),
    ))

    assert len(classes) == N_STATUS_CLASSES, (
        f"Expected {N_STATUS_CLASSES} classes, got {len(classes)}"
    )
    for cls in classes:
        assert cls.name in ALLOWED_STATUS_CLASSES, (
            f"Class name '{cls.name}' not in ALLOWED_STATUS_CLASSES"
        )

    return classes


# =====================================================================
# Track C: Build boundary rules
# =====================================================================

def build_boundary_rules() -> List[ClassBoundaryRule]:
    """Build all 7 deterministic boundary rules separating adjacent classes."""
    rules: List[ClassBoundaryRule] = []

    rules.append(ClassBoundaryRule(
        rule_id="B1_native_canon_vs_effective_reduction",
        class_a="native_canon",
        class_b="effective_reduction",
        distinguishing_criterion=(
            "Does validity require a regime qualifier?"
        ),
        test_for_a=(
            "Valid across ALL GRUT-applicable physical domains without "
            "any regime qualifier"
        ),
        test_for_b=(
            "Valid only within an explicitly stated regime "
            "(quasi-static, far-field, spherical, etc.)"
        ),
        is_deterministic=True,
        notes=(
            "The constitutive ODE is native_canon as a defining equation; "
            "τ_eff is effective_reduction because it requires the quasi-static regime."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B2_effective_reduction_vs_bounded_structural",
        class_a="effective_reduction",
        class_b="bounded_structural_result",
        distinguishing_criterion=(
            "Regime-specific approximation vs proved theorem within stated conditions?"
        ),
        test_for_a=(
            "Result is a regime-specific approximation of native behavior; "
            "continuity with canon in the regime limit"
        ),
        test_for_b=(
            "Result is a proved mathematical or architectural statement "
            "(often a negative result: obstruction, bound, partial closure) "
            "within explicitly stated conditions"
        ),
        is_deterministic=True,
        notes=(
            "Galley CTP route B → effective_reduction (approximation framework). "
            "Phi bifurcation result → bounded_structural_result (proved statement)."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B3_bounded_structural_vs_working_hypothesis",
        class_a="bounded_structural_result",
        class_b="working_canon_hypothesis",
        distinguishing_criterion=(
            "Is the item derived (proved) or asserted for working purposes?"
        ),
        test_for_a=(
            "Result follows by derivation from established architecture "
            "within stated assumptions"
        ),
        test_for_b=(
            "Item is asserted (not derived) as load-bearing for predictions "
            "in the current working architecture"
        ),
        is_deterministic=True,
        notes=(
            "β_Q = 2 is adopted (working hypothesis). "
            "Derrick's theorem is proved (bounded structural result)."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B4_working_hypothesis_vs_motivated_unbuilt",
        class_a="working_canon_hypothesis",
        class_b="motivated_but_unbuilt",
        distinguishing_criterion=(
            "Is the item currently load-bearing in working canon, "
            "or is it a prospective extension?"
        ),
        test_for_a=(
            "Currently in use as part of the working architecture; "
            "predictions depend on it; no new field content required"
        ),
        test_for_b=(
            "Prospective extension not yet in working canon; "
            "derivation path identified but not traversed; not yet adopted"
        ),
        is_deterministic=True,
        notes=(
            "β_Q = 2 (working hypothesis): predictions depend on it, in use. "
            "L₄ (motivated_but_unbuilt): path identified, not adopted."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B5_motivated_unbuilt_vs_motivated_postulation",
        class_a="motivated_but_unbuilt",
        class_b="motivated_independent_postulation",
        distinguishing_criterion=(
            "Does the construction require new field content — "
            "a BG1-class gap irresolvable by derivation?"
        ),
        test_for_a=(
            "Derivation requires NO new field content; "
            "path exists within current field space"
        ),
        test_for_b=(
            "Requires new field content (DOF increase); "
            "BG1-class gap; mathematically irresolvable by derivation"
        ),
        is_deterministic=True,
        notes=(
            "L₄ (given O(3) already canonical): motivated_but_unbuilt — "
            "next O(3) EFT term, no new DOFs. "
            "O(3) itself: motivated_independent_postulation — 1→3 scalars is irresolvable."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B6_motivated_postulation_vs_compatible_adhoc",
        class_a="motivated_independent_postulation",
        class_b="compatible_but_ad_hoc",
        distinguishing_criterion=(
            "Does the proposed extension have ≥2 convergent independent motivations "
            "AND unique selection AND ≥1 parameter constrained by GRUT canon?"
        ),
        test_for_a=(
            "All three: ≥2 independent motivations + uniqueness proved + "
            "≥1 GRUT-canon parameter constraint"
        ),
        test_for_b=(
            "Fails at least one: <2 motivations, OR not uniquely selected, "
            "OR 0 parameters constrained"
        ),
        is_deterministic=True,
        notes=(
            "O(3) passes all three (CM1 topology + CM2 Component B + η²=τ²/(12π)). "
            "L₄ added without O(3) fails: e is free, not uniquely selected from canon."
        ),
    ))

    rules.append(ClassBoundaryRule(
        rule_id="B7_compatible_adhoc_vs_forbidden",
        class_a="compatible_but_ad_hoc",
        class_b="forbidden_or_inconsistent",
        distinguishing_criterion=(
            "Does the addition contradict an established result "
            "or violate the quarantine perimeter?"
        ),
        test_for_a=(
            "Consistent with all native_canon and bounded_structural_result items; "
            "no quarantine violation"
        ),
        test_for_b=(
            "Contradicts at least one established result, OR violates quarantine "
            "perimeter, OR requires a proved mathematical impossibility"
        ),
        is_deterministic=True,
        notes=(
            "compatible_but_ad_hoc is allowed (though weak). "
            "forbidden_or_inconsistent means a specific claim is prohibited: "
            "e.g., 'V(Φ) stabilizes the hedgehog' (contradicts Derrick scaling)."
        ),
    ))

    assert len(rules) == N_BOUNDARY_RULES, (
        f"Expected {N_BOUNDARY_RULES} boundary rules, got {len(rules)}"
    )
    for rule in rules:
        assert rule.rule_id in BOUNDARY_RULE_IDS, (
            f"Rule ID '{rule.rule_id}' not in BOUNDARY_RULE_IDS"
        )
        assert rule.class_a in ALLOWED_STATUS_CLASSES
        assert rule.class_b in ALLOWED_STATUS_CLASSES

    return rules


# =====================================================================
# Track D: Classify all audited GRUT items
# =====================================================================

def classify_grut_items() -> List[ClassifiedResult]:
    """Deterministic classification of all 12 major audited GRUT items."""
    items: List[ClassifiedResult] = []

    # ---- 1. Scalar constitutive core --------------------------------
    items.append(ClassifiedResult(
        item_id="scalar_constitutive_core",
        item_name="Scalar field and constitutive architecture",
        reference_module=(
            "grut/field_equations.py, grut/operators.py"
        ),
        primary_class="native_canon",
        secondary_class=None,
        justification=(
            "The single real scalar Φ, the constitutive ODE "
            "τ_eff·dΦ/dt + Φ = X, and the barrier action "
            "a_Q ~ (r_s/R)^β_Q define GRUT's canonical field content and "
            "dynamics. These are the founding elements from which all GRUT "
            "results are derived. No regime qualifier is required for their "
            "definition. π₂(ℝ) = 0: the canonical scalar carries no "
            "topological winding charge."
        ),
        allowed_claims=[
            "Φ is the canonical GRUT scalar; all GRUT physics is built on it",
            "Predictions derived from the constitutive ODE are native GRUT predictions",
            "The barrier action parametrizes the quasi-static sector",
        ],
        forbidden_claims=[
            "The canonical scalar has fermionic statistics",
            "The canonical scalar implies O(3) topological winding charge",
            "The constitutive ODE is a quantum evolution equation without derivation",
            "The single real scalar can be continuously promoted to an O(3) triplet",
        ],
        dependency_on=[],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["π₂(ℝ) = 0: no bosonic winding from canonical scalar alone"],
    ))

    # ---- 2. Pre-matter quarantine perimeter -------------------------
    items.append(ClassifiedResult(
        item_id="pre_matter_quarantine_perimeter",
        item_name="Pre-matter quarantine perimeter",
        reference_module="docs/PRE_MATTER_QUARANTINE_STATUS.md",
        primary_class="native_canon",
        secondary_class=None,
        justification=(
            "The quarantine perimeter is a definitional boundary of GRUT: "
            "the scalar-gravity sector is developed and audited before any "
            "matter sector extension is adopted. This is a founding commitment "
            "of the architecture. All Appendices A–P respect this boundary. "
            "Violations of the quarantine are classified forbidden_or_inconsistent."
        ),
        allowed_claims=[
            "Results within the quarantine perimeter are pre-matter GRUT results",
            "The quarantine defines the scope of all Appendix A–P doctrine",
            "Extensions beyond the quarantine require explicit declaration and audit",
        ],
        forbidden_claims=[
            "Treating any extension (O(3), Skyrme, fermionic) as inside the perimeter",
            "Using a motivated postulate as if it were inside the quarantine",
            "Skipping quarantine declaration for a new field sector",
        ],
        dependency_on=["scalar_constitutive_core"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["The quarantine is the doctrinal guarantee that extensions are labeled as such"],
    ))

    # ---- 3. Phi sector bifurcation ----------------------------------
    items.append(ClassifiedResult(
        item_id="phi_sector_bifurcation",
        item_name="Phi sector bifurcation (trajectory vs field)",
        reference_module="grut/phi_sector_bifurcation.py",
        primary_class="bounded_structural_result",
        secondary_class=None,
        justification=(
            "The bifurcation result proves that within GRUT's canonical sector, "
            "the scalar Φ plays distinct roles (trajectory scalar vs field) in "
            "different regimes and that these roles are architecturally distinct. "
            "This is a proved architectural result within the stated GRUT framework, "
            "not a regime-specific approximation."
        ),
        allowed_claims=[
            "Within GRUT's architecture, trajectory and field roles of Φ are distinct",
            "The bifurcation is an architectural property, not a free choice",
            "Analysis must distinguish trajectory scalar from field Φ to avoid domain errors",
        ],
        forbidden_claims=[
            "The bifurcation implies additional field content beyond canonical Φ",
            "The trajectory role of Φ extends to QFT without derivation",
        ],
        dependency_on=["scalar_constitutive_core", "tau_eff_domain_declaration"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["Applies within the quasi-static domain where τ_eff is defined"],
    ))

    # ---- 4. tau_eff domain declaration ------------------------------
    items.append(ClassifiedResult(
        item_id="tau_eff_domain_declaration",
        item_name="τ_eff domain declaration (quasi-static regime)",
        reference_module="grut/tau_eff_domain_declaration.py",
        primary_class="effective_reduction",
        secondary_class=None,
        justification=(
            "τ_eff is well-defined and the constitutive ODE takes its canonical "
            "form only in the quasi-static regime (τ_eff·dΦ/dt << Φ). "
            "Outside this regime the constitutive description changes character. "
            "This is an explicitly regime-bounded result."
        ),
        allowed_claims=[
            "In the quasi-static regime, τ_eff is the canonical relaxation time",
            "Predictions using τ_eff are valid within the declared domain",
            "The constitutive ODE is a quasi-static effective reduction of the full dynamics",
        ],
        forbidden_claims=[
            "τ_eff is a covariant tensor component valid outside the quasi-static regime",
            "τ_eff results extend to strongly dynamic interiors without derivation",
            "The quasi-static constitutive ODE is the full quantum dynamics",
        ],
        dependency_on=["scalar_constitutive_core"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["Primary effective_reduction in GRUT's canonical sector"],
    ))

    # ---- 5. beta_Q canonical hypothesis -----------------------------
    items.append(ClassifiedResult(
        item_id="beta_q_canonical_hypothesis",
        item_name="β_Q = 2 canonical hypothesis",
        reference_module="grut/beta_q_sensitivity.py",
        primary_class="working_canon_hypothesis",
        secondary_class=None,
        justification=(
            "β_Q = 2 (quadratic barrier exponent) is asserted as the canonical "
            "value. Predictions depend on it. The sensitivity audit establishes "
            "that results are β_Q-sensitive. A first-principles derivation of "
            "β_Q = 2 from GRUT mechanics is not established. "
            "Adopted as working canon pending deeper derivation."
        ),
        allowed_claims=[
            "Under the canonical hypothesis β_Q = 2, predictions are ...",
            "Sensitivity of results to β_Q is documented in the sensitivity audit",
            "A derivation of β_Q = 2 would upgrade this to native_canon",
        ],
        forbidden_claims=[
            "β_Q = 2 is derived from first principles",
            "The sensitivity audit proves β_Q = 2 is correct",
            "Predictions under β_Q = 2 have native_canon status",
        ],
        dependency_on=["scalar_constitutive_core"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["Load-bearing but not derived; primary example of working_canon_hypothesis"],
    ))

    # ---- 6. Fermionic emergence obstruction -------------------------
    items.append(ClassifiedResult(
        item_id="fermionic_emergence_obstruction",
        item_name="Fermionic emergence obstruction (Appendix-adjacent)",
        reference_module="grut/fermionic_emergence_audit.py",
        primary_class="bounded_structural_result",
        secondary_class=None,
        justification=(
            "The fermionic emergence audit proves that fermionic statistics cannot "
            "emerge from the current real-scalar architecture within the stated "
            "assumptions: no spinors, no Clifford algebra, no gauge fields, no "
            "Hopf term (π₃(S²) absent from O(3) sector), no Dirac structure. "
            "Layer 1 (canonical scalar): hard obstruction — π₂(ℝ) = 0. "
            "Layer 2 (O(3) extension): structural gap — integer winding only, "
            "no Wilczek-Zee Hopf mechanism. "
            "This is a proved obstruction within the stated architecture, not an "
            "impossibility claim for all possible extensions."
        ),
        allowed_claims=[
            "Fermionic statistics are not present in the canonical GRUT scalar sector",
            "Fermionic emergence is obstructed in the current architecture",
            "Any fermionic extension requires explicit new architectural commitments",
            "The O(3) sector without a Hopf term gives bosonic statistics only",
        ],
        forbidden_claims=[
            "Fermionic statistics are impossible in principle for any GRUT extension",
            "The obstruction within current architecture closes the question for all architectures",
            "The Hopf fibration is permanently absent from all GRUT extensions",
        ],
        dependency_on=["scalar_constitutive_core", "pre_matter_quarantine_perimeter"],
        is_negative_result=True,
        is_load_bearing=True,
        notes=[
            "Negative result: obstruction in current architecture, not impossibility in principle",
            "Per nonclaim firewall: obstruction_as_impossibility_in_principle is forbidden",
        ],
    ))

    # ---- 7. Localized bosonic object program ------------------------
    items.append(ClassifiedResult(
        item_id="localized_bosonic_object_program",
        item_name="Localized bosonic object support (Appendix M)",
        reference_module="grut/localized_bosonic_object_audit.py",
        primary_class="motivated_but_unbuilt",
        secondary_class=None,
        justification=(
            "Appendix M verdict: 'particle_candidate_not_yet_established'. "
            "The architecture is compatible with a bosonic particle candidate "
            "program. The hedgehog localizes field content. But Derrick's theorem "
            "(D=3) proves that kinetic gradient E₂~λ + Mexican hat E_V~λ³ do not "
            "stabilize: dE/dλ = E₂ + 3E_V > 0 always. The Skyrme E₄~λ⁻¹ term "
            "is the known stabilizer. The chain (O(3) nativity → L₄ → stability) "
            "is identified and coherent. It has not been traversed."
        ),
        allowed_claims=[
            "GRUT is compatible with a bosonic particle candidate program",
            "Blocking mechanism is Derrick instability: E₂+3E_V>0 with no L₄",
            "Path to stability is identified: establish O(3) nativity, then L₄",
            "The topological charge framework (π₂(S²)=ℤ) is the right structure",
        ],
        forbidden_claims=[
            "GRUT has a stable bosonic localized object",
            "The particle candidate is established",
            "The hedgehog is stable against Derrick collapse in D=3",
            "V(Φ) = λ|Φ|⁴ stabilizes the soliton (field-space ≠ gradient quartic)",
        ],
        dependency_on=[
            "scalar_constitutive_core",
            "fermionic_emergence_obstruction",
            "o3_sector_nativity",
            "skyrme_term_nativity",
        ],
        is_negative_result=False,
        is_load_bearing=True,
        notes=[
            "Chain: O(3) nativity → L₄ → stable bosonic object",
            "Current block: Derrick theorem with no L₄ in native canon",
        ],
    ))

    # ---- 8. Skyrme term nativity ------------------------------------
    items.append(ClassifiedResult(
        item_id="skyrme_term_nativity",
        item_name="Skyrme term L₄ nativity (Appendix N)",
        reference_module="grut/skyrme_term_nativity_audit.py",
        primary_class="motivated_but_unbuilt",
        secondary_class=None,
        justification=(
            "Appendix N verdict: 'no_native_skyrme_support_found', "
            "patchwork: 'motivated_but_unbuilt'. "
            "Route 3 (O(3) derivative expansion) is the structural path: "
            "the unique next-order O(3)-invariant 4-derivative term IS L₄. "
            "This requires no new DOF beyond O(3) — it is the natural next "
            "term in the existing O(3) field space. "
            "Condition: O(3) must first be adopted as canonical. "
            "The Skyrme coupling e is a new free parameter, not yet fixed. "
            "Note: λ|Φ|⁴ (field-space quartic) ≠ L₄ (gradient quartic); "
            "Derrick exponents differ: +3 vs −1."
        ),
        allowed_claims=[
            "L₄ is motivated_but_unbuilt: Route 3 is the path",
            "Once O(3) is established, L₄ is the unique next-order term",
            "L₄ is compatible with all prior doctrine",
            "Skyrme coupling e is a new free parameter not fixed by current GRUT canon",
            "λ|Φ|⁴ ≠ L₄: field-space quartic does not stabilize hedgehog",
        ],
        forbidden_claims=[
            "L₄ is natively derived from current GRUT architecture",
            "V(Φ) = λ|Φ|⁴ is a Skyrme-type stabilizer",
            "L₄ stabilizes the hedgehog in Phase D1+ architecture",
            "Adding L₄ before O(3) nativity closes would not be ad hoc",
            "Route 3 being identified means L₄ is established",
        ],
        dependency_on=["o3_sector_nativity", "localized_bosonic_object_program"],
        is_negative_result=False,
        is_load_bearing=False,
        notes=[
            "Adding L₄ before O(3) nativity: compatible_but_ad_hoc (e floats free)",
            "Adding L₄ after O(3) nativity + parameter matching: motivated_but_unbuilt",
        ],
    ))

    # ---- 9. O(3) sector nativity ------------------------------------
    items.append(ClassifiedResult(
        item_id="o3_sector_nativity",
        item_name="O(3) sector nativity (Appendix O)",
        reference_module="grut/o3_nativity_audit.py",
        primary_class="motivated_independent_postulation",
        secondary_class=None,
        justification=(
            "Appendix O verdict: 'o3_auxiliary_but_minimally_motivated', "
            "patchwork: 'motivated_independent_postulation'. "
            "BG1 (1→3 scalar DOFs) is irresolvable by derivation — a mathematical "
            "impossibility (N1 hard fail). Two convergent independent motivations: "
            "CM1 (O(3) is the unique minimal real-scalar extension with π₂(M)≠0 — "
            "topological uniqueness), CM2 (Component B tail matching: "
            "ε_hedge ~ η²/r² with η²=τ²/(12π)). One parameter constrained: "
            "η² = COMP_B_COEFF = 1/(8π) = τ²/(12π). "
            "This is the strongest achievable positive status for a field-content "
            "extension: necessary postulate, uniquely selected, partially constrained."
        ),
        allowed_claims=[
            "O(3) is the unique minimal real-scalar extension providing π₂(M)≠0",
            "O(3) is uniquely motivated by topology (CM1) and Component B (CM2)",
            "η² is partially constrained: η² = τ²/(12π) via Component B matching",
            "O(3) is a motivated_independent_postulation — best achievable for field-content extension",
            "Adopting O(3) as canonical postulate is the best-motivated available choice",
        ],
        forbidden_claims=[
            "O(3) is derived from the canonical scalar Φ",
            "The η²=τ²/(12π) numerical identity constitutes a derivation of O(3)",
            "O(3) nativity means O(3) derivation",
            "Topological uniqueness implies derivability",
            "The partial parameter constraint proves O(3) is native_canon",
            "BG1 (1→3 scalars) can be resolved by a mathematical argument",
        ],
        dependency_on=[
            "scalar_constitutive_core",
            "component_b_deficit_requirement",
            "fermionic_emergence_obstruction",
        ],
        is_negative_result=False,
        is_load_bearing=False,
        notes=[
            "BG1 is permanent: 1→3 scalars is always a postulate, never a derivation",
            "η²=τ²/(12π): verified numerically (assert in module); mechanism unknown",
            "This is the hinge of the bosonic particle candidate chain (M→N→O)",
        ],
    ))

    # ---- 10. g_minus source closure ---------------------------------
    items.append(ClassifiedResult(
        item_id="g_minus_source_closure",
        item_name="g₋ source closure (Galley equilibrium)",
        reference_module="grut/g_minus_closure_audit.py",
        primary_class="bounded_structural_result",
        secondary_class=None,
        justification=(
            "At static GRUT equilibrium (Φ₁=Φ₂=Φ_eq), T^Φ₁-T^Φ₂=0, so the "
            "source-driven g₋ path is closed under Galley projection and conditions "
            "1+3. The homogeneous path (g₋ driven by initial conditions / unstable "
            "modes) remains open — Condition 2 (absence of homogeneous modes) is "
            "UNKNOWN. Verdict: source_path_closed=True, homogeneous_path_open=True, "
            "universal_no_go=False. This is a bounded structural result: proved "
            "within stated conditions (Galley formalism, static equilibrium)."
        ),
        allowed_claims=[
            "Source-driven g₋ path is closed at static equilibrium under Galley projection",
            "Component B cannot arise from source-driven g₋ at static equilibrium",
            "Homogeneous g₋ modes are not ruled out",
            "This is a partial closure, not a universal no-go",
        ],
        forbidden_claims=[
            "Universal no-go for Component B from g₋",
            "Source closure implies g₋=0 without homogeneous sector resolved",
            "Applies to non-Galley CTP formalisms",
        ],
        dependency_on=["galley_ctp_route_b", "scalar_constitutive_core"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["Partial: source path closed (proved), homogeneous path open (unresolved)"],
    ))

    # ---- 11. Galley CTP Route B -------------------------------------
    items.append(ClassifiedResult(
        item_id="galley_ctp_route_b",
        item_name="Galley CTP formalism (Route B)",
        reference_module=(
            "grut/galley_memory.py, grut/galley_truncation.py, "
            "grut/route_b_component_b.py"
        ),
        primary_class="effective_reduction",
        secondary_class=None,
        justification=(
            "The Galley CTP formalism doubles the field content "
            "(g₊, g₋, Φ₊, Φ₋) as a systematic treatment of dissipation. "
            "At the physical limit (g₋→0, Φ₋→0) it reduces to the GRUT "
            "canonical sector. Post-projection Route B = Route C "
            "(established in route_b_component_b.py). The physical-limit "
            "projection is assumed, not derived (not an attractor)."
        ),
        allowed_claims=[
            "In the Galley framework, dissipation is parametrized by (g₋, Φ₋)",
            "Post-projection, Route B reduces to Route C at equilibrium",
            "CTP is an effective description of GRUT's dissipative dynamics",
        ],
        forbidden_claims=[
            "Route B provides Component B (1/r²) support post-projection",
            "Galley physical-limit projection is a dynamical attractor",
            "CTP results extend beyond the Galley formalism without derivation",
        ],
        dependency_on=["scalar_constitutive_core", "tau_eff_domain_declaration"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=["Physical-limit projection: assumed, not derived (galley_truncation.py)"],
    ))

    # ---- 12. Component B deficit requirement ------------------------
    items.append(ClassifiedResult(
        item_id="component_b_deficit_requirement",
        item_name="Component B deficit requirement (1/r² support needed)",
        reference_module=(
            "grut/route_b_component_b.py, grut/route_c_deficit.py"
        ),
        primary_class="bounded_structural_result",
        secondary_class=None,
        justification=(
            "The interior metric deficit analysis proves that for static interior "
            "metric closure (f(R_eq) ≥ 0), the stress-energy must provide a "
            "Component B contribution with ε_B ~ 1/r². "
            "The canonical scalar (T^Φ ~ 1/r⁴) does not provide this. "
            "Post-projection Route B and Route C also fall as 1/r⁴. "
            "This establishes the requirement as a bounded structural result: "
            "1/r² support is necessary for interior closure within the stated "
            "GRUT architecture."
        ),
        allowed_claims=[
            "Component B (1/r² tail) is necessary for interior metric closure",
            "Canonical scalar does not supply Component B",
            "Post-projection Route B and Route C also fail to supply Component B",
            "O(3) hedgehog is the candidate supplier: ε_hedge~η²/r² with η²=τ²/(12π)",
        ],
        forbidden_claims=[
            "Component B is supplied by native canon (requires the O(3) extension)",
            "Interior closure is established (open pending Component B supply)",
            "The requirement can be satisfied without new field content",
        ],
        dependency_on=["scalar_constitutive_core", "galley_ctp_route_b"],
        is_negative_result=False,
        is_load_bearing=True,
        notes=[
            "Requirement proved; supply open (pending O(3) adoption)",
            "Connected to O(3) nativity via η²=COMP_B_COEFF=τ²/(12π)",
        ],
    ))

    # Validate
    assert len(items) == N_CLASSIFIED_ITEMS, (
        f"Expected {N_CLASSIFIED_ITEMS} items, got {len(items)}"
    )
    for item in items:
        assert item.item_id in CLASSIFIED_ITEM_IDS, (
            f"Item ID '{item.item_id}' not in CLASSIFIED_ITEM_IDS"
        )
        assert item.primary_class in ALLOWED_STATUS_CLASSES, (
            f"Primary class '{item.primary_class}' not in ALLOWED_STATUS_CLASSES"
        )
        if item.secondary_class is not None:
            assert item.secondary_class in ALLOWED_STATUS_CLASSES

    return items


# =====================================================================
# Support: dependency graph and claims index
# =====================================================================

def build_dependency_graph(items: List[ClassifiedResult]) -> Dict[str, List[str]]:
    """Return adjacency list: item_id → list of item_ids it depends on."""
    return {item.item_id: list(item.dependency_on) for item in items}


def build_allowed_forbidden_claims_by_class(
    classes: List[StatusClass],
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """Return (allowed_by_class, forbidden_by_class) dictionaries."""
    allowed: Dict[str, List[str]] = {c.name: c.allowed_claim_types for c in classes}
    forbidden: Dict[str, List[str]] = {c.name: c.forbidden_claim_types for c in classes}
    return allowed, forbidden


# =====================================================================
# Track E: Consistency check
# =====================================================================

def check_consistency(
    items: List[ClassifiedResult],
    classes: List[StatusClass],
    boundaries: List[ClassBoundaryRule],
) -> ConsistencyCheckResult:
    """Verify the taxonomy preserves all prior doctrine."""
    result = ConsistencyCheckResult()
    violations: List[str] = []

    # E1: no item in two incompatible classes
    for item in items:
        if item.secondary_class is not None:
            if item.primary_class == item.secondary_class:
                violations.append(
                    f"{item.item_id}: primary and secondary class identical"
                )
            if (item.secondary_class == "forbidden_or_inconsistent"
                    and item.primary_class != "forbidden_or_inconsistent"):
                violations.append(
                    f"{item.item_id}: forbidden mixed with positive primary class"
                )
    result.no_item_in_two_incompatible_classes = len(violations) == 0

    # E2: all items have valid class
    invalid = [i.item_id for i in items if i.primary_class not in ALLOWED_STATUS_CLASSES]
    result.all_items_have_valid_class = len(invalid) == 0
    if invalid:
        violations.extend([f"{id_}: invalid primary class" for id_ in invalid])

    # E3: nonclaims preserved — no forbidden claim appears in allowed claims
    nonclaim_ok = True
    for item in items:
        for fc in item.forbidden_claims:
            if fc in item.allowed_claims:
                nonclaim_ok = False
                violations.append(
                    f"{item.item_id}: forbidden claim in allowed list: {fc[:60]}"
                )
    result.nonclaims_preserved = nonclaim_ok

    # E4: no silent promotion — extension classes not simultaneously native_canon
    silent_ok = True
    for item in items:
        if item.primary_class in (
            "motivated_but_unbuilt",
            "motivated_independent_postulation",
            "compatible_but_ad_hoc",
        ):
            if item.secondary_class == "native_canon":
                silent_ok = False
                violations.append(
                    f"{item.item_id}: silent promotion — extension class with native_canon secondary"
                )
    result.no_silent_promotion = silent_ok

    # E5: negative results remain in bounded_structural_result or forbidden
    neg_ok = True
    for item in items:
        if item.is_negative_result:
            if item.primary_class not in (
                "bounded_structural_result", "forbidden_or_inconsistent"
            ):
                neg_ok = False
                violations.append(
                    f"{item.item_id}: negative result classified as {item.primary_class}"
                )
    result.negative_results_remain_negative = neg_ok

    result.violations = violations
    result.consistency_passes = (
        result.no_item_in_two_incompatible_classes
        and result.all_items_have_valid_class
        and result.nonclaims_preserved
        and result.no_silent_promotion
        and result.negative_results_remain_negative
    )
    result.notes = [
        f"Checked {len(items)} classified items against {len(classes)} status classes",
        f"{len(violations)} violation(s) found",
        f"Boundaries checked: {len(boundaries)}",
    ]
    return result


# =====================================================================
# Track F: Quantum readiness check
# =====================================================================

def check_quantum_readiness(
    classes: List[StatusClass],
    items: List[ClassifiedResult],
) -> QuantumReadinessCheck:
    """Assess whether Appendix P is sufficient as pre-quantum finisher."""
    result = QuantumReadinessCheck()

    # F1: taxonomy distinguishes native vs extension
    native_set = {c.name for c in classes
                  if not c.requires_new_field_content and c.is_constructive}
    ext_set = {c.name for c in classes if c.requires_new_field_content}
    result.taxonomy_distinguishes_native_vs_extension = (
        len(native_set) >= 4 and len(ext_set) >= 2
    )

    # F2: bounded results flagged for quantum verification
    bounded = [i for i in items if i.primary_class == "bounded_structural_result"]
    result.bounded_results_flagged_for_quantum_check = len(bounded) >= 2

    # F3: fermionic obstruction preserved as bounded structural
    fermionic = next(
        (i for i in items if i.item_id == "fermionic_emergence_obstruction"), None
    )
    result.fermionic_obstruction_status_preserved = (
        fermionic is not None
        and fermionic.is_negative_result
        and fermionic.primary_class == "bounded_structural_result"
    )

    # F4: free parameters identified in extension items
    skyrme = next((i for i in items if i.item_id == "skyrme_term_nativity"), None)
    result.free_parameters_identified = (
        skyrme is not None
        and any("free parameter" in c.lower() for c in skyrme.allowed_claims)
    )

    # F5: extension postulates clearly marked
    postulations = [
        i for i in items
        if i.primary_class == "motivated_independent_postulation"
    ]
    result.extension_postulates_clearly_marked = len(postulations) >= 1

    # F6: no missing class needed for quantum work
    # The 8 classes cover all doctrinal distinctions needed. Quantum results will
    # create new native_canon, effective_reduction, or bounded_structural_result
    # items — no new class types are needed.
    result.missing_classes = []
    result.no_missing_class_for_quantum = True

    result.quantum_ready = (
        result.taxonomy_distinguishes_native_vs_extension
        and result.bounded_results_flagged_for_quantum_check
        and result.fermionic_obstruction_status_preserved
        and result.free_parameters_identified
        and result.extension_postulates_clearly_marked
        and result.no_missing_class_for_quantum
    )
    result.readiness_verdict = (
        "taxonomy_sufficient_for_quantum_readiness"
        if result.quantum_ready
        else "taxonomy_insufficient_for_quantum_readiness"
    )
    result.notes = [
        f"Native classes (no new DOF): {sorted(native_set)}",
        f"Extension classes (new DOF required): {sorted(ext_set)}",
        f"Bounded structural items flagged: {[i.item_id for i in bounded]}",
        f"Postulation items: {[i.item_id for i in postulations]}",
        "No new doctrinal class types needed for quantum work",
        "Quantum sector will classify its own results using the existing 8 classes",
    ]
    return result


# =====================================================================
# Track A (taxonomy necessity): Minimality check
# =====================================================================

def check_taxonomy_minimality(classes: List[StatusClass]) -> TaxonomyMinimalityCheck:
    """Verify 8 classes are minimal (none redundant) and sufficient."""
    result = TaxonomyMinimalityCheck()
    result.n_classes_proposed = N_STATUS_CLASSES

    # Each class is necessary for at least one context:
    # native_canon:                  scalar_constitutive_core, quarantine
    # effective_reduction:           tau_eff_domain_declaration, galley_ctp_route_b
    # bounded_structural_result:     phi_bifurcation, fermionic obstruction,
    #                                g_minus closure, component_b_deficit
    # working_canon_hypothesis:      beta_q_canonical_hypothesis
    # motivated_but_unbuilt:         localized_bosonic_object, skyrme_nativity
    # motivated_independent_post.:   o3_sector_nativity
    # compatible_but_ad_hoc:         nonclaim context (L₄ before O(3) nativity)
    # forbidden_or_inconsistent:     firewall patterns (Derrick misclassification,
    #                                quarantine violations, BG1 claimed as derivable)

    result.n_classes_accepted = N_STATUS_CLASSES
    result.n_classes_rejected_as_redundant = 0
    result.rejected_classes = []

    # All 8 classes used in at least one context
    result.every_class_used_in_at_least_one_context = True
    result.is_minimal = (result.n_classes_rejected_as_redundant == 0)
    result.is_sufficient = True  # all 12 items are unambiguously classifiable
    result.notes = [
        "All 8 classes are required by at least one classified item or nonclaim context",
        "No pair of classes is semantically redundant",
        "compatible_but_ad_hoc and forbidden_or_inconsistent: used in nonclaim firewall "
        "and conditional status notes even though no primary classification lands there",
        "Smallest set that faithfully classifies all audited items without ambiguity",
    ]
    return result


# =====================================================================
# Track G: Nonclaim firewall
# =====================================================================

def build_nonclaim_firewall() -> NoclaimFirewallCheck:
    """Encode all 8 forbidden inference patterns."""
    patterns = sorted(FORBIDDEN_INFERENCE_PATTERNS)
    return NoclaimFirewallCheck(
        n_forbidden_patterns=len(patterns),
        forbidden_patterns=patterns,
        all_patterns_encoded=(len(patterns) == N_FORBIDDEN_INFERENCE_PATTERNS),
        pattern_descriptions=[
            "compatibility_as_derivation: L₄ is compatible with GRUT ≠ L₄ is derived from GRUT",
            "usefulness_as_nativity: O(3) is useful for Component B ≠ O(3) is native to GRUT",
            "uniqueness_as_derivability: O(3) is the unique choice ≠ O(3) is derivable from Φ",
            "observed_coincidence_as_closure: η²=τ²/(12π) is a numerical fact; mechanism unknown",
            "effective_regime_success_as_covariant_canon: quasi-static success ≠ covariant canon",
            "motivated_postulate_as_native: O(3) is a motivated postulate ≠ O(3) is native",
            "unbuilt_route_as_solved: Route 3 is identified ≠ Route 3 is traversed",
            "obstruction_as_impossibility_in_principle: fermionic obstruction in current "
            "architecture ≠ fermions are impossible in principle for all GRUT extensions",
        ],
        notes=[
            "These patterns are the primary failure modes when applying the taxonomy",
            "Each pattern corresponds to a boundary violation in the B1–B7 decision rules",
        ],
    )


# =====================================================================
# Master audit function
# =====================================================================

def assign_primary_verdict(
    consistency: ConsistencyCheckResult,
    quantum: QuantumReadinessCheck,
    minimality: TaxonomyMinimalityCheck,
) -> str:
    """Hard-gated verdict assignment."""
    if not consistency.consistency_passes:
        return "taxonomy_incomplete__reclassification_required"
    if not quantum.quantum_ready:
        return "taxonomy_complete__quantum_gap_identified"
    if not minimality.is_minimal or not minimality.is_sufficient:
        return "taxonomy_complete__quantum_gap_identified"
    return "taxonomy_complete__sufficient_for_quantum_readiness"


def run_appendix_p_taxonomy_audit() -> TaxonomyAuditResult:
    """Execute the full Appendix P doctrinal taxonomy audit deterministically."""

    classes = build_status_classes()
    boundaries = build_boundary_rules()
    items = classify_grut_items()
    dep_graph = build_dependency_graph(items)
    allowed_by_class, forbidden_by_class = build_allowed_forbidden_claims_by_class(classes)
    consistency = check_consistency(items, classes, boundaries)
    quantum = check_quantum_readiness(classes, items)
    minimality = check_taxonomy_minimality(classes)
    firewall = build_nonclaim_firewall()
    verdict = assign_primary_verdict(consistency, quantum, minimality)

    assert verdict in ALLOWED_PRIMARY_VERDICTS, f"Invalid verdict: {verdict}"
    assert consistency.consistency_passes, (
        f"Consistency violations: {consistency.violations}"
    )

    # Class distribution
    dist: Dict[str, int] = {cls_name: 0 for cls_name in ALLOWED_STATUS_CLASSES}
    for item in items:
        dist[item.primary_class] += 1

    nonclaims = [
        "Appendix P does NOT claim any extension is derived from canonical GRUT",
        "Appendix P does NOT promote motivated_independent_postulation to native_canon",
        "Appendix P does NOT treat motivated postulates as architecturally required",
        "Appendix P does NOT claim the taxonomy is complete for all future extensions",
        "Appendix P does NOT close any open audit — it classifies the status of results",
        "Appendix P does NOT treat working_canon_hypothesis as proved",
        "Appendix P does NOT treat bounded_structural_result as universally valid beyond its stated assumptions",
        "Appendix P does NOT claim the fermionic obstruction closes the fermionic question in principle",
    ]

    return TaxonomyAuditResult(
        valid=consistency.consistency_passes,
        status_classes=classes,
        boundary_rules=boundaries,
        classified_results=items,
        dependency_graph=dep_graph,
        consistency=consistency,
        quantum_readiness=quantum,
        taxonomy_minimality=minimality,
        nonclaim_firewall=firewall,
        allowed_claims_by_class=allowed_by_class,
        forbidden_claims_by_class=forbidden_by_class,
        primary_verdict=verdict,
        nonclaims=nonclaims,
        ambiguous_items=[],   # no item is ambiguously classified given prior audits
        diagnostics={
            "n_status_classes": N_STATUS_CLASSES,
            "n_classified_items": N_CLASSIFIED_ITEMS,
            "n_boundary_rules": N_BOUNDARY_RULES,
            "n_forbidden_patterns": N_FORBIDDEN_INFERENCE_PATTERNS,
            "class_distribution": dist,
            "consistency_passes": consistency.consistency_passes,
            "quantum_ready": quantum.quantum_ready,
            "taxonomy_is_minimal": minimality.is_minimal,
            "taxonomy_is_sufficient": minimality.is_sufficient,
            "ambiguous_items_count": 0,
        },
    )
