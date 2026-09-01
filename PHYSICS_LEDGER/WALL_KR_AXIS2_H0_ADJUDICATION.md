# AXIS-2 ADJUDICATION AT H⁰ — RECORD

**Date:** 2026-09-01 · **Authorization:** owner, post-D5 gate (H⁰ only) ·
**Instrument:** `wall_kr_axis2_h0.py` · **Artifact:**
`WALL_KR_AXIS2_H0_RESULT.json` · **Battery: 30/30, zero failures, all
four controls detecting.** · **Frozen inputs touched: NONE** (every
upstream artifact re-hashed byte-identical after the run).
**W-0: computed-and-reported, NOT banked. HARD STOP.**

## FINAL CLASSIFICATION: **C — INDETERMINATE**

Not because the calculation failed, and not because the local terms are
unknown — they are now determined. **C because exactly one required
input remains unresolved by the frozen record: the renormalization
scale μ, in plant units.** Declaration 1 orders μ *"kept symbolic and
its dependence recorded"*; Option β ruled the **continuation**, not the
scale. The instrument searched for a μ pinning and found none, so no
numeric μ was adopted.

## 1. THE REGISTERED CRITERION (quoted, not paraphrased)

> **Axis 2 — analytic character within the declared validity domain
> (ω ≪ ω_c):** `PURELY-RELAXATIONAL` (Re χ > 0 throughout, no
> resonance) · `RESONANT` (Re χ changes sign inside the domain) ·
> `INDETERMINATE`.

Operative domain: the registered probe span **[0.3, 0.9] × WC**, WC = 1
plant units. *Disclosed looseness:* "ω ≪ ω_c" is not a sharp interval;
the probe span is used as the operative domain and every verdict is
reported against it explicitly. Object: **χ = −K_R at kernel level** —
the register does not define Axis 2 on a dressed propagator, and no
switch was made.

## 2. CERTIFIED INPUTS CONSUMED (12ea453 / 04b8d6c)

    A  = -3/(1280 pi^2)          (frozen: log coefficient AND 1/eps residue)
    c0 = 0, c2 = 0               (EXACT, structural)
    c4 = A * (-6841/2835 - gamma_E + log 4pi)   ~ +1.0906e-4 at mu = 1

c4 was **read back from the D5 artifact's own `c4_over_A` field**, not
retyped from a report. The exact symbolic form is authoritative.

## 3. THE H⁰ REAL RESPONSE, AND TWO INDEPENDENT ROUTES

    Re chi^{H0}(omega) = (-A) omega^4 [ log(mu^2/omega^2) + kappa ],
    kappa = -6841/2835 - gamma_E + log 4pi,   -A > 0

- **Route A:** the frozen Tier-4 stored dispersive completion with the
  certified local slot substituted.
- **Route B:** the direct radial integral **re-executed** from the
  frozen Tier-3 cone data through the gated master formulas and
  MS-subtracted.

**Route A ≡ Route B exactly** — two genuinely different constructions
(stored completion vs. re-run direct integration), one real response.
Not a self-simplification.

## 4. ZERO SEARCH

Because −A > 0 and ω⁴ > 0, sign(Re χ) = sign of the bracket exactly.

**Exact unique positive zero: ω\* = μ·exp(κ/2), i.e. ω\*/μ =
0.79483456354** — a pure computed number, scheme-fixed given the
declared continuation. (The only other zero is ω = 0, order 4, the
domain edge — not an interior sign change.)

Verification: root bracketed before solving; **two independent methods**
(bisection, secant) agree with each other and with the exact root to
< 1e-20; direct-substitution residual 4.35e-30; stable under
dps 25/40/60 to < 1e-20; **sign-change count exactly 1 at sampling
densities 201/401/801** — not a sampling artifact, and no second
crossing missed. Numerical root-finding used a **disclosed reference
slice μ = 1×WC** solely to exercise the machinery; **no verdict was
taken at a single μ.**

## 5. THE μ-MAP — the verdict-bearing object

ω\* lies inside the registered span ⟺ **μ ∈ (0.377437, 1.132311) × WC**:

| regime | Axis-2 outcome |
|---|---|
| μ < 0.377437 WC | Re χ < 0 **throughout** the domain — **neither registered label applies** |
| 0.377437 < μ/WC < 1.132311 | Re χ **changes sign inside** the domain → **RESONANT** |
| μ > 1.132311 WC | Re χ > 0 **throughout** → **PURELY-RELAXATIONAL** |

Each regime was verified by direct endpoint evaluation at a μ inside it.

**FINDING (unnamed case):** for μ below the lower boundary the response
is negative across the whole domain — a case the registered trichotomy
does **not** name. Recorded, not resolved here.

**Scheme-dependence, stated explicitly as the record requires:** the
registered Axis-2 criterion **is** scheme-dependent through the local
real terms.

## 6. WHAT D5 DID RESOLVE

The five-constant H⁰ ambiguity has collapsed to **one scale**: c0 and c2
are exactly zero, c4 is calculated, and the zero's **location ratio
ω\*/μ is a fixed computed number**. Before D5, Axis 2 was open in a
5-parameter space; it is now open in exactly one, with the decision
boundaries computed to nine figures.

## 7. CONTROLS — all detecting

| control | result |
|---|---|
| A. local-term sign flip | zero moves 0.79483 μ → 1.25812 μ — the adjudication genuinely consumes D5 |
| B. remove local term (c4 = 0) | zero sits exactly at ω\* = μ, distinct from certified — the constant does real work |
| C. known 10% perturbation of c4 | zero moves to 0.77679 μ (2.27% shift), resolved where expected |
| D. reality | the adjudicated object is exactly real — no absorptive leakage into the Re-sign test |

## 8. EXCLUSION OF THE UNCERTIFIED PRE-REPAIR READINGS

`wall_kr_d5_exec_run2/3/4.log` were located, hashed, and confirmed
**RED on their own face** (failing gates). They are excluded; **no
number was read from them**, verified by a source-level check that the
instrument contains no numeric read of those files. The adjudication
stands independently of them.

## 9. DEFECT HISTORY (run 1 → run 2, gate-side)

Two reds, both mine, both gate-side: `float()` truncated the reference
root to ~1e-16 and could never satisfy a 1e-20 comparison; and I had the
**sign wrong** on two control mutations — since Re χ = (−A)ω⁴(L+κ) with
c4 = Aκ, removing the local term *adds* c4ω⁴ rather than subtracting it.
Both fixed; the physics was unaffected.

## 10. H² FIREWALL — HONORED

No H² local computed, fitted, inferred or backsolved. Noise fork not
opened. The α = −2 result was not consulted. Tier-4 validity boundary,
Ward Class-B finding, and the registered J(ω) conclusion untouched.

## HARD STOP

Axis 2 at H⁰ is adjudicated as far as the frozen record permits. The
single remaining input is a **μ-convention ruling** (μ in plant units) —
an owner action, and per the critical principle it may **not** be
justified by reference to any spectral or memory outcome.
