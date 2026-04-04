# Appendix W0: Extension Entry Inventory

GRUT Extension Program -- Phase W0 (Book III Opening)

---

## Extension Dependency Table (Ranked)

| Rank | Extension | Deps | Layer | Priority | Risk | Minimal Postulate |
|------|-----------|------|-------|----------|------|-------------------|
| 1 | Propagation sector | 0 | 0 | foundational | medium | Spatial operator |
| 2 | Action completion | 1 | 1 | foundational | medium | Response-field S_eff |
| 3 | Born probability | 0 | 0 | foundational | low | P(n)=Tr(rho P_n) |
| 4 | Probe coupling | 1 | 1 | structural | high | F=-alpha grad(Phi) |
| 5 | Geometry dynamics | 2 | 2 | structural | high | Effective metric |
| 6 | Gauge structure | 2 | 2 | structural | high | Gauge field A_mu |
| 7 | Fermionic matter | 2 | 2 | completion | medium | Hopf/spinor |
| 8 | Chemistry composite | 3 | 3 | completion | high | Multiple postulates |
| 9 | Cosmological content | 2 | 2 | completion | high | Vacuum energy |
| 10 | Quantum/thermal vacuum | 2 | 2 | completion | medium | Noise + bath |

## Dependency Layers
- **Layer 0**: propagation_sector, born_probability (build first)
- **Layer 1**: action_completion, probe_coupling
- **Layer 2**: geometry, gauge, fermions, cosmology, quantum/thermal
- **Layer 3**: chemistry_composite (highest burden)

## Recommendation
**Build first**: born_probability (one axiom, no new DOF) AND/OR
propagation_sector (unlocks spatial transport).

**Verdict**: extension_inventory_complete_and_ranked
