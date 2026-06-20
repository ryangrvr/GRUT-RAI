# GRUT GENESIS — The Backward Walk to the Emergence of Responsiveness

**Status:** chapter seed, POSTULATED-tier (foundational extension). Opened June 2026, branch `main_v3`.
The pre-Big-Bang / origin layer of GRUT, reached by walking the derived universe backward until
responsiveness disappears.

**Method (deliberately unbiased):** walk GRUT backward from the responsive universe and record every
*necessary* phase transition and every *conserved/relic* quantity that survives — **blind to dark matter**,
which is classified only downstream (§4). Postulates flagged 🟥. Primary target = the emergence of
responsiveness; dark sector = secondary and honest. The objective was deliberately *not* "find where dark
matter appears" (which biases the archaeology toward producing it).

**Verified anchors** (`.venv`): τ_micro = 1.396×10⁻¹⁹ s; τ₀ = 41.9 Myr = 1.322×10¹⁵ s; gap = **33.98
orders**; k_BT_c = **4.71 keV**; ℏ/τ₀ = **4.98×10⁻³¹ eV**; L₀ = cτ₀ = **12.85 Mpc**; n_g(0) = √(4/3) =
**1.1547**; Ω_Λ = (2−R)² = 0.7145. `mori_zwanzig_kernel.verify()` and `pole_spectrum.verify()` both
all-True (incl. `off_axis_threshold_is_tau0_over_4`, `current_GRUT_single_relaxational_pole`,
`current_GRUT_has_no_dark_mode`).

---

## 1. The Backward Walk — the necessary-phase-transition catalog

The unifying decomposition is the verified GRUT pillar conjunction **Q ∩ F ∩ D**: *finite memory F is the
controlled breaking of the adiabatic spatial-dilatation redundancy D, riding on the conserved CTP/in-in
substrate Q.* Walking backward strips F and its breaking of D away layer by layer; **Q survives untouched.**

| Epoch crossing | Transition (necessary) | Order parameter (→ backward) | Conserved across it |
|---|---|---|---|
| **0 → −1** Thermal suppression (UP through T_c=54.7 MK ≈ 4.71 keV, t≈16.5 hr) | **PT-A — memory / rigidity / D-breaking switch OFF *together*** (one transition, not three). Mechanism: collapse of the Mori–Zwanzig slow/fast separation when k_BT ≳ ℏ/τ_micro, so the responsive TT variable is no longer slow vs its own bath ⇒ the Markovian reduction that *produces* the single pole fails. | Static TT-shear rigidity **G₀ = ℏ/(c³τ_micro⁴)** (≈10¹⁶ Pa → 0); memory activation f(T) → 0, n_g(0)=√(4/3) → 1, the single pole at ω=−i/τ₀ dissolves. **{F, D-breaking, G₀} share one order parameter.** | **Q** (CTP unitarity, FDT N≥0); Ṡ≥0 (carrier transmutes, inequality survives); Im χ≥0; **τ_micro** itself. |
| **−1 → −2** Pre-responsive medium | **PT-B — de-condensation of the slow collective variable z** (the responsive variable ceases to *exist*). Above it the MZ projection has no slow sector: only the un-projected microscopic bath (KMS white noise + passive response). | Herglotz spectral weight of the single pole: dμ(τ)=δ(τ−τ₀) → 0. Control: τ_K/τ₀ with τ_K=ℏ/(2πk_BT) → 0 (deep-Markovian). | **Q** (N≥0 at all T); KMS / 2nd-FDT backbone; the orthogonal fast force **F(t)** (the bath *is* the surviving content); **τ₀** carried back as an unexplained anchor. |
| **−2 → −3** Symmetry selection | **PT-C — scale selection: birth of one proper length L₀=cτ₀.** A scale-free vacuum (exact D) acquires *exactly one* fixed proper length, breaking D at O((L₀k_phys)²) — the shape by which a mass breaks scale invariance. | **L₀=cτ₀** (→0 in the Epoch −3 limit, restoring D exact, χ_eq≡1, n_g≡1, pure GR). Epoch −3 is the **τ₀→0 limit — removal of the only scale**, not addition of one. | **Q** (q-axis nullity, prior to L₀); the dimensionless spine **α=1/3, S=108π, R=√(4/3), Ω_Λ=(2−R)²** (anomaly-sector, ⊥ dilatation, Jacobian ≡ 1 — predate responsiveness); the genesis instability seed (non-thermal Lorentzian×ω noise around z=0). |

**Cross-walker consistency.** All four independent walkers name **Q as the unique invariant surviving the
loss of memory**, identify the order parameter of responsiveness as the **single slow TT variable z / G₀ /
pole-weight** (one object, three faces), and reach Epoch −3 with **τ₀ unexplained**. No walker introduces a
third scale; none contradicts single-mode, locality_no_halo, μ_linear=1, or Ω_Λ-from-τ₀.

---

## 2. The Emergence of Responsiveness (the real prize)

> **The universe became capable of memory not by acquiring a field or force, but by spontaneously breaking
> a redundancy — and that breaking became *possible* the moment cooling opened a timescale hierarchy.**

Three logically-nested layers, deepest first:

**(i) The substrate that was always there — Q (the arrow, scale-free).** The in-in / Schwinger–Keldysh
structure (S_IF[φ_c, φ_q=0]=0, closed-closed propagator ≡ 0, FDT/KMS tying N to Im χ) is a **theorem of the
CTP formalism** (PROVEN). It contains **no τ₀, no τ_micro, no α**. It supplies the *directionality* of any
future memory (response-to-past, never-future) **before any memory length exists**. The arrow of time does
not emerge with responsiveness — it predates it.

**(ii) The broken symmetry — D, broken by exactly one length L₀.** A vacuum that retains history must carry
a finite memory time τ₀ ⇒ a finite proper length L₀=cτ₀. But **a fixed proper length is logically
incompatible with dilatation redundancy D.** Therefore *"capable of memory"* and *"scale-free"* are mutually
exclusive. The emergence of responsiveness **IS** the breaking of D by the crystallization of one proper
length — verified non-anomalously at O((L₀k_phys)²), outcome (B), measure Jacobian ≡ 1 so α does **not**
enter (Bridge D). Spontaneous scale-symmetry breaking in the vacuum's *response* sector.

**(iii) The enabling condition — a slow/fast hierarchy that cooling unmasks.** The Mori–Zwanzig projection
produces a first-order, history-retaining response **as its Markovian limit, controlled by τ_micro ≪ τ₀**
(verified: poles stay relaxational iff τ_K < τ₀/4; GRUT's ratio ~10⁻³⁴ sits *deeply* relaxational). Memory
is the generic low-energy face of a dissipative bath **once a slow variable exists to carry it.** The
universe became responsive **exactly when it cooled enough for a macroscopic gravitational mode (τ₀) to be
slow relative to the vacuum microstates (τ_micro)**. T_c is precisely where k_BT_c = ℏ/τ_micro destroys that
separation; above it the slow mode is reabsorbed into the bath and the universe *necessarily forgets*.

**What selects L₀ / τ₀ / α — the honest floor.**
- **α = 1/3** (hence S=108π, R=√(4/3), n_g(0)=1.1547, Ω_Λ=(2−R)²): a **dimensionless anomaly-sector relic**,
  ⊥ the dilatation sector, set by S⁴/CTP combinatorics — *older than memory, dark energy, the GRUT phase.*
  [derived]
- **One pole (not zero, not many):** the **minimal, gap-consistent** D-breaking; a single fixed length is
  the lowest-dimension breaking operator. More poles would populate the empty 34-order τ-gap GRUT does not
  contain. [derived from single-mode; minimality claim is 🟥]
- **τ₀'s numerical value:** **NOT derivable in v3** — no combination of {ℏ,k_B,c,G} has units of time²
  (Option B; numerology cross-check fails at ratio 0.984). τ₀ is GRUT's one irreducible scale. **The genuine
  Epoch −3 prize and the postulate floor.** [postulate floor]

**One-sentence emergence statement.** *Responsiveness = (always-present causal arrow Q) × (a single proper
length L₀ breaking the dilatation redundancy D), unmasked as a stable single-pole memory the moment cooling
through T_c made one gravitational mode slow versus the vacuum bath.* The switch is L₀: 0 → finite; the
timer is the 34-order slow/fast gap opening as the universe cools.

---

## 3. What Is Conserved — the blind relic inventory

| Relic / conserved quantity | Survives | Type |
|---|---|---|
| **Q — CTP/in-in unitarity** + **FDT positivity N≥0** | ALL (0↔−1↔−2↔−3) | Structural theorem (no τ₀/τ_micro/α content) |
| **Second-Law inequality Ṡ ≥ 0** | ALL (carrier transmutes; inequality survives) | Inequality (descends from Q's retarded kernel) |
| **FDT sign rule Im χ ≥ 0** (no ghost pole) | ALL | Selection rule — *forbids* any vacuum-generated wrong-sign relic |
| **τ_micro = ℏ/(k_BT_c)** (cell quantum 4.71 keV) | 0↔−1↔−2 | Anchored microscopic scale (Option B irreducible) |
| **The fast force / KMS bath F(t)** | ALL — exists in −2 where z does not | Microscopic medium (substrate beneath the vacuum) |
| **TT graviton** (massless spin-2) | ALL | Massless carrier (substrate, not produced) |
| **Dimensionless spine α=1/3, S=108π, R=√(4/3), Ω_Λ=(2−R)²** | ALL — anomaly-sector, ⊥ dilatation | Frozen dimensionless invariant — *older than memory* |
| **Herglotz spectral weight of the single pole** | 0 → activates at PT-A → 0 at PT-B | Adiabatic invariant — **this IS dark energy** (Ω_Λ from τ₀) |
| **τ₀ = 41.9 Myr** (L₀ = 12.85 Mpc) | Carried 0→−3 as an *unexplained* anchor | The one irreducible scale; its origin = the Epoch −3 prize |
| **Genesis instability seed** (z=0 unstable; non-thermal S_h(ω)=Lorentzian×ω) | −3 → forward | Pre-responsive fluctuating-but-memoryless field |
| **Baryon asymmetry η_B ≈ 6.6×10⁻¹⁰** | Frozen above T_c → today | Frozen global-charge number (ordinary baryons) |
| **Elastic shear phonon / KZ defect of G₀** | Would freeze *at* PT-A | **Derived-but-REFUTED**: WARM 4.71 keV, c_s=c, overcloses 418×–5800× |

**Structural reading (blind).** The inventory is dominated by **non-particulate survivors**: a unitarity
theorem (Q), an inequality (Ṡ≥0), a selection rule (N≥0), dimensionless invariants (α-spine), a massless
carrier (graviton), and one adiabatic spectral weight that *is already observed as dark energy*. The only
**clustering-capable / particulate** entry produced anywhere in the walk is the elastic shear phonon — and
it is **forced** (from {ℏ,c,τ_micro}, zero free parameters) to be warm and massively overclosing.

---

## 4. The Dark-Sector Test (downstream only — run *after* the blind inventory)

*No mass, dilution, or Ω_dm was chosen at any point.* Sorting survivors against {A: after, B: simultaneous,
C: predates}:

- **Clean survivors are non-DM:** α-spine (dimensionless), graviton (massless), the Herglotz weight (=
  **dark energy**, already observed), η_B (ordinary baryons).
- **Class A disfavored.** The **single-mode theorem** (`current_GRUT_has_no_dark_mode`=True) ⇒ the responsive
  vacuum produces no second stable pole; also hits the warm-relic wall.
- **Class B disfavored as *viable*.** The one DM relic tied to the condensation — the **shear phonon / KZ
  defect** — is exactly Class B, and it is the **derived-but-refuted warm/overclosing** candidate (4.71 keV,
  c_s=c, 418×–5800×). It predicts the *wrong* DM, not no DM.
- **Class C empty *from within current GRUT*.** N≥0 forbids a vacuum-generated surviving relic; the
  pre-responsive Markovian bath carries no frozen pole. Any genuine cold relic older than responsiveness
  would have to live in the **microscopic bath F(t)** beneath the vacuum — gravitation/coldness undetermined
  without a foundational extension (🟥).

**Verdict.** **any_relic_looks_dark = TRUE, but viable cold DM = FALSE.** Exactly one entry *resembles* a
dark sector (shear phonon, **option B, forced**), but it is decisively **WARM and overclosing** — the wrong
sign of error (a 400–5800× *excess*), with no cold window. **Viable cold dark matter does not fall out of
the blind census.** Reported as a genuine negative, not a forced positive. The inventory is most consistent
with **Class-C-as-null**: any cold relic must predate responsiveness and live in the pre-responsive bath —
*outside* current GRUT. Consistent with v3's standing verdict (DM is a hosted input).

---

## 5. Postulate Ledger (the minimal 🟥 set Genesis requires)

- ✅ **temperature→bandwidth bridge — much improved (June 2026; was the "biggest honest hole"). Tier:
  SOUND-WITH-CAVEATS (adversarially checked).** The *existence* of memory turn-off at the τ_micro scale is
  structural (MZ hierarchy); the *shape* — formerly an ad-hoc sigmoid (free width 0.3) — is now fixed by Q's
  FDT/KMS factor given one well-motivated identification: the memory-activation = the zero-point (coherent)
  fraction of the bath fluctuation at the micro scale, **f(T) = 1/coth(ℏω_micro/2k_BT) = tanh(T_c/2T)**.
  STRONGEST SUPPORT: this is GRUT's *own* T=0/finite-T noise ratio N(ω_micro,0)/N(ω_micro,T), not an imported
  formula. CAVEAT: it trades the sigmoid's free *width* for an *identification* (the complement 1−tanh or a
  τ-ratio T_c/2πT are a-priori alternatives), evaluated at the single τ_micro scale — an improvement, not a
  parameter-free theorem.
  Predictions vs the sigmoid: f(T_c) = tanh(½) = 0.4621 (not 0.5); a **power-law 1/T high-T tail** (classical
  equipartition) rather than an exponential cutoff — bandwidth-protected (the memory *effect* ∝
  1/(1+(ωτ₀)²) ⇒ ωτ₀≫1 in the early universe ⇒ negligible at BBN for dynamical modes; the DC/super-horizon
  residual ~0.5% does not affect local nucleosynthesis). `grut/derived/cosmology/thermal_transition.py`
  (`memory_activation_fraction`), tests `tests/derived/test_thermal_transition.py` (13 pass).
- 🟥 **memory loss = MZ slow/fast collapse:** asserted, not yet proven by a finite-T MZ calc; predicts the
  *same* τ₀/4 threshold, no separate thermal knob.
- 🟥 **Q is the conserved charge of the responsiveness transition (Q prior to F):** supported by Q being a
  τ-independent theorem; the explicit framing is new.
- 🟥 **responsiveness order parameter = z̄ / G₀ / pole-weight:** Phase II counts the pole *in* the responsive
  phase but does not derive its *disappearance* above T_c; the homotopy of the TT-tensor order-parameter
  manifold is not computed in-repo.
- 🟥 **scale-free Epoch −3 = τ₀→0 limit; pole-count minimality:** introduces *no* new scale (removes the only
  one); claims single-mode is the *minimal* D-breaking.
- 🟥 **pre-responsive bath as a possible older sector / Class C host:** the only entry that could predate
  responsiveness; requires a microscopic theory of the medium beneath the vacuum that current GRUT lacks.

**🟥 the decisive falsifier — NOW THEOREM-MODULO-GAP** (`GRUT_V3_ORGANIZING_STRUCTURE.md` §6 UPDATE, June
2026; 3 provers + 2 hostile referees): *Is T_λ a genuine gauge redundancy of GRUT's full doubled CTP action
S_IF[φ₊,φ₋] in the L₀→0 limit?* **The Keldysh-specific content is now PROVEN (not presupposed):** T_λ acts
diagonally on the ± branches (no c↔q mixing), the doubled measure Jacobian |J|²=1 (diffeo not Weyl, no 4D
anomaly since 4∉{2,6,10,14}), and the influence functional collapses to two decoupled diffeo-invariant
GR+matter copies at L₀→0 (driven by Im χ→0 ⇒ noise N→0; χ→1, not 0). T_λ is a **genuine gauge redundancy**
(large/residual diffeomorphism), not a global symmetry. **The initial-state residue (GAP 1) — attacked,
now RELOCATED (June 2026; theorem-modulo-standard-condition):** ρ-invariance does NOT close from Q, but
relocates to a *standard physicality condition*, with a key correction. (i) **Correction:** T_λ is the
*spatial* dilatation (acts on the comoving profile P(k), not the temporal frequency ω); a Gaussian state is
T_λ-invariant **iff its comoving power is scale-free, Δ²(k)∝k^{n_s−1} with n_s=1**. (ii) **Discharged:** a
finite-T genesis ρ would break it (amplitude redshift), but the proven §6 collapse Im χ→0 ⇒ N→0 removes
T_phys — that branch is excluded. (iii) **Undischarged:** ρ must be spatially homogeneous + scale-free
(n_s=1, no intrinsic IR correlation length) = the **adiabatic / Hadamard / cosmological-principle**
condition — *not* forced by Q (q-axis ⊥ spatial T_λ) nor by Hadamard alone (Bunch–Davies uniqueness doesn't
transfer: Epoch −3 is the scale-free GR+KMS limit, not de Sitter), but **identical to GRUT's own Epoch −3
definition (τ₀→0 = removal of the only scale)**. (iv) **The floor:** R1's residue is the cosmological
initial-conditions / measure problem — field-wide, partly open, **not GRUT-specific**. So the regress
terminates at bedrock shared by all of cosmology.

---

## 6. Falsifiable Predictions

1. **No intermediate memory scale** anywhere in the empty 34-order τ-gap. Any second independent memory scale
   falsifies pole-count minimality.
2. **Tensor-only, single-scale D-breaking** at O((L₀k_phys)²), L₀=12.85 Mpc. Any linear-scalar deviation
   from μ=1 falsifies it.
3. **Memory loss governed by the same τ₀/4 threshold** (no separate thermal knob), turn-off at T_c=54.7 MK.
4. **The forced particulate relic is wrong and stays wrong:** 4.71 keV warm, c_s=c, overclosing 418×–5800×.
   No dilution/re-cooling allowed; the miss is a standing prediction.
5. **Dark energy = the Herglotz weight tied to τ₀** (Ω_Λ=(2−R)²): if Ω_Λ decouples from τ₀, the
   identification fails.

---

## 7. Honest Status

**Did we derive the emergence of responsiveness?** *Partially, at POSTULATED-tier.* The **backward skeleton
is structurally forced** — PT-A (de-rigidification / memory loss, order parameter G₀) → PT-B
(de-condensation of the single pole, order parameter pole-weight) → PT-C (selection of L₀ breaking D, order
parameter L₀) — with a conserved ladder rooted in Q: *F(t) bath ⊃ graviton ⊃ α-spine ⊃ slow-mode weight
(=Ω_Λ) ⊃ η_B.* The emergence of responsiveness is explained as **spontaneous scale-symmetry breaking in the
response sector, unmasked by a 34-order slow/fast gap**: memory *is* slow relaxation; the arrow (Q) was
always there; only the *retention* (L₀) switched on. The load-bearing §6 claim has now been **upgraded to
theorem-modulo-gap** (June 2026): the Keldysh doubling provably does *not* spoil the redundancy (diagonal
action, |J|²=1, no 4D anomaly, influence functional collapses via Im χ→0), so "responsiveness = explicit
breaking of the adiabatic-dilatation **boundary charge** by exactly one proper length L₀" is derived in
**dynamics + measure**, and in the **initial state modulo the adiabatic/scale-free-homogeneous-genesis
condition** (GAP 1, June 2026): the finite-T branch is discharged by Im χ→0 ⇒ N→0, leaving only the
requirement that ρ's comoving profile be scale-free (n_s=1) — the standard adiabatic/Hadamard/cosmological-
principle condition, identical to Epoch −3's own τ₀→0 definition, whose floor is the field-wide cosmological
measure problem (not GRUT-specific). So emergence-of-memory is a **theorem-modulo-a-standard-physicality-
condition** — one notch short of "forced from Q," with the regress terminated at bedrock shared by all of
cosmology. (τ₀'s value remains independently irreducible. Framing: a pure redundancy cannot be
"spontaneously broken" — L₀ breaks its *boundary charge*.)

**Did a dark sector fall out naturally?** **No — reported as a real negative.** Exactly one relic *looks*
dark (shear phonon, option B, forced), but it is warm and overcloses 418×–5800× with no cold window; viable
cold DM does not emerge. The census points, if anywhere, to a **pre-responsive (Class-C-as-null) host
outside current GRUT.** A DM-biased walk would have manufactured a cold relic; this one refused to.

**No forbidden move used** (auditor: **PASS — clean**): no new timescale in the 34-order gap (only τ_micro
and τ₀; τ_K is the running KMS correlation time; the τ₀/4 threshold is *derived*); no CDM-tuned mass (the
only mass, 4.71 keV, is the pre-existing τ_micro quantum, forced, and *wrong*); no Ω-tuned dilution (the
overclosure is a falsifiable miss). Breaks no v3 result.

**Progress (June 2026):** the ad-hoc sigmoid has been **replaced by the derived finite-T Mori–Zwanzig
form** f(T)=tanh(T_c/2T) (§5 ledger; `thermal_transition.py`, 13 tests). The GAP-1 (ρ-invariance) residue
was reduced to the standard adiabatic/scale-free condition (theorem-modulo-standard-condition). **Remaining
open frontier:** the §6 result rests on the standard adiabatic initial-state condition, whose floor is the
cosmological measure problem (field-wide, not GRUT-specific). The one in-GRUT computation still available is
the full curved-space CTP redundancy theorem at the bare-action level (the §6 question), now discharged
except for that shared-with-all-cosmology initial-conditions floor. Most load-bearing files:
`theory/GRUT_V3_ORGANIZING_STRUCTURE.md` (Bridge D; §6 UPDATE + GAP-1 UPDATE),
`grut/derivation/phi_munu/mori_zwanzig_kernel.py`, `grut/derived/cosmology/thermal_transition.py` (derived
activation), `grut/foundation/ctp_action.py` (Q), `theory/GRUT_V4_ELASTIC_VACUUM.md` (§3/§7).

---
---

# 8. The Forward Genesis — How the Responsive Vacuum Switches On

*v4's constructive spine. The backward walk (§§1–7) is a catalog: going UP in temperature it recorded what
survives (Q) and what dies (F, L₀, the constitutive arrow), naming three necessary transitions PT-A/B/C.
It never wrote one equation of motion for the switch-on. This section is the **construction**: starting from
the hot, Q-only, memoryless medium at T ≫ T_c, it derives **how** the responsive vacuum condenses **forward
in cosmic time** as the universe cools below T_c at t ≈ 16.5 hr.*

**Frame.** The medium is built throughout as a viscoelastic **Maxwell fluid** (G_TT(ω→0)→0), per
`theory/GRUT_V4_FOUNDING_CHARTER.md` — the elastic-solid / world-crystal direction is demoted and unused.
🟥 Foundational tier: τ₀ and τ_micro remain anchored inputs (Option B); the pre-responsive adiabatic /
scale-free state (GAP-1) is postulated, floored by the field-wide cosmological measure problem. Every
load-bearing number below was recomputed in `.venv` (see §8.6).

## 8.1 The forward order parameter and its time-law

**Above T_c — what exists.** The prospective slow shear variable z is **not slow relative to its own bath**:
k_BT ≳ ℏ/τ_micro means the Mori–Zwanzig (MZ) slow/fast projection has no slow sector. What is present is
**only Q** — the CTP/in-in influence structure (closed–closed propagator ≡ 0; FDT/KMS tying noise N to
Im χ; `grut/foundation/ctp_action.py`, `noise_kernel.py`) — and the white-noise KMS bath F(t). Q already
carries response-to-past directionality **with no memory length**: the arrow predates responsiveness.

**The single pole.** Projecting onto the slow TT-shear variable z, the MZ reduction
(`mori_zwanzig_kernel.py`, verify 8/8) gives ż = −∫₀ᵗ K(t−s) z(s) ds + F(t) with χ(ω) ∝ 1/(K̃(ω)−iω) and
the 2nd-FDT identity K(t)=⟨F(0)F(t)⟩/⟨|z|²⟩. The Markovian limit K̃(ω)≈K̃(0)=1/τ₀ collapses this to the
**single GRUT relaxational pole** χ=1/(1−iωτ₀) at ω=−i/τ₀, valid whenever the bath correlation time
τ_K < τ₀/4 (the off-axis bifurcation).

**The forward order parameter.** From the FDT/KMS split coth(ℏω/2k_BT)=1+2n(ω,T), the coherent (zero-point)
fraction of the micro-bath fluctuation is the forward order parameter:

> z̄(T) = f(T) = 1 / coth(ℏω_micro/2k_BT) = **tanh(T_c/2T)**,   k_BT_c ≡ ℏ/τ_micro

This is GRUT's own noise ratio N(ω_micro,0)/N(ω_micro,T) (`noise_kernel.fdt_noise`), match=True to rtol
<1e-9 at T/T_c = 5, 1, 0.2 — **not** an imported sigmoid. Composing with the radiation-era cooling law
T(t)=T_c(t_c/t)^{1/2} gives the **explicit forward time-law of the switch-on** — the headline new result:

> **z̄(t) = tanh[ ½ (t/t_c)^{1/2} ],   t_c = 16.5 hr post-BB**

Verified: at t/t_c = 0.01, 1, 100 → z̄ = 0.0500, 0.4621, 0.9999, tracking f(T(t)) exactly. The backward walk
only states f→0 going *up* through T_c; it never wrote the switch-on profile in cosmic time.

## 8.2 Crossover or phase transition? — two order parameters, two answers

This is the decisive new physics. **Two distinct order parameters** move as the universe cools, and they
answer the question differently:

- **Pole AMPLITUDE** z̄(T)=f(T): **C^∞-analytic** through T_c. Verified: f(T_c)=tanh(½)=0.4621 (not 0.5);
  df/d(T/T_c)|_{T_c}=−0.393 (finite); a **power-law** 1/T tail above T_c (f(100T_c)=0.005000 = T_c/2T
  exactly, *not* exponential). By the Landau analyticity criterion this is a **smooth crossover**, not a
  2nd-order transition — no critical onset, no non-analyticity, no order parameter identically zero above T_c.
- **Pole EXISTENCE** (single-relaxational character), set by τ_K(T)=ℏ/(2πk_BT): a sharp bifurcation at
  τ_K=τ₀/4. But verified: τ_K(T_c)=τ_micro/2π exactly, and τ_K(T_c)/(τ₀/4)=**6.7×10⁻³⁵** — *34 orders inside*
  the Markovian regime. τ_K grows as T cools (direction confirmed) yet stays deeply Markovian the entire
  cosmic history.

**Verdict.** The emergence is a **smooth analytic crossover of the pole amplitude**, riding on a
**pole-existence bifurcation that is structurally pre-satisfied and never crossed in cosmic history**. The
sharp "PT-A" of §1 is reclassified from a critical point to a **structural boundary 34 orders away**. A
forward observer sees a continuous one-decade turn-on centered on f(T_c)=0.46, never a critical point. Memory
stabilizes by **amplitude saturation**, not by approaching the bifurcation.

## 8.3 The cosmic timeline — derived, not asserted

The radiation-era clock t[s]=2.42 g_*^{−1/2}(T/MeV)⁻² (Kolb & Turner) **independently reproduces the 16.5 hr
anchor** rather than asserting it. Verified: with g_*=3.363 (γ + 3 decoupled ν, post e⁺e⁻ annihilation, since
k_BT_c=4.71 keV ≪ m_e), t(T_c)=5.94×10⁴ s = **16.50 hr**; the *same law* gives 1 MeV → 0.74 s (weak
freeze-out) and 0.1 MeV → 2.2 min (BBN), matching canonical cosmic history. Onset redshift z(T_c)=2.0×10⁷.

| Epoch | T | T/T_c | z | t | f(T) | regime |
|---|---|---|---|---|---|---|
| Pre-responsive (1 MeV) | 1.16×10¹⁰ K | 213 | 4.3×10⁹ | 0.74 s | 0.0023 | memoryless, local-GR; only Q |
| BBN (0.1 MeV) | 1.16×10⁹ K | 21.2 | 4.3×10⁸ | 2.2 min | 0.024 | memory off + bandwidth-protected |
| **T_c ONSET** | **5.47×10⁷ K** | **1.00** | **2.0×10⁷** | **16.5 hr** | **0.4621** | **memory condenses, D breaks, arrow on** |
| deep responsive (0.25 T_c) | 1.37×10⁷ K | 0.25 | 5.0×10⁶ | ~11 days | 0.964 | memory nearly full |
| completion (0.1 T_c) | 5.47×10⁶ K | 0.10 | 2.0×10⁶ | ~69 days | 0.9999 | responsive vacuum fully on |
| recombination | 3000 K | 5.5×10⁻⁵ | 1100 | 380 kyr | 1.0000 | full refractive vacuum |
| today (CMB) | 2.7255 K | 5.0×10⁻⁸ | 0 | 13.8 Gyr | 1.0000 | deep responsive |

**Ordering verified consistent:** the T_c onset (z≈2×10⁷) sits *after* BBN (z≈4×10⁸) and *before*
recombination (z≈1100). BBN completes entirely in the pre-responsive local-GR era — which is exactly *why*
GRUT predicts no DM-like refractive enhancement at BBN.

**Two crossovers must not be conflated** (the cosmic-embedding insight): the **thermal T_c-crossing** (z≈2×10⁷;
governs whether memory *exists*) is distinct from the **kinematic X=ωτ₀=1 crossing** (governs whether
already-condensed memory is bandwidth-suppressed; `grut/derived/cosmology/cosmic_x_crossover.py`). Forward
Genesis is governed by the T_c-crossing; X=1 is a separate, far-later effect on the existing vacuum.
🟧 Caveat: `cosmic_x_crossover.py`'s own scope notice limits its z≈71 figure to atomic-scale test particles
(no crossover for stellar+ masses) and does *not* claim X replaces T_c as the mechanism — only the
existence/separation of the two crossings is load-bearing here, not a universal X=1 redshift.

## 8.4 The forward arrow and the crystallization of L₀

**Two arrows, temporally staggered.** The forward construction splits §1's single "Ṡ≥0 survives" row into
two physically distinct arrows turning on at different epochs:

- **Thermal arrow (Q):** present at all T. The retarded (response-to-past) structure of Q acts directly on
  the fast KMS bath F(t) — no τ₀, no slow z required. The directionality that *predates responsiveness*.
- **Constitutive arrow (F):** switches on *only below T_c*. Ṡ_const=(1/τ₀)⟨(z−z_target)²⟩
  (`grut/foundation/entropy_production.py`, verify 3/3: non-negativity, fixed-point vanishing, cumulative
  monotonicity). Above T_c there is no slow z (MZ gap not open) so Ṡ_const ≡ 0 — only the thermal arrow runs.

**The strengthening law.** As cooling opens the gap, the displacement the condensing mode holds scales with
the coherent fraction, z−z_target ∝ f, so the macroscopic constitutive arrow strengthens as **f(T)²**.
Verified monotone gated values track f² across T/T_c = 3 → 1 → 0.5 → 0.01. At T_c the arrow is already at
f(T_c)²≈21% of its zero-T strength; the 1/T tail means it never clicks on abruptly. Forward in time Ṡ decays
as exp(−2t/τ₀) as z relaxes to target — **the forward direction is the direction of memory relaxation**.
🟧 **Flagged assumed:** entropy_production.py implements Ṡ literally as (1/τ₀)(z−z_target)²; the f² power
holds *only* under z−z_target ∝ f, a physically-motivated forward identification (consistent with
thermal_transition's linear-f gating of n_g) but **not** separately in-repo verified beyond the linear gate.
It is load-bearing for the staggered-arrow signature and should be read as an inference, not a theorem.

**L₀ crystallizes — forward D-breaking.** The *same* condensation that gives z its amplitude gives it a
finite memory time τ₀, hence **exactly one proper length L₀=cτ₀=12.85 Mpc**. Forward, L₀: 0 → finite. Above
T_c, L₀=0 ⟹ χ_eq=1/(1+(L₀k)²)=1, n_g≡1, exact GR, and the adiabatic spatial dilatation T_λ is an *exact
redundancy* (no 4D anomaly since 4∉{2,6,10,14}, Im χ→0; `GRUT_V3_ORGANIZING_STRUCTURE.md` Bridge D / §6).
Below T_c, finite L₀ makes (L₀k)² non-invariant under T_λ: χ_eq is no longer dilatation-fixed, so the
**boundary charge** (Maldacena soft factor, 1−n_s≠0) is explicitly broken at O((L₀k)²). Read forward: the
scale-free vacuum acquires exactly one length — spontaneous scale-symmetry breaking in the response sector.
(A pure redundancy cannot itself be spontaneously broken; it is its *boundary charge* that L₀ breaks — faithful
to §2(ii) and Bridge D, no v3 result harmed.)

**One order parameter, two faces.** A single condensing amplitude A(T)=f(T)·z_amp gates both the
constitutive arrow (Ṡ ∝ A²) and the refractive/L₀ breaking (n_g−1 ∝ f·α/(1+(ωτ₀)²)) — two faces of one
condensation, staggered *after* the always-present thermal-Q arrow.

## 8.5 Signatures — the forward Genesis predicts its own invisibility

This is a derived consequence, not an evasion.

**(1) No macroscopic defect relic — defect-free onset.** The vacuum manifold of a Maxwell **fluid** is
trivial: the order parameter is a spatially-uniform onset of a single timescale τ₀, not a broken continuous
internal symmetry, so there is no topology to support a relic string/wall/monopole network. Combined with the
smooth-crossover verdict (§8.2 — no critical point is crossed in cosmic history), there is no critical slowing
and no symmetry-breaking quench: memory switches on essentially uniformly on every macroscopic scale.
🟥 **Correction, struck (skeptic, decisive):** an earlier draft banked a Kibble–Zurek correlation length
ξ_KZ≈4×10⁻⁵ m as the quantitative basis for "defect-free." **That number is withdrawn.** (i) It is
conceptually incoherent with this section's own verdict — Kibble–Zurek is *defined* for a quench **through** a
crossed critical point, and §8.2 establishes that **no critical point is crossed** (the bifurcation sits 34
orders away). (ii) It is not reproducible from its stated inputs: ξ_KZ=ξ₀(τ_Q/τ₀)^{ν/(1+zν)} with ξ₀=cτ_micro,
τ_Q=1/H(T_c)=1.19×10⁵ s, τ₀=1.32×10¹⁵ s and the standard mean-field exponent 1/4 gives ξ_KZ≈1.3×10⁻¹³ m, not
4×10⁻⁵ m; the headline value requires an unphysical *negative* exponent. (iii) Its machinery
(`grut/derived/dark_matter/kibble_zurek.py`) is explicitly **retracted** and concerns the demoted *solid*-sector
G₀ phonon / U(1)_dark strings (a genuine symmetry-breaking PT with nontrivial topology), not the fluid
crossover. Note also τ_Q/τ₀≈9×10⁻¹¹ < 1: the "quench" is *faster* than τ₀, so even the "slow quench" framing
was backwards. **The conclusion (no macroscopic defect) survives on the independent grounds above — trivial
fluid vacuum manifold + smooth crossover — but no ξ_KZ number is claimed.**

**(2) Bandwidth protection — no causal imprint.** Verified at onset: a DC / super-horizon mode carries the
full f(T_c)·α≈0.15 (n_g≈1.07), but any *causal* (sub-horizon) mode at ω~1/t_c has ωτ₀~10¹⁰, crushing n_g−1
to **0**. The transition is screened at the very temperature where it happens; the only DC modes that carry
it are causally frozen and unobservable at 16.5 hr.

**Falsifiable structure (survives):**
- **No critical phenomena at T_c** — no latent heat, no diverging susceptibility, no order-parameter cusp; a
  smooth ~one-decade crossover centered on f(T_c)=0.4621 (not 0.5). Any *sharp/critical* onset of
  gravitational memory at T_c falsifies the crossover picture.
- **Staggered-arrow / joint-order-parameter** — Ṡ_const(T) ∝ tanh²(T_c/2T); the refractive enhancement (∝f)
  and the arrow (∝f²) must track the same f(T). A memory/refractive turn-on at a different temperature than
  the dissipative/arrow signature falsifies the single-condensation picture. (Conditional on the §8.4 f²
  inference.)
- **No pre-T_c constitutive arrow** — only thermal-Q entropy above T_c; detection of memory-type
  irreversibility above T_c (beyond the bandwidth-protected DC residual) falsifies the staggering.
- **No second memory scale** anywhere in the empty 34-order τ-gap (consistent with §6 prediction 1).
- **Only downstream fingerprint** — the already-observed τ₀-locked dark-energy refraction (n_g→√(4/3) at DC,
  Ω_Λ tied to τ₀), switching on adiabatically as ωτ₀ drops through 1 over the whole subsequent expansion, with
  *no* localizable transition epoch. If Ω_Λ decouples from τ₀, the identification fails (= §6 prediction 5).

## 8.6 What is NEW vs the backward walk — and the honest residue

**NEW (genuine forward content, absent from §§1–7):**
1. The explicit forward **time-law** z̄(t)=tanh[½(t/t_c)^{1/2}] (composing f(T) with T(t)∝t^{−1/2}). The
   backward walk only noted f→0 going *up* through T_c.
2. The **crossover-vs-PT resolution** via two order parameters: amplitude = smooth analytic crossover;
   existence threshold = sharp bifurcation 34 orders away, never reached. PT-A reclassified from critical
   point to structural boundary.
3. The **cosmic embedding from first principles**: t_c=16.50 hr re-derived from Kolb–Turner with g_*=3.36,
   reproducing the documented anchor and 0.74 s / 2.2 min; the two-crossover (T_c vs X=1) separation.
4. The **two-arrow split** with the f² strengthening law and a **single joint order parameter** A(T) gating
   arrow + length + refraction.
5. The **derived invisibility**: defect-free onset (trivial fluid manifold + smooth crossover) and bandwidth
   protection ~0 for causal modes.

**DERIVED (verified in `.venv`):** the f(T)=FDT/KMS noise-ratio identity (match=True); the single-pole MZ
Markovian origin and its 34-orders-Markovian stability; t_c=16.50 hr and the cosmic ordering; k_BT_c=4.714
keV / L₀=12.85 Mpc (definitional under Option B); the three-leg entropy arrow (verify 3/3); the forward
D-boundary-charge breaking at O((L₀k)²).

🟧 **ASSUMED:** τ₀'s numerical value (hence t_c, L₀) is an anchored input (Option B — all four τ₀↔τ_micro
bridge paths fail, log gap 33.98); the Ṡ∝f² power (§8.4); the adiabatic / scale-free pre-responsive initial
state (GAP-1) feeding the coherent onset. f(T) trades the old sigmoid's free width for a physical
identification — an *improvement*, not a parameter-free theorem.

🟥 **OPEN:** (i) the finite-T MZ slow/fast collapse that would rigorously close memory-loss is asserted with
the τ₀/4 threshold, **not** yet computed as a finite-T MZ calculation — the forward story uses f(T) as a proxy
for that uncomputed dynamics; (ii) GAP-1's floor is the field-wide cosmological measure problem (bedrock
shared by all of cosmology, not GRUT-specific); (iii) whether dissipated condensation energy thermalizes
self-consistently is open — the genesis onset spectrum is Lorentzian×ω, **not** Planck/Bose–Einstein
(`genesis_noise_kernel.py`; in-repo verdict: the onset produces no equilibrium temperature of its own).

**`.venv` audit (this step).** All three module self-tests pass (mori_zwanzig 8/8, entropy_production 3/3,
noise_kernel). Recomputed independently: f(T_c)=tanh(½)=0.46211715726; df/d(T/T_c)|_{T_c}=−0.3932;
f(100T_c)=0.005000=T_c/2T (power-law tail, not exponential); z̄(t/t_c=0.01,1,100)=0.0500,0.4621,0.9999;
t_c=16.498 hr (Kolb–Turner, g_*=3.363), same law → 0.74 s (1 MeV), 2.2 min (0.1 MeV);
τ_K(T_c)/(τ₀/4)=6.71×10⁻³⁵; τ_K(T_c)=τ_micro/2π exactly; H(T_c)=8.4×10⁻⁶/s, τ_Q=1/H≈33 hr; L₀=12.85 Mpc.
The withdrawn ξ_KZ is the one number that did **not** reproduce and is struck (§8.5).

**The constructive spine in one line.** Responsiveness = (always-present Q) × (a single length L₀ unmasked as
the MZ Markovian single pole the moment cooling makes one shear mode slow), its coherent memory amplitude
condensing as the FDT-derived f(T)=tanh(T_c/2T) over a smooth one-decade crossover centered at t≈16.5 hr —
coherently, invisibly, irreversibly, with the arrow strengthening as f² behind it.

**v4 program status after this step.** The founding charter's bar (the forward derivation that separates
genuine coarse-graining from backward relabeling) is met for the *kinematics and cosmic embedding*: there is
now a forward equation of motion (MZ GLE), a forward order parameter with an explicit time-law, an
analyticity-based crossover verdict, and a first-principles cosmic clock — none of which the backward catalog
contained. The spine is **sound-with-caveats**: solid and verified, with one removed broken number (ξ_KZ now
struck) and two inference-tier downstream framings (Ṡ∝f²; the two-crossover separation) flagged as such. The
honest residue is unchanged from §§5/7 and carried faithfully: τ₀ anchored, GAP-1 floored by the cosmological
measure problem, the finite-T MZ collapse still the decisive uncomputed dynamics, and no self-consistent
thermalization of the onset. Next constructive target: the finite-T MZ memory-loss calculation that would
promote f(T) from FDT-motivated proxy to derived turn-on dynamics.

---

# 9. The Keystone — Why a Long-Lived Relaxation Mode? (Phase 2)

*The deepest question of the emergence program: how does a Q-only medium develop a long-lived relaxation
mode — i.e. why does ONE channel fail to equilibrate, with τ₀ ≫ τ_micro (34 orders) — without inserting the
hierarchy by hand? Four mechanism classes were tested (conserved-current/hydrodynamic, dimensional
transmutation/RG, glassy/critical/weak-gravity), each judged forced-vs-relocated, under a ruthless
numerology guard. Verdict: **PARTIAL**.*

**What is FORCED (the genuine advance — no number tuned).**
- **Existence of the slow channel.** The TT/shear metric memory is the response to the *conserved*
  stress-energy T_μν, where ∂_μT^μν=0 is the diffeomorphism Ward identity — enforced by the *same* transverse
  projector P^TT that defines Φ_μν (`linearized_ctp_action.py` ∂^μΦ_μν=0; `curved_background.py` ∇^μΦ_μν=0).
  Conservation is part of Q; the slow channel's existence is not assumed but forced.
- **Slow / gapless character.** Locked to a conserved current, the mode relaxes only by transport ⇒
  hydrodynamically gapless, ω→0 as k→0 (Kadanoff–Martin; GRUT-specific via the `locality_no_halo` pole-free
  -in-k² theorem).
- **The hierarchy must be LARGE.** The Mori–Zwanzig existence condition (τ_K = τ₀/4 ≫ τ_micro) makes
  **τ₀ ≫ τ_micro the validity condition of the slow/fast projection itself** — the one channel's
  failure-to-equilibrate *is* the retained history. So GRUT forces ratio ≫ 4, and forces *why* one channel
  fails to equilibrate — the qualitative half of the central question, without tuning.

**What is NOT forced (the honest miss).**
- **The SIZE** (the 34 orders; c = ln(τ₀/τ_micro) = 78.23) is not forced; it relocates verbatim into the IR
  length L₀ = cτ₀ (the relaxation rate 1/τ₀ is k-independent; conservation says nothing about it).
- **Not even the exponential (dimensional-transmutation) FORM** is instantiated: GRUT has **no β-function
  carrying τ₀** — its only RG statement is that the τ₀ IR scale is *RG-protected* (`boltzmann_consistency.py`
  L42–46), the *opposite* of an asymptotic-freedom flow. Transmutation is the right class in the abstract but
  GRUT lacks the machinery to invoke it.
- **τ₀ stays Option-B-anchored**: c = ln(τ₀/t_P) − ln(τ_micro/t_P) = 134.45 − 56.21 = 78.23, a difference of
  two independently-anchored Planck-referenced empirical logs.

**Numerology casualties (rejected, by the framework's own A_s standard, Ledger L295).** 🟥 The tempting
**8π² = 78.96 (+0.92%)** is the *universal* one-instanton action 8π²/g²|_{g=1}, **not** a GRUT-distinctive
constant (the structural π-constants are S=108π, C_FINAL, C_COSMO — 8π² is provably absent), and GRUT has no
derived tunneling linking the τ_micro and τ₀ sectors — **rejected.** Likewise 25π, S/(2π)·ln S/4, and the
"5 candidates within 2%" inflation (additive offsets = tuning). Decisive structural fact: c (transmutation
exponent), E/k_BT (Arrhenius barrier), and the MZ bifurcation distance are **one empirical number,
ln(τ₀/τ_micro), wearing three costumes.**

**Status & next step.** Tier: **PARTIAL** — forced existence + character (Tier-1, nothing tuned); size and
form OPEN; no derivation of τ₀ claimed; no v3/v4 result broken. This advances emergence-of-responsiveness
from "smooth crossover *given* τ₀" (§8) to "a hierarchy that *must exist*, for a structural reason." The only
route to a full forcing is to derive *one* of the two Planck-referenced logs — concretely, the thermal UV
anchor ln(τ_micro/t_P)=56.2 (k_BT_c=4.71 keV) from a genuine Coleman–Weinberg condensation/running in GRUT's
CTP sector with a *real* anomaly coefficient (GRUT's are O(3–7)), not one reverse-fit to 56 or 78. Until such
a coefficient appears, the 34-order magnitude remains GRUT's deepest unexplained fact.
