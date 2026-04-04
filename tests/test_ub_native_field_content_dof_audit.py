"""Tests for U-B --- Native Field Content and DOF."""
import pytest
from grut.ub_native_field_content_dof_audit import (
    N_REGIMES, N_UB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    UB_DOF_VERDICT, UB_SOURCE_VERDICT, UB_MEMORY_VERDICT,
    UB_EXTENSION_VERDICT, UB_AUTH_VERDICT, UB_OVERALL_P,
    DOF_OPTIONS, SOURCE_OPTIONS, MEMORY_OPTIONS, EXTENSION_OPTIONS,
    AUTH_OPTIONS, UB_NONCLAIMS,
    run_ub_native_field_content_dof_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_ub_native_field_content_dof_audit()

class TestConstants:
    def test_nonclaims(self):
        assert len(UB_NONCLAIMS)==N_UB_NONCLAIMS
        for nc in UB_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UB_DOF_VERDICT=="single_scalar_dof_natively_supported"
        assert UB_SOURCE_VERDICT=="X_is_external_or_constitutive_input"
        assert UB_MEMORY_VERDICT=="memory_modifies_evolution_without_new_native_field"

class TestTrackA:
    def test_phi_only(self, result):
        text=" ".join(result.track_a_variables.findings).lower()
        assert "phi" in text and "single" in text

class TestTrackC:
    def test_x_external(self, result):
        text=" ".join(result.track_c_source.findings).lower()
        assert "external" in text or "input" in text

class TestTrackD:
    def test_no_new_field(self, result):
        text=" ".join(result.track_d_memory.findings).lower()
        assert "not add" in text or "does not" in text

class TestTrackE:
    def test_nonnative(self, result):
        text=" ".join(result.track_e_extensions.findings).lower()
        assert "not native" in text or "nonnative" in text or "extension" in text

class TestEvidence:
    def test_count(self, result): assert len(result.evidence_table)==N_REGIMES

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_dof_status in DOF_OPTIONS
        assert result.source_status in SOURCE_OPTIONS
        assert result.memory_status in MEMORY_OPTIONS
        assert result.extension_field_status in EXTENSION_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.native_dof_status,result.source_status,
           result.memory_status,result.extension_field_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_dof_count(self, result): assert result.diagnostics["native_dof_count"]==1
    def test_field_type(self, result): assert result.diagnostics["native_field_type"]=="real_scalar"
    def test_first_order(self, result): assert result.diagnostics["evolution_order"]=="first_order_in_time"
    def test_x_no_evol(self, result): assert result.diagnostics["x_has_evolution_equation"] is False
    def test_ctp_no_field(self, result): assert result.diagnostics["ctp_adds_native_field"] is False

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_ub_native_field_content_dof_audit()
        r2=run_ub_native_field_content_dof_audit()
        assert r1.native_dof_status==r2.native_dof_status
    def test_self_test(self): assert _self_test() is True
