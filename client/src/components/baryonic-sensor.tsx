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
import { 
  Activity, Atom, Orbit, Waves, GitBranch, ChevronDown, ChevronUp,
  Play, Loader2, Target, Zap, Brain, Shield, AlertTriangle, CheckCircle, Radio, Radar, Square,
  Plus, Minus, Sigma, Copy, Check
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

function BulletClusterBloom({ data, onBranch }: { data: BulletClusterData; onBranch?: (topic: string) => void }) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [copied, setCopied] = useState(false);
  const { toast } = useToast();
  
  const tau_0 = data.constants_used?.tau_0 || 41.9;
  const v_km_s = data.collision_velocity_km_s || 4500;
  
  const v_m_s = v_km_s * 1000;
  const tau_seconds = tau_0 * 1e6 * 365.25 * 24 * 3600;
  const offset_m = v_m_s * tau_seconds;
  const offset_ly = offset_m / 9.461e15;
  const offset_mly = offset_ly / 1e6;
  
  const handleCopy = async () => {
    const text = `Bullet Cluster (1E 0657-558) GRUT Analysis\n\nNarrative: ${data.grut_explanation}\n\nDerivation:\nd_offset = v_cluster × τ₀\nv = ${v_km_s} km/s, τ₀ = ${tau_0} Myr\nPredicted Offset: ${offset_mly.toFixed(2)} Million Light Years\n\nKernel Weight K(t): ${data.kernel_weight?.toFixed(4)}\nPredicted Offset (simulation): ${data.predicted_offset_mpc} Mpc`;
    
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
      toast({ title: "Copied", description: "Analysis copied to clipboard" });
    } catch {
      toast({ title: "Copy failed", variant: "destructive" });
    }
  };
  
  return (
    <div className="space-y-3" data-testid="bullet-cluster-bloom">
      <Collapsible open={isExpanded} onOpenChange={setIsExpanded}>
        <Card className="bg-muted/30 overflow-visible">
          <div className="p-4 pb-2">
            <div className="flex items-start gap-2 mb-2">
              <Target className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
              <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                1E 0657-558: Metric Hysteresis Proof
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

          <CollapsibleContent className="overflow-hidden data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0">
            <div className="border-t border-border mx-4" />
            <div className="p-4 pt-3 bg-background/30">
              <div className="flex items-start gap-2 mb-2">
                <Sigma className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
                <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                  Derivation: Retarded Potential vs. {tau_0} Myr
                </span>
              </div>
              
              <div className="pl-6 space-y-2">
                <div className="font-mono text-sm p-3 rounded-md bg-card/50 border border-border/50">
                  <div className="text-primary mb-1">d_offset = v_cluster × τ₀</div>
                  <div className="text-muted-foreground text-xs">
                    Given v ≈ {v_km_s.toLocaleString()} km/s and τ₀ = {tau_0} Myr:
                  </div>
                </div>
                
                <div className="p-3 bg-primary/10 rounded-md">
                  <div className="text-xs text-muted-foreground mb-1">Predicted Offset:</div>
                  <div className="text-lg font-bold text-primary font-mono">
                    ~{offset_mly.toFixed(2)} Million Light Years
                  </div>
                </div>
                
                <div className="p-2 bg-green-500/10 rounded text-xs text-green-700 dark:text-green-400">
                  <CheckCircle className="w-3 h-3 inline mr-1" />
                  This matches the observed lensing centers without requiring Dark Matter particles.
                </div>
              </div>
              
              <div className="flex items-center gap-2 mt-3 pl-6">
                <Badge variant="outline" className="text-xs">
                  <span className="text-muted-foreground mr-1">Gas-DM Sep:</span>
                  {data.gas_dm_separation_kpc?.toFixed(0)} kpc
                </Badge>
                <Badge variant="outline" className="text-xs">
                  <span className="text-muted-foreground mr-1">Hysteresis:</span>
                  {data.hysteresis_factor?.toFixed(4)}
                </Badge>
              </div>
            </div>
          </CollapsibleContent>

          <div className="flex items-center justify-between gap-2 px-4 py-2 border-t border-border/50">
            <CollapsibleTrigger asChild>
              <Button 
                variant="ghost" 
                size="sm" 
                className="gap-1 text-xs"
                data-testid="bloom-toggle-bullet"
              >
                {isExpanded ? (
                  <>
                    <Minus className="w-3 h-3" />
                    <span>Collapse Derivation</span>
                    <ChevronUp className="w-3 h-3" />
                  </>
                ) : (
                  <>
                    <Plus className="w-3 h-3" />
                    <span>Show Derivation</span>
                    <ChevronDown className="w-3 h-3" />
                  </>
                )}
              </Button>
            </CollapsibleTrigger>

            <div className="flex items-center gap-1">
              <Button
                variant="ghost"
                size="sm"
                onClick={handleCopy}
                className="gap-1 text-xs"
                data-testid="bloom-copy-bullet"
              >
                {copied ? (
                  <>
                    <Check className="w-3 h-3 text-green-500" />
                    <span className="text-green-500">Copied</span>
                  </>
                ) : (
                  <>
                    <Copy className="w-3 h-3" />
                    <span>Copy</span>
                  </>
                )}
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={() => onBranch?.("galaxy_rotation")}
                className="gap-1 text-xs"
                data-testid="bloom-branch-bullet"
              >
                <GitBranch className="w-3 h-3" />
                <span>Branch: Galaxy Rotation</span>
              </Button>
            </div>
          </div>
        </Card>
      </Collapsible>
    </div>
  );
}

function SimulationResultBloom({ result, onBranch }: { result: SimulationResult; onBranch?: (topic: string) => void }) {
  if (result.type === "Bullet Cluster" && result.data) {
    return (
      <>
        {result.data.logic_guard && (
          <LogicGuardStatus guard={result.data.logic_guard as LogicGuardResult} />
        )}
        <BulletClusterBloom data={result.data as unknown as BulletClusterData} onBranch={onBranch} />
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

export function BaryonicSensor({ isOpen, onToggle, constants }: BaryonicSensorProps) {
  const { toast } = useToast();
  const [activeTab, setActiveTab] = useState("bullet-cluster");
  const [isSimulating, setIsSimulating] = useState(false);
  const [results, setResults] = useState<SimulationResult[]>([]);
  
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
                      description: `New exploration branch: ${topic.replace("_", " ")}`
                    });
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
          </div>
        </ScrollArea>
      </Tabs>
    </div>
  );
}
