# Sector 4 — Gravity: Specification

## Sector name
Gravity

## Status
**Partial**

This is the first genuinely partial sector. It has significant computational results — including negative results that constrain the program's trajectory. Honesty about what failed is as important as what succeeded.

## Claim boundary

**What is claimed:**
- GRUT operates WITHIN standard Einstein gravity, with constitutive scalar matter as the source
- The gravitational decoherence sector (Sector 3) provides the primary novel gravity-facing prediction
- The semiclassical coupling of the constitutive field to the Schwarzschild metric is numerically implemented and produces locked results
- The static scalar-only TOV interior WORSENS the metric (f = -17.71, negative result, LOCKED)
- The dynamical interior shows transient metric improvement but late-time failure
- All tested singularity-resolution routes have FAILED (10 routes total, FROZEN)
- The weak-field exterior correction is analytically constrained but observationally silent at all physical tau

**What is NOT claimed:**
- No native gravity derivation (gravity is not emergent from GRUT)
- No graviton
- No full backreaction closure
- No UV completion
- No singularity resolution (all routes failed)
- No modification of Einstein's equations
- No restored ToE through the gravity sector alone

## Gravity identity
"Matter/organization theory within standard Einstein gravity." (from program_state.py)

## Dependencies

- **Sector 1:** QM recovery (constitutive backbone)
- **Sector 3:** Gravitational decoherence (the primary novel sub-sector)
- **A0-A2:** Foundational axioms
- **GR:** Standard Einstein gravity (external, not derived)

## Deliverables

| # | Deliverable | Path |
|---|-------------|------|
| 1 | Specification | this file |
| 2 | Math scaffold | `docs/v4_part2/sector_04_gravity_math.md` |
| 3 | Code interface | `grut_solver/sectors/gravity/` |
| 4 | Validation tests | `tests/sectors/gravity/test_sector_04.py` |
| 5 | Notebook | `notebooks/sector_04_gravity.py` |
| 6 | Paper summary | `docs/v4_part2/sector_04_gravity_for_paper.md` |

## Closure condition

This sector is NOT closed. Closure would require:
1. A working singularity-resolution mechanism (none exists)
2. Full backreaction of the constitutive field on the metric (not achieved)
3. A graviton or quantized gravitational mode (not present)
4. UV completion of the gravitational sector (not present)

The sector is honestly partial. The computational infrastructure exists but the physics goals are unmet.
