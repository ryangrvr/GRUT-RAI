"""Gauge-fixing placeholders for the S4 CTP scaffold."""

from dataclasses import dataclass


@dataclass(frozen=True)
class GaugeFixing:
    """Gauge-fixing metadata placeholder."""
    name: str
    description: str
    parameters: tuple[str, ...] = ()


def de_donder_gauge() -> GaugeFixing:
    """Placeholder for de Donder gauge fixing."""
    return GaugeFixing(
        name="de_donder",
        description="De Donder gauge placeholder; no explicit operator defined.",
        parameters=("alpha",),
    )
