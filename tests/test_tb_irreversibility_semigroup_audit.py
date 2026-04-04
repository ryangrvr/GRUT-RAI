"""Tests for T-B --- Irreversibility and Semigroup Structure."""
import math
import pytest
from grut.tb_irreversibility_semigroup_audit import (
    TAU, CONTRACTION_RATE, N_REGIMES, N_TB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    TB_EVOLUTION_VERDICT, TB_INVERTIBILITY_VERDICT,
    TB_ATTRACTOR_VERDICT, TB_IRREVERSIBILITY_VERDICT,
    TB_AUTH_VERDICT, TB_OVERALL_P,
    EVOLUTION_OPTIONS, INVERTIBILITY_OPTIONS, ATTRACTOR_OPTIONS,
    IRREVERSIBILITY_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    TB_NONCLAIMS,
    run_tb_irreversibility_semigroup_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_tb_irreversibility_semigroup_audit()

class TestConstants:
    def test_contraction_rate(self):
        assert abs(CONTRACTION_RATE - 1.0/TAU) < 1e-15
    def test_nonclaims(self):
        assert len(TB_NONCLAIMS) == N_TB_NONCLAIMS
        for nc in TB_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert TB_EVOLUTION_VERDICT == "forward_semigroup_natively_supported"
        assert TB_INVERTIBILITY_VERDICT == "asymptotically_state_forgetting"
        assert TB_ATTRACTOR_VERDICT == "relaxation_to_fixed_or_steady_structures_supported"
        assert TB_IRREVERSIBILITY_VERDICT == "genuine_dynamical_irreversibility_supported"

class TestTrackA:
    def test_findings(self, result):
        assert len(result.track_a_semigroup.findings) >= 4
    def test_semigroup_mentioned(self, result):
        text = " ".join(result.track_a_semigroup.findings).lower()
        assert "semigroup" in text

class TestTrackB:
    def test_findings(self, result):
        assert len(result.track_b_invertibility.findings) >= 4
    def test_amplification(self, result):
        text = " ".join(result.track_b_invertibility.findings).lower()
        assert "amplif" in text

class TestTrackC:
    def test_attractor(self, result):
        text = " ".join(result.track_c_attractor.findings).lower()
        assert "attractor" in text

class TestTrackD:
    def test_genuine(self, result):
        text = " ".join(result.track_d_directionality.findings).lower()
        assert "genuine" in text

class TestTrackE:
    def test_contraction(self, result):
        text = " ".join(result.track_e_compression.findings).lower()
        assert "contraction" in text or "contract" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table) == N_REGIMES
    def test_free_relaxation(self, result):
        fr = result.evidence_table[0]
        assert "Yes" in fr.forward_well_posed
        assert "semigroup" in fr.row_verdict.lower() or "irreversible" in fr.row_verdict.lower()
    def test_backward(self, result):
        bk = result.evidence_table[4]
        assert "non_recoverable" in bk.row_verdict.lower() or "amplif" in bk.inverse_licensed.lower()

class TestLicensed:
    def test_semigroup(self, result):
        assert any("semigroup" in t for t in result.licensed_language.licensed)
    def test_irreversibility(self, result):
        assert any("irreversibility" in t for t in result.licensed_language.licensed)

class TestNonlicensed:
    def test_entropy(self, result):
        assert "entropy" in result.nonlicensed_language.nonlicensed
    def test_temperature(self, result):
        assert "temperature" in result.nonlicensed_language.nonlicensed
    def test_stat_mech(self, result):
        assert "statistical_mechanics" in result.nonlicensed_language.nonlicensed

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.evolution_structure in EVOLUTION_OPTIONS
        assert result.invertibility_status in INVERTIBILITY_OPTIONS
        assert result.attractor_status in ATTRACTOR_OPTIONS
        assert result.irreversibility_status in IRREVERSIBILITY_OPTIONS
        assert result.authorization in AUTH_OPTIONS
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_all_distinct(self, result):
        v = {result.evolution_structure, result.invertibility_status,
             result.attractor_status, result.irreversibility_status,
             result.authorization}
        assert len(v) == 5

class TestDiagnostics:
    def test_rate(self, result):
        assert abs(result.diagnostics["contraction_rate"] - 1.0/TAU) < 1e-15
    def test_rate_is_gamma(self, result):
        assert result.diagnostics["contraction_rate_is_gamma"] is True
    def test_timescale(self, result):
        assert abs(result.diagnostics["state_forgetting_timescale"] - TAU) < 1e-15

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings) >= 6
    def test_idempotency(self):
        r1 = run_tb_irreversibility_semigroup_audit()
        r2 = run_tb_irreversibility_semigroup_audit()
        assert r1.irreversibility_status == r2.irreversibility_status
    def test_self_test(self): assert _self_test() is True
