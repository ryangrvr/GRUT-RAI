"""Tests for Y0 --- Quantum-Dynamical Closure Entry Inventory."""
import pytest
from grut.y0_quantum_dynamical_closure_entry_inventory import (
    N_ITEMS, N_Y0_NONCLAIMS, ALLOWED_CLS,
    Y0_INVENTORY, Y0_QUANTUM, Y0_INTERFACE, Y0_NONCLAIMS,
    run_y0_quantum_dynamical_closure_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_y0_quantum_dynamical_closure_entry_inventory()

class TestInventory:
    def test_count(self,result): assert result.n_items==N_ITEMS
    def test_valid(self,result):
        for i in result.items: assert i.classification in ALLOWED_CLS
    def test_absent(self,result): assert result.n_absent>=9
    def test_ext_est(self,result): assert result.n_ext_est>=7

class TestVerdicts:
    def test_inv(self,result): assert result.inventory_verdict==Y0_INVENTORY
    def test_q(self,result): assert result.quantum_status_verdict==Y0_QUANTUM
    def test_i(self,result): assert result.interface_verdict==Y0_INTERFACE

class TestDiag:
    def test_unit(self,result): assert result.diagnostics["unitarity_present"] is False
    def test_evol(self,result): assert result.diagnostics["between_measurement_evolution"] is False

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_nc(self): assert len(Y0_NONCLAIMS)==N_Y0_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
