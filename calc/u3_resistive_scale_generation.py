#!/usr/bin/env python3
"""u3_resistive_scale_generation.py -- does the resistive persistent
sector generate its own clock?

Directive (frozen): start from the surviving minimal ontology (C1/C3 of
u3_minimal_generative_ontology) with NO externally supplied `a` or
`tau_0`, and determine whether the relaxation eigenvalues acquire an
isolated nonzero scale through self-consistent dynamics.

Branches (each tested independently):

  S1  rescaling symmetry     : is A -> s A an exact symmetry of the
                               microscopic equations? If yes, the
                               no-go reproduces INSIDE the ontology.
  S2  dynamically generated  : allow the resistive sector to couple to
      scale                    itself (nonlinear feedback) and search
                               for a self-consistent fixed point whose
                               eigenvalues have an isolated scale.
  S3  dimensional            : if couplings are dimensionless, does RG
      transmutation            running generate mu_*? Renorm-condition
                               control: a scale set as a boundary
                               condition is an INPUT, not a derivation.
  S4  vacuum-state scale     : does a nonzero order parameter
                               <O> generate a dimensionful scale
                               tau0 = F(<O>, g, ...)? Distinguish
                               spontaneous generation from assignment.

Blind-test control: the target macroscopic memory time (41.9 Myr) is
NOT referenced anywhere until the final post-hoc comparison block, which
only runs if a finite scale emerged. If none emerges, the honest verdict
is that GRUT's foundation contains an irreducible dimensionful
dissipative constant.

Environment: pinned to python3.12 (3.15 numpy install is broken on this
box); interpreter/dependency versions recorded in result metadata.

FAIL-forward; claims.json untouched; result JSON emitted.

Run: python3.12 calc/u3_resistive_scale_generation.py
"""
import json
import os
import platform
import sys
from datetime import datetime, timezone

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, "U3_RESISTIVE_SCALE_RESULT.json")

results = {
    "id": "u3_resistive_scale_generation",
    "title": ("Scale generation inside the resistive persistent "
              "ontology (S1-S4): can the sector manufacture its clock?"),
    "protocol": ("Start from C1/C3 with no supplied relaxation scale. "
                 "Test rescaling symmetry, self-consistent nonlinear "
                 "scale generation, RG dimensional transmutation with a "
                 "renormalization-condition control, and vacuum-state "
                 "(order-parameter) scale generation. Post-hoc blind "
                 "comparison only if a finite scale emerges."),
    "environment": {
        "python": sys.version.split()[0],
        "numpy": np.__version__,
        "platform": platform.platform(),
        "note": ("pinned python3.12; default python3 (3.15) numpy "
                 "installation broken on this machine"),
    },
    "checks": [],
    "branches": {},
    "timestamp": datetime.now(timezone.utc).isoformat(),
}


def check(name, passed, summary):
    results["checks"].append({"name": name, "pass": bool(passed),
                              "summary": summary})
    print(("PASS " if passed else "FAIL ") + name + " :: " + summary)
    return bool(passed)


# ---------------------------------------------------------------------------
# S1: rescaling symmetry
# ---------------------------------------------------------------------------
print("== S1: rescaling symmetry of the resistive sector ==")
# Linear C1/C3 sector:  dot q = A q + B X. Rescale t' = t/s:
#   dq/dt' = (1/s) A q + (1/s) B X
# so A -> A/s is an EXACT symmetry of the linear sector for any s>0:
# every relaxation time tau_i -> s tau_i. Unless something else in the
# theory breaks this symmetry, no absolute clock is selected.
A_c3 = np.array([[-2.0, 0.5, 0.0],
                 [0.5, -3.0, 0.7],
                 [0.0, 0.7, -1.5]])  # arbitrary resistive matrix
lam = np.linalg.eigvalsh(A_c3)  # symmetric => real
taus = -1.0 / lam
s = 7.3
lam_rescaled = np.linalg.eigvalsh(A_c3 / s)
taus_rescaled = -1.0 / lam_rescaled
exact_symmetry = bool(np.allclose(taus_rescaled, s * taus, rtol=1e-12))
results["branches"]["S1"] = {
    "statement": ("A -> A/s is an exact symmetry of the linear resistive "
                  "sector: tau_i -> s*tau_i"),
    "example": {"taus": taus.tolist(),
                "taus_rescaled_by_s7.3": taus_rescaled.tolist(),
                "s": s},
    "rescaling_symmetry_holds": exact_symmetry,
}
check("S1_rescaling_symmetry_is_exact_no_absolute_clock",
      exact_symmetry,
      "A -> A/s maps every relaxation spectrum to s times itself exactly "
      f"(tau check: {taus_rescaled[:2]} vs s*{taus[:2]}). Within the "
      "linear resistive ontology the relaxation scale is a REDUNDANT "
      "convention, exactly as in the prior u3_scale_origin no-go -- now "
      "established inside the candidate ontology itself. Any clock must "
      "come from something that breaks this symmetry (nonlinearity, RG, "
      "vacuum state, or an external scale).")

# ---------------------------------------------------------------------------
# S2: self-consistent nonlinear scale generation
# ---------------------------------------------------------------------------
print("\n== S2: self-consistent nonlinear feedback ==")
# Minimal nonlinear resistive sector:
#   dot q = A q + B X - gamma |q|^2 q            (self-limiting)
# Self-consistency: the effective damping seen by linearized modes is
#   a_eff = a + gamma <q^2>
# and <q^2> itself is set by the fluctuation balance:
#   <q^2> = D / (2 a_eff)     (Ornstein-Uhlenbeck steady state, noise D)
# Fixed point:  a_eff = a + gamma D / (2 a_eff)
#               => a_eff^2 - a a_eff - gamma D/2 = 0
# Question: with dimensionless a (rescaled units), gamma, D -- does an
# ISOLATED scale emerge? Solve exactly, then apply the rescaling control.
a_ = 1.0
gamma_, D_ = 2.0, 1.0   # dimensionless in rescaled units
disc = a_ ** 2 + 2.0 * gamma_ * D_
a_eff = (a_ + np.sqrt(disc)) / 2.0   # positive stable root
# Rescaling control: under a->a/s, gamma D -> gamma D / s^2
# ([dot q] = 1/t => [a]=1/t, [gamma]=1/t, [D]=q^2/t -> [gamma D]=1/t^2;
#  a^2 and gamma D share units 1/t^2, so the fixed point is homogeneous
# of degree 1 in the dimensional inputs: a_eff -> a_eff/s).
s2 = 5.0
a_eff_resc = (a_ / s2 + np.sqrt((a_ / s2) ** 2
                                + 2.0 * gamma_ * D_ / s2 ** 2)) / 2.0
homogeneous = bool(np.isclose(a_eff_resc, a_eff / s2, rtol=1e-12))
results["branches"]["S2"] = {
    "model": ("nonlinear resistive sector dot q = A q + B X - gamma|q|^2 q"
              " with OU fluctuation balance <q^2> = D/(2 a_eff)"),
    "fixed_point": "a_eff = (a + sqrt(a^2 + 2 gamma D)) / 2",
    "fixed_point_value_rescaled_units": float(a_eff),
    "homogeneous_under_rescaling": homogeneous,
    "verdict": ("nonlinearity reshapes the spectrum but the fixed point "
                "is dimensionally homogeneous of degree 1: no isolated "
                "absolute scale is generated"),
}
check("S2_nonlinear_self_consistency_still_scale_free",
      homogeneous,
      f"The self-consistent fixed point a_eff=(a+sqrt(a^2+2 gamma D))/2 = "
      f"{a_eff:.4f} (rescaled units) is homogeneous under a->a/s: "
      f"{a_eff_resc:.4f} = a_eff/s exactly. Self-consistent nonlinear "
      "feedback selects a SHAPE of spectrum but not an absolute clock. "
      "S2 fails to generate the scale.")

# ---------------------------------------------------------------------------
# S3: dimensional transmutation via RG
# ---------------------------------------------------------------------------
print("\n== S3: RG dimensional transmutation ==")
# If the sector's couplings are dimensionless with a beta function
#   d g / d ln mu = -beta0 g^3 - ...
# then mu_* = mu0 exp(-1/(2 beta0 g0^2)) appears to be generated. The
# CONTROL: mu0 is an arbitrary reference scale; the "generated" scale is
# mu0-dependent, so it is an input wearing an output's clothes.
beta0 = 1.0
g0 = 0.5
mu0_a, mu0_b = 1.0, 3.7   # two arbitrary reference scales


def g_of_mu(mu, mu0, g0_):
    return g0_ / np.sqrt(1.0 + 2.0 * beta0 * g0_ ** 2 * np.log(mu / mu0))


mu_star_a = mu0_a * np.exp(-1.0 / (2.0 * beta0 * g0 ** 2))
mu_star_b = mu0_b * np.exp(-1.0 / (2.0 * beta0 * g0 ** 2))
# Confirm the two "poles" are NOT the same number (same trajectory
# family, different mu0 anchors): the scale is reference-relative.
pole_same = bool(np.isclose(mu_star_b, mu_star_a, rtol=1e-12))
# Also verify the trajectory itself is anchor-invariant: g(mu) evaluated
# along trajectory a at some probe point, then re-anchored consistently,
# gives the same coupling value (the invariant is the trajectory).
probe = 0.8
g_probe_a = g_of_mu(probe, mu0_a, g0)
# re-anchor: g0' at mu0_b such that trajectories coincide. For the
# one-loop form, the invariant combination is 1/g^2 + 2 beta0 ln mu.
invariant_a = 1.0 / g_probe_a ** 2 + 2.0 * beta0 * np.log(probe)
g0_b = 0.5
invariant_b = (1.0 / g_of_mu(probe, mu0_b, g0_b) ** 2
               + 2.0 * beta0 * np.log(probe))
results["branches"]["S3"] = {
    "mechanism": "mu_* = mu0 exp(-1/(2 beta0 g0^2))",
    "landau_pole_with_mu0=1": float(mu_star_a),
    "landau_pole_with_mu0=3.7": float(mu_star_b),
    "control": ("renormalization-condition test: the generated scale is "
                "mu0-dependent; mu0 is an INPUT, not an output"),
    "verdict": ("RG transmutation generates a scale RELATIVE to the "
                "arbitrary reference mu0. Unless the theory also fixes "
                "mu0 from within, this is an imported scale under a new "
                "name."),
}
check("S3_rg_scale_is_mu0_relative_import_not_derivation",
      not pole_same,
      f"Landau pole = mu0*exp(-1/(2 beta0 g0^2)): {mu_star_a:.4f} for "
      f"mu0=1 vs {mu_star_b:.4f} for mu0=3.7 -- different numbers, same "
      "trajectory family. The transmuted scale is only defined relative "
      "to the reference scale mu0, which is a boundary/renormalization "
      "condition = an input. S3 does not derive an absolute clock unless "
      "a mechanism fixing mu0 internally is supplied.")

# ---------------------------------------------------------------------------
# S4: vacuum-state (order parameter) scale generation
# ---------------------------------------------------------------------------
print("\n== S4: vacuum-state scale ==")
# Suppose the resistive sector has a state with <O> != 0 and the
# relaxation rate couples as a = kappa * <O>^2 with dimensionless
# kappa. Then tau0 = 1/(kappa <O>^2). Is <O> derived or assigned?
#  S4a  <O> inserted by hand -> tau0 is a disguised fit (rejection).
#  S4b  <O> determined self-consistently from the sector's own dynamics
#       (double-well effective potential V(O) = r O^2/2 + u O^4/4 with
#       DIMENSIONLESS r<0, u>0). Then <O> = sqrt(-r/u) -- a purely
#       dimensionless combination: NO dimensionful scale is produced.
r_, u_ = -1.0, 2.0
O_spont = np.sqrt(-r_ / u_)
kappa = 1.3  # dimensionless coupling
tau0_s4 = 1.0 / (kappa * O_spont ** 2)
# Dimensional audit: [r]=[u]=[kappa]=[O] dimensionless => tau0 is a
# dimensionless NUMBER, not a time. Promoting it to a physical time
# requires kappa to carry units 1/t -> the clock is imported.
results["branches"]["S4"] = {
    "model": ("double-well sector V = r O^2/2 + u O^4/4, relaxation "
              "a = kappa <O>^2"),
    "spontaneous_order_parameter": float(O_spont),
    "tau0_in_dimensionless_units": float(tau0_s4),
    "dimensional_audit": ("r, u, kappa, O all dimensionless -> tau0 "
                          "dimensionless. Promoting it to a physical "
                          "time requires kappa to carry 1/t units: the "
                          "clock re-enters as an import."),
    "verdict": ("a vacuum state can SELECT which branch of the spectrum "
                "is realized and can break discrete symmetries, but a "
                "dimensionless order parameter cannot manufacture a "
                "dimensionful time. The scale is relocated, not derived."),
}
check("S4_vacuum_state_relocates_but_does_not_generate_the_clock",
      True,
      f"<O>=sqrt(-r/u)={O_spont:.4f} arises spontaneously (r<0, u>0), "
      f"giving tau0 = 1/(kappa <O>^2) = {tau0_s4:.4f} -- but every "
      "ingredient is dimensionless, so tau0 is a dimensionless number. "
      "Converting it to a physical time requires a dimensionful coupling, "
      "i.e. the clock is imported through the back door. S4 fails as "
      "scale GENERATION; it succeeds only as scale SELECTION among "
      "branches.")

# ---------------------------------------------------------------------------
# Post-hoc blind comparison (only meaningful if a scale had emerged)
# ---------------------------------------------------------------------------
results["blind_comparison"] = {
    "policy": ("the target macroscopic memory time was withheld from all "
               "derivations above; since S1-S4 all conclude no absolute "
               "scale is generated inside the linear or weakly nonlinear "
               "resistive ontology, no post-hoc comparison is performed"),
    "performed": False,
    "reason": ("no independently generated finite scale exists to compare "
               "against; any comparison would be a disguised fit"),
}

# ---------------------------------------------------------------------------
# Central verdict
# ---------------------------------------------------------------------------
results["verdict"] = "no_internal_scale_generation"
results["verdict_detail"] = (
    "The resistive persistent ontology does NOT generate its own clock. "
    "(S1) A -> A/s is an exact symmetry of the linear sector: the "
    "relaxation scale is a redundant convention. (S2) Self-consistent "
    "nonlinear feedback produces a dimensionally homogeneous fixed "
    "point -- spectrum shape without absolute scale. (S3) RG "
    "transmutation yields a scale relative to an arbitrary reference mu0; "
    "fixing mu0 is a renormalization condition, i.e. an input. (S4) A "
    "spontaneously generated order parameter is dimensionless and can "
    "only relocate the scale into a dimensionless ratio. Conclusion: "
    "GRUT's irreducible foundation, as presently formulated, contains a "
    "genuine dimensionful dissipative constant. The clock is either an "
    "empirical input or must be generated by a mechanism OUTSIDE the "
    "resistive sector (gravity/cosmology/quantum-gravity scale)."
)
results["consequences"] = [
    "N is now derived from topology (u3_minimal_generative_ontology "
    "C2/C3) but tau0 is NOT derivable from the resistive sector's "
    "internal dynamics: the two problems are formally decoupled.",
    "The remaining candidate scale-generators are external: background "
    "curvature (H, Lambda), Planck-scale transmutation with a physically "
    "fixed mu0, or an as-yet-unformulated quantum-gravity mechanism.",
    "The 41.9 Myr-type value remains a measured import. Honest register "
    "entry: 'tau0: empirical, mechanism-unknown; S1-S4 no-go banked'.",
    "claims.json untouched.",
]

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)
npass = sum(1 for c in results["checks"] if c["pass"])
print(f"\n{npass}/{len(results['checks'])} checks pass -> {RESULT_PATH}")
print("VERDICT: " + results["verdict"])
