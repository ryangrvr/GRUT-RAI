# L0-1h — OWNER RULING 01 (O-2 form: theorem document + exact appendix)

**Date:** 2026-09-29 · Given in session, on design rev 2
(`L0_1H_DHERM_B_DESIGN_01.md`, commit `5040dc9`; Issue #2 comment
`5896362378`).

## Adopted explicitly

1. **Form:** the theorem document plus an exact appendix (the O-4
   precedent), with **clause-level reporting kept intact.**
2. **The clauses stay completely separate:**
   - H2-m: growth causes the failure;
   - H2-s: accretivity is sufficient for monotone decrease;
   - H2-n: spectral stability without accretivity is insufficient.

   **H2-n may not rescue H2-m or H2-s,** because they answer different
   questions.
3. **The affinity line stays outside O-2.** Otherwise O-2 becomes a
   catch-all, and the orthogonality the floor has built is lost.

## The owner's reading (preserved)

> P-1 says that cannot be the mechanism visible to the retained-site
> kernel. The full state can grow while the observed one-site response
> remains bounded and decaying. That means "positivity" is not merely a
> proxy for state stability or transient growth.

> The thing I would watch most closely in the exact appendix is whether
> H2-s and H2-n separate cleanly … If that survives the actual n = 23,
> a = 1 family … spectral stability and observed monotone response are
> genuinely different structural layers, with monotone decrease possibly
> selecting a narrower class than either notion of passivity.

> A genuine reversal would have to appear as a new dependency, not as
> our interpretation of a similarity.

## Not ruled explicitly: recorded as open

**The mapping from clauses to O-2's single terminal label** (design
rev 2 §4, the operator's recommendation) was not stated. The owner's
no-rescue rule agrees with it, but the recommendation has a consequence
the owner should confirm knowingly: P-1 already excludes H2-m by
theorem, so **under that mapping O-2's label is already FALSIFIED, and
no appendix outcome can change it.** See `L0_1H_THEOREM_01.md` §0.
