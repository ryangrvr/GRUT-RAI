(*
  Gate 3 Hminus-Derivative-Regularized Phase A: Laurent Extraction
  
  Purpose: Compute I(h_-, epsilon) for multiple h_- values and extract Laurent expansion
  
  Specification version: gate3-hminus-dr-spec-v1.0
  Date: May 15, 2026
  
  This script:
  1. Loads HypExp package
  2. Defines the full cube integral with h_- = alpha as free parameter
  3. Samples at h_- in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
  4. For each h_-, computes I(h_-, epsilon) for epsilon in [0.01, 0.005, 0.002, 0.001]
  5. Fits Laurent expansion I(h_-, epsilon) = sum_k A_k(epsilon) h_-^k
  6. Outputs gate3_hminus_dr_laurent_extraction.json
*)

(* ===== Setup & Package Loading ===== *)

(* Print header *)
Print["Gate 3 Phase A: Laurent Extraction in h_- (hminus_derivative_regularized)"];
Print["Specification: gate3-hminus-dr-spec-v1.0"];
Print["Start time: " <> DateString[]];

(* Load HypExp *)
If[!MemberQ[$ContextPath, "HypExp`"], AppendTo[$ContextPath, "HypExp`"]];
Needs["HypExp`"];
Print["HypExp package loaded successfully"];

(* ===== Constants & Configuration ===== *)

h_minus_values = {0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001};
epsilon_values = {0.01, 0.005, 0.002, 0.001};

(* Output directory *)
script_dir = If[StringQ[$InputFileName], DirectoryName[$InputFileName], DirectoryName[NotebookFileName[]]];
output_dir = FileNameJoin[{script_dir, "gate3_outputs"}];
If[!DirectoryQ[output_dir], CreateDirectory[output_dir]];
output_file = FileNameJoin[{output_dir, "gate3_hminus_dr_laurent_extraction.json"}];

Print["Output will be written to: " <> output_file];

(* ===== Define Integral ===== *)

(* 
  Allen-Jacobson branch for hminus_derivative_regularized:
  h_+ = D - 1 (massless minimally coupled)
  h_- = alpha (regulator, treated as free parameter)
  D = 4 - 2*epsilon
  
  Full cube integral (u-space):
  I(alpha, epsilon) = 2 * 4^{(D-3)/2} * Integral_0^1 
                      2F1(h_+, alpha; D/2; u)^3 * u^{(D-3)/2} * (1-u)^{(D-3)/2} du
*)

defineIntegral[alpha_, eps_] := Module[
  {D, hplus, hminus, prefactor, integrand},
  
  D = 4 - 2*eps;
  hplus = D - 1;
  hminus = alpha;
  
  prefactor = 2 * 4^((D - 3)/2);
  
  integrand = Hypergeometric2F1[hplus, hminus, D/2, u]^3 * 
              u^((D - 3)/2) * (1 - u)^((D - 3)/2);
  
  prefactor * integrand
];

(* ===== Sample Collection ===== *)

Print["Beginning sample collection..."];
samples = {};
sample_count = 0;

Do[
  Do[
    sample_count++;
    If[Mod[sample_count, 10] == 0, Print["Sample " <> ToString[sample_count] <> " of 28..."]];
    
    (* Numerically integrate *)
    result = Quiet[
      NIntegrate[
        defineIntegral[h_minus, eps],
        {u, 0, 1},
        WorkingPrecision -> 50,
        PrecisionGoal -> 15,
        MaxRecursion -> 20,
        Method -> "AdaptiveQuadrature"
      ],
      {Power::infy, Infinity::indet}
    ];
    
    If[NumberQ[result],
      AppendTo[samples, {h_minus, eps, result}],
      AppendTo[samples, {h_minus, eps, "failed"}]
    ];
    
  , {eps, epsilon_values}],
  {h_minus, h_minus_values}
];

Print["Completed " <> ToString[Length[samples]] <> " samples"];

(* ===== Laurent Fitting in h_- ===== *)

Print["Performing Laurent expansion fitting in h_-..."];

(* Extract successful samples *)
successful_samples = Select[samples, NumberQ[#[[3]]] &];
Print["Successful samples: " <> ToString[Length[successful_samples]] <> " / " <> ToString[Length[samples]]];

If[Length[successful_samples] < 10,
  Print["WARNING: Insufficient successful samples for fitting. Aborting."];
  Abort[]
];

(* Fit Laurent expansion for each epsilon: I(h_-, eps) = sum_k A_k(eps) * h_-^k *)
laurent_coefficients = <||>;

Do[
  (* Extract data for this epsilon *)
  data_this_eps = Select[successful_samples, #[[2]] == eps &];
  
  If[Length[data_this_eps] >= 5,
    (* Use polynomial fit up to order 3 in h_- *)
    fit = LinearModelFit[
      {#[[1]], #[[3]]} & /@ data_this_eps,
      {1, h, h^2, h^3},
      h
    ];
    
    (* Extract coefficients *)
    coeff_0 = Normal[fit] /. h -> 0;
    coeff_1 = D[Normal[fit], h] /. h -> 0;
    coeff_2 = D[Normal[fit], {h, 2}]/2! /. h -> 0;
    coeff_3 = D[Normal[fit], {h, 3}]/3! /. h -> 0;
    
    laurent_coefficients[eps] = {
      "A_0" -> coeff_0,
      "A_1" -> coeff_1,
      "A_2" -> coeff_2,
      "A_3" -> coeff_3,
      "fit_r2" -> fit["RSquared"]
    };
  ],
  {eps, epsilon_values}
];

Print["Fitted Laurent coefficients for " <> ToString[Length[laurent_coefficients]] <> " epsilon values"];

(* Determine pole order empirically *)
(* Check if A_-1 coefficient is needed *)
pole_order = 0;
Do[
  If[Abs[laurent_coefficients[eps]["A_1"]] > 0.1 * Abs[laurent_coefficients[eps]["A_0"]],
    pole_order = Max[pole_order, 1]
  ],
  {eps, epsilon_values}
];

Print["Empirically determined pole order: " <> ToString[pole_order]];

(* ===== Output JSON ===== *)

Print["Formatting output JSON..."];

output_json = <|
  "spec_version" -> "1.0",
  "date" -> DateString[],
  "h_minus_values" -> h_minus_values,
  "epsilon_values" -> epsilon_values,
  "total_samples" -> Length[samples],
  "successful_samples" -> Length[successful_samples],
  "I_samples" -> <|
    StringJoin[ToString[N[#[[1]], 5]], ", ", ToString[N[#[[2]], 5]]] -> N[#[[3]], 20]
    & /@ successful_samples
  |>,
  "laurent_fit" -> <|
    "pole_order" -> pole_order,
    "coefficients" -> <|
      ToString[eps] -> laurent_coefficients[eps]
      & /@ epsilon_values
    |>,
    "fit_quality" -> <|
      "method" -> "LinearModelFit polynomial degree 3",
      "avg_r2" -> Mean[Map[#"fit_r2" &, Values[laurent_coefficients]]]
    |>
  |>
|>;

(* Write JSON *)
json_string = ExportString[output_json, "JSON"];
Put[json_string, output_file];

Print["Output written to: " <> output_file];
Print["File size: " <> ToString[FileByteCount[output_file]] <> " bytes"];

(* ===== Completion ===== *)

Print[""];
Print["============ Phase A COMPLETE ============"];
Print["Specification: gate3-hminus-dr-spec-v1.0"];
Print["Output: " <> output_file];
Print["End time: " <> DateString[]];
Print[""];

(* Return output file path for shell wrapper *)
Print[output_file];
