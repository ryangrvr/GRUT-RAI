# GRUT — Dark-Matter Candidate Test: Non-Thermal Coherent Residue in the Pre-Responsive Bath F(t)

**Tier: CONJECTURAL / deeper substrate-sector of GRUT (not a v4-core derivation).** A result about GRUT's own pre-responsive substrate layer F(t) — a deeper level of GRUT's layered ontology, not a successor theory. It stays conjectural and two-parameter, so it is NOT part of the zero-free-parameter v4 core. A clean NEGATIVE is a first-class result, banked exactly like the 4.71 keV warm shear phonon.

**Verdict (one line): (b) SHARPENED IMPOSSIBILITY — dark matter stays HOSTED, but the missing host is now SPECIFIED-AND-UNMET to the dex.**

---

## 1. Purpose & Charter

Dark matter in GRUT is **HOSTED**, not derived. Three no-gos block deriving it from the vacuum's own action (all theorems about the **vacuum's action**, `grut/toe/registry.py`): `vacuum_spectrum_pole_classification` (:5340 — single relaxational pole, single-mode ⇒ "dark matter is a HOSTED matter field, permanently"), `propagating_relic_forbidden_pincer` (:5471 — no second propagating vacuum pole; Ostrogradsky+Q/FDT), `locality_no_halo_theorem` (:5532 — no extended 1/r² halo from a local causal kernel). The only relic GRUT can FORCE — the elastic shear phonon at k_B T_c = 4.71 keV — is WARM, c_s = c, and overcloses (418×–5800×), with no cold window (`GRUT_GENESIS.md:101`).

**The reframe (the key move).** Drop the thermal-relic framing. Under it, every route inherits τ_micro = 4.71 keV. Test instead a **non-thermal coherent candidate** — a condensate / coherent field with NO temperature (the axion / fuzzy / wave-DM category: never equilibrated, a single coherent low-momentum field, zero entropy). Source it NOT in the vacuum action but in the **pre-responsive bath F(t)** — the substrate *beneath* the vacuum (`GRUT_V4_SPINE.md:311-312`: "beneath the vacuum itself, lies the microscopic KMS bath F(t): the only place a genuine cold relic … could attach").

**Direct internal hook (verified).** `genesis_noise_kernel.py:220-252` documents the onset spectrum `S_h(ω, T=0) ∝ ω/(1+(ωτ₀)²)` — Lorentzian×ω, **explicitly NOT Planck/Bose–Einstein**, with no equilibrium temperature. `GRUT_GENESIS.md:99` names the "Genesis instability seed … non-thermal S_h(ω)=Lorentzian×ω — pre-responsive fluctuating-but-memoryless field." A no-temperature source already lives in GRUT. The test: does that non-thermal onset admit a **coherent residue** that survives as dark matter?

**Charter compliance (non-negotiable).**
- F(t) is BENEATH the vacuum — it is GRUT's OWN pre-responsive substrate sector (`GRUT_V4_SPINE.md:311-312`: "the microscopic KMS bath F(t)… beneath the vacuum"), the layer Genesis is already built on (Q → F(t) → memory → responsive vacuum → physics). Giving F(t) field content breaks NO GRUT premise: Q intact, locality intact, the vacuum sector unchanged, the no-gos untouched (they are theorems about the *vacuum's* action). This is GRUT extending into its own deeper layer — **NOT** the vacuum-pole case `GRUT_V4_SPINE.md:670` forbids (that line scopes "constitutes a different theory, not GRUT" to a *new propagating vacuum pole / new mode* — adding field content to the substrate slot GRUT already posits is not that). The analogy: F(t)-microphysics is to GRUT what the Standard Model is to GR's T_μν — the content of a matter/substrate slot the umbrella theory already has, not a successor to it. Any POSITIVE here is therefore a **deeper substrate-sector result of GRUT (conjectural, not a v4-core derivation)**, **NEVER upgraded to DERIVED**. F(t) sits outside the no-gos' jurisdiction *precisely because* the no-gos are theorems about the vacuum's action, not the substrate under it.
- **Numerology guard in force.** The same standard that rejected 8π² ≈ 78.96 (+0.92%) as "not a GRUT-distinctive constant" and the A_s coincidence (`GRUT_GENESIS.md:502-508`; `registry.py:4474-4478`). NO mass, coupling, or abundance may be reverse-fit to Ω_dm. (The "Ledger L295" id at `GENESIS.md:502` is a cosmetic/fabricated id — the operative standard is the *substance* of the A_s/8π² rejection, not that id.)
- **Two kinds of wall.** SINGLE-MODE is a movable POSTULATE (channel-counting). The LOCALITY/NO-HALO theorem and the PROPAGATING-RELIC PINCER are THEOREMS — they move only by breaking a premise (Q or locality) = a different theory. The candidate must avoid tripping the **theorem-walls**; it may live only where they have no jurisdiction (F(t)).

A NEGATIVE is a first-class result.

---

## 2. The Specification — the no-gos read as a spec (the 4-item bar)

Read together, the three no-gos do not merely forbid — they **SPECIFY** the missing object. The candidate must clear all four:

1. **NON-THERMAL / COHERENT (no temperature)** — escapes the warm-relic wall by not being a thermal relic at all (zero entropy, coherent field ⟨φ⟩≠0, not an equilibrated ensemble).
2. **INTERMEDIATE SCALE** — in the EMPTY MIDDLE of the 34-order τ-gap. BOTH endpoints excluded: ℏ/τ_micro = 4.71 keV free-streams galactic structure away; ℏ/τ₀ ≈ 5×10⁻³¹ eV has a cosmological coherence length (too smooth to cluster). The clustering window (canonical fuzzy DM ~10⁻²² eV → kpc cores) sits BETWEEN them.
3. **SOURCED OUTSIDE THE VACUUM ACTION (F(t))** — so it trips NONE of the three no-gos. If it cannot avoid tripping them, that is a NEGATIVE.
4. **GRAVITATES VIA STANDARD GR, CLUSTERS, STABLE ≳14 Gyr, DELIVERS Ω_dm h² ≈ 0.12** — pre-responsive = above-T_c = local-GR coupling: a pre-responsive lump carries ordinary stress-energy and gravitates normally.

This is the no-gos read as a shopping list. The registry itself names the remedy: a "FOUNDATIONAL EXTENSION (a microscopic medium with massive excitations)" (`registry.py:5491-5494`).

---

## 3. Task A — the target window + dex-miss of τ_micro/τ₀

**The window is real and standard wave-DM physics** (all .venv-verified). de Broglie λ = ℏ/(m v):

| m | v | λ_dB | meaning |
|---|---|---|---|
| 10⁻²² eV | 10 km/s | **1.92 kpc** | canonical fuzzy-DM kpc soliton core |
| 10⁻²² eV | 100 km/s | 0.192 kpc | |
| 10⁻²² eV | 200 km/s | 0.096 kpc | |

Clustering window: log₁₀(m/eV) ∈ [−22, −19] (kpc cores; Lyman-α pushes the floor toward ~2×10⁻²¹ eV), center 3.16×10⁻²¹ eV (log₁₀ = −20.50).

**GRUT's two endpoints** (reproduced exactly from `closure_protocol.py` TAU_0_SEC, TAU_MICRO_SEC):

| anchor | energy | log₁₀(eV) |
|---|---|---|
| ℏ/τ_micro | 4713.68 eV = **4.7137 keV** | +3.673 |
| ℏ/τ₀ | **4.9775×10⁻³¹ eV** | −30.303 |

ℏ/τ_micro = k_B T_c **identically** (ratio = 1.000 in .venv) — the charter's flagged tautology, confirmed at `closure_protocol.py:411` (`TAU_MICRO_SEC = HBAR/(K_B*T_C_KELVIN_CANONICAL)`). It is an identity, not a second derivation.

**Endpoint span = 33.976 dex** = log₁₀(τ₀/τ_micro), the 34-order τ-gap, as it must be.

**The dex-miss on each side** (.venv; partition closes exactly):
- **UPPER:** ℏ/τ_micro overshoots the window TOP (10⁻¹⁹ eV) by **22.67 dex** — far too heavy/hot (as a relic it free-streams structure away; also WARM, c_s = c, overcloses 418×–5800×).
- **LOWER:** ℏ/τ₀ undershoots the window FLOOR (10⁻²² eV) by **8.30 dex** — far too light/smooth (its coherence length is cosmological; this scale is dark ENERGY, the Herglotz weight Ω_Λ, `GENESIS.md:97`, not a clusterer).
- **Check:** 22.673 (upper) + 3.000 (window) + 8.303 (lower) = **33.976 dex** = full span. The window is genuinely BETWEEN the two anchors and EMPTY.

---

## 4. Task B — bath-sourcing feasibility (the crux)

Does the genesis onset spectrum admit a coherent, zero-entropy component at an intermediate scale, **without importing a new scale by hand**? Two independent failures, both structural.

**(I) The spectrum deposits power ONLY at the two endpoints — never the middle.** `S_h(ω, T=0) = (2ℏ/τ₀)·ω/(1+(ωτ₀)²)` has exactly two features, and both sit at the excluded endpoints:
- The **amplitude peak** is at ω = 1/τ₀ (`genesis_noise_kernel.py:103-112`, `spectral_peak_omega_T0`), i.e. ℏω = ℏ/τ₀ = 4.98×10⁻³¹ eV — the τ₀ "too smooth" endpoint (verified: peak energy = ℏ/τ₀ exactly).
- The **integrated variance** ⟨h²⟩ (`:138-153`) is log-divergent: the power-per-log integrand d⟨h²⟩/d ln ω ∝ ω²/(1+(ωτ₀)²) is FLAT in log ω above 1/τ₀ all the way to the UV cutoff — so the variance accumulates at the high-ω / τ_micro = 4.71 keV endpoint.

Verified spectral shape (.venv): low-ω log-slope = **+1.000**, high-ω log-slope = **−1.000** (Lorentzian×ω, NOT the cubic-rise/exponential-cutoff Planck shape). The featureless flat-in-log integrand across the entire 34-decade middle means there is **no spectral feature at the fuzzy-DM window to seed a residue.** The spectrum literally has nothing to deposit there.

**(II) The coherence leg fails independently.** S_h is the symmetrized FDT/KMS noise spectrum = the two-point function ⟨{h,h}⟩ (`genesis_noise_kernel.py:65-95`, `kms_noise_spectrum`). At T=0, coth→1 and N = 2ℏω·Im χ is the zero-point fluctuation — a "fluctuating-but-memoryless" field with ⟨h⟩ = 0 and random phase (exactly `GENESIS.md:99`). A coherent / zero-entropy condensate requires a homogeneous classical expectation value ⟨φ⟩ ≠ 0 (misalignment-type) — a **different object** the noise spectrum does not carry. The in-repo verdict is explicit: "the onset produces no equilibrium temperature of its own" (`GENESIS.md:443-444`). The onset seed is incoherent zero-point noise, not a coherent field — it fails the coherence half of bar #1 at the source, before scale even enters.

**(III) No production mechanism reaches the middle without a new scale.** The only frequencies F(t) supplies are 1/τ₀ and 1/τ_micro — GRUT's two endpoint anchors. Meeting the spec demands TWO imported inputs:
- a **mass m** ∈ [10⁻²², 10⁻¹⁹] eV. A fuzzy m = 10⁻²² eV is a **THIRD frequency**, 8.30 dex above 1/τ₀ and 22.67 dex below 1/τ_micro — absent from {1/τ₀, 1/τ_micro};
- an **amplitude / decay constant** φ_i for the abundance — a SECOND independent input.

**Numerology guard applied (.venv).** The one natural dimensionless bridge — the geometric mean √(E_micro·E_τ₀) = **4.844×10⁻¹⁴ eV** (log₁₀ = −13.31) — misses the window center (−20.50) by **7.19 dex**. No clean combination (product/ratio/mean) of the two endpoints lands in the window without a third number. This is not even a sub-1% near-miss to reject — it simply does not point at the window. By the framework's own A_s/8π²-rejection standard, there is nothing to bank.

---

## 5. Task C — no-go consistency (the candidate IS clean)

A coherent field living in F(t) and gravitating as ordinary stress-energy trips **NONE** of the three walls. This is a genuine partial positive.

**(i) `propagating_relic_forbidden_pincer` (registry.py:5471).** A theorem about the **vacuum's OWN action** generating a relic: a propagating vacuum pole needs a higher-derivative TT operator ⇒ Ostrogradsky ghost ⇒ Im χ < 0 ⇒ (by FDT) N < 0 ⇒ violates Q. A **bath-sourced field is not a vacuum response**; it needs no second vacuum pole, so the pincer never engages. The registry names exactly this remedy: a "derived dark sector requires a FOUNDATIONAL EXTENSION (a microscopic medium with massive excitations)" (`:5491-5494`).

**(ii) `locality_no_halo_theorem` (registry.py:5532).** Forbids the **vacuum's response kernel** (matter→metric) from carrying a 1/k² inverse-Laplacian (manufacturing an extended halo out of baryons). A coherent field that clumps under its own self-gravity sources the metric through the ordinary Einstein equation (T_μν) — it **IS the matter, not the kernel**. The 1/∇² it uses is the STANDARD Newtonian Green's function, which the theorem explicitly permits for actual matter ("local in the field, NONLOCAL in matter"). Verified: `locality_no_halo` self-test reproduces 6/6 True (halo slope −1.026, source −0.004, analytic-kernel-keeps-local −0.002, pole-kernel-delocalizes −2.004, grut_kernel_analytic_at_k0 True). A bath field is a localized source, not the forbidden kernel.

**(iii) `vacuum_spectrum_pole_classification` (registry.py:5340).** "Single-mode vs multi-mode" concerns poles of the **vacuum response spectrum**. Phase II verdict (`:5398-5409`): "a dark mode requires an INERTIAL, matter-like degree of freedom … allowed only as an extension." F(t) **is** that extra inertial matter DOF, sitting beneath the vacuum — not a new vacuum pole. The single-mode result is untouched.

**Conclusion (Task C):** the candidate requires none of (i) a 2nd propagating vacuum pole, (ii) a 1/k² nonlocal inverse-Laplacian in the matter→metric kernel, (iii) a new relaxational vacuum pole. The no-gos have NO JURISDICTION over F(t) — they are theorems about the vacuum's action, and F(t) is GRUT's own substrate sector beneath it (`SPINE.md:311-312`). This is precisely why a positive here would be a deeper substrate-sector result of GRUT (conjectural, not a v4-core derivation), never a v4-core GRUT derivation — and equally never the vacuum-pole "different theory" of `SPINE.md:670`.

---

## 6. Adversarial Results

- **Does the bath field silently reinstate the 1/k² nonlocality?** No. The theorem scopes the ban to the *vacuum response kernel*. A self-gravitating lump is the matter T_μν coupling through the permitted Newtonian Green's function — explicitly named as allowed for actual matter. Verified 6/6 True.
- **Is the "non-thermal" claim real or definitional?** Real and computed: S_h(ω,T=0) ∝ ω/(1+(ωτ₀)²), slopes +1.000/−1.000, no temperature makes it coincide with Planck (`shape_difference_from_planck`). But it is a no-temperature **noise** spectrum, not a condensate — the reframe clears bar #1 *in category*, the GRUT *instance* does not (it carries ⟨h⟩=0, random phase).
- **Reverse-fit check.** The candidate masses (10⁻²²–10⁻¹⁹ eV) come from external canonical wave-DM phenomenology (kpc cores, Lyman-α floor), NOT back-solved from Ω_dm. φ_i is presented as the *consequence* of choosing m and flagged as un-forced, never sold as a prediction. To hit Ω_dm h² = 0.12 at m = 10⁻²² eV needs φ_i ≈ **1.095×10¹⁷ GeV** (≈ 0.045 M_Pl,red) — a number chosen to land the abundance is exactly the reverse-fit the guard forbids.
- **Genesis order parameter as amplitude?** No. f(T_c) = tanh(½) = **0.4621** is a *dimensionless* pole-amplitude fraction (`GENESIS.md:277-285`), not a GeV field VEV, and carries no mass.
- **Numerology-lean.** The geom-mean does not even point at the window (7.19 dex off). Rejected by the A_s/8π² standard; the "L295" id is cosmetic, cited by substance not id.

All cited file:lines real; all .venv numbers reproduce exactly.

---

## 7. Verdict

### VERDICT: (b) SHARPENED IMPOSSIBILITY — DM stays HOSTED, host now SPECIFIED-AND-UNMET to the dex.

| Bar | Result | Why |
|---|---|---|
| **1. Non-thermal / coherent** | CLEARED in CATEGORY, FAILS in INSTANCE | The reframe correctly escapes the warm-relic wall (a zero-entropy coherent field does not inherit τ_micro). A real no-temperature source exists in F(t): `S_h(ω,T=0) ∝ ω/(1+(ωτ₀)²)`, slopes ±1.000. **But** GRUT's instance is symmetrized KMS **noise** ⟨{h,h}⟩ with ⟨h⟩=0, random-phase, "fluctuating-but-memoryless" — a dissipative spectrum, not a condensate ⟨φ⟩≠0. |
| **2. Intermediate scale** | WINDOW OPEN, NOT MET | The window log₁₀(m/eV) ∈ [−22,−19] sits in the genuinely empty middle (22.67 dex below ℏ/τ_micro, 8.30 dex above ℏ/τ₀). **But** the bath's only feature is the peak at ω=1/τ₀ — *at* the too-smooth endpoint. The power-per-log integrand is featureless flat across all 34 decades; no feature in the middle. |
| **3. Sourced outside the vacuum action** | CLEARED (genuine partial positive) | F(t) is the substrate beneath the vacuum. Trips NONE of the three no-gos (Task C). |
| **4. Gravitates / clusters / stable / Ω_dm h²≈0.12** | FAILS — the binding obstacle | Misalignment needs TWO un-forced dimensionful inputs: a mass m AND an amplitude φ_i (≈1.095×10¹⁷ GeV at m=10⁻²² eV). F(t) supplies neither — no V(φ), no mass term, no field VEV; f(T_c)=0.4621 is dimensionless. |

**Which wall binds.** **Not the no-gos** (Task C: clean) and **not the scale window per se** (Bar 2: genuinely open, 8.30–22.67 dex of room). The binding wall is **Bar 4 sourcing under the numerology guard.** GRUT's F(t) is specified *only* as a memoryless KMS noise spectrum (Lorentzian×ω, peaked at the τ₀ endpoint) — no potential, no mass term, no amplitude. A coherent relic needs all three. Reaching the middle requires a **third scale** (m ∈ [10⁻²², 10⁻¹⁹] eV) plus an **independent abundance dial** (φ_i ~ 10¹⁶–10¹⁷ GeV); picking them to land Ω_dm = 0.12 is the forbidden reverse-fit.

**The win (the specification upgrade).** The single-mode/no-DM conclusion moves from "single-mode postulate + warm-relic miss" to a **specified-and-unsourced shopping list for GRUT's own substrate sector F(t).** The missing microphysics of F(t) must supply, all beneath the vacuum (so it trips no theorem-wall — and crucially, all *inside* GRUT's existing substrate slot, not the new vacuum pole `SPINE.md:670` forbids):
- (i) a **coherent zero-entropy scalar** with ⟨φ⟩ ≠ 0 (the reframe is the right category);
- (ii) a **new mass scale** m ∈ [10⁻²² eV, ~keV], sweet spot ~10⁻²² eV for kpc cores — a third anchor 22.67 dex below ℏ/τ_micro and 8.30 dex above ℏ/τ₀ that GRUT does not contain;
- (iii) an **independent amplitude** φ_i ~ 10¹⁶–10¹⁷ GeV, frozen by Hubble friction until H~m, then matter-like a⁻³ (automatically cold, stable ≫14 Gyr), gravitating via ordinary T_μν.

The empty middle is now mapped to the dex.

**Falsifier.** The candidate (or any F(t)-microphysics filling the substrate slot) is falsified if the wave-DM soliton-core scale is excluded observationally: small-scale power suppression vs **Lyman-α forest + Milky-Way dwarf-satellite counts** pushing the fuzzy-DM mass floor above ~2×10⁻²¹ eV and closing the kpc-core window. If the clustering window itself is observationally eliminated, the substrate slot is empty regardless of what F(t) could supply — the impossibility becomes total rather than sharpened.

**Tier.** CONJECTURAL / deeper substrate-sector of GRUT (not a v4-core derivation). Even a positive here would be a deeper-layer result of GRUT (detailing its own pre-responsive substrate F(t)), never a v4-core DERIVATION — and never the vacuum-pole "different theory" of `SPINE.md:670`. It carries 2 free dimensionful parameters (m, φ_i) + an inserted potential shape, so it stays outside the zero-free-parameter v4 core. This is a clean NEGATIVE — a first-class result, banked exactly like the 4.71 keV warm shear phonon.

---

**Better DEFINITION of dark matter (GRUT's layered ontology):** *Dark matter is a no-go-clean coherent scalar resident in GRUT's own pre-responsive substrate layer F(t) — internal to GRUT's layered ontology (Q → F(t) → responsiveness → vacuum → physics) at the substrate level, NOT external to it — gravitating by ordinary GR stress-energy, carrying one new intermediate mass scale (~10⁻²² eV, in the empty middle of GRUT's 34-order τ-gap) and one independent abundance amplitude. The vacuum sector still does not generate it (the three no-gos hold); but it is contained in GRUT's own deeper substrate layer, not in a successor theory. It is two-parameter and conjectural — specified-and-unmet, not derived, and not part of the zero-free-parameter v4 core.*

---

**Verified file:lines:** `grut/foundation/closure_protocol.py:411` (τ_micro tautology); `grut/toe/registry.py:5340` / `:5471` / `:5532` (three no-gos), `:5491-5494` (foundational-extension remedy), `:4474-4478` (numerology guard); `grut/derived/cosmology/genesis_noise_kernel.py:65-95` (KMS noise), `:103-112` (peak at 1/τ₀), `:220-252` (non-thermal shape); `theory/GRUT_GENESIS.md:99` (non-thermal seed), `:443-444` (no equilibrium T of its own), `:502-508` (A_s/8π² rejection standard; "L295" cosmetic id); `theory/GRUT_V4_SPINE.md:311-312` (F(t) substrate), `:670` (different theory). All .venv numbers reproduced exactly.
