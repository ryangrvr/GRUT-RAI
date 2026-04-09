"""
Module 3: Aharonov-Bohm phase benchmark.

Phase shift delta_phi = e * integral A dx / hbar, linear in A.
Status: Demonstrated.
"""

import numpy as np
from grut_solver.sectors.ew.gauge_u1 import gauge_rhs
from grut_solver.sectors.qm.schrodinger_recovery import rk4_step


def ab_phase_test(A_values: list = None, L_AB: float = 5.0,
                  e: float = 1.0, m: float = 1.0,
                  Nx: int = 256, L: float = 20.0, sigma: float = 1.5,
                  k0: float = 2.0, dt: float = 0.001,
                  N_steps: int = 500) -> dict:
    """Measure AB phase shift for several A values. Verify linearity."""
    if A_values is None:
        A_values = [0.1, 0.2, 0.3, 0.5]

    hbar = 1.0
    tau_I = hbar / 2
    c_2 = tau_I**2 / m
    dx = L / Nx
    x = np.linspace(-L/2, L/2, Nx, endpoint=False)
    Phi = np.zeros(Nx)
    mask = np.abs(x) < L_AB / 2

    z0 = np.exp(-x**2 / (4*sigma**2)) * np.exp(1j * k0 * x)
    z0 = z0.astype(complex)
    z0 /= np.sqrt(np.sum(np.abs(z0)**2) * dx)

    # Free-propagation reference
    z_free = z0.copy()
    for _ in range(N_steps):
        z_free = rk4_step(z_free, gauge_rhs, dt,
                          np.zeros(Nx), Phi, e, c_2, tau_I, dx)
    peak_idx = int(np.argmax(np.abs(z_free)))

    results = []
    for A_0 in A_values:
        A_field = np.zeros(Nx)
        A_field[mask] = A_0

        z = z0.copy()
        for _ in range(N_steps):
            z = rk4_step(z, gauge_rhs, dt, A_field, Phi, e, c_2, tau_I, dx)

        phase_meas = np.angle(z[peak_idx]) - np.angle(z_free[peak_idx])
        phase_meas = (phase_meas + np.pi) % (2*np.pi) - np.pi
        phase_theory = e * A_0 * L_AB / hbar
        phase_theory = (phase_theory + np.pi) % (2*np.pi) - np.pi

        results.append({
            "A_0": A_0,
            "phase_theory": phase_theory,
            "phase_measured": phase_meas,
            "delta": abs(phase_meas - phase_theory),
        })

    # Linearity check: fit phase vs A
    A_arr = np.array([r["A_0"] for r in results])
    ph_arr = np.array([r["phase_measured"] for r in results])
    if len(A_arr) > 2:
        slope = np.polyfit(A_arr, ph_arr, 1)[0]
        slope_theory = e * L_AB / hbar
        linearity_err = abs(slope - slope_theory) / abs(slope_theory)
    else:
        linearity_err = float('nan')

    return {
        "points": results,
        "linearity_error": linearity_err,
        "status": "PASS" if linearity_err < 0.05 else "FAIL",
    }
