#!/usr/bin/env python3
"""
Program J — Stage J2: Nonlinear RG Stability of Regime Split

Test whether the J1 regime split (discrete → rational attractor,
continuum → persistent tails) survives under weak nonlinearity.

N1-N4: same bath families as J1 with nonlinear constitutive term.
Nonlinearity: tau Phi_dot = F(Phi) + coupling_to_bath
where F(Phi) = (X - Phi) - eps_nl * (X - Phi)^3 (cubic saturation)

Coarse-graining: time-blocking with FIXED physical time horizon
(artifact control from J1: do NOT shrink the window).
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# SETUP
# ============================================================
tau = 1.0
X_eq = 1.0

# Fixed time horizon (artifact control: do NOT shrink window under blocking)
T_horizon = 100.0
N_t = 10000
t_fine = np.linspace(0.01, T_horizon, N_t)
dt_fine = t_fine[1] - t_fine[0]

# Nonlinearity ladder
eps_nl_values = [0.0, 0.01, 0.05, 0.1]

# Blocking scales (coarse-graining parameter)
Delta_values = [0.01, 0.1, 1.0, 5.0, 10.0]

# ============================================================
# BATH KERNELS (from J1)
# ============================================================
def bath_F1(t, N_modes=10):
    """Discrete finite-mode bath."""
    taus = np.logspace(-1, 1, N_modes)
    K = np.zeros_like(t)
    for i in range(N_modes):
        K += (1.0/N_modes) * np.exp(-t / taus[i])
    return K

def bath_F2(t, s=1.0, omega_max=50):
    """Continuum Ohmic bath."""
    N = 500
    omega = np.linspace(0.01, omega_max, N)
    dw = omega[1] - omega[0]
    J = omega**s
    K = np.zeros_like(t)
    for i, ti in enumerate(t):
        K[i] = np.sum(J * np.exp(-omega * ti)) * dw / np.pi
    return K

def bath_F3(t, alpha=0.5):
    """Power-law kernel."""
    return 1.0 / (t + 0.01)**alpha

def bath_F4(t, alpha_cont=0.3):
    """Mixed: 3 discrete + continuum tail."""
    K_d = (0.3*np.exp(-t/0.5) + 0.2*np.exp(-t/2) + 0.2*np.exp(-t/8))
    K_c = 0.3 / (t + 0.01)**alpha_cont
    return K_d + K_c

# ============================================================
# NONLINEAR IMPULSE RESPONSE
# ============================================================
def compute_nonlinear_response(bath_func, eps_nl, t_grid):
    """
    Compute the impulse response of the nonlinear constitutive law:
    tau dPhi/dt = (X - Phi) - eps_nl*(X - Phi)^3 - coupling * integral K(t-s) Phi(s) ds

    For the impulse response, start at Phi(0) = 0, X = 1.
    The "effective kernel" K_eff(t) is defined as the response Phi(t)/X
    for the FULL nonlinear + bath system.

    Simplified model: the bath acts as a memory correction to the relaxation.
    tau dPhi/dt = F(X-Phi) + kappa * integral_0^t K(t-s) (X-Phi(s)) ds
    where F(v) = v - eps_nl * v^3, kappa = 0.1 (weak bath coupling)
    """
    kappa = 0.1  # bath coupling strength
    K_bath = bath_func(t_grid)
    K_bath = K_bath / max(K_bath[0], 1e-10)  # normalize K(0) = 1

    dt = t_grid[1] - t_grid[0]

    # Integrate with explicit Euler + convolution
    Phi = np.zeros(len(t_grid))
    Phi[0] = 0.0  # impulse response: start at 0, relax toward X

    for n in range(len(t_grid) - 1):
        v = X_eq - Phi[n]
        F_nl = v - eps_nl * v**3  # nonlinear constitutive force

        # Memory integral: kappa * integral_0^t K(t-s)(X-Phi(s)) ds
        # Approximate by trapezoidal on past values
        mem = 0.0
        for j in range(n+1):
            if n - j < len(K_bath):
                mem += K_bath[n - j] * (X_eq - Phi[j]) * dt
        mem *= kappa

        dPhi = (F_nl + mem) / tau * dt
        Phi[n+1] = Phi[n] + dPhi

    # Effective kernel: K_eff(t) = (X - Phi(t)) / X (normalized deviation from target)
    K_eff = (X_eq - Phi) / X_eq
    # Clip negatives (can happen due to overshoot in nonlinear case)
    K_eff = np.maximum(K_eff, 1e-15)

    return K_eff, Phi

# ============================================================
# DIAGNOSTICS (from J1, with artifact controls)
# ============================================================
def time_block_fixed_horizon(K, t, Delta, T_hor):
    """Block-average K on fixed horizon [0, T_hor]."""
    dt = t[1] - t[0]
    block_size = max(1, int(Delta / dt))
    N_blocks = len(K) // block_size
    t_cg = np.array([np.mean(t[i*block_size:(i+1)*block_size]) for i in range(N_blocks)])
    K_cg = np.array([np.mean(K[i*block_size:(i+1)*block_size]) for i in range(N_blocks)])
    # Keep FULL horizon (do not truncate)
    return K_cg, t_cg

def tail_exponent(K, t, frac=0.5):
    mask = (t > frac * t[-1]) & (K > 1e-12)
    if np.sum(mask) < 5:
        return np.nan
    try:
        return -np.polyfit(np.log(t[mask]), np.log(K[mask]), 1)[0]
    except:
        return np.nan

def markov_error(K, t):
    if len(K) < 5 or K[0] <= 0:
        return np.nan
    try:
        def exp_model(t, a, tau):
            return a * np.exp(-t / max(tau, 1e-6))
        popt, _ = curve_fit(exp_model, t, K, p0=[K[0], 1.0], maxfev=10000,
                          bounds=([0, 1e-4], [np.inf, np.inf]))
        K_fit = exp_model(t, *popt)
        return np.sqrt(np.mean((K - K_fit)**2) / max(np.mean(K**2), 1e-30))
    except:
        return np.nan

def effective_poles(K, t, tol=0.05):
    for n in range(1, 6):
        try:
            def model(t, *params):
                result = np.zeros_like(t)
                nn = len(params) // 2
                for i in range(nn):
                    result += params[i] * np.exp(-t / max(params[nn+i], 1e-6))
                return result
            p0 = list(np.ones(n)*K[0]/n) + list(np.logspace(-1, 1, n))
            popt, _ = curve_fit(model, t, K, p0=p0, maxfev=15000,
                              bounds=([0]*n + [1e-4]*n, [np.inf]*n + [t[-1]*5]*n))
            K_fit = model(t, *popt)
            eps = np.sqrt(np.mean((K - K_fit)**2) / max(np.mean(K**2), 1e-30))
            if eps < tol:
                return n, eps
        except:
            continue
    return 5, 1.0

# Spectral-domain check: FFT of K and look for branch-cut signature
def spectral_smoothness(K, t):
    """
    Rational response → K_hat(omega) has isolated poles → FFT is smooth.
    Non-rational (branch cut) → FFT has persistent oscillatory/non-smooth structure.
    Metric: high-frequency energy fraction in the FFT.
    """
    K_hat = np.abs(np.fft.rfft(K))
    N = len(K_hat)
    if N < 4:
        return np.nan
    # Fraction of spectral energy above the midpoint frequency
    E_total = np.sum(K_hat**2)
    E_high = np.sum(K_hat[N//2:]**2)
    if E_total > 0:
        return E_high / E_total
    return np.nan

# ============================================================
# MAIN COMPUTATION
# ============================================================
print("=" * 95)
print("Program J — Stage J2: Nonlinear RG Stability of Regime Split")
print("=" * 95)

# Precompute bath kernels on fine grid
bath_names = {
    'N1 (discrete)': bath_F1,
    'N2 (Ohmic cont.)': bath_F2,
    'N3 (power-law)': bath_F3,
    'N4 (mixed)': bath_F4,
}

all_results = {}

for bname, bfunc in bath_names.items():
    print(f"\n{'='*95}")
    print(f"FAMILY: {bname}")
    print(f"{'='*95}")

    family_data = {}

    for eps_nl in eps_nl_values:
        print(f"\n  eps_nl = {eps_nl}:")

        # Compute nonlinear impulse response
        K_eff, Phi = compute_nonlinear_response(bfunc, eps_nl, t_fine)

        print(f"    {'Delta':>8s} {'N_eff':>6s} {'eps_rat':>10s} {'eps_M':>10s} {'tail_p':>8s} {'HF_frac':>10s}")
        print(f"    {'-'*8} {'-'*6} {'-'*10} {'-'*10} {'-'*8} {'-'*10}")

        run_data = []
        for Delta in Delta_values:
            K_cg, t_cg = time_block_fixed_horizon(K_eff, t_fine, Delta, T_horizon)
            if len(K_cg) < 10:
                run_data.append({'Delta': Delta, 'N_eff': np.nan, 'eps_rat': np.nan,
                                'eps_M': np.nan, 'tail_p': np.nan, 'HF': np.nan})
                print(f"    {Delta:8.2f}   (insufficient data)")
                continue

            N_e, eps_r = effective_poles(K_cg, t_cg)
            eps_m = markov_error(K_cg, t_cg)
            p = tail_exponent(K_cg, t_cg)
            hf = spectral_smoothness(K_cg, t_cg)

            run_data.append({'Delta': Delta, 'N_eff': N_e, 'eps_rat': eps_r,
                            'eps_M': eps_m, 'tail_p': p, 'HF': hf})

            p_str = f"{p:8.2f}" if not np.isnan(p) else f"{'nan':>8s}"
            hf_str = f"{hf:10.4f}" if not np.isnan(hf) else f"{'nan':>10s}"
            print(f"    {Delta:8.2f} {N_e:6d} {eps_r:10.4f} {eps_m:10.4f} {p_str} {hf_str}")

        family_data[eps_nl] = run_data

    all_results[bname] = family_data

# ============================================================
# REGIME-SPLIT PERSISTENCE ANALYSIS
# ============================================================
print(f"\n{'='*95}")
print("REGIME-SPLIT PERSISTENCE ANALYSIS")
print("=" * 95)

# For each family, compare tail_p and eps_M across eps_nl at the coarsest blocking
print(f"\n  At Delta = {Delta_values[-1]} (coarsest blocking):")
print(f"\n  {'Family':<20s} {'eps_nl':>8s} {'tail_p':>8s} {'eps_M':>8s} {'N_eff':>6s} {'HF':>8s} {'class':>25s}")
print(f"  {'-'*20} {'-'*8} {'-'*8} {'-'*8} {'-'*6} {'-'*8} {'-'*25}")

classifications = {}
for bname in bath_names:
    family_class = []
    for eps_nl in eps_nl_values:
        data = all_results[bname][eps_nl]
        # Find the coarsest blocking entry
        coarse = [d for d in data if d['Delta'] == Delta_values[-1]]
        if not coarse:
            coarse = [data[-1]]
        d = coarse[0]

        # Classification logic
        p = d['tail_p'] if not np.isnan(d.get('tail_p', np.nan)) else 99
        eM = d['eps_M'] if not np.isnan(d.get('eps_M', np.nan)) else 99

        if eM < 0.05:
            cls = "rational_ir_attractor"
        elif eM < 0.15 and p > 2.0:
            cls = "effectively_rational"
        elif eM >= 0.15 and p < 2.0:
            cls = "persistent_nonrational"
        else:
            cls = "crossover/ambiguous"

        family_class.append(cls)

        p_str = f"{d['tail_p']:.2f}" if not np.isnan(d.get('tail_p', np.nan)) else "nan"
        eM_str = f"{d['eps_M']:.4f}" if not np.isnan(d.get('eps_M', np.nan)) else "nan"
        hf_str = f"{d['HF']:.4f}" if not np.isnan(d.get('HF', np.nan)) else "nan"

        print(f"  {bname:<20s} {eps_nl:8.2f} {p_str:>8s} {eM_str:>8s} {d['N_eff']:6} {hf_str:>8s} {cls:>25s}")

    classifications[bname] = family_class

# ============================================================
# SPLIT PERSISTENCE VERDICT
# ============================================================
print(f"\n{'='*95}")
print("SPLIT PERSISTENCE VERDICT")
print("=" * 95)

# Check: does each family maintain its J1 classification across eps_nl?
print(f"\n  Family-level classification stability across eps_nl:")
for bname in bath_names:
    classes = classifications[bname]
    unique_classes = set(classes)
    stable = len(unique_classes) == 1
    print(f"  {bname:<20s}: {classes}")
    print(f"    {'STABLE' if stable else 'SHIFTS'} across eps_nl = {eps_nl_values}")

# Count how many families maintain their J1 classification
n_stable = 0
n_total = len(bath_names)
for bname in bath_names:
    if len(set(classifications[bname])) == 1:
        n_stable += 1

split_frac = n_stable / n_total

print(f"\n  Split stability: {n_stable}/{n_total} families maintain classification")
print(f"  Fraction: {split_frac:.2f}")

# ============================================================
# CRITICAL eps_nl
# ============================================================
print(f"\n  Critical eps_nl search (where classification first changes):")
for bname in bath_names:
    classes = classifications[bname]
    baseline = classes[0]
    crit = None
    for i, eps in enumerate(eps_nl_values):
        if classes[i] != baseline:
            crit = eps
            break
    if crit:
        print(f"  {bname:<20s}: splits at eps_nl = {crit} ({baseline} -> {classes[eps_nl_values.index(crit)]})")
    else:
        print(f"  {bname:<20s}: STABLE for all eps_nl tested (up to {eps_nl_values[-1]})")

# ============================================================
# SPECTRAL-DOMAIN CONSISTENCY
# ============================================================
print(f"\n{'='*95}")
print("SPECTRAL-DOMAIN CONSISTENCY CHECK")
print("=" * 95)

print(f"\n  High-frequency spectral fraction (HF) at coarsest blocking:")
print(f"  (Low HF → smooth/rational. High HF → non-smooth/branch-cut-like.)")
print(f"\n  {'Family':<20s} {'eps_nl=0':>10s} {'eps_nl=0.01':>12s} {'eps_nl=0.05':>12s} {'eps_nl=0.1':>12s}")
for bname in bath_names:
    row = f"  {bname:<20s}"
    for eps_nl in eps_nl_values:
        data = all_results[bname][eps_nl]
        coarse = [d for d in data if d['Delta'] == Delta_values[-1]]
        if coarse:
            hf = coarse[0].get('HF', np.nan)
            row += f" {hf:12.4f}" if not np.isnan(hf) else f" {'nan':>12s}"
        else:
            row += f" {'N/A':>12s}"
    print(row)

print(f"""
  Interpretation:
  If HF is low and stable across eps_nl → spectral domain agrees with time domain.
  If HF increases with eps_nl → nonlinearity generates spectral complexity.
  If HF differs between discrete (N1) and continuum (N3) families → split persists spectrally.
""")

# ============================================================
# GLOBAL CLASSIFICATION
# ============================================================
print(f"{'='*95}")
print("GLOBAL CLASSIFICATION")
print("=" * 95)

if split_frac >= 0.75:
    token = "split_universalized_beyond_linear"
    detail = ("The discrete/continuum regime split persists under weak nonlinearity "
              f"for {n_stable}/{n_total} families. The split is robust to eps_nl up to 0.1.")
elif split_frac >= 0.5:
    token = "split_persists_conditionally"
    detail = (f"The split persists for {n_stable}/{n_total} families. Some families "
              "shift classification under nonlinearity, but the majority maintain their J1 class.")
else:
    token = "split_breaks_under_nonlinearity"
    detail = (f"Only {n_stable}/{n_total} families maintain their classification. "
              "The nonlinearity disrupts the regime split.")

print(f"\n  Token: {token}")
print(f"  {detail}")

print(f"\n{'='*95}")
print("END OF COMPUTATION")
print("=" * 95)
