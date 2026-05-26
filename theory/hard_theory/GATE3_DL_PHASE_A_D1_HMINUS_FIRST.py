#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Phase A-D1: Sequential Limit (h_- first, then epsilon)

Prescription D1:
  Stage 1: For each epsilon in eps_outer, compute I(h_-, eps) on a fine h_- grid
           near 0. Fit polynomial in h_- and extrapolate to h_- -> 0 -> I_D1(eps).
  Stage 2: Fit I_D1(eps) over eps_outer values and extrapolate to eps -> 0 -> C_Euler_D1.

Acceptance criteria (from spec) evaluated here:
  - Laurent fit quality: R^2 of Stage 1 polynomial fit in h_-
  - Epsilon expansion smoothness: residual of Stage 2 extrapolation in eps

Spec: GATE3_HMINUS_DIRECT_LIMIT_SPEC.md (2026-05-24)
"""

import json
import numpy as np
from scipy.integrate import quad
from scipy.special import hyp2f1
from pathlib import Path
from datetime import datetime

SPEC_VERSION = "gate3-hminus-direct-limit-spec-v1.0"
SPEC_DATE = "2026-05-24"
PRESCRIPTION_LABEL = "D1_sequential_hminus_first"


def compute_integral(h_minus, eps):
    """
    I(h_-, eps) = 2 * 4^((D-3)/2) * integral_0^1
                  2F1(h_+, h_-; D/2; u)^3 * [u(1-u)]^((D-3)/2) du
    where h_+ = D-1, D = 4 - 2*eps.
    """
    D = 4.0 - 2.0 * eps
    hplus = D - 1.0
    prefactor = 2.0 * (4.0 ** ((D - 3.0) / 2.0))
    exp = (D - 3.0) / 2.0

    def integrand(u):
        if u <= 0.0 or u >= 1.0:
            return 0.0
        try:
            hyp = hyp2f1(hplus, h_minus, D / 2.0, u)
            return prefactor * (hyp ** 3) * (u ** exp) * ((1.0 - u) ** exp)
        except Exception:
            return 0.0

    result, error = quad(
        integrand, 0, 1,
        limit=200, epsabs=1e-20, epsrel=1e-15,
        points=[0.5]
    )
    return float(result), float(error)


def fit_and_extrapolate(x_data, y_data, degree, target=0.0):
    """
    Fit polynomial of given degree to (x_data, y_data).
    Return (value_at_target, r2, residual, poly_coeffs).
    residual = max absolute deviation from fit.
    """
    x = np.array(x_data, dtype=float)
    y = np.array(y_data, dtype=float)
    coeffs = np.polyfit(x, y, min(degree, len(x) - 1))
    y_pred = np.polyval(coeffs, x)
    ss_res = float(np.sum((y - y_pred) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 1.0
    residual = float(np.max(np.abs(y - y_pred)))
    value_at_target = float(np.polyval(coeffs, target))
    return value_at_target, r2, residual, [float(c) for c in coeffs]


def main():
    print("=" * 70)
    print("Gate 3 DL Phase A-D1: Sequential Limit (h_- first, then epsilon)")
    print(f"Spec:  {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 70)

    script_dir = Path(__file__).parent.absolute()
    output_dir = script_dir / "gate3_dl_outputs"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "gate3_dl_d1_extraction.json"

    # Outer grid: eps values for Stage 2 extrapolation (same as DR route)
    eps_outer = [0.01, 0.005, 0.002, 0.001]
    # Inner grid: h_- values for Stage 1 fitting (fine near 0)
    h_minus_inner = [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]

    total_samples = len(eps_outer) * len(h_minus_inner)
    print(f"Outer eps values:    {eps_outer}")
    print(f"Inner h_- values:    {h_minus_inner}")
    print(f"Total samples:       {total_samples}\n")

    all_samples = {}
    stage1_results = {}

    # ── Stage 1: h_- → 0 at each fixed eps ──────────────────────────────────
    print("Stage 1: h_- → 0 fits at each fixed epsilon")
    print("-" * 50)

    for eps in eps_outer:
        print(f"\n  eps = {eps}")
        h_data, I_data = [], []

        for h in h_minus_inner:
            val, err = compute_integral(h, eps)
            key = f"h{h:.6f}_e{eps:.6f}"
            all_samples[key] = {"h_minus": h, "eps": eps, "value": val, "error": err}
            if np.isfinite(val) and err < 1e-2:
                h_data.append(h)
                I_data.append(val)
                print(f"    h_- = {h:.5f}: I = {val:.10f}  err = {err:.2e}")
            elif np.isfinite(val):
                print(f"    h_- = {h:.5f}: EXCLUDED (err={err:.2e} > 1e-2)")
            else:
                print(f"    h_- = {h:.5f}: FAILED (non-finite)")

        if len(h_data) >= 3:
            # Degree-3 polynomial in h_-, consistent with DR route
            I_D1_eps, r2, resid, coeffs = fit_and_extrapolate(h_data, I_data, degree=3, target=0.0)
            print(f"    => I_D1(eps={eps}) = {I_D1_eps:.10f}  R² = {r2:.8f}  resid = {resid:.2e}")
            stage1_results[str(eps)] = {
                "eps": eps,
                "I_D1": I_D1_eps,
                "fit_r2": r2,
                "fit_residual": resid,
                "poly_coeffs": coeffs,
                "h_data": h_data,
                "I_data": [float(v) for v in I_data],
                "n_samples": len(h_data),
            }
        else:
            print(f"    => INSUFFICIENT DATA ({len(h_data)} samples)")
            stage1_results[str(eps)] = {"eps": eps, "error": "insufficient_data"}

    # ── Stage 2: eps → 0 extrapolation from I_D1(eps) sequence ──────────────
    print("\nStage 2: eps → 0 extrapolation")
    print("-" * 50)

    eps_seq, I_D1_seq, stage1_r2_seq = [], [], []
    for eps in eps_outer:
        res = stage1_results.get(str(eps), {})
        if "I_D1" in res:
            eps_seq.append(eps)
            I_D1_seq.append(res["I_D1"])
            stage1_r2_seq.append(res.get("fit_r2", 0.0))

    stage2 = {
        "eps_sequence": eps_seq,
        "I_D1_sequence": I_D1_seq,
        "stage1_min_r2": float(min(stage1_r2_seq)) if stage1_r2_seq else None,
        "C_Euler_D1": None,
        "fit_r2": None,
        "fit_residual": None,
        "poly_coeffs": None,
    }

    if len(eps_seq) >= 2:
        C_Euler_D1, r2_s2, resid_s2, coeffs_s2 = fit_and_extrapolate(
            eps_seq, I_D1_seq, degree=min(len(eps_seq) - 1, 2), target=0.0
        )
        stage2["C_Euler_D1"] = C_Euler_D1
        stage2["fit_r2"] = r2_s2
        stage2["fit_residual"] = resid_s2
        stage2["poly_coeffs"] = coeffs_s2
        print(f"  C_Euler_D1 = {C_Euler_D1:.10f}")
        print(f"  R²         = {r2_s2:.8f}")
        print(f"  residual   = {resid_s2:.6e}")
        print(f"  Stage-1 min R² = {stage2['stage1_min_r2']:.8f}")
    else:
        print("  INSUFFICIENT Stage-1 results for Stage-2 extrapolation")

    output = {
        "spec": SPEC_VERSION,
        "spec_date": SPEC_DATE,
        "prescription": PRESCRIPTION_LABEL,
        "date": datetime.now().isoformat(),
        "eps_outer": eps_outer,
        "h_minus_inner": h_minus_inner,
        "total_samples_attempted": total_samples,
        "successful_samples": len([s for s in all_samples.values() if np.isfinite(s["value"])]),
        "all_samples": all_samples,
        "stage1_results": stage1_results,
        "stage2": stage2,
    }

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput: {output_file}  ({output_file.stat().st_size} bytes)")
    print("=" * 70)
    print("Phase A-D1 COMPLETE")
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
