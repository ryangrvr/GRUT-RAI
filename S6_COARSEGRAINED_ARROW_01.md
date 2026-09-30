# S6-0 — COARSE-GRAINED ARROW 01 (formulation/audit gate only)

**STATUS: PRE-REGISTERED.**
- §§0–3 are frozen at the commit that introduces this file, **before any candidate measure is
  evaluated and before the O-6 records are re-inspected for this gate**.
- The audit (§4) and the assignment (§5) are appended later, in separate commits.

**Authority:** `L0_STRUCTURAL_DIAGNOSTIC_REVERSAL_OWNER_RULING_01.md` §§8-15 (Issue #2 comment
`5913714570`). **All candidate measures below are the ruling's own (§10); none is invented here.**

**Scope of this gate:**
- audit only;
- no physics run, no v4 exception, no RNG;
- no numerical evaluation of members;
- abstract symbolic reasoning only.

**Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Question

> **Can the already-declared conservative pinned-chain parent (O-6) exhibit a threshold-free,
> mathematically principled coarse-grained temporal arrow, even though band-edge memory destroys
> strict pointwise ordering?**

**Background:**
- **O-6 is FALSIFIED for its strict charter.** Band-edge memory gives infinitely many sign reversals.
- **S-6 is the question O-6 preserved:** whether a coarse-grained arrow survives.

**Interpretation fence (ruling §14).** A positive result means only:

> **net/integrated directional transport survives despite arbitrarily late microscopic backflow.**

It does not restore any of these:
- strict Lyapunov ordering;
- pointwise monotonicity;
- a fundamental thermodynamic arrow;
- O-6;
- the reversal hypothesis.

## §1 Definitions (frozen)

### 1.1 Parent and observables

**Parent.** The declared O-6 conservative pinned chain, with its declared split, its declared initial
ensemble and its declared temperature pairs. The audit locates and cites them.

**Observables.** The **declared** O-6 observables, which the audit locates:
- **J(t):** the signed energy/heat flux;
- **Ḋ(t):** the reduced relative-entropy derivative.

If either is not fully declared (definition, sign, and which subsystem it belongs to), the audit
reports it as undefined (ruling Q1).

### 1.2 Orientation (fixed before evaluation)

"Forward" is the direction fixed by the **declared initial hot/cold ordering**. Each observable is
oriented so that forward transport is positive:
- **J:** J > 0 means energy flows from the initially hotter subsystem to the initially colder one.
- **Ḋ:** the forward-oriented entropy observable is σ := −Ḋ. So σ > 0 means the reduced relative
  entropy is decreasing.

**Governing rules:**
- If the record's own sign convention differs, **the record's convention is translated into this
  orientation**; it is never re-chosen per result.
- If the record declares no hot/cold ordering for a member (for example, equal temperatures), that
  member has no orientation and is excluded, and the exclusion is reported.

### 1.3 Primary object: the recurrence-free N → ∞ limit

- **Primary object.** The recurrence-free N → ∞ object is the one the O-6 record declares (for
  example, the admitted L-N limit).
- **Finite-N guarded windows** may be used **only** as cross-checks, never as the definition (ruling
  Q4).
- **Missing object.** If no N → ∞ object is declared for J or Ḋ, the audit reports it (Q2).

### 1.4 Integrated quantities

For a forward-oriented observable f (f = J or f = σ):

| Symbol | Definition |
|---|---|
| X_f(T) | ∫₀ᵀ f dt |
| A_f(T) | ∫₀ᵀ \|f\| dt |
| f⁻ | max(−f, 0) |
| B_f(T) | ∫₀ᵀ f⁻ dt / A_f(T), defined when A_f(T) > 0 |
| X_f(∞), A_f(∞), B_f(∞) | the limits as T → ∞, **where they exist** |

**Identity (frozen):** B_f(T) < 1/2 ⟺ X_f(T) > 0.

### 1.5 Candidate criteria (from ruling §§10-11; each classified separately)

| # | Criterion | Statement |
|---|---|---|
| **K-1** | asymptotic dominance | B_f(∞) < 1/2, equivalently X_f(∞) > 0, given that A_f(∞) is finite and positive |
| **K-2** | no complete erasure | X_f(T) > 0 for all T > 0 (equivalently B_f(T) < 1/2 for all T > 0). This is the ruling's "cumulative progress never completely erased". |
| **K-3** | normalized drawdown | worst drawdown divided by net rise, compared with a chosen level. **It counts as threshold-free only if the audit derives the comparison level from an identity**, not from a chosen tolerance (ruling §10 D). |

Each of K-1, K-2 and K-3 is evaluated for **f = J** and for **f = σ**, and the two results are reported
separately. **Agreement between the heat measure and the entropy measure is not assumed.**

### 1.6 Criterion classes

Each (criterion, observable) pair is placed in exactly one class. Classes are checked in this order,
and the first that applies is assigned.

| Class | Definition |
|---|---|
| **UNDEF** | A load-bearing object is not declared. Examples: J or Ḋ undeclared; no orientation; no N → ∞ object; A_f(∞) infinite or zero, making B_f(∞) undefined. |
| **NEEDS-CG** | Defining the criterion needs an undeclared smoothing kernel, window, blocking scale or other coarse-graining (ruling Q3). |
| **ARBITRARY** | The criterion's truth condition contains a free tolerance or scale not fixed by an identity. |
| **DECIDED** | The criterion is threshold-free and needs no new coarse-graining, and its truth value **follows from accepted O-6 identities and asymptotics**, plus general facts that hold on the declared parent. Examples of such facts: energy conservation, absolute integrability of a declared tail, and the identity in 1.4. The value (TRUE/FALSE) is reported. **The independent verifier must confirm it.** |
| **EXECUTABLE** | The criterion is threshold-free and needs no new coarse-graining, but its truth value is **not** fixed by accepted identities. Settling it needs an exact analytic derivation or an exact finite-member evaluation, which is not performed at this gate (ruling Q7). |

### 1.7 Asymptotic audit (ruling §11; done before any classification)

**Question:** is the declared tail f(t) ~ t⁻³ × (oscillatory) **absolutely integrable**, and is A_f(∞)
therefore finite?

**If yes, the audit records the consequences** (abstract mathematics, not evaluation):
- the total late-time backflow is finite;
- B_f(∞) is well defined when A_f(∞) > 0;
- infinitely many sign reversals do **not** imply B_f(∞) = 1/2;
- K-1 reduces to the sign of the finite integrated imbalance X_f(∞).

**The audit also checks:**
- whether the early-time behaviour, including t → 0, keeps A_f finite;
- whether the tail exponent and form are actually declared for J and for σ, or only for one of them.

## §2 Per-object audit template (frozen)

Every answer carries a file:line citation; an uncited answer counts as undefined.
- **Q1–Q7** of ruling §12, answered in turn.
- **The declared forms of:**
  - J and Ḋ;
  - their signs and subsystems;
  - the initial ensemble and temperature pairs;
  - the N → ∞ object;
  - the tail asymptotics, with exponents and the declared prefactor structure;
  - any accepted identity involving ∫J or ∫Ḋ, such as energy balance or a relative-entropy identity.
- **Classification:** each (K, f) pair gets a class from 1.6, with its ground.

## §3 Frozen outcomes and mechanical rule

### 3.1 Outcomes (ruling §13, verbatim labels)

| # | Outcome | Predicate |
|---|---|---|
| O-1 | **PRINCIPLED-COARSE-ARROW-TEST-FOUND** | at least one (K, f) pair is EXECUTABLE |
| O-2 | **IDENTITY-DECIDED** | at least one (K, f) pair is DECIDED (value reported) |
| O-3 | **ONLY-ARBITRARY-THRESHOLDS** | every (K, f) pair that is not UNDEF is ARBITRARY |
| O-4 | **FORMULABLE-ONLY-WITH-NEW-COARSE-GRAINING** | no pair is EXECUTABLE or DECIDED, and at least one is NEEDS-CG |
| O-5 | **UNFORMULABLE** | every (K, f) pair is UNDEF |

### 3.2 Mechanical rule

1. **Primary terminal:** the first true predicate in the order O-1 … O-5 (the ruling's list order).
2. **Sub-labels:** every other true predicate. O-1 and O-2 can hold together, with some pairs decided
   and others executable. In that case every DECIDED value is reported as well.
3. **If O-1 is primary:** draft an S6-1 charter for the EXECUTABLE pair(s), and **HARD STOP before any
   run** (ruling §13).
4. **Otherwise:** HARD STOP for the owner.

### 3.3 Audit method (frozen)

- **Read-only.**
- **Two parallel auditors:**
  - **A** covers the O-6 declarations: parent, split, ensemble, J, Ḋ, signs, the N → ∞ object, the
    finite-N windows, and the preserved S-6 / O-6 review text on B and D.
  - **B** covers the asymptotics: the declared tail forms and exponents, absolute integrability,
    early-time behaviour, energy-balance or entropy identities, and the S5-1 derivation's spectral
    weights where O-6 relies on them.
- **One independent adversarial verifier** checks:
  - every DECIDED and EXECUTABLE classification;
  - every UNDEF claim;
  - the primary terminal.

### 3.4 Fences

**Not authorized:**
- an S6 run;
- S-4, S-7 or S-8;
- a new reversal diagnostic;
- S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

**No drawdown threshold is frozen** unless an identity derives it (1.5 K-3).

### 3.5 Prior expectations (disclosed; not evidence)

These are recalled from earlier gates, not taken from inspection at this gate.

**Expectation 1: the tail is absolutely integrable.**
- The t⁻³ oscillatory tail is absolutely integrable.
- So A_f(∞) is finite and B_f(∞) is well defined.
- Therefore the recurring reversals do not force B_∞ = 1/2.

**Expectation 2: K-1 for J may be DECIDED.**
- By energy conservation, X_J(∞) equals the net energy the initially hotter subsystem loses between
  t = 0 and its asymptotic state.
- If the record fixes that asymptotic state, for example as relaxation to the bath temperature in the
  L-N limit, then K-1 for J is DECIDED.
- The coupling-energy bookkeeping may complicate this, and so may whether the retained site
  thermalizes at all. S5-1 reported non-Markovian dissipation only at g = 1.

**Expectation 3: K-2 is likely EXECUTABLE, and K-3 may be ARBITRARY.**
- K-2 depends on the early-time signs, not only on the asymptotics.
- K-3 may be ARBITRARY unless "complete erasure" (K-2) is identified as its only principled form.

**Expectation 4: the entropy observable σ may differ from J.**

**Hence the expected terminal:** PRINCIPLED-COARSE-ARROW-TEST-FOUND, with sub-label IDENTITY-DECIDED.
This must be tested, not assumed.

## §4 Audit

*(appended after this pre-registration is committed)*

## §5 Mechanical assignment

*(appended after §4)*
