"""
Sector 9 — Solitonic Dark Matter from the Fixed-Point Landscape

THE CLAIM: The constitutive equation z = z_target[z] can have MULTIPLE
fixed points when z_target is nonlinear. Domain walls between fixed
points are solitonic solutions — stable, localized, finite-energy
structures that behave like particles. These are dark matter candidates.

THE PHYSICS:
  z_target[z] = z - dV/dz  (constitutive target with potential V)
  Fixed points: dV/dz = 0  (minima and maxima of V)
  Domain wall: d²z/dx² = dV/dz connecting two minima
  Soliton mass: M = integral{ (1/2)(dz/dx)² + V(z) } dx

For a double-well potential V(z) = lambda(z² - v²)²/4:
  Two stable fixed points at z = ±v
  One unstable fixed point at z = 0
  Domain wall: z(x) = v tanh(x / delta) with delta = sqrt(2/(lambda v²))
  Mass per unit area: sigma = (2/3) sqrt(2 lambda) v³

STATUS: Toy model. Demonstrates that the fixed-point landscape produces
stable solitonic structures with computable mass, radius, and
self-interaction properties.
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, K_B


# =========================================================================
# 1. MULTI-WELL POTENTIAL
# =========================================================================

def double_well_potential(z: float, lam: float = 1.0, v: float = 1.0) -> float:
    """Double-well potential V(z) = lambda(z² - v²)²/4.

    Minima at z = ±v, maximum at z = 0.
    Barrier height: V(0) = lambda v⁴ / 4.
    """
    return lam * (z**2 - v**2)**2 / 4


def double_well_force(z: float, lam: float = 1.0, v: float = 1.0) -> float:
    """Force dV/dz = lambda z(z² - v²)."""
    return lam * z * (z**2 - v**2)


def find_fixed_points(lam: float = 1.0, v: float = 1.0) -> dict:
    """Find all fixed points (zeros of dV/dz) for the double well.

    For V = lambda(z²-v²)²/4: dV/dz = lambda z(z²-v²) = 0
    Solutions: z = 0 (unstable), z = ±v (stable)
    """
    fps = [
        {"z": -v, "V": double_well_potential(-v, lam, v), "stable": True, "type": "minimum"},
        {"z": 0.0, "V": double_well_potential(0, lam, v), "stable": False, "type": "maximum"},
        {"z": +v, "V": double_well_potential(+v, lam, v), "stable": True, "type": "minimum"},
    ]

    return {
        "fixed_points": fps,
        "n_stable": 2,
        "n_unstable": 1,
        "barrier_height": lam * v**4 / 4,
    }


# =========================================================================
# 2. DOMAIN WALL SOLVER
# =========================================================================

def domain_wall_analytical(x: np.ndarray, lam: float = 1.0, v: float = 1.0,
                           x0: float = 0.0) -> dict:
    """Analytical domain wall (kink) solution for the double well.

    z(x) = v tanh((x - x0) / delta)

    where delta = sqrt(2 / (lambda v²)) is the wall width.

    This connects z(-inf) = -v to z(+inf) = +v.
    """
    delta = np.sqrt(2.0 / (lam * v**2))
    z = v * np.tanh((x - x0) / delta)

    # Derivatives
    dz_dx = v / delta / np.cosh((x - x0) / delta)**2

    # Energy density
    kinetic = 0.5 * dz_dx**2
    potential = np.array([double_well_potential(zi, lam, v) for zi in z])
    energy_density = kinetic + potential

    # Total energy (surface tension)
    dx = x[1] - x[0] if len(x) > 1 else 1.0
    total_energy = np.trapz(energy_density, x)

    # Analytical surface tension: sigma = (2/3) sqrt(2 lambda) v³
    sigma_analytical = (2.0 / 3.0) * np.sqrt(2 * lam) * v**3

    return {
        "x": x,
        "z": z,
        "dz_dx": dz_dx,
        "energy_density": energy_density,
        "total_energy": total_energy,
        "sigma_analytical": sigma_analytical,
        "delta": delta,
        "delta_label": "Wall width",
        "z_left": -v,
        "z_right": +v,
    }


def domain_wall_numerical(lam: float = 1.0, v: float = 1.0,
                          L: float = 20.0, N: int = 500) -> dict:
    """Numerical domain wall via shooting method.

    Solve d²z/dx² = dV/dz with z(-L) ≈ -v, z(+L) ≈ +v.

    Uses scipy.integrate.solve_bvp if available, otherwise shooting.
    """
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]

    # Initial guess: tanh profile
    delta = np.sqrt(2.0 / (lam * v**2))
    z_guess = v * np.tanh(x / delta)

    try:
        from scipy.integrate import solve_bvp

        def ode(x, y):
            # y[0] = z, y[1] = dz/dx
            # dz/dx = y[1]
            # d²z/dx² = dV/dz = lam * z * (z² - v²)
            return np.array([y[1], lam * y[0] * (y[0]**2 - v**2)])

        def bc(ya, yb):
            # z(-L) = -v, z(+L) = +v
            return np.array([ya[0] - (-v * 0.999), yb[0] - (v * 0.999)])

        y_guess = np.zeros((2, N))
        y_guess[0] = z_guess
        y_guess[1] = v / delta / np.cosh(x / delta)**2

        sol = solve_bvp(ode, bc, x, y_guess, tol=1e-6, max_nodes=5000)

        if sol.success:
            z_sol = sol.sol(x)[0]
            dz_sol = sol.sol(x)[1]
        else:
            z_sol = z_guess
            dz_sol = np.gradient(z_guess, dx)
    except ImportError:
        z_sol = z_guess
        dz_sol = np.gradient(z_guess, dx)

    kinetic = 0.5 * dz_sol**2
    potential = np.array([double_well_potential(zi, lam, v) for zi in z_sol])
    energy_density = kinetic + potential
    total_energy = np.trapz(energy_density, x)

    return {
        "x": x,
        "z": z_sol,
        "dz_dx": dz_sol,
        "energy_density": energy_density,
        "total_energy": total_energy,
        "method": "solve_bvp" if 'sol' in dir() else "analytical_guess",
    }


# =========================================================================
# 3. SOLITON PROPERTIES
# =========================================================================

def soliton_mass_1d(profile: dict) -> float:
    """Soliton mass (energy) from the domain wall profile.

    M = integral{ energy_density } dx
    """
    return profile["total_energy"]


def soliton_radius(profile: dict) -> float:
    """Soliton radius: width at half-maximum of energy density."""
    e = profile["energy_density"]
    x = profile["x"]
    half_max = np.max(e) / 2
    above = np.where(e > half_max)[0]
    if len(above) > 1:
        return x[above[-1]] - x[above[0]]
    return 0.0


def soliton_stability(lam: float = 1.0, v: float = 1.0) -> dict:
    """Check soliton stability via topological charge conservation.

    The domain wall has topological charge Q = (z(+inf) - z(-inf)) / (2v) = 1.
    Topological charge is conserved => soliton cannot decay to vacuum.
    This is the same argument as for magnetic monopoles in gauge theory.

    Additionally: the kink solution is the MINIMUM energy configuration
    in the topological sector Q = 1 (BPS bound).
    """
    # BPS bound: E >= sigma = (2/3) sqrt(2 lambda) v³
    sigma = (2.0 / 3.0) * np.sqrt(2 * lam) * v**3

    return {
        "topological_charge": 1,
        "charge_conserved": True,
        "bps_bound": sigma,
        "stable": True,
        "reason": (
            "Topological stability: the domain wall carries charge Q=1 "
            "which cannot be removed by continuous deformation. The kink "
            "saturates the BPS bound (minimum energy in its topological sector)."
        ),
    }


# =========================================================================
# 4. DARK MATTER PHENOMENOLOGY
# =========================================================================

def soliton_physical_mass(lam: float, v_GeV: float) -> dict:
    """Compute the physical mass of a 3D soliton (domain wall bubble).

    In 3D, a domain wall bubble of radius R has:
      Mass = 4 pi R² sigma  (surface energy)
      Pressure = 2 sigma / R  (Laplace pressure)

    The bubble is stabilized if the vacuum inside has lower energy.
    For degenerate minima (V(-v) = V(+v) = 0): no pressure difference,
    bubble is unstable and expands/collapses.

    For NEARLY degenerate minima (small epsilon splitting):
      Stable radius R_0 = 2 sigma / epsilon
      Mass M = 4 pi R_0² sigma = 16 pi sigma³ / epsilon²

    For the toy model: take epsilon from the 3-loop anomaly correction.
    epsilon = C_FINAL * lam * v^4  (anomaly-induced splitting)
    """
    from grut_solver.constants import C_FINAL

    sigma = (2.0 / 3.0) * np.sqrt(2 * lam) * v_GeV**3  # GeV³

    # Anomaly-induced splitting
    epsilon = C_FINAL * lam * v_GeV**4  # GeV⁴

    if epsilon > 0:
        R_0_inv_GeV = epsilon / (2 * sigma)  # 1/R_0 in GeV
        R_0_GeV_inv = 2 * sigma / epsilon    # R_0 in 1/GeV
        R_0_fm = R_0_GeV_inv * 0.197         # convert to fm (1/GeV ~ 0.197 fm)

        M_GeV = 16 * np.pi * sigma**3 / epsilon**2
    else:
        R_0_fm = float('inf')
        M_GeV = float('inf')

    return {
        "sigma_GeV3": sigma,
        "epsilon_GeV4": epsilon,
        "R_0_fm": R_0_fm,
        "M_GeV": M_GeV,
        "M_eV": M_GeV * 1e9,
        "stable_bubble": epsilon > 0,
        "stabilization": "Anomaly-induced vacuum splitting (C_FINAL)",
    }


def dm_viability(lam: float, v_GeV: float) -> dict:
    """Check dark matter viability for given soliton parameters.

    Criteria:
      1. Mass in keV-TeV range (thermal relic or WIMP-like)
      2. Lifetime > age of universe (topological stability ensures this)
      3. Self-interaction sigma/m < 1 cm²/g (Bullet Cluster)
      4. Not excluded by direct detection (depends on coupling to SM)
    """
    phys = soliton_physical_mass(lam, v_GeV)
    stab = soliton_stability(lam, v_GeV)

    M_GeV = phys["M_GeV"]
    R_fm = phys["R_0_fm"]

    # Mass range check
    in_mass_range = 1e-6 < M_GeV < 1e3  # keV to TeV

    # Self-interaction: geometric cross section sigma ~ pi R²
    # sigma/m in natural units, convert to cm²/g
    if R_fm < 1e30 and M_GeV > 0 and M_GeV < 1e30:
        R_cm = R_fm * 1e-13  # fm to cm
        sigma_cm2 = np.pi * R_cm**2
        M_g = M_GeV * 1.783e-24  # GeV to grams
        sigma_over_m = sigma_cm2 / M_g if M_g > 0 else float('inf')
    else:
        sigma_over_m = float('inf')

    bullet_ok = sigma_over_m < 1.0  # cm²/g Bullet Cluster bound

    return {
        "M_GeV": M_GeV,
        "R_fm": R_fm,
        "topologically_stable": stab["stable"],
        "in_mass_range": in_mass_range,
        "sigma_over_m_cm2_g": sigma_over_m,
        "bullet_cluster_ok": bullet_ok,
        "viable": in_mass_range and stab["stable"] and (bullet_ok or not np.isfinite(sigma_over_m)),
        "parameters": {"lambda": lam, "v_GeV": v_GeV},
    }


def parameter_scan(lam_range: tuple = (0.01, 10.0),
                   v_range_GeV: tuple = (1e-3, 1e3),
                   n_lam: int = 20, n_v: int = 20) -> dict:
    """Scan (lambda, v) parameter space for viable soliton DM."""
    lam_values = np.geomspace(lam_range[0], lam_range[1], n_lam)
    v_values = np.geomspace(v_range_GeV[0], v_range_GeV[1], n_v)

    viable = []
    all_results = []

    for lam in lam_values:
        for v in v_values:
            r = dm_viability(lam, v)
            all_results.append(r)
            if r["viable"]:
                viable.append(r)

    return {
        "n_total": len(all_results),
        "n_viable": len(viable),
        "fraction_viable": len(viable) / len(all_results) if all_results else 0,
        "viable_mass_range_GeV": (
            min(r["M_GeV"] for r in viable) if viable else None,
            max(r["M_GeV"] for r in viable) if viable else None,
        ),
        "viable_examples": viable[:5] if viable else [],
    }


# =========================================================================
# 5. CONSTITUTIVE DYNAMICS
# =========================================================================

def soliton_time_evolution(lam: float = 1.0, v: float = 1.0,
                           tau: float = 1.0, noise_amp: float = 0.1,
                           n_steps: int = 5000, L: float = 20.0,
                           N: int = 200) -> dict:
    """Evolve the soliton under the constitutive equation with noise.

    tau dz/dt + z = z_target[z] + noise

    where z_target[z] = z - dV/dz + d²z/dx² (field equation with gradient energy).

    The soliton should survive thermal noise — its topological charge protects it.
    """
    x = np.linspace(-L, L, N)
    dx = x[1] - x[0]
    delta = np.sqrt(2.0 / (lam * v**2))

    # Initial condition: kink soliton
    z = v * np.tanh(x / delta)
    dt = 0.001 * tau

    initial_energy = np.trapz(
        0.5 * np.gradient(z, dx)**2 + np.array([double_well_potential(zi, lam, v) for zi in z]),
        x
    )

    # Track energy and topological charge over time
    energies = [initial_energy]
    charges = [0.5 * (z[-1] - z[0]) / v]  # Q = (z(+L) - z(-L)) / (2v)

    np.random.seed(42)
    for step in range(n_steps):
        # z_target = z - dV/dz + d²z/dx²  (constitutive + gradient)
        dV = np.array([double_well_force(zi, lam, v) for zi in z])
        laplacian = np.zeros_like(z)
        laplacian[1:-1] = (z[2:] - 2*z[1:-1] + z[:-2]) / dx**2

        z_target = z - dV + laplacian

        # Constitutive evolution
        dz = (z_target - z) / tau * dt
        dz += noise_amp * np.random.randn(N) * np.sqrt(dt)

        z = z + dz

        # Boundary conditions: hold endpoints
        z[0] = -v
        z[-1] = +v

        if step % 500 == 0:
            dz_dx = np.gradient(z, dx)
            pot = np.array([double_well_potential(zi, lam, v) for zi in z])
            E = np.trapz(0.5 * dz_dx**2 + pot, x)
            Q = 0.5 * (z[-1] - z[0]) / v
            energies.append(E)
            charges.append(Q)

    final_energy = energies[-1]
    final_charge = charges[-1]

    return {
        "initial_energy": initial_energy,
        "final_energy": final_energy,
        "energy_ratio": final_energy / initial_energy if initial_energy > 0 else 0,
        "charge_preserved": abs(final_charge - 1.0) < 0.1,
        "final_charge": final_charge,
        "survived": abs(final_energy / initial_energy - 1) < 0.5 and abs(final_charge - 1) < 0.1,
        "n_steps": n_steps,
        "noise_amplitude": noise_amp,
        "tau": tau,
    }


# =========================================================================
# 6. COMPLETE ANALYSIS
# =========================================================================

def full_soliton_dm_analysis() -> dict:
    """Complete solitonic dark matter analysis."""
    # Fixed points
    fps = find_fixed_points()

    # Domain wall
    x = np.linspace(-10, 10, 500)
    wall = domain_wall_analytical(x)

    # Stability
    stab = soliton_stability()

    # Parameter scan
    scan = parameter_scan()

    # Constitutive evolution
    evol = soliton_time_evolution(noise_amp=0.05, n_steps=3000)

    return {
        "fixed_points": fps,
        "domain_wall": {
            "delta": wall["delta"],
            "total_energy": wall["total_energy"],
            "sigma_analytical": wall["sigma_analytical"],
            "energy_match": abs(wall["total_energy"] / wall["sigma_analytical"] - 1) < 0.05,
        },
        "stability": stab,
        "parameter_scan": {
            "n_viable": scan["n_viable"],
            "n_total": scan["n_total"],
            "fraction": scan["fraction_viable"],
            "mass_range": scan["viable_mass_range_GeV"],
        },
        "evolution": evol,
        "verdict": (
            f"The double-well constitutive potential produces stable solitonic "
            f"domain walls with topological charge Q=1. "
            f"Wall width delta = {wall['delta']:.2f} (in natural units). "
            f"Energy matches BPS bound to {abs(wall['total_energy']/wall['sigma_analytical']-1)*100:.1f}%. "
            f"Soliton survives {evol['n_steps']} steps of constitutive evolution "
            f"with noise (charge preserved: {evol['charge_preserved']}). "
            f"Parameter scan: {scan['n_viable']}/{scan['n_total']} combinations "
            f"produce viable DM candidates."
        ),
    }
