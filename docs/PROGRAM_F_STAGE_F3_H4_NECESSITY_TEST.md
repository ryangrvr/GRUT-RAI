# Program F — Stage F3: H4 Necessity Test (Thermodynamic Completion vs Repackaging)

**Predecessor:** F2-B (phi_identification_narrowed, H4 = entropy-density scalar ranked #1).

**Question:** Is H4 trivial repackaging of known relativistic thermodynamics, or does it add unique predictive content?

---

## 1. Formal Mapping to Known Frameworks

### The H4 constitutive law

```
τ u^μ ∇_μ s + s = s_eq(g)
```

where s is the entropy density, u^μ is the fluid four-velocity (= n^μ the foliation normal in the rest frame), τ is the relaxation time, and s_eq(g) is the equilibrium entropy determined by local geometry.

### Mapping A: Relativistic hydrodynamics

**First-order (Eckart / Landau-Lifshitz):**

In relativistic hydrodynamics, the entropy current is:

```
s^μ = s u^μ + q^μ / T
```

where q^μ is the heat flux. The entropy production rate is:

```
∇_μ s^μ = σ_s ≥ 0  (second law)
```

In the Landau frame (u^μ is the energy-flow velocity), the first-order constitutive relation for heat conduction is:

```
q^μ = -κ (g^{μν} + u^μ u^ν)(∂_ν T + T u^ν ∇_ν u_μ)  [Fourier's law in curved spacetime]
```

The entropy evolution in the absence of heat flow (q = 0) and for a fluid at rest in a gravitational field:

```
u^μ ∇_μ s = σ_s / n  [entropy per particle production rate]
```

**Comparison to H4:**

| H4 term | Standard hydro equivalent | Status |
|---------|--------------------------|:------:|
| u^μ ∇_μ s | Comoving entropy derivative | **ALREADY STANDARD** |
| s_eq(g) | Tolman-Ehrenfest equilibrium entropy (s at T_eq = T₀/√g₀₀) | **ALREADY STANDARD** |
| τ | Relaxation timescale | **ALREADY STANDARD** (= thermalization time in kinetic theory) |
| τ u^μ ∇_μ s + s = s_eq | First-order relaxation toward equilibrium | **SEE BELOW** |

**The specific equation τ ṡ + s = s_eq is Maxwell-Cattaneo-type relaxation applied to entropy density.** This is a known construction in extended irreversible thermodynamics (EIT), developed by Jou, Casas-Vázquez, Lebon (1988-present) and Müller-Ruggeri (rational extended thermodynamics). The first-order relaxation equation for a thermodynamic variable toward equilibrium, with a finite relaxation time, is the DEFINING FEATURE of EIT.

**Classification: The H4 equation IS the EIT entropy relaxation equation in a gravitational field.** It is not new.

### Mapping B: Tolman-Ehrenfest conditions

The Tolman-Ehrenfest equilibrium condition for temperature in a static gravitational field:

```
T(x) √g₀₀(x) = T₀ = const  (Tolman 1930)
```

This gives the equilibrium temperature profile. The equilibrium entropy s_eq follows from the equation of state s = s(T, ρ, ...) evaluated at T = T_eq(x) = T₀/√g₀₀(x).

**Comparison to H4:** s_eq(g) in the H4 equation IS the Tolman-Ehrenfest equilibrium entropy. The mapping is:

```
X(g) = s_eq(g) = s(T₀/√g₀₀, ρ_eq, ...)
```

This uses the Ricci scalar R through the Einstein equation (g₀₀ depends on the matter content and hence on R). The specific AB1 choice X = β + αR is a LINEARIZATION of s_eq(g₀₀) around flat space:

```
s_eq ≈ s₀ + (ds/dg₀₀)|_flat × δg₀₀ + ...
     = s₀ + α × R + ...    [where α encodes the thermal response to curvature]
```

**Classification: s_eq(g) = Tolman-Ehrenfest equilibrium entropy.** The linear approximation X = β + αR corresponds to the leading-order thermal response. **ALREADY STANDARD.**

### Mapping C: Entropy production

The standard entropy production in irreversible thermodynamics:

```
σ_s = (1/τ)(s - s_eq)² / s_eq  ≥ 0  [near equilibrium, quadratic form]
```

The H4 equation τ ṡ + s = s_eq gives:

```
ṡ = (s_eq - s) / τ
σ_s ~ (s_eq - s)² / τ  [from standard irreversible thermo]
```

This is the Onsager linear-response regime of entropy production. **ALREADY STANDARD.**

### Term-by-term classification

| H4 element | Known framework equivalent | Classification |
|-----------|--------------------------|:-:|
| τ u^μ ∇_μ s | Comoving entropy rate (hydro) | **ALREADY STANDARD** |
| s = s_eq(g) at equilibrium | Tolman-Ehrenfest (1930) | **ALREADY STANDARD** |
| τ = thermalization timescale | Kinetic theory relaxation time (Boltzmann τ_c) | **ALREADY STANDARD** |
| τ ṡ + s = s_eq | Maxwell-Cattaneo / EIT relaxation equation | **ALREADY STANDARD** |
| X = β + αR (linearization) | Linear thermal response to curvature | **EQUIVALENT under variable redefinition** (α = ds_eq/dR)|_flat) |
| CTP derivation of the equation | Variational formulation of dissipative thermo | **GENUINE ADDITION** (see below) |
| USL = Gm²/(ℏl) | Newtonian gravitational dephasing | **INDEPENDENT** (not specific to H4) |

### The one genuinely additional element

The CTP DERIVATION of the constitutive law from a variational principle (Iota-Prime) IS genuinely additional. Standard irreversible thermodynamics and EIT write the entropy relaxation equation PHENOMENOLOGICALLY — they postulate it. The GRUT program derives it from a CTP effective action, proving it is the classical EOM of a well-defined action principle. This is a FORMAL UPGRADE (from phenomenological postulate to variational derivation) but it does not change the physics content — the equation is the same.

---

## 2. Three Uniqueness Tests

### U1: First-order form uniqueness

**Question:** Is τ u^μ ∇_μ s + s = s_eq the ONLY admissible entropy relaxation equation?

**Test:** Apply the T2-mid constraints (covariance + irreversibility + first-order + scalar + unique attractor):

Under these constraints (E2-B), the dynamics must take the form τ n^μ ∇_μ Φ + Φ = X(g). With Φ = s: the equation IS forced (within the T2-mid forced class). But the T2-mid constraints ALSO admit:

- Second-order: τ₁τ₂ ∇² s + τ₁ ṡ + s = s_eq (telegraph equation) — excluded IF we impose first-order
- Memory kernel: ∫ K(t-t') ṡ(t') dt' + s = s_eq — excluded IF we impose Markovian
- Nonlinear: τ ṡ + f(s) = X(g) — excluded IF we impose linear

**Result:** The first-order form is forced IF we assume first-order + Markovian + linear + scalar. But these assumptions are themselves NOT uniquely motivated by thermodynamics:

- Second-order (telegraph) IS used in EIT for causal heat propagation
- Memory kernels ARE present in non-Markovian transport
- Nonlinear entropy production IS standard far from equilibrium

**Verdict: NOT UNIQUE.** The first-order form is the SIMPLEST admissible form — the leading-order EFT (E3 finding). It is one member of a family that includes second-order, memory-kernel, and nonlinear forms. All are standard in irreversible thermodynamics. **ALREADY KNOWN in EIT.**

### U2: Equilibrium target uniqueness

**Question:** Is s_eq(g) uniquely fixed?

**Test:** The Tolman-Ehrenfest condition fixes T_eq(x) = T₀/√g₀₀(x) for a static spacetime. Given an equation of state s = s(T, P, ...), the equilibrium entropy s_eq = s(T_eq, P_eq, ...) is determined.

**But:** The equation of state s(T, P, ...) depends on the MATTER CONTENT (ideal gas, radiation, degenerate fermion gas, etc.). Different matter has different s(T, P). The equilibrium entropy is not universally determined by geometry alone — it depends on what the matter IS.

**Residual freedom:** s_eq(g) = s(T₀/√g₀₀, P_eq(g), matter_type). The function s_eq depends on:
- T₀ (free: the global equilibrium temperature)
- The equation of state (free: depends on matter content)
- The gravitational potential g₀₀ (determined by the metric)

**Verdict: NOT UNIQUE.** s_eq(g) depends on the matter content and the global temperature, both of which are free. The geometry constrains the TEMPERATURE PROFILE but not the equation of state. This corresponds to the EFT parameters β and α being free — β encodes the equation of state, α encodes the thermal response coefficient. **STANDARD THERMO.**

### U3: τ determination

**Question:** Is τ derivable from fundamental principles?

**Test:** In kinetic theory, the relaxation time τ is determined by the collision cross-section and particle density:

```
τ ≈ 1 / (n σ v_th)  [for a dilute gas]
```

This IS derivable from microscopic physics (Boltzmann equation). For more complex systems (liquids, plasmas, solids), τ depends on the transport coefficients, which depend on the detailed microscopic interactions.

**Is τ universal?** No. τ depends on the SPECIFIC MATTER AND ITS STATE. A dilute gas has τ ~ microseconds to milliseconds. A neutron star interior has τ ~ seconds to years. A cosmological plasma has τ ~ Hubble time. The GRUT Level-1 formula 1/τ = 1/τ₀ + 1/t_dyn, if identified with the kinetic-theory relaxation time, says: the thermalization rate is the sum of a background rate (1/τ₀, from non-gravitational collisions) and a gravitational rate (1/t_dyn ~ √(Gρ), from gravitational collapse timescale). This IS physically motivated — in a self-gravitating system, the gravitational dynamical time sets a floor on the equilibration time.

**But:** The Level-1 formula is a SPECIFIC parametrization of τ(g). Kinetic theory gives a MORE DETAILED (and matter-dependent) τ. The Level-1 formula captures the gross dependence on gravitational potential but not the full microscopic physics.

**Verdict: PARTIALLY DERIVABLE.** τ is derivable from kinetic theory for specific matter types. It is NOT universal (depends on matter content). The Level-1 formula is a coarse-grained approximation of the kinetic-theory result. **STANDARD KINETIC THEORY** with gravitational correction.

---

## 3. New-Prediction Test

### Candidate novel predictions from H4

| # | Candidate prediction | Standard thermo+GR equivalent? | Novelty | Measurability | Discriminating power |
|---|---------------------|:------------------------------:|:-------:|:------------:|:-------------------:|
| NP1 | Entropy density relaxes toward Tolman-Ehrenfest equilibrium with timescale τ | YES (Tolman 1930 + kinetic theory) | **EQUIVALENT** | HIGH | ZERO (already known) |
| NP2 | τ is bounded below by the gravitational dynamical time 1/t_dyn = √(Gρ) | PARTIALLY (Level-1 formula). Kinetic theory gives τ from collisions; gravitational contribution is a correction, not the leading term for most systems. | **AMBIGUOUS** | MEDIUM (measure τ near compact objects and compare to √(Gρ)) | LOW (hard to disentangle gravitational τ-correction from collision-dominated τ) |
| NP3 | The CTP action provides a variational derivation of the entropy relaxation equation | NOT available in standard thermo (EIT postulates the equation) | **NOVEL** (formal, not physical) | N/A (mathematical structure, not an observable) | ZERO (formal upgrade, same equation) |
| NP4 | USL: Λ = Gm²/(ℏl) for massive superpositions | INDEPENDENT of H4 (Newtonian gravity, any theory) | **NOT H4-SPECIFIC** | MEDIUM (hardware-limited) | ZERO (for H4 vs other candidates) |
| NP5 | Bistability in the entropy density (two equilibrium entropy values at the same curvature) | NOT standard (standard thermo has unique equilibrium entropy for given T, P). But: phase transitions DO produce multiple equilibria. If interpreted as a phase transition, this IS standard. | **AMBIGUOUS** | LOW (requires identifying the two "attractors" as distinct thermodynamic phases) | MEDIUM (if the bistability has observable consequences not predictable by standard phase-transition theory) |

### Assessment

- **NP1:** No new physics. Standard Tolman-Ehrenfest + kinetic theory.
- **NP2:** The Level-1 gravitational correction to τ is a SPECIFIC claim but hard to disentangle experimentally from the dominant collision-determined τ. Ambiguous novelty.
- **NP3:** The CTP derivation is formally novel but produces the same equation. No new observable.
- **NP4:** Not H4-specific. Shared by all class members.
- **NP5:** Bistability as a thermodynamic phase transition is standard. Bistability in entropy density at a given curvature (the GRUT-II Nu result) COULD be interpreted as predicting a new type of gravitational phase transition — where the local entropy jumps between two values as a function of curvature. This is the ONE genuinely potentially novel prediction. But its status is AMBIGUOUS: it could be a standard phase transition repackaged, or it could be a genuinely new gravitational-thermodynamic effect.

---

## 4. Decision Matrix

### Evidence summary

| Test | Result | Points toward |
|------|--------|:------------:|
| Mapping A (hydro) | H4 equation = EIT entropy relaxation in curved spacetime | REPACKAGING |
| Mapping B (Tolman-Ehrenfest) | s_eq(g) = standard thermal equilibrium in gravity | REPACKAGING |
| Mapping C (entropy production) | σ_s = Onsager linear response | REPACKAGING |
| U1 (form uniqueness) | First-order is simplest, not unique; family includes 2nd-order, memory, nonlinear | REPACKAGING |
| U2 (target uniqueness) | s_eq depends on equation of state (free); not geometry-only | REPACKAGING |
| U3 (τ determination) | Derivable from kinetic theory (matter-dependent) | REPACKAGING |
| NP1-NP4 | All either standard or H4-independent | REPACKAGING |
| NP5 (bistability as gravitational phase transition) | Potentially novel — AMBIGUOUS | CONDITIONAL UPGRADE |
| CTP derivation (NP3) | Formally novel: variational principle for EIT | CONDITIONAL UPGRADE (formal, not physical) |

### Score

| Criterion | Repackaging evidence | Upgrade evidence |
|-----------|:-------------------:|:----------------:|
| Physical content | 6 items (mappings, U1-U3, NP1-NP4) | 0 items confirmed novel |
| Formal content | — | 1 item (CTP derivation: same equation, new derivation) |
| Potentially novel | — | 1 item (NP5: bistability as gravitational phase transition — AMBIGUOUS) |

### Decision

### **h4_repackaging** (with two qualifications)

**Confidence: 0.75**

**Evidence:** The H4 identification maps the GRUT constitutive law to a known equation (EIT entropy relaxation in a gravitational field), with known equilibrium conditions (Tolman-Ehrenfest), known relaxation timescale (kinetic theory), and known entropy production (Onsager). Every physical element of H4 exists in the standard literature. The GRUT-specific additions are:

1. **The CTP variational derivation** — formally novel (the EIT equation is usually postulated, not derived from an action). This is a genuine mathematical contribution but does not change the physics.

2. **The bistability prediction (NP5)** — if the two-attractor structure (GRUT-II Nu) is mapped to H4, it predicts a novel gravitational-thermodynamic phase transition where the local entropy density can exist at two distinct equilibria for the same curvature. This is NOT in the standard EIT literature. Its status is AMBIGUOUS: it could be a standard phase transition in disguise, or it could be genuinely new. Resolution requires explicit construction and comparison to known phase-transition theories.

---

## 5. Program Impact Update

### Since h4_repackaging:

**What remains scientifically valuable:**

1. **The CTP derivation** of irreversible thermodynamics in a gravitational field. This is a contribution to the FORMALISM of non-equilibrium statistical mechanics, even if the resulting equation is known. The derivation chain (CTP action → variation → EIT equation) is cleaner and more rigorous than the standard phenomenological derivation.

2. **The USL prediction** — unchanged. It is a property of Newtonian gravity, independent of H4 or any Φ identification. It remains the program's primary testable output.

3. **The forced form-class** (Program E) — unchanged. The classification of allowed dynamics under covariance + irreversibility is a valid structural result.

4. **The extended-body correction** (Kappa-Prime) and the corrected operating point — unchanged and valuable for any experiment testing gravitational decoherence.

5. **The falsification protocol** (F2-A) — unchanged and operational. It tests the entire class, not a specific member.

6. **The program methodology** — the audit/correct/close discipline, the regime tagging, the blacklist system, the Feynman tests (D1, D2). This is transferable to other theory programs.

**What is NOT a new claim:**

- The constitutive law τ ṡ + s = s_eq(g) is NOT a new equation. It is EIT in a gravitational field.
- The Level-1 formula is NOT a new transport result. It is a coarse-grained kinetic-theory estimate.
- The equilibrium s_eq(g) is NOT a new equilibrium condition. It is Tolman-Ehrenfest.
- H4 does NOT elevate GRUT from "generic EFT" to "uniquely determined theory."

**New claims allowed (precisely two):**

1. "The EIT entropy relaxation equation in a gravitational field can be derived from a CTP effective action." (Formal contribution. Status: DERIVED.)

2. "The nonlinear extension (GRUT-II Nu bistability) predicts a potentially novel gravitational-thermodynamic phase transition." (Status: AMBIGUOUS/OPEN. Requires further investigation to confirm or refute novelty.)

**Claims still forbidden:**

All existing forbidden claims (FF1-FF10) remain. Additionally:
- "H4 provides new physics beyond standard irreversible thermodynamics" — **FORBIDDEN** (not demonstrated).
- "The GRUT constitutive law is a new equation" — **FORBIDDEN** (it is EIT in curved spacetime).

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **F3-G1** | Formal equivalence mapping complete | **PASS** | Three mappings (hydro, Tolman-Ehrenfest, entropy production). Term-by-term classification: 5 "already standard," 1 "equivalent under redefinition," 1 "genuine addition" (CTP derivation). |
| **F3-G2** | U1/U2/U3 explicitly answered | **PASS** | U1: form not unique (EIT family). U2: target not unique (depends on EOS). U3: τ partially derivable (kinetic theory). |
| **F3-G3** | New-prediction test completed | **PASS** | Five candidates tested. NP1-NP4: no novelty. NP5: ambiguous (bistability as gravitational phase transition). NP3: formally novel (CTP derivation). |
| **F3-G4** | Decision token evidence-backed | **PASS** | h4_repackaging with two qualifications. Evidence: 6 repackaging items, 0 confirmed novel physics, 2 formal/ambiguous additions. Confidence 0.75. |
| **F3-G5** | Claim policy updated without inflation | **PASS** | Two new claims allowed (CTP derivation of EIT, and bistability phase transition as OPEN). Existing forbidden claims maintained. No inflation. |

## Decision Token

### **h4_repackaging**

(With two qualifications: CTP derivation is formally novel; bistability as gravitational phase transition is AMBIGUOUS/OPEN.)

---

*Program F Stage F3 complete. Decision: h4_repackaging (confidence 0.75). The H4 identification maps GRUT to Extended Irreversible Thermodynamics in a gravitational field — a known framework. Every physical element (equation, equilibrium, τ, entropy production) exists in the standard literature. Two qualifications: (1) the CTP variational derivation is formally novel (same equation, new derivation method); (2) the bistability prediction (NP5) is potentially novel but AMBIGUOUS. Program's permanent value: USL prediction, CTP formalism for EIT, forced form-class, experimental protocol, and methodology. Gates: 5/5 pass.*
