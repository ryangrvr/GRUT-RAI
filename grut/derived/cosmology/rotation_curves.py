"""
Galactic Rotation Curves via the GRUT engine (SPARC-ready).

PROVENANCE (v2 self-containment audit, June 2026)
─────────────────────────────────────────────────
This engine is **MOND-compatible**, not MOND-derived. Of the three pieces:

  • a_0 = cH_0/(2π)              — GRUT-DERIVED scale (from τ_Λ = 1/H_0); A_0_SI
  • gate 1/(1+X²), X = ω_dyn τ_0 — FORM GRUT-DERIVED from χ(ω) (single-pole
                                    relaxation kernel); controlling frequency
                                    ω_dyn = v/r ASSUMED — extrapolated from the
                                    cosmological DC χ, not yet CTP-derived for
                                    bound systems (see open discharge in
                                    theory/GRUT_V3_TEST_01_DARK_SECTOR.md)
  • ν(y) = ½ + √(¼ + 1/y)        — ADOPTED from MOND (the "simple" function),
                                    NOT derived. GRUT's bounded refractive
                                    enhancement (n_g² ≤ 4/3) provably cannot
                                    bend a flat curve; neither v2 nor V7 derives
                                    ν(y). See theory/PROJECTOR_CONSISTENCY_NOGO.md.

The engine mapping (ν(y) adopted; a_0 and the gate GRUT-derived):

    y = g_bar / a_0                           (dimensionless acceleration)
    ν(y) = 1/2 + √(1/4 + 1/y)                 (MOND simple function — ADOPTED)
    X = ω_dyn τ_0                             (regime gate — GRUT-derived)
    g_eff = g_bar × [1 + (ν(y) − 1) / (1 + X²)]

Limits:
    y ≫ 1  (high acceleration, Newtonian):  g_eff ≈ g_bar
    y ≪ 1  (deep-response):                 g_eff ≈ √(g_bar × a_0)
    X ≫ 1  (solar system, fast orbits):      g_eff → g_bar (GR recovered)
    X ≪ 1  (galactic, slow orbits):           g_eff → g_bar × ν(y)

GRUT's distinction from MOND: the DEEP-RESPONSE regime requires BOTH
  - low acceleration (y ≪ 1, same as MOND)
  - AND low frequency (X ≪ 1, NEW in GRUT)

This dual gate predicts deviations from MOND for systems that are
low-acceleration but high-frequency (e.g., certain wide binaries,
specific orbital phases). Phase I §8.1 documents this as a falsifiable
distinction.
"""

import numpy as np

from grut.foundation.closure_protocol import (
    ALPHA_VAC, TAU_0_SEC, A_0_SI,
    regime_parameter_X, alpha_effective, nu_interpolation, g_effective,
    n_g_refractive,
)
from grut.foundation.constants import G as G_NEWTON


# SI conversions
KM = 1000.0
KPC_IN_M = 3.086e19
MSUN_KG = 1.989e30


def v_circ_newtonian(M_enclosed_kg, r_m):
    """Newtonian circular velocity from enclosed mass."""
    return np.sqrt(G_NEWTON * M_enclosed_kg / r_m)


def g_bar_newtonian(M_enclosed_kg, r_m):
    """Newtonian (baryonic-only) gravitational acceleration."""
    return G_NEWTON * M_enclosed_kg / r_m**2


def v_circ_GRUT(M_bar_kg, r_m, omega_dyn_Hz=None):
    """Circular velocity under the GRUT engine.

    If ω_dyn is None, it is computed self-consistently from v_circ:
        ω_dyn = v_circ / r
    using v_circ from the Newtonian limit as an initial guess.

    Returns v_circ in m/s.
    """
    g_bar = g_bar_newtonian(M_bar_kg, r_m)
    if omega_dyn_Hz is None:
        # Self-consistent: start from Newtonian, one step of Picard iteration
        v_init = np.sqrt(g_bar * r_m)           # Newtonian
        omega_dyn_Hz = v_init / r_m

    g_eff = g_effective(g_bar, omega_dyn_Hz,
                        a_0=A_0_SI, tau_0_sec=TAU_0_SEC)
    return np.sqrt(g_eff * r_m)


def rotation_curve(M_bar_kg, r_array_m):
    """Generate a rotation curve v(r) under the GRUT engine.

    Returns dict with r, v_newton, v_GRUT, v_flat (asymptotic).
    """
    r = np.asarray(r_array_m)
    v_n = np.array([v_circ_newtonian(M_bar_kg, ri) for ri in r])
    v_g = np.array([v_circ_GRUT(M_bar_kg, ri) for ri in r])
    # Flat/deep asymptote: v⁴ = G M a_0
    v_flat = (G_NEWTON * M_bar_kg * A_0_SI) ** 0.25
    return {
        "r_m":          r,
        "r_kpc":        r / KPC_IN_M,
        "v_newton":     v_n,
        "v_GRUT":       v_g,
        "v_flat_asymp": v_flat,
        "M_bar_kg":     M_bar_kg,
        "M_bar_Msun":   M_bar_kg / MSUN_KG,
    }


def BTFR_coefficient_GRUT():
    """Baryonic Tully-Fisher relation: v_flat⁴ = G × M × a_0.

    In the deep-response limit, GRUT predicts the BTFR exactly with
    proportionality constant G × a_0. This is the same slope MOND
    predicts (because a_0 plays the same role), but GRUT DERIVES a_0
    from τ_Λ = H_0⁻¹ rather than fitting it.

    Returns G × a_0 in SI (m⁴ / (kg s⁴)), which equals v_flat⁴ / M.
    """
    return G_NEWTON * A_0_SI


def regime_diagnostic(M_bar_kg, r_m):
    """Report the regime parameters (y, X) and engine output at a radius.

    Useful for understanding where in the (y, X) plane a given galactic
    system sits.
    """
    g_bar = g_bar_newtonian(M_bar_kg, r_m)
    v_init = np.sqrt(g_bar * r_m)
    omega_dyn = v_init / r_m

    y = g_bar / A_0_SI
    X = regime_parameter_X(omega_dyn, tau_0_sec=TAU_0_SEC)
    nu = nu_interpolation(y)
    g_eff = g_effective(g_bar, omega_dyn)
    n_g = n_g_refractive(omega_dyn)

    return {
        "r_m":            r_m,
        "r_kpc":          r_m / KPC_IN_M,
        "M_bar_Msun":     M_bar_kg / MSUN_KG,
        "v_newton_km_s":  v_init / KM,
        "v_GRUT_km_s":    np.sqrt(g_eff * r_m) / KM,
        "g_bar_m_s2":     g_bar,
        "omega_dyn_Hz":   omega_dyn,
        "y_gbar_over_a0": y,
        "X_regime_gate":  X,
        "nu_interp":      float(nu),
        "n_g_refractive": float(n_g),
        "regime": _regime_label(y, X),
    }


def _regime_label(y, X):
    if X > 1e3:
        return "solar-system-like (GR recovered)"
    if y > 10 and X < 0.1:
        return "Newtonian galactic (inner region)"
    if y < 0.1 and X < 0.1:
        return "deep-response (asymptotic flat)"
    return "intermediate"


def phase_i_verify():
    """Run a canonical cross-check on the engine at a fiducial galaxy.

    Uses M_bar = 5×10¹⁰ M_sun (Milky Way-like) at r = 10 kpc:
        expected Newtonian v ≈ 146 km/s
        expected GRUT v     ≈ 163-200 km/s (depending on regime)
    """
    M = 5e10 * MSUN_KG
    r = 10 * KPC_IN_M
    return regime_diagnostic(M, r)


if __name__ == "__main__":
    import json
    d = phase_i_verify()
    print("Fiducial galaxy (5e10 M_sun, r = 10 kpc):")
    print(json.dumps(d, indent=2, default=str))
    print()
    # Scan across radii
    M = 5e10 * MSUN_KG
    radii = np.array([1, 3, 10, 30, 100]) * KPC_IN_M
    print("Radial scan:")
    for r in radii:
        d = regime_diagnostic(M, r)
        print(f"  r = {d['r_kpc']:5.1f} kpc  y = {d['y_gbar_over_a0']:.3e}  "
              f"X = {d['X_regime_gate']:.3e}  v_N = {d['v_newton_km_s']:5.1f}  "
              f"v_GRUT = {d['v_GRUT_km_s']:5.1f} km/s  [{d['regime']}]")
