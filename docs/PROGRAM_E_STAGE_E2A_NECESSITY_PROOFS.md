# Program E — Stage E2-A: Necessity Proof Attempts (T1 then T3)

**Predecessor:** E1 (formal_system_ready). Axioms A1-A5. Imports IA-1..5. Branches AF-1a/b, AF-2a/b.

---

## 1. Branch-Specific Theorem Statements

### T1: Decoherence necessity

#### T1-AF-2a (Classical probability)

```
ASSUMPTIONS: A1-A5 (history space, poset, observer, probability, consistency).
             AF-2a: μ is a real-valued Kolmogorov probability measure.

CLAIM: Consistent probability assignment over histories requires a
       decoherence condition on off-diagonal terms.

PROOF STRATEGY: Examine whether the classical probability axioms impose
  any constraint analogous to decoherence.

FAILURE: If classical probability is self-consistent without any
  additional condition — i.e., μ(A) = Σ_{h ∈ A} μ(h) is always
  well-defined for any non-negative μ with Σ μ(h) = 1.
```

#### T1-AF-2b (Quantum decoherence functional)

```
ASSUMPTIONS: A1-A5 + IA-2 (decoherence functional D: H×H → ℂ with
             D(h,h) ≥ 0, hermiticity, normalization).
             AF-2b: probabilities are derived from D via μ(A) = Σ_{h∈A} D(h,h).

CLAIM: For μ to be a well-defined (additive) probability measure on
       coarse-grained history classes, the off-diagonal terms of D must
       satisfy a consistency/decoherence condition:

       Re Σ_{h∈α, h'∈β, h≠h'} D(h, h') ≈ 0

       for distinct coarse-grained classes α ≠ β within the same partition.

PROOF STRATEGY: Show that additivity μ(α ∪ β) = μ(α) + μ(β) requires
  the vanishing of interference terms.

FAILURE: If additivity can hold even with nonzero off-diagonal D(h,h').
```

### T3: Entropy-growth necessity

```
ASSUMPTIONS: A1-A5 + IA-4 (coarse-graining C: H_fine → H_coarse)
             + IA-5 (typicality: μ approximately uniform within each macrostate).

CLAIM: The Boltzmann entropy S[M] = log |C⁻¹(M)| is non-decreasing along
       the causal ordering with probability approaching 1 as the number
       of microstates grows:

       Prob(S[M₂] ≥ S[M₁]) → 1 for M₁ ≤ M₂

PROOF STRATEGY: Boltzmann H-theorem adapted to the history framework.
  Show that typicality + causal ordering + consistency imply that
  transitions to higher-entropy macrostates are exponentially more probable.

FAILURE: If a consistent, typical measure assigns non-negligible probability
  to entropy-decreasing trajectories even at large system size.
```

---

## 2. T1 Proof Attempt

### Branch AF-2a: Classical probability

**Theorem candidate T1-AF-2a:**

Under classical probability (real-valued μ), is any decoherence-like condition necessary?

**Analysis:**

In classical probability, the measure μ assigns a non-negative real number to each fine-grained history:

```
μ: H → [0,1],    Σ_h μ(h) = 1
```

For a coarse-grained class α ⊂ H:

```
μ(α) = Σ_{h ∈ α} μ(h)
```

Additivity for disjoint classes:

```
μ(α ∪ β) = Σ_{h ∈ α∪β} μ(h) = Σ_{h ∈ α} μ(h) + Σ_{h ∈ β} μ(h) = μ(α) + μ(β)
```

This holds AUTOMATICALLY for any non-negative measure. No condition on "interference" or "off-diagonal terms" is needed because there ARE no off-diagonal terms in classical probability. The measure is diagonal by construction.

**Result: T1-AF-2a is TRIVIALLY TRUE (vacuously satisfied).**

The decoherence condition is vacuous in the classical branch because classical probability has no interference terms to suppress. This is not a theorem — it is the absence of a non-trivial condition.

**Classification: NOT A NECESSITY RESULT.** The classical branch produces no constraint. T1 has content only in the quantum branch.

---

### Branch AF-2b: Quantum decoherence functional

**Theorem candidate T1-AF-2b:**

Under quantum probability (IA-2: decoherence functional D), does consistent probability assignment require decoherence?

**Proof:**

**Step 1: Setup.**

Let D: H × H → ℂ satisfy (IA-2):
- D(h, h) ≥ 0 for all h
- D(h, h') = D(h', h)* (hermiticity)
- Σ_{h,h'} D(h, h') = 1 (normalization)

The candidate probability for a coarse-grained class α is:

```
p(α) = Σ_{h ∈ α} D(h, h)
```

This is the diagonal part of D restricted to α.

**Step 2: The additivity test.**

Consider a partition of H into coarse-grained classes {α₁, α₂, ...}. The probability of the union α_i ∪ α_j (for disjoint i, j) must satisfy:

```
p(α_i ∪ α_j) = p(α_i) + p(α_j)     [additivity]
```

Now compute p(α_i ∪ α_j) from the decoherence functional:

```
p(α_i ∪ α_j) = Σ_{h ∈ α_i ∪ α_j} D(h, h)
              = Σ_{h ∈ α_i} D(h, h) + Σ_{h ∈ α_j} D(h, h)
              = p(α_i) + p(α_j)
```

**Wait.** This is just the sum of diagonal terms. It is automatically additive because we defined p from the diagonal of D. The off-diagonal terms D(h, h') for h ≠ h' do NOT appear in p at all.

**Step 3: Where does decoherence actually enter?**

The standard decoherent-histories argument involves a DIFFERENT probability formula. The Gell-Mann–Hartle probability for a coarse-grained class α is:

```
p_GH(α) = Σ_{h ∈ α, h' ∈ α} D(h, h')     [sum over ALL pairs within α]
```

This INCLUDES the off-diagonal terms. This is the square of a sum of amplitudes, not a sum of squares. It is the quantum rule.

The diagonal-only formula p(α) = Σ_{h ∈ α} D(h, h) is the DECOHERED probability — it is what you get AFTER the off-diagonal terms vanish.

**The question becomes:** Which probability formula is correct?

**Step 4: The Gell-Mann–Hartle consistency condition.**

For p_GH to be additive (probability sum rule), we need:

```
p_GH(α_i ∪ α_j) = p_GH(α_i) + p_GH(α_j)
```

Computing:

```
p_GH(α_i ∪ α_j) = Σ_{h ∈ α_i∪α_j, h' ∈ α_i∪α_j} D(h, h')
                  = Σ_{h,h' ∈ α_i} D(h,h') + Σ_{h,h' ∈ α_j} D(h,h')
                    + Σ_{h ∈ α_i, h' ∈ α_j} D(h,h') + Σ_{h ∈ α_j, h' ∈ α_i} D(h,h')
                  = p_GH(α_i) + p_GH(α_j) + 2 Re Σ_{h ∈ α_i, h' ∈ α_j} D(h,h')
```

Additivity requires:

```
Re Σ_{h ∈ α_i, h' ∈ α_j} D(h, h') = 0     for all i ≠ j
```

**THIS IS THE DECOHERENCE CONDITION.** It states that the real part of the off-diagonal block of D between distinct coarse-grained classes must vanish.

**Step 5: Is this a theorem or a definition?**

It is a THEOREM given the following chain:

```
Premise 1: Probabilities are assigned by p_GH(α) = Σ_{h,h' ∈ α} D(h,h').  [quantum probability rule]
Premise 2: p_GH must satisfy the probability sum rule (additivity).          [from A4]
Conclusion: Re D(h,h') = 0 for h ∈ α_i, h' ∈ α_j with i ≠ j.             [decoherence condition]
```

The proof is a three-line algebraic identity. QED.

**Step 6: What are the real assumptions?**

The non-trivial content is in **Premise 1**: that probabilities are computed from the FULL decoherence functional (including off-diagonal terms), not from the diagonal alone. This is the quantum probability rule — it is NOT a consequence of A1-A5. It is a consequence of IA-2 combined with the specific interpretation that p_GH (not p_diagonal) is the physical probability.

**If one uses the diagonal formula p(α) = Σ D(h,h):** additivity is automatic, no decoherence condition is needed, and T1 is trivial (same as AF-2a).

**If one uses the GH formula p_GH(α) = Σ D(h,h'):** additivity REQUIRES decoherence. This is a genuine theorem.

**The fork:** which formula is "correct" depends on whether one adopts the quantum probability rule (p_GH) or the classical extraction (p_diagonal). This is the content of AF-2b: the quantum branch adopts p_GH by definition (via IA-2).

**Step 7: Statement of result.**

```
THEOREM T1-AF-2b:

Given: A history space (H, Σ) with a decoherence functional D satisfying
IA-2, and the quantum probability rule p(α) = Σ_{h,h' ∈ α} D(h,h'),
and the requirement that p satisfies the probability sum rule (A4):

Then: the decoherence condition
  Re Σ_{h ∈ α_i, h' ∈ α_j} D(h, h') = 0  for all i ≠ j
must hold for any partition {α_i} on which probabilities are assigned.

Proof: Direct algebraic expansion of the additivity condition. Three lines.
Status: PROVEN.
```

**Caveats and honest classification:**

1. The theorem is a CONDITIONAL result: it requires IA-2 (decoherence functional exists) and the quantum probability rule (p = p_GH, not p_diagonal). Without IA-2, the result is trivial.

2. The algebraic content is not new — it is the standard Gell-Mann–Hartle consistency condition (1990), reformulated in our axiom language. Program E's contribution is placing it within the A1-A5 + IA-2 framework, not the algebra itself.

3. The theorem does NOT derive the decoherence functional D from the primitives. It assumes D exists (IA-2) and derives what consistency requires of it.

---

### T1 Countermodel Battery

**Countermodel for T1 (attempt to violate):**

Can we have a system satisfying A1-A5 + IA-2 where p_GH is additive WITHOUT the decoherence condition?

No. The algebraic identity is exact:

```
p_GH(α∪β) − p_GH(α) − p_GH(β) = 2 Re Σ_{h∈α,h'∈β} D(h,h')
```

If this equals zero for all partitions, the decoherence condition holds. If it does not equal zero, additivity fails. There is no escape. **No countermodel exists within the declared branch.** The theorem is tight.

**Countermodel for the IMPORT IA-2:**

Model M2 (classical Markov chain from E1) satisfies A1-A5 without IA-2. In M2, there is no decoherence functional, and the decoherence condition is vacuous. This confirms that IA-2 is genuinely required — the theorem has no content without it.

---

### T1 Classification

| Branch | Result | Status | Confidence |
|--------|--------|:------:|:----------:|
| AF-2a (classical) | Trivially satisfied. No constraint. | **NOT A NECESSITY RESULT** | 1.00 |
| AF-2b (quantum, with IA-2) | Decoherence condition proven from additivity + GH probability rule. | **CONDITIONALLY NECESSARY** | 0.90 |

**Conditional on:** IA-2 (existence of decoherence functional) + quantum probability rule (p = p_GH). These are the imports. The theorem within them is exact.

---

## 3. T3 Proof Attempt

### Setup

```
ASSUMPTIONS: A1-A5 + IA-4 (coarse-graining C) + IA-5 (typicality).

CLAIM: Boltzmann entropy S[M] = log |C⁻¹(M)| is non-decreasing
along causal ordering with probability → 1 at large system size.
```

### Proof attempt

**Step 1: The counting argument.**

Consider a macrostate M₁ at time (causal position) t₁ and the macrostates {M₂} accessible from M₁ at a later causal position t₂. The number of microstates compatible with M₁ is W₁ = |C⁻¹(M₁)|.

Under the admissibility relation R (A5), each microstate h₁ ∈ C⁻¹(M₁) transitions to some microstate h₂ in the causal future. The microstate h₂ belongs to some macrostate M₂ = C(h₂).

**Step 2: Typicality argument.**

Under IA-5, μ is approximately uniform within each macrostate:

```
μ(h) ≈ 1/W₁  for h ∈ C⁻¹(M₁)
```

The probability of transitioning to macrostate M₂ is:

```
p(M₂ | M₁) = |{h₁ ∈ C⁻¹(M₁) : C(R(h₁)) = M₂}| / W₁
```

where R(h₁) denotes the microstate(s) reachable from h₁.

**Step 3: The Boltzmann argument.**

If the dynamics R is such that most microstates in C⁻¹(M₁) transition to macrostates with LARGER W₂ = |C⁻¹(M₂)|, then S[M₂] > S[M₁] with high probability.

The standard argument: the number of microstates in a "higher entropy" macrostate is exponentially larger than in a "lower entropy" one (in the thermodynamic limit). If the dynamics is "mixing" — meaning it does not confine microstates to low-entropy macrostates — then the overwhelming majority of transitions go uphill in entropy.

**Step 4: Where does this break?**

The argument requires:

**(a) The dynamics R is sufficiently mixing.** If R is a permutation that maps each macrostate to itself (a "non-ergodic" dynamics), entropy is constant — it does not increase. The argument requires that R explores the accessible phase space rather than remaining confined.

**(b) The system is large.** The exponential dominance of high-entropy states applies only in the thermodynamic limit (W >> 1). For small systems, entropy fluctuations are significant and can go either direction.

**(c) Typicality (IA-5) holds.** If the initial measure is NOT typical (e.g., concentrated on a special subset of C⁻¹(M₁)), the argument fails. A carefully prepared "anti-typical" measure can have decreasing entropy.

**Step 5: Is this a theorem?**

Strictly speaking: NO, it is not a theorem from A1-A5 + IA-4 + IA-5 alone. It requires an additional assumption about the dynamics R:

```
IA-6 (CANDIDATE): The admissibility relation R is "macroscopically mixing" —
  for sufficiently large systems, the fraction of microstates in C⁻¹(M₁)
  that transition to macrostates with S[M₂] < S[M₁] is exponentially
  small in the system size.
```

With IA-6, the entropy-growth result follows. Without IA-6, countermodels exist.

### T3 Countermodel Battery

**Countermodel CM-T3-1: Non-ergodic dynamics.**

Let H be the set of histories on a finite lattice. Let R be a permutation that maps each microstate to another microstate within the SAME macrostate (R preserves the macrostate). Then S[M₂] = S[M₁] for all transitions. Entropy is constant, not increasing. This system satisfies A1-A5 + IA-4 + IA-5 but violates T3's claim.

**Is CM-T3-1 "physical"?** It requires R to be exactly entropy-preserving, which is a measure-zero condition in the space of all admissibility relations. It is not generic. But it exists and satisfies the axioms.

**Countermodel CM-T3-2: Entropy-decreasing dynamics (anti-typical).**

Construct R such that it maps every microstate in a high-entropy macrostate M_high to a specific microstate in a low-entropy macrostate M_low. This is possible if |C⁻¹(M_high)| is large (many microstates map to the same target). Under IA-5 (typicality), the typical microstate in M_high transitions to M_low → entropy DECREASES.

**Is CM-T3-2 consistent?** Yes, provided R is well-defined. It satisfies A5 (admissibility is just a relation — no constraint on whether R increases or decreases entropy). It satisfies A1-A5, IA-4, IA-5.

**Conclusion:** T3 is NOT a theorem from A1-A5 + IA-4 + IA-5 alone. The axioms do not constrain R to be entropy-increasing. Additional assumptions about R (such as IA-6, mixing) are needed.

### T3 conditional result

```
THEOREM T3-CONDITIONAL:

Given: A1-A5 + IA-4 + IA-5 + IA-6 (macroscopic mixing):

Then: Prob(S[M₂] ≥ S[M₁]) → 1 as system size → ∞.

Proof: Standard Boltzmann H-theorem / typicality argument.
  The fraction of microstates transitioning to lower entropy is
  exponentially suppressed by the ratio of accessible phase space volumes.

Status: CONDITIONALLY PROVEN (requires IA-6).
```

### T3 Classification

| Condition set | Result | Status | Confidence |
|---------------|--------|:------:|:----------:|
| A1-A5 + IA-4 + IA-5 | NOT NECESSARY. Countermodels CM-T3-1, CM-T3-2 exist. | **NOT NECESSARY** from these axioms alone | 0.90 |
| A1-A5 + IA-4 + IA-5 + IA-6 (mixing) | Conditionally proven. | **CONDITIONALLY NECESSARY** | 0.80 |

**Conditional on:** IA-6 (macroscopic mixing). Without IA-6, the result fails. IA-6 is a DYNAMICAL assumption about R that is not derivable from the structural primitives P1-P5. It is a separate physical input.

---

## 4. Countermodel Summary

| Target | Countermodel | Axioms satisfied | Claim violated | Implication |
|:------:|-------------|:----------------:|:--------------:|-------------|
| T1-AF-2a | M2 (classical Markov) | A1-A5 (no IA-2) | T1 trivial | T1 requires IA-2 |
| T1-AF-2b | None found | A1-A5 + IA-2 | Cannot be violated | T1-AF-2b is tight |
| T3 | CM-T3-1 (non-ergodic R) | A1-A5 + IA-4 + IA-5 | S constant, not increasing | T3 requires mixing (IA-6) |
| T3 | CM-T3-2 (entropy-decreasing R) | A1-A5 + IA-4 + IA-5 | S decreasing | T3 requires mixing (IA-6) |

---

## 5. Status Classification

| Target | Branch/Conditions | Result | Confidence |
|:------:|-------------------|:------:|:----------:|
| **T1** | AF-2a (classical) | **VACUOUS** (no constraint, no content) | 1.00 |
| **T1** | AF-2b (quantum, IA-2 + GH rule) | **CONDITIONALLY NECESSARY** (decoherence condition proven from additivity) | 0.90 |
| **T3** | A1-A5 + IA-4 + IA-5 | **NOT NECESSARY** (countermodels exist) | 0.90 |
| **T3** | A1-A5 + IA-4 + IA-5 + IA-6 (mixing) | **CONDITIONALLY NECESSARY** (Boltzmann argument) | 0.80 |

### What "conditionally necessary" means precisely

For T1: decoherence is necessary IF you adopt quantum probability (IA-2 + GH rule). The condition IA-2 is an IMPORT — it is not derivable from P1-P5. The theorem is real but its premises include model content.

For T3: entropy growth is necessary IF the dynamics is macroscopically mixing (IA-6). The condition IA-6 is a DYNAMICAL import — it constrains the admissibility relation R beyond what A5 requires. The theorem is the standard Boltzmann argument, which has always required a mixing assumption (the historical "Stosszahlansatz" or molecular chaos hypothesis).

---

## 6. Exit-Token Impact Update

| Token | Status before E2-A | Status after E2-A | Reason |
|-------|:------------------:|:-----------------:|--------|
| **necessity_emerges** | Requires 2+ of T1-T4 proven + T5 finite | **NOT MET.** 0 unconditional proofs. 2 conditional proofs (T1-AF-2b, T3+IA-6). Conditional results require additional imports (IA-2, IA-6) that are themselves model-dependent assumptions. | Conditional ≠ unconditional |
| **conditional_necessity** | 1+ proven conditionally | **APPROACHING.** Two conditional results exist. But both depend on imports that bring significant model content (quantum probability, mixing). Whether these qualify as "weaker than postulating the answer" is debatable. | IA-2 and IA-6 are substantial imports |
| **non_uniqueness_persists** | All disproven or N=∞ | **NOT YET REACHED.** T1 and T3 are not disproven — they are conditional. T2, T4, T5 are untested. | More work needed |
| **blocked** | Cannot proceed | **NOT REACHED.** T2 and T5 remain as targets. | Proceed to E2-B |

### Assessment of import cost

The two conditional results cost:
- **IA-2:** A complex-valued decoherence functional. This is essentially the postulate that quantum mechanics (or something like it) governs the interference of histories. It is a MAJOR import — nearly equivalent to assuming quantum theory.
- **IA-6:** Macroscopic mixing. This is the classical Boltzmann hypothesis. It constrains the dynamics (the admissibility relation R) in a way that A5 does not. It is a MODERATE import — physically motivated but not derivable from structural primitives.

**Honest evaluation:** The Program E primitives P1-P5 alone are TOO WEAK to derive decoherence or entropy growth. Both require additional physical content: quantum probability for T1, dynamical mixing for T3. The structural primitives provide a framework (history space, causal ordering, probability) but do not determine the physics.

This is not a failure of Program E — it is an honest finding about the limits of purely structural axiomatics. The question "what must the universe be like?" cannot be answered from P1-P5 alone. It requires additional physical inputs.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **E2A-G1** | T1 analyzed in both AF-2 branches | **PASS** | AF-2a: trivially satisfied, no content. AF-2b: decoherence condition proven from additivity + GH rule (3-line algebra). Both branches completed. |
| **E2A-G2** | T3 analyzed with explicit IA-4/IA-5 dependence | **PASS** | T3 shown NOT necessary from A1-A5+IA-4+IA-5 alone (countermodels CM-T3-1, CM-T3-2). Conditionally necessary with IA-6 (mixing). Import dependence explicit. |
| **E2A-G3** | Countermodel or impossibility for each | **PASS** | T1-AF-2b: no countermodel (algebraic identity is tight). T3: two countermodels (non-ergodic, entropy-decreasing). |
| **E2A-G4** | Necessity status assigned with evidence | **PASS** | T1: conditionally necessary (AF-2b, confidence 0.90). T3: not necessary (without IA-6), conditionally necessary (with IA-6, confidence 0.80). |
| **E2A-G5** | Exit-token impact updated | **PASS** | necessity_emerges: not met. conditional_necessity: approaching (2 conditional results). non_uniqueness_persists: not reached. blocked: not reached. |

## Decision Token

### **proceed_E2B**

**Rationale:** T1 and T3 have produced conditional necessity results, not unconditional ones. The remaining targets T2 (covariant irreversibility) and T5 (uniqueness) are the higher-risk, potentially higher-reward theorems. T2 in particular (via IA-1, Lorentzian manifold) could provide the strongest constraint — if covariant irreversibility forces geometry-coupling, that would be a structural result beyond mere import-dependence. T5 depends on T1-T3 results and can now be scoped.

**Next:** E2-B attempts T2 (covariant irreversibility, requiring IA-1) and scopes T5 (uniqueness, given T1/T3 conditional results).

---

*Program E Stage E2-A complete. Decision: proceed_E2B. T1: conditionally necessary (quantum branch, IA-2 + GH rule, decoherence condition proven by algebra). T3: not necessary from primitives alone (countermodels exist); conditionally necessary with IA-6 (mixing). Two conditional results, zero unconditional. Import cost: IA-2 (quantum probability, major) and IA-6 (mixing, moderate). Structural primitives P1-P5 alone are too weak to derive decoherence or entropy growth. Exit token conditional_necessity is approaching but not met. Proceed to T2 and T5.*
