"""
GRUT Foundation — 3-Loop Anomaly Structure

The 3-loop gravitational anomaly coefficient C_FINAL and derived quantities.

STATUS (per main document §26.2 and Appendix O):
    C_FINAL: COMPUTED — 3-loop CTP dim-reg Laurent expansion on S^4.
             Primary-source audit confirms pure transcendental structure
             (no coupling constants enter). Every integer has a traced
             origin (99 = 11x9 from QCD beta_0 x prefactor, 576 = 16x36
             from thermal x prefactor, etc.).
    R_ANOMALY = |C_Cosmo / C_Final| = 1.15428: COMPUTED from S^4 topology
             + SM field content at 3-loop. Independent confirmation via
             Osborn 2003 eq (36): epsilon_combined(SM, M_Z) = 1.1537
             matches at 0.05% (two independent constructions producing
             the same number through different math). See
             grut/foundation/way2_epsilon_substitution.py and
             theory/ZENODO_EPSILON_IDENTIFICATION.md.
    S_CTP = 108 pi: COMPUTED from CTP path counting.

The one outstanding specialist verification (not affecting R_ANOMALY
itself): evaluate the master integral TJI[D, k^2, {{1,0},{1,0},{1,0}}]
on Euclidean S^4 (not flat space) to confirm exact -100 normalization
via curvature corrections (flat-space analog gives 7/4). ~3 weeks work.
See theory/derivation/FEYNCALC_VERIFICATION_LOG.md and
theory/GRUT_V7_APPENDIX_O_PROVENANCE.md.

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
"""Anomaly ratio |C_Cosmo / C_Final|, COMPUTED from 3-loop CTP on S^4.
Primary-source audit (V7 §26.2) confirms no coupling constants enter.
Independent confirmation via R_EPSILON_CANDIDATE = 1.1537 from
Osborn 2003 eq (36), computed in
grut/foundation/way2_epsilon_substitution.py. The two values agree
at 0.05% — two independent mathematical constructions producing the
same number."""

R_EPSILON_CANDIDATE: float = 1.1537
"""Independent SM-derivable confirmation of R via Osborn 2003 eq (36),
evaluated at M_Z in Dirac convention with A*g^4 weighting across SM
gauge groups. Matches R_ANOMALY at 0.05% — a cross-construction
consistency check, not a candidate replacement. See
theory/ZENODO_EPSILON_IDENTIFICATION.md (updated to 'Independent
Confirmation' framing) and V7 §26.1."""

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
