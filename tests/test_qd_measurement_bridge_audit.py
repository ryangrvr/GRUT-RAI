"""
Tests for grut/qd_measurement_bridge_audit.py
Q-D Measurement Bridge Audit — full pytest suite (~180 tests, 14 classes)
"""

import math
import pytest

from grut.qd_measurement_bridge_audit import (
    # Constants
    TAU_SQ,
    TAU,
    GAMMA,
    PHI_MINUS_GROWTH_RATE_SIGN,
    PHI_MINUS_CAN_BE_IMAGINARY_PART,
    N_POINTER_BASIS_CANDIDATES,
    N_VIABLE_POINTER_BASES,
    N_OUTCOME_SELECTION_MECHANISMS,
    N_OUTCOME_MECHANISMS_PRESENT,
    N_QD_NONCLAIMS,
    QD_DECOHERENCE_VERDICT,
    QD_POINTER_VERDICT,
    QD_MEASUREMENT_SCOPE_VERDICT,
    QD_OUTCOME_SELECTION_VERDICT,
    QD_AUTHORIZATION_VERDICT,
    QD_OVERALL_APPENDIX_P_CLASS,
    QC_INHERITED_LAW_CLASS,
    QC5_INHERITED_RECOVERY,
    QC5_INHERITED_AUTHORIZATION,
    # Allowed frozensets
    ALLOWED_DECOHERENCE_VERDICTS,
    ALLOWED_POINTER_VERDICTS,
    ALLOWED_MEASUREMENT_SCOPE_VERDICTS,
    ALLOWED_OUTCOME_SELECTION_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    # Main function
    run_qd_measurement_bridge_audit,
)


# ---------------------------------------------------------------------------
# Module-level fixture — run once, shared across all classes
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def result():
    return run_qd_measurement_bridge_audit()


# ===========================================================================
# 1. TestQDConstants
# ===========================================================================

class TestQDConstants:
    def test_tau_sq_value(self):
        assert TAU_SQ == 1.5

    def test_tau_sq_exact_fraction(self):
        assert TAU_SQ == 3.0 / 2.0

    def test_tau_value(self):
        assert TAU == math.sqrt(1.5)

    def test_gamma_value(self):
        assert GAMMA == 1.0 / math.sqrt(1.5)

    def test_gamma_tau_product_is_one(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-10

    def test_phi_minus_growth_rate_sign(self):
        assert PHI_MINUS_GROWTH_RATE_SIGN == +1

    def test_phi_minus_growth_rate_sign_is_int(self):
        assert isinstance(PHI_MINUS_GROWTH_RATE_SIGN, int)

    def test_phi_minus_can_be_imaginary_part_is_false(self):
        assert PHI_MINUS_CAN_BE_IMAGINARY_PART is False

    def test_phi_minus_can_be_imaginary_part_is_bool(self):
        assert isinstance(PHI_MINUS_CAN_BE_IMAGINARY_PART, bool)

    def test_n_pointer_basis_candidates(self):
        assert N_POINTER_BASIS_CANDIDATES == 5

    def test_n_viable_pointer_bases(self):
        assert N_VIABLE_POINTER_BASES == 1

    def test_n_outcome_selection_mechanisms(self):
        assert N_OUTCOME_SELECTION_MECHANISMS == 4

    def test_n_outcome_mechanisms_present(self):
        assert N_OUTCOME_MECHANISMS_PRESENT == 0

    def test_n_qd_nonclaims(self):
        assert N_QD_NONCLAIMS == 8

    def test_decoherence_verdict_nonempty(self):
        assert isinstance(QD_DECOHERENCE_VERDICT, str) and len(QD_DECOHERENCE_VERDICT) > 0

    def test_pointer_verdict_nonempty(self):
        assert isinstance(QD_POINTER_VERDICT, str) and len(QD_POINTER_VERDICT) > 0

    def test_measurement_scope_verdict_nonempty(self):
        assert isinstance(QD_MEASUREMENT_SCOPE_VERDICT, str) and len(QD_MEASUREMENT_SCOPE_VERDICT) > 0

    def test_outcome_selection_verdict_nonempty(self):
        assert isinstance(QD_OUTCOME_SELECTION_VERDICT, str) and len(QD_OUTCOME_SELECTION_VERDICT) > 0

    def test_authorization_verdict_nonempty(self):
        assert isinstance(QD_AUTHORIZATION_VERDICT, str) and len(QD_AUTHORIZATION_VERDICT) > 0

    def test_decoherence_verdict_in_allowed(self):
        assert QD_DECOHERENCE_VERDICT in ALLOWED_DECOHERENCE_VERDICTS

    def test_pointer_verdict_in_allowed(self):
        assert QD_POINTER_VERDICT in ALLOWED_POINTER_VERDICTS

    def test_measurement_scope_verdict_in_allowed(self):
        assert QD_MEASUREMENT_SCOPE_VERDICT in ALLOWED_MEASUREMENT_SCOPE_VERDICTS

    def test_outcome_selection_verdict_in_allowed(self):
        assert QD_OUTCOME_SELECTION_VERDICT in ALLOWED_OUTCOME_SELECTION_VERDICTS

    def test_authorization_verdict_in_allowed(self):
        assert QD_AUTHORIZATION_VERDICT in ALLOWED_AUTHORIZATION_VERDICTS

    def test_qc_inherited_law_class(self):
        assert QC_INHERITED_LAW_CLASS == "lindbladian_like_law_preferred"

    def test_qc5_inherited_recovery_contains_effective_regime(self):
        assert "effective_regime" in QC5_INHERITED_RECOVERY

    def test_qc5_inherited_authorization(self):
        assert QC5_INHERITED_AUTHORIZATION == "authorized_to_proceed_to_QD"

    def test_qd_overall_appendix_p_class(self):
        assert QD_OVERALL_APPENDIX_P_CLASS == "motivated_but_unbuilt"

    def test_allowed_decoherence_verdicts_length(self):
        assert len(ALLOWED_DECOHERENCE_VERDICTS) >= 4

    def test_allowed_pointer_verdicts_length(self):
        assert len(ALLOWED_POINTER_VERDICTS) >= 4

    def test_allowed_measurement_scope_verdicts_length(self):
        assert len(ALLOWED_MEASUREMENT_SCOPE_VERDICTS) >= 5

    def test_allowed_outcome_selection_verdicts_length(self):
        assert len(ALLOWED_OUTCOME_SELECTION_VERDICTS) >= 4

    def test_allowed_authorization_verdicts_length(self):
        assert len(ALLOWED_AUTHORIZATION_VERDICTS) >= 4


# ===========================================================================
# 2. TestTrackADecoherence
# ===========================================================================

class TestTrackADecoherence:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_a_decoherence

    def test_off_diagonal_decay_formula_has_phi_m(self):
        assert "phi_m" in self.track.off_diagonal_decay_rate_formula

    def test_off_diagonal_decay_formula_has_phi_n(self):
        assert "phi_n" in self.track.off_diagonal_decay_rate_formula

    def test_off_diagonal_decay_formula_has_gamma(self):
        assert "gamma" in self.track.off_diagonal_decay_rate_formula

    def test_decoherence_basis(self):
        assert self.track.decoherence_basis == "eigenbasis_of_Phi_hat"

    def test_decoherence_regime_conditions_length(self):
        assert len(self.track.decoherence_regime_conditions) >= 3

    def test_decoherence_regime_conditions_first_markovian(self):
        assert "markovian" in self.track.decoherence_regime_conditions[0].lower()

    def test_decoherence_status(self):
        assert self.track.decoherence_status == "demonstrated_in_effective_regime"

    def test_decoherence_verdict_value(self):
        assert self.track.decoherence_verdict == "effective_regime_decoherence_demonstrated"

    def test_decoherence_verdict_in_allowed(self):
        assert self.track.decoherence_verdict in ALLOWED_DECOHERENCE_VERDICTS

    def test_notes_length(self):
        assert len(self.track.notes) >= 5

    def test_notes_contain_decay(self):
        assert any("decay" in note.lower() for note in self.track.notes)

    def test_notes_contain_diagonal(self):
        assert any("diagonal" in note.lower() for note in self.track.notes)

    def test_notes_reference_formula_or_fraction(self):
        combined = " ".join(self.track.notes)
        assert "1/2" in combined or "1/tau" in combined or "0.5" in combined or "formula" in combined.lower()

    def test_decoherence_status_contains_demonstrated(self):
        assert "demonstrated" in self.track.decoherence_status

    def test_decoherence_verdict_matches_constant(self):
        assert self.track.decoherence_verdict == QD_DECOHERENCE_VERDICT


# ===========================================================================
# 3. TestTrackBPointerCandidates
# ===========================================================================

class TestTrackBPointerCandidates:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_b_pointer_basis
        self.candidates = self.track.candidates

    def test_candidates_count(self):
        assert len(self.candidates) == 5

    def test_pb1_basis_id_prefix(self):
        assert self.candidates[0].basis_id.startswith("PB1")

    def test_pb2_basis_id_prefix(self):
        assert self.candidates[1].basis_id.startswith("PB2")

    def test_pb3_basis_id_prefix(self):
        assert self.candidates[2].basis_id.startswith("PB3")

    def test_pb4_basis_id_prefix(self):
        assert self.candidates[3].basis_id.startswith("PB4")

    def test_pb5_basis_id_prefix(self):
        assert self.candidates[4].basis_id.startswith("PB5")

    def test_pb1_viable_true(self):
        assert self.candidates[0].viable is True

    def test_pb2_viable_false(self):
        assert self.candidates[1].viable is False

    def test_pb3_viable_true(self):
        assert self.candidates[2].viable is True

    def test_pb4_viable_false(self):
        assert self.candidates[3].viable is False

    def test_pb5_viable_false(self):
        assert self.candidates[4].viable is False

    def test_n_viable_via_analysis_field(self):
        # n_viable=1 reflects one class counted once even though PB1 and PB3 are both viable
        assert self.track.n_viable == 1

    def test_pb3_appendix_p_class(self):
        assert self.candidates[2].appendix_p_class == "motivated_but_unbuilt"

    def test_pb5_appendix_p_class(self):
        assert self.candidates[4].appendix_p_class == "bounded_structural_result"

    def test_pb1_or_pb3_notes_mention_same_or_dynamical_or_canonical(self):
        pb1_notes = " ".join(self.candidates[0].notes)
        pb3_notes = " ".join(self.candidates[2].notes)
        combined = pb1_notes + " " + pb3_notes
        assert "same" in combined.lower() or "dynamical" in combined.lower() or "canonical" in combined.lower()

    def test_pb3_selection_mechanism_dynamical_or_jump_operator(self):
        mech = self.candidates[2].selection_mechanism
        assert "jump_operator" in mech or "dynamical" in mech


# ===========================================================================
# 4. TestTrackBPointerAudit
# ===========================================================================

class TestTrackBPointerAudit:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_b_pointer_basis

    def test_n_candidates(self):
        assert self.track.n_candidates == 5

    def test_n_viable(self):
        assert self.track.n_viable == 1

    def test_chosen_pointer_basis_id(self):
        assert self.track.chosen_pointer_basis_id == "PB3_jump_operator_eigenbasis"

    def test_chosen_pointer_basis_name_nonempty(self):
        assert len(self.track.chosen_pointer_basis_name) > 0

    def test_unique_basis_false(self):
        assert self.track.unique_basis is False

    def test_pointer_verdict_value(self):
        assert self.track.pointer_verdict == "pointer_basis_class_selected"

    def test_pointer_verdict_in_allowed(self):
        assert self.track.pointer_verdict in ALLOWED_POINTER_VERDICTS

    def test_notes_mention_pb1_and_pb3(self):
        combined = " ".join(self.track.notes)
        assert "PB1" in combined and "PB3" in combined

    def test_notes_mention_n_viable_or_one_or_1(self):
        combined = " ".join(self.track.notes)
        assert "n_viable" in combined or "one" in combined.lower() or "=1" in combined or " 1 " in combined

    def test_pointer_verdict_matches_constant(self):
        assert self.track.pointer_verdict == QD_POINTER_VERDICT


# ===========================================================================
# 5. TestTrackCTimescale
# ===========================================================================

class TestTrackCTimescale:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_c_timescale

    def test_decoherence_rate_formula_has_gamma_or_tau(self):
        formula = self.track.decoherence_rate_formula
        assert "gamma" in formula or "tau" in formula

    def test_decoherence_timescale_formula_has_tau(self):
        assert "tau" in self.track.decoherence_timescale_formula

    def test_timescale_governed_by_tau_and_separation(self):
        tgb = self.track.timescale_governed_by
        assert "tau" in tgb and ("eigenvalue" in tgb or "separation" in tgb)

    def test_tau_sq_value(self):
        assert abs(self.track.tau_sq_value - 1.5) < 1e-10

    def test_gamma_value(self):
        assert abs(self.track.gamma_value - GAMMA) < 1e-10

    def test_characteristic_timescale_contains_tau(self):
        ct = self.track.characteristic_decoherence_timescale
        assert "tau" in ct or "sqrt(2)" in ct

    def test_consistent_with_prior_timescales(self):
        assert self.track.consistent_with_prior_timescales is True

    def test_notes_length(self):
        assert len(self.track.notes) >= 5

    def test_notes_reference_sqrt2_or_delta_phi(self):
        combined = " ".join(self.track.notes)
        assert "sqrt(2)" in combined or "sqrt_2" in combined or "√2" in combined or "delta_phi" in combined

    def test_notes_mention_gamma_tau_product(self):
        combined = " ".join(self.track.notes)
        assert "gamma" in combined or "gamma_tau" in combined or "1/tau" in combined

    def test_decoherence_rate_formula_references_delta_phi_or_eigenvalue(self):
        formula = self.track.decoherence_rate_formula
        assert "delta_phi" in formula or "phi_m" in formula

    def test_timescale_governed_by_not_tau_only(self):
        assert self.track.timescale_governed_by != "tau_only"


# ===========================================================================
# 6. TestTrackDMeasurementBridge
# ===========================================================================

class TestTrackDMeasurementBridge:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_d_measurement_bridge

    def test_entries_count(self):
        assert len(self.track.entries) == 5

    def test_decoherence_achieved(self):
        assert self.track.decoherence_achieved is True

    def test_pointer_structure_achieved(self):
        assert self.track.pointer_structure_achieved is True

    def test_partial_determination_not_achieved(self):
        assert self.track.partial_determination_achieved is False

    def test_full_measurement_not_achieved(self):
        assert self.track.full_measurement_achieved is False

    def test_born_rule_not_achieved(self):
        assert self.track.born_rule_achieved is False

    def test_measurement_scope_verdict_value(self):
        assert self.track.measurement_scope_verdict == "decoherence_plus_pointer_structure"

    def test_measurement_scope_verdict_in_allowed(self):
        assert self.track.measurement_scope_verdict in ALLOWED_MEASUREMENT_SCOPE_VERDICTS

    def test_at_least_two_entries_achieved(self):
        count = sum(1 for e in self.track.entries if e.achieved)
        assert count >= 2

    def test_at_least_three_entries_not_achieved(self):
        count = sum(1 for e in self.track.entries if not e.achieved)
        assert count >= 3

    def test_notes_contain_boundary_language(self):
        combined = " ".join(self.track.notes)
        assert "NOT" in combined or "does not" in combined.lower() or "absent" in combined.lower()

    def test_measurement_scope_verdict_matches_constant(self):
        assert self.track.measurement_scope_verdict == QD_MEASUREMENT_SCOPE_VERDICT


# ===========================================================================
# 7. TestTrackEOutcomeSelection
# ===========================================================================

class TestTrackEOutcomeSelection:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_e_outcome_selection

    def test_mechanisms_count(self):
        assert len(self.track.mechanisms) == 4

    def test_n_mechanisms(self):
        assert self.track.n_mechanisms == 4

    def test_n_present(self):
        assert self.track.n_present == 0

    def test_any_outcome_selection_present_false(self):
        assert self.track.any_outcome_selection_present is False

    def test_outcome_selection_verdict_value(self):
        assert self.track.outcome_selection_verdict == "born_rule_or_outcome_selection_not_natively_derived"

    def test_outcome_selection_verdict_in_allowed(self):
        assert self.track.outcome_selection_verdict in ALLOWED_OUTCOME_SELECTION_VERDICTS

    def test_all_mechanisms_not_present(self):
        assert all(not m.present for m in self.track.mechanisms)

    def test_all_mechanisms_appendix_p_class_valid(self):
        for m in self.track.mechanisms:
            assert m.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_born_rule_mechanism_not_present(self):
        born_rule = [m for m in self.track.mechanisms if "born_rule" in m.mechanism_name]
        if born_rule:
            assert born_rule[0].present is False

    def test_single_outcome_mechanism_not_present(self):
        single = [m for m in self.track.mechanisms if "single_outcome" in m.mechanism_name]
        if single:
            assert single[0].present is False

    def test_notes_length(self):
        assert len(self.track.notes) >= 3

    def test_outcome_selection_verdict_matches_constant(self):
        assert self.track.outcome_selection_verdict == QD_OUTCOME_SELECTION_VERDICT


# ===========================================================================
# 8. TestTrackFObservableClassicality
# ===========================================================================

class TestTrackFObservableClassicality:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_f_observable_classicality

    def test_constitutive_observable(self):
        assert self.track.constitutive_observable == "Phi_hat"

    def test_pointer_observable_contains_phi_hat(self):
        assert "Phi_hat" in self.track.pointer_observable

    def test_same_observable_true(self):
        assert self.track.same_observable is True

    def test_strength_of_identification_conditional(self):
        assert "conditional" in self.track.strength_of_identification.lower()

    def test_strength_of_identification_references_qc5_or_jump_operator(self):
        s = self.track.strength_of_identification
        assert "QC5" in s or "Q-C.5" in s or "jump_operator" in s

    def test_classicality_verdict_contains_conditionally(self):
        assert "conditionally" in self.track.classicality_verdict.lower() or "conditional" in self.track.classicality_verdict.lower()

    def test_appendix_p_class(self):
        assert self.track.appendix_p_class == "motivated_but_unbuilt"

    def test_notes_length(self):
        assert len(self.track.notes) >= 4

    def test_notes_contain_conditional_or_not_independently(self):
        combined = " ".join(self.track.notes)
        assert "conditional" in combined.lower() or "NOT independently" in combined

    def test_notes_mention_l_change_breaks_coincidence(self):
        combined = " ".join(self.track.notes)
        assert "L" in combined and ("changed" in combined.lower() or "break" in combined.lower() or "if" in combined.lower())


# ===========================================================================
# 9. TestTrackGAppendixP
# ===========================================================================

class TestTrackGAppendixP:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_g_appendix_p

    def test_n_entries(self):
        assert self.track.n_entries == 5

    def test_overall_class(self):
        assert self.track.overall_class == "motivated_but_unbuilt"

    def test_no_native_canon(self):
        assert self.track.no_native_canon is True

    def test_all_entries_appendix_p_class_valid(self):
        for e in self.track.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_at_least_three_entries_mbu(self):
        mbu_count = sum(1 for e in self.track.entries if e.appendix_p_class == "motivated_but_unbuilt")
        assert mbu_count >= 3

    def test_at_least_one_entry_bsr(self):
        bsr_count = sum(1 for e in self.track.entries if e.appendix_p_class == "bounded_structural_result")
        assert bsr_count >= 1

    def test_all_entries_have_allowed_claim(self):
        for e in self.track.entries:
            assert isinstance(e.allowed_claim, str) and len(e.allowed_claim) > 0

    def test_all_entries_have_forbidden_claim(self):
        for e in self.track.entries:
            assert isinstance(e.forbidden_claim, str) and len(e.forbidden_claim) > 0

    def test_notes_length(self):
        assert len(self.track.notes) >= 1

    def test_entries_count_matches_n_entries(self):
        assert len(self.track.entries) == self.track.n_entries


# ===========================================================================
# 10. TestTrackHAuthorization
# ===========================================================================

class TestTrackHAuthorization:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_h_authorization

    def test_qe_authorized_true(self):
        assert self.track.qe_authorized is True

    def test_preconditions_satisfied_length(self):
        assert len(self.track.preconditions_satisfied) >= 3

    def test_qe_constraints_length(self):
        assert len(self.track.qe_constraints) >= 3

    def test_authorization_verdict_value(self):
        assert self.track.authorization_verdict == "authorized_to_proceed_to_QE"

    def test_authorization_verdict_in_allowed(self):
        assert self.track.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_any_constraint_mentions_born_rule(self):
        combined = " ".join(self.track.qe_constraints)
        assert "Born_rule" in combined or "born_rule" in combined

    def test_any_constraint_mentions_mbu_or_floor_or_measurement_closure(self):
        combined = " ".join(self.track.qe_constraints)
        assert "MBU" in combined or "floor" in combined or "measurement_closure" in combined or "full_measurement" in combined

    def test_authorization_verdict_matches_constant(self):
        assert self.track.authorization_verdict == QD_AUTHORIZATION_VERDICT


# ===========================================================================
# 11. TestTrackINonclaims
# ===========================================================================

class TestTrackINonclaims:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.track = result.track_i_nonclaims

    def test_n_nonclaims(self):
        assert self.track.n_nonclaims == 8

    def test_nonclaims_list_length(self):
        assert len(self.track.nonclaims) == 8

    def test_all_registered_true(self):
        assert self.track.all_registered is True

    def test_all_nonclaims_start_with_not_claiming(self):
        for nc in self.track.nonclaims:
            assert nc.startswith("NOT_claiming_"), f"Nonclaim does not start with NOT_claiming_: {nc!r}"

    def test_at_least_one_nonclaim_mentions_collapse(self):
        assert any("collapse" in nc.lower() for nc in self.track.nonclaims)

    def test_at_least_one_nonclaim_mentions_born_rule_or_probabilities(self):
        assert any("Born_rule" in nc or "probabilities" in nc for nc in self.track.nonclaims)

    def test_at_least_one_nonclaim_mentions_ontology(self):
        assert any("ontology" in nc.lower() or "ontological" in nc.lower() for nc in self.track.nonclaims)

    def test_n_nonclaims_matches_list_length(self):
        assert self.track.n_nonclaims == len(self.track.nonclaims)


# ===========================================================================
# 12. TestHardGatedVerdicts
# ===========================================================================

class TestHardGatedVerdicts:
    def test_decoherence_verdict_on_result(self, result):
        assert result.decoherence_verdict == "effective_regime_decoherence_demonstrated"

    def test_pointer_verdict_on_result(self, result):
        assert result.pointer_verdict == "pointer_basis_class_selected"

    def test_measurement_scope_verdict_on_result(self, result):
        assert result.measurement_scope_verdict == "decoherence_plus_pointer_structure"

    def test_outcome_selection_verdict_on_result(self, result):
        assert result.outcome_selection_verdict == "born_rule_or_outcome_selection_not_natively_derived"

    def test_authorization_verdict_on_result(self, result):
        assert result.authorization_verdict == "authorized_to_proceed_to_QE"

    def test_decoherence_verdict_in_allowed(self, result):
        assert result.decoherence_verdict in ALLOWED_DECOHERENCE_VERDICTS

    def test_pointer_verdict_in_allowed(self, result):
        assert result.pointer_verdict in ALLOWED_POINTER_VERDICTS

    def test_measurement_scope_verdict_in_allowed(self, result):
        assert result.measurement_scope_verdict in ALLOWED_MEASUREMENT_SCOPE_VERDICTS

    def test_outcome_selection_verdict_in_allowed(self, result):
        assert result.outcome_selection_verdict in ALLOWED_OUTCOME_SELECTION_VERDICTS

    def test_authorization_verdict_in_allowed(self, result):
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_five_verdicts_are_distinct(self, result):
        verdicts = [
            result.decoherence_verdict,
            result.pointer_verdict,
            result.measurement_scope_verdict,
            result.outcome_selection_verdict,
            result.authorization_verdict,
        ]
        assert len(verdicts) == len(set(verdicts))

    def test_qd_appendix_p_class_on_result(self, result):
        assert result.qd_appendix_p_class == "motivated_but_unbuilt"


# ===========================================================================
# 13. TestMasterAudit
# ===========================================================================

class TestMasterAudit:
    @pytest.fixture(autouse=True)
    def _setup(self, result):
        self.result = result

    def test_valid_true(self):
        assert self.result.valid is True

    def test_track_a_not_none(self):
        assert self.result.track_a_decoherence is not None

    def test_track_b_not_none(self):
        assert self.result.track_b_pointer_basis is not None

    def test_track_c_not_none(self):
        assert self.result.track_c_timescale is not None

    def test_track_d_not_none(self):
        assert self.result.track_d_measurement_bridge is not None

    def test_track_e_not_none(self):
        assert self.result.track_e_outcome_selection is not None

    def test_track_f_not_none(self):
        assert self.result.track_f_observable_classicality is not None

    def test_track_g_not_none(self):
        assert self.result.track_g_appendix_p is not None

    def test_track_h_not_none(self):
        assert self.result.track_h_authorization is not None

    def test_track_i_not_none(self):
        assert self.result.track_i_nonclaims is not None

    def test_allowed_claims_length(self):
        assert len(self.result.allowed_claims) >= 6

    def test_forbidden_claims_length(self):
        assert len(self.result.forbidden_claims) >= 6

    def test_exact_nonclaims_length(self):
        assert len(self.result.exact_nonclaims) == 8

    def test_all_exact_nonclaims_start_with_not_claiming(self):
        for nc in self.result.exact_nonclaims:
            assert nc.startswith("NOT_claiming_"), f"Unexpected nonclaim prefix: {nc!r}"

    def test_diagnostics_tau_sq(self):
        assert self.result.diagnostics["tau_sq"] == 1.5

    def test_diagnostics_gamma_tau(self):
        assert abs(self.result.diagnostics["gamma_tau"] - 1.0) < 1e-10

    def test_diagnostics_n_outcome_present(self):
        assert self.result.diagnostics["n_outcome_present"] == 0

    def test_diagnostics_n_nonclaims(self):
        assert self.result.diagnostics["n_nonclaims"] == 8

    def test_diagnostics_n_pointer_candidates(self):
        assert self.result.diagnostics["n_pointer_candidates"] == 5

    def test_diagnostics_n_viable_pointer(self):
        assert self.result.diagnostics["n_viable_pointer"] == 1

    def test_diagnostics_has_decoherence_rate_formula(self):
        assert "decoherence_rate_formula" in self.result.diagnostics

    def test_diagnostics_has_decoherence_timescale_formula(self):
        assert "decoherence_timescale_formula" in self.result.diagnostics

    def test_idempotency_valid(self):
        result2 = run_qd_measurement_bridge_audit()
        assert result2.valid is True

    def test_idempotency_decoherence_verdict(self):
        result2 = run_qd_measurement_bridge_audit()
        assert result2.decoherence_verdict == self.result.decoherence_verdict

    def test_idempotency_pointer_verdict(self):
        result2 = run_qd_measurement_bridge_audit()
        assert result2.pointer_verdict == self.result.pointer_verdict

    def test_idempotency_measurement_scope_verdict(self):
        result2 = run_qd_measurement_bridge_audit()
        assert result2.measurement_scope_verdict == self.result.measurement_scope_verdict

    def test_idempotency_authorization_verdict(self):
        result2 = run_qd_measurement_bridge_audit()
        assert result2.authorization_verdict == self.result.authorization_verdict


# ===========================================================================
# 14. TestPhysicsInvariants
# ===========================================================================

class TestPhysicsInvariants:
    def test_gamma_tau_product_is_one(self):
        tau = math.sqrt(1.5)
        gamma = 1.0 / tau
        assert abs(gamma * tau - 1.0) < 1e-10

    def test_decoherence_rate_at_delta_phi_sqrt2_equals_gamma(self, result):
        # R_dec(sqrt(2)) = 0.5 * gamma * (sqrt(2))^2 = 0.5 * gamma * 2 = gamma
        assert abs(result.diagnostics["decoherence_rate_at_delta_phi_sqrt2"] - GAMMA) < 1e-9

    def test_decoherence_timescale_at_delta_phi_sqrt2_equals_tau(self, result):
        # tau_dec(sqrt(2)) = 2 * tau / (sqrt(2))^2 = 2 * tau / 2 = tau
        assert abs(result.diagnostics["decoherence_timescale_at_delta_phi_sqrt2"] - TAU) < 1e-9

    def test_track_c_tau_sq_value(self, result):
        assert result.track_c_timescale.tau_sq_value == 1.5

    def test_track_c_gamma_value(self, result):
        gamma = 1.0 / math.sqrt(1.5)
        assert abs(result.track_c_timescale.gamma_value - gamma) < 1e-10

    def test_decoherence_and_pointer_structure_achieved(self, result):
        bridge = result.track_d_measurement_bridge
        assert bridge.decoherence_achieved and bridge.pointer_structure_achieved

    def test_born_rule_not_achieved(self, result):
        assert not result.track_d_measurement_bridge.born_rule_achieved
