"""Tests for U-G --- Sector Integration and Unified-Field Status."""
import pytest
from grut.ug_sector_integration_unified_field_audit import (
    N_ASSEMBLIES, N_OBSTRUCTIONS, N_UG_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UG_CARRIER, UG_DYNAMICS, UG_CLOSURE, UG_UNIFIED, UG_AUTH, UG_OVERALL,
    CARRIER_OPTIONS, DYNAMICS_OPTIONS, CLOSURE_OPTIONS, UNIFIED_OPTIONS,
    AUTH_OPTIONS, UG_NONCLAIMS,
    run_ug_sector_integration_unified_field_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ug_sector_integration_unified_field_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UG_NONCLAIMS)==N_UG_NONCLAIMS
        for nc in UG_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UG_CARRIER=="scalar_core_plus_nonnative_attachments"
        assert UG_DYNAMICS=="scalar_core_with_postulated_sector_responses"
        assert UG_CLOSURE=="layered_nonclosure_persists"
        assert UG_UNIFIED=="constitutive_architecture_only"

class TestTrackA:
    def test_no_shared(self, result):
        text=" ".join(result.track_a_carrier.findings).lower()
        assert "distinct" in text or "no common" in text

class TestTrackC:
    def test_nonclosure(self, result):
        text=" ".join(result.track_c_closure.findings).lower()
        assert "nonclosure" in text or "do not close" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_ASSEMBLIES
    def test_all_no_closure(self, result):
        last=result.evidence_table[-1]
        assert "No" in last.closure or "no" in last.closure.lower()

class TestObstructions:
    def test_count(self, result): assert len(result.track_g_obstructions)==N_OBSTRUCTIONS

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.carrier_status in CARRIER_OPTIONS
        assert result.dynamics_status in DYNAMICS_OPTIONS
        assert result.closure_status in CLOSURE_OPTIONS
        assert result.unified_field_status in UNIFIED_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.carrier_status,result.dynamics_status,
           result.closure_status,result.unified_field_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_no_carrier(self, result): assert result.diagnostics["shared_carrier_found"] is False
    def test_no_dynamics(self, result): assert result.diagnostics["shared_dynamics_found"] is False
    def test_no_closure(self, result): assert result.diagnostics["closure_found"] is False
    def test_no_unified(self, result): assert result.diagnostics["unified_field_established"] is False

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_ug_sector_integration_unified_field_audit()
        r2=run_ug_sector_integration_unified_field_audit()
        assert r1.unified_field_status==r2.unified_field_status
    def test_self_test(self): assert _self_test() is True
