"""Tests for V-H --- Final Vacuum Ontology Ledger."""
import pytest
from grut.vh_final_vacuum_ontology_ledger import (
    N_LEDGER, N_NOEQUIV, N_FUTURE, N_OBSTRUCTIONS,
    N_VH_NONCLAIMS, N_ALLOWED, N_FORBIDDEN, ALLOWED_CLASSIFICATIONS,
    VH_NATIVE, VH_MANIFEST, VH_CEILING, VH_FUTURE, VH_AUTH, VH_OVERALL,
    NATIVE_OPTIONS, MANIFEST_OPTIONS, CEILING_OPTIONS, FUTURE_OPTIONS,
    AUTH_OPTIONS, VH_NONCLAIMS,
    run_vh_final_vacuum_ontology_ledger, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_vh_final_vacuum_ontology_ledger()

class TestConstants:
    def test_nonclaims(self):
        assert len(VH_NONCLAIMS)==N_VH_NONCLAIMS
        for nc in VH_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert VH_NATIVE=="persistent_scalar_dissipative_substrate_confirmed"
        assert VH_MANIFEST=="source_dependent_manifestation_on_persistent_substrate_confirmed"
        assert VH_CEILING=="distinct_substrate_category_with_strict_limits_confirmed"
        assert VH_AUTH=="appendix_V_closed_book_II_foundation_complete"

class TestLedger:
    def test_count(self,result): assert len(result.ledger)==N_LEDGER
    def test_all_valid(self,result):
        for i in result.ledger: assert i.classification in ALLOWED_CLASSIFICATIONS
    def test_native_count(self,result):
        n=sum(1 for i in result.ledger if i.classification=="native_established")
        assert n>=9

class TestNonEquivalences:
    def test_count(self,result): assert len(result.non_equivalences)==N_NOEQUIV
    def test_aether(self,result):
        assert any("aether" in ne.identity.lower() for ne in result.non_equivalences)
    def test_quantum(self,result):
        assert any("quantum" in ne.identity.lower() for ne in result.non_equivalences)

class TestFuturePostulates:
    def test_count(self,result): assert len(result.future_postulates)==N_FUTURE
    def test_gauge(self,result):
        assert any("gauge" in fp.structure.lower() for fp in result.future_postulates)
    def test_born(self,result):
        assert any("born" in fp.structure.lower() for fp in result.future_postulates)

class TestObstructions:
    def test_count(self,result): assert len(result.obstructions)==N_OBSTRUCTIONS
    def test_sequential(self,result):
        for i,o in enumerate(result.obstructions): assert o.rank==i+1

class TestHardGated:
    def test_all_in_allowed(self,result):
        assert result.native_vacuum_architecture_status in NATIVE_OPTIONS
        assert result.manifestation_status in MANIFEST_OPTIONS
        assert result.ontology_ceiling_status in CEILING_OPTIONS
        assert result.future_boundary_status in FUTURE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
    def test_all_distinct(self,result):
        v={result.native_vacuum_architecture_status,result.manifestation_status,
           result.ontology_ceiling_status,result.future_boundary_status,
           result.authorization}
        assert len(v)==5

class TestMaster:
    def test_valid(self,result): assert result.valid is True
    def test_claims(self,result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key(self,result): assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_vh_final_vacuum_ontology_ledger()
        r2=run_vh_final_vacuum_ontology_ledger()
        assert r1.authorization==r2.authorization
    def test_self_test(self): assert _self_test() is True
