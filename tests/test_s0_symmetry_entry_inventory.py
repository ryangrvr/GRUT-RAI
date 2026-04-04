"""Tests for Appendix S0 --- Symmetry Entry Inventory."""
import pytest
from grut.s0_symmetry_entry_inventory import (
    N_TOTAL, N_CAT_A, N_CAT_B, N_CAT_C, N_CAT_D, N_CAT_E,
    N_S0_NONCLAIMS, N_HARD_RULES, N_ALLOWED, N_FORBIDDEN,
    ALLOWED_STATES, ALLOWED_P_CLASSES, ALLOWED_CATS,
    S0_VERDICT, S0_NONCLAIMS,
    run_s0_symmetry_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_s0_symmetry_entry_inventory()

class TestConstants:
    def test_total(self):
        assert N_CAT_A+N_CAT_B+N_CAT_C+N_CAT_D+N_CAT_E == N_TOTAL
    def test_nonclaims(self):
        assert len(S0_NONCLAIMS)==N_S0_NONCLAIMS
        for nc in S0_NONCLAIMS: assert nc.startswith("NOT_claiming_")

class TestInventory:
    def test_total(self, result): assert result.n_total==N_TOTAL
    def test_unique_ids(self, result):
        ids=[i.item_id for i in result.items]; assert len(ids)==len(set(ids))
    def test_all_states_valid(self, result):
        for i in result.items: assert i.presence_state in ALLOWED_STATES
    def test_all_classes_valid(self, result):
        for i in result.items: assert i.appendix_p_class in ALLOWED_P_CLASSES
    def test_all_cats_valid(self, result):
        for i in result.items: assert i.category in ALLOWED_CATS

class TestCategoryA:
    def test_count(self, result):
        assert sum(1 for i in result.items if i.category=="A_native_scalar")==N_CAT_A
    def test_all_present(self, result):
        for i in result.items:
            if i.category=="A_native_scalar": assert i.presence_state=="present"

class TestCategoryD:
    def test_d1_blocked(self, result):
        d1=[i for i in result.items if i.item_id=="D1"][0]
        assert d1.presence_state=="blocked"

class TestCategoryE:
    def test_count(self, result):
        assert sum(1 for i in result.items if i.category=="E_sector_relations")==N_CAT_E
    def test_e3_blocked(self, result):
        e3=[i for i in result.items if i.item_id=="E3"][0]
        assert e3.presence_state=="blocked"

class TestReadiness:
    def test_ready(self, result): assert result.readiness.ready_for_sb is True

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_verdict(self, result): assert result.inventory_verdict==S0_VERDICT
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_idempotency(self):
        r1=run_s0_symmetry_entry_inventory()
        r2=run_s0_symmetry_entry_inventory()
        assert r1.n_total==r2.n_total
    def test_self_test(self): assert _self_test() is True
