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
  TAU_0: "41.9 Myr",    // Relaxation time constant
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
