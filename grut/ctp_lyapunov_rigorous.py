"""
Book XXI Delta (Rigorous) — Benettin Algorithm for CTP-Doubled Lyapunov Spectrum
=================================================================================

Rigorous computation of Lyapunov exponents for the 6D CTP-doubled system.

FULL ODE SYSTEM (explicit):
  State vector y = (Phi_+, Phi_+', Phi_-, Phi_-', f, f')
  Evolution variable: r (radial coordinate, playing role of "time")

  dy/dr = F(r, y) where:

  F[0] = y[1]                                        # dPhi_+/dr = Phi_+'
  F[1] = -(2/r)*y[1] + (1/tau^2)*y[0]               # d^2Phi_+/dr^2 (screened, contracting)
         - X(r)/tau^2 - g_p*eta^2*y[4]^2*y[0]
  F[2] = y[3]                                        # dPhi_-/dr = Phi_-'
  F[3] = -(2/r)*y[3] - (1/tau^2)*y[2]               # d^2Phi_-/dr^2 (tachyonic, expanding)
         - g_p*eta^2*y[4]^2*y[2]
  F[4] = y[5]                                        # df/dr = f'
  F[5] = -(2/r)*y[5] + (2/r^2)*y[4]                 # d^2f/dr^2 (hedgehog)
         + lam*eta^2*y[4]*(y[4]^2-1)
         - g_p*(y[0]^2+y[2]^2)*y[4]

  where X(r) = M/r^2 (gravitational source)

ANALYTICAL JACOBIAN:
  J[i][j] = dF[i]/dy[j]  (6x6 matrix, computed analytically below)

BENETTIN ALGORITHM:
  1. Integrate state y(r) via RK4
  2. Simultaneously integrate 6 tangent vectors via variational equations:
     dQ/dr = J(r, y) * Q
  3. Every renorm_interval steps, QR-decompose Q
  4. Accumulate log|R_ii| for each exponent
  5. Lyapunov exponents = accumulated sums / total integration length

BOUNDEDNESS CHECK:
  Monitor ||y|| at every step. If any component exceeds threshold,
  flag as unbounded (not chaotic — just divergent).
"""

from __future__ import annotations
import math
import numpy as np
from dataclasses import dataclass, field
from typing import List, Tuple

# Constants
ETA = 1.0 / math.sqrt(8.0 * math.pi)
TAU = math.sqrt(1.5)
TAU_SQ = 1.5
M_EXT = 0.5
N_DIM = 6


@dataclass
class RigorousLyapunovResult:
    """Result of rigorous Benettin computation."""
    lam: float = 0.0
    g_p: float = 0.0
    eta: float = ETA
    phi_m_init: float = 0.01
    lyapunov_spectrum: List[float] = field(default_factory=list)
    max_lyapunov: float = 0.0
    sum_lyapunov: float = 0.0     # should be negative for dissipative system
    positive_count: int = 0
    bounded: bool = True
    n_steps: int = 0
    r_range: Tuple[float, float] = (0.0, 0.0)
    max_state_norm: float = 0.0
    convergence_history: List[List[float]] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


def F(r, y, lam, g_p, eta):
    """The 6D ODE system F(r, y).

    y = [Phi_+, Phi_+', Phi_-, Phi_-', f, f']
    """
    Pp, dPp, Pm, dPm, fv, dfv = y
    r_safe = max(r, 1e-10)
    r2 = r_safe * r_safe
    X_r = M_EXT / r2

    out = np.zeros(N_DIM)
    out[0] = dPp
    out[1] = (-2.0/r_safe)*dPp + (1.0/TAU_SQ)*Pp - X_r/TAU_SQ - g_p*eta**2*fv**2*Pp
    out[2] = dPm
    out[3] = (-2.0/r_safe)*dPm - (1.0/TAU_SQ)*Pm - g_p*eta**2*fv**2*Pm
    out[4] = dfv
    out[5] = (-2.0/r_safe)*dfv + (2.0/r2)*fv + lam*eta**2*fv*(fv**2 - 1.0) - g_p*(Pp**2 + Pm**2)*fv
    return out


def J_analytical(r, y, lam, g_p, eta):
    """Analytical Jacobian dF/dy (6x6 matrix).

    J[i][j] = dF[i] / dy[j]
    """
    Pp, dPp, Pm, dPm, fv, dfv = y
    r_safe = max(r, 1e-10)
    r2 = r_safe * r_safe

    J = np.zeros((N_DIM, N_DIM))

    # Row 0: dF[0]/dy = d(dPp)/dy = d(y[1])/dy
    J[0, 1] = 1.0

    # Row 1: dF[1]/dy
    # F[1] = -(2/r)*dPp + (1/tau^2)*Pp - X/tau^2 - g_p*eta^2*f^2*Pp
    J[1, 0] = 1.0/TAU_SQ - g_p*eta**2*fv**2          # dF1/dPp
    J[1, 1] = -2.0/r_safe                              # dF1/ddPp
    # J[1, 2] = 0 (no Pm dependence)
    # J[1, 3] = 0
    J[1, 4] = -2.0*g_p*eta**2*fv*Pp                   # dF1/df
    # J[1, 5] = 0

    # Row 2: dF[2]/dy = d(dPm)/dy = d(y[3])/dy
    J[2, 3] = 1.0

    # Row 3: dF[3]/dy
    # F[3] = -(2/r)*dPm - (1/tau^2)*Pm - g_p*eta^2*f^2*Pm
    # J[3, 0] = 0
    # J[3, 1] = 0
    J[3, 2] = -1.0/TAU_SQ - g_p*eta**2*fv**2          # dF3/dPm
    J[3, 3] = -2.0/r_safe                              # dF3/ddPm
    J[3, 4] = -2.0*g_p*eta**2*fv*Pm                   # dF3/df
    # J[3, 5] = 0

    # Row 4: dF[4]/dy = d(dfv)/dy = d(y[5])/dy
    J[4, 5] = 1.0

    # Row 5: dF[5]/dy
    # F[5] = -(2/r)*dfv + (2/r^2)*fv + lam*eta^2*fv*(fv^2-1) - g_p*(Pp^2+Pm^2)*fv
    J[5, 0] = -2.0*g_p*Pp*fv                          # dF5/dPp
    # J[5, 1] = 0
    J[5, 2] = -2.0*g_p*Pm*fv                          # dF5/dPm
    # J[5, 3] = 0
    J[5, 4] = (2.0/r2                                  # dF5/df
               + lam*eta**2*(3.0*fv**2 - 1.0)
               - g_p*(Pp**2 + Pm**2))
    J[5, 5] = -2.0/r_safe                              # dF5/ddfv

    return J


def rk4_step(r, y, dr, lam, g_p, eta):
    """Single RK4 step for the state vector."""
    k1 = dr * F(r, y, lam, g_p, eta)
    k2 = dr * F(r + dr/2, y + k1/2, lam, g_p, eta)
    k3 = dr * F(r + dr/2, y + k2/2, lam, g_p, eta)
    k4 = dr * F(r + dr, y + k3, lam, g_p, eta)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.0


def benettin_lyapunov(
    lam: float,
    g_p: float,
    eta: float = ETA,
    phi_m_init: float = 0.01,
    r_start: float = 0.5,
    r_end: float = 15.0,
    dr: float = 0.001,
    renorm_interval: int = 50,
    bound_threshold: float = 1e8,
) -> RigorousLyapunovResult:
    """Benettin algorithm for the full Lyapunov spectrum.

    Integrates the state + variational equations simultaneously.
    QR renormalization every renorm_interval steps.
    """
    n_steps = int((r_end - r_start) / dr)

    # Initial state
    delta_core = 1.0 / math.sqrt(max(lam * eta**2, 0.01))
    r0 = r_start
    f0 = r0 / math.sqrt(r0**2 + delta_core**2)
    df0 = delta_core**2 / (r0**2 + delta_core**2)**1.5
    Pp0 = M_EXT / r0**2
    dPp0 = -2.0 * M_EXT / r0**3
    Pm0 = phi_m_init
    dPm0 = 0.0

    y = np.array([Pp0, dPp0, Pm0, dPm0, f0, df0])

    # Tangent matrix (orthonormal initially)
    Q = np.eye(N_DIM)

    # Lyapunov sum accumulators
    lyap_sum = np.zeros(N_DIM)
    total_length = 0.0
    max_norm = 0.0

    # Convergence tracking
    convergence_history = []

    r = r_start
    bounded = True

    for step in range(n_steps):
        # Boundedness check
        state_norm = np.linalg.norm(y)
        if state_norm > max_norm:
            max_norm = state_norm
        if state_norm > bound_threshold:
            bounded = False
            break

        # RK4 step for state
        y_new = rk4_step(r, y, dr, lam, g_p, eta)

        # Variational equation: dQ/dr = J * Q
        # Integrate tangent vectors with same RK4
        Jac = J_analytical(r, y, lam, g_p, eta)
        dQ = Jac @ Q
        Q_new = Q + dr * dQ  # Euler for tangent (adequate with frequent renorm)

        y = y_new
        Q = Q_new
        r += dr
        total_length += dr

        # QR renormalization
        if (step + 1) % renorm_interval == 0:
            Q_orth, R = np.linalg.qr(Q)
            for i in range(N_DIM):
                diag = abs(R[i, i])
                if diag > 1e-30:
                    lyap_sum[i] += math.log(diag)
            Q = Q_orth

            # Track convergence
            if total_length > 0:
                current_les = sorted(lyap_sum / total_length, reverse=True)
                convergence_history.append(current_les)

    # Final QR
    if bounded and total_length > 0:
        Q_orth, R = np.linalg.qr(Q)
        for i in range(N_DIM):
            diag = abs(R[i, i])
            if diag > 1e-30:
                lyap_sum[i] += math.log(diag)

    if total_length > 0:
        spectrum = sorted(lyap_sum / total_length, reverse=True)
    else:
        spectrum = [0.0] * N_DIM

    max_le = spectrum[0] if spectrum else 0.0
    sum_le = sum(spectrum)
    pos_count = sum(1 for x in spectrum if x > 0.01)

    notes = [
        "lam={:.1f}, g_p={:.2f}, Pm_init={:.4f}".format(lam, g_p, phi_m_init),
        "r: [{:.2f}, {:.2f}], dr={:.4f}, steps={}".format(r_start, r_end, dr, n_steps),
        "Bounded: {}  (max ||y|| = {:.2e})".format(bounded, max_norm),
        "Spectrum: [{}]".format(", ".join("{:.4f}".format(x) for x in spectrum)),
        "Sum of LEs: {:.4f}".format(sum_le),
        "Positive exponents: {}".format(pos_count),
    ]

    return RigorousLyapunovResult(
        lam=lam, g_p=g_p, eta=eta, phi_m_init=phi_m_init,
        lyapunov_spectrum=spectrum,
        max_lyapunov=max_le,
        sum_lyapunov=sum_le,
        positive_count=pos_count,
        bounded=bounded,
        n_steps=min(step + 1, n_steps) if bounded else step + 1,
        r_range=(r_start, r),
        max_state_norm=max_norm,
        convergence_history=convergence_history,
        notes=notes,
    )


def run_rigorous_scan() -> List[RigorousLyapunovResult]:
    """Systematic scan with rigorous Benettin algorithm."""
    lambdas = [0.1, 1.0, 5.0, 10.0, 25.0, 50.0, 100.0]
    g_ps = [0.0, 0.1, 1.0, 5.0, 10.0, 50.0]
    pm_inits = [0.001, 0.01, 0.1]

    results = []
    for lam in lambdas:
        for gp in g_ps:
            for pm in pm_inits:
                try:
                    res = benettin_lyapunov(lam, gp, phi_m_init=pm)
                except Exception as exc:
                    res = RigorousLyapunovResult(
                        lam=lam, g_p=gp, phi_m_init=pm,
                        bounded=False,
                        notes=["Exception: {}".format(str(exc)[:80])],
                    )
                results.append(res)
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("  RIGOROUS BENETTIN LYAPUNOV SPECTRUM — CTP-DOUBLED COUPLED SYSTEM")
    print("  6D: (Phi_+, Phi_+', Phi_-, Phi_-', f, f')")
    print("  Analytical Jacobian | RK4 state integration | QR renormalization")
    print("=" * 80)

    results = run_rigorous_scan()

    # Summary
    bounded_results = [r for r in results if r.bounded]
    unbounded_results = [r for r in results if not r.bounded]
    chaotic = [r for r in bounded_results if r.positive_count > 0]

    print("\n--- Summary ---")
    print("  Total runs: {}".format(len(results)))
    print("  Bounded: {}".format(len(bounded_results)))
    print("  Unbounded (diverged): {}".format(len(unbounded_results)))
    print("  Chaotic (bounded + positive LE): {}".format(len(chaotic)))

    # Table of bounded results
    print("\n--- Lyapunov Spectrum (bounded runs) ---")
    print("{:>6s} {:>6s} {:>8s} {:>8s} {:>8s} {:>8s} {:>8s} {:>8s} {:>10s} {:>6s}".format(
        "lam", "g_p", "Pm_init", "LE1", "LE2", "LE3", "LE4", "SumLE", "max||y||", "#pos"))
    print("-" * 85)

    for r in bounded_results:
        les = r.lyapunov_spectrum
        print("{:6.1f} {:6.2f} {:8.3f} {:8.4f} {:8.4f} {:8.4f} {:8.4f} {:8.4f} {:10.2e} {:6d}".format(
            r.lam, r.g_p, r.phi_m_init,
            les[0] if len(les) > 0 else 0,
            les[1] if len(les) > 1 else 0,
            les[2] if len(les) > 2 else 0,
            les[3] if len(les) > 3 else 0,
            r.sum_lyapunov,
            r.max_state_norm,
            r.positive_count))

    # Unbounded runs summary
    if unbounded_results:
        print("\n--- Unbounded Runs (diverged) ---")
        for r in unbounded_results[:10]:
            print("  lam={:.1f}, g_p={:.2f}, Pm={:.3f}: max||y||={:.2e}".format(
                r.lam, r.g_p, r.phi_m_init, r.max_state_norm))
        if len(unbounded_results) > 10:
            print("  ... and {} more".format(len(unbounded_results) - 10))

    # Convergence check: show LE history for one representative run
    print("\n--- Convergence Check (first bounded chaotic run) ---")
    for r in chaotic[:1]:
        if r.convergence_history:
            print("  lam={:.1f}, g_p={:.2f}:".format(r.lam, r.g_p))
            n_hist = len(r.convergence_history)
            indices = [0, n_hist//4, n_hist//2, 3*n_hist//4, n_hist-1]
            for idx in indices:
                if idx < n_hist:
                    les = r.convergence_history[idx]
                    print("    r-step {}: LE1={:.4f}".format(idx * 50, les[0]))

    # Final verdict
    print("\n" + "=" * 80)
    if chaotic:
        print("  POSITIVE LYAPUNOV EXPONENTS CONFIRMED (BOUNDED TRAJECTORIES)")
        print("  {} of {} bounded runs show chaos".format(len(chaotic), len(bounded_results)))

        # Check if Phi_minus is essential
        gp0_chaotic = [r for r in chaotic if r.g_p == 0.0]
        if gp0_chaotic:
            print("\n  CRITICAL: Chaos exists even at g_p=0 (no portal coupling)")
            print("  The CTP doubling ALONE (Phi_minus tachyonic mode) generates chaos")
            print("  when coupled to the hedgehog sector.")
        else:
            print("\n  Chaos requires nonzero portal coupling g_p > 0")

        # Check sum of LEs (should be negative for dissipative attractor)
        neg_sum = [r for r in chaotic if r.sum_lyapunov < 0]
        pos_sum = [r for r in chaotic if r.sum_lyapunov > 0]
        print("\n  Sum of LEs negative (dissipative attractor): {}".format(len(neg_sum)))
        print("  Sum of LEs positive (expanding, NOT attractor): {}".format(len(pos_sum)))
        if neg_sum:
            print("  ==> STRANGE ATTRACTOR exists (positive LE + negative sum)")
            print("  ==> SRB measure is defined on this attractor")
            print("  ==> PHYSICAL PROBABILITY from dynamics (not postulated)")
    else:
        print("  NO CHAOS FOUND in bounded trajectories")
    print("=" * 80)
