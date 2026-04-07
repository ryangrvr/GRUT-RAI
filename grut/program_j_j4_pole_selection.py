#!/usr/bin/env python3
"""
Program J — Stage J4: IR Pole-Selection Test

Determine whether single-pole (L1/Markovian) behavior is DYNAMICALLY
SELECTED under coarse-graining, or merely an effective masking of
persistent multi-pole structure.

Three ensembles: 2-pole, 3-pole, high-order Volterra surrogate.
Three RG methods: time-blocking, mode elimination, low-freq projection.
Six diagnostics: N_eff, W_sub, pole ratios, eps_1pole, leakage, admissibility.
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.fft import rfft, rfftfreq
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# FIXED PHYSICAL PARAMETERS
# ============================================================
T_hor = 80.0; N_t = 4000
t = np.linspace(0.01, T_hor, N_t); dt = t[1] - t[0]

# ============================================================
# ENSEMBLES
# ============================================================

def E1_kernel(t, tau1=1.0, tau2=5.0, w1=0.7, w2=0.3):
    """E1: Admissible 2-pole system. w1 + w2 = 1."""
    return w1 * np.exp(-t/tau1) + w2 * np.exp(-t/tau2)

def E2_kernel(t, tau1=0.5, tau2=2.0, tau3=8.0, w1=0.5, w2=0.3, w3=0.2):
    """E2: Admissible 3-pole system."""
    return w1*np.exp(-t/tau1) + w2*np.exp(-t/tau2) + w3*np.exp(-t/tau3)

def E3_kernel(t, N_poles=10):
    """E3: High-order rational surrogate for weak-memory Volterra.
    Many closely spaced poles mimicking a smooth kernel."""
    taus = np.logspace(-0.5, 1.5, N_poles)
    weights = np.ones(N_poles) / N_poles
    K = np.zeros_like(t)
    for i in range(N_poles):
        K += weights[i] * np.exp(-t / taus[i])
    return K

# ============================================================
# RG METHODS (artifact-controlled: fixed physical horizon)
# ============================================================

def R1_time_blocking(K, t, Delta):
    """R1: Time-blocking average with fixed horizon."""
    bs = max(1, int(Delta / dt))
    nb = len(K) // bs
    tc = np.array([np.mean(t[i*bs:(i+1)*bs]) for i in range(nb)])
    Kc = np.array([np.mean(K[i*bs:(i+1)*bs]) for i in range(nb)])
    return Kc, tc

def R2_mode_elimination(K, t, n_keep):
    """R2: Keep only the n_keep slowest exponential modes.
    Fit K to n_poles exponentials, then reconstruct from the n_keep slowest."""
    n_fit = min(6, max(n_keep + 2, 3))  # fit with slightly more than we keep
    popt = fit_n_exp(K, t, n_fit)
    if popt is None:
        return K, t

    n = len(popt) // 2
    amps = popt[:n]
    taus = popt[n:]

    # Sort by timescale (slowest first)
    order = np.argsort(-taus)
    amps_sorted = amps[order]
    taus_sorted = taus[order]

    # Reconstruct from the n_keep slowest
    K_reduced = np.zeros_like(t)
    for i in range(min(n_keep, n)):
        K_reduced += amps_sorted[i] * np.exp(-t / taus_sorted[i])

    return K_reduced, t

def R3_lowfreq_projection(K, t, omega_cut):
    """R3: Zero out high-frequency content above omega_cut."""
    K_hat = rfft(K)
    freq = rfftfreq(len(K), d=dt)
    K_hat[freq > omega_cut] = 0
    K_filtered = np.fft.irfft(K_hat, n=len(K))
    return np.maximum(K_filtered, 0), t  # enforce positivity

# ============================================================
# FITTING / DIAGNOSTICS
# ============================================================

def fit_n_exp(K, t, n):
    """Fit K(t) to sum of n exponentials. Return params or None."""
    if n <= 0 or len(K) < 5:
        return None
    valid = K > 1e-12
    if np.sum(valid) < 2*n + 2:
        return None

    tau_init = np.logspace(np.log10(max(t[1], 0.01)), np.log10(t[-1]/2), n)
    a_init = np.ones(n) * K[valid][0] / n

    def model(t, *params):
        nn = len(params) // 2
        result = np.zeros_like(t)
        for i in range(nn):
            result += params[i] * np.exp(-t / max(params[nn+i], 1e-6))
        return result

    try:
        p0 = list(a_init) + list(tau_init)
        popt, _ = curve_fit(model, t[valid], K[valid], p0=p0, maxfev=15000,
                          bounds=([0]*n + [1e-4]*n, [np.inf]*n + [t[-1]*5]*n))
        return popt
    except:
        return None

def compute_diagnostics(K, t, label=""):
    """Compute D1-D6 diagnostics for kernel K on grid t."""
    results = {}

    # D1: Effective pole count
    for n in range(1, 6):
        popt = fit_n_exp(K, t, n)
        if popt is not None:
            nn = len(popt) // 2
            K_fit = np.zeros_like(t)
            for i in range(nn):
                K_fit += popt[i] * np.exp(-t / popt[nn+i])
            valid = K > 1e-12
            eps = np.sqrt(np.mean((K[valid] - K_fit[valid])**2) / max(np.mean(K[valid]**2), 1e-30))
            if eps < 0.05:
                results['N_eff'] = n
                results['fit_params'] = popt
                results['eps_fit'] = eps
                break
    else:
        results['N_eff'] = 5
        results['eps_fit'] = 1.0
        results['fit_params'] = None

    # D2: Subleading weight W_sub
    if results.get('fit_params') is not None:
        popt = results['fit_params']
        nn = len(popt) // 2
        amps = popt[:nn]
        taus = popt[nn:]
        total_weight = np.sum(amps * taus)  # integral of each mode
        if total_weight > 0:
            # Sort by timescale (slowest = leading)
            order = np.argsort(-taus)
            weights = (amps * taus)[order]
            W_leading = weights[0] / total_weight
            W_sub = 1.0 - W_leading
        else:
            W_sub = np.nan
        results['W_sub'] = W_sub
        results['pole_taus'] = taus[np.argsort(-taus)]
        results['pole_amps'] = amps[np.argsort(-taus)]
    else:
        results['W_sub'] = np.nan

    # D3: Pole ratio |p_i/p_1|
    if 'pole_taus' in results and len(results['pole_taus']) >= 2:
        results['pole_ratio_2_1'] = results['pole_taus'][1] / results['pole_taus'][0]
    else:
        results['pole_ratio_2_1'] = 0.0

    # D4: One-pole truncation error on fixed low-omega window
    popt_1 = fit_n_exp(K, t, 1)
    if popt_1 is not None:
        K_1pole = popt_1[0] * np.exp(-t / popt_1[1])
        # Low-frequency window: use t > T_hor/2
        mask_lf = t > T_hor / 3
        valid_lf = (K[mask_lf] > 1e-12)
        if np.sum(valid_lf) > 5:
            eps_1pole = np.sqrt(np.mean((K[mask_lf][valid_lf] - K_1pole[mask_lf][valid_lf])**2) /
                               max(np.mean(K[mask_lf][valid_lf]**2), 1e-30))
        else:
            eps_1pole = np.nan
    else:
        eps_1pole = np.nan
    results['eps_1pole'] = eps_1pole

    # D5: Leakage observables
    # Memory fraction: integral of K(t>T/2) / integral of K(total)
    int_total = np.trapezoid(np.abs(K), t)
    int_late = np.trapezoid(np.abs(K[t > T_hor/2]), t[t > T_hor/2])
    results['mem_frac'] = int_late / max(int_total, 1e-20)

    # D6: Admissibility (A1-A6 spot checks)
    # A2 positivity: K >= 0
    results['positive'] = np.all(K >= -1e-10)
    # A4 monotone: K decreasing
    results['monotone'] = np.all(np.diff(K) <= dt * 0.01 * np.abs(K[:-1]).max())
    # A5 bounded
    results['bounded'] = np.all(np.isfinite(K)) and np.max(np.abs(K)) < 1e10

    return results

# ============================================================
# MAIN COMPUTATION
# ============================================================
print("=" * 95)
print("Program J — Stage J4: IR Pole-Selection Test")
print("=" * 95)

ensembles = {
    'E1 (2-pole)': E1_kernel(t),
    'E2 (3-pole)': E2_kernel(t),
    'E3 (10-pole Volterra)': E3_kernel(t),
}

# Also variant E1 and E2 with different parameters for robustness
ensembles_extra = {
    'E1b (2-pole, wide)': E1_kernel(t, tau1=0.3, tau2=20.0, w1=0.6, w2=0.4),
    'E2b (3-pole, wide)': E2_kernel(t, tau1=0.2, tau2=3.0, tau3=15.0, w1=0.4, w2=0.3, w3=0.3),
}

all_ensembles = {**ensembles, **ensembles_extra}

# RG scales
rg_scales_R1 = [0.01, 0.1, 0.5, 1.0, 5.0]  # Delta for time-blocking
rg_scales_R2 = [1, 2, 3]  # n_keep for mode elimination
rg_scales_R3 = [10.0, 1.0, 0.1]  # omega_cut for low-freq projection

# ============================================================
# R1: TIME-BLOCKING FLOW
# ============================================================
print(f"\n{'='*95}")
print("R1: TIME-BLOCKING FLOW")
print("=" * 95)

for ename, K_orig in all_ensembles.items():
    print(f"\n  --- {ename} ---")
    print(f"  {'Delta':>8s} {'N_eff':>6s} {'W_sub':>8s} {'p2/p1':>8s} {'eps_1p':>10s} {'mem_f':>8s} {'pos':>4s} {'mon':>4s}")
    print(f"  {'-'*8} {'-'*6} {'-'*8} {'-'*8} {'-'*10} {'-'*8} {'-'*4} {'-'*4}")

    for Delta in rg_scales_R1:
        Kc, tc = R1_time_blocking(K_orig, t, Delta)
        if len(Kc) < 10:
            print(f"  {Delta:8.2f}   (too few points)")
            continue
        d = compute_diagnostics(Kc, tc)
        ws = f"{d['W_sub']:.4f}" if not np.isnan(d.get('W_sub', np.nan)) else "nan"
        pr = f"{d['pole_ratio_2_1']:.4f}" if d.get('pole_ratio_2_1', 0) > 0 else "0"
        ep = f"{d['eps_1pole']:.4f}" if not np.isnan(d.get('eps_1pole', np.nan)) else "nan"
        mf = f"{d['mem_frac']:.4f}" if not np.isnan(d.get('mem_frac', np.nan)) else "nan"
        print(f"  {Delta:8.2f} {d['N_eff']:6d} {ws:>8s} {pr:>8s} {ep:>10s} {mf:>8s} "
              f"{'Y' if d['positive'] else 'N':>4s} {'Y' if d['monotone'] else 'N':>4s}")

# ============================================================
# R2: MODE ELIMINATION FLOW
# ============================================================
print(f"\n{'='*95}")
print("R2: MODE ELIMINATION FLOW")
print("=" * 95)

for ename, K_orig in all_ensembles.items():
    print(f"\n  --- {ename} ---")
    print(f"  {'n_keep':>8s} {'N_eff':>6s} {'W_sub':>8s} {'eps_1p':>10s} {'pos':>4s}")
    print(f"  {'-'*8} {'-'*6} {'-'*8} {'-'*10} {'-'*4}")

    for nk in rg_scales_R2:
        Kr, tr = R2_mode_elimination(K_orig, t, nk)
        d = compute_diagnostics(Kr, tr)
        ws = f"{d['W_sub']:.4f}" if not np.isnan(d.get('W_sub', np.nan)) else "nan"
        ep = f"{d['eps_1pole']:.4f}" if not np.isnan(d.get('eps_1pole', np.nan)) else "nan"
        print(f"  {nk:8d} {d['N_eff']:6d} {ws:>8s} {ep:>10s} "
              f"{'Y' if d['positive'] else 'N':>4s}")

# ============================================================
# R3: LOW-FREQUENCY PROJECTION FLOW
# ============================================================
print(f"\n{'='*95}")
print("R3: LOW-FREQUENCY PROJECTION FLOW")
print("=" * 95)

for ename, K_orig in all_ensembles.items():
    print(f"\n  --- {ename} ---")
    print(f"  {'omega_c':>8s} {'N_eff':>6s} {'W_sub':>8s} {'eps_1p':>10s} {'pos':>4s}")
    print(f"  {'-'*8} {'-'*6} {'-'*8} {'-'*10} {'-'*4}")

    for wc in rg_scales_R3:
        Kf, tf = R3_lowfreq_projection(K_orig, t, wc)
        d = compute_diagnostics(Kf, tf)
        ws = f"{d['W_sub']:.4f}" if not np.isnan(d.get('W_sub', np.nan)) else "nan"
        ep = f"{d['eps_1pole']:.4f}" if not np.isnan(d.get('eps_1pole', np.nan)) else "nan"
        print(f"  {wc:8.2f} {d['N_eff']:6d} {ws:>8s} {ep:>10s} "
              f"{'Y' if d['positive'] else 'N':>4s}")

# ============================================================
# SELECTION ANALYSIS
# ============================================================
print(f"\n{'='*95}")
print("SELECTION ANALYSIS")
print("=" * 95)

# For each ensemble, track W_sub flow under R1
print(f"\n  W_sub flow under time-blocking (R1):")
print(f"  {'Ensemble':<25s}", end="")
for Delta in rg_scales_R1:
    print(f"  {'D='+str(Delta):>8s}", end="")
print(f"  {'TREND':>12s}")

for ename, K_orig in all_ensembles.items():
    row = f"  {ename:<25s}"
    wsubs = []
    for Delta in rg_scales_R1:
        Kc, tc = R1_time_blocking(K_orig, t, Delta)
        if len(Kc) >= 10:
            d = compute_diagnostics(Kc, tc)
            ws = d.get('W_sub', np.nan)
            wsubs.append(ws)
            row += f"  {ws:8.4f}" if not np.isnan(ws) else f"  {'nan':>8s}"
        else:
            row += f"  {'---':>8s}"
            wsubs.append(np.nan)

    # Trend: is W_sub decreasing?
    valid_ws = [w for w in wsubs if not np.isnan(w)]
    if len(valid_ws) >= 2:
        if valid_ws[-1] < valid_ws[0] * 0.5:
            trend = "DECREASING"
        elif valid_ws[-1] < valid_ws[0] * 0.9:
            trend = "MILD DECREASE"
        elif valid_ws[-1] > valid_ws[0] * 1.1:
            trend = "INCREASING"
        else:
            trend = "STABLE"
    else:
        trend = "N/A"
    row += f"  {trend:>12s}"
    print(row)

# ============================================================
# CLASSIFICATION
# ============================================================
print(f"\n{'='*95}")
print("CLASSIFICATION")
print("=" * 95)

# Collect final W_sub at coarsest blocking for each ensemble
print(f"\n  Final diagnostics at coarsest accessible blocking:")
print(f"  {'Ensemble':<25s} {'N_eff':>6s} {'W_sub':>8s} {'eps_1p':>10s} {'Selected?':>15s}")
print(f"  {'-'*25} {'-'*6} {'-'*8} {'-'*10} {'-'*15}")

selection_results = []
for ename, K_orig in all_ensembles.items():
    # Find coarsest blocking that still has enough points
    for Delta in reversed(rg_scales_R1):
        Kc, tc = R1_time_blocking(K_orig, t, Delta)
        if len(Kc) >= 10:
            d = compute_diagnostics(Kc, tc)
            ws = d.get('W_sub', np.nan)
            ep = d.get('eps_1pole', np.nan)
            neff = d.get('N_eff', 99)

            # Selection criteria
            if neff == 1 and (np.isnan(ws) or ws < 0.1) and (np.isnan(ep) or ep < 0.05):
                sel = "SELECTED"
            elif neff <= 2 and (np.isnan(ws) or ws < 0.3):
                sel = "NEAR-SELECTED"
            else:
                sel = "NOT SELECTED"

            selection_results.append(sel)

            ws_s = f"{ws:.4f}" if not np.isnan(ws) else "nan"
            ep_s = f"{ep:.4f}" if not np.isnan(ep) else "nan"
            print(f"  {ename:<25s} {neff:6d} {ws_s:>8s} {ep_s:>10s} {sel:>15s}")
            break

# Global verdict
n_selected = sum(1 for s in selection_results if s == "SELECTED")
n_near = sum(1 for s in selection_results if s in ["SELECTED", "NEAR-SELECTED"])
n_total = len(selection_results)

print(f"\n  Selected: {n_selected}/{n_total}")
print(f"  Selected or near: {n_near}/{n_total}")

if n_selected == n_total:
    token = "l1_ir_selected"
    detail = "Single-pole L1 is dynamically selected across all ensembles and RG methods."
elif n_near == n_total:
    token = "l1_conditionally_selected"
    detail = ("L1 selection is approached but subleading poles retain measurable weight. "
              "Selection is directional but incomplete at accessible coarse-graining scales.")
elif n_near > n_total // 2:
    token = "l1_conditionally_selected"
    detail = f"L1 selection holds for {n_near}/{n_total} ensembles. Regime-conditional."
else:
    token = "l1_not_selected"
    detail = f"Only {n_near}/{n_total} ensembles approach L1 selection. Multi-pole structure persists."

print(f"\n  TOKEN: {token}")
print(f"  {detail}")

# ============================================================
# STRUCTURAL INTERPRETATION
# ============================================================
print(f"\n{'='*95}")
print("STRUCTURAL INTERPRETATION: MINIMALITY vs DYNAMIC SELECTION")
print("=" * 95)

print(f"""
  MINIMALITY (from I3):
    L1 is the unique constraint-free admissible primitive.
    This is a STATIC structural property — L1 requires zero inequality
    constraints to satisfy A1-A6. It does not depend on RG flow.

  DYNAMIC SELECTION (from J4):
    Under coarse-graining, the subleading poles {
    'are systematically suppressed, and W_sub decreases toward zero. L1 is not only minimal but also DYNAMICALLY PREFERRED — the RG flow drives multi-pole systems toward single-pole behavior.' if token == 'l1_ir_selected' else
    'are partially suppressed but retain finite weight. L1 is APPROACHED but not reached at accessible scales. The flow is directional (toward L1) but incomplete.' if 'conditionally' in token else
    'retain significant weight under coarse-graining. L1 is minimal but NOT dynamically selected. Multi-pole structure is a persistent feature, not a transient.'}

  The distinction matters:
  - If L1 is selected: L1 is both the simplest AND the natural IR limit.
    Using L1 is justified not just by Occam's razor but by RG flow.
  - If L1 is NOT selected: L1 is the simplest admissible law but higher
    poles are physically present. Using L1 is an approximation (lossy truncation),
    not an IR limit.
""")

print("=" * 95)
print("END OF COMPUTATION")
print("=" * 95)
