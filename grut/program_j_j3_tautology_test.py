#!/usr/bin/env python3
"""
Program J — Stage J3: Non-Tautology Validation

Test whether J2's "universal effective rationalization" is genuinely
emergent or tautologically imposed by the contractive constitutive operator.

Four tests:
1. Constitutive-operator ablation (A: 1st-order, B: Volterra, C: 2nd-order)
2. Late-time dominance falsification (vary tau, bath strength)
3. Observable-level invariance
4. Frequency-domain analyticity
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.fft import rfft, rfftfreq
import warnings
warnings.filterwarnings('ignore')

X_eq = 1.0
T_hor = 80.0; N_t = 3000
t = np.linspace(0.01, T_hor, N_t); dt = t[1] - t[0]

# Power-law bath (strongest non-rational test case)
def bath_PL(t, alpha=0.5):
    return 1.0 / (t + 0.01)**alpha

def tail_p(K, t, frac=0.3):
    mask = (t > frac*t[-1]) & (K > 1e-10) & np.isfinite(K)
    if np.sum(mask) < 10: return np.nan
    try: return -np.polyfit(np.log(t[mask]), np.log(K[mask]), 1)[0]
    except: return np.nan

def eps_M(K, t):
    valid = (K > 1e-10) & np.isfinite(K)
    if np.sum(valid) < 10: return np.nan
    try:
        popt, _ = curve_fit(lambda t, a, tau: a*np.exp(-t/max(tau, 1e-6)),
                           t[valid], K[valid], p0=[K[valid][0], 1], maxfev=5000,
                           bounds=([0, 1e-4], [np.inf, np.inf]))
        Kf = popt[0]*np.exp(-t[valid]/popt[1])
        return np.sqrt(np.mean((K[valid]-Kf)**2) / max(np.mean(K[valid]**2), 1e-30))
    except: return np.nan

# ============================================================
# TEST 1: CONSTITUTIVE-OPERATOR ABLATION
# ============================================================
print("=" * 90)
print("TEST 1: CONSTITUTIVE-OPERATOR ABLATION")
print("=" * 90)

kappa = 0.3  # stronger bath coupling to stress-test

def run_operator_A(tau, K_bath, t):
    """A) First-order contractive: tau dPhi/dt = (X-Phi) + kappa*mem"""
    N = len(t); Phi = np.zeros(N)
    for n in range(N-1):
        v = X_eq - Phi[n]
        mem = 0.0
        for j in range(max(0, n-300), n+1):
            if n-j < len(K_bath): mem += K_bath[n-j]*(X_eq-Phi[j])*dt
        Phi[n+1] = Phi[n] + (v + kappa*mem)/tau*dt
    return np.maximum((X_eq - Phi)/X_eq, 1e-15)

def run_operator_B(tau, tau_mem, lam, K_bath, t):
    """B) Weak-memory Volterra: tau dPhi/dt + Phi + lam*Z = X + kappa*mem
       tau_mem dZ/dt + Z = Phi"""
    N = len(t); Phi = np.zeros(N); Z = np.zeros(N)
    for n in range(N-1):
        mem = 0.0
        for j in range(max(0, n-300), n+1):
            if n-j < len(K_bath): mem += K_bath[n-j]*(X_eq-Phi[j])*dt
        dPhi = (X_eq - Phi[n] - lam*Z[n] + kappa*mem)/tau*dt
        dZ = (Phi[n] - Z[n])/tau_mem*dt
        Phi[n+1] = Phi[n] + dPhi
        Z[n+1] = Z[n] + dZ
    return np.maximum((X_eq - Phi)/X_eq, 1e-15)

def run_operator_C(tau1, tau2, K_bath, t):
    """C) Second-order local: tau1*tau2*Phi_ddot + (tau1+tau2)*Phi_dot + Phi = X + kappa*mem
       Rewritten as two first-order: dPhi/dt = V, dV/dt = ..."""
    N = len(t); Phi = np.zeros(N); V = np.zeros(N)
    for n in range(N-1):
        mem = 0.0
        for j in range(max(0, n-300), n+1):
            if n-j < len(K_bath): mem += K_bath[n-j]*(X_eq-Phi[j])*dt
        # tau1*tau2*V_dot + (tau1+tau2)*V + Phi = X + kappa*mem
        V_dot = (X_eq + kappa*mem - Phi[n] - (tau1+tau2)*V[n])/(tau1*tau2)
        Phi[n+1] = Phi[n] + V[n]*dt
        V[n+1] = V[n] + V_dot*dt
    return np.maximum((X_eq - Phi)/X_eq, 1e-15)

K_bath = bath_PL(t, alpha=0.5)
K_bath_norm = K_bath / K_bath[0]

tau_test = 1.0

print(f"\n  Bath: power-law alpha=0.5, kappa={kappa}")
print(f"\n  {'Operator':>25s} {'tail_p':>8s} {'eps_M':>10s} {'class':>25s}")
print(f"  {'-'*25} {'-'*8} {'-'*10} {'-'*25}")

K_A = run_operator_A(tau_test, K_bath_norm, t)
pA = tail_p(K_A, t); eA = eps_M(K_A, t)

K_B = run_operator_B(tau_test, 0.5, 0.1, K_bath_norm, t)
pB = tail_p(K_B, t); eB = eps_M(K_B, t)

K_C = run_operator_C(tau_test, 0.5, K_bath_norm, t)
pC = tail_p(K_C, t); eC = eps_M(K_C, t)

for name, p, e in [("A) 1st-order contractive", pA, eA),
                     ("B) Volterra (memory)", pB, eB),
                     ("C) 2nd-order local", pC, eC)]:
    cls = "rational" if (not np.isnan(e) and e < 0.05) else ("near-rational" if (not np.isnan(e) and e < 0.15) else "non-rational")
    p_s = f"{p:.2f}" if not np.isnan(p) else "nan"
    e_s = f"{e:.4f}" if not np.isnan(e) else "nan"
    print(f"  {name:>25s} {p_s:>8s} {e_s:>10s} {cls:>25s}")

print(f"""
  ABLATION RESULT:
  - Operator A (1st-order): {'rational' if eA and eA < 0.05 else 'see above'}
  - Operator B (Volterra): {'rational' if eB and eB < 0.05 else 'non-rational' if eB and eB > 0.15 else 'see above'}
  - Operator C (2nd-order): {'rational' if eC and eC < 0.05 else 'see above'}

  If ALL three show rational → rationalization is from the BATH coupling, not the operator form.
  If ONLY A shows rational → rationalization is from the 1st-order contraction (tautological).
  If A and C but not B → the attractor structure matters, not just the order.
""")

# ============================================================
# TEST 2: LATE-TIME DOMINANCE FALSIFICATION
# ============================================================
print("=" * 90)
print("TEST 2: LATE-TIME DOMINANCE FALSIFICATION")
print("=" * 90)
print(f"\n  Vary tau and kappa to find where bath tail dominates:")
print(f"\n  {'tau':>8s} {'kappa':>8s} {'tail_p':>8s} {'eps_M':>10s} {'bath dominates?':>20s}")
print(f"  {'-'*8} {'-'*8} {'-'*8} {'-'*10} {'-'*20}")

bath_dominant_found = False
for tau_v in [0.1, 0.5, 1.0, 5.0, 10.0, 50.0]:
    for kappa_v in [0.1, 0.3, 1.0, 3.0, 10.0]:
        K_test = run_operator_A(tau_v, K_bath_norm * kappa_v / kappa, t)
        p_test = tail_p(K_test, t)
        e_test = eps_M(K_test, t)

        # Bath dominates if tail_p is close to bath alpha (0.5) and eps_M is large
        p_val = p_test if not np.isnan(p_test) else 99
        e_val = e_test if not np.isnan(e_test) else 0
        bath_dom = p_val < 3.0 and e_val > 0.15

        if bath_dom:
            bath_dominant_found = True

        p_s = f"{p_test:.2f}" if not np.isnan(p_test) else "nan"
        e_s = f"{e_test:.4f}" if not np.isnan(e_test) else "nan"
        dom_s = "YES" if bath_dom else "no"
        print(f"  {tau_v:8.1f} {kappa_v:8.1f} {p_s:>8s} {e_s:>10s} {dom_s:>20s}")

if bath_dominant_found:
    print(f"\n  BATH TAIL DOMINANCE FOUND in some parameter regions.")
    print(f"  The universality claim is WEAKENED to regime-conditional.")
    print(f"  The constitutive contraction dominates only when tau is small")
    print(f"  relative to the bath memory depth. When tau >> tau_bath, the")
    print(f"  bath tail can leak through.")
else:
    print(f"\n  No bath tail dominance found across the tested parameter range.")

# ============================================================
# TEST 3: OBSERVABLE-LEVEL INVARIANCE
# ============================================================
print(f"\n{'='*90}")
print("TEST 3: OBSERVABLE-LEVEL INVARIANCE")
print("=" * 90)

# Compare physically measurable quantities between bath types
# at fixed constitutive parameters

K_bath_exp = np.exp(-t / 2.0)  # exponential bath (discrete, rational)
K_bath_pl = bath_PL(t, alpha=0.5)  # power-law bath (non-rational)
K_bath_exp_norm = K_bath_exp / K_bath_exp[0]
K_bath_pl_norm = K_bath_pl / K_bath_pl[0]

tau_obs = 1.0; kappa_obs = 0.3

K_eff_exp = run_operator_A(tau_obs, K_bath_exp_norm, t)
K_eff_pl = run_operator_A(tau_obs, K_bath_pl_norm, t)

# Observable 1: response half-life (time for K_eff to drop to 0.5)
def half_life(K, t):
    idx = np.argmax(K < 0.5)
    if idx > 0: return t[idx]
    return np.nan

hl_exp = half_life(K_eff_exp, t)
hl_pl = half_life(K_eff_pl, t)

# Observable 2: low-frequency susceptibility slope
# chi(omega) = FT[K_eff]. Slope at omega=0: d chi/d omega|_{omega→0}
K_hat_exp = np.abs(rfft(K_eff_exp))
K_hat_pl = np.abs(rfft(K_eff_pl))
freq = rfftfreq(len(K_eff_exp), d=dt)

# Low-freq slope: (K_hat[1] - K_hat[0]) / (freq[1] - freq[0])
if len(freq) > 2:
    slope_exp = (K_hat_exp[2] - K_hat_exp[0]) / (freq[2] - freq[0] + 1e-20)
    slope_pl = (K_hat_pl[2] - K_hat_pl[0]) / (freq[2] - freq[0] + 1e-20)
else:
    slope_exp = slope_pl = np.nan

# Observable 3: integrated memory contribution
# M_frac = integral K_bath * K_eff / integral K_eff
if np.sum(K_eff_exp) > 0:
    M_frac_exp = kappa_obs * np.sum(K_bath_exp_norm * K_eff_exp * dt) / np.sum(K_eff_exp * dt)
    M_frac_pl = kappa_obs * np.sum(K_bath_pl_norm * K_eff_pl * dt) / np.sum(K_eff_pl * dt)
else:
    M_frac_exp = M_frac_pl = np.nan

print(f"\n  Constitutive: tau={tau_obs}, kappa={kappa_obs}")
print(f"  {'Observable':<35s} {'Exp bath':>12s} {'PL bath':>12s} {'ratio':>8s} {'distinguish?':>14s}")
print(f"  {'-'*35} {'-'*12} {'-'*12} {'-'*8} {'-'*14}")

for name, v1, v2 in [("Response half-life", hl_exp, hl_pl),
                       ("Low-freq suscept. slope", slope_exp, slope_pl),
                       ("Memory contribution frac", M_frac_exp, M_frac_pl)]:
    if v1 and v2 and not np.isnan(v1) and not np.isnan(v2) and v2 != 0:
        ratio = v1/v2
        dist = "YES" if abs(ratio - 1) > 0.1 else "MARGINAL" if abs(ratio - 1) > 0.03 else "NO"
    else:
        ratio = np.nan; dist = "N/A"
    v1_s = f"{v1:.4f}" if v1 and not np.isnan(v1) else "nan"
    v2_s = f"{v2:.4f}" if v2 and not np.isnan(v2) else "nan"
    r_s = f"{ratio:.4f}" if not np.isnan(ratio) else "nan"
    print(f"  {name:<35s} {v1_s:>12s} {v2_s:>12s} {r_s:>8s} {dist:>14s}")

# ============================================================
# TEST 4: FREQUENCY-DOMAIN ANALYTICITY
# ============================================================
print(f"\n{'='*90}")
print("TEST 4: FREQUENCY-DOMAIN ANALYTICITY CHECK")
print("=" * 90)

# A rational (meromorphic) function has isolated poles → smooth FFT
# A non-rational (branch cut) function has non-isolated singularity → rough/oscillatory FFT
# Measure: spectral roughness = variance of d|K_hat|/d_omega normalized

def spectral_roughness(K, t):
    K_hat = np.abs(rfft(K))
    if len(K_hat) < 10: return np.nan
    dK = np.diff(K_hat)
    return np.std(dK) / max(np.mean(np.abs(dK)), 1e-20)

# Compare bath kernels directly (should show the difference)
sr_bath_exp = spectral_roughness(K_bath_exp_norm[:N_t], t)
sr_bath_pl = spectral_roughness(K_bath_pl_norm[:N_t], t)

# Compare effective responses (J2 claim: should both be smooth)
sr_eff_exp = spectral_roughness(K_eff_exp, t)
sr_eff_pl = spectral_roughness(K_eff_pl, t)

print(f"\n  Spectral roughness (higher = more non-analytic structure):")
print(f"  {'Object':<30s} {'Exp bath':>12s} {'PL bath':>12s}")
print(f"  {'-'*30} {'-'*12} {'-'*12}")
print(f"  {'Bath kernel K_bath':<30s} {sr_bath_exp:12.4f} {sr_bath_pl:12.4f}")
print(f"  {'Effective response K_eff':<30s} {sr_eff_exp:12.4f} {sr_eff_pl:12.4f}")

if sr_bath_pl > 1.5 * sr_bath_exp:
    print(f"\n  Bath level: PL bath is rougher than Exp bath (expected: branch cut).")
else:
    print(f"\n  Bath level: roughness similar (spectral test inconclusive at bath level).")

if abs(sr_eff_pl - sr_eff_exp) / max(sr_eff_exp, 1e-10) < 0.3:
    print(f"  Effective level: roughness SIMILAR for both baths.")
    print(f"  → Constitutive operator smooths the spectral structure.")
    print(f"  → Branch-cut signature is SUPPRESSED (not eliminated) in K_eff.")
elif sr_eff_pl > 1.5 * sr_eff_exp:
    print(f"  Effective level: PL bath still rougher → branch cut LEAKS through.")
else:
    print(f"  Effective level: inconclusive.")

# Branch-cut residue: measure energy in high-frequency spectral tail
K_hat_eff_pl = np.abs(rfft(K_eff_pl))
K_hat_eff_exp = np.abs(rfft(K_eff_exp))
N_freq = len(K_hat_eff_pl)
if N_freq > 4:
    E_total_pl = np.sum(K_hat_eff_pl**2)
    E_high_pl = np.sum(K_hat_eff_pl[N_freq//2:]**2)
    E_total_exp = np.sum(K_hat_eff_exp**2)
    E_high_exp = np.sum(K_hat_eff_exp[N_freq//2:]**2)
    hf_pl = E_high_pl / max(E_total_pl, 1e-30)
    hf_exp = E_high_exp / max(E_total_exp, 1e-30)
    print(f"\n  High-freq energy fraction:")
    print(f"    Exp bath K_eff: {hf_exp:.6f}")
    print(f"    PL bath K_eff:  {hf_pl:.6f}")
    print(f"    Ratio: {hf_pl/max(hf_exp, 1e-20):.2f}")

    if hf_pl > 2 * hf_exp:
        print(f"    PL bath retains MORE high-freq content → branch-cut residue non-zero.")
    else:
        print(f"    Similar high-freq content → branch-cut residue suppressed.")

# ============================================================
# SYNTHESIS
# ============================================================
print(f"\n{'='*90}")
print("SYNTHESIS AND CLASSIFICATION")
print("=" * 90)

print(f"""
  TEST 1 (ABLATION):
    Operator A (1st-order contractive): eps_M = {eA:.4f if not np.isnan(eA) else 'nan'}
    Operator B (Volterra memory):       eps_M = {eB:.4f if not np.isnan(eB) else 'nan'}
    Operator C (2nd-order local):       eps_M = {eC:.4f if not np.isnan(eC) else 'nan'}

    {'ALL operators show similar effective rationalization → NOT tautological from 1st-order form alone.' if eA and eB and eC and max(eA,eB,eC)<0.15 else 'Operators differ → rationalization IS operator-dependent.' if eA and eB and eC else 'Incomplete data.'}

  TEST 2 (LATE-TIME FALSIFICATION):
    {'Bath tail dominance FOUND at some parameters → universality is REGIME-CONDITIONAL.' if bath_dominant_found else 'No bath tail dominance found → constitutive contraction dominates at all tested parameters.'}

  TEST 3 (OBSERVABLE INVARIANCE):
    {'Observables DIFFER between bath types → the two models ARE operationally distinguishable despite similar eps_M.' if any(abs(v1/v2-1)>0.1 for v1,v2 in [(hl_exp,hl_pl),(M_frac_exp,M_frac_pl)] if v1 and v2 and v2!=0 and not np.isnan(v1) and not np.isnan(v2)) else 'Observables similar → operationally indistinguishable.'}

  TEST 4 (SPECTRAL ANALYTICITY):
    Branch-cut structure is {'SUPPRESSED but detectable' if hf_pl > 1.5*hf_exp else 'effectively eliminated'} in the effective response.
""")

# Final classification
if bath_dominant_found:
    cls_final = "regime_limited_effective_rationalization"
    detail = ("The constitutive contraction rationalizes the effective response ONLY when "
              "the constitutive timescale tau is shorter than the bath memory depth. "
              "When tau >> bath timescale or kappa >> 1, the bath tail can dominate.")
elif eB and eB > 0.15:
    cls_final = "regime_limited_effective_rationalization"
    detail = ("The Volterra operator (B) does NOT show effective rationalization — "
              "the memory operator form matters. The J2 universality is partially "
              "an artifact of the 1st-order contractive form.")
else:
    cls_final = "universal_effective_rationalization"
    detail = ("All three operator forms and all bath types show effective rationalization. "
              "The result is not tautological — it extends beyond the 1st-order form.")

print(f"  CLASSIFICATION: {cls_final}")
print(f"  {detail}")

print(f"\n{'='*90}")
print("END OF COMPUTATION")
print("=" * 90)
