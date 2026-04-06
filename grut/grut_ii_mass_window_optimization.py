#!/usr/bin/env python3
"""
GRUT II Epsilon-Prime — Mass-Window Optimization and Protocol Feasibility Audit

Scans mass from 3 fg to 100 fg, computing:
1. USL prediction (Lambda_USL ~ m^2)
2. Gas collision rate (Lambda_gas ~ m^{2/3})
3. BB emission rate (Lambda_emi ~ m^2 via V^2 scaling)
4. Protocol feasibility metrics (superposition creation difficulty)
5. Combined figure-of-merit: signal strength × protocol feasibility

Key scaling laws:
- Lambda_USL = G m^2 / (hbar l)                       [m^2]
- Lambda_gas = n_gas * pi * R^2 * v_th                 [R^2 ~ m^{2/3}]
- Lambda_emi ~ V^2 * T_int^7 / c^5                    [V^2 ~ m^2]
- x_zpf = sqrt(hbar / (2 m omega_trap))               [m^{-1/2}]
- Free expansion time to l: t_exp ~ l / (x_zpf * omega_trap) [m^{1/2}]
- Decoherence during expansion: exp(-Gamma * t_exp)    [worse with mass]
"""

import numpy as np

# ============================================================
# CONSTANTS
# ============================================================
G       = 6.67430e-11    # m^3 kg^-1 s^-2
hbar    = 1.05457e-34    # J s
k_B     = 1.38065e-23    # J/K
c       = 2.99792e8      # m/s
amu     = 1.66054e-27    # kg

# ============================================================
# FIXED PLATFORM PARAMETERS
# ============================================================
rho     = 2200.0         # kg/m^3 (silica)
l       = 10e-9          # m (10 nm branch separation — fixed)
T_env   = 4.0            # K
T_int   = 20.0           # K
P_gas   = 1e-13          # Pa (10^-15 mbar)
m_gas   = 28 * amu       # N2
omega_trap = 2 * np.pi * 1e5  # rad/s (100 kHz)

# Gas parameters at T_env
v_th = np.sqrt(8 * k_B * T_env / (np.pi * m_gas))
n_gas = P_gas / (k_B * T_env)

# Thermal de Broglie of gas
lambda_dB_gas = hbar * np.sqrt(2 * np.pi / (m_gas * k_B * T_env))

# BB emission reference (from Delta-Prime at m_ref)
# Lambda_emi = 2.70e-6 at m = 3.89 fg, R = 75 nm
# Scales as V^2 ~ R^6 ~ m^2
m_ref_emi = 3.89e-18
Lambda_emi_ref = 2.70e-6

# ============================================================
# MASS SCAN
# ============================================================
masses_fg = np.array([3, 4, 5, 7, 10, 12, 15, 20, 25, 30, 40, 50, 70, 100])
masses_kg = masses_fg * 1e-18

print("=" * 100)
print("GRUT II Epsilon-Prime: Mass-Window Optimization")
print("=" * 100)

# ============================================================
# PART I — SCAN DEFINITION
# ============================================================
print("\n" + "=" * 100)
print("PART I — SCAN DEFINITION")
print("=" * 100)

print(f"\nFixed parameters:")
print(f"  Branch separation: l = {l*1e9:.0f} nm")
print(f"  Environment: T_env = {T_env} K, P = {P_gas:.0e} Pa, gas = N2")
print(f"  Internal temp: T_int = {T_int} K")
print(f"  Trap frequency: {omega_trap/(2*np.pi)/1e3:.0f} kHz")
print(f"  Material: silica (rho = {rho} kg/m^3)")
print(f"  Protocol: dark, charge-neutral")

print(f"\nMass scan: {masses_fg[0]} fg to {masses_fg[-1]} fg ({len(masses_fg)} points)")

# ============================================================
# PART II — ENVIRONMENTAL SCALING
# ============================================================
print("\n" + "=" * 100)
print("PART II — ENVIRONMENTAL SCALING ACROSS MASS")
print("=" * 100)

# Compute for each mass
R_arr = (3 * masses_kg / (4 * np.pi * rho))**(1/3)
diam_arr = 2 * R_arr

# Lambda_USL = G m^2 / (hbar l)
Lambda_USL_arr = G * masses_kg**2 / (hbar * l)

# Lambda_gas = n_gas * pi * R^2 * v_th (short-wavelength limit, l >> lambda_dB)
Lambda_gas_arr = n_gas * np.pi * R_arr**2 * v_th

# Lambda_emi scales as m^2 from reference
Lambda_emi_arr = Lambda_emi_ref * (masses_kg / m_ref_emi)**2

# Total env (gas dominates, but include emission)
Lambda_env_arr = Lambda_gas_arr + Lambda_emi_arr

# Ratio
ratio_arr = Lambda_USL_arr / Lambda_env_arr
ratio_gas_arr = Lambda_USL_arr / Lambda_gas_arr

print(f"\n{'m(fg)':>6s} {'R(nm)':>7s} {'d(nm)':>7s} {'L_USL':>12s} {'L_gas':>12s} {'L_emi':>12s} {'L_env':>12s} {'USL/env':>10s} {'USL/gas':>10s} {'Class':>20s}")
print(f"{'-'*6} {'-'*7} {'-'*7} {'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*10} {'-'*10} {'-'*20}")

for i in range(len(masses_fg)):
    mf = masses_fg[i]
    R_nm = R_arr[i] * 1e9
    d_nm = diam_arr[i] * 1e9
    lu = Lambda_USL_arr[i]
    lg = Lambda_gas_arr[i]
    le = Lambda_emi_arr[i]
    lt = Lambda_env_arr[i]
    r = ratio_arr[i]
    rg = ratio_gas_arr[i]

    if r > 10:
        cls = "USL-DOMINATED"
    elif r > 1:
        cls = "USL > env"
    elif r > 0.3:
        cls = "COMPARABLE"
    elif r > 0.1:
        cls = "env-dominated (close)"
    else:
        cls = "env-dominated"

    print(f"{mf:6.0f} {R_nm:7.1f} {d_nm:7.0f} {lu:12.4e} {lg:12.4e} {le:12.4e} {lt:12.4e} {r:10.3f} {rg:10.3f} {cls:>20s}")

# ============================================================
# PART III — PROTOCOL FEASIBILITY SCALING
# ============================================================
print("\n" + "=" * 100)
print("PART III — PROTOCOL FEASIBILITY SCALING")
print("=" * 100)

# Zero-point motion
x_zpf_arr = np.sqrt(hbar / (2 * masses_kg * omega_trap))

# Free expansion time to reach l = 10 nm
# sigma(t) ~ x_zpf * omega_trap * t for omega*t >> 1
# t_expand = l / (x_zpf * omega_trap)
t_expand_arr = l / (x_zpf_arr * omega_trap)

# With inverted potential (exponential expansion), much faster:
# sigma(t) ~ x_zpf * exp(omega_inv * t)
# t_inv = (1/omega_inv) * ln(l / x_zpf)
# Assume omega_inv ~ omega_trap (typical for inverted potential)
omega_inv = omega_trap
t_inv_arr = (1 / omega_inv) * np.log(l / x_zpf_arr)

# Decoherence accumulated during expansion
# Phi_gas = Lambda_gas * t_expand (free expansion)
# Phi_gas_inv = Lambda_gas * t_inv (inverted potential)
Phi_gas_free_arr = Lambda_gas_arr * t_expand_arr
Phi_gas_inv_arr = Lambda_gas_arr * t_inv_arr

# Visibility survival during expansion
V_surv_free_arr = np.exp(-Phi_gas_free_arr)
V_surv_inv_arr = np.exp(-Phi_gas_inv_arr)

# SUPER-MARIO achievable separation for fixed optics
# Delta_x ~ m^(-1/6) (rough scaling from PNAS 2024)
# Normalize to: at m = 1 fg, SUPER-MARIO gives ~5 nm (room temp)
# At arbitrary mass: Delta_x_SM ~ 5 nm * (1e-18 / m)^(1/6)
Delta_x_SM_arr = 5e-9 * (1e-18 / masses_kg)**(1/6)

# Stern-Gerlach separation: Delta_x ~ 1/m for fixed gradient and time
# Normalize: at m = 10^-17 kg, Delta_x_SG ~ 100 nm (from arXiv:2601.06608)
Delta_x_SG_arr = 100e-9 * (1e-17 / masses_kg)

# Whether 10 nm is achievable by each method
SM_achievable = Delta_x_SM_arr >= l
SG_achievable = Delta_x_SG_arr >= l

# Total interrogation time needed (for free-fall measurement)
# If free expansion is used: need t_expand to CREATE superposition + t_int to MEASURE
# Total time: t_total = t_expand + t_int
# But the interrogation time IS the expansion time for a free-fall interferometer
# The coherence must survive for t_expand (creation) + t_recombine (= t_expand) + t_readout
# Total coherent time ~ 2 * t_expand (Mach-Zehnder like)
t_coherent_free_arr = 2 * t_expand_arr
t_coherent_inv_arr = 2 * t_inv_arr

# Free-fall distance during coherent time
g = 9.81  # m/s^2
h_fall_free_arr = 0.5 * g * t_coherent_free_arr**2
h_fall_inv_arr = 0.5 * g * t_coherent_inv_arr**2

# Protocol feasibility score (0 to 1)
# Penalize: long expansion time, poor visibility survival, large free fall
# Score = V_surv * (1 if achievable else 0) * exp(-h_fall / h_max)
h_max = 10.0  # m (maximum practical free-fall height, e.g. drop tower)

# For inverted potential protocol
score_inv_arr = V_surv_inv_arr * np.exp(-h_fall_inv_arr / h_max)
# Clip to 0 if expansion time is unreasonable
score_inv_arr = np.where(t_inv_arr > 1.0, 0, score_inv_arr)  # > 1 s expansion = impractical

# For free expansion
score_free_arr = V_surv_free_arr * np.exp(-h_fall_free_arr / h_max)
score_free_arr = np.where(t_expand_arr > 10.0, 0, score_free_arr)

print(f"\n{'m(fg)':>6s} {'x_zpf(pm)':>10s} {'t_exp(ms)':>10s} {'t_inv(us)':>10s} {'Phi_gas_f':>10s} {'Phi_gas_i':>10s} {'V_surv_i':>10s} {'h_fall_i(m)':>12s} {'SM_dx(nm)':>10s} {'SG_dx(nm)':>10s}")
print(f"{'-'*6} {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*10} {'-'*10}")

for i in range(len(masses_fg)):
    mf = masses_fg[i]
    xzpf_pm = x_zpf_arr[i] * 1e12
    t_exp_ms = t_expand_arr[i] * 1e3
    t_inv_us = t_inv_arr[i] * 1e6
    phi_f = Phi_gas_free_arr[i]
    phi_i = Phi_gas_inv_arr[i]
    vs_i = V_surv_inv_arr[i]
    hf_i = h_fall_inv_arr[i]
    sm_nm = Delta_x_SM_arr[i] * 1e9
    sg_nm = Delta_x_SG_arr[i] * 1e9

    print(f"{mf:6.0f} {xzpf_pm:10.2f} {t_exp_ms:10.3f} {t_inv_us:10.1f} {phi_f:10.4e} {phi_i:10.4e} {vs_i:10.6f} {hf_i:12.4e} {sm_nm:10.2f} {sg_nm:10.1f}")

# ============================================================
# EXPANDED PROTOCOL ANALYSIS
# ============================================================
print("\n--- Protocol Feasibility Summary ---")
print(f"\n{'m(fg)':>6s} {'Method':>15s} {'t_create':>12s} {'V_survive':>10s} {'h_fall':>10s} {'10nm OK?':>10s}")
print(f"{'-'*6} {'-'*15} {'-'*12} {'-'*10} {'-'*10} {'-'*10}")

for i in range(len(masses_fg)):
    mf = masses_fg[i]

    # Inverted potential method
    t_c = t_inv_arr[i]
    vs = V_surv_inv_arr[i]
    hf = h_fall_inv_arr[i]

    if t_c < 1e-3:
        t_str = f"{t_c*1e6:.1f} us"
    elif t_c < 1:
        t_str = f"{t_c*1e3:.2f} ms"
    else:
        t_str = f"{t_c:.2f} s"

    if hf < 0.001:
        hf_str = f"{hf*1e3:.2f} mm"
    elif hf < 1:
        hf_str = f"{hf*100:.1f} cm"
    else:
        hf_str = f"{hf:.1f} m"

    ok = "YES" if (vs > 0.9 and hf < 10 and t_c < 0.1) else ("MARGINAL" if (vs > 0.5 and hf < 100) else "NO")

    print(f"{mf:6.0f} {'inv. pot.':>15s} {t_str:>12s} {vs:10.6f} {hf_str:>10s} {ok:>10s}")

# ============================================================
# PART IV — TRUE OPTIMUM WINDOW
# ============================================================
print("\n" + "=" * 100)
print("PART IV — TRUE OPTIMUM WINDOW")
print("=" * 100)

# Figure of merit 1: USL/env ratio (theory-only optimum)
# Maximize Lambda_USL / Lambda_env
# Lambda_USL ~ m^2, Lambda_gas ~ m^{2/3}
# Ratio ~ m^{4/3} → monotonically increasing → theory optimum is at MAX mass

print(f"\nTheory-only optimum: USL/env ratio = Lambda_USL/Lambda_gas ~ m^{{4/3}}")
print(f"  This is MONOTONICALLY INCREASING with mass.")
print(f"  Theory-only optimum: LARGEST POSSIBLE MASS (no upper limit from decoherence alone)")
print(f"  At 100 fg: USL/gas = {ratio_gas_arr[-1]:.1f}")

# Figure of merit 2: Detectability = (Delta_V / V) = 1 - exp(-Lambda_USL * t_int)
# where t_int is limited by decoherence and free-fall
# Practical constraint: t_int limited by protocol feasibility

# For inverted potential:
# Visibility = exp(-Lambda_total * 2 * t_inv) where Lambda_total = Lambda_gas + Lambda_USL
# The SIGNAL is: [V(env only) - V(env+USL)] / V(env only) = 1 - exp(-Lambda_USL * 2*t_inv)
# But if total decoherence kills ALL visibility, signal is unobservable

# Practical figure of merit: signal-to-noise per run
# SNR_run = Delta_V / sigma_V ~ Delta_V * sqrt(N_photons)
# For simplicity: SNR_run ~ (V_without - V_with) * sqrt(some efficiency)
# ~ Lambda_USL * t_meas * exp(-Lambda_env * t_meas)

# Optimize t_meas for maximum (Lambda_USL * t * exp(-Lambda_env * t)):
# d/dt [t * exp(-Gamma * t)] = exp(-Gamma*t) * (1 - Gamma*t) = 0 at t* = 1/Gamma
# So optimal measurement time = 1/Gamma_env

print(f"\nOptimal interrogation time (maximizes signal × visibility):")
print(f"  t_opt = 1 / Gamma_env")

t_opt_arr = 1 / Lambda_env_arr
h_opt_arr = 0.5 * g * t_opt_arr**2

# But t_opt may exceed free-fall constraints
# Practical limit: h_fall < 10 m → t < sqrt(2*10/9.81) = 1.43 s
t_max_ground = np.sqrt(2 * 10 / g)  # 1.43 s (10 m drop tower)
t_max_space = 100.0  # s (space)
t_max_drop = np.sqrt(2 * 100 / g)  # 4.52 s (100 m drop tower, e.g. ZARM Bremen = 110 m)

print(f"  Ground (10 m drop): t_max = {t_max_ground:.2f} s")
print(f"  Drop tower (100 m): t_max = {t_max_drop:.2f} s")
print(f"  Space: t_max = {t_max_space} s")

# Actual interrogation time: min(t_opt, t_max)
for label, t_max in [("Ground (10m)", t_max_ground), ("Drop tower (100m)", t_max_drop), ("Space", t_max_space)]:
    print(f"\n--- {label} ---")
    t_actual = np.minimum(t_opt_arr, t_max)

    # Signal: Lambda_USL * t_actual * exp(-Lambda_env * t_actual)
    signal_arr = Lambda_USL_arr * t_actual * np.exp(-Lambda_env_arr * t_actual)

    # Decoherence penalty
    V_env_arr = np.exp(-Lambda_env_arr * t_actual)

    # Visibility contrast
    DeltaV_arr = np.exp(-Lambda_env_arr * t_actual) - np.exp(-(Lambda_env_arr + Lambda_USL_arr) * t_actual)

    # Free-fall height
    h_fall = 0.5 * g * t_actual**2

    # Need creation time INSIDE the interrogation time
    # If using inverted potential: creation takes t_inv
    # Remaining time for measurement: t_actual - t_inv (must be > 0)
    t_measure = t_actual - t_inv_arr
    t_measure = np.maximum(t_measure, 0)

    # Effective signal including creation overhead:
    signal_eff = Lambda_USL_arr * t_measure * np.exp(-Lambda_env_arr * t_actual)

    # Number of runs for 3-sigma (ideal shot noise)
    # Need DeltaV / sqrt(N) / V_env > 3 → N > 9 * V_env^2 / DeltaV^2
    N_3sigma = np.where(DeltaV_arr > 0, 9 * V_env_arr**2 / DeltaV_arr**2, np.inf)

    print(f"  {'m(fg)':>6s} {'t_opt(s)':>10s} {'t_act(s)':>10s} {'DeltaV':>12s} {'V_env':>10s} {'h(m)':>8s} {'N_3sig':>10s} {'signal':>12s}")
    print(f"  {'-'*6} {'-'*10} {'-'*10} {'-'*12} {'-'*10} {'-'*8} {'-'*10} {'-'*12}")

    for i in range(len(masses_fg)):
        mf = masses_fg[i]
        to = t_opt_arr[i]
        ta = t_actual[i]
        dv = DeltaV_arr[i]
        ve = V_env_arr[i]
        hh = h_fall[i]
        nn = N_3sigma[i]
        ss = signal_eff[i]

        n_str = f"{nn:.0f}" if nn < 1e8 else "inf"
        print(f"  {mf:6.0f} {to:10.1f} {ta:10.3f} {dv:12.4e} {ve:10.6f} {hh:8.2f} {n_str:>10s} {ss:12.4e}")

    # Find optimal mass for this platform
    best_idx = np.argmax(signal_eff)
    print(f"\n  OPTIMAL MASS ({label}): {masses_fg[best_idx]} fg")
    print(f"  Signal: {signal_eff[best_idx]:.4e}, DeltaV: {DeltaV_arr[best_idx]:.4e}, N_3sig: {N_3sigma[best_idx]:.0f}")

# ============================================================
# PART V — PRACTICAL GO/NO-GO THRESHOLDS
# ============================================================
print("\n" + "=" * 100)
print("PART V — PRACTICAL GO/NO-GO THRESHOLDS")
print("=" * 100)

# Where USL clearly dominates gas
idx_dominate = np.argmax(ratio_gas_arr > 3)
if ratio_gas_arr[idx_dominate] > 3:
    print(f"\n1. USL clearly dominates gas (ratio > 3):")
    print(f"   First at m = {masses_fg[idx_dominate]} fg, ratio = {ratio_gas_arr[idx_dominate]:.2f}")
else:
    print(f"\n1. USL never dominates gas by 3x in scan range")

# Where visibility contrast > 1%
for platform, t_max in [("Ground (10m)", t_max_ground), ("Drop tower (100m)", t_max_drop)]:
    t_actual = np.minimum(t_opt_arr, t_max)
    DeltaV = np.exp(-Lambda_env_arr * t_actual) - np.exp(-(Lambda_env_arr + Lambda_USL_arr) * t_actual)
    V_env = np.exp(-Lambda_env_arr * t_actual)
    contrast = np.where(V_env > 0, DeltaV / V_env, 0)

    idx_1pct = np.argmax(contrast > 0.01)
    if contrast[idx_1pct] > 0.01:
        print(f"\n2. Visibility contrast > 1% ({platform}):")
        print(f"   First at m = {masses_fg[idx_1pct]} fg, contrast = {contrast[idx_1pct]*100:.2f}%")

    idx_5pct = np.argmax(contrast > 0.05)
    if contrast[idx_5pct] > 0.05:
        print(f"3. Visibility contrast > 5% ({platform}):")
        print(f"   First at m = {masses_fg[idx_5pct]} fg, contrast = {contrast[idx_5pct]*100:.2f}%")

# Where N_runs < 1000
print(f"\n4. N_runs < 1000 for 3-sigma detection:")
for platform, t_max in [("Ground (10m)", t_max_ground), ("Drop tower (100m)", t_max_drop)]:
    t_actual = np.minimum(t_opt_arr, t_max)
    DeltaV = np.exp(-Lambda_env_arr * t_actual) - np.exp(-(Lambda_env_arr + Lambda_USL_arr) * t_actual)
    V_env = np.exp(-Lambda_env_arr * t_actual)
    N_3sig = np.where(DeltaV > 0, 9 * V_env**2 / DeltaV**2, np.inf)

    idx_1k = np.argmax(N_3sig < 1000)
    if N_3sig[idx_1k] < 1000:
        print(f"   {platform}: first at m = {masses_fg[idx_1k]} fg, N = {N_3sig[idx_1k]:.0f}")

# Where protocol becomes limiting
print(f"\n5. Protocol difficulty thresholds:")
for i in range(len(masses_fg)):
    mf = masses_fg[i]
    xzpf = x_zpf_arr[i]
    t_inv = t_inv_arr[i]

    # Inverted potential expansion: need to create l = 10 nm from x_zpf
    expansion_ratio = l / xzpf
    # This ratio must be achievable without losing coherence

    if expansion_ratio > 10000:
        difficulty = "EXTREMELY HARD"
    elif expansion_ratio > 3000:
        difficulty = "VERY HARD"
    elif expansion_ratio > 1000:
        difficulty = "HARD"
    elif expansion_ratio > 300:
        difficulty = "MODERATE"
    else:
        difficulty = "ACHIEVABLE"

    print(f"   m = {mf:3.0f} fg: x_zpf = {xzpf*1e12:.1f} pm, expansion ratio = {expansion_ratio:.0f}x, difficulty: {difficulty}")

# ============================================================
# COMBINED OPTIMUM
# ============================================================
print("\n" + "=" * 100)
print("COMBINED OPTIMUM ANALYSIS")
print("=" * 100)

# Define a combined figure of merit:
# FoM = (USL/gas ratio) * (visibility survival during creation) * (1 / expansion_ratio_penalty)
# The expansion ratio penalty captures protocol difficulty

expansion_ratio_arr = l / x_zpf_arr

# Penalty: exponential above a threshold ratio
# Protocol gets hard above ~1000x expansion
expansion_penalty_arr = np.exp(-np.maximum(expansion_ratio_arr - 1000, 0) / 3000)

# Combined FoM for inverted potential protocol
FoM_arr = ratio_gas_arr * V_surv_inv_arr * expansion_penalty_arr

print(f"\n{'m(fg)':>6s} {'USL/gas':>10s} {'V_surv':>10s} {'exp_ratio':>10s} {'exp_penalty':>12s} {'FoM':>12s}")
print(f"{'-'*6} {'-'*10} {'-'*10} {'-'*10} {'-'*12} {'-'*12}")

for i in range(len(masses_fg)):
    print(f"{masses_fg[i]:6.0f} {ratio_gas_arr[i]:10.3f} {V_surv_inv_arr[i]:10.6f} {expansion_ratio_arr[i]:10.0f} {expansion_penalty_arr[i]:12.4f} {FoM_arr[i]:12.4f}")

best_fom_idx = np.argmax(FoM_arr)
print(f"\nPeak FoM at m = {masses_fg[best_fom_idx]} fg")
print(f"  USL/gas = {ratio_gas_arr[best_fom_idx]:.2f}")
print(f"  Visibility survival = {V_surv_inv_arr[best_fom_idx]:.6f}")
print(f"  Expansion ratio = {expansion_ratio_arr[best_fom_idx]:.0f}x")

# ============================================================
# SECONDARY SCAN: PRESSURE SENSITIVITY
# ============================================================
print("\n" + "=" * 100)
print("PRESSURE SENSITIVITY (at optimal mass)")
print("=" * 100)

m_opt = masses_kg[best_fom_idx]
R_opt = R_arr[best_fom_idx]

pressures = [1e-12, 5e-13, 1e-13, 5e-14, 1e-14, 5e-15, 1e-15]

print(f"\nAt m = {masses_fg[best_fom_idx]} fg (R = {R_opt*1e9:.0f} nm):")
print(f"\n{'P (Pa)':>12s} {'P (mbar)':>12s} {'L_gas':>12s} {'L_USL':>12s} {'USL/gas':>10s} {'DeltaV(10s)':>12s}")
print(f"{'-'*12} {'-'*12} {'-'*12} {'-'*12} {'-'*10} {'-'*12}")

L_USL_opt = Lambda_USL_arr[best_fom_idx]

for P in pressures:
    n_g = P / (k_B * T_env)
    L_g = n_g * np.pi * R_opt**2 * v_th
    ratio_p = L_USL_opt / L_g
    t_int_p = min(1/L_g, t_max_ground)
    dV = np.exp(-L_g * t_int_p) - np.exp(-(L_g + L_USL_opt) * t_int_p)
    print(f"{P:12.0e} {P*1e5:12.0e} {L_g:12.4e} {L_USL_opt:12.4e} {ratio_p:10.2f} {dV:12.4e}")

# ============================================================
# FINAL VERDICT
# ============================================================
print("\n" + "=" * 100)
print("PART VI — FINAL VERDICT")
print("=" * 100)

print(f"\n*** THEORY-ONLY OPTIMUM ***")
print(f"  USL/gas ~ m^{{4/3}} → monotonically increasing")
print(f"  No upper limit from decoherence alone up to ~100 fg")
print(f"  At 100 fg: USL/gas = {ratio_gas_arr[-1]:.1f}, Lambda_USL = {Lambda_USL_arr[-1]:.2e}")

print(f"\n*** PROTOCOL-LIMITED OPTIMUM ***")
print(f"  Optimal mass: {masses_fg[best_fom_idx]} fg")
print(f"  Diameter: {diam_arr[best_fom_idx]*1e9:.0f} nm")
print(f"  USL/gas: {ratio_gas_arr[best_fom_idx]:.2f}")
print(f"  Expansion ratio: {expansion_ratio_arr[best_fom_idx]:.0f}x (from x_zpf to 10 nm)")
print(f"  Protocol difficulty: {'MODERATE' if expansion_ratio_arr[best_fom_idx] < 3000 else 'HARD'}")

# The key insight: protocol difficulty (expansion ratio) grows as m^{1/2}
# while USL advantage grows as m^{4/3}
# So the FoM keeps growing until expansion ratio penalty kicks in hard
# For the exponential penalty model, this happens around expansion_ratio ~ 3000-5000
# which corresponds to x_zpf ~ 2-3 pm, or m ~ 20-40 fg at 100 kHz

print(f"\n*** THE WINDOW ***")
print(f"  Lower edge: ~7 fg (USL first exceeds gas)")
print(f"  Sweet spot: ~{masses_fg[best_fom_idx]} fg (best FoM)")
print(f"  Upper practical edge: ~40-50 fg (expansion ratio > 5000x)")
print(f"  Physics ceiling: ~500 fg (Mie scattering onset, thermal emission grows)")

# Does window widen above 10 fg?
if best_fom_idx > np.searchsorted(masses_fg, 10):
    answer = "YES — optimal is above 10 fg"
elif best_fom_idx == np.searchsorted(masses_fg, 10):
    answer = "10 fg is near-optimal"
else:
    answer = "NO — optimal is below 10 fg"

print(f"\n  Does the window widen above 10 fg? {answer}")
print(f"  Preferred target mass: {masses_fg[best_fom_idx]} fg ({diam_arr[best_fom_idx]*1e9:.0f} nm diameter)")

print(f"\n" + "=" * 100)
print(f"END OF COMPUTATION")
print(f"=" * 100)
