"""Tests for X0 --- Probability/Measurement Entry Inventory."""
import pytest
from grut.x0_probability_measurement_entry_inventory import (
    N_ITEMS, N_X0_NONCLAIMS, ALLOWED_CLS,
    X0_INVENTORY, X0_QUANTUM, X0_POSTULATE, X0_NONCLAIMS,
    run_x0_probability_measurement_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_x0_probability_measurement_entry_inventory()

class TestInventory:
    def test_count(self,result): assert result.n_items==N_ITEMS
    def test_valid(self,result):
        for i in result.items: assert i.classification in ALLOWED_CLS
    def test_born_absent(self,result):
        b=[i for i in result.items if i.item_id=="X5"][0]
        assert b.classification=="absent_unbuilt"
    def test_extension_count(self,result): assert result.n_extension>=12
    def test_absent_count(self,result): assert result.n_absent>=6

class TestVerdicts:
    def test_inv(self,result): assert result.inventory_verdict==X0_INVENTORY
    def test_q(self,result): assert result.quantum_content_verdict==X0_QUANTUM
    def test_p(self,result): assert result.postulate_verdict==X0_POSTULATE

class TestDiag:
    def test_born(self,result): assert result.diagnostics["born_rule_present"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_nc(self):
        assert len(X0_NONCLAIMS)==N_X0_NONCLAIMS
        for nc in X0_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_self_test(self): assert _self_test() is True
