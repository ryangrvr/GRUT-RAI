"""Tests for v9.0 thermal transition at T_c = 54.7 MK."""

import pytest


class TestThermalTransition:
    def test_T_c_is_54p7_MK(self):
        from grut.derived.cosmology.thermal_transition import T_C_MK
        assert abs(T_C_MK - 54.7) / 54.7 < 0.05

    def test_BBN_above_T_c(self):
        """BBN epoch (T ~ 10⁹ K) is above T_c, so no DM effects then."""
        from grut.derived.cosmology.thermal_transition import (
            T_BBN_K, T_C_KELVIN, in_memory_regime,
        )
        assert T_BBN_K > T_C_KELVIN
        assert not in_memory_regime(T_BBN_K)

    def test_recombination_below_T_c(self):
        """Recombination (T ~ 3000 K) is below T_c, DM effects active."""
        from grut.derived.cosmology.thermal_transition import (
            T_RECOMBINATION_K, in_memory_regime,
        )
        assert in_memory_regime(T_RECOMBINATION_K)

    def test_CMB_today_fully_in_memory_regime(self):
        from grut.derived.cosmology.thermal_transition import (
            T_CMB_TODAY_K, memory_activation_fraction,
        )
        f = memory_activation_fraction(T_CMB_TODAY_K)
        assert f > 0.99

    def test_BBN_fully_suppressed(self):
        from grut.derived.cosmology.thermal_transition import (
            T_BBN_K, memory_activation_fraction,
        )
        f = memory_activation_fraction(T_BBN_K)
        assert f < 0.01

    def test_activation_is_half_at_T_c(self):
        from grut.derived.cosmology.thermal_transition import (
            T_C_KELVIN, memory_activation_fraction,
        )
        assert abs(memory_activation_fraction(T_C_KELVIN) - 0.5) < 0.01

    def test_effective_n_g_with_thermal_zero_at_BBN(self):
        """At BBN T > T_c: n_g should be ~ 1 (no enhancement)."""
        from grut.derived.cosmology.thermal_transition import (
            T_BBN_K, effective_n_g_with_thermal,
        )
        ng = effective_n_g_with_thermal(0.0, T_BBN_K)
        assert abs(ng - 1.0) < 0.01

    def test_effective_n_g_with_thermal_full_at_CMB(self):
        """At CMB today: n_g full enhancement ~ 1.1547."""
        from grut.derived.cosmology.thermal_transition import (
            T_CMB_TODAY_K, effective_n_g_with_thermal,
        )
        import numpy as np
        ng = effective_n_g_with_thermal(0.0, T_CMB_TODAY_K)
        assert abs(ng - np.sqrt(4/3)) / np.sqrt(4/3) < 0.01

    def test_cosmological_chronology_returns_expected_epochs(self):
        from grut.derived.cosmology.thermal_transition import cosmological_chronology
        chron = cosmological_chronology()
        for epoch in ["plasma_era_BBN", "T_c_transition",
                       "recombination", "CMB_today"]:
            assert epoch in chron

    def test_verify_all_pass(self):
        from grut.derived.cosmology.thermal_transition import verify
        for name, passed in verify().items():
            assert passed, f"Thermal transition check failed: {name}"
