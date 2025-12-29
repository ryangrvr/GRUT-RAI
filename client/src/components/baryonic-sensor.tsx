import { useState } from "react";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { ScrollArea } from "@/components/ui/scroll-area";
import { 
  Activity, Atom, Orbit, Waves, GitBranch, ChevronDown, ChevronUp,
  Play, Loader2, Target, Zap, Brain
} from "lucide-react";
import { apiRequest } from "@/lib/queryClient";
import { useToast } from "@/hooks/use-toast";

interface SimulationResult {
  type: string;
  data: Record<string, unknown>;
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
      
      toast({
        title: "Simulation Complete",
        description: `${type} analysis finished successfully`
      });
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

            {latestResult && (
              <div className="mt-4 pt-4 border-t border-border">
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-medium text-muted-foreground">Latest Result</span>
                  <Badge variant="outline" className="text-xs">{latestResult.type}</Badge>
                </div>
                <Card className="bg-muted/30">
                  <CardContent className="p-3">
                    <pre className="text-xs font-mono overflow-x-auto whitespace-pre-wrap code-block-vacuum">
                      {JSON.stringify(latestResult.data, null, 2)}
                    </pre>
                  </CardContent>
                </Card>
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
