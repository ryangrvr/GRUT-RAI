# Book XVIII — Target Beta: Observable Discriminator Matrix

---

## Table 1 — Candidate Observable Classes

| # | Class | Mechanism | Kill Criterion | Verdict |
|---|-------|-----------|---------------|---------|
| 1 | Direct Phi measurement | Measure Phi(t); extract spectrum | No coupling H_int = g Phi O_det identified | **KILLED** |
| 2 | Metric fluctuation | delta g from delta T^Phi | Signal 10^-48; LIGO at 10^-23 (25-order gap) | **KILLED** |
| 3 | Cosmological stochastic BG | S_bath seeds GW background | Amplitude negligible; T^Phi reducible at equil. | **KILLED** |
| 4 | Decoherence rate | Bath corrections to R_dec | Environmental decoherence dominates at all T | **KILLED** |
| 5 | Precision noise floor | Fundamental floor from constitutive sector | Coupling absent; level large enough IF coupled | **CONDITIONAL** (principle only) |

---

## Table 2 — Intrinsic vs Driven Decomposition

| Component | Definition | Native (A) | Bath (B) | Discriminates? |
|-----------|-----------|-----------|----------|----------------|
| S_intrinsic,const(omega) | Noise from constitutive sector at equilibrium | **0** | 2kT tau/(1+omega^2 tau^2) | **YES** |
| S_driven(omega) | Response to time-varying X(t) | \|chi\|^2 S_X | \|chi\|^2 S_X (same) | **NO** |
| S_quantum(omega) | Standard QFT vacuum | hbar omega/2 (same) | hbar omega/2 (same) | **NO** |

**Only S_intrinsic,const differs between the two hypotheses. Driven and quantum components are identical.**

---

## Table 3 — Background Hierarchy

| Level | Source | Suppressible? | Relative to Constitutive Signal |
|-------|--------|---------------|-------------------------------|
| 1 (top) | Instrumental noise | YES (engineering) | Dominates at current sensitivity |
| 2 | Thermal/environmental | PARTIALLY (cryo, isolation) | Dominates at room temperature |
| 3 | Astrophysical foreground | PARTIALLY (by channel) | Dominates in GW band |
| 4 | Quantum vacuum | **NO** (fundamental) | Floor at hbar omega / 2 |
| 5 | Driven constitutive | YES (subtract if X(t) known) | Identical in A and B |
| 6 (bottom) | **Intrinsic constitutive** | **THIS IS THE SIGNAL** | 0 (A) or Lorentzian (B) |

---

## Table 4 — Regime Comparison: S_native vs S_bath

| Regime | tau | Corner freq (1/tau) | S_bath at corner | S_QV at corner | Bath/QV ratio | Accessible? |
|--------|-----|-------------------|-----------------|----------------|---------------|-------------|
| Cosmological | 10^15 s | 10^-15 Hz | kT × 10^15 | hbar × 10^-15 | 10^63 (3K) | **NO** (no detector) |
| Galactic | 10^10 s | 10^-10 Hz | kT × 10^10 | hbar × 10^-10 | 10^53 | **NO** (below PTA) |
| Solar system | 10^6 s | 10^-6 Hz | kT × 10^6 | hbar × 10^-6 | 10^43 | **NO** (no coupling) |
| Compact object | 10^-4 s | 10^4 Hz | kT × 10^-4 | hbar × 10^4 | 10^17 | **NO** (metric coupling 10^-48) |
| Planck | 10^-43 s | 10^43 Hz | kT_P × 10^-43 | ~hbar × 10^43 | ~1 | **NO** (no detector) |

**All regimes: inaccessible due to coupling absence, background dominance, or frequency inaccessibility.**

---

## Table 5 — Kill Criteria

| Kill Criterion | Definition | Classes Killed |
|---------------|-----------|----------------|
| **No coupling** | No H_int = g Phi O_detector identified | Classes 1, 5 (partially) |
| **Signal below background** | Signal power < detector noise floor | Class 2 (25 orders below LIGO) |
| **Amplitude negligible** | Constitutive contribution undetectable vs foreground | Class 3 |
| **Environmental dominance** | Environmental decoherence >> constitutive correction | Class 4 |
| **Frequency inaccessible** | Corner frequency outside detector band | All regimes in Table 4 |

---

## Table 6 — Final Verdict Classification

| Question | Answer |
|----------|--------|
| Measurable now? | **NO** (all 5 classes killed or conditional) |
| Measurable in principle? | **YES** (spectral shapes differ; noise floor detectable IF coupled) |
| Ontological distinction only? | **NO** (predictions are different physical quantities) |
| Controlling obstruction | **COUPLING ABSENCE** (no Phi-detector mechanism identified) |
| Secondary obstruction | Background dominance (quantum vacuum + environmental) |
| Tertiary obstruction | Frequency inaccessibility (corner freq outside bands) |

**Global Verdict: MEASURABLE IN PRINCIPLE ONLY.**

---

*Discriminator Matrix complete. 6 tables. 5 classes tested. 4 killed. 1 conditional. Verdict: principle only. Obstruction: coupling.*
