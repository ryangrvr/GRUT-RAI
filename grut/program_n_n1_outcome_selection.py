#!/usr/bin/env python3
"""
Program N - Stage N1: Unitary-Constitutive Coupled Dynamics

Starting from:
  1. Unitary quantum evolution of a system
  2. Constitutive coupling to a scalar field Phi
  3. NO imported Born rule, NO assumed tau = hbar/(kT), NO assumed noise floor

Test whether the coupled system dynamically produces:
  A. Branch instability (superposition becomes unstable)
  B. Single-outcome stabilization (one branch dominates)
  C. |psi|^2 statistics (over an ensemble of runs)

Model:
  Quantum system: 2-level (|0>, |1>) with Hamiltonian H_S
  Constitutive field: Phi with tau dPhi/dt + Phi = X
  Coupling: X depends on which quantum state is occupied
    X = X_0 if system in |0>, X = X_1 if system in |1>
  The coupling is BACK-REACTIVE: Phi shifts the quantum Hamiltonian.

The key: Phi is a CLASSICAL field (Sectors 1-2 of the CTP action).
The quantum system evolves unitarily UNTIL coupled to Phi.
The coupling creates entanglement between the quantum state and Phi.
Tracing over Phi produces decoherence. But does it produce SELECTION?
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

# ============================================================
# MODEL DEFINITION
# ============================================================

# Quantum system: 2-level
# |psi> = c0 |0> + c1 |1>
# H_S = E0 |0><0| + E1 |1><1|  (diagonal in measurement basis)
# With constitutive coupling:
# H_eff = H_S + lambda_c * Phi * sigma_z
# where sigma_z = |0><0| - |1><1|
# and lambda_c is the coupling strength

# Constitutive field:
# tau dPhi/dt + Phi = X(quantum state)
# X depends on the quantum state through the EXPECTATION VALUE:
# X = X_0 <0|rho|0> + X_1 <1|rho|1>
#   = X_0 |c0|^2 + X_1 |c1|^2
# This is the MEAN-FIELD coupling: Phi responds to the average
# quantum state, not to individual branches.

# ALTERNATIVE (stronger coupling):
# Phi responds to the FULL density matrix diagonal:
# But in the semiclassical limit, Phi IS a classical field
# that sees the expectation value.

# The density matrix evolves as:
# drho/dt = -i[H_eff, rho] + L[rho]  (if dissipation present)
# where the Phi-dependent Hamiltonian creates FEEDBACK:
# Phi depends on rho (through X = f(rho))
# rho depends on Phi (through H_eff = H_S + lambda_c Phi sigma_z)

# Parameters
E0 = 0.0      # energy of |0>
E1 = 1.0      # energy of |1> (units: 1/time)
lambda_c = 0.5  # constitutive coupling strength
X_0 = 1.0     # Phi target when system is in |0>
X_1 = -1.0    # Phi target when system is in |1>
tau = 1.0      # constitutive relaxation time (NOT assumed = hbar/kT)
D = 0.0        # noise coefficient (START with zero noise — pure dynamics)

# NO hbar in the constitutive sector. hbar enters ONLY through
# the quantum evolution: drho/dt = -i/hbar [H, rho].
# We set hbar = 1 (natural units for the quantum sector).
hbar = 1.0

# ============================================================
# EQUATIONS OF MOTION
# ============================================================

# State vector: (rho_00, rho_11, Re(rho_01), Im(rho_01), Phi)
# rho_00 + rho_11 = 1 (trace), so rho_11 = 1 - rho_00
# But keep both for clarity.

# The density matrix is:
# rho = [[rho_00, rho_01], [rho_01*, rho_11]]
# where rho_01 = Re(rho_01) + i Im(rho_01)

def coupled_eom(t, state, tau=tau, lambda_c=lambda_c, D=D, noise_realization=None):
    rho_00 = state[0]
    rho_11 = state[1]
    re_rho_01 = state[2]
    im_rho_01 = state[3]
    Phi = state[4]

    # Effective Hamiltonian
    # H_eff = diag(E0, E1) + lambda_c * Phi * diag(1, -1)
    # = diag(E0 + lambda_c*Phi, E1 - lambda_c*Phi)
    E_eff_0 = E0 + lambda_c * Phi
    E_eff_1 = E1 - lambda_c * Phi
    delta_E = E_eff_0 - E_eff_1  # energy splitting

    # Quantum evolution: drho/dt = -i/hbar [H_eff, rho]
    # [H, rho]_00 = H_00 rho_00 + H_01 rho_10 - rho_00 H_00 - rho_01 H_10
    #             = 0 (diagonal H, diagonal element)
    # So: drho_00/dt = -i/hbar * (H_00 - H_00) * rho_00 + ...
    # For diagonal H: [H, rho]_ij = (H_ii - H_jj) rho_ij
    # [H, rho]_00 = 0
    # [H, rho]_01 = (E_eff_0 - E_eff_1) rho_01 = delta_E * rho_01

    # d(rho_00)/dt = -i/hbar * [H,rho]_00 = 0 (unitary: populations don't change for diagonal H)
    # d(rho_01)/dt = -i/hbar * delta_E * rho_01

    # In terms of real and imaginary parts:
    # d(Re(rho_01))/dt = (delta_E / hbar) * Im(rho_01)
    # d(Im(rho_01))/dt = -(delta_E / hbar) * Re(rho_01)

    drho_00 = 0.0  # unitary evolution with diagonal H preserves populations
    drho_11 = 0.0
    d_re_rho_01 = (delta_E / hbar) * im_rho_01
    d_im_rho_01 = -(delta_E / hbar) * re_rho_01

    # Constitutive field evolution
    # X = X_0 * rho_00 + X_1 * rho_11 (mean-field coupling)
    X_current = X_0 * rho_00 + X_1 * rho_11
    dPhi = (X_current - Phi) / tau

    # Add noise if present
    if noise_realization is not None:
        # Find the noise value at this time
        idx = min(int(t / 0.001), len(noise_realization) - 1)
        dPhi += noise_realization[idx] / tau

    return [drho_00, drho_11, d_re_rho_01, d_im_rho_01, dPhi]

# ============================================================
# TEST A: BRANCH INSTABILITY
# ============================================================
print("=" * 90)
print("Program N — Stage N1: Unitary-Constitutive Coupled Dynamics")
print("=" * 90)

print(f"\nParameters:")
print(f"  E0 = {E0}, E1 = {E1}")
print(f"  lambda_c = {lambda_c} (coupling)")
print(f"  X_0 = {X_0}, X_1 = {X_1} (constitutive targets)")
print(f"  tau = {tau} (relaxation time)")
print(f"  D = {D} (noise — initially zero)")
print(f"  hbar = {hbar}")

print(f"\n{'='*90}")
print("TEST A: BRANCH INSTABILITY")
print("=" * 90)
print(f"\nQuestion: does the superposition become dynamically unstable")
print(f"when coupled to the constitutive field?")

# Initial state: equal superposition |psi> = (|0> + |1>)/sqrt(2)
# rho_00 = 0.5, rho_11 = 0.5, rho_01 = 0.5 (real, positive)
# Phi starts at 0 (no prior bias)

state0 = [0.5, 0.5, 0.5, 0.0, 0.0]  # equal superposition, Phi = 0
T_sim = 50.0

sol = solve_ivp(coupled_eom, (0, T_sim), state0,
                t_eval=np.linspace(0, T_sim, 5000), rtol=1e-12, atol=1e-14)

rho_00 = sol.y[0]
rho_11 = sol.y[1]
re_01 = sol.y[2]
im_01 = sol.y[3]
Phi = sol.y[4]
coherence = np.sqrt(re_01**2 + im_01**2)

print(f"\n  Initial: rho_00 = {rho_00[0]:.4f}, |rho_01| = {coherence[0]:.4f}, Phi = {Phi[0]:.4f}")
print(f"  Final:   rho_00 = {rho_00[-1]:.4f}, |rho_01| = {coherence[-1]:.4f}, Phi = {Phi[-1]:.4f}")
print(f"  Populations changed: {abs(rho_00[-1] - rho_00[0]) > 0.01}")
print(f"  Coherence changed: {abs(coherence[-1] - coherence[0]) > 0.01}")

# KEY CHECK: do the populations change?
# For a diagonal Hamiltonian with unitary evolution: drho_00/dt = 0.
# The populations are CONSTANTS OF MOTION under unitary evolution,
# regardless of the coupling to Phi.
# This is because H_eff is diagonal in the |0>, |1> basis.

pop_change = np.max(np.abs(rho_00 - rho_00[0]))
coh_change = np.max(np.abs(coherence - coherence[0]))

print(f"\n  Max population deviation: {pop_change:.6e}")
print(f"  Max coherence deviation: {coh_change:.6e}")

# What Phi does:
print(f"\n  Phi trajectory:")
print(f"    Phi(0) = {Phi[0]:.4f}")
print(f"    Phi(tau) = {Phi[int(len(Phi)*tau/T_sim)]:.4f}")
print(f"    Phi(5tau) = {Phi[int(len(Phi)*5*tau/T_sim)]:.4f}")
print(f"    Phi(final) = {Phi[-1]:.4f}")
print(f"    X_target = X_0*0.5 + X_1*0.5 = {X_0*0.5 + X_1*0.5:.4f}")

print(f"""
  RESULT A: NO BRANCH INSTABILITY (with diagonal H).

  The populations rho_00 and rho_11 are EXACTLY constant under
  unitary evolution with a diagonal Hamiltonian — even with
  constitutive coupling. The coupling modifies the ENERGY SPLITTING
  (through lambda_c * Phi * sigma_z) but not the populations.

  The coherence |rho_01| oscillates (phase precession from the
  Phi-dependent energy splitting) but does not DECAY in the
  absence of noise/dissipation.

  Phi relaxes to X_mean = X_0*rho_00 + X_1*rho_11 = {X_0*0.5 + X_1*0.5:.1f}
  (the mean-field average). It does not select a branch.

  DIAGNOSIS: Mean-field constitutive coupling CANNOT produce branch
  instability or outcome selection. The populations are protected
  by unitarity. Only the PHASE evolves (precession, not collapse).
""")

# ============================================================
# TEST A2: NON-DIAGONAL COUPLING (sigma_x type)
# ============================================================
print(f"{'='*90}")
print("TEST A2: NON-DIAGONAL COUPLING (transitions allowed)")
print("=" * 90)

# What if the coupling is NOT diagonal? If H_eff = H_S + lambda_c * Phi * sigma_x,
# the Phi-dependent term can induce TRANSITIONS between |0> and |1>.
# sigma_x = |0><1| + |1><0|

def coupled_eom_sigmax(t, state, tau=tau, lambda_c=lambda_c):
    rho_00, rho_11, re_01, im_01, Phi = state

    # H_eff = diag(E0, E1) + lambda_c * Phi * sigma_x
    # H_eff = [[E0, lambda_c*Phi], [lambda_c*Phi, E1]]

    # [H, rho] for non-diagonal H:
    # [H,rho]_00 = H_01 rho_10 - rho_01 H_10
    #            = lambda_c*Phi*(rho_01* - rho_01)
    #            = lambda_c*Phi*(-2i Im(rho_01))
    # d(rho_00)/dt = -i/hbar * [H,rho]_00 = -i/hbar * lambda_c*Phi*(-2i)*Im(rho_01)
    #             = -2*lambda_c*Phi*Im(rho_01)/hbar

    drho_00 = -2 * lambda_c * Phi * im_01 / hbar
    drho_11 = -drho_00  # trace preservation

    # [H,rho]_01 = (E0 - E1)*rho_01 + lambda_c*Phi*(rho_00 - rho_11)
    # d(rho_01)/dt = -i/hbar * [(E0-E1)*rho_01 + lambda_c*Phi*(rho_00-rho_11)]

    delta_E = E0 - E1
    pop_diff = rho_00 - rho_11

    d_re_01 = (delta_E * im_01 + lambda_c * Phi * 0) / hbar  # real part of -i*(...)
    # -i * [(E0-E1)(re+i*im) + lc*Phi*pop_diff]
    # = -i*(E0-E1)*re + (E0-E1)*im - i*lc*Phi*pop_diff
    # Real part: (E0-E1)*im = delta_E * im_01
    # Wait, let me be more careful.
    # d(rho_01)/dt = (-i/hbar) * [delta_E * rho_01 + lambda_c * Phi * pop_diff]
    # = (-i/hbar) * [delta_E * (re + i*im) + lambda_c * Phi * pop_diff]
    # = (-i/hbar) * [delta_E*re + lambda_c*Phi*pop_diff + i*delta_E*im]
    # = (1/hbar) * [delta_E*im + i*(-delta_E*re - lambda_c*Phi*pop_diff)]
    # Real: delta_E * im / hbar
    # Imag: (-delta_E * re - lambda_c * Phi * pop_diff) / hbar

    d_re_01 = delta_E * im_01 / hbar
    d_im_01 = (-delta_E * re_01 - lambda_c * Phi * pop_diff) / hbar

    # Constitutive field: X = X_0 rho_00 + X_1 rho_11
    X_current = X_0 * rho_00 + X_1 * rho_11
    dPhi = (X_current - Phi) / tau

    return [drho_00, drho_11, d_re_01, d_im_01, dPhi]

# Run with sigma_x coupling
state0_sx = [0.5, 0.5, 0.5, 0.0, 0.0]
sol_sx = solve_ivp(coupled_eom_sigmax, (0, T_sim), state0_sx,
                    t_eval=np.linspace(0, T_sim, 5000), rtol=1e-12, atol=1e-14)

rho_00_sx = sol_sx.y[0]
rho_11_sx = sol_sx.y[1]
coh_sx = np.sqrt(sol_sx.y[2]**2 + sol_sx.y[3]**2)
Phi_sx = sol_sx.y[4]

print(f"\n  Sigma_x coupling: H_eff = diag(E0,E1) + lambda_c * Phi * sigma_x")
print(f"  Initial: rho_00 = {rho_00_sx[0]:.4f}, |rho_01| = {coh_sx[0]:.4f}, Phi = {Phi_sx[0]:.4f}")
print(f"  Final:   rho_00 = {rho_00_sx[-1]:.4f}, |rho_01| = {coh_sx[-1]:.4f}, Phi = {Phi_sx[-1]:.4f}")

pop_range = np.max(rho_00_sx) - np.min(rho_00_sx)
print(f"\n  Population range: {np.min(rho_00_sx):.4f} to {np.max(rho_00_sx):.4f} (swing: {pop_range:.4f})")
print(f"  Coherence range: {np.min(coh_sx):.4f} to {np.max(coh_sx):.4f}")
print(f"  Phi range: {np.min(Phi_sx):.4f} to {np.max(Phi_sx):.4f}")

# Check: does the system settle into a definite state?
# Or does it oscillate forever?
# For a Hamiltonian system (unitary + constitutive with no dissipation):
# the total energy is conserved (or slowly exchanged with Phi).
# The system oscillates but does not settle.

print(f"""
  RESULT A2: OSCILLATION, NOT SELECTION.

  With sigma_x coupling, the populations DO change — the Phi-dependent
  coupling induces transitions between |0> and |1>. The populations
  oscillate with amplitude {pop_range:.4f}.

  BUT: the system does NOT settle into a definite state. It OSCILLATES
  forever (Hamiltonian dynamics is conservative). There is no damping
  of the population oscillation because the constitutive field provides
  a deterministic feedback, not a dissipative loss.

  For SELECTION: the oscillation must be DAMPED, i.e., the populations
  must approach a definite value. This requires DISSIPATION — which
  means noise (D > 0) in the constitutive sector.
""")

# ============================================================
# TEST B: WITH NOISE (stochastic constitutive field)
# ============================================================
print(f"{'='*90}")
print("TEST B: STOCHASTIC SELECTION (with noise)")
print("=" * 90)

# Now add noise to the constitutive field:
# tau dPhi/dt + Phi = X + xi(t)
# where <xi xi> = 2D delta(t-t')
#
# The noise breaks the conservative oscillation and can drive
# the system toward one branch or the other.
#
# CRITICAL: we do NOT set D = hbar/(2tau) or any other quantum value.
# D is a FREE PARAMETER (from the environmental bath, per A3).

# Run an ENSEMBLE of stochastic trajectories and collect statistics.

D_values = [0.01, 0.1, 0.5, 1.0]
N_ensemble = 500
dt_stoch = 0.01
N_steps = int(T_sim / dt_stoch)

# For each D, run N_ensemble trajectories and record the final state
# Use sigma_x coupling (which allows population changes)

print(f"\n  Ensemble size: {N_ensemble}")
print(f"  Integration: dt = {dt_stoch}, T = {T_sim}")

# Initial superposition: |psi> = c0 |0> + c1 |1>
# Try DIFFERENT initial amplitudes to test Born-rule emergence
initial_configs = [
    (np.sqrt(0.5), np.sqrt(0.5), "50/50"),
    (np.sqrt(0.3), np.sqrt(0.7), "30/70"),
    (np.sqrt(0.1), np.sqrt(0.9), "10/90"),
    (np.sqrt(0.8), np.sqrt(0.2), "80/20"),
]

for D_test in [0.1, 0.5]:
    print(f"\n  --- D = {D_test} ---")
    print(f"  {'Config':>10s} {'|c0|^2':>8s} {'|c1|^2':>8s} {'<rho00>_final':>14s} {'frac(0)':>10s} {'frac(1)':>10s} {'Born?':>8s}")
    print(f"  {'-'*10} {'-'*8} {'-'*8} {'-'*14} {'-'*10} {'-'*10} {'-'*8}")

    for c0_amp, c1_amp, label in initial_configs:
        # Initial density matrix
        rho00_init = c0_amp**2
        rho11_init = c1_amp**2
        re01_init = c0_amp * c1_amp  # real, positive for this choice
        im01_init = 0.0

        outcomes_0 = 0
        outcomes_1 = 0
        final_rho00_list = []

        for trial in range(N_ensemble):
            # Euler-Maruyama integration
            rho00 = rho00_init
            rho11 = rho11_init
            re01 = re01_init
            im01 = im01_init
            Phi_val = 0.0

            np.random.seed(trial * 1000 + int(D_test * 100))

            for step in range(N_steps):
                # Constitutive
                X_curr = X_0 * rho00 + X_1 * rho11
                dW = np.random.randn() * np.sqrt(dt_stoch)
                dPhi_val = ((X_curr - Phi_val) / tau) * dt_stoch + np.sqrt(2*D_test) / tau * dW

                # Quantum (sigma_x coupling)
                delta_E = E0 - E1
                pop_diff = rho00 - rho11

                drho00_val = (-2 * lambda_c * Phi_val * im01 / hbar) * dt_stoch
                d_re01_val = (delta_E * im01 / hbar) * dt_stoch
                d_im01_val = ((-delta_E * re01 - lambda_c * Phi_val * pop_diff) / hbar) * dt_stoch

                rho00 += drho00_val
                rho11 = 1.0 - rho00  # enforce trace
                re01 += d_re01_val
                im01 += d_im01_val
                Phi_val += dPhi_val

                # Enforce physicality (density matrix constraints)
                rho00 = np.clip(rho00, 0, 1)
                rho11 = 1.0 - rho00
                # Coherence bound: |rho01|^2 <= rho00 * rho11
                coh_max = np.sqrt(max(rho00 * rho11, 0))
                coh_curr = np.sqrt(re01**2 + im01**2)
                if coh_curr > coh_max and coh_curr > 0:
                    scale = coh_max / coh_curr
                    re01 *= scale
                    im01 *= scale

            final_rho00_list.append(rho00)
            if rho00 > 0.5:
                outcomes_0 += 1
            else:
                outcomes_1 += 1

        mean_rho00 = np.mean(final_rho00_list)
        frac_0 = outcomes_0 / N_ensemble
        frac_1 = outcomes_1 / N_ensemble

        # Born rule prediction: frac_0 should = |c0|^2
        born_match = abs(frac_0 - c0_amp**2) < 0.1

        print(f"  {label:>10s} {c0_amp**2:8.2f} {c1_amp**2:8.2f} {mean_rho00:14.4f} {frac_0:10.3f} {frac_1:10.3f} {'YES' if born_match else 'NO':>8s}")

# ============================================================
# TEST C: BORN RULE STATISTICS
# ============================================================
print(f"\n{'='*90}")
print("TEST C: BORN RULE STATISTICS (detailed)")
print("=" * 90)

# Scan over many initial |c0|^2 values and check if outcome
# fractions match |c0|^2

D_born = 0.5
N_ens_born = 1000

c0_sq_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print(f"\n  D = {D_born}, N_ensemble = {N_ens_born}")
print(f"\n  {'|c0|^2':>8s} {'frac(0)':>10s} {'delta':>10s} {'|delta|':>10s}")
print(f"  {'-'*8} {'-'*10} {'-'*10} {'-'*10}")

deltas = []
for c0_sq in c0_sq_values:
    c0_amp = np.sqrt(c0_sq)
    c1_amp = np.sqrt(1 - c0_sq)

    rho00_init = c0_sq
    rho11_init = 1 - c0_sq
    re01_init = c0_amp * c1_amp
    im01_init = 0.0

    outcomes_0 = 0
    for trial in range(N_ens_born):
        rho00 = rho00_init
        rho11 = rho11_init
        re01 = re01_init
        im01 = im01_init
        Phi_val = 0.0

        np.random.seed(trial * 7919 + int(c0_sq * 1000))

        for step in range(N_steps):
            X_curr = X_0 * rho00 + X_1 * rho11
            dW = np.random.randn() * np.sqrt(dt_stoch)
            dPhi_val = ((X_curr - Phi_val) / tau) * dt_stoch + np.sqrt(2*D_born) / tau * dW

            delta_E = E0 - E1
            pop_diff = rho00 - rho11

            drho00_val = (-2 * lambda_c * Phi_val * im01 / hbar) * dt_stoch
            d_re01_val = (delta_E * im01 / hbar) * dt_stoch
            d_im01_val = ((-delta_E * re01 - lambda_c * Phi_val * pop_diff) / hbar) * dt_stoch

            rho00 += drho00_val
            rho11 = 1.0 - rho00
            re01 += d_re01_val
            im01 += d_im01_val
            Phi_val += dPhi_val

            rho00 = np.clip(rho00, 0, 1)
            rho11 = 1.0 - rho00
            coh_max = np.sqrt(max(rho00 * rho11, 0))
            coh_curr = np.sqrt(re01**2 + im01**2)
            if coh_curr > coh_max and coh_curr > 0:
                scale = coh_max / coh_curr
                re01 *= scale
                im01 *= scale

        if rho00 > 0.5:
            outcomes_0 += 1

    frac_0 = outcomes_0 / N_ens_born
    delta = frac_0 - c0_sq
    deltas.append(delta)
    print(f"  {c0_sq:8.1f} {frac_0:10.3f} {delta:+10.3f} {abs(delta):10.3f}")

mean_abs_delta = np.mean(np.abs(deltas))
max_abs_delta = np.max(np.abs(deltas))
print(f"\n  Mean |delta|: {mean_abs_delta:.4f}")
print(f"  Max |delta|:  {max_abs_delta:.4f}")

if mean_abs_delta < 0.05:
    born_verdict = "BORN RULE EMERGES (mean deviation < 5%)"
elif mean_abs_delta < 0.15:
    born_verdict = "PARTIAL BORN RULE (mean deviation < 15%)"
else:
    born_verdict = "BORN RULE DOES NOT EMERGE (mean deviation > 15%)"

print(f"\n  VERDICT: {born_verdict}")

# ============================================================
# STRUCTURAL ANALYSIS
# ============================================================
print(f"\n{'='*90}")
print("STRUCTURAL ANALYSIS")
print("=" * 90)

print(f"""
  TEST A (diagonal coupling, no noise):
    Populations are CONSTANTS OF MOTION. Unitary evolution with
    diagonal Hamiltonian preserves populations exactly.
    Branch instability: NO.
    Selection: NO.

  TEST A2 (sigma_x coupling, no noise):
    Populations OSCILLATE (Phi-dependent transitions). But the
    system is conservative — no damping, no settling.
    Branch instability: YES (populations can change).
    Selection: NO (oscillation, not convergence).

  TEST B/C (sigma_x coupling, WITH noise):
    The constitutive noise breaks the oscillation symmetry.
    The noise-driven Phi kicks the populations stochastically.
    Whether this produces Born-rule statistics depends on
    the SPECIFIC coupling structure and noise amplitude.

  THE FUNDAMENTAL STRUCTURAL ISSUE:

  In the MEAN-FIELD coupling (X = X_0 rho_00 + X_1 rho_11):
  Phi sees the AVERAGE quantum state, not the individual branches.
  The constitutive field cannot "select" a branch because it
  never sees the branches individually — only their average.

  For genuine branch selection: Phi must couple to INDIVIDUAL
  branches (not the mean field). This requires going BEYOND
  the semiclassical/mean-field approximation — it requires
  the FULL quantum CTP path integral where Phi_+ and Phi_-
  on the two branches of the CTP contour are DIFFERENT.

  In the CTP formalism: the two branches are the + and - paths.
  Phi_+ couples to the |0> branch, Phi_- to the |1> branch.
  The DIFFERENCE (Phi_+ - Phi_-) = Phi_a (the quantum field)
  is what drives decoherence. But whether Phi_a dynamics
  produces SELECTION (not just decoherence) requires the
  FULL nonlinear CTP dynamics, not the mean-field approximation.

  This computation tested the MEAN-FIELD level. At this level:
  - Branch instability requires non-diagonal coupling (A2)
  - Selection requires noise (B)
  - Born-rule statistics depend on the coupling/noise details (C)

  The mean-field level CANNOT produce genuine branch selection
  because it averages over branches before the selection happens.
  This is a STRUCTURAL LIMITATION of the semiclassical treatment.
""")

print("=" * 90)
print("END OF COMPUTATION")
print("=" * 90)
