# FOREST — PHASE 10: TARGET SELECTION / NOVELTY ISOLATION

**Date:** 2026-09-04 · **Instrument:** `forest_phase10_selection.py` ·
**Artifact:** `FOREST_PHASE10_RESULT.json` · **Base:** ad5ea33 (H¹ FROZEN; Phases 1–9
untouched). **Battery: 40/40, zero failures.** **VERDICT: `FOREST-EMPTY`.**

**The first draft of this phase selected `kk_static_transfer` as TARGET-1. Both
adversarial legs returned FAILED, and the selection is WITHDRAWN.** The decisive fact —
which I verified directly in the register before accepting it — is that the register
records that question as **ANSWERED 2026-08-09**, negatively. This record is the
corrected phase. It selects no target, runs no physics campaign, computes nothing,
selects no A–F decision, and does not use H¹ as evidence for anything.
Register sha256 identical pre/post; W-0.

## A · FOREST INVENTORY (machine-generated, all 74 nodes, content-based)

| bucket | count |
|---|---|
| UNSET | 34 |
| NON-DIFFERENTIATING | 15 |
| **CONDITIONAL** | **12** |
| FAILS-DIFFERENTIATION | 5 |
| NO-GO-EXPORT (deflationary) | 1 |
| **LIVE** | **7** |

**Headline, now actually gated:** the set of nodes that are LIVE, tier ∈
{shown, measured, derived}, and free of conditional/deferred language is **EMPTY** —
**zero nodes carry an unconditional, currently-observable differentiating result.**

## B · CANDIDATE PROVENANCE

The 7 live nodes: `kk_static_transfer` (ANSWERED, negatively), `zeta_interior_family`,
`x_no_pin_theorem`, `rung3_single_pole`, `rung6_qm_limit`, `rung7_wz`,
`kr_contract_retarded_tier4` (QUARANTINED — the frozen H¹ benchmark).
`rung1_ontology_finite_memory` is CONDITIONAL, not LIVE (corrected below).

## C · STANDARD-THEORY SUBTRACTION

Subtracted as standard: CTP/open-system machinery, FDT/KMS, **Kramers–Kronig and
passivity themselves**, the Bardeen μ–Σ parameterization and its DESI constraints, TT
projection, EFT bookkeeping, H¹/EH recovery. What remains after subtraction is a
**stance** — that the vacuum is a passive medium with finite memory — not a mechanism.

## D · NOVELTY CLASSIFICATION

`zeta_interior_family` → STANDARD-PARAMETERIZATION (free amplitude; its window numbers
are **amplitude bounds, not sign statements**). `x_no_pin_theorem` →
STANDARD-CONSEQUENCE, explicitly *no ratio pin*. `rung7_wz` →
STANDARD-PARAMETERIZATION. `rung3_single_pole`, `rung6_qm_limit` → NOVELTY-UNRESOLVED
(observable deferred; or orders below detectability). `kk_static_transfer` →
**RESOLVED-NEGATIVE**, see §I.

## E · COMPETING BASELINES

The first draft named "GR + ΛCDM, μ = 1 exactly" as the strongest fair comparator. **That
was the wrong comparator class**, and the correction is decisive for the verdict: a
one-signed **μ ≥ 1** in the quasi-static limit is **already the standard expectation** for
stable ghost-free Horndeski with c_T = 1 (Pogosian–Silvestri — in the repository's own
`sources.json`), and f(R) in the chameleon range gives 1 ≤ μ ≤ 4/3. A measured μ−1 > 0
would therefore not separate a passive-responsive vacuum from the mainstream
modified-gravity landscape at all — only from exact GR, which no one is defending.
Additionally, the standard baseline at DESI sensitivity is not exactly μ = 1 (massive
neutrinos, anisotropic stress, bias), and the register carries no accounting of that.

## F · FALSIFIABILITY — WHY THE SIGN ROUTE FAILS IT

The predicted region **contains the standard point**: the floor is non-strict
(ω·Im c₀ ≥ 0) and the c₀ = 0 branch is registered as exact-ΛCDM, so the claim is
μ−1 ≥ 0, a closed half-line whose boundary is the GR value. With the amplitude free
**down to zero** and the register's own concession that *"x has no lower observational
floor — the family allows, never predicts"*, every null is absorbed by x → 0. Current
data are null (μ₀ = 0.05 ± 0.22). Falsification would require a *significant detection of
the opposite sign* — so a lifetime of nulls leaves the claim permanently unfalsified
rather than tested. **This is a heads-I-win structure and it disqualifies the route.**

## G · DEPENDENCY FIREWALLS

H¹/K_R quarantined (frozen; no-citation rule honored). **Firewall exception NOT
discharged:** the first draft invoked §4's "unless the premise is what is being tested"
for `rung1`, but the selected campaign was an internal analyticity question whose
outcomes leave `rung1` untouched either way; only the observable terminus would test it,
and this phase disclaims computing it. The exception is withdrawn with the selection.

## H · TOP-THREE RANKING — WITHDRAWN AS SCORED

The first draft's ranking is void. Its parameter column ("0 for the sign") was **false**,
and its dependency claims were **inverted**: nothing in the register depends on
`kk_static_transfer` (gated), its own scope line says it *"does not gate the family
window"*, and the sign it needs lives in `rung3` — so A was downstream of C, not upstream
of B.

## I · SELECTED TARGET OR FOREST-EMPTY

**`FOREST-EMPTY`.** No live node combines (a) a working observable today, (b) a
difference not absorbed by a free parameter, and (c) separation from the broader
modified-gravity landscape.

**On the withdrawn target, precisely:** `kk_static_transfer.sub_status` records
**ANSWERED 2026-08-09** (`calc/kk_static_transfer.py`, prereg-sealed, four-mutant
battery) at outcomes (ii) **and** (iii): unconditional transfer **refuted permanently** by
an explicit passive counterexample, and the whole transfer question shown to collapse
onto **sign(χ_∞)** — the instantaneous/contact part, to which *passivity, causality and
the KMS lock are structurally blind*. A contact term is a **renormalization condition
fixed by measurement, not a prediction**. So the "parameter-free sign" that carried the
entire selection does not exist: the honest count is one undetermined bit (sign χ_∞) +
one free amplitude with no lower floor + one free functional form (x is a kernel
x(ω,k²), not a number).

## J · EXACT REASON — AND MY OWN DEFECTS, DISCLOSED

The reason for FOREST-EMPTY is §E + §F: the only candidate with an observable terminus
predicts a sign that is (i) not derivable without a free contact input, (ii) already the
standard expectation of the mainstream MG landscape, and (iii) unfalsifiable by nulls.

Defects in the first draft, all mine, all caught by the legs:

1. **Selected an already-answered target.** I read `statement`/`differentiator`/`tier`
   but never `sub_status`/`boundary_condition` — I checked the key list of `claims[0]`
   and assumed a uniform schema; it is not uniform. This is the root cause.
2. **`gate(True)` headline** — the **seventh occurrence** of the non-falsifiable-gate
   pattern in this program, committed in the phase immediately after the sixth was
   recorded as the standing lesson. Now really gated.
3. **LIVE bucket was a prefix artifact** (`rung1` begins "CONDITIONAL-…" and was mis-filed
   LIVE): corrected 11/8 → **12/7**.
4. **"Matches the in-repo DIFFERENTIATOR_TABLE" was overstated** — that table is stale
   (71 nodes), produced by a different classifier with no LIVE bucket, and disagrees on
   several nodes. Claim withdrawn; only the one-sentence headline agrees.
5. **I breached a standing prohibition in the same document that cites it:** §F of the
   first draft listed "sign(μ−1) fixed" as the GRUT-class value — an unconditional sign
   floor — when the register forbids any artifact quoting an unconditional μ floor. The
   conditional (χ_∞) was nowhere attached. Withdrawn and disclosed.
6. **Dependency claims inverted** (§H).
7. **The "one computed datum" was near-vacuous and stale in framing:** it tested the
   growth of a monomial, which fixes the *number of subtractions* rather than making a
   dispersion relation unavailable — and the register's own answer shows the obstruction
   is not falloff at all but sign(χ_∞). Withdrawn.

## K · UNRESOLVED ASSUMPTIONS

1. `rung1` remains a STANCE; nothing here tests it.
2. sign(χ_∞) is a genuinely open UV/contact question owned by `rung3` — but it is a
   renormalization condition, so resolving it yields a *conditional* floor, not a
   parameter-free prediction.
3. The owed low-ℓ TT-auto calc still binds `zeta_interior_family`'s window; unrun.
4. Flavor and strong-CP were queued in the breadth-first turn but are **not in the
   register** — unmapped, and ineligible for this ranking. If the program wants a fresh
   candidate pool, mapping them is the prerequisite, not a re-ranking of this one.
5. The standing prohibition stands: **no artifact may quote "x ≥ 0" for the
   observable-facing coupling** — including this one.

## §12/§13 · ADVERSARIAL LEGS

**Leg A (independent ranking): `FAILED`.** Reproduced the inventory bit-for-bit, then
found the prefix artifact, the stale-table overstatement, the ungated `gate(True)`
headline, the undischarged §4 exception, the inverted dependencies, and — decisively —
that the target was already answered and its sign is a free contact input.
**Leg B (hostile standard-theory referee): `FAILED`.** Demanded the equation and showed
it cannot be cleanly stated: the mathematics is textbook once-subtracted Kramers–Kronig
for a passive medium (which §C already subtracts as standard), the phenomenology is
MGCAMB μ–Σ with one free amplitude, μ ≥ 1 is already standard for stable Horndeski, and
both limbs of the offered falsification condition fail — one unattainable, one already
met and recorded as met. Eight errors listed, all verified against the files.

Both verdicts are **adopted in full**. No finding was contested.

## GOVERNANCE EXIT

H¹ frozen and unchanged; Phases 1–9 byte-identical; register unchanged; **no A-F
selection**; no physics campaign launched; no target computation started; HEAD ==
origin/v4. **This phase is NOT authorized to compute anything**; with FOREST-EMPTY there
is also nothing to authorize.

## W-0 STATUS — forest surveyed; verdict FOREST-EMPTY; selection withdrawn; nothing banked.
