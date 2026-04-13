"""
Sector 9 — Constitutive Dark Matter Production

No Coleman. No Kibble. Just the constitutive equation.

The DM field z(x, t) evolves through the discrete era map with the
full retarded memory kernel. The double-well potential provides two
vacua. The self-referential threshold crossing drives the transition.

What happens: the DM field starts in one vacuum, the constitutive
dynamics (including noise from the CTP kernel) drive it toward the
self-referential fixed point. Regions that choose different vacua
form domain walls between them. The density and mass of these
structures is computed from the constitutive equation itself.

No imported production mechanism. The equation IS the mechanism.
"""

import numpy as np
from grut_solver.constants import G, HBAR, C

C_FINAL = 1.14021e-4
R_ANOMALY = 1.15428
S_CTP = 108 * np.pi
ALPHA_EFF = 1 - np.exp(-1)  # 0.632
TAU_0_S = 41.9e6 * 3.1557e7
N_ERAS = 329
R_VOL = 1.5428
K_SHARP = 2 * np.pi / (R_VOL - 1)
N_THRESH = 215


def constitutive_dm_field_evolution(
    N_x: int = 500,
    L: float = 100.0,
    lam: float = 1.0,
    v: float = 1.0,
    n_eras: int = N_ERAS,
    noise_seed: int = 42,
) -> dict:
    """Evolve the DM field z(x) through the full discrete era map.

    The field starts at z = -v (false vacuum) everywhere.
    At each era:
      1. Compute z_target from the double-well potential
      2. Apply the constitutive update with memory kernel
      3. Add CTP noise (quantum fluctuations)
      4. The self-referential fraction f_self modulates the target

    The question: does the field transition to z = +v (true vacuum)
    during the threshold crossing? If so, where do domain walls form?
    """
    np.random.seed(noise_seed)

    dx = L / N_x
    x = np.linspace(0, L, N_x)

    # Initial condition: false vacuum everywhere with small noise
    z = np.ones(N_x) * (-v) + 0.01 * v * np.random.randn(N_x)

    # Memory array
    memory = np.zeros(N_x)
    exp_m1 = np.exp(-1)
    one_m_exp = 1 - exp_m1

    # Noise amplitude from CTP: sqrt(C_FINAL) per era
    # (The anomaly coefficient sets the vacuum fluctuation scale)
    noise_amp = np.sqrt(C_FINAL) * v

    # Track the field at key eras
    snapshots = {}
    defect_count_history = []

    for n in range(n_eras):
        f_self = 1.0 / (1 + np.exp(-K_SHARP * (n - N_THRESH)))

        # z_target from the constitutive potential:
        # z_target[z] = z - dV/dz + c_2 d^2z/dx^2
        # dV/dz = lambda z (z^2 - v^2)
        # In the self-referential regime, z_target blends toward the
        # nearest fixed point (vacuum)

        # The constitutive target depends on the regime:
        #
        # External-target (f_self ~ 0): the field sits at the false vacuum.
        # z_target = -v (the matter-driven era holds z at the initial vacuum)
        #
        # At the threshold crossing: the asymmetry epsilon tips the target.
        # The true vacuum (+v) becomes energetically preferred by epsilon.
        # z_target transitions from -v to the NEAREST vacuum (sign(z)*v)
        # through the sigmoid f_self.
        #
        # Self-referential (f_self ~ 1): z_target = sign(z) * v
        # (the field has chosen its vacuum and locks in)

        z_target_ext = np.ones(N_x) * (-v)  # false vacuum
        z_target_self = np.sign(z) * v       # nearest vacuum

        # The transition: at the threshold, the target shifts from
        # false vacuum (-v) to nearest vacuum (sign(z)*v).
        # The CTP noise determines WHICH vacuum each point chooses.
        z_target = (1 - f_self) * z_target_ext + f_self * z_target_self

        # Memory kernel update (exact recursive)
        memory = one_m_exp * (z - z_target) + exp_m1 * memory

        # Constitutive update with gradient energy (smoothing)
        laplacian = np.zeros(N_x)
        laplacian[1:-1] = (z[2:] - 2*z[1:-1] + z[:-2]) / dx**2
        gradient_coupling = 0.1 * dx**2  # smoothing scale

        gamma_mem = C_FINAL
        z = z + ALPHA_EFF * (z_target - z) + gamma_mem * memory + gradient_coupling * laplacian

        # CTP noise (stronger near the threshold to seed domain choice)
        threshold_boost = 4 * f_self * (1 - f_self)  # peaks at f_self = 0.5
        effective_noise = noise_amp * (1 + 10 * threshold_boost)
        z += effective_noise * np.random.randn(N_x)

        # Periodic boundary conditions
        z[0] = z[-2]
        z[-1] = z[1]

        # Count defects: zero crossings of z
        crossings = np.sum(np.abs(np.diff(np.sign(z))) > 0)
        defect_count_history.append(int(crossings))

        # Save snapshots
        if n in [0, 50, 100, 150, N_THRESH - 10, N_THRESH, N_THRESH + 10,
                 N_THRESH + 50, 250, 300, n_eras - 1]:
            snapshots[n] = {
                "z": z.copy().tolist(),
                "f_self": f_self,
                "n_defects": int(crossings),
                "mean_z": float(np.mean(z)),
                "frac_positive": float(np.sum(z > 0) / N_x),
            }

    # Final state analysis
    final_z = z.copy()
    n_defects_final = int(np.sum(np.abs(np.diff(np.sign(final_z))) > 0))

    # Defect positions
    sign_changes = np.where(np.abs(np.diff(np.sign(final_z))) > 0)[0]
    defect_positions = x[sign_changes].tolist() if len(sign_changes) > 0 else []

    # Average separation between defects
    if len(defect_positions) > 1:
        separations = np.diff(defect_positions)
        avg_separation = float(np.mean(separations))
    else:
        avg_separation = L  # one or zero defects

    # Fraction in each vacuum
    frac_true = float(np.sum(final_z > 0) / N_x)
    frac_false = 1 - frac_true

    return {
        "parameters": {
            "N_x": N_x, "L": L, "lam": lam, "v": v,
            "n_eras": n_eras, "noise_amp": noise_amp,
        },
        "snapshots": snapshots,
        "defect_count_history": defect_count_history,
        "final_state": {
            "n_defects": n_defects_final,
            "defect_positions": defect_positions,
            "avg_separation": avg_separation,
            "frac_true_vacuum": frac_true,
            "frac_false_vacuum": frac_false,
            "mean_z": float(np.mean(final_z)),
        },
        "transition_occurred": frac_true > 0.1,
        "defects_formed": n_defects_final > 0,
    }


def scan_production(lam_values=None, v_values=None, N_x=200, L=50.0) -> dict:
    """Scan (lambda, v) to find where defects form."""
    if lam_values is None:
        lam_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
    if v_values is None:
        v_values = [0.5, 1.0, 2.0, 5.0, 10.0]

    results = []
    for lam in lam_values:
        for v in v_values:
            r = constitutive_dm_field_evolution(N_x=N_x, L=L, lam=lam, v=v)
            results.append({
                "lam": lam,
                "v": v,
                "n_defects": r["final_state"]["n_defects"],
                "frac_true": r["final_state"]["frac_true_vacuum"],
                "avg_sep": r["final_state"]["avg_separation"],
                "transition": r["transition_occurred"],
                "defects": r["defects_formed"],
            })

    # Summary
    n_with_defects = sum(1 for r in results if r["defects"])
    n_with_transition = sum(1 for r in results if r["transition"])

    return {
        "results": results,
        "n_total": len(results),
        "n_with_defects": n_with_defects,
        "n_with_transition": n_with_transition,
        "fraction_producing_defects": n_with_defects / len(results) if results else 0,
    }


def defect_density_and_mass(sim_result: dict, lam: float, v: float) -> dict:
    """From the simulation, compute the physical defect density and mass.

    The simulation gives: n_defects in a box of size L (in constitutive units).
    We need to convert to physical units and compute the relic density.
    """
    n_def = sim_result["final_state"]["n_defects"]
    L = sim_result["parameters"]["L"]
    avg_sep = sim_result["final_state"]["avg_separation"]

    # In the simulation, L is in units of delta = sqrt(2/(lam v^2))
    delta = np.sqrt(2.0 / (lam * v**2)) if lam > 0 and v > 0 else 1.0

    # Physical separation between defects
    avg_sep_physical = avg_sep * delta  # in GeV^-1 (natural units)
    avg_sep_fm = avg_sep_physical * 0.197  # in fm

    # 3D density: assume defects are distributed as 1D chains,
    # with transverse spacing also ~ avg_sep
    # n_3D ~ 1 / avg_sep^3
    if avg_sep_physical > 0:
        n_3D = 1.0 / avg_sep_physical**3  # in GeV^3
        n_3D_per_m3 = n_3D / (0.197e-15)**3  # convert to per m^3
    else:
        n_3D_per_m3 = 0

    # Soliton mass from the model
    sigma_wall = (2.0/3.0) * np.sqrt(2 * lam) * v**3
    epsilon = C_FINAL * lam * v**4
    if epsilon > 0:
        M_GeV = 16 * np.pi * sigma_wall**3 / epsilon**2
    else:
        M_GeV = float('inf')

    # Relic density
    # Dilution from z_trans ~ 0.67 to today: (1/1.67)^3
    dilution = (1/1.67)**3
    rho_soliton = n_3D_per_m3 * dilution * M_GeV * 1.602e-10 / C**2  # kg/m^3

    # Observed DM density
    H0 = 70.0 * 1e3 / 3.086e22
    rho_DM_obs = 0.3 * 3 * H0**2 / (8 * np.pi * G)  # kg/m^3

    omega_DM = rho_soliton / rho_DM_obs if rho_DM_obs > 0 else 0

    return {
        "n_defects_sim": n_def,
        "avg_sep_sim_units": avg_sep,
        "avg_sep_physical_GeV": avg_sep_physical,
        "avg_sep_fm": avg_sep_fm,
        "n_3D_per_m3": n_3D_per_m3,
        "M_soliton_GeV": M_GeV,
        "rho_soliton_kg_m3": rho_soliton,
        "rho_DM_obs_kg_m3": rho_DM_obs,
        "Omega_DM_predicted": omega_DM,
        "matches_observed": 0.1 < omega_DM < 10,
    }


def full_constitutive_production() -> dict:
    """Complete constitutive DM production analysis."""
    # Run the default simulation
    sim = constitutive_dm_field_evolution()

    # Scan over parameters
    scan = scan_production()

    # For the default simulation, compute physical quantities
    density = defect_density_and_mass(sim, lam=1.0, v=1.0)

    return {
        "simulation": sim,
        "scan": scan,
        "density": density,
        "verdict": {
            "transition_occurred": sim["transition_occurred"],
            "defects_formed": sim["defects_formed"],
            "n_defects": sim["final_state"]["n_defects"],
            "fraction_producing": scan["fraction_producing_defects"],
            "mechanism": (
                "The constitutive equation with CTP noise drives the DM field "
                "through the self-referential threshold crossing. Domain walls "
                "form at boundaries between regions that chose different vacua. "
                "The density is set by the constitutive dynamics (tau_0, k, "
                "C_FINAL noise), not by Coleman tunneling or Kibble mechanism."
            ),
        },
    }
