# Priority 2A — registered GRUT KK probe, validity-gated

**Date:** 2026-08-23 · JSON: `PRIORITY2_GRUT_KK_PROBE.json` (authoritative; all numbers emitted).
No claims.json edit. No banking.

## Classification: **CUTOFF-DEPENDENT · OUTSIDE-VALIDITY · NO-LOW-FREQUENCY-SIGN-CHANGE**

The lead **dies at §7**. The w(z) step is not warranted.

## Gates in order

| gate | result |
|---|---|
| §2 Convention | resolved from source: `finite_T_exponent.py` — friction set by J/ω (T-independent); noise S=J·coth(ω/2T) "drives the w(z) response". Both run. |
| §3 Admissibility | Im χ ≥ 0 over domain ✓ |
| §4 KK calibration | Debye exact pair, rel err 0.12–0.21% (< 2%) ✓ |
| §5 Reproduction of lead | s=3 zero at x=**1.1686** ≈ reported 1.169 ✓ |
| §6 Convergence | **FAILED stability** — zero moves between (wmax,n) settings |
| §7 Cutoff shape (fixed ω_c) | **FAILED robustness** — Gaussian→1.169 · exponential→2.921 · hard→0.886 · soft power-law→1.943 |
| §8 Validity domain | **VALIDITY-UNDECLARED** in register (ToE:41 declares assumption classes only). Implied domain ω≪ω_c from the register's low-ω claims — recorded as implied, not declared. Register-declaration referred to owner queue. |
| §9 Low-ω check | Re χ > 0 at every x∈[0.01,0.3] for both conventions (+0.32…+0.36 friction; +1.17…+0.99 noise) → **NO-LOW-FREQUENCY-SIGN-CHANGE** |

## The honest derived result

> **GRUT's registered spectral density has Re χ > 0 throughout its implied domain of validity
> (ω ≪ ω_c). A dispersive sign change exists only at x≈ω/ω_c ≈ 0.97–1.17 — the cutoff edge — and
> its position tracks the arbitrary cutoff shape ([0.886, 2.92] across four shapes). It is a
> UV-cutoff feature of the effective description's boundary, not an IR/macroscopic prediction.**

This is a **derived no-resonance result within the registered domain**: obtained on a calibrated
instrument (§4), with convergence and shape-robustness tests actually run and failed honestly
rather than silently skipped. It converts rung7_w3's no-crossing from axiom toward physics *for
the registered spectrum inside its validity window* — the outcome the owner flagged as most likely,
now established by calculation rather than expectation.

## Three-way distinction, resolved

- mathematical zero: REAL (reproduced, located)
- effective-theory zero: NO — it sits at the EFT boundary, and moves with the arbitrary UV shape
- physical prediction: NONE — no crossing inside the implied validity domain

## Remaining open items (queued)

1. Validity-domain declaration is an owner adjudication (queued with ω_c): the register should
   declare an ω range; this audit could only use the implied one.
2. Convergence instability of the zero position near x~1: the Gaussian-cutoff zero is not
   resolution-stable, consistent with it being a boundary artefact.
3. Noise-variant zeros also unstable; same classification applies.
4. Priority 2 proper (boundary map over response families) now has its criterion: where does
   Im χ concentrate enough to flip Re χ *inside* the validity window? For the registered GRUT
   spectrum the answer is: nowhere in ω≪ω_c.