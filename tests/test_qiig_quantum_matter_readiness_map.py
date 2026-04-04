"""
Tests for Appendix Q-II.G --- Quantum Matter-Readiness Map
==========================================================
"""

import pytest

from grut.qiig_quantum_matter_readiness_map import (
    TAU, GAMMA,
    N_HANDOFF_ITEMS, N_READINESS_DOMAINS,
    N_R_ASSUMES, N_R_EXTENSION_FLAGS, N_R_MUST_NOT_ASSUME, N_R_MUST_REAUDIT,
    N_APPENDIX_P_ENTRIES, N_QIIG_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    ALLOWED_READINESS_LEVELS,
    QIIG_BOSONIC_VERDICT, QIIG_FERMIONIC_VERDICT,
    QIIG_PROBABILITY_BOUNDARY_VERDICT,
    QIIG_APPENDIX_R_ENTRY_VERDICT, QIIG_OVERALL_VERDICT,
    QIIG_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_BOSONIC_VERDICTS, ALLOWED_FERMIONIC_VERDICTS,
    ALLOWED_PROBABILITY_BOUNDARY_VERDICTS,
    ALLOWED_APPENDIX_R_ENTRY_VERDICTS, ALLOWED_OVERALL_VERDICTS,
    ALLOWED_APPENDIX_P_CLASSES,
    QIIG_NONCLAIMS,
    run_qiig_quantum_matter_readiness_map, _self_test,
)


@pytest.fixture(scope="module")
def result():
    return run_qiig_quantum_matter_readiness_map()


class TestQIIGConstants:
    def test_gamma_tau(self):
        assert abs(GAMMA * TAU - 1.0) < 1e-15

    def test_counts(self):
        assert N_HANDOFF_ITEMS == 9
        assert N_READINESS_DOMAINS == 10
        assert N_R_ASSUMES == 4
        assert N_R_EXTENSION_FLAGS == 5
        assert N_R_MUST_NOT_ASSUME == 5
        assert N_R_MUST_REAUDIT == 3
        assert N_QIIG_NONCLAIMS == 8

    def test_nonclaims(self):
        assert len(QIIG_NONCLAIMS) == N_QIIG_NONCLAIMS
        for nc in QIIG_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

    def test_verdicts(self):
        assert QIIG_BOSONIC_VERDICT == "bosonic_pre_matter_readiness_advanced"
        assert QIIG_FERMIONIC_VERDICT == "fermionic_obstruction_unchanged"
        assert "explicit_probability_postulate" in QIIG_PROBABILITY_BOUNDARY_VERDICT
        assert "extension_flags" in QIIG_APPENDIX_R_ENTRY_VERDICT
        assert "sufficient_to_open" in QIIG_OVERALL_VERDICT

    def test_frozensets(self):
        for fs in [ALLOWED_BOSONIC_VERDICTS, ALLOWED_FERMIONIC_VERDICTS,
                   ALLOWED_PROBABILITY_BOUNDARY_VERDICTS,
                   ALLOWED_APPENDIX_R_ENTRY_VERDICTS, ALLOWED_OVERALL_VERDICTS]:
            assert len(fs) == 4

    def test_readiness_levels(self):
        assert len(ALLOWED_READINESS_LEVELS) == 4


class TestTrackAHandoff:
    def test_n_items(self, result):
        assert result.track_a_handoff.n_items == N_HANDOFF_ITEMS

    def test_n_ready(self, result):
        assert result.track_a_handoff.n_ready == 2

    def test_n_extension_ready(self, result):
        assert result.track_a_handoff.n_extension_ready == 5

    def test_n_precondition(self, result):
        assert result.track_a_handoff.n_precondition == 1

    def test_n_blocked(self, result):
        assert result.track_a_handoff.n_blocked == 1

    def test_counts_sum(self, result):
        h = result.track_a_handoff
        assert h.n_ready + h.n_extension_ready + h.n_precondition + h.n_blocked == h.n_items

    def test_hi1_ready(self, result):
        hi1 = result.track_a_handoff.items[0]
        assert hi1.readiness == "ready"

    def test_hi8_blocked(self, result):
        hi8 = result.track_a_handoff.items[7]
        assert hi8.readiness == "blocked"
        assert "fermionic" in hi8.item_name.lower()

    def test_all_readiness_valid(self, result):
        for i in result.track_a_handoff.items:
            assert i.readiness in ALLOWED_READINESS_LEVELS

    def test_all_classes_valid(self, result):
        for i in result.track_a_handoff.items:
            assert i.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


class TestTrackBBosonic:
    def test_state_grammar(self, result):
        assert result.track_b_bosonic.state_grammar_ready is True

    def test_excitation(self, result):
        assert result.track_b_bosonic.excitation_structure_ready is True

    def test_constitutive(self, result):
        assert result.track_b_bosonic.constitutive_bridge_ready is True

    def test_no_particles(self, result):
        assert result.track_b_bosonic.particle_like_readiness is False

    def test_no_bound_states(self, result):
        assert result.track_b_bosonic.bound_state_readiness is False

    def test_verdict(self, result):
        assert result.track_b_bosonic.bosonic_readiness_verdict == QIIG_BOSONIC_VERDICT


class TestTrackCFermionic:
    def test_obstruction_unchanged(self, result):
        assert result.track_c_fermionic.obstruction_changed is False

    def test_no_new_route(self, result):
        assert result.track_c_fermionic.new_route_identified is False

    def test_verdict(self, result):
        assert result.track_c_fermionic.fermionic_readiness_verdict == QIIG_FERMIONIC_VERDICT

    def test_obstruction_mentions_pi2(self, result):
        assert "pi_2" in result.track_c_fermionic.obstruction_description


class TestTrackDBoundState:
    def test_composite_available(self, result):
        assert result.track_d_bound_state.composite_grammar_available is True

    def test_no_interaction(self, result):
        assert result.track_d_bound_state.interaction_hamiltonian_available is False

    def test_no_binding(self, result):
        assert result.track_d_bound_state.binding_mechanism_available is False


class TestTrackEProbability:
    def test_born_not_derived(self, result):
        assert result.track_e_probability.born_rule_derived is False

    def test_weights_available(self, result):
        assert result.track_e_probability.diagnostic_weights_available is True

    def test_extension_identified(self, result):
        assert result.track_e_probability.extension_route_identified is True

    def test_verdict(self, result):
        assert result.track_e_probability.probability_boundary_verdict == \
               QIIG_PROBABILITY_BOUNDARY_VERDICT


class TestTrackFReadinessTable:
    def test_n_entries(self, result):
        assert result.track_f_readiness_table.n_entries == N_READINESS_DOMAINS

    def test_n_ready(self, result):
        assert result.track_f_readiness_table.n_ready == 1

    def test_n_extension_ready(self, result):
        assert result.track_f_readiness_table.n_extension_ready == 5

    def test_n_blocked(self, result):
        assert result.track_f_readiness_table.n_blocked == 1

    def test_all_levels_valid(self, result):
        for e in result.track_f_readiness_table.entries:
            assert e.readiness_level in ALLOWED_READINESS_LEVELS

    def test_fermionic_blocked(self, result):
        ferm = [e for e in result.track_f_readiness_table.entries
                if "fermionic" in e.domain.lower()]
        assert len(ferm) == 1
        assert ferm[0].readiness_level == "blocked"

    def test_constitutive_ready(self, result):
        const = [e for e in result.track_f_readiness_table.entries
                 if "constitutive" in e.domain.lower()]
        assert len(const) == 1
        assert const[0].readiness_level == "ready"


class TestTrackGREntry:
    def test_n_assumes(self, result):
        assert len(result.track_g_r_entry.r_may_assume) == N_R_ASSUMES

    def test_n_flags(self, result):
        assert len(result.track_g_r_entry.r_must_carry_extension_flags) == N_R_EXTENSION_FLAGS

    def test_n_must_not(self, result):
        assert len(result.track_g_r_entry.r_must_not_assume) == N_R_MUST_NOT_ASSUME

    def test_n_reaudit(self, result):
        assert len(result.track_g_r_entry.r_must_reaudit) == N_R_MUST_REAUDIT

    def test_must_not_born(self, result):
        text = " ".join(result.track_g_r_entry.r_must_not_assume).lower()
        assert "born" in text

    def test_must_not_fermionic(self, result):
        text = " ".join(result.track_g_r_entry.r_must_not_assume).lower()
        assert "fermionic" in text

    def test_verdict(self, result):
        assert result.track_g_r_entry.appendix_r_entry_verdict == QIIG_APPENDIX_R_ENTRY_VERDICT


class TestTrackHAppendixP:
    def test_n_entries(self, result):
        assert result.track_h_appendix_p.n_entries == N_APPENDIX_P_ENTRIES

    def test_no_native_canon(self, result):
        assert result.track_h_appendix_p.no_native_canon is True

    def test_overall_bsr(self, result):
        assert result.track_h_appendix_p.overall_class == "bounded_structural_result"

    def test_all_valid(self, result):
        for e in result.track_h_appendix_p.entries:
            assert e.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES


class TestTrackINonclaims:
    def test_count(self, result):
        assert result.track_i_nonclaims.n_nonclaims == N_QIIG_NONCLAIMS

    def test_registered(self, result):
        assert result.track_i_nonclaims.all_registered is True

    def test_mentions_particles(self, result):
        text = " ".join(result.track_i_nonclaims.nonclaims).lower()
        assert "particle" in text

    def test_mentions_fermionic(self, result):
        text = " ".join(result.track_i_nonclaims.nonclaims).lower()
        assert "fermionic" in text

    def test_mentions_matter(self, result):
        text = " ".join(result.track_i_nonclaims.nonclaims).lower()
        assert "matter" in text


class TestHardGatedVerdicts:
    def test_bosonic(self, result):
        assert result.bosonic_readiness_verdict == QIIG_BOSONIC_VERDICT
        assert result.bosonic_readiness_verdict in ALLOWED_BOSONIC_VERDICTS

    def test_fermionic(self, result):
        assert result.fermionic_readiness_verdict == QIIG_FERMIONIC_VERDICT
        assert result.fermionic_readiness_verdict in ALLOWED_FERMIONIC_VERDICTS

    def test_probability(self, result):
        assert result.probability_boundary_verdict == QIIG_PROBABILITY_BOUNDARY_VERDICT
        assert result.probability_boundary_verdict in ALLOWED_PROBABILITY_BOUNDARY_VERDICTS

    def test_r_entry(self, result):
        assert result.appendix_r_entry_verdict == QIIG_APPENDIX_R_ENTRY_VERDICT
        assert result.appendix_r_entry_verdict in ALLOWED_APPENDIX_R_ENTRY_VERDICTS

    def test_overall(self, result):
        assert result.overall_q_to_r_verdict == QIIG_OVERALL_VERDICT
        assert result.overall_q_to_r_verdict in ALLOWED_OVERALL_VERDICTS

    def test_all_distinct(self, result):
        v = {result.bosonic_readiness_verdict, result.fermionic_readiness_verdict,
             result.probability_boundary_verdict, result.appendix_r_entry_verdict,
             result.overall_q_to_r_verdict}
        assert len(v) == 5


class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True

    def test_all_tracks(self, result):
        for attr in ['track_a_handoff', 'track_b_bosonic', 'track_c_fermionic',
                     'track_d_bound_state', 'track_e_probability',
                     'track_f_readiness_table', 'track_g_r_entry',
                     'track_h_appendix_p', 'track_i_nonclaims']:
            assert getattr(result, attr) is not None

    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS

    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_QIIG_NONCLAIMS

    def test_diagnostics(self, result):
        d = result.diagnostics
        assert d["born_rule_derived"] is False
        assert d["fermionic_obstruction_changed"] is False
        assert d["particle_ontology_ready"] is False
        assert d["bound_state_ready"] is False

    def test_idempotency(self):
        r1 = run_qiig_quantum_matter_readiness_map()
        r2 = run_qiig_quantum_matter_readiness_map()
        assert r1.overall_q_to_r_verdict == r2.overall_q_to_r_verdict

    def test_self_test(self):
        assert _self_test() is True


class TestDoctrinalBoundaries:
    def test_no_particle_claim(self, result):
        for c in result.forbidden_claims:
            if "particle" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about particles")

    def test_no_fermionic_dissolved(self, result):
        for c in result.forbidden_claims:
            if "fermionic" in c.lower():
                break
        else:
            pytest.fail("No forbidden claim about fermionic dissolution")

    def test_no_matter_closure(self, result):
        for c in result.forbidden_claims:
            if "matter" in c.lower() and ("canon" in c.lower() or "closure" in c.lower()):
                break
        else:
            pytest.fail("No forbidden claim about matter closure/canon")

    def test_readiness_map_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "readiness" in text or "handoff" in text

    def test_appendix_r_in_allowed(self, result):
        text = " ".join(result.allowed_claims).lower()
        assert "appendix r" in text or "appendix_r" in text
