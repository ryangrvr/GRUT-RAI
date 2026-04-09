"""
Module 5: Anomaly cancellation — exact-zero checks.

Three conditions verified for one complete SM generation.
All three must be exactly zero for gauge consistency.
Status: Demonstrated. All three = 0.000000.
"""

import numpy as np

# Left-handed Weyl fermions (one generation)
# (name, Y, color_multiplicity)
LH_FERMIONS = [
    ("nu_L",  -1.0, 1),
    ("e_L",   -1.0, 1),
    ("u_L",   1/3,  3),
    ("d_L",   1/3,  3),
    ("e_R^c", 2.0,  1),    # RH conjugate
    ("u_R^c", -4/3, 3),
    ("d_R^c", 2/3,  3),
]

# Doublet members only
DOUBLETS = [f for f in LH_FERMIONS if f[0] in ("nu_L", "e_L", "u_L", "d_L")]


def anomaly_check() -> dict:
    """Check all three anomaly cancellation conditions.

    1. sum Y = 0 (gravitational)
    2. sum Y^3 = 0 (U(1)_Y^3)
    3. sum Y over doublets = 0 (SU(2)^2 × U(1)_Y)
    """
    sum_Y = sum(Y * Nc for _, Y, Nc in LH_FERMIONS)
    sum_Y3 = sum(Y**3 * Nc for _, Y, Nc in LH_FERMIONS)
    sum_Y_doublets = sum(Y * Nc for _, Y, Nc in DOUBLETS)

    return {
        "sum_Y": sum_Y,
        "sum_Y3": sum_Y3,
        "sum_Y_doublets": sum_Y_doublets,
        "gravitational_cancels": abs(sum_Y) < 1e-10,
        "cubic_cancels": abs(sum_Y3) < 1e-10,
        "mixed_cancels": abs(sum_Y_doublets) < 1e-10,
        "all_cancel": (abs(sum_Y) < 1e-10 and abs(sum_Y3) < 1e-10
                       and abs(sum_Y_doublets) < 1e-10),
        "status": "PASS" if (abs(sum_Y) < 1e-10 and abs(sum_Y3) < 1e-10
                             and abs(sum_Y_doublets) < 1e-10) else "FAIL",
    }
