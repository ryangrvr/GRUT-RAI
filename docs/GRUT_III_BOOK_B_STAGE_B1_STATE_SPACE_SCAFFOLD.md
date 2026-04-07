# GRUT III Book B — Stage B1: State-Space Inventory and Operator Scaffold

**Inherited:** BA1-BA7, X1-X10 (Book A). X[g_r] = X_0 + alpha R(g_r) (B0, provisional).

---

## 1. Formal State Tuple S_t

### Definition

At time t, the GRUT system state is the tuple:

```
S_t = (Phi_t, X_t, H_t, E_t)
```

where:

| Component | Symbol | Type | Definition | Status |
|-----------|--------|------|------------|:------:|
| **Constitutive field** | Phi_t | Scalar (real) | The current value of the constitutive field at time t. This is Phi_r in the CTP notation (the classical/mean-field value). | **DERIVED** from CTP backbone (BA2) |
| **Equilibrium target** | X_t | Scalar (real) | The current curvature-determined equilibrium: X_t = X_0 + alpha R(g_r(t)). Determined by the local geometry. | **ASSUMED** (B0 provisional interface) |
| **History functional** | H_t | Functional | The weighted history of past X values: H_t = integral_0^t K(t-s) X_s ds, where K is the retarded kernel. In the Markovian limit: H_t is not needed (the ODE is local in time). In the non-Markovian extension: H_t encodes memory. | **DERIVED** in Markovian limit (trivially: H_t = Phi_t). **OPEN** in non-Markovian extension. |
| **Environment state** | E_t | Parameter set | The environmental parameters at time t: (tau_t, D_t, T_t). These are EFT inputs from the traced-out environmental bath (L11, BA4). In the simplest case, they are constants. In general, they may vary slowly with the local geometry and matter content. | **ASSUMED** (A3: environmental bath provides these) |

### Dimensions

| Symbol | Dimensions | Typical scale |
|--------|-----------|---------------|
| Phi_t | [Phi] (dimensionless if Phi is normalized) | O(1) |
| X_t | [Phi] | O(1) at background; O(alpha × G rho) near matter |
| tau_t | [time] | Seconds to years (EFT input) |
| D_t | [Phi]^2 / [time] | k_B T tau / 2 (from FDT, BA5) |
| T_t | [temperature] | 4 K (lab) to 10^7 K (stellar) |

### Regime scope

| Component | Controlled | Caution | Unsafe |
|-----------|:----------:|:-------:|:------:|
| Phi_t | Linear regime, |Phi - X| << X_0 | Nonlinear regime (bistability) | Divergent Phi |
| X_t | Weak curvature, alpha R << X_0 | Moderate curvature | Strong curvature (X → ±∞ for Kretschner) |
| H_t | Markovian (H_t trivial) | Non-Markovian (memory corrections) | Highly non-Markovian (full kernel needed) |
| E_t | Slowly varying, thermal equilibrium | Rapidly changing environment | Out-of-equilibrium, non-Ohmic |

### Confidence: 0.70

(The state tuple is well-defined in the Markovian/linear/weak-field regime. The history functional H_t is trivial there. Extension to non-Markovian or nonlinear regimes requires additional structure.)

---

## 2. Irreversible Update Rule U_{Delta t}

### Definition

The update rule advances the state from S_t to S_{t + Delta t}:

```
U_{Delta t}: S_t → S_{t + Delta t}
```

### Explicit form (Markovian, linear, deterministic)

```
Phi_{t+dt} = Phi_t + (1/tau) (X_t - Phi_t) dt
X_{t+dt} = X_0 + alpha R(g_r(t + dt))     [determined by external geometry]
H_{t+dt} = H_t  [trivial in Markovian limit]
E_{t+dt} = E_t  [slowly varying assumption]
```

Equivalently in continuous form: tau dPhi/dt = X - Phi.

### Stochastic extension (with noise from Sector 2)

```
Phi_{t+dt} = Phi_t + (1/tau) (X_t - Phi_t) dt + sqrt(2D/tau^2) dW_t
```

where dW_t is a Wiener increment (Gaussian, <dW> = 0, <dW^2> = dt).

### Properties of U

| Property | Status | Evidence |
|----------|:------:|---------|
| **Irreversibility** | **DERIVED** | The update rule is dissipative: Phi → X monotonically (in the deterministic case). The Lyapunov function V = (Phi - X)^2 / 2 satisfies dV/dt = -(1/tau) V ≤ 0. Time-reversal symmetry is broken by the first-order structure. (GRUT-I theorem.) |
| **Contractivity** | **DERIVED** | The map is a contraction: |Phi_{t+dt} - X| = (1 - dt/tau) |Phi_t - X| for dt < tau. Contraction factor = exp(-dt/tau) over finite intervals. (Forward semigroup.) |
| **Unique fixed point** | **DERIVED** (linear regime) | Phi* = X is the unique attractor. Verified in Iota-Prime. Voided in nonlinear regime (GRUT-II Nu bistability). |
| **Positivity of density matrix** | **DERIVED** | The stochastic extension preserves non-negative probabilities via the CTP positivity condition Im S_eff ≥ 0 (BA1, A1-U3). |
| **Composability** | **DERIVED** | U_{dt1} ∘ U_{dt2} = U_{dt1 + dt2} (semigroup property). Follows from the linear ODE structure. Breaks for nonlinear extensions. |

### Regime scope

| Regime | U is valid | U breaks |
|--------|:----------:|:--------:|
| Markovian, linear, slowly-varying X | ✓ Full semigroup | — |
| Non-Markovian | U requires memory: Phi_{t+dt} depends on H_t, not just Phi_t | Semigroup property fails; update is non-Markovian |
| Nonlinear (cubic saturation) | U is modified: (X - Phi) → h(X - Phi) | Unique fixed point voided; bistability possible |
| Rapidly varying X (omega_X ~ 1/tau) | U may lag: Phi does not track X adiabatically | Transient errors of order tau × dX/dt |

### Confidence: 0.85

(Exact in the Markovian/linear regime. Well-understood modifications in extensions.)

---

## 3. Residue Functional R[history]

### Definition

The residue functional measures the accumulated deviation of the system from its equilibrium target over a history interval [0, t]:

```
R[{Phi_s, X_s}_{s=0}^t] = integral_0^t w(t-s) |Phi_s - X_s|^2 ds
```

where w(t-s) is a weighting kernel. Choices:

| Kernel | Form | Meaning |
|--------|------|---------|
| **Uniform** | w = 1 | Total integrated squared deviation. Simplest. |
| **Exponential** | w(t-s) = exp(-(t-s)/tau_R) / tau_R | Memory-weighted residue. Recent deviations count more. tau_R is the memory scale. |
| **Delta** | w(t-s) = delta(t-s) | Instantaneous residue: R = |Phi_t - X_t|^2. No history. |

### Role in the theory

R serves two functions:

1. **Lyapunov diagnostic.** For the deterministic constitutive law, R(instantaneous) = V = (Phi - X)^2 / 2 is the Lyapunov function. dV/dt ≤ 0 guarantees convergence. R measures "how far from equilibrium" the system is.

2. **Memory encoding.** In the non-Markovian extension, R with exponential kernel tracks the accumulated history of deviation, weighted by the memory timescale. This connects to the GRUT-I kernel reduction (Kappa): the kernel K_n(s) determines how past deviations contribute to the current dynamics.

### Properties

| Property | Status | Notes |
|----------|:------:|-------|
| R ≥ 0 | **DERIVED** | R is a sum of squared terms with positive weight. |
| R = 0 iff Phi_s = X_s for all s in [0,t] | **DERIVED** | The system has been in exact equilibrium throughout the interval. |
| dR/dt ≤ 0 for instantaneous R under deterministic U | **DERIVED** | Follows from the Lyapunov theorem. |
| R increases under stochastic noise | **DERIVED** | Noise kicks Phi away from X, increasing the instantaneous residue. In equilibrium, <R_inst> = D (the noise variance). |

### Regime scope

| Regime | R is well-defined | Notes |
|--------|:-----------------:|-------|
| Markovian, linear | ✓ | R_inst = (Phi - X)^2 / 2 is the Lyapunov function. |
| Non-Markovian | ✓ | R with exponential kernel is well-defined. The kernel tau_R should match the bath memory time. |
| Nonlinear (bistability) | ✓ but interpretation changes | R may have two local minima (one per attractor). R = 0 is no longer the unique equilibrium. |
| Stochastic | ✓ | <R> reaches the equilibrium fluctuation level D = k_B T tau / 2. |

### Confidence: 0.80

(Well-defined mathematically. The connection to the CTP action is structural but not unique — R is a diagnostic, not a term in the action.)

---

## 4. Admissibility Functional A[path]

### Definition

The admissibility functional evaluates whether a given path {S_s}_{s=0}^t is physically allowed under the GRUT constitutive framework:

```
A[{S_s}] = {
  1   if the path satisfies all admissibility conditions
  0   if any condition is violated
}
```

### Admissibility conditions

| # | Condition | Statement | Source | Regime |
|---|-----------|-----------|--------|--------|
| **A1** | Constitutive equation satisfied | tau dPhi/dt + Phi = X + xi(t), where xi is the noise with correct statistics | BA2, L2, L3 | Markovian, overdamped, linear |
| **A2** | Lyapunov non-increase (deterministic) | d[(Phi-X)^2/2]/dt ≤ 0 in the absence of noise | GRUT-I Lyapunov theorem | Deterministic, linear |
| **A3** | FDT consistency | The noise variance matches D = k_B T tau / 2 (CTP convention) in thermal equilibrium | BA5, L5 | Ohmic, high-T, equilibrium |
| **A4** | Regime validity | The path remains within the controlled domain: weak curvature (alpha R << X_0), Markovian (omega << omega_D), linear (|Phi - X| << X_0) | Book A domain map | All |
| **A5** | Positivity | If the path represents a density matrix evolution, Im S_eff ≥ 0 along the path | A1-U3, BA1 | All CTP paths |
| **A6** | Causality | Phi_t depends only on {X_s, Phi_s}_{s ≤ t}, not on future values | Retarded kernel structure | All |
| **A7** | USL regime validity (if quantum sector active) | Superposition separation l > 2R for point-mass USL; else use Diosi integral | Kappa-Prime, L10 | Quantum sector |

### Interpretation

A = 1 means the path is a legitimate trajectory of the GRUT EFT. A = 0 means the path violates the constitutive law, the domain of validity, or a structural constraint. Paths with A = 0 are not predictions of the theory — they are either errors or signals that the EFT has been pushed outside its regime.

### Confidence: 0.75

(The conditions are well-defined and individually derived/assumed with known status. The admissibility functional as a whole is a CONSTRUCTION of this stage, not a derived object from the CTP action. Its role is diagnostic/organizational.)

---

## 5. Three Toy Trajectories

All trajectories use the Markovian, linear, weak-field regime with:
- tau = 1 s, X_0 = 1.0, alpha = 0 (flat space, constant X)
- D = 0.01 (some noise for the stochastic case)

### Trajectory 1: ADMISSIBLE (deterministic relaxation)

```
Initial: Phi_0 = 0.0, X = 1.0
Evolution: Phi(t) = 1.0 - exp(-t)
```

| Condition | Check |
|-----------|:-----:|
| A1 (constitutive eq) | ✓ dPhi/dt + Phi = X = 1.0 |
| A2 (Lyapunov) | ✓ V(t) = exp(-2t)/2, monotonically decreasing |
| A3 (FDT) | N/A (deterministic) |
| A4 (regime) | ✓ Phi remains in [0, 1], all within controlled domain |
| A5 (positivity) | ✓ (deterministic, trivially positive) |
| A6 (causality) | ✓ (local ODE) |

**Verdict: A = 1. Admissible.**

### Trajectory 2: INADMISSIBLE (anti-relaxation)

```
Initial: Phi_0 = 0.5, X = 1.0
Evolution: Phi(t) = 1.0 + 0.5 exp(+t)   [Phi moves AWAY from X]
```

| Condition | Check |
|-----------|:-----:|
| A1 (constitutive eq) | ✗ dPhi/dt = 0.5 exp(t), but X - Phi = -0.5 exp(t). So tau dPhi/dt + Phi = 0.5 exp(t) + 1.0 + 0.5 exp(t) = 1.0 + exp(t) ≠ X = 1.0 |
| A2 (Lyapunov) | ✗ V(t) = 0.5 exp(2t)/4, INCREASING |

**Verdict: A = 0. Inadmissible.** The path violates the constitutive law and the Lyapunov condition. It represents anti-dissipation (entropy decrease) — thermodynamically forbidden in the deterministic sector.

### Trajectory 3: BOUNDARY CASE (regime exit)

```
Initial: Phi_0 = 0.0, X(t) = 1.0 + 100 sin(omega_fast t)  with omega_fast = 10/tau
Evolution: Phi(t) ≈ 1.0 + 100 sin(omega_fast t) / (1 + i omega_fast tau)  [tracking with lag]
```

| Condition | Check |
|-----------|:-----:|
| A1 (constitutive eq) | ✓ (the ODE is still satisfied if we solve it exactly) |
| A2 (Lyapunov) | Ambiguous: V oscillates because X oscillates. The instantaneous V is not monotonically decreasing. But the time-averaged V approaches the steady-state amplitude. |
| A4 (regime) | ✗ omega_fast = 10/tau. If omega_fast > omega_D (the bath cutoff), the Markovian assumption fails. The ODE is still well-posed but the CTP derivation that justifies it may not apply. |

**Verdict: A = BOUNDARY.** The constitutive equation is satisfied (it's a linear ODE, always solvable). But the regime condition A4 may be violated if the driving frequency exceeds the Markovian cutoff. The path is admissible as a mathematical solution of the ODE, but its physical interpretation as a CTP prediction is questionable above omega_D. The correct treatment would require the non-Markovian extension with the full retarded kernel.

---

## Summary Tables

### State Tuple

| Component | Symbol | Role | Status | Confidence |
|-----------|--------|------|:------:|:----------:|
| Constitutive field | Phi_t | Current field value | DERIVED (BA2) | 0.90 |
| Equilibrium target | X_t | Curvature-determined target | ASSUMED (B0) | 0.50 |
| History functional | H_t | Memory of past X-Phi deviations | DERIVED (Markov: trivial) / OPEN (non-Markov) | 0.70 |
| Environment state | E_t = (tau, D, T) | Bath parameters | ASSUMED (A3, BA4) | 0.60 |

### Operator Properties

| Property | Status | Regime |
|----------|:------:|--------|
| Irreversibility | DERIVED | All (first-order structure) |
| Contractivity | DERIVED | Linear, Markovian |
| Unique fixed point | DERIVED | Linear only (voided if nonlinear) |
| Semigroup | DERIVED | Markovian only |
| Positivity | DERIVED | CTP construction |

### Residue Properties

| Property | Status |
|----------|:------:|
| Non-negative | DERIVED |
| Zero iff equilibrium | DERIVED |
| Monotone decrease (det.) | DERIVED |
| Equilibrium fluctuation level | DERIVED (= D) |

### Admissibility Conditions

| # | Condition | Confidence |
|---|-----------|:----------:|
| A1 | Constitutive equation | 0.90 |
| A2 | Lyapunov non-increase | 0.85 |
| A3 | FDT consistency | 0.80 |
| A4 | Regime validity | 0.75 |
| A5 | Positivity | 0.90 |
| A6 | Causality | 0.95 |
| A7 | USL regime (l > 2R) | 0.98 |

---

## Gate Status

### B0 Gates (Source Coupling)

| Gate | Status | Notes |
|------|:------:|-------|
| X[g] candidate specified | **PASS** | X = X_0 + alpha R. Provisional. |
| Regime tagged | **PASS** | Weak field: controlled. Vacuum-blind: flagged. |
| Book A consistency | **PASS** | BA1-BA7 respected. X1-X10 not violated. |

### B1 Gates

| Gate | Status | Notes |
|------|:------:|-------|
| State tuple S_t defined | **PASS** | (Phi_t, X_t, H_t, E_t) with regime tags. |
| Update rule U specified | **PASS** | Deterministic + stochastic forms. Properties derived. |
| Residue functional R defined | **PASS** | Three kernel choices. Properties derived. |
| Admissibility functional A defined | **PASS** | Seven conditions. Three toy trajectories tested. |
| Toy trajectories | **PASS** | Admissible / inadmissible / boundary — all classified correctly. |

---

## Conflict Log

### CN-B1-1: Unique attractor vs bistability

The update rule U has "unique fixed point" as a DERIVED property (in the linear regime). But GRUT-II Nu demonstrated bistability under cubic saturation. The admissibility functional A does not currently handle bistable dynamics — it assumes a single equilibrium in condition A2.

**Resolution:** A2 is restricted to the linear regime. In the nonlinear extension, A2 must be replaced with a basin-of-attraction condition: the path must converge to ONE of the stable fixed points, not necessarily to Phi* = X. This is flagged for Book B Stage B2 (nonlinear extension), not resolved here.

**Status:** OPEN (flagged, not harmonized).

### CN-B1-2: History functional H_t is trivial in Markovian limit

In the Markovian regime, H_t carries no information beyond Phi_t (since Phi_t is the integral of the exponential kernel over past X). The history functional is structurally present but functionally redundant. In the non-Markovian extension, H_t becomes nontrivial and essential.

**Resolution:** H_t is retained in the state tuple as a placeholder for the non-Markovian extension. In the Markovian controlled domain, it can be set to H_t = Phi_t without loss.

**Status:** RESOLVED (by explicit declaration of Markovian simplification).

---

*GRUT III Book B Stages B0-B1 complete. B0: X[g_r] = X_0 + alpha R provisionally adopted (confidence 0.50, vacuum-blind flagged). B1: State tuple S_t = (Phi_t, X_t, H_t, E_t) defined. Update rule U specified with five derived properties. Residue functional R defined with three kernel choices. Admissibility functional A defined with seven conditions. Three toy trajectories classified. Two conflicts logged (bistability, trivial H_t). All B0 and B1 gates pass.*
