# Book XXI — Target Beta: Embedded Multiplet Dynamics and Attractor Audit

## Mathematical Dynamics Audit

**Predecessor:** Book XXI Alpha (embedding Phi = |vec_Phi| feasible at zero cost; continuation not successor)
**Function:** Determine whether the embedding is dynamically consistent and whether it produces genuinely richer dynamics than the unique-attractor linear scalar core

---

## 1. Executive Verdict

**embedding_dynamically_consistent_but_single_attractor — with one structurally significant caveat.**

The embedding Phi = |vec_Phi| = eta f(r) is equation-level INCONSISTENT as a literal identification: the radial mode of the triplet satisfies a topology-driven BVP, while the native scalar satisfies a source-driven constitutive ODE. These are different equations with different mechanisms. The identification works at the EFFECTIVE level (shape agreement at 1/r^4) but fails at the mechanistic level (topology-driven vs source-driven; coefficient mismatch factor ~300x).

However, the embedded system has one structurally significant feature the scalar core lacked: **the vacuum manifold S^2 provides a continuous infinity of orientational vacua.** The radial mode has a unique profile (one attractor in f), but the DIRECTION n_hat on S^2 is unconstrained. This is topological degeneracy, not dynamical multiplicity — but it is genuine multiplicity of the equilibrium configuration.

**Whether this orientational degeneracy can be promoted to dynamical multiplicity depends on whether angular perturbations of the hedgehog have multiple stable configurations. This is an open question not resolved by the current static BVP analysis.**

---

## Part I — Equation-Level Consistency

### The two equations

**Radial mode of the triplet** (from hedgehog ansatz vec_Phi = eta f(r) r_hat):
```
f'' + (2/r)f' - (2/r^2)f - lambda eta^2 f(f^2 - 1) = 0
BCs: f(0) = 0, f(inf) = 1
```

**Native scalar constitutive law:**
```
tau dPhi/dt + Phi = X(r)
Static form: Phi_eq(r) = X(r) = M/r^2
```

### The inconsistency

These are DIFFERENT equations:

| Property | Triplet radial mode | Native scalar |
|----------|-------------------|--------------|
| Order | Second (in r) | First (in t); algebraic in static |
| Type | Elliptic BVP | Parabolic ODE / algebraic |
| Mechanism | Topology (angular gradient + potential) | Source-driven (X = M/r^2) |
| Nonlinearity | lambda eta^2 f(f^2-1) | LINEAR (in Phi) |
| Boundary conditions | f(0)=0, f(inf)=1 | Phi(r) = X(r) everywhere |
| Profile shape | f(r): 0 → 1 transition at core width delta | Phi(r) = M/r^2 (monotone 1/r^2 decay) |
| Asymptotics | f → 1 (constant) | Phi → 0 (decays as 1/r^2) |

**The identification Phi = eta f(r) requires Phi → eta ≠ 0 at infinity, while the native scalar has Phi → 0. These are structurally incompatible asymptotic behaviors.**

### Classification of the identification

The identification Phi = |vec_Phi| is **NOT an exact recovery** of the native scalar. It is:

- **Shape agreement at intermediate scales:** D4 confirmed that the radial kinetic energy (1/2)(eta f')^2 scales as 1/r^4 (exponent -2.89 approaching -4.0), which matches the Component A budget shape.
- **Coefficient mismatch:** The radial kinetic amplitude is 0.35% of the Component A budget (factor ~300x too small).
- **Mechanism mismatch:** The radial mode is topology-driven (self-interaction + boundary conditions); the scalar is source-driven (gravitational acceleration).

**Result: SYMBOLIC ONLY at the equation level. The identification is an architectural association, not a dynamical identity.**

---

## Part II — Radial/Angular Decomposition

### Full triplet decomposition

Write vec_Phi = rho(r,t) n_hat(theta, phi, t) where rho = |vec_Phi| (radial modulus) and n_hat is the unit orientation on S^2.

The O(3) sigma-model energy decomposes as:

```
E = integral [
  (1/2)(nabla rho)^2                    [radial gradient]
  + (1/2) rho^2 |nabla n_hat|^2         [angular gradient = covariant derivative on S^2]
  + V(rho)                               [Mexican-hat potential: lambda(rho^2 - eta^2)^2/4]
] d^3x
```

### Radial sector

The radial mode rho(r) = eta f(r) satisfies the radial BVP. At equilibrium, rho(r) is FIXED by the topology (hedgehog boundary conditions) and the potential. The Lyapunov structure of the native scalar core does NOT apply here — the radial profile is determined by spatial balance, not by temporal relaxation.

**Does the dissipative grammar G1-G6 apply to the radial mode?** Only if we add a temporal relaxation equation for rho. The pure hedgehog BVP is STATIC. To make it dynamical, one would write:

```
tau_rho d(rho)/dt + rho = rho_eq(r)     [hypothetical constitutive extension]
```

where rho_eq(r) = eta f_eq(r) is the hedgehog profile. This is POSSIBLE but NOT in the current canon. It would be a new constitutive equation for the radial mode, extending the grammar from (Phi → X) to (rho → rho_eq). This is an admissible extension but not a free one.

### Angular sector

The angular modes n_hat(theta, phi) live on the S^2 vacuum manifold. For the hedgehog, n_hat = r_hat (locked to spatial direction). Perturbations around the hedgehog have two types:

1. **Massive radial perturbation:** delta rho around eta. The potential V(rho) has a minimum at rho = eta with mass m_radial = sqrt(2 lambda) eta. These are GAPPED (massive) and decay.

2. **Massless angular perturbation (Goldstone modes):** delta n_hat on S^2. The O(3) → U(1) breaking produces 2 Goldstone bosons. These are GAPLESS and propagate.

The angular Goldstone modes represent the NEW content that the embedding provides beyond the 1D scalar. They are:
- Long-range (massless)
- Propagating (if spatial dynamics are included)
- Topologically constrained (hedgehog winding fixes global orientation)
- NOT subject to the dissipative grammar (they are conservative, wave-like modes)

**This is the key structural result: the embedding produces angular modes that are OUTSIDE the dissipative grammar. They are conservative, not dissipative. They propagate, not relax.**

---

## Part III — Phase Portrait and Attractor Audit

### Radial attractor structure

The hedgehog BVP f'' + ... = 0 with f(0) = 0, f(inf) = 1 has:

**Single radial profile per parameter set (lambda, eta).** The numerical evidence (D2, D11) shows convergence to a unique f(r) at each tested lambda. No bifurcation in the radial mode has been observed.

**BUT: formal uniqueness is NOT proven** (D11 Nonclaim 7). The nonlinear BVP could in principle admit multiple solutions at untested parameter values. This is an open question.

| Feature | Status | Evidence |
|---------|--------|---------|
| Single global attractor (radial) | **PRESENT (numerically)** | D2: unique f(r) at each lambda tested (5-200) |
| Multiple attractors (radial) | **NOT OBSERVED** | No bifurcation found in tested range |
| Formal uniqueness proof | **ABSENT** | D11 Nonclaim 7 |
| Bifurcation search performed | **NO** | Not systematically tested |

### Angular attractor structure

The vacuum manifold S^2 has a **continuous infinity of degenerate vacua** — every direction n_hat on S^2 is an equally valid equilibrium orientation. The hedgehog selects n_hat = r_hat, but this is a TOPOLOGICAL CONSTRAINT (winding number = 1), not a dynamical preference.

| Feature | Status | Significance |
|---------|--------|-------------|
| **S^2 orientational degeneracy** | **PRESENT (structurally significant)** | Continuously many equilibrium directions |
| Symmetry-broken branches | **PRESENT** | Each direction on S^2 is a distinct broken-symmetry state |
| Topological sectors | **PRESENT** | Hedgehog (n=1) vs anthedgehog (n=-1) vs higher winding |
| Basin partitioning | **PRESENT (topological)** | Winding number partitions configurations into disjoint sectors |
| Dynamically distinct endpoints | **CONDITIONAL** | For purely angular perturbations, all S^2 directions are degenerate |

**The S^2 degeneracy is TOPOLOGICAL MULTIPLICITY, not DYNAMICAL MULTIPLICITY.** All directions are energetically equivalent. There is no dynamical mechanism that prefers one direction over another. The hedgehog selects r_hat because of the boundary conditions, not because of energetics.

### Combined radial + angular

The full phase portrait of the embedded system is:

```
Radial: unique profile f(r) per (lambda, eta)     [one attractor in radial sector]
Angular: degenerate S^2 of orientations             [continuous manifold of equilibria]
Topological: discrete winding sectors (n = 0, ±1, ±2, ...)  [disjoint sectors]
```

**Classification:**
- Single global attractor: **NO** (S^2 degeneracy means infinitely many equilibria)
- Multiple attractors: **YES** (but degenerate, not competing)
- Bifurcations: **NOT OBSERVED** (radial); **STRUCTURAL** (topological winding)
- Metastable states: **OPEN** (higher winding numbers may be metastable)
- Symmetry-broken branches: **YES** (O(3) → U(1) at vacuum)

---

## Part IV — Basin and Multiplicity Analysis

### Topological sectors as basin partition

The winding number n = (1/4pi) integral n_hat . (dn_hat x dn_hat) dOmega partitions the configuration space into disjoint sectors. The hedgehog (n=1) and antihedgehog (n=-1) are in DIFFERENT sectors. Transitions between sectors require infinite energy (topological barrier).

**This is genuine basin partitioning** — but it is TOPOLOGICAL, not dynamical. A system starting in sector n=1 stays in sector n=1 forever. There is no probability of transitioning to n=-1.

### S^2 orientational degeneracy as multiplicity

Within the n=1 sector, the hedgehog direction n_hat = r_hat is selected by the boundary conditions. But if the boundary conditions were different (e.g., at finite radius with different angular profile), different orientations would be selected.

**Does this create multiplicity relevant to probability?** No — for a given set of boundary conditions, the orientation is DETERMINED. There is no uncertainty about which direction the hedgehog points once the boundary is specified.

### Does XX Alpha's unique-attractor theorem survive?

**MODIFIED, not overthrown.** The radial sector retains a unique attractor (single f(r) profile). The angular sector has degenerate equilibria (S^2 of orientations). The combined system has a unique attractor WITHIN each topological sector once boundary conditions are specified.

**The contraction theorem is LOCALIZED:** within each topological sector and with fixed boundary conditions, the dynamics contract toward a unique equilibrium. The multiplicity is in the CHOICE of sector and boundary, not in the dynamics within a sector.

---

## Part V — Probability Relevance Test

### Does the S^2 degeneracy help with probability?

**No, for the following reasons:**

1. **Degeneracy ≠ probability.** The S^2 directions are all EQUALLY VALID equilibria. There is no dynamical mechanism to weight one direction over another. A probability measure over S^2 would have to be POSTULATED (e.g., uniform Haar measure), not derived.

2. **Topological sectors ≠ probabilistic branches.** The winding-number sectors are DISJOINT (infinite energy barrier). A system in sector n=1 has probability 1 of staying there. There is no branching.

3. **Within a sector, the dynamics are deterministic.** Given initial conditions and boundary conditions, the system evolves to a UNIQUE equilibrium. There is no splitting, no branching, no weighting.

4. **The angular Goldstone modes are CONSERVATIVE, not dissipative.** They propagate like waves, not relax like the constitutive equation. They do not have the Lyapunov/semigroup structure of the core grammar. They cannot inherit the fluctuation-absence result (XVIII Alpha applies to the DISSIPATIVE sector only).

### Is probability still extension-only?

**YES.** The embedding produces richer mathematical structure (S^2 manifold, topological sectors, Goldstone modes) but does not produce probability. The XX Alpha verdict (probability_extension_only) survives. Multiple equilibria exist (orientationally degenerate) but are not dynamically weighted.

### What WOULD be needed for probability?

A mechanism that:
- Breaks the S^2 degeneracy dynamically (not just topologically)
- Creates COMPETING attractors with different energies
- Induces a natural measure over the competing attractors

The Mexican-hat potential does not do this (all directions equally deep). An EXTERNAL symmetry-breaking field would — but that is a new postulate.

---

## Part VI — Cost and Continuity

### Does the zero-debt reinterpretation survive?

**PARTIALLY.** The identification Phi = |vec_Phi| is architecturally meaningful (it associates the scalar core with the radial mode of the committed triplet) but equation-level INCONSISTENT (different equations, different mechanisms, coefficient mismatch). The embedding is a DESIGN PRINCIPLE, not a dynamical identity.

**Cost analysis:**

| Aspect | Cost | Status |
|--------|------|--------|
| Embedding identification Phi = eta f(r) | 0 | SYMBOLIC (not equation-level) |
| Radial constitutive extension (tau_rho drho/dt + rho = rho_eq) | +1P (new constitutive equation for radial mode) | NOT in canon; would need postulation |
| S^2 Goldstone dynamics | 0 (already in O(3) sigma model) | BRIDGE-LEVEL (from matter bridge) |
| Angular measure / weighting | +1P (Haar measure or symmetry-breaking) | NOT in canon; extension-only |

**The "zero cost" claim from XXI Alpha holds for the symbolic identification but NOT for making the embedding dynamically operative.**

### Ontological reduction?

The embedding DOES NOT reduce the ontological count. Before: 1 scalar + 3 triplet = 4 DOF. The identification Phi = eta f means the scalar is the radial mode, so effectively 3 DOF (the triplet with radial mode = "scalar"). But the scalar's constitutive equation is DIFFERENT from the triplet's hedgehog equation, so the two are not actually identified at the dynamical level.

**Honest count: the embedding is an architectural association, not an ontological reduction.**

---

## Part VII — Final Verdict

### **embedding_dynamically_consistent_but_single_attractor**

The embedding is architecturally meaningful but dynamically incomplete. The radial mode of the triplet and the native scalar satisfy different equations with different mechanisms. The S^2 orientational degeneracy provides genuine multiplicity of equilibria but not dynamical multiplicity or probability. The Goldstone modes are conservative (wave-like), not dissipative, and fall outside the constitutive grammar.

### Consequence Statement

The GRUT core has NOT genuinely become richer in the load-bearing sense. The phase portrait gained S^2 degeneracy (orientational) and topological sectors (winding), but these are STRUCTURAL features of the already-committed O(3) sector, not new consequences of the embedding. The unique-attractor theorem is modified (localized to sectors) but not overthrown. The probability question is NOT reopened.

XXI Alpha was a correct feasibility assessment: the embedding is feasible as an architectural association. XXI Beta shows it does not change the dynamical category. The program remains a deterministic irreversible process framework. The embedding is a clarifying move (associating the scalar with the radial mode) but not a productive one (no new dynamics, no new multiplicity, no new probability).

**The honest next step is either:**
1. **Accept the framework as complete at the current level** and stabilize its identity
2. **Test whether the nonlinear coupled system has bifurcations at untested parameter values** (genuine computation; might find dynamical multiplicity; might not)

Option 2 is the only live path that could change the program's category. It requires numerical bifurcation analysis of the coupled (Phi, f) system across the full (lambda, g_p, eta) parameter space.

---

## Hard-Gated Summary Table

| Test | Verdict |
|------|---------|
| Equation-level consistency tested | **YES** — SYMBOLIC ONLY (different equations, different mechanisms) |
| Radial/angular decomposition written | **YES** — radial BVP + angular Goldstone |
| Phase portrait analyzed | **YES** — unique radial attractor; S^2 angular degeneracy |
| Basin structure assessed | **YES** — topological sectors (disjoint); S^2 degenerate (no weighting) |
| Probability relevance tested | **YES** — still extension-only (degeneracy ≠ probability) |
| Cost and continuity assessed | **YES** — symbolic identification free; dynamical extension costs +1P |
| Final verdict clear | **YES** — embedding_dynamically_consistent_but_single_attractor |

---

*XXI Beta complete. Embedding is architecturally meaningful but dynamically incomplete. Radial mode: unique attractor. Angular: degenerate S^2. No probability. No new dynamical category. Goldstone modes are conservative, not dissipative. The program remains a deterministic irreversible process framework. Live path: bifurcation analysis of the coupled nonlinear system.*
