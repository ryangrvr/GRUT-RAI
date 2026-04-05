# Book XVII — Target Alpha: GRUT-RAI Dynamical Core State Model

---

## 1. Theorem Fields

| Field | Value |
|-------|-------|
| `theorem_count` | `5` |
| `theorem_1` | `forward_semigroup: S(t) = exp(-t/tau); LOCKED` |
| `theorem_2` | `lyapunov_stability: V = (Phi-X)^2/2; dV/dt = -2V/tau; LOCKED` |
| `theorem_3` | `dissipative_balance: dV/dt + D = 0; LOCKED` |
| `theorem_4` | `native_t_breaking: not t-reversal invariant; LOCKED` |
| `theorem_5` | `monotone_contraction: ||Phi(t)-X|| monotone decreasing; LOCKED` |
| `all_proven` | `true` |
| `all_locked` | `true` |

## 2. Scope Fields

| Field | Value |
|-------|-------|
| `literal_sectors` | `2 (vacuum, gravity equilibrium)` |
| `recovered_sectors` | `1 (quantum classical limit; 3 limits required)` |
| `heuristic_sectors` | `1 (cosmology; extension-heavy)` |
| `excluded_sectors` | `4 (defects, waves, biology, carriers)` |
| `universality_type` | `ARCHITECTURAL (not grammatical)` |

## 3. Embeddability Fields

| Field | Value |
|-------|-------|
| `vs_lagrangian` | `NOT_EMBEDDABLE (EL eqs are 2nd-order, reversible)` |
| `vs_hamiltonian` | `NOT_EMBEDDABLE (preserves phase volume; incompatible with contraction)` |
| `vs_kg_plus_bath` | `EMBEDDABLE (overdamped limit reproduces full ODE)` |
| `vs_lindblad` | `RECOVERED (expectation-value eq under 3 limits)` |
| `vs_generic_open_system` | `GENERIC (structural properties shared by all 1st-order dissipative)` |

## 4. Irreducibility Fields

| Field | Value |
|-------|-------|
| `vs_conservative` | `IRREDUCIBLE (no Lagrangian/Hamiltonian parent; theorem-grade)` |
| `vs_open_system` | `NOT_IRREDUCIBLE (generic structural properties)` |
| `specific_content` | `NARROW (tau^2 = 3/2; X = m/r^2; GR coupling; but gravity coupling silent)` |
| `overall_irreducibility` | `CONDITIONAL` |
| `t_breaking_status` | `NATIVE (vs conservative); EMERGENT (vs coarse-grained parent)` |
| `ontological_status` | `CHOICE (fundamental vs effective is not empirically decidable)` |
| `observational_anchor` | `ABSENT` |

## 5. Limitation/Failure Fields

| Field | Value |
|-------|-------|
| `generic_properties` | `HIGH (semigroup, Lyapunov, T-breaking shared by all 1st-order dissipative)` |
| `observationally_unanchored` | `HIGH (no known test)` |
| `coarse_grained_embeddable` | `MODERATE (KG + bath overdamped limit)` |
| `ontological_not_physical` | `MODERATE (fundamental vs effective = choice)` |
| `gravity_coupling_silent` | `HIGH (XVI Beta: reducible + silent at equilibrium)` |
| `decoherence_conditional` | `MODERATE (depends on postulated L)` |

## 6. Frontier-Status Fields

| Field | Value |
|-------|-------|
| `dynamical_frontier` | `CONDITIONAL (wedge real but narrow + generic + unanchored)` |
| `gravity_frontier` | `FROZEN (XVI Terminal)` |
| `biology_frontier` | `INTACT (26 zero-cost targets; extension level; productive)` |
| `quantum_frontier` | `INTACT (second-wave authorized; Q-II unbuilt)` |
| `program_continues` | `true` |
| `program_honest` | `true` |

## 7. Next-Stage Fields

| Field | Value |
|-------|-------|
| `path_a` | `Search for specific-ODE observable consequence (tau^2 = 3/2 effect)` |
| `path_b` | `Deploy architecture in productive sectors (biology T3/T4; quantum Q-II)` |
| `recommended` | `PATH_B (higher feasibility; lower risk; genuine structural leverage)` |
| `path_a_risk` | `HIGH (may find nothing; dynamics may remain unanchored)` |
| `path_b_risk` | `LOW-MODERATE (biology requires new bridge postulates; quantum is authorized)` |

## 8. Verdict Fields

| Field | Value |
|-------|-------|
| `xvii_alpha_verdict` | `B_conditional_irreducible_wedge` |
| `theorems_consolidated` | `true` |
| `scope_clarified` | `true` |
| `embeddability_tested` | `true` |
| `irreducible_vs_conservative` | `true (genuine)` |
| `irreducible_vs_open_system` | `false (generic)` |
| `observational_anchor` | `absent` |
| `changes_interpretation` | `true (from "irreducible frontier" to "conditional wedge, generic, unanchored")` |

## 9. Minimal Serialized State

```json
{
  "schema_version": "2.1.0",
  "last_book": "XVII_Alpha",
  "last_updated": "2026-04",

  "theorems": {
    "count": 5,
    "all_proven": true,
    "all_locked": true,
    "literal_sectors": 2,
    "excluded_sectors": 4
  },

  "embeddability": {
    "vs_lagrangian": "NOT_EMBEDDABLE",
    "vs_hamiltonian": "NOT_EMBEDDABLE",
    "vs_coarse_grained": "EMBEDDABLE",
    "vs_generic_open_system": "GENERIC"
  },

  "irreducibility": {
    "vs_conservative": "IRREDUCIBLE",
    "vs_open_system": "NOT_IRREDUCIBLE",
    "overall": "CONDITIONAL",
    "observational_anchor": "ABSENT",
    "t_breaking": "NATIVE_VS_CONSERVATIVE_EMERGENT_VS_OPEN"
  },

  "frontier": {
    "dynamics": "CONDITIONAL",
    "gravity": "FROZEN",
    "biology": "INTACT",
    "quantum": "INTACT"
  },

  "next": {
    "recommended": "deploy architecture in productive sectors (biology, quantum)",
    "alternative": "search for specific-ODE observable"
  },

  "surplus": {"demonstrated": 0, "conditional": 0, "total": 0},
  "cost": {"postulates": 16, "parameters": 11, "fields": 1, "dof": 6, "change": "ZERO"},
  "verdict": "B_conditional_irreducible_wedge"
}
```

---

*Dynamical Core State Model complete. 5 theorems. Conditional wedge. Generic properties. Observationally unanchored. Next: productive sectors.*
