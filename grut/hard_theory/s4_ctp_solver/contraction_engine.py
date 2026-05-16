"""Contraction engine scaffold for Stage 3B."""

from dataclasses import dataclass
from typing import Tuple

from grut.hard_theory.s4_ctp_solver.diagram_topologies import DiagramTopology


@dataclass(frozen=True)
class ContractionRecord:
    topology_id: str
    propagators_used: Tuple[str, ...]
    tensor_contractions_status: str
    scalar_integrals_status: str
    result_status: str
    omitted_terms: Tuple[str, ...]


def symbolic_contract_topology_with_propagators(
    topology: DiagramTopology,
    propagator_records: Tuple[str, ...],
) -> ContractionRecord:
    return ContractionRecord(
        topology_id=topology.topology_id,
        propagators_used=propagator_records,
        tensor_contractions_status="not_evaluated",
        scalar_integrals_status="not_evaluated",
        result_status="scaffold_only",
        omitted_terms=("full tensor contractions omitted", "full scalar integrals omitted"),
    )
