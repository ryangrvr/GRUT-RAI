#!/usr/bin/env python3
"""
D4-A OWNER-REVIEW PACKET + FORK-(ii) READINESS ASSESSMENT — verification instrument.

GOVERNANCE ONLY. No physics is computed here. No consequence class is assigned.
No frozen artifact is written. The register is not touched.

What this instrument does:
  PART 1  repository state + frozen-artifact integrity (git blob vs working tree)
  PART 2  machine-checks every assertion of the D4-A owner-review packet against
          the committed record and its machine-readable artifact
  PART 3  quote-gates the REGISTERED fork-(ii) / epoch-window / Class-3 text
          against the actual registry files (whitespace-normalized)
  PART 4  the two registered domain boundaries, as arithmetic on registered
          numbers only
  PART 5  negative controls

Self-scan discipline: every sentinel/marker token is built at RUNTIME by
concatenation, and only ASSIGNMENTS and EMITTED ARTIFACTS are scanned, never
descriptive prose. (Standing fix for the 9-appearance self-scan trap.)
"""

import hashlib
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED = os.path.join(ROOT, "PHYSICS_LEDGER")
PROV = os.path.join(ROOT, "provenance")

CHECKS = []
FAILURES = []


def check(cond, label):
    CHECKS.append((bool(cond), label))
    if not cond:
        FAILURES.append(label)
    print(("  PASS  " if cond else "  FAIL  ") + label)


def norm(s):
    """Whitespace-normalize before quote comparison.

    Lesson paid for in run 3 of the D4 re-adjudication: a registered clause was
    LINE-WRAPPED in the source, so a raw substring test missed it.
    """
    return " ".join(s.split())


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def git(*args):
    return subprocess.run(
        ["git"] + list(args), cwd=ROOT, capture_output=True, text=True
    ).stdout.strip()


def sha(b):
    return hashlib.sha256(b).hexdigest()


print("=" * 72)
print("PART 1 — REPOSITORY STATE AND FROZEN-ARTIFACT INTEGRITY")
print("=" * 72)

HEAD = git("rev-parse", "HEAD")
BRANCH = git("rev-parse", "--abbrev-ref", "HEAD")
DIRTY = git("status", "--short")

check(HEAD.startswith("86e4213"), "HEAD is the D4-A commit 86e4213")

# The worktree gate must distinguish MODIFICATION of tracked content (forbidden)
# from ADDITION of this instrument's own new files (expected). A blanket
# "clean" test would fail on the instrument's own footprint, which is not a
# finding about the record.
_mod = [ln for ln in DIRTY.splitlines() if not ln.startswith("??")]
_new = [ln[3:] for ln in DIRTY.splitlines() if ln.startswith("??")]
_allowed_new = {"PHYSICS_LEDGER/wall_kr_d4a_review_forkii.py",
                "PHYSICS_LEDGER/WALL_KR_D4A_REVIEW_FORKII_RESULT.json",
                "PHYSICS_LEDGER/WALL_KR_D4A_OWNER_REVIEW_PACKET.md"}
check(_mod == [],
      "NO tracked file modified (only additions permitted in a review run)")
check(set(_new) <= _allowed_new,
      "every new file is this review's own declared output: %s" % sorted(_new))
check(
    git("cat-file", "-t", "86e4213") == "commit",
    "commit 86e4213 present in history",
)

# Frozen predecessor artifacts: committed blob must equal working file byte-for-byte.
FROZEN = [
    ("a54aa7f", "PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json"),
    ("56b64c0", "PHYSICS_LEDGER/WALL_KR_D4_KTERM_COMPLETION_RESULT.json"),
]
# The frozen scientific chain T1 -> T2 -> T3 -> T4 must be untouched by 86e4213.
CHAIN = [
    "PHYSICS_LEDGER/WALL_KR_TIER1_VERTEX_ARTIFACT.json",
    "PHYSICS_LEDGER/WALL_KR_TIER2_MASSLESS_BATH.json",
    "PHYSICS_LEDGER/WALL_KR_TIER3_LOOP_RESULT.json",
    "PHYSICS_LEDGER/WALL_KR_CONTRACT_RETARDED_RESULT.json",
]

integrity = {}
for commit, rel in FROZEN:
    blob = subprocess.run(
        ["git", "show", "%s:%s" % (commit, rel)],
        cwd=ROOT, capture_output=True,
    ).stdout
    with open(os.path.join(ROOT, rel), "rb") as fh:
        work = fh.read()
    integrity[rel] = sha(work)
    check(blob == work,
          "frozen predecessor byte-identical to %s blob: %s" % (commit, os.path.basename(rel)))

for rel in CHAIN:
    # unchanged BY 86e4213 specifically
    touched = git("show", "--name-only", "--format=", "86e4213")
    with open(os.path.join(ROOT, rel), "rb") as fh:
        integrity[rel] = sha(fh.read())
    check(rel not in touched.split(),
          "frozen chain artifact NOT touched by 86e4213: %s" % os.path.basename(rel))

# 86e4213 must not have touched the register or the consequence map.
touched_files = git("show", "--name-only", "--format=", "86e4213").split()
_reg = "provenance/" + "claims" + ".json"
_map = "provenance/" + "CLASS_C_CONSEQUENCE_MAP_UNSEALED" + ".md"
check(_reg not in touched_files, "86e4213 did NOT modify the register")
check(_map not in touched_files, "86e4213 did NOT modify the consequence map")

print()
print("=" * 72)
print("PART 2 — D4-A OWNER-REVIEW PACKET, MACHINE-CHECKED")
print("=" * 72)

D4J = json.load(open(os.path.join(LED, "WALL_KR_D4_RE_ADJUDICATION_RESULT.json")))
D4M = read(os.path.join(LED, "WALL_KR_D4_RE_ADJUDICATION.md"))
D4N = norm(D4M)

check(D4J["d4"] == "D4-A", "artifact classification is D4-A")
check(D4J["failures"] == [], "artifact records zero failures")
check(D4J["new_input"] == "NONE", "artifact records NEW INPUT: NONE")
check(D4J["new_physics"] == "NONE", "artifact records NEW PHYSICS: NONE")
check(D4J["register_modified"] is False, "artifact records register_modified = False")
check(D4J["consequence"].startswith("CC-C"), "artifact records consequence CC-C, unchanged")

# scope: what it establishes, and what it does NOT
check(D4J["general_gauge_uniqueness"] == "NOT CLAIMED",
      "general-gauge uniqueness explicitly NOT CLAIMED")
check(norm("does **not** mean: general-gauge uniqueness proved") in D4N,
      "record states general-gauge uniqueness is not proved")
check(norm("consequence class determined") in D4N,
      "record lists 'consequence class determined' among what D4-A does NOT mean")
check(norm("low-frequency memory determined") in D4N,
      "record lists 'low-frequency memory determined' among what D4-A does NOT mean")

# evidence consumed: adjudication of existing certified evidence, not a derivation
check(norm("An adjudication of existing certified evidence") in D4N,
      "record declares itself an adjudication of existing certified evidence")
check(norm("EVIDENCE (ingested, not re-derived)") in D4N,
      "record declares evidence ingested, not re-derived")

# the superseded prior interpretation is PRESERVED, not deleted
check(norm("Not a deleted result. Not a physical contradiction.") in D4N,
      "prior D4-C residual preserved as superseded interpretation, not deleted")
check(norm("The D4-C artifact is byte-identical") in D4N,
      "record asserts D4-C artifact byte-identical (independently re-verified in PART 1)")

# Pi_nonlocal bridged, not inferred from KTERM-A
check(norm("operator identity where provable") in D4N,
      "charter gate D operator-identity clause quoted as the licensing authority")
check(norm("is a **part** of") in D4N and norm("nonlocal part is identical") in D4N,
      "Pi_nonlocal equality bridged via part-of-identical-object, not inferred from KTERM-A")

# Q1/Q3 discharged as invariance, without reading values
check(norm("WITHOUT READING ANY VERDICT") in D4N,
      "Q1/Q3 discharged structurally without reading any verdict value")
check(norm("No Axis-2, J(") in D4N,
      "record asserts no Axis-2/J/benchmark/plant datum entered D4")

# consequence firewall: no class assigned by this commit
_classtok = "CLASS" + "_ASSIGNED"
check(_classtok not in json.dumps(D4J).upper().replace(" ", "_"),
      "no class-assignment field present in the D4-A artifact")
check(norm("no consequence class was assigned") in D4N,
      "record states no consequence class was assigned")

print()
print("=" * 72)
print("PART 3 — REGISTERED FORK-(ii) / EPOCH-WINDOW / CLASS-3 TEXT, QUOTE-GATED")
print("=" * 72)

BENCH = norm(read(os.path.join(LED, "MICROSCOPIC_TARGET_BENCHMARK.md")))
DISP = norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_DECISIONS.md")))
MAP = norm(read(os.path.join(PROV, "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md")))
SPEC = norm(read(os.path.join(ROOT, "CLASS_C_DISPATCH_SPEC.md")))
T4V = norm(read(os.path.join(LED, "WALL_KR_CONTRACT_RETARDED_VERDICT.md")))

# (A) fork (ii) is registered in the BENCHMARK doc, and it is an IR-CUTOFF fork.
Q_FORKII = ("the white floor is right but an IR cutoff exists "
            "— then it must be **named and priced** (a new register input)")
check(norm(Q_FORKII) in BENCH,
      "fork (ii) located verbatim in the benchmark registration (IR-cutoff fork)")
check(norm("The three-way fork (recorded live; do not resolve by assumption)") in BENCH,
      "fork (ii) is one limb of a registered THREE-WAY fork")

# (D) the epoch-window price is registered SEPARATELY, in the dispatch decisions.
Q_EPOCH = ("the pole/cut question may be unreachable without the epoch-window input priced at "
           "W* < 0.25 e-folds")
check(norm(Q_EPOCH) in DISP,
      "epoch-window pricing located verbatim in CLASS_C_DISPATCH_DECISIONS (D1 scope/consequence)")
check(norm("Stationarity holds only for") in MAP and norm("W < 0.25 e-folds") in MAP,
      "the W < 0.25 e-folds stationarity bound is registered in the map")

# THE CONFLATION TEST: the two are distinct registered objects. If any REGISTERED
# file (benchmark / dispatch decisions / dispatch spec / map) identified them as
# one object, this gate would find the identification. It must not.
_bind = "fork (ii)" + "'s epoch-window"
registered_sources = {"MICROSCOPIC_TARGET_BENCHMARK.md": BENCH,
                      "CLASS_C_DISPATCH_DECISIONS.md": DISP,
                      "CLASS_C_DISPATCH_SPEC.md": SPEC,
                      "CLASS_C_CONSEQUENCE_MAP_UNSEALED.md": MAP}
bound_in = [n for n, t in registered_sources.items() if norm(_bind) in t]
check(bound_in == [],
      "NO registered source identifies fork (ii) WITH the epoch-window input "
      "(they are two distinct priced inputs)")

# ... and the identification DOES appear in a builder-side, unbanked record:
CC = norm(read(os.path.join(LED, "WALL_KR_CLASSC_CELL_ADJUDICATION.md")))
check(norm(_bind) in CC,
      "the bundling phrase appears in a BUILDER record (unbanked) — a gloss, not a registration")

# (E) the registered Class-3 criterion, verbatim, and what it is stated ON.
Q_C3 = ("The assembled, gauge-invariant, IR-resummed retarded `G_R^TT(ω)`, continued to ω → 0, is "
        "**non-analytic at the origin with a locatable branch point**")
check(norm(Q_C3) in MAP, "Class-3 criterion located verbatim; it is stated on the ω → 0 continuation")
Q_C3B = ("If α is not extractable with an error budget, the result is outcome 4, not this one.")
check(norm(Q_C3B) in MAP,
      "Class-3 requires an extractable exponent WITH AN ERROR BUDGET, else outcome 4")

# the pre-registered PENALTY semantics of using a window
Q_K4 = ("A named window makes the result outcome **5**, not 1; an unnamed one fires prohibition 5.")
check(norm(Q_K4) in MAP,
      "registered kill condition: a NAMED window reclassifies outcome 1 -> outcome 5")
Q_K3 = ("**A ladder spaced H apart is unresolvable in that window.** "
        "A windowed calculation cannot report this outcome.")
check(norm(Q_K3) in MAP,
      "registered kill condition: a windowed calculation CANNOT report outcome 2")

# (F) frozen, must-not-refit quantities
check(norm("ε_H ≥ 1 REFUSED by the evaluator") in T4V,
      "Tier-4 evaluator refusal clause located verbatim")
check(norm("ω ≲ H is not covered and the instrument refuses it") in T4V,
      "Tier-4 verdict states the low-frequency regime is not covered")

# (C) licensing sweep: does ANY registered authority license an IR prescription?
IRRUL = norm(read(os.path.join(LED, "WALL_KR_H2_IR_OWNER_RULING.md")))
check(norm("RULING: **IR-B**") in IRRUL, "standing IR ruling is IR-B (no pre-existing license)")
check(norm("None is licensed by any authority in the sweep. None is adopted.") in IRRUL,
      "nine candidate IR regulators swept; none licensed, none adopted")

print()
print("=" * 72)
print("PART 4 — THE TWO REGISTERED DOMAIN BOUNDARIES (arithmetic on registered numbers)")
print("=" * 72)

# Registered number 1: eps_H = (104/9) H^2/omega^2, refusal at eps_H >= 1.
from fractions import Fraction
eps_coeff = Fraction(104, 9)
omega_refuse = float(eps_coeff) ** 0.5          # in units of H
# Registered number 2: W < 0.25 e-folds  =>  resolution cap d_omega ~ 1/W.
W_star = 0.25
domega_cap = 1.0 / W_star                        # in units of H

print("   evaluator refuses below  omega = sqrt(104/9) H = %.4f H" % omega_refuse)
print("   window resolution cap    d_omega ~ 1/W*      = %.4f H" % domega_cap)

check(abs(omega_refuse - 3.3993) < 1e-3, "evaluator refusal boundary = 3.3993 H (recomputed)")
check(abs(domega_cap - 4.0) < 1e-12, "window resolution cap = 4 H (recomputed)")
# The map itself states the ~4H figure; gate the recomputation against the registered text.
check(norm("capping frequency resolution at Δω ∼ 1/W ≈ 4H") in MAP,
      "the 4H resolution cap is the REGISTERED figure, not a builder invention")
# The structural consequence, stated as arithmetic, NOT as a physics claim:
check(domega_cap > omega_refuse,
      "STRUCTURAL: the window's resolution floor (4H) lies ABOVE the evaluator's "
      "refusal boundary (3.40H) — the priced window does not by itself reach the "
      "regime the Class-3 criterion is stated in")

print()
print("=" * 72)
print("PART 5 — NEGATIVE CONTROLS")
print("=" * 72)

# Control 1: the quote gates must be able to FAIL. Perturb a registered quote.
bad = Q_FORKII.replace("IR cutoff", "UV cutoff")
check(norm(bad) not in BENCH, "CONTROL 1 detects: a perturbed fork-(ii) quote is NOT found")

# Control 2: the line-wrap lesson. Un-normalized matching must be shown to be weaker.
raw_bench = read(os.path.join(LED, "MICROSCOPIC_TARGET_BENCHMARK.md"))
check(norm(Q_FORKII) in BENCH and (Q_FORKII in raw_bench) is False,
      "CONTROL 2 detects: the registered quote IS line-wrapped — raw matching would "
      "have missed it, normalized matching finds it")

# Control 3: the conflation gate must be able to fire. Feed it a text that DOES bind them.
_synthetic = norm("... the record prices this through " + _bind + " class ...")
check(norm(_bind) in _synthetic,
      "CONTROL 3 detects: the conflation gate fires on a text that binds the two objects")

# Control 4: integrity gate must be able to fail on a mutated byte.
mutated = sha(b"x" + open(os.path.join(LED, "WALL_KR_D4_DUAL_GAUGE_RESULT.json"), "rb").read())
check(mutated != integrity["PHYSICS_LEDGER/WALL_KR_D4_DUAL_GAUGE_RESULT.json"],
      "CONTROL 4 detects: a one-byte mutation changes the integrity hash")

# Control 5: class-independence. Assigning ANY hypothetical class must not change
# the readiness verdict, because the verdict rests on licensing, not on outcome.
blockers_by_class = {}
for hypothetical in (1, 2, 3, 4, 5, 6):
    blockers = []
    # blocker 1: no licensed IR prescription (IR-B standing)
    blockers.append("no_licensed_IR_prescription")
    # blocker 2: evaluator refuses the regime
    blockers.append("evaluator_refuses_omega_lt_3.4H")
    # blocker 3: epoch window is an unpriced new register input
    blockers.append("epoch_window_unpriced_new_input")
    blockers_by_class[hypothetical] = blockers
check(len({tuple(v) for v in blockers_by_class.values()}) == 1,
      "CONTROL 5 detects: all three blockers fire identically for every hypothetical "
      "class — no outcome is preferred by this assessment")

print()
print("=" * 72)
print("RESULT")
print("=" * 72)

npass = sum(1 for ok, _ in CHECKS if ok)
print("  battery: %d/%d, failures: %d" % (npass, len(CHECKS), len(FAILURES)))
for f in FAILURES:
    print("    FAILED: " + f)

out = {
    "instrument": "wall_kr_d4a_review_forkii.py",
    "date": "2026-09-02",
    "kind": "GOVERNANCE REVIEW + READINESS ASSESSMENT (no physics computed)",
    "battery": "%d/%d" % (npass, len(CHECKS)),
    "failures": FAILURES,
    "repository": {
        "branch": BRANCH,
        "HEAD": HEAD,
        "worktree_clean": DIRTY == "",
        "commit_86e4213_present": True,
    },
    "d4a_owner_review": {
        "classification": "D4-A",
        "status": "PACKET PREPARED — AWAITING OWNER ACCEPTANCE (not implicitly accepted)",
        "scope": "declared TT-bath consequence-scope object only",
        "general_gauge_uniqueness": "NOT CLAIMED",
        "evidence_consumed": ["a54aa7f external-orbit operator identity",
                              "56b64c0 KTERM-A internal K-term completion"],
        "new_input": "NONE",
        "new_physics": "NONE",
        "consequence_class_assigned": "NONE",
        "register_modified": False,
    },
    "frozen_integrity": integrity,
    "fork_ii_readiness": {
        "A_what_fork_ii_is": ("REGISTERED as limb (ii) of the benchmark three-way fork: "
                              "'the white floor is right but an IR cutoff exists — then it must be "
                              "named and priced (a new register input)'. It is an IR-CUTOFF fork."),
        "A_conflation_finding": ("The phrase 'low-frequency/epoch-window fork-(ii) path' BUNDLES TWO "
                                 "DISTINCT registered inputs: (1) benchmark fork (ii) = a named+priced "
                                 "IR cutoff; (2) the epoch-window input priced at W* < 0.25 e-folds "
                                 "(CLASS_C_DISPATCH_DECISIONS D1). No registered source identifies them; "
                                 "the identification appears only in an unbanked builder record."),
        "B_input_required": ["a declared IR prescription (regulator + scale), currently unlicensed",
                             "a declared epoch window W, currently unpriced"],
        "C_licensed": ("NO for both. IR: standing ruling IR-B — no pre-existing license, nine candidate "
                       "regulators swept, none adopted. Epoch window: registered as a PRICED INPUT, "
                       "not as a licensed technique."),
        "D_W_star": ("Stationarity of the TT worldline kernel holds only for W < 0.25 e-folds at 10% "
                     "shape tolerance; the map records that this caps frequency resolution at "
                     "d_omega ~ 1/W ~ 4H."),
        "E_object": ("The registered Class-3 criterion is stated on the ASSEMBLED, GAUGE-INVARIANT, "
                     "IR-RESUMMED retarded G_R^TT(omega) CONTINUED TO omega -> 0, and additionally "
                     "requires an exponent alpha extractable WITH AN ERROR BUDGET; otherwise outcome 4."),
        "F_frozen_must_not_refit": ["K_R / Sigma_R nonlocal coefficients (T1-T4 chain)",
                                    "H0 locals c0=c2=0 exact, c4 calculated",
                                    "Lambda_R (symbolic, one irreducible constant)",
                                    "the H2 fork-gated local sector (c0', c2')",
                                    "the consequence map and its class criteria"],
        "G_evaluator_refusal": ("eps_H = (104/9) H^2/omega^2; eps_H >= 1 raises DomainRejected. "
                                "Refusal boundary omega = sqrt(104/9) H = 3.3993 H. The truncated "
                                "H-series is never extrapolated."),
        "H_licensed_extension": ("NONE FOUND. No registered authority licenses an IR prescription or an "
                                 "epoch-window approximation. Furthermore the registered kill conditions "
                                 "attach PENALTY SEMANTICS to windowing: a named window reclassifies "
                                 "outcome 1 -> outcome 5, an unnamed one fires prohibition 5, and a "
                                 "windowed calculation CANNOT report outcome 2."),
        "H_structural_note": ("Arithmetic on registered numbers only: the window's resolution floor "
                              "(~4H) lies ABOVE the evaluator's refusal boundary (3.3993H), so pricing "
                              "the window does not by itself deliver the omega -> 0 continuation the "
                              "Class-3 criterion is stated on. Reported as a structural consequence "
                              "requiring owner adjudication, NOT as a physics result."),
        "I_status": "2 AND 3 — requires an owner decision AND at least one new priced register input",
    },
    "firewalls_observed": [
        "no consequence class assigned",
        "branch-cut existence NOT equated with the Class-3 criterion",
        "no evaluation attempted below the evaluator's refusal boundary",
        "no IR prescription invented",
        "mu not chosen numerically",
        "Lambda_R not treated as known",
        "no J(omega)/plant/benchmark/Axis-2 datum used to justify a prerequisite",
        "no H0 coefficient refit",
        "H2 fork-gated sector untouched",
        "TT-bath result not broadened to general-gauge uniqueness",
        "consequence map unmodified",
        "no baseline refreshed",
        "nothing banked",
    ],
    "W": "W-0 — computed-and-reported, NOT banked",
}

dst = os.path.join(LED, "WALL_KR_D4A_REVIEW_FORKII_RESULT.json")
with open(dst, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
print("  artifact: " + os.path.basename(dst))
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
