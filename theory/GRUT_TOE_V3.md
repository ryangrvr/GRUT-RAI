# GRUT — The Theory of Everything, Version 3

**The Geometric Response of the Unitary Time-contour.**
Version 3.0 · June 2026 · branch `main_v3`
Operative root: `grut/v3/picture.py` · audited source of truth: `grut/toe/registry.py` (116 claims) + `grut/toe/ledger.py` (28 open negatives, 1:1)

> **Status.** This is the v3 edition. It inherits the verified v2 backend (frozen at tag `v2-final`) and
> presents only what survived a full adversarial re-audit. Every claim below is stated at its **audited
> tier** — computed, anchored, conjectural, foundational, or open-negative — and the tiers are enforced by
> the test suite (3,227 passing). Where v2 over-claimed, v3 demotes and says so. The recurring signature of
> this edition: **the mathematics usually survives; the ontology changes.**

---

> **How GRUT is built, tested, and carried.** GRUT is carried by **GRUT-RAI** — the *Responsive AI* research
> platform that implements the theory as runnable code, not prose alone. Every quantitative claim is a
> structured record in the **claim registry** (`grut/toe/registry.py`, 116 claims): the physical statement,
> its audited tier, the code that computes it, the tests that check it, its dependencies, and the observation
> that would falsify it. Every claim in this document is backed, one-to-one, by such a record. The framework is
> held to account by **3,227 passing tests** — every *computed* result reproduces from the code — and
> enforcement tests (`tests/toe/test_registry_completeness.py`, `tests/toe/test_ledger.py`) guarantee that no
> claim is left unregistered, untested, or untiered, and that each of the **28 open negatives** carries a 1:1
> entry in the **open-question ledger** (`grut/toe/ledger.py`) stating its closure condition, the effort
> required, and which results it would strengthen. Registry, tests, and ledger are one source of truth; nothing
> is hand-curated or fitted away.

---

## Abstract

GRUT is **general relativity's long-wavelength rescaling redundancy, broken in a controlled way by exactly
one memory scale** `L₀ = c·τ₀ ≈ 12.85 Mpc`. A theory is defined by *which* symmetry it breaks and by *how
much*; GRUT breaks the adiabatic spatial-dilatation redundancy of GR by one finite memory length, the same
shape by which a particle mass breaks scale invariance. From this single broken symmetry, two proven/
postulated pillars, and **one dimensionless axiom** `α = 1/3`, the framework reconstructs a universe whose
*linear* cosmology is exactly ΛCDM, fixes a set of certified constants and one sharp tabletop falsifier, and
— this is the v3 result — proves by a locality theorem that it possesses **no derived dark-matter mechanism**:
dark matter is a hosted input. The cost of honesty is the gain in falsifiability.

---

# PART I — THE PICTURE

## 1. The picture in one line

> GRUT is GR's adiabatic-rescaling redundancy `D`, broken by finite memory `F`, observed through the
> closed-time-path response `Q`. "The vacuum responds only to physically distinguishable structure" is the
> *name* for the conjunction `Q ∩ F ∩ D` — not a separate axiom.

| | | Standing |
|---|---|---|
| **Q** | CTP / in-in unitarity — physics is the response to *realized differences*, `S_IF[φ₊=φ₋] = 0` | **proven** (theorem of the formalism) |
| **F** | finite single-pole memory `χ(ω) = 1/(1 − iωτ₀)` — causal, bounded, GR-recovering | **postulated** (one scale, τ₀) |
| **D** | the adiabatic-dilatation redundancy of GR | **bridge** — *F breaks D* (theorem, outcome B) |

The whole theory is the disciplined unfolding of this sentence. Chapters 1–4 establish the three letters;
Part II builds the universe forward from them; Part III audits each physical sector against them; Part IV is
the honest ledger of what is *not* yet derived.

## 2. The single axiom and the single scale

GRUT admits **exactly one dimensionless axiom and one dimensionful input.**

**The axiom — `α_vac = 1/3`** (`alpha_vac_axiom`, *foundational*). The vacuum impedance / deep-IR refractive
normalization. It is *posited*, the way `c` and `ℏ` are posited. A conditional theorem is verified
Fraction-exact at code level: **if** the gravitational conformal mode (`g_μν = e^{2σ}ĝ_μν`, σ one real
conformally-coupled scalar, `ξ_c = 1/6`) **is** the IR carrier, **then** the trace anomaly `a/c = 1/3`
(Komargodski–Schwimmer 2011). The framework adopts `α = 1/3`; its **first-principles derivation is OPEN**
(`alpha_vac_derivation`, *open-negative* + ledger): the antecedent is unproven and the historical "vacuum
impedance = 1/d" origin is ungrounded. From α follow the deep-IR refractive index `R = √(4/3) ≈ 1.1547`
(Ch. 7) and the screening constant `S = 108π` (Ch. 4).

**The scale — `τ₀ = 41.9 Myr`** (`tau_0_derivation`, *computed*; `tau_0_cross_consistency`, *anchored*). The
single relaxation time. It is **anchored** by convergent observation, not derived from the CTP formalism:
cosmic-baseline routes cluster at 41.4 ± 1.5 Myr, cluster-merger routes at 50.0 ± 3 Myr, agreeing at the
20.7% level (within the ~30% observational uncertainty, with a documented systematic). It defines the memory
length `L₀ = c·τ₀ ≈ 12.85 Mpc` — **the one scale that breaks D** — and through it every dimensionless `ωτ₀`
regime by which a GRUT prediction must be classified. **Zero free parameters** beyond {α, τ₀}
(`zero_free_parameters`, *computed*).

## 3. The responsive vacuum (Q) — proven

Physics is the response to *realized* differences. On the closed time path the influence action vanishes on
the classical diagonal, `S_IF[h₊ = h₋] = 0`, and the physical response is `δS_IF/δh_q|_{q=0}`
(`ctp_action_structure`, *computed*). The vacuum's response obeys a first-order constitutive law

```
τ₀ ż + z = z_target          (Mori–Zwanzig; constitutive_equation, computed)
```

whose single-pole susceptibility `χ(ω) = 1/(1 − iωτ₀)` is the Fourier transform of exponential relaxation —
causal, Kramers–Kronig compatible, GR-recovering at high frequency. The retarded memory kernel
(`memory_kernel_form`, *computed*) is, in the surviving transverse channel,

```
K^R_μνρσ(ω) = α_vac · χ(ω) · P^TT_μνρσ
```

— temporal memory `χ(ω)` times the dimensionless transverse-tracefree projector `P^TT`. **General relativity
is recovered** in the memoryless / high-frequency limit (`gr_recovery`, *computed*); the solar system is safe
(`solar_system_safety`, *computed*).

## 4. The organizing principle — F breaks D

The load-bearing theorem of v3 (`adiabatic_dilatation_redundancy_nogo`, *computed*;
`organizing_structure_v3`, *foundational*):

> The adiabatic spatial-dilatation redundancy `D` is exact only in the memoryless `L₀ → 0` limit. Finite
> memory `F` breaks it for every `k ≠ 0` at order `(L₀ k_phys)²` — **non-anomalously**: the trace-anomaly
> coefficient α does *not* enter the breaking (outcome **B**, independently verified). GRUT is what GR
> becomes when this one redundancy is gently broken by one length.

This is the spine. Everything downstream — the no-gos, the emergent ΛCDM universe, the closed dark sector —
is a consequence of *which* symmetry is broken and by *how much*.

---

# PART II — THE FORWARD BUILD

The v3 universe is constructed in six steps (`grut/v3/picture.forward_chain()`); each is what the previous
one entails.

## 5. The boundary operator — what the vacuum is forbidden to respond to

The no-gos are not failures; they map the shape of the allowed solution space.

- **Pure-gauge / adiabatic modes** ⇒ **`μ_linear = 1`.** A conformal-mode scalar response cannot be
  separate-universe invariant at `k → 0`; the long-wavelength adiabatic mode *is* the separate-universe mode.
  Conformal enhancement and separate-universe invariance are mutually exclusive on linear scalars. Therefore
  the linear modified-gravity enhancement (`μ → 4/3`) is **ruled out** — by consistency *and* by the low-ℓ
  CMB ISW (≈ 2.79×, ~32σ). **Linear cosmology is exactly ΛCDM** — a *derived requirement*, not a fit.
- **The bare gauge-dependent density**, and **unbounded / infinite response**, are likewise forbidden.

## 6. The emergent universe — what is certified

| Quantity | Value | Tier | Claim |
|---|---|---|---|
| α (vacuum impedance) | 1/3 | **axiom** | `alpha_vac_axiom` |
| R (deep-IR refractive index) | √(4/3) ≈ 1.1547 | computed | `r_canonical_path_g`, `three_routes_convergence` |
| τ₀ (relaxation time) | 41.9 Myr | anchored | `tau_0_cross_consistency` |
| L₀ (memory length) | c·τ₀ ≈ 12.85 Mpc | derived | — |
| S (screening) | 108π | computed | `screening_108pi` |
| μ_linear | 1 (⇒ linear cosmology = ΛCDM) | computed | (boundary operator) |
| η_B (baryon asymmetry) | ≈ 6.6×10⁻¹⁰ | computed | `baryogenesis_eta_b` |
| H₀ | ≈ 68.8 km/s/Mpc | anchored | `h_0_prediction` |
| Ω_Λ | 0.6886 (Planck: 0.6889) | anchored | `omega_lambda_prediction` |
| decoherence plateau | ~689 Hz | computed | `decoherence_plateau` |
| a₀ (MOND scale) | cH₀/2π | computed | `mond_a_0_emergence` |

The cosmological constant appears as a terminal velocity; the background `H(z)`/BAO are ΛCDM-level. The
headline numbers `H₀`, `Ω_Λ` are honestly **anchored** — clean consequences of the empirical `τ₀`, not
first-principles derivations.

---

# PART III — THE SECTORS (at audited tiers)

## 7. Cosmological parameters (Ch. 8)

`H₀ ≈ 68.8 km/s/Mpc` sits in the Hubble-tension gap between Planck (67.4) and SH0ES (73.0) — GRUT's natural
value lies between them (`h_0_prediction`, *anchored*). `Ω_Λ = 0.6886` matches Planck 2018 to 0.04%
(`omega_lambda_prediction`, *anchored*; zero free parameters in the `H_inf → Ω_Λ` conversion, but the input
`τ₀` is empirically anchored). `H_inf` decomposition, the thermal transition `T_c`, and the cross-sector
bridge parameter are *computed* (`h_inf_decomposition`, `t_c_thermal_transition`, `bridge_parameter_cross_sector`).
The dual microphysical scale `τ_micro = ℏ/(k_B T_c)` is *conjectural* (an inverse definition from an anchored
input; its interpretation as a vacuum-microstate relaxation time is open).

## 8. Gravitational decoherence — the primary falsifier (Ch. 5)

GRUT's sharpest near-term, table-top prediction: a **gravitational-decoherence plateau at ~689 Hz**
(`decoherence_plateau`, *computed*), with a CSL/isotope discriminator (`grut_csl_isotope_discriminator`) and a
systematic comparison against alternative collapse models (`decoherence_alternative_models_comparison`). The
gravitational entanglement formation rate is *anchored* (`gravitational_entanglement_formation_rate`). This is
the cleanest place the theory can be killed in a laboratory.

## 9. Saturation & black holes (Ch. 6)

Finite memory caps curvature. The Ricci scalar of a matter-bearing interior saturates at
`R_max = α_vac/(c²τ₀²) ≈ 2.1×10⁻⁴⁸ m⁻²`, and via Einstein's equation every black-hole core reaches a
mass-independent `ρ_max ≈ 1.1×10⁻²² kg/m³`. **v3 re-audit demoted both to *conjectural***
(`r_max_ricci_saturation`, `rho_max_universal`): the *values* are anchored consequences of {α, τ₀}, but the
saturation *mechanism* is not yet derived from the full CTP closure. The linearized `Φ_μν` response is
*computed* (`phi_munu_linearized_derivation`); its FRW construction is *conjectural*, valid only in the WKB
regime (`phi_munu_frw_explicit_construction`).

## 10. The trace-anomaly R-routes (Ch. 7)

The deep-IR refractive index `R ≈ 1.154` is confirmed by **two independent computed routes** that share no
inputs: Path G (tree-level `√(4/3) ≈ 1.15470`, zero couplings) and Osborn (1-loop coupling-corrected at M_Z,
`1.15367`) — agreement to 0.1% is independent confirmation (`r_canonical_path_g`, `r_path_osborn_epsilon`,
`three_routes_convergence`, all *computed*). The Christensen–Duff Euler-diagonal identity is exact
(*computed*). A third route (V7 §26 3-loop CTP) is **open-negative** (`tji_7_4_open_negative` — the round-S⁴
Euler anomaly quotient is symbolically constructed but numerically uncomputed). The SM 1-loop cross-checks are
*conjectural* (Dirac, `r_path_d_dirac`) and **open-negative** (Majorana, a rejected alternative).

## 11. Flavor (Ch. 9) — hosted

The charged-lepton **Koide ratio `K = 2/3`** is GRUT's *empirical anchor* for the Z₃ flavor structure,
verified to 0.005% (`koide_k_2_over_3`, *anchored* — empirical input, not a derivation; the fixed-point no-go
bars deriving the amplitude `A = √2`). The Z₃ circulant structure and the `θ = 2/9` uniqueness are *computed*
(`koide_z3_circulant_structure`, `koide_theta_2_over_9_uniqueness`); the structure provably does **not**
extend to neutrinos as charged leptons (`charged_lepton_z3_does_not_extend_to_neutrinos`, *computed*). With
the coupling `a_ν = 1` derived (boundary-degenerate uniqueness theorem, Correction #29), the **normal
hierarchy is a unique, falsifiable prediction** (`neutrino_hierarchy_z3_nh_prediction`, *computed* — promoted
in the v3 re-audit), testable by JUNO/DUNE, CMB-S4, Project 8, 0νββ. The Standard Model **satisfies** five
CTP-derived structural constraints (gauge group, anomaly cancellation, three generations, Koide, trace
anomaly), verified *consistent* — but **uniqueness is not established** (`sm_emergence`, *computed* for
consistency only). Flavor is **hosted** Standard-Model input.

## 12. Measurement & quantum mechanics (Ch. 10–11)

Quantum mechanics is *recovered* (`qm_recovery`, *computed*); the arrow of time follows from entropy
production (`arrow_of_time_from_entropy`, *computed*). Measurement resolves as CTP contact (`measurement_resolution`,
`lambda_contact_ctp_derivation`, `wigner_friend_dissolution`, all *computed*); the ontic/epistemic split of
the `μ`/`γ` rates is *computed*. The Bayesian observer-filtering equation and the position-basis pointer are
*anchored* epistemic machinery (not first-principles derived). The **Born rule remains a postulate**
(`born_rule_postulate_open_negative`). The "observer-as-crystal" and neural-resonance framings are explicitly
*conjectural/speculative* and labeled as such. Black-hole information recovery is *anchored/partial*. The
Schrödinger's-cat thought experiment is reframed with the observer as the boxed, information-limited system
(`schrodinger_in_box_inversion`, *anchored*) — synchronization through contact, not creation through measurement.

## 13. The dark sector — the closed chapter (Ch. 9)

This is the chapter v3 rewrote. The audit (Tests 01–06) and the constructive-phase K⁽²⁾ flagship reduced the
dark sector from a sprawl of mechanisms to a single computation, then closed it.

**What was ruled out**
- **Linear / dielectric `Ω_dm = α = 1/3`** — the bandwidth integral is correct math computing a *ruled-out*
  linear branch (`omega_dm_equals_alpha`, `bandwidth_integral`, both *open-negative*): `μ_linear = 1` forbids
  it; CMB-ISW falsifies it at 32σ.
- **The linear growth enhancement** — archived/ruled out (`modified_linear_growth_first_look`, *open-negative*).
- **The orbital-gate (C5b) mechanism** — refuted; realized structure ~1/√N, negligible (Test 03).
- **The Kibble–Zurek route** — retracted (`kibble_zurek_dm_route`, *open-negative*).

**What survives**
- **The MOND scale `a₀ = cH₀/2π` is *derived*** (`mond_a_0_emergence`, *computed*) — the *scale* is real; the
  interpolation function `ν(y)` is adopted, not derived — and Test 07 shows it *cannot* be derived locally
  (it is a response to the acceleration `g = ∇Φ`, the forbidden nonlocal `1/∇²`). Rotation-curve and bullet-cluster *fits* via this
  scale are *computed* (`rotation_curves_match`, `bullet_cluster_offset`).

**The flagship — C5a, the W² second-order channel — and its closure.**
After everything else died, exactly one channel remained: the second-order Weyl-squared response
(`c5a_weyl_squared_dark_sector`). The constructive phase computed it (`grut/derivation/phi_munu/second_order_kernel.py`;
`theory/GRUT_V3_K2_DERIVATION.md`):

1. **Operator (Stage A):** `W²` is the *unique* dynamically-active second-order operator (E₄ is topologically
   dormant; Ricci-built terms are forbidden by `μ_linear = 1`).
2. **Scale (Stage B):** the explicit kernel `K⁽²⁾(ω,k) = σ·α·χ(ω)` carries **no `1/k²` pole** ⇒ the coupling
   length is forced to `L₀`. A spatially-local causal memory kernel is a polynomial in `k²`; it cannot
   manufacture the inverse Laplacian a different scale would need.
3. **Magnitude (Stage C):** `ρ_eff/ρ_baryon ~ O(1–100)` at galactic scales — *viable*, **not** the `10⁻²⁷` an
   intermediate calculation reported (a unit-mixing + wrong-Weyl-formula error, caught before banking),
   because `L₀ ≈` the curvature radius of a weak-field galaxy.
4. **Shape (Stage D + Test 06):** `ρ_eff ∝ W² ∝ (ρ − ⟨ρ⟩)²` falls as `1/r⁴` (interior) to `1/r⁶` (outskirts)
   — far steeper than the `1/r²` a flat rotation curve requires. **This is a theorem, not an artifact**
   (`theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md`): every permitted local tensor realization gives the same
   too-steep profile, and shallowing to `1/r²` requires the very `1/∇²` the locality result forbids. The
   `P^TT` projector's `k̂k̂/k²` is degree-0 angular structure, not an inverse Laplacian.

**Test 07 — the locality–no-halo theorem (spectral form; `locality_no_halo_theorem`, *computed*).** The
failure is not really about `W²` — it is about **analyticity at `k = 0`**, and in that form it classifies
the *entire category* of local mechanisms at once. A flat-curve halo (`ρ ∝ 1/r²`) has a `k = 0`
*singularity* (`ρ(k) ∝ 1/k`); a localized baryon source is analytic there; so an extended halo can appear
only if the **response itself is singular at `k = 0`** — a pole / inverse-Laplacian `1/∇²`. Every
covariant, matter-local GRUT response is *analytic* at `k = 0`, walled off three independent ways:
curvature invariants give `≥ 1/r⁶`; the acceleration `g = ∇Φ` would give `1/r²` but is non-covariant
**and** is the nonlocal `1/∇²` of the matter (`g = ∇(1/∇²)ρ` — the enclosed mass); a response linear in
`ρ_b` is forbidden by the No-Go. **MOND is the illuminating case** — it produces the right `1/r²` phantom
precisely *because* it responds to `g`, the forbidden nonlocal object, which is exactly why GRUT carries
the *scale* `a₀` but cannot locally derive an interpolation *function*. **Therefore no local GRUT response
can be a halo, and a derived dark sector requires a NEW POLE in the vacuum spectrum (a stable massive
matter-like mode whose relic density is the hosted dark matter), not a new operator.** This one principle
— locality = analyticity at `k = 0` — subsumes the linear-enhancement, dielectric, orbital-gate, Weyl²
and Bach no-gos, and reframes the dark-matter question as the **Spectrum Program**
(`theory/GRUT_V3_TEST_07_LOCALITY_NO_HALO.md`).

> **Verdict.** C5a has roughly the right magnitude but the wrong radial profile to be the dark-matter halo.
> **GRUT has no derived dark-matter mechanism reproducing halo phenomenology; dark matter is a HOSTED input**
> (with the derived `a₀` scale and `μ_linear = 1`). The last survivor did not die because it was too weak — it
> died because it was *too local*. The TT/GW channel (C5c) remains a distinct *non-DM* signature (the 689 Hz
> falsifier), not a clustering mechanism.

The dark-matter mechanism search is **closed pending covariant review** — the only way back is to overturn a
foundational result (locality, the No-Go, the CTP structure, or the profile theorem), not to invent a new
channel. The constructive path forward is therefore the **Spectrum Program**: determine whether the
responsive vacuum's effective action contains an additional stable, massive pole — the one structure that
could host a *derived* dark sector. Absent such a pole, dark matter is a hosted input permanently.

---

# PART IV — HONESTY

## 14. The open-negatives ledger

v3 carries **28 open negatives**, each with a closure condition and effort estimate (`grut/toe/ledger.py`,
1:1 with the registry, test-enforced). The load-bearing ones:

| Open negative | What it is |
|---|---|
| `alpha_vac_derivation` | the first-principles derivation of α = 1/3 (the one axiom) — Riegert closure + IR-carrier antecedent |
| `c5a_weyl_squared_dark_sector` | the dark-matter channel — closed (right magnitude, wrong-profile theorem) |
| `omega_dm_equals_alpha`, `bandwidth_integral`, `modified_linear_growth_first_look` | the ruled-out linear dark sector (correct math, dead ontology) |
| `kibble_zurek_dm_route`, `r_path_d_majorana` | retracted exploration / rejected SM alternative |
| `tji_7_4_open_negative`, `two_route_convergence_physical_equivalence_open_question` | the third R-route (3-loop CTP) — numerically uncomputed |
| `born_rule_postulate_open_negative` | the Born rule remains postulated |
| `koide_phase_4_open_negative` | a first-principles fix of (M₀, θ) in the flavor sector |
| `phi_munu_frw_beyond_wkb_open_question` | the FRW response beyond WKB |

The honest position, stated plainly: GRUT rests on **one adopted axiom** (α) whose derivation is open, an
**anchored scale** (τ₀), a **proven** response principle (Q), a **postulated** memory (F), and a theorem that
it has **no derived dark sector**. That is a more falsifiable object than any version that hid these.

## 15. What changed, V2 → V3

- **Linear modified-gravity enhancement (μ → 4/3): RULED OUT** — do not reintroduce.
- **α = 1/3 is an axiom, not "derived/Gate-R-closed."** (v3 re-audit demotion.)
- **The dark-matter mechanism is closed** (locality theorem), not an open search.
- **`H₀`, `Ω_Λ`, `R_max`, `ρ_max`, Koide K, τ₀-consistency** re-tiered from "computed" to anchored/conjectural
  to match what was actually earned.
- **SM uniqueness** retracted to SM *consistency*.
- The default cosmology baseline is **stock ΛCDM** (not the GRUT-fork μ-always-on).

The full re-audit re-tiered 20 of ~70 inherited claims; the "certified" set is now a defended 46 computed +
18 anchored, with 28 honest open negatives.

## 16. Falsifiers & predictions dashboard

GRUT is killed by any of: a measured **gravitational-decoherence plateau ≠ ~689 Hz**; an **inverted neutrino
hierarchy** (the Z₃ structure predicts normal); a confirmed **linear modified-gravity enhancement** (μ ≠ 1)
on cosmological scales (the theory forbids it); or a first-principles result that **contradicts the dark-sector
locality theorem**. The six near-term tests are catalogued in `falsifier_paper_six_near_term_tests`.

---

## Appendices (inherited, verified)

- **A. The Claim Registry** — `grut/toe/registry.py` (116 claims, tier-enforced): the machine-readable source
  of truth this document is written against.
- **B. The Open-Negative Ledger** — `grut/toe/ledger.py` (28, 1:1).
- **C. Dependency graph & derivation index** — `dependency_graph_appendix`, `derivation_index_appendix`.
- **D. The dark-sector record** — `theory/GRUT_V3_TEST_0[1-6]_*.md`, `theory/GRUT_V3_K2_DERIVATION.md`.
- **E. The corrected physical picture** — `theory/GRUT_V3.md`, `theory/V2_TO_V3_SYNTHESIS.md`,
  `theory/GRUT_V3_ORGANIZING_STRUCTURE.md`.

---

*GRUT Research — www.zenodo.org/communities/GRUT. This v3 edition is precise where it earned it, honest-but-open
where it has not, and states which is which on every line. The math survives; the ontology changes.*
