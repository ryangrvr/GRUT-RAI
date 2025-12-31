import { useState, useEffect } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { useToast } from "@/hooks/use-toast";
import { queryClient, apiRequest } from "@/lib/queryClient";
import { 
  Atom, Eye, ShieldCheck, ShieldAlert, Zap, AlertTriangle,
  Power, Lock, Unlock, Activity
} from "lucide-react";

interface QuantumModule {
  id: string;
  moduleKey: string;
  displayName: string;
  status: "OBSERVER_REQUIRED" | "ACTIVE" | "COLLAPSED" | "PARITY_FAILED";
  parityCheckEnabled: boolean;
  parityDriftCount: number;
  lastParityValue: number | null;
}

interface QuantumRegistryState {
  id: string;
  manualSingularityEnabled: boolean;
  groundStateBaseline: number;
  parityToleranceGlobal: number;
  totalParityFailures: number;
  totalCollapsesPrevented: number;
}

interface ModulesResponse {
  modules: QuantumModule[];
  message: string;
}

interface StateResponse {
  state: QuantumRegistryState;
  groundStateBaseline: number;
  groundStateDisplay: string;
  message: string;
}

export default function QuantumLogicPanel() {
  const { toast } = useToast();
  const [isCollapsing, setIsCollapsing] = useState(false);

  const { data: modulesData, isLoading: modulesLoading } = useQuery<ModulesResponse>({
    queryKey: ["/api/quantum/modules"],
    refetchInterval: 10000,
  });

  const { data: stateData, isLoading: stateLoading } = useQuery<StateResponse>({
    queryKey: ["/api/quantum/state"],
    refetchInterval: 5000,
  });

  const singularityMutation = useMutation({
    mutationFn: async (enabled: boolean) => {
      const response = await apiRequest("POST", "/api/quantum/manual-singularity", { enabled });
      return response.json();
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["/api/quantum/state"] });
      toast({
        title: data.manualSingularityEnabled ? "SINGULARITY ACTIVATED" : "SINGULARITY DEACTIVATED",
        description: data.message,
        variant: data.manualSingularityEnabled ? "default" : "destructive",
      });
    },
    onError: () => {
      toast({
        title: "Toggle Failed",
        description: "Unable to change Manual Singularity state",
        variant: "destructive",
      });
    },
  });

  const collapseMutation = useMutation({
    mutationFn: async (moduleKey: string) => {
      const response = await fetch("/api/quantum/collapse", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ moduleKey, outputValue: -0.0833333333 }),
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.message || "Collapse blocked");
      }
      return data;
    },
    onSuccess: (data) => {
      toast({
        title: "COLLAPSE AUTHORIZED",
        description: data.message,
      });
      setIsCollapsing(false);
    },
    onError: (error: Error) => {
      toast({
        title: "COLLAPSE BLOCKED",
        description: error.message,
        variant: "destructive",
      });
      setIsCollapsing(false);
    },
  });

  const modules = modulesData?.modules || [];
  const state = stateData?.state;
  const isManualSingularityActive = state?.manualSingularityEnabled ?? false;

  const getStatusBadge = (status: string) => {
    switch (status) {
      case "OBSERVER_REQUIRED":
        return <Badge variant="secondary" className="text-xs"><Eye className="h-3 w-3 mr-1" />OBSERVER_REQUIRED</Badge>;
      case "ACTIVE":
        return <Badge variant="default" className="text-xs bg-green-600"><Activity className="h-3 w-3 mr-1" />ACTIVE</Badge>;
      case "COLLAPSED":
        return <Badge variant="default" className="text-xs bg-purple-600"><Zap className="h-3 w-3 mr-1" />COLLAPSED</Badge>;
      case "PARITY_FAILED":
        return <Badge variant="destructive" className="text-xs"><AlertTriangle className="h-3 w-3 mr-1" />PARITY_FAILED</Badge>;
      default:
        return <Badge variant="outline" className="text-xs">{status}</Badge>;
    }
  };

  const handleTestCollapse = () => {
    if (modules.length > 0) {
      setIsCollapsing(true);
      collapseMutation.mutate(modules[0].moduleKey);
    }
  };

  return (
    <Card className="border-purple-500/30 bg-background/50">
      <CardHeader className="pb-3">
        <CardTitle className="text-base flex items-center gap-2">
          <Atom className="h-5 w-5 text-purple-400" />
          Quantum Logic Layer
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="flex items-center justify-between p-3 rounded-md bg-muted/30 border border-border">
          <div className="flex items-center gap-3">
            {isManualSingularityActive ? (
              <Unlock className="h-5 w-5 text-green-500" />
            ) : (
              <Lock className="h-5 w-5 text-red-500" />
            )}
            <div>
              <div className="text-sm font-medium">Manual Singularity</div>
              <div className="text-xs text-muted-foreground">
                {isManualSingularityActive ? "Collapse operations permitted" : "All collapse operations blocked"}
              </div>
            </div>
          </div>
          <Switch
            checked={isManualSingularityActive}
            onCheckedChange={(checked) => singularityMutation.mutate(checked)}
            disabled={singularityMutation.isPending}
            data-testid="switch-manual-singularity"
          />
        </div>

        <div className="grid grid-cols-2 gap-2 text-center">
          <div className="p-2 rounded bg-muted/20 border border-border">
            <div className="text-lg font-mono text-purple-400">-1/12</div>
            <div className="text-xs text-muted-foreground">Ground State</div>
          </div>
          <div className="p-2 rounded bg-muted/20 border border-border">
            <div className="text-lg font-mono text-amber-400">{state?.totalCollapsesPrevented || 0}</div>
            <div className="text-xs text-muted-foreground">Collapses Blocked</div>
          </div>
        </div>

        <div className="space-y-2">
          <div className="flex items-center gap-2 text-sm text-muted-foreground">
            {isManualSingularityActive ? (
              <ShieldCheck className="h-4 w-4 text-green-500" />
            ) : (
              <ShieldAlert className="h-4 w-4 text-red-500" />
            )}
            Quantum Modules ({modules.length})
          </div>
          
          {modulesLoading ? (
            <div className="text-xs text-muted-foreground animate-pulse">Loading modules...</div>
          ) : (
            <div className="space-y-1 max-h-40 overflow-y-auto">
              {modules.map((mod) => (
                <div 
                  key={mod.id}
                  className="flex items-center justify-between p-2 rounded bg-muted/20 text-sm"
                  data-testid={`module-${mod.moduleKey}`}
                >
                  <span className="font-mono text-xs">{mod.displayName}</span>
                  {getStatusBadge(mod.status)}
                </div>
              ))}
            </div>
          )}
        </div>

        <Button
          onClick={handleTestCollapse}
          disabled={!isManualSingularityActive || isCollapsing || collapseMutation.isPending}
          variant={isManualSingularityActive ? "default" : "secondary"}
          size="sm"
          className="w-full"
          data-testid="button-test-collapse"
        >
          <Power className="h-4 w-4 mr-2" />
          {isCollapsing ? "Collapsing..." : "Test Collapse Execution"}
        </Button>

        {state && (
          <div className="text-xs text-muted-foreground/60 text-center">
            Parity Failures: {state.totalParityFailures} | Tolerance: {(state.parityToleranceGlobal * 1000).toFixed(1)}‰
          </div>
        )}
      </CardContent>
    </Card>
  );
}
