"""
Tests for Appendix Q-II.C --- Entanglement and Nonfactorized Structure Audit
=============================================================================
"""

import math
import pytest

from grut.qiic_entanglement_nonfactorized_audit import (
    TAU_SQ, TAU, GAMMA,
    COMPOSITE_HILBERT_DIM, SINGLE_SYSTEM_DIM,
    MAXIMALLY_ENTANGLED_REDUCED_PURITY, PURE_STATE_PURITY,
    N_STATE_CLASSES, N_FACTORIZATION_LEVELS, N_REDUCED_STATE_TESTS,
    N_WITNESS_CANDIDATES, N_DECOHERENCE_EFFECTS,
    N_BENCHMARK_CANDIDATES, N_BELL_CANDIDATES,
    N_APPENDIX_P_ENTRIES, N_QIIC_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    QIIB_INHERITED_SUBSYSTEM, QIIB_INHERITED_COMPOSITION,
    QIIB_INHERITED_AUTHORIZATION,
    QIIC_NONFACTORIZATION_VERDICT, QIIC_REDUCED_STATE_VERDICT,
    QIIC_WITNESS_VERDICT, QIIC_BELL_BOUNDARY_VERDICT,
    QIIC_AUTHORIZATION_VERDICT, QIIC_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_NONFACTORIZATION_VERDICTS, ALLOWED_REDUCED_STATE_VERDICTS,
    ALLOWED_WITNESS_VERDICTS, ALLOWED_BELL_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    QIIC_NONCLAIMS,
    run_qiic_entanglement_nonfactorized_audit, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiic_entanglement_nonfactorized_audit()


class TestQIICConstants:
    def test_tau_sq(self):
        assert TAU_SQ == 1.5

    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_composite_dim(self):
        assert COMPOSITE_HILBERT_DIM == 4

    def test_max_entangled_purity(self):
        assert abs(MAXIMALLY_ENTANGLED_REDUCED_PURITY - 0.5) < 1e-15

    def test_pure_state_purity(self):
        assert PURE_STATE_PURITY == 1.0

    def test_n_state_classes(self):
        assert N_STATE_CLASSES == 5

    def test_n_nonclaims(self):
        assert N_QIIC_NONCLAIMS == 8

    def test_nonclaims_length(self):
        assert len(QIIC_NONCLAIMS) == N_QIIC_NONCLAIMS

    def test_all_nonclaims_start_not_claiming(self):
        for nc in QIIC_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_verdict_constants(self):
        assert QIIC_NONFACTORIZATION_VERDICT == "nonfactorized_two_subsystem_states_demonstrated"
        assert QIIC_REDUCED_STATE_VERDICT == "reduced_state_entanglement_signatures_available"
        assert QIIC_WITNESS_VERDICT == "separability_or_purity_witness_justified"
        assert QIIC_BELL_BOUNDARY_VERDICT == "bell_nonlocality_not_yet_justified"
        assert QIIC_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QIID"

    def test_frozenset_sizes(self):
        assert len(ALLOWED_NONFACTORIZATION_VERDICTS) == 4
        assert len(ALLOWED_REDUCED_STATE_VERDICTS) == 4
        assert len(ALLOWED_WITNESS_VERDICTS) == 4
        assert len(ALLOWED_BELL_VERDICTS) == 4
        assert len(ALLOWED_AUTHORIZATION_VERDICTS) == 4

    def test_inherited_verdicts(self):
        assert "extension_level" in QIIB_INHERITED_SUBSYSTEM
        assert "extension_level" in QIIB_INHERITED_COMPOSITION
        assert "QIIC" in QIIB_INHERITED_AUTHORIZATION


class TestTrackANonfactorized:
    def test_n_classes(self, result):
        assert result.track_a_nonfactorized.n_classes == N_STATE_CLASSES

    def test_n_admissible(self, result):
        assert result.track_a_nonfactorized.n_admissible == 4

    def test_n_entangled(self, result):
        assert result.track_a_nonfactorized.n_entangled_classes == 2

    def test_sc1_product(self, result):
        sc1 = result.track_a_nonfactorized.state_classes[0]
        assert sc1.admissible is True and sc1.entangled is False

    def test_sc2_classically_correlated(self, result):
        sc2 = result.track_a_nonfactorized.state_classes[1]
        assert sc2.admissible is True and sc2.entangled is False

    def test_sc3_pure_nonfactorized(self, result):
        sc3 = result.track_a_nonfactorized.state_classes[2]
        assert sc3.admissible is True and sc3.entangled is True

    def test_sc4_mixed_nonfactorized(self, result):
        sc4 = result.track_a_nonfactorized.state_classes[3]
        assert sc4.admissible is True and sc4.entangled is True

    def test_sc5_null_rejected(self, result):
        sc5 = result.track_a_nonfactorized.state_classes[4]
        assert sc5.admissible is False

    def test_verdict(self, result):
        assert result.track_a_nonfactorized.nonfactorization_verdict == QIIC_NONFACTORIZATION_VERDICT


class TestTrackBFactorization:
    def test_n_levels(self, result):
        assert result.track_b_factorization.n_levels == N_FACTORIZATION_LEVELS

    def test_fl1_product(self, result):
        assert result.track_b_factorization.levels[0].level_id == "FL1"

    def test_fl3_entangled(self, result):
        fl3 = result.track_b_factorization.levels[2]
        assert fl3.level_id == "FL3"
        assert "nonfactorized" in fl3.level_name.lower() or "entangled" in fl3.level_name.lower()

    def test_boundary_criterion_mentions_ppt(self, result):
        assert "PPT" in result.track_b_factorization.boundary_criterion or \
               "ppt" in result.track_b_factorization.boundary_criterion.lower()


class TestTrackCReducedState:
    def test_n_tests(self, result):
        assert result.track_c_reduced_state.n_tests == N_REDUCED_STATE_TESTS

    def test_all_available(self, result):
        assert result.track_c_reduced_state.n_available == N_REDUCED_STATE_TESTS

    def test_all_quantitative(self, result):
        assert result.track_c_reduced_state.n_quantitative == N_REDUCED_STATE_TESTS

    def test_rst1_purity(self, result):
        rst1 = result.track_c_reduced_state.tests[0]
        assert rst1.available is True and rst1.quantitative is True

    def test_rst4_ppt(self, result):
        rst4 = result.track_c_reduced_state.tests[3]
        assert rst4.available is True
        assert "ppt" in rst4.test_name.lower() or "PPT" in rst4.description

    def test_verdict(self, result):
        assert result.track_c_reduced_state.reduced_state_verdict == QIIC_REDUCED_STATE_VERDICT


class TestTrackDWitness:
    def test_n_candidates(self, result):
        assert result.track_d_witness.n_candidates == N_WITNESS_CANDIDATES

    def test_ew2_justified(self, result):
        ew2 = result.track_d_witness.candidates[1]
        assert ew2.candidate_id == "EW2"
        assert ew2.justified is True

    def test_ew4_bell_not_justified(self, result):
        ew4 = result.track_d_witness.candidates[3]
        assert ew4.candidate_id == "EW4"
        assert ew4.justified is False
        assert "born" in ew4.obstruction_if_not.lower() or "observable" in ew4.obstruction_if_not.lower()

    def test_chosen_ew2(self, result):
        assert "EW2" in result.track_d_witness.justified_candidate_id

    def test_verdict(self, result):
        assert result.track_d_witness.witness_verdict == QIIC_WITNESS_VERDICT


class TestTrackEDecoherence:
    def test_n_effects(self, result):
        assert result.track_e_decoherence.n_effects == N_DECOHERENCE_EFFECTS

    def test_suppressed(self, result):
        assert result.track_e_decoherence.entanglement_suppressed_by_decoherence is True

    def test_interaction_absent(self, result):
        assert result.track_e_decoherence.interaction_hamiltonian_absent is True

    def test_de1_demonstrated(self, result):
        de1 = result.track_e_decoherence.effects[0]
        assert de1.status == "demonstrated"

    def test_de4_gap(self, result):
        de4 = result.track_e_decoherence.effects[3]
        assert de4.status == "gap_documented"


class TestTrackFBenchmark:
    def test_n_candidates(self, result):
        assert result.track_f_benchmark.n_candidates == N_BENCHMARK_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_f_benchmark.n_viable == 2

    def test_chosen_eb1(self, result):
        assert "EB1" in result.track_f_benchmark.chosen_benchmark_id

    def test_eb1_purity(self, result):
        eb1 = result.track_f_benchmark.candidates[0]
        assert abs(eb1.reduced_purity_a - 0.5) < 1e-15

    def test_eb1_no_bell(self, result):
        eb1 = result.track_f_benchmark.candidates[0]
        not_demo = " ".join(eb1.does_not_demonstrate).lower()
        assert "bell" in not_demo

    def test_eb1_no_dynamical(self, result):
        eb1 = result.track_f_benchmark.candidates[0]
        not_demo = " ".join(eb1.does_not_demonstrate).lower()
        assert "dynamical" in not_demo


class TestTrackGBell:
    def test_n_candidates(self, result):
        assert result.track_g_bell.n_candidates == N_BELL_CANDIDATES

    def test_verdict(self, result):
        assert result.track_g_bell.bell_boundary_verdict == QIIC_BELL_BOUNDARY_VERDICT

    def test_missing_prerequisites(self, result):
        assert len(result.track_g_bell.missing_prerequisites) >= 3

    def test_prerequisites_mention_born(self, result):
        text = " ".join(result.track_g_bell.missing_prerequisites).lower()
        assert "born" in text

    def test_prerequisites_mention_observable(self, result):
        text = " ".join(result.track_g_bell.missing_prerequisites).lower()
        assert "observable" in text

    def test_bl3_not_justified(self, result):
        bl3 = result.track_g_bell.candidates[2]
        assert bl3.justified is False

    def test_bl4_not_justified(self, result):
        bl4 = result.track_g_bell.candidates[3]
        assert bl4.justified is False


class TestTrackHAppendixP:
    def test_n_entries(self, result):
        assert result.track_h_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_h_appendix_p.no_native_canon is True

    def test_overall_class(self, result):
        assert result.track_h_appendix_p.overall_class == QIIC_OVERALL_APPENDIX_P_CLASS

    def test_all_classes_valid(self, result):
        for e in result.track_h_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_at_least_one_bsr(self, result):
        n = sum(1 for e in result.track_h_appendix_p.entries
                if e.appendix_p_class == "bounded_structural_result")
        assert n >= 1


class TestTrackIAuthorization:
    def test_authorized(self, result):
        assert result.track_i_authorization.qiid_authorized is True

    def test_verdict(self, result):
        assert result.track_i_authorization.authorization_verdict == QIIC_AUTHORIZATION_VERDICT

    def test_basis_length(self, result):
        assert len(result.track_i_authorization.authorization_basis) >= 3

    def test_constraints_length(self, result):
        assert len(result.track_i_authorization.qiid_constraints) >= 3

    def test_constraints_mention_observable(self, result):
        text = " ".join(result.track_i_authorization.qiid_constraints).lower()
        assert "observable" in text


class TestTrackJNonclaims:
    def test_count(self, result):
        assert result.track_j_nonclaims.n_nonclaims == N_QIIC_NONCLAIMS

    def test_registered(self, result):
        assert result.track_j_nonclaims.all_registered is True

    def test_all_start_not_claiming(self, result):
        for nc in result.track_j_nonclaims.nonclaims:
            assert nc.startswith("NOT_claiming_")

    def test_mentions_bell(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "bell" in text

    def test_mentions_native_canon(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "native_canon" in text or "native canon" in text

    def test_mentions_matter(self, result):
        text = " ".join(result.track_j_nonclaims.nonclaims).lower()
        assert "matter" in text


class TestHardGatedVerdicts:
    def test_nonfactorization_exact(self, result):
        assert result.nonfactorization_verdict == QIIC_NONFACTORIZATION_VERDICT

    def test_reduced_state_exact(self, result):
        assert result.reduced_state_verdict == QIIC_REDUCED_STATE_VERDICT

    def test_witness_exact(self, result):
        assert result.witness_verdict == QIIC_WITNESS_VERDICT

    def test_bell_exact(self, result):
        assert result.bell_boundary_verdict == QIIC_BELL_BOUNDARY_VERDICT

    def test_authorization_exact(self, result):
        assert result.authorization_verdict == QIIC_AUTHORIZATION_VERDICT

    def test_all_in_allowed(self, result):
        assert result.nonfactorization_verdict in ALLOWED_NONFACTORIZATION_VERDICTS
        assert result.reduced_state_verdict in ALLOWED_REDUCED_STATE_VERDICTS
        assert result.witness_verdict in ALLOWED_WITNESS_VERDICTS
        assert result.bell_boundary_verdict in ALLOWED_BELL_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_five_distinct(self, result):
        verdicts = {
            result.nonfactorization_verdict, result.reduced_state_verdict,
            result.witness_verdict, result.bell_boundary_verdict,
            result.authorization_verdict,
        }
        assert len(verdicts) == 5

    def test_appendix_p_class(self, result):
        assert result.qiic_appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks(self, result):
        assert result.track_a_nonfactorized is not None
        assert result.track_b_factorization is not None
        assert result.track_c_reduced_state is not None
        assert result.track_d_witness is not None
        assert result.track_e_decoherence is not None
        assert result.track_f_benchmark is not None
        assert result.track_g_bell is not None
        assert result.track_h_appendix_p is not None
        assert result.track_i_authorization is not None
        assert result.track_j_nonclaims is not None

    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_QIIC_NONCLAIMS

    def test_diagnostics_purity(self, result):
        assert abs(result.diagnostics["maximally_entangled_reduced_purity"] - 0.5) < 1e-15

    def test_diagnostics_suppressed(self, result):
        assert result.diagnostics["entanglement_suppressed_by_decoherence"] is True

    def test_diagnostics_interaction_absent(self, result):
        assert result.diagnostics["interaction_hamiltonian_absent"] is True

    def test_idempotency(self):
        r1 = run_qiic_entanglement_nonfactorized_audit()
        r2 = run_qiic_entanglement_nonfactorized_audit()
        assert r1.valid == r2.valid
        assert r1.nonfactorization_verdict == r2.nonfactorization_verdict

    def test_self_test(self):
        assert _self_test() is True


class TestDoctrinalBoundaries:
    def test_no_bell_claim(self, result):
        for c in result.forbidden_claims:
            if "bell" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim mentions Bell")

    def test_no_native_entanglement(self, result):
        for c in result.forbidden_claims:
            if "native" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about native entanglement")

    def test_no_measurement_from_mixedness(self, result):
        for c in result.forbidden_claims:
            if "measurement" in c.lower() or "born" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about measurement from mixedness")

    def test_entanglement_transient_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "transient" in text or "suppresses" in text

    def test_ppt_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "ppt" in text or "separability" in text or "purity" in text
