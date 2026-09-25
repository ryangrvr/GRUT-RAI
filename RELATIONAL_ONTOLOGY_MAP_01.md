# RELATIONAL ONTOLOGY MAP 01 — the partition attack's verdict and the (𝒜,𝒞,ρ) dependency graph

**Date:** 2026-09-25 · **Charter:** `RELATIONAL_ONTOLOGY_CHARTER_01.md`
(pre-registration frozen at `3bba895` before the run) · **Instrument:**
`calc/partition_selection_p1.py` · **Artifact:**
`PARTITION_SELECTION_P1_RESULT.json` (sha `8220a4f57074c309…`) ·
**Battery 6/6**, controls at machine precision (ring spectrum 6.2e-15,
GLE exact, Gaussian purity 2.3e-15), rigging control passed, tolerance-flip
stable. Register untouched; ledger 0; fenced routes untouched. **Toy-class
scope travels with every claim below: the exactly solvable Gaussian world;
verdicts are about the criterion class, not about reality directly.**

---

## 1. P-1 VERDICT — with an instrument disclosure first

**Disclosure (defect, not softened):** the mechanical signature printed
**B**, but B was the rule's else-branch, and the pre-registered B definition
("intrinsic criteria select only up to ties/families, coherently") does
**not describe the data**. The pre-registered A/B/C taxonomy was
incomplete: the observed pattern is a fourth thing. The mechanical output
and the taxonomy gap are both on the artifact face; nothing was reclassified
after the fact.

**What the data actually shows — a regime trichotomy, per testbed:**

- **X1 (symmetric world): clean B-behavior.** All three intrinsic criteria
  return TIE-ORBITs (translation symmetry respected to 1e-6; the rigging
  halt never fired). Note: the criteria choose *different* orbits (C1 the
  distance-2 pairs; C2 and C3 the adjacent pairs) — symmetry is respected,
  but the criteria already disagree about what "natural" means.
- **X2 (structured world — the impurity): partial A, criterion-relative.**
  The intrinsic causal-cohesion criterion **selected the impurity {0}
  uniquely, strongly (gap 0.678), and stably under coarse-graining, without
  being told it existed.** The mutual-information criterion's winner is
  also {0} but sub-threshold (gap 0.145) and cg-unstable. The kernel-rank
  criterion picked something else entirely ([7,9], gap 0.082, no
  selection). One genuine intrinsic detection; no two-criterion agreement;
  A-as-pre-registered not reached.
- **X3 (generic world): C-region behavior, CPR-consistent.** No intrinsic
  criterion selects anything (gaps 0.002–0.091); winners disagree; the
  anchored criterion also fails at |S| ≤ 2. Exactly what CPR's
  measure-zero-existence predicts for generic dynamics.
- **C4 (the anchored criterion) behaved as designed:** it selects when an
  anchor plus real structure exist (X2), and cannot manufacture a subsystem
  from an anchor alone (X1, X3 at the size cap) — anchors are necessary
  but not sufficient.

**The verdict, stated at earned strength:**

> **Subsystem structure, in the tested class, is regime-dependent:
> emergent where the dynamics genuinely distinguishes a sector (one
> intrinsic criterion found it unaided), representational where symmetry
> makes partitions equivalent, and unselected — supplied, not found — in
> generic worlds.** And the criterion class is **not univocal**: minimal
> bath-rank, minimal entanglement, and causal cohesion are inequivalent
> notions of "subsystem" that coincide only where structure is strong.

This is simultaneously less than the relational hypothesis hoped (no
universal invariant selection functional) and more than the null (intrinsic
selection is *possible* — X2 is an existence proof that a partition can be
derived from correlation structure with no anchor, in at least one regime,
by at least one criterion).

**The owner's three-way question, answered as the data allows:** not A, not
B, not C globally — **A-where-structured, B-where-symmetric,
C-where-generic**, with "which criterion" as an extra, unanticipated axis.
The NOT-SHARPER-THAN-PHILOSOPHY exit was **not** triggered: the trichotomy
is computed, threshold-stable, and control-guarded — the question is
calculable. What is not yet sharp is the *unification* of the criterion
class (see §4, P-2).

## 2. THE (𝒜, 𝒞, ρ) DEPENDENCY GRAPH

| arrow | status | basis |
|---|---|---|
| (𝒜,𝒞,ρ) → correlation structure | **DERIVED (definitional)** in any model class — correlations are what a state on an algebra under dynamics *is*; no content yet |
| correlation structure → subsystem partition | **CONDITIONALLY DERIVED** (toy-class, regime-scoped): derivable unaided where dynamics distinguishes a sector (P-1/X2, one criterion, cg-stable); **EMPIRICAL INPUT** in generic worlds (P-1/X3; CPR measure-zero); representational under symmetry (P-1/X1). The criterion-relativity is a measured fact, new to the record |
| partition → K(t,t′) | **DERIVED-GIVEN-PARTITION** — exact in the Gaussian class (the GLE kernel); KERNEL-STANDARD at field level (ROOT-1: forced by no principle); partition-dependence proven by the Wilsonian countermodel |
| K(t,t′) → stationary K(Δt) | **CONDITIONALLY DERIVED** on symmetric states only — unchanged from the transport/non-stationarity chain (R = 0.516 on the frozen grid); the relational picture *predicts* this shape but does not own it (see next row) |
| relational picture → the memory/dissipation/non-stationarity record | **CONSISTENT, NOT DISCRIMINATING (OPEN).** The K(t,t′)-primacy, state-supplied direction, and partition-dependent kernel results sit naturally in (𝒜,𝒞,ρ) — but they sit equally in a constitutive-medium reading with priced inputs. **No calculation on record distinguishes the two readings**; claiming the record as evidence for relationalism would be the flattering move the charter forbids. The distinguishing calculation is named in §4 |
| correlation structure → geometry | **OPEN**, unchanged: the 1Space sevenfold non-circularity failure stands; nothing in P-1 touches geometry; a non-circular metric-from-correlations construction remains unexhibited |
| 𝒜 commutative-classical → quantum structure | **DISDERIVED as tested** (unchanged): every audited route failed (ℏ, interference carrier, Born, outcomes); P-1's classical world selected subsystems but produced nothing quantum. On the present record, **quantum/noncommutative structure enters 𝒜 as a primitive** unless F-4 (the interference carrier) resolves otherwise. Noncommutativity itself: still UNTESTED as an emergence target |
| observer / system / environment as effective roles of one structure | **PARTIALLY SUPPORTED (toy-class) / OPEN (field level).** P-1's anchored-vs-intrinsic split makes "role" operational: an anchor buys selection only where structure permits. But the field-level record still runs the other way (CLPW: constitution FROM a supplied observer); the register's observer question remains UNPOSED |
| "substrate as representation of relational structure" (the owner's demotion) | **OPEN, with regime-scoped partial support.** P-1 shows medium-talk (a preferred S with a bath) is *derived* where dynamics distinguishes it and *conventional* where it doesn't. That is support for the demotion **in the tested class only**. The record neither forces nor forbids the demotion globally |

## 3. THE MINIMUM MATHEMATICS OF (𝒜, 𝒞, ρ) — as far as it is currently sharp

> **Reality₀ = (𝒜, 𝒞, ρ):** 𝒜 an algebra of degrees of freedom (its
> commutativity status is a free input — the record has never produced
> quantum structure from a commutative 𝒜); 𝒞 a dynamics generating the
> correlation functions; ρ the state/history selecting which correlations
> are realized. **Subsystemhood is a functional 𝔖[𝒜,𝒞,ρ], not a property
> of 𝒜** — and the measured facts about 𝔖 are: (i) inequivalent natural
> functionals exist (rank / entanglement / cohesion) and coincide only
> where structure is strong; (ii) 𝔖 selects unaided in structured
> regimes, respects symmetry orbits in symmetric ones, and returns nothing
> in generic ones; (iii) every effective kernel K(t,t′) is downstream of a
> choice of 𝔖-sector, which is why the kernel could never be primitive.

**Is this sharper than a philosophical restatement? Partially — and the
boundary is explicit.** Sharp: the subsystem question is calculable (P-1),
the trichotomy is measured, the kernel's downstream position is derived.
Not yet sharp: the unification of 𝔖 (is there one master functional?),
the field-theoretic extension (type III vs the toy's type I — the recorded
III₁ obstruction stands), geometry, and everything quantum. Per the
charter's mandate, that boundary is the finding, stated rather than
blurred.

## 4. WHAT WOULD ADVANCE OR KILL IT (named, not opened)

1. **P-2 — criterion unification:** is there a single variational
   functional whose limits reproduce C1/C2/C3, and does it inherit the
   trichotomy? If provably none exists, "subsystem" is irreducibly plural
   — itself a structural result.
2. **P-3 — the quantum lift:** repeat P-1 in a fermionic/spin class
   (finite type I but genuinely noncommutative); the recorded III₁
   obstruction predicts new behavior at the field-theory boundary.
3. **The relational-vs-medium discriminator** (the missing calculation of
   §2 row 5): find an observable whose value differs between "K is
   obtained by reduction from (𝒜,𝒞,ρ)" and "K is constitutive with priced
   inputs" — none is currently known; if none can exist, the two readings
   are a formulation choice and the demotion is representational, not
   physical (which would itself close the question honestly).
4. **The geometry leg** stays where the reconstruction put it: a
   non-circular construction or nothing.

## 5. HARD STOP

The signature, the taxonomy gap, and the map are recorded. The decision
this stop waits on: **the owner reads the regime trichotomy and rules on
the relational candidate** — adopt it as the working frame at toy-class
strength, order P-2/P-3, or reject. Λ_R, Matsubara, Π₀, U5 remain fenced;
no prediction campaign was opened; the register is untouched.
