"""Baryon Asymmetry — eta_B from CTP anomaly formula.

eta_B = J_CP × K_neq × (2 - R_B) / S_B

Route 1: Field-content scaling (R_B from decomposed C_FINAL integers)
Route 2: ABJ + sphaleron (R_B from non-perturbative rate)
"""
import numpy as np
from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP, c_cosmo
from grut.foundation.constants import ZETA_3

# SM parameters
J_CP = 3.18e-5       # Jarlskog invariant (PDG 2024)
K_NEQ = 1.19e-2       # Constitutive nonequilibrium at EW threshold
N_WEYL = 45           # Total SM Weyl fermions
ETA_OBS = 6.1e-10     # Planck 2018

# Baryonic field content fractions
# Quarks: 36 Weyl, each B = 1/3, B^2 = 1/9 → effective = 4
# Leptons: 9 Weyl, B = 0 → effective = 0
F_FERMION = 4.0 / 45.0   # B^2-weighted fermion fraction
F_GAUGE_GLUON = 8 * (1.0/3.0)**2 / 12   # gluons couple only to quarks
F_GAUGE_EW = 4 * (36.0/45.0) * (1.0/3.0)**2 / 12  # W/Z partial
F_GAUGE = F_GAUGE_GLUON + F_GAUGE_EW     # ~0.1037
F_OVERALL = F_FERMION                      # conservative: use fermion fraction


def compute_eta_b(route=1):
    """Compute baryon asymmetry from GRUT formula."""
    S_B = 4 * np.pi * N_WEYL  # 565.5 (all SM Weyl in CTP path counting)

    if route == 1:
        # Decompose C_FINAL integers and weight each by baryonic fraction
        n1 = 99.0                               # rational (mixed)
        n2 = 2.0 * np.pi**2                     # fermionic
        n3 = 576.0 * np.log(2) * ZETA_3         # gauge
        denom = 16384.0 * np.pi**6

        n1_B = n1 * F_OVERALL     # rational: use overall fraction
        n2_B = n2 * F_FERMION     # fermionic: use fermion fraction
        n3_B = n3 * F_GAUGE       # gauge: use gauge fraction

        c_b_final = 3.0 * (n1_B + n2_B + n3_B) / denom
        c_b_cosmo = c_cosmo() * F_OVERALL
        R_B = abs(c_b_cosmo / c_b_final) if c_b_final != 0 else 0
    else:
        # Route 2: ABJ + sphaleron
        # k_ABJ = N_gen/(16 pi^2), sphaleron coupling = kappa alpha_W^5
        kappa = 25.0; alpha_W = 0.0336; N_gen = 3
        c_b_local = kappa * alpha_W**5
        c_b_nonlocal = N_gen / (16.0 * np.pi**2)
        R_B = abs(c_b_local / c_b_nonlocal)

    eta = J_CP * K_NEQ * (2 - R_B) / S_B
    return {
        "eta_B": eta, "eta_observed": ETA_OBS,
        "deviation_pct": (eta / ETA_OBS - 1) * 100,
        "R_B": R_B, "two_minus_R_B": 2 - R_B,
        "S_B": S_B, "J_CP": J_CP, "K_neq": K_NEQ,
        "route": route, "status": "COMPUTED",
    }
