> **HISTORICAL PHASE PROMPT (June 2026, 13-claim era).** Retained as a build-log record; the register has since moved (see `GRUT_ToE.md` and the live gate). The numbers below are as-of-phase.

# GRUT build — Phase 2 prompt: the auditing engine (+ Phase-1 sync)

You (build chat) are back on the pen; the overseer returns to the overseer seat. We check each other — both directions. Two parts below: **(A) absorb what changed in Phase 1 — by verifying it against the actual files, NOT by trusting this summary**; then **(B) build Phase 2.** Operate under `CHARTER.md`.

---

## A. Absorb Phase 1 (verify against the workspace — do not trust this prose)

Phase 1 ("harden the earned core") was executed directly by the overseer this run. TWO new consolidation docs are in the workspace. READ them and confirm against `provenance/claims.json`:

- **`ARROW_OF_TIME.md`** — the existence/direction arrow decomposition lifted into a standalone, GRUT-independent citable note (GRUT appears ONLY in the §6 corollary; §§1–5 stand without it). Its §3 numerics were verified against `calc/arrow_origin.py`. It references the `arrow_of_time` claim; the claim's **tier is UNTOUCHED** (still `assumed`, +1 — the Past Hypothesis is the named import; it does NOT "solve" the arrow).
- **`NO_GO_LEDGER.md`** — seven banked no-gos/containments consolidated, each at its EARNED strength + a constructive spec: (1) α-bridge SETTLED-NEGATIVE, (2) μ=4/3 EMPIRICALLY-EXCLUDED, (3) economical w(z) SETTLED-NEGATIVE, (4) 689 INVISIBLE-BY-SUPPRESSION, (5) GW INVISIBLE-BY-SUPPRESSION, (6) GR BORROWED, (7) Born rule BORROWED. **The rebuild banks NO FORBIDDEN no-go** — stated honestly, because saying so is part of the discipline.
- BOTH are consolidation ONLY — **no claim added, no ledger change.** Confirm `python3 provenance/validate.py` is GREEN at **net +12** with the SAME 13 claims.

**The Phase-1 lesson you must internalize (it cost three correction rounds):** even the overseer, holding the pen, PERSISTENTLY half-reached beyond the strict register — first importing prior-lineage (v4) content (a FORBIDDEN "propagating-relic" entry + a v4 GW figure from memory), then mis-attributing real register content to the WRONG claim (the 1/k⁴/Paneitz argument belongs to `rung9a`/`rung7`, NOT `rung9b`, which explicitly fences the propagating-pole question). Independent firewall passes caught every instance; nothing wrong banked. Now binding on **both** of us:

1. **Work STRICTLY from the clean register** (`claims.json` + `calc/*` + workspace docs). **NEVER import prior-lineage (v2/v3/v4) content** — not even "marked as a forward item." If a prior result seems relevant, re-derive + bank it inside this rebuild first, or it does not exist for our purposes.
2. **Verify every number and claim against the register/code, never from memory.**
3. **The strict-register fix for an over-reach is often REMOVAL, not rewording.**
4. **Mis-attributing real register content to the wrong claim is also a leak** — cite the claim that actually grounds the statement.
5. **Every artifact gets an independent check before banking** — self-verification is not enough (proven this run).

---

## B. Phase 2 — the auditing engine (the AI seed)

Per the chosen sequence (1 → 3 → 2), Phase 2 generalizes the gate/provenance machinery into a **reusable physics-claim auditor** — the seed of the eventual responsive AI. Goal: extract the discipline engine from the GRUT-specific register so it can tier and audit an ARBITRARY claim set, not only GRUT's ladder.

Concretely:

1. **Generalize the discipline rules** from `validate.py` into a reusable module (e.g. `provenance/auditor.py`) that accepts a claim `{statement, tier, sources, overturning_computation, ledger_delta}` and a source register, and applies the SAME checks: tier ∈ the vocab; sources present and in-register; `overturning_computation` present; laundering blocked (net-positive `ledger_delta` on `shown`/`derived`/`derived-pending` without `laundering_ok`); `assumed`+positive warns. It must operate on ANY (claims, sources) pair — do not hardcode GRUT's.
2. **Keep `validate.py` working on `claims.json`** as a regression — the existing gate must still pass GREEN at +12 (have it call the generalized engine, or keep it as a thin wrapper).
3. **Tests** (stdlib-only, the rebuild's style): a clean claim passes; a missing-source claim blocks; a missing-falsifier blocks; a laundering rung (net-positive `shown`/`derived`) blocks; an `assumed`+positive warns. Mirror the existing discipline exactly.
4. **A short doc** (e.g. `RESULTS_auditor.md`) stating plainly what the auditor does and — critically — what it does NOT do.

**THE CRITICAL CALIBRATION — mark it, do not launder it:** the auditor enforces the **provenance/tiering discipline** — it checks that every claim is sourced, falsifiable, and not laundered. **It does NOT certify physical correctness.** A wrong-but-well-provenanced claim passes GREEN; the gate sums `ledger_delta` blindly and cannot catch a physics error or a double-count (as already seen with the item-#13 double-count, which rested on prose + a hand-check, not the validator). So the auditor's self-description must say, plainly: **"this verifies discipline, not truth."** That distinction is the honest core of the eventual AI — an everything-machine whose claims carry *provenance*, not one that asserts *correctness*. Over-claiming the auditor as "verifies physics" would be the exact failure mode the whole program guards against.

**Scope discipline:** this is TOOLING. It adds NO physics claim and must NOT change the ledger — **+12 stays.** It generalizes the existing gate; it does not touch the physics register's content. (Optional adjacent item, only if natural: harden the validator to assert the α-normalization cost is booked exactly once — the `#13` / suspended-credit single-count that currently rests on prose. Mark it as a separate, GRUT-specific check, not part of the generalization.)

---

## C. The model — we check each other

Build Phase 2; run `validate.py` (must stay GREEN +12) and the new tests; relay to the overseer (via the user). The overseer screens the auditor and its self-description with fresh eyes before anything is called done — especially the **"verifies discipline, not truth"** calibration and the scope (no ledger change). Relay any tier graduation or any approach to a reserved frontier UP before banking. Mutual checking, both directions.
