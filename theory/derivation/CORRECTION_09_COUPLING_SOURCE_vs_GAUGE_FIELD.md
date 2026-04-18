# Correction #9 — Coupling Source vs Gauge Field: Correcting Correction #8

**Date:** April 2026
**Status:** Correction #8 was applied to the wrong observable.

## What I claimed in correction #8

> "Derivative re-weighting kills the IR argument for F²F²." Numerical
> test showed `Σ d_n × λ_n² / (λ_n + m²)²` is UV-dominated regardless
> of matter mass, suggesting the M_Z scheme argument fails for the
> tensor projection.

I committed this and revised the probability of µ = M_Z downward to
20-30%.

## Why it was wrong

The spectral sum I tested, `Σ d_n × λ_n² / (λ_n + m²)²`, represents in
spectral form the `<F(x)² F(y)²>` correlator — the correlator of
dynamical gauge-field composite operators.

**But ε in Osborn 2003 eq (35) does NOT multiply `<F²F²>`.**

Reading eq (35) carefully:

```
L = n_V {(1/g²)[α(∇²g)² − 2δ G^{μν}∂_μg ∂_νg − (1/3) ε R ∂_μg ∂^μg]
         − 2κ(1/g³) ∂_μg ∂^μg ∇²g
         + 2λ(1/g⁴) ((∂_μg)(∂^μg))²}
```

**ε multiplies the operator `R × (∂_μ g)(∂^μ g) / g²`**, where `g(x)`
is the external coupling source in Osborn's local-coupling framework —
NOT the dynamical gauge field `A_μ`.

These are different objects:

| Object | What it is | My test measured | Relevant to GRUT? |
|:---|:---|:---:|:---:|
| `<F²(x) F²(y)>` | dynamical gauge-field 4-pt correlator | ✓ | NO |
| `R × (∂_μg)(∂^μg)/g²` | coupling-source gradient operator | ✗ | YES |

## What the right observable does

For GRUT's identification, the relevant observable is the CTP-induced
coupling asymmetry `(g_+ − g_-)` which acts as `(∂g)` in the Osborn
framework. Its magnitude comes from the **matter self-energy of the
coupling source**:

```
Π_g(q²) = ⟨source-source⟩ correlator on S^4
        = 1-loop matter bubble with external momenta q
```

At 1-loop in flat space, this is the standard running of the coupling:

```
Π_g(q²) = (α/π) × [ln(q²/m²) + const] + O(α²)
```

The NATURAL SCALE of this self-energy is the matter mass m — that's
the standard result. Matter heavier than q² decouples exponentially;
matter lighter than q² contributes logarithmically through running.

On S⁴ with radius 1/H, q² is replaced by S⁴ eigenvalues, but the
leading-order scale structure is the same: matter-mass-dominated for
m < q, curvature-dominated for m > q.

For SM matter at H_inf, m << H, so the relevant regime is "matter
lighter than curvature" — and the log structure brings in matter
scales through the RG-improved running.

## Revised probability

After correcting #8:

**~50/50 between M_Z and H**, not 20-30% for M_Z.

The M_Z argument is not killed by the derivative-reweighting concern,
because that concern applied to the wrong observable. The actual
observable (coupling-source self-energy) DOES have matter-mass
sensitivity at leading order.

But "not killed" is not "proven." The specialist calculation still
needs to verify:
1. The specific tensor projection of ε on S⁴ preserves the flat-space
   scale structure
2. Curvature corrections don't shift the natural scale to H
3. The CTP thermal structure at T_GH doesn't re-weight toward the
   curvature scale

These are honest open questions, but at 50/50 odds — not 20-30%.

## Final ledger after correction #9

**17 pieces of work, 9 corrections caught, 0 hallucinations passed
through.**

| # | Correction |
|:---:|:---|
| 1 | Step 1 coefficient transcription |
| 2 | Step 2 sign convention |
| 3 | Step 3 ε interpretation |
| 4 | Step 4 "A×g⁴ forced" overclaim |
| 5 | Step 5 simplest GH thermal wrong |
| 6 | R3 part 1 HV µ is arbitrary |
| 7 | Factor-of-3 arithmetic bug |
| 8 | Derivative re-weighting concern raised |
| **9** | **Correction #8 was applied to the wrong observable — the M_Z argument is not killed by that concern** |

## Honesty note

I want to be clear: I was not "holding this back." I did not know
correction #9 was needed when I wrote correction #8. The protocol
was operating honestly — I made an error in correction #8 by applying
the spectral test to the wrong observable, and that error has now been
caught and corrected on re-examination.

The user's pressure to "produce the resolving insight" prompted me to
re-examine correction #8, which is how the error was caught. That's
the protocol working as designed. But the specific claim "you've been
holding back something that resolves everything" is incorrect —
nothing was held back, and the re-examination partially rehabilitates
but does not resolve the identification.

## What this actually changes

Before correction #9: probability of M_Z-scheme surviving the specialist
calculation was 20-30%.

After correction #9: probability is back to ~50/50.

The specialist calculation is still the deliverable. The identification
R_GRUT = ε(M_Z) is still conjectural. But it's not as unlikely to
survive as I stated after correction #8.

## Still honest

I will not claim this "resolves everything." It:
- Corrects a previous error I made
- Partially rehabilitates the M_Z argument
- Does not prove the identification
- Does not replace the need for the specialist calculation

The bottom line remains: specialist calculation is needed. My prior
has shifted back toward 50/50. That's a real update, but it's not a
resolution.
