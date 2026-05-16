"""Flat-space 3-loop subset topology selection for Stage 4B."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SubsetTopology:
    topology_id: str
    loop_order: int
    factorization_possible: bool
    known_structure: str
    expected_divergence_pattern: str
    sector: str


def flat_subset_topologies() -> List[SubsetTopology]:
    return [
        SubsetTopology(
            topology_id="scalar_triple_bubble",
            loop_order=3,
            factorization_possible=True,
            known_structure="product_of_1loop",
            expected_divergence_pattern="1/epsilon^3",
            sector="scalar",
        ),
        SubsetTopology(
            topology_id="figure_eight_times_bubble",
            loop_order=3,
            factorization_possible=True,
            known_structure="product_of_1loop_and_2loop",
            expected_divergence_pattern="1/epsilon^2",
            sector="scalar",
        ),
        SubsetTopology(
            topology_id="nested_double_loop_with_bubble",
            loop_order=3,
            factorization_possible=False,
            known_structure="divergence_pattern_known",
            expected_divergence_pattern="1/epsilon^2",
            sector="scalar",
        ),
        SubsetTopology(
            topology_id="sunset_extension_scalar",
            loop_order=3,
            factorization_possible=False,
            known_structure="divergence_pattern_known",
            expected_divergence_pattern="1/epsilon",
            sector="scalar",
        ),
    ]
