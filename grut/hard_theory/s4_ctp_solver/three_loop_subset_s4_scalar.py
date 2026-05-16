"""Curved S4 scalar 3-loop subset topologies for Stage 4C."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class S4SubsetTopology:
    topology_id: str
    loop_order: int
    background: str
    curvature_dependence: bool
    truncation_level: int
    evaluation_type: str
    status: str


def s4_scalar_subset_topologies(l_max: int) -> List[S4SubsetTopology]:
    return [
        S4SubsetTopology(
            topology_id="s4_scalar_triple_bubble",
            loop_order=3,
            background="S4",
            curvature_dependence=True,
            truncation_level=l_max,
            evaluation_type="spectral_truncated",
            status="partial_curved_subset",
        ),
        S4SubsetTopology(
            topology_id="s4_bubble_curvature_insertion",
            loop_order=3,
            background="S4",
            curvature_dependence=True,
            truncation_level=l_max,
            evaluation_type="curvature_expansion",
            status="partial_curved_subset",
        ),
        S4SubsetTopology(
            topology_id="s4_curvature_corrected_sunset",
            loop_order=3,
            background="S4",
            curvature_dependence=True,
            truncation_level=l_max,
            evaluation_type="curvature_expansion",
            status="partial_curved_subset",
        ),
        S4SubsetTopology(
            topology_id="s4_truncated_spectral_triple_product",
            loop_order=3,
            background="S4",
            curvature_dependence=True,
            truncation_level=l_max,
            evaluation_type="spectral_truncated",
            status="partial_curved_subset",
        ),
    ]
