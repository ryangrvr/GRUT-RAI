# RRT1_REDUCIBILITY_CORRECTION.md — CORRECTS THE ESCAPE-CONDITION CLAIM OF THE DESIGN AUDIT

Status: **ANALYTIC CORRECTION AUDIT.** No simulation battery, no RRT-0 modification, no RRT-1
build. Supersedes specific claims of `RRT1_DESIGN_SPACE_AUDIT.md` (`3f313ce`) named below; that
file is preserved byte-identical as provenance. Numerical confirmation is a 3-line d=4 check,
recorded, not a campaign. Provenance: branch `rrt0-phase2`, HEAD `3f313ce`.

## 0 · THE CATCH (owner, adopted in full)

The design audit claimed the RRT-0 no-go rests on **invertibility (R2)** and that a general
CPTP channel "breaks the exact minimal escape condition." **Both claims are FALSE.** The
response-reducibility identity uses only **linearity** — no inverse anywhere — so it holds for
the entire linear dynamical universe, invertible or not, unitary or dissipative. The following
sections in the prior audit are **CORRECTED and superseded**: §1 (naming R2 load-bearing), §3
(minimum escape = loss of invertibility), and the §8 justification insofar as it claims a
general channel *escapes* the no-go. The candidate comparison, the input ledger, the mirror
design, and the fixed-point/first-theorem analysis **survive** — and become MORE central.

## 1 · THE GENERALIZED IDENTITY (proved; assumptions exact)

For ANY linear map 𝒯 on operators, any intervention map E, discrete step count n:

    Δ_n := 𝒯ⁿ(E[ρ]) − 𝒯ⁿ(ρ) = 𝒯ⁿ(E[ρ] − ρ) = 𝒯ⁿ((E−I)[ρ]).

One line, from linearity of 𝒯ⁿ alone: 𝒯ⁿ(A) − 𝒯ⁿ(B) = 𝒯ⁿ(A−B). **No inverse, no unitarity,
no trace preservation, no complete positivity is used.**

**Exact assumptions required for `Δ_residual ≡ 0` (response reducibility):**
1. **𝒯 linear** in the operator ρ (so 𝒯ⁿ is linear). — LOAD-BEARING.
2. **E linear or affine** in ρ (E[ρ] = (1−λ)ρ + λσ is affine; the difference E[ρ]−ρ is linear
   in ρ, = λ(σ−ρ)... note σ may depend on ρ; for the canonical σ_α FIXED this is affine and
   the identity holds exactly). — LOAD-BEARING.
3. **Readout linear** (Tr[B·]). — LOAD-BEARING for the scalar statistic.
**NOT required:** invertibility of 𝒯; unitarity; CPTP; a semigroup property; a fixed point.

**What the earlier "U^{−τ}" was.** The RRT-0 gate wrote Δ = U^τ[E−ρ]U^{−τ}. The U^{−τ} = (U†)^τ
is the RIGHT factor of the FORWARD conjugation channel 𝒯(X)=UXU† applied τ times, 𝒯^τ(X) =
U^τ X (U†)^τ. It is **not a channel inverse** and is applied forward in both Δ_raw and
Δ_supplied. The mistake in the design audit was reading that (U†)^τ as "un-propagation
requiring invertibility." It is nothing of the kind.

## 2 · NUMERICAL CONFIRMATION (d=4, three genuinely non-invertible channels)

Δ_raw − 𝒯ⁿ((E−I)ρ), Frobenius norm, over n ∈ {1,3,7}:

| channel | invertible | max residual |
|---|---|---|
| depolarizing (p=0.7) | NO | 5.3e-17 |
| amplitude damping (g=0.3), non-unital | NO | 4.3e-17 |
| full reset → rank-1 |onto \|0><0\| | NO (rank collapse) | 2.8e-17 |
| Lindblad e^{t𝓛}, t ∈ {0.5, 2.0} | generally NO | ≤ 9.5e-17 |

Machine-zero in every case, including total rank collapse. **Non-invertibility does not perturb
the identity at all.** Continuous time confirmed via the superoperator exponential:
Δ(t) = e^{t𝓛}((E−I)ρ), holding for any generator 𝓛.

## 3 · FOUR DISTINCT PROPOSITIONS (the design audit conflated the first two)

| proposition | statement | holds iff | invertibility role |
|---|---|---|---|
| **P1 response reducibility** | Δ = 𝒯ⁿ((E−I)ρ) | 𝒯, E, readout **linear** | **NONE** — holds invertible or not |
| **P2 state recoverability** | ρ₀ recoverable from ρ_t = 𝒯ᵗ(ρ₀) | 𝒯 **invertible** | THIS is where invertibility lives |
| **P3 asymptotic-structure reducibility** | attractors/pointer/DFS reduce to Fix(𝒯), peripheral algebra | function of 𝒯's spectral data | non-invertibility CREATES the structure |
| **P4 operator-algebra reducibility** | emergent preferred algebra = a function of the generator's algebra | governed by Fix/Comm{L_a} | as P3 |

**The RRT-0 gate tests P1.** The design audit imported P2's invertibility condition into P1 by
mistake. P1 is escaped ONLY by abandoning linearity (of the dynamics, the intervention, or the
readout). P2/P3/P4 are separate questions where invertibility and dissipation DO matter — but
they are not the RRT-0 response quantity.

## 4 · CORRECTED MINIMUM ESCAPE CONDITION

**For P1 (the RRT-0 reducibility quantity): the minimum escape condition is LOSS OF
LINEARITY — not loss of invertibility, not dissipation, not non-unitarity, not information
loss.** The full corrected hierarchy (owner's table, verified):

| dynamics | linear | invertible | P1 response-reducible |
|---|---|---|---|
| unitary | yes | yes | **YES** |
| non-unitary invertible | yes | yes | **YES** |
| non-unitary non-invertible | yes | no | **YES** |
| CPTP channel | yes | often no | **YES** |
| Lindblad e^{t𝓛} | yes | generally no | **YES** |
| **nonlinear dynamics / nonlinear E / nonlinear readout** | **NO** | — | **POTENTIAL ESCAPE** |

**RRT-0 discovered a broader no-go than it was designed to find: linearity alone makes
intervention-response reducibility robust across essentially the entire linear dynamical
universe, dissipative channels and Lindbladians included.** This is the audit's real result and
it is bigger than the RRT-1 question it was meant to set up.

## 5 · WHAT THIS DOES TO RRT-1

The design audit's recommendation (a general channel, "because it breaks invertibility cheaply")
is **withdrawn as justified** — a general channel does NOT break P1. The corrected RRT-1
landscape has TWO genuinely distinct forks, and the choice between them is now the real design
decision:

**FORK A — keep linearity, change the QUESTION from P1 to P3/P4.**
Accept that P1 is a dead quantity for all linear dynamics. Ask instead: *does the ASYMPTOTIC /
operator-algebra organization of a supplied linear irreversible map exceed what is encoded in
its own Fix/peripheral/decoherence algebra?* This keeps the model class cheap (channels,
Lindblad as sub-case) and honest. **Prediction (operator-algebra prior, unchanged):
generically NO — asymptotics reduce to Fix(𝒯); a positive result lives only in the
non-generic/transient regime.** So Fork A most likely yields **another no-go class** (open
linear quantum dynamics adds nothing beyond its supplied algebra), which is itself a valuable
elimination — exactly the owner's "brutal result."

**FORK B — abandon linearity (the only P1 escape).**
Nonlinear ρ-dynamics (e.g. mean-field / ρ-dependent generator), OR a ρ-dependent intervention
E[ρ], OR a nonlinear readout. This is the ONLY way the original RRT-0 response quantity can
become irreducible. But nonlinearity is a heavy, physically loaded input (nonlinear QM is
non-standard and has its own no-gos — Gisin signalling), and it must be declared and firewalled
as such: a nonlinear model that "produces structure" has supplied the nonlinearity that does it.

**Recommendation, corrected:** do **Fork A first**, as a design-grade **no-go attempt**, not an
emergence hunt — the strongest defensible RRT-1 is "prove open linear quantum dynamics is
P3/P4-reducible to its supplied algebra, or exhibit the exact non-generic residual that isn't."
Reserve Fork B (nonlinearity) as the named, expensive, honesty-fenced alternative to open ONLY
if Fork A's no-go closes and the question is still worth the cost. Do NOT adopt Lindblad or any
channel as an "emergence" instrument under the P1 framing — that framing is now closed.

## 6 · WHAT CANNOT BE CONCLUDED

That open/dissipative systems have no interesting structure (false — P3 attractors, pointer
states, DFS all exist; the claim is only that they are functions of the supplied 𝒯). That
nonlinearity WILL yield irreducible organization (unknown; only that it is the sole P1 escape).
Anything about the RAI half-line/KMS residue (still inexpressible in finite type-I). No transfer
of RRT-0's PASSes to any new class.

## CORRECTION SUMMARY (supersedes RRT1_DESIGN_SPACE_AUDIT.md §1, §3, §8-justification)

- Minimum escape from the RRT-0 response no-go is **loss of LINEARITY**, not invertibility.
- The identity Δ = 𝒯ⁿ((E−I)ρ) holds for **all linear 𝒯** (proved; confirmed on non-invertible
  and rank-collapsing channels and on Lindblad e^{t𝓛} at machine precision).
- The four propositions P1–P4 are distinct; RRT-0 tests P1; invertibility governs P2, not P1.
- RRT-1 should be posed as a P3/P4 **no-go attempt on open LINEAR dynamics (Fork A)**, with
  nonlinearity (Fork B) as the fenced, expensive, only-true-P1-escape alternative.
- RRT-0's finding is upgraded: **a linear-universe-wide response no-go**, broader than intended.

## STOP-POINT
Analytic correction only. No RRT-1 build, no battery, no RRT-0 change, no commit pending
authorization.
