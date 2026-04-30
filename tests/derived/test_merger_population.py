"""Tests for grut.derived.cluster.merger_population — the v × τ_0
cluster-merger scaling law applied to four independent systems:
Bullet Cluster, MACS J0025, Abell 520, El Gordo.

The honest result the framework is committing to:
    - 3 of 4 systems lie within factor 1.3 of observation
    - El Gordo is an explicit outlier (factor ~3.5 under-predicted)
    - Internal v × τ_0 scaling holds at the 1.7% level across the sample

These tests pin both the agreement (for 3 systems) and the outlier
status (for El Gordo) — the framework is responsible for both.
"""

import math

import pytest

from grut.derived.cluster.bullet_cluster import BulletClusterObs
from grut.derived.cluster.merger_population import (
    ABELL_520,
    BULLET,
    CLUSTER_MERGERS,
    EL_GORDO,
    MACS_J0025,
    MergerPrediction,
    PopulationSummary,
    population_summary,
    predict_merger,
    predict_population,
    scaling_law_residual,
    verify,
)


class TestPopulationStructure:
    """The cluster sample is well-formed."""

    def test_four_systems_in_population(self):
        assert len(CLUSTER_MERGERS) == 4

    def test_each_entry_is_named(self):
        for name, obs in CLUSTER_MERGERS:
            assert isinstance(name, str) and name
            assert isinstance(obs, BulletClusterObs)

    def test_velocities_in_published_band(self):
        """All systems have v_initial in the 2000-5000 km/s band."""
        for _, obs in CLUSTER_MERGERS:
            assert 2000 <= obs.v_initial_km_s <= 5000

    def test_observed_offsets_positive(self):
        for _, obs in CLUSTER_MERGERS:
            assert obs.gas_lensing_offset_kpc > 0


class TestPerSystemPredictions:
    """Each merger's prediction is in the documented band."""

    def test_bullet_cluster_within_factor_1p5(self):
        p = predict_merger(BULLET, name="Bullet Cluster")
        assert 0.6 < p.ratio_pred_over_obs < 1.5

    def test_bullet_kernel_around_130_kpc(self):
        p = predict_merger(BULLET, name="Bullet Cluster")
        assert 100 < p.grut_kernel_kpc < 160

    def test_macs_j0025_within_factor_1p5(self):
        p = predict_merger(MACS_J0025, name="MACS J0025")
        assert 0.6 < p.ratio_pred_over_obs < 1.5

    def test_macs_kernel_around_65_kpc(self):
        p = predict_merger(MACS_J0025, name="MACS J0025")
        # 1500 km/s × 41.9 Myr ≈ 65 kpc
        assert 50 < p.grut_kernel_kpc < 80

    def test_abell_520_within_factor_1p5(self):
        p = predict_merger(ABELL_520, name="Abell 520")
        assert 0.6 < p.ratio_pred_over_obs < 1.5

    def test_el_gordo_is_explicit_outlier(self):
        """El Gordo's GRUT prediction is < factor 0.5 of observation —
        framework under-predicts by factor 3-4 for this extreme system."""
        p = predict_merger(EL_GORDO, name="El Gordo")
        assert p.ratio_pred_over_obs < 0.5
        assert not p.in_factor_2_band


class TestScalingLawInternal:
    """offset / v_final is constant across the sample to ~5%."""

    def test_residual_under_5_pct(self):
        preds = predict_population()
        residual = scaling_law_residual(preds)
        assert residual < 0.05

    def test_residual_under_3_pct(self):
        """Tighter: GRUT internally produces v × τ_0 to within 3%."""
        preds = predict_population()
        residual = scaling_law_residual(preds)
        assert residual < 0.03

    def test_residual_pinned_at_1p72_pct(self):
        """Pin the actual computed residual value documented in
        cluster_merger_internal_scaling_residual (Ch 9, computed).
        The framework's predicted offsets across the four-cluster
        sample scale linearly with v_final to 1.72% internal residual.
        Tolerance: ±0.5% absolute to allow for floating-point drift
        without permitting the value to silently shift.
        """
        preds = predict_population()
        residual = scaling_law_residual(preds)
        assert abs(residual - 0.0172) < 0.005, (
            f"Internal scaling residual = {residual:.4f}, expected "
            f"~0.0172 ± 0.005. If this value has shifted, the "
            f"cluster_merger_internal_scaling_residual claim's "
            f"statement (which pins 1.72%) needs review."
        )


class TestPopulationSummary:
    """Population-level statistics report the honest result."""

    def test_n_in_band_is_3(self):
        s = population_summary(predict_population())
        assert s.n_in_band == 3

    def test_in_band_fraction_75_percent(self):
        s = population_summary(predict_population())
        assert abs(s.in_band_fraction - 0.75) < 1e-9

    def test_median_ratio_around_0p83(self):
        """Median pred/obs ratio reflects 3-of-4 close match."""
        s = population_summary(predict_population())
        assert 0.7 < s.median_ratio < 1.0

    def test_el_gordo_listed_as_outlier(self):
        s = population_summary(predict_population())
        assert "El Gordo" in s.outliers
        assert len(s.outliers) == 1


class TestScalingPredicition:
    """The v × τ_0 scaling produces the expected ratio between systems."""

    def test_macs_offset_about_half_of_bullet(self):
        """v_MACS ≈ 0.5 × v_Bullet → offset_MACS ≈ 0.5 × offset_Bullet."""
        bullet = predict_merger(BULLET, name="Bullet Cluster")
        macs = predict_merger(MACS_J0025, name="MACS J0025")
        ratio = macs.grut_kernel_kpc / bullet.grut_kernel_kpc
        v_ratio = MACS_J0025.v_final_km_s / BULLET.v_final_km_s
        # GRUT prediction: kernel offset is linear in v_final
        assert abs(ratio - v_ratio) / v_ratio < 0.05

    def test_abell_offset_about_half_of_bullet(self):
        bullet = predict_merger(BULLET, name="Bullet Cluster")
        abell = predict_merger(ABELL_520, name="Abell 520")
        ratio = abell.grut_kernel_kpc / bullet.grut_kernel_kpc
        v_ratio = ABELL_520.v_final_km_s / BULLET.v_final_km_s
        assert abs(ratio - v_ratio) / v_ratio < 0.05


class TestVerifyHarness:

    def test_all_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"Population-test failures: {failed}"


class TestObservationalProvenance:
    """Each system's notes field cites its observational source."""

    def test_bullet_cites_clowe(self):
        assert "Clowe" in BULLET.notes or "Markevitch" in BULLET.notes

    def test_macs_cites_bradac(self):
        assert "Bradač" in MACS_J0025.notes or "Bradac" in MACS_J0025.notes

    def test_abell_cites_mahdavi_or_jee(self):
        assert "Mahdavi" in ABELL_520.notes or "Jee" in ABELL_520.notes

    def test_el_gordo_cites_jee(self):
        assert "Jee" in EL_GORDO.notes


class TestElGordoOutlierIsHonestNegative:
    """El Gordo's deviation is documented as an explicit gap, not hidden."""

    def test_el_gordo_notes_acknowledge_model_dependence(self):
        notes = EL_GORDO.notes.lower()
        assert "model" in notes or "different" in notes

    def test_summary_reports_el_gordo_outlier(self):
        s = population_summary(predict_population())
        assert "El Gordo" in s.outliers

    def test_population_doc_acknowledges_outlier(self):
        """Documentation explicitly mentions the outlier status."""
        from grut.derived.cluster import merger_population
        doc = merger_population.__doc__ or ""
        assert "outlier" in doc.lower() or "fail" in doc.lower() or "El Gordo" in doc
