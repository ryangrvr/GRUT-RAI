# Program G — Stage G2-A: Markovian Validity Envelope Mapping

**Predecessor:** G1 (bifurcate_G2, memory_generated for broad τ distributions).

---

## Results

### Phase Diagram

The Markovian closure error ε_M as a function of spectral width W_τ (decades of timescale spread) and number of fast modes N_fast:

| W_τ (decades) | N=1 | N=5 | N=20 | N=100 | Zone |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0.000 | 0.000 | 0.000 | 0.000 | VALID |
| 0.5 | 0.000 | 0.038 | 0.029 | 0.026 | VALID |
| 1.0 | 0.000 | 0.120 | 0.095 | 0.090 | MARGINAL |
| 1.5 | 0.000 | 0.190 | 0.165 | 0.157 | MARGINAL |
| 2.0 | 0.000 | 0.230 | 0.215 | 0.209 | INVALID |
| 3.0 | 0.000 | 0.260 | 0.271 | 0.269 | INVALID |
| 4.0 | 0.000 | 0.276 | 0.318 | 0.321 | INVALID |

**N=1 is always ε_M = 0** (single exponential is exactly Markovian). For N ≥ 5 and broad W_τ, ε_M converges to a value determined primarily by W_τ.

### Boundary Law

```
ε_M ≈ 0.55 × (1 - exp(-W_τ / 4.5))

Critical boundaries (N = 20, uniform coupling):
  W_τ* = 0.7 decades   (VALID → MARGINAL, ε_M = 0.05)
  W_τ** = 1.8 decades  (MARGINAL → INVALID, ε_M = 0.20)
  Saturation: ε_M → 0.55 as W_τ → ∞
```

ε_M converges rapidly with N (stabilizes by N ~ 20). The spectral width W_τ is the dominant control parameter, not N or coupling heterogeneity.

### N-independence

At W_τ = 2.0 (two decades of timescale spread): ε_M = 0.105 (N=2) → 0.215 (N=20) → 0.209 (N=200). The error stabilizes by N ~ 20 and changes by < 3% beyond that. **The Markovian validity depends on the WIDTH of the timescale distribution, not on the number of modes.**

### Coupling heterogeneity

Coupling heterogeneity H_J (std/mean of coupling constants) has a SECONDARY effect. At fixed W_τ, varying H_J from 0 to 1 changes ε_M by ~30% in either direction (noise from random coupling realization). The primary control parameter remains W_τ.

---

## Physical Archetype Mapping

| Environment | W_τ (decades) | Zone | Markovian law valid? |
|------------|:-------------:|:----:|:--------------------:|
| **Dilute monatomic gas** | 0 | VALID | **YES** (exact) |
| **Dense molecular gas** | 0.5 | VALID | **YES** (ε_M < 0.03) |
| **Multi-component plasma** | 1.5 | MARGINAL | **APPROXIMATELY** (ε_M ~ 0.10-0.17) |
| **Neutron star crust** | 3+ | INVALID | **NO** (multi-exponential memory essential) |
| **Galaxy interior** | 5+ | INVALID | **NO** |
| **Early universe** | 10+ | INVALID | **NO** (grossly inadequate) |

### Interpretation

The Markovian constitutive law τ dΦ/dt + Φ = X(g) is valid for **homogeneous, single-timescale environments** (laboratory gases, simple plasmas). It breaks for **any environment where relaxation processes span more than ~1-2 decades of timescale**. This includes most astrophysical and cosmological environments.

This is consistent with the EIT literature: the first-order Markovian form is the leading-order approximation (valid near single-timescale equilibrium) and breaks down for multi-scale transport.

---

## Premise Checks

**I* = 1.15428:** No boundary ratio or diagnostic matches this value.
- W_τ** / W_τ* = 2.69 (not 1.15)
- ε_sat / ε_1 = 11.0 (not 1.15)
- Status: **undefined_in_G2A** (OPEN)

**IR nonlocal:** Not addressed in G2-A (linear Gaussian scope; deferred to G2-B if nonlinear).

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **G2A-G1** | Control parameter set explicit | **PASS** | W_τ, N_fast, H_J, λ_cg defined with ranges and interpretations. |
| **G2A-G2** | Valid/marginal/invalid map produced | **PASS** | Two phase diagrams (W_τ × N_fast, W_τ × H_J) with explicit thresholds (ε_1 = 0.05, ε_2 = 0.20). |
| **G2A-G3** | Boundary laws extracted | **PASS** | ε_M ≈ 0.55(1 − exp(−W_τ/4.5)). W_τ* = 0.7, W_τ** = 1.8 decades. |
| **G2A-G4** | Physical archetype mapping | **PASS** | Six environments classified from VALID to INVALID with W_τ estimates and Markovian reliability assessment. |
| **G2A-G5** | Regime guidance operational | **PASS** | Any user of the Markovian constitutive law can check: "Is my environment's timescale spread < 0.7 decades?" If yes: valid. If 0.7-1.8: marginal. If > 1.8: invalid. |

## Decision Token

### **proceed_G2B**

**Rationale:** The Markovian validity envelope is quantified. The boundary is sharp: W_τ ~ 0.7-1.8 decades separates valid from invalid regimes. G2-B should now characterize the MEMORY STRUCTURE in the invalid regime: what kernel forms emerge, what observables they modify, and whether the non-Markovian corrections have detectable physical consequences.

---

*Program G Stage G2-A complete. Decision: proceed_G2B. Markovian validity boundary: W_τ* = 0.7 decades (VALID/MARGINAL), W_τ** = 1.8 decades (MARGINAL/INVALID). Boundary law: ε_M ≈ 0.55(1-exp(-W_τ/4.5)). Physical: VALID for homogeneous gas/plasma. INVALID for astrophysical multi-scale environments. I*: undefined. Gates: 5/5 pass.*
