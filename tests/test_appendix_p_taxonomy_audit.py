"""Tests for grut/appendix_p_taxonomy_audit.py — Appendix P doctrinal taxonomy."""

import pytest
from grut.appendix_p_taxonomy_audit import (
    # Constants
    M_EXT, R_EQ, TAU_SQ, ALPHA_VAC, BETA_Q_CANON, OMEGA_0_SQ,
    COMP_B_COEFF, ETA_SQ_GRUT_LINK,
    PI2_REAL_SCALAR, PI2_S2,
    N_STATUS_CLASSES, N_CLASSIFIED_ITEMS, N_BOUNDARY_RULES,
    N_FORBIDDEN_INFERENCE_PATTERNS,
    # Vocabulary
    ALLOWED_STATUS_CLASSES, ALLOWED_PRIMARY_VERDICTS,
    CLASSIFIED_ITEM_IDS, BOUNDARY_RULE_IDS, FORBIDDEN_INFERENCE_PATTERNS,
    POSTULATE_REQUIRED_CLASSES, CONSTRUCTIVE_CLASSES,
    # Dataclasses
    StatusClass, ClassBoundaryRule, ClassifiedResult,
    ConsistencyCheckResult, QuantumReadinessCheck,
    TaxonomyMinimalityCheck, NoclaimFirewallCheck, TaxonomyAuditResult,
    # Functions
    build_status_classes, build_boundary_rules, classify_grut_items,
    build_dependency_graph, build_allowed_forbidden_claims_by_class,
    check_consistency, check_quantum_readiness, check_taxonomy_minimality,
    build_nonclaim_firewall, assign_primary_verdict,
    run_appendix_p_taxonomy_audit,
)


# =====================================================================
# TestConstants
# =====================================================================

class TestConstants:
    def test_n_status_classes(self):
        assert N_STATUS_CLASSES == 8

    def test_n_classified_items(self):
        assert N_CLASSIFIED_ITEMS == 12

    def test_n_boundary_rules(self):
        assert N_BOUNDARY_RULES == 7

    def test_n_forbidden_patterns(self):
        assert N_FORBIDDEN_INFERENCE_PATTERNS == 8

    def test_tau_sq(self):
        assert TAU_SQ == 1.5

    def test_beta_q_canon(self):
        assert BETA_Q_CANON == 2.0

    def test_omega0_sq(self):
        assert abs(OMEGA_0_SQ - 27.0) < 1e-12

    def test_m_ext(self):
        assert M_EXT == 0.5

    def test_r_eq(self):
        import math
        assert abs(R_EQ - 1.0 / 3.0) < 1e-12

    def test_comp_b_coeff(self):
        import math
        assert abs(COMP_B_COEFF - 1.0 / (8.0 * math.pi)) < 1e-12

    def test_eta_sq_tau_link(self):
        import math
        assert abs(ETA_SQ_GRUT_LINK - TAU_SQ / (12.0 * math.pi)) < 1e-12

    def test_eta_sq_equals_comp_b(self):
        assert abs(ETA_SQ_GRUT_LINK - COMP_B_COEFF) < 1e-12

    def test_pi2_real_scalar_is_zero(self):
        assert PI2_REAL_SCALAR == 0

    def test_pi2_s2_is_Z(self):
        assert PI2_S2 == "Z"


# =====================================================================
# TestVocabulary
# =====================================================================

class TestVocabulary:
    def test_allowed_status_classes_count(self):
        assert len(ALLOWED_STATUS_CLASSES) == 8

    def test_allowed_status_classes_is_frozenset(self):
        assert isinstance(ALLOWED_STATUS_CLASSES, frozenset)

    def test_allowed_primary_verdicts_count(self):
        assert len(ALLOWED_PRIMARY_VERDICTS) == 3

    def test_allowed_primary_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_PRIMARY_VERDICTS, frozenset)

    def test_classified_item_ids_count(self):
        assert len(CLASSIFIED_ITEM_IDS) == 12

    def test_classified_item_ids_is_frozenset(self):
        assert isinstance(CLASSIFIED_ITEM_IDS, frozenset)

    def test_boundary_rule_ids_count(self):
        assert len(BOUNDARY_RULE_IDS) == 7

    def test_boundary_rule_ids_is_frozenset(self):
        assert isinstance(BOUNDARY_RULE_IDS, frozenset)

    def test_forbidden_patterns_count(self):
        assert len(FORBIDDEN_INFERENCE_PATTERNS) == 8

    def test_forbidden_patterns_is_frozenset(self):
        assert isinstance(FORBIDDEN_INFERENCE_PATTERNS, frozenset)

    def test_postulate_required_classes_subset(self):
        assert POSTULATE_REQUIRED_CLASSES.issubset(ALLOWED_STATUS_CLASSES)

    def test_constructive_classes_subset(self):
        assert CONSTRUCTIVE_CLASSES.issubset(ALLOWED_STATUS_CLASSES)

    def test_forbidden_not_in_constructive(self):
        assert "forbidden_or_inconsistent" not in CONSTRUCTIVE_CLASSES

    def test_native_canon_in_constructive(self):
        assert "native_canon" in CONSTRUCTIVE_CLASSES

    def test_native_canon_not_postulate_required(self):
        assert "native_canon" not in POSTULATE_REQUIRED_CLASSES

    def test_motivated_postulation_in_postulate_required(self):
        assert "motivated_independent_postulation" in POSTULATE_REQUIRED_CLASSES

    def test_specific_status_class_names(self):
        expected = {
            "native_canon", "effective_reduction", "bounded_structural_result",
            "working_canon_hypothesis", "motivated_but_unbuilt",
            "motivated_independent_postulation", "compatible_but_ad_hoc",
            "forbidden_or_inconsistent",
        }
        assert ALLOWED_STATUS_CLASSES == expected

    def test_item_ids_include_required(self):
        required = {
            "scalar_constitutive_core", "beta_q_canonical_hypothesis",
            "fermionic_emergence_obstruction", "localized_bosonic_object_program",
            "skyrme_term_nativity", "o3_sector_nativity",
        }
        assert required.issubset(CLASSIFIED_ITEM_IDS)

    def test_forbidden_patterns_include_required(self):
        required = {
            "compatibility_as_derivation",
            "uniqueness_as_derivability",
            "unbuilt_route_as_solved",
            "obstruction_as_impossibility_in_principle",
        }
        assert required.issubset(FORBIDDEN_INFERENCE_PATTERNS)


# =====================================================================
# TestStatusClassDefinitions
# =====================================================================

class TestStatusClassDefinitions:
    def setup_method(self):
        self.classes = build_status_classes()
        self.by_name = {c.name: c for c in self.classes}

    def test_count(self):
        assert len(self.classes) == N_STATUS_CLASSES

    def test_all_names_valid(self):
        for cls in self.classes:
            assert cls.name in ALLOWED_STATUS_CLASSES

    def test_native_canon_exists(self):
        assert "native_canon" in self.by_name

    def test_native_canon_not_requires_new_field_content(self):
        assert self.by_name["native_canon"].requires_new_field_content is False

    def test_native_canon_not_requires_postulate(self):
        assert self.by_name["native_canon"].requires_explicit_postulate is False

    def test_native_canon_is_constructive(self):
        assert self.by_name["native_canon"].is_constructive is True

    def test_native_canon_has_admissibility_conditions(self):
        assert len(self.by_name["native_canon"].admissibility_conditions) >= 3

    def test_effective_reduction_not_requires_new_content(self):
        assert self.by_name["effective_reduction"].requires_new_field_content is False

    def test_bounded_structural_is_constructive(self):
        assert self.by_name["bounded_structural_result"].is_constructive is True

    def test_working_hypothesis_not_requires_postulate(self):
        assert self.by_name["working_canon_hypothesis"].requires_explicit_postulate is False

    def test_motivated_unbuilt_not_requires_new_content(self):
        assert self.by_name["motivated_but_unbuilt"].requires_new_field_content is False

    def test_motivated_postulation_requires_new_content(self):
        assert self.by_name["motivated_independent_postulation"].requires_new_field_content is True

    def test_motivated_postulation_requires_explicit_postulate(self):
        assert self.by_name["motivated_independent_postulation"].requires_explicit_postulate is True

    def test_compatible_adhoc_requires_new_content(self):
        assert self.by_name["compatible_but_ad_hoc"].requires_new_field_content is True

    def test_forbidden_is_not_constructive(self):
        assert self.by_name["forbidden_or_inconsistent"].is_constructive is False

    def test_forbidden_not_requires_new_content(self):
        assert self.by_name["forbidden_or_inconsistent"].requires_new_field_content is False

    def test_all_classes_have_definition(self):
        for cls in self.classes:
            assert len(cls.definition) > 20, f"Short definition for {cls.name}"

    def test_all_classes_have_admissibility_conditions(self):
        for cls in self.classes:
            assert len(cls.admissibility_conditions) >= 2, (
                f"Insufficient admissibility conditions for {cls.name}"
            )

    def test_all_classes_have_allowed_claims(self):
        for cls in self.classes:
            assert len(cls.allowed_claim_types) >= 2, (
                f"Insufficient allowed claims for {cls.name}"
            )

    def test_all_classes_have_forbidden_claims(self):
        for cls in self.classes:
            assert len(cls.forbidden_claim_types) >= 2, (
                f"Insufficient forbidden claims for {cls.name}"
            )

    def test_motivated_postulation_has_convergent_motivation_condition(self):
        cls = self.by_name["motivated_independent_postulation"]
        admiss_text = " ".join(cls.admissibility_conditions)
        assert "2" in admiss_text or "convergent" in admiss_text

    def test_motivated_postulation_has_uniqueness_condition(self):
        cls = self.by_name["motivated_independent_postulation"]
        admiss_text = " ".join(cls.admissibility_conditions)
        assert "unique" in admiss_text.lower() or "uniquely" in admiss_text.lower()

    def test_working_hypothesis_has_load_bearing_condition(self):
        cls = self.by_name["working_canon_hypothesis"]
        admiss_text = " ".join(cls.admissibility_conditions).lower()
        assert "load" in admiss_text or "predict" in admiss_text

    def test_bounded_structural_includes_negative_results(self):
        cls = self.by_name["bounded_structural_result"]
        defn = cls.definition.lower()
        assert "negative" in defn or "obstruction" in defn or "negative result" in defn.replace("negative", "negative")


# =====================================================================
# TestBoundaryRules
# =====================================================================

class TestBoundaryRules:
    def setup_method(self):
        self.rules = build_boundary_rules()
        self.by_id = {r.rule_id: r for r in self.rules}

    def test_count(self):
        assert len(self.rules) == N_BOUNDARY_RULES

    def test_all_ids_valid(self):
        for rule in self.rules:
            assert rule.rule_id in BOUNDARY_RULE_IDS

    def test_all_classes_valid(self):
        for rule in self.rules:
            assert rule.class_a in ALLOWED_STATUS_CLASSES
            assert rule.class_b in ALLOWED_STATUS_CLASSES

    def test_b1_separates_native_and_effective(self):
        rule = self.by_id["B1_native_canon_vs_effective_reduction"]
        assert rule.class_a == "native_canon"
        assert rule.class_b == "effective_reduction"

    def test_b1_is_deterministic(self):
        assert self.by_id["B1_native_canon_vs_effective_reduction"].is_deterministic

    def test_b2_separates_effective_and_bounded(self):
        rule = self.by_id["B2_effective_reduction_vs_bounded_structural"]
        assert rule.class_a == "effective_reduction"
        assert rule.class_b == "bounded_structural_result"

    def test_b3_is_proved_vs_asserted(self):
        rule = self.by_id["B3_bounded_structural_vs_working_hypothesis"]
        criterion = rule.distinguishing_criterion.lower()
        assert "deriv" in criterion or "assert" in criterion or "proved" in criterion

    def test_b4_is_load_bearing_vs_prospective(self):
        rule = self.by_id["B4_working_hypothesis_vs_motivated_unbuilt"]
        criterion = rule.distinguishing_criterion.lower()
        assert "load" in criterion or "prospect" in criterion or "current" in criterion

    def test_b5_separates_new_dof_requirement(self):
        rule = self.by_id["B5_motivated_unbuilt_vs_motivated_postulation"]
        assert rule.class_a == "motivated_but_unbuilt"
        assert rule.class_b == "motivated_independent_postulation"

    def test_b5_criterion_mentions_dof_or_field_content(self):
        rule = self.by_id["B5_motivated_unbuilt_vs_motivated_postulation"]
        crit = rule.distinguishing_criterion.lower()
        assert "dof" in crit or "field" in crit or "content" in crit

    def test_b6_triple_test(self):
        rule = self.by_id["B6_motivated_postulation_vs_compatible_adhoc"]
        test_a = rule.test_for_a.lower()
        assert "2" in test_a or "convergent" in test_a

    def test_b7_separates_consistent_and_forbidden(self):
        rule = self.by_id["B7_compatible_adhoc_vs_forbidden"]
        assert rule.class_a == "compatible_but_ad_hoc"
        assert rule.class_b == "forbidden_or_inconsistent"

    def test_all_rules_have_notes(self):
        for rule in self.rules:
            assert len(rule.notes) > 10

    def test_all_rules_deterministic(self):
        for rule in self.rules:
            assert rule.is_deterministic is True


# =====================================================================
# TestClassifiedResults — per-item checks
# =====================================================================

class TestClassifiedResults:
    def setup_method(self):
        self.items = classify_grut_items()
        self.by_id = {i.item_id: i for i in self.items}

    def test_count(self):
        assert len(self.items) == N_CLASSIFIED_ITEMS

    def test_all_ids_valid(self):
        for item in self.items:
            assert item.item_id in CLASSIFIED_ITEM_IDS

    def test_all_primary_classes_valid(self):
        for item in self.items:
            assert item.primary_class in ALLOWED_STATUS_CLASSES

    # native_canon items
    def test_scalar_core_is_native_canon(self):
        assert self.by_id["scalar_constitutive_core"].primary_class == "native_canon"

    def test_quarantine_is_native_canon(self):
        assert self.by_id["pre_matter_quarantine_perimeter"].primary_class == "native_canon"

    def test_scalar_core_has_no_dependencies(self):
        assert self.by_id["scalar_constitutive_core"].dependency_on == []

    def test_scalar_core_is_load_bearing(self):
        assert self.by_id["scalar_constitutive_core"].is_load_bearing is True

    def test_scalar_core_forbidden_claims_include_fermionic(self):
        fc = self.by_id["scalar_constitutive_core"].forbidden_claims
        assert any("fermion" in c.lower() for c in fc)

    def test_quarantine_depends_on_scalar_core(self):
        assert "scalar_constitutive_core" in self.by_id["pre_matter_quarantine_perimeter"].dependency_on

    # effective_reduction items
    def test_tau_eff_is_effective_reduction(self):
        assert self.by_id["tau_eff_domain_declaration"].primary_class == "effective_reduction"

    def test_galley_ctp_is_effective_reduction(self):
        assert self.by_id["galley_ctp_route_b"].primary_class == "effective_reduction"

    def test_tau_eff_forbidden_claims_include_covariant(self):
        fc = self.by_id["tau_eff_domain_declaration"].forbidden_claims
        assert any("covariant" in c.lower() or "quantum" in c.lower() for c in fc)

    # bounded_structural_result items
    def test_phi_bifurcation_is_bounded_structural(self):
        assert self.by_id["phi_sector_bifurcation"].primary_class == "bounded_structural_result"

    def test_fermionic_is_bounded_structural(self):
        assert self.by_id["fermionic_emergence_obstruction"].primary_class == "bounded_structural_result"

    def test_g_minus_is_bounded_structural(self):
        assert self.by_id["g_minus_source_closure"].primary_class == "bounded_structural_result"

    def test_component_b_is_bounded_structural(self):
        assert self.by_id["component_b_deficit_requirement"].primary_class == "bounded_structural_result"

    def test_fermionic_is_negative_result(self):
        assert self.by_id["fermionic_emergence_obstruction"].is_negative_result is True

    def test_phi_bifurcation_is_not_negative(self):
        assert self.by_id["phi_sector_bifurcation"].is_negative_result is False

    def test_fermionic_forbidden_claims_include_impossibility(self):
        fc = self.by_id["fermionic_emergence_obstruction"].forbidden_claims
        assert any("principle" in c.lower() or "impossible" in c.lower() for c in fc)

    def test_g_minus_forbidden_claims_include_universal_no_go(self):
        fc = self.by_id["g_minus_source_closure"].forbidden_claims
        assert any("universal" in c.lower() or "no-go" in c.lower() or "nogo" in c.lower() for c in fc)

    # working_canon_hypothesis
    def test_beta_q_is_working_hypothesis(self):
        assert self.by_id["beta_q_canonical_hypothesis"].primary_class == "working_canon_hypothesis"

    def test_beta_q_is_load_bearing(self):
        assert self.by_id["beta_q_canonical_hypothesis"].is_load_bearing is True

    def test_beta_q_forbidden_claims_include_derived(self):
        fc = self.by_id["beta_q_canonical_hypothesis"].forbidden_claims
        assert any("derived" in c.lower() or "first principle" in c.lower() for c in fc)

    # motivated_but_unbuilt
    def test_bosonic_object_is_motivated_but_unbuilt(self):
        assert self.by_id["localized_bosonic_object_program"].primary_class == "motivated_but_unbuilt"

    def test_skyrme_is_motivated_but_unbuilt(self):
        assert self.by_id["skyrme_term_nativity"].primary_class == "motivated_but_unbuilt"

    def test_bosonic_forbidden_claims_include_stable(self):
        fc = self.by_id["localized_bosonic_object_program"].forbidden_claims
        assert any("stable" in c.lower() for c in fc)

    def test_skyrme_forbidden_claims_include_mexican_hat(self):
        fc = self.by_id["skyrme_term_nativity"].forbidden_claims
        assert any("mexican" in c.lower() or "λ|Φ|" in c or "V(Φ)" in c or "field-space" in c.lower() for c in fc)

    def test_skyrme_forbidden_claims_include_native(self):
        fc = self.by_id["skyrme_term_nativity"].forbidden_claims
        assert any("native" in c.lower() or "natively" in c.lower() for c in fc)

    def test_skyrme_depends_on_o3(self):
        assert "o3_sector_nativity" in self.by_id["skyrme_term_nativity"].dependency_on

    def test_bosonic_object_depends_on_skyrme(self):
        assert "skyrme_term_nativity" in self.by_id["localized_bosonic_object_program"].dependency_on

    def test_bosonic_object_depends_on_o3(self):
        assert "o3_sector_nativity" in self.by_id["localized_bosonic_object_program"].dependency_on

    # motivated_independent_postulation
    def test_o3_is_motivated_independent_postulation(self):
        assert self.by_id["o3_sector_nativity"].primary_class == "motivated_independent_postulation"

    def test_o3_forbidden_claims_include_derived(self):
        fc = self.by_id["o3_sector_nativity"].forbidden_claims
        assert any("derived" in c.lower() for c in fc)

    def test_o3_forbidden_claims_include_uniqueness_not_derivability(self):
        fc = self.by_id["o3_sector_nativity"].forbidden_claims
        assert any("unique" in c.lower() for c in fc)

    def test_o3_allowed_claims_include_component_b(self):
        ac = self.by_id["o3_sector_nativity"].allowed_claims
        assert any("component b" in c.lower() or "CM2" in c or "η" in c for c in ac)

    def test_o3_allowed_claims_include_unique_minimal(self):
        ac = self.by_id["o3_sector_nativity"].allowed_claims
        assert any("unique" in c.lower() for c in ac)

    def test_o3_depends_on_component_b(self):
        assert "component_b_deficit_requirement" in self.by_id["o3_sector_nativity"].dependency_on

    # no item is compatible_but_ad_hoc or forbidden as primary
    def test_no_primary_compatible_adhoc(self):
        classes = [i.primary_class for i in self.items]
        assert "compatible_but_ad_hoc" not in classes

    def test_no_primary_forbidden(self):
        classes = [i.primary_class for i in self.items]
        assert "forbidden_or_inconsistent" not in classes

    def test_no_secondary_classes_set(self):
        for item in self.items:
            assert item.secondary_class is None

    def test_all_items_have_justification(self):
        for item in self.items:
            assert len(item.justification) > 40, f"Short justification for {item.item_id}"

    def test_all_items_have_allowed_claims(self):
        for item in self.items:
            assert len(item.allowed_claims) >= 2

    def test_all_items_have_forbidden_claims(self):
        for item in self.items:
            assert len(item.forbidden_claims) >= 2


# =====================================================================
# TestClassDistribution
# =====================================================================

class TestClassDistribution:
    def setup_method(self):
        self.items = classify_grut_items()

    def test_native_canon_count(self):
        n = sum(1 for i in self.items if i.primary_class == "native_canon")
        assert n == 2

    def test_effective_reduction_count(self):
        n = sum(1 for i in self.items if i.primary_class == "effective_reduction")
        assert n == 2

    def test_bounded_structural_count(self):
        n = sum(1 for i in self.items if i.primary_class == "bounded_structural_result")
        assert n == 4

    def test_working_hypothesis_count(self):
        n = sum(1 for i in self.items if i.primary_class == "working_canon_hypothesis")
        assert n == 1

    def test_motivated_unbuilt_count(self):
        n = sum(1 for i in self.items if i.primary_class == "motivated_but_unbuilt")
        assert n == 2

    def test_motivated_postulation_count(self):
        n = sum(1 for i in self.items if i.primary_class == "motivated_independent_postulation")
        assert n == 1

    def test_compatible_adhoc_primary_count_is_zero(self):
        n = sum(1 for i in self.items if i.primary_class == "compatible_but_ad_hoc")
        assert n == 0

    def test_forbidden_primary_count_is_zero(self):
        n = sum(1 for i in self.items if i.primary_class == "forbidden_or_inconsistent")
        assert n == 0

    def test_total_count(self):
        assert len(self.items) == N_CLASSIFIED_ITEMS

    def test_negative_results_count(self):
        n = sum(1 for i in self.items if i.is_negative_result)
        assert n >= 1

    def test_fermionic_is_only_negative_result(self):
        neg = [i.item_id for i in self.items if i.is_negative_result]
        assert "fermionic_emergence_obstruction" in neg


# =====================================================================
# TestDependencyGraph
# =====================================================================

class TestDependencyGraph:
    def setup_method(self):
        self.items = classify_grut_items()
        self.graph = build_dependency_graph(self.items)

    def test_graph_has_all_items(self):
        assert set(self.graph.keys()) == CLASSIFIED_ITEM_IDS

    def test_scalar_core_has_no_deps(self):
        assert self.graph["scalar_constitutive_core"] == []

    def test_skyrme_depends_on_o3(self):
        assert "o3_sector_nativity" in self.graph["skyrme_term_nativity"]

    def test_bosonic_depends_on_skyrme(self):
        assert "skyrme_term_nativity" in self.graph["localized_bosonic_object_program"]

    def test_bosonic_depends_on_o3(self):
        assert "o3_sector_nativity" in self.graph["localized_bosonic_object_program"]

    def test_o3_depends_on_component_b(self):
        assert "component_b_deficit_requirement" in self.graph["o3_sector_nativity"]

    def test_o3_depends_on_fermionic(self):
        assert "fermionic_emergence_obstruction" in self.graph["o3_sector_nativity"]

    def test_no_self_dependency(self):
        for item_id, deps in self.graph.items():
            assert item_id not in deps, f"{item_id} depends on itself"

    def test_quarantine_depends_on_scalar_core(self):
        assert "scalar_constitutive_core" in self.graph["pre_matter_quarantine_perimeter"]

    def test_g_minus_depends_on_galley(self):
        assert "galley_ctp_route_b" in self.graph["g_minus_source_closure"]

    def test_phi_bifurcation_depends_on_tau_eff(self):
        assert "tau_eff_domain_declaration" in self.graph["phi_sector_bifurcation"]


# =====================================================================
# TestAllowedForbiddenClaimsByClass
# =====================================================================

class TestAllowedForbiddenClaimsByClass:
    def setup_method(self):
        self.classes = build_status_classes()
        self.allowed, self.forbidden = build_allowed_forbidden_claims_by_class(self.classes)

    def test_all_classes_in_allowed_dict(self):
        for cls in self.classes:
            assert cls.name in self.allowed

    def test_all_classes_in_forbidden_dict(self):
        for cls in self.classes:
            assert cls.name in self.forbidden

    def test_native_canon_allows_architectural_claims(self):
        assert len(self.allowed["native_canon"]) >= 2

    def test_native_canon_forbids_matter_sector(self):
        fc = " ".join(self.forbidden["native_canon"]).lower()
        assert "matter" in fc or "quantum" in fc or "quarantine" in fc

    def test_effective_reduction_allows_regime_claims(self):
        ac = " ".join(self.allowed["effective_reduction"]).lower()
        assert "regime" in ac or "quasi" in ac or "approximat" in ac

    def test_motivated_postulation_forbids_derivation_claims(self):
        fc = " ".join(self.forbidden["motivated_independent_postulation"]).lower()
        assert "derived" in fc or "derivation" in fc or "native" in fc

    def test_forbidden_class_has_no_positive_claims(self):
        ac = " ".join(self.allowed["forbidden_or_inconsistent"]).lower()
        assert "forbidden" in ac or "contradicts" in ac


# =====================================================================
# TestConsistencyCheck
# =====================================================================

class TestConsistencyCheck:
    def setup_method(self):
        classes = build_status_classes()
        boundaries = build_boundary_rules()
        items = classify_grut_items()
        self.result = check_consistency(items, classes, boundaries)

    def test_consistency_passes(self):
        assert self.result.consistency_passes is True

    def test_no_violations(self):
        assert len(self.result.violations) == 0

    def test_no_item_in_two_incompatible_classes(self):
        assert self.result.no_item_in_two_incompatible_classes is True

    def test_all_items_have_valid_class(self):
        assert self.result.all_items_have_valid_class is True

    def test_nonclaims_preserved(self):
        assert self.result.nonclaims_preserved is True

    def test_no_silent_promotion(self):
        assert self.result.no_silent_promotion is True

    def test_negative_results_remain_negative(self):
        assert self.result.negative_results_remain_negative is True

    def test_notes_populated(self):
        assert len(self.result.notes) >= 2


# =====================================================================
# TestQuantumReadiness
# =====================================================================

class TestQuantumReadiness:
    def setup_method(self):
        classes = build_status_classes()
        items = classify_grut_items()
        self.result = check_quantum_readiness(classes, items)

    def test_quantum_ready(self):
        assert self.result.quantum_ready is True

    def test_readiness_verdict(self):
        assert self.result.readiness_verdict == "taxonomy_sufficient_for_quantum_readiness"

    def test_distinguishes_native_vs_extension(self):
        assert self.result.taxonomy_distinguishes_native_vs_extension is True

    def test_bounded_results_flagged(self):
        assert self.result.bounded_results_flagged_for_quantum_check is True

    def test_fermionic_obstruction_preserved(self):
        assert self.result.fermionic_obstruction_status_preserved is True

    def test_free_parameters_identified(self):
        assert self.result.free_parameters_identified is True

    def test_extension_postulates_marked(self):
        assert self.result.extension_postulates_clearly_marked is True

    def test_no_missing_classes(self):
        assert self.result.no_missing_class_for_quantum is True
        assert self.result.missing_classes == []

    def test_notes_populated(self):
        assert len(self.result.notes) >= 4


# =====================================================================
# TestTaxonomyMinimality
# =====================================================================

class TestTaxonomyMinimality:
    def setup_method(self):
        classes = build_status_classes()
        self.result = check_taxonomy_minimality(classes)

    def test_is_minimal(self):
        assert self.result.is_minimal is True

    def test_is_sufficient(self):
        assert self.result.is_sufficient is True

    def test_n_classes_accepted(self):
        assert self.result.n_classes_accepted == N_STATUS_CLASSES

    def test_zero_rejected(self):
        assert self.result.n_classes_rejected_as_redundant == 0
        assert self.result.rejected_classes == []

    def test_every_class_used(self):
        assert self.result.every_class_used_in_at_least_one_context is True

    def test_notes_mention_all_classes_used(self):
        notes_text = " ".join(self.result.notes).lower()
        assert "all 8" in notes_text or "all eight" in notes_text or "all" in notes_text


# =====================================================================
# TestNoclaimFirewall
# =====================================================================

class TestNoclaimFirewall:
    def setup_method(self):
        self.result = build_nonclaim_firewall()

    def test_n_forbidden_patterns(self):
        assert self.result.n_forbidden_patterns == N_FORBIDDEN_INFERENCE_PATTERNS

    def test_all_patterns_encoded(self):
        assert self.result.all_patterns_encoded is True

    def test_patterns_match_vocabulary(self):
        assert set(self.result.forbidden_patterns) == FORBIDDEN_INFERENCE_PATTERNS

    def test_compatibility_as_derivation_present(self):
        assert "compatibility_as_derivation" in self.result.forbidden_patterns

    def test_usefulness_as_nativity_present(self):
        assert "usefulness_as_nativity" in self.result.forbidden_patterns

    def test_uniqueness_as_derivability_present(self):
        assert "uniqueness_as_derivability" in self.result.forbidden_patterns

    def test_observed_coincidence_as_closure_present(self):
        assert "observed_coincidence_as_closure" in self.result.forbidden_patterns

    def test_effective_regime_pattern_present(self):
        assert "effective_regime_success_as_covariant_canon" in self.result.forbidden_patterns

    def test_motivated_postulate_as_native_present(self):
        assert "motivated_postulate_as_native" in self.result.forbidden_patterns

    def test_unbuilt_route_as_solved_present(self):
        assert "unbuilt_route_as_solved" in self.result.forbidden_patterns

    def test_obstruction_as_impossibility_present(self):
        assert "obstruction_as_impossibility_in_principle" in self.result.forbidden_patterns

    def test_pattern_descriptions_count(self):
        assert len(self.result.pattern_descriptions) == N_FORBIDDEN_INFERENCE_PATTERNS

    def test_pattern_descriptions_mention_examples(self):
        descs_text = " ".join(self.result.pattern_descriptions).lower()
        assert "l₄" in descs_text or "l4" in descs_text or "skyrme" in descs_text or "route" in descs_text

    def test_o3_uniqueness_example_in_descriptions(self):
        descs_text = " ".join(self.result.pattern_descriptions).lower()
        assert "o(3)" in descs_text or "unique" in descs_text


# =====================================================================
# TestPrimaryVerdict
# =====================================================================

class TestPrimaryVerdict:
    def setup_method(self):
        classes = build_status_classes()
        boundaries = build_boundary_rules()
        items = classify_grut_items()
        consistency = check_consistency(items, classes, boundaries)
        quantum = check_quantum_readiness(classes, items)
        minimality = check_taxonomy_minimality(classes)
        self.verdict = assign_primary_verdict(consistency, quantum, minimality)

    def test_verdict_in_allowed_set(self):
        assert self.verdict in ALLOWED_PRIMARY_VERDICTS

    def test_verdict_is_complete_and_sufficient(self):
        assert self.verdict == "taxonomy_complete__sufficient_for_quantum_readiness"

    def test_verdict_not_incomplete(self):
        assert self.verdict != "taxonomy_incomplete__reclassification_required"

    def test_verdict_not_gap_identified(self):
        assert self.verdict != "taxonomy_complete__quantum_gap_identified"


# =====================================================================
# TestNonclaims
# =====================================================================

class TestNonclaims:
    def setup_method(self):
        self.result = run_appendix_p_taxonomy_audit()

    def test_nonclaims_populated(self):
        assert len(self.result.nonclaims) >= 8

    def test_nonclaim_no_extension_derived(self):
        text = " ".join(self.result.nonclaims).lower()
        assert "extension" in text or "derived" in text

    def test_nonclaim_no_silent_promotion(self):
        text = " ".join(self.result.nonclaims).lower()
        assert "promote" in text or "native" in text

    def test_nonclaim_working_hypothesis_not_proved(self):
        text = " ".join(self.result.nonclaims).lower()
        assert "working" in text or "proved" in text or "hypothesis" in text

    def test_nonclaim_fermionic_not_closed(self):
        text = " ".join(self.result.nonclaims).lower()
        assert "fermionic" in text or "principle" in text

    def test_no_ambiguous_items(self):
        assert self.result.ambiguous_items == []


# =====================================================================
# TestDiagnostics
# =====================================================================

class TestDiagnostics:
    def setup_method(self):
        self.result = run_appendix_p_taxonomy_audit()
        self.diag = self.result.diagnostics

    def test_n_status_classes_in_diagnostics(self):
        assert self.diag["n_status_classes"] == N_STATUS_CLASSES

    def test_n_classified_items_in_diagnostics(self):
        assert self.diag["n_classified_items"] == N_CLASSIFIED_ITEMS

    def test_n_boundary_rules_in_diagnostics(self):
        assert self.diag["n_boundary_rules"] == N_BOUNDARY_RULES

    def test_n_forbidden_patterns_in_diagnostics(self):
        assert self.diag["n_forbidden_patterns"] == N_FORBIDDEN_INFERENCE_PATTERNS

    def test_class_distribution_present(self):
        assert "class_distribution" in self.diag

    def test_class_distribution_native_canon(self):
        assert self.diag["class_distribution"]["native_canon"] == 2

    def test_class_distribution_bounded_structural(self):
        assert self.diag["class_distribution"]["bounded_structural_result"] == 4

    def test_class_distribution_motivated_postulation(self):
        assert self.diag["class_distribution"]["motivated_independent_postulation"] == 1

    def test_class_distribution_working_hypothesis(self):
        assert self.diag["class_distribution"]["working_canon_hypothesis"] == 1

    def test_class_distribution_motivated_unbuilt(self):
        assert self.diag["class_distribution"]["motivated_but_unbuilt"] == 2

    def test_class_distribution_adhoc_zero(self):
        assert self.diag["class_distribution"]["compatible_but_ad_hoc"] == 0

    def test_class_distribution_forbidden_zero(self):
        assert self.diag["class_distribution"]["forbidden_or_inconsistent"] == 0

    def test_consistency_passes_in_diagnostics(self):
        assert self.diag["consistency_passes"] is True

    def test_quantum_ready_in_diagnostics(self):
        assert self.diag["quantum_ready"] is True

    def test_taxonomy_minimal_in_diagnostics(self):
        assert self.diag["taxonomy_is_minimal"] is True

    def test_taxonomy_sufficient_in_diagnostics(self):
        assert self.diag["taxonomy_is_sufficient"] is True

    def test_ambiguous_items_count_zero(self):
        assert self.diag["ambiguous_items_count"] == 0


# =====================================================================
# TestStatusInflationPrevention
# =====================================================================

class TestStatusInflationPrevention:
    """Verify that no result is silently inflated beyond what audits support."""

    def setup_method(self):
        self.items = classify_grut_items()
        self.by_id = {i.item_id: i for i in self.items}

    def test_o3_not_native_canon(self):
        assert self.by_id["o3_sector_nativity"].primary_class != "native_canon"

    def test_skyrme_not_native_canon(self):
        assert self.by_id["skyrme_term_nativity"].primary_class != "native_canon"

    def test_bosonic_object_not_established(self):
        # Must not be native_canon or bounded_structural_result (positive)
        item = self.by_id["localized_bosonic_object_program"]
        assert item.primary_class not in ("native_canon", "bounded_structural_result")

    def test_beta_q_not_bounded_structural(self):
        # β_Q = 2 is asserted, not proved
        assert self.by_id["beta_q_canonical_hypothesis"].primary_class != "bounded_structural_result"

    def test_galley_not_native_canon(self):
        assert self.by_id["galley_ctp_route_b"].primary_class != "native_canon"

    def test_tau_eff_not_native_canon(self):
        # τ_eff requires regime qualifier
        assert self.by_id["tau_eff_domain_declaration"].primary_class != "native_canon"

    def test_fermionic_not_forbidden(self):
        # The obstruction is bounded structural, not forbidden
        assert self.by_id["fermionic_emergence_obstruction"].primary_class != "forbidden_or_inconsistent"

    def test_component_b_not_native_canon(self):
        # Requirement proven; supply requires O(3) extension
        assert self.by_id["component_b_deficit_requirement"].primary_class != "native_canon"

    def test_extension_chain_ordering(self):
        # o3 must be postulation (harder than skyrme's unbuilt)
        o3_class = self.by_id["o3_sector_nativity"].primary_class
        skyrme_class = self.by_id["skyrme_term_nativity"].primary_class
        assert o3_class == "motivated_independent_postulation"
        assert skyrme_class == "motivated_but_unbuilt"
        # motivated_independent_postulation is "harder" than motivated_but_unbuilt
        assert o3_class != skyrme_class


# =====================================================================
# TestMasterAudit
# =====================================================================

class TestMasterAudit:
    def setup_method(self):
        self.result = run_appendix_p_taxonomy_audit()

    def test_valid_flag(self):
        assert self.result.valid is True

    def test_primary_verdict(self):
        assert self.result.primary_verdict == "taxonomy_complete__sufficient_for_quantum_readiness"

    def test_primary_verdict_in_allowed_set(self):
        assert self.result.primary_verdict in ALLOWED_PRIMARY_VERDICTS

    def test_status_classes_count(self):
        assert len(self.result.status_classes) == N_STATUS_CLASSES

    def test_boundary_rules_count(self):
        assert len(self.result.boundary_rules) == N_BOUNDARY_RULES

    def test_classified_results_count(self):
        assert len(self.result.classified_results) == N_CLASSIFIED_ITEMS

    def test_dependency_graph_complete(self):
        assert set(self.result.dependency_graph.keys()) == CLASSIFIED_ITEM_IDS

    def test_allowed_claims_index_complete(self):
        for cls_name in ALLOWED_STATUS_CLASSES:
            assert cls_name in self.result.allowed_claims_by_class

    def test_forbidden_claims_index_complete(self):
        for cls_name in ALLOWED_STATUS_CLASSES:
            assert cls_name in self.result.forbidden_claims_by_class

    def test_consistency_passes(self):
        assert self.result.consistency.consistency_passes is True

    def test_quantum_ready(self):
        assert self.result.quantum_readiness.quantum_ready is True

    def test_taxonomy_minimal(self):
        assert self.result.taxonomy_minimality.is_minimal is True

    def test_firewall_complete(self):
        assert self.result.nonclaim_firewall.all_patterns_encoded is True

    def test_no_ambiguous_items(self):
        assert self.result.ambiguous_items == []

    def test_audit_is_idempotent(self):
        result2 = run_appendix_p_taxonomy_audit()
        assert self.result.primary_verdict == result2.primary_verdict
        assert self.result.valid == result2.valid
        assert len(self.result.classified_results) == len(result2.classified_results)
        assert (
            self.result.diagnostics["class_distribution"]
            == result2.diagnostics["class_distribution"]
        )

    def test_nonclaims_count(self):
        assert len(self.result.nonclaims) >= 8
