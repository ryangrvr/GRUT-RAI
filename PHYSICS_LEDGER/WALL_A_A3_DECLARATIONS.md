# WALL A, STAGE A3 — DECLARATIONS (FROZEN 2026-08-25, CHECKER-AMENDED)

**Date:** drafted 2026-08-24 (Ox), reviewed and amended 2026-08-25 (checker) ·
**Standing state:** `372d02d` (A1 countersigned `92adbe3`) ·
**Status:** **FROZEN** per the owner-mandated two-step protocol: the checker's review
found SEVEN findings (F1–F7, each patched in place above, marked CHECKER-AMENDED/-ADDED/
-CORRECTED) before hashing. The freeze hashes live in AGENT_COORDINATION.md and the
freeze commit — a hash cannot live inside the file it hashes. This document is now
IMMUTABLE: any change requires a superseding v2 that cites this one; results later cite
this document; it never cites results.
**W-0:** declarations are commitments about method, not physics results. Nothing here is
banked; nothing here computes a loop quantity.

**Why A3 exists:** this is the final place the program can make an advance choice without
seeing a loop result. Every choice below is explicit, with alternatives named and
selection criteria stated. A choice made silently inside the loop assembly would
contaminate the blind on wall questions (i)/(ii)/(iii).

---

## DECLARATION 1 — RENORMALISATION SCHEME

### The mandated split

Every assembled quantity is decomposed, in the assembly code itself, as:

```
Π_ren = Π_local^scheme + Π_nonlocal^invariant
```

- **Π_local^scheme**: local terms — **CHECKER-AMENDED PREDICATE (F1):** polynomial in
  **(ω², k²)** — the derivative structure, which is what locality means — with
  coefficients arbitrary FINITE functions of (m², H², μ), where **μ is the
  regularisation scale the draft omitted**. The draft's predicate ("polynomial in
  (ω², k², m², H²)") would have misclassified legitimate local counterterms whose
  coefficients carry log(m²/μ²) or log(H²/μ²) — standard in dimensional regularisation —
  as nonlocal, either breaking renormalisation or inviting an ad-hoc reinterpretation
  mid-assembly: exactly the hidden fork A3 exists to prevent. Analytic at ω = 0 and
  k = 0 by construction; the hostile cases (ω²·log k², ω⁴/k²) remain nonlocal under the
  corrected predicate.
- **Π_nonlocal^invariant**: the finite nonlocal response — branch-cut structure, memory,
  the low-frequency analytic behaviour. **This is where wall question (iii) lives.**

The split is auditable **in the assembly code**: each subtraction term must be
individually expressible in the corrected local form (checked term-by-term: polynomial
in (ω², k²), coefficients finite functions of (m², H², μ)); anything not so expressible
is nonlocal by declaration and may not be subtracted.

### The scheme

**Primary scheme: de Sitter-invariant dimensional regularisation** — the one-loop
integrals are analytically continued to d = 4 − ε spacetime dimensions, preserving
de Sitter invariance of the regularised two-point functions; divergences appear as
poles in ε and are subtracted by the counterterm basis of DECLARATION 1b below.

**Genuine alternative named now:** Pauli–Villars regularization with two regulator
fields of mass M₁, M₂ taken to infinity after the loop. The robustness test (below)
is run against this alternative at the assembly stage.

**Selection criterion for the primary scheme** (stated before any result): preservation
of de Sitter isometry invariance of the regulated correlators, and auditability of the
local/nonlocal split. **CHECKER-ADDED (F7):** the scheme's symmetry property may NOT be
cited as evidence in the wall-question (i) placement verdict — placement is read off the
computed nonlocal decomposition only. A symmetric regulator avoids *introducing* spurious
breaking; it is not itself a demonstration that the response lies in the covariant
subspace, and using it as one would partially impose exactly what the booked +1's
discharge condition requires the calculation to demonstrate unimposed. **The critical principle, owner's words, binding:**

> No finite local counterterm may be selected because it produces a preferred spectral
> or memory behavior.

**CHECKER-AMENDED (F2):** the draft selected finite counterterms by "(a) absorbing the
ε-poles, and (b) the renormalisation conditions declared in 1b" — but 1b declares only
the OPERATOR BASIS, no conditions. The finite parts of the six coefficients are exactly
where a hidden choice could sit. The conditions are therefore declared now:

**Renormalisation condition: MINIMAL SUBTRACTION** — pole terms only are subtracted;
finite parts of all six basis coefficients are left exactly as the loop produces them;
μ is kept symbolic and its dependence recorded as part of Π_local^scheme's data. This
is the unique condition with ZERO finite-part discretion — the conservative completion
of the critical principle above. Any deviation from pole-only subtraction at the
assembly stage is a FINDING, not a choice. (Checker-added declaration, disclosed as
such: the owner may order a v2 of this document before assembly begins if different
conditions are wanted; after freeze, changes require a superseding v2, never an edit.)

Any counterterm choice whose justification references spectral density, memory behavior,
or convergence class is PROHIBITED and would invalidate the blind.

### DECLARATION 1b — the counterterm basis (frozen)

The local counterterm basis is frozen to the diffeomorphism-invariant local operators of
the declared action: cosmological constant Λ, Newton's constant G (i.e. the EH term),
R², R_{μν}², R_{μνρσ}², and □R. **No other operator may enter.** Each divergent local
term in the loop must map onto this basis; a divergent term that does not fit the basis
is a FINDING to be reported, not absorbed.

### Wall-question sensitivity map (declared in advance)

| wall question | sensitive to Π_local^scheme? | sensitive to Π_nonlocal^invariant? |
|---|---|---|
| (i) 3D Lorentz placement | Only in the audit sense: local counterterms contribute ONLY structures generated by the frozen basis (recorded per-term); they may not be used to claim or deny placement. The placement verdict is decided by the NONLOCAL part. | **YES — primary.** The tensor decomposition of the nonlocal integrand onto {P², P⁰ˢ, X_sw, residue} decides (i). |
| (ii) 2D closure / equilibrium | NO — scheme-independent. (ii) is decided by the state/KMS status (DECLARATION 2) and the reciprocity diagnostic, not by subtractions. | Indirectly: the reciprocity diagnostic runs on the computed kernel; subtractions do not alter its verdict. |
| (iii) IR analytic structure / convergence class | NO for the class: local terms are polynomials in ω — analytic at ω = 0 — and cannot change the nonlocal low-frequency analytic class (branch cut vs analytic, s-class). The split must be auditable so this claim is CHECKED, not assumed. | **YES — entirely.** The convergence-boundary diagnostic reads only the nonlocal part. |

### Robustness test (declared now, executed at assembly)

Because two admissible schemes can differ only by local polynomial terms, the assembly
stage MUST additionally run the primary scheme against the Pauli–Villars alternative and
require: **the nonlocal low-frequency analytic structure (branch-cut location, s-class at
the convergence boundary) agrees.** Disagreement in the nonlocal part is a FINDING
(scheme-sensitivity of question (iii)), reported as such — never averaged away.

---

## DECLARATION 2 — BATH-STATE STATUS

### The distinction that must not collapse

```
STATE SPECIFICATION   ≠   KMS / detailed-balance OF THE INTERACTING RESPONSE
```

Specifying Bunch–Davies fixes the FREE field theory's two-point functions. It does NOT,
by itself, establish that the INTERACTING response kernel satisfies KMS or detailed
balance — and after the closure-premise result, equilibrium/KMS is precisely what licenses
3 → 2 while genuine non-equilibrium honestly leaves the family 3D. **A3 therefore does
not pre-answer wall question (ii).**

### What BD fixes

- **Kinematically:** the mode functions of the free bath scalar on the declared chart
  (positive frequency w.r.t. the BD vacuum in the far past η → −∞); the ultraviolet
  behaviour of the bath two-point functions; the iε/Feynman prescription of the loop.
- **Spectrally (free level):** the Wightman functions entering the loop integrand are
  BD-determined. This is an input to Σ_R^TT's construction — declared, auditable.

### What BD does NOT fix (fenced as the assembly-stage question)

- **The KMS / detailed-balance status of the interacting response.** The horizon
  thermality claim ("the BD vacuum restricted to the static patch is thermal at
  T = H/2π for comoving observers") is **CLAIMED-NOT-COMPUTED** for the interacting
  kernel. Whether the computed Σ_R^TT satisfies a KMS/detailed-balance relation —
  which is what would license the 3 → 2 reduction per the closure-premise result —
  is a loop-stage COMPUTATION (the reciprocity diagnostic of the closure test, run on
  the actual kernel). It is fenced here as wall question (ii)'s content.
- **The equilibrium regime itself.** de Sitter with the BD state is not thermal in the
  naive global sense; whether the response behaves as an equilibrium medium is question
  (ii), not an input.

### Alternative states (named now, with declared consequences)

| alternative | what would change |
|---|---|
| generic α-vacuum (α₁, α₂) | Alters the bath Wightman functions at short and long distances; known unitarity/analyticity pathologies at the free level; would change the loop's spectral weight and potentially the convergence class (iii). Declared OUT unless a FINDING forces revisiting. |
| excited/squeezed initial state (occupation n_k ≠ 0) | Moves the state genuinely out of equilibrium: the closure test then predicts the family stays 3D — i.e. this alternative would change question (ii)'s expected answer. Declared as the sensitivity probe if (ii) is answered "non-equilibrium". |
| thermal (static-patch) initial state | Would ASSUME the equilibrium that question (ii) must compute. PROHIBITED as an input for the primary run; permitted only as a cross-check AFTER (ii) is answered. |

---

## DECLARATION 3 — G0 SPECTRAL WIRING (enforced by code, not prose)

### The forbidden direction

```
registered J(ω)  →  Σ_R^TT construction          FORBIDDEN
```

### The frozen direction

```
BD mode functions + declared interactions  →  loop  →  Σ_R^TT / K_R / Im χ
       →  compare AFTERWARD with the registered J(ω)
```

The registered spectrum is the **BENCHMARK UNDER TEST**, not an ingredient.

### Enforcement mechanism (executable, inherited by the assembly instrument)

The machine registry (`WALL_A_A3_REGISTRY.json`) carries the **barred-inputs list as
data**. The assembly instrument is REQUIRED to:

1. **LOAD** the registry at start and **ECHO** it verbatim into its output (a silent
   deviation becomes a diff, not a memory);
2. **SCAN** its own imports, file reads, and symbol table against the barred list
   (module names, file names, symbol names) before any loop quantity is computed —
   **CHECKER-HARDENED (F5): the import scan is TRANSITIVE (`sys.modules` at scan time,
   not the import statements)**, so a barred module reached through an intermediate
   import still fails the run;
3. **FAIL** (non-zero exit) if any barred item is matched — the run is void, not warned;
4. Keep the comparison-to-J(ω) step in a **separate post-assembly artifact** that reads
   both the computed Σ_R and the registered J(ω) — the construction code physically
   cannot reach the registered objects because the scan runs first and the comparison
   code is not linked into it;
5. **CHECKER-ADDED (F5) — content-hash barring:** each barred FILE entry carries the
   sha256 of its current content in the registry; the scan hashes every file the
   instrument reads and fails on a hash match — a renamed copy of a barred file is
   caught by content, not name;
6. **CHECKER-ADDED (F5) — numeric-fingerprint audit:** the assembly source may not
   contain numeric literals characterising the registered family's spectral shape (the
   register's s = 3 exponent, the fitted (ε, τ₂) values); every numeric constant in the
   assembly must cite a registry entry or be a mathematical constant. The source is
   grep-audited against the fingerprint list in the registry; matches are FINDINGS
   requiring justification on the artifact face. (This closes the "copied constant"
   leak the symbol scan cannot see — the draft itself flagged its enumeration as best
   effort; this is the audit it asked for.)

**CHECKER-ADDED (F5) — barred list extended:** the review found `wall_a_g1_ohmic_plant.py`
— which carries the registered Ohmic J(ω) explicitly — absent from the barred files, along
with `kk_dos_signchange_probe.py`, the G1/rung7/priority result JSONs, and
`MICROSCOPIC_TARGET_BENCHMARK.md` (the Q3 comparator: it belongs to the post-assembly
comparison artifact, and construction-stage code reading the benchmark would un-blind Q3).
All added to the registry's barred list.

The registered J(ω) family remains BARRED as an input to Σ_R^TT. It is the thing being
tested against.


---

## DECLARATION 4 — THE BLIND, RESTATED OPERATIONALLY

The assembly stage will compute exactly the following quantities. The inside/outside
criteria are written NOW, before the integral is touched. **Nothing is evaluated here.**

| id | quantity the assembly computes | INSIDE criterion | OUTSIDE criterion |
|---|---|---|---|
| Q1 | Tensor decomposition of the loop integrand's nonlocal part onto the countersigned channel basis {P², P⁰ˢ, X_sw, residue} | Every nonlocal coefficient function multiplies ONLY structures in {P², P⁰ˢ, X_sw}; residue = 0 or a recorded FINDING | Any nonlocal coefficient multiplying a structure OUTSIDE the 3D family (P1, P0w, Xws, or a genuinely new structure) — including coefficient functions that vanish only on-shell |
| Q2 | a(η)-weighted time integrals acting on the a² and a⁴ vertex channels | Bookkeeping only: convergence status of each channel declared per-channel; no placement verdict | An ill-defined channel (non-convergent after the declared regularisation) — reported as FINDING, not regularised ad hoc |
| Q3 | Convergence-boundary diagnostic: Re χ(0) = (2/π) ∫ Im χ(ω′)/ω′ dω′; spectral class s | s ≥ 2: convergent (the registered benchmark's class) | s ≤ 1: divergent — reported as found; BLIND to which outcome favours the register |
| Q4 | Reciprocity / detailed-balance diagnostic on the COMPUTED kernel (the closure test's mechanism, run on Σ_R^TT) | Holds ⇒ the equilibrium regime is established ⇒ the 2D closure reduction is licensed for the computed response | Fails ⇒ the response family stays honestly 3D for this state; question (ii) answered NEGATIVE |

**CHECKER-ADDED PRE-REGISTRATIONS (F4, F6) — added before freeze per target 4's own rule:**

| id | quantity | INSIDE criterion | OUTSIDE criterion |
|---|---|---|---|
| Q5 | **Flat-limit reduction** of Π_nonlocal: the H → 0 limit, per channel | The limit exists per-channel and its decomposition onto the FLAT 3D family {P², P⁰ˢ, X_sw} matches Q1's placement | The limit fails to exist / does not commute with the decomposition (IR obstruction) — a FINDING; the booked +1 is then UNDISCHARGEABLE via this route |

- **Q1b (sub-record, mandatory if Q1's X_sw coefficient ≠ 0):** record the coefficient's
  (ω-parity, H-parity) decomposition and its H → 0 behaviour — the closure test's
  interpretive frame (an X_sw piece odd in H and vanishing at H → 0 is
  flat-limit-compatible; one surviving H → 0 is a flat placement failure).
- **Q3 gap closed:** 1 < s < 2 is INTERMEDIATE — neither criterion covers it; reported
  as its own finding, never rounded to either side.
- **Q4 predicate pinned:** the reciprocity diagnostic is the PROPER Onsager–Casimir test
  of the countersigned closure instrument (ε-signature-corrected slot exchange; H treated
  as T-ODD) — NOT the naive slot-symmetry test, which the closure review exhibited
  killing a legitimate Hall term. The implementation must cite
  `wall_a_closure_premises.py` / `second_author_closure_premises.py`.
- **THE +1 DISCHARGE MAP (pre-registered so no post-hoc interpretation is possible):**
  the booked `response_lorentz_covariance` +1 is dischargeable ONLY by Q1 INSIDE **and**
  Q5 INSIDE, per the owner's discharge condition ("…lies in that 3-dimensional
  Lorentz-covariant subspace without imposing it as an input"). Q3 and Q4 do NOT vote on
  the +1 — they answer questions (iii) and (ii) respectively. Any discharge claim citing
  other evidence is invalid. (Discharge itself remains an owner ruling at the bank gate;
  this map only fixes what evidence could support one.)

Additional blind rules:
- Local counterterm contributions are listed per-term against the frozen basis and are
  EXCLUDED from all placement verdicts (they cannot vote on (i) or (iii)).
- The comparison with the registered J(ω) happens ONLY in the separate post-assembly
  artifact, after Q1–Q5 verdicts are recorded.
- Any anomaly is diagnosed before being reported; defects (including self-caught) are
  disclosed on the artifact face.

---

## DECLARATION 5 — A4 DUAL-GAUGE PROTOCOL (frozen now)

**Slot:** after A3 (this document, once frozen), BEFORE Σ_R^TT assembly. The second
gauge does not make its first appearance at the loop, and the comparison protocol cannot
be redesigned after seeing a first-gauge answer.

**Second gauge: synchronous gauge** — **CHECKER-CORRECTED (F3), two defects in the
draft's specification:**

1. The draft's residual-fixing condition ∂₀(h₀ᵢ/a²) = 0 conditions a component that
   synchronous gauge sets IDENTICALLY TO ZERO (synchronous means δg₀₀ = δg₀ᵢ = 0) — it
   was vacuous and fixed nothing. Corrected: the genuine residual freedom of synchronous
   gauge is ξ⁰ = C(x)/a(η) plus time-independent spatial reparametrisations
   ξⁱ = ξⁱ(x); it is fixed by the declared prescription that the synchronous coordinates
   coincide with the unfixed-computation coordinates asymptotically as η → −∞ (the BD
   asymptotic region), which removes both C(x) and the spatial freedom.
2. The draft called the first computation "the covariant/de Donder-type gauge of
   A1/A2" — A1 fixed NO gauge: the countersigned vertex is the full untruncated h_μν
   with all non-TT content tracked and orbit-reconciled. The A4 comparison is therefore
   **gauge-UNFIXED (full h, orbit-tracked) vs synchronous**, which is the stronger test:
   the second computation imposes a genuine gauge slice and must reproduce the
   gauge-invariant content of the computation that imposed none.

**Quantities compared (gauge-invariant content only):**
1. Γ^TT-level objects: the TT-projected vertex and the recorded discard bookkeeping
   (trace + longitudinal), reconciled against the gauge orbit — the orbit structure is
   gauge-independent by the countersigned Bardeen machinery, so the discards must map
   orbit-to-orbit.
2. Π_nonlocal^invariant: the nonlocal part of the assembled self-energy — REQUIRED to
   match exactly (symbolic equality after the gauge transformation to the second gauge).
3. The Q1 placement verdict and the Q3 convergence class: REQUIRED to match (both are
   declared gauge-invariant content).

**Match criterion:** exact symbolic equality for (1) after transformation, and for (2);
identical verdict strings for (3). The LOCAL scheme parts are recorded in both gauges but
are NOT required equal term-by-term — they are required to differ only by the declared
gauge transformation of the counterterm basis (checked against the frozen basis list).

**Failure handling:** any mismatch in (1)–(3) is a FINDING that blocks Σ_R^TT assembly —
it means one of the two computations (or the transformation) is wrong, and the
discrepancy must be resolved before the wall question is answered.

---

## SECOND-AUTHOR TARGETS (load-bearing first — this list is what the checker's review executes)

1. **The local/nonlocal split's auditability** (D1): a hostile reviewer attacks by
   exhibiting a subtraction that is NOT a local polynomial yet would pass a naive check
   — e.g. a term polynomial in ω but non-analytic in ω²/k² at k = 0. The declaration's
   defence: the split is checked term-by-term in the assembly code against the frozen
   basis; the reviewer should demand the check's exact predicate.
2. **The BD ≠ equilibrium fence** (D2): attack by showing some clause lets "BD" stand in
   for "KMS response". The defence: the fence is structural (state declaration names no
   KMS property) AND the Q4 diagnostic computes (ii) rather than assuming it. Reviewer
   should verify no other declaration references BD-thermality as an input.
3. **The barred-inputs guard's executability** (D3): attack by exhibiting a leak path —
   an indirect import, a renamed symbol, a numeric constant copied from J(ω) rather than
   the object. The defence: the scan runs on imports, file reads, AND symbol names; the
   reviewer should demand the scan's implementation and try to defeat it.
4. **The blind criteria's completeness** (D4): attack by naming a quantity the assembly
   will compute that has no pre-registered inside/outside criterion (e.g. the X_sw
   coefficient's ω-dependence class). If one exists, it must be added BEFORE freeze.
5. **The A4 protocol's freeze completeness** (D5): attack by showing a gauge-dependent
   quantity that the protocol fails to classify as local^scheme (and hence not required
   to match). The frozen counterterm-basis list is the defence.
6. **The prohibition's teeth** (D1 critical principle): attack by proposing a finite
   counterterm whose justification is phrased neutrally but whose effect is a preferred
   memory behavior. The defence: selection criteria reference only pole-absorption and
   the declared renormalisation conditions; the reviewer should audit every criterion
   sentence for spectral language.

