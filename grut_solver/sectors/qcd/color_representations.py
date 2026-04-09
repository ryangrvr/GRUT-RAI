"""
Module 2: Color representations — fundamental, anti-fundamental, adjoint.

Status: Implemented (bookkeeping and verification).
"""

import numpy as np
from grut_solver.sectors.qcd.su3_structure import T_GEN, N_C, N_GEN, casimir_fundamental


# ── Quark color assignments ─────────────────────────────────
COLOR_LABELS = ["red", "green", "blue"]

# Fundamental representation basis vectors
COLOR_STATES = {
    "red":   np.array([1, 0, 0], dtype=complex),
    "green": np.array([0, 1, 0], dtype=complex),
    "blue":  np.array([0, 0, 1], dtype=complex),
}


def color_charge(state: np.ndarray, generator_idx: int) -> complex:
    """Compute the color charge <state|T^a|state>."""
    T = T_GEN[generator_idx]
    return np.vdot(state, T @ state)


def color_singlet_check(state_3x3: np.ndarray) -> dict:
    """Check if a 3-component state is a color singlet (T^a |state> = 0 for all a).

    A true singlet requires a composite object (e.g., qqq baryon or q-qbar meson).
    A single quark is never a singlet.
    """
    max_charge = 0.0
    for a in range(N_GEN):
        charge = np.linalg.norm(T_GEN[a] @ state_3x3)
        max_charge = max(max_charge, float(charge))

    return {
        "max_color_charge": max_charge,
        "is_singlet": max_charge < 1e-10,
    }


def representation_dimensions() -> dict:
    """Document the standard SU(3) representations."""
    C_F = casimir_fundamental()
    C_A = float(N_C)  # Adjoint Casimir = N

    return {
        "fundamental": {"dim": N_C, "Casimir": C_F, "objects": "quarks"},
        "anti_fundamental": {"dim": N_C, "Casimir": C_F, "objects": "antiquarks"},
        "adjoint": {"dim": N_GEN, "Casimir": C_A, "objects": "gluons"},
        "singlet": {"dim": 1, "Casimir": 0.0, "objects": "hadrons (color-neutral)"},
        "C_F_expected": (N_C**2 - 1) / (2 * N_C),
    }
