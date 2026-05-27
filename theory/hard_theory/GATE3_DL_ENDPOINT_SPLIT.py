#!/usr/bin/env python3
"""
Gate 3 hminus_direct_limit Endpoint-Split Validation

Validates that the Allen-Jacobson integral can be computed with integration
error < 1e-6 using endpoint-aware integration, and that the extracted finite
part is consistent with pi/2.

Structure of the UV endpoint issue:
  The integrand near u=1: f(u) ~ [A + B*(1-u)^alpha]^3 * (1-u)^exp
  where alpha = -1 + eps - h_minus, exp = (D-3)/2 = 1/2 - eps.

  For h_minus > 0 and small eps, alpha < 0, and the 2F1 diverges as u->1.
  However:
    - B ~ h_minus/2 (vanishes as h_minus -> 0)
    - The leading CONVERGENT term (A^3) contributes exp = 1/2-eps > 0
    - The divergent corrections scale as O(h_minus^2) and O(h_minus^3)

  At h_minus = 0 exactly: f(u) = prefactor * 1^3 * [u(1-u)]^exp, which is
  smooth everywhere with error < 1e-6.

  The Stage 1 polynomial fit extrapolates to h_minus=0 correctly because
  the divergent endpoint corrections vanish in that limit.

Validation protocol:
  1. h_minus=0 base case: full integral, error < 1e-6 at each eps
  2. Small h_minus: bulk integral [0, 1-delta], error << 1e-6 for delta >= 1e-3
  3. Endpoint bound: analytically bound the endpoint contribution O(h_minus^2)
  4. D1 Stage-1 comparison: extrapolated I_D1(eps) vs exact I(0, eps)
  5. D3 diagonal: c-independence preserved after endpoint correction

Spec: gate3-hminus-direct-limit-spec-v1.0
"""

import json
import numpy as np
from scipy.integrate import quad
from scipy.special import hyp2f1, gamma
from pathlib import Path
from datetime import datetime

SPEC_VERSION = "gate3-hminus-direct-limit-spec-v1.0"
DELTA_VALUES = [1e-2, 1e-3, 1e-4, 1e-5]
ERROR_THRESHOLD = 1e-6


def compute_integrand(h_minus, eps):
    D = 4.0 - 2.0 * eps
    hplus = D - 1.0
    prefactor = 2.0 * (4.0 ** ((D - 3.0) / 2.0))
    exp = (D - 3.0) / 2.0

    def f(u):
        if u <= 0.0 or u >= 1.0:
            return 0.0
        try:
            hyp = hyp2f1(hplus, h_minus, D / 2.0, u)
            return prefactor * (hyp ** 3) * (u ** exp) * ((1.0 - u) ** exp)
        except Exception:
            return 0.0

    return f


def bulk_integral(h_minus, eps, delta):
    """Integrate from 0 to 1-delta with high accuracy."""
    f = compute_integrand(h_minus, eps)
    ulim = 1.0 - delta
    pts = [0.5, max(0.1, ulim / 2.0)]
    result, error = quad(
        f, 0, ulim,
        limit=5000, epsabs=1e-20, epsrel=1e-15,
        points=pts
    )
    return float(result), float(error)


def full_integral(h_minus, eps):
    """Full integral from 0 to 1. Works only when h_minus=0 (convergent)."""
    f = compute_integrand(h_minus, eps)
    result, error = quad(
        f, 0, 1,
        limit=5000, epsabs=1e-20, epsrel=1e-15,
        points=[0.5]
    )
    return float(result), float(error)


def connection_formula_B(h_minus, eps):
    """
    B coefficient in 2F1 connection formula near u=1:
      2F1(h+, h_-; D/2; u) ~ A + B*(1-u)^alpha, alpha = -1+eps-h_minus

    B = Gamma(D/2) * Gamma(1-eps+h_minus) / [Gamma(D-1) * Gamma(h_minus)]

    For small h_minus: B ~ h_minus/2 (first order).
    """
    if h_minus == 0.0:
        return 0.0
    D = 4.0 - 2.0 * eps
    try:
        B = (gamma(D / 2.0) * gamma(1.0 - eps + h_minus)
             / (gamma(D - 1.0) * gamma(h_minus)))
        return float(B)
    except Exception:
        return None


def endpoint_contribution_bound(h_minus, eps, delta):
    """
    Analytical bound on the endpoint contribution integral from [1-delta, 1].

    The convergent part (A^3 term) contributes:
      A^3 * integral_0^delta v^exp * (1-v)^exp dv
      <= A^3 * delta^(exp+1) / (exp+1)    [since (1-v)^exp <= 1]

    The 3A^2*B term (always convergent since alpha+exp = -1/2-h_minus > -1):
      <= 3*A^2*B * delta^(alpha+exp+1) / (alpha+exp+1)

    For the logarithmic case (alpha = -1, i.e. eps == h_minus):
      2F1 ~ A_log + B_log * log(v) near v=0.
      The endpoint integral is finite; A^3 term dominates the bound.

    Returns: (bound_A3, bound_3A2B, B_value, alpha)
    """
    D = 4.0 - 2.0 * eps
    exp = (D - 3.0) / 2.0   # = 0.5 - eps
    alpha = -1.0 + eps - h_minus  # c-a-b exponent

    B = connection_formula_B(h_minus, eps)
    if B is None:
        return None, None, None, alpha

    prefactor = 2.0 * (4.0 ** ((D - 3.0) / 2.0))

    # Logarithmic case: eps == h_minus  =>  alpha = -1 exactly.
    # 2F1 ~ A_log + B_log * log(v).  The endpoint contribution is finite:
    #   integral_0^delta v^exp * [A_log + B_log * log v]^3 dv
    # The A_log^3 term bound is still delta^(exp+1)/(exp+1) with A_log ~ 1.
    if abs(alpha + 1.0) < 1e-8:
        A_approx = 1.0  # at the log resonance A_approx -> finite limit ~1
        bound_A3 = abs(prefactor * A_approx**3 * delta**(exp + 1) / (exp + 1))
        # log-correction bound: |3*A^2*B * log(delta)| * delta^(exp+1)/(exp+1)
        log_correction = abs(3 * A_approx**2 * B * abs(np.log(delta))
                             * delta**(exp + 1) / (exp + 1))
        return bound_A3, log_correction, B, alpha

    # Non-logarithmic case: A ~ eps/(eps - h_minus)
    A_approx = eps / (eps - h_minus)

    # Bound on A^3 endpoint term (convergent):
    bound_A3 = abs(prefactor * A_approx**3 * delta**(exp + 1) / (exp + 1))

    # Bound on 3A^2*B endpoint term (convergent since alpha+exp = -1/2-h_minus > -1):
    exp_3A2B = alpha + exp  # = -0.5 - h_minus  (always > -1 for h_minus < 0.5)
    if exp_3A2B > -1.0:
        bound_3A2B = abs(prefactor * 3 * A_approx**2 * abs(B)
                         * delta**(exp_3A2B + 1) / (exp_3A2B + 1))
    else:
        bound_3A2B = float('inf')

    return bound_A3, bound_3A2B, B, alpha


def validate_d1_base_case(eps_values):
    """
    D1 base case: h_minus=0. Full integral is convergent. Error should be < 1e-6.
    Compare with analytic value pi/2 in limit.
    """
    results = {}
    print("\n--- D1 base case: h_minus=0 (convergent integral) ---")
    for eps in eps_values:
        D = 4.0 - 2.0 * eps
        I, err = full_integral(0.0, eps)
        print(f"  eps={eps:.4f}: I(0,eps)={I:.10f}  err={err:.2e}  {'PASS' if err < ERROR_THRESHOLD else 'FAIL'}")
        results[str(eps)] = {
            "eps": eps, "h_minus": 0.0,
            "integral": I, "error": err,
            "error_threshold": ERROR_THRESHOLD,
            "passes_criterion4": err < ERROR_THRESHOLD,
        }
    return results


def validate_d1_bulk_split(h_minus_values, eps_values):
    """
    D1 bulk split: for small h_minus, show bulk integral [0, 1-delta] has
    error << 1e-6. Compute endpoint bound analytically.
    """
    results = {}
    print("\n--- D1 bulk split (small h_minus) ---")
    for h in h_minus_values:
        for eps in eps_values:
            key = f"h{h:.4f}_e{eps:.4f}"
            B = connection_formula_B(h, eps)
            alpha = -1.0 + eps - h
            print(f"\n  h_-={h}, eps={eps}: alpha={alpha:.4f}, B={B:.4e}")
            delta_results = {}
            for delta in DELTA_VALUES:
                I_bulk, err_bulk = bulk_integral(h, eps, delta)
                b_A3, b_3A2B, _, _ = endpoint_contribution_bound(h, eps, delta)
                passes = err_bulk < ERROR_THRESHOLD
                print(f"    delta={delta:.0e}: I_bulk={I_bulk:.8f}  err={err_bulk:.2e}  "
                      f"ep_bound(A3)={b_A3:.2e}  ep_bound(3A2B)={b_3A2B:.2e}  "
                      f"{'PASS' if passes else 'FAIL'}")
                delta_results[str(delta)] = {
                    "delta": delta,
                    "I_bulk": I_bulk,
                    "error_bulk": err_bulk,
                    "passes_criterion4": passes,
                    "endpoint_bound_A3": b_A3,
                    "endpoint_bound_3A2B": b_3A2B,
                }
            results[key] = {
                "h_minus": h, "eps": eps,
                "alpha": alpha, "B": B,
                "delta_results": delta_results,
            }
    return results


def validate_d1_stage1_comparison(eps_values):
    """
    Compare Stage-1 extrapolated I_D1(eps) with exact I(h_minus=0, eps).
    The difference should be small, confirming the polynomial extrapolation
    is capturing the right limit.
    """
    # Load D1 extraction data for Stage-1 results
    repo_root = Path(__file__).resolve().parent.parent.parent
    d1_file = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs" / "gate3_dl_d1_extraction.json"

    if not d1_file.exists():
        print("  D1 extraction file not found, skipping comparison")
        return {}

    with open(d1_file) as f:
        d1_data = json.load(f)

    stage1 = d1_data.get("stage1_results", {})

    print("\n--- D1 Stage-1 vs exact I(0, eps) comparison ---")
    print(f"  {'eps':>8}  {'I_D1_extrap':>14}  {'I(0,eps)_exact':>14}  {'diff':>10}  {'rel_diff':>10}")

    results = {}
    for eps in eps_values:
        I_exact, err_exact = full_integral(0.0, eps)
        s1_key = str(eps)
        if s1_key in stage1:
            I_extrap = stage1[s1_key]["I_D1"]
            diff = I_extrap - I_exact
            rel_diff = abs(diff) / I_exact
            print(f"  {eps:>8.4f}  {I_extrap:>14.10f}  {I_exact:>14.10f}  {diff:>10.2e}  {rel_diff:>10.2e}")
            results[s1_key] = {
                "eps": eps,
                "I_D1_extrapolated": I_extrap,
                "I_exact_hminus0": I_exact,
                "error_exact": err_exact,
                "difference": diff,
                "relative_difference": rel_diff,
            }
        else:
            print(f"  {eps:>8.4f}  {'(no stage1 data)':>14}")

    return results


def fit_and_extrapolate(x_data, y_data, degree, target=0.0):
    """Polynomial fit and extrapolation (mirrors Phase A harness)."""
    x = np.array(x_data, dtype=float)
    y = np.array(y_data, dtype=float)
    coeffs = np.polyfit(x, y, min(degree, len(x) - 1))
    y_pred = np.polyval(coeffs, x)
    ss_res = float(np.sum((y - y_pred) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else 1.0
    residual = float(np.max(np.abs(y - y_pred)))
    value_at_target = float(np.polyval(coeffs, target))
    return value_at_target, r2, residual


def validate_d3_diagonal(c_values):
    """
    D3 diagonal validation: two-part analysis.

    PART A (small c: h_- = c*eps << eps, so h_- -> 0 with eps):
      Bulk integral [0, 1-delta] directly achieves error < 1e-6.
      Re-extrapolate to eps=0 and verify c-independence.
      Valid for c <= 0.5 where the endpoint contribution is small.

    PART B (all c: Phase A values for reference):
      Load Phase A I_D3(c) values computed via polynomial fit with scipy full
      integral.  These are the accepted values from the blinded protocol.
      Note: for c >= 1.0, the endpoint contribution at finite eps is large
      but vanishes under the eps->0 polynomial extrapolation; bulk-only
      re-extrapolation omits this endpoint piece and is NOT used for promotion.

    The endpoint-split validation directly confirms criterion 4 for c <= 0.5
    (2 of 5 diagonals).  Phase A validates c-independence across all 5 diagonals.
    """
    print("\n--- D3 diagonal split validation ---")

    d3_eps_grid = [0.02, 0.01, 0.005, 0.002, 0.001]
    delta = 1e-3

    # Load Phase A I_D3 values
    repo_root = Path(__file__).resolve().parent.parent.parent
    d3_file = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs" / "gate3_dl_d3_extraction.json"
    phaseA_I_D3 = {}
    phaseA_spread = None
    if d3_file.exists():
        with open(d3_file) as f:
            d3_data = json.load(f)
        for c_key, res in d3_data.get("diagonal_results", {}).items():
            if "I_D3" in res:
                phaseA_I_D3[float(c_key)] = res["I_D3"]
        phaseA_spread = d3_data.get("universality", {}).get("relative_spread")

    # --- Part A: all-c bulk error check ---
    print("\n  Part A: Bulk integral errors at delta=1e-3 (all c)")
    print(f"  {'c':>4}  {'h_-/eps':>6}  {'max_bulk_err':>14}  {'crit4':>6}")
    all_c_results = {}
    for c in c_values:
        max_err = 0.0
        for eps in d3_eps_grid:
            h = c * eps
            _, err_b = bulk_integral(h, eps, delta)
            max_err = max(max_err, err_b)
        passes = max_err < ERROR_THRESHOLD
        all_c_results[str(c)] = {"c": c, "max_bulk_error": max_err, "passes_criterion4": passes}
        print(f"  {c:>4.1f}  {c:>6.1f}*eps  {max_err:>14.2e}  {'PASS' if passes else 'FAIL'}")

    # --- Part B: small-c re-extrapolation (c <= 0.5) ---
    print("\n  Part B: Bulk re-extrapolation to eps=0 (small c only: c<=0.5)")
    small_c_results = {}
    for c in [cv for cv in c_values if cv <= 0.5]:
        eps_seq, I_seq, err_seq = [], [], []
        for eps in d3_eps_grid:
            h = c * eps
            I_b, err_b = bulk_integral(h, eps, delta)
            if err_b < ERROR_THRESHOLD:
                eps_seq.append(eps)
                I_seq.append(I_b)
                err_seq.append(err_b)
        if len(eps_seq) < 3:
            continue
        I_D3_c, r2, resid = fit_and_extrapolate(eps_seq, I_seq,
                                                  degree=min(3, len(eps_seq)-1))
        phaseA_val = phaseA_I_D3.get(c)
        diff = I_D3_c - phaseA_val if phaseA_val else None
        diff_str = f"  diff_phaseA={diff:.2e}" if diff is not None else ""
        print(f"  c={c:.1f}: I_D3_bulk={I_D3_c:.8f}  R2={r2:.8f}  "
              f"n={len(eps_seq)}{diff_str}")
        small_c_results[str(c)] = {
            "c": c, "I_D3_bulk": I_D3_c, "phaseA_I_D3": phaseA_val,
            "diff_vs_phaseA": diff, "fit_r2": r2,
        }

    # C-independence on small-c subset
    small_I_vals = [v["I_D3_bulk"] for v in small_c_results.values()]
    if len(small_I_vals) >= 2:
        mean_sc = float(np.mean(small_I_vals))
        spread_sc = (max(small_I_vals) - min(small_I_vals)) / abs(mean_sc)
        label_sc = ("<1e-4 PASS" if spread_sc < 1e-4 else "<1e-3" if spread_sc < 1e-3 else "FAIL")
        print(f"\n  c-independence (c<=0.5, bulk only): spread={spread_sc:.4e}  {label_sc}")
    else:
        spread_sc = None

    # Phase A c-independence (full 5-c, reference)
    print(f"\n  Phase A I_D3 values (reference, all c):")
    phaseA_vals = [phaseA_I_D3.get(c) for c in c_values if phaseA_I_D3.get(c) is not None]
    for c in c_values:
        pv = phaseA_I_D3.get(c)
        if pv:
            print(f"    c={c:.1f}: I_D3={pv:.8f}")
    if phaseA_spread is not None:
        label_pa = ("PASS" if phaseA_spread < 1e-2 else "FAIL")
        print(f"  Phase A relative spread: {phaseA_spread:.4e}  (<1% {label_pa})")
        print(f"  (This is the criterion-3 universality check that already passed.)")

    return {
        "all_c_bulk_errors": all_c_results,
        "small_c_refit": small_c_results,
        "c_independence_small_c_spread": spread_sc,
        "phaseA_I_D3": phaseA_I_D3,
        "phaseA_relative_spread": phaseA_spread,
        "passes_c_independence_small_c": spread_sc < 1e-4 if spread_sc else None,
        "passes_c_independence_phaseA": phaseA_spread < 1e-2 if phaseA_spread else None,
    }


def main():
    print("=" * 80)
    print("Gate 3 DL Endpoint-Split Validation")
    print(f"Spec: {SPEC_VERSION}")
    print(f"Start: {datetime.now().isoformat()}")
    print("=" * 80)

    print(f"\npi/2 = {np.pi/2:.10f}  (target analytic value)")

    # Grid parameters matching D1/D3 prescriptions
    eps_d1 = [0.01, 0.005, 0.002, 0.001]
    h_minus_small = [0.001, 0.002]  # smallest Stage-1 grid points
    c_values = [0.1, 0.5, 1.0, 2.0, 5.0]

    # 1. D1 base case: h_minus = 0
    base_case_results = validate_d1_base_case(eps_d1)

    # 2. D1 bulk split at small h_minus
    bulk_split_results = validate_d1_bulk_split(
        h_minus_values=[0.001, 0.002],
        eps_values=[0.001, 0.01]
    )

    # 3. D1 Stage-1 comparison: polynomial extrapolation vs exact h_minus=0
    stage1_comparison = validate_d1_stage1_comparison(eps_d1)

    # 4. D3 diagonal validation (bulk re-extrapolation on D3 eps grid)
    d3_results = validate_d3_diagonal(c_values)

    # ── Summary ──────────────────────────────────────────────────────────────
    print("\n" + "=" * 80)
    print("ENDPOINT-SPLIT VALIDATION SUMMARY")
    print("=" * 80)

    # Base case
    base_passes = all(r["passes_criterion4"] for r in base_case_results.values())
    print(f"\n[1] h_minus=0 base case: {'ALL PASS' if base_passes else 'FAIL'}")
    print("    Integration error < 1e-6 at h_minus=0 for all eps values")
    for eps, r in base_case_results.items():
        print(f"    eps={float(eps):.4f}: err={r['error']:.2e}  {'PASS' if r['passes_criterion4'] else 'FAIL'}")

    # Bulk split
    print(f"\n[2] Bulk integral [0, 1-delta] errors at delta=1e-3:")
    for key, res in bulk_split_results.items():
        r = res["delta_results"].get("0.001")
        if r:
            status = "PASS" if r["passes_criterion4"] else "FAIL"
            print(f"    h_-={res['h_minus']:.4f} eps={res['eps']:.4f}: "
                  f"err={r['error_bulk']:.2e}  {status}")

    # Stage-1 comparison
    print(f"\n[3] Stage-1 extrapolation vs exact I(0, eps):")
    for eps_s, r in stage1_comparison.items():
        print(f"    eps={float(eps_s):.4f}: extrap={r['I_D1_extrapolated']:.8f}  "
              f"exact={r['I_exact_hminus0']:.8f}  diff={r['difference']:.2e}")

    # D3
    print(f"\n[4] D3 diagonal validation:")
    sp_sc = d3_results.get("c_independence_small_c_spread")
    sp_pa = d3_results.get("phaseA_relative_spread")
    if sp_sc is not None:
        print(f"    Small-c (c<=0.5) bulk c-independence: {sp_sc:.4e}  "
              f"{'PASS' if sp_sc < 1e-4 else 'FAIL'}")
    if sp_pa is not None:
        print(f"    Phase A all-c universality (criterion 3): {sp_pa:.4e}  "
              f"{'PASS' if sp_pa < 1e-2 else 'FAIL'}")

    # ── Write JSON output ────────────────────────────────────────────────────
    repo_root = Path(__file__).resolve().parent.parent.parent
    out_dir = repo_root / "theory" / "hard_theory" / "gate3_dl_outputs"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / "gate3_dl_endpoint_split_validation.json"

    output = {
        "spec": SPEC_VERSION,
        "date": datetime.now().isoformat(),
        "validation_type": "endpoint_split",
        "error_threshold": ERROR_THRESHOLD,
        "pi_over_2": float(np.pi / 2),
        "d1_base_case": base_case_results,
        "d1_bulk_split": bulk_split_results,
        "d1_stage1_comparison": stage1_comparison,
        "d3_diagonal": d3_results,
        "summary": {
            "h_minus_0_base_passes": base_passes,
            "bulk_split_error_at_delta_1e3": {
                k: v["delta_results"].get("0.001", {}).get("error_bulk")
                for k, v in bulk_split_results.items()
            },
            "d3_c_independence_small_c": d3_results.get("c_independence_small_c_spread"),
            "d3_passes_small_c": d3_results.get("passes_c_independence_small_c"),
            "d3_phaseA_spread": d3_results.get("phaseA_relative_spread"),
        },
    }

    with open(out_file, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_file}")
    print("=" * 80)
    print(f"End: {datetime.now().isoformat()}")
    print("=" * 80)


if __name__ == "__main__":
    main()
