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

    def test_BBN_power_law_tail(self):
        """Derived finite-T MZ form has a 1/T tail: f(T_BBN) ≈ T_c/2T_BBN
        (small but nonzero), NOT the ad-hoc sigmoid's ~0."""
        from grut.derived.cosmology.thermal_transition import (
            T_BBN_K, T_C_KELVIN, memory_activation_fraction,
        )
        f = memory_activation_fraction(T_BBN_K)
        assert abs(f - T_C_KELVIN / (2 * T_BBN_K)) < 1e-3   # power-law asymptote
        assert 0.01 < f < 0.05                               # small but nonzero tail

    def test_activation_at_T_c_is_tanh_half(self):
        """Derived value at T_c is tanh(½)=0.4621, NOT the ad-hoc sigmoid's 0.5."""
        import math
        from grut.derived.cosmology.thermal_transition import (
            T_C_KELVIN, memory_activation_fraction,
        )
        assert abs(memory_activation_fraction(T_C_KELVIN) - math.tanh(0.5)) < 1e-9

    def test_bbn_effect_bandwidth_protected(self):
        """At BBN the memory EFFECT on dynamical (sub-horizon, ωτ_0≫1) modes is
        bandwidth-suppressed → n_g ≈ 1 despite the ~2.7% f(T) tail; the DC/
        super-horizon residual is small (~0.5%) and does not affect local BBN."""
        from grut.derived.cosmology.thermal_transition import (
            T_BBN_K, effective_n_g_with_thermal,
        )
        ng_dyn = effective_n_g_with_thermal(1.0, T_BBN_K)    # ω=1 Hz, ωτ_0≫1
        assert abs(ng_dyn - 1.0) < 1e-12                      # bandwidth-protected
        ng_dc = effective_n_g_with_thermal(0.0, T_BBN_K)     # DC / super-horizon
        assert abs(ng_dc - 1.0) < 0.01                        # small residual only

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

    def test_derived_form_is_tanh(self):
        """f(T) = tanh(T_c/2T) exactly (no free width parameter)."""
        import math
        from grut.foundation.closure_protocol import T_C_KELVIN
        from grut.derived.cosmology.thermal_transition import memory_activation_fraction
        for T in (1e3, 1e6, T_C_KELVIN, 1e8, 1e10):
            assert abs(memory_activation_fraction(T) - math.tanh(T_C_KELVIN / (2 * T))) < 1e-12

    def test_fdt_coherence_fraction(self):
        """f = 1/coth(T_c/2T): the zero-point (coherent) fraction of the bath
        fluctuation at the micro scale — the FDT/KMS provenance."""
        import math
        from grut.foundation.closure_protocol import T_C_KELVIN
        from grut.derived.cosmology.thermal_transition import memory_activation_fraction
        for T in (1e6, T_C_KELVIN, 1e9):
            x = T_C_KELVIN / (2 * T)
            assert abs(memory_activation_fraction(T) - math.tanh(x)) < 1e-12  # =1/coth(x)

    def test_monotonic_decreasing_in_T(self):
        from grut.derived.cosmology.thermal_transition import memory_activation_fraction
        # non-increasing everywhere (saturates to 1.0 for T ≪ T_c)
        Ts_all = [1e4, 1e6, 1e7, 1e8, 1e9, 1e10]
        fs_all = [memory_activation_fraction(T) for T in Ts_all]
        assert all(fs_all[i] >= fs_all[i + 1] for i in range(len(fs_all) - 1))
        # strictly decreasing in the active regime (T ≳ T_c)
        Ts = [3e7, 5e7, 1e8, 1e9, 1e10]
        fs = [memory_activation_fraction(T) for T in Ts]
        assert all(fs[i] > fs[i + 1] for i in range(len(fs) - 1))
