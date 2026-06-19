# Spectrum of the Responsive Vacuum — the post-v3 dark-sector program

**Opened:** June 2026 · branch `main_v3` · successor program to the v3 dark-sector closure.

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
