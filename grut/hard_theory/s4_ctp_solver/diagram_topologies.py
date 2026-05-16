"""Symbolic diagram topology records for Stage 3 partials."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class DiagramTopology:
    topology_id: str
    loop_order: int
    internal_line_count: int
    vertex_count: int
    field_content: Tuple[str, ...]
    ctp_branch_labels: Tuple[str, ...]
    gauge_label: str
    scheme_label: str
    regulator_label: str
    status: str = "represented_not_evaluated"


def stage3_topologies() -> Tuple[DiagramTopology, ...]:
    """Return the Stage 3 representative 3-loop topology set."""
    ctp = ("+", "-")
    return (
        DiagramTopology(
            topology_id="sunset_basketball",
            loop_order=3,
            internal_line_count=5,
            vertex_count=3,
            field_content=("graviton", "ghost"),
            ctp_branch_labels=ctp,
            gauge_label="covariant",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
        DiagramTopology(
            topology_id="figure_eight_with_tail",
            loop_order=3,
            internal_line_count=4,
            vertex_count=3,
            field_content=("graviton", "matter"),
            ctp_branch_labels=ctp,
            gauge_label="covariant",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
        DiagramTopology(
            topology_id="triple_bubble",
            loop_order=3,
            internal_line_count=6,
            vertex_count=3,
            field_content=("matter", "matter"),
            ctp_branch_labels=ctp,
            gauge_label="background_field",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
        DiagramTopology(
            topology_id="ghost_loop_corrected",
            loop_order=3,
            internal_line_count=5,
            vertex_count=4,
            field_content=("ghost", "graviton"),
            ctp_branch_labels=ctp,
            gauge_label="covariant",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
        DiagramTopology(
            topology_id="matter_loop_insertion",
            loop_order=3,
            internal_line_count=5,
            vertex_count=4,
            field_content=("matter", "graviton"),
            ctp_branch_labels=ctp,
            gauge_label="background_field",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
        DiagramTopology(
            topology_id="graviton_self_energy_insertion",
            loop_order=3,
            internal_line_count=5,
            vertex_count=4,
            field_content=("graviton",),
            ctp_branch_labels=ctp,
            gauge_label="covariant",
            scheme_label="ms_bar",
            regulator_label="dim_reg",
        ),
    )
