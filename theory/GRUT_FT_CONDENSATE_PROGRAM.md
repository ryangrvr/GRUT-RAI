# THE F(t) CONDENSATE PROGRAM
## A minimal substrate-sector host for dark matter (a deeper layer of GRUT), with its honest cost

**TIER: CONJECTURAL / substrate-sector of GRUT / deeper layer (NOT a v4-core derivation: it adds 2 free parameters).**

This document works out the layer of GRUT's own substrate — the pre-responsive bath F(t),
which GRUT already posits *beneath the vacuum* — that would have to be given field content
to host the dark-matter candidate that
test `GRUT_DM_NONTHERMAL_COHERENT_TEST.md` (commit 836ffb4) left **specified-and-unmet
to the dex** — outcome (b). A positive here is *GRUT extending into its own deeper
substrate layer*; it is **never** a GRUT (v4-core) derivation, because it costs 2 free
dimensionful parameters. The deliverable is the precise blueprint and its honest cost,
not a sale.

**Headline verdict (all three construction angles concur, all numbers `.venv`-reproduced):**
the bath sources **0 of 3** requirements. The substrate-sector construction is a **clean 2-dial
dimensionful insertion** (mass `m`, amplitude `φ_i`) plus the structural addition of a
scale-breaking potential the scale-free bath does not carry. It stays no-go-clean and
KMS/Q-clean. It is **GRUT — its substrate sector detailed — not a different theory**; the
substrate it adds is exactly the "microscopic medium beneath the vacuum that current
GRUT has not yet detailed" (`GRUT_V4_SPINE.md:311-312, :163`). (Analogy: this is to GRUT
what the Standard Model is to general relativity's `T_μν` — the content of a substrate slot
the umbrella theory already has, not a successor to it.)

---

## 1. PURPOSE & TIER

The predecessor DM test returned outcome (b): dark matter remains **HOSTED but
SPECIFIED-AND-UNMET to the dex**. The missing host is a coherent zero-entropy scalar in
the pre-responsive bath F(t), needing three things: (i) a field VEV `⟨φ⟩ ≠ 0`, (ii) a
NEW mass scale `m ~ 10⁻²²` eV in the empty middle of the 34-order gap, (iii) an
abundance dial `φ_i ~ 10¹⁶⁻¹⁷` GeV. This program works out that substrate-sector layer: the
minimal construction, its honest cost, and whether the bath can source any of it.

**This is GRUT detailing its own deeper substrate layer, beneath the vacuum.** F(t) is the
substrate the framework has always posited and flagged as its open frontier
(`GRUT_GENESIS.md:94`: F(t) = "Microscopic medium (substrate beneath the vacuum)";
`GRUT_V4_SPINE.md:311`: "beneath the vacuum itself, lies the microscopic" medium). Giving
that already-posited bath field content breaks no GRUT premise (Q intact, locality intact,
vacuum sector unchanged, no-gos untouched). A positive is GRUT extending into its own
substrate sector — **never** a v4-core derivation (it adds 2 free parameters).

**Fail-conditions held in force throughout:**

- **No reverse-fit (binding rule).** `m` and `φ_i` must NOT be back-solved from
  `Ω_dm = 0.12` or from `10⁻²²` eV. Either a quantity is SOURCED from the bath's existing
  structure (mechanism shown) or it is an INSERTED new input (labeled, counted). The
  numerology guard (`GRUT_GENESIS.md:502-508`; `registry.py` `A_s`/`8π²` standard) is on:
  the geom-mean of GRUT's two anchors misses the window center by **7.19 dex**, so a new
  scale is genuinely needed — an inserted scale must not be disguised as a derived one.
- **No-go-clean.** The condensate must gravitate via ORDINARY GR (`T_μν` source, the
  permitted Newtonian Green's function) and cluster via ORDINARY collapse — NOT a `1/k²`
  inverse-Laplacian kernel, NOT a second vacuum pole, NOT a new relaxational mode.
- **Q/KMS-consistent.** It must respect KMS positivity and unitarity — no `Im χ < 0`,
  no `N < 0`.
- **Honest input count.** State EXACTLY how many NEW independent inputs the condensate
  costs on top of `{Q, α, τ₀, τ_micro}`, and which (if any) are SOURCED rather than
  INSERTED.

---

## 2. THE SPECIFICATION INHERITED

The DM test's shopping list, with the empty middle mapped in dex (all `.venv`-reproduced;
ledger in §"`.venv` verification"):

| Requirement | Target | Where it sits |
|---|---|---|
| **VEV** | `⟨φ⟩ ≠ 0` (coherent, zero-entropy) | a homogeneous classical mean — a *different object* from the bath's `⟨h⟩ = 0` noise |
| **Mass** | `m ~ 10⁻²²` eV, window `[10⁻²², 10⁻¹⁹]` eV | **22.67 dex below** `ℏ/τ_micro = 4713.68 eV`; **8.30 dex above** `ℏ/τ₀ = 4.978×10⁻³¹ eV` |
| **Abundance** | `φ_i ~ 10¹⁶⁻¹⁷` GeV | sets `Ω_dm` via misalignment; `≈ 0.045 M_Pl,red` to land 0.12 at `m = 10⁻²²` eV |

**The dex-mapped empty middle.** The two GRUT anchors span `log₁₀(τ₀/τ_micro) = 33.976`
dex. The fuzzy-DM window occupies a 3-dex slot inside it, and the partition closes
exactly: `22.673` (upper miss, `E_micro` to window top) `+ 3.000` (window) `+ 8.303`
(lower miss, window floor to `E_τ₀`) `= 33.976`. The DM test found **no spectral feature**
in this middle — featureless and flat across the 34 decades, with power only at the `τ₀`
peak (the too-smooth endpoint).

---

## 3. THE MINIMAL CONSTRUCTION

Add to F(t), beneath the responsive vacuum, **one classical homogeneous real scalar `φ`**
with the minimal scale-breaking potential and a frozen initial misalignment:

```
V(φ) = ½ m² φ²          (canonical fuzzy/ULA potential; m² = V'')
EOM:  φ̈ + 3H φ̇ + m² φ = 0
IC:   φ(t_i) = φ_i ,  φ̇(t_i) ≈ 0   (misaligned, Hubble-frozen)
```

**Production = vacuum misalignment** (canonical wave/fuzzy DM — Hui et al. 2017;
Marsh 2016):

- While `H ≫ m`, Hubble friction freezes `φ` at `φ_i` (`w ≈ −1`, a tiny vacuum term).
- When `H ~ m` the field rolls and **oscillates**; the cycle-averaged energy redshifts as
  `a⁻³` — it becomes **cold dust, `w = 0`, automatically stable ≫ 14 Gyr**.
  (`.venv`: `m/H₀ ≈ 6.9×10¹⁰ ≫ 1` at `m = 10⁻²²` eV — deep in the cold/oscillating
  regime today.)
- It **gravitates as ordinary matter**: `T_μν = ½φ̇² + ½m²φ²` sources the Einstein
  equation through the **permitted Newtonian Green's function**, and clusters by
  **ordinary gravitational collapse** — not via a `1/k²` inverse-Laplacian, not as a
  second vacuum pole, not as a new relaxational mode.

**Abundance (misalignment relic):**

```
Ω_dm h² ≈ 0.1 · (φ_i / 10¹⁷ GeV)² · (m / 10⁻²² eV)^0.5
```

**Phenomenology that fixes the target window** (external — *not* from `Ω_dm`, see §7): a
`10⁻²²` eV field has de Broglie wavelength `λ_dB = 1.917 kpc` at `v = 10 km/s`
(`.venv`, `λ = ℏ/mv` per `GRUT_DM_NONTHERMAL_COHERENT_TEST.md:41`), giving kpc-scale
soliton cores; the Lyman-α floor sits near `~2×10⁻²¹` eV. The clustering window is
`m ∈ [10⁻²², 10⁻¹⁹]` eV.

This is textbook fuzzy DM. The entire GRUT-specific content is the *location* — it lives
in F(t), the substrate, the only entry in the whole framework where "a genuine cold relic
could attach" (`GRUT_V4_SPINE.md:311`, `GRUT_GENESIS.md:125`).

---

## 4. THE COST LEDGER — sourced vs inserted

What F(t) actually provides (all verified):

- **Two frequencies only:** `ℏ/τ_micro = 4713.68 eV` (log₁₀ `+3.6734`) and
  `ℏ/τ₀ = 4.9775×10⁻³¹ eV` (log₁₀ `−30.3030`), span `33.976` dex
  (`closure_protocol.py:206, :411`).
- **A dissipative noise spectrum** `S_h(ω, T=0) ∝ ω/(1+(ωτ₀)²)` — Lorentzian×ω, **not**
  Planck/Bose–Einstein, slopes verified `+1.000 / −1.000`, single peak at
  `ω = 1/τ₀ = 7.562×10⁻¹⁶ Hz` (`genesis_noise_kernel.py:65-95, :103-112`). `⟨h⟩ = 0`,
  random phase, "fluctuating-but-memoryless," "no equilibrium temperature of its own"
  (`GRUT_GENESIS.md:99, :444`).
- **One dimensionless order parameter** `f(T_c) = tanh(½) = 0.4621` — GRUT's own noise
  ratio, a fraction in `[0,1]` (`GRUT_GENESIS.md:277-285, :143`).

### The ledger

| Requirement | Bath structure available | Verdict | Why |
|---|---|---|---|
| **(1) Mass `m ~ 10⁻²²` eV** | the two anchor frequencies + combinations | **INSERTED** | the middle of the 34-dex gap is **featureless** (`max\|d²logS_h\| ≪ 1` in window — no resonance, no gap, no pole); the natural bridge `√(E_micro·E_τ₀) = 4.844×10⁻¹⁴ eV` **misses the window center by 7.185 dex** and does not point at the window; `m = V''` requires a scale-breaking term, and **grep returns 0 substantive `V(φ)`/mass-term/VEV hits** in the bath spec files. `m` is a genuine **third frequency**. |
| **(2) Coherent VEV `⟨φ⟩ ≠ 0`** | the `z=0` instability seed | **INSERTED (does not form)** | `S_h` is the **symmetrized KMS two-point** `⟨{h,h}⟩` with `⟨h⟩ = 0`; a symmetrized two-point function **has no first moment** — the seed *fluctuates*, it does not *condense* to a coherent mean. A misalignment condensate needs a homogeneous classical `⟨φ⟩ ≠ 0` displaced in a potential — an object the noise spectrum does not carry. |
| **(3) Amplitude `φ_i ~ 10¹⁶⁻¹⁷` GeV** | `f(T_c) = 0.4621`; seed fluctuation `√⟨h²⟩` | **INSERTED** | `f(T_c)` is **dimensionless** (a noise fraction, no GeV); the dimensionful bath energies are both ≥22.7 dex below the abundance scale (`f(T_c)·E_micro = 2.18×10⁻⁶ GeV`); `√⟨h²⟩` is a **log-UV-divergent** fluctuation power (`ln(1+(ω_uv τ₀)²) ≈ 268.8`, cutoff-dependent) with `⟨h⟩ = 0` — wrong category, wrong units. |

### New-input count (the one number that matters)

Starting from GRUT's current minimal set **{Q, α, τ₀, τ_micro}** + proven structure, the
substrate-sector layer costs:

> **EXACTLY 2 new independent dimensionful inputs, both INSERTED, zero sourced:**
> 1. **the mass `m ∈ [10⁻²², 10⁻¹⁹]` eV** — a third frequency absent from
>    `{1/τ₀, 1/τ_micro}`;
> 2. **the amplitude `φ_i ~ 10¹⁶⁻¹⁷` GeV** — the misalignment decay constant / VEV (the
>    *dominant* abundance dial: `d ln Ω/d ln φ_i = 2`, vs the weak
>    `d ln Ω/d ln m = 0.5`).

Riding along, **not a new free scale but a real structural cost: (3) the potential SHAPE**
`V(φ) = ½m²φ²` — a scale-breaking quadratic with a displaced minimum that the
**scale-free, memoryless** bath does not provide. It is the structural carrier of input
(1), and it is what would make the bath's noise *condense* rather than merely *fluctuate*.
The gravitational coupling is **not** a new input (ordinary minimal `T_μν`).

*(Reconciling the angles: the three construction angles count "2 dimensionful dials + 1
inserted potential shape" vs "3 inputs." These are the same ledger stated two ways —
**2 new numbers, plus 1 new structure**. I report it as 2 dimensionful dials with the
potential as an explicit structural insertion, because `Ω_dm` and `m` are set by two
numbers, but the honest reader must see the potential is also absent from the bath.)*

GRUT's minimal set grows:
**{Q, α, τ₀, τ_micro} → {Q, α, τ₀, τ_micro, m, φ_i} + a quadratic potential `V(φ)`.**

---

## 5. SOURCING RESULTS — the make-or-break

Can the bath's **existing** structure source any of the three requirements **without
reverse-fit**? The honest answer, on every leg, is **no** — a clean 0-of-3.

**(1) MASS — INSERTED.** Searched for any genuine bath feature in `[10⁻²², 10⁻¹⁹]` eV:

- The spectrum `S_h(ω, T=0) = (2ℏ/τ₀)·ω/(1+(ωτ₀)²)` has log-slope `−1.0000` across the
  window and `max|d²logS_h| ≪ 1` (featureless — no resonance, gap, or pole). The only
  amplitude peak is at `ω = 1/τ₀` (the too-smooth `τ₀` endpoint).
- The power-per-log integrand `ω²/(1+(ωτ₀)²)` is flat across the entire middle: variance
  accumulates at the `τ_micro` UV endpoint, nothing deposits in the window.
- The linearized `z=0` instability has **one** rate, `1/τ₀ → 4.98×10⁻³¹ eV` — the same
  endpoint, no new scale.
- Dimensional combinations of the two anchors: the geom-mean
  `√(E_micro·E_τ₀) = 4.844×10⁻¹⁴ eV` misses the window center by **7.185 dex**; the true
  seesaws `E_τ₀²/E_micro = −64.28 dex` and `E_micro²/E_τ₀ = +37.65 dex` are wildly out.

`m = V''` requires a scale-breaking term the bath does not carry (grep: 0 substantive
hits). **`m` is inserted** — a genuine third frequency.

**(2) CONDENSATE — does not form.** The mechanism that exists (the `z=0` seed) is
symmetrized KMS noise with `⟨h⟩ = 0`, random phase, "fluctuating-but-memoryless"
(`GRUT_GENESIS.md:99`). A symmetrized two-point function has no first moment: it
fluctuates, it does not condense to `⟨φ⟩ ≠ 0`. The mechanism the construct *needs* — a
potential with a displaced minimum — is absent (`GRUT_GENESIS.md:444`: "no equilibrium
temperature of its own"). **The VEV is inserted.**

**(3) ABUNDANCE — INSERTED.** The order parameter `f(T_c) = tanh(½) = 0.4621` is GRUT's
zero-point/total noise *ratio* — a **dimensionless** fraction in `[0,1]`
(`GRUT_GENESIS.md:277-285`), carrying no GeV. Adversarial attempts all fail:
`f(T_c)·E_micro = 2.18×10⁻⁶ GeV` (22.7 dex short); `√⟨h²⟩` is a log-UV-divergent
fluctuation power (`⟨h⟩ = 0`, cutoff-dependent units); the instability seed's `n_s = 1`
tilt is dimensionless. **`φ_i` is inserted.**

**The zero-entropy-condensate vs dissipative-bath tension — resolved, not hand-waved.**
F(t) is a dissipative FDT/KMS *noise* medium, not a Gibbs state — it "produces no
equilibrium temperature of its own" (`GRUT_GENESIS.md:444`). A coherent classical mean
`⟨φ⟩ ≠ 0` is *orthogonal* to the symmetrized two-point `⟨{h,h}⟩` (which has no first
moment). So the condensate and the KMS noise are **additive, non-competing** structures:
adding a zero-entropy VEV does not contradict the bath's dissipative character — it is a
new object placed alongside it, not in tension with it.

---

## 6. NO-GO + Q + UMBRELLA STATUS

### Stays outside all three no-gos (`pole_spectrum.verify()` all-True)

The three no-gos are **theorems about the VACUUM's action / response spectrum**. F(t) is
the substrate **beneath** the vacuum (`GRUT_V4_SPINE.md:311`, `GRUT_GENESIS.md:94`), so
all three lack jurisdiction over a condensate placed there — **provided** the condensate
behaves as ordinary matter, which the construction enforces:

- **`vacuum_spectrum_pole_classification` (`registry.py:5340`)** — forbids deriving DM
  from an extra *vacuum* pole. ✔ The condensate is not a vacuum pole; it is a matter field
  with its own `T_μν`.
- **`propagating_relic_forbidden_pincer` (`registry.py:5471`)** — Ostrogradsky + Q forbid
  a *vacuum-generated* propagating relic (higher-deriv TT ⇒ ghost ⇒ residue `−1/M²` ⇒
  `Im χ < 0` ⇒ `N < 0`). ✔ The condensate needs **no** higher-derivative TT operator; it
  is a healthy minimal scalar. *This no-go's own remedy clause (`registry.py:5492`)
  names this construction in advance:* "a derived dark sector requires a FOUNDATIONAL
  EXTENSION (a microscopic medium with massive excitations / a second metric)."
- **`locality_no_halo_theorem` (`registry.py:5532`)** — bans a `1/k²` inverse-Laplacian
  in the matter→metric kernel. ✔ The condensate clusters by **ordinary gravitational
  collapse** via the permitted Newtonian Green's function: the Poisson solve applies
  `1/∇²` to its **own** `ρ_φ` (what every matter field does), **not** a `1/k²` response to
  *baryons* where baryons have vanished (the forbidden `ρ_eff ∝ 1/k²`). No `1/k²`.

### Stays Q/KMS-clean

The condensate is a positive-energy classical `⟨φ⟩ ≠ 0` that **adds** to, and does not
spoil, the verified bath positivity. A bath-resident massive scalar has `Im χ ≥ 0` at
`+m`, so `N = 2ℏ coth(ℏω/2kT)·Im χ ≥ 0` is **preserved** — the exact opposite of the
forbidden vacuum route. `.venv` confirms `N ≥ 0` and `S_h ≥ 0` across `ω = 10⁻²⁰…10⁵²` Hz.
No `Im χ < 0`, no `N < 0`, unitarity intact.

### Substrate sector of GRUT, not a different theory

**This is GRUT detailing its own substrate sector — still GRUT, not a broken
premise.** Nothing in the construction requires `Im χ < 0`, `N < 0`, a second vacuum pole,
a `1/k²` kernel, or any violation of locality, causality, CTP unitarity, or finite memory.
Q's FDT/KMS structure is respected; the vacuum sector is unchanged; the three no-gos retain
their truth (the condensate lives outside their jurisdiction — they are theorems about the
*vacuum's* action, and this is the *substrate*). The GRUT umbrella — "Grand Responsive
Universe Theory" — **already contains** this slot: F(t) is the bath GRUT posits beneath the
vacuum, and giving it field content is GRUT extending into a deeper level of its own layered
ontology (Q → F(t) → responsiveness → vacuum → physics → structure → observers).

**But the honesty clause:** the substrate content it adds is the **one thing current GRUT
has not yet detailed** — "a microscopic theory of the medium beneath the vacuum that
current GRUT lacks" (`GRUT_GENESIS.md:163`; `GRUT_V4_SPINE.md:311`). Two distinct moves
must not be conflated:

- **Changing the responsive vacuum itself** (adding a new propagating vacuum pole / breaking
  single-mode minimalism — the route a *derived* cold DM from the vacuum would need):
  **forbidden / a different theory.** This changes the core object all v3/v4 results were
  derived from; the pincer forbids it. `GRUT_V4_SPINE.md:670`: a new vacuum mode / second
  metric "constitutes a different theory, not GRUT." The condensate does **not** do this —
  the vacuum cannot source it (the pincer), so the host had to move to the substrate.
- **Detailing the substrate F(t)** (giving the already-posited bath a condensing potential,
  with its 2 dials honestly counted): **GRUT — its substrate sector — not a different
  theory, and not a successor layer.** It breaks no GRUT premise (Q intact, locality intact,
  vacuum sector unchanged, no-gos untouched). It adds substrate structure GRUT always
  flagged as the open frontier. But it is **not part of GRUT's zero-free-parameter v4 core
  and not a v4-deliverable derivation**: it costs 2 free dimensionful parameters, so it is a
  distinct, larger-parameter, deeper deliverable under the GRUT umbrella. It is the *minimal*
  such detailing, and it remains minimal precisely because the bath sources none of the
  inputs — there is nothing cheaper to be had. (Analogy: F(t)-DM is to GRUT what the
  Standard Model is to GR's `T_μν` — matter/substrate content the umbrella theory already
  has a slot for, not a successor to it.)

---

## 7. ADVERSARIAL RESULTS

**Reverse-fit guard — PASSED.** No quantity was back-solved from `Ω_dm = 0.12` or from
`10⁻²²` eV.

- The window `[10⁻²², 10⁻¹⁹]` eV is **external canonical wave-DM phenomenology** (kpc
  soliton cores, Lyman-α floor), not derived from abundance. The window center is used
  only to *measure* the disqualifying geom-mean miss, never to fit `m`.
- The numerology guard is applied **positively** to confirm a new scale is needed: the
  geom-mean misses the window center by **7.185 dex** — not a sub-1% near-miss to bank,
  simply non-pointing (the same standard that rejected `8π² = 78.96` at `+0.92%` and the
  `A_s` coincidence; `GRUT_GENESIS.md:502-508`).
- The only combination that "lands" — the 3:1 log-mean
  `E_τ₀^0.75 · E_micro^0.25 = −21.81 dex` — is rejected on **three independent grounds:**
  (i) the center-hitting exponent is `0.7115`, **not** `3/4` (`a = 2/3 → −18.98`, out;
  `a = 4/5 → −23.51`, out — the "success" is a knife-edge); (ii) ~35% of exponents in
  `[0.60, 0.85]` land *only because the window is 3 dex wide* (not diagnostic); (iii) **no
  QFT mechanism** makes a condensate mass a fractional-power blend of two relaxation rates
  (`m² = V''`, never `τ₀^a τ_micro^(1−a)`).
- `φ_i` was presented strictly as the **consequence of choosing `m`** (the slide
  `1.095×10¹⁷ / 6.16×10¹⁶ / 3.46×10¹⁶ / 1.95×10¹⁶ GeV` for
  `m = 10⁻²²/⁻²¹/⁻²⁰/⁻¹⁹` eV is tabulated and flagged as the forbidden move), **never sold
  as a prediction**.

**Tier discipline — held.** Stays CONJECTURAL / substrate-sector-of-GRUT throughout; never
upgraded to DERIVED, and never smuggled into the zero-parameter v4 core. The construction is
GRUT detailing its own substrate sector (not a different theory, not a successor layer), but
it is **not a v4-core derivation** the instant that is claimed — because it adds 2 free
dimensionful parameters (the discipline of the pincer's remedy clause: the host is a deeper
substrate layer, kept out of the zero-parameter claim). The genuinely-different-theory line
(`GRUT_V4_SPINE.md:670`) applies to the *vacuum-pole* route, not to this substrate detailing.

**Input-count reconciliation.** The "2 vs 3" discrepancy across angles is the same ledger
stated two ways (2 dimensionful numbers `m`, `φ_i` + 1 inserted potential shape), reported
transparently as "2 dials + 1 potential," not hidden.

**Convention notes (non-load-bearing).** Low-`ω` spectral slope `+1.000` is the asymptotic
value (`ωτ₀ ≪ 1`); the actual window sits on the `−1.000` falling tail (`ωτ₀ ~ 10⁸`),
which *strengthens* the no-middle-feature conclusion. de Broglie `λ = ℏ/mv` uses reduced
`ℏ` matching the predecessor doc (`GRUT_DM_NONTHERMAL_COHERENT_TEST.md:41`); the full
`2πℏ` convention gives `12.05 kpc` — either lands in the kpc-core window.

---

## 8. VERDICT + FALSIFIER + NEXT STEP

**Tiered verdict.** A **viable substrate-sector blueprint at 2-dial dimensionful cost** —
*and simultaneously* a confirmation that no cheaper route exists. The minimal F(t)
condensate that hosts the GRUT dark-matter candidate is a **textbook misalignment scalar**
`V = ½m²φ²` placed in the substrate beneath the vacuum. Its honest cost is **2 inserted
dimensionful dials (`m`, `φ_i`) + 1 inserted potential shape; 0 of 3 requirements sourced
from existing bath structure.** It is **no-go-clean** (ordinary `T_μν`, ordinary collapse,
no `1/k²`, no second vacuum pole, no new relaxational mode) and **Q/KMS-clean** (`N ≥ 0`,
no `Im χ < 0`). It is **GRUT — its substrate sector detailed — a CONJECTURAL deeper layer,
not a different theory and not a successor layer**, but it is **not a v4-core derivation**
the moment that is claimed — because it adds 2 free parameters, and because the bath, like
the vacuum, sources none of it. (The genuinely-different-theory verdict belongs to the
*vacuum-pole* route, not to this substrate detailing.) The predecessor test's outcome (b) —
"hosted but specified-and-unmet to the dex" — is hereby **confirmed at the construction
level:** the host exists, the bath cannot pay for it, and the exact price is two numbers and
a potential.

**Falsifier.** Wave-DM in this mass window makes a sharp, near-term prediction: a `10⁻²²`
eV scalar forms **kpc-scale soliton cores** (`λ_dB = 1.917 kpc` at `v = 10 km/s`) and
suppresses small-scale structure. **Lyman-α forest counts** already push the floor toward
`~2×10⁻²¹` eV, and **dwarf-galaxy core/cusp and satellite counts** constrain the soliton
profile. If observations force `m ≳ 10⁻¹⁹` eV (no detectable wave-DM signature), the
fuzzy-DM end of the window closes and the misalignment construction loses its
distinguishing phenomenology — the substrate sector would then have to be re-specified at a
different mass, or abandoned for a non-misalignment host.

**What would have to be true for the bath to source a condensate (the next step).** The
bath would have to acquire, from its *existing* structure and without reverse-fit, all
three of: (a) a **scale-breaking potential `V(φ)`** with a displaced minimum (the bath is
currently scale-free and memoryless — `V'' = 0`); (b) a genuine **spectral feature** —
resonance, gap, or pole — somewhere in `[10⁻²², 10⁻¹⁹]` eV (the middle is currently
featureless, `max|d²logS_h| ≪ 1`, with power only at the `τ₀` endpoint); and (c) a
**coherent first moment** `⟨φ⟩ ≠ 0` out of what is presently a `⟨h⟩ = 0` symmetrized
two-point. A genuine tie of even **one** of these to bath structure would be a major
partial result; the present analysis finds none. The most promising single target is
mechanism (b): if the **MZ memory function** (the decisive uncomputed gap flagged in the
first-order-vacuum frontier) were computed and turned out to carry a third intrinsic time
scale in the empty middle, that would be the one place a bath-sourced mass could appear.
Absent that, the substrate sector is a clean 2-dial insertion.

---

## `.venv` verification ledger (all reproduced exactly)

- `τ₀ = 1.322364×10¹⁵ s`; `τ_micro = 1.396386×10⁻¹⁹ s`; span `33.97635` dex.
- `E_micro = ℏ/τ_micro = 4713.682 eV` (log₁₀ `+3.6734`);
  `E_τ₀ = ℏ/τ₀ = 4.977540×10⁻³¹ eV` (log₁₀ `−30.3030`).
- Window center `3.1623×10⁻²¹ eV` (log₁₀ `−20.50`); upper miss `22.6734`, lower miss
  `8.3030`, **partition `22.6734 + 3.000 + 8.3030 = 33.97635` (closes exactly)**.
- Geom-mean `√(E_micro·E_τ₀) = 4.843815×10⁻¹⁴ eV` (log₁₀ `−13.3148`), **misses center by
  7.1852 dex**.
- Misalignment `0.1·(φ_i/10¹⁷)²·(m/10⁻²²)^0.5`: at `m = 10⁻²²` eV,
  `φ_i = 1.095445×10¹⁷ GeV = 0.045 M_Pl,red` ⇒ `Ω h² = 0.120000`; slide
  `1.0954×10¹⁷ / 6.160×10¹⁶ / 3.464×10¹⁶ / 1.948×10¹⁶ GeV` for
  `m = 10⁻²²/⁻²¹/⁻²⁰/⁻¹⁹` eV.
- `λ_dB(10⁻²² eV) = 1.917 / 0.192 / 0.096 kpc` at `v = 10/100/200 km/s`.
- KMS: `N ≥ 0` and `S_h ≥ 0` across `ω = 10⁻²⁰…10⁵²` Hz; slopes `+1.000 / −1.000`; peak
  `ω = 1/τ₀ = 7.562×10⁻¹⁶ Hz`; window `max|d²logS_h| ≪ 1` (featureless).
- Cold onset `m/H₀ ≈ 6.9×10¹⁰ ≫ 1`. Order parameter `f(T_c) = tanh(½) = 0.4621172`
  (dimensionless). `f(T_c)·E_micro = 2.18×10⁻⁶ GeV` (22.7 dex below `10¹⁷ GeV`).
- Reverse-fit guard: center-hitting exponent `0.71148` (≠ `3/4`); `35.2%` of `a ∈
  [0.60,0.85]` land (3-dex-window artifact); seesaws `−64.28 / +37.65 dex`.
- grep for `V(φ)`/mass-term/VEV/condensate in `genesis_noise_kernel.py` +
  `closure_protocol.py`: **0 substantive hits**. `pole_spectrum.verify()`: all-True
  (incl. `current_GRUT_has_no_dark_mode = True`).

**Files (absolute):**

- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/cosmology/genesis_noise_kernel.py`
  (`:65-95` KMS noise, `:85-95` `S_h`, `:103-112` peak at `1/τ₀`, `:138-153`
  log-divergent variance, `:220-252` non-thermal shape)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/foundation/closure_protocol.py`
  (`:106` `ALPHA_VAC`, `:142` `S_SCREENING`, `:206` `TAU_0_SEC`, `:411` `TAU_MICRO_SEC`)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/toe/registry.py`
  (`:5340` pole_classification, `:5471` propagating_relic_pincer, `:5492` the
  "FOUNDATIONAL EXTENSION" remedy clause, `:5532` locality_no_halo)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/GRUT_GENESIS.md`
  (`:94` bath = substrate beneath vacuum, `:99` fluctuating-but-memoryless seed, `:125`
  cold relic must live in F(t), `:163` "current GRUT lacks", `:277-285` order parameter,
  `:444` "no equilibrium temperature of its own", `:502-508` numerology standard)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/GRUT_V4_SPINE.md`
  (`:311` substrate frontier, `:670` "different theory, not GRUT")
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/GRUT_DM_NONTHERMAL_COHERENT_TEST.md`
  (commit 836ffb4; `:41` `λ = ℏ/mv`; the outcome-(b) verdict this layer extends)

---

## Bottom line

The minimal F(t) condensate that hosts the GRUT dark-matter candidate is a **textbook
misalignment scalar** `V = ½m²φ²` placed in the substrate beneath the vacuum. Its honest
cost is **2 inserted dimensionful dials (`m`, `φ_i`) + 1 inserted potential shape; 0 of 3
requirements sourced from existing bath structure.** It is **no-go-clean** and
**Q/KMS-clean**, **GRUT — its substrate sector detailed — a CONJECTURAL deeper layer, not a
different theory and not a successor layer**, but **not a v4-core derivation** the moment
that is claimed — because it adds 2 free parameters, and because the bath, like the vacuum,
sources none of it. (The different-theory verdict belongs to the vacuum-pole route, not to
this substrate detailing.) The host exists, the bath cannot pay for it, and the exact price
is two numbers and a potential.
