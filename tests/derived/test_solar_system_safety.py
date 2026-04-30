"""Tests for grut.derived.solar_system_safety — multi-test
quantitative safety demonstration.

The framework's safety claim is converted from "Saturn orbit is in
deep crystal" to "eight independent GR tests, each below detection
precision by factors of 10⁵-10³⁵."
"""

import math
from pathlib import Path

import pytest

from grut.derived.solar_system_safety import (
    SOLAR_SYSTEM_TESTS,
    SolarSystemTest,
    render_full_report,
    render_table,
    safety_report,
    verify,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestStructure:
    def test_eight_tests_present(self):
        assert len(SOLAR_SYSTEM_TESTS) == 8

    def test_unique_short_ids(self):
        ids = [t.short_id for t in SOLAR_SYSTEM_TESTS]
        assert len(ids) == len(set(ids))

    def test_each_has_citation(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.citation.strip()

    def test_each_has_omega_basis(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.omega_basis.strip()

    def test_each_has_obs_precision_basis(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.obs_precision_basis.strip()

    def test_periods_positive(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.period_seconds > 0

    def test_obs_precisions_positive(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.obs_precision > 0


class TestComputedQuantities:
    def test_omega_correct(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert abs(t.omega_Hz - 2 * math.pi / t.period_seconds) < 1e-12

    def test_omega_tau_above_1_for_all(self):
        """All solar-system frequencies are deep crystal: ωτ_0 ≫ 1."""
        for t in SOLAR_SYSTEM_TESTS:
            assert t.omega_tau_0 > 1.0

    def test_alpha_eff_below_1e_minus_10(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.alpha_eff < 1e-10

    def test_alpha_eff_decreases_with_frequency(self):
        """Higher ω → smaller α_eff. Sort tests by frequency."""
        sorted_tests = sorted(SOLAR_SYSTEM_TESTS, key=lambda t: t.omega_Hz)
        prev_alpha = float("inf")
        for t in sorted_tests:
            assert t.alpha_eff <= prev_alpha
            prev_alpha = t.alpha_eff


class TestSafetyFactors:
    def test_all_safety_factors_above_1(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.safety_factor > 1.0, (
                f"{t.name} safety factor = {t.safety_factor:.2e}"
            )

    def test_all_safety_factors_above_1e4(self):
        for t in SOLAR_SYSTEM_TESTS:
            assert t.safety_factor > 1e4

    def test_saturn_safety_around_1e5(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS01")
        assert 1e4 < s.safety_factor < 1e7

    def test_ligo_safety_around_1e35(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS07")
        assert 1e30 < s.safety_factor < 1e40


class TestSpecificTests:
    def test_saturn_period_30yr(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS01")
        assert "30 yr" in s.period_human or "30 year" in s.period_human

    def test_mercury_period_88d(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS02")
        assert "88" in s.period_human

    def test_lunar_laser_cites_williams(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS03")
        assert "Williams" in s.citation

    def test_cassini_shapiro_cites_bertotti(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS06")
        assert "Bertotti" in s.citation

    def test_ligo_cites_abbott(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS07")
        assert "Abbott" in s.citation

    def test_hulse_taylor_cites_weisberg(self):
        s = next(t for t in SOLAR_SYSTEM_TESTS if t.short_id == "SS05")
        assert "Weisberg" in s.citation


class TestSafetyReport:
    def test_all_safe(self):
        rep = safety_report()
        assert rep.n_safe == rep.n_tests

    def test_all_substantial_margin(self):
        rep = safety_report()
        assert rep.n_safe_with_margin == rep.n_tests

    def test_min_safety_above_1e4(self):
        rep = safety_report()
        assert rep.min_safety_factor > 1e4

    def test_max_safety_at_LIGO(self):
        rep = safety_report()
        # LIGO at 100 Hz gives the largest ωτ_0 → smallest α_eff → largest safety
        assert rep.max_safety_factor > 1e30


class TestRendering:
    def test_table_renders(self):
        out = render_table()
        for t in SOLAR_SYSTEM_TESTS:
            assert t.short_id in out

    def test_table_includes_headers(self):
        out = render_table()
        assert "ωτ_0" in out
        assert "α_eff" in out
        assert "Safety factor" in out

    def test_full_report_includes_aggregate(self):
        out = render_full_report()
        assert "Aggregate" in out
        assert "Per-test breakdown" in out
        assert "Detailed entries" in out

    def test_full_report_includes_all_tests(self):
        out = render_full_report()
        for t in SOLAR_SYSTEM_TESTS:
            assert t.short_id in out
            assert t.name in out


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Solar-system safety verify failures: {failed}"

    def test_returns_six_legs(self):
        assert len(verify()) == 6


class TestDocumentExists:
    def test_solar_system_doc_present(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_SOLAR_SYSTEM_SAFETY.md"
        assert doc.is_file()

    def test_doc_has_substantive_content(self):
        doc = REPO_ROOT / "theory" / "GRUT_TOE_SOLAR_SYSTEM_SAFETY.md"
        text = doc.read_text(encoding="utf-8")
        assert len(text.splitlines()) > 50
        for t in SOLAR_SYSTEM_TESTS:
            assert t.short_id in text


class TestFrequencySpan:
    """The eight tests span a wide frequency range — demonstrates safety
    isn't a coincidence at one frequency."""

    def test_min_period_is_LIGO(self):
        sorted_tests = sorted(SOLAR_SYSTEM_TESTS, key=lambda t: t.period_seconds)
        assert sorted_tests[0].short_id == "SS07"  # LIGO

    def test_max_period_is_Saturn_or_Earth(self):
        sorted_tests = sorted(SOLAR_SYSTEM_TESTS, key=lambda t: t.period_seconds)
        assert sorted_tests[-1].short_id in {"SS01", "SS08"}

    def test_periods_span_more_than_10_orders(self):
        periods = [t.period_seconds for t in SOLAR_SYSTEM_TESTS]
        # LIGO ~10 ms vs Saturn ~30 yr ~ 9e8 s → span ~10¹¹
        assert max(periods) / min(periods) > 1e10
