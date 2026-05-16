"""1-loop gauge boson trace anomaly benchmarks."""

from dataclasses import dataclass
import sympy as sp

from grut.hard_theory.s4_ctp_solver.heat_kernel import euler_density_s4


@dataclass(frozen=True)
class AnomalyCoefficients:
    a: sp.Expr
    c: sp.Expr
    b: sp.Expr
    status: str = "benchmarked"


def gauge_anomaly_coefficients() -> AnomalyCoefficients:
    """Canonical gauge boson anomaly coefficients (Duff 1994 conventions)."""
    return AnomalyCoefficients(
        a=sp.Rational(31, 180),
        c=sp.Rational(1, 10),
        b=sp.Rational(-31, 180),
    )


def gauge_trace_anomaly_s4(radius_a: sp.Expr) -> sp.Expr:
    """Gauge trace anomaly on S4 (W2=0, box R=0)."""
    coeffs = gauge_anomaly_coefficients()
    return coeffs.a * euler_density_s4(radius_a)
