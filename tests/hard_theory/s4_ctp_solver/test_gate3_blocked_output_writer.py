import json
from pathlib import Path

from grut.hard_theory.s4_ctp_solver.gate3_blocked_output_writer import (
    write_gate3_blocked_outputs,
)
from grut.hard_theory.s4_ctp_solver.gate3_import_and_classify import (
    run_gate3_import_and_classify,
)
from grut.hard_theory.s4_ctp_solver.gate3_mathematica_import import (
    import_mathematica_coefficient,
)


def test_blocked_writer_creates_schema_compliant_json(tmp_path: Path) -> None:
    written = write_gate3_blocked_outputs(
        output_dir=str(tmp_path),
        blocker="test blocker",
        source_file="test_source.wl",
    )
    assert len(written) == 2

    for path in written:
        payload = json.loads(Path(path).read_text())
        assert payload["status"] == "blocked"
        assert payload["value"] is None
        assert payload["epsilon_pole"] is None
        assert payload["finite_part"] is None
        assert payload["manual_target_matching"] is False
        assert payload["channel"] == "Euler"
        assert payload["projection"] == "round_s4_euler"


def test_blocked_output_imports_successfully_as_blocked(tmp_path: Path) -> None:
    write_gate3_blocked_outputs(
        output_dir=str(tmp_path),
        blocker="blocked fixture",
        source_file="test_source.wl",
    )
    out = import_mathematica_coefficient(str(tmp_path / "C_Euler_cosmo.json"))
    assert out["accepted"] is True
    assert out["result"].status == "blocked"


def test_blocked_outputs_classify_as_blocked_not_computed(tmp_path: Path) -> None:
    write_gate3_blocked_outputs(
        output_dir=str(tmp_path),
        blocker="blocked fixture",
        source_file="test_source.wl",
    )
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(tmp_path / "C_Euler_cosmo.json"),
        final_json_path=str(tmp_path / "C_Euler_final.json"),
    )
    assert out["classification"]["classification"] == "blocked"


def test_missing_finite_part_allowed_only_when_blocked(tmp_path: Path) -> None:
    write_gate3_blocked_outputs(
        output_dir=str(tmp_path),
        blocker="blocked fixture",
        source_file="test_source.wl",
    )
    payload = json.loads((tmp_path / "C_Euler_final.json").read_text())
    assert payload["status"] == "blocked"
    assert payload["finite_part"] is None
