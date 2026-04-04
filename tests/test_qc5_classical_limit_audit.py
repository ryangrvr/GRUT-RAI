"""Test suite for grut/qc5_classical_limit_audit.py — Q-C.5 Classical-Limit Recovery Audit."""

import math
import sys

sys.path.insert(0, ".")

from grut.qc5_classical_limit_audit import (
    # Physical constants
    TAU_SQ,
    TAU,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    # Count constants
    N_CLASSICAL_OBSERVABLE_CANDIDATES,
    N_VIABLE_OBSERVABLE_CANDIDATES,
    N_LIMIT_TYPES_TESTED,
    N_PREFERRED_LIMIT_COMBINATION,
    N_QC5_NONCLAIMS,
    N_SECONDARY_CLASSES_TESTED,
    # Verdict strings
    QC5_CONSTITUTIVE_RECOVERY_VERDICT,
    QC5_PARAMETER_MATCHING_VERDICT,
    QC5_PREFERRED_CLASS_RETENTION_VERDICT,
    QC5_AUTHORIZATION_VERDICT,
    QC5_OVERALL_APPENDIX_P_CLASS,
    # Inherited Q-C values
    QC_INHERITED_PRIMARY_LAW_CLASS,
    QC_INHERITED_CLASSICAL_LIMIT,
    QC_INHERITED_AUTHORIZATION,
    # Nonclaims list
    QC5_NONCLAIMS,
    # Frozensets
    ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS,
    ALLOWED_PARAMETER_MATCHING_VERDICTS,
    ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    # Private track builders (accessed via module attribute)
    _build_track_a,
    _build_track_b,
    _build_track_c,
    _build_track_d,
    _build_track_e,
    _build_track_f,
    _build_track_g,
    _build_track_h,
    _build_track_i,
    _build_track_j,
    _build_track_k,
    # Master function
    run_qc5_classical_limit_audit,
)


# ================================================================
# TestQC5Constants — ~20 tests
# ================================================================

class TestQC5Constants:
    def test_tau_sq_exact(self):
        assert TAU_SQ == 3.0 / 2.0

    def test_tau_sq_numeric(self):
        assert abs(TAU_SQ - 1.5) < 1e-15

    def test_tau_is_sqrt_of_tau_sq(self):
        assert abs(TAU - math.sqrt(TAU_SQ)) < 1e-12

    def test_tau_approx_value(self):
        assert abs(TAU - 1.2247448713915890) < 1e-10

    def test_tau_positive(self):
        assert TAU > 0.0

    def test_phi_minus_growth_rate_sign_positive(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_cannot_be_imaginary_part(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_n_classical_observable_candidates(self):
        assert N_CLASSICAL_OBSERVABLE_CANDIDATES == 6

    def test_n_viable_observable_candidates(self):
        assert N_VIABLE_OBSERVABLE_CANDIDATES == 1

    def test_n_limit_types_tested(self):
        assert N_LIMIT_TYPES_TESTED == 7

    def test_n_preferred_limit_combination(self):
        assert N_PREFERRED_LIMIT_COMBINATION == 3

    def test_n_qc5_nonclaims(self):
        assert N_QC5_NONCLAIMS == 8

    def test_n_secondary_classes_tested(self):
        assert N_SECONDARY_CLASSES_TESTED == 3

    def test_inherited_primary_law_class(self):
        assert QC_INHERITED_PRIMARY_LAW_CLASS == "lindbladian_like_law_preferred"

    def test_inherited_classical_limit(self):
        assert QC_INHERITED_CLASSICAL_LIMIT == "constitutive_limit_structurally_plausible_but_unbuilt"

    def test_inherited_authorization(self):
        assert QC_INHERITED_AUTHORIZATION == "authorized_to_proceed_to_QC5"

    def test_allowed_constitutive_recovery_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS, frozenset)

    def test_allowed_parameter_matching_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_PARAMETER_MATCHING_VERDICTS, frozenset)

    def test_allowed_preferred_class_retention_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS, frozenset)

    def test_allowed_authorization_verdicts_is_frozenset(self):
        assert isinstance(ALLOWED_AUTHORIZATION_VERDICTS, frozenset)

    def test_constitutive_recovery_verdict_in_allowed(self):
        assert QC5_CONSTITUTIVE_RECOVERY_VERDICT in ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS

    def test_parameter_matching_verdict_in_allowed(self):
        assert QC5_PARAMETER_MATCHING_VERDICT in ALLOWED_PARAMETER_MATCHING_VERDICTS

    def test_preferred_class_retention_verdict_in_allowed(self):
        assert QC5_PREFERRED_CLASS_RETENTION_VERDICT in ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS

    def test_authorization_verdict_in_allowed(self):
        assert QC5_AUTHORIZATION_VERDICT in ALLOWED_AUTHORIZATION_VERDICTS


# ================================================================
# TestTrackAObservable — ~20 tests
# ================================================================

class TestTrackAObservable:
    def setup_method(self):
        self.track = _build_track_a()

    def test_n_candidates(self):
        assert self.track.n_candidates == N_CLASSICAL_OBSERVABLE_CANDIDATES

    def test_n_viable(self):
        assert self.track.n_viable == N_VIABLE_OBSERVABLE_CANDIDATES

    def test_candidates_list_length(self):
        assert len(self.track.candidates) == N_CLASSICAL_OBSERVABLE_CANDIDATES

    def test_co1_is_viable(self):
        co1 = next(c for c in self.track.candidates if c.candidate_id == "CO1_expectation_value")
        assert co1.viable is True

    def test_co2_not_viable(self):
        co2 = next(c for c in self.track.candidates if c.candidate_id == "CO2_reduced_state_coarse_grained")
        assert co2.viable is False

    def test_co3_not_viable(self):
        co3 = next(c for c in self.track.candidates if c.candidate_id == "CO3_pointer_variable")
        assert co3.viable is False

    def test_co4_not_viable(self):
        co4 = next(c for c in self.track.candidates if c.candidate_id == "CO4_diagonal_density_component")
        assert co4.viable is False

    def test_co5_not_viable(self):
        co5 = next(c for c in self.track.candidates if c.candidate_id == "CO5_history_space_saddle")
        assert co5.viable is False

    def test_co5_not_ghost_safe(self):
        co5 = next(c for c in self.track.candidates if c.candidate_id == "CO5_history_space_saddle")
        assert co5.ghost_safe is False

    def test_co6_not_viable(self):
        co6 = next(c for c in self.track.candidates if c.candidate_id == "CO6_no_valid_classical_observable")
        assert co6.viable is False

    def test_chosen_observable_id(self):
        assert self.track.chosen_observable_id == "CO1_expectation_value"

    def test_chosen_observable_map(self):
        assert self.track.chosen_observable_map == "Phi_cl(t) = Tr(Phi_hat * rho(t))"

    def test_only_one_viable_candidate(self):
        viable = [c for c in self.track.candidates if c.viable]
        assert len(viable) == 1

    def test_viable_candidate_is_co1(self):
        viable = [c for c in self.track.candidates if c.viable]
        assert viable[0].candidate_id == "CO1_expectation_value"

    def test_all_non_co1_not_viable(self):
        non_co1 = [c for c in self.track.candidates if c.candidate_id != "CO1_expectation_value"]
        assert all(not c.viable for c in non_co1)

    def test_all_six_candidate_ids_present(self):
        ids = {c.candidate_id for c in self.track.candidates}
        expected = {
            "CO1_expectation_value",
            "CO2_reduced_state_coarse_grained",
            "CO3_pointer_variable",
            "CO4_diagonal_density_component",
            "CO5_history_space_saddle",
            "CO6_no_valid_classical_observable",
        }
        assert ids == expected

    def test_n_candidates_equals_six(self):
        assert self.track.n_candidates == 6

    def test_n_viable_equals_one(self):
        assert self.track.n_viable == 1

    def test_co1_ghost_safe(self):
        co1 = next(c for c in self.track.candidates if c.candidate_id == "CO1_expectation_value")
        assert co1.ghost_safe is True


# ================================================================
# TestTrackBSourceMapping — ~10 tests
# ================================================================

class TestTrackBSourceMapping:
    def setup_method(self):
        self.track = _build_track_b()

    def test_viable_source_identification(self):
        assert self.track.viable_source_identification == "external_drive_or_bath_induced_bias"

    def test_source_enters_as(self):
        assert self.track.source_enters_as == "external_drive"

    def test_source_mapping_complete(self):
        assert self.track.source_mapping_complete is True

    def test_source_mapping_status(self):
        assert self.track.source_mapping_status == "structurally_complete_operator_unbuilt"

    def test_source_x_candidates_list_exists(self):
        assert hasattr(self.track, "source_x_candidates")
        assert isinstance(self.track.source_x_candidates, list)

    def test_source_identification_nonempty(self):
        assert len(self.track.viable_source_identification) > 0

    def test_source_enters_as_nonempty(self):
        assert len(self.track.source_enters_as) > 0

    def test_mapping_status_contains_structurally_complete(self):
        assert "structurally_complete" in self.track.source_mapping_status

    def test_mapping_status_contains_operator_unbuilt(self):
        assert "operator_unbuilt" in self.track.source_mapping_status

    def test_source_mapping_complete_is_bool(self):
        assert isinstance(self.track.source_mapping_complete, bool)


# ================================================================
# TestTrackCTauMapping — ~12 tests
# ================================================================

class TestTrackCTauMapping:
    def setup_method(self):
        self.track = _build_track_c()

    def test_tau_identification(self):
        assert self.track.tau_identification == "inverse_damping_rate_gamma_eq_1_over_tau"

    def test_tau_enters_as(self):
        assert self.track.tau_enters_as == "dissipator_coefficient"

    def test_tau_sq_value(self):
        assert abs(self.track.tau_sq_value - 1.5) < 1e-12

    def test_gamma_eq_1_over_tau_flag(self):
        assert self.track.gamma_eq_1_over_tau is True

    def test_mapping_preserves_prior_tau_meaning(self):
        assert self.track.mapping_preserves_prior_tau_meaning is True

    def test_mapping_status(self):
        assert self.track.mapping_status == "tau_matching_complete"

    def test_gamma_times_tau_equals_one(self):
        gamma = 1.0 / self.track.tau_value
        tau = self.track.tau_value
        assert abs(gamma * tau - 1.0) < 1e-10

    def test_tau_sq_value_matches_global_tau_sq(self):
        assert abs(self.track.tau_sq_value - TAU_SQ) < 1e-12

    def test_tau_identification_nonempty(self):
        assert len(self.track.tau_identification) > 0

    def test_mapping_status_nonempty(self):
        assert len(self.track.mapping_status) > 0

    def test_tau_sq_value_is_three_halves(self):
        assert self.track.tau_sq_value == 3.0 / 2.0

    def test_mapping_status_contains_complete(self):
        assert "complete" in self.track.mapping_status


# ================================================================
# TestTrackDLimitTypes — ~15 tests
# ================================================================

class TestTrackDLimitTypes:
    def setup_method(self):
        self.track = _build_track_d()

    def test_n_limits_tested(self):
        assert self.track.n_limits_tested == N_LIMIT_TYPES_TESTED

    def test_n_limits_tested_equals_seven(self):
        assert self.track.n_limits_tested == 7

    def test_preferred_limit_combination_length(self):
        assert len(self.track.preferred_limit_combination) == N_PREFERRED_LIMIT_COMBINATION

    def test_preferred_limit_combination_length_equals_three(self):
        assert len(self.track.preferred_limit_combination) == 3

    def test_markovian_in_preferred_combination(self):
        assert "markovian_limit" in self.track.preferred_limit_combination

    def test_weak_coupling_in_preferred_combination(self):
        assert "weak_coupling_limit" in self.track.preferred_limit_combination

    def test_expectation_value_in_preferred_combination(self):
        assert "expectation_value_limit" in self.track.preferred_limit_combination

    def test_multi_limit_required(self):
        assert self.track.multi_limit_required is True

    def test_minimal_coherent_route_identified(self):
        assert self.track.minimal_coherent_route_identified is True

    def test_markovian_limit_applicable(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "markovian_limit")
        assert e.limit_applicable is True

    def test_markovian_limit_role_primary(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "markovian_limit")
        assert e.limit_role == "primary"

    def test_weak_coupling_limit_applicable(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "weak_coupling_limit")
        assert e.limit_applicable is True

    def test_weak_coupling_limit_role_primary(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "weak_coupling_limit")
        assert e.limit_role == "primary"

    def test_mean_field_limit_not_applicable(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "mean_field_limit")
        assert e.limit_applicable is False

    def test_semiclassical_limit_not_applicable(self):
        e = next(lt for lt in self.track.limit_entries if lt.limit_name == "semiclassical_limit")
        assert e.limit_applicable is False

    def test_limit_entries_list_length(self):
        assert len(self.track.limit_entries) == N_LIMIT_TYPES_TESTED

    def test_three_primary_limits(self):
        primaries = [lt for lt in self.track.limit_entries if lt.limit_role == "primary"]
        assert len(primaries) == 3

    def test_two_secondary_limits(self):
        secondaries = [lt for lt in self.track.limit_entries if lt.limit_role == "secondary"]
        assert len(secondaries) == 2

    def test_two_not_applicable_limits(self):
        na = [lt for lt in self.track.limit_entries if lt.limit_role == "not_applicable"]
        assert len(na) == 2


# ================================================================
# TestTrackEEquationRecovery — ~12 tests
# ================================================================

class TestTrackEEquationRecovery:
    def setup_method(self):
        self.track = _build_track_e()

    def test_target_equation(self):
        assert self.track.target_equation == "tau * dPhi/dt + Phi = X"

    def test_recovered_equation(self):
        assert self.track.recovered_equation == "tau * d<Phi_hat>/dt + <Phi_hat> = <X_hat>"

    def test_recovery_classification(self):
        assert self.track.recovery_classification == "effective_regime_constitutive_recovery"

    def test_corrections_present_false(self):
        assert self.track.corrections_present is False

    def test_recovery_status(self):
        assert self.track.recovery_status == "effective_regime_constitutive_recovery_demonstrated"

    def test_recovery_conditions_count(self):
        assert len(self.track.recovery_conditions) == 5

    def test_recovery_status_in_allowed_verdicts(self):
        assert self.track.recovery_status in ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS

    def test_target_equation_contains_tau(self):
        assert "tau" in self.track.target_equation

    def test_recovered_equation_contains_tau(self):
        assert "tau" in self.track.recovered_equation

    def test_target_equation_nonempty(self):
        assert len(self.track.target_equation) > 0

    def test_recovered_equation_nonempty(self):
        assert len(self.track.recovered_equation) > 0

    def test_recovery_conditions_nonempty_items(self):
        for cond in self.track.recovery_conditions:
            assert len(cond) > 0


# ================================================================
# TestTrackFParameterMatching — ~15 tests
# ================================================================

class TestTrackFParameterMatching:
    def setup_method(self):
        self.track = _build_track_f()

    def test_four_parameter_entries(self):
        assert len(self.track.parameter_entries) == 4

    def test_tau_param_present(self):
        tau_p = next(p for p in self.track.parameter_entries if p.parameter_name == "tau")
        assert tau_p is not None

    def test_tau_param_complete(self):
        tau_p = next(p for p in self.track.parameter_entries if p.parameter_name == "tau")
        assert tau_p.match_status == "complete"

    def test_source_x_param_present(self):
        sx = next(p for p in self.track.parameter_entries if p.parameter_name == "source_x")
        assert sx is not None

    def test_source_x_param_partial(self):
        sx = next(p for p in self.track.parameter_entries if p.parameter_name == "source_x")
        assert sx.match_status == "partial"

    def test_damping_coefficient_present(self):
        dc = next(p for p in self.track.parameter_entries if p.parameter_name == "damping_coefficient")
        assert dc is not None

    def test_damping_coefficient_complete(self):
        dc = next(p for p in self.track.parameter_entries if p.parameter_name == "damping_coefficient")
        assert dc.match_status == "complete"

    def test_normalization_scaling_present(self):
        ns = next(p for p in self.track.parameter_entries if p.parameter_name == "normalization_scaling")
        assert ns is not None

    def test_normalization_scaling_underdetermined(self):
        ns = next(p for p in self.track.parameter_entries if p.parameter_name == "normalization_scaling")
        assert ns.match_status == "underdetermined"

    def test_n_complete_equals_two(self):
        assert self.track.n_complete == 2

    def test_n_partial_equals_one(self):
        assert self.track.n_partial == 1

    def test_n_underdetermined_equals_one(self):
        assert self.track.n_underdetermined == 1

    def test_n_blocked_equals_zero(self):
        assert self.track.n_blocked == 0

    def test_extra_free_parameters_count(self):
        assert len(self.track.extra_free_parameters) == 2

    def test_parameter_matching_verdict(self):
        assert self.track.parameter_matching_verdict == "partial_parameter_matching_achieved"

    def test_parameter_matching_verdict_in_allowed(self):
        assert self.track.parameter_matching_verdict in ALLOWED_PARAMETER_MATCHING_VERDICTS


# ================================================================
# TestTrackGRegimeValidity — ~12 tests
# ================================================================

class TestTrackGRegimeValidity:
    def setup_method(self):
        self.track = _build_track_g()

    def test_quasi_static_consistent(self):
        assert self.track.quasi_static_consistent is True

    def test_preferred_frame_consistent(self):
        assert self.track.preferred_frame_consistent is True

    def test_open_system_consistent(self):
        assert self.track.open_system_consistent is True

    def test_low_frequency_long_time_consistent(self):
        assert self.track.low_frequency_long_time_consistent is True

    def test_quarantine_perimeter_respected(self):
        assert self.track.quarantine_perimeter_respected is True

    def test_tau_eff_domain_consistent(self):
        assert self.track.tau_eff_domain_consistent is True

    def test_additional_restrictions_count(self):
        assert len(self.track.additional_restrictions) == 2

    def test_regime_validity_status(self):
        assert self.track.regime_validity_status == "regime_limited_but_internally_consistent"

    def test_regime_validity_status_nonempty(self):
        assert len(self.track.regime_validity_status) > 0

    def test_additional_restrictions_nonempty_items(self):
        for r in self.track.additional_restrictions:
            assert len(r) > 0

    def test_all_six_boolean_flags_true(self):
        flags = [
            self.track.quasi_static_consistent,
            self.track.preferred_frame_consistent,
            self.track.open_system_consistent,
            self.track.low_frequency_long_time_consistent,
            self.track.quarantine_perimeter_respected,
            self.track.tau_eff_domain_consistent,
        ]
        assert all(flags)

    def test_regime_status_contains_internally_consistent(self):
        assert "internally_consistent" in self.track.regime_validity_status


# ================================================================
# TestTrackHCrosscheck — ~12 tests
# ================================================================

class TestTrackHCrosscheck:
    def setup_method(self):
        self.track = _build_track_h()

    def test_three_secondary_entries(self):
        assert len(self.track.secondary_entries) == 3

    def test_secondary_entries_count_matches_constant(self):
        assert len(self.track.secondary_entries) == N_SECONDARY_CLASSES_TESTED

    def test_cl3_present(self):
        cl3 = next(c for c in self.track.secondary_entries if c.class_id == "CL3")
        assert cl3 is not None

    def test_cl3_does_not_outperform_lindblad(self):
        cl3 = next(c for c in self.track.secondary_entries if c.class_id == "CL3")
        assert cl3.outperforms_lindblad is False

    def test_cl4_present(self):
        cl4 = next(c for c in self.track.secondary_entries if c.class_id == "CL4")
        assert cl4 is not None

    def test_cl4_does_not_outperform_lindblad(self):
        cl4 = next(c for c in self.track.secondary_entries if c.class_id == "CL4")
        assert cl4.outperforms_lindblad is False

    def test_cl5_present(self):
        cl5 = next(c for c in self.track.secondary_entries if c.class_id == "CL5")
        assert cl5 is not None

    def test_cl5_does_not_outperform_lindblad(self):
        cl5 = next(c for c in self.track.secondary_entries if c.class_id == "CL5")
        assert cl5.outperforms_lindblad is False

    def test_any_class_outperforms_lindblad_false(self):
        assert self.track.any_class_outperforms_lindblad is False

    def test_preferred_class_retention_verdict(self):
        assert self.track.preferred_class_retention_verdict == "lindbladian_preference_retained"

    def test_preferred_class_retention_verdict_in_allowed(self):
        assert self.track.preferred_class_retention_verdict in ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS

    def test_all_secondary_entries_do_not_outperform(self):
        assert all(not c.outperforms_lindblad for c in self.track.secondary_entries)


# ================================================================
# TestTrackIAppendixP — ~10 tests
# ================================================================

class TestTrackIAppendixP:
    def setup_method(self):
        self.track = _build_track_i()

    def test_n_entries_equals_five(self):
        assert self.track.n_entries == 5

    def test_entries_list_length(self):
        assert len(self.track.entries) == 5

    def test_overall_class(self):
        assert self.track.overall_class == "motivated_but_unbuilt"

    def test_no_native_canon(self):
        assert self.track.no_native_canon is True

    def test_overall_class_in_allowed_appendix_p_classes(self):
        assert self.track.overall_class in ALLOWED_APPENDIX_P_CLASSES

    def test_all_entry_classes_in_allowed(self):
        for entry in self.track.entries:
            assert entry.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_classical_observable_map_entry_present(self):
        ids = [e.item_id for e in self.track.entries]
        assert any("classical_observable_map" in item_id for item_id in ids)

    def test_source_mapping_entry_present(self):
        ids = [e.item_id for e in self.track.entries]
        assert any("source_mapping" in item_id for item_id in ids)

    def test_tau_matching_entry_present(self):
        ids = [e.item_id for e in self.track.entries]
        assert any("tau_matching" in item_id for item_id in ids)

    def test_no_native_canon_is_bool(self):
        assert isinstance(self.track.no_native_canon, bool)


# ================================================================
# TestTrackJAuthorization — ~8 tests
# ================================================================

class TestTrackJAuthorization:
    def setup_method(self):
        self.track = _build_track_j()

    def test_qd_authorized_true(self):
        assert self.track.qd_authorized is True

    def test_preconditions_satisfied_count(self):
        assert len(self.track.preconditions_satisfied) >= 3

    def test_qd_constraints_count(self):
        assert len(self.track.qd_constraints) >= 3

    def test_authorization_verdict(self):
        assert self.track.authorization_verdict == "authorized_to_proceed_to_QD"

    def test_authorization_verdict_in_allowed(self):
        assert self.track.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_preconditions_satisfied_nonempty_items(self):
        for p in self.track.preconditions_satisfied:
            assert len(p) > 0

    def test_qd_constraints_nonempty_items(self):
        for c in self.track.qd_constraints:
            assert len(c) > 0

    def test_qd_authorized_is_bool(self):
        assert isinstance(self.track.qd_authorized, bool)


# ================================================================
# TestTrackKNonclaims — ~8 tests
# ================================================================

class TestTrackKNonclaims:
    def setup_method(self):
        self.track = _build_track_k()

    def test_n_nonclaims(self):
        assert self.track.n_nonclaims == N_QC5_NONCLAIMS

    def test_n_nonclaims_equals_eight(self):
        assert self.track.n_nonclaims == 8

    def test_nonclaims_list_length(self):
        assert len(self.track.nonclaims) == 8

    def test_all_registered(self):
        assert self.track.all_registered is True

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in self.track.nonclaims:
            assert nc.startswith("NOT_claiming_"), f"Nonclaim does not start with NOT_claiming_: {nc}"

    def test_nonclaims_are_strings(self):
        for nc in self.track.nonclaims:
            assert isinstance(nc, str)

    def test_all_registered_is_bool(self):
        assert isinstance(self.track.all_registered, bool)

    def test_no_duplicate_nonclaims(self):
        assert len(set(self.track.nonclaims)) == len(self.track.nonclaims)


# ================================================================
# TestHardGatedVerdicts — ~10 tests
# ================================================================

class TestHardGatedVerdicts:
    def test_constitutive_recovery_verdict_exact(self):
        assert QC5_CONSTITUTIVE_RECOVERY_VERDICT == "effective_regime_constitutive_recovery_demonstrated"

    def test_parameter_matching_verdict_exact(self):
        assert QC5_PARAMETER_MATCHING_VERDICT == "partial_parameter_matching_achieved"

    def test_preferred_class_retention_verdict_exact(self):
        assert QC5_PREFERRED_CLASS_RETENTION_VERDICT == "lindbladian_preference_retained"

    def test_authorization_verdict_exact(self):
        assert QC5_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QD"

    def test_overall_appendix_p_class_exact(self):
        assert QC5_OVERALL_APPENDIX_P_CLASS == "motivated_but_unbuilt"

    def test_constitutive_recovery_verdict_in_allowed(self):
        assert QC5_CONSTITUTIVE_RECOVERY_VERDICT in ALLOWED_CONSTITUTIVE_RECOVERY_VERDICTS

    def test_parameter_matching_verdict_in_allowed(self):
        assert QC5_PARAMETER_MATCHING_VERDICT in ALLOWED_PARAMETER_MATCHING_VERDICTS

    def test_preferred_class_retention_verdict_in_allowed(self):
        assert QC5_PREFERRED_CLASS_RETENTION_VERDICT in ALLOWED_PREFERRED_CLASS_RETENTION_VERDICTS

    def test_authorization_verdict_in_allowed(self):
        assert QC5_AUTHORIZATION_VERDICT in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_four_verdict_strings_distinct(self):
        verdicts = {
            QC5_CONSTITUTIVE_RECOVERY_VERDICT,
            QC5_PARAMETER_MATCHING_VERDICT,
            QC5_PREFERRED_CLASS_RETENTION_VERDICT,
            QC5_AUTHORIZATION_VERDICT,
        }
        assert len(verdicts) == 4


# ================================================================
# TestMasterAudit — ~15 tests
# ================================================================

class TestMasterAudit:
    def setup_method(self):
        self.result = run_qc5_classical_limit_audit()

    def test_valid_true(self):
        assert self.result.valid is True

    def test_constitutive_recovery_verdict(self):
        assert self.result.constitutive_recovery_verdict == "effective_regime_constitutive_recovery_demonstrated"

    def test_parameter_matching_verdict(self):
        assert self.result.parameter_matching_verdict == "partial_parameter_matching_achieved"

    def test_preferred_class_retention_verdict(self):
        assert self.result.preferred_class_retention_verdict == "lindbladian_preference_retained"

    def test_authorization_verdict(self):
        assert self.result.authorization_verdict == "authorized_to_proceed_to_QD"

    def test_qc5_appendix_p_class(self):
        assert self.result.qc5_appendix_p_class == "motivated_but_unbuilt"

    def test_diagnostics_tau_sq(self):
        assert abs(self.result.diagnostics["tau_sq"] - 1.5) < 1e-12

    def test_diagnostics_gamma_tau_product(self):
        assert abs(self.result.diagnostics["gamma_tau_product"] - 1.0) < 1e-10

    def test_diagnostics_n_nonclaims(self):
        assert self.result.diagnostics["n_nonclaims"] == 8

    def test_track_a_observable_audit_present(self):
        assert self.result.track_a_observable_audit is not None

    def test_track_b_source_mapping_present(self):
        assert self.result.track_b_source_mapping is not None

    def test_track_c_tau_mapping_present(self):
        assert self.result.track_c_tau_mapping is not None

    def test_track_d_limit_type_present(self):
        assert self.result.track_d_limit_type is not None

    def test_track_e_equation_recovery_present(self):
        assert self.result.track_e_equation_recovery is not None

    def test_track_f_parameter_matching_present(self):
        assert self.result.track_f_parameter_matching is not None

    def test_track_g_regime_validity_present(self):
        assert self.result.track_g_regime_validity is not None

    def test_track_h_crosscheck_present(self):
        assert self.result.track_h_crosscheck is not None

    def test_track_i_appendix_p_present(self):
        assert self.result.track_i_appendix_p is not None

    def test_track_j_authorization_present(self):
        assert self.result.track_j_authorization is not None

    def test_track_k_nonclaims_present(self):
        assert self.result.track_k_nonclaims is not None

    def test_idempotency_valid(self):
        result2 = run_qc5_classical_limit_audit()
        assert result2.valid == self.result.valid

    def test_idempotency_authorization_verdict(self):
        result2 = run_qc5_classical_limit_audit()
        assert result2.authorization_verdict == self.result.authorization_verdict

    def test_idempotency_constitutive_recovery_verdict(self):
        result2 = run_qc5_classical_limit_audit()
        assert result2.constitutive_recovery_verdict == self.result.constitutive_recovery_verdict

    def test_track_a_n_candidates_via_result(self):
        assert self.result.track_a_observable_audit.n_candidates == 6

    def test_track_k_n_nonclaims_via_result(self):
        assert self.result.track_k_nonclaims.n_nonclaims == 8
