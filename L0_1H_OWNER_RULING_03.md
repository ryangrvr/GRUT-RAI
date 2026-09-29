# L0-1h — OWNER RULING 03 (O-2 = FALSIFIED, terminal)

**Date:** 2026-09-29 · Given in session, on `L0_1H_APPENDIX_01.md`
(commit `ff76f82`; Issue #2 comment `5896579147`).

## The ruling

**O-2 = FALSIFIED, terminal**, at the frozen scope. The original
H-HERM-2 proposal, that **accretivity carries the relevant
monotone-response positivity**, is falsified at the declared scope.

| Clause | Verdict | Reason |
|---|---|---|
| **H2-m** (transient growth is the mechanism) | **FALSIFIED** | Theorem P-1 rules it out for the retained-site kernel on every stable member. |
| **H2-s** (accretive ⇒ monotone decrease) | **FALSIFIED** | Exact counterexample members at all 8 declared g, with certified positive rise margins (smallest 1.44). |
| **H2-n** (stable and non-accretive ⇒ non-monotone) | **HOLDS at tested scope** | Certified across the whole exact band at all 8 declared g. **Recorded independently; it cannot rescue H2-m or H2-s.** |

**The certified nesting** at every tested g (n = 23, a = 1, retained
site):

> w\* < d_acc < d_mono, so **stable ⊋ accretive ⊋
> monotone-decreasing retained response.**

The owner's summary: **spectral stability ≠ accretivity ≠ monotone
response.**

**Method closure, as the owner recorded it:**
- The counterexample is certified (k′(t\*) > 0 on a strictly accretive
  member, margin ≥ 1.44). It is not a tolerance artifact.
- The negative control showed the instrument can reject a false
  certificate.
- The e¹¹⁰⁰ overflow was a float-harness issue, correctly isolated, and
  never entered the exact certification.

**Limits kept (the owner's):**
- **The mechanism is not established.** The ring-lap interpretation
  stays untested.
- **No stronger interpretation is recorded** than the separation
  itself.

## Operator note: consistency with the O-2 limitation in the termination adoption

`L0_1_FLOOR_TERMINATION_ADOPTION_01.md` binds the following: an
observability limit of the retained-site observable is never to be
counted as a verdict on accretivity.

- H2-m's falsification does rest on such an identity (P-1: state growth
  exists but the retained site cannot see it). Taken alone, it is an
  observability result about the mechanism.
- **The label does not depend on it.** H2-s fails independently by
  certified *positive* findings: strictly accretive members whose
  retained response rises. That is a separation the observable *sees*,
  not a blindness.
- So O-2 = FALSIFIED is consistent with the adoption ruling.

## Floor status

| Obligation | Terminal result |
|---|---|
| O-1 | CLASS-SPLIT |
| O-2 | **FALSIFIED** |
| O-3 | DISCHARGED |
| O-4 | CLASS-SPLIT |
| O-5 | DISCHARGED |
| O-6 | FALSIFIED |
| O-7 | **ready for adjudication** (T5 precondition met) |

**Next (the owner's direction):** the O-7 synthesis, using all six
terminal records exactly as they stand, including the failed hypotheses
and the scoped qualifications.
