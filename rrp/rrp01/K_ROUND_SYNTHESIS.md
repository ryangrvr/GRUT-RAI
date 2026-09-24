# K_ROUND_SYNTHESIS — what the kernel test actually found

**Date:** 2026-09-24. **Round:** RRP-01 K-round (protocol frozen `rrp/rrp01/K_ROUND_PROTOCOL.md`).
**Inputs:** four refuters; six blinded kernel computations (53 contractions, 244 kernel
elements) at `rrp/rrp01/kernels/`; comparator `rrp/rrp01/COMPARATOR_02.json`.
**Verdict: K-U-PARTIAL.** Owner-ratified formulation (2026-09-24): *the sweep provides
evidence for a nontrivial correspondence in several independently motivated contraction
classes — some priced quantities are demonstrably retained by the relevant contraction; the
correspondence is neither universal nor sufficient to characterize the priced inventory.*

## 0. Instrument defects, stated first

Three, in descending order of seriousness. **The worst is mine.**

1. **The instrument leaked the category.** My kernel-computer prompt offered
   "undetermined-by-the-flow" as an example kernel type. That phrase is co-extensive with
   "supplied input" — it *is* the definition of a priced item. All six blinded computers
   used it by name. **Any correspondence established through that category is analytic, not
   empirical**, and the comparator discounted accordingly. The blinding of *content* held
   (verified: no stripped-field value appears anywhere unreachable from a non-stripped
   field); the blinding of the *question* did not. A future run must define kernel purely
   as "provably not erased," with no undetermined-by-the-flow clause.
2. **The corpus leaked the audit's own typing in 24 of 48 rows** through the unstripped
   `primitives` field, which is phrased in priced vocabulary ("a declared input, not an
   output"; "assumed rather than derived"), plus the `known_connections` past-hypothesis
   edge and four more fields carrying "low-entropy." Computers quoted these back as
   justification. **Seven rows were discounted to NO on this ground — every one of them a
   K-U showcase instance** (past hypothesis; system–environment split; Mori–Zwanzig
   projector; local equilibrium; probability measure; relaxation direction ×2).
3. **My earlier prompt truncation** invalidated the first comparator run (2.5 of 6 kernels;
   the negative control never ran). Disclosed, discarded, re-run from disk.

**What survives these defects is what matters**, and the comparator's own observation is
the reason to take it seriously: the surviving matches concentrate in rows drawn from the
*stripped* fields — the ones blinding actually protected.

## 1. The scoreboard

- **All four candidates REFUTED as stated** (K-I, K-II, K-III, K-U).
- **25 of 48 priced rows matched** a blind-computed kernel element under strict scoring
  (15 THEOREM-grade, 10 STANDARD); 18 NO, 5 with no contraction available to test.
- **Four genuine physical counterexamples**: substrate Hamiltonian, material-specific
  inputs (the designated stress case), EFT organization primitives (*they are the
  contraction, and a contraction cannot be its own kernel*), cosmological principle
  (on both sides).
- **244 kernel elements against 48 priced rows.** Nine-tenths of the kernel is unpriced.

The guard did not fire — not every item kernelizes, and the contractions were not chosen:
they are forced by named theorems (Elitzur, Ocneanu rigidity, Hastings–Michalakis, Wald's
Bianchi-IX threshold, Albert–Jiang, Komargodski–Schwimmer, Kay–Wald, Buchholz–D'Antoni–
Fredenhagen), and several computers volunteered constraints *against their own kernels*.

## 2. The real finding: kernel-membership is necessary, not sufficient

The surplus is the headline. The 244-element kernel splits cleanly in two:

> **(i) elements the theory's own structure FIXES** — critical exponents and scaling laws,
> anomaly coefficients with A_UV = A_IR, Zamolodchikov's c-function and the a-theorem,
> Luttinger's and Kohn's theorems, the Goldstone count, parameter-free EFT corrections.
> These are *outputs*: derived, predicted, unpriced.
>
> **(ii) elements the contraction retains but the theory LEAVES UNDETERMINED** — these are
> the priced inputs.

So the corrected relation is not K-U's "priced = kernel." It is: **priced ⊂ kernel — across
the tested surviving cases, not as a universal theorem.**
Survival of contraction is *necessary* for being priced — anything a contraction erases
cannot be a standing input of the contracted description — but it is not sufficient, and
the extra condition is exactly the law/state question RRP-01 started from. **Contraction
explains WHICH information must be supplied; it does not explain HOW MUCH, and it reaches
nothing upstream of itself.**

## 3. The four classes where the correspondence is real

**A. Invariant-ring coordinates of an exact redundancy quotient — the sharpest class, where
the count is derivable.** The blinded flavor computer reconstructed the SM flavor inventory
from scratch: G_F = U(3)⁵ acting by field redefinitions, quark sector 36 real parameters
minus 26 orbit dimensions = 10, lepton sector 18 − 15 = 3, total **13 — the priced flavor
parameters, as the invariant ring**, plus θ̄ from the chiral/anomaly quotient, with the
Jarlskog invariant identified as the unique CP-odd quark invariant. Here contraction
delivers both the *identity* and the *dimension* of the priced set. This is the strongest
single result of the round.

**B. Retained coordinates of a scale or time contraction** (the "complete sufficient
statistic" class): (J(ω), β) for a Feynman–Vernon bath, exact within its model class; the
Davies on-shell γ(ω); transport coefficients and equation of state as the Chapman–Enskog
residue; relevant and marginal couplings under EFT truncation; the frozen adiabatic
amplitude after horizon exit; relic abundances after freeze-out. **This is where genuine
smallness lives — and it is local and relative**: an infinite-dimensional space of
microscopic theories reduces to a finite list. It never states the size of the list.

**C. Conserved or protected labels the contraction cannot move**: ADM charges; η_B
surviving annihilation because B−L is conserved; pointer populations under pure dephasing
(the branch-weights row, at THEOREM grade via the Schur-multiplier argument); superselection
labels; the Chern integer behind R_K; T_CMB as the label of the blackbody attractor.

**D. Relevant directions — where the map is EXPANDING, not contracting**: G, Λ, the Higgs
mass-squared, gauge-coupling boundary values. Contraction explains why these must be
supplied, and **predicts anti-smallness** there.

Three results are precise beyond what resemblance could produce: horizon exit annihilates
exactly one of two functions of initial data per mode — **explaining why the primordial
input is one power spectrum rather than two** (contraction explaining the *type* of a priced
input); Feynman–Vernon's sufficient statistic, with the on-shell dissipator separated from
the Lamb shift's off-shell functional; and the flavor invariant-ring count.

## 4. The negative control failed as a control — informatively

K-U and K-III shared the premise "flavor sector: no known contraction, and indeed not
small." **It is wrong, and the blinded computer corrected it unprompted**: as an ODE flow
at finite scale ratio, RG running in the flavor sector is *invertible* — "RG running
neither creates nor destroys basis-invariant flavor information," and reading flavor
erasure as an RG effect is "the most likely error this classification could induce." The
dominant flavor erasure is not RG at all but the **flavor-basis quotient**, exact at every
scale, acting before any running. So the control's premise dissolves: there *is* a massive
contraction there, and its kernel is precisely the priced list. This is a **hit for the
correspondence and a miss for the smallness story** — the two claims K-U had bundled, now
separated. And K-I's refuter reached the same place from the other side: the Standard Model
is the paradigm RG-organized description with 19+ parameters; **RG explains why the priced
list is CLOSED, never why it is SHORT.**

## 5. Verdict, at exactly its strength

**K-U as stated is refuted. A narrowed correspondence survives**, with this boundary:

> For a description sitting under an identifiable contraction, its priced inputs are drawn
> from the contraction's kernel — the invariant-ring coordinates of exact redundancy
> quotients, the retained coordinates of scale/time contractions, protected labels, and the
> expanding directions. Kernel-membership is necessary, not sufficient: the kernel also
> contains everything the theory derives. Contraction accounts for *which* information must
> be supplied and sometimes its *type* and *dimension* (class A); it does not account for
> smallness, and it says nothing upstream of itself or where no contraction exists.

**Not banked as established.** Grade: one round, in-house, read-level verification, with the
category-leak defect of §0 unrepaired. What would settle it: a clean re-run with the kernel
definition purged of "undetermined-by-the-flow" and the `primitives` field stripped — the
seven discounted showcase rows are the test set, and they are the rows K-U most needs.

## 6. What this does to the phase

RRP-01 asked why law fixes dynamics while selections ride the state. The round's answer is
partial and honest: **where a contraction exists, it determines which quantities *can* be
standing inputs — that is a real, theorem-grade structural constraint on the law/state
boundary, and in one class it even fixes the count.** But the residue of the original
question is untouched and now sharply located: *within* the kernel, what decides which
elements the theory fixes and which it leaves open? That is the law/state split again, one
level in — not dissolved, relocated, exactly as C-II would predict of any explanation in
this phase.

The compressibility question is **not** answered. Smallness in class B is local and
relative; class D predicts anti-smallness; and the SM's 19+ parameters stand as the
counterexample to every version of "contraction makes it small."


---

## AMENDMENT 01 (2026-09-24, owner ruling — language and verdict ledger)

Wording above adjusted per owner: "the correspondence is real" replaced by the bounded
formulation; "priced ⊂ kernel" scoped to the tested surviving cases, never a universal
theorem. Owner's recorded verdict ledger for this round: **K-U as originally stated:
REFUTED. K-U as a universal explanation of priced inputs: REFUTED. Contraction/kernel
structure as a partial correspondence with the law/state boundary: supported by the
surviving cases, not universal, not yet explanatory of the residual selection. "Contraction
explains smallness": not established** — the flavor result is a potentially important
counterpoint, not an establishment. The three-way separation is recorded as the round's
strongest output: **kernel-retained ≠ law-determined ≠ law-undetermined** — with a fourth,
type-error class (parameters *defining* the contraction — slow-variable declarations,
system/environment splits, projectors, cutoffs — are not kernel elements at all). The
carried-forward question: *why does a physical theory determine some elements of a retained
kernel while leaving others as supplied content?* Next step per owner: inspection of the
actual blinded outputs (no new campaign) — `K_ROUND_INSPECTION_01.md`.
