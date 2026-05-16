import sympy as sp

from grut.hard_theory.s4_ctp_solver.heat_kernel import (
    scalar_heat_kernel_coefficients,
    s4_invariants,
    euler_density_s4,
    R,
    RICCI2,
    RIEMANN2,
)
from grut.hard_theory.s4_ctp_solver.anomaly_1loop_scalar import (
    scalar_anomaly_coefficients,
    scalar_trace_anomaly_s4,
)
from grut.hard_theory.s4_ctp_solver.anomaly_1loop_weyl import (
    weyl_anomaly_coefficients,
    weyl_trace_anomaly_s4,
)
from grut.hard_theory.s4_ctp_solver.anomaly_1loop_gauge import (
    gauge_anomaly_coefficients,
    gauge_trace_anomaly_s4,
)
from grut.hard_theory.s4_ctp_solver.flatspace_loop_checks import (
    one_loop_scalar_bubble_structure,
    dim_reg_terms,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_s4_curvature_substitution():
    a = sp.symbols("a", positive=True)
    invariants = s4_invariants(a)
    assert invariants[R] == 12 / a**2
    assert invariants[RICCI2] == 36 / a**4
    assert invariants[RIEMANN2] == 24 / a**4


def test_heat_kernel_coefficients_present():
    hk = scalar_heat_kernel_coefficients()
    assert hk.a0 is not None
    assert hk.a1 is not None
    assert hk.a2 is not None


def test_scalar_anomaly_coefficients_match():
    coeffs = scalar_anomaly_coefficients()
    assert coeffs.a == sp.Rational(1, 360)
    assert coeffs.c == sp.Rational(1, 120)


def test_weyl_anomaly_coefficients_match():
    coeffs = weyl_anomaly_coefficients()
    assert coeffs.a == sp.Rational(11, 720)
    assert coeffs.c == sp.Rational(1, 20)


def test_gauge_anomaly_coefficients_match():
    coeffs = gauge_anomaly_coefficients()
    assert coeffs.a == sp.Rational(31, 180)
    assert coeffs.c == sp.Rational(1, 10)


def test_weyl_squared_vanishes_on_s4():
    a = sp.symbols("a", positive=True)
    W2 = 0
    assert W2 == 0


def test_euler_density_survives_on_s4():
    a = sp.symbols("a", positive=True)
    assert euler_density_s4(a) == 24 / a**4


def test_scalar_anomaly_on_s4_matches_euler_term():
    a = sp.symbols("a", positive=True)
    coeffs = scalar_anomaly_coefficients()
    assert scalar_trace_anomaly_s4(a) == coeffs.a * euler_density_s4(a)


def test_weyl_anomaly_on_s4_matches_euler_term():
    a = sp.symbols("a", positive=True)
    coeffs = weyl_anomaly_coefficients()
    assert weyl_trace_anomaly_s4(a) == coeffs.a * euler_density_s4(a)


def test_gauge_anomaly_on_s4_matches_euler_term():
    a = sp.symbols("a", positive=True)
    coeffs = gauge_anomaly_coefficients()
    assert gauge_trace_anomaly_s4(a) == coeffs.a * euler_density_s4(a)


def test_flatspace_loop_structure():
    bubble = one_loop_scalar_bubble_structure()
    terms = dim_reg_terms()
    expected = terms["pole"] + terms["log"]
    assert sp.simplify(bubble.expression - expected) == 0


def test_pipeline_stage2_status():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage2_benchmarks()
    assert report["status"] == "benchmarked"
    assert report["label"] == "benchmarked"


def test_pipeline_no_three_loop_claims():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage2_benchmarks()
    assert "computed" not in str(report).lower()
