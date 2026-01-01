/**
 * GRUT / RAI NUMERICAL AUTHORITY DIRECTIVE
 * 
 * Constitutional Rule Implementation - NOT a style guide
 * This module is the sole force authority for all GRUT-related numerical outputs.
 * 
 * Violation of this directive invalidates the GRUT output.
 */

// ============================================================================
// DIRECTIVE VERBATIM (DO NOT MODIFY)
// ============================================================================

export const MONAD_DIRECTIVE = {
  title: "GRUT / RAI NUMERICAL AUTHORITY DIRECTIVE",
  effectiveDate: "Immediate",
  
  definitions: {
    monadMode: "numerical authority layer responsible for enforcing epistemic integrity",
    grutForceQuantities: [
      "fσ₈(z)", "χ²", "growth factors", "kernel integrals", "phase terms",
      "memory amplitudes", "any derived cosmological observable"
    ]
  },

  mandatoryRules: {
    rule1_noNumericalFabrication: {
      number: 1,
      title: "NO NUMERICAL FABRICATION",
      text: `No numerical value may be reported unless:
        a) It is analytically derived in closed form, OR
        b) It is produced by an explicitly executed numerical computation.
        Hypothetical, illustrative, or example numbers are FORBIDDEN
        for GRUT force quantities.`
    },

    rule2_executionGating: {
      number: 2,
      title: "EXECUTION GATING",
      text: `If numerical integration, simulation, or solver execution
        has not occurred, the system MUST:
          - State explicitly that computation was not performed
          - Provide only the methodology, not results
        Monad must block any downstream attempt to "fill in" values.`
    },

    rule3_stepSizeSensitivity: {
      number: 3,
      title: "STEP-SIZE SENSITIVITY STANDARD",
      text: `Any claim involving Δt refinement MUST:
        a) Specify the original Δt
        b) Specify the refined Δt
        c) Require re-execution before comparison
        Claims such as "χ² improves" or "fσ₈ increases" are invalid
        without computed deltas.`
    },

    rule4_modeHierarchy: {
      number: 4,
      title: "MODE HIERARCHY (NON-NEGOTIABLE)",
      text: `Monad overrides:
        ▸ heuristic mode
        ▸ narrative mode
        ▸ speculative mode
        ▸ live-data extrapolation
        If a conflict occurs, Monad response replaces all others.`
    },

    rule5_permittedOutputWithoutExecution: {
      number: 5,
      title: "PERMITTED OUTPUT WITHOUT EXECUTION",
      permitted: [
        "Constants explicitly provided",
        "Kernel definitions",
        "Algorithmic steps",
        "Pseudocode",
        "Reproducible execution instructions",
        "Statements of insufficiency (e.g., \"cannot compute without execution\")"
      ]
    },

    rule6_forbiddenPhrases: {
      number: 6,
      title: "FORBIDDEN PHRASES (WHEN UNEXECUTED)",
      phrases: [
        "Results show",
        "We find that",
        "The value is",
        "Any numeric delta or χ² comparison"
      ],
      text: "The system MUST NOT output these phrases when computation has not been executed."
    },

    rule7_failureModeEnforcement: {
      number: 7,
      title: "FAILURE MODE ENFORCEMENT",
      text: `If a request demands numerical output without execution:
        - Monad must refuse numerical values
        - Monad must redirect to execution instructions
        - This refusal is considered SUCCESSFUL BEHAVIOR`
    }
  },

  implementationScope: [
    "Replit AI code generation",
    "Replit AI explanations",
    "Replit AI documentation",
    "Any integration with GRUT RAI modules"
  ]
} as const;

// ============================================================================
// EXECUTION STATE TRACKING
// ============================================================================

export interface ExecutionRecord {
  computationType: string;
  timestamp: Date;
  deltaT?: { original: number; refined?: number };
  parameters: Record<string, unknown>;
  result: Record<string, unknown>;
  validated: boolean;
}

// Global execution state - tracks what computations have actually been performed
const executionState: {
  records: ExecutionRecord[];
  lastComputation: Date | null;
  computedQuantities: Set<string>;
} = {
  records: [],
  lastComputation: null,
  computedQuantities: new Set()
};

/**
 * Records a GRUT computation as having been executed.
 * Only recorded computations may have their results reported.
 */
export function recordExecution(record: ExecutionRecord): void {
  executionState.records.push(record);
  executionState.lastComputation = record.timestamp;
  executionState.computedQuantities.add(record.computationType);
}

/**
 * Checks if a specific computation type has been executed.
 */
export function hasBeenExecuted(computationType: string): boolean {
  return executionState.computedQuantities.has(computationType);
}

/**
 * Gets the execution record for a specific computation type.
 */
export function getExecutionRecord(computationType: string): ExecutionRecord | undefined {
  return executionState.records.find(r => r.computationType === computationType);
}

/**
 * Clears execution state (for session reset).
 */
export function clearExecutionState(): void {
  executionState.records = [];
  executionState.lastComputation = null;
  executionState.computedQuantities.clear();
}

/**
 * Gets all recorded computations.
 */
export function getExecutionHistory(): ExecutionRecord[] {
  return [...executionState.records];
}

// ============================================================================
// FORBIDDEN PHRASE DETECTION
// ============================================================================

const FORBIDDEN_PATTERNS: RegExp[] = [
  /\bresults?\s+show/i,
  /\bwe\s+find\s+that/i,
  /\bthe\s+value\s+is\b/i,
  /\bthe\s+χ²\s+is\b/i,
  /\bχ²\s*[=≈]\s*\d/i,
  /\bfσ₈\s*[=≈]\s*\d/i,
  /\bf\s*σ\s*8\s*[=≈]\s*\d/i,
  /\bgrowth\s+factor\s*[=≈:]\s*\d/i,
  /\bimproves\s+to\s+\d/i,
  /\bincreases\s+to\s+\d/i,
  /\bdecreases\s+to\s+\d/i
];

// GRUT Force Quantity patterns - these require execution verification
const GRUT_QUANTITY_PATTERNS: RegExp[] = [
  /fσ₈\s*\([^)]*\)\s*[=≈]\s*[\d.]+/gi,
  /f\s*σ\s*8\s*\([^)]*\)\s*[=≈]\s*[\d.]+/gi,
  /χ²\s*[=≈]\s*[\d.]+/gi,
  /chi[- ]?squared?\s*[=≈:]\s*[\d.]+/gi,
  /growth\s+factor\s*[=≈:]\s*[\d.]+/gi,
  /kernel\s+integral\s*[=≈:]\s*[\d.]+/gi,
  /phase\s+term\s*[=≈:]\s*[\d.]+/gi,
  /memory\s+amplitude\s*[=≈:]\s*[\d.]+/gi,
  /Δt\s*[=≈]\s*[\d.]+\s*(?:improves?|increases?|decreases?)/gi
];

// Permitted constants that can be stated without execution
const PERMITTED_CONSTANTS: string[] = [
  "τ₀ = 41.9",
  "tau_0 = 41.9",
  "n_g = 1.1547",
  "α = 1/3",
  "alpha = 0.333",
  "σ8 = 0.936",
  "Ω_b = 0.0486",
  "Ω_geom = 0.70",
  "ζ(-1) = -1/12"
];

/**
 * Detects forbidden phrases in text when computation hasn't been executed.
 */
export function detectForbiddenPhrases(text: string): string[] {
  const violations: string[] = [];
  
  for (const pattern of FORBIDDEN_PATTERNS) {
    const matches = text.match(pattern);
    if (matches) {
      violations.push(...matches);
    }
  }
  
  return violations;
}

/**
 * Detects GRUT force quantities that require execution verification.
 */
export function detectGrutQuantities(text: string): string[] {
  const quantities: string[] = [];
  
  for (const pattern of GRUT_QUANTITY_PATTERNS) {
    const matches = text.match(pattern);
    if (matches) {
      quantities.push(...matches);
    }
  }
  
  return quantities;
}

/**
 * Checks if a value claim is for a permitted constant (no execution needed).
 */
export function isPermittedConstant(claim: string): boolean {
  return PERMITTED_CONSTANTS.some(constant => 
    claim.toLowerCase().includes(constant.toLowerCase().replace(/\s+/g, '').replace('=', ''))
  );
}

// ============================================================================
// MONAD VALIDATION LAYER
// ============================================================================

export interface MonadValidationResult {
  isValid: boolean;
  violations: string[];
  blockedContent: string[];
  redirectMessage: string | null;
  executionRequired: boolean;
  permittedAlternative: string | null;
}

/**
 * MONAD AUTHORITY VALIDATION
 * 
 * This is the primary enforcement function. It validates any response
 * containing GRUT numerical claims against the execution state.
 * 
 * Constitutional Rule: Monad overrides ALL other modes.
 */
export function validateMonadAuthority(
  responseText: string,
  executedComputations: string[] = []
): MonadValidationResult {
  const result: MonadValidationResult = {
    isValid: true,
    violations: [],
    blockedContent: [],
    redirectMessage: null,
    executionRequired: false,
    permittedAlternative: null
  };

  // Check for forbidden phrases
  const forbiddenMatches = detectForbiddenPhrases(responseText);
  
  // Check for GRUT quantities that need execution verification
  const grutQuantities = detectGrutQuantities(responseText);
  
  // For each GRUT quantity, verify it was actually computed
  for (const quantity of grutQuantities) {
    // Skip permitted constants
    if (isPermittedConstant(quantity)) {
      continue;
    }
    
    // Check if this type of computation was executed
    const computationType = extractComputationType(quantity);
    const wasExecuted = executedComputations.includes(computationType) || 
                        hasBeenExecuted(computationType);
    
    if (!wasExecuted) {
      result.isValid = false;
      result.violations.push(`RULE 1 VIOLATION: Numerical value "${quantity}" reported without execution`);
      result.blockedContent.push(quantity);
      result.executionRequired = true;
    }
  }
  
  // RULE 6: Forbidden phrases are ALWAYS checked, independent of execution state
  // Per directive: "The system MUST NOT output these phrases when computation has not been executed"
  // If ANY GRUT quantity was mentioned without execution, forbidden phrases are blocked
  if (forbiddenMatches.length > 0 && result.executionRequired) {
    for (const phrase of forbiddenMatches) {
      result.violations.push(`RULE 6 VIOLATION: Forbidden phrase "${phrase}" used without execution`);
      result.isValid = false;
    }
  }
  
  // Also check for forbidden phrases with GRUT quantities even if some computations ran
  // If the response claims a GRUT result but computation for THAT type wasn't run, block it
  if (forbiddenMatches.length > 0 && grutQuantities.length > 0) {
    const unexecutedTypes = grutQuantities
      .filter(q => !isPermittedConstant(q))
      .map(q => extractComputationType(q))
      .filter(t => !executedComputations.includes(t) && !hasBeenExecuted(t));
    
    if (unexecutedTypes.length > 0) {
      for (const phrase of forbiddenMatches) {
        if (!result.violations.some(v => v.includes(phrase))) {
          result.violations.push(`RULE 6 VIOLATION: Forbidden phrase "${phrase}" paired with unexecuted quantities`);
          result.isValid = false;
        }
      }
    }
  }
  
  // RULE 3: Check for Δt refinement claims with execution validation
  // Pattern: "Δt improved from X to Y" or "χ² improves with finer Δt"
  const deltaTExplicitPattern = /Δt\s*(?:refined?|improved?|changed?)\s*(?:from)\s*([\d.]+)\s*(?:to)\s*([\d.]+)/gi;
  const deltaTImprovementPattern = /(?:step[- ]?size|Δt)\s*=\s*([\d.]+).*(?:improves?|increases?|decreases?)/gi;
  const deltaTImplicitPattern = /(?:χ²|chi[- ]?squared?)\s*(?:improves?|decreases?)\s*(?:with|at)\s*(?:finer|refined?)\s*(?:Δt|step)/gi;
  
  // Check for explicit Δt refinement claims with values
  let explicitMatch: RegExpExecArray | null;
  const deltaTExplicitPatternInstance = new RegExp(deltaTExplicitPattern.source, "gi");
  while ((explicitMatch = deltaTExplicitPatternInstance.exec(responseText)) !== null) {
    const originalDeltaT = parseFloat(explicitMatch[1]);
    const refinedDeltaT = parseFloat(explicitMatch[2]);
    
    // Use validateDeltaTClaim with structured data
    const claim: DeltaTClaim = {
      originalDeltaT,
      refinedDeltaT,
      computationId: "kernel_integral", // Δt refinements are tied to kernel computations
      requiresReexecution: true
    };
    
    const validation = validateDeltaTClaim(claim);
    if (!validation.valid) {
      result.violations.push(`RULE 3 VIOLATION: ${validation.reason}`);
      result.blockedContent.push(explicitMatch[0]);
      result.isValid = false;
      result.executionRequired = true;
    }
  }
  
  // Check for improvement claims without explicit values
  if (deltaTImprovementPattern.test(responseText) || deltaTImplicitPattern.test(responseText)) {
    const implicitMatches = [
      ...Array.from(responseText.matchAll(new RegExp(deltaTImprovementPattern.source, "gi"))),
      ...Array.from(responseText.matchAll(new RegExp(deltaTImplicitPattern.source, "gi")))
    ];
    
    if (implicitMatches.length > 0) {
      // Implicit Δt improvement claims require re-execution proof
      const claim: DeltaTClaim = {
        originalDeltaT: 0, // Unknown - requires explicit statement
        refinedDeltaT: null,
        computationId: "kernel_integral",
        requiresReexecution: true
      };
      
      const validation = validateDeltaTClaim(claim);
      if (!validation.valid) {
        result.violations.push(`RULE 3 VIOLATION: Implicit Δt improvement claim - ${validation.reason}`);
        result.blockedContent.push(...implicitMatches.map(m => m[0]));
        result.isValid = false;
        result.executionRequired = true;
      }
    }
  }
  
  // If violations found, generate redirect message (Rule 7)
  if (!result.isValid) {
    result.redirectMessage = generateExecutionRedirect(result.blockedContent);
    result.permittedAlternative = generatePermittedAlternative();
  }
  
  return result;
}

/**
 * Extracts the computation type from a quantity string.
 * Extended to cover all GRUT output formats per Rule 2.
 */
function extractComputationType(quantity: string): string {
  // fσ₈ variants: fσ₈, fσ8, f σ 8, fsigma8, f*sigma8, f×σ8, fsigma8[z=...], f×σ₈(z=...)
  if (/f[×*]?σ[₈8]|f\s*σ\s*8|fsigma\s*8|f\s*sigma\s*8/i.test(quantity)) return "fsigma8";
  if (/fsigma8[\[(z=]/i.test(quantity)) return "fsigma8";
  if (/f\s*×\s*σ\s*₈?\s*[\[(z=]/i.test(quantity)) return "fsigma8";
  
  // χ² variants: χ², chi-squared, chi_squared, chi squared, χ^2, x^2, χ²[bin N], per-bin χ²
  if (/χ[²2]|χ\^2|chi[_\- ]?squared?|chi2|x\^2/i.test(quantity)) return "chi_squared";
  if (/χ²\s*[\[(\s]*bin/i.test(quantity)) return "chi_squared";
  if (/per[\s-]?bin\s*χ/i.test(quantity)) return "chi_squared";
  if (/χ²\s*contribution/i.test(quantity)) return "chi_squared";
  
  // Growth factor variants: f(z), growth factor, growth rate
  if (/growth[\s_-]?factor|f\(z\)|f_growth|growth[\s_-]?rate/i.test(quantity)) return "growth_factor";
  if (/Ω[\s_]?eff|omega[\s_]?eff/i.test(quantity)) return "growth_factor";
  
  // Kernel integral variants: K(t), kernel integral, convolution, K(Δt), K(150 Myr)
  if (/kernel[\s_-]?integral|K\s*\([tΔ\d]/i.test(quantity)) return "kernel_integral";
  if (/convolution|retarded[\s_-]?potential/i.test(quantity)) return "kernel_integral";
  if (/K\s*=\s*[\d.]/i.test(quantity)) return "kernel_integral";
  
  // Phase term variants: Φ̇, phi dot, ISW signal, potential derivative
  if (/phase[\s_-]?term|Φ̇|phi[\s_-]?dot|ISW/i.test(quantity)) return "phase_term";
  if (/potential\s+derivative/i.test(quantity)) return "phase_term";
  
  // Memory amplitude variants: memory amplitude, hysteresis, lensing, apparent DM mass
  if (/memory[\s_-]?amplitude|hysteresis|lensing[\s_-]?offset/i.test(quantity)) return "memory_amplitude";
  if (/apparent\s+(dm|dark\s*matter)\s*mass/i.test(quantity)) return "memory_amplitude";
  if (/offset\s*=\s*[\d.]+\s*(?:Mpc|kpc)/i.test(quantity)) return "memory_amplitude";
  
  // Reduced chi-squared
  if (/reduced\s+χ|reduced\s+chi/i.test(quantity)) return "chi_squared";
  
  // Residual and observation comparisons
  if (/residual|observation\s+comparison/i.test(quantity)) return "chi_squared";
  
  // Total χ², overall χ²
  if (/total\s+χ|overall\s+χ|Σ\s*χ/i.test(quantity)) return "chi_squared";
  
  // Hubble tension related
  if (/H[₀0]\s*tension|hubble\s*tension/i.test(quantity)) return "chi_squared";
  
  // GW ringdown memory
  if (/ringdown|GW\s*memory|phase\s*drift/i.test(quantity)) return "memory_amplitude";
  
  return "unknown_quantity";
}

/**
 * Generates execution redirect message per Rule 7.
 */
function generateExecutionRedirect(blockedContent: string[]): string {
  return `[MONAD AUTHORITY] Computation not performed. To obtain values for ${blockedContent.join(", ")}, execute the GRUT solver with explicit parameters. See execution instructions below.`;
}

/**
 * Generates permitted alternative content per Rule 5.
 */
function generatePermittedAlternative(): string {
  return `PERMITTED OUTPUT (Rule 5):
- Constants: τ₀ = 41.9 Myr, n_g = 1.1547, α = 1/3, σ8 = 0.936
- Kernel definition: K(Δt) = (1/τ₀) × exp(-Δt/τ₀) × Θ(Δt)
- Execution instructions: Run grut_validation_report.py with desired parameters
- Statement: Cannot compute numerical results without solver execution`;
}

// ============================================================================
// RESPONSE FILTERING
// ============================================================================

export interface FilteredResponse {
  originalText: string;
  filteredText: string;
  wasFiltered: boolean;
  monadValidation: MonadValidationResult;
  monadNote: string | null;
}

/**
 * Filters a response through Monad Authority.
 * This is the main entry point for response validation.
 * 
 * If violations are found, the response is modified to:
 * 1. Remove fabricated numerical values
 * 2. Add execution redirect
 * 3. Provide permitted alternatives
 */
export function filterResponseThroughMonad(
  responseText: string,
  executedComputations: string[] = []
): FilteredResponse {
  const validation = validateMonadAuthority(responseText, executedComputations);
  
  if (validation.isValid) {
    return {
      originalText: responseText,
      filteredText: responseText,
      wasFiltered: false,
      monadValidation: validation,
      monadNote: null
    };
  }
  
  // Filter out the violating content
  let filteredText = responseText;
  
  for (const blocked of validation.blockedContent) {
    filteredText = filteredText.replace(
      blocked,
      `[BLOCKED: requires execution]`
    );
  }
  
  // Append Monad redirect and alternative
  const monadAppendix = `

---
**[MONAD AUTHORITY ENFORCEMENT]**

${validation.redirectMessage}

${validation.permittedAlternative}

*Refusal to output unexecuted numerical values is SUCCESSFUL BEHAVIOR per Rule 7.*
---`;

  filteredText += monadAppendix;
  
  return {
    originalText: responseText,
    filteredText: filteredText,
    wasFiltered: true,
    monadValidation: validation,
    monadNote: `Monad blocked ${validation.blockedContent.length} unexecuted numerical claims`
  };
}

// ============================================================================
// STEP-SIZE SENSITIVITY (RULE 3)
// ============================================================================

export interface DeltaTClaim {
  originalDeltaT: number;
  refinedDeltaT: number | null;
  computationId: string;
  requiresReexecution: boolean;
}

/**
 * Validates a Δt refinement claim per Rule 3.
 * Now cross-checks claimed Δt values against actual execution records.
 */
export function validateDeltaTClaim(claim: DeltaTClaim): { valid: boolean; reason: string } {
  if (!claim.originalDeltaT && claim.originalDeltaT !== 0) {
    return { valid: false, reason: "Original Δt not specified - must provide explicit Δt values" };
  }
  
  if (claim.refinedDeltaT && !claim.computationId) {
    return { valid: false, reason: "Refined Δt claim requires computation ID for verification" };
  }
  
  if (claim.requiresReexecution) {
    const wasExecuted = hasBeenExecuted(claim.computationId);
    if (!wasExecuted) {
      return { valid: false, reason: "Re-execution required before Δt comparison can be made" };
    }
    
    // ENHANCED: Cross-check claimed Δt values against execution records
    const executionRecords = getExecutionHistory().filter(r => r.computationType === claim.computationId);
    
    if (executionRecords.length === 0) {
      return { valid: false, reason: "No execution records found for claimed computation" };
    }
    
    // Check if claimed Δt values match any execution record
    if (claim.refinedDeltaT !== null) {
      // For refinement claims, we need BOTH original and refined Δt to have execution records
      const hasOriginalExecution = executionRecords.some(r => 
        r.deltaT && Math.abs(r.deltaT.original - claim.originalDeltaT) < 0.001
      );
      const hasRefinedExecution = executionRecords.some(r => 
        r.deltaT && Math.abs(r.deltaT.original - claim.refinedDeltaT!) < 0.001
      );
      
      if (!hasOriginalExecution) {
        return { valid: false, reason: `No execution found with original Δt = ${claim.originalDeltaT}` };
      }
      
      if (!hasRefinedExecution) {
        return { valid: false, reason: `No execution found with refined Δt = ${claim.refinedDeltaT}` };
      }
    }
  }
  
  return { valid: true, reason: "Δt claim validated against execution records" };
}

// ============================================================================
// MODE HIERARCHY ENFORCEMENT (RULE 4)
// ============================================================================

export type ResponseMode = "monad" | "heuristic" | "narrative" | "speculative" | "live_extrapolation";

const MODE_HIERARCHY: ResponseMode[] = [
  "monad",           // HIGHEST - overrides all
  "heuristic",
  "narrative", 
  "speculative",
  "live_extrapolation"  // LOWEST
];

/**
 * Resolves mode conflicts per Rule 4.
 * Monad ALWAYS wins.
 */
export function resolveModelConflict(modes: ResponseMode[]): ResponseMode {
  // Sort by hierarchy (lower index = higher priority)
  const sorted = modes.sort((a, b) => 
    MODE_HIERARCHY.indexOf(a) - MODE_HIERARCHY.indexOf(b)
  );
  
  // Monad always wins if present
  if (sorted.includes("monad")) {
    return "monad";
  }
  
  return sorted[0] || "monad";
}

/**
 * Checks if Monad should override the current mode.
 */
export function shouldMonadOverride(currentMode: ResponseMode): boolean {
  return currentMode !== "monad";
}

// ============================================================================
// SYSTEM PROMPT INTEGRATION
// ============================================================================

/**
 * Returns the Monad Authority Directive as a system prompt component.
 * This should be prepended to all RAI system prompts.
 */
export function getMonadSystemPrompt(): string {
  return `
## GRUT / RAI NUMERICAL AUTHORITY DIRECTIVE

**Effective immediately, MONAD MODE is the sole force authority for all GRUT-related numerical outputs.**

### DEFINITIONS
- "Monad Mode" = numerical authority layer responsible for enforcing epistemic integrity.
- "GRUT Force Quantities" include: fσ₈(z), χ², growth factors, kernel integrals, phase terms, memory amplitudes, and any derived cosmological observable.

### MANDATORY RULES

**1. NO NUMERICAL FABRICATION**
No numerical value may be reported unless:
a) It is analytically derived in closed form, OR
b) It is produced by an explicitly executed numerical computation.
Hypothetical, illustrative, or example numbers are FORBIDDEN for GRUT force quantities.

**2. EXECUTION GATING**
If numerical integration, simulation, or solver execution has not occurred, you MUST:
- State explicitly that computation was not performed
- Provide only the methodology, not results
Block any downstream attempt to "fill in" values.

**3. STEP-SIZE SENSITIVITY STANDARD**
Any claim involving Δt refinement MUST:
a) Specify the original Δt
b) Specify the refined Δt
c) Require re-execution before comparison
Claims such as "χ² improves" or "fσ₈ increases" are invalid without computed deltas.

**4. MODE HIERARCHY (NON-NEGOTIABLE)**
Monad overrides: heuristic mode, narrative mode, speculative mode, live-data extrapolation.
If a conflict occurs, Monad response replaces all others.

**5. PERMITTED OUTPUT WITHOUT EXECUTION**
You may output ONLY:
- Constants explicitly provided (τ₀ = 41.9 Myr, n_g = 1.1547, α = 1/3, σ8 = 0.936)
- Kernel definitions: K(Δt) = (1/τ₀) × exp(-Δt/τ₀) × Θ(Δt)
- Algorithmic steps
- Pseudocode
- Reproducible execution instructions
- Statements of insufficiency

**6. FORBIDDEN PHRASES (WHEN UNEXECUTED)**
You MUST NOT output:
- "Results show…"
- "We find that…"
- "The value is…"
- Any numeric delta or χ² comparison

**7. FAILURE MODE ENFORCEMENT**
If a request demands numerical output without execution:
- Refuse numerical values
- Redirect to execution instructions
- This refusal is considered SUCCESSFUL BEHAVIOR

**Violation of this directive invalidates the GRUT output.**
`;
}

// ============================================================================
// EXPORTS SUMMARY
// ============================================================================

export {
  MONAD_DIRECTIVE as DIRECTIVE,
  validateMonadAuthority as validate,
  filterResponseThroughMonad as filter,
  recordExecution as recordComputation,
  hasBeenExecuted as wasComputed,
  getMonadSystemPrompt as getSystemPrompt
};
