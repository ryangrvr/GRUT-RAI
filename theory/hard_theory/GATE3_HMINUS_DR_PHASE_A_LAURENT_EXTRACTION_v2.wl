(*
  Gate 3 Hminus-Derivative-Regularized Phase A: Laurent Extraction (Simplified v2)
  
  Purpose: Compute I(h_-, epsilon) and extract Laurent expansion
  Uses built-in Hypergeometric2F1 instead of HypExp for robustness.
  
  Specification version: gate3-hminus-dr-spec-v1.0
  Date: May 16, 2026
*)

Print[""];
Print["Gate 3 Phase A: Laurent Extraction (v2 - Simplified)"];
Print["Specification: gate3-hminus-dr-spec-v1.0"];
Print["Start time: " <> DateString[]];
Print[""];

(* ===== Setup ===== *)

script_dir = DirectoryName[$InputFileName];
output_dir = FileNameJoin[{script_dir, "gate3_outputs"}];
If[!DirectoryQ[output_dir], CreateDirectory[output_dir, CreateIntermediateDirectories -> True]];
output_file = FileNameJoin[{output_dir, "gate3_hminus_dr_laurent_extraction.json"}];

Print["Output directory: " <> output_dir];
Print["Output file: " <> output_file];
Print[""];

(* ===== Configuration ===== *)

h_minus_values = {0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001};
epsilon_values = {0.01, 0.005, 0.002, 0.001};

Print["h_minus values: " <> ToString[h_minus_values]];
Print["epsilon values: " <> ToString[epsilon_values]];
Print["Total samples to compute: " <> ToString[Length[h_minus_values] * Length[epsilon_values]]];
Print[""];

(* ===== Define Integral ===== *)

defineIntegral[alpha_, eps_] := Module[
  {D_val, hplus, prefactor, integrand},
  
  D_val = 4 - 2*eps;
  hplus = D_val - 1;
  
  prefactor = 2 * 4^((D_val - 3)/2);
  
  integrand = Hypergeometric2F1[hplus, alpha, D_val/2, u]^3 * 
              u^((D_val - 3)/2) * (1 - u)^((D_val - 3)/2);
  
  prefactor * integrand
];

Print["Integral definition loaded"];
Print[""];

(* ===== Sample Collection ===== *)

Print["Beginning sample collection..."];
Print[""];

samples = {};
successful_count = 0;

(* Outer loop over h_minus *)
Do[
  
  (* Inner loop over epsilon *)
  Do[
    sample_num = (Position[h_minus_values, h_val][[1, 1]] - 1) * Length[epsilon_values] + Position[epsilon_values, eps_val][[1, 1]];
    
    Print["Sample " <> ToString[sample_num] <> " of " <> ToString[Length[h_minus_values] * Length[epsilon_values]] <> 
          ": h_- = " <> ToString[h_val] <> ", eps = " <> ToString[eps_val]];
    
    (* Numerically integrate *)
    result = Quiet[
      NIntegrate[
        defineIntegral[h_val, eps_val],
        {u, 0, 1},
        WorkingPrecision -> 50,
        PrecisionGoal -> 15,
        MaxRecursion -> 20,
        Method -> "AdaptiveQuadrature"
      ],
      {Power::infy, Infinity::indet, NIntegrate::ncvb}
    ];
    
    If[NumberQ[result] && !FailureQ[result],
      AppendTo[samples, {h_val, eps_val, result}];
      successful_count++;
      Print["  Result: " <> ToString[N[result, 10]]],
      Print["  FAILED: " <> ToString[result]]
    ];
    
  , {eps_val, epsilon_values}],
  
  {h_val, h_minus_values}
];

Print[""];
Print["Sample collection complete"];
Print["Total samples: " <> ToString[Length[samples]]];
Print["Successful samples: " <> ToString[successful_count]];
Print[""];

(* ===== Laurent Fitting in h_- ===== *)

Print["Performing Laurent expansion fitting in h_-..."];
Print[""];

successful_samples = Select[samples, NumberQ[#[[3]]] &];

If[Length[successful_samples] < 5,
  Print["ERROR: Insufficient samples (" <> ToString[Length[successful_samples]] <> " < 5)"];
  Print["Cannot proceed with fitting."];
  Quit[1]
];

(* Fit Laurent expansion for each epsilon *)
laurent_coefficients = <||>;
pole_order = 0;

Do[
  (* Extract data for this epsilon *)
  data_this_eps = Select[successful_samples, #[[2]] == eps_val &];
  
  Print["Epsilon " <> ToString[eps_val] <> ": " <> ToString[Length[data_this_eps]] <> " samples"];
  
  If[Length[data_this_eps] >= 3,
    (* Prepare data as pairs *)
    data_pairs = Map[{#[[1]], #[[3]]} &, data_this_eps];
    
    (* Fit polynomial up to degree 3 in h *)
    fit = LinearModelFit[data_pairs, {1, h, h^2, h^3}, h, IncludeConstantBasis -> False];
    
    (* Extract coefficients *)
    fit_normal = Normal[fit];
    coeff_0 = fit_normal /. h -> 0;
    coeff_1 = (D[fit_normal, h] /. h -> 0);
    coeff_2 = (D[fit_normal, {h, 2}] /. h -> 0) / 2;
    coeff_3 = (D[fit_normal, {h, 3}] /. h -> 0) / 6;
    
    laurent_coefficients[eps_val] = <|
      "A_0" -> N[coeff_0, 15],
      "A_1" -> N[coeff_1, 15],
      "A_2" -> N[coeff_2, 15],
      "A_3" -> N[coeff_3, 15],
      "fit_r2" -> fit["RSquared"]
    |>;
    
    (* Track pole order *)
    If[Abs[coeff_1] > 0.1 * Abs[coeff_0], pole_order = Max[pole_order, 1]];
    
    Print["  A_0 = " <> ToString[N[coeff_0, 10]]];
    Print["  A_1 = " <> ToString[N[coeff_1, 10]]];
    Print["  R² = " <> ToString[fit["RSquared"]]];
  ,
    Print["  WARNING: Insufficient data for this epsilon"]
  ];
  
  Print[""];
  
, {eps_val, epsilon_values}];

Print["Fitted " <> ToString[Length[laurent_coefficients]] <> " epsilon values"];
Print["Empirically determined pole order: " <> ToString[pole_order]];
Print[""];

(* ===== Build Output JSON ===== *)

Print["Building output JSON..."];

(* Build I_samples dictionary *)
i_samples_dict = <||>;
Do[
  key = StringJoin[ToString[N[sample[[1]], 5]], "_", ToString[N[sample[[2]], 5]]];
  i_samples_dict[key] = N[sample[[3]], 20],
  {sample, successful_samples}
];

(* Build coefficients dictionary *)
coeff_dict = <||>;
Do[
  coeff_dict[ToString[eps_val]] = laurent_coefficients[eps_val],
  {eps_val, epsilon_values}
];

output_json = <|
  "spec_version" -> "1.0",
  "date" -> DateString[],
  "h_minus_values" -> h_minus_values,
  "epsilon_values" -> epsilon_values,
  "total_samples" -> Length[samples],
  "successful_samples" -> Length[successful_samples],
  "I_samples" -> i_samples_dict,
  "laurent_fit" -> <|
    "pole_order" -> pole_order,
    "coefficients" -> coeff_dict,
    "fit_quality" -> <|
      "method" -> "LinearModelFit polynomial degree 3",
      "avg_r2" -> If[Length[laurent_coefficients] > 0, 
                     N[Mean[Map[#["fit_r2"] &, Values[laurent_coefficients]]], 10],
                     0]
    |>
  |>
|>;

(* ===== Write Output ===== *)

Print["Writing output to file..."];

Export[output_file, output_json, "JSON"];

If[FileExistsQ[output_file],
  Print["SUCCESS: Output written to " <> output_file];
  Print["File size: " <> ToString[FileByteCount[output_file]] <> " bytes"],
  Print["ERROR: Output file not created"]
];

Print[""];
Print["============ Phase A COMPLETE ============"];
Print["Specification: gate3-hminus-dr-spec-v1.0"];
Print["Output: " <> output_file];
Print["End time: " <> DateString[]];
Print[""];
