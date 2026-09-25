# GRUT — THE GRAND RESPONSIVE UNIVERSE THEORY, AS ITS RECORD DEFINES IT (theory paper, working draft 01)

**Date:** 2026-09-25 · **Authority:** owner ruling on the synthesis
(`GRUT_WORKING_THEORY_01.md`, AMENDMENT 01): *turn the working theory
into the foundation of the actual theory paper; no physics fork before
this paper exists.* · **Status: WORKING DRAFT. Nothing banked. Not for
external distribution** (D-1 standing direction: external review
deferred; no outside human has reviewed any of this).

**Genre declaration.** The synthesis answered *what survived*. This
document answers: **what is GRUT as a theory, mathematically and
physically, given what survived?** It states the theory as a formal
architecture — a chain of typed objects and annotated arrows — with the
priced-input inventory as explicit axioms-of-supply, the surviving
results as theorem-shaped statements with their class scopes, and
completion defined as a finite list of mathematical requirements. Every
annotation traces to the frozen record via the synthesis; this paper
introduces no new result and promotes nothing.

**The claim-form (owner-fixed, binding):**

> GRUT identifies a hierarchy in which local microscopic dynamics can
> generate continuum spectral structure, influence functionals, memory
> and dissipation, and — given an access structure — recoverable spatial
> geometry and a constrained graviton-response sector. The program also
> identifies the specific structures that remain irreducible inputs or
> unresolved seams.

Not claimed: that GRUT derives spacetime and gravity from local
microscopic dynamics. The distance between the two statements is the
content of §6 (completion).

---

## 1. WHAT KIND OF THEORY THIS IS

GRUT, as its record now defines it, is a **generative-hierarchy theory
with an explicit priced-input inventory**. It has three kinds of
content:

1. **Derived structure** — transitions that calculations force within
   stated model classes, at the level of passing pre-registered checks.
2. **Constraint structure** — admissibility conditions (cones,
   positivity hierarchies, counting laws, selection tables) that
   restrict without selecting a point.
3. **The inventory** — the supplied inputs, each reduced by a dedicated
   attack to its smallest known form, carried openly as the theory's
   price.

A statement of GRUT that omits any of the three is not GRUT. In
particular, the inventory is not a list of embarrassments awaiting
removal: the program's audit arm (RRP-00…03, at audited scope) found the
same derived-structure/supplied-point architecture in every audited
formulation of established physics. What is GRUT-specific is *which*
structures turn out derivable and *how small* the supplied remainder has
been made.

**Notation.** 𝒜 denotes an algebra of degrees of freedom; 𝔖 the
subsystem functional (P-1); 𝔠 an admissibility cone; (K, N) ≡ (J, ν) the
Gaussian influence pair (response/dissipation and fluctuation data);
ℐ the full influence hierarchy; 𝔄 the access structure. The formal
chain below is the owner's:

    𝒪_local → 𝒞_continuum → ℐ → 𝔄 → 𝒢 → ℱ_eff → 𝒢_grav

with one structural caveat stated now: **𝔄 threads the whole chain
rather than occupying one slot.** A partition choice (an 𝔄-datum) is
already consumed upstream, in defining which variables 𝒞_continuum
retains (P-1: the kernel is downstream of an 𝔖-sector choice); the
chain places 𝔄 where its *selective* content is consumed — between the
influence data and everything reconstructed from them. Arrow
annotations below make each consumption explicit.

---

## 2. THE OBJECTS (definitions at the record's level of sharpness)

**𝒪_local — the microscopic layer.** A finite set of local degrees of
freedom with neighborhood structure and autonomous first-order passive
dynamics, under the admitted principles P0 = {strict locality; finite
microscopic content; first-order autonomy; passivity (no internal
free-energy source); time-translation invariance; standard open-system
reduction}. P0 is the definition of "derivable" at this layer. The
flag travels with it: the time-translation item is the seam S1 of §5.
The record does **not** fix a substrate ontology; it fixes the
constraint system any substrate must satisfy (ontology reconstruction,
items A1–A9), including: no forcing of substrate-level locality,
Lorentz invariance, tensor structure, or arrow; commutativity of 𝒜 has
never produced quantum structure; a finite closed linear system cannot
host the surviving influence datum.

**𝒞_continuum — the continuum layer.** The infinite-volume /
thermodynamic limit of 𝒪_local together with a retained sector R
(an 𝔖-choice). Its defining relations:

    q̇(t) = −∫₀ᵗ K_R(t−s) q(s) ds + drive
    K_R(t) = Σ_k (v_{1k})² e^{λ_k t}   (finite N)
           → ∫ e^(−t/τ) dρ(τ)          (limit; completely monotone class)

with ρ ≥ 0 (Bernstein–Widder), repeated poles excluded by passivity,
realization dimension = number of distinct eliminated modes, and
late-time class t^(−d/2) in substrate dimension d.

**ℐ — the influence structure.** The full hierarchy of multi-time
connected influence moments of retained variables: the theory's
effective interface. Its Gaussian face is (K, N); its admissibility
structure is

    𝔠_Gauss = { (J, ν) : J(ω) ≥ 0,  ν(ω) ≥ ℏ J(ω)/2 }     (Gaussian class)

lifting at matrix level to ν ± J/2 ≥ 0, and at hierarchy level to one
positive object: complete positive-definiteness of the influence moment
hierarchy — which **is** state positivity on the generated *-algebra
(an identity, not a new principle). Dynamical selection inside ℐ is by
locality + symmetry power counting on exponent classes (per-branch,
with min-dominance masking at matrix level); amplitudes and states are
never selected.

**𝔄 — the access structure.** A seed subalgebra S together with its
dynamically generated closure, and the events that change the boundary.
The record's theorems: the closure is canonical *given* the seed; the
seed is not dynamically selectable (non-injective closure,
path-dependent minimality); factorization/embedding is
representational; access-boundary changes are exactly where hidden
differences become physical; decidability of every reconstruction
question class-splits by access reach.

**𝒢 — the geometric layer.** Not a primitive: a family of functionals
of (ℐ, 𝔄) — spectral dimension estimators, hop metrics, resistance/
metric-density forms, walk-count topology invariants — whose output is
geometry **as far as access reaches** and no farther, with the dynamic
hierarchy strictly stronger than static data and the topology horizon
at circumference order. Absolute geometry is not an object of the
theory as currently defined.

**ℱ_eff — the effective sector/probe layer.** Sector classes inside the
cone; the retained gravitational-side sector class (gapless, z = 1,
locally accessible Goldstone), conditional on CARRIER; and the probe
structure: a supplied massless, gauge/Lorentz-redundant field with
universal reach, from which C_cons (conserved-current coupling) and
clock universality-under-exchange follow. The constant-probe limit is
governed by the co-stretch declaration (Sel-4x): a constant probe is a
unit change iff every intrinsic scale co-stretches — a classification,
not a selection.

**𝒢_grav — the graviton-response sector.** The (K, N)_grav hierarchy
point (vacuum on the cone floor); the exponent-class occupancy
(ω⁷-class, within-class derived, class-4 open); and the physical TT
channel: tensor structure forced, leading IR coupling forced, higher
form factors constrained-nonunique, channel existence class-split by
the retained sector's light cone relative to the probe's, ξ irrelevant
on-shell.

---

## 3. THE ARROWS (the annotated architecture — the paper's core)

Annotation key: **D** = derived (in the stated class, at check level) ·
**C** = constrained-nonunique · **S** = supplied at this arrow ·
**U** = unresolved · **red** = a preserved failed frozen gate lives
here. Sources are fork IDs; numbers are in the synthesis and verdicts.

### Arrow 1: 𝒪_local → 𝒞_continuum

| content | status |
|---|---|
| memory ⟺ persistent auxiliary state (both directions) | **D** (P1/P2; constructive converse re-banked: P3 1.4e-16, P4 distinct-modes law, E4a) |
| continuum spectra + irreversibility in the infinite-volume limit; t^(−d/2) | **D** in tested classes |
| spectral form: ρ ≥ 0, no repeated poles; uniqueness of ρ | **D** (form) / **C** (uniqueness only for light tails; gravitational kernels are heavy-tailed) |
| which variables are retained (the partition) | **S** in generic worlds / **D** where dynamics distinguishes a sector / representational under symmetry (P-1 trichotomy) — an 𝔄-datum consumed here |
| content of ρ (support, τ₀); arrow direction | **S** (six no-gos; boundary data) |
| validity beyond stationary backgrounds | **U** — seam S1: the construction assumes time-translation invariance; the physical cosmological kernel is two-time at order unity (R = 0.516) with no licensed local transport (lags ≲ 0.25/H₀ only) |

### Arrow 2: 𝒞_continuum → ℐ

| content | status |
|---|---|
| retained dynamics → its influence data | **D** (definitional given the reduction; exact in the Gaussian class) |
| Gaussian admissibility = the two-inequality cone; minimality | **D** in-class (constructive interior incl. non-KMS; false constraints counterexampled; vacuum saturates the floor) |
| the ℏ floor | **S** (located as the floor height; classical = floor removed) |
| (K,N) as the whole interface | **refuted**; hierarchy complete-as-interface in-class for declared access; first obstruction κ₄ | 
| hierarchy positivity as a new principle | **null** — reduces to state positivity (identity, so flagged) |
| discrimination ladder (first unmatched order) | **D**, with the order-8 window gate **red** (count diagnostic toward 2⁸, non-asymptotic couplings) |
| sector → exponent class | **D** (locality+symmetry counting; matrix masking modifies it, H3 eigenvalue gate **red**) |
| sector → point in class (amplitude, state) | **S** (no-pin at cone level) |
| KMS/FDT/stationarity/single-pole | states **inside** the cone, never constraints on it |

### Arrow 3: ℐ → 𝔄 (what access does to influence data)

| content | status |
|---|---|
| physical meaningfulness = change in accessible influence data | **D** (the access-relativity principle; D-1, P-5) |
| the seed | **S** (P-5/P-6: non-derived; closure canonical given it; selection attacked and refuted; one **red** at the degenerate control) |
| access-boundary changes carry physical content | **D** (post-quench split) |
| medium-vs-relational vocabulary at fixed (K,N) and S-access | representational (**D** demotion) |
| why access exists at all (observers) | **U** (unposed) |

### Arrow 4: (ℐ, 𝔄) → 𝒢

| content | status |
|---|---|
| dimension, hop metric, metric density from spectral functionals | **D** (G-2, 35/35; arrival-time route dead — G-1's eight **reds** preserved with the located obstruction) |
| elimination of genuinely different geometries within access reach (isospectral included) | **D** (GS-1) |
| dynamic hierarchy ≻ static geometry | **D** (Y–Δ: static-blind, ω²-coefficient separates, analytic match) |
| geometry under partial access | **C** (single-site families; LocPos narrows, does not select) |
| topology below circumference order | invisible (**D** horizon law) |
| absolute geometry | **U** |
| constant spatial rescaling | classified (**D** identity): co-stretch ≡ unit change; the general hypothesis false (rigid stretch observable); which one a probe performs = the co-stretch declaration (**S**) |

### Arrow 5: (ℐ, 𝔄, 𝒢) → ℱ_eff

| content | status |
|---|---|
| probe structure (massless, gauge/Lorentz-redundant) | **S** (CC-1: C_cons follows from 𝔠 only for this probe; massive probes don't force it) |
| universal reach | **S**; universality then **D under exchange** (forced ≥ 0.13 vs 9e-16; g → 0 continuous); irreducible for genuinely decoupled sectors |
| clock coupling O ~ H | **D** for generic non-integrable sectors given C_cons; structurally fails for free/integrable sectors (2R-charge towers) — the loophole L1 of §5; GeoInv the recorded, unpromoted candidate |
| CARRIER (bath = geometry carrier) | **S** — reduced to an access-seed coincidence (CA-1: four sectors carry identical geometry; the cone cuts the classical carrier, an earned cut; a non-carrier bath survives everything earned) |
| retained-sector class (gapless, z = 1, accessible Goldstone) | **D-in-class conditional** on CARRIER + probe (RS-1; flexural gate **red**); the member and its dispersion curvature **S/U** |
| full-stress coupling | permitted, not forced (**C**) |

### Arrow 6: ℱ_eff → 𝒢_grav

| content | status |
|---|---|
| (K,N)_grav admissible hierarchy point; vacuum on the floor | **D** (GR-1) |
| exponent-class selection | **D** as selected-by-structure-in-class (counterfactual battery; branch elimination structural) |
| ω⁷ | within-class **D** (dual pre-registration: exponent ω^7.008, coefficient ratio 1.0005; mechanism by counterfactuals) — program-wide **occupancy evidence only**; class-4 gate open, obstruction = the §4 inventory items are load-bearing; κ discharged |
| TT tensor structure; leading IR coupling | **D** (forced in tested class; rank 1 per point) |
| ξ on the physical channel | **D** (irrelevant; identity-grade projector algebra; survives off-shell/trace only) |
| higher TT form factors | **C** (rank-count gate **red**: 3 vs 4, the on-shell linear-sector identity; curvature restores 4); inherits Sel-4x |
| channel existence | class-split by relative light cone (**D** classification): dead at exact v = c; open ∝ subluminality; closed superluminal; under per-sector v = c units it rides **only** on dispersion curvature (**S/U** microscopic content) |
| 3D dimension-consistency | **red** (5.362 vs 6 ± 0.6, diagnostic attached, unrepaired) |
| aligned channel | dead twice over (**D**: unimposed transversality + kinematic closure); the no-go *misreading* refuted — non-aligned acoustic channel open |
| absolute amplitude (κ) | **S** (dimensionful; no-pin) |
| cross-sector light cone | **S** — seam S2 of §5 |

---

## 4. THE INVENTORY (the theory's axioms-of-supply)

The complete list of what GRUT currently supplies rather than derives,
each at its smallest attacked form. Per AMENDMENT 01: most structural
items collapse into two stems; the quantum and boundary-data items are
separately priced.

**Stem A — access:**
- **I1** the access seed (P-6: non-derived, path-dependent, physical at
  boundary changes) — and with it **I2** CARRIER, reduced to a seed
  coincidence (CA-1).

**Stem B — probe structure:**
- **I3** the massless, gauge/Lorentz-redundant probe (CC-1);
- **I4** universal reach (U-1);
- **I5** the co-stretch declaration Sel-4x (SX-1);
- **I6** the cross-sector light-cone relation (TT-1; = seam S2).

**Separately priced:**
- **I7** ℏ (the cone's floor height — located, not derived);
- **I8** the Born measure and outcome selection (routes tested,
  negative);
- **I9** noncommutativity of 𝒜 (emergence untested-to-failed);
- **I10** states and boundary data: sector amplitudes and states
  (no-pin), the arrow's direction, the low-entropy past; on FRW
  additionally a state choice, a temperature structure, and a proved
  stationary reduction (kernel-transport verdict);
- **I11** microscopic sector content: ρ's support and τ₀; the retained
  sector's dispersion curvature (the TT channel's existence rides on
  it).

An inventory item is discharged only by a chartered derivation or
formally established as irreducible by a principled argument (the C5
criterion of §6); nothing else moves it.

---

## 5. INTERNAL CONSISTENCY: SEAMS, LOOPHOLE, RED REGISTER

**The assembly test passed** (synthesis §11): no arrow of §3 consumes
an assumption another fork eliminated. What remains are two seams — 
missing constructions, not contradictions — one loophole, and the red
register.

- **S1 — the stationarity seam.** Arrow 1 is derived under
  time-translation invariance; the physical cosmological kernel is
  two-time at order unity with no licensed local transport. The
  microscopic → continuum construction and the cosmological sector do
  not yet meet. (Completion problem C1.)
- **S2 — the causal seam.** 𝒢 is spatial; the causal relation between
  sectors — exactly what 𝒢_grav's existence split turns on — is
  supplied (I6). The one earned road toward it is exchange (U-1's
  forcing), which stops at I4. The theory has an earned spatial layer
  and a supplied causal layer, not yet unified. (C2.)
- **L1 — the free-sector loophole.** The clock-coupling derivation is
  forced for generic interacting sectors and structurally fails for
  free/integrable ones — and the gravity-side retained sector (free
  phonons) sits in the exception class of the universality argument
  used on its own coupling chain. Not a contradiction; a
  self-consistency demand: the architecture does not yet explain why
  this sector may be the carrier without importing more structure
  (GeoInv is the recorded candidate, never promoted). (Feeds C3/C7.)

**Red register (all preserved, none repaired):** G-1's eight
(arrival-time metric program); GR-1's 3D gate (5.362 vs 6 ± 0.6); P-6
degenerate-companion (0.0); P-3 H3 eigenvalue (+2.216; masking); P-4
order-8 window (67.8); EQ-1 static discriminator (claim withdrawn);
RS-1 flexural (R ~ N·d²); TT-1 form-factor rank (3 vs 4). A theory
statement contradicting a red gate is out of bounds until the gate is
green by measurement.

**Integrity rule carried:** five documented narrative-vs-run instances
are on record; checks outrank prose; every status in this paper traces
to a frozen check outcome or an owner ruling.

---

## 6. WHAT WOULD CONSTITUTE COMPLETION OF GRUT

Completion is defined here as a finite list of mathematical
requirements — not an experiment queue. Each problem states what
success is and what a principled irreducibility verdict would be; both
outcomes complete that item. Order is the owner's; no problem is
opened by this document.

**C1 — Unify the stationary microscopic construction with
non-stationary backgrounds.** *Success:* an infinite-volume /
retained-sector construction (Arrow 1) on a background with ε = −Ḣ/H²
of order unity, producing a two-time K(t,t′) whose measured
non-stationarity (R ≈ 0.5 class, same-lag drift order unity)
is *derived* rather than measured — or a theorem that the Layer-I
limit commutes with slow background evolution in a stated regime.
*Irreducibility form:* a no-go showing the P0 construction cannot be
extended off stationary backgrounds without a new priced input, with
the input named. *Status:* seam S1; nothing committed attempts it.

**C2 — Derive or explain the causal/light-cone structure.** *Success:*
an earned construction of a common causal cone across
exchange-coupled sectors from influence/access data — the causal
analogue of GS-1's spatial eliminations — turning I6 from supplied to
derived-under-exchange, the way U-1 did for clock universality.
*Irreducibility form:* a demonstration that relative cone data cannot
be extracted from any influence hierarchy at declared access (a D-1/
P-4-style interface-completeness argument applied to causal order).
*Status:* seam S2; U-1's exchange forcing is the only earned foothold.

**C3 — Account for the access seed.** *Success:* a selection principle
for the seed that survives the P-6 battery (non-injectivity,
path-dependence, degenerate controls) in a strictly larger class than
the ones that refuted minimality/closure — or a derivation that seeds
are physically equivalent up to the boundary-change events that P-5
proved contentful. *Irreducibility form:* elevation of the seed to an
explicit axiom of the theory with its measured content (the
access-relativity principle) stated as the axiom's consequence.
*Status:* stem A; the observer question (unposed) lives here; L1
partially feeds it via CARRIER.

**C4 — Account for the massless probe structure.** *Success:* deriving
any of I3–I5 from earned structure — e.g., a demonstration that only a
gauge-redundant massless probe with universal reach is admissible
against the cone plus the retained-sector class (the CC-1 positivity
route generalized from "follows for a supplied massless probe" to
"forced among declared alternatives"). *Irreducibility form:* a
classification proving the probe structure is an independent axis of
the theory's model class (a CC-1/U-1-grade battery whose alternatives
all survive). *Status:* stem B; CC-1/U-1 mark the boundary precisely.

**C5 — Derive the quantum scale and outcome structure, or formally
establish them as irreducible.** *Success (scale):* a generative
account of the cone's floor — why ν ≥ ℏJ/2 with this ℏ — beyond its
located geometric meaning. *Success (outcomes):* a derivation of the
Born measure that survives an Experiment-P-grade adversarial battery.
*Irreducibility form:* a theorem-shaped negative in a declared class
(the record already holds route-failures, not yet a classification).
*Status:* separately priced (I7–I9); untouched by the campaign by
design.

**C6 — Resolve the gravity-consistency red gates.** *Success:* the
GR-1 3D gate green by measurement on a refined instrument whose
refinement rule was frozen in advance (the existing diagnostic's
5.36→5.49→5.66 trend is a hypothesis for that instrument, not a
result); disposition of the TT-1 rank count under the now-identified
on-shell identity; the P-3 masking law confirmed or bounded at
eigenvalue level. *Never:* prose reinterpretation of a red gate.
*Status:* red register, §5.

**C7 — Confront the retained-sector construction with the external QFT
anchor.** *Success:* the T3 confrontation run as pre-registered — the
derived matter-side kernel class mapped onto the certificate's
in-window observable (ω ≳ 3.4H, branch-cut class, dissipative sign)
with the mapping frozen before numbers; agreement at exponent-class
level is the first discriminator-grade internal support, mismatch
kills the gravitational identification at a certified wall. L1 (the
free-sector loophole) must be addressed in the mapping's premises:
the confrontation is only as meaningful as the sector selection it
assumes. *Status:* protocol adopted (2026-09-24); the mapping run has
never been executed; dispersion curvature (I11) is one candidate
input *inside* this problem rather than a free-standing next
experiment.

**Completion, stated:** GRUT is complete as a theory of its domain when
every item C1–C7 is closed — each either by derivation or by a
principled irreducibility verdict that converts the corresponding
inventory item into a declared axiom. The theory then consists of: the
axioms (the surviving inventory), the derived hierarchy of §3, and the
kill conditions of §7. Nothing in this definition requires that the
inventory empty; it requires that its boundary be *proved* rather than
merely recorded.

---

## 7. FALSIFIABILITY AND NON-CLAIMS

**Kill conditions (standing):** the T3 confrontation (C7) at a
certified wall; any measured K_R requiring a non-positive measure or
repeated poles (falsifies the derived form constraints — deeper than
the gravitational identification); the DESI w(z) channel (armed, not
sealed: the no-crossing export is held to-derive, gated on its
anchor). A cone violation — realizable Gaussian influence data outside
𝔠_Gauss — would falsify the admissibility layer in-class.

**Non-claims:** no observable prediction beyond the kill channels; no
Standard Model content (silent); no derivation of quantum mechanics,
ℏ, or Born statistics; no absolute geometry; no substrate ontology
(a constraint system on candidates, A1–A9); the historical claim set
(pre-2026-09-23) closed. Named obstructions carried: Weinberg–Witten
(named-exit condition), soft-graviton universality (= the priced
probe, I3–I4), Lorentz recovery (open), Bianchi/energy bookkeeping of
a dissipative gravitational sector (open). Nearest relatives
(Caldeira–Leggett, stochastic gravity, induced gravity, Jacobson) are
comparisons, not support; GRUT's differentiator, if C7 ever passes, is
the direction of the identification.

---

## 8. GOVERNANCE

- Evidence base: `GRUT_WORKING_THEORY_01.md` (as amended) and, through
  it, the frozen record — 22 campaign forks, the foundations chain,
  the adjudicator-track skeleton v02.1, the stratum-1 register at
  recorded strength. This paper cites through the synthesis; where the
  two disagree, the frozen verdicts win and both documents are amended
  by dated entry.
- Fences honored: no absolute exponent computed or compared to 7; ω⁷
  occupancy-only outside its scoped within-class row; v3 closed; ℏ
  located-not-generated; operator ordering fenced; Λ_R / Matsubara /
  Π₀ / U5 untouched; no external dispatch.
- Status changes in this paper occur only by: a chartered fork's
  verdict + owner ruling (for physics), or owner edit / dated
  amendment (for text). Working-draft versioning: successor drafts are
  `_02`, `_03`, …; this file is never silently rewritten.

## HARD STOP

Working draft 01 recorded. No physics fork is opened; per the owner's
ruling none opens before this paper exists — it now exists, as a
draft. The decision this stop waits on: **the owner reads the draft
and rules — amend the architecture, iterate the draft, or select from
C1–C7.**
