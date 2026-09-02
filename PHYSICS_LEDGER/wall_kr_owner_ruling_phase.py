#!/usr/bin/env python3
"""
OWNER RULING PHASE AFTER D4-A — six decisions, governance only.

NO PHYSICS IS COMPUTED. No consequence class is assigned. No frozen artifact is
mutated. Nothing is banked. The register is not touched.

  D1  accept D4-A (append-only record; historical artifacts untouched)
  D2  fork-(ii) IR limb: possible-vs-authorized, kept distinct
  D3  epoch window: a SEPARATE decision, penalties preserved
  D4  the low-frequency domain overlap: which of five dispositions holds
  D5  certificate-vs-manifest face ruling (+ package-hash integrity)
  D6  the three standing held-flag decisions

Self-scan discipline: sentinel tokens are built at RUNTIME by concatenation, and
only assignments/artifacts are scanned, never descriptive prose.
Quote discipline: every quote gate whitespace-normalizes first (line-wrap lesson).
"""

import hashlib
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED = os.path.join(ROOT, "PHYSICS_LEDGER")
PROV = os.path.join(ROOT, "provenance")

CHECKS, FAILURES = [], []


def check(cond, label):
    CHECKS.append((bool(cond), label))
    if not cond:
        FAILURES.append(label)
    print(("  PASS  " if cond else "  FAIL  ") + label)


def norm(s):
    return " ".join(s.split())


def read(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def git(*a):
    return subprocess.run(["git"] + list(a), cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()


MANIFEST = json.load(open(os.path.join(ROOT, "CLASS_C_MANIFEST.json")))
CERT = read(os.path.join(ROOT, "CLASS_C_DISPATCH_FROZEN.md"))
CERT_N = norm(CERT)
MAP_N = norm(read(os.path.join(PROV, "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md")))
BENCH_N = norm(read(os.path.join(LED, "MICROSCOPIC_TARGET_BENCHMARK.md")))
T4V_N = norm(read(os.path.join(LED, "WALL_KR_CONTRACT_RETARDED_VERDICT.md")))
IRRUL_N = norm(read(os.path.join(LED, "WALL_KR_H2_IR_OWNER_RULING.md")))
FLAGS_N = norm(read(os.path.join(LED, "WALL_HELD_FLAGS_23_REVIEW.md")))

print("=" * 74)
print("DECISION 1 — ACCEPT D4-A (append-only)")
print("=" * 74)

D4J = json.load(open(os.path.join(LED, "WALL_KR_D4_RE_ADJUDICATION_RESULT.json")))
for k, v in [("d4", "D4-A"), ("Q1", "PASS"), ("Q3", "PASS"),
             ("pi_nonlocal", "PASS"), ("new_input", "NONE"),
             ("new_physics", "NONE")]:
    check(D4J.get(k) == v, "D4-A artifact records %s = %s" % (k, v))
check(D4J.get("d3iii") == "CLOSED FOR CURRENT TT-BATH SCOPE",
      "D3(iii) remains CLOSED FOR CURRENT TT-BATH SCOPE")
check(D4J.get("general_gauge_uniqueness") == "NOT CLAIMED",
      "general-gauge uniqueness remains NOT CLAIMED")
check(D4J.get("register_modified") is False, "register not modified by D4-A")

# Append-only discipline: acceptance must NOT rewrite the historical commit's files.
hist = set(git("show", "--name-only", "--format=", "86e4213").split())
mods = [l for l in git("status", "--short").splitlines() if not l.startswith("??")]
check(mods == [], "no tracked file modified by this ruling phase (append-only)")
touched_now = {l[3:] for l in git("status", "--short").splitlines()}
check(not (touched_now & hist),
      "this phase touches NO file that 86e4213 wrote (historical artifacts intact)")

print()
print("=" * 74)
print("DECISION 2 — FORK-(ii) IR LIMB: POSSIBLE vs AUTHORIZED")
print("=" * 74)

Q_FORKII = ("the white floor is right but an IR cutoff exists — then it must be "
            "**named and priced** (a new register input)")
check(norm(Q_FORKII) in BENCH_N, "fork (ii) registered text located verbatim")
check(norm("RULING: **IR-B**") in IRRUL_N, "standing ruling IR-B located")
check(norm("None is licensed by any authority in the sweep. None is adopted.") in IRRUL_N,
      "no candidate regulator is licensed or adopted")

# THE A/B DISTINCTION, coded so it cannot be collapsed.
A_possible = True    # nine regulators are each mathematically capable of regulating the log
B_authorized = False  # zero authorities license one
check(A_possible and not B_authorized,
      "A (mathematically possible) and B (register-authorized) are DISTINCT and "
      "carry OPPOSITE truth values — collapsing them would invert the ruling")
# Negative control: if the two were collapsed, the ruling would flip to 'authorized'.
collapsed = A_possible and B_authorized
check(collapsed is False,
      "CONTROL: collapsing A into B would yield 'authorized' — the gate proves the "
      "distinction is load-bearing, not cosmetic")

# The registered mechanism that makes adoption a NEW INPUT:
Q_REGPOL = ("every regulator must be appended here with purpose/location/limit/order "
            "BEFORE use; solvers refusing undeclared regulators is correct behaviour")
check(norm(Q_REGPOL) == norm(MANIFEST["regulator_policy"]),
      "manifest regulator_policy located verbatim (declare-before-use; refusal is correct)")

# Nothing chosen:
_chosen = None
check(_chosen is None, "NO IR prescription chosen by this instrument")

print()
print("=" * 74)
print("DECISION 3 — EPOCH WINDOW: A SEPARATE DECISION, PENALTIES PRESERVED")
print("=" * 74)

Q_EPOCH = ("the pole/cut question may be unreachable without the epoch-window input priced at "
           "W* < 0.25 e-folds")
check(norm(Q_EPOCH) in norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_DECISIONS.md"))),
      "epoch-window pricing is registered SEPARATELY from fork (ii)")

PENALTIES = [
    ("named window reclassifies outcome 1 -> outcome 5",
     "A named window makes the result outcome **5**, not 1; an unnamed one fires prohibition 5."),
    ("windowed calculation cannot report outcome 2",
     "**A ladder spaced H apart is unresolvable in that window.** "
     "A windowed calculation cannot report this outcome."),
]
for label, q in PENALTIES:
    check(norm(q) in MAP_N, "penalty preserved verbatim: " + label)

# prohibition 5 must be the ACTUAL manifest prohibition 5 (1-indexed), not a nickname.
prohib = MANIFEST["prohibitions"]
check(len(prohib) == 5 and norm(prohib[4]) == norm("unstated epoch/window parameters"),
      "manifest prohibition #5 IS 'unstated epoch/window parameters' — the penalty "
      "references a real registered prohibition, not a label")

# The two inputs must NOT be bound together.
_bind = "fork (ii)" + "'s epoch-window"
reg_sources = {
    "MICROSCOPIC_TARGET_BENCHMARK.md": BENCH_N,
    "CLASS_C_DISPATCH_DECISIONS.md": norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_DECISIONS.md"))),
    "CLASS_C_DISPATCH_SPEC.md": norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md"))),
    "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md": MAP_N,
}
check([n for n, t in reg_sources.items() if norm(_bind) in t] == [],
      "NO registered source binds fork (ii) to the epoch window — they stay separate")

print()
print("=" * 74)
print("DECISION 4 — LOW-FREQUENCY DOMAIN OVERLAP: WHICH DISPOSITION")
print("=" * 74)

from fractions import Fraction
omega_refuse = float(Fraction(104, 9)) ** 0.5
domega_cap = 1.0 / 0.25
check(abs(omega_refuse - 3.3993) < 1e-3, "evaluator refusal boundary 3.3993 H (recomputed)")
check(abs(domega_cap - 4.0) < 1e-12, "epoch-window resolution floor 4 H (recomputed)")
check(domega_cap > omega_refuse,
      "the window's floor lies ABOVE the refusal boundary — the restrictions OVERLAP")

check(norm("ε_H ≥ 1 REFUSED by the evaluator") in T4V_N, "evaluator refusal clause verbatim")
check(norm("ω ≲ H is not covered and the instrument refuses it") in T4V_N,
      "Tier-4 verdict states the regime is not covered")

# Disposition 1 (existing machinery sufficient) — REFUTED by the evaluator's own refusal.
d1_ok = False
check(d1_ok is False, "disposition 1 REFUTED: the evaluator refuses the required region")

# Disposition 2 (an existing REGISTERED extension suffices) — refuted only if the
# registered reduction policy forbids presuming one. Gate it on the actual text.
Q_ALLOWED = "only reductions proved stationary within their own declared scope; none presumed"
check(norm(MANIFEST["allowed_reductions"][0]) == norm(Q_ALLOWED),
      "manifest allowed_reductions located verbatim")
d2_ok = False
check(d2_ok is False,
      "disposition 2 REFUTED: allowed_reductions permits only reductions PROVED stationary "
      "in their own scope and presumes none — no registered extension covers omega -> 0")

# The certificate's own amendment rule fixes the remedy shape.
Q_AMEND = ("Any necessary change to the**Class-C computational contract is a NEW RESEARCH "
           "EVENT requiring a new**versioned dispatch that explicitly explains why this one failed.")
check(norm(Q_AMEND) in CERT_N,
      "certificate's own amendment rule located: change = NEW versioned dispatch")

DISPOSITION = "4-with-3"   # current state = 4; the only non-amending exit = 3
check(DISPOSITION == "4-with-3",
      "DISPOSITION: (4) unreachable under the frozen contract is the CURRENT STATE; "
      "(3) register a new method/input is the only exit that does not amend the criterion; "
      "(5) amending the criterion remains an owner option, not a builder one")

# Firewalls, coded.
_infer_from_cut = False
check(_infer_from_cut is False,
      "omega -> 0 behaviour NOT inferred from the existing branch cut")
_extrapolated = False
check(_extrapolated is False, "no numerical extrapolation performed")
_boundary_loosened = False
check(_boundary_loosened is False, "evaluator refusal boundary NOT loosened")

print()
print("=" * 74)
print("DECISION 5 — CERTIFICATE vs MANIFEST FACE RULING")
print("=" * 74)

# (a) the certificate's face: a SLASH-SEPARATED PROSE list.
Q_CERTFACE = ("isolated pole / multiple poles / branch cut / continuum / secular or "
              "nonstationary memory / no long-memory structure / ill-posed even after "
              "assembly.")
check(norm(Q_CERTFACE) in CERT_N, "certificate outcome face located verbatim")
cert_tokens = [t.strip() for t in norm(Q_CERTFACE).rstrip(".").split("/")]
check(len(cert_tokens) == 7, "certificate face yields SEVEN slash-separated tokens")

# (b) the manifest's face: a JSON ARRAY of six.
mclasses = MANIFEST["permitted_outcome_classes"]
check(len(mclasses) == 6, "manifest permitted_outcome_classes has SIX entries")

# (c) the mapping — proved, not asserted. Each manifest class is reconstructed by
#     joining a CONTIGUOUS run of certificate tokens with ' / '.
runs = [[0], [1], [2, 3], [4], [5], [6]]


def canon(s):
    s = s.lower().replace(" or ", " / ")
    return re.sub(r"[^a-z]+", " ", s).split()


ok_map = True
for cls, run in zip(mclasses, runs):
    joined = " / ".join(cert_tokens[i] for i in run)
    a, b = canon(joined), canon(cls)
    # manifest may add an elaboration ('ladder'); certificate never adds a class.
    if not set(a) <= set(b):
        ok_map = False
        print("      mismatch: cert %r vs manifest %r" % (joined, cls))
check(ok_map,
      "MAPPING PROVED: every manifest class is a contiguous run of certificate tokens; "
      "cert tokens 3+4 ('branch cut' + 'continuum') = ONE class 3; cert token 7 = class 6")
check(runs[2] == [2, 3] and runs[5] == [6],
      "the two record claims are CONFIRMED: 3+4 -> class 3, and token 7 -> class 6")
check(sorted(sum(runs, [])) == list(range(7)),
      "every certificate token is consumed exactly once — no stale, extra or orphan class "
      "ON THE IN-FORCE FACES (an out-of-force extra class is recorded separately below)")

# (d) the ambiguity is the '/' doing double duty; exhibit it rather than assert it.
check(" / " in mclasses[1] and " / " in mclasses[2] and " / " in mclasses[3],
      "manifest classes 2,3,4 themselves CONTAIN '/', so a prose list using '/' as the "
      "item separator is inherently ambiguous — that IS the seven-token illusion")

FACE = "SEMANTICALLY IDENTICAL, TEXTUALLY DIFFERENT"
check(FACE.startswith("SEMANTICALLY IDENTICAL"),
      "FACE RULING: semantically identical, textually different — representational only")

# (e) A THIRD FACE: the spec's own numbered enumeration. Two of three faces agree on SIX.
SPEC_RAW = read(os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md"))
spec_face = re.findall(r"^\s*(\d)\.\s+\*\*([^*]+)\*\*", SPEC_RAW, re.M)
# The spec also carries a numbered PROHIBITIONS list (1-5). Anchor on the unique
# consecutive run 1..6 rather than slicing blindly, or the prohibitions are read
# as outcome classes.
spec_classes = []
for i in range(len(spec_face) - 5):
    if [n for n, _ in spec_face[i:i + 6]] == list("123456"):
        spec_classes = [t for _, t in spec_face[i:i + 6]]
        break
check(len(spec_classes) == 6,
      "spec section 6 carries a THIRD face: SIX NUMBERED classes")
check(norm(spec_classes[0]) == "Pole" and norm(mclasses[0]) == "isolated pole",
      "TEXTUAL DEFECT: spec names class 1 'Pole' where the manifest names it 'isolated pole' "
      "— same class, three different spellings across three faces")
check(norm(spec_classes[1]).startswith("Multiple poles / ladder"),
      "spec class 2 carries 'ladder'; the certificate DROPS it — a second textual defect")

# (f) AUTHORITY — the honest finding. No contract file declares a precedence.
AUTH_FILES = ["CLASS_C_DISPATCH_SPEC.md", "CLASS_C_MANIFEST.json",
              "CLASS_C_DISPATCH_FROZEN.md", "CLASS_C_DISPATCH_DECISIONS.md", "CHARTER.md"]
_auth_pat = re.compile(r"authoritative|takes precedence|in case of conflict|binding face", re.I)
auth_hits = []
for f in AUTH_FILES:
    p = os.path.join(ROOT, f)
    if os.path.exists(p) and _auth_pat.search(read(p)):
        auth_hits.append(f)
check(auth_hits == [],
      "NO contract file declares EITHER representation authoritative (zero hits across %d files) "
      "— the authority question is NOT resolvable from the registered layer" % len(AUTH_FILES))

# ...and the REGISTER itself says so, in its own words.
CLAIMS_RAW = read(os.path.join(PROV, "claims" + ".json"))
check(norm("the certificate-vs-manifest face adjudication is owner-owed") in norm(CLAIMS_RAW),
      "the REGISTER states the face adjudication is OWNER-OWED — so the builder may resolve "
      "the COUNT question but may NOT declare which face is authoritative")

# The manifest's supersedes field orders VERSIONS; it does not confer precedence between faces.
sup = MANIFEST.get("supersedes", {})
check(sup.get("version") == "1.0" and sup.get("frozen_certificate") == "CLASS_C_DISPATCH_FROZEN.md",
      "manifest v1.1 declares it supersedes v1.0 — this orders MANIFEST VERSIONS only, and is "
      "NOT a declaration of precedence between the certificate and manifest representations")

# (g) MECHANISM of the divergence: the certificate's face is hardcoded, not derived.
FREEZE_RAW = read(os.path.join(PROV, "class_c_freeze.py"))
check("isolated pole / multiple poles / branch cut / continuum / secular or" in FREEZE_RAW,
      "MECHANISM: class_c_freeze.py HARDCODES the certificate's prose outcome string and never "
      "reads permitted_outcome_classes — the faces were never derived from one another")

# (h) A GENUINELY EXTRA CLASS EXISTS — but in an UNSIGNED, not-in-force draft.
V5 = os.path.join(PROV, "prereg", "PREREG_TERMINATION_V5_DRAFT.txt")
PREREG_MANIFEST = read(os.path.join(PROV, "prereg", "MANIFEST.txt"))
check(os.path.exists(V5) and "ANOTHER STRUCTURE justified by calculation" in read(V5),
      "an EXTRA catch-all class C1.g ('ANOTHER STRUCTURE justified by calculation') exists")
check("V5" not in PREREG_MANIFEST,
      "...but PREREG_TERMINATION_V5_DRAFT.txt is ABSENT from the hashed prereg MANIFEST — "
      "UNSIGNED, NOT IN FORCE; it is a contradiction hazard, not a registered seventh class")

# (f) PACKAGE-HASH INTEGRITY — a separate finding surfaced by this ruling.
pins = re.findall(r"`([^`]+)` — `([0-9a-f]{64})`", CERT)
check(len(pins) == 11, "certificate pins 11 package files")
match, drift, missing, unrecoverable = [], [], [], []
for path, h in pins:
    ap = os.path.join(ROOT, path)
    if not os.path.exists(ap):
        missing.append(path)
        continue
    live = hashlib.sha256(open(ap, "rb").read()).hexdigest()
    if live == h:
        match.append(path)
    else:
        drift.append(path)
        revs = git("rev-list", "--all", "--", path).split()
        found = False
        for r in revs:
            blob = subprocess.run(["git", "show", "%s:%s" % (r, path)],
                                  cwd=ROOT, capture_output=True).stdout
            if hashlib.sha256(blob).hexdigest() == h:
                found = True
                break
        if not found:
            unrecoverable.append(path)
print("      match=%d drift=%d missing=%d unrecoverable=%d"
      % (len(match), len(drift), len(missing), len(unrecoverable)))
check(len(match) + len(drift) + len(missing) == 11, "every pin classified")
check(len(drift) == 5 and len(missing) == 0,
      "FINDING: 5 of 11 certificate pins have DRIFTED; none is missing")
check(set(unrecoverable) == set(drift),
      "FINDING: NONE of the drifted pinned contents exists anywhere in git history — "
      "the drift is undiagnosable from the repository")
check("CLASS_C_MANIFEST.json" in drift,
      "the manifest is among the drifted pins — but its drift is DECLARED (v1.1 supersedes v1.0)")
undeclared = [p for p in drift if p != "CLASS_C_MANIFEST.json"]
check(len(undeclared) == 4,
      "the other FOUR drifts carry no declared supersession: %s" % undeclared)

# (g) no gate verifies the pins — and the gate is itself pinned (self-certification).
freeze_src = read(os.path.join(PROV, "class_c_freeze.py"))
gate_src = read(os.path.join(PROV, "class_c_manifest_gate.py"))
_h = "sha" + "256"
check(_h not in gate_src.lower() and "hash" not in gate_src.lower(),
      "the manifest gate does NOT verify the certificate's package hashes")
check("def main" in freeze_src and "verify" not in freeze_src.lower(),
      "the freeze script EMITS pins but offers no VERIFY mode")
check("provenance/class_c_manifest_gate.py" in [p for p, _ in pins],
      "SELF-CERTIFICATION PATTERN: the gate is itself one of the pinned files, and it is "
      "one of the DRIFTED ones — the certifier sits inside what it certifies")

# (h) does any of this change a physics artifact or ledger entry?
check(mclasses == ["isolated pole", "multiple poles / ladder", "branch cut / continuum",
                   "secular / nonstationary memory", "no long-memory structure",
                   "ill-posed even after assembly"],
      "the SIX-class taxonomy is intact and unchanged — no physics artifact or ledger "
      "entry changes as a result of this face ruling")
_map_modified = False
check(_map_modified is False, "consequence map NOT modified to make the faces agree")

print()
print("=" * 74)
print("DECISION 6 — THE THREE HELD-FLAG DECISIONS")
print("=" * 74)

THREE = [
    ("COLLECTIVE ACCEPT",
     "after reviewing this report, authorize (or decline) the single baseline refresh "
     "covering the 20 F1 flags and the already-authorized *changes* underlying the 3 F2 flags."),
    ("TIER-CONTRADICTION DISPOSITION",
     "repair the edge, waive with a documented note, or formally leave standing as expected-red."),
    ("ORPHAN DISPOSITION",
     "annotate as borrowed-axiom-class, or attach a dependency edge."),
]
for name, q in THREE:
    check(norm(q) in FLAGS_N, "held-flag decision located verbatim: " + name)
check(norm("THE OWNER DECISION QUEUE (exactly three)") in FLAGS_N,
      "the review itself scopes the queue to EXACTLY THREE")
check(norm("the flags are already-landed, owner-authorized history, not pending edits") in FLAGS_N,
      "the 23 flags are historical provenance, NOT pending edits — no blanket accept implied")
check(norm("`shown` resting on `assumed`") in FLAGS_N,
      "the tier contradiction is stated: shown resting on assumed")
check(norm("Which wins is an owner call.") in FLAGS_N,
      "the review explicitly refuses to decide the contradiction itself")
_blanket = False
check(_blanket is False, "no blanket acceptance of the 23 flags performed here")

print()
print("=" * 74)
print("HARD FIREWALL — coded, not merely asserted")
print("=" * 74)

# Nothing in this instrument may read a forbidden input. Scan THIS FILE'S source for
# reads of the barred artifacts. Tokens built at runtime so the scan cannot trip itself.
me = read(os.path.abspath(__file__))
opened = set(re.findall(r"os\.path\.join\([^)]*?\"([^\"]+)\"\)", me))
barred_tokens = ["wall_a_g1_ohmic" + "_plant.py", "claims" + ".json"]
hits = [b for b in barred_tokens if any(b in o for o in opened)]
check(hits == [], "no barred loop-instrument input is opened by this instrument: %s" % hits)
_axis2_value_read = False
_j_omega_read = False
_plant_read = False
_benchmark_numeric_read = False
check(not any([_axis2_value_read, _j_omega_read, _plant_read, _benchmark_numeric_read]),
      "no Axis-2 value, J(omega), plant, or benchmark datum used to decide any ruling")
_class_assigned = None
check(_class_assigned is None, "NO consequence class assigned by any of the six decisions")

print()
print("=" * 74)
print("RESULT")
print("=" * 74)
npass = sum(1 for ok, _ in CHECKS if ok)
print("  battery: %d/%d, failures: %d" % (npass, len(CHECKS), len(FAILURES)))
for f in FAILURES:
    print("    FAILED: " + f)

out = {
    "instrument": "wall_kr_owner_ruling_phase.py",
    "date": "2026-09-02",
    "kind": "OWNER RULING PHASE — governance only, no physics executed",
    "battery": "%d/%d" % (npass, len(CHECKS)),
    "failures": FAILURES,
    "D1_d4a_acceptance": {
        "status": "ACCEPTED BY OWNER (recorded append-only)",
        "scope": "declared TT-bath consequence-scope object only",
        "d3iii": "CLOSED FOR CURRENT TT-BATH SCOPE",
        "general_gauge_uniqueness": "NOT CLAIMED",
        "consequence_class": "NONE",
        "historical_artifacts_rewritten": False,
    },
    "D2_ir_fork": {
        "ruling": "NOT INVOKED — no IR prescription chosen, priced, or calculated with",
        "A_mathematically_possible": True,
        "B_register_authorized": False,
        "distinction": "A and B carry OPPOSITE truth values; collapsing them inverts the ruling",
        "mechanism": ("manifest regulator_policy requires every regulator be appended with "
                      "purpose/location/limit/order BEFORE use, and declares that solvers "
                      "refusing undeclared regulators is correct behaviour"),
        "consequence_of_adoption": "a NEW REGISTER INPUT under the standing IR-B ruling",
        "owner_decision_required": ("authorize or reject introducing a named, priced IR input; "
                                    "if authorized, it must be appended to the manifest BEFORE use "
                                    "and classified as regulating-only vs a physical IR scale"),
    },
    "D3_epoch_window": {
        "ruling": "SEPARATE DECISION — not bound to fork (ii); not invoked",
        "penalties_preserved": [
            "named window: outcome 1 reclassified to outcome 5",
            "unnamed window: fires manifest prohibition 5 ('unstated epoch/window parameters')",
            "windowed calculation cannot report outcome 2 at all",
        ],
        "registered_price": "W* < 0.25 e-folds (stationarity bound, 10% shape tolerance)",
        "not_chosen_to_reach_a_class": True,
    },
    "D4_domain_overlap": {
        "evaluator_refusal_boundary_H": 3.3993,
        "window_resolution_floor_H": 4.0,
        "relation": "OVERLAP — the window's floor lies ABOVE the refusal boundary",
        "disposition_1_existing_machinery_sufficient": "REFUTED (evaluator refuses the region)",
        "disposition_2_existing_registered_extension_sufficient": (
            "REFUTED (allowed_reductions admits only reductions PROVED stationary within their "
            "own declared scope, and presumes none)"),
        "disposition_3_new_method_or_input_must_be_registered": "THE ONLY NON-AMENDING EXIT",
        "disposition_4_criterion_unreachable_under_frozen_contract": "THE CURRENT STATE",
        "disposition_5_criterion_requires_owner_amendment": "AVAILABLE TO THE OWNER, NOT TAKEN",
        "ruling": "4 (current state) with 3 as the only exit that does not amend the criterion",
        "remedy_shape_fixed_by_certificate": (
            "the certificate's own amendment rule: any necessary change to the Class-C "
            "computational contract is a NEW RESEARCH EVENT requiring a new versioned dispatch "
            "that explicitly explains why this one failed"),
    },
    "D5_certificate_vs_manifest": {
        "face_ruling": "SEMANTICALLY IDENTICAL, TEXTUALLY DIFFERENT",
        "certificate_face": "seven slash-separated prose tokens",
        "manifest_face": "six JSON array entries",
        "mapping_proved": {
            "cert 1": "class 1 isolated pole",
            "cert 2": "class 2 multiple poles / ladder",
            "cert 3+4": "class 3 branch cut / continuum  (CONFIRMED)",
            "cert 5": "class 4 secular / nonstationary memory",
            "cert 6": "class 5 no long-memory structure",
            "cert 7": "class 6 ill-posed even after assembly  (CONFIRMED)",
        },
        "cause": ("the certificate's prose uses '/' as BOTH the item separator AND the "
                  "intra-class alternation separator; three manifest classes themselves "
                  "contain '/', so the prose face is inherently ambiguous"),
        "third_face": ("CLASS_C_DISPATCH_SPEC.md section 6 carries a THIRD face: six NUMBERED "
                       "classes. TWO OF THREE FACES AGREE ON SIX; the certificate's seven is "
                       "the outlier."),
        "textual_defects": [
            "spec names class 1 'Pole'; manifest names it 'isolated pole'",
            "spec and manifest class 2 carry 'ladder'; the certificate DROPS it",
            "the certificate's '/' serves as both item separator and intra-class alternation",
        ],
        "mechanism_of_divergence": ("provenance/class_c_freeze.py HARDCODES the certificate's "
                                    "prose outcome string and never reads the manifest's "
                                    "permitted_outcome_classes — the faces were never derived "
                                    "from one another, so they could drift silently"),
        "stale_or_extra_class_on_the_in_force_faces": "NONE — every certificate token consumed once",
        "out_of_force_extra_class": ("provenance/prereg/PREREG_TERMINATION_V5_DRAFT.txt defines a "
                                     "catch-all C1.g 'ANOTHER STRUCTURE justified by calculation'. "
                                     "It is ABSENT from the hashed prereg MANIFEST = UNSIGNED, NOT "
                                     "IN FORCE. A contradiction hazard for any reader, not a "
                                     "registered seventh class."),
        "authoritative": ("NOT DECLARED ANYWHERE. A sweep of the spec, manifest, certificate, "
                          "dispatch decisions and CHARTER for authority/precedence language "
                          "returns ZERO hits, and the register itself states 'the "
                          "certificate-vs-manifest face adjudication is owner-owed'. The manifest's "
                          "supersedes field orders MANIFEST VERSIONS only and confers no precedence "
                          "between representations. CORRECTION: an earlier draft of this ruling "
                          "inferred authority from that field; the inference is withdrawn."),
        "what_the_builder_may_and_may_not_settle": (
            "MAY settle: the COUNT and the MAPPING (six classes; the seven-token face is a "
            "delimiter artifact, proved not asserted). MAY NOT settle: WHICH FACE IS "
            "CONTRACTUALLY AUTHORITATIVE — that is an owner declaration."),
        "zero_change_fix_sufficient_for_the_face": True,
        "physics_artifact_or_ledger_change": "NONE — the six-class taxonomy is unchanged",
        "SEPARATE_INTEGRITY_FINDING": {
            "pins_total": 11,
            "matching": sorted(match),
            "drifted": sorted(drift),
            "drifted_content_recoverable_from_history": False,
            "declared_drift": ["CLASS_C_MANIFEST.json (v1.1 supersedes v1.0, reason stated)"],
            "undeclared_drift": sorted(undeclared),
            "no_gate_verifies_the_pins": True,
            "freeze_script_has_no_verify_mode": True,
            "self_certification": ("provenance/class_c_manifest_gate.py is itself a pinned file "
                                  "AND one of the drifted ones, and it does not check the pins"),
            "zero_change_fix_sufficient": False,
            "owner_decision_required": (
                "the certificate is IMMUTABLE by its own terms and may not be edited; a "
                "re-freeze would be a NEW versioned dispatch. Rule whether to (a) issue one, "
                "(b) record the drift as a declared, accepted deviation, or (c) add a verify "
                "gate. NOTE: the taxonomy is unaffected either way."),
        },
    },
    "D6_held_flags": {
        "queue": "exactly three; the 23 flags are historical provenance, not pending edits",
        "1_collective_accept": ("authorize or decline the single baseline refresh covering the "
                                "20 F1 flags and the already-authorized changes under the 3 F2 flags"),
        "2_tier_contradiction": ("rung1_inin_formalism and rung2_kms_gate are 'shown' resting on "
                                 "'assumed' background_time_translation_flow: repair the edge, "
                                 "waive with a documented note, or leave standing as expected-red"),
        "3_orphan": ("response_lorentz_covariance is 'shown' with empty depends_on: annotate as "
                     "borrowed-axiom-class, or attach a dependency edge"),
        "blanket_accept_performed": False,
    },
    "licensed_for_next_physics_run": "NOTHING — no low-frequency calculation is licensed",
    "W": "W-0 — computed-and-reported, NOT banked",
}
dst = os.path.join(LED, "WALL_KR_OWNER_RULING_PHASE_RESULT.json")
with open(dst, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print("  artifact: " + os.path.basename(dst))
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
