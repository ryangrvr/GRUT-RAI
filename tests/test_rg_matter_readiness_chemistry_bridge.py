"""Tests for Appendix R-G --- Matter-Readiness to Chemistry Bridge."""
import pytest
from grut.rg_matter_readiness_chemistry_bridge import (
    N_MATTER_INVENTORY_ITEMS, N_CHEMISTRY_PREREQS, N_BRIDGE_CONDITIONS,
    N_READINESS_DOMAINS, N_APPENDIX_P_ENTRIES, N_RG_NONCLAIMS,
    N_ALLOWED_CLAIMS, N_FORBIDDEN_CLAIMS,
    RG_BOSONIC_VERDICT, RG_FERMIONIC_VERDICT,
    RG_CHEMISTRY_BOUNDARY_VERDICT, RG_BRIDGE_CONDITION_VERDICT,
    RG_FINAL_MATTER_VERDICT, RG_OVERALL_APPENDIX_P_CLASS,
    ALLOWED_BOSONIC_VERDICTS, ALLOWED_FERMIONIC_VERDICTS,
    ALLOWED_CHEMISTRY_VERDICTS, ALLOWED_BRIDGE_VERDICTS,
    ALLOWED_FINAL_VERDICTS, ALLOWED_APPENDIX_P_CLASSES,
    ALLOWED_READINESS_LEVELS, RG_NONCLAIMS,
    run_rg_matter_readiness_chemistry_bridge, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_rg_matter_readiness_chemistry_bridge()

class TestRGConstants:
    def test_counts(self):
        assert N_MATTER_INVENTORY_ITEMS == 10
        assert N_CHEMISTRY_PREREQS == 6
        assert N_BRIDGE_CONDITIONS == 6
        assert N_RG_NONCLAIMS == 8
    def test_nonclaims(self):
        assert len(RG_NONCLAIMS) == N_RG_NONCLAIMS
        for nc in RG_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_verdicts(self):
        assert RG_BOSONIC_VERDICT == "bosonic_matter_scaffold_established"
        assert RG_FERMIONIC_VERDICT == "fermionic_matter_blocked_but_route_inventory_complete"
        assert RG_CHEMISTRY_BOUNDARY_VERDICT == "chemistry_boundary_precisely_mapped"
        assert RG_BRIDGE_CONDITION_VERDICT == "minimum_chemistry_bridge_conditions_identified"
        assert RG_FINAL_MATTER_VERDICT == "matter_program_complete_as_pre_chemistry_ledger"

class TestTrackAInventory:
    def test_n_items(self, result):
        assert result.track_a_inventory.n_items == N_MATTER_INVENTORY_ITEMS
    def test_zero_achieved(self, result):
        assert result.track_a_inventory.n_achieved == 0
    def test_five_extension(self, result):
        assert result.track_a_inventory.n_extension == 5
    def test_binding_blocked(self, result):
        mi6 = result.track_a_inventory.items[5]
        assert mi6.status == "blocked"
    def test_fermionic_blocked(self, result):
        mi9 = result.track_a_inventory.items[8]
        assert mi9.status == "blocked"

class TestTrackBChemistry:
    def test_all_unmet(self, result):
        assert result.track_b_chemistry_prereqs.n_met == 0
        assert result.track_b_chemistry_prereqs.n_unmet == N_CHEMISTRY_PREREQS

class TestTrackCBosonic:
    def test_no_chemistry_from_bosons(self, result):
        assert result.track_c_bosonic_limit.chemistry_from_bosons_alone is False

class TestTrackEProbability:
    def test_born_required(self, result):
        assert result.track_e_probability.born_required_for_chemistry is True

class TestTrackFBridge:
    def test_n_conditions(self, result):
        assert result.track_f_bridge.n_conditions == N_BRIDGE_CONDITIONS
    def test_zero_met(self, result):
        assert result.track_f_bridge.n_met == 0
    def test_all_unmet(self, result):
        assert result.track_f_bridge.n_unmet == N_BRIDGE_CONDITIONS

class TestTrackGReadiness:
    def test_n_entries(self, result):
        assert result.track_g_readiness.n_entries == N_READINESS_DOMAINS
    def test_all_valid(self, result):
        for e in result.track_g_readiness.entries:
            assert e.readiness_level in ALLOWED_READINESS_LEVELS
    def test_chemistry_blocked(self, result):
        chem = [e for e in result.track_g_readiness.entries if "chemistry_pre" in e.domain]
        assert chem[0].readiness_level == "blocked"

class TestTrackHAppendixP:
    def test_no_native_canon(self, result):
        assert result.track_h_appendix_p.no_native_canon is True
    def test_overall_bsr(self, result):
        assert result.track_h_appendix_p.overall_class == "bounded_structural_result"

class TestHardGatedVerdicts:
    def test_all_exact(self, result):
        assert result.bosonic_matter_verdict == RG_BOSONIC_VERDICT
        assert result.fermionic_matter_verdict == RG_FERMIONIC_VERDICT
        assert result.chemistry_boundary_verdict == RG_CHEMISTRY_BOUNDARY_VERDICT
        assert result.bridge_condition_verdict == RG_BRIDGE_CONDITION_VERDICT
        assert result.final_matter_verdict == RG_FINAL_MATTER_VERDICT
    def test_all_in_allowed(self, result):
        assert result.bosonic_matter_verdict in ALLOWED_BOSONIC_VERDICTS
        assert result.fermionic_matter_verdict in ALLOWED_FERMIONIC_VERDICTS
        assert result.chemistry_boundary_verdict in ALLOWED_CHEMISTRY_VERDICTS
        assert result.bridge_condition_verdict in ALLOWED_BRIDGE_VERDICTS
        assert result.final_matter_verdict in ALLOWED_FINAL_VERDICTS
    def test_all_distinct(self, result):
        v = {result.bosonic_matter_verdict, result.fermionic_matter_verdict,
             result.chemistry_boundary_verdict, result.bridge_condition_verdict,
             result.final_matter_verdict}
        assert len(v) == 5

class TestMasterAudit:
    def test_valid(self, result):
        assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED_CLAIMS
        assert len(result.forbidden_claims) == N_FORBIDDEN_CLAIMS
    def test_diagnostics(self, result):
        assert result.diagnostics["n_prereqs_met"] == 0
        assert result.diagnostics["n_bridge_met"] == 0
        assert result.diagnostics["chemistry_from_bosons_alone"] is False
        assert result.diagnostics["born_required_for_chemistry"] is True
    def test_idempotency(self):
        r1 = run_rg_matter_readiness_chemistry_bridge()
        r2 = run_rg_matter_readiness_chemistry_bridge()
        assert r1.final_matter_verdict == r2.final_matter_verdict
    def test_self_test(self):
        assert _self_test() is True
