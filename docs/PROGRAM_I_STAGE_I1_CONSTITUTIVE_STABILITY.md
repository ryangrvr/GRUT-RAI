# Program I — Stage I1: Constitutive Stability Under Microscopic O(κ₀) Error

**Predecessor:** H3 (intermediate_followup_needed, δκ/κ ≈ 2% at κ₀ = 0.10). G2-A (Markovian validity: W_τ* = 0.7 decades).

---

## Results

### Perturbation channels (H3-calibrated: δ = 0.21 × κ₀/k_F)

| Channel | Mechanism | Form impact | Attractor | Stability |
|:-------:|-----------|:-----------:|:---------:|:---------:|
| **P1** (τ → τ(1+δ)) | Relaxation time shift | **FORM-PRESERVING** | Φ* = X (unchanged) | Preserved |
| **P2** (D → D(1+δ)) | Noise amplitude shift | **FORM-PRESERVING** | Φ* = X (unchanged) | Preserved |
| **P3** (memory kernel) | τΦ̇ + Φ + λ∫KΦ = X | **WEAKLY DEFORMED** | Φ* = X/(1+λ) (shifted) | Preserved |

### Sensitivity map at κ₀/k_F = 0.10

| Output | P1 drift | P2 drift | P3 drift |
|--------|:--------:|:--------:|:--------:|
| Equilibrium Φ* | 0.00% | 0.00% | **2.06%** |
| Relaxation timescale | **2.10%** | 0.00% | modified (2nd-order) |
| Fluctuation variance | 0.00% | **2.10%** | open |

### Structural invariant survival

| Invariant | P1 | P2 | P3 | Survives all? |
|-----------|:--:|:--:|:--:|:---:|
| Unique attractor | ✓ | ✓ | ✓ (shifted) | **YES** |
| Monotone relaxation | ✓ | ✓ | ✓ (both eigenvalues real, negative) | **YES** |
| Bounded response | ✓ | ✓ | ✓ | **YES** |
| CTP positivity | ✓ | ✓ | OPEN | **OPEN** |
| Exponential semigroup | ✓ | ✓ | **FAILS** (2nd-order system) | **NO** |

### Regime robustness

| Regime | P1 | P2 | P3 | Overall |
|--------|:--:|:--:|:--:|:-------:|
| **R1** (W_τ < 0.7, Markov-valid) | FORM-PRESERVING | FORM-PRESERVING | Weakly deformed (< 1% at κ₀ ≤ 0.10) | **STABLE** |
| **R2** (0.7 < W_τ < 1.8, marginal) | FORM-PRESERVING | FORM-PRESERVING | Weakly deformed (few % corrections) | **MARGINAL** |

---

## Uncertainty Budget (at κ₀/k_F = 0.10, Markov-valid regime)

| Source | Output affected | Uncertainty |
|--------|----------------|:-----------:|
| P1 (τ renormalization) | Relaxation timescale | ±2.1% |
| P2 (noise coefficient) | Fluctuation variance | ±2.1% |
| P3 (memory kernel) | Equilibrium value | ±2.1% |
| P3 (memory kernel) | Transient shape | ~few % |
| **TOTAL (quadrature)** | **Combined** | **±3.6%** |

---

## Classification

### **stable_with_corrections**

The constitutive law τ dΦ/dt + Φ = X(g) is structurally stable under all three H3-calibrated perturbation channels:

1. **P1 and P2 are exactly form-preserving.** They shift parameters (τ, D) without modifying the equation's structure. The attractor, semigroup, and all invariants are unchanged.

2. **P3 weakly deforms the form.** The memory kernel converts the 1st-order ODE to a coupled 2nd-order system. The exponential semigroup is lost. But: the attractor remains unique and stable, monotone relaxation is preserved, bounded response is preserved, and the deformation is O(κ₀) — perturbatively small.

3. **The total uncertainty budget is ±3.6%** at κ₀/k_F = 0.10 in the Markov-valid regime. This is well within the "intermediate" zone from H3 and does not compromise qualitative predictions.

4. **One invariant fails (semigroup)** and **one is open (CTP positivity under memory).** These are structural consequences of the memory correction and would need to be addressed if precision constitutive dynamics (< 1% accuracy) is required.

### Practical recommendation

- **Qualitative work:** Use the Markovian constitutive law as-is. The ±2-4% systematic is below typical modeling uncertainties.
- **Precision work (< 1%):** Include P3 memory corrections at O(κ₀), or accept the systematic as a documented uncertainty.
- **Strong coupling (κ₀/k_F > 0.10):** Memory corrections exceed ~4% and grow linearly. Parquet-level treatment recommended.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **I1-G1** | P1-P3 executed | **PASS** | All three channels computed with H3-calibrated perturbations across κ₀ ∈ [0.01, 0.10]. |
| **I1-G2** | Form-stability classification | **PASS** | P1: form-preserving. P2: form-preserving. P3: weakly deformed. Combined: stable_with_corrections. |
| **I1-G3** | Regime-tagged robustness | **PASS** | R1 (Markov-valid): stable (< 1% corrections). R2 (marginal): weakly deformed (few % corrections). R3: excluded. |
| **I1-G4** | Invariant survival table | **PASS** | 3/5 survive all channels. 1 fails (semigroup under P3). 1 open (CTP positivity under P3). |
| **I1-G5** | Uncertainty budget | **PASS** | ±3.6% total at κ₀ = 0.10. Decomposed by channel and output. Practical recommendation issued. |

## Decision Token

### **stable_with_corrections**

The constitutive structure survives H3-calibrated microscopic uncertainty. The law is form-preserving under parameter shifts (P1, P2) and weakly deformed under memory corrections (P3). The attractor, monotonicity, and boundedness are preserved. The semigroup is lost under P3 but the replacement dynamics is stable. The total uncertainty budget is ±3.6% — manageable and documented.

---

*Program I Stage I1 complete. Decision: stable_with_corrections. P1 (τ shift): form-preserving. P2 (D shift): form-preserving. P3 (memory): weakly deformed (2nd-order, Φ* shifted by 2.1%, semigroup lost). 3/5 invariants survive all channels. Total uncertainty: ±3.6% at κ₀ = 0.10. Constitutive law is structurally stable in the Markov-valid regime. Gates: 5/5 pass.*
