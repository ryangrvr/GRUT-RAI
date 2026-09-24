# RRP_03_CONCEPTUAL_PASS_01 — formalizing the recursion before testing it

**Date:** 2026-09-24. **Grade: CONCEPTUAL, UNCHALLENGED — nothing banks.** Inline, main
session. Purpose: define the map class and the candidate invariant precisely enough to
attack; state the null models; and record two pre-audit observations that materially
shape the fork.

## 1. The objects and the map class 𝔐

**Objects:** audited descriptions D = (framework presentation P; typed supplied-content
ledger L(D) — the per-map ledgers the program already produces; accounted empirical
record R(D) ⊆ the corpus). The program now holds ~14 concrete ledgers: the eight
reconstruction rows (RRP-01 C-II table), the six S-audits, and the K-round exemplar maps.

**Maps:** m: D → D′ is admissible (m ∈ 𝔐) iff it is **record-preserving**:
R(D) ⊆ R(D′) with the shared record accounted compatibly (same measured values on the
presentation-absolute images — RRP-01 Route 1's invariant). Three sub-classes, to be kept
typed: **reformulations** (R equal; presentation changes — the Route-1/2 class),
**extensions/deepenings** (R(D′) ⊇ R(D); T′ claims to derive parts of D's specification —
the RRP-02 class), **scoped reductions** (R(D′) ⊊ R(D) deliberately — EFT decoupling;
these are *not* eliminations and must be firewalled from them, see §3).

## 2. The candidate invariant, stated as an order property

Define a **typed comparison** on ledgers: L(D′) ⪯ L(D) iff there is a type-honest
correspondence under which every supplied item of D′ maps into the supplied content of D
with no unpaid remainder (the operational content of every audit already performed). A map
m is **strictly reducing** iff L(D′) ≺ L(D): strictly less supplied content, type-honest,
payment ledger closed. Then:

> **(II″) — the invariant candidate:** *𝔐, restricted to the audited record, contains no
> strictly reducing maps.* (The class-4 gate, restated as an order-theoretic property of
> the category of audited descriptions over the fixed corpus.)

**Known formalization risks, named at birth:** (i) the order may be too partial —
if almost all ledger pairs are incomparable, (II″) is vacuously true and therefore
ill-posed as an invariant (this is the NOT-FORMALIZABLE-TYPE-MIXED verdict biting one
level up; finding it would itself be a Branch-1-flavored result); (ii) "type-honest
correspondence" must be definable from the existing audit practice without consulting the
desired verdict (the computed-independently discipline applied to the order itself).
The formalization attack tests both on the actual 14 ledgers.

## 3. Two pre-audit observations that shape the fork (TO-VERIFY at source in the round)

**Observation A — the recursion appears to hold in pure logic, at the sharp grain.**
Logic's flagship elimination — second-order categoricity (the model of arithmetic pinned
uniquely, "which model" apparently *eliminated*) — is, on the standard critique, a
**relocation to the metatheory**: the categoricity theorem consumes the full semantics of
second-order quantification, i.e. the supplied content moves into the background set
theory (Väänänen's line — verify at source). Reverse mathematics is literally derived
implication-structure on axiom-space with the adopted subsystem supplied (the RM Zoo,
already screened in CONTROL6). If this observation survives verification, **Branch 1 is
live at the coarse grain**: even mathematics exhibits derive-structure/supply-point/
relocate-under-reformulation.

**Observation B — but formalism's "eliminations" are scoped, exactly like physics's.**
Conservativity results (WKL₀ over RCA₀ for Π⁰₂ — verify) eliminate an axiom *relative to a
theorem class*, precisely as EFT decoupling eliminates heavy content *relative to
low-energy observables* (Appelquist–Carazzone, already in the corpus). Both are
scoped-irrelevance, not specification elimination — the supplied item persists in the full
system. If B holds, then **the null model does not actually contain the thing whose
absence in physics we were treating as remarkable** — genuine elimination may be absent
from formal description as such. That reading *supports* Branch 1 (architecture) — but it
sharpens what Branch 2 would require: a **discriminant**, something quantitative the
physics instances have that generic specification systems lack.

## 4. Candidate discriminants for the hunt (each with its kill condition)

- **D1 — derivable image dimensions/counts:** physics's forced factorizations deliver the
  *size and stratification* of the supplied space as theorems (13 flavor invariants;
  rank-one per mode; Δ^{n−1}). Kill: exhibit generic formal systems whose configuration
  spaces come with equally forced, derivable dimension theory (type-theoretic universes?
  compiler config lattices? — if commonplace, D1 is not a discriminant).
- **D2 — type-conversion directionality:** in the audited physics ledgers, compression
  payments show a pattern (discrete → continuous + structure debt, SO(10)). Kill: show
  the pattern is an artifact of which maps physicists happen to build, or exhibit the
  reverse direction on the record.
- **D3 — empirical anchoring:** physics ledgers are pinned to a measured,
  presentation-absolute record; formal-system "ledgers" float free. This is a real
  disanalogy but risks being definitional (physics ≝ the anchored case). Kill: state D3
  non-circularly or concede it is the definition of the subject, not a discriminant.
- **D4 — no-free-completion:** in the audited record, every structure-derivation consumed
  *physical* content (couplings, states, selections), never only logical content. Kill:
  a physics instance whose entire payment is metatheoretic/logical.

## 5. The round (four instruments, bounded)

1. **Formalization attack** on (II″) against the 14 concrete ledgers: build the order,
   report comparability statistics honestly, adjudicate vacuity.
2. **Logic null model**: verify Observations A and B at source (Väänänen-class;
   conservativity theorems; RM Zoo structure); adjudicate whether the recursion holds in
   pure formalism and whether genuine (unscoped) elimination exists anywhere in logic.
3. **Engineered-systems null model**: specification stacks with no physics (language/
   compiler/protocol layers): does derive-structure/supply-point/relocate hold trivially?
   What is demonstrably absent versus the physics instances (feeding the discriminant
   hunt)?
4. **Discriminant hunt**: D1–D4 (and any found), each adjudicated with its kill
   condition; default to NOT-A-DISCRIMINANT when uncertain.

Branch verdict by the main session afterward. If Branch 1: the recursion is recorded as a
description-architecture phenomenon, the branch closes, and what remains of RRP is the
audited physics content itself. If Branch 2: the surviving discriminant is stated at
recorded strength — and only then does "what fixes S" reopen, carrying that discriminant
as its first constraint.
