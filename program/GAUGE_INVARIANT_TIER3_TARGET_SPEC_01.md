# GAUGE_INVARIANT_TIER3_TARGET_SPEC_01 — the (O, D, L, R) of the next target

**Status: TARGET SPECIFICATION, awaiting owner ratification. NO computation is
authorized by this document.** Written 2026-09-16 on the owner's instruction *"read A4
first, then write the charter."* Every claim about a frozen object below is either a
quotation (file named) or is tagged **[INFERENCE]** / **[HYPOTHESIS]** — this
document's, not the record's. The first draft of this document failed an independent
quotation audit (NOT_SOURCE_FAITHFUL: it called the graviton loop's working gauge
"underdefined" and its D4 check "never executed," quoting the pre-ruling charter as if
current, while three frozen D4 records and two owner rulings sat on disk). That draft
is superseded by this one; the audit and re-audit records are filed in the companion
`GAUGE_INVARIANT_TIER3_TARGET_SPEC_01.json` (written from both audit reports at commit). The Wall-A HARD STOP remains in force.

**IN LARGE LETTERS, per the owner:**

> **DO NOT CONSTRUCT A GAUGE-INVARIANT OBJECT WHOSE FINITENESS IS ASSUMED BY THE
> CONSTRUCTION. DETERMINE FINITENESS AS THE OUTPUT.**

"Ward repair" means only: *construct the correctly defined gauge-invariant
observable/response for the Tier-3 pure-gravity problem, then independently determine
whether its IR behavior is finite. The Ward identity is a diagnostic, not a desired
answer.*

## 0. The four Wall-A statements this target inherits (kept separate)

From `program/WALL_A_REDUCTION_01.md`:
1. Divergent leg weight — *"All of the IR-divergent weight of O_flat's TT-gauge BD legs
   restricted to any patch is the constant TT mode … EXACTLY a linearized
   diffeomorphism, L_ζ g for ζ^i = ε_ij x^j/2 … regular on r < 1/H"*: patch-locally gauge.
2. Power class — *"requires k_ext = 0 EXACTLY"*. **[INFERENCE]** at that slice-wide locus
   the gauge parameter ζ ∝ x is unbounded; the record speaks only of *"a gauge parameter
   bounded on the patch"* (`WALL_A_REDUCTION_01.json`).
3. Log class — *"does NOT require k_ext = 0 … locus-INDEPENDENT"*.
4. *"V₀ = 8ω⁴/15 ≠ 0 … loop-level with its gauge status undecided"*.

## 1. What the record says about gauge on the Tier-3 side — read from the sources

**(a) The working gauge was RULED.** `K_R_CONTRACT_OWNER_RULING.md` §3: *"D2 — working
gauge: OPTION 2a — gauge-UNFIXED, orbit-tracked … D4 therefore runs verbatim as frozen
(unfixed vs synchronous)."* §4: *"D3 — bath state + IR: OPTION 3a — BD-analogue Option-B
adiabatic … IR: dimensional continuation ONLY; NO explicit IR scale."* Countersigned
(`WALL_KR_TIER1_VERTEX_RESULT.json`: *"D1=1a, D2=2a, D3=3a (countersigned d5dc33b)"*).
The charter's earlier "UNDERDEFINED" list (`K_R_CONTRACT_EXECUTION_CHARTER.md` STEP 1,
self-described *"owner-resolved before Tier 1"*) **[INFERENCE from file dates and the
rulings' content]** is pre-ruling text, resolved by these rulings and — for its item
(iii) — by the D3(iii) ruling (§1b).

**(b) The internal-leg gauge scope was RULED, with its limits stated.**
`WALL_KR_D3III_OWNER_RULING.md`, seven clauses verbatim, including: *"1. The consequence
object may be treated as the registered TT-bath retarded TT response. 2. Gauge/orbit
robustness is required within that declared TT bath. 3. No claim is made that this
TT-bath prescription is the unique admissible general-gauge graviton propagator. 4. The
existence of alternative general-gauge/non-TT propagator content remains a separately
scoped theoretical question. 5. D3(iii) is therefore CLOSED FOR CURRENT CONSEQUENCE
SCOPE, NOT SOLVED AS A GENERAL GAUGE-UNIQUENESS THEOREM."* The internal legs are the
declared TT bath (`wall_kr_tier3_loop.py`: *"internal slots are TT bath: time rows
vanish"*; *"tensor rule <h h> = P^TT x W (frozen declaration)"*).

**(c) The D4 dual-gauge check WAS executed on the graviton loop, in three records
(2026-09-02).** `WALL_KR_D4_DUAL_GAUGE_AUDIT.md`: *"D4-C — INDETERMINATE AT THIS RUN'S
EXECUTABLE LEVEL"* — external orbit *"OPERATOR IDENTITY — PASSES at every H order
identically"*, internal-line sector *"UNDECIDED — the insertion is NONZERO at H⁰/H¹/H²"*
with the H⁰ obstruction *"(7/2) i ω² q (X0 ± X3)(t11 − t22)"*. `WALL_KR_D4_KTERM_COMPLETION.md`:
*"KTERM-A … The registered K-term mechanism — transversality + trace cancellation —
applied to the internal slot annihilates the full internal orbit direction exactly: for
arbitrary direction, arbitrary gauge parameter, and uniformly in H."*
`WALL_KR_D4_RE_ADJUDICATION.md`: *"D4-A — ALL REGISTERED D4 CONDITIONS SATISFIED for the
declared consequence-scope object"*, with the prior nonzero residual *"SUPERSEDED, NOT
DELETED"* (it inserted the gauge image *"as a free polarization on the internal slot"*,
not the declared *"P^TT × W"* contraction), and §8: *"It does not mean: general-gauge
uniqueness proved."*

**(d) The identity all three D4 records rest on, verbatim.** `WALL_KR_D4_DUAL_GAUGE_AUDIT.md`
Part 1: *"For arbitrary direction k, arbitrary ξ, and arbitrary trace coefficient
λ = 2(a′/a)ξ⁰: P^TT [ i(k_i ξ_j + k_j ξ_i) + λ δ_ij ] = 0 identically — gradients die by
transversality, the trace term by tracelessness."* And the re-adjudication's bridge (b):
*"On a fixed background at linear order, any such transformation acts on the spatial
block as δh_ij = i(k_iξ_j + k_jξ_i) + λδ_ij … including the particular ξ that reaches
synchronous gauge."* The audit states the identity *"covers the external probe legs,
G0^TT's linear invariance, and the corrected synchronous residual class in one stroke."*

**(e) The A-side residual family and its fixing, verbatim.** `WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md`
(superseding the v1 clause): *"The full residual family preserving synchronous gauge
(δg₀₀ = δg₀ᵢ = 0) is: ζ⁰ = C(x)/a(η) ; ζ_i = C_i(x) − (∂_i C) · Ia(η), Ia′(η) = 1/a(η)"*
and *"The fixing prescription is unchanged and still suffices: asymptotic coincidence
with the unfixed computation at η → −∞ kills the entire C-sector (both ζ⁰ = C/a and its
coupled −(∂_iC)·Ia piece; e.g. on the de Sitter chart a = −1/(Hη) both grow without
bound as η → −∞) and fixes the C_i."* **[INFERENCE]** the amendment exhibits a
growth mechanism for the C-sector and states *"and fixes the C_i"* without one; for a
time-independent C_i(x) this document reads the fixing as a coincidence condition
imposed by declaration rather than by a decay/growth argument.

**(f) The A4 orbit family on the matter side is plane-wave at the external K.**
`wall_a4_response_flat.py`: *"delta_e(X)_mu nu = i (K_mu X_nu + K_nu X_mu), K_mu =
(omega, 0, 0, -k)"*; the solver gate: *"consistent with Declaration 5's residual family
(zeta^0 = C(x)/a + static spatial maps) being zero-frequency only, hence empty at
omega != 0"*. The V2 amendment records every A4 physics conclusion as holding *"for
arbitrary ζ"*, and `WALL_A_A4_STAGE.md` fact 4: *"the spatial-TT projection of the orbit
direction vanishes for arbitrary (ζ, a′/a, k)."*

## 2. Gate A — orbit status of the boundary mode, answered on the record

The owner's Gate A: *can the existing orbit framework legitimately classify the ω = 0,
k_ext = 0 constant-TT leg?* Three source facts and one checkable inference decide it.

**Fact 1.** The constant mode is transverse and traceless in the position-space sense
(∂_i ε_ij = 0, ε_ii = 0). **[INFERENCE — with its sense specified]** The frozen
instrument's P^TT is the per-direction projector transverse to the internal momentum n̂
(`wall_kr_tier3_loop.py`: *"p2 = (nu1, +q n^hat), p3 = (nu2, -q n^hat)"*), whose action on a
constant ε_ij is n̂-dependent, not the identity; what the record establishes is that the
angular-averaged TT weight of the constant tensor is NONZERO — Wall-A computed the
isotropic factor *"<eps:P^TT(k^):eps>/(eps:eps) = 2/5"* (`WALL_A_REDUCTION_01.json`) and the
constant-mode two-point structure *"<P^TT> = (2/5)[(dd+dd)/2 - dd/3] (4/15, 1/5, -2/15
components computed)"* (`A34_CONTRACT_DIFFERENTIAL_01.json`, checker). So the P^TT × W
contraction retains the mode with weight 2/5 after angular averaging; it does not remove it.

**Fact 2.** The mode is a gauge direction: `WALL_A_REDUCTION_01` computed it as *"EXACTLY a
linearized diffeomorphism, L_ζ g for ζ^i = ε_ij x^j/2 (all components, computed)"* (`.json`:
*"L_zeta g = a^2 eps_ij dx^i dx^j … with a gauge parameter bounded on the patch"*) — i.e.
δh_ij = ε_ij = ∂_(i ζ_j) **[restated]**, patch-locally.

**Fact 3.** The D4 identity (§1d) annihilates orbit directions of the form
i(k_iξ_j + k_jξ_i) + λδ_ij *"for arbitrary direction k, arbitrary ξ"* — the plane-wave
form at a given k, with the gradient piece proportional to k. **[HYPOTHESIS — this
document's central one; checkable]** The constant mode is not of that form at any k:
its "gradient" ∂_(iζ_j) is k-independent (ζ linear in x), so *"gradients die by
transversality"* has no purchase on it — there is no k for transversality to kill. The
D4 identity is true as stated and does not reach this direction; the mode is
simultaneously TT (Fact 1) and pure gauge (Fact 2), which is exactly the case the
identity's mechanism excludes from its scope. The audit's *"covers … the corrected
synchronous residual class"* refers to the plane-wave residual family at ω ≠ 0
(*"zero-frequency only, hence empty at omega != 0"*, §1f); the k = 0 generator sits in
the zero-frequency set that family is empty on.

**Gate A answer: UNRESOLVED AT THE EXISTING ORBIT APPARATUS — precisely because the
apparatus's declared R retains the mode as bath content.** Under the ruled scope
(§1b), the mode is retained in the TT bath by Fact 1; the D4-A robustness certificate is
about orbit directions that leave the TT block (*"the orbit moves content only within the
discard space and never touches the TT block"*, `WALL_KR_D4_RE_ADJUDICATION.md` REQ (1))
and — **[INFERENCE, from Fact 3]** — is silent on a direction that lies within it. The alternative — quotienting the linear diffeomorphism, as the static
RW/Zerilli master variable does at free-leg level (Wall-A) — is *"alternative
general-gauge/non-TT propagator content"*, which the D3(iii) ruling places *"outside the
present consequence-scope contract."* **So Gate A's residue is one owner decision:
whether to extend the consequence-scope contract to a second equivalence relation R′
that quotients linear (large) diffeomorphisms on the internal legs — and if so, under
what boundary condition on the slice.** No computation can make that decision; it is a
scope ruling of the same kind as D3(iii).

## 3. The (O, D, L, R) of the target

- **O.** The retarded response of the Tier-3 pure-gravity problem (frozen Tier-1 hhh
  vertex; frozen Tier-2 massless BD legs) with the internal legs expressed in variables
  invariant under R′ (below) — the invariance built into the leg operator and the
  V₀ coupling, never imposed on the output. NOT the A3-4 matter object
  (`A34_CONTRACT_DIFFERENTIAL_01`: different diagram); NOT the D4-A consequence-scope
  object (which is the TT-bath object under R, already adjudicated); NOT K_R downstream
  of the obstructed dressing.
- **D.** D1 = 1a, D2 = 2a, D3 = 3a as ruled (§1a): controlled k → 0 with the isotropy
  gate (*"OPTION 1a"*); gauge-unfixed, orbit-tracked; BD-analogue Option-B adiabatic state
  with dimensional continuation and no IR scale (fork (ii) gated). Background as frozen
  in the Tier-2/Tier-3 instruments: the Section-D conformal chart a(u) = 1/(1−Hu),
  graded a² = 1+2Hu+3H²u² through O(H²) (`wall_kr_tier2_massless_bath.py` docstring). Any further assumption the R′-construction requires is a new
  declared input, priced.
- **L.** One of: (i) k_ext = 0 exactly; (ii) the D1-ruled controlled k → 0
  (*"OPTION 1a … Option 1b (literal k = 0) is rejected"*, `K_R_CONTRACT_OWNER_RULING.md`);
  (iii) a horizon-localized TT window of physical width R. Wall-A found these
  inequivalent for the power class, equivalent for the log class; the target declares
  one and reports the other two.
- **R vs R′ — THE DECISION.**
  - **R (ruled, in force):** the TT-bath prescription — internal legs = P^TT × W;
    gauge/orbit robustness required *within* it (D3(iii) clauses 1–2); general-gauge
    uniqueness NOT CLAIMED (clause 3). Under R the constant mode is retained (Fact 1).
  - **R′ (the proposal, owner's to grant or refuse):** R plus the quotient by
    time-independent spatial reparametrizations ζ_i(x) with ∂_(iζ_j) transverse-traceless
    — the family whose constant member is the Wall-A generator — **with a declared
    boundary condition on the slice** (decay at spatial infinity? asymptotic
    coincidence in the sense of Declaration 5's prescription — already in force at
    contract scope for the *synchronous* residual family (`K_R_CONTRACT_OWNER_RULING.md`
    §3: *"D4 therefore runs verbatim as frozen (unfixed vs synchronous)"*;
    `WALL_KR_D4_DUAL_GAUGE_AUDIT.md` §1: *"fixed by BD-asymptotic coincidence"*), but
    never stated for the TT-bath residual family, which the record does not name? none?). Patch-locally
    the constant member is gauge under any choice; on the slice-wide k_ext = 0 locus its
    status *is* the boundary condition. **[HYPOTHESIS]** this family is the residual
    freedom of the TT-bath prescription; no frozen source names it, and defining it
    by quotation is impossible because the record never wrote it down — which is itself
    the finding.
  - **Without R′ declared, O is ill-posed.** With R′ declared, O is defined and Gate B
    becomes a computation.

## 4. Gate B — coupling status (specified, NOT authorized)

Only under a declared R′: rebuild the internal-leg Wightman functions in R′-invariant
variables (the static-chart instance is the RW/Zerilli master variable, blind to the
constant mode at free-leg level per Wall-A; the flat-slicing analogue must be
*constructed* — **[proposal]**), recompute the O(H²) small-q class in both CTP
combinations with the frozen T3-1 criterion (Laurent exponent of the angular-averaged
radial integrand), and read the class. Whether V₀ = 8ω⁴/15 ≠ 0 survives the quotient is
the output. The DomainRejected fence and the fork's pricing text are outputs, never
inputs. A new instrument, its own freeze, its own controls: a broken-R′ plant must be
detected; a transverse-by-fiat plant must be detected; the D4-A machinery's five
negative controls are the template.

## 5. Pre-registered outcomes (the owner's six)

- **FINITE_PHYSICAL_RESPONSE** — R′-invariant O(H²) object IR-finite in both
  combinations; the fork's divergence was carried entirely by the quotiented sector.
- **DIVERGENT_PHYSICAL_RESPONSE** — still diverges (class, combination stated); the IR
  problem is physical under R′.
- **RESIDUAL_GAUGE_OR_BOUNDARY_AMBIGUITY** — finiteness depends on R′'s boundary
  condition; exhibited as a function of the choice.
- **OBJECT_NOT_WELL_DEFINED_UNDER_R′** — no R′-invariant leg variable exists on the
  declared background (obstruction named).
- **APPARATUS_CANNOT_CLASSIFY** — Gate A's answer for the existing apparatus; would
  recur if the constructed variables cannot represent the mode.
- **UNEXPECTED_STRUCTURE** — **[this document's count]** Wall-A's outcome was MIXED
  (none of its four pre-registered outcomes) and its ROUTE-B mechanism was refuted;
  the taxonomy has been wrong before.

**Success ceiling:** *"under R′ = ⟨declared⟩ with boundary condition ⟨stated⟩, the
Tier-3 O(H²) response in R′-invariant variables is [finite/divergent] in [combinations]."*
**Standing negative results:** (i) the patch-local gauge identification (Wall-A) is NOT
evidence the R′-invariant loop is finite; (ii) D4-A's certificate under R is NOT evidence
about R′ — it is silent on the direction by construction (§2); (iii) a finite result
under one boundary condition is NOT evidence about another.

## 6. Anti-optimization

FINITE is the framework-favorable trap. DIVERGENT is deflation-comfortable. AMBIGUITY is
deference-comfortable. **Choosing R′'s boundary condition so that it comes out finite is
the forbidden move in its purest form** — which is why R′ is declared by the owner,
on the record, before Gate B runs, and never revised after the class is seen. The
D3(iii) ruling's own wording discipline (*"the record never asserts general-gauge
uniqueness in any phrasing"*) is the template: this target may never assert that R′ is
*the* correct equivalence, only that it is *the declared one*.

## 7. Fences (all standing; none relaxed here)

Wall-A HARD STOP; the D4-A and D3(iii) rulings untouched (R′ extends, it does not
overturn); no K_R build; no s ≥ 2 reinterpretation; the A3-4 ±i0 defect flagged/inert;
fork (ii) gated; rung3's tier untouched; nothing banked; frozen artifacts read-only.

---

*Sources quoted: PHYSICS_LEDGER/{K_R_CONTRACT_OWNER_RULING.md, WALL_KR_TIER1_VERTEX_RESULT.json,
WALL_KR_D3III_OWNER_RULING.md, WALL_KR_D4_DUAL_GAUGE_AUDIT.md, WALL_KR_D4_KTERM_COMPLETION.md,
WALL_KR_D4_RE_ADJUDICATION.md, wall_kr_tier3_loop.py, WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md,
wall_a4_response_flat.py, WALL_A_A4_STAGE.md, K_R_CONTRACT_EXECUTION_CHARTER.md};
program/{WALL_A_REDUCTION_01.md, WALL_A_REDUCTION_01.json, A34_CONTRACT_DIFFERENTIAL_01.md}.
Quotation-audited against the files by two independent read-only passes before commit
(first draft: NOT_SOURCE_FAITHFUL, superseded; this draft: SOURCE_FAITHFUL_WITH_CORRECTIONS,
all six corrections applied); both reports preserved in the companion .json. Awaiting the owner's R′ decision and ratification.*
