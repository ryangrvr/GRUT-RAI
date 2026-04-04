"""Tests for U0 --- Unified-Field Entry Inventory."""
import pytest
from grut.u0_unified_field_entry_inventory import (
    N_ITEMS, N_U0_NONCLAIMS, ALLOWED_CLASSIFICATIONS,
    U0_INVENTORY_VERDICT, U0_FIELD_CONTENT, U0_ACTION_STATUS,
    U0_GEOMETRY_STATUS, U0_AUTH, U0_NONCLAIMS,
    run_u0_unified_field_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_u0_unified_field_entry_inventory()

class TestConstants:
    def test_items(self): assert N_ITEMS == 25
    def test_nonclaims(self):
        assert len(U0_NONCLAIMS) == N_U0_NONCLAIMS
        for nc in U0_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestInventory:
    def test_count(self, result): assert result.n_items == N_ITEMS
    def test_all_valid(self, result):
        for i in result.items: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_native_present(self, result): assert result.n_native >= 3
    def test_emergent_present(self, result): assert result.n_emergent >= 5
    def test_absent_present(self, result): assert result.n_absent >= 6
    def test_blocked_present(self, result): assert result.n_blocked >= 3
    def test_action_absent(self, result):
        a = [i for i in result.items if i.item_id == "U13"][0]
        assert a.classification == "absent_unbuilt"
    def test_gauge_absent(self, result):
        g = [i for i in result.items if i.item_id == "U9"][0]
        assert g.classification == "absent_unbuilt"
    def test_counts_sum(self, result):
        total = (result.n_native + result.n_limited + result.n_extension +
                 result.n_emergent + result.n_absent + result.n_blocked + result.n_postulate)
        assert total == result.n_items

class TestVerdicts:
    def test_inventory(self, result): assert result.inventory_verdict == U0_INVENTORY_VERDICT
    def test_field(self, result): assert result.field_content_verdict == U0_FIELD_CONTENT
    def test_action(self, result): assert result.action_status_verdict == U0_ACTION_STATUS
    def test_geometry(self, result): assert result.geometry_status_verdict == U0_GEOMETRY_STATUS
    def test_auth(self, result): assert result.auth_verdict == U0_AUTH

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_idempotency(self):
        r1 = run_u0_unified_field_entry_inventory()
        r2 = run_u0_unified_field_entry_inventory()
        assert r1.n_items == r2.n_items
    def test_self_test(self): assert _self_test() is True
