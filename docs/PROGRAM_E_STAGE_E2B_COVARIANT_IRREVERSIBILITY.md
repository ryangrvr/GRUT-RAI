# Program E — Stage E2-B: Covariant Irreversibility (T2) + Uniqueness Scope (T5)

**Predecessor:** E2-A (T1 conditionally necessary under IA-2; T3 conditionally necessary under IA-6; P1-P5 alone too weak).

---

## 1. T2 Theorem Candidates (Minimal-to-Strong Ladder)

### T2-min: Weakest assumptions

```
ASSUMPTIONS:
  A1-A5 (primitives).
  IA-1-min: The causal poset (E, ≤) admits a SMOOTH MANIFOLD embedding —
    i.e., E can be identified with points in a smooth manifold M, and ≤
    is compatible with a partial ordering derived from some continuous
    structure on M. (NO metric assumed. No Lorentzian signature. No dimension.)

CLAIM:
  If a first-order dissipative dynamics exists on M (a vector field V on M
  with a global attractor), and this dynamics is required to be compatible
  with the smooth structure (V is smooth), then V must be a gradient-like
  flow: there exists a smooth function L: M → ℝ such that V·∇L ≤ 0.

PROOF STRATEGY:
  Appeal to Conley's fundamental theorem of dynamical systems (1978):
  every continuous flow on a compact metric space admits a complete
  Lyapunov function L that decreases along orbits outside the chain-
  recurrent set. If the chain-recurrent set is a single fixed point
  (global attractor, from A5's admissibility), then L decreases
  everywhere except at the fixed point.

FALSIFICATION: A smooth dynamics on M with a unique global attractor
  that does NOT admit any smooth Lyapunov function. (This would
  contradict Conley's theorem on compact spaces.)
```

### T2-mid: Moderate imports

```
ASSUMPTIONS:
  A1-A5 + IA-1 (Lorentzian manifold (M, g_{μν})).
  IA-7 (new): The dissipative dynamics of a scalar field Φ on (M, g) is
    formulated via a CTP action that is invariant under spatial
    diffeomorphisms (3-diffeomorphisms that preserve the foliation).

CLAIM:
  Spatial diffeomorphism invariance of the CTP dissipative action
  constrains the dissipative term to couple to the extrinsic curvature
  K_{μν} or the lapse/shift of the foliation. Specifically: the
  "time direction" that defines irreversibility must be the unit normal
  n^μ to the spatial foliation, which is a GEOMETRIC object (derived
  from g_{μν} and the foliation choice), not an external structure.

PROOF STRATEGY:
  The dissipative term in the CTP action breaks time-reversal symmetry.
  In a diffeomorphism-invariant theory, the only available vector field
  that can define a preferred time direction without introducing external
  structure is n^μ (the foliation normal). The dissipative operator
  must therefore be constructed from n^μ and the spatial metric h_{ij} =
  g_{ij} + n_i n_j. The simplest such operator is n^μ ∂_μ Φ (the proper-
  time derivative), which is the "∂_t Φ" in the constitutive law.

  Reference: Salcedo, Simpkins & Solon (2025, arXiv:2412.21136) construct
  exactly this structure for dissipative open systems coupled to gravity.
  The minimal dissipative operator consistent with 3-diff invariance is:
  Δ_{μν} = (Γ/N)(K_{μν} - K P_{μν}) √(-g^{00})
  where N is the lapse, K is extrinsic curvature, and Γ is the dissipation
  coefficient.

FALSIFICATION: A spatially diffeomorphism-invariant CTP action with a
  dissipative term that does NOT couple to the foliation geometry (n^μ, K, N).
  If such a term exists and produces well-defined dissipation, T2-mid fails.
```

### T2-strong: Full geometric + thermodynamic imports

```
ASSUMPTIONS:
  A1-A5 + IA-1 (Lorentzian) + IA-7 (3-diff invariance) + IA-2 (decoherence
  functional) + IA-6 (mixing) + IA-8 (new): the FULL diffeomorphism group
  Diff(M) is a symmetry of the CTP action (not just spatial diffs).

CLAIM:
  Full diffeomorphism invariance of the CTP dissipative action, combined
  with decoherence (T1 result) and entropy growth (T3 result), forces the
  scalar field dynamics to be of the form:

    τ n^μ ∇_μ Φ + Φ = X(g)

  where τ is a scalar function, n^μ is the unit normal to some foliation,
  and X(g) is a scalar functional of the metric. The relaxation form is
  not a choice but a consequence of covariance + irreversibility +
  thermodynamic consistency.

PROOF STRATEGY:
  (i) Full diff-invariance requires the action to be a spacetime scalar.
  (ii) Irreversibility requires a preferred time direction → must be
       geometric (n^μ from a foliation or fluid velocity u^μ).
  (iii) First-order (overdamped) dynamics means the leading term is
        n^μ ∇_μ Φ, not □Φ or higher derivatives.
  (iv) The "target" X must be a scalar built from the metric → X = X(g).
  (v) The relaxation form τ n^μ ∇_μ Φ + Φ = X(g) is the unique
       first-order, scalar, covariant dissipative equation with a
       geometry-determined attractor.

FALSIFICATION:
  A first-order scalar dissipative equation on a Lorentzian manifold
  that (a) is fully diffeomorphism-invariant, (b) has a unique attractor,
  (c) is thermodynamically consistent (FDT-compatible), but (d) is NOT
  of the form τ n^μ ∇_μ Φ + Φ = X(g).
```

---

## 2. Import Ledger (Lemma-Level)

### T2-min

| Step | Import used | Import ID | Necessity | Pre-assumes conclusion? |
|------|-----------|:---------:|:---------:|:-----------------------:|
| "M is a smooth manifold" | Smooth manifold embedding of E | IA-1-min (new, weaker than IA-1) | REQUIRED | NO (manifold ≠ Lorentzian metric) |
| "V is a smooth vector field with global attractor" | Dynamics is smooth + has unique attractor | From A5 (admissibility) + smoothness | REQUIRED | NO |
| "Conley's theorem applies" | M is compact (or dynamics is bounded) | ASSUMED (regularity) | REQUIRED | NO (compactness is a regularity condition, not a physical conclusion) |
| "L exists" (Lyapunov function) | Conley (1978) | EXTERNAL THEOREM | REQUIRED | **PARTIALLY.** Conley guarantees a Lyapunov function exists, but this is a TOPOLOGICAL result, not a claim about geometry-coupling. The Lyapunov function L is not necessarily related to the metric. |

**Circularity check:** T2-min's conclusion (gradient-like flow with Lyapunov function) is weaker than the GRUT claim (relaxation toward GEOMETRIC equilibrium). The Lyapunov function L in Conley's theorem need not depend on the metric — it is a topological construct. T2-min does NOT pre-assume the conclusion. But it also does not REACH the conclusion: it proves gradient-like flow exists but does not prove the flow is toward a GEOMETRY-determined target.

### T2-mid

| Step | Import used | Import ID | Necessity | Pre-assumes conclusion? |
|------|-----------|:---------:|:---------:|:-----------------------:|
| "Lorentzian manifold" | Metric g_{μν} with (−,+,+,+) signature | IA-1 | REQUIRED | NO |
| "CTP action on curved background" | Schwinger-Keldysh formalism + gravity | IA-1 + CTP (from A4/A5 structure) | REQUIRED | NO |
| "3-diffeomorphism invariance" | Spatial diffs are symmetries | IA-7 (new) | REQUIRED | **PARTIALLY.** 3-diff invariance forces the time direction to be geometric. This is close to the conclusion — but it does not fix the FORM of the dissipative term, only its building blocks. |
| "Dissipative term must use n^μ, K, h" | Classification of 3-diff-invariant dissipative operators | Salcedo et al. (2025), classification lemma | EXTERNAL RESULT | **NO** (this is derived in the literature, not assumed) |
| "Simplest operator is n^μ ∂_μ Φ" | Derivative counting | Direct argument | REQUIRED | NO (simplicity argument, not uniqueness) |

**Circularity check:** IA-7 (3-diff invariance) imports the requirement that the time direction be geometric. This is a STRONG import — it effectively builds in the answer that dissipation must couple to geometry. However, IA-7 is WEAKER than the full conclusion: it says the dissipative operator's building blocks are geometric, not that the dynamics takes the specific relaxation form τ n^μ ∇_μ Φ + Φ = X. The gap between "building blocks are geometric" and "the equation is τ dΦ/dt + Φ = X(g)" is genuine and must be bridged by the proof.

**Assessment: borderline.** IA-7 is a strong import that does much of the work. The theorem is non-trivial beyond IA-7 only insofar as it constrains the FORM of the equation, not just its ingredients.

### T2-strong

| Step | Import used | Import ID | Necessity | Pre-assumes conclusion? |
|------|-----------|:---------:|:---------:|:-----------------------:|
| Full diff-invariance | Diff(M) symmetry | IA-8 (new) | REQUIRED | **YES — partially.** Full diff-invariance + scalar field + first-order dynamics very tightly constrains the equation. The conclusion almost follows from the classification of diff-invariant first-order scalar operators. |
| Decoherence (T1) | IA-2 + T1 result | E2-A | Used to justify CTP structure | NO (T1 is an independent result) |
| Entropy growth (T3) | IA-4 + IA-5 + IA-6 + T3 result | E2-A | Used to justify irreversibility | NO (T3 is independent) |
| "Unique first-order covariant scalar dissipative eq" | Classification of operators | Direct argument | REQUIRED | **NEAR-CIRCULAR.** If we assume first-order + scalar + covariant + dissipative + unique attractor, the space of allowed equations is very small. The relaxation form may be the ONLY member. But this "uniqueness" is a consequence of the heavy import stack, not of the primitives. |

**Circularity assessment for T2-strong:** The import stack (IA-1 + IA-2 + IA-6 + IA-7 + IA-8) is so heavy that the conclusion nearly follows from the imports by classification of operators. This is a VALID mathematical argument but it achieves necessity by importing enough constraints that only one equation survives — which is methodologically close to assuming the answer in pieces rather than deriving it from primitives.

---

## 3. T2 Proof/Impossibility Results

### T2-min: Gradient-like flow exists

```
CLAIM: A smooth dynamics on a compact manifold M with a unique global
attractor admits a Lyapunov function L with V·∇L ≤ 0.

RESULT: PROVEN (Conley, 1978).

But: The Lyapunov function L is topological, not geometric. L need not
depend on any metric. The result is REAL but DOES NOT reach the target
(geometry-coupling). It proves that irreversible dynamics has Lyapunov
structure, not that the Lyapunov function is curvature-related.

CLASSIFICATION: PROVEN but INSUFFICIENT for geometry-coupling.
Confidence: 0.95 (the theorem is standard; its insufficiency is clear).
```

**Countermodel for geometry-coupling (even with T2-min):**

Take M = [0,1] with the dynamics dx/dt = -(x - 0.5). The Lyapunov function is L = (x - 0.5)². The attractor is x* = 0.5. This dynamics has nothing to do with any geometry or curvature. The attractor is a constant, not a function of any metric. T2-min's Lyapunov theorem applies but produces no geometry-coupling.

### T2-mid: Dissipation couples to foliation geometry

```
CLAIM: 3-diff-invariant CTP dissipative action for a scalar field must
use geometric objects (n^μ, K_{μν}, h_{ij}) to define the time direction.

RESULT: CONDITIONALLY NECESSARY (under IA-1 + IA-7).

The argument: In a 3-diff-invariant theory, any scalar constructed from
the spatial metric h_{ij} is 3-diff-invariant. But a TIME derivative
(needed for dissipation) requires a choice of time. The only 3-diff-
invariant choices are:
  (a) n^μ ∇_μ Φ (proper-time derivative along the foliation normal)
  (b) u^μ ∇_μ Φ (derivative along a fluid velocity, if matter defines one)
Both are geometric objects. No NON-geometric time direction is 3-diff-
invariant (any externally imposed time vector would break 3-diffs).

This DOES constrain the dissipative operator to couple to geometry.

CLASSIFICATION: CONDITIONALLY NECESSARY (requires IA-1 + IA-7).
Confidence: 0.75.
```

**Countermodel attempt:** Can we have a 3-diff-invariant CTP action with a dissipative term that does NOT use n^μ or K?

The dissipative term must be linear in time derivatives (first-order) and a 3-scalar. The available building blocks are: n^μ (from the foliation), h_{ij} (spatial metric), K_{ij} (extrinsic curvature), and spatial covariant derivatives D_i. The only first-order time derivative available is n^μ ∇_μ Φ. There is no alternative.

**No countermodel found.** Within the 3-diff-invariant framework, the dissipative term MUST use the foliation geometry.

**BUT:** The conclusion (dissipation uses n^μ) follows almost directly from the definition of 3-diff invariance. The import IA-7 does most of the work. The theorem's content beyond the import is the CLASSIFICATION (enumerating what's allowed), not a deep derivation.

### T2-strong: Full relaxation form forced

```
CLAIM: The unique first-order, scalar, fully diff-invariant, dissipative
equation with a unique attractor is τ n^μ ∇_μ Φ + Φ = X(g).

RESULT: NEAR-CIRCULAR.

Analysis: Under full diff-invariance (IA-8):
- The LHS must be a scalar involving at most first time derivatives of Φ.
  The only option: τ n^μ ∇_μ Φ + f(Φ) for some function f.
- The unique-attractor condition requires f(Φ*) = 0 and f'(Φ*) > 0
  (stable fixed point). The simplest f: f(Φ) = Φ - X for some target X.
- X must be a scalar functional of g (covariance requires it).

The relaxation form follows. But it follows from an import stack
(IA-1 + IA-7 or IA-8 + first-order + scalar + unique attractor + covariance)
that is so constrained it leaves essentially one option.

CLASSIFICATION: CONDITIONALLY NECESSARY but NEAR-CIRCULAR.
The imports effectively specify the answer in pieces.
Confidence: 0.60 (mathematically valid but methodologically weak).
```

**Circularity assessment:** The T2-strong import stack can be decomposed:
- IA-1 (Lorentzian manifold) → provides geometric time direction
- IA-7/IA-8 (diff-invariance) → forces operator to use geometry
- First-order (overdamped) → eliminates □Φ and higher derivatives
- Scalar → eliminates vector/tensor equations
- Unique attractor → fixes the structure of f(Φ)
- Covariance of target → X = X(g)

Each import is INDIVIDUALLY non-circular. But COLLECTIVELY they leave no room. The relaxation form is the intersection of all constraints, not a consequence of deep structure. This is classification by elimination, not derivation from principle.

### Summary of T2 results

| Version | Result | Classification | Confidence | Countermodel? |
|---------|--------|:-:|:-:|:-:|
| T2-min | Lyapunov exists (Conley) | PROVEN but INSUFFICIENT | 0.95 | Yes (non-geometric Lyapunov) |
| T2-mid | Dissipation uses n^μ, K | CONDITIONALLY NECESSARY | 0.75 | None found (within IA-1+IA-7) |
| T2-strong | Full relaxation form forced | CONDITIONALLY NECESSARY but NEAR-CIRCULAR | 0.60 | None (but import stack nearly specifies answer) |

---

## 4. T5 Scope Update: Non-Uniqueness Pressure

### What T1 + T3 + T2 constrain (all conditional)

Collecting all E2 results:

| Constraint | Source | Import cost | What it constrains |
|-----------|--------|-------------|-------------------|
| Decoherence condition | T1 (AF-2b) | IA-2 (quantum probability) | Off-diagonal interference must vanish for consistent histories |
| Entropy growth | T3 | IA-4 + IA-5 + IA-6 | Dynamics must be mixing (R does not confine to low-entropy states) |
| Dissipation uses geometry | T2-mid | IA-1 + IA-7 | Time derivative is n^μ ∇_μ Φ, not external |
| Relaxation form | T2-strong | IA-1 + IA-7/8 + first-order + scalar + unique-attractor | τ n^μ ∇_μ Φ + Φ = X(g) |

### How large is the remaining dynamics class?

Even under ALL conditional constraints (T1 + T2-strong + T3), the following remain FREE:

| Free parameter/function | What it controls | Constrained by anything? |
|------------------------|-------------------|:-:|
| τ (scalar function on M) | Relaxation timescale | NO (bounded below by T4 if proven, but T4 is not ready) |
| X(g) (scalar functional of metric) | Equilibrium target | Constrained to be a scalar of g. But WHICH scalar? R, K, R_{μν}R^{μν}, etc. — infinite family. |
| D (noise coefficient) | Fluctuation strength | Fixed by FDT given τ and T. But T is free. |
| T (temperature) | Bath temperature | NO (environmental input) |
| Number of fields | One Φ? Two (Φ,Ψ)? More? | NO (nothing constrains the field content) |
| f(Φ) (the nonlinear force) | Shape of potential / attractor structure | Constrained to have at least one attractor. Could be linear, cubic, or anything else. |

### Class-size estimate

```
N = dim(dynamics class under all conditional T1+T2+T3 constraints)

τ: function on M → infinite-dimensional
X(g): functional of g → infinite-dimensional (space of scalar curvature invariants)
f(Φ): function ℝ→ℝ with at least one zero → infinite-dimensional
Field content: {Φ}, {Φ,Ψ}, {Φ,Ψ,χ}, ... → unbounded
T: function on M → infinite-dimensional

N = ∞ (EFFECTIVELY UNBOUNDED)
```

Even the strongest T2 result (T2-strong) leaves an INFINITE-DIMENSIONAL family of allowed dynamics. The constraints fix the FORM of the equation (τ n^μ ∇_μ Φ + Φ = X(g)) but not the CONTENT (what τ is, what X is, how many fields there are, what the nonlinearity is).

### What would reduce N?

| Reduction mechanism | What it would do | Available? |
|---|---|:-:|
| T4 (Bekenstein bound on τ) | Would bound τ from below by a geometric quantity | NOT READY (requires IA-3, very high risk) |
| Principle selecting X(g) | Would pick a specific curvature scalar for X | NONE KNOWN |
| Field-content constraint | Would fix the number and type of fields | NONE KNOWN |
| UV completion | Would fix parameters from a fundamental theory | OUTSIDE Program E scope |

**T5 verdict: N = ∞.** The conditional constraints from T1-T3 + T2-strong constrain the FORM but not the CONTENT of the dynamics. The class is infinite-dimensional. Non-uniqueness persists.

---

## 5. Structural Conclusion Memo

### Does P1-P5 force covariant irreversibility?

**NO.** P1-P5 alone do not even provide a manifold (AF-1a: abstract poset). Without IA-1, there is no metric, no covariance, and no concept of "covariant irreversibility." P1-P5 admit classical Markov chains on finite graphs (toy model M1 from E1), which have nothing to do with covariant irreversibility.

### Does P1-P5 + imports force it?

**CONDITIONALLY, under a heavy import stack.** With IA-1 (Lorentzian manifold) + IA-7 (3-diff invariance) + first-order + scalar + unique-attractor assumptions, the dissipative dynamics MUST couple to the foliation geometry and takes the relaxation form τ n^μ ∇_μ Φ + Φ = X(g). But this import stack is FIVE additional assumptions beyond P1-P5, each introducing significant model content.

### What this implies for exit tokens

The conditional results from T2 are REAL but EXPENSIVE. The price of each result is a corresponding import. The "necessity" emerges only because the imports leave no room for alternatives — which is classification by elimination, not derivation from deep principles.

**The honest structural conclusion:** The Program E primitives P1-P5 are a clean, model-independent starting point. But they are too weak to determine physics. Every step toward a specific dynamics (decoherence, entropy growth, covariant relaxation) requires importing physical content (quantum probability, mixing, manifold geometry, diffeomorphism invariance) that carries most of the answer within it. The theorems are VALID — the algebra is correct — but the explanatory force rests in the imports, not in the primitives.

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **E2B-G1** | T2 ladder defined with assumption hierarchy | **PASS** | T2-min (manifold only), T2-mid (+IA-1+IA-7), T2-strong (+full diffs+first-order+scalar+attractor). Three levels with explicit imports at each. |
| **E2B-G2** | Import ledger complete and auditable | **PASS** | Every proof step tagged with import ID, necessity, and circularity check. T2-strong flagged as near-circular. |
| **E2B-G3** | T2 classification issued | **PASS** | T2-min: proven but insufficient. T2-mid: conditionally necessary. T2-strong: conditionally necessary but near-circular. |
| **E2B-G4** | T5 class-size issued | **PASS** | N = ∞ (unbounded). Free: τ, X(g), f(Φ), field content, T. Nothing reduces N to finite without additional mechanisms not available in Program E. |
| **E2B-G5** | Exit-token impact updated | **PASS** | See below. |

### Exit-token update

| Token | Status | Reason |
|-------|:------:|--------|
| **necessity_emerges** | **NOT MET** | Zero unconditional proofs. All results conditional on imports. T5: N = ∞. |
| **conditional_necessity** | **MET (weakly)** | T1 (quantum branch) + T2-mid + T3 (with mixing) are all conditionally necessary. But each requires imports. And T5 shows N = ∞ even under all conditions. Conditional necessity of FORM is achieved. Conditional necessity of CONTENT is not. |
| **non_uniqueness_persists** | **MET** | T5: N = ∞. The constrained dynamics class is infinite-dimensional. The form τ n^μ ∇_μ Φ + Φ = X(g) is forced (conditionally) but τ, X, field content, and nonlinearity are unconstrained. |
| **blocked** | Not reached | T4 remains as a future target, though at very high risk. |

---

## Decision Token

### **non_uniqueness_persists_now**

**Rationale:**

1. The form of the dynamics (first-order scalar relaxation toward a geometry-determined target) is conditionally forced by the T2-mid/strong import stack. This is a REAL result.

2. But the CONTENT (what τ is, what X(g) is, how many fields, what nonlinearity) is unconstrained. N = ∞.

3. The conditional necessity of form + non-uniqueness of content means: Program E has found the SHAPE of the answer (relaxation-to-geometry) but not the SUBSTANCE (which relaxation, toward which geometry, at what rate).

4. This is EXACTLY the D2 finding at a deeper level: the GRUT ansatz (relaxation-to-geometry) is confirmed as the right CLASS of dynamics under the import stack, but it is not singled out as the unique member. GRUT is a specific point in an infinite-dimensional family.

5. The primitives P1-P5 alone cannot resolve the non-uniqueness. Additional physics (beyond any import so far considered) would be needed. The highest remaining target (T4, Bekenstein bound) could bound τ but requires importing conjectural quantum-gravity content (IA-3) — an even heavier cost.

**The program has reached a clean structural terminus.** The answer is: physical primitives + reasonable imports force the FORM (covariant relaxation-to-geometry) but not the CONTENT (parameters, field multiplicity, coupling specifics). Non-uniqueness persists at the content level. The GRUT ansatz is a valid member of the forced class but not a unique member.

---

*Program E Stage E2-B complete. Decision: non_uniqueness_persists_now. T2-min: Lyapunov exists (Conley, proven, but no geometry-coupling). T2-mid: dissipation uses geometric time (conditionally necessary under IA-1+IA-7). T2-strong: relaxation form forced (conditionally, near-circular under heavy imports). T5: N = ∞ (dynamics class is infinite-dimensional even under all conditional constraints). Exit tokens: conditional_necessity met weakly (form forced). non_uniqueness_persists met (content unconstrained). The primitives + imports force the shape but not the substance. GRUT is a valid but non-unique member of the forced class. Gates: 5/5 pass.*
