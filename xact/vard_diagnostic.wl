(* ================================================================
   VarD Diagnostic Suite — Finding the Working Approach
   ================================================================
   RUN: wolframscript -file xact/vard_diagnostic.wl
   ================================================================ *)

Print[""];
Print["================================================================"];
Print["VarD DIAGNOSTIC SUITE"];
Print["================================================================"];
Print[""];

(* ----------------------------------------------------------------
   Load xAct
   ---------------------------------------------------------------- *)
Print["[0] Loading xAct..."];
Quiet[
  Needs["xAct`xTensor`"];
, {General::argtu, UpSetDelayed::write, SetDelayed::write, General::stop}];
Print["    xTensor loaded."];

(* ----------------------------------------------------------------
   Define manifold and metric
   ---------------------------------------------------------------- *)
Print[""];
Print["[1] Defining manifold and metric..."];
DefManifold[M4, 4, IndexRange[a, p]];
DefMetric[-1, gg[-a, -b], CD,
  PrintAs -> "g",
  SymbolOfCovD -> {";", "\[Del]"}];
DefTensor[phi[], M4, PrintAs -> "Phi"];
Print["    Done."];

(* ----------------------------------------------------------------
   TEST 1: Ricci scalar — THE canonical xAct example
   This MUST work if xAct is functioning properly.
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 1: VarD of Ricci scalar (Einstein equations)"];
Print["================================================================"];
Print["  Computing VarD[RicciScalarCD[], CD][gg[-a,-b]]..."];

test1 = Quiet[VarD[RicciScalarCD[], CD][gg[-a, -b]]];
Print["  Result: ", test1];
Print["  Is zero? ", test1 === 0];
If[test1 =!= 0,
  test1c = test1 // ContractMetric[#, gg]& // ToCanonical;
  Print["  Canonical: ", test1c];
];

(* ----------------------------------------------------------------
   TEST 2: VarD with gg[-a,-b] (metric, lower indices)
   vs gg[a,b] (inverse metric, upper indices)
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 2: Kinetic term — explicit metric form"];
Print["================================================================"];

(* Form A: Explicit metric contraction *)
Print["  Form A: L = -1/2 gg[c,d] CD[-c][phi] CD[-d][phi]"];
Lkin2A = -1/2 gg[c, d] CD[-c][phi[]] CD[-d][phi[]];
Print["  Expression: ", Lkin2A];
Print["  ScalarQ: ", xAct`xTensor`ScalarQ[Lkin2A]];

Print["  2A-i:  VarD[L, CD][gg[-a,-b]]..."];
r2Ai = Quiet[VarD[Lkin2A, CD][gg[-a, -b]]];
Print["         Result: ", r2Ai];
Print["         Is zero? ", r2Ai === 0];

Print["  2A-ii: VarD[L, CD][gg[a,b]]..."];
r2Aii = Quiet[VarD[Lkin2A, CD][gg[a, b]]];
Print["         Result: ", r2Aii];
Print["         Is zero? ", r2Aii === 0];

(* ----------------------------------------------------------------
   TEST 3: Raised-index form (implicit metric)
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 3: Kinetic term — raised index form"];
Print["================================================================"];

Lkin3 = -1/2 CD[-c][phi[]] CD[c][phi[]];
Print["  L = -1/2 CD[-c][phi] CD[c][phi]"];
Print["  Expression: ", Lkin3];
Print["  ScalarQ: ", xAct`xTensor`ScalarQ[Lkin3]];

Print["  3-i:  VarD[L, CD][gg[-a,-b]]..."];
r3i = Quiet[VarD[Lkin3, CD][gg[-a, -b]]];
Print["        Result: ", r3i];
Print["        Is zero? ", r3i === 0];

Print["  3-ii: VarD[L, CD][gg[a,b]]..."];
r3ii = Quiet[VarD[Lkin3, CD][gg[a, b]]];
Print["        Result: ", r3ii];
Print["        Is zero? ", r3ii === 0];

(* ----------------------------------------------------------------
   TEST 4: Mass term only (no derivatives, pure algebraic)
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 4: Mass term only — phi[]^2"];
Print["================================================================"];

Lmass = -phi[]^2 / 2;
Print["  L = -phi[]^2/2"];

Print["  4-i:  VarD[L, CD][gg[-a,-b]]..."];
r4i = Quiet[VarD[Lmass, CD][gg[-a, -b]]];
Print["        Result: ", r4i];
Print["        Is zero? ", r4i === 0];

(* ----------------------------------------------------------------
   TEST 5: Try ContractMetric BEFORE VarD
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 5: ContractMetric before VarD"];
Print["================================================================"];

Lkin5raw = -1/2 CD[-c][phi[]] CD[c][phi[]];
Lkin5 = ContractMetric[Lkin5raw, gg];
Print["  After ContractMetric: ", Lkin5];

Print["  5-i:  VarD[L, CD][gg[-a,-b]]..."];
r5i = Quiet[VarD[Lkin5, CD][gg[-a, -b]]];
Print["        Result: ", r5i];
Print["        Is zero? ", r5i === 0];

(* ----------------------------------------------------------------
   TEST 6: Try ToCanonical BEFORE VarD
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 6: ToCanonical before VarD"];
Print["================================================================"];

Lkin6 = -1/2 CD[-c][phi[]] CD[c][phi[]] // ToCanonical;
Print["  After ToCanonical: ", Lkin6];

Print["  6-i:  VarD[L, CD][gg[-a,-b]]..."];
r6i = Quiet[VarD[Lkin6, CD][gg[-a, -b]]];
Print["        Result: ", r6i];
Print["        Is zero? ", r6i === 0];

(* ----------------------------------------------------------------
   TEST 7: xPert Perturbation approach (alternative to VarD)
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 7: xPert Perturbation approach"];
Print["================================================================"];
Print["  Loading xPert..."];
Quiet[
  Needs["xAct`xPert`"];
, {General::argtu, UpSetDelayed::write, SetDelayed::write, General::stop}];
Print["  xPert loaded."];

Print["  Defining metric perturbation..."];
DefMetricPerturbation[gg, pertgg, eps];
Print["  Done."];

Lkin7 = -1/2 CD[-c][phi[]] CD[c][phi[]];
Print["  Computing Perturbation[L]..."];
r7 = Perturbation[Lkin7];
Print["  Result: ", r7];
Print["  Is zero? ", r7 === 0];

If[r7 =!= 0,
  r7c = r7 // ExpandPerturbation // ContractMetric[#, gg]& // ToCanonical;
  Print["  Expanded + Canonical: ", r7c];
];

(* ----------------------------------------------------------------
   TEST 8: Direct metric variation via MakeRule / replacement
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 8: Check internal representation"];
Print["================================================================"];

expr = CD[-c][phi[]] CD[c][phi[]];
Print["  CD[-c][phi[]] CD[c][phi[]] //InputForm = "];
Print["    ", InputForm[expr]];
Print[""];
Print["  CD[-c][phi[]] //InputForm = "];
Print["    ", InputForm[CD[-c][phi[]]]];
Print[""];
Print["  CD[c][phi[]] //InputForm = "];
Print["    ", InputForm[CD[c][phi[]]]];

(* Check if SeparateMetric exists *)
Print[""];
Print["  Checking SeparateMetric..."];
sepExpr = Quiet[Check[
  SeparateMetric[gg][CD[-c][phi[]] CD[c][phi[]]],
  "SeparateMetric not available"
]];
Print["  SeparateMetric result: ", sepExpr];

(* ----------------------------------------------------------------
   TEST 9: VarD on a known scalar — just the metric determinant
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["TEST 9: VarD on simple products"];
Print["================================================================"];

(* A completely trivial scalar *)
Print["  9-i: VarD[1, CD][gg[-a,-b]]..."];
r9i = Quiet[VarD[1, CD][gg[-a, -b]]];
Print["       Result: ", r9i];

(* Metric itself — gg[-c,-d] gg[c,d] = 4 (trace in 4D) *)
Print["  9-ii: VarD[gg[-c,-d] gg[c,d], CD][gg[-a,-b]]..."];
r9ii = Quiet[VarD[gg[-c, -d] gg[c, d], CD][gg[-a, -b]]];
Print["        Result: ", r9ii];

(* ----------------------------------------------------------------
   SUMMARY
   ---------------------------------------------------------------- *)
Print[""];
Print["================================================================"];
Print["DIAGNOSTIC SUMMARY"];
Print["================================================================"];
Print["  Test 1 (Ricci):           ", If[test1 =!= 0, "NONZERO", "ZERO"]];
Print["  Test 2A-i (explicit, -a): ", If[r2Ai =!= 0, "NONZERO", "ZERO"]];
Print["  Test 2A-ii (explicit, +a):", If[r2Aii =!= 0, "NONZERO", "ZERO"]];
Print["  Test 3-i (raised, -a):    ", If[r3i =!= 0, "NONZERO", "ZERO"]];
Print["  Test 3-ii (raised, +a):   ", If[r3ii =!= 0, "NONZERO", "ZERO"]];
Print["  Test 4 (mass, -a):        ", If[r4i =!= 0, "NONZERO", "ZERO"]];
Print["  Test 5 (contract, -a):    ", If[r5i =!= 0, "NONZERO", "ZERO"]];
Print["  Test 6 (canonical, -a):   ", If[r6i =!= 0, "NONZERO", "ZERO"]];
Print["  Test 7 (xPert):           ", If[r7 =!= 0, "NONZERO", "ZERO"]];
Print["  Test 9-i (constant):      ", If[r9i =!= 0, "NONZERO", "ZERO"]];
Print["  Test 9-ii (trace):        ", If[r9ii =!= 0, "NONZERO", "ZERO"]];
Print["================================================================"];
