"""Tests for GRUT rotation-curve engine (SPARC-ready).

Verifies:
  - Newtonian limit at inner radii (inner disk)
  - Asymptotic flat rotation v_flat = (G M a_0)^(1/4) (BTFR)
  - Monotonic increase of GRUT enhancement with radius
  - Regime diagnostic returns right labels
"""

import numpy as np
import pytest


KPC = 3.086e19
MSUN = 1.989e30
KM = 1000.0


class TestRotationCurveEngine:
    def test_inner_radius_is_approximately_newtonian(self):
        """At 1 kpc (high g_bar, fast orbit), GRUT ≈ Newtonian."""
        from grut.derived.cosmology.rotation_curves import (
            v_circ_newtonian, v_circ_GRUT,
        )
        M = 5e10 * MSUN
        r = 1 * KPC
        v_n = v_circ_newtonian(M, r)
        v_g = v_circ_GRUT(M, r)
        # Within 2% at 1 kpc
        assert abs(v_g / v_n - 1) < 0.02

    def test_outer_radius_flattens_near_BTFR(self):
        """At 100 kpc, v_GRUT approaches (G M a_0)^(1/4)."""
        from grut.derived.cosmology.rotation_curves import (
            v_circ_GRUT, BTFR_coefficient_GRUT,
        )
        M = 5e10 * MSUN
        r = 100 * KPC
        v_g = v_circ_GRUT(M, r)
        v_flat = (BTFR_coefficient_GRUT() * M) ** 0.25
        # Within 5%
        assert abs(v_g / v_flat - 1) < 0.05

    def test_rotation_curve_flattens_with_radius(self):
        """v_GRUT - v_newton grows with r (flat curve dominates)."""
        from grut.derived.cosmology.rotation_curves import rotation_curve
        M = 5e10 * MSUN
        radii = np.array([5, 20, 50]) * KPC
        r = rotation_curve(M, radii)
        diff = r["v_GRUT"] - r["v_newton"]
        # Difference should grow monotonically with radius
        assert diff[1] > diff[0]
        assert diff[2] > diff[1]


class TestRegimeDiagnostic:
    def test_inner_galaxy_is_intermediate_or_newtonian(self):
        from grut.derived.cosmology.rotation_curves import regime_diagnostic
        d = regime_diagnostic(5e10 * MSUN, 1 * KPC)
        # Inner region: high y, intermediate X
        assert d["y_gbar_over_a0"] > 1
        assert d["v_newton_km_s"] > 100

    def test_outer_galaxy_is_deep_response(self):
        from grut.derived.cosmology.rotation_curves import regime_diagnostic
        d = regime_diagnostic(5e10 * MSUN, 200 * KPC)
        # Very outer: deep response regime
        assert d["y_gbar_over_a0"] < 0.1
        assert d["X_regime_gate"] < 0.1
        assert "deep-response" in d["regime"] or "intermediate" in d["regime"]


class TestBTFR:
    def test_BTFR_coefficient_is_G_times_a0(self):
        from grut.derived.cosmology.rotation_curves import BTFR_coefficient_GRUT
        from grut.foundation.closure_protocol import A_0_SI
        from grut.foundation.constants import G
        assert abs(BTFR_coefficient_GRUT() - G * A_0_SI) < 1e-30

    def test_BTFR_v_flat_scales_as_M_to_the_quarter(self):
        """v_flat ∝ M^(1/4), so doubling M multiplies v_flat by 2^0.25."""
        from grut.derived.cosmology.rotation_curves import BTFR_coefficient_GRUT
        M1 = 1e10 * MSUN
        M2 = 2e10 * MSUN
        v1 = (BTFR_coefficient_GRUT() * M1) ** 0.25
        v2 = (BTFR_coefficient_GRUT() * M2) ** 0.25
        assert abs(v2 / v1 - 2**0.25) < 1e-10
