"""Vertex placeholders for the S4 CTP scaffold."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Vertex:
    """Symbolic vertex placeholder."""
    name: str
    fields: Tuple[str, ...]
    derivatives: str
    notes: str


def graviton_vertex(order: int) -> Vertex:
    """Placeholder for n-graviton vertex."""
    return Vertex(
        name=f"graviton_vertex_{order}",
        fields=tuple(["h_mu_nu"] * order),
        derivatives="symbolic",
        notes="Vertex structure not expanded at Stage 1.",
    )
