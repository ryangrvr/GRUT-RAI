# APPENDIX Q-D — DECOHERENCE AND MEASUREMENT BRIDGE AUDIT

**GRUT Quantum Program | Phase Q-D**
**Status:** Audit Complete
**Appendix P Classification:** `motivated_but_unbuilt` (all Q-D results)
**Authorization Inherited:** `authorized_to_proceed_to_QD` from Q-C.5
**Authorization Granted:** `authorized_to_proceed_to_QE`

---

## Framing Statement

The correct reading of Q-D is as follows: GRUT's preferred open-system extension demonstrates effective-regime decoherence and a pointer-basis class, while leaving outcome selection and Born-rule weighting unresolved. The decoherence verdict must not be read as measurement-bridge solved. Every section of this appendix enforces this boundary.

---

## Hard-Gated Verdict Table

The following five verdicts are fixed by the Q-D audit. They cannot be modified by downstream appendices without re-opening Q-D.

| Verdict Key | Value |
|---|---|
| `decoherence_verdict` | `effective_regime_decoherence_demonstrated` |
| `pointer_verdict` | `pointer_basis_class_selected` |
| `measurement_scope_verdict` | `decoherence_plus_pointer_structure` |
| `outcome_selection_verdict` | `born_rule_or_outcome_selection_not_natively_derived` |
| `authorization_verdict` | `authorized_to_proceed_to_QE` |

**Overall Appendix P:** `motivated_but_unbuilt`

---

## Section 1 — Exact Question Being Audited

**Audit question:** Given the preferred Lindbladian-like open-system microdynamics from Q-C and the effective-regime constitutive recovery from Q-C.5, does the GRUT quantum extension natively derive decoherence and pointer-structure selection, and what exactly remains unresolved about measurement and outcome selection?

This question has two halves that must not be collapsed into one another:

- **Half A (derivation):** Does the GRUT open-system structure produce decoherence in a definite basis? Does it dynamically select a pointer-basis class?
- **Half B (gap):** After establishing what is derived, what precisely remains absent? Specifically: is outcome selection present? Is Born-rule weighting derivable from the audited structure?

Half A receives a positive verdict. Half B receives a negative verdict. The two verdicts are logically independent and must both be stated. Conflating them — reading a positive verdict on Half A as closing Half B — is the primary doctrinal error this appendix is constructed to prevent.

### Inherited Authorizations and Structures

**Authorization chain:**
- Q-A charter: granted `authorized_to_proceed_to_QB`
- Q-B: granted `authorized_to_proceed_to_QB5`
- Q-B.5: granted `authorized_to_proceed_to_QC0`
- Q-C0: granted `authorized_to_proceed_to_QC`
- Q-C: granted `authorized_to_proceed_to_QC5`
- Q-C.5: granted `authorized_to_proceed_to_QD`
- **Q-D (this appendix):** grants `authorized_to_proceed_to_QE`

**Inherited law class:** `lindbladian_like_law_preferred` with jump operator L = (1/√τ)·Φ̂, dissipation rate γ = 1/τ.

**Inherited recovery:** `effective_regime_constitutive_recovery_demonstrated` — in the effective regime, the expectation-value evolution satisfies τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩.

**Inherited regime conditions:** Markovian approximation (bath memory time ≪ τ); Born-Markov approximation valid; weak-coupling regime. These are genuine constraints on the domain of all Q-D results — they are not packaging language.

---

## Section 2 — Inherited Lindbladian-like and Q-C.5 Recovery Structure

Q-D inherits the following verdicts from prior quantum program appendices. Each is stated precisely because Q-D results depend on them structurally and any change upstream would propagate downward.

### Inherited Verdicts

**From Q-C:**
- `lindbladian_like_law_preferred` — the Lindbladian-like master equation is the preferred open-system generator, preferred over non-Lindblad alternatives on grounds of complete positivity and trace preservation.
- `minimal_extension_burden_identified` — the extension from classical GRUT dynamics to quantum open-system dynamics carries a minimal but nonzero structural burden; the Lindbladian choice minimizes this burden.

**From Q-C.5:**
- `effective_regime_constitutive_recovery_demonstrated` — in the Markovian + weak-coupling regime, the expectation-value equation τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩ is recovered from the Lindblad master equation.
- `partial_parameter_matching_achieved` — τ² = 3/2 fixes the unique parameter of the constitutive equation; the parameter τ is matched to the dissipation rate γ = 1/τ.
- `lindbladian_preference_retained` — Q-C.5 does not overturn the Q-C preference; the Lindbladian-like structure is retained after constitutive recovery is verified.

### Jump Operator Specification

The jump operator fixed in Q-C.5 and inherited into Q-D is:

```
L = (1/√τ) · Φ̂
γ = 1/τ
τ² = 3/2
γ · τ = 1.0 (exact, by construction)
```

The product γ·τ = 1.0 is an exact algebraic consequence of the Q-C.5 parameter matching. It is not an approximation.

### Kinematic Package Inheritance

From Q-C0, the kinematic package is:

| Item | Appendix P Classification |
|---|---|
| J (momentum/kinetic sector) | MIP (minimally-in-place) |
| g (metric/geometric sector) | MIP |
| Lindbladian-like generator | MBU (minimally-but-unbuilt) |

The MBU classification of the generator propagates: all Q-D results that depend on the Lindbladian-like generator carry at minimum an MBU Appendix P floor. Because Q-D results depend on this generator, the `motivated_but_unbuilt` floor applies to the entire Q-D appendix.

### Regime Conditions (Inherited, Binding)

The following conditions are not optional context — they are preconditions for the Q-D results. Any application of Q-D results outside these regimes is not authorized.

1. **Bath memory time ≪ τ:** The Markovian approximation requires that environmental correlations decay on timescales short compared to τ. This is the Born-Markov regime.
2. **Weak coupling:** The system-bath coupling must be weak enough that the Born approximation (factorization of total density matrix) remains valid throughout.
3. **Effective regime:** The constitutive recovery result (Q-C.5) holds only in this regime. Q-D decoherence results are derived under the same regime.

These conditions are not "fine print." They are structural constraints that define what `effective_regime_decoherence_demonstrated` means. The word "effective_regime" in the decoherence verdict refers specifically to these inherited conditions.

---

## Section 3 — Decoherence Mechanism Analysis

### Setup

The Lindblad master equation with a single jump operator L = (1/√τ)·Φ̂ takes the form:

```
dρ/dt = -i[H, ρ] + γ(L ρ L† - ½{L†L, ρ})
```

where γ = 1/τ and L†L = (1/τ)·Φ̂²  (assuming Φ̂ is self-adjoint, so L† = L = (1/√τ)·Φ̂).

The dissipator term is:

```
𝒟[ρ] = γ(Φ̂ρΦ̂/τ - ½{Φ̂²/τ, ρ})
      = (1/τ)(Φ̂ρΦ̂ - ½Φ̂²ρ - ½ρΦ̂²)
```

### Exact Derivation in the Φ̂-Eigenbasis

Work in the eigenbasis of Φ̂ where Φ̂|φₙ⟩ = φₙ|φₙ⟩. Denote matrix elements ρₘₙ = ⟨φₘ|ρ|φₙ⟩. The dissipator acts on an off-diagonal element as follows:

```
⟨φₘ| [γ(Φ̂ρΦ̂† - ½{Φ̂†Φ̂, ρ})] |φₙ⟩

= γ [⟨φₘ|Φ̂ρΦ̂|φₙ⟩ - ½⟨φₘ|Φ̂²ρ|φₙ⟩ - ½⟨φₘ|ρΦ̂²|φₙ⟩]

= γ [φₘ · ρₘₙ · φₙ - ½φₘ² · ρₘₙ - ½ρₘₙ · φₙ²]

= γ · ρₘₙ · [φₘφₙ - ½φₘ² - ½φₙ²]

= -½γ(φₘ - φₙ)² · ρₘₙ
```

The step from line 2 to line 3 uses Φ̂|φₙ⟩ = φₙ|φₙ⟩ and ⟨φₘ|Φ̂ = φₘ⟨φₘ|. The step from line 3 to line 4 factors ρₘₙ. The final step is the algebraic identity:

```
φₘφₙ - ½φₘ² - ½φₙ² = -½(φₘ² - 2φₘφₙ + φₙ²) = -½(φₘ - φₙ)²
```

### Result

```
dρₘₙ/dt|_diss = -½γ(φₘ - φₙ)² · ρₘₙ
```

This is the central result of Q-D. Its implications are exact within the regime conditions:

- **Off-diagonal elements (φₘ ≠ φₙ):** The dissipator drives exponential decay at rate:
  ```
  R_dec = ½γ(φₘ - φₙ)² = (φₘ - φₙ)²/(2τ)
  ```
  The larger the eigenvalue separation, the faster the decoherence. Off-diagonal elements are not merely suppressed — they decay at a rate set by the squared eigenvalue difference.

- **Diagonal elements (φₘ = φₙ):** The decay rate R_dec = 0. The dissipator does not affect the diagonal. Population on the diagonal is not destroyed by decoherence — it is redistributed only by coherent Hamiltonian dynamics.

- **Basis selection:** The Φ̂-eigenbasis is the unique basis in which diagonal elements are protected and off-diagonal elements decay. This is the decoherence basis.

### Classification

The verdict `effective_regime_decoherence_demonstrated` is warranted because:

1. The derivation is exact in the Φ̂-eigenbasis under the inherited regime conditions.
2. The regime conditions (Markovian, weak-coupling) are genuine constraints: the result does not hold outside the effective regime.
3. The jump operator L ∝ Φ̂ is required: a different jump operator would select a different decoherence basis.
4. The result is derived from the GRUT-preferred Lindbladian-like law (Q-C), not assumed independently.

**Critical distinction:** The derivation demonstrates that off-diagonal coherences decay. It does not select which diagonal element "wins." After decoherence, the density matrix is approximately diagonal in the Φ̂-eigenbasis, but the diagonal entries ρₙₙ are determined by prior dynamics and initial conditions — not by the decoherence mechanism itself. The decoherence mechanism is blind to the relative magnitudes of the diagonal entries. This distinction between coherence suppression and outcome selection is the fundamental boundary of Q-D.

---

## Section 4 — Pointer-Basis Analysis

The pointer-basis problem asks: in what basis does the system become effectively classical under the influence of environmental decoherence? For GRUT's Q-D structure, this question has a determinate answer at the level of a basis class, but not a fully pinned unique basis.

### Candidate Table

Five candidate pointer bases are assessed:

| ID | Name | Viable | Selection Mechanism |
|---|---|---|---|
| PB1 | Φ̂-eigenbasis (observable language) | ✓ | Zero decoherence rate for diagonal elements; off-diagonal decay rate = ½γ(φₘ−φₙ)² |
| PB2 | X̂-eigenbasis | ✗ | X̂ not independently specified in Q-D; no dynamical selection mechanism present |
| PB3 | Jump-operator eigenbasis (dynamical language) | ✓ | Jump operator L ∝ Φ̂ dynamically selects its own eigenbasis as the stable, non-decohering basis |
| PB4 | Reduced classical observable basis | ✗ | Not independent of PB1; coincides with PB1 in the expectation-value limit by Q-C.5 recovery |
| PB5 | No unique pointer basis (null case) | ✗ | Rejected: PB1 and PB3 both viable; the null case is not consistent with the Q-D derivation |

### Note on PB1 vs PB3

PB1 and PB3 do not identify two distinct bases. They identify the same basis class under two complementary descriptions:

- **PB1 — observable language:** "The eigenstates of Φ̂ have zero decoherence rate from the dissipator." This is a stability statement about the diagonal in the Φ̂-eigenbasis.
- **PB3 — dynamical language:** "The jump operator L = (1/√τ)·Φ̂ commutes with Φ̂ and therefore selects the Φ̂-eigenbasis as the basis left invariant by the dissipator."

These are two descriptions of one structural fact: the eigenbasis of the jump operator is the decoherence-stable basis. PB3 is designated the canonical selection label because it identifies the mechanism (the jump operator structure) rather than merely describing the consequence (diagonal stability).

**Count:** n_viable = 1 (one basis class, described via two consistent routes).

### Why Basis Class, Not Unique Basis

The verdict is `pointer_basis_class_selected` rather than `unique_pointer_basis_selected` for the following reason: the full spectrum of Φ̂ is not specified within the Q-D structure. If the spectrum of Φ̂ is degenerate — if multiple eigenstates share the same eigenvalue φₙ — then any linear combination of those degenerate eigenstates has R_dec = 0 and is equally "pointer-stable." The pointer basis class is the Φ̂-eigenbasis, but within degenerate eigenspaces the pointer basis is not pinned.

Until the spectrum of Φ̂ is fully specified (continuous? discrete? finitely or infinitely degenerate?), the pointer-basis class is identified but the unique pointer basis is not available. Claiming `unique_pointer_basis_selected` would outrun the available structure.

**Verdict:** `pointer_basis_class_selected`

### Why PB2 Is Rejected

X̂ appears in the Q-C.5 constitutive recovery as the "source" side of τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩. However, X̂ is not independently specified as an operator in Q-D, and no dynamical mechanism in Q-D selects the X̂-eigenbasis as decoherence-stable. The jump operator L ∝ Φ̂, not L ∝ X̂. PB2 would be viable only if the jump operator were redefined as L ∝ X̂, which is a different model not audited here.

### Why PB4 Is Rejected

PB4 (reduced classical observable basis) is presented as a candidate on the grounds that the classical limit of the GRUT observable might define a separate pointer basis. However, in the effective regime, ⟨Φ̂⟩ relaxes toward ⟨X̂⟩ (Q-C.5), and the expectation-value level coincides with the PB1 description. PB4 is not an independent candidate — it is PB1 viewed through the expectation-value lens. Counting it as independent would double-count.

---

## Section 5 — Decoherence-Timescale Analysis

The decoherence timescale τ_dec is defined as the inverse of the decoherence rate R_dec for a given pair of eigenstates:

```
τ_dec(φₘ, φₙ) = 1/R_dec = 2τ/(φₘ - φₙ)²  =  2τ/Δφ²
```

where Δφ = |φₘ − φₙ| is the eigenvalue separation.

### Numerical Table (Reference Values)

| Quantity | Formula | Value (at Δφ = √2) |
|---|---|---|
| τ² | fixed by Q-C.5 parameter matching | 3/2 = 1.5 |
| τ | √(3/2) | ≈ 1.2247 |
| γ = 1/τ | 1/√(3/2) | ≈ 0.8165 |
| R_dec(Δφ) | Δφ²/(2τ) | 1/τ = γ ≈ 0.8165 at Δφ = √2 |
| τ_dec(Δφ) | 2τ/Δφ² | τ ≈ 1.2247 at Δφ = √2 |

At the reference separation Δφ = √2, the decoherence timescale equals τ exactly:

```
τ_dec(√2) = 2τ/(√2)² = 2τ/2 = τ
```

This is not a coincidence of fine-tuning — it is an algebraic consequence of τ² = 3/2 and the Q-C.5 parameter matching. The single timescale τ governs both constitutive relaxation (Q-C.5) and decoherence (Q-D) at eigenvalue separation √2.

### Regime Analysis

Three regimes of the eigenvalue separation Δφ relative to unity:

**Large separation (Δφ ≫ 1):**
```
τ_dec = 2τ/Δφ² ≪ τ
```
Decoherence is fast relative to the constitutive relaxation timescale. Superpositions of widely-separated eigenstates are destroyed quickly; the system effectively classicalizes on the decoherence timescale before the constitutive relaxation completes.

**Unit separation (Δφ = √2, reference case):**
```
τ_dec = τ
```
Decoherence and constitutive relaxation occur on the same timescale. The two processes are not separable into "fast environment" and "slow system." This is the regime where Q-C.5 and Q-D results are most tightly coupled.

**Small separation (Δφ → 0):**
```
τ_dec = 2τ/Δφ² → ∞
```
Nearly-degenerate eigenstates decohere arbitrarily slowly. In the strict degenerate limit (Δφ = 0), decoherence does not occur at all between those states. This is consistent with the pointer-basis degeneracy caveat in Section 4: degenerate eigenstates are not distinguished by the dissipator.

### Structural Observation

The eigenvalue separation Δφ is the only free parameter in the decoherence timescale formula. The timescale τ is fixed by Q-C.5 and cannot be re-tuned independently without changing the constitutive recovery. This means Q-D results are not freely adjustable — the decoherence speed is set by the same parameter that determines the relaxation speed of ⟨Φ̂⟩. This is a structural coherence across Q-C.5 and Q-D that has no additional free parameters.

---

## Section 6 — Measurement-Bridge Analysis

The measurement-bridge problem asks: does the GRUT quantum extension close the gap from quantum dynamics to measurement outcomes? This section audits five progressive levels of measurement closure.

### Level Table

| Level | Achieved | Basis |
|---|---|---|
| Decoherence only | ✓ | Off-diagonal element decay demonstrated in Section 3 |
| Decoherence + pointer structure | ✓ | Φ̂-eigenbasis pointer class identified in Section 4 |
| Decoherence + partial determination | ✗ | No tendency toward specific outcomes demonstrated; diagonal evolves without selection bias |
| Full measurement closure | ✗ | No collapse mechanism, no Born rule, no irreversible branching; observer-conditioned update absent |
| Born-rule weighting | ✗ | Probability mechanism entirely absent; FFM1 from Q-A charter prohibits Born-rule claims |

### What Q-D Establishes

The GRUT quantum extension demonstrates two things in Q-D:

1. **Decoherence:** Off-diagonal density-matrix elements in the Φ̂-eigenbasis decay exponentially at rate R_dec = (φₘ−φₙ)²/(2τ). This is a derivation from the preferred Lindbladian-like law, not an assumption.

2. **Pointer structure:** The Φ̂-eigenbasis is identified as the decoherence-stable pointer-basis class via the dynamical mechanism of the jump operator L ∝ Φ̂.

Together, these constitute `decoherence_plus_pointer_structure`. This is a genuine result. It is not nothing. But it is also not measurement closure.

### The Genuine Gap

After decoherence, the density matrix ρ is approximately diagonal in the Φ̂-eigenbasis:

```
ρ ≈ Σₙ ρₙₙ |φₙ⟩⟨φₙ|   (after decoherence timescale)
```

The diagonal entries ρₙₙ are non-negative and sum to one (trace preservation). They are determined by the initial state and the coherent Hamiltonian evolution. What is absent is any mechanism that:

- Selects one n and declares |φₙ⟩ the "actual" outcome.
- Weights the probabilities of different outcomes according to Born rule Prob(n) = ρₙₙ.
- Produces an irreversible branch selection (no "collapse").
- Conditions the state on an observer's measurement record.

The gap between "approximately diagonal density matrix" and "single outcome selected with Born-rule probabilities" is the measurement problem, and Q-D does not close it. This is not a deficiency of Q-D specifically — it is the standard situation for open-system quantum mechanics. The Lindblad master equation is a deterministic equation for ρ. It does not produce stochastic outcome selection.

The measurement scope verdict `decoherence_plus_pointer_structure` is therefore an accurate and complete description of what Q-D delivers.

### BSR Classification of the Gap

The gap is classified as BSR (bounded structural result — absence recorded, not permanent impossibility). BSR means:

- The absence of outcome selection and Born-rule derivation is documented as a structural fact of the audited framework.
- It does not mean outcome selection is impossible in principle in any extension of GRUT.
- It does not mean Q-D has failed. The audit question was whether GRUT natively derives these things, and the answer is documented.
- Future appendices (Q-E and beyond) may introduce additional structure that addresses the gap, but they must do so explicitly — they cannot retroactively attribute outcome selection to Q-D.

---

## Section 7 — Outcome-Selection Obstruction Analysis

Four mechanisms by which outcome selection could in principle be introduced are assessed. All four are absent from the Q-D structure.

### Obstruction Table

| Mechanism | Present | Reason | Appendix P |
|---|---|---|---|
| Single-outcome selection | ✗ | Lindblad master equation is deterministic for ρ; it evolves the full density matrix without stochastic branching | BSR |
| Born-rule probabilities | ✗ | No probability-weighting formula is present in Q-D; Q-A charter FFM1 prohibits Born-rule claims from open-system dynamics alone | BSR |
| Irreversible branch selection | ✗ | Lindblad evolution is continuous, trace-preserving, and completely positive; no branch collapse or irreversible selection occurs | BSR |
| Observer-conditioned update | ✗ | No observer or detector coupling is defined in Q-D; no measurement model is introduced; conditional state update is not constructed | BSR |

### Mechanism-by-Mechanism Analysis

**Single-outcome selection:** The Lindblad master equation dρ/dt = ℒ[ρ] is a first-order ordinary differential equation in the space of density matrices. Given initial ρ(0), the solution ρ(t) is uniquely determined. There is no stochastic element in this equation that could "choose" one eigenstate over another. The equation evolves all diagonal entries ρₙₙ simultaneously. Nothing in the equation selects n = 3 over n = 7, for example. Outcome selection would require either a stochastic differential equation (quantum trajectory / quantum jump formalism) or an additional physical postulate. Neither is introduced in Q-D.

**Born-rule probabilities:** Born rule states Prob(outcome n) = ⟨φₙ|ρ|φₙ⟩ = ρₙₙ. The fact that ρₙₙ can be computed does not mean the Born rule is derived — it means the density-matrix formalism has diagonal entries. The Born rule is the interpretive postulate that identifies these diagonal entries as probabilities of measurement outcomes. This postulate is not derived from the Lindblad equation; it must be introduced separately. Q-A charter FFM1 (probability-injection prohibition) forbids claiming derivation of Born-rule probabilities from microdynamics that do not natively produce them. Q-D obeys FFM1.

**Irreversible branch selection:** Lindblad evolution satisfies:
- Trace preservation: Tr(ρ(t)) = 1 for all t.
- Complete positivity: ρ(t) is a valid density matrix for all t.
- Continuity: ρ(t) varies continuously in time.

These three properties together prohibit any discontinuous "collapse" in which ρ jumps from a mixed state to a pure state |φₙ⟩⟨φₙ|. Irreversible branch selection would require discontinuous evolution or an external intervention (measurement apparatus coupling). Neither is present in Q-D.

**Observer-conditioned update:** Observer-conditioned state update (von Neumann measurement postulate, Bayesian updating on measurement record, etc.) requires a model of the measurement apparatus and its coupling to the system. Q-D introduces no measurement apparatus. The system-environment coupling is modeled as an unobserved bath (the Lindblad formalism traces over the bath). There is no "observer" in the Lindblad bath — there is only environmental decoherence. Observer-conditioned update is therefore structurally absent, not merely uncomputed.

### The Fundamental Boundary

Decoherence suppresses interference between basis states. It does not suppress which basis state "happens." This distinction is fundamental and must not be blurred. After decoherence, ρ ≈ Σₙ ρₙₙ |φₙ⟩⟨φₙ|. The off-diagonal interference terms are gone. But the diagonal is a probability distribution over outcomes, not a single outcome. Selecting the outcome — extracting a single n from the distribution — is precisely what the measurement problem requires, and precisely what decoherence does not provide.

The diagonal entries ρₙₙ after decoherence represent: "the probability of finding the system in state |φₙ⟩ if a measurement is performed." They do not represent: "the system is in state |φₙ⟩." The transition from the first to the second reading is the measurement problem. Q-D is entirely located on the first side of this transition.

---

## Section 8 — Observable-Classicality Analysis

### Coincidence of Constitutive and Pointer Observables

The constitutive observable of Q-C.5 is Φ̂: it is the operator whose expectation value obeys the relaxation equation τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩. The pointer observable of Q-D is the eigenbasis of Φ̂: it is the basis in which decoherence leaves the diagonal invariant.

These coincide. The same operator Φ̂ appears as:
- The constitutive observable in Q-C.5 (classical relaxation of its expectation value).
- The jump operator (up to normalization) in Q-C and Q-D: L = (1/√τ)·Φ̂.
- The pointer observable in Q-D (eigenbasis = decoherence-stable basis).

**Exact headline statement:** The constitutive observable Φ̂ and the pointer observable coincide conditionally on the Q-C.5 jump-operator choice L ∝ Φ̂. This identification is internally coherent but not independently derived — it is a structural consequence of the same operator choice that yielded constitutive recovery in Q-C.5.

### Conditionality

The conditionality is genuine and must be stated. If the jump operator were changed to L ∝ Â for some other operator Â, then:

- The constitutive recovery (Q-C.5) would need re-derivation with L ∝ Â — it might or might not hold.
- The pointer basis would shift to the eigenbasis of Â.
- The constitutive observable Φ̂ would remain fixed (it is not set by the jump operator; it is the physical observable of the system).
- The coincidence of constitutive and pointer observables would break.

The coincidence is therefore not a necessary consequence of GRUT structure in general — it is a consequence of the specific jump operator L ∝ Φ̂ chosen in Q-C. The choice is motivated (it yields constitutive recovery), but it is a choice. Alternative jump operators are not audited in Q-D.

### Structural Coherence

The coincidence, conditional as it is, represents genuine structural coherence across Q-C.5 and Q-D. The variable that relaxes classically and the variable that decoheres are the same variable, under the same regime conditions. This means:

1. The classical limit of the GRUT quantum extension is not fragmented — the classicalization via expectation-value relaxation and the classicalization via decoherence both point to Φ̂.
2. The parameter τ governs both processes (constitutive relaxation timescale = τ; decoherence timescale = τ at Δφ = √2).
3. The effective-regime conditions (Markovian, weak-coupling) are shared between Q-C.5 and Q-D.

This is a notable structural coherence. It is `motivated_but_unbuilt` in Appendix P terms: the motivation is visible (coherent operator structure), but the build is unfinished (jump operator is MBU, Φ̂ spectrum unspecified, coincidence conditional).

---

## Section 9 — Exact Verdicts

### Verdict Table

| Verdict Key | Value |
|---|---|
| `decoherence_verdict` | `effective_regime_decoherence_demonstrated` |
| `pointer_verdict` | `pointer_basis_class_selected` |
| `measurement_scope_verdict` | `decoherence_plus_pointer_structure` |
| `outcome_selection_verdict` | `born_rule_or_outcome_selection_not_natively_derived` |
| `authorization_verdict` | `authorized_to_proceed_to_QE` |

**Overall Appendix P:** `motivated_but_unbuilt`

### Verdict Justifications

**Why `effective_regime_decoherence_demonstrated` and not `native_decoherence_demonstrated`?**
The derivation requires the Markovian regime (bath memory time ≪ τ) and the weak-coupling Born-Markov approximation. These are regime conditions, not properties of the GRUT structure in isolation. "Native" would imply derivation without regime conditions. "Effective_regime" correctly identifies the domain of the result.

**Why `pointer_basis_class_selected` and not `unique_pointer_basis_selected`?**
The spectrum of Φ̂ is unspecified. Degenerate eigenspaces of Φ̂ are all equally pointer-stable (R_dec = 0 within a degenerate subspace). The class is the Φ̂-eigenbasis, but within degenerate subspaces the unique basis is not pinned. Claiming uniqueness would outrun the available structure.

**Why `decoherence_plus_pointer_structure` and not `decoherence_plus_partial_determination_structure`?**
"Partial determination" would imply that the diagonal evolution exhibits some asymmetry or tendency toward preferred outcomes. No such asymmetry is present. The diagonal entries ρₙₙ evolve under coherent Hamiltonian dynamics, which Q-D does not constrain. The dissipator leaves all diagonal entries invariant (R_dec = 0 for all n). There is no partial determination.

**Why `decoherence_plus_pointer_structure` and not `effective_outcome_tendency_only`?**
"Effective_outcome_tendency" would suggest that outcomes are not selected exactly but have a tendency or preference. This would require some asymmetry in the diagonal evolution — for instance, if the dissipator drove ρ toward a preferred eigenstate. The dissipator does not do this: it drives off-diagonals to zero while leaving diagonals unchanged. No tendency language is warranted.

**Why `born_rule_or_outcome_selection_not_natively_derived`?**
This is the direct consequence of Section 7: all four outcome-selection mechanisms are absent. The "or" is precise — neither Born-rule probability weighting nor outcome selection (which could in principle occur without Born rule, in some interpretations) is natively derived. Both are absent.

**Why `authorized_to_proceed_to_QE`?**
Q-E benchmark toy models require decoherence and pointer structure as prerequisites for constructing sensible toy examples of the GRUT quantum dynamics. Both prerequisites are established in Q-D. Q-E does not require full measurement closure — it is a benchmark exercise, not a measurement theory. The authorization is granted with the binding constraints stated in Section 12.

---

## Section 10 — Allowed and Forbidden Claims

### Allowed Claims

The following eight claims are authorized by the Q-D audit. Each may be reproduced in downstream appendices without re-opening Q-D.

1. Effective-regime decoherence of off-diagonal density-matrix elements is demonstrated in the Φ̂-eigenbasis, under the Markovian and weak-coupling regime conditions inherited from Q-C.5. The decoherence rate is R_dec = (φₘ−φₙ)²/(2τ).

2. The pointer-basis class is identified as the Φ̂-eigenbasis via dynamical selection by jump operator L = (1/√τ)·Φ̂. The selection mechanism is: the jump operator L commutes with Φ̂ (since L ∝ Φ̂), leaving the Φ̂-eigenbasis invariant under the dissipator.

3. The decoherence timescale is τ_dec = 2τ/Δφ². At eigenvalue separation Δφ = √2, τ_dec = τ exactly, consistent with all prior τ identifications in the quantum program.

4. The constitutive observable Φ̂ and the pointer observable (Φ̂-eigenbasis) coincide conditionally on the Q-C.5 jump-operator choice L ∝ Φ̂. This identification is a structural consequence of the same operator choice that yielded constitutive recovery in Q-C.5.

5. The measurement scope established by Q-D is `decoherence_plus_pointer_structure`. This is not full measurement closure. The gap between decoherence plus pointer structure and full measurement closure is genuine and documented as BSR.

6. All four outcome-selection mechanisms (single-outcome selection, Born-rule probabilities, irreversible branch selection, observer-conditioned update) are absent from the Q-D structure. These absences are classified BSR.

7. Q-E (benchmark toy models) is authorized to proceed subject to the binding constraints stated in Section 12.

8. All Q-D results carry `motivated_but_unbuilt` Appendix P floor, inherited from the MBU status of the Lindbladian-like generator (Q-C0).

### Forbidden Claims

The following eight claims are prohibited from any downstream appendix, document, or summary that cites Q-D results.

1. Decoherence implies, causes, or is equivalent to wavefunction collapse. Off-diagonal suppression is not collapse. Collapse requires irreversible single-outcome selection, which is absent.

2. Pointer-basis selection implies Born-rule probability weighting. Identifying which basis is stable does not assign probabilities to specific outcomes in that basis.

3. Off-diagonal suppression yields single-outcome selection. Suppressing interference between basis states is not the same as selecting one basis state.

4. The decoherence result is native GRUT canon. All Q-D results are MBU — they depend on the unbuilt Lindbladian-like generator and the regime conditions of Q-C.5.

5. Constitutive-observable recovery in Q-C.5 implies full measurement solved. Q-C.5 recovery is at the expectation-value level: τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩. This is not outcome-level measurement.

6. The observer problem is solved by Lindbladian open-system dynamics. The Lindblad formalism traces over the bath; it does not model an observer. The observer problem requires outcome selection, which Q-D does not provide.

7. Born rule is derived from or implied by any Q-D result. Born-rule derivation is explicitly out of scope in Q-D. The Q-A charter FFM1 (probability-injection prohibition) is in force throughout.

8. Pointer-basis identification fixes the ontology of measurement outcomes. Identifying the basis class in which decoherence is fast is a kinematic structural result. It does not determine what "actually happens" when a measurement occurs — that is an interpretive question that Q-D does not address.

---

## Section 11 — Exact Nonclaims

The following eight nonclaims are stated verbatim. Each is a precise doctrinal boundary marker for the Q-D audit. Downstream appendices must not assert any of these.

1. `NOT_claiming_decoherence_therefore_collapse__off_diagonal_suppression_does_not_select_single_outcomes`

2. `NOT_claiming_pointer_basis_therefore_Born_rule__basis_stability_does_not_yield_probability_weighting`

3. `NOT_claiming_off_diagonal_suppression_therefore_single_outcome__decoherence_removes_interference_not_branches`

4. `NOT_claiming_effective_regime_result_therefore_native_canon__all_QD_results_carry_MBU_floor_per_QA_R3`

5. `NOT_claiming_constitutive_observable_recovery_therefore_full_measurement_solved__QC5_recovery_is_expectation_value_level_only`

6. `NOT_claiming_Lindbladian_decoherence_therefore_observer_problem_solved__observer_problem_requires_outcome_selection_which_is_not_demonstrated`

7. `NOT_claiming_open_system_dynamics_therefore_probabilities_derived__Born_rule_derivation_is_explicitly_out_of_scope`

8. `NOT_claiming_basis_stability_therefore_ontology_fixed__pointer_basis_class_is_kinematic_not_ontological`

### Nonclaim Commentary

Nonclaim 1 is the primary gate. Every measurement-theory discussion must clear this gate first: decoherence is not collapse. Nonclaim 3 restates this at a more specific level: off-diagonal suppression removes interference terms from the density matrix; it does not remove branches, select outcomes, or force the universe to choose a reality.

Nonclaims 2 and 7 together close the probability gap: neither basis stability (nonclaim 2) nor open-system dynamics in general (nonclaim 7) yields Born-rule probabilities. These are independent routes to the same gap.

Nonclaim 4 is the Appendix P floor: the MBU classification is not a matter of degree. All Q-D results carry it. There is no subset of Q-D results that is "effectively canon."

Nonclaim 5 is the Q-C.5 boundary: the expectation-value recovery (τ·d⟨Φ̂⟩/dt + ⟨Φ̂⟩ = ⟨X̂⟩) is a statement about ⟨Φ̂⟩, not about individual measurement outcomes. Reading Q-C.5 as "measurement solved at expectation-value level" conflates expectation values with outcomes.

Nonclaim 6 addresses the observer problem specifically: the Lindblad bath is not an observer. Tracing out an unobserved environment is not the same as conditioning on an observer's measurement record. The observer problem requires outcome selection; nonclaim 1 establishes that Q-D does not provide this.

Nonclaim 8 is the ontology gate: identifying a pointer-basis class is a kinematic result. It says which basis decoheres fastest. It does not say which element of that basis is "real" or "selected." Ontological claims about measurement outcomes are out of scope for Q-D.

---

## Section 12 — Whether Q-E May Proceed

### Authorization Verdict

**`authorized_to_proceed_to_QE`**

Q-E (benchmark toy models) is authorized. The authorization is not conditional on resolving the measurement gap — Q-E is not a measurement theory appendix. Q-E's scope is to test whether the GRUT Lindbladian-like law with L = (1/√τ)·Φ̂ produces physically sensible behavior on benchmark quantum states, and to verify that Q-C.5 constitutive recovery and Q-D decoherence are mutually consistent in toy examples.

### Binding Constraints for Q-E

The following three constraints are binding. Violation of any constraint would require reopening Q-D before Q-E results are credited.

**Constraint QE-1: No Born rule assumption.**
Q-E must not assume Born-rule probabilities or outcome selection. These are absent from Q-D (`outcome_selection_verdict` = `born_rule_or_outcome_selection_not_natively_derived`). If Q-E requires probability assignments, it must introduce them explicitly as additional structure — not as inherited results from Q-D.

**Constraint QE-2: MBU/MIP floor inheritance.**
All Q-E results inherit the `motivated_but_unbuilt` Appendix P floor from Q-D (and transitively from Q-C's MBU generator and Q-C0's MIP kinematic package). Q-E may not claim MIP or canonical status for any result derived from the Lindbladian-like law.

**Constraint QE-3: No full measurement closure assumption.**
Q-E must not assume that the measurement scope exceeds `decoherence_plus_pointer_structure`. Benchmark models that require collapse, observer coupling, or irreversible outcome selection as inputs are outside the authorized scope of Q-E under Q-D authorization.

### What Q-E Should Do

1. Test whether the Lindbladian-like law with L = (1/√τ)·Φ̂ and γ = 1/τ produces physically sensible density-matrix evolution on explicitly specified benchmark initial states.

2. Verify that the constitutive recovery (Q-C.5) and decoherence (Q-D) are mutually consistent in toy examples: specifically, that a toy example can simultaneously exhibit τ-timescale relaxation of ⟨Φ̂⟩ and R_dec-rate decay of off-diagonal elements, with no contradiction.

3. Probe the decoherence timescale formula τ_dec = 2τ/Δφ² on benchmark states with specified eigenvalue separations, verifying the Section 5 analysis on concrete examples.

4. Identify whether any toy-model results motivate further specification of Φ̂'s spectrum, or provide grounds for preferring a discrete over continuous spectrum.

### What Q-E Must Not Do

1. Assume wavefunction collapse occurs during toy-model evolution. The Lindblad equation does not collapse; Q-E toy models do not collapse.

2. Invoke Born-rule probabilities to compute toy-model observables as "measurement outcomes." Expectation values ⟨Φ̂⟩ may be computed; outcome probabilities Prob(n) = ρₙₙ may be stated as conditional quantities (conditional on an unmodeled measurement), but may not be presented as derived from the GRUT structure.

3. Claim that toy-model success implies the measurement problem is solved. Toy-model success demonstrates internal consistency of the Lindbladian-like law on benchmark states. It does not close the measurement bridge gap documented in Q-D.

4. Introduce new operator content (additional jump operators, new kinematic variables) without explicit statement that this constitutes a new extension beyond the Q-D audited structure.

---

## Quantum Program Inheritance Table

Complete inheritance record from Q-B through Q-D, with Q-E as the forthcoming appendix.

| Appendix | Appendix P | Key Result |
|---|---|---|
| Q-B | BSR | No native quantum state space; Hilbert-space structure is absent from GRUT canon |
| Q-B.5 | MIP | J is MIP; ghost obstruction confirmed; indefinite metric sector documented |
| Q-C0 | MIP | Minimum kinematic package: J (MIP) + g (MIP) + Lindbladian-like generator (MBU) |
| Q-C | MBU | Lindbladian-like law preferred; minimal extension burden identified; L = (1/√τ)·Φ̂ |
| Q-C.5 | MBU | Effective-regime constitutive recovery demonstrated; τ² = 3/2; γ·τ = 1.0 exact |
| **Q-D** | **MBU** | **Effective-regime decoherence + pointer-basis class (Φ̂-eigenbasis); outcome selection and Born rule unresolved** |
| Q-E | TBD | Benchmark toy models (next); authorized under Q-D binding constraints QE-1, QE-2, QE-3 |

### Cumulative Gaps Carried into Q-E

At the close of Q-D, the following structural gaps are open and carried forward:

| Gap | Documented In | Status |
|---|---|---|
| No native quantum state space | Q-B | BSR — Hilbert space is extension, not canon |
| Ghost obstruction in J sector | Q-B.5 | MIP — documented, not resolved |
| Lindbladian-like generator unbuilt | Q-C, Q-C0 | MBU — preferred but not derived |
| Φ̂ spectrum unspecified | Q-C.5, Q-D | Open — continuous? discrete? degenerate? |
| Outcome selection absent | Q-D | BSR — documented absence, not impossibility |
| Born-rule probabilities absent | Q-D | BSR — not derivable from audited structure |
| Observer coupling undefined | Q-D | BSR — no measurement model introduced |
| X̂ operator unspecified | Q-C.5, Q-D | Open — source side of constitutive equation |

These gaps do not prevent Q-E from proceeding. They are the honest accounting of what the GRUT quantum program has and has not established as of Q-D.

---

*Appendix Q-D complete. Authorization `authorized_to_proceed_to_QE` granted. All Q-D results carry `motivated_but_unbuilt` Appendix P floor. The decoherence verdict must not be read as measurement-bridge solved.*
