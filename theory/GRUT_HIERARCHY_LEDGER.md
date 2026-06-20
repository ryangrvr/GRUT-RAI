# GRUT Hierarchy Ledger — The 34-Order Gap, Audited

*A stabilization document. Every identity below was re-derived in `.venv` against
the cited file:line; nothing here is asserted on memory. This ledger consolidates
the τ₀ / τ_micro structure before any attempt to force the gap's magnitude, so
that a future derivation inherits no hidden assumptions and we know exactly how
many genuinely independent numbers the hierarchy contains.*

---

## 1. PURPOSE

GRUT's deepest unexplained fact is a single number: the ~34-order separation
between the macroscopic relaxation time τ₀ ≈ 41.9 Myr and the microscopic
correlation time τ_micro ≈ 1.4×10⁻¹⁹ s. The framework already records this
honestly — `tau_hierarchy_decision.py:358` sets `relation_derivable = False`
(Option B: the two scales are independently anchored, with no derivation between
them) — but the gap does not appear in one place. It surfaces, in many costumes,
across the foundation code, the response/memory sector, the cosmology
observables, and the theory docs/registry.

Before attempting the deepest derivation — forcing the *magnitude* of
τ_micro/τ₀ from first principles — we must first **stabilize and audit** the
hierarchy as a coherent structure. The danger in a magnitude derivation is
circularity: a "derivation of c = ln(τ₀/τ_micro)" that quietly re-uses τ₀ has
assumed half the answer. This ledger traces every appearance of the gap, classifies
each as **FORCED**, **ANCHORED**, or **UNKNOWN**, and exposes which apparent
derivations are identities in disguise — so the charge to a future derivation
(§5) can name exactly what it must force and what it must not secretly assume.

The work is anti-salesmanship by design. It enumerates what is *not* derived as
carefully as what is.

---

## 2. THE FORCED / ANCHORED / UNKNOWN TABLE

Three classes, applied to every distinct hierarchy quantity:

- **FORCED** — follows from GRUT structure with no number tuned (e.g. the slow
  mode's existence from conservation; the Mori–Zwanzig split *requiring* τ₀≫τ_micro).
- **ANCHORED** — an empirical input fixed to observation (τ₀ to H₀/Bullet;
  T_c/τ_micro to the cosmic-chronology pin), or an algebraic restatement of one.
- **UNKNOWN** — no mechanism (what fixes the *magnitude* of the hierarchy).

### 2A. The genuinely independent inputs (ANCHORED, no disguise)

| Quantity | File:line | Class | Independent? |
|---|---|---|---|
| **τ₀ = 41.9 Myr = 1.322×10¹⁵ s** | `closure_protocol.py:201-239` | ANCHORED | **YES — dimensional anchor #1.** Two anchors agree ~10–20%: cosmic-baseline 1/(H₀·108π)→41.2 Myr at H₀=70; Bullet δ≈v·τ₀→~49 Myr. The "V7 gold-benchmark derivation" was retracted (docstring 218–226: ℏl/Gm² gives microseconds, not Myr). |
| **T_c = 54.7 MK = 4.71 keV** | `closure_protocol.py:395-405` | ANCHORED | **YES — dimensional anchor #2.** Cosmic-chronology pin (T at t≈16 h post-BB). Docstring 400–401: "τ_micro is derived from this, not the other way around." |
| **ln(τ₀/t_P) = 134.45** | `GRUT_GENESIS.md:499` (doc-only log) | ANCHORED | **YES — independent Planck-log #1.** Verified 134.4472. (Code carries the raw ratio τ₀/t_P=2.45×10⁵⁸ at `primordial_curvature.py:242`; the *log* is a doc quantity.) |
| **ln(τ_micro/t_P) = 56.21** | `GRUT_GENESIS.md:499,513` | ANCHORED | **YES — independent Planck-log #2.** Verified 56.2137. The honest forcing route targets THIS one. |
| **α_vac = 1/3** | `closure_protocol.py:104-136` | ANCHORED (axiom if postulate fails) | Separate **dimensionless** third number — **not a face of the τ-gap.** Derived only under the conformal-mode-scalar postulate (KS-2011); de-facto axiom otherwise. Sets S, R, n_g(0); never the 34-order scale. |

### 2B. Identities-in-disguise (ANCHORED-derived; carry NO new information)

All equalities below verified to machine precision in `.venv`.

| Quantity | File:line | Disguise |
|---|---|---|
| **τ_micro = 1.396×10⁻¹⁹ s** | `closure_protocol.py:407` | ≡ ℏ/(k_B·T_c). The SI-dual of T_c; `registry.py:1442` labels it "DERIVED from the empirical T_c anchor." Not independent. |
| **T_C_KELVIN (recovered)** | `closure_protocol.py:435-460` | Circular round-trip T_c→τ_micro→T_c; = canonical by construction. |
| **4.71 keV warm-DM gap** | `GRUT_V4_FOUNDING_CHARTER.md:58` | ≡ k_B·T_c = ℏ/τ_micro = 4.7137 keV (both verified equal). Charter calls it a "definitional tautology." |
| **G₀ = ℏ/(c³τ_micro⁴) ≈ 1.03×10¹⁶ Pa** | `GRUT_GENESIS.md:29`; `CHARTER.md:25,42,66` | = ℏ/(ℓ_micro³·τ_micro) — the **same Debye equation written twice** (verified machine-precision: G₀·ℓ³ = ℏ/τ_micro = 7.55×10⁻¹⁶ J). τ_micro alone. **Not in `grut/` code — v4 theory-doc only.** |
| **ℓ_micro = c·τ_micro = 4.19×10⁻¹¹ m** | charter; venv | Unit conversion of τ_micro. |
| **L₀ = c·τ₀ = 12.85 Mpc** | `second_order_kernel.py:99`; `retarded_kernel_frw.py:88`; `cmb_isw.py:174` | Unit conversion of τ₀ ("the size relocates verbatim into L₀", GENESIS:493). Verified 12.8476 Mpc. |
| **ratio τ₀/τ_micro = 9.47×10³³** | `tau_hierarchy_decision.py:154` | τ₀/τ_micro. Existence forced; magnitude = the two anchors. log₁₀ = 33.976. |
| **c = ln(τ₀/τ_micro) = 78.23** | `GRUT_GENESIS.md:499,506-508` | = ln(τ₀/t_P) − ln(τ_micro/t_P) = 134.45 − 56.21 (verified to machine precision). **The DIFFERENCE of the two independent logs — not independent.** |
| **T_peak = ℏ/(τ₀·k_B) = 5.78×10⁻²⁷ K** | `tau_hierarchy_decision.py:166`; `primordial_amplitude.py:105` | **The τ₀-dual *temperature*** — "the thermal equivalent of the gravitational pole." The thermal mirror of the 4.71 keV gap, related to it by exactly τ₀/τ_micro. A fourth temperature-costume of τ₀, alongside μ₀. |
| **S = 12π/α² = 108π = 339.29** | `closure_protocol.py:138`; `anomaly.py:142` | Pure function of α_vac; not a τ-gap face. Maps τ₀↔τ_Λ. |
| **τ_Λ = S·τ₀ = 14.22 Gyr** | `closure_protocol.py:241` | τ₀ × S. |
| **H₀_implied = 68.77 km/s/Mpc** | `closure_protocol.py:247` | = 1/(S·τ₀). **H₀ is DERIVED from τ₀ — H₀ is NOT an independent anchor; τ₀ is.** |
| **μ₀ = ℏ/τ₀; μ_Λ = ℏ/τ_Λ** | `closure_protocol.py:316-322` | ℏ-duals of τ₀; μ₀/μ_Λ = S by construction. |
| **a_* = c/τ_Λ; a₀ = a_*/2π ≈ 1.2×10⁻¹⁰** | `closure_protocol.py:329-336` | = c/(2π·S·τ₀). a₀ is a genuine τ₀-magnitude consequence; the ν(y) MOND *shape* is ADOPTED, not derived. |
| **R_max = α/(c²τ₀²); ρ_max** | `closure_protocol.py:255-309` | Functions of α_vac, τ₀; ∝ τ₀⁻². |
| **Ω_Λ = (2−R)² = 0.7145** *(conditional)* | `vacuum.py:22-46`; `hubble_from_first_principles.py:95` | τ₀ cancels **only at the cosmic-baseline H₀ = 1/(S·τ₀)** (verified 0.71453 = (2−R)²). Against an *external* H₀=70 it is 0.6897 and τ₀ does **not** cancel (verified). A *conditional* identity in τ₀, not an absolute one. |

### 2C. FORCED (existence-only — depend on τ₀≫τ_micro, NOT its magnitude)

| Quantity | File:line | Magnitude-inert? |
|---|---|---|
| **First-order-ness / single relaxational pole** | `mori_zwanzig_kernel.py:72-75`; `pole_spectrum.py:63,141` | Yes — flips at ratio 1/4 only |
| **MZ no-dark-mode theorem** | `mori_zwanzig_kernel.py:99-105` | **Yes — verified live: ratios 1e-1…1e-34 ALL give forbids_dark=True; flip at exactly τ₀/4 (0.24→True, 0.25→False).** |
| **Off-axis threshold = τ₀/4** | `mori_zwanzig_kernel.py:85-88` | Pure dimensionless ratio 1/4 |
| **Fast-pole suppression O(τ_K/τ₀)** | `mori_zwanzig_kernel.py:108-117` | Existence-only |
| **MZ validity condition (gap must be LARGE, ratio≫4)** | `GRUT_GENESIS.md:487-490` | The slow/fast projection's own self-consistency |
| **Φ_μν kernel = α·χ(ω)** | `linearized_ctp_action.py:410-427` | τ₀ inherited, not re-derived |
| **Locality / no-halo (k=0 analytic, no 1/k²)** | `locality_no_halo.py:78-89`; `second_order_kernel.py:203` | Independent of ALL τ values |
| **μ_linear = 1 / D = 1.0 (ΛCDM linear growth)** | `constitutive_growth.py:198-274` | Conformal flatness; hierarchy-independent |
| **ρ_eff shape (slope −4)** | `second_order_kernel.py:161-200` | Shape L₀-independent; only band scales |
| **n_g(0) = √(4/3) = 1.1547** | `closure_protocol.py:515-524` | Set by α_vac alone, τ₀-free |
| **Crystallinity X≫1 (deep crystal)** | `lambda_contact.py:322`; `cosmic_x_crossover.py:108` | Needs only τ₀ large enough; regime ordering |
| **Existence + character of the slow mode** | `GRUT_GENESIS.md:60-66,479-490`; `registry.py:5414` | Conservation/Ward ⇒ slow channel |

### 2D. UNKNOWN (no mechanism for the magnitude)

| Quantity | File:line | Note |
|---|---|---|
| **The MAGNITUDE of the gap** (34 orders / c=78.23 / 54.7 MK / 4.71 keV / 12.85 Mpc) | `tau_hierarchy_decision.py:358` `relation_derivable=False` | All four closure paths fail (run live). |
| **Option-B decision** | `tau_hierarchy_decision.py:90-132` | Path1 T_peak=5.78×10⁻²⁷ K (34 orders below T_c); Path3 product T*=4.14×10⁻⁸ K (unphysical 41 nK). |
| **BBN-buffer bridge attempt** | `bbn_thermal_buffer.py` | Standard cosmology, no GRUT scales; refuted as a τ₀↔τ_micro bridge by ~10 orders. |

---

## 3. THE 6 ANSWERS

**(1) Where τ₀ enters.** Through the single-pole susceptibility χ(ω)=1/(1−iωτ₀) —
the spine of the entire response sector (`closure_protocol.py:507`;
`linearized_ctp_action.py:249,427`; `second_order_kernel.py:110`;
`retarded_kernel_frw.py:43`). Its **magnitude** enters via: L₀=c·τ₀=12.85 Mpc
(K²-coupling / FRW scale, `sok:99`, `frw:88`); QS-validity τ₀H (`frw:14`); τ_Λ=S·τ₀
⇒ H₀, Ω_Λ, age t₀=N_eras·τ₀, a₀/MOND, μ₀, R_max; and the cosmic-baseline
τ₀=1/(108π·H₀).

**(2) Where τ_micro enters.** In `grut/` code, only two places: `mori_zwanzig_kernel.py:69`
(as τ_K, where its *value* is irrelevant) and `closure_protocol.py:407` (the T_c
dual). Everything else τ_micro-flavored is a function of T_c: the 4.71 keV gap,
G₀ (theory-doc only), ℓ_micro, f(T)=tanh(T_c/2T) (`thermal_transition.py:60-94`),
the BBN>T_c>recomb chronology bracket. **The macroscopic response is built
entirely from τ₀; τ_micro never touches Φ_μν / FRW / growth.**

**(3) Depend ONLY on the EXISTENCE of the hierarchy (τ₀≫τ_micro).** All of §2C.
The decisive evidence: the MZ overdamping / no-dark-mode result is **operationally
inert across 33 orders** — verified live that ratios 1e-1 through 1e-34 give the
identical conclusion, and the criterion flips only at the pure ratio τ_K/τ₀=1/4
(`off_axis_threshold = tau0/4`, scale-free). Any ratio > 4 suffices. Also
existence-only / structural: locality, n_g(0)=√(4/3), Ω_Λ=(2−R)² (τ₀ cancels at
the cosmic baseline), D=1.0, slope −4.

**(4) Depend on the exact MAGNITUDE.** Every numerical face: 54.7 MK, 4.71 keV,
12.85 Mpc, ℓ_micro, G₀≈10¹⁶ Pa, ratio 9.47×10³³, c=78.23. And the genuinely
load-bearing magnitude pins: H₀'s absolute value (anchors τ₀, partly circular
with τ₀'s own definition), a₀ in the RAR band, galaxy-rotation 10 kpc at
X=ωτ₀≈0.94 (`closure_protocol.py:531`), the QS-validity arithmetic (τ₀H=1 at
z≈77), the T_c decade (BBN>T_c>recomb), warm-relic overclosure, and age via the
separately-anchored integer N_eras=329.

**(5) Which logarithms are genuinely INDEPENDENT.** **ln(τ₀/t_P)=134.45 and
ln(τ_micro/t_P)=56.21 are the two independent ones.** c=ln(τ₀/τ_micro)=78.23 is
**exactly their difference** (verified to machine precision: 134.4472 − 56.2137 =
78.2334) — NOT independent. The MZ control parameter τ_K/τ₀ = exp(−c) =
1.056×10⁻³⁴ (verified) is the same single derived combination.

**(6) IDENTITIES IN DISGUISE — the complete catalog** (all `.venv`-verified):

| # | Identity | Costumes | Source |
|---|---|---|---|
| **K (KEYSTONE)** | **c = ln(τ₀/τ_micro) = 78.23** | (i) transmutation exponent, (ii) Arrhenius barrier E/k_BT [verified ln(E/kT)=78.2334 with E=ℏ/τ_micro, kT=ℏ/τ₀], (iii) MZ bifurcation distance, (iv) ln(τ₀/t_P)−ln(τ_micro/t_P) | `GENESIS.md:506-508` |
| a | k_B T_c = ℏ/τ_micro = 4.71 keV | T_c ↔ τ_micro ↔ 4.71 keV ↔ ℏ/τ_micro | `closure_protocol.py:407` |
| b | G₀ = ℏ/(c³τ_micro⁴) = ℏ/(ℓ³τ_micro) | "same Debye ansatz written twice" — G₀ ↔ τ_micro | `CHARTER.md:42,66` |
| c | L₀ = c·τ₀; ℓ_micro = c·τ_micro | length costume of each τ (pure unit conversion) | `ORGANIZING_STRUCTURE.md:18` |
| d | T_peak = ℏ/(τ₀·k_B) = 5.78×10⁻²⁷ K | the τ₀-dual *temperature* (thermal mirror of 4.71 keV; ratio = τ₀/τ_micro) — a fourth costume of τ₀ alongside μ₀ | `tau_hierarchy_decision.py:166` |
| e | f(T) = tanh(T_c/2T) | τ_micro as the thermal order parameter (genuine FDT/KMS *form*; *scale* = T_c) | `GENESIS.md:139-152` |
| f | τ₀ = 1/(108π·H₀) | relabels τ₀ as H₀; 108π = 12π/α² is the pre-existing α-spine, not new content | `registry.py:180` |
| g | τ_K/τ₀ = exp(−c) | the MZ "memory-separation" costume of the single hierarchy number | `mori_zwanzig_kernel.py:163` |
| h | χ(ω)=1/(1−iωτ₀) ⟷ K(t)=(1/τ₀)e^{−t/τ₀} ⟷ τ₀ż+z=z_target | one single-relaxation object in three forms (FT pair + ODE): "first-order-ness = Markovian limit = single pole" | `closure_protocol.py:497-512` |
| i | Ω_Λ = (2−R)² *(conditional)* | τ₀ cancels **only** under the cosmic-baseline H₀=1/(S·τ₀) — an identity in τ₀ under that convention; regains τ₀-dependence (→0.690) against external H₀ | `vacuum.py:22-46` |
| — | **REJECTED numerology** | 8π²=78.96 (+0.92%, verified) — universal one-instanton action, NOT GRUT-distinctive; also 25π, S/(2π)·lnS/4 | `GENESIS.md:502-505` |

---

## 4. THE INDEPENDENT-INPUT COUNT — the punchline

**The whole 34-order hierarchy reduces to exactly TWO genuinely independent
anchored dimensional numbers.**

```
  τ₀  (gravitational)   ≡ ln(τ₀/t_P)     = 134.45    [anchored via H₀ / Bullet]
  T_c (thermal)         ≡ ln(τ_micro/t_P) = 56.21    [anchored via cosmic chronology]
  ─────────────────────────────────────────────────────────────────────
  c, ratio, τ_micro, G₀, ℓ_micro, L₀, T_peak, 4.71 keV,
  τ_Λ, H₀, Ω_Λ, μ₀, a₀, R_max, f(T) …  = ALL disguises of the two
```

Plus **α_vac = 1/3** as a separate **dimensionless** third number —
derived-under-postulate, orthogonal to the τ-gap (it sets S, R, n_g(0), the shape
constants, but never the 34-order scale).

This is confirmed independently at all four sweep levels (foundation code,
response sector, cosmology observables, theory docs/registry) and corroborated by
the framework's own meta-accounting: `registry.py:404` (`zero_free_parameters`)
scopes the one-parameter claim to the gravitational core and explicitly names
τ_micro "a second independently anchored scale … NOT derivable from τ₀";
`CHARTER.md:46` lists "only FOUR logically independent: {Q, conformal-mode/α, τ₀,
τ_micro}."

**No hidden third dimensional anchor exists.** The two anchors are mechanistically
independent: a grep over `grut/` finds no formula linking τ₀ to T_c/τ_micro, and
`relation_derivable=False`.

**A required correction to the count's *proof*.** An earlier framing cited the
Path-3 cross-check ratio 0.9838 ≠ 1.000 as evidence that "the two anchors satisfy
no exact identity." **This citation is invalid and is retracted here.**
Decomposed in `.venv`: `PATH3_CROSS_CHECK_RATIO = TAU_PRODUCT_S2 /
(_TAU_0_FROM_H0_DEF · _TAU_MICRO_FROM_TC_DEF)`, and τ_micro is byte-identical on
both sides (`HBAR/(K_B·T_c)` appears in numerator and denominator and cancels
exactly — verified `np.isclose=True`; the ratio reduces *exactly* to
`TAU_0_SEC / (1/(H₀·S))` = 0.9838). The 0.9838 is therefore a **τ₀-vs-1/(H₀·S)
anchor-consistency check** — the posited τ₀ implies H₀=68.77, not the Planck
67.66 plugged in — and says **nothing** about whether τ₀ and τ_micro are related.
The count of **2 is still correct** (confirmed by the absence of any linking
mechanism), but it rests on `relation_derivable=False`, not on 0.9838.

---

## 5. THE CHARGE TO A FUTURE τ_micro DERIVATION

Given the ledger, a genuine magnitude-derivation faces sharp constraints.

**It MUST produce ONE of the two independent Planck-logs from first principles** —
concretely the thermal UV anchor **ln(τ_micro/t_P) = 56.21**, i.e. k_B T_c = 4.71
keV (`GENESIS.md:513`). Deriving c, the ratio, or "34" directly is **insufficient
and circular**: c is the *difference* of the two logs, so any "derivation of c"
that uses τ₀ has already assumed log #1. The one honest target is to close one log
*absolutely* (against t_P), not relatively (against the other anchor).

**It MUST come from a real mechanism with a real coefficient.** GENESIS is
explicit (verified text): transmutation is "the right class in the abstract but
GRUT lacks the machinery — GRUT has no β-function carrying τ₀"; its only RG
statement is that τ₀ is RG-*protected* (`boltzmann_consistency.py` L42-46), the
*opposite* of an asymptotic-freedom flow. The named honest route is a
Coleman–Weinberg condensation/running in the CTP sector with a real anomaly
coefficient (GRUT's are O(3–7)) — **not reverse-fit to 56 or 78.**

**It MUST NOT secretly assume any of these** (each would smuggle the answer in):

- ✗ τ_micro ≡ ℏ/(k_B T_c) as if it *derives* τ_micro — it is the definition
  (`closure_protocol.py:407`). T_c and τ_micro are one number.
- ✗ G₀, ℓ_micro, the 4.71 keV gap, or T_peak as independent constraints — all are
  τ_micro/T_c (or τ₀) restated; G₀ is the Debye ansatz "written twice."
- ✗ 8π² = 78.96 or any sub-1% dimensionless target — the repo already rejects
  this by its own A_s standard.
- ✗ H₀ as an *independent* check on τ₀ — H₀ is derived *from* τ₀
  (`closure_protocol.py:247`); using it to pin τ₀ is the cosmic-baseline anchor
  itself, not a second route.
- ✗ The Path-3 0.9838 cross-check as evidence of τ₀↔τ_micro independence — it is
  a τ₀/H₀ check in which τ_micro cancels (§4).
- ✗ The MZ existence result as if it constrained magnitude — it is provably
  magnitude-inert (1e-1…1e-34 identical, flip at τ₀/4).

**It inherits zero hidden assumptions.** The framework already concedes the
magnitude is its deepest unexplained fact (`relation_derivable=False`, Option B).
The forced half — existence + character of the slow mode, via Mori–Zwanzig +
conservation — is real and value-independent; the unforced half — the *size* — is
cleanly isolated as the single standing UNKNOWN. A derivation that forces
ln(τ_micro/t_P)=56.21 from a real condensation coefficient, with τ₀ never
entering, would convert the framework from two anchors to one. Nothing less will
do, and nothing less is claimed.

---

## Appendix — Code-hygiene findings surfaced during the audit (out-of-scope of the ledger, verified)

- **`grut/derived/cosmology/primordial_amplitude.py:105`** — `T_C_KELVIN =
  HBAR/(TAU_0_SEC·K_B)` = 5.78×10⁻²⁷ K. This is **not** a resurrected
  pre-Correction-22 wrong-scale bug: the value is *intentionally* the τ₀-dual
  temperature T_peak ("the boiling point of gravity," k_B T = ℏ/τ₀; identical to
  the named `T_PEAK_NOISE_KERNEL_K` at `tau_hierarchy_decision.py:166`, verified
  equal). The defect is a **symbol collision** — it reuses the name `T_C_KELVIN`,
  which in the foundation means 54.7 MK, for a different physical quantity.
  Recommended fix: rename to `T_PEAK_KELVIN`. (It feeds `ou_variance_h_dimensional`
  and the A_s evaluation "at T=T_c," so the collision is worth resolving.)
- **`grut/derivation/phi_munu/mori_zwanzig_kernel.py:68-69`** hardcodes τ₀ and
  τ_micro rather than importing `closure_protocol` constants (values consistent;
  duplication).
- **`grut/foundation/noise_kernel.py:89`** uses `tau_kms = ℏ/(2π k_B T)`, which
  differs from τ_micro = ℏ/(k_B T_c) by a factor of 2π — distinct "thermal time"
  conventions; τ_micro does NOT carry the KMS 2π. Consistency/convention note.
