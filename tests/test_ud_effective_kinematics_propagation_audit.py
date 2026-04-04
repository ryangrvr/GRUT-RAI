"""Tests for U-D --- Effective Kinematics and Propagation."""
import pytest
from grut.ud_effective_kinematics_propagation_audit import (
    N_REGIMES, N_OBSTRUCTIONS, N_UD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UD_KIN, UD_PROP, UD_SPEED, UD_MEM_KIN, UD_AUTH, UD_OVERALL,
    KIN_OPTIONS, PROP_OPTIONS, SPEED_OPTIONS, MEM_KIN_OPTIONS,
    AUTH_OPTIONS, UD_NONCLAIMS,
    run_ud_effective_kinematics_propagation_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ud_effective_kinematics_propagation_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UD_NONCLAIMS)==N_UD_NONCLAIMS
        for nc in UD_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UD_KIN=="local_relaxation_only_natively_supported"
        assert UD_PROP=="no_independent_propagating_mode_licensed"
        assert UD_SPEED=="no_native_speed_concept_beyond_rate"

class TestTrackA:
    def test_no_spatial(self, result):
        text=" ".join(result.track_a_local_vs_spatial.findings).lower()
        assert "no spatial" in text or "no nabla" in text

class TestTrackC:
    def test_no_speed(self, result):
        text=" ".join(result.track_c_speed.findings).lower()
        assert "no native speed" in text or "not a speed" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_REGIMES
    def test_free_no_propagation(self, result):
        assert "No" in result.evidence_table[0].spatial_propagation

class TestObstructions:
    def test_count(self, result): assert len(result.obstructions)==N_OBSTRUCTIONS
    def test_first(self, result):
        assert "spatial" in result.obstructions[0].name.lower()

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_kinematics_status in KIN_OPTIONS
        assert result.propagation_type_status in PROP_OPTIONS
        assert result.finite_speed_status in SPEED_OPTIONS
        assert result.memory_kinematics_status in MEM_KIN_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.native_kinematics_status,result.propagation_type_status,
           result.finite_speed_status,result.memory_kinematics_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_no_spatial(self, result):
        assert result.diagnostics["native_spatial_derivatives"] is False
    def test_no_speed(self, result):
        assert result.diagnostics["native_speed_concept"] is False
    def test_no_propagation(self, result):
        assert result.diagnostics["autonomous_spatial_propagation"] is False
    def test_local_yes(self, result):
        assert result.diagnostics["local_relaxation_supported"] is True

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_ud_effective_kinematics_propagation_audit()
        r2=run_ud_effective_kinematics_propagation_audit()
        assert r1.native_kinematics_status==r2.native_kinematics_status
    def test_self_test(self): assert _self_test() is True
