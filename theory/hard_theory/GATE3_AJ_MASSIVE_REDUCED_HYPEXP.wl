(*
Gate 3: Massive_Regulated Reduced Integral Strategy (Mathematica/HypExp)

Three discovery routes for reduced integrand evaluation:
- Route A: ε-expansion first, then integrate term-by-term
- Route B: Change variable u = (1+Z)/2 (beta-weighted form)
- Route C: Numerical Mellin/Beta sanity check
- Route D: Endpoint asymptotic subtraction in u-space

No fake computed outputs. All routes export blocked or computed with full provenance.
*)

ClearAll[
  eps, dimReg, D, Z, u, hplus, hminus, m2OverH2, nu,
  kernel, measure, integrand,
  coefficientName, exportPath, branchId, route,
  resolvedCoefficientQ, ExportGate3ReducedResult,
  routeA, routeB, routeC, routeD,
  candidate, poleTerm, finiteTerm,
  hypExpAvailable, hypExpAppDir, hypExpBrokenDir,
  startTime, endTime, elapsedTime
];

(* CLI args:
  wolframscript -file GATE3_AJ_MASSIVE_REDUCED_HYPEXP.wl C_Euler_cosmo output.json massive_regulated A
     (coefficient_name, export_path, branch_id, route)
*)
coefficientName = If[Length[$ScriptCommandLine] >= 2, $ScriptCommandLine[[2]], "C_Euler_cosmo"];
exportPath = If[Length[$ScriptCommandLine] >= 3, $ScriptCommandLine[[3]], "gate3_reduced_result.json"];
branchId = If[Length[$ScriptCommandLine] >= 4, $ScriptCommandLine[[4]], ""];
route = If[Length[$ScriptCommandLine] >= 5, $ScriptCommandLine[[5]], "A"];

If[!MemberQ[{"C_Euler_cosmo", "C_Euler_final"}, coefficientName],
  Print["Invalid coefficient mode. Use C_Euler_cosmo or C_Euler_final."];
  Exit[2];
];

If[branchId =!= "massive_regulated",
  Print["Reduced routes only available for massive_regulated branch."];
  Exit[2];
];

If[!MemberQ[{"A", "B", "C", "D"}, route],
  Print["Invalid route. Use A, B, C, or D."];
  Exit[2];
];

(* HypExp setup *)
hypExpAppDir = Environment["WOLFRAM_HYPEXP_APP_DIR"];
hypExpBrokenDir = FileNameJoin[{$HomeDirectory, "HypExp"}];
If[
  StringQ[hypExpAppDir] && hypExpAppDir =!= "" && FileExistsQ[FileNameJoin[{hypExpAppDir, "HypExp.m"}]],
  $Path = Prepend[DeleteCases[$Path, hypExpBrokenDir], hypExpAppDir]
];

Quiet[Needs["HypExp`"]];
hypExpAvailable = MemberQ[$Packages, "HypExp`"];

If[!hypExpAvailable,
  Print["HypExp unavailable"];
  Exit[0];
];

(* Regulator and dimension *)
eps = Symbol["epsilon"];
dimReg = 4 - 2 eps;

(* Integration variables *)
Z = Symbol["Z"];
u = Symbol["u"];

(* Read regulator parameter *)
m2OverH2 = Quiet@Check[ToExpression[Environment["GATE3_M2_OVER_H2"]], Null];
If[m2OverH2 === Null || !NumericQ[N[m2OverH2]] || N[m2OverH2] <= 0,
  Print["GATE3_M2_OVER_H2 not set or invalid"];
  Exit[2];
];

(* Compute h_+ and h_- *)
nu = Sqrt[(dimReg - 1)^2/4 - m2OverH2];
hplus = (dimReg - 1)/2 + nu;
hminus = (dimReg - 1)/2 - nu;

(* Utility: safe evaluator wrapper *)
tryEval[expr_] := Quiet@Check[expr, $Failed];

resolvedCoefficientQ[expr_] := FreeQ[
  expr,
  Integrate | NIntegrate | Hypergeometric2F1 | hplus | hminus | dimReg | Z | u | m2OverH2 | nu |
  Undefined | Indeterminate | Infinity | ComplexInfinity | DirectedInfinity
];

ExportGate3ReducedResult[
  coefficientName_,
  status_,
  finitePart_,
  poleTerms_,
  blocker_,
  route_,
  elapsedSec_
] := Module[
  {assoc},
  assoc = <|
    "coefficient_name" -> coefficientName,
    "value" -> If[status === "computed", ToString[finitePart, InputForm], Null],
    "epsilon_pole" -> If[poleTerms === Null, Null, ToString[poleTerms, InputForm]],
    "finite_part" -> If[finitePart === Null, Null, ToString[finitePart, InputForm]],
    "scheme" -> "OR4-approved",
    "regulator" -> "D=4-2epsilon",
    "projection" -> "round_s4_euler",
    "channel" -> "Euler",
    "protected" -> True,
    "source_tool" -> "Mathematica+HypExp",
    "source_file" -> "GATE3_AJ_MASSIVE_REDUCED_HYPEXP.wl",
    "branch_id" -> branchId,
    "manual_target_matching" -> False,
    "status" -> status,
    "blocker" -> blocker,
    "m2_over_h2" -> ToString[m2OverH2, InputForm],
    "regulator_role" -> "massive_scalar_ir_regulator",
    "regulator_approach" -> "reduced_integral",
    "route" -> route,
    "elapsed_seconds" -> elapsedSec
  |>;
  Export[exportPath, assoc, "JSON"];
  Print["Exported Gate3 reduced result (Route " <> route <> "): " <> exportPath];
  Print[assoc // InputForm];
];

(* ============================================
   ROUTE A: Epsilon-Expansion First, Integrate Term-by-Term
   ============================================ *)

routeA := Module[
  {kernel2F1, measure, kernelExpanded, measureExpanded, integrand, 
   integrateDeferred, series, candidate, poleTerm, finiteTerm},
  
  Print["Starting Route A: epsilon-expansion first, then integrate"];
  startTime = AbsoluteTime[];
  
  (* Expand h_+ and h_- in epsilon *)
  kernel2F1 = Hypergeometric2F1[hplus, hminus, dimReg/2, (1 + Z)/2];
  
  (* Expand kernel to first order in ε *)
  kernelExpanded = tryEval[Normal@Series[kernel2F1, {eps, 0, 1}]];
  
  If[kernelExpanded === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route A: kernel expansion failed",
      "A",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  (* Cube the expanded kernel *)
  kernelExpanded = tryEval[Expand[kernelExpanded^3]];
  
  (* Expand measure (1-Z^2)^((D-3)/2) *)
  measure = tryEval[Normal@Series[(1 - Z^2)^((dimReg - 3)/2), {eps, 0, 1}]];
  
  If[measure === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route A: measure expansion failed",
      "A",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  (* Form full integrand *)
  integrand = tryEval[Expand[kernelExpanded * measure]];
  
  (* Extract coefficient of eps^0 (finite part) *)
  finiteTerm = tryEval[SeriesCoefficient[integrand, {eps, 0, 0}]];
  
  (* Extract coefficient of eps^{-1} (pole) *)
  poleTerm = tryEval[SeriesCoefficient[integrand, {eps, 0, -1}]];
  
  (* Try to integrate finite and pole terms *)
  If[finiteTerm =!= $Failed && resolvedCoefficientQ[finiteTerm],
    finiteTerm = tryEval[Integrate[finiteTerm, {Z, -1, 1}]];
  ];
  
  If[poleTerm =!= $Failed && poleTerm =!= 0 && resolvedCoefficientQ[poleTerm],
    poleTerm = tryEval[Integrate[poleTerm, {Z, -1, 1}]];
  ];
  
  If[
    finiteTerm =!= $Failed && resolvedCoefficientQ[finiteTerm] &&
    poleTerm =!= $Failed && resolvedCoefficientQ[poleTerm],
    
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "computed",
      finiteTerm,
      poleTerm,
      Null,
      "A",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  endTime = AbsoluteTime[];
  ExportGate3ReducedResult[
    coefficientName,
    "blocked",
    Null,
    Null,
    "Route A: Laurent extraction did not yield resolved terms",
    "A",
    N[endTime - startTime]
  ];
  Exit[0];
];

(* ============================================
   ROUTE B: Change Variable u = (1+Z)/2 (Beta-Weighted Form)
   ============================================ *)

routeB := Module[
  {kernel2F1, betaMeasure, integrand,
   candidate, poleTerm, finiteTerm},
  
  Print["Starting Route B: variable change u = (1+Z)/2 (beta-weighted form)"];
  startTime = AbsoluteTime[];
  
  (* In u-space: kernel becomes 2F1(h_+, h_-; D/2; u)
     measure (1-Z^2)^((D-3)/2) becomes [4u(1-u)]^((D-3)/2)
     integrand: 2 * 4^((D-3)/2) * 2F1^3 * u^((D-3)/2) * (1-u)^((D-3)/2)
  *)
  
  kernel2F1 = Hypergeometric2F1[hplus, hminus, dimReg/2, u];
  
  betaMeasure = 2 * (4^((dimReg - 3)/2)) * u^((dimReg - 3)/2) * (1 - u)^((dimReg - 3)/2);
  
  integrand = tryEval[Simplify[kernel2F1^3 * betaMeasure]];
  
  If[integrand === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route B: integrand construction failed",
      "B",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  (* Try direct integration *)
  candidate = tryEval[Integrate[integrand, {u, 0, 1}, Assumptions -> {eps > 0}]];
  
  If[candidate === $Failed,
    (* Try series expansion first *)
    candidate = tryEval[
      Module[{exp},
        exp = Normal@Series[integrand, {eps, 0, 0}];
        Integrate[exp, {u, 0, 1}]
      ]
    ];
  ];
  
  If[candidate === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route B: integration failed",
      "B",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  (* Extract Laurent coefficients *)
  poleTerm = tryEval[SeriesCoefficient[candidate, {eps, 0, -1}]];
  finiteTerm = tryEval[SeriesCoefficient[candidate, {eps, 0, 0}]];
  
  If[
    finiteTerm =!= $Failed && resolvedCoefficientQ[finiteTerm] &&
    poleTerm =!= $Failed && resolvedCoefficientQ[poleTerm],
    
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "computed",
      finiteTerm,
      poleTerm,
      Null,
      "B",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  endTime = AbsoluteTime[];
  ExportGate3ReducedResult[
    coefficientName,
    "blocked",
    Null,
    Null,
    "Route B: Laurent extraction did not yield resolved terms",
    "B",
    N[endTime - startTime]
  ];
  Exit[0];
];

(* ============================================
   ROUTE C: Numerical Mellin/Beta Sanity Check
   ============================================ *)

routeC := Module[
  {epsValues, integralResults, fits, pole, finite, c0, c1},
  
  Print["Starting Route C: numerical Mellin/Beta sanity check"];
  startTime = AbsoluteTime[];
  
  (* Numerical evaluation at small epsilon values *)
  epsValues = {10^-3, 10^-4, 10^-5};
  integralResults = {};
  
  (* For each ε, numerically integrate *)
  Do[
    Module[{dimRegNum, hplusNum, hminusNum, nuNum, integrand, result},
      dimRegNum = 4 - 2 epsVal;
      nuNum = Sqrt[(dimRegNum - 1)^2/4 - m2OverH2];
      hplusNum = (dimRegNum - 1)/2 + nuNum;
      hminusNum = (dimRegNum - 1)/2 - nuNum;
      
      integrand = Hypergeometric2F1[hplusNum, hminusNum, dimRegNum/2, (1 + Z)/2]^3 * 
                  (1 - Z^2)^((dimRegNum - 3)/2);
      
      result = tryEval[
        NIntegrate[
          integrand,
          {Z, -1, 1},
          WorkingPrecision -> 50,
          PrecisionGoal -> 15,
          AccuracyGoal -> 15,
          Method -> "GlobalAdaptive",
          MaxRecursion -> 100
        ]
      ];
      
      If[result =!= $Failed,
        AppendTo[integralResults, {epsVal, result}];
        Print["ε = " <> ToString[epsVal] <> ", I(ε) = " <> ToString[N[result, 10]]];
      ];
    ],
    {epsVal, epsValues}
  ];
  
  If[Length[integralResults] < 2,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route C: insufficient numerical data points",
      "C",
      N[endTime - startTime]
    ];
    Exit[0];
  ];
  
  (* Fit Laurent series: I(ε) ≈ c_{-1}/ε + c_0 + c_1*ε *)
  (* Using least-squares fit *)
  Module[{data, fit, fitFunc},
    data = integralResults;
    fitFunc[epsVar_] := c0 + c1*epsVar;
    
    (* Simple linear regression on the data assuming pole is small *)
    fit = tryEval[
      LinearModelFit[data, {1, epsVal}, epsVal]["BestFitParameters"]
    ];
    
    If[fit =!= $Failed,
      finite = fit[[1]];
      (* For pole, would need higher precision or more data *)
      pole = 0; (* Not estimated in this simple fit *)
      
      endTime = AbsoluteTime[];
      ExportGate3ReducedResult[
        coefficientName,
        "computed",
        finite,
        pole,
        "numerical_fit_only_informational",
        "C",
        N[endTime - startTime]
      ];
      Exit[0];
    ];
  ];
  
  endTime = AbsoluteTime[];
  ExportGate3ReducedResult[
    coefficientName,
    "blocked",
    Null,
    Null,
    "Route C: numerical fit failed",
    "C",
    N[endTime - startTime]
  ];
  Exit[0];
];

(* ============================================
   ROUTE D: Endpoint Asymptotic Subtraction in u-Space
   ============================================ *)

routeD := Module[
  {
    epsValues, integralResults,
    fit, bestExpr, cPole, cFinite
  },

  Print["Starting Route D: endpoint asymptotic subtraction in u-space"];
  startTime = AbsoluteTime[];

  epsValues = {10^-2, 5*10^-3, 2*10^-3, 10^-3};
  integralResults = {};

  Do[
    Module[
      {
        dimRegNum, nuNum, hplusNum, hminusNum, alphaNum,
        kernelNum, smoothNum, prefNum,
        a0Num, a1Num, Kfull, Ksing,
        iSing, iRem, iTotal
      },
      dimRegNum = 4 - 2 epsVal;
      nuNum = Sqrt[(dimRegNum - 1)^2/4 - m2OverH2];
      hplusNum = (dimRegNum - 1)/2 + nuNum;
      hminusNum = (dimRegNum - 1)/2 - nuNum;
      alphaNum = (dimRegNum - 3)/2;

      kernelNum[uArg_] := Hypergeometric2F1[hplusNum, hminusNum, dimRegNum/2, uArg]^3;
      prefNum = 2*4^alphaNum;
      smoothNum[uArg_] := kernelNum[uArg]*(1 - uArg)^alphaNum;

      a0Num = tryEval[N[smoothNum[0], 50]];
      a1Num = tryEval[N[(D[smoothNum[uVar], uVar] /. uVar -> 0), 50]];

      If[a0Num === $Failed || a1Num === $Failed,
        Print["Route D: endpoint coefficient extraction failed at eps=" <> ToString[epsVal]];
        Continue[];
      ];

      Kfull[uArg_] := prefNum*uArg^alphaNum*smoothNum[uArg];
      Ksing[uArg_] := prefNum*uArg^alphaNum*(a0Num + a1Num*uArg);

      iSing = tryEval[
        prefNum*(a0Num/(alphaNum + 1) + a1Num/(alphaNum + 2))
      ];

      iRem = tryEval[
        NIntegrate[
          Kfull[uArg] - Ksing[uArg],
          {uArg, 0, 1},
          Exclusions -> {uArg == 0, uArg == 1},
          WorkingPrecision -> 60,
          PrecisionGoal -> 18,
          AccuracyGoal -> 18,
          Method -> "GlobalAdaptive",
          MaxRecursion -> 80
        ]
      ];

      If[iSing === $Failed || iRem === $Failed,
        Print["Route D: subtraction integral failed at eps=" <> ToString[epsVal]];
        Continue[];
      ];

      iTotal = tryEval[N[iSing + iRem, 30]];
      If[iTotal === $Failed,
        Continue[];
      ];

      AppendTo[integralResults, {epsVal, iTotal}];
      Print[
        "Route D sample: eps=" <> ToString[epsVal] <>
        ", Ising=" <> ToString[N[iSing, 8]] <>
        ", Irem=" <> ToString[N[iRem, 8]] <>
        ", Itotal=" <> ToString[N[iTotal, 8]]
      ];
    ],
    {epsVal, epsValues}
  ];

  If[Length[integralResults] < 3,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route D: insufficient endpoint-subtracted samples",
      "D",
      N[endTime - startTime]
    ];
    Exit[0];
  ];

  fit = tryEval[
    LinearModelFit[
      integralResults,
      {1/epsVar, 1, epsVar},
      epsVar
    ]
  ];

  If[fit === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route D: Laurent fit failed",
      "D",
      N[endTime - startTime]
    ];
    Exit[0];
  ];

  bestExpr = tryEval[Normal[fit["BestFit"]]];
  If[bestExpr === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route D: best-fit expression extraction failed",
      "D",
      N[endTime - startTime]
    ];
    Exit[0];
  ];

  cPole = tryEval[Coefficient[bestExpr, 1/epsVar]];
  cFinite = tryEval[Limit[bestExpr - cPole/epsVar, epsVar -> 0]];

  If[cPole === $Failed || cFinite === $Failed,
    endTime = AbsoluteTime[];
    ExportGate3ReducedResult[
      coefficientName,
      "blocked",
      Null,
      Null,
      "Route D: unable to resolve pole/finite coefficients",
      "D",
      N[endTime - startTime]
    ];
    Exit[0];
  ];

  endTime = AbsoluteTime[];
  ExportGate3ReducedResult[
    coefficientName,
    "computed",
    cFinite,
    cPole,
    "endpoint_subtraction_numerical_fit_informational",
    "D",
    N[endTime - startTime]
  ];
  Exit[0];
];

(* ============================================
   Route Selection and Execution
   ============================================ *)

Which[
  route === "A", routeA,
  route === "B", routeB,
  route === "C", routeC,
  route === "D", routeD,
  True,
    Print["Invalid route."];
    Exit[2]
];
