"""Tests for grut.toe.coherence — V7/V8/ToE drift detector."""

import re
import textwrap
from pathlib import Path

import pytest

from grut.toe.coherence import (
    CANONICAL_VALUES,
    CanonicalValue,
    DriftReport,
    Hit,
    coherence_report,
    default_scan_paths,
    scan_document,
    verify,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestCanonicalValuesRegistryStructure:
    """The CANONICAL_VALUES list itself is well-formed."""

    def test_non_empty(self):
        assert len(CANONICAL_VALUES) > 0

    def test_unique_names(self):
        names = [cv.name for cv in CANONICAL_VALUES]
        assert len(names) == len(set(names))

    def test_each_has_at_least_one_pattern(self):
        for cv in CANONICAL_VALUES:
            assert cv.patterns, f"{cv.name} has no patterns"

    def test_each_pattern_is_valid_regex(self):
        for cv in CANONICAL_VALUES:
            for pat in cv.patterns:
                try:
                    re.compile(pat)
                except re.error as exc:
                    pytest.fail(
                        f"{cv.name} has invalid regex {pat!r}: {exc}"
                    )

    def test_canonicals_are_finite(self):
        import math
        for cv in CANONICAL_VALUES:
            assert math.isfinite(cv.canonical)

    def test_historical_records_have_supersedes(self):
        for cv in CANONICAL_VALUES:
            if cv.is_historical:
                assert cv.supersedes is not None, (
                    f"{cv.name} is historical but has no supersedes"
                )

    def test_supersedes_points_to_real_canonical(self):
        names = {cv.name for cv in CANONICAL_VALUES}
        for cv in CANONICAL_VALUES:
            if cv.supersedes:
                assert cv.supersedes in names, (
                    f"{cv.name}.supersedes={cv.supersedes!r} not in registry"
                )


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Coherence registry failed checks: {failed}"


class TestScanDocumentMissingFile:
    """Missing files are tolerated — return empty hits, don't raise."""

    def test_missing_file_returns_empty(self, tmp_path):
        result = scan_document(tmp_path / "nonexistent.md")
        assert result == []

    def test_missing_file_does_not_raise(self, tmp_path):
        scan_document(tmp_path / "really_nonexistent.md")  # no exception


class TestScanDocumentBasicHits:
    """Synthetic documents produce expected hits."""

    def _write_doc(self, tmp_path, name, content):
        p = tmp_path / name
        p.write_text(textwrap.dedent(content), encoding="utf-8")
        return p

    def test_alpha_vac_match_one_third(self, tmp_path):
        p = self._write_doc(tmp_path, "doc.md", """
            The vacuum impedance is α_vac = 1/3 from KS 2011.
        """)
        hits = scan_document(p)
        names = {h.value_name for h in hits}
        assert "alpha_vac" in names

    def test_tau_0_match(self, tmp_path):
        p = self._write_doc(tmp_path, "doc.md", """
            The relaxation time τ_0 = 41.9 Myr is benchmark-anchored.
        """)
        hits = scan_document(p)
        names = {h.value_name for h in hits}
        assert "tau_0_Myr" in names

    def test_canonical_R_match(self, tmp_path):
        p = self._write_doc(tmp_path, "doc.md", """
            The canonical refractive index is R = √(4/3) ≈ 1.15470.
        """)
        hits = scan_document(p)
        names = {h.value_name for h in hits}
        assert "R_canonical" in names

    def test_historical_R_flagged_as_historical(self, tmp_path):
        p = self._write_doc(tmp_path, "doc.md", """
            V7 §26.2.3 reports R = 1.15428 from a 3-loop CTP calculation.
        """)
        hits = scan_document(p)
        historical_hits = [h for h in hits if h.is_historical]
        assert len(historical_hits) >= 1
        assert any(h.value_name == "R_anomaly_historical" for h in historical_hits)

    def test_no_match_returns_empty_for_unrelated_text(self, tmp_path):
        p = self._write_doc(tmp_path, "doc.md", """
            This document contains no canonical numerical claims.
            We discuss the philosophy of physics in general terms.
        """)
        hits = scan_document(p)
        # Some loose patterns may catch incidental matches; what we
        # really want is that no historical-flagged hit appears.
        assert not any(h.is_historical for h in hits)


class TestCoherenceReportStructure:
    """coherence_report assembles hits into a structured DriftReport."""

    def test_report_handles_only_missing_files(self, tmp_path):
        report = coherence_report([
            tmp_path / "missing_a.md",
            tmp_path / "missing_b.md",
        ])
        assert report.documents_scanned == ()
        assert len(report.documents_missing) == 2
        assert report.total_hits == 0

    def test_report_counts_per_value_per_document(self, tmp_path):
        a = tmp_path / "a.md"
        a.write_text("τ_0 = 41.9 Myr appears here.\nAnd 41.9 again.\n")
        b = tmp_path / "b.md"
        b.write_text("In document B we say τ_0 = 41.9 Myr once.\n")
        report = coherence_report([a, b])
        # tau_0_Myr should appear in both documents
        assert "tau_0_Myr" in report.per_value_counts
        per_doc = report.per_value_counts["tau_0_Myr"]
        assert per_doc.get("a.md", 0) >= 1
        assert per_doc.get("b.md", 0) >= 1

    def test_historical_uses_collected(self, tmp_path):
        d = tmp_path / "d.md"
        d.write_text("Historical R = 1.15428 from V7.\n")
        report = coherence_report([d])
        assert len(report.historical_uses) >= 1
        assert all(h.is_historical for h in report.historical_uses)

    def test_report_total_hits_equals_sum_of_hits(self, tmp_path):
        d = tmp_path / "d.md"
        d.write_text(
            "α_vac = 1/3.\nτ_0 = 41.9 Myr.\nR = √(4/3) ≈ 1.15470.\n"
        )
        report = coherence_report([d])
        # Each line should produce at least one hit; total must match
        # what scan_document produces directly
        assert report.total_hits == len(scan_document(d))


class TestDefaultScanPaths:
    def test_paths_include_v7_v8_toe(self):
        paths = default_scan_paths(REPO_ROOT)
        names = {p.name for p in paths}
        assert "GRUT_V7_FULL.md" in names
        assert "GRUT_V8.md" in names
        assert "GRUT_V8_CLEAN.md" in names
        assert "GRUT_TOE.md" in names

    def test_real_repo_scan_runs_without_error(self):
        """End-to-end: scan the actual repo, no exception."""
        paths = default_scan_paths(REPO_ROOT)
        report = coherence_report(paths)
        # At least V7 and V8 are present — should produce some hits
        assert report.total_hits >= 0
        assert isinstance(report.documents_scanned, tuple)


class TestHistoricalDriftDetectionInRealDocs:
    """The whole point: 1.15428 should be flagged as historical wherever
    it appears in V7 prose (which was written before Path G was canonical)."""

    def test_historical_R_present_in_v7(self):
        """V7 contains many 1.15428 references — checker must surface them."""
        paths = default_scan_paths(REPO_ROOT)
        report = coherence_report(paths)
        if "GRUT_V7_FULL.md" not in report.documents_scanned:
            pytest.skip("GRUT_V7_FULL.md not present in this checkout")
        v7_historical = [
            h for h in report.historical_uses
            if h.document == "GRUT_V7_FULL.md"
        ]
        # V7 was written when 1.15428 was canonical — many hits expected
        assert len(v7_historical) > 0


class TestTierMarkerValidator:
    """The marker validator catches drift between prose tier-markers
    and registry-claim tiers."""

    def test_scan_markers_returns_empty_for_missing_file(self, tmp_path):
        from grut.toe.coherence import scan_markers
        result = scan_markers(tmp_path / "nonexistent.md")
        assert result == []

    def test_scan_markers_finds_open_marker(self, tmp_path):
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        p.write_text("Some prose here.\nResult [OPEN] needs work.\n")
        hits = scan_markers(p)
        assert len(hits) == 1
        assert hits[0].marker == "OPEN"

    def test_scan_markers_finds_speculative_marker(self, tmp_path):
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        p.write_text("**[SPECULATIVE]** This is uncertain.\n")
        hits = scan_markers(p)
        assert len(hits) == 1
        assert hits[0].marker == "SPECULATIVE"

    def test_scan_markers_finds_outstanding_verification(self, tmp_path):
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        p.write_text("Outstanding verification: this depends on TJI Phase 1.\n")
        hits = scan_markers(p)
        assert len(hits) == 1
        assert hits[0].marker == "OUTSTANDING"

    def test_orphan_marker_when_no_claim_id_nearby(self, tmp_path):
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        p.write_text("This is speculative content [SPECULATIVE].\n")
        hits = scan_markers(p)
        assert len(hits) == 1
        assert hits[0].is_orphan
        assert len(hits[0].matched_registry_claims) == 0

    def test_marker_associated_with_real_claim_id_nearby(self, tmp_path):
        """If a known claim ID is in backticks near the marker, it's
        associated, not orphan."""
        from grut.toe.coherence import scan_markers
        # Use a real registered claim ID
        p = tmp_path / "doc.md"
        p.write_text(
            "The TJI Phase-1 calculation is documented in `tji_7_4_open_negative`\n"
            "and remains [OPEN] pending specialist verification.\n"
        )
        hits = scan_markers(p)
        assert len(hits) == 1
        assert not hits[0].is_orphan
        assert "tji_7_4_open_negative" in hits[0].matched_registry_claims

    def test_tier_mismatch_when_marker_disagrees_with_claim_tier(self, tmp_path):
        """An [OPEN] marker near a 'computed' claim flags as mismatch."""
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        # gr_recovery is tier=computed; pairing with [OPEN] should mismatch.
        # (Was alpha_vac_derivation, which the v3 re-audit demoted to
        # open_negative — so it no longer mismatches an [OPEN] marker.)
        p.write_text(
            "The GR limit `gr_recovery` is supposedly [OPEN].\n"
        )
        hits = scan_markers(p)
        assert len(hits) == 1
        assert hits[0].tier_mismatch
        assert "gr_recovery" in hits[0].matched_registry_claims

    def test_no_tier_mismatch_when_marker_agrees(self, tmp_path):
        """A [SPECULATIVE] marker near a 'conjectural' claim is consistent."""
        from grut.toe.coherence import scan_markers
        p = tmp_path / "doc.md"
        # one_space_endpoint is tier=conjectural; SPECULATIVE matches
        p.write_text(
            "The `one_space_endpoint` framing is [SPECULATIVE].\n"
        )
        hits = scan_markers(p)
        assert len(hits) == 1
        assert not hits[0].tier_mismatch


class TestMarkerAuditReport:
    """Aggregated marker audit across documents."""

    def test_handles_only_missing_files(self, tmp_path):
        from grut.toe.coherence import marker_audit_report
        rep = marker_audit_report([tmp_path / "missing.md"])
        assert rep.total_markers == 0
        assert len(rep.documents_missing) == 1

    def test_aggregates_marker_counts(self, tmp_path):
        from grut.toe.coherence import marker_audit_report
        a = tmp_path / "a.md"
        a.write_text("[OPEN] one.\n[SPECULATIVE] two.\n")
        b = tmp_path / "b.md"
        b.write_text("Outstanding verification needed.\n")
        rep = marker_audit_report([a, b])
        assert rep.total_markers == 3
        assert rep.by_marker_type["OPEN"] == 1
        assert rep.by_marker_type["SPECULATIVE"] == 1
        assert rep.by_marker_type["OUTSTANDING"] == 1

    def test_separates_orphans_from_associated(self, tmp_path):
        from grut.toe.coherence import marker_audit_report
        p = tmp_path / "doc.md"
        # First marker has no nearby claim → orphan
        # Second marker has a real registry claim ID nearby → associated
        p.write_text(
            "Loose speculation [SPECULATIVE].\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "\n"
            "The `tji_7_4_open_negative` is [OPEN] and well-documented.\n"
        )
        rep = marker_audit_report([p])
        assert rep.total_markers == 2
        assert len(rep.orphan_markers) == 1
        assert rep.orphan_markers[0].marker == "SPECULATIVE"

    def test_real_repo_scan_completes_without_error(self):
        """End-to-end: scan the real document set, no exception."""
        from grut.toe.coherence import default_scan_paths, marker_audit_report
        paths = default_scan_paths(REPO_ROOT)
        rep = marker_audit_report(paths)
        # Real docs have substantive marker counts
        assert rep.total_markers >= 0
        assert isinstance(rep.documents_scanned, tuple)


class TestPatternMatchingPrecision:
    """Patterns shouldn't match unrelated numbers."""

    def test_tau_0_does_not_match_419(self, tmp_path):
        """The pattern \\b41.9\\b shouldn't match '419' or '41.95'."""
        p = tmp_path / "doc.md"
        p.write_text("This document mentions 419 lines and value 41.95.\n")
        hits = scan_document(p)
        # We only need: no hit on tau_0_Myr from "419" (the integer)
        for h in hits:
            if h.value_name == "tau_0_Myr":
                assert h.matched_text == "41.9"
