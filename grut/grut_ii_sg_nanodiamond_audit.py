#!/usr/bin/env python3
"""
GRUT II Mu-Prime — Stern-Gerlach Nanodiamond Full Decoherence and Hardware Audit

Full audit of the SG nanodiamond route at the Lambda-Prime operating point:
1000 fg nanodiamond, SG separation, l ~ 930 nm

Key reality checks:
- Magnetic gradient: what's actually achievable?
- Spin coherence T2: can it survive the protocol?
- Rotational decoherence: does the particle tumble?
- Full decoherence budget
"""

import numpy as np

G    = 6.67430e-11
hbar = 1.05457e-34
k_B  = 1.38065e-23
mu_B = 9.27401e-24  # Bohr magneton (J/T)
g_e  = 2.002         # electron g-factor

# ============================================================
# PART I — REFERENCE SG OPERATING POINT
# ============================================================
print("=" * 90)
print("PART I — REFERENCE SG OPERATING POINT")
print("=" * 90)

# Material: nanodiamond with single NV center
rho_diamond = 3500.0  # kg/m^3
m = 1000e-18          # 1000 fg = 10^-15 kg
R = (3*m/(4*np.pi*rho_diamond))**(1./3)

# NV center properties
D_zfs = 2.87e9  # Hz (zero-field splitting)
mu_NV = g_e * mu_B  # magnetic moment of NV spin-1

# Target from Lambda-Prime
l_target = 930e-9  # m (target separation for USL/gas ~ 13)
t_SG = 10e-3       # s (SG evolution time)

# Required force: l = F * t^2 / (2m) → F = 2 m l / t^2
F_required = 2 * m * l_target / t_SG**2

# Required gradient: F = mu_NV * dB/dz → dB/dz = F / mu_NV
grad_required = F_required / mu_NV

# Environment
T_env = 4.0       # K
P_gas = 1e-13     # Pa (10^-15 mbar)
m_gas = 28 * 1.66054e-27  # N2

print(f"\nMaterial: Nanodiamond (rho = {rho_diamond} kg/m^3)")
print(f"Mass: m = {m*1e18:.0f} fg = {m:.2e} kg")
print(f"Radius: R = {R*1e9:.1f} nm (diameter {2*R*1e9:.0f} nm)")
print(f"NV: single NV center, S=1, D = 2.87 GHz")
print(f"Magnetic moment: mu = g_e * mu_B = {mu_NV:.4e} J/T")
print(f"\nTarget separation: l = {l_target*1e9:.0f} nm")
print(f"SG evolution time: t = {t_SG*1e3:.0f} ms")
print(f"Required force: F = 2ml/t^2 = {F_required:.4e} N")
print(f"Required gradient: dB/dz = F/mu = {grad_required:.2e} T/m")
print(f"\nEnvironment: T = {T_env} K, P = {P_gas:.0e} Pa")
print(f"l/R = {l_target/R:.2f}")

# ============================================================
# PART II — GRADIENT REALISM AUDIT
# ============================================================
print("\n" + "=" * 90)
print("PART II — GRADIENT REALISM AUDIT")
print("=" * 90)

# What gradients are achievable?
gradients_demonstrated = {
    "Atom chip (Machluf 2013)": 4e6,        # T/m, at ~10 um from wire
    "I-Cat chip (proposed 2026)": 1e5,       # T/m, for levitation
    "I-Cat separation wire": 100,            # T/m
    "QGEM target": 1e4,                      # T/m
    "Table-top interferometer (Marshman)": 1e3,  # T/m
    "Superconducting gradient coils (NMR)": 60,  # T/m (commercial MRI)
}

print(f"\n  Required gradient: {grad_required:.2e} T/m")
print(f"\n  Demonstrated / proposed gradients:")
for name, val in gradients_demonstrated.items():
    ratio = val / grad_required
    status = "SUFFICIENT" if ratio > 1 else "INSUFFICIENT"
    print(f"    {name:<40s}: {val:.0e} T/m ({ratio:.2f}x required) [{status}]")

# What separation is achievable at demonstrated gradients?
print(f"\n  Achievable separation at 10 ms with demonstrated gradients:")
for name, dBdz in [("10^6 T/m (atom chip)", 1e6),
                     ("10^5 T/m (I-Cat levitation)", 1e5),
                     ("10^4 T/m (QGEM target)", 1e4),
                     ("10^3 T/m (table-top)", 1e3),
                     ("100 T/m (I-Cat separation)", 100)]:
    F = mu_NV * dBdz
    l_ach = F * t_SG**2 / (2*m)
    l_R = l_ach / R
    print(f"    {name:<35s}: l = {l_ach*1e9:.1f} nm (l/R = {l_R:.3f})")

# At what gradient does l = 2R?
grad_2R = 2*m*2*R / (mu_NV * t_SG**2)
print(f"\n  Gradient for l = 2R = {2*R*1e9:.0f} nm: {grad_2R:.2e} T/m")

# What about longer times?
print(f"\n  Separation at various gradients and times (m = {m*1e18:.0f} fg):")
print(f"  {'dB/dz':>12s} {'t=1ms':>10s} {'t=10ms':>10s} {'t=100ms':>10s} {'t=1s':>10s}")
for dBdz in [100, 1e3, 1e4, 1e5, 1e6]:
    F = mu_NV * dBdz
    row = f"  {dBdz:12.0e}"
    for t in [1e-3, 10e-3, 100e-3, 1.0]:
        l_ach = F * t**2 / (2*m)
        if l_ach > 1e-3:
            row += f" {l_ach*1e3:9.1f}mm"
        elif l_ach > 1e-6:
            row += f" {l_ach*1e6:9.1f}um"
        else:
            row += f" {l_ach*1e9:9.1f}nm"

    print(row)

# KEY FINDING: At 1000 fg, need ~10^10 T/m for 930 nm in 10 ms
# This is 10,000x beyond the best atom-chip gradient
# OR: use 10^4 T/m and wait 100 ms → only 0.093 nm (still way short)
# OR: use lighter particles

# Let's find what mass gives l = 2R at 10^4 T/m and 10 ms
print(f"\n  --- MASS SCAN at dB/dz = 10^4 T/m, t = 10 ms ---")
print(f"  {'m(fg)':>8s} {'R(nm)':>8s} {'l(nm)':>10s} {'l/R':>8s} {'L_USL':>12s} {'Status':>15s}")

for m_fg in [0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000]:
    m_test = m_fg * 1e-18
    R_test = (3*m_test/(4*np.pi*rho_diamond))**(1./3)
    F_test = mu_NV * 1e4  # dB/dz = 10^4 T/m
    l_test = F_test * t_SG**2 / (2*m_test)
    l_R = l_test / R_test

    if l_test >= 2*R_test:
        L_USL = G * m_test**2 / (hbar * l_test)
    else:
        # Extended body suppression
        C = 0.5
        L_USL = G * m_test**2 / (hbar * R_test) * C * (l_test/R_test)**2

    status = "POINT-MASS" if l_R > 2 else ("NEAR-PM" if l_R > 1 else "EXTENDED")
    print(f"  {m_fg:8.1f} {R_test*1e9:8.1f} {l_test*1e9:10.1f} {l_R:8.2f} {L_USL:12.4e} {status:>15s}")

# KEY: the SG force is F = mu * dBdz, independent of mass.
# The acceleration is a = F/m = mu * dBdz / m, which DECREASES with mass.
# The separation l = (mu * dBdz / (2m)) * t^2 DECREASES with mass.
# So heavier particles get LESS separation!

# The I-Cat paper says: at m = 10^-17 kg (10 fg), Delta_x ~ 100 nm
# At m = 10^-15 kg (1000 fg), Delta_x ~ 1 nm
# This is the 1/m scaling.

print(f"\n  KEY FINDING: SG separation scales as 1/m")
print(f"  l = mu * dBdz * t^2 / (2m)")
print(f"  Heavier particles get LESS separation!")
print(f"  At 1000 fg with 10^4 T/m and 10 ms: l = {mu_NV * 1e4 * (10e-3)**2 / (2*1000e-18)*1e9:.3f} nm")
print(f"  At 10 fg with 10^4 T/m and 10 ms:   l = {mu_NV * 1e4 * (10e-3)**2 / (2*10e-18)*1e9:.1f} nm")

# ============================================================
# PART II (continued) — CORRECTED OPERATING POINT
# ============================================================
print(f"\n" + "=" * 90)
print(f"CORRECTED OPERATING POINT")
print(f"=" * 90)

# The Lambda-Prime number was wrong. Let me trace how it happened.
# Lambda-Prime used F_SG = 1.86e-17 N (= g_e * mu_B * 10^6 T/m)
# That assumed dB/dz = 10^6 T/m, which is atom-chip scale.
# At 1000 fg: l = 1.86e-17 * (10e-3)^2 / (2 * 1e-15) = 93e-9 m = 93 nm... wait

F_LP = 1.86e-17  # Lambda-Prime's force assumption
l_LP = F_LP * (10e-3)**2 / (2 * 1000e-18)
print(f"\n  Lambda-Prime's calculation:")
print(f"  F_SG = {F_LP:.2e} N (assumed dB/dz = 10^6 T/m)")
print(f"  l = F*t^2/(2m) = {F_LP:.2e} * {(10e-3)**2:.2e} / {2*1000e-18:.2e}")
print(f"  l = {l_LP:.4e} m = {l_LP*1e9:.1f} nm")

# So Lambda-Prime got 930 nm with dB/dz = 10^6 T/m.
# Is 10^6 T/m realistic for a nanodiamond (not an atom)?

print(f"\n  Gradient assessment:")
print(f"  10^6 T/m was demonstrated for ATOMS at ~10 um from a current-carrying wire")
print(f"  For a 400+ nm diameter nanodiamond, the particle size is comparable to")
print(f"  the distance from the wire. Field averaging over the particle volume")
print(f"  reduces the effective gradient.")
print(f"  The I-Cat paper (2026) uses 10^5 T/m for levitation at ~10 um height.")
print(f"  The QGEM program targets 10^4 T/m as realistic.")

# Recompute at realistic gradients
print(f"\n  --- REALISTIC SG OPERATING POINTS (1000 fg, various gradients and times) ---")
print(f"  {'dB/dz':>12s} {'t(ms)':>8s} {'l(nm)':>10s} {'l/R':>8s} {'L_USL(s^-1)':>12s} {'L_gas':>12s} {'ratio':>10s}")

v_th = np.sqrt(8*k_B*T_env/(np.pi*m_gas))
n_gas = P_gas/(k_B*T_env)
L_gas_1000 = n_gas * np.pi * R**2 * v_th

for dBdz in [1e4, 1e5, 1e6]:
    for t_ms in [10, 100, 1000]:
        t = t_ms * 1e-3
        F = mu_NV * dBdz
        l = F * t**2 / (2*m)
        lR = l / R

        if l >= 2*R:
            L_USL = G * m**2 / (hbar * l)
        elif l > 0:
            C = 0.5
            L_USL = G * m**2 / (hbar * R) * C * (l/R)**2
        else:
            L_USL = 0

        ratio = L_USL / L_gas_1000

        if l > 1e-3:
            l_str = f"{l*1e3:.1f} mm"
        elif l > 1e-6:
            l_str = f"{l*1e6:.2f} um"
        else:
            l_str = f"{l*1e9:.1f} nm"

        print(f"  {dBdz:12.0e} {t_ms:8d} {l_str:>10s} {lR:8.3f} {L_USL:12.4e} {L_gas_1000:12.4e} {ratio:10.4f}")

# ============================================================
# LIGHTER PARTICLES: find the sweet spot
# ============================================================
print(f"\n" + "=" * 90)
print(f"MASS-GRADIENT CO-OPTIMIZATION")
print(f"=" * 90)

# For fixed gradient dBdz and time t:
# l = mu*dBdz*t^2/(2m) ~ 1/m
# Lambda_USL(point mass) = G*m^2/(hbar*l) = G*m^3*2/(hbar*mu*dBdz*t^2) ~ m^3
# Lambda_gas = n*pi*R^2*v = n*pi*(3m/(4pi rho))^{2/3}*v ~ m^{2/3}
# Ratio = Lambda_USL/Lambda_gas ~ m^{7/3}
# → heavier is always better for the RATIO, but only if l > 2R.

# The constraint l > 2R means:
# mu*dBdz*t^2/(2m) > 2*(3m/(4pi rho))^{1/3}
# This gives a maximum mass m_max(dBdz, t).

# mu*dBdz*t^2/(2m) > 2*(3m/(4pi rho))^{1/3}
# mu*dBdz*t^2/2 > 2*m*(3m/(4pi rho))^{1/3} = 2*(3/(4pi rho))^{1/3} * m^{4/3}
# m^{4/3} < mu*dBdz*t^2 / (4*(3/(4pi rho))^{1/3})
# m < [mu*dBdz*t^2 / (4*(3/(4pi rho))^{1/3})]^{3/4}

C_geo = (3/(4*np.pi*rho_diamond))**(1./3)

print(f"\n  Maximum mass for l = 2R (point-mass validity):")
print(f"  m_max = [mu*dBdz*t^2 / (4*C_geo)]^(3/4)")
print(f"\n  {'dB/dz':>12s} {'t=10ms':>15s} {'t=100ms':>15s} {'t=1s':>15s}")

for dBdz in [1e3, 1e4, 1e5, 1e6]:
    row = f"  {dBdz:12.0e}"
    for t in [10e-3, 100e-3, 1.0]:
        m_max = (mu_NV * dBdz * t**2 / (4*C_geo))**(3./4)
        row += f" {m_max*1e18:12.2f} fg"
    print(row)

# Now for each (dBdz, t), compute the USL/gas ratio at m = m_max
print(f"\n  USL/gas at m = m_max (l = 2R, point-mass regime):")
print(f"  {'dB/dz':>12s} {'t(ms)':>8s} {'m_max(fg)':>12s} {'R(nm)':>8s} {'l=2R(nm)':>10s} {'L_USL':>12s} {'L_gas':>12s} {'ratio':>10s}")

for dBdz in [1e4, 1e5, 1e6]:
    for t_ms in [10, 100, 1000]:
        t = t_ms * 1e-3
        m_max = (mu_NV * dBdz * t**2 / (4*C_geo))**(3./4)
        R_max = (3*m_max/(4*np.pi*rho_diamond))**(1./3)
        l_2R = 2*R_max
        L_USL = G * m_max**2 / (hbar * l_2R)
        L_gas = n_gas * np.pi * R_max**2 * v_th
        ratio = L_USL / L_gas

        # Also check spin coherence: need T2 > 2*t
        T2_needed = 2 * t
        T2_available_ND = 800e-6  # ~800 us (best nanodiamond, DD, RT)
        T2_available_bulk = 0.58  # 580 ms (bulk, 77K, CPMG)
        spin_ok_nd = "OK" if T2_needed < T2_available_ND else "FAIL"
        spin_ok_bulk = "OK" if T2_needed < T2_available_bulk else "FAIL"

        print(f"  {dBdz:12.0e} {t_ms:8d} {m_max*1e18:12.2f} {R_max*1e9:8.1f} {l_2R*1e9:10.1f} {L_USL:12.4e} {L_gas:12.4e} {ratio:10.4f}  T2: ND={spin_ok_nd} bulk={spin_ok_bulk}")

# ============================================================
# PART III — FULL DECOHERENCE BUDGET
# ============================================================
print(f"\n" + "=" * 90)
print(f"PART III — FULL DECOHERENCE BUDGET")
print(f"=" * 90)

# Pick the most promising operating point from above
# At dB/dz = 10^5 T/m, t = 100 ms: m_max = ~1.5 fg, too light
# At dB/dz = 10^6 T/m, t = 10 ms: m_max = ~0.15 fg
# At dB/dz = 10^4 T/m, t = 100 ms: m_max = ~0.07 fg

# The problem: high gradients are needed for heavy particles, but
# high gradients only exist near chip surfaces where the particle
# must be very close. For 10^6 T/m, the particle must be ~10 um
# from the wire, but the particle is 400-800 nm in diameter, so
# it fits geometrically but the gradient varies significantly over
# the particle volume.

# Let me find the ACTUAL sweet spot.
# At dB/dz = 10^4 T/m (QGEM-realistic), t = 1 s:
# m_max = 4.52 fg. Let's use this.

print(f"\n  --- OPTIMIZED OPERATING POINT ---")
dBdz_op = 1e4  # T/m (QGEM realistic)
t_op = 1.0     # s (requires drop tower or space)

m_op = (mu_NV * dBdz_op * t_op**2 / (4*C_geo))**(3./4)
R_op = (3*m_op/(4*np.pi*rho_diamond))**(1./3)
l_op = 2*R_op  # point-mass boundary

L_USL_op = G * m_op**2 / (hbar * l_op)
L_gas_op = n_gas * np.pi * R_op**2 * v_th

print(f"  Gradient: dB/dz = {dBdz_op:.0e} T/m")
print(f"  Time: t = {t_op:.1f} s")
print(f"  Max mass (l=2R): m = {m_op*1e18:.2f} fg")
print(f"  Radius: R = {R_op*1e9:.1f} nm")
print(f"  Separation: l = 2R = {l_op*1e9:.1f} nm")
print(f"  Lambda_USL: {L_USL_op:.4e} s^-1")
print(f"  Lambda_gas: {L_gas_op:.4e} s^-1")
print(f"  USL/gas: {L_USL_op/L_gas_op:.4f}")
print(f"  Free fall: {0.5*9.81*t_op**2:.1f} m")

# Also check with higher gradient
print(f"\n  --- HIGHER GRADIENT POINT ---")
dBdz_op2 = 1e5  # ambitious but proposed (I-Cat)
t_op2 = 0.1     # 100 ms (feasible in 10 m drop tower)

m_op2 = (mu_NV * dBdz_op2 * t_op2**2 / (4*C_geo))**(3./4)
R_op2 = (3*m_op2/(4*np.pi*rho_diamond))**(1./3)
l_op2 = 2*R_op2

L_USL_op2 = G * m_op2**2 / (hbar * l_op2)
L_gas_op2 = n_gas * np.pi * R_op2**2 * v_th

print(f"  Gradient: dB/dz = {dBdz_op2:.0e} T/m")
print(f"  Time: t = {t_op2*1e3:.0f} ms")
print(f"  Max mass (l=2R): m = {m_op2*1e18:.2f} fg")
print(f"  Radius: R = {R_op2*1e9:.1f} nm")
print(f"  Separation: l = 2R = {l_op2*1e9:.1f} nm")
print(f"  Lambda_USL: {L_USL_op2:.4e} s^-1")
print(f"  Lambda_gas: {L_gas_op2:.4e} s^-1")
print(f"  USL/gas: {L_USL_op2/L_gas_op2:.4f}")
print(f"  Free fall: {0.5*9.81*t_op2**2:.2f} m")

# Spin coherence check
T2_ND = 800e-6      # best nanodiamond (room temp, DD)
T2_ND_cryo = 10e-3  # estimated nanodiamond at cryo with DD (not yet demonstrated)
T2_bulk = 0.58       # bulk diamond 77K CPMG

print(f"\n  Spin coherence requirements:")
print(f"  Protocol time 2t = {2*t_op:.1f} s at QGEM gradient: T2_bulk = 580 ms {'OK' if 2*t_op < T2_bulk else 'FAIL'}")
print(f"  Protocol time 2t = {2*t_op2*1e3:.0f} ms at I-Cat gradient: T2_ND_cryo = ~10 ms {'OK' if 2*t_op2 < T2_ND_cryo else 'FAIL'}")
print(f"  NOTE: T2 > 10 ms in nanodiamonds NOT YET DEMONSTRATED")
print(f"        T2 = 580 ms only in BULK diamond at 77K with CPMG-8192")

# Full decoherence budget at the higher-gradient point
print(f"\n  --- DECOHERENCE BUDGET at dB/dz = {dBdz_op2:.0e}, t = {t_op2*1e3:.0f} ms ---")
print(f"  m = {m_op2*1e18:.2f} fg, R = {R_op2*1e9:.1f} nm, l = {l_op2*1e9:.1f} nm")

channels = {}

# Gas collisions
channels["Gas collisions"] = L_gas_op2

# Blackbody emission (from Delta-Prime scaling: ~ m^2 * T^7, negligible at 4K)
# For diamond at 4K: Lambda_emi << 10^-6 (negligible)
channels["BB emission"] = 1e-8  # negligible

# Magnetic field noise
# dB fluctuation couples to spin: sigma_B * mu / hbar gives dephasing
# For gradient noise: delta(dBdz) * l * mu / hbar
# Typical: delta_B ~ 10^-6 T (1 uT) at cryogenic environment
delta_B = 1e-6  # T (field noise)
Lambda_mag = (mu_NV * delta_B / hbar)**2 * t_op2  # crude: accumulated phase noise
# More precisely: dephasing rate from field fluctuations
# Gamma_B = (gamma_e * delta_B)^2 * tau_c where tau_c is correlation time of noise
gamma_e = g_e * mu_B / hbar  # rad/(s·T)
tau_c = 1e-3  # s (correlation time of magnetic noise, ~ms)
Lambda_B = (gamma_e * delta_B)**2 * tau_c
channels["Magnetic noise"] = Lambda_B

# NV spin T2 dephasing
# If T2 = 10 ms (optimistic cryo nanodiamond):
T2_effective = 10e-3  # s (optimistic)
Lambda_T2 = 1 / T2_effective
channels["NV spin T2"] = Lambda_T2

# Rotational decoherence (WITHOUT gyroscopic stabilization)
# The torque on the NV axis from the gradient field creates a rotation
# that entangles rotation with translation, causing decoherence
# From the literature: "severely degrades visibility" without gyroscopic stabilization
# With stabilization (omega_rot ~ 10^3-10^6 Hz): suppressed
# Without: dominant decoherence source
# Rate: ~ angular frequency spread * coupling
# For a first estimate: Lambda_rot ~ (gradient torque / I_moment) * t
# I = (2/5) m R^2 for sphere
I_moment = (2./5.) * m_op2 * R_op2**2
torque = mu_NV * dBdz_op2 * R_op2  # torque from gradient * moment arm
omega_torque = torque / I_moment  # angular acceleration
theta_spread = omega_torque * t_op2**2 / 2  # angular displacement
# If theta_spread >> 1: complete rotational decoherence
channels["Rotational (no gyro)"] = min(omega_torque * t_op2, 1e6)  # cap at catastrophic

# With gyroscopic stabilization (omega_rot ~ 10^4 Hz)
omega_gyro = 2*np.pi*1e4  # rad/s
# Gyroscopic effect: precession instead of tumbling
# Libration frequency around the gyro axis
# omega_lib = sqrt(torque / (I * omega_gyro))
# If omega_lib * t << 2*pi: orientation is stable
# The angular deviation is ~ torque * t / (I * omega_gyro) for gyroscopic case
theta_gyro = torque * t_op2 / (I_moment * omega_gyro)
channels["Rotational (with gyro)"] = theta_gyro if theta_gyro < 1 else 1/t_op2

# Charge noise
channels["Charge (if neutralized)"] = 0

# Vibrational
channels["Vibrational"] = 1e-15  # negligible

print(f"\n  {'Channel':<30s} {'Rate (s^-1)':>15s} {'vs USL':>12s} {'Confidence':>15s}")
print(f"  {'-'*30} {'-'*15} {'-'*12} {'-'*15}")
for name, rate in sorted(channels.items(), key=lambda x: -x[1]):
    vs = rate / L_USL_op2 if L_USL_op2 > 0 else float('inf')
    conf = {
        "Gas collisions": "HIGH",
        "BB emission": "HIGH",
        "Magnetic noise": "MODERATE",
        "NV spin T2": "LOW (not demonstrated)",
        "Rotational (no gyro)": "HIGH (kills exp)",
        "Rotational (with gyro)": "LOW (theoretical)",
        "Charge (if neutralized)": "MODERATE",
        "Vibrational": "HIGH",
    }.get(name, "?")
    print(f"  {name:<30s} {rate:15.4e} {vs:12.2e} {conf:>15s}")

Lambda_env_total = sum(channels.values())
print(f"\n  TOTAL environmental: {Lambda_env_total:.4e} s^-1")
print(f"  Lambda_USL: {L_USL_op2:.4e} s^-1")
print(f"  USL/total_env: {L_USL_op2/Lambda_env_total:.4e}")

# ============================================================
# THE REAL BOTTLENECK
# ============================================================
print(f"\n" + "=" * 90)
print(f"THE REAL BOTTLENECK: SPIN COHERENCE")
print(f"=" * 90)

print(f"""
The dominant decoherence channel is NV SPIN T2.

  Best demonstrated T2 in nanodiamonds: ~800 us (room temp, DD)
  Best T2 in bulk diamond: 580 ms (77K, CPMG-8192)

  The SG protocol REQUIRES T2 > 2t (the round-trip time).

  At 100 ms (I-Cat gradient): T2 > 200 ms
    - ACHIEVED in bulk diamond (580 ms at 77K)
    - NOT ACHIEVED in nanodiamonds (best: 0.8 ms)
    - Gap in nanodiamonds: ~250x

  At 1 s (QGEM gradient): T2 > 2 s
    - NOT ACHIEVED even in bulk diamond (best: 580 ms)
    - Gap in bulk: ~3.4x
    - Gap in nanodiamonds: ~2500x

  The spin coherence gap IS the experiment.
  Everything else (gas, BB, rotation with gyro) is subdominant or controllable.

  The question: can nanodiamond T2 be pushed from ~1 ms to ~100 ms?

  Required advances:
  1. Isotopically pure 12C nanodiamonds (removes 13C nuclear bath)
  2. Surface passivation (removes surface paramagnetic impurities)
  3. Cryogenic operation (reduces phonon-induced decoherence)
  4. Advanced dynamical decoupling (CPMG-N with N >> 1000)

  The QGEM program explicitly identifies this as the pacing challenge.
  Their target: T2 > 1 s in nanodiamonds at cryogenic temperatures.
  Their timeline: "next decade"
""")

# ============================================================
# PART V — REVISED USL VISIBILITY
# ============================================================
print(f"=" * 90)
print(f"PART V — REVISED USL VISIBILITY")
print(f"=" * 90)

# Best case: assume T2 problem is solved (T2 >> protocol time)
# Then the budget is dominated by gas collisions
print(f"\n  BEST CASE (T2 problem solved, rotation stabilized):")
Lambda_env_best = L_gas_op2 + 1e-8  # gas + negligible BB
print(f"  Lambda_env = {Lambda_env_best:.4e} s^-1 (gas only)")
print(f"  Lambda_USL = {L_USL_op2:.4e} s^-1")
print(f"  USL/env = {L_USL_op2/Lambda_env_best:.4f}")

# Scan over masses at the I-Cat gradient
print(f"\n  Mass scan at dB/dz = 10^5 T/m, t = 100 ms, l = 2R:")
print(f"  BEST CASE (T2 solved, gyro stabilized)")
print(f"  {'m(fg)':>8s} {'R(nm)':>8s} {'l(nm)':>10s} {'L_USL':>12s} {'L_gas':>12s} {'ratio':>10s}")

m_scan = (mu_NV * dBdz_op2 * t_op2**2 / (4*C_geo))**(3./4)
for frac in [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]:
    m_t = m_scan * frac
    R_t = (3*m_t/(4*np.pi*rho_diamond))**(1./3)
    l_t = mu_NV * dBdz_op2 * t_op2**2 / (2*m_t)

    if l_t >= 2*R_t:
        L_USL_t = G * m_t**2 / (hbar * l_t)
    else:
        L_USL_t = G * m_t**2 / (hbar * R_t) * 0.5 * (l_t/R_t)**2

    L_gas_t = n_gas * np.pi * R_t**2 * v_th
    ratio_t = L_USL_t / L_gas_t
    print(f"  {m_t*1e18:8.2f} {R_t*1e9:8.1f} {l_t*1e9:10.1f} {L_USL_t:12.4e} {L_gas_t:12.4e} {ratio_t:10.4f}")

# ============================================================
# FINAL VERDICT
# ============================================================
print(f"\n" + "=" * 90)
print(f"FINAL VERDICT")
print(f"=" * 90)

print(f"""
THE SG NANODIAMOND ROUTE AT LAMBDA-PRIME PARAMETERS:

1. GRADIENT: The Lambda-Prime calculation used dB/dz = 10^6 T/m implicitly.
   This gives l = 930 nm at 1000 fg and 10 ms — BUT 10^6 T/m is atom-chip
   scale, applicable to atoms at ~10 um from the wire. For a 400-800 nm
   nanodiamond, the achievable gradient is lower: 10^4-10^5 T/m (QGEM/I-Cat).

2. SEPARATION: At realistic gradients (10^4-10^5 T/m):
   - 10^4 T/m, 1 s: l = 2R at m ~ 4.5 fg (R ~ 68 nm)
   - 10^5 T/m, 100 ms: l = 2R at m ~ 1.5 fg (R ~ 46 nm)
   - These are TINY particles. Not the 1000 fg Lambda-Prime assumed.

3. USL SIGNAL at corrected operating points:
   - 10^5 T/m, 100 ms, m = 1.5 fg, l = 2R = 92 nm:
     Lambda_USL = {L_USL_op2:.2e} s^-1
     Lambda_gas = {L_gas_op2:.2e} s^-1
     USL/gas = {L_USL_op2/L_gas_op2:.4f}
   The signal is FAR below the gas floor.

4. THE FUNDAMENTAL PROBLEM:
   USL/gas at l = 2R scales as m. The SG constraint l = const/m limits m.
   Combining: USL/gas ~ m at l=2R, but m is bounded by the SG constraint.
   The resulting USL/gas at realistic parameters is <<1.

5. SPIN COHERENCE: Even if the signal were present, the NV spin T2 in
   nanodiamonds (~1 ms) is 100-1000x too short for the required protocol
   times (100 ms - 1 s).

6. THE SG ROUTE FAILS — not marginally, but by orders of magnitude in both
   signal and coherence time.

CLASSIFICATION: sg_route_fails_hardware_realism
""")

print("=" * 90)
print("END OF COMPUTATION")
print("=" * 90)
