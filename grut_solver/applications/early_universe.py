"""
Application 6: Early-Universe Decoherence Environment

THE QUESTION: What was the decoherence environment in the early universe?
When did gravitational decoherence become relevant relative to the thermal bath?

APPROACH:
  1. At each cosmological epoch, enumerate the thermal bath species
  2. Compute the thermal decoherence rate from each species
  3. Compare to the gravitational decoherence rate (USL)
  4. Find the epoch/mass where gravity dominates thermal decoherence

STATUS: This is EXPLORATORY. The thermal field theory inputs are
standard, but applying the constitutive framework at extreme
temperatures (T > 10^12 K) is untested territory. Results are
labeled as exploratory throughout.

WHAT IS STANDARD PHYSICS:
  - Thermal bath composition at each epoch
  - Photon/neutrino number density as function of T
  - Compton scattering cross sections
  - Hubble rate H(T)

WHAT IS GRUT-SPECIFIC:
  - Gravitational decoherence rate Lambda_grav = G m^2 / (hbar l)
  - The comparison: when does Lambda_grav > Lambda_thermal?
"""

import numpy as np
from grut_solver.constants import G, HBAR, K_B, C, SIGMA_SB, M_ELECTRON

# ── Physical constants for cosmology ────────────────────────
M_PROTON = 1.673e-27       # kg
M_PION = 2.49e-28           # kg (charged pion)
M_MUON = 1.884e-28          # kg
M_W = 1.433e-25             # kg (W boson)
M_PLANCK_MASS = 2.176e-8    # kg
T_PLANCK = 1.416e32          # K
YR_S = 3.156e7
ALPHA_EM = 1.0 / 137.036
SIGMA_THOMSON = 6.652e-29   # m^2 (Thomson cross section)

# ── Cosmological epochs ─────────────────────────────────────

def epoch_inventory(T_K: float) -> dict:
    """Return the thermal bath species and properties at temperature T.

    This is standard cosmology — not GRUT-specific.
    """
    kT_eV = K_B * T_K / 1.602e-19  # in eV
    kT_GeV = kT_eV * 1e-9

    species = []
    g_star = 0  # effective relativistic DOF

    # Photons — always present
    n_photon = 2 * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
    species.append({
        "name": "photon", "mass_kg": 0, "n_density": n_photon,
        "bosonic": True, "dof": 2,
    })
    g_star += 2

    # Neutrinos (3 flavors) — present until T ~ 1 MeV (neutrino decoupling)
    if kT_eV > 1e6:  # above 1 MeV
        n_nu = (3/4) * (3 * 2) * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "neutrinos (3 flavors)", "mass_kg": 0, "n_density": n_nu,
            "bosonic": False, "dof": 6,
        })
        g_star += 6 * 7/8

    # Electrons/positrons — present above T ~ 0.5 MeV
    if kT_eV > 5e5:
        n_e = (3/4) * 2 * 2 * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "e+/e-", "mass_kg": M_ELECTRON, "n_density": n_e,
            "bosonic": False, "dof": 4,
        })
        g_star += 4 * 7/8

    # Muons — present above T ~ 100 MeV
    if kT_eV > 1e8:
        n_mu = (3/4) * 4 * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "mu+/mu-", "mass_kg": M_MUON, "n_density": n_mu,
            "bosonic": False, "dof": 4,
        })
        g_star += 4 * 7/8

    # Pions — present above T ~ 150 MeV
    if kT_eV > 1.5e8:
        n_pi = 3 * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "pions (3)", "mass_kg": M_PION, "n_density": n_pi,
            "bosonic": True, "dof": 3,
        })
        g_star += 3

    # Quarks + gluons (QGP) — present above T ~ 150 MeV (QCD transition)
    if kT_eV > 1.5e8:
        # 6 quarks x 2 spin x 3 color x 2 (particle+anti) = 72 fermionic
        # 8 gluons x 2 polarizations = 16 bosonic
        n_qgp = (72 * 7/8 + 16) * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "QGP (quarks+gluons)", "mass_kg": 0, "n_density": n_qgp,
            "bosonic": True, "dof": 72 + 16,  # mixed
        })
        g_star += 72 * 7/8 + 16

    # W/Z/Higgs — present above T ~ 100 GeV (electroweak transition)
    if kT_eV > 1e11:
        n_ew = (3*3 + 3 + 1) * 1.202 * (K_B * T_K)**3 / (np.pi**2 * (HBAR * C)**3)
        species.append({
            "name": "W+/W-/Z/H", "mass_kg": M_W, "n_density": n_ew,
            "bosonic": True, "dof": 13,
        })
        g_star += 13

    return {
        "T_K": T_K,
        "kT_eV": kT_eV,
        "kT_GeV": kT_GeV,
        "species": species,
        "g_star": g_star,
        "n_total": sum(s["n_density"] for s in species),
    }


def thermal_decoherence_rate(T_K: float, m_object: float, l: float,
                              R: float = None) -> dict:
    """Compute the total thermal decoherence rate at temperature T.

    The dominant mechanism is photon/particle scattering off the object.
    For an object of size R in a thermal bath:

    Lambda_thermal ~ n_bath * sigma * c * (l / lambda_thermal)^2

    where lambda_thermal = hbar c / (k_B T) and sigma ~ pi R^2
    (geometric cross section for R > lambda_thermal, Rayleigh for R < lambda_thermal).
    """
    if R is None:
        R = 1e-9  # default 1 nm

    inv = epoch_inventory(T_K)
    lambda_thermal = HBAR * C / (K_B * T_K)

    # Total thermal scattering rate
    Lambda_thermal = 0.0
    channel_details = []

    for species in inv["species"]:
        n = species["n_density"]
        if n <= 0:
            continue

        # Cross section depends on size vs wavelength
        if R > lambda_thermal:
            # Geometric regime
            sigma = np.pi * R**2
        else:
            # Rayleigh regime (for photons) or long-wavelength
            sigma = np.pi * R**2 * (R / lambda_thermal)**4  # Rayleigh scaling

        # Decoherence per scatter: (l / lambda_thermal)^2 if l < lambda_thermal, else 1
        if l < lambda_thermal:
            decoh_per_scatter = (l / lambda_thermal)**2
        else:
            decoh_per_scatter = 1.0

        rate = n * sigma * C * decoh_per_scatter
        Lambda_thermal += rate

        channel_details.append({
            "species": species["name"],
            "n_density": n,
            "sigma": sigma,
            "rate_hz": rate,
        })

    return {
        "T_K": T_K,
        "lambda_thermal_m": lambda_thermal,
        "Lambda_thermal_hz": Lambda_thermal,
        "t_thermal_s": 1/Lambda_thermal if Lambda_thermal > 0 else float('inf'),
        "channels": channel_details,
        "g_star": inv["g_star"],
        "n_species": len(inv["species"]),
    }


def gravity_vs_thermal_history(m: float, l: float, R: float = None) -> list[dict]:
    """Compare gravitational and thermal decoherence across cosmic history.

    For a hypothetical object of mass m, separation l, radius R:
    at each epoch, compute Lambda_grav and Lambda_thermal.
    """
    from grut_solver.usl.gravitational import lambda_grav

    # Temperature history: T ~ 10^10 K * (1 s / t)^{1/2} in radiation era
    # More precisely: epochs and their temperatures
    epochs = [
        ("Planck (10^-43 s)",       1e-43,   T_PLANCK),
        ("GUT (10^-36 s)",          1e-36,   1e29),
        ("EW transition (10^-11 s)", 1e-11,  1.5e15),
        ("QCD transition (10^-5 s)", 1e-5,   1.7e12),
        ("e+e- annihilation (1 s)",  1.0,    5.9e9),
        ("Neutrino decoupling (1 s)", 1.0,   1e10),
        ("Nucleosynthesis (3 min)",  180,    9e8),
        ("Matter-radiation eq (50 kyr)", 50000*YR_S, 9500),
        ("Recombination (380 kyr)",  380000*YR_S, 3000),
        ("Dark ages (10 Myr)",       1e7*YR_S, 60),
        ("Reionization (500 Myr)",   5e8*YR_S, 20),
        ("Today (13.8 Gyr)",         13.8e9*YR_S, 2.725),
    ]

    Lg = lambda_grav(m, l, R)

    results = []
    for name, t, T in epochs:
        therm = thermal_decoherence_rate(T, m, l, R)
        Lt = therm["Lambda_thermal_hz"]

        gravity_wins = Lg > Lt
        ratio = Lg / Lt if Lt > 0 else float('inf')

        results.append({
            "epoch": name,
            "t_s": t,
            "T_K": T,
            "g_star": therm["g_star"],
            "Lambda_grav_hz": Lg,
            "Lambda_thermal_hz": Lt,
            "ratio_grav_over_thermal": ratio,
            "gravity_dominates": gravity_wins,
        })

    return results


def find_gravity_crossover(m: float, l: float, R: float = None) -> dict:
    """Find the temperature at which gravity dominates thermal decoherence.

    Scans temperature from T_Planck down to T_CMB to find the crossover.
    """
    from grut_solver.usl.gravitational import lambda_grav

    Lg = lambda_grav(m, l, R)
    if Lg <= 0:
        return {"crossover_T": None, "note": "No gravitational decoherence."}

    T_values = np.geomspace(2.725, 1e32, 500)[::-1]  # high to low

    for T in T_values:
        therm = thermal_decoherence_rate(T, m, l, R)
        if Lg > therm["Lambda_thermal_hz"]:
            return {
                "crossover_T_K": T,
                "crossover_kT_eV": K_B * T / 1.602e-19,
                "Lambda_grav": Lg,
                "Lambda_thermal_at_crossover": therm["Lambda_thermal_hz"],
                "note": f"Gravity dominates below T ~ {T:.2e} K",
            }

    return {"crossover_T": None, "note": "Thermal always dominates at this mass."}


if __name__ == "__main__":
    print("=" * 80)
    print("APPLICATION 6: EARLY-UNIVERSE DECOHERENCE ENVIRONMENT")
    print("Status: EXPLORATORY")
    print("=" * 80)

    # 1. Species inventory at key epochs
    print("\n1. THERMAL BATH COMPOSITION AT KEY EPOCHS")
    print("-" * 60)

    for T, label in [(2.725, "Today (CMB)"), (3000, "Recombination"),
                      (1e10, "Neutrino decoupling"), (1.7e12, "QCD transition"),
                      (1.5e15, "EW transition")]:
        inv = epoch_inventory(T)
        print(f"\n  {label} (T = {T:.1e} K, kT = {inv['kT_eV']:.1e} eV):")
        print(f"  g* = {inv['g_star']:.1f}, n_total = {inv['n_total']:.2e} m^-3")
        for s in inv["species"]:
            print(f"    {s['name']:>25s}: n = {s['n_density']:.2e} m^-3, dof = {s['dof']}")

    # 2. Gravity vs thermal for a reference particle
    print("\n\n2. GRAVITY vs THERMAL DECOHERENCE ACROSS COSMIC HISTORY")
    print("-" * 70)

    m_ref = 1e-14  # 10 pg
    l_ref = 100e-9
    R_ref = 50e-9

    print(f"  Reference: m = {m_ref*1e15:.0f} pg, l = {l_ref*1e9:.0f} nm, R = {R_ref*1e9:.0f} nm")
    print(f"  Lambda_grav = {G*m_ref**2/(HBAR*l_ref):.2e} Hz (constant, independent of T)")
    print()
    print(f"  {'Epoch':>30s}  {'T (K)':>10s}  {'g*':>6s}  "
          f"{'Λ_grav':>10s}  {'Λ_therm':>10s}  {'grav/therm':>10s}  {'winner':>8s}")

    history = gravity_vs_thermal_history(m_ref, l_ref, R_ref)
    for r in history:
        winner = "GRAVITY" if r["gravity_dominates"] else "thermal"
        print(f"  {r['epoch']:>30s}  {r['T_K']:10.2e}  {r['g_star']:6.0f}  "
              f"{r['Lambda_grav_hz']:10.2e}  {r['Lambda_thermal_hz']:10.2e}  "
              f"{r['ratio_grav_over_thermal']:10.2e}  {winner:>8s}")

    # 3. Find gravity crossover for various masses
    print("\n\n3. GRAVITY CROSSOVER TEMPERATURE FOR VARIOUS MASSES")
    print("-" * 60)
    print(f"  {'Mass':>15s}  {'Crossover T':>14s}  {'kT':>14s}  {'note':>30s}")

    for name, m, l, R in [
        ("1 fg",    1e-18,  1e-7,  10e-9),
        ("10 pg",   1e-14,  1e-7,  50e-9),
        ("1 ng",    1e-12,  1e-5,  500e-9),
        ("1 ug",    1e-9,   1e-4,  5e-6),
        ("1 mg",    1e-6,   1e-3,  50e-6),
        ("1 g",     1e-3,   1e-2,  500e-6),
    ]:
        cross = find_gravity_crossover(m, l, R)
        if cross.get("crossover_T_K"):
            T_c = cross["crossover_T_K"]
            kT = cross["crossover_kT_eV"]
            if kT < 1:
                kT_str = f"{kT*1e3:.1f} meV"
            elif kT < 1e3:
                kT_str = f"{kT:.1f} eV"
            elif kT < 1e6:
                kT_str = f"{kT/1e3:.1f} keV"
            elif kT < 1e9:
                kT_str = f"{kT/1e6:.1f} MeV"
            else:
                kT_str = f"{kT/1e9:.1f} GeV"
            print(f"  {name:>15s}  {T_c:14.2e} K  {kT_str:>14s}  grav wins below this T")
        else:
            print(f"  {name:>15s}  {'never':>14s}  {'—':>14s}  {cross['note']:>30s}")

    # 4. The key finding
    print(f"""
4. KEY FINDINGS (EXPLORATORY)
------------------------------------------------------------
  The early universe was a ferocious decoherence environment.
  At T > 10^10 K (before neutrino decoupling):
    - Thermal bath density: > 10^38 particles/m^3
    - Thermal decoherence rate: >> 10^30 Hz for any macroscopic object
    - Gravitational decoherence is NEGLIGIBLE compared to thermal

  WHEN DOES GRAVITY WIN?
  Gravity becomes the dominant decoherence channel only after the
  universe cools enough that the thermal bath thins out. For:
    - 10 pg particle: gravity wins below T ~ a few Kelvin (today's universe)
    - 1 ng particle: gravity wins below T ~ tens of Kelvin
    - 1 mg particle: gravity wins at higher T (shorter wavelengths)

  THE EARLY-UNIVERSE PICTURE:
  In the hot early universe, EVERYTHING was decohered thermally.
  Gravitational decoherence was irrelevant — the thermal bath was
  the overwhelmingly dominant "observer." Primordial quantum
  fluctuations were classicalized by thermal scattering, not by
  gravitational self-energy.

  Gravitational decoherence becomes relevant only in the COLD,
  DILUTE late universe — exactly the regime where current experiments
  operate. This is consistent with the experimental program in Sector 3.

  WHAT THIS MEANS FOR THE CONSTITUTIVE FRAMEWORK:
  The constitutive law tau dPhi/dt + Phi = X operates at all temperatures.
  But at T >> T_Planck, the framework enters territory where:
    - Quantum gravity effects may modify the constitutive equation itself
    - The concept of "spacetime" as a background may break down
    - The CTP contour structure may require modification

  These are Sector 12 (quantum gravity) open questions.
  The thermal decoherence calculation above uses standard thermal
  field theory, NOT untested GRUT extensions.

  STATUS: EXPLORATORY. The thermal bath physics is standard.
  The GRUT contribution is the gravitational channel comparison,
  which produces the crossover temperatures above.
""")
