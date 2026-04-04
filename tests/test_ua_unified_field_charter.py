"""Tests for U-A --- Unified-Field Charter."""
import pytest
from grut.ua_unified_field_charter import (
    STAGES, N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS,
    FFM_NAMES, N_UA_NONCLAIMS, UA_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    run_ua_unified_field_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ua_unified_field_charter()

class TestConstants:
    def test_stages(self): assert N_STAGES == 9
    def test_distinctions(self): assert N_DISTINCTIONS == 12
    def test_rules(self): assert N_RULES == 8
    def test_ffms(self): assert N_FFMS == 8
    def test_nonclaims(self):
        assert len(UA_NONCLAIMS) == N_UA_NONCLAIMS
        for nc in UA_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestDistinctions:
    def test_count(self, result): assert len(result.distinctions) == N_DISTINCTIONS
    def test_d1(self, result):
        assert result.distinctions[0].left == "constitutive_evolution"
        assert result.distinctions[0].right == "action_principle"

class TestStages:
    def test_count(self, result): assert len(result.stage_sequence) == N_STAGES
    def test_sequential(self, result):
        for i, s in enumerate(result.stage_sequence): assert s.stage_index == i
    def test_ub_third(self, result): assert "U-B" in result.stage_sequence[2].stage_id
    def test_uh_last(self, result): assert "U-H" in result.stage_sequence[-1].stage_id

class TestFFMs:
    def test_count(self, result): assert len(result.ffms) == N_FFMS
    def test_all_names(self, result):
        names = [f.name for f in result.ffms]
        for n in FFM_NAMES: assert n in names

class TestUBLicensed:
    def test_count(self, result): assert len(result.ub_licensed.licensed_tests) >= 3

class TestVerdicts:
    def test_charter(self, result): assert result.charter_verdict == CHARTER_VERDICT
    def test_auth(self, result): assert result.authorization_verdict == AUTH_VERDICT
    def test_overall(self, result): assert result.overall_appendix_p == OVERALL_P

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_idempotency(self):
        r1 = run_ua_unified_field_charter()
        r2 = run_ua_unified_field_charter()
        assert r1.charter_verdict == r2.charter_verdict
    def test_self_test(self): assert _self_test() is True
