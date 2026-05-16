import math

from grut.hard_theory.s4_ctp_solver.conventions import S4Geometry, s4_volume
from grut.hard_theory.s4_ctp_solver.ctp_fields import keldysh_basis, inverse_keldysh
from grut.hard_theory.s4_ctp_solver.diagrams import Diagram, diagram_placeholder
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline
from grut.hard_theory.s4_ctp_solver.ward_identities import ctp_unitarity_placeholder


def test_s4_curvature_identities():
    geom = S4Geometry(radius_a=2.0)
    assert math.isclose(geom.curvature_scalar, 12.0 / 4.0)
    assert math.isclose(geom.ricci_tensor_prefactor, 3.0 / 4.0)
    assert math.isclose(geom.riemann_prefactor, 1.0 / 4.0)


def test_s4_volume_formula():
    vol = s4_volume(radius_a=3.0)
    expected = 8.0 * math.pi ** 2 * 3.0 ** 4 / 3.0
    assert math.isclose(vol, expected)


def test_keldysh_transform_invertible():
    h_plus = 1.25
    h_minus = -0.75
    h_r, h_a = keldysh_basis(h_plus, h_minus)
    h_plus_2, h_minus_2 = inverse_keldysh(h_r, h_a)
    assert math.isclose(h_plus, h_plus_2)
    assert math.isclose(h_minus, h_minus_2)


def test_ctp_unitarity_placeholder():
    result = ctp_unitarity_placeholder()
    assert result["Gamma_g_g"] == 0.0
    assert result["status"] == "not_evaluated"


def test_diagram_metadata_fields():
    diag = diagram_placeholder(loop_order=3)
    assert isinstance(diag, Diagram)
    assert diag.loop_order == 3
    assert diag.branch_labels
    assert diag.scheme_label
    assert diag.regulator_label


def test_three_loop_diagram_placeholder_not_evaluated():
    diag = diagram_placeholder(loop_order=3)
    assert diag.loop_order == 3
    assert diag.symmetry_factor == "TBD"


def test_pipeline_status_scaffold():
    pipeline = S4CTPPipeline()
    status = pipeline.status()
    assert status.tier == "scaffold"


def test_pipeline_refuses_promotion():
    pipeline = S4CTPPipeline()
    try:
        pipeline.promote_to_computed()
    except RuntimeError as exc:
        assert "scaffold" in str(exc).lower()
    else:
        raise AssertionError("Expected RuntimeError")


def test_ward_identity_not_evaluated():
    pipeline = S4CTPPipeline()
    assert pipeline.status().tier == "scaffold"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as _
    assert _.S4CTPPipeline
