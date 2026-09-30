# S2-HB — HAMILTONIAN-BATH BOUNDARY 01 (audit/formulation only)

**STATUS: PRE-REGISTERED.** §§0–3 are frozen at the commit that introduces this file, **before any
candidate record is inspected**. The audit (§4) and the mechanical assignment (§5) are appended later
in separate commits.
- **Authority:** `S2_OWNER_RULING_03.md` §11 (Issue #2 comment `5909019588`).
- **What this gate is:** audit only. There is no physics run, no v4 exception, no RNG, no simulation
  and no numerical evaluation of declared members. **No new bath may be invented.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

## §0 Question

> **Can the C-B reduced stochastic response be reproduced by deterministic evolution on a larger
> state space whose hidden environmental degrees of freedom are randomized only at the initial
> time?**

**Target (frozen from S2-1; charter `227dd09` §§0–1):**
- **C-B:** dx = [−K_b x − 4βx^{∘3}]dt + B dW, with Q = BBᵀ = 2 diag(T_i), on the 23-site K_b.
- **Retained object O-1:** m₁(t; a) = 𝔼[x₁(t) | x(0) = a·e₁].
- **Frozen preparations:** a ∈ {±1/1000, ±1, ±3}.
- **Discriminating members:** β > 0 with a T₁ > 0 profile (F or GR(∞)). There,
  Δc₂ = −24βT₁a (accepted; ruling S2-03 §4).
- **Already excluded (S2-1):** the same state space ℝ²³ with a random initial condition only.

## §1 Definitions (frozen)

### 1.1 Candidate

A **candidate** is any construction in the record, or named by the owner (§3), in which the retained
C-B coordinates (or a declared parent of them) are embedded in a larger state space that evolves
deterministically.

### 1.2 HB-U: unrestricted deterministic enlargement

A candidate is **HB-U** when it is deterministic but fails at least one HB-P condition (1.3). The
typical cases are:
- the hidden state is (or is in bijection with) a driving path ω(·), evolved by a path-space shift;
- an abstract dilation (Sz.-Nagy/isometric/unitary, Koopman/KvN lift) whose enlarged dynamics is not
  a declared physical Hamiltonian with declared bath degrees of freedom.

**No-triviality rule (ruling §11.3), frozen:** a hidden variable equal to the whole Wiener trajectory,
evolved by the shift on path space, is **UNRESTRICTED-REALIZATION**. It is never HB-P, however the
shift is dressed (for example, as a "free field" whose only role is to carry ω).

### 1.3 HB-P: a physically constrained deterministic parent

A candidate is **HB-P-admissible** iff **all** of the following hold:

| # | Condition | Question |
|---|---|---|
| P-1 | The enlarged evolution is deterministic. | Q1 |
| P-2 | It is autonomous: the generator has no explicit time dependence. | Q2 |
| P-3 | It is **Hamiltonian/symplectic, or a declared conservative (unitary) parent**. A merely measure-preserving map or path shift fails. | Q3 |
| P-4 | Randomness is confined to the initial state of the environmental degrees of freedom. | Q4 |
| P-5 | The initial environmental law is independent of the preparation a. | Q5 |
| P-6 | The future forcing is **GENERATED-BY-DYNAMICS**, not **ENCODED-AS-DATA** (1.4). | Q8 |
| P-7 | The parent is **DECLARED** in the record: its Hamiltonian (system part, bath part, coupling) and its bath initial law are all written down there. It is not merely possible by a general theorem. | Q9 |
| P-8 | Its couplings are **local**, i.e. finite-range as declared: each coupling term involves finitely many declared sites or modes. | ruling §11.1 "local" |

**Q7** (infinitely many hidden degrees of freedom) is **recorded, not disqualifying.** A physical bath
may need a thermodynamic limit. Whether such a limit is declared/admitted is part of P-7 and of 1.6.

### 1.4 Encoding versus generation (Q8), frozen

In any deterministic bath, the initial bath state determines the future force. That alone is **not**
encoding.

- **ENCODED-AS-DATA:** the hidden initial datum *is* the force/noise path, or is chosen as a function
  of the target path. The dynamics does no work beyond reading it out; a shift is the canonical case.
- **GENERATED-BY-DYNAMICS:** the force is the output of a declared Hamiltonian flow on declared bath
  coordinates. Their initial law is a declared state (for example, Gibbs/KMS at declared T) that is
  fixed before, and independently of, any target path.
- **N/A:** the candidate has no forcing channel.

### 1.5 Reproduction scope (Q6), frozen ladder

For a candidate, compare its reduced retained response with C-B O-1 on a discriminating member (§0).

| Level | Meaning |
|---|---|
| **R-FULL** | The reduced law of the retained x (finite-dimensional distributions) equals the C-B law. |
| **R-MAP** | The reduced m₁(t; a) equals the C-B m₁(t; a) for **all** frozen a on some 0 ≤ t < ε. |
| **R-DISC** | The reduced m₁ matches the C-B Taylor germ through t², **including Δc₂ = −24βT₁a** with β > 0. This is the minimum that reaches the S2-1 discriminator. |
| **R-2** | Only linear/Gaussian second-order objects match: covariances, linear response, the S-1 tested objects. There is no nonlinear-drift content. |
| **NONE** | Not even R-2, or the retained object is not identified. |

Higher implies lower: R-FULL ⇒ R-MAP ⇒ R-DISC. R-2 is the separate linear class.

**Retained-variable identification is part of the scope.** The candidate's retained coordinate must be
identified with the C-B x through a **declared** reduction, map or limit. If the declared reduction
produces a different class of law (for example, underdamped instead of the first-order C-B law), the
level is read on that declared reduction as it stands.

### 1.6 Limits

A reproduction may be exact, or it may hold in a limit. **A limit counts only if it is already declared
and admitted in the record.**
- The limits the owner has ruled **not admitted** (L-WB and L-OD; ruling S5 pre-freeze, comment
  `5904251680`; S5-WB/S5-OD not opened, comment `5904495463`) do **not** count.
- A candidate that would reach R-DISC or higher **only** through a not-admitted limit gets the
  sub-label **BLOCKED-BY-NOT-ADMITTED-LIMIT**. It is reported for the owner and does not satisfy any
  outcome predicate.

### 1.7 Status of a construction (Q9)

| Status | Meaning |
|---|---|
| **DECLARED** | Written in a committed record with its ingredients. |
| **GENERAL-THEOREM-ONLY** | Available only from a standard theorem cited or statable without new structure. Examples: canonical Wiener-shift realization; strong-solution maps; Sz.-Nagy dilation. |
| **ABSENT** | Neither. |

A GENERAL-THEOREM-ONLY construction may support HB-U. **It can never support HB-P** (P-7).

## §2 Per-candidate record (frozen template)

For each candidate the audit reports:
- **Q1–Q9**, with file:line citations;
- **P-1 … P-8**, each as pass, fail or undefined;
- **HB class:** HB-P-admissible, HB-U, or NOT-AN-ENLARGEMENT;
- **scope level (1.5);**
- **limit status (1.6);**
- **"formulable":** whether the declared structure alone fixes an exact executable test of R-DISC or
  R-MAP (§3.2 O-2).

## §3 Frozen outcomes and mechanical rule

### 3.1 Candidate scope

**The owner's eight targets (ruling §11.2):**
1. the S-1 Hamiltonian-bath / Gaussian realization;
2. O-6 conservative-chain results;
3. S5-1 conservative-origin results;
4. Sz.-Nagy / conservative dilation records;
5. Koopman/KvN realizations;
6. L0-1e stochastic extension;
7. CTP / influence-functional records;
8. declared FDT/KMS structures.

**Plus a discovery sweep.** It covers any committed record that self-declares a Hamiltonian,
conservative or bath parent for noise. Found records are listed as candidates, and none is invented.

**Records that are not candidates** are listed with the reason. For example, a record that states a
fluctuation-dissipation relation but declares no parent is NOT-AN-ENLARGEMENT and is recorded as
contributing structure only.

### 3.2 Outcome predicates

| # | Outcome | Predicate |
|---|---|---|
| O-1 | **PHYSICAL-BATH-ALREADY-REALIZES** | Some HB-P-admissible candidate has R-FULL or R-MAP for C-B on a discriminating member, **established in the record**, exactly or through an admitted limit. |
| O-2 | **FORMULABLE-PHYSICAL-BATH-TEST** | No proof as in O-1 exists, but some HB-P-admissible candidate is **formulable**: its declared system part, coupling, bath law and reduction/limit all come from the record and admitted limits. Together they fix an exact executable test of R-DISC or R-MAP against C-B with **no new ingredient**. |
| O-3 | **UNRESTRICTED-REALIZATION-ONLY** | A deterministic enlargement reaching R-MAP or R-FULL for C-B exists (DECLARED or GENERAL-THEOREM-ONLY), but only as HB-U. |
| O-4 | **SECOND-ORDER-ONLY** | Some HB-P-admissible declared bath reaches R-2, but none reaches R-DISC, and none is formulable for it. |
| O-5 | **NO-PHYSICAL-BATH-CANDIDATE** | No HB-P-admissible candidate exists. Every declared conservative/Hamiltonian parent fails P-1 … P-8, or cannot formulate the C-B test without new structure. |
| O-6 | **UNFORMULABLE** | The comparison itself is undefined from the record. For example, no candidate's retained object can be put against O-1 at all, or a load-bearing predicate is undefined for every candidate. |

**Composition rule (disclosed choice DC-1).** Composing a declared bath with the C-B system through a
coupling that the record does **not** declare counts as **new structure**. Such a composition is not
formulable under O-2. The audit reports it as the sub-label **FORMULABLE-ONLY-WITH-NEW-COUPLING**.
The owner may overrule DC-1. If so, the audit's sub-labels already contain what is needed to re-read
the outcome, with no new inspection.

### 3.3 Mechanical rule

1. The primary terminal is the **first true predicate in the order O-1 … O-6** (the owner's list
   order).
2. **Every other true predicate is reported as a sub-label.** This matters because O-3 and O-4 (or O-3
   and O-5) can hold together.
3. Also reported as sub-labels when they occur: **BLOCKED-BY-NOT-ADMITTED-LIMIT** and
   **FORMULABLE-ONLY-WITH-NEW-COUPLING**.
4. The terminal is proposed for owner adjudication. **HARD STOP.**

### 3.4 Audit method (frozen)

- **Read-only.** There are no code runs on members. Abstract symbolic reasoning only; no RNG.
- **Two parallel read-only auditors:**
  - one over targets 1–3 and 6;
  - one over targets 4, 5, 7 and 8 plus the discovery sweep.
- **One independent adversarial verifier** for load-bearing classifications: every
  HB-P-admissible/formulable claim, and the primary-terminal predicate.
- **Citations:** every Q/P answer cites file:line. An uncited answer counts as **undefined**.

### 3.5 Fences

The result, whatever it is, does **not** establish:
- primitive/ontological noise;
- that no physical bath could exist (only that none is declared or formulable at this scope);
- quantum outcomes, Born probabilities or collapse;
- a derived L0-1c drift.

**O-2, if assigned, authorizes nothing.** A test run needs a separate ruling.

### 3.6 Prior expectations (disclosed before inspection; not evidence)

**Expectations from memory of earlier gates, not from inspection at this gate:**
- The S-1 Hamiltonian-bath (FKM-type) realization reaches only the linear/Gaussian R-2 class.
- Path-space/Wiener-shift and Sz.-Nagy/Koopman constructions are HB-U.
- The S5-1 conservative parent derives an underdamped Markov law, and reaching the first-order C-B law
  would need the not-admitted wide-band/overdamped limits.

**Hence the expected outcome** is UNRESTRICTED-REALIZATION-ONLY, with sub-labels SECOND-ORDER-ONLY and
possibly BLOCKED-BY-NOT-ADMITTED-LIMIT and FORMULABLE-ONLY-WITH-NEW-COUPLING. This expectation must be
tested, not assumed. The audit must look for, and report, any record that contradicts it.

## §4 Audit

*(appended after this pre-registration is committed)*

## §5 Mechanical assignment

*(appended after §4)*
