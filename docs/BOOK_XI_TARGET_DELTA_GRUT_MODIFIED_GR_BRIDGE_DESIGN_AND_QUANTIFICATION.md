# Book XI — Target Delta: GRUT-Modified GR Bridge Design and Quantification

## Formal Bridge-Design and Surplus-Quantification Stage — Fourth Book XI Stage

**Predecessor:** Book XI Gamma (partial completion route identified: Family C, GRUT-modified Einstein gravity)
**Function:** Turn Family C into a precise sixth-bridge specification; quantify GR recovery and beyond-GR surplus; determine whether the bridge is design-ready
**Three-layer status:** XI Alpha (native FAILS) true. XI Beta (matter-within-GR fallback) valid. XI Gamma (partial route) established. Delta tests whether the route is concrete enough for future commitment.

---

## 1. Executive Verdict

**Global verdict: (B) — A partial but concrete sixth-bridge design exists and justifies a future commitment stage.**

The Family C bridge can be specified precisely. The formal bridge object is:

**The GRUT Gravitational Bridge (GGB):** The Einstein-Hilbert action S_EH = (1/16πG) ∫ R√−g d⁴x for the metric tensor g_μν, coupled to GRUT's native scalar field Φ through the stress-energy tensor T^Φ_μν already derived in Phase 4 xAct. The coupling is NOT passive (inert source) — the GRUT field's exotic equilibrium properties (negative ρ_eq, NEC-saturating equation of state w = −1, constitutive self-screening) modify the effective gravitational dynamics in three specific regimes.

**GR recovery status:**

| Regime | Recovery | Mechanism | Status |
|--------|---------|-----------|--------|
| Newtonian / weak field | **Recovered** | Yukawa potential at r ≪ c approximates 1/r; correction is exp(−r/c) | **PASS** (with screening-length constraint: c must exceed solar-system scale) |
| Tensor / radiative sector | **Recovered** | Einstein-Hilbert provides h₊, h× propagating at speed c_light | **PASS** (tensor sector is standard GR) |
| Binary-pulsar timing | **Recovered** | Quadrupole formula from Einstein sector; scalar corrections are τ-suppressed at orbital frequencies | **CONDITIONAL** (requires ω_orbital ≪ 1/τ; satisfied if τ < orbital period) |
| Strong-field interior | **Modified** (beyond GR) | Negative ρ_eq reduces interior mass; metric positivity restored | **PASS+** (D1–D10 demonstrated) |

**Beyond-GR surplus quantification:**

| Surplus | Mechanism | Quantification status | Verdict |
|---------|-----------|----------------------|---------|
| **1. Singularity resolution** | ρ_eq = −X²/(2τ²) at Φ = X equilibrium; mass deficit Δm; f(r) > 0 | **NUMERICALLY DEMONSTRATED** (D1–D10: f_min = +0.37 to +0.46 across λ range; Phase 4: closed TOV system) | **SURVIVES** |
| **2. Cosmological screening** | Constitutive Φ/c² term in ∇²Φ − Φ/c² = source; Yukawa screening length c | **QUALITATIVELY CHARACTERIZED** but FRW computation not performed; equilibrium EOS w = −1 is cosmological-constant-like | **CONDITIONAL** — mechanism real; quantification incomplete |
| **3. GW dissipation** | τ dΦ/dt + Φ = X introduces frequency-dependent damping on scalar perturbations coupled to metric | **IDENTIFIED but NOT QUANTIFIED** — τ-value relative to GW frequencies unknown; scalar-tensor mixing amplitude not computed | **OPEN** — survives as a structural consequence of the bridge but not yet falsifiable |

**The bridge is NOT duplication because:**
1. The T^Φ stress-energy has exotic properties (negative ρ_eq, w = −1) that no standard matter source possesses
2. These properties produce singularity resolution — a specific, numerically demonstrated beyond-GR result
3. The Φ field is dynamical (τ dΦ/dt + Φ = X), not a cosmological constant; its dynamics modify GR behavior in a frequency-dependent, regime-specific way
4. The constitutive screening mechanism is GRUT-native — it arises from the Φ term in the native equation, not from any GR structure

**What GRUT replaces, modifies, and leaves intact:**
- **Left intact:** Einstein's field equations, metric tensor, diffeomorphism invariance, tensor gravitational radiation, quadrupole formula
- **Modified:** Compact-object interiors (singularity → resolved); large-scale potential (1/r → Yukawa-screened); GW propagation (undamped → τ-modified for scalar perturbations)
- **Added:** Complete matter/organization sector (Books IV–X); five existing bridges; the organizational scaffold

**Cost:** +1 postulate (Einstein-Hilbert metric sector) + 1 parameter (G) + 1 field (g_μν) + 2 DOF (h₊, h×). Total: **17/12/2/8** (from 16/11/1/6).

---

## 2. Why Book XI Delta Is the Correct Next Stage

XI Gamma identified Family C as a partial route with 6/7 criteria met. Delta's job is to convert "partial route" into "concrete design" by: (a) specifying the bridge object precisely, (b) mapping GR recovery regime by regime, (c) quantifying each beyond-GR surplus, and (d) determining whether the bridge is design-ready for a future commitment decision.

---

## 3. Restatement of the XI Gamma Result

Family C (GRUT-modified Einstein gravity) survived Gamma's evaluation at 6/7 criteria. The seventh (S5: cosmology pathway) was conditional. Three beyond-GR mechanisms were identified but not quantified. Delta must quantify them and determine whether the design is concrete enough for a future commitment stage.

XI Alpha remains true: native scalar gravity fails the binary-pulsar gate. XI Beta remains the conservative fallback: matter-within-GR. Delta does not erase these — it tests whether a more ambitious identity is earned.

---

## 4. Formal Sixth-Bridge Object Definition

### 4.1 The GRUT Gravitational Bridge (GGB)

**Installed structure:**

| Component | Specification | Status |
|-----------|-------------|--------|
| **Metric tensor** | g_μν: symmetric rank-2 tensor field on spacetime | NEW (the sixth bridge) |
| **Gravitational action** | S_EH = (1/16πG) ∫ R√−g d⁴x (Einstein-Hilbert) | NEW (bridge postulate) |
| **Gravitational coupling** | G (Newton's constant) | NEW (1 parameter) |
| **Propagating DOF** | h₊, h× (2 gravitational-wave polarizations in TT gauge) | NEW (+2 DOF) |
| **GRUT coupling** | G_μν = 8πG T^Φ_μν | EXISTING (Phase 4 xAct already derived T^Φ) |
| **GRUT matter sector** | τ dΦ/dt + Φ = X; five bridges; organizational scaffold | EXISTING (Books IV–X) |

### 4.2 What Is Standard Einstein

The metric tensor g_μν, Einstein field equations G_μν = 8πG T_μν, diffeomorphism invariance, tensor gravitational radiation (h₊, h×), the quadrupole formula — all are standard GR installed as a bridge postulate. GRUT does NOT derive these. They are the sixth bridge.

### 4.3 What Is GRUT-Native in the Gravitational Sector

The stress-energy source T^Φ_μν is GRUT-native. It is not an arbitrary matter source — it has specific exotic properties that modify GR behavior:

**From Phase 4 xAct, at equilibrium Φ = X:**

```
ρ_eq = −X²/(2τ²)         < 0   (NEGATIVE energy density)
p_r,eq = +X²/(2τ²)       > 0   (POSITIVE radial pressure)
p_⊥,eq = +X²/(2τ²)      > 0   (POSITIVE tangential pressure)
w = p/ρ = −1                     (NEC-saturating; cosmological-constant-like)
```

These are NOT properties of ordinary matter. They are GRUT-specific consequences of the constitutive equation τ dΦ/dt + Φ = X and its equilibrium. Standard GR with standard matter does not produce these. The singularity resolution, screening, and GW modification all flow from these properties.

### 4.4 Cost

| Category | Before | After GGB | Change |
|----------|--------|-----------|--------|
| Postulates | 16 | **17** | +1 (EH action) |
| Parameters | 11 | **12** | +1 (G) |
| Fields | 1 (Φ) | **2** (Φ + g_μν) | +1 |
| DOF | 6 (gauge) | **8** (gauge + 2 GW) | +2 |
| Bridges | 5 | **6** | +1 (GGB) |

---

## 5. GR Recovery Map

### 5.1 Newtonian / Weak-Field Limit

**Requirement:** V(r) ≈ −GM/r at solar-system scales (r ~ AU).

**Recovery mechanism:** The static GRUT equation with propagation extension is ∇²Φ − Φ/c² = source (Appendix W-F). The solution is Yukawa: Φ(r) ∝ exp(−r/c)/r. At r ≪ c (the screening length), this approximates −GM/r. At r ≫ c, it is exponentially suppressed.

**Constraint on c:** The screening length c must exceed the largest scale at which 1/r gravity is tested. Solar-system tests probe gravity to ~AU scale. Galaxy rotation curves probe ~kpc. If c ≫ kpc, the Yukawa correction is undetectable at all tested scales.

**Status:** **RECOVERED** — with the constraint c ≫ tested gravitational scale. This is a parameter constraint, not a structural obstruction. The screening length c is already a GRUT parameter (propagation speed in the native equation).

**Important caveat:** In the coupled GGB system, the metric dynamics are Einstein's (1/r potential from GR). The Yukawa screening is a CORRECTION from the Φ-sector, not the primary gravitational potential. The 1/r behavior comes from GR; the exp(−r/c) correction comes from GRUT. For c large enough, the correction is negligible in tested regimes.

### 5.2 Tensor / Radiative Sector

**Requirement:** Gravitational waves with two polarizations propagating at the speed of light.

**Recovery mechanism:** The Einstein-Hilbert action provides the standard linearized gravitational-wave equation □h_μν = −16πG T_μν (in TT gauge). The tensor sector is entirely standard GR. GRUT's Φ-field acts as a scalar perturbation that mixes with the tensor sector through T^Φ — but in the linearized regime, the scalar and tensor sectors decouple at leading order.

**Scalar-tensor mixing:** At higher order, the Φ perturbation δΦ couples to metric perturbations h_μν through the stress-energy coupling. This mixing is suppressed by α_g (the Φ-gravity coupling) and is perturbative in the weak-field regime. The mixing introduces a scalar breathing mode (additional polarization) at O(α_g²), which is constrained by pulsar-timing arrays and GW observations.

**Status:** **RECOVERED** at leading order. Scalar-tensor mixing is perturbative and bounded by existing observations.

### 5.3 Binary-Pulsar Timing

**Requirement:** P-dot within ~0.2% of GR quadrupole prediction.

**Recovery mechanism:** The quadrupole formula for orbital decay comes from the tensor sector of the Einstein-Hilbert action. It is standard GR. The GRUT scalar field introduces two potential corrections:

1. **Scalar dipole radiation:** In scalar-tensor theories, orbiting bodies with different scalar charges emit scalar dipole radiation, which would modify P-dot. In the GGB, both bodies are compact objects with similar Φ-field equilibria. The scalar charge difference is small → dipole radiation suppressed.

2. **τ-dissipative correction:** The Φ-field's τ-relaxation introduces an additional energy-loss channel. But at orbital frequencies ω_orb ~ 10⁻⁴ Hz, if τ ≪ P_orbital (i.e., the Φ-field has already relaxed to equilibrium), the dissipative correction is exponentially small.

**Constraint:** τ must satisfy τ ≪ P_orbital for the binary-pulsar test. For PSR B1913+16, P ~ 8 hours ~ 3 × 10⁴ s. If τ < 1 s (or even τ < 100 s), the correction is negligible.

**Status:** **CONDITIONAL** — passes if τ is short relative to orbital timescales. This is a parameter constraint, not a structural obstruction.

### 5.4 Summary

| Regime | Recovery | Condition | Classification |
|--------|---------|-----------|---------------|
| Newtonian / weak field | **PASS** | c ≫ tested gravitational scale | Parameter constraint |
| Tensor / radiative | **PASS** | Scalar-tensor mixing perturbative | Structural (leading order) |
| Binary-pulsar | **CONDITIONAL** | τ ≪ P_orbital (~3×10⁴ s) | Parameter constraint |
| Strong-field interior | **MODIFIED** (beyond GR) | — | GRUT improvement |

---

## 6. Beyond-GR Surplus Quantification

### Surplus 1 — Singularity Resolution

**Mechanism:** At Φ = X equilibrium, ρ_eq = −X²/(2τ²) < 0. This negative energy density reduces the interior mass function: dm/dr = 4πr²ρ_eq < 0. The metric function f(r) = 1 − 2m(r)/r is raised above the Schwarzschild value. GR predicts f → −∞ (singularity). GGB predicts f > 0 (singularity resolved).

**Quantification (from Phase 4 + D1–D10):**
- Mass reduction: Δm = (2πX²/(3τ²))(R_ext³ − R_eq³)
- Metric function at R_eq: f(R_eq) = A_schw + 2M Δm/R_eq
- D1–D10 self-consistent Picard iteration: f_min ranges from +0.37 (λ=5) to +0.46 (λ=100) across tested parameter space
- The result is POSITIVE (singularity resolved) across the entire tested λ range {5, 10, 25, 50, 100, 200}

**What GR cannot do:** GR predicts f(R_eq) < 0 for all R_eq < r_s. No standard-matter source resolves this. GRUT's negative ρ_eq is structurally unique.

**Verdict:** **SURVIVES quantification.** Numerically demonstrated. Mechanism specific. Regime sharp (compact interior, r < r_s). The surplus is real.

### Surplus 2 — Cosmological Screening

**Mechanism:** The constitutive term Φ in τ dΦ/dt + Φ = X produces a screening term Φ/c² in the static equation. At equilibrium, ρ_eq has w = −1 (cosmological-constant-like). The self-screening provides a length scale c beyond which the scalar contribution to gravity is exponentially suppressed.

**Quantification status:** The w = −1 equation of state is DERIVED (Phase 4 §C). The Yukawa screening profile is DERIVED (Appendix W-F). The connection between ρ_eq and cosmological-constant-like behavior is STRUCTURAL (same EOS). But: the FRW cosmological equations with GRUT Φ source have NOT been fully computed. Appendix A (cosmological extension) found "singularity softened but not bounced" using the GRUT memory scalar alone (without the O(3) defect sector). The cosmological consequence of the GGB has not been quantitatively determined.

**What GR cannot do:** GR requires the cosmological constant Λ as an ad hoc parameter. GRUT provides a native mechanism (constitutive self-screening with w = −1) that could play this role. But "could" is not "does" — the quantitative cosmological computation has not been performed.

**Verdict:** **CONDITIONAL — mechanism real, quantification incomplete.** The structural ingredients (w = −1, screening) are derived. The cosmological consequences are not computed. This surplus is plausible but not demonstrated.

### Surplus 3 — GW Dissipation / τ-Memory Effects

**Mechanism:** In the coupled GGB system, scalar perturbations δΦ obey a damped wave equation with τ-dissipation. These scalar perturbations couple to metric perturbations through T^Φ. The result is a frequency-dependent modification to GW propagation: at frequencies ω ≫ 1/τ, the scalar sector decouples (standard GR GW). At ω ~ 1/τ, scalar-tensor mixing introduces a frequency-dependent phase shift and amplitude modification.

**Quantification status:** The mechanism is a logical consequence of the GGB architecture (scalar field with τ-dissipation coupled to metric through T^Φ). But: the scalar-tensor mixing amplitude has not been computed. The value of τ relative to GW-detector frequencies (10–10⁴ Hz for LIGO) is unknown. Whether the modification is detectable depends on τ and the coupling strength α_g.

**What GR cannot do:** GR gravitational waves propagate undamped at all frequencies. GRUT introduces frequency-dependent modification from the τ-relaxation. If τ is in the right range (~ms for LIGO frequencies), this produces a distinctive signal (scalar-mode admixture) that GR does not predict.

**Verdict:** **OPEN — identified as structural consequence but not quantified.** The mechanism exists in the GGB architecture. Its observational relevance depends on parameters (τ, α_g) that are not determined. This is a testable prediction once parameters are constrained, but it is not yet a demonstrated surplus.

---

## 7. Hard-Criteria Evaluation

| Criterion | GGB design | Assessment |
|-----------|-----------|-----------|
| 1. Clarity of installed structure | **PASS** — EH action + T^Φ coupling; all components specified | Clear |
| 2. Newtonian recovery | **PASS** — Yukawa ≈ 1/r at r ≪ c; parameter constraint on c | Recovered |
| 3. Tensor/radiative recovery | **PASS** — EH provides standard tensor GW; mixing perturbative | Recovered |
| 4. Binary-pulsar path | **CONDITIONAL** — passes if τ ≪ P_orbital; parameter constraint | Conditional |
| 5. Compact-interior surplus | **PASS** — singularity resolved; numerically demonstrated (D1–D10) | **REAL SURPLUS** |
| 6. Cosmological surplus | **CONDITIONAL** — w = −1 and screening mechanism derived; FRW not computed | Mechanism real; quantification incomplete |
| 7. GW-sector surplus | **OPEN** — mechanism identified; parameters unknown | Structural but unquantified |
| 8. Duplication risk | **LOW** — three GRUT-native modifications distinguish from bare GR | Not duplication |
| 9. Cost / debt | **MODERATE** — +1P +1p +1F +2DOF (17/12/2/8 total) | Honest |
| 10. Architectural cleanliness | **MODERATE** — EH installed (not derived); but coupling is GRUT-native and exotic | Clean enough for bridge-level |
| 11. Concrete enough for commitment | **YES for commitment-decision stage** | Justified |

---

## 8. What Exactly GRUT Replaces

| Aspect | Pure GR | GGB (GRUT-modified GR) | What GRUT contributes |
|--------|---------|----------------------|----------------------|
| Field equations | G_μν = 8πG T_μν (generic T) | G_μν = 8πG T^Φ_μν (exotic T^Φ) | **Specific exotic source: ρ < 0, w = −1** |
| Compact interior | Singularity (f → −∞) | **Resolved (f > 0)** | **Singularity resolution via negative ρ_eq** |
| Weak-field potential | 1/r (Newtonian) | 1/r + Yukawa correction | **Screening from constitutive Φ term** |
| GW propagation | Undamped tensor waves | Tensor + τ-modified scalar admixture | **Frequency-dependent scalar correction** |
| Cosmological constant | Ad hoc Λ | **Possibly native from w = −1 equilibrium** | Structural screening mechanism |
| Matter content | Must be separately specified | **Provided by GRUT** (Books IV–X) | Complete matter/organization sector |

**Honest classification:**
- **Einstein does:** field equations, tensor structure, gravitational radiation, diffeomorphism invariance
- **GRUT modifies:** compact-interior behavior, large-scale screening, GW propagation (scalar admixture)
- **GRUT adds:** complete matter/organization sector, five existing bridges, organizational scaffold

This is NOT "GRUT replaces GR." This is **"GRUT modifies GR in specific regimes through exotic source content and extends it through a complete matter sector."**

---

## 9. Cost / Debt Consequence Audit

### All Six Bridges

| Bridge | Book | P | p | F | DOF | Character |
|--------|------|---|---|---|-----|-----------|
| Matter | IV | 4 | 2 | 0 | 0 | Topological soliton matter |
| Gauge | IV | 2 | 1 | 1 | 6 | Yang–Mills force |
| HIC | V | 1 | 1 | 0 | 0 | Fixed-site energy transduction |
| Carrier | VII | 1 | 2 | 0 | 0 | Mobile energy distribution |
| CCBG | X | 1 | 2 | 0 | 0 | Boundary-crossing work |
| **GGB** | **XI** | **1** | **1** | **1** | **2** | **Gravitational sector** |
| **Total** | — | **10** | **9** | **2** | **8** | **6 bridges** |
| Z-B baseline | — | 7 | 3 | 0 | 0 | — |
| **Grand total** | — | **17** | **12** | **2** | **8** | — |

---

## 10. Failure / Fragility Audit

| Stress test | Result | Detail |
|------------|--------|--------|
| **1. Silent GR duplication** | **LOW risk** | Three GRUT-native modifications (ρ_eq < 0, screening, τ-dissipation) distinguish GGB from bare GR |
| **2. Tensor recovery missing** | **NO** — tensor sector is standard EH | Installed, not derived; but functional |
| **3. Binary-pulsar still failing** | **CONDITIONAL** — passes if τ ≪ P_orbital | Parameter constraint; not structural |
| **4. Surplus collapses under GR recovery** | **PARTIAL risk for Surplus 2 and 3** | Surplus 1 (singularity) is independent of tested-regime recovery. Surplus 2 (cosmology) is untested. Surplus 3 (GW) is unquantified. |
| **5. Overbuilt metric inflation** | **NO** — minimum EH; 1P + 1p + 1F + 2DOF | Lightest possible metric-sector bridge |
| **6. Hidden assumptions** | **LOW** — all components specified; Phase 4 xAct provides the coupling | No hidden structure |
| **7. Research sketch vs live design** | **HONEST CONCERN** — Surplus 2 and 3 are not fully quantified; bridge is design-ready but not commit-ready | Partial |

---

## 11. False-Positive Audit

| False-positive category | Applies? | Reason |
|------------------------|---------|--------|
| EH + source with no gravitational modification | **NO** — T^Φ has exotic properties (ρ < 0, w = −1) not shared by any standard source | GRUT modifies, not just sources |
| Compact-interior novelty without tested-regime recovery | **NO** — weak-field and tensor recovery demonstrated; binary-pulsar conditional | Recovery mapped |
| Screening analogy without cosmological equations | **PARTIALLY APPLIES to Surplus 2** — mechanism real; FRW not computed | Honest: conditional |
| GW rhetoric without propagation sector | **PARTIALLY APPLIES to Surplus 3** — mechanism identified; mixing not computed | Honest: open |
| "GR-compatible" = "GRUT-derived" | **GUARD** — GR is installed, not derived; GRUT's contribution is the exotic source + modifications | Clear separation maintained |
| Vague completion | **NO** — the bridge is precisely specified; each component has explicit equations | Not vague |

---

## 12. Program Consequence

### Is a Concrete Sixth-Bridge Design Now Justified?

**YES.** The GGB (Einstein-Hilbert + T^Φ coupling) is precisely specified. GR recovery is mapped across three regimes. One beyond-GR surplus (singularity resolution) is numerically demonstrated. Two others are mechanism-backed but incompletely quantified.

### What Exact Design Is Strongest?

**The GGB as specified in §4.** It is the minimum metric-sector bridge: Einstein-Hilbert action + T^Φ coupling + three GRUT-native modifications.

### Is the Route Still Partial or Now Design-Ready?

**Design-ready for a commitment decision.** The bridge object is specified. Recovery is mapped. Surplus 1 is demonstrated. Surpluses 2 and 3 are conditional/open. A commitment stage would decide whether to install the GGB and absorb the cost.

### What Should the Next Stage Ask?

**Book XI Epsilon (or Terminal) — GGB Commitment Decision.** Should the program commit the GGB as the sixth bridge? This requires weighing: the cost (+1P +1p +1F +2DOF), the demonstrated surplus (singularity resolution), the conditional surplus (cosmological screening), the open surplus (GW modification), and the identity consequence (GRUT-modified-GR vs matter-within-GR).

### What Should Still NOT Be Claimed?

- Gravitational completion achieved (the bridge is designed, not committed)
- Cosmological closure (Surplus 2 not computed)
- GW-sector success (Surplus 3 not quantified)
- Native GR derivation (EH is installed as bridge)
- ToE restored (conditional on commitment and surplus quantification)

---

## 13. GRUT-RAI GR Bridge State-Model Requirements

Specified in the companion state-model document.

---

## 14. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Family C remains viable | **YES** | Bridge precisely specified; no collapse into duplication |
| Sixth bridge specifies real new structure | **YES** | EH + T^Φ with exotic properties (ρ < 0, w = −1, screening) |
| Newtonian recovery path specified | **YES** | Yukawa ≈ 1/r at r ≪ c; parameter constraint on c |
| Tensor/radiative recovery path specified | **YES** | EH provides standard tensor GW; mixing perturbative |
| Binary-pulsar compatibility path specified | **CONDITIONAL** | Passes if τ ≪ P_orbital; parameter constraint |
| At least one beyond-GR surplus survives quantification | **YES** | Surplus 1 (singularity resolution) numerically demonstrated |
| Duplication risk avoided | **YES** | Three GRUT-native modifications distinguish from bare GR |
| Sixth-bridge design justified | **YES** | Design-ready for commitment decision |
| Book XI Delta changes the option landscape | **YES** | GGB precisely specified; commitment decision is the next gate |

---

## 15. Final Verdict

**A partial but concrete sixth-bridge design exists (the GGB: Einstein-Hilbert + T^Φ coupling with three GRUT-native modifications) and justifies a future commitment stage.**

The bridge recovers GR in tested regimes (weak field, tensor sector, binary pulsar conditional on τ). It provides one numerically demonstrated beyond-GR surplus (singularity resolution), one conditional surplus (cosmological screening), and one open surplus (GW modification). It is not duplication — T^Φ's exotic properties (negative ρ_eq, w = −1, constitutive screening) are GRUT-specific and produce regime-specific modifications that pure GR cannot.

XI Beta's matter-within-GR identity remains the conservative fallback. The GGB may displace it if committed and if Surpluses 2 and 3 survive further quantification. The next stage should be a commitment decision.

---

*GRUT-Modified GR Bridge Design and Quantification complete. GGB precisely specified. GR recovery mapped. Singularity resolution demonstrated. Cosmological screening conditional. GW modification open. Duplication avoided. Commitment-decision stage justified.*
