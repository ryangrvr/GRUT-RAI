"""Tests for V0 --- Vacuum Ontology Entry Inventory."""
import pytest
from grut.v0_vacuum_ontology_entry_inventory import (
    N_ITEMS, N_V0_NONCLAIMS, ALLOWED_CLASSIFICATIONS,
    V0_INVENTORY, V0_VACUUM, V0_SOURCE, V0_NONCLAIMS,
    run_v0_vacuum_ontology_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_v0_vacuum_ontology_entry_inventory()

class TestConstants:
    def test_items(self): assert N_ITEMS==25
    def test_nonclaims(self):
        assert len(V0_NONCLAIMS)==N_V0_NONCLAIMS
        for nc in V0_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestInventory:
    def test_count(self,result): assert result.n_items==N_ITEMS
    def test_all_valid(self,result):
        for i in result.items: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_native_count(self,result): assert result.n_native>=6
    def test_counts_sum(self,result):
        total=result.n_native+result.n_limited+result.n_constitutive+result.n_extension+result.n_absent+result.n_blocked+result.n_postulate
        assert total==result.n_items
    def test_quantum_blocked(self,result):
        q=[i for i in result.items if i.item_id=="V13"][0]
        assert q.classification=="blocked_by_structure"

class TestVerdicts:
    def test_inventory(self,result): assert result.inventory_verdict==V0_INVENTORY
    def test_vacuum(self,result): assert result.vacuum_verdict==V0_VACUUM
    def test_source(self,result): assert result.source_verdict==V0_SOURCE

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_idempotency(self):
        r1=run_v0_vacuum_ontology_entry_inventory()
        r2=run_v0_vacuum_ontology_entry_inventory()
        assert r1.n_items==r2.n_items
    def test_self_test(self): assert _self_test() is True
