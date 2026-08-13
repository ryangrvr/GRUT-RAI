#!/usr/bin/env python3
"""u5u6_deformability: the one in-house computation that settles the SCALING-LEVEL STRUCTURE of both
u5's class count and u6's order-parameter-reality, by FACTORING the deformability question -- at the
scaling level we can honestly reach (it graduates NEITHER claim; the horn itself stays undecided).

CLAIM (default-BROKEN): the u5 surviving sector (relativistic, passive, KMS, causal viscoelastic
transport) is labeled by the reversible mode-coupling / Poisson-bracket structure (u6's candidate
order parameter, the rel. E/F/G/H/J analogs). Whether that partition is SHARP (distinct fixed points
=> real order parameter + phase structure) or DEFORMABLE (couplings RG-irrelevant => collapse => one
rigid class + info_i2-adjacent) is the deformability question. This toy shows the question factors
into TWO knobs and reduces to a sharp, physical input.

  KNOB 1 -- DEFORMABILITY (RG-relevance at the relativistic z=1 fixed point). SYMMETRY-PROTECTION is
    decidable: a bracket forced by a conservation law the vacuum HAS is present and cannot be tuned to
    zero. RG-RELEVANCE (does the present coupling DISTINGUISH a fixed point, or flow away?) is the
    fixed-point computation -- NOT decided here. TOY/SCALING points the direction; it does not resolve.
  KNOB 2 -- AVAILABILITY (conserved-charge content). A reversible bracket {phi, Q} exists only if Q is
    a conserved charge of the vacuum. T_mu_nu is universal (=> the Model-H advective bracket is always
    present AND symmetry-forced). Every OTHER bracket (J, E/F, G) needs an EXTRA conserved charge the
    pure gravitational vacuum may or may not carry. So, GIVEN sharp, the class count is a MONOTONE
    function of charge content (schematically ~1 per unlocked bracket): only T_mu_nu -> 1 (rigid);
    extra charges -> a family (phase structure).

RESULT (scaling level): the deformability question FACTORS, and (given sharp) its class-count leg
REDUCES to 'how many conserved charges beyond T_mu_nu does the responsive vacuum carry?'. This is a
FACTORIZATION of the u5/u6 deformability question at the scaling level -- it graduates NEITHER claim,
and the horn itself (KNOB 1, sharp-vs-deformable) stays UNDECIDED.

FENCES (both directions):
  - TOY/SCALING: symmetry + naive scaling only; NOT the rigorous fixed-point (anomalous-dimension) RG,
    which is the research computation. Points the direction; does not resolve. On every claim.
  - The conserved-charge content is a FENCED MODELING INPUT (rung3-channel-shaped): does GRUT's vacuum
    carry a charge beyond T_mu_nu (a conformalon current? an anomaly current?) is NOT settled here.
  - Both horns FIRST-CLASS: sharp => order parameter + phase structure; deformable => collapse + rigid.
  - 'only T_mu_nu => rigid' is a LEAN conditioned on TWO fenced inputs (the charge content AND
    'sharp'), NOT a banked result.
  - Does NOT graduate u5 or u6 (both stay to-derive, ledger 0).

Refs: Hohenberg-Halperin 1977 (the A-J dynamic classes); Forster 1975 (reversible Poisson-bracket
mode coupling). Pure stdlib. Strictly v5 register.
"""

# --------------------------------------------------------------------------------------------------
# (A) The reversible mode-coupling brackets of the surviving sector (rel. E/F/G/H/J analogs).
#     Each is {OP, conserved generator}; the generator is either T_mu_nu (universal) or an extra charge.
#     E and F share one U(1) bracket (HH convention), so four bracket entries cover the five labels.
#     Scope: 'T_mu_nu universal' is the flat-space / fixed-background EFT sense the HH mode-coupling
#     dictionary assumes -- T^{0i} generates translations (a covariant T_mu_nu gives an integral charge
#     only with a Killing vector / asymptotic symmetry).
# --------------------------------------------------------------------------------------------------

T_MUNU = "T_mu_nu"

BRACKETS = [
    {
        "name": "H",
        "op": "conserved scalar density (e.g. energy/number)",
        "generator": "T^{0i} (momentum density)",
        "generator_is_Tmunu": True,
        "requires_charge": T_MUNU,
        "note": "OP advected by conserved momentum -- the T_mu_nu/stress-tensor analog; symmetry-forced.",
    },
    {
        "name": "J",
        "op": "non-abelian conserved current (OP is its own generator)",
        "generator": "{S^a,S^b}=eps^abc S^c (self-precession)",
        "generator_is_Tmunu": False,
        "requires_charge": "non-abelian internal charge (e.g. SU(2))",
        "note": "needs an extra non-abelian conserved charge with the OP in its algebra.",
    },
    {
        "name": "E/F",
        "op": "complex scalar charged under a conserved U(1)",
        "generator": "conserved U(1) charge density",
        "generator_is_Tmunu": False,
        "requires_charge": "U(1) internal charge",
        "note": "needs an extra conserved U(1) the OP is charged under.",
    },
    {
        "name": "G",
        "op": "staggered OP + conserved magnetization",
        "generator": "internal charge + sublattice (staggered) structure",
        "generator_is_Tmunu": False,
        "requires_charge": "internal charge + staggered structure",
        "note": "needs extra internal + sublattice structure.",
    },
]


# --------------------------------------------------------------------------------------------------
# (B) RG relevance / deformability. Symmetry-protection is DECIDABLE; fixed-point relevance is NOT.
# --------------------------------------------------------------------------------------------------

def protection_status(bracket):
    """DECIDABLE part: is the bracket forced-present by a conservation law the vacuum universally has?
    Returns the symmetry-protection status. RG-relevance (sharp vs deformable) at the z=1 fixed point
    is a SEPARATE, fenced fixed-point question -- see relevance_is_fenced()."""
    if bracket["generator_is_Tmunu"]:
        return "symmetry-FORCED-present (T_mu_nu conservation + Lorentz; cannot be tuned to zero)"
    return "conditional -- present ONLY IF the vacuum carries: " + bracket["requires_charge"]


def relevance_is_fenced():
    """The honest scaling-level statement about RG-relevance under RELATIVISTIC (z=1) dynamic scaling.

    z=1 (space and time scale identically) is guaranteed only IF the critical dynamics flows to a
    Lorentz-INVARIANT fixed point; in a thermal / dissipative (KMS) medium boosts are broken (a thermal
    state picks a rest frame), so z=1 here is a FIXED-POINT ASSUMPTION, not a symmetry theorem. Under
    z=1 the non-relativistic Hohenberg-Halperin upper-critical-dimension logic (which works by letting
    the mode coupling DRIVE z away from its van Hove value) does NOT transfer directly. A present
    reversible coupling is then either (i) RG-IRRELEVANT at the z=1 fixed point -> it does not
    distinguish a class -> DEFORMABLE / collapse to the pure dissipative class (u6 order parameter
    collapses; info_i2-adjacent), or (ii) RG-RELEVANT / marginal -> a DISTINCT fixed point -> SHARP.

    Which one holds is set by the ANOMALOUS dimension at the interacting fixed point -- a loop / epsilon-
    expansion computation. Naive engineering power counting does NOT decide it. THIS TOY DOES NOT RESOLVE
    KNOB 1; it establishes only that the H-bracket is symmetry-PRESENT (a necessary condition for a sharp
    H-class) and reduces the COUNT (knob 2) to a clean charge-counting question below."""
    return ("UNDECIDED at scaling level (z=1 is a fixed-point assumption in a KMS medium; the fixed-"
            "point anomalous dimension is the decider = research calc). Protection gives PRESENCE, not "
            "relevance.")


# --------------------------------------------------------------------------------------------------
# (C) Availability = conserved-charge content. The clean, decidable computable core.
# --------------------------------------------------------------------------------------------------

def available_brackets(charges):
    """Which reversible brackets are AVAILABLE given the vacuum's conserved charges (a set of labels).
    T_mu_nu is universal (H always available); every other bracket needs its extra charge present."""
    charges = set(charges) | {T_MUNU}  # T_mu_nu is always present
    avail = []
    for b in BRACKETS:
        if b["generator_is_Tmunu"] or b["requires_charge"] in charges:
            avail.append(b)
    return avail


def class_count(charges, sharp):
    """The u5 class count as a function of (charge content, deformability horn).
      sharp=True  (KNOB 1 = relevant): each AVAILABLE bracket = a distinct sharp class.
      sharp=False (KNOB 1 = irrelevant): all reversible couplings flow away -> ONE dissipative class."""
    if not sharp:
        return 1  # DEFORMABLE horn: collapse to the single pure-dissipative class (rigid, u6 collapses)
    return len(available_brackets(charges))  # SHARP horn: count = number of available brackets


# --------------------------------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------------------------------

def part_A():
    print("\n" + "=" * 94)
    print("PART A -- the reversible mode-coupling brackets of the surviving sector (rel. E/F/G/H/J)")
    print("=" * 94)
    print(" bracket  order parameter                              generator                 charge needed")
    print(" " + "-" * 92)
    for b in BRACKETS:
        need = "T_mu_nu (universal)" if b["generator_is_Tmunu"] else b["requires_charge"]
        print(" %-7s  %-42s %-24s %s" % (b["name"], b["op"][:42], b["generator"][:24], need))


def part_B():
    print("\n" + "=" * 94)
    print("PART B -- deformability = RG-relevance (KNOB 1). Symmetry-protection DECIDABLE; relevance NOT.")
    print("=" * 94)
    for b in BRACKETS:
        print("  %-5s : %s" % (b["name"], protection_status(b)))
    print("\n  RG-RELEVANCE at the relativistic z=1 fixed point:")
    print("   " + relevance_is_fenced())
    print("  => KNOB 1 is a fixed-point (anomalous-dimension) computation. TOY/SCALING does NOT resolve")
    print("     it; it fixes only that the H-bracket is PRESENT (symmetry-forced), a necessary condition")
    print("     for a sharp H-class.")


def part_C():
    print("\n" + "=" * 94)
    print("PART C -- availability = conserved-charge content (KNOB 2). The clean, decidable core.")
    print("=" * 94)
    scenarios = [
        ("pure gravity", set()),                              # only T_mu_nu
        ("+ U(1)", {"U(1) internal charge"}),
        ("+ non-abelian SU(2)", {"non-abelian internal charge (e.g. SU(2))"}),
        ("+ U(1) + SU(2) + staggered", {"U(1) internal charge",
                                        "non-abelian internal charge (e.g. SU(2))",
                                        "internal charge + staggered structure"}),
    ]
    print("  vacuum charge content        available brackets        count (SHARP)   count (DEFORMABLE)")
    print("  " + "-" * 88)
    for label, extra in scenarios:
        avail = [b["name"] for b in available_brackets(extra)]
        print("  %-27s %-24s %-15d %d"
              % (label, "{" + ",".join(avail) + "}", class_count(extra, True), class_count(extra, False)))
    print("\n  => GIVEN sharp, the u5 COUNT is a monotone function of the conserved-charge content.")
    print("     Pure gravity (only T_mu_nu) -> count 1 (only the forced H-bracket) -> RIGID.")
    print("     Extra charges -> count > 1 -> PHASE STRUCTURE (a family). And note: for pure gravity")
    print("     BOTH horns give count 1 -- the sharp/deformable split there is whether the ONE class")
    print("     carries a real (single-valued) order parameter or a collapsed one.")


def part_D():
    print("\n" + "=" * 94)
    print("PART D -- both-horn read (default-BROKEN; neither banked)")
    print("=" * 94)
    print("  DEFORMABLE horn (KNOB 1 = irrelevant): reversible couplings flow away -> one pure-")
    print("    dissipative class -> u5 RIGID, u6 order parameter COLLAPSES (info_i2-adjacent). First-class.")
    print("  SHARP horn (KNOB 1 = relevant/protected): available brackets = distinct classes -> the u5")
    print("    count = f(charge content) [KNOB 2]; u6 order parameter is REAL. Sub-split by KNOB 2:")
    print("      only T_mu_nu   -> count 1 -> RIGID (order parameter real but single-valued);")
    print("      extra charges  -> count > 1 -> PHASE STRUCTURE (a family, labeled by charge content).")
    print("  THE REDUCTION (the finding): the deformability question factors as KNOB1 x KNOB2 and the")
    print("    u5 COUNT reduces to 'how many conserved charges beyond T_mu_nu does the vacuum carry?'.")
    print("  LEAN (held loosely; NOT banked): T_mu_nu is the only guaranteed current, so IF the vacuum")
    print("    carries only T_mu_nu AND the H-bracket is sharp, the count is 1 -> rigid. BOTH the 'only")
    print("    T_mu_nu' charge content AND 'sharp' are FENCED INPUTS the toy does not settle.")


def main():
    print("=" * 94)
    print("u5/u6 DEFORMABILITY -- one calc, both claims (default-BROKEN, TOY/SCALING; graduates NEITHER)")
    print("=" * 94)
    part_A()
    part_B()
    part_C()
    part_D()

    print("\n" + "=" * 94)
    print("VERDICT (default-BROKEN, honest; TOY/SCALING; does NOT graduate u5 or u6):")
    print("=" * 94)
    print("  DERIVED (scaling level) -- the FACTORIZATION only (graduates NEITHER u5 nor u6; horn")
    print("  UNDECIDED): the deformability question FACTORS into two knobs --")
    print("   KNOB 1 (RG-relevance / sharp-vs-deformable): UNDECIDED at scaling level (fixed-point calc);")
    print("     the H-bracket is symmetry-FORCED-present, a necessary condition for a sharp H-class.")
    print("   KNOB 2 (charge content): DECIDABLE -- given sharp, the u5 count is a MONOTONE function of")
    print("     charge content (schematically ~1 per unlocked bracket; some classes need combined")
    print("     structure, and one charge can seed several). So the count REDUCES to 'how many conserved")
    print("     charges beyond T_mu_nu?'.")
    print("  => u5/u6's scaling-level STRUCTURE settled TOGETHER (neither graduated): sharp+extra-charges")
    print("     => real order parameter + phase structure; deformable => collapse + rigid; sharp+only-")
    print("     T_mu_nu => real but single-valued order parameter + rigid.")
    print("  FENCES: TOY/SCALING (symmetry + naive scaling, NOT the fixed-point RG -- points the")
    print("   direction, does not resolve KNOB 1); the charge content is a FENCED modeling input (a")
    print("   SECOND rung3-shaped input, distinct from u6's already-held coarse-graining/slow-variable")
    print("   conditional, which stays live); both horns first-class; 'only T_mu_nu => rigid' is a LEAN")
    print("   conditioned on TWO inputs (charge content AND 'sharp'), not a result; u5/u6 stay to-derive.")

    ok = _selftest()
    print("\n  SELFTEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


# --------------------------------------------------------------------------------------------------
# Test -- verify the availability / count logic (the decidable core) and the both-horn structure.
# --------------------------------------------------------------------------------------------------

def _selftest():
    ok = True
    U1 = "U(1) internal charge"
    SU2 = "non-abelian internal charge (e.g. SU(2))"

    # (1) pure gravity (only T_mu_nu) -> only the H-bracket available.
    avail = [b["name"] for b in available_brackets(set())]
    if avail != ["H"]:
        print("   [FAIL] pure gravity available != {H}:", avail); ok = False

    # (2) extra charges unlock exactly their brackets; H always present.
    if "E/F" not in [b["name"] for b in available_brackets({U1})]:
        print("   [FAIL] U(1) does not unlock E/F"); ok = False
    if "J" not in [b["name"] for b in available_brackets({SU2})]:
        print("   [FAIL] SU(2) does not unlock J"); ok = False
    if "H" not in [b["name"] for b in available_brackets({U1, SU2})]:
        print("   [FAIL] H not universally present"); ok = False

    # (3) availability is monotone in charge content (sharp count non-decreasing as charges added).
    seq = [set(), {U1}, {U1, SU2}]
    counts = [class_count(c, True) for c in seq]
    if not all(counts[i] <= counts[i + 1] for i in range(len(counts) - 1)):
        print("   [FAIL] sharp count not monotone in charges:", counts); ok = False

    # (4) pure gravity gives count 1 in BOTH horns (the key structural fact).
    if class_count(set(), True) != 1 or class_count(set(), False) != 1:
        print("   [FAIL] pure gravity count != 1 in both horns"); ok = False

    # (5) phase structure (count > 1) requires BOTH sharp AND extra charges.
    if class_count({U1}, False) != 1:
        print("   [FAIL] deformable horn should collapse to 1 even with extra charges"); ok = False
    if class_count({U1}, True) <= 1:
        print("   [FAIL] sharp + extra charge should give a family (>1)"); ok = False

    # (6) deformable horn always collapses to 1 regardless of charge content.
    if any(class_count(c, False) != 1 for c in [set(), {U1}, {U1, SU2}]):
        print("   [FAIL] deformable horn not always 1"); ok = False

    return ok


if __name__ == "__main__":
    raise SystemExit(main())
