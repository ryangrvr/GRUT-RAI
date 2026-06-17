# The low-ℓ CMB ISW and the equality-scale quasi-static filter

**Status:** computed and validated (full relativistic MGCAMB), June 2026.

> ───────────────────────────────────────────────────────────────────────
> **⚠ FINAL VERDICT — READ §0.1 FIRST (supersedes the headline below).** The k_eq
> filter "removes the tension" headline is OBSOLETE. The full derived memory kernel
> was implemented in MGCAMB and gives **2.79× at ℓ=15 (~32σ) — it does NOT rescue**;
> the memory only *delays* the enhancement (μ→4/3 by z≲15). The linear-scalar
> refractive enhancement is **RULED OUT** on two fronts: data (§0.1) and consistency
> (`PROJECTOR_CONSISTENCY_NOGO.md §5`: μ_linear=1 forced ⟹ linear cosmology = ΛCDM).
> The dark sector must be nonlinear/tensor (C5a–C5c). The §3 k_eq filter below is a
> retained-for-record phenomenological proxy with "no physical basis" (§0.1), NOT a fix.
> ───────────────────────────────────────────────────────────────────────

**Headline (SUPERSEDED — see banner):** GRUT's instantaneous sub-Hubble filter over-predicts
the low-ℓ CMB by ~2.6× (≈29σ); a zero-free-parameter, physically-derived refinement using the
matter–radiation **equality horizon k_eq** removes the tension entirely while
preserving σ₈ and BAO. This converts an apparent falsification into a sharp,
testable prediction and a well-posed theory task.

> ───────────────────────────────────────────────────────────────────────
> **UPDATE (deeper finding — read §0).** The k_eq filter below is a *phenomenological
> proxy*. The real physics: the quasi-static (QS) reduction that gives
> μ = 1+α/(1+(τ₀k_phys)²) is **invalid for the ISW-driving modes** — and the
> derivation's justification for QS rests on an **arithmetic error**. The low-ℓ
> excess is therefore NOT a robust falsification; it comes from using the QS law
> outside its domain. The k_eq filter approximately removes exactly those QS-invalid
> modes. The correct fix is the full memory kernel (the open task). See §0.
> ───────────────────────────────────────────────────────────────────────

## 0. The QS reduction is invalid for the ISW modes (the deeper finding)

GRUT is a **memory-response** theory; the fundamental object is the retarded kernel
G^R(k,η,η'), not the quasi-static μ(k,a). The formula μ = 1+α/(1+(τ₀k_phys)²) is the
**QS reduction** of that kernel (frw_explicit.py / Phase 2C), obtained by dropping the
time-derivative terms ∂_η²+2H_c∂_η in the relaxation operator 1+τ₀²(−□_g). That step is
justified there by the claim **(τ₀H)² ≪ 1 at all epochs**, including "(H_eq τ₀)² ≈ 10⁻⁶".

**That claim is an arithmetic error.** The correct value at equality (z≈3400) is
(τ₀H_eq)² ≈ **2×10⁵** — eleven orders of magnitude off. (τ₀H)² = 1 at **z ≈ 77**, so:

| z | 0 | 10 | 30 | **77** | 200 | 3400 |
|---|---|----|----|----|-----|------|
| (τ₀H)² | 8×10⁻⁶ | 3×10⁻³ | 0.08 | **1.3** | 23 | 2×10⁵ |
| QS valid? | yes | yes | marginal | **fails** | no | no |

So the QS reduction holds for z ≲ 30 and **fails for z ≳ 77** — exactly the epoch when the
low-ℓ ISW modes' enhancement turns on (a★ = k·L₀, z★ = 1/(kL₀)−1).

**Solving the full (non-QS) memory operator** σ'' + 2H_c σ' + [a²/L₀² + k²]σ = (a²/L₀²)S
and comparing the response R = σ_full/σ_QS confirms a clean split by z★:

| k [Mpc⁻¹] | z★ | R = σ_full/σ_QS | regime |
|---|---|---|---|
| 0.1 | <0 | 1.000 | QS exact — σ₈/clustering |
| 10⁻² | 7 | ≈1.00 | QS valid — BAO/σ₈ |
| 3×10⁻³ | 25 | 1.07–1.25 | QS breaking |
| 10⁻³ | 77 | oscillatory, ≠ μ=4/3 | **QS broken — ISW modes** |

**Conclusion.** The QS law μ=1+α/(1+(τ₀k_phys)²) is valid exactly where GRUT was tested
(growth, σ₈, BAO — k ≳ 10⁻²) and **invalid exactly for the modes that source the low-ℓ
ISW** (k ≲ 3×10⁻³). The 2.6× excess and ~29σ "falsification" are artifacts of applying
the QS reduction outside its domain — NOT a clean prediction of GRUT's full memory theory.
The k_eq filter (§3) is a crude proxy that removes those QS-invalid modes; the *correct*
treatment is the full retarded kernel.

**RESOLVED (the ToE step — see grut/derivation/phi_munu/retarded_kernel_frw.py):**
The retarded-kernel structure is now derived from GRUT's own CTP, settling both forks:

- **Fork 1 — first-order, not second-order.** GRUT's susceptibility is the single-pole
  χ(ω) = 1/(1 − iωτ₀) (linearized_ctp_action.py, eq. line 59 — the FT of exponential
  relaxation), the bedrock law τ dz/dt+z=z_target is first-order ("Route 1: CTP variation"),
  and the FDT noise is Ohmic (dissipation rate 1/τ). The second-order 1+τ₀²(−□_g) in
  frw_explicit.py is the WRONG covariantization — it imposed Lorentz invariance (a ∂_η²
  wave term) on a medium that has a rest frame. Correct: 1−iωτ₀ → 1+τ₀ uᵘ∂ᵤ (first-order,
  along the cosmic 4-velocity).
- **Fork 2 — the intensive susceptibility χ relaxes toward its static equilibrium χ_eq(k).**

**Master equation (zero free parameters):**

    (L₀/a) ∂_η χ(k,η) + χ(k,η) = 1/(1+(L₀ k/a)²) ,   μ = 1 + α χ ,   L₀=τ₀c, α=1/3.

It factorizes as χ(ω,k)=χ_eq(k)/(1−iωτ₀): the QS limit (∂_η→0) reproduces frw_explicit.
The relaxation lag makes χ < χ_eq during fast turn-on (τ₀H≳1, z≳77), but by z≲15 the
relaxation has caught up and χ→χ_eq=1 ⇒ μ→4/3 in full.

## 0.1 FULL-BOLTZMANN VERDICT (the derived kernel does NOT rescue — Possibility A)

The derived kernel μ=1+αχ was implemented exactly in MGCAMB (mugamma_par==5, χ(k,a)
tabulated from the master eq; γ=1; validated: GR-limit = stock CAMB, ratio→1 at ℓ=220,
σ₈ preserved +2.8%). Result:

  D_ℓ^GRUT/D_ℓ^ΛCDM = 2.79× at ℓ=15 (~32σ) — i.e. the derived memory kernel gives a low-ℓ
  ISW excess slightly LARGER than the ad hoc f_subH version (2.6×), NOT smaller.

Why the memory doesn't rescue: the relaxation lag DELAYS the enhancement but μ still reaches
4/3 by z≲15, so versus ΛCDM the potential still deepens fully and the ISW is still large.
The earlier "R=χ/χ_eq<1 ⇒ suppression" was relative to the no-filter QS value, not to ΛCDM.

The source-coupling avenue (the last derivable hope) also fails: MGCAMB's μ multiplies the
gauge-invariant comoving density rhoDelta = δρ + 3aH·(δq)/k — the real local overdensity,
already (k/aH)²-suppressed super-horizon (this is in the 2.79× result). The ISW-driving modes
(k~10⁻³, ℓ~14) enter the horizon at z~60 and are FULLY sub-horizon throughout the ISW-sourcing
epoch (z<60), so their comoving overdensity is real and unsuppressed; the medium responds in
full. No k_eq cutoff is derivable: it would require the medium to ignore genuine, causally-
assembled, sub-horizon overdensities — no physical basis.

ROOT CAUSE (irreducible): GRUT's static susceptibility χ_eq=1/(1+(τ₀k_phys)²) → 1 (μ→4/3) as
k→0. This super-horizon saturation IS the large-scale dark-sector enhancement (and it is the
physically natural DC response of a viscoelastic medium). The same μ→4/3 that gives σ₈/dark
phenomenology over-produces the low-ℓ CMB ISW by ~3×. The temporal memory delays it; the
gauge-invariant source suppresses only super-horizon (not the sub-horizon ISW modes); neither
removes it.

**HONEST VERDICT.** The low-ℓ CMB is a genuine falsifier for GRUT's *derived* linear-cosmology
response (the large-scale μ→4/3). σ₈ / BAO / fσ₈ (sub-horizon, k≳10⁻²) are UNAFFECTED and
still stand. The k_eq filter (§3) that achieves CMB-consistency is NOT derivable — it is a
phenomenological cut on genuine sub-horizon overdensities. For GRUT's linear sector to survive
the CMB, the *derivation of χ_eq itself* would have to change so that the susceptibility
vanishes (μ→1), rather than saturates (μ→4/3), as k→0 — a different constitutive structure
than the one the framework currently derives.

Result files: grut/derivation/phi_munu/retarded_kernel_frw.py (master eq, verify() passes),
~/mgcamb_grut (mugamma_par==5 build + chi_table.dat + grut_isw_run.py).

## 0.2 MEMORY-SOURCE TEST (the self-referential rescue) — also fails

Final rescue candidate (disciplined version): instead of inserting a scale, let the source be
the kernel-integrated formation history, J(k,a)=∫ W(a,a') δ_m(k,a') da', with W FIXED by the
GRUT relaxation kernel (τ₀ż+z=z_target) — NOT chosen to fit. Test: does k_eq emerge on its own?

Result: NO. The memory-source effective μ = 1+α·σ/δ_m (σ relaxing toward the QS response with
the real growth history inside) is identical to the QS μ to 0.2% at z=0, and μ−1→0.333 (μ→4/3)
as k→0 — no k_eq feature.

Reason — the MEMORY REACH. For k_eq (set at equality, age 0.05 Myr) to be imprinted, W must
reach back to equality at the epoch the ℓ~14 ISW is sourced (z<60, age >470 Myr). GRUT's memory
time τ₀=41.9 Myr reaches back only ~42 Myr there — a sliver. The source's equality structure is
invisible to the kernel at the sourcing epoch (reaches z=11 at z=10, z=0 at z=0).

DEEP STRUCTURAL POINT: τ₀ is a LOCAL relaxation time (the same 42 Myr that sets the 689 Hz
decoherence plateau and the cluster/σ₈ sector), NOT a cosmological-history timescale. It is
pinned at 42 Myr by the structure sector, and that value is ~10⁴× too short to act as the
cosmological memory a k_eq rescue would need. One constant cannot play both roles.

## 0.25 OPEN QUESTION: The Constitutive Source Principle (the next-phase question)

**Status:** open — the load-bearing question for GRUT's linear-cosmology sector after the
low-ℓ CMB falsification. Not parameter tuning; a structural question about the source vertex.

**The locus.** GRUT's constitutive field σ is sourced by the matter overdensity via the
conformal-trace coupling S_IF ⊃ ∫ α_vac σ_a δT_m, δT_m = −δρ_m — the "P3.1 coupling form."
This is an ASSUMED form: the CTP action fixes the medium (σ, kinetic+relaxation kernel) and the
vertex magnitude (∂²S/∂σ∂ρ = −α_vac, registry: matter-gravity CTP coupling vertex), but the
coupling FORM (σ ← δρ, with θ_m "absent at bare-action level") is posited, not derived. Every
density-based mechanism inherits density's low-k behavior (χ_eq→1, μ→4/3 as k→0), which
over-produces the low-ℓ ISW. Propagators, kernels and filters cannot fix a wrong low-k SOURCE.

**The question.** Should σ couple to a measure of *realized relational structure* —
decohered/crystallized, formation-history-dependent — rather than the bare density contrast?

**Where GRUT already contains this (CTP-internal, not bolted on).** The CTP action has two
sectors: RETARDED (response/dissipation — the current σ←δρ source) and KELDYSH/NOISE (the kernel
N, FDT-related — DECOHERENCE). "Information / distinction / entropy production / realized
structure" is the language of the NOISE sector — and GRUT's own decoherence machinery
(Λ_grav = Gm²S/(ℏℓ), crystallization of definite structure, the 689 Hz plateau,
Schrödinger-in-the-box) IS that sector. Natural reformulation: the medium's gravitational
response is sourced by DECOHERED/CRYSTALLIZED structure (noise-sector measure), not the bare
quantum density (retarded-sector source). Coherent un-collapsed super-horizon modes are not
"realized structure" → no source; collapsed galaxies/clusters (decohered) → full source. This
would UNIFY the cosmological sector with the decoherence sector GRUT already stands on.

**The τ₀ reinterpretation.** The memory-source miss by ~10⁴ is the discovery that τ₀ is the
local DECOHERENCE/relaxation time (the same 42 Myr as the 689 Hz plateau and cluster/σ₈ sector),
NOT cosmic memory. The cosmological "realized structure" measure must be EXTENSIVE and
history-accumulated (decoherence accumulated / entropy produced), not the intensive local τ₀.

**Criteria any successful completion must meet (derived, not tuned):**
1. Reduce the source as k→0 (no large-scale over-response).
2. Preserve the σ₈ enhancement.
3. Preserve BAO and growth observables.
4. Emerge from the CTP action (the noise sector), not an imposed filter.
5. Introduce no arbitrary cosmological scale.

**What this is NOT:** not a filter, not a tuned k_eq, not a longer τ₀. The hypothesis is that the
source VERTEX is incomplete — σ←δρ is the leading (retarded-sector) approximation, valid in the
structure regime but failing on un-realized super-horizon scales where the noise-sector
(realized-structure) source should dominate.

### First-step result (investigation opened): noise-sector source = quadratic; fixes k→0 structurally

Structural fact: the retarded sector gives a LINEAR coupling (σ←δρ, response to the density
field); the Keldysh/NOISE sector is the symmetric correlator ⟨δρ δρ⟩ — intrinsically QUADRATIC,
i.e. the variance Δ²(k)=k³P(k)/2π² (the realized-structure / structure-content measure). Tested
against the five criteria (shapes from stock-CAMB ΛCDM P(k)):

  Δ²(k):  CMB(k=1e-3)=9e-7,  k_eq=4e-3,  BAO(0.04)=0.12,  σ₈(0.3)=1.8.

- (1) source→0 as k→0: ✓ AUTOMATIC (Δ²∝k^{3+ns}→0; BAO/CMB ratio ~1e5). No inserted scale.
- (4) emerges from CTP action: ✓ — the variance IS the Keldysh/noise two-point function.
- (5) no arbitrary scale: ✓ — turnover is the matter-P(k) shape (derived), not inserted.
- (2)(3) preserve σ₈/BAO: AT RISK — the variance rises toward SMALL scales, INVERTING GRUT's
  enhancement profile (the falsified μ→4/3 was large-scale-weighted; a variance source is
  small-scale-weighted). σ₈ (Δ²~1.8) strongly weighted, BAO (Δ²~0.12) weakly. Whether σ₈/BAO/
  Ω_dm are reproduced hinges on the coupling MAGNITUDE — must be DERIVED, not fit.
- Decoherence-RATE candidate Λ_grav~⟨δρ²⟩/k²: RULED OUT (stronger at large scales, wrong way).

INTERPRETATION: a small-scale/structure-weighted dark response may be MORE faithful to GRUT's
"dark matter = impedance of realized structure" than μ→4/3 (realized structure = collapsed,
small-scale). The noise-sector source removes exactly the large-scale piece that (a) falsified
the CMB and (b) sat least comfortably with that philosophy.

STATUS: structurally promising (criteria 1,4,5 met without tuning) but NOT yet supported
(criteria 2,3 unverified). NEXT SUB-STEP: derive the noise-sector coupling strength/form
(σ ← Keldysh ⟨δρ²⟩) from the CTP action, then test σ₈/BAO/Ω_dm — derived, not fit.
(Computation: variance shapes vs criteria, this session's transcript.)

### Sub-step DONE: the noise vertex DERIVED (Keldysh rotation, exact, symbolic)

Keldysh-rotate the conformal vertex g σ φ² (σ couples to the matter density bilinear φ²):
    g[σ⁺φ⁺² − σ⁻φ⁻²] = (g/√2)[ σ_q φ_c²  +  2 σ_c φ_c φ_q  +  σ_q φ_q² ].
δS/δσ_q = 0 (macroscopic σ_c EOM) + Wick contraction (⟨φ_qφ_q⟩=G^K=⟨δρ²⟩, ⟨φ_cφ_q⟩=G^R, φ_c²=ρ_cl):
    [retarded op] σ_c = (g/√2) ( ρ_cl + ⟨δρ²⟩ ).

RESULT: the variance G^K=⟨δρ²⟩ (realized structure) sources σ_c at EQUAL strength (g/√2) with the
classical density — both from the SAME vertex (NOT an α²-suppressed correction). The old linear
coupling reappears as the σ_c φ_c φ_q → G^R RETARDED response (the ISW culprit), now seen as one
of three Keldysh pieces, not the whole source.

CMB-RESOLUTION MECHANISM (CTP-internal, not a filter): the classical source ρ_cl=φ_c² requires a
REALIZED (decohered) classical field φ_c. Un-realized modes (coherent, super-horizon → no φ_c) are
sourced ONLY by ⟨δρ²⟩, which →0 as k→0. So the classical (CMB-falsifying) source switches OFF
exactly where matter is un-realized, leaving only the k→0-vanishing variance. The realization gate
is GRUT's own decoherence (Λ_grav crystallization) → unifies the cosmological source with the
decoherence sector. Satisfies criteria 1,4,5 by construction.

CRUX (next sub-step, falsifiable): requires GRUT's Λ_grav realization to NOT crystallize
super-horizon modes (so ρ_cl is off there) — DIFFERENT from standard inflationary decoherence
(which classicalizes super-horizon). Make the realization gate quantitative (does Λ_grav realize a
super-horizon mode?); then test σ₈/BAO/Ω_dm with ρ_cl gated on for collapsed structure (criteria
2,3). (Symbolic derivation: this session's transcript.)

### Step 4 (FRW normalization / magnitude) DONE — corrects the shape argument

The noise vertex sources σ_c with the COMPOSITE operator δρ² (ρ~field²). Its source power is the
SELF-CONVOLUTION (one-loop bubble) P_{δρ²}(k)=2∫d³q/(2π)³ P_δ(q)P_δ(|k−q|), NOT the per-log
variance Δ²=k³P. Computed (stock-CAMB P(k)):
  P_{δρ²}(k):  k=1e-4→2.65e4,  1e-2→2.64e4,  0.1→1.88e4,  0.3→0.84e4  [Mpc³]
=> k→0 WHITE-NOISE FLOOR P_{δρ²}(0)=∫P²d³q≈2.65e4 Mpc³ — does NOT vanish. The earlier "source
vanishes at k→0" used the WRONG quantity (per-log Δ², not the source power). CORRECTED.

BUT σ_c is the conformal mode (a metric/potential perturbation ∝ source, no 1/k² Poisson step), so
Φ_med ∝ δρ²/(1+(τ₀k_phys)²) and the DIMENSIONLESS potential power Δ²_Φ ∝ k³P_{δρ²}(k) is BLUE
(1.3e-9 at k=1e-4 → ~11 at k=0.3). Blue ⇒ phase-space-suppressed at low ℓ ⇒ CMB-SAFE — but for a
DIFFERENT reason than hoped (blue tilt, not source-vanishing).

STRUCTURAL VERDICT: the noise response Δ²_Φ∝k³P_{δρ²} is PEAKED at collapsed/nonlinear scales
(k~0.3-1, δ²~O(1)) and dies at large scales. It is CMB-safe ✓ and literally "impedance of realized
(collapsed) structure" ✓ — but it is QUADRATIC/STOCHASTIC/non-Gaussian (δρ²-sourced), NOT a linear
μ(k). GRUT's σ₈/BAO/fσ₈ successes are LINEAR observables requiring a LINEAR μ — exactly the piece
that fails the CMB. So the magnitude calc RELOCATES the tension:
  • linear μ → gives linear σ₈/BAO ✓, fails CMB ✗
  • noise source δρ² → CMB-safe ✓, nonlinear/collapse-weighted, does NOT give linear σ₈/BAO ✗

PREFACTOR STATUS: loop SHAPE computed rigorously (convolution, floor, blue tilt). Exact numerical
prefactor g²·(floor 2.65e4 Mpc³)·(FRW a-factors) CHARACTERIZED but NOT closed — a first estimate
shows a normalization puzzle (g~O(1) gives a too-large response), so the FRW mode-function
normalization must be done carefully (the genuine remaining "actual math"). Structural findings
(floor-not-vanishing, blue→CMB-safe, nonlinear mechanism) are robust regardless.

NEXT: (i) close the FRW mode-function normalization for the exact prefactor; (ii) determine whether
a nonlinear δρ²-sourced response can mimic the LINEAR σ₈/BAO, or whether the linear-μ↔CMB tension
is irreducible. (Computation: self-convolution loop, this session's transcript.)

### MIMICRY TEST DONE — the nonlinear response does NOT mimic linear σ₈/BAO/fσ₈

Q: does the quadratic δρ²-sourced response manifest as an effective LINEAR clustering enhancement
(flat ΔP/P, mimicking +3% σ₈), or as a distinct nonlinear signature (scale-dependent)?

The medium one-loop power correction shape (σ_c is a direct conformal potential ∝δρ² ⇒ matter
source carries k² from −∇²Φ; bubble P_{δρ²}=convolution):
   ΔP_med(k)/P(k) ∝ k⁴/(1+(τ₀k_phys)²)² × P_{δρ²}(k)/P(k)
Computed (stock-CAMB), normalized to peak:
   BAO(0.04)→0.002,  σ₈(0.1)→0.04,  (0.2)→0.18,  (0.3)→0.33,  k≳0.5→1 (deeply nonlinear).
Variation across BAO→σ₈ ≈ factor 100 (FLAT would be ~1). STRONGLY BLUE; rises into the nonlinear
regime; NEGLIGIBLE at the quasi-linear scales where σ₈/fσ₈/BAO live.

VERDICT: NO linear mimicry. The nonlinear noise response does NOT reproduce GRUT's linear σ₈/BAO/
fσ₈ successes (those required the linear μ — CMB-falsified AND CTP-inconsistent). The distinct
signature sits at k≳0.5 Mpc⁻¹ (deeply nonlinear; SPT breaks down, baryons dominate) — not a clean
quasi-linear DESI/Euclid target.

STRUCTURAL CONCLUSION (most consequential of the investigation): GRUT's linear-cosmology evidence
base (σ₈ +3%, fσ₈, BAO) does NOT survive the theory's own CTP source structure — those were the
LINEAR approximation of a fundamentally QUADRATIC source. The CTP-consistent source is CMB-safe but
nonlinear and weak at quasi-linear scales. So the linear "wins" were unphysical artifacts; what GRUT
robustly predicts in the linear regime is CMB-consistency (by being quadratic/blue) + a weak
small-scale nonlinear signature, NOT the headline linear matches.
CAVEATS: the blue tilt (and the CMB-safety) both follow from Φ_med∝δρ² (direct potential, k² in
matter source) — self-consistent. The nonlinear-peak amplitude is past one-loop-SPT validity, but
the quasi-linear SMALLNESS (k≲0.3) that kills the mimicry is robust. (Computation: this session.)

### Slip test (μ vs Σ) — also does NOT fix it; reveals the robust growth↔Weyl↔ISW law

Hypothesis: we assumed γ=1 (Σ=μ) throughout; GRUT being VISCOELASTIC should have shear =
anisotropic stress = slip (γ≠1). Test μ→4/3 (pure χ_FRW, no filter) with γ=2/μ−1 ⇒ Σ=1 (Weyl/
lensing protected), MGCAMB mugamma_par==6. RESULT: σ₈ +3.19% ✓ but low-ℓ ISW NOT fixed (~25σ; peak
3.2× at ℓ=10, even higher than no-slip's 2.6×). (Caveat: large slip γ=½ is subtle; exact number
not fully trusted — possible slip-anisotropic-stress dynamics/implementation subtlety. But it
clearly does NOT give the hoped ISW=ΛCDM.)

ROBUST REASON: the ISW is sourced by the Weyl potential, which is sourced by the matter Δ — and
μ→4/3 ENHANCES Δ (that IS σ₈). Σ=1 fixes the Weyl↔Δ relation but Δ is still larger ⇒ Weyl still
deepens ⇒ ISW still fires. Full cancellation needs Σ∝1/D_growth (fine-tuned), not a natural slip.

### THE STRUCTURAL LAW (what GRUT is telling us — robust across ALL avenues)

Every attempt to break the low-ℓ ISW failed for the SAME reason:
  scale filters (not derivable) · memory source (τ₀ 10⁴× too short) · quadratic noise source
  (CMB-safe but nonlinear, loses linear σ₈) · slip μ vs Σ (growth still feeds Weyl).
=> LAW: large-scale structure-growth enhancement (the dark sector / σ₈) is WELDED to the low-ℓ CMB
   ISW — both sourced by the same enhanced clustering of the Weyl potential. NO standard MG
   structure (μ, γ, Σ, source, memory, slip) decouples them. Breaking the link requires NEW physics
   that adds dark-sector FORCE without adding WEYL curvature (decouples clustering from the metric
   it sources) — outside every standard parametrization. This is GRUT's central open cosmology
   problem: either crack it (new constitutive physics breaking growth↔Weyl) or state it honestly.

## 0.3 FINAL VERDICT — every in-framework avenue closed

- Propagator: derived → μ→4/3 super-horizon (not the fix).
- Local source F[δρ,∇δρ,Φ]: density/Φ worse; tidal/equivalence-principle → horizon scale
  (f_subH, 2.6×), not k_eq. Closed.
- Memory/self-referential source (kernel-integrated history): k_eq does not emerge; τ₀ too
  short by ~10⁴. Closed.

The low-ℓ CMB is a GENUINE FALSIFIER for GRUT's derived large-scale linear response (μ→4/3 at
k≲k_eq), robust because the framework's own structure is exhausted. UNAFFECTED: σ₈/BAO/fσ₈/
growth (sub-horizon, k≳10⁻²) — those stand. A rescue would require a NEW cosmological-scale
ingredient (a second, much longer memory tied to structure formation, or χ_eq re-derived to
VANISH rather than saturate as k→0) — a different constitutive theory, not a completion of this
one. (Computation: memory-reach + memory-source μ in this session's transcript.)

---

## (Below: the original k_eq-filter writeup — now understood as a proxy for §0.)

---

## 1. The problem (validated negative)

GRUT modifies gravity through μ(k,a) in the Poisson equation with γ = 1 (no slip).
Run through the full Einstein–Boltzmann system (MGCAMB, with GRUT's μ inserted into
the validated (μ,γ) hooks), GRUT's prescription with the **instantaneous** sub-Hubble
filter

    f_subH(k,a) = (k/aH)² / (1 + (k/aH)²)          ["Axiom A1", evaluated at time a]

predicts a large low-ℓ ISW **excess**:

| ℓ | 2 | 6 | 10 | 16 | 20 | 30 | 100 | 220 |
|---|---|---|----|----|----|----|----|----|
| D_ℓ^GRUT / D_ℓ^ΛCDM | 0.93 | 1.80 | 2.37 | **2.61** | 2.53 | 2.04 | 1.03 | 1.00 |

Coherent across ℓ = 5–30, this is a **~29σ** cosmic-variance tension — and in the
**wrong direction** (Planck observes a mild low-ℓ *deficit*).

**Validation of the negative (it is real, not a code artifact):**
- MGCAMB's GR limit (MG off) reproduces stock CAMB 1.5.8 (PyPI) **exactly**
  (D₂ = 1023.6 vs 1023.6); acoustic peaks match to 5 sig figs; ratio → 1.000 at ℓ=220.
- Numerically bulletproof: identical under AccuracyBoost 1→3, lSampleBoost, GRtrans 1e-3↔1e-4.
- Independently corroborated by GRUT's own metric-consistent CAMB fork (`~/camb_grut`),
  which gives ~2× in the same regime.
- (Caution recorded: an earlier *approximate* line-of-sight estimate gave 6–11×, but it
  used the GRUT-contaminated `~/camb_grut` transfer as its "ΛCDM" base and double-counted.
  The MGCAMB figure, ~2.6×, supersedes it.)

---

## 2. The origin: a quasi-static-approximation error

The (μ,γ) parametrization — and GRUT's μ — encode the medium's **quasi-static (QS),
sub-horizon** gravitational response. The QS approximation is valid only for modes
**deep inside the horizon throughout the epoch in which the potential evolves.**

The instantaneous filter f_subH = (k/aH)² uses the **current** comoving horizon
(aH today ≈ 2.3×10⁻⁴ Mpc⁻¹). It therefore admits modes near k ~ 10⁻³ Mpc⁻¹ that only
recently crossed the horizon (k ~ 10⁻³ enters at z ~ 60) and for which the QS response
has **not** held across the matter era. Applying the QS μ to these near-horizon modes
spuriously drives the Bardeen potential to evolve, sourcing the large unphysical ISW.

This is a known failure mode of QS modified-gravity prescriptions near the horizon —
not evidence that GRUT's medium response is wrong, but that the *filter selecting where
that response applies* was too permissive.

---

## 3. The fix: the equality horizon k_eq (zero free parameters)

The correct condition is that the QS medium response must hold (and accumulate) **throughout
matter domination**, when the potential is evolving. The binding constraint is the
**smallest comoving horizon during that era**, which occurs at matter–radiation equality:

    k > k_eq = a_eq H(a_eq) = 0.073 Ω_m h² ≈ 0.0104 Mpc⁻¹.

Modes with k < k_eq entered the horizon *during* matter domination (or remain near-horizon)
and never satisfy the QS condition over the full evolution. The reference scale in the
sub-horizon filter should therefore be the **equality horizon k_eq**, not the instantaneous
horizon aH(today). This is fixed entirely by Ω_m h² — **no new free parameter.**

Implemented filter (applied alongside f_subH):

    f_eq(k) = (k/k_eq)² / (1 + (k/k_eq)²),   k_eq computed from the background.

This is also consistent with GRUT's nature as a viscoelastic **memory** medium: the
gravitational response accumulates over the mode's sub-horizon-and-matter-dominated
history, which naturally introduces the equality scale — content the instantaneous
Axiom A1 filter omits.

---

## 4. Result (full relativistic MGCAMB, k_eq from background, zero free parameters)

| quantity | naive (instantaneous) | **derived k_eq filter** |
|---|---|---|
| low-ℓ D_ℓ ratio, ℓ=2–30 | 0.93 – 2.61 (≈29σ) | **0.989 – 1.005 (consistent)** |
| σ₈ | +3.13% | **+2.81%** |
| P(k): BAO (k=0.04) | +17% | **+16% (intact)** |
| P(k): quasilinear (k=0.1) | +4.5% | +3.9% (intact) |
| P(k): σ₈-scale (k=0.3) | +0.5% | +0.5% (intact) |
| P(k): super-equality (k=0.002) | +100% | **+3% (suppressed → fixes ISW)** |

- The CMB low-ℓ tension is **gone** (every multipole within ~1% of ΛCDM).
- All genuinely sub-horizon (QS-valid) structure-growth predictions — σ₈, BAO, fσ₈ — are
  **preserved**. Only the >Gpc super-equality modes (which source the low-ℓ ISW and almost
  nothing else observable) lose their enhancement.
- **Robust, not fine-tuned:** varying k_eq by ±40% (0.0073 ↔ 0.0146) leaves the ISW at
  ratio 1.00–1.01. The physics is the *scale* (k_eq), not a tuned value.

---

## 5. Honest scope — what is derived vs. modelled vs. open

- **Derived / robust:** the reference *scale* is the equality horizon k_eq, forced by
  QS-validity (sub-horizon throughout matter domination) and fixed by Ω_m h². Zero free
  parameters. The numerical result is from the full relativistic Boltzmann solver.
- **Modelled (ansatz):** the smooth Lorentzian shape f_eq = (k/k_eq)²/(1+(k/k_eq)²) of the
  transition. The result is insensitive to the precise shape/value (§4 robustness).
- **Open (the remaining ToE step):** deriving the filter — scale *and* shape — directly from
  GRUT's CTP constitutive action / viscoelastic memory kernel, rather than from the
  (standard, but here imposed) quasi-static-validity argument. This would turn "rescuable
  by a motivated refinement" into "predicted from first principles."
- **Implication for Axiom A1:** the instantaneous sub-Hubble filter must be replaced by the
  equality-referenced (memory-consistent) filter. This is a correction to GRUT's stated
  prescription, not a free addition.

---

## 6. Reproduction

- MGCAMB build with GRUT μ + k_eq filter: `~/mgcamb_grut/fortran/mgcamb.f90`,
  `mugamma_par == 4` (μ, μ̇ with f_subH·f_eq; γ=1). Build: isolated venv `~/mgcamb_venv`.
- Driver / data: `~/mgcamb_grut/grut_isw_run.py`, results `~/mgcamb_grut/grut_isw_definitive.npz`.
- Selector: `set_mgparams(MG_flag=1, pure_MG_flag=1, mugamma_par=4, GRtrans=0.001, E11=e)`
  with `E11=0` → k_eq from background (physical), `E11>0` → manual k_eq, `E11<0` → filter off
  (naive). Ground truth ΛCDM: stock CAMB 1.5.8 (`~/stockcamb_venv`).
