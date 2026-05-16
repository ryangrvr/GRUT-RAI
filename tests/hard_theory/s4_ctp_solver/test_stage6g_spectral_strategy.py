from grut.hard_theory.s4_ctp_solver.s4_tt_mode_decomposition import (
    define_tt_mode_decomposition,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_eigenvalues import define_tt_eigenvalues
from grut.hard_theory.s4_ctp_solver.s4_tt_degeneracies import define_tt_degeneracies
from grut.hard_theory.s4_ctp_solver.s4_tt_zero_mode_handling import (
    define_zero_mode_strategy,
)
from grut.hard_theory.s4_ctp_solver.s4_tt_inversion_strategy import (
    define_spectral_inversion_strategy,
)
from grut.hard_theory.s4_ctp_solver.stage6g_spectral_strategy import (
    run_stage6g_spectral_strategy,
)
from grut.hard_theory.s4_ctp_solver.pipeline import S4CTPPipeline


def test_tt_mode_decomposition_defined():
    decomposition = define_tt_mode_decomposition()
    assert decomposition["decomposition_id"] == "s4_tt_modes"


def test_tt_eigenvalues_defined():
    eigenvalues = define_tt_eigenvalues()
    assert eigenvalues["eigenvalues_id"] == "s4_tt_eigenvalues"
    assert eigenvalues["status"] == "defined_not_summed"


def test_tt_degeneracies_defined():
    degeneracies = define_tt_degeneracies()
    assert degeneracies["degeneracies_id"] == "s4_tt_degeneracies"


def test_zero_mode_strategy_defined():
    zero_modes = define_zero_mode_strategy()
    assert zero_modes["zero_mode_id"] == "s4_tt_zero_modes"
    assert "project_out_gauge_modes" in zero_modes["handling_strategy"]


def test_inversion_strategy_combines_components():
    strategy = define_spectral_inversion_strategy()
    assert strategy["strategy_id"] == "s4_tt_spectral_inversion"
    assert strategy["components"]
    assert strategy["status"] == "strategy_defined_not_executed"


def test_stage6g_flags_and_guard():
    report = run_stage6g_spectral_strategy()
    assert report["can_extract"] is False
    assert report["can_compute_r"] is False
    assert report["promotes_claims"] is False
    assert report["inversion_performed"] is False
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_stage6g_pipeline_statuses_unchanged():
    pipeline = S4CTPPipeline()
    stage6f_before = pipeline.run_stage6f_tt_propagator()
    _ = pipeline.run_stage6g_spectral_strategy()
    stage6f_after = pipeline.run_stage6f_tt_propagator()
    assert stage6f_before["status"] == stage6f_after["status"]


def test_no_full_three_loop_claims_in_stage6g():
    pipeline = S4CTPPipeline()
    report = pipeline.run_stage6g_spectral_strategy()
    assert report["can_compute_full_3loop"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
