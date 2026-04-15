"""
GRUT Foundation — The Noise Kernel

    delta^2 S_CTP / delta z_a^2 = i N                             (7)

The noise kernel N and dissipation 1/tau are related by FDT:
    N(omega) = (2/tau) hbar omega coth(hbar omega / 2 k_B T)      (9)

In the gravitational sector (Newtonian limit):
    N_grav(x, x') = G / (hbar |x - x'|)                           (12)
"""

import numpy as np
from grut.foundation.constants import G, HBAR, K_B


def noise_kernel_gravitational(x, x_prime):
    """The Diósi gravitational noise kernel.

    N_grav(x, x') = G / (hbar |x - x'|)

    Derived from the imaginary part of the CTP influence functional
    in the Newtonian limit (Anastopoulos & Hu, CQG 30, 165007, 2013).
    """
    r = np.abs(x - x_prime)
    if r == 0:
        return 0.0  # self-energy regularized by finite body
    return G / (HBAR * r)


def fdt_noise(omega, tau, T):
    """Fluctuation-dissipation relation: noise from dissipation + temperature.

    N(omega) = (2/tau) × hbar omega × coth(hbar omega / (2 k_B T))

    Classical limit (kT >> hbar omega): N → (2/tau) × 2 k_B T
    Quantum limit (kT << hbar omega): N → (2/tau) × hbar omega
    """
    if tau <= 0:
        return 0.0
    x = HBAR * omega / (2 * K_B * T) if T > 0 else float('inf')
    if x > 500:
        coth = 1.0
    elif x < 1e-10:
        coth = 1.0 / x
    else:
        coth = np.cosh(x) / np.sinh(x)
    return (2.0 / tau) * HBAR * omega * coth


def extended_body_suppression(l, R):
    """Extended-body suppression factor S(l/R).

    S(l/R) = min(1, (l/R)^3 / 6)

    Arises from integrating the Diósi kernel over a uniform sphere.
    Near field (l < R): suppressed by (l/R)^3.
    Far field (l > R): point-mass limit, S = 1.
    """
    if R <= 0:
        return 1.0
    ratio = l / R
    return min(1.0, ratio**3 / 6.0)


def lambda_grav(m, l, R=None):
    """Gravitational decoherence rate [Hz].

    Lambda_grav = G m^2 S(l/R) / (hbar l)

    Zero free parameters. Derived from the CTP noise kernel.
    """
    if m <= 0 or l <= 0:
        return 0.0
    S = extended_body_suppression(l, R) if R is not None else 1.0
    return G * m**2 * S / (HBAR * l)


def tau_kms(T_kelvin):
    """KMS thermal relaxation time.

    tau_KMS = hbar / (2 pi k_B T)

    Derived from the KMS condition for thermal equilibrium
    in the CTP formalism.
    """
    if T_kelvin <= 0:
        return float('inf')
    return HBAR / (2 * np.pi * K_B * T_kelvin)


def verify() -> dict:
    """Self-test noise kernel."""
    # Lambda_grav for gold benchmark
    m_gold = 80.8e-15  # kg
    R_gold = 1e-6       # m
    l_gold = 1e-6        # m
    Lambda = lambda_grav(m_gold, l_gold, R_gold)
    gold_ok = abs(Lambda - 689) / 689 < 0.01

    # S(l/R) = 1/6 when l = R
    S_at_1 = extended_body_suppression(1e-6, 1e-6)
    s_ok = abs(S_at_1 - 1/6) < 0.01

    # FDT classical limit: N → 4 k_B T / tau
    tau_test = 1.0
    T_test = 300.0
    omega_test = 1.0  # low frequency
    N = fdt_noise(omega_test, tau_test, T_test)
    # coth(hbar omega / 2kT) → 2kT/(hbar omega) for small x
    N_classical = (2/tau_test) * 2 * K_B * T_test
    fdt_ok = abs(N - N_classical) / N_classical < 0.01

    return {
        "gold_benchmark_689Hz": gold_ok,
        "suppression_at_l_eq_R": s_ok,
        "fdt_classical_limit": fdt_ok,
    }
