"""Tests for U-C --- Action Principle and Variational Structure."""
import pytest
from grut.uc_action_principle_variational_audit import (
    N_CANDIDATES, N_OBSTRUCTIONS, N_UC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UC_NATIVE_ACTION, UC_AUX, UC_MEMORY_VAR, UC_STRONGEST,
    UC_AUTH, UC_OVERALL_P,
    NATIVE_ACTION_OPTIONS, AUX_OPTIONS, MEMORY_VAR_OPTIONS,
    STRONGEST_OPTIONS, AUTH_OPTIONS, UC_NONCLAIMS,
    run_uc_action_principle_variational_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_uc_action_principle_variational_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UC_NONCLAIMS)==N_UC_NONCLAIMS
        for nc in UC_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UC_NATIVE_ACTION=="native_action_obstructed_by_dissipative_structure"
        assert UC_AUX=="multiplier_or_response_formalism_available_but_nonnative"
        assert UC_STRONGEST=="pseudoaction_or_response_functional_only"

class TestTrackA:
    def test_obstruction(self, result):
        text=" ".join(result.track_a_native_action.findings).lower()
        assert "obstruct" in text or "cannot" in text or "no real" in text

class TestTrackC:
    def test_doubled(self, result):
        text=" ".join(result.track_c_doubled.findings).lower()
        assert "reproduces" in text or "recovers" in text

class TestTrackE:
    def test_lyapunov_not_action(self, result):
        text=" ".join(result.track_e_pseudoaction.findings).lower()
        assert "not an action" in text or "not action" in text

class TestObstructions:
    def test_count(self, result): assert len(result.track_f_obstructions)==N_OBSTRUCTIONS
    def test_first_is_dissipative(self, result):
        assert "dissipative" in result.track_f_obstructions[0].name.lower()

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_CANDIDATES
    def test_native_obstructed(self, result):
        assert "obstructed" in result.evidence_table[0].row_verdict.lower()
    def test_response_available(self, result):
        assert "available" in result.evidence_table[2].row_verdict.lower()

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_action_status in NATIVE_ACTION_OPTIONS
        assert result.auxiliary_variational_status in AUX_OPTIONS
        assert result.memory_variational_status in MEMORY_VAR_OPTIONS
        assert result.strongest_action_like_language in STRONGEST_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.native_action_status,result.auxiliary_variational_status,
           result.memory_variational_status,result.strongest_action_like_language,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_no_native_action(self, result):
        assert result.diagnostics["native_action_possible"] is False
    def test_response_available(self, result):
        assert result.diagnostics["response_field_available"] is True
    def test_lyapunov_not_action(self, result):
        assert result.diagnostics["lyapunov_is_action"] is False

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_uc_action_principle_variational_audit()
        r2=run_uc_action_principle_variational_audit()
        assert r1.native_action_status==r2.native_action_status
    def test_self_test(self): assert _self_test() is True
