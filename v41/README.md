# GRUT-RAI v4.1 — the honest, forward-derived rebuild

**Foundation first, then house.** A clean-room rebuild that contains only what
survived adversarial verification, built so an outside physicist — handed the
registry — can see *in one pass and without trusting us*: what is **derived**,
what is **anchored**, what is **open**, what is **borrowed**, and what would
**falsify** each forward claim.

This package does **not** import the v4 `grut/` code. It is a fresh kernel.

## The gate is the product (Principle 0)

`gate.py` mechanizes the tier rules. `ci_check.py` fails the build (exit 1) on any
violation. A claim is `gate.Claim{ id, statement, tier, inputs[], derivation_ref,
check, novelty, ... }`. Tiers: `ANCHOR · DERIVED · HOSTED · FORBIDDEN · OPEN ·
CONJECTURAL`. Enforced rules:

1. **DERIVED requires a `derivation_ref` AND a passing runnable `check` AND a novelty tag.** No exceptions; a check that returns non-`True` or raises is a fail.
2. **Anti-laundering:** a DERIVED claim may not *consume* an `OPEN`/`CONJECTURAL` input. (α and single-pole-ness are OPEN, so nothing built on them can be DERIVED until they close.)
3. **`OPEN` must name a computable `target`** that would close it.
4. **No claim is `RESOLVED` while its blocker is open.**
5. Every input must exist in the registry.

The proof that the gate *works* is `tests/test_gate.py` — it builds deliberately
laundered claims and asserts the gate rejects each. (Executable evidence is the
only kind that counts: not "it sounded rigorous," not multi-agent agreement.)

### One deviation from the brief, flagged

The brief's literal rule — "consumes an OPEN/**ANCHOR** input ⇒ not DERIVED" —
would empty the DERIVED set, because Q and μ_linear=1 derive from the CTP action,
which the brief itself tags ANCHOR. So:
- the **hard anti-laundering bite is on OPEN/CONJECTURAL inputs** (the real gaps);
- **ANCHOR-consumption is permitted but force-surfaced** as `SPLIT (mechanism
  derived; consumes anchored: …)` — never silent;
- the foundational **action carries `axiom=True`**, so deriving *from* it reads as
  `clean`, while consuming a measured value (τ₀, τ_micro) reads as `SPLIT`.

Overrule to the strict version by removing the `axiom` exemption if you prefer an
empty DERIVED set.

## Structure

| File | Role |
|---|---|
| `gate.py` | **Principle 0** — Claim, Tier/Novelty/Step, `validate()`, closure helpers |
| `registry.py` | the foundation (anchors + the 2 OPENs) + forward rungs, each a `Claim` |
| `checks.py` | self-contained runnable checks (μ_linear via P^TT, arrow Ṡ≥0, QM-as-τ→0, Q-causality) |
| `targets/memory_function.py` | **Target 1** — K̃(ω) from the bath (decides single-pole / dark-pole) |
| `targets/riegert_paneitz.py` | **Target 2** — S⁴ a/c (decides α's antecedent) |
| `falsifiers/decoherence_689hz.py` | **Step 5** — the standalone, framework-independent 689 Hz falsifier |
| `audit.py` | the **one-pass reader view** (the success criterion) |
| `ci_check.py` | the build gate (CI) |
| `tests/test_gate.py` | proof the gate rejects laundering |

## Run

```
python -m v41.ci_check      # the gate: exit 0 = clean, exit 1 = violations
python -m v41.audit         # the one-pass reader view
python -m pytest v41/tests  # proof the gate rejects laundering
python -m v41.falsifiers.decoherence_689hz   # the standalone falsifier
```

## Current state (Steps 1–5 stood up)

- **5 DERIVED** (Q, μ_linear, arrow-form, QM-recovery, the 689 Hz plateau) — each checked, novelty-tagged, DERIVE-scored. μ_linear and Q and QM read *clean*; the arrow and the plateau read *SPLIT* (anchored τ₀).
- **4 ANCHORS** (τ₀, τ_micro, **single-pole**, **α**) + the axiom action; **0 OPEN**. Both
  research-spine gaps are now *proven anchors*: each is a clean CONDITIONAL theorem whose
  consequent is computable (single-pole: bath IR exponent s; α: a/c = 1/3) but whose antecedent
  is **free data the action does not fix** (single-pole: bath collisionality, Targets 1/1B/1C;
  α: which mode is the IR carrier, Target 2). Neither is a missing computation — de-anchoring
  either requires *new physics* (bath microphysics; or anomaly-induced conformal dynamics).
- **1 FORBIDDEN** no-go (honestly tagged `KNOWN-REUSED` — assembled from Ostrogradsky/Stelle/Horndeski/dRGT; *provisional* on single-pole).
- **1 HOSTED** (Ω_Λ — the gate *forbids* it being DERIVED because it rests on α-OPEN: the anti-laundering rule biting in the open).
- **1 CONJECTURAL** (F(t) dark matter).

## What not to do

Do not expand sectors before the **S⁴ a/c** (α) lands. The single-pole gap is closed —
not by deriving it, but by proving it *can't* be derived from current content and
anchoring it honestly (Targets 1B/1C). Any sector built on single-pole-ness now rests on
that ANCHOR, and the audit must show the SPLIT. Breadth on an unproven footing is the v4
baggage in cleaner code. Success is the reader of the audit, not the count of sectors.
