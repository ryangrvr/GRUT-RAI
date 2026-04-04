# GRUT-RAI Program-State Schema

## Machine-Usable Cross-Sector State Representation

---

## 1. Purpose

This document defines the machine-usable schema that holds the complete program state across all sectors. It is the single source of truth for GRUT-RAI's understanding of where the program stands.

The schema is implemented as a Python dataclass hierarchy in `grut/program_state.py` and serializable to JSON.

---

## 2. Top-Level Schema

```
ProgramState
├── identity: ProgramIdentity
├── sectors: Dict[str, SectorState]
│   ├── "vacuum_constitutive": SectorState
│   ├── "matter_biology": SectorState
│   ├── "gravitational": SectorState
│   ├── "cosmological": SectorState
│   ├── "strong_field_compact": SectorState
│   ├── "source_defect": SectorState
│   └── "grut_rai": SectorState
├── authority_registry: AuthorityRegistry
├── failed_routes: List[FailedRoute]
├── nonclaims: List[Nonclaim]
├── cost: CostLedger
├── handoffs: List[SectorHandoff]
└── meta: SchemaMeta
```

---

## 3. Component Definitions

### ProgramIdentity

| Field | Type | Description |
|-------|------|-------------|
| `identity_statement` | str | One-sentence program identity |
| `public_canon_layer` | str | What public canon contains |
| `validated_baseline_layer` | str | What validated baseline contains |
| `active_frontier_layer` | str | What active frontier contains |
| `toe_status` | enum | {ACTIVE, RETIRED, CONDITIONALLY_REOPENABLE} |
| `gravity_identity` | str | Current gravitational identity |

### SectorState

| Field | Type | Description |
|-------|------|-------------|
| `name` | str | Sector identifier |
| `backbone_relation` | str | How this sector connects to τ dΦ/dt + Φ = X |
| `authority_tier` | enum | C0–C6 |
| `status` | enum | {FROZEN, ACTIVE, FRONTIER, FAILED, BLOCKED} |
| `validated_content` | List[str] | What is established |
| `conditional_content` | List[str] | What is conditional (with gates) |
| `open_content` | List[str] | What is unresolved |
| `failed_content` | List[str] | What has been tested and failed |
| `nonclaims` | List[str] | What must not be claimed |
| `reality_touching_outputs` | List[RealityOutput] | Classified outputs (R1–R7) |
| `dependencies` | List[str] | Sectors this depends on |
| `next_legitimate_step` | str | One concrete next action |
| `changes_program_identity` | bool | Whether changes here affect the three-layer structure |

### RealityOutput

| Field | Type | Description |
|-------|------|-------------|
| `description` | str | What the output is |
| `class_code` | enum | R1–R7 |
| `authority_tier` | enum | C0–C6 |
| `comparison_ready` | bool | Whether it can be compared to data |

### CostLedger

| Field | Type | Description |
|-------|------|-------------|
| `committed_postulates` | int | Currently committed postulates |
| `committed_parameters` | int | Currently committed parameters |
| `committed_fields` | int | Currently committed fields |
| `committed_dof` | int | Currently committed DOF |
| `bridges_committed` | int | Number of committed bridges |
| `hypothetical_ggb_postulates` | int | If GGB committed |
| `hypothetical_ggb_parameters` | int | If GGB committed |
| `hypothetical_ggb_fields` | int | If GGB committed |
| `hypothetical_ggb_dof` | int | If GGB committed |
| `zero_cost_targets` | int | Count of zero-cost upper-stack targets |

### FailedRoute

| Field | Type | Description |
|-------|------|-------------|
| `name` | str | What failed |
| `book` | str | Where it failed |
| `reason` | str | Why it failed |
| `sector` | str | Which sector |
| `permanently_failed` | bool | Whether new work could revive it |

### Nonclaim

| Field | Type | Description |
|-------|------|-------------|
| `claim` | str | What is not claimed |
| `reason` | str | Why it is a nonclaim |
| `permanent` | bool | Whether this can ever be lifted |

### SectorHandoff

| Field | Type | Description |
|-------|------|-------------|
| `from_sector` | str | Source sector |
| `to_sector` | str | Receiving sector |
| `content` | str | What is handed off |
| `authority_inherited` | enum | Maximum authority tier inherited |
| `conditions_carried` | List[str] | Conditions that carry forward |

### SchemaMeta

| Field | Type | Description |
|-------|------|-------------|
| `schema_version` | str | Schema version |
| `last_updated` | str | Date of last update |
| `last_book` | str | Last Book that modified state |
| `charter_version` | str | Charter version this state conforms to |

---

## 4. Current Program State (Serialized)

See the implementation in `grut/program_state.py` for the canonical serialized state.

---

*Program-State Schema complete. Top-level structure, component definitions, field specifications, and relationship to the charter and authority architecture.*
