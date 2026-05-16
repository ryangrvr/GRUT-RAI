"""Regularization schemes for TT spectral inversion (structural)."""

from typing import Dict


def define_regularization_schemes() -> Dict[str, object]:
    return {
        "schemes": ["cutoff", "exponential_damping", "zeta_placeholder"],
        "status": "defined_not_fully_applied",
        "promotes_claims": False,
    }
