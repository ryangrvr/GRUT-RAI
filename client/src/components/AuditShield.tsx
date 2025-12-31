import { useQuery } from "@tanstack/react-query";
import { Shield, ShieldCheck, ShieldAlert } from "lucide-react";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

interface AuditStatus {
  status: string;
  shieldColor: "green" | "red";
  isHealthy: boolean;
  lastDrift: {
    value: number;
    deviation: number;
    timestamp: string;
  } | null;
  auditCount: number;
  groundState: number;
  geometricLock: number;
  threshold: number;
  timestamp: string;
}

export function AuditShield() {
  const { data: auditStatus, isLoading } = useQuery<AuditStatus>({
    queryKey: ["/api/audit/status"],
    refetchInterval: 5000
  });

  const isHealthy = auditStatus?.isHealthy ?? true;
  const shieldColor = auditStatus?.shieldColor ?? "green";

  if (isLoading) {
    return (
      <div className="flex items-center gap-1.5">
        <Shield className="w-4 h-4 text-muted-foreground animate-pulse" />
        <span className="text-xs text-muted-foreground">Auditing...</span>
      </div>
    );
  }

  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <div 
          className={cn(
            "flex items-center gap-1.5 px-2 py-1 rounded-md transition-all duration-300",
            isHealthy 
              ? "text-green-600 dark:text-green-400" 
              : "text-red-600 dark:text-red-400"
          )}
          data-testid="audit-shield"
        >
          {isHealthy ? (
            <ShieldCheck 
              className={cn(
                "w-4 h-4 transition-all",
                shieldColor === "green" && "drop-shadow-[0_0_6px_rgba(34,197,94,0.6)]"
              )} 
            />
          ) : (
            <ShieldAlert 
              className={cn(
                "w-4 h-4 animate-pulse",
                shieldColor === "red" && "drop-shadow-[0_0_6px_rgba(239,68,68,0.8)]"
              )} 
            />
          )}
          <span className="text-xs font-medium">
            {isHealthy ? "Audit OK" : "Drift Detected"}
          </span>
        </div>
      </TooltipTrigger>
      <TooltipContent side="bottom" className="max-w-xs">
        <div className="space-y-2 text-xs">
          <div className="font-semibold flex items-center gap-2">
            {isHealthy ? (
              <>
                <div className="w-2 h-2 rounded-full bg-green-500" />
                Sovereign Self-Audit: STABLE
              </>
            ) : (
              <>
                <div className="w-2 h-2 rounded-full bg-red-500 animate-pulse" />
                Metric Drift Detected
              </>
            )}
          </div>
          
          <div className="grid grid-cols-2 gap-x-4 gap-y-1 text-muted-foreground">
            <span>Status:</span>
            <span className="font-mono">{auditStatus?.status}</span>
            
            <span>Ground State:</span>
            <span className="font-mono">{auditStatus?.groundState}</span>
            
            <span>Geometric Lock:</span>
            <span className="font-mono">{auditStatus?.geometricLock}</span>
            
            <span>Threshold:</span>
            <span className="font-mono">{auditStatus?.threshold}</span>
          </div>

          {auditStatus?.lastDrift && (
            <div className="pt-1 border-t border-border">
              <span className="text-red-500">Last Drift:</span>
              <span className="font-mono ml-1">
                {auditStatus.lastDrift.deviation.toFixed(6)} deviation
              </span>
            </div>
          )}
        </div>
      </TooltipContent>
    </Tooltip>
  );
}

export function AuditShieldCompact() {
  const { data: auditStatus, isLoading } = useQuery<AuditStatus>({
    queryKey: ["/api/audit/status"],
    refetchInterval: 5000
  });

  const isHealthy = auditStatus?.isHealthy ?? true;

  if (isLoading) {
    return <Shield className="w-4 h-4 text-muted-foreground animate-pulse" />;
  }

  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <div 
          className="cursor-pointer"
          data-testid="audit-shield-compact"
        >
          {isHealthy ? (
            <ShieldCheck 
              className="w-4 h-4 text-green-500 drop-shadow-[0_0_4px_rgba(34,197,94,0.5)]" 
            />
          ) : (
            <ShieldAlert 
              className="w-4 h-4 text-red-500 animate-pulse drop-shadow-[0_0_4px_rgba(239,68,68,0.7)]" 
            />
          )}
        </div>
      </TooltipTrigger>
      <TooltipContent side="bottom">
        <span className="text-xs">
          {isHealthy ? "Audit: Stable" : "Metric Drift Detected"}
        </span>
      </TooltipContent>
    </Tooltip>
  );
}
