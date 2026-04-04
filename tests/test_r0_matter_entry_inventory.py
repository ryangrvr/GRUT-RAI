"""Tests for Appendix R0 --- Matter Entry Inventory."""
import pytest
from grut.r0_matter_entry_inventory import (
    N_TOTAL_ITEMS, N_CATEGORY_A_ITEMS, N_CATEGORY_B_ITEMS,
    N_CATEGORY_C_ITEMS, N_CATEGORY_D_ITEMS, N_CATEGORY_E_ITEMS,
    N_CATEGORY_F_ITEMS, N_R0_NONCLAIMS, N_HARD_RULES,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    ALLOWED_PRESENCE_STATES, ALLOWED_APPENDIX_P_CLASSES, ALLOWED_CATEGORY_LABELS,
    R0_INVENTORY_VERDICT, R0_NONCLAIMS, HARD_EPISTEMIC_RULES,
    run_r0_matter_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_r0_matter_entry_inventory()

class TestR0Constants:
    def test_total(self):
        s = N_CATEGORY_A_ITEMS + N_CATEGORY_B_ITEMS + N_CATEGORY_C_ITEMS + \
            N_CATEGORY_D_ITEMS + N_CATEGORY_E_ITEMS + N_CATEGORY_F_ITEMS
        assert s == N_TOTAL_ITEMS
    def test_nonclaims(self):
        assert len(R0_NONCLAIMS) == N_R0_NONCLAIMS
        for nc in R0_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_hard_rules(self):
        assert len(HARD_EPISTEMIC_RULES) == N_HARD_RULES
    def test_verdict_string(self):
        assert "inventory_complete" in R0_INVENTORY_VERDICT

class TestCategoryA:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "A_bosonic_ready")
        assert n == N_CATEGORY_A_ITEMS
    def test_a1_present(self, result):
        a1 = [i for i in result.items if i.item_id == "A1"][0]
        assert a1.presence_state == "present"

class TestCategoryB:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "B_matter_blocking_gaps")
        assert n == N_CATEGORY_B_ITEMS
    def test_all_absent(self, result):
        for i in result.items:
            if i.category == "B_matter_blocking_gaps":
                assert i.presence_state == "absent"

class TestCategoryC:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "C_fermionic_blockers")
        assert n == N_CATEGORY_C_ITEMS
    def test_c1_blocked(self, result):
        c1 = [i for i in result.items if i.item_id == "C1"][0]
        assert c1.presence_state == "blocked"

class TestCategoryD:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "D_probability_constraints")
        assert n == N_CATEGORY_D_ITEMS
    def test_d1_present(self, result):
        d1 = [i for i in result.items if i.item_id == "D1"][0]
        assert d1.presence_state == "present"
    def test_d3_absent(self, result):
        d3 = [i for i in result.items if i.item_id == "D3"][0]
        assert d3.presence_state == "absent"

class TestCategoryE:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "E_extension_chain")
        assert n == N_CATEGORY_E_ITEMS
    def test_all_extension_ready(self, result):
        for i in result.items:
            if i.category == "E_extension_chain":
                assert i.presence_state == "extension_ready"

class TestCategoryF:
    def test_count(self, result):
        n = sum(1 for i in result.items if i.category == "F_matter_readiness_domains")
        assert n == N_CATEGORY_F_ITEMS
    def test_f5_blocked(self, result):
        f5 = [i for i in result.items if i.item_id == "F5"][0]
        assert f5.presence_state == "blocked"
    def test_f8_absent(self, result):
        f8 = [i for i in result.items if i.item_id == "F8"][0]
        assert f8.presence_state == "absent"

class TestCounts:
    def test_total(self, result):
        assert result.n_total == N_TOTAL_ITEMS
    def test_unique_ids(self, result):
        ids = [i.item_id for i in result.items]
        assert len(ids) == len(set(ids))
    def test_all_states_valid(self, result):
        for i in result.items:
            assert i.presence_state in ALLOWED_PRESENCE_STATES
    def test_all_classes_valid(self, result):
        for i in result.items:
            assert i.appendix_p_class in ALLOWED_APPENDIX_P_CLASSES
    def test_all_categories_valid(self, result):
        for i in result.items:
            assert i.category in ALLOWED_CATEGORY_LABELS

class TestReadiness:
    def test_ready_for_rb(self, result):
        assert result.readiness_assessment.ready_for_rb is True
    def test_fermionic_preserved(self, result):
        assert result.readiness_assessment.fermionic_obstruction_preserved is True
    def test_probability_preserved(self, result):
        assert result.readiness_assessment.probability_boundary_preserved is True

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_verdict(self, result):
        assert result.inventory_verdict == R0_INVENTORY_VERDICT
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_idempotency(self):
        r1 = run_r0_matter_entry_inventory()
        r2 = run_r0_matter_entry_inventory()
        assert r1.n_total == r2.n_total
    def test_self_test(self):
        assert _self_test() is True
