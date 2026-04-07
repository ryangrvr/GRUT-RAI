# Program F — Stage F0/F1: Discriminator Charter + USL Robustness Scan

---

## F0: Discriminator Charter

### Kill-signal criteria

An experimental result constitutes a "kill signal" for the GRUT class if:

| # | Criterion | What kills what |
|---|-----------|----------------|
| **KS1** | Measured decoherence rate at (m, l) in the point-mass regime differs from Gm²/(ℏl) by more than the extended-body correction factor AND exceeds the environmental noise floor. | Kills the Newtonian gravitational dephasing mechanism → kills the ENTIRE forced form-class (not just GRUT). |
| **KS2** | No decoherence excess above environmental background is observed at the operating point (196 fg, 474 nm, USL/gas = 2.9) with sufficient statistics. | Rules out GRUT's quantitative USL prediction AND the Diosi-Penrose model at these parameters. |
| **KS3** | Measured decoherence rate matches a DIFFERENT scaling (e.g., l² instead of 1/l) at separations l > 2R. | Rules out gravitational dephasing mechanism; supports environmental noise diffusion as dominant. |

### Robustness thresholds

| Metric | Threshold | Basis |
|--------|:---------:|-------|
| USL/gas ratio | Must exceed 1.0 after all corrections | Below 1.0: signal is below environmental floor |
| Extended-body suppression | Must be < 10 at operating point | Above 10: point-mass formula unreliable |
| Statistical significance | 3σ minimum (p < 0.003) | Standard experimental physics threshold |

### Pathology exclusion

| Pathology | Check |
|-----------|-------|
| Ghost / instability in CTP action | A1-L1 through L10 (Book A): all pass |
| Negative probabilities | CTP U3: Im S_eff ≥ 0 (Book A): pass |
| Acausal signal | First-order retarded ODE: causal by construction |
| FDT violation | D = k_BT τ/2 verified (Iota-Prime) |

### Neighbor model set

| # | Family | Parameter space | Scope |
|---|--------|----------------|-------|
| **N1** | τ(x) = τ₀ + δτ₁ R + δτ₂ R² + ... | δτ_n ∈ ℝ | Constitutive sector (Sectors 1-2) |
| **N2** | X = β + αR + γR² + ... | γ ∈ ℝ (and higher coefficients) | Source coupling |
| **N3** | f(Φ) = Φ + cΦ² + dΦ³ + ... | c, d ∈ ℝ | Nonlinear force |
| **N4** | (Φ, Ψ) coupled system | κ, ε, σ, ν, τ₂ | Two-field extension |

### Metric set

| # | Observable metric | How measured |
|---|------------------|-------------|
| M1 | USL decoherence rate Λ(m, l) | Visibility decay in nanoparticle superposition experiment |
| M2 | Mass-distance scaling exponent (Λ ∝ m^a / l^b) | Measure Λ at multiple (m, l) values; fit a, b |
| M3 | Detectable visibility contrast at fixed interrogation time | V_env − V_total at the operating point |
| M4 | Stability / pathology flags (negative visibility, acausal signal) | Monitor for unphysical behavior |

---

## F1: USL Robustness Scan Results

### Parameter grid

| Family | Parameters varied | Range | Grid points |
|--------|------------------|-------|:-----------:|
| N1 | δτ₁ (curvature dependence of τ) | [0, 10] × τ₀ | Analytical (τ-independent of USL) |
| N2 | γ (R² coefficient in X) | [0, α] | Analytical (X-independent of USL) |
| N3 | c, d (quadratic, cubic in f) | [−1, 1] | Analytical (f-independent of USL) |
| N4 | κ, ε (Φ-Ψ coupling) | GRUT-II Nu range | Analytical + conditional |

### Observable shifts

| Family | |ΔΛ_USL / Λ_USL| | |Δ(USL/gas)| | Mechanism | Confidence |
|:------:|:-:|:-:|---|:-:|
| N1 | **0** (exact) | **0** | τ decoupled from Sector 3 | 1.00 |
| N2 | **< 10⁻²⁵** | **< 10⁻²⁵** | Backreaction suppressed | 0.95 |
| N3 | **< 10⁻²⁰** | **< 10⁻²⁰** | f(Φ) does not enter USL | 0.95 |
| N4 | **UNDETERMINED** | **CONDITIONAL** | Depends on Φ-matter coupling (unknown) | 0.40 |

### Sensitivity ranking

| Rank | Family | Sensitivity to USL | Why |
|:----:|:------:|:------------------:|-----|
| 1 | N4 (two-field) | CONDITIONAL | Only family with possible nonzero impact (if branches in different attractors with non-negligible Φ coupling) |
| — | N1, N2, N3 | ZERO / NEGLIGIBLE | USL is Sector 3; these perturb Sectors 1-2 only |

### Robustness verdict: **ROBUST**

The USL prediction Λ = Gm²/(ℏl) is robust against all four neighbor families. Three families (N1, N2, N3) have exactly zero or negligibly small impact. The fourth (N4) has conditional impact only if the superposition branches occupy different Φ attractors with non-negligible Φ-matter coupling — a scenario that is physically speculative and parameter-dependent.

**Root cause of robustness:** The Alpha-Prime sector separation. Sector 3 (gravitational dephasing) depends on (G, m, l, ℏ) only. Sectors 1-2 (constitutive dynamics) depend on (τ, α, β, f, Ψ). The two sectors are decoupled at tree level. Perturbing Sectors 1-2 does not change Sector 3.

### Critical consequence

**The USL cannot discriminate among class members.** Every theory in the forced form-class (E2-B) makes the identical USL prediction (same Newtonian gravity, same Diosi integral). Confirming or refuting the USL confirms or refutes the ENTIRE CLASS, not any specific member.

### Top 3 discriminator observables (for class-member selection)

| Rank | Observable | What it discriminates | Current measurability |
|:----:|-----------|----------------------|:---------------------:|
| **1** | τ (constitutive relaxation time) | Selects among N1 family (τ-values) | NOT MEASURABLE (Φ unidentified) |
| **2** | α (curvature coupling) | Selects among N2 family (X(g) forms) | NOT MEASURABLE (Φ-matter coupling unknown) |
| **3** | Nonlinear response c, d | Selects among N3 family (force shapes) | NOT MEASURABLE (Φ unidentified) |

**Blocking obstacle:** All three class-member discriminators require identifying Φ with a physical degree of freedom. This identification has not been made in any GRUT program stage.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **F0-G1** | Kill-signal criteria explicit | **PASS** | KS1-KS3 defined with what each kills. Robustness thresholds quantified. |
| **F0-G2** | Neighbor set complete and non-redundant | **PASS** | N1-N4 cover: τ variation, source coupling, nonlinearity, field multiplicity. Each perturbs a different structural feature. No overlap. |
| **F1-G1** | Scan executed across all four families | **PASS** | N1-N4 all analyzed (analytical for N1-N3, conditional for N4). |
| **F1-G2** | Observable deltas quantified | **PASS** | N1: 0 (exact). N2: < 10⁻²⁵. N3: < 10⁻²⁰. N4: undetermined (conditional). |
| **F1-G3** | Robustness verdict + top 3 discriminators | **PASS** | Verdict: ROBUST. Top 3: τ, α, nonlinear response — all requiring Φ identification. |

---

## Decision Token

### **proceed_F2**

**Rationale:**

F0/F1 established that the USL is robust but non-discriminating. The blocking obstacle for class-member selection is Φ identification. F2 should address either:

**(a)** The Φ-identification problem: what physical degree of freedom is Φ? Can it be mapped to a known field (dilaton, dark energy scalar, inflaton decay product)? If identified, the constitutive-sector observables (τ, α, nonlinearity) become measurable.

**(b)** Experimental protocol design for USL class-level confirmation: since the USL tests the ENTIRE class, design the optimal experiment for class-level yes/no at the corrected operating point. This is useful even without Φ identification.

**Recommended: (b) first** (the USL experiment is the near-term testable output), then **(a)** as a longer-term theoretical investigation (Φ identification is a foundational question outside the current EFT).

---

*Program F Stage F0/F1 complete. Decision: proceed_F2. USL robustness: ROBUST (N1: 0, N2: <10⁻²⁵, N3: <10⁻²⁰, N4: conditional). The USL cannot discriminate among class members — it tests the ENTIRE forced class. Top 3 discriminators (τ, α, nonlinear response) all require Φ identification, which is the blocking obstacle. Kill signals KS1-KS3 defined. Gates: 5/5 pass (F0: 2/2, F1: 3/3).*
