"""
Book XXI Delta — CTP-Doubled Constitutive Dynamics: Chaos and Lyapunov Exponents
==================================================================================

The CTP (closed-time-path) doubling of the constitutive equation produces
two real modes:

  Phi_plus:   tau * dPhi_plus/dt  + Phi_plus  = X    (CONTRACTING, rate -1/tau)
  Phi_minus:  tau * dPhi_minus/dt - Phi_minus  = 0    (EXPANDING,  rate +1/tau)

Phi_plus is the physical forward mode (standard GRUT).
Phi_minus is the ghost/partner mode — exponentially growing.

QB5 rejected Phi_minus as the imaginary part of a complex amplitude (growth != oscillation).
But Phi_minus EXISTS as a real dynamical variable in the CTP formalism.

OPTION 2 POSTULATE: Phi_minus is physical in certain regimes.

The 4D system:
  (Phi_plus, Phi_minus, f, f')

where f is the hedgehog profile coupled via portal, has:
  - 1 contracting direction (Phi_plus relaxation)
  - 1 expanding direction (Phi_minus growth)
  - 2 spatial BVP directions (f, f')

For chaos we need: >=3D + nonlinearity + expanding AND contracting directions.
The CTP-doubled coupled system has all three.

THIS MODULE:
  1. Formulates the 4D dynamical system
  2. Integrates forward in time from various initial conditions
  3. Computes Lyapunov exponents via QR decomposition method
  4. Tests for sensitive dependence on initial conditions
  5. Searches for parameter regimes with positive maximal Lyapunov exponent

IMPORTANT: Converting the hedgehog BVP (spatial) into a time-evolution system
requires treating r as an evolution parameter. This is standard in the
"shooting method" interpretation: the BVP becomes an IVP in r, and the
4D system (Phi_+, Phi_-, f, f') evolves in the "time" variable r.

The combined system with portal coupling:
  dPhi_+/dr = -(1/tau)*Phi_+ + X(r)/tau + spatial_terms
  dPhi_-/dr = +(1/tau)*Phi_- + coupling_terms
  df/dr     = f'
  df'/dr    = -(2/r)*f' + (2/r^2)*f + lam*eta^2*f*(f^2-1) - g_p*(Phi_+^2 + Phi_-^2)*f
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

# Constants
ETA = 1.0 / math.sqrt(8.0 * math.pi)
TAU = math.sqrt(1.5)
M_EXT = 0.5
R_EQ = 1.0 / 3.0


@dataclass
class LyapunovResult:
    """Lyapunov exponent computation result."""
    lam: float = 0.0
    g_p: float = 0.0
    eta: float = ETA
    lyapunov_exponents: List[float] = field(default_factory=list)
    max_lyapunov: float = 0.0
    positive_exponent: bool = False
    dimension: int = 4
    integration_steps: int = 0
    converged: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass
class ChaosScanResult:
    """Full chaos search result."""
    results: List[LyapunovResult] = field(default_factory=list)
    any_chaos: bool = False
    chaos_points: List[Tuple[float, float]] = field(default_factory=list)
    max_lyapunov_found: float = 0.0
    total_tested: int = 0
    notes: List[str] = field(default_factory=list)


def ctp_coupled_system(r, y, lam, g_p, eta, tau):
    """The 4D CTP-doubled coupled system.

    State vector y = [Phi_plus, Phi_minus, f, f_prime]

    Equations:
      dPhi_+/dr = Phi_+'  (need second eq for spatial propagation)

    Actually, we need to be careful. The constitutive equation is in TIME,
    not in RADIUS. To get a 4D dynamical system in a single evolution
    variable, we must either:

    (A) Evolve in TIME with spatial profile held fixed (unrealistic)
    (B) Evolve in RADIUS treating it as the independent variable

    For the chaos search, we use approach (B): the "time" variable is r,
    and the system evolves spatially. This is the shooting method picture.

    For the CTP doubled scalar in the spatial domain, we promote the
    first-order temporal equation to a second-order spatial equation
    (from the field-theoretic completion in D8):

      Phi_+'' + (2/r)Phi_+' - (1/tau^2)Phi_+ + X(r)/tau^2 + g_p*eta^2*f^2*Phi_+ = 0
      Phi_-'' + (2/r)Phi_-' + (1/tau^2)Phi_- + g_p*eta^2*f^2*Phi_- = 0

    Combined with the hedgehog:
      f'' + (2/r)f' - (2/r^2)f - lam*eta^2*f*(f^2-1) + g_p*(Phi_+^2 + Phi_-^2)*f = 0

    This gives a 6D system: (Phi_+, Phi_+', Phi_-, Phi_-', f, f')
    """
    Phi_p, dPhi_p, Phi_m, dPhi_m, f_val, df = y

    r_safe = max(r, 1e-10)
    X_r = M_EXT / r_safe**2  # gravitational source

    # Phi_plus: D8 spatial equation with mass term -1/tau^2
    # (contracting mode: mass^2 = +1/tau^2 > 0, so Yukawa-screened)
    d2Phi_p = (-(2.0/r_safe)*dPhi_p
               + (1.0/tau**2)*Phi_p
               - X_r/tau**2
               - g_p*eta**2*f_val**2*Phi_p)

    # Phi_minus: CTP partner with REVERSED mass sign
    # (expanding mode: mass^2 = -1/tau^2 < 0, tachyonic)
    d2Phi_m = (-(2.0/r_safe)*dPhi_m
               - (1.0/tau**2)*Phi_m
               - g_p*eta**2*f_val**2*Phi_m)

    # Hedgehog f: standard + portal from BOTH Phi modes
    d2f = (-(2.0/r_safe)*df
           + (2.0/r_safe**2)*f_val
           + lam*eta**2*f_val*(f_val**2 - 1.0)
           - g_p*(Phi_p**2 + Phi_m**2)*f_val)

    return np.array([dPhi_p, d2Phi_p, dPhi_m, d2Phi_m, df, d2f])


def compute_lyapunov_exponents(
    lam: float,
    g_p: float,
    eta: float = ETA,
    tau: float = TAU,
    r_start: float = 0.5,
    r_end: float = 8.0,
    n_steps: int = 5000,
    n_dim: int = 6,
    Phi_m_init: float = 0.01,
) -> LyapunovResult:
    """Compute Lyapunov exponents of the 6D CTP-doubled coupled system.

    Uses the standard QR decomposition method:
    1. Evolve the state AND a set of n_dim tangent vectors
    2. Periodically QR-decompose the tangent matrix
    3. Accumulate log of diagonal elements of R
    4. Lyapunov exponents = accumulated sums / total integration length
    """
    dr = (r_end - r_start) / n_steps

    # Initial state
    delta_core = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
    r0 = r_start
    f0 = r0 / math.sqrt(r0**2 + delta_core**2)
    df0 = delta_core**2 / (r0**2 + delta_core**2)**1.5
    Phi_p0 = M_EXT / r0**2
    dPhi_p0 = -2.0 * M_EXT / r0**3
    Phi_m0 = Phi_m_init  # small nonzero seed for the expanding mode
    dPhi_m0 = 0.0

    y = np.array([Phi_p0, dPhi_p0, Phi_m0, dPhi_m0, f0, df0])

    # Tangent vectors (identity matrix initially)
    Q = np.eye(n_dim)

    # Accumulated log stretching
    lyap_sum = np.zeros(n_dim)
    total_r = 0.0

    # QR renormalization interval
    renorm_interval = 10
    step_count = 0

    def rhs(r, state):
        return ctp_coupled_system(r, state, lam, g_p, eta, tau)

    def jacobian(r, state):
        """Numerical Jacobian of the 6D system."""
        eps = 1e-7
        J = np.zeros((n_dim, n_dim))
        f0 = rhs(r, state)
        for j in range(n_dim):
            state_p = state.copy()
            state_p[j] += eps
            J[:, j] = (rhs(r, state_p) - f0) / eps
        return J

    r = r_start
    diverged = False

    for step in range(n_steps):
        # Check for divergence
        if np.any(np.abs(y) > 1e10):
            diverged = True
            break

        # RK4 step for state
        k1 = dr * rhs(r, y)
        k2 = dr * rhs(r + dr/2, y + k1/2)
        k3 = dr * rhs(r + dr/2, y + k2/2)
        k4 = dr * rhs(r + dr, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0

        # Evolve tangent vectors
        J = jacobian(r, y)
        Q = Q + dr * J @ Q  # linearized tangent evolution (Euler; adequate for Lyapunov)

        r += dr
        total_r += dr
        step_count += 1

        # QR renormalization
        if step_count % renorm_interval == 0:
            Q_new, R = np.linalg.qr(Q)
            for i in range(n_dim):
                if abs(R[i, i]) > 1e-30:
                    lyap_sum[i] += math.log(abs(R[i, i]))
            Q = Q_new

    # Final QR
    if not diverged and step_count > 0:
        Q_new, R = np.linalg.qr(Q)
        for i in range(n_dim):
            if abs(R[i, i]) > 1e-30:
                lyap_sum[i] += math.log(abs(R[i, i]))

    if total_r > 0:
        lyap_exponents = sorted(lyap_sum / total_r, reverse=True)
    else:
        lyap_exponents = [0.0] * n_dim

    max_le = lyap_exponents[0] if lyap_exponents else 0.0

    notes = [
        "lambda={:.1f}, g_p={:.2f}, eta={:.4f}".format(lam, g_p, eta),
        "Phi_m_init={:.4f}".format(Phi_m_init),
        "Steps: {}, total_r: {:.2f}".format(step_count, total_r),
        "Diverged: {}".format(diverged),
        "Lyapunov exponents: {}".format(
            ", ".join("{:.4f}".format(x) for x in lyap_exponents)),
        "Max LE: {:.6f}".format(max_le),
        "Positive exponent: {}".format(max_le > 0.01),
    ]

    return LyapunovResult(
        lam=lam, g_p=g_p, eta=eta,
        lyapunov_exponents=lyap_exponents,
        max_lyapunov=max_le,
        positive_exponent=(max_le > 0.01),
        dimension=n_dim,
        integration_steps=step_count,
        converged=(not diverged),
        notes=notes,
    )


def run_chaos_scan() -> ChaosScanResult:
    """Scan parameter space for chaos (positive Lyapunov exponents)."""

    # Parameters to scan
    lambdas = [0.1, 0.5, 1.0, 5.0, 10.0, 25.0, 50.0, 100.0, 500.0]
    g_ps = [0.0, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0]
    phi_m_inits = [0.001, 0.01, 0.1, 1.0]

    results = []
    chaos_points = []
    max_le_found = -float('inf')

    for lam in lambdas:
        for g_p in g_ps:
            for pm_init in phi_m_inits:
                try:
                    res = compute_lyapunov_exponents(
                        lam, g_p, Phi_m_init=pm_init,
                    )
                except Exception as exc:
                    res = LyapunovResult(
                        lam=lam, g_p=g_p,
                        notes=["Exception: {}".format(str(exc)[:80])],
                    )
                results.append(res)
                if res.max_lyapunov > max_le_found:
                    max_le_found = res.max_lyapunov
                if res.positive_exponent and res.converged:
                    chaos_points.append((lam, g_p))

    any_chaos = len(chaos_points) > 0

    notes = [
        "Total configurations tested: {}".format(len(results)),
        "Converged: {}".format(sum(1 for r in results if r.converged)),
        "Diverged: {}".format(sum(1 for r in results if not r.converged)),
        "Positive max LE (converged): {}".format(
            sum(1 for r in results if r.positive_exponent and r.converged)),
        "Max Lyapunov exponent found: {:.6f}".format(max_le_found),
        "ANY CHAOS: {}".format(any_chaos),
    ]
    if any_chaos:
        notes.append("CHAOS POINTS:")
        for p in set(chaos_points):
            notes.append("  lambda={}, g_p={}".format(*p))

    return ChaosScanResult(
        results=results,
        any_chaos=any_chaos,
        chaos_points=list(set(chaos_points)),
        max_lyapunov_found=max_le_found,
        total_tested=len(results),
        notes=notes,
    )


if __name__ == "__main__":
    print("=" * 75)
    print("  BOOK XXI DELTA — CTP-DOUBLED CHAOS SEARCH")
    print("  6D system: (Phi_+, Phi_+', Phi_-, Phi_-', f, f')")
    print("  Searching for positive Lyapunov exponents")
    print("=" * 75)

    scan = run_chaos_scan()

    print("\n--- Scan Summary ---")
    for n in scan.notes:
        print("  {}".format(n))

    # Detailed table
    print("\n--- Lyapunov Exponent Table (converged only) ---")
    header = "{:>6s} {:>6s} {:>8s} {:>10s} {:>10s} {:>10s} {:>8s}".format(
        "lam", "g_p", "Pm_init", "LE_max", "LE_2", "LE_min", "Chaos?")
    print(header)
    print("-" * 70)

    for r in scan.results:
        if r.converged and r.lyapunov_exponents:
            les = r.lyapunov_exponents
            # Find Phi_m_init from notes
            pm_init = "?"
            for n in r.notes:
                if "Phi_m_init" in n:
                    pm_init = n.split("=")[1]
                    break
            print("{:6.1f} {:6.2f} {:>8s} {:10.4f} {:10.4f} {:10.4f} {:>8s}".format(
                r.lam, r.g_p, pm_init,
                les[0], les[1] if len(les) > 1 else 0,
                les[-1] if les else 0,
                "YES" if r.positive_exponent else "no"))

    print("\n" + "=" * 75)
    if scan.any_chaos:
        print("  POSITIVE LYAPUNOV EXPONENT FOUND")
        print("  The CTP-doubled coupled system exhibits sensitive dependence")
        print("  on initial conditions at {} parameter point(s)".format(
            len(scan.chaos_points)))
        print("  This opens the SRB measure route to probability.")
    else:
        print("  NO POSITIVE LYAPUNOV EXPONENT FOUND (converged runs)")
        print("  Max LE: {:.6f}".format(scan.max_lyapunov_found))
        if scan.max_lyapunov_found > -0.1:
            print("  Note: max LE near zero suggests marginal stability,")
            print("  not strong contraction. Further investigation warranted.")
        else:
            print("  The 6D CTP-doubled system is non-chaotic in all tested regimes.")
    print("=" * 75)
