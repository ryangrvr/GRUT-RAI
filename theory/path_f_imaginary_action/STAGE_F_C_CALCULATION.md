# Path F-C — Conformal-Mode + SM Trace Anomaly Calculation

**Date:** April 26, 2026
**Stage:** F-C (Candidate II from F.0).
**Goal:** Test whether including the graviton/conformal-mode contribution with explicit sign tracking (per V7 §26.2.3a's no-rotation convention) reproduces V7's R = 1.15428.
**Result:** **No.** F-C produces values clustering around Path D's 1.17 ± 0.01 with the conformal-mode-only convention, or wildly different values when the full graviton is included. **V7's specific 1.15428 is not reproducible by this in-pipeline calculation.**

---

## F-C.1 — Sourced graviton trace-anomaly constraint

From Duff 1994 (arXiv:hep-th/9308075, page 17, Table 1) and Duff "40 years of the Weyl anomaly" (TAMU slides, p. 15), the Christensen-Duff per-spin formula is:

    A_total = 4 N_0 + 7 N_{1/2} − 52 N_1 − 233 N_{3/2} + 848 N_2

where `A` corresponds to `2(c − a)·360` in KS 2011 conventions.

**Verification against KS 2011 per-species values:**

| Field | KS (a, c) | 2(c − a) | Duff A | Match |
|:---|:---|:---:|:---:|:---:|
| Real scalar | (1, 3) | 4 | 4 | ✓ |
| Weyl fermion | (11/2, 9) | 7 | 7 | ✓ |
| Gauge field | (62, 36) | −52 | −52 | ✓ |
| Graviton (spin-2) | unknown individually | **848** | **848** | constraint only |

**Critical: the graviton's individual a and c are NOT cleanly available in literature** at the same authoritative level as KS's (1,3), (11/2, 9), (62, 36). The Christensen-Duff formula gives `2(c_grav − a_grav) = 848`, equivalently `c_grav − a_grav = 424`. Individual values depend on gauge-fixing convention, ghost handling, and whether de Donder vs harmonic gauge is used. We have one constraint, two unknowns.

This is a structural limit on F-C that wasn't apparent until we tried.

---

## F-C.2 — Calculation under multiple conventions

We computed the SM-matter + graviton-related a/c ratio under five conventions:

### Path D baseline (SM matter only, no graviton)

```
a_SM = 1991/2 = 995.5
c_SM = 849
a_SM / c_SM = 1991/1698 ≈ 1.17256
```

### Convention A: Conformal-mode only, V7's no-rotation convention

Per V7 §26.2.3a line 1735: "GRUT does not need the Gibbons-Hawking rotation. The −100 is not a pathology to be hidden by contour rotation — it is the topological drive for cosmic expansion."

Interpretation: the conformal mode (single scalar trace mode of the graviton) contributes with NEGATIVE sign in V7's no-rotation convention (the GHP wrong-sign kinetic term is kept rather than absorbed by Ω → iΩ). So conformal-mode contribution = `(−1) × (real scalar contribution)`:

```
a_total = 1991/2 + (−1) = 1989/2
c_total = 849 + (−3) = 846
a/c = 1989/1692 = 221/188 ≈ 1.17553
```

This is **0.30% above Path D**, slightly further from V7's 1.15428.

### Convention B: Conformal-mode only, standard GHP rotation (positive)

If we treat the conformal mode like a normal real scalar (after Ω → iΩ rotation):

```
a_total = 1991/2 + 1 = 1993/2
c_total = 849 + 3 = 852
a/c = 1993/1704 ≈ 1.16960
```

**0.25% below Path D**, slightly closer to V7's 1.15428 but still 1.34% off.

### Convention C: Full graviton with constraint 2(c_grav − a_grav) = 848

Treating graviton as a parameter family with a_grav free, c_grav = a_grav + 424:

| a_grav | a_total | c_total | a/c |
|:---:|:---:|:---:|:---:|
| 0 | 995.5 | 1273 | 0.7820 |
| 100 | 1095.5 | 1373 | 0.7979 |
| 212 | 1207.5 | 1485 | 0.8131 |
| 717 (Christensen-Duff std?) | 1712.5 | 1990 | 0.8606 |
| 1000 | 1995.5 | 2273 | 0.8779 |
| −100 | 895.5 | 1173 | 0.7634 |
| −424 (c_grav = 0 case) | 571.5 | 849 | 0.6731 |

**All values < 1**, very different from V7's 1.15 or Path D's 1.17. **Adding the full graviton with c_grav > a_grav (which is the structural constraint) shifts a/c well below 1.**

### Convention D: V7 no-rotation flips the graviton sign overall

If V7's no-rotation convention applies to the WHOLE graviton (not just the conformal scalar mode), the constraint becomes `2(c_grav − a_grav) = −848`, equivalently `c_grav − a_grav = −424`:

| a_grav | a_total | c_total | a/c |
|:---:|:---:|:---:|:---:|
| 0 | 995.5 | 425 | 2.342 |
| −100 | 895.5 | 325 | 2.755 |
| −212 | 783.5 | 213 | 3.678 |
| −500 | (495.5) | (−75 unphysical) | — |
| −717 | (278.5) | (−292 unphysical) | — |

Some values give a/c much > 2, putting `f(R) = 2 − R < 0` and producing imaginary H_inf. **Most parameter values are unphysical or far from any sensible target.**

---

## F-C.3 — What the calculation actually shows

| Convention | a/c | Δ from V7's 1.15428 |
|:---|:---:|:---:|
| Path D (SM only) | 1.17256 | +1.58% |
| Convention A (conf-mode neg) | 1.17553 | +1.84% |
| Convention B (conf-mode pos) | 1.16960 | +1.33% |
| Convention C (full grav, a_g any) | 0.67–0.88 | far off |
| Convention D (V7 sign-flip on full grav) | 2.34–3.68+ | far off, often unphysical |

**Observations:**

1. **Conformal-mode-only contributions barely move the answer** from Path D's 1.17. Whether the conformal mode is added with V7's negative convention or standard positive convention, the result stays in 1.17 ± 0.01. The 1-loop conformal-mode contribution alone doesn't get us to 1.15.

2. **Including the full graviton (Conventions C and D) produces values far from V7's 1.15** under any value of the unknown a_graviton. The graviton's c_grav − a_grav = 424 is too large a perturbation; it dominates the SM matter contribution and shifts a/c dramatically.

3. **None of these in-pipeline conventions reproduces V7's 1.15428.** The closest is Convention B at 1.34% off; the conformal-mode-only convention from V7's narrative gives 1.17–1.18, not 1.15.

---

## F-C.4 — Honest verdict

**Path F-C, run as a Candidate II in-pipeline calculation, does not reproduce V7's 1.15428.** The closest values (Conventions A and B) are ~1.17, the same regime as Path D, with small ~0.3% shifts depending on conformal-mode sign convention. Including the full graviton produces dramatically different values (0.67 or 2.34, depending on sign convention) that don't match V7 or Path D.

**Why this happens:**

V7's R = 1.15428 comes from specific 3-loop transcendental expressions:

```
C_FINAL  = 3(99 + 2π² + 576 ln2 ζ_3) / (16384 π⁶)  ≈  1.140 × 10⁻⁴
C_Cosmo = (−108000 + π⁴ + 1536 π⁴ ln2 + 540 ζ_3) / (276480 π⁴)  ≈  −1.316 × 10⁻⁴
R = |C_Cosmo / C_FINAL| ≈ 1.15428
```

These are specific 3-loop CTP-on-S⁴ Feynman-diagram outputs. The integers (99, 576, −108000, 540) and transcendentals (π², π⁴, ζ_3, ln 2) come from specific 3-loop integrals on Euclidean S⁴, not from 1-loop trace anomaly coefficient combinations.

**Path F-C combines 1-loop coefficients with various sign-tracking conventions; that's not the same calculation.** The graviton constraint `2(c_grav − a_grav) = 848` from Christensen-Duff is correct as a 1-loop result, but combining it with SM matter at 1-loop gives a 1-loop ratio, which V7's 3-loop transcendental result doesn't have to match.

In other words: **F-C is computing a DIFFERENT object than V7's R, just like Path D was.** Path D was 1-loop a/c with no graviton. F-C is 1-loop a/c with graviton. Both are real calculations, but neither is V7's 3-loop CTP transcendental.

---

## F-C.5 — What F-C does establish

F-C, despite not reproducing 1.15428, has produced a real result:

1. **The graviton/conformal-mode contribution doesn't significantly shift the 1-loop a/c result** (in the conformal-mode-only convention). The number stays in 1.17 ± 0.01.

2. **The full-graviton contribution produces dramatic shifts** that don't land near 1.15. Including the graviton at 1-loop in any convention C or D way gives a/c far from any sensible cosmological target.

3. **The original 1.15428 must come from beyond-1-loop machinery.** Specifically, the 3-loop CTP-on-S⁴ calculation V7 §26.2 outlined. F-C confirms this — 1-loop combinations don't reproduce V7's number under any convention we tried.

**This is a positive finding.** It tells us that V7's R = 1.15428 is genuinely a 3-loop transcendental result, not a 1-loop ratio. And it tells us that Path D's 1.17256 is the cleanest 1-loop derivation available.

---

## F-C.6 — Where this lands

**For "priority one is the proper derivation":**

The proper 1-loop derivation is Path D's 1991/1698 ≈ 1.17256 (or 1.15525 with Dirac neutrinos). This is the most defensible in-pipeline number we have.

The proper 3-loop derivation that would reproduce V7's 1.15428 requires the TJI Phase-1 specialist work outlined in V7 §26.2.5. F-C cannot shortcut this — including the graviton at 1-loop doesn't bridge the gap from 1.17 to 1.15.

**Three honest options for what GRUT's R is:**

| Option | R value | Provenance | 4% Planck tension? |
|:---|:---:|:---|:---|
| **Path D (canonical 1-loop)** | 1.17256 | KS + Duff sourced; full SM with Majorana ν | yes (4.06% below) |
| **Path D + Dirac ν (1-loop)** | 1.15525 | Path D + 3 RH neutrinos | no (0.01% below) |
| **V7 historical (3-loop transcendental)** | 1.15428 | Outlined in V7 §26.2; specialist verification pending | no (0.22% above) |

The 1.15525 (Dirac ν) and 1.15428 (V7 historical) values are within 0.08% of each other. Both differ from Path D's 1.17256 by ~1.5%. **F-C did not collapse this ambiguity.**

---

## F-C.7 — Recommendation

Given priority one is proper derivation:

**Path D's 1.17256 is the cleanest in-pipeline derivation that survives F-C's audit.** It's full-SM, 1-loop, sourced. F-C established that adding 1-loop graviton contributions doesn't significantly change it (under conformal-mode-only conventions), and that the 3-loop V7 result requires specialist work to verify.

If you commit to Path D, you commit to:
- R = 1991/1698 ≈ 1.17256 (or 253/219 ≈ 1.15525 with Dirac ν as a discoverable contingency)
- Ω_Λ = 0.6609 (Majorana) or 0.6888 (Dirac), 4% or 0.01% Planck tension respectively
- Reframing V7 §12 as "1-loop derivation, with 3-loop refinement pending specialist TJI work"

If you don't commit yet:
- F-C has confirmed F.0's structural finding: V7's 1.15428 is a 3-loop transcendental, not reproducible by 1-loop assembly
- Path D is the cleanest 1-loop derivation we have
- TJI Phase-1 specialist work is the next-step that could produce or refute V7's specific number

**F-C does not change the recommendation from Stage F.0.** The honest path forward is either commit to Path D (with appropriate caveats) or defer to specialist for full 3-loop verification.

---

## Sources

- [Duff 1994 "Twenty years of the Weyl anomaly" (arXiv:hep-th/9308075)](https://arxiv.org/abs/hep-th/9308075) — Table 1 gives 2(c−a) per spin
- [Duff "40 years of the Weyl anomaly" TAMU slides (2017)](https://cft.physics.tamu.edu/Slides/Duff.pdf) — confirms A_total formula with N_0...N_2 coefficients 4, 7, −52, −233, 848
- [Komargodski-Schwimmer 2011 (arXiv:1107.3987)](https://arxiv.org/abs/1107.3987) — per-species (a, c) for matter fields
- V7 local: §26.2.3a (lines 1735, 1743) for no-rotation convention
- V7 local: §26.2 for the 3-loop transcendental form of C_FINAL and C_Cosmo
