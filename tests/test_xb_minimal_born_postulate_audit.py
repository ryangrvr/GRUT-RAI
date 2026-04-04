"""Tests for X-B --- Minimal Born Postulate."""
import pytest
from grut.xb_minimal_born_postulate_audit import (
    N_CANDIDATES, N_XB_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    XB_BORN, XB_PREF, XB_INFLATION, XB_SCOPE, XB_AUTH, XB_OVERALL,
    BORN_OPTIONS, PREF_OPTIONS, INFLATION_OPTIONS, SCOPE_OPTIONS, AUTH_OPTIONS,
    XB_NONCLAIMS, run_xb_minimal_born_postulate_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_xb_minimal_born_postulate_audit()

class TestConstants:
    def test_nc(self):
        assert len(XB_NONCLAIMS)==N_XB_NONCLAIMS
        for nc in XB_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestCandidates:
    def test_count(self,result): assert result.n_candidates==N_CANDIDATES
    def test_preferred(self,result): assert "born" in result.recommended.lower()

class TestHardGated:
    def test_all(self,result):
        assert result.born_postulate_status in BORN_OPTIONS
        assert result.preferred_rule_class in PREF_OPTIONS
        assert result.inflation_status in INFLATION_OPTIONS
        assert result.scope_status in SCOPE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.born_postulate_status,result.preferred_rule_class,
           result.inflation_status,result.scope_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_axioms(self,result): assert result.diagnostics["new_axioms"]==1
    def test_dof(self,result): assert result.diagnostics["new_dof"]==0
    def test_objects(self,result): assert result.diagnostics["new_objects"]==0
    def test_norm(self,result): assert result.diagnostics["normalized"] is True
    def test_pos(self,result): assert result.diagnostics["positive"] is True
    def test_no_psi(self,result): assert result.diagnostics["psi_ontology_required"] is False
    def test_no_collapse(self,result): assert result.diagnostics["collapse_required"] is False
    def test_no_completion(self,result): assert result.diagnostics["measurement_completion"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
