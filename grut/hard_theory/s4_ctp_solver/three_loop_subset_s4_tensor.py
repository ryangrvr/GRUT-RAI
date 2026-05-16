"""Tensor-sector subset topologies for Stage 4D."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class S4TensorSubsetTopology:
    topology_id: str
    loop_order: int
    background: str
    includes_tensor: bool
    tensor_role: str
    evaluation_type: str
    status: str


def s4_tensor_subset_topologies() -> List[S4TensorSubsetTopology]:
    return [
        S4TensorSubsetTopology(
            topology_id="scalar_loop_with_tt_insertion",
            loop_order=3,
            background="S4",
            includes_tensor=True,
            tensor_role="insertion",
            evaluation_type="structure_only",
            status="tensor_subset_structural",
        ),
        S4TensorSubsetTopology(
            topology_id="tt_bubble_times_scalar_bubble",
            loop_order=3,
            background="S4",
            includes_tensor=True,
            tensor_role="propagator_placeholder",
            evaluation_type="structure_only",
            status="tensor_subset_structural",
        ),
        S4TensorSubsetTopology(
            topology_id="tensor_corrected_sunset",
            loop_order=3,
            background="S4",
            includes_tensor=True,
            tensor_role="vertex_structure",
            evaluation_type="structure_only",
            status="tensor_subset_structural",
        ),
        S4TensorSubsetTopology(
            topology_id="graviton_self_energy_insertion",
            loop_order=3,
            background="S4",
            includes_tensor=True,
            tensor_role="insertion",
            evaluation_type="structure_only",
            status="tensor_subset_structural",
        ),
    ]
