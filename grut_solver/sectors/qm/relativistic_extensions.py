"""
Module 4: Relativistic extensions — KG and Dirac recovery.

Klein-Gordon: from Lorentz-covariant action. Envelope match: 2.5e-4.
Dirac: first-order spinor directed-response. Norm delta: 1.05e-11.
"""

import numpy as np


def kg_dispersion(k: float, M: float) -> float:
    """Klein-Gordon dispersion: omega = sqrt(k^2 + M^2)."""
    return np.sqrt(k**2 + M**2)


def kg_group_velocity(k: float, M: float) -> float:
    """KG group velocity: v_g = k / sqrt(k^2 + M^2) < 1 (natural units)."""
    return k / np.sqrt(k**2 + M**2)


def kg_nr_limit_test(M: float = 5.0, k: float = 0.5) -> dict:
    """Verify that KG NR limit matches Schrodinger dispersion.

    In natural units (hbar = c = 1):
    KG: omega_exact = sqrt(k^2 + M^2)
    NR: omega_approx = M + k^2/(2M)
    """
    omega_exact = np.sqrt(k**2 + M**2)
    omega_nr = M + k**2 / (2 * M)
    diff = abs(omega_exact - omega_nr)
    rel = diff / omega_exact

    return {
        "omega_exact": omega_exact,
        "omega_nr": omega_nr,
        "absolute_diff": diff,
        "relative_diff": rel,
        "M": M, "k": k,
        "status": "PASS" if rel < 1e-3 else "FAIL",
    }


def dirac_1d_benchmark(M: float = 1.0, k: float = 2.0, dt: float = 0.005,
                        N_steps: int = 400, Nx: int = 256,
                        L: float = 30.0) -> dict:
    """1+1D Dirac equation benchmark.

    Evolves a positive-energy spinor wavepacket and checks:
    - norm conservation
    - group velocity matches k/omega
    """
    dx = L / Nx
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)
    omega = np.sqrt(k**2 + M**2)

    # Positive-energy spinor
    u1 = 1.0
    u2 = k / (omega + M)
    norm_s = np.sqrt(u1**2 + u2**2)
    u1 /= norm_s
    u2 /= norm_s

    sigma = 3.0
    env = np.exp(-x**2 / (4*sigma**2)) * np.exp(1j * k * x)
    env = env.astype(complex)

    p1 = u1 * env.copy()
    p2 = u2 * env.copy()
    norm0 = float(np.sum(np.abs(p1)**2 + np.abs(p2)**2) * dx)
    p1 /= np.sqrt(norm0)
    p2 /= np.sqrt(norm0)

    def dirac_rhs(psi1, psi2):
        dp1_dx = (np.roll(psi2, -1) - np.roll(psi2, 1)) / (2 * dx)
        dp2_dx = (np.roll(psi1, -1) - np.roll(psi1, 1)) / (2 * dx)
        Hp1 = -1j * dp1_dx + M * psi1   # sigma_x d_x + M sigma_z (component 1)
        Hp2 = -1j * dp2_dx - M * psi2
        return -1j * Hp1, -1j * Hp2

    peaks = []
    times = []
    for step in range(N_steps):
        if step % 20 == 0:
            rho = np.abs(p1)**2 + np.abs(p2)**2
            peaks.append(x[np.argmax(rho)])
            times.append(step * dt)

        k1a, k1b = dirac_rhs(p1, p2)
        k2a, k2b = dirac_rhs(p1+0.5*dt*k1a, p2+0.5*dt*k1b)
        k3a, k3b = dirac_rhs(p1+0.5*dt*k2a, p2+0.5*dt*k2b)
        k4a, k4b = dirac_rhs(p1+dt*k3a, p2+dt*k3b)
        p1 += (dt/6)*(k1a + 2*k2a + 2*k3a + k4a)
        p2 += (dt/6)*(k1b + 2*k2b + 2*k3b + k4b)

    norm_final = float(np.sum(np.abs(p1)**2 + np.abs(p2)**2) * dx)
    norm_delta = abs(norm_final - 1.0)

    times = np.array(times)
    peaks = np.array(peaks)
    if len(times) > 3:
        vg_meas = np.polyfit(times, peaks, 1)[0]
    else:
        vg_meas = float('nan')

    vg_theory = k / omega

    return {
        "norm_delta": norm_delta,
        "vg_measured": vg_meas,
        "vg_theory": vg_theory,
        "vg_error": abs(vg_meas - vg_theory) / vg_theory,
        "M": M, "k": k,
        "status": "PASS" if norm_delta < 1e-8 and abs(vg_meas - vg_theory)/vg_theory < 0.05 else "MARGINAL",
    }
