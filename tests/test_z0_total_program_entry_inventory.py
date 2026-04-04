"""Tests for Z0 --- Total Program Entry Inventory."""
import pytest
from grut.z0_total_program_entry_inventory import (
    TAU_SQ, TAU, N_ITEMS, N_Z0_NONCLAIMS, ALLOWED_CLS,
    Z0_INVENTORY, Z0_CANON, Z0_ABSENCE, Z0_NONCLAIMS,
    run_z0_total_program_entry_inventory, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_z0_total_program_entry_inventory()


class TestConstants:
    def test_tau_sq(self): assert TAU_SQ == 1.5
    def test_tau(self): assert abs(TAU - 1.2247448713916) < 1e-10
    def test_n_items(self): assert N_ITEMS == 32
    def test_n_nc(self): assert N_Z0_NONCLAIMS == 8
    def test_cls_count(self): assert len(ALLOWED_CLS) == 8
    def test_cls_native(self): assert "native_established" in ALLOWED_CLS
    def test_cls_ext(self): assert "extension_established" in ALLOWED_CLS
    def test_cls_absent(self): assert "absent_unbuilt" in ALLOWED_CLS
    def test_cls_blocked(self): assert "blocked_by_structure" in ALLOWED_CLS


class TestItems:
    def test_count(self, result): assert len(result.items) == N_ITEMS
    def test_ids_sequential(self, result):
        for i, it in enumerate(result.items):
            assert it.item_id == f"Z{i+1}"
    def test_all_classified(self, result):
        for it in result.items:
            assert it.classification in ALLOWED_CLS
    def test_z_action_valid(self, result):
        for it in result.items:
            assert it.z_action in ("freeze", "fence")


class TestCounts:
    def test_native(self, result): assert result.n_native >= 8
    def test_ext(self, result): assert result.n_ext >= 10
    def test_absent(self, result): assert result.n_absent >= 6
    def test_blocked(self, result): assert result.n_blocked >= 2
    def test_analogy(self, result): assert result.n_analogy >= 3
    def test_constitutive(self, result): assert result.n_constitutive >= 1
    def test_total(self, result):
        t = (result.n_native + result.n_ext + result.n_operational +
             result.n_analogy + result.n_constitutive + result.n_absent +
             result.n_blocked + result.n_future)
        assert t == result.n_items


class TestVerdicts:
    def test_inventory(self, result): assert result.inventory_verdict == Z0_INVENTORY
    def test_canon(self, result): assert result.canon_verdict == Z0_CANON
    def test_absence(self, result): assert result.absence_verdict == Z0_ABSENCE


class TestDiagnostics:
    def test_n_items(self, result): assert result.diagnostics["n_items"] == N_ITEMS
    def test_ext_total(self, result): assert result.diagnostics["grand_total_extensions"] == 7
    def test_params(self, result): assert result.diagnostics["grand_total_parameters"] == 3
    def test_fields(self, result): assert result.diagnostics["grand_total_new_fields"] == 0
    def test_qm(self, result): assert result.diagnostics["full_qm"] is False
    def test_closure(self, result): assert result.diagnostics["unified_closure"] is False
    def test_toe(self, result): assert result.diagnostics["toe_status"] is False


class TestNonclaims:
    def test_count(self): assert len(Z0_NONCLAIMS) == N_Z0_NONCLAIMS
    def test_prefix(self):
        for nc in Z0_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")


class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_nonclaims(self, result): assert len(result.nonclaims) == N_Z0_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
    def test_idempotent(self):
        r1 = run_z0_total_program_entry_inventory()
        r2 = run_z0_total_program_entry_inventory()
        assert r1.valid == r2.valid
        assert r1.n_items == r2.n_items
        assert r1.inventory_verdict == r2.inventory_verdict
