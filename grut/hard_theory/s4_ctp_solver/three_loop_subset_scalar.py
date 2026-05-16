"""Scalar-only 3-loop subset topology selection for Stage 4B."""

from typing import List

from grut.hard_theory.s4_ctp_solver.three_loop_subset_flat import (
    SubsetTopology,
    flat_subset_topologies,
)


def scalar_subset_topologies() -> List[SubsetTopology]:
    return [topo for topo in flat_subset_topologies() if topo.sector == "scalar"]
