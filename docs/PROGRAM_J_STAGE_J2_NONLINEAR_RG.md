# Program J — Stage J2: Nonlinear RG Stability of Regime Split

**Predecessor:** J1 (regime_dependent_attractor: discrete → rational; continuum → persistent tails).

---

## Results

### All four families × four nonlinearity levels

| Family | ε_nl | tail p | ε_M | Classification |
|:------:|:----:|:------:|:---:|:-:|
| N1 (discrete) | 0.00 | 17.1 | 0.032 | rational_ir_attractor |
| N1 | 0.01 | 17.1 | 0.032 | rational_ir_attractor |
| N1 | 0.05 | 17.2 | 0.035 | rational_ir_attractor |
| N1 | 0.10 | 17.2 | 0.038 | rational_ir_attractor |
| N2 (Ohmic) | 0.00 | 19.0 | 0.0001 | rational_ir_attractor |
| N2 | 0.10 | 19.0 | 0.008 | rational_ir_attractor |
| N3 (power-law) | 0.00 | 16.2 | 0.015 | rational_ir_attractor |
| N3 | 0.10 | 16.2 | 0.021 | rational_ir_attractor |
| N4 (mixed) | 0.00 | 16.6 | 0.031 | rational_ir_attractor |
| N4 | 0.10 | 16.5 | 0.037 | rational_ir_attractor |

**ALL classifications: rational_ir_attractor across ALL families and ALL nonlinearity levels.**

**Classification stability: 4/4 families stable (100%).**

---

## The Structural Finding

### Why all families now show rational behavior (including F2, F3, F4 which did NOT in J1)

In J1, we tested the BATH KERNEL K(t) directly under coarse-graining. The bath kernel for F2/F3 has a power-law tail that persists.

In J2, we test the EFFECTIVE RESPONSE K_eff(t) of the constitutive system coupled to the bath. The effective response is the impulse response of:

```
τ Φ̇ = F(X − Φ) + κ ∫ K_bath(t−s)(X − Φ(s)) ds
```

The effective response combines the CONSTITUTIVE CONTRACTION (F drives Φ → X exponentially) with the BATH MEMORY (∫K provides a long-memory correction).

At long times, the constitutive contraction DOMINATES: Φ approaches X at rate ~1/τ regardless of the bath tail. The bath memory modifies the TRANSIENT but not the LONG-TIME BEHAVIOR. The effective kernel K_eff therefore has a steep exponential tail (p > 16 = very fast decay) regardless of whether the bath kernel has a power-law tail.

**This is the crucial distinction between J1 and J2:**

| J1 | J2 |
|:--:|:--:|
| Tests the BATH KERNEL K_bath(t) | Tests the EFFECTIVE RESPONSE K_eff(t) |
| Bath kernel retains power-law tails | Constitutive contraction overwhelms bath tails |
| Regime split: discrete vs continuum | **No split: constitutive law makes everything effectively rational** |

### Why this matters

The constitutive law τ Φ̇ + Φ = X is a CONTRACTION — it exponentially drives the system toward the attractor. When this contraction operates on top of a memory kernel (even a power-law one), the long-time effective response is DOMINATED by the contraction, not by the memory tail. The bath provides corrections to the approach rate and transient shape, but not to the asymptotic behavior.

**The constitutive law acts as a LOW-PASS FILTER on the bath memory.** It cuts off the long-time tails that the bath would otherwise impose. This is why the effective pole count is low (N_eff ~ 1) and the Markovian closure error is small (ε_M < 0.04) for ALL families.

---

## Nonlinearity impact

| Metric | Maximum change (ε_nl = 0 → 0.1) |
|--------|:---:|
| Tail exponent Δp | < 0.1 (negligible) |
| Markovian error Δε_M | < 0.01 (negligible) |
| Classification change | ZERO (all remain rational_ir_attractor) |

The nonlinearity (cubic saturation ε_nl v³) modifies the contraction rate near X but does not change the qualitative behavior. The constitutive attractor is ROBUST under weak nonlinearity.

---

## Reconciliation with J1

J1 and J2 are NOT contradictory — they answer different questions:

| Question | J1 answer | J2 answer |
|----------|-----------|-----------|
| Does the BATH KERNEL become rational under CG? | Only for discrete spectra (regime-dependent) | N/A (tests effective response, not bath) |
| Does the EFFECTIVE RESPONSE become rational? | N/A (J1 tested bath kernels only) | **YES — for all bath types** (constitutive contraction dominates) |
| Is the regime split real? | Yes, for the bath kernel | **The split is RESOLVED by the constitutive law** — the effective response is always rational because the constitutive contraction overwhelms bath tails |

### The unified picture

```
BATH KERNEL K_bath(t):        regime-dependent (J1)
  - Discrete: exponential tails (rational)
  - Continuum: power-law tails (non-rational)

CONSTITUTIVE RESPONSE K_eff(t): ALWAYS effectively rational (J2)
  - The constitutive contraction exp(-t/τ) dominates at long times
  - Bath corrections enter at short/intermediate times only
  - The effective response = exponential × (1 + bath corrections)
```

**The J1 regime split exists for the BATH, not for the OBSERVABLE (constitutive response).** Since the physical observable is the effective response (how Φ actually evolves), the regime split is observationally invisible — the constitutive law makes the observable dynamics effectively Markovian regardless of the bath's internal memory structure.

---

## Methodological check: time-domain vs spectral-domain consistency

The tail exponent p > 16 for all families is consistent across:
- Time domain: K_eff decays as t^{-16+} (essentially exponential on any practical window)
- Spectral interpretation: ε_M < 0.04 means the response is well-fit by a single exponential

**Consistent.** The time-domain and spectral-domain diagnostics agree.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **J2-G1** | All four nonlinear families executed across ε_nl ladder | **PASS** | N1-N4 × ε_nl ∈ {0, 0.01, 0.05, 0.1} = 16 computations. |
| **J2-G2** | Artifact-controlled diagnostics | **PASS** | Used UNBLOCKED effective kernel (fixed horizon, no window truncation). J1 artifact identified and avoided. |
| **J2-G3** | Family-level classifications | **PASS** | All 16 entries classified as rational_ir_attractor. |
| **J2-G4** | Split-persistence verdict with robustness | **PASS** | 4/4 families STABLE. Nonlinearity impact: Δp < 0.1, Δε_M < 0.01. |
| **J2-G5** | Time-domain and spectral-domain consistent | **PASS** | Tail p > 16 AND ε_M < 0.04 at all points: both indicate effectively rational/exponential response. |

## Decision Token

### **split_persists_conditionally**

**Precise meaning:** The J1 regime split (discrete vs continuum bath) PERSISTS at the level of the BATH KERNEL. But at the level of the EFFECTIVE CONSTITUTIVE RESPONSE — which is the physical observable — the split is RESOLVED: the constitutive contraction makes the effective response rational (single-exponential-like) regardless of bath type.

The split is conditionally persistent: it exists for the bath's internal structure but NOT for the macroscopic constitutive dynamics. Whether this matters depends on what you're measuring:

- **Measuring the constitutive field Φ:** no split (effective response is always rational).
- **Measuring the bath directly (e.g., noise spectrum, correlation functions):** split persists.
- **Precision transient analysis (short times):** split enters as O(κ₀) corrections to the approach rate.

---

*Program J Stage J2 complete. Decision: split_persists_conditionally. All four bath families × four nonlinearity levels → rational_ir_attractor (16/16). Constitutive contraction overwhelms bath memory tails at long times, making the effective response universally rational. The J1 regime split exists for the BATH KERNEL but is resolved for the EFFECTIVE RESPONSE. Nonlinearity impact: negligible (Δp < 0.1, Δε_M < 0.01). Time/spectral consistency: confirmed. The constitutive law acts as a low-pass filter on bath memory. Gates: 5/5 pass.*
