# S5-0 — GENERATOR ORIGIN: can the generator be derived rather than presupposed? (audit/formulation only)

**STATUS: §§0–4 PRE-REGISTERED** before any selector or generator class is evaluated. §5 (the audit)
and §6 (the outcome) will be added in a later commit.
- **Authority:** `SFG0_OWNER_RULING_01.md` §6 (Issue #2 comment `5903805047`).
- **No new numerical physics and no v4 exception.**
- **Date:** 2026-09-30 · **Branch:** `master-w25bu9`.

**Disclosure.** The auditor holds one prior expectation: the Level-0 program *declared*
ẋ = −Kx as its substrate premise, which would make selectors "earned" downstream of it circular.
The P-0 premise audit and the H-1 circularity check (§3) are written so that this expectation is
tested, not assumed.

## §0 Question (ruling §6.1)

For the already-earned substrate/structural data, does any existing GRUT principle select the
**form (kind) of the temporal generator**, or do multiple inequivalent generators remain compatible
with the same substrate data? Symbolically: substrate/static structure ⟹? generator class.

Magnitudes of derived constants are **out of scope.**

## §1 Comparison set and comparison object (frozen)

**Static datum shared by all classes.** A symmetric positive (semi)definite K on a declared site net,
together with its geometry. Two declared instances:
- **(R)** the CA-1 ring K(k) = 4 sin²(k/2);
- **(B)** the Level-0 bath block K_b (open chain, pin 0.3), also written K_N.

| Tag | Generator class | Where declared (to be verified in §5) |
|---|---|---|
| **G-D** | first-order dissipative, ẋ = −Kx (and the gradient ẋ = −∇V, 𝒞₂) | Level-0 / EA-0; CA-1 D (with noise) |
| **G-S** | Schrödinger-type, iψ̇ = Kψ | CA-1 M |
| **G-W** | conservative wave/phonon, q̈ = −Kq (Hamiltonian on T\*) | CA-1 P/T; O-6 𝒦_N |
| **G-OU** | stochastic, dx = −Kx dt + B dW | 𝒞₃; CA-1 D |
| **G-L** | dilation / lift realizations: Sz.-Nagy; quasi-free Lindblad loss; cotangent pᵀf | lift-selection records |
| **G-F** | fermionic hopping, i ċ = hc with h = K − 2 (CA-1 F) | CA-1 F / SF-1 |

- **Comparison object (common, time-structure-neutral as far as possible):** the pair (K, 𝒜). Here 𝒜
  is the generator as an operator-valued function of K on its declared state space, together with
  its **type**:
  - a real contraction semigroup;
  - a unitary group;
  - a symplectic/Hamiltonian flow;
  - a Markov semigroup;
  - a CP semigroup / dilation.
- **Invariants for "genuinely inequivalent":** the SF-0 §2 list, read on the retained response of a
  common declared observable:
  - the dispersion functional (for example −K vs −iK vs ±i√K);
  - I-z, I-gap, I-pc, I-c;
  - reversibility (time-reversal symmetric vs not);
  - norm or energy conservation vs contraction.
- **Representational equivalence ≃_G.** G-a ≃_G G-b iff an invertible map between the state spaces
  intertwines the two flows (on the same K) and maps the declared observables to each other. This
  follows `L0_LIFT_SELECTION_EVALUATION_01.md`: Koopman/KvN/Liouville are representational.
  - **Declared now:** a map that changes the K-functional counts as **a different class on the same
    K**. An example is G-W on K ≅ G-S on √K.

## §2 Selector inventory and admission (frozen)

**Admissible selectors** (ruling §6.3; record items only):

| # | Selector |
|---|---|
| S-loc | locality |
| S-pos | positivity/passivity/accretivity |
| S-gap | gap/memory |
| S-geo | geometry |
| S-acc | retained access |
| S-obs | observability |
| S-ord | strict Lyapunov / order (D-ORD / O-series) |
| S-cm | complete monotonicity, where earned |
| S-cone | influence-cone / noise-response |
| S-LG | Lorentz/gauge (**SUPPLIED**, per record status) |
| S-FDT | FDT/equilibrium, with its conditioning |
| S-var | earned variational/gradient formulation |
| S-symp | declared conservative/symplectic structure |
| S-SF | the SF-1/SFG-0 result |

**Candidate imports, listed and not consumed:** least action, maximum entropy, minimal complexity,
and similar.

**Grade of each selector, taken from the record** (quoted status):
- **EARNED**: an accepted finding or theorem, unconditional at its scope;
- **CONDITIONAL**;
- **SUPPLIED**;
- **CRITERION** (priced only).

Only EARNED selectors can *select*. The others are recorded as **prices.**

## §3 Mandatory checks (frozen)

- **P-0 premise audit.** For each generator class, establish from the record whether it entered as
  a **declared premise** (substrate definition, charter assumption) or as a **derived** result. Quote
  the entry point.
- **H-1 circularity.** A selector whose *statement presupposes* a time-evolution form cannot select
  that class over others. Examples: a Lyapunov/passivity property defined only for ẋ = −Kx, or an
  "earned" result obtained after assuming ẋ = −Kx. Such a selector is re-graded **CRITERION
  (definitional).** Each selector's H-1 status must be stated with a citation.
- **NG-1 no-go (ruling §6.6):**

  > If the same K-level substrate and geometry support dissipative, unitary/Schrödinger and
  > conservative/wave generators, then K + geometry alone cannot select the generator.

  - Accepted only at the scope demonstrated (CA-1 and related records). That scope must be stated:
    which K, which classes, and which geometry observables.
  - Then ask whether any **EARNED** (post-H-1) selector breaks the degeneracy.
  - A break by SUPPLIED Lorentz, gauge, statistics or lift assumptions is recorded as a **price**.
- **Primitive-price table (ruling §6.4; descriptive):** the extra structure each class needs beyond
  K and site locality, with record citations where the record states it.

## §4 Outcomes and determination rule (frozen; no ranking)

**Outcomes (ruling §6.5):**
- GENERATOR-SELECTED-IN-CLASS;
- GENERATOR-CONSTRAINED-NONUNIQUE;
- GENERATOR-IRREDUCIBLE/SUPPLIED;
- CLASS-SPLIT;
- REPRESENTATIONAL-ONLY;
- UNFORMULABLE.

This is a **determination procedure applied to the audit's findings.** It expresses no preference.
Take the first step that applies.

1. **UNFORMULABLE:** the §1 comparison object cannot be stated for the declared classes without
   importing the temporal structure under test. (The P-0/H-1 findings feed this.)
2. **REPRESENTATIONAL-ONLY:** every pair of classes in the comparison set is ≃_G on the same K.
3. Otherwise, take the post-H-1 **EARNED** selectors and, for each declared substrate instance
   (R, B, or any further declared substrate class), record which ≄_G classes each selector
   eliminates at identity/record grade.
   - **CLASS-SPLIT:** different substrate classes leave different unique survivors, under declared
     conditions.
   - **GENERATOR-SELECTED-IN-CLASS:** exactly one class survives, consistently.
   - **GENERATOR-CONSTRAINED-NONUNIQUE:** at least one class is eliminated, but several survive.
   - **GENERATOR-IRREDUCIBLE/SUPPLIED:** no class is eliminated by an EARNED selector. The only
     separations come from SUPPLIED, CONDITIONAL or CRITERION items, which are recorded as prices.

**Fences:**
- No S5-1 run, no SF-2 and no new parent.
- No gravity reopen, no Π₀ and no cosmology.
- Imports are not consumed.

## §5 Audit

*(Added in a later commit.)*

## §6 Outcome

*(Added in a later commit.)*
