# S2-HB — HAMILTONIAN-BATH BOUNDARY 01 (audit/formulation only)

> **ACCEPTED (owner ruling S2-HB-02, Issue #2 comment `5909652190`; `S2_HB_OWNER_RULING_02.md`):**
> - **S2-HB = UNRESTRICTED-REALIZATION-ONLY**, with sub-label **NO-PHYSICAL-BATH-CANDIDATE**.
> - **FORMULABLE-ONLY-WITH-NEW-COUPLING** is report-only, with a fence: the coupling is *necessary, not
>   sufficient*.
> - Rulings on the open items:
>   - **A-1:** a latent taxonomy gap; inactive here.
>   - **A-1a:** O-6 fails P-4.
>   - **A-1b:** S5-1 C₀ fails P-6.
>   - **A-2:** R-2 means the β = 0 control class (a wording clarification).
>   - **A-4:** reporting only.
> - **SECOND-ORDER-ONLY = FALSE** and **BLOCKED-BY-NOT-ADMITTED-LIMIT** is not assigned.
> - **No rescue bath.** The S-2 chain is closed; see `S2_NOISE_ORIGIN_DEPOSIT_02.md`.
>
> The text below is preserved as filed.

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

**How the audit was run.** §§0–3 were frozen at `0942dbd` before any candidate was inspected.
- **Auditors:** two read-only auditors, per §3.4. Auditor A covered targets 1–3 and 6; auditor B covered
  targets 4, 5, 7 and 8 plus the discovery sweep.
- **Verifier:** one independent adversarial verifier, on claims C1–C5. **All five are confirmed**, with
  one correction to auditor A (§4.3).
  - After the interim ruling was relayed, the verifier re-assessed C4 under the narrow O-5 reading. It
    found that the HB-P/scope-NONE gap (A-1) is real if O-6 or S5-1 were HB-P-admissible.
  - The primary terminal is unchanged.
- **Mid-audit ruling:** `S2_HB_OWNER_RULING_01.md` (comment `5909260267`, recorded at `d1ba71d`)
  confirms DC-1 and reads O-5 narrowly. It amends nothing in §§0–3.
- **Discipline:** no files were changed by the auditors, and no code was run on members. Only abstract
  symbolic reasoning was used; no RNG.

### 4.1 Per-candidate table (§2 template)

Key to the P-string: P = pass, F = fail, U = undefined, V = vacuous, N/A = no forcing channel (counts as
fail for P-6).

| Candidate (status, Q9) | Q1/Q2/Q3 | Q4 / Q5 | Q6 scope vs C-B | Q7 | Q8 | P-1…P-8 | HB class | Limit | Formulable |
|---|---|---|---|---|---|---|---|---|---|
| **W. C-B Wiener-shift skew product** Θ_t(x, ω) = (φ(t, ω)x, θ_tω). **GENERAL-THEOREM-ONLY**; no declared equivalent anywhere (verifier C1). | yes / yes (on the skew product) / **measure-preserving semiflow, not symplectic** | yes (ω ~ Wiener) / yes | **R-FULL**, exact | yes (path space) | **ENCODED-AS-DATA** | P P F P P F F U | **HB-U** (no-triviality rule, 1.2) | none needed | n/a |
| **1. S-1 FKM-type Hamiltonian bath** (`L0_1_FLOOR_SUCCESSOR_LIST.md:11`; `L0_1E_PREFREEZE_REVIEW_01.md:58-60`). **GENERAL-THEOREM-ONLY**: no H, coupling, spectral density or bath law is written (`L0_ACCESS_BRIDGE_01.md:166`; "NONUNIQUE", `L0_LIFT_SELECTION_01.md:42`). | yes / U / Hamiltonian by name | yes / yes | **R-2 at most, linear drift only.** Exactness is NOT-ESTABLISHED: a finite bath cannot do it; it holds only "as the mean response in an infinite Ohmic overdamped limit" (`L0_LIFT_SELECTION_VERIFICATION_01.md:39`; `L0_LIFT_SELECTION_CORRECTIONS_01.md:13,31`). | yes | U (flow undeclared) | P U P P P U F U | **HB-U** (1.7: GENERAL-THEOREM-ONLY never supports HB-P) | its R-2 content needs the L-OD/L-WB-type limit; R-DISC is unreachable in any limit (linear) | no |
| **2. O-6 harmonic chain** 𝒦_N (`L0_1G_CHARTER_01.md:45-65`). **DECLARED.** | yes / yes / **Hamiltonian**, H = ½\|p\|² + ½qᵀK_N q | **No**: the declared initial ensemble randomizes the **system** too: ⟨q₁²⟩ = T_s/K₁₁, ⟨p₁²⟩ = T_s (`L0_1G_CHARTER_01.md:54-58`). There is no preparation a. | **NONE**: second-order/underdamped; φ′(0) = 0 (`S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md:61-66,113-119`) vs C-B m₁′(0) = −K₁₁a − 4βa³ ≠ 0; harmonic only, "No anharmonic" (`L0_1G_CHARTER_01.md:152-153`) | N ∈ {23, 47, 95}; L-N admitted | GENERATED-BY-DYNAMICS | P P P **F** U P P P | **not HB-P-admissible as declared** (P-4) | no route to R-DISC in any limit (β absent) | no; also FORMULABLE-ONLY-WITH-NEW-COUPLING (§4.2) |
| **3. S5-1 conservative origin** (same parent, `S5_CONSERVATIVE_ORIGIN_01.md:30-44`). **DECLARED.** | yes / yes / Hamiltonian | none at all: C₀ is the bath at rest, and "the Gibbs product is report-only" (`S5_CONSERVATIVE_ORIGIN_01.md:43`) / V | **NONE**: no exact semigroup; L-N gives non-Markovian dissipation; L-vH is underdamped, with no first-order law for q₁ (derivation:54-66, 224-240; verdict:87-98) | N → ∞ (L-N) | **N/A** (no noise term, derivation:123-132) | P P P V V **F** P P | **not HB-P-admissible** (P-6) | L-WB/L-OD not admitted (`S5_OWNER_RULING_02.md:39-42`), and not shown necessary or sufficient (`S5_OWNER_RULING_03.md:104-111`) | no |
| **4. Sz.-Nagy / unitary dilation of e^{−K_b t}** (`L0_LIFT_SELECTION_01.md:42`; `L0_LIFT_SELECTION_VERIFICATION_01.md:40,111-115`). A dilation of the *deterministic* linear flow, not of C-B. **GENERAL-THEOREM-ONLY.** | yes / yes / unitary, abstract | vacuous / yes | NONE on β > 0 (a linear-only no-go, `L0_LIFT_SELECTION_VERIFICATION_01.md:47-49`) | yes | N/A | P P P U P F F U | HB-U | — | no |
| **5a. Koopman Λ-K** (`L0_LIFT_SELECTION_01.md:40`; `L0_ACCESS_BRIDGE_CORRECTIONS_01.md:67-69`). Representational. | yes / yes / composition operator | ensemble only / yes | NONE: it reproduces the deterministic law (`L0_LIFT_SELECTION_VERIFICATION_01.md:35`) | function space | N/A | P P F U P F F U | HB-U | — | no |
| **5b. KvN** (`L0_ACCESS_BRIDGE_CORRECTIONS_01.md:66,102-110`; `L0_LIFT_SELECTION_VERIFICATION_01.md:36`). Representational. | yes / yes / unitary, representational | \|ψ\|² / yes | NONE: deterministic flow in the δ-limit, and the HT-B class otherwise | yes | N/A | P P P U P F F U | HB-U | — | no |
| **5c. Cotangent lift H = pᵀf** (`L0_LIFT_SELECTION_VERIFICATION_01.md:37`; `L0_ACCESS_BRIDGE_VERIFICATION_01.md:107`). Nonlinear, first-order. | yes / yes / canonical, indefinite | p₀ "any", never reaches x / yes | **NONE on discriminating members.** The x-projection is closed, so this is the same-state-space class that **HT-B already excludes** (Δc₂ = 0). It matches the linear response at β = 0 only. | no | N/A | P P P P P F F P | HB-U (P-6, P-7) | — | no |
| **6. L0-1e** (`L0_1E_CHARTER_01.md:59-70`) | **not deterministic**: primitive SDE; "the deleted axiom is determinism" | — | it *is* the β = 0 target member | — | — | — | **NOT-AN-ENLARGEMENT** (structure: Q = 2 diag(Tᵢ)) | — | — |
| **7. CTP / S_IF** (`S_IF.md:16-24,30`; `CHARTER.md:67`) | influence action only; the system is h_μν, not C-B x; the bath is "integrated out and NOT specified" | — | — | — | — | — | **NOT-AN-ENLARGEMENT** | — | no (no bath, no coupling) |
| **8. FDT/KMS structures** (`L0_1E_THEOREM_01.md:68-78`; `P2_INFLUENCE_CONE_VERDICT_01.md:34`; `S5_GENERATOR_ORIGIN_01.md:280`; `XI_STOCHASTIC_CHARTER_01.md:15-31`) | relations/states only | — | — | — | — | — | **NOT-AN-ENLARGEMENT** | — | — |
| Real Λ-B OU semigroup; complex quasi-free Λ-B/Λ-F (`L0_LIFT_SELECTION_VERIFICATION_01.md:47-49,97-99`) | Markov / CP semigroups, not deterministic enlargements; linear; cannot reach β > 0 | — | — | — | — | — | NOT-AN-ENLARGEMENT | — | — |

**Discovery sweep: declared Hamiltonian baths whose system is not C-B.** None of these is a candidate
under 1.1.
- **D-1 worlds W-A/W-D:** one oscillator plus 8 modes (`DISCRIMINATOR_CHARTER_01.md:21-40`).
- **3-spin bath:** `P3_NC_LIFT_VERDICT_01.md:14`.
- **Independent-boson dephasing:** `ARROW_OF_TIME.md:36`.
- **Free-scalar graviton-probe bath:** `PHYSICS_LEDGER/WALL_A_A3_DECLARATIONS.md:115-133`.

Each would need a new C-B system part and a new coupling (DC-1: FORMULABLE-ONLY-WITH-NEW-COUPLING).

**Naming artefact:** "bath block K_b" means C-B's own sites, not an environment.

**Record answer to ruling §11.1** ("does the record already contain an equivalent dilation/path-space
statement?"): **No.** Every dilation, Koopman or KvN record lifts the *deterministic* flow. The C-B
path-space realization is GENERAL-THEOREM-ONLY.

### 4.2 Verified load-bearing findings

**C1: HB-U exists, by general theorem only (CONFIRMED).**
- Because the noise is additive, y = x − Bω solves ẏ = f(y + Bω).
- f is one-sided Lipschitz: ⟨f(x) − f(y), x − y⟩ ≤ −λ_min|x − y|², with λ_min(K_b) ≥ 3/10 by
  Gershgorin, since (a³ − b³)(a − b) ≥ 0 and β ≥ 0.
- It is also coercive. So solutions are global for **every** continuous ω, and φ is a perfect cocycle
  under the increment shift. Θ is therefore a deterministic, autonomous semiflow.
- Pathwise uniqueness gives uniqueness in law, so the finite-dimensional distributions equal the C-B
  law: **R-FULL**. Degenerate Q (T₁ = 0 in G(∞); T₂₃ = 0 in GR(∞)) does not matter.
- Θ preserves μ⊗P for the stationary μ, and is **not invertible and not symplectic**: the cubic drift
  blows up backwards, and the fibre is 23-dimensional (odd) and volume-contracting.
- It is exactly the no-triviality case. **HB-U / UNRESTRICTED-REALIZATION.**

**C2: No HB-P parent for C-B is formulable (CONFIRMED).**
- **No declared bath parent has the nonlinear β > 0 system part.** The strongest near-miss is the
  anharmonic βq⁴ chain (`L0_1_NECESSITY_SWEEP_DESIGN_01.md:121-122`). It was realized only as the
  **first-order gradient flow**, with "second-order (Newtonian) dynamics … out of scope"
  (`L0_1C_CHARTER_01.md:67-75`). It has no bath, coupling or bath law.
- **No declared reduction gives a first-order x-law** except through the not-admitted
  Ohmic/overdamped limit.
- **The O-6 "bath" at N = 23 is C-B's own sites 2…23** (K₂₃ = K_b). It is a second-order version of the
  same sites, not extra environment.
- **Missing structure (verifier defect note 3):**
  - A C-B test from the record would need a new system–bath coupling (DC-1).
  - The natural Zwanzig-type route would also need:
    - a new second-order system part (momenta, H = ½|p|² + V);
    - a new spectral density;
    - the not-admitted L-WB and L-OD limits.

  The sub-label below names only the coupling. **The fuller list is stated here for the owner.**

**C3: SECOND-ORDER-ONLY is false (CONFIRMED).**
- **Response.** The O-6 retained linear response is φ(t) with φ′(0) = 0. C-B at β = 0 has
  m₁′(0) = −K₁₁a.
- **Covariance attack (fails).** The q-marginal of O-6's *global* Gibbs state at T = 1 equals C-B's
  F-profile Σ = K_b⁻¹ at β = 0.
  - But global Gibbs is only the L2 reference (`L0_1G_CHARTER_01.md:87`), not the declared initial law.
  - The declared product law is block-diagonal, with 1/K₁₁ < (K⁻¹)₁₁. It never relaxes at finite N.
  - The two-time correlations differ: cos(√K τ)K⁻¹ vs e^{−Kτ}K⁻¹.
  - It fails on GR(∞) and at β > 0.
  - No q ↔ x identification is declared (`S5_CONSERVATIVE_ORIGIN_01.md:68-72`).

  **Scope NONE under every reading.**
- **S-1 FKM** reaches R-2 only in a not-admitted limit, and it is HB-U anyway (P-7).
- **The cotangent lift** matches the β = 0 linear response, but it is HB-U (P-6, P-7).
- **No HB-P-admissible bath reaching R-2 exists.** The §3.6 prior sub-label is **refuted.**

### 4.3 Correction to auditor A (verifier; checked against the record)

Auditor A passed O-6 on P-4. **The record says otherwise.** The declared O-6 initial ensemble is "a
zero-mean Gaussian product of the uncoupled Gibbs states", and it includes the **system**:
⟨q₁²⟩ = T_s/K₁₁ and ⟨p₁²⟩ = T_s (`L0_1G_CHARTER_01.md:54-58`).

So randomness is **not** confined to the environment, and there is no preparation a. **P-4 fails for
O-6 as declared.** The S5-1 variant (bath at rest, C₀) has no randomness and no forcing channel, so P-6
fails (N/A).

An (a, 0)-system / Gibbs-bath hybrid would make P-4 pass. **That hybrid is not declared.** Adopting it
would be new structure.

### 4.4 Ambiguities reported for adjudication (not repaired, per interim ruling §3)

| # | Ambiguity | Effect here |
|---|---|---|
| **A-1** | **An HB-P / scope-NONE gap.** Suppose O-6 or S5-1 were HB-P-admissible. Both have scope **NONE** against C-B (the verifier found no defensible R-2 reading, and identification is a scope matter, not a candidacy matter, under 1.1/1.5). Then O-4 is false (no R-2), O-5 is false under the narrow reading (a candidate exists), and O-6 is false. **No frozen predicate covers "HB-P-admissible but reaches NONE".** | The **primary terminal is unaffected** (O-3 precedes both). Only the O-5 sub-label depends on it. |
| **A-1a** | **P-4 edge case.** O-6's declared product law randomizes the system momentum p₁ (⟨p₁²⟩ = T_s) even after conditioning on q₁(0) = a. **The audit reads this literally as a P-4 failure**: the randomness is not confined to the environment. | If the owner rules otherwise, O-6 enters A-1. |
| **A-1b** | **P-6 N/A case.** S5-1 (C₀, bath at rest) has no randomness, so P-4 is vacuous, and it has no forcing channel, so P-6 is N/A. **The audit reads N/A as a P-6 failure**: P-6 requires the forcing to be GENERATED-BY-DYNAMICS, and a candidate with no forcing does not satisfy it. The frozen text does not say this explicitly. | If the owner rules N/A as a pass, S5-1 enters A-1. |
| **A-2** | **R-2 is not anchored to a member.** 1.5 says "on a discriminating member" (β > 0), but R-2's objects are β = 0 objects. | None: no HB-P-admissible candidate reaches R-2 under either reading. |
| **A-3** | **O-5's two sentences disagree.** | The interim ruling resolves this narrowly ("no HB-P-admissible candidate at all"). Applied here, O-5 is true on the §4.3 ground: none of the declared parents is HB-P-admissible. |
| **A-4** | **The FORMULABLE-ONLY-WITH-NEW-COUPLING label understates the missing structure.** It lists only a coupling, while the route also needs a new second-order system part, a new spectral density and not-admitted limits (§4.2 C2). BLOCKED-BY-NOT-ADMITTED-LIMIT cannot record limits that a non-record construction would need. | Reporting only. |

## §5 Mechanical assignment (§3.3; interim ruling 01 applied)

| Predicate | Value | Ground |
|---|---|---|
| O-1 PHYSICAL-BATH-ALREADY-REALIZES | **false** | No HB-P-admissible candidate reaches R-MAP/R-FULL in the record. |
| O-2 FORMULABLE-PHYSICAL-BATH-TEST | **false** | No HB-P-admissible candidate. Every route needs an undeclared coupling (DC-1, confirmed) and a new nonlinear second-order system part. |
| **O-3 UNRESTRICTED-REALIZATION-ONLY** | **true** | The C-B Wiener-shift skew product: GENERAL-THEOREM-ONLY, R-FULL, HB-U. The only realizations are path-space/dilation. |
| O-4 SECOND-ORDER-ONLY | **false** | No HB-P-admissible declared bath reaches R-2 against C-B (§4.2 C3, §4.3). |
| O-5 NO-PHYSICAL-BATH-CANDIDATE | **true** (narrow reading) | As declared, O-6 fails P-4 (A-1a) and S5-1 fails P-6 (A-1b). S-1 FKM, Sz.-Nagy, Koopman, KvN and the cotangent lift are HB-U. The off-scope quantum baths are not C-B candidates. **Conditional on A-1a/A-1b.** If either is ruled the other way, O-5 is false and the A-1 gap is live. |
| O-6 UNFORMULABLE | **false** | The comparison is defined. |

**Sub-labels:**
- **NO-PHYSICAL-BATH-CANDIDATE** (true on the literal P-4/P-6 readings; conditional on A-1a/A-1b);
- **FORMULABLE-ONLY-WITH-NEW-COUPLING**, for the off-scope declared baths and for O-6/S5-1. Per A-4, it
  would also need a new anharmonic second-order system part.

**Not assigned:**
- **BLOCKED-BY-NOT-ADMITTED-LIMIT:** no candidate would reach R-DISC even through L-WB/L-OD.
- **SECOND-ORDER-ONLY.**

> **S2-HB = UNRESTRICTED-REALIZATION-ONLY** (proposed, mechanical), with sub-label
> **NO-PHYSICAL-BATH-CANDIDATE** and sub-label **FORMULABLE-ONLY-WITH-NEW-COUPLING**.

In the three categories of interim ruling §4:
1. **HB-U exact realization: exists**, by general theorem only; it is not declared in the record.
2. **HB-P R-2 realization: does not exist in the record.** The S-1 FKM bath is general-theorem-only.
   The declared O-6 chain randomizes the system and does not match even the linear C-B response.
3. **HB-P C-B candidate: does not exist.**

**Prior expectation (§3.6):**
- The primary terminal is **confirmed**.
- The SECOND-ORDER-ONLY sub-label is **refuted**.
- BLOCKED-BY-NOT-ADMITTED-LIMIT is **not supported**.

**Reading (fenced).**
- The C-B reduced law is mathematically realizable by deterministic evolution on an enlarged
  (path-space) state space.
- The current record declares **no** physical Hamiltonian/conservative parent that could even pose
  the reproduction test. It does not declare one for the linear/Gaussian sector in C-B form either.
- **This does not establish that no physical bath could exist**, nor primitive noise (§3.5). It says
  that the record does not yet supply one.
- **The noise-origin question stays open at the physical-parent level.**

**HARD STOP.** Proposed for owner adjudication. No physics run, no new bath, nothing opened.
