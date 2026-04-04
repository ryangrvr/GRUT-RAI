"""Tests for T-C --- Dissipation Functional, Lyapunov, Balance-Law."""
import math, pytest
from grut.tc_dissipation_functional_lyapunov_audit import (
    TAU, GAMMA, DECAY_RATE_V, N_REGIMES, N_TC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    TC_LYAPUNOV_VERDICT, TC_DISSIPATION_VERDICT, TC_BALANCE_VERDICT,
    TC_FIREWALL_VERDICT, TC_AUTH_VERDICT, TC_OVERALL_P,
    LYAPUNOV_OPTIONS, DISSIPATION_OPTIONS, BALANCE_OPTIONS,
    FIREWALL_OPTIONS, AUTH_OPTIONS, TC_NONCLAIMS,
    run_tc_dissipation_functional_lyapunov_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_tc_dissipation_functional_lyapunov_audit()

class TestConstants:
    def test_decay_rate(self):
        assert abs(DECAY_RATE_V - 2.0/TAU) < 1e-15
    def test_decay_is_2gamma(self):
        assert abs(DECAY_RATE_V - 2.0*GAMMA) < 1e-15
    def test_nonclaims(self):
        assert len(TC_NONCLAIMS) == N_TC_NONCLAIMS
        for nc in TC_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestTrackA:
    def test_lyapunov(self, result):
        text = " ".join(result.track_a_lyapunov.findings).lower()
        assert "lyapunov" in text
    def test_exponential(self, result):
        text = " ".join(result.track_a_lyapunov.findings)
        assert "exp(-2t/tau)" in text or "exp(-2" in text

class TestTrackB:
    def test_dissipation(self, result):
        text = " ".join(result.track_b_dissipation.findings).lower()
        assert "dissipation" in text or "decay" in text

class TestTrackC:
    def test_balance(self, result):
        text = " ".join(result.track_c_balance.findings).lower()
        assert "balance" in text

class TestTrackE:
    def test_firewall(self, result):
        text = " ".join(result.track_e_entropy_firewall.findings).lower()
        assert "not" in text and "entropy" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table) == N_REGIMES
    def test_free_monotone(self, result):
        assert "Yes" in result.evidence_table[0].monotone

class TestLicensed:
    def test_lyapunov_licensed(self, result):
        assert any("lyapunov" in t.lower() for t in result.licensed_language.licensed)

class TestNonlicensed:
    def test_entropy(self, result):
        assert any("entropy" in t.lower() for t in result.nonlicensed_language.nonlicensed)
    def test_temperature(self, result):
        assert any("temperature" in t.lower() for t in result.nonlicensed_language.nonlicensed)

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.lyapunov_status in LYAPUNOV_OPTIONS
        assert result.dissipation_functional_status in DISSIPATION_OPTIONS
        assert result.balance_law_status in BALANCE_OPTIONS
        assert result.entropy_firewall_status in FIREWALL_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v = {result.lyapunov_status, result.dissipation_functional_status,
             result.balance_law_status, result.entropy_firewall_status,
             result.authorization}
        assert len(v) == 5

class TestDiagnostics:
    def test_rate(self, result):
        assert result.diagnostics["lyapunov_decay_rate_is_2_gamma"] is True
    def test_conditional(self, result):
        assert result.diagnostics["conditional_on_forcing"] is True

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings) >= 6
    def test_idempotency(self):
        r1 = run_tc_dissipation_functional_lyapunov_audit()
        r2 = run_tc_dissipation_functional_lyapunov_audit()
        assert r1.lyapunov_status == r2.lyapunov_status
    def test_self_test(self): assert _self_test() is True
