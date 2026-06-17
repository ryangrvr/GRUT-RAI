"""Tests for grut.derived.cosmology.cmb_isw.

Certifies the CMB low-ℓ ISW prediction:
  - GRUT reduced potential Φ̃(a=1) ≈ 2.079 at k=10⁻³ Mpc⁻¹ (locked)
  - ΛCDM reduced potential Φ̃(a=1) ≈ 0.788 at k=10⁻³ Mpc⁻¹ (locked)
  - Ratio GRUT/ΛCDM ≈ 2.64 (locked)
  - μ_GRUT at z=1100 ≈ 1.0 (SW unchanged; locked)
  - ISW direction: GRUT → cooling (potential deepened)
                  ΛCDM → heating (potential decayed)
  - ISW amplitude ratio ≈ 5.09 (locked)
  - Consistent with Planck low-ℓ anomaly direction

Key physics locked in:
  Φ̃_GRUT(z=0) = 2.079   ΔΦ̃ = +1.079   ISW = cooling → reduces D_ℓ at ℓ=10–30
  Φ̃_ΛCDM(z=0) = 0.788   ΔΦ̃ = −0.212   ISW = heating → adds D_ℓ at ℓ=10–30
  Ratio = 2.64×  ISW amplitude ratio = 5.09×
  μ at z=1100 = 1.0017 (SW unmodified at 0.17%)
  GRUT transition z★ ≈ 77 (before structure formation, after recombination)
"""

import math
import pytest


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture(scope="module")
def comparison():
    from grut.derived.cosmology.cmb_isw import cmb_isw_comparison
    return cmb_isw_comparison()

@pytest.fixture(scope="module")
def history_low_ell():
    from grut.derived.cosmology.cmb_isw import reduced_potential_history, CMB_K_LOW_ELL
    return reduced_potential_history(CMB_K_LOW_ELL)

@pytest.fixture(scope="module")
def history_horizon():
    from grut.derived.cosmology.cmb_isw import reduced_potential_history, CMB_K_HORIZON
    return reduced_potential_history(CMB_K_HORIZON)


# ── Constants ─────────────────────────────────────────────────────────────────

class TestCMBISWConstants:
    """Verify module constants are physically correct."""

    def test_cmb_k_low_ell(self):
        from grut.derived.cosmology.cmb_isw import CMB_K_LOW_ELL
        assert abs(CMB_K_LOW_ELL - 1e-3) < 1e-6, "CMB_K_LOW_ELL should be 10⁻³ Mpc⁻¹"

    def test_cmb_k_horizon(self):
        from grut.derived.cosmology.cmb_isw import CMB_K_HORIZON
        assert abs(CMB_K_HORIZON - 4.5e-4) < 1e-7, "CMB_K_HORIZON should be 4.5×10⁻⁴ Mpc⁻¹"

    def test_tau0_c_mpc_correct(self):
        """c τ₀ ≈ 12.85 Mpc is the GRUT characteristic length scale."""
        from grut.derived.cosmology.cmb_isw import TAU0_C_MPC
        assert 12.5 < TAU0_C_MPC < 13.2, f"c τ₀ = {TAU0_C_MPC:.3f} Mpc, expected ~12.85"

    def test_planck_low_ell_ratio_in_range(self):
        from grut.derived.cosmology.cmb_isw import PLANCK_LOW_ELL_RATIO
        assert 0.70 < PLANCK_LOW_ELL_RATIO < 0.95, (
            f"PLANCK_LOW_ELL_RATIO = {PLANCK_LOW_ELL_RATIO}, expected 0.70–0.95"
        )

    def test_grut_omega_m(self):
        from grut.derived.cosmology.cmb_isw import GRUT_OMEGA_M
        assert abs(GRUT_OMEGA_M - 0.290) < 0.001

    def test_planck_omega_m(self):
        from grut.derived.cosmology.cmb_isw import PLANCK_OMEGA_M
        assert abs(PLANCK_OMEGA_M - 0.3153) < 0.001


# ── GRUT transition epoch ─────────────────────────────────────────────────────

class TestGRUTTransitionEpoch:
    """Verify GRUT modification starts well after recombination and before LSS."""

    def test_transition_before_recombination_is_false(self):
        """The GRUT modification should NOT be active at recombination for CMB scales."""
        from grut.derived.cosmology.cmb_isw import grut_transition_scale, CMB_K_LOW_ELL
        a_star = grut_transition_scale(CMB_K_LOW_ELL)
        a_rec  = 1.0 / 1100.0
        assert a_star > a_rec, (
            f"a★ = {a_star:.5f} should be > a_rec = {a_rec:.5f}: "
            "modification starts after recombination ✓"
        )

    def test_transition_z_locked(self):
        """GRUT transition at k=10⁻³ occurs at z★ ≈ 77 (locked)."""
        from grut.derived.cosmology.cmb_isw import grut_transition_scale, CMB_K_LOW_ELL
        a_star = grut_transition_scale(CMB_K_LOW_ELL)
        z_star = 1.0 / a_star - 1.0
        assert 60 < z_star < 100, f"z★ = {z_star:.1f}, expected ~77"

    def test_mu_at_recombination_near_one(self):
        """μ_GRUT at z=1100 ≈ 1.0017 — SW is virtually unchanged."""
        from grut.derived.cosmology.cmb_isw import mu_at_recombination, CMB_K_LOW_ELL
        mu = mu_at_recombination(CMB_K_LOW_ELL)
        assert abs(mu - 1.0) < 0.005, f"μ(z=1100) = {mu:.5f}, expected ~1.0"

    def test_mu_at_recombination_locked(self):
        """μ_GRUT(k=10⁻³, z=1100) ≈ 1.0017 (locked)."""
        from grut.derived.cosmology.cmb_isw import mu_at_recombination, CMB_K_LOW_ELL
        mu = mu_at_recombination(CMB_K_LOW_ELL)
        assert abs(mu - 1.0017) < 0.0005, f"μ(z=1100) = {mu:.5f}, expected 1.0017"


# ── Reduced potential history ─────────────────────────────────────────────────

class TestReducedPotentialHistory:
    """Verify Φ̃(a) evolution for GRUT vs ΛCDM."""

    def test_history_has_required_keys(self, history_low_ell):
        required = {
            "a_arr", "phi_grut", "phi_lcdm",
            "phi_grut_today", "phi_lcdm_today", "phi_ratio",
            "delta_phi_grut", "delta_phi_lcdm",
            "isw_sign_grut", "isw_sign_lcdm",
            "isw_amplitude_ratio", "a_star", "z_star",
            "mu_at_rec", "k_mpc",
        }
        assert required.issubset(history_low_ell.keys())

    def test_lcdm_phi_normalised_at_init(self, history_low_ell):
        """Φ̃_ΛCDM(a_init) = 1.0 (normalization check)."""
        phi = history_low_ell["phi_lcdm"]
        assert abs(phi[0] - 1.0) < 0.01, f"ΛCDM Φ̃(a_init) = {phi[0]:.4f}, expected 1.0"

    def test_grut_phi_normalised_at_init(self, history_low_ell):
        """Φ̃_GRUT(a_init) = 1.0 (at a_init, μ≈1 for both)."""
        phi = history_low_ell["phi_grut"]
        assert abs(phi[0] - 1.0) < 0.01, f"GRUT Φ̃(a_init) = {phi[0]:.4f}, expected 1.0"

    def test_lcdm_phi_decays(self, history_low_ell):
        """ΛCDM Φ̃ decays monotonically (potential weakens under Λ)."""
        phi = history_low_ell["phi_lcdm"]
        # Monotonic up to small noise from ODE — check net direction
        assert phi[-1] < phi[0], "ΛCDM potential should decay from a_init to today"
        assert phi[-1] < 0.95, f"ΛCDM Φ̃ at a=1 = {phi[-1]:.3f}, expected < 0.95"

    def test_grut_phi_grows(self, history_low_ell):
        """GRUT Φ̃ GROWS significantly (potential deepens from μ>1)."""
        phi = history_low_ell["phi_grut"]
        assert phi[-1] > 1.5, (
            f"GRUT Φ̃ at a=1 = {phi[-1]:.3f}, expected > 1.5 (potential deepened)"
        )

    def test_grut_phi_today_locked(self, history_low_ell):
        """Φ̃_GRUT(a=1) ≈ 2.079 at k=10⁻³ Mpc⁻¹ (locked)."""
        phi_today = history_low_ell["phi_grut_today"]
        assert abs(phi_today - 2.079) < 0.050, (
            f"Φ̃_GRUT(z=0) = {phi_today:.4f}, expected 2.079"
        )

    def test_lcdm_phi_today_locked(self, history_low_ell):
        """Φ̃_ΛCDM(a=1) ≈ 0.788 at k=10⁻³ Mpc⁻¹ (locked)."""
        phi_today = history_low_ell["phi_lcdm_today"]
        assert abs(phi_today - 0.788) < 0.020, (
            f"Φ̃_ΛCDM(z=0) = {phi_today:.4f}, expected 0.788"
        )

    def test_phi_ratio_locked(self, history_low_ell):
        """Φ̃_GRUT / Φ̃_ΛCDM ≈ 2.64 at z=0 (locked)."""
        r = history_low_ell["phi_ratio"]
        assert abs(r - 2.64) < 0.15, f"phi_ratio = {r:.3f}, expected ~2.64"

    def test_grut_phi_above_lcdm(self, history_low_ell):
        """GRUT potential is deeper than ΛCDM at all late times."""
        phi_g = history_low_ell["phi_grut"]
        phi_l = history_low_ell["phi_lcdm"]
        a_arr = history_low_ell["a_arr"]
        # At all a > 0.1, GRUT Φ̃ > ΛCDM Φ̃
        late = a_arr > 0.1
        assert all(phi_g[late] > phi_l[late]), (
            "GRUT reduced potential should exceed ΛCDM at a > 0.1"
        )


# ── ISW direction and amplitude ───────────────────────────────────────────────

class TestISWSign:
    """Verify the ISW cooling/heating direction for GRUT vs ΛCDM."""

    def test_grut_isw_is_cooling(self, history_low_ell):
        """GRUT ISW is cooling: Φ̃ deepened → photons lose energy."""
        assert history_low_ell["isw_sign_grut"] == "cooling"

    def test_lcdm_isw_is_heating(self, history_low_ell):
        """ΛCDM ISW is heating: Φ̃ decayed → photons gain energy."""
        assert history_low_ell["isw_sign_lcdm"] == "heating"

    def test_delta_phi_grut_positive(self, history_low_ell):
        """ΔΦ̃_GRUT = Φ̃(1) − 1 > 0: potential deepened from MD to today."""
        dphi = history_low_ell["delta_phi_grut"]
        assert dphi > 0.5, f"ΔΦ̃_GRUT = {dphi:.4f}, expected > 0.5"

    def test_delta_phi_lcdm_negative(self, history_low_ell):
        """ΔΦ̃_ΛCDM = Φ̃(1) − 1 < 0: potential decayed from MD to today."""
        dphi = history_low_ell["delta_phi_lcdm"]
        assert dphi < -0.10, f"ΔΦ̃_ΛCDM = {dphi:.4f}, expected < -0.10"

    def test_isw_amplitude_ratio_locked(self, history_low_ell):
        """ISW amplitude ratio |GRUT|/|ΛCDM| ≈ 5.09 (locked)."""
        r = history_low_ell["isw_amplitude_ratio"]
        assert abs(r - 5.09) < 0.50, f"ISW amplitude ratio = {r:.3f}, expected ~5.09"

    def test_isw_amplitude_ratio_exceeds_three(self, history_low_ell):
        """GRUT ISW signal is at least 3× larger than ΛCDM ISW."""
        assert history_low_ell["isw_amplitude_ratio"] > 3.0

    def test_isw_signs_opposite(self, history_low_ell):
        """GRUT and ΛCDM ISW have opposite signs (cooling vs heating)."""
        assert history_low_ell["isw_sign_grut"] != history_low_ell["isw_sign_lcdm"]


# ── Horizon-scale results ─────────────────────────────────────────────────────

class TestHorizonScale:
    """Verify reduced potential at horizon / quadrupole scale k=4.5×10⁻⁴ Mpc⁻¹."""

    def test_horizon_phi_grut_larger_than_low_ell(self, history_low_ell, history_horizon):
        """Longer-wavelength modes are more affected: phi_grut_hor > phi_grut_le."""
        assert history_horizon["phi_grut_today"] > history_low_ell["phi_grut_today"]

    def test_horizon_ratio_locked(self, history_horizon):
        """Φ̃_GRUT / Φ̃_ΛCDM ≈ 3.06 at k=4.5×10⁻⁴ Mpc⁻¹ (locked)."""
        r = history_horizon["phi_ratio"]
        assert abs(r - 3.06) < 0.20, f"horizon phi_ratio = {r:.3f}, expected ~3.06"

    def test_horizon_isw_also_cooling(self, history_horizon):
        """ISW cooling direction holds at horizon scale too."""
        assert history_horizon["isw_sign_grut"] == "cooling"


# ── Full comparison dict ──────────────────────────────────────────────────────

class TestCMBISWComparison:
    """Verify the cached full CMB ISW comparison dict."""

    def test_has_required_keys(self, comparison):
        required = {
            "phi_grut_today_low_ell", "phi_lcdm_today_low_ell", "phi_ratio_low_ell",
            "delta_phi_grut_low_ell", "delta_phi_lcdm_low_ell",
            "isw_amplitude_ratio_low_ell",
            "phi_grut_today_horizon", "phi_lcdm_today_horizon", "phi_ratio_horizon",
            "isw_sign_grut", "isw_sign_lcdm",
            "isw_prediction_ell2", "isw_prediction_ell10_30",
            "planck_low_ell_ratio", "planck_consistent",
            "tau0_c_mpc", "mu_at_recombination",
            "a_star_low_ell", "z_star_low_ell",
            "note",
        }
        assert required.issubset(comparison.keys())

    def test_phi_grut_today_locked(self, comparison):
        """Φ̃_GRUT(z=0) ≈ 2.079 at k=10⁻³ Mpc⁻¹ (locked)."""
        v = comparison["phi_grut_today_low_ell"]
        assert abs(v - 2.079) < 0.060, f"Φ̃_GRUT = {v:.4f}, expected 2.079"

    def test_phi_lcdm_today_locked(self, comparison):
        """Φ̃_ΛCDM(z=0) ≈ 0.788 at k=10⁻³ Mpc⁻¹ (locked)."""
        v = comparison["phi_lcdm_today_low_ell"]
        assert abs(v - 0.788) < 0.020, f"Φ̃_ΛCDM = {v:.4f}, expected 0.788"

    def test_phi_ratio_locked(self, comparison):
        """Φ̃ ratio ≈ 2.64 (locked)."""
        r = comparison["phi_ratio_low_ell"]
        assert abs(r - 2.64) < 0.15, f"phi_ratio = {r:.3f}, expected 2.64"

    def test_isw_sign_grut(self, comparison):
        assert comparison["isw_sign_grut"] == "cooling"

    def test_isw_sign_lcdm(self, comparison):
        assert comparison["isw_sign_lcdm"] == "heating"

    def test_isw_amplitude_ratio_locked(self, comparison):
        """ISW amplitude ratio ≈ 5.09 (locked)."""
        r = comparison["isw_amplitude_ratio_low_ell"]
        assert abs(r - 5.09) < 0.60, f"ISW ratio = {r:.3f}, expected 5.09"

    def test_planck_consistent_true(self, comparison):
        """GRUT ISW direction (cooling/reduced power) is consistent with Planck anomaly."""
        assert comparison["planck_consistent"] is True

    def test_mu_at_recombination_locked(self, comparison):
        """μ_GRUT(k=10⁻³, z=1100) ≈ 1.0017 — SW unchanged (locked)."""
        mu = comparison["mu_at_recombination"]
        assert abs(mu - 1.0017) < 0.0005, f"μ(rec) = {mu:.5f}, expected 1.0017"

    def test_z_star_locked(self, comparison):
        """GRUT transition z★ ≈ 77 for k=10⁻³ Mpc⁻¹ (locked)."""
        z = comparison["z_star_low_ell"]
        assert abs(z - 76.8) < 5.0, f"z★ = {z:.1f}, expected ~77"

    def test_horizon_phi_ratio_locked(self, comparison):
        """Φ̃ ratio at horizon scale ≈ 3.06 (locked)."""
        r = comparison["phi_ratio_horizon"]
        assert abs(r - 3.06) < 0.25, f"horizon phi_ratio = {r:.3f}, expected 3.06"

    def test_isw_prediction_ell10_30_mentions_cooling(self, comparison):
        """ℓ=10–30 prediction string mentions 'cooling' or reduced power."""
        pred = comparison["isw_prediction_ell10_30"].lower()
        assert "cooling" in pred or "reduc" in pred

    def test_caching_returns_same_object(self, comparison):
        from grut.derived.cosmology.cmb_isw import cmb_isw_comparison
        c1 = cmb_isw_comparison()
        c2 = cmb_isw_comparison()
        assert c1 is c2, "Cache broken: different objects returned"

    def test_note_contains_key_numbers(self, comparison):
        note = comparison["note"]
        assert isinstance(note, str) and len(note) > 100
        assert "2.0" in note or "2.1" in note or "Φ̃" in note

    def test_tau0_c_correct(self, comparison):
        assert abs(comparison["tau0_c_mpc"] - 12.8475) < 0.1
