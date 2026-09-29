# EA-0 — OWNER RULING 01 (terminal withheld; independent verification ordered)

**Date:** 2026-09-29 · Given in session, on `EA0_ENDOGENOUS_ACCESS_FORMULATION_01.md` (commit
`1748ccd`; Issue #2 comment `5897588240`). Recorded from the owner's words; any misstatement is
corrected by owner edit, not defended.

**Accepted as recorded:** the H-ADM correction and the P-4 correction (`454ba5a`).

## 1. Independent verification: YES

EA-0's proposed terminal rests on proof-sketch claims, so one independent, adversarial,
read-only theorem-verification pass of L1–L8 and the conclusions built on them comes first. It
must separate five grades: theorem/identity; standard result imported; consequence proved only
under extra hypotheses; heuristic interpretation; unsupported strengthening. **No result is
protected.**
- **Per-lemma verdicts:** VERIFIED / VERIFIED-WITH-NARROWER-SCOPE / NOT ESTABLISHED /
  COUNTEREXAMPLE / IMPORTED-STANDARD.
- **Output:** `EA0_INDEPENDENT_VERIFICATION_01.md`.
- **Not allowed during the pass:** no EA-1 charter, no new physics model, no numerical member
  campaign.
- **`EA0_ENDOGENOUS_ACCESS_FORMULATION_01.md` is not modified during verification.** Any
  correction is proposed afterwards, additively.

**Verification targets (owner):**
- **L1–L3:** what exactly "generic" means.
- **L2's dissipative extension:** it must follow from assumptions actually earned. No
  nondegenerate-noise assumption may be imported silently from another layer.
- **L4:** separate the exact theorem ("compression cannot create an edge absent from the
  uncompressed relation") from the stronger interpretation ("state dependence only excludes
  physical interactions").
- **L5:** all degeneracy qualifications.
- **L6:** linear observables in the quadratic class only.
- **L7 — highest priority.** Separate five statements, and do not treat 3–5 as equivalent
  unless proved:
  1. P_ρ ≠ I needs a proper invariant subspace;
  2. Γ(ρ) ≠ Γ needs every relevant compressed double commutator to vanish;
  3. that implies exact invariant structure in the generator;
  4. that structure is "aligned with a local configuration";
  5. the coupling "acts trivially" in the sector.

  Test whether symmetry or cancellation can make P_ρ[A,[H,B]]P_ρ = 0 while a microscopic
  coupling stays nonzero on the invariant sector. If it can, **narrow L7 to its actual
  necessary-and-sufficient statement and retire the stronger mechanism language.**
- **L8:** check against the frozen P-1 definitions, keeping the distinction that C2 uses the
  model's ground state.

## 2. The local site net: ADMISSIBLE, with a boundary

The substrate local net {𝒜_x} may be presupposed for EA-0. Locality is declared substrate
structure in the Level-0 program, and L0-1b certified it as load-bearing for the recorded
geometry predicate. The qualification, carried prominently:

> EA-0 is conditional on an already-local ontology. It does not derive the existence,
> uniqueness, or origin of the local net itself.

C-6 may be called **seedless relative to the declared local net.** Do not call it absolutely
structure-free.

## 3. "H is k-local": NOT YET a principled selector

- Do not use C-9 to rescue EA-0. Locality being an earned ingredient does not imply that the
  tensor-product structure in which H is k-local is uniquely or necessarily selected.
- **C-9 = CRITERION-SMUGGLED / EXTERNAL-UNVERIFIED** until a separate in-house argument
  establishes the criterion from earned structure.
- It may remain a future mathematical route.

## 4. EA-0 terminal: WITHHELD pending verification

**The owner's provisional classification:**

> TRIVIAL/IDENTITY ON THE EARNED SCOPE, with a CONDITIONAL FORMULABLE branch when the generator
> contains suitable exact local invariant/exclusion structure.

**Why:**
- C-6 is genuinely seedless relative to the local net.
- It is trivial on every class Level-0 has earned so far.
- Its non-trivial branch needs generator structure that Level-0 has not earned.
- So calling it CLASS-SPLIT would risk treating a conditional, externally named branch as though
  both sides were equally established.

**CLASS-SPLIT becomes justified only if** verification proves the non-trivial branch at theorem
strength within an explicitly declared class.

## 5. The owner's reading (preserved)

> EA-0 may already have answered the state-exclusion idea more sharply than an EA-1 experiment
> would have: the state can select among structural sectors, but so far the generator has to
> provide those sectors first. If that survives verification, then the real Level-0 problem has
> migrated to S-5: where does the generator's structure come from?

## 6. HARD STOP

Stop after the verification report. **EA-1 remains NOT AUTHORIZED.**
