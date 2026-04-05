"""
GRUT-II Zeta — LIGO O3/O4a Confrontation
==========================================

Converts the GRUT-II near-horizon prediction into Omega_GW(f) and
confronts it against the published LIGO-Virgo-KAGRA stochastic limits.

Published limits (O4a, 95% CL, log-uniform prior):
  alpha = 0: Omega_ref < 2.8e-9 at 25 Hz
  alpha = 2/3: Omega_ref < 2.0e-9 at 25 Hz
  alpha = 3: Omega_ref < 3.2e-10 at 25 Hz

GRUT-II prediction (single 10 M_sun BH at 10 kpc):
  h_TT ~ 4.8e-17 * (D/D_max) at f ~ 254 Hz

Must convert single-source strain to Omega_GW for a population.
"""

import math

# Constants
G = 6.674e-11
C = 2.998e8
M_SUN = 1.989e30
H_0 = 2.18e-18  # Hubble constant: 67.4 km/s/Mpc in s^-1
RHO_CRIT = 3 * H_0**2 / (8 * math.pi * G)  # critical density

# LIGO published limits (O4a, 95% CL)
OMEGA_LIMIT_FLAT = 2.8e-9      # alpha = 0
OMEGA_LIMIT_CBC = 2.0e-9       # alpha = 2/3 at 25 Hz
OMEGA_LIMIT_ALPHA3 = 3.2e-10   # alpha = 3 at 25 Hz


def single_source_to_omega(h_rms, f_signal, tau_signal, R_source):
    """Convert single-source RMS strain to Omega_GW contribution.

    For a single source at distance R:
    S_h(f) = h_rms^2 * tau_signal  (strain PSD at signal frequency)

    Omega_GW(f) = (2 * pi^2 / (3 * H_0^2)) * f^3 * S_h(f)

    But this is for ONE source. For a population, we need to sum
    over all sources in the observable universe.
    """
    S_h = h_rms**2 * tau_signal  # strain^2 / Hz
    Omega = (2 * math.pi**2 / (3 * H_0**2)) * f_signal**3 * S_h
    return S_h, Omega


def population_omega(h_rms_single, f_signal, tau_signal, R_single, n_density, R_max):
    """Estimate Omega_GW from a population of sources.

    For sources uniformly distributed with number density n [Mpc^-3]:
    N(< R) = (4/3) pi R^3 n
    Each source at distance R contributes h ~ h_single * (R_single / R)
    S_h_total = integral n * h^2(R) * tau * 4*pi*R^2 dR / (4*pi*R^2)
              ... this needs care.

    Standard result for isotropic stochastic background:
    Omega_GW(f) = (f / rho_crit) * integral dz (R_m(z) / (1+z)) * (dE_GW/df_s) / H(z)

    For a simpler estimate: if there are N_eff sources contributing
    within the LIGO horizon at this frequency, and each contributes
    S_h_single at distance R_single:

    S_h_total ~ N_eff * S_h_single * (R_single / R_eff)^2

    where R_eff is the effective distance for the population.

    Let's use the simple estimate.
    """
    # Number of stellar-mass BHs in the observable universe
    # Estimate: ~10^8 stellar-mass BHs per galaxy, ~10^11 galaxies
    # Total: ~10^19 stellar-mass BHs
    # Within 10 Mpc: ~10^4 galaxies, ~10^12 BHs
    # Within the Hubble volume: ~10^19 BHs

    # Each BH contributes h ~ h_single * (R_single / R)
    # S_h ~ h^2 * tau = h_single^2 * (R_single/R)^2 * tau

    # Integral over shell [R, R+dR]:
    # dS_h = n * 4*pi*R^2 * h_single^2 * (R_single/R)^2 * tau * dR
    #       = 4*pi * n * h_single^2 * R_single^2 * tau * dR
    # This is INDEPENDENT of R! Each shell contributes equally.
    # Total: S_h_total = 4*pi * n * h_single^2 * R_single^2 * tau * R_max

    S_h_total = 4 * math.pi * n_density * h_rms_single**2 * R_single**2 * tau_signal * R_max
    Omega = (2 * math.pi**2 / (3 * H_0**2)) * f_signal**3 * S_h_total
    return S_h_total, Omega


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT-II ZETA — LIGO O3/O4a CONFRONTATION")
    print("=" * 80)

    # ================================================================
    # PART I: Level-1 stochastic consistency
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART I: LEVEL-1 STOCHASTIC CONSISTENCY")
    print("=" * 80)
    print("""
  The Level-1 rule: 1/tau_local = 1/tau_0 + 1/t_dyn

  Original derivation (Appendix G): motivated by parallel-rate competition
  between global (tau_0) and local (t_dyn) relaxation channels.
  Classification: structurally_motivated_heuristic_not_derived.

  Assumptions that depended on LINEAR DETERMINISTIC relaxation:
  1. The rate 1/tau is a DISSIPATION rate (not stochastic)
  2. The parallel-rate competition assumes each channel operates independently
  3. No noise-induced modification of the effective tau was considered

  In the stochastic regime (sigma/X not tiny):
  - The dissipation rate 1/tau_local is still the DAMPING rate in the Langevin equation
  - The Langevin equation tau dPhi/dt + Phi = X + xi is EXACTLY solvable for ANY tau
  - The Level-1 rule determines tau; the noise D enters independently
  - tau_local itself does NOT fluctuate (it is a PARAMETER, not a dynamical variable)

  HOWEVER: if sigma/X ~ O(1), the background on which tau_local was computed
  (the equilibrium Schwarzschild + constitutive energy) is significantly perturbed.
  The Level-1 rule was derived on the DETERMINISTIC background.
  Self-consistency requires: the fluctuation-modified background has approximately
  the same t_dyn as the unperturbed background.

  For sigma/X < 0.1 (D < 0.01 D_max at ISCO): the background perturbation is < 1%.
  Level-1 is safe. For sigma/X ~ 0.3 (D ~ 0.1 D_max): perturbation is ~10%.
  Level-1 is marginal. For sigma/X > 0.5: Level-1 needs stochastic correction.

  VERDICT: Level-1 marginal but usable perturbatively for D < 0.1 D_max.
""")

    # ================================================================
    # PART II-III: Signal chain and far-field transfer
    # ================================================================
    print("=" * 80)
    print("  PART II-III: SIGNAL CHAIN AND FAR-FIELD TRANSFER AUDIT")
    print("=" * 80)

    M = 10 * M_SUN
    rs = 2 * G * M / C**2
    r_isco = 3 * rs  # Schwarzschild ISCO = 6M = 3 r_s

    tau_local_s = math.sqrt(r_isco**3 / (2 * G * M))
    tau_geom = tau_local_s * C / rs

    # Constitutive parameters
    tau_can = math.sqrt(1.5)
    D_geom_max = 0.01 * tau_can

    # The signal chain has a CRITICAL issue I must audit:
    # The Epsilon calculation used delta_m / R for the strain.
    # But delta_m was computed as delta_rho * V_corr where V_corr ~ l_corr^3.
    # This gives a MASS PERTURBATION at the source.
    # The GW strain from a fluctuating mass monopole is... ZERO.
    # Monopole radiation is forbidden by mass conservation.
    # Only QUADRUPOLE and higher radiate.

    print("""
  CRITICAL AUDIT: MONOPOLE vs QUADRUPOLE RADIATION

  The Epsilon calculation computed delta_m (mass perturbation) and used
  h ~ delta_m / R. This is the Newtonian potential perturbation, NOT
  gravitational wave strain.

  GW radiation requires TIME-VARYING QUADRUPOLE (or higher multipole).
  A spherically symmetric mass fluctuation (monopole) does NOT radiate GW.
  (Birkhoff's theorem: spherically symmetric → no radiation.)

  The constitutive fluctuation delta_rho(r,t) is STOCHASTIC and
  NOT spherically symmetric (different patches fluctuate independently).
  So there IS a quadrupole component.

  But the quadrupole is SUPPRESSED relative to the monopole by:
    Q_ij ~ integral delta_rho(x) (x_i x_j - (1/3) delta_ij r^2) d^3x

  For N incoherent patches of size l_corr at radius r:
    Q ~ delta_m_patch * l_corr^2 * sqrt(N)

  The GW strain from quadrupole radiation at distance R:
    h ~ (G/c^4) * d^2Q/dt^2 / R
    h ~ (G/c^4) * Q * omega^2 / R

  In geometric units (G=c=1):
    h ~ Q * omega^2 / R
    h ~ delta_m_patch * l_corr^2 * omega^2 * sqrt(N) / R

  This is what Epsilon computed. The formula IS correct for quadrupole
  radiation from incoherent patches. The monopole (delta_m_total) does
  not radiate; only the quadrupole (spatial asymmetry) does.

  BUT: the Epsilon estimate assumed the quadrupole efficiency is O(1)
  because l_corr / r ~ 1.7 (correlation length comparable to radius).
  This needs checking.

  For a shell of patches at radius r with patch size l:
    Quadrupole / Monopole ~ (l/r)^2 for l << r
    ~ O(1) for l ~ r

  At ISCO: l_corr = tau_geom * r_s (in physical units)
  l_corr / r_isco = tau_geom / 3 = {:.2f}

  This is ORDER 1. The quadrupole efficiency IS unsuppressed.
  The Epsilon estimate is correct in order of magnitude.
""".format(tau_geom / 3))

    # Now do the careful conversion
    print("  CAREFUL CONVERSION: local perturbation → far-field strain")
    print()

    # Parameters
    sigma_sq_per_D = 1.0 / tau_geom  # sigma^2 / D_geom
    X_geom = 0.5 / (3.0)**2  # 0.0556

    # drho/dPhi at equilibrium
    drho_dPhi = X_geom * (1.0 - tau_geom) / tau_geom**2
    print("  drho/dPhi = {:.4e}".format(drho_dPhi))

    # For a given D/D_max fraction:
    for D_frac in [1.0, 0.1, 0.01, 1e-3, 1e-4, 1e-6, 1e-8]:
        D_geom = D_geom_max * D_frac
        sigma_sq = D_geom / tau_geom
        sigma = math.sqrt(sigma_sq)

        # RMS delta_rho (leading order)
        rms_delta_rho = abs(drho_dPhi) * sigma

        # Quadrupole from one patch
        l_corr = tau_geom  # in r_s units
        V_patch = (4/3) * math.pi * l_corr**3
        delta_m_patch = rms_delta_rho * V_patch

        # Number of patches
        r_geom = 3.0
        N_patches = 4 * math.pi * r_geom**2 / l_corr**2

        # Quadrupole moment
        Q = delta_m_patch * l_corr**2
        omega = 1.0 / tau_geom

        # GW strain at distance R (geometric units)
        # h = Q * omega^2 * sqrt(N) / R
        R_10kpc_m = 3.086e20  # 10 kpc
        R_geom = R_10kpc_m / rs

        h_single_patch = Q * omega**2 / R_geom
        h_total = h_single_patch * math.sqrt(N_patches)

        # Convert to physical frequency
        f_proper = 1.0 / (2 * math.pi * tau_local_s)
        f_isco = 1.0 - 1.0 / 3.0  # f(r) at ISCO
        redshift_factor = math.sqrt(f_isco)
        f_observed = f_proper * redshift_factor

        # S_h for this single source
        S_h = h_total**2 * tau_local_s

        # Omega_GW for this single source
        Omega_single = (2 * math.pi**2 / (3 * H_0**2)) * f_observed**3 * S_h

        if D_frac in [1.0, 0.01, 1e-4, 1e-6, 1e-8]:
            print("  D/D_max = {:.0e}: sigma/X={:.3f}, h={:.2e}, f={:.0f}Hz, S_h={:.2e}, Omega_single={:.2e}".format(
                D_frac, sigma/X_geom, h_total, f_observed, S_h, Omega_single))

    # ================================================================
    # PART V-VI: Population estimate and LIGO confrontation
    # ================================================================
    print("\n" + "=" * 80)
    print("  PART V-VI: POPULATION ESTIMATE AND LIGO CONFRONTATION")
    print("=" * 80)

    # Stellar-mass BH number density
    # Estimated: ~10^7 - 10^8 per galaxy; ~0.01 Mpc^-3 galaxy density
    # n_BH ~ 10^6 Mpc^-3 (order of magnitude)
    n_BH_Mpc3 = 1e6  # BHs per Mpc^3
    n_BH_m3 = n_BH_Mpc3 / (3.086e22)**3  # convert to m^-3

    # Hubble radius
    R_hubble = C / H_0  # ~ 4.4e26 m ~ 14 Gpc

    print("\n  BH number density: ~{:.0e} Mpc^-3".format(n_BH_Mpc3))
    print("  Hubble radius: {:.2e} m = {:.0f} Gpc".format(R_hubble, R_hubble / 3.086e25))

    # For the population: each BH at distance R contributes h ~ h_10kpc * (10 kpc / R)
    # S_h_total = integral n * h(R)^2 * tau * 4*pi*R^2 dR
    # = integral n * h_10kpc^2 * (10kpc)^2 / R^2 * tau * 4*pi*R^2 dR
    # = 4*pi * n * h_10kpc^2 * (10kpc)^2 * tau * integral dR from 0 to R_max
    # = 4*pi * n * h_10kpc^2 * (10kpc)^2 * tau * R_max

    # This integral DIVERGES linearly with R_max. That's the standard result for
    # uniform density sources: each shell contributes equally.
    # In practice, R_max ~ Hubble radius / (1+z_cutoff).

    R_10kpc = 3.086e20  # m

    print("\n  CONFRONTATION WITH O4a LIMITS:")
    print()
    print("  {:>10s} {:>10s} {:>12s} {:>14s} {:>14s} {:>10s}".format(
        "D/D_max", "sigma/X", "h(10kpc)", "Omega_pop", "O4a limit", "Status"))
    print("  " + "-" * 75)

    for D_frac in [1.0, 0.1, 0.01, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]:
        D_geom = D_geom_max * D_frac
        sigma_sq = D_geom / tau_geom
        sigma = math.sqrt(sigma_sq)
        sigma_over_X = sigma / X_geom

        rms_delta_rho = abs(drho_dPhi) * sigma
        delta_m_patch = rms_delta_rho * (4/3) * math.pi * tau_geom**3
        Q = delta_m_patch * tau_geom**2
        omega = 1.0 / tau_geom
        R_geom = R_10kpc / rs

        h_10kpc = Q * omega**2 * math.sqrt(N_patches) / R_geom

        # Population S_h
        S_h_pop = 4 * math.pi * n_BH_m3 * h_10kpc**2 * R_10kpc**2 * tau_local_s * R_hubble

        # Omega_GW
        f_obs = f_proper * redshift_factor
        Omega_pop = (2 * math.pi**2 / (3 * H_0**2)) * f_obs**3 * S_h_pop

        # Compare to O4a flat limit
        status = "EXCLUDED" if Omega_pop > OMEGA_LIMIT_FLAT else "allowed"
        if sigma_over_X > 1.0:
            status += " (NL!)"

        print("  {:10.0e} {:10.3f} {:12.2e} {:14.2e} {:14.2e} {:>10s}".format(
            D_frac, sigma_over_X, h_10kpc, Omega_pop, OMEGA_LIMIT_FLAT, status))

    # Find the D/D_max that saturates the O4a limit
    print("\n  --- Solving for D_max allowed by O4a ---")
    # Omega_pop scales as D^2 (through h^2 which scales as D^2 through sigma^2 ~ D)
    # Wait: h ~ delta_rho * V * omega^2 / R ~ drho/dPhi * sigma * ... ~ sigma ~ sqrt(D)
    # So h ~ sqrt(D), h^2 ~ D, S_h ~ D, Omega ~ D
    # NO: h ~ drho/dPhi * sigma ~ sigma ~ sqrt(D)
    # h^2 ~ D, S_h ~ D * tau, Omega ~ D

    # Actually: let me trace more carefully.
    # sigma = sqrt(D/tau_geom), so sigma ~ D^(1/2)
    # delta_rho ~ drho/dPhi * sigma ~ D^(1/2)
    # delta_m ~ delta_rho * V ~ D^(1/2)
    # Q ~ delta_m * l^2 ~ D^(1/2)
    # h ~ Q * omega^2 / R ~ D^(1/2)
    # h^2 ~ D
    # S_h ~ h^2 * tau ~ D
    # Omega ~ f^3 * S_h ~ D

    # So Omega_pop scales LINEARLY with D_frac (not quadratically!).
    # Let me find D_frac where Omega_pop = Omega_limit

    # Compute at D_frac = 1
    D_geom_1 = D_geom_max
    sigma_1 = math.sqrt(D_geom_1 / tau_geom)
    rms_rho_1 = abs(drho_dPhi) * sigma_1
    dm_1 = rms_rho_1 * (4/3) * math.pi * tau_geom**3
    Q_1 = dm_1 * tau_geom**2
    h_1 = Q_1 * omega**2 * math.sqrt(N_patches) / R_geom
    S_h_pop_1 = 4 * math.pi * n_BH_m3 * h_1**2 * R_10kpc**2 * tau_local_s * R_hubble
    Omega_1 = (2 * math.pi**2 / (3 * H_0**2)) * f_obs**3 * S_h_pop_1

    print("  Omega_pop at D_max: {:.2e}".format(Omega_1))
    print("  O4a limit (flat): {:.2e}".format(OMEGA_LIMIT_FLAT))

    D_frac_limit = OMEGA_LIMIT_FLAT / Omega_1  # since Omega scales linearly with D_frac
    print("  D/D_max allowed: {:.2e}".format(D_frac_limit))
    print()

    sigma_at_limit = math.sqrt(D_geom_max * D_frac_limit / tau_geom)
    print("  At the O4a bound:")
    print("    D = {:.2e} * D_max".format(D_frac_limit))
    print("    sigma/X = {:.4f}".format(sigma_at_limit / X_geom))
    print("    h(10 kpc) = {:.2e}".format(h_1 * math.sqrt(D_frac_limit)))
    print("    Perturbative: {}".format("YES" if sigma_at_limit / X_geom < 0.3 else "MARGINAL"))

    # ================================================================
    # FINAL VERDICT
    # ================================================================
    print("\n" + "=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)

    if D_frac_limit < 1e-10:
        verdict = "window collapses: D forced below useful range"
    elif D_frac_limit < 1e-4:
        verdict = "window exists but narrow"
    elif D_frac_limit < 0.1:
        verdict = "healthy window survives"
    else:
        verdict = "no useful constraint from current data"

    print("""
  LIGO O4a stochastic background limit: Omega_GW < {limit:.1e} (flat, 95% CL)
  GRUT-II population Omega_GW at D_max: {omega:.1e}

  GRUT-II is {'EXCLUDED' if Omega_1 > OMEGA_LIMIT_FLAT else 'allowed'} at D = D_max.

  The O4a limit constrains D to:
    D < {frac:.2e} * D_max

  At this bound:
    sigma/X = {sX:.4f} ({'perturbative' if sigma_at_limit/X_geom < 0.3 else 'marginal'})
    h(10 kpc) = {h:.2e}

  WINDOW STATUS: {verdict}

  The GRUT-II prediction at D = D_max is {ratio:.0e}x above the O4a limit.
  Existing data ALREADY constrains D to {frac:.2e} of its maximum.
  This is a REAL observational bound on a GRUT-II parameter from LIGO data.
  """.format(
        limit=OMEGA_LIMIT_FLAT,
        omega=Omega_1,
        frac=D_frac_limit,
        sX=sigma_at_limit/X_geom,
        h=h_1*math.sqrt(D_frac_limit),
        verdict=verdict,
        ratio=Omega_1/OMEGA_LIMIT_FLAT
    ))
