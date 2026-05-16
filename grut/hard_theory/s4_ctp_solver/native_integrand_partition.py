"""Partition the native integrand into auditable pieces."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_subintegrand_set import (
    select_native_subintegrand_set,
)


TESTED_SUBINTEGRAND_IDS = (
    "native_subintegrand_chain_v1",
    "native_subintegrand_scalar_slice_v1",
    "native_subintegrand_ghost_vector_slice_v1",
)


def _tested_partitions(integrand: Dict[str, object]) -> List[Dict[str, object]]:
    tested = select_native_subintegrand_set(integrand)
    return [
        {
            "partition_id": entry["subintegrand_id"],
            "partition_type": "tested_minimal",
            "origin": "native_integrand",
            "requires_full_diagram": False,
            "requires_finite_part": False,
            "status": "partition_mapped",
            "promotes_claims": False,
        }
        for entry in tested
    ]


def partition_native_integrand(integrand: Dict[str, object]) -> List[Dict[str, object]]:
    partitions = _tested_partitions(integrand)

    partitions.extend(
        [
            {
                "partition_id": "eligible_scalar_chain_v2",
                "partition_type": "eligible_future",
                "origin": "native_integrand",
                "requires_full_diagram": False,
                "requires_finite_part": False,
                "status": "partition_mapped",
                "promotes_claims": False,
            },
            {
                "partition_id": "eligible_ghost_vector_slice_v2",
                "partition_type": "eligible_future",
                "origin": "native_integrand",
                "requires_full_diagram": False,
                "requires_finite_part": False,
                "status": "partition_mapped",
                "promotes_claims": False,
            },
            {
                "partition_id": "blocked_tensor_heavy_v1",
                "partition_type": "blocked",
                "origin": "native_integrand",
                "requires_full_diagram": False,
                "requires_finite_part": False,
                "status": "partition_mapped",
                "promotes_claims": False,
            },
            {
                "partition_id": "forbidden_full_diagram_v1",
                "partition_type": "forbidden_full_diagram",
                "origin": "native_integrand",
                "requires_full_diagram": True,
                "requires_finite_part": True,
                "status": "partition_mapped",
                "promotes_claims": False,
            },
        ]
    )

    return partitions
