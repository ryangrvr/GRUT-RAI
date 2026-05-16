"""Propagator placeholders for the S4 CTP scaffold."""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class PropagatorPlaceholder:
    """Symbolic propagator placeholder.

    Fields are descriptive only; no explicit closed form is encoded.
    """
    name: str
    field: str
    kernel_type: str
    notes: str


def graviton_propagator_placeholder() -> PropagatorPlaceholder:
    return PropagatorPlaceholder(
        name="graviton",
        field="h_mu_nu",
        kernel_type="placeholder",
        notes="S4 graviton propagator not defined at Stage 1.",
    )


def ghost_propagator_placeholder() -> PropagatorPlaceholder:
    return PropagatorPlaceholder(
        name="ghost",
        field="c_mu",
        kernel_type="placeholder",
        notes="S4 ghost propagator placeholder; no closed form.",
    )


def matter_propagator_placeholder(field_name: str) -> PropagatorPlaceholder:
    return PropagatorPlaceholder(
        name=f"matter_{field_name}",
        field=field_name,
        kernel_type="placeholder",
        notes="Matter propagator placeholder on S4.",
    )


def kernel_placeholders() -> Dict[str, PropagatorPlaceholder]:
    """Return retarded/Hadamard/Feynman kernel placeholders."""
    return {
        "retarded": PropagatorPlaceholder(
            name="retarded_kernel",
            field="generic",
            kernel_type="retarded",
            notes="Retarded kernel placeholder (no explicit support).",
        ),
        "hadamard": PropagatorPlaceholder(
            name="hadamard_kernel",
            field="generic",
            kernel_type="hadamard",
            notes="Hadamard kernel placeholder (no explicit form).",
        ),
        "feynman": PropagatorPlaceholder(
            name="feynman_kernel",
            field="generic",
            kernel_type="feynman",
            notes="Feynman kernel placeholder (no explicit form).",
        ),
    }
