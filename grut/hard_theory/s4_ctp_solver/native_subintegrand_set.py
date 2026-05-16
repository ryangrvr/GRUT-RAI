"""Select a minimal set of native sub-integrands for consistency checks."""

from typing import Dict, List


def select_native_subintegrand_set(integrand: Dict[str, object]) -> List[Dict[str, object]]:
    return [
        {
            "subintegrand_id": "native_subintegrand_chain_v1",
            "origin": "native_integrand",
            "complexity": "minimal",
            "full_diagram": False,
            "status": "subintegrand_selected",
            "promotes_claims": False,
        },
        {
            "subintegrand_id": "native_subintegrand_scalar_slice_v1",
            "origin": "native_integrand",
            "complexity": "minimal",
            "full_diagram": False,
            "status": "subintegrand_selected",
            "promotes_claims": False,
        },
        {
            "subintegrand_id": "native_subintegrand_ghost_vector_slice_v1",
            "origin": "native_integrand",
            "complexity": "minimal",
            "full_diagram": False,
            "status": "subintegrand_selected",
            "promotes_claims": False,
        },
    ]
