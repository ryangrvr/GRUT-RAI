# GRUT ToE v4 — The Core Derivation Chain (Foundation Lock)

*Organ #2 of the v4 build. The spine narrates the universe forward; this document does
something narrower and harder. It takes the foundation — the four inputs, the one
constitutive law they assemble into, and the handful of core results that law forces — and
audits it as a **skeleton**: every node at its true tier, every edge with its real
premise-set made explicit, every edge tagged by how much weight it actually bears. The
goal is not to re-tell the story. It is to find out, before v4 expands into per-sector
contracts, exactly where the foundation is **welded** and exactly where it is merely
**jointed by an unstated premise**. A known gap, named plainly, is worth more than a
varnished edge.*

---

## 1. Purpose — locking the foundation before expansion

A theory expands safely only from a load-bearing core. v4 is about to grow per-sector
contracts (cosmology, dark sector, flavor, the Standard Model). Each of those contracts
will *inherit* the foundation. If a foundational edge is silently overclaimed — a HOSTED or
OPEN result quietly tiered as DERIVED — every contract built on it inherits the overclaim,
and the whole structure fails on contact with a referee at the worst possible moment: deep
in a downstream sector, far from the actual seam.

So before expansion we lock the core. "Locking" here means: trace the foundational inputs
into the constitutive law, trace the law into its core results, and **audit every edge**.
An audited edge carries one of three tags.

- **SOLID** — a genuine derivation from the stated premises, with no hidden assumption. If
  you grant the inputs named on the edge, the conclusion follows. Proven-tier.
- **COMPUTED** — a real derivation, but parameter-dependent. It needs the adopted value
  α = 1/3 and/or the anchored value τ₀, and it inherits whatever is open about those. The
  premise is **named, not hidden** — this is honest, but it is not zero-input.
- **DOTTED** — a gap. The edge does **not** close without a premise that is not supplied by
  the inputs on the edge. The missing premise is named. The dotted edges are where the
  foundation needs shoring; they are the prioritized output of this document (§5).

One discipline rule decides the borderline cases: **an edge tag reflects whether *what the
edge claims* holds, not whether everything one might wish were true holds.** An edge that
honestly delivers a form-class and explicitly hands a sub-problem to a later edge is SOLID
for the form-class — the sub-problem's gap is charged to the edge that owns it, not
double-counted here. (This rule resolves the one place the four independent audit maps
disagreed; see E1 in §4.)

A second rule: **an identity is not an edge.** A Fourier transform of the law into the
susceptibility adds no derivational content — it is the same object in another
representation. Such steps are flagged, not tagged, so they cannot be miscounted as
derivations.

All numbers below were re-verified in `.venv` (`numpy`/`sympy`). All nodes and edges are
grounded in a specific `file:line` and a registry tier in `grut/toe/registry.py`. Tiers
match the spine `theory/GRUT_V4_SPINE.md`; nothing is inflated.

---

## 2. The foundational nodes — {Q, F, D, α}

Four inputs feed the constitutive law. Exactly **one** of them is a true zero-input proven
theorem. The other three are **[SPLIT]** — part derived, part assumed — and the split is
where the honesty lives.

### Q — the in-in causal arrow

The Closed Time Path (Schwinger–Keldysh) action with the influence functional vanishing on
the diagonal (S_IF = 0 when φ₊ = φ₋), the closed-closed propagator identically zero, the
retarded kernel vanishing for t < 0, and FDT/KMS tying the noise to the dissipation with
N ≥ 0. Scale-free: Q contains no τ₀, no τ_micro, no α.

- **Tier: DERIVED.** A proven theorem of the formalism — the **only true zero-input SOLID
  node** in the graph. The four structural legs (field doubling, variation principle,
  causality, FDT/KMS) are verified on a concrete driven-oscillator example.
- **Grounding:** `grut/foundation/ctp_action.py:42-225` (`verify()` returns 5/5 True);
  registry `ctp_action_structure` tier=computed, `registry.py:451`. It is the highest-fanout
  claim in the registry (32 downstream dependencies).

### F — finite single-pole memory  **[SPLIT]**

The susceptibility χ(ω) = α/(1 − iωτ₀), equivalently the constitutive law τ₀ż + z = z_target,
equivalently the exponential kernel K(t) = (1/τ₀)e^{−t/τ₀}Θ(t). One object, three forms.

- **Tier: HOSTED [SPLIT].** The single-pole **FORM** is *derived* — it is the
  Mori–Zwanzig Markovian limit of a slow dissipative variable, exact to O(τ_K/τ₀). But F
  *as a pillar*, and the **VALUE** of τ₀, are postulated/anchored.
- **The split matters because the converse is false.** Q alone does **not** force
  single-pole-ness. Passivity (Herglotz) is strictly weaker than complete monotonicity: a
  passive kernel can carry negative Debye weight or off-axis poles (e.g.
  1/(1 − iωτ₀ − ω²τ₁²) is passive yet decomposes with a negative weight). The registry
  states this in so many words: *"single-pole-ness is NOT a theorem of Q alone."*
- **Grounding:** `grut/derivation/phi_munu/mori_zwanzig_kernel.py:21-43` (8/8 verify);
  registry `finite_memory_form_from_q` `registry.py:5270` (notes the false converse,
  `:5287`), `first_order_from_mori_zwanzig` `registry.py:5414` (computed),
  `tau_0_derivation` `registry.py:180` (value anchored).

### D — broken adiabatic dilatation redundancy  **[SPLIT]**

The Weinberg adiabatic spatial-dilatation mode is an exact gauge redundancy in the L₀ → 0
limit; the one proper length L₀ = cτ₀ breaks its boundary charge at O((L₀k)²),
non-anomalously (a diffeomorphism, measure Jacobian ≡ 1, so α does **not** enter).

- **Tier: OPEN [SPLIT].** The **breaking** is derived and non-anomalous. But the underlying
  L₀ → 0 redundancy itself is **presupposed** — imported from Weinberg, not re-derived from
  the CTP action — and one residue, the scale-free in-in initial-state condition
  (GAP-1, n_s = 1), is OPEN.
- The registry is explicit: *"The theorem establishes the BREAKING; it presupposes (does
  not re-derive) the underlying L0->0 redundancy."*
- **Grounding:** `theory/GRUT_V3_ORGANIZING_STRUCTURE.md` (Bridge D); registry
  `adiabatic_dilatation_redundancy_nogo` tier=computed, `registry.py:5219` (presupposition
  noted ~`:5260`).

### α = 1/3 — the adopted dimensionless axiom  **[SPLIT]**

The single dimensionless input. It sets the DC response amplitude χ(0) = α, the refractive
index R = √(1+α), and the screening S = 12π/α².

- **Tier: OPEN [SPLIT].** The value 1/3 is **adopted** (foundational by adoption). The
  *conditional* theorem a/c = 1/3 for a single real conformally-coupled scalar
  (Komargodski–Schwimmer / Duff) is **proven Fraction-exact**. But the *antecedent* — that
  the gravitational conformal mode IS the IR carrier of the vacuum susceptibility — is OPEN.
- This is **the single most load-bearing open gap** in the framework. The registry flags
  it as *"the most load-bearing open gap in v3."* It fans out maximally: R, S, and Ω_Λ all
  carry `deps=(alpha_vac_derivation, …)`, and ±0.07 in α moves Ω_Λ by roughly one order.
- **Grounding:** `grut/foundation/conformal_mode_scalar.py` (a/c = Fraction(1,3), 9/9
  verify); registry `alpha_vac_axiom` tier=foundational, `registry.py:238`;
  `alpha_vac_derivation` tier=**open_negative**, `registry.py:274` (notes `:329`).

---

## 3. The hub — the constitutive law τ₀ż + z = z_target[z]

The load-bearing equation. Every sector is a regime of it. It assembles from {Q, F, D} as
follows, and the real premise-set is the point.

- **Q supplies the form-class.** The CTP variation δS_CTP/δz_a|_{z_a=0} = F[z_r] yields a
  *causal, retarded, passive* (Herglotz) relaxation structure: a response-to-the-past
  toward a target, with FDT fixing the noise. This is genuine and zero-input — but it is
  only the form-*class*. It does not by itself pick out a single pole.
- **F upgrades the form-class to the law.** The Mori–Zwanzig Markovian limit of a single
  slow dissipative variable collapses the generic Herglotz form to the specific single pole
  χ = α/(1 − iωτ₀) ⇔ τ₀ż + z = z_target, exact to O(τ_K/τ₀). The first non-Markovian rung
  goes off-axis (dark-capable) only if τ_K > τ₀/4; GRUT's anchored hierarchy
  τ_micro/τ₀ ~ 1e-34 forbids it. The **value** τ₀ rides in here as an anchor.
- **D supplies neither the form nor the law, but the structural reading.** D is *not* a
  route to the hub. It certifies that the hub's one proper length L₀ = cτ₀ is the
  controlled, non-anomalous breaking of scale-freedom, and confines the law's nontrivial
  action to the **tensor** sector. That confinement is what later makes the linear-scalar
  consequence μ_linear = 1 clean.
- **α supplies the normalization, not the dynamics.** α sets the DC amplitude χ(0) = α and
  fixes S = 12π/α². The hub's *dynamics* — the τ₀ relaxation — is α-independent.

**Real premise-set of the hub:** {Q (form-class, zero-input) + F-form (MZ, given the
slow/fast separation) + α (normalization) + the anchored τ₀ (scale)}, with D as the
structural confinement. The hub is therefore **DERIVED-as-synthesis [SPLIT]**: the *form*
is derived; the law-as-pillar, the τ₀ value, and α's antecedent are taken in, named.
Registry `constitutive_equation` tier=computed, `registry.py:496` (deps=ctp_action_structure).

---

## 4. The edge table — the skeleton

Every edge from→to, its derivation, its real premise-set, its final tag, and its grounding.
This is the load-bearing output. **Final counts: 3 SOLID, 3 COMPUTED, 5 DOTTED**, plus one
step (E5) flagged as a **definitional identity — not an edge**.

| # | Edge | Derivation | Real premises / hidden assumption | Tag | Grounding |
|---|------|-----------|-----------------------------------|-----|-----------|
| **E1** | Q → HUB | CTP variation gives the causal/retarded/passive (Herglotz) **form-class** of the relaxation operator. | **Only** causal+passive form-class. Does **not** supply single-pole-ness — that is explicitly handed to F (E2), not smuggled here. No α, no τ₀. | **SOLID** | `ctp_action.py:55-107`; registry `finite_memory_form_from_q` `:5270` |
| **E2** | F → HUB | The single pole is the Mori–Zwanzig Markovian limit of one slow dissipative variable, exact to O(τ_K/τ₀). | Needs the slow/fast separation τ_K ≪ τ₀ (= "z is slow", stated) **+ the anchored τ₀ value**. Off-axis dark pole needs τ_K > τ₀/4; GRUT's ratio ~4.2e-34 forbids it. | **COMPUTED** | `mori_zwanzig_kernel.py:21-43`; registry `first_order_from_mori_zwanzig` `:5414` |
| **E3** | D → HUB | D reads the hub as the controlled breaking of the L₀→0 redundancy; supplies L₀ = cτ₀ and the tensor-sector confinement. | Presupposes the imported Weinberg L₀→0 redundancy **+ OPEN GAP-1** (scale-free in-in initial state). D is the *structural reading*, not a form-input — one notch short of "forced from Q." | **DOTTED** | registry `adiabatic_dilatation_redundancy_nogo` `:5219` (`:5260`) |
| **E4** | α → HUB | α sets the DC amplitude χ(0) = α and S = 12π/α² = 108π. | The dynamics is α-independent; only the amplitude/normalization needs α. Inherits α's **open antecedent** (IR-carrier). | **COMPUTED** | `conformal_mode_scalar.py`; registry `alpha_vac_axiom` `:238`, `alpha_vac_derivation` `:274` |
| **E5** | HUB → χ / kernel | Fourier transform of the law: τ₀ż+z=z_target ⇔ K(t)=(1/τ₀)e^{−t/τ₀}Θ(t) ⇔ χ=α/(1−iωτ₀). | sympy: FT[α·e^{−t/τ₀}/τ₀] − α/(1−iωτ₀) = 0. **One object, three forms.** Single-pole content already bought at E2. | **IDENTITY — flagged, not an edge** | `closure_protocol.py:497-524`; registry `memory_kernel_form` `:516` |
| **E6** | χ → R = √(4/3) | DC refractive index n_g(0) = √(1+α); τ₀ cancels at DC. | Needs **α only**. Inherits α's open antecedent. R = 1.1547005 verified. | **COMPUTED** | `closure_protocol.py:142,515-524`; registry `r_canonical_path_g` `:1194` |
| **E7** | R → Ω_Λ | Terminal velocity: drive (2−R) balanced by screened friction 1/(Sτ₀); Ω_Λ = (H_inf/H₀)². | **Tree:** (2−R)² = 0.71453 needs **R only** — τ₀ **and** S both cancel at cosmic baseline H₀ = 1/(Sτ₀) (verified). **Published 0.6886** is full-Friedmann **ANCHORED** — a *different number*. Conflation is the overclaim trap. | **COMPUTED** (tree) / DOTTED (published 0.6886) | `vacuum.py:22,45-47`; registry `h_inf_decomposition` `:1325`, `omega_lambda_prediction` (anchored) `:1346` |
| **E8** | HUB (via D) → μ_linear = 1 | The tracefree transverse P^TT projector annihilates the linear-scalar response ⇒ linear cosmology = ΛCDM. | **α-free, τ₀-free, structural** (∂^μP^TT = 0). Draws only on D's *derived* leg (tensor confinement), not its presupposed leg. Over-determined ~32σ by ISW. | **SOLID** | registry `adiabatic_dilatation_redundancy_nogo` `:5219` (`:5232`); `theory/PROJECTOR_CONSISTENCY_NOGO.md` §5 |
| **E9** | χ / single-mode → DM HOSTED + hierarchy magnitude FORBIDDEN | Single relaxational pole; a derived dark sector or a hierarchy-carrying β-function would each need a **new propagating vacuum pole** that locality + Q forbid. | **Single-mode is a binary channel-counting POSTULATE, not a theorem of Q.** The 12,800-pole scan covered only **relaxational** variables (cannot see an inertial DOF). The Q-pincer is theorem-modulo-gap (no in-repo Boulware–Deser). | **DOTTED** | registry `vacuum_spectrum_pole_classification` `:5340`, `propagating_relic_forbidden_pincer` (conjectural) `:5471`, `locality_no_halo_theorem` `:5532` |
| **E10** | HUB → QM(τ→0) + arrow(Ṡ≥0) | τ→0 limit = one first-order Euler–Schrödinger step (norm preserved); Ṡ = (1/τ₀)⟨(z−z_target)²⟩ ≥ 0. | Hub alone. No α; arrow needs only τ₀ > 0 (sign-only prefactor). **Scope flag:** decoherence/pointer basis recovered, **Born weights NOT** (open). | **SOLID** | registry `qm_recovery` `:753`, `arrow_of_time_from_entropy` `:1726` |
| **E11** | HUB → particle heads (Koide K=2/3, NH, N=3, SM) | The chain *reaches* the matter sector via the anomaly numerators that feed R and the Z₃ circulant mass operator. | **Reachability only.** HOSTED SM field content + ASSUMED Z₃ circulant (M₀, θ fitted); K=2/3 needs a=√2 (verified: at a=1, K=0.5). N=3 HOSTED. NH conditional on a_ν=1. Flavor mechanism OPEN. | **DOTTED** | registry `koide_z3_circulant_structure` `:2800`, `sm_emergence` `:789`, `neutrino_hierarchy_z3_nh_prediction` `:2918` |

### The one map-split, resolved (E1 / E2)

Two of the four independent audit maps tagged **Q → HUB** SOLID; two tagged it DOTTED. The
disagreement is a **scoping** question, not a disagreement about any fact. All four maps
agree on the underlying truth: single-pole-ness is not a theorem of Q alone
(`finite_memory_form_from_q`, `registry.py:5287` — the passive ⇒ positive-Debye converse is
false). The question is only *which edge owns that gap*.

**Final call: E1 is SOLID for the form-class it actually claims** (causal + passive), with
single-pole-ness explicitly handed to E2. Tagging E1 dotted double-counts the same gap that
E2 already owns. The discipline rule — *an edge's tag reflects whether what it claims
holds* — makes E1 solid. The single-pole gap lives on E2, where it is **COMPUTED** (not
dotted): the MZ premise and the anchored τ₀ are real, but they are *named, not hidden*.

---

## 5. The gap list — every DOTTED edge in priority order

These are the shore-up targets. Priority is by **downstream weight on the least-settled
premise**, not by depth in the chain.

### Priority 1 — the α antecedent (under E4, E6, E7)

- **Hidden assumption it needs:** the gravitational conformal mode IS the IR carrier of the
  vacuum susceptibility. The conditional a/c = 1/3 is proven; the antecedent is unproven.
- **Why it is first:** it is **both open and maximally fanned-out.** R = √(1+α),
  S = 12π/α², and Ω_Λ = (2−R)² all carry `deps=(alpha_vac_derivation)`; ±0.07 in α moves
  Ω_Λ by ~1 order. A single open antecedent silently propagates through the entire
  cosmological column.
- **Where to shore:** an in-repo Riegert/Paneitz 4th-order closure that establishes the
  IR-carrier identification. `registry.py:274` (open_negative).

### Priority 2 — E9, single-mode and the twin no-gos

- **Hidden assumption it needs:** that the responsive vacuum is **single-mode** (a binary
  channel count).
- **Why it is second:** it bears the **most downstream weight** (both the dark-matter
  verdict and the hierarchy-magnitude verdict hang on it) on a premise GRUT's own Spectrum
  Program lists as the **open central question** — not merely an import, but actively
  *undecided* (`registry.py:5340` frames it so). The 12,800-pole scan is blind to an
  inertial DOF; the Ostrogradsky leg of the pincer has one stated Boulware–Deser gap. **The
  deepest structural fact in this skeleton: the DM-hosting no-go and the
  hierarchy-forbidding no-go are the SAME no-go** — both forbid a new propagating vacuum
  pole.
- **Where to shore:** a Phase-II effective-action derivation that *decides* single- vs
  multi-mode, and an in-repo Boulware–Deser/Hamiltonian-constraint analysis of a general
  covariant higher-derivative TT completion.

### Priority 3 — E3, D → HUB

- **Hidden assumption it needs:** the L₀ → 0 Weinberg redundancy itself (imported, not
  re-derived from the CTP action) **+ GAP-1** (the scale-free in-in initial state, n_s = 1).
- **Why it is third:** it sits **directly on the hub** — closer to the spine than E9 or
  E11 — but unlike E9 its gap is a *clean, scoped import*, not an undecided question. That
  makes it tractable, which is why it ranks below the two heavier gaps but is still a
  priority.
- **Where to shore:** derive the redundancy from the CTP initial state, or axiomatize it
  explicitly and discharge GAP-1. `registry.py:5219` (`:5260`).

### Priority 4 — E11, particle heads

- **Hidden assumption it needs:** HOSTED SM field content + an ASSUMED Z₃ circulant with a
  **tuned amplitude**. Code-verified here: K = 2/3 is θ-independent **only at a = √2** (at
  a = 1, K = 0.5) — so the Z₃ structure *and* its amplitude are both assumed. N = 3 is
  HOSTED (it is fixed by matching the empirical K = 2/3, **not** by phase-independence; the
  earlier "unique at N=3" rationale was false-as-stated and has been corrected at
  `koide_operator.py`). NH is conditional on a_ν = 1.
- **Where to shore:** a flavor mechanism — what feature of S_CTP selects Z₃, M₀, θ, and
  a = √2. `registry.py:2800`, `:789`, `:2918`.

### Two confirmed code defects (spawned as background tasks — *not* foundation gaps)

These are codebase self-inconsistencies, distinct from the foundational gaps above.

- **R-source split.** `grut/derived/cosmology/vacuum.py:22` builds `H_INF` from
  `R_PRIMARY = R_REFRACTIVE = √(4/3)`, while `grut/foundation/anomaly.py`
  `h_inf_drive_over_friction` builds the drive from `(2 − R_ANOMALY) = 0.846` with
  `R_ANOMALY = 1.15428` (3-loop, verification-pending). The codebase disagrees with itself
  on **which R drives H_inf**. The registry (`h_inf_decomposition` deps=r_canonical_path_g)
  sides with √(4/3); the anomaly-module code does not.
- **Neutrino-NH tier mismatch.** `registry.py:2918` carries `tier="computed"` but its own
  notes (`~:2962`) say *"ANCHORED tier."* The field and the notes disagree.

---

## 6. The load-bearing verdict

**Is the SOLID proven core airtight? Yes — and it is small.** With **zero hidden
assumptions**, what survives as welded-by-derivation is the chain rooted in Q:

- **Q** itself (proven theorem of the formalism, scale-free).
- **E1** Q → HUB form-class (causal + passive).
- **E8** μ_linear = 1 (the P^TT projector no-go — α-free, τ₀-free, the framework's cleanest
  theorem; over-determined ~32σ by ISW).
- **E10** QM-recovery-as-limit + the arrow of time Ṡ ≥ 0 (needs only τ₀ > 0).

These four are welded. **Everything quantitative is COMPUTED, not solid.** R, S, and Ω_Λ
ride on the adopted α whose antecedent is open (E4, E6, E7). Everything in the
dark/spectrum/flavor sectors is DOTTED or a boundary terminal.

**The minimal genuine input set the whole core rests on:**

> **{Q, α} + the two anchors {τ₀, τ_micro}**

This matches the hierarchy ledger exactly. Q is the proven backbone; α is the single
load-bearing **open axiom**; τ₀ and τ_micro are the two anchored numbers — and their
*difference* is the hierarchy, not a third number. F's form and D's breaking are *derived
from these* (F via MZ given τ_micro ≪ τ₀; D's breaking given L₀ = cτ₀). D's underlying
redundancy and α's antecedent are the imported/open premises *on top of* this minimal set.

**The core is not zero-input, and it does not pretend to be.** Three edges are welded
(E1, E8, E10) plus Q; three are COMPUTED on the open α (E4/E6/E7) plus E2 on the anchored
τ₀; five are DOTTED at named seams (E3, E9, E11, plus the α-antecedent and single-mode gaps
that live under them). The single deepest fact this skeleton exposes is the **unity of the
two no-gos** (E9): dark-matter-hosting and hierarchy-forbidding are one no-go, and that one
edge bears the most downstream weight on the *least-settled* premise. **Shore α first
(widest fan-out), single-mode second (deepest structural unity), the D-redundancy third (on
the hub), flavor fourth.**

---

## 7. Sector-contract heads

The terminal nodes of the chain, each a stub ready for the next phase (organ #1/#7
expansion). Each is a legitimate place the chain *reaches*; none is a varnishable edge.

| Head | Status | Contract premise (what the sector must close) |
|------|--------|-----------------------------------------------|
| **Ω_Λ / H₀** cosmology | COMPUTED (tree) / ANCHORED (published) | Discharge the α antecedent; keep (2−R)² = 0.7145 vs full-Friedmann 0.6886 **distinct**; single-source R (fix the R-source defect). |
| **Dark matter** | BOUNDARY: HOSTED / no-halo FORBIDDEN | Decide single- vs multi-mode (Priority-2 gap). A legitimate terminal, not a gap to varnish. |
| **Hierarchy magnitude** | BOUNDARY: FORBIDDEN-by-theorem / existence forced | The *same* no-go as dark matter. Close the Boulware–Deser leg of the Q-pincer. |
| **Koide K = 2/3** | DERIVED-identity of an ASSUMED Z₃ (needs a = √2) | Derive the Z₃ structure **and** the amplitude a = √2 from S_CTP; mechanism open. |
| **N = 3 generations** | HOSTED (empirical 2/N match) | **Not** forced by phase-independence (corrected). Needs a genuine counting principle. |
| **Neutrino NH (Σm_ν ≈ 60 meV)** | OPEN [SPLIT], conditional on a_ν = 1 | A structural account of the K = 2/3 → 1/2 transition. Live falsifiers: JUNO/DUNE IH, DESI Σm_ν. Fix the tier mismatch defect. |
| **SM C1–C5** | HOSTED, necessary-not-sufficient | Uniqueness ("the SM falls out") is **not** established; field content is received. |

---

*Anti-salesmanship summary. The foundation is honestly jointed. Three edges are welded
(E1, E8, E10) plus the proven node Q; three are COMPUTED on the open α (and one on the
anchored τ₀); five are DOTTED at named seams. The skeleton's deepest exposed fact is the
unity of the two no-gos — dark-matter-hosting and hierarchy-forbidding are one no-go, both
forbidding a new propagating vacuum pole — and that edge bears the most downstream weight on
the least-settled premise (single-mode), which GRUT's own program lists as undecided. The
minimal genuine input set is {Q, α} + {τ₀, τ_micro}. A spine that quietly upgrades any of
the dotted edges to DERIVED is the one failure mode that sinks the whole thing; this
skeleton refuses that upgrade everywhere it is tempting.*
