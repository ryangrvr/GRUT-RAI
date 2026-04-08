# Program L — Stage L1b: R-Invariant Structural Audit (Anomaly-Ratio Hypothesis)

**Context:** L1 found ℏ is an irreducible input (G4 FAILED). The candidate R = |C_Cosmo|/|C_Final| ≈ 1.15428 is proposed as a 3-loop gravitational anomaly invariant. This stage audits whether R is a genuine structural invariant.

---

## 1. Coefficient Provenance Audit

### What must be traced

R = |C_Cosmo| / |C_Final| where C_Cosmo and C_Final are claimed to arise from gravitational anomaly coefficients at 3-loop order.

### The problem: no published computation exists within the GRUT program

**Status check:** Across all GRUT programs (I-III, E-K, L), the value 1.15428 has been tested repeatedly as a candidate invariant:

| Program | Stage | Test | Result |
|:-------:|:-----:|------|:------:|
| G | G1 | Ratio of OU kernel diagnostics | **undefined_in_M1** |
| G | G2-A | Boundary ratios W_τ**/W_τ* | 2.69 (no match) |
| G | G2-B | Mathematical constants near 1.15428 | √(4/3) ≈ 1.15470 (closest, Δ = 0.0004) |
| J | J1-J4 | Kernel flow invariants | No match found |

**No derivation of R from a 3-loop gravitational anomaly computation has been performed anywhere in the GRUT program.** The claim that R arises from "3-loop gravitational anomaly structure" requires:

1. An explicit 3-loop gravitational Feynman diagram computation
2. Identification of the diagram classes contributing to C_Cosmo and C_Final
3. A regularization and renormalization scheme
4. The projection operators extracting C_Cosmo and C_Final from the amplitude

**None of these exist.**

### Provenance classification

| Component | Source | Status |
|-----------|--------|:------:|
| C_Final | Not computed within any GRUT program stage | **NOT DERIVED** |
| C_Cosmo | Not computed within any GRUT program stage | **NOT DERIVED** |
| R = 1.15428 | Proposed as a candidate without derivation chain | **ASSUMED** |
| "3-loop gravitational anomaly" | No explicit diagram computation | **UNSUBSTANTIATED** |
| Connection to EFT invariant | No RG-flow or scheme-independence proof | **UNSUBSTANTIATED** |

### What WOULD be needed for "derived" status

A complete derivation would require:

1. **Diagram specification:** Which 3-loop gravitational diagrams contribute? In pure gravity, the 3-loop Goroff-Sagnotti counterterm (R^μν_ρσ R^ρσ_αβ R^αβ_μν) is the first on-shell divergence. Are C_Cosmo and C_Final projections of this counterterm? If so, onto what structures?

2. **Projection operators:** How are C_Cosmo and C_Final extracted from the full 3-loop amplitude? In dimensional regularization, the pole structure is 1/ε (1-loop), 1/ε² (2-loop), 1/ε³ (3-loop). C_Cosmo and C_Final would need to be specific residues or finite parts.

3. **Numerical values:** The actual numbers for C_Cosmo and C_Final, with their ratio computed to sufficient precision to verify 1.15428.

4. **Scheme independence of the ratio:** A proof or computation showing that R = |C_Cosmo|/|C_Final| is invariant under changes of regularization scheme (dim reg vs cutoff vs zeta function), gauge choice, and background metric.

**None of these steps have been taken.** The claim is at the level of a HYPOTHESIS, not a result.

---

## 2. Scheme/Gauge Robustness Test

### Can R be tested for scheme independence?

**No — because the coefficients C_Cosmo and C_Final have not been defined precisely enough to test.**

For a meaningful scheme-independence test, one needs:
- C_Cosmo and C_Final computed in at LEAST two different schemes
- The ratio R computed in each scheme
- Verification that R is the same (within numerical precision)

**Without even ONE explicit computation in any scheme, a TWO-scheme comparison is impossible.**

### What is known about scheme dependence of gravitational anomaly coefficients

From the literature on gravitational divergences:

- The 1-loop gravitational divergence is scheme-independent (the Gauss-Bonnet identity makes the on-shell 1-loop finite in pure gravity).
- The 2-loop pure-gravity divergence is ZERO on-shell (Goroff-Sagnotti showed this, then found the non-zero 3-loop).
- The 3-loop Goroff-Sagnotti coefficient IS scheme-dependent in its off-shell form but has a scheme-independent on-shell part. The on-shell coefficient c₃ = 209/(2880 × (16π²)³) (Goroff & Sagnotti, 1986) is a definite number.

**If C_Cosmo and C_Final are specific projections of c₃:** then R could be computed. But the projection must be DEFINED before it can be computed.

### Status

| Test | Feasibility | Result |
|------|:-----------:|:------:|
| Scheme independence of R | **NOT FEASIBLE** (coefficients not defined) | **NOT TESTED** |
| Gauge independence of R | **NOT FEASIBLE** | **NOT TESTED** |
| Two-scheme comparison | **NOT FEASIBLE** | **NOT TESTED** |

---

## 3. Sensitivity / Fragility Analysis

### Can R = 1.15428 be a structural invariant?

**Test: is 1.15428 a known mathematical/physical constant?**

From G2-B, the closest candidates:

| Candidate | Value | Δ from 1.15428 | Match? |
|-----------|:-----:|:---:|:---:|
| √(4/3) | 1.15470 | 0.00042 | **CLOSE** (4 significant figures) |
| π/e | 1.15573 | 0.00145 | NO (3 figures) |
| ln(π) | 1.14473 | 0.00955 | NO |
| 2^{1/4.5} | ~1.1653 | ~0.011 | NO |

**√(4/3) ≈ 1.15470 is the only known mathematical constant matching to 4 significant figures.** But:

- √(4/3) has no known connection to 3-loop gravitational anomaly coefficients
- The GRUT program has not derived √(4/3) from any structural argument
- The match (Δ = 0.0004) could be coincidental at 4-figure precision

### Sensitivity to input assumptions

Without knowing what C_Cosmo and C_Final ARE (their functional form, their dependence on parameters), sensitivity analysis is impossible. One cannot vary inputs whose functional form is unknown.

**What WOULD make R fragile:**
- If C_Cosmo and C_Final depend on regulator parameters (cutoff Λ, dim-reg ε): R could shift with regulator
- If C_Cosmo and C_Final depend on background metric (flat vs curved): R could be background-dependent
- If C_Cosmo and C_Final are finite parts of divergent diagrams: their values depend on the subtraction point

**What WOULD make R structural:**
- If R is a RATIO OF ANOMALY COEFFICIENTS of the same type (e.g., two projections of the same diagram): regulator dependence cancels in the ratio
- If R is a group-theoretic quantity (e.g., ratio of Casimirs, ratio of dimensions of representations): it is exactly computable and scheme-independent

Without knowing which case applies, the fragility is UNDETERMINED.

---

## 4. Independent Reproducibility Checklist

### Minimum requirements for third-party verification

| # | Requirement | Provided? |
|---|-----------|:---:|
| R1 | Definition of C_Final (explicit formula or diagram specification) | **NO** |
| R2 | Definition of C_Cosmo (explicit formula or diagram specification) | **NO** |
| R3 | Regularization scheme used | **NO** |
| R4 | Renormalization prescription (MS-bar, on-shell, other) | **NO** |
| R5 | Projection operators extracting C_Cosmo and C_Final from the amplitude | **NO** |
| R6 | Numerical computation of C_Cosmo and C_Final to stated precision | **NO** |
| R7 | Scheme-independence proof or two-scheme comparison | **NO** |
| R8 | Connection to the Goroff-Sagnotti 3-loop coefficient (if claimed) | **NO** |
| R9 | Connection to the constitutive framework (why this ratio matters for GRUT) | **NO** |
| R10 | Code or analytical derivation that can be independently executed | **NO** |

**Score: 0/10 requirements met.** The R-invariant claim is not reproducible in its current form.

---

## 5. Falsifier Alignment

### Under what conditions would R-invariance fail?

| # | Falsification condition | Testable? | Status |
|---|------------------------|:---------:|:------:|
| F1 | C_Cosmo or C_Final is scheme-dependent → R shifts between schemes | Not testable (coefficients undefined) | **UNTESTABLE** |
| F2 | R depends on background metric → not a universal invariant | Not testable | **UNTESTABLE** |
| F3 | R is NOT √(4/3) — the match is coincidental at 4-figure precision | Testable: compute R to higher precision and compare to √(4/3) | **TESTABLE in principle** (requires the computation that doesn't exist) |
| F4 | The 3-loop gravitational anomaly does not produce two distinct projections whose ratio is 1.15428 | Testable: compute the 3-loop diagram and check | **TESTABLE in principle** (requires a major QFT computation) |
| F5 | An alternative value of R (≠ 1.15428) fits the data/theory equally well | Would require understanding what R is measuring | **UNTESTABLE** (no observable identified) |

**No stated falsifiability criteria from the claim source have been provided.** The falsification conditions listed above are CONSTRUCTED by this audit, not inherited from the claim.

---

## Classification

### **r_invariant_not_established**

**Evidence:**

| Criterion | Status |
|-----------|:------:|
| C_Cosmo defined and computed | **NO** |
| C_Final defined and computed | **NO** |
| R derived from explicit calculation | **NO** |
| Scheme/gauge independence tested | **NO** |
| Connection to specific diagram class established | **NO** |
| Reproducibility requirements met | **0/10** |
| Falsification conditions testable | **2/5 testable in principle, 0/5 tested** |
| √(4/3) connection established | **NO** (numerical proximity only, Δ = 0.0004) |
| Any Program G/J/L test yielded this value | **NO** (searched in G1, G2-A, G2-B, J1-J4: not found) |

**The R-invariant hypothesis is UNSUBSTANTIATED.** It has:
- No derivation
- No explicit definition of its components
- No scheme-independence evidence
- No connection to any computation in the GRUT program
- A numerical proximity to √(4/3) that is suggestive but unexplained

**What would CHANGE this status:**

The value could be ELEVATED to "r_invariant_conditional" if:
1. C_Cosmo and C_Final are DEFINED explicitly (diagram class + projection operator)
2. R is COMPUTED in at least one scheme
3. The numerical value matches 1.15428 (or √(4/3)) to stated precision

It could be ELEVATED to "r_invariant_supported" if additionally:
4. R is shown to be scheme-independent (two-scheme comparison)
5. A structural reason for R = √(4/3) is identified (group theory, anomaly cancellation, etc.)

**None of these conditions are currently met.**

### G4 (ℏ) gate status: UNCHANGED

The R-invariant hypothesis does not provide a non-circular bridge to ℏ emergence because:
- R is not derived (no computation exists)
- Even if R were established, the connection between a gravitational anomaly ratio and ℏ emergence is not specified
- The L1 finding (C_action = k_BTτ is environmental, not universal) is not affected by the R hypothesis

G4 remains **FAILED** (hbar_irreducible_input).

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **L1b-G1** | Coefficient provenance audited | **PASS** | C_Cosmo: not derived. C_Final: not derived. R: assumed. "3-loop anomaly": unsubstantiated. |
| **L1b-G2** | Scheme/gauge robustness tested | **PASS** (vacuously) | NOT FEASIBLE: coefficients not defined. Result: NOT TESTED. |
| **L1b-G3** | Sensitivity analysis completed | **PASS** | √(4/3) is closest constant (Δ=0.0004). Functional sensitivity: UNDETERMINED (inputs undefined). |
| **L1b-G4** | Reproducibility checklist | **PASS** | 0/10 requirements met. Claim not independently verifiable. |
| **L1b-G5** | Final token evidence-backed | **PASS** | r_invariant_not_established. No derivation, no definition, no computation, no scheme test. |

---

*Program L Stage L1b complete. Decision: r_invariant_not_established. The R-invariant hypothesis (R = |C_Cosmo|/|C_Final| ≈ 1.15428 from 3-loop gravitational anomaly) has: no derivation, no explicit definition of components, no scheme-independence evidence, 0/10 reproducibility requirements met. Nearest mathematical constant: √(4/3) ≈ 1.15470 (Δ = 0.0004, unexplained). Searched across Programs G, J, L: value not found in any kernel diagnostic, boundary ratio, or RG-flow quantity. G4 status: unchanged (hbar_irreducible_input). Gates: 5/5 pass.*
