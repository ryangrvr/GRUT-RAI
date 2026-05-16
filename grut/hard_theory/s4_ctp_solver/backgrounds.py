"""Background selection for the S4 CTP scaffold."""

from dataclasses import dataclass
from grut.hard_theory.s4_ctp_solver.conventions import S4Geometry


@dataclass(frozen=True)
class Background:
    """Named background wrapper."""
    name: str
    geometry: S4Geometry


def s4_background(radius_a: float) -> Background:
    """Create the canonical S4 background."""
    return Background(name="S4", geometry=S4Geometry(radius_a=radius_a))
