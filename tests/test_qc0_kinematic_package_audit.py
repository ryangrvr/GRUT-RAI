"""Tests for Appendix Q-C0 — Kinematic Package Completion Audit.

Covers all 10 audit tracks, 5 hard-gated verdicts, and the master
run_qc0_kinematic_package_audit() function. All tests are deterministic.

Target: ~140 tests.
"""

import pytest

from grut.qc0_kinematic_package_audit import (
    # Constants
    ALLOWED_PACKAGE_VERDICTS,
    ALLOWED_INNER_PRODUCT_VERDICTS,
    ALLOWED_POSITIVITY_VERDICTS,
    ALLOWED_GENERATOR_CLASS_VERDICTS,
    ALLOWED_READINESS_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_PACKAGE_ITEM_STATUSES,
    ALLOWED_OBSERVABLE_VERDICTS,
    N_PACKAGE_ITEMS,
    N_INNER_PRODUCT_CANDIDATES,
    N_INNER_PRODUCT_VIABLE,
    N_MINIMUM_PACKAGE_ELEMENTS,
    N_QC0_NONCLAIMS,
    N_ITEMS_ALREADY_PRESENT,
    N_ITEMS_PARTIALLY_PRESENT,
    N_ITEMS_ABSENT,
    N_ITEMS_OBSTRUCTED,
    N_ITEMS_EXTENSION_LEVEL,
    TAU_SQ,
    TAU,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    QC0_PACKAGE_VERDICT,
    QC0_INNER_PRODUCT_VERDICT,
    QC0_POSITIVITY_VERDICT,
    QC0_GENERATOR_CLASS_VERDICT,
    QC0_READINESS_VERDICT,
    QC0_OVERALL_APPENDIX_P_CLASS,
    QC0_MINIMUM_PACKAGE_ELEMENTS,
    QC0_NONCLAIMS,
    # Builder functions
    build_track_a_package_inventory,
    build_inner_product_candidate_ip1,
    build_inner_product_candidate_ip2,
    build_inner_product_candidate_ip3,
    build_inner_product_candidate_ip4,
    build_inner_product_candidate_ip5,
    build_track_b_inner_product,
    build_track_c_norm_positivity,
    build_track_d_state_space_topology,
    build_track_e_generator,
    build_track_f_observable,
    build_track_g_minimum_package,
    build_track_h_appendix_p,
    build_track_i_readiness,
    build_track_j_nonclaims,
    build_allowed_claims,
    build_forbidden_claims,
    # Master function
    run_qc0_kinematic_package_audit,
)
import math


# ================================================================
# TestQC0Constants — 18 tests
# ================================================================

class TestQC0Constants:
    def test_n_package_items(self):
        assert N_PACKAGE_ITEMS == 7

    def test_n_inner_product_candidates(self):
        assert N_INNER_PRODUCT_CANDIDATES == 5

    def test_n_inner_product_viable(self):
        assert N_INNER_PRODUCT_VIABLE == 1

    def test_n_minimum_package_elements(self):
        assert N_MINIMUM_PACKAGE_ELEMENTS == 3

    def test_n_qc0_nonclaims(self):
        assert N_QC0_NONCLAIMS == 8

    def test_n_items_already_present(self):
        assert N_ITEMS_ALREADY_PRESENT == 0

    def test_n_items_partially_present(self):
        assert N_ITEMS_PARTIALLY_PRESENT == 1

    def test_n_items_absent(self):
        assert N_ITEMS_ABSENT == 5

    def test_n_items_obstructed(self):
        assert N_ITEMS_OBSTRUCTED == 0

    def test_n_items_extension_level(self):
        assert N_ITEMS_EXTENSION_LEVEL == 1

    def test_item_counts_sum_to_n_package_items(self):
        total = (N_ITEMS_ALREADY_PRESENT + N_ITEMS_PARTIALLY_PRESENT
                 + N_ITEMS_ABSENT + N_ITEMS_OBSTRUCTED + N_ITEMS_EXTENSION_LEVEL)
        assert total == N_PACKAGE_ITEMS

    def test_tau_sq_canonical(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_tau_derived(self):
        assert TAU == pytest.approx(math.sqrt(1.5))

    def test_phi_minus_growth_rate_sign(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_package_verdict_in_allowed(self):
        assert QC0_PACKAGE_VERDICT in ALLOWED_PACKAGE_VERDICTS

    def test_inner_product_verdict_in_allowed(self):
        assert QC0_INNER_PRODUCT_VERDICT in ALLOWED_INNER_PRODUCT_VERDICTS

    def test_positivity_verdict_in_allowed(self):
        assert QC0_POSITIVITY_VERDICT in ALLOWED_POSITIVITY_VERDICTS

    def test_generator_class_verdict_in_allowed(self):
        assert QC0_GENERATOR_CLASS_VERDICT in ALLOWED_GENERATOR_CLASS_VERDICTS

    def test_readiness_verdict_in_allowed(self):
        assert QC0_READINESS_VERDICT in ALLOWED_READINESS_VERDICTS

    def test_overall_appendix_p_class_in_allowed(self):
        assert QC0_OVERALL_APPENDIX_P_CLASS in ALLOWED_APPENDIX_P_CLASSES

    def test_overall_appendix_p_class_is_mip(self):
        assert QC0_OVERALL_APPENDIX_P_CLASS == "motivated_independent_postulation"

    def test_minimum_package_elements_is_list_of_3(self):
        assert isinstance(QC0_MINIMUM_PACKAGE_ELEMENTS, list)
        assert len(QC0_MINIMUM_PACKAGE_ELEMENTS) == 3

    def test_nonclaims_list_length(self):
        assert len(QC0_NONCLAIMS) == N_QC0_NONCLAIMS

    def test_package_verdict_value(self):
        assert QC0_PACKAGE_VERDICT == "minimum_kinematic_package_identified"

    def test_inner_product_verdict_value(self):
        assert QC0_INNER_PRODUCT_VERDICT == "inner_product_motivated_independent_postulation"

    def test_positivity_verdict_value(self):
        assert QC0_POSITIVITY_VERDICT == "positivity_requires_postulate"

    def test_generator_class_verdict_value(self):
        assert QC0_GENERATOR_CLASS_VERDICT == "lindbladian_like_generator_kinematically_admissible"

    def test_readiness_verdict_value(self):
        assert QC0_READINESS_VERDICT == "ready_only_if_package_is_postulated"


# ================================================================
# TestTrackAPackageInventory — 22 tests
# ================================================================

class TestTrackAPackageInventory:
    def setup_method(self):
        self.inv = build_track_a_package_inventory()

    def test_n_items(self):
        assert self.inv.n_items == N_PACKAGE_ITEMS

    def test_n_items_len(self):
        assert len(self.inv.items) == N_PACKAGE_ITEMS

    def test_n_already_present(self):
        assert self.inv.n_already_present == 0

    def test_n_partially_present(self):
        assert self.inv.n_partially_present == 1

    def test_n_absent(self):
        assert self.inv.n_absent == 5

    def test_n_obstructed(self):
        assert self.inv.n_obstructed == 0

    def test_n_extension_level(self):
        assert self.inv.n_extension_level == 1

    def test_ki1_j_status(self):
        ki1 = next(it for it in self.inv.items if it.item_id == "KI1_complex_structure_j")
        assert ki1.status == "extension_level_only"

    def test_ki1_j_appendix_p(self):
        ki1 = next(it for it in self.inv.items if it.item_id == "KI1_complex_structure_j")
        assert ki1.appendix_p_class == "motivated_independent_postulation"

    def test_ki2_inner_product_status(self):
        ki2 = next(it for it in self.inv.items if it.item_id == "KI2_inner_product")
        assert ki2.status == "absent"

    def test_ki2_inner_product_appendix_p(self):
        ki2 = next(it for it in self.inv.items if it.item_id == "KI2_inner_product")
        assert ki2.appendix_p_class == "motivated_independent_postulation"

    def test_ki3_norm_status(self):
        ki3 = next(it for it in self.inv.items if it.item_id == "KI3_norm_normalization")
        assert ki3.status == "absent"

    def test_ki3_norm_appendix_p(self):
        ki3 = next(it for it in self.inv.items if it.item_id == "KI3_norm_normalization")
        assert ki3.appendix_p_class == "motivated_independent_postulation"

    def test_ki4_positivity_status(self):
        ki4 = next(it for it in self.inv.items if it.item_id == "KI4_positivity")
        assert ki4.status == "absent"

    def test_ki4_positivity_appendix_p(self):
        ki4 = next(it for it in self.inv.items if it.item_id == "KI4_positivity")
        assert ki4.appendix_p_class == "motivated_independent_postulation"

    def test_ki5_topology_status(self):
        ki5 = next(it for it in self.inv.items if it.item_id == "KI5_state_space_topology")
        assert ki5.status == "partially_present"

    def test_ki5_topology_appendix_p(self):
        ki5 = next(it for it in self.inv.items if it.item_id == "KI5_state_space_topology")
        assert ki5.appendix_p_class == "bounded_structural_result"

    def test_ki6_generator_status(self):
        ki6 = next(it for it in self.inv.items if it.item_id == "KI6_dynamics_generator")
        assert ki6.status == "absent"

    def test_ki6_generator_appendix_p(self):
        ki6 = next(it for it in self.inv.items if it.item_id == "KI6_dynamics_generator")
        assert ki6.appendix_p_class == "motivated_but_unbuilt"

    def test_ki7_observable_status(self):
        ki7 = next(it for it in self.inv.items if it.item_id == "KI7_observable_structure")
        assert ki7.status == "absent"

    def test_ki7_observable_appendix_p(self):
        ki7 = next(it for it in self.inv.items if it.item_id == "KI7_observable_structure")
        assert ki7.appendix_p_class == "compatible_but_ad_hoc"

    def test_all_statuses_valid(self):
        for item in self.inv.items:
            assert item.status in ALLOWED_PACKAGE_ITEM_STATUSES

    def test_all_appendix_p_classes_valid(self):
        for item in self.inv.items:
            assert item.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


# ================================================================
# TestTrackBCandidatesIndividual — 20 tests
# ================================================================

class TestTrackBCandidatesIndividual:
    def test_ip1_id(self):
        ip1 = build_inner_product_candidate_ip1()
        assert ip1.candidate_id == "IP1_constitutive_field_space"

    def test_ip1_not_viable(self):
        ip1 = build_inner_product_candidate_ip1()
        assert ip1.viable is False

    def test_ip1_classification_cah(self):
        ip1 = build_inner_product_candidate_ip1()
        assert ip1.classification == "compatible_but_ad_hoc"

    def test_ip1_rejection_reason_non_empty(self):
        ip1 = build_inner_product_candidate_ip1()
        assert ip1.rejection_reason is not None and len(ip1.rejection_reason) > 0

    def test_ip2_id(self):
        ip2 = build_inner_product_candidate_ip2()
        assert ip2.candidate_id == "IP2_ctp_doubled_field"

    def test_ip2_not_viable(self):
        ip2 = build_inner_product_candidate_ip2()
        assert ip2.viable is False

    def test_ip2_classification_foi(self):
        ip2 = build_inner_product_candidate_ip2()
        assert ip2.classification == "forbidden_or_inconsistent"

    def test_ip2_rejection_reason_mentions_ghost(self):
        ip2 = build_inner_product_candidate_ip2()
        assert "ghost" in ip2.rejection_reason.lower() or "grow" in ip2.rejection_reason.lower()

    def test_ip3_id(self):
        ip3 = build_inner_product_candidate_ip3()
        assert ip3.candidate_id == "IP3_o3_sector_induced"

    def test_ip3_not_viable(self):
        ip3 = build_inner_product_candidate_ip3()
        assert ip3.viable is False

    def test_ip3_classification_cah(self):
        ip3 = build_inner_product_candidate_ip3()
        assert ip3.classification == "compatible_but_ad_hoc"

    def test_ip4_id(self):
        ip4 = build_inner_product_candidate_ip4()
        assert ip4.candidate_id == "IP4_effective_open_system"

    def test_ip4_not_viable(self):
        ip4 = build_inner_product_candidate_ip4()
        assert ip4.viable is False

    def test_ip4_classification_cah(self):
        ip4 = build_inner_product_candidate_ip4()
        assert ip4.classification == "compatible_but_ad_hoc"

    def test_ip4_rejection_mentions_circular(self):
        ip4 = build_inner_product_candidate_ip4()
        assert "circular" in ip4.rejection_reason.lower()

    def test_ip5_id(self):
        ip5 = build_inner_product_candidate_ip5()
        assert ip5.candidate_id == "IP5_postulated_j_compatible"

    def test_ip5_viable(self):
        ip5 = build_inner_product_candidate_ip5()
        assert ip5.viable is True

    def test_ip5_classification_mip(self):
        ip5 = build_inner_product_candidate_ip5()
        assert ip5.classification == "motivated_independent_postulation"

    def test_ip5_no_rejection_reason(self):
        ip5 = build_inner_product_candidate_ip5()
        assert ip5.rejection_reason is None

    def test_only_ip5_is_viable(self):
        candidates = [
            build_inner_product_candidate_ip1(),
            build_inner_product_candidate_ip2(),
            build_inner_product_candidate_ip3(),
            build_inner_product_candidate_ip4(),
            build_inner_product_candidate_ip5(),
        ]
        viable = [c for c in candidates if c.viable]
        assert len(viable) == 1
        assert viable[0].candidate_id == "IP5_postulated_j_compatible"


# ================================================================
# TestTrackBInnerProductAudit — 10 tests
# ================================================================

class TestTrackBInnerProductAudit:
    def setup_method(self):
        self.audit = build_track_b_inner_product()

    def test_n_candidates(self):
        assert self.audit.n_candidates == N_INNER_PRODUCT_CANDIDATES

    def test_n_viable(self):
        assert self.audit.n_viable == N_INNER_PRODUCT_VIABLE

    def test_primary_candidate(self):
        assert self.audit.primary_candidate_id == "IP5_postulated_j_compatible"

    def test_inner_product_verdict(self):
        assert self.audit.inner_product_verdict == QC0_INNER_PRODUCT_VERDICT

    def test_real_bilinear_native(self):
        assert self.audit.real_bilinear_native is True

    def test_complex_inner_product_not_native(self):
        assert self.audit.complex_inner_product_native is False

    def test_candidates_len(self):
        assert len(self.audit.candidates) == N_INNER_PRODUCT_CANDIDATES

    def test_all_classifications_valid(self):
        for c in self.audit.candidates:
            assert c.classification in ALLOWED_APPENDIX_P_CLASSES

    def test_viable_count_matches(self):
        assert sum(1 for c in self.audit.candidates if c.viable) == self.audit.n_viable

    def test_verdict_in_allowed(self):
        assert self.audit.inner_product_verdict in ALLOWED_INNER_PRODUCT_VERDICTS


# ================================================================
# TestTrackCNormPositivity — 12 tests
# ================================================================

class TestTrackCNormPositivity:
    def setup_method(self):
        self.track_c = build_track_c_norm_positivity()

    def test_ghost_obstruction_inherited(self):
        assert self.track_c.ghost_obstruction_inherited is True

    def test_phi_minus_growth_rate_sign(self):
        assert self.track_c.phi_minus_growth_rate_sign == +1

    def test_ctp_based_norm_ghost_contaminated(self):
        assert self.track_c.ctp_based_norm_ghost_contaminated is True

    def test_ctp_based_norm_not_valid(self):
        assert self.track_c.ctp_based_norm_valid is False

    def test_j_compatible_norm_available_with_postulate(self):
        assert self.track_c.j_compatible_norm_available_with_postulate is True

    def test_positivity_not_native(self):
        assert self.track_c.positivity_native is False

    def test_positivity_not_effectively_recoverable(self):
        assert self.track_c.positivity_effectively_recoverable is False

    def test_positivity_requires_postulate(self):
        assert self.track_c.positivity_requires_postulate is True

    def test_positivity_open_system_compatible(self):
        assert self.track_c.positivity_open_system_compatible is True

    def test_positivity_verdict(self):
        assert self.track_c.positivity_verdict == QC0_POSITIVITY_VERDICT

    def test_positivity_verdict_in_allowed(self):
        assert self.track_c.positivity_verdict in ALLOWED_POSITIVITY_VERDICTS

    def test_notes_non_empty(self):
        assert len(self.track_c.notes) > 0


# ================================================================
# TestTrackDStateSpaceTopology — 10 tests
# ================================================================

class TestTrackDStateSpaceTopology:
    def setup_method(self):
        self.track_d = build_track_d_state_space_topology()

    def test_native_topology(self):
        assert self.track_d.native_topology == "real_linear_field_space_over_R"

    def test_minimum_topology_for_qc(self):
        assert self.track_d.minimum_topology_for_qc == "complex_linear_prehilbert_space"

    def test_topology_after_j(self):
        assert "complex" in self.track_d.topology_after_j.lower()

    def test_topology_after_j_and_g(self):
        assert "pre_hilbert" in self.track_d.topology_after_j_and_g.lower()

    def test_projective_space_not_needed_for_qc(self):
        assert self.track_d.projective_space_needed_for_qc is False

    def test_completeness_not_needed_for_qc(self):
        assert self.track_d.completeness_needed_for_qc is False

    def test_density_operator_cone_not_needed(self):
        assert self.track_d.density_operator_cone_needed is False

    def test_functional_space_not_minimum(self):
        assert self.track_d.functional_space_over_histories is False

    def test_minimum_topology_description_non_empty(self):
        assert len(self.track_d.minimum_topology_description) > 0

    def test_notes_non_empty(self):
        assert len(self.track_d.notes) > 0


# ================================================================
# TestTrackEGenerator — 14 tests
# ================================================================

class TestTrackEGenerator:
    def setup_method(self):
        self.track_e = build_track_e_generator()

    def test_hamiltonian_kinematically_admissible(self):
        assert self.track_e.hamiltonian_kinematically_admissible is True

    def test_lindbladian_kinematically_admissible(self):
        assert self.track_e.lindbladian_kinematically_admissible is True

    def test_memory_kernel_kinematically_admissible(self):
        assert self.track_e.memory_kernel_kinematically_admissible is True

    def test_influence_functional_kinematically_admissible(self):
        assert self.track_e.influence_functional_kinematically_admissible is True

    def test_non_hermitian_effective_kinematically_admissible(self):
        assert self.track_e.non_hermitian_effective_kinematically_admissible is True

    def test_hamiltonian_not_grut_consistent(self):
        assert self.track_e.hamiltonian_grut_consistent is False

    def test_lindbladian_grut_consistent(self):
        assert self.track_e.lindbladian_grut_consistent is True

    def test_memory_kernel_grut_consistent(self):
        assert self.track_e.memory_kernel_grut_consistent is True

    def test_primary_admissible_class(self):
        assert self.track_e.primary_admissible_class == "lindbladian_like"

    def test_additional_admissible_classes_count(self):
        assert len(self.track_e.additional_admissible_classes) >= 2

    def test_memory_kernel_in_additional(self):
        assert "memory_kernel" in self.track_e.additional_admissible_classes

    def test_influence_functional_in_additional(self):
        assert "influence_functional" in self.track_e.additional_admissible_classes

    def test_generator_class_verdict(self):
        assert self.track_e.generator_class_verdict == QC0_GENERATOR_CLASS_VERDICT

    def test_generator_class_verdict_in_allowed(self):
        assert self.track_e.generator_class_verdict in ALLOWED_GENERATOR_CLASS_VERDICTS


# ================================================================
# TestTrackFObservable — 6 tests
# ================================================================

class TestTrackFObservable:
    def setup_method(self):
        self.track_f = build_track_f_observable()

    def test_not_needed_before_qc(self):
        assert self.track_f.needed_before_qc is False

    def test_inseparable_from_inner_product(self):
        assert self.track_f.inseparable_from_inner_product is True

    def test_expectation_value_formula_non_empty(self):
        assert len(self.track_f.expectation_value_formula) > 0

    def test_observable_verdict(self):
        assert self.track_f.observable_verdict == "not_needed_yet_for_QC"

    def test_observable_verdict_in_allowed(self):
        assert self.track_f.observable_verdict in ALLOWED_OBSERVABLE_VERDICTS

    def test_notes_non_empty(self):
        assert len(self.track_f.notes) > 0


# ================================================================
# TestTrackGMinimumPackage — 10 tests
# ================================================================

class TestTrackGMinimumPackage:
    def setup_method(self):
        self.track_g = build_track_g_minimum_package()

    def test_n_elements(self):
        assert self.track_g.n_elements == N_MINIMUM_PACKAGE_ELEMENTS

    def test_all_elements_specified(self):
        assert self.track_g.all_elements_specified is True

    def test_package_elements_len(self):
        assert len(self.track_g.package_elements) == N_MINIMUM_PACKAGE_ELEMENTS

    def test_j_in_package(self):
        assert any("J" in e or "j" in e for e in self.track_g.package_elements)

    def test_inner_product_in_package(self):
        assert any("inner_product" in e or "g_mip" in e for e in self.track_g.package_elements)

    def test_generator_in_package(self):
        assert any("lindbladian" in e or "generator" in e for e in self.track_g.package_elements)

    def test_package_appendix_p_classes_len(self):
        assert len(self.track_g.package_appendix_p_classes) == N_MINIMUM_PACKAGE_ELEMENTS

    def test_j_and_g_classes_are_mip(self):
        classes = self.track_g.package_appendix_p_classes
        # First two (J and g) should be MIP
        assert classes[0] == "motivated_independent_postulation"
        assert classes[1] == "motivated_independent_postulation"

    def test_generator_class_is_mbu(self):
        assert self.track_g.package_appendix_p_classes[2] == "motivated_but_unbuilt"

    def test_what_is_not_in_package_non_empty(self):
        assert len(self.track_g.what_is_not_in_package) >= 3

    def test_born_rule_deferred(self):
        deferred = " ".join(self.track_g.what_is_not_in_package)
        assert "born" in deferred.lower() or "born_rule" in deferred.lower()

    def test_package_verdict(self):
        assert self.track_g.package_verdict == QC0_PACKAGE_VERDICT


# ================================================================
# TestTrackHAppendixP — 14 tests
# ================================================================

class TestTrackHAppendixP:
    def setup_method(self):
        self.track_h = build_track_h_appendix_p()

    def test_n_entries(self):
        assert self.track_h.n_entries == len(self.track_h.entries)

    def test_n_entries_at_least_6(self):
        assert self.track_h.n_entries >= 6

    def test_overall_package_class_mip(self):
        assert self.track_h.overall_package_class == "motivated_independent_postulation"

    def test_all_appendix_p_classes_valid(self):
        for e in self.track_h.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES, (
                f"Entry {e.item_id} has invalid class: {e.appendix_p_class}"
            )

    def test_ki1_j_entry_mip(self):
        ki1 = next(e for e in self.track_h.entries if e.item_id == "KI1_J")
        assert ki1.appendix_p_class == "motivated_independent_postulation"

    def test_ki2_inner_product_entry_mip(self):
        ki2 = next(e for e in self.track_h.entries if e.item_id == "KI2_inner_product_g")
        assert ki2.appendix_p_class == "motivated_independent_postulation"

    def test_ki3_norm_entry_mip(self):
        ki3 = next(e for e in self.track_h.entries if e.item_id == "KI3_norm")
        assert ki3.appendix_p_class == "motivated_independent_postulation"

    def test_ki4_positivity_entry_mip(self):
        ki4 = next(e for e in self.track_h.entries if e.item_id == "KI4_positivity")
        # After typo fix, should be motivated_independent_postulation not motivated_independent_postulate
        assert ki4.appendix_p_class == "motivated_independent_postulation"

    def test_ki4_typo_fixed(self):
        ki4 = next(e for e in self.track_h.entries if e.item_id == "KI4_positivity")
        assert ki4.appendix_p_class != "motivated_independent_postulate"

    def test_ki5_topology_entry_bsr(self):
        ki5 = next(e for e in self.track_h.entries if e.item_id == "KI5_topology")
        assert ki5.appendix_p_class == "bounded_structural_result"

    def test_ki6_generator_entry_mbu(self):
        ki6 = next(e for e in self.track_h.entries if e.item_id == "KI6_generator_class")
        assert ki6.appendix_p_class == "motivated_but_unbuilt"

    def test_all_entries_have_allowed_claim(self):
        for e in self.track_h.entries:
            assert len(e.allowed_claim) > 0

    def test_all_entries_have_forbidden_claim(self):
        for e in self.track_h.entries:
            assert len(e.forbidden_claim) > 0

    def test_no_native_canon_in_quantum_elements(self):
        for e in self.track_h.entries:
            assert e.appendix_p_class != "native_canon"


# ================================================================
# TestTrackIReadiness — 10 tests
# ================================================================

class TestTrackIReadiness:
    def setup_method(self):
        self.track_i = build_track_i_readiness()

    def test_native_grut_not_sufficient(self):
        assert self.track_i.native_grut_sufficient_for_qc is False

    def test_package_postulation_required(self):
        assert self.track_i.package_postulation_required is True

    def test_j_postulated_flag(self):
        assert self.track_i.j_postulated is True

    def test_inner_product_postulated_flag(self):
        assert self.track_i.inner_product_postulated is True

    def test_generator_class_identified(self):
        assert self.track_i.generator_class_identified is True

    def test_qc_can_proceed_with_postulate(self):
        assert self.track_i.qc_can_proceed_with_postulate is True

    def test_readiness_verdict(self):
        assert self.track_i.readiness_verdict == QC0_READINESS_VERDICT

    def test_readiness_verdict_in_allowed(self):
        assert self.track_i.readiness_verdict in ALLOWED_READINESS_VERDICTS

    def test_qc_appendix_p_floor(self):
        assert self.track_i.qc_appendix_p_floor == "motivated_independent_postulation"

    def test_conditions_for_qc_non_empty(self):
        assert len(self.track_i.conditions_for_qc) >= 3


# ================================================================
# TestTrackJNonclaims — 8 tests
# ================================================================

class TestTrackJNonclaims:
    def setup_method(self):
        self.track_j = build_track_j_nonclaims()

    def test_n_nonclaims(self):
        assert self.track_j.n_nonclaims == N_QC0_NONCLAIMS

    def test_all_registered(self):
        assert self.track_j.all_registered is True

    def test_nonclaims_len(self):
        assert len(self.track_j.nonclaims) == N_QC0_NONCLAIMS

    def test_j_alone_nonclaim_present(self):
        joined = " ".join(self.track_j.nonclaims)
        assert "J_alone" in joined or "j_alone" in joined.lower()

    def test_bilinear_nonclaim_present(self):
        joined = " ".join(self.track_j.nonclaims)
        assert "bilinear" in joined.lower()

    def test_ghost_nonclaim_present(self):
        joined = " ".join(self.track_j.nonclaims)
        assert "ghost" in joined.lower()

    def test_lindblad_nonclaim_present(self):
        joined = " ".join(self.track_j.nonclaims)
        assert "lindblad" in joined.lower() or "Lindblad" in joined

    def test_native_canon_nonclaim_present(self):
        joined = " ".join(self.track_j.nonclaims)
        assert "native_canon" in joined.lower() or "MIP" in joined


# ================================================================
# TestAllowedForbiddenClaims — 6 tests
# ================================================================

class TestAllowedForbiddenClaims:
    def test_allowed_claims_non_empty(self):
        claims = build_allowed_claims()
        assert len(claims) >= 5

    def test_forbidden_claims_non_empty(self):
        claims = build_forbidden_claims()
        assert len(claims) >= 5

    def test_allowed_claims_mentions_mip(self):
        joined = " ".join(build_allowed_claims())
        assert "MIP" in joined or "motivated_independent" in joined.lower()

    def test_forbidden_claims_mentions_ghost(self):
        joined = " ".join(build_forbidden_claims())
        assert "ghost" in joined.lower() or "CTP" in joined

    def test_allowed_claims_mentions_lindbladian(self):
        joined = " ".join(build_allowed_claims()).lower()
        assert "lindblad" in joined

    def test_forbidden_claims_mentions_native_canon(self):
        joined = " ".join(build_forbidden_claims()).lower()
        assert "native_canon" in joined


# ================================================================
# TestHardGatedVerdicts — 15 tests
# ================================================================

class TestHardGatedVerdicts:
    def setup_method(self):
        self.result = run_qc0_kinematic_package_audit()

    def test_package_verdict_set(self):
        assert self.result.package_verdict == "minimum_kinematic_package_identified"

    def test_package_verdict_in_allowed(self):
        assert self.result.package_verdict in ALLOWED_PACKAGE_VERDICTS

    def test_inner_product_verdict_set(self):
        assert self.result.inner_product_verdict == "inner_product_motivated_independent_postulation"

    def test_inner_product_verdict_in_allowed(self):
        assert self.result.inner_product_verdict in ALLOWED_INNER_PRODUCT_VERDICTS

    def test_positivity_verdict_set(self):
        assert self.result.positivity_verdict == "positivity_requires_postulate"

    def test_positivity_verdict_in_allowed(self):
        assert self.result.positivity_verdict in ALLOWED_POSITIVITY_VERDICTS

    def test_generator_class_verdict_set(self):
        assert self.result.generator_class_verdict == "lindbladian_like_generator_kinematically_admissible"

    def test_generator_class_verdict_in_allowed(self):
        assert self.result.generator_class_verdict in ALLOWED_GENERATOR_CLASS_VERDICTS

    def test_readiness_verdict_set(self):
        assert self.result.readiness_verdict == "ready_only_if_package_is_postulated"

    def test_readiness_verdict_in_allowed(self):
        assert self.result.readiness_verdict in ALLOWED_READINESS_VERDICTS

    def test_all_five_verdicts_distinct(self):
        verdicts = [
            self.result.package_verdict,
            self.result.inner_product_verdict,
            self.result.positivity_verdict,
            self.result.generator_class_verdict,
            self.result.readiness_verdict,
        ]
        assert len(set(verdicts)) == 5

    def test_package_verdict_is_not_blocked(self):
        assert self.result.package_verdict != "no_coherent_package_found"

    def test_inner_product_verdict_is_not_blocked(self):
        assert self.result.inner_product_verdict != "inner_product_blocked_or_inconsistent"

    def test_positivity_verdict_is_not_unavailable(self):
        assert self.result.positivity_verdict != "positivity_currently_unavailable"

    def test_readiness_not_still_blocked(self):
        assert self.result.readiness_verdict != "still_not_ready_for_QC"


# ================================================================
# TestMasterAudit — 20 tests
# ================================================================

class TestMasterAudit:
    def setup_method(self):
        self.result = run_qc0_kinematic_package_audit()

    def test_valid(self):
        assert self.result.valid is True

    def test_all_tracks_present(self):
        assert self.result.track_a_package_inventory is not None
        assert self.result.track_b_inner_product is not None
        assert self.result.track_c_norm_positivity is not None
        assert self.result.track_d_state_space_topology is not None
        assert self.result.track_e_generator is not None
        assert self.result.track_f_observable is not None
        assert self.result.track_g_minimum_package is not None
        assert self.result.track_h_appendix_p is not None
        assert self.result.track_i_readiness is not None
        assert self.result.track_j_nonclaims is not None

    def test_track_a_n_items(self):
        assert self.result.track_a_package_inventory.n_items == N_PACKAGE_ITEMS

    def test_track_b_n_candidates(self):
        assert self.result.track_b_inner_product.n_candidates == N_INNER_PRODUCT_CANDIDATES

    def test_track_b_n_viable(self):
        assert self.result.track_b_inner_product.n_viable == N_INNER_PRODUCT_VIABLE

    def test_track_c_ctp_norm_not_valid(self):
        assert self.result.track_c_norm_positivity.ctp_based_norm_valid is False

    def test_track_c_positivity_requires_postulate(self):
        assert self.result.track_c_norm_positivity.positivity_requires_postulate is True

    def test_track_d_native_topology(self):
        assert self.result.track_d_state_space_topology.native_topology == "real_linear_field_space_over_R"

    def test_track_e_lindbladian_consistent(self):
        assert self.result.track_e_generator.lindbladian_grut_consistent is True

    def test_track_e_hamiltonian_not_consistent(self):
        assert self.result.track_e_generator.hamiltonian_grut_consistent is False

    def test_track_f_not_needed_before_qc(self):
        assert self.result.track_f_observable.needed_before_qc is False

    def test_track_g_n_elements(self):
        assert self.result.track_g_minimum_package.n_elements == N_MINIMUM_PACKAGE_ELEMENTS

    def test_track_h_all_classes_valid(self):
        for e in self.result.track_h_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_track_i_native_grut_not_sufficient(self):
        assert self.result.track_i_readiness.native_grut_sufficient_for_qc is False

    def test_track_j_n_nonclaims(self):
        assert self.result.track_j_nonclaims.n_nonclaims == N_QC0_NONCLAIMS

    def test_qc0_appendix_p_class(self):
        assert self.result.qc0_appendix_p_class == "motivated_independent_postulation"

    def test_allowed_claims_present(self):
        assert len(self.result.allowed_claims) >= 5

    def test_forbidden_claims_present(self):
        assert len(self.result.forbidden_claims) >= 5

    def test_diagnostics_populated(self):
        assert isinstance(self.result.diagnostics, dict)
        assert len(self.result.diagnostics) > 0

    def test_diagnostics_tau_sq(self):
        assert self.result.diagnostics["tau_sq"] == pytest.approx(1.5)

    def test_diagnostics_ghost_inherited(self):
        assert self.result.diagnostics["ghost_obstruction_inherited"] is True

    def test_run_twice_idempotent(self):
        r2 = run_qc0_kinematic_package_audit()
        assert r2.valid is True
        assert r2.package_verdict == self.result.package_verdict
        assert r2.readiness_verdict == self.result.readiness_verdict
