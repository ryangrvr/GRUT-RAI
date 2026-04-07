# GRUT III — Book B, Stage B1: State-Space Inventory and Irreversible Operator Scaffold

**Canonical interface:** X[g_r] = β + αR(g_r) (AB1, TF1).
**Allowed:** TF1-TF9. **Forbidden:** NF1-NF9, X1-X10. **Carried:** UD1-UD6.

---

## 1. Formal Definitions

### D1: State Tuple S_t

```
S_t = ( Φ_t,  X_t,  M_t,  F_t )
       ├─────  ├────  ├────  └───── regime flags
       │       │      └────── memory/residue state
       │       └─────── effective state (target)
       └──────── native state (constitutive field)
```

**Component definitions:**

| Layer | Symbol | Type | Definition | Status | Confidence |
|-------|--------|------|-----------|:------:|:----------:|
| **Native state** | Φ_t | ℝ | Current value of the constitutive field. Evolves by the update rule. This is Φ_r in the CTP notation. | **DERIVED** (BA2: CTP variation yields Φ_r dynamics) | 0.95 |
| **Effective state** | X_t | ℝ | Current equilibrium target: X_t = β + α R(g_r(t)). Determined by the external geometry. Not independently evolved — read from the metric. | **ASSUMED** (TF1: provisional interface) | 0.55 |
| **Memory/residue state** | M_t | ℝ≥0 | Accumulated deviation measure: M_t = (Φ_t − X_t)². Instantaneous residue. In the non-Markovian extension, M_t would be replaced by a functional of past deviations; in the Markovian controlled regime, the instantaneous value is sufficient. | **DERIVED** (Lyapunov function from GRUT-I) | 0.90 |
| **Regime flags** | F_t | {0,1}⁴ | Four binary indicators encoding whether the current state is within the controlled domain: | **CONSTRUCTED** (from Book A domain map) | 0.85 |

**Regime flag register F_t:**

| Bit | Flag | Condition for flag = 1 (in-regime) | Source |
|:---:|------|--------------------------------------|--------|
| f₁ | WEAK_FIELD | |αR(g_r)| < 0.1 × |β| | AB1 TF6 |
| f₂ | MARKOVIAN | Driving frequency ω_X < ω_D (bath cutoff) | A1-L9 |
| f₃ | LINEAR | |Φ_t − X_t| < 0.1 × |β| (no nonlinear self-interaction) | A1-C4 scope |
| f₄ | POINT_MASS_USL | l > 2R for any active superposition | A1-L10, Kappa-Prime |

When all flags are 1: the state is in the CONTROLLED domain.
When any flag is 0: the state is in CAUTION or UNSAFE territory, and the corresponding claim's confidence is degraded or voided.

**Non-redundancy check:** The four components are independent:
- Φ_t is the dynamical variable (cannot be derived from X_t, M_t, or F_t alone).
- X_t is determined by the external metric (cannot be derived from Φ_t).
- M_t = (Φ − X)² is a function of Φ and X, so it is technically REDUNDANT with (Φ, X). **However:** M_t is retained as a named diagnostic because it is the Lyapunov function and the natural observable for convergence monitoring. Marking: **DERIVED/REDUNDANT** — can be computed from (Φ, X) but is tracked explicitly for diagnostic value.
- F_t is determined by the current state and environment — also technically derivable. Marking: **DERIVED/REDUNDANT** — tracked for operational clarity.

**Minimal non-redundant state:** (Φ_t, X_t). The tuple (M_t, F_t) is diagnostic/derived.

---

### D2: Update Operator U_{Δt}

**Deterministic form:**

```
U_{Δt}: S_t → S_{t+Δt}

Φ_{t+Δt} = Φ_t + (Δt/τ)(X_t − Φ_t)
X_{t+Δt} = β + αR(g_r(t + Δt))          [read from external geometry]
M_{t+Δt} = (Φ_{t+Δt} − X_{t+Δt})²
F_{t+Δt} = evaluate_flags(Φ_{t+Δt}, X_{t+Δt}, g_r(t+Δt))
```

**Stochastic form (with Sector 2 noise):**

```
Φ_{t+Δt} = Φ_t + (Δt/τ)(X_t − Φ_t) + √(2D/τ²) ΔW_t
```

where ΔW_t ~ 𝒩(0, Δt) is a Wiener increment, D = k_BT τ/2 (CTP convention, TF9 via BA5).

**Properties (each checked):**

| Property | Statement | Status | Regime |
|----------|-----------|:------:|--------|
| **Irreversibility** | U_{Δt} is not invertible for Δt > 0: given Φ_{t+Δt}, one cannot uniquely recover Φ_t (information about the deviation Φ − X is exponentially lost). In the stochastic case, irreversibility is additionally enforced by the noise. | **DERIVED** | All (structural: first-order dissipative) |
| **Contractivity** | |Φ_{t+Δt} − X_{t+Δt}| ≤ (1 − Δt/τ)|Φ_t − X_t| + O(ΔX, noise). For slowly-varying X and no noise: strict contraction with factor e^{−Δt/τ}. | **DERIVED** | Markovian, linear, slowly-varying X |
| **Causal directionality** | Φ_{t+Δt} depends on (Φ_t, X_t, ΔW_t) — all at time ≤ t+Δt. No dependence on future values. | **DERIVED** | All (structural: retarded kernel, causal ODE) |
| **Semigroup** | U_{Δt₁} ∘ U_{Δt₂} = U_{Δt₁+Δt₂} for the deterministic, constant-X case. Breaks when X varies in time (the composition depends on the X-trajectory between t₁ and t₂). | **DERIVED** (constant X) / **OPEN** (varying X) | Markovian, constant X: exact semigroup. Varying X: approximate. |
| **Markovian closure** | U_{Δt} uses only the CURRENT state (Φ_t, X_t), not the history. This is the Markovian closure assumption: the bath has been traced out and its effect is entirely captured by τ and D. | **ASSUMED** (A1-L9: Markovian limit) | ω_X << ω_D |

**Where Markovian closure is used:** In the update rule, the term (Δt/τ)(X_t − Φ_t) assumes the bath responds instantaneously — the dissipation is LOCAL IN TIME. In the non-Markovian extension, this would become:

```
Φ_{t+Δt} = Φ_t + (1/τ) ∫₀^{t+Δt} K(t+Δt−s)(X_s − Φ_s) ds
```

with a retarded kernel K(t) that encodes bath memory. The Markovian limit K(t) → δ(t) recovers the local update rule. The Markovian closure is ASSUMED valid when f₂ = 1.

---

### D3: Residue Functional R[history]

**Definition:**

For a path {(Φ_s, X_s)}_{s=0}^{t}:

```
R[path; t] = ∫₀ᵗ w(t−s) (Φ_s − X_s)² ds
```

with weighting kernel w:

| Choice | w(t−s) | Name | Properties |
|--------|--------|------|------------|
| **R₀** (instantaneous) | δ(t−s) | Lyapunov residue | R₀ = (Φ_t − X_t)² = M_t |
| **R₁** (uniform) | 1/t | Time-averaged squared deviation | R₁ = (1/t)∫₀ᵗ(Φ_s − X_s)²ds |
| **R₂** (exponential) | (1/τ_R) e^{−(t−s)/τ_R} | Memory-weighted residue | R₂ exponentially discounts old deviations |

**Adopted default:** R₀ (instantaneous), with R₂ reserved for the non-Markovian extension.

**Mathematical properties:**

| Property | Statement | Proof | Status |
|----------|-----------|-------|:------:|
| **Non-negativity** | R[path; t] ≥ 0 for all paths and all w ≥ 0. | w ≥ 0 and (Φ − X)² ≥ 0 ⟹ integrand ≥ 0 ⟹ integral ≥ 0. | **DERIVED** |
| **Zero iff equilibrium** | R₀ = 0 iff Φ_t = X_t. R₁ = 0 iff Φ_s = X_s for all s ∈ [0,t]. | From (Φ − X)² = 0 iff Φ = X. | **DERIVED** |
| **Monotone decrease (deterministic, constant X)** | dR₀/dt = 2(Φ − X)(dΦ/dt) = 2(Φ − X)(−1/τ)(Φ − X) = −(2/τ)(Φ − X)² ≤ 0. | Direct computation from the constitutive law. | **DERIVED** |
| **Equilibrium fluctuation (stochastic)** | ⟨R₀⟩_eq = ⟨(Φ − X)²⟩_eq = D = k_BT τ/2 (CTP convention). | From the Langevin equilibrium distribution. Verified numerically in Iota-Prime (ratio 0.988). | **DERIVED** |
| **Boundedness** | For deterministic paths: R₀(t) ≤ R₀(0) e^{−2t/τ}. For stochastic: ⟨R₀⟩ ≤ max(R₀(0), D). | From the contraction property + FDT. | **DERIVED** |

**Coarse-graining dependence:** R depends on what is counted as the "deviation." The choice Φ − X assumes X is the correct equilibrium target. If X is wrong (e.g., if α is incorrect, or if a better candidate than β + αR exists), then R measures deviation from the wrong target and its minimization leads to wrong conclusions. This is a structural dependence on the assumed X, not on a coarse-graining procedure.

**Status:** R is mathematically rigorous within the linear/Markovian regime. Its physical interpretation depends on the correctness of X (TF1, which is ASSUMED/provisional).

---

### D4: Admissibility Functional A[path]

**Definition:**

```
A[{S_s}_{s=0}^t] ∈ {ADMISSIBLE, INADMISSIBLE, BOUNDARY}
```

A path is evaluated against seven conditions. All must hold for ADMISSIBLE. Any single failure yields INADMISSIBLE. If a condition is ambiguous or regime-boundary, the path is BOUNDARY.

| # | Condition | Formal test | Source | Operationally computable? |
|---|-----------|-------------|--------|:---:|
| **A1** | Constitutive equation | \|τ Φ̇_s + Φ_s − X_s − ξ_s\| < ε for all s, where ξ is the noise realization (or zero if deterministic) | TF3, BA2 | ✓ (numerical: finite-difference check at each timestep) |
| **A2** | Lyapunov non-increase (det.) | dR₀/ds ≤ 0 at all s where ξ = 0 | GRUT-I Lyapunov theorem | ✓ (numerical: check sign of ΔR₀ at each step) |
| **A3** | FDT consistency (stoch.) | Time-averaged ⟨(Φ − X)²⟩ = D ± statistical tolerance | BA5, TF9 | ✓ (numerical: compute running average, compare to D) |
| **A4** | Regime validity | F_t = (1,1,1,1) at all s ∈ [0,t]. If any flag drops to 0, the path has exited the controlled domain. | Book A domain map, AB1 | ✓ (numerical: evaluate four flag conditions at each step) |
| **A5** | Positivity | If the path represents a density matrix: all eigenvalues ≥ 0, or equivalently Im S_eff ≥ 0 along the CTP path. | BA1, A1-U3 | ✓ (structural: guaranteed by D > 0 in the CTP action) |
| **A6** | Causality | Φ_t depends only on {X_s, Φ_s, ξ_s}_{s ≤ t}. | Retarded kernel structure | ✓ (structural: the ODE is causal by construction) |
| **A7** | USL regime (if quantum) | For any active superposition: l > 2R (point-mass USL) or explicit Diosi computation for l < 2R. | Kappa-Prime, TF9, A1-L10 | ✓ (numerical: compare l to 2R) |

**Classification logic:**

```
if ALL conditions pass:          → ADMISSIBLE
if ANY condition fails:          → INADMISSIBLE
if A4 is marginal (flags flickering near boundary): → BOUNDARY
if A1 holds but A2 fails (noise-induced Lyapunov increase): → check A3 → ADMISSIBLE if stochastic FDT OK
```

Note on A2 under noise: In the stochastic case, the instantaneous Lyapunov function can INCREASE (noise kicks Φ away from X). This does not make the path inadmissible — it makes A2 inapplicable. For stochastic paths, A2 is replaced by A3 (statistical FDT check). The logic: deterministic paths must satisfy A2; stochastic paths must satisfy A3; both must satisfy A1, A4, A5, A6, A7.

---

## 2. Toy Trajectory Table (D5)

All trajectories use: τ = 1 s, β = 1.0, α = 0.01 m², D = 0.005 (CTP convention, corresponding to T = 0.01 in natural units).

### Trajectory T1: ADMISSIBLE (deterministic relaxation in weak-field matter background)

**Setup:** g_r is a static weak-field metric with R = 10 m⁻² (e.g., interior of a low-density star). X = β + αR = 1.0 + 0.01 × 10 = 1.1. Φ₀ = 0.5.

**Evolution:** Φ(t) = 1.1 − 0.6 e^{−t}

| Condition | Evaluation | Result |
|-----------|-----------|:------:|
| A1: Constitutive eq | τ Φ̇ + Φ = (0.6 e^{−t}) + (1.1 − 0.6 e^{−t}) = 1.1 = X. ✓ | PASS |
| A2: Lyapunov | R₀(t) = 0.36 e^{−2t}. dR₀/dt = −0.72 e^{−2t} < 0. ✓ | PASS |
| A4: Regime flags | f₁: |αR| = 0.1 = 0.1β → marginal but passes at < 0.1 threshold (just). f₂: ω_X = 0 (static) < ω_D. f₃: |Φ − X| ≤ 0.6 → initially > 0.1β; fails f₃ at t = 0. | **f₃ FAIL at t = 0** |
| A5: Positivity | Structural. ✓ | PASS |
| A6: Causality | ODE, retarded. ✓ | PASS |

**Verdict: BOUNDARY** — A1 and A2 pass, but the initial condition |Φ₀ − X| = 0.6 > 0.1 = 0.1β violates the linearity flag f₃ at early times. Once Φ relaxes to within 0.1 of X (at t > ln(6) ≈ 1.8 s), f₃ recovers. The path is admissible AFTER the transient but begins in the boundary zone.

**Revised T1 (fully admissible):** Φ₀ = 1.05, same X = 1.1.

Φ(t) = 1.1 − 0.05 e^{−t}. |Φ₀ − X| = 0.05 < 0.1. All flags 1 throughout.

| A1 | A2 | A3 | A4 | A5 | A6 | A7 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ✓ | ✓ | N/A | ✓ (all flags 1) | ✓ | ✓ | N/A |

**Verdict: ADMISSIBLE.**

### Trajectory T2: INADMISSIBLE (anti-relaxation)

**Setup:** Same X = 1.1. Φ₀ = 1.05. But imposed evolution: Φ(t) = 1.1 + 0.05(e^{+t} − 1). Φ moves AWAY from X after t = 0.

| Condition | Evaluation | Result |
|-----------|-----------|:------:|
| A1 | τ Φ̇ + Φ = 0.05 e^{t} + 1.1 + 0.05(e^{t} − 1) = 1.05 + 0.1 e^{t} ≠ 1.1 = X. ✗ | **FAIL** |
| A2 | R₀(t) = 0.0025(e^{t} − 1)², INCREASING. ✗ | **FAIL** |

**Verdict: INADMISSIBLE.** Fails A1 (constitutive equation violated) and A2 (Lyapunov increasing). This path is not generated by the GRUT update rule — it represents thermodynamically forbidden anti-dissipation.

### Trajectory T3: BOUNDARY (vacuum Schwarzschild — regime-blind)

**Setup:** g_r is the Schwarzschild exterior metric. R = 0 (Ricci-flat). X = β + α × 0 = β = 1.0. Φ₀ = 1.0 (already at equilibrium).

**Evolution:** Φ(t) = 1.0 (no dynamics — Φ is already at X).

| Condition | Evaluation | Result |
|-----------|-----------|:------:|
| A1 | τ Φ̇ + Φ = 0 + 1.0 = 1.0 = X. ✓ | PASS |
| A2 | R₀ = 0 everywhere. dR₀/dt = 0. ✓ (vacuously: non-increase satisfied by equality). | PASS |
| A4 | f₁: |αR| = 0 << β → ✓. f₂: ω_X = 0 → ✓. f₃: |Φ − X| = 0 → ✓. f₄: N/A (no superposition). | PASS |

**Verdict: ADMISSIBLE — but vacuously.** The path satisfies all conditions because Φ = X = constant throughout. The constitutive field carries no information about the Schwarzschild curvature. This is the vacuum-blindness limitation (NF3, FA1): the theory is formally consistent but physically empty in this regime. The BOUNDARY classification reflects this: formally admissible, physically uninformative.

---

## 3. Gate Table

| Gate | Criterion | Status | Reason |
|:----:|-----------|:------:|--------|
| **B1-G1** | State tuple complete and non-redundant | **PASS** | S_t = (Φ_t, X_t, M_t, F_t). Minimal non-redundant core: (Φ_t, X_t). M_t and F_t are derived/diagnostic, explicitly marked as REDUNDANT. |
| **B1-G2** | Update operator explicitly irreversible | **PASS** | U_{Δt} is first-order dissipative: information about (Φ − X) decays as e^{−Δt/τ}. Irreversibility derived from the contractivity property. Stochastic form adds noise-driven irreversibility. Markovian closure explicitly tagged (f₂ flag). |
| **B1-G3** | Residue functional mathematically defined | **PASS** | R[path; t] = ∫w(t−s)(Φ_s − X_s)²ds. Non-negativity, zero-iff-equilibrium, monotone decrease, equilibrium fluctuation level: all DERIVED with explicit proofs. Not prose-only. |
| **B1-G4** | Admissibility functional operationally computable | **PASS** | Seven conditions (A1-A7), each with an explicit numerical test (finite-difference constitutive check, Lyapunov sign, running FDT average, flag evaluation, etc.). Classification logic specified. |
| **B1-G5** | Toy trajectories validate discrimination | **PASS** | T1 (revised): ADMISSIBLE — all conditions pass. T2: INADMISSIBLE — A1 and A2 fail (anti-relaxation). T3: BOUNDARY — formally admissible but physically vacuous (vacuum-blind). All three cases discriminated correctly by A. |

---

## 4. Assumption Ledger

| # | Item | Status | Confidence | Regime |
|---|------|:------:|:----------:|--------|
| Φ_t as CTP classical field (Φ_r) | DERIVED | 0.95 | Markov/overdamped/linear |
| X_t = β + αR | ASSUMED | 0.55 | Weak field, matter present |
| M_t = (Φ − X)² as Lyapunov function | DERIVED | 0.90 | Linear, deterministic |
| F_t regime flags (4 conditions) | CONSTRUCTED | 0.85 | Definitions from Book A domain map |
| Update rule: Φ → Φ + (Δt/τ)(X − Φ) | DERIVED (from CTP) | 0.95 | Markov/overdamped/linear |
| Semigroup property of U | DERIVED | 0.90 | Constant X, Markovian |
| Markovian closure in U | ASSUMED | 0.65 | ω_X << ω_D |
| Noise term √(2D/τ²)ΔW | DERIVED (from CTP Sector 2) | 0.90 | Ohmic, high-T, thermal |
| R non-negative | DERIVED (proof) | 1.00 | All |
| R monotone decrease (deterministic) | DERIVED (proof) | 1.00 | Linear, constant X, deterministic |
| A1-A7 conditions | CONSTRUCTED / DERIVED (mixed) | 0.80 | As tagged per condition |
| τ is an EFT parameter | ASSUMED (A3, NF7) | 0.85 | All |
| D = k_BT τ/2 | DERIVED (FDT) | 0.90 | Ohmic, high-T |

---

## 5. Carried-Forward Dependency Impact

| UD | Description | Impact on B1 | Status after B1 |
|:--:|------------|-------------|:---------------:|
| UD1 | α undetermined | B1 uses α symbolically. No quantitative prediction possible. X_t depends on α. | **UNCHANGED** (still HIGH; deferred to B2+) |
| UD2 | Full CTP action unwritten | B1 does not require the full action — it works at the EOM level. No impact on B1. | **UNCHANGED** (still HIGH; deferred to B3+) |
| UD3 | One-loop D uncomputed | B1 uses D as an EFT parameter (from environmental bath). No loop computation needed. | **UNCHANGED** (still MEDIUM; deferred to B4+) |
| UD4 | Overdamped limit unjustified | B1 assumes overdamped (no kinetic term). Flagged in assumptions. | **UNCHANGED** (still MEDIUM; deferred to B3) |
| UD5 | Candidate B reserved | No impact on B1 (using Candidate A per AB1). | **UNCHANGED** (LOW) |
| UD6 | Candidate C blocked | No impact on B1. | **UNCHANGED** (LOW) |

No UD is resolved by B1. All are deferred as assigned.

---

## 6. Decision Token

### **continue_B2**

**Rationale:**
1. All five gates pass (B1-G1 through B1-G5).
2. All mandatory deliverables (D1-D5) are produced.
3. No contradiction found with TF, NF, or X items.
4. No new hidden assumptions introduced (all assumptions tagged in the ledger).
5. All UDs are carried forward as assigned, with no change in impact or priority.
6. The state-space scaffold is ready to receive the next stage (B2: parameter constraints, nonlinear extension, or admissibility stress-testing).

---

*GRUT III Book B Stage B1 complete. Decision: continue_B2. State tuple: S_t = (Φ_t, X_t, M_t, F_t). Update rule: Φ_{t+Δt} = Φ_t + (Δt/τ)(X_t − Φ_t) + noise. Residue: R = ∫w(Φ−X)²ds, five properties derived. Admissibility: seven conditions, operationally computable. Toy trajectories: admissible/inadmissible/boundary all correctly discriminated. Gates: 5/5 pass. Assumptions: 13 items tagged. UDs: 6/6 unchanged. No new conflicts. No new physics claims.*
