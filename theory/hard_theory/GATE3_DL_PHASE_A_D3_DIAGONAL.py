#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Phase A-D3: Diagonal Limit (h_- = c * epsilon -> 0)

Prescription D3:
  For each coupling ratio c in c_values, compute I(c*eps, eps) at decreasing eps
  values, fit polynomial in eps, and extrapolate to eps -> 0 -> I_D3(c).
  Then check whether I_D3(c) is c-independent (universality check).
  C_Euler_D3 = mean of I_D3(c) values if c-independent, else INCONCLUSIVE.

Key diagnostic: if the limit is path-independent, I_D3(c) is constant across c
values, confirming the two-variable limit (h_-, eps) -> (0,0) is well-defined.
If I_D3(c) varies significantly with c, the limit does not exist uniformly.

Note: as eps -> 0 along h_- = c*eps, the hypergeometric argument h_- = c*eps -> 0
simultaneously, so 2F1(h_+, c*eps; D/2; u) -> 2F1(3, 0; 2; u) = 1 for any c.
This makes D3 qualitatively similar to D1 in the simultaneous-limit regime, but
tests whether the rate of approach matters.

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
PRESCRIPTION_LABEL = "D3_diagonal_limit"


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
    print("Gate 3 DL Phase A-D3: Diagonal Limit (h_- = c * eps -> 0)")
    print(f"Spec:  {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 70)

    script_dir = Path(__file__).parent.absolute()
    output_dir = script_dir / "gate3_dl_outputs"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "gate3_dl_d3_extraction.json"

    # Coupling ratios to probe (span two decades: c = h_- / eps)
    c_values = [0.1, 0.5, 1.0, 2.0, 5.0]
    # eps decreasing sequence for each diagonal
    eps_values = [0.02, 0.01, 0.005, 0.002, 0.001]

    total_samples = len(c_values) * len(eps_values)
    print(f"c values (h_-/eps): {c_values}")
    print(f"eps values:         {eps_values}")
    print(f"Total samples:      {total_samples}\n")

    all_samples = {}
    diagonal_results = {}

    # ── Per-diagonal fits: eps -> 0 along h_- = c*eps ────────────────────────
    print("Per-diagonal fits: eps -> 0 along each h_- = c*eps path")
    print("-" * 50)

    for c in c_values:
        print(f"\n  c = {c} (h_- = {c}*eps)")
        eps_data, I_data = [], []

        for eps in eps_values:
            h = c * eps
            val, err = compute_integral(h, eps)
            key = f"c{c:.3f}_e{eps:.6f}"
            all_samples[key] = {
                "c": c, "eps": eps, "h_minus": h,
                "value": val, "error": err
            }
            if np.isfinite(val) and err < 1e-2:
                eps_data.append(eps)
                I_data.append(val)
                print(f"    eps = {eps:.5f}  h_- = {h:.6f}: I = {val:.10f}  err = {err:.2e}")
            elif np.isfinite(val):
                print(f"    eps = {eps:.5f}  h_- = {h:.6f}: EXCLUDED (err={err:.2e} > 1e-2)")
            else:
                print(f"    eps = {eps:.5f}  h_- = {h:.6f}: FAILED (non-finite)")

        if len(eps_data) >= 3:
            I_D3_c, r2, resid, coeffs = fit_and_extrapolate(eps_data, I_data, degree=3, target=0.0)
            print(f"    => I_D3(c={c}) = {I_D3_c:.10f}  R² = {r2:.8f}  resid = {resid:.2e}")
            diagonal_results[str(c)] = {
                "c": c,
                "I_D3": I_D3_c,
                "fit_r2": r2,
                "fit_residual": resid,
                "poly_coeffs": coeffs,
                "eps_data": eps_data,
                "I_data": [float(v) for v in I_data],
                "n_samples": len(eps_data),
            }
        else:
            print(f"    => INSUFFICIENT DATA ({len(eps_data)} samples)")
            diagonal_results[str(c)] = {"c": c, "error": "insufficient_data"}

    # ── Universality check and C_Euler_D3 ────────────────────────────────────
    print("\nUniversality check")
    print("-" * 50)

    I_D3_values = []
    for c in c_values:
        res = diagonal_results.get(str(c), {})
        if "I_D3" in res:
            I_D3_values.append(res["I_D3"])

    universality = {}
    C_Euler_D3 = None

    if len(I_D3_values) >= 2:
        mean_val = float(np.mean(I_D3_values))
        max_dev = float(np.max(np.abs(np.array(I_D3_values) - mean_val)))
        rel_spread = max_dev / abs(mean_val) if abs(mean_val) > 1e-12 else float("inf")
        C_Euler_D3 = mean_val
        universality = {
            "I_D3_values": I_D3_values,
            "mean": mean_val,
            "max_absolute_deviation": max_dev,
            "relative_spread": rel_spread,
            "c_independent": bool(rel_spread < 0.01),
        }
        print(f"  I_D3 values:        {[f'{v:.8f}' for v in I_D3_values]}")
        print(f"  Mean:               {mean_val:.10f}")
        print(f"  Max abs deviation:  {max_dev:.6e}")
        print(f"  Relative spread:    {rel_spread:.6e}")
        print(f"  c-independent (<1%): {universality['c_independent']}")
        if not universality["c_independent"]:
            print("  WARNING: I_D3 varies with c — limit is path-dependent")
    else:
        print("  INSUFFICIENT diagonal results for universality check")

    output = {
        "spec": SPEC_VERSION,
        "spec_date": SPEC_DATE,
        "prescription": PRESCRIPTION_LABEL,
        "date": datetime.now().isoformat(),
        "c_values": c_values,
        "eps_values": eps_values,
        "total_samples_attempted": total_samples,
        "successful_samples": len([s for s in all_samples.values() if np.isfinite(s["value"])]),
        "all_samples": all_samples,
        "diagonal_results": diagonal_results,
        "universality": universality,
        "C_Euler_D3": C_Euler_D3,
    }

    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput: {output_file}  ({output_file.stat().st_size} bytes)")
    print("=" * 70)
    print("Phase A-D3 COMPLETE")
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
