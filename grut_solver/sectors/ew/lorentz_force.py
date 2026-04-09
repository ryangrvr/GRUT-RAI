"""
Module 2: Lorentz force recovery — wavepacket acceleration in E field.

Ehrenfest: m d^2<x>/dt^2 = eE. Verified to < 2%.
Status: Demonstrated.
"""

import numpy as np
from grut_solver.sectors.ew.gauge_u1 import gauge_rhs
from grut_solver.sectors.qm.schrodinger_recovery import rk4_step


def lorentz_force_test(E_field: float = 0.5, e: float = 1.0, m: float = 1.0,
                        Nx: int = 256, L: float = 20.0, sigma: float = 1.5,
                        k0: float = 2.0, dt: float = 0.001,
                        N_steps: int = 300) -> dict:
    """Measure wavepacket acceleration in uniform E field.

    V = e Phi, Phi = -E*x. Classical prediction: a = eE/m.
    """
    hbar = 1.0
    tau_I = hbar / 2
    c_2 = tau_I**2 / m
    dx = L / Nx
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)

    Phi = -E_field * x
    A = np.zeros(Nx)

    z = np.exp(-x**2 / (4*sigma**2)) * np.exp(1j * k0 * x)
    z = z.astype(complex)
    z /= np.sqrt(np.sum(np.abs(z)**2) * dx)

    times, x_mean = [], []
    for step in range(N_steps):
        if step % 25 == 0:
            rho = np.abs(z)**2
            rho /= np.sum(rho) * dx
            times.append(step * dt)
            x_mean.append(float(np.sum(x * rho) * dx))

        z = rk4_step(z, gauge_rhs, dt, A, Phi, e, c_2, tau_I, dx)

    times = np.array(times)
    x_mean = np.array(x_mean)

    if len(times) > 3:
        coeffs = np.polyfit(times, x_mean, 2)
        a_measured = 2 * coeffs[0]
    else:
        a_measured = float('nan')

    a_theory = e * E_field / m
    rel_err = abs(a_measured - a_theory) / a_theory if a_theory != 0 else 0

    return {
        "E_field": E_field,
        "a_theory": a_theory,
        "a_measured": a_measured,
        "relative_error": rel_err,
        "status": "PASS" if rel_err < 0.02 else "FAIL",
    }
