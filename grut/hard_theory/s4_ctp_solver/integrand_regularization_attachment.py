"""Attach symbolic regularization metadata to an integrand scaffold."""

from typing import Dict, List


def attach_regularization_to_integrand(
    integrand: Dict[str, object],
    scheme: Dict[str, object],
) -> Dict[str, object]:
    divergence_tags: List[str] = [
        "uv_sensitive",
        "ir_sensitive",
        "scheme_dependent",
    ]

    return {
        "integrand_id": integrand.get("integrand_id"),
        "regularization_attached": True,
        "scheme": scheme,
        "regulator_factor": "symbolic_regulator_factor",
        "divergence_tags": divergence_tags,
        "integration_performed": False,
        "amplitude_computed": False,
        "finite_part_computed": False,
        "extraction_performed": False,
        "r_extracted": False,
        "status": "regularized_integrand_scaffold",
        "promotes_claims": False,
    }
