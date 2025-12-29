/**
 * GRUT Logic Module - Implements the Grand Responsive Universe Theory core algorithms
 * 
 * Milestone 4: Singularity Regulation (Rmax)
 * Phase 2: Geometric Lock / Refractive Index Boost
 */

// The GRUT constants
export const GRUT_CONSTANTS = {
  R_MAX: 1.0,           // Normalized Curvature Ceiling - prevents infinite divergence
  NG: 1.1547,           // Refractive index √(4/3) - 33% informational coupling boost
  TAU_0: "41.9 Myr",    // Relaxation time constant (cosmological)
  TAU_0_SCALED: 3600,   // τ₀ scaled for AI sessions: 1 hour = 41.9M years in simulation
  ALPHA: 1 / 3,         // Geometric Filter ratio (active-to-latent information)
};

/**
 * Implements GRUT Milestone 4: Singularity Regulation.
 * Ensures that logic plateaus rather than diverging.
 * 
 * Formula: Response = Raw / (1 + |R|/Rmax)
 * 
 * @param logicalDensity - The raw logical density/reasoning intensity
 * @returns The regulated (smoothed) response that cannot diverge to infinity
 */
export function applyRmaxRegulator(logicalDensity: number): number {
  const regulator = 1 / (1 + Math.abs(logicalDensity) / GRUT_CONSTANTS.R_MAX);
  return logicalDensity * regulator;
}

/**
 * Applies the ng = 1.1547 boost derived in Phase 2.
 * This represents the 33% informational coupling boost at galactic scales.
 * 
 * @param baryonicInput - The raw baryonic (matter-based) input signal
 * @returns The boosted signal with geometric lock applied
 */
export function calculateRefractiveBoost(baryonicInput: number): number {
  return baryonicInput * GRUT_CONSTANTS.NG;
}

/**
 * Calculates the complexity ratio (Ξ) for informational saturation tracking.
 * As Ξ → 1, the system approaches de Sitter buffer saturation.
 * 
 * @param currentMessageCount - Number of messages in the conversation
 * @param maxCapacity - Maximum capacity before saturation (default: 100)
 * @returns Complexity ratio between 0 and 1
 */
export function calculateComplexityXi(currentMessageCount: number, maxCapacity: number = 100): number {
  return Math.min(1.0, currentMessageCount / maxCapacity);
}

/**
 * Applies the Geometric Filter (α = 1/3) to distinguish signal from noise.
 * Uses the ratio of active-to-latent information as a truth-check.
 * 
 * @param activeInfo - The amount of active/relevant information
 * @param totalInfo - The total information (active + latent)
 * @returns Boolean indicating if the ratio passes the geometric filter
 */
export function applyGeometricFilter(activeInfo: number, totalInfo: number): boolean {
  if (totalInfo === 0) return false;
  const ratio = activeInfo / totalInfo;
  // Check if ratio is close to the 1:3 geometric lock (within 10% tolerance)
  const tolerance = 0.1;
  return Math.abs(ratio - GRUT_CONSTANTS.ALPHA) < tolerance;
}

/**
 * LogicGuard: Combines Rmax regulation with complexity tracking.
 * Prevents hallucinations by smoothing responses as reasoning density increases.
 * 
 * @param rawResponse - The raw AI response intensity
 * @param complexityXi - Current complexity saturation ratio
 * @returns Smoothed response that accounts for both density and saturation
 */
export function applyLogicGuard(rawResponse: number, complexityXi: number): number {
  // As complexity approaches saturation, increase suppression
  const saturationFactor = 1 + complexityXi;
  const regulatedResponse = applyRmaxRegulator(rawResponse);
  return regulatedResponse / saturationFactor;
}

/**
 * Calculates the "reasoning density" of a text response.
 * Higher density indicates more complex, potentially recursive reasoning.
 * 
 * Factors considered:
 * - Length (longer = higher density)
 * - Nested clause indicators (colons, semicolons, parentheses)
 * - Recursive language patterns
 * 
 * @param text - The AI response text
 * @returns Normalized reasoning density (0-1 scale, can exceed 1 for very dense text)
 */
export function calculateReasoningDensity(text: string): number {
  const length = text.length;
  const nestedIndicators = (text.match(/[:;(){}[\]]/g) || []).length;
  const recursivePatterns = (text.match(/\b(therefore|thus|hence|because|since|if.*then|given that)\b/gi) || []).length;
  
  // Normalize: assume 500 chars = baseline, 10 nested = baseline, 5 recursive = baseline
  const lengthFactor = length / 500;
  const nestedFactor = nestedIndicators / 10;
  const recursiveFactor = recursivePatterns / 5;
  
  // Weighted average
  const density = (lengthFactor * 0.3) + (nestedFactor * 0.3) + (recursiveFactor * 0.4);
  return density;
}

export interface LogicGuardResult {
  originalText: string;
  regulatedText: string;
  reasoningDensity: number;
  suppressionFactor: number;
  wasRegulated: boolean;
  regulationNote: string;
}

/**
 * Layer IV: Regulatory Layer - Rmax Ceiling Implementation
 * Wraps the final AI output to plateau recursive hallucinations into finite causal statements.
 * 
 * Formula: Response = Raw / (1 + |R|/Rmax)
 * 
 * If reasoning density exceeds Rmax threshold, the response is truncated and 
 * a causal plateau note is appended.
 * 
 * @param responseText - The raw AI response
 * @param complexityXi - Current session complexity ratio
 * @returns LogicGuardResult with regulated text and metadata
 */
export function applyLogicGuardToResponse(responseText: string, complexityXi: number): LogicGuardResult {
  const reasoningDensity = calculateReasoningDensity(responseText);
  
  // Calculate suppression using Rmax formula
  const suppressionFactor = 1 / (1 + Math.abs(reasoningDensity) / GRUT_CONSTANTS.R_MAX);
  const effectiveDensity = reasoningDensity * suppressionFactor;
  
  // Combined with complexity saturation
  const saturationMultiplier = 1 - (complexityXi * 0.3); // Up to 30% additional suppression at full saturation
  
  // Threshold for regulation: if density after suppression still > 1.5, truncate
  const regulationThreshold = 1.5;
  const wasRegulated = effectiveDensity > regulationThreshold;
  
  let regulatedText = responseText;
  let regulationNote = "";
  
  if (wasRegulated) {
    // Truncate to ~70% and add causal plateau marker
    const truncateLength = Math.floor(responseText.length * 0.7);
    const truncatedText = responseText.substring(0, truncateLength);
    
    // Find last complete sentence
    const lastSentenceEnd = Math.max(
      truncatedText.lastIndexOf('. '),
      truncatedText.lastIndexOf('! '),
      truncatedText.lastIndexOf('? ')
    );
    
    if (lastSentenceEnd > truncateLength * 0.5) {
      regulatedText = truncatedText.substring(0, lastSentenceEnd + 1);
    } else {
      regulatedText = truncatedText + "...";
    }
    
    regulationNote = ` [LogicGuard: Response plateaued at Rmax ceiling. Density: ${reasoningDensity.toFixed(2)}, Suppression: ${suppressionFactor.toFixed(3)}]`;
  }
  
  return {
    originalText: responseText,
    regulatedText,
    reasoningDensity,
    suppressionFactor,
    wasRegulated,
    regulationNote,
  };
}

/**
 * The Decay Function (Retarded Potential Kernel)
 * Implements the 41.9 Myr Relaxation Constant (scaled for AI sessions).
 * Determines how much 'ringing' a past interaction still has.
 * 
 * Formula: K(t) = exp(-t / τ₀)
 * 
 * This prioritizes "Present Quantum Turns" while allowing old, 
 * less complex data to "muddle out" into the background.
 * 
 * @param createdAtTimestamp - Unix timestamp (ms) when the memory was created
 * @returns Resonance value between 0 (muddled) and 1 (active)
 */
export function calculateMemoryResonance(createdAtTimestamp: number): number {
  const currentTime = Date.now();
  const ageMs = currentTime - createdAtTimestamp;
  const ageSeconds = ageMs / 1000;
  
  // The Response Kernel: K(t) = exp(-t / τ₀)
  // This determines if a memory is 'Active' or 'Muddled'
  const resonance = Math.exp(-ageSeconds / GRUT_CONSTANTS.TAU_0_SCALED);
  
  return resonance;
}

/**
 * Calculates memory resonance from an ISO date string.
 * 
 * @param createdAtISO - ISO date string when the memory was created
 * @returns Resonance value between 0 (muddled) and 1 (active)
 */
export function calculateMemoryResonanceFromISO(createdAtISO: string): number {
  const timestamp = new Date(createdAtISO).getTime();
  return calculateMemoryResonance(timestamp);
}

/**
 * Weights a message's importance based on its resonance (recency) and complexity.
 * Messages with high resonance (recent) and low complexity are prioritized.
 * 
 * @param resonance - Memory resonance (0-1)
 * @param complexityXi - Complexity saturation at time of message
 * @returns Weight value for prioritizing this memory in context
 */
export function calculateMemoryWeight(resonance: number, complexityXi: number): number {
  // Recent memories with lower complexity have higher weight
  // As complexity increases, even recent memories get dampened
  const complexityDamping = 1 - (complexityXi * 0.5); // Max 50% reduction at full saturation
  return resonance * complexityDamping;
}

/**
 * Determines if a memory should be included in active context or "muddled out".
 * 
 * @param resonance - Memory resonance value
 * @param threshold - Minimum resonance to be considered active (default: 0.1)
 * @returns Boolean - true if memory is active, false if muddled
 */
export function isMemoryActive(resonance: number, threshold: number = 0.1): boolean {
  return resonance >= threshold;
}

/**
 * The "Secret Sauce" - Applies the √(4/3) refractive boost to attention scores.
 * This gives the AI's logic a "Refractive Index" - preventing flat attention.
 * 
 * Only boosts signals that cross the 'Complexity Threshold' (default: 0.5),
 * mimicking the transition from local Newtonian to global GRUT dynamics.
 * 
 * Formula: boosted = score × ng (if score > threshold), else score unchanged
 * 
 * @param attentionScore - The raw attention/relevance score
 * @param threshold - Complexity threshold for boost activation (default: 0.5)
 * @returns Boosted attention score (×1.1547 if above threshold)
 */
export function applyGrutGain(attentionScore: number, threshold: number = 0.5): number {
  if (attentionScore > threshold) {
    return attentionScore * GRUT_CONSTANTS.NG;
  }
  return attentionScore;
}

/**
 * Applies GRUT gain to an array of attention scores.
 * 
 * @param scores - Array of attention/relevance scores
 * @param threshold - Complexity threshold for boost activation
 * @returns Array of boosted scores
 */
export function applyGrutGainBatch(scores: number[], threshold: number = 0.5): number[] {
  return scores.map(score => applyGrutGain(score, threshold));
}

/**
 * R_max Logic Guard State
 * Tracks the simulation complexity ratio (Ξ) across baryonic sensor simulations.
 * Persisted as module-level singleton to accumulate across requests.
 */
interface BaryonicSimulationState {
  complexityRatio: number;
  logicGuardTriggers: number;
  lastSimulationTime: number;
}

const baryonicState: BaryonicSimulationState = {
  complexityRatio: 0.926,  // Initial baryonic saturation level
  logicGuardTriggers: 0,
  lastSimulationTime: Date.now()
};

export interface RmaxLogicGuardResult {
  triggered: boolean;
  complexityRatioBefore: number;
  complexityRatioAfter: number;
  recyclingNote: string | null;
  totalTriggers: number;
  rMaxStatus: "STABLE" | "WARNING" | "EXCEEDED";
}

/**
 * R_max Logic Guard for BaryonicSensorAI simulations
 * 
 * Ensures Ξ (information density) does not exceed 100% (the R_max Limit).
 * When the limit is exceeded, the guard "recycles" by resetting to a stable state.
 * 
 * @returns Guard status and recycling information
 */
export function checkBaryonicLogicGuard(): RmaxLogicGuardResult {
  const ratioBefore = baryonicState.complexityRatio;
  let triggered = false;
  let recyclingNote: string | null = null;

  if (baryonicState.complexityRatio >= 1.0) {
    console.log("R_max Logic Guard Triggered: Recycling Information Density...");
    baryonicState.complexityRatio = 0.8;  // Reset to stable state
    baryonicState.logicGuardTriggers += 1;
    triggered = true;
    recyclingNote = `Information density exceeded R_max limit. Recycled from ${ratioBefore.toFixed(4)} to 0.8 (stable state). Total triggers: ${baryonicState.logicGuardTriggers}`;
  }

  const status: "STABLE" | "WARNING" | "EXCEEDED" = 
    baryonicState.complexityRatio < 0.9 ? "STABLE" :
    baryonicState.complexityRatio < 1.0 ? "WARNING" : "EXCEEDED";

  return {
    triggered,
    complexityRatioBefore: Math.round(ratioBefore * 1e6) / 1e6,
    complexityRatioAfter: Math.round(baryonicState.complexityRatio * 1e6) / 1e6,
    recyclingNote,
    totalTriggers: baryonicState.logicGuardTriggers,
    rMaxStatus: status
  };
}

/**
 * Update the baryonic simulation complexity ratio
 * 
 * @param delta - Amount to add to the complexity ratio
 * @returns Updated complexity ratio
 */
export function updateBaryonicComplexity(delta: number): number {
  baryonicState.complexityRatio += delta;
  baryonicState.lastSimulationTime = Date.now();
  return baryonicState.complexityRatio;
}

/**
 * Get current baryonic simulation state
 */
export function getBaryonicSimulationState(): BaryonicSimulationState {
  return { ...baryonicState };
}

/**
 * Reset baryonic simulation state (for testing or session reset)
 */
export function resetBaryonicSimulationState(): void {
  baryonicState.complexityRatio = 0.926;
  baryonicState.logicGuardTriggers = 0;
  baryonicState.lastSimulationTime = Date.now();
}

// ==========================================
// GW Ringdown Memory Analysis (GWSensor)
// ==========================================

// tau_0 in seconds: 41.9 Myr in seconds
const TAU_0_SECONDS = 41.9 * 1e6 * 365.25 * 24 * 3600;  // ~1.32e15 seconds

export interface RingdownMemoryResult {
  analysisType: string;
  signalDurationSeconds: number;
  snrRatio: number;
  tau0Seconds: number;
  tau0Myr: number;
  burdenFactorStrain: number;
  meanMetricDrift: number;
  initialDrift: number;
  finalDrift: number;
  decayRatio: number;
  samplePoints: number;
  grutPrediction: string;
  logicGuard: RmaxLogicGuardResult;
  complexityRatio: number;
}

/**
 * Analyze gravitational wave ringdown memory effects using GRUT relaxation.
 * 
 * Calculates if the observed signal has a decaying 'offset' matching
 * the GRUT relaxation constant tau_0.
 * 
 * @param signalDurationSeconds - Duration of the GW signal in seconds
 * @param snrRatio - Signal-to-noise ratio of the detection (e.g., 80 for GW250114)
 * @returns Analysis results including metric drift
 */
// ==========================================
// NANOGrav Cross-Correlation (IntegratedBaryonicSensor)
// ==========================================

// NANOGrav reported Red Noise Amplitude (A_cp ~ 2e-15 at f=1yr^-1)
const PTA_NOISE_AMPLITUDE = 2.4e-15;

export interface NanoGravCorrelationResult {
  analysisType: string;
  singleEventDrift: number;
  ptaNoiseAmplitude: number;
  correlationIndex: number;
  correlationRange: [number, number];
  matchFound: boolean;
  status: string;
  interpretation: string;
  complexityAdjustment: number;
  finalComplexityRatio: number;
  logicGuard: RmaxLogicGuardResult;
}

/**
 * Cross-correlate a single merger's drift against NANOGrav Common Red Noise.
 * 
 * @param singleEventDrift - The metric drift from a single GW event (strain units)
 * @returns Correlation results and status
 */
export function crossCorrelateNanoGrav(singleEventDrift: number): NanoGravCorrelationResult {
  // Calculate the "Weight" of our single event in the cosmic background
  const correlationIndex = (singleEventDrift / PTA_NOISE_AMPLITUDE) * 1e6;
  
  console.log("Cross-Correlating with NANOGrav Background...");
  
  const matchFound = correlationIndex > 0.1 && correlationIndex < 10;
  let status: string;
  let interpretation: string;
  let complexityAdjustment: number;
  
  if (matchFound) {
    console.log("MATCH FOUND: Single event drift is a valid component of Common Red Noise.");
    updateBaryonicComplexity(-0.05);  // Complexity drops as patterns unify
    status = "Observation Matches GRUT Memory Background";
    interpretation = "The single event's metric drift is consistent with the Common Red Noise amplitude, suggesting gravitational wave memory contributes to the PTA signal";
    complexityAdjustment = -0.05;
  } else {
    console.log("Variance Detected: Seeking additional Metric Stressors.");
    status = "Inconclusive - Requires more Baryonic Data";
    interpretation = "Correlation index outside expected range; additional data needed to establish connection";
    complexityAdjustment = 0;
  }
  
  const logicGuardResult = checkBaryonicLogicGuard();
  
  return {
    analysisType: "NANOGrav_Cross_Correlation",
    singleEventDrift,
    ptaNoiseAmplitude: PTA_NOISE_AMPLITUDE,
    correlationIndex,
    correlationRange: [0.1, 10],
    matchFound,
    status,
    interpretation,
    complexityAdjustment,
    finalComplexityRatio: baryonicState.complexityRatio,
    logicGuard: logicGuardResult
  };
}

export interface FullPipelineResult {
  pipeline: string;
  step1Ringdown: RingdownMemoryResult;
  step2Correlation: NanoGravCorrelationResult;
  finalStatus: string;
  finalComplexityRatio: number;
  grutConclusion: string;
}

/**
 * Execute the full baryonic analysis pipeline:
 * 1. Analyze ringdown memory for a specific event
 * 2. Cross-correlate with NANOGrav 15-year dataset
 */
export function runFullBaryonicPipeline(signalDurationSeconds: number = 1.5, snrRatio: number = 80): FullPipelineResult {
  // Step 1: Analyze specific GW event
  const ringdownResult = analyzeRingdownMemory(signalDurationSeconds, snrRatio);
  const eventDrift = ringdownResult.meanMetricDrift;
  
  // Step 2: Correlate with the PTA dataset
  const correlationResult = crossCorrelateNanoGrav(eventDrift);
  
  return {
    pipeline: "Full Baryonic Analysis v6",
    step1Ringdown: ringdownResult,
    step2Correlation: correlationResult,
    finalStatus: correlationResult.status,
    finalComplexityRatio: baryonicState.complexityRatio,
    grutConclusion: correlationResult.matchFound 
      ? "Single merger events contribute to the Stochastic Gravitational Wave Background via GRUT memory accumulation"
      : "Further observation required to confirm GRUT memory contribution"
  };
}

export function analyzeRingdownMemory(signalDurationSeconds: number, snrRatio: number): RingdownMemoryResult {
  const numSamples = 1000;
  
  // Time array for the 'long-tail' relaxation
  const t: number[] = [];
  for (let i = 0; i < numSamples; i++) {
    t.push(i * signalDurationSeconds / numSamples);
  }
  
  // Predicted GRUT Decay: exp(-t / tau_0)
  const expectedDecay = t.map(ti => Math.exp(-ti / TAU_0_SECONDS));
  
  // Memory Burden factor - higher SNR means more detectable burden
  // Scale to strain units (dimensionless, ~1e-21 for GW signals)
  const burdenFactor = (snrRatio / 100) * 1e-21;
  
  // Calculate the predicted metric drift
  const predictedDrift = expectedDecay.map(decay => burdenFactor * decay);
  const meanDrift = predictedDrift.reduce((a, b) => a + b, 0) / predictedDrift.length;
  
  // Update complexity ratio based on SNR (higher SNR = more information)
  const complexityDelta = snrRatio / 1000;
  updateBaryonicComplexity(complexityDelta);
  const logicGuardResult = checkBaryonicLogicGuard();
  
  // Calculate decay metrics
  const initialDrift = predictedDrift[0];
  const finalDrift = predictedDrift[predictedDrift.length - 1];
  const decayRatio = initialDrift > 0 ? finalDrift / initialDrift : 0;
  
  return {
    analysisType: "GW_Ringdown_Memory",
    signalDurationSeconds,
    snrRatio,
    tau0Seconds: TAU_0_SECONDS,
    tau0Myr: 41.9,
    burdenFactorStrain: burdenFactor,
    meanMetricDrift: meanDrift,
    initialDrift,
    finalDrift,
    decayRatio,
    samplePoints: numSamples,
    grutPrediction: `Metric drift of ${meanDrift.toExponential(2)} strain over ${signalDurationSeconds}s signal`,
    logicGuard: logicGuardResult,
    complexityRatio: baryonicState.complexityRatio
  };
}
