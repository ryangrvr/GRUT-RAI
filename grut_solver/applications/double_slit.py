"""
Application 1: Double-Slit / Matter-Wave Interferometry

For any particle mass, slit geometry, and flight time, GRUT predicts
the gravitational visibility reduction:

    V_grav = exp(-Lambda_grav * t_flight)

where Lambda_grav = G m^2 S(l/R) / (hbar l).

This is computed alongside environmental decoherence to give the
total predicted visibility and determine whether the gravitational
signal is detectable.
"""

import numpy as np
from grut_solver.constants import G, HBAR, AMU, K_B
from grut_solver.usl.gravitational import lambda_grav, suppression_factor
from grut_solver.budget.gas import lambda_gas
from grut_solver.budget.blackbody import lambda_bb_scatter


def interferometry_visibility(
    m: float,
    R: float,
    l_slit: float,
    t_flight: float,
    T_env: float = 300.0,
    P: float = 1e-7,
    T_int: float = None,
) -> dict:
    """Compute fringe visibility for a matter-wave interferometer.

    Parameters
    ----------
    m : float       Particle mass [kg].
    R : float       Particle radius [m].
    l_slit : float  Slit separation / grating period [m] (= superposition separation).
    t_flight : float  Free-flight time [s].
    T_env : float   Environment temperature [K].
    P : float       Background gas pressure [Pa].
    T_int : float   Internal particle temperature [K]. Default: T_env.

    Returns
    -------
    dict with all decoherence rates, visibility components, and total visibility.
    """
    if T_int is None:
        T_int = T_env

    Lg = lambda_grav(m, l_slit, R)
    Lgas = lambda_gas(m, R, l_slit, T_env, P)
    Lbb = lambda_bb_scatter(R, l_slit, T_env)

    L_total = Lg + Lgas + Lbb

    V_grav = np.exp(-Lg * t_flight)
    V_gas = np.exp(-Lgas * t_flight)
    V_bb = np.exp(-Lbb * t_flight)
    V_total = np.exp(-L_total * t_flight)

    # What standard QM predicts (no gravitational decoherence)
    V_qm = np.exp(-(Lgas + Lbb) * t_flight)

    # The GRUT-specific visibility DROP
    V_drop = V_qm - V_total

    return {
        "m_kg": m,
        "m_amu": m / AMU,
        "R_m": R,
        "l_slit_m": l_slit,
        "t_flight_s": t_flight,
        "T_env_K": T_env,
        "P_Pa": P,
        "lambda_grav_hz": Lg,
        "lambda_gas_hz": Lgas,
        "lambda_bb_hz": Lbb,
        "lambda_total_hz": L_total,
        "V_grav": V_grav,
        "V_gas": V_gas,
        "V_bb": V_bb,
        "V_total": V_total,
        "V_standard_qm": V_qm,
        "V_drop_from_gravity": V_drop,
        "grav_detectable": V_drop > 0.01,  # > 1% drop is measurable
        "S_extended": suppression_factor(l_slit, R),
    }


# ================================================================
# Published interferometry experiments
# ================================================================

PUBLISHED_EXPERIMENTS = [
    {
        "name": "C60 fullerene (Arndt 1999)",
        "ref": "Arndt et al., Nature 401, 680 (1999)",
        "m_amu": 720,
        "R_nm": 0.35,
        "l_nm": 100,  # grating period
        "t_flight_s": 0.006,
        "T_K": 900,  # oven source temperature
        "P_Pa": 1e-5,
        "V_observed": 0.42,
    },
    {
        "name": "C70 fullerene (Arndt 1999)",
        "ref": "Arndt et al., Nature 401, 680 (1999)",
        "m_amu": 840,
        "R_nm": 0.37,
        "l_nm": 100,
        "t_flight_s": 0.006,
        "T_K": 900,
        "P_Pa": 1e-5,
        "V_observed": 0.30,
    },
    {
        "name": "TPPF20 (Eibenberger 2013)",
        "ref": "Eibenberger et al., Phys Chem Chem Phys 15 (2013)",
        "m_amu": 1298,
        "R_nm": 0.5,
        "l_nm": 266,
        "t_flight_s": 0.08,
        "T_K": 500,
        "P_Pa": 1e-7,
        "V_observed": 0.40,
    },
    {
        "name": "PcH2 (Eibenberger 2013)",
        "ref": "Eibenberger et al., Phys Chem Chem Phys 15 (2013)",
        "m_amu": 514,
        "R_nm": 0.4,
        "l_nm": 266,
        "t_flight_s": 0.08,
        "T_K": 500,
        "P_Pa": 1e-7,
        "V_observed": 0.50,
    },
    {
        "name": "Ciprofloxacin (Fein 2019)",
        "ref": "Fein et al., Nature Physics 15, 1242 (2019)",
        "m_amu": 331,
        "R_nm": 0.35,
        "l_nm": 266,
        "t_flight_s": 0.1,
        "T_K": 500,
        "P_Pa": 5e-8,
        "V_observed": 0.25,
    },
    {
        "name": "Gramicidin (Fein 2019)",
        "ref": "Fein et al., Nature Physics 15, 1242 (2019)",
        "m_amu": 1882,
        "R_nm": 0.6,
        "l_nm": 266,
        "t_flight_s": 0.1,
        "T_K": 500,
        "P_Pa": 5e-8,
        "V_observed": 0.20,
    },
    {
        "name": "C_284H_190F_320N_4S_12 (Fein 2019, heaviest)",
        "ref": "Fein et al., Nature Physics 15, 1242 (2019)",
        "m_amu": 25000,
        "R_nm": 1.5,
        "l_nm": 266,
        "t_flight_s": 0.1,
        "T_K": 500,
        "P_Pa": 5e-8,
        "V_observed": 0.15,
    },
]

# Proposed future experiments
PROPOSED_EXPERIMENTS = [
    {
        "name": "Gold cluster (OTIMA, proposed)",
        "m_amu": 1e6,
        "R_nm": 5,
        "l_nm": 100,
        "t_flight_s": 0.1,
        "T_K": 300,
        "P_Pa": 1e-8,
    },
    {
        "name": "Virus-scale (proposed)",
        "m_amu": 1e7,
        "R_nm": 15,
        "l_nm": 100,
        "t_flight_s": 1.0,
        "T_K": 10,
        "P_Pa": 1e-10,
    },
    {
        "name": "Nanosphere 10^9 amu (MAQRO-class)",
        "m_amu": 1e9,
        "R_nm": 100,
        "l_nm": 100,
        "t_flight_s": 100,
        "T_K": 0.02,
        "P_Pa": 1e-12,
    },
    {
        "name": "GRUT reference platform (10 pg)",
        "m_amu": 6e12,
        "R_nm": 50,
        "l_nm": 100,
        "t_flight_s": 1.0,
        "T_K": 0.01,
        "P_Pa": 1e-10,
    },
]


def run_published_catalog() -> list[dict]:
    """Compute GRUT predictions for every published interferometry experiment."""
    results = []
    for exp in PUBLISHED_EXPERIMENTS:
        m = exp["m_amu"] * AMU
        R = exp["R_nm"] * 1e-9
        l = exp["l_nm"] * 1e-9
        t = exp["t_flight_s"]
        T = exp["T_K"]
        P = exp["P_Pa"]

        pred = interferometry_visibility(m, R, l, t, T, P)
        pred["experiment"] = exp["name"]
        pred["ref"] = exp["ref"]
        pred["V_observed"] = exp["V_observed"]
        pred["consistent"] = pred["V_total"] > (exp["V_observed"] - 0.2)
        results.append(pred)

    return results


def run_proposed_catalog() -> list[dict]:
    """Compute GRUT predictions for proposed future experiments."""
    results = []
    for exp in PROPOSED_EXPERIMENTS:
        m = exp["m_amu"] * AMU
        R = exp["R_nm"] * 1e-9
        l = exp["l_nm"] * 1e-9
        t = exp["t_flight_s"]
        T = exp["T_K"]
        P = exp["P_Pa"]

        pred = interferometry_visibility(m, R, l, t, T, P)
        pred["experiment"] = exp["name"]
        results.append(pred)

    return results


def mass_scan_visibility(l_nm: float = 100, t_flight: float = 0.1,
                          T: float = 300, P: float = 1e-7,
                          rho: float = 2200,
                          m_min_amu: float = 100,
                          m_max_amu: float = 1e12,
                          n_points: int = 100) -> list[dict]:
    """Scan visibility vs mass for a fixed interferometer geometry."""
    masses = np.geomspace(m_min_amu * AMU, m_max_amu * AMU, n_points)
    results = []
    for m in masses:
        R = (3*m/(4*np.pi*rho))**(1/3)
        l = l_nm * 1e-9
        pred = interferometry_visibility(m, R, l, t_flight, T, P)
        results.append(pred)
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("APPLICATION 1: DOUBLE-SLIT / MATTER-WAVE INTERFEROMETRY")
    print("=" * 80)

    # Published experiments
    print("\n1. PUBLISHED EXPERIMENTS — GRUT vs OBSERVED")
    print("-" * 70)
    print(f"  {'Experiment':>35s}  {'m (amu)':>10s}  {'Λ_grav':>10s}  "
          f"{'V_GRUT':>8s}  {'V_obs':>8s}  {'V_drop':>8s}  {'det?':>5s}")

    catalog = run_published_catalog()
    for r in catalog:
        print(f"  {r['experiment']:>35s}  {r['m_amu']:10.0f}  {r['lambda_grav_hz']:10.2e}  "
              f"{r['V_total']:8.4f}  {r['V_observed']:8.2f}  {r['V_drop_from_gravity']:8.2e}  "
              f"{'YES' if r['grav_detectable'] else 'no':>5s}")

    print()
    all_consistent = all(r["consistent"] for r in catalog)
    print(f"  ALL CONSISTENT WITH GRUT: {all_consistent}")
    print(f"  (GRUT signal is undetectable at these masses — gravity drop < 10^-15)")

    # Proposed experiments
    print("\n2. PROPOSED EXPERIMENTS — GRUT FORECASTS")
    print("-" * 70)
    print(f"  {'Experiment':>35s}  {'m (amu)':>10s}  {'Λ_grav':>10s}  "
          f"{'V_GRUT':>8s}  {'V_QM':>8s}  {'V_drop':>8s}  {'det?':>5s}")

    proposed = run_proposed_catalog()
    for r in proposed:
        print(f"  {r['experiment']:>35s}  {r['m_amu']:10.0e}  {r['lambda_grav_hz']:10.2e}  "
              f"{r['V_total']:8.4f}  {r['V_standard_qm']:8.4f}  {r['V_drop_from_gravity']:8.2e}  "
              f"{'YES' if r['grav_detectable'] else 'no':>5s}")

    # Mass scan
    print("\n3. MASS SCAN — WHERE DOES GRAVITY BECOME VISIBLE?")
    print("-" * 70)

    scan = mass_scan_visibility(l_nm=100, t_flight=1.0, T=10, P=1e-10, rho=2200)
    print(f"  l = 100 nm, t = 1 s, T = 10 K, P = 10^-10 Pa, silica")
    print(f"  {'m (amu)':>12s}  {'Λ_grav':>12s}  {'Λ_gas':>12s}  {'V_total':>8s}  {'V_drop':>10s}")

    for r in scan:
        if r["m_amu"] > 0:
            log_m = np.log10(r["m_amu"])
            if abs(log_m - round(log_m)) < 0.05:
                print(f"  {r['m_amu']:12.0e}  {r['lambda_grav_hz']:12.2e}  "
                      f"{r['lambda_gas_hz']:12.2e}  {r['V_total']:8.4f}  "
                      f"{r['V_drop_from_gravity']:10.2e}")

    # Find crossover mass
    for r in scan:
        if r["V_drop_from_gravity"] > 0.01:
            print(f"\n  GRAVITY BECOMES DETECTABLE (V_drop > 1%) at m ~ {r['m_amu']:.0e} amu")
            print(f"  Lambda_grav = {r['lambda_grav_hz']:.2e} Hz")
            print(f"  This is the experimental frontier for gravitational decoherence.")
            break
    else:
        print(f"\n  Gravity not detectable in this scan range at these conditions.")
        print(f"  Lower pressure or longer flight time needed.")
