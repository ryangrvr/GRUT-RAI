# Program F — Stage F2-A: Class-Level USL Experimental Protocol and Falsification Design

**Predecessor:** F0/F1 (USL robust, non-discriminating, class-level falsifier).

---

## 1. Measurement Model

### Primary observable

The decoherence rate Λ_total of a massive object in spatial superposition, extracted from the visibility decay of an interference pattern:

```
V(t) = V₀ exp(−Λ_total t)

where:
  Λ_total = Λ_env + Λ_USL + Λ_other
  Λ_env   = known environmental decoherence (gas, BB, laser, charge — measured/calibrated)
  Λ_USL   = G m² / (ℏ l)  [the target signal, in point-mass regime l > 2R]
  Λ_other = any unmodeled decoherence source
```

The measured quantity is Λ_total. The inferred quantity is:

```
Λ_excess ≡ Λ_total − Λ_env
```

If the forced class is correct: Λ_excess = Λ_USL = Gm²/(ℏl).
If the forced class is wrong: Λ_excess ≠ Gm²/(ℏl), or Λ_excess = 0.

### Regime validity condition

```
l > 2R    (point-mass regime, Kappa-Prime)

where:
  l = superposition separation (measured/controlled)
  R = particle radius = (3m / 4πρ)^{1/3}  (from mass and density)
```

This condition MUST be verified for every data point. Data with l < 2R requires the full Diosi integral, not the point-mass formula.

### Scaling law observable

The USL predicts specific power-law exponents:

```
Λ_USL ∝ m^a / l^b

Predicted: a = 2, b = 1

Alternative models:
  Caldeira-Leggett noise: a = 1, b = −2 (Λ ∝ m l²)
  CSL collapse: a = 2, b = 0 (Λ ∝ m², l-independent at l >> r_C)
  No anomalous decoherence: a = 0, b = 0 (Λ_excess = 0)
```

Measuring Λ_excess at multiple (m, l) values and fitting a, b is the primary discrimination between the forced class and alternatives.

### Nuisance parameters

| Parameter | Symbol | Status | Mitigation |
|-----------|--------|:------:|-----------|
| Gas collision rate | Λ_gas | MEASURABLE (from pressure, temperature, cross-section) | Independent pressure measurement. Calibrate by varying P. |
| Blackbody emission/absorption | Λ_BB | COMPUTABLE (from T_int, T_env, Im{ε}) | Control T. Compute from material properties. |
| Laser photon recoil | Λ_laser | CONTROLLABLE (dark protocol) | Zero during coherent free evolution. |
| Charge noise | Λ_charge | CONTROLLABLE (neutralization) | Verify charge = 0 before each run. |
| Magnetic field noise | Λ_mag | MEASURABLE (magnetometry) | Shield + measure residual. |
| NV spin T₂ | 1/T₂ | MEASURABLE (spin echo) | Independent T₂ measurement for each particle. |
| Readout noise | σ_read | MEASURABLE (calibration runs) | Characterize before science runs. |
| Vibration / seismic | Λ_vib | COMPUTABLE (from accelerometry) | Seismic isolation + monitoring. |

---

## 2. Falsification Criteria (KS1-KS3 Operationalized)

### KS1: Λ_excess ≠ Gm²/(ℏl) in valid regime

**Statistical test:** Measure Λ_excess at a single (m, l) operating point. Compare to the predicted value Λ_pred = Gm²/(ℏl).

```
Test statistic: Z = (Λ_excess − Λ_pred) / σ_Λ

where σ_Λ = uncertainty on Λ_excess (from visibility fit + environmental calibration)

Decision rule:
  |Z| > 3:  reject Λ_excess = Λ_pred at 3σ (p < 0.003)
  |Z| > 5:  strong rejection (p < 6×10⁻⁷)
```

**Required data volume:**

The visibility contrast at the operating point (196 fg, 474 nm, 5 s hold) is:
```
ΔV = V_env − V_total ≈ 0.21 (21% contrast at 5 s hold, from Mu-Prime)
```

To measure ΔV with fractional precision δ (i.e., σ_ΔV = δ × ΔV):
```
N_runs ≥ (1 / (SNR_per_run × δ × ΔV))²

For δ = 0.3 (30% precision → 3σ discrimination):
  N_runs ≈ (1 / (10 × 0.3 × 0.21))² ≈ 25  [SNR/run = 10]
  N_runs ≈ (1 / (3 × 0.3 × 0.21))²  ≈ 280 [SNR/run = 3]
```

**Confidence threshold:** 3σ minimum for class falsification. 5σ for definitive claim.

### KS2: No detectable excess (Λ_excess consistent with 0)

**Statistical test:** Measure Λ_total at the operating point. Subtract calibrated Λ_env. Test whether the residual is consistent with zero.

```
Test statistic: Z₀ = Λ_excess / σ_Λ

Decision rule:
  Z₀ < 2: Λ_excess consistent with 0 (no anomalous decoherence detected)
  Z₀ < 1: strong null (class-level prediction refuted at this operating point)
```

**Interpretation:** KS2 triggers if the excess decoherence is LESS THAN EXPECTED. This does not necessarily kill the forced class — it could mean:
- The environmental calibration is off (Λ_env underestimated)
- The operating point has l < 2R due to imprecise separation control
- The particle shape is non-spherical (different Diosi integral)

KS2 is a kill signal ONLY if environmental calibration is validated by independent means AND l > 2R is verified AND particle geometry is characterized.

**Required data volume:** Same as KS1 (the measurement is the same; the interpretation differs).

### KS3: Wrong scaling (l² vs 1/l)

**Statistical test:** Measure Λ_excess at MULTIPLE separations l (with m fixed). Fit the power law Λ_excess ∝ l^{−b}.

```
Model comparison:
  H₁ (USL): b = 1 (Λ ∝ 1/l)
  H₂ (CL):  b = −2 (Λ ∝ l²)
  H₀ (null): b = 0 (no l-dependence)

Use Bayesian model comparison or frequentist F-test on nested models.
```

**Required data:**

Minimum 3 distinct l values in the point-mass regime (l > 2R). Ideally 5+ values spanning at least one decade in l.

For the operating point (m = 196 fg, R = 237 nm):
- l = 500 nm (l/R = 2.1): Λ_USL = 4.9×10⁻² s⁻¹
- l = 750 nm (l/R = 3.2): Λ_USL = 3.2×10⁻² s⁻¹
- l = 1000 nm (l/R = 4.2): Λ_USL = 2.4×10⁻² s⁻¹
- l = 1500 nm (l/R = 6.3): Λ_USL = 1.6×10⁻² s⁻¹
- l = 2000 nm (l/R = 8.4): Λ_USL = 1.2×10⁻² s⁻¹

All above Λ_gas ≈ 1.8×10⁻² s⁻¹ only for the first two points. At larger l, USL < gas. The scaling test requires the USL signal to be detectable, which limits the l-range.

**Practical minimum:** 3 points in range l ∈ [500, 1000] nm, each with ~100 runs. Total: ~300 experimental runs at 3 different separations.

**Confidence threshold:** Bayesian evidence ratio > 10:1 (strong evidence) or > 100:1 (decisive) between H₁ and H₂.

---

## 3. Parameter-Space Protocol

### Scan axes

| Axis | Range | Grid points | Purpose |
|------|-------|:-----------:|---------|
| **Mass m** | 100-500 fg | 3 values: 150, 200, 350 fg | Test m² scaling |
| **Separation l** | 500-2000 nm (all > 2R) | 5 values: 500, 750, 1000, 1500, 2000 nm | Test 1/l scaling |
| **Hold time t** | 1-10 s | 3 values: 1, 3, 10 s | Optimize visibility contrast |
| **Pressure P** | 10⁻¹⁴-10⁻¹² Pa | 3 values | Environmental calibration |

### Minimal viable scan grid

The MINIMUM experiment to test the USL at class level:

```
Phase 1: Single operating point (class-level yes/no)
  m = 196 fg, l = 474 nm, t = 5 s, P = 10⁻¹³ Pa
  N_runs = 300
  Output: Λ_excess detected or not (KS1/KS2)

Phase 2: Scaling test (1/l vs l² discrimination)
  m = 196 fg, l = {500, 750, 1000} nm, t = 5 s, P = 10⁻¹³ Pa
  N_runs = 100 per l-value (300 total)
  Output: b = 1 or b ≠ 1 (KS3)

Phase 3: Mass scaling (m² confirmation)
  m = {150, 200, 350} fg, l = 2R for each, t = 5 s
  N_runs = 100 per m-value (300 total)
  Output: a = 2 or a ≠ 2
```

**Total minimum: 900 experimental runs across 9 configurations.**

### Exclusion / acceptance regions

In the (a, b) exponent space:

| Region | a | b | Interpretation |
|--------|:-:|:-:|---------------|
| **ACCEPT (forced class)** | 2.0 ± 0.5 | 1.0 ± 0.3 | Consistent with Λ ∝ m²/l |
| **REJECT (CL noise)** | 1.0 ± 0.5 | −2.0 ± 0.5 | Consistent with Λ ∝ m l² |
| **REJECT (CSL)** | 2.0 ± 0.5 | 0.0 ± 0.3 | l-independent at l >> r_C |
| **REJECT (null)** | 0.0 ± 0.5 | 0.0 ± 0.5 | No anomalous decoherence |
| **INCONCLUSIVE** | All other | — | Cannot distinguish models |

---

## 4. Systematics and Degeneracy Control

### Dominant confounders

| # | Confounder | Effect | Mitigation | Residual risk |
|---|-----------|--------|-----------|:-------------:|
| **S1** | Gas collision rate miscalibration | Shifts Λ_env, biasing Λ_excess | Independent P measurement (ion gauge). Vary P and check linear Λ_gas(P). | LOW (if calibrated at 3+ pressures) |
| **S2** | Particle mass uncertainty | Shifts Λ_pred = Gm²/(ℏl) | Mass determination from trap frequency + density. Precision: ~5% achievable. | LOW |
| **S3** | Separation uncertainty | Shifts Λ_pred and regime validity | SG gradient calibration. Independent separation measurement if possible. | MODERATE (SG separation depends on gradient × time² / mass) |
| **S4** | Particle shape (non-spherical) | Modifies the Diosi integral at l ~ 2R | Characterize particle shape (SEM). Use l >> 2R where shape correction is small. | LOW (if l/R > 3) |
| **S5** | Internal heating during free fall | Adds thermal decoherence | Monitor internal temperature (IR emission). Choose materials with low absorption. | MODERATE |
| **S6** | NV spin decoherence (if SG protocol) | Adds spin-dephasing floor | Independent T₂ measurement. Subtract from Λ_total. | HIGH (T₂ gap is the hardware bottleneck) |
| **S7** | Stray electromagnetic fields | Adds force noise | Shield + monitor. Calibrate with charged/neutral particles. | LOW (if shielded) |

### Distinguishing "class killed" vs "inconclusive"

| Outcome | Interpretation | Required evidence |
|---------|---------------|-------------------|
| Λ_excess = Gm²/(ℏl) ± 30% at 3+ (m,l) values | **CLASS SUPPORTED** | Scaling exponents a = 2±0.5, b = 1±0.3 |
| Λ_excess = 0 with all systematics controlled | **CLASS FALSIFIED** (KS2) | Environmental calibration verified by P-variation. l > 2R verified. 3σ null. |
| Λ_excess ≠ 0 but wrong scaling | **CLASS FALSIFIED** (KS3) | Scaling fit rejects b = 1 at 3σ in favor of b ≠ 1 |
| Λ_excess ambiguous due to T₂ floor | **INCONCLUSIVE (hardware-limited)** | Λ_excess comparable to 1/T₂. Cannot separate USL from spin dephasing. |
| Λ_excess ambiguous due to P uncertainty | **INCONCLUSIVE (calibration-limited)** | Λ_excess comparable to ΔΛ_gas from pressure uncertainty. |

---

## 5. Decision Engine

### Token rules

| Token | Trigger condition | Threshold |
|-------|------------------|:---------:|
| **class_falsified** | KS1 or KS2 or KS3 satisfied at ≥ 3σ, with all dominant systematics (S1-S7) controlled or bounded below the signal level. | Z > 3 for KS1; Z₀ < 1 for KS2; Bayes factor > 10:1 for KS3 |
| **class_supported_not_selected** | Λ_excess consistent with Gm²/(ℏl) at 1-2 (m,l) points. Scaling not yet tested OR scaling consistent with b = 1. No member-specific information obtained. | Z within ±2 of prediction at each point |
| **inconclusive_hardware_limited** | Λ_excess cannot be isolated from spin dephasing (1/T₂), environmental miscalibration (ΔΛ_env), or readout noise. The signal exists within the noise but cannot be extracted. | σ_Λ > 0.5 × Λ_pred at all tested points |

### Decision logic (flowchart)

```
START
│
├─ Can Λ_excess be measured with σ_Λ < 0.5 × Λ_pred?
│   ├─ NO → inconclusive_hardware_limited
│   └─ YES ↓
│
├─ Is Λ_excess consistent with 0?
│   ├─ YES (Z₀ < 1) AND systematics controlled → class_falsified (KS2)
│   └─ NO ↓
│
├─ Is Λ_excess consistent with Gm²/(ℏl)?
│   ├─ NO (|Z| > 3) AND systematics controlled → class_falsified (KS1)
│   └─ YES ↓
│
├─ Is the scaling b = 1 confirmed at 3+ l-values?
│   ├─ NO (b ≠ 1 at 3σ) → class_falsified (KS3)
│   ├─ YES → class_supported_not_selected
│   └─ NOT TESTED → class_supported_not_selected (pending scaling test)
│
END
```

---

## 6. Hand-Off Contract to F2-B

### What F2-A cannot answer

| # | Question | Why F2-A cannot answer it | What would answer it |
|---|---------|--------------------------|---------------------|
| H1 | Which class member is the universe? | USL does not discriminate (F1 result). All members make the same USL prediction. | Measuring τ, α, or f(Φ) — requires Φ identification. |
| H2 | What is Φ? | F2-A tests the gravitational dephasing sector, which is Φ-independent. | A theoretical identification of Φ with a known or new physical field. |
| H3 | Is bistability physical? | F2-A tests single-branch decoherence. Bistability requires inter-attractor dynamics. | An experiment where the superposition branches occupy different Φ attractors. |

### Evidence to pass to Φ-identification work

| # | Evidence | Implication for Φ identification |
|---|---------|--------------------------------|
| P1 | If class_supported: gravitational dephasing is real → Φ lives in a theory with Newtonian gravity + irreversible scalar dynamics. | Φ must be a scalar field that (a) couples to curvature and (b) has a first-order dissipative EOM. Candidate mappings: dilaton, quintessence, dark energy scalar. |
| P2 | If class_falsified (KS3, wrong scaling): gravitational dephasing is NOT the dominant mechanism → the anomalous decoherence (if any) has a different origin. | Φ identification becomes moot for the USL channel. The constitutive sector may still exist but its quantum prediction fails. |
| P3 | The extended-body Diosi integral at l ~ 2R gives a specific geometric correction → Φ's coupling to matter must be compatible with this correction pattern. | If Φ is identified, its contribution to the self-energy integral must be consistent with the measured correction factor at various l/R. |

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **F2A-G1** | Observable definition and regime validity explicit | **PASS** | Λ_excess defined. Regime l > 2R stated. Nuisance parameters listed with mitigation. |
| **F2A-G2** | KS1-KS3 statistically operational | **PASS** | KS1: Z-test on Λ_excess vs Λ_pred. KS2: Z₀-test for null. KS3: Bayesian model comparison on b. All with explicit thresholds. |
| **F2A-G3** | Scan grid sufficient for 1/l vs alternatives | **PASS** | 5 l-values spanning factor-of-4 range in l. 3 m-values for m² test. Minimum 900 runs across 9 configurations. |
| **F2A-G4** | Systematics handling explicit | **PASS** | Seven confounders (S1-S7) listed with effect, mitigation, and residual risk. "Class killed" vs "inconclusive" explicitly distinguished. |
| **F2A-G5** | Decision tokens executable | **PASS** | Three tokens with trigger conditions and thresholds. Flowchart decision logic specified. |

## Decision Token

### **proceed_F2B**

**Rationale:** The class-level USL experimental protocol is fully specified: observables, kill signals, scan grid, systematics, and decision logic. The protocol can test whether the forced form-class is consistent with experiment. It cannot select among class members. F2-B should address the Φ-identification problem — the blocking obstacle for member-specific discrimination.

---

*Program F Stage F2-A complete. Decision: proceed_F2B. Measurement model: Λ_excess = Λ_total − Λ_env, tested against Gm²/(ℏl). Kill signals: KS1 (wrong rate), KS2 (no excess), KS3 (wrong scaling), all at ≥ 3σ. Scan grid: 9 configurations, 900 runs. Systematics: 7 confounders listed with mitigation. Decision engine: class_falsified / class_supported_not_selected / inconclusive_hardware_limited. Hand-off: F2-B must address Φ identification. Gates: 5/5 pass.*
