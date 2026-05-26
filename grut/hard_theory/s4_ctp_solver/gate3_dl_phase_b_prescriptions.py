#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Phase B: Prescription Application (Blind)

Reads the three Phase A extraction JSONs (D1, D2, D3) and emits a single
prescription_coefficients JSON with blind labels prescription_1/2/3.
The mapping (D1->1, D2->2, D3->3) is intentionally kept here but the
classifier in Phase C must not use it — Phase C receives only generic labels.

Outputs: gate3_dl_prescription_coefficients.json

Spec: GATE3_HMINUS_DIRECT_LIMIT_SPEC.md (2026-05-24)
"""

import json
import sys
from pathlib import Path
from datetime import datetime


def log(msg: str):
    print(f"[{datetime.now().isoformat()}] {msg}")


def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def summarize_d1(d: dict) -> dict:
    """Extract prescription summary from D1 extraction JSON."""
    s2 = d.get("stage2", {})
    C = s2.get("C_Euler_D1")
    r2 = s2.get("fit_r2")
    resid = s2.get("fit_residual")
    stage1_min_r2 = s2.get("stage1_min_r2")

    # Collect all Stage-1 fit residuals for criterion 1
    stage1 = d.get("stage1_results", {})
    stage1_r2_values = [v.get("fit_r2") for v in stage1.values() if "fit_r2" in v]
    stage1_resid_values = [v.get("fit_residual") for v in stage1.values() if "fit_residual" in v]

    return {
        "prescription_label": "prescription_1",
        "source": "D1_sequential_hminus_first",
        "epsilon_to_0_finite": C,
        "epsilon_to_0_pole": 0.0,
        "stage1_min_r2": stage1_min_r2,
        "stage1_r2_values": stage1_r2_values,
        "stage1_max_residual": max(stage1_resid_values) if stage1_resid_values else None,
        "stage2_r2": r2,
        "fit_residual": resid,
        "expansion_terms": [C, 0.0, 0.0] if C is not None else None,
        "extrapolation_method": "sequential_h_minus_first_then_eps",
    }


def summarize_d2(d: dict) -> dict:
    """Extract prescription summary from D2 extraction JSON."""
    s2 = d.get("stage2", {})
    C = s2.get("C_Euler_D2")
    r2 = s2.get("fit_r2")
    resid = s2.get("fit_residual")

    # Stage-1 fit quality (eps -> 0 extrapolations at each h_-)
    stage1 = d.get("stage1_results", {})
    stage1_r2_values = [v.get("fit_r2") for v in stage1.values() if "fit_r2" in v]
    stage1_resid_values = [v.get("fit_residual") for v in stage1.values() if "fit_residual" in v]

    # For criterion 2 ("eps → 0 smoothness"), the relevant residual is from Stage 1
    # (the eps → 0 extrapolation at each fixed h_-).  Stage 2 is h_- → 0, not eps → 0.
    stage1_max_resid = s2.get("stage1_max_residual")  # max over all h_- values

    return {
        "prescription_label": "prescription_2",
        "source": "D2_sequential_epsilon_first",
        "epsilon_to_0_finite": C,
        "epsilon_to_0_pole": 0.0,
        "stage1_min_r2": s2.get("stage1_min_r2"),
        "stage1_r2_values": stage1_r2_values,
        "stage1_max_residual": stage1_max_resid,
        "stage1_eps_residuals": stage1_resid_values,
        "stage2_r2": r2,
        "stage2_fit_residual": resid,          # h_- → 0 smoothness (diagnostic only)
        "fit_residual": stage1_max_resid,      # eps → 0 smoothness (criterion 2)
        "expansion_terms": [C, 0.0, 0.0] if C is not None else None,
        "extrapolation_method": "sequential_eps_first_then_h_minus",
    }


def summarize_d3(d: dict) -> dict:
    """Extract prescription summary from D3 extraction JSON."""
    C = d.get("C_Euler_D3")
    u = d.get("universality", {})

    # Per-diagonal fit quality (criterion 1: Laurent R² of each eps→0 fit)
    diag = d.get("diagonal_results", {})
    diag_r2_values = [v.get("fit_r2") for v in diag.values() if "fit_r2" in v]
    diag_resid_values = [v.get("fit_residual") for v in diag.values() if "fit_residual" in v]

    # For criterion 2 ("eps → 0 smoothness"), use the max per-diagonal eps→0 fit residual.
    # The universality deviation (how flat I_D3(c) is across c values) is diagnostic
    # for criterion 5 (analytic continuation) but is NOT the eps→0 residual.
    eps_to_0_max_residual = max(diag_resid_values) if diag_resid_values else None
    universality_residual = u.get("max_absolute_deviation")

    return {
        "prescription_label": "prescription_3",
        "source": "D3_diagonal_limit",
        "epsilon_to_0_finite": C,
        "epsilon_to_0_pole": 0.0,
        "diagonal_min_r2": min(diag_r2_values) if diag_r2_values else None,
        "diagonal_r2_values": diag_r2_values,
        "diagonal_max_residual": eps_to_0_max_residual,
        "stage1_min_r2": min(diag_r2_values) if diag_r2_values else None,
        "stage1_r2_values": diag_r2_values,
        "fit_residual": eps_to_0_max_residual,    # eps → 0 smoothness (criterion 2)
        "universality_residual": universality_residual,  # c-independence (diagnostic)
        "c_independent": u.get("c_independent"),
        "relative_spread": u.get("relative_spread"),
        "I_D3_values": u.get("I_D3_values"),
        "expansion_terms": [C, 0.0, 0.0] if C is not None else None,
        "extrapolation_method": "diagonal_h_minus_eq_c_eps",
    }


def main():
    log("=" * 80)
    log("Gate 3 DL Phase B: Prescription Application (Blind)")
    log("Spec: gate3-hminus-direct-limit-spec-v1.0")
    log("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]
    dl_out = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"

    d1_file = dl_out / "gate3_dl_d1_extraction.json"
    d2_file = dl_out / "gate3_dl_d2_extraction.json"
    d3_file = dl_out / "gate3_dl_d3_extraction.json"
    output_file = dl_out / "gate3_dl_prescription_coefficients.json"

    # Load Phase A outputs
    missing = [p for p in [d1_file, d2_file, d3_file] if not p.exists()]
    if missing:
        log(f"ERROR: Missing Phase A files: {missing}")
        log("Run all three Phase A scripts before Phase B.")
        sys.exit(1)

    log(f"Loading D1: {d1_file}")
    d1 = load_json(d1_file)
    log(f"  C_Euler_D1 = {d1.get('stage2', {}).get('C_Euler_D1')}")

    log(f"Loading D2: {d2_file}")
    d2 = load_json(d2_file)
    log(f"  C_Euler_D2 = {d2.get('stage2', {}).get('C_Euler_D2')}")

    log(f"Loading D3: {d3_file}")
    d3 = load_json(d3_file)
    log(f"  C_Euler_D3 = {d3.get('C_Euler_D3')}")

    # Build blind prescription summaries
    log("Applying blind prescription labels...")
    pres1 = summarize_d1(d1)
    pres2 = summarize_d2(d2)
    pres3 = summarize_d3(d3)

    for p in [pres1, pres2, pres3]:
        log(f"  {p['prescription_label']}: finite = {p['epsilon_to_0_finite']}, "
            f"fit_residual = {p['fit_residual']}, stage1_min_r2 = {p.get('stage1_min_r2')}")

    output = {
        "spec": "gate3-hminus-direct-limit-spec-v1.0",
        "spec_date": "2026-05-24",
        "phase_a_dates": {
            "D1": d1.get("date"),
            "D2": d2.get("date"),
            "D3": d3.get("date"),
        },
        "application_date": datetime.now().isoformat(),
        "prescriptions": {
            "prescription_1": pres1,
            "prescription_2": pres2,
            "prescription_3": pres3,
        },
        "note": (
            "Prescriptions labeled 1/2/3 (blind). "
            "Phase C classifier must not use source field before acceptance gating."
        ),
    }

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    log(f"Output written: {output_file}  ({output_file.stat().st_size} bytes)")
    log("=" * 80)
    log("Phase B COMPLETE")
    log("=" * 80)


if __name__ == "__main__":
    main()
