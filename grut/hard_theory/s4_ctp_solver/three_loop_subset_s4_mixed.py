"""Mixed scalar-tensor subset topologies for Stage 4E."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class S4MixedSubsetTopology:
    topology_id: str
    loop_order: int
    background: str
    scalar_component: bool
    tensor_component: bool
    evaluation_type: str
    status: str


def s4_mixed_subset_topologies() -> List[S4MixedSubsetTopology]:
    return [
        S4MixedSubsetTopology(
            topology_id="scalar_triple_bubble_with_tt_insertion",
            loop_order=3,
            background="S4",
            scalar_component=True,
            tensor_component=True,
            evaluation_type="spectral_truncated_mixed",
            status="mixed_subset_structural",
        ),
        S4MixedSubsetTopology(
            topology_id="scalar_bubble_times_tensor_bubble",
            loop_order=3,
            background="S4",
            scalar_component=True,
            tensor_component=True,
            evaluation_type="structure_only",
            status="mixed_subset_structural",
        ),
        S4MixedSubsetTopology(
            topology_id="scalar_spectral_with_tensor_vertex_correction",
            loop_order=3,
            background="S4",
            scalar_component=True,
            tensor_component=True,
            evaluation_type="spectral_truncated_mixed",
            status="mixed_subset_structural",
        ),
        S4MixedSubsetTopology(
            topology_id="curvature_corrected_scalar_with_tensor_insertion",
            loop_order=3,
            background="S4",
            scalar_component=True,
            tensor_component=True,
            evaluation_type="curvature_expansion_mixed",
            status="mixed_subset_structural",
        ),
    ]
