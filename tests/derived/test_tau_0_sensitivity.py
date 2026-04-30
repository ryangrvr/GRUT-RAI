"""Tests for grut.derived.cluster.tau_0_sensitivity — single-τ_0 best-fit
across the three normal-regime cluster mergers.

The framework's adopted τ_0 = 41.9 Myr produces ratios 0.79-0.88 across
the three mergers. This module finds the best-fit τ_0 that closes the
systematic. The result (≈ 49 Myr, 11× chi² improvement) pins the
diagnostic interpretation: the cluster regime exhibits a τ_0 ~20%
higher than the cosmic-baseline value, consistently across multiple
analyses (cluster_merger_scaling_law, tau_0_cross_consistency,
this sensitivity analysis).
"""

import pytest

from grut.derived.cluster.tau_0_sensitivity import (
    DEFAULT_TAU_0_GRID_MYR,
    NORMAL_REGIME_CLUSTERS,
    TauComparisonReport,
    TauSweepPoint,
    best_fit_tau_0,
    comparison_report,
    evaluate_at_tau_0,
    predicted_offset_at_tau_0,
    ratio_at_tau_0,
    tau_0_sweep,
    verify,
)


class TestSweepGrid:
    def test_grid_covers_30_to_65_Myr(self):
        assert min(DEFAULT_TAU_0_GRID_MYR) <= 30.0
        assert max(DEFAULT_TAU_0_GRID_MYR) >= 65.0

    def test_grid_resolution_under_1_Myr(self):
        spacing = DEFAULT_TAU_0_GRID_MYR[1] - DEFAULT_TAU_0_GRID_MYR[0]
        assert spacing <= 1.0

    def test_three_clusters_in_normal_regime(self):
        assert len(NORMAL_REGIME_CLUSTERS) == 3
        names = {name for name, _ in NORMAL_REGIME_CLUSTERS}
        assert "Bullet Cluster" in names
        assert "MACS J0025" in names
        assert "Abell 520" in names

    def test_el_gordo_excluded(self):
        names = {name for name, _ in NORMAL_REGIME_CLUSTERS}
        assert "El Gordo" not in names


class TestSweepPoint:
    def test_canonical_ratios_match_documented(self):
        """At τ_0 = 41.9 Myr, the three clusters give 0.79-0.88."""
        p = evaluate_at_tau_0(41.9)
        for ratio in p.ratios.values():
            assert 0.75 < ratio < 0.92

    def test_canonical_systematic_visible(self):
        """RMS deviation at canonical should be > 5% (diagnostic)."""
        p = evaluate_at_tau_0(41.9)
        assert p.rms_deviation_from_unity > 0.05

    def test_chi_squared_minimized_around_best_fit(self):
        """Sweep across the grid; best chi² is near the 49 Myr expected value."""
        sweep = tau_0_sweep()
        best = min(sweep, key=lambda p: p.chi_squared)
        assert 45.0 <= best.tau_0_Myr <= 55.0

    def test_chi_squared_higher_at_canonical_than_at_best_fit(self):
        canon = evaluate_at_tau_0(41.9)
        best = best_fit_tau_0()
        assert canon.chi_squared > best.chi_squared


class TestBestFit:
    def test_best_fit_around_49_Myr(self):
        best = best_fit_tau_0()
        assert 47.0 <= best.tau_0_Myr <= 51.0

    def test_best_fit_closes_systematic(self):
        """All three ratios at best-fit within ±10% of unity."""
        best = best_fit_tau_0()
        for ratio in best.ratios.values():
            assert abs(ratio - 1.0) < 0.10

    def test_best_fit_chi_squared_under_0p01(self):
        best = best_fit_tau_0()
        assert best.chi_squared < 0.01


class TestComparisonReport:
    def test_canonical_chi_above_best(self):
        rep = comparison_report()
        assert rep.canonical_point.chi_squared > rep.best_fit_point.chi_squared

    def test_improvement_factor_above_5(self):
        rep = comparison_report()
        assert rep.improvement_factor > 5.0

    def test_improvement_factor_around_11(self):
        """Expected ~11× improvement based on canonical chi² 0.077 / best 0.007."""
        rep = comparison_report()
        assert 8.0 < rep.improvement_factor < 20.0

    def test_systematic_closed_at_best_fit(self):
        rep = comparison_report()
        assert rep.systematic_closed_at_best_fit

    def test_best_fit_agrees_with_cluster_inferred_tau_0(self):
        """Best-fit τ_0 should match the simple δ/v cluster-inferred mean
        within a few Myr — the two analyses point at the same answer."""
        rep = comparison_report()
        assert abs(
            rep.best_fit_point.tau_0_Myr
            - rep.cluster_inferred_tau_0_mean_Myr
        ) < 5.0


class TestPerClusterPredictions:
    def test_bullet_at_canonical_around_130(self):
        from grut.derived.cluster.merger_population import BULLET
        pred = predicted_offset_at_tau_0(BULLET, 41.9)
        assert 125 < pred < 140

    def test_bullet_at_best_fit_close_to_observed(self):
        from grut.derived.cluster.merger_population import BULLET
        pred = predicted_offset_at_tau_0(BULLET, 49.0)
        # Observed 150 kpc; at 49 Myr should be very close
        assert abs(pred - 150.0) < 30.0

    def test_abell_520_largest_systematic_at_canonical(self):
        """Abell 520 has ratio 0.79 — the largest deviation from unity."""
        from grut.derived.cluster.merger_population import ABELL_520
        ratio = ratio_at_tau_0(ABELL_520, 41.9)
        assert ratio < 0.85


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"τ_0 sensitivity verify failures: {failed}"

    def test_returns_six_legs(self):
        assert len(verify()) == 6


class TestDiagnosticInterpretation:
    """The result distinguishes 'observational uncertainty' from 'specific signature'."""

    def test_specific_signature_supported(self):
        """A single best-fit τ_0 ≠ 41.9 closes the systematic — supports
        the 'specific signature' reading from cluster_merger_scaling_law."""
        rep = comparison_report()
        # Distance from canonical should be substantial (> 5 Myr)
        assert abs(
            rep.best_fit_point.tau_0_Myr - rep.canonical_tau_0_Myr
        ) > 5.0

    def test_three_independent_analyses_agree(self):
        """The three analyses (cluster_merger_scaling_law, tau_0_cross_consistency,
        and this sensitivity analysis) all point at cluster τ_0 ≈ 50 Myr."""
        rep = comparison_report()

        # Sensitivity analysis says best-fit ≈ 49 Myr
        assert 47 < rep.best_fit_point.tau_0_Myr < 51

        # Cluster-inferred mean (from tau_0_cross_consistency-style δ/v) ≈ 50 Myr
        assert 47 < rep.cluster_inferred_tau_0_mean_Myr < 53

        # Both analyses agree within 5 Myr
        diff = abs(
            rep.best_fit_point.tau_0_Myr
            - rep.cluster_inferred_tau_0_mean_Myr
        )
        assert diff < 5.0
