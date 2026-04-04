"""Tests for Z-A --- Final Sovereign Ledger Charter."""
import pytest
from grut.za_sovereign_ledger_charter import (
    N_STAGES, N_DISTINCTIONS, N_RULES, N_FFMS, N_ZA_NONCLAIMS,
    N_ALLOWED, N_FORBIDDEN, FFM_NAMES, ZA_NONCLAIMS,
    CHARTER_VERDICT, AUTH_VERDICT, OVERALL_P,
    ALLOWED_CHARTER_VERDICTS, ALLOWED_AUTH_VERDICTS, ALLOWED_OVERALL_VERDICTS,
    run_za_sovereign_ledger_charter, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_za_sovereign_ledger_charter()


class TestConstants:
    def test_n_stages(self): assert N_STAGES == 6
    def test_n_dist(self): assert N_DISTINCTIONS == 12
    def test_n_rules(self): assert N_RULES == 8
    def test_n_ffms(self): assert N_FFMS == 8
    def test_n_nc(self): assert N_ZA_NONCLAIMS == 8
    def test_n_allowed(self): assert N_ALLOWED == 7
    def test_n_forbidden(self): assert N_FORBIDDEN == 7
    def test_ffm_count(self): assert len(FFM_NAMES) == N_FFMS


class TestDistinctions:
    def test_count(self, result): assert len(result.distinctions) == N_DISTINCTIONS
    def test_ids(self, result):
        for i, d in enumerate(result.distinctions):
            assert d.dist_id == f"MD{i+1}"
    def test_left_right_distinct(self, result):
        for d in result.distinctions:
            assert d.left != d.right


class TestStages:
    def test_count(self, result): assert len(result.stage_sequence) == N_STAGES
    def test_indices(self, result):
        for i, s in enumerate(result.stage_sequence):
            assert s.stage_index == i
    def test_z0_first(self, result): assert result.stage_sequence[0].stage_id == "Z0"
    def test_ze_last(self, result): assert result.stage_sequence[-1].stage_id == "Z-E"


class TestRules:
    def test_count(self, result): assert len(result.rules) == N_RULES
    def test_ids(self, result):
        for i, r in enumerate(result.rules):
            assert r.rule_id == f"ZR{i+1}"


class TestFFMs:
    def test_count(self, result): assert len(result.ffms) == N_FFMS
    def test_names(self, result):
        names = [f.name for f in result.ffms]
        for n in FFM_NAMES:
            assert n in names
    def test_ids(self, result):
        for i, f in enumerate(result.ffms):
            assert f.mode_id == f"FFM-Z.{i+1}"


class TestVerdicts:
    def test_charter(self, result):
        assert result.charter_verdict == CHARTER_VERDICT
        assert result.charter_verdict in ALLOWED_CHARTER_VERDICTS
    def test_auth(self, result):
        assert result.authorization_verdict == AUTH_VERDICT
        assert result.authorization_verdict in ALLOWED_AUTH_VERDICTS
    def test_overall(self, result):
        assert result.overall_appendix_p == OVERALL_P
        assert result.overall_appendix_p in ALLOWED_OVERALL_VERDICTS
    def test_distinct(self, result):
        v = {result.charter_verdict, result.authorization_verdict, result.overall_appendix_p}
        assert len(v) == 3


class TestNonclaims:
    def test_count(self): assert len(ZA_NONCLAIMS) == N_ZA_NONCLAIMS
    def test_prefix(self):
        for nc in ZA_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_firewall(self, result):
        assert result.nonclaim_firewall.n_nonclaims == N_ZA_NONCLAIMS
        assert result.nonclaim_firewall.all_registered is True


class TestDiagnostics:
    def test_ext(self, result): assert result.diagnostics["grand_total_extensions"] == 7
    def test_params(self, result): assert result.diagnostics["grand_total_parameters"] == 3
    def test_fields(self, result): assert result.diagnostics["grand_total_new_fields"] == 0
    def test_items(self, result): assert result.diagnostics["grand_total_items"] == 32
    def test_qm(self, result): assert result.diagnostics["full_qm"] is False
    def test_closure(self, result): assert result.diagnostics["unified_closure"] is False
    def test_toe(self, result): assert result.diagnostics["toe_status"] is False


class TestClaims:
    def test_allowed(self, result): assert len(result.allowed_claims) == N_ALLOWED
    def test_forbidden(self, result): assert len(result.forbidden_claims) == N_FORBIDDEN


class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_key(self, result): assert len(result.key_findings) >= 5
    def test_self_test(self): assert _self_test() is True
    def test_idempotent(self):
        r1 = run_za_sovereign_ledger_charter()
        r2 = run_za_sovereign_ledger_charter()
        assert r1.valid == r2.valid
        assert r1.charter_verdict == r2.charter_verdict
