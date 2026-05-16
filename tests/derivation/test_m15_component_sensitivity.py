from grut.derivation.euler.m15_component_sensitivity import run_component_sensitivity_audit


def test_expected_scenario_count() -> None:
    result = run_component_sensitivity_audit()
    scenarios = result["scenarios"]
    # 2 + 2 + 2 + 3 + 3 = 12 scenarios
    assert len(scenarios) == 12


def test_baseline_x_matches_derivation() -> None:
    result = run_component_sensitivity_audit()
    assert abs(result["base_x"] - 0.065963) < 1e-6


def test_closest_case_is_s4_plus_50() -> None:
    result = run_component_sensitivity_audit()
    closest = result["closest_to_target"]
    assert closest.component == "M_triangle"
    assert closest.perturbation == "+5%"


def test_counterterm_and_s4_in_top_leverage() -> None:
    result = run_component_sensitivity_audit()
    top8 = result["leverage_rank"][:8]
    names = {s.component for s in top8}
    assert "M_counterterm" in names
    assert "M_S4_projection" in names
