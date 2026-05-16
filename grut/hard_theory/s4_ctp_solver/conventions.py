"""S4 background conventions for the hard-theory scaffold."""

from dataclasses import dataclass
from math import pi
from typing import Dict, Tuple


@dataclass(frozen=True)
class S4Geometry:
    """S4 geometry conventions.

    Args:
        radius_a: Sphere radius a.
    """
    radius_a: float

    @property
    def curvature_scalar(self) -> float:
        """R = 12 / a^2."""
        return 12.0 / (self.radius_a ** 2)

    @property
    def ricci_tensor_prefactor(self) -> float:
        """Ricci tensor prefactor: R_mu_nu = (3 / a^2) g_mu_nu."""
        return 3.0 / (self.radius_a ** 2)

    @property
    def riemann_prefactor(self) -> float:
        """Riemann prefactor for constant curvature."""
        return 1.0 / (self.radius_a ** 2)

    def riemann_constant_curvature_form(self) -> Dict[str, str]:
        """Symbolic constant-curvature form.

        Returns a dictionary with a symbolic expression string.
        """
        return {
            "expression": "R_abcd = (1/a^2) (g_ac g_bd - g_ad g_bc)",
            "prefactor": "1/a^2",
        }


def s4_volume(radius_a: float) -> float:
    """Vol(S4) = 8 pi^2 a^4 / 3."""
    return (8.0 * pi ** 2 * radius_a ** 4) / 3.0


def s4_curvature_identities(radius_a: float) -> Dict[str, float]:
    """Return the canonical S4 curvature identities."""
    geom = S4Geometry(radius_a=radius_a)
    return {
        "R": geom.curvature_scalar,
        "Ricci_prefactor": geom.ricci_tensor_prefactor,
        "Riemann_prefactor": geom.riemann_prefactor,
        "Volume": s4_volume(radius_a),
    }
