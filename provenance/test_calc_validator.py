#!/usr/bin/env python3
"""FAIL-forward pytest integration for calc/validate_calc_results.py.

Wires the shared calc result-JSON validator into the pytest suite. A
malformed artifact is a real test failure — never a skip.

Note: provenance/test_calc_result_schema.py already covers schema-shape
rules; this module covers the HARD rules (parseable JSON, non-empty
checks list, verdict present) by running the actual validator script and
asserting exit code 0.
"""
import json
import os
import subprocess
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
VALIDATOR = os.path.join(REPO, "calc", "validate_calc_results.py")


def test_validator_script_exists():
    assert os.path.isfile(VALIDATOR), "calc/validate_calc_results.py missing"


def test_validator_passes_on_current_repo_state():
    """FAIL-forward: validator exit code 0 means every calc/*_RESULT*.json
    is parseable JSON with a non-empty 'checks' list and a 'verdict'.
    Any malformed artifact surfaces as a test failure, not a skip."""
    r = subprocess.run(
        [sys.executable, VALIDATOR],
        capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 0, (
        f"calc result validation failed (exit {r.returncode}):\n"
        f"{r.stdout}\n{r.stderr}"
    )


def _run_validator_on(bad):
    """Load the validator module pointed at a specific artifact via the
    CALC_RESULT_DIR override, and capture its exit code and failures."""
    import importlib.util
    os.environ["CALC_RESULT_DIR"] = str(os.path.dirname(str(bad)))
    try:
        spec = importlib.util.spec_from_file_location(
            "validate_calc_results_test", VALIDATOR)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except SystemExit as exc:
            return exc.code, mod
        return 0, mod
    finally:
        os.environ.pop("CALC_RESULT_DIR", None)


def test_validator_catches_malformed_artifact(tmp_path):
    """The validator itself must fail loudly on a broken artifact —
    verify the FAIL-forward semantics with a deliberately corrupt file."""
    bad = tmp_path / "FAKE_RESULT.json"
    bad.write_text("{not json")
    code, mod = _run_validator_on(bad)
    assert code == 1, "validator must exit 1 on malformed input"
    assert mod.failures, "validator did not flag the malformed file"


def test_validator_catches_empty_checks(tmp_path):
    """A result with an empty checks list is not a result."""
    bad = tmp_path / "FAKE_RESULT.json"
    bad.write_text(json.dumps({"id": "x", "checks": [], "verdict": "v"}))
    code, mod = _run_validator_on(bad)
    assert code == 1
    assert any("checks" in f for f in mod.failures)


def test_validator_accepts_wellformed_artifact(tmp_path):
    good = tmp_path / "FAKE_RESULT.json"
    good.write_text(json.dumps({
        "id": "test_result", "title": "Test", "protocol": "p",
        "checks": [{"name": "c", "pass": True, "summary": "s"}],
        "verdict": "ok",
    }))
    code, mod = _run_validator_on(good)
    assert code == 0
    assert mod.failures == []
