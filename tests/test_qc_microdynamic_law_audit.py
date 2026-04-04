"""Tests for Appendix Q-C — Microdynamic Law Audit.

Covers all 9 audit tracks and 4 hard-gated verdicts.
All tests are deterministic.

Target: ~150 tests.
"""

import pytest

from grut.qc_microdynamic_law_audit import (
    # Constants
    ALLOWED_PRIMARY_LAW_CLASS_VERDICTS,
    ALLOWED_CLASSICAL_LIMIT_VERDICTS,
    ALLOWED_BURDEN_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_ARCH_COMPAT_RATINGS,
    ALLOWED_CLASSICAL_LIMIT_STATUSES,
    ALLOWED_RECOVERY_TYPES,
    N_CANDIDATE_LAW_CLASSES,
    N_VIABLE_CANDIDATES,
    N_PREFERRED_CANDIDATES,
    N_QC_NONCLAIMS,
    N_KINEMATIC_COMPAT_CHECKS,
    N_ARCH_COMPAT_CHECKS,
    TAU_SQ,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    QC_PRIMARY_LAW_CLASS_VERDICT,
    QC_CLASSICAL_LIMIT_VERDICT,
    QC_BURDEN_VERDICT,
    QC_AUTHORIZATION_VERDICT,
    QC_OVERALL_APPENDIX_P_CLASS,
    QC_NONCLAIMS,
    # Builder functions
    build_candidate_cl1_hamiltonian,
    build_candidate_cl2_lindbladian,
    build_candidate_cl3_nonhermitian,
    build_candidate_cl4_memory_kernel,
    build_candidate_cl5_influence_functional,
    build_candidate_cl6_no_law,
    build_track_a_candidate_inventory,
    build_track_b_kinematic_compat,
    build_track_c_arch_compat,
    build_track_d_classical_limit,
    build_track_e_burden,
    build_track_f_appendix_p,
    build_track_g_preferred_law,
    build_track_h_authorization,
    build_track_i_nonclaims,
    build_allowed_claims,
    build_forbidden_claims,
    # Master function
    run_qc_microdynamic_law_audit,
)
import math


# ================================================================
# TestQCConstants — 22 tests
# ================================================================

class TestQCConstants:
    def test_n_candidate_law_classes(self):
        assert N_CANDIDATE_LAW_CLASSES == 6

    def test_n_viable_candidates(self):
        assert N_VIABLE_CANDIDATES == 4

    def test_n_preferred_candidates(self):
        assert N_PREFERRED_CANDIDATES == 1

    def test_n_qc_nonclaims(self):
        assert N_QC_NONCLAIMS == 8

    def test_n_kinematic_compat_checks(self):
        assert N_KINEMATIC_COMPAT_CHECKS == 5

    def test_n_arch_compat_checks(self):
        assert N_ARCH_COMPAT_CHECKS == 5

    def test_tau_sq(self):
        assert TAU_SQ == pytest.approx(1.5)

    def test_phi_minus_growth_rate_sign(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_primary_law_class_verdict_in_allowed(self):
        assert QC_PRIMARY_LAW_CLASS_VERDICT in ALLOWED_PRIMARY_LAW_CLASS_VERDICTS

    def test_classical_limit_verdict_in_allowed(self):
        assert QC_CLASSICAL_LIMIT_VERDICT in ALLOWED_CLASSICAL_LIMIT_VERDICTS

    def test_burden_verdict_in_allowed(self):
        assert QC_BURDEN_VERDICT in ALLOWED_BURDEN_VERDICTS

    def test_authorization_verdict_in_allowed(self):
        assert QC_AUTHORIZATION_VERDICT in ALLOWED_AUTHORIZATION_VERDICTS

    def test_overall_appendix_p_class_in_allowed(self):
        assert QC_OVERALL_APPENDIX_P_CLASS in ALLOWED_APPENDIX_P_CLASSES

    def test_primary_law_class_verdict_value(self):
        assert QC_PRIMARY_LAW_CLASS_VERDICT == "lindbladian_like_law_preferred"

    def test_classical_limit_verdict_value(self):
        assert QC_CLASSICAL_LIMIT_VERDICT == "constitutive_limit_structurally_plausible_but_unbuilt"

    def test_burden_verdict_value(self):
        assert QC_BURDEN_VERDICT == "minimal_extension_burden_identified"

    def test_authorization_verdict_value(self):
        assert QC_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QC5"

    def test_overall_appendix_p_class_is_mbu(self):
        assert QC_OVERALL_APPENDIX_P_CLASS == "motivated_but_unbuilt"

    def test_nonclaims_list_length(self):
        assert len(QC_NONCLAIMS) == N_QC_NONCLAIMS

    def test_all_four_verdicts_distinct(self):
        verdicts = {
            QC_PRIMARY_LAW_CLASS_VERDICT,
            QC_CLASSICAL_LIMIT_VERDICT,
            QC_BURDEN_VERDICT,
            QC_AUTHORIZATION_VERDICT,
        }
        assert len(verdicts) == 4

    def test_classical_limit_not_demonstrated(self):
        assert QC_CLASSICAL_LIMIT_VERDICT != "constitutive_limit_demonstrated"


# ================================================================
# TestTrackACandidateInventory — 20 tests
# ================================================================

class TestTrackACandidateInventory:
    def setup_method(self):
        self.inv = build_track_a_candidate_inventory()

    def test_n_candidates(self):
        assert self.inv.n_candidates == N_CANDIDATE_LAW_CLASSES

    def test_n_viable(self):
        assert self.inv.n_viable == N_VIABLE_CANDIDATES

    def test_n_preferred(self):
        assert self.inv.n_preferred == N_PREFERRED_CANDIDATES

    def test_candidates_len(self):
        assert len(self.inv.candidates) == N_CANDIDATE_LAW_CLASSES

    def test_cl1_hamiltonian_not_viable(self):
        cl1 = next(c for c in self.inv.candidates if c.candidate_id == "CL1_hamiltonian_like")
        assert cl1.viable is False

    def test_cl1_has_grut_conflict(self):
        cl1 = next(c for c in self.inv.candidates if c.candidate_id == "CL1_hamiltonian_like")
        assert cl1.grut_conflict is not None

    def test_cl2_lindbladian_viable(self):
        cl2 = next(c for c in self.inv.candidates if c.candidate_id == "CL2_lindbladian_like")
        assert cl2.viable is True

    def test_cl2_no_grut_conflict(self):
        cl2 = next(c for c in self.inv.candidates if c.candidate_id == "CL2_lindbladian_like")
        assert cl2.grut_conflict is None

    def test_cl3_nonhermitian_viable(self):
        cl3 = next(c for c in self.inv.candidates if c.candidate_id == "CL3_nonhermitian_effective")
        assert cl3.viable is True

    def test_cl4_memory_kernel_viable(self):
        cl4 = next(c for c in self.inv.candidates if c.candidate_id == "CL4_memory_kernel")
        assert cl4.viable is True

    def test_cl5_influence_functional_viable(self):
        cl5 = next(c for c in self.inv.candidates if c.candidate_id == "CL5_influence_functional")
        assert cl5.viable is True

    def test_cl6_no_law_not_viable(self):
        cl6 = next(c for c in self.inv.candidates if c.candidate_id == "CL6_no_coherent_law")
        assert cl6.viable is False

    def test_cl2_appendix_p_mbu(self):
        cl2 = next(c for c in self.inv.candidates if c.candidate_id == "CL2_lindbladian_like")
        assert cl2.appendix_p_class == "motivated_but_unbuilt"

    def test_cl1_appendix_p_cah(self):
        cl1 = next(c for c in self.inv.candidates if c.candidate_id == "CL1_hamiltonian_like")
        assert cl1.appendix_p_class == "compatible_but_ad_hoc"

    def test_cl3_appendix_p_cah(self):
        cl3 = next(c for c in self.inv.candidates if c.candidate_id == "CL3_nonhermitian_effective")
        assert cl3.appendix_p_class == "compatible_but_ad_hoc"

    def test_cl4_appendix_p_mbu(self):
        cl4 = next(c for c in self.inv.candidates if c.candidate_id == "CL4_memory_kernel")
        assert cl4.appendix_p_class == "motivated_but_unbuilt"

    def test_cl5_appendix_p_mbu(self):
        cl5 = next(c for c in self.inv.candidates if c.candidate_id == "CL5_influence_functional")
        assert cl5.appendix_p_class == "motivated_but_unbuilt"

    def test_cl6_appendix_p_bsr(self):
        cl6 = next(c for c in self.inv.candidates if c.candidate_id == "CL6_no_coherent_law")
        assert cl6.appendix_p_class == "bounded_structural_result"

    def test_all_appendix_p_classes_valid(self):
        for c in self.inv.candidates:
            assert c.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_viable_count_matches(self):
        assert sum(1 for c in self.inv.candidates if c.viable) == self.inv.n_viable


# ================================================================
# TestTrackBKinematicCompat — 16 tests
# ================================================================

class TestTrackBKinematicCompat:
    def setup_method(self):
        self.compat = build_track_b_kinematic_compat()

    def test_n_checks_per_candidate(self):
        assert self.compat.n_checks_per_candidate == N_KINEMATIC_COMPAT_CHECKS

    def test_total_entries(self):
        assert len(self.compat.entries) == N_CANDIDATE_LAW_CLASSES * N_KINEMATIC_COMPAT_CHECKS

    def test_ghost_constraint_preserved(self):
        assert self.compat.ghost_constraint_preserved is True

    def test_cl2_all_compatible(self):
        assert "CL2_lindbladian_like" in self.compat.candidates_all_kinematically_compatible

    def test_cl3_all_compatible(self):
        assert "CL3_nonhermitian_effective" in self.compat.candidates_all_kinematically_compatible

    def test_cl4_all_compatible(self):
        assert "CL4_memory_kernel" in self.compat.candidates_all_kinematically_compatible

    def test_cl5_all_compatible(self):
        assert "CL5_influence_functional" in self.compat.candidates_all_kinematically_compatible

    def test_cl1_not_fully_compatible(self):
        assert "CL1_hamiltonian_like" not in self.compat.candidates_all_kinematically_compatible

    def test_cl6_not_fully_compatible(self):
        assert "CL6_no_coherent_law" not in self.compat.candidates_all_kinematically_compatible

    def test_cl1_kinematically_blocked(self):
        assert "CL1_hamiltonian_like" in self.compat.candidates_kinematically_blocked

    def test_cl1_open_system_fails(self):
        cl1_open_system = next(
            e for e in self.compat.entries
            if e.candidate_id == "CL1_hamiltonian_like"
            and e.check_name == "open_system_consistency"
        )
        assert cl1_open_system.compatible is False

    def test_cl2_j_compatible(self):
        cl2_j = next(
            e for e in self.compat.entries
            if e.candidate_id == "CL2_lindbladian_like"
            and e.check_name == "j_complex_structure"
        )
        assert cl2_j.compatible is True

    def test_cl2_positivity_compatible(self):
        cl2_pos = next(
            e for e in self.compat.entries
            if e.candidate_id == "CL2_lindbladian_like"
            and e.check_name == "inner_product_positivity"
        )
        assert cl2_pos.compatible is True

    def test_all_viable_candidates_pass_ghost_check(self):
        for cid in ["CL2_lindbladian_like", "CL3_nonhermitian_effective",
                    "CL4_memory_kernel", "CL5_influence_functional"]:
            ghost_entry = next(
                e for e in self.compat.entries
                if e.candidate_id == cid and e.check_name == "ghost_constraint"
            )
            assert ghost_entry.compatible is True

    def test_n_fully_compatible_candidates(self):
        assert len(self.compat.candidates_all_kinematically_compatible) == N_VIABLE_CANDIDATES


# ================================================================
# TestTrackCArchCompat — 16 tests
# ================================================================

class TestTrackCArchCompat:
    def setup_method(self):
        self.arch = build_track_c_arch_compat()

    def test_n_entries(self):
        assert len(self.arch.entries) == N_CANDIDATE_LAW_CLASSES

    def test_cl2_structurally_natural(self):
        assert "CL2_lindbladian_like" in self.arch.structurally_natural_ids

    def test_cl4_structurally_natural(self):
        assert "CL4_memory_kernel" in self.arch.structurally_natural_ids

    def test_cl5_structurally_natural(self):
        assert "CL5_influence_functional" in self.arch.structurally_natural_ids

    def test_cl1_incompatible(self):
        assert "CL1_hamiltonian_like" in self.arch.incompatible_ids

    def test_cl3_only_compatible(self):
        assert "CL3_nonhermitian_effective" in self.arch.only_compatible_ids

    def test_cl6_underdetermined(self):
        assert "CL6_no_coherent_law" in self.arch.underdetermined_ids

    def test_cl2_dissipation_natural(self):
        cl2 = next(e for e in self.arch.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.dissipation_rating == "structurally_natural"

    def test_cl1_dissipation_incompatible(self):
        cl1 = next(e for e in self.arch.entries if e.candidate_id == "CL1_hamiltonian_like")
        assert cl1.dissipation_rating == "incompatible"

    def test_cl4_memory_structure_natural(self):
        cl4 = next(e for e in self.arch.entries if e.candidate_id == "CL4_memory_kernel")
        assert cl4.memory_structure_rating == "structurally_natural"

    def test_cl5_ctp_galley_natural(self):
        cl5 = next(e for e in self.arch.entries if e.candidate_id == "CL5_influence_functional")
        assert cl5.ctp_galley_rating == "structurally_natural"

    def test_all_overall_ratings_valid(self):
        for e in self.arch.entries:
            assert e.overall_arch_rating in ALLOWED_ARCH_COMPAT_RATINGS

    def test_n_structurally_natural(self):
        assert len(self.arch.structurally_natural_ids) == 3  # CL2, CL4, CL5

    def test_n_incompatible(self):
        assert len(self.arch.incompatible_ids) == 1  # CL1

    def test_cl2_tau_eff_natural(self):
        cl2 = next(e for e in self.arch.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.tau_eff_rating == "structurally_natural"

    def test_cl1_tau_eff_incompatible(self):
        cl1 = next(e for e in self.arch.entries if e.candidate_id == "CL1_hamiltonian_like")
        assert cl1.tau_eff_rating == "incompatible"


# ================================================================
# TestTrackDClassicalLimit — 18 tests
# ================================================================

class TestTrackDClassicalLimit:
    def setup_method(self):
        self.cl = build_track_d_classical_limit()

    def test_n_demonstrated(self):
        assert self.cl.n_demonstrated == 0

    def test_n_plausible_but_unbuilt(self):
        assert self.cl.n_plausible_but_unbuilt == 4

    def test_n_blocked(self):
        assert self.cl.n_blocked == 1

    def test_n_underdetermined(self):
        assert self.cl.n_underdetermined == 1

    def test_classical_limit_verdict(self):
        assert self.cl.classical_limit_verdict == QC_CLASSICAL_LIMIT_VERDICT

    def test_classical_limit_verdict_in_allowed(self):
        assert self.cl.classical_limit_verdict in ALLOWED_CLASSICAL_LIMIT_VERDICTS

    def test_preferred_recovery_type(self):
        assert self.cl.preferred_recovery_type == "expectation_value_limit"

    def test_cl1_recovery_blocked(self):
        cl1 = next(e for e in self.cl.entries if e.candidate_id == "CL1_hamiltonian_like")
        assert cl1.recovery_status == "recovery_blocked"

    def test_cl1_blocking_reason_non_empty(self):
        cl1 = next(e for e in self.cl.entries if e.candidate_id == "CL1_hamiltonian_like")
        assert cl1.blocking_reason is not None and len(cl1.blocking_reason) > 0

    def test_cl2_recovery_plausible(self):
        cl2 = next(e for e in self.cl.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.recovery_status == "recovery_structurally_plausible_but_unbuilt"

    def test_cl2_no_blocking_reason(self):
        cl2 = next(e for e in self.cl.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.blocking_reason is None

    def test_cl2_recovery_type(self):
        cl2 = next(e for e in self.cl.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.recovery_type == "expectation_value_limit"

    def test_cl4_recovery_plausible(self):
        cl4 = next(e for e in self.cl.entries if e.candidate_id == "CL4_memory_kernel")
        assert cl4.recovery_status == "recovery_structurally_plausible_but_unbuilt"

    def test_cl5_recovery_plausible(self):
        cl5 = next(e for e in self.cl.entries if e.candidate_id == "CL5_influence_functional")
        assert cl5.recovery_status == "recovery_structurally_plausible_but_unbuilt"

    def test_cl6_recovery_underdetermined(self):
        cl6 = next(e for e in self.cl.entries if e.candidate_id == "CL6_no_coherent_law")
        assert cl6.recovery_status == "recovery_underdetermined"

    def test_all_recovery_statuses_valid(self):
        for e in self.cl.entries:
            assert e.recovery_status in ALLOWED_CLASSICAL_LIMIT_STATUSES

    def test_all_recovery_types_valid(self):
        for e in self.cl.entries:
            assert e.recovery_type in ALLOWED_RECOVERY_TYPES

    def test_cl2_tau_appears_as_decay_rate(self):
        cl2 = next(e for e in self.cl.entries if e.candidate_id == "CL2_lindbladian_like")
        assert "tau" in cl2.tau_appears_as.lower() or "gamma" in cl2.tau_appears_as.lower()


# ================================================================
# TestTrackEBurden — 12 tests
# ================================================================

class TestTrackEBurden:
    def setup_method(self):
        self.burden = build_track_e_burden()

    def test_minimum_burden_candidate(self):
        assert self.burden.minimum_burden_candidate_id == "CL2_lindbladian_like"

    def test_burden_verdict(self):
        assert self.burden.burden_verdict == QC_BURDEN_VERDICT

    def test_burden_verdict_in_allowed(self):
        assert self.burden.burden_verdict in ALLOWED_BURDEN_VERDICTS

    def test_preferred_by_burden(self):
        assert self.burden.preferred_by_burden == "CL2_lindbladian_like"

    def test_cl2_lowest_burden_score(self):
        cl2 = next(e for e in self.burden.entries if e.candidate_id == "CL2_lindbladian_like")
        for other in self.burden.entries:
            if other.candidate_id != "CL2_lindbladian_like":
                assert cl2.burden_score <= other.burden_score

    def test_cl5_highest_burden_score(self):
        cl5 = next(e for e in self.burden.entries if e.candidate_id == "CL5_influence_functional")
        for other in self.burden.entries:
            assert other.burden_score <= cl5.burden_score

    def test_cl2_no_new_field_content(self):
        cl2 = next(e for e in self.burden.entries if e.candidate_id == "CL2_lindbladian_like")
        assert len(cl2.new_field_content) == 0

    def test_cl2_no_new_state_objects(self):
        cl2 = next(e for e in self.burden.entries if e.candidate_id == "CL2_lindbladian_like")
        assert len(cl2.new_state_objects) == 0

    def test_cl4_has_kernel_parameter(self):
        cl4 = next(e for e in self.burden.entries if e.candidate_id == "CL4_memory_kernel")
        has_kernel = any("kernel" in p.lower() for p in cl4.new_free_parameters)
        assert has_kernel

    def test_cl5_has_new_state_objects(self):
        cl5 = next(e for e in self.burden.entries if e.candidate_id == "CL5_influence_functional")
        assert len(cl5.new_state_objects) > 0

    def test_n_entries_at_least_4(self):
        assert len(self.burden.entries) >= 4  # viable candidates only

    def test_notes_non_empty(self):
        assert len(self.burden.notes) > 0


# ================================================================
# TestTrackFAppendixP — 14 tests
# ================================================================

class TestTrackFAppendixP:
    def setup_method(self):
        self.ap = build_track_f_appendix_p()

    def test_n_entries(self):
        assert self.ap.n_entries == N_CANDIDATE_LAW_CLASSES

    def test_entries_len(self):
        assert len(self.ap.entries) == N_CANDIDATE_LAW_CLASSES

    def test_overall_program_class_mbu(self):
        assert self.ap.overall_program_class == "motivated_but_unbuilt"

    def test_no_native_canon(self):
        assert self.ap.no_native_canon_in_any_class is True

    def test_all_appendix_p_classes_valid(self):
        for e in self.ap.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_cl2_mbu(self):
        cl2 = next(e for e in self.ap.entries if e.candidate_id == "CL2_lindbladian_like")
        assert cl2.appendix_p_class == "motivated_but_unbuilt"

    def test_cl4_mbu(self):
        cl4 = next(e for e in self.ap.entries if e.candidate_id == "CL4_memory_kernel")
        assert cl4.appendix_p_class == "motivated_but_unbuilt"

    def test_cl5_mbu(self):
        cl5 = next(e for e in self.ap.entries if e.candidate_id == "CL5_influence_functional")
        assert cl5.appendix_p_class == "motivated_but_unbuilt"

    def test_cl1_cah(self):
        cl1 = next(e for e in self.ap.entries if e.candidate_id == "CL1_hamiltonian_like")
        assert cl1.appendix_p_class == "compatible_but_ad_hoc"

    def test_cl3_cah(self):
        cl3 = next(e for e in self.ap.entries if e.candidate_id == "CL3_nonhermitian_effective")
        assert cl3.appendix_p_class == "compatible_but_ad_hoc"

    def test_cl6_bsr(self):
        cl6 = next(e for e in self.ap.entries if e.candidate_id == "CL6_no_coherent_law")
        assert cl6.appendix_p_class == "bounded_structural_result"

    def test_all_allowed_claims_non_empty(self):
        for e in self.ap.entries:
            assert len(e.allowed_claim) > 0

    def test_all_forbidden_claims_non_empty(self):
        for e in self.ap.entries:
            assert len(e.forbidden_claim) > 0

    def test_no_entry_has_native_canon(self):
        for e in self.ap.entries:
            assert e.appendix_p_class != "native_canon"


# ================================================================
# TestTrackGPreferredLaw — 12 tests
# ================================================================

class TestTrackGPreferredLaw:
    def setup_method(self):
        self.pref = build_track_g_preferred_law()

    def test_preferred_candidate_id(self):
        assert self.pref.preferred_candidate_id == "CL2_lindbladian_like"

    def test_n_criteria_met(self):
        assert self.pref.n_criteria_met == 5

    def test_unique_preference(self):
        assert self.pref.unique_preference is True

    def test_primary_law_class_verdict(self):
        assert self.pref.primary_law_class_verdict == QC_PRIMARY_LAW_CLASS_VERDICT

    def test_runner_up_ids_non_empty(self):
        assert len(self.pref.runner_up_ids) >= 2

    def test_cl4_is_runner_up(self):
        assert "CL4_memory_kernel" in self.pref.runner_up_ids

    def test_cl5_is_runner_up(self):
        assert "CL5_influence_functional" in self.pref.runner_up_ids

    def test_why_not_runner_ups_non_empty(self):
        assert len(self.pref.why_not_runner_ups) > 0

    def test_selection_criteria_met_list_length(self):
        assert len(self.pref.selection_criteria_met) == 5

    def test_criteria_include_package_compatibility(self):
        assert "compatible_with_minimum_package" in self.pref.selection_criteria_met

    def test_criteria_include_ghost_constraints(self):
        assert "preserves_ghost_constraints" in self.pref.selection_criteria_met

    def test_criteria_include_minimizes_structure(self):
        assert "minimizes_added_structure" in self.pref.selection_criteria_met


# ================================================================
# TestTrackHAuthorization — 10 tests
# ================================================================

class TestTrackHAuthorization:
    def setup_method(self):
        self.auth = build_track_h_authorization()

    def test_qc5_authorized(self):
        assert self.auth.qc5_authorized is True

    def test_qd_not_ready(self):
        assert self.auth.qd_measurement_ready is False

    def test_benchmark_not_ready(self):
        assert self.auth.benchmark_toy_models_ready is False

    def test_no_additional_closure_required(self):
        assert self.auth.more_microdynamic_closure_required is False

    def test_authorization_verdict(self):
        assert self.auth.authorization_verdict == QC_AUTHORIZATION_VERDICT

    def test_authorization_verdict_in_allowed(self):
        assert self.auth.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_preconditions_non_empty(self):
        assert len(self.auth.preconditions_for_qc5) >= 3

    def test_what_qc5_must_do_non_empty(self):
        assert len(self.auth.what_qc5_must_do) > 0

    def test_qc5_mentions_lindblad(self):
        assert "lindblad" in self.auth.what_qc5_must_do.lower() or "Lindblad" in self.auth.what_qc5_must_do

    def test_preconditions_mention_ghost(self):
        joined = " ".join(self.auth.preconditions_for_qc5).lower()
        assert "ghost" in joined


# ================================================================
# TestTrackINonclaims — 8 tests
# ================================================================

class TestTrackINonclaims:
    def setup_method(self):
        self.nc = build_track_i_nonclaims()

    def test_n_nonclaims(self):
        assert self.nc.n_nonclaims == N_QC_NONCLAIMS

    def test_all_registered(self):
        assert self.nc.all_registered is True

    def test_nonclaims_len(self):
        assert len(self.nc.nonclaims) == N_QC_NONCLAIMS

    def test_admissible_not_derived_nonclaim(self):
        joined = " ".join(self.nc.nonclaims).lower()
        assert "admissible" in joined and "derived" in joined

    def test_classical_limit_nonclaim(self):
        joined = " ".join(self.nc.nonclaims).lower()
        assert "plausib" in joined or "classical_limit" in joined

    def test_measurement_nonclaim(self):
        joined = " ".join(self.nc.nonclaims).lower()
        assert "measurement" in joined

    def test_native_canon_nonclaim(self):
        joined = " ".join(self.nc.nonclaims).lower()
        assert "native" in joined or "canon" in joined or "mbu" in joined

    def test_preferred_not_solved_nonclaim(self):
        joined = " ".join(self.nc.nonclaims).lower()
        assert "solved" in joined or "preferred" in joined


# ================================================================
# TestAllowedForbiddenClaims — 6 tests
# ================================================================

class TestAllowedForbiddenClaims:
    def test_allowed_claims_non_empty(self):
        assert len(build_allowed_claims()) >= 5

    def test_forbidden_claims_non_empty(self):
        assert len(build_forbidden_claims()) >= 5

    def test_allowed_mentions_lindbladian(self):
        joined = " ".join(build_allowed_claims()).lower()
        assert "lindblad" in joined

    def test_forbidden_mentions_derived(self):
        joined = " ".join(build_forbidden_claims()).lower()
        assert "derived" in joined

    def test_allowed_mentions_mbu(self):
        joined = " ".join(build_allowed_claims()).lower()
        assert "mbu" in joined or "motivated_but_unbuilt" in joined

    def test_forbidden_mentions_native_canon(self):
        joined = " ".join(build_forbidden_claims()).lower()
        assert "native_canon" in joined


# ================================================================
# TestHardGatedVerdicts — 16 tests
# ================================================================

class TestHardGatedVerdicts:
    def setup_method(self):
        self.result = run_qc_microdynamic_law_audit()

    def test_primary_law_class_verdict(self):
        assert self.result.primary_law_class_verdict == "lindbladian_like_law_preferred"

    def test_primary_law_class_verdict_in_allowed(self):
        assert self.result.primary_law_class_verdict in ALLOWED_PRIMARY_LAW_CLASS_VERDICTS

    def test_classical_limit_verdict(self):
        assert self.result.classical_limit_verdict == "constitutive_limit_structurally_plausible_but_unbuilt"

    def test_classical_limit_verdict_in_allowed(self):
        assert self.result.classical_limit_verdict in ALLOWED_CLASSICAL_LIMIT_VERDICTS

    def test_burden_verdict(self):
        assert self.result.burden_verdict == "minimal_extension_burden_identified"

    def test_burden_verdict_in_allowed(self):
        assert self.result.burden_verdict in ALLOWED_BURDEN_VERDICTS

    def test_authorization_verdict(self):
        assert self.result.authorization_verdict == "authorized_to_proceed_to_QC5"

    def test_authorization_verdict_in_allowed(self):
        assert self.result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_not_no_coherent_law(self):
        assert self.result.primary_law_class_verdict != "no_coherent_microdynamic_law_found"

    def test_not_no_unique_preferred(self):
        assert self.result.primary_law_class_verdict != "no_unique_preferred_law_class"

    def test_not_demonstrated(self):
        assert self.result.classical_limit_verdict != "constitutive_limit_demonstrated"

    def test_not_blocked(self):
        assert self.result.classical_limit_verdict != "constitutive_limit_blocked"

    def test_burden_not_excessive(self):
        assert self.result.burden_verdict != "extension_burden_excessive"

    def test_authorized_not_blocked(self):
        assert self.result.authorization_verdict != "not_authorized_to_proceed"

    def test_qc5_authorized_consistent(self):
        assert self.result.track_h_authorization.qc5_authorized is True

    def test_preferred_candidate_consistent(self):
        assert self.result.track_g_preferred_law.preferred_candidate_id == "CL2_lindbladian_like"


# ================================================================
# TestMasterAudit — 20 tests
# ================================================================

class TestMasterAudit:
    def setup_method(self):
        self.result = run_qc_microdynamic_law_audit()

    def test_valid(self):
        assert self.result.valid is True

    def test_all_tracks_present(self):
        assert self.result.track_a_candidate_inventory is not None
        assert self.result.track_b_kinematic_compat is not None
        assert self.result.track_c_arch_compat is not None
        assert self.result.track_d_classical_limit is not None
        assert self.result.track_e_burden is not None
        assert self.result.track_f_appendix_p is not None
        assert self.result.track_g_preferred_law is not None
        assert self.result.track_h_authorization is not None
        assert self.result.track_i_nonclaims is not None

    def test_track_a_n_candidates(self):
        assert self.result.track_a_candidate_inventory.n_candidates == N_CANDIDATE_LAW_CLASSES

    def test_track_a_n_viable(self):
        assert self.result.track_a_candidate_inventory.n_viable == N_VIABLE_CANDIDATES

    def test_track_b_ghost_preserved(self):
        assert self.result.track_b_kinematic_compat.ghost_constraint_preserved is True

    def test_track_c_cl2_natural(self):
        assert "CL2_lindbladian_like" in self.result.track_c_arch_compat.structurally_natural_ids

    def test_track_c_cl1_incompatible(self):
        assert "CL1_hamiltonian_like" in self.result.track_c_arch_compat.incompatible_ids

    def test_track_d_zero_demonstrated(self):
        assert self.result.track_d_classical_limit.n_demonstrated == 0

    def test_track_d_four_plausible(self):
        assert self.result.track_d_classical_limit.n_plausible_but_unbuilt == 4

    def test_track_e_minimum_burden(self):
        assert self.result.track_e_burden.minimum_burden_candidate_id == "CL2_lindbladian_like"

    def test_track_f_no_native_canon(self):
        assert self.result.track_f_appendix_p.no_native_canon_in_any_class is True

    def test_track_g_preferred_id(self):
        assert self.result.track_g_preferred_law.preferred_candidate_id == "CL2_lindbladian_like"

    def test_track_g_n_criteria(self):
        assert self.result.track_g_preferred_law.n_criteria_met == 5

    def test_track_h_qc5_authorized(self):
        assert self.result.track_h_authorization.qc5_authorized is True

    def test_track_i_n_nonclaims(self):
        assert self.result.track_i_nonclaims.n_nonclaims == N_QC_NONCLAIMS

    def test_qc_appendix_p_class(self):
        assert self.result.qc_appendix_p_class == "motivated_but_unbuilt"

    def test_allowed_claims_present(self):
        assert len(self.result.allowed_claims) >= 5

    def test_forbidden_claims_present(self):
        assert len(self.result.forbidden_claims) >= 5

    def test_diagnostics_populated(self):
        assert isinstance(self.result.diagnostics, dict)
        assert len(self.result.diagnostics) > 0

    def test_diagnostics_tau_sq(self):
        assert self.result.diagnostics["tau_sq"] == pytest.approx(1.5)

    def test_run_twice_idempotent(self):
        r2 = run_qc_microdynamic_law_audit()
        assert r2.valid is True
        assert r2.primary_law_class_verdict == self.result.primary_law_class_verdict
        assert r2.authorization_verdict == self.result.authorization_verdict
