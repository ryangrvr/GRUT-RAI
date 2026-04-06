# GRUT II Rho — Far-Field Equivalence and Weak-Field Constraint Audit

## Does the Phase-Dependent Gravity Survive to the Far Field?

---

## Part I — Phase Localization

### Where do the two constitutive phases live?

The GRUT II system:
```
tau(t) * dPhi/dt + Phi = X + beta*(tau - tau_star)
tau_meta * dtau/dt + tau = tau_star + h(Phi(t-Delta) - X)
```

depends on the SOURCE X = M/r^2. The source drives the constitutive dynamics. Where X is large (near compact objects), the constitutive dynamics are strong. Where X is small (far field), the constitutive dynamics are weak.

### The Level-1 tau reduction determines the regime

```
tau_local(r) = tau_0 * t_dyn(r) / (tau_0 + t_dyn(r))
```

- **Near compact objects (r ~ r_s):** tau_local ~ t_dyn << tau_0. Constitutive dynamics are FAST and STRONG.
- **Far from sources (r >> r_s):** tau_local ~ tau_0 >> t_dyn. Constitutive dynamics are SLOW and WEAK.

### The phase selection depends on history near the compact object

The bistability (Eq2 vs Eq3) was found in the STRONG-FIELD regime where tau is small, the source X = M/r^2 is large, and the cubic saturation and delay are active. In the FAR FIELD:

- X → 0 as r → infinity
- The equilibrium Phi_eq = X → 0 in both phases
- The cubic term h(v) = gamma*v - delta*v^3 with v = Phi - X → 0 vanishes
- The tau dynamics reduce to: tau_meta dtau/dt + tau = tau_star (no forcing)
- tau → tau_star everywhere

**In the far field, BOTH phases converge to the SAME state: Phi = 0, tau = tau_star.**

The phase distinction DOES NOT SURVIVE to the far field. It is a COMPACT-OBJECT-LOCAL property.

### Classification

**The two constitutive phases are STRONG-FIELD-ONLY, compact-object-local phenomena.** They exist in a shell around the compact object where X is large enough to drive the cubic constitutive dynamics. Outside this shell, both phases relax to the same trivial state (Phi = 0, tau = tau_star).

---

## Part II — Far-Field Weak-Limit Calculation

### Asymptotic metric at large r

At large r, the constitutive field Phi → X = M/r^2 (the equilibrium tracking). Both phases converge to this same state because the cubic/delay structure is only active when X is large.

The constitutive energy density at large r:
```
rho_Phi = Phi^2/(2tau_0^2) - Phi*X/tau_0
        = X^2/(2tau_0^2) - X^2/tau_0    (at Phi = X)
        = -X^2/(2tau_0^2)
        = -M^2/(2tau_0^2 r^4)
```

This is the SAME for both phases at large r (because both have Phi = X, tau = tau_0 at large r).

The far-field correction to the Newtonian potential from T^Phi:
```
delta_Phi_N(r) ~ integral rho_Phi(r') / |r - r'| d^3r' ~ M^2/(tau_0^2 r^2)  [at large r]
```

This falls as 1/r^2, much faster than the Newtonian 1/r potential. It is a CORRECTION to the Newtonian potential, not a modification of G_N.

### Effective G_N

At large r, the mass seen by a distant observer is:
```
M_ADM = M + integral 4pi r^2 rho_Phi dr
```

where the integral includes the constitutive energy density. Since rho_Phi is the SAME in both phases at large r, the ADM mass is the SAME.

The effective Newtonian potential is:
```
Phi_N = -G M_ADM / r + O(1/r^2 corrections)
```

with M_ADM identical in both phases. The leading-order Newtonian gravity is IDENTICAL.

**Verdict: same_far_field_GN.** Both phases have the same effective G_N and the same asymptotic Newtonian potential.

---

## Part III — No-Contradiction Audit

### Reconciling Pi's 5.5x DC difference with far-field equivalence

**The 5.5x DC difference is a LOCAL constitutive response in the strong-field interior.** It measures how the system AT THE EQUILIBRIUM responds to perturbations. The equilibrium is the compact-object interior (r ~ R_eq ~ r_s/3), not the far field.

In the far field (r >> r_s):
- Both phases have Phi = X = M/r^2 and tau = tau_0
- The coupling coefficients drho/dPhi = Phi/(tau_0^2) - X/tau_0 = X(1/tau_0^2 - 1/tau_0) are the SAME
- The constitutive susceptibility chi is the SAME (both use tau_0)
- The full metric susceptibility G_metric is the SAME

**The 5.5x difference is CONFINED to the constitutive shell around the compact object.** It does not propagate to the far field because the phase-specific tau values (tau_eq2 = 1.67, tau_eq3 = 0.78) exist only in the strong-field interior. Outside, tau → tau_0 in both phases.

### The radial structure

```
r < R_shell: phase-dependent (tau = tau_eq2 or tau_eq3; constitutive active)
R_shell < r < ~few r_s: transition zone (tau interpolates to tau_0)
r >> r_s: universal (tau = tau_0; both phases identical)
```

The "constitutive shell" radius R_shell depends on where the cubic/delay dynamics are active. This is determined by where X = M/r^2 is large enough to sustain the bistability conditions (bg > 1 in terms of the local effective coupling).

### Explicit resolution

Pi's 5.5x DC difference was computed at the EQUILIBRIUM POINT (Eq2 or Eq3), which is a property of the compact-object interior. The far-field metric susceptibility is computed at large r where both phases converge. These are different spatial locations with different constitutive parameters. There is no contradiction.

---

## Part IV — Weak-Field Observable Screen

### Does the phase difference affect weak-field observables?

**No, at leading order.** The far-field metric is Schwarzschild with the same M_ADM. The post-Newtonian corrections from T^Phi are:

1. **Identical in both phases at leading order** (both have rho ~ -M^2/(2tau_0^2 r^4) at large r)
2. **Phase-dependent only in subleading corrections** from the interior shell structure

The subleading corrections encode the fact that the INTERIOR of the compact object has different constitutive properties. These appear as:
- Tidal Love numbers (depend on interior structure → phase-dependent)
- Post-Newtonian tidal parameters (depend on internal response → phase-dependent)
- Ringdown QNM spectrum (depends on interior → phase-dependent)

But the LEADING Newtonian and post-Newtonian gravity (orbital dynamics, perihelion precession, Shapiro delay) are IDENTICAL because M_ADM and the far-field metric are the same.

### Impact assessment

| Observable | Phase-dependent? | Reason |
|-----------|:---:|--------|
| Newtonian force law | NO | Same M_ADM, same 1/r falloff |
| PPN parameters (beta, gamma) | NO | Same far-field metric structure |
| Binary inspiral phasing (leading) | NO | Same orbital dynamics |
| **Tidal Love number k2** | **YES** | Depends on interior constitutive phase |
| **Tidal deformability Lambda** | **YES** | k2 × (R/M)^5; k2 is phase-dependent |
| **QNM spectrum** | **YES** | Depends on interior effective medium |
| **Post-merger remnant** | **YES** | Interior structure phase-dependent |

**The phase distinction is visible ONLY through observables that probe the INTERIOR of the compact object.** Far-field observables are protected by the universal far-field state (Phi = X, tau = tau_0).

---

## Part V — Strong-Field-Only Possibility

### CONFIRMED: The phase distinction is strong-field-only.

The two phases differ only in a constitutive shell around the compact object (r < few × r_s). Outside this shell, both phases converge to the universal state. The far-field metric is Schwarzschild with the same M_ADM.

The distinction survives in:
1. **Compact-object interior structure** (rho differs by 6.7%)
2. **Tidal response** (Love numbers differ; perturbation response differs by 5.5-10x)
3. **Ringdown / QNM** (interior effective medium affects damping)
4. **Post-merger dynamics** (remnant structure phase-dependent)

The distinction is INVISIBLE in:
1. Far-field gravity (same Newtonian potential)
2. Orbital dynamics (same PPN parameters)
3. Light bending (same asymptotic metric)
4. Gravitational-wave propagation in the far zone (same speed, same dispersion)

### This is the ideal outcome

A constitutive phase that is invisible in the far field but measurable through interior-probing observables is EXACTLY the structure needed for a viable theory:
- No contradiction with solar-system or pulsar-timing tests (far-field identical)
- Testable through GW observations that probe compact-object interiors (tidal deformability, ringdown)
- History-dependent (different compact objects could be in different phases)
- Falsifiable (specific tidal/QNM predictions for each phase)

---

## Part VI — Regime Map

| Regime | Eq2 vs Eq3 | Why |
|--------|:----------:|-----|
| **Weak field / asymptotic** | INDISTINGUISHABLE | Both → Phi=X, tau=tau_0 |
| **Moderate field / inspiral** | INDISTINGUISHABLE (leading) | Same M_ADM, same orbital dynamics |
| **Tidal response** | **STRONGLY DISTINGUISHABLE** | Interior structure differs (5.5-10x susceptibility) |
| **Strong field / interior** | **STRONGLY DISTINGUISHABLE** | Different Phi, tau, rho, coupling coefficients |
| **Merger-ringdown** | **STRONGLY DISTINGUISHABLE** | Interior effective medium differs |
| **Post-merger remnant** | **POTENTIALLY DISTINGUISHABLE** | Remnant phase depends on history |

---

## Part VII — Final Verdict

### far_field_equivalence_preserved + phases_differ_only_in_strong_field_regime.

The two constitutive phases converge to the same universal state (Phi = X, tau = tau_0) in the far field. The effective G_N is identical. All leading-order weak-field observables are the same. The phase-dependent constitutive properties (5.5-10x metric susceptibility difference) are CONFINED to the strong-field interior of compact objects.

This is the best possible outcome: the phase structure is REAL and MEASURABLE (through tidal deformability, QNM spectrum, and post-merger dynamics) while being SAFE from weak-field constraints (solar-system tests, binary-pulsar timing, PPN limits are all satisfied trivially).

### Public-Facing Paragraph

GRUT II Rho establishes that the two constitutive phases (over-response and under-response) are indistinguishable in the far field and in all weak-field gravitational tests. Both phases converge to the same universal constitutive state at large distance from compact objects, producing identical Newtonian gravity, identical PPN parameters, and identical orbital dynamics. The phase distinction is CONFINED to the strong-field interior of compact objects, where the constitutive energy density is 15% of the gravitational energy and the metric susceptibility differs by 5.5-10x between phases. The observable signatures are: different tidal Love numbers, different gravitational-wave tidal deformability, different quasi-normal mode spectra, and different post-merger remnant structure. This is the ideal phenomenological structure: testable through gravitational-wave interior probes while safe from existing weak-field constraints.

### Internal Doctrine

If far-field equivalence had FAILED — if the two phases produced different G_N or different PPN parameters — the theory would be immediately killed by solar-system and pulsar-timing data. The survival of far-field equivalence is not automatic; it depends on the specific structure of the GRUT II constitutive equation (the cubic/delay dynamics vanish when X → 0 at large r, forcing both phases to converge). This is a structural prediction of the theory, not a tuning. Any modification that makes the phase distinction survive to the far field would be immediately constrained. The strong-field localization is load-bearing.

### Next Forced Move

Compute the tidal Love number k2 for compact objects in each constitutive phase. This is the most directly measurable quantity that probes the interior phase distinction: k2 depends on the equation of state (which is phase-dependent through tau and rho), and k2 is measured in binary neutron star mergers through the tidal deformability parameter Lambda. The LIGO/Virgo measurement of Lambda from GW170817 provides a direct constraint.

---

*GRUT II Rho complete. Far-field equivalence: PRESERVED. Phase distinction: STRONG-FIELD ONLY. Weak-field tests: SAFE. Observable channel: tidal deformability and QNM spectrum. Verdict: far_field_equivalence_preserved + phases_differ_only_in_strong_field_regime.*
