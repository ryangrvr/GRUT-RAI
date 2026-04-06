#!/usr/bin/env python3
"""
GRUT II Gamma-Prime — Exact USL Prediction for Levitated-Nanoparticle Experiments

Computes Lambda_USL = G m^2 / (hbar l) for the specific parameters of:
1. ETH Zurich (Rossi et al., 2024) — current experimental record
2. SUPER-MARIO protocol (Aspelmeyer/Romero-Isart, PNAS 2024) — near-term proposal
3. Blueprint proposal (arXiv Dec 2025) — optimistic ground-based
4. MAQRO-PF (space, 2030s) — long-term

For each: compares Lambda_USL to the environmental decoherence budget
to determine whether the USL signal is above or below the noise floor.

The decisive question: is there an experiment where Lambda_USL > Lambda_env?
"""

import numpy as np

# ============================================================
# Fundamental constants
# ============================================================
G = 6.67430e-11      # m^3 kg^-1 s^-2
hbar = 1.05457e-34   # J s
k_B = 1.38065e-23    # J/K
c = 2.99792e8        # m/s
amu = 1.66054e-27    # kg

# ============================================================
# USL rate
# ============================================================
def lambda_usl(m, l):
    """Lambda_USL = G m^2 / (hbar l) in s^-1"""
    return G * m**2 / (hbar * l)

def tau_usl(m, l):
    """Decoherence time from USL in seconds"""
    return 1.0 / lambda_usl(m, l)

# ============================================================
# Environmental decoherence rates
# ============================================================
def lambda_gas(m, R, P, T):
    """
    Gas collision decoherence rate (Joos-Zeh).
    Lambda_gas = (16 pi / 3) * P * R^2 / (m_gas * v_th * l^2) ...

    For a sphere of radius R in gas at pressure P, temperature T:
    Scattering rate = n_gas * sigma * v_th
    where n_gas = P/(k_B T), sigma = pi R^2, v_th = sqrt(8 k_B T / (pi m_gas))

    This gives the MOMENTUM decoherence rate. For SPATIAL decoherence
    of a superposition with separation l, the rate is:
    Gamma_gas = (8/3) * P * R^2 / (hbar * sqrt(pi * m_gas * k_B * T)) * l^2

    But for localization (l << thermal de Broglie wavelength of gas):
    Gamma_gas ~ n_gas * sigma * v_th * (l / lambda_dB_gas)^2

    We use the standard result from Romero-Isart et al. (2011):
    Gamma_gas = (16 pi / 3) * P * R^2 * l^2 * sqrt(2 pi m_gas / (k_B T)) / hbar^2

    Actually, the standard Joos-Zeh formula for spatial decoherence at separation l:
    Lambda = (8 * sqrt(2*pi) / 3) * P * R^2 * l^2 * sqrt(m_gas) / (hbar^2 * sqrt(k_B * T))

    For N2 gas molecules.
    """
    m_gas = 28 * amu  # N2
    # Hornberger et al. (2012), Eq. (3.65):
    # Lambda_gas = n * sigma * v_th * F(l)
    # In the short-wavelength limit (l >> lambda_dB of gas, which is ~pm):
    # F(l) -> 1 (full decoherence per scatter)
    # In the long-wavelength limit (l << lambda_dB):
    # F(l) ~ (l / lambda_dB)^2

    # Thermal de Broglie wavelength of gas molecule
    lambda_dB = hbar / np.sqrt(2 * m_gas * k_B * T)

    # Number density
    n_gas = P / (k_B * T)

    # Cross section (geometric)
    sigma = np.pi * R**2

    # Mean thermal speed
    v_th = np.sqrt(8 * k_B * T / (np.pi * m_gas))

    # Scattering rate
    Gamma_scatter = n_gas * sigma * v_th

    return Gamma_scatter, lambda_dB

def lambda_blackbody_emission(R, T_int):
    """
    Blackbody photon emission decoherence rate.
    For a dielectric sphere at internal temperature T_int,
    emitting thermal photons that carry away which-path information.

    Dominant for T_int > ~100 K.

    From Chang et al. (2010), Romero-Isart et al. (2011):
    Gamma_bb ~ (8! * zeta(9) / (9 * pi)) * (k_B T / (hbar c))^9 * R^3 * Im(epsilon) * l^2

    For the RATE (not position-dependent part):
    Gamma_bb = emission_rate * (l / lambda_thermal)^2  when l << lambda_thermal

    We use the simplified estimate from the Blueprint paper:
    Gamma_bb < 10^-4 s^-1 for T_int < 20 K
    """
    # Thermal wavelength of peak emission
    lambda_thermal = hbar * c / (k_B * T_int)  # ~hbar c / kT

    # For silica, Im(epsilon) at thermal frequencies ~ 0.1-1
    # Emission rate for a dielectric sphere:
    # P_emit ~ (4 pi / 3) R^3 * Im(epsilon) * (2 pi k_B T / hbar)^4 / (pi^2 c^3) * sigma_SB * T^4 * ...

    # Use scaling from Romero-Isart (2011) Table I:
    # Gamma_bb = C_bb * R^3 * T_int^6  (for nanospheres, dominant regime)
    # C_bb ~ 10^-36 s^-1 m^-3 K^-6 (approximate from literature fits)

    # More precisely: rate of thermal photon emission
    # n_photon_rate ~ (16 pi^3 / 3) * R^3 * Im(eps) * (k_B T_int)^4 / (hbar^4 c^3 * (2pi)^3)

    # Since exact coefficients depend on material properties, we parametrize:
    # For silica (SiO2), using tabulated values from Jain et al. (2016):
    Im_eps = 0.1  # effective imaginary dielectric constant at thermal freq

    # Photon emission rate (approximate):
    omega_thermal = k_B * T_int / hbar
    n_emit = (4/3) * np.pi * R**3 * Im_eps * omega_thermal**3 / (3 * np.pi**2 * c**3)

    return n_emit, lambda_thermal

def lambda_photon_recoil(P_laser, omega_laser, R):
    """
    Laser photon recoil decoherence rate.
    Scattered photons carry which-path information.

    Gamma_recoil = n_scatter * (1 - sinc(l * k_photon))

    For Rayleigh scattering from a dielectric nanosphere:
    sigma_Rayleigh = (128 pi^5 / 3) * R^6 / lambda^4 * |K|^2
    where K = (eps - 1)/(eps + 2)

    Scattering rate = P_laser * sigma_Rayleigh / (hbar * omega * A_beam)
    """
    # For 1550 nm laser
    lambda_laser = 2 * np.pi * c / omega_laser
    k_laser = omega_laser / c

    # Clausius-Mossotti factor for silica (eps ~ 2.1 at 1550 nm)
    eps = 2.1
    K = (eps - 1) / (eps + 2)

    # Rayleigh cross section
    sigma_R = (128 * np.pi**5 / 3) * R**6 / lambda_laser**4 * K**2

    # Photon flux (approximate, for focused beam)
    # Intensity ~ P / A_beam, A_beam ~ lambda^2
    A_beam = lambda_laser**2  # diffraction-limited focus
    n_photon_flux = P_laser / (hbar * omega_laser * A_beam)

    # Scattering rate
    Gamma_scatter = n_photon_flux * sigma_R

    return Gamma_scatter, sigma_R

# ============================================================
# Experiment definitions
# ============================================================

print("=" * 80)
print("GRUT II Gamma-Prime: Exact USL vs Environmental Decoherence")
print("=" * 80)

experiments = []

# --- Experiment 1: ETH Zurich (Rossi et al., 2024) — ACHIEVED ---
print("\n" + "=" * 80)
print("EXPERIMENT 1: ETH Zurich — Rossi et al. (2024)")
print("Status: ACHIEVED (current experimental record)")
print("=" * 80)

m1 = 1.2e-18  # kg (1.2 fg, 100 nm silica)
R1 = 50e-9    # m (50 nm radius)
l1_achieved = 73e-12  # m (73 pm coherence length — ACHIEVED)
l1_zpf = 17e-12  # m (17 pm zero-point fluctuation)
T1 = 7.0      # K (cryogenic)
P1 = 1e-7     # Pa (10^-9 mbar)
omega_trap1 = 2 * np.pi * 56.5e3  # rad/s (z-axis trap frequency)
P_laser1 = 0.66  # W
omega_laser1 = 2 * np.pi * c / 1550e-9  # rad/s (1550 nm)

# USL prediction at achieved coherence length
L_usl_1a = lambda_usl(m1, l1_achieved)
tau_usl_1a = tau_usl(m1, l1_achieved)

# USL prediction at zero-point fluctuation
L_usl_1z = lambda_usl(m1, l1_zpf)
tau_usl_1z = tau_usl(m1, l1_zpf)

print(f"\nParticle: m = {m1:.2e} kg = {m1/amu:.2e} amu")
print(f"          R = {R1*1e9:.0f} nm")
print(f"Achieved coherence length: l = {l1_achieved*1e12:.0f} pm")
print(f"Zero-point fluctuation:    l = {l1_zpf*1e12:.0f} pm")

print(f"\nUSL at achieved l = {l1_achieved*1e12:.0f} pm:")
print(f"  Lambda_USL = {L_usl_1a:.4e} s^-1")
print(f"  tau_USL    = {tau_usl_1a:.4e} s")

print(f"\nUSL at ZPF l = {l1_zpf*1e12:.0f} pm:")
print(f"  Lambda_USL = {L_usl_1z:.4e} s^-1")
print(f"  tau_USL    = {tau_usl_1z:.4e} s")

# Environmental rate (measured)
Gamma_env_1 = 23.7e3  # phonons/s (measured total decoherence rate)
print(f"\nMeasured total decoherence: Gamma_env = {Gamma_env_1:.2e} s^-1")
print(f"\nRatio Lambda_USL / Gamma_env = {L_usl_1a / Gamma_env_1:.4e}")
print(f"USL is {Gamma_env_1 / L_usl_1a:.2e}x BELOW environmental noise floor")

# --- Experiment 2: SUPER-MARIO protocol (PNAS 2024) — PROPOSED ---
print("\n" + "=" * 80)
print("EXPERIMENT 2: SUPER-MARIO Protocol (Aspelmeyer/Romero-Isart, 2024)")
print("Status: PROPOSED — near-term achievable")
print("=" * 80)

# Room-temperature version
m2 = 6e8 * amu  # ~10^-18 kg
R2 = 50e-9  # m
l2_rt = 5e-9  # m (5 nm fringe spacing, room temp)
l2_cryo = 100e-9  # m (100 nm at cryogenic)
T2_rt = 300  # K
T2_cryo = 50  # K
P2_rt = 1e-8  # Pa (10^-10 mbar)
P2_cryo = 1e-11  # Pa (10^-13 mbar)

# Protocol duration
t_protocol = 2.07e-3  # s (2.07 ms total)

print(f"\nParticle: m = {m2:.2e} kg = {m2/amu:.2e} amu")
print(f"          R = {R2*1e9:.0f} nm")

# Room temperature case
L_usl_2rt = lambda_usl(m2, l2_rt)
tau_usl_2rt = tau_usl(m2, l2_rt)

print(f"\n--- Room Temperature Case (T = 300 K, P = 10^-10 mbar) ---")
print(f"Target separation: l = {l2_rt*1e9:.0f} nm")
print(f"  Lambda_USL = {L_usl_2rt:.4e} s^-1")
print(f"  tau_USL    = {tau_usl_2rt:.4e} s")
print(f"  Protocol duration: {t_protocol*1e3:.2f} ms")

# Environmental decoherence during protocol
# Gas collisions at room temp
Gamma_gas_2rt, ldB_2rt = lambda_gas(m2, R2, P2_rt, T2_rt)
print(f"  Gas scattering rate: {Gamma_gas_2rt:.4e} s^-1")
print(f"  Gas thermal de Broglie: {ldB_2rt*1e12:.2f} pm")

# Position-dependent decoherence factor for gas
# Gamma_spatial = Gamma_scatter * (1 - exp(-l^2/(2*ldB^2)))
# For l >> ldB (which is ~pm scale): Gamma_spatial ~ Gamma_scatter
if l2_rt > 10 * ldB_2rt:
    Gamma_gas_spatial_2rt = Gamma_gas_2rt  # full decoherence per scatter
else:
    Gamma_gas_spatial_2rt = Gamma_gas_2rt * (l2_rt / ldB_2rt)**2

print(f"  Gas spatial decoherence at l={l2_rt*1e9:.0f} nm: {Gamma_gas_spatial_2rt:.4e} s^-1")

# Visibility loss during protocol
vis_loss_usl = 1 - np.exp(-L_usl_2rt * t_protocol)
vis_loss_gas = 1 - np.exp(-Gamma_gas_spatial_2rt * t_protocol)
print(f"  Visibility loss from USL during {t_protocol*1e3:.1f} ms: {vis_loss_usl:.6e}")
print(f"  Visibility loss from gas during {t_protocol*1e3:.1f} ms: {vis_loss_gas:.6e}")

# Signal-to-noise
print(f"  Ratio Lambda_USL / Lambda_gas = {L_usl_2rt / Gamma_gas_spatial_2rt:.4e}")

# Cryogenic case
L_usl_2cryo = lambda_usl(m2, l2_cryo)
tau_usl_2cryo = tau_usl(m2, l2_cryo)

print(f"\n--- Cryogenic Case (T = 50 K, P = 10^-13 mbar) ---")
print(f"Target separation: l = {l2_cryo*1e9:.0f} nm")
print(f"  Lambda_USL = {L_usl_2cryo:.4e} s^-1")
print(f"  tau_USL    = {tau_usl_2cryo:.4e} s")

Gamma_gas_2cryo, ldB_2cryo = lambda_gas(m2, R2, P2_cryo, T2_cryo)
if l2_cryo > 10 * ldB_2cryo:
    Gamma_gas_spatial_2cryo = Gamma_gas_2cryo
else:
    Gamma_gas_spatial_2cryo = Gamma_gas_2cryo * (l2_cryo / ldB_2cryo)**2

print(f"  Gas spatial decoherence: {Gamma_gas_spatial_2cryo:.4e} s^-1")
print(f"  Ratio Lambda_USL / Lambda_gas = {L_usl_2cryo / Gamma_gas_spatial_2cryo:.4e}")

# --- Experiment 3: Blueprint (arXiv Dec 2025) — PROPOSED ---
print("\n" + "=" * 80)
print("EXPERIMENT 3: Blueprint for Collapse Tests (arXiv 2512.02838)")
print("Status: PROPOSED — optimistic ground-based")
print("=" * 80)

m3 = 1e-17  # kg
R3 = 50e-9  # m
l3_zpf = 7e-13  # m (zero-point width)
T3 = 5  # K
P3 = 1e-13  # Pa (10^-15 mbar)
t_coherence_target = 10  # s

# Superposition separation targets from this proposal
# They want to distinguish CSL from environmental — need l >> zpf
# Typical target: l ~ 10 nm to 100 nm (via free evolution)
# After free evolution for time t, position spread ~ sqrt(hbar t / m)
# For m = 10^-17 kg, t = 1 s: delta_x = sqrt(1.05e-34 * 1 / 1e-17) = sqrt(1.05e-17) ~ 3 nm
l3_free = np.sqrt(hbar * t_coherence_target / m3)

print(f"\nParticle: m = {m3:.2e} kg = {m3/amu:.2e} amu")
print(f"          R = {R3*1e9:.0f} nm")
print(f"Zero-point width: {l3_zpf*1e12:.1f} pm")
print(f"Free-evolution spread after {t_coherence_target} s: {l3_free*1e9:.2f} nm")

# Environmental budget from the paper
Gamma_env_3 = 3e-3  # s^-1 (total, from paper)
Gamma_gas_3 = 1e-3  # s^-1
Gamma_bb_3 = 1e-4   # s^-1
Gamma_recoil_3 = 1e-3  # s^-1

# USL at zero-point fluctuation
L_usl_3_zpf = lambda_usl(m3, l3_zpf)
# USL at free-evolution spread
L_usl_3_free = lambda_usl(m3, l3_free)
# USL at 10 nm (typical target)
L_usl_3_10nm = lambda_usl(m3, 10e-9)
# USL at 100 nm
L_usl_3_100nm = lambda_usl(m3, 100e-9)

print(f"\nUSL predictions:")
print(f"  At ZPF (l = {l3_zpf*1e12:.1f} pm):  Lambda_USL = {L_usl_3_zpf:.4e} s^-1")
print(f"  At free-evol (l = {l3_free*1e9:.2f} nm): Lambda_USL = {L_usl_3_free:.4e} s^-1")
print(f"  At l = 10 nm:  Lambda_USL = {L_usl_3_10nm:.4e} s^-1")
print(f"  At l = 100 nm: Lambda_USL = {L_usl_3_100nm:.4e} s^-1")

print(f"\nEnvironmental budget (from paper):")
print(f"  Total: Gamma_env = {Gamma_env_3:.2e} s^-1")
print(f"  Gas:   {Gamma_gas_3:.2e} s^-1")
print(f"  BB:    {Gamma_bb_3:.2e} s^-1")
print(f"  Recoil:{Gamma_recoil_3:.2e} s^-1")

print(f"\nRatios Lambda_USL / Gamma_env:")
print(f"  At ZPF:        {L_usl_3_zpf / Gamma_env_3:.4e}")
print(f"  At free-evol:  {L_usl_3_free / Gamma_env_3:.4e}")
print(f"  At 10 nm:      {L_usl_3_10nm / Gamma_env_3:.4e}")
print(f"  At 100 nm:     {L_usl_3_100nm / Gamma_env_3:.4e}")

# CSL prediction for comparison
lambda_CSL = 1e-21  # s^-1 (CSL collapse rate)
r_C = 100e-9  # m (CSL correlation length)
# CSL decoherence: Gamma_CSL ~ lambda_CSL * (m/m_0)^2 * (l/r_C)^2 / (4*pi*r_C^2)
# More precisely from Adler (2007):
# Gamma_CSL = lambda_CSL * (m / m_nucleon)^2 * f(l, R, r_C)
m_nucleon = amu
n_nucleons = m3 / m_nucleon
# For l << r_C and R << r_C:
# Gamma_CSL ~ lambda_CSL * n_nucleons^2 * l^2 / (4 * r_C^2)
Gamma_CSL_10nm = lambda_CSL * n_nucleons**2 * (10e-9)**2 / (4 * r_C**2)

print(f"\nFor comparison — CSL prediction at l = 10 nm:")
print(f"  Gamma_CSL = {Gamma_CSL_10nm:.4e} s^-1")
print(f"  Ratio Lambda_USL / Gamma_CSL (at 10 nm) = {L_usl_3_10nm / Gamma_CSL_10nm:.4e}")

# --- Experiment 4: MAQRO-PF (space, 2030s) ---
print("\n" + "=" * 80)
print("EXPERIMENT 4: MAQRO-PF Space Mission")
print("Status: PROPOSED — 2030s timeline")
print("=" * 80)

m4 = 1e9 * amu  # 10^9 amu ~ 1.66e-18 kg
R4 = 50e-9  # m (approximate)
# Free evolution in space: t ~ 100 s
t_free_4 = 100  # s
l4_free = np.sqrt(hbar * t_free_4 / m4)
# Grating: 405 nm
l4_grating = 405e-9 / 2  # half-grating period ~ 200 nm

T4 = 5  # K (space, shield)
P4 = 1e-11  # Pa (10^-13 mbar)

print(f"\nParticle: m = {m4:.2e} kg = {m4/amu:.2e} amu")
print(f"          R = {R4*1e9:.0f} nm")
print(f"Free-evolution spread after {t_free_4} s: {l4_free*1e9:.3f} nm")
print(f"Grating half-period: {l4_grating*1e9:.0f} nm")

L_usl_4_free = lambda_usl(m4, l4_free)
L_usl_4_grating = lambda_usl(m4, l4_grating)

print(f"\nUSL predictions:")
print(f"  At free-evol spread (l = {l4_free*1e9:.3f} nm): Lambda_USL = {L_usl_4_free:.4e} s^-1")
print(f"  At grating period (l = {l4_grating*1e9:.0f} nm): Lambda_USL = {L_usl_4_grating:.4e} s^-1")

# Environmental in space
Gamma_gas_4, _ = lambda_gas(m4, R4, P4, T4)
print(f"\nEnvironmental:")
print(f"  Gas scattering rate (at {P4:.0e} Pa): {Gamma_gas_4:.4e} s^-1")
print(f"  Target total: < 0.01 s^-1 (for 100 s coherence)")

Gamma_env_4 = 0.01  # target
print(f"\nRatios Lambda_USL / Gamma_env:")
print(f"  At free-evol:  {L_usl_4_free / Gamma_env_4:.4e}")
print(f"  At grating:    {L_usl_4_grating / Gamma_env_4:.4e}")

# ============================================================
# THE DECISIVE ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("DECISIVE ANALYSIS: Where does Lambda_USL exceed Lambda_env?")
print("=" * 80)

# For each mass, find the separation l where Lambda_USL = Lambda_env
def l_crossover(m, Gamma_env):
    """Separation where Lambda_USL = Gamma_env"""
    return G * m**2 / (hbar * Gamma_env)

print("\nCrossover separation l* where Lambda_USL = Gamma_env:")
print("(USL detectable only if experimental separation l < l*)")
print()

cases = [
    ("ETH Zurich (achieved)", m1, Gamma_env_1, l1_achieved),
    ("SUPER-MARIO (RT)", m2, 10.0, l2_rt),  # estimate env rate
    ("Blueprint", m3, Gamma_env_3, 10e-9),
    ("MAQRO-PF", m4, Gamma_env_4, l4_grating),
]

for name, m, G_env, l_exp in cases:
    l_cross = l_crossover(m, G_env)
    L_usl_val = lambda_usl(m, l_exp)
    ratio = L_usl_val / G_env
    detectable = "YES" if ratio > 0.1 else ("MARGINAL" if ratio > 0.01 else "NO")

    print(f"  {name}:")
    print(f"    m = {m:.2e} kg, Gamma_env = {G_env:.2e} s^-1")
    print(f"    l* = {l_cross:.4e} m = {l_cross*1e9:.4e} nm")
    print(f"    Experimental l = {l_exp:.2e} m = {l_exp*1e9:.2e} nm")
    print(f"    Lambda_USL at l_exp = {L_usl_val:.4e} s^-1")
    print(f"    Ratio USL/env = {ratio:.4e}")
    print(f"    Detectable? {detectable}")
    print()

# ============================================================
# PARAMETER SPACE SCAN
# ============================================================
print("=" * 80)
print("PARAMETER SPACE: Required mass × separation for USL detection")
print("=" * 80)

print("\nFor Lambda_USL = Gamma_env (detection threshold):")
print("  G m^2 / (hbar l) = Gamma_env")
print("  m^2 / l = Gamma_env * hbar / G")
print()

for Gamma_target_label, Gamma_target in [("10^-3 (optimistic ground)", 1e-3),
                                           ("10^-2 (MAQRO-like)", 1e-2),
                                           ("10^0 (current tech)", 1.0),
                                           ("10^3 (easily detectable)", 1e3)]:
    m_l_ratio = Gamma_target * hbar / G
    print(f"  Gamma_env = {Gamma_target_label} s^-1:")
    print(f"    m^2/l = {m_l_ratio:.4e} kg^2/m")

    for l_nm in [1, 10, 100, 1000]:
        l_val = l_nm * 1e-9
        m_needed = np.sqrt(m_l_ratio * l_val)
        print(f"    At l = {l_nm:4d} nm: m_needed = {m_needed:.4e} kg = {m_needed/amu:.2e} amu ({m_needed*1e18:.2f} fg)")
    print()

# ============================================================
# THE SPECIFIC DELIC/ASPELMEYER PREDICTION
# ============================================================
print("=" * 80)
print("SPECIFIC PREDICTION: Delic/Aspelmeyer-class experiment")
print("=" * 80)

# Best current platform: 143 nm silica, ~10^-18 kg
# Target protocol: prepare ground state, create superposition via
# pulsed potential, observe interference
m_DA = 1e-18  # kg
R_DA = 71.5e-9  # m (143 nm diameter)

# Scenario A: 10 nm superposition (near-term target)
l_A = 10e-9
L_A = lambda_usl(m_DA, l_A)

# Scenario B: 100 nm superposition (ambitious)
l_B = 100e-9
L_B = lambda_usl(m_DA, l_B)

# Scenario C: 1 nm superposition (conservative)
l_C = 1e-9
L_C = lambda_usl(m_DA, l_C)

print(f"\nPlatform: m = {m_DA:.2e} kg, R = {R_DA*1e9:.1f} nm")

# Environmental decoherence budget for this platform
# Estimate from combination of papers
# At best conditions: P ~ 10^-10 Pa, T ~ 10 K
P_DA = 1e-10  # Pa
T_DA = 10  # K

Gamma_gas_DA, ldB_DA = lambda_gas(m_DA, R_DA, P_DA, T_DA)
print(f"\nEnvironmental decoherence budget (P = {P_DA:.0e} Pa, T = {T_DA} K):")
print(f"  Gas scattering rate: {Gamma_gas_DA:.4e} s^-1")

# At l = 10 nm (>> gas ldB ~ pm)
print(f"  Gas thermal de Broglie: {ldB_DA*1e12:.2f} pm")
print(f"  Since l >> lambda_dB(gas), full decoherence per scatter")
print(f"  Gas spatial decoherence: ~ {Gamma_gas_DA:.2e} s^-1 (independent of l)")

# Blackbody emission at T = 10 K is negligible
print(f"  Blackbody emission (T = {T_DA} K): ~ 10^-6 s^-1 (negligible)")

# Photon recoil
print(f"  Photon recoil: ~ 10^-2 to 10^-1 s^-1 (depends on trap power)")

# Conservative total
Gamma_env_DA = 0.1  # s^-1 (conservative estimate)
Gamma_env_DA_optimistic = 1e-3  # s^-1 (optimistic, Blueprint-level)

print(f"\n  Conservative total: Gamma_env ~ {Gamma_env_DA} s^-1")
print(f"  Optimistic total:  Gamma_env ~ {Gamma_env_DA_optimistic} s^-1")

print(f"\nUSL predictions for Delic/Aspelmeyer-class platform:")
print(f"  {'Scenario':<30s} {'l (nm)':>10s} {'Lambda_USL':>15s} {'tau_USL':>15s} {'vs conservative':>20s} {'vs optimistic':>20s}")
print(f"  {'-'*30} {'-'*10} {'-'*15} {'-'*15} {'-'*20} {'-'*20}")

for label, l_val, L_val in [("C: 1 nm (conservative)", l_C, L_C),
                              ("A: 10 nm (near-term)", l_A, L_A),
                              ("B: 100 nm (ambitious)", l_B, L_B)]:
    tau_val = 1/L_val
    ratio_cons = L_val / Gamma_env_DA
    ratio_opt = L_val / Gamma_env_DA_optimistic
    print(f"  {label:<30s} {l_val*1e9:>10.0f} {L_val:>15.4e} {tau_val:>15.4e} {ratio_cons:>20.4e} {ratio_opt:>20.4e}")

print(f"\n*** CRITICAL FINDING ***")
print(f"At l = {l_A*1e9:.0f} nm (near-term target):")
print(f"  Lambda_USL = {L_A:.4e} s^-1")
print(f"  tau_USL = {1/L_A:.4e} s = {1/L_A*1e3:.4f} ms")
print(f"  This predicts decoherence in {1/L_A*1e3:.2f} ms")
if L_A > Gamma_env_DA:
    print(f"  USL rate EXCEEDS conservative environmental rate by {L_A/Gamma_env_DA:.1f}x")
    print(f"  *** THE USL IS DETECTABLE IN THIS REGIME ***")
elif L_A > Gamma_env_DA_optimistic:
    print(f"  USL rate is {L_A/Gamma_env_DA:.2f}x conservative env")
    print(f"  USL rate EXCEEDS optimistic env by {L_A/Gamma_env_DA_optimistic:.1f}x")
    print(f"  *** MARGINAL: detectable only with optimistic environmental control ***")
else:
    print(f"  USL rate is {L_A/Gamma_env_DA:.4e}x conservative env — BELOW noise floor")

# ============================================================
# SENSITIVITY THRESHOLD
# ============================================================
print("\n" + "=" * 80)
print("SENSITIVITY THRESHOLD: Minimum mass for USL detection")
print("=" * 80)

# For a given separation l and environmental rate Gamma_env,
# the minimum mass for detection is:
# G m^2 / (hbar l) = Gamma_env
# m_min = sqrt(Gamma_env * hbar * l / G)

for l_nm, l_val in [(1, 1e-9), (10, 10e-9), (100, 100e-9)]:
    print(f"\nAt separation l = {l_nm} nm:")
    for Gamma_label, Gamma_val in [("10^-3 s^-1 (optimistic)", 1e-3),
                                    ("10^-1 s^-1 (conservative)", 1e-1),
                                    ("10^1 s^-1 (poor)", 10)]:
        m_min = np.sqrt(Gamma_val * hbar * l_val / G)
        print(f"  Gamma_env = {Gamma_label}: m_min = {m_min:.4e} kg = {m_min/amu:.2e} amu ({m_min*1e18:.3f} fg)")

# ============================================================
# FINAL VERDICT
# ============================================================
print("\n" + "=" * 80)
print("FINAL VERDICT")
print("=" * 80)

# Compute the precise numbers for the most promising scenario
m_best = 1e-17  # kg (Blueprint-class, 10x heavier than current)
l_best = 10e-9  # m (10 nm separation)
Gamma_best = 3e-3  # s^-1 (Blueprint environmental budget)

L_usl_best = lambda_usl(m_best, l_best)
ratio_best = L_usl_best / Gamma_best

print(f"\nMost promising near-term scenario (Blueprint-class):")
print(f"  m = {m_best:.2e} kg, l = {l_best*1e9:.0f} nm")
print(f"  Lambda_USL = {L_usl_best:.4e} s^-1")
print(f"  Gamma_env = {Gamma_best:.2e} s^-1")
print(f"  Ratio = {ratio_best:.4e}")
print(f"  tau_USL = {1/L_usl_best:.4e} s")

if ratio_best > 1:
    print(f"\n  *** USL EXCEEDS environmental noise by {ratio_best:.1f}x ***")
    print(f"  *** THIS EXPERIMENT CAN TEST THE USL ***")
    print(f"  Expected signature: excess decoherence of {L_usl_best:.2e} s^-1")
    print(f"  above the environmental budget of {Gamma_best:.2e} s^-1")
    print(f"  Coherence time with USL: {1/(Gamma_best + L_usl_best):.4f} s")
    print(f"  Coherence time without USL: {1/Gamma_best:.1f} s")
    print(f"  Distinguishable if coherence measured to ~{100*Gamma_best/L_usl_best:.1f}% precision")
else:
    print(f"\n  USL is {1/ratio_best:.0f}x below environmental noise")
    print(f"  NOT detectable at these parameters")

# Current best platform
m_curr = 1e-18  # kg (Delic/Aspelmeyer class)
l_curr = 10e-9  # m
Gamma_curr = 0.1  # s^-1 (conservative for current tech)

L_usl_curr = lambda_usl(m_curr, l_curr)
ratio_curr = L_usl_curr / Gamma_curr

print(f"\nCurrent-generation platform (Delic/Aspelmeyer class):")
print(f"  m = {m_curr:.2e} kg, l = {l_curr*1e9:.0f} nm")
print(f"  Lambda_USL = {L_usl_curr:.4e} s^-1")
print(f"  Gamma_env = {Gamma_curr:.2e} s^-1")
print(f"  Ratio = {ratio_curr:.4e}")

if ratio_curr > 1:
    print(f"  *** DETECTABLE ***")
elif ratio_curr > 0.01:
    print(f"  MARGINAL — {1/ratio_curr:.0f}x below threshold")
    print(f"  Requires 10x better environmental control OR 10x heavier particle")
else:
    print(f"  NOT detectable — {1/ratio_curr:.0f}x below threshold")
    print(f"  Requires {np.sqrt(1/ratio_curr):.0f}x heavier particle at same l and Gamma_env")

print(f"\n*** BOTTOM LINE ***")
print(f"The USL prediction Lambda = Gm^2/(hbar l) gives:")
print(f"  For m = 10^-18 kg, l = 10 nm: Lambda_USL = {lambda_usl(1e-18, 10e-9):.2e} s^-1")
print(f"  For m = 10^-17 kg, l = 10 nm: Lambda_USL = {lambda_usl(1e-17, 10e-9):.2e} s^-1")
print(f"  For m = 10^-16 kg, l = 10 nm: Lambda_USL = {lambda_usl(1e-16, 10e-9):.2e} s^-1")
print(f"")
print(f"Environmental noise floor: Gamma_env ~ 10^-3 to 10^-1 s^-1")
print(f"")
print(f"CROSSOVER MASS at l = 10 nm, Gamma_env = 10^-3 s^-1:")
m_cross = np.sqrt(1e-3 * hbar * 10e-9 / G)
print(f"  m_cross = {m_cross:.4e} kg = {m_cross/amu:.2e} amu")
print(f"  This is a {(m_cross / (4/3 * np.pi * (50e-9)**3 * 2200))**(1/3) * 100:.0f} nm silica particle")
print(f"  (roughly {m_cross/1e-17:.1f} × 10^-17 kg)")
print(f"")

# Effective particle size for crossover mass
rho_silica = 2200  # kg/m^3
R_cross = (3 * m_cross / (4 * np.pi * rho_silica))**(1/3)
print(f"  Crossover particle radius: {R_cross*1e9:.1f} nm")
print(f"  Crossover particle diameter: {2*R_cross*1e9:.0f} nm")
print(f"")
print(f"VERDICT: The USL becomes testable for particles of mass > {m_cross:.1e} kg")
print(f"         (diameter > {2*R_cross*1e9:.0f} nm silica)")
print(f"         superposed over > 10 nm separation")
print(f"         with environmental decoherence < 10^-3 s^-1")
print(f"")
print(f"This is EXACTLY the Blueprint-class experiment (arXiv 2512.02838).")
print(f"The current Delic/Aspelmeyer platform (m ~ 10^-18 kg) is {m_cross/1e-18:.0f}x too light.")
print(f"Scaling to m ~ 10^-17 kg (diameter ~{2*(3*1e-17/(4*np.pi*rho_silica))**(1/3)*1e9:.0f} nm)")
print(f"puts the USL at Lambda_USL = {lambda_usl(1e-17, 10e-9):.2e} s^-1,")
print(f"which is {lambda_usl(1e-17, 10e-9)/1e-3:.0f}x above the optimistic noise floor.")
