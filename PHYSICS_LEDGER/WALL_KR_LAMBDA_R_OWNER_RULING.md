# OWNER DECISION RECORD — THE Λ_R RENORMALIZATION INPUT

**Date:** 2026-09-01 · **Ruling issued by:** the owner · **Recorded and
mechanically verified by:** `wall_kr_lambdaR_owner_ruling.py` ·
**Companion:** `WALL_KR_LAMBDA_R_OWNER_RULING_RESULT.json` ·
**Battery: 15/15, zero failures.** · **Numerical value introduced:
NO.** · **Register modified: NO.**
**W-0: computed-and-reported, NOT banked. HARD STOP.**

## THE RULING (verbatim)

> **The current GRUT record does not contain an independently justified
> numerical value for the renormalization invariant Λ_R. No numerical
> value will be introduced at this stage. Λ_R remains symbolic and is
> carried as one unresolved renormalization input. Axis 2 therefore
> remains parametrically unresolved with respect to Λ_R. Future
> numerical fixing is permitted only through an independently justified
> renormalization/matching condition that is established without
> reference to Axis 1, Axis 2, J(ω), plant data, resonance, memory
> behavior, or other downstream outcomes.**

Recorded, not composed by the builder. Its four operative clauses are
gated present: (a) no independently justified value exists; (b) none is
introduced now; (c) Λ_R is carried as **one** unresolved renormalization
input; (d) future fixing only via an independent condition.

## MECHANICAL VERIFICATION THAT NOTHING DOWNSTREAM WAS USED

- **No value assigned.** A pattern scan over this record's own source
  finds no numeric assignment to Λ_R or μ; Λ_R is carried as a free
  symbol throughout. The detector carries a teeth-control: a sentinel
  assembled at runtime *is* caught by the same scan.
- **Evidence basis.** The ruling rests on the hash-pinned authority
  sweep (8 entries, **zero** supplying a numerical scale) and on ruling
  C — not on any outcome artifact. The Axis-2 artifact is pinned for
  provenance only; its `out` block, which carries the classification and
  the regime map, is **never dereferenced**.
- **No barred channel.** The set of files read, intersected with the
  registry's barred set, is **empty** — the comparator-to-response
  channel is not used.

## THE STRUCTURAL RESULT: THE H⁰ FREE-INPUT COUNT IS EXACTLY ONE

| stage | H⁰ local freedom |
|---|---|
| before D5 | five real local constants (c0, c2, c4, c0p, c2p) plus the scale μ |
| after D5 (H⁰) | **c0 = 0 and c2 = 0 exactly** (structural); the surviving (μ, c4) pair is redundant by exactly one function's worth |
| **irreducible count** | **1 — the single constant Λ_R = μ·exp(c4/2A), RG-invariant** |

Gated two ways: the response genuinely **depends** on Λ_R
(∂ReΣ/∂Λ_R ≠ 0, so the count is not zero), and the explicit (μ, c4)
form is **identically** the one-constant form (so the count is not two).
A control confirms a *wrong* invariant fails the identity, so the
collapse is specific to Λ_R and not an artifact of the algebra.

**Framing (owner's refinement, adopted): REPARAMETERIZED, not removed.**
Nothing left the theory. Two redundant parameters were replaced by one
irreducible constant — which is why this is a positive structural
result and not a loss.

The H² locals (c0p, c2p) are **not** in this count — they remain
fork-gated.

## WHAT THE RULING SETTLES — AND WHAT IT DOES NOT

**Settles:** that no numerical value enters GRUT at this stage; that Λ_R
is carried as one unresolved renormalization input; that Axis 2 is
parametrically unresolved with respect to Λ_R (**classification C
stands**); and the admissibility condition governing any future fixing.

**Does not settle:** the value of Λ_R; Axis 2's absolute
classification; the H² local fork; Gate-E; the consequence cell beyond
recording C.

**Explicitly not done here:** the register/ledger parameter-count
update. `provenance/claims.json` is read-only in this stage and the net
stands unchanged. That update is the **next** stage and awaits its own
authorization.

## THE EPISTEMIC POSITION THIS PRESERVES

The calculation supplies the functional form and the nonlocal
coefficient of the H⁰ contract response:

    Re Sigma^{H0}(omega) = 2 A omega^4 log( Lambda_R / omega ),
    A = -3/(1280 pi^2)   [nonlocal, fixed, cross-route verified]

It does **not** contain a mechanism that determines the dimensionful
integration/renormalization constant. Recording that honestly is
stronger than selecting the value that would make the downstream
phenomenology most interesting — and the blind that bars the
comparator-to-response channel is precisely what would have been
violated by the most tempting choice.

## HARD STOP

No numerical Axis-2 verdict follows from this ruling. **C stands unless
an independently justified renormalization condition is subsequently
introduced.** Next: the ledger/parameter-count update, then the H²
local fork and Gate-E, each separately authorized.
