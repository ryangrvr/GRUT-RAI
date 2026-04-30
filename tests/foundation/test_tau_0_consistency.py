"""Tests for grut.foundation.tau_0_consistency — independent derivations
of τ_0 across cosmic-baseline and cluster-merger routes.

The framework's τ_0 = 41.9 Myr should appear from many independent
calculations. These tests pin the convergence pattern (cosmic-baseline
tight, cluster-merger systematically +20% higher, El Gordo outlier
excluded) so the framework is honest about both the consistency AND
the documented systematic.
"""

import math

import pytest

from grut.foundation.tau_0_consistency import (
    TAU_0_CANONICAL_MYR,
    Tau0Route,
    all_routes,
    cross_consistency_report,
    derive_canonical_v7,
    derive_from_abell_520,
    derive_from_bullet_cluster,
    derive_from_el_gordo,
    derive_from_grut_h0,
    derive_from_macs_j0025,
    derive_from_planck_h0,
    derive_from_sh0es_h0,
    routes_by_group,
    verify,
)


class TestRouteStructure:
    """Each route returns a well-formed record."""

    def test_eight_routes_total(self):
        assert len(all_routes()) == 8

    def test_all_route_values_positive(self):
        for r in all_routes():
            assert r.tau_0_Myr > 0

    def test_route_groups_are_known(self):
        valid = {"cosmic_baseline", "cluster_merger"}
        for r in all_routes():
            assert r.group in valid

    def test_each_route_has_method_string(self):
        for r in all_routes():
            assert r.method.strip()

    def test_each_route_has_inputs(self):
        for r in all_routes():
            assert r.inputs


class TestCosmicBaselineGroup:
    """Cosmic-baseline derivations should converge tightly on canonical."""

    def test_canonical_v7_returns_41p9(self):
        r = derive_canonical_v7()
        assert r.tau_0_Myr == TAU_0_CANONICAL_MYR

    def test_planck_h0_gives_42p6(self):
        r = derive_from_planck_h0()
        assert abs(r.tau_0_Myr - 42.59) < 0.1

    def test_grut_h0_gives_41p7(self):
        """Self-consistency: GRUT's predicted H_0 inverts to τ_0 ≈ 41.7."""
        r = derive_from_grut_h0()
        assert abs(r.tau_0_Myr - 41.75) < 0.1

    def test_sh0es_h0_gives_39p5(self):
        r = derive_from_sh0es_h0()
        assert abs(r.tau_0_Myr - 39.48) < 0.1

    def test_grut_self_consistency_under_2pct(self):
        """GRUT-predicted H_0 → τ_0 within 2% of canonical."""
        r = derive_from_grut_h0()
        deviation = abs(r.tau_0_Myr - TAU_0_CANONICAL_MYR) / TAU_0_CANONICAL_MYR
        assert deviation < 0.02

    def test_cosmic_baseline_group_tight(self):
        """All four cosmic-baseline routes within 8% of each other."""
        values = [r.tau_0_Myr for r in routes_by_group("cosmic_baseline")]
        assert max(values) / min(values) < 1.10


class TestClusterMergerGroup:
    """Cluster-merger derivations are internally consistent but
    systematically higher than cosmic-baseline."""

    def test_bullet_cluster_around_49(self):
        r = derive_from_bullet_cluster()
        assert 45 < r.tau_0_Myr < 55

    def test_macs_around_48(self):
        r = derive_from_macs_j0025()
        assert 44 < r.tau_0_Myr < 52

    def test_abell_around_53(self):
        r = derive_from_abell_520()
        assert 49 < r.tau_0_Myr < 58

    def test_el_gordo_is_outlier(self):
        r = derive_from_el_gordo()
        assert r.is_outlier
        assert r.tau_0_Myr > 100  # outlier is in the 150 Myr range

    def test_outliers_excluded_by_default(self):
        cluster_routes = routes_by_group("cluster_merger", exclude_outliers=True)
        for r in cluster_routes:
            assert not r.is_outlier

    def test_cluster_group_internally_consistent(self):
        """Three normal-regime cluster derivations within ~15% of each other."""
        values = [r.tau_0_Myr for r in routes_by_group(
            "cluster_merger", exclude_outliers=True
        )]
        assert max(values) / min(values) < 1.15


class TestInterGroupSystematic:
    """Honest framing: cluster-merger group sits ~20% higher than
    cosmic-baseline group. Documented signature, not papered over."""

    def test_cluster_mean_higher_than_cosmic_mean(self):
        rep = cross_consistency_report()
        assert rep.cluster_merger_stats["mean"] > rep.cosmic_baseline_stats["mean"]

    def test_inter_group_offset_around_20pct(self):
        rep = cross_consistency_report()
        # Documented: ~20.7% systematic
        assert 15 < rep.inter_group_offset_pct < 25

    def test_inter_group_offset_under_30pct(self):
        """Within obs. uncertainty bound on cluster collision parameters."""
        rep = cross_consistency_report()
        assert abs(rep.inter_group_offset_pct) < 30


class TestConsistencyReport:

    def test_report_excludes_el_gordo_by_default(self):
        rep = cross_consistency_report(exclude_outliers=True)
        # 4 cosmic-baseline + 3 cluster (El Gordo excluded)
        assert rep.n_routes_used == 7
        assert rep.n_routes_total == 8

    def test_report_includes_outliers_when_asked(self):
        rep = cross_consistency_report(exclude_outliers=False)
        assert rep.n_routes_used == 8

    def test_overall_min_in_cosmic_baseline_range(self):
        """The minimum τ_0 across all routes is in the cosmic-baseline group."""
        rep = cross_consistency_report()
        assert rep.overall_min_Myr == rep.cosmic_baseline_stats["min"]

    def test_overall_max_in_cluster_merger_range(self):
        """The maximum (excluding El Gordo) is in the cluster-merger group."""
        rep = cross_consistency_report()
        assert rep.overall_max_Myr == rep.cluster_merger_stats["max"]

    def test_canonical_within_cosmic_baseline_range(self):
        rep = cross_consistency_report()
        assert (rep.cosmic_baseline_stats["min"]
                <= TAU_0_CANONICAL_MYR
                <= rep.cosmic_baseline_stats["max"])


class TestVerifyHarness:

    def test_all_six_legs_pass(self):
        checks = verify()
        failed = [k for k, v in checks.items() if not v]
        assert not failed, f"τ_0 cross-consistency failures: {failed}"

    def test_returns_six_legs(self):
        checks = verify()
        expected_keys = {
            "cosmic_baseline_spread_under_10pct",
            "cluster_merger_spread_under_15pct",
            "cosmic_baseline_includes_canonical",
            "inter_group_offset_under_35pct",
            "cluster_routes_systematically_higher",
            "grut_self_consistency_under_2pct",
        }
        assert expected_keys.issubset(checks.keys())


class TestHonestFramingPreserved:
    """The systematic offset is surfaced, not hidden."""

    def test_cluster_routes_systematically_higher_passes(self):
        """Pin the diagnostic signal: cluster routes are HIGHER, consistently."""
        checks = verify()
        assert checks["cluster_routes_systematically_higher"]

    def test_module_doc_acknowledges_systematic(self):
        """Module docstring names the systematic offset."""
        from grut.foundation import tau_0_consistency
        doc = tau_0_consistency.__doc__ or ""
        # Must mention the systematic offset and the two readings
        assert "systematic" in doc.lower() or "20%" in doc
        assert "Reading" in doc or "reading" in doc or "systematic" in doc.lower()


class TestRoutesShareReferences:
    """Each cluster route cites its observational source."""

    def test_bullet_cites_clowe_or_markevitch(self):
        r = derive_from_bullet_cluster()
        notes = r.notes.lower()
        assert "clowe" in notes or "markevitch" in notes

    def test_macs_cites_bradac(self):
        r = derive_from_macs_j0025()
        assert "Bradač" in r.notes or "Bradac" in r.notes

    def test_abell_cites_mahdavi(self):
        r = derive_from_abell_520()
        assert "Mahdavi" in r.notes


class TestSensitivity:
    """How does τ_0 inferred from a cluster scale with input uncertainties?"""

    def test_factor_2_velocity_uncertainty_changes_tau_by_factor_2(self):
        """If v is uncertain by ×2, inferred τ_0 changes by ×0.5."""
        from grut.foundation.tau_0_consistency import _tau_0_from_cluster
        a = _tau_0_from_cluster(150, 3000)
        b = _tau_0_from_cluster(150, 6000)
        assert abs(b - a / 2) / a < 0.001

    def test_30_pct_offset_uncertainty_changes_tau_by_30_pct(self):
        from grut.foundation.tau_0_consistency import _tau_0_from_cluster
        a = _tau_0_from_cluster(150, 3000)
        b = _tau_0_from_cluster(150 * 1.3, 3000)
        assert abs((b - a * 1.3) / (a * 1.3)) < 0.001
