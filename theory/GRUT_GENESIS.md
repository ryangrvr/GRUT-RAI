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
