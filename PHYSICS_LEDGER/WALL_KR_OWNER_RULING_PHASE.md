# OWNER RULING PHASE AFTER D4-A — SIX DECISIONS

**Date:** 2026-09-02 · **Instrument:** `wall_kr_owner_ruling_phase.py` ·
**Artifact:** `WALL_KR_OWNER_RULING_PHASE_RESULT.json` ·
**Battery: 75/75, zero failures.**
**Governance only. No physics executed. No consequence class assigned. No
frozen artifact mutated. Register untouched. Nothing banked. W-0.**

**The question this phase answers is "are we allowed to calculate?" — not
"what does the calculation say?"** The answer is no, and the reasons are
three separate ones.

---

## DECISION 1 — D4-A ACCEPTED

Commit `86e4213` is accepted as the formal D4-A adjudication for the
**declared TT-bath consequence-scope object**, recorded here append-only.
No historical artifact was rewritten; this phase modified no tracked file
and touched no file that `86e4213` wrote.

Acceptance means only: D4-A accepted; external orbit satisfied; internal
K-term satisfied; Π_nonlocal invariance satisfied through the
charter-licensed operator-identity route; Q1/Q3 satisfied structurally;
D3(iii) remains CLOSED FOR CURRENT TT-BATH SCOPE; general-gauge
uniqueness remains NOT CLAIMED; no consequence class; no new physics; no
new input.

## DECISION 2 — FORK-(ii) NOT INVOKED

No IR prescription was chosen, priced, or calculated with.

**The distinction, kept open and coded so it cannot collapse:**

| | |
|---|---|
| **A — mathematically possible** | **TRUE.** Nine regulators are each capable of regulating the log. |
| **B — authorized by the register** | **FALSE.** Zero authorities license one. |

A and B carry **opposite truth values**. A gate confirms that collapsing A
into B would invert the ruling to "authorized" — so the distinction is
load-bearing, not cosmetic.

**The mechanism that makes adoption a new input** is registered in the
manifest: *"every regulator must be appended here with
purpose/location/limit/order BEFORE use; solvers refusing undeclared
regulators is correct behaviour."* Note the second clause — **the
evaluator's refusal is contractually correct behaviour, not a limitation
to be engineered around.**

**Owner decision required:** authorize or reject introducing a named,
priced IR input. If authorized, it must be appended to the manifest
*before* use and classified as regulating-only versus a physical IR scale
— the first may leave the parameter count unchanged, the second is a new
counted input.

## DECISION 3 — EPOCH WINDOW: A SEPARATE DECISION

Not bound to fork (ii); not invoked. A gate confirms **no registered
source binds the two** — the bundling exists only in an unbanked builder
record of mine.

Penalties preserved verbatim:

- a **named** window makes the result **outcome 5, not outcome 1**;
- an **unnamed** window fires **prohibition 5** — verified to be the
  actual manifest prohibition #5, *"unstated epoch/window parameters"*,
  not a nickname;
- a windowed calculation **cannot report outcome 2 at all**.

Registered price: W* < 0.25 e-folds (stationarity bound, 10% shape
tolerance). No window was chosen, and none may be chosen to make a
consequence class reachable.

## DECISION 4 — THE LOW-FREQUENCY OVERLAP: DISPOSITION 4, WITH 3 AS THE EXIT

| | |
|---|---|
| evaluator refusal boundary | ω = √(104/9)·H = **3.3993 H** |
| epoch-window resolution floor | Δω ≈ 1/W* = **4 H** |
| relation | **OVERLAP** — the floor lies *above* the boundary |

- **Disposition 1 — existing machinery sufficient: REFUTED.** The
  evaluator raises DomainRejected in the required region.
- **Disposition 2 — an existing registered extension suffices: REFUTED**
  by the manifest's own `allowed_reductions`: *"only reductions proved
  stationary within their own declared scope; none presumed."* Nothing
  registered covers ω → 0.
- **Disposition 3 — a new method/input must be registered:** the **only
  exit that does not amend the criterion**.
- **Disposition 4 — the criterion is currently unreachable under the
  frozen contract:** **this is the current state.**
- **Disposition 5 — amend the criterion:** available to the owner, not
  taken here.

**Ruling: 4 is the state; 3 is the exit.** The remedy's *shape* is fixed
by the certificate's own amendment rule — any necessary change to the
Class-C computational contract is a NEW RESEARCH EVENT requiring a new
versioned dispatch that explains why this one failed.

ω → 0 behaviour was **not** inferred from the existing branch cut; nothing
was extrapolated; the refusal boundary was not loosened.

## DECISION 5 — CERTIFICATE vs MANIFEST: THE FACE RULING

### The count question: RESOLVED — semantically identical, textually different

There are **three** faces, not two:

| face | form | count |
|---|---|---|
| `CLASS_C_DISPATCH_FROZEN.md` (certificate) | slash-separated prose | **7 apparent tokens** |
| `CLASS_C_MANIFEST.json` v1.1 | JSON array | **6** |
| `CLASS_C_DISPATCH_SPEC.md` §6 | numbered list | **6** |

**Two of three agree on six; the certificate is the outlier.** The mapping
is *proved*, not asserted — every manifest class is reconstructed as a
contiguous run of certificate tokens:

    cert 1     -> class 1  isolated pole
    cert 2     -> class 2  multiple poles / ladder
    cert 3 + 4 -> class 3  branch cut / continuum      <- CONFIRMED
    cert 5     -> class 4  secular / nonstationary memory
    cert 6     -> class 5  no long-memory structure
    cert 7     -> class 6  ill-posed even after assembly <- CONFIRMED

Every token is consumed exactly once. **Cause:** the certificate's prose
uses `/` as *both* the item separator *and* the intra-class alternation
separator, and three manifest classes themselves contain `/`. The
seven-token face is a delimiter artifact.

**Mechanism:** `provenance/class_c_freeze.py` **hardcodes** the prose
string and never reads `permitted_outcome_classes`. The faces were never
derived from one another, so they could drift without anything noticing.

**Textual defects (real, non-semantic):** the spec names class 1 *"Pole"*
where the manifest says *"isolated pole"*; the certificate **drops
"ladder"** from class 2.

### The authority question: NOT RESOLVABLE BY ME — and I withdraw an earlier inference

A sweep of the spec, manifest, certificate, dispatch decisions and CHARTER
for authority/precedence language returns **zero hits**. No contract file
declares either representation authoritative. The register itself states
*"the certificate-vs-manifest face adjudication is owner-owed."*

**Correction.** My first draft of this ruling inferred that the manifest
was authoritative from its `supersedes` field. **That inference is
withdrawn.** The field orders *manifest versions*; it confers no
precedence between *representations*. The distinction matters: I may
settle the count and the mapping, and I may not settle which face binds.

### An out-of-force extra class

`provenance/prereg/PREREG_TERMINATION_V5_DRAFT.txt` defines a genuine
catch-all **C1.g — "ANOTHER STRUCTURE justified by calculation"**. It is
**absent from the hashed prereg MANIFEST**, therefore unsigned and not in
force. A contradiction hazard for any reader, not a registered seventh
class.

### A SEPARATE INTEGRITY FINDING — the certificate's package hashes

| | |
|---|---|
| pins recorded | 11 |
| still matching | 6 |
| **drifted** | **5** |
| drifted content recoverable from git history | **none** |

Only **one** of the five drifts is declared (the manifest's, via the
v1.0→v1.1 supersession). The other four — the spec, the contamination
audit and its script, and the manifest gate — carry **no declared
supersession**. And because the pinned bytes were never committed, **what
changed is undiagnosable from the repository**; the drift can be reported
but not characterized.

**No gate verifies these pins.** The freeze script only emits them and has
no verify mode; the manifest gate checks the key's presence, never the
hashes. Worse: `provenance/class_c_manifest_gate.py` is *itself* one of
the pinned files **and** one of the drifted ones — the campaign's
self-certification pattern again, the certifier sitting inside what it
certifies.

**Zero-change fix sufficient?** For the *face*, yes — recording the
semantic identity settles it, and no physics artifact or ledger entry
changes because the six-class taxonomy is intact. For the *hash-pin
integrity*, **no**. The certificate is immutable by its own terms and may
not be edited.

**Owner decision required:** (a) issue a new versioned dispatch, (b)
record the drift as a declared and accepted deviation, or (c) add a verify
gate. The taxonomy is unaffected either way.

## DECISION 6 — THE THREE HELD FLAGS

Not blanket-accepted. The 23 flags are *"already-landed, owner-authorized
history, not pending edits."* The genuine queue is exactly three:

1. **COLLECTIVE ACCEPT** — authorize or decline the single baseline
   refresh covering the 20 F1 flags and the already-authorized changes
   under the 3 F2 flags.
2. **TIER-CONTRADICTION DISPOSITION** — `rung1_inin_formalism` and
   `rung2_kms_gate` are `shown` resting on `assumed`
   `background_time_translation_flow`. Repair the edge, waive with a
   documented note, or leave standing as expected-red. The tension is
   real: the omission was booked *precisely to expose* the presupposition,
   which is arguably correct bookkeeping, while the tier rule forbids
   `shown` on `assumed`. The review says plainly: *"Which wins is an owner
   call."*
3. **ORPHAN DISPOSITION** — `response_lorentz_covariance` is `shown` with
   empty `depends_on`. Annotate as borrowed-axiom-class, or attach a
   dependency edge.

---

## WHAT IS LICENSED FOR THE NEXT PHYSICS RUN

**Nothing. No low-frequency calculation is currently licensed.**

Three independent blockers stand, and a class-independence control
confirms all three fire identically for every hypothetical outcome — no
result is favoured by this phase.

## HARD STOP

No ω ≪ H evaluation. No IR scale. No epoch window. μ untouched, Λ_R
untouched, H² locals untouched. No frozen coefficient refit. No class
assigned. Nothing banked. No baseline refreshed.
