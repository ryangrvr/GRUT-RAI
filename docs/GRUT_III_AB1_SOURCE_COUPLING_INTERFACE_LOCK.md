# GRUT III — A→B Bridge, Stage AB1: Source Coupling Interface Lock

**Inherited from Book A:** BA1-BA7 (assumable), X1-X10 (blacklist), domain map (A4), bath verdict (A3: mixed bath, environmental Sectors 1-2, gravitational Sector 3).

**Purpose:** Select and lock the X[g_{mu nu}] interface that Book B may assume. This is a transfer stage, not a Book B stage. It resolves MC1 (Book A's highest-priority open closure condition).

---

## Candidate A: X = αR + β

### 1. Explicit assumptions

| # | Assumption | Tag |
|---|-----------|:---:|
| AA1 | Phi couples to the Ricci scalar R of the classical metric g_r. | ASSUMED |
| AA2 | The coupling is linear in R. | ASSUMED (simplest choice; quadratic R^2 is a different theory) |
| AA3 | β is a constant background equilibrium, independent of position and time. | ASSUMED |
| AA4 | α is a constant coupling, independent of position and time. | ASSUMED |
| AA5 | The Einstein equation holds on-shell: R = -8πG T^{matter}/c^4 (trace). | INHERITED (GR in controlled regime) |

### 2. Regime tags

| Regime | Zone | Condition |
|--------|:----:|-----------|
| Flat space (R = 0) | **CONTROLLED** | X = β. Trivial. |
| Weak field + matter (αR << β) | **CONTROLLED** | X = β − 8πGα T^m/c^4. Perturbative correction. Constitutive law well-posed. |
| Moderate curvature (αR ~ β) | **CAUTION** | X changes sign possible. Phi attractor shifts significantly. Linear analysis still valid but perturbative hierarchy breaks. |
| Vacuum Schwarzschild/Kerr (R = 0) | **CONTROLLED but BLIND** | X = β. No curvature response. Not wrong — just vacuous. |
| Strong curvature (r ~ R_S, matter interior) | **UNSAFE** | R may be large and rapidly varying. α not bounded. Overdamped limit untested. |
| Cosmological (FRW) | **CONTROLLED** | R = 6(ä/a + (ȧ/a)² + k/a²). X varies on Hubble timescale >> τ. Adiabatic tracking. |

### 3. Φ role classification

| Condition | Φ role | Status |
|-----------|:------:|:------:|
| X = const (flat space, static matter) | **Auxiliary** (slaved: Φ* = X, no independent DOF) | DERIVED |
| X(t) varies (dynamic spacetime) | **Dynamical** (Φ tracks X with lag τ, encodes curvature history) | DERIVED |
| X varies faster than 1/τ | **Transient-dominated** (Φ lags significantly behind X) | DERIVED |

No regime in which Φ is a propagating wave mode. The overdamped limit (A1-L8, ASSUMED) excludes this. Φ is always relaxational, never oscillatory, under Candidate A with the current backbone.

### 4. Semiclassical consistency impact

The semiclassical Einstein equation with Candidate A reads:

```
G_{μν} = 8πG [ T^{matter}_{μν} + T^{Φ}_{μν}(Φ, X(R)) ]
```

T^{Φ}_{μν} depends on R through X = β + αR. This creates an implicit equation for R:

```
R = −8πG(T^{matter} + T^{Φ}(R)) / c⁴
```

**In the controlled regime (αR << β):** T^{Φ} ≈ T^{Φ}(β) ≈ −β²/(2τ²). This is a constant energy density, independent of R. The backreaction on the Einstein equation is a cosmological-constant-like term:

```
Λ_eff = 8πG β²/(2τ²c⁴)
```

For β ~ 1 (natural units), τ ~ 1 s: Λ_eff ~ 10⁻²⁶ m⁻² (similar to the observed cosmological constant if β and τ are tuned). This is an OBSERVATION, not a derivation — no fine-tuning claim is made.

**At next order (linear in αR):** The correction to T^{Φ} is proportional to αR, giving a term αR × (dT^{Φ}/dX) in the Einstein equation. This modifies the effective gravitational coupling:

```
G_eff = G / (1 − 8πG α (dT^{Φ}/dX) / c⁴)
```

For this to be perturbatively controlled: |8πGα(dT^{Φ}/dX)/c⁴| << 1. Since dT^{Φ}/dX = −X/τ² ≈ −β/τ², the condition is |8πGαβ/(τ²c⁴)| << 1.

**Status:** Perturbatively consistent at small α. No obstruction. Not self-contradictory.

### 5. Linear stability / ghost screen (declared regime)

**Linearize** around Φ = β, g = η + h:

```
τ δΦ̇ + δΦ = α δR
```

- δΦ eigenvalue: λ = −1/τ < 0. **Exponentially stable.** No growing mode.
- No new propagating mode: δΦ is slaved to δR with time constant τ. One degree of freedom (δΦ), first-order, damped.
- Ghost check: The CTP noise term iD Φ_a² has D > 0 (from FDT). No negative-norm state. The coupling αR appears in the REAL part of the CTP action (Sector 1), which is linear in Φ_a — it does not modify the positivity condition Im S_eff ≥ 0.

**Verdict: No instability, no ghost, no new propagating DOF in the declared regime.** Status: **DERIVED** (linearized analysis).

### 6. Parameter-cost score

| Metric | Assessment | Score |
|--------|-----------|:-----:|
| Number of new parameters | 2 (β, α) | 2/5 |
| Derivative order of X | 0 (X depends on R, which is 2nd derivative of g, but X itself is algebraic in R) | 1/5 |
| New DOF introduced | 0 | 1/5 |
| Analytic tractability | High (linear ODE, linear source) | 1/5 |
| **Total complexity** | | **5/20 = 1.25/5** |

### 7. Failure modes

| # | Mode | Severity | Regime |
|---|------|:--------:|--------|
| FA1 | Vacuum-blind (R = 0 in Schwarzschild exterior) | KNOWN LIMITATION | Vacuum spacetimes |
| FA2 | f(R)-like backreaction at large α | MODERATE | α R ~ β |
| FA3 | α and β undetermined (EFT inputs, not predictions) | STRUCTURAL | All |

### 8. Nonclaims

- A does NOT make the CTP action covariant. X is a covariant scalar, but the CTP action is Newtonian.
- A does NOT predict α or β. They are parameters.
- A does NOT apply at strong curvature.
- A does NOT resolve the vacuum-curvature problem.

---

## Candidate B: X = αR + γT + β

### 1. Explicit assumptions

AA1-AA5 from Candidate A, plus:

| # | Assumption | Tag |
|---|-----------|:---:|
| AB6 | Phi additionally couples to the trace of the matter stress-energy T = g^{μν}T^{matter}_{μν}. | ASSUMED |
| AB7 | γ is a constant coupling independent of position and time. | ASSUMED |

### 2-5. Assessment (abbreviated)

**On-shell degeneracy (decisive):** In GR, R = −8πGT/c⁴. Therefore:

```
αR + γT = (−8πGα/c⁴ + γ)T ≡ γ_eff × T
```

Candidate B collapses to a single effective coupling γ_eff to the matter trace. The parameters α and γ are NOT independently measurable on-shell in the controlled (GR-valid) regime.

**Consequence:** B adds one parameter (γ) but gains zero independent physics over A in the declared regime. The only scenario where α and γ decouple is when Φ backreaction modifies the Einstein equation enough to break R = −8πGT/c⁴ — which is a CAUTION/UNSAFE regime effect.

### 6. Parameter-cost score

| Metric | Score |
|--------|:-----:|
| Parameters | 3 (but 2 effective on-shell) |
| Redundancy | HIGH |
| **Total** | **3/5** (penalized for redundancy) |

### 7. Failure modes

All of A, plus:
- FB1: On-shell parameter degeneracy. α and γ cannot be separated without leaving the declared regime.
- FB2: Circular backreaction T^{Φ}(Φ(X(T))) adds algebraic complexity without physical content at leading order.

### 8. Nonclaims

Same as A, plus: B does NOT provide independent curvature AND matter coupling in the controlled regime.

---

## Candidate C: X = αR + β + ε□R

### 1. Explicit assumptions

AA1-AA5 from A, plus:

| # | Assumption | Tag |
|---|-----------|:---:|
| AC6 | X includes a term proportional to the d'Alembertian of R: ε□R. | ASSUMED |
| AC7 | ε is a constant coupling. [Phi] × [length]⁴. | ASSUMED |

### 2. Regime tags

- Static spacetimes: □R = 0. C reduces to A. No additional content.
- Dynamic spacetimes: □R ≠ 0. C provides a response to the RATE OF CHANGE of curvature.
- Strong field: □R involves 4th derivatives of the metric. Ostrogradsky ghost risk.

### 5. Linear stability / ghost screen

**BLOCKED.** The □R term, when coupled back through the semiclassical Einstein equation, introduces 4th-order metric derivatives. The Ostrogradsky theorem (1850) states that non-degenerate Lagrangians with higher-than-2nd-order time derivatives generically produce ghost instabilities (unbounded negative-energy modes).

In pure R + cR² gravity (Starobinsky), the 4th-order terms are degenerate and the ghost is absent (the extra DOF is a healthy scalaron). But the ε□R coupling to Φ is NOT the Starobinsky structure — it is a mixed higher-derivative coupling between Φ and g. Ghost-freedom is NOT guaranteed and has NOT been checked.

**Verdict: BLOCKED.** Cannot pass AB1-G3 without an explicit ghost-freedom proof, which does not exist.

### 6. Parameter-cost score: **5/5** (maximum complexity, blocked).

---

## Gate Evaluation

### AB1-G1: Minimality (lowest-complexity viable interface)

| Candidate | Complexity | Viable? | Minimal? |
|:---------:|:----------:|:-------:|:--------:|
| A | 1.25/5 | **YES** | **YES** |
| B | 3/5 | YES (but redundant on-shell) | NO |
| C | 5/5 | **BLOCKED** | NO |

**Gate AB1-G1: PASS (Candidate A).**

### AB1-G2: Internal consistency in declared regime

Candidate A:
- Constitutive law well-posed with X = β + αR: ✓
- CTP unitarity unaffected (X enters linearly in Sector 1): ✓
- FDT unaffected (D and τ independent of X): ✓
- Semiclassical backreaction perturbatively controlled at small α: ✓
- No self-contradiction found: ✓

**Gate AB1-G2: PASS (Candidate A).**

### AB1-G3: No unstable/ghost-like behavior in declared regime

Candidate A:
- Linearized eigenvalue: −1/τ < 0 (stable): ✓
- No new propagating DOF: ✓
- CTP positivity Im S_eff ≥ 0 preserved: ✓
- No Ostrogradsky risk (no higher derivatives): ✓

**Gate AB1-G3: PASS (Candidate A). BLOCKED (Candidate C).**

### AB1-G4: Regime boundaries explicit

| Regime | Candidate A status |
|--------|:------------------:|
| Flat space | CONTROLLED |
| Weak field + matter | CONTROLLED |
| Vacuum Schwarzschild | CONTROLLED but BLIND |
| Moderate curvature | CAUTION |
| Strong curvature | UNSAFE |
| Cosmological | CONTROLLED |

All boundaries are explicit. No regime is left untagged.

**Gate AB1-G4: PASS.**

### AB1-G5: Book-B transfer contract clear

See Section below.

**Gate AB1-G5: PASS** (contract written).

---

## Decision Token: **adopt_A**

**Rationale:**
1. Candidate A passes all five bridge gates.
2. Candidate B is viable but on-shell degenerate with A — adds a parameter without adding physics. Rejected by minimality (G1).
3. Candidate C is blocked by unresolved Ostrogradsky ghost risk (G3).
4. A is the unique minimum-complexity passing candidate.

---

## A→B TRANSFER CONTRACT

### What Book B may assume

| # | Assumable item | Conditions | Source |
|---|---------------|------------|--------|
| TF1 | X[g_r] = β + αR(g_r) is the source coupling interface. | Provisional. May be revised by future stages. | AB1 |
| TF2 | β and α are EFT parameters (constant, undetermined). | All regimes. | AB1 |
| TF3 | The constitutive law with this X is: τ dΦ/dt + Φ = β + αR. | Markovian, overdamped, linear, weak-field. | AB1 + BA2 |
| TF4 | The coupling is linearly stable with eigenvalue −1/τ. | Linearized, weak-field. | AB1-G3 |
| TF5 | No ghost or new propagating DOF from the X coupling. | Linearized, weak-field. | AB1-G3 |
| TF6 | Semiclassical backreaction is perturbatively controlled. | |αR| << β. | AB1 §4 |
| TF7 | All Book A inheritables BA1-BA7. | Per Book A conditions. | Book A |
| TF8 | Environmental bath provides τ, D, T (Sectors 1-2). | Flat space and weak field. | A3, BA4 |
| TF9 | USL: Λ = Gm²/(ℏl) for l > 2R; Diosi integral for l < 2R. | Newtonian, tree-level. | BA3 |

### What Book B may NOT assume

| # | Forbidden assumption | Reason |
|---|---------------------|--------|
| NF1 | That X = β + αR is the correct or unique coupling. | It is provisional and ASSUMED, not derived. |
| NF2 | That α is known, constrained, or small. | α is an undetermined EFT parameter. |
| NF3 | That Φ responds to vacuum curvature. | R = 0 in Schwarzschild/Kerr exterior. X = β only. |
| NF4 | That the CTP action is covariant. | It is not. Newtonian limit only. |
| NF5 | That the semiclassical Einstein equation has been verified for the (g, Φ) system. | Only the perturbative consistency of the backreaction has been checked, not the full variation w.r.t. g_a. |
| NF6 | That the overdamped limit is justified from first principles. | It is ASSUMED (A1-L8). |
| NF7 | That τ is predicted by the theory. | It is an EFT parameter (A3, C6). |
| NF8 | That the theory is valid at strong curvature. | UNSAFE per Book A domain map. |
| NF9 | That GRUT is a ToE. | Blacklisted (X10). |

### Unresolved dependencies carried forward

| # | Dependency | Origin | Impact on Book B |
|---|-----------|--------|-----------------|
| UD1 | α not determined. | AB1 | Book B cannot make quantitative predictions involving X without specifying or constraining α. |
| UD2 | Full (g, Φ) CTP action not written. | Book A MC2 | Book B cannot verify semiclassical Einstein equation or compute one-loop effects. |
| UD3 | One-loop gravitational D not computed. | Book A MC3, D1 | Bath identity (environmental vs gravitational near horizons) remains bounded-open. |
| UD4 | Overdamped limit not justified. | Book A MC4 | Φ inertial mass M unknown; overdamped assumption untested. |
| UD5 | Candidate B (αR + γT + β) reserved. | AB1 | If backreaction breaks on-shell degeneracy, B may need to replace A. |
| UD6 | Candidate C (□R) blocked. | AB1 | If dynamical curvature response is needed, ghost-freedom must be demonstrated first. |

### Exact blacklist inherited from Book A

X1-X10 (full list in Book A Stage A4). All remain binding. No additions from AB1.

---

*GRUT III A→B Bridge Stage AB1 complete. Decision: adopt_A. X = β + αR. All five gates pass: minimality (G1), consistency (G2), stability/ghosts (G3), regime boundaries (G4), transfer contract (G5). Candidate B rejected (on-shell degenerate, violates G1). Candidate C blocked (Ostrogradsky, violates G3). Transfer contract: 9 assumables (TF1-TF9), 9 forbidden (NF1-NF9), 6 unresolved dependencies (UD1-UD6), full blacklist (X1-X10). Book B may now open.*
