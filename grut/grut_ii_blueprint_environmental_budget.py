#!/usr/bin/env python3
"""
GRUT II Delta-Prime — Blueprint-Platform Environmental Budget and USL Testability Audit

Full environmental decoherence inventory for a concrete Blueprint-class
levitated nanoparticle platform, compared to the USL prediction.

Seven decoherence channels computed from published formulas:
1. Residual gas collisions (Hornberger-Sipe / Joos-Zeh)
2. Blackbody emission (thermal photon emission from hot particle)
3. Blackbody absorption (ambient thermal photon absorption)
4. Blackbody scattering (Rayleigh scattering of ambient thermal photons)
5. Trap-laser photon recoil (during any illuminated phase)
6. Electric/charge noise (patch potentials, residual charge)
7. Vibrational/seismic coupling

All formulas sourced from:
- Romero-Isart et al. (2011), arXiv:1110.4495
- Bateman et al. (2014), arXiv:1312.0500
- Blueprint paper (2025), arXiv:2512.02838
- Hornberger & Sipe (2003), quant-ph/0303094
- Chang et al. (2010)
"""

import numpy as np
from scipy.special import dawsn  # Dawson function for unified gas formula

# ============================================================
# FUNDAMENTAL CONSTANTS
# ============================================================
G       = 6.67430e-11    # m^3 kg^-1 s^-2  (Newton)
hbar    = 1.05457e-34    # J s
k_B     = 1.38065e-23    # J/K
c       = 2.99792e8      # m/s
amu     = 1.66054e-27    # kg
e_charge = 1.60218e-19   # C
epsilon_0 = 8.85419e-12  # F/m
sigma_SB = 5.67037e-8    # W m^-2 K^-4  (Stefan-Boltzmann)

# ============================================================
# PART I — REFERENCE PLATFORM SPECIFICATION
# ============================================================
print("=" * 80)
print("GRUT II Delta-Prime: Blueprint Environmental Budget")
print("=" * 80)

print("\n" + "=" * 80)
print("PART I — REFERENCE PLATFORM SPECIFICATION")
print("=" * 80)

# Material: amorphous silica (SiO2)
rho_silica = 2200.0      # kg/m^3
n_silica   = 1.45        # refractive index at optical frequencies
eps_opt    = n_silica**2  # = 2.1025 (optical dielectric constant)

# Clausius-Mossotti factor at optical frequencies
K_CM = (eps_opt - 1) / (eps_opt + 2)  # = 0.355

# Particle
R       = 75e-9          # m  (150 nm diameter — crossover from Gamma-Prime)
m       = rho_silica * (4/3) * np.pi * R**3  # kg
V_part  = (4/3) * np.pi * R**3  # m^3 (volume)

# Superposition parameters
l       = 10e-9          # m  (10 nm branch separation)
t_int   = 10.0           # s  (interrogation / free-fall time)

# Environmental conditions
T_env   = 4.0            # K  (cryogenic shield, liquid He)
T_int   = 20.0           # K  (internal particle temperature after laser release)
P_gas   = 1e-13          # Pa (10^-15 mbar — extreme UHV)

# Trapping
omega_trap = 2 * np.pi * 1e5  # rad/s (100 kHz trap frequency)
lambda_laser = 1550e-9   # m  (telecom laser for trapping)
omega_laser  = 2 * np.pi * c / lambda_laser
k_laser      = omega_laser / c
P_laser      = 5e-3      # W  (5 mW — low power for minimal recoil)

# Readout: Talbot-Lau interferometry or direct position measurement
# Release: laser switched off, particle in free fall

# Residual charge
n_charges = 1            # residual elementary charges (best case: neutralized)

# Vibrational isolation
S_vib = 1e-18            # m^2/Hz (seismic PSD at trap frequency — state of art)

print(f"\nMaterial: Amorphous silica (SiO2)")
print(f"  Density:     {rho_silica} kg/m^3")
print(f"  Refractive index (optical): {n_silica}")
print(f"  Clausius-Mossotti K:        {K_CM:.4f}")
print(f"\nParticle:")
print(f"  Radius:      R = {R*1e9:.1f} nm (diameter {2*R*1e9:.0f} nm)")
print(f"  Mass:        m = {m:.4e} kg = {m/amu:.2e} amu = {m*1e18:.3f} fg")
print(f"  Volume:      V = {V_part:.4e} m^3")
print(f"\nSuperposition:")
print(f"  Branch separation: l = {l*1e9:.0f} nm")
print(f"  Interrogation time: t = {t_int} s")
print(f"\nEnvironment:")
print(f"  Shield temperature:    T_env = {T_env} K")
print(f"  Internal temperature:  T_int = {T_int} K")
print(f"  Residual gas pressure: P = {P_gas:.0e} Pa = {P_gas*1e5:.0e} mbar")
print(f"\nTrapping:")
print(f"  Trap frequency: {omega_trap/(2*np.pi)/1e3:.0f} kHz")
print(f"  Laser: {lambda_laser*1e9:.0f} nm, {P_laser*1e3:.0f} mW")
print(f"\nCharge: {n_charges} elementary charges")
print(f"Vibrational PSD: S_vib = {S_vib:.0e} m^2/Hz")

# ============================================================
# PART II — FULL ENVIRONMENTAL DECOHERENCE INVENTORY
# ============================================================
print("\n" + "=" * 80)
print("PART II — FULL ENVIRONMENTAL DECOHERENCE INVENTORY")
print("=" * 80)

# All decoherence rates are computed as Lambda(l) in s^-1
# using the master framework: Lambda = D_pp * l^2 / hbar^2
# where D_pp is the momentum diffusion constant (kg^2 m^2 s^-3)

# ----------------------------------------------------------
# Channel 1: Residual gas collisions
# ----------------------------------------------------------
print("\n--- Channel 1: Residual Gas Collisions ---")

# Gas: N2 at temperature T_env
m_gas = 28 * amu  # kg (N2)

# Thermal de Broglie wavelength of gas molecule
lambda_dB_gas = hbar * np.sqrt(2 * np.pi / (m_gas * k_B * T_env))
# Mean thermal speed
v_th = np.sqrt(8 * k_B * T_env / (np.pi * m_gas))
# Number density
n_gas = P_gas / (k_B * T_env)
# Geometric cross section
sigma_geo = np.pi * R**2

# Momentum diffusion from gas collisions (Hornberger-Sipe):
# D_pp^gas = (8/3) * sqrt(2*pi) * P * R^2 * sqrt(m_gas * k_B * T)
# This is the standard result from Joos-Zeh in the long-wavelength limit
D_pp_gas = (8/3) * np.sqrt(2 * np.pi) * P_gas * R**2 * np.sqrt(m_gas * k_B * T_env)

# Spatial decoherence rate:
# In the long-wavelength limit (l << lambda_dB_gas):
# Lambda_gas = D_pp * l^2 / hbar^2
# In the short-wavelength limit (l >> lambda_dB_gas):
# Lambda_gas = scattering_rate (full decoherence per scatter)

# Unified formula using Dawson function (arXiv:2410.20910):
# Lambda(l) = Gamma_sc * [1 - exp(-q^2/2)]  where q = l / lambda_dB_gas
# But more precisely, for a sphere:
# Lambda(l) = n_gas * sigma_geo * v_th * F(l)
# where F(l) = 1 - sinc(l * k_typical) averaged over thermal distribution

# For the long-wavelength limit (l << thermal wavelength):
q_gas = l / lambda_dB_gas
Lambda_gas = D_pp_gas * l**2 / hbar**2

# Also compute full scattering rate for comparison
Gamma_scatter_gas = n_gas * sigma_geo * v_th

print(f"  Gas: N2, m_gas = {m_gas:.4e} kg")
print(f"  T_env = {T_env} K, P = {P_gas:.0e} Pa")
print(f"  Number density: n = {n_gas:.4e} m^-3")
print(f"  Thermal de Broglie (gas): lambda_dB = {lambda_dB_gas*1e12:.2f} pm")
print(f"  Mean thermal speed: v_th = {v_th:.2f} m/s")
print(f"  Geometric cross section: sigma = {sigma_geo:.4e} m^2")
print(f"  Gas scattering rate: Gamma_sc = {Gamma_scatter_gas:.4e} s^-1")
print(f"  D_pp^gas = {D_pp_gas:.4e} kg^2 m^2 s^-3")
print(f"  q = l/lambda_dB = {q_gas:.2f}")

if q_gas < 1:
    print(f"  Regime: LONG-WAVELENGTH (l < lambda_dB)")
    print(f"  Lambda_gas(l={l*1e9:.0f}nm) = D_pp * l^2 / hbar^2 = {Lambda_gas:.4e} s^-1")
else:
    print(f"  Regime: SHORT-WAVELENGTH (l > lambda_dB)")
    Lambda_gas = Gamma_scatter_gas  # full decoherence per scatter
    print(f"  Lambda_gas(l={l*1e9:.0f}nm) = Gamma_scatter = {Lambda_gas:.4e} s^-1")

print(f"  Formula: Hornberger-Sipe D_pp = (8/3)*sqrt(2pi)*P*R^2*sqrt(m_gas*kT)")
print(f"  Confidence: HIGH (standard, well-tested formula)")

# ----------------------------------------------------------
# Channel 2: Blackbody EMISSION from particle
# ----------------------------------------------------------
print("\n--- Channel 2: Blackbody Emission ---")

# The particle at T_int emits thermal photons.
# Each emitted photon carries momentum hbar*omega/c, providing which-path info.
#
# Momentum diffusion from emission (Bateman et al. 2014, Eq. 10):
# D_pp^emi = (8*pi^5/189) * V^2 * hbar / (pi^2 * c^5) *
#            integral[ omega^8 * Im{(eps(omega)-1)/(eps(omega)+2)} * n_BE(omega, T_int) * d_omega ]
#
# For constant epsilon approximation:
# D_pp^emi = (8*pi^5/189) * V^2 * Im{K_CM} * (k_B * T_int)^7 / (hbar^6 * c^5 * pi^2)
#            * [numerical integral factor]
#
# Simplified using the result from Bateman et al. (2014):
# Gamma_emi = (16*pi^3 / 189) * R^6 / c^5 * Im{(eps-1)/(eps+2)} *
#             integral_0^inf [ omega^6 * (n_BE + 1) * d_omega ]
#
# For silica, the dominant absorption is at ~10 um (Si-O stretch, omega ~ 2e14 rad/s)
# Im{epsilon} at 10 um for fused silica: ~ 1.0 (strong absorption band)
# Im{K_CM} at thermal frequencies for T_int = 20 K:
#   Peak Planck emission at T_int = 20 K: lambda_peak ~ 2898/20 = 145 um
#   At 145 um = 145e-6 m, omega = 2*pi*c/lambda = 1.3e13 rad/s
#   At this frequency, silica has Im{epsilon} ~ 0.05-0.1 (far-IR wing of phonon band)
#
# We use the parameterized result from the literature:
# For a silica nanosphere at T_int K:
# D_pp^emi ≈ C_emi * R^6 * T_int^7
# where C_emi ~ 10^-5 to 10^-4 (depends on dielectric model)
#
# More precise: use the leading Planck integral
# I_7 = integral_0^inf x^6 * n_BE(x) dx = pi^6/42 * Gamma(7) * zeta(7)
# Actually: integral_0^inf x^n / (e^x - 1) dx = Gamma(n+1) * zeta(n+1)
# For n=6: Gamma(7)*zeta(7) = 720 * 1.00835 = 726.01

# Use explicit formula from Romero-Isart (2011) for emission rate:
# N_emi = (4/3) * V * Im{K} * integral[ omega^3 / (pi^2 c^3) * n_BE(omega,T_int) * d_omega ]
# This is the total photon emission rate.
# Each photon carries momentum ~ hbar * omega_peak / c
# So D_pp^emi ~ N_emi * (hbar * omega_peak / c)^2

# Let's compute numerically
# Im{K_CM} for silica at thermal frequencies
# At T = 20 K, peak emission is at lambda ~ 145 um
# Silica Im{eps} at 145 um: approximately 0.05 (far-infrared, decreasing from phonon band)
Im_eps_thermal = 0.05  # conservative for T_int = 20 K regime
Im_K_thermal = Im_eps_thermal * 3 / abs(eps_opt + 2)**2  # Im{(eps-1)/(eps+2)} approximation
# More carefully: K = (eps-1)/(eps+2). If eps = eps_r + i*eps_i with eps_i << eps_r:
# Im{K} = 3*eps_i / |eps+2|^2 ≈ 3*eps_i / (eps_r+2)^2
Im_K_20K = 3 * Im_eps_thermal / (eps_opt + 2)**2

# Photon emission rate (Planck integral):
# N_emi = V * (2/(pi^2)) * Im_K * (k_B*T_int/hbar)^4 * integral[x^3/(e^x-1) dx] / c^3
# integral_0^inf x^3/(e^x-1) dx = pi^4/15
I3 = np.pi**4 / 15  # = 6.4939

omega_th_int = k_B * T_int / hbar  # thermal frequency at T_int
N_emi = V_part * (2 / np.pi**2) * Im_K_20K * omega_th_int**4 * I3 / c**3

# Mean photon energy
# <omega> = (k_B*T/hbar) * integral[x^4/(e^x-1)dx] / integral[x^3/(e^x-1)dx]
# = (k_B*T/hbar) * (24*zeta(5)) / (pi^4/15)
# integral x^4/(e^x-1) = 24*zeta(5) = 24*1.0369 = 24.886
I4 = 24 * 1.03693  # = 24.886
omega_mean_emi = omega_th_int * I4 / I3

# Momentum diffusion from emission:
# D_pp^emi = N_emi * (hbar * omega_mean_emi / c)^2 * (2/3)
# Factor 2/3 from angular averaging (isotropic emission)
D_pp_emi = N_emi * (2/3) * (hbar * omega_mean_emi / c)**2

# Decoherence rate
Lambda_emi = D_pp_emi * l**2 / hbar**2

print(f"  Particle internal temperature: T_int = {T_int} K")
print(f"  Peak emission wavelength: lambda_peak = {2898/T_int:.0f} um")
print(f"  Im{{epsilon}} at thermal freq: {Im_eps_thermal}")
print(f"  Im{{K_CM}} at thermal freq: {Im_K_20K:.4e}")
print(f"  Particle volume: V = {V_part:.4e} m^3")
print(f"  Thermal photon emission rate: N_emi = {N_emi:.4e} s^-1")
print(f"  Mean emitted photon frequency: omega = {omega_mean_emi:.4e} rad/s")
print(f"  Mean emitted photon wavelength: {2*np.pi*c/omega_mean_emi*1e6:.1f} um")
print(f"  D_pp^emi = {D_pp_emi:.4e} kg^2 m^2 s^-3")
print(f"  Lambda_emi(l={l*1e9:.0f}nm) = {Lambda_emi:.4e} s^-1")
print(f"  Formula: Romero-Isart (2011) Planck emission + momentum recoil")
print(f"  Confidence: MODERATE (depends on Im{{eps}} at far-IR, approximate)")

# ----------------------------------------------------------
# Channel 3: Blackbody ABSORPTION from environment
# ----------------------------------------------------------
print("\n--- Channel 3: Blackbody Absorption ---")

# Same formula as emission but with T_env instead of T_int
# And absorption FROM the environment (photon comes from thermal bath)

omega_th_env = k_B * T_env / hbar

# At T_env = 4 K, peak is at lambda ~ 725 um
# Silica Im{eps} at 725 um: very small, ~ 0.01 (deep far-IR)
Im_eps_abs = 0.01  # conservative for 725 um
Im_K_4K = 3 * Im_eps_abs / (eps_opt + 2)**2

N_abs = V_part * (2 / np.pi**2) * Im_K_4K * omega_th_env**4 * I3 / c**3
omega_mean_abs = omega_th_env * I4 / I3
D_pp_abs = N_abs * (2/3) * (hbar * omega_mean_abs / c)**2
Lambda_abs = D_pp_abs * l**2 / hbar**2

print(f"  Environmental temperature: T_env = {T_env} K")
print(f"  Peak absorption wavelength: {2898/T_env:.0f} um")
print(f"  Im{{epsilon}} at {2898/T_env:.0f} um: {Im_eps_abs}")
print(f"  Photon absorption rate: N_abs = {N_abs:.4e} s^-1")
print(f"  D_pp^abs = {D_pp_abs:.4e} kg^2 m^2 s^-3")
print(f"  Lambda_abs(l={l*1e9:.0f}nm) = {Lambda_abs:.4e} s^-1")
print(f"  Confidence: MODERATE (Im{{eps}} at deep far-IR poorly characterized)")

# ----------------------------------------------------------
# Channel 4: Blackbody Rayleigh SCATTERING
# ----------------------------------------------------------
print("\n--- Channel 4: Blackbody Rayleigh Scattering ---")

# Elastic scattering of environmental thermal photons
# sigma_sca(omega) = (128*pi^5/3) * R^6 * |K_CM|^2 / lambda^4
#                  = (8/3) * (omega/c)^4 * R^6 * |K_CM|^2 * pi
#
# Scattering rate:
# N_sca = integral[ n_photon(omega) * c * sigma_sca(omega) * d_omega ]
# where n_photon = (omega^2/(pi^2 c^3)) * n_BE(omega,T_env)

# This gives D_pp scaling as T^11 (very steep):
# D_pp^sca ~ R^6 * |K|^2 * (k_B T)^9 / (hbar^8 * c^7)

# Numerical computation:
# N_sca = V^2 * (128*pi^5/3) * |K_CM|^2 / (4*pi*R^6) * ...
# Actually, more directly:
# sigma_sca = (128*pi^5/3) * R^6 / lambda^4 * |K_CM|^2
#           = (8*pi/3) * k^4 * R^6 * |K_CM|^2

# Scattering rate = integral over Planck spectrum * sigma_sca * c
# = (8*pi/3) * R^6 * |K_CM|^2 * c * integral[ (omega/(2*pi*c))^4 * (omega^2/(pi^2*c^3)) * n_BE * d_omega/(2*pi) ]
# Simplifying:
# = (8*pi/3) * R^6 * |K_CM|^2 / (c^3 * (2*pi)^4) * integral[omega^6 * n_BE(omega,T) d_omega / (pi^2 c^3)]
# Hmm, let me be more careful.

# sigma_Rayleigh(omega) = (8*pi/3) * (omega/c)^4 * R^6 * |K_CM|^2
# Photon flux per unit frequency: dPhi/d_omega = c * u(omega) = c * (hbar*omega^3)/(pi^2*c^3) * n_BE(omega,T)
# Scattering rate: N_sca = integral sigma(omega) * dPhi/d_omega d_omega
# = (8*pi/3) * R^6 * |K_CM|^2 * integral[ (omega/c)^4 * hbar*omega^3 / (pi^2*c^2) * n_BE * d_omega ]
# = (8*pi/3) * R^6 * |K_CM|^2 * hbar / (pi^2 * c^6) * integral[ omega^7 * n_BE d_omega ]

# integral omega^7 * n_BE d_omega = (k_B*T/hbar)^8 * Gamma(8)*zeta(8)
# Gamma(8) = 5040, zeta(8) = pi^8/9450 = 1.00408
I7_zeta8 = 5040 * 1.00408  # = 5060.56

N_sca = (8 * np.pi / 3) * R**6 * K_CM**2 * hbar / (np.pi**2 * c**6) * \
        (k_B * T_env / hbar)**8 * I7_zeta8

# Momentum per scattered photon: hbar * omega_mean / c
# Mean frequency for scattering is weighted by omega^7 * n_BE:
# <omega>_sca = integral[omega^8 n_BE] / integral[omega^7 n_BE]
# = (kT/hbar) * Gamma(9)*zeta(9) / (Gamma(8)*zeta(8))
# Gamma(9) = 40320, zeta(9) = 1.00200
I8_zeta9 = 40320 * 1.00200
omega_mean_sca = (k_B * T_env / hbar) * I8_zeta9 / I7_zeta8

D_pp_sca = N_sca * (2/3) * (hbar * omega_mean_sca / c)**2
Lambda_sca = D_pp_sca * l**2 / hbar**2

print(f"  |K_CM|^2 = {K_CM**2:.4f}")
print(f"  Rayleigh scattering rate: N_sca = {N_sca:.4e} s^-1")
print(f"  Mean scattered photon wavelength: {2*np.pi*c/omega_mean_sca*1e6:.1f} um")
print(f"  D_pp^sca = {D_pp_sca:.4e} kg^2 m^2 s^-3")
print(f"  Lambda_sca(l={l*1e9:.0f}nm) = {Lambda_sca:.4e} s^-1")
print(f"  Confidence: HIGH (well-understood Rayleigh regime, R << lambda)")

# ----------------------------------------------------------
# Channel 5: Trap-laser photon recoil
# ----------------------------------------------------------
print("\n--- Channel 5: Trap-Laser Photon Recoil ---")

# During trapping phase ONLY (before release into free fall)
# After release, no laser → zero contribution during free evolution
# But: any brief illumination for readout contributes

# Rayleigh scattering cross section at 1550 nm
sigma_Rayleigh_trap = (128 * np.pi**5 / 3) * R**6 / lambda_laser**4 * K_CM**2

# Laser intensity at focus
# Assuming Gaussian beam focused to w0 ~ lambda/pi ~ 500 nm
w0 = lambda_laser / np.pi  # beam waist
A_beam = np.pi * w0**2
I_laser = P_laser / A_beam

# Photon scattering rate during illumination
Gamma_sc_laser = sigma_Rayleigh_trap * I_laser / (hbar * omega_laser)

# D_pp from laser scattering
D_pp_laser = (2/3) * Gamma_sc_laser * (hbar * k_laser)**2

# If laser is on for trapping ONLY and off during free evolution:
# The decoherence during free evolution is ZERO from this channel
# But any readout pulse contributes.
# Assume: readout pulse duration t_read = 1 ms at same power
t_read = 1e-3  # s

# Decoherence accumulated during readout:
Lambda_laser_during_readout = D_pp_laser * l**2 / hbar**2
# Total phase accumulated = Lambda * t_read (not Lambda * t_int)
# But we want an effective rate over the full interrogation:
Lambda_laser_eff = Lambda_laser_during_readout * t_read / t_int

print(f"  Laser: {lambda_laser*1e9:.0f} nm, {P_laser*1e3:.0f} mW")
print(f"  Rayleigh cross section: sigma = {sigma_Rayleigh_trap:.4e} m^2")
print(f"  Beam waist: w0 = {w0*1e9:.0f} nm")
print(f"  Peak intensity: I = {I_laser:.4e} W/m^2")
print(f"  Photon scattering rate (during illumination): Gamma_sc = {Gamma_sc_laser:.4e} s^-1")
print(f"  D_pp^laser = {D_pp_laser:.4e} kg^2 m^2 s^-3")
print(f"  Lambda during illumination = {Lambda_laser_during_readout:.4e} s^-1")
print(f"  Readout pulse: {t_read*1e3:.0f} ms")
print(f"  Effective Lambda over {t_int}s = {Lambda_laser_eff:.4e} s^-1")
print(f"  NOTE: ZERO during free evolution (laser off)")
print(f"  Confidence: HIGH (Rayleigh scattering is exact for R << lambda)")

# Alternative: NO readout illumination (dark free-fall interferometry)
Lambda_laser_dark = 0.0
print(f"  If fully dark protocol: Lambda_laser = 0 (no laser during coherence)")

# ----------------------------------------------------------
# Channel 6: Electric / charge noise
# ----------------------------------------------------------
print("\n--- Channel 6: Electric / Charge Noise ---")

# Residual charge on particle: n_charges * e
q = n_charges * e_charge

# Electric field noise spectral density
# From patch potentials on surrounding electrodes:
# S_E ~ V_patch^2 / (d^4 * f)  where V_patch ~ 10 mV, d ~ 100 um
# For well-shielded cryogenic environment:
# S_E(100 kHz) ~ 10^-12 (V/m)^2/Hz  (achievable in cryogenic systems)
S_E = 1e-12  # (V/m)^2/Hz — conservative for cryogenic shielded environment

# At trap frequency:
# D_pp^charge = q^2 * S_E
# But this is the force noise PSD, so:
# D_pp^charge = q^2 * S_E  [units: C^2 * (V/m)^2/Hz = N^2/Hz = kg^2 m^2 s^-4 / Hz]
# Wait: S_E has units (V/m)^2/Hz. F = qE, so S_F = q^2 S_E [(C*V/m)^2/Hz = N^2/Hz]
# D_pp = integral S_F d_omega ~ S_F * bandwidth
# For decoherence: D_pp = q^2 * S_E * Delta_omega
# Effective bandwidth: the particle's motion bandwidth ~ 1/t_int
Delta_omega_charge = 1.0 / t_int  # Hz

D_pp_charge = q**2 * S_E  # This is actually the one-sided PSD of momentum kicks
# The position decoherence rate is:
# Lambda_charge = D_pp_charge * l^2 / hbar^2
# But we need to be careful: D_pp here is per unit time (spectral density integrated)
# More precisely: for white noise S_F over bandwidth Df,
# <Delta p^2> = S_F * t_int (accumulated over interrogation time)
# Decoherence: exp(-<Delta p^2> * l^2 / (2 hbar^2))
# Rate: Lambda = S_F * l^2 / (2 * hbar^2) [note: this is for two-sided PSD]
# For one-sided: Lambda = q^2 * S_E * l^2 / hbar^2

Lambda_charge = q**2 * S_E * l**2 / hbar**2

print(f"  Residual charge: {n_charges}e = {q:.4e} C")
print(f"  Electric field noise PSD: S_E = {S_E:.0e} (V/m)^2/Hz")
print(f"  D_pp^charge = q^2 * S_E = {q**2 * S_E:.4e} N^2 s")
print(f"  Lambda_charge = {Lambda_charge:.4e} s^-1")
print(f"  NOTE: Assumes particle is charge-neutralized to {n_charges}e")
print(f"  If charge = 0: Lambda_charge = 0")
print(f"  Confidence: LOW-MODERATE (S_E depends strongly on electrode geometry & shielding)")

# For n_charges = 0 (neutralized):
Lambda_charge_neutral = 0.0
print(f"  Best case (neutralized): Lambda_charge = 0")

# ----------------------------------------------------------
# Channel 7: Vibrational / seismic coupling
# ----------------------------------------------------------
print("\n--- Channel 7: Vibrational / Seismic Coupling ---")

# Vibrations of the experimental platform couple to the particle's CoM
# Through the trapping potential (while trapped) or through gravity gradients (free fall)
#
# While trapped: D_pp^vib = m^2 * omega_trap^4 * S_x(omega_trap)
# While in free fall: coupling is through gravity gradients only
# D_pp^vib_freefall = m^2 * omega_grav_grad^2 * S_x(0)
# where omega_grav_grad ~ sqrt(G*rho_earth) ~ 10^-3 s^-1 (negligible)

# During free evolution (laser off, free fall):
# The dominant coupling is through the gravity gradient of nearby masses
# omega_grav ~ sqrt(G * M_apparatus / d^3) where M_apparatus ~ 1 kg, d ~ 0.1 m
M_app = 1.0  # kg
d_app = 0.1  # m
omega_grav_grad = np.sqrt(G * M_app / d_app**3)

# Vibrational noise of apparatus at low frequency:
# Cryostat vibrations at ~Hz: S_x ~ 10^-18 m^2/Hz (state of art)
S_x_low = 1e-18  # m^2/Hz

D_pp_vib_freefall = m**2 * omega_grav_grad**4 * S_x_low
Lambda_vib = D_pp_vib_freefall * l**2 / hbar**2

print(f"  During free fall, coupling via gravity gradient only:")
print(f"  Gravity gradient frequency: omega_gg = {omega_grav_grad:.4e} rad/s")
print(f"  Apparatus vibration PSD: S_x = {S_x_low:.0e} m^2/Hz")
print(f"  D_pp^vib = {D_pp_vib_freefall:.4e} kg^2 m^2 s^-3")
print(f"  Lambda_vib = {Lambda_vib:.4e} s^-1")
print(f"  Confidence: HIGH (gravity gradient coupling is fundamental, vibration PSD is measured)")

# ============================================================
# PART III — TOTAL BUDGET vs USL
# ============================================================
print("\n" + "=" * 80)
print("PART III — TOTAL BUDGET vs USL")
print("=" * 80)

# USL prediction
Lambda_USL = G * m**2 / (hbar * l)

# Collect all channels
channels = {
    "Gas collisions":        Lambda_gas,
    "BB emission":           Lambda_emi,
    "BB absorption":         Lambda_abs,
    "BB Rayleigh scattering":Lambda_sca,
    "Laser recoil (readout)":Lambda_laser_eff,
    "Charge noise (1e)":     Lambda_charge,
    "Vibrational":           Lambda_vib,
}

# Conservative budget (includes charge, readout laser)
Lambda_env_total = sum(channels.values())

# Optimistic budget (neutralized, dark protocol)
channels_optimistic = dict(channels)
channels_optimistic["Laser recoil (readout)"] = Lambda_laser_dark
channels_optimistic["Charge noise (1e)"] = Lambda_charge_neutral
Lambda_env_optimistic = sum(channels_optimistic.values())

print(f"\nParticle: m = {m:.4e} kg ({m*1e18:.3f} fg), R = {R*1e9:.0f} nm")
print(f"Separation: l = {l*1e9:.0f} nm")
print(f"\n*** USL PREDICTION ***")
print(f"  Lambda_USL = G m^2 / (hbar l) = {Lambda_USL:.4e} s^-1")
print(f"  tau_USL = {1/Lambda_USL:.4e} s")

print(f"\n--- Environmental Decoherence Budget ---")
print(f"  {'Channel':<30s} {'Rate (s^-1)':>15s} {'Fraction':>15s} {'Confidence':>15s}")
print(f"  {'-'*30} {'-'*15} {'-'*15} {'-'*15}")

for name, rate in sorted(channels.items(), key=lambda x: -x[1]):
    frac = rate / Lambda_env_total if Lambda_env_total > 0 else 0
    confidence = {
        "Gas collisions": "HIGH",
        "BB emission": "MODERATE",
        "BB absorption": "MODERATE",
        "BB Rayleigh scattering": "HIGH",
        "Laser recoil (readout)": "HIGH",
        "Charge noise (1e)": "LOW",
        "Vibrational": "HIGH",
    }.get(name, "?")
    print(f"  {name:<30s} {rate:>15.4e} {frac:>15.2%} {confidence:>15s}")

print(f"  {'─'*75}")
print(f"  {'TOTAL (conservative)':<30s} {Lambda_env_total:>15.4e}")
print(f"  {'TOTAL (optimistic)':<30s} {Lambda_env_optimistic:>15.4e}")

print(f"\n*** COMPARISON ***")
print(f"  Lambda_USL / Lambda_env (conservative) = {Lambda_USL / Lambda_env_total:.4f}")
print(f"  Lambda_USL / Lambda_env (optimistic)   = {Lambda_USL / Lambda_env_optimistic:.4f}")

if Lambda_USL > 10 * Lambda_env_total:
    classification = "USL-DOMINATED"
elif Lambda_USL > Lambda_env_total:
    classification = "USL-COMPARABLE (USL > env)"
elif Lambda_USL > 0.1 * Lambda_env_total:
    classification = "ENVIRONMENT-DOMINATED BUT CLOSE"
elif Lambda_USL > 0.01 * Lambda_env_total:
    classification = "ENVIRONMENT-DOMINATED (within 2 orders)"
else:
    classification = "ENVIRONMENT-DOMINATED BY ORDERS OF MAGNITUDE"

print(f"\n  Classification: {classification}")

# ============================================================
# PART IV — VISIBILITY AND RUN-COUNT FORECAST
# ============================================================
print("\n" + "=" * 80)
print("PART IV — VISIBILITY AND RUN-COUNT FORECAST")
print("=" * 80)

# Total decoherence with and without USL
Gamma_with_USL = Lambda_env_total + Lambda_USL
Gamma_without_USL = Lambda_env_total

# Coherence times
tau_with = 1 / Gamma_with_USL
tau_without = 1 / Gamma_without_USL

# Visibility after interrogation time t_int
V_with = np.exp(-Gamma_with_USL * t_int)
V_without = np.exp(-Gamma_without_USL * t_int)
Delta_V = V_without - V_with

# For optimistic budget
Gamma_with_USL_opt = Lambda_env_optimistic + Lambda_USL
Gamma_without_USL_opt = Lambda_env_optimistic

tau_with_opt = 1 / Gamma_with_USL_opt
tau_without_opt = 1 / Gamma_without_USL_opt

V_with_opt = np.exp(-Gamma_with_USL_opt * t_int)
V_without_opt = np.exp(-Gamma_without_USL_opt * t_int)
Delta_V_opt = V_without_opt - V_with_opt

print(f"\n--- Conservative Budget ---")
print(f"  Gamma_env = {Gamma_without_USL:.4e} s^-1")
print(f"  Gamma_env + USL = {Gamma_with_USL:.4e} s^-1")
print(f"  tau_coh (env only): {tau_without:.2f} s")
print(f"  tau_coh (env + USL): {tau_with:.2f} s")
print(f"  Ratio: {tau_without/tau_with:.4f}")
print(f"  Visibility at t = {t_int} s:")
print(f"    Without USL: {V_without:.6f}")
print(f"    With USL:    {V_with:.6f}")
print(f"    Difference:  {Delta_V:.6f} ({Delta_V/V_without*100:.4f}%)")

print(f"\n--- Optimistic Budget ---")
print(f"  Gamma_env = {Gamma_without_USL_opt:.4e} s^-1")
print(f"  Gamma_env + USL = {Gamma_with_USL_opt:.4e} s^-1")
print(f"  tau_coh (env only): {tau_without_opt:.2f} s")
print(f"  tau_coh (env + USL): {tau_with_opt:.2f} s")
print(f"  Ratio: {tau_without_opt/tau_with_opt:.4f}")
print(f"  Visibility at t = {t_int} s:")
print(f"    Without USL: {V_without_opt:.6f}")
print(f"    With USL:    {V_with_opt:.6f}")
print(f"    Difference:  {Delta_V_opt:.6f} ({Delta_V_opt/V_without_opt*100:.4f}%)")

# Run-count estimate for 3-sigma detection
# Signal: Delta_V (visibility difference)
# Noise per run: shot noise ~ 1/sqrt(N_photons)
# For visibility measurement, uncertainty ~ 1/sqrt(N_runs)
# Need: Delta_V / sigma_V > 3 for 3-sigma
# sigma_V = V / sqrt(N_runs) (assuming Poisson statistics)
# N_runs = (3 * V / Delta_V)^2

print(f"\n--- Run Count for 3-sigma Detection ---")
for label, dv, v_ref in [("Conservative", Delta_V, V_without),
                           ("Optimistic", Delta_V_opt, V_without_opt)]:
    if dv > 0:
        # Assume visibility can be measured with fractional precision 1/sqrt(N)
        N_runs_3sigma = (3 * v_ref / dv)**2
        # More realistic: include readout noise. Assume SNR per run = 10
        snr_per_run = 10
        N_runs_realistic = (3 / (dv / v_ref * snr_per_run))**2
        print(f"  {label}:")
        print(f"    Signal: Delta_V/V = {dv/v_ref:.4e}")
        print(f"    Ideal (shot-noise-limited): N_runs > {N_runs_3sigma:.0f}")
        print(f"    Realistic (SNR/run = {snr_per_run}): N_runs > {N_runs_realistic:.0f}")
    else:
        print(f"  {label}: Signal too small to detect")

# Also: effect on coherence time measurement
print(f"\n--- Coherence Time Discrimination ---")
for label, tw, two in [("Conservative", tau_with, tau_without),
                        ("Optimistic", tau_with_opt, tau_without_opt)]:
    reduction = (two - tw) / two
    print(f"  {label}:")
    print(f"    tau without USL: {two:.2f} s")
    print(f"    tau with USL:    {tw:.2f} s")
    print(f"    Reduction:       {reduction*100:.2f}%")
    print(f"    Need precision:  ~{reduction*100/3:.1f}% on tau measurement for 3-sigma")

# ============================================================
# PART V — SENSITIVITY BOTTLENECK ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("PART V — SENSITIVITY BOTTLENECK ANALYSIS")
print("=" * 80)

sorted_channels = sorted(channels.items(), key=lambda x: -x[1])

print(f"\nRanked environmental channels (conservative):")
for i, (name, rate) in enumerate(sorted_channels):
    bar = "=" * max(1, int(50 * rate / sorted_channels[0][1]))
    print(f"  {i+1}. {name:<30s} {rate:.4e} s^-1  {bar}")

print(f"\n  WORST BOTTLENECK:  {sorted_channels[0][0]} ({sorted_channels[0][1]:.2e} s^-1)")
print(f"  SECOND WORST:      {sorted_channels[1][0]} ({sorted_channels[1][1]:.2e} s^-1)")

# Which improvements matter most?
print(f"\n--- Impact of Improvements ---")

# Remove each channel and see new total
for name, rate in sorted_channels:
    new_total = Lambda_env_total - rate
    new_ratio = Lambda_USL / new_total if new_total > 0 else float('inf')
    print(f"  Without '{name}': Lambda_env = {new_total:.4e}, USL/env = {new_ratio:.4f}")

# What pressure is needed to make gas subdominant?
Lambda_target_gas = Lambda_USL / 10  # gas should be < 10% of USL
# Lambda_gas ~ D_pp * l^2 / hbar^2 ~ P * R^2 * sqrt(m_gas * kT) * l^2 / hbar^2
# So P_needed ~ Lambda_target_gas * hbar^2 / (R^2 * sqrt(m_gas*kT) * l^2 * C)
# where C = (8/3) * sqrt(2*pi)
C_gas = (8/3) * np.sqrt(2 * np.pi)
P_needed_gas = Lambda_target_gas * hbar**2 / (C_gas * R**2 * np.sqrt(m_gas * k_B * T_env) * l**2)

print(f"\n--- Required Conditions ---")
print(f"  For gas < 10% of USL: P < {P_needed_gas:.2e} Pa = {P_needed_gas*1e5:.2e} mbar")
print(f"  Current target: P = {P_gas:.0e} Pa")
print(f"  Status: {'ACHIEVED' if P_gas < P_needed_gas else 'NOT MET — need ' + f'{P_needed_gas/P_gas:.0f}x lower pressure'}")

# What T_int is needed to make emission subdominant?
# Lambda_emi scales roughly as T_int^7 (crude)
# We need Lambda_emi < Lambda_USL / 10
if Lambda_emi > 0:
    T_int_needed = T_int * (Lambda_USL / (10 * Lambda_emi))**(1/7)
    print(f"  For BB emission < 10% of USL: T_int < {T_int_needed:.1f} K")
    print(f"  Current target: T_int = {T_int} K")
    print(f"  Status: {'ACHIEVED' if T_int < T_int_needed else 'NOT MET'}")

# ============================================================
# PART VI — VIABILITY LADDER
# ============================================================
print("\n" + "=" * 80)
print("PART VI — VIABILITY LADDER")
print("=" * 80)

# Assess each requirement
requirements = [
    ("Particle mass 4+ fg (150 nm silica)", "ALREADY ACHIEVABLE",
     "Commercial silica nanospheres available up to micron scale"),
    ("Optical trapping & ground-state cooling", "ALREADY ACHIEVABLE",
     "Demonstrated by Delic 2020, Rossi 2024"),
    ("Charge neutralization to 0-1e", "PLAUSIBLE WITH NEAR-TERM IMPROVEMENT",
     "Demonstrated for levitated particles, reliability improving"),
    ("Cryogenic environment T_env < 5 K", "ALREADY ACHIEVABLE",
     "Standard dilution refrigerator technology"),
    ("Internal temperature T_int < 20 K", "PLAUSIBLE WITH NEAR-TERM IMPROVEMENT",
     "Requires radiative cooling after trap release, ~seconds timescale"),
    ("Pressure P < 10^-13 Pa (10^-15 mbar)", "REQUIRES MAJOR TECHNICAL ADVANCE",
     "Current best: ~10^-10 Pa in room-temp UHV. Cryogenic helps via cryopumping. 10^-15 mbar is extreme."),
    ("Spatial superposition l ~ 10 nm", "REQUIRES MAJOR TECHNICAL ADVANCE",
     "Current record: 73 pm. Need 100x improvement. No demonstrated protocol at nanoparticle scale."),
    ("10+ second free evolution", "REQUIRES MAJOR TECHNICAL ADVANCE",
     "Requires microgravity (drop tower, space) OR magnetic levitation with sub-nm stability"),
    ("Readout with single-run visibility", "REQUIRES MAJOR TECHNICAL ADVANCE",
     "Talbot-Lau or direct position sensing at nm resolution after seconds of free fall"),
    ("Combined: all above simultaneously", "SPECULATIVE WITH CURRENT ARCHITECTURE",
     "No experiment has demonstrated more than 2 of the above requirements simultaneously"),
]

print(f"\n{'Requirement':<50s} {'Status':<45s}")
print(f"{'-'*50} {'-'*45}")
for req, status, note in requirements:
    print(f"  {req:<48s} {status}")
    print(f"  {'':48s} ({note})")
    print()

# Count by category
from collections import Counter
status_counts = Counter(s for _, s, _ in requirements)
print(f"\nSummary:")
for status, count in status_counts.most_common():
    print(f"  {status}: {count}")

# ============================================================
# PART VII — FINAL VERDICT
# ============================================================
print("\n" + "=" * 80)
print("PART VII — FINAL VERDICT")
print("=" * 80)

print(f"\n*** QUANTITATIVE SUMMARY ***")
print(f"")
print(f"  Reference platform:")
print(f"    150 nm silica, m = {m:.2e} kg ({m*1e18:.1f} fg)")
print(f"    l = {l*1e9:.0f} nm, t_int = {t_int:.0f} s")
print(f"    T_env = {T_env} K, T_int = {T_int} K, P = {P_gas:.0e} Pa")
print(f"")
print(f"  USL prediction:")
print(f"    Lambda_USL = {Lambda_USL:.4e} s^-1")
print(f"")
print(f"  Environmental budget:")
print(f"    Conservative: {Lambda_env_total:.4e} s^-1")
print(f"    Optimistic:   {Lambda_env_optimistic:.4e} s^-1")
print(f"")
print(f"  Ratio USL/env:")
print(f"    Conservative: {Lambda_USL/Lambda_env_total:.4f}")
print(f"    Optimistic:   {Lambda_USL/Lambda_env_optimistic:.4f}")
print(f"")
print(f"  Signal (optimistic):")
print(f"    Coherence reduction: {(tau_without_opt - tau_with_opt)/tau_without_opt*100:.1f}%")
print(f"    Visibility contrast: {Delta_V_opt:.4e} over {t_int} s")

# Determine verdict
if Lambda_USL / Lambda_env_optimistic > 1.0:
    if Lambda_USL / Lambda_env_total > 1.0:
        verdict = "blueprint_window_survives_full_budget"
        detail = "USL exceeds environmental noise even with conservative assumptions."
    else:
        verdict = "usl_test_window_narrows_but_survives"
        detail = "USL exceeds optimistic environmental budget. Conservative budget is marginal."
elif Lambda_USL / Lambda_env_optimistic > 0.1:
    verdict = "usl_test_window_narrows_but_survives"
    detail = "USL is within one order of magnitude of the optimistic environmental budget."
elif Lambda_USL / Lambda_env_total > 0.01:
    verdict = "environmental_budget_kills_current_blueprint_target"
    detail = "USL is 1-2 orders below the environmental budget."
else:
    verdict = "usl_testability_requires_specific_breakthrough"
    detail = "USL is orders of magnitude below environmental noise at these parameters."

print(f"\n*** VERDICT: {verdict} ***")
print(f"  {detail}")

# Check if scaling up mass helps
print(f"\n--- Mass scaling check ---")
for m_test_fg in [4, 10, 50, 100]:
    m_test = m_test_fg * 1e-18
    R_test = (3 * m_test / (4 * np.pi * rho_silica))**(1/3)
    L_usl_test = G * m_test**2 / (hbar * l)

    # Gas scales as R^2 ~ m^(2/3)
    L_gas_test = Lambda_gas * (R_test / R)**2
    # BB emission scales as R^6 * ... ~ V^2 ~ m^2 (approximately)
    L_emi_test = Lambda_emi * (m_test / m)**2
    # BB absorption same
    L_abs_test = Lambda_abs * (m_test / m)**2
    # BB scattering scales as R^6
    L_sca_test = Lambda_sca * (R_test / R)**6
    # Charge same (doesn't scale with mass)
    L_charge_test = Lambda_charge
    # Vib scales as m^2
    L_vib_test = Lambda_vib * (m_test / m)**2

    L_env_test = L_gas_test + L_emi_test + L_abs_test + L_sca_test + L_charge_test + L_vib_test
    ratio_test = L_usl_test / L_env_test

    print(f"  m = {m_test_fg} fg (R = {R_test*1e9:.0f} nm):")
    print(f"    Lambda_USL = {L_usl_test:.4e}, Lambda_env = {L_env_test:.4e}, ratio = {ratio_test:.4f}")
    print(f"    Dominant env: gas={L_gas_test:.2e}, emi={L_emi_test:.2e}, sca={L_sca_test:.2e}")

print(f"\n" + "=" * 80)
print(f"END OF COMPUTATION")
print(f"=" * 80)
