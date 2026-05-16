# Gate 3 Mathematica Result Schema

Date: May 9, 2026  
Purpose: Define strict JSON payload format imported from Mathematica/HypExp.

## Required JSON Fields

```json
{
  "coefficient_name": "C_Euler_cosmo or C_Euler_final",
  "value": "exact symbolic/rational/string or null",
  "epsilon_pole": "pole term representation or null",
  "finite_part": "finite epsilon^0 representation or null",
  "scheme": "OR4-approved (or explicit compatible scheme)",
  "regulator": "D=4-2epsilon",
  "channel": "Euler",
  "projection": "round_s4_euler",
  "protected": true,
  "source_tool": "Mathematica/HypExp",
  "source_file": "notebook_or_script_name",
  "manual_target_matching": false,
  "status": "computed or blocked",
  "blocker": "required when status=blocked; null otherwise"
}
```

## Validation Rules

- Reject missing `scheme`.
- Reject missing `regulator`.
- Reject non-Euler `channel`.
- Reject non-round-S4 `projection`.
- Reject `manual_target_matching = true`.
- Reject `status = computed` when `value` or `finite_part` is missing.
- Reject `protected = false` for quotient-eligible coefficients.
- Allow `status = blocked` only with non-empty `blocker` message.

## Example 1: Blocked Result

```json
{
  "coefficient_name": "C_Euler_cosmo",
  "value": null,
  "epsilon_pole": null,
  "finite_part": null,
  "scheme": "OR4-approved",
  "regulator": "D=4-2epsilon",
  "channel": "Euler",
  "projection": "round_s4_euler",
  "protected": true,
  "source_tool": "Mathematica/HypExp",
  "source_file": "GATE3_AJ_CUBE_INTEGRAL_HYPEXP.wl",
  "manual_target_matching": false,
  "status": "blocked",
  "blocker": "Hypergeometric cube Laurent extraction unresolved"
}
```

## Example 2: Computed Protected Coefficient

```json
{
  "coefficient_name": "C_Euler_final",
  "value": "115428/100000",
  "epsilon_pole": "-3/epsilon",
  "finite_part": "115428/100000",
  "scheme": "OR4-approved",
  "regulator": "D=4-2epsilon",
  "channel": "Euler",
  "projection": "round_s4_euler",
  "protected": true,
  "source_tool": "Mathematica/HypExp",
  "source_file": "gate3_notebook.nb",
  "manual_target_matching": false,
  "status": "computed",
  "blocker": null
}
```

## Example 3: Rejected Non-Euler Coefficient

```json
{
  "coefficient_name": "C_Weyl_candidate",
  "value": "1",
  "epsilon_pole": null,
  "finite_part": "1",
  "scheme": "OR4-approved",
  "regulator": "D=4-2epsilon",
  "channel": "Weyl",
  "projection": "round_s4_euler",
  "protected": true,
  "source_tool": "Mathematica/HypExp",
  "source_file": "gate3_notebook.nb",
  "manual_target_matching": false,
  "status": "computed",
  "blocker": null
}
```

## Example 4: Rejected Manual-Target Result

```json
{
  "coefficient_name": "C_Euler_cosmo",
  "value": "1.15470",
  "epsilon_pole": null,
  "finite_part": "1.15470",
  "scheme": "OR4-approved",
  "regulator": "D=4-2epsilon",
  "channel": "Euler",
  "projection": "round_s4_euler",
  "protected": true,
  "source_tool": "Mathematica/HypExp",
  "source_file": "gate3_notebook.nb",
  "manual_target_matching": true,
  "status": "computed",
  "blocker": null
}
```
