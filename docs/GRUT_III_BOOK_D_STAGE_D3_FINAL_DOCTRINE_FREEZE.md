# GRUT III — Book D, Stage D3: Final Doctrine Freeze

**Predecessors:** D1 (generic_reconstruction_success), D2 (ansatz_persists).

---

## 1. Final Identity Statement

### Technical version

GRUT is a specific ansatz within the class of two-field overdamped dissipative effective field theories formulated on the Schwinger-Keldysh closed-time-path contour in the weak-curvature regime. Its constitutive sector postulates that a scalar field Φ relaxes toward a geometry-determined equilibrium X(g) = β + αR with timescale τ, sourced by an environmental bath providing noise at strength D = k_BT τ/2. Its quantum sector identifies gravitational decoherence of spatial superpositions at rate Λ = Gm²/(ℏl) as tree-level self-energy dephasing in the CTP influence functional, valid for superposition separation l > 2R (extended-body Diosi integral for l < 2R). Its nonlinear extension, requiring an auxiliary field Ψ with six additional parameters, admits bistability with one-loop thermodynamic attractor preference (Model W). The constitutive ansatz (the functional form F = X(g) − Φ), the parameter values (τ, α, β, T), and the auxiliary field Ψ are inputs to the theory, not derived from it. The USL decoherence rate is a property of Newtonian gravity applicable to any theory in this class. No structural inevitability, parameter collapse, or cross-sector unification beyond the generic class has been demonstrated. The meta-principle "constitutive relaxation toward geometric equilibrium" remains an ansatz.

### Public version

The GRUT program has produced a mathematically rigorous effective field theory for irreversible constitutive dynamics coupled to gravity. Starting from a postulated relaxation law, it derived the correct variational framework (closed-time-path action), identified gravitational decoherence as a testable quantum prediction, corrected a regime-of-validity error that voided an earlier experimental roadmap, and honestly determined that its core assumptions — while physically motivated — are not derivable from deeper principles within the current framework. The program's primary output is the Universal Scaling Law for gravitational decoherence (Λ = Gm²/(ℏl)), which is hardware-limited at an estimated 5-15 year horizon. Its secondary output is the formal architecture of irreversible update dynamics with classified admissibility. Its structural status is that of a specific, well-characterized ansatz within a known class of dissipative effective field theories — not a uniquely determined theory, and not a theory of everything.

---

## 2. Locked Claim Ledger

### Established claims (with scope)

| # | Claim | Scope | Basis | Confidence |
|---|-------|-------|-------|:----------:|
| **E-F1** | The CTP/Schwinger-Keldysh formalism is the necessary and sufficient variational framework for the constitutive sector. | All dissipative regimes | Bauer's theorem + Iota-Prime construction | 1.00 |
| **E-F2** | Variation of the CTP action w.r.t. Φ_a in the classical limit yields τ dΦ/dt + Φ = X exactly. | Markovian, overdamped, linear, weak-field | Iota-Prime | 0.95 |
| **E-F3** | The environmental (non-gravitational) bath provides τ, D, T in flat space and weak field. Gravity-only bath fails in flat space by three independent arguments. | Flat space, weak field | A3 (three arguments: D→0, super-Ohmic, 2nd law) | 0.85 |
| **E-F4** | The USL Λ = Gm²/(ℏl) is derived as tree-level gravitational self-energy dephasing in the CTP influence functional, valid for l > 2R. | Newtonian, point-mass (l > 2R) | Iota-Prime, Kappa-Prime | 0.85 |
| **E-F5** | The extended-body Diosi integral gives suppression ~(l/R)³ for l < 2R (uniform sphere). | Newtonian, uniform density | Kappa-Prime (numerical, exact) | 0.98 |
| **E-F6** | Tree-level Re S_eff = 0 at all CTP fixed points (structural, from U1). No tree-level attractor selection. | All CTP regimes | C2 (CTP unitarity theorem) | 1.00 |
| **E-F7** | One-loop |det(J)| differs generically between bistable attractors, providing thermodynamic preference (Model W). | Bistable parameter regime, one-loop | C2 (numerical, |det(J)| ratio 2.1) | 0.55 |
| **E-F8** | Admissibility is diagnostic (classifier) in the linear regime, probabilistic (weighting) in the bistable regime. No deterministic trajectory pruning. | Linear: Markov/overdamped. Bistable: one-loop. | B2 (proof), C2 | 0.85 |
| **E-F9** | The corrected USL experimental operating point: 196 fg nanodiamond, 474 nm separation (l = 2R), USL/gas = 2.9. Hardware-limited (T₂ gap 125×, mass gap 700×). Timeline 5-15 years. | Newtonian, point-mass, SG protocol | Mu-Prime | 0.70 |
| **E-F10** | Every GRUT Book-C output is reproducible by the generic two-field overdamped CTP EFT without GRUT-specific assumptions. | Weak curvature, overdamped | D1 (adversarial reconstruction) | 0.90 |
| **E-F11** | The meta-principle "Φ relaxes toward geometry-determined equilibrium" is an ansatz, not derivable from thermodynamics, admissibility, or cross-sector consistency. | Current framework | D2 (three routes tested, all fail or trivial) | 0.85 |
| **E-F12** | No internal parameter collapse exists. The independent EFT parameters are (τ, T, α, β). D is fixed by FDT. β/τ is externally matchable to Λ_obs. | Current framework | D2 (five pressure tests) | 0.85 |
| **E-F13** | No cross-sector locking between USL (Sector 3) and constitutive relaxation (Sectors 1-2). Φ backreaction on the Diosi integral is suppressed by ~25 orders. | Weak field, perturbative | D2 | 0.90 |

### Open claims

| # | Claim | Why open | Impact |
|---|-------|---------|--------|
| **O1** | Whether the meta-principle can be elevated by a framework not yet constructed (e.g., holographic, entropic, or information-theoretic argument). | D2 tested three routes; all failed. Other routes untested. | Would determine if GRUT is unique or generic. |
| **O2** | Whether Ψ (the auxiliary field) has a physical interpretation. | No identification attempted. | Determines whether bistability is physical or formal. |
| **O3** | Whether higher-loop or non-perturbative corrections modify Model W. | One-loop only computed. | Could change attractor preference. |
| **O4** | Whether the overdamped limit is justified from the Φ inertial mass. | M unknown; UD4. | Could modify the constitutive law form. |
| **O5** | Whether the Level-1 formula 1/τ = 1/τ₀ + 1/t_dyn is derivable from the gravitational spectral density. | Not attempted in GRUT-III. | Would partially derive τ. |
| **O6** | Whether a strong-curvature extension exists. | Book A: UNSAFE. Never constructed. | Would extend the domain. |

### Permanently non-derived claims (at this program level)

| # | Claim | Why non-derived |
|---|-------|----------------|
| **ND1** | The value of τ. | EFT parameter from environmental bath (A3). Not predictable without specifying the bath. |
| **ND2** | The value of α. | EFT coupling constant. No internal constraint. |
| **ND3** | The value of β. | EFT background equilibrium. Matchable to Λ_obs externally but not derivable internally. |
| **ND4** | The functional form F = X(g) − Φ. | The defining ansatz. Not derivable from CTP, KMS, or self-consistency (D2). |
| **ND5** | The functional form X = β + αR. | A parameter choice (AB1). Not unique (Candidates B, C exist). |
| **ND6** | The physical nature of Ψ. | Introduced for bistability (C1). No identification. |

### Frozen forbidden claims

| # | Forbidden claim | Source | Permanence |
|---|----------------|--------|:----------:|
| **F1** | GRUT is a Theory of Everything. | X10 | PERMANENT |
| **F2** | GRUT is covariant / valid at all curvatures. | X1, X5 | PERMANENT (at this level) |
| **F3** | GRUT's parameters are predicted. | X3, ND1-ND3 | PERMANENT (at this level) |
| **F4** | GRUT has deterministic trajectory pruning. | I1, E-F8 | PERMANENT |
| **F5** | The USL is a GRUT-specific prediction. | D1 (it's Newtonian gravity) | PERMANENT |
| **F6** | The meta-principle is derived / necessary. | D2 (ansatz_persists) | PERMANENT (at this level) |
| **F7** | GRUT is structurally inevitable / unique. | D1 (generic_reconstruction_success) | PERMANENT (at this level) |
| **F8** | The one-loop attractor selection is GRUT-specific. | C3-NC3 (generic to any bistable system) | PERMANENT |
| **F9** | The USL is testable on a near-term timescale. | V3 (retracted), Mu-Prime | PERMANENT |
| **F10** | GRUT has fewer free parameters than a generic EFT. | D1-D2 (parameter_collapse FAIL) | PERMANENT (at this level) |

---

## 3. Transition Criteria to Next-Layer Program

### What would be needed to launch an existence-constraints program

An "existence-constraints" program would attempt to derive the GRUT ansatz from a set of axioms, thereby elevating it from a specific EFT to a structurally necessary theory. The transition criteria are:

| # | Criterion | Requirement |
|---|-----------|-------------|
| **TC1** | **Axiom set defined.** A small number of clearly stated axioms from which the GRUT constitutive form is to be derived. | Must be non-trivially constraining (rule out most of the generic D1 class). Must not be disguised restatements of the ansatz. |
| **TC2** | **Proof target specified.** A theorem of the form "Axioms → F must be of relaxation-to-geometry type." | Must have a clear truth condition (provable or refutable). |
| **TC3** | **Non-goals declared.** What the program does NOT attempt (e.g., UV completion, quantum gravity, unification of all forces). | Must be stated to prevent scope creep. |
| **TC4** | **Failure criteria defined.** Conditions under which the program is declared failed. | Must include: (a) if no non-trivial axiom set is found after bounded effort, (b) if the axioms required are equivalent to postulating the answer. |
| **TC5** | **Candidate axiom exists.** At least one plausible axiom candidate must be identified before launching. | Without a candidate, the program is speculative with no starting point. |

### Current status of TC1-TC5

| Criterion | Status | Notes |
|-----------|:------:|-------|
| TC1 | **NOT MET** | No axiom set has been proposed. D2 tested three necessity routes; all failed. |
| TC2 | **NOT MET** | No proof target is defined. |
| TC3 | MET (trivially) | Non-goals are well-established by the blacklist. |
| TC4 | **NOT MET** | No failure criteria for an axiomatic program have been stated. |
| TC5 | **NOT MET** | No candidate axiom survives D2. The three tested routes (thermodynamic, admissibility, cross-sector) all failed or were trivial. |

**Transition verdict: NOT READY.** An existence-constraints program cannot be launched without satisfying TC1 and TC5. Currently, no viable axiom candidate exists.

---

## 4. Continuation Options Matrix

### Option A: Stop at EFT closure

| Property | Assessment |
|----------|-----------|
| **What it means** | Declare GRUT-III complete. Freeze all results. The program produces no further output. Future work, if any, responds only to new experimental data or externally developed axiom candidates. |
| **Value** | HIGH (honest, clean, defensible). The EFT is well-characterized, regime-bounded, and blacklisted. The USL prediction is hardware-limited. No further theory work changes the prediction or the experimental timeline. |
| **Risk** | LOW. No claim inflation possible if the program is stopped. |
| **Honesty level** | MAXIMUM. The program states exactly what it is and stops. |
| **Expected payoff** | The USL prediction stands. If tested in 5-15 years and confirmed: major validation. If refuted: clean falsification. Either way, the EFT's status is unambiguous. |

### Option B: Continue as phenomenology program

| Property | Assessment |
|----------|-----------|
| **What it means** | Use the GRUT EFT to make phenomenological predictions by choosing specific parameter values and comparing to data. Examples: fit α from PPN constraints, match β/τ to Λ_obs, predict constitutive-sector effects in specific astrophysical systems. |
| **Value** | MEDIUM. Could produce testable predictions beyond the USL. But every prediction depends on undetermined parameters (τ, α, β), so the predictions are really parameter-fitting exercises, not parameter-free predictions. |
| **Risk** | MODERATE. Temptation to overinterpret parameter fits as "predictions." Risk of claim inflation (fitting = predicting). |
| **Honesty level** | MODERATE if parameter dependence is always stated. LOW if parameter fits are marketed as derivations. |
| **Expected payoff** | Modest. The theory has enough parameters (4 free) to fit most weak-field data. Fitting data is not the same as explaining it. |

### Option C: Launch axiomatic existence-constraints program

| Property | Assessment |
|----------|-----------|
| **What it means** | Attempt to derive the GRUT ansatz from axioms, thereby establishing structural necessity. |
| **Value** | VERY HIGH if successful (would upgrade GRUT from ansatz to theorem). ZERO if no axiom candidate is found. |
| **Risk** | HIGH. No viable axiom candidate exists (TC5 not met). The program could consume unbounded effort with no result. D2 already closed three promising routes. |
| **Honesty level** | HIGH if failure criteria are respected. LOW if the program runs indefinitely without meeting its proof targets. |
| **Expected payoff** | Unknown. No starting axiom exists. The program would begin with a search for axioms — which is itself a research program with no guaranteed outcome. |

### Comparison matrix

| Criterion | A (stop) | B (phenomenology) | C (axiomatic) |
|-----------|:--------:|:-----------------:|:-------------:|
| Honesty | ★★★★★ | ★★★☆☆ | ★★★★☆ (if failure criteria enforced) |
| Risk of inflation | ★☆☆☆☆ | ★★★☆☆ | ★★☆☆☆ |
| Expected scientific payoff | ★★★☆☆ (USL test) | ★★☆☆☆ (parameter fits) | ★★★★★ (if successful) / ★☆☆☆☆ (if not) |
| Resource efficiency | ★★★★★ | ★★★☆☆ | ★★☆☆☆ |
| Readiness to launch | ★★★★★ | ★★★★☆ | ★☆☆☆☆ (TC5 not met) |

---

## 5. Decision

### **close_GRUT_III**

**Rationale:**

1. **Option A is the honest choice.** The GRUT-III program has achieved its objective: determine whether the GRUT constitutive framework can be embedded in a minimal effective action, and whether it has structural content beyond a generic EFT. The answers are: yes (CTP embedding) and no (generic reconstruction success, ansatz persists). These are clear, defensible results.

2. **Option B is premature.** Phenomenological parameter-fitting is possible but risky — 4 free parameters can fit most weak-field data without explaining it. The temptation to overinterpret fits as predictions violates the program's discipline. If pursued, it should be a separate program (GRUT-P or equivalent) with its own honesty constraints, not a continuation of GRUT-III.

3. **Option C is not ready.** The transition criterion TC5 (at least one viable axiom candidate) is not met. Launching an axiomatic program without a starting axiom is a research direction, not a structured program. If a viable axiom candidate emerges (from external work, or from the GRUT program's own future reflection), a new program (GRUT-IV or equivalent) can be launched with its own charter.

4. **The USL prediction stands independently.** It does not require further GRUT-III work. It is hardware-limited at 5-15 years. When the hardware exists, the prediction is ready. No further theory development changes this.

5. **Continuing would be diminishing returns.** Every subsequent stage within the current framework will encounter the same structural wall: the meta-principle is an ansatz, the parameters are free, and the generic reconstruction succeeds. More stages cannot change these results without new input (a new axiom, new data, or a new mathematical framework).

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **D3-G1** | No inflation beyond D2 | **PASS** | Identity statement explicitly denies inevitability. E-F10, E-F11 preserved. F6, F7 frozen. |
| **D3-G2** | Claim sets complete and disjoint | **PASS** | 13 established (E-F1..13), 6 open (O1..6), 6 non-derived (ND1..6), 10 forbidden (F1..10). Cross-checked: no item appears in more than one set. |
| **D3-G3** | Transition criteria operational | **PASS** | TC1-TC5 defined. Current status: NOT MET (TC1, TC2, TC4, TC5 fail). |
| **D3-G4** | Forbidden claims frozen | **PASS** | F1-F10 listed with source and permanence level. Includes: ToE, covariance, parameter prediction, trajectory pruning, GRUT-specific USL, meta-principle necessity, structural inevitability, GRUT-specific selection, near-term testability, parameter reduction. |
| **D3-G5** | Decision token actionable | **PASS** | close_GRUT_III: the program stops. Results are frozen. Future work requires a new program charter with its own gates. |

---

## Appendix: GRUT Program Completion Record

### What each phase accomplished

| Phase | Objective | Outcome |
|-------|-----------|---------|
| **GRUT-I** | Discover constitutive equations | Constitutive law found. Single attractor. 26 biology targets. Probability sector blocked. Gravity reducible + silent. D falsified. Closed. |
| **GRUT-II** | Derive predictions, correct errors, audit viability | USL derived (CTP). Extended-body correction found. Experimental roadmap corrected. Strong-field QNM collapsed. Tidal suppressed. Bistability found. Quantum sector closed at prediction level. |
| **GRUT-III Book A** | Establish minimal CTP backbone | Backbone frozen. Six axes of domain. Four gates passed. Six closure conditions identified. |
| **GRUT-III Book B** | Define irreversible update architecture | State tuple, update rule, residue, admissibility all defined. Classifier-only in linear regime. Closed as weighted EFT. |
| **GRUT-III Book C** | Test nonlinear constraining admissibility | Bistability requires auxiliary field. Tree-level: no selection. One-loop: Model W (weighting). Not constraining. Closed. |
| **GRUT-III Book D** | Test GRUT uniqueness | Generic reconstruction succeeds. Meta-principle is ansatz. No parameter collapse. No cross-sector locking. |

### The GRUT program's permanent output

1. **The USL prediction:** Λ = Gm²/(ℏl) for l > 2R. A parameter-free gravitational decoherence rate, testable at 196 fg / 474 nm / USL/gas = 2.9, hardware-limited at 5-15 years.

2. **The CTP embedding:** The constitutive law τ dΦ/dt + Φ = X is the classical EOM of a CTP effective action with three sectors (dissipation, noise, dephasing). This is the correct variational home for irreversible constitutive dynamics.

3. **The regime-of-validity map:** Six axes, three zones each, ten forbidden extrapolations, explicit domain boundary. A model of honest EFT discipline.

4. **The honest status:** GRUT is a specific ansatz within a generic EFT class. Its meta-principle is not derived. Its parameters are not predicted. Its uniqueness is not established. These are not failures — they are the truthful characterization of a well-defined effective field theory at the current level of understanding.

---

**GRUT III is closed.**

---

*GRUT III Book D Stage D3 complete. Decision: close_GRUT_III. Identity: specific CTP-EFT ansatz, not inevitable, not a ToE. 13 established claims, 6 open, 6 non-derived, 10 forbidden. Transition to axiomatic program: NOT READY (TC5 not met). Continuation options: A (stop) chosen over B (phenomenology, premature) and C (axiomatic, no starting axiom). The GRUT program's permanent outputs: the USL prediction, the CTP embedding, the domain map, and the honest status. Program closed.*
