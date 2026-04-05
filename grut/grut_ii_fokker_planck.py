"""
GRUT-II Alpha — Exact Fokker-Planck Derivation, Stationary Measure, and Spectral Signature
=============================================================================================

The stochastic constitutive equation:

    tau * dPhi/dt + Phi = X + xi(t)

where xi(t) is Gaussian white noise with:

    <xi(t)> = 0
    <xi(t) xi(t')> = 2D delta(t - t')

D is the single new parameter (diffusion coefficient / noise strength).
GRUT is the D -> 0 limit.

THIS MODULE DERIVES (not assumes):
  1. The Fokker-Planck equation for P(Phi, t)
  2. The stationary measure P_ss(Phi)
  3. The power spectral density S(omega)
  4. The fluctuation-dissipation relation
  5. The variance, autocorrelation, and all moments

All derivations are exact for the linear Langevin equation.
No approximations. No handwaving.
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List


# ================================================================
# Constants
# ================================================================

TAU = math.sqrt(1.5)      # GRUT canonical: tau^2 = 3/2
TAU_SQ = 1.5


# ================================================================
# DERIVATION 1: Fokker-Planck Equation
# ================================================================

def derive_fokker_planck():
    """
    DERIVATION (exact, no approximation):

    Start from the Langevin equation:

        tau dPhi/dt + Phi = X + xi(t)

    Rewrite as:

        dPhi/dt = -(1/tau)(Phi - X) + (1/tau) xi(t)

    This is a standard Ornstein-Uhlenbeck process with:
        drift:     a(Phi) = -(1/tau)(Phi - X)
        diffusion: b = 1/tau  (multiplies the noise)

    The noise has correlator:
        <xi(t) xi(t')> = 2D delta(t - t')

    So the effective diffusion in the Ito SDE is:
        dPhi = a(Phi) dt + b dW(t)

    where dW is a Wiener process with <dW^2> = dt, and
        b^2 * (noise_strength) = (1/tau)^2 * 2D * (1/2) ...

    More carefully: the SDE in standard form is:

        dPhi = -(1/tau)(Phi - X) dt + sqrt(2D)/tau dW(t)

    because xi(t) dt = sqrt(2D) dW(t), and the 1/tau prefactor gives
    the diffusion coefficient:

        D_eff = (1/2) * (sqrt(2D)/tau)^2 = D/tau^2

    The Fokker-Planck equation for P(Phi, t) is:

        dP/dt = -d/dPhi [a(Phi) P] + D_eff d^2P/dPhi^2

    Substituting a(Phi) = -(1/tau)(Phi - X) and D_eff = D/tau^2:

        dP/dt = (1/tau) d/dPhi [(Phi - X) P] + (D/tau^2) d^2P/dPhi^2

    Multiply through by tau:

        tau dP/dt = d/dPhi [(Phi - X) P] + (D/tau) d^2P/dPhi^2

    Or equivalently (the form requested):

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   dP/dt = (1/tau) d/dPhi [(Phi - X) P] + (D/tau^2) d^2P/dPhi^2  │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    This is EXACT. No approximation was made. The derivation uses only:
      (i)   the Langevin equation (the postulate)
      (ii)  Gaussian white noise (the noise model)
      (iii) the Ito calculus correspondence dW^2 = dt

    GRUT limit: D -> 0 gives dP/dt = (1/tau) d/dPhi[(Phi-X)P],
    whose solution is P -> delta(Phi - X(t)) (deterministic trajectory).
    """
    return {
        "equation": "dP/dt = (1/tau) d_Phi[(Phi - X) P] + (D/tau^2) d^2_Phi P",
        "drift": "a(Phi) = -(1/tau)(Phi - X)",
        "diffusion_coefficient": "D_eff = D / tau^2",
        "noise_model": "<xi(t) xi(t')> = 2D delta(t-t')",
        "grut_limit": "D -> 0: P -> delta(Phi - X)",
        "derivation_status": "EXACT (Ito calculus; no approximation)",
    }


# ================================================================
# DERIVATION 2: Stationary Measure
# ================================================================

def derive_stationary_measure():
    """
    DERIVATION (exact):

    At stationarity, dP/dt = 0. The Fokker-Planck becomes:

        0 = (1/tau) d/dPhi [(Phi - X) P] + (D/tau^2) d^2P/dPhi^2

    This is a second-order ODE for P_ss(Phi). For the OU process,
    the stationary solution satisfies detailed balance:

        J = -(1/tau)(Phi - X) P_ss - (D/tau^2) dP_ss/dPhi = 0

    (The probability current J vanishes at stationarity for a confining potential.)

    Solving:

        dP_ss/dPhi = -(tau/D)(Phi - X) P_ss

    This is separable:

        dP_ss / P_ss = -(tau/D)(Phi - X) dPhi

    Integrating:

        ln P_ss = -(tau/D) * (Phi - X)^2 / 2 + const

    Therefore:

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   P_ss(Phi) = (1/sqrt(2 pi sigma^2)) exp[-(Phi-X)^2 / (2 sigma^2)]  │
    │                                                             │
    │   where sigma^2 = D*tau  (= D/gamma, gamma = 1/tau)        │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    Wait — let me be precise about the sigma.

    From dP/dPhi = -(tau/D)(Phi-X) P, the exponent is -(tau/(2D))(Phi-X)^2.
    So the variance is:

        <(Phi - X)^2> = D / tau    ... NO. Let me redo.

    The exponent is -(tau/D)(Phi-X)^2/2 = -(Phi-X)^2 / (2 D/tau).

    Comparing with Gaussian exp[-(Phi-X)^2/(2 sigma^2)]:

        sigma^2 = D / tau

    CHECK via equipartition: The potential is V(Phi) = (1/(2tau))(Phi-X)^2.
    The OU process has <(Phi-X)^2> = D_eff / gamma where gamma = 1/tau
    and D_eff = D/tau^2.

        <(Phi-X)^2> = (D/tau^2) / (1/tau) = D/tau.  CONSISTENT.

    So:

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   P_ss(Phi) = sqrt(tau / (2 pi D)) * exp[-(Phi-X)^2 tau / (2D)]  │
    │                                                             │
    │   Variance: sigma^2 = D / tau                               │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    This is the DERIVED probability measure. Not assumed. Not postulated.
    It follows from the Langevin equation + noise model.

    GRUT limit: D -> 0 gives sigma -> 0, P_ss -> delta(Phi - X).
    Deterministic equilibrium recovered.

    PHYSICAL CONTENT: The width of the distribution is sqrt(D/tau).
    Larger D -> wider fluctuations. Larger tau -> narrower (stronger damping
    concentrates the distribution). The measure is Gaussian, centered at X.
    """
    return {
        "stationary_measure": "P_ss(Phi) = sqrt(tau/(2piD)) exp[-(Phi-X)^2 tau/(2D)]",
        "variance": "sigma^2 = D / tau",
        "mean": "<Phi> = X",
        "normalization": "sqrt(tau / (2 pi D))",
        "grut_limit": "D -> 0: sigma -> 0, P_ss -> delta(Phi - X)",
        "derivation_status": "EXACT (detailed balance; no approximation)",
    }


# ================================================================
# DERIVATION 3: Power Spectral Density
# ================================================================

def derive_power_spectrum():
    """
    DERIVATION (exact):

    The Langevin equation in frequency domain:

        tau dPhi/dt + Phi = X + xi(t)

    Take Fourier transform (Phi(t) = integral Phi_hat(omega) exp(i omega t) domega):

        (i omega tau + 1) Phi_hat(omega) = X_hat(omega) + xi_hat(omega)

    For the FLUCTUATION part (subtract the mean response to X):

        delta_Phi_hat(omega) = xi_hat(omega) / (1 + i omega tau)

    The transfer function (susceptibility):

        chi(omega) = 1 / (1 + i omega tau)

    The noise spectral density:

        S_xi(omega) = 2D    (white noise: flat spectrum)

    The output power spectrum (Wiener-Khinchin):

        S_Phi(omega) = |chi(omega)|^2 * S_xi(omega)
                     = [1 / (1 + omega^2 tau^2)] * 2D

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   S(omega) = 2D / (1 + omega^2 tau^2)                      │
    │                                                             │
    │   Corner frequency: omega_c = 1/tau                         │
    │   Zero-frequency: S(0) = 2D                                 │
    │   High-frequency: S(omega >> 1/tau) ~ 2D/(omega^2 tau^2)   │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    WAIT: the user specified S(omega) = 2D*tau / (1 + omega^2 tau^2).
    Let me check.

    The discrepancy is a convention on how the noise enters.

    In the form: dPhi/dt = -(1/tau)(Phi-X) + (1/tau) xi(t)
    with <xi xi'> = 2D delta:

    Phi_hat = xi_hat / [tau(i omega + 1/tau)]
    |Phi_hat|^2 = S_xi / [tau^2(omega^2 + 1/tau^2)]
                = 2D / [tau^2 omega^2 + 1]

    Hmm, that gives S = 2D / (1 + tau^2 omega^2). Same thing.

    Now check: integral S domega/(2pi) should equal the variance D/tau.

        integral_{-inf}^{inf} 2D / (1 + tau^2 omega^2) domega / (2pi)
        = (2D / (2pi)) * (pi / tau)
        = D / tau.  CHECK. Consistent with sigma^2 = D/tau.

    The user's form S = 2D*tau / (1 + omega^2 tau^2) differs by a factor tau.
    This depends on the convention for where tau enters. Let me use the form
    that gives the correct variance:

        integral S domega/(2pi) = sigma^2 = D/tau

    With S = 2D/(1 + omega^2 tau^2):
        integral = 2D * pi/(tau) / (2pi) = D/tau. YES.

    With S = 2D*tau/(1 + omega^2 tau^2):
        integral = 2D*tau * pi/(tau) / (2pi) = D. NO (this gives variance = D, not D/tau).

    The correct form (consistent with the Langevin and stationary measure) is:

        S(omega) = 2D / (1 + omega^2 tau^2)

    The factor-of-tau difference comes from how xi enters. In our convention
    (xi multiplied by 1/tau in the drift equation), S = 2D/(1+omega^2 tau^2).

    ALTERNATIVELY, if the Langevin is written as:
        tau dPhi/dt + Phi = X + eta(t) with <eta eta'> = 2D*tau delta
    then S = 2D*tau/(1 + omega^2 tau^2) and sigma^2 = D.

    Both conventions are self-consistent. I will use the first (the one that
    matches the postulate <xi xi'> = 2D delta and gives sigma^2 = D/tau).
    """
    return {
        "power_spectrum": "S(omega) = 2D / (1 + omega^2 tau^2)",
        "corner_frequency": "omega_c = 1/tau",
        "zero_frequency": "S(0) = 2D",
        "high_frequency": "S(omega >> 1/tau) ~ 2D / (omega tau)^2",
        "total_variance": "integral S domega/(2pi) = D/tau = sigma^2",
        "lorentzian_shape": True,
        "grut_limit": "D -> 0: S(omega) -> 0 identically (XVIII Alpha recovered)",
        "derivation_status": "EXACT (Fourier transform + Wiener-Khinchin; no approximation)",
    }


# ================================================================
# DERIVATION 4: Fluctuation-Dissipation Relation
# ================================================================

def derive_fdt():
    """
    DERIVATION (exact):

    The fluctuation-dissipation theorem (FDT) relates the response function
    to the noise spectrum. For the OU process:

    Response function (susceptibility):
        chi(omega) = 1 / (1 + i omega tau)

    Imaginary part:
        Im[chi(omega)] = -omega tau / (1 + omega^2 tau^2)

    Dissipation spectrum:
        chi''(omega) = Im[chi(omega)] = -omega tau / (1 + omega^2 tau^2)

    FDT (classical):
        S(omega) = -2 k_B T * Im[chi(omega)] / omega

    If we identify:
        S(omega) = 2D / (1 + omega^2 tau^2)

    Then:
        2D / (1 + omega^2 tau^2) = -2 k_B T * [-omega tau / (1 + omega^2 tau^2)] / omega
                                  = 2 k_B T tau / (1 + omega^2 tau^2)

    Therefore:

    ┌─────────────────────────────────────────────────────────────┐
    │                                                             │
    │   D = k_B T tau                                             │
    │                                                             │
    │   The noise strength D is related to temperature T          │
    │   and dissipation rate 1/tau via the classical FDT.         │
    │                                                             │
    │   Equivalently: k_B T = D / tau = sigma^2                   │
    │   (equipartition: (1/2) k_B T per DOF)                     │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘

    WAIT: let me be more careful. The susceptibility for
    dPhi/dt = -(1/tau)(Phi-X) + noise is:

        chi(omega) = (1/tau) / (i omega + 1/tau) = 1 / (1 + i omega tau)

    Im chi = -omega tau / (1 + omega^2 tau^2).

    FDT: S(omega) = (2 k_B T / omega) |Im chi(omega)|
                   = (2 k_B T / omega) * omega tau / (1 + omega^2 tau^2)
                   = 2 k_B T tau / (1 + omega^2 tau^2)

    So S = 2 k_B T tau / (1 + omega^2 tau^2), which means:

        D = k_B T tau    and    sigma^2 = D/tau = k_B T.

    OR: in our convention S = 2D/(1+omega^2 tau^2), matching gives D = k_B T tau.

    Let me just be explicit. With the Langevin:
        tau dPhi/dt + Phi = X + xi,  <xi xi'> = 2D delta

    Dividing by tau:
        dPhi/dt = -(Phi-X)/tau + xi/tau,  effective noise = xi/tau,
        effective noise correlator = (2D/tau^2) delta

    Standard OU: dPhi/dt = -gamma Phi + sigma_noise dW/dt
    with gamma = 1/tau, sigma_noise^2 = 2D/tau^2.

    FDT for standard OU at temperature T:
        sigma_noise^2 = 2 gamma k_B T
        => 2D/tau^2 = 2(1/tau) k_B T
        => D/tau = k_B T
        => D = k_B T tau

    All consistent. The FDT is:

        D = k_B T * tau

    and the variance is:

        sigma^2 = D/tau = k_B T

    This is the standard equipartition result for one degree of freedom.
    """
    return {
        "fdt": "D = k_B T * tau",
        "temperature_from_D": "k_B T = D / tau = sigma^2",
        "equipartition": "<(Phi - X)^2> = k_B T  (one DOF)",
        "physical_meaning": "If D and tau are known, temperature is determined",
        "grut_limit": "D -> 0 implies T -> 0 (zero-temperature deterministic limit)",
        "derivation_status": "EXACT (standard FDT for Ornstein-Uhlenbeck)",
    }


# ================================================================
# DERIVATION 5: Autocorrelation and All Moments
# ================================================================

def derive_autocorrelation():
    """
    DERIVATION (exact):

    Autocorrelation function of the fluctuations delta_Phi = Phi - X:

        C(t) = <delta_Phi(t) delta_Phi(0)> = sigma^2 exp(-|t|/tau)
             = (D/tau) exp(-|t|/tau)

    This is the inverse Fourier transform of S(omega) = 2D/(1+omega^2 tau^2).

    All moments of the stationary Gaussian:
        <(Phi - X)^{2n}> = (2n-1)!! * sigma^{2n} = (2n-1)!! * (D/tau)^n
        <(Phi - X)^{2n+1}> = 0  (symmetric)

    Kurtosis: <(Phi-X)^4> / <(Phi-X)^2>^2 = 3 (Gaussian).
    """
    return {
        "autocorrelation": "C(t) = (D/tau) exp(-|t|/tau)",
        "correlation_time": "tau_corr = tau",
        "variance": "sigma^2 = D/tau",
        "all_even_moments": "<(Phi-X)^{2n}> = (2n-1)!! (D/tau)^n",
        "all_odd_moments": "0 (Gaussian symmetry)",
        "kurtosis": "3 (Gaussian)",
        "derivation_status": "EXACT (Ornstein-Uhlenbeck; Gaussian process)",
    }


# ================================================================
# NUMERICAL VERIFICATION
# ================================================================

def numerical_verification(
    D: float = 1.0,
    tau: float = TAU,
    X: float = 5.0,
    dt: float = 0.001,
    n_steps: int = 1000000,
    seed: int = 42,
) -> dict:
    """Numerically simulate the Langevin equation and verify all derived quantities."""
    rng = np.random.default_rng(seed)

    gamma = 1.0 / tau
    sigma_noise = math.sqrt(2 * D) / tau  # effective noise amplitude in dPhi/dt form

    # Euler-Maruyama integration
    Phi = X  # start at equilibrium
    trajectory = np.zeros(n_steps)

    for i in range(n_steps):
        trajectory[i] = Phi
        dW = rng.normal(0, math.sqrt(dt))
        Phi = Phi + (-gamma * (Phi - X)) * dt + sigma_noise * dW

    # Discard transient
    burn = n_steps // 10
    data = trajectory[burn:]

    # Measured quantities
    mean_measured = np.mean(data)
    var_measured = np.var(data)
    var_predicted = D / tau

    # Autocorrelation (first 1000 lags)
    n_lags = min(1000, len(data) // 10)
    delta = data - np.mean(data)
    autocorr = np.correlate(delta[:len(delta)//2], delta[:len(delta)//2], mode='full')
    autocorr = autocorr[len(autocorr)//2:]
    autocorr = autocorr / autocorr[0]
    # Fit exponential to get tau_corr
    lags = np.arange(n_lags) * dt
    log_ac = np.log(np.maximum(autocorr[:n_lags], 1e-10))
    # Linear fit to log(C(t)) = -t/tau_corr
    valid = autocorr[:n_lags] > 0.01
    if np.sum(valid) > 10:
        coeffs = np.polyfit(lags[valid], log_ac[valid], 1)
        tau_corr_measured = -1.0 / coeffs[0]
    else:
        tau_corr_measured = float('nan')

    # Power spectrum (FFT)
    n_fft = min(2**16, len(data))
    fft_data = np.fft.rfft(delta[:n_fft])
    freqs = np.fft.rfftfreq(n_fft, d=dt)
    psd_measured = (2 * dt / n_fft) * np.abs(fft_data)**2
    # Predicted PSD
    omega = 2 * np.pi * freqs
    psd_predicted = 2 * D / (1 + omega**2 * tau**2)

    # Compare at a few frequencies
    freq_checks = [0.01, 0.1, 1.0 / (2 * np.pi * tau), 1.0]
    psd_comparisons = []
    for f in freq_checks:
        idx = np.argmin(np.abs(freqs - f))
        if idx < len(psd_measured):
            psd_comparisons.append({
                "freq": f,
                "measured": float(psd_measured[idx]),
                "predicted": float(psd_predicted[idx]),
                "ratio": float(psd_measured[idx] / max(psd_predicted[idx], 1e-30)),
            })

    return {
        "D": D, "tau": tau, "X": X,
        "n_steps": n_steps, "dt": dt,
        "mean_predicted": X,
        "mean_measured": float(mean_measured),
        "mean_error": float(abs(mean_measured - X)),
        "variance_predicted": var_predicted,
        "variance_measured": float(var_measured),
        "variance_ratio": float(var_measured / var_predicted),
        "tau_corr_predicted": tau,
        "tau_corr_measured": float(tau_corr_measured),
        "tau_corr_ratio": float(tau_corr_measured / tau) if not math.isnan(tau_corr_measured) else float('nan'),
        "psd_comparisons": psd_comparisons,
        "fdt_temperature": D / tau,
    }


# ================================================================
# MAIN
# ================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-II ALPHA — EXACT FOKKER-PLANCK DERIVATION")
    print("  Stochastic constitutive equation: tau dPhi/dt + Phi = X + xi(t)")
    print("=" * 80)

    # 1. Fokker-Planck
    print("\n--- DERIVATION 1: Fokker-Planck Equation ---")
    fp = derive_fokker_planck()
    for k, v in fp.items():
        print("  {}: {}".format(k, v))

    # 2. Stationary Measure
    print("\n--- DERIVATION 2: Stationary Measure ---")
    sm = derive_stationary_measure()
    for k, v in sm.items():
        print("  {}: {}".format(k, v))

    # 3. Power Spectrum
    print("\n--- DERIVATION 3: Power Spectral Density ---")
    ps = derive_power_spectrum()
    for k, v in ps.items():
        print("  {}: {}".format(k, v))

    # 4. FDT
    print("\n--- DERIVATION 4: Fluctuation-Dissipation Relation ---")
    fdt = derive_fdt()
    for k, v in fdt.items():
        print("  {}: {}".format(k, v))

    # 5. Autocorrelation
    print("\n--- DERIVATION 5: Autocorrelation and Moments ---")
    ac = derive_autocorrelation()
    for k, v in ac.items():
        print("  {}: {}".format(k, v))

    # 6. Numerical Verification
    print("\n--- NUMERICAL VERIFICATION ---")
    print("  Simulating 10^6 steps of Langevin equation...")
    ver = numerical_verification(D=1.0, tau=TAU, X=5.0, dt=0.001, n_steps=1000000)

    print("  D = {}, tau = {:.4f}, X = {}".format(ver["D"], ver["tau"], ver["X"]))
    print("  Mean:     predicted={:.4f}, measured={:.4f}, error={:.6f}".format(
        ver["mean_predicted"], ver["mean_measured"], ver["mean_error"]))
    print("  Variance: predicted={:.4f}, measured={:.4f}, ratio={:.4f}".format(
        ver["variance_predicted"], ver["variance_measured"], ver["variance_ratio"]))
    print("  Tau_corr: predicted={:.4f}, measured={:.4f}, ratio={:.4f}".format(
        ver["tau_corr_predicted"], ver["tau_corr_measured"], ver["tau_corr_ratio"]))
    print("  FDT temperature: k_B T = D/tau = {:.4f}".format(ver["fdt_temperature"]))

    print("\n  PSD Comparison:")
    for c in ver["psd_comparisons"]:
        print("    f={:.4f}: measured={:.4e}, predicted={:.4e}, ratio={:.2f}".format(
            c["freq"], c["measured"], c["predicted"], c["ratio"]))

    print("\n" + "=" * 80)
    print("  ALL DERIVATIONS EXACT. NUMERICAL VERIFICATION COMPLETE.")
    print("")
    print("  GRUT-II POSTULATE: +1P (noise xi exists), +1p (D)")
    print("  GRUT-II DERIVES:   Fokker-Planck, stationary measure, spectrum, FDT")
    print("  GRUT RECOVERY:     D -> 0 gives delta(Phi-X), S=0, deterministic")
    print("  TESTABLE:          S(omega) = 2D/(1+omega^2 tau^2); D = k_B T tau")
    print("=" * 80)
