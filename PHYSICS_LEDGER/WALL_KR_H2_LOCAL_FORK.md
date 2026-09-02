# H² LOCAL FORK — AUDIT RECORD

> ## ⚠ EVIDENCE SUPERSEDED — READ FIRST
>
> **The numeric route in this record integrated the c_m cone branch
> ALONE.** With both retarded branches summed, the **q^-4 / a=-1 power
> contribution cancels exactly**, and what remains is a **nonzero
> q^-3 / a=0 logarithmic IR divergence** of coefficient **−8ω²/15**.
> The "≈10× per decade / 1/δ power divergence" ladder below is therefore
> **branch-incomplete and superseded**.
>
> **The verdict H2-B is NOT superseded.** The original classification was
> branch-incomplete; the corrected full retarded integrand still diverges
> logarithmically, so the H² local sector remains fork-gated for the same
> reason — now stated correctly.
>
> Authoritative characterization and correction:
> `WALL_KR_H2_IR_OWNER_RULING.md` (Part 0) and
> `WALL_KR_H2_IR_OWNER_DECISION.md`. Commits `47aa43e`,
> and this record's own commit `390a22d` for provenance.


**Date:** 2026-09-01 · **Instrument:** `wall_kr_h2_local_fork.py` ·
**Artifact:** `WALL_KR_H2_LOCAL_FORK_RESULT.json` · **Battery: 24/24,
zero failures, first run.** · **Frozen inputs touched: NONE** (Tier-1..4,
D5, the H⁰ ledger, the declarations and the register all byte-identical
after the run). **W-0: unbanked. HARD STOP.**

## VERDICT: **H2-B**

**H² local coefficients are NOT uniquely determined: a registered
scheme/IR ambiguity remains.** Not forced to H2-A; not H2-C.

## THE QUESTION AND THE ANSWER

*Can the H² local coefficients be determined under the frozen Option-β
continuation, without a new physical input and without any downstream
spectral outcome?*

**No — because the H² direct radial integral genuinely requires the
infrared region, so its 1/(d−3) poles are IR-contaminated and pole-only
MS cannot legitimately extract a finite local part.** This is precisely
the registered IR-scale condition. **No scale was invented; no
dimensional-regularization interpretation was manufactured for an IR
divergence.**

## THE EVIDENCE — TWO INDEPENDENT ROUTES

**Route A (analytic).** Each radial master ∫₀^∞ q^{a−1}/(q−x)^{n+1} dq
converges only for 0 < Re a < n+1; a ≤ 0 is the **IR** end, a ≥ n+1 the
**UV** end. Term inventory of the frozen H² cone (a evaluated at d = 3):

| Δ-power | q-power | a(d=3) | strip | origin |
|---|---|---|---|---|
| Δ⁰ | q⁰ | 3 | (0,1) | UV |
| Δ⁰ | q⁻¹ | 2 | (0,1) | UV |
| Δ⁰ | q⁻² | 1 | (0,1) | UV |
| Δ⁰ | **q⁻³** | **0** | (0,1) | **IR** |
| Δ⁰ | **q⁻⁴** | **−1** | (0,1) | **IR** |
| Δ¹ | q¹ | 4 | (0,2) | UV |
| Δ¹ | q⁰ | 3 | (0,2) | UV |
| Δ¹ | q⁻¹ | 2 | (0,2) | UV |
| Δ¹ | q⁻² | 1 | (0,2) | convergent |
| Δ¹ | **q⁻³** | **0** | (0,2) | **IR** |

**Three terms carry IR-origin poles** (a = 0 and a = −1).

**Route B (numeric, independent).** The H² radial integrand at d = 3,
integrated from a small-q cutoff δ up to a fixed point below the cone:

    delta = 1e-2  ->  27.0169
    delta = 1e-3  ->  289.622
    delta = 1e-4  ->  2924.98
    delta = 1e-5  ->  29287.9

**≈10× per decade — a 1/δ power divergence**, exactly the strength the
a = −1 (q⁻⁴) term predicts. The divergence is *demonstrated*, not
inferred from power counting. **Teeth:** an IR-finite surrogate
integrand shows no such growth under the identical ladder, so the
detector responds to the divergence and not merely to shrinking the
interval.

## WHY THIS BLOCKS THE EXTRACTION

Pole-only MS against the frozen 1b counterterm basis is licensed for
**UV** poles. An IR-origin 1/(d−3) cannot be absorbed by a local
counterterm. Subtracting it as though it were UV would be exactly the
illegitimate move the frozen record forbids — and Control C makes the
point operational: any "MS finite part" extracted here would still carry
the cutoff dependence Route B exhibits.

**The obstruction is not a basis deficiency.** The UV-origin poles
(a = 1, 2, 3, 4) map onto the registered curvature/local class; **no
operator outside the frozen basis is required**, and none was added.

## SEPARATION HELD

This is the **retarded local** sector. The noise α = −2 result was **not
imported** and plays no role: the divergence found here is a property of
the retarded radial integrand itself. Retarded, noise, equal-time/secular
and state/IR contributions were kept distinct throughout.

## THE CONDITIONAL STRUCTURE (recorded, NOT claimed)

If the fork were resolved such that the extraction became legitimate,
the scale-free ω^(d−1) form would carry the single power ω² at d = 3 —
which would force **c0p = 0 structurally** and leave **c2p** as the one
determined H² constant, in exact parallel with H⁰. **This is recorded as
conditional only. It is not claimed, because the extraction is not
currently licensed.**

## PARAMETER-COUNT IMPACT

- **H⁰: unchanged** — exactly one irreducible unresolved constant, Λ_R.
  This stage does not touch it.
- **H²: adds nothing.** No H² constant was demonstrated, so none is
  counted. The sector remains fork-gated and **outside** the count.
- **New independent input: NO** — and none was introduced.
- No redundant parameterization is double-counted; nothing was folded
  into Λ_R.

## CONTROLS — all detecting

**A.** wrong-evanescent/projector (continue the measure in d, freeze the
projector algebra at d = 3) — visible to the radial inventory.
**B.** wrong-local-reference — a 10% perturbation of the frozen H²
nonlocal reference is caught by comparison against the artifact value.
**C.** wrong-subtraction — a local counterterm cannot remove Route B's
cutoff dependence.

## FROZEN-INPUT INTEGRITY

H⁰ absorptive coefficient A unchanged; H² logarithmic coefficient and
Im Σ_R^{H2} = −13H²ω²/(480π) unchanged (loaded from the frozen artifact,
never refitted); Tier-4 branch structure untouched; the register
byte-identical.

## HARD STOP

The **registered IR-scale condition is encountered**. The stage stops
here pending the owner's fork decision. No Axis-2 computation, no μ or
Λ_R selection, no noise-fork resolution, no Gate-E, no basis broadening.
