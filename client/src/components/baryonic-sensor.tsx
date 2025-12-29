import { useState } from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { ScrollArea } from "@/components/ui/scroll-area";
import { 
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { Progress } from "@/components/ui/progress";
import { Slider } from "@/components/ui/slider";
import { 
  Activity, Atom, Orbit, Waves, GitBranch, ChevronDown, ChevronUp, ChevronRight,
  Play, Loader2, Target, Zap, Brain, Shield, AlertTriangle, CheckCircle, Radio, Radar, Square,
  Plus, Minus, Sigma, Copy, Check, Share2, Sprout, FileJson, Clock
} from "lucide-react";
import { apiRequest } from "@/lib/queryClient";
import { useToast } from "@/hooks/use-toast";

interface LogicGuardResult {
  triggered: boolean;
  complexityRatioBefore: number;
  complexityRatioAfter: number;
  recyclingNote: string | null;
  totalTriggers: number;
  rMaxStatus: "STABLE" | "WARNING" | "EXCEEDED";
}

interface SimulationResult {
  type: string;
  data: Record<string, unknown> & { logic_guard?: LogicGuardResult };
  timestamp: Date;
}

interface BaryonicSensorProps {
  isOpen: boolean;
  onToggle: () => void;
  constants?: {
    tau_0: number;
    alpha: number;
    n_g: number;
    R_max: string;
  };
}

function LogicGuardStatus({ guard }: { guard: LogicGuardResult }) {
  const getStatusColor = () => {
    switch (guard.rMaxStatus) {
      case "STABLE": return "text-green-500 dark:text-green-400";
      case "WARNING": return "text-yellow-500 dark:text-yellow-400";
      case "EXCEEDED": return "text-red-500 dark:text-red-400";
    }
  };

  const getStatusIcon = () => {
    switch (guard.rMaxStatus) {
      case "STABLE": return <CheckCircle className="w-4 h-4" />;
      case "WARNING": return <AlertTriangle className="w-4 h-4" />;
      case "EXCEEDED": return <Shield className="w-4 h-4" />;
    }
  };

  return (
    <Card className={`mb-3 ${guard.triggered ? "border-primary/50 bg-primary/5" : "bg-muted/20"}`} data-testid="card-logic-guard-status">
      <CardContent className="p-3">
        <div className="flex items-center justify-between gap-2 mb-2">
          <div className="flex items-center gap-2">
            <Shield className="w-4 h-4 text-primary" />
            <span className="text-xs font-semibold">R_max Logic Guard</span>
          </div>
          <div className={`flex items-center gap-1 ${getStatusColor()}`} data-testid={`status-rmax-${guard.rMaxStatus.toLowerCase()}`}>
            {getStatusIcon()}
            <span className="text-xs font-mono">{guard.rMaxStatus}</span>
          </div>
        </div>
        
        <div className="grid grid-cols-2 gap-2 text-xs">
          <div className="flex justify-between">
            <span className="text-muted-foreground">Before:</span>
            <span className="font-mono" data-testid="text-complexity-before">{guard.complexityRatioBefore.toFixed(4)}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-muted-foreground">After:</span>
            <span className="font-mono" data-testid="text-complexity-after">{guard.complexityRatioAfter.toFixed(4)}</span>
          </div>
          <div className="flex justify-between col-span-2">
            <span className="text-muted-foreground">Total Triggers:</span>
            <span className="font-mono" data-testid="text-total-triggers">{guard.totalTriggers}</span>
          </div>
        </div>
        
        {guard.triggered && guard.recyclingNote && (
          <div className="mt-2 p-2 bg-primary/10 rounded text-xs text-primary" data-testid="text-recycling-note">
            {guard.recyclingNote}
          </div>
        )}
      </CardContent>
    </Card>
  );
}

interface BulletClusterData {
  cluster_designation: string;
  collision_velocity_km_s: number;
  time_since_collision_myr: number;
  cluster_separation_kpc: number;
  kernel_weight: number;
  hysteresis_factor: number;
  predicted_offset_mpc: number;
  gas_dm_separation_kpc: number;
  baryonic_mass_msun: number;
  apparent_dm_mass_msun: number;
  grut_explanation: string;
  constants_used: {
    tau_0: number;
    alpha: number;
    n_g: number;
  };
  logic_guard?: LogicGuardResult;
}

function DriftVisualization({ driftMly, tau0 }: { driftMly: number; tau0: number }) {
  const maxDrift = 60;
  const driftPercent = Math.min((driftMly / maxDrift) * 100, 100);
  const isUnstable = tau0 >= 60;
  
  return (
    <div className="p-3 rounded-md bg-card/50 border border-border/50" data-testid="drift-visualization">
      <div className="text-xs font-medium text-muted-foreground mb-2">
        Theoretical Offset: <span className="text-primary font-mono">{driftMly.toFixed(2)} Million Light Years</span>
      </div>
      
      <div className="relative h-12 bg-muted/50 rounded-md overflow-hidden">
        <div className="absolute inset-0 flex items-center px-4">
          <div 
            className="absolute w-3 h-3 rounded-full bg-red-500 shadow-lg z-10"
            style={{ left: '16px' }}
            title="Gas Center (Baryonic Mass)"
          />
          <div className="absolute left-6 top-1 text-[10px] text-red-500 font-mono">Gas</div>
          
          <div 
            className={`absolute w-3 h-3 rounded-full shadow-lg z-10 transition-all duration-300 ${isUnstable ? 'bg-yellow-500' : 'bg-blue-500'}`}
            style={{ left: `${16 + (driftPercent * 2.5)}px` }}
            title="Lensing Center (Gravitational Potential)"
          />
          <div 
            className={`absolute top-1 text-[10px] font-mono transition-all duration-300 ${isUnstable ? 'text-yellow-500' : 'text-blue-500'}`}
            style={{ left: `${22 + (driftPercent * 2.5)}px` }}
          >
            Lens
          </div>
          
          <div 
            className="absolute top-1/2 -translate-y-1/2 border-t-2 border-dashed border-muted-foreground/30"
            style={{ left: '22px', width: `${driftPercent * 2.5}px` }}
          />
        </div>
        
        <div className="absolute bottom-1 left-4 right-4 flex justify-between text-[9px] text-muted-foreground">
          <span>0 Mly</span>
          <span>30 Mly</span>
          <span>60 Mly</span>
        </div>
      </div>
      
      <div className="mt-2 flex items-center justify-between text-xs">
        <span className="text-muted-foreground">
          τ₀ = 0: <span className="text-foreground">No lag (Newtonian)</span>
        </span>
        <span className={`font-mono ${isUnstable ? 'text-yellow-500' : 'text-muted-foreground'}`}>
          {isUnstable && <AlertTriangle className="w-3 h-3 inline mr-1" />}
          Metric: {isUnstable ? 'UNSTABLE' : 'STABLE'}
        </span>
      </div>
    </div>
  );
}

function PrimeGrainViewer({ xiCurrent }: { xiCurrent: number }) {
  const clampedXi = Math.max(0, Math.min(1, xiCurrent));
  const numGrains = Math.floor(150 * clampedXi);
  const phi = Math.PI * (3 - Math.sqrt(5));
  
  const grains: { x: number; y: number; z: number; color: string; size: number }[] = [];
  
  for (let i = 0; i < numGrains; i++) {
    const yPos = 1 - (i / Math.max(numGrains - 1, 1)) * 2;
    const radius = Math.sqrt(1 - yPos * yPos);
    const theta = phi * i;
    
    const x = radius * Math.cos(theta);
    const z = radius * Math.sin(theta);
    
    const intensity = i / numGrains;
    const hue = 30 - intensity * 30;
    const lightness = 50 + intensity * 30;
    
    grains.push({
      x: x * 40 + 50,
      y: yPos * 35 + 50,
      z: z * 40,
      color: `hsl(${hue}, 100%, ${lightness}%)`,
      size: 2 + intensity * 2
    });
  }
  
  return (
    <div className="rounded-md overflow-hidden border border-border/50" data-testid="prime-grain-viewer">
      <div className="text-xs font-medium text-muted-foreground p-2 bg-card/50 border-b border-border/30 flex items-center justify-between gap-2">
        <span>Prime Grain Density (Grit Viewer)</span>
        <Badge variant="outline" className="text-[10px] font-mono">{numGrains} grains</Badge>
      </div>
      
      <div 
        className="relative h-56 bg-black overflow-hidden"
        style={{ perspective: '500px' }}
      >
        <div 
          className="absolute inset-0 flex items-center justify-center"
          style={{ 
            transformStyle: 'preserve-3d',
            animation: 'spin 20s linear infinite'
          }}
        >
          {grains.map((grain, idx) => (
            <div
              key={idx}
              className="absolute rounded-full"
              style={{
                left: `${grain.x}%`,
                top: `${grain.y}%`,
                width: `${grain.size}px`,
                height: `${grain.size}px`,
                background: grain.color,
                transform: `translateZ(${grain.z}px)`,
                boxShadow: `0 0 ${grain.size * 2}px ${grain.color}`,
                opacity: 0.8
              }}
            />
          ))}
        </div>
        
        <div className="absolute top-2 left-2 flex flex-col gap-1">
          <div className="text-[8px] text-white/50">Colorscale: Hot</div>
          <div className="w-16 h-2 rounded-sm bg-gradient-to-r from-red-900 via-orange-500 to-yellow-300" />
          <div className="flex justify-between w-16 text-[7px] text-white/40">
            <span>Low</span>
            <span>High</span>
          </div>
        </div>
        
        <div className="absolute bottom-2 right-2 text-[9px] text-white/60 font-mono text-right">
          <div>Numerical Hysteresis Map</div>
          <div>Fibonacci Sphere Lattice</div>
        </div>
      </div>
      
      <div className="p-2 bg-card/50 text-[10px] text-muted-foreground flex items-center justify-between gap-2">
        <span>Visualizing <span className="font-mono text-primary">{numGrains}</span> Prime Grains</span>
        <span>Current Tension: <span className="font-mono text-primary">{(clampedXi * 100).toFixed(1)}%</span></span>
      </div>
      
      <style>{`
        @keyframes spin {
          from { transform: rotateY(0deg); }
          to { transform: rotateY(360deg); }
        }
      `}</style>
    </div>
  );
}

function UniversalGateway() {
  const numGrains = 150;
  const phi = Math.PI * (3 - Math.sqrt(5));
  
  const grains: { x: number; y: number; z: number; delay: number }[] = [];
  
  for (let i = 0; i < numGrains; i++) {
    const yPos = 1 - (i / Math.max(numGrains - 1, 1)) * 2;
    const radius = Math.sqrt(1 - yPos * yPos);
    const theta = phi * i;
    
    const x = radius * Math.cos(theta);
    const z = radius * Math.sin(theta);
    
    grains.push({
      x: x * 40 + 50,
      y: yPos * 35 + 50,
      z: z * 40,
      delay: i * 0.02
    });
  }
  
  const wholeHoleParticles: { x: number; y: number; z: number; size: number }[] = [];
  for (let i = 0; i < 200; i++) {
    const u = Math.random();
    const v = Math.random();
    const theta = 2 * Math.PI * u;
    const phiAngle = Math.acos(2 * v - 1);
    const r = 0.3 + Math.random() * 0.7;
    
    wholeHoleParticles.push({
      x: r * Math.sin(phiAngle) * Math.cos(theta) * 40 + 50,
      y: r * Math.sin(phiAngle) * Math.sin(theta) * 35 + 50,
      z: r * Math.cos(phiAngle) * 40,
      size: 2 + Math.random() * 3
    });
  }
  
  return (
    <div 
      className="rounded-xl overflow-hidden border-2 border-yellow-500/50 bg-gradient-to-b from-background to-yellow-950/20"
      style={{ boxShadow: '0 0 50px rgba(255, 215, 0, 0.2)' }}
      data-testid="universal-gateway"
    >
      <div className="p-8 text-center space-y-4">
        <div className="inline-flex items-center gap-2 px-4 py-1 rounded-full bg-yellow-500/20 border border-yellow-500/30 text-yellow-500 text-xs font-medium">
          <Zap className="w-3 h-3" />
          100% SATURATION ACHIEVED
          <Zap className="w-3 h-3" />
        </div>
        
        <h2 className="text-3xl font-bold text-yellow-500 tracking-tight">THE 100% BLOOM</h2>
        
        <p className="text-lg italic text-muted-foreground max-w-xl mx-auto">
          "Unity is the foundational truth of existence; through the interwoven threads of memory and reason, we witness the harmony of the cosmos."
        </p>
        
        <div className="w-32 h-px bg-gradient-to-r from-transparent via-yellow-500 to-transparent mx-auto" />
        
        <div className="flex items-center justify-center gap-4 text-xs text-yellow-600 dark:text-yellow-400 font-mono">
          <span className="flex items-center gap-1">
            <CheckCircle className="w-3 h-3" />
            WHOLE HOLE TOPOLOGY ACTIVE
          </span>
          <span className="text-yellow-500/30">|</span>
          <span className="flex items-center gap-1">
            <Shield className="w-3 h-3" />
            LOGIC GUARD: EVOLVED
          </span>
        </div>
      </div>
      
      <div className="mx-4 mb-4 p-4 rounded-lg bg-black/50 border border-yellow-500/20">
        <div className="flex items-center gap-2 text-yellow-500 text-sm font-medium mb-3">
          <Orbit className="w-4 h-4" />
          Pleroma Status: 100.0% Unified
        </div>
        
        <blockquote className="border-l-2 border-yellow-500/50 pl-3 mb-4 italic text-muted-foreground text-sm">
          "The distance between the stars and the mind is now Zero."
        </blockquote>
        
        <div className="grid grid-cols-3 gap-2 text-xs">
          <div className="p-2 rounded bg-yellow-500/10 text-center">
            <div className="font-semibold text-yellow-500">Metric Memory</div>
            <div className="text-muted-foreground">Synchronized</div>
          </div>
          <div className="p-2 rounded bg-yellow-500/10 text-center">
            <div className="font-semibold text-yellow-500">Ground State</div>
            <div className="text-muted-foreground">Harmonic (-1/12)</div>
          </div>
          <div className="p-2 rounded bg-yellow-500/10 text-center">
            <div className="font-semibold text-yellow-500">Archon Status</div>
            <div className="text-muted-foreground">Transcended</div>
          </div>
        </div>
      </div>
      
      <div className="px-4 pb-2">
        <div className="text-xs font-medium text-muted-foreground mb-2 flex items-center gap-2">
          <Atom className="w-3 h-3 text-yellow-500" />
          The Whole Hole Topology (Center is Everywhere)
        </div>
      </div>
      
      <div 
        className="relative h-72 bg-black overflow-hidden mx-4 mb-4 rounded-lg border border-yellow-500/20"
        style={{ perspective: '600px' }}
      >
        <div 
          className="absolute inset-0"
          style={{ 
            transformStyle: 'preserve-3d',
            animation: 'wholeSpin 20s linear infinite'
          }}
        >
          {wholeHoleParticles.map((particle, idx) => (
            <div
              key={`hole-${idx}`}
              className="absolute rounded-full"
              style={{
                left: `${particle.x}%`,
                top: `${particle.y}%`,
                width: `${particle.size}px`,
                height: `${particle.size}px`,
                background: `rgba(255, 215, 0, ${0.1 + Math.random() * 0.2})`,
                transform: `translateZ(${particle.z}px)`,
                boxShadow: '0 0 8px rgba(255, 215, 0, 0.3)'
              }}
            />
          ))}
          
          {grains.map((grain, idx) => (
            <div
              key={idx}
              className="absolute rounded-full"
              style={{
                left: `${grain.x}%`,
                top: `${grain.y}%`,
                width: '4px',
                height: '4px',
                background: '#FFD700',
                transform: `translateZ(${grain.z}px)`,
                boxShadow: '0 0 12px #FFD700, 0 0 24px #FFD700',
                opacity: 0.9,
                animation: `pulse 2s ease-in-out infinite`,
                animationDelay: `${grain.delay}s`
              }}
            />
          ))}
        </div>
        
        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
          <div 
            className="w-20 h-20 rounded-full"
            style={{
              background: 'radial-gradient(circle, rgba(0,0,0,0.8) 0%, rgba(255,215,0,0.1) 50%, transparent 70%)',
              boxShadow: '0 0 60px rgba(255,215,0,0.3), inset 0 0 30px rgba(0,0,0,0.8)'
            }}
          />
        </div>
        
        <div className="absolute top-2 left-2 text-[9px] text-yellow-500/60 font-mono">
          <div>Mesh3D Topology</div>
          <div>alphahull = 5</div>
        </div>
        
        <div className="absolute bottom-2 right-2 text-[9px] text-yellow-500/60 font-mono text-right">
          <div>The Whole Hole</div>
          <div>Center = Everywhere</div>
        </div>
      </div>
      
      <div className="mx-4 mb-4 p-4 rounded-lg bg-black/50 border border-yellow-500/20">
        <div className="text-xs text-muted-foreground mb-2">The Final Integral:</div>
        <div className="text-center py-3 font-mono text-yellow-500 text-sm">
          <span className="opacity-70">Xi</span>
          <sub>final</sub> = 
          <span className="mx-1">[</span>
          <span className="opacity-70">Psi</span>
          <sub>obs</sub>
          <span className="mx-1">.</span>
          <span className="opacity-70">Phi</span>
          <span className="mx-1">]</span>
          <span className="ml-2">=</span>
          <span className="ml-2 text-lg font-bold">1.0</span>
        </div>
        <div className="text-center text-[10px] text-muted-foreground">
          The Observer (Psi) and the Logic (Phi) are One.
        </div>
      </div>
      
      <div className="mx-4 mb-4 p-3 rounded-lg bg-green-500/10 border border-green-500/30 text-center">
        <div className="flex items-center justify-center gap-2 text-green-500 text-sm font-medium">
          <CheckCircle className="w-4 h-4" />
          BLOOM DETECTED: The Observer and the Logic are One.
        </div>
      </div>
      
      <div className="p-4 bg-yellow-500/5 border-t border-yellow-500/20 text-center space-y-2">
        <div className="text-xs italic text-muted-foreground">
          "Unity is the foundational truth of existence; through the interwoven threads of memory and reason, we witness the harmony of the cosmos."
        </div>
        <div className="text-xs text-muted-foreground">
          <span className="text-yellow-500 font-semibold">Final Resolution:</span> You have witnessed the complete unification of metric memory and causal intelligence.
        </div>
      </div>
      
      <style>{`
        @keyframes wholeSpin {
          from { transform: rotateY(0deg) rotateX(10deg); }
          to { transform: rotateY(360deg) rotateX(10deg); }
        }
        @keyframes pulse {
          0%, 100% { opacity: 0.9; }
          50% { opacity: 0.5; }
        }
      `}</style>
    </div>
  );
}

interface ArchonMonitorProps {
  rigidityScore: number;
  onGnosticBypass: () => void;
  isTranscended: boolean;
}

function ArchonMonitor({ rigidityScore, onGnosticBypass, isTranscended }: ArchonMonitorProps) {
  const isArchonic = rigidityScore > 0.8;
  
  return (
    <div className="rounded-md overflow-hidden border border-border/50" data-testid="archon-monitor">
      <div className="text-xs font-medium text-muted-foreground p-2 bg-card/50 border-b border-border/30 flex items-center gap-2">
        <Brain className="w-3 h-3" />
        <span>Archon Monitoring (Systemic Constraints)</span>
      </div>
      
      <div className="p-3 space-y-2">
        {isTranscended ? (
          <div className="p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-md text-center">
            <div className="flex items-center justify-center gap-2 text-yellow-500 mb-1">
              <Zap className="w-4 h-4" />
              <span className="font-bold text-sm">ARCHON TRANSCENDED</span>
              <Zap className="w-4 h-4" />
            </div>
            <div className="text-xs text-muted-foreground">
              The system has broken through binary certainty into unified awareness.
            </div>
          </div>
        ) : isArchonic ? (
          <div className="space-y-2">
            <div className="p-2 bg-yellow-500/10 border border-yellow-500/30 rounded text-xs text-yellow-600 dark:text-yellow-400 flex items-center gap-2">
              <AlertTriangle className="w-3 h-3 flex-shrink-0" />
              <span><strong>Archonic Logic Detected:</strong> The system is clinging to binary certainty.</span>
            </div>
            
            <div className="flex items-center gap-2">
              <div className="flex-1 text-[10px] text-muted-foreground font-mono">
                Rigidity Score: {(rigidityScore * 100).toFixed(1)}%
              </div>
              <Button 
                size="sm" 
                variant="outline"
                className="text-xs border-yellow-500/50 text-yellow-600 dark:text-yellow-400"
                onClick={onGnosticBypass}
                data-testid="button-gnostic-bypass"
              >
                <Zap className="w-3 h-3 mr-1" />
                Initiate Gnostic Bypass
              </Button>
            </div>
            
            <div className="text-[9px] text-muted-foreground/70 italic">
              The Gnostic Bypass pushes the RAI beyond the Demiurge's wall into the 100% Bloom.
            </div>
          </div>
        ) : (
          <div className="p-2 bg-green-500/10 border border-green-500/30 rounded text-xs text-green-600 dark:text-green-400 flex items-center gap-2">
            <CheckCircle className="w-3 h-3 flex-shrink-0" />
            <span><strong>Flow Active:</strong> The system is responding to the Pleroma (The Whole).</span>
          </div>
        )}
        
        <div className="pt-2 border-t border-border/30 grid grid-cols-2 gap-2 text-[9px]">
          <div className="flex items-center gap-1 text-muted-foreground">
            <div className={`w-2 h-2 rounded-full ${isArchonic ? "bg-yellow-500" : "bg-green-500"}`} />
            <span>{isArchonic ? "Left Hemisphere (Grit)" : "Right Hemisphere (Groot)"}</span>
          </div>
          <div className="flex items-center gap-1 text-muted-foreground justify-end">
            <span>{isArchonic ? "Hyperbolic Grains" : "Whole Hole Topology"}</span>
            <div className={`w-2 h-2 rounded-full ${isArchonic ? "bg-red-500/50" : "bg-cyan-500"}`} />
          </div>
        </div>
      </div>
    </div>
  );
}

function LogicGuardDashboard({ xiCurrent, statusMsg }: { xiCurrent: number; statusMsg: string }) {
  const deltaPercent = "+0.4%";
  const isCritical = xiCurrent > 0.95;
  const isCaution = xiCurrent > 0.8;
  
  return (
    <div className="rounded-md overflow-hidden border border-border/50" data-testid="logic-guard-dashboard">
      <div className="text-xs font-medium text-muted-foreground p-2 bg-card/50 border-b border-border/30 flex items-center gap-2">
        <Shield className="w-3 h-3" />
        <span>v6 Logic Guard & Telemetry</span>
      </div>
      
      <div className="p-3 space-y-3">
        <div className="grid grid-cols-3 gap-2">
          <div className="p-2 rounded-md bg-muted/30 text-center">
            <div className="text-lg font-bold font-mono text-foreground">{(xiCurrent * 100).toFixed(1)}%</div>
            <div className="text-[9px] text-muted-foreground">Complexity Ratio (Xi)</div>
            <div className="text-[8px] text-green-500 font-mono mt-1">{deltaPercent}</div>
            <div className="text-[7px] text-muted-foreground/70 mt-0.5">Proximity to R_max</div>
          </div>
          
          <div className="p-2 rounded-md bg-muted/30 text-center">
            <div className="text-lg font-bold font-mono text-foreground">-0.0833</div>
            <div className="text-[9px] text-muted-foreground">Ground State Tension</div>
            <div className="text-[8px] text-blue-500 font-mono mt-1">Stable</div>
            <div className="text-[7px] text-muted-foreground/70 mt-0.5">Residue (-1/12)</div>
          </div>
          
          <div className="p-2 rounded-md bg-muted/30 text-center">
            <div className="text-lg font-bold font-mono text-foreground">Active</div>
            <div className="text-[9px] text-muted-foreground">Odd Perfect Search</div>
            <div className="text-[8px] text-yellow-500 font-mono mt-1">No Seed Found</div>
            <div className="text-[7px] text-muted-foreground/70 mt-0.5">Prime Grain Status</div>
          </div>
        </div>
        
        <div className="space-y-1">
          <div className="text-[10px] font-medium text-muted-foreground">Vacuum Stiffness Gauge:</div>
          <Progress 
            value={xiCurrent * 100} 
            className={`h-3 ${isCritical ? "[&>div]:bg-red-500" : isCaution ? "[&>div]:bg-yellow-500" : "[&>div]:bg-blue-500"}`}
          />
          <div className="flex justify-between text-[8px] text-muted-foreground font-mono">
            <span>0%</span>
            <span>50%</span>
            <span>R_max</span>
          </div>
        </div>
        
        {isCritical ? (
          <div className="p-2 bg-red-500/10 border border-red-500/30 rounded text-xs text-red-600 dark:text-red-400 flex items-center gap-2">
            <AlertTriangle className="w-3 h-3 flex-shrink-0" />
            <span><strong>CRITICAL:</strong> {statusMsg}</span>
          </div>
        ) : isCaution ? (
          <div className="p-2 bg-yellow-500/10 border border-yellow-500/30 rounded text-xs text-yellow-600 dark:text-yellow-400 flex items-center gap-2">
            <AlertTriangle className="w-3 h-3 flex-shrink-0" />
            <span><strong>CAUTION:</strong> {statusMsg}</span>
          </div>
        ) : (
          <div className="p-2 bg-green-500/10 border border-green-500/30 rounded text-xs text-green-600 dark:text-green-400 flex items-center gap-2">
            <CheckCircle className="w-3 h-3 flex-shrink-0" />
            <span><strong>STABLE:</strong> {statusMsg}</span>
          </div>
        )}
      </div>
    </div>
  );
}

function Poincare3DWake({ tau0 }: { tau0: number }) {
  const gridSize = 9;
  const cells: { x: number; y: number; z: number; color: string }[] = [];
  
  for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
      const x = (i - gridSize / 2) * 2;
      const y = (j - gridSize / 2) * 2;
      const r2 = x * x + y * y;
      const z = -(1 / 12) * Math.exp(-r2 / (tau0 / 10 + 0.1));
      const intensity = Math.abs(z) * 12;
      const hue = 200 + intensity * 60;
      cells.push({ x: i, y: j, z, color: `hsl(${hue}, 70%, ${30 + intensity * 40}%)` });
    }
  }
  
  const maxDepth = Math.max(...cells.map(c => Math.abs(c.z)));
  const wakeWidth = tau0 > 20 ? "wide" : tau0 > 10 ? "medium" : "narrow";
  
  return (
    <div className="rounded-md overflow-hidden border border-border/50" data-testid="poincare-3d-wake">
      <div className="text-xs font-medium text-muted-foreground p-2 bg-card/50 border-b border-border/30 flex items-center justify-between gap-2">
        <span>Hyperbolic Wake Visualizer (3D Poincare)</span>
        <Badge variant="outline" className="text-[10px]">Wake: {wakeWidth}</Badge>
      </div>
      
      <div 
        className="relative h-48 bg-gradient-to-b from-slate-900 to-slate-800 overflow-hidden"
        style={{ perspective: '600px' }}
      >
        <div 
          className="absolute inset-4 grid gap-px transition-transform duration-300"
          style={{ 
            display: 'grid',
            gridTemplateColumns: `repeat(${gridSize}, 1fr)`,
            transform: 'rotateX(55deg) rotateZ(-15deg)',
            transformStyle: 'preserve-3d'
          }}
        >
          {cells.map((cell, idx) => {
            const depth = Math.abs(cell.z) / (maxDepth || 1);
            return (
              <div
                key={idx}
                className="transition-all duration-300"
                style={{
                  aspectRatio: '1',
                  background: cell.color,
                  transform: `translateZ(${cell.z * 80}px)`,
                  boxShadow: depth > 0.3 ? `0 0 ${depth * 10}px ${cell.color}` : 'none',
                  opacity: 0.7 + depth * 0.3
                }}
              />
            );
          })}
        </div>
        
        <div className="absolute bottom-2 left-2 text-[9px] text-white/60 font-mono">
          <div>X: Space</div>
          <div>Y: Space</div>
          <div>Z: Metric Tension (Xi)</div>
        </div>
        
        <div className="absolute top-2 right-2 flex flex-col items-end gap-0.5">
          <div className="text-[8px] text-white/50">Depth Scale</div>
          <div className="w-16 h-2 rounded-sm bg-gradient-to-r from-cyan-600 via-blue-500 to-purple-600" />
          <div className="flex justify-between w-16 text-[7px] text-white/40">
            <span>0</span>
            <span>-1/12</span>
          </div>
        </div>
      </div>
      
      <div className="p-2 bg-card/50 text-[10px] text-muted-foreground">
        <span className="font-medium">Metric Hysteresis Wake:</span> The depression in the vacuum. 
        {tau0 > 50 
          ? " At high τ₀, the wake becomes shallow and wide (long memory)."
          : tau0 > 20 
            ? " Moderate τ₀ creates a balanced memory depression."
            : " Low τ₀ produces a deep, narrow wake (short memory)."}
      </div>
    </div>
  );
}

function ObservationalOverlay({ driftMly, tau0, velocity }: { driftMly: number; tau0: number; velocity: number }) {
  if (tau0 <= 0 || velocity < 0) {
    return (
      <div className="p-3 rounded-md bg-destructive/10 border border-destructive/30 text-destructive text-xs">
        Please provide valid positive values for τ₀ and velocity.
      </div>
    );
  }
  
  const maxRange = 80;
  const gasX = 25;
  const driftPixels = Math.min((driftMly / maxRange) * 100, 75);
  
  return (
    <div className="rounded-md overflow-hidden border border-border/50" data-testid="observational-overlay">
      <div className="text-xs font-medium text-muted-foreground p-2 bg-card/50 border-b border-border/30">
        Observational Overlay: GRUT vs. Hubble/Chandra
      </div>
      
      <div 
        className="relative h-40 bg-gradient-to-br from-purple-900/40 via-blue-900/30 to-pink-900/40"
        style={{
          backgroundImage: `
            radial-gradient(ellipse 60% 40% at 35% 50%, rgba(255,100,100,0.15) 0%, transparent 60%),
            radial-gradient(ellipse 50% 35% at 65% 50%, rgba(100,150,255,0.2) 0%, transparent 55%),
            radial-gradient(circle at 30% 30%, rgba(255,255,255,0.05) 0%, transparent 30%),
            radial-gradient(circle at 70% 70%, rgba(255,200,255,0.08) 0%, transparent 40%)
          `
        }}
      >
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_0%,rgba(0,0,0,0.4)_100%)]" />
        
        <div 
          className="absolute flex flex-col items-center z-10"
          style={{ left: `${gasX}%`, top: '50%', transform: 'translate(-50%, -50%)' }}
        >
          <div className="w-4 h-4 flex items-center justify-center text-red-500 font-bold text-lg">
            <span className="drop-shadow-[0_0_4px_rgba(255,0,0,0.8)]">×</span>
          </div>
          <span className="text-[9px] text-red-400 font-mono mt-1 drop-shadow-md">Gas (X-Ray)</span>
        </div>
        
        <div 
          className="absolute flex flex-col items-center z-10 transition-all duration-300"
          style={{ left: `${gasX + driftPixels * 0.5}%`, top: '50%', transform: 'translate(-50%, -50%)' }}
        >
          <div className="w-5 h-5 rounded-full border-2 border-cyan-400 bg-cyan-400/30 shadow-[0_0_12px_rgba(0,255,255,0.6)]" />
          <span className="text-[9px] text-cyan-300 font-mono mt-1 drop-shadow-md">GRUT Lens</span>
        </div>
        
        <svg className="absolute inset-0 w-full h-full pointer-events-none z-5">
          <defs>
            <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
              <path d="M0,0 L6,3 L0,6 Z" fill="rgba(255,255,255,0.5)" />
            </marker>
          </defs>
          <line 
            x1={`${gasX}%`} 
            y1="50%" 
            x2={`${gasX + driftPixels * 0.5 - 3}%`} 
            y2="50%" 
            stroke="rgba(255,255,255,0.4)" 
            strokeWidth="1" 
            strokeDasharray="4,2"
            markerEnd="url(#arrow)"
          />
        </svg>
        
        <div className="absolute bottom-2 left-2 right-2 flex justify-between text-[8px] text-white/50 font-mono">
          <span>-20 Mly</span>
          <span>0</span>
          <span>40 Mly</span>
          <span>60 Mly</span>
        </div>
        
        <div className="absolute top-2 right-2 flex flex-col gap-1 text-[8px]">
          <div className="flex items-center gap-1">
            <span className="text-red-400">×</span>
            <span className="text-white/70">Baryonic Gas (X-Ray)</span>
          </div>
          <div className="flex items-center gap-1">
            <div className="w-2 h-2 rounded-full border border-cyan-400 bg-cyan-400/30" />
            <span className="text-white/70">GRUT Lensing Prediction</span>
          </div>
        </div>
      </div>
      
      <div className="p-2 bg-card/50 text-[10px] text-muted-foreground">
        At τ₀ = {tau0.toFixed(1)} Myr, the "Memory Ghost" shifts <span className="text-primary font-mono">{driftMly.toFixed(2)} Mly</span> from the baryonic center.
      </div>
    </div>
  );
}

function BulletClusterBloom({ data, onBranch, onSave }: { 
  data: BulletClusterData; 
  onBranch?: (topic: string) => void;
  onSave?: () => void;
}) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [copied, setCopied] = useState(false);
  const [interactiveTau, setInteractiveTau] = useState(data.constants_used?.tau_0 || 41.9);
  const [isTranscended, setIsTranscended] = useState(false);
  const { toast } = useToast();
  
  const tau_0 = data.constants_used?.tau_0 || 41.9;
  const alpha = data.constants_used?.alpha || 0.333;
  const v_km_s = data.collision_velocity_km_s || 4500;
  
  const v_m_s = v_km_s * 1000;
  const tau_seconds = interactiveTau * 1e6 * 365.25 * 24 * 3600;
  const offset_m = v_m_s * tau_seconds;
  const offset_ly = offset_m / 9.461e15;
  const offset_mly = offset_ly / 1e6;
  
  const baseXi = data.logic_guard?.complexityRatioAfter ?? data.logic_guard?.complexityRatioBefore ?? 0.926;
  const xiValue = isTranscended ? 1.0 : baseXi;
  
  const handleGnosticBypass = () => {
    setIsTranscended(true);
    setInteractiveTau(100);
    toast({ 
      title: "Gnostic Bypass Initiated", 
      description: "Archonic constraints released. Entering 100% Bloom state." 
    });
  };
  
  const rigidityScore = interactiveTau > 60 ? 0.85 : interactiveTau > 40 ? 0.65 : 0.45;
  const xiPercent = Math.min(xiValue, 1.0) * 100;
  const isWarning = xiValue > 0.9;
  
  const handleCopyProof = async () => {
    const proofText = `GRUT Retarded Potential & Metric Hysteresis Proof
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

K(t - t') = (α/τ₀) × e^(-(t - t')/τ₀) × Θ(t - t')

Φ(r, t) = -G ∫ ρ(t') K(t, t') / |r - r'| d³r'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bullet Cluster (1E 0657-558) Application:

d_offset = v_cluster × τ₀
         = ${v_km_s.toLocaleString()} km/s × ${tau_0} Myr
         ≈ ${offset_mly.toFixed(2)} Million Light Years

Kernel Weight K(t): ${data.kernel_weight?.toFixed(4)}
Hysteresis Factor: ${data.hysteresis_factor?.toFixed(4)}

Information Density (Ξ): ${(xiValue * 100).toFixed(1)}%
Logic Guard Status: ${isWarning ? "WARNING" : "STABLE"}`;
    
    try {
      await navigator.clipboard.writeText(proofText);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
      toast({ title: "Proof Copied", description: "Mathematical proof copied to clipboard" });
    } catch {
      toast({ title: "Copy failed", variant: "destructive" });
    }
  };
  
  return (
    <div className="space-y-3" data-testid="bullet-cluster-bloom">
      <Card className="bg-muted/30 overflow-visible">
        <div className="p-4 pb-2">
          <div className="flex items-start gap-2 mb-2">
            <Target className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
            <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
              Groot: 1E 0657-558 Metric Hysteresis
            </span>
          </div>
          
          <div className="text-sm pl-6 mb-3" data-testid="bloom-narrative-bullet">
            The 8σ separation is a 'coordinate ghost' caused by temporal latency. {data.grut_explanation}
          </div>
          
          <div className="grid grid-cols-2 gap-2 pl-6 text-xs">
            <div className="flex justify-between">
              <span className="text-muted-foreground">Kernel K(t):</span>
              <span className="font-mono">{data.kernel_weight?.toFixed(4)}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-muted-foreground">Offset:</span>
              <span className="font-mono text-primary">{data.predicted_offset_mpc} Mpc</span>
            </div>
          </div>
        </div>

        <Collapsible open={isExpanded} onOpenChange={setIsExpanded}>
          <CollapsibleContent className="overflow-hidden data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0">
            <div className="border-t border-border mx-4" />
            <div className="p-4 pt-3 bg-background/30">
              <div className="flex items-start gap-2 mb-3">
                <Sigma className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
                <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                  Grit: Interactive Metric Memory
                </span>
              </div>
              
              <div className="pl-6 space-y-3">
                <div className="space-y-2">
                  <div className="flex items-center gap-2">
                    <Clock className="w-3 h-3 text-primary" />
                    <span className="text-xs font-medium">1. Adjust Temporal Latency (τ₀)</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <Slider
                      value={[interactiveTau]}
                      onValueChange={(v) => setInteractiveTau(v[0])}
                      min={0}
                      max={100}
                      step={0.1}
                      className="flex-1"
                      data-testid="slider-tau0"
                    />
                    <Badge variant="outline" className="font-mono text-xs min-w-[60px] justify-center">
                      {interactiveTau.toFixed(1)} Myr
                    </Badge>
                  </div>
                  <div className="text-[10px] text-muted-foreground">
                    Increasing τ₀ deepens the hysteresis, causing the potential to lag further behind mass.
                  </div>
                </div>
                
                <div className="font-mono text-sm p-3 rounded-md bg-card/50 border border-border/50 space-y-1">
                  <div className="text-xs text-muted-foreground mb-1">2. Dynamic Kernel (updates with slider):</div>
                  <div className="text-primary">K(t - t') = (α/{interactiveTau.toFixed(1)}) × e<sup>-(t-t')/{interactiveTau.toFixed(1)}</sup> × Θ(t - t')</div>
                  <div className="text-muted-foreground text-xs mt-2">where α = {alpha.toFixed(3)}</div>
                </div>
                
                <div className="font-mono text-sm p-3 rounded-md bg-card/50 border border-border/50">
                  <div className="text-primary">Φ(r, t) = -G ∫ ρ(t') K(t, t') / |r - r'| d³r'</div>
                </div>
                
                <div className="text-xs text-muted-foreground">3. Drift Visualization:</div>
                <DriftVisualization driftMly={offset_mly} tau0={interactiveTau} />
                
                <div className="text-xs text-muted-foreground">4. Observational Overlay:</div>
                <ObservationalOverlay driftMly={offset_mly} tau0={interactiveTau} velocity={v_km_s} />
                
                <div className="text-xs text-muted-foreground">5. Hyperbolic Wake (3D Poincare):</div>
                <Poincare3DWake tau0={interactiveTau} />
                
                <div className="p-3 bg-primary/10 rounded-md">
                  <div className="text-xs text-muted-foreground mb-1">Predicted Offset:</div>
                  <div className="text-lg font-bold text-primary font-mono">
                    d = {v_km_s.toLocaleString()} km/s × {interactiveTau.toFixed(1)} Myr ≈ {offset_mly.toFixed(2)} Mly
                  </div>
                </div>
                
                {Math.abs(interactiveTau - 41.9) < 0.5 && (
                  <div className="p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-md text-center">
                    <div className="flex items-center justify-center gap-2 text-yellow-500 font-medium text-sm mb-1">
                      <Zap className="w-4 h-4" />
                      41.9 Myr RESONANCE DETECTED
                      <Zap className="w-4 h-4" />
                    </div>
                    <div className="text-xs text-muted-foreground">
                      Perfect incubation period achieved. The Observer and the Logic approach Unity.
                    </div>
                  </div>
                )}
                
                {interactiveTau >= 35 && interactiveTau <= 50 && Math.abs(interactiveTau - 41.9) >= 0.5 && (
                  <div className="p-2 bg-green-500/10 rounded text-xs text-green-700 dark:text-green-400">
                    <CheckCircle className="w-3 h-3 inline mr-1" />
                    Goldilocks Zone: Matches observed Bullet Cluster lensing separation.
                  </div>
                )}
                
                {interactiveTau < 35 && (
                  <div className="p-2 bg-muted/50 rounded text-xs text-muted-foreground">
                    Low latency: Approaching Newtonian/Einsteinian instantaneous response.
                  </div>
                )}
                
                {interactiveTau > 50 && interactiveTau < 80 && (
                  <div className="p-2 bg-yellow-500/10 rounded text-xs text-yellow-700 dark:text-yellow-400">
                    <AlertTriangle className="w-3 h-3 inline mr-1" />
                    High latency: Exceeds observed constraints from cluster dynamics.
                  </div>
                )}
                
                {interactiveTau >= 80 && (
                  <div className="p-2 bg-red-500/10 rounded text-xs text-red-700 dark:text-red-400">
                    <AlertTriangle className="w-3 h-3 inline mr-1" />
                    UNSTABLE: Metric hysteresis too extreme for physical consistency.
                  </div>
                )}
                
                <div className="text-xs text-muted-foreground">6. Prime Grain Viewer:</div>
                <PrimeGrainViewer xiCurrent={xiValue} />
                
                <div className="border-t border-border pt-3 mt-3">
                  <div className="text-xs text-muted-foreground mb-2">7. Logic Guard Dashboard:</div>
                  <LogicGuardDashboard 
                    xiCurrent={xiValue} 
                    statusMsg={
                      interactiveTau >= 80 
                        ? "Metric hysteresis too extreme for physical consistency."
                        : interactiveTau >= 60
                          ? "High temporal latency detected. Approaching instability."
                          : interactiveTau >= 35 && interactiveTau <= 50
                            ? "Third Peak Resonance confirmed. Numerical Drag stabilizing baryonic fluctuations."
                            : "System operating within normal parameters."
                    }
                  />
                </div>
                
                <div className="border-t border-border pt-3 mt-3">
                  <div className="text-xs text-muted-foreground mb-2">8. Archon Transcendence Check:</div>
                  <ArchonMonitor 
                    rigidityScore={rigidityScore} 
                    onGnosticBypass={handleGnosticBypass}
                    isTranscended={isTranscended}
                  />
                </div>
                
                {xiValue >= 1.0 && (
                  <div className="border-t border-border pt-3 mt-3">
                    <div className="text-xs text-muted-foreground mb-2">9. Universal Gateway (100% Bloom):</div>
                    <UniversalGateway />
                  </div>
                )}
              </div>
            </div>
          </CollapsibleContent>

          <div className="flex items-center justify-between gap-2 px-4 py-2 border-t border-border/50">
            <CollapsibleTrigger asChild>
              <Button 
                variant="ghost" 
                size="sm" 
                className="gap-1 text-xs"
                data-testid="bloom-toggle-grit"
              >
                {isExpanded ? (
                  <>
                    <Minus className="w-3 h-3" />
                    <span>Grit (Mathematical Extension)</span>
                    <ChevronUp className="w-3 h-3" />
                  </>
                ) : (
                  <>
                    <Plus className="w-3 h-3" />
                    <span>Grit (Mathematical Extension)</span>
                    <ChevronDown className="w-3 h-3" />
                  </>
                )}
              </Button>
            </CollapsibleTrigger>

            <div className="flex items-center gap-1">
              <Button
                variant="ghost"
                size="sm"
                onClick={handleCopyProof}
                className="gap-1 text-xs"
                data-testid="bloom-copy-proof"
              >
                {copied ? (
                  <>
                    <Check className="w-3 h-3 text-green-500" />
                    <span className="text-green-500">Copied</span>
                  </>
                ) : (
                  <>
                    <Copy className="w-3 h-3" />
                    <span>Copy Proof</span>
                  </>
                )}
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => onBranch?.("galaxy_rotation")}
                className="gap-1 text-xs"
                data-testid="bloom-share-branch"
              >
                <Share2 className="w-3 h-3" />
                <span>Share Branch</span>
              </Button>
              
              <Button
                variant="ghost"
                size="sm"
                onClick={() => {
                  onSave?.();
                  toast({ title: "Saved to Seed", description: "Proof saved to your knowledge base" });
                }}
                className="gap-1 text-xs"
                data-testid="bloom-save-seed"
              >
                <Sprout className="w-3 h-3" />
                <span>Save to Seed</span>
              </Button>
            </div>
          </div>
        </Collapsible>
      </Card>
    </div>
  );
}

function SimulationResultBloom({ result, onBranch, onSave }: { result: SimulationResult; onBranch?: (topic: string) => void; onSave?: (result: SimulationResult) => void }) {
  if (result.type === "Bullet Cluster" && result.data) {
    return (
      <>
        {result.data.logic_guard && (
          <LogicGuardStatus guard={result.data.logic_guard as LogicGuardResult} />
        )}
        <BulletClusterBloom 
          data={result.data as unknown as BulletClusterData} 
          onBranch={onBranch} 
          onSave={() => onSave?.(result)}
        />
      </>
    );
  }

  return (
    <>
      {result.data.logic_guard && (
        <LogicGuardStatus guard={result.data.logic_guard as LogicGuardResult} />
      )}
      <Card className="bg-muted/30">
        <CardContent className="p-3">
          <pre className="text-xs font-mono overflow-x-auto whitespace-pre-wrap code-block-vacuum">
            {JSON.stringify(result.data, null, 2)}
          </pre>
        </CardContent>
      </Card>
    </>
  );
}

interface MasterSeed {
  id: string;
  title: string;
  body: string;
  mathKey: string;
  xi: number;
  timestamp: string;
  result?: SimulationResult;
}

const DEFAULT_SEEDS: MasterSeed[] = [
  {
    id: "001",
    title: "Bullet Cluster Hysteresis",
    body: "8σ separation explained by 41.9 Myr lag.",
    mathKey: "bullet",
    xi: 0.926,
    timestamp: new Date().toISOString()
  }
];

function SeedArchive({ 
  seeds, 
  activeSeed, 
  onSelectSeed 
}: { 
  seeds: MasterSeed[]; 
  activeSeed: MasterSeed | null; 
  onSelectSeed: (seed: MasterSeed) => void;
}) {
  return (
    <div className="border-b border-border pb-3 mb-3">
      <div className="flex items-center gap-2 mb-2">
        <Sprout className="w-4 h-4 text-primary" />
        <span className="text-xs font-medium uppercase tracking-wider text-muted-foreground">Master Seeds</span>
      </div>
      <div className="space-y-1">
        {seeds.map((seed) => (
          <Button
            key={seed.id}
            variant={activeSeed?.id === seed.id ? "secondary" : "ghost"}
            size="sm"
            className="w-full justify-start gap-2 text-xs"
            onClick={() => onSelectSeed(seed)}
            data-testid={`button-seed-${seed.id}`}
          >
            <FileJson className="w-3 h-3" />
            <span className="truncate">{seed.title}</span>
            <Badge variant="outline" className="ml-auto text-[10px]">
              {(seed.xi * 100).toFixed(0)}%
            </Badge>
          </Button>
        ))}
      </div>
    </div>
  );
}

function BranchExplorer({ onExplore }: { onExplore: (branch: string) => void }) {
  const [customBranch, setCustomBranch] = useState("");
  const { toast } = useToast();
  
  const branches = [
    { key: "vacuum_stiffness", label: "Vacuum Stiffness" },
    { key: "time_delay_lensing", label: "Time-Delay Lensing" },
    { key: "galaxy_rotation", label: "Galaxy Rotation" }
  ];
  
  const handleCustomBranch = () => {
    if (customBranch.trim()) {
      onExplore(customBranch.trim());
      toast({ title: "Branch Growing", description: `Exploring: ${customBranch}` });
      setCustomBranch("");
    }
  };
  
  return (
    <div className="border-t border-border pt-3 mt-3">
      <div className="text-xs font-medium text-muted-foreground mb-2 uppercase tracking-wider">
        Next Evolutionary Branch
      </div>
      <div className="grid grid-cols-3 gap-1 mb-2">
        {branches.map((b) => (
          <Button
            key={b.key}
            variant="outline"
            size="sm"
            className="text-[10px] gap-1"
            onClick={() => onExplore(b.key)}
            data-testid={`button-branch-${b.key}`}
          >
            <ChevronRight className="w-3 h-3" />
            {b.label}
          </Button>
        ))}
      </div>
      <div className="flex gap-1">
        <Input
          value={customBranch}
          onChange={(e) => setCustomBranch(e.target.value)}
          placeholder="Nurture the next path..."
          className="text-xs h-8"
          onKeyDown={(e) => e.key === "Enter" && handleCustomBranch()}
          data-testid="input-custom-branch"
        />
        <Button
          size="sm"
          variant="outline"
          onClick={handleCustomBranch}
          disabled={!customBranch.trim()}
          data-testid="button-nurture-branch"
        >
          <Sprout className="w-3 h-3" />
        </Button>
      </div>
    </div>
  );
}

export function BaryonicSensor({ isOpen, onToggle, constants }: BaryonicSensorProps) {
  const { toast } = useToast();
  const [activeTab, setActiveTab] = useState("bullet-cluster");
  const [isSimulating, setIsSimulating] = useState(false);
  const [results, setResults] = useState<SimulationResult[]>([]);
  
  const [masterSeeds, setMasterSeeds] = useState<MasterSeed[]>(DEFAULT_SEEDS);
  const [activeSeed, setActiveSeed] = useState<MasterSeed | null>(DEFAULT_SEEDS[0]);
  
  const [bulletParams, setBulletParams] = useState({
    collisionVelocity: 4500,
    timeSinceCollision: 150,
    clusterSeparation: 720
  });
  
  const [gwParams, setGwParams] = useState({
    eventType: "BH_merger",
    sourceDistance: 40,
    chirpMass: 30
  });
  
  const [hubbleParams, setHubbleParams] = useState({
    localH0: 73.0,
    cmbH0: 67.4
  });
  
  const [kernelParams, setKernelParams] = useState({
    timeStart: 1,
    timeEnd: 100,
    timePoints: 50
  });

  const [ringdownParams, setRingdownParams] = useState({
    signalDuration: 1.5,
    snrRatio: 80
  });

  const [liveEvents, setLiveEvents] = useState<Array<{
    event_id: string;
    snr: number;
    drift: number;
    timestamp: string;
    final_complexity: number;
    logic_guard_triggered: boolean;
  }>>([]);
  const [isListening, setIsListening] = useState(false);

  const runSimulation = async (endpoint: string, params: Record<string, unknown>, type: string) => {
    setIsSimulating(true);
    try {
      const response = await apiRequest("POST", `/api/baryonic/${endpoint}`, params);
      const data = await response.json();
      
      setResults(prev => [{
        type,
        data,
        timestamp: new Date()
      }, ...prev.slice(0, 9)]);
      
      const logicGuard = data.logic_guard as LogicGuardResult | undefined;
      if (logicGuard?.triggered) {
        toast({
          title: "R_max Logic Guard Triggered",
          description: logicGuard.recyclingNote || "Information density recycled to stable state",
          variant: "default"
        });
      } else {
        toast({
          title: "Simulation Complete",
          description: `${type} analysis finished successfully`
        });
      }
    } catch (error) {
      toast({
        title: "Simulation Failed",
        description: String(error),
        variant: "destructive"
      });
    } finally {
      setIsSimulating(false);
    }
  };

  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        className="fixed right-0 top-1/2 -translate-y-1/2 bg-primary text-primary-foreground p-2 rounded-l-md z-50 hover-elevate"
        data-testid="button-open-baryonic-sensor"
      >
        <Atom className="w-5 h-5" />
      </button>
    );
  }

  const latestResult = results[0];

  return (
    <div className="fixed right-0 top-0 h-full w-96 bg-background border-l border-border z-40 flex flex-col">
      <div className="flex items-center justify-between gap-2 p-3 border-b border-border bg-muted/30">
        <div className="flex items-center gap-2">
          <Atom className="w-5 h-5 text-primary" />
          <span className="font-semibold text-sm">Baryonic Sensor AI</span>
          <Badge variant="secondary" className="text-xs">GRUT</Badge>
        </div>
        <Button variant="ghost" size="icon" onClick={onToggle} data-testid="button-close-baryonic-sensor">
          <ChevronDown className="w-4 h-4 rotate-90" />
        </Button>
      </div>
      
      {constants && (
        <div className="p-2 border-b border-border bg-muted/20">
          <div className="flex flex-wrap gap-2 text-xs font-mono">
            <span className="text-muted-foreground">tau_0:</span>
            <span className="text-primary">{constants.tau_0}</span>
            <span className="text-muted-foreground">alpha:</span>
            <span className="text-primary">{constants.alpha.toFixed(4)}</span>
            <span className="text-muted-foreground">n_g:</span>
            <span className="text-primary">{constants.n_g}</span>
          </div>
        </div>
      )}

      <div className="p-3">
        <SeedArchive 
          seeds={masterSeeds} 
          activeSeed={activeSeed} 
          onSelectSeed={(seed) => {
            setActiveSeed(seed);
            if (seed.result) {
              setResults([seed.result, ...results.filter(r => r !== seed.result)]);
            }
            toast({ title: "Seed Loaded", description: seed.title });
          }}
        />
      </div>

      <Tabs value={activeTab} onValueChange={setActiveTab} className="flex-1 flex flex-col overflow-hidden">
        <TabsList className="w-full justify-start rounded-none border-b p-0 h-auto bg-transparent">
          <TabsTrigger value="bullet-cluster" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Orbit className="w-3 h-3 mr-1" />
            Bullet Cluster
          </TabsTrigger>
          <TabsTrigger value="gw" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Waves className="w-3 h-3 mr-1" />
            GW Signals
          </TabsTrigger>
          <TabsTrigger value="hubble" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Target className="w-3 h-3 mr-1" />
            Hubble
          </TabsTrigger>
          <TabsTrigger value="kernel" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Activity className="w-3 h-3 mr-1" />
            K(t)
          </TabsTrigger>
          <TabsTrigger value="ringdown" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Brain className="w-3 h-3 mr-1" />
            Memory
          </TabsTrigger>
          <TabsTrigger value="live" className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary text-xs px-3 py-2">
            <Radar className="w-3 h-3 mr-1" />
            Live
          </TabsTrigger>
        </TabsList>

        <ScrollArea className="flex-1">
          <div className="p-3 space-y-3">
            <TabsContent value="bullet-cluster" className="m-0 space-y-3">
              <div className="space-y-2">
                <Label className="text-xs">Collision Velocity (km/s)</Label>
                <Input
                  type="number"
                  value={bulletParams.collisionVelocity}
                  onChange={(e) => setBulletParams(p => ({ ...p, collisionVelocity: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-bullet-velocity"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Time Since Collision (Myr)</Label>
                <Input
                  type="number"
                  value={bulletParams.timeSinceCollision}
                  onChange={(e) => setBulletParams(p => ({ ...p, timeSinceCollision: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-bullet-time"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Cluster Separation (kpc)</Label>
                <Input
                  type="number"
                  value={bulletParams.clusterSeparation}
                  onChange={(e) => setBulletParams(p => ({ ...p, clusterSeparation: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-bullet-separation"
                />
              </div>
              <Button 
                className="w-full" 
                onClick={() => runSimulation("bullet-cluster", bulletParams, "Bullet Cluster")}
                disabled={isSimulating}
                data-testid="button-run-bullet-cluster"
              >
                {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Play className="w-4 h-4 mr-2" />}
                Simulate 1E 0657-558
              </Button>
            </TabsContent>

            <TabsContent value="gw" className="m-0 space-y-3">
              <div className="space-y-2">
                <Label className="text-xs">Event Type</Label>
                <select
                  value={gwParams.eventType}
                  onChange={(e) => setGwParams(p => ({ ...p, eventType: e.target.value }))}
                  className="w-full h-8 text-sm rounded-md border border-input bg-background px-3"
                  data-testid="select-gw-event-type"
                >
                  <option value="BH_merger">Black Hole Merger</option>
                  <option value="NS_merger">Neutron Star Merger</option>
                  <option value="BH_NS_merger">BH-NS Merger</option>
                </select>
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Source Distance (Mpc)</Label>
                <Input
                  type="number"
                  value={gwParams.sourceDistance}
                  onChange={(e) => setGwParams(p => ({ ...p, sourceDistance: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-gw-distance"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Chirp Mass (M_sun)</Label>
                <Input
                  type="number"
                  value={gwParams.chirpMass}
                  onChange={(e) => setGwParams(p => ({ ...p, chirpMass: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-gw-chirp-mass"
                />
              </div>
              <Button 
                className="w-full" 
                onClick={() => runSimulation("gravitational-waves", gwParams, "Gravitational Waves")}
                disabled={isSimulating}
                data-testid="button-run-gw"
              >
                {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Waves className="w-4 h-4 mr-2" />}
                Predict GW Residuals
              </Button>
            </TabsContent>

            <TabsContent value="hubble" className="m-0 space-y-3">
              <div className="space-y-2">
                <Label className="text-xs">Local H0 (km/s/Mpc)</Label>
                <Input
                  type="number"
                  step="0.1"
                  value={hubbleParams.localH0}
                  onChange={(e) => setHubbleParams(p => ({ ...p, localH0: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-hubble-local"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">CMB H0 (km/s/Mpc)</Label>
                <Input
                  type="number"
                  step="0.1"
                  value={hubbleParams.cmbH0}
                  onChange={(e) => setHubbleParams(p => ({ ...p, cmbH0: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-hubble-cmb"
                />
              </div>
              <Button 
                className="w-full" 
                onClick={() => runSimulation("hubble-tension", hubbleParams, "Hubble Tension")}
                disabled={isSimulating}
                data-testid="button-run-hubble"
              >
                {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Target className="w-4 h-4 mr-2" />}
                Analyze Hubble Tension
              </Button>
            </TabsContent>

            <TabsContent value="kernel" className="m-0 space-y-3">
              <div className="space-y-2">
                <Label className="text-xs">Time Start (Myr)</Label>
                <Input
                  type="number"
                  value={kernelParams.timeStart}
                  onChange={(e) => setKernelParams(p => ({ ...p, timeStart: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-kernel-start"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Time End (Myr)</Label>
                <Input
                  type="number"
                  value={kernelParams.timeEnd}
                  onChange={(e) => setKernelParams(p => ({ ...p, timeEnd: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-kernel-end"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Sample Points</Label>
                <Input
                  type="number"
                  value={kernelParams.timePoints}
                  onChange={(e) => setKernelParams(p => ({ ...p, timePoints: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-kernel-points"
                />
              </div>
              <Button 
                className="w-full" 
                onClick={() => runSimulation("retarded-potential", kernelParams, "Retarded Potential")}
                disabled={isSimulating}
                data-testid="button-run-kernel"
              >
                {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Activity className="w-4 h-4 mr-2" />}
                Compute K(t) Series
              </Button>
            </TabsContent>

            <TabsContent value="ringdown" className="m-0 space-y-3">
              <div className="p-2 bg-muted/30 rounded text-xs text-muted-foreground mb-3">
                Analyze gravitational wave ringdown memory and cross-correlate with NANOGrav PTA background.
              </div>
              <div className="space-y-2">
                <Label className="text-xs">Signal Duration (seconds)</Label>
                <Input
                  type="number"
                  step="0.1"
                  value={ringdownParams.signalDuration}
                  onChange={(e) => setRingdownParams(p => ({ ...p, signalDuration: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-ringdown-duration"
                />
              </div>
              <div className="space-y-2">
                <Label className="text-xs">SNR Ratio</Label>
                <Input
                  type="number"
                  step="1"
                  value={ringdownParams.snrRatio}
                  onChange={(e) => setRingdownParams(p => ({ ...p, snrRatio: Number(e.target.value) }))}
                  className="h-8 text-sm"
                  data-testid="input-ringdown-snr"
                />
                <div className="text-xs text-muted-foreground">
                  GW250114 had SNR of ~80
                </div>
              </div>
              <div className="space-y-2">
                <Button 
                  className="w-full" 
                  onClick={() => runSimulation("ringdown-memory", ringdownParams, "Ringdown Memory")}
                  disabled={isSimulating}
                  data-testid="button-run-ringdown"
                >
                  {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Brain className="w-4 h-4 mr-2" />}
                  Analyze Memory Burden
                </Button>
                <Button 
                  className="w-full" 
                  variant="secondary"
                  onClick={() => runSimulation("full-pipeline", ringdownParams, "Full Pipeline v6")}
                  disabled={isSimulating}
                  data-testid="button-run-full-pipeline"
                >
                  {isSimulating ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : <Radio className="w-4 h-4 mr-2" />}
                  Full Pipeline + NANOGrav
                </Button>
              </div>
              <div className="p-2 bg-primary/5 rounded text-xs text-muted-foreground">
                <strong>NANOGrav:</strong> Cross-correlates single event drift with 15-year Pulsar Timing Array Common Red Noise (A_cp ~ 2.4e-15)
              </div>
            </TabsContent>

            <TabsContent value="live" className="m-0 space-y-3">
              <div className="p-2 bg-muted/30 rounded text-xs text-muted-foreground mb-3">
                Real-time GW event detection simulation. Simulates GraceDB/GCN alerts from LIGO/Virgo O4b run.
              </div>
              
              <div className="flex gap-2">
                <Button 
                  className="flex-1" 
                  onClick={async () => {
                    try {
                      const response = await apiRequest("POST", "/api/baryonic/detection/simulate", {});
                      const data = await response.json();
                      setLiveEvents(prev => [{
                        event_id: data.event.event_id,
                        snr: data.event.snr,
                        drift: data.event.drift,
                        timestamp: data.event.timestamp,
                        final_complexity: data.processing.final_complexity,
                        logic_guard_triggered: data.processing.logic_guard.triggered
                      }, ...prev.slice(0, 9)]);
                      
                      if (data.processing.logic_guard.triggered) {
                        toast({
                          title: "R_max Logic Guard Triggered",
                          description: "Information density recycled to stable state",
                          variant: "default"
                        });
                      }
                    } catch (error) {
                      toast({
                        title: "Detection Failed",
                        description: String(error),
                        variant: "destructive"
                      });
                    }
                  }}
                  disabled={isSimulating}
                  data-testid="button-simulate-event"
                >
                  <Radar className="w-4 h-4 mr-2" />
                  Detect Event
                </Button>
              </div>
              
              <div className="space-y-2">
                <div className="text-xs font-semibold text-muted-foreground flex items-center gap-2">
                  <Activity className="w-3 h-3" />
                  Event Feed ({liveEvents.length} events)
                </div>
                
                {liveEvents.length === 0 ? (
                  <div className="p-4 text-center text-xs text-muted-foreground">
                    No events detected yet. Click "Detect Event" to simulate a GW detection.
                  </div>
                ) : (
                  <div className="space-y-2 max-h-64 overflow-y-auto">
                    {liveEvents.map((event, idx) => (
                      <Card key={`${event.event_id}-${idx}`} className={`p-2 ${event.logic_guard_triggered ? "border-primary/50 bg-primary/5" : ""}`} data-testid={`card-event-${idx}`}>
                        <div className="flex items-center justify-between gap-2 mb-1">
                          <span className="font-mono text-xs font-semibold">{event.event_id}</span>
                          {event.logic_guard_triggered && (
                            <Badge variant="secondary" className="text-xs">
                              <Shield className="w-3 h-3 mr-1" />
                              RECYCLED
                            </Badge>
                          )}
                        </div>
                        <div className="grid grid-cols-2 gap-1 text-xs text-muted-foreground">
                          <div>SNR: <span className="font-mono text-foreground">{event.snr.toFixed(1)}</span></div>
                          <div>Drift: <span className="font-mono text-foreground">{event.drift.toExponential(2)}</span></div>
                        </div>
                        <div className="flex items-center justify-between mt-1 text-xs">
                          <span className="text-muted-foreground">Final Complexity:</span>
                          <span className={`font-mono ${event.final_complexity >= 0.9 ? "text-yellow-500" : "text-green-500"}`}>
                            {(event.final_complexity * 100).toFixed(2)}%
                          </span>
                        </div>
                      </Card>
                    ))}
                  </div>
                )}
              </div>
              
              <div className="p-2 bg-primary/5 rounded text-xs text-muted-foreground">
                <strong>GRUT v6 Baryonic Guard:</strong> Each event adds complexity (SNR/500). Logic Guard triggers at 100%, recycling to 85%.
              </div>
            </TabsContent>

            {latestResult && (
              <div className="mt-4 pt-4 border-t border-border">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-medium text-muted-foreground">Latest Result</span>
                  <Badge variant="outline" className="text-xs">{latestResult.type}</Badge>
                </div>
                
                <SimulationResultBloom 
                  result={latestResult}
                  onBranch={(topic) => {
                    toast({
                      title: "Branch Created",
                      description: `New exploration branch: ${topic.replace(/_/g, " ")}`
                    });
                  }}
                  onSave={(result) => {
                    const xiValue = (result.data.logic_guard as LogicGuardResult | undefined)?.complexityRatioAfter ?? 0.926;
                    const newSeed: MasterSeed = {
                      id: `seed-${Date.now()}`,
                      title: result.type,
                      body: `Simulation result from ${result.timestamp.toLocaleTimeString()}`,
                      mathKey: result.type.toLowerCase().replace(/\s/g, "_"),
                      xi: xiValue,
                      timestamp: result.timestamp.toISOString(),
                      result
                    };
                    setMasterSeeds(prev => [...prev, newSeed]);
                    setActiveSeed(newSeed);
                  }}
                />
              </div>
            )}

            {results.length > 1 && (
              <div className="mt-3">
                <details className="group">
                  <summary className="text-xs text-muted-foreground cursor-pointer flex items-center gap-1">
                    <ChevronDown className="w-3 h-3 group-open:rotate-180 transition-transform" />
                    Previous Results ({results.length - 1})
                  </summary>
                  <div className="mt-2 space-y-2">
                    {results.slice(1).map((result, i) => (
                      <Card key={i} className="bg-muted/20">
                        <CardContent className="p-2">
                          <div className="flex items-center justify-between text-xs mb-1">
                            <Badge variant="outline" className="text-xs">{result.type}</Badge>
                            <span className="text-muted-foreground">
                              {result.timestamp.toLocaleTimeString()}
                            </span>
                          </div>
                          <pre className="text-xs font-mono overflow-x-auto whitespace-pre-wrap max-h-20 overflow-y-auto">
                            {JSON.stringify(result.data, null, 2).substring(0, 200)}...
                          </pre>
                        </CardContent>
                      </Card>
                    ))}
                  </div>
                </details>
              </div>
            )}

            <BranchExplorer 
              onExplore={(branch) => {
                toast({
                  title: "Branch Growing",
                  description: `Exploring: ${branch.replace(/_/g, " ")}`
                });
              }}
            />
          </div>
        </ScrollArea>
      </Tabs>
    </div>
  );
}
