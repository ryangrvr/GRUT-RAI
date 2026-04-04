"""Tests for T-A --- Thermodynamic Charter."""
import pytest
from grut.ta_thermodynamic_charter import (
    STAGES, N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS,
    FFM_NAMES, N_TA_NONCLAIMS, TA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_ta_thermodynamic_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ta_thermodynamic_charter()

class TestConstants:
    def test_stages(self): assert N_STAGES == 6
    def test_distinctions(self): assert N_DISTINCTIONS == 10
    def test_nonclaims(self):
        assert len(TA_NONCLAIMS) == N_TA_NONCLAIMS
        for nc in TA_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert CHARTER_VERDICT == "charter_defined_with_strict_prohibitions"
        assert AUTH_VERDICT == "authorized_to_proceed_to_TB"
        assert OVERALL_P == "thermodynamic_program_opened_under_strict_limits"

class TestDistinctions:
    def test_count(self, result): assert len(result.distinctions) == N_DISTINCTIONS
    def test_d1_dissipation_vs_thermo(self, result):
        assert result.distinctions[0].left == "dissipation"
        assert result.distinctions[0].right == "thermodynamics"
    def test_d7_monotone_vs_entropy(self, result):
        assert "monotone" in result.distinctions[6].left
        assert "entropy" in result.distinctions[6].right

class TestStages:
    def test_count(self, result): assert len(result.stage_sequence) == N_STAGES
    def test_sequential(self, result):
        for i, s in enumerate(result.stage_sequence): assert s.stage_index == i
    def test_tb(self, result): assert "T-B" in result.stage_sequence[2].stage_id

class TestRules:
    def test_count(self, result): assert len(result.rules) == N_RULES

class TestFFMs:
    def test_count(self, result): assert len(result.ffms) == N_FFMS
    def test_all_names(self, result):
        names = [f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestTBLicensed:
    def test_count(self, result): assert len(result.tb_licensed.licensed_tests) >= 3
    def test_semigroup(self, result):
        text = " ".join(result.tb_licensed.licensed_tests).lower()
        assert "semigroup" in text

class TestVerdicts:
    def test_charter(self, result): assert result.charter_verdict == CHARTER_VERDICT
    def test_auth(self, result): assert result.authorization_verdict == AUTH_VERDICT
    def test_overall(self, result): assert result.overall_appendix_p == OVERALL_P

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings) >= 5
    def test_idempotency(self):
        r1 = run_ta_thermodynamic_charter()
        r2 = run_ta_thermodynamic_charter()
        assert r1.charter_verdict == r2.charter_verdict
    def test_self_test(self): assert _self_test() is True
