"""Tests for T0 --- Thermodynamic Entry Inventory."""
import pytest
from grut.t0_thermodynamic_entry_inventory import (
    N_INVENTORY_ITEMS, N_T0_NONCLAIMS, ALLOWED_CLASSIFICATIONS,
    T0_INVENTORY_VERDICT, T0_NATIVE_CONTENT, T0_STATISTICAL_FOUNDATION,
    T0_NONCLAIMS, run_t0_thermodynamic_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_t0_thermodynamic_entry_inventory()

class TestConstants:
    def test_items(self): assert N_INVENTORY_ITEMS == 20
    def test_nonclaims(self):
        assert len(T0_NONCLAIMS) == N_T0_NONCLAIMS
        for nc in T0_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestInventory:
    def test_count(self, result): assert result.n_items == N_INVENTORY_ITEMS
    def test_all_valid(self, result):
        for i in result.items: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_dissipation_native(self, result):
        assert result.items[0].classification == "present_native"
    def test_entropy_absent(self, result):
        t7 = [i for i in result.items if i.item_id == "T7"][0]
        assert t7.classification == "absent_unbuilt"
    def test_temperature_absent(self, result):
        t9 = [i for i in result.items if i.item_id == "T9"][0]
        assert t9.classification == "absent_unbuilt"
    def test_probability_blocked(self, result):
        t13 = [i for i in result.items if i.item_id == "T13"][0]
        assert t13.classification == "blocked_by_structure"
    def test_counts_sum(self, result):
        total = (result.n_present_native + result.n_present_limited +
                 result.n_absent + result.n_blocked +
                 result.n_extension + result.n_new_postulate)
        assert total == result.n_items
    def test_native_present_count(self, result):
        assert result.n_present_native >= 3
    def test_absent_count(self, result):
        assert result.n_absent >= 7

class TestVerdicts:
    def test_inventory(self, result):
        assert result.inventory_verdict == T0_INVENTORY_VERDICT
    def test_native(self, result):
        assert result.native_content_verdict == T0_NATIVE_CONTENT
    def test_statistical(self, result):
        assert result.statistical_foundation_verdict == T0_STATISTICAL_FOUNDATION

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_idempotency(self):
        r1 = run_t0_thermodynamic_entry_inventory()
        r2 = run_t0_thermodynamic_entry_inventory()
        assert r1.n_items == r2.n_items
    def test_self_test(self): assert _self_test() is True
