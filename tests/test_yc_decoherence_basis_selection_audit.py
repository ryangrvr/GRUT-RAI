"""Tests for Y-C --- Decoherence, Pointer Basis, Basis-Selection."""
import pytest
from grut.yc_decoherence_basis_selection_audit import (
    N_CANDIDATES, N_YC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    YC_DECOH, YC_BASIS, YC_COLLAPSE, YC_APP, YC_AUTH, YC_OVERALL,
    DECOH_OPTIONS, BASIS_OPTIONS, COLLAPSE_OPTIONS, APP_OPTIONS, AUTH_OPTIONS,
    YC_NONCLAIMS, run_yc_decoherence_basis_selection_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_yc_decoherence_basis_selection_audit()

class TestHardGated:
    def test_all(self,result):
        assert result.decoherence_status in DECOH_OPTIONS
        assert result.basis_status in BASIS_OPTIONS
        assert result.collapse_boundary_status in COLLAPSE_OPTIONS
        assert result.apparatus_boundary_status in APP_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.decoherence_status,result.basis_status,
           result.collapse_boundary_status,result.apparatus_boundary_status,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_axioms(self,result): assert result.diagnostics["new_axioms"]==0
    def test_decoh(self,result): assert result.diagnostics["decoherence_demonstrated"] is True
    def test_basis(self,result): assert result.diagnostics["pointer_basis_identified"] is True
    def test_collapse(self,result): assert result.diagnostics["collapse_imported"] is False
    def test_app(self,result): assert result.diagnostics["apparatus_required"] is False
    def test_x_compat(self,result): assert result.diagnostics["compatible_with_x_stack"] is True
    def test_yb_compat(self,result): assert result.diagnostics["compatible_with_yb_evolution"] is True

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_nc(self): assert len(YC_NONCLAIMS)==N_YC_NONCLAIMS
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
