# Program N — Stage N3: Full CTP Branch-Specific Coupling

---

## The Three-Stage Arc

| Stage | Model | Selection? | Born rule? |
|:-----:|-------|:----------:|:----------:|
| N1 | Linear mean-field | NO | NO |
| N2 | Bistable mean-field | YES (50/50) | NO (δ up to 0.55) |
| **N3** | **Full CTP branch-specific** | **YES (by construction)** | **PRESERVED, not derived** |

---

## The N3 Structural Result

### The CTP diagonal constraint (U1)

The CTP effective action satisfies S_eff[r, a=0] = 0 (Book A, unitarity condition U1). For the diagonal density matrix elements (branch probabilities): Φ₊ = Φ₋ → the CTP weight is exp(iS/ℏ − iS/ℏ) = 1.

**The CTP formalism assigns UNIT WEIGHT to every diagonal element.** It does not determine branch probabilities — those come from the quantum amplitudes |cᵢ|² as initial conditions.

### The partition-function analysis

The total probability of outcome i is:

```
p(i) = |cᵢ|² × Z_constitutive(X_i) / Σⱼ |cⱼ|² Z_constitutive(X_j)
```

For the **LINEAR** constitutive law: Z is a Gaussian functional integral whose kernel depends on τ and D but NOT on X. Therefore Z(X₀) = Z(X₁) exactly. The Born rule is exactly preserved: p(i) = |cᵢ|².

For the **NONLINEAR** (bistable) constitutive law: Z(X) depends on the attractor structure. But with symmetric branch targets (X₀ = −X₁ = 2.0): the Z₂ symmetry of the landscape gives Z(X₀) = Z(X₁) = 0.5836... exactly. The Born rule is again preserved.

### Numerical verification

| |c₀|² | Born pred | Z₀ | Z₁ | p_corrected | delta |
|:-----:|:---------:|:--:|:--:|:-----------:|:-----:|
| 0.10 | 0.100 | 0.5836 | 0.5836 | 0.100000 | 0.000000 |
| 0.30 | 0.300 | 0.5836 | 0.5836 | 0.300000 | 0.000000 |
| 0.50 | 0.500 | 0.5836 | 0.5836 | 0.500000 | 0.000000 |
| 0.70 | 0.700 | 0.5836 | 0.5836 | 0.700000 | 0.000000 |
| 0.90 | 0.900 | 0.5836 | 0.5836 | 0.900000 | 0.000000 |

**Born rule preserved to machine precision across all amplitudes.** Zero correction from the constitutive sector.

---

## The Structural Theorem

```
THEOREM (Constitutive Born-Rule Transparency):

For a quantum system |ψ⟩ = Σ cᵢ |i⟩ coupled to a constitutive field Φ
with branch-specific targets Xᵢ:

  LINEAR constitutive law:
    Z(Xᵢ) = Z (independent of X, Gaussian kernel)
    p(i) = |cᵢ|² exactly

  NONLINEAR with symmetric targets (Xᵢ = -Xⱼ):
    Z(Xᵢ) = Z(Xⱼ) (Z₂ symmetry)
    p(i) = |cᵢ|² exactly

  NONLINEAR with asymmetric targets:
    Z(Xᵢ) ≠ Z(Xⱼ) in general
    p(i) = |cᵢ|² × Z(Xᵢ) / Σ |cⱼ|² Z(Xⱼ)
    Born rule receives O(ΔZ/Z) corrections

In all cases: the Born rule |cᵢ|² enters as a QUANTUM INITIAL CONDITION.
The constitutive sector TRANSMITS it (preserves or slightly modifies)
but does NOT GENERATE it.
```

---

## What This Means

### The constitutive sector is TRANSPARENT to the Born rule

The Born rule is a property of the QUANTUM path integral — the unitary evolution that created the superposition. The constitutive sector is a POST-QUANTUM process: it provides the physical mechanism for outcome selection (bistability + noise → basin selection) but the PROBABILITIES of each outcome are set by the quantum amplitudes, not by the constitutive dynamics.

This is structurally analogous to a coin flip: the mechanism of the flip (constitutive dynamics) determines that ONE outcome occurs, but the probability of heads vs tails (Born rule) is set by the initial conditions (quantum amplitudes), not by the flip dynamics.

### The Born rule CANNOT be derived from constitutive dynamics

This is the definitive negative result of Program N:

- N1: Linear constitutive → no selection mechanism at all
- N2: Bistable constitutive → selection mechanism exists, but produces ~50/50 (wrong statistics)
- N3: Full CTP analysis → the Born rule enters as |cᵢ|² from the quantum sector; the constitutive sector transmits it with unit Z-factor ratio

At no level does the constitutive sector GENERATE the Born rule. The quantum sector provides it; the constitutive sector preserves it.

### Implication for the ToE quantum-closure gates

| Gate | Status after N3 |
|:----:|:---:|
| G2 (Born rule) | **CANNOT be derived from constitutive dynamics.** The Born rule is upstream of the constitutive sector. It must be imported from the quantum sector (IA-2 from Program E). |
| G4 (ℏ emergence) | **UNCHANGED (FAILED from L1).** N3 does not involve ℏ in the constitutive sector. |
| G1 (de Broglie) | Still untested. |
| G3 (Bell) | Still untested. |

### The honest conclusion of Program N

**The constitutive sector provides the MECHANISM of outcome selection (bistability + noise → definite outcome) but NOT the PROBABILITY RULE (Born rule).** The mechanism and the rule are STRUCTURALLY INDEPENDENT: the mechanism is constitutive, the rule is quantum.

This means the "qualitatively new structural ingredient" for ToE closure cannot be found within the constitutive sector. The constitutive sector is necessary (it provides the physical measurement mechanism) but not sufficient (it does not derive the Born rule or ℏ). The quantum sector must be imported as an independent structure.

**Program N is closed.**

---

*Program N Stage N3 complete. Token: born_rule_upstream_of_constitutive. The Born rule is PRESERVED by the constitutive sector (Z₀ = Z₁ for linear and symmetric-nonlinear cases) but NOT DERIVED from it. The constitutive sector provides the outcome-selection MECHANISM (bistability + noise) but not the probability RULE (|cᵢ|²). The Born rule is a quantum input, not a constitutive output. This is the definitive structural boundary of the program. Gates G2 and G4 remain failed/unreachable from the constitutive sector. Program N closed.*
