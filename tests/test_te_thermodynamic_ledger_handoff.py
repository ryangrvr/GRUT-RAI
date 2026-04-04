"""Tests for T-E --- Final Thermodynamic Ledger and Handoff to U."""
import pytest
from grut.te_thermodynamic_ledger_handoff import (
    N_LEDGER_ITEMS, N_OBSTRUCTIONS, N_U_SETTLED, N_U_FORBIDDEN, N_U_LICENSED,
    N_TE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN, ALLOWED_CLASSIFICATIONS,
    TE_NATIVE_VERDICT, TE_BOOKKEEPING_VERDICT, TE_THERMAL_VERDICT,
    TE_INHERIT_VERDICT, TE_AUTH_VERDICT, TE_OVERALL_P,
    NATIVE_OPTIONS, BOOKKEEPING_OPTIONS, THERMAL_OPTIONS,
    INHERIT_OPTIONS, AUTH_OPTIONS, TE_NONCLAIMS,
    run_te_thermodynamic_ledger_handoff, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_te_thermodynamic_ledger_handoff()

class TestConstants:
    def test_nonclaims(self):
        assert len(TE_NONCLAIMS) == N_TE_NONCLAIMS
        for nc in TE_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert TE_NATIVE_VERDICT == "irreversible_dissipative_core_confirmed"
        assert TE_BOOKKEEPING_VERDICT == "lyapunov_and_balance_ledger_confirmed"
        assert TE_THERMAL_VERDICT == "equilibrium_and_temperature_absent"
        assert TE_OVERALL_P == "irreversible_dissipative_ledger_closed_without_thermal_completion"

class TestLedger:
    def test_count(self, result): assert len(result.ledger) == N_LEDGER_ITEMS
    def test_all_valid(self, result):
        for i in result.ledger: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_native_count(self, result):
        n = sum(1 for i in result.ledger if i.classification == "native_established")
        assert n >= 9
    def test_entropy_absent(self, result):
        ent = [i for i in result.ledger if i.structure == "entropy"][0]
        assert ent.classification == "absent_unbuilt"
    def test_temperature_absent(self, result):
        temp = [i for i in result.ledger if i.structure == "temperature"][0]
        assert temp.classification == "absent_unbuilt"
    def test_probability_blocked(self, result):
        prob = [i for i in result.ledger if i.structure == "probability_foundation"][0]
        assert prob.classification == "blocked_by_structure"

class TestObstructions:
    def test_count(self, result): assert len(result.obstructions) == N_OBSTRUCTIONS
    def test_sequential(self, result):
        for i, o in enumerate(result.obstructions): assert o.rank == i + 1
    def test_probability_first(self, result):
        assert "probability" in result.obstructions[0].name.lower()

class TestHandoff:
    def test_settled(self, result):
        assert len(result.handoff.settled_inheritance) == N_U_SETTLED
    def test_forbidden(self, result):
        assert len(result.handoff.forbidden_assumptions) == N_U_FORBIDDEN
    def test_licensed(self, result):
        assert len(result.handoff.licensed_questions) == N_U_LICENSED
    def test_entropy_forbidden(self, result):
        text = " ".join(result.handoff.forbidden_assumptions).lower()
        assert "entropy" in text
    def test_action_licensed(self, result):
        text = " ".join(result.handoff.licensed_questions).lower()
        assert "action" in text

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_thermodynamic_status in NATIVE_OPTIONS
        assert result.bookkeeping_status in BOOKKEEPING_OPTIONS
        assert result.thermal_completion_status in THERMAL_OPTIONS
        assert result.inheritance_status_for_U in INHERIT_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v = {result.native_thermodynamic_status, result.bookkeeping_status,
             result.thermal_completion_status, result.inheritance_status_for_U,
             result.authorization}
        assert len(v) == 5

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result): assert len(result.key_findings) >= 6
    def test_idempotency(self):
        r1 = run_te_thermodynamic_ledger_handoff()
        r2 = run_te_thermodynamic_ledger_handoff()
        assert r1.thermal_completion_status == r2.thermal_completion_status
    def test_self_test(self): assert _self_test() is True
