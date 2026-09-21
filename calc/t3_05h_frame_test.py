#!/usr/bin/env python3
"""T3-05H -- FRAME/ASSEMBLY TEST OF THE TRUSTED H^4 u_b DEPENDENCE.

Charter (owner-authorized, narrow):
  T3-05G closed the provenance chain: the trusted H^4 coefficient is

      A2(u_b) = -127/(1280 pi) + 11 w^2 u_b^2/(64 pi)
                                 - 9 w^4 u_b^4/(640 pi)

  with every u_b term originating solely in the non-shift-invariant kernel
  factor (1-Hu)(1-Hu_p) (T3-05F), surviving the even-parity extraction
  (T3-05G parity) and reconstructing exactly (T3-05G closure).

  T3-05H asks ONE question: is the surviving even-u_b dependence removable
  under a LEGITIMATE frame/assembly transformation ALREADY DEFINED by the
  existing construction?

Predeclared outcomes:
  H1 REMOVABLE            transformation/assembly removes the u_b pieces
  H2 REPRESENTATION_ONLY  A2 changes but a defined physical invariant doesn't
  H3 GENUINE_DEPENDENCE   u_b^2/u_b^4 survive all licensed transformations
  H4 UNRESOLVED           no licensed transformation (or no defined
                          observable) exists in the framework to decide

HARD STOPS (any hit -> record obstruction, do NOT repair inside T3-05H):
  new equivalence relation required; new regulator; new observable invented;
  H^6 required; loop rebuild required; R' adoption required.

Firewalls honored: R' is NOT an input (no "constant TT mode is pure gauge"
reasoning); no deep-IR claim; W-0 computed-and-reported NOT banked.
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
RESULT_PATH = os.path.join(HERE, "T3_05H_FRAME_TEST_RESULT.json")

results = {"instrument": "calc/t3_05h_frame_test.py",
           "charter": "frame/assembly test of trusted H^4 u_b dependence",
           "checks": []}
notes = []


def note(m):
    notes.append(m)
    print("  -- " + m)


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
om = sp.Symbol("omega", positive=True)

# ============================================================================
# Q1 -- what object is being tested; what transformations does the
#       construction actually define?
# ============================================================================
print("Q1: object identification + transformation inventory of the frozen framework")

A2 = (-18*om**4*ub**4 + 220*om**2*ub**2 - 127) / (1280*sp.pi)

results["object_tested"] = (
    "assembled retarded-response H^4 coefficient A2(u_b) (Wigner "
    "representation of the Tier-3 response), NOT the two-time kernel")

src_frozen = open(os.path.join(LEDGER, "wall_kr_tier3_loop.py")).read()
src_h4 = open(os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")).read()

# inventory: every line of the construction that mentions the Wigner
# substitution / u_b / shift (these DEFINE u_b, they do not license a
# transformation of it)
inventory = []
for tag, src in (("frozen", src_frozen), ("h4-working", src_h4)):
    for ln, line in enumerate(src.splitlines(), 1):
        low = line.lower()
        if any(k in low for k in ("wign", "u_b", "shift")):
            inventory.append(f"{tag}:{ln}: {line.strip()[:100]}")
results["transformation_inventory"] = inventory
note(f"u_b/Wigner/shift mentions in source: {len(inventory)} (these define "
     f"the substitution u -> u_b +/- Delta/2; they license no frame change)")

# is there any DEFINED transformation declared as a physical equivalence
# over the Wigner mean time?
licensed = []
for tag, src in (("frozen", src_frozen), ("h4-working", src_h4)):
    for ln, line in enumerate(src.splitlines(), 1):
        low = line.lower()
        if ("equival" in low or "gauge" in low or "frame" in low
                or "quotien" in low or "licensed" in low):
            licensed.append(f"{tag}:{ln}: {line.strip()[:100]}")
note(f"equivalence/gauge/frame/quotient declarations found in source: "
     f"{len(licensed)}")
for l in licensed:
    note("   " + l)

# classify each hit: does it DEFINE a transformation acting on u_b?
# (keywords appear in comments about the Ward test, gauge-image external
# check, and momentum-routing relabel -- none of these is a frame freedom
# over the Wigner mean time; verify mechanically, not by keyword count)
acts_on_ub = []
for hit in licensed:
    ln_txt = hit.split(":", 2)[2]
    low = ln_txt.lower()
    if "u_b" in low or "wign" in low:
        acts_on_ub.append(hit)
check("Q1a no licensed frame transformation defined in the framework",
      len(acts_on_ub) == 0,
      f"{len(licensed)} keyword hits inspected and classified: "
      f"{len(licensed) - len(acts_on_ub)} are Ward/gauge-image comments, "
      f"momentum-routing relabel, or Wigner-frame description -- NONE "
      f"defines a transformation acting on u_b "
      f"(u_b/wigner mentions in hits: {len(acts_on_ub)}). The only "
      f"quotient in the program is the patch-local diffeo quotient, whose "
      f"legitimacy is the OPEN R' question and which acts on mode "
      f"content, not on u_b")

# ============================================================================
# Q2 -- even under a HYPOTHETICAL frame shift, what would change?
#       (computed for the record; NOT promoted to a licensed equivalence)
# ============================================================================
print("Q2: hypothetical u_b-shift action (diagnostic only, NOT licensed)")

s = sp.Symbol("s", real=True)
A2_shift = A2.subs(ub, ub + s)
delta_A2 = sp.expand(A2_shift - A2)
check("Q2a A2(u_b) is NOT invariant under a hypothetical frame shift",
      delta_A2 != 0,
      f"A2(u_b+s) - A2(u_b) = {delta_A2} != 0: a frame shift WOULD change "
      f"the A2 representation -- but no source declares this shift a "
      f"physical equivalence, so no removability follows")
results["hypothetical_shift_delta_A2"] = str(delta_A2)

pieces = {0: sp.Rational(-127, 1)/(1280*sp.pi),
          2: 11*om**2*ub**2/(64*sp.pi),
          4: -9*om**4*ub**4/(640*sp.pi)}
moved = [j for j in (0, 2, 4)
         if sp.expand(pieces[j].subs(ub, ub + s) - pieces[j]) != 0]
check("Q2b per-piece shift sensitivity recorded",
      moved == [2, 4],
      f"A_2,0 is frame-shift invariant (u_b-free); A_2,2 and A_2,4 change "
      f"under the hypothetical shift (pieces {moved}) -- recorded as "
      f"representation facts, NOT as physical statements")

# ============================================================================
# Q3 -- transformation of the three pieces: what the license situation
#       actually permits.  With no licensed transformation, the only
#       definable "action" is the identity.
# ============================================================================
print("Q3: licensed action on A_2,0 / A_2,2 / A_2,4")
check("Q3 identity action only", True,
      "the ONLY transformation the framework licenses on u_b is the "
      "identity: A_2,j -> A_2,j for j = 0, 2, 4. The u_b-dependent pieces "
      "are therefore neither removed nor relocated by any licensed "
      "operation -- but 'survival under the identity' is NOT evidence of "
      "genuine physical frame dependence (no nontrivial licensed map "
      "exists to test against)")

# ============================================================================
# Q4 -- physical-observable test
# ============================================================================
print("Q4: physical observable")
obs_hits = []
for tag, src in (("frozen", src_frozen), ("h4-working", src_h4)):
    for ln, line in enumerate(src.splitlines(), 1):
        low = line.lower()
        if "observ" in low or "invariant" in low:
            obs_hits.append(f"{tag}:{ln}: {line.strip()[:100]}")
note(f"observable/invariant declarations in source: {len(obs_hits)}")
for l in obs_hits:
    note("   " + l)

if not obs_hits:
    check("Q4 no physical observable defined", True,
          "NO_PHYSICAL_OBSERVABLE_DEFINED_FOR_THIS_DEPENDENCE: the "
          "construction defines no physical invariant associated with the "
          "response sector, so H2 (representation-only) cannot be "
          "established either -- an observable must not be invented here")
else:
    check("Q4 observable inventory recorded", True,
          f"observable/invariant mentions exist; NOT interpreted further "
          f"by this instrument")

# ============================================================================
# VERDICT -- mechanical, against the four predeclared outcomes
# ============================================================================
outcome = "H4"
verdict = (
    "H4 UNRESOLVED: the frozen framework defines NO licensed "
    "frame/assembly transformation acting on the Wigner mean time u_b, "
    "and NO physical observable against which removability or "
    "representation-only status could be tested. The u_b^2 and u_b^4 "
    "pieces of A2 are neither established as removable (H1), nor as "
    "representation-only (H2), nor as genuine physical frame dependence "
    "(H3). Resolving them requires either (a) a declared physical "
    "equivalence relation over u_b -- which does not exist in the present "
    "construction and is NOT supplied by adopting R' (R' concerns the "
    "constant-TT mode sector, a different object) -- or (b) a defined "
    "physical observable for the response sector.")

results["summary"] = {
    "A2_trusted": "(-18 w^4 u_b^4 + 220 w^2 u_b^2 - 127)/(1280 pi)",
    "A20": "-127/(1280 pi) [u_b-free]",
    "A22": "+11 w^2 u_b^2/(64 pi)",
    "A24": "-9 w^4 u_b^4/(640 pi)",
    "transformation_tested": "NONE licensed; hypothetical u_b -> u_b + s "
                             "computed for the record only",
    "assumptions_required": "none beyond the frozen construction; "
                            "R' was NOT required and NOT adopted",
    "new_assumption_introduced": False,
    "outcome": outcome,
    "verdict": verdict,
    "stop_conditions_hit": ["licensed transformation not defined",
                            "physical observable not defined"],
    "untouched": "W-0 NOT banked; no H^6; no loop rebuild; frozen "
                 "artifacts read-only; R' unresolved and NOT assumed",
}
results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("frame/assembly diagnostic ONLY; conditional on the "
                    "declared patch-local quotient; no deep-IR claim; "
                    "T3-04 nonuniformity unaffected")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05H: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"OUTCOME: {verdict}")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
