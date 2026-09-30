# SF-1 — OWNER RULING 02 (terminal accepted; architectural consequence; SFG-0 opened)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5903593151`**, after review of
`8a4f71c` (charter), `840b3c3` (pre-run script), `1fedd3e` (the single run's result and verdict)
and the closed-form derivation in `calc/sf1_formation.py`. The comment is authoritative; this file
records it.

## 1. Terminal: ACCEPTED

- **SF-1 = FORMATION-OF-LAW-CLASS**, terminal at the frozen SF-1 scope.
- **C-6 = MULTISCALE / PATH-DEPENDENT IR**, report-only.
- The single run is valid. **No re-run is needed or authorized.**

## 2. Provenance: accepted

- Charter `8a4f71c` → script `840b3c3` → result/verdict `1fedd3e`.
- The script blob is byte-identical at `840b3c3` and `1fedd3e` (git blob `7cb8be3…`).
- There was no second run, and all integrity gates passed.
- AM-7 is accepted: it was made pre-computation, disclosed, and derived from a Lipschitz bound,
  not from residuals. AM-8 is accepted as pre-freeze specification.
- The non-member sympy tooling checks did not evaluate any SF-1 family or terminal quantity. They
  are no violation.

## 3. Not an implementation artifact

- The contrast follows analytically from the same parent, ε(k) = −2 cos k, and the same
  density-response edge:
  - fixed density: ω⁻ ~ v_F q, so z = 1;
  - fixed N: ω⁻ = 4 sin²(q/2) ~ q², so z = 2.
- I-q differs (2 vs 1) on the same object.
- The D-¼, D-¾, E-3 and PH controls show these are **family classes**, not one chosen member.
- **The conserved sector selects which region of the one dispersion becomes the IR reference
  structure.**

## 4. Accepted finding (verbatim)

> **Within one fixed free-fermion microscopic parent, different exact conserved particle-number
> scaling sectors support inequivalent IR effective-law classes under the preregistered
> density-response coarse-graining.** **The result concerns distinct asymptotic sector scalings;
> intermediate sub-extensive particle-number scalings form a crossover/multiscale regime rather than
> a third preregistered terminal class.**

The finding is: fixed microscopic law + different conserved boundary/state sector ⟹ different IR
universality class.

## 5. Terminology fence: "law class"

- The microscopic law did **not** change.
- **Use:** "effective-law class", "IR universality class", "sector-conditioned effective physics".
- **Not:** "different fundamental laws", "the laws of physics changed", "different universes
  derived".
- The result is stronger than STATE-NOT-LAW, because z and the soft-branch structure are structural
  IR invariants. It is weaker than deriving different microscopic Hamiltonians.

## 6. C-6 is a positive finding

- N_L ~ L^{1/2} gives k_F ~ L^{−1/2}:
  - P gives z = 2;
  - P′ (q ~ L^{−1} ≪ k_F) gives ω₁ ~ v_F q ~ L^{−3/2}, so z = 3/2.
- Record:

  > **The parent does not possess only two possible IR behaviors. Dense and fixed-N dilution are two
  > asymptotic universality classes, connected by multiscale crossover sectors whose effective
  > exponent depends on the path through (q, k_F) → (0, 0).**

## 7. Architectural consequence

- **Not discharged:** SF-1 does not discharge the post-floor finding that the physical lift is
  IRREDUCIBLE/SUPPLIED.
- **Falsified in general:** the informal inference *"if a member is supplied rather than selected
  by the microscopic equations, its effective physics must also be supplied at the law level."*
  - SF-1 is the counterexample: the sector label is supplied, the generator is fixed, and the IR
    class follows once the sector scaling is supplied.
- **The architecture now distinguishes:**
  - **microscopic-law selection**;
  - **sector/boundary selection**;
  - **effective-law emergence within the sector**.

  In symbols: H_micro + S_boundary ⟶ L_eff[S].

> **A supplied sector does not imply a supplied effective law.**

## 8. Not established

SF-1 does not establish:
- universes or cosmological domains;
- varying constants;
- mixing, or an explanation of observed constants;
- a GRUT-specific formation mechanism;
- spontaneous selection, or relaxation into a sector;
- a derivation of the sector label, or of the physical lift;
- a solution of S-5.

This is **formation-by-sector restriction, not formation by attractor dynamics.**

## 9. Next campaign: SFG-0 (audit only)

- **Output:** `SFG0_GRUT_FORMATION_VARIABLE_01.md`. No new physics run.
- **Question:**

  > Does the earned/current GRUT substrate contain a conserved, topological, boundary, occupancy,
  > realization, or other persistent sector variable Q such that one unchanged GRUT-relevant parent
  > can be restricted to distinct Q-scalings and thereby yield inequivalent effective-law classes?

- **Candidates to inspect:**
  - U3 realization dimension and continuum modes;
  - L0-1a/b/c substrate variables;
  - the FS-1 conserved tower;
  - P-6 exact invariant sectors;
  - O-6 conservative tori;
  - relational partition sectors;
  - access seeds;
  - geometry/carrier sectors;
  - any topological, winding or conserved labels;
  - any state/boundary datum controlling kernel spectral support without changing the generator.
- **Six questions per candidate:**
  1. Is Q state/boundary/conserved data, not a generator parameter?
  2. Is the parent unchanged across Q?
  3. Are the sectors exact/persistent?
  4. Is there one common retained observable/coarse-graining?
  5. Does changing Q alter a pre-registered structural IR invariant, not only a value?
  6. Is the change already known, formulable, or absent?
- **Frozen outcomes:**
  - GRUT-CANDIDATE-FOUND;
  - CLASS-SPLIT;
  - STATE-NOT-LAW;
  - SECTOR-SMUGGLED;
  - NO-CANDIDATE-IN-EARNED-CORE;
  - UNFORMULABLE.
- **No new variable may be invented.**
- **Why SFG-0 precedes S-5:**
  - If GRUT has a formation variable, test it before asking where the generator comes from.
  - If not, the formation route cannot presently absorb GRUT's supplied selections, and S-5 becomes
    the cleaner next question.

## 10. Record / state actions

- Create this file.
- Put an accepted-terminal banner on the verdict, preserving the original.
- Update CURRENT_STATE: **SF-1 CLOSED / ACCEPTED: FORMATION-OF-LAW-CLASS**; C-6 report-only;
  **SFG-0 open, audit only.**
- HARD STOP after the SFG-0 audit.
- No second SF-1 run, no SF-2, no domain mixing, no S-5 yet, no empirical/cosmological
  extrapolation.
