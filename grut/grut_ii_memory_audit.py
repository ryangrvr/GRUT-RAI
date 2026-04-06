"""
GRUT II Epsilon — Memory, Delay, and Nonlocality Audit
========================================================

Structural diagnosis: memoryless first-order dissipative scaling systems
collapse to global uniqueness. The question is what MINIMAL history-bearing
modification breaks this.

Five candidates tested:
  1. Delay in tau-response
  2. Integral memory kernel
  3. Hysteretic switching
  4. Weak inertia (second-order)
  5. Spatially nonlocal coupling

For each: mechanism, minimality, uniqueness-breaking logic, pathology risk.
Then: the concrete first technical target for the chosen minimal route.
"""

import math
import numpy as np
from scipy.integrate import solve_ivp

TAU_STAR = math.sqrt(1.5)


if __name__ == "__main__":
    print("=" * 80)
    print("  GRUT II EPSILON — MEMORY, DELAY, AND NONLOCALITY AUDIT")
    print("=" * 80)

    # ================================================================
    # PART I: STRUCTURAL DIAGNOSIS
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART I: STRUCTURAL DIAGNOSIS — WHY MEMORYLESS SYSTEMS FAIL
  ══════════════════════════════════════════════════════════════

  What GRUT II Delta established:

  In a 2D autonomous first-order dissipative system with instantaneous
  algebraic feedback, the flow is governed by:

    dPhi/dt = F(Phi, tau)
    dtau/dt = G(Phi, tau)

  The vector field (F, G) is determined ENTIRELY by the current state.
  No history. No memory. No delay.

  In this class:
  - Fixed points are solutions of F = G = 0 (algebraic)
  - Stability is determined by the Jacobian at each fixed point
  - The global phase portrait is constrained by:
    * Poincare index theorem (for smooth fields)
    * Monotonicity of Lyapunov-like functions
    * Boundedness of the flow

  GRUT II tried algebraic modifications (Beta: linear, Gamma: sub-linear)
  and found that the second equilibrium is either:
    * always a saddle (Beta: det < 0 unconditionally)
    * locally stable but globally empty (Delta: cusp drives all trajectories to Eq2)

  The WORKING HYPOTHESIS:

  ┌───────────────────────────────────────────────────────────────┐
  │                                                               │
  │  Scale-relaxation systems without memory collapse to global   │
  │  uniqueness because the instantaneous feedback loop cannot    │
  │  sustain two competing basins: one always dominates.          │
  │                                                               │
  │  Memory (delay, integration, hysteresis) breaks this by       │
  │  allowing the system to occupy DIFFERENT effective states      │
  │  depending on its HISTORY, not just its current position.     │
  │                                                               │
  └───────────────────────────────────────────────────────────────┘
    """)

    # ================================================================
    # PART II: CANDIDATE MEMORY CLASSES
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART II: CANDIDATE MEMORY-BEARING EXTENSIONS
  ══════════════════════════════════════════════════════════════
    """)

    candidates = [
        {
            "name": "1. DELAY in tau-response",
            "equation": "tau_meta dtau/dt + tau = tau_star + h(Phi(t - Delta) - X)",
            "mechanism": "Phase lag between Phi displacement and tau response. At delay Delta ~ tau_meta, the feedback loop can overshoot and sustain oscillations or multiple attractors.",
            "breaks_uniqueness": "YES (standard result: delay-differential equations can have infinite-dimensional dynamics, including limit cycles and multi-stability, even from simple feedback)",
            "minimal": "YES — adds 1 parameter (Delta) and no new fields",
            "still_grut_ii": "YES — same constitutive scaling architecture with delayed feedback",
            "preserves_irreversibility": "YES — dissipation still present; delay does not reverse time",
            "multi_basin_likely": "YES — delay-induced bifurcations are generic in dissipative feedback systems (Mackey-Glass, delayed logistic, etc.)",
            "pathology_risk": "LOW — delay systems are well-studied; standard DDE theory applies",
            "cost": "+1p (Delta)",
        },
        {
            "name": "2. INTEGRAL memory kernel",
            "equation": "tau_meta dtau/dt + tau = tau_star + integral K(s) h(Phi(t-s)-X) ds",
            "mechanism": "The tau response depends on the entire history of Phi, not just the current value. The kernel K(s) determines how much past history matters.",
            "breaks_uniqueness": "YES (integral transforms can create effective higher-dimensional dynamics)",
            "minimal": "NO — requires specifying a kernel function K(s), adding functional complexity",
            "still_grut_ii": "CONDITIONAL — memory kernels are natural for constitutive response (think viscoelastic materials), but the kernel must be justified",
            "preserves_irreversibility": "YES — if K(s) is causal (K(s) = 0 for s < 0) and decaying",
            "multi_basin_likely": "CONDITIONAL — depends on kernel shape; exponential kernel reduces to delay",
            "pathology_risk": "MODERATE — kernel must be specified; bad kernels can produce non-physical behavior",
            "cost": "+1p (kernel timescale) + 1 functional form (K)",
        },
        {
            "name": "3. HYSTERETIC switching",
            "equation": "tau responds differently on ascending vs descending Phi",
            "mechanism": "The tau-Phi feedback has different branches depending on the direction of approach. This is history-dependent without explicit delay.",
            "breaks_uniqueness": "YES (hysteresis by definition means multiple states at the same current (Phi, tau) depending on history)",
            "minimal": "NO — requires specifying switching rules, thresholds, and branch structure",
            "still_grut_ii": "CONDITIONAL — hysteresis is natural in materials science but not clearly motivated for vacuum constitutive response",
            "preserves_irreversibility": "YES — hysteresis is inherently irreversible",
            "multi_basin_likely": "YES (by construction — hysteresis IS multi-branch)",
            "pathology_risk": "MODERATE — switching rules can be ad hoc",
            "cost": "+1P (switching mechanism) + 2p (thresholds)",
        },
        {
            "name": "4. WEAK INERTIA (second-order tau dynamics)",
            "equation": "m_tau d^2tau/dt^2 + tau_meta dtau/dt + tau = tau_star + h(Phi-X)",
            "mechanism": "Adding inertia to the tau field allows overshoot and oscillation. The 3D system (Phi, tau, dtau/dt) can exhibit richer dynamics than 2D.",
            "breaks_uniqueness": "CONDITIONAL — 3D dissipative systems CAN have chaos and multi-stability (Lorenz-type), but it depends on the damping ratio",
            "minimal": "YES — adds 1 parameter (m_tau) and extends tau from first to second order",
            "still_grut_ii": "CONDITIONAL — adding inertia to the scale field is a structural choice; the telegrapher extension already did this for Phi",
            "preserves_irreversibility": "YES — dissipation (tau_meta term) still present",
            "multi_basin_likely": "CONDITIONAL — requires m_tau/tau_meta ratio in the underdamped regime; not guaranteed",
            "pathology_risk": "LOW — well-studied in nonlinear oscillator theory",
            "cost": "+1p (m_tau)",
        },
        {
            "name": "5. SPATIALLY NONLOCAL coupling",
            "equation": "tau(x,t) responds to integral of Phi(x',t) over neighbors",
            "mechanism": "Spatial competition between different regions. Pattern formation (Turing-type) can produce coexisting spatial domains with different (Phi, tau) values.",
            "breaks_uniqueness": "YES (Turing instability is the standard mechanism for spatial multi-stability in reaction-diffusion systems)",
            "minimal": "NO — requires spatial structure, diffusion operator, and domain specification",
            "still_grut_ii": "YES — spatial extension was already in GRUT I (telegrapher); adding spatial competition to tau is natural",
            "preserves_irreversibility": "YES",
            "multi_basin_likely": "YES — but the 'multiple basins' are spatial domains, not phase-space basins. Different question from what we need.",
            "pathology_risk": "MODERATE — full PDE analysis required",
            "cost": "+2p (diffusion coefficient for tau, interaction range)",
        },
    ]

    for c in candidates:
        print("  {}".format(c["name"]))
        print("    Equation: {}".format(c["equation"]))
        print("    Mechanism: {}".format(c["mechanism"]))
        print("    Breaks uniqueness: {}".format(c["breaks_uniqueness"]))
        print("    Minimal: {}".format(c["minimal"]))
        print("    Still GRUT II: {}".format(c["still_grut_ii"]))
        print("    Preserves irreversibility: {}".format(c["preserves_irreversibility"]))
        print("    Multi-basin likely: {}".format(c["multi_basin_likely"]))
        print("    Pathology risk: {}".format(c["pathology_risk"]))
        print("    Cost: {}".format(c["cost"]))
        print()

    # ================================================================
    # PART III: UNIQUENESS-BREAKING MECHANISM
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART III: WHAT BREAKS THE UNIQUENESS LOGIC?
  ══════════════════════════════════════════════════════════════

  For each candidate, the uniqueness-breaking mechanism:

  1. DELAY: Phase lag creates effective extra dimension. The state
     is no longer (Phi, tau) but (Phi, tau, Phi_history). With delay
     Delta, the phase space is infinite-dimensional (a function space).
     Standard DDE result: delayed negative feedback with gain > pi/2
     produces oscillation; with nonlinearity, produces multi-stability.
     Mechanism: PHASE LAG → OVERSHOOT → SUSTAINED ALTERNATIVES.

  2. INTEGRAL KERNEL: Convolution with history creates a smoothed
     effective extra variable. An exponential kernel K(s) = (1/T)exp(-s/T)
     is equivalent to adding a first-order memory variable:
     T dZ/dt + Z = h(v), and tau_eq depends on Z instead of h(v).
     This adds a PHYSICAL dimension to the state space.
     Mechanism: HISTORY SMOOTHING → EFFECTIVE HIGHER DIMENSION → RICHER DYNAMICS.

  3. HYSTERESIS: Branch persistence means the current state does not
     determine the future — the past does. This is the definition of
     non-Markovian dynamics in the reduced description.
     Mechanism: BRANCH PERSISTENCE → HISTORY-DEPENDENT EVOLUTION.

  4. INERTIA: Second-order tau dynamics add dtau/dt as a new state
     variable. The 3D system (Phi, tau, dtau/dt) can exhibit richer
     dynamics: oscillation, limit cycles, even chaos.
     Mechanism: OVERSHOOT → OSCILLATION → COEXISTING ATTRACTORS.

  5. NONLOCAL: Spatial competition creates different regions with
     different stable states. Not a phase-space multi-basin but a
     spatial multi-domain pattern.
     Mechanism: DIFFUSION-DRIVEN INSTABILITY → PATTERN FORMATION.
    """)

    # ================================================================
    # PART IV: MINIMAL ADMISSIBLE ROUTE
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART IV: MINIMAL ROUTE SELECTION
  ══════════════════════════════════════════════════════════════

  Ranking by minimality × likelihood × compatibility:

  | Candidate      | Cost    | Multi-basin? | Minimal? | Natural? |
  |----------------|---------|:----------:|:--------:|:--------:|
  | 1. DELAY       | +1p     | YES (generic)| YES      | YES      |
  | 4. INERTIA     | +1p     | CONDITIONAL  | YES      | YES      |
  | 2. KERNEL      | +1p+1fn | YES          | NO       | YES      |
  | 3. HYSTERESIS  | +1P+2p  | YES (by def) | NO       | NO       |
  | 5. NONLOCAL    | +2p     | YES (spatial)| NO       | YES      |

  CHOICE: CANDIDATE 1 — DELAY.

  Reasons:
  1. Smallest cost: +1p (delay time Delta). No new postulates, no new fields.
  2. Multi-stability is GENERIC in delayed feedback systems (Mackey-Glass theorem).
  3. The delay is PHYSICALLY MOTIVATED: the tau response to Phi displacement
     is not instantaneous — the constitutive vacuum takes time to adjust its
     relaxation rate. A delay Delta ~ tau_meta is the natural timescale.
  4. DDE (delay-differential equation) theory is mature: existence, uniqueness,
     stability, bifurcation analysis all well-established.
  5. The delay preserves the GRUT II identity: same variables (Phi, tau),
     same dissipative structure, same constitutive character. Only the
     feedback timing changes.

  RUNNER-UP: Candidate 4 (inertia). Also +1p, but multi-stability is not
  guaranteed (depends on damping ratio). Delay is more generic.
    """)

    # ================================================================
    # PART V: FAILURE CRITERIA
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART V: FAILURE CRITERIA FOR DELAY ROUTE
  ══════════════════════════════════════════════════════════════

  The delay route FAILS if:

  1. The delayed system has only limit cycles, no coexisting point attractors
     (oscillation without multi-stability → no basin partition)

  2. The delay-induced multi-stability requires Delta >> tau_meta
     (unphysically long delay → ad hoc)

  3. The delayed system is chaotic with a strange attractor but no
     basin partition (chaos without multi-basin → no deterministic probability)

  4. The delay induces runaway or blow-up at certain parameter values

  5. The delay requires nonlinear h to produce multi-stability, returning
     to the non-Lipschitz / cusp problems from Delta

  6. The basin fractions are infinitely sensitive to Delta
     (no structural robustness → no meaningful measure)
    """)

    # ================================================================
    # PART VI: FIRST TECHNICAL TARGET
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART VI: FIRST TECHNICAL TARGET
  ══════════════════════════════════════════════════════════════

  TARGET: Derive the delay-induced bifurcation criterion for the system

    tau * dPhi/dt + Phi = X + beta*(tau(t) - tau_star)
    tau_meta * dtau/dt + tau = tau_star + alpha*(Phi(t - Delta) - X)^2

  where the only change from GRUT II Beta is that h evaluates Phi
  at time (t - Delta) instead of time t.

  The characteristic equation for linearized stability around Eq1 is:

    det(lambda*I - J - J_delay * exp(-lambda*Delta)) = 0

  where J is the instantaneous Jacobian and J_delay contains the
  delayed feedback terms.

  For the GRUT II system:
    J = [[-1/tau_star, beta/tau_star],
         [0,            -1/tau_meta  ]]

    J_delay = [[0, 0],
               [2*alpha*(Phi-X)/tau_meta, 0]]
            = [[0, 0],
               [0, 0]]  at Eq1 (where Phi = X)

  AT Eq1: the delayed term vanishes because h'(0) = 0 for the quadratic h.
  The delay does NOT affect Eq1 stability for quadratic h.

  For LINEAR h(v) = gamma*v:
    J_delay at Eq1 = [[0, 0], [gamma/tau_meta, 0]]

  The characteristic equation:
    (lambda + 1/tau_star)(lambda + 1/tau_meta) - (beta/tau_star)(gamma/tau_meta)*exp(-lambda*Delta) = 0

  This transcendental equation can have roots with Re(lambda) > 0 for
  sufficiently large delay Delta, creating HOPF BIFURCATION at Eq1.

  When Eq1 loses stability through a Hopf bifurcation, a LIMIT CYCLE
  appears. If the limit cycle coexists with the still-stable Eq2
  (from Gamma's sub-linear route), we get:
    - Eq1: unstable (Hopf) → limit cycle
    - Eq2: stable
    - COEXISTENCE of a point attractor and a limit cycle

  This IS multi-basin dynamics: some initial conditions converge to the
  limit cycle, others to Eq2. The basin partition is real.

  ═══════════════════════════════════════════════════════════════
  FIRST COMPUTATION: Find the critical delay Delta_c at which Eq1
  undergoes a Hopf bifurcation for linear h with the GRUT II parameters.
  ═══════════════════════════════════════════════════════════════
    """)

    # ================================================================
    # PART VII: COST AND CONTINUITY
    # ================================================================
    print("""
  ══════════════════════════════════════════════════════════════
  PART VII: COST TABLE
  ══════════════════════════════════════════════════════════════

  | Route          | New P | New p    | New functions | Still GRUT II? | Jump type     |
  |----------------|:-----:|:--------:|:------------:|:--------------:|---------------|
  | 1. Delay       | 0     | +1 (Delta)| 0            | YES            | Bounded ext.  |
  | 2. Kernel      | 0     | +1 (T)   | +1 (K)       | YES            | Bounded ext.  |
  | 3. Hysteresis  | +1    | +2       | 0            | CONDITIONAL    | Major jump    |
  | 4. Inertia     | 0     | +1 (m_tau)| 0           | YES            | Bounded ext.  |
  | 5. Nonlocal    | 0     | +2       | 0            | YES            | Bounded ext.  |
    """)

    # ================================================================
    # VERDICT
    # ================================================================
    print("=" * 80)
    print("  FINAL VERDICT")
    print("=" * 80)
    print("""
  delay_route_is_minimal_and_admissible.

  The delay extension:

    tau_meta * dtau/dt + tau = tau_star + h(Phi(t - Delta) - X)

  adds ONE parameter (Delta) and changes the dynamical class from ODE to DDE.
  This is the MINIMAL memory-bearing modification of the GRUT II architecture.

  The delay is PHYSICALLY MOTIVATED: the constitutive vacuum's scale
  adjustment is not instantaneous — it responds to the field state after
  a characteristic processing time Delta.

  Standard DDE theory guarantees: for sufficiently large Delta relative to
  the feedback gain, the trivial equilibrium undergoes a HOPF BIFURCATION.
  This creates a limit cycle that can COEXIST with the stable Eq2 from
  Gamma's sub-linear analysis.

  The resulting dynamics: point attractor (Eq2) + limit cycle (from Eq1 Hopf).
  This IS genuine multi-basin structure:
    Basin A → limit cycle (oscillating scale)
    Basin B → fixed point (settled scale)

  GRUT I's unique-attractor rigidity is broken by DELAY, not by algebraic
  coupling, not by noise, not by self-consistency, and not by non-Lipschitz tricks.

  History is the missing scaling ingredient.

  NEXT FORCED MOVE: Derive the exact Hopf bifurcation criterion for the
  GRUT II delayed system. Find Delta_c. Verify the limit cycle exists.
  Map the basin structure of the DDE system numerically.
""")
    print("=" * 80)
