# Primordial A_s — Physical Investigation of the α/S³ Coincidence

**Status:** Stage 1 complete. Stages 2–4 pending.
**Started:** 2026-04-28.
**Trigger:** Stage-1 primordial-amplitude attempt
(`grut/derived/cosmology/primordial_amplitude.py`, registry claim
`primordial_amplitude_zero_parameter_open_negative`) found that
α/S³ ≈ 8.53 × 10⁻⁹ lands at factor 4 from observed
A_s = 2.1 × 10⁻⁹. With 11 dimensional candidates tested, this is
statistically plausible coincidence. The investigation asks: is
there a physical motivation for this combination, or is it
genuinely chance?

**Methodological constraint (load-bearing):** Do not start from the
known answer α/S³ and search for a derivation that produces it.
That is reverse-engineering and a discipline failure. Start from
"what does primordial-amplitude physics naturally produce in
GRUT's framework?" and let the answer fall where it falls. The
α/S³ comparison is post-hoc; the framework's natural scaling is
the actual investigation target.

---

## Stage 1 — Algebraic decomposition

### Numerical verification

```
α   = 1/3
S   = 12π/α² = 12π × 9 = 108π
S³  = (108π)³ = 1,259,712 × π³
α/S³ = (1/3) / (1,259,712 × π³)
     = 1 / (3,779,136 × π³)
     ≈ 8.534 × 10⁻⁹
```

Observed (Planck 2018): A_s = 2.1 × 10⁻⁹. Ratio: α/S³ / A_s ≈ 4.06.

### Equivalence class — expanded

The single number α/S³ ≈ 8.534 × 10⁻⁹ has many equivalent algebraic
expressions, each pointing at a different physical mechanism.
Verified numerically; all forms below evaluate to the same value
to floating-point precision.

| Form | Expression | Type |
|:---|:---|:---|
| **F1** | α/S³ | (α, S) basis, integer powers |
| **F2** | α⁷/(12π)³ | (α, 12π) basis, integer powers |
| **F3** | α⁷/(27·(4π)³) | (α, 4π) basis, separating 12π = 4π·3 |
| **F4** | (α^(7/2)/(12π)^(3/2))² | Squared form (variance picture) |
| **F5** | (α^(7/3)/(12π))³ | Cubed form (3D phase-space picture) |
| **F6** | α·(α²/12π)³ | F1 with S expanded |
| **F7** | α¹⁰/(4π)³ | Numerical identity at α = 1/3 specifically |
| **F8** | 1/(3¹⁰·(4π)³) | Pure numerical |
| **F9** | α/(4π/α³)³ | Using S = 4π/α³ identity at α = 1/3 |
| **F10** | (α⁵/(12π)²)·(α²/12π) | F1 split into "5-vertex × 2-vertex" decomposition |

Important distinction: **F1–F6 are algebraic identities** (true for
arbitrary α via S = 12π/α²). **F7–F9 are numerical identities at
the framework's specific α = 1/3** — they exploit 1/α³ = 27 (a
property of the rational α = 1/3 that doesn't hold for arbitrary α).

The α = 1/3 identity 1/α³ = 27 means S = 12π/α² = 4π · 3/α² = 4π/α³.
At this value, the screening factor has a single-power form
S = 4π/α³ as well as the canonical S = 12π/α². This is a *property
of the GRUT framework's specific α value*, not a general identity.

### Physical lenses — what each form suggests

Each algebraic form points at a different physical mechanism. The
investigation in Stage 2 must search the framework for derivations
that *naturally* produce one of these structures, not retrofit one
to match.

### Physical lenses

Each algebraic form points at a different physical mechanism. The
investigation in Stage 2 must search the framework for derivations
that *naturally* produce one of these structures, not retrofit
one to match.

#### Lens A — α⁷ from a 7-vertex graph (form F1)

**Mathematical structure:** α appears to the 7th power.

**Physical interpretation:** Seven independent insertions of
vacuum-impedance physics, each contributing α at a distinct vertex.
The (12π)³ in the denominator is three angular/solid-angle
integrations.

**Plausibility:** Low. A high-order graph (7 vertices) is not
typically dominant in any framework. Most derivations of cosmological
amplitudes give α at low integer power (1, 2, occasionally 3). To
get α⁷ would require either:
- A 7-loop calculation in CTP (implausible — even 3-loop is heavy);
- A coincidental combinatorial coefficient like (Wick contractions)
  × α^k giving net α^7;
- Iteration: α^7 emerging from (constitutive equation iterated 7×).

**Verdict for Stage 2:** Worth checking if the constitutive equation
applied iteratively to the noise kernel produces α^k for some
specific k, but α⁷ would be a surprising endpoint.

#### Lens B — One impedance × three screenings (form F4)

**Mathematical structure:** α × (1/S)³.

**Physical interpretation:** A single insertion of vacuum impedance
(one factor of α from a fluctuation source), divided by three factors
of screening (three propagation/regulation steps). The 3 in the
exponent corresponds to three independent suppressions.

**Plausibility:** Moderate. Three suppressions could be:
- 3D momentum-space integration (each direction contributes a 1/S);
- Three CTP propagator insertions (forward → backward → forward);
- A volume integral (3 spatial dimensions in a cosmological
  perturbation calculation).

**Specific candidate:** Standard inflationary A_s involves
(H/M_Pl)² × (1/ε), where the (H/M_Pl)² comes from de Sitter mode
function squaring at horizon crossing. In GRUT, replacing M_Pl
with the screening-mediated cosmic baseline τ_Λ might produce a
factor of 1/S² (from (H_inf × τ₀ × S)⁻²) times 1/S from
normalization.

**Verdict for Stage 2:** This is the most physically natural form
to investigate. The 1/S³ structure could arise from cosmological
perturbation theory in the constitutive framework.

#### Lens C — Bandwidth-integral structure

**Mathematical structure:** α from the bandwidth integral, multiplied
by some momentum-space factor that produces 1/S³.

**Physical interpretation:** GRUT's bandwidth integral over the
linear-regime power spectrum gives Ω_dm = α exactly. If the same
bandwidth integral evaluated for primordial fluctuations (a
different observable, but the same machinery) produces α × (k_*/k_S)³
for some characteristic scales, where (k_*/k_S)³ ≈ 1/S³, this would
be a natural form.

**Plausibility:** Worth exploring. The bandwidth integral is the
framework's natural cosmological-scale machinery; using it for a
different observable (primordial amplitude rather than relic
density) is a well-defined extension.

**Verdict for Stage 2:** Investigate whether the bandwidth integral
applied at the primordial scale produces a 1/S³ factor naturally.

#### Lens D — Constitutive-fixed-point variance

**Mathematical structure:** Variance of the noise-driven fluctuation
of the constitutive field z around z = 0, computed using the
fixed-point linearization.

**Physical interpretation:** The Stage-1 OU-process attempt (Path A)
gave 10⁻¹⁹ — too small by 10¹⁰. But that calculation used a
specific Planck-rescaling (⟨h²⟩/ℏ) that may not be the right
dimensional reduction for primordial curvature ζ.

If the right rescaling involves S (the screening factor mapping
local τ₀ to cosmic τ_Λ), the variance could naturally pick up
factors of S that change the magnitude.

**Plausibility:** Moderate. The Stage-1 Path A calculation was
honest but used a specific normalization choice; an alternative
(S-based) normalization could be physically motivated.

**Verdict for Stage 2:** Re-examine Path A with rescaling by τ_Λ
or by S × ℏ rather than ℏ alone. Document what falls out.

#### Lens E — Volume-form (3D screening-cubed)

**Mathematical structure:** S³ as a "screening volume" — i.e., S
has natural geometric interpretation as a 3D screening length.

**Physical interpretation:** The screening factor S = 12π/α²
already has 12π as a solid-angle-times-3 combination (4π × 3).
S³ might be (4π/α²)³ × 27 — eight independent geometric volumes
from a triple integration. The 27 is 3³ — a 3D combinatorial
factor.

**Plausibility:** Moderate. The 12π = 4π × 3 decomposition is
well-established (Phase I §5). The ³-power from cubing it
naturally fits 3D physics.

**Verdict for Stage 2:** Check whether GRUT's screening derivation
extended to a 3D volume integration (rather than the radial
integration that produced 12π in the first place) gives the 1/S³
factor.

#### Lens F — Variance from a fractional-power mode function (form F4)

**Mathematical structure:** ⟨h²⟩ = ψ_k² where ψ_k = α^(7/2)/(12π)^(3/2).

**Physical interpretation:** Mode functions in standard QFT often
scale with half-integer powers (e.g., ψ_k ~ 1/√(2k³) for free
fields). The half-integer powers arise from quantization
normalization. If GRUT's primordial mode functions inherit this
half-integer structure with α and 12π factors, the variance ⟨h²⟩
naturally produces α⁷/(12π)³ through squaring.

**Plausibility:** Moderate. The half-integer-power structure
matches standard QFT conventions for mode functions. The α^(7/2)
prefactor is unusual, but could come from a 7-vertex tree-level
amplitude square-rooted (which gives α^(7/2)) — different physics
than 7-vertex one-loop (which gives α⁷ directly).

**Verdict for Stage 2:** Investigate whether GRUT's mode-function
normalization for cosmological perturbations naturally produces
α^(7/2)/(12π)^(3/2) (or some equivalent fractional-power form).

#### Lens G — Cubed phase-space integration (form F5)

**Mathematical structure:** [α^(7/3)/(12π)]³ — a single quantity
to the third power.

**Physical interpretation:** A 3D phase-space integration over
momentum modes ∫ d³k F(k) where F has α^(7/3)/(12π) per mode.
The exponent 3 is the spatial-dimension count.

**Plausibility:** Moderate. Three factors of (something) is the
natural form for integrating over three momentum directions, with
the "something" being a per-direction contribution.

**Verdict for Stage 2:** Check whether the bandwidth integral or a
related momentum-space integration in the framework decomposes as
(per-direction contribution)³.

#### Lens H — α=1/3 numerical accident (forms F7, F8, F9)

**Mathematical structure:** α¹⁰/(4π)³ — only equivalent to α/S³
at α = 1/3 specifically.

**Physical interpretation:** If the framework's specific α value
is ITSELF derived (which it is — from the conformal-mode scalar's
a/c = 1/3), then numerical identities at α = 1/3 might encode
deeper structure not visible at the algebraic level.

**Plausibility:** Speculative but worth flagging. The fact that
1/α³ = 27 at α = 1/3 connects "screening cubed" naturally to
"vacuum impedance to the third inverse power." If this connection
has physical content, the derivation might naturally produce α¹⁰
where one would expect 27 from a 3D volume integration.

**Verdict for Stage 2:** Note this as a meta-clue. If a Stage-2
candidate produces α^k where the natural expectation is 27 = 1/α³,
that's evidence the α = 1/3 numerical identity is at work.

---

## Stage 1 — Honest read

The α/S³ combination has multiple algebraic decompositions (10
documented above), and each points at a different physical
mechanism. The most physically natural lenses are:

- **Lens B** (one impedance × three screenings) — fits standard
  cosmological-perturbation structure.
- **Lens C** (bandwidth-integral evaluated at primordial scale).
- **Lens D** (OU-process variance with alternative S-based
  rescaling).
- **Lens F** (variance from fractional-power mode function) —
  matches standard QFT mode-function normalization conventions.

Less likely but algebraically valid:

- **Lens A** (α⁷ from a 7-vertex graph) — high-order, unusual.
- **Lens G** (cubed phase-space integration) — natural for 3D but
  needs a specific per-mode form.
- **Lens H** (α = 1/3 numerical identity) — exploits 1/α³ = 27 at
  the framework's specific α value; speculative.

**Critical caution:** Each lens is a *candidate* mechanism. None
has been derived. The risk in Stage 2 is grabbing the most
attractive lens and constructing a derivation that produces α/S³
because that's the target. The discipline must be: pick a lens,
follow it forward, and report what falls out — even if the result
is α/S^n for n ≠ 3, or α^k × (other factors) entirely.

---

## Meta-observation on search-space framing

The Stage-1 primordial-amplitude attempt tested 11 dimensional
candidates and found α/S³ as the closest match. Two refinements to
that statistical framing surfaced in this investigation:

### Duplicate-candidate identified

`kT_c/E_Pl` and `t_Pl/τ₀` were both included as Path-C candidates,
but they are **identically the same number by definition**:

```
k_B T_c = ℏ/τ_0           (definition of T_c)
1/E_Pl   = t_Pl/ℏ           (definition of E_Pl, t_Pl)
=> k_B T_c / E_Pl = ℏ/(τ_0 E_Pl) = t_Pl/τ_0
```

So the original "11 candidates" was actually **10 distinct
numbers**. (This duplicate is not a bug in the calculation — both
candidates correctly evaluate to 4.08 × 10⁻⁵⁹ — it's a
multiplicity issue in the candidate count.)

### Equivalence-class framing

More fundamentally: each distinct *number* admits multiple
*algebraic forms*. α/S³ has at least 10 equivalent expressions
(F1–F10 above). The original 11-candidate list mixed:

- Distinct numbers (e.g., α/S² ≠ α/S³)
- Algebraic forms of the same number (no overcounting beyond the
  one duplicate above, but in principle the same issue could arise)

For statistical assessment of "chance match," the relevant search
space is **distinct numbers**, not algebraic forms. With 10
distinct numbers tested over a wide log-range, expecting ~1
within-decade match is still plausible coincidence.

The refined Stage-2 search target follows from this: a derivation
that produces *any member of the α/S³ equivalence class* counts
as a candidate. A derivation producing α^5/(12π)² evaluated to
~10⁻⁹ would not normally be checked against α/S³ at the algebraic
level, but it IS a candidate if it equals α/S³ numerically. The
form in which the derivation naturally produces the result is
itself informative — it tells us which physical picture is
correct.

### Implications for Stage 2

The Stage-2 forward derivations should:

- Output their natural algebraic form, not be steered toward any
  specific decomposition (F1–F10 or otherwise).
- Compare numerically to α/S³ ≈ 8.534 × 10⁻⁹ AND to the observed
  A_s ≈ 2.1 × 10⁻⁹.
- Report the natural form. If the derivation produces α^a × S^b
  in some specific (a, b), that's the framework's natural primordial
  scaling. Whether it numerically matches α/S³ is a separate
  question.

---

## Stage 2 — Forward derivation: Lens B/F (COMPLETE, rescaling-conditional)

**Date:** 2026-04-28.
**Module:** `grut/derived/cosmology/primordial_curvature.py`
**Tests:** `tests/derived/test_primordial_curvature.py` (31 tests, all passing)

### Setup

Linearize the constitutive equation around the null fixed point z = 0:

    τ_0 d(δz)/dt + δz = ξ(t)

In Fourier space (k, ω): ⟨|δz_k(ω)|²⟩ = N_k(ω) / (1 + ω²τ_0²).

The CTP noise kernel has Diósi-Penrose spatial structure
(N_grav(x-x') = G/(ℏ|x-x'|), Fourier-transforming to 4πG/(ℏk²))
combined with KMS thermal temporal structure
(N_T(ω) = (2/τ_0)·ℏω·coth(ℏω/(2k_BT))).

Evaluate at the framework's natural crossover scale ωτ_0 = 1, giving
k_* = 1/(cτ_0). The crossover wavelength is **~81 Mpc** — galaxy-cluster
/ BAO scale, well within the observable universe.

### The dimensional variance

    ⟨|δz_{k*}(1/τ_0)|²⟩ = 2π G c² × coth(ℏ/(2k_BT τ_0))

This is a definite physical result with units [m²/(kg·s)] from G c².

### The dimensionless P_ζ depends on rescaling choice

To convert to dimensionless P_ζ for comparison with A_s, a rescaling
is required. Three natural choices:

| Rescaling | Natural ratio | P_ζ formula | P_ζ value | α-S structure | vs A_s |
|:---|:---|:---|:---|:---|:---:|
| **(A) Planck** | t_Pl/τ_0 | (1/π)(t_Pl/τ_0)³ | 2.16×10⁻¹⁷⁶ | NONE | factor 10¹⁶⁷ too small |
| **(B) Cosmic-baseline** | τ_0/τ_Λ = 1/S | 1/(πS³) | 8.15×10⁻⁹ | S³ — IN α/S³ family | factor 3.88 |
| **(C) H_inf** | H_inf·τ_0 = (2-R)/S | ((2-R)/S)³/π | 4.92×10⁻⁹ | (2-R)³/S³ — also S³ family | factor 2.34 |

### Critical finding — α/S³ family IS recovered under (B) and (C)

The numerical relationship between (B) and α/S³:

    1/(πS³) / (α/S³) = 1/(α·π) = 3/π ≈ 0.9549

So 1/(πS³) and α/S³ differ by ~5%, both have S³ structure. The
cosmic-baseline rescaling produces a member of the α/S³ family at
factor 3.88 from observed A_s — slightly closer than α/S³ itself.

Under H_inf rescaling, ((2-R)/S)³/π ≈ 4.92×10⁻⁹ is even closer
(factor 2.34 from A_s), still in the S³ family with the (2-R)³
prefactor.

Under Planck rescaling, the result is (t_Pl/τ_0)³ — no α-S structure
at all, and 167 orders of magnitude below A_s.

### The framework does NOT pin the rescaling

This is the load-bearing finding. The choice between (A), (B), and
(C) corresponds to the choice of natural unit for cosmological-
perturbation power spectra in the framework. Specifically:

- (A) treats fluctuations as fundamentally Planck-scale, with τ_0
  measuring their decay timescale. Makes sense if cosmological
  perturbation theory is constructed at the Planck scale.
- (B) treats τ_Λ as the natural cosmological timescale; fluctuations
  are measured relative to the cosmic-baseline scale. Makes sense
  if cosmological perturbation theory is constructed at the τ_Λ scale.
- (C) treats H_inf as the natural Hubble scale; fluctuations are
  measured analogously to standard inflation but using GRUT's
  terminal-velocity H rather than an inflationary H.

The framework currently provides no formal cosmological perturbation
theory that would pin one of these choices. **This is precisely the
n_g(ω) covariance open negative (#9 in the ledger).** Closing #9 —
specifically, deciding whether ω is Fourier frequency, conformal-time
frequency, or some covariantly-defined object, AND mapping the result
to standard MG-EFT μ(k,a)/γ(k,a) parameterization — would pin the
natural rescaling and thereby determine whether A_s lands at ~10⁻¹⁷⁶
(Planck) or ~10⁻⁹ (cosmic-baseline).

### Stage 2 verdict

**RESCALING-CONDITIONAL.** Lens B/F's forward derivation does not
produce a clean honest negative on the α/S³ coincidence. Under one
of three plausible rescalings, the α/S³ family IS recovered at
roughly the right magnitude. Under another, the result fails by 167
orders. The framework's choice between rescalings is an upstream
gap (the n_g(ω) covariance open negative).

The α/S³ coincidence is therefore **conditionally derived**, blocked
on closing the covariance gap — not closed as coincidence.

### Structural link to open negative #9

`primordial_amplitude_zero_parameter_open_negative` is now formally
linked to `n_g_omega_cosmological_covariance_open_question` via the
ledger's `blocked_by` field. This is a structural finding: closing
#9 either closes the primordial-amplitude gap with A_s ~ 1/(πS³)
(cosmic-baseline rescaling, match within factor 4) OR sharpens its
honest negative with A_s ~ (t_Pl/τ_0)³ (Planck rescaling, fails by
167 orders).

### What this means about the user's flagged concerns

- **Flag 1 (z=0 vs z=z*):** Lens B/F was computed at z = 0.
  Linearizing around z = z* would introduce A_* = z_target'(z*) - 1
  in the denominator (1 + ω²τ_0² + A_*² for noise pump). This
  doesn't change the rescaling-sensitivity finding but adds an
  additional unknown (z_target'(z*)) that the framework also
  doesn't pin. Implemented in `power_spectrum_at_z_star()`.
- **Flag 2 (scale choice):** The crossover ωτ_0 = 1 was chosen.
  Implemented `power_spectrum_at_alternative_scales()` evaluating
  at ω = H_inf and ω = c·k_pivot as alternatives. The crossover
  is the framework-natural choice; the others give different but
  related results.
- **Flag 3 (rescaling):** This was the load-bearing flag. The
  rescaling sensitivity is now fully analyzed and reported — it
  IS the central Stage-2 finding.
- **Flag 4 (success criterion):** Pre-commitment to expected
  failure was right under Planck rescaling. The discipline held —
  no parameter tuning was applied. The success criterion that
  "α/S³-as-evidence" requires has been refined: it requires either
  (a) closure of #9 selecting cosmic-baseline rescaling, or (b)
  an independent derivation producing α/S³.

### Implications for next steps

Lens B/F has produced a definite conditional result. Lenses C
(bandwidth integral at primordial scale) and D (alternative OU
rescaling) could provide independent cross-check on which rescaling
the framework's other infrastructure prefers. They are no longer
strictly necessary — the covariance gap is the central blocker.

---

## Stage 2 — Forward derivation candidates (PRIOR PLAN, superseded)

Three concrete calculations to attempt:

1. **Bandwidth-integral evaluated at the inflationary/primordial
   scale.** Use existing `grut/derived/cosmology/bandwidth_integral.py`
   machinery; evaluate at k_* (primordial pivot) instead of galactic
   modes. Document what α-S structure emerges.

2. **OU-process variance with τ_Λ rescaling instead of ℏ.** Path A
   from Stage 1 used ⟨h²⟩/ℏ. Alternative natural rescaling:
   ⟨h²⟩/(τ_Λ × ℏ) or ⟨h²⟩/(τ₀² × E_Pl). Document each.

3. **Cosmological-perturbation theory in the constitutive
   framework.** Linearize the constitutive equation around a
   homogeneous-isotropic background; identify ζ as the gauge-
   invariant curvature; compute ⟨ζ²⟩ at horizon crossing using
   the noise kernel as the source. This is the closest GRUT
   analogue to the standard inflationary derivation.

**Stage 2 honesty protocol:**

- Each candidate must produce its actual α-S scaling, not be
  steered toward α/S³.
- If a candidate produces α/S^n for n ≠ 3, that's *informative* —
  the framework's natural primordial scaling is what it is, even
  if it doesn't match the dimensional coincidence.
- If no candidate produces anything close to α/S³, the coincidence
  stays a coincidence with documented attempted physical motivation.

---

## Stage 3 — Numerical comparison (PENDING)

Compare each Stage-2 derivation's output to:
- The α/S³ ≈ 8.53 × 10⁻⁹ dimensional coincidence;
- The observed A_s ≈ 2.1 × 10⁻⁹.

Possible outcomes per Stage-2 candidate:
- **Exact match to α/S³:** the dimensional coincidence becomes
  evidence; the derivation is the framework's natural primordial
  amplitude.
- **Different scaling:** the framework has a different natural
  primordial amplitude. Compare to A_s on its own merits.
- **No clean output:** the candidate fails. Move to next candidate.

---

## Stage 4 — Document and update (PENDING)

Three possible registry updates:

(a) **Derivation found that produces α/S³:** tier-promote
`primordial_amplitude_zero_parameter_open_negative` →
`anchored` or `scoping` (depending on rigor). New computed
claim documenting the derivation.

(b) **Derivation found producing different α-S scaling:** keep
the open negative for A_s match specifically, but add a new
claim documenting the framework's natural primordial-amplitude
scaling.

(c) **No derivation found:** keep open negative as-is, with notes
expanded to document Stage-1 algebraic decompositions and
Stage-2 attempts. The α/S³ coincidence remains explicitly a
coincidence, with the closure conditions narrowed by what the
investigation ruled out.

---

## End of Stage 1

Ten equivalent algebraic forms documented (F1–F10), spanning
integer-power, fractional-power, and α=1/3-specific identities.
Eight physical lenses identified (A–H), four physically plausible
for Stage-2 investigation. One duplicate caught in the original
Path-C candidate list (kT_c/E_Pl ≡ t_Pl/τ₀), reducing the
effective Stage-1 search space from 11 to 10 distinct numbers.

The Stage-2 search target is broadened: any natural derivation
producing a member of the α/S³ equivalence class counts as a
candidate, with the *form* of the derivation telling us which
physical picture is correct.

Pausing for review per investigation protocol.
