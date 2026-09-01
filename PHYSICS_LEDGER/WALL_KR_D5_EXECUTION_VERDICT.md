# D5 EXECUTION UNDER THE OWNER'S SCHEME RULING (Option β): RESULT

**Date:** 2026-09-01 · **Ruling:** Option **β** — extend the
already-authorized D3/Option-3a *spatial* continuation to the direct
real/local sector. A **scheme ruling, not a spectral choice.** ·
**Instrument:** `wall_kr_d5_execution.py` · **Artifact:**
`WALL_KR_D5_EXECUTION_RESULT.json` (sha `b60cecc2f7d356f7…`) ·
**Battery: 27/27, zero failures, every control detecting.**
**W-0: computed-and-reported, NOT banked. HARD STOP.**

> **THE SCHEME MAY BE DECLARED. THE FINITE LOCAL NUMBERS MAY ONLY BE
> CALCULATED.** (owner, verbatim — the governing principle, and the
> instrument was built so the machine enforces it)

## THE OBJECTIVE, MET

*"Prove that the D3-extended local renormalization calculation is
numerically and analytically valid."* — **Proven at H⁰.** The direct
(non-dispersive) retarded integral was assembled in closed form from the
frozen Tier-3 cone data, continued in the declared spatial d = 3 − 2ε,
and MS-subtracted pole-only per the frozen Declaration-1 doctrine.

## THE D5 OUTPUT — calculated, never chosen

    Sigma_R^direct(omega) = omega^(d+1) mu^(3-d) F(d)     [SCALE-FREE]

    1/eps pole   :  -(3/1280 pi^2) omega^4 / eps
    MS finite    :  A omega^4 [ L - 6841/2835 - EulerGamma + log(4 pi) ]
                    + i pi A omega^4        (the frozen absorptive part)
    A = -3/(1280 pi^2),  L = log(mu^2/omega^2)

**The local slot, determined:**

| slot | value | status |
|---|---|---|
| c0 | **0** | EXACT, structural |
| c2 | **0** | EXACT, structural |
| c4 | A·(−6841/2835 − γ_E + log 4π) ≈ **+1.0906×10⁻⁴** (μ = 1) | CALCULATED |
| c0p, c2p | not computed | H² sector **fork-gated** (T3-1 fenced) |

**c0 = c2 = 0 is a structural result, not a choice:** the H⁰ integrand
is scale-free, so the direct result is a *single power* ω^(d+1) — it
cannot generate ω⁰ or ω² at this order. That expectation was **declared
in the instrument's header before the computation ran**, then verified
as a gate. The five-constant ambiguity the consequence stage faced is
reduced at H⁰ to **one computed number plus the declared symbolic μ.**

## VALIDATION

- **Master integrals — convergence ladder** (the owner's mandated
  repair, replacing a tolerance that had been set below the method's
  reach): J₊ rel **3.6e-05 → 1.2e-08 → 3.2e-13**, J₋(PV) **4.8e-05 →
  1.6e-08 → 4.2e-13** — monotone at ≥3 decades per refinement step,
  final below the **declared** 1e-12. The rate is the evidence; the
  threshold was declared at what the method demonstrably reaches, never
  relaxed to cover a standing discrepancy. J₋'s imaginary part matches
  π x^(a−1) to <1e-25 (the retarded i0 pole crossing).
- **Ladder negative control:** against a reference perturbed by 1 part
  in 1e9 the ladder **plateaus** (3.6e-05 → 1.3e-08 → 1.0e-09) instead
  of converging — the criterion detects a wrong target and is not
  merely rewarding refinement.
- **ANCHOR 1 (nonlocal):** the direct route's log coefficient **and**
  the 1/ε pole residue both equal the frozen Tier-4 dispersive value
  −3/(1280π²) **exactly** — two independent routes, one nonlocal answer.
- **POLE/LOG relation, independently:** expanding at L = 1 and L = 3
  gives finite parts differing by exactly A·(L₂−L₁) — pole and log are
  one object, verified without differentiating the symbolic result.
- **ANCHOR 2 (absorptive):** Im of the direct MS result equals the
  frozen −3ω⁴/(1280π) exactly. **Im K_R is unchanged**, and the
  local/absorptive separation is gated (the finite remainder's
  imaginary part is exactly πA — absorptive content, not a local term).
- **Independent renormalization check:** numeric evaluation of F(d) at
  ε = 1e-3, 3e-4 reproduces pole/ε + finite (rel 1.7e-05, O(ε)-limited).
- **BASIS FIT (1b):** the UV pole is pure ω⁴ × constant — it maps onto
  the frozen basis's curvature-squared class; no operator outside the
  frozen basis is needed.
- **Controls, all detecting:** wrong regulator continuation, wrong
  finite-local coefficient, wrong renormalization sign, accidental Im
  alteration, benchmark-tuned local constant.

## TWO FINDINGS FROM FAILED GATES (disclosed, not smoothed)

1. **My first "wrong regulator" control was ill-posed.** It flipped
   d = 3−2ε → 3+2ε and demanded the MS finite part change. It did not,
   and the control read ctrl-MISSED. The reason is a **theorem**: for
   F = A/δ + B, both parameterizations give finite part B − AL/2. The
   ε-sign invariance is a consistency property, now **recorded as such**
   and the control **rebuilt** around a genuinely wrong scheme —
   continuing the measure in d while freezing the projector algebra at
   d = 3 (the classic dropped-evanescent-terms error), which does change
   the finite part and is now detected.
2. **Earlier runs' red gates were gate defects, not physics.** The
   master formulas were right from the start (J₊ agreed to 1.4e-14, J₋'s
   Im part exactly); my tolerances were unreachable, and one anchor
   compared A·ω⁴ against a per-ω⁴ constant — a dimensional mismatch in
   my own comparison. A literally vacuous gate ()
   was also shipped and is now replaced; the instrument contains **zero**
    gates.

## BOUNDARIES HONORED

Frozen nonlocal K_R, its absorptive part, branch structure and s-class:
**unaltered** (all four upstream artifact hashes re-verified after the
run). No local constant chosen by hand. Nothing tuned to any Axis-2
outcome. Declaration-1's spacetime scheme **retained as a recorded,
unresolved alternative** (Option α), with the PV-pattern
scheme-independence demonstration (Option γ) still open. H² sector
**not executed** — fork-gated.

**Axis 2: NOT COMPUTED**, per the owner's continuation directive
("finish the renormalization audit first"). *Disclosure:* a preliminary
Axis-2 reading appears in the on-disk logs of the **red** pre-repair
runs (`wall_kr_d5_exec_run2/3/4.log`); it is uncertified, not carried
into the artifact, and not relied on anywhere. It is named here only
because it exists on disk.

## HARD STOP

The H⁰ local renormalization is valid and its constants are determined.
Axis 2 awaits its own authorization; the H² locals await the fork
ruling.
