"""Tests for Appendix S-E --- Unified Sector Ledger and Handoff to T."""
import pytest
from grut.se_unified_sector_ledger_handoff import (
    N_LEDGER_ITEMS, N_SYMMETRY_ITEMS, N_OBSTRUCTIONS,
    N_T_SETTLED, N_T_FORBIDDEN, N_T_LICENSED,
    N_SE_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    ALLOWED_CLASSIFICATIONS,
    SE_NATIVE_VERDICT, SE_EXTENSION_VERDICT, SE_UNIFICATION_VERDICT,
    SE_INHERITANCE_VERDICT, SE_AUTH_VERDICT, SE_OVERALL_P,
    NATIVE_OPTIONS, EXTENSION_OPTIONS, UNIFICATION_OPTIONS,
    INHERITANCE_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    SE_NONCLAIMS,
    run_se_unified_sector_ledger_handoff, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_se_unified_sector_ledger_handoff()

class TestConstants:
    def test_nonclaims(self):
        assert len(SE_NONCLAIMS)==N_SE_NONCLAIMS
        for nc in SE_NONCLAIMS: assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert SE_NATIVE_VERDICT=="scalar_dissipative_native_core_confirmed"
        assert SE_EXTENSION_VERDICT=="extensions_coherent_but_nonfoundational"
        assert SE_UNIFICATION_VERDICT=="sector_layering_only"
        assert SE_INHERITANCE_VERDICT=="thermodynamic_handoff_clean_with_limits"
        assert SE_AUTH_VERDICT=="authorized_to_proceed_to_T"
        assert SE_OVERALL_P=="nonunified_but_stable_sector_ledger"

class TestLedger:
    def test_count(self, result):
        assert len(result.sector_ledger)==N_LEDGER_ITEMS
    def test_all_valid_classification(self, result):
        for i in result.sector_ledger:
            assert i.classification in ALLOWED_CLASSIFICATIONS, i.structure
    def test_native_exact_count(self, result):
        n=sum(1 for i in result.sector_ledger if i.classification=="native_exact")
        assert n==5  # scalar, tau, Z2, parity, dissipation arrow
    def test_native_broken_count(self, result):
        n=sum(1 for i in result.sector_ledger if i.classification=="native_broken")
        assert n==3  # Lorentz, T, scale
    def test_lorentz_broken(self, result):
        lor=[i for i in result.sector_ledger if "lorentz_inv" in i.structure.lower()]
        assert lor[0].classification=="native_broken"
    def test_gauge_absent(self, result):
        g=[i for i in result.sector_ledger if "gauge" in i.structure.lower()]
        assert g[0].classification=="absent_unbuilt"
    def test_fermionic_blocked(self, result):
        f=[i for i in result.sector_ledger if "fermionic" in i.structure.lower()]
        assert f[0].classification=="blocked_by_structure"

class TestSymmetryTable:
    def test_count(self, result):
        assert len(result.symmetry_table)==N_SYMMETRY_ITEMS
    def test_z2_native_exact(self, result):
        z2=[s for s in result.symmetry_table if "Z2" in s.symmetry]
        assert z2[0].native_exact is True
    def test_lorentz_broken(self, result):
        lor=[s for s in result.symmetry_table if "Lorentz inv" in s.symmetry]
        assert lor[0].native_broken is True
    def test_gauge_absent(self, result):
        ga=[s for s in result.symmetry_table if "Gauge" in s.symmetry]
        assert ga[0].absent is True
    def test_o3_extension(self, result):
        o3=[s for s in result.symmetry_table if "O(3) target" in s.symmetry]
        assert len(o3)==1
        assert o3[0].extension_only is True

class TestObstructions:
    def test_count(self, result):
        assert len(result.obstruction_ranking)==N_OBSTRUCTIONS
    def test_sequential(self, result):
        for i,o in enumerate(result.obstruction_ranking):
            assert o.rank==i+1
    def test_fermionic_first(self, result):
        assert "fermionic" in result.obstruction_ranking[0].name.lower()
    def test_born_second(self, result):
        assert "born" in result.obstruction_ranking[1].name.lower()

class TestHandoff:
    def test_settled(self, result):
        assert len(result.handoff.settled_inheritance)==N_T_SETTLED
    def test_forbidden(self, result):
        assert len(result.handoff.forbidden_assumptions)==N_T_FORBIDDEN
    def test_licensed(self, result):
        assert len(result.handoff.licensed_questions)==N_T_LICENSED
    def test_settled_includes_arrow(self, result):
        text=" ".join(result.handoff.settled_inheritance).lower()
        assert "arrow" in text
    def test_forbidden_includes_gauge(self, result):
        text=" ".join(result.handoff.forbidden_assumptions).lower()
        assert "gauge" in text
    def test_licensed_includes_irreversibility(self, result):
        text=" ".join(result.handoff.licensed_questions).lower()
        assert "irreversibility" in text

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.native_sector_status in NATIVE_OPTIONS
        assert result.extension_sector_status in EXTENSION_OPTIONS
        assert result.unification_status in UNIFICATION_OPTIONS
        assert result.inheritance_status_for_T in INHERITANCE_OPTIONS
        assert result.authorization in AUTH_OPTIONS
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_all_distinct(self, result):
        v={result.native_sector_status,result.extension_sector_status,
           result.unification_status,result.inheritance_status_for_T,
           result.authorization}
        assert len(v)==5

class TestDiagnostics:
    def test_native_exact(self, result):
        assert result.diagnostics["n_native_exact"]==5
    def test_native_broken(self, result):
        assert result.diagnostics["n_native_broken"]==3
    def test_obstructions(self, result):
        assert result.diagnostics["n_obstructions"]==8

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims)==N_ALLOWED
        assert len(result.forbidden_claims)==N_FORBIDDEN
    def test_key_findings(self, result):
        assert len(result.key_findings)>=6
    def test_idempotency(self):
        r1=run_se_unified_sector_ledger_handoff()
        r2=run_se_unified_sector_ledger_handoff()
        assert r1.unification_status==r2.unification_status
    def test_self_test(self): assert _self_test() is True
