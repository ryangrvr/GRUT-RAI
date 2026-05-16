"""Write schema-compliant blocked Gate 3 coefficient JSON artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional


def _blocked_payload(
    coefficient_name: str,
    blocker: str,
    source_file: Optional[str],
    m2_over_h2: Optional[str] = None,
    regulator_role: Optional[str] = None,
) -> Dict[str, object]:
    payload = {
        "coefficient_name": coefficient_name,
        "value": None,
        "epsilon_pole": None,
        "finite_part": None,
        "scheme": "round_s4_euler_dimreg",
        "regulator": "D=4-2epsilon",
        "channel": "Euler",
        "projection": "round_s4_euler",
        "protected": True,
        "source_tool": "blocked_preflight",
        "source_file": source_file,
        "manual_target_matching": False,
        "status": "blocked",
        "blocker": blocker,
    }
    # Add regulator metadata if provided
    if m2_over_h2 is not None:
        payload["m2_over_h2"] = m2_over_h2
    if regulator_role is not None:
        payload["regulator_role"] = regulator_role
    return payload


def write_gate3_blocked_outputs(
    *,
    output_dir: str,
    blocker: str,
    source_file: Optional[str] = None,
    m2_over_h2: Optional[str] = None,
    regulator_role: Optional[str] = None,
) -> List[str]:
    """Write blocked JSONs for C_Euler_cosmo and C_Euler_final."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    paths: List[str] = []
    for coefficient in ("C_Euler_cosmo", "C_Euler_final"):
        payload = _blocked_payload(
            coefficient,
            blocker,
            source_file,
            m2_over_h2=m2_over_h2,
            regulator_role=regulator_role,
        )
        path = out / f"{coefficient}.json"
        path.write_text(json.dumps(payload, indent=2))
        paths.append(str(path))
    return paths


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Write blocked Gate 3 output JSON files.")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--blocker", required=True)
    parser.add_argument("--source-file", default=None)
    parser.add_argument("--m2-over-h2", default=None, help="Regulator parameter m^2/H^2 (optional)")
    parser.add_argument("--regulator-role", default=None, help="Regulator role annotation (optional)")
    args = parser.parse_args()

    written = write_gate3_blocked_outputs(
        output_dir=args.output_dir,
        blocker=args.blocker,
        source_file=args.source_file,
        m2_over_h2=args.m2_over_h2,
        regulator_role=args.regulator_role,
    )
    for p in written:
        print(p)
