# Program J — Stage J3: Non-Tautology Validation of Effective Rationalization

**Predecessor:** J2 (split_persists_conditionally: constitutive contraction rationalizes effective response).

---

## Test Results

### Test 1: Constitutive-Operator Ablation

| Operator | tail p | ε_M | Classification |
|:--------:|:------:|:---:|:-:|
| **A) 1st-order contractive** | 14.3 | 0.032 | **rational** |
| **B) Volterra (memory)** | 0.0 | **0.674** | **NON-RATIONAL** |
| **C) 2nd-order local** | 14.0 | 0.110 | **near-rational** |

**Finding:** The Volterra operator (B) does NOT show effective rationalization. Only operators with a contractive attractor (A, C) rationalize the response. This means:

- The rationalization is NOT tautological from the 1st-order form alone — Operator C (2nd-order) also rationalizes.
- The rationalization IS attractor-dependent — it requires a contractive fixed point that dominates long-time behavior.
- Operator B (pure memory convolution without direct restoring force) CANNOT rationalize the bath tail.

**Implication:** J2's "universal effective rationalization" holds for attractor-bearing constitutive operators (L1 and L3/2nd-order), but NOT for pure Volterra memory operators. The result is NOT tautological (it doesn't depend on being first-order) but IS attractor-conditional (it requires a contractive fixed point).

### Test 2: Late-Time Dominance Falsification

50 parameter combinations tested (τ ∈ [0.1, 50], κ ∈ [0.1, 10]).

**Result:** No bath-tail dominance found at ANY tested parameter. The constitutive contraction always dominates the long-time behavior, even at extreme coupling (κ = 10) and slow relaxation (τ = 50).

However: ε_M reaches 0.24 at (τ=50, κ=10) — the effective response is 24% non-Markovian even though it is not bath-tail-dominated. At extreme parameters, the memory correction is large even though the contraction still wins asymptotically.

**Implication:** The constitutive contraction is robust across a WIDE parameter range. Bath-tail dominance would require either κ → ∞ (bath coupling overwhelms constitutive force) or a constitutive operator without a fixed point (Test 1, Operator B).

### Test 3: Observable-Level Invariance

| Observable | Exp bath | PL bath | Ratio | Distinguishable? |
|-----------|:--------:|:-------:|:-----:|:---:|
| Response half-life | 0.650 | 0.677 | 0.96 | MARGINAL (4% difference) |
| Low-freq susceptibility slope | −11.2 | −16.2 | 0.69 | **YES (31% difference)** |
| Memory contribution fraction | 0.230 | 0.073 | 3.13 | **YES (3.1× difference)** |

**Finding:** Despite both having small ε_M (both classified as "effectively rational" by the Markovian-fit metric), the exponential and power-law baths produce **operationally distinguishable** macroscopic observables. The low-frequency susceptibility differs by 31% and the memory contribution fraction by 3.1×.

**Implication:** "Effectively rational ε_M" does NOT mean "indistinguishable." The bath structure leaks through in precision observables even when the impulse response fits well to a single exponential. The Markovian fit captures the DOMINANT timescale but misses the DETAILED frequency structure.

### Test 4: Frequency-Domain Analyticity

| Level | Spectral roughness (Exp bath) | Spectral roughness (PL bath) |
|-------|:---:|:---:|
| Bath kernel | 6.8 | **27.8** (4× rougher) |
| Effective response | 4.1 | 4.4 (similar) |

High-frequency energy fraction: Exp 0.98%, PL 0.90% — virtually identical.

**Finding:** The constitutive operator SMOOTHS the spectral structure. The bath-level branch cut (PL bath 4× rougher) is suppressed in the effective response (roughness equalized). The branch-cut residue is below the spectral resolution at the effective level.

---

## Synthesis

### What the four tests establish together

| Test | Result | What it proves |
|------|--------|---------------|
| **T1 (Ablation)** | Operator B (Volterra) does NOT rationalize | Rationalization requires a CONTRACTIVE ATTRACTOR, not just any first-order structure |
| **T2 (Falsification)** | No bath dominance at any tested (τ, κ) | Constitutive contraction is robust across wide parameter range |
| **T3 (Observables)** | Precision observables DIFFER between bath types | "Effectively rational" ≠ "indistinguishable" — bath structure is detectable |
| **T4 (Spectral)** | Spectral roughness is equalized in K_eff | Branch-cut structure is SUPPRESSED (not eliminated) by the constitutive operator |

### The answer to the tautology question

**The effective rationalization is NOT a tautology.** It is:

1. **Attractor-conditional:** requires a contractive fixed point (L1 or equivalent). The Volterra memory operator without a fixed point does NOT rationalize. This means the rationalization is a genuine property of ATTRACTOR-BEARING constitutive operators, not of all first-order dynamics.

2. **Robust but not absolute:** the contraction dominates the long-time effective response for all tested parameters, but the memory correction is detectable in precision observables (31% susceptibility difference, 3.1× memory fraction difference). The bath structure is SUPPRESSED at the level of the impulse-response fit but VISIBLE at the level of precision measurement.

3. **Spectrally real:** the constitutive operator genuinely smooths the branch-cut structure in the effective response (spectral roughness equalized). This is not a fitting artifact — the branch-cut residue is physically suppressed by the contractive dynamics.

---

## Classification

### **close_J_regime_conditional**

The effective rationalization is:

- **GENUINE** (not tautological): it requires attractor structure, not just first-order form. Operator B disproves tautology.
- **REGIME-CONDITIONAL** (not universal): it holds for attractor-bearing operators (L1, L3) but not for pure Volterra operators (L2 without restoring force). It is robust across a wide parameter range but the bath structure is detectable in precision observables.
- **OPERATIONALLY INCOMPLETE** at the precision level: despite small ε_M, bath types are distinguishable through susceptibility and memory-fraction measurements. The effective rationalization describes the DOMINANT behavior but not the DETAILED structure.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **J3-G1** | Ablation A/B/C completed | **PASS** | Three operators tested against power-law bath. A: rational. B: non-rational. C: near-rational. |
| **J3-G2** | Tail-dominance falsification | **PASS** | 50 (τ, κ) combinations tested. No bath dominance found. ε_M up to 0.24 at extremes. |
| **J3-G3** | Observable comparison | **PASS** | Three observables compared. Two show > 10% difference. Bath types ARE distinguishable. |
| **J3-G4** | Spectral analyticity | **PASS** | Bath-level roughness 4× different. Effective-level roughness equalized. Branch-cut suppressed. |
| **J3-G5** | Classification evidence-backed | **PASS** | Four tests converge: attractor-conditional, regime-robust, precision-distinguishable, spectrally smoothed. |

## Decision Token

### **close_J_regime_conditional**

Program J has answered its core questions:
- J1: Rational response is an IR attractor for discrete spectra (regime-dependent for bath kernels)
- J2: Constitutive contraction rationalizes the effective response for all bath types
- J3: The rationalization is genuine (not tautological), attractor-conditional, and operationally incomplete at precision level

**Program J is closed.**

---

*Program J Stage J3 complete. Decision: close_J_regime_conditional. Ablation: Volterra operator does NOT rationalize (disproves tautology). Falsification: constitutive contraction dominates at all tested parameters. Observables: bath types distinguishable at 31% (susceptibility) and 3.1× (memory fraction) despite similar ε_M. Spectral: branch-cut suppressed (roughness equalized in K_eff). Classification: effective rationalization is genuine, attractor-conditional, and operationally incomplete at precision level. Program J closed. Gates: 5/5 pass.*
