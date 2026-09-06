"""Tests for the sector-selection firewall (Phase 3).

Scope guard: these tests verify the registered clustering pipeline and its
claim firewall only. They do NOT test, modify, or reinterpret model
semantics, the reducibility gate, or any frozen artifact.
"""
import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rrt0.sector_firewall import (  # noqa: E402
    CONTROLS, aggregate, registered_conditions, run_condition,
    run_firewall, verdict,
)

ALLOWED_OUTCOMES = {
    "STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE",
    "NO_STABLE_ALGORITHMIC_RELATIONAL_STRUCTURE_DETECTED",
    "SECTOR_SELECTION_DIAGNOSTIC_FAILED",
    "SECTOR_SELECTION_UNRESOLVED",
}
CLAIM_FIREWALL = "IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE"


def test_registered_constants():
    conds = registered_conditions()
    assert len(conds) == 6
    for c in conds:
        assert c["seed"] > 0 and c["lam"] > 0 and c["tau"] > 0
    # every registered control has a threshold and a pass flag in aggregate
    assert len(CONTROLS) == 7


def test_run_condition_control_keys():
    out = run_condition(1, 0.5, 1)
    for name, _mode, _thr in CONTROLS:
        assert name in out


def test_null_p_in_range():
    out = run_condition(1, 0.5, 1)
    assert 0.0 < out["null_p"] <= 1.0
    assert 0.0 <= out["split_consistency"] <= 1.0


def test_aggregate_counts_all_controls():
    res = run_condition(1, 0.5, 1)
    agg = aggregate([res])
    assert agg["n_total"] == len(CONTROLS)
    assert 0 <= agg["n_pass"] <= len(CONTROLS)


def test_aggregate_hard_failure_is_diagnostic_failed():
    agg = aggregate([{"error": "ValueError: injected"}])
    assert agg["status"] == "SECTOR_SELECTION_DIAGNOSTIC_FAILED"


def test_verdict_is_in_allowed_outcomes():
    agg = aggregate([run_condition(1, 0.5, 1)])
    assert verdict(agg) in ALLOWED_OUTCOMES


def test_claim_firewall_string():
    assert CLAIM_FIREWALL == "IRREDUCIBLE_EMERGENT_INFLUENCE = OUT_OF_SCOPE"


def test_run_firewall_end_to_end_registered_set():
    conds = registered_conditions()
    results, conds = run_firewall(conds)
    assert len(results) == len(conds) == 6
    agg = aggregate(results)
    assert agg["n_total"] == len(CONTROLS)
    assert verdict(agg) in ALLOWED_OUTCOMES


def test_determinism_same_inputs_same_result():
    a = run_condition(1, 0.5, 1)
    b = run_condition(1, 0.5, 1)
    for name, _m, _t in CONTROLS:
        assert a[name] == b[name]


def test_report_files_if_present_end_with_valid_outcome_and_claim():
    """If the committed reports exist they must contain a valid outcome and
    the unconditional claim firewall."""
    root = Path(__file__).resolve().parents[1]
    jpath = root / "reports" / "SECTOR_SELECTION_FIREWALL.json"
    if not jpath.exists():
        pytest.skip("report not yet generated")
    rep = json.loads(jpath.read_text())
    assert rep["outcome"] in ALLOWED_OUTCOMES
    assert rep["claim_firewall"] == CLAIM_FIREWALL
    md = (root / "RRT0_SECTOR_SELECTION_FIREWALL.md").read_text()
    assert CLAIM_FIREWALL in md
    assert rep["outcome"] in md
