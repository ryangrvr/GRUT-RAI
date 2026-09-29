# L0-1 FLOOR — O-7 ADJUDICATION 01 (proposal for owner ruling)

**Status: PROPOSAL.** O-1 … O-6 are all terminal (T5 precondition met;
`L0_1H_OWNER_RULING_03.md`). This document adjudicates the frozen
two-property hypothesis from those six records **exactly as they
stand.** No new computation was run.

It supersedes the provisional draft
`L0_1_FLOOR_SYNTHESIS_DRAFT_01.md`. That draft's §3 (no-patching rules)
and §3a (the owner's reading and the binding method) carry over
unchanged.

**The method (binding, owner):**
- **O-2 result → O-7**, never the reverse.
- O-7 is **an accounting exercise**: *what is the smallest structural
  statement that survives all of the deletions and counterexamples?*
  It is not "what theory accommodates everything?".

## §0 The terminal record

| Obligation | Label | What it earned (recorded scope) | Ruling |
|---|---|---|---|
| O-1 D-HERM-a | CLASS-SPLIT | Zero-affinity asymmetry leaves response CM intact; cycle affinity breaks it at every declared member. **Asymmetry ≠ the relevant distinction.** | `L0_1D_OWNER_RULING_01.md` |
| O-2 D-HERM-b | **FALSIFIED** | Accretivity does not carry monotone retained response. H2-m falls to P-1; H2-s falls to exact counterexamples; H2-n holds independently. **Certified w\* < d_acc < d_mono at 8 g.** | `L0_1H_OWNER_RULING_03.md` |
| O-3 D-DET-a | DISCHARGED | With FDT held, determinism is not load-bearing (identity-grade). Primitive vs derived noise is unformulable at second order (S-1). | `5888965691` |
| O-4 D-DET-b | CLASS-SPLIT | Correlation CM is a convex cone in temperature space with FDT in its interior. **Placement, not the size of the detailed-balance break, decides.** | `5893630527` |
| O-5 D-ORD-a | DISCHARGED | Strict-Lyapunov structure is sufficient for derived order; recurrence obstructs it (Conley). The generator is presupposed (S-5). | `5893871264` |
| O-6 D-ORD-b | FALSIFIED | Strict ordering fails in the conservative split: no state-function order, an initial slip, and band-edge reversals. **Emergent dissipation ≠ emergent strict ordering.** | `5895858851` |

## §1 What O-2 moves (read first, per the binding direction)

**(i) The passivity → positivity row of the ingredient ledger.** It
said "necessity-certified (symmetric case; the non-normal distinction
is O-2)". It now reads:
- **Necessary for monotone retained response** (the (b) component):
  - L0-1a, symmetric case;
  - H2-n, at O-2's scope: every stable, non-accretive member is
    non-monotone.
- **Not sufficient:** H2-s falls. Strictly accretive members exist whose
  retained response rises.
- **Spectral stability is weaker still** (P-2: the band is non-empty).

This is accounting. It does not alter O-2's label (owner ruling 03:
H2-n rescues nothing).

**(ii) P_positivity is not one property.** In O-2's family:
- component (a), nonnegativity, holds at every member (Metzler
  identity, J-3);
- component (b), monotone decrease, **switches at d_mono** (J-6 plus
  the appendix).

In O-1, component (c), complete monotonicity, switches with cycle
affinity. The components have **different boundaries.**

**(iii) Clause DB on the generator route.**
- Across O-2's family, the detailed-balance status is **fixed**. Every
  ring edge is one-way (K_ij·K_ji = 0), so the Kolmogorov cycle
  criterion fails at every member, independent of d. That is
  construction data, not a result.
- Yet component (b) **switches** across d_mono.
- So **even on the generator route, detailed-balance status does not
  decide (b).**

*Operator flag, for the owner to accept or strike:* this reading uses
only the family's construction data and the O-2 certificate. It does
**not** use the affinity line (J-4, CM), which stays outside O-2 and
unregistered. If the owner judges that even this use contaminates the
separation, strike (iii), and clause DB reverts to the O-1/O-4 reading
alone. §3's proposed label does not depend on (iii).

## §2 The clauses (frozen wording unchanged)

> "the floor's three formulability obligations reduce to two deeper
> structural properties: **dissipation (for ordering)** and **detailed
> balance (for the generator and noise structure).**" (design §2)

**Clause D, "dissipation (for ordering)": CLASS-SPLIT** (unchanged from
the provisional draft; O-2 could not move it).
- **Holds:** primitive dissipative generators (O-5). Strict-Lyapunov
  structure gives derived order.
- **Fails:** emergent dissipation in the conservative split (O-6).
  Decay and memory appear, but strict order does not.
- Both sides are certified.

**Clause DB, "detailed balance (for the generator and noise
structure)": CLASS-SPLIT by route and object, with an unreduced
generator-route residue.**
- **Decisive:** generator route, response object, component (c) (O-1).
- **Not decisive:** noise route, correlation object (O-4). Placement
  decides there.
- **Unreduced residue** (O-2, via §1(iii), if the owner keeps it):
  component (b) on the generator route switches at fixed
  detailed-balance status.
- **The D-HERM obligation does not reduce to detailed balance.** Its
  second leg (O-2) concerned passivity. The passivity notions failed to
  carry the property, and the boundary that does govern it (d_mono) is
  not a detailed-balance boundary.

## §3 The hypothesis as a whole: proposed label

**Proposed: O-7 = FALSIFIED.** The frozen hypothesis is a *reduction*:
three obligations reduce to two properties. The record does not merely
qualify that reduction. It contains certified property boundaries that
neither named property accounts for:
1. **O-2:** a positivity component (b) with a certified boundary strictly
   inside accretivity, at fixed detailed-balance status. Neither the
   dissipation-type notions (accretivity, stability) nor detailed
   balance decides it.
2. **O-4:** correlation positivity decided by placement, with the
   magnitude of the detailed-balance break explicitly **not** deciding.
3. **O-6:** dissipation present (emergent) with ordering absent, on the
   frozen, unqualified wording "dissipation (for ordering)".

Each failure is certified at its scope. Under T2, FALSIFIED means the
frozen hypothesis failed a clean gate, and (1) is an exact gate.

**The alternative, stated fairly: CLASS-SPLIT.**
- The reduction "holds" in the reversible, primitive-dissipative
  subclass and fails outside it.
- **Why the operator does not recommend it:** on the reversible side,
  every obligation's live content is absent by identity (F-1, F-5/F-6,
  F-3). So "holds" there is not a certified holding of the reduction.
  It is the reduction's premises being vacuous. T2's CLASS-SPLIT
  requires *both* sides certified.

**The label is the owner's.**

**The patches the no-patching rule forbids** (each would be a new
hypothesis, not a rescue):
- adding a third property, e.g. "damping rate relative to transport",
  to cover d_mono;
- re-reading "dissipation" to mean "primitive strict-Lyapunov
  structure" (that is S-4, and needs a T4 ruling);
- re-reading "detailed balance" as "placement of nonequilibrium
  structure relative to the access site". The owner flagged the
  relational theme "very carefully" as interpretation, not a result.

## §4 The smallest structural statement that survives

Stated only from certified lines, at their recorded scopes:

> **At the floor, the retained-site description has no single deep
> organizing pair. Its behavioral properties factor across distinct
> structural ingredients, each with its own certified boundary. The
> certified relations among them are almost entirely non-implications.**

**The boundaries** (property ← ingredient that sets it, at its scope):

| Property | Boundary set by | Grade | Source |
|---|---|---|---|
| finite memory | spectral gap | necessity-certified | L0-1a |
| geometry | locality (not response) | split certified | L0-1b |
| exact reduction | linearity (only) | certified | L0-1c |
| positivity (c), response CM | cycle affinity (not asymmetry) | class-split certified | O-1 |
| positivity (c), correlation CM | noise placement relative to the retained site (not detailed-balance magnitude) | class-split certified | O-4 |
| positivity (b), monotone retained response | a boundary d_mono **strictly inside** accretivity, which is strictly inside stability | certified at 8 g | O-2 |
| derived strict order | primitive strict-Lyapunov structure (sufficient); recurrence obstructs | theorem | O-5 |
| orientation of order | the generator's sign (presupposed) | theorem-face | O-5; S-5 |
| any nontrivial conservative-class order | a restricted initial class (**forced**, not sufficient) | identity + falsified | O-6 |

**The certified non-implications** (the owner's list, with O-2 added):
- linearity ⇏ memory;
- locality ⇏ memory;
- asymmetry ⇏ irreversibility-relevant structure;
- noise nonequilibrium ⇏ correlation failure;
- effective (emergent) dissipation ⇏ strict ordering;
- past hypothesis ⇏ arrow at t = 0;
- **spectral stability ⇏ accretivity ⇏ monotone retained response**
  (O-2).

**Presupposed, not derived:** the generator itself (S-5), and whether
noise is primitive or derived (S-1, unformulable at second order).

**The reversal diagnostic** (quarantined, pre-registered Level-0
synthesis test; not evaluated here). Status only:
- the floor produced **no property → ingredient edge**, because no
  obligation could by construction;
- the composed dependency graph remains **acyclic**.

A reversal would have to appear as a new dependency from constructive
post-floor work, not as an interpretation of this table (owner ruling
02, §2).

## §5 Successor items O-2 raises (T4; proposed additions)

- **S-7: What sets the monotone boundary d_mono?**
  - The ring-lap attribution (untested).
  - The characterization of d_mono(g) beyond the certified lower bound.
  - Other n, a, and sites.
  - Whether d_mono < d_acc ever occurs in any class (the appendix could
    not certify that direction).
- **S-8: The affinity line.** The one-way ring breaks CM at every g > 0
  (J-4). The owner allowed pre-registering it "later, as its own line",
  and it must not contaminate the passivity question.

## §6 After the ruling

- **If the owner rules O-7:** the floor is COMPLETE (T5).
- **The deposit** is filed as one document: the terminal label of each
  of O-1 … O-7, and the successor list S-1 … S-6, plus S-7 and S-8 if
  accepted.
- The broader investigation stays open beyond that boundary (T6).

**HARD STOP** pending the owner's ruling on O-7's label, on §1(iii),
and on S-7/S-8.
