# Program N — Stage N2: Bistable Quantum-Constitutive Selection and Born Rule Test

---

## Results

### Branch instability and single-outcome selection: YES

The bistable (Φ, Ψ) system with quantum-branch-dependent sources DOES produce:

1. **Two attractors** across the bistable range (X ∈ [−1.6, 1.6] for these parameters)
2. **Noise-driven basin selection** — each stochastic trajectory settles into one attractor
3. **Near-perfect 50/50 split** at equal superposition (X = 0): 0.507/0.493

**The constitutive dynamics selects outcomes.** This is the first time in the entire program that a definite outcome (one attractor, not a mixture) emerges from the quantum-constitutive coupling.

### Born rule: DOES NOT EMERGE

| |c₀|² | X_source | #FPs | frac(0) | Born pred | delta |
|:-----:|:--------:|:----:|:-------:|:---------:|:-----:|
| 0.05 | −1.80 | 1 | 0.000 | 0.050 | −0.050 (monostable) |
| 0.10 | −1.60 | 2 | **0.593** | 0.100 | **+0.493** |
| 0.20 | −1.20 | 2 | 0.600 | 0.200 | +0.400 |
| 0.30 | −0.80 | 2 | 0.570 | 0.300 | +0.270 |
| 0.40 | −0.40 | 2 | 0.537 | 0.400 | +0.137 |
| **0.50** | **0.00** | **2** | **0.502** | **0.500** | **+0.002** |
| 0.60 | +0.40 | 2 | 0.463 | 0.600 | −0.137 |
| 0.70 | +0.80 | 2 | 0.415 | 0.700 | −0.285 |
| 0.80 | +1.20 | 2 | 0.407 | 0.800 | −0.393 |
| 0.90 | +1.60 | 2 | 0.352 | 0.900 | −0.548 |
| 0.95 | +1.80 | 1 | 1.000 | 0.950 | +0.050 (monostable) |

**Mean |δ| = 0.25. Max |δ| = 0.55.** Far from the Born rule.

### The pattern: frac(0) ≈ 0.5 everywhere (not |c₀|²)

The basin selection is nearly SYMMETRIC (~50/50) across the entire bistable range, regardless of |c₀|². At |c₀|² = 0.1 (should be 10/90): the system gives 59/41. At |c₀|² = 0.9 (should be 90/10): it gives 35/65.

**The constitutive dynamics knows the system is bistable but does NOT know the quantum amplitudes.** The basin fractions are determined by the CONSTITUTIVE LANDSCAPE (attractor positions, basin boundaries, noise amplitude), not by the quantum state.

### Why the Born rule fails

The quantum amplitudes enter the constitutive dynamics ONLY through:

```
X_source = X_branch_0 × |c₀|² + X_branch_1 × |c₁|²
```

This shifts the ENTIRE constitutive landscape (both attractors move). But the BASIN BOUNDARY — which determines the selection probability — does not shift LINEARLY with |c₀|². The basin boundary is determined by the SADDLE POINT between the two attractors, which is a nonlinear function of X_source.

For the Born rule to emerge: the basin boundary would need to shift such that the fraction of initial conditions falling into basin 0 equals exactly |c₀|². This would require a SPECIFIC RELATIONSHIP between the nonlinear (Φ, Ψ) dynamics and the quantum amplitudes — a relationship that is NOT present in the current model.

### Noise-independence test

At |c₀|² = 0.3 (Born prediction: 0.3):

| D | frac(0) | delta |
|:-:|:-------:|:-----:|
| 0.05 | 0.797 | +0.497 |
| 0.10 | 0.743 | +0.443 |
| 0.50 | 0.563 | +0.263 |
| 2.00 | 0.517 | +0.217 |

The basin fraction VARIES with D (noise amplitude). It approaches 0.5 (symmetric) as D increases (strong noise washes out the landscape asymmetry). The Born rule value 0.3 is never reached at any D.

**The selection is noise-dependent, not Born-rule-universal.** This disqualifies the mechanism as a Born-rule derivation even in principle: a genuine Born rule must be independent of the noise amplitude.

---

## Structural Diagnosis

### What works

1. **Bistable constitutive dynamics produces definite outcomes.** The stochastic (Φ, Ψ) system falls into one of two basins. Each run gives a specific attractor — not a mixture.

2. **The symmetry point works perfectly.** At |c₀|² = 0.5 (equal superposition, X = 0): the system gives 50.2/49.8 — consistent with the Born rule. The symmetric case is trivial (equal basins → equal probability).

3. **The monostable endpoints work.** At |c₀|² = 0.05 and 0.95: the system is monostable (only one attractor exists), and the outcome is determined (0 or 1). This is correct: near a pure state, the constitutive landscape has only one minimum.

### What fails

**The intermediate amplitudes.** At |c₀|² = 0.3 (say): the Born rule predicts 30/70. The constitutive dynamics gives ~57/43. The basin structure is too symmetric — the landscape responds weakly to the amplitude asymmetry.

**Root cause:** The mean-field coupling X = Σ cᵢ² Xᵢ shifts the ENTIRE landscape, but the basin VOLUMES do not track the amplitudes linearly. The basin volumes are determined by the TOPOLOGY of the bistable landscape (positions and curvatures of the two attractors and the saddle point), which is a nonlinear function of X_source.

### The fundamental structural gap

The Born rule requires:

```
p(outcome i) = |cᵢ|²
```

The bistable constitutive dynamics produces:

```
p(outcome i) = f(basin_structure(X_source))
```

where f is determined by the constitutive nonlinear dynamics and the noise. For the Born rule to emerge: f must EQUAL the identity function on |cᵢ|². This is a CONSTRAINT on f — equivalently, a constraint on the constitutive potential V(Φ, Ψ) and the coupling X(quantum state).

**The current model does not satisfy this constraint.** The basin volumes do not track the amplitudes. The mechanism produces outcomes but not the RIGHT DISTRIBUTION of outcomes.

---

## What This Means

### For the program

N2 has demonstrated the FIRST HALF of outcome selection:
- ✓ Branch instability (bistability creates two attractors)
- ✓ Single-outcome stabilization (noise drives into one basin)
- ✗ Born-rule statistics (basin fractions ≠ |cᵢ|²)

The missing ingredient is now sharper than before: it is NOT "a selection mechanism" (that exists). It is the SPECIFIC CONSTRAINT that makes basin volumes proportional to |cᵢ|².

### For a potential N3

The Born rule could still emerge if:
1. The coupling is NOT mean-field (X ≠ Σ cᵢ² Xᵢ) but rather BRANCH-SPECIFIC (each branch sees its own constitutive field — requiring full CTP, not mean-field)
2. The constitutive potential is TUNED so that basin volumes track amplitudes (but this would be inserting the Born rule, not deriving it)
3. There is a DEEPER principle (beyond the constitutive EFT) that constrains the basin structure to match quantum amplitudes

Option 1 is the most promising — it requires going beyond mean-field to the FULL CTP path integral where Φ₊ and Φ₋ on the two CTP branches evolve independently, coupled only through the influence functional. This is a qualitatively different computation from mean-field, and it is the natural next step.

Option 3 would be the qualitatively new structural ingredient — but we don't have it yet.

---

*Program N Stage N2 complete. Bistable constitutive dynamics produces DEFINITE OUTCOMES (branch selection) but NOT Born-rule statistics (basin fractions ≈ 0.5, not |cᵢ|²). Mean |δ| = 0.25. The basin structure is too symmetric: it responds weakly to quantum amplitude asymmetry through the mean-field coupling. Noise-dependence: selection fractions vary with D (not universal). The Born rule is NOT a generic property of bistable constitutive dynamics with mean-field quantum coupling. The gap: basin volumes do not track amplitudes. The next step (N3): test whether FULL CTP branch-specific coupling (not mean-field) changes the picture.*
