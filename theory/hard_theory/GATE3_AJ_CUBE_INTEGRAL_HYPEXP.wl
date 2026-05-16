(*
Gate 3: Allen-Jacobson cube integral handoff skeleton (Mathematica/HypExp)

This script computes coefficient candidates only.
It must NOT target-match R and must NOT promote R claims.

Hard constraints:
- Weyl channel is forbidden on round S4 because W^2 = 0.
- Im-log causal channel is forbidden unless CTP-to-Euler projection is derived.
- Target values 1.15470 or 1.15428 must not be used.
*)

ClearAll[
  eps, dimReg, Z, u, hplus, hminus, kernel, measure, integrand,
  coefficientName, exportPath, branchId, tryEval, ExportGate3Result,
  routeDirect, integrandU, routeUIntegrate, seriesBefore,
  routeSeriesBeforeIntegrate, routeIntegrateBeforeSeries,
  hypExpAvailable, routeHypExp, routeNumericSanity,
  candidate, poleTerm, finiteTerm, status, blockerMsg, notesAssoc,
  hypExpAppDir, hypExpBrokenDir, resolvedCoefficientQ, m2OverH2, nu
];

(* CLI args:
  wolframscript -file GATE3_AJ_CUBE_INTEGRAL_HYPEXP.wl C_Euler_cosmo output.json branch_id
*)
coefficientName = If[Length[$ScriptCommandLine] >= 2, $ScriptCommandLine[[2]], "C_Euler_cosmo"];
exportPath = If[Length[$ScriptCommandLine] >= 3, $ScriptCommandLine[[3]], "gate3_mathematica_result.json"];
branchId = If[Length[$ScriptCommandLine] >= 4, $ScriptCommandLine[[4]], ""];

If[!MemberQ[{"C_Euler_cosmo", "C_Euler_final"}, coefficientName],
  Print["Invalid coefficient mode. Use C_Euler_cosmo or C_Euler_final."];
  Exit[2];
];

If[
  !MemberQ[
    {"conformal_closed_form", "massive_regulated", "hminus_direct_limit", "hminus_derivative_regularized", "mmc_massless"},
    branchId
  ],
  Print["Invalid or missing branch_id."];
  Exit[2];
];

hypExpAppDir = Environment["WOLFRAM_HYPEXP_APP_DIR"];
hypExpBrokenDir = FileNameJoin[{$HomeDirectory, "HypExp"}];
If[
  StringQ[hypExpAppDir] && hypExpAppDir =!= "" && FileExistsQ[FileNameJoin[{hypExpAppDir, "HypExp.m"}]],
  $Path = Prepend[DeleteCases[$Path, hypExpBrokenDir], hypExpAppDir]
];

(* Regulator and dimension *)
eps = Symbol["epsilon"];
dimReg = 4 - 2 eps;

(* Integration variable and domain *)
Z = Symbol["Z"];

(* Optional variable transform *)
u = Symbol["u"];

(* S4 measure *)
measure = (1 - Z^2)^((dimReg - 3)/2);

(*
Allen-Jacobson scalar kernel:
  Hypergeometric2F1[hplus, hminus, D/2, (1+Z)/2]

hplus/hminus kept symbolic; massless/conformal limit and hminus -> 0 require care.
*)
kernel = Hypergeometric2F1[hplus, hminus, D/2, (1 + Z)/2];
kernel = Hypergeometric2F1[hplus, hminus, dimReg/2, (1 + Z)/2];

(* Cube integrand *)
integrand = kernel^3 * measure;

(* Utility: safe evaluator wrapper *)
tryEval[expr_] := Quiet@Check[expr, $Failed];

resolvedCoefficientQ[expr_] := FreeQ[
  expr,
  Integrate | NIntegrate | Hypergeometric2F1 | hplus | hminus | dimReg | Z | u |
  Undefined | Indeterminate | Infinity | ComplexInfinity | DirectedInfinity
];

ExportGate3Result[coefficientName_, status_, finitePart_, poleTerms_, blocker_, m2OverH2Value_: Null, regulatorRole_: Null] := Module[
  {protectedFlag, assoc},
  protectedFlag = True;
  assoc = <|
    "coefficient_name" -> coefficientName,
    "value" -> If[status === "computed", ToString[finitePart, InputForm], Null],
    "epsilon_pole" -> If[poleTerms === Null, Null, ToString[poleTerms, InputForm]],
    "finite_part" -> If[finitePart === Null, Null, ToString[finitePart, InputForm]],
    "scheme" -> "OR4-approved",
    "regulator" -> "D=4-2epsilon",
    "projection" -> "round_s4_euler",
    "channel" -> "Euler",
    "protected" -> protectedFlag,
    "source_tool" -> "Mathematica+HypExp",
    "source_file" -> "GATE3_AJ_CUBE_INTEGRAL_HYPEXP.wl",
    "branch_id" -> branchId,
    "manual_target_matching" -> False,
    "status" -> status,
    "blocker" -> blocker
  |>;
  (* Add regulator metadata if provided *)
  If[m2OverH2Value =!= Null, assoc["m2_over_h2"] = ToString[m2OverH2Value, InputForm]];
  If[regulatorRole =!= Null, assoc["regulator_role"] = regulatorRole];
  Export[exportPath, assoc, "JSON"];
  Print["Exported Gate3 result: " <> exportPath];
  Print[assoc // InputForm];
];

(* HypExp availability gate *)
Quiet[Needs["HypExp`"]];
hypExpAvailable = MemberQ[$Packages, "HypExp`"];
If[!hypExpAvailable,
  ExportGate3Result[coefficientName, "blocked", Null, Null, "HypExp unavailable"];
  Exit[0];
];

(* Explicit AJ branch prescription gate before kernel construction *)
Which[
  branchId === "conformal_closed_form",
    hplus = dimReg/2;
    hminus = (dimReg - 2)/2,
  branchId === "massive_regulated",
    m2OverH2 = Quiet@Check[ToExpression[Environment["GATE3_M2_OVER_H2"]], Symbol["m2_over_h2"]];
    If[m2OverH2 === Symbol["m2_over_h2"],
      ExportGate3Result[
        coefficientName,
        "blocked",
        Null,
        Null,
        "massive_regulated requires GATE3_M2_OVER_H2 environment variable",
        Null,
        "massive_scalar_ir_regulator"
      ];
      Exit[0];
    ];
    (* Validate that m2OverH2 is numeric and positive *)
    If[!NumericQ[N[m2OverH2]] || N[m2OverH2] <= 0,
      ExportGate3Result[
        coefficientName,
        "blocked",
        Null,
        Null,
        "GATE3_M2_OVER_H2 must be a positive number",
        ToString[m2OverH2, InputForm],
        "massive_scalar_ir_regulator"
      ];
      Exit[0];
    ];
    nu = Sqrt[(dimReg - 1)^2/4 - m2OverH2];
    hplus = (dimReg - 1)/2 + nu;
    hminus = (dimReg - 1)/2 - nu,
  branchId === "hminus_direct_limit",
    ExportGate3Result[
      coefficientName,
      "blocked",
      Null,
      Null,
      "branch hminus_direct_limit blocked until limit prescription is validated"
    ];
    Exit[0],
  branchId === "hminus_derivative_regularized",
    ExportGate3Result[
      coefficientName,
      "blocked",
      Null,
      Null,
      "branch hminus_derivative_regularized selected but derivative prescription is not implemented"
    ];
    Exit[0],
  branchId === "mmc_massless",
    ExportGate3Result[
      coefficientName,
      "blocked",
      Null,
      Null,
      "branch mmc_massless blocked by zero-mode/IR singular structure"
    ];
    Exit[0],
  True,
    ExportGate3Result[coefficientName, "blocked", Null, Null, "branch dispatch failure"];
    Exit[0]
];

routeDirect = tryEval[Integrate[integrand, {Z, -1, 1}, Assumptions -> {eps > 0, -1 <= Z <= 1}]];

(* Z -> u substitution, Z = 2u - 1, dZ = 2 du, u in [0,1] *)
integrandU = Simplify[(integrand /. Z -> (2 u - 1)) * 2, Assumptions -> {u >= 0, u <= 1, eps > 0}];
routeUIntegrate = tryEval[Integrate[integrandU, {u, 0, 1}, Assumptions -> {eps > 0, 0 <= u <= 1}]];

(* Series before integration *)
seriesBefore = tryEval[Normal@Series[integrandU, {eps, 0, 0}]];
routeSeriesBeforeIntegrate = If[
  seriesBefore === $Failed,
  $Failed,
  tryEval[Integrate[seriesBefore, {u, 0, 1}, Assumptions -> {0 <= u <= 1}]]
];

(* Integration before series *)
routeIntegrateBeforeSeries = If[
  routeUIntegrate === $Failed,
  $Failed,
  tryEval[Normal@Series[routeUIntegrate, {eps, 0, 0}]]
];

(* HypExp path - placeholder operation if package loaded *)
routeHypExp = tryEval[
  Module[{tmp},
    tmp = routeUIntegrate;
    If[tmp === $Failed, $Failed, Normal@Series[tmp, {eps, 0, 0}]]
  ]
];

(* High-precision numeric sanity route (diagnostic only) *)
routeNumericSanity = tryEval[
  NIntegrate[
    Evaluate[integrandU /. {hplus -> 3/2, hminus -> 1/2, eps -> 10^-3}],
    {u, 0, 1},
    WorkingPrecision -> 80,
    PrecisionGoal -> 20,
    AccuracyGoal -> 20,
    Method -> "GlobalAdaptive"
  ]
];

candidate = Which[
  routeHypExp =!= $Failed, routeHypExp,
  routeIntegrateBeforeSeries =!= $Failed, routeIntegrateBeforeSeries,
  routeSeriesBeforeIntegrate =!= $Failed, routeSeriesBeforeIntegrate,
  routeUIntegrate =!= $Failed, routeUIntegrate,
  routeDirect =!= $Failed, routeDirect,
  True, $Failed
];

If[candidate === $Failed,
  ExportGate3Result[
    coefficientName,
    "blocked",
    Null,
    Null,
    "Integrate failed across all routes for AJ cube integral"
  ];
  Exit[0];
];

poleTerm = tryEval[SeriesCoefficient[candidate, {eps, 0, -1}]];
finiteTerm = tryEval[SeriesCoefficient[candidate, {eps, 0, 0}]];

If[
  poleTerm === $Failed || finiteTerm === $Failed || finiteTerm === Null ||
    !resolvedCoefficientQ[finiteTerm] || !resolvedCoefficientQ[poleTerm],
  ExportGate3Result[
    coefficientName,
    "blocked",
    Null,
    Null,
    "Series or Laurent extraction did not yield resolved coefficient terms"
  ];
  Exit[0];
];

ExportGate3Result[coefficientName, "computed", finiteTerm, poleTerm, Null];
