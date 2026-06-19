# Spectrum of the Responsive Vacuum — a continuing v3 dark-sector program

**Opened:** June 2026 · branch `main_v3` · the next phase of v3's self-reframing, following the
dark-sector closure. (v3 is a living framework: it keeps re-deriving and re-defining as the work
proceeds, and forks to a new major version only when the parts can no longer be adapted — as v2 did.
This program is v3 continuing, not a successor version.)

The v3 dark-sector results (the C5a closure and the **Locality–No-Halo Theorem**, Test 07) did more than
rule mechanisms out — they *changed the question*. The progression:

1. *What operator generates halos?* → every local operator fails (Stage A–D).
2. *What singularity structure generates halos?* → a `k = 0` pole; locality forbids it (Test 07, spectral form).
3. **What pole structure does the vacuum response spectrum possess?** ← the program defined here.

Question 3 is the fundamental one. The dark-matter problem inside GRUT has been reduced to a single,
mathematically decidable question about the spectrum of the responsive vacuum.

---

## Phase I — the Pole Classification Theorem  ✅ COMPLETE

> **Pole Classification Theorem.** The current GRUT kernel `χ(ω) = 1/(1 − iωτ₀)` possesses **a single
> relaxational pole** (at `ω = −i/τ₀`: on the imaginary axis ⇒ massless, overdamped, purely dissipative;
> in the lower half-plane ⇒ causal and stable). **A derived dark sector requires additional *stable*
> poles in the vacuum response spectrum.** Whether such poles exist is **not** forbidden by GRUT's
> constraints (causality, CTP unitarity, finite memory, locality all permit a richer kernel); it is
> *determined by the effective action* — and constitutes the central question of the Spectrum Program.

**The general criterion (model-independent).** A derived dark sector requires **additional dynamical
degrees of freedom beyond the single relaxational mode** — additional poles. Equivalently: a stable,
gapped, long-lived pole *off* the imaginary axis (`Re ω ≠ 0` ⇒ a mass; `Im ω < 0`, `|Im ω| ≪ |Re ω|` ⇒
stable and long-lived) is a particle-like, dark-matter-capable mode. The single relaxational pole is none
of these.

**Inertia is the most obvious realization, not the only one.** Raising the constitutive law's *dynamical
order* is what adds poles:

```
first-order   τ₀ ż + z = z_target              → one pole  (relaxational, massless)        [current GRUT]
second-order  τ₁² z̈ + τ₀ ż + z = z_target       → two poles; off-axis (massive) iff 4τ₁² > τ₀²
```

A `z̈` (inertia) term is the simplest way to get a second pole, but the theorem is stated in terms of
*poles*, not *inertia*, so it remains intact for any other route to additional dynamical order (a coupled
auxiliary field, a non-Markovian memory function with internal structure, an additional sector, …).

**Verification** (`grut/derivation/phi_munu/pole_spectrum.py`, `verify()`): the first-order kernel has
exactly one pole, on the `−i` axis (massless, stable); a second-order kernel reproduces it as `τ₁ → 0`,
and develops an off-axis (massive) stable pole pair once `4τ₁² > τ₀²`. The classifier is general (it takes
the denominator polynomial of any candidate kernel and returns the pole inventory + classification), so it
is the reusable tool for Phase II.

---

## The central question

> **Is the responsive vacuum fundamentally single-mode or multi-mode?**

Everything in the GRUT dark-matter problem is now downstream of this. Two decisive outcomes:

- **Single-mode** (one relaxational pole, no additional stable poles). Then the single-pole result is a
  *theorem*, not a model assumption: the vacuum is fundamentally overdamped, and **dark matter exits GRUT
  permanently** as a hosted matter component external to the responsive-vacuum sector. A legitimate, sharp
  scientific endpoint.
- **Multi-mode** (an additional stable, gapped pole). Then GRUT has a **derived dark sector** for the
  first time — a candidate identified as a mode of the theory, to be tested for darkness, abundance, and
  cosmological survival (later phases).

---

## Phase II — the effective action: the deciding computation  ✅ COMPLETE

The pole structure is not something to *assume*; it *follows* from the action. So Phase II does not ask
"can we write a second-order equation?" — it asks:

> **What is the most general quadratic CTP effective action compatible with Q (CTP/in-in unitarity), F
> (finite memory), and D (the adiabatic-dilatation bridge)?**

Once that action is written, the kernel and its poles follow automatically. The `z̈` term then resolves
into three distinct questions, in increasing strength:

1. **Allowed?** — is a second-order (inertial / multi-pole) term permitted by Q, F, D?
2. **Generated?** — does the CTP / Mori–Zwanzig reduction actually produce one?
3. **Required?** — is it forced, or can it be set to zero consistently?

The first-order law was "derived from three routes"; the gradient-flow route is inherently overdamped
(first-order), while the Mori–Zwanzig memory function *can* carry internal structure (additional poles).
Phase II is where that ambiguity is resolved.

**Verdict (computed).** The pole structure of the quadratic CTP action is fixed by two facts: (i)
**#poles = #independent responsive variables** (the zeros of `det K^R`); and (ii) a **dark-capable pole
— stable, gapped, off the imaginary axis — requires an *inertial*, matter-like degree of freedom** (a
`z̈` + restoring term). A scan of 12,800 poles over arbitrarily coupled *relaxational* variables (the kind
F supplies) found **no stable off-axis pole**: coupling relaxors only redistributes poles along the `−i`
axis (overdamped, massless). GRUT's responsive vacuum is relaxational *by construction* (F = finite
memory, gradient-flow, single τ₀) and carries exactly **one** responsive variable (the TT memory; the
scalar channel is killed by the No-Go, the vector is non-dynamical) atop the single massless graviton.

> **So the responsive vacuum is single-mode, and a dark sector requires an added inertial matter field —
> by construction a hosted input.** On the three questions: a dark (inertial / second-order) term is
> *allowed* only as an **extension** of F, is *not generated* by the single-variable relaxational
> reduction, and is *not required* (the first-order kernel is self-consistent). **The central question is
> answered: the responsive vacuum is single-mode; dark matter is a hosted matter field, permanently,
> within GRUT's foundations.**

This is conditional on F (relaxational finite memory) as the vacuum's actual dynamics. The *only* way to a
GRUT-derived dark sector is to **extend the foundations** with an inertial, matter-like degree of freedom
— a genuinely new postulate (a microscopic medium with massive excitations), not anything the current
action generates. Verified: `grut/derivation/phi_munu/pole_spectrum.py` (`verify()`).

---

## Honest prior

The v3 audit trail has consistently *removed* degrees of freedom — dark-energy claims weakened, the
dark-matter response sector collapsed, the MOND interpolation left external, locality strengthened, halo
mechanisms eliminated. The framework has become steadily more minimal. By pattern recognition (not
pessimism), the lean is toward the **single-mode** outcome — one TT mode, one relaxation pole, no derived
dark sector. But the point of Phase I is precisely that this is now decidable by computation rather than
argued by intuition — and **Phase II has now settled it: single-mode** (a dark sector would require
extending F's foundations with an inertial matter degree of freedom). The lean became a result.

---

## Deriving F — how much of the finite-memory postulate follows from Q

F (the single-pole memory `χ(ω) = 1/(1 − iωτ₀)`) has been carried as a *postulate*. The spectral machinery
lets us ask how much of it is actually forced. The answer is layered:

- **The FORM is derived from Q.** CTP unitarity, through the fluctuation–dissipation relation (noise
  kernel positive, `N ≥ 0`), forces the response to be **causal** (analytic in the upper half ω-plane —
  the pole sits at `ω = −i/τ₀`, lower half) and **passive** (`Im χ(ω) ≥ 0` for `ω > 0`; here
  `ωτ₀/(1+(ωτ₀)²)`, with Re,Im a Kramers–Kronig pair). A causal, passive response is a **Herglotz
  function**, and the Herglotz representation theorem forces it to be a **positive superposition of
  single-pole Debye modes**, `χ(ω) = ∫ dμ(τ)/(1 − iωτ)`, `dμ ≥ 0`. Finite memory puts the support at
  finite τ. So the single-exponential **shape is not a free ansatz — it is the only shape Q allows.**
- **The SINGLE pole is the irreducible content.** One relaxation channel (`dμ = δ(τ − τ₀)`) is the
  minimal Herglotz measure — and by Phase II it is *identically* the statement that the vacuum has one
  responsive variable, the **single-mode** spectrum. So F's single-pole content and the
  no-derived-dark-matter verdict are **the same postulate**: deriving one derives the other.
- **The VALUE τ₀ is anchored — and its irreducibility is itself established.** The `τ₀ ↔ τ_micro` bridge
  was investigated to closure (Option B, June 2026; `grut/foundation/tau_hierarchy_decision.py`): the
  gravitational τ₀ (41.9 Myr) and the thermal τ_micro (≈ 1.4×10⁻¹⁹ s) differ by 34 orders with **no
  derivation between them** — no combination of {ℏ, k_B, c, G} has units of time², and the numerology
  cross-check fails (ratio ≈ 0.984 ≠ 1; implied T\* ≈ 40 nK, unphysical). So τ₀ is **GRUT's one
  irreducible fundamental scale**, not a pending derivation.

**Consequence for GRUT's foundations.** F is no longer a free functional postulate. It reduces to **Q
(proven) ⇒ the Herglotz form**, plus **one channel-counting postulate** (= single-mode — the very input
that makes dark matter hosted), plus **the anchored scale τ₀**. So GRUT's dynamical inputs are fewer and
sharper than "Q + F + α + τ₀ as four independent things": the *form* of F is a theorem of Q, and its
remaining content is one binary structural choice (single- vs multi-channel) plus one number. Another step
of v3 reframing in place — a postulate partly dissolved into a consequence. Verified:
`grut/derivation/phi_munu/pole_spectrum.py`.

**The floor.** With the form derived from Q and τ₀'s irreducibility established (Option B), GRUT's
irreducible inputs are now fully mapped: **Q** (proven), the **single-channel / single-mode** structural
postulate (one input, identical to the dark-matter verdict), the dimensionless axiom **α = 1/3**, and the
single anchored scale **τ₀**. The "zero free parameters" claim is honestly scoped to that gravitational
predictive core (τ₀, α). This is bedrock for the current foundations: going below it — deriving τ₀, or
deriving the single-channel choice — requires a deeper microscopic theory of the responsive medium, i.e.
a *foundational extension* of v3, not a further derivation within it.
