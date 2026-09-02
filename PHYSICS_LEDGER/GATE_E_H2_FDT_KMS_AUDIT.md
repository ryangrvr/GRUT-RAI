# GATE-E — FDT/KMS CONSISTENCY VERIFICATION AT O(H²): AUDIT RECORD

**Date:** 2026-09-01 · **Instrument:** `wall_kr_gate_e_fdt_kms.py` ·
**Artifact:** `GATE_E_H2_FDT_KMS_RESULT.json` · **Battery: 32/32,
zero failures, six controls detecting.** · **Frozen inputs and register:
byte-identical before and after.** · **W-0: unbanked. HARD STOP.**

## CLASSIFICATION: **GATE-E-A**

**The FDT/KMS lock PASSES at O(H⁰), O(H¹) and O(H²), within the declared
validity domain (ω ≫ H). Nothing is claimed at ω ~ H or ω → 0.**

| order | verdict | content |
|---|---|---|
| H⁰ | **PASS** | support identity + exact coefficient match |
| H¹ | **PASS** | demonstrated, not skipped: both sides ≡ 0, each computed |
| H² | **PASS** | support identity + exact coefficient match |

## 1. THE REGISTERED CRITERION (three sources, composed — no conflict)

- **Charter gate E** (verbatim): "the retarded/noise (K_R, N) pair
  verified against the rung2 FDT lock; normalization by derived theorem
  gate; TT reduction strictly downstream."
- **rung2 register node** (verbatim): "the noise kernel N is locked to
  Im[χ] by FDT with a coth(ħω/2kT) factor; admissible kernels must
  satisfy KMS detailed balance" — enforced as the residual
  |G_K − coth·(G_R − G_A)|.
- **Frozen Tier-2 graded form**: the T = 0 lock, N(ω) = ½ sgn(ω) ρ(ω)
  per order — with the KMS scope note that the dS temperature H/2π is
  non-perturbative: exp(−2πω/H) vanishes to all orders in the H grading.

**The coth → sgn grading was DERIVED, not asserted:** coth(πω/H) − 1 =
2/(exp(2πω/H) − 1) has vanishing H-limit *and* vanishing first and
second H-derivatives at fixed ω > 0. The composed per-order relation:

    R_n(omega) = [Sig_> + Sig_<]_n - sgn(omega) [Sig_> - Sig_<]_n == 0
    (on-cone content, per H order, on the controlled domain)

**Structural exclusion of the unresolved locals:** Σ_K carries no θ(Δ),
hence no PV/dispersive part — the unresolved local real terms (c0′,
c2′, the Λ_R slot) are real polynomials in the *dispersive* sector and
**cannot enter either side**. Excluded by the structure of the
registered relation, not by assumption — no Gate-E outcome can
back-propagate into the IR decision.

## ROUTE A — SUPPORT SEPARATION (structural, per order)

From the frozen T3 Wightman integrands (Σ_>, Σ_<), cone-split per H
order in the common Wigner frame:

| order | Σ_> wrong-branch | Σ_< wrong-branch | strays |
|---|---|---|---|
| H⁰ | ≡ 0 | ≡ 0 | none |
| H¹ | (entire order ≡ 0) | (entire order ≡ 0) | none |
| H² | **≡ 0** | **≡ 0** | none |

**Support separation holds exactly through O(H²):** Σ_> carries only
positive-frequency content, Σ_< only negative. For ω > 0 the on-cone
content of Σ_< vanishes, so R_n = 2·Σ_<,n = 0 **identically** — the
graded T = 0 lock is a *support identity* per order, independent of the
radial integration and hence untouched by any IR structure. (H¹
vanishes for each Wightman function *individually* — stronger than the
certified retarded H¹ ≡ 0.)

## ROUTE B — INDEPENDENT COEFFICIENT TEST

The noise combination's on-cone content, extracted from the Σ_>/Σ_<
cones by a delta-support formula **calibrated against an independent
Gaussian-damped numeric Fourier transform** (exact Gaussian moments in
Δ, numeric q integral, linear η-Richardson to the numeric floor, with a
perturbed-formula teeth-control), compared against the **certified
retarded absorptive values** through the exact frozen-orientation
conversion [Σ_> − Σ_<]_oncone = −2 Im Σ_R:

| order | noise pipeline | −2 × certified Im Σ_R | match |
|---|---|---|---|
| H⁰ | 3ω⁴/(640π) | 3ω⁴/(640π) | **EXACT** |
| H¹ | 0 | 0 | **EXACT** |
| H² | 13ω²/(240π) per H² | 13ω²/(240π) per H² | **EXACT** |

The two routes share no intermediate objects.

## IR ANALYSIS AND VALIDITY BOUNDARY (brief §6: classification A)

The relation constrains **on-cone content only**; at fixed ω > 0 the
delta pins q = ω/2, strictly away from q = 0 — no radial IR integration
enters either side. The certified H² retarded LOG divergence lives in
the PV/local sector, which the lock never sees. **No IR regulator was
introduced — none is needed.** The frozen noise α = −2 record (the
small-q-expanded integrand's 1/q² coefficient 4ω⁴/15) describes the
q → 0 / ω → 0 zero-mode regime, **outside** the controlled domain:
echoed for provenance, **not consumed, not resolved**. Domain identical
to the retarded contract: ω ≫ H controlled; ω ~ H boundary; ω ≪ H out
of scope.

## DIMENSIONS / SCALING

H⁰ content homogeneous of degree 4, H² of degree 2 in ω — matching the
certified retarded scalings; **full coefficients tested**, not
exponents alone.

## NEGATIVE CONTROLS — all detecting

Wrong retarded sign; wrong factor of two in N; **wrong KMS factor**
(coth at ad hoc numeric T = 0.3 leaves a nonzero residual while the
registered graded factor leaves ~0); perturbed H² noise coefficient
(+10%); **support-separation teeth** (an injected wrong-branch term in
Σ_> is caught — the loop-level analogue of Tier-2's wrong-state
control); outcome-token scanner with runtime sentinel.

## DEFECT HISTORY (all mine, gate-side, disclosed)

Extraction run 1 died on memory (full symbolic expand of the graded
identity — swap-death lesson reapplied: numeric 6-point exact-rational
identity check, disclosed in the cache). Run 2 exposed a **frame
mismatch in my own check** — Σ_>/Σ_< cached in (u, u′) variables, nk in
Wigner variables. Battery run 1: the cones' TT-trace **d never
substituted**, and the delta formula used (+i/2)ⁿ where the frozen
transform convention gives (−i/2)ⁿ — with a toy "calibration" that
derived both sides by the same hand algebra, so the shared error passed
(**the calibration trap**; replaced by the independent damped-FT
reference). Runs 2–3: Richardson h²-weights on a linear-in-η error,
then a strict-improvement test that rejected exact convergence (0 < 0).
The physics never moved.

## INTERPRETATION FIREWALL (verbatim in the artifact)

A Gate-E pass does **NOT**: fix c0′; fix c2′; fix Λ_R; remove the H² IR
fork; prove GRUT; establish a unique thermal state; establish a pole.
**H² local fork: UNRESOLVED, unchanged. Noise fork: untouched. Axis-2:
C, unchanged. Λ_R: ONE, unchanged. New input: NONE.**

## HARD STOP

Gate-E is a consistency lock, and it locked. Owner's desk: the standing
queue (noise fork; T4 + consequence-cell adjudications; the fork-(ii)
option). No subsequent stage is entered automatically.
