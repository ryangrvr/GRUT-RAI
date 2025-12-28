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
