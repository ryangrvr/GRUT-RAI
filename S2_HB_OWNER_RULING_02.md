# S2-HB — OWNER RULING 02 (terminal accepted; A-1 … A-4; S-2 chain closed; S-3 selected)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5909652190`**, after review of the
pre-registration `0942dbd`, interim ruling `d1ba71d`, audit `bf0706e`, and the O-6 / S5-1 source
records. The comment is authoritative; this file records it.

## 1. Primary terminal: ACCEPTED

**S2-HB = UNRESTRICTED-REALIZATION-ONLY**, under the frozen O-1 → O-6 precedence.

> **Binding reading:** The nonlinear C-B stochastic process has an exact deterministic enlarged-state
> realization by a standard path-space/skew-product construction. But the current GRUT record
> declares no physically constrained Hamiltonian/conservative bath that realizes, or can presently
> formulate, the C-B discriminator.

- The exact realization is **HB-U, not HB-P**. It is the no-triviality case: the hidden state is the
  driving path, evolved by a deterministic shift/cocycle.
- It is **a mathematical representation theorem, not a physical origin theorem.**

## 2. A-1: the outcome-list gap is real but inactive

- **The gap:** the frozen outcomes have no label for "HB-P-admissible + scope NONE". The taxonomy is
  not exhaustive over every imaginable audit state.
- **Why it is inactive:** once A-1a and A-1b are ruled, no actual candidate lands in that cell.
- **Handling:**
  - Do not amend the frozen outcome list retroactively.
  - Record A-1 as a **latent taxonomy gap with no effect on this terminal.**
  - A future case in that cell requires an owner ruling, not silent mapping.
- O-3 precedes O-4 and O-5 in any event.

## 3. A-1a: P-4 FAILS for O-6 as declared

- O-6's declared split names site 1, with state (q₁, p₁), as the **retained system**. Its ensemble
  randomizes ⟨q₁²⟩ = T_s/K₁₁ and ⟨p₁²⟩ = T_s. **p₁ is not environmental.**
- Relabelling p₁ as "hidden bath" would change the declared partition after inspection.
- The hybrid q₁(0) = a, p₁(0) = 0 with a Gibbs-random bath is a different initial class. It is **not
  declared and cannot be imported.**

## 4. A-1b: P-6 FAILS for S5-1 C₀

- P-6 is a positive requirement: the forcing must be GENERATED-BY-DYNAMICS. A setup with the bath at
  rest and no forcing channel cannot satisfy it. **"N/A" is not a pass.**
- This is not a criticism of S5-1, which asked a different question.

## 5. O-5 sub-label: TRUE

**NO-PHYSICAL-BATH-CANDIDATE = TRUE**, as a sub-label under the narrow reading. No candidate passes
all of P-1 … P-8.

| Candidate | Why it fails |
|---|---|
| O-6 | P-4 |
| S5-1 C₀ | P-6 |
| S-1 FKM | P-7: general-theorem-only, undeclared |
| Sz.-Nagy / Koopman / KvN / cotangent lift | HB-U or representational |
| CTP / FDT / KMS | no parent declared |

## 6. A-2: R-2 anchoring (wording clarification, not an amendment)

- **R-2 means the β = 0 linear/Gaussian control class.** It is used only to report whether a physical
  bath reproduces the old S-1 second-order equivalence. **It does not count as reproduction of a
  β > 0 discriminating member.**
- No result changes.

## 7. SECOND-ORDER-ONLY: correctly NOT assigned

The audit's refutation is accepted, on four grounds:
- **Response mismatch.** O-6 has φ′(0) = 0, whereas C-B has m₁′(0) = −K₁₁a.
- **The global-Gibbs covariance coincidence is not enough.** It is:
  - not the declared law;
  - of the wrong two-time form;
  - without a declared identification;
  - not extendable to the discriminator.
- **S-1 FKM** is not a declared HB-P parent. It relies on the non-admitted Ohmic/overdamped route.
- **Hence SECOND-ORDER-ONLY = FALSE.**

## 8. A-4: FORMULABLE-ONLY-WITH-NEW-COUPLING kept, fenced

This label remains report-only. **Fence: the new coupling is necessary, not sufficient.**

A physical C-B bath would also need at least:
- a second-order Hamiltonian nonlinear system parent matching the C-B quartic drift;
- system momenta / symplectic structure;
- a declared spectral density / bath family;
- a declared bath initial state;
- possibly the wide-band and overdamped/slaving structures, which are **not admitted**.

**BLOCKED-BY-NOT-ADMITTED-LIMIT is not assigned.** The parent itself is missing before any limit
question becomes adjudicative.

## 9. Accepted S2-HB synthesis

| Question | Answer |
|---|---|
| Same-state-space initial uncertainty = C-B ongoing noise? | **No** (S2-1) |
| Unrestricted enlarged deterministic realization? | **Possible** |
| Declared physical Hamiltonian-bath realization? | **Absent from the current record** |

> **The current GRUT record can distinguish ongoing noise from initial uncertainty on the same
> nonlinear state space. It does not yet distinguish fundamental stochasticity from a suitably
> enlarged deterministic physical environment, because no such physical parent has been declared and
> tested.** This is the strongest statement earned.

## 10. No automatic rescue bath

- Do not open an S2-HB physics construction.
- Inventing a quartic Hamiltonian system parent, a bath coupling, a spectral density, an initial bath
  state and a wide-band/overdamped hierarchy because the record lacks them would be a **new-parent
  rescue**.
- Such work is preserved only as a possible future hypothesis campaign, chosen explicitly by the owner.

## 11. The S-2 chain is closed

| Gate | Terminal |
|---|---|
| S2-0 | CLASS-SPLIT |
| S2-1 | FULL-DISCRIMINATOR-CONFIRMED |
| S2-HB | UNRESTRICTED-REALIZATION-ONLY |

- **Sub-label:** NO-PHYSICAL-BATH-CANDIDATE.
- **Report-only:** FORMULABLE-ONLY-WITH-NEW-COUPLING, with the A-4 fence.
- **Deposit:** `S2_NOISE_ORIGIN_DEPOSIT_02.md`, containing no new analysis.

## 12. Next: the S-3 crossed cell (S3-0 formulation/audit gate only)

> **Does generator-side cycle affinity break correlation complete monotonicity when the noise is held
> FDT-like?**

- **Why S-3:** it is the missing crossed cell in the pre-registered reversal diagnostic. It was
  preserved before these results and imports no new parent.
- **File:** `S3_CROSSED_CELL_01.md`. No physics execution; no v4 exception.
- **Objective:** from declared records only, construct the crossed comparison: **generator affinity
  varied**, with the **noise/dissipation relation held FDT-like**. Ask whether P^corr_CM is preserved
  or lost.
- **What the audit must determine:** whether the crossed cell is formulable **without changing**:
  - the substrate class;
  - the retained observable;
  - the stochastic convention;
  - the temperature/noise rule;
  - the response/correlation normalization.

  **If it is not formulable, stop; do not invent a hybrid.**
- **Why now:** S2 separated noise type from drift curvature. S-3 asks about generator relational
  asymmetry → correlation structure, with the noise controlled. That is the remaining crossed cell
  needed before the reversal diagnostic can be evaluated without confounding the generator, noise,
  response and correlation axes.

## 13. Actions / fences

**Create:**
- this ruling;
- the accepted banner in `S2_HAMILTONIAN_BATH_BOUNDARY_01.md`;
- `S2_NOISE_ORIGIN_DEPOSIT_02.md`;
- the CURRENT_STATE update (S2-HB closed).

**Then open and pre-register S3-0 only.**

**Not authorized:**
- an S3 physics run;
- a reversal-diagnostic terminal;
- a new bath construction;
- S-6, S5-WB or S5-OD;
- gravity, Π₀ or cosmology.

> **S2 has excluded initial uncertainty as a substitute for ongoing nonlinear noise, but it has not
> established primitive noise.** Exact deterministic path-space realization exists, while no declared
> physical Hamiltonian bath currently reaches the nonlinear discriminator. The next clean question is
> the pre-existing S-3 crossed cell, not a rescue bath invented after the fact.
