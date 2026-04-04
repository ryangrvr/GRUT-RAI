"""Tests for W-H --- Final Extension Ledger and Book III Closure."""
import pytest
from grut.wh_final_extension_ledger_book_iii_closure import (
    N_LEDGER, N_MISSING, N_WH_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    ALLOWED_CLASSIFICATIONS,
    WH_ARCH, WH_GRAV, WH_COMP, WH_FUTURE, WH_AUTH, WH_OVERALL,
    EXT_ARCH_OPTIONS, GRAV_OPTIONS, COMP_OPTIONS, FUTURE_OPTIONS, AUTH_OPTIONS,
    WH_NONCLAIMS, run_wh_final_extension_ledger, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_wh_final_extension_ledger()

class TestLedger:
    def test_count(self,result): assert len(result.ledger)==N_LEDGER
    def test_valid(self,result):
        for i in result.ledger: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_established(self,result):
        n=sum(1 for i in result.ledger if i.classification=="extension_established")
        assert n>=6

class TestMissing:
    def test_count(self,result): assert len(result.missing_structures)==N_MISSING
    def test_seq(self,result):
        for i,m in enumerate(result.missing_structures): assert m.rank==i+1

class TestHardGated:
    def test_all(self,result):
        assert result.extension_architecture_status in EXT_ARCH_OPTIONS
        assert result.gravity_extension_status in GRAV_OPTIONS
        assert result.completion_status in COMP_OPTIONS
        assert result.future_boundary_status in FUTURE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_distinct(self,result):
        v={result.extension_architecture_status,result.gravity_extension_status,
           result.completion_status,result.future_boundary_status,result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_postulates(self,result): assert result.diagnostics["total_new_postulates"]==4
    def test_params(self,result): assert result.diagnostics["total_new_parameters"]==3
    def test_fields(self,result): assert result.diagnostics["total_new_fields"]==0
    def test_book2(self,result): assert result.diagnostics["book_ii_immutable"] is True
    def test_gr(self,result): assert result.diagnostics["gr_derived"] is False
    def test_born(self,result): assert result.diagnostics["born_adopted"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_self_test(self): assert _self_test() is True
