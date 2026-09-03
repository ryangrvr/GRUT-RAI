# H¹ CAMPAIGN — STAGE 2B.4.1: THE PROTECTION-2 OBJECT, FROZEN

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_stage2b41_freeze.py` ·
**Artifacts:** `WALL_KR_H1_STAGE2B41_RESULT.json` + **`WALL_KR_H1_P2_OBJECTS.json`**
(716 KB, sha `1b136cd4…`) · **Battery: 15/15, zero failures.**
**2B.4.1 only — the dissection stages (2B.4.2+) were not entered.** Read-only on frozen
artifacts; register sha256 identical pre/post; A-F unselected; nothing banked. W-0.

## WHAT WAS FROZEN

Derived from scratch on the frozen `assemble()` machinery (Stage-1 cache never read):

| object | content |
|---|---|
| `Sigma0_flat` | flat assembly, H-free |
| `B_lines` | O(H) of the H⁰-vertex × full-W assembly — 270 raw terms (matches 2B.1) |
| `B_pureconf` | −2(u+u′)·Σ⁰_flat |
| **`B_mixed`** | **B_lines − B_pureconf — 292 raw terms, stored PRE-simplification** |

Gates: B_mixed is nonzero raw; vanishes phase-merged (the Protection-2 zero, reproduced here
from scratch — recorded as consistency with accepted 2B.1 evidence, not as an input); the
stored srepr round-trips byte-faithfully; H⁰ consistency holds; machinery provenance recorded
by sha.

## ONE OBSERVATION FOR THE DISSECTION (recorded, not pursued)

**B_mixed's free symbols are exactly {d, ω, q, u, u′}** — the internal frequencies ν₁, ν₂ are
already consumed as derivative eigenvalues, and no Δ-form has been imposed. The routing
dissection therefore operates on a d-parameterized (ω,q) structure with endpoint polynomials,
which is a smaller search space than the raw tag suggested.

## STOP CONDITIONS

None fired: same frozen machinery file (sha-recorded), B_mixed reconstructed exactly, no
assumption introduced. Protection 1 was **not** rerun, per the order.

## VERDICT: DEFERRED — PROTECTION2 status not adjudicated at 2B.4.1.

## W-0 STATUS — Protection-2 object frozen for dissection; no low-frequency physics; A-F unchanged; nothing banked.
