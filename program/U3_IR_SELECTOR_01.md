# U3_IR_SELECTOR_01 — RESULT: can the theory select its own IR completion?

**OUTCOME: PARTIAL-SELECTOR — with the checker's corrected survivor set, and a weaker
sense of "survive" than the deriver filed. The owner's threshold is NOT crossed.**

**Threshold statement, plainly:** the microscopic construction does not select its IR
completion (S6 silent, confirmed with special care). The consistency conditions do
not select one either — they **exclude every corpus-represented sharp completion**,
including the deriver's own survivor, and leave three things standing that are not
standing in the same sense: an *untested* smooth window, a *non-computable* resummation,
and a *different object*. The completion remains an external declaration.

Executed 2026-09-15/16 under `U3_IR_SELECTOR_01_PROTOCOL.md` (frozen `a676734`).
Surveyor → deriver (7 selectors × 10 candidates, computations exhibited) → adversarial
checker (CONFIRMED_WITH_CORRECTIONS: 16/18 exclusions re-derived and agreed; **two
refuted — both on the deriver's survivor**; checker scratch hashed in the .json). No
resolver needed: the checker's refutations were of sub-steps, the outcome label held.
Zero register edits; fork stays gated; rung3's tier untouched.

## 1. S6 — the dynamics are silent (the clean negative result)

The Tier-1/Tier-2/CTP construction determines the superhorizon **occupation** completely
and uniquely — β_k = 0 at every k by the far-past BD condition, n_k = (aH/k)⁴/4 relative
to the instantaneous vacuum (derived; re-derived by hand by the checker) — and determines
the fork-driving vertex content (V₀ = 8ω⁴/15 from the frozen C-matrix's bare H⁰ entries,
reproduced by an independent sphere quadrature; the recorded noise pole 4ω⁴/15 and the
retarded Δ-part −4iΔω⁴/15 both reproduced exactly). What it contains **nothing** of: any
system/bath partition, any initial time, any zero-mode prescription, any zero-mode
dynamics — token scan of the frozen instruments: zero occurrences; the radial measure has
no lower limit; the corpus declares no partition anywhere (ROOT-1 §8, Q2 arrow 6,
NOISE-A, EFT baseline, all verified). Candidate 1 is therefore a change of an
*undeclared* input, not a contradiction of a declared one. The one thing that could make
S6 speak — a closed self-interacting graviton zero-mode equation — is NOT_PRESENT on the
corpus's own audit; the scalar Starobinsky–Yokoyama instance is not the graviton.

## 2. The consistency selectors — what they excluded, by exhibited computation

Built explicitly: the completed k_ext = 0 kernel on exact dS in U2's two-time form, per
candidate; every exclusion below is a computation on that object.

- **S1 (dilatation covariance / D3c stationarity):** excludes every comoving/initial-time
  completion — the fixed q_IR of `tt_worldline` and ROOT-1 §8, the box/q_min regulators,
  epoch windows, and **rung9's conformalon e-fold counting** (initial-time class). Not
  circular (checker): S1 was not "covariance imposed, covariant found" — it was exhibited
  as a stationarity computation, excludes only the comoving class, and is classified as
  a *symmetry-consistency demand*, not a derivation from the dynamics. Its status is
  conditional, exactly as U2 carried it: a comoving completion is physically meaningful
  (the standard way the massless dS two-point function is made well defined, at the
  price of a preferred epoch).
- **S3 (KMS at T_dS = H/2π, cosmic time):** cuts *inside* the covariant class. Every
  physical-scale dressing fails except one: **U2's own conformal-midpoint a(u_b)/tanh
  form is EXCLUDED** — iβ-periodic but violating the KMS boundary relation at O(1), with
  an essential singularity inside the strip; the arithmetic-mean and max-projection forms
  fail likewise; derived general statement: an even, iβ-periodic dressing must be
  nonvanishing and finite on the closed strip, which excludes every polynomial in
  cosh(Hτ). α-vacua excluded (non-thermal for the static observer). **Correction to
  U2's record**: a(t̄) = √(aa′) gives ln(2ε sinh(Hτ/2)) — KMS with strip analyticity;
  a(u_b) gives ln(2ε tanh(Hτ/2)) — iβ-periodic but not KMS. U2's comoving half is
  unchanged. *Preserved as history, not rewritten.*
- **S5 (positivity/passivity) — THE CHECKER'S LOAD-BEARING REFUTATION.** The deriver
  filed the cosmic-midpoint sharp cutoff q > εH√(aa′) as surviving for ε ≥ ε* ≈ 1.3–1.5,
  having scanned ω ∈ [0, 8H]. **The checker went past the grid**: at ε = 1.5 the completed
  kernel's spectral weight is negative at ω = 9.25H (G_> = −0.117; three independent
  routes — x-route at dps 30 and 45, and a Bessel-K representation — agree to six
  digits) and again at 18H (−0.056), with excursion amplitude growing like
  2√(πω/H)/ε³ — the endpoint term of the q-integral. First negative excursion sits at
  ω ~ (π/4)ε⁶H, so no ε rescues it. **The sharp covariant form fails positivity at
  every ε.** The trap the owner named — "the covariant prescription is obviously
  right" — is not merely avoided but *inverted*: the covariant sharp form is the one
  that fails.
- **S7 (cross-consistency) — second refutation, same survivor:** the deriver's
  "flat anchor reproduced as H → 0" held only for the H⁰ term of the graded integrand.
  On the exact completed object the edge term is non-analytic in H (stationary point at
  τ ~ (2/H)ln(ω/εH)), its ringing amplitude is H-independent at fixed ω/H, and the
  spectral function has **no H → 0 limit at fixed ω** — it does not approach the banked
  flat anchor. **Every sharp cutoff, physical or comoving, fails exact S7.** The
  H-independent comoving scale additionally fails S7 by gapping the banked gapless
  branch point (ROOT-1 §8's countermodel, re-derived symbolically).
- **S2, S4:** no additional exclusions (S2's null stands with a corrected reason — the
  endpoint term grows like e^{Hτ/2} on the real axis, but UHP analyticity of Σ_R holds).
- **KMS on the α = −2 noise power** (the place flagged as likeliest for a missed
  exclusion): checked — the completed G-form kernel *includes* the q⁻² and q⁻⁴ power
  terms and satisfies the KMS boundary relation exactly (direct quadrature 1.7e−25). KMS
  alone does not exclude the sharp covariant completion; positivity and exact S7 do.

## 3. What is left standing — three things, not four viable theories, and not alike

| Survivor | Sense of "survives" |
|---|---|
| **Candidate 1, smooth-window form only** — w(q/(εH√(aa′))), C^∞-flat IR edge | KMS-analytic by the deriver's argument (stands); **positivity and exact S7 UNTESTED** — defined, executable computations on the same kernels, not yet run. A Wigner-midpoint *regulator* of the loop kernel, **not a bath partition**: the fork's literal "bath support restricted to k > εH" is the product-of-projections form, which S3 excludes. Candidate 1 in its stated operator sense has no KMS-consistent physical-scale realization. |
| **Candidate 2** — secular-sector resummation | Not computable in-corpus for the graviton (Q2 bridge blocked on seven arrows; O2 unresolved). Survives by non-computability, not by passing. |
| **Candidate 6 / 3** — the static-patch l ≥ 2 multipole host / white-floor reading | A **different object**: IR-finite at free level (ρ_l ~ ω_T² for l ≥ 1, derived; only the scalar's l = 0 zero mode diverges), Killing-covariant, natively KMS. Its reduction to the fired flat-slicing k_ext = 0 loop is the unperformed wall-A step. Object-slippage fence: calling it a "surviving completion" of the fired loop would be exactly the mistake the (O, D, L, R) discipline exists to prevent. |

**Observable consequences: none survive.** The deriver's conditional class/amplitude
predictions (η Ohmic with a finite white floor; χ_static's IR segment; k = 0
thermality) rested on a covariant, KMS-analytic, positive completion that no
corpus-represented form now exhibits — and independently, the "Ohmic" class claim was
built on the vertex-stripped proxy, referent-less for the actual object. What survives
is the *structural spread*: c₂′ shifts by −(8/15)ω²H²·ln ε (61.9× the H² absorptive
coefficient per e-fold of ε) and the O(H/ε) demotion of the noise side — the price of
the fork stated as a spread, not a prediction.

## 4. The finding, in the owner's distinction

**Constraint transmission, not generation.** The dynamics did not select the IR
prescription. The admissibility constraints did not select one either — they *emptied*
the corpus's sharp-completion space by the construction's own consistency structure
(dilatation covariance + per-mode positivity + BD thermality), while the two things that
would count as a selection (a smooth window passing S5/S7; a static→flat reduction
theorem) are each one defined, unexecuted computation away. "Only this survives our
constraints" was never reached, so it could not be upgraded to "nature chooses this."
The fork is preserved as an independent physical input, its price now stated as a
spread. Two failures of the deriver, both in the framework-favorable direction
(survivor claimed on a truncated grid; anchor recovery claimed for the graded term only),
both caught by the checker with independent numerics — on the ledger.

## 5. Not decided / next defined computations (no target issued; owner's call)

The smooth-window S5/S7 test (executable now on the same kernels); the wall-A static→flat
reduction (U1's B1, still the precondition of everything); whether rung9's e-fold
bookkeeping, now S1-excluded as a class, needs its own review (cross-sector consequence,
flagged only); the two U2 record corrections (the a(u_b) vs √(aa′) forms) to be carried
into any future U2 citation. The fork stays gated; nothing banked; Born 2A/2B unchanged.

---

*Filed 2026-09-16. Deriver, checker, and surveyor filings in full in
`U3_IR_SELECTOR_01.json`; checker scratch hashes recorded there (c1 1defb9da …
c3 6af91a89); repo verified clean at `a676734` by the checker.*
