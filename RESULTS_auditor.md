# The auditing engine — what it verifies, and what it cannot

*Phase 2 of the rebuild. The gate/provenance machinery, generalized out of GRUT's register into a reusable physics-claim auditor — the seed of the eventual responsive AI. This note states plainly what the auditor does and, critically, what it does **not** do.*

---

## The one calibration that matters: **this verifies discipline, not truth**

The auditor enforces the **provenance / tiering discipline**. It checks that every claim is **sourced**, **falsifiable**, **tiered**, and **not laundered**. It does **not** — and **cannot** — certify that a claim is *physically correct*.

A claim that is **wrong but well-provenanced passes GREEN.** The auditor has no model of physics; it has a model of *bookkeeping honesty*. Two concrete blind spots, stated so they are never mistaken for coverage:

- **It cannot catch a physics error.** A false statement with a real source, a real falsifying computation, and a legal tier audits clean. Provenance is not proof.
- **It cannot catch a double-count.** The net ledger is a **blind sum** of `ledger_delta`. If one underived input were booked as `+1` on two different claims, the sum would simply be wrong and the gate would still pass. (This is exactly the item-#13 α-normalization single-count that, in the GRUT register, rests on prose + a hand-check — see the GRUT-specific wrapper check below.)

Over-claiming the auditor as "verifies physics" would be the **exact failure mode the whole program exists to prevent.** The honest core of the eventual everything-machine is that its claims carry *provenance*, not that it asserts *correctness*. The auditor is the machine that keeps that distinction enforced.

---

## What it checks (the discipline)

For every claim `{statement, tier, sources, overturning_computation, ledger_delta}` against a source register, the engine blocks on:

| Check | Blocks when | Why |
|---|---|---|
| **Tiered** | `tier` ∉ the allowed vocabulary | every claim must carry an explicit epistemic status |
| **Sourced** | `sources[]` empty, or a source id not in the register | no unprovenanced claims |
| **Falsifiable** | no `overturning_computation` | every claim must name what would kill it |
| **Integer ledger** | `ledger_delta` is not an int | the input count must be countable |
| **Not laundered** | net-positive `ledger_delta` on `shown` / `derived` / `derived-pending` **without** `laundering_ok` | a derivation must not quietly expand the input list |

…and **warns** (non-blocking) on `assumed` + positive `ledger_delta`: a *recovery-with-imports* — legal, but it must be labeled a recovery, never sold as a derivation.

The default tier vocabulary is `{shown, derived, derived-pending, assumed, to-derive}`. The win condition is a **short, marked** list of inputs, not zero — every `+1` is flagged in the open, not hidden.

## Architecture

- **`provenance/auditor.py`** — the **generalized engine**. `audit(claims, source_ids, valid_tiers=DEFAULT_TIERS)` and `audit_claim(claim, ...)` operate on **any** `(claims, sources)` pair with any tier vocabulary. Nothing here is GRUT-specific. Pure: it returns an `AuditResult` (`blocking`, `warnings`, `net`, `rows`) and never prints or exits — callers decide.
- **`provenance/validate.py`** — the **GRUT-specific gate**, now a thin wrapper: it loads `claims.json` + `sources.json`, calls `audit()`, prints the report, sets the exit code, and runs one **GRUT-specific** ledger invariant kept deliberately *out* of the generalized engine:
  - *α-normalization single-count*: the adopted `c₀` normalization (`rung9b_bridge`) must carry **no** positive `ledger_delta`, because that cost is already booked once as the **suspended rung-9 anchor credit** (`rung9a_value` at 0 / dependency-ledger item #13). This closes the one double-count a blind sum cannot — but only for this register; it is **not** a general truth-check and does not live in `auditor.py`.
- **`provenance/test_auditor.py`** — stdlib `unittest`. Mirrors the discipline exactly: clean passes; missing/unknown source blocks; missing falsifier blocks; invalid tier blocks; laundering blocks (and `laundering_ok` exempts); `assumed`+positive warns, not blocks; the engine works on a **non-GRUT** claim set with a custom vocabulary; and a **regression** that the live GRUT register still audits GREEN at **net +12** with 43 nodes.

## Scope — tooling only

This phase is **tooling**. It adds **no physics claim** and changes **no ledger entry**: the GRUT register is untouched and `validate.py` still passes **GREEN at net +12** with the same 13 claims. The auditor *generalizes* the existing gate; it does not touch the physics register's content. The eventual AI inherits this engine — and inherits, with it, the discipline that its outputs are *provenanced*, not *certified true*.

## Reproducibility

```
python3 provenance/validate.py        # the GRUT gate: GREEN, net +12, 43 nodes
python3 provenance/test_auditor.py     # 16 discipline tests, all green
```
Pure Python stdlib; no third-party dependencies.


*Sync note (2026-08-02): the run-now expectations above are as-of-phase; for the live count and net, see the `GRUT_ToE.md` header and changelog (REGISTER-SYNC-guarded).*

---

## Standing note (2026-08-09, overseer-ordered): the verification asymmetry

Recorded at the overseer's own instruction, against themselves. Five wrong conclusions from
greps in one session: retirement text read as live text; the wrong layer for the fitted floor;
the wrong directory for the protocol; hash-vs-filename ordering; and a check for one subfield's
vocabulary in another subfield's document, whose absence was read as "the observable was never
specified" — a finding that, acted on, would have held a ready dispatch and made it worse.

Same shape every time: **a check that tests for the wrong thing returns a confident wrong
answer.** The builder's calcs carry mutation batteries that make exactly this fail loudly — a
selftest that cannot catch a wrong answer is treated as decoration (`provenance/
mutation_registry.py`). The overseer's checks carry nothing equivalent: no pre-registered wrong
answers, no control that the probe would detect the thing it claims to test for. That asymmetry
is now on the record. Practical consequence adopted with it: an overseer verification that
gates an action (holding a dispatch, reversing a builder resolution) should state what result
would have confirmed the artifact was CORRECT — if the probe cannot say what a pass looks like,
it is a grep, not a check.

*Continuation (2026-08-10): the asymmetry above acquired its first mechanized battery. An
outside review of the sealed termination condition v2 found it MISQUOTING the register's own
rung7 overturning clause — in the flattering direction, invisible to seven rounds of internal
review, because every internal pass audited the document's structure and none audited its
citations of the register. The response is structural, per the standing rule that a new guard
must name the physics it protects: `provenance/test_register_citations.py` verifies, both ways
and whitespace-normalized only, every registered (artifact, node, field, verbatim-quote) tuple —
and its bite test proves it catches the actual v2 defect. The program now audits documents'
claims ABOUT the register, not only documents against the register and the register against
itself.*
