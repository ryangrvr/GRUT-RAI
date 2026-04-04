"""Tests for U-H --- Final Unified-Field Ledger and Handoff to V."""
import pytest
from grut.uh_final_unified_field_ledger_handoff import (
    N_LEDGER_ITEMS, N_OBSTRUCTIONS, N_V_SETTLED, N_V_FORBIDDEN, N_V_LICENSED,
    N_UH_NONCLAIMS, N_ALLOWED, N_FORBIDDEN, ALLOWED_CLASSIFICATIONS,
    UH_NATIVE, UH_DESCRIPTOR, UH_UNIFICATION, UH_INHERIT, UH_AUTH, UH_OVERALL,
    NATIVE_OPTIONS, DESCRIPTOR_OPTIONS, UNIFICATION_OPTIONS,
    INHERIT_OPTIONS, AUTH_OPTIONS, UH_NONCLAIMS,
    run_uh_final_unified_field_ledger_handoff, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_uh_final_unified_field_ledger_handoff()

class TestConstants:
    def test_nonclaims(self):
        assert len(UH_NONCLAIMS)==N_UH_NONCLAIMS
        for nc in UH_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert UH_NATIVE=="sparse_scalar_dissipative_core_confirmed"
        assert UH_UNIFICATION=="constitutive_architecture_ceiling_confirmed"
        assert UH_OVERALL=="unified_field_ledger_closes_with_sparse_constitutive_architecture"

class TestLedger:
    def test_count(self, result): assert len(result.ledger)==N_LEDGER_ITEMS
    def test_all_valid(self, result):
        for i in result.ledger: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_native_count(self, result):
        n=sum(1 for i in result.ledger if i.classification=="native_established")
        assert n>=5
    def test_action_absent(self, result):
        a=[i for i in result.ledger if i.structure=="action_principle"][0]
        assert a.classification=="absent_unbuilt"
    def test_gauge_absent(self, result):
        g=[i for i in result.ledger if i.structure=="gauge_structure"][0]
        assert g.classification=="absent_unbuilt"
    def test_unified_absent(self, result):
        u=[i for i in result.ledger if i.structure=="unified_field_framework"][0]
        assert u.classification=="absent_unbuilt"

class TestObstructions:
    def test_count(self, result): assert len(result.obstructions)==N_OBSTRUCTIONS
    def test_sequential(self, result):
        for i,o in enumerate(result.obstructions): assert o.rank==i+1

class TestHandoff:
    def test_settled(self, result): assert len(result.handoff.settled_inheritance)==N_V_SETTLED
    def test_forbidden(self, result): assert len(result.handoff.forbidden_assumptions)==N_V_FORBIDDEN
    def test_licensed(self, result): assert len(result.handoff.licensed_questions)==N_V_LICENSED
    def test_vacuum_licensed(self, result):
        text=" ".join(result.handoff.licensed_questions).lower()
        assert "vacuum" in text or "medium" in text or "ontology" in text

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_field_architecture_status in NATIVE_OPTIONS
        assert result.effective_descriptor_status in DESCRIPTOR_OPTIONS
        assert result.unification_completion_status in UNIFICATION_OPTIONS
        assert result.inheritance_status_for_V in INHERIT_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self, result):
        v={result.native_field_architecture_status,result.effective_descriptor_status,
           result.unification_completion_status,result.inheritance_status_for_V,
           result.authorization}
        assert len(v)==5

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self, result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_uh_final_unified_field_ledger_handoff()
        r2=run_uh_final_unified_field_ledger_handoff()
        assert r1.unification_completion_status==r2.unification_completion_status
    def test_self_test(self): assert _self_test() is True
