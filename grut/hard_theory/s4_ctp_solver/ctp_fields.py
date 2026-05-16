"""CTP and Keldysh field conventions for curved-background scaffolding."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class CTPFields:
    """Container for CTP metric and fluctuation fields."""
    g_plus: str
    g_minus: str
    h_plus: str
    h_minus: str


def keldysh_basis(h_plus: float, h_minus: float) -> Tuple[float, float]:
    """Keldysh basis: h_r = (h_plus + h_minus)/2, h_a = h_plus - h_minus."""
    h_r = (h_plus + h_minus) / 2.0
    h_a = h_plus - h_minus
    return h_r, h_a


def inverse_keldysh(h_r: float, h_a: float) -> Tuple[float, float]:
    """Inverse Keldysh transform: h_plus = h_r + h_a/2, h_minus = h_r - h_a/2."""
    h_plus = h_r + h_a / 2.0
    h_minus = h_r - h_a / 2.0
    return h_plus, h_minus


def default_ctp_fields() -> CTPFields:
    """Return symbolic placeholders for CTP fields."""
    return CTPFields(g_plus="g_plus", g_minus="g_minus", h_plus="h_plus", h_minus="h_minus")
