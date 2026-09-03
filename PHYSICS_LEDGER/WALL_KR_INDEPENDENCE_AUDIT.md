# STATEMENT-LEVEL INDEPENDENCE AUDIT — THE 13 CANDIDATES

**Date:** 2026-09-02 · **Instrument:** `wall_kr_independence_audit.py` ·
**Artifact:** `WALL_KR_INDEPENDENCE_AUDIT_RESULT.json` · **Battery: 25/25, zero failures.**
**Read-only. No physics. No A-F selected, recommended, inferred or defaulted.** W-0.

## SELF-CORRECTION FIRST — 3 OF MY 13 WERE WRONG

The candidate list in `765327f` was built with a **one-level** dependency check. Re-derived
with full transitive ancestry, **three of the thirteen sit inside the blast radius**:
`info_i2_beyond_standard_bridge`, `l0_r2_exact_unique_breaker`, `u2_kernel_universality`.

The adversarial pass was run against my own list, and my own list is what it caught. This is
exactly why "keyword absence is not evidence of independence" needed to be a gate rather than
a caveat.

## THE MATRIX

| item | tier | A-F dependency | btt-flow dep. | load-bearing? | bypass? | classification |
|---|---|---|---|---|---|---|
| `u3_split_origin` | to-derive | none | **none — sits BELOW rung1** | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `u4_constitutive_origin` | to-derive | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `u6_constitutive_order` | to-derive | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `emergence_chain` | to-derive | none | none (renders register) | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `method_novelty` | to-derive | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `lambda_undetermined` | to-derive | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `vc_w_equals_minus_one` | open | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `vc_grut_relation` | open | none | none | n/a | n/a | **CONFIRMED INDEPENDENT** |
| `founding_h2_R_zeta_bridge` | to-derive | none | none | n/a | — | **CONDITIONALLY INDEPENDENT** |
| `u5_constitutive_phases` | to-derive | none by graph | **none by graph — but see below** | **content-level** | not sought | **CONDITIONALLY INDEPENDENT** |
| `info_i2_beyond_standard_bridge` | to-derive | **F** | via rung1+rung2 | inherits FDT (ω-domain) | none found | **OWNER-DECISION DEPENDENT** |
| `u2_kernel_universality` | to-derive | **C + F** | via rung1, rung3 | **content IS low-ω** | none | **OWNER-DECISION DEPENDENT** |
| `l0_r2_exact_unique_breaker` | to-derive | **F?** | via rung1 | **turns on rung1's own status** | possible | **UNRESOLVED** |

**Tally: 8 confirmed · 2 conditional · 2 owner-dependent · 1 unresolved.**

## THE THREE FINDINGS THAT MATTER

**1. A missing dependency edge.** `u5_constitutive_phases` declares **zero** dependencies,
but its content is *"classify the UNIVERSALITY CLASSES of the constitutive response
chi(omega,k)"* — the single-frequency kernel whose definability is precisely what
`background_time_translation_flow` licenses. It is independent by graph and **not**
independent by content. **Reported, not rewritten.**

**2. `u2` is worse than F-dependent — it is C-dependent.** Its content is *"the SPECIFIC
response kernel (L0, the low-omega pole structure)"*. That is squarely the regime the
evaluator refuses. It also depends on `rung3_single_pole`, itself derived-pending and
low-frequency-blocked. It was in my candidate list; it is arguably the most blocked item of
the thirteen.

**3. `u3` cannot inherit the lineage.** Its statement says it *"sits BELOW rung1 (rung1
assumes the split)"* — it is upstream of the whole dependency chain, so it is independent for
a structural reason rather than an accidental one. Of everything on this list, its
independence is the most robust.

## DECISION B HAS ZERO REGISTER FOOTPRINT

`epoch` occurs **zero times** in the register. **No registered claim depends on decision B.**
B can be left undecided indefinitely without conditioning anything already banked — which
separates it sharply from A, C and F.

## TWO AGENT CLAIMS — VERIFIED, THEN CORRECTED

A background audit agent (2 of 15 survived the usage limit; none of its verifiers ran)
produced two claims I checked rather than adopted:

- **"A dangling id `rung1_inin_action`."** **Corrected — not a defect.** The register's own
  ledger notes record it as the *pre-rename* name and use it as contemporaneous provenance
  prose. Renaming history is exactly what those fields are for.
- **"A hidden dependency: the H² dispersion samples ω′ ≲ H."** **Corrected — real but not
  hidden.** It is recorded on the Tier-4 artifact face verbatim, with an O(ε_H²) error
  estimate inside the domain gate's tolerance. A disclosed systematic, not a concealed one.

## INDEPENDENCE IS NOT ACTIONABILITY

Of the 8 confirmed independent, only **4 are internally advanceable**: `u3_split_origin`,
`u4_constitutive_origin`, `u6_constitutive_order`, `emergence_chain`.

The other four are independent but cannot be advanced by our own work: `method_novelty`
graduates *only* on external validation by a different team; `lambda_undetermined` is an
open-field marker asserting an absence; `vc_w_equals_minus_one` moves with data, not with us;
`vc_grut_relation` is answered only by deriving ρ_Λ, which `lambda_undetermined` denies.

Reporting "8 independent items" as available work would have overstated the reachable set by
half.

## ONE DECISION-FREE CHECK, EXECUTED

`python3 provenance/emergence_chain.py --check` — verified read-only before running (the
write path is in the non-check branch), worktree confirmed unchanged after. Result:
**"chain matches the register (no drift)."**

## LEGITIMATE NEXT TASKS REQUIRING ZERO OWNER SELECTIONS

1. **`u3_split_origin`** — why is there a system/bath split at all. Structurally upstream of
   the contested lineage.
2. **`u4_constitutive_origin`** — why coarse-graining yields constitutive/response form.
3. **`u6_constitutive_order`** — an order parameter for constitutive organization.
4. **`emergence_chain` drift check** — done this run; no drift.
5. **Provenance hygiene** — reference cleanup; a certificate-pin verify gate that records
   drift without repairing it.

Items 1-3 are genuine open research programs, not short tasks. I am not proposing which to
run, or in what order.

## HARD STOP

A-F: **all unselected**. No physics executed. No IR prescription, epoch window, ω ≪ H
evaluation, or α extraction. Evaluator, register, frozen artifacts, certificate pins,
regulator policy and class state all untouched. The missing edge was reported, not written.
Nothing banked.
