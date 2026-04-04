# Appendix W-B: Spatial Propagation Extension

GRUT Extension Program -- Phase W-B

---

## Recommended Extension: Damped Hyperbolic (Telegrapher)

    tau_2 d^2Phi/dt^2 + tau_1 dPhi/dt + Phi - c^2 nabla^2 Phi = X

**New postulates**: 2 parameters (tau_2 inertial timescale, c speed). No new fields.

**Properties**:
- Finite characteristic speed: c = ell/sqrt(tau_2)
- Preserves native dissipation: tau_1 term = Book II native core
- Native recovered as limit: tau_2 -> 0 gives tau dPhi/dt + Phi = X
- Restricted Lorentz: at omega >> 1/tau_1, approximates wave equation

## Candidate Comparison

| Class | Params | Fields | Speed? | Dissipation? | Lorentz? | Cost | Verdict |
|-------|--------|--------|--------|-------------|---------|------|---------|
| C1 Diffusive | 1 | 0 | No | Yes | No | minimal | no speed |
| **C2 Telegrapher** | **2** | **0** | **Yes** | **Yes** | **Restricted** | **moderate** | **PREFERRED** |
| C3 Nonlocal | many | 0 | depends | Yes | depends | high | underdetermined |
| C4 Auxiliary | 3+ | 1 | Yes | Yes | conditional | highest | costly |

## Verdicts

| Verdict | Value |
|---------|-------|
| Extension | minimal_propagation_patch_identified |
| Preferred | damped_hyperbolic_extension_preferred |
| Speed | finite_characteristic_speed_conditionally_supported |
| Lorentz | restricted_effective_lorentz_appearance_supported |
| Authorization | authorized_to_proceed_to_WC |

**Overall: first_propagation_extension_identified_under_strict_postulate_accounting**

All new scales are EXPLICIT POSTULATES. Propagation was NOT native.
Book II is the long-time LIMIT of the extension.

**W-C authorized** for Born probability extension.
