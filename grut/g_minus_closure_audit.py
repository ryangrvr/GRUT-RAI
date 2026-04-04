"""GRUT g_- Closure Status Audit.

This module resolves the open question left by Appendix K
(metric_closure_program.py): whether the pre-projection g_- (doubled-metric)
sector of Route B (Galley) can act as a Component B analogue and supply the
missing 1/r² support for a static interior metric with f(R_eq) >= 0.

BACKGROUND
----------
route_b_component_b.py established:
  - Post-projection Route B = Route C (1/r^4, insufficient)
  - Phi_- scalar sector: ghost-kinetic, 1/r^4, Component B ruled out
  - g_- (doubled-metric): energy density NOT computed in closed form;
    "1/r^2 cannot be ruled out"  (Result C — key unresolved channel)

This audit resolves the g_- open door through a structural source argument,
with explicit conditional statements about the three assumptions required.

THE CLOSURE ARGUMENT
--------------------
The g_- field equation in the Galley doubled formalism is driven by:

  L[g_-] = T^Phi_1_munu - T^Phi_2_munu   (stress-energy difference)

At GRUT static equilibrium (Phi_1 = Phi_2 = Phi_eq, Phi_dot = 0):

  T^Phi_1_munu = T^Phi_2_munu  =>  source = 0

IF g_- = 0 then its contribution to the effective stress-energy entering the
g_+ Einstein equation is zero, and no Component B can arise.

However, the inference  "source = 0 => g_- = 0"  requires three explicit
conditions that are NOT all established:

  Condition 1 — Static boundary conditions:
    Phi_1 and Phi_2 satisfy the same equilibrium BCs.
    Status: TRUE under GRUT equilibrium assumption.

  Condition 2 — Absence of homogeneous g_- solutions:
    L[g_-] = 0 must have no growing solutions.  The wrong-sign EH action
    is expected UNSTABLE (route_b_component_b.py), so homogeneous modes
    of L[g_-] = 0 may exist and grow from initial perturbations.
    Status: UNKNOWN — not established either way.

  Condition 3 — Galley projection assumption:
    The physical limit g_- -> 0 at late times is a consistent truncation.
    Known NOT to be an attractor (galley_truncation.py); it is assumed, not derived.
    Status: TRUE under Galley formalism assumption.

Because Condition 2 is UNKNOWN, the inference is conditional:

  - Source-driven path (g_- forced by T^Phi_1 - T^Phi_2): CLOSED.
    Under conditions 1+3 (which hold), the source vanishes => g_- = 0 on this path.

  - Homogeneous path (g_- driven by initial conditions / unstable modes):
    OPEN.  Cannot be ruled out without establishing stability of L[g_-] = 0.

RESULT CLASSIFICATION
---------------------
  source_path_closed  = True
  homogeneous_path_open = True
  universal_no_go = False

  verdict: "static_source_vanishes_under_galley_projection__
            g_minus_zero_not_guaranteed_due_to_homogeneous_modes__
            component_b_implausible_not_impossible"

This is a CONDITIONAL PARTIAL CLOSURE:
  Stronger than "unresolved" (source path is closed; the gap is
    now precisely characterised as the homogeneous sector).
  Weaker than a universal no-go (homogeneous modes unresolved).

DYNAMIC CASE
------------
When Phi_dot != 0, T^Phi_1 - T^Phi_2 is nonzero and g_- is actively sourced.
However:
  - The dynamic Killing horizon (f = 0 at A >= A_crit) is fully explained
    by kinetic Component A alone (interior_metric_closure.py / Appendix J, locked).
  - Any g_- correction is first-order in g_-, subleading relative to the
    dominant A_crit kinetic term.
  - Dynamic g_- does not open a new static closure path.

Phi_- SCALAR SECTOR (CONFIRMATION)
-----------------------------------
Already established in route_b_component_b.py (Result B):
  T^Phi_-_munu at physical limit = ghost copy of T^Phi_+_munu
  Kinetic sign = -1 (ghost), radial power = 4 (1/r^4), provides_component_b = False.
Confirmed here for completeness; no new analysis.

NONCLAIMS
---------
1. This module does NOT compute the g_- energy density in closed form.
   The closure is at the source level, not the Green's function level.
2. This module does NOT rule out Component B from homogeneous g_- solutions.
3. This module does NOT apply to non-Galley CTP formalisms.
4. The source-path closure is conditional on Phi_1 = Phi_2 = Phi_eq
   (GRUT static equilibrium assumption).
5. universal_no_go = False: the architecture search is not closed by this audit.

SELF-CONTAINED: imports constants from metric_closure_program; no other grut/ imports.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import List, Dict, Any

from grut.metric_closure_program import (
    M_EXT, R_EQ, TAU_SQ, A_CRIT,
    F_STATIC, M_STATIC,
)


# ================================================================
# Canonical constants (re-derived for self-documentation)
# ================================================================

RHO_EQ_AT_R_EQ = -M_EXT ** 2 / (2.0 * TAU_SQ * R_EQ ** 4)
"""Static equilibrium energy density at R_eq.
rho_eq = -M^2 / (2 tau^2 r^4).  Same value for both fields at equilibrium.
"""


# ================================================================
# Verdict vocabulary
# ================================================================

VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN = (
    "static_source_vanishes_under_galley_projection__"
    "g_minus_zero_not_guaranteed_due_to_homogeneous_modes__"
    "component_b_implausible_not_impossible"
)

VERDICT_FULLY_CLOSED = (
    "static_g_minus_fully_closed__source_zero_homogeneous_absent__"
    "no_component_b_from_g_minus"
)

VERDICT_SOURCE_NONZERO = (
    "static_g_minus_source_nonzero__"
    "component_b_not_ruled_out__requires_explicit_computation"
)

FORBIDDEN_CLAIMS = [
    "universal_no_go_for_g_minus",         # homogeneous path open
    "g_minus_energy_density_computed",      # not computed here
    "non_galley_ctp_closed",               # only Galley assessed
    "component_b_impossible_from_g_minus", # homogeneous modes could contribute
    "search_exhaustively_closed",           # catalog statement only
    "appendix_c_blockers_overridden",
]


# ================================================================
# Data structures
# ================================================================

@dataclass
class ClosureConditions:
    """The three conditions required for the full inference source=0 => g_-=0.

    All three must hold for the source-path closure to be watertight.
    Condition 2 is UNKNOWN, preventing a full guarantee.
    """
    # Condition 1: both fields use the same static equilibrium BC
    condition_1_static_bc: bool = False
    condition_1_status: str = ""
    condition_1_notes: str = ""

    # Condition 2: no homogeneous g_- solutions (L[g_-]=0 has no growing modes)
    condition_2_no_homogeneous: bool = False   # UNKNOWN — stored as False
    condition_2_status: str = ""               # "unknown"
    condition_2_notes: str = ""

    # Condition 3: Galley physical-limit projection (g_- -> 0) is assumed
    condition_3_galley_projection: bool = False
    condition_3_status: str = ""
    condition_3_notes: str = ""

    # Aggregate: all three must hold for guaranteed g_- = 0
    all_conditions_met: bool = False           # computed: False (condition_2 unknown)

    notes: List[str] = field(default_factory=list)


@dataclass
class GMinusStaticSourceTest:
    """Test of the g_- source at static GRUT equilibrium.

    At static equilibrium Phi_1 = Phi_2 = Phi_eq =>
    T^Phi_1_munu = T^Phi_2_munu => source = 0 (under condition 1).
    """
    rho_eq_field1: float = 0.0        # T^Phi_00 field 1 at R_eq
    rho_eq_field2: float = 0.0        # T^Phi_00 field 2 at R_eq (same)
    source_difference: float = 0.0    # field1 - field2 (exact 0.0)
    source_vanishes: bool = False      # True if |difference| < tol

    # Implications (conditional on ClosureConditions)
    g_minus_zero_guaranteed: bool = False     # False: condition 2 unknown
    g_minus_zero_under_projection: bool = False  # True: under conditions 1+3

    # Component B verdict for each path
    source_driven_component_b: bool = False   # False: source path closed
    homogeneous_component_b: str = ""         # "undetermined": homogeneous open

    notes: List[str] = field(default_factory=list)


@dataclass
class GMinusDynamicAssessment:
    """Assessment of the dynamic (Phi_dot != 0) g_- sector.

    When Phi_dot != 0 the g_- source T^Phi_1 - T^Phi_2 is nonzero.
    But the A_crit dynamic Killing horizon is already fully explained
    by kinetic Component A alone (Appendix J, locked). g_- is subleading.
    """
    a_crit_scenario_closes: bool = False   # True: locked from interior_metric_closure.py
    a_crit_value: float = 0.0             # 1.062
    g_minus_correction_order: str = ""    # "first_order_in_g_minus"
    g_minus_subsumed: bool = False        # True: dynamic closure already explained
    opens_new_static_path: bool = False   # False: dynamic ≠ static mechanism
    notes: List[str] = field(default_factory=list)


@dataclass
class ScalarPhiMinusAssessment:
    """Confirmation of the Phi_- scalar sector verdict from route_b_component_b.py.

    Already established as Result B.  Confirmed here for completeness.
    """
    kinetic_sign: int = 0          # -1 (wrong-sign, ghost)
    radial_power: int = 0          # 4 (1/r^4; same as T^Phi_+)
    provides_component_b: bool = True   # False
    energy_density_scaling: str = ""    # "1_over_r4_ghost"
    source_reference: str = ""         # "route_b_component_b.py Result B"
    notes: List[str] = field(default_factory=list)


@dataclass
class GMinusClosureResult:
    """Master result of the g_- closure status audit."""
    valid: bool = False

    conditions: ClosureConditions = field(default_factory=ClosureConditions)
    static_test: GMinusStaticSourceTest = field(default_factory=GMinusStaticSourceTest)
    dynamic_assessment: GMinusDynamicAssessment = field(
        default_factory=GMinusDynamicAssessment
    )
    phi_minus_assessment: ScalarPhiMinusAssessment = field(
        default_factory=ScalarPhiMinusAssessment
    )

    # Computed summary booleans
    source_path_closed: bool = False      # True: source-driven g_- = 0 under projection
    homogeneous_path_open: bool = False   # True: homogeneous modes unresolved
    universal_no_go: bool = False         # Always False: nonclaim

    verdict: str = ""                     # computed from above booleans
    nonclaims: List[str] = field(default_factory=list)
    forbidden_claims: List[str] = field(default_factory=list)
    diagnostics: Dict[str, Any] = field(default_factory=dict)


# ================================================================
# Section A — Closure conditions
# ================================================================

def build_closure_conditions() -> ClosureConditions:
    """Assess the three conditions required for source=0 => g_-=0.

    Returns
    -------
    ClosureConditions
        Explicit status for each condition.
    """
    # Condition 1: static boundary conditions
    c1 = True
    c1_status = "satisfied"
    c1_notes = (
        "At GRUT static equilibrium, both fields satisfy the same equation "
        "tau*Phi_dot + Phi = X = M/r^2 with Phi_dot = 0. "
        "The unique static solution Phi_eq = M/r^2 applies to both fields. "
        "T^Phi_1_munu = T^Phi_2_munu = T^Phi_eq_munu."
    )

    # Condition 2: absence of homogeneous g_- solutions
    # The wrong-sign EH action L_EH[g_-] has wrong-sign kinetic energy.
    # This makes the homogeneous equation L[g_-] = 0 expected UNSTABLE.
    # route_b_component_b.py: g_- = 0 is "expected UNSTABLE from wrong-sign EH action".
    # galley_truncation.py: g_- = 0 is NOT an attractor.
    # => homogeneous modes likely exist and grow.
    # Status: LIKELY_FALSE — the wrong-sign EH is expected unstable, so growing
    # homogeneous modes are anticipated.  Stored False (pessimistic bool) with
    # status string carrying the detail.  NOT simply "unknown" — there is positive
    # evidence of instability from the wrong-sign kinetic structure.
    c2 = False   # pessimistic: condition NOT verified; growing modes expected
    c2_status = "likely_false__wrong_sign_EH_expected_unstable"
    c2_notes = (
        "The linearized g_- equation L[g_-] = source has a homogeneous sector "
        "L[g_-] = 0. The wrong-sign Einstein-Hilbert action makes this equation "
        "EXPECTED UNSTABLE: homogeneous solutions likely exist and grow. "
        "route_b_component_b.py: g_- = 0 is 'expected UNSTABLE from wrong-sign EH action'. "
        "galley_truncation.py: the projection g_- = 0 is NOT an attractor. "
        "This condition is stored as False (pessimistic) because the available evidence "
        "suggests homogeneous modes exist — not merely that their absence is unverified. "
        "Status 'likely_false__wrong_sign_EH_expected_unstable' carries this nuance."
    )

    # Condition 3: Galley projection assumption
    c3 = True
    c3_status = "assumed"
    c3_notes = (
        "The Galley formalism assumes the physical limit projection Phi_- -> 0, "
        "g_- -> 0 is a consistent truncation of the doubled system. "
        "This is the standard Galley assumption. "
        "It is a structural assumption of the formalism, not a derived result. "
        "Under this assumption, g_- = 0 is enforced at the level of the formalism "
        "independently of the source structure."
    )

    # Aggregate: ALL conditions must hold for guaranteed g_- = 0
    # Since condition 2 is unknown (stored as False), all_conditions_met = False
    all_met = c1 and c2 and c3   # = False

    notes = [
        f"Condition 1 (static BC):         {c1_status} — {c1}",
        f"Condition 2 (no homogeneous):    {c2_status} — stored as {c2} (likely_false / pessimistic)",
        f"Condition 3 (Galley projection): {c3_status} — {c3}",
        f"all_conditions_met = {all_met}  "
        f"(False because condition 2 is unknown)",
        "Source-path closure: holds under conditions 1+3 (both satisfied/assumed).",
        "Homogeneous-path: open — condition 2 cannot be established.",
    ]

    return ClosureConditions(
        condition_1_static_bc=c1,
        condition_1_status=c1_status,
        condition_1_notes=c1_notes,
        condition_2_no_homogeneous=c2,
        condition_2_status=c2_status,
        condition_2_notes=c2_notes,
        condition_3_galley_projection=c3,
        condition_3_status=c3_status,
        condition_3_notes=c3_notes,
        all_conditions_met=all_met,
        notes=notes,
    )


# ================================================================
# Section B — Static source test
# ================================================================

def run_static_source_test(conditions: ClosureConditions) -> GMinusStaticSourceTest:
    """Compute T^Phi at static equilibrium for both doubled fields.

    At equilibrium Phi_1 = Phi_2 = Phi_eq = M/r^2:
      rho_eq = -M^2 / (2 tau^2 r^4)  at r = R_eq
      T^Phi_1_00 = T^Phi_2_00 = rho_eq (same)
      source_difference = T^Phi_1 - T^Phi_2 = 0 (exact)

    Implications depend on the three conditions:
      - g_minus_zero_guaranteed: requires ALL conditions (False, cond.2 unknown)
      - g_minus_zero_under_projection: requires conditions 1+3 (True)
      - source_driven_component_b: False (source path closed)
      - homogeneous_component_b: "undetermined" (homogeneous path open)
    """
    tol = 1e-14

    rho1 = RHO_EQ_AT_R_EQ
    rho2 = RHO_EQ_AT_R_EQ   # same: Phi_1 = Phi_2 = Phi_eq at equilibrium
    diff = rho1 - rho2       # exactly 0.0 (floating point)

    source_vanishes = abs(diff) < tol

    # g_- = 0 guaranteed only if all three conditions hold
    g_minus_zero_guaranteed = conditions.all_conditions_met   # False

    # g_- = 0 under Galley projection (conditions 1+3 hold)
    g_minus_zero_under_projection = (
        conditions.condition_1_static_bc
        and conditions.condition_3_galley_projection
        and source_vanishes
    )

    # Source-driven Component B: False (source = 0, no driving force)
    source_driven_component_b = not source_vanishes   # False

    # Homogeneous path: open whenever condition_2_no_homogeneous is False.
    # "undetermined" = not closed regardless of whether instability is merely
    # suspected ("likely_false") or unknown — the homogeneous spectrum is
    # not computed either way.
    if conditions.condition_2_no_homogeneous:
        homogeneous_component_b = "ruled_out"
    else:
        homogeneous_component_b = "undetermined"

    notes = [
        f"rho_eq at R_eq = {rho1:.6e}  (same for both fields)",
        f"source_difference = {diff:.2e}  (exact zero: Phi_1 = Phi_2 = Phi_eq)",
        f"source_vanishes = {source_vanishes}",
        f"g_minus_zero_guaranteed = {g_minus_zero_guaranteed}  "
        f"(False: condition 2 unknown)",
        f"g_minus_zero_under_projection = {g_minus_zero_under_projection}  "
        f"(True: conditions 1+3 hold)",
        f"source_driven_component_b = {source_driven_component_b}  (source path closed)",
        f"homogeneous_component_b = {homogeneous_component_b}  "
        f"(condition 2 status: {conditions.condition_2_status})",
        "Physical interpretation: the source-driven path to Component B is closed.",
        "The homogeneous path remains open: if unstable modes of L[g_-]=0 exist,",
        "g_- could be nonzero even with zero source.  Whether such modes provide",
        "1/r^2 support requires computing the g_- homogeneous spectrum — not done here.",
    ]

    return GMinusStaticSourceTest(
        rho_eq_field1=rho1,
        rho_eq_field2=rho2,
        source_difference=diff,
        source_vanishes=source_vanishes,
        g_minus_zero_guaranteed=g_minus_zero_guaranteed,
        g_minus_zero_under_projection=g_minus_zero_under_projection,
        source_driven_component_b=source_driven_component_b,
        homogeneous_component_b=homogeneous_component_b,
        notes=notes,
    )


# ================================================================
# Section C — Dynamic assessment
# ================================================================

def assess_dynamic_g_minus() -> GMinusDynamicAssessment:
    """Assess whether the dynamic g_- sector opens a new static closure path.

    When Phi_dot != 0 (A > 0), the source T^Phi_1 - T^Phi_2 is nonzero
    and g_- is actively driven.  But:

    1. The A_crit dynamic Killing horizon (f = 0) is already fully explained
       by kinetic Component A alone (interior_metric_closure.py / Appendix J).
    2. The g_- correction enters at first order in g_-, subleading relative
       to the dominant kinetic cancellation.
    3. The dynamic g_- sector does not open a new STATIC closure path:
       any g_- sourced by dynamic Phi_dot is itself time-dependent, not static.
    """
    notes = [
        f"A_crit = {A_CRIT}: kinetic Component A achieves f=0 transiently (Appendix J, locked).",
        "Dynamic regime: T^Phi_1 - T^Phi_2 nonzero when Phi_dot != 0.",
        "g_- is sourced dynamically; its contribution enters at first order in g_-.",
        "The A_crit scenario closes f=0 WITHOUT requiring g_- contribution.",
        "g_- correction is subleading (first order in g_-, small relative to A_crit effect).",
        "Dynamic g_- does NOT open a new static closure path:",
        "  - any sourced g_- is time-dependent (driven by Phi_dot != 0)",
        "  - static Component B requires a time-independent 1/r^2 source",
        "  - dynamic g_- ≠ static Component B.",
    ]

    return GMinusDynamicAssessment(
        a_crit_scenario_closes=True,
        a_crit_value=A_CRIT,
        g_minus_correction_order="first_order_in_g_minus",
        g_minus_subsumed=True,
        opens_new_static_path=False,
        notes=notes,
    )


# ================================================================
# Section D — Phi_- confirmation
# ================================================================

def assess_phi_minus() -> ScalarPhiMinusAssessment:
    """Confirm the Phi_- scalar sector verdict from route_b_component_b.py.

    Already established as Result B in route_b_component_b.py.
    No new computation: ghost-kinetic, 1/r^4, provides_component_b = False.
    """
    notes = [
        "Established in route_b_component_b.py Result B.",
        "T^Phi_-_munu at physical limit = -T^Phi_+_munu (ghost copy, wrong sign).",
        "Kinetic sign = -1 (wrong-sign kinetic energy, ghost mode).",
        "Radial power = 4: energy density ~ 1/r^4 (Component A profile).",
        "provides_component_b = False: 1/r^4 is Component A, not Component B (1/r^2).",
        "Spatial profile is IC-dependent (not sourced by geometric X = M/r^2).",
        "No new analysis needed; confirmed here for completeness.",
    ]

    return ScalarPhiMinusAssessment(
        kinetic_sign=-1,
        radial_power=4,
        provides_component_b=False,
        energy_density_scaling="1_over_r4_ghost",
        source_reference="route_b_component_b.py Result B",
        notes=notes,
    )


# ================================================================
# Section E — Verdict assignment
# ================================================================

def assign_closure_verdict(
    static_test: GMinusStaticSourceTest,
    conditions: ClosureConditions,
) -> tuple[str, bool, bool]:
    """Compute verdict string and summary booleans from test outcomes.

    Returns
    -------
    (verdict, source_path_closed, homogeneous_path_open)
    """
    # Source path: closed if source vanishes and conditions 1+3 hold
    source_path_closed = (
        static_test.source_vanishes
        and static_test.g_minus_zero_under_projection
        and not static_test.source_driven_component_b
    )

    # Homogeneous path: open whenever condition_2_no_homogeneous is False
    # (condition 2 is either "unknown" or "likely_false" — in both cases open)
    homogeneous_path_open = not conditions.condition_2_no_homogeneous

    # Assign verdict string from computed booleans
    if source_path_closed and not homogeneous_path_open:
        verdict = VERDICT_FULLY_CLOSED
    elif source_path_closed and homogeneous_path_open:
        verdict = VERDICT_SOURCE_CLOSED_HOMOGENEOUS_OPEN
    else:
        verdict = VERDICT_SOURCE_NONZERO

    return verdict, source_path_closed, homogeneous_path_open


# ================================================================
# Master audit
# ================================================================

def run_g_minus_closure_audit() -> GMinusClosureResult:
    """Run the complete g_- closure status audit.

    Returns
    -------
    GMinusClosureResult
        Conditional partial closure verdict, computed from explicit tests.
    """
    conditions = build_closure_conditions()
    static_test = run_static_source_test(conditions)
    dynamic = assess_dynamic_g_minus()
    phi_minus = assess_phi_minus()

    verdict, source_path_closed, homogeneous_path_open = assign_closure_verdict(
        static_test, conditions
    )

    nonclaims = [
        "This module does NOT compute the g_- energy density in closed form.",
        "The closure is at the source level only (T^Phi_1 - T^Phi_2 = 0 at eq.).",
        "Component B from homogeneous g_- solutions is NOT ruled out.",
        "This module does NOT apply to non-Galley CTP formalisms.",
        "The source-path closure is conditional on Phi_1 = Phi_2 = Phi_eq (GRUT static eq.).",
        "universal_no_go = False: the Component B search is not exhaustively closed.",
        "All Appendix C quantum blockers remain in force.",
    ]

    diagnostics = {
        "rho_eq_at_R_eq": RHO_EQ_AT_R_EQ,
        "source_difference": static_test.source_difference,
        "condition_1_static_bc": conditions.condition_1_static_bc,
        "condition_2_status": conditions.condition_2_status,
        "condition_3_galley_projection": conditions.condition_3_galley_projection,
        "all_conditions_met": conditions.all_conditions_met,
        "source_vanishes": static_test.source_vanishes,
        "g_minus_zero_guaranteed": static_test.g_minus_zero_guaranteed,
        "g_minus_zero_under_projection": static_test.g_minus_zero_under_projection,
        "source_driven_component_b": static_test.source_driven_component_b,
        "homogeneous_component_b": static_test.homogeneous_component_b,
        "source_path_closed": source_path_closed,
        "homogeneous_path_open": homogeneous_path_open,
        "universal_no_go": False,
        "a_crit": A_CRIT,
        "dynamic_subsumed": dynamic.g_minus_subsumed,
        "phi_minus_radial_power": phi_minus.radial_power,
        "phi_minus_provides_component_b": phi_minus.provides_component_b,
    }

    return GMinusClosureResult(
        valid=True,
        conditions=conditions,
        static_test=static_test,
        dynamic_assessment=dynamic,
        phi_minus_assessment=phi_minus,
        source_path_closed=source_path_closed,
        homogeneous_path_open=homogeneous_path_open,
        universal_no_go=False,
        verdict=verdict,
        nonclaims=nonclaims,
        forbidden_claims=FORBIDDEN_CLAIMS,
        diagnostics=diagnostics,
    )
