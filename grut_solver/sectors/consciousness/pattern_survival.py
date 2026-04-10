"""
Sector 13 — Pattern Survival Under Local Decoherence

The core speculative claim: even if individual quantum states decohere
in femtoseconds, COLLECTIVE information (patterns, topology, mutual
information) can survive longer.

This module computes:
  1. Mutual information between subsystems under Lindblad dephasing
  2. Topological index (winding number) survival on MT lattice
  3. Entanglement entropy decay for N-qubit systems

STATUS: Computed (Lindblad dynamics, exact for small N, mean-field beyond).
The INTERPRETATION (that pattern survival enables consciousness) is SPECULATIVE.
"""

import numpy as np
from grut_solver.constants import HBAR


def _pauli_z():
    return np.array([[1, 0], [0, -1]], dtype=complex)

def _pauli_x():
    return np.array([[0, 1], [1, 0]], dtype=complex)

def _identity(n):
    return np.eye(n, dtype=complex)

def _kron_op(op, site, n_sites):
    """Place operator op at site `site` in an n_sites chain (tensor product)."""
    result = np.array([[1.0]], dtype=complex)
    for i in range(n_sites):
        result = np.kron(result, op if i == site else _identity(2))
    return result


def _lindblad_step(rho, H, L_ops, gamma_ops, dt):
    """Single Euler step of the Lindblad master equation.

    drho/dt = -i[H, rho] + sum_k gamma_k (L_k rho L_k^dag - {L_k^dag L_k, rho}/2)
    """
    d = rho.shape[0]
    drho = -1j * (H @ rho - rho @ H)

    for L, gamma in zip(L_ops, gamma_ops):
        Ld = L.conj().T
        LdL = Ld @ L
        drho += gamma * (L @ rho @ Ld - 0.5 * (LdL @ rho + rho @ LdL))

    return rho + drho * dt


def _von_neumann_entropy(rho):
    """Von Neumann entropy S = -Tr(rho log rho)."""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = eigvals[eigvals > 1e-15]
    return float(-np.sum(eigvals * np.log2(eigvals)))


def _partial_trace(rho, n_total, keep_sites):
    """Partial trace: keep specified sites, trace out the rest.

    For small systems only (n_total <= 14).
    """
    d = 2 ** n_total
    n_keep = len(keep_sites)
    d_keep = 2 ** n_keep
    d_trace = d // d_keep

    trace_sites = [s for s in range(n_total) if s not in keep_sites]

    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)

    for i in range(d_keep):
        for j in range(d_keep):
            for k in range(d_trace):
                # Construct full indices
                row_bits = [0] * n_total
                col_bits = [0] * n_total
                for idx, s in enumerate(keep_sites):
                    row_bits[s] = (i >> (n_keep - 1 - idx)) & 1
                    col_bits[s] = (j >> (n_keep - 1 - idx)) & 1
                for idx, s in enumerate(trace_sites):
                    bit = (k >> (len(trace_sites) - 1 - idx)) & 1
                    row_bits[s] = bit
                    col_bits[s] = bit

                row = 0
                col = 0
                for b in range(n_total):
                    row = (row << 1) | row_bits[b]
                    col = (col << 1) | col_bits[b]

                rho_reduced[i, j] += rho[row, col]

    return rho_reduced


def mutual_information_under_decoherence(n_sites: int = 8,
                                         gamma_local: float = 1e15,
                                         J_coupling: float = 1e10,
                                         t_values: list = None) -> dict:
    """Mutual information I(A:B) decay under local dephasing.

    Models a chain of n_sites coupled two-level systems:
      H = J * sum_{<ij>} sigma_z^i sigma_z^j
      L_k = sigma_z^k  (local dephasing at rate gamma)

    Splits into subsystem A (first half) and B (second half).
    Computes I(A:B) = S(A) + S(B) - S(AB) at each time step.

    Parameters
    ----------
    n_sites : int      Number of sites (max ~10 for tractability).
    gamma_local : float  Local dephasing rate [Hz].
    J_coupling : float   Nearest-neighbor coupling strength [Hz].
    t_values : list      Times to evaluate [s]. Default: log-spaced.

    Returns
    -------
    dict with I(A:B) vs time, plus key timescales.
    """
    if n_sites > 10:
        # Fall back to analytical mean-field for large systems
        return _mutual_info_mean_field(n_sites, gamma_local, J_coupling, t_values)

    d = 2 ** n_sites

    # Build Hamiltonian: nearest-neighbor Ising
    H = np.zeros((d, d), dtype=complex)
    for i in range(n_sites - 1):
        sz_i = _kron_op(_pauli_z(), i, n_sites)
        sz_j = _kron_op(_pauli_z(), i + 1, n_sites)
        H += J_coupling * sz_i @ sz_j

    # Lindblad operators: local dephasing
    L_ops = [_kron_op(_pauli_z(), i, n_sites) for i in range(n_sites)]
    gamma_ops = [gamma_local] * n_sites

    # Initial state: GHZ-like entangled state
    psi = np.zeros(d, dtype=complex)
    psi[0] = 1.0 / np.sqrt(2)
    psi[-1] = 1.0 / np.sqrt(2)
    rho = np.outer(psi, psi.conj())

    # Time evolution
    if t_values is None:
        t_values = np.logspace(-18, -8, 50).tolist()

    dt = min(t_values) / 10 if t_values else 1e-19
    # Cap dt for stability: dt < 1 / (4 * gamma * n_sites)
    dt = min(dt, 1.0 / (4 * gamma_local * n_sites))

    n_A = n_sites // 2
    sites_A = list(range(n_A))
    sites_B = list(range(n_A, n_sites))

    results = []
    t_current = 0.0
    t_sorted = sorted(t_values)

    for t_target in t_sorted:
        n_steps = max(1, int((t_target - t_current) / dt))
        actual_dt = (t_target - t_current) / n_steps
        for _ in range(n_steps):
            rho = _lindblad_step(rho, H, L_ops, gamma_ops, actual_dt)
        t_current = t_target

        # Ensure Hermiticity and trace = 1
        rho = 0.5 * (rho + rho.conj().T)
        rho /= np.trace(rho).real

        # Partial traces
        rho_A = _partial_trace(rho, n_sites, sites_A)
        rho_B = _partial_trace(rho, n_sites, sites_B)

        S_AB = _von_neumann_entropy(rho)
        S_A = _von_neumann_entropy(rho_A)
        S_B = _von_neumann_entropy(rho_B)
        I_AB = S_A + S_B - S_AB

        results.append({
            "t_s": t_target,
            "S_A": S_A,
            "S_B": S_B,
            "S_AB": S_AB,
            "I_AB": max(0.0, I_AB),
        })

    # Extract key timescales
    I_initial = results[0]["I_AB"] if results else 0
    I_half_idx = next((i for i, r in enumerate(results)
                       if r["I_AB"] < I_initial / 2), len(results) - 1)
    t_half = results[I_half_idx]["t_s"] if results else 0

    return {
        "n_sites": n_sites,
        "gamma_local_hz": gamma_local,
        "J_coupling_hz": J_coupling,
        "results": results,
        "I_initial": I_initial,
        "t_half_life_s": t_half,
        "t_half_life_label": f"{t_half:.2e} s",
        "note": (
            f"Mutual information half-life: {t_half:.2e} s for "
            f"{n_sites}-site chain with gamma={gamma_local:.0e} Hz. "
            f"At water decoherence rates (~10^15 Hz), mutual info "
            f"decays in ~femtoseconds — same timescale as local coherence."
        ),
    }


def _mutual_info_mean_field(n_sites, gamma, J, t_values):
    """Analytical mean-field result for large N.

    For local dephasing with rate gamma, the mutual information
    decays as I(t) ~ N * exp(-2 gamma t) for a GHZ state.
    """
    if t_values is None:
        t_values = np.logspace(-18, -8, 50).tolist()

    I_0 = 1.0  # 1 bit for GHZ bipartition
    results = []
    for t in t_values:
        decay = np.exp(-2 * gamma * t)
        I_t = I_0 * max(0, decay)
        results.append({"t_s": t, "I_AB": I_t})

    t_half = np.log(2) / (2 * gamma)

    return {
        "n_sites": n_sites,
        "gamma_local_hz": gamma,
        "J_coupling_hz": J,
        "results": results,
        "I_initial": I_0,
        "t_half_life_s": t_half,
        "t_half_life_label": f"{t_half:.2e} s",
        "method": "mean_field",
        "note": f"Mean-field: I half-life = {t_half:.2e} s (ln2 / 2gamma).",
    }


def topological_index_survival(lattice_size: int = 13,
                               n_rings: int = 125,
                               gamma: float = 1e15,
                               t_values: list = None) -> dict:
    """Topological invariant survival on microtubule cylindrical lattice.

    The microtubule is a 13-protofilament helix with ~125 rings.
    Model: assign a phase theta_i to each site on the cylinder.
    The winding number nu = (1/2pi) * sum_{<ij>} (theta_j - theta_i)
    around one ring is a topological invariant.

    Under local phase noise (dephasing), individual theta_i randomize,
    but the WINDING NUMBER can survive if the noise is spatially
    uncorrelated — because uncorrelated noise adds random walks that
    partially cancel around a closed loop.

    This is computed analytically: for N sites around a ring with
    independent Gaussian noise of variance sigma^2 per site,
    the variance of the winding number grows as N * sigma^2 / (2pi)^2.
    The winding number survives (error < 0.5) when sigma < pi / sqrt(N).

    Returns winding number survival probability vs time.
    """
    N = lattice_size  # sites per ring

    if t_values is None:
        t_values = np.logspace(-18, -8, 50).tolist()

    results = []
    for t in t_values:
        # Phase noise variance per site: sigma^2 = 2 * gamma * t
        sigma2 = 2 * gamma * t
        sigma = np.sqrt(sigma2)

        # Winding number error: delta_nu ~ sqrt(N) * sigma / (2pi)
        delta_nu = np.sqrt(N) * sigma / (2 * np.pi)

        # Survival probability: winding number within ±0.5
        # P(|delta_nu| < 0.5) for Gaussian
        if delta_nu > 0:
            from math import erf
            p_survive = erf(0.5 / (delta_nu * np.sqrt(2)))
        else:
            p_survive = 1.0

        results.append({
            "t_s": t,
            "sigma_rad": sigma,
            "delta_nu": delta_nu,
            "p_survive": p_survive,
        })

    # Find survival half-life: when p_survive drops below 0.5
    t_survive = None
    for r in results:
        if r["p_survive"] < 0.5:
            t_survive = r["t_s"]
            break

    # Analytical: p = 0.5 when delta_nu ~ 0.48
    # sqrt(N) * sqrt(2*gamma*t) / (2pi) = 0.48
    # t* = (0.48 * 2pi)^2 / (2 * gamma * N)
    t_analytical = (0.48 * 2 * np.pi)**2 / (2 * gamma * N)

    # Local phase coherence time: sigma = 1 rad when 2*gamma*t = 1 -> t = 1/(2*gamma)
    t_local = 1.0 / (2 * gamma) if gamma > 0 else float('inf')
    ratio = t_analytical / t_local if t_local > 0 else 0

    # For N sites around a ring, the winding number error grows as sqrt(N)
    # relative to individual phases, so the topological index is LESS robust
    # than single-site phase for uncorrelated noise. This is an honest negative result.
    # For CORRELATED noise (which preserves the winding structure), the topological
    # index would survive better — but uncorrelated thermal noise is the relevant case.

    return {
        "lattice_size": N,
        "n_rings": n_rings,
        "gamma_hz": gamma,
        "results": results,
        "t_survive_s": t_survive or t_analytical,
        "t_survive_analytical_s": t_analytical,
        "t_local_coherence_s": t_local,
        "ratio_to_local": ratio,
        "topology_helps": ratio > 1.0,
        "note": (
            f"Topological index (winding number) on {N}-site ring: "
            f"survives {t_analytical:.2e} s vs local phase coherence "
            f"{t_local:.2e} s — ratio {ratio:.2f}x. "
            f"{'Topology helps.' if ratio > 1 else 'Topology does NOT help for uncorrelated noise.'} "
            f"The winding number error grows as sqrt(N) for uncorrelated dephasing, "
            f"making it LESS robust than individual phase coherence. "
            f"Correlated (spatially structured) noise could change this, "
            f"but that requires a specific mechanism."
        ),
    }


def entanglement_entropy_decay(n_qubits: int = 8,
                               decoherence_rate: float = 1e15,
                               t_values: list = None) -> dict:
    """Von Neumann entanglement entropy decay under local dephasing.

    For a GHZ state |000...0> + |111...1>, the entanglement entropy
    of a bipartition has an analytical form:
      S(t) = H(p(t))  where p = (1 + exp(-2 * N * gamma * t)) / 2
      H(p) = -p log2(p) - (1-p) log2(1-p)

    The key result: entanglement entropy decays at rate N * gamma,
    NOT gamma. More qubits = faster decoherence. This is the
    opposite of what pattern survival would need.

    Parameters
    ----------
    n_qubits : int             Number of qubits in GHZ state.
    decoherence_rate : float   Local dephasing rate [Hz].
    t_values : list            Times to evaluate [s].
    """
    if t_values is None:
        t_values = np.logspace(-18, -8, 50).tolist()

    gamma = decoherence_rate
    N = n_qubits

    results = []
    for t in t_values:
        p = 0.5 * (1 + np.exp(-2 * N * gamma * t))
        if 0 < p < 1:
            S = -p * np.log2(p) - (1 - p) * np.log2(1 - p)
        else:
            S = 0.0

        results.append({
            "t_s": t,
            "p": p,
            "S_bits": S,
        })

    # Half-life of entanglement entropy
    t_half = np.log(2) / (2 * N * gamma)

    # Key timescale comparisons
    t_water = 1.0 / gamma
    t_firing = 1e-3
    t_gamma_period = 0.025

    return {
        "n_qubits": N,
        "decoherence_rate_hz": gamma,
        "results": results,
        "S_initial_bits": 1.0,
        "t_half_s": t_half,
        "t_water_s": t_water,
        "t_firing_s": t_firing,
        "t_gamma_s": t_gamma_period,
        "ratio_entropy_to_water": t_half / t_water,
        "note": (
            f"GHZ-{N} entanglement entropy half-life: {t_half:.2e} s. "
            f"This is {N}x FASTER than single-qubit decoherence ({t_water:.2e} s). "
            f"More entanglement = faster decoherence. GHZ states are fragile, "
            f"not robust. Pattern survival requires a different encoding."
        ),
    }
