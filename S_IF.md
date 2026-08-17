# S_IF — the formal action specification

*Status: **CONSTRUCTION DOCUMENT, ledger 0** — this file declares the action GRUT has always
gestured at; it derives nothing new and banks nothing by itself. Every load-bearing line below
carries its register home in brackets. Built 2026-08-09 under the overseer's x-floor brief
(Parts 2–3), answering the standing external criticism ("the central vocabulary remains too
elastic: 'responsiveness' can become a narrative absorber unless tied to a precise action,
parameter space, and exclusion rule"). The rule this document is written under, verbatim from
the brief: **do not re-assert pure-TT as an axiom inside the action — that is the
stiffer-suit failure and the whole reason for the exercise. If the action doesn't fix x, it
carries the family and says so.** (It doesn't, and it does — §6.)*

---

## 1. Field content

- **System**: the symmetric rank-2 metric perturbation h_μν on a declared background (flat FRW
  for every banked observable; the linear-cosmology frame is the fixed-slicing spatial-SVT
  frame of `mu_linear` — [eft_operator_basis, KC5 fence]). Schwinger–Keldysh doubling
  h⁺, h⁻; Keldysh basis h_r = (h⁺+h⁻)/2, h_a = h⁺−h⁻ [rung1_inin_action].
- **Bath**: the gravitational vacuum's non-metric degrees of freedom, **integrated out and NOT
  specified**. This is not an omission of this document; it is rung3's frontier, priced where
  it lives [rung3_single_pole, derived-pending; the dispatch]. S_IF is defined at the level of
  its kernels (the Gaussian truncation S2 makes this complete at quadratic order).
- **State**: a KMS state at inverse temperature β for the equilibrium statements
  [rung2_kms_gate]; the cross-cluster shared input S1 (a state and an expectation functional
  on the observable algebra) is acknowledged as sitting UNDER this declaration
  [vc_state_expectation_functional].

## 2. Symmetry content (the register-declared inventory, none invented here)

Exactly the S1–S7 inventory `calc/operator_basis.py` reads off the register: causal/retarded
structure (S1), quadratic truncation (S2), the system/bath split (S3), KMS/FDT + matrix
passivity (S4), diffeomorphism invariance with its banked Ward limitation (S5), background
homogeneity/isotropy + inherited parity-evenness (S6), pair symmetry / Onsager (S7).
**No symmetry beyond these is declared, and in particular linearized Weyl invariance is NOT
available** — GRUT imports α as the trace-anomaly ratio, and the anomaly is the statement that
Weyl invariance is broken [p_tt_ansatz.boundary_condition].

## 3. Kernel structure — the action, written out

In the Keldysh basis, at quadratic order, at fixed (ω, k) in the enumerated frame:

    S_IF[h_r, h_a] = ∫ (dω/2π) d³k  [ h_a · K_R(ω, k²) · h_r  +  (i/2) h_a · N(ω, k²) · h_a ]

with BOTH kernels decomposed on the Ward-surviving projector pair [eft_operator_basis: exactly two survivors at this frame/order — **WARD-SCOPE CORRECTION 2026-08-14**: per the SCDP read (arXiv:2507.03103), dissipative and noise operators necessarily break the doubled diffeomorphism group to its diagonal, so the two-survivor exhaustiveness is conditional on an advanced-branch identity no dissipative completion sustains. Under the surviving diagonal identity, K_R's transversality on its **retarded slot** is Ward-bought; the **advanced-slot and noise-kernel transversality are INPUTS** — supported externally by stochastic-gravity Bianchi consistency (Hu–Verdaguer), cited not claimed. The family below is therefore a **declared restriction**, not the full admissible open-gravity space (SCDP's own noise functional carries non-transverse structures); the passivity and no-pin results are statements WITHIN this declared family]:

    K_R(ω, k²) = c₂(ω, k²) P⁽²⁾ + c₀(ω, k²) P⁽⁰ˢ⁾        (retarded / dissipation)
    N(ω, k²)   = n₂(ω, k²) P⁽²⁾ + n₀(ω, k²) P⁽⁰ˢ⁾        (noise)

Structural conditions, each with its home:

| condition | statement | home |
|---|---|---|
| causality | c_i(ω) analytic in the upper half ω-plane (retarded) | rung1 / rung4_love_kk |
| KMS lock | n_i(ω) = coth(βω/2) · Im c_i(ω), per channel | rung2_kms_gate |
| passivity | ω·Im c₂ ≥ 0 AND ω·Im c₀ ≥ 0, channel by channel, pointwise — the matrix condition is EXACTLY these two scalar conditions, no cross-channel rescue | **passivity_channel_diagonal** (the general lemma) applied as **x_no_pin_theorem** (this wave; calc/x_no_pin.py) |
| pair symmetry | K symmetric under index-pair exchange | S7, inherited-not-chosen |
| finite memory | c_i's dissipative structure single-pole (Debye) rather than branch-cut | rung3_single_pole — **the conjecture, not a theorem; external** |

GR normalization anchor (banked exact fact, carried so the moduli have a scale): linearized
Einstein–Hilbert is itself (1/2)k²[P⁽²⁾ − 2P⁽⁰ˢ⁾] — **GR's own kernel carries a scalar
component twice its spin-2 one** [p_tt_ansatz.boundary_condition, exact-arithmetic-verified].
The vacuum-response moduli are deviations riding on top of that kinematic structure; GR-relative
minimality therefore favors a NONZERO scalar modulus, which is why minimality can never defend
pure-TT [X_FLOOR_MAP trap fence, refuted-in-advance].

## 4. Dimensions

h dimensionless; K_R and N carry M_P²k² (the EH anchor's units); c₂, c₀ are then dimensionless
moduli functions of (ω, k²); β carries inverse energy [rung2]; the finite-memory scale L₀ (the
single relaxation time, IF rung3 lands pole-class) carries time [rung3]. No further
dimensionful parameter is declared — a dimensionful constant appearing anywhere downstream must
name which of these it is made of, or it is an insertion.

## 5. The parameter space, and THE DECLARATION

**x is defined, not free-floating** (this is the move that discharges `mu_slip_interior.py`'s
open item R1 — by construction, not by inference):

    x(ω, k²)  :=  c₀(ω, k²) / c₀^{trace-only}(ω, k²)

— the P⁽⁰ˢ⁾ modulus in units of the trace-only endpoint's coupling, the same normalization
`mu_slip_interior` already uses for its endpoints (x=1 ≡ trace-only, x=0 ≡ pure-TT). What was
previously a phenomenological dial with an unstated relation to the action is now the action's
own scalar-channel modulus, normalized. The passivity trap this dissolves: ζ→x sign transfer is
no longer an analogy across an unestablished map — it is the same quantity read in two
normalizations [PREREG_X_NO_PIN, variable caution; BRIEF_p_tt_interrogation KC4].

**DECLARED A KERNEL, NOT A CONSTANT.** x(ω, k²) is a function unless some specific argument
forces it constant, and no such argument exists in the corpus. Three independent lines already
point this way, plus one observational echo:
1. `calc/rung3_spectral_structure.py`: passivity is frequency-resolved (ω·ρ(ω) ≥ 0; different
   powers of ω behave differently) — the constraint structure is native to functions.
2. `calc/anomaly_c0_map.py` (R1): the anomaly-induced x is a form factor,
   x_anom(k) = [1/(3α)]·k²/(k²+M_σ²) — a momentum profile, not a number.
3. `calc/mu_slip_interior.py` R1: the x↔c₀ map is action-level and frequency-native.
4. The κ wave's finding — κ is "a coordinate on a model dimension GRUT never banked" — is the
   same unbanked k-structure seen from the observational side [X_FLOOR_MAP A8].
**Consequence, stated without euphemism: the constant-x interior family is a ONE-DIMENSIONAL
CUT through a function space.** RULED 2026-08-09 (the Part-4 relay): no new dial books — the
function-space freedom is already priced at eft_operator_basis (count-once) — and every
constant-x number carries the cut-conditionality qualifier now recorded at
zeta_interior_family.

Priors (all banked, none new): the constant-x cut's window is x < ~0.59 (DESI Σ₀ lensing,
central-inputs loose-upper, F-MAP fence) [zeta_interior_family]; every TT-auto-gate verdict is
κ-conditional / insertion-contaminated [A8]; x has NO observational floor — the family allows,
never predicts [zeta_interior_family]; the dissipative TT modulus is bounded far below
observability [rung8/SIGNATURE_AUDIT].

## 6. THE EXCLUSION RULE (the load-bearing section)

**What this action FORBIDS** — each a real exclusion with a home:

1. **Anti-passive response in either channel, at any frequency**: ω·Im c_i(ω) < 0 anywhere is
   excluded, per channel, with no cross-channel rescue [x_no_pin_theorem, via the general
   passivity_channel_diagonal lemma]. This is
   the floor: under §5's declaration it reads **x_diss(ω) ≥ 0 pointwise** (see §7 for exactly
   what that does and does not mean).
2. **Noise detached from dissipation in equilibrium** [rung2 KMS lock — and the lock is
   channel-diagonal, so it cannot be satisfied "on net" either].
3. **Acausal kernels** (non-retarded analyticity) [rung1/rung4].
4. **The trace-only endpoint** x = 1 at constant-x (μ = 4/3): excluded empirically +
   structurally [mu_linear, p_tt-independent]. (Deliberately NOT listed: a propagating-pole
   no-go — NO_GO_LEDGER records that this register banks NO claim at FORBIDDEN strength; the
   α-bridge is settled-negative, which is weaker, and the two must not be conflated.)
5. **Phantom-divide crossing from a single passive channel** [rung7_w3 / RESULTS_wz_sign: the
   second law fixes the side, not the slope].

**What this action does NOT forbid, recorded with equal weight**: any amplitude of either
modulus (no ceiling — the cone is amplitude-homogeneous per channel); any ratio x ≥ 0 (no pin);
any k-structure or ω-structure of x compatible with causality+KMS+passivity. **The action
carries the family.**

**The pre-registered termination points for "does anything fix x?", with this document's
honest landing:**
- **T1 — bath-derived suppression** (Π₀ = 0 non-perturbative): would fix x = 0, costs a new +1
  at rung3 (relocation, not discharge) [p_tt_ansatz "the one escape"; X_FLOOR_MAP D1].
  NOT reachable in-house; it is the dispatch's question.
- **T2 — the action derives a different preferred x**: would be GRUT's first positive
  prediction; subject to the D2 sub-fork and full battery + independent reproduction
  [X_FLOOR_MAP D2]. This document finds NO such derivation in the declared structure.
- **T3 — the action fixes nothing**: **THIS IS THE LANDING.** The declared field content,
  symmetries, and kernel conditions orient the channels (the floor) and fix no point of the
  family. x stays free — but now it is a named modulus of a written action with a declared
  normalization, an orientation, and its freedom stated as a function space rather than
  absorbed into a word. The difference this makes: "we assume pure-TT" becomes "here is the
  action, here is its parameter space, and here is the one function it does not fix — x, with
  three routes closed (R1 no-pin computed; u5 classifier-not-pinner computed; the anomaly
  carries no pin) and one open (rung3, external)."
- **T4 — the range question** (the fourth route this wave added): the FLOOR landed
  in-house [x_no_pin_theorem]. The CEILING is honestly out of in-house reach — an
  Israel–Stewart causality ceiling needs a relaxation time, a sound speed, and an entropy
  density, none of which exist in this corpus; it is reclassified as a rung3-dispatch
  sub-question [SPECIALIST_BRIEF_rung3_spine.md Rider C], and the borrowed node
  `relativistic_hydro_israel_stewart` (attaches_to, no depends_on) cannot supply it.

**Elasticity, answered**: "responsiveness" now means — a rank-2 field with doubled contour, the
S1–S7 inventory, two kernel channels with declared analyticity/KMS/passivity structure, one
adopted dimensionless axiom (α, conditional-theorem grade [rung9a_value]), one conjecture
(single-pole memory, external [rung3]), one hand-chosen point (x = 0 constant [p_tt_ansatz,
+1]), and one honestly-unfixed function (x(ω,k²), oriented but unbounded). Anything claimed of
"responsiveness" that is not derivable from that list is an insertion and books as one.

## 7. Part 3 — the lemma in the action's own variable

Under §5's declaration (and ONLY under it — the transfer is definitional):

    x_diss(ω) ≥ 0  pointwise in ω

— the channel-diagonal passivity floor, restated as a constraint on a FUNCTION, never an
inequality on a bare number. Recorded explicitly, per the brief, what this does NOT give:

- **No ceiling.** The admissible cone is closed under x → λx, λ ≥ 0 [calc/x_no_pin.py Part D].
- **No pin.** Every nonnegative ratio is realized; passivity selects nothing.
- **No licence to set any channel to zero.** The guard, verbatim [BRIEF_p_tt_interrogation
  KC4]: passivity "can propagate a channel's vanishing … but can never source one."
- **No unconditional statement about the STATIC modulus.** The floor constrains the
  dissipative part ω·Im c₀. A DC corollary (static susceptibility ≥ 0 via Kramers–Kronig over
  a passive spectral density) is NOT asserted, because gravitational kernels may need
  subtracted dispersion relations, and a subtraction constant breaks the positivity transfer.
  **ANSWERED (2026-08-09, `calc/kk_static_transfer.py`, prereg-sealed, staged at the gate):**
  unconditional transfer REFUTED (a passive kernel with negative static modulus exists — a
  negative contact term is invisible to passivity, causality, and the two-point KMS lock);
  conditional transfer DERIVED at the tightest class-level criterion **χ_∞ ≥ 0** (sufficient,
  not necessary — passivity gives χ(0) ≥ χ_∞ and no necessary condition on χ_∞; rung3's
  single-pole family is a sufficient subclass — the floor does not die if single-pole falls,
  and is never unconditional). The quasi-static x that `mu_slip_interior` couples to
  observables inherits a sign from this lemma ONLY conditional on the vacuum kernel's
  nonnegative instantaneous part (bath/UV structure, rung3's domain) — unconditionally, never.

*Changed-field note: this document's register-facing identifications were relayed
(RELAY_kernel_reframe_2026-08-09.md) and RULED 2026-08-09: the x ≡ normalized-c₀ declaration
accepted (R1 discharged-by-construction), the cut-conditionality qualifier applied at
zeta_interior_family, no new dial booked, and the static-transfer gap promoted to register node
kk_static_transfer.*
