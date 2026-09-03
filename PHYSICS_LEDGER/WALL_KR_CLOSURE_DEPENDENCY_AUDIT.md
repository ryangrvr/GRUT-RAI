# CLOSURE / DEPENDENCY AUDIT — POST-8d00097

**Date:** 2026-09-02 · **Instrument:** `wall_kr_closure_dependency_audit.py` ·
**Artifact:** `WALL_KR_CLOSURE_DEPENDENCY_AUDIT_RESULT.json` ·
**Battery: 29/29, zero failures.**
**Read-only. No physics executed. No A-F decision selected, recommended, inferred or
defaulted. No tracked file modified.** W-0.

## THE HEADLINE

**Yes — there is legitimate decision-free work.** But the audit also found that the
register's entire net of **+16 sits downstream of a single `assumed` node**, which makes
decision **F** far more consequential than its "three held flags" framing suggests.

---

## Q6 — THE HIDDEN DEPENDENCY (the most important finding)

`background_time_translation_flow` is tier **`assumed`** and carries **+1**.

| | |
|---|---|
| transitive dependents | **30 of 74 nodes** |
| ledger carried by those dependents | **+15** |
| plus the node itself | **+1** |
| **total downstream** | **+16 — the entire register net** |
| `shown`-tier nodes downstream | **8** |

**The distinction that matters, and I am keeping it sharp:** the *tier-rule violation* is
narrow — exactly two direct `shown`-on-`assumed` edges, `rung1_inin_formalism` and
`rung2_kms_gate`, precisely as the held-flag review said. The **dependency scope** is a
different quantity, and it is the whole register. F2 is not a bookkeeping wrinkle; however
it is disposed, it conditions essentially everything.

**OWNER-DECISION REQUIRED: F.**

## Q5 — OVERCLAIM SWEEP

The Tier-4 register node is **exemplary**, not an overclaim: it states validity `ω >> H`,
separates UNCONDITIONAL from CONDITIONAL content, says *"NO pole claim is made"*, and
explicitly disclaims being a Class-C classification.

**One stale clause found.** That same node still cites *"D4 dual-gauge unexecuted"* as a
live reason the cell is CC-C — but D4-A is now accepted. **The conclusion survives**: CC-C
still stands on the other two stated reasons (the low-frequency criterion lies outside the
truncation's domain; the face adjudication is owner-owed). Only the justification is out of
date.

**Repair class: register mutation — OWNER/BANK-GATED. Not a decision-free fix, and not
performed.**

## Q4 — DEFECTS, AND A SHARP CONTRAST

| provenance chain | result |
|---|---|
| `provenance/prereg/MANIFEST.txt` | **INTACT — 18/18 hashes verify** |
| Class-C certificate package pins | **6/11 verify — 5 drifted** |

This contrast is the finding. The drift is **mechanism-specific, not systemic**: the
hashed-manifest design holds perfectly, while the emit-once, never-verified certificate
design does not. The project's provenance discipline is sound; one instrument's design is
not.

Dangling references: `gw_tensor_friction.py` is absent but is **declared future work**, not
a broken link. `pi0_trace_channel.py` is absent and cited in `X_FLOOR_MAP.md`.

**A defect of my own, disclosed:** my first reference sweep did not search
`provenance/prereg/`, and falsely reported a prereg cited by a `shown` register node as
missing. The file is present and correctly hashed. Checker fixed; the false positive is
recorded rather than quietly dropped.

**Decision-free repairs available:** documentation/reference hygiene, and adding a
certificate-pin **verify gate** — which records drift rather than repairing it, so it
alters no frozen content and manufactures no owner decision.

## Q1, Q2, Q3, Q7 — THE DEPENDENCY MATRIX

Register: 74 nodes, net **+16**. Tiers: 12 `shown`, 17 `assumed`, 14 `postulate`,
20 `to-derive`, 4 `derived-pending`, 3 `measured`, 2 `heuristic`, 2 `open`.

### Standing results, by dependence on A-F

| result | evidence status | depends on A-F? | frozen? |
|---|---|---|---|
| T1 dS TT-TT-TT vertex | validated | **No** | Yes |
| T2 massless TT bath | validated | **No** | Yes |
| T3 contract loop | validated | **No** | Yes |
| T4 retarded K_R, `ω >> H` | validated **in declared domain** | **No** | Yes |
| branch point at ω=0 / gapless cut | validated, unconditional | **No** | Yes |
| D4-A dual-gauge TT robustness | accepted | **No** | Yes |
| Gate-E FDT/KMS/noise | validated in scope | **No** | Yes |
| H⁰ locals c0=c2=0 exact | calculated | **No** | Yes |
| c4 / Λ_R | **unresolved input** | **Yes — A-adjacent** | registered unresolved |
| H² locals c0′, c2′ | **unresolved** | **Yes — A** | fork-gated |
| low-frequency consequence | **blocked** | **Yes — A + C** | No |
| consequence class | **unassigned (CC-C)** | **Yes — A + C + D** | No |
| *everything above* | — | **conditioned by F** | — |

### Owed work: 26 nodes

**13 candidates show no keyword blocker and no unresolved dependency** — including the
universality family (`u2_kernel_universality`, `u3_split_origin`, `u4_constitutive_origin`,
`u5_constitutive_phases`, `u6_constitutive_order`), `method_novelty`,
`founding_h2_R_zeta_bridge`, `info_i2_beyond_standard_bridge`, `l0_r2_exact_unique_breaker`,
`lambda_undetermined`, `vc_w_equals_minus_one`, `vc_grut_relation`, `emergence_chain`.

**SCOPE LIMIT, stated plainly:** keyword absence is **not proof of independence**. These are
*candidates*. Each needs statement-level confirmation before anyone commits to it — that
confirmation is itself decision-free work.

### Smallest unlock set per blocked item

| blocked item | smallest owner-decision set |
|---|---|
| H² local sector | **A** |
| low-frequency consequence | **A + C** (plus **B** only if the route is windowed) |
| consequence class assignment | **A + C + D** |
| use of the certificate face | **D** |
| certificate pin integrity | **E** |
| *the register beneath all of them* | **F** |

---

## ANSWER TO THE CLOSING QUESTION

**Is there a legitimate next computational task requiring none of A-F?**

**Yes** — two kinds, both decision-free:

1. **Statement-level confirmation** of the 13 candidate independent items, converting
   "no keyword blocker" into an actual dependency proof. This is exactly the work that
   determines whether A-F even need deciding.
2. **Provenance hygiene:** a certificate-pin verify gate, and the dangling-reference
   cleanup.

Neither requires an owner decision, neither touches frozen physics, and neither advances
the blocked low-frequency campaign.

**What I am NOT doing:** proposing which to run, or treating "decision-free work exists" as
permission to start it.

## HARD STOP

A-F: **all unselected**. No physics. No IR prescription. No epoch window. No ω ≪ H. No α.
Evaluator untouched. Register untouched and unmutated — including the stale clause, which is
reported and left. Nothing banked.
