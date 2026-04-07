# Program G — Stage G0: Charter Freeze for Scale-Universality and Memory-Kernel Stability

---

## 1. Program Identity

### Technical

Program G investigates whether the first-order Markovian constitutive law τ u^μ∇_μΦ + Φ = X(g) is stable under coarse-graining (an RG attractor in the space of dissipative dynamics), or whether non-Markovian memory kernels are generically generated when microscopic or intermediate-scale degrees of freedom are integrated out. It does NOT assume the Markovian form is correct at all scales. It does NOT import any GRUT-specific conclusion as an axiom. It treats the Markovian constitutive law as a HYPOTHESIS TO BE TESTED under RG flow, not as an established result.

### Separation from prior programs

| Prior result | Program G treatment |
|-------------|-------------------|
| F3: GRUT = EIT in curved spacetime (repackaging) | INHERITED as fact. Not contested. Program G asks a DIFFERENT question: is the EIT first-order form stable under scale change? |
| E3: GRUT is a generic class member (non-unique) | INHERITED. Program G does not seek uniqueness. It seeks STABILITY — whether the Markovian form persists under coarse-graining regardless of which class member one starts with. |
| A3: Environmental bath provides τ, D | INHERITED. Program G investigates how τ and D transform under coarse-graining — whether they remain well-defined Markovian parameters or acquire memory structure. |
| F1: USL is robust and class-universal | NOT REOPENED. Program G concerns Sectors 1-2 (constitutive dynamics), not Sector 3 (USL). |

### Non-goals

- No ToE claim.
- No uniqueness claim for the Markovian form.
- No claim that GRUT is special among class members.
- No strong-field or UV-complete extension.
- No attempt to derive τ from first principles (that failed in D2).

---

## 2. Core Question Formalization

### Q1: Markovian closure under coarse-graining

```
QUESTION: Given a microscopic dynamics with many degrees of freedom and
short-range correlations, does integrating out short-wavelength / fast
modes generically produce a MARKOVIAN effective dynamics for the remaining
slow modes?

Formally: Start with a system of N coupled first-order equations
  τ_i ẋ_i = F_i(x₁,...,x_N, g)    i = 1,...,N

Integrate out the fast modes {x_{k+1},...,x_N} (those with τ_i << τ_slow).

Question: Is the resulting effective dynamics for the slow modes {x₁,...,x_k}
  (a) Markovian:  τ_eff ẋ_slow = F_eff(x_slow, g)
  (b) Non-Markovian: ẋ_slow(t) = ∫₀ᵗ K(t−s) F(x_slow(s), g) ds
  (c) Dependent on the scale separation (Markovian only when τ_fast << τ_slow)

If (a): Markovian closure is an attractor.
If (b): memory kernels are generically generated.
If (c): Markovian form is a controlled approximation, not a universal attractor.
```

### Q2: Kernel classification under coarse-graining

```
QUESTION: When memory kernels ARE generated, what is their generic form?

Candidate kernel classes:
  K₁(t) = (1/τ) exp(−t/τ)                     [exponential — Markovian limit]
  K₂(t) = Σᵢ aᵢ exp(−t/τᵢ)                    [multi-exponential — finite memory]
  K₃(t) = t^{−α} / Γ(1−α)  for 0 < α < 1      [power-law — fractional / long memory]
  K₄(t) = (1/τ) exp(−t/τ) cos(ωt)              [oscillatory — underdamped modes]

Each class has different physical implications:
  K₁: Markovian, memoryless, single timescale
  K₂: Finite-depth memory, multiple timescales
  K₃: Long-range memory, no characteristic timescale (scale-invariant)
  K₄: Memory with oscillation (underdamped integrated-out modes)

Question: Which class(es) appear generically under coarse-graining of
a multi-scale dissipative system?
```

### Q3: Attractor status of the Markovian form

```
QUESTION: In the space of memory kernels K(t), is K₁(t) = (1/τ)e^{−t/τ}
an RG FIXED POINT, an ATTRACTOR BASIN, or a FINE-TUNED SURFACE?

Formally: Define a coarse-graining map CG_λ that integrates out modes
with timescale < λ. Apply CG_λ to a general kernel K(t):

  CG_λ[K] = K_eff(t; λ)

Question:
  (a) Does K_eff(t; λ) → K₁ as λ → ∞?           [ATTRACTOR: Markovian is the IR limit]
  (b) Does K_eff(t; λ) ≈ K₁ only when K ≈ K₁?    [FIXED POINT but not attractive]
  (c) Does K_eff(t; λ) generically develop
      non-exponential tails (K₂, K₃)?              [NOT AN ATTRACTOR: memory is generic]
```

---

## 3. Minimal Model Ladder

### M1: Toy stochastic microdynamics

```
MODEL: N coupled Ornstein-Uhlenbeck processes on a graph.
  τᵢ ẋᵢ = −xᵢ + Σⱼ Jᵢⱼ xⱼ + ξᵢ(t)
  where Jᵢⱼ is a coupling matrix (sparse, random, or structured)
  and ξᵢ is white noise with ⟨ξᵢξⱼ⟩ = 2Dᵢ δᵢⱼ δ(t−t')

  Timescale distribution: τᵢ drawn from a distribution p(τ).
  Separate "fast" (τ < λ) and "slow" (τ > λ) modes.
  Integrate out fast modes exactly (Gaussian system → exact).
  Extract effective kernel K_eff(t) for slow modes.

OBSERVABLES:
  - K_eff shape (exponential? multi-exponential? power-law?)
  - Effective τ_eff and how it depends on the cutoff λ
  - Memory depth: ∫₀^∞ t |K(t)| dt / ∫₀^∞ |K(t)| dt
  - Markovian closure error: ||K_eff − K₁||₂ / ||K_eff||₂

ASSUMPTIONS:
  - Linear coupling (Gaussian system → exactly solvable)
  - No gravity (flat space, no curvature coupling)
  - Fixed timescale distribution p(τ)

EXPECTED SIGNATURES:
  If p(τ) is narrowly distributed: K_eff ≈ K₁ (Markovian)
  If p(τ) is broadly distributed: K_eff ≈ K₂ or K₃ (multi-exponential or power-law)
  If p(τ) ~ τ^{−γ} (power-law): K_eff ~ K₃ (fractional/long memory)
```

### M2: Mesoscopic entropy-density transport

```
MODEL: 1D entropy-density field s(x,t) with local production and diffusion.
  ∂s/∂t = D_s ∂²s/∂x² + (s_eq − s)/τ(x) + σ(x) ξ(x,t)
  where τ(x) varies spatially (multi-scale environment)

  Coarse-grain: average s over blocks of size L.
  Extract effective dynamics for the coarse-grained s̄(X, t).

OBSERVABLES:
  - Effective relaxation kernel K_L(t) at scale L
  - How K_L changes as L increases (RG flow)
  - Whether K_L → K₁ at large L (Markovian attractor?)

ASSUMPTIONS:
  - H4 identification: s = entropy density
  - Local equilibrium: s_eq(x) varies slowly
  - τ(x) is random (quenched disorder) or structured

EXPECTED SIGNATURES:
  If τ(x) = const: K_L = K₁ for all L (trivially Markovian)
  If τ(x) is random with finite variance: K_L → K₁ at large L (CLT averaging)
  If τ(x) has long-range correlations or heavy-tailed distribution: K_L develops
    non-Markovian tails (anomalous transport / fractional dynamics)
```

### M3: Curvature-coupled effective model

```
MODEL: Entropy-density field on a curved background with X = β + αR.
  τ(g) u^μ ∇_μ s + s = s_eq(R)
  τ(g) = τ₀ + τ₁ R + ...  (curvature-dependent relaxation)

  In a multi-scale gravitational environment (e.g., galaxy with
  varying curvature from center to outskirts), coarse-grain over
  curvature fluctuations.

OBSERVABLES:
  - Effective kernel for the curvature-averaged dynamics
  - Whether curvature fluctuations generate memory
  - Spectral index of the effective bath

ASSUMPTIONS:
  - H4 identification (F2-B)
  - Weak curvature (controlled regime)
  - τ(g) variation is perturbative (δτ₁ R << τ₀)

EXPECTED SIGNATURES:
  If curvature is slowly varying: Markovian to leading order (adiabatic)
  If curvature fluctuates on timescale ~ τ₀: resonance / memory effects
  If curvature has spatial structure at multiple scales: multi-exponential kernel
```

---

## 4. Memory Diagnostics

### D1: Kernel shape K(Δt)

```
Definition: The retarded response function of the coarse-grained system.

K(Δt) = response of x_slow(t + Δt) to a unit impulse in F_eff at time t.

Measured by: impulse-response computation (numerical) or Green's function
extraction (analytical, for Gaussian systems).

Classification:
  K₁ if K ~ exp(−Δt/τ_eff)         → MARKOVIAN
  K₂ if K ~ Σ aᵢ exp(−Δt/τᵢ)      → FINITE MEMORY (n timescales)
  K₃ if K ~ Δt^{−α}                → LONG MEMORY (power-law)
  K₄ if K ~ exp(−Δt/τ) cos(ωΔt)   → UNDERDAMPED MEMORY
```

### D2: Effective memory depth

```
Definition: M_eff = ∫₀^∞ Δt |K(Δt)| dΔt / ∫₀^∞ |K(Δt)| dΔt

Interpretation:
  M_eff = τ_eff  for K₁ (exponential: memory depth = relaxation time)
  M_eff = max(τᵢ) for K₂ (multi-exponential: longest timescale dominates)
  M_eff = ∞ for K₃ (power-law: infinite memory)
  M_eff ~ τ for K₄ (oscillatory envelope)
```

### D3: Markovian closure error

```
Definition: ε_M = ||K_eff − K₁_best||₂ / ||K_eff||₂

where K₁_best = best-fit single exponential to K_eff.

Interpretation:
  ε_M < 0.05: effectively Markovian (< 5% non-Markovian content)
  0.05 < ε_M < 0.3: moderately non-Markovian
  ε_M > 0.3: strongly non-Markovian
```

### D4: Spectral index

```
Definition: Fit the noise spectral density J(ω) = η ω^s at low frequency.

  s = 1: Ohmic (Markovian-compatible)
  s < 1: sub-Ohmic (long-memory bath)
  s > 1: super-Ohmic (short-memory bath, Markovian better justified)

Measured from: the Fourier transform of the noise autocorrelation.
```

### D5: RG flow indicator

```
Definition: Track (τ_eff, ε_M, s) as a function of the coarse-graining
scale λ or block size L.

RG attractor test:
  If (τ_eff, ε_M) → (τ_∗, 0) as λ → ∞: Markovian is an IR attractor.
  If ε_M → const > 0 as λ → ∞: memory is persistent (not removable by coarse-graining).
  If ε_M grows with λ: coarse-graining GENERATES memory (Markovian is UV, not IR).
```

---

## 5. Success/Failure Criteria

| Token | Objective criteria |
|-------|-------------------|
| **markovian_attractor_supported** | At M1 and M2 levels: ε_M → 0 as coarse-graining scale λ → ∞ for a broad class of timescale distributions p(τ). The Markovian form K₁ is the generic IR limit. Spectral index s → 1 at large λ. Must hold for at least 2 of the 3 model levels (M1, M2, M3). |
| **memory_kernels_generic** | At M1 and M2 levels: ε_M → const > 0 or ε_M grows with λ for a broad class of p(τ). Non-Markovian tails persist or emerge under coarse-graining. K₂ or K₃ are the generic IR forms, not K₁. Must hold for at least 2 of 3 model levels. |
| **regime_split** | Markovian form is the IR attractor ONLY in a restricted regime (e.g., narrowly distributed p(τ), or slowly varying τ(x), or s > 1 bath). Outside this regime, memory is generic. Both Markovian and non-Markovian regions are explicitly characterized. |
| **blocked** | The model ladder cannot be executed (e.g., M1 is not exactly solvable, M2 requires numerics beyond scope, M3 requires strong-field input). |

---

## 6. Claim Policy

### Allowed during Program G

| # | Claim | Condition |
|---|-------|-----------|
| GA1 | "Under coarse-graining of model M_n, the effective kernel is K_class." | Must have explicit computation (analytical or numerical) at the stated model level. |
| GA2 | "The Markovian closure error is ε_M = value at scale λ." | Must have explicit computation. |
| GA3 | "The Markovian form is/is not an IR attractor for model class M_n." | Must have RG flow evidence (ε_M vs λ curve or analytical argument). |
| GA4 | "Memory kernels of class K_n are generically generated for timescale distribution p(τ)." | Must have explicit computation for at least 3 choices of p(τ). |

### Forbidden during Program G

| # | Claim | Reason |
|---|-------|--------|
| GF1 | "The Markovian constitutive law is universally valid at all scales." | Requires multi-level closure proof (not a single-model result). |
| GF2 | "GRUT is a universal theory because the Markovian form is an attractor." | Even if Markovian is an attractor, GRUT is non-unique (E3, D1). Stability ≠ uniqueness. |
| GF3 | "Memory effects are negligible." | Must be demonstrated, not assumed. ε_M must be computed. |
| GF4 | Any ToE claim. | Perpetually forbidden. |
| GF5 | Any retroactive upgrade of F3 conclusion (repackaging). | F3 is closed. Program G asks a different question (stability, not novelty). |
| GF6 | "The non-Markovian extension is GRUT-specific." | Non-Markovian transport is generic to all dissipative systems. |

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **G0-G1** | Scope and non-goals explicit | **PASS** | Section 1: technical identity, separation from F and E, five non-goals listed. |
| **G0-G2** | Core questions formally stated | **PASS** | Section 2: Q1 (Markovian closure), Q2 (kernel classification), Q3 (attractor status). Each with formal setup and possible outcomes. |
| **G0-G3** | Model ladder executable | **PASS** | Section 3: M1 (toy OU system, exactly solvable), M2 (entropy-density transport, numerically tractable), M3 (curvature-coupled, perturbative). Observables and expected signatures for each. |
| **G0-G4** | Diagnostics mathematically defined | **PASS** | Section 4: D1-D5, each with definition, measurement method, and interpretation thresholds. |
| **G0-G5** | Exit-token criteria operational | **PASS** | Section 5: four tokens with objective criteria (ε_M behavior, model-level requirements). |

## Decision Token

### **charter_frozen**

**Rationale:** All five gates pass. The charter defines a self-contained computation/theorem program testing the RG stability of the Markovian constitutive law. Three model levels, five diagnostics, four exit tokens, six forbidden claims. No GRUT-specific content imported. No ToE claim. Executable starting at M1 (exactly solvable Gaussian system).

**Program G may begin at Stage G1: M1 Computation (Toy Microdynamics Coarse-Graining).**

---

*Program G Stage G0 complete. Decision: charter_frozen. Three core questions (Q1: Markovian closure, Q2: kernel classification, Q3: attractor status). Three model levels (M1: toy OU, M2: entropy transport, M3: curvature-coupled). Five diagnostics (kernel shape, memory depth, closure error, spectral index, RG flow). Four exit tokens. Six forbidden claims. Gates: 5/5 pass.*
