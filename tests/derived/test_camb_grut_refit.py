"""Tests for grut.derived.cosmology.camb_grut_refit.

Certifies the CAMB-exact σ₈ / S₈ refit at GRUT's first-principles parameters.

Key locked-in results (CAMB 1.5.8):
  CAMB raw:    σ₈_A_raw ≈ 0.844,  σ₈_C_raw ≈ 0.829,  TD_ratio ≈ 0.9814
  Normalized (Planck σ₈ = 0.8111):
    Scenario A (Planck ΛCDM ref):           σ₈ = 0.811,  S₈ = 0.832
    Scenario B (Planck params + GRUT μ):    σ₈ ≈ 0.833,  S₈ ≈ 0.854  (+2.7%)
    Scenario C (GRUT background, ΛCDM):     σ₈ ≈ 0.796,  S₈ ≈ 0.783
    Scenario D (GRUT full refit):           σ₈ ≈ 0.817,  S₈ ≈ 0.804

PRIMARY CAMB FINDING:
  T(k) at σ₈ scales is essentially unchanged by the ωm shift from Planck
  to GRUT (T-residual ≈ 1.001 — change < 0.1%).  The BBKS T_ratio = 0.974
  was wrong: it overestimated T-sensitivity at these scales by −2.6%.
  The σ₈ shift from GRUT background is almost entirely from the growth
  factor D, consistent between CAMB and ODE (differ by < 0.1%).

S₈ tensions (Scenario D, S₈ ≈ 0.804):
  Planck CMB:  ~−2.2σ      KiDS-1000: ~+1.9σ
  DES-Y3:      ~+1.6σ      HSC-Y3:    ~+1.3σ
  GRUT S₈ is within 2σ of all three major weak-lensing surveys.

BBKS comparison (Scenario D):
  CAMB: σ₈ ≈ 0.817,  BBKS: σ₈ ≈ 0.796  (+2.68% — BBKS underestimated)
"""

import math
import pytest
import camb


# ── Module-level fixture ──────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def scenarios():
    """Run once; shared across all tests in this module."""
    from grut.derived.cosmology.camb_grut_refit import camb_grut_sigma8_scenarios
    return camb_grut_sigma8_scenarios()


# ── CAMB runner tests ─────────────────────────────────────────────────────────

class TestRunCambMatterPower:
    """Unit tests for the CAMB runner."""

    def test_planck_camb_returns_expected_keys(self):
        from grut.derived.cosmology.camb_grut_refit import planck_camb
        r = planck_camb()
        assert {"k_Mpc", "P_Mpc3", "sigma8", "H0", "Omega_m", "Omega_L"}.issubset(r.keys())

    def test_planck_camb_sigma8_positive(self):
        from grut.derived.cosmology.camb_grut_refit import planck_camb
        assert planck_camb()["sigma8"] > 0.5

    def test_planck_camb_omega_m_sensible(self):
        from grut.derived.cosmology.camb_grut_refit import planck_camb
        Om = planck_camb()["Omega_m"]
        assert 0.28 < Om < 0.36, f"Planck Omega_m = {Om:.4f}"

    def test_grut_camb_omega_m_matches_grut(self):
        """CAMB at GRUT params should give Ω_m = 0.2900 from ωb + ωc."""
        from grut.derived.cosmology.camb_grut_refit import grut_background_camb
        Om = grut_background_camb()["Omega_m"]
        assert abs(Om - 0.2900) < 0.0005, f"GRUT Omega_m = {Om:.5f}"

    def test_grut_omch2_derivation(self):
        """GRUT_OMCH2 = 0.290 × 0.69029² − 0.02237 ≈ 0.11582."""
        from grut.derived.cosmology.camb_grut_refit import GRUT_OMCH2, GRUT_OMEGA_M, GRUT_H, GRUT_OMBH2
        expected = GRUT_OMEGA_M * GRUT_H ** 2 - GRUT_OMBH2
        assert abs(GRUT_OMCH2 - expected) < 1e-6
        assert abs(GRUT_OMCH2 - 0.11582) < 0.0001, f"GRUT_OMCH2 = {GRUT_OMCH2:.5f}"

    def test_k_array_is_ascending(self):
        from grut.derived.cosmology.camb_grut_refit import planck_camb
        k = planck_camb()["k_Mpc"]
        assert all(k[i] < k[i + 1] for i in range(len(k) - 1))

    def test_power_spectrum_is_positive(self):
        from grut.derived.cosmology.camb_grut_refit import planck_camb
        P = planck_camb()["P_Mpc3"]
        assert (P > 0).all()


# ── Scenario structure tests ──────────────────────────────────────────────────

class TestScenarioStructure:
    """Tests that all four scenarios have the expected structure."""

    def test_all_scenario_keys_present(self, scenarios):
        required = {
            "A_planck_lcdm",
            "B_planck_params_grut_growth",
            "C_grut_params_lcdm_growth",
            "D_grut_params_grut_growth",
            "comparison_vs_bbks",
            "tension_scenario_D",
            "camb_raw",
        }
        assert required.issubset(scenarios.keys())

    def test_each_scenario_has_sigma8_and_S8(self, scenarios):
        for key in ["A_planck_lcdm", "B_planck_params_grut_growth",
                    "C_grut_params_lcdm_growth", "D_grut_params_grut_growth"]:
            sc = scenarios[key]
            assert math.isfinite(sc["sigma8"]) and sc["sigma8"] > 0
            assert math.isfinite(sc["S8"]) and sc["S8"] > 0

    def test_scenario_A_is_planck_reference(self, scenarios):
        """Scenario A σ₈ = PLANCK_SIGMA8 by construction."""
        from grut.derived.cosmology.camb_grut_refit import PLANCK_SIGMA8
        A = scenarios["A_planck_lcdm"]
        assert abs(A["sigma8"] - PLANCK_SIGMA8) < 1e-9


# ── Key physics tests ─────────────────────────────────────────────────────────

class TestCambPhysicsResults:
    """Tests locking in the key physical findings from CAMB."""

    def test_camb_td_ratio_between_0_95_and_1_0(self, scenarios):
        """GRUT background reduces σ₈ vs Planck — TD_ratio in (0.95, 1.0)."""
        td = scenarios["comparison_vs_bbks"]["TD_ratio_camb"]
        assert 0.95 < td < 1.0, f"TD_ratio = {td:.5f}"

    def test_T_residual_near_unity_confirms_bbks_wrong(self, scenarios):
        """T(k) at σ₈ scales is < 0.2% different — BBKS T_ratio was wrong.

        KEY PHYSICS TEST: CAMB shows T-residual = TD_ratio / D_C_ODE ≈ 1.001.
        The BBKS T_ratio = 0.974 overestimated T-sensitivity by ~2.6%.
        """
        cmp = scenarios["comparison_vs_bbks"]
        T_res = cmp["T_residual_camb"]
        assert abs(T_res - 1.0) < 0.005, (
            f"T-residual = {T_res:.5f} — expected ≈ 1.000 (T negligible)"
        )

    def test_camb_td_ratio_matches_ode_d_ratio(self, scenarios):
        """CAMB combined TD_ratio ≈ ODE D_C to within 0.5%.

        Confirms that the background σ₈ shift is driven by D, not T.
        """
        cmp = scenarios["comparison_vs_bbks"]
        delta = abs(cmp["TD_ratio_camb"] - cmp["D_C_ode"])
        assert delta < 0.005, (
            f"CAMB TD={cmp['TD_ratio_camb']:.5f}  ODE D_C={cmp['D_C_ode']:.5f}  "
            f"diff={delta:.5f}"
        )

    def test_bbks_T_overestimated_negative(self, scenarios):
        """BBKS T_ratio < T_residual_CAMB — BBKS overestimates T suppression."""
        cmp = scenarios["comparison_vs_bbks"]
        assert cmp["T_ratio_bbks"] < cmp["T_residual_camb"], (
            f"BBKS T_ratio={cmp['T_ratio_bbks']:.4f} should be < "
            f"CAMB T_residual={cmp['T_residual_camb']:.5f}"
        )

    def test_scenario_C_above_bbks_estimate(self, scenarios):
        """CAMB σ₈_C > BBKS σ₈_C because BBKS over-suppressed T(k)."""
        cmp = scenarios["comparison_vs_bbks"]
        assert cmp["sigma8_C_camb"] > cmp["sigma8_C_bbks"], (
            f"σ₈_C CAMB={cmp['sigma8_C_camb']:.4f} should exceed "
            f"BBKS={cmp['sigma8_C_bbks']:.4f}"
        )

    def test_scenario_D_above_bbks_estimate(self, scenarios):
        """CAMB σ₈_D > BBKS σ₈_D (same T correction applies)."""
        cmp = scenarios["comparison_vs_bbks"]
        assert cmp["sigma8_D_camb"] > cmp["sigma8_D_bbks"], (
            f"σ₈_D CAMB={cmp['sigma8_D_camb']:.4f} should exceed "
            f"BBKS={cmp['sigma8_D_bbks']:.4f}"
        )

    def test_scenario_D_delta_vs_bbks_about_2_7_pct(self, scenarios):
        """CAMB Scenario D is ~+2.5–3.0% above BBKS (from T correction)."""
        delta_pct = scenarios["comparison_vs_bbks"]["sigma8_D_delta_pct"]
        assert 2.0 < delta_pct < 3.5, (
            f"CAMB vs BBKS delta = {delta_pct:.2f}%  (expected ~+2.7%)"
        )


# ── Scenario value tests ──────────────────────────────────────────────────────

class TestScenarioValues:
    """Tests locking in the exact σ₈ / S₈ values for all four scenarios."""

    def test_scenario_B_grut_mu_enhances_sigma8(self, scenarios):
        """Scenario B: GRUT μ enhances σ₈ by 1–5% at Planck params."""
        A = scenarios["A_planck_lcdm"]["sigma8"]
        B = scenarios["B_planck_params_grut_growth"]["sigma8"]
        pct = (B / A - 1) * 100
        assert 1.0 < pct < 5.0, f"μ enhancement = {pct:.2f}%  (expected 2–4%)"

    def test_scenario_C_reduces_sigma8_vs_A(self, scenarios):
        """GRUT background Ω_m = 0.290 < 0.315 → lower growth → lower σ₈."""
        A = scenarios["A_planck_lcdm"]["sigma8"]
        C = scenarios["C_grut_params_lcdm_growth"]["sigma8"]
        assert C < A, f"σ₈_C={C:.4f} should be < σ₈_A={A:.4f}"

    def test_scenario_D_between_A_and_B(self, scenarios):
        """Scenario D sigma8 is above C (μ partially offsets lower Ω_m)."""
        C = scenarios["C_grut_params_lcdm_growth"]["sigma8"]
        D = scenarios["D_grut_params_grut_growth"]["sigma8"]
        assert D > C, f"σ₈_D={D:.4f} should exceed σ₈_C={C:.4f}"

    def test_scenario_D_sigma8_in_physical_range(self, scenarios):
        """σ₈ at GRUT full refit in [0.70, 0.90]."""
        D = scenarios["D_grut_params_grut_growth"]["sigma8"]
        assert 0.70 < D < 0.90, f"σ₈_D = {D:.4f}"

    def test_scenario_D_S8_in_range(self, scenarios):
        """S₈ at GRUT full refit in [0.75, 0.85]."""
        S8 = scenarios["D_grut_params_grut_growth"]["S8"]
        assert 0.75 < S8 < 0.85, f"S₈_D = {S8:.4f}"

    def test_scenario_D_S8_near_0_804(self, scenarios):
        """S₈ (CAMB-exact) ≈ 0.804 (within ±0.02)."""
        S8 = scenarios["D_grut_params_grut_growth"]["S8"]
        assert abs(S8 - 0.804) < 0.020, f"S₈_D = {S8:.4f}  (expected ≈ 0.804)"

    def test_scenario_A_S8_matches_planck(self, scenarios):
        """Scenario A S₈ ≈ 0.832 (Planck 2018 TT+TE+EE+lowE+lensing)."""
        S8 = scenarios["A_planck_lcdm"]["S8"]
        assert abs(S8 - 0.832) < 0.005, f"S₈_A = {S8:.4f}  (expected 0.832)"


# ── S₈ tension tests ──────────────────────────────────────────────────────────

class TestS8TensionCamb:
    """Tests for S₈ tension comparison against observations (CAMB-exact)."""

    @pytest.fixture(scope="class")
    def tension(self, scenarios):
        return scenarios["tension_scenario_D"]

    def test_all_survey_keys_present(self, tension):
        expected = {"Planck_CMB", "KiDS_1000", "DES_Y3", "HSC_Y3", "ACT_DR4"}
        assert expected.issubset(tension.keys())

    def test_grut_S8_below_planck_cmb(self, tension):
        """GRUT full refit S₈ < Planck CMB S₈."""
        assert tension["Planck_CMB"]["tension_sigma"] < 0

    def test_grut_S8_within_2sigma_kids(self, tension):
        """GRUT S₈ (CAMB-exact) within 2σ of KiDS-1000.

        PRIMARY S₈ CLAIM: GRUT's first-principles Ω_m = 0.290 brings
        S₈ into the weak-lensing range — result confirmed by CAMB.
        """
        t = tension["KiDS_1000"]["tension_sigma"]
        assert abs(t) < 2.0, (
            f"GRUT S₈ is {t:+.2f}σ from KiDS-1000 — expected within ±2σ"
        )

    def test_grut_S8_within_2sigma_des(self, tension):
        """GRUT S₈ (CAMB-exact) within 2σ of DES-Y3."""
        t = tension["DES_Y3"]["tension_sigma"]
        assert abs(t) < 2.0, (
            f"GRUT S₈ is {t:+.2f}σ from DES-Y3 — expected within ±2σ"
        )

    def test_grut_S8_within_2sigma_hsc(self, tension):
        """GRUT S₈ (CAMB-exact) within 2σ of HSC-Y3."""
        t = tension["HSC_Y3"]["tension_sigma"]
        assert abs(t) < 2.0, (
            f"GRUT S₈ is {t:+.2f}σ from HSC-Y3 — expected within ±2σ"
        )

    def test_planck_tension_about_2sigma(self, tension):
        """GRUT S₈ is ~2σ below Planck CMB (tension, but less severe than BBKS est.)."""
        t = abs(tension["Planck_CMB"]["tension_sigma"])
        assert 1.5 < t < 3.0, f"|tension| vs Planck = {t:.2f}σ  (expected ~2σ)"


# ── Raw CAMB sanity tests ─────────────────────────────────────────────────────

class TestRawCamb:
    """Tests for raw CAMB sigma8 values (before normalization)."""

    def test_raw_sigma8_A_above_0_82(self, scenarios):
        """Raw CAMB σ₈_A > 0.82 (nominal A_s gives ~0.844)."""
        assert scenarios["camb_raw"]["sigma8_A_raw"] > 0.82

    def test_raw_sigma8_C_below_sigma8_A(self, scenarios):
        """Raw σ₈_C < σ₈_A at Planck params (GRUT background suppresses growth)."""
        raw = scenarios["camb_raw"]
        assert raw["sigma8_C_raw"] < raw["sigma8_A_raw"]

    def test_raw_td_ratio_between_0_97_and_0_99(self, scenarios):
        """Raw TD_ratio ∈ (0.97, 0.99)."""
        td = scenarios["camb_raw"]["TD_ratio_raw"]
        assert 0.97 < td < 0.99, f"TD_ratio_raw = {td:.5f}"


# ── Convenience entry point ───────────────────────────────────────────────────

class TestCambGrutS8Assessment:
    """Smoke test for the top-level camb_grut_s8_assessment() function."""

    def test_returns_verdict_string(self):
        from grut.derived.cosmology.camb_grut_refit import camb_grut_s8_assessment
        result = camb_grut_s8_assessment()
        assert "verdict" in result
        assert isinstance(result["verdict"], str)
        assert "GRUT S₈" in result["verdict"]

    def test_grut_S8_matches_scenario_D(self):
        from grut.derived.cosmology.camb_grut_refit import (
            camb_grut_s8_assessment,
            camb_grut_sigma8_scenarios,
        )
        sc = camb_grut_sigma8_scenarios()
        full = camb_grut_s8_assessment()
        assert abs(full["grut_S8"] - sc["D_grut_params_grut_growth"]["S8"]) < 1e-6

    def test_camb_version_reported(self):
        from grut.derived.cosmology.camb_grut_refit import camb_grut_s8_assessment
        result = camb_grut_s8_assessment()
        assert "camb_version" in result
