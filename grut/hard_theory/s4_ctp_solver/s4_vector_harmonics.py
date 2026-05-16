"""Vector harmonic structure on S4 (structural only)."""

from typing import Dict


def build_vector_harmonics_structure() -> Dict[str, object]:
    return {
        "structure": "vector_harmonics",
        "components": ["transverse", "longitudinal"],
        "properties": {
            "divergence_free_modes": "transverse vector harmonics",
            "gradient_modes": "longitudinal gradients of scalar harmonics",
        },
        "status": "structural_only",
        "promotes_claims": False,
    }
