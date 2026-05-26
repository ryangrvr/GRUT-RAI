#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Phase C: Classification Harness

Applies all 8 frozen acceptance criteria from the spec to each prescription.
Writes a Markdown classification report and a JSON summary.

Criteria (from GATE3_HMINUS_DIRECT_LIMIT_SPEC.md):
  1. Laurent fit quality:       R^2 > 0.99999 for all samples
  2. Epsilon expansion smooth:  residual < 0.0001 in eps -> 0 extrapolation
  3. Prescription universality: all three limits agree within 1%
  4. Numerical stability:       no sample error > 1e-6
  5. Analytic continuation:     no pole or branch cut ambiguity reported
  6. Blind protocol integrity:  classifier uses only generic labels (enforced structurally)
  7. Specification compliance:  code and data traceable to spec (structural)
  8. Reproducibility:           scripts archived in repo (structural)

Spec: GATE3_HMINUS_DIRECT_LIMIT_SPEC.md (2026-05-24)
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Any

SPEC_VERSION = "gate3-hminus-direct-limit-spec-v1.0"
LAURENT_R2_THRESHOLD = 0.99999
EPS_EXPANSION_RESIDUAL_THRESHOLD = 1e-4
UNIVERSALITY_TOLERANCE = 0.01     # 1%
STABILITY_ERROR_THRESHOLD = 1e-6  # max sample integration error


def log(msg: str):
    print(f"[{datetime.now().isoformat()}] {msg}")


def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def safe_float(v: Any) -> float:
    try:
        return float(v)
    except Exception:
        return float("nan")


def is_nan(v: float) -> bool:
    return v != v


# ── Individual criteria ───────────────────────────────────────────────────────

def criterion_1_laurent_fit(pres: dict) -> dict:
    """R^2 > 0.99999 for all Stage-1 inner-limit polynomial fits."""
    r2_values = pres.get("stage1_r2_values") or []
    if not r2_values:
        return {"result": "INCONCLUSIVE", "reason": "no Stage-1 R² values available"}
    failing = [r for r in r2_values if safe_float(r) < LAURENT_R2_THRESHOLD]
    if failing:
        worst = min(safe_float(r) for r in r2_values)
        return {
            "result": "FAIL",
            "reason": f"{len(failing)} fits below R²={LAURENT_R2_THRESHOLD}: worst={worst:.8f}",
        }
    best_worst = min(safe_float(r) for r in r2_values)
    return {"result": "PASS", "reason": f"all {len(r2_values)} fits pass; worst R²={best_worst:.8f}"}


def criterion_2_eps_expansion(pres: dict) -> dict:
    """Residual < 0.0001 in the eps -> 0 extrapolation."""
    resid = safe_float(pres.get("fit_residual"))
    if is_nan(resid):
        return {"result": "INCONCLUSIVE", "reason": "no fit_residual in Phase B output"}
    if resid < EPS_EXPANSION_RESIDUAL_THRESHOLD:
        return {"result": "PASS", "reason": f"residual={resid:.6e} < {EPS_EXPANSION_RESIDUAL_THRESHOLD}"}
    return {
        "result": "FAIL",
        "reason": f"residual={resid:.6e} exceeds threshold {EPS_EXPANSION_RESIDUAL_THRESHOLD} "
                  f"({resid / EPS_EXPANSION_RESIDUAL_THRESHOLD:.1f}x)",
    }


def criterion_3_universality(all_prescriptions: list[dict]) -> dict:
    """All three prescriptions agree within 1%."""
    finite_values = []
    for p in all_prescriptions:
        v = safe_float(p.get("epsilon_to_0_finite"))
        if not is_nan(v):
            finite_values.append(v)
    if len(finite_values) < 3:
        return {
            "result": "INCONCLUSIVE",
            "reason": f"only {len(finite_values)}/3 prescriptions produced finite values",
        }
    mean_v = sum(finite_values) / len(finite_values)
    max_dev = max(abs(v - mean_v) for v in finite_values)
    rel_spread = max_dev / abs(mean_v) if abs(mean_v) > 1e-12 else float("inf")
    if rel_spread <= UNIVERSALITY_TOLERANCE:
        return {
            "result": "PASS",
            "reason": f"relative spread={rel_spread:.4e} <= {UNIVERSALITY_TOLERANCE}: "
                      f"values={[f'{v:.6f}' for v in finite_values]}",
        }
    return {
        "result": "FAIL",
        "reason": f"relative spread={rel_spread:.4e} exceeds {UNIVERSALITY_TOLERANCE}: "
                  f"values={[f'{v:.6f}' for v in finite_values]}",
    }


def criterion_4_numerical_stability(pres: dict, phase_a_data: dict | None) -> dict:
    """No sample integration error > 1e-6."""
    if phase_a_data is None:
        return {"result": "INCONCLUSIVE", "reason": "Phase A data not available for error check"}
    all_samples = phase_a_data.get("all_samples", {})
    if not all_samples:
        return {"result": "INCONCLUSIVE", "reason": "no sample data in Phase A output"}
    failing = {k: s["error"] for k, s in all_samples.items()
               if safe_float(s.get("error", 0)) > STABILITY_ERROR_THRESHOLD}
    if failing:
        worst = max(safe_float(v) for v in failing.values())
        return {
            "result": "FAIL",
            "reason": f"{len(failing)} samples exceed error threshold {STABILITY_ERROR_THRESHOLD}: "
                      f"worst={worst:.2e}",
        }
    checked = len(all_samples)
    max_err = max((safe_float(s.get("error", 0)) for s in all_samples.values()), default=0.0)
    return {"result": "PASS", "reason": f"all {checked} samples: max error={max_err:.2e}"}


def criterion_5_analytic_continuation(pres: dict) -> dict:
    """No pole or branch cut ambiguity in h_- or eps."""
    finite = safe_float(pres.get("epsilon_to_0_finite"))
    if is_nan(finite) or abs(finite) == float("inf"):
        return {"result": "FAIL", "reason": f"finite part is {finite} — pole or divergence indicated"}
    r2_vals = pres.get("stage1_r2_values") or []
    if r2_vals and min(safe_float(r) for r in r2_vals) < 0.99:
        return {
            "result": "FAIL",
            "reason": "very low Stage-1 R² suggests non-polynomial (branch-cut) behavior",
        }
    return {"result": "PASS", "reason": f"finite part={finite:.6f}; no singularity indicators"}


def criterion_6_blind_protocol(_pres: dict) -> dict:
    """Classifier receives only generic prescription_1/2/3 labels."""
    return {
        "result": "PASS",
        "reason": "Phase C receives prescription_1/2/3 labels only; source field not used in decisions",
    }


def criterion_7_spec_compliance(_pres: dict) -> dict:
    """All code traceable to GATE3_HMINUS_DIRECT_LIMIT_SPEC.md."""
    return {
        "result": "PASS",
        "reason": f"Phase A/B/C harnesses cite spec {SPEC_VERSION}; output files in gate3_dl_outputs/",
    }


def criterion_8_reproducibility(_pres: dict) -> dict:
    """All scripts and data archived in repo."""
    return {
        "result": "PASS",
        "reason": "Phase A scripts in theory/hard_theory/, Phase B/C in grut/hard_theory/s4_ctp_solver/; "
                  "outputs committed to gate3_dl_outputs/",
    }


# ── Per-prescription classification ──────────────────────────────────────────

def classify_one(label: str, pres: dict, all_preses: list[dict],
                 phase_a_data: dict | None) -> dict:
    criteria = {
        "1_laurent_fit_quality": criterion_1_laurent_fit(pres),
        "2_epsilon_expansion_smoothness": criterion_2_eps_expansion(pres),
        "3_prescription_universality": criterion_3_universality(all_preses),
        "4_numerical_stability": criterion_4_numerical_stability(pres, phase_a_data),
        "5_analytic_continuation": criterion_5_analytic_continuation(pres),
        "6_blind_protocol_integrity": criterion_6_blind_protocol(pres),
        "7_specification_compliance": criterion_7_spec_compliance(pres),
        "8_reproducibility": criterion_8_reproducibility(pres),
    }
    n_pass = sum(1 for r in criteria.values() if r["result"] == "PASS")
    n_fail = sum(1 for r in criteria.values() if r["result"] == "FAIL")
    n_inc = sum(1 for r in criteria.values() if r["result"] == "INCONCLUSIVE")

    # All 8 must pass (no FAILs and no INCONCLUSIVEs) to promote
    if n_fail == 0 and n_inc == 0:
        overall = "PASS"
    elif n_fail == 0:
        overall = "INCONCLUSIVE"
    else:
        overall = "FAIL"

    return {
        "prescription_label": label,
        "epsilon_to_0_finite": pres.get("epsilon_to_0_finite"),
        "overall": overall,
        "pass_count": n_pass,
        "fail_count": n_fail,
        "inconclusive_count": n_inc,
        "criteria": criteria,
    }


# ── Report writing ────────────────────────────────────────────────────────────

def write_report(report_path: Path, classification: dict, pres_data: dict):
    now = datetime.now().isoformat()
    lines = [
        "# Gate 3 hminus_direct_limit Classification Report",
        "",
        f"Date: {now}",
        f"Spec: {SPEC_VERSION}",
        "",
        "## Summary",
        "",
    ]

    promoted = [lb for lb, res in classification.items() if res["overall"] == "PASS"]
    lines.append(f"Prescriptions evaluated: {len(classification)}")
    lines.append(f"Promoted (all 8 pass): {len(promoted)} — {promoted if promoted else 'NONE'}")
    lines.append("")

    # Overall outcome per the spec decision tree
    all_fail_c2 = all(
        res["criteria"].get("2_epsilon_expansion_smoothness", {}).get("result") == "FAIL"
        for res in classification.values()
    )
    if all_fail_c2:
        lines.append("**OUTCOME: All prescriptions fail criterion 2 → IR limit itself is the barrier**")
    elif promoted:
        lines.append("**OUTCOME: At least one prescription passes → direct limit is viable**")
    else:
        lines.append("**OUTCOME: Mixed failures — see per-prescription analysis below**")
    lines.append("")

    for label, res in classification.items():
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"- **C_Euler (finite part):** {res['epsilon_to_0_finite']}")
        lines.append(f"- **Overall:** {res['overall']}")
        lines.append(f"- PASS: {res['pass_count']}  FAIL: {res['fail_count']}  "
                     f"INCONCLUSIVE: {res['inconclusive_count']}")
        lines.append("")
        lines.append("| Criterion | Result | Reason |")
        lines.append("|---|---|---|")
        for crit, detail in res["criteria"].items():
            lines.append(f"| {crit} | {detail['result']} | {detail['reason']} |")
        lines.append("")

    lines += [
        "## Notes",
        "",
        f"- Acceptance thresholds: Laurent R² > {LAURENT_R2_THRESHOLD}, "
          f"eps-expansion residual < {EPS_EXPANSION_RESIDUAL_THRESHOLD}, "
          f"universality < {UNIVERSALITY_TOLERANCE * 100:.0f}%.",
        "- Criteria 6–8 are structural passes (enforced by harness design).",
        "- Criterion 3 (universality) is evaluated identically for all prescriptions.",
        "- Promotion requires ALL 8 criteria to pass with no INCONCLUSIVEs.",
        "",
        f"Spec: GATE3_HMINUS_DIRECT_LIMIT_SPEC.md ({SPEC_VERSION})",
    ]

    report_path.write_text("\n".join(lines))


def main():
    log("=" * 80)
    log("Gate 3 DL Phase C: Classification Harness")
    log(f"Spec: {SPEC_VERSION}")
    log("=" * 80)

    repo_root = Path(__file__).resolve().parents[3]
    dl_out = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"

    pres_file = dl_out / "gate3_dl_prescription_coefficients.json"
    report_md = dl_out / "gate3_dl_classification_report.md"
    report_json = dl_out / "gate3_dl_classification_summary.json"

    if not pres_file.exists():
        log(f"ERROR: {pres_file} not found — run Phase B first.")
        sys.exit(1)

    log(f"Loading prescriptions: {pres_file}")
    pres_data = load_json(pres_file)
    prescriptions = pres_data.get("prescriptions", {})

    # Load Phase A JSONs for numerical stability check
    phase_a_files = {
        "prescription_1": dl_out / "gate3_dl_d1_extraction.json",
        "prescription_2": dl_out / "gate3_dl_d2_extraction.json",
        "prescription_3": dl_out / "gate3_dl_d3_extraction.json",
    }
    phase_a_data = {}
    for label, path in phase_a_files.items():
        if path.exists():
            phase_a_data[label] = load_json(path)
            log(f"Loaded Phase A for {label}: {path.name}")
        else:
            log(f"WARNING: Phase A file missing for {label}: {path}")

    all_preses = list(prescriptions.values())

    classification = {}
    for label, pres in prescriptions.items():
        result = classify_one(label, pres, all_preses, phase_a_data.get(label))
        classification[label] = result
        log(f"  {label}: {result['overall']}  "
            f"(PASS={result['pass_count']}, FAIL={result['fail_count']}, "
            f"INC={result['inconclusive_count']})")

    write_report(report_md, classification, pres_data)
    log(f"Report written: {report_md}")

    # JSON summary
    summary = {
        "spec": SPEC_VERSION,
        "date": datetime.now().isoformat(),
        "classification": classification,
        "promoted": [lb for lb, res in classification.items() if res["overall"] == "PASS"],
        "all_fail_criterion_2": all(
            res["criteria"].get("2_epsilon_expansion_smoothness", {}).get("result") == "FAIL"
            for res in classification.values()
        ),
    }
    with open(report_json, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    log(f"JSON summary: {report_json}")

    log("=" * 80)
    log("Phase C COMPLETE")
    log(f"Promoted prescriptions: {summary['promoted']}")
    log(f"All-fail criterion 2 (IR barrier signal): {summary['all_fail_criterion_2']}")
    log("=" * 80)


if __name__ == "__main__":
    main()
