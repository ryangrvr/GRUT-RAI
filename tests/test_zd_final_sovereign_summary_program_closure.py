"""Tests for Z-D --- Final Sovereign Summary, Program Closure, and Future-Boundary Seal."""
import pytest
from grut.zd_final_sovereign_summary_program_closure import (
    N_IDENTITY_CANDIDATES, N_CANON_CATEGORIES, N_LANGUAGE_ENTRIES,
    N_FUTURE_RULES, N_CLOSURE_ITEMS, N_ZD_NONCLAIMS, N_ALLOWED, N_FORBIDDEN,
    IDENTITY_OPTIONS, CANON_SEAL_OPTIONS, LANGUAGE_OPTIONS,
    FUTURE_BOUNDARY_OPTIONS, AUTH_OPTIONS, OVERALL_OPTIONS,
    ZD_IDENTITY, ZD_CANON_SEAL, ZD_LANGUAGE, ZD_FUTURE, ZD_AUTH, ZD_OVERALL,
    ZD_NONCLAIMS,
    run_zd_final_sovereign_summary_program_closure, _self_test,
)

@pytest.fixture(scope="module")
def result():
    return run_zd_final_sovereign_summary_program_closure()


# ── Constants ──

class TestConstants:
    def test_identity(self): assert N_IDENTITY_CANDIDATES == 5
    def test_canon(self): assert N_CANON_CATEGORIES == 6
    def test_language(self): assert N_LANGUAGE_ENTRIES == 8
    def test_future(self): assert N_FUTURE_RULES == 8
    def test_closure(self): assert N_CLOSURE_ITEMS == 4
    def test_nc(self): assert N_ZD_NONCLAIMS == 8
    def test_allowed(self): assert N_ALLOWED == 7
    def test_forbidden(self): assert N_FORBIDDEN == 7


# ── Track A: Program Identity ──

class TestIdentity:
    def test_count(self, result):
        assert len(result.identity_candidates) == N_IDENTITY_CANDIDATES
    def test_exactly_one_supported(self, result):
        supported = [i for i in result.identity_candidates if i.supported]
        assert len(supported) == 1
    def test_bounded_supported(self, result):
        supported = [i for i in result.identity_candidates if i.supported][0]
        assert supported.label == "bounded_world_model_framework"
    def test_toe_rejected(self, result):
        toe = [i for i in result.identity_candidates
               if i.label == "theory_of_everything"][0]
        assert not toe.supported
    def test_final_identity(self, result):
        assert result.final_identity == "bounded_world_model_framework"


# ── Track B: Canon Seal ──

class TestCanonSeal:
    def test_category_count(self, result):
        assert len(result.canon_categories) == N_CANON_CATEGORIES
    def test_total_entries(self, result):
        assert result.canon_total_entries == 35
    def test_native_count(self, result):
        nat = [c for c in result.canon_categories if c.category == "native_canon"][0]
        assert nat.count == 8
    def test_extension_count(self, result):
        ext = [c for c in result.canon_categories if c.category == "extension_canon"][0]
        assert ext.count == 13
    def test_analogy_count(self, result):
        ana = [c for c in result.canon_categories if c.category == "analogy_only"][0]
        assert ana.count == 3
    def test_constitutive_count(self, result):
        con = [c for c in result.canon_categories
               if c.category == "constitutive_or_effective_only"][0]
        assert con.count == 1
    def test_absent_count(self, result):
        ab = [c for c in result.canon_categories if c.category == "absent_unbuilt"][0]
        assert ab.count == 8
    def test_blocked_count(self, result):
        bl = [c for c in result.canon_categories if c.category == "blocked_by_structure"][0]
        assert bl.count == 2
    def test_total_sum(self, result):
        total = sum(c.count for c in result.canon_categories)
        assert total == 35
    def test_categories_unique(self, result):
        cats = [c.category for c in result.canon_categories]
        assert len(cats) == len(set(cats))


# ── Track C: Language ──

class TestLanguage:
    def test_count(self, result):
        assert len(result.language_entries) == N_LANGUAGE_ENTRIES
    def test_allowed_count(self, result):
        assert result.n_allowed_phrases == 4
    def test_forbidden_count(self, result):
        assert result.n_forbidden_phrases == 4
    def test_toe_forbidden(self, result):
        toe = [l for l in result.language_entries
               if "everything" in l.phrase.lower()]
        assert len(toe) >= 1
        for t in toe:
            assert not t.allowed
    def test_bounded_allowed(self, result):
        bnd = [l for l in result.language_entries
               if "bounded" in l.phrase.lower() and "world" in l.phrase.lower()]
        assert len(bnd) >= 1
        assert bnd[0].allowed
    def test_unified_forbidden(self, result):
        uni = [l for l in result.language_entries
               if "unified" in l.phrase.lower()]
        for u in uni:
            assert not u.allowed
    def test_full_qm_forbidden(self, result):
        fqm = [l for l in result.language_entries
               if "full quantum" in l.phrase.lower()]
        for f in fqm:
            assert not f.allowed


# ── Track D: Future Boundary ──

class TestFutureBoundary:
    def test_count(self, result):
        assert len(result.future_rules) == N_FUTURE_RULES
    def test_ids_sequential(self, result):
        for i, rule in enumerate(result.future_rules):
            assert rule.rule_id == f"FB{i+1}"
    def test_fb1_explicit_postulates(self, result):
        assert "explicit" in result.future_rules[0].statement.lower()
    def test_fb2_no_retroactive(self, result):
        assert "retroactive" in result.future_rules[1].statement.lower()
    def test_fb7_book_ii_immutable(self, result):
        assert "immutable" in result.future_rules[6].statement.lower()
    def test_fb8_baseline(self, result):
        assert "7/3/0/0" in result.future_rules[7].statement


# ── Track E: Closure ──

class TestClosure:
    def test_count(self, result):
        assert len(result.closure_items) == N_CLOSURE_ITEMS
    def test_closed_item(self, result):
        cl = [c for c in result.closure_items if c.domain == "closed"][0]
        assert "sealed" in cl.description.lower() or "closed" in cl.description.lower()
    def test_open_item(self, result):
        op = [c for c in result.closure_items if c.domain == "open"][0]
        assert "absent" in op.description.lower() or "blocked" in op.description.lower()
    def test_excluded_item(self, result):
        ex = [c for c in result.closure_items if c.domain == "permanently_excluded"][0]
        assert "gauge" in ex.description.lower()
    def test_next_gen_item(self, result):
        ng = [c for c in result.closure_items if c.domain == "next_generation"][0]
        assert "NOT" in ng.description or "may NOT" in ng.description.lower() or \
               "May NOT" in ng.description


class TestHandoff:
    def test_may_do(self, result):
        assert len(result.handoff.what_next_gen_may_do) >= 3
    def test_may_not_do(self, result):
        assert len(result.handoff.what_next_gen_may_not_do) >= 3
    def test_no_reopen(self, result):
        may_not = " ".join(result.handoff.what_next_gen_may_not_do).lower()
        assert "reopen" in may_not
    def test_no_toe(self, result):
        may_not = " ".join(result.handoff.what_next_gen_may_not_do).lower()
        assert "theory of everything" in may_not or "toe" in may_not


# ── Hard-Gated Verdicts ──

class TestHardGatedVerdicts:
    def test_identity(self, result):
        assert result.program_identity_status == ZD_IDENTITY
        assert result.program_identity_status in IDENTITY_OPTIONS
    def test_canon_seal(self, result):
        assert result.canon_seal_status == ZD_CANON_SEAL
        assert result.canon_seal_status in CANON_SEAL_OPTIONS
    def test_language(self, result):
        assert result.language_status == ZD_LANGUAGE
        assert result.language_status in LANGUAGE_OPTIONS
    def test_future(self, result):
        assert result.future_boundary_status == ZD_FUTURE
        assert result.future_boundary_status in FUTURE_BOUNDARY_OPTIONS
    def test_auth(self, result):
        assert result.authorization == ZD_AUTH
        assert result.authorization in AUTH_OPTIONS
    def test_overall(self, result):
        assert result.overall_appendix_p == ZD_OVERALL
        assert result.overall_appendix_p in OVERALL_OPTIONS
    def test_distinct(self, result):
        v = {result.program_identity_status, result.canon_seal_status,
             result.language_status, result.future_boundary_status,
             result.authorization}
        assert len(v) == 5


# ── Diagnostics ──

class TestDiagnostics:
    def test_identity_supported(self, result):
        assert result.diagnostics["n_identity_supported"] == 1
    def test_final_identity(self, result):
        assert result.diagnostics["final_identity"] == "bounded_world_model_framework"
    def test_canon_total(self, result):
        assert result.diagnostics["canon_total_entries"] == 35
    def test_native(self, result):
        assert result.diagnostics["n_native"] == 8
    def test_extension(self, result):
        assert result.diagnostics["n_extension"] == 13
    def test_absent(self, result):
        assert result.diagnostics["n_absent"] == 8
    def test_blocked(self, result):
        assert result.diagnostics["n_blocked"] == 2
    def test_postulates(self, result):
        assert result.diagnostics["grand_total_postulates"] == 7
    def test_params(self, result):
        assert result.diagnostics["grand_total_parameters"] == 3
    def test_fields(self, result):
        assert result.diagnostics["grand_total_new_fields"] == 0
    def test_dof(self, result):
        assert result.diagnostics["grand_total_new_dof"] == 0
    def test_qm(self, result):
        assert result.diagnostics["full_qm"] is False
    def test_toe(self, result):
        assert result.diagnostics["toe_achieved"] is False
    def test_closure(self, result):
        assert result.diagnostics["unified_closure"] is False
    def test_program_closed(self, result):
        assert result.diagnostics["program_closed"] is True
    def test_z_sealed(self, result):
        assert result.diagnostics["appendix_z_sealed"] is True


# ── Nonclaims ──

class TestNonclaims:
    def test_count(self): assert len(ZD_NONCLAIMS) == N_ZD_NONCLAIMS
    def test_prefix(self):
        for nc in ZD_NONCLAIMS:
            assert nc.startswith("NOT_claiming_")
    def test_firewall(self, result):
        assert result.nonclaim_firewall.n_nonclaims == N_ZD_NONCLAIMS
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
        assert len(result.exact_nonclaims) == N_ZD_NONCLAIMS
    def test_self_test(self): assert _self_test() is True
    def test_idempotent(self):
        r1 = run_zd_final_sovereign_summary_program_closure()
        r2 = run_zd_final_sovereign_summary_program_closure()
        assert r1.valid == r2.valid
        assert r1.program_identity_status == r2.program_identity_status
        assert r1.authorization == r2.authorization
    def test_authorization_is_closed(self, result):
        assert result.authorization == "appendix_Z_closed_program_sovereign_ledger_complete"
