"""Regularization scheme definition for loop-integrand scaffold."""

from typing import Dict, List


def define_integrand_regularization_scheme() -> Dict[str, object]:
    regulators: List[str] = [
        "dimensional_regularization_placeholder",
        "spectral_cutoff_placeholder",
        "exponential_damping_placeholder",
        "zeta_placeholder",
    ]

    return {
        "scheme_id": "integrand_regularization_v1",
        "regulators": regulators,
        "default_regulator": "dimensional_regularization_placeholder",
        "status": "defined_symbolic",
        "promotes_claims": False,
    }
