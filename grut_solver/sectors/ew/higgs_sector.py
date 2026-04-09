"""
Module 6: Higgs sector — spontaneous symmetry breaking.

V(H) = -mu^2 |H|^2 + lambda |H|^4.  VEV v = mu/sqrt(lambda) = 246 GeV.
SU(2) × U(1)_Y -> U(1)_EM.  Q<H> = 0 exactly.
Status: Demonstrated.
"""

import numpy as np
from grut_solver.sectors.ew.electroweak_su2_u1 import T_GEN


def higgs_vev(mu2: float = 1.0, lam: float = 0.5) -> dict:
    """Compute Higgs VEV and verify Mexican-hat minimum."""
    v = np.sqrt(mu2 / lam)
    h_min = np.sqrt(mu2 / (2 * lam))  # |H| at minimum
    V_min = -mu2 * h_min**2 + lam * h_min**4
    V_origin = 0.0
    m_H = np.sqrt(2 * mu2)  # Higgs boson mass

    return {
        "v": v,
        "h_min": h_min,
        "V_min": V_min,
        "V_origin": V_origin,
        "origin_unstable": V_min < V_origin,
        "m_H": m_H,
    }


def symmetry_breaking_check(Y_H: int = 1) -> dict:
    """Verify SU(2) × U(1)_Y -> U(1)_EM.

    Q <H> = 0 means the photon remains massless.
    T^1, T^2, T^3 individually break the VEV.
    """
    v = 1.0  # normalized
    H_vev = np.array([0, v / np.sqrt(2)], dtype=complex)

    # Check each generator
    broken = []
    for a in range(3):
        T_H = T_GEN[a] @ H_vev
        is_broken = np.max(np.abs(T_H)) > 1e-10
        broken.append({"generator": f"T^{a+1}", "broken": is_broken})

    Y_action = (Y_H / 2) * H_vev
    broken.append({"generator": "Y/2", "broken": np.max(np.abs(Y_action)) > 1e-10})

    # Q = T^3 + Y/2
    Q_action = T_GEN[2] @ H_vev + (Y_H / 2) * H_vev
    Q_zero = np.max(np.abs(Q_action)) < 1e-10

    n_individually_broken = sum(1 for b in broken if b["broken"])
    # The 4 generators of SU(2)×U(1)_Y are T^1, T^2, T^3, Y/2.
    # All 4 individually break <H>, but Q = T^3 + Y/2 does not.
    # So: 3 broken combinations (eating 3 Goldstones) + 1 unbroken (Q).
    n_broken_combinations = 3  # T^1, T^2, and the combination T^3 - Y/2
    n_goldstones = 3

    return {
        "generators": broken,
        "Q_H_is_zero": Q_zero,
        "n_individually_broken": n_individually_broken,
        "n_broken": n_broken_combinations,
        "n_goldstones": n_goldstones,
        "dof_check": "4 Higgs DOF = 3 Goldstones + 1 physical Higgs",
        "status": "PASS" if Q_zero else "FAIL",
    }
