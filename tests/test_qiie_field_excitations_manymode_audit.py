"""
Tests for Appendix Q-II.E --- Field Excitations and Many-Mode Structure
=======================================================================
"""

import pytest

from grut.qiie_field_excitations_manymode_audit import (
    TAU, GAMMA, SINGLE_SITE_DIM, TWO_SITE_DIM, N_SITE_BENCHMARK,
    N_ELIGIBILITY_INGREDIENTS, N_MODE_CANDIDATES,
    N_EXCITATION_CANDIDATES, N_PROPAGATION_CANDIDATES,
    N_BENCHMARK_CANDIDATES, N_EXCITATION_CLASS_LEVELS,
    N_CONSTITUTIVE_CHECKS, N_MATTER_LEVELS,
    N_APPENDIX_P_ENTRIES, N_QIIE_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    QIIE_MODE_VERDICT, QIIE_EXCITATION_VERDICT,
    QIIE_PROPAGATION_VERDICT, QIIE_MATTER_BOUNDARY_VERDICT,
    QIIE_AUTHORIZATION_VERDICT, QIIE_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_MODE_VERDICTS, ALLOWED_EXCITATION_VERDICTS,
    ALLOWED_PROPAGATION_VERDICTS, ALLOWED_MATTER_BOUNDARY_VERDICTS,
    ALLOWED_AUTHORIZATION_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    QIIE_NONCLAIMS,
    run_qiie_field_excitations_manymode_audit, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiie_field_excitations_manymode_audit()


class TestQIIEConstants:
    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_dims(self):
        assert SINGLE_SITE_DIM == 2
        assert TWO_SITE_DIM == 4
        assert N_SITE_BENCHMARK == 2

    def test_counts(self):
        assert N_ELIGIBILITY_INGREDIENTS == 5
        assert N_MODE_CANDIDATES == 5
        assert N_EXCITATION_CANDIDATES == 4
        assert N_PROPAGATION_CANDIDATES == 5
        assert N_BENCHMARK_CANDIDATES == 4
        assert N_QIIE_NONCLAIMS == 8

    def test_nonclaims_length(self):
        assert len(QIIE_NONCLAIMS) == N_QIIE_NONCLAIMS

    def test_nonclaims_start(self):
        for nc in QIIE_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_verdicts(self):
        assert QIIE_MODE_VERDICT == "mode_grammar_extension_level_only"
        assert QIIE_EXCITATION_VERDICT == "dissipative_mode_excitation_structure_demonstrated"
        assert QIIE_PROPAGATION_VERDICT == "dissipative_propagation_only"
        assert "particle_ontology_premature" in QIIE_MATTER_BOUNDARY_VERDICT
        assert QIIE_AUTHORIZATION_VERDICT == "authorized_to_proceed_to_QIIF"

    def test_frozensets(self):
        for fs in [ALLOWED_MODE_VERDICTS, ALLOWED_EXCITATION_VERDICTS,
                   ALLOWED_PROPAGATION_VERDICTS, ALLOWED_MATTER_BOUNDARY_VERDICTS,
                   ALLOWED_AUTHORIZATION_VERDICTS]:
            assert len(fs) == 4
        assert len(ALLOWED_APPENDIX_P_CLASSES) == 8


class TestTrackAEligibility:
    def test_n_ingredients(self, result):
        assert result.track_a_eligibility.n_ingredients == N_ELIGIBILITY_INGREDIENTS

    def test_n_present(self, result):
        assert result.track_a_eligibility.n_present == 1

    def test_n_extension(self, result):
        assert result.track_a_eligibility.n_extension_level == 4

    def test_n_absent(self, result):
        assert result.track_a_eligibility.n_absent == 0

    def test_ee5_present(self, result):
        ee5 = result.track_a_eligibility.ingredients[4]
        assert ee5.ingredient_id == "EE5"
        assert ee5.status == "present"


class TestTrackBModeLabel:
    def test_n_candidates(self, result):
        assert result.track_b_mode_label.n_candidates == N_MODE_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_b_mode_label.n_viable == 1

    def test_chosen_ml1(self, result):
        assert "ML1" in result.track_b_mode_label.chosen_candidate_id

    def test_ml1_viable(self, result):
        ml1 = result.track_b_mode_label.candidates[0]
        assert ml1.viable is True

    def test_ml2_blocked(self, result):
        ml2 = result.track_b_mode_label.candidates[1]
        assert ml2.viable is False

    def test_verdict(self, result):
        assert result.track_b_mode_label.mode_verdict == QIIE_MODE_VERDICT


class TestTrackCExcitationOp:
    def test_n_candidates(self, result):
        assert result.track_c_excitation_op.n_candidates == N_EXCITATION_CANDIDATES

    def test_chosen_ex1(self, result):
        assert "EX1" in result.track_c_excitation_op.chosen_candidate_id

    def test_ex1_coherent(self, result):
        ex1 = result.track_c_excitation_op.candidates[0]
        assert ex1.coherent is True

    def test_verdict(self, result):
        assert result.track_c_excitation_op.excitation_verdict == QIIE_EXCITATION_VERDICT


class TestTrackDPropagation:
    def test_n_candidates(self, result):
        assert result.track_d_propagation.n_candidates == N_PROPAGATION_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_d_propagation.n_viable == 2

    def test_chosen_pr1(self, result):
        assert "PR1" in result.track_d_propagation.chosen_candidate_id

    def test_pr1_preserves_decoherence(self, result):
        pr1 = result.track_d_propagation.candidates[0]
        assert pr1.preserves_decoherence is True

    def test_verdict(self, result):
        assert result.track_d_propagation.propagation_verdict == QIIE_PROPAGATION_VERDICT


class TestTrackEBenchmark:
    def test_n_candidates(self, result):
        assert result.track_e_benchmark.n_candidates == N_BENCHMARK_CANDIDATES

    def test_n_viable(self, result):
        assert result.track_e_benchmark.n_viable == 2

    def test_chosen_mb1(self, result):
        assert "MB1" in result.track_e_benchmark.chosen_benchmark_id

    def test_benchmark_dim(self, result):
        assert result.track_e_benchmark.benchmark_hilbert_dim == TWO_SITE_DIM

    def test_benchmark_sites(self, result):
        assert result.track_e_benchmark.benchmark_n_sites == N_SITE_BENCHMARK

    def test_mb1_demonstrates(self, result):
        mb1 = result.track_e_benchmark.candidates[0]
        assert len(mb1.demonstrates) >= 3

    def test_mb1_not_demonstrate(self, result):
        mb1 = result.track_e_benchmark.candidates[0]
        not_d = " ".join(mb1.does_not_demonstrate).lower()
        assert "particle" in not_d or "matter" in not_d


class TestTrackFExcitationClass:
    def test_n_levels(self, result):
        assert result.track_f_excitation_class.n_levels == N_EXCITATION_CLASS_LEVELS

    def test_ec1_achieved(self, result):
        assert result.track_f_excitation_class.levels[0].achieved is True

    def test_ec3_achieved(self, result):
        assert result.track_f_excitation_class.levels[2].achieved is True

    def test_ec4_not_achieved(self, result):
        assert result.track_f_excitation_class.levels[3].achieved is False

    def test_ec5_not_achieved(self, result):
        assert result.track_f_excitation_class.levels[4].achieved is False

    def test_highest_is_ec3(self, result):
        assert "EC3" in result.track_f_excitation_class.highest_achieved_id


class TestTrackGConstitutive:
    def test_n_checks(self, result):
        assert result.track_g_constitutive.n_checks == N_CONSTITUTIVE_CHECKS

    def test_compatible(self, result):
        assert result.track_g_constitutive.compatible is True


class TestTrackHMatter:
    def test_n_levels(self, result):
        assert result.track_h_matter.n_levels == N_MATTER_LEVELS

    def test_fermionic_blocked(self, result):
        assert result.track_h_matter.fermionic_still_blocked is True

    def test_mr1_achieved(self, result):
        assert result.track_h_matter.levels[0].status == "achieved"

    def test_mr3_not_achieved(self, result):
        assert result.track_h_matter.levels[2].status == "not_achieved"

    def test_mr5_blocked(self, result):
        assert result.track_h_matter.levels[4].status == "blocked"

    def test_verdict(self, result):
        assert result.track_h_matter.matter_boundary_verdict == QIIE_MATTER_BOUNDARY_VERDICT


class TestTrackIAppendixP:
    def test_n_entries(self, result):
        assert result.track_i_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_i_appendix_p.no_native_canon is True

    def test_all_valid(self, result):
        for e in result.track_i_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES

    def test_at_least_one_mip(self, result):
        n = sum(1 for e in result.track_i_appendix_p.entries
                if e.appendix_p_class == "motivated_independent_postulation")
        assert n >= 1

    def test_at_least_one_bsr(self, result):
        n = sum(1 for e in result.track_i_appendix_p.entries
                if e.appendix_p_class == "bounded_structural_result")
        assert n >= 1


class TestTrackJAuthorization:
    def test_authorized(self, result):
        assert result.track_j_authorization.qiif_authorized is True

    def test_verdict(self, result):
        assert result.track_j_authorization.authorization_verdict == QIIE_AUTHORIZATION_VERDICT

    def test_constraints_mention_born(self, result):
        text = " ".join(result.track_j_authorization.qiif_constraints).lower()
        assert "born" in text


class TestTrackKNonclaims:
    def test_count(self, result):
        assert result.track_k_nonclaims.n_nonclaims == N_QIIE_NONCLAIMS

    def test_registered(self, result):
        assert result.track_k_nonclaims.all_registered is True

    def test_mentions_particles(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "particle" in text

    def test_mentions_fermionic(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "fermionic" in text

    def test_mentions_field_theory(self, result):
        text = " ".join(result.track_k_nonclaims.nonclaims).lower()
        assert "field_theory" in text or "field theory" in text


class TestHardGatedVerdicts:
    def test_mode_exact(self, result):
        assert result.mode_verdict == QIIE_MODE_VERDICT

    def test_excitation_exact(self, result):
        assert result.excitation_verdict == QIIE_EXCITATION_VERDICT

    def test_propagation_exact(self, result):
        assert result.propagation_verdict == QIIE_PROPAGATION_VERDICT

    def test_matter_exact(self, result):
        assert result.matter_boundary_verdict == QIIE_MATTER_BOUNDARY_VERDICT

    def test_authorization_exact(self, result):
        assert result.authorization_verdict == QIIE_AUTHORIZATION_VERDICT

    def test_all_in_allowed(self, result):
        assert result.mode_verdict in ALLOWED_MODE_VERDICTS
        assert result.excitation_verdict in ALLOWED_EXCITATION_VERDICTS
        assert result.propagation_verdict in ALLOWED_PROPAGATION_VERDICTS
        assert result.matter_boundary_verdict in ALLOWED_MATTER_BOUNDARY_VERDICTS
        assert result.authorization_verdict in ALLOWED_AUTHORIZATION_VERDICTS

    def test_all_distinct(self, result):
        v = {result.mode_verdict, result.excitation_verdict,
             result.propagation_verdict, result.matter_boundary_verdict,
             result.authorization_verdict}
        assert len(v) == 5

    def test_appendix_p(self, result):
        assert result.qiie_appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks(self, result):
        for attr in ['track_a_eligibility', 'track_b_mode_label',
                     'track_c_excitation_op', 'track_d_propagation',
                     'track_e_benchmark', 'track_f_excitation_class',
                     'track_g_constitutive', 'track_h_matter',
                     'track_i_appendix_p', 'track_j_authorization',
                     'track_k_nonclaims']:
            assert getattr(result, attr) is not None

    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_QIIE_NONCLAIMS

    def test_diagnostics(self, result):
        assert result.diagnostics["single_site_dim"] == SINGLE_SITE_DIM
        assert result.diagnostics["fermionic_still_blocked"] is True

    def test_idempotency(self):
        r1 = run_qiie_field_excitations_manymode_audit()
        r2 = run_qiie_field_excitations_manymode_audit()
        assert r1.valid == r2.valid
        assert r1.mode_verdict == r2.mode_verdict

    def test_self_test(self):
        assert _self_test() is True


class TestDoctrinalBoundaries:
    def test_no_particle_claim(self, result):
        for c in result.forbidden_claims:
            if "particle" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about particles")

    def test_no_field_theory_claim(self, result):
        for c in result.forbidden_claims:
            if "field" in c.lower() and ("theory" in c.lower() or "quantization" in c.lower()):
                break
        else:
            pytest.fail("No forbidden claim about field theory")

    def test_no_native_canon(self, result):
        for c in result.forbidden_claims:
            if "native canon" in c.lower() or "native_canon" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about native canon")

    def test_dissipative_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "dissipative" in text

    def test_fermionic_blocked_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "fermionic" in text and "blocked" in text
