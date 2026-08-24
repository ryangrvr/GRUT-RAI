# Wall A — next session state (honest boundary)

**Date:** 2026-08-23 late · A5 FULL PASS · A2 Phase 2 implementation deferred to fresh capacity.

## Why stopping here

Routes A and B for the 6→3→2 verification are well-specified but require clean exact-arithmetic
code that I cannot reliably produce right now. Three attempts produced fragmented files due to
tool corruption and my own fatigue-induced errors. Per this session's own discipline: stop rather
than ship something broken.

## What the next session implements

**Route A** — coefficient algebra over six BR structures. Apply retarded-slot Ward, then S7.
Expected: 6→3→2.

**Route B** — independent exact tensor linear algebra. Build general covariant kernel from
{η,k}, impose Ward as Fraction linear constraints, compute nullity independently.

Both routes must agree. Plants included (both-slot Ward, no-Ward). No known-answer targets.

## Licensing deliverables

A: exactly-two = diagonal Ward + S7 reciprocity (currently unbooked — flagged).
B: c₀=0 is NOT licensed by any symmetry; EH counterexample stands.

## Key parameters for implementation

k = (5,4,2,1), k² = 4, all rational. Six BR structures span a 6-dim space at fixed k.
Ward constraint: k_μ K^{μν,αβ} = 0 on retarded slot only.
S7 pair symmetry kills the transfer operator P⁰sw (its transpose P⁰ws is not Ward-viable).

## Standing fences (unchanged)

W-0 · +1 discharge outside builder authority · blinding · interleave contract · ledger hygiene.