# OWNER DECISION PACKET AFTER 4cb5d23

**Date:** 2026-09-02 · **Instrument:** `wall_kr_owner_decision_packet.py` ·
**Artifact:** `WALL_KR_OWNER_DECISION_PACKET_RESULT.json` ·
**State:** commit `4cb5d23`, branch `v4`, D4-A accepted, worktree clean.
**Owner disposition (recorded append-only):** the packet at `c5948f6` is **ACCEPTED as a
neutral decision packet**, with A–F remaining unselected. Acceptance carries one binding
scoping instruction, applied in Decision D below. The three textual/provenance questions
stay open and do not block acceptance.
**No physics run authorized. No decision in this packet is made by the agent.**
W-0: unbanked.

---

## 1. OWNER DECISION SUMMARY

Six decisions are open. **None is selected here.** Each is presented with its
verified evidence and its option set.

| | decision | option set | agent selection |
|---|---|---|---|
| **A** | IR input (fork-(ii)) | A1 / A2 / A3 | **NONE** |
| **B** | Epoch window | B1 / B2 / B3 | **NONE** |
| **C** | Low-frequency domain | amendment prerequisites stated | **NONE** |
| **D** | Certificate / manifest face | comparison only | **NONE** — no face declared authoritative |
| **E** | Hash-pin drift | E1 / E2 / E3 | **NONE** |
| **F** | Three held flags | F1 / F2 / F3 | **NONE** |

---

## 2. VERIFIED EVIDENCE FOR EACH DECISION

### DECISION A — IR INPUT

Verified:

- Fork-(ii) is **mathematically possible** — nine candidate prescriptions are each
  capable of regulating the log.
- It is **not register-authorized**. Standing ruling **IR-B**; the authority sweep
  returned zero licensing entries.
- The manifest's `regulator_policy` requires every regulator be appended *"with
  purpose/location/limit/order BEFORE use"*, and states that *"solvers refusing
  undeclared regulators is correct behaviour."*
- Adoption would therefore constitute a **new register input**.

"Mathematically possible" and "authorized under the register" are **different
propositions**, and they currently carry **opposite truth values**.

**Owner choices — none selected:**

- **A1.** Leave IR fork-(ii) uninvoked.
- **A2.** Authorize a named/priced IR prescription through a new versioned register entry.
- **A3.** Reject fork-(ii) for the consequence campaign.

*If A2: the prescription must be appended to the manifest before use, and classified
as regulating-only (parameter count may be unchanged) versus introducing a physical IR
scale (a new counted input). That classification is itself part of the ruling.*

### DECISION B — EPOCH WINDOW (independent of A)

Verified:

- Separately registered and separately priced at **W\* < 0.25 e-folds**.
- **Not** licensed by any consideration of fork-(ii). No registered source binds the two.
- **Named** window: outcome 1 is reclassified to **outcome 5**.
- **Unnamed** window: fires manifest **prohibition 5**, *"unstated epoch/window parameters"*
  (verified to be the actual prohibition #5, not a nickname).
- A windowed calculation **cannot report outcome 2 at all**.

**Owner choices — none selected:**

- **B1.** Do not invoke the window.
- **B2.** Authorize a specifically named/priced window under its pre-registered consequences.
- **B3.** Reject windowing for the consequence campaign.

*B is not collapsed into A. They are two inputs requiring two declarations.*

### DECISION C — LOW-FREQUENCY DOMAIN

Verified structural conflict:

| element | value |
|---|---|
| criterion requires | assembled, gauge-invariant, **IR-resummed** `G_R^TT` continued toward ω → 0 |
| criterion also requires | exponent α extractable **with an error budget**, else outcome 4 |
| Tier-4 evaluator refuses | ω ≤ √(104/9)·H ≈ **3.3993 H** (DomainRejected; refusal is a tested control) |
| epoch-window resolution floor | Δω ≈ 1/W\* ≈ **4 H** |
| `allowed_reductions` | *"only reductions proved stationary within their own declared scope; none presumed"* |

**Current disposition: 4.** Disposition 3 is the only exit currently identified.

The overlap is **not** presented as a physics result. Nothing was extrapolated, the
refusal boundary was not loosened, and no low-frequency approximation was invented.

**What a versioned dispatch amendment would have to authorize before any calculation
could occur** — stated as prerequisites, not as a proposal:

1. **An evaluator or assembly valid at ω ≲ 3.3993 H.** The present refusal is by
   design (ε_H ≥ 1), so this requires either a treatment non-perturbative in H or an
   explicitly declared extension of the H-truncation with its own error control.
2. **An IR prescription for the resummed object's ω → 0 continuation** — regulator and
   scale — appended to the manifest *before* use, per `regulator_policy`.
3. **A reduction proved stationary in the ω → 0 scope**, or an explicit waiver of the
   `allowed_reductions` clause. This is load-bearing: the TT channel was exhibited
   **non-stationary** (shape drift up to 134%), which is why no reduction may be presumed.
4. **If the route is windowed:** a named, priced window, accepted together with its
   pre-registered penalties — and noting that Δω ≈ 4H does not by itself reach below
   the 3.3993 H boundary.
5. **A method for extracting α with an error budget.** Without it the criterion returns
   outcome 4 by its own terms, regardless of what the continuation shows.
6. **The amendment's form is fixed by the certificate itself:** a NEW versioned dispatch
   that explicitly explains why this one failed. The certificate may not be edited.

### DECISION D — CERTIFICATE / MANIFEST FACE

**No face is declared authoritative. The withdrawn claim stays withdrawn.**

#### Neutral comparison

**FACE 1**
- **Source:** `CLASS_C_DISPATCH_FROZEN.md` (immutable certificate, frozen 2026-08-22 12:29:21)
- **Literal representation:** a single prose sentence, slash-separated —
  *"isolated pole / multiple poles / branch cut / continuum / secular or nonstationary
  memory / no long-memory structure / ill-posed even after assembly."*
- **Six-class interpretation:** 7 slash-delimited tokens; under the contiguous-run
  mapping below they reduce to the same six classes.

**FACE 2**
- **Source:** `CLASS_C_MANIFEST.json`, `manifest_version` "1.1", key `permitted_outcome_classes`
- **Literal representation:** a JSON array of six strings — `isolated pole` ·
  `multiple poles / ladder` · `branch cut / continuum` · `secular / nonstationary memory` ·
  `no long-memory structure` · `ill-posed even after assembly`
- **Six-class interpretation:** six, explicitly enumerated.

**FACE 3**
- **Source:** `CLASS_C_DISPATCH_SPEC.md` §6
- **Literal representation:** a numbered markdown list, 1–6 — **Pole** ·
  **Multiple poles / ladder** · **Branch cut / continuum** · **Secular / nonstationary
  memory** · **No long-memory structure** · **Ill-posed even after assembly**
- **Six-class interpretation:** six, explicitly numbered.

#### Where they differ syntactically

- Face 1 uses `/` as **both** the item separator **and** the intra-class alternation
  separator. Three of the six classes themselves contain `/`, so the prose face is
  inherently ambiguous — this is the entire source of the 7-vs-6 count.
- Face 1 **drops "ladder"** from class 2.
- Face 3 names class 1 **"Pole"**; Face 2 names it **"isolated pole"**.
- `provenance/class_c_freeze.py` **hardcodes** Face 1's prose string and never reads
  `permitted_outcome_classes`, so the faces were never derived from one another.

#### Whether they differ semantically

**No semantic difference was found among the three faces — scoped strictly to the
six-class interpretation compared here.** All six meanings appear on all three, and each
face's set is closed.

**This does NOT establish that the three documents are interchangeable for any other
purpose.** It establishes one thing: the same six-class mapping holds under the comparison
performed. The dropped "ladder", the "Pole" vs "isolated pole" naming, and the
out-of-force `C1.g` all remain open, and any of them could matter for a use other than
enumerating the six classes.

#### Mappings PROVEN

Every Face-2 class is reconstructible as a **contiguous run** of Face-1 tokens, each
token consumed exactly once:

    cert 1     -> class 1  isolated pole
    cert 2     -> class 2  multiple poles / ladder        (Face 1 omits "ladder")
    cert 3 + 4 -> class 3  branch cut / continuum         PROVEN
    cert 5     -> class 4  secular / nonstationary memory
    cert 6     -> class 5  no long-memory structure
    cert 7     -> class 6  ill-posed even after assembly  PROVEN

#### What remains genuinely ambiguous

1. **Which face is contractually authoritative.** Five contract files contain **no**
   precedence statement, and the register itself records the face adjudication as
   **owner-owed**. `supersedes` orders manifest *versions*; it establishes no
   representational precedence.
2. **Whether the two textual defects** (dropped "ladder"; "Pole" vs "isolated pole")
   are errata to be corrected or are themselves frozen content.
3. **The status of an out-of-force extra class.**
   `provenance/prereg/PREREG_TERMINATION_V5_DRAFT.txt` defines a catch-all
   **C1.g — "ANOTHER STRUCTURE justified by calculation"**. It is absent from the hashed
   prereg MANIFEST, therefore **unsigned and not in force** — a contradiction hazard for
   any reader, not a registered seventh class.

**Owner decision required:** declare which representation binds, and dispose of the two
textual defects and the out-of-force draft. Neither the certificate nor the manifest was
modified.

### DECISION E — HASH-PIN DRIFT (integrity, not physics)

Verified:

- **5 of 11** certificate hash-pins have drifted:
  `CLASS_C_MANIFEST.json`, `CLASS_C_DISPATCH_SPEC.md`,
  `provenance/CLASS_C_CONTAMINATION_AUDIT.md`,
  `provenance/class_c_contamination_audit.py`, `provenance/class_c_manifest_gate.py`.
- **The drifted content has not been located in git history.** What changed is therefore
  **not characterized**, and is not characterizable from the repository.
- **Only one drift is declared** (the manifest's, via v1.0 → v1.1).
- **No gate verifies these pins.** The freeze script emits them and has no verify mode;
  the manifest gate checks key presence, never hashes.
- `class_c_manifest_gate.py` is **itself pinned and itself drifted**.

The current content is **not** assumed correct. No pin was repaired. This is an
integrity/provenance issue and **not a physics failure**; the six-class taxonomy is
intact and no physics artifact or ledger entry changes either way.

**Owner choices — none selected:**

- **E1.** Freeze current state and commission provenance recovery.
- **E2.** Re-freeze / re-pin through a new versioned certificate process.
- **E3.** Declare the affected certificate face unusable pending recovery.

### DECISION F — THREE HELD FLAGS

The historical 23 flags are **not** blanket-accepted and the prior review is **not**
reinterpreted. The three actual owner decisions:

- **F1.** Collective baseline acceptance — authorize or decline the single baseline
  refresh covering the 20 F1 flags and the already-authorized changes under the 3 F2 flags.
- **F2.** Tier contradiction — `rung1_inin_formalism` and `rung2_kms_gate` are `shown`
  resting on `assumed` `background_time_translation_flow`. Repair the edge, waive with a
  documented note, or leave standing as expected-red.
- **F3.** Orphan disposition — `response_lorentz_covariance` is `shown` with empty
  `depends_on`. Annotate as borrowed-axiom-class, or attach a dependency edge.

---

## 3. OWNER OPTIONS — WITHOUT SELECTING ONE

A1/A2/A3 · B1/B2/B3 · C: amendment prerequisites 1–6 above · D: declare a binding face
· E1/E2/E3 · F1/F2/F3. **The agent selects none of these.**

---

## 4. CURRENT REGISTER STATE

Untouched. Net **+16**. CC-C. Axis-2 **C**. Gate-E **A**. Noise **A**. Tier-4 **banked**.
Λ_R: **one** unresolved irreducible constant. H² locals: **fork-gated**. D3(iii): closed
for current TT-bath scope. General-gauge uniqueness: **NOT CLAIMED**.

---

## 5. EXACT PREREQUISITES FOR A FUTURE LOW-FREQUENCY RUN

All six items under Decision C, plus: whichever of A2 and B2 the owner authorizes must be
**registered before** the run, not during it. Nothing may be presumed by the executing
instrument.

---

## 6. INTEGRITY / PROVENANCE ISSUES

The five drifted hash-pins (Decision E), the undiagnosable drift content, the absent
verification gate, the self-certifying manifest gate, and the unsigned V5 draft carrying
an out-of-force seventh class. **None of these is physics evidence.**

---

## 7. ANTI-OVERCLAIM FIREWALL

- D4-A is accepted **only** within the declared TT-bath consequence scope.
- **General-gauge uniqueness remains NOT CLAIMED.**
- D4-A **does not** determine a consequence class.
- **The branch cut alone does not satisfy the registered Class-3 criterion** — that
  criterion is stated on the IR-resummed object continued to ω → 0 and demands an
  exponent with an error budget.
- **No low-frequency result exists yet.**
- **No IR prescription is licensed.**
- **No epoch window is licensed.**
- **Λ_R remains unresolved.**
- **H² local terms remain fork-gated.**
- **No physics artifact was changed by this decision packet.**

## HARD STOP

No physics executed. No IR regulator. No epoch window. No ω ≪ H evaluation. Tier-4
evaluator unaltered. No frozen artifact mutated. No consequence class. Nothing banked.
**Every decision above is the owner's.**
