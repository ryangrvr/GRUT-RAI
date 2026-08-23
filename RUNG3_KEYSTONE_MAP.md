# The rung-3 keystone map — clocks, free spectrum, the required self-energy, and what is already calculable

> **STATUS: NOTHING BANKED. NOT A CLAIM. NOT A RESULT.**
> The register (`provenance/claims.json`) is untouched by this file. No node added, no tier moved,
> no `ledger_delta` changed. This is an orientation/scoping document written **default-BROKEN** per
> CHARTER §1.4, and it may not be cited as content by any other artifact. Before any part of it
> enters the register it requires an adversarial pre-screen (CHARTER §1.3) and an overseer relay
> (CHARTER §5.3). Commissioned by the owner, 2026-08-21, following the stage-close addendum's
> finding that every *"Ht ≈ 1 versus Ht ≳ 4.3"* comparison filed into `rung3` compares two clocks
> without checking they are the same one.
>
> **No ledger net figure is typed anywhere in this document**; nets and counts ride
> `validate.py` / `emit_public_numbers.py` on their own faces, per the `PUBLIC_NUMBERS.md` rule.
> Filename note: commissioned as "RUNG3_KESTONE_MAP"; shipped at the correct English spelling.
>
> **SCREENED 2026-08-21** — hostile verification pass (embedding constraint checks, induced-metric
> check, invariant-reduction numerics) plus three refuter lenses against the owner's eight
> screening points. Two defects found and amended on this face (the static-patch embedding typo,
> §1.2; the D3 overstatement, split into D3a/D3b); C1–C3, C7, E6 and §6.1 re-scoped accordingly;
> one refusal recorded at §6.5. Record: `provenance/SCREEN_RECORD_2026-08-21_keystone_map.md`.
> Verdict there: **AMBER — amended, conditions listed; banking remains the owner's.**

## 0. The constraint this document works under

Binding on everything below (owner, 2026-08-21):

> Do not search for a way to make GRUT work. Search for the mathematically necessary bridge
> between the already-banked responsive-vacuum structure and the required low-frequency
> gravitational response. If the bridge cannot be derived from the existing priced inputs,
> identify the exact new input required and whether introducing it merely relocates the
> assumption. Do not promote a possibility to a result.

Accordingly this map does four things and no more: (1) **derive** the clock mapping the filed
comparisons skipped (§1); (2) state exactly what the free spectral computation established, at
its earned strength (§2); (3) name the self-energy object actually required (§3); (4) inventory
what already exists, labelled (§4). It resolves nothing by prose.

---

## 1. Clock normalization

### 1.1 The clocks currently in use

| clock | symbol | where it is used | how it entered |
|---|---|---|---|
| Cosmic time (flat patch), constant-H dS | `t`, ln a = Ht | `rung3_spectral_structure.py` (secular envelopes), `two_scale_desitter.py` (SY Langevin `dphi/dt`), conformalon N-arithmetic, `finite_T_pole_structure.py` dominance thresholds | the metric |
| E-folding counter | `N = ln a` | conformalon `⟨σ²⟩` growth (loop-sized *per e-fold*), the N=60 magnitude legs | the metric |
| Static-patch Killing time | `T` | `static_patch_tt_response.py`; the Gibbons–Hawking temperature T_dS = H/2π is defined **on this flow**; the state's KMS structure | the metric |
| FRW cosmic time now | `t₀`, H(z), H₀ | `rung7` τ₂ ~ 1/H₀; `mu_linear`, `isw_*`, `sigma0_anomaly_screen`, `gw_dissipation_bounds` (sub-horizon quasi-static) | the metric |
| Laboratory / tabletop | 689 Hz, T_lab | `rung8` energy-basis falsifier band | experiment |
| **The toy's stationary time** | unnamed | `finite_T_exponent.py`, `finite_T_pole_structure.py`: every integral assumes the kernel is a function of t−t′ | **imported with the QBM toy's stationarity assumption, never named** |

The last row is the load-bearing omission: the Matsubara-ladder result is a statement about a
*stationary* kernel, and stationarity in de Sitter holds w.r.t. one specific clock (D3 below).
Identifying the toy's silent `t` with cosmic time — or with Killing time — is an assumption the
toy does not state and has never paid for.

### 1.2 The transformations, derived rather than asserted

Embed both patches in the hyperboloid −X₀²+X⃗²+X₄² = H⁻². Flat patch: X₀ = H⁻¹sinh(Ht) +
(H/2)e^{Ht}x², Xᵢ = e^{Ht}xᵢ, X₄ = H⁻¹cosh(Ht) − (H/2)e^{Ht}x². Static patch: X₀ =
H⁻¹√(1−H²r²)sinh(HT), Xᵢ = rnᵢ, X₄ = H⁻¹√(1−H²r²)cosh(HT).
*[2026-08-21 screen correction: this line originally read Xᵢ = Hrnᵢ, which violates the
constraint — caught by direct numerical check; both embeddings now verified against the
hyperboloid and the flat induced metric equals diag(−1, e^{2Ht}) at sampled points.]*

- **(D1) On the axis, T = t.** At r = 0 (equivalently x = 0): sinh(HT)·H⁻¹ = sinh(Ht)·H⁻¹ and
  cosh likewise, so **T = t**; both are proper time on the same comoving geodesic, origins
  alignable. Derived, exact.
- **(D2) Off the axis there is no identification.** A static observer at fixed r ≠ 0 is
  accelerated — dτ_static = √(1−H²r²) dT ≠ dt anywhere off-axis — and that observer is not
  comoving in the flat slicing. The two foliations share only the axis. Consequently **w(z), a
  quantity of the cosmological background averaged over a comoving slice, is not an
  origin-worldline quantity**. *(2026-08-21 screen refinement: pointwise coordinate maps between
  the patches exist — both are time functions on the shared region — so the precise statement is
  NOT "no conversion exists" but "no conversion exists under which both descriptions retain
  their form": the stationary/spectral decomposition is preserved by no global map. See D3.)*
  Derived.
- **(D3) Stationarity, stated at the strength the numerics force** *(2026-08-21 screen
  amendment — the original blanket claim "no reduction w.r.t. cosmic time" was FALSE as stated;
  see the screening record)*. A de-Sitter-invariant G(x,x′) depends on the invariant
  z ∝ −(|Δη|−iε)² + |Δx⃗|², and the answer splits two ways:
  - **(D3a) Along any single comoving geodesic, the restricted correlator IS stationary in
    cosmic proper time**: for equal spatial positions z reduces exactly to z = H⁻²cosh(HΔt),
    independent of t₀ (verified numerically to 12 decimals). A one-time Fourier transform
    exists w.r.t. t ON THE WORLDLINE, and a geodesic detector sees BD thermally at T_dS = H/2π
    in that clock — the classical Gibbons–Hawking detector result, here derived from the
    embedding rather than cited. **Consequence: the QBM toy's silent cosmic clock is LICENSED
    for along-worldline kernels — at that scope only.**
  - **(D3b) For spatially separated pairs, z depends jointly on t₁+t₂ and Δt** (verified:
    same-Δt/different-t₀ pairs give distinct invariants), so **the FULL two-point object
    Σ(x;x′) does not reduce to a function of a time difference in any single global clock**;
    only the static patch offers a global reduction, because Killing stationarity makes z a
    function of T−T′ everywhere. Derived.
  *Re-scoped consequence:* the DISPATCH hold stands with a sharper reason — not "cosmic ω does
  not exist" (along worldlines it does, D3a), but "the assembled Σ(x;x′) has never been reduced
  to ANY one-time kernel; the available reductions are along-single-worldline (stationary,
  T = H/2π) or global static-Killing, and whether the gauge-invariant assembled TT response
  admits such a reduction is itself part of wall (A)'s assembly."
- **(D4) Rate conversions are local only.** For intervals Δt·H ≪ 1 (a ≈ const) a decay e^{−Γt}
  reads identically in T on the axis (by D1). Globally they disagree violently: with HT = e^{Ht}
  (axis, integrated from the D1 origin alignment), e^{−Γt} = (HT)^{−Γ/H} — a **power law in T**,
  not an exponential; conversely e^{−ΓT} is super-exponential in t. **Any comparison of rates
  across more than O(1/H) of elapsed time is clock-dependent.** Derived.
- **(D5)** N = H·t exactly on constant-H dS. In FRW, ΔN = ∫H dt requires the background history
  H(z) — an assumed input, w(z)-dependent. Derived / assumed respectively.
- **(D6)** T_dS = H/2π is the temperature of the Bunch–Davies state **with respect to the static
  Killing (boost) flow** — precisely the Bisognano–Wichmann/Sewell structure that
  `PRIMITIVE_INVERSION_SCOPE.md` §4.3 targets. Quoting coth(ω/2T_dS) against frequencies defined
  in any other clock silently transports a Killing-clock object across. The attribution is
  derived; **the transport itself is the assumption**, and it is currently unpaid.

### 1.3 Every conversion a filed comparison actually uses

| # | comparison as filed | source clock → target clock | transformation used (or skipped) | valid domain | derived / assumed | legitimate today? |
|---|---|---|---|---|---|---|
| C1 | "rung7 carries τ₂ ~ 1/H₀, i.e. Ht ~ 1; single-pole dominance needs Ht > 4.3" (`finite_T_pole_structure.py:262`) | toy-stationary t → FRW cosmic t₀ | *(re-scoped by the 2026-08-21 screen)*: D3a licenses the toy's cosmic clock for ALONG-WORLDLINE kernels, so pure clock-conversion no longer kills it; what remains: conflates *elapsed time since onset* with a *relaxation time*, imports dS-H history into an H₀ question (D5), and rung3's asserted object — the static-patch tower / assembled response — is not yet shown to be an along-worldline kernel (D3b + wall A) | recomputation in one named clock, plus the reduction question settled | partly licensed (D3a), partly assumed | **STILL NO — not as filed**, but for narrower reasons than first stated |
| C2 | rung3's ladder rate is "per static-patch Killing time" vs rung7's FRW cosmic time (stage-close addendum) | T → t₀ | D1 holds on the axis only; D2 limits any global map; **screen refinement**: the coth ladder's TEMPERATURE H/2π is the same in both stationary reductions (D3a, D6), so the ladder spacing H does not pick a clock — the Killing-clock concern attaches specifically to the static-patch tower family (E1), axis-only | axis for tower statements; worldline for noise-kernel statements | derived | the tension is REAL but its LOCUS moved: from "wrong clock" to "missing reduction + wrong object" |
| C3 | `RESULTS_finite_T.md` scale-map row: rung7 uses T = T_dS against ω ~ H(z) ("ω/ω* ≈ 3") | Killing-flow temperature → cosmic-time frequency ratio | none; D6 transport | local only; **weakened by D3a**: along a comoving worldline T_dS IS the cosmic-clock temperature, so this leg is now licensed for worldline kernels | now partly derived (D3a) | legitimate for worldline kernels; must still name that scope |
| C4 | conformalon ⟨σ²⟩ per e-fold, N = 60 ↔ DESI z ≈ 0 | N → t₀ | D5: exact on dS; needs H(z) history across matter era | locally fine at each epoch | partly derived, partly assumed | legitimate with the D5 caveat carried; magnitude conclusion unaffected by clock choice |
| C5 | mu_linear / ISW / σ₀-screen exclusions; GW dephasing bounds vs LIGO band | single FRW cosmic clock throughout | identity | sub-horizon quasi-static | derived | fine internally |
| C6 | static-patch tower rates (l+1)H quoted against anything cosmic | T → t | D4: exponential↔power-law mismatch beyond O(1/H) | axis, local | derived | fenced anyway by §2's retraction status |
| C7 | DISPATCH_ONE_PAGE pins ω to cosmic time ("ω conjugate to cosmic time… ln a = Ht") | t → ω_t | presupposes the reduction D3b shows has not been performed for the ASSEMBLED object; D3a licenses it only along single worldlines | worldlines only | **unperformed reduction, not a contradiction** | the HOLD stands; its stated reason should be upgraded to the D3a/D3b split |

### 1.4 What the clock audit changes for the stage's central adverse finding

The "Ht ≈ 1 versus Ht ≳ 4.3" tension is real **as a within-toy statement**:
`finite_T_pole_structure.py` prints it inside one stationary toy clock, where it is coherent.
*(2026-08-21 screen re-scope:)* its promotion to a rung7/rung3 contradiction was charged with
three defects, of which the screen **removed one**: pure clock-conversion (the toy's cosmic
clock is licensed for along-worldline kernels by D3a). What survives as defects — and they are
enough — are: (i) the elapsed-time-vs-relaxation-time conflation; (ii) dS-H history imported
into an H₀ question (D5); (iii) rung3's asserted object (static-patch tower / assembled TT
response) not yet shown to reduce to an along-worldline kernel at all (D3b + wall A); plus D4's
locality limit on any rate language. The addendum already ruled the recomputation outranks
everything else queued; this map sharpens what that recomputation must settle: **one named
clock AND the reduction question**, which either strengthens the adverse finding by surviving a
check nobody ran, or exposes an artifact of scope rather than of coordinate. It does not
perform it.

---

## 2. The free spectral object — exactly what is established

Object: the one-parameter family of radial master equations on the static patch,
f (f ψ′)′ + (ω² − V)ψ = 0 with V = f(r)·(l(l+1)/r² + cH²), f = 1 − H²r²
(`calc/static_patch_tt_response.py`), read against the state's KMS structure.

- **(E1) EXACT, symbolic.** For every c the series truncates to a polynomial at
  **ω_{n,l}/H = −i[ l + 2n + (3 ∓ √(1−4c))/2 ], n = 0, 1, 2, …** — discrete, purely imaginary,
  spaced exactly 2H in overtone index; residual of the ODE checked symbolically zero.
- **(E2) c-SELECTIVITY.** The integer bracket holds iff √(1−4c) is an odd integer, while β =
  2π/H is c-independent. A thermal cause cannot be c-selective: **the temperature is not what
  puts anything on the integers** (`PRIMITIVE_INVERSION_SCOPE.md` §9).
- **(E3) c = 0 IS THE AXIAL GRAVITON** — derived in-house by linearising R_mn = Λg_mn with an
  explicit-l odd-parity Regge–Wheeler ansatz (V = f·l(l+1)/r², c = 0 exactly). The polar sector
  is *reported* to share the master equation and is NOT verified here. Scope carried.
- **(E4) RETRACTED (2026-08-19), read first:** these frequencies are **NOT established as
  quasinormal**. The boundary check tested non-vanishing of a hypergeometric factor at the
  horizon, which does not establish outgoingness. The **free retarded response is pole-free**
  (pure dS is a trivial scattering problem whose amplitude is a finite Blaschke product).
  Status: **null, not adverse** — but also not structure the dynamics has exhibited.
- **(E5) Zeros, not poles.** The free response vanishes at the 2l+1 points |m| ≤ l — precisely
  where the state's ladder sits — and nowhere else. What survives is an infinite family indexed
  by multipole, lowest rate (l+1)H: **the node asserts *the* memory time; the free theory
  supplies a family.**
- **(E6) The ladder is the STATE'S, not the dynamics'.** coth(ω/2T) has simple poles at ω_n =
  −2πinT with uniform residue 2T = H/π, present for ANY J and any contour-closable regulator;
  with rung2's declared T = H/2π the spacing is exactly H. Matsubara frequencies are sampling
  points of the Euclidean correlator — G_E has no poles there; a retarded pole is a property of
  THE DYNAMICS and must lie in the lower half plane. Different objects. *(2026-08-21 screen
  fence added:* the KMS weight is CLOCK-FORM-UNIVERSAL — T_dS = H/2π governs both the global
  boost reduction (D6) and the along-worldline reduction (D3a); so "the state's ladder" names
  the state's temperature structure, while WHICH kernel manifests it is route-dependent per E7.
  The two boxed implications stand: free ladder ⇒ neither the memory pole NOR its impossibility.*)
- **(E7) Scope of (E6): the noise kernel only.** Whether the projected memory kernel inherits
  the ladder is TWO-ANSWERED (`mz_inheritance.py`, derived from definitions): the symmetrised
  route inherits it (J(iν) ≠ 0 everywhere on the imaginary axis closes the cancellation escape);
  the conventional Kubo–Mori route has **no ladder at all** (C_K = 2χ″/(βω): coth replaced by
  2/(βω)); the GLE friction kernel is temperature-independent outright. So rung3's phrase "the
  Mori–Zwanzig kernel" currently denotes no unique object — a defect in the node's STATEMENT,
  cheap to repair, owed before the ladder can bear on the conjecture at all.
- **(E8) The fence this section exists to enforce: FREE LADDER ≠ EFFECTIVE SINGLE POLE.**
  No parameter separates the leading term from the rest (gap and spacing both O(H); ratio O(1),
  no small quantity). Separation comes only by WAITING (contributions split as e^{−2Ht}), never
  by a parametric limit. "Parametrically suppressed" and "eventually negligible" are different
  claims and only the second is available.

---

## 3. The self-energy object actually required

Not "a graviton propagator." The target is fixed by rung3 and the dispatch brief:

> **ρ_TT(ω→0) = 2 Im G_R^TT(ω)**, equivalently η = lim_{ω→0} Im G_R^TT(ω)/ω,

obtained AFTER: (i) gauge-invariant assembly of source vertex + observer vertex +
external-mode-function corrections; (ii) IR resummation; (iii) analytic continuation ω → 0.

**Precondition surfaced by §1 (before pole-vs-cut even has meaning):** the assembled two-point
object must first be reduced to a kernel of a time difference **in a named clock**. By (D3) the
only clock in which that reduction is currently legitimate is the static Killing time — which
contradicts the dispatch's cosmic-time pinning (C7) and is the precise content of the HOLD.

**Named walls (unchanged from `DISPATCH_ONE_PAGE.md` / `SPECIALIST_BRIEF_rung3_spine.md`):**

- **(A) No graviton-probe assembly exists.** arXiv:2602.07908 (JHEP 04 (2026) 159) constructs
  the assembly for a **scalar probe**; the gravitational version changes the vertex rules, the
  reduction identities, and plausibly the diagram count. The scalar result cannot be borrowed.
- **(B) The resummation tool is half-discharged.** The h_μ0 untangling half of the
  arXiv:2409.12003 deferral was completed (arXiv:2507.04308); the **RG half was not**
  (`renormalization group` occurs zero times in its 24 pages; authors "enjoin caution"). The
  bare de Donder self-energy is gauge-dependent in the relevant sector (arXiv:1205.4468; TTW
  §4.3 states the gauge effect on the logarithms is unknown), so **the verdict cannot be read
  off the gauge-fixed object**.
- **(C) Graviton-loop premise correction (2026-08-10).** TTW's "no changes in the graviton mode
  function" is scalar-loop-scoped; for the graviton loop Table 8 is nonzero with ln(H²Δx²) —
  but it is the in-out (Feynman) object, not retarded; not exact; not usable at coincidence;
  and a position-space log is not time-domain secularity (needs the x′ integration of their
  eq. (109), listed by the epilogue as not done).

**Guards riding along (from the brief, mandatory):** do not manufacture a pole; do not
manufacture responsiveness; an early "my machinery cannot in principle produce this, and here
is which obstruction applies" is a first-class result that terminates the question cleanly.

---

## 4. What is already calculable — inventory at earned strength

Labels: EXACT / NUMERICAL / TOY / WRONG-CHANNEL / SCALING-ASSUMPTION / SUPERSEDED / RETRACTED /
BANKED. "Banked" = carried by a register claim; everything else is working material.

| file | object | label | status |
|---|---|---|---|
| `rung3_spectral_structure.py` | secular-envelope → low-ω dictionary (t^p → ρ; ln t → −2(γ+ln ω)/ω) | EXACT (self-test rel.err ~1e-13); BANKED as method | channel INPUTS SUPERSEDED — frozen-TT is scalar-loop-scoped; the O(G²) localization does NOT carry over to graviton loops unexamined; "both horns live" stands |
| `finite_T_exponent.py` | s_eff: 3 → 2 across ω* = 2T; DC floor → 0 as ω²; τ_ν cutoff-set | NUMERICAL TOY; BANKED | "soften, not break"; re-reporting it as a new defect would be fabricated — the repository already contains the answer |
| `finite_T_pole_structure.py` | Matsubara ladder ω_n = −2πinT, residues, leading-rung shares, regulator guard | EXACT residue analysis (noise-kernel scope) | ladder hidden from τ_ν (weighted-mean diagnostic answers another question); MZ-inheritance step explicitly NOT taken here |
| `mz_inheritance.py` | inheritance question answered TWO ways | DERIVED from definitions | symmetrised route inherits; Kubo–Mori route has no ladder; friction kernel T-independent — rung3's kernel phrase denotes no unique object; repair owed |
| `static_patch_tt_response.py` | master-equation family, truncation frequencies, c = 0 axial graviton | EXACT symbolic; **QNM reading RETRACTED** | free response pole-free (Blaschke); zeros at |m| ≤ l; tower conditional |
| `two_scale_desitter.py` | OU moment ODEs, τ_relax = 3H/m²; SY dynamical mass m²_eff ~ √λ H² | CLOSED-FORM + numerical check | horizon-FORCED: existence of a relaxation; INSERTED: the timescale τ₂ ~ 1/H (needs λ ~ O(1), exactly where the weak-coupling SY attractor is unverified) |
| `conformalon_joint.py`, `conformalon_q2_band.py` | one-Q² double-duty; Q²_SM ≈ 5.53; prefactor ratios k_w/k_α | GROUNDED prefactors; hypothesis DECIDED | outcome C — closed: w = +1/3 (wrong EOS), w-deviation ~8× below DESI, k_α plausibly zero; the "near-hit" was a dropped-prefactor artifact |
| `wz_dark_energy.py` | relaxor w(z) = −1 + ε(Hτ)²/(1+(Hτ)²) | HEURISTIC TOY | w_a sign RETRACTED (frontier-indeterminate); ε staked at 0.4 with source disclaiming the form; robust content = no-crossing + needs ≥2 modes; UV memory gives w ≡ −1 flat |
| `gw_dissipation_bounds.py` | GW dephasing / v_g ≠ c orders of magnitude | COMPUTED | 22–62 orders (exponent-units slip repaired post-close); EDIT 1 in `handover/REGISTER_EDITS_DRAFT_2026-08-20.md` makes invisibility CONDITIONAL — amplitude channel uncovered, sector question open |
| `mu_linear.py`, `sigma0_anomaly_screen.py`, `isw_exclusion.py`, `isw_tt_auto.py` | μ = 1 + xα growth family; ISW / σ₀ exclusions | COMPUTED EXCLUSIONS | μ = 4/3 excluded (~2σ t-g cross + ~3.5σ lensing, post-retraction); ceiling b on x but NO floor (no-pin theorem); FRW cosmic clock throughout (row C5) |
| `anomaly_c0_map.py` | anomaly-induced kernel c₀ = α? | COMPUTED NULL | local R², ≥108 decades below any bound; amplitude/sign degenerate with a free counterterm — fixes a scale, not a number |
| `q1_energy_basis_magnitude.py`, `energy_basis_decoherence.py` | tabletop falsifier magnitude | COMPUTED NEGATIVE | quiet-or-faint: diagonal coupling S(0)=0, off-diagonal 7–47 orders below detectability; rung8 FAILS-DIFFERENTIATION |
| `kk_static_transfer.py` | the ω → 0 static **modulus** | DIFFERENT OBJECT | name collision with the static **patch**: shares no object with `static_patch_tt_response.py` (the program's fifth colliding name) |

The pattern the labels encode: every apparently promising spectral shortcut run so far —
secular-log ⇒ cut (**wrong channel**, and the assembled object was never computed), the
Matsubara-coincidence ⇒ pole reading (**the state's coth, not dynamics; c-selective**),
gapped-tower ⇒ QNM (**the boundary check tested the wrong thing**) — was killed by exactly the
distinctions this map pins in place. Keep them fixed.

---

## 5. The keystone question

Once §1's clock is named and §3's assembly exists, the question is single:

> **Does the gauge-invariant, resummed gravitational G_R^TT(ω) develop a pole, a cut, or
> neither?**

Three outcomes, all first-class, none predetermined:

- **POLE** → then ask whether its location/residue dynamically supplies the required memory
  scale — with τ₂ ~ 1/H₀ stated in the SAME clock the pole is defined in; §1's map decides
  whether that comparison is legitimate.
- **CUT / continuum** → then determine whether the low-frequency behavior can produce the
  required memory kernel.
- **NEITHER** → then determine whether the memory architecture survives through some other
  mathematically justified structure — or terminates. That is a result, not a loss.

What is forbidden: predetermining which outcome GRUT needs; importing the answer from a
gauge-fixed or scalar-probe surrogate (walls A–C); promoting any §4 toy to evidence here.

---

## 6. The primitive-inversion connection — why `PRIMITIVE_INVERSION_SCOPE.md` §4.3 and rung3 are one question

1. **The ladder follows the STATE'S TEMPERATURE, not a chosen clock.** *(2026-08-21 screen
   refinement of the original "the modular clock IS the ladder's clock" — that sentence was an
   interpretation, not a derivation, and D3a forced its weakening.)* Bisognano–Wichmann/Sewell:
   the modular flow of the Bunch–Davies state is the static-patch boost/Killing flow, KMS by
   construction; but D3a shows comoving geodesics see the SAME temperature in cosmic proper
   time. So T_dS = H/2π governs every legitimate stationary reduction, and the ladder spacing H
   follows the temperature into whichever reduction you form. What the inversion would actually
   fix is unchanged and stays where `PRIMITIVE_INVERSION_SCOPE.md` §5 puts it: whether the flow
   THE KERNEL USES is the state's modular flow — the one break point that neither this map nor
   D3a touches.
2. **The register lacks the vocabulary this whole audit needs.** The addendum's finding stands:
   no register field mentions foliation, cosmic time, or proper time — which is how the C1/C2
   mismatch passed two pre-registrations. A successful inversion FORCES that vocabulary into
   existence (the flow must be named to be discharged); an honest rung3 recomputation forces the
   same vocabulary from the other side. Two documents, one repair.
3. **The break point stays where §5 of that document puts it.** The framework's system/bath
   split and its cosmological exports (μ_linear, w(z)) live naturally on the COSMIC clock;
   modular/KMS structure lives on the STATIC clock; D2 shows these coincide only on the axis,
   while w(z) is not an axis quantity. Bridging them is either a theorem (derived) or a new
   priced input (§7's test). This is "where it most likely breaks," as that document itself says.
4. **K3 remains the presumed outcome**, and the anti-scope-creep clause is respected: this map
   works neither the inversion nor the self-energy — it only shows they are the same bottleneck,
   so the inversion cannot be treated as a separate philosophical exercise from the keystone.
5. **REFUSAL, recorded so it is not re-raised from the flattering direction** *(2026-08-21
   screen)*: nothing here claims response theory can INVERT to a unique microscopic/modular
   primitive. Mori–Zwanzig coarse-graining is many-to-one — the influence functional fixes only
   certain bath correlators, and distinct microscopics wash to the same low-frequency kernel —
   so "response ⇒ unique primitive dynamics" is almost certainly false as stated. The defensible
   version is the classification question already fenced at u4/u5 (which constitutive classes
   are compatible), held default-BROKEN with first-class failure states ("no / only-one-class /
   reduces-to-known" are results). An invertibility claim would be a NEW question requiring its
   own scoping document, its own pre-registration, and a burden of proof this program's own
   history says it will not meet cheaply.

---

## 7. The bridge test — discharge or relocate

Every candidate input that would carry the free theory to the keystone gets one question:
does introducing it DERIVE the low-frequency response, or RELOCATE the assumption?
Precedents already in the record fix the pattern:

- **p_tt escape route:** a bath-microphysics commitment making ⟨T^μ_μ T^ν_ν⟩_R vanish would
  flip CHOSEN → FORCED — priced as a NEW +1 at its point of entry (rung3). Relocates; does not
  discharge.
- **conformalon:** tracking removes the mass-tuning but relocates the onset coincidence into a
  structural bundle (light IR mode + O(1) coupling + broken shift symmetry); the double-duty
  version then closed on three independent grounds anyway.
- **noise transversality:** derived ON the booked family, CONDITIONAL on rung1's fourth input —
  the relocation paid openly at entry.

Rule going forward: any "the bath will select the TT corner / the pole" claim enters the
register at its point of entry with its price, or it is laundering. And per §0's constraint,
the TT question stays SEPARATE: symmetry rhetoric for TT-only is closed (Weyl-broken by the
program's own anomaly import; EH counterexample exact), P^(0s) remains admissible, and the live
question is whether microscopic bath dynamics selects the constitutive corner dynamically —
a classification question homed at u4/u5, not a derivation to be resurrected.

---

## 8. Guards

1. **Nothing here banks.** No register edit is licensed by this file; every §1–§4 statement is
   either already in a cited calc's write-up or is derived here and unbanked by construction.
2. **Clock statements are derived or they are not made.** Any future comparison of two rates
   must name both clocks, cite D1–D6, and state the locality domain — no prose resolutions.
3. **The free-ladder ≠ single-pole fence (E8) rides on every use of §2**, and E4's retraction
   status rides on every use of the static-patch frequencies.
4. **Three outcomes, equal standing.** Directional-optimism rule (CHARTER §1.4) applies hardest
   to POLE — the outcome the program wants.
5. **No net figures typed here**; nothing for `test_doc_sync.py` to guard that it does not
   already guard.
6. This file may not be cited as content by any artifact until screened (CHARTER §1.3) and
   relayed (CHARTER §5.3).

## 9. The near-term deliverables this map orders

1. **The one-clock recomputation** (C1/C2): recompute rung3's tower-separation requirement and
   rung7's τ₂ requirement in one named coordinate; file whichever way it lands.
2. **Repair rung3's kernel-phrase defect** (E7): name which MZ object the node means, before
   any ladder-based argument is filed against it again.
3. **`calc/gw_tensor_friction.py`** — unchanged as the near-term deliverable; it inherits C5
   (single clock) and EDIT 1's conditional marker untouched.
4. Only then: the keystone itself (§3's object), whose walls (A)–(B) are outside this program's
   in-house reach by standing rule — the dispatch re-pose, not a new in-house month.

