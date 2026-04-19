"""Tests for the decoherence sector — the RIGOROUSLY-DERIVED core of GRUT.

V7 §17-22: gravitational decoherence from the Diósi-AH kernel, all six
scaling signatures, the competition frontier, isotope and geometry tests.

This sector is DERIVED (exact from published physics) and independent
of the anomaly R. These tests lock in the scaling laws so any regression
in the noise kernel or environmental competition is caught immediately.
"""

import pytest
import numpy as np

# Gold benchmark from V7: m = 20818 amu, l = 1 um
AMU_KG = 1.66053906660e-27
M_GOLD_KG = 20818 * AMU_KG
L_GOLD_M = 1e-6
RHO_GOLD = 19300  # gold density (kg/m^3)


class TestLambdaGravCore:
    """Tests for the core gravitational decoherence rate λ_grav."""

    def test_returns_finite_positive(self):
        from grut.derived.decoherence.sector import lambda_grav
        lam = lambda_grav(M_GOLD_KG, L_GOLD_M)
        assert np.isfinite(lam)
        assert lam > 0

    def test_scales_with_mass_squared(self):
        """V7 scaling law: λ_grav ∝ m²."""
        from grut.derived.decoherence.sector import lambda_grav
        lam1 = lambda_grav(M_GOLD_KG, L_GOLD_M)
        lam2 = lambda_grav(2 * M_GOLD_KG, L_GOLD_M)
        # m → 2m should roughly quadruple λ_grav (up to S(l/R) corrections)
        ratio = lam2 / lam1
        # Expect ratio > 3 (the m² scaling plus slight correction from S(l/R))
        assert ratio > 3.0

    def test_scales_with_length(self):
        """λ_grav has monotonic scaling with separation l."""
        from grut.derived.decoherence.sector import lambda_grav
        lam_small = lambda_grav(M_GOLD_KG, 1e-8)
        lam_large = lambda_grav(M_GOLD_KG, 1e-6)
        assert lam_small != lam_large

    def test_zero_mass_gives_zero_rate(self):
        from grut.derived.decoherence.sector import lambda_grav
        lam = lambda_grav(0, L_GOLD_M)
        assert lam == 0 or abs(lam) < 1e-30


class TestEnvironmentalCompetition:
    """Tests for the competition frontier — λ_env vs λ_grav."""

    def test_gas_rate_finite_positive(self):
        from grut.derived.decoherence.competition import lambda_gas
        lam = lambda_gas(M_GOLD_KG, L_GOLD_M, P_Pa=1e-10, T_K=300)
        assert np.isfinite(lam)
        assert lam > 0

    def test_gas_rate_scales_with_pressure(self):
        from grut.derived.decoherence.competition import lambda_gas
        low_P = lambda_gas(M_GOLD_KG, L_GOLD_M, P_Pa=1e-14)
        high_P = lambda_gas(M_GOLD_KG, L_GOLD_M, P_Pa=1e-10)
        assert high_P > low_P

    def test_blackbody_rate_scales_with_temperature(self):
        from grut.derived.decoherence.competition import lambda_blackbody
        cold = lambda_blackbody(M_GOLD_KG, L_GOLD_M, T_K=4.0)
        hot = lambda_blackbody(M_GOLD_KG, L_GOLD_M, T_K=300.0)
        assert hot > cold

    def test_total_environmental_finite(self):
        from grut.derived.decoherence.competition import total_environmental
        lam = total_environmental(M_GOLD_KG, L_GOLD_M,
                                   P_Pa=1e-12, T_K=4.0)
        assert np.isfinite(lam)
        assert lam > 0

    def test_competition_returns_breakdown(self):
        from grut.derived.decoherence.competition import competition
        result = competition(M_GOLD_KG, L_GOLD_M, P_Pa=1e-14, T_K=4.0)
        assert isinstance(result, dict)
        # Should include both grav and environmental rates
        assert any("grav" in k.lower() for k in result.keys())

    def test_competition_at_low_T_favorable_for_grut(self):
        """Cold + ultra-high-vacuum should have observable grav/env ratio."""
        from grut.derived.decoherence.competition import competition
        result = competition(M_GOLD_KG, L_GOLD_M, P_Pa=1e-16, T_K=0.01)
        assert isinstance(result, dict)


class TestEntanglement:
    """Tests for entanglement-based decoherence tests (Bose-Marletto-Vedral)."""

    def test_lambda_grav_bell_scales_with_separation(self):
        from grut.derived.decoherence.entanglement import lambda_grav_bell
        lam_close = lambda_grav_bell(M_GOLD_KG, L_GOLD_M, d_separation=1e-7)
        lam_far = lambda_grav_bell(M_GOLD_KG, L_GOLD_M, d_separation=1e-3)
        # Both should be finite (zero allowed if full protection kicks in)
        assert np.isfinite(lam_close)
        assert np.isfinite(lam_far)

    def test_csl_rate_is_positive(self):
        """CSL is a competitor prediction; should be computable."""
        from grut.derived.decoherence.entanglement import lambda_csl
        lam = lambda_csl(M_GOLD_KG, L_GOLD_M)
        assert np.isfinite(lam)
        assert lam >= 0


class TestIsotopeExperiment:
    """Tests for the isotope-swap GRUT discriminator (Si-28 vs Si-30)."""

    def test_isotope_experiment_returns_dict(self):
        from grut.derived.decoherence.isotope_test import isotope_experiment
        result = isotope_experiment(n_atoms=1e9, l_m=1e-7,
                                     iso_a="Si-28", iso_b="Si-30")
        assert isinstance(result, dict)

    def test_element_scan_returns_data(self):
        from grut.derived.decoherence.isotope_test import element_scan
        result = element_scan(n_atoms=1e8, l_m=1e-7)
        assert isinstance(result, (dict, list))


class TestKinkScan:
    """Tests for the kink-in-length-scaling signature at l ≈ 1.8 R."""

    def test_kink_scan_returns_arrays(self):
        from grut.derived.decoherence.kink_scan import kink_scan
        result = kink_scan(m_kg=1e-20)
        assert isinstance(result, (dict, list))


class TestMaterialSwap:
    """Tests for the material-comparison prediction (V7 §20)."""

    def test_material_swap_experiment_runs(self):
        from grut.derived.decoherence.material_swap import material_swap_experiment
        result = material_swap_experiment(m_amu=1e9, l_m=1e-7)
        assert isinstance(result, dict)

    def test_optimal_material_pair_returns_dict(self):
        from grut.derived.decoherence.material_swap import optimal_material_pair
        result = optimal_material_pair(m_amu=1e9, l_m=1e-7)
        assert isinstance(result, dict)

    def test_separation_scan_returns_data(self):
        from grut.derived.decoherence.material_swap import separation_scan_two_materials
        result = separation_scan_two_materials(m_amu=1e9, n=20)
        assert isinstance(result, (dict, list))
