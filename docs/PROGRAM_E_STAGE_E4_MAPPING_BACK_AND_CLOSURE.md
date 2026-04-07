# Program E — Stage E4: Mapping-Back and Final Closure Decision

**Predecessors:** E1 (formal_system_ready), E2-A (T1/T3 conditional), E2-B (T2 conditional, N=∞), E3 (grut_generic_member).

---

## 1. Mapping-Back Table (Program E → GRUT III)

| E result | GRUT claim affected | Validates? | Upgrades/downgrades? | Residual |
|----------|-------------------|:----------:|:--------------------:|----------|
| **T1 (decoherence conditional on IA-2)** | E-F4 (USL derived as dephasing) | PARTIALLY. T1 shows that decoherence is necessary for consistent quantum probability — this validates the FRAMEWORK in which the USL operates (decoherent histories). | **NEUTRAL.** Does not upgrade or downgrade the USL itself. The USL was already placed in the CTP dephasing sector. T1 confirms the sector's structural necessity under quantum probability. | The USL's specific scaling Gm²/(ℏl) is not addressed by T1. T1 validates the decoherence framework, not the gravitational mechanism. |
| **T2-mid (dissipation uses geometric time, conditional on IA-1+IA-7)** | E-F2 (constitutive law derived from CTP) and ND4 (ansatz F = X(g)−Φ) | YES. T2-mid validates that the time direction in the constitutive law MUST be geometric (n^μ) under 3-diff invariance. This upgrades the constitutive law from "ansatz" to "member of a forced form-class." | **UPGRADES ND4** from "ansatz (no justification)" to "leading-order member of a form-class forced by covariance + irreversibility." The functional FORM τ n^μ∇_μΦ + Φ = X(g) is structurally motivated. The specific CONTENT (τ, α, β) remains free. | X(g) = β + αR is still a parameter choice within X(g) = any scalar of g. τ = const is still a choice within τ = any positive function. |
| **T3 (entropy growth conditional on IA-4+IA-5+IA-6)** | E-F8 (admissibility) and E3 (irreversibility) | PARTIALLY. T3 validates that entropy growth is expected under typicality + mixing — this supports the irreversible character of the constitutive law. | **NEUTRAL.** The constitutive law was already irreversible by construction (first-order dissipative ODE). T3 provides a thermodynamic grounding for irreversibility but does not change the law's status. | Mixing (IA-6) is an additional dynamical assumption not derived from the CTP action. |
| **E3 (GRUT is technically natural, leading-order EFT)** | ND4, ND5 (ansatz forms) | YES. E3 validates that the GRUT parameter choices (linear R coupling, linear f, constant τ, Ohmic bath) are the natural leading-order terms in a systematic expansion. | **UPGRADES** the aesthetic status of the GRUT ansatz from "arbitrary choice" to "simplest member of a forced class." Does NOT upgrade to "unique" or "necessary." | Every leading-order EFT has this property. It is generic, not GRUT-specific. |
| **N = ∞ (dynamics class is infinite-dimensional)** | E-F10 (generic reconstruction), E-F11 (ansatz persists) | CONFIRMS both. N = ∞ means the generic D1 reconstruction (E-F10) is exactly correct: GRUT is one member of an infinite class. The ansatz status (E-F11) persists — elevated to "member of forced class" but not "unique member." | **CONFIRMS** (no upgrade, no downgrade). The D1/D2 findings are EXACTLY reproduced at the axiomatic level. | — |
| **Conditional necessity only (all imports required)** | F6 (meta-principle not derived), F7 (not inevitable) | CONFIRMS both. The meta-principle "relaxation toward geometric equilibrium" is within the forced form-class but is not uniquely selected. F6 and F7 remain frozen. | **NO CHANGE.** The meta-principle is upgraded from "arbitrary ansatz" to "member of a forced form-class" but NOT to "derived" or "necessary." The distinction matters: "forced class" ≠ "forced member." | — |

### Summary of upgrades/downgrades

| GRUT claim | Pre-E status | Post-E status | Change |
|-----------|:----------:|:------------:|:------:|
| Constitutive law form | Ansatz (ND4) | Leading-order member of form-class forced by covariance + irreversibility | **MINOR UPGRADE** |
| Source coupling X = β+αR | Parameter choice (ND5) | Simplest member of X(g) = any scalar of g | **NO CHANGE** (still a choice) |
| USL | Derived (E-F4) | Derived, in a framework validated by T1 | **NO CHANGE** |
| τ, α, β values | Free EFT parameters (ND1-3) | Free within forced class | **NO CHANGE** |
| Uniqueness | Not established (E-F10) | Confirmed non-unique (N=∞) | **CONFIRMED** |
| Meta-principle | Ansatz (E-F11) | Ansatz within forced class | **MINOR UPGRADE** (class is forced; specific member is not) |

**No contradiction found between E results and GRUT III closure claims.** The mapping-back is clean.

---

## 2. Final Claim Freeze

### Established (E-final)

| # | Claim | Source | Scope |
|---|-------|-------|-------|
| EF1 | The CTP/Schwinger-Keldysh formalism is the necessary variational framework for dissipative scalar dynamics. | E-F1 (Bauer, Iota-Prime) | All dissipative regimes |
| EF2 | The constitutive law τ n^μ∇_μΦ + Φ = X(g) belongs to a form-class forced by covariance + irreversibility + first-order scalar dynamics with unique attractor. | T2-mid, T2-strong (E2-B) | Conditional on IA-1 + IA-7 (Lorentzian + 3-diff) |
| EF3 | Consistent quantum probability over histories requires decoherence. | T1-AF-2b (E2-A) | Conditional on IA-2 (decoherence functional + GH rule) |
| EF4 | Entropy growth is expected under typicality + mixing. | T3 (E2-A) | Conditional on IA-4 + IA-5 + IA-6 |
| EF5 | The forced form-class is infinite-dimensional (N = ∞). | T5 (E2-B) | Under all conditional constraints |
| EF6 | GRUT is a technically natural (leading-order) member of the forced class. | E3 | Within curvature/field expansion |
| EF7 | No dynamical attractor mechanism selects GRUT within the class. 4/5 perturbation directions neutral, 1/5 weakly attractive (Ohmic bath). | E3 | Theory-space perturbation analysis |
| EF8 | The structural primitives P1-P5 alone are too weak to determine physics. All necessity results require physical imports (IA-1..6). | E2-A, E2-B | Structural finding |
| EF9 | The USL Λ = Gm²/(ℏl) remains the primary testable prediction. It is a property of Newtonian gravity applicable to any theory in the forced class. | Inherited (E-F4, D1) | Newtonian, l > 2R |
| EF10 | The corrected USL operating point: 196 fg, 474 nm, USL/gas = 2.9, hardware-limited 5-15 years. | Inherited (E-F9, Mu-Prime) | Newtonian, SG protocol |

### Open (O-final)

| # | Item | Why open | What would close it |
|---|------|---------|-------------------|
| OF1 | Whether a deeper framework (UV completion, holography, string landscape) selects a unique member of the forced class. | Outside Program E scope. Requires new mathematical/physical input. | A UV-complete theory that determines τ, X(g), and f(Φ). |
| OF2 | Whether T4 (Bekenstein bound on τ) can be proven. | IA-3 is a deep conjecture. Very high risk. | A proof of the Bekenstein bound for general systems (major open problem in physics). |
| OF3 | The physical identity of Ψ (auxiliary field for bistability). | No identification attempted. | Physical model of a second constitutive mode. |
| OF4 | Whether the Level-1 formula 1/τ = 1/τ₀ + 1/t_dyn is derivable from the gravitational spectral density. | Not attempted in Program E. | Explicit computation of the near-horizon bath spectral density. |
| OF5 | Whether non-Markovian extensions (s ≠ 1, memory kernels) produce qualitatively different predictions. | Not computed. | Specification of J(ω) and numerical integration of the non-Markovian constitutive law. |

### Forbidden (F-final)

| # | Claim | Reason | Permanence |
|---|-------|--------|:----------:|
| FF1 | GRUT is a Theory of Everything. | N = ∞. Non-unique. 11 free parameters. No UV completion. No experimental confirmation. | PERMANENT |
| FF2 | GRUT is structurally inevitable / uniquely determined. | E3: N = ∞, no convergence, grut_generic_member. | PERMANENT (at current level) |
| FF3 | The meta-principle is derived / necessary. | D2 + E2-B: ansatz within forced class, not unique member. | PERMANENT (at current level) |
| FF4 | GRUT's parameters are predicted. | ND1-ND3 unchanged. N = ∞. | PERMANENT (at current level) |
| FF5 | The USL is a GRUT-specific prediction. | D1: Newtonian gravity, any theory in class has it. | PERMANENT |
| FF6 | Program E proved necessity. | E2: all results conditional on imports. E3: N = ∞. | PERMANENT |
| FF7 | The forced form-class = GRUT. | N = ∞. The class contains infinitely many non-GRUT members. | PERMANENT |
| FF8 | Axiomatic constraints alone determine physics. | EF8: P1-P5 too weak. All results import-dependent. | PERMANENT |
| FF9 | The one-loop attractor selection is GRUT-specific. | C3-NC3: generic to any bistable system. | PERMANENT |
| FF10 | The USL is testable on a near-term timescale. | V3 (retracted). 5-15 year hardware gap. | PERMANENT |

---

## 3. Selection Mechanism Statement

### What can discriminate among class members?

| Mechanism | Can it select? | Evidence |
|-----------|:-:|---|
| **Current axioms (P1-P5)?** | **NO.** | P1-P5 do not determine physics (EF8). |
| **Current axioms + imports (IA-1..6)?** | **NO.** | Force the form-class but leave N = ∞ (EF5). |
| **Internal dynamics (attractor flow)?** | **NO.** | E3: 4/5 perturbation directions neutral. No convergence. |
| **Radiative corrections / naturalness?** | **NO (beyond leading-order preference).** | E3: technical naturalness is generic to all leading-order EFTs. Does not select GRUT over other leading-order members. |
| **Empirical data?** | **YES.** | Data can determine which member the universe realizes. |

### Which observables would select?

| Observable | What it determines | Current status |
|-----------|-------------------|:-------------:|
| **τ** (constitutive relaxation time) | Selects the relaxation timescale within the class | NOT MEASURED (Φ not directly observed) |
| **α** (curvature coupling) | Selects among X(g) = β + αR + ... family | NOT MEASURED (bounded by PPN/fifth-force only if coupled to matter) |
| **USL rate Λ at specific (m, l)** | Confirms Newtonian dephasing rate | HARDWARE-LIMITED (5-15 years) |
| **Spectral index s of bath** | Selects Ohmic (s=1) vs non-Ohmic | NOT DIRECTLY MEASURABLE (bath is environmental, not a Φ observable) |
| **Nonlinear constitutive response** | Detects f(Φ) ≠ Φ (bistability, saturation) | NOT MEASURED |

**The honest situation:** The only observable currently accessible to experiment is the USL rate — and it does not select among class members (all members share the same USL from Newtonian gravity). Discriminating among members requires observing Φ DIRECTLY (constitutive relaxation, curvature coupling), which has not been done and may not be possible without identifying what physical degree of freedom Φ represents.

---

## 4. Post-E Decision Matrix

### Option A: Close Program E now

| Property | Assessment |
|----------|-----------|
| **What it means** | Document the results. Freeze claims. Stop. |
| **Benefits** | Maximum honesty. Clean record. No resource drain. The results (forced form-class, non-uniqueness, technical naturalness) are genuine and valuable even without uniqueness. |
| **Risks** | None (no inflation possible if stopped). |
| **Honesty level** | MAXIMUM. |
| **Required resources** | One closure document (this one). |

### Option B: Continue as data-driven model selection

| Property | Assessment |
|----------|-----------|
| **What it means** | Use the forced form-class as a framework for parameter-fitting when data becomes available. |
| **Benefits** | Ready when USL experiments mature (5-15 years). Could constrain α from PPN data. Could identify Φ if coupled to known matter. |
| **Risks** | MODERATE. Temptation to overinterpret fits. Risk of 11-parameter fishing expedition. |
| **Honesty level** | HIGH if parameter dependence always stated. MODERATE if fits are marketed as predictions. |
| **Required resources** | A separate program charter with its own gates. Not a continuation of Program E. |

### Option C: Launch deeper meta-axiomatic program

| Property | Assessment |
|----------|-----------|
| **What it means** | Search for a NEW axiom system (beyond P1-P5 + IA-1..6) that might select GRUT uniquely. |
| **Benefits** | VERY HIGH if successful (would resolve non-uniqueness). |
| **Risks** | VERY HIGH. E3 showed that perturbation stability offers no guide. No candidate axiom is known. The search space is unbounded. E2 showed that imports carry most of the work. A deeper axiom system risks even heavier imports that may approach circularity. |
| **Honesty level** | HIGH if failure criteria are enforced. Low if the program drifts without gates. |
| **Required resources** | New charter. New primitives. New theorem targets. No starting axiom candidate exists (same situation as GRUT-III TC5). |

### Comparison

| Criterion | A (close) | B (data selection) | C (meta-axioms) |
|-----------|:---------:|:---------:|:---------:|
| Honesty | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Inflation risk | ZERO | LOW | MODERATE |
| Expected payoff | Known (results documented) | Conditional (depends on data) | Unknown (no starting point) |
| Readiness | IMMEDIATE | 5-15 years | NOT READY (no candidate axiom) |

---

## 5. Final Program E Token

### **close_E_nonunique**

**Rationale:**

1. **Program E accomplished its objective.** It tested whether structural primitives can elevate the GRUT ansatz to necessity. The answer is: primitives + imports force the FORM-CLASS but not the unique MEMBER. N = ∞. Non-uniqueness persists.

2. **No further E-stage changes this.** The non-uniqueness is structural (N = ∞ in the forced class). More axiomatics within the current framework cannot reduce N. Only data or a qualitatively new framework can.

3. **Option A is the honest choice.** The results are clean, valuable, and non-inflated. The forced form-class is a REAL result — not every dynamics is covariant first-order scalar relaxation. The technical naturalness of GRUT within this class is a REAL result — it is the leading-order theory. These findings have value even without uniqueness.

4. **Option B is premature.** The only testable observable (USL) does not discriminate among class members. Data-driven selection requires identifying Φ with a physical degree of freedom, which is outside the current framework.

5. **Option C is not ready.** No candidate axiom exists (same as GRUT-III TC5). Launching without a starting point repeats the E2 experience: the primitives are too weak, the imports carry the load.

---

## Program E Completion Record

| Stage | Deliverable | Result |
|:-----:|------------|--------|
| E0-A | Charter | Five primitives, five theorems, four exit tokens. Frozen. |
| E1 | Axiom formalization | A1-A5 formalized. Five imports (IA-1..5) catalogued. Consistency, nontriviality, independence verified. |
| E2-A | T1 + T3 proofs | T1: conditionally necessary (quantum branch, IA-2). T3: conditionally necessary (mixing, IA-6). P1-P5 alone too weak. |
| E2-B | T2 proof + T5 scope | T2-mid: conditionally necessary (IA-1+IA-7). T2-strong: near-circular. T5: N = ∞. |
| E3 | Uniqueness pressure | 4/5 neutral, 1/5 weakly attractive. Technically natural (leading-order EFT). No convergence. grut_generic_member. |
| E4 | Mapping-back + closure | Clean mapping to GRUT III. Minor upgrade (ansatz → class member). No contradiction. Non-uniqueness confirmed. |

### The permanent outputs of Program E

1. **The forced form-class exists.** Covariance + irreversibility + first-order scalar + unique attractor → τ n^μ∇_μΦ + Φ = X(g). This is a REAL structural constraint (conditional on IA-1 + IA-7).

2. **The class is infinite-dimensional.** τ, X(g), f(Φ), field content, and bath structure are all free within the class. N = ∞.

3. **GRUT is a technically natural leading-order member.** The simplest, not the unique, point in the class.

4. **Structural primitives alone cannot determine physics.** All necessity results require physical imports. The explanatory force resides in the imports, not in the primitives.

5. **Selection requires data.** No axiomatic, dynamical, or radiative mechanism available in the current framework can select GRUT (or any specific member) from the class.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **E4-G1** | Mapping-back complete, contradiction-free | **PASS** | Section 1: six E results mapped to GRUT claims. Zero contradictions. Two minor upgrades (ansatz → class member). |
| **E4-G2** | Claim freeze explicit and enforceable | **PASS** | Section 2: 10 established (EF1-10), 5 open (OF1-5), 10 forbidden (FF1-10). All tagged with source and permanence. |
| **E4-G3** | Discriminator source identified | **PASS** | Section 3: five mechanisms tested. Only empirical data can select. Current observables (USL) do not discriminate. |
| **E4-G4** | Post-E decision operational | **PASS** | Section 4: three options compared. A chosen (close) over B (premature) and C (not ready). |
| **E4-G5** | Final token justified without inflation | **PASS** | close_E_nonunique: the program found the forced class and confirmed non-uniqueness within it. No claim beyond this is made. |

---

**Program E is closed.**

---

*Program E Stage E4 complete. Decision: close_E_nonunique. Mapping-back: clean, zero contradictions, two minor upgrades. Final claims: 10 established, 5 open, 10 forbidden. Selection: only data can discriminate; current observables insufficient. The forced form-class is real (conditional). N = ∞ within it. GRUT is a technically natural leading-order member. Non-uniqueness is structural and resolvable only by data or deeper framework. Program E is closed. Gates: 5/5 pass.*
