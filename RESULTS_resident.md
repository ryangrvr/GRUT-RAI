# The GRUT Resident — Layers 2–3: the dependency graph + the propose interface

*The deterministic floor of the "scientific operating system." This note states what the resident does, where it sits in the five-layer architecture, and — load-bearing — its honest scope: it enforces **discipline and consistency, not truth**, and it makes laundering **harder**, never banking **easier**.*

---

## What the resident does

The static auditor (`auditor.py`) checks one claim at a time: is it tiered, sourced, falsifiable, not laundered? The **resident** (`resident.py`) lifts that into a *consistency engine*: given a **proposed new claim** or a **change to an existing one**, it deterministically reports the full consequences on the GRUT register — and returns a verdict.

```
propose(claim, claims, source_ids)            -> report + verdict
check_change(claim_id, new_fields, claims, …) -> report + verdict   (merges then proposes)
dependency_graph(claims)                       -> (DAG, errors)      (acyclic + resolves?)
downstream(claim_id, claims)                   -> [affected dependents]
```

A report contains, all computed deterministically:

- **Discipline** (via `auditor.audit_claim`): tier valid, sourced, falsifiable, **laundering?**
- **Ledger**: this claim's `ledger_delta`, the current net, the **new net**, and whether the net changes.
- **Dependencies**: which claims it **rests on** (must resolve); for a change, which existing claims are **downstream-affected**.
- **Consistency flags** (machine-checkable only — *not* truth):
  - **RE-OPENS** — changing a claim that is currently `settled-negative` / `refuted` / `moot` / `no_go_export` / `disfavored` / `deferred`.
  - **BUILDS-ON-CLOSED** — a new claim that rests on such a closed/disfavored claim.
  - **TIER-CONTRADICTION** — a *result* tier (`shown`/`derived`) resting on an **open** input (`to-derive`/`assumed`/`derived-pending`). *(A `derived-pending` claim resting on an `assumed` input is **not** flagged — that is exactly what "pending" means; e.g. `mu_linear` on `p_tt_ansatz`.)*
  - **PRIOR-LINEAGE** — references a v2/v3/v4 prior lineage (heuristic; forbidden).
  - **UNRESOLVED-DEPS** — a `depends_on` that names no real claim.
- **Verdict**: **PASS** (non-substantive, disciplined, consistent) / **BLOCK** (discipline or structural violation) / **FLAG-FOR-FIREWALL** (the default for any new substantive claim, and for any consistency flag).

**The dependency graph** is the second new artifact: a `depends_on: [...]` field on each claim captures the already-implicit rests-on structure (e.g. `mu_linear → p_tt_ansatz`; the α-exports → `rung9a_value`/`rung9b_bridge`; `founding_h3 → rung8_falsifier`/`founding_h2`). `dependency_graph` builds and **validates** it — acyclic, every edge resolves. The live register is a valid DAG: **32 nodes, 52 edges.** Adding `depends_on` was **metadata only**: every tier and `ledger_delta` is byte-identical, net stays **+12**.

## The load-bearing boundary: discipline and consistency, NOT truth

The resident **reports consequences; it does not certify physical correctness, and it does not auto-bank substantive claims.** This is the same calibration as the auditor, sharpened for proposals:

- **Every new substantive claim defaults to `FLAG-FOR-FIREWALL`.** The resident never turns a substantive claim into a silent `PASS`. The adversarial screen (the firewall) + human sign-off remain the truth-check — exactly as they were for the ζ and information-principle candidates.
- **It makes laundering harder, never banking easier.** It can `BLOCK` (a laundering or structural violation) or `FLAG`; it has no path that *relaxes* the established discipline. A consistency flag can only *raise* a verdict toward `FLAG`, never lower it toward `PASS`.
- **It enforces the established rules** — no-laundering, no-prior-lineage, default-broken, human-in-the-loop — and **invents no new authority.** `PASS` is reserved for genuinely non-substantive changes (e.g. a metadata-only `depends_on` edit that is disciplined and introduces no inconsistency).

## Disposition markers must live in `sub_status`

The resident protects a claim's disposition only if it can *see* it: **every closed/disfavored marker
(`settled-negative`, `refuted`, `moot`, `no_go_export`, `disfavored`, `deferred`, `forbidden`) must live
in the claim's `sub_status` field** — the machine-checkable field `_is_closed` scans. `tier_note` is
prose-commentary only; a disposition recorded there but not in `sub_status` is invisible to the resident,
so a later softening of it banks as a silent PASS (this was a real hole found by the independent
verify-the-verifier firewall — `founding_h2`'s "disfavored" lived only in `tier_note` until the marker
was added to `sub_status`). Making `_is_closed` scan `tier_note` instead is **verified over-reach** (≈12
claims' notes mention *other* claims' markers and would be falsely flagged). **The data home, not the
scan, is correct: put the marker where the machine looks.** (CHARTER.md §7.)

**Negation guard on `refuted` (fixed 2026-06-29, found during the rung7 w(z) work).** `_is_closed`
substring-matched the bare token `refuted` — which also fired inside `rung3`'s *negation*
`"... neither derived nor refuted"`, falsely marking the **open** anchor `rung3` (and its dependents
`rung5`, `rung7_wz`) as a closed disposition and stamping them with a spurious `BUILDS-ON-CLOSED`. A false
"closed" on an open claim is exactly the inaccuracy the resident exists to prevent (and noise that could
mask a *real* `BUILDS-ON-CLOSED`). `_is_closed` now strips a negated `refuted` (`nor/not/never refuted`)
before the marker scan, so the token counts only as an actual disposition (e.g. `info_i2`'s
`screened-refuted` still reads closed; a bare `refuted:` disposition still reads closed). The harness's
`PROV_CLOSED_MARKERS` already sidestepped the same trap; this aligns the resident. Two regression tests pin
it (`test_negated_refuted_is_not_closed`, `test_rung3_dependents_have_no_false_builds_on_closed`).

**Version-token precision on `_prior_lineage` (fixed 2026-06-29, found while opening Version II).** The
old `\bv[2-9]\b` (case-insensitive) didn't just collide with the `V2` = Version II label — it flagged
**`v5`, the current clean rebuild itself**, and every future capital-V program phase, as "prior lineage."
A false flag that fires on the current version *pressures authors to reword honest claims to dodge it* —
exactly the content-distortion the discipline rejects. Fixed by narrowing the version token to the actual
prior versions `v[2-4]` and making it **case-sensitive lowercase** (lowercase `v4` = lineage convention;
capital-V `Version II`/`V2` = program phase; `v5` = current). The phrase markers stay case-insensitive.
Both-directions regression: real lineage still flags (`v4`, `v2/v3`, "previous version", "propagating-relic");
the current program does not (`Version II`, `V2 frontier`, `the v5 register`) — pinned by
`test_prior_lineage_version_token_precision` and `test_live_register_no_false_prior_lineage`.

> **Known fragility (mark, don't chase) — a V2-era floor-cleanup task.** This is the **second** free-text-regex
> false-positive in the resident this session (the `refuted` negation above; now the version token).
> Pattern-matching *prose* for disposition/lineage is structurally brittle. The durable answer is the same
> lesson `_is_closed` taught (CHARTER §7): **disposition belongs in a structured marker** — a claim that
> genuinely imports prior lineage should *carry a field/tag*, with the free-text regex demoted to a backstop,
> the way closed-disposition lives in `sub_status`. That is a floor **refactor**, deliberately **not** done
> mid-V2-opening; recorded here as the durable direction. The narrow regex fix + regression tests are
> sufficient to clear the field for now.

**The disposition refactor — DONE (2026-07-04, after a *third* near-miss).** The third false-positive
(`_is_closed` matching `refuted` inside `u6`'s cross-reference to `info_i2`'s marker) confirmed the pattern,
so the durable fix above was built: a **structured `disposition` field** (enumerated: `screened-refuted`,
`settled-negative`, `no_go_export`, `disfavored`, `frozen-V1`, `moot`, `deferred`, `screened-dissolves`,
`forbidden`; absent = open) and a boolean `prior_lineage` flag. **`_is_closed` and `_prior_lineage` read the
structured fields authoritatively**; the free-text regexes are **demoted to non-authoritative hints** (`_disposition_hint`
/ `_lineage_hint`) that *may warn* (surfaced in `propose(...)["hints"]`) but **never flag alone**. Each claim's OWN
markers were migrated to the field (7 closed claims); **cross-references and negations stay in prose** and can no
longer false-close, because prose is no longer authoritative. Both-directions regression pins all three historical
near-misses (`rung3` "neither refuted", the `v5`/Version-II token, the `u6` "info_i2 was refuted" cross-ref → all
clean) and every genuine closed claim (still caught). `disposition`/`prior_lineage` are in `SUBSTANTIVE_FIELDS`
(changing one is a substantive re-open). This retires the fragility, not just the instance.

**Object-type taxonomy — recorded, deferred (a future structural direction).** The register now holds
*heterogeneous* objects: physics claims, a governing charter (`u0`), classification-programs (`u5`/`u6`), and a
provisional definition (`GLOSSARY.md`). A referee's observation: this could be schematized with an explicit
object-type field. It is a **good future direction but premature now** — there are ~three de-facto types, not
seven; most have a single instance; the definition already lives fine as a glossary stipulation; and adding a
type system now would over-engineer a register that works. **Add object-types when instances earn them**, not
before. Recorded here so the direction is not lost.

## The five-layer architecture

| Layer | What it does | Status |
|---|---|---|
| **1 — Auditor** | per-claim discipline: tiered, sourced, falsifiable, not laundered (`auditor.py`) | **built** |
| **2 — Dependency graph** | the DAG of rests-on edges; acyclic + resolvable (`resident.py`) | **built (this)** |
| **3 — Propose interface** | `propose`/`check_change`: full deterministic consistency consequences + verdict | **built (this)** |
| **4 — LLM semantic** | does a proposal *mean* to re-open a no-go; is it truly novel vs already-banked; does its statement assert content a no-go forbids *in meaning*, not just tokens | later |
| **5 — Test wiring** | each claim's `overturning_computation` actually runnable / wired to a test that can fail it | later |

Layers 2–3 are the **deterministic floor**: everything they report is mechanical and reproducible, with no model judgment. Layer 4 is where semantic "does this *really* contradict a no-go / re-open a closed thread" judgment lives — and it, too, will feed the firewall, not replace it. Layer 5 closes the loop between a claim's stated falsifier and an executable test.

## Honest scope

This is a **working seed of the scientific operating system**, not the finished AI:

- It is **deterministic and mechanical** — a few hundred lines of pure-stdlib Python over the register. It has no model of physics and no semantic understanding; the "does this proposal make sense" judgment is exactly what it defers to the firewall and the human.
- It is **human-in-the-loop by construction**: it surfaces consequences and a verdict, and stops. Banking a substantive claim still requires the adversarial screen and an overseer sign-off.
- The **resident vision** — an always-on engine that keeps an entire scientific corpus consistent and refuses to let contradictions or laundering in silently — is what this seed points toward. We claim the seed, the dependency graph, the propose interface, and the demonstration; we do **not** claim the finished platform.

## Reproducibility

```
python3 provenance/resident.py        # demo: graph validity + example propose/check_change reports
python3 provenance/test_resident.py    # 38 tests (graph, propose, change, consistency, disposition-refactor regression)
python3 provenance/validate.py         # the gate: GREEN, net +12, 43 nodes (tiers unchanged)
```
Pure Python stdlib; no third-party dependencies. The resident reads the register and reports; it never writes it.


*Sync note (2026-08-02): the run-now expectations above are as-of-phase; for the live count and net, see the `GRUT_ToE.md` header and changelog (REGISTER-SYNC-guarded).*
