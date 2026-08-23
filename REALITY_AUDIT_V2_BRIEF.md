# REALITY AUDIT V2 — load-bearing chain forensics

*Owner brief 2026-08-23 carried in full; additions marked **[ADDED]**. Supersedes nothing —
`REALITY_AUDIT_CHARTER.md`, `REALITY_AUDIT_BRIEF.md` and V1's outputs all remain in force.*

---

## [ADDED-A] THE STANDING NUMERICAL RULE — now permanent, and wider than matrices

> **Any numerical statement describing repository state must be EMITTED from a machine-readable
> artifact, or independently verified immediately before publication.**

Covers: node counts · tier counts · blast radii · percentages · test totals · PASS/FAIL counts ·
date and version claims · **and any "X of Y" sentence**.

Three emitters exist and one of them must be the source: `emit_public_numbers.py` (register),
`emit_gate_status.py` (gates), `emit_audit_matrix.py` (audit). **This is a reproducibility rule,
not a style rule.** Five failures in one stretch established that.

### [ADDED-B] Analyse the five drift events; do not merely preserve them

The owner's step 3 says preserve them as immutable history. **Also analyse them, because they are a
dataset and the direction matters.** Preliminary reading, to be checked rather than accepted:

| # | drift | direction |
|---|---|---|
| 1 | "factor 2/π² correct" after correction | re-asserted a superseded state |
| 2 | "C1 4/5" when it was 5/5 | **understated its own success** |
| 3 | "27 untracked files" on a clean tree | stale, neutral |
| 4 | "C1 primitive DEBUG-IN-PROGRESS" at 6/6 | **understated its own success** |
| 5 | matrix totalling 72 | over-counted findings by one |

**They are NOT uniformly self-favouring — two understate the builder's own passing results.** That
matters: it argues the mechanism is genuine stale-read from a long uninterrupted run, not motivated
reasoning, and the repair is therefore mechanical (emit) rather than dispositional (try harder).
**Confirm or overturn this reading and record it.** If the drifts turn out directionally biased
after all, that is a different and more serious finding.

---

## THE CHAIN (owner's steps 4–6, 8–9)

    background_time_translation_flow  ->  rung1_inin_action  ->  rung2_kms_gate  ->  (25 more)
    union = 28 of 71 nodes            [emitted, not typed]

### [ADDED-C] The three hypotheses need DISCRIMINATORS, not just names

The owner's three possibilities for the root are the right partition. They are useless without a
test that separates them. Here are three, in increasing cost:

**H1 — genuine logical dependence.** Removing it breaks a specific *derivation step*, and you can
point at the line that fails.
**H2 — registry architecture.** Removing it breaks *edges* but no derivation; the physics goes
through unchanged and only bookkeeping breaks.
**H3 — an unrecognised physical assumption wearing infrastructure's clothes.** There is a world in
which it is false and the physics differs.

**DISCRIMINATOR 1 (cheap, run it first) — the use-vs-cite test.** The node books that the background
carries a time-translation flow, whose entire purpose is to make a *single-frequency* kernel
`K_R(ω,k)` definable. So: **for each of the 28 dependents, does its CONTENT use a one-frequency
object, or does it merely CITE the node?** Grep the dependents and their calc files for `omega`,
`K_R(`, Fourier/spectral objects, `chi(`, pole/cut language.

- dependents that manipulate ω-space objects → **H1** for those
- dependents that cite it with no ω-object anywhere → **H2** for those
- **Expect a mixture. Report the split as a number, emitted.** If most of the 28 are cite-only, the
  root's reach is architectural and the "39%" headline needs immediate restatement.

**DISCRIMINATOR 2 — the counterfactual-world test for H3.** Name a physically admissible background
with *no* global time-translation flow (a generic FRW with time-dependent H is one; de Sitter in
flat slicing has no global timelike Killing vector at all — which is what the keystone map's D2/D3b
already establish). Then ask: **does GRUT's content change there, or only its formalism?** If the
physics changes, the node is H3 and its `assumed` tier is correct but its `sub_status` disclaimer
("NOT a physics claim about de Sitter") is wrong.

**DISCRIMINATOR 3 — the recompute test.** For two or three H1 dependents, actually redo the step
without assuming the flow. Does it survive in a two-time form `K(t,t')`, or does it fail?

### [ADDED-D] "Delete-one" needs a defined operation — three exist and they disagree

The owner's step 6 says remove the node and rebuild the closure. **For an `assumed` node there are
three different removals, and they give different answers.** Pick per purpose and say which:

| operation | meaning | answers |
|---|---|---|
| **DELETE** | the claim is absent | architectural reach (H2 test) |
| **NEGATE** | assume ¬X and see what survives | whether dependents secretly require X |
| **UN-ASSUME** | X must now be derived or dependents become conditional | **the minimum-core question** |

**UN-ASSUME is the operation the owner's real question needs.** Deleting an assumption is not the
same as declining to grant it. Run UN-ASSUME for the core question and DELETE for the reach test;
report them separately and never merge the counts.

### [ADDED-E] Step 7's split must be typed before it is priced

Split `rung1_inin_action` into **R1-FORMALISM** (single SK influence action, K_R + N, doubled
fields — borrowed and `shown`: Schwinger 1961, Keldysh 1964, Feynman-Vernon 1963, Calzetta-Hu) and
**R1-ONTOLOGY** (the gravitational vacuum *is* a responsive medium with finite memory — a stance,
by the node's own `ledger_note`). Do not bank.

**[ADDED] And do not propose the Δ4 allocation.** Which part carries the +4, and whether the split
moves the net, is a register decision with ledger consequences. **Report the split's SHAPE and leave
the price to the owner.** A split proposed with a price attached is a ledger edit wearing an
analysis's clothes.

**[ADDED] Then re-run the reach on the split pair.** If most of the 27 depend on R1-FORMALISM and
few on R1-ONTOLOGY, the program's weight sits on borrowed physics and the stance is nearly free —
which would be the single most important thing this audit could establish. **The reverse is equally
possible and equally publishable.**

---

## [ADDED-F] The minimum physical core — and it may be EMPTY

The owner's reframe: *what is the minimum physical core left after removing every unsupported
assumption?* That is the right question and it needs one fence before it is asked.

**Pre-register now: the core may be empty, or may consist entirely of borrowed physics with no
GRUT-specific remainder.** The register carries **zero** nodes at tier `derived`; its 10 `shown`
nodes are borrowed by construction; both root novelty candidates dissolved; every empirical
differentiator died. **An empty or wholly-borrowed core is a legitimate, expected, publishable
result — and finding one would be more valuable than a small manufactured remainder.**

State the core three ways: (i) what survives UN-ASSUME; (ii) of that, what is GRUT-specific rather
than borrowed; (iii) of that, what is not already predicted by a competitor framework. **(iii) is
the number that matters and it has never been computed.**

## [ADDED-G] A stopping rule for step 10

"Recursively audit the highest-blast-radius dependents" is unbounded. **Stop when either: blast
radius falls below 3, or every dependent of the node is already UNRESOLVED-BLOCKED** — auditing a
node whose dependents cannot be graded adds nothing. Report where you stopped and why. The owner's
own instruction stands above this: *do not let this become an endless bookkeeping project.*

---

## The owner's brief, in force

1. `REALITY_AUDIT_RESULTS.json` and the emitted matrix are authoritative.
2. No hand-typed numerical summary (now [ADDED-A], permanent and wider).
3. Preserve V1 and the five drift events as immutable history (and analyse them, [ADDED-B]).
4. Fully adjudicate the three-node chain.
5. Per node: exact physical proposition · physics/formalism/bookkeeping/interface · evidence class ·
   exact scope · direct, indirect and prose dependents.
6. Sandbox delete-one per node, reporting register nodes losing support · physical claims losing
   support · claims independently supported · claims becoming ASSERTED (see [ADDED-D] for which
   removal operation).
7. Split rung1 into R1-FORMALISM / R1-ONTOLOGY; do not bank (see [ADDED-E]).
8. Determine whether the root's 28-node reach is logical dependence, registry architecture, or both
   (see [ADDED-C]).
9. Determine whether `rung2_kms_gate`'s downstream support actually requires rung1 or can be
   established independently.
10. Only then recurse into the highest-blast-radius dependents (bounded by [ADDED-G]).
11. Generated emitters for ALL numbers.
12. **Keep the 65 blocked until the missing instruments exist. Do not lower the standard to fill the
    table.**

**The V1 verdicts that stand:** rung1 HOLDS-NARROWER with the SPLIT owed · the chain at 28 of 71 ·
zero DOES-NOT-HOLD · 65 UNRESOLVED-BLOCKED upheld.
