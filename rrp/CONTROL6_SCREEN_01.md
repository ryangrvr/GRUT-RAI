# CONTROL6_SCREEN_01 — prior-art screen before engine software (RRP Stage 3 gate item)

**Date:** 2026-09-23. **Mandate:** `TOE_LAB_CHARTER.md` CONTROL 6 — screen Metamath, Lean,
reverse mathematics, and the RM Zoo before building generic-lab software ("Building a generic
ToE lab without it risks rebuilding something that has existed for three decades").

**Screened (web-verified 2026-09-23):**
- **Reverse Mathematics Zoo** (rmzoo.math.uconn.edu): a database of implication and
  non-implication relations between formal principles over subsystems of second-order
  arithmetic; compiled from a plain relations file by an updater; derived relations deduced
  mechanically (the "s-logic" line: arXiv:1512.08035, arXiv:1412.2022, arXiv:1602.02270).
- **Metamath / Lean** (`#print axioms`): axiom-dependency tracking over machine-checked
  formal proofs.

**Verdict: NO DUPLICATION.** The RRP corpus and correspondence layer operate on *cited
physical claims with provenance classes*, not on formalized theorems with machine-checked
derivations; the objects and the certainty model differ in kind. Two adopt-don't-rebuild
consequences are binding on Stage 3:

1. **Adopt the RM Zoo architecture pattern**: correspondences are declared in plain data
   files; anything derived from them is computed mechanically by an updater; the tool is a
   declaration-schema-plus-validator and **never an adjudicator** (matching the in-house
   `merge_criterion.py` self-limitation).
2. **If Stage 4 ever requires formal verification of a claimed equivalence or derivation,
   use Lean/Metamath as external tools** — do not build proof machinery inside RRP.

Scope note: this screen covers the Stage-3 validator/engine class only. Any future module of
a different class re-screens under its own capability contract.
