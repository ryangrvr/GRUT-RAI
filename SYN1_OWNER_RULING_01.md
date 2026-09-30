# SYN-1 — OWNER RULING 01 (readiness accepted; A-1 … A-4 approved; Theorem LD and sector-selection S-1 statuses fixed)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5916545551`**, after review of the final SYN-1
package at `cec1f14` (the four deliverables, the readiness verdict, and the verifier's V1–V4 and m1–m10 corrections).
The comment is authoritative; this file records it.

## 1. Readiness terminal: ACCEPTED

**SYN-1 = READY-WITH-ADDITIVE-CORRECTIONS.**
- There is **no unresolved record conflict** in the canonical package: **NOT-READY — RECORD CONFLICT = FALSE**.
- The only remaining blockers are the four additive/status corrections A-1 … A-4. **None changes a scientific
  terminal.**

## 2. A-1: banner on the old working theory — APPROVED

The banner added to `GRUT_WORKING_THEORY_01.md` (owner's exact text):

> **CURRENT WORKING-THEORY POINTER:** The governing working-theory statement is
> `GRUT_WORKING_THEORY_SYNTHESIS_01.md` (SYN-0, accepted). The canonical deposit is
> `GRUT_WORKING_THEORY_DEPOSIT_01.md`. For superseded wording on the ω⁷ grade and on noncommutativity versus physical
> lift selection, see `GRUT_RECORD_RECONCILIATION_INDEX_01.md` items 5 and 6.

- Historical content below the banner remains unchanged.
- The older synthesis is not rewritten to agree with the newer record.

## 3. A-2: Theorem LD — APPROVED / ACCEPTED at its audited scope

**Owner statement: THEOREM LD = ACCEPTED AT AUDITED S2-0 SCOPE.**

**Binding statement:**

> **For a linear canonical Itô drift f_can(x) = −Mx, with post-t = 0 forcing given by a true zero-mean martingale
> satisfying the stated integrability conditions,**
>
> 𝔼[x(t) | x₀] = e^{−Mt}x₀.

This includes the audited Itô stochastic-integral and compensated finite-first-moment Lévy cases recorded in S2-0.

**Accepted consequence at the frozen observables:**

> **The retained mean response is noise-blind in that linear canonical-drift class; the anchored stationary
> correlation has the recorded deterministic-ensemble representation when the required stationary second moments
> exist.**

**Scope fences:**
- This is **not** a claim that all statistics are equivalent.
- O-3 / conditional variance can distinguish stochastic forcing from deterministic initial uncertainty.
- It does not apply automatically outside the true-martingale / stated-integrability setting.
- It does not settle physical noise origin.
- It does not supersede S2-1's nonlinear C-B discriminator.

**Standing:** this acknowledgement makes explicit a theorem already consumed by the accepted S2-0 classification. It
adds no new physics. It is recorded additively; the S2 audit is not rewritten.

## 4. A-3: sector-selection S-1 status — APPROVED

**Owner status statement: SECTOR-SELECTION S-1 = PROVISIONAL (IN CLASS).**

The governing formulation is the P3/P4 restatement:

> **locality + symmetry → branch classes → spectral/matrix selection → effective sector**

**Binding fences:**
- Stop saying **"counting selects the exponent."**
- The result is a **class/compatibility selection statement**, not a unique point-selection law.
- Amplitude, state and boundary data remain supplied where the governing records say they are supplied.
- The ω⁷ result is governed by the later GR2A wording: **"conditional occupancy evidence, not selected by the
  generative core."**
- This note does not promote the sector-selection result beyond its tested class.

`SECTOR_SELECTION_VERDICT_01.md` remains historical and unchanged. This note fixes standing only; it creates no new
terminal.

## 5. A-4: pointer on the historical successor list — APPROVED

The pointer added to the top of `L0_1_FLOOR_SUCCESSOR_LIST.md` (owner's exact text):

> **CURRENT STATUS POINTER:** Current successor statuses are maintained in `GRUT_SUCCESSOR_STATUS_01.md`. The
> historical successor questions below are preserved unchanged.

No status columns are added to the historical list, and its question text is not rewritten.

## 6. Readiness transition (mechanical)

After the four corrections are applied exactly:
1. mark A-1 … A-4 **APPLIED** in `GRUT_RECORD_RECONCILIATION_INDEX_01.md`;
2. record this ruling;
3. banner `SYN1_READINESS_VERDICT_01.md` as accepted;
4. update CURRENT_STATE;
5. run the state/render sync checks.

Then perform one **read-only editorial cross-check**:
- all four corrections exist;
- no historical body text was rewritten;
- D-1 and D-4 remain byte/content-equivalent except for required bookkeeping;
- no terminal wording changed.

**If it passes, the readiness state advances mechanically to PUBLICATION-READY.** No second owner adjudication is
required for that rename. If the cross-check finds an unexpected divergence, stop at READY-WITH-ADDITIVE-CORRECTIONS
and return for ruling.

## 7. What PUBLICATION-READY means

> **The canonical working-theory package is internally reconciled and suitable to serve as the next public GRUT
> record.**

It does **not** mean:
- the theory is experimentally confirmed;
- the theory is fundamental;
- the public brief replaces the technical record;
- the package has external peer review;
- the package contains a confirmed novel quantitative prediction.

The public brief's statement "zero confirmed novel quantitative predictions; no external peer review" is preserved
unless and until the record itself changes.

## 8. Publication authorization

**This ruling does not authorize a Zenodo upload.** After the corrections and the mechanical PUBLICATION-READY state
are recorded: **HARD STOP for the owner's publication decision.**

**Not opened:**
- new physics;
- the faithful-representation audit;
- S-7, S-8 or S-4;
- a new bath;
- S5-WB or S5-OD;
- gravity or Π₀;
- a new quantum route.
