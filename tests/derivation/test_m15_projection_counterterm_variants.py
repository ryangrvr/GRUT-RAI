from grut.derivation.euler.m15_projection_counterterm_variants import (
    classify_audit_outcome,
    counterterm_variants,
    projection_variants,
    run_variant_audit,
)


def test_variant_catalog_sizes() -> None:
    assert len(projection_variants()) == 5
    assert len(counterterm_variants()) == 5


def test_grid_size_is_25() -> None:
    result = run_variant_audit()
    assert len(result["results"]) == 25


def test_ranked_first_is_best_by_abs_target_distance() -> None:
    result = run_variant_audit()
    ranked = result["ranked"]
    best = ranked[0]
    for row in ranked[1:]:
        assert abs(best.r_value - 1.1547005383792515) <= abs(row.r_value - 1.1547005383792515)


def test_classification_return_shape() -> None:
    result = run_variant_audit()
    classification = result["classification"]
    assert "outcome" in classification
    assert "meaning" in classification


def test_classification_enum_coverage() -> None:
    # Counterterm-dominant branch
    out = classify_audit_outcome([], [], True)
    assert out["outcome"] == "counterterm choice dominates"
