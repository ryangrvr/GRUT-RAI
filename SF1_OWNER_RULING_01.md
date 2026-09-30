# SF-1 — OWNER RULING 01 (pre-freeze review; execution authorization; v4 exception)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5903400225`**, after review of
`SF1_FORMATION_CHARTER_01.md` at `f2177da`, `SF0_OWNER_RULING_01.md` and the frozen SF-0
definitions. The comment is authoritative; this file records it.

**Decision:** the charter is **APPROVED WITH AMENDMENTS.** Once the amendments are recorded and the
charter is frozen at a new commit, **SF-1 is AUTHORIZED FOR ONE EXECUTION.** This ruling
explicitly grants the **campaign-specific exception to the post-v4 in-house physics stop, for SF-1
only.** No other post-v4 physics campaign is reopened.

## 1. OR-1: procedural mappings

- **1a. Integrity failure = RUN VOID, no terminal (APPROVED).** This applies when V-FOCK, C-1 or C-5
  fails for an implementation or integrity reason. On a void run:
  - preserve the failed artifact and identify the defect;
  - do not silently repair and re-run;
  - return to an owner ruling before any second execution.

  A void run is not STATE-NOT-LAW, EDGE-ONLY-NONROBUST or UNFORMULABLE.
- **1b. C-2 / C-3 (APPROVED WITH NARROWING).**
  - Classes well-defined but differing within the declared family ⇒ **EDGE-ONLY-NONROBUST**.
  - The relevant class cannot be defined under the frozen common procedure ⇒ **UNFORMULABLE**.
  - Apply mechanically.

## 2. OR-2: C-6 adopted, REPORT-ONLY

- **Family:** N_L = nearest odd(√L), on a predeclared even-L sequence.
- **Purpose:** map the crossover between finite density and fixed-N dilution, and test for a
  genuine two-scale regime. It has two vanishing scales, k_F(L) ~ N_L/L and q(L), and P and P′ can
  probe different relative scalings of them.
- **Constraints:**
  - It need not land in D or E.
  - A P/P′ disagreement in C-6 does **not** trigger EDGE-ONLY-NONROBUST.
  - **It cannot assign or change the terminal.**
- **Required report, without fitting:**
  - the exact k_F(L) scaling;
  - the P result and the P′ result;
  - whether a unique one-parameter z exists;
  - if not, the label **MULTISCALE / PATH-DEPENDENT IR** (report-only).
- A C-6 mismatch is neither a defect nor a negative terminal. It constrains interpretation: a
  positive result is then two **asymptotic sector classes** separated by a crossover/double-scaling
  family, not an exhaustive binary classification.

## 3. OR-3: boundary condition and parity

- **Periodic BC: APPROVED.** RS-1's antiperiodic grid does not bind SF-1. The two must not be mixed
  in this campaign.
- **Odd-N convention: APPROVED.** There is no averaging over even-N degenerate ground states. The
  V-FOCK uniqueness check stays mandatory.
- **Added analytic control:**
  - For the periodic ring with N odd, the occupied ground-state momenta are the symmetric set around
    k = 0. They fill every ±k degeneracy pair together, so no partially filled ±k pair remains at the
    Fermi edge.
  - The particle–hole controls must confirm the corresponding odd-hole statement.
  - **Analytic vs exact finite-Fock disagreement ⇒ RUN VOID.**

## 4. I-q Brillouin-zone quotient

- Soft momenta are identified modulo **q ~ −q ~ q + 2π**, with the representative in [0, π].
- This prevents D-¼ and D-¾ from being assigned different I-q only because their 2k_F-type points
  are represented on opposite sides of the zone.
- **C-1 must verify the quotient.**

## 5. Freeze order

1. Amend OR-1.
2. Add C-6 as REPORT-ONLY.
3. Freeze periodic BC and the odd-N convention.
4. Add the analytic odd-N control.
5. Clarify the I-q quotient.
6. Replace §10 with the rulings.
7. Commit the charter.
8. Record that commit hash as the **SF-1 frozen charter** in CURRENT_STATE.

Only then may implementation begin. **No preview calculation before the frozen commit.**

## 6. Authorization and v4 exception (SF-1 only)

**Covers:**
- `calc/sf1_formation.py`;
- the exact/symbolic derivations the frozen charter requires;
- the finite-Fock integrity checks and the finite-size cross-checks;
- C-1 … C-6 as frozen;
- `SF1_FORMATION_RESULT.json` and `SF1_FORMATION_VERDICT_01.md`.

**Does not cover:**
- a second run after a void or a failure;
- changing the sector families;
- interactions or a chemical potential;
- changing the BC;
- a new parent;
- SF-2 / domain mixing;
- S-5, gravity or Π₀;
- any empirical or cosmological interpretation.

**One run, one verdict, hard stop.**

## 7. Terminals

- **Physics terminals:** FORMATION-OF-LAW-CLASS, STATE-NOT-LAW, EDGE-ONLY-NONROBUST, SECTOR-SMUGGLED,
  UNFORMULABLE.
- **Procedural state:** **RUN VOID**, which is not a physics terminal.
- C-6 cannot assign or change the terminal.

**Positive-result wording fence** (the strongest allowed statement):

> Within one fixed free-fermion microscopic parent, different exact conserved particle-number
> scaling sectors support inequivalent IR effective-law classes under the preregistered
> density-response coarse-graining.

If C-6 is path-dependent, append:

> The result concerns distinct asymptotic sector scalings; intermediate sub-extensive particle-number
> scalings form a crossover/multiscale regime rather than a third preregistered terminal class.

Do not call this spontaneous universe formation or dynamical selection. The sector is supplied by
conserved boundary/state data.

## 8–9. Significance and HARD STOP

**The result counts only if the whole package survives:**
- the same full parent H;
- the same parameters, statistics and readout;
- a difference in exact conserved sector only;
- a common coarse-graining;
- an inequivalent structural invariant after the quotient.

**On failure,** record it without replacing the free-fermion parent.

**After the single run:**
- commit the result and the verdict;
- update CURRENT_STATE;
- stop for owner adjudication.

There is no automatic SF-2, and no migration of the result to cosmology or to GRUT's substrate.
