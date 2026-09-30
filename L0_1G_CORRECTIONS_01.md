# L0-1g (O-6) — CORRECTIONS 01 (additive; entropy-rate tail)

**Authority:** `S6_OWNER_RULING_02.md` §7 (Issue #2 comment `5915173769`).
- **Additive only.** The original O-6 ruling (`L0_1G_OWNER_RULING_02.md`) and the historical records are not
  rewritten.
- **No O-6 terminal changes.**
- **Date:** 2026-09-30.

## Correction C-1: the Ḋ tail

**1. What the accepted O-6 text says.** It describes the reduced relative-entropy derivative Ḋ as carrying "t⁻³
sign-alternating ripples" (`L0_1G_OWNER_RULING_02.md:36-38`; `L0_1G_PREFREEZE_REVIEW_01.md:31`). That is **correct
as a loose O(t⁻³) upper bound**, but **not as the leading asymptotic power**.

**2. What S6-1 proves** (`S6_1_THEOREM_01.md` LS-3, verified; accepted in `S6_OWNER_RULING_02.md` §6). On the
declared infinite pinned chain:

> D(t) = t⁻⁶P(t) + O(t⁻⁷),  Ḋ(t) = t⁻⁶P′(t) + O(t⁻⁷),

where P = ¼‖M‖_F² is the quasi-periodic band-edge amplitude.

**3. Late sign reversal survives, now unconditionally.** P is analytically non-constant for every positive
temperature pair, because its e^{4iψ₋} coefficient satisfies p₄,₀ > 0. Hence **Ḋ still changes sign at arbitrarily
late times**, with envelope t⁻⁶.

**4. Scope.**
- **J is unaffected:** its t⁻³ statement stands as an upper bound.
- **O-6 remains FALSIFIED** for strict pointwise / whole-window ordering.
- The correction **strengthens** the qualitative basis of that terminal. It does not reverse it.
