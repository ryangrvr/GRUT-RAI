#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/theory/hard_theory/gate3_outputs"
WL_SCRIPT="$ROOT_DIR/theory/hard_theory/GATE3_AJ_CUBE_INTEGRAL_HYPEXP.wl"
WL_REDUCED_SCRIPT="$ROOT_DIR/theory/hard_theory/GATE3_AJ_MASSIVE_REDUCED_HYPEXP.wl"
PYTHON_BIN="${PYTHON_BIN:-python}"
HYPEXP_APP_DIR="${WOLFRAM_HYPEXP_APP_DIR:-$HOME/Library/Wolfram/Applications/HypExp-2.0}"
HYPEXP_PROBE_CODE='If[StringQ[Environment["WOLFRAM_HYPEXP_APP_DIR"]] && Environment["WOLFRAM_HYPEXP_APP_DIR"] =!= "" && FileExistsQ[FileNameJoin[{Environment["WOLFRAM_HYPEXP_APP_DIR"], "HypExp.m"}]], $Path = Prepend[DeleteCases[$Path, FileNameJoin[{$HomeDirectory, "HypExp"}]], Environment["WOLFRAM_HYPEXP_APP_DIR"]]]; Quiet[Needs["HypExp`"]]; If[MemberQ[$Packages, "HypExp`"], Null, Exit[2]]'
BRANCH_ID="${GATE3_BRANCH_ID:-}"
REGULATOR_PARAM="${GATE3_M2_OVER_H2:-}"
REDUCED_ROUTE="${GATE3_MASSIVE_ROUTE:-}"

mkdir -p "$OUT_DIR"

COSMO_JSON="$OUT_DIR/C_Euler_cosmo.json"
FINAL_JSON="$OUT_DIR/C_Euler_final.json"

# Validate GATE3_M2_OVER_H2 as positive rational/decimal if massive_regulated branch is selected.
validate_m2_over_h2() {
  local param="$1"
  if [[ -z "$param" ]]; then
    echo "GATE3_M2_OVER_H2 is empty; rejecting massive_regulated branch"
    return 1
  fi
  # Check if string is numeric (int or float) and positive
  if ! [[ "$param" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    echo "GATE3_M2_OVER_H2='$param' is not a positive number; rejecting"
    return 1
  fi
  # Check if greater than 0
  if (( $(echo "$param <= 0" | bc -l) )); then
    echo "GATE3_M2_OVER_H2='$param' is not positive; rejecting"
    return 1
  fi
  return 0
}

write_blocked() {
  local reason="$1"
  local regulator="${2:-}"
  local regulator_role="${3:-}"
  
  "$PYTHON_BIN" -m grut.hard_theory.s4_ctp_solver.gate3_blocked_output_writer \
    --output-dir "$OUT_DIR" \
    --blocker "$reason" \
    --source-file "$WL_SCRIPT" \
    ${regulator:+--m2-over-h2 "$regulator"} \
    ${regulator_role:+--regulator-role "$regulator_role"}
}

if [[ -z "$BRANCH_ID" ]]; then
  echo "branch_id is required (set GATE3_BRANCH_ID); writing blocked outputs"
  write_blocked "branch_id missing"
  exit 0
fi

case "$BRANCH_ID" in
  conformal_closed_form|hminus_direct_limit|hminus_derivative_regularized|mmc_massless)
    ;;
  massive_regulated)
    if ! validate_m2_over_h2 "$REGULATOR_PARAM"; then
      write_blocked "massive_regulated requires GATE3_M2_OVER_H2 (positive rational or decimal)" "$REGULATOR_PARAM" "massive_scalar_ir_regulator"
      exit 0
    fi
    ;;
  *)
    echo "Invalid branch_id '$BRANCH_ID'; writing blocked outputs"
    write_blocked "branch_id invalid"
    exit 0
    ;;
esac

if ! command -v wolframscript >/dev/null 2>&1; then
  echo "wolframscript not found; writing blocked outputs"
  write_blocked "wolframscript unavailable"
  exit 0
fi

# Probe whether kernel is runnable and license is valid.
if ! wolframscript -code 'Print["wolfram_ok"]' >/dev/null 2>&1; then
  echo "wolframscript exists but kernel/license unavailable; writing blocked outputs"
  write_blocked "wolframscript license/kernel unavailable"
  exit 0
fi

# Probe HypExp availability before full run.
if ! WOLFRAM_HYPEXP_APP_DIR="$HYPEXP_APP_DIR" wolframscript -code "$HYPEXP_PROBE_CODE" >/dev/null 2>&1; then
  echo "HypExp unavailable; writing blocked outputs"
  write_blocked "HypExp unavailable"
  exit 0
fi

# If reduced route is requested for massive_regulated, use reduced script instead
if [[ "$BRANCH_ID" == "massive_regulated" && -n "$REDUCED_ROUTE" ]]; then
  echo "Using reduced-integral strategy for massive_regulated with route: $REDUCED_ROUTE"
  
  # Validate route
  if ! [[ "$REDUCED_ROUTE" =~ ^[ABCD]$ ]]; then
    echo "Invalid GATE3_MASSIVE_ROUTE='$REDUCED_ROUTE'; must be A, B, C, or D"
    write_blocked "invalid reduced route"
    exit 0
  fi
  
  echo "Running Mathematica Gate3 reduced-route handoff (Route $REDUCED_ROUTE) for C_Euler_cosmo"
  if ! WOLFRAM_HYPEXP_APP_DIR="$HYPEXP_APP_DIR" GATE3_M2_OVER_H2="$REGULATOR_PARAM" wolframscript -file "$WL_REDUCED_SCRIPT" C_Euler_cosmo "$COSMO_JSON" "$BRANCH_ID" "$REDUCED_ROUTE"; then
    echo "Mathematica reduced-route run failed for C_Euler_cosmo; writing blocked outputs"
    write_blocked "Mathematica reduced-route run failed during C_Euler_cosmo"
    exit 0
  fi
  
  echo "Running Mathematica Gate3 reduced-route handoff (Route $REDUCED_ROUTE) for C_Euler_final"
  if ! WOLFRAM_HYPEXP_APP_DIR="$HYPEXP_APP_DIR" GATE3_M2_OVER_H2="$REGULATOR_PARAM" wolframscript -file "$WL_REDUCED_SCRIPT" C_Euler_final "$FINAL_JSON" "$BRANCH_ID" "$REDUCED_ROUTE"; then
    echo "Mathematica reduced-route run failed for C_Euler_final; writing blocked outputs"
    write_blocked "Mathematica reduced-route run failed during C_Euler_final"
    exit 0
  fi
  
  echo "Gate3 reduced-route handoff completed. Outputs:"
  echo "$COSMO_JSON"
  echo "$FINAL_JSON"
  exit 0
fi

echo "Running Mathematica Gate3 handoff for C_Euler_cosmo"
if ! WOLFRAM_HYPEXP_APP_DIR="$HYPEXP_APP_DIR" wolframscript -file "$WL_SCRIPT" C_Euler_cosmo "$COSMO_JSON" "$BRANCH_ID"; then
  echo "Mathematica run failed for C_Euler_cosmo; writing blocked outputs"
  write_blocked "Mathematica run failed during C_Euler_cosmo"
  exit 0
fi

echo "Running Mathematica Gate3 handoff for C_Euler_final"
if ! WOLFRAM_HYPEXP_APP_DIR="$HYPEXP_APP_DIR" wolframscript -file "$WL_SCRIPT" C_Euler_final "$FINAL_JSON" "$BRANCH_ID"; then
  echo "Mathematica run failed for C_Euler_final; writing blocked outputs"
  write_blocked "Mathematica run failed during C_Euler_final"
  exit 0
fi

echo "Gate3 handoff completed. Outputs:"
echo "$COSMO_JSON"
echo "$FINAL_JSON"
