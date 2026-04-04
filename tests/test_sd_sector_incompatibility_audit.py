"""Tests for Appendix S-D --- Sector Incompatibilities."""
import pytest
from grut.sd_sector_incompatibility_audit import (
    SD_TOPO_DISS_VERDICT, SD_OBS_CONST_VERDICT, SD_SCALE_VERDICT,
    SD_SECTOR_VERDICT, SD_AUTH_VERDICT, SD_OVERALL_P,
    TOPO_DISS_OPTIONS, OBS_CONST_OPTIONS, SCALE_OPTIONS,
    SECTOR_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    N_EVIDENCE_ROWS, N_OBSTRUCTIONS, N_SD_NONCLAIMS,
    N_ALLOWED, N_FORBIDDEN, SD_NONCLAIMS,
    run_sd_sector_incompatibility_audit, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_sd_sector_incompatibility_audit()

class TestVerdictConstants:
    def test_topo(self):
        assert SD_TOPO_DISS_VERDICT == "topological_protection_survives_only_conditionally"
    def test_obs(self):
        assert SD_OBS_CONST_VERDICT == "carrier_space_mismatch_no_derivation"
    def test_scale(self):
        assert SD_SCALE_VERDICT == "multiple_unbridged_scales_persist"
    def test_sector(self):
        assert SD_SECTOR_VERDICT == "mutually_independent_layers"
    def test_auth(self):
        assert SD_AUTH_VERDICT == "authorized_to_proceed_to_SE"
    def test_overall(self):
        assert SD_OVERALL_P == "layered_but_nonunified"

class TestNonclaims:
    def test_count(self):
        assert len(SD_NONCLAIMS) == N_SD_NONCLAIMS
    def test_start(self):
        for nc in SD_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")

class TestTrackA:
    def test_findings(self, result):
        assert len(result.track_a_topo_diss.findings) >= 4
    def test_friction(self, result):
        assert len(result.track_a_topo_diss.friction_points) >= 3
    def test_verdict(self, result):
        assert result.track_a_topo_diss.verdict_contribution == SD_TOPO_DISS_VERDICT

class TestTrackB:
    def test_findings(self, result):
        assert len(result.track_b_obs_const.findings) >= 4
    def test_friction(self, result):
        text = " ".join(result.track_b_obs_const.friction_points).lower()
        assert "mismatch" in text or "carrier" in text

class TestTrackC:
    def test_findings(self, result):
        assert len(result.track_c_scale.findings) >= 5
    def test_mentions_tau(self, result):
        text = " ".join(result.track_c_scale.findings).lower()
        assert "tau" in text

class TestTrackD:
    def test_findings(self, result):
        assert len(result.track_d_closure.findings) >= 4
    def test_no_common(self, result):
        text = " ".join(result.track_d_closure.findings).lower()
        assert "no common" in text or "no single" in text

class TestTrackE:
    def test_7_breaks(self, result):
        text = " ".join(result.track_e_native_persist.findings).lower()
        assert "persists" in text
    def test_verdict(self, result):
        assert "persist" in result.track_e_native_persist.verdict_contribution.lower()

class TestTrackF:
    def test_findings(self, result):
        assert len(result.track_f_thermo.findings) >= 4

class TestEvidenceTable:
    def test_rows(self, result):
        assert len(result.evidence_table) == N_EVIDENCE_ROWS
    def test_last_row_combined(self, result):
        last = result.evidence_table[-1]
        assert "ALL" in last.pair or "all" in last.pair.lower()
        assert "independent" in last.row_verdict.lower()
    def test_fermionic_blocked(self, result):
        ferm = [r for r in result.evidence_table if "fermionic" in r.pair.lower()]
        assert len(ferm) == 1
        assert "blocked" in ferm[0].row_verdict.lower()

class TestObstructions:
    def test_count(self, result):
        assert len(result.obstruction_ranking) == N_OBSTRUCTIONS
    def test_sequential(self, result):
        for i, obs in enumerate(result.obstruction_ranking):
            assert obs.rank == i + 1
    def test_fermionic_first(self, result):
        assert "fermionic" in result.obstruction_ranking[0].obstruction_name.lower()
    def test_born_second(self, result):
        assert "born" in result.obstruction_ranking[1].obstruction_name.lower()

class TestHardGated:
    def test_all_in_allowed(self, result):
        assert result.topological_dissipative_status in TOPO_DISS_OPTIONS
        assert result.observable_constitutive_status in OBS_CONST_OPTIONS
        assert result.scale_status in SCALE_OPTIONS
        assert result.sector_relation in SECTOR_OPTIONS
        assert result.authorization in AUTH_OPTIONS
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_all_distinct(self, result):
        v = {result.topological_dissipative_status,
             result.observable_constitutive_status,
             result.scale_status, result.sector_relation,
             result.authorization}
        assert len(v) == 5

class TestDiagnostics:
    def test_no_common_carrier(self, result):
        assert result.diagnostics["common_carrier_found"] is False
    def test_no_closure(self, result):
        assert result.diagnostics["transformation_closure_found"] is False
    def test_no_contradiction(self, result):
        assert result.diagnostics["any_contradiction_found"] is False
    def test_native_breaks(self, result):
        assert result.diagnostics["n_native_breaks_persisting"] == 7
    def test_derived_scales(self, result):
        assert result.diagnostics["n_derived_scale_relations"] == 1

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_claims(self, result):
        assert len(result.allowed_claims) == N_ALLOWED
        assert len(result.forbidden_claims) == N_FORBIDDEN
    def test_key_findings(self, result):
        assert len(result.key_findings) >= 6
    def test_nonclaims(self, result):
        assert len(result.exact_nonclaims) == N_SD_NONCLAIMS
    def test_idempotency(self):
        r1 = run_sd_sector_incompatibility_audit()
        r2 = run_sd_sector_incompatibility_audit()
        assert r1.sector_relation == r2.sector_relation
    def test_self_test(self):
        assert _self_test() is True
