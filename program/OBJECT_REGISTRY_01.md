# OBJECT REGISTRY 01 — TYPED INVENTORY

> **SCAFFOLDING ARTIFACT. NOT A RESULT.** No classification is asserted. No relationship between
> objects is claimed here. Fields the corpus does not specify read **NOT SPECIFIED** or
> **UNRESOLVED** — they are **not** filled from standard QFT knowledge.
>
> **Archival boundary: `d10e974`.** Q3 **OPEN**. Ledger delta **0**. Register 74 nodes,
> `beaeb84e8a6f8468`. No physics run. No new primitive. Nothing dispatched.

**Purpose.** Establish **what each object is** in the current GRUT record, before anyone draws arrows
between them. The failure this prevents: assigning dependencies between things that only resemble
one another in prose. Standard Mori–Zwanzig terminology must **not** be assumed to match GRUT's use.

**The categories are NOT peers.** A partition, a projection, a state, a gauge transformation and an
observable are different mathematical species.

| Category | Objects |
|---|---|
| **Physical partitioning** | A system/bath split · B slow-variable selection |
| **Mathematical reduction** | C projection `P` · D inner product |
| **State / scale data** | D state · E cutoff / separation scale |
| **Description redundancy** | F gauge / field-redefinition freedom |
| **Observable** | G response-object definition |

---

## A · SYSTEM/BATH PARTITION

- **Type (as recorded):** a partition of degrees of freedom. The canonical form is **not** a tensor
  split — *"type III₁ forbids it; what survives translation is a one-sided inclusion"*.
- **Status:** **priced input**, not a convention — `provenance/claims.json:22`, *"+3 declared inputs:
  system/bath split … **STANCE, not derivation**"*; `CHARTER.md:52` lists it under **assumed**,
  *"the system/bath split (the deepest)"*.
- **Provenance conflict (see §Sept-3 in the audit spec):** `GRUT_PROGRAM_FREEZE.md:49-51`
  (`7399765`, 2026-09-06 14:39) — *"the specific partition used by the contract was never declared in
  D1–D5"*; `GRUT_MODEL_FRAMEWORK.md:37` (`cc6c147`, 14:45) — the operative partition (external-leg vs
  internal-line) *"was historically **undeclared** — now declared here"*. **Not reconciled.**
- **Relation to C:** **NOT SETTLED BY THE RECORD.** `WALL_KR_U3_SPECIFICATION.md:72-81` carries two
  competing orderings (Zurek: split → coarse-graining; Mori–Zwanzig: choosing `P` *is* the partition)
  and states *"**None is selected.** This is the sharpest single result of the audit."*
- **Gauge / state / regulator dependence · domain/codomain · allowed transformations:** NOT SPECIFIED.
- **Unresolved specification:** which partition; and whether A and C are one decision.

## B · SLOW-VARIABLE / COARSE-GRAINING SELECTION

- **Type (as recorded):** a choice of which variables are retained as slow.
  `WALL_KR_U3_EFT_BASELINE_RESULT.json:18` — *"WHICH variables are retained as slow. **NOT generally
  free** — a different projection is a different effective theory, not a rescheme."*
- **Status:** **ASSUMED.** Same file `:26` — *"why these modes are the natural effective variables":
  "**ASSUMED** — the choice of slow variables is exactly the Mori-Zwanzig 'which P' question,
  unanswered here."*
- **Relation to C:** **UNDER-DETERMINED.** Established this phase: retaining the same variable does
  **not** determine the projected object (see D).
- **Domain/codomain · gauge/state/regulator dependence · allowed transformations:** NOT SPECIFIED.
- **Unresolved specification:** **no document declares a slow-variable set for this sector.**

## C · PROJECTION `P`

- **Type (as recorded):** `WALL_KR_U3_SPECIFICATION_RESULT.json` — *"a projection operator `P` defines
  relevant/irrelevant"*. **Whether it is a linear projection, a conditional expectation, or a
  restricted construction: NOT SPECIFIED in GRUT's own terms.**
- **Record's own note:** `WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json` — `"partition": "CHOSEN (P IS
  the partition)"`, `"unexplained": "what selects P"`.
- **Related but distinct registered object:** `p_tt_ansatz`, tier **assumed** — *"the projector P^TT
  **chosen (not derived)**"*.
- **Status:** unselected; *"what selects P"* recorded as unexplained.
- **Unresolved specification:** the map's type; what selects it; whether A, B and C are one decision.

## D · INNER PRODUCT / STATE SUPPLYING IT

- **Type (as recorded):** a bilinear structure plus the state that supplies it. Two constructions are
  named in the corpus: **Kubo–Mori (canonical)** and **symmetrised**.
- **The load-bearing record:** `calc/mz_inheritance.py:31-34` — *"rung3's phrase 'the Mori-Zwanzig
  kernel' **does not currently denote a unique object**, and the two objects it could denote **answer
  this question OPPOSITELY**."*
- **State dependence:** explicit. `RAI_GRUT_RESURRECTION.md:108-110` — producing the registered object
  *"requires `P` orthogonal w.r.t. a **state-induced Kubo–Mori inner product** — so producing GRUT's
  registered object **needs the state**."*
- **Status:** `:120` — *"the state supplying the inner product (**unpriced anywhere**)."*
- **Unresolved specification:** which inner product; which state; whether D is separable from C.

## E · CUTOFF / SEPARATION SCALE

- **Type (as recorded):** contested. `WALL_KR_U3_EFT_BASELINE_RESULT.json:11` — *"**NOT B (Wilsonian
  momentum-shell)**. The implemented split is the **external-leg vs internal-line** partition of a
  one-loop influence-functional calculation … Category H (hybrid): a diagrammatic partition described
  in scale/mode language."*
- **`:12`** — `"no_cutoff_parameter": true`; **`:13`** — *"dimensional continuation only; NO explicit
  IR scale"*; `WALL_KR_U3_EFT_BASELINE.md:28` — *"there is **no cutoff parameter whose placement could
  be varied**."*
- **Contradicted, unretracted:** `WALL_KR_U3_SCALE_SPLIT_CORRECTION.md:73-75` — *"an EFT program whose
  split is a **cutoff choice**."*
- **Meaning of "cutoff" in each statement:** NOT SPECIFIED by the corpus. **Not resolved here.**
- **Recorded consequence, if the split is not a scale split:** `WALL_KR_U3_EFT_BASELINE.md:31-34` —
  *"the O(H²) IR divergence … is what happens when there is **no actual scale split**."*

## F · GAUGE / FIELD-REDEFINITION FREEDOM

- **Type (as recorded):** a description transformation.
  `WALL_KR_U3_EFT_BASELINE_RESULT.json` — *"on-shell observables are invariant (equivalence theorem);
  **off-shell Green's functions are NOT**."*
- **Status:** the only one of the seven with a **stated invariance theorem attached**, and it is
  **scoped to on-shell observables only**.
- **Unresolved specification:** whether GRUT's response object is on-shell in the required sense.

## G · RESPONSE-OBJECT DEFINITION

- **Type (as recorded):** `CLASS_C_MANIFEST.json`, key `clock.declaration` — *"primary class-C object
  is the **two-time response** `G_R(x,x')`; **no global ρ(ω) presumed**; any one-clock spectral
  reduction **requires its own proof for the assembled object**."*
- **Designated observable:** `CLASS_C_WALL_CONTRACTS.md:18` — `rho_TT(w->0) = 2 Im G_R^TT(w)`,
  `eta = lim Im G_R^TT / w`.
- **Status:** the assembled object **does not exist**; its three-step extraction *"does not yet
  exist"*. `gauge` and `renormalization` are `UNDECIDED-DISPATCH`.
- **CRITICAL:** **G is the object being defined, not merely another choice.** It may not be treated as
  a scalar symbol until channel, background, state, retarded prescription and renormalization
  convention are fixed.

---

## THE THREE MINIMA — DEFINED, NONE ASSERTED

| | Requires |
|---|---|
| **I_formal** | enough to define a mathematical response / kernel |
| **I_physical** | enough to define a **gauge-consistent, state-specific** observable |
| **I_predictive** | enough to calculate an observable with **no unconstrained normalization or scale** |

**None of these is known.** `\|I_formal\| < \|I_physical\| < \|I_predictive\|` is a **possibility to
test**, not a claim. *"Minimum not presently demonstrable"* is a legitimate result.

---

## DEFERRED FIELD — populate only in the audit phase, NOT here

For each object: **"Can this object be varied independently while preserving the same declared
physical setup?"** — **left blank by design.** It separates *"this is mathematically a projection"*
from *"this projection constitutes a physically variable choice."*
