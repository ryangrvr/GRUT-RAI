import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_harmonic_spectra import (
    define_s4_harmonic_spectra,
)
from grut.hard_theory.s4_ctp_solver.s4_vector_harmonics import (
    build_vector_harmonics_structure,
)
from grut.hard_theory.s4_ctp_solver.s4_tensor_harmonics_extended import (
    extend_tensor_harmonics,
)
from grut.hard_theory.s4_ctp_solver.harmonic_consistency_checks import (
    check_harmonic_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage6e_harmonic_benchmark import (
    run_stage6e_harmonic_benchmark,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_scalar_harmonic_spectrum_defined():
    spectra = define_s4_harmonic_spectra()
    assert spectra["scalar_modes"]
    radius = sp.symbols("a", positive=True)
    eigenvalue = spectra["scalar_modes"][1]["eigenvalue"]
    assert sp.simplify(eigenvalue - (1 * (1 + 3) / radius**2)) == 0


def test_vector_harmonics_components():
    vector_structure = build_vector_harmonics_structure()
    assert "transverse" in vector_structure["components"]
    assert "longitudinal" in vector_structure["components"]


def test_tensor_harmonics_tt_placeholder():
    tensor_structure = extend_tensor_harmonics()
    assert "TT_placeholder" in tensor_structure["components"]
    assert tensor_structure["status"] == "structural_placeholder"


def test_consistency_checks_run():
    spectra = define_s4_harmonic_spectra()
    vector_structure = build_vector_harmonics_structure()
    tensor_structure = extend_tensor_harmonics()
    consistency = check_harmonic_consistency(
        spectra,
        vector_structure,
        tensor_structure,
    )
    assert consistency["consistency"] == "harmonic_decomposition"
    assert consistency["status"] in {"consistent", "incomplete"}


def test_stage6e_flags_and_guard():
    report = run_stage6e_harmonic_benchmark()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6e_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6d_before = pipeline.run_stage6d_ghost_propagator()
    _ = pipeline.run_stage6e_harmonic_benchmark()
    stage6d_after = pipeline.run_stage6d_ghost_propagator()
    assert stage6d_before["status"] == stage6d_after["status"]


def test_no_full_three_loop_claims_in_stage6e():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6e_harmonic_benchmark()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
