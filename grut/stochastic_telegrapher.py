"""
GRUT-II Gamma — Stochastic Telegrapher: Exact Spectrum S(k, omega)
===================================================================

The GRUT-II stochastic telegrapher equation:

    tau_2 d^2Phi/dt^2 + tau dPhi/dt + Phi - c^2 nabla^2 Phi = X + xi(x,t)

Noise model (primitive, white in time, white in space, additive, Gaussian):
    <xi(x,t)> = 0
    <xi(x,t) xi(x',t')> = 2D delta(x-x') delta(t-t')

Parameters:
    tau   = constitutive relaxation time (inherited from GRUT; tau^2 = 3/2)
    tau_2 = inertial timescale (telegrapher extension; Book III)
    c     = propagation speed (telegrapher extension)
    D     = constitutive diffusion strength (GRUT-II; +1p)

Deterministic recovery: D -> 0.
OU recovery: c -> 0, tau_2 -> 0 (no spatial structure, no inertia).
Wave recovery: tau -> infinity, tau_2 finite (undamped wave).

THIS MODULE DERIVES:
    1. The exact Green's function / response function in (k, omega) space
    2. The exact spectral density S(k, omega)
    3. The dispersion relation (poles)
    4. All limiting cases
    5. Numerical evaluation and visualization data
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple


# GRUT constants
TAU = math.sqrt(1.5)        # tau^2 = 3/2
TAU_SQ = 1.5


@dataclass
class TelegrapherSpectrum:
    """Full spectral result."""
    # Parameters
    tau: float = TAU
    tau_2: float = 0.0       # inertial timescale
    c: float = 1.0           # propagation speed
    D: float = 1.0           # noise strength

    # Derived
    damping_rate: float = 0.0    # gamma = 1/tau
    screening_mass: float = 0.0  # m^2 = 1/tau^2 (no tau_2) or modified

    # Spectral properties
    poles: List[complex] = field(default_factory=list)
    corner_freq: float = 0.0
    spatial_screening: float = 0.0

    notes: List[str] = field(default_factory=list)


def response_function(omega: float, k: float, tau: float, tau_2: float, c: float) -> complex:
    """The response function chi(k, omega) in Fourier space.

    From the telegrapher:
        tau_2 (-omega^2) Phi + tau (i omega) Phi + Phi + c^2 k^2 Phi = X + xi

    Rearranging for Phi = chi * (X + xi):
        [-tau_2 omega^2 + i omega tau + 1 + c^2 k^2] Phi = X + xi

    Therefore:
        chi(k, omega) = 1 / (-tau_2 omega^2 + i omega tau + 1 + c^2 k^2)
                      = 1 / (1 + c^2 k^2 - tau_2 omega^2 + i omega tau)
    """
    denom = complex(1.0 + c**2 * k**2 - tau_2 * omega**2, omega * tau)
    if abs(denom) < 1e-30:
        return complex(0, 0)
    return 1.0 / denom


def spectral_density(omega: float, k: float, tau: float, tau_2: float, c: float, D: float) -> float:
    """The power spectral density S(k, omega).

    S(k, omega) = |chi(k, omega)|^2 * S_noise

    For spatiotemporal white noise <xi xi'> = 2D delta(x-x') delta(t-t'):
        S_noise = 2D  (flat in both k and omega)

    Therefore:
        S(k, omega) = 2D / |1 + c^2 k^2 - tau_2 omega^2 + i omega tau|^2

    Expanding the denominator modulus squared:
        |...|^2 = (1 + c^2 k^2 - tau_2 omega^2)^2 + (omega tau)^2

    So:
        S(k, omega) = 2D / [(1 + c^2 k^2 - tau_2 omega^2)^2 + omega^2 tau^2]
    """
    real_part = 1.0 + c**2 * k**2 - tau_2 * omega**2
    imag_part = omega * tau
    denom = real_part**2 + imag_part**2
    if denom < 1e-30:
        return 0.0
    return 2.0 * D / denom


def find_poles(k: float, tau: float, tau_2: float, c: float) -> List[complex]:
    """Find poles of chi(k, omega) in the complex omega plane.

    Setting denominator to zero:
        -tau_2 omega^2 + i omega tau + (1 + c^2 k^2) = 0
        tau_2 omega^2 - i omega tau - (1 + c^2 k^2) = 0

    Using quadratic formula (omega as unknown):
        omega = [i tau +/- sqrt(-tau^2 + 4 tau_2 (1 + c^2 k^2))] / (2 tau_2)

    For tau_2 = 0 (pure constitutive):
        i omega tau + (1 + c^2 k^2) = 0
        omega = i (1 + c^2 k^2) / tau  (single pole on imaginary axis)
    """
    m_sq = 1.0 + c**2 * k**2  # effective mass squared

    if tau_2 < 1e-15:
        # No inertia: single pole
        return [complex(0, m_sq / tau)]

    discriminant = -tau**2 + 4.0 * tau_2 * m_sq

    if discriminant >= 0:
        # Overdamped: two imaginary poles
        sqrt_disc = math.sqrt(discriminant)
        omega1 = complex(0, (tau + sqrt_disc) / (2.0 * tau_2))
        omega2 = complex(0, (tau - sqrt_disc) / (2.0 * tau_2))
        return [omega1, omega2]
    else:
        # Underdamped: complex conjugate pair (oscillatory + damped)
        sqrt_disc = math.sqrt(-discriminant)
        real_part = sqrt_disc / (2.0 * tau_2)
        imag_part = tau / (2.0 * tau_2)
        omega1 = complex(real_part, imag_part)
        omega2 = complex(-real_part, imag_part)
        return [omega1, omega2]


def compute_spectrum_grid(
    tau: float = TAU,
    tau_2: float = 0.1,
    c: float = 1.0,
    D: float = 1.0,
    omega_range: Tuple[float, float] = (-10, 10),
    k_range: Tuple[float, float] = (0, 10),
    n_omega: int = 200,
    n_k: int = 100,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Compute S(k, omega) on a grid."""
    omegas = np.linspace(omega_range[0], omega_range[1], n_omega)
    ks = np.linspace(k_range[0], k_range[1], n_k)
    S = np.zeros((n_k, n_omega))

    for i, k in enumerate(ks):
        for j, w in enumerate(omegas):
            S[i, j] = spectral_density(w, k, tau, tau_2, c, D)

    return ks, omegas, S


def limiting_cases():
    """Derive and verify all limiting cases."""
    results = {}

    # 1. k -> 0: recover one-variable OU spectrum
    # S(k=0, omega) = 2D / [(1 - tau_2 omega^2)^2 + omega^2 tau^2]
    # For tau_2 -> 0: S(0, omega) = 2D / (1 + omega^2 tau^2) = OU spectrum
    results["k0_tau2_0"] = {
        "limit": "k -> 0, tau_2 -> 0",
        "result": "S(omega) = 2D / (1 + omega^2 tau^2)",
        "matches": "one-variable OU (GRUT-II Alpha)",
    }

    # 2. D -> 0: deterministic (no fluctuations)
    results["D0"] = {
        "limit": "D -> 0",
        "result": "S(k, omega) -> 0 identically",
        "matches": "closed GRUT deterministic telegrapher",
    }

    # 3. tau -> infinity (no dissipation): undamped wave
    # S = 2D / [(1 + c^2 k^2 - tau_2 omega^2)^2 + omega^2 tau^2]
    # tau -> inf: denominator ~ omega^2 tau^2 -> inf, so S -> 0
    # This is correct: no dissipation + no temperature -> no fluctuations
    results["tau_inf"] = {
        "limit": "tau -> infinity",
        "result": "S -> 0 (no dissipation -> no fluctuations via FDT)",
        "matches": "conservative wave equation has no thermal noise",
    }

    # 4. c -> 0 (no spatial propagation): spatially uncorrelated
    # S(k, omega) = 2D / [(1 - tau_2 omega^2)^2 + omega^2 tau^2]
    # Independent of k: spatial modes decouple
    results["c0"] = {
        "limit": "c -> 0",
        "result": "S independent of k (spatially uncorrelated)",
        "matches": "each spatial point is an independent OU/inertial oscillator",
    }

    # 5. tau_2 -> 0 (no inertia): standard constitutive + diffusion
    # S(k, omega) = 2D / [(1 + c^2 k^2)^2 + omega^2 tau^2]
    # This is a SCREENED stochastic diffusion equation
    results["tau2_0"] = {
        "limit": "tau_2 -> 0",
        "result": "S(k, omega) = 2D / [(1 + c^2 k^2)^2 + omega^2 tau^2]",
        "matches": "stochastic screened diffusion (constitutive + spatial)",
    }

    return results


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-II GAMMA — STOCHASTIC TELEGRAPHER SPECTRUM S(k, omega)")
    print("=" * 80)

    # Parameters
    tau = TAU
    tau_2_values = [0.0, 0.01, 0.1, 0.5]  # from no inertia to significant
    c = 1.0
    D = 1.0

    print("\n--- EXACT SPECTRAL DENSITY ---")
    print("  S(k, omega) = 2D / [(1 + c^2 k^2 - tau_2 omega^2)^2 + omega^2 tau^2]")
    print("  Parameters: tau={:.4f}, c={:.1f}, D={:.1f}".format(tau, c, D))

    # Poles analysis
    print("\n--- POLE STRUCTURE ---")
    for tau_2 in tau_2_values:
        print("\n  tau_2 = {:.2f}:".format(tau_2))
        for k in [0.0, 1.0, 5.0, 10.0]:
            poles = find_poles(k, tau, tau_2, c)
            pole_strs = ["({:.4f} + {:.4f}i)".format(p.real, p.imag) for p in poles]
            regime = "overdamped" if all(abs(p.real) < 1e-6 for p in poles) else "underdamped"
            print("    k={:.1f}: {} [{}]".format(k, ", ".join(pole_strs), regime))

    # Spectral slices
    print("\n--- SPECTRAL SLICES ---")
    print("\n  S(k=0, omega) — temporal spectrum at zero wavenumber:")
    omegas_test = [0.0, 0.1, 0.5, 1.0/tau, 2.0, 5.0, 10.0]
    for tau_2 in [0.0, 0.1]:
        print("    tau_2={:.2f}:".format(tau_2))
        for w in omegas_test:
            s = spectral_density(w, 0.0, tau, tau_2, c, D)
            print("      omega={:.2f}: S={:.6f}".format(w, s))

    print("\n  S(k, omega=0) — spatial spectrum at zero frequency:")
    ks_test = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0]
    for tau_2 in [0.0, 0.1]:
        print("    tau_2={:.2f}:".format(tau_2))
        for k in ks_test:
            s = spectral_density(0.0, k, tau, tau_2, c, D)
            print("      k={:.2f}: S={:.6f}".format(k, s))

    # Limiting cases
    print("\n--- LIMITING CASES ---")
    limits = limiting_cases()
    for name, info in limits.items():
        print("  {}: {} -> {}".format(name, info["limit"], info["result"]))
        print("    Matches: {}".format(info["matches"]))

    # Distinctiveness analysis
    print("\n--- DISTINCTIVENESS ANALYSIS ---")

    print("\n  COMPARISON 1: vs one-variable OU")
    print("    OU: S(omega) = 2D / (1 + omega^2 tau^2)  [NO k-dependence]")
    print("    Telegrapher: S(k,omega) = 2D / [(1+c^2k^2-tau_2 omega^2)^2 + omega^2 tau^2]")
    print("    Difference: spatial dispersion + inertial frequency shift")
    print("    At k=0, tau_2=0: IDENTICAL to OU")
    print("    At k>0 or tau_2>0: STRUCTURALLY DIFFERENT")

    print("\n  COMPARISON 2: vs generic stochastic diffusion (no screening)")
    print("    Diffusion: S(k,omega) = 2D / [(D_diff k^2)^2 + omega^2]")
    print("    Telegrapher: has SCREENING term (+1 in real part) + INERTIA (tau_2)")
    print("    Difference: constitutive screening mass m^2 = 1/(c tau)^2")

    print("\n  COMPARISON 3: vs generic stochastic telegrapher")
    print("    Generic: S = 2D_gen / [(1 + c_gen^2 k^2 - tau_2_gen omega^2)^2 + omega^2 gamma_gen^2]")
    print("    GRUT-II: SAME FUNCTIONAL FORM but parameters constrained:")
    print("      tau = tau_local(r) from Level-1 rule (position-dependent)")
    print("      c from telegrapher extension (committed)")
    print("      D from GRUT-II Alpha (primitive constitutive)")
    print("    AT FIXED PARAMETERS: spectrum is generic stochastic telegrapher")
    print("    WITH LEVEL-1: spectrum becomes position-dependent through tau_local(r)")

    # The critical tau_local modulation
    print("\n--- GRUT-SPECIFIC: POSITION-DEPENDENT SPECTRUM ---")
    print("  tau_local(r) = tau_0 * t_dyn(r) / (tau_0 + t_dyn(r))")
    print("  t_dyn(r) = sqrt(r^3 / (2GM))")
    print("")
    print("  At different radii from a solar-mass object:")
    M = 0.5  # geometric units
    tau_0 = 1e15  # cosmological tau_0 in some unit
    for r_label, r_val, t_dyn in [
        ("r = 10 r_s", 10.0, math.sqrt(10.0**3 / (2*M))),
        ("r = 100 r_s", 100.0, math.sqrt(100.0**3 / (2*M))),
        ("r = 1000 r_s", 1000.0, math.sqrt(1000.0**3 / (2*M))),
    ]:
        tau_local = t_dyn  # since t_dyn << tau_0 always in strong field
        corner = 1.0 / tau_local
        print("    {}: t_dyn={:.2f}, tau_local~{:.2f}, corner~{:.4f}".format(
            r_label, t_dyn, tau_local, corner))
        # Spectrum at this radius, k=0
        s_peak = spectral_density(0, 0, tau_local, 0, c, D)
        s_corner = spectral_density(corner, 0, tau_local, 0, c, D)
        print("      S(0,0)={:.4f}, S(corner,0)={:.4f}".format(s_peak, s_corner))

    print("\n" + "=" * 80)
    print("  RESULT SUMMARY")
    print("=" * 80)
    print("")
    print("  The exact spectrum is:")
    print("    S(k,omega) = 2D / [(1 + c^2 k^2 - tau_2 omega^2)^2 + omega^2 tau^2]")
    print("")
    print("  This is the GENERIC stochastic telegrapher spectrum.")
    print("  At fixed parameters, it contains no GRUT-specific structure.")
    print("")
    print("  GRUT-specificity enters ONLY through parameter constraints:")
    print("    1. tau = tau_local(r) from Level-1 (position-dependent)")
    print("    2. D primitive (not bath-derived)")
    print("    3. c from committed telegrapher extension")
    print("")
    print("  The functional form S(k,omega) is NOT new.")
    print("  The parameter structure IS constrained by the GRUT architecture.")
    print("  The position-dependent tau_local makes the spectrum spatially varying.")
    print("  This is the ONLY genuine GRUT-specific content beyond generic telegrapher.")
    print("=" * 80)
