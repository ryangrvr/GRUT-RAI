"""Tests for Track VII Step 3 — correct topology and vortex/vorton physics.

Lock in:
  - Topology analysis correctly identifies strings, not monopoles
  - BPS string tension μ = π v² = 0.56 GeV²
  - Gμ is well below CMB bound (10⁻⁷) by many orders
  - Pure string scaling gives negligible Ω (~10⁻⁴²)
  - Vorton abundance with XY universality UNDER-produces by factor ~30
  - M_vorton mismatch with V7 M_soliton (factor ~450) is a real discrepancy

This is the hardest test suite to write honestly — it locks in that
Step 3 REOPENS Track VII rather than closing it.
"""

import pytest
import numpy as np


class TestTopologicalDefectAnalysis:
    """π_n(U(1)) → cosmic strings, not monopoles."""

    def test_identifies_strings_not_monopoles(self):
        from grut.derived.dark_matter.vortex_strings import topological_defect_analysis
        r = topological_defect_analysis()
        assert "string" in r["dominant_defect"].lower()
        assert "NO monopoles" in r["pi_2"]

    def test_defect_dimension_is_one(self):
        from grut.derived.dark_matter.vortex_strings import topological_defect_analysis
        r = topological_defect_analysis()
        assert r["defect_dimension"] == 1

    def test_flags_step_1_topology_inconsistency(self):
        from grut.derived.dark_matter.vortex_strings import topological_defect_analysis
        r = topological_defect_analysis()
        assert "INCONSISTENT" in r["step_1_assumption"]


class TestBPSStringTension:
    """μ = π v² for Nielsen-Olesen BPS vortex."""

    def test_tension_is_pi_v_squared(self):
        from grut.derived.dark_matter.vortex_strings import bps_string_tension
        r = bps_string_tension(v_GeV=0.422)
        expected = np.pi * 0.422**2
        assert abs(r["mu_BPS_GeV2"] - expected) < 1e-10

    def test_Gmu_far_below_CMB_limit(self):
        """Dark string Gμ ~ 10⁻³⁹, far below CMB's 10⁻⁷ bound."""
        from grut.derived.dark_matter.vortex_strings import bps_string_tension
        r = bps_string_tension()
        assert r["G_mu_dimensionless"] < 1e-30
        # At least 20 orders below CMB limit
        assert r["below_CMB_limit_by_orders"] > 20

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.vortex_strings import bps_string_tension
        r = bps_string_tension()
        for k in ["v_GeV", "mu_BPS_GeV2", "G_mu_dimensionless",
                   "CMB_limit_Gmu", "r_core_GeV_inv"]:
            assert k in r


class TestStringScalingSolution:
    """Pure string scaling → negligible Ω."""

    def test_Omega_string_is_negligible(self):
        from grut.derived.dark_matter.vortex_strings import string_scaling_solution_relic
        r = string_scaling_solution_relic()
        # Pure strings give Ω < 10⁻³⁰ (need DM >> this)
        assert r["Omega_string_today"] < 1e-30

    def test_verdict_mentions_cannot_account_for_DM(self):
        from grut.derived.dark_matter.vortex_strings import string_scaling_solution_relic
        r = string_scaling_solution_relic()
        assert "cannot account" in r["verdict"].lower()


class TestVortonRelic:
    """Vortons from Kibble-Zurek loops — UNDER-produce with XY universality."""

    def test_XY_universality_under_produces(self):
        """CORRECT universality class UNDER-produces Ω_dm by factor ~30."""
        from grut.derived.dark_matter.vortex_strings import vorton_relic_from_kibble_zurek
        r = vorton_relic_from_kibble_zurek(nu=0.672, z_dyn=2.04,
                                             use_constitutive=True)
        # XY result: Ω ~ 0.008, factor ~30 low
        assert r["Omega_vorton"] < 0.05
        assert r["ratio_to_observed"] < 0.1

    def test_M_vorton_far_below_M_soliton(self):
        """Natural KZ-loop vorton mass ~10⁶ GeV, not M_soliton ~10⁹ GeV."""
        from grut.derived.dark_matter.vortex_strings import vorton_relic_from_kibble_zurek
        r = vorton_relic_from_kibble_zurek(nu=0.672, z_dyn=2.04,
                                             use_constitutive=True)
        # Factor >100 mismatch
        assert r["M_vorton_GeV"] < r["M_soliton_V7_GeV"] / 100

    def test_returns_expected_keys(self):
        from grut.derived.dark_matter.vortex_strings import vorton_relic_from_kibble_zurek
        r = vorton_relic_from_kibble_zurek()
        for k in ["M_vorton_GeV", "n_vorton_today_per_m3", "Omega_vorton",
                  "ratio_to_observed", "log10_deviation"]:
            assert k in r


class TestMVortonAudit:
    """The mass mismatch: V7's M_soliton vs KZ-natural M_vorton."""

    def test_audit_reports_large_ratio(self):
        from grut.derived.dark_matter.vortex_strings import M_vorton_vs_M_soliton_audit
        r = M_vorton_vs_M_soliton_audit(xi_KZ_natural=1.33e6)
        # M_soliton / M_vorton_KZ > 100 (actually ~450 for XY)
        assert r["M_soliton_over_M_vorton_KZ"] > 100

    def test_required_R_much_larger_than_xi_KZ(self):
        from grut.derived.dark_matter.vortex_strings import M_vorton_vs_M_soliton_audit
        r = M_vorton_vs_M_soliton_audit(xi_KZ_natural=1.33e6)
        assert r["R_over_xi_KZ"] > 100


class TestLoopSizeSensitivity:
    """Scan over loop-size hypotheses."""

    def test_small_loops_under_produce(self):
        from grut.derived.dark_matter.vortex_strings import loop_size_sensitivity_scan
        r = loop_size_sensitivity_scan()
        # String core size gives way too little
        assert r["scenarios"]["string_core_1_over_m_h"]["Omega_vorton"] < 1e-6

    def test_horizon_scale_loops_over_produce(self):
        from grut.derived.dark_matter.vortex_strings import loop_size_sensitivity_scan
        r = loop_size_sensitivity_scan()
        # Horizon-size loops give way too much
        assert r["scenarios"]["1_over_H_PT"]["Omega_vorton"] > 1e6

    def test_required_R_is_not_typical_KZ_size(self):
        from grut.derived.dark_matter.vortex_strings import loop_size_sensitivity_scan
        r = loop_size_sensitivity_scan()
        # Required R to match observed is >5x xi_KZ
        assert r["R_required_over_xi_KZ"] > 5


class TestStep3Summary:
    """Full Step 3 verdict."""

    def test_status_says_REOPENED(self):
        """Step 3 REOPENS Track VII rather than closing it."""
        from grut.derived.dark_matter.vortex_strings import track_vii_step_3_summary
        r = track_vii_step_3_summary()
        assert "REOPENED" in r["status"]

    def test_verdict_flags_step_1_wrong(self):
        from grut.derived.dark_matter.vortex_strings import track_vii_step_3_summary
        r = track_vii_step_3_summary()
        assert "WRONG topology" in r["verdict"] or "Step 1" in r["verdict"]

    def test_includes_all_four_scenarios(self):
        from grut.derived.dark_matter.vortex_strings import track_vii_step_3_summary
        r = track_vii_step_3_summary()
        assert "scenario_1_pure_strings" in r
        assert "scenario_2_vortons_from_KZ_loops" in r
        assert "M_vorton_audit" in r
        assert "loop_size_sensitivity" in r
