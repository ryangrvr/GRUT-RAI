"""Select a minimal native sub-integrand for a dry run."""

from typing import Dict


def select_native_subintegrand(integrand: Dict[str, object]) -> Dict[str, object]:
    return {
        "subintegrand_id": "native_subintegrand_v1",
        "origin": "native_integrand",
        "complexity": "minimal",
        "full_diagram": False,
        "status": "subintegrand_selected",
        "promotes_claims": False,
    }
