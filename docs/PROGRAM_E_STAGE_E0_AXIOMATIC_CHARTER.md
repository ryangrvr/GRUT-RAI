# Program E — Stage E0: Axiomatic Charter and Proof Targets

---

## 1. Program Identity

### Technical

Program E is an exploratory axiomatic investigation testing whether the GRUT constitutive ansatz F = X(g) − Φ (relaxation toward geometry-determined equilibrium) can be derived as a necessary consequence of a small set of physically motivated axioms, thereby elevating it from a specific EFT ansatz to a structurally constrained theory class. Program E inherits no claim of necessity, uniqueness, or ToE status from GRUT III. It starts from the D2 verdict (ansatz_persists) and the D1 verdict (generic_reconstruction_success) as given facts.

### Public-facing

Program E asks whether the structure of irreversible constitutive dynamics coupled to gravity is forced by basic physical principles, or is merely one choice among many. It is not a continuation of the GRUT effective field theory program (which is closed). It is a new investigation into whether the GRUT ansatz has deeper roots.

### Explicit separation from GRUT III

| Item | GRUT III status | Program E treatment |
|------|:-:|---|
| GRUT is a specific EFT ansatz | ESTABLISHED (D1, D3) | INHERITED as starting fact. Not contested. |
| Meta-principle is an ansatz | ESTABLISHED (D2) | The TARGET of E is to test this. If E fails, the D2 verdict stands. |
| USL is Newtonian gravity | ESTABLISHED (D1) | NOT reopened. Program E is about the constitutive sector, not the USL. |
| Parameters are free | ESTABLISHED (D2) | Program E tests whether axioms can constrain them. If not, D2 stands. |
| No ToE claim | FROZEN (F1) | Remains frozen. Program E cannot upgrade to ToE without meeting all exit criteria AND external validation. |

---

## 2. Axiom Candidate Scope

### Domain A: Consistency of histories

| Field | Content |
|-------|---------|
| **Why included** | The GRUT constitutive law selects a specific class of histories (relaxational, monotonically approaching equilibrium). An axiom requiring "consistent histories" in the decoherent-histories sense might constrain the allowed dynamics classes. |
| **Out of scope** | Full quantum-gravity decoherent-histories framework. Many-worlds interpretation. Interpretation-dependent claims. |
| **Minimal formal objects** | A space of histories H, a decoherence functional D[h, h'], a consistency condition D[h, h'] ≈ 0 for h ≠ h'. The constitutive law defines which histories are quasi-classical. |

### Domain B: Causality structure

| Field | Content |
|-------|---------|
| **Why included** | The constitutive law is strictly causal (retarded). Axiomatizing causality (no future-dependence, retarded propagator) might constrain the allowed force functions F(φ, g) to relaxation-type forms. |
| **Out of scope** | Causal set theory. Discrete spacetime. Non-standard causality. |
| **Minimal formal objects** | A causal ordering on spacetime. A retarded Green's function G_R. The requirement that F(φ, g) produces only retarded response. |

### Domain C: Global entropy / memory structure

| Field | Content |
|-------|---------|
| **Why included** | The constitutive law has a Lyapunov function V = (Φ − X)² that decreases monotonically (deterministic, constant X). This is an entropy-like structure. An axiom requiring global entropy increase might constrain F to relaxation forms. |
| **Out of scope** | Full non-equilibrium thermodynamic formalism. Information-theoretic entropy beyond Shannon/von Neumann. Black hole entropy. |
| **Minimal formal objects** | A Lyapunov functional V[Φ, X]. A monotonicity condition dV/dt ≤ 0. The constitutive law as the generator of V-decreasing flow. |

### Domain D: Information-theoretic constraints

| Field | Content |
|-------|---------|
| **Why included** | The constitutive law irreversibly erases information about initial conditions (the contraction e^{−t/τ}). An axiom about information loss rates or channel capacities might constrain the dynamics. |
| **Out of scope** | Quantum error correction. Holographic entanglement entropy (without derivation chain). Computational complexity bounds. |
| **Minimal formal objects** | A mutual information I(Φ_0; Φ_t) that decays with t. A channel capacity C(τ) determined by the relaxation time. The constitutive law as a lossy channel. |

### Domain E: Covariance–irreversibility compatibility

| Field | Content |
|-------|---------|
| **Why included** | General covariance (diffeomorphism invariance) and irreversibility (preferred time direction) are in tension. An axiom requiring their compatibility might constrain the allowed dissipative structures on curved spacetime. Recent work (Salcedo et al. 2025) on CTP gravity + dissipation addresses exactly this tension. |
| **Out of scope** | Full quantum gravity. String theory. Loop quantum gravity. Non-perturbative covariance proofs. |
| **Minimal formal objects** | A diffeomorphism-invariant CTP action. A dissipative term that breaks time-reversal but preserves spatial diffeomorphisms. The conditions under which this is consistent. |

---

## 3. Theorem Target List

### T1: Necessity of relaxation-to-geometry

```
ASSUMPTIONS:
  T1-A1. A scalar field Φ on a CTP contour with first-order dissipative dynamics.
  T1-A2. Φ couples to a background metric g through the CTP action.
  T1-A3. The dynamics admits a unique stable fixed point for each static g.
  T1-A4. A global Lyapunov functional V[Φ, g] exists with dV/dt ≤ 0.

CLAIM:
  The fixed point Φ* is necessarily a local scalar functional of g:
  Φ* = X[g], where X depends on g only through curvature scalars.

PROOF STANDARD: Full proof or explicit counterexample.

FALSIFICATION CONDITION:
  A counterexample: a system satisfying T1-A1..A4 where Φ* depends on
  non-geometric data (initial conditions, external fields, or topological
  data not encoded in local curvature scalars).
```

**Preliminary assessment:** T1-A3 (unique fixed point) + T1-A2 (coupling to g) generically give Φ* = Φ*(g) (D2 Candidate B showed this is trivially true). The non-trivial content is whether Φ* depends on g through LOCAL curvature scalars only (not through non-local geometric data). This is a genuine question. Counterexample candidate: Φ* could depend on the global topology (e.g., volume of a compact space), which is geometric but non-local.

### T2: Uniqueness of the relaxation dynamics class

```
ASSUMPTIONS:
  T2-A1. Φ satisfies a first-order dissipative ODE: T dΦ/dt = F(Φ, g).
  T2-A2. F has a unique, globally attracting fixed point Φ* = X(g) for each static g.
  T2-A3. The CTP action satisfies unitarity (U1-U3) and KMS symmetry.

CLAIM:
  F is necessarily of the form F = f(X(g) − Φ) for some monotone
  increasing function f with f(0) = 0, where X(g) is a scalar functional
  of g. That is: the dynamics is necessarily relaxation TOWARD a
  geometry-determined target, with the rate depending only on the
  deviation from that target.

PROOF STANDARD: Full proof or explicit counterexample showing an
  F satisfying T2-A1..A3 that is NOT of this form.

FALSIFICATION CONDITION:
  An F satisfying all assumptions but not of the form f(X − Φ).
  For example: F = a(g) Φ² − b(g) Φ + c(g) with a ≠ 0 (quadratic,
  not relaxation-to-target). Does this satisfy T2-A2 and T2-A3?
```

**Preliminary assessment:** T2-A2 (unique global attractor) constrains F heavily but does not force the f(X − Φ) form. A quadratic F can have a unique attractor (if the quadratic has one stable root) without being of the relaxation-to-target form. The KMS condition (T2-A3) constrains the fluctuations but not the deterministic force shape (per D2 Candidate A). Likely outcome: T2 FAILS (counterexample exists). The relaxation-to-target form is a SUBCLASS of the allowed dynamics, not the unique class.

### T3: Parameter-collapse possibility

```
ASSUMPTIONS:
  T3-A1. The constitutive law is τ dΦ/dt + Φ = β + αR (GRUT form).
  T3-A2. The CTP action satisfies U1-U3 and FDT.
  T3-A3. The semiclassical Einstein equation is self-consistent
         (perturbative backreaction of Φ on g).
  T3-A4. The effective cosmological constant Λ_eff = 4πGβ²/(τ²c²)
         matches the observed Λ_obs.

CLAIM:
  The matching condition T3-A4, combined with T3-A3, reduces the
  independent parameter set {τ, α, β} by at least one relation.

PROOF STANDARD: Explicit computation showing a derived relation
  among {τ, α, β}, or proof that no such relation exists beyond T3-A4.

FALSIFICATION CONDITION:
  Proof that T3-A3 imposes no constraint on {τ, α, β} beyond the
  trivially satisfiable perturbative condition |αR| << β.
```

**Preliminary assessment:** D2 Candidate C already showed the only relation is β/τ ~ Λ_obs^{1/2} (external matching). T3 asks whether the semiclassical self-consistency imposes additional internal relations (e.g., between α and τ). This requires the full perturbative backreaction computation (UD2-dependent). Possible but not guaranteed.

### T4: Entropy monotonicity forces relaxation form

```
ASSUMPTIONS:
  T4-A1. A scalar field Φ with first-order dynamics on a CTP contour.
  T4-A2. A global entropy functional S[Φ, g] exists with dS/dt ≥ 0
         (second law).
  T4-A3. S is local: S = ∫ s(Φ, ∂Φ, g) d³x for some entropy density s.
  T4-A4. S is maximized at a unique equilibrium Φ* for each g.

CLAIM:
  The dynamics is necessarily of gradient flow form:
  T dΦ/dt = −δF/δΦ where F = −T_env S is a free energy,
  and Φ* is the minimum of F.
  This is equivalent to the relaxation-to-equilibrium form.

PROOF STANDARD: Full proof or counterexample.

FALSIFICATION CONDITION:
  A dynamics satisfying T4-A1..A4 that is NOT gradient flow.
  For example: a rotational (non-gradient) vector field with
  the same fixed point and a Lyapunov function.
```

**Preliminary assessment:** This is the strongest theorem target. Gradient flow from a free energy IS the relaxation-to-target form (F = −δF/δΦ = −∂V/∂Φ where V = (Φ − X)²/2 gives F = X − Φ). If T4 is true, the GRUT constitutive form follows from entropy + locality + uniqueness. However: non-gradient systems CAN have Lyapunov functions (any dissipative system does, by Lyapunov's theorem). The converse — that Lyapunov implies gradient — is FALSE in general (rotational components are allowed). T4 likely FAILS unless additional constraints (like detailed balance or time-reversal in the noise sector) are imposed.

---

## 4. Exit-Token Criteria

| Token | Objective criteria | How measured |
|-------|-------------------|-------------|
| **necessity_emerges** | At least one of T1-T4 is PROVEN with full proof. The proof establishes that the GRUT constitutive form (or a class containing it) is the UNIQUE dynamics satisfying the stated axioms. The axioms are non-trivially constraining (rule out at least 50% of the generic D1 class by formal measure or explicit counterexample count). | Proof document with referee-grade rigor. Axiom non-triviality demonstrated by exhibiting excluded alternatives. |
| **conditional_necessity** | At least one of T1-T4 is proven CONDITIONALLY: the GRUT form follows IF additional physically motivated assumptions are added. The additional assumptions are stated explicitly and are not equivalent to postulating the GRUT form. | Proof document with explicit list of additional assumptions and a demonstration that they are weaker than the conclusion. |
| **ansatz_persists** | All of T1-T4 are either DISPROVEN (counterexample found) or SHOWN UNDECIDABLE within the stated axiom framework. No viable axiom candidate has been found that constrains the dynamics to the GRUT class. | Counterexamples for each failed theorem. Undecidability argument for any remaining theorem. |
| **blocked** | The program cannot proceed due to unresolvable technical or conceptual obstacles. No theorem target is addressable without importing new mathematical or physical machinery beyond the declared scope. | Explicit statement of the blocking obstacle and why it cannot be resolved within scope. |

---

## 5. Claim Policy

### Allowed claims during Program E

| # | Allowed | Conditions |
|---|---------|-----------|
| EA1 | "We are testing whether the GRUT constitutive form can be derived from axioms." | Must state that this is an investigation, not a result. |
| EA2 | "Theorem T_n is proven / disproven / open." | Must have proof or counterexample at referee grade. |
| EA3 | "Axiom set {A_n} is non-trivially constraining." | Must demonstrate by exhibiting excluded alternatives. |
| EA4 | "Program E has achieved conditional_necessity." | Only if the exit-token criteria are met in full. |
| EA5 | All GRUT-III established claims (E-F1..13). | Unchanged. Inherited read-only. |

### Forbidden claims during Program E

| # | Forbidden | Reason |
|---|-----------|--------|
| EF1 | "GRUT is a Theory of Everything." | F1 (perpetual, from GRUT-III). Not upgradeable without full necessity + uniqueness + UV completion + experimental confirmation. |
| EF2 | "The meta-principle is derived / necessary" BEFORE a theorem is proven. | D2 verdict (ansatz_persists) stands until overturned by proof. |
| EF3 | "The GRUT-III closure was premature / wrong." | The closure was correct given the evidence at that time. Program E is a NEW investigation, not a revision. |
| EF4 | "This axiom set is the only possible one." | Axiom non-uniqueness is inherent. State the chosen axioms and their motivation; do not claim uniqueness. |
| EF5 | "The proof is complete" without exhibiting excluded alternatives. | Non-triviality must be demonstrated, not asserted. |
| EF6 | Importing covariance or strong-field claims without explicit proof within the declared scope. | GRUT-III blacklist X1, X5 remain binding until explicitly superseded by proof. |

---

## 6. Stage Skeleton

| Stage | Intent | First gate |
|-------|--------|-----------|
| **E1** | Construct the minimal axiom set from Domain A-E that is non-trivially constraining. Test each axiom for independence and non-triviality. | E1-G1: At least one non-trivial axiom candidate identified and formally stated. |
| **E2** | Attempt necessity proofs for T1-T4 under the E1 axiom set. For each: produce proof, counterexample, or impossibility argument. | E2-G1: Each theorem target has a definitive result (proven / disproven / undecidable with explicit reason). |
| **E3** | If any necessity result from E2: test uniqueness by attempting to reconstruct the proven dynamics class from the D1 generic model. If the proven class is still generic: necessity is trivial. | E3-G1: Uniqueness pressure test completed with explicit generic/non-generic classification. |
| **E4** | If any non-trivial necessity + non-generic uniqueness from E2-E3: test whether the axiom set constrains {τ, α, β, D} beyond external matching. | E4-G1: Parameter-constraint result (collapse / no collapse) with explicit computation. |

**Total estimated stages: 4.** Each stage has a hard gate. Failure at any stage triggers the ansatz_persists exit token (unless the failure is itself informative and redirects to a modified theorem target).

---

## 7. Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **E0-G1** | Scope explicit and non-overlapping | **PASS** | Five axiom domains (A-E) with distinct formal objects. Out-of-scope items listed for each. No domain overlaps with another's formal objects. |
| **E0-G2** | Theorem targets formal and testable | **PASS** | T1-T4: each has assumptions, claim, proof standard, and falsification condition. Each is mathematically precise (not prose-only). T1 and T2 have preliminary assessments suggesting specific outcomes. |
| **E0-G3** | Exit-token criteria operational | **PASS** | Four tokens with objective criteria and measurement methods. No token requires subjective judgment. |
| **E0-G4** | Claim policy explicit and enforceable | **PASS** | 5 allowed claims (EA1-EA5) with conditions. 6 forbidden claims (EF1-EF6) with reasons. Enforceable: each forbidden claim has a specific test (e.g., EF2: "before a theorem is proven" — binary check). |
| **E0-G5** | Workplan executable without hidden assumptions | **PASS** | E1-E4 defined with one-line intents and first gates. No stage assumes the outcome of a prior stage. Each stage has an explicit failure mode (triggers ansatz_persists). |

## Decision Token

### **charter_frozen**

**Rationale:** All five gates pass. The charter defines scope, targets, criteria, policy, and workplan without importing new physics, inflating claims, or assuming outcomes. Program E can begin at Stage E1.

---

*Program E Stage E0 complete. Decision: charter_frozen. Four theorem targets (T1-T4). Five axiom domains (A-E). Four exit tokens with objective criteria. Six forbidden claims. Four stages (E1-E4). No ToE claim. No GRUT-III revision. The investigation begins at E1: axiom construction.*
