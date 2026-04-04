"""Tests for Z-C --- Total Canon Map and Final ToE-Status Boundary Audit."""
import pytest
from grut.zc_total_canon_map_toe_boundary import (
    N_CANON_ENTRIES, N_TOE_CANDIDATES, N_SCOPE_SECTORS, N_MISSING_SECTORS,
    N_LANGUAGE_LEVELS, N_ZC_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    CANON_CLASSIFICATIONS, TOE_CANDIDATE_LABELS, SCOPE_VERDICTS,
    MISSING_SEVERITY,
    CANON_MAP_OPTIONS, TOE_STATUS_OPTIONS, WORLD_MODEL_OPTIONS,
    MISSING_SECTOR_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    ZC_CANON_MAP, ZC_TOE, ZC_WORLD_MODEL, ZC_MISSING, ZC_AUTH, ZC_OVERALL,
    ZC_NONCLAIMS,
    run_zc_total_canon_map_toe_boundary, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_zc_total_canon_map_toe_boundary()


# ── Constants ──

class TestConstants:
    def test_canon_entries(self): assert N_CANON_ENTRIES == 32
    def test_toe_candidates(self): assert N_TOE_CANDIDATES == 4
    def test_scope_sectors(self): assert N_SCOPE_SECTORS == 6
    def test_missing_sectors(self): assert N_MISSING_SECTORS == 10
    def test_language_levels(self): assert N_LANGUAGE_LEVELS == 5
    def test_nonclaims(self): assert N_ZC_NONCLAIMS == 8
    def test_allowed(self): assert N_ALLOWED == 7
    def test_forbidden(self): assert N_FORBIDDEN == 7
    def test_canon_cls_count(self): assert len(CANON_CLASSIFICATIONS) == 8


# ── Track A: Canon Map ──

class TestCanonMap:
    def test_count(self, result):
        assert len(result.canon_map) >= N_CANON_ENTRIES
    def test_classifications_valid(self, result):
        for c in result.canon_map:
            assert c.classification in CANON_CLASSIFICATIONS
    def test_native_count(self, result):
        assert result.n_native >= 8
    def test_extension_count(self, result):
        assert result.n_extension >= 10
    def test_absent_count(self, result):
        assert result.n_absent >= 6
    def test_blocked_count(self, result):
        assert result.n_blocked >= 2
    def test_analogy_count(self, result):
        assert result.n_analogy >= 3
    def test_constitutive_count(self, result):
        assert result.n_constitutive >= 1
    def test_total_consistent(self, result):
        total = (result.n_native + result.n_extension + result.n_operational +
                 result.n_analogy + result.n_constitutive + result.n_absent +
                 result.n_blocked + result.n_future)
        assert total == len(result.canon_map)
    def test_ids_unique(self, result):
        ids = [c.entry_id for c in result.canon_map]
        assert len(ids) == len(set(ids))
    def test_capstone_treatments(self, result):
        for c in result.canon_map:
            assert c.capstone_treatment in ("freeze", "fence", "document")
    def test_native_entries_freeze(self, result):
        for c in result.canon_map:
            if c.classification == "native_canon":
                assert c.capstone_treatment == "freeze"
    def test_absent_entries_document(self, result):
        for c in result.canon_map:
            if c.classification == "absent_unbuilt":
                assert c.capstone_treatment == "document"


# ── Track B: ToE Status ──

class TestToEStatus:
    def test_candidate_count(self, result):
        assert len(result.toe_candidates) == N_TOE_CANDIDATES
    def test_labels_valid(self, result):
        for t in result.toe_candidates:
            assert t.label in TOE_CANDIDATE_LABELS
    def test_exactly_one_supported(self, result):
        supported = [t for t in result.toe_candidates if t.supported]
        assert len(supported) == 1
    def test_supported_is_bounded(self, result):
        supported = [t for t in result.toe_candidates if t.supported][0]
        assert supported.label == "bounded_world_model_framework_with_explicit_gaps"
    def test_full_toe_rejected(self, result):
        full = [t for t in result.toe_candidates
                if t.label == "full_toe_completion"][0]
        assert not full.supported
    def test_complete_foundational_rejected(self, result):
        cf = [t for t in result.toe_candidates
              if t.label == "complete_foundational_toe_architecture"][0]
        assert not cf.supported
    def test_partial_toe_rejected(self, result):
        pt = [t for t in result.toe_candidates
              if t.label == "bounded_partial_toe"][0]
        assert not pt.supported
    def test_strongest_label(self, result):
        assert "bounded" in result.strongest_honest_label.lower()
        assert "Theory of Everything" not in result.strongest_honest_label or \
               "Not" in result.strongest_honest_label


# ── Track C: World-Model Scope ──

class TestWorldModelScope:
    def test_sector_count(self, result):
        assert len(result.scope_sectors) == N_SCOPE_SECTORS
    def test_all_covered(self, result):
        assert result.n_covered == N_SCOPE_SECTORS
    def test_none_absent(self, result):
        assert result.n_scope_absent == 0
    def test_verdicts_valid(self, result):
        for s in result.scope_sectors:
            assert s.scope_verdict in SCOPE_VERDICTS
    def test_substrate(self, result):
        sub = [s for s in result.scope_sectors if s.sector_name == "substrate_ontology"][0]
        assert sub.scope_verdict == "covered_in_bounded_form"
    def test_measurement(self, result):
        meas = [s for s in result.scope_sectors if s.sector_name == "measurement_probability"][0]
        assert meas.scope_verdict == "covered_in_bounded_form"
    def test_all_have_ceilings(self, result):
        for s in result.scope_sectors:
            assert len(s.ceiling) > 0


# ── Track D: Missing-Sector Severity ──

class TestMissingSectors:
    def test_count(self, result):
        assert len(result.missing_sectors) == N_MISSING_SECTORS
    def test_severity_valid(self, result):
        for m in result.missing_sectors:
            assert m.severity in MISSING_SEVERITY
    def test_fatal_toe_count(self, result):
        assert result.n_fatal_toe >= 8
    def test_all_compatible_with_bounded(self, result):
        assert result.n_compatible == N_MISSING_SECTORS
    def test_gauge_fatal(self, result):
        g = [m for m in result.missing_sectors if m.sector_name == "gauge_structure"][0]
        assert g.severity == "fatal_to_full_toe"
    def test_fermion_fatal(self, result):
        f = [m for m in result.missing_sectors if m.sector_name == "fermionic_structure"][0]
        assert f.severity == "fatal_to_full_toe"
    def test_chemistry_cascade(self, result):
        c = [m for m in result.missing_sectors if m.sector_name == "chemistry_composite"][0]
        assert c.severity == "blocked_cascade"


# ── Track E: Capstone Language ──

class TestLanguageLevels:
    def test_count(self, result):
        assert len(result.language_levels) == N_LANGUAGE_LEVELS
    def test_safe_count(self, result):
        n_safe = sum(1 for l in result.language_levels if l.safe)
        assert n_safe == 4
    def test_unsafe_count(self, result):
        n_unsafe = sum(1 for l in result.language_levels if not l.safe)
        assert n_unsafe == 1
    def test_toe_unsafe(self, result):
        toe = [l for l in result.language_levels if "everything" in l.label.lower()][0]
        assert not toe.safe
    def test_bounded_safe(self, result):
        bnd = [l for l in result.language_levels if "world_model" in l.label][0]
        assert bnd.safe


# ── Track F: Finalization ──

class TestFinalization:
    def test_zd_needed(self, result):
        assert result.finalization.zd_needed is True
    def test_ze_not_needed(self, result):
        assert result.finalization.ze_needed is False
    def test_scope_nonempty(self, result):
        assert len(result.finalization.zd_scope) > 0


# ── Hard-Gated Verdicts ──

class TestHardGatedVerdicts:
    def test_canon_map(self, result):
        assert result.canon_map_status == ZC_CANON_MAP
        assert result.canon_map_status in CANON_MAP_OPTIONS
    def test_toe(self, result):
        assert result.toe_status == ZC_TOE
        assert result.toe_status in TOE_STATUS_OPTIONS
    def test_world_model(self, result):
        assert result.world_model_status == ZC_WORLD_MODEL
        assert result.world_model_status in WORLD_MODEL_OPTIONS
    def test_missing(self, result):
        assert result.missing_sector_status == ZC_MISSING
        assert result.missing_sector_status in MISSING_SECTOR_OPTIONS
    def test_auth(self, result):
        assert result.authorization == ZC_AUTH
        assert result.authorization in AUTH_OPTIONS
    def test_overall(self, result):
        assert result.overall_appendix_p == ZC_OVERALL
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_distinct(self, result):
        v = {result.canon_map_status, result.toe_status,
             result.world_model_status, result.missing_sector_status,
             result.authorization}
        assert len(v) == 5


# ── Diagnostics ──

class TestDiagnostics:
    def test_canon_total(self, result):
        assert result.diagnostics["n_canon_entries"] >= N_CANON_ENTRIES
    def test_toe_supported(self, result):
        assert result.diagnostics["n_toe_supported"] == 1
    def test_toe_rejected(self, result):
        assert result.diagnostics["n_toe_rejected"] == 3
    def test_scope_covered(self, result):
        assert result.diagnostics["n_scope_covered"] == N_SCOPE_SECTORS
    def test_missing(self, result):
        assert result.diagnostics["n_missing_sectors"] == N_MISSING_SECTORS
    def test_qm(self, result):
        assert result.diagnostics["full_qm"] is False
    def test_toe_achieved(self, result):
        assert result.diagnostics["toe_achieved"] is False
    def test_closure(self, result):
        assert result.diagnostics["unified_closure"] is False
    def test_postulates(self, result):
        assert result.diagnostics["grand_total_postulates"] == 7
    def test_fields(self, result):
        assert result.diagnostics["grand_total_new_fields"] == 0
    def test_params(self, result):
        assert result.diagnostics["grand_total_parameters"] == 3
    def test_zd(self, result):
        assert result.diagnostics["zd_needed"] is True
    def test_ze(self, result):
        assert result.diagnostics["ze_needed"] is False
    def test_language_safe(self, result):
        assert result.diagnostics["n_language_safe"] == 4
    def test_language_unsafe(self, result):
        assert result.diagnostics["n_language_unsafe"] == 1


# ── Nonclaims ──

class TestNonclaims:
    def test_count(self): assert len(ZC_NONCLAIMS) == N_ZC_NONCLAIMS
    def test_prefix(self):
        for nc in ZC_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_firewall(self, result):
        assert result.nonclaim_firewall.n_nonclaims == N_ZC_NONCLAIMS
        assert result.nonclaim_firewall.all_registered is True


# ── Claims ──

class TestClaims:
    def test_allowed(self, result): assert len(result.allowed_claims) == N_ALLOWED
    def test_forbidden(self, result): assert len(result.forbidden_claims) == N_FORBIDDEN


# ── Master ──

class TestMaster:
    def test_valid(self, result): assert result.valid is True
    def test_key(self, result): assert len(result.key_findings) >= 6
    def test_nonclaims_list(self, result):
        assert len(result.exact_nonclaims) == N_ZC_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
    def test_idempotent(self):
        r1 = run_zc_total_canon_map_toe_boundary()
        r2 = run_zc_total_canon_map_toe_boundary()
        assert r1.valid == r2.valid
        assert r1.canon_map_status == r2.canon_map_status
        assert r1.toe_status == r2.toe_status
