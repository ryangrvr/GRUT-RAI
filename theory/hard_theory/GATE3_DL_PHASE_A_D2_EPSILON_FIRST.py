#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Phase A-D2: Sequential Limit (epsilon first, then h_-)

Prescription D2:
  Stage 1: For each h_- in h_minus_outer, compute I(h_-, eps) on a fine eps grid
           near 0. Fit polynomial in eps and extrapolate to eps -> 0 -> I_D2(h_-).
  Stage 2: Fit I_D2(h_-) over h_minus_outer values and extrapolate to h_- -> 0
           -> C_Euler_D2.

Key diagnostic: if I(h_-, eps) diverges as eps -> 0 at fixed h_- > 0, the Stage 1
fit quality will degrade and/or the fit_residual will exceed the threshold, providing
direct evidence that eps -> 0 at fixed h_- is the structural barrier.

Acceptance criteria (from spec) evaluated here:
  - Laurent fit quality: R^2 of Stage 1 polynomial fit in eps
  - Epsilon expansion smoothness: residual of Stage 1 eps -> 0 extrapolation

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
PRESCRIPTION_LABEL = "D2_sequential_epsilon_first"


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
    print("Gate 3 DL Phase A-D2: Sequential Limit (epsilon first, then h_-)")
    print(f"Spec:  {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 70)

    script_dir = Path(__file__).parent.absolute()
    output_dir = script_dir / "gate3_dl_outputs"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "gate3_dl_d2_extraction.json"

    # Outer grid: h_- values for Stage 2 extrapolation
    h_minus_outer = [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    # Inner grid: eps values for Stage 1 fitting (extended toward 0 to probe divergence)
    eps_inner = [0.02, 0.01, 0.005, 0.002, 0.001, 0.0005]

    total_samples = len(h_minus_outer) * len(eps_inner)
    print(f"Outer h_- values:    {h_minus_outer}")
    print(f"Inner eps values:    {eps_inner}")
    print(f"Total samples:       {total_samples}\n")

    all_samples = {}
    stage1_results = {}

    # ── Stage 1: eps → 0 at each fixed h_- ───────────────────────────────────
    print("Stage 1: eps → 0 fits at each fixed h_-")
    print("-" * 50)

    for h in h_minus_outer:
        print(f"\n  h_- = {h}")
        eps_data, I_data = [], []

        for eps in eps_inner:
            val, err = compute_integral(h, eps)
            key = f"h{h:.6f}_e{eps:.6f}"
            all_samples[key] = {"h_minus": h, "eps": eps, "value": val, "error": err}
            if np.isfinite(val) and err < 1e-2:
                eps_data.append(eps)
                I_data.append(val)
                print(f"    eps = {eps:.5f}: I = {val:.10f}  err = {err:.2e}")
            elif np.isfinite(val):
                print(f"    eps = {eps:.5f}: EXCLUDED (err={err:.2e} > 1e-2)")
            else:
                print(f"    eps = {eps:.5f}: FAILED (non-finite)")

        if len(eps_data) >= 3:
            I_D2_h, r2, resid, coeffs = fit_and_extrapolate(eps_data, I_data, degree=3, target=0.0)
            print(f"    => I_D2(h_-={h}) = {I_D2_h:.10f}  R² = {r2:.8f}  resid = {resid:.2e}")
            stage1_results[str(h)] = {
                "h_minus": h,
                "I_D2": I_D2_h,
                "fit_r2": r2,
                "fit_residual": resid,
                "poly_coeffs": coeffs,
                "eps_data": eps_data,
                "I_data": [float(v) for v in I_data],
                "n_samples": len(eps_data),
            }
        else:
            print(f"    => INSUFFICIENT DATA ({len(eps_data)} samples)")
            stage1_results[str(h)] = {"h_minus": h, "error": "insufficient_data"}

    # ── Stage 2: h_- → 0 extrapolation from I_D2(h_-) sequence ──────────────
    print("\nStage 2: h_- → 0 extrapolation")
    print("-" * 50)

    h_seq, I_D2_seq, stage1_r2_seq, stage1_resid_seq = [], [], [], []
    for h in h_minus_outer:
        res = stage1_results.get(str(h), {})
        if "I_D2" in res:
            h_seq.append(h)
            I_D2_seq.append(res["I_D2"])
            stage1_r2_seq.append(res.get("fit_r2", 0.0))
            stage1_resid_seq.append(res.get("fit_residual", float("nan")))

    stage2 = {
        "h_sequence": h_seq,
        "I_D2_sequence": I_D2_seq,
        "stage1_min_r2": float(min(stage1_r2_seq)) if stage1_r2_seq else None,
        "stage1_max_residual": float(max(stage1_resid_seq)) if stage1_resid_seq else None,
        "C_Euler_D2": None,
        "fit_r2": None,
        "fit_residual": None,
        "poly_coeffs": None,
    }

    if len(h_seq) >= 2:
        C_Euler_D2, r2_s2, resid_s2, coeffs_s2 = fit_and_extrapolate(
            h_seq, I_D2_seq, degree=min(len(h_seq) - 1, 2), target=0.0
        )
        stage2["C_Euler_D2"] = C_Euler_D2
        stage2["fit_r2"] = r2_s2
        stage2["fit_residual"] = resid_s2
        stage2["poly_coeffs"] = coeffs_s2
        print(f"  C_Euler_D2 = {C_Euler_D2:.10f}")
        print(f"  R²         = {r2_s2:.8f}")
        print(f"  residual   = {resid_s2:.6e}")
        print(f"  Stage-1 min R²        = {stage2['stage1_min_r2']:.8f}")
        print(f"  Stage-1 max residual  = {stage2['stage1_max_residual']:.6e}")
    else:
        print("  INSUFFICIENT Stage-1 results for Stage-2 extrapolation")

    output = {
        "spec": SPEC_VERSION,
        "spec_date": SPEC_DATE,
        "prescription": PRESCRIPTION_LABEL,
        "date": datetime.now().isoformat(),
        "h_minus_outer": h_minus_outer,
        "eps_inner": eps_inner,
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
    print("Phase A-D2 COMPLETE")
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
