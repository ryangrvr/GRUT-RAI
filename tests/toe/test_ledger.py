"""Tests for grut.toe.ledger — every open_negative claim in the
registry must have a corresponding ledger entry, and every ledger
entry must point at a registered claim."""

import pytest

from grut.toe.ledger import (
    LedgerEntry,
    OPEN_NEGATIVES,
    affects_summary,
    all_claim_ids_in_ledger,
    by_claim,
    closure_dependency_chain,
    coverage_report,
    open_negatives_in_registry,
)
from grut.toe.registry import REGISTRY, by_id


class TestLedgerStructuralIntegrity:

    def test_ledger_non_empty(self):
        assert len(OPEN_NEGATIVES) > 0

    def test_unique_claim_ids(self):
        ids = [e.claim_id for e in OPEN_NEGATIVES]
        assert len(ids) == len(set(ids))

    def test_each_entry_has_closure_condition(self):
        for e in OPEN_NEGATIVES:
            assert e.closure_condition.strip(), (
                f"{e.claim_id} has empty closure_condition"
            )

    def test_each_entry_has_closure_effort(self):
        for e in OPEN_NEGATIVES:
            assert e.closure_effort.strip(), (
                f"{e.claim_id} has empty closure_effort"
            )


class TestRegistryAlignment:
    """Every open_negative in the registry maps to a ledger entry, and
    every ledger entry maps to a registered open_negative."""

    def test_coverage_is_complete(self):
        rep = coverage_report()
        assert rep["coverage_complete"], (
            f"Coverage gap. In registry not ledger: "
            f"{rep['in_registry_not_ledger']}. "
            f"In ledger not registry: {rep['in_ledger_not_registry']}."
        )

    def test_all_ledger_ids_are_open_negative_claims(self):
        for e in OPEN_NEGATIVES:
            c = by_id(e.claim_id)
            assert c is not None, f"{e.claim_id} not in registry"
            assert c.tier == "open_negative", (
                f"{e.claim_id} is not tier='open_negative' "
                f"(tier={c.tier!r})"
            )

    def test_no_open_negative_claim_unrepresented(self):
        in_ledger = all_claim_ids_in_ledger()
        in_registry = open_negatives_in_registry()
        missing = in_registry - in_ledger
        assert not missing, f"Open negatives missing ledger entries: {missing}"


class TestAffectsConsistency:
    """`affects` ids must point to real registry claims."""

    def test_affects_resolve(self):
        registered = {c.id for c in REGISTRY}
        for e in OPEN_NEGATIVES:
            for a in e.affects:
                assert a in registered, (
                    f"{e.claim_id}.affects={a!r} is not a registered claim"
                )

    def test_blocked_by_resolve(self):
        in_ledger = all_claim_ids_in_ledger()
        for e in OPEN_NEGATIVES:
            for b in e.blocked_by:
                assert b in in_ledger, (
                    f"{e.claim_id}.blocked_by={b!r} is not a ledger entry"
                )


class TestClosureDependencyChain:

    def test_chain_returns_tuple_for_real_claims(self):
        for e in OPEN_NEGATIVES:
            chain = closure_dependency_chain(e.claim_id)
            assert isinstance(chain, tuple)

    def test_chain_excludes_self(self):
        for e in OPEN_NEGATIVES:
            chain = closure_dependency_chain(e.claim_id)
            assert e.claim_id not in chain

    def test_tji_blocked_by_allen_jacobson(self):
        """tji_7_4_open_negative should list allen_jacobson_phase1_stub
        in its closure dependency chain — both must close together."""
        chain = closure_dependency_chain("tji_7_4_open_negative")
        assert "allen_jacobson_phase1_stub_open_negative" in chain


class TestCoverageReport:

    def test_report_has_expected_keys(self):
        rep = coverage_report()
        for key in (
            "ledger_entries",
            "registry_open_negatives",
            "in_registry_not_ledger",
            "in_ledger_not_registry",
            "coverage_complete",
        ):
            assert key in rep

    def test_report_lists_are_sorted(self):
        rep = coverage_report()
        for key in ("ledger_entries", "registry_open_negatives"):
            assert rep[key] == sorted(rep[key])


class TestAffectsSummary:

    def test_affects_summary_keys_match_ledger(self):
        s = affects_summary()
        assert set(s.keys()) == all_claim_ids_in_ledger()


class TestByClaim:

    def test_by_claim_returns_entry(self):
        e = by_claim("tji_7_4_open_negative")
        assert e is not None
        assert e.claim_id == "tji_7_4_open_negative"

    def test_by_claim_returns_none_for_unknown(self):
        assert by_claim("not_a_real_claim_id") is None
