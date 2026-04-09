"""
Module 7: W/Z mass relations and rho parameter.

m_W = gv/2, m_Z = sqrt(g^2+g'^2) v/2, rho = 1.000000 at tree level.
Status: Demonstrated.
"""

import numpy as np
from grut_solver.constants import AMU


# SM physical parameters
G_WEAK = 0.653
G_PRIME = 0.350
V_HIGGS = 246.0  # GeV


def gauge_boson_masses(g: float = G_WEAK, g_prime: float = G_PRIME,
                        v: float = V_HIGGS) -> dict:
    """Compute W, Z masses, Weinberg angle, rho parameter."""
    m_W = g * v / 2
    m_Z = np.sqrt(g**2 + g_prime**2) * v / 2
    m_photon = 0.0

    sin2_W = g_prime**2 / (g**2 + g_prime**2)
    cos2_W = g**2 / (g**2 + g_prime**2)
    theta_W = np.arcsin(np.sqrt(sin2_W))
    e_em = g * np.sqrt(sin2_W)  # electromagnetic coupling

    rho = m_W**2 / (m_Z**2 * cos2_W)

    # Neutral mass matrix eigenvalues
    M2 = (v**2 / 4) * np.array([
        [g**2, -g*g_prime],
        [-g*g_prime, g_prime**2],
    ])
    eigenvalues = np.sort(np.linalg.eigvalsh(M2))

    return {
        "m_W": m_W,
        "m_Z": m_Z,
        "m_photon": m_photon,
        "sin2_theta_W": sin2_W,
        "cos2_theta_W": cos2_W,
        "theta_W_deg": np.degrees(theta_W),
        "e_em": e_em,
        "rho": rho,
        "rho_exact_one": abs(rho - 1.0) < 1e-10,
        "photon_massless": eigenvalues[0] < 1e-6,
        "neutral_eigenvalues": eigenvalues.tolist(),
        "status": "PASS" if abs(rho - 1.0) < 1e-10 else "FAIL",
    }


def fermion_masses(v: float = V_HIGGS) -> dict:
    """Compute fermion masses from M_f = y_f v / sqrt(2). Yukawas are FREE."""
    fermions = [
        ("electron",  0.000511), ("muon",    0.1057),  ("tau",    1.777),
        ("up",        0.0022),   ("down",    0.0047),  ("charm",  1.28),
        ("strange",   0.095),    ("top",     173.0),   ("bottom", 4.18),
    ]
    results = []
    for name, mass_gev in fermions:
        y_f = mass_gev * np.sqrt(2) / v
        results.append({"name": name, "M_GeV": mass_gev, "y_f": y_f})

    y_top = 173.0 * np.sqrt(2) / v
    y_electron = 0.000511 * np.sqrt(2) / v
    hierarchy = y_top / y_electron

    return {
        "fermions": results,
        "yukawa_hierarchy": hierarchy,
        "v_GeV": v,
        "yukawas_free": True,
        "note": "Yukawa couplings are FREE parameters (same as SM). Not derived.",
    }


def sm_parameter_count() -> dict:
    """Count SM-equivalent free parameters in the GRUT framework."""
    # Individual parameter accounting
    params = {
        "tau_I (= hbar/2)": ("identified", 1),
        "v (Higgs VEV)": ("free", 1),
        "g (SU(2))": ("free", 1),
        "g' (U(1)_Y)": ("free", 1),
        "g_s (SU(3))": ("free", 1),
        "lambda (Higgs self-coupling)": ("free", 1),
        "y_e": ("free", 1), "y_mu": ("free", 1), "y_tau": ("free", 1),
        "y_u": ("free", 1), "y_d": ("free", 1), "y_c": ("free", 1),
        "y_s": ("free", 1), "y_t": ("free", 1), "y_b": ("free", 1),
        "CKM theta_12": ("free", 1), "CKM theta_13": ("free", 1),
        "CKM theta_23": ("free", 1), "CKM delta": ("free", 1),
        "theta_QCD": ("free", 1),
    }
    n_free = sum(c for s, c in params.values() if s == "free")
    n_identified = sum(c for s, c in params.values() if s == "identified")

    return {
        "parameters": params,
        "n_free": n_free,
        "n_identified": n_identified,
        "total": n_free + n_identified,
        "matches_SM": True,
        "note": "Parameter count matches the Standard Model. No reduction.",
    }
