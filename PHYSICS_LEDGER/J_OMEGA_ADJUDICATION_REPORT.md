# J(ω) ADJUDICATION REPORT — claim dependencies, the K_R gap, and the +1 package

**Date:** 2026-08-30 · W-0: computed-and-reported, NOT banked · No result modified.
**Companion:** `J_OMEGA_CLAIM_DEPENDENCY.json` (machine-readable table).
**Inputs (all hash-pinned, none modified):** frozen kernel `dd77b194…`, A3-4 /
A4 / PV / J-comparison results, `MICROSCOPIC_TARGET_BENCHMARK.md`
(`f6513b1e…`), `wall_a_g1_ohmic_plant.py` (`facacda5…`), the A3 declarations
(+V2–V4), `provenance/claims.json` (read-only).

---

## 1. The benchmark contract, audited

**K_R, as frozen.** The register (`rung1_inin_formalism`, tier *shown*) defines
K_R as *"the retarded dissipation kernel"* of the Schwinger–Keldysh influence
action S_IF for the doubled graviton field. The benchmark's pipeline is
`Σ(x,x′) → G_R^TT(x,x′) → K_R → J(ω)`, and its own status line records the
assembly as **"OBSTRUCTED AT WALL A — no graviton-probe assembly exists"**,
naming the graviton-probe influence functional (and Wall B's RG half) as what
K_R construction requires.

**Is K_R mathematically distinct from the computed Σ_R^finite / χ?** **YES.**
Σ_R^TT is the one-loop matter self-energy insertion; K_R is the effective
kernel of the probe's influence action after the `G_R^TT` dressing step —
a further construction (dressing/reduction) the campaign has not built.
Structural properties (pole vs branch cut, gap vs gapless) are **not**
automatically inherited across that step.

**"Single-pole," as frozen.** Three distinct register objects use the phrase:
- `rung1_ontology_finite_memory` (tier **assumed** — "a STANCE, explicitly not
  derived"): the vacuum IS a responsive medium with single-pole memory.
- `rung3_single_pole` (tier derived-pending, anchor-class): massless modes ⇒
  DOS~ω² ⇒ J~ω³ (s=3); single-pole collapse *provided* no second internal
  scale; **"whether GRUT's vacuum IS in that regime (pole vs branch-cut) is
  the open anchor question."**
- The benchmark's G3 rider: *"pure relaxation suffices for no-crossing;
  single-pole is stronger than needed"* — pre-declaring that a
  relaxational-but-not-single-pole outcome leaves the single-pole commitment
  explicitly underived.

**The +1 discharge rule, as frozen (Declaration 4, verbatim in substance):**
the `response_lorentz_covariance` +1 is dischargeable **only** by Q1 INSIDE
**and** Q5 INSIDE; Q3 and Q4 do not vote; *"any discharge claim citing other
evidence is invalid"*; discharge itself is an owner ruling at the bank gate.
**Therefore K_R is NOT required for the +1 — and equally, no K_R result could
substitute for Q1∧Q5.** The rule cuts both ways and is closed.

**The convergent/relaxational axes, as frozen:** the two-axis table is
pre-registered *"for whoever runs the assembly"* — its ledger-consequence
column (row 1: "derives what rung7 needs … +1 partially discharges; excess
strength of single-pole becomes explicit") is written against the **pipeline
output**. The J-comparison filled the table for **χ_Σ (the Σ-level TT
response)** — disclosed as such in the instrument and in this report.

---

## 2. Claim dependency table (full version in the companion JSON)

| claim | required object | evidence available | evidence missing | status |
|---|---|---|---|---|
| Q1^TT INSIDE | Σ-level TT (Decl. 4 object) | A3-4 exact, all orders; A4 gauge-robust; PV scheme-robust | none | **COMPLETE** |
| Q5^TT INSIDE | Σ-level flat limit | same chain | none | **COMPLETE** |
| Q4^TT HOLDS | Σ_R^TT | A3-4 + A4 + PV absorptive | none | **COMPLETE** |
| Q3 class | Σ-level nonlocal TT | gapped, s ≥ 2 rigorous; PV-robust | none (class is settled at declared scope) | **COMPLETE** (class ≠ s=3 claim) |
| J5 / s=3 | gapless IR access | INAPPLICABLE / GAP OBSCURES | the registered IR limit itself (massless limit undeclared, uncomputed) | **RECORDED — not convertible** |
| Benchmark convergence axis | pipeline output (contract) / χ_Σ (as run) | χ_Σ: IR-CONVERGENT rigorously | K_R-level confirmation **or** owner scope ruling | **SCOPED EVIDENCE** |
| Benchmark relaxational axis | pipeline output (contract) / χ_Σ (as run) | χ_Σ full response: 0 crossings; light-cone diagnosis; scheme caveat | same as above | **SCOPED EVIDENCE** |
| Single-pole statement | K_R analytic structure | Σ-level: branch cut, NOT single-pole; G3 rider pre-declared this outcome class | K_R (dressing can change pole structure) | **UNDERIVED — excess strength explicit, per the benchmark's own row-1 wording** |
| +1 discharge (`response_lorentz_covariance`) | Q1∧Q5 ONLY (frozen map) | both INSIDE, preregistered, robust | **owner ruling only** | **READY FOR ADJUDICATION** |
| Ward/Bardeen finding | (separate track) | class-B, vector-channel, cut-carrying, primary-only | Bardeen completion / owner charter | **UNRESOLVED — SEPARATE** |

**The determination the brief asked for:** K_R is **NOT required** for the +1
discharge, nor for Q1/Q4/Q5/Q3, nor for the J5 record. K_R (or an explicit
owner ruling that χ_Σ-scope suffices) **IS required** before the benchmark's
ledger-consequence cell — the rung7-side "partially discharges" — can be
executed at the contract's own scope, and before any claim about the vacuum
bath kernel's pole-vs-branch-cut anchor question (`rung3_single_pole`) is made.

---

## 3. K_R — not built, per the brief; the prerequisite specification

If the owner later charters a K_R stage, the frozen texts fix its inputs:
1. the graviton-probe influence functional (Wall A's remaining assembly — the
   staged `gw_tensor_friction.py` work named by the benchmark);
2. the `G_R^TT` dressing of the frozen Σ_R^finite (input: kernel
   `dd77b194…`, immutable);
3. Wall B's RG half, per the benchmark's obstruction note;
4. the TTW/retarded-structure premise (Wall C) for the in-out vs retarded
   reduction;
5. the same fences: pre-registered criteria before computation, the massless
   limit as a *declared* question if it is to be asked, no fitting.
Nothing beyond this specification is constructed here.

---

## 4. The J(ω) result, preserved exactly

Computed response: **gapped, convergent, purely relaxational** (full MS-fixed
response; the nonlocal part's single Re-crossing is the light cone ω = k,
domain-exiting as k → 0). Direct gapless s=3 family: **not reproduced** —
different analytic classes. J5: **INAPPLICABLE / GAP OBSCURES REGISTERED IR
LIMIT** — not CONFIRMED, not REFUTED, no fit above threshold performed or
permitted. The benchmark's own closing rule was followed: the actual
functional form (gapped) was reported and the convergence integral computed
directly; no effective exponent was fitted.

**Scope note (recorded, not a repair):** the computed Σ is a **massive**
matter loop; the registered s=3 derives from **massless** modes (DOS~ω²).
The analytic-class mismatch is exactly what that difference predicts. The
massless limit is undeclared and was not computed; it is the natural bridge
question **for the owner to charter or decline**.

---

## 5. The +1 adjudication package (prepared; NOT executed)

- **Q1^TT = INSIDE**: exact symbolic identity at H⁰/H¹/H², P₂ not imposed
  (A3-4 layer 2, 31/31); gauge-robust by operator identity (A4); absorptive
  content scheme-robust at 7.02e-17 (PV).
- **Q5^TT = INSIDE**: flat limit structural, matches Q1's placement (same
  chain of three independent confirmations).
- **Preregistration:** both criteria frozen in `WALL_A_A3_DECLARATIONS.md`
  (`87e2d24d…`, 2026-08-25) before the integral was touched; the layer-2
  predicates hash-frozen (commit `0bb30fc`) before the TT numbers existed.
- **No fitting:** the placement was decided by exact residue = 0, no basis or
  benchmark quantity entered the response-side construction (guard clean on
  every run; J(ω) unsealed only after all verdicts were recorded).
- **The frozen rule:** Q1 INSIDE ∧ Q5 INSIDE is the only admissible evidence;
  discharge is an owner ruling at the bank gate.
- **This instrument has NOT discharged the +1.**

## 6. The three findings, kept separate

1. **TT physical response:** structure/gauge/scheme robust.
2. **Non-TT vector Ward residual:** unresolved, class B, cut-carrying,
   primary-only — untouched by the benchmark result in either direction.
3. **Benchmark:** gapped/convergent/relaxational; not a direct s=3 match;
   single-pole explicitly underived.

## 7. Exact next stage

**Owner adjudication** of: (a) the `response_lorentz_covariance` +1 (package
above; K_R not required); (b) the scope ruling on the benchmark's
ledger-consequence cell (χ_Σ-level vs K_R-level); (c) disposition of the Ward
class-B finding; (d) whether to charter K_R construction (spec in §3) and/or
the massless-limit bridge question. **Nothing further is computed until then.**
