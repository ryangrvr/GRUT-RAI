# RPRIME_ADJUDICATION_01 — RESULT

**OUTCOME: R′_UNRESOLVED — demonstrated, not assumed. R′_ADOPTED is excluded on the
record. R′_REJECTED is not established either. The owner's ruling (R′ NOT ADOPTED)
stands as the status quo; the mode stays in any loop.**

Executed 2026-09-16 under `RPRIME_ADJUDICATION_01_PROTOCOL.md`. Process, in order: a
read-only quotation audit of the protocol itself (SOURCE_FAITHFUL_WITH_CORRECTIONS —
its corrections were fed to every downstream role); surveyor (every boundary/slice
declaration, temporal and spatial, from full reads of all named sources); adjudicator
(the owner's six items); adversarial checker (CONFIRMED_WITH_CORRECTIONS; every
relied-on quotation verified; **no IR computation performed — verified**; six
corrections, all applied below; nothing refuted). Zero register edits.

## 1. The finding that decides it: the contract's boundary declarations are temporal only

Established by reading (surveyor: all sources read in full; adjudicator and checker each
re-ran the vocabulary sweep — falloff / spatial infinity / periodic / box / compact
support / decay / normalizable / square-integrable / large gauge / large diffeo / tempered
/ zero mode / constant mode — across the sixteen named sources and then repo-wide):
**the listed vocabulary returns ZERO hits in the contract sources (tier2, tier3,
`wall_a4_response_flat.py`, the K_R owner ruling and execution charter, A3 v1/V2/V3/V4, the
D4 audit, `S_IF.md`). The only occurrence of "boundary condition(s)" in any executed
contract instrument is the section header `wall_a4_response_flat.py` line 432,
"=== A4-6: BOUNDARY CONDITIONS ===", whose single check is the shared retarded prescription
plus the η → −∞ coincidence clause. The sources are full of spatial content (e^{+ikz},
S^{d−1} averages, the d^dk measure); what is absent is any spatial BOUNDARY or
equivalence-class DECLARATION.** (Repo-wide, the vocabulary hits only questions and
inferences — the target spec, this adjudication's own files — never a declaration.)

What the sources DO declare about the slice, exhaustively: the bath mode is *"spatial
wave e^{+ikz} with k > 0"* (`wall_kr_tier2_massless_bath.py` line 396) with `k` and `q`
declared `positive=True` (tier2 line 157; tier3 line 116); the mode sum is
*"int d^dk/(2pi)^d"* with measure Ω_d(2π)^{−d} k^{d−1} (tier2 lines 593, 646, 650; tier3
`MEAS` lines 544–545) and angular average *"over S^{d-1}"* — no bounds written; the IR end
is *"dimensional continuation ONLY; NO explicit IR scale"* (`K_R_CONTRACT_OWNER_RULING.md`
§4) with *"split point k0 arbitrary"* and *"NO IR scale is introduced"* (tier2 lines
600–604); S6 background homogeneity/isotropy (`S_IF.md` §2) with *"No symmetry beyond
these is declared."* **No source declares any falloff, decay-at-infinity, periodicity,
box, compact-support, or normalizability condition on h_ij or on the gauge parameter over
the spatial slice.**

**Two protocol premises were corrected by the audit and are corrected here:** (i) the
"positive frequency … far past η → −∞" clause I quoted is the *matter-side* A3
declaration (Declaration 2), not the graviton contract's — the executed contract
scripts contain no far-past clause at all (tier3 has no occurrence of "BD" or "Bunch";
the bath is imported as *"frozen Tier-2 forms"*); the contract's state is *"BD-analogue
via the Option-B adiabatic route"* executed as *"positive frequency e^{-iku}"* with the
exact mode *"h_k(u) = N e^{-iku}[(1-Hu) + iH/k]"* (tier2 line 17; line 730 records it as
*"h_k = e^{-iku}[(1-Hu) + iH/k]"* with the normalization carried separately). (ii) My "no mechanism / fixed by fiat"
reading of Declaration 5's *"and fixes the C_i"* was **wrong and is withdrawn**: the
checker showed the coincidence prescription (ζ^μ → 0 as η → −∞) applied to a
time-*independent* C_i(x) forces C_i(x) ≡ 0 for every x — a stated mechanism, matching
v1's *"removes both C(x) and the spatial freedom"* and V2's *"the surviving freedom is
time-independent spatial reparametrisation, all removed — stands."*

## 2. The six items (checker-corrected)

1. **Local gauge status** — restated from Wall-A: *"EXACTLY a linearized
   diffeomorphism, L_ζ g for ζ^i = ε_ij x^j/2 (all components, computed)"*, *"with a
   gauge parameter bounded on the patch"*. Free-leg level.
2. **Global behavior** — ζ ~ x is unbounded on the R³ continuum the contract uses. The
   executed gauge apparatus structurally cannot represent it: the Tier-3 Ward image at
   k_ext = 0 has components only in e_00 and e_0i (`wall_kr_tier3_loop.py` lines 238–240)
   — the plane-wave orbit at zero spatial momentum has no spatial-block direction at all
   (surveyor's reading, filed in the companion `.json`); and the symbol domain k, q > 0
   (`positive=True`) places the constant mode outside the executed internal legs' symbol
   domain by assumption — the k → 0 endpoint is nonetheless evaluated by dimensional
   continuation (tier2 lines 594–604: *"its k -> 0 evaluation is finite ONLY for d > 3 --
   at d = 3 the IR portion is the scaleless pole"*), so this is an assumption about the
   symbol, not an exclusion of the IR endpoint from the calculation. **[INFERENCE from the quoted construction]** the mode
   lies outside the declared gauge parametrization, not inside its quotient.
3. **Boundary condition** — temporal, declared (state prescription; retarded ω + i0
   analyticity; the damped Δ-transform); spatial: **none, established by reading**
   (§1). The record's own implicit assumptions, tagged: the Fourier representation
   presupposes Fourier-transformable configurations on R^d; `positive=True` excludes
   k = q = ω = 0 from the symbol domain by assumption; the per-mode normalization chain
   is silent on the k → 0 sector; the D4 plane-wave orbit presupposes the gauge parameter
   is itself a plane wave at the same k.
4. **Relation to Declaration 5 — SUBFAMILY, by construction.** The TT-bath residual
   family is written in **no source** (tier2 has zero occurrences of gauge / zeta / xi /
   diffeo; the bath is the ansatz *"g = a^2(u) diag(1, -1+s, -1-s, -1)"*, line 207).
   **[INFERENCE, elementary]** any transformation preserving the TT-bath conditions
   (h_0μ = 0 + traceless + transverse) preserves the synchronous conditions, so it is a
   subfamily of Declaration 5's; the Wall-A generator is its C = 0 linear member.
   Subfamily membership does not transfer the prescription's *role*: Declaration 5 is a
   coordinate fixing of the *external* synchronous representative for a different object
   (the matter loop), disposed of kinematically at ω ≠ 0 (`wall_a4_response_flat.py`
   A4-6: *"zero-frequency family, empty at the omega != 0 kinematics used here"*).
   Transfer as the TT-bath boundary condition: **impermissible on either reading of
   STEP 10** — its exhaustive *"the only things that carry are VALIDATED MACHINERY … and
   the sign DICTIONARY"* forbids a physics-content prescription if STEP 10 governs; if it
   governs results only, the transfer falls to the owner's declaration domain. **And
   insufficient even if declared**: a gauge-parameter condition at *temporal* infinity
   does not declare the small/large split, which is a statement about the field
   configuration space at *spatial* infinity.
   **The conflicting on-record signal (checker):** Declaration 5's literal family, with no
   growth class, *names the Wall-A generator as residual freedom* — an adopting-direction
   signal in force at contract scope via D2 = 2a — countered by the D4 plane-wave orbit
   statements and Wall-A's *"gauge status undecided."* **The ground for UNRESOLVED is
   conflicting on-record signals at the k = 0 endpoint plus the absence of any field-side
   boundary declaration — not silence alone.**
5. **Observable meaning.** *Under quotient:* configurations h_ij and h_ij + ε_ij over the
   whole slice declared the same state. **[INFERENCE, free-leg level]** coherent for
   patch-localized observables (the static master variable is *"identically blind to
   that mode"* — free-leg; the coupling is *"loop-level with its gauge status
   undecided"*). For slice-wide observables — **[INFERENCE]** the contract's declared
   class, from *"probe = a long-wavelength TT metric perturbation"* (`K_R_CONTRACT_EXECUTION_CHARTER.md`
   STEP 1) and D1 = 1a's
   *"'long-wavelength probe' IS k → 0 taken first"*, executed at p₁ = (ω,0,0,0),
   *"x-independent over the WHOLE infinite comoving slice"* — the quotient declares the
   slice's constant shear (boundary data at spatial infinity) unobservable, which is
   incoherent unless declared. *Under retention:* the mode is distinguishable only by
   what the contract's declared observable class can see; the checker struck my
   imported standard-physics conclusion (soft-graviton consistency relations presuppose
   a loop-level Ward identity the record's T3-8 reports NONZERO) — **no conclusion is
   imported; the standard literature on adiabatic tensor modes and large
   diffeomorphisms is cited for orientation only.**
6. **No IR calculation** — affirmed; checker-verified: no loop, no small-q class, no
   finiteness statement under any relation.

## 3. Why UNRESOLVED and not the other three

- **R′_ADOPTED — EXCLUDED on the record.** No declared condition, temporal or spatial,
  establishes h ~ h + ε over the slice; every declared and executed element (TT-bath
  P^TT × W contraction; positive-k symbol domain; finite-amplitude plane-wave orbit with
  no spatial-block direction at k_ext = 0; S5 — diffeomorphism invariance *"with its
  banked Ward limitation"* (`S_IF.md` §2), **[INFERENCE]** transversality at fixed k;
  D3(iii) scoping alternative gauge content out) *retains* the mode; Declaration 5 cannot be transferred (item 4).
  The framework-favorable trap is avoided at the definition.
- **R′_REJECTED — NOT established, deliberately.** It would convert the contract's
  *silence* about the spatial boundary into a positive declaration that the slice-wide
  constant shear is physical — deciding a frozen object's meaning from vocabulary rather
  than source. **The strongest REJECTED-direction reading, named (checker):** retention
  by declared continuity — D1 = 1a makes the probe the k → 0 limit of finite-k plane
  waves; the continuum has no lower limit; the D4 identity holds at every finite k. Why
  it is construction, not declaration: D1 governs the *external* probe (and Tier 3
  executed k_ext = 0 exactly, not the limit); **[INFERENCE]** dimensional continuation fixes *how* the
  endpoint is evaluated, not *whether* configurations at it are identified (the ruling
  says only *"IR: dimensional continuation ONLY; NO explicit IR scale"*).
  **Operationally, R′_REJECTED and R′_UNRESOLVED coincide today: the mode stays in any
  loop.** They differ in what the record *says* — and that difference is the point.
- **R′_CONDITIONALLY_ADOPTED — not selected**, because the two admissible declarations
  resolve R′ in *opposite* directions and the contract leans neither way (§4).

## 4. The missing declaration, named, and its two candidate forms, priced

**Missing:** a contract-scope declaration of the spatial boundary / equivalence class of
the TT-bath internal legs — three coupled items no source contains: (i) the admissible
**growth class** of gauge parameters ζ^i(x) counted as redundancies (is |ζ| = O(|x|) a
redundancy of the bath or a symmetry acting on physical data?); (ii) equivalently, the
**boundary class** of h_ij at spatial infinity (decaying / bounded / constant admitted);
(iii) the **observable class** for which the equivalence is asserted (the k → 0 plane-wave
probe of D1, or horizon-localized windows). Also required before any reuse of Declaration
5 for this purpose: a *written* TT-bath residual family, and a mapping of the η → −∞
prescription from the chart a = −1/(Hη) onto the executed chart a = 1/(1−Hu).

- **Candidate A — RETAINING declaration** (a falloff class on h_ij at spatial infinity, or
  a boundedness class on admissible ζ, excluding O(|x|) parameters as redundancies).
  Price: one new register input, +1 **[INFERENCE from the ledger's pricing rule]**.
  Relocation: none into the IR prescription; it converts the executed
  *retention-by-construction* into *retention-by-declaration* — the slice-wide constant
  shear becomes declared physical boundary data, and the fired sector's status at that
  locus becomes an input rather than a finding. R′_REJECTED by declaration; **GRUT takes
  the hit by declaration.** Consistent with D1 = 1a, S6, and the no-IR-scale ruling as
  they stand.
- **Candidate B — ADOPTING declaration** (an equivalence admitting O(|x|)
  time-independent ζ as redundancies). Price: one new register input extending S5
  beyond *"No symmetry beyond these is declared"*, +1; PLUS a coherence condition — an
  observable-class declaration restricting the contract's observables to those blind
  to the boundary shear (horizon-localized windows), or an explicit declaration that the
  shear is unobservable; PLUS a written TT-bath residual family and R′-invariant leg
  variables (Gate B's construction, not authorized). **Relocation: YES** — "the constant
  mode is gauge" moves from the bath's gauge structure into the observable class L, in
  tension with D1 = 1a's slice-wide plane-wave limit and the executed k_ext = 0
  evaluation point; either L is amended (a change of the declared object) or the shear
  is declared unobservable. **[INFERENCE, tagged per the checker]** on the executed
  domain (k, q > 0) R′ has no configuration to act on and touches the object only through
  the treatment of the k → 0 endpoint — the same endpoint the IR prescription governs;
  its pricing route (through fork (ii) or as its own declaration) is the owner's.

**The adopting declaration carries the larger price and relocates an assumption; the
retaining declaration names what the construction already does.** The contract leans
neither way by declaration.

## 5. Housekeeping fences (from the adjudication; none acted on)

No downstream document should cite Declaration 5 as the TT-bath prescription's boundary
condition. The D4 audit restates the *superseded* v1 residual family — do not propagate
it. Wall-A's "BD at η → −∞" wording in its (O,D,L,R) should not be cited as a contract
instrument clause (the contract scripts carry none). The target spec's R′ family
definition remains a [HYPOTHESIS] until the owner writes the TT-bath residual family and
its boundary class down. Name collision noted: "U3 S6" (the selector) ≠ S_IF "S6"
(homogeneity/isotropy).

## 6. Recommendation to the owner

R′ stays NOT ADOPTED. If the question is to be decided, the missing declaration (§4) must
be made as a new contract-scope input, on the record, **before** any R′-dependent
computation and never revised after a class is seen. The two candidates are priced; they
point in opposite directions; the choice is a physics declaration about the slice, not a
bookkeeping act. **R′_ADOPTED ⇏ IR finite** under any of this.

---

*Filed 2026-09-16. All roles' filings (protocol audit, surveyor, adjudicator, checker) and
the pre-commit quotation audit of this result (SOURCE_FAITHFUL_WITH_CORRECTIONS, seven
corrections applied) are in the companion `RPRIME_ADJUDICATION_01.json`, written in the
same commit. Fork (ii) gated; Wall-A HARD STOP; D3(iii) and D4-A
untouched; nothing banked; no IR computation.*
