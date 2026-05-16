import inspect

from grut.derivation.euler import m15_diagram_origin_derivation as mod


def test_has_required_component_terms() -> None:
    terms = mod.build_independent_decomposition()
    names = {t.name for t in terms}
    assert names == {
        "M_box",
        "M_triangle",
        "M_bubble",
        "M_counterterm",
        "M_S4_projection",
    }


def test_no_target_in_assembly_function() -> None:
    # Enforce strict rule: diagnostic reference must not appear inside assembly.
    src = inspect.getsource(mod.derive_m15_from_diagrams)
    src = src.replace(" ", "")
    assert "DIAGNOSTIC_REQUIRED_X" not in src.split("outcome=")[0]


def test_derived_x_is_physical_and_positive() -> None:
    result = mod.derive_m15_from_diagrams()
    assert result["x_derived"] > 0.0
    assert result["m15_derived"] > 0.0


def test_outcome_table_strong_resolution_band() -> None:
    out = mod.classify_outcome(
        x_derived=0.066,
        x_uncertainty=0.002,
        x_reference=0.0664,
        scheme_sensitive=False,
    )
    assert out["outcome"] == "derived value 0.064-0.068*kappa"
    assert out["meaning"] == "strong Gate 2 resolution"


def test_outcome_table_baseline_survives() -> None:
    out = mod.classify_outcome(
        x_derived=0.078,
        x_uncertainty=0.003,
        x_reference=0.0664,
        scheme_sensitive=False,
    )
    assert out["outcome"] == "derived value closer to 0.080*kappa"
    assert out["meaning"] == "V5 baseline survives, R remains off"


def test_outcome_table_proportional_informative() -> None:
    out = mod.classify_outcome(
        x_derived=0.055,
        x_uncertainty=0.003,
        x_reference=0.0664,
        scheme_sensitive=False,
    )
    assert out["outcome"] == "derived value closer to 0.052*kappa"
    assert out["meaning"] == "proportional decomposition was too strong but informative"


def test_outcome_table_scheme_dependent() -> None:
    out = mod.classify_outcome(
        x_derived=0.066,
        x_uncertainty=0.02,
        x_reference=0.0664,
        scheme_sensitive=True,
    )
    assert out["outcome"] == "scheme-dependent value"
    assert out["meaning"] == "no promotion"


def test_outcome_table_cannot_compute() -> None:
    out = mod.classify_outcome(
        x_derived=-1.0,
        x_uncertainty=0.0,
        x_reference=0.0664,
        scheme_sensitive=False,
    )
    assert out["outcome"] == "cannot compute"
    assert out["meaning"] == "blocked, not resolved"
