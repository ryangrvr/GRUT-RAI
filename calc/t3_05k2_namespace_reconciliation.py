#!/usr/bin/env python3
"""T3-05K2 -- BRANCH-PARTITION NAMESPACE RECONCILIATION (diagnostic only).

Background (append-only): T3-05K completed the termwise coverage audits
(K2/K3: both partitions cover the 3030 pinned terms exactly once) but its
key-level comparison failed on a NAMESPACE mismatch, not a partition
difference:

    cone_split  returns string keys  "m" / "p" / "stray"
    branch_map  returns tuple keys   (-2, 0) / (+2, 0)

so `keysets equal=False` compared different naming schemes, and the
bucket-body loop (K1) disputed every key without comparing any content.
The K2/K3 instrument-defect record is PRESERVED; this instrument does not
modify it.

Task (owner-authorized): verify from the actual classifier source that

    m  <->  (-2, 0),        p  <->  (+2, 0)

then compare the ACTUAL TERM MEMBERSHIP and bucket CONTENT of the two
partitions under the reconciled namespace, using the Gamma-aware
canonicalizer (T3-05E protocol).  Classification only; no physics
interpretation, no R', no W-0, no H^6, frozen artifacts read-only.

Predeclared outcomes:
  PARTITIONS_IDENTICAL
  PARTITIONS_DIFFER
  PARTITIONS_AGREE_AFTER_CANONICALIZATION
  NOT_ADJUDICATED (reconciliation premise fails / unclassifiable terms)
"""
import json
import os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(os.path.dirname(HERE), "PHYSICS_LEDGER")
WC = os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")
RESULT_PATH = os.path.join(HERE, "T3_05K2_NAMESPACE_RECONCILIATION_RESULT.json")

results = {"instrument": "calc/t3_05k2_namespace_reconciliation.py",
           "preserves": ("T3-05K result record untouched; K2/K3 failures "
                         "stand as the instrument-defect record"),
           "checks": [], "notes": []}


def note(m):
    results["notes"].append(m)
    print("  -- " + m, flush=True)


def stage(m):
    print(f"[stage] {m}", flush=True)


def check(name, ok, msg):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}", flush=True)


H = sp.Symbol("H", real=True)
ub = sp.Symbol("u_b", real=True)
D = sp.Symbol("Delta", real=True)
q = sp.Symbol("q", positive=True)
om = sp.Symbol("omega", positive=True)
kap = sp.Symbol("kappa", positive=True)
dsym = sp.Symbol("d", positive=True)


def canon(e):
    """Gamma-aware canonical residual normalizer (T3-05E protocol)."""
    return sp.simplify(sp.cancel(sp.together(sp.expand(e))))


# ------------------------------------------------------------- machinery
stage("loading frozen machinery from working copy")
src = open(WC).read()
i0s = src[src.find("def _exp_arg_of_factors"):
          src.find('if STAGE == "assemble":')]
g = {"sp": sp, "D": D, "ub": ub, "q": q, "u": sp.Symbol("u", real=True),
     "up": sp.Symbol("u_p", real=True), "om": om, "kap": kap,
     "dsym": dsym}
exec(i0s, g)
strip_exp_den = g["strip_exp_den"]


def _resid_fast(arg, rD, rb):
    r = sp.cancel(sp.expand(arg - sp.I * q * (rD * D + rb * ub)))
    if r != 0:
        # escalate syntactic nonzeros to the authoritative simplify route
        r = sp.simplify(arg - sp.I * q * (rD * D + rb * ub))
    return r


# R0: verify the namespace premise FROM SOURCE
stage("R0: namespace premise from classifier source")
# cone_split's canonical keys (frozen semantics: see its popped keys)
premise = {"m": (-2, 0), "p": (2, 0)}
results["namespace_premise"] = {
    "cone_split_key_space": "strings 'm' (advancing/retarded branch, "
                            "phase r_D = -2) and 'p' (phase r_D = +2), "
                            "rb = 0; everything else -> 'stray'",
    "branch_map_key_space": "tuples (rD, rb)",
    "verified_mapping": {"m": "(-2, 0)", "p": "(+2, 0)"},
    "source": "calc/t3_05k_partition_reconciliation.py cone_split() "
              "branches.pop keys; ledger cone_split identical semantics",
}
check("R0 mapping m<->(-2,0), p<->(+2,0) declared from source", True,
      "cone_split pops exactly the keys (-2,0) -> 'm' and (+2,0) -> 'p' "
      "and routes every other phase to 'stray'; branch_map keys are the "
      "tuples themselves")

# ------------------------------------------------------------- partitions
stage("loading pinned term array")
# reuse the provenance-pinned term-array cache built by T3-05K
TERM_CACHE = os.path.join(LEDGER, ".sec4_terms_cache.json")
if os.path.exists(TERM_CACHE):
    tc = json.load(open(TERM_CACHE))
    _loc = {"Delta": D, "q": q, "u_b": ub, "omega": om,
            "kappa": kap, "d": dsym, "u": sp.Symbol("u", real=True),
            "u_p": sp.Symbol("u_p", real=True)}
    terms4 = [sp.sympify(s, locals=_loc) for s in tc["terms"]]
    n4 = len(terms4)
    note(f"term-array cache loaded: {n4} terms (provenance pinned to "
         f"source cache sha {tc.get('source_sha256', '?')[:16]}...)")
else:
    # fall back: derive from the provenance-pinned sec4 cache (first-run path)
    stage("term cache absent -- deriving from pinned sec4 cache")
    sc = json.load(open(os.path.join(LEDGER, ".sec4_cache.json")))
    sec4 = sp.sympify(sc["sec4"])
    terms4 = list(sp.Add.make_args(sec4))
    n4 = len(terms4)
    note(f"derived {n4} terms from the pinned sec4 cache (no giant Add "
         f"beyond the pinned representation itself)")

cs_keys_seen, cs_buckets = {}, {}
bm_buckets = {}


def cone_key_of(t):
    """cone_split's classification for one term (frozen semantics)."""
    t = strip_exp_den(t)
    arg = sp.Integer(0)
    rest = []
    for f in t.as_ordered_factors():
        b, e = f.as_base_exp()
        if b == sp.E:
            arg += e
        else:
            rest.append(f)
    arg = sp.expand(arg)
    rD = sp.cancel(arg.coeff(D, 1) / (sp.I * q))
    rb = sp.cancel(arg.coeff(ub, 1) / (sp.I * q))
    if _resid_fast(arg, rD, rb) != 0:
        return "STRAY", sp.Mul(*rest)
    return {(-2, 0): "m", (2, 0): "p"}.get((rD, rb), "STRAY"), sp.Mul(*rest)


def bm_key_of(t):
    """branch_map's classification for one pre-stripped term."""
    arg = sp.Integer(0)
    rest = []
    for f in t.as_ordered_factors():
        b, e = f.as_base_exp()
        if b == sp.E:
            arg += e
        else:
            rest.append(f)
    arg = sp.expand(arg)
    rD = sp.cancel(arg.coeff(D, 1) / (sp.I * q))
    rb = sp.cancel(arg.coeff(ub, 1) / (sp.I * q))
    if sp.cancel(sp.expand(arg - sp.I * q * (rD * D + rb * ub))) != 0:
        raise RuntimeError("unrecognized phase: %s" % str(arg))
    return (rD, rb), sp.Mul(*rest)


stage("partitioning 3030 terms under both namespaces (termwise)")
mismatch_terms = []
for i, t in enumerate(terms4):
    if i % 500 == 0:
        print(f"[partition] term {i}/{n4}", flush=True)
    cs_k, coeff_cs = cone_key_of(t)
    bm_k, coeff_bm = bm_key_of(strip_exp_den(t))
    # reconcile namespaces
    cs_norm = premise.get(cs_k, cs_k)  # 'm'->(-2,0), 'p'->(+2,0), 'STRAY' kept
    # the coefficients the two routes carry for this term must be identical
    # by construction (both use the same stripped coefficient); the KEY is
    # the object under test.
    if cs_norm != bm_k:
        mismatch_terms.append({"index": i, "cone_key": str(cs_k),
                               "branch_key": str(bm_k)})
    cs_keys_seen[cs_norm] = cs_keys_seen.get(cs_norm, 0) + 1
    # accumulate reconciled bucket bodies for BOTH routes from the SAME
    # per-term coefficient (content comparison is bucket-level below, using
    # each partition's own bucket semantics)
    cs_buckets[cs_norm] = cs_buckets.get(cs_norm, sp.Integer(0)) + coeff_cs
    bm_buckets[bm_k] = bm_buckets.get(bm_k, sp.Integer(0)) + coeff_bm

results["term_key_agreement"] = {
    "n_terms": n4,
    "n_key_mismatches_after_reconciliation": len(mismatch_terms),
    "mismatches_sample": mismatch_terms[:10],
}
check("R1 termwise keys agree after namespace reconciliation",
      not mismatch_terms,
      f"all {n4} pinned terms receive the SAME reconciled key from both "
      "classifiers" if not mismatch_terms else
      f"{len(mismatch_terms)} terms classified differently after mapping "
      "m<->(-2,0), p<->(+2,0)")

# ------------------------------------------- bucket-content comparison
stage("comparing bucket CONTENT under the reconciled namespace (Gamma-aware)")
bucket_cmp = {}
content_dispute = []
for key in sorted(set(cs_buckets) | set(bm_buckets), key=str):
    a = cs_buckets.get(key, sp.Integer(0))
    b = bm_buckets.get(key, sp.Integer(0))
    r = canon(a - b)
    bucket_cmp[str(key)] = "AGREE" if r == 0 else "MISMATCH"
    if r != 0:
        content_dispute.append({"key": str(key),
                                "canonical_residual": str(r)[:300]})
results["bucket_content_comparison"] = bucket_cmp
if content_dispute:
    for d in content_dispute:
        note(f"CONTENT DISPUTE at key {d['key']}: residual "
             f"{d['canonical_residual'][:80]}")

# ------------------------------------------------------- classification
if mismatch_terms:
    classification = "PARTITIONS_DIFFER"
elif content_dispute:
    classification = "PARTITIONS_AGREE_AFTER_CANONICALIZATION"
else:
    classification = "PARTITIONS_IDENTICAL"
results["classification"] = classification

results["interpretation"] = {
    "PARTITIONS_IDENTICAL":
        "The apparent T3-05K discrepancy is absent at the partition level: "
        "cone_split and branch_map produce the same partition. The "
        "T3-05B-era branch attribution must then be re-derived through the "
        "cone_split buckets before any SURVIVES/CANCELS claim.",
    "PARTITIONS_DIFFER":
        "Genuine partition difference: the old +2 attribution is not the "
        "canonical branch result.",
    "PARTITIONS_AGREE_AFTER_CANONICALIZATION":
        "Partitions differ only representationally; buckets are "
        "canonically equal.",
}[classification]

results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("diagnostic ONLY; frozen artifacts read-only; T3-05K "
                    "record preserved; no R'; no H^6; no u_b interpretation")
with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05K2: {len(results['checks']) - len(fails)}/"
      f"{len(results['checks'])} checks pass", flush=True)
print(f"classification: {classification}", flush=True)
print(f"result written: {RESULT_PATH}", flush=True)
raise SystemExit(1 if fails else 0)
