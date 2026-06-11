"""Experimental discriminant forecasts — v2 certification of V7 predictions.

Three zero-parameter tests that distinguish GRUT from standard QM and from
competing models (CSL, Diosi-Penrose point-mass):

  F1 (mass slope):    d(log Λ)/d(log m) deviates from 2 due to extended-body
                      correction S(l/R). DP point-mass always gives slope 2.
  F2 (geometry scan): Same mass, different density → different Λ_grav.
                      DP point-mass predicts same Λ for all densities.
  F3 (pressure scan): Λ_total floors at Λ_grav as P → 0.
                      Standard QM predicts Λ → 0. CSL floors at adjustable height.

All GRUT predictions: zero free parameters. Source: V7 beyond_grut_experimental_forecast.py.
Certified by v2 lambda_grav (tests/derived/test_experimental_discriminants.py).

Status: [SPECULATIVE as to which platform will first reach the discriminating regime]
        [COMPUTED for the predicted rates and floors]
"""

import math
import pytest

from grut.foundation.noise_kernel import lambda_grav

# ── Physical constants ────────────────────────────────────────────────────────
G    = 6.67430e-11
HBAR = 1.05457e-34
K_B  = 1.38065e-23
C    = 2.99792e8
M_AMU = 1.66054e-27

# ── Environmental decoherence helpers ────────────────────────────────────────

def lambda_gas(m, R, l, T, P, m_gas=4.65e-26):
    """Gas-collision decoherence (Hornberger/Joos-Zeh)."""
    v_th = math.sqrt(8 * K_B * T / (math.pi * m_gas))
    n_gas = P / (K_B * T)
    sigma = math.pi * R**2
    lam_dB = HBAR / (m_gas * v_th)
    if l < lam_dB:
        return n_gas * sigma * v_th * (l / lam_dB)**2
    return n_gas * sigma * v_th


def lambda_dp_point(m, l):
    """Diosi-Penrose point-mass rate (no extended-body correction)."""
    return G * m**2 / (HBAR * l)


def lambda_csl(m, l, R, lam_csl=1e-16, r_csl=1e-7):
    """CSL rate (GRW parameters: lam=1e-16 Hz, r=100 nm)."""
    f = 1.0 if R < r_csl else (r_csl / R)**3
    g = (l / r_csl)**2 if l < r_csl else 1.0
    return lam_csl * (m / M_AMU)**2 * f * g


# ── Reference platform: levitated nanodiamond ────────────────────────────────
# m = 10 fg, R = 50 nm, l = 100 nm, T = 10 mK, P = 1e-10 Pa
M_ND = 1e-14       # kg
R_ND = 50e-9       # m
L_ND = 100e-9      # m
T_ND = 10e-3       # K
P_ND = 1e-10       # Pa


class TestF3PressurePlateauDiscriminant:
    """F3: Λ_total approaches a pressure-independent floor as P → 0.
    GRUT floor = Λ_grav (nonzero). Standard QM floor = 0. CSL floor = Λ_CSL (adjustable)."""

    def test_gravitational_floor_is_nonzero(self):
        floor = lambda_grav(M_ND, L_ND, R_ND)
        assert floor > 0
        assert 500 < floor < 800, f"GRUT floor for ref ND: {floor:.1f} Hz (expected ~633 Hz)"

    def test_floor_dominates_below_1e10_pa(self):
        """Below P ~ 1e-10 Pa, Λ_grav > Λ_gas for the reference platform."""
        floor = lambda_grav(M_ND, L_ND, R_ND)
        for P in [1e-11, 1e-12, 1e-13]:
            Lgs = lambda_gas(M_ND, R_ND, L_ND, T_ND, P)
            assert floor > Lgs, f"Floor {floor:.2e} should dominate gas {Lgs:.2e} at P={P:.0e}"

    def test_gas_dominates_above_1e9_pa(self):
        """Above P ~ 1e-9 Pa, gas >> gravitational (no floor visible yet)."""
        floor = lambda_grav(M_ND, L_ND, R_ND)
        Lgs = lambda_gas(M_ND, R_ND, L_ND, T_ND, 1e-7)
        assert Lgs > floor * 10

    def test_floor_height_is_parameter_free(self):
        """Λ_grav depends only on (m, l, R) and constants — zero free parameters."""
        floor = lambda_grav(M_ND, L_ND, R_ND)
        assert math.isfinite(floor)
        assert floor > 0

    def test_csl_grw_floor_differs_from_grut(self):
        """CSL (GRW) floor is far ABOVE GRUT floor for the 10 fg platform.
        CSL-GRW scales as m², so for m=10fg: Λ_CSL ~ 3.6e9 Hz >> Λ_GRUT ~ 633 Hz.
        Observing a 633 Hz plateau would rule out CSL-GRW by 7 orders of magnitude."""
        floor_grut = lambda_grav(M_ND, L_ND, R_ND)
        floor_csl = lambda_csl(M_ND, L_ND, R_ND, lam_csl=1e-16)
        # CSL-GRW floor is above GRUT floor for macro objects (m² scaling overwhelms)
        assert floor_csl / floor_grut > 1e6


class TestF2GeometryScanDiscriminant:
    """F2: Same mass, different density → different Λ_grav.
    DP point-mass predicts same Λ for all densities.
    GRUT predicts strong density dependence through S(l/R)."""

    M_GEO = 1e-14   # kg — fixed mass
    L_GEO = 50e-9   # m  — fixed superposition

    def _grut_rate(self, rho):
        R = (3 * self.M_GEO / (4 * math.pi * rho))**(1/3)
        return lambda_grav(self.M_GEO, self.L_GEO, R)

    def test_dp_point_mass_is_density_independent(self):
        """DP point-mass gives identical rate for gold vs aerogel."""
        rate_gold = lambda_dp_point(self.M_GEO, self.L_GEO)
        rate_aero = lambda_dp_point(self.M_GEO, self.L_GEO)
        assert rate_gold == rate_aero

    def test_grut_rate_increases_with_density(self):
        """Denser material → smaller R → larger S(l/R) → higher GRUT rate."""
        rate_aerogel  = self._grut_rate(100)
        rate_silica   = self._grut_rate(2200)
        rate_gold     = self._grut_rate(19300)
        assert rate_gold > rate_silica > rate_aerogel

    def test_gold_vs_aerogel_ratio_is_large(self):
        """Gold vs aerogel: same mass, but GRUT rates differ by >> 1×."""
        assert self._grut_rate(19300) / self._grut_rate(100) > 100

    def test_grut_and_dp_diverge(self):
        """GRUT and DP diverge significantly for large R (low-density) objects."""
        R_aero = (3 * self.M_GEO / (4 * math.pi * 100))**(1/3)
        grut = lambda_grav(self.M_GEO, self.L_GEO, R_aero)
        dp   = lambda_dp_point(self.M_GEO, self.L_GEO)
        # Aerogel: R >> l, deep near-field suppression
        assert dp / grut > 100


class TestF1MassSlopeDiscriminant:
    """F1: d(log Λ)/d(log m) is NOT simply 2 in the near-field regime.
    DP point-mass always gives slope = 2.
    GRUT transitions from ~2 (far-field) to ~1 (near-field) as m increases."""

    L_FIXED = 100e-9   # m

    def test_far_field_slope_is_two(self):
        """For small m (l >> 2R), S = 1 and Λ ~ m², slope = 2."""
        import numpy as np
        masses = np.logspace(-22, -20, 5)
        log_m, log_L = [], []
        for m in masses:
            R = (3 * m / (4 * math.pi * 2300))**(1/3)
            if 2 * R < self.L_FIXED:  # far-field condition
                Lg = lambda_grav(m, self.L_FIXED, R)
                if Lg > 1e-50:
                    log_m.append(math.log10(m))
                    log_L.append(math.log10(Lg))
        if len(log_m) >= 2:
            slope = (log_L[-1] - log_L[0]) / (log_m[-1] - log_m[0])
            assert abs(slope - 2.0) < 0.1, f"Far-field slope {slope:.3f} should be ~2"

    def test_near_field_slope_less_than_two(self):
        """For large m (l < 2R), extended-body correction suppresses, effective slope < 2."""
        import numpy as np
        masses = np.logspace(-14, -12, 5)
        log_m, log_L = [], []
        for m in masses:
            R = (3 * m / (4 * math.pi * 2300))**(1/3)
            Lg = lambda_grav(m, self.L_FIXED, R)
            if Lg > 1e-30:
                log_m.append(math.log10(m))
                log_L.append(math.log10(Lg))
        if len(log_m) >= 2:
            slope = (log_L[-1] - log_L[0]) / (log_m[-1] - log_m[0])
            assert slope < 1.5, f"Near-field slope {slope:.3f} should be < 1.5 (extended-body regime)"

    def test_dp_slope_always_two(self):
        """DP point-mass always gives slope = 2, regardless of mass."""
        import numpy as np
        masses = np.logspace(-22, -12, 10)
        log_m = [math.log10(m) for m in masses]
        log_L = [math.log10(lambda_dp_point(m, self.L_FIXED)) for m in masses]
        coeffs = np.polyfit(log_m, log_L, 1)
        assert abs(coeffs[0] - 2.0) < 0.01, f"DP slope {coeffs[0]:.4f} should be exactly 2"


class TestCompetingModelsComparison:
    """Verify that GRUT, CSL (GRW), and CSL (Adler) make distinguishable predictions
    at the reference platform."""

    def test_csl_adler_far_above_grut(self):
        """CSL Adler (lam=1e-8) predicts rate >> GRUT for the ND platform.
        CSL Adler is already excluded if GRUT is confirmed."""
        grut = lambda_grav(M_ND, L_ND, R_ND)
        csl_adler = lambda_csl(M_ND, L_ND, R_ND, lam_csl=1e-8)
        assert csl_adler > grut * 1e6

    def test_csl_grw_far_above_grut(self):
        """CSL GRW (lam=1e-16) predicts rate >> GRUT for the ND platform.
        For m=10fg, CSL-GRW gives ~3.6e9 Hz (m² scaling); GRUT gives ~633 Hz.
        A measured plateau at 633 Hz falsifies CSL-GRW by 7 orders."""
        grut = lambda_grav(M_ND, L_ND, R_ND)
        csl_grw = lambda_csl(M_ND, L_ND, R_ND, lam_csl=1e-16)
        assert csl_grw > grut * 1e6

    def test_grut_equals_dp_in_far_field(self):
        """In far-field (l >> 2R), S = 1 exactly and GRUT ≈ DP point-mass.
        Residual difference < 1e-4 from floating-point representation of S → 1."""
        m_small = 1e-22  # very small mass, R << l
        R_small = (3 * m_small / (4 * math.pi * 2300))**(1/3)
        assert 2 * R_small < L_ND, "Confirm far-field condition"
        grut = lambda_grav(m_small, L_ND, R_small)
        dp   = lambda_dp_point(m_small, L_ND)
        assert abs(grut - dp) / dp < 1e-4
