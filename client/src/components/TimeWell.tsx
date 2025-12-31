import { useState, useRef, useEffect, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Slider } from "@/components/ui/slider";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { 
  Dna, 
  Clock, 
  AlertTriangle, 
  Activity, 
  Waves,
  History,
  Shield,
  Trash2,
  Save,
  RotateCcw
} from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { apiRequest, queryClient } from "@/lib/queryClient";
import { useQuery, useMutation } from "@tanstack/react-query";

const COSMIC_AGE_MYR = 13800;
const TIPPING_POINT_MYR = 0.00038;
const GROUND_STATE = -1 / 12;
const TAU_MYR = 41.9;

interface TimeWellMetrics {
  rMaxTriggered: boolean;
  anchorPointMyr: number;
  groundStateDecay: number | null;
  reconstructionAccuracy: number;
  kernelSeed?: number[];
  standingWavePattern?: number[];
  distanceFromPresent?: number;
  cycleNumber?: number;
  grut_insight?: string;
  error?: string;
  message?: string;
  safetyLimit?: number;
}

interface HistoricalResonance {
  id: string;
  biologicalMarker: string;
  anchorPointMyr: number;
  groundStateDecay: number;
  reconstructionAccuracy: number;
  standingWavePattern?: number[];
  rMaxTriggered?: boolean;
  notes?: string;
  createdAt: string;
}

export function TimeWell() {
  const { toast } = useToast();
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const animationRef = useRef<number | null>(null);
  
  const [biologicalMarker, setBiologicalMarker] = useState("");
  const [anchorPointMyr, setAnchorPointMyr] = useState(COSMIC_AGE_MYR);
  const [metrics, setMetrics] = useState<TimeWellMetrics | null>(null);
  const [isSyncing, setIsSyncing] = useState(false);
  const [notes, setNotes] = useState("");

  const { data: resonancesData } = useQuery<{ resonances: HistoricalResonance[] }>({
    queryKey: ["/api/time-well/resonances"],
  });

  const calculateMutation = useMutation({
    mutationFn: async (data: { biologicalMarker: string; anchorPointMyr: number }) => {
      const response = await fetch("/api/time-well/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(data)
      });
      const responseData = await response.json();
      
      if (response.status === 403) {
        setMetrics({
          rMaxTriggered: true,
          anchorPointMyr: data.anchorPointMyr,
          groundStateDecay: null,
          reconstructionAccuracy: 0,
          error: "R_MAX_LOGIC_GUARD_TRIGGERED",
          message: responseData.message || "Tipping Point boundary reached."
        });
        setIsSyncing(false);
        toast({
          title: "R_MAX LOGIC GUARD TRIGGERED",
          description: "Cannot look beyond the Tipping Point (0.00038 Myr). Vacuum Reset initiated.",
          variant: "destructive"
        });
        throw new Error("R_MAX_TRIGGERED");
      }
      
      if (!response.ok) {
        throw new Error(responseData.error || "Calculation failed");
      }
      
      return responseData as TimeWellMetrics;
    },
    onSuccess: (data: TimeWellMetrics) => {
      setMetrics(data);
    },
    onError: (error: Error) => {
      if (!error.message.includes("R_MAX_TRIGGERED")) {
        toast({
          title: "Calculation Failed",
          description: "Unable to compute time-well metrics",
          variant: "destructive"
        });
      }
    }
  });

  const saveMutation = useMutation({
    mutationFn: async (data: { biologicalMarker: string; anchorPointMyr: number; notes?: string }) => {
      const response = await fetch("/api/time-well/resonance", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify(data)
      });
      const responseData = await response.json();
      
      if (response.status === 403) {
        toast({
          title: "R_MAX LOGIC GUARD",
          description: "Cannot save beyond Tipping Point boundary.",
          variant: "destructive"
        });
        throw new Error("R_MAX_TRIGGERED");
      }
      
      if (!response.ok) {
        throw new Error(responseData.error || "Save failed");
      }
      
      return responseData;
    },
    onSuccess: () => {
      toast({
        title: "Anchor Point Saved",
        description: `Historical resonance at ${anchorPointMyr.toFixed(2)} Myr established.`
      });
      queryClient.invalidateQueries({ queryKey: ["/api/time-well/resonances"] });
    },
    onError: (error: Error) => {
      if (!error.message.includes("R_MAX_TRIGGERED")) {
        toast({
          title: "Save Failed",
          description: "Unable to save historical resonance",
          variant: "destructive"
        });
      }
    }
  });

  const deleteMutation = useMutation({
    mutationFn: async (id: string) => {
      const response = await apiRequest("DELETE", `/api/time-well/resonance/${id}`);
      return response.json();
    },
    onSuccess: () => {
      toast({ title: "Resonance Deleted" });
      queryClient.invalidateQueries({ queryKey: ["/api/time-well/resonances"] });
    }
  });

  const drawVisualization = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext("2d");
    if (!ctx) return;
    
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, width, height);
    
    const time = Date.now() / 1000;
    
    if (isSyncing && metrics?.standingWavePattern) {
      ctx.strokeStyle = "rgba(147, 51, 234, 0.8)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      
      const pattern = metrics.standingWavePattern;
      for (let i = 0; i < width; i++) {
        const patternIdx = Math.floor((i / width) * pattern.length);
        const baseY = height / 2;
        const amplitude = (pattern[patternIdx] || 0) * height * 2;
        const standingWave = amplitude * Math.sin(time * 0.5);
        const y = baseY + standingWave;
        
        if (i === 0) {
          ctx.moveTo(i, y);
        } else {
          ctx.lineTo(i, y);
        }
      }
      ctx.stroke();
      
      ctx.fillStyle = "rgba(147, 51, 234, 0.3)";
      ctx.fillText("STANDING WAVE - STATIC MEMORY", 10, 20);
    } else {
      ctx.strokeStyle = "rgba(34, 197, 94, 0.6)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      
      for (let i = 0; i < width; i++) {
        const x = i;
        const baseY = height / 2;
        const frequency = 0.02;
        const amplitude = 20;
        const y = baseY + Math.sin((i + time * 50) * frequency) * amplitude * 
                  Math.sin(time * 2) * (1 + Math.sin(i * 0.01) * 0.5);
        
        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }
      ctx.stroke();
      
      ctx.fillStyle = "rgba(34, 197, 94, 0.3)";
      ctx.fillText("LIVE NANOGRAV PULSE", 10, 20);
    }
    
    if (metrics?.rMaxTriggered) {
      ctx.fillStyle = "rgba(239, 68, 68, 0.8)";
      ctx.font = "bold 14px monospace";
      ctx.fillText("R_MAX LOGIC GUARD ACTIVE", width / 2 - 100, height / 2);
    }
    
    animationRef.current = requestAnimationFrame(drawVisualization);
  }, [isSyncing, metrics]);

  useEffect(() => {
    animationRef.current = requestAnimationFrame(drawVisualization);
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [drawVisualization]);

  useEffect(() => {
    if (biologicalMarker && biologicalMarker.length >= 2) {
      const debounceTimer = setTimeout(() => {
        calculateMutation.mutate({ biologicalMarker, anchorPointMyr });
      }, 300);
      return () => clearTimeout(debounceTimer);
    }
  }, [anchorPointMyr, biologicalMarker]);

  const handleSliderChange = (value: number[]) => {
    const newValue = value[0];
    setAnchorPointMyr(newValue);
    
    if (newValue <= TIPPING_POINT_MYR) {
      setIsSyncing(false);
      setMetrics({
        rMaxTriggered: true,
        anchorPointMyr: newValue,
        groundStateDecay: null,
        reconstructionAccuracy: 0,
        error: "R_MAX_LOGIC_GUARD_TRIGGERED",
        message: "Approaching Tipping Point boundary. Vacuum Reset required."
      });
    }
  };

  const handleSync = () => {
    if (!biologicalMarker) {
      toast({
        title: "Biological Marker Required",
        description: "Enter a DNA/biological marker to seed the K(t) kernel.",
        variant: "destructive"
      });
      return;
    }
    
    if (metrics?.rMaxTriggered) {
      toast({
        title: "Cannot Sync",
        description: "R_MAX Logic Guard prevents synchronization beyond Tipping Point.",
        variant: "destructive"
      });
      return;
    }
    
    setIsSyncing(true);
  };

  const handleVacuumReset = () => {
    setIsSyncing(false);
    setAnchorPointMyr(COSMIC_AGE_MYR);
    setMetrics(null);
    toast({
      title: "Vacuum Reset Complete",
      description: "Timeline restored to present. Ground state stabilized."
    });
  };

  const handleSaveResonance = () => {
    if (metrics?.rMaxTriggered) {
      toast({
        title: "R_MAX Logic Guard Active",
        description: "Cannot save anchor points beyond Tipping Point boundary.",
        variant: "destructive"
      });
      return;
    }
    
    if (!biologicalMarker) {
      toast({
        title: "Marker Required",
        description: "Enter a biological marker before saving.",
        variant: "destructive"
      });
      return;
    }
    saveMutation.mutate({ biologicalMarker, anchorPointMyr, notes: notes || undefined });
  };

  const formatMyr = (myr: number): string => {
    if (myr >= 1000) {
      return `${(myr / 1000).toFixed(2)} Gyr`;
    } else if (myr >= 1) {
      return `${myr.toFixed(2)} Myr`;
    } else if (myr >= 0.001) {
      return `${(myr * 1000).toFixed(2)} kyr`;
    } else {
      return `${(myr * 1e6).toFixed(2)} yr`;
    }
  };

  const getEraName = (myr: number): string => {
    if (myr > 13799) return "Present Day";
    if (myr > 13500) return "Early Humans";
    if (myr > 13000) return "Dinosaur Era";
    if (myr > 10000) return "Complex Life";
    if (myr > 4000) return "Earth Formation";
    if (myr > 1000) return "Early Galaxies";
    if (myr > 100) return "Dark Ages";
    if (myr > 0.38) return "Recombination";
    if (myr > TIPPING_POINT_MYR) return "Primordial Soup";
    return "BEYOND TIPPING POINT";
  };

  const resonances = resonancesData?.resonances || [];

  return (
    <Card className="relative overflow-visible" data-testid="card-time-well">
      <CardHeader className="flex flex-row items-center justify-between gap-2 pb-2">
        <CardTitle className="text-lg font-semibold flex items-center gap-2">
          <Dna className="h-5 w-5 text-purple-400" />
          DNA-Resonance & Time-Well
        </CardTitle>
        <Badge 
          variant={metrics?.rMaxTriggered ? "destructive" : isSyncing ? "default" : "secondary"}
          className={isSyncing && !metrics?.rMaxTriggered ? "bg-purple-500 text-white" : ""}
          data-testid="badge-time-well-status"
        >
          {metrics?.rMaxTriggered ? "R_MAX GUARD" : isSyncing ? "SYNCED" : "STANDBY"}
        </Badge>
      </CardHeader>
      
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="biological-marker" className="text-sm flex items-center gap-2">
            <Dna className="h-4 w-4" />
            Biological Marker (Hex/String)
          </Label>
          <Tooltip>
            <TooltipTrigger asChild>
              <Input
                id="biological-marker"
                placeholder="Enter DNA sequence or hex identifier..."
                value={biologicalMarker}
                onChange={(e) => setBiologicalMarker(e.target.value)}
                className="font-mono"
                data-testid="input-biological-marker"
              />
            </TooltipTrigger>
            <TooltipContent>
              <p>Seeds the K(t) kernel to localize universal past to your genetic line</p>
            </TooltipContent>
          </Tooltip>
        </div>
        
        <div className="space-y-2">
          <div className="flex items-center justify-between">
            <Label className="text-sm flex items-center gap-2">
              <Clock className="h-4 w-4" />
              Timeline Position
            </Label>
            <span className="text-sm font-mono text-muted-foreground">
              {formatMyr(anchorPointMyr)}
            </span>
          </div>
          
          <Slider
            value={[anchorPointMyr]}
            onValueChange={handleSliderChange}
            min={0}
            max={COSMIC_AGE_MYR}
            step={0.1}
            className={`${metrics?.rMaxTriggered ? "[&>span]:bg-red-500" : ""}`}
            data-testid="slider-timeline"
          />
          
          <div className="flex justify-between text-xs text-muted-foreground">
            <span>Tipping Point</span>
            <span className="font-medium text-foreground">{getEraName(anchorPointMyr)}</span>
            <span>Present</span>
          </div>
        </div>
        
        {metrics?.rMaxTriggered && (
          <div className="p-3 rounded-md bg-red-500/20 border border-red-500/40 space-y-2">
            <div className="flex items-center gap-2 text-red-400">
              <AlertTriangle className="h-4 w-4" />
              <span className="font-semibold">R_MAX LOGIC GUARD TRIGGERED</span>
            </div>
            <p className="text-sm text-muted-foreground">
              Cannot look beyond {TIPPING_POINT_MYR} Myr post-Planck. 
              Vacuum Reset required to prevent infinite noise feedback.
            </p>
            <Button
              onClick={handleVacuumReset}
              variant="destructive"
              size="sm"
              className="w-full"
              data-testid="button-vacuum-reset"
            >
              <RotateCcw className="h-4 w-4 mr-2" />
              Initiate Vacuum Reset
            </Button>
          </div>
        )}
        
        {metrics && !metrics.rMaxTriggered && (
          <div className="p-3 rounded-md bg-purple-500/10 border border-purple-500/30 space-y-3">
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div className="space-y-1">
                <span className="text-muted-foreground">Ground State Decay</span>
                <div className="font-mono text-foreground" data-testid="text-ground-decay">
                  {metrics.groundStateDecay?.toFixed(6) || "N/A"}
                </div>
              </div>
              <div className="space-y-1">
                <span className="text-muted-foreground">Reconstruction Accuracy</span>
                <div className="font-mono text-foreground" data-testid="text-reconstruction-accuracy">
                  {((metrics.reconstructionAccuracy || 0) * 100).toFixed(2)}%
                </div>
              </div>
              <div className="space-y-1">
                <span className="text-muted-foreground">Breath Cycles Back</span>
                <div className="font-mono text-foreground">
                  {metrics.cycleNumber || 0}
                </div>
              </div>
              <div className="space-y-1">
                <span className="text-muted-foreground">Distance from Present</span>
                <div className="font-mono text-foreground">
                  {formatMyr(metrics.distanceFromPresent || 0)}
                </div>
              </div>
            </div>
            
            {metrics.grut_insight && (
              <p className="text-xs text-purple-400/80 italic">
                {metrics.grut_insight}
              </p>
            )}
          </div>
        )}
        
        <div className="relative rounded-md overflow-hidden">
          <canvas
            ref={canvasRef}
            width={300}
            height={80}
            className="w-full h-20 bg-black/50 rounded-md"
            data-testid="canvas-resonance-map"
          />
          <div className="absolute bottom-1 right-1 text-xs text-muted-foreground/60">
            {isSyncing ? "Standing Wave Pattern" : "NANOGrav Pulse"}
          </div>
        </div>
        
        <div className="space-y-2">
          <Input
            placeholder="Notes (optional)..."
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            className="text-sm"
            data-testid="input-notes"
          />
        </div>
        
        <div className="flex gap-2">
          <Button
            onClick={isSyncing ? () => setIsSyncing(false) : handleSync}
            variant={isSyncing ? "destructive" : "outline"}
            size="default"
            className="flex-1"
            disabled={metrics?.rMaxTriggered || calculateMutation.isPending}
            data-testid="button-sync-past"
          >
            {isSyncing ? (
              <>
                <Waves className="h-4 w-4 mr-2" />
                Desync
              </>
            ) : (
              <>
                <History className="h-4 w-4 mr-2" />
                Sync with Past Era
              </>
            )}
          </Button>
          
          <Button
            onClick={handleSaveResonance}
            variant="default"
            size="default"
            className="flex-1"
            disabled={metrics?.rMaxTriggered || saveMutation.isPending || !biologicalMarker}
            data-testid="button-save-resonance"
          >
            <Save className="h-4 w-4 mr-2" />
            {saveMutation.isPending ? "Saving..." : "Save Anchor"}
          </Button>
        </div>
        
        {resonances.length > 0 && (
          <div className="space-y-2 pt-2 border-t border-border">
            <div className="flex items-center gap-2 text-sm text-muted-foreground">
              <Shield className="h-4 w-4" />
              Saved Anchor Points ({resonances.length})
            </div>
            <div className="max-h-32 overflow-y-auto space-y-1">
              {resonances.map((res) => (
                <div 
                  key={res.id}
                  className="flex items-center justify-between p-2 rounded bg-muted/30 text-sm"
                >
                  <div className="flex-1 min-w-0">
                    <div className="font-mono text-xs truncate">{res.biologicalMarker}</div>
                    <div className="text-xs text-muted-foreground">
                      {formatMyr(res.anchorPointMyr)} - {((res.reconstructionAccuracy || 0) * 100).toFixed(1)}% accuracy
                    </div>
                  </div>
                  <Button
                    size="icon"
                    variant="ghost"
                    onClick={() => deleteMutation.mutate(res.id)}
                    data-testid={`button-delete-resonance-${res.id}`}
                  >
                    <Trash2 className="h-4 w-4 text-muted-foreground" />
                  </Button>
                </div>
              ))}
            </div>
          </div>
        )}
        
        {isSyncing && (
          <div className="text-xs text-center text-purple-400/80 animate-pulse">
            Resonating with {getEraName(anchorPointMyr)}. Standing wave pattern active.
          </div>
        )}
      </CardContent>
    </Card>
  );
}
