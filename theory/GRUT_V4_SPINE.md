# GRUT ToE v4 — The Emergence of Everything

## How to read this

This document runs the universe forward — from before there was time, to the observers
who would one day measure it — and places each thing that emerges at its *true tier*. It
is the v4 **spine**: a single forward-time narrative that first states what GRUT is, then
tells the story of emergence epoch by epoch, and finally asks what kind of theory the
whole thing amounts to.

Two distinctions govern everything that follows.

**Umbrella vs. deliverable.** *GRUT* — Grand Responsive Universe Theory — is the umbrella
principle that the gravitational vacuum is a *responsive medium* rather than an inert
stage. It is not, by itself, a finished theory of everything; it is the stance from which
the finished theories are built. The falsifiable rungs built on that stance are named
*GRUT ToE vN*. This document is the v4 spine of that program. Where the prose says "GRUT
derives," read it as "the deliverable, built on the umbrella principle, derives."

**What makes it a Theory of Everything — the destination, not the present state.**
First, a tense correction this document holds to throughout: **GRUT ToE v4 is the current
rung, not the arrival.** *GRUT* (the umbrella) is the program; the **GRUT ToE vN** are its
falsifiable rungs; **a complete GRUT ToE is the *result* the program walks toward** as the
open rungs close. Aiming at that destination is what any serious program is entitled to do;
asserting one has arrived is not. So nothing below should be read as "v4 *is* the finished
theory of everything" — it is the latest honest map.

Second, what *kind* of completeness the destination has. A ToE, in the sense meant here, is
**not** a theory that *derives* everything. It is a theory that has a coherent, tiered
**place** for everything, with a **sharp boundary** — completeness of the *map*, not
omniscience. And this is a **deliberate commitment, not a shortfall**: GRUT's defining
minimalism (one dynamical metric, one memory channel, Q) *forbids* the moves a
derive-everything ToE would require, so the completed GRUT ToE is a complete tiered **map**
by construction. The places where GRUT must *receive* an input (HOSTED) or *forbids*
something from its own axioms (FORBIDDEN) are not gaps in the story. They are the **seams**
of a layered ontology showing through, woven into the narrative as such: *here the universe
makes X; here it must receive Y; here it forbids Z.*

Third, adaptability — stated precisely so it is not a loophole. Some walls are **postulates**
(single-mode is a channel-counting choice) and genuinely move with more work; those OPEN
cells are the rungs. Others are **theorems** (locality/no-halo; the propagating-relic
pincer) and move only by breaking a premise — Q or locality — which does not "adapt" the
theory but **constitutes a different theory, not GRUT**. A separate move stays inside GRUT:
descending into **a deeper substrate layer of GRUT** (the bath F(t) it already posits
*beneath* the vacuum, where those theorems have no jurisdiction). That descent breaks no
premise — it is not a successor theory; F(t) is a level GRUT's own ontology already contains
(Q → F(t) → responsiveness → vacuum → physics), so giving it field content leaves Q,
locality, the vacuum sector, and the theorem-walls all intact; it is simply conjectural and
below the zero-parameter v4 core. The GRUT umbrella encompasses that
downward growth, so "complete" can *deepen* across versions; but each deliverable vN states
honestly which cells it derives, hosts, and forbids *today*. Anti-salesmanship is the point:
a spine that quietly upgrades a HOSTED or OPEN result to DERIVED is the one failure mode
that sinks the whole thing on contact with a referee, and this document refuses that upgrade
everywhere it is tempting.

### The boundary legend (five tiers)

Every emergence event below carries exactly one of these tags. They map onto the
machine-checked registry tiers in `grut/toe/registry.py`
(computed / anchored / conjectural / open_negative / foundational / meta), restated in
plain language.

| Tier | Meaning | Canonical example |
|---|---|---|
| **DERIVED** | GRUT makes it from its own structure (zero / low free parameters). | μ_linear = 1 (the projector theorem); Koide K = 2/3 as a Z₃ identity; the arrow of time from Ṡ ≥ 0; QM in the τ → 0 limit; Q, the in-in causal arrow. |
| **HOSTED** | GRUT *receives* it as a boundary condition it does **not** generate. | **Dark matter** — hosted by the locality/no-halo theorem plus the single-mode channel-counting postulate. Also the SM gauge group; τ₀ and τ_micro as anchors. |
| **FORBIDDEN-BY-THEOREM** | GRUT *rules it out* from its own axioms. | The hierarchy **magnitude**; a propagating dark relic / second vacuum pole; linear-scalar enhancement μ_linear → 4/3 (refuted at ~32σ). |
| **OPEN** | No mechanism yet, but attackable. | The α = 1/3 antecedent (the Riegert / IR-carrier identification); the D initial-state condition; baryogenesis magnitude; the Born-rule weights; the flavor mechanism. |
| **CONJECTURAL** | A structural hook only — far from derivation. | **Consciousness** — the in-in self-comparison is a hook, *not* a theory of mind. Also the black-hole interior / "1 Space"; the θ = 2/9 candidate identity. |

Several events are **split-tier seams**: the mechanism is DERIVED but its input is
anchored, or a *form* is DERIVED while its *antecedent* is OPEN. These are tagged `[SPLIT]`,
and the split is the honest content — it must not be collapsed to the higher tier.

### The through-line

One sentence the whole spine serves:

> **Responding → memory → time → vacuum → structure → observers** — a closed,
> self-referential universe in which the always-present causal arrow (Q) acquires a single
> memory channel (τ₀), and with it time, a responsive vacuum, cosmic structure, and finally
> the observers that are themselves crystallized medium — with the no-gos carried not as
> embarrassments but as the load-bearing seams that make the map complete and the boundary
> sharp.

### Section map

- **§0 — What GRUT Is** (the legend, before time)
- **§1 — Genesis** (before time → emergence of responsiveness)
- **§2 — The Primordial Universe** (the thermal transition and the primordial handles)
- **§3 — Matter** (the particle sector)
- **§4 — Gravitation & the Dark Sector**
- **§5 — Quantum Gravity & the Medium** (the boundary of GRUT's reach)
- **§6 — Observers & Self-Knowledge**
- **§7 — What Kind of ToE This Is** (closing)

---

## §0 — What GRUT Is

Before the forward story can begin, we need the legend it will be read against. This
section is not yet narrative; it is the standing description of the theory, the apparatus
that will let every later claim be tiered honestly rather than asserted.

GRUT begins from a single ontological commitment: **the gravitational vacuum is a medium
that responds, not an inert background.** A medium that responds has a response function,
and a response function has a structure — and it is from the structure, not from the
commitment, that the theory's content comes. That structure rests on three pieces of very
unequal standing, plus one dimensionless number and one anchored time.

**Pillar Q — the in-in causal arrow.** The single object GRUT is built on is the
Schwinger–Keldysh closed-time-path (CTP) action: the universe is described by *two*
copies of its own history, a forward branch φ₊ and a backward branch φ₋, and physical
response is the variation of the influence functional S_IF with respect to their
difference. Q is the set of structural facts that follow: the closed–closed propagator is
identically zero; the response when nothing has changed (S_IF on the diagonal, φ₊ = φ₋)
is exactly zero; the fluctuation–dissipation / KMS relation ties the noise N to Im χ with
N ≥ 0. Q contains no τ₀, no τ_micro, no α — it is scale-free — and it supplies a
**response-to-past, never-to-future directionality before any memory length exists.** This
is GRUT's strongest piece: a theorem of the formalism, verified on a concrete example in
all four legs (doubling invertible, variation principle reproducing the equation of
motion, retarded propagator causal, FDT recovering both classical and quantum limits). —
**DERIVED.** *(`ctp_action_structure`, tier computed; `grut/foundation/ctp_action.py`.)*

**Pillar F — finite single-pole memory.** The vacuum relaxes on *one* time τ₀ ≈ 41.9 Myr,
giving a susceptibility χ(ω) = α/(1 − iωτ₀) with a single pole at ω = −i/τ₀ in the lower
half-plane (causal, Kramers–Kronig compatible, recovering GR as ω → ∞). Equivalently, the
vacuum obeys the constitutive law τ₀ż + z = z_target. The single-pole *form* is not
arbitrary: it is the Markovian limit of a Mori–Zwanzig projection of the slow
transverse-traceless shear variable, exact to first order in τ_K/τ₀, and an off-axis
"dark-capable" pole would require τ_K > τ₀/4, which the 34-order separation forbids. But
the form being derived is not the same as the pillar being derived. **F is POSTULATED, and
the value τ₀ is anchored** — Q does not generate either. — **HOSTED `[SPLIT]`**: the *form*
is DERIVED (the MZ Markovian limit), but F as a pillar and the value of τ₀ are taken in,
not made. FDT-consistency with Q is consistency, not derivation. *(`memory_kernel_form`,
`first_order_from_mori_zwanzig`, tier computed; the postulate status per the v3 reader
edition.)*

**Bridge D — the broken dilatation redundancy.** A scale-free theory has an adiabatic
spatial-dilatation redundancy: rescaling lengths x → (1 + λ)x while holding comoving modes
fixed is the Weinberg adiabatic mode, a large/residual diffeomorphism, an exact gauge
redundancy in the L₀ → 0 limit. The arrival of a finite memory time gives the vacuum
exactly one proper length, L₀ = cτ₀ ≈ 12.85 Mpc, and a fixed proper length is logically
incompatible with that redundancy. Responsiveness *is* the controlled, non-anomalous
breaking of D by this single scale: (L₀ k_phys)² is no longer dilatation-invariant, the
breaking enters at O((L₀ k_phys)²), it is a diffeomorphism (not a Weyl rescaling, so α
does not enter), and it is confined to the tensor sector — which is exactly why linear
scalar cosmology is left untouched (μ_linear = 1, below). The breaking term is rigorously
computed and the Keldysh-doubling content proven; what is *presupposed* is the underlying
L₀ → 0 redundancy itself, imported from Weinberg rather than re-derived, with one
undischarged residue (whether the in-in initial state is separate-universe invariant — the
scale-free / n_s = 1 condition, GAP-1). — **OPEN `[SPLIT]`**: breaking DERIVED, redundancy
PRESUPPOSED, initial-state residue OPEN. A pure redundancy cannot be spontaneously broken;
what L₀ breaks is its *boundary charge*. *(`adiabatic_dilatation_redundancy_nogo`, tier
computed; `organizing_structure_v3`, foundational.)*

**The one number and the one time.** From the synthesis — GR's redundant limit *plus* the
controlled breaking of D by L₀ — the gravitational core derives its outputs from just two
inputs. The first is the dimensionless axiom **α = 1/3**, adopted as c and ℏ are adopted.
It fixes the deep-IR refractive index R = √(4/3) = 1.1547, the screening factor
S = 12π/α² = 108π = 339.29, and the normalization of the response. A *conditional* theorem
is verified Fraction-exact: if the gravitational conformal mode is the IR carrier, then the
trace-anomaly ratio a/c = 1/3 (Duff; Komargodski–Schwimmer). But the antecedent is
unproven and the value is adopted. — **OPEN `[SPLIT]`**: value ADOPTED, conditional math
verified, antecedent OPEN. *(`alpha_vac_axiom`, foundational; `alpha_vac_derivation`,
open_negative — the most load-bearing open gap.)* The second input is the anchored time
**τ₀ ≈ 41.9 Myr**, cross-checked by cluster-merger offsets, and a second anchored scale
**τ_micro ≈ 1.4 × 10⁻¹⁹ s** in the thermal sector. The gravitational core has *zero free
parameters given {α, τ₀}*; the framework as a whole is a two-anchored-scale theory, never
globally one-parameter. — **HOSTED.** *(`tau_0_derivation`, `zero_free_parameters`,
computed; `tau_0_cross_consistency`, anchored.)*

**What the core then makes.** From {α, τ₀} the core yields R = √(4/3), a dark-energy
fraction Ω_Λ, a Hubble rate H₀ ≈ 68.8 km/s/Mpc sitting in the tension gap, and one
genuinely robust theorem: **μ_linear = 1** — linear cosmology *is* exactly ΛCDM, forced two
independent ways and over-determined by data. — **DERIVED `[SPLIT]`** for the theorem;
the Ω_Λ and H₀ *numbers* are derived-given-anchored-τ₀ and the registry tiers them
*anchored*. Standard physics is recovered, not re-postulated: quantum mechanics as the
τ → 0 limit of the constitutive law, the arrow of time as constitutive entropy production
Ṡ ≥ 0, GR at high frequency, and the Standard Model passing five CTP-derived structural
constraints. — **DERIVED**, with one honesty flag: the SM passing C1–C5 is *consistency*,
not *uniqueness*; "the SM falls out" would be an overclaim.

And the seams are already visible at this rung, before the story has even begun. **Dark
matter is HOSTED** — received, not derived, by the locality/no-halo and single-mode
theorems. **A propagating dark relic and the hierarchy magnitude are FORBIDDEN-by-theorem**
— and, as §5 will show, for the *same* reason. **The α-antecedent is OPEN**, τ₀ is
anchored, and **consciousness is at most a CONJECTURAL hook.** None of this is hidden; all
of it is machine-checked. The honesty is itself an artifact: a 121-claim registry where
every claim carries a tier, code references, tests, and a single falsifier; a passing test
suite (over 3,000 tests gating every computed claim) plus an open-question ledger recording
what would close each gap. A claim
advances a tier only when a test certifies it; a failed result is demoted and logged,
never quietly dropped. — **DERIVED** (the meta-layer that makes the tiering auditable
rather than asserted). *(`grut/toe/registry.py`; `grut/toe/ledger.py`.)*

That is the legend. Now the universe runs forward.

---

## §1 — Genesis (before time → emergence of responsiveness)

Run the clock backward as far as it will go, and you do not arrive at nothing. You arrive
at **Q without F** — a medium that already responds to realized differences, with the
causal arrow already pointing from past to future, but with no memory, no characteristic
length, and therefore no time in the sense of a clock the universe sets for itself. This is
the deepest positive result in the entire framework, and it is the keystone of the layered
ontology: **across every backward crossing, Q is the one thing that survives the loss of
memory.** It contains no τ₀, no τ_micro, no α; it is the floor everything else rides on. The
arrow of time does not emerge *with* responsiveness — it *predates* it. — **DERIVED.**
*(`GRUT_GENESIS.md` §2(i), §5; `ctp_action_structure`, computed; the MZ and pole-spectrum
verify harnesses pass.)*

Now let the universe cool. Above a critical temperature T_c the prospective slow shear
variable z is *not* slow relative to its own microscopic bath — k_BT ≳ ℏ/τ_micro, so there
is no slow/fast separation for a Mori–Zwanzig projection to act on, and no memory. As the
temperature falls through T_c, that separation opens, and one relaxation channel — the
single transverse-traceless shear mode, the one locked to the conserved stress-energy
(∂_μ T^μν = 0 being the diffeomorphism Ward identity, part of Q) — fails to equilibrate.
**Memory condenses as the un-rejected remainder**: the MZ projection of that surviving slow
channel yields the first-order, history-retaining response χ = 1/(1 − iωτ₀) as its
Markovian limit. The *existence* and the *slow, gapless character* of this channel are
forced, without tuning, by conservation. — **DERIVED `[SPLIT]`**: the existence and
character are forced; the finite-temperature MZ calculation that would rigorously prove
memory turns *off* again above T_c is asserted via the τ_K < τ₀/4 threshold, not yet
computed — and the forward story uses the temperature law f(T) as a proxy for that
uncomputed dynamics. *(`memory_kernel_form`, computed; `GRUT_GENESIS.md` §2(iii), §8.1,
§9.)*

How fast does memory switch on? Not by an imported sigmoid with a free width, but by
GRUT's own noise ratio. Splitting Q's FDT/KMS relation into its zero-point and thermal
parts gives a coherent fraction of the bath fluctuation, and that fraction *is* the
order parameter: **f(T) = tanh(T_c/2T)**, and composing with radiation-era cooling
T(t) = T_c (t_c/t)^½ gives the explicit forward switch-on profile
z̄(t) = tanh[½ (t/t_c)^½]. This is the headline new v4 result — the thing the older
backward catalog never wrote. Notice it does *not* equal a clean ½ at T_c: f(T_c) =
tanh(½) = 0.4621, with a power-law 1/T high-temperature tail rather than an exponential
one. — **DERIVED `[SPLIT]`**: the shape and limits follow from Q's FDT/KMS structure given
*one physical identification* (memory-activation = the bath's zero-point fraction at the
single τ_micro scale). It trades the old sigmoid's free width for a motivated
identification — an improvement, *not* a parameter-free theorem; the complement 1 − tanh
or a τ-ratio T_c/2πT are a-priori alternatives. One caveat must be kept sharp: it is the
memory-*amplitude* order parameter f(T) that is derived this way from FDT/KMS; the elastic
*rigidity* onset shape — the G₀ that turns on at T_c in v4's solid candidate — is, per
`GRUT_V4_ELASTIC_VACUUM.md` §7, *still* an ad-hoc sigmoid pending the finite-temperature MZ
calculation. The "{F, D-breaking, G₀} share one order parameter" claim of the elastic
program is therefore an aspiration on the rigidity leg, not yet a derivation. *(`GRUT_GENESIS.md` §8.1, §8.6;
`thermal_transition.py`.)*

And here the theory corrects itself, which is exactly the discipline the spine is built to
honor. The older catalog called this onset a "phase transition." The forward analysis
demotes it. The pole *amplitude* f(T) is C∞-analytic straight through T_c — no critical
onset, no diverging susceptibility, no latent heat — so by Landau's analyticity criterion
it is a **smooth crossover, not a second-order transition.** There *is* a sharp
bifurcation in the underlying physics — the pole-*existence* boundary at τ_K = τ₀/4 — but
it sits roughly 34 orders of magnitude away (τ_K(T_c)/(τ₀/4) ≈ 7 × 10⁻³⁵), structurally
pre-satisfied and never reached in cosmic history. Emergence is a phase transition *only*
in the spontaneous-scale-symmetry-breaking sense, L₀ : 0 → finite — executed as an analytic
amplitude crossover, and decidedly not as Darwinian selection or a critical quench. —
**DERIVED.** *(`GRUT_GENESIS.md` §8.2, §8.6.)*

The same condensation that gives z its amplitude gives it a finite memory time τ₀, and
therefore exactly one proper length, **L₀ = cτ₀ ≈ 12.85 Mpc.** "Capable of memory" and
"scale-free" are now mutually exclusive: the appearance of L₀ breaks the boundary charge of
the dilatation redundancy D at O((L₀ k)²), non-anomalously (4 ∉ {2, 6, 10, 14}), with a
measure Jacobian identically one (so α does not enter). The decisive falsifier — that the
Keldysh doubling might secretly spoil the redundancy — is discharged: T_λ acts diagonally
on the ± branches, |J|² = 1, and the influence functional collapses to two decoupled
diffeomorphism-invariant GR copies as L₀ → 0. — **DERIVED `[SPLIT]`**: dynamics and measure
DERIVED; the initial state is theorem-modulo GAP-1 (the in-in state must be spatially
homogeneous and scale-free, the standard adiabatic / cosmological-principle condition),
whose floor is the field-wide cosmological measure problem — shared by all of cosmology,
not specific to GRUT. One notch short of "forced from Q." *(`GRUT_GENESIS.md` §8.4, §7;
`GRUT_V3_ORGANIZING_STRUCTURE.md` Bridge D.)*

Two things are carried *through* genesis rather than made by it, and the story must say so
plainly. The first is τ₀'s **numerical value** — the 34-order hierarchy. It arrives as an
unexplained anchor and stays one: no combination of {ℏ, k_B, c, G} has units of time², the
numerology cross-checks fail, and the §9 keystone forces the gap to be *large* (the MZ
projection's own validity needs τ₀ ≫ τ_micro) and forces *why one channel fails to
equilibrate* — but it does not force the *size*. The size, ln(τ₀/τ_micro) = 78.23,
relocates verbatim into L₀ and remains anchored (the two Planck-logs are differenced before
rounding; see Appendix B). — **FORBIDDEN-BY-THEOREM** (magnitude)
**+ OPEN** (antecedent). This is the one fact that sinks the spine if it is ever inflated.
*(`GRUT_GENESIS.md` §2, §9; `GRUT_HIERARCHY_LEDGER.md`.)* The second is the **α = 1/3
spine** (S = 108π, R = √(4/3), Ω_Λ = (2 − R)²): a dimensionless anomaly-sector relic,
orthogonal to the dilatation sector, frozen *before* responsiveness and inherited by the
GRUT phase rather than generated by it. — **DERIVED `[SPLIT]`**: everything downstream of α
is derived; the derivation *of* α is OPEN. *(`alpha_vac_axiom`, foundational;
`screening_108pi`, computed.)*

Of everything the genesis leaves behind, exactly one relic is already observed.
**Dark energy is the Herglotz spectral weight of the single pole, tied to τ₀.** It switches
on adiabatically as ωτ₀ drops through 1 over the whole subsequent expansion, with no
localizable transition epoch — the only downstream fingerprint of the genesis itself. The
identification is the load-bearing claim; the precise number carries the anchored caveat
(the raw relation gives (2 − R)² = 0.7145; the full-Friedmann anchored value is 0.6886 —
two different numbers, never conflated). — **DERIVED** (the emergence) / *anchored* (the
value). *(`GRUT_GENESIS.md` §3, §4; `omega_lambda_prediction`, anchored.)*

Then the blind test — and the honest negative that defines the boundary. Run the relic
inventory forward *without* biasing it toward producing dark matter, and ask whether viable
cold dark matter falls out. It does not. The single-mode structure forbids a second stable
*relaxational* pole — itself a channel-counting postulate (single- vs multi-channel), not a
consequence of Q alone, the seam laid bare in §4/§5; the one condensation-tied relic — an
elastic shear phonon at 4.71 keV — is *warm*,
travels at c_s = c, and overcloses the universe by a factor of several hundred to several
thousand. GRUT does not predict *no* dark matter; it predicts the *wrong* dark matter, and
reports that as a genuine negative. **Dark matter is HOSTED.** — **HOSTED.**
*(`GRUT_GENESIS.md` §3, §4; `locality_no_halo_theorem`, computed.)* Ordinary survivors
ride through unremarkably: the observed baryon asymmetry η_B ≈ 6.1 × 10⁻¹⁰ (Planck) is a
frozen global-charge number whose genesis *mechanism* is OPEN (GRUT's own route lands
+7.7% high; see §2), and BBN completes entirely in the pre-responsive
local-GR era (which is *why* GRUT predicts no refractive enhancement at nucleosynthesis);
the massless TT graviton is substrate, present across all crossings, not produced. —
**HOSTED / OPEN.** And at the very bottom, beneath the vacuum itself, lies the microscopic
KMS bath F(t): the only place a genuine cold relic — or any consciousness hook — could
attach, and the one entry that would require detailing GRUT's own **substrate sector** — the
microscopic medium beneath the vacuum that current GRUT posits but does not yet specify. — **CONJECTURAL / OPEN.** This is the outer edge of
the map: *beyond here, current GRUT posits a deeper layer but does not yet detail it* — the
substrate sector, not a different theory.

---

## §2 — The Primordial Universe

The universe is now hot, expanding, and — critically — too hot to remember. Epoch 2 is the
story of one phase boundary and the handful of primordial numbers attached to it.

The boundary is the moment the responsive vacuum cools through **T_c ≈ 54.7 MK** — the
"boiling point of gravity," reached at roughly 16.5 hours after the Big Bang. Above T_c the
metric responds locally, with no memory and no refractive enhancement: standard GR. Below
it, the single-pole kernel activates and gravity becomes bandwidth-limited, with the
refractive index running to n_g → R = √(4/3) at DC. Today, at 2.725 K, the universe sits
far below T_c, deep in the refractive regime. The transition *exists* and forces its
consequence — and that is the derived content. Its *value*, however, is not GRUT-internal:
T_c is fixed empirically by the standard cosmological-chronology pin. — **DERIVED `[SPLIT]`**:
the transition and the n_g = R consequence are derived; the value is anchored.
*(`t_c_thermal_transition`, computed; `grut/derived/cosmology/thermal_transition.py`.)*

And τ_micro is T_c in disguise. The genuinely independent number is the empirical thermal
anchor **T_c ≈ 54.7 MK** (fixed by the standard cosmological-chronology pin), from which the
microscopic relaxation time **τ_micro = ℏ/(k_B·T_c) ≈ 1.4 × 10⁻¹⁹ s** is derived through the
ℏ ↔ k_B·time correspondence; τ_micro is the microscopic *expression* of T_c, separated from
the gravitational τ₀ by 34 orders of magnitude. **This T_c / τ_micro scale is the *second* of
the theory's two independent anchors** — and this is where the two-anchor seam of the entire
framework shows through the narrative. There is no closure path from it to τ₀: the magnitude
that separates them
cannot be derived, and (as §5 makes structural) the two-anchor split is *protected* by
GRUT's own locality + Q, because closing it would require a forbidden new propagating pole.
— **HOSTED** (with a FORBIDDEN relation to τ₀). *(`tau_micro_thermal_scale`, registry tier
conjectural; reported here as hosted-with-forbidden-magnitude — the load-bearing seam of
the epoch.)*

The transition does not snap; it crosses over. The activation profile
**f(T) = tanh(T_c/2T)** — the same order parameter introduced in genesis — smoothly switches
memory on as the universe cools: f(T_c) ≈ 0.462, f → 1 deep below T_c, and a 1/T power-law
tail above. Its shape and limits are forced by Q's FDT/KMS structure given the one physical
identification (activation = the bath's zero-point fraction). — **DERIVED `[SPLIT]`**, with
the same caveat as in genesis: motivated identification, not a fully parameter-free theorem.
*(`grut/derived/cosmology/thermal_transition.py`.)*

That profile does useful work immediately: it protects BBN. At the nucleosynthesis era
(T ≈ 18 T_c) the f(T) tail leaves only ~2.7% residual activation, *and* the physical memory
effect is bandwidth-suppressed because BBN-era dynamics have ωτ₀ ≫ 1 — so n_g → 1 exactly,
and GRUT predicts no dark-matter-like refractive signature at nucleosynthesis. This is a
falsifiable *no-effect* prediction. The honest framing is precise: GRUT does not compute BBN
abundances; it borrows standard BBN and shows that its own correction *vanishes* there — a
derived null, not a derived BBN. — **DERIVED** (a null).
*(`grut/derived/cosmology/thermal_transition.py`.)*

The two quantitative primordial handles of standard cosmology fare oppositely.

**Baryogenesis** is derived at the level of *existence*. The CTP path is asymmetric (the
canonical ratio R ≠ 1), and a nonzero baryon-to-photon ratio is forced by that asymmetry —
it would vanish identically at R = 1. The structural factor (2 − R_B)/S_B, multiplied by
external Standard-Model inputs, lands η_B ≈ 6.57 × 10⁻¹⁰, about +7.7% from the Planck value.
But only the (2 − R_B)/S_B factor is native; the Jarlskog J_CP and the electroweak
nonequilibrium factor K_neq are hosted SM inputs. — **DERIVED `[SPLIT]`**: existence derived
(the Sakharov-CP content), magnitude assisted by hosted inputs — the 7.7% agreement must not
be read as zero-parameter. *(`baryogenesis_eta_b`, computed.)*

The primordial **scalar amplitude A_s ≈ 2.1 × 10⁻⁹** is the honest negative of the epoch.
GRUT has no inflationary epoch, and all three computational paths fail badly: an
Ornstein–Uhlenbeck variance from the KMS noise kernel misses by ~10¹⁰, a naive inflationary
substitution by ~10¹⁰⁹, and the closest dimensional candidate α/S³ ≈ 8.5 × 10⁻⁹ sits a
factor of four away and is flagged a *clue*, not promoted (one near-miss among eleven
candidates is plausible chance). A_s is observation-anchored input. — **OPEN.** A theory of
everything that does not make A_s, and says so, is doing exactly what the charter requires.
*(`primordial_amplitude_zero_parameter_open_negative`, open_negative.)*

The spectral **tilt n_s ≈ 0.965** is weaker still. GRUT offers a constitutive-dissipation
form, n_s = 1 − 2(Hτ)²/(1 + (Hτ)²), which can match Planck — but only by solving for Hτ from
the *observed* n_s. The agreement is a fit, not a prediction, and the source tags it
[HYPOTHESIS] accordingly. The genuine forward content is the *running* dn_s/dln k, which
differs from slow-roll and is CMB-S4-falsifiable — though it too currently leans on a
phenomenological input. — **CONJECTURAL.** *(`grut/derived/cosmology/spectral_running.py`.)*

So the epoch's verdict: one derived phase transition (existence forced, value anchored to
the second hierarchy pin), one existence-derived asymmetry, and two observation-anchored
numbers the framework does not generate. The seams are exactly where a referee would push,
and they are placed in the open.

---

## §3 — Matter (the particle sector)

This is where GRUT's ToE-as-a-map posture is sharpest, because the matter sector is mostly
**HOSTED** — and the spine must say so without flinching. Once a responsive vacuum with
finite memory exists, the universe has to be populated with matter, and GRUT *receives* that
content rather than generating it.

The Standard Model is checked against five CTP-derived structural constraints, C1 through
C5, and it passes all five. But the registry is explicit and the spine honors it: passing
is *necessary, not sufficient*; the "unique minimal theory" claim is not established. So the
**gauge group SU(3) × SU(2) × U(1)** (C1: 8 + 3 + 1 = 12 gauge bosons) is a consistency
check GRUT verifies, not a selection it forces. — **HOSTED.** The **anomaly cancellation**
(C2: ΣY² = 10, the 1-loop β = 20/3, ΣY³ = 0, ΣY = 0) is a property of the *received*
hypercharge assignments; GRUT verifies that the arithmetic is exact and self-consistent, and
this matters downstream because the same field content fixes the trace-anomaly numerators
that feed cosmology. — **HOSTED.** The **three generations** (C3: 15 Weyl fermions ×3 = 45)
are verified as a count. — **HOSTED `[SPLIT]`**, with a correction the spine must make
loudly: the in-code rationale that "N = 3 is the unique integer for which the Koide ratio is
phase-independent" is *false as stated*. The Koide ratio K = 2/N is phase-independent for
*all* N ≥ 3 (N = 3 → 2/3, N = 4 → ½, N = 5 → 2/5, …); N = 3 is selected only by additionally
matching the *empirical* charged-lepton value 2/3. (A *second* in-code route —
`grut/derivation/task01_n_generation_under_epsilon.py:139-222`, claiming "N = 3 is uniquely
selected by Ω_Λ within Planck 2σ" — does not lift the tier either: it is not a registered
registry claim, it is a-posteriori membership in a 2σ band rather than a forcing, and it
presupposes the SM field content R_ψ that is itself HOSTED.) The generation count is therefore
HOSTED, not θ-independently derived — and presenting it otherwise is precisely the salesmanship
trap the spine exists to avoid. *(`sm_emergence`, computed; `sm_field_content_locked`, computed.)*

Where GRUT *does* pay off in this sector, it pays off downstream. Given the hosted field
content, the 1-loop **trace-anomaly numerators are exact rationals**: a = 1991/2 (in both
Duff and KS conventions) and c_KS = 849, both reproduced in `.venv`. These are load-bearing
— they feed Path D → R = √(4/3) and the −100 drive, so the matter sector hands cosmology a
*rigid number, not a fit*. The honest framing is layered: the field content is HOSTED, but
the anomaly coefficients computed from it are DERIVED. — **DERIVED `[SPLIT]`**.
*(`sm_field_content_locked`, computed; `grut/foundation/conformal_mode_scalar.py`.)*

Within flavor, the genuine derivations are narrow and algebraic. The **Koide relation
K = 2/3** for the charged leptons holds at machine precision as an algebraic *identity* of a
Z₃-circulant mass operator, for any overall scale M₀ and any phase θ. — **DERIVED `[SPLIT]`**:
the identity is the honest claim and it holds; but the Z₃ circulant is a *parameterization*
(M₀ and θ are fitted to the masses), and what physically realizes the Z₃ structure in the
CTP action is OPEN. "K = 2/3 is a theorem of Z₃" is derived; "GRUT forces Z₃" is not.
*(`koide_z3_circulant_structure`, computed.)* The remaining flavor phase, **θ = 2/9**, is
matched by K·α_vac = (2/3)(1/3) at 4.62 ppm, and a rational scan confirms 2/9 is the unique
best approximant (the nearest competitor is hundreds of times worse, ruling out numerology).
But no algebraic derivation from the CTP action exists. — **CONJECTURAL**: a *candidate
identity* that ties the flavor phase to the already-adopted α, falsifiable by a ≤10 ppm
τ-mass measurement; the scan is computed, the mechanism is absent. (The registry tier-field
reads `computed` for the uniqueness *scan*; the algebraic-mechanism tier is OPEN, so the
spine books the overall claim CONJECTURAL / candidate-identity — above hypothesis, below
derived.) *(`koide_theta_2_over_9_uniqueness`, tier computed for the scan.)*

The neutrino subsector carries the epoch's live falsifiers. GRUT **prefers Dirac over
Majorana** neutrinos — Path D Dirac gives a/c = 1.15525, closer to the canonical √(4/3) =
1.15470 than Majorana's 1.17256 — but this is a closeness *preference*, not a proof, and a
positive neutrinoless-double-beta-decay signal would sink it and the chain that rests on it.
— **OPEN.** *(`neutrino_dirac_prediction`, anchored.)* Sharper still: the charged-lepton Z₃
structure provably does **not** extend to neutrinos. The same a = √2 ansatz that gives
K = 2/3 forces a mass-splitting ratio Δm²_atm/Δm²_sol ≥ 194.7, against the observed 33.9 — a
factor of six too large, computed and unconditional. Neutrinos require a distinct
mechanism (K_ν = ½, a_ν = 1). — **FORBIDDEN-BY-COMPUTATION**, and this is a virtue, not a
gap: the no-go *is* the physics, the layered ontology showing as an internal wall.
*(`charged_lepton_z3_does_not_extend_to_neutrinos`, computed.)* Conditional on the
structural value a_ν = 1, the generalized ansatz then admits a unique normal-hierarchy
interior solution — Σm_ν ≈ 60 meV, with the inverted hierarchy sitting at a degenerate,
fine-tuned boundary — so GRUT **prefers normal ordering**, with m_β ≈ 9 meV within Project 8
reach and Σm_ν comfortably below the Planck+BAO bound. — **OPEN `[SPLIT]`**: the NH
preference and Σm_ν are derived *from* a_ν = 1, and a_ν = 1 is itself structurally DERIVED as
the unique boundary-degenerate Z₃ coupling (Correction #29 —
`neutrino_z3_coupling_a_equals_1_uniqueness_theorem`, computed; it is no longer a postulate);
what remains OPEN is only the deeper channel-counting / KS-anomaly account of *why* neutrinos
lack the EM channel. (The hierarchy claim's registry tier field reads "computed" while its
notes read "anchored" — a tension flagged here, not papered over.) It is a live falsifier: JUNO/DUNE
confirming IH, or DESI/Euclid pushing Σm_ν out of band, kills it.
*(`neutrino_hierarchy_z3_nh_prediction`.)*

Under all of it sits the honest floor: **the flavor mechanism — what physically selects
(M₀, θ) and the Z₃ structure from the CTP fixed point — is OPEN.** Everything derived in
this sector rests on an *assumed* Z₃ circulant whose emergence has not been shown. This is
the matter sector's principal open frontier, and stating it plainly is what keeps K = 2/3
honestly at "derived identity" rather than "derived mechanism." — **OPEN.**
*(`koide_phase_4_open_negative`, open_negative.)*

The headline for Epoch 3: GRUT does not derive the particle list. It has a sharp, tiered
place for every piece of it, computes the anomaly numbers that bridge to cosmology, derives
K = 2/3 as an identity, and stakes falsifiable neutrino predictions — with the flavor
mechanism as its named open frontier.

---

## §4 — Gravitation & the Dark Sector

Here the layered ontology is most exposed, and the discipline of honest tiering matters
most. There is one clean derived win, one sharp laboratory falsifier, and three seams.

The win is **dark energy as a terminal velocity.** Empty spacetime has a negative-energy
conformal (Gibbons–Hawking) mode that drives runaway expansion; the vacuum's finite-memory
kernel has a dissipative part that opposes rapid change. The two balance at a constant rate,
exactly a terminal velocity: H_inf = (2 − R)/(S·τ₀), with the drive (2 − R) being
conformal-mode physics and the friction 1/(S·τ₀) the screened constitutive relaxation. The
cosmological constant is then not a tuned vacuum energy but a balance, and Ω_Λ = (H_inf/H₀)²
follows with zero free parameters in the conversion. — **DERIVED `[SPLIT]`**: the mechanism
and structure are derived; the *number* is anchored through τ₀.
*(`h_inf_decomposition`, computed.)* And the number must be stated carefully, because this
is a place the narrative could tempt an upgrade. The full-Friedmann treatment with anchored
τ₀ gives **Ω_Λ = 0.6886** (Planck: 0.6889, a 0.04% match). The tree-level closed form
(2 − R)² ≈ 0.7145 uses a cosmic-baseline approximation. **These are two different numbers** —
conflating them, or calling 0.6886 "derived from (2 − R)²," would be exactly the kind of
over-claim that sinks the spine. — **HOSTED** (anchored). *(`omega_lambda_prediction`,
anchored.)*

The same τ₀ surfaces as the framework's **sharpest near-term falsifier**: the
gravitational-decoherence plateau. For a gold microsphere of radius 1 μm (mass ≈ 80.8 pg —
the in-code benchmark docstring at `grut/derived/decoherence/alternative_models.py:20,119`
reads "80.8 fg," a units typo: a 1 μm-radius gold sphere at 19,300 kg/m³ is 80.8 *pico*grams,
not femtograms),
GRUT computes a decoherence frequency of **689 Hz** from {G, ℏ, c, τ₀} with zero free
parameters, with coherence destroyed in ~1.5 ms. Because the same τ₀ fixes Ω_Λ through the
terminal-velocity relation, a tabletop measurement of where decoherence saturates pins both
the memory scale and the dark-energy fraction at once. — **DERIVED.** The seam is that 689 Hz
is a *predicted test point*, not an anchor — it inherits τ₀'s anchoring, so measuring the
plateau is a way of *measuring* τ₀. *(`decoherence_plateau`, computed.)*

And the same memory length that produces those signatures must also leave the Solar System
untouched, or the theory is dead on arrival — so its safety there is a derived win, not an
assumption. Because the refractive enhancement is bandwidth-suppressed, α_eff(ω) =
α/(1 + (ωτ₀)²) is far below measurement precision everywhere ωτ₀ ≫ 1 holds, which is the
entire Solar-System regime: GRUT passes eight independent precision tests of GR spanning >10
orders of magnitude in frequency — Saturn ranging, Mercury perihelion, lunar laser ranging,
GPS, the Hulse–Taylor pulsar, the Cassini Shapiro delay, LIGO propagation, Earth ranging —
with safety factors from 2.3 × 10⁵ (Saturn) to 1.5 × 10³⁵ (LIGO), median ~10¹⁶, n_g → 1 by
the same bandwidth gate that switches off memory at high frequency. — **DERIVED.**
*(`solar_system_safety`, computed.)*

Now the three seams.

**Linear modified gravity is FORBIDDEN — and dead twice over.** In the linear scalar sector
the tracefree transverse projector annihilates the constitutive response, so μ_linear = 1
exactly: linear cosmology is ΛCDM, with γ = 1 and no gravitational slip. Any enhanced-growth
branch (μ ≠ 1, the old "refractive" modification) is forbidden by separate-universe /
adiabatic-dilatation invariance *and* independently killed at ~32σ by the low-ℓ CMB ISW
excess. A whole family of v2 "predictions" — enhanced growth, a linear dielectric dark
sector with Ω_dm = α — is now audit-trail-only, recorded as dead. — **FORBIDDEN-BY-THEOREM.**
This is anti-salesmanship operating on the theory's own former flagships.
*(`adiabatic_dilatation_redundancy_nogo`, computed.)*

**Dark matter is HOSTED, and the reason is a theorem.** The Spectrum Program reduced the
entire dark-matter question to a single sharp one — is the responsive vacuum single-mode or
multi-mode? — and answered, via a 12,800-pole scan, *single-mode*: coupled relaxational
variables never give a stable off-axis dark-capable pole. Single-mode is not, however, a
theorem from Q alone: it is itself one binary channel-counting postulate (single- vs
multi-channel), and the scan covered only *relaxational* variables — so the seam is fully
exposed, *dark matter is HOSTED because single-mode is postulated*, not forced. So within the
single-variable F-reduction, dark matter is hosted permanently. The mechanism that justifies the hosting is
the **locality / no-halo theorem**: any GRUT dark-sector response that is covariant, local
in the matter fields (analytic and pole-free in k² near k = 0, as a causal local memory
kernel must be), and nonlinear yields an effective source no more spatially extended than
its baryons. An extended ρ ∝ 1/r² halo has a k = 0 singularity that requires a 1/k² pole — an
inverse-Laplacian 1/∇² — which locality forbids. (MOND is the illuminating case: it gets the
1/r² phantom precisely by responding to that forbidden nonlocal term.) The explicit Weyl²
channel has roughly the right *magnitude* but a too-steep 1/r⁴ → 1/r⁶ profile. — **HOSTED**
(the input) / **FORBIDDEN-BY-THEOREM** (the halo). "GR never predicted the electron"; a
single-pole spectrum that makes dark matter a permanent hosted input is a respectable,
falsifiable endpoint, not a failure. *(`vacuum_spectrum_pole_classification`,
`locality_no_halo_theorem`, computed.)* And one level deeper, a *propagating* dark relic — a
stable pole atop the massless graviton, built from the vacuum's own action — is forbidden by
an Ostrogradsky + Q pincer: it needs a higher-derivative TT operator whose ghost gives a
wrong-sign residue, Im χ < 0, hence noise N < 0 by FDT, hence a violation of Q. Every escape
requires *imported* structure GRUT's one-metric CTP action does not contain. —
**FORBIDDEN-BY-THEOREM** (registry-tiered conjectural = *theorem-modulo-gap* on the static
face — no in-repo Boulware–Deser analysis of a fully general covariant completion exists —
computed on the Mori–Zwanzig dynamical face). *(`propagating_relic_forbidden_pincer`,
conjectural.)*

**MOND is half-derived.** The trigger acceleration **a₀ = c/(2π τ_Λ) = cH₀/(2π) ≈
1.06 × 10⁻¹⁰ m/s²** emerges from the cosmological response time and lands in the MOND band,
and the high-frequency gate *form* 1/(1 + (ωτ₀)²) follows from χ(ω). But the controlling
frequency ω_dyn = v/r is *assumed* (extrapolated from the cosmological DC response, not
CTP-derived for bound systems), the interpolation function ν(y) is *adopted* from MOND, and
the rotation-curve *mechanism* is refuted: after the no-go removes the linear-scalar mean
field, the realized structure varying at ω_dyn is only granular, ~1/√N (≈10⁻⁶ for a galaxy),
so the gate acts on a negligible source. — **OPEN `[SPLIT]`**: the a₀ scale and gate form are
derived; the interpolation function is adopted and the mechanism refuted. GRUT is
MOND-*compatible* with a derived a₀, not a derivation of MOND. *(`mond_a_0_emergence`,
computed-with-flags.)*

Finally, the conjectural frontier. Inside a black hole, the matter-bearing interior's Ricci
scalar saturates at R_max = α_vac/(c²τ₀²), bounding *interior trace* curvature only (the
Schwarzschild vacuum exterior has R = 0 identically and is unconstrained), and every core
saturates at the same mass-independent density ρ_max ≈ 1.1 × 10⁻²² kg/m³ — the saturated,
fully-crystallized end-state interpreted as "1 Space." — **CONJECTURAL**: ρ_max is a flagged
open numerical problem (it sits below naive interior densities), only 4 of 8 nonlinear-GR
rungs are closed, and "1 Space" is explicitly interpretive. Listed for narrative
completeness; not presented as derived. *(`r_max_ricci_saturation`, `one_space_endpoint`,
conjectural.)*

Epoch 4 reads as a ToE not by deriving the dark sector but by having a sharp, tiered place
for every part of it: one derivation (Λ), one falsifier (689 Hz), one forbidden family
(linear MG), one hosted input justified by theorem (dark matter), one mixed scale (a₀), one
conjectural frontier (BH interiors). The seams are the story.

---

## §5 — Quantum Gravity & the Medium (the boundary of GRUT's reach)

This is the rung where the forward narrative meets the edge of what GRUT can make from
itself, and the honest content of the epoch is mostly that edge, drawn sharply. The question
beneath the question is whether there is a deeper engine — a UV-complete dynamical sector —
that would *fix* the scales rather than merely host them. GRUT's answer is a layered no, with
one genuine derived win along the way.

**The medium: one derived number, then a refutation.** v3 used only the *viscous* half of
the viscoelastic vacuum (the single-pole Maxwell-fluid memory). v4 activates the *elastic*
half: if the vacuum is a viscoelastic *solid* with static shear rigidity G₀ > 0, then the
Debye / Kleinert world-crystal identity — one energy quantum ℏ/τ_micro per cell of spacing
ℓ_micro = cτ_micro — *forces* G₀ = ℏ/(c³ τ_micro⁴) ≈ 1.03 × 10¹⁶ Pa from {ℏ, c, τ_micro} with
no dial. That is a real, mechanism-backed number, not numerology. — **DERIVED `[SPLIT]`**,
and demoted on two counts. First, the solid is not forced: v3's memory is a Maxwell *fluid*
(static TT shear → 0), so the solid is one of at least four degenerate medium classes and
G₀ > 0 is an *unpaid postulate*; the v4 elastic-vacuum document is explicitly a candidate
within the founding charter, not the settled thesis. Second, the same forced G₀ predicts the
*wrong* dark sector: c_s = c exactly (a stiff relativistic solid with no slow phonon), a warm
4.71 keV gap at the Lyman-α floor, and overclosure by ~400–5800×. — **FORBIDDEN-BY-THEOREM**
(as a viable cold-DM derivation): GRUT contains exactly two transition scales (warm at
τ_micro, fuzzy at τ₀) at opposite ends of the 34-order gap, and a cold clustering relic would
have to live strictly *inside* the empty gap GRUT does not populate. It is banked as a
derived-but-refuted prediction — more scientific than a free dial, and a confirmation of the
hosting boundary rather than a crossing of it. *(`GRUT_V4_ELASTIC_VACUUM.md` §§2–3, 7.)*

**The conformal mode σ fails to close.** The natural quantum-gravity carrier — the
gravitational conformal mode σ — is the obvious substrate for both α = 1/3 and any UV
engine. GRUT computes the anomaly ratio a/c = 1/3 (Komargodski–Schwimmer, Fraction-exact),
but σ is fourth-order (Riegert/Paneitz), and *that* closure is OPEN: the in-repo module is a
ratio calculator with the anomaly coefficients but no σ field, no potential V(σ), no
propagator, no running coupling. α = 1/3 is a conditional theorem *if* the conformal mode is
the IR carrier — an antecedent that is unproven. — **OPEN.** This is the single most
load-bearing open gap in the framework, because cosmology is α-sensitive (a ±0.07 shift moves
Ω_Λ by about an order). The conditional math survives; the "derived" ontology does not.
*(`alpha_vac_derivation`, open_negative.)*

**Deriving the hierarchy magnitude is currently not even askable.** A
Coleman–Weinberg / dimensional-transmutation derivation of ln(τ_micro/t_P) = 56.21 would
need three dynamical ingredients — a condensing scale-invariant potential, a GRUT-origin
running coupling, and a Planck-scale boundary condition — and GRUT has none of them. It
*has* the right-magnitude coefficient (the normalized anomaly is the right size to source a
50–100 Planck-log), but the loop factor always cancels into the dimensionless a/c ratio and
there is no β-function to run it. The missing ingredient is the *machinery*, not the
coefficient. — **OPEN** at the feasibility tier (the standing charge: build the dynamics
first, never reverse-fit the number). *(`GRUT_UV_ANCHOR_FEASIBILITY.md`.)*

And the construction pass hardens that OPEN into a structural **NO**, through an obstacle
internal to GRUT — the **locality–dynamics fork.** The anomaly number that would source a
Riegert action lives in the E₄ / a-channel, which GRUT's own second-order analysis proves is
Lovelock-null, dynamically dormant; the only *live* channel is the c / Weyl² channel. So σ
is caught in a fork with no third branch: either it is locality-safe and ghost-free but
*inert* (confined to E₄, no β-function), or it is dynamically live but then it *is* the
metric trace tied to T_μν by the Ward identity — giving a 1/k⁴ matter→metric pole (strictly
worse than the forbidden 1/k², verified as a divergent limit) *and* a fourth-order
Ostrogradsky ghost (opposite-sign residues ⇒ Im χ < 0 ⇒ N < 0 ⇒ non-unitary). No window
exists where σ is simultaneously locality-safe, Q-safe, and live. — **FORBIDDEN-BY-THEOREM**
(modulo one stated Ostrogradsky-leg gap that a covariant Paneitz-BRST treatment would close;
locality already kills the route independently). This is the sharp boundary of GRUT's
explanatory reach. *(`GRUT_UV_SECTOR_CONSTRUCTION.md` §5; `second_order_kernel.py`.)*

Stand back and the two great no-gos turn out to be one. A genuinely *derived* dark sector and
a *derived* hierarchy magnitude would each require the same thing: a **new propagating vacuum
pole** — a new *mode*, not merely a new operator. The locality/no-halo theorem and the
Ostrogradsky + Q pincer jointly forbid it from the vacuum's own action (the pincer modulo
one stated Boulware–Deser/Ostrogradsky leg that a covariant Paneitz-BRST treatment would
close; locality already forbids it independently). Two escapes must be kept apart. *Changing
the vacuum itself* — adding a new propagating vacuum pole, or a second metric — genuinely
**"constitutes a different theory, not GRUT"**: it alters the single-mode object every v3/v4
result was derived from, and *that* is what the no-go forbids. *Specifying field content for
the microscopic bath F(t)* is a different move entirely: F(t) is the pre-responsive substrate
GRUT already posits (Q → F(t) → responsiveness → vacuum), it lives *outside* the no-gos'
jurisdiction precisely because the theorems are about the vacuum's action and not the medium
beneath it, and detailing it breaks no GRUT premise — it is **a deeper substrate layer of
GRUT, not a successor theory**. It buys no *derived* dark sector or hierarchy magnitude here:
it is conjectural, costs free parameters, and so cannot upgrade either HOSTED/FORBIDDEN result
to DERIVED — which is exactly why the vacuum-level verdict stands. — **FORBIDDEN-BY-THEOREM**
(modulo that one gap). This is the deepest
unity in the framework: **dark matter is HOSTED and the hierarchy magnitude is FORBIDDEN for
the same structural reason.**

And so the 34-order hierarchy is not an embarrassment but a **structurally protected**
feature. It reduces to exactly two anchored numbers — ln(τ₀/t_P) = 134.447 and
ln(τ_micro/t_P) = 56.214 — plus the orthogonal dimensionless α; the famous gap
c = ln(τ₀/τ_micro) = 78.233 is exactly their *difference*, not an independent third number. Its
*existence* is forced (the MZ projection requires τ₀ ≫ τ_micro; the no-dark-mode result is
magnitude-inert across thirty-four orders, flipping only at the pure ratio τ_K/τ₀ = 1/4). Its
*magnitude* is unknown, and the RG firewall is *directional* — the UV cannot reach down to
generate the IR operator — so it protects the two-anchor split rather than bridging it. —
**FORBIDDEN-BY-THEOREM** (magnitude) **+ DERIVED** (existence). This is the cleanest example
in the whole spine of placing a fact at its true tier: GRUT forces *that* a hierarchy exists,
forbids deriving *how big* it is, and books the size honestly as an anchored input.
*(`GRUT_HIERARCHY_LEDGER.md`; `tau_hierarchy_decision.py`.)*

GRUT does not contain a quantum theory of gravity in the sense of a UV-complete dynamical
sector. It contains a precise *map* of where that sector would have to live, and a proof
(modulo one stated gap) that it cannot be built from GRUT's own content without fracturing
the framework. That is the ToE move at this rung: not omniscience, but a sharp boundary
honestly drawn.

---

## §6 — Observers & Self-Knowledge

Run forward far enough and the universe folds back on itself: the same constitutive law that
built the cosmos now describes the things inside it that *measure*. This is the highest and
most fragile rung, and its honesty is the whole point. Almost everything here is
DERIVED-*as-recovery* — you get the law back in a limit, you do not add a new postulate —
with two razor-sharp seams where the boundary shows through.

**Quantum mechanics is recovered, not assumed.** Write the constitutive law τż + z = z_target
with z_target built from the Schrödinger residual as a Newton–Raphson step. In the τ → 0
(zero-memory) limit the equation becomes algebraic, z = z_target — the instantaneous
response — and one constitutive step *is* the first-order Euler–Schrödinger update exactly,
with norm preserved and ⟨σ_x(t)⟩ = cos ωt on a precessing qubit. QM is the zero-memory face
of the responsive vacuum. — **DERIVED** (as recovery, not from nothing): the recovery is
exact *as a limit*, verified at first order on a single qubit; promotion to many-body
Hamiltonians is the unbuilt part. *(`qm_recovery`, computed.)*

**The arrow of time is a consequence, not an axiom.** Constitutive evolution carries an
entropy production Ṡ = (1/τ₀)⟨(z − z_target)²⟩, which is non-negative for any state, zero only
at the fixed point, and cumulatively monotone — verified numerically to be strictly positive
over 10⁵ random states and exactly zero at z = z_target. The Second Law follows from Q's
retarded kernel rather than being postulated alongside it. — **DERIVED.** And the
directionality is even more primitive than memory: the in-in arrow (response-to-past,
S_IF[φ₊ = φ₋] = 0) is a theorem of the formalism containing no τ₀, and so it *predates* the
emergence of responsiveness — the keystone of §1 reappearing as the floor of this section.
*(`arrow_of_time_from_entropy`, computed.)*

**The measurement problem dissolves into physics — almost entirely.** When a deep-crystal
apparatus (Λ_grav·τ₀ ≫ 1) couples to a quantum object (Λ_grav·τ₀ ≲ 1), the joint dynamics is
apparatus-dominated and the faster crystallizer drags the slower across the
refractive→classical threshold. Collapse is physical contact through the low-bandwidth memory
channel — no observer postulate, the same scaling law applying to measurer and measured
(verified on a 1 g / atom example, with the apparatus crystallizing ~10³² times faster).
Wigner's friend dissolves as conditional-state consistency. — **DERIVED `[SPLIT]`**: this
derives decoherence, diagonalization, and the pointer basis — but *not* the probability
weights. *(`measurement_resolution`, computed.)* That exception is the sharpest seam of the
spine. The CTP / noise-kernel machinery produces off-diagonal decay and an asymptotically
diagonal density matrix in the pointer basis, but it does **not** produce the specific
weights |⟨ψ|pointer_i⟩|² on the diagonal — those inherit from the Hilbert-space inner
product, not from the noise kernel. **The Born rule is OPEN** (and, honestly, HOSTED: the
weights are received from the postulated inner product, and no GRUT mechanism yet generates
them). This is the one place a careless spine would claim "GRUT derives QM probabilities" and
be refuted on contact — and it is, notably, *not* a GRUT-specific weakness: Copenhagen,
Many-Worlds, decoherent histories, and CSL all require extra structure here. —
**OPEN.** *(`born_rule_postulate_open_negative`, open_negative.)*

**Unification is the meta-statement, and it has a sharp boundary built in.** GRUT's
unification is not a reconciliation of two languages but a single parameter space: QM is the
τ₀ → 0 limit of the constitutive law, GR is the ωτ₀ → ∞ limit where n_g → 1 and gravity is
instantaneous; both limits are exact, and the crossover is the crystalline boundary
X = Λ_grav·τ₀ = 1. One closed-time-path action on S⁴ with SM content yields the sectoral
limits, and the unification *scale* is the table-top decoherence plateau (~689 Hz), not the
Planck energy — which is why GRUT has near-term falsifiers at all. — **DERIVED `[SPLIT]`** as
a meta-statement. The boundary is the ToE claim itself: unification means a coherent tiered
*place* for everything, not omniscience. The very minimalism that unifies QM and GR — one
dynamical metric, one memory pole — is what *forbids* a second propagating pole, and that is
precisely *why* dark matter is HOSTED and the hierarchy magnitude FORBIDDEN. Unification and
the no-gos are the same fact seen from two sides. *(`closed_universe`, `fixed_point_principle`,
foundational; `ctp_action_structure`, computed.)*

**The universe knowing itself.** A closed universe has no external observer, so it performs
self-measurement by maintaining two copies of its own history — φ₊ forward, φ₋ backward — and
the physical dynamics is the *difference* between them; S_IF[φ₊ = φ₋] = 0, zero response when
nothing has changed. The CTP formalism, read this way, compares the universe to itself, and
the same equation describes observer and observed; the fixed point z* = z_target[z*] is the
state that generates its own boundary conditions. — **CONJECTURAL `[SPLIT]`**: the *object*
(the in-in self-comparison, S_IF vanishing on the diagonal) is *proven* — a genuine theorem.
Reading it as the universe "knowing itself" is a structural interpretation layered on top.
The structure is proven; the metaphor is flagged. *(`closed_universe`, foundational; the
self-knowledge reading is interpretive.)*

**Consciousness — a hook, and only a hook.** This is the most speculative event in the entire
spine, and it is tagged loudly. GRUT offers two structural footholds and nothing more: the
in-in self-comparison provides a formal self-reference ("the universe knowing itself"), and a
40 Hz neural resonance arises from two independent framework routes (Λ_grav at tubulin-dimer
parameters → 39.9 Hz; self-referential fixed-point network dynamics → 41.7 Hz) that share no
fitted parameters, with the constitutive driving term vanishing at the fixed point (a
self-maintaining system). The 40 Hz *numbers* are computed; the *consciousness bridge* is
not. — **CONJECTURAL.** What the hook *is*: self-reference plus a numerical coincidence. What
it is *not*: any account of experience, qualia, or awareness. What would be required to go
further: a derivation connecting the fixed-point self-reference to a first-person observable,
which GRUT does not have and does not claim. Nothing in the framework depends on it — if it is
wrong, nothing else changes — and the v3 reader edition makes no consciousness claim at all.
Honesty here is load-bearing for the whole ToE's credibility. *(`neural_resonance_speculative`,
conjectural.)*

The epoch reads as a Theory of Everything in the honest sense: a coherent tiered place for
the observer — recovered, not bolted on — with a razor-sharp boundary at the Born rule and at
consciousness.

---

## §7 — What Kind of ToE This Is

The universe has now run forward, from Q-without-time to observers who are themselves
crystallized medium. It remains to say what the whole thing amounts to.

A Theory of Everything, in the sense this spine has tried to earn, is a **complete tiered map
with a sharp boundary** — not a derivation of everything. The map is complete in the sense that matters: it covers
genesis, the primordial universe, matter, gravity, the dark sector, quantum gravity, and
observers, and at every stage it names the tier of what emerges. The boundary is sharp: it is
drawn at exactly the places where GRUT's own structure draws it, and it is machine-enforced.

Completeness here means *every sector is tiered, including as not-yet-addressed* — not that
every Standard-Model puzzle is solved. Honesty requires naming the ones GRUT does not
currently place: the **strong-CP problem / axion** has no entry in the framework (absent, not
forbidden); the primordial **tensor-to-scalar ratio r** is OPEN — with no inflationary epoch
GRUT predicts no tensor spectrum and does not currently compute r; and the primordial scalar
amplitude A_s is the OPEN honest negative of §2. These are placed in the open, as the charter
requires, rather than passed over by a blanket "complete" — and they mark where the next
rungs of the program have to be built.

**The seams are the story, not the apology.** Dark matter is HOSTED; the hierarchy magnitude
and a second propagating pole are FORBIDDEN; the α-antecedent, the D initial-state condition,
A_s, the Born-rule weights, and the flavor mechanism are OPEN; consciousness is CONJECTURAL.
Each of these is the layered ontology showing through — *here the universe makes X, here it
must receive Y, here it forbids Z* — and each is woven into the forward narrative rather than
confessed at the end.

**The deepest unity is a single no-go wearing two faces.** The dark-matter no-go and the
hierarchy-magnitude no-go are the *same* no-go: both would require a new propagating vacuum
pole that GRUT's minimalism — one dynamical metric, one memory channel — forbids by locality
and by Q (the Q-pincer leg modulo one stated Ostrogradsky/Boulware–Deser gap, with locality
forbidding it independently). The same minimalism that *unifies* QM and GR as two exact limits of one action is
the minimalism that makes those two great unknowns structural rather than accidental. The
two-anchor hierarchy (τ₀, τ_micro) is therefore not a loose end but a *protected* feature,
guarded by GRUT's own locality and Q.

**The honesty is auditable.** Every tier asserted in this spine is checkable against
`grut/toe/registry.py` (121 claims across six tiers) and reproducible in `.venv`. A claim
advances a tier only when a test certifies it; a failed result is demoted and logged, never
quietly dropped. The discipline that a spine must not upgrade a HOSTED or OPEN result to
DERIVED is not a stylistic preference — it is operationalized in the apparatus, and it is the
reason this document can claim ToE status without claiming omniscience.

The through-line, restated one last time: **responding → memory → time → vacuum → structure →
observers** — with the no-gos carried not as embarrassments but as the load-bearing seams that
make the map complete and the boundary sharp. That completeness and that sharpness, together,
are the kind of Theory of Everything a *complete* GRUT ToE will be — in the only sense that
survives contact with a referee. v4 is the rung that has walked the universe end-to-end and
tiered every step; the destination is the same map with fewer OPEN cells. It arrives not when
GRUT derives everything — its own minimalism forbids that — but when every cell is settled at
the standing it has earned.

---

## Appendix A — Overclaim risks (the flagged list)

Each row is a place a careless or salesmanship-driven spine would inflate a tier. The
"honest statement" is what this document says instead.

| # | Risk | Tempting overclaim | Honest statement | Where it bites |
|---|---|---|---|---|
| 1 | **Dark matter** | "GRUT derives / explains dark matter." | HOSTED — received as a boundary condition; the locality/no-halo theorem plus the single-mode channel-counting postulate make this structural. The blind census refused to manufacture a cold relic. | §0, §1, §4, §5 |
| 2 | **Hierarchy magnitude** | "GRUT derives the 34-order hierarchy / τ₀'s value." | Existence FORCED; the MAGNITUDE is FORBIDDEN-by-theorem (no β-function carrying τ₀; needs a forbidden new pole). Booked as anchored. *The single fact that sinks the spine if inflated.* | §1, §5 |
| 3 | **Ω_Λ number** | "Ω_Λ = (2−R)² = 0.6886, derived." | (2−R)² = **0.7145** (tree-level) and **0.6886** (anchored full-Friedmann) are *different numbers*; the number is anchored via τ₀, the mechanism is derived. | §0, §1, §4 |
| 4 | **Baryogenesis** | "GRUT predicts η_B = 6.6×10⁻¹⁰." | EXISTENCE derived (R ≠ 1); MAGNITUDE uses HOSTED SM inputs (J_CP, K_neq). Not zero-parameter. | §1, §2 |
| 5 | **Consciousness** | "GRUT explains consciousness / the universe is conscious." | A CONJECTURAL hook only (in-in self-reference + a non-load-bearing 40 Hz coincidence); no account of experience; nothing depends on it. | §0, §6 |
| 6 | **α = 1/3** | "GRUT derives α = 1/3." | The value is ADOPTED; everything downstream is derived *from* it; the first-principles derivation (Riegert / IR-carrier antecedent) is OPEN. | §0, §1, §5 |
| 7 | **Standard Model** | "The SM falls out of the CTP action." | The SM is *consistent* with five CTP constraints (necessary, NOT sufficient); uniqueness not established. Gauge group, generations, content are HOSTED. | §0, §3 |
| 8 | **Generation count N = 3** | "K = 2/N is uniquely phase-independent at N = 3." | ⚠ FALSE as stated — K = 2/N is phase-independent for *all* N ≥ 3; N = 3 is fixed only by matching empirical K = 2/3. N_gen is HOSTED. *Was a false docstring at `koide_theta_uniqueness.py:12` — CORRECTED (commits 6b9c5e3, 4114daa) across the koide code (`koide_theta_uniqueness.py`, `koide_operator.py`) and the historical manuscripts (`GRUT_V7_FULL.md`, `GRUT_V8.md`, `GRUT_V8_CLEAN.md`, `README.md`).* The second in-code route (Ω_Λ→N=3 within Planck 2σ, `task01_n_generation_under_epsilon.py:139-222`) is unregistered, a-posteriori, and presupposes HOSTED field content — so it does not lift the tier either. | §3 |
| 9 | **Koide K = 2/3** | "GRUT forces the Z₃ flavor structure." | K = 2/3 is a DERIVED algebraic identity of an *assumed* Z₃ circulant; the structure is a fitted parameterization whose mechanism is OPEN. | §3 |
| 10 | **θ = 2/9** | "θ = 2/9 = K·α_vac is derived." | A CONJECTURAL candidate identity — registry tier-field reads `computed` for the uniqueness *scan*, but the algebraic-mechanism tier is OPEN (CTP-action derivation absent), so the spine books it CONJECTURAL / candidate-identity. | §3 |
| 11 | **Neutrino ordering** | "GRUT predicts normal ordering, parameter-free." | NH preference + Σm_ν ≈ 60 meV are DERIVED-from-a_ν=1; a_ν = 1 is itself DERIVED (unique boundary-degenerate Z₃ coupling, computed); only the deeper KS-anomaly account of the absent EM channel is OPEN; registry tier-field/notes tension flagged. Live falsifier. | §3 |
| 12 | **MOND** | "GRUT derives MOND / rotation curves." | The a₀ scale is DERIVED and in the band; ν(y) is ADOPTED, the mechanism REFUTED. MOND-compatible, not a derivation. | §4 |
| 13 | **Linear modified gravity** | quoting old v2 "enhanced growth / Ω_dm = α" as live. | FORBIDDEN (μ_linear = 1 by projector no-go) and refuted at ~32σ; now audit-trail-only. | §0, §4 |
| 14 | **Born rule** | "GRUT derives the Born probabilities." | GRUT derives decoherence + diagonalization + pointer basis; the weights are OPEN/HOSTED (inherit from the Hilbert inner product). | §6 |
| 15 | **f(T) / memory amplitude** | "f(T) = tanh(T_c/2T) is a parameter-free theorem." | Shape + limits follow from Q's FDT/KMS *given one identification*; trades a free width for a motivated identification — not fully parameter-free. | §1, §2 |
| 16 | **Elastic G₀ / viscoelastic SOLID** | "GRUT derives the vacuum rigidity G₀." | G₀'s *value* is derived from {ℏ, c, τ_micro}, but the SOLID premise (G₀ > 0) is an UNPAID POSTULATE — one of ≥4 degenerate medium classes; the resulting dark sector is REFUTED. | §5 |
| 17 | **A_s** | "GRUT predicts the primordial amplitude." | OPEN honest negative; all paths fail; α/S³ is a flagged clue, not promoted. | §2 |
| 18 | **n_s** | "GRUT predicts the spectral tilt." | CONJECTURAL fit — Hτ is back-solved from the observed n_s; the forward content is the running, CMB-S4-falsifiable. | §2 |
| 19 | **Unification** | "One action ⇒ GRUT explains everything." | Unification = QM and GR as exact limits of one action = a tiered PLACE for everything, NOT omniscience; the same minimalism forbids the second pole. | §6, §7 |
| 20 | **Pillar F / single-pole memory** | "F is derived from Q." | The single-pole FORM is derived (MZ Markovian limit); F as a pillar and τ₀'s value are POSTULATED/anchored. FDT-consistency is not derivation. | §0 |
| 21 | **Bridge D** | "Responsiveness is the spontaneous breaking of an exact GRUT symmetry." | The breaking term is derived; the underlying L₀→0 redundancy is PRESUPPOSED (Weinberg); GAP-1 (scale-free initial state) is OPEN. A redundancy can't be spontaneously broken — L₀ breaks its boundary *charge*. | §0, §1 |
| 22 | **BH interior / "1 Space"** | "GRUT derives the black-hole interior end-state." | CONJECTURAL; ρ_max is a flagged open numerical problem; 4-of-8 nonlinear rungs open; "1 Space" is interpretive. | §4 |

---

## Appendix B — Verified numbers (reproduced in `.venv`)

All checked against `.venv/bin/python` at authoring time:

- α = 1/3 = 0.33333; R = √(4/3) = 1.15470; S = 108π = 12π/α² = 339.292
- Ω_Λ bare = (2 − R)² = 0.71453 (vs the published full-Friedmann anchored value 0.6886)
- α/S³ = 8.534 × 10⁻⁹ (the A_s "clue," a factor ~4 from observed — *not promoted*)
- f(T_c) = tanh(½) = 0.46212; L₀ = cτ₀ ≈ 12.85 Mpc
- log₁₀(τ₀/τ_micro) = 33.98; ln(τ₀/τ_micro) = 78.233 = ln(τ₀/t_P) − ln(τ_micro/t_P) = 134.447 − 56.214 (differences taken at full precision before rounding; the rounded 134.45 − 56.21 = 78.24 is a display artifact, not the value)
- trace-anomaly numerators a = 1991/2, c_KS = 849
- G₀ = ℏ/(c³ τ_micro⁴) = 1.0294 × 10¹⁶ Pa, computed with the exact τ_micro = ℏ/(k_B·T_c) = 1.39639 × 10⁻¹⁹ s (NOT the rounded 1.4 × 10⁻¹⁹ s, which gives ≈ 1.02 × 10¹⁶); c_s/c = 1.0; warm gap = 4.71 keV
- η_B route ≈ 6.57 × 10⁻¹⁰ vs Planck 6.10 × 10⁻¹⁰ (+7.7%)
- a₀ = cH₀/(2π) ≈ 1.06 × 10⁻¹⁰ m/s²; H₀ ≈ 68.8 km/s/Mpc
- Registry tier census (exact, `Counter(c.tier for c in REGISTRY)`): 49 computed, 28 open_negative, 19 anchored, 11 conjectural, 10 meta, 4 foundational = 121 claims
