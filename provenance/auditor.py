#!/usr/bin/env python3
"""GRUT provenance auditor -- the generalized discipline engine (the AI seed).

Extracted from validate.py so the SAME tiering / anti-laundering discipline can audit an
ARBITRARY claim set, not only GRUT's ladder. The GRUT-specific gate (validate.py) is now a
thin wrapper around audit() in this module. Nothing here hardcodes GRUT: pass any (claims,
source_ids) pair and, optionally, your own tier vocabulary.

WHAT THIS VERIFIES: discipline, NOT truth.  It checks that every claim is
  - TIERED        -- tier is in the allowed vocabulary;
  - SOURCED       -- has sources[], and every source id resolves in the supplied register;
  - FALSIFIABLE   -- carries an overturning_computation (something that could kill it);
  - NOT LAUNDERED -- no net-positive ledger_delta sold as 'shown'/'derived'/'derived-pending'
                     without an explicit laundering_ok flag; 'assumed'+positive only WARNS
                     (a recovery-with-imports, legal but must be labeled a recovery).

WHAT THIS DOES NOT DO -- and cannot:  it does not certify PHYSICAL CORRECTNESS. A claim that
is wrong-but-well-provenanced passes GREEN. The ledger is a BLIND SUM of ledger_delta: the
engine cannot detect a physics error, and it cannot detect a double-count (e.g. one input
booked as +1 on two different claims). Provenance is not proof. See RESULTS_auditor.md.

Pure Python stdlib; no third-party deps.
"""

# The standard tiering vocabulary. Callers may override valid_tiers for a non-GRUT claim set.
DEFAULT_TIERS = {"shown", "derived", "derived-pending", "assumed", "to-derive"}

# Tiers that assert a derivation/result: a net-positive ledger_delta here is LAUNDERING
# (a derivation that quietly expands the input list) unless laundering_ok=true is declared.
LAUNDERABLE_TIERS = frozenset({"shown", "derived", "derived-pending"})


class AuditResult:
    """Aggregated outcome of auditing a claim set. Carries no I/O -- callers print/exit."""

    def __init__(self):
        self.blocking = []          # list[str]: violations that must FAIL the gate
        self.warnings = []          # list[str]: non-blocking (recovery-with-imports)
        self.net = 0                # int: blind sum of ledger_delta across the set
        self.rows = []              # list[(tier, id, delta, flagged_stance)] for display

    @property
    def ok(self):
        return not self.blocking


def audit_claim(claim, source_ids, valid_tiers=DEFAULT_TIERS):
    """Apply the discipline to ONE claim.

    claim: dict with keys id, tier, sources, overturning_computation, ledger_delta,
           and optionally laundering_ok.
    source_ids: a collection of known source ids (the register's keys).
    valid_tiers: the allowed tier vocabulary.

    Returns (blocking: list[str], warnings: list[str], delta: int, flagged_stance: bool).
    Does not print, does not raise on a bad claim -- it REPORTS, so the caller decides.
    """
    cid = claim.get("id", "<no-id>")
    tier = claim.get("tier")
    srcs = claim.get("sources", [])
    delta = claim.get("ledger_delta")
    laundering_ok = claim.get("laundering_ok", False)

    blocking, warnings = [], []

    # tiered
    if tier not in valid_tiers:
        blocking.append(f"{cid}: invalid tier {tier!r}")
    # sourced
    if not srcs:
        blocking.append(f"{cid}: NO sources[] (unprovenanced claim)")
    for s in srcs:
        if s not in source_ids:
            blocking.append(f"{cid}: source {s!r} not in register")
    # falsifiable
    if not claim.get("overturning_computation"):
        blocking.append(f"{cid}: NO overturning_computation (nothing could kill it)")
    # ledger integer (reject bool explicitly: isinstance(True, int) is True in Python,
    # so a JSON `true` would otherwise be silently miscounted as +1 in the blind net sum)
    if not isinstance(delta, int) or isinstance(delta, bool):
        blocking.append(f"{cid}: ledger_delta must be int, got {delta!r}")
        delta = 0

    # 1b (2026-08-09, external-review close-out): a waiver must COST something. laundering_ok
    # waives the launderability block for +8 of the register's +13; a self-granted exemption with
    # no stated stance is exactly the shape the review flagged. The justification is not verified
    # for TRUTH (this engine verifies discipline) -- it is required to EXIST, so the waiver is a
    # declared stance rather than a silent flag.
    if laundering_ok and not str(claim.get("stance_justification") or "").strip():
        blocking.append(
            f"{cid}: laundering_ok WITHOUT stance_justification -- a waiver that costs nothing "
            f"is a self-granted exemption; state WHY carrying +delta at this tier is a declared "
            f"stance rather than laundering")

    # not laundered
    if isinstance(delta, int) and delta > 0:
        if tier in LAUNDERABLE_TIERS and not laundering_ok:
            blocking.append(
                f"{cid}: LAUNDERING - tier '{tier}' but ledger_delta=+{delta} "
                f"(a derivation that expands the input list)"
            )
        elif tier == "assumed":
            warnings.append(
                f"{cid}: recovery-with-imports (tier assumed, +{delta}) - "
                f"must be labeled a RECOVERY, not a derivation"
            )

    flagged_stance = isinstance(delta, int) and delta > 0 and laundering_ok
    return blocking, warnings, delta, flagged_stance


def audit(claims, source_ids, valid_tiers=DEFAULT_TIERS):
    """Apply the discipline to a WHOLE claim set (any (claims, sources) pair).

    Returns an AuditResult. Pure: no printing, no sys.exit -- the gate wrapper handles those.
    """
    source_ids = set(source_ids)
    res = AuditResult()
    for c in claims:
        blocking, warnings, delta, flagged = audit_claim(c, source_ids, valid_tiers)
        res.blocking.extend(blocking)
        res.warnings.extend(warnings)
        res.net += delta
        res.rows.append((c.get("tier"), c.get("id", "<no-id>"), delta, flagged))
    return res
