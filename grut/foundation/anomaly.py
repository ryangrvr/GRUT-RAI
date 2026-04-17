"""
GRUT Foundation — 3-Loop Anomaly Structure

The 3-loop gravitational anomaly coefficient C_FINAL and derived quantities.

STATUS (per main document §26 and §26.1):
    C_FINAL: CONDITIONAL — hand-constructed, awaiting independent 3-loop
             CTP verification.
    R_ANOMALY = |C_Cosmo / C_Final| = 1.15428: CONDITIONAL — hand-constructed.
             An SM-derivable candidate R = epsilon_combined(SM, M_Z) = 1.1537
             from Osborn 2003 eq (36) matches the hand-constructed value
             at 0.05%. See grut/foundation/way2_epsilon_substitution.py and
             theory/ZENODO_EPSILON_IDENTIFICATION.md.
    S_CTP = 108 pi: COMPUTED from CTP path counting.

Formulae retained below for continuity; all consumers should treat
R_ANOMALY as CONDITIONAL and consult the epsilon candidate as the
SM-derivable alternative.

C_FINAL = 3(99 + 2 pi^2 + 576 ln(2) zeta(3)) / (16384 pi^6)
R_ANOMALY = |C_Cosmo / C_Final| = 1.15428
S_CTP = 108 pi (CTP path-counting normalization)
"""

import numpy as np
from grut.foundation.constants import ZETA_3


# =============================================================================
# 3-LOOP ANOMALY COEFFICIENT (scheme-protected)
# =============================================================================

def compute_c_final():
    """Compute C_FINAL from SM field content.

    C_FINAL = 3(99 + 2 pi^2 + 576 ln(2) zeta(3)) / (16384 pi^6)

    The integers:
        99   — rational (SM combinatorics)
        2    — fermionic (trace structure)
        576  — gauge (boson loops)
    """
    n_rational = 99.0
    n_fermionic = 2.0 * np.pi**2
    n_gauge = 576.0 * np.log(2) * ZETA_3
    numerator = 3.0 * (n_rational + n_fermionic + n_gauge)
    denominator = 16384.0 * np.pi**6
    return numerator / denominator


C_FINAL: float = compute_c_final()
"""3-loop gravitational anomaly coefficient. Scheme-protected (nonlocal operator)."""

R_ANOMALY: float = 1.15428
"""Anomaly ratio |C_Cosmo / C_Final|, hand-constructed value.
CONDITIONAL (see module docstring). The SM-derivable candidate is
R_EPSILON_CANDIDATE = 1.1537 from Osborn 2003 eq (36), computed in
grut/foundation/way2_epsilon_substitution.py. The two values agree
at 0.05%."""

R_EPSILON_CANDIDATE: float = 1.1537
"""SM-derivable candidate for R from Osborn 2003 eq (36), evaluated at M_Z
in Dirac convention with A*g^4 weighting across SM gauge groups.
Matches R_ANOMALY at 0.05%. See theory/ZENODO_EPSILON_IDENTIFICATION.md
and grut/foundation/way2_epsilon_substitution.py for derivation and
verification path."""

S_CTP: float = 108.0 * np.pi
"""CTP normalization from path counting. S = 108 pi = 339.292."""


def c_cosmo():
    """Cosmological anomaly coefficient.

    C_Cosmo = (-108000 + pi^4 + 1536 pi^4 ln(2) + 540 zeta(3)) / (276480 pi^4)

    LOCAL operator — subject to finite renormalization. Less protected than C_FINAL.
    """
    num = -108000 + np.pi**4 + 1536 * np.pi**4 * np.log(2) + 540 * ZETA_3
    den = 276480 * np.pi**4
    return num / den


def verify() -> dict:
    """Self-test anomaly structure."""
    c = compute_c_final()
    r = abs(c_cosmo() / c)

    return {
        "C_FINAL": abs(c - 1.14021e-4) / 1.14021e-4 < 1e-4,
        "R_ANOMALY": abs(r - R_ANOMALY) / R_ANOMALY < 1e-3,
        "S_CTP": abs(S_CTP - 339.292) / 339.292 < 1e-3,
    }
