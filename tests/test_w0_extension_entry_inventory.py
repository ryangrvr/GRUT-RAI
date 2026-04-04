"""Tests for W0 --- Extension Entry Inventory."""
import pytest
from grut.w0_extension_entry_inventory import (
    N_EXTENSIONS, N_W0_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    W0_VERDICT, W0_NONCLAIMS,
    run_w0_extension_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_w0_extension_entry_inventory()

class TestConstants:
    def test_n(self): assert N_EXTENSIONS==10
    def test_nc(self):
        assert len(W0_NONCLAIMS)==N_W0_NONCLAIMS
        for nc in W0_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestExtensions:
    def test_count(self,result): assert result.n_extensions==N_EXTENSIONS
    def test_sequential(self,result):
        for i,e in enumerate(result.extensions): assert e.rank==i+1
    def test_all_compatible(self,result):
        for e in result.extensions: assert e.book2_compatible is True
    def test_layers(self,result): assert len(result.dependency_layers)==4
    def test_layer0(self,result):
        assert "propagation_sector" in result.dependency_layers[0]
        assert "born_probability" in result.dependency_layers[0]

class TestDiagnostics:
    def test_compat(self,result): assert result.diagnostics["all_book2_compatible"] is True
    def test_smallest(self,result): assert result.diagnostics["smallest_postulate"]=="born_probability"
    def test_structural(self,result): assert result.diagnostics["most_structural"]=="propagation_sector"

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_verdict(self,result): assert result.inventory_verdict==W0_VERDICT
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=5
    def test_self_test(self): assert _self_test() is True
