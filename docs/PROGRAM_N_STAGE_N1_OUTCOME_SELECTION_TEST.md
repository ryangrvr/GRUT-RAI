# Program N — Stage N1: Unitary-Constitutive Coupled Dynamics and Outcome Selection Test

**No imported assumptions.** Starting from unitary quantum evolution + constitutive coupling. Testing whether the coupled system dynamically produces branch instability, single-outcome stabilization, and |ψ|² statistics.

---

## Test Results

### Test A: Diagonal coupling (σ_z), no noise

**Setup:** |ψ⟩ = (|0⟩ + |1⟩)/√2, H_eff = diag(E₀ + λΦ, E₁ − λΦ), constitutive τ dΦ/dt + Φ = X₀ρ₀₀ + X₁ρ₁₁.

**Result:** Populations are EXACTLY constant (ρ₀₀ = 0.5 throughout). The diagonal Hamiltonian preserves populations under unitary evolution. Φ relaxes to X_mean = (X₀ + X₁)/2 = 0. Coherence oscillates (phase precession) but does not decay.

**Branch instability: NO. Selection: NO.**

### Test A2: Non-diagonal coupling (σ_x), no noise

**Setup:** Same, but H_eff = diag(E₀, E₁) + λΦ σ_x. This allows Φ-dependent transitions.

**Result:** Population range: 0.500 to 0.500 — no oscillation with these parameters (the coupling is too weak relative to the energy splitting, or the Phi feedback suppresses it). Conservative dynamics: no settling.

**Branch instability: MINIMAL. Selection: NO (no damping).**

### Test B/C: σ_x coupling WITH noise

**Setup:** D = 0.3, 200 ensemble members, T = 20, dt = 0.02. Scan over initial |c₀|² from 0.1 to 0.9.

| |c₀|² | frac(outcome 0) | delta |
|:-----:|:---:|:---:|
| 0.1 | 0.000 | −0.100 |
| 0.2 | 0.255 | +0.055 |
| 0.3 | 0.455 | +0.155 |
| 0.5 | 0.525 | +0.025 |
| 0.7 | 0.505 | −0.195 |
| 0.8 | 0.680 | −0.120 |
| 0.9 | 1.000 | +0.100 |

**The outcome fractions do NOT match the Born rule.** The deltas are large (up to 0.195) and show no systematic relationship to |c₀|². The mean absolute delta is ~0.11 — far from the < 0.05 threshold for Born-rule emergence.

**Born rule: DOES NOT EMERGE from mean-field constitutive coupling with noise.**

---

## Structural Diagnosis

### Why the mean-field coupling fails

The constitutive field Φ couples to the AVERAGE quantum state:

```
X = X₀ ρ₀₀ + X₁ ρ₁₁
```

This means Φ sees the POPULATION-WEIGHTED AVERAGE, not the individual branches. When ρ₀₀ = 0.5 (equal superposition), Φ relaxes to (X₀ + X₁)/2 — the midpoint. It has no information about WHICH branch is "more real." The constitutive field responds to the statistical mixture, not to the quantum superposition.

### Why linear constitutive dynamics cannot select

The linear constitutive law τ dΦ/dt + Φ = X has ONE attractor: Φ* = X. For an equal superposition: X = (X₀ + X₁)/2. There is ONE target, not two. The constitutive field AVERAGES over branches rather than selecting one.

For SELECTION (ρ₀₀ → 0 or 1): the constitutive dynamics would need TWO attractors — one at X₀ (for branch |0⟩) and one at X₁ (for branch |1⟩). This requires BISTABILITY: a nonlinear constitutive landscape with two basins.

### The structural requirement for outcome selection

```
LINEAR constitutive law:
  One attractor → one equilibrium → NO SELECTION
  (averaging, not choosing)

BISTABLE constitutive law:
  Two attractors → two basins → POTENTIAL SELECTION
  (but requires mechanism to route each outcome to a basin)

QUANTUM-CONSTITUTIVE BISTABILITY:
  The quantum superposition creates two branches, each with its own X(g_i).
  If the constitutive landscape is bistable with basins centered at X(g₀)
  and X(g₁), the noise-driven Φ FALLS INTO ONE BASIN — selecting that branch.
  The PROBABILITY of falling into basin i would depend on the basin structure,
  which is determined by the quantum amplitudes through the coupling.
```

This is the GRUT-II Nu architecture (from Book C): the coupled (Φ, Ψ) system with cubic saturation can have two stable fixed points. The connection to outcome selection is: the quantum superposition creates the two attractors, and the constitutive noise drives the system into one.

### But: does the basin probability match |c_i|²?

This is the question N2-N4 would test — IF the bistable constitutive dynamics is set up. The linear N1 test shows that WITHOUT bistability, there is no selection mechanism at all. The Born-rule question only becomes meaningful once selection exists.

---

## What N1 Establishes

| Question | Answer |
|----------|--------|
| Does linear constitutive coupling produce branch instability? | **NO** (diagonal) / **MINIMAL** (σ_x) |
| Does it produce single-outcome stabilization? | **NO** (one attractor = averaging, not selecting) |
| Does it produce |ψ|² statistics? | **NO** (outcome fractions do not match Born rule) |
| What structural ingredient is MISSING? | **BISTABILITY** — two attractors, one per quantum branch |
| Where does this exist in the GRUT program? | GRUT-II Nu / Book C (coupled (Φ,Ψ) with cubic saturation) |

---

## The Path Forward (N2)

N1 has identified the precise structural requirement: **quantum-constitutive bistability.** The linear L1 law CANNOT select outcomes. The nonlinear (Φ,Ψ) coupled system from GRUT-II Nu CAN have two attractors.

N2 should test: if the quantum superposition creates a bistable constitutive landscape (two attractors, one per branch), does the noise-driven basin selection reproduce the Born rule? This requires:

1. Formulating the (Φ,Ψ) coupled constitutive dynamics with quantum-branch-dependent targets
2. Computing the basin volumes / noise-driven selection probabilities
3. Checking whether p(basin i) = |c_i|² for all initial amplitudes

This is the test of whether BISTABILITY + NOISE = BORN RULE. It cannot be done at the linear mean-field level (N1 proved this). It requires the full nonlinear constitutive dynamics.

---

*Program N Stage N1 complete. Linear mean-field constitutive coupling: NO branch selection, NO Born rule. The structural requirement is BISTABILITY — two constitutive attractors, one per quantum branch. Linear L1 has one attractor (averaging). Nonlinear (Φ,Ψ) from GRUT-II Nu has two (potential selection). N2: test bistable constitutive selection with quantum-branch-dependent attractors.*
