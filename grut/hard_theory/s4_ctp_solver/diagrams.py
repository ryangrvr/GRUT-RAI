"""Diagram bookkeeping for the S4 CTP scaffold."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Diagram:
    """Diagram bookkeeping structure (no evaluation).

    All fields are metadata placeholders.
    """
    name: str
    loop_order: int
    vertices: Tuple[str, ...]
    internal_lines: Tuple[str, ...]
    external_legs: Tuple[str, ...]
    branch_labels: Tuple[str, ...]
    symmetry_factor: str
    scheme_label: str
    regulator_label: str


def diagram_placeholder(loop_order: int) -> Diagram:
    """Create a generic diagram placeholder."""
    return Diagram(
        name=f"loop_{loop_order}_placeholder",
        loop_order=loop_order,
        vertices=(),
        internal_lines=(),
        external_legs=(),
        branch_labels=("+", "-"),
        symmetry_factor="TBD",
        scheme_label="unspecified",
        regulator_label="unspecified",
    )
