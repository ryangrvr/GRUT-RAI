from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)


def test_stage12b_classifications_run():
    report = run_stage12b_scheme_stability_audit()
    classifications = report["classifications"]["classifications"]
    assert classifications


def test_nonlocal_protected_candidate_marked_stable():
    report = run_stage12b_scheme_stability_audit()
    stable_keys = {
        entry["candidate_key"] for entry in report["audit"]["stable_candidates"]
    }
    assert "nonlocal_scheme_protected_candidate" in stable_keys


def test_c_cosmo_candidate_marked_fragile():
    report = run_stage12b_scheme_stability_audit()
    fragile_keys = {
        entry["candidate_key"] for entry in report["audit"]["fragile_candidates"]
    }
    assert "c_cosmo_candidate" in fragile_keys


def test_scheme_fragile_candidate_marked_fragile():
    report = run_stage12b_scheme_stability_audit()
    fragile_keys = {
        entry["candidate_key"] for entry in report["audit"]["fragile_candidates"]
    }
    assert "scheme_fragile_candidate" in fragile_keys


def test_r_route_legality_assessed():
    report = run_stage12b_scheme_stability_audit()
    assert report["r_route"]["r_route_status"] in {
        "blocked",
        "conditionally_allowed_future",
    }


def test_r_route_stays_blocked_for_now():
    report = run_stage12b_scheme_stability_audit()
    assert report["can_compute_r"] is False
    assert report["r_route"]["can_compute_r_now"] is False


def test_no_coefficient_computation_or_extraction():
    report = run_stage12b_scheme_stability_audit()
    assert report["can_compute_c_final"] is False
    assert report["can_compute_c_cosmo"] is False
    assert report["can_extract"] is False
    assert report["r_route"]["can_extract"] is False


def test_recursive_guard_invoked():
    report = run_stage12b_scheme_stability_audit()
    assert report["guard"]["guard"] == "tensor_placeholder_guard"


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
