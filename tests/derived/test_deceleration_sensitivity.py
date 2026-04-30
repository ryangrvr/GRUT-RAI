"""Tests for grut.derived.cluster.deceleration_sensitivity — the
(τ_0, dec_ratio) degeneracy analysis.

Disambiguates: is the +20% cluster-merger systematic a τ_0 effect, a
velocity-convention effect, or a degenerate combination? Result: the
two effects are degenerate from offset data alone — both
parameter directions close the systematic with comparable χ²
improvements (~11×), and dec_ratio × τ_0 ≈ 31.5 along the chi-min
ridge (vs canonical 26.7).

Closure path: independent v_post-collision measurements per cluster
(currently only Bullet has this from Springel & Farrar 2007).
"""

import pytest

from grut.derived.cluster.deceleration_sensitivity import (
    CANONICAL_DEC_RATIO,
    DEFAULT_DEC_RATIO_GRID,
    DEFAULT_DEC_RATIO_GRID_2D,
    DEFAULT_TAU_0_GRID_MYR_2D,
    NORMAL_REGIME_CLUSTERS,
    DecRatioSweepPoint,
    DegeneracyReport,
    TwoDSweepPoint,
    best_fit_2d,
    best_fit_dec_ratio,
    dec_ratio_sweep,
    degeneracy_analysis,
    evaluate_2d,
    evaluate_dec_ratio,
    predicted_offset_kpc,
    ratio_at,
    two_d_sweep,
    verify,
)
from grut.derived.cluster.merger_population import BULLET, MACS_J0025, ABELL_520


class TestCanonicalState:
    def test_canonical_dec_ratio_is_bullet_extrapolated(self):
        """The canonical 0.638 comes from Bullet's measured 3000/4700."""
        assert abs(CANONICAL_DEC_RATIO - 3000.0 / 4700.0) < 1e-6

    def test_canonical_chi_squared_matches_documented(self):
        """At canonical (τ_0=41.9, dec_ratio=0.638), χ² ≈ 0.077."""
        p = evaluate_dec_ratio(CANONICAL_DEC_RATIO, 41.9)
        assert 0.05 < p.chi_squared < 0.10

    def test_canonical_state_shows_systematic(self):
        p = evaluate_dec_ratio(CANONICAL_DEC_RATIO, 41.9)
        # All three ratios at canonical should be < 1 (the 0.79-0.88 pattern)
        for r in p.ratios.values():
            assert r < 1.0


class TestDecRatioSweep:
    def test_grid_covers_reasonable_range(self):
        assert min(DEFAULT_DEC_RATIO_GRID) < 0.50
        assert max(DEFAULT_DEC_RATIO_GRID) > 0.95

    def test_best_fit_dec_ratio_around_0p76(self):
        best = best_fit_dec_ratio()
        assert 0.70 < best.dec_ratio < 0.82

    def test_best_fit_dec_ratio_substantial_improvement(self):
        canon = evaluate_dec_ratio(CANONICAL_DEC_RATIO, 41.9)
        best = best_fit_dec_ratio()
        assert canon.chi_squared / best.chi_squared > 5.0

    def test_dec_ratio_sweep_has_clear_minimum(self):
        sweep = dec_ratio_sweep()
        chis = [p.chi_squared for p in sweep]
        # Minimum is interior, not at the endpoints
        min_idx = chis.index(min(chis))
        assert 0 < min_idx < len(chis) - 1


class TestDegeneracyReport:
    def test_dec_ratio_only_improvement_around_12x(self):
        rep = degeneracy_analysis()
        improvement = rep.canonical_chi_squared / rep.best_fit_dec_ratio_only_chi
        assert 8.0 < improvement < 20.0

    def test_tau_0_only_improvement_around_11x(self):
        rep = degeneracy_analysis()
        improvement = rep.canonical_chi_squared / rep.best_fit_tau_0_only_chi
        assert 8.0 < improvement < 20.0

    def test_both_best_fit_chis_comparable(self):
        """The two routes give χ² within a factor of 2 — degenerate."""
        rep = degeneracy_analysis()
        ratio = (
            max(rep.best_fit_dec_ratio_only_chi, rep.best_fit_tau_0_only_chi)
            / min(rep.best_fit_dec_ratio_only_chi, rep.best_fit_tau_0_only_chi)
        )
        assert ratio < 2.0

    def test_products_match_within_5_pct(self):
        """The (dec_ratio × τ_0) products at the two best-fits agree
        within 5% — confirms degeneracy."""
        rep = degeneracy_analysis()
        assert rep.products_within_5_pct

    def test_canonical_product_is_26p7(self):
        rep = degeneracy_analysis()
        # 0.638 × 41.9 ≈ 26.74
        assert 26.0 < rep.canonical_product < 27.5

    def test_best_fit_products_around_31p5(self):
        """Both best-fit products land at ~31.5 (vs canonical 26.7) —
        the +20% systematic shifts the product by ~20%."""
        rep = degeneracy_analysis()
        assert 30.5 < rep.best_fit_product_dec_only < 33.0
        assert 30.5 < rep.best_fit_product_tau_only < 33.0


class TestTwoDSweep:
    def test_2d_sweep_runs(self):
        sweep = two_d_sweep()
        assert len(sweep) > 0

    def test_2d_best_fit_on_degeneracy_ridge(self):
        """The 2D minimum's product should land near the 1D best-fit products."""
        bf2d = best_fit_2d()
        # Product around 31-32
        assert 30.0 < bf2d.product < 33.0

    def test_2d_best_fit_chi_below_one_d_canonical(self):
        bf2d = best_fit_2d()
        canon = evaluate_dec_ratio(CANONICAL_DEC_RATIO, 41.9)
        assert bf2d.chi_squared < canon.chi_squared

    def test_2d_best_fit_chi_at_least_as_good_as_1d(self):
        """The 2D best-fit must do at least as well as either 1D best-fit."""
        bf2d = best_fit_2d()
        rep = degeneracy_analysis()
        assert bf2d.chi_squared <= rep.best_fit_dec_ratio_only_chi + 1e-6


class TestPerClusterPredictions:
    def test_bullet_at_dec_0p76_close_to_observed(self):
        pred = predicted_offset_kpc(BULLET, 0.76, 41.9)
        # Observed 150 kpc; should be ~155
        assert abs(pred - 150.0) < 30.0

    def test_macs_at_dec_0p76_close_to_observed(self):
        pred = predicted_offset_kpc(MACS_J0025, 0.76, 41.9)
        # Observed 75 kpc
        assert abs(pred - 75.0) < 15.0

    def test_predictions_scale_linearly_with_dec_ratio(self):
        """At fixed τ_0, prediction is linear in dec_ratio (since v_final
        is linear and offset ≈ v_final × τ_0 in kernel-dominated regime)."""
        a = predicted_offset_kpc(BULLET, 0.50, 41.9)
        b = predicted_offset_kpc(BULLET, 0.75, 41.9)
        # b/a should be 1.5 (since 0.75/0.50 = 1.5)
        ratio = b / a
        assert abs(ratio - 1.5) < 0.05


class TestVerifyHarness:
    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Deceleration-sensitivity verify failures: {failed}"

    def test_returns_six_legs(self):
        assert len(verify()) == 6


class TestDegeneracyInterpretation:
    """Pin the diagnostic answer: the +20% is degenerate between
    τ_0 and dec_ratio."""

    def test_two_routes_close_systematic_equivalently(self):
        """Both varying τ_0 alone AND varying dec_ratio alone produce
        comparable χ² improvements — neither route is dominant."""
        rep = degeneracy_analysis()
        # Both should improve χ² by at least 5×
        dec_improvement = rep.canonical_chi_squared / rep.best_fit_dec_ratio_only_chi
        tau_improvement = rep.canonical_chi_squared / rep.best_fit_tau_0_only_chi
        assert dec_improvement > 5.0
        assert tau_improvement > 5.0
        # And they agree to within a factor of 2
        assert max(dec_improvement, tau_improvement) / min(
            dec_improvement, tau_improvement
        ) < 2.0

    def test_offset_data_alone_cannot_disambiguate(self):
        """Two distinct (τ_0, dec_ratio) points give nearly identical χ² —
        offset data alone does not pin the answer."""
        # Point A: τ_0 = 41.9, dec_ratio = 0.76 (dec-only best fit)
        a = evaluate_dec_ratio(0.76, 41.9)
        # Point B: τ_0 = 49.0, dec_ratio = 0.638 (τ_0-only best fit)
        b = evaluate_dec_ratio(0.638, 49.0)
        # Both χ² should be small and similar
        assert a.chi_squared < 0.02
        assert b.chi_squared < 0.02
        # Within factor 2 of each other
        assert max(a.chi_squared, b.chi_squared) / min(
            a.chi_squared, b.chi_squared
        ) < 2.0
