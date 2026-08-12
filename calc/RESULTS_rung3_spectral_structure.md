# rung3 — the spectral structure of the earned-under-determined disposition (in-house toy + verdict)

> ## ⚠️ LOAD-BEARING INPUT SUPERSEDED (marked 2026-08-12) — READ BEFORE USING THE O(G²) RESULT
>
> **This file's entire premise is the frozen-TT input, and that input was re-scoped on 2026-08-10.**
> The document below rests on "the TT graviton mode function is frozen at one loop," taken from
> Tan–Tsamis–Woodard arXiv:2103.08547. The register's scoping correction of 2026-08-10
> (`rung3_single_pole.boundary_condition`, source-verified) established that the paper's
> "no changes in the graviton mode function" sentence is **explicitly SCALAR-LOOP-SCOPED** — its
> citation is Park–Woodard 2011, the massless-minimally-coupled-scalar computation. For the
> **graviton loop**, the same paper's Table 8 entries are **nonzero and carry ln(H²Δx²)**.
>
> **Consequence for the O(G²) conclusion:** the "frozen at O(G) ⇒ leading TT dissipation is O(G²)"
> chain holds **for scalar-loop sources**. For graviton-loop sources — which is GRUT's own case,
> the pure-graviton self-energy — the premise is contradicted at the gauge-fixed level, so the
> O(G²) localization **does not carry over unexamined**. Whether the graviton-loop TT dissipation
> is still O(G²) for some other reason is **open and uncomputed**; nothing here establishes it.
>
> **What survives unchanged:** the secular-envelope → low-ω-singularity dictionary itself (verified,
> self-test at rel.err ~1e-13); the fence that "frozen at O(G)" means **silent**, not Class A and
> not Class B, with **both horns live**; and the file's own catch that the spin-0 "Class-B-like"
> label re-performed the retracted secular-log⇒cut shortcut.
>
> **Recorded as the pattern, not an excuse:** the 2026-08-10 correction reached the register node,
> then the standing documents, then the source registry entry — and **not this calculation's
> write-up**, which is where the superseded premise does the most work. Fourth relocation site.
> The O(G²) result must not be used in any public document at its stated strength until the
> graviton-loop case is worked or the claim is restated as scalar-loop-scoped.
>
> **RULED 2026-08-12 (overseer): do NOT work the graviton-loop case to rescue this.** That is
> blocker-(A)-scale new physics, not a section. The public document's Part IV.2 is written as
> what actually happened: *the fork was located at O(G²); the localization rested on a premise
> the program then corrected against itself; where the graviton-loop fork sits is open and
> uncomputed.* Losing the document's strongest physics section to the program's own correction
> IS the document's thesis, demonstrated on the freshest possible material.


*Turns the QUALITATIVE spine-test result ("earned under-determined") into its QUANTITATIVE form. The spine test banked that the de Sitter secular growth is channel-dependent (spin-0 potentials Ψ,Φ grow ∼ ln a; the TT graviton mode function is frozen at one loop). This feeds that channel-resolved input through the exact secular-envelope → low-ω-singularity dictionary and reads off ρ(ω)=2 Im G_R(ω) channel by channel. Code: `calc/rung3_spectral_structure.py`. Register: `rung3_single_pole` (derived-pending, ledger 0 — UNCHANGED). Scope, held throughout: **TOY/SCALING** (envelopes, not the tensor/gauge-invariant self-energy), inputs at **leading-order/simplest-gauge**, **O(G) un-resummed**. Default-BROKEN: the win is the honest quantitative form, not a resolved class.*

---

## The claim (default-BROKEN)

The branch-cut (Class-B) signal lives in the **spin-0** channel (a specific non-integrable low-ω singularity) — **not** the TT channel that G_R^TT probes; the TT channel is **frozen at O(G)**, carries no such singularity, and its leading dissipation is **O(G²) ∼ G²H⁵** — too weak for the current (un-resummed, O(G), simplest-gauge) computation to settle. If so, "earned under-determined" becomes **derived**: the channel carrying the cut-signal is the wrong one, and the right channel's dissipation is a higher-order effect below current resolution.

## Part A — the spectral dictionary (general, exact, computable)

For a causal retarded response G_R(t≥0) with late-time envelope ∼ t^p, the regulated transform is G̃_R(ω)=∫₀^∞ dt t^p e^{(iω−ε)t} = Γ(p+1)/(ε−iω)^{p+1}, and ρ(ω)=2 Im G̃_R(ω). The eps→0 dictionary:

| envelope | low-ω ρ(ω) | kind | integrability at ω→0 |
|---|---|---|---|
| p=0 (bounded) | ρ ∼ **2/ω** | power (PV 1/ω) | marginal (log-divergent) |
| p=½ (generic frac.) | ρ ∼ 2Γ(1.5)·ω^(−1.5) = 1.253·ω^(−1.5) | power ω^(−(p+1)) | **non-integrable** |
| **p=1 (linear = ln a)** | ρ ∼ **δ′(ω)** ("1/ω²") | **delta-derivative** | **non-integrable / pinned at ω=0** |
| p=2 (quadratic) | ρ ∼ −4·ω^(−3) | power | non-integrable |
| ln t | ρ ∼ −2(γ+ln ω)/ω ∼ \|ln ω\|/ω | log-power | non-integrable |

General law: ρ(ω→0) = 2Γ(p+1)sin((p+1)π/2)·ω^(−(p+1)). The distributional δ^(n)(ω) (weight pinned at ω=0) arises only for **odd integer** p (sin=0); even integers and non-integers give ordinary (though possibly non-integrable) power laws. **Rule of thumb: any secular growth (p≥1) ⇒ a non-integrable low-ω structure = a free-streaming / non-decaying-mode signal.**

**Passivity caveat (the map is a *formal* scaling transform, not a passive-response guarantee).** A causal *passive* response obeys ω·ρ(ω)≥0 (KMS / 2nd law). This holds for p≤1 (p=0: ω·ρ=2>0; p=1: δ′-weight at 0). For p≥2 the transform is **sign-indefinite** (p=2: ρ∼−4/ω³ ⇒ ω·ρ<0) — a *growing/unstable* mode, not a passive dissipative response. So only p≤1 entries carry a direct passive-response reading. The physics application uses only p=1 (spin-0) and the frozen TT channel — both fine.

*Numeric confirmation (in the code): Simpson quadrature reproduces the closed form to rel.err ∼1e-13; the p=0 → 2/ω limit, the p=½ log-log slope −1.5013, the p=1 δ′(ω) signature (∫ρ_ε·g → +2π g′(0), monotone from below), and the ln t form all verified by the self-test (PASS).*

## Part B — apply it channel by channel (inputs = banked spine-test finding, LO/simplest-gauge)

**The derived content is the TT channel.**
- **TT / spin-2 (GRUT's transport object ρ_TT = 2 Im G_R^TT):** mode function **frozen at O(G)** ⇒ no secular envelope ⇒ **no low-ω growth-singularity at O(G)** ⇒ leading O(G) TT dissipation **vanishes** ⇒ η_TT = **O(G²) or higher**.
  - **FENCE (the single easiest over-claim):** "frozen at O(G)" = **silent at O(G)** (no distinguishing singularity), **NOT** "analytic / Class A" **AND NOT** "Class B." A frozen mode is equally consistent with a razor-thin O(G²) pole **or** a trivial no-response — **both horns stay live.**
- **Spin-0 (Ψ,Φ) — a *wrong-channel check*, not a cut-establishment:** grow ∼ ln a = Ht (TTW-type, arXiv:2405.00116). **Scaling assumption (toy, load-bearing):** *take* the field/correlator secular envelope ∼ ln a as the retarded-response envelope; ln a is linear in cosmic time (a=e^{Ht}) ⇒ p=1. If one takes that bare envelope **at face value** and runs the dictionary ⇒ ρ ∼ δ′(ω) (non-integrable, weight pinned at 0; the "1/ω²" gloss is loose). One might call it "Class-B-like" — **but this face-value continuation is *exactly* the secular-log⇒cut shortcut the register's 3rd/symmetric correction retracted**: the real ω→0 continuation of the *assembled* object has not been done, so **the secular log establishes NO cut**. And it is the **wrong channel** (not what G_R^TT probes). So the naive signal, even at face value, sits in the wrong channel and says **nothing** about ρ_TT.

## Part C — order-counting coherence (not a precise η)

frozen-TT at O(G) ⇒ leading η_TT is **O(G²) or higher**; the banked null-collision estimate is Γ ∼ G²H⁵, also **O(G²)** (dimensional/order-of-magnitude, **not a computed rate**). Both say the TT dissipation is a G² effect, extraordinarily weak. So the pole-vs-cut distinction — a **razor-thin Lorentzian** of width ∼Γ∼G²H⁵ **vs** a **free-streaming branch cut** — lives at **O(G²)**, below the resolution of the current O(G), un-resummed, simplest-gauge computation. Consistency at leading nonzero order (both ∼G²) is the coherence check; it does **not** compute η and does **not** pick a horn.

## Verdict (default-BROKEN, honest; TOY/SCALING; does NOT graduate rung3)

**DERIVED — the quantitative form of earned-under-determined (carried by the TT channel):**
1. The TT channel (GRUT's transport object) is **frozen at O(G)**: no low-ω growth-singularity; leading dissipation **O(G²) or higher ∼ G²H⁵**, consistent at leading nonzero order with the null-collision estimate.
2. So the pole-vs-cut fork sits at **O(G²), a razor's edge** below the current O(G) resolution — "under-determined" is now **derived** (quantitatively located), not asserted.
3. **Wrong-channel check:** the spin-0 ln-a growth, taken at face value (the shortcut the 3rd correction *retracted* ⇒ establishes **no** cut), would map to a non-integrable δ′(ω) — but that is the **wrong channel** (not what G_R^TT probes) and says nothing about ρ_TT.

**Fences (both directions):**
- **TOY/SCALING** — envelopes only; not the tensor/gauge-invariant self-energy. On every claim.
- **Channel inputs** (spin-0 secular, TT frozen) = banked spine-test finding, LO/simplest-gauge; if the true growth differs (e.g. mixed ln(aHr) terms) the channel assignment shifts — **report the ambiguity, do not paper it**.
- **Frozen-TT does NOT collapse to Class A OR Class B.** Silent at O(G); both horns live. (This is the single easiest over-claim here.)
- **rung3 STAYS derived-pending, ledger 0.** This derives the FORM, not the class.

## Independent firewall (2026-07-04) — both directions, amber→green after fixes

A three-lens firewall (over-claim / physics-math / consistency) ran *before* banking. Outcome: **no blockers; physics fully re-derived and correct; the toy does NOT resolve the transport class** (frozen-TT stays silent, both horns live, ledger 0, does-not-graduate). Two required fixes, both applied:
- **Consistency (the sharp catch).** The original spin-0 "Class-B-like signal" label re-performed, in the wrong channel, exactly the secular-log⇒cut analytic continuation the register's 3rd/symmetric correction *retracted*. Reframed: the TT-channel O(G²) razor's edge is the derived content; the spin-0 result is now an explicitly **face-value** wrong-channel check that flags it re-runs the retracted shortcut and establishes no cut.
- **Symmetric fence.** The TT fence now reads "NOT Class A **AND NOT Class B**" (both horns), not just "NOT Class A."

Optional hedges also applied: "or higher" on η_TT=O(G²); "not a computed rate" on Γ~G²H⁵; the p≥2 passivity caveat (ω·ρ<0 ⇒ unstable mode, not passive ⇒ only p≤1 has a passive-response reading); δ′(ω) is the odd-integer sub-family; δ′(ω) primary with "1/ω²" as a loose gloss; the field-envelope→response-envelope step marked as the load-bearing scaling assumption.

Independently confirmed by the physics lens: the dictionary and all four entries (p=0→2/ω; p=1→δ′(ω); p=2→−4/ω³; ln t→−2(γ+ln ω)/ω), the p=1 δ′ signature (∫ρ_ε·g→+2π g′(0)), and the frozen-TT→O(G²) power counting are all correct; the self-test passes at rel.err ∼1e-13.
