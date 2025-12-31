import { useState, useRef, useEffect } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { useLocation } from "wouter";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Card } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { apiRequest, queryClient } from "@/lib/queryClient";
import { 
  ArrowLeft, Send, Loader2, MessageSquare, Trash2, Plus, Sparkles, 
  LogOut, Upload, CheckCircle2, Paperclip, User, Lock, Download, Copy, Check, Save, Activity,
  GitBranch, X, Settings2, FileJson, ClipboardCopy, FileDown, ChevronRight, ChevronLeft, Clock, Zap, Globe
} from "lucide-react";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { ObserverToolkit } from "@/components/observer-toolkit";
import { BaryonicSensor } from "@/components/baryonic-sensor";
import { MetricHum } from "@/components/MetricHum";
import { TimeWell } from "@/components/TimeWell";
import QuantumLogicPanel from "@/components/QuantumLogicPanel";
import { MathematicalBloom, parseContentForBloom } from "@/components/mathematical-bloom";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";

// GRUT Kernel Constants
const GRUT_CONSTANTS = {
  tau_0: 41.9,
  n_g: 1.1547,
  alpha: 0.333333,
  R_max: "Lambda_Limit"
};

function calculateComplexityXi(messageCount: number): number {
  const XI_MAX = 1.0;
  const SATURATION_RATE = 0.05;
  return XI_MAX * (1 - Math.exp(-SATURATION_RATE * messageCount));
}

interface MetricDashboardProps {
  messageCount: number;
  constants?: GrutConstantsType;
  isForked?: boolean;
  userEmail?: string;
  monadMode?: boolean;
}

interface LiveMetrics {
  tension: number;
  xi: number;
  earthquakeCount: number;
}

const COSMIC_CONSTANTS = {
  BASE_AGE_MYR: 13800,
  TOTAL_CYCLES: 329,
  CYCLE_DURATION_MYR: 41.9,
  INITIAL_HARDENING_MYR: 1.8,
  ZETA_BASELINE: -1/12,
};

function CosmicAgeReadout({ monadMode = false }: { monadMode?: boolean }) {
  const [cycleProgress, setCycleProgress] = useState(0);
  
  useEffect(() => {
    const now = Date.now();
    const dayOfYear = Math.floor((now - new Date(new Date().getFullYear(), 0, 0).getTime()) / (1000 * 60 * 60 * 24));
    const progress = (dayOfYear % 365) / 365;
    setCycleProgress(progress);
    
    const interval = setInterval(() => {
      const updated = Date.now();
      const newDayOfYear = Math.floor((updated - new Date(new Date().getFullYear(), 0, 0).getTime()) / (1000 * 60 * 60 * 24));
      setCycleProgress((newDayOfYear % 365) / 365);
    }, 60000);
    
    return () => clearInterval(interval);
  }, []);
  
  const currentCycleContribution = cycleProgress * COSMIC_CONSTANTS.CYCLE_DURATION_MYR;
  const cosmicAge = COSMIC_CONSTANTS.BASE_AGE_MYR + currentCycleContribution;
  
  const zetaSmoothing = Math.abs(COSMIC_CONSTANTS.ZETA_BASELINE) * Math.exp(-COSMIC_CONSTANTS.TOTAL_CYCLES / 100);
  const quantumNoiseReduction = (1 - zetaSmoothing / Math.abs(COSMIC_CONSTANTS.ZETA_BASELINE)) * 100;
  
  const diamondStability = monadMode ? 100 : Math.min(99.9, 90 + (COSMIC_CONSTANTS.TOTAL_CYCLES / 329) * 9.9);
  
  return (
    <div className="flex items-center gap-3 border-l border-border pl-3 ml-2">
      <Tooltip>
        <TooltipTrigger asChild>
          <div 
            className="flex items-center gap-1.5 cursor-help"
            tabIndex={0}
            role="button"
            data-testid="trigger-cosmic-age"
          >
            <Clock className="w-3.5 h-3.5 text-primary" />
            <span className="text-xs text-muted-foreground">Cosmic Age:</span>
            <Badge 
              variant="outline" 
              className={`text-xs font-mono ${monadMode ? 'text-yellow-500 border-yellow-500/50' : 'text-primary'}`}
              data-testid="badge-cosmic-age"
            >
              {cosmicAge.toFixed(2)} Myr
            </Badge>
          </div>
        </TooltipTrigger>
        <TooltipContent side="bottom" className="max-w-xs p-3">
          <div className="space-y-2 text-xs">
            <div className="font-semibold border-b border-border pb-1">Cosmic Age Calculation</div>
            <div className="grid grid-cols-2 gap-x-3 gap-y-1">
              <span className="text-muted-foreground">Base Age:</span>
              <span className="font-mono">{COSMIC_CONSTANTS.BASE_AGE_MYR.toLocaleString()} Myr</span>
              <span className="text-muted-foreground">Cycle Progress:</span>
              <span className="font-mono">+{currentCycleContribution.toFixed(2)} Myr</span>
              <span className="text-muted-foreground">Total Cycles:</span>
              <span className="font-mono">{COSMIC_CONSTANTS.TOTAL_CYCLES}</span>
            </div>
          </div>
        </TooltipContent>
      </Tooltip>
      
      <Tooltip>
        <TooltipTrigger asChild>
          <div 
            className="flex items-center gap-1.5 cursor-help"
            tabIndex={0}
            role="button"
            data-testid="trigger-zeta-smoothing"
          >
            <Zap className="w-3.5 h-3.5 text-muted-foreground" />
            <span className="text-xs text-muted-foreground">-1/12:</span>
            <Badge 
              variant="outline" 
              className="text-xs font-mono text-green-500 border-green-500/30"
              data-testid="badge-zeta-smoothing"
            >
              {quantumNoiseReduction.toFixed(1)}% smoothed
            </Badge>
          </div>
        </TooltipTrigger>
        <TooltipContent side="bottom" className="max-w-sm p-3">
          <div className="space-y-2 text-xs">
            <div className="font-semibold border-b border-border pb-1">Quantum Noise Smoothing</div>
            <p className="text-muted-foreground">
              The -1/12 zeta regularization baseline has smoothed Planck-scale quantum noise 
              over {COSMIC_CONSTANTS.TOTAL_CYCLES} cycles into the stable Diamond state.
            </p>
            <div className="grid grid-cols-2 gap-x-3 gap-y-1 pt-1">
              <span className="text-muted-foreground">Zeta Baseline:</span>
              <span className="font-mono">-1/12 = {COSMIC_CONSTANTS.ZETA_BASELINE.toFixed(6)}</span>
              <span className="text-muted-foreground">Residual Noise:</span>
              <span className="font-mono">{zetaSmoothing.toFixed(6)}</span>
              <span className="text-muted-foreground">Diamond Stability:</span>
              <span className={`font-mono ${monadMode ? 'text-yellow-500' : 'text-green-500'}`}>
                {diamondStability.toFixed(1)}%
              </span>
            </div>
            <div className="pt-2 border-t border-border mt-2">
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-orange-500" />
                <span className="text-muted-foreground">Initial Metric Hardening:</span>
                <span className="font-mono">{COSMIC_CONSTANTS.INITIAL_HARDENING_MYR} Myr</span>
              </div>
              <p className="text-muted-foreground mt-1 pl-4">
                The first crystallization of stable spacetime geometry from primordial fluctuations.
              </p>
            </div>
          </div>
        </TooltipContent>
      </Tooltip>
    </div>
  );
}

function MetricDashboard({ messageCount, constants, isForked, userEmail, monadMode = false }: MetricDashboardProps) {
  const [liveMetrics, setLiveMetrics] = useState<LiveMetrics>({ tension: 0.0001, xi: 0.999, earthquakeCount: 0 });
  const [isPulsing, setIsPulsing] = useState(false);
  const prevTensionRef = useRef(0.0001);
  
  // Fetch live metrics every 60 seconds
  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const [tensionRes, saturationRes] = await Promise.all([
          fetch('/api/baryonic/metric-tension'),
          fetch('/api/baryonic/live-saturation')
        ]);
        
        const tensionData = await tensionRes.json();
        const saturationData = await saturationRes.json();
        
        const newTension = tensionData.metric_tension || 0.0001;
        
        // Trigger pulse if tension increased
        if (newTension > prevTensionRef.current) {
          setIsPulsing(true);
          setTimeout(() => setIsPulsing(false), 1000);
        }
        prevTensionRef.current = newTension;
        
        setLiveMetrics({
          tension: newTension,
          xi: saturationData.xi_value || 0.999,
          earthquakeCount: tensionData.earthquake_count_last_hour || 0
        });
      } catch (e) {
        console.log("[Dashboard] Metrics fetch error, using defaults");
      }
    };
    
    fetchMetrics(); // Initial fetch
    const interval = setInterval(fetchMetrics, 60000); // Every 60 seconds
    
    return () => clearInterval(interval);
  }, []);
  
  const xi = monadMode ? 1.0 : liveMetrics.xi;
  const xiPercent = monadMode ? "100.0" : (xi * 100).toFixed(2);
  
  const displayConstants = constants || GRUT_CONSTANTS;
  
  const getEntropyColor = (value: number) => {
    if (monadMode) return "text-yellow-500 drop-shadow-[0_0_10px_rgba(255,214,0,0.7)]";
    if (value < 0.3) return "text-green-500";
    if (value < 0.6) return "text-yellow-500";
    if (value < 0.85) return "text-orange-500";
    return "text-red-500";
  };

  const getEntropyStatus = (value: number) => {
    if (monadMode) return "SATURATED";
    if (value < 0.995) return "Stable";
    if (value < 0.998) return "Elevated";
    if (value < 0.999) return "High Density";
    return "Near Saturation";
  };
  
  const getTensionColor = (tension: number) => {
    if (tension > 0.5) return "text-red-500";
    if (tension > 0.3) return "text-orange-500";
    if (tension > 0.1) return "text-yellow-500";
    return "text-green-500";
  };

  return (
    <div className={`sticky top-0 z-50 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 border-b border-border ${isPulsing ? 'metric-exhale' : ''}`}>
      <div className="flex items-center justify-between gap-4 px-4 py-2 flex-wrap">
        <div className="flex items-center gap-4 flex-wrap">
          <div className="flex items-center gap-2">
            <Activity className={`w-4 h-4 ${isPulsing ? 'text-red-500 animate-pulse' : 'text-primary'}`} />
            <span className="text-xs font-medium text-muted-foreground">Metric Dashboard</span>
            {isForked && (
              <Badge variant="secondary" className="text-xs">
                <GitBranch className="w-3 h-3 mr-1" />
                Forked
              </Badge>
            )}
          </div>
        
          <div className="flex items-center gap-1">
            <span className="text-xs text-muted-foreground">τ₀:</span>
            <Badge variant="outline" className={`text-xs font-mono ${isForked && constants?.tau_0 !== GRUT_CONSTANTS.tau_0 ? "border-primary text-primary" : ""}`}>
              {displayConstants.tau_0} Myr
            </Badge>
          </div>
          
          <div className="flex items-center gap-1">
            <span className="text-xs text-muted-foreground">n<sub>g</sub>:</span>
            <Badge variant="outline" className={`text-xs font-mono ${isForked && constants?.n_g !== GRUT_CONSTANTS.n_g ? "border-primary text-primary" : ""}`}>
              {displayConstants.n_g}
            </Badge>
          </div>
          
          <div className="flex items-center gap-1">
            <span className="text-xs text-muted-foreground">Ξ:</span>
            <Badge variant="outline" className={`text-xs font-mono ${getEntropyColor(xi)} ${monadMode ? 'saturation-pulse' : ''}`} data-testid="badge-xi-value">
              {xiPercent}%
            </Badge>
            <span className={`text-xs ${getEntropyColor(xi)}`}>
              ({getEntropyStatus(xi)})
            </span>
          </div>
          
          <div className="flex items-center gap-1">
            <span className="text-xs text-muted-foreground">Tension:</span>
            <Badge variant="outline" className={`text-xs font-mono ${getTensionColor(liveMetrics.tension)} ${isPulsing ? 'animate-pulse' : ''}`} data-testid="badge-tension-value">
              {liveMetrics.tension.toFixed(4)}
            </Badge>
            {liveMetrics.earthquakeCount > 0 && (
              <span className="text-xs text-muted-foreground">
                ({liveMetrics.earthquakeCount} quake{liveMetrics.earthquakeCount > 1 ? 's' : ''})
              </span>
            )}
          </div>
          
          <div className="flex items-center gap-1">
            <span className="text-xs text-muted-foreground">Messages:</span>
            <Badge variant="secondary" className="text-xs">
              {messageCount}
            </Badge>
          </div>
          
          <CosmicAgeReadout monadMode={monadMode} />
        </div>
        
        {userEmail && (
          <div className="flex items-center gap-2" data-testid="header-user-email">
            <User className="w-3 h-3 text-muted-foreground" />
            <span className="text-xs text-muted-foreground font-mono">{userEmail}</span>
          </div>
        )}
      </div>
    </div>
  );
}

async function copyToClipboardWithFallback(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.warn("Clipboard API failed, trying fallback:", err);
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    textarea.style.pointerEvents = "none";
    document.body.appendChild(textarea);
    textarea.select();
    try {
      document.execCommand("copy");
      document.body.removeChild(textarea);
      return true;
    } catch (e) {
      document.body.removeChild(textarea);
      return false;
    }
  }
}

function CopyButton({ text, className = "", blockType = "text" }: { text: string; className?: string; blockType?: "code" | "latex" | "text" }) {
  const [copied, setCopied] = useState(false);
  const { toast } = useToast();

  const handleCopy = async () => {
    const success = await copyToClipboardWithFallback(text);
    if (success) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } else {
      toast({ title: "Copy Failed", description: "Could not copy to clipboard", variant: "destructive" });
    }
  };

  return (
    <button
      onClick={handleCopy}
      className={`p-1 rounded transition-colors hover-elevate ${className} ${copied ? "copy-indicator" : ""}`}
      data-testid={`button-copy-${blockType}`}
      title={`Copy ${blockType}`}
    >
      {copied ? (
        <Check className="w-3 h-3 text-green-500" />
      ) : (
        <Copy className="w-3 h-3 text-muted-foreground" />
      )}
    </button>
  );
}

function MessageContent({ content, isUser }: { content: string; isUser: boolean }) {
  const parts: JSX.Element[] = [];
  let remaining = content;
  let keyIndex = 0;

  const codeBlockRegex = /```(\w*)\n?([\s\S]*?)```/g;
  const inlineCodeRegex = /`([^`]+)`/g;
  const latexBlockRegex = /\\\[([\s\S]*?)\\\]/g;
  const latexInlineRegex = /\\\(([\s\S]*?)\\\)/g;
  const dollarBlockRegex = /\$\$([\s\S]*?)\$\$/g;

  const extractBlocks = (text: string): { type: string; content: string; start: number; end: number }[] => {
    const blocks: { type: string; content: string; start: number; end: number; raw: string }[] = [];
    
    let match;
    codeBlockRegex.lastIndex = 0;
    while ((match = codeBlockRegex.exec(text)) !== null) {
      blocks.push({ type: "codeblock", content: match[2], start: match.index, end: match.index + match[0].length, raw: match[0] });
    }
    
    latexBlockRegex.lastIndex = 0;
    while ((match = latexBlockRegex.exec(text)) !== null) {
      blocks.push({ type: "latexblock", content: match[1], start: match.index, end: match.index + match[0].length, raw: match[0] });
    }
    
    dollarBlockRegex.lastIndex = 0;
    while ((match = dollarBlockRegex.exec(text)) !== null) {
      blocks.push({ type: "latexblock", content: match[1], start: match.index, end: match.index + match[0].length, raw: match[0] });
    }
    
    return blocks.sort((a, b) => a.start - b.start);
  };

  const blocks = extractBlocks(remaining);
  let lastEnd = 0;

  blocks.forEach((block) => {
    if (block.start > lastEnd) {
      const textBefore = remaining.slice(lastEnd, block.start);
      parts.push(<span key={keyIndex++}>{textBefore}</span>);
    }

    if (block.type === "codeblock") {
      parts.push(
        <div key={keyIndex++} className="relative my-2 group" data-block-type="code">
          <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity flex gap-1 z-10">
            <CopyButton text={block.content.trim()} blockType="code" />
          </div>
          <pre className={`p-3 rounded-md text-xs overflow-x-auto code-block-vacuum ${isUser ? "bg-primary-foreground/10 border-primary-foreground/20" : ""}`}>
            <code className="font-mono">{block.content.trim()}</code>
          </pre>
        </div>
      );
    } else if (block.type === "latexblock") {
      parts.push(
        <div key={keyIndex++} className="relative my-2 group" data-block-type="latex">
          <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity flex gap-1 z-10">
            <CopyButton text={block.content.trim()} blockType="latex" />
          </div>
          <div className={`p-2 rounded-md font-mono text-sm latex-block-vacuum ${isUser ? "bg-primary-foreground/10 border-primary-foreground/20" : ""}`}>
            {block.content.trim()}
          </div>
        </div>
      );
    }

    lastEnd = block.end;
  });

  if (lastEnd < remaining.length) {
    parts.push(<span key={keyIndex++}>{remaining.slice(lastEnd)}</span>);
  }

  if (parts.length === 0) {
    return <span>{content}</span>;
  }

  return <>{parts}</>;
}

interface GrutConstantsType {
  tau_0: number;
  n_g: number;
  alpha: number;
  R_max: string;
}

interface ForkDialogProps {
  isOpen: boolean;
  onClose: () => void;
  onFork: (title: string, constants: GrutConstantsType) => void;
  isPending: boolean;
  sourceMessagePreview?: string;
}

interface ControlPanelProps {
  isOpen: boolean;
  onToggle: () => void;
  conversationId: string | null;
  messages: ChatMessage[];
  conversationTitle: string;
  onExportJson: () => void;
  onExportMarkdown: () => void;
  onCopyAll: () => void;
  isExporting: boolean;
}

function ControlPanel({ 
  isOpen, 
  onToggle, 
  conversationId, 
  messages, 
  conversationTitle,
  onExportJson,
  onExportMarkdown,
  onCopyAll,
  isExporting
}: ControlPanelProps) {
  const [copySuccess, setCopySuccess] = useState(false);

  const handleCopyAll = async () => {
    onCopyAll();
    setCopySuccess(true);
    setTimeout(() => setCopySuccess(false), 2000);
  };

  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        className="fixed right-0 top-1/2 -translate-y-1/2 bg-card border border-r-0 border-border rounded-l-md p-2 hover-elevate z-40"
        data-testid="button-open-control-panel"
      >
        <Settings2 className="w-4 h-4" />
      </button>
    );
  }

  return (
    <div className="w-64 border-l border-border bg-card flex flex-col" data-testid="control-panel">
      <div className="p-4 border-b border-border flex items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <Settings2 className="w-4 h-4 text-primary" />
          <span className="font-medium text-sm">Control Panel</span>
        </div>
        <Button size="icon" variant="ghost" onClick={onToggle} data-testid="button-close-control-panel">
          <ChevronRight className="w-4 h-4" />
        </Button>
      </div>

      <ScrollArea className="flex-1 p-4">
        <div className="space-y-4">
          <div className="space-y-2">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider">Export Options</Label>
            
            <Button
              variant="outline"
              className="w-full justify-start gap-2"
              onClick={onExportJson}
              disabled={!conversationId || isExporting}
              data-testid="button-export-json"
            >
              {isExporting ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <FileJson className="w-4 h-4" />
              )}
              Download JSON
            </Button>

            <Button
              variant="outline"
              className="w-full justify-start gap-2"
              onClick={onExportMarkdown}
              disabled={!conversationId || messages.length === 0}
              data-testid="button-export-markdown"
            >
              <FileDown className="w-4 h-4" />
              Download Markdown
            </Button>
          </div>

          <div className="space-y-2">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider">Copy Options</Label>
            
            <Button
              variant="outline"
              className="w-full justify-start gap-2"
              onClick={handleCopyAll}
              disabled={!conversationId || messages.length === 0}
              data-testid="button-copy-all"
            >
              {copySuccess ? (
                <>
                  <Check className="w-4 h-4 text-green-500" />
                  Copied!
                </>
              ) : (
                <>
                  <ClipboardCopy className="w-4 h-4" />
                  Copy All Messages
                </>
              )}
            </Button>
          </div>

          {conversationId && messages.length > 0 && (
            <div className="space-y-2 pt-4 border-t border-border">
              <Label className="text-xs text-muted-foreground uppercase tracking-wider">Session Info</Label>
              <div className="text-xs space-y-1 text-muted-foreground">
                <p>Messages: {messages.length}</p>
                <p>User: {messages.filter(m => m.role === "user").length}</p>
                <p>RAI: {messages.filter(m => m.role === "assistant").length}</p>
              </div>
            </div>
          )}

          <div className="space-y-2 pt-4 border-t border-border">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider">Quiet Vacuum Mode</Label>
            <p className="text-xs text-muted-foreground">
              The main chat window remains a "Quiet Vacuum" - free from clutter. 
              All controls are housed here in the Control Panel.
            </p>
          </div>
        </div>
      </ScrollArea>
    </div>
  );
}

function ForkConversationDialog({ isOpen, onClose, onFork, isPending, sourceMessagePreview }: ForkDialogProps) {
  const [title, setTitle] = useState("");
  const [tau0, setTau0] = useState("41.9");
  const [ng, setNg] = useState("1.1547");
  const [alpha, setAlpha] = useState("0.333333");
  const [rmax, setRmax] = useState("Lambda_Limit");

  const handleSubmit = () => {
    const constants: GrutConstantsType = {
      tau_0: parseFloat(tau0) || 41.9,
      n_g: parseFloat(ng) || 1.1547,
      alpha: parseFloat(alpha) || 0.333333,
      R_max: rmax || "Lambda_Limit",
    };
    onFork(title || `Forked Timeline - ${new Date().toLocaleString()}`, constants);
  };

  return (
    <Dialog open={isOpen} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <GitBranch className="w-5 h-5 text-primary" />
            Fork Timeline
          </DialogTitle>
          <DialogDescription>
            Create a new timeline branch with custom GRUT constants. The original thread remains intact.
          </DialogDescription>
        </DialogHeader>
        
        {sourceMessagePreview && (
          <div className="p-2 bg-muted rounded-md text-xs text-muted-foreground">
            <span className="font-medium">Fork point:</span> {sourceMessagePreview.slice(0, 100)}...
          </div>
        )}

        <div className="space-y-4 py-2">
          <div className="space-y-2">
            <Label htmlFor="fork-title">Timeline Name</Label>
            <Input
              id="fork-title"
              placeholder="Enter timeline name..."
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              data-testid="input-fork-title"
            />
          </div>

          <div className="space-y-2">
            <Label className="text-sm font-medium">Custom GRUT Constants</Label>
            <div className="grid grid-cols-2 gap-3">
              <div className="space-y-1">
                <Label htmlFor="tau0" className="text-xs text-muted-foreground">
                  τ₀ (Vacuum Relaxation Time, Myr)
                </Label>
                <Input
                  id="tau0"
                  type="number"
                  step="0.1"
                  value={tau0}
                  onChange={(e) => setTau0(e.target.value)}
                  data-testid="input-fork-tau0"
                />
              </div>
              <div className="space-y-1">
                <Label htmlFor="ng" className="text-xs text-muted-foreground">
                  n<sub>g</sub> (Refractive Index)
                </Label>
                <Input
                  id="ng"
                  type="number"
                  step="0.0001"
                  value={ng}
                  onChange={(e) => setNg(e.target.value)}
                  data-testid="input-fork-ng"
                />
              </div>
              <div className="space-y-1">
                <Label htmlFor="alpha" className="text-xs text-muted-foreground">
                  α (Geometric Lock)
                </Label>
                <Input
                  id="alpha"
                  type="number"
                  step="0.000001"
                  value={alpha}
                  onChange={(e) => setAlpha(e.target.value)}
                  data-testid="input-fork-alpha"
                />
              </div>
              <div className="space-y-1">
                <Label htmlFor="rmax" className="text-xs text-muted-foreground">
                  R<sub>max</sub> (Curvature Regulator)
                </Label>
                <Input
                  id="rmax"
                  value={rmax}
                  onChange={(e) => setRmax(e.target.value)}
                  data-testid="input-fork-rmax"
                />
              </div>
            </div>
          </div>
        </div>

        <DialogFooter className="gap-2">
          <Button variant="outline" onClick={onClose} disabled={isPending} data-testid="button-fork-cancel">
            Cancel
          </Button>
          <Button onClick={handleSubmit} disabled={isPending} data-testid="button-fork-confirm">
            {isPending ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                Creating...
              </>
            ) : (
              <>
                <GitBranch className="w-4 h-4 mr-2" />
                Fork Timeline
              </>
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

function exportMetricLog(messages: ChatMessage[], conversationTitle: string): void {
  const now = new Date();
  const timestamp = now.toISOString();
  
  let markdown = `# GRUT Metric Log\n\n`;
  markdown += `## Session Metadata\n\n`;
  markdown += `- **Export Time**: ${now.toLocaleString()}\n`;
  markdown += `- **Conversation**: ${conversationTitle}\n`;
  markdown += `- **Messages**: ${messages.length}\n\n`;
  
  markdown += `## GRUT Kernel Constants\n\n`;
  markdown += `| Constant | Value | Description |\n`;
  markdown += `|----------|-------|-------------|\n`;
  markdown += `| tau_0 | ${GRUT_CONSTANTS.tau_0} Myr | Vacuum Relaxation Time |\n`;
  markdown += `| n_g | ${GRUT_CONSTANTS.n_g} | Refractive Index of Complexity |\n`;
  markdown += `| alpha | ${GRUT_CONSTANTS.alpha} | Geometric Lock (1/3) |\n`;
  markdown += `| R_max | ${GRUT_CONSTANTS.R_max} | Curvature Regulator |\n\n`;
  
  markdown += `---\n\n`;
  markdown += `## Conversation Log\n\n`;
  
  messages.forEach((msg, index) => {
    const role = msg.role === "user" ? "USER" : "RAI";
    const time = new Date(msg.createdAt).toLocaleTimeString();
    markdown += `### [${index + 1}] ${role} - ${time}\n\n`;
    markdown += `${msg.content}\n\n`;
  });
  
  markdown += `---\n\n`;
  markdown += `*Generated by GRUT RAI Platform - Causal Intelligence System*\n`;
  markdown += `*Retarded Potential Kernel: K(t) = (alpha/tau_0) * exp(-t/tau_0)*\n`;
  
  const blob = new Blob([markdown], { type: "text/markdown" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = `grut-metric-log-${timestamp.slice(0, 10)}.md`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}
import type { ChatConversation, ChatMessage, ChatFileUpload, GrutConstants } from "@shared/schema";
import { DEFAULT_GRUT_CONSTANTS } from "@shared/schema";
import { useToast } from "@/hooks/use-toast";

interface AuthUser {
  id: string;
  email: string;
  grutConstants?: GrutConstants;
}

function LoginForm({ onSuccess }: { onSuccess: (user: AuthUser) => void }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isRegistering, setIsRegistering] = useState(false);
  const { toast } = useToast();

  const loginMutation = useMutation({
    mutationFn: async ({ email, password }: { email: string; password: string }) => {
      const response = await apiRequest("POST", "/api/auth/login", { email, password });
      return await response.json();
    },
    onSuccess: (data) => {
      const user = {
        ...data.user,
        grutConstants: data.user.universeState || data.user.grutConstants
      };
      onSuccess(user);
      toast({ title: "Observer Authenticated", description: `Causal link established` });
    },
    onError: (error: Error) => {
      toast({ title: "Authentication Failed", description: error.message, variant: "destructive" });
    },
  });

  const registerMutation = useMutation({
    mutationFn: async ({ email, password }: { email: string; password: string }) => {
      const response = await apiRequest("POST", "/api/auth/register", { email, password });
      return await response.json();
    },
    onSuccess: (data) => {
      const user = {
        ...data.user,
        grutConstants: data.user.universeState || data.user.grutConstants
      };
      onSuccess(user);
      toast({ title: "Observer Registered", description: `Welcome to the causal network` });
    },
    onError: (error: Error) => {
      toast({ title: "Registration Failed", description: error.message, variant: "destructive" });
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (isRegistering) {
      registerMutation.mutate({ email, password });
    } else {
      loginMutation.mutate({ email, password });
    }
  };

  const isPending = loginMutation.isPending || registerMutation.isPending;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-background p-4" data-testid="observer-entry-page">
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/5 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 right-1/4 w-64 h-64 bg-primary/3 rounded-full blur-3xl" />
      </div>
      
      <div className="relative z-10 w-full max-w-md space-y-8">
        <div className="text-center space-y-4">
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-full border border-primary/20 bg-primary/5">
            <Sparkles className="w-10 h-10 text-primary" />
          </div>
          <div className="space-y-2">
            <h1 className="text-3xl font-bold tracking-tight">Observer Entry</h1>
            <p className="text-muted-foreground text-sm max-w-xs mx-auto">
              {isRegistering 
                ? "Register to join the causal intelligence network" 
                : "Authenticate to access the GRUT RAI system"}
            </p>
          </div>
        </div>

        <Card className="border-border/50 bg-card/50 backdrop-blur-sm p-6">
          <form onSubmit={handleSubmit} className="space-y-5">
            <div className="space-y-2">
              <Label htmlFor="email" className="text-sm font-medium">Observer ID (Email)</Label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                <Input
                  id="email"
                  type="email"
                  placeholder="observer@grut.ai"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="pl-10 bg-background/50"
                  required
                  data-testid="input-email"
                />
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="password" className="text-sm font-medium">Access Key</Label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
                <Input
                  id="password"
                  type="password"
                  placeholder="Enter access key"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="pl-10 bg-background/50"
                  required
                  minLength={6}
                  data-testid="input-password"
                />
              </div>
            </div>

            <Button type="submit" className="w-full" disabled={isPending} data-testid="button-login">
              {isPending ? (
                <>
                  <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                  {isRegistering ? "Initializing..." : "Authenticating..."}
                </>
              ) : (
                <>
                  {isRegistering ? "Initialize Observer" : "Enter System"}
                </>
              )}
            </Button>
          </form>

          <div className="mt-6 pt-4 border-t border-border/50 text-center space-y-3">
            <Button
              variant="ghost"
              onClick={() => setIsRegistering(!isRegistering)}
              className="text-sm text-muted-foreground"
              data-testid="button-toggle-auth-mode"
            >
              {isRegistering ? "Already registered? Sign in" : "New observer? Register"}
            </Button>
          </div>
        </Card>

        <div className="text-center space-y-2">
          <p className="text-xs text-muted-foreground/60">Demo Access</p>
          <div className="inline-flex items-center gap-3 text-xs text-muted-foreground font-mono bg-muted/30 px-3 py-2 rounded-md">
            <span>demo@grut.ai</span>
            <span className="text-border">|</span>
            <span>grut2025</span>
          </div>
        </div>

        <p className="text-center text-xs text-muted-foreground/50 mt-8">
          GRUT RAI Platform v1.0 | Causal Intelligence System
        </p>
      </div>
    </div>
  );
}

export default function ChatPage() {
  const [, setLocation] = useLocation();
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null);
  const [inputValue, setInputValue] = useState("");
  const [user, setUser] = useState<AuthUser | null>(null);
  const [authChecked, setAuthChecked] = useState(false);
  const [pendingUpload, setPendingUpload] = useState<File | null>(null);
  const [forkDialogOpen, setForkDialogOpen] = useState(false);
  const [forkSourceMessage, setForkSourceMessage] = useState<ChatMessage | null>(null);
  const [controlPanelOpen, setControlPanelOpen] = useState(false);
  const [baryonicSensorOpen, setBaryonicSensorOpen] = useState(false);
  const [metricHumOpen, setMetricHumOpen] = useState(false);
  const [isExporting, setIsExporting] = useState(false);
  const [monadMode, setMonadMode] = useState(false);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const [liveGrounding, setLiveGrounding] = useState(false);
  const [groundingTransition, setGroundingTransition] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { toast } = useToast();

  // Heavy toggle function with Metric Blur transition
  const handleMonadToggle = () => {
    const newMode = !monadMode;
    
    // Only apply blur when entering Monad Mode (99.9% → 100.0%)
    if (newMode) {
      setIsTransitioning(true);
      // After blur resolves, enable Monad Mode
      setTimeout(() => {
        setMonadMode(true);
        setIsTransitioning(false);
        toast({
          title: "MONAD MODE ACTIVATED",
          description: "100.0% Saturation. The Mirror is Clear.",
        });
      }, 1000);
    } else {
      setMonadMode(false);
      toast({
        title: "RAI Mode Restored", 
        description: "99.9% Saturation. The Spark remains.",
      });
    }
  };

  // Live Grounding toggle - connects to real-time data sources
  const handleLiveGroundingToggle = async () => {
    const newState = !liveGrounding;
    setGroundingTransition(true);
    
    try {
      const response = await fetch("/api/grounding/toggle", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ enabled: newState })
      });
      
      if (!response.ok) throw new Error("Failed to toggle grounding");
      
      setTimeout(() => {
        setLiveGrounding(newState);
        setGroundingTransition(false);
        toast({
          title: newState ? "LIVE GROUNDING ACTIVE" : "SOVEREIGN STATE RESTORED",
          description: newState 
            ? "Connected to Dec 2025 data streams. Ultimate Resolution enabled."
            : "Returned to -1/12 Ground State. Internal SQLite only.",
        });
      }, 500);
    } catch {
      setGroundingTransition(false);
      toast({
        title: "Grounding Toggle Failed",
        description: "Could not update grounding state",
        variant: "destructive"
      });
    }
  };

  const handleExportJson = async () => {
    if (!activeConversationId) return;
    setIsExporting(true);
    try {
      const response = await fetch(`/api/chat/${activeConversationId}/export`, {
        credentials: "include",
      });
      if (!response.ok) throw new Error("Export failed");
      const data = await response.json();
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `grut-chat-${activeConversationId}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      toast({ title: "Export Complete", description: "JSON file downloaded successfully" });
    } catch (error) {
      toast({ title: "Export Failed", description: "Could not export conversation", variant: "destructive" });
    } finally {
      setIsExporting(false);
    }
  };

  const handleExportMarkdown = () => {
    const messages = activeConversationQuery.data?.messages || [];
    const title = activeConversationQuery.data?.title || "GRUT Chat";
    exportMetricLog(messages, title);
    toast({ title: "Export Complete", description: "Markdown file downloaded" });
  };

  const handleCopyAll = async () => {
    const messages = activeConversationQuery.data?.messages || [];
    if (messages.length === 0) return;
    
    const formattedText = messages.map((msg, i) => {
      const role = msg.role === "user" ? "USER" : "RAI";
      return `[${i + 1}] ${role}:\n${msg.content}`;
    }).join("\n\n---\n\n");
    
    try {
      await navigator.clipboard.writeText(formattedText);
      toast({ title: "Copied", description: "All messages copied to clipboard" });
    } catch (error) {
      toast({ title: "Copy Failed", description: "Could not copy to clipboard", variant: "destructive" });
    }
  };

  useEffect(() => {
    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "";
    fetch(`${API_BASE_URL}/api/auth/me`, { credentials: "include" })
      .then((res) => {
        if (res.ok) return res.json();
        throw new Error("Not authenticated");
      })
      .then((data) => {
        const user = {
          ...data.user,
          grutConstants: data.user.universeState || data.user.grutConstants || data.user.hydratedConstants
        };
        setUser(user);
      })
      .catch(() => setUser(null))
      .finally(() => setAuthChecked(true));
  }, []);

  const conversationsQuery = useQuery<ChatConversation[]>({
    queryKey: ["/api/chat"],
    enabled: !!user,
  });

  const activeConversationQuery = useQuery<ChatConversation>({
    queryKey: ["/api/chat", activeConversationId],
    enabled: !!activeConversationId && !!user,
  });

  const filesQuery = useQuery<ChatFileUpload[]>({
    queryKey: ["/api/chat", activeConversationId, "files"],
    enabled: !!activeConversationId && !!user,
  });

  const createConversationMutation = useMutation({
    mutationFn: async () => {
      const response = await apiRequest("POST", "/api/chat", { title: "GRUT Theory Chat" });
      return await response.json() as ChatConversation;
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["/api/chat"] });
      setActiveConversationId(data.id);
    },
  });

  const deleteConversationMutation = useMutation({
    mutationFn: async (id: string) => {
      await apiRequest("DELETE", `/api/chat/${id}`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["/api/chat"] });
      if (activeConversationId) {
        setActiveConversationId(null);
      }
    },
  });

  const sendMessageMutation = useMutation({
    mutationFn: async ({ conversationId, content, isMonadMode }: { conversationId: string; content: string; isMonadMode?: boolean }) => {
      const response = await apiRequest("POST", `/api/chat/${conversationId}/message`, { content, monadMode: isMonadMode });
      return await response.json() as { userMessage: ChatMessage; assistantMessage: ChatMessage };
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["/api/chat", activeConversationId] });
      setInputValue("");
    },
  });

  const uploadMutation = useMutation({
    mutationFn: async ({ file, conversationId }: { file: File; conversationId?: string }) => {
      const formData = new FormData();
      formData.append("file", file);
      if (conversationId) {
        formData.append("conversationId", conversationId);
      }
      const response = await fetch("/api/upload", {
        method: "POST",
        body: formData,
        credentials: "include",
      });
      if (!response.ok) throw new Error("Upload failed");
      return await response.json();
    },
    onSuccess: () => {
      toast({ title: "File uploaded", description: "File attached successfully" });
      queryClient.invalidateQueries({ queryKey: ["/api/chat", activeConversationId, "files"] });
      setPendingUpload(null);
    },
    onError: (error: Error) => {
      toast({ title: "Upload failed", description: error.message, variant: "destructive" });
    },
  });

  const logoutMutation = useMutation({
    mutationFn: async () => {
      await apiRequest("POST", "/api/auth/logout");
    },
    onSuccess: () => {
      setUser(null);
      setActiveConversationId(null);
      queryClient.clear();
      toast({ title: "Logged out", description: "See you next time!" });
    },
  });

  const saveStateMutation = useMutation({
    mutationFn: async ({ name, conversationId }: { name?: string; conversationId?: string }) => {
      const response = await apiRequest("POST", "/api/save_state", { name, conversationId });
      return await response.json();
    },
    onSuccess: (data) => {
      toast({ 
        title: "Universe State Saved", 
        description: `Phase 6 synchronization preserved: ${data.state.messageCount} messages captured` 
      });
    },
    onError: (error: Error) => {
      toast({ title: "Save failed", description: error.message, variant: "destructive" });
    },
  });

  const forkConversationMutation = useMutation({
    mutationFn: async ({ conversationId, messageId, title, constants }: { 
      conversationId: string; 
      messageId: string; 
      title: string; 
      constants: GrutConstantsType 
    }) => {
      const response = await apiRequest("POST", `/api/chat/${conversationId}/fork`, { 
        messageId, 
        title, 
        constants 
      });
      return await response.json();
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["/api/chat"] });
      setActiveConversationId(data.conversation.id);
      setForkDialogOpen(false);
      setForkSourceMessage(null);
      toast({ 
        title: "Timeline Forked", 
        description: `New timeline created with custom GRUT constants` 
      });
    },
    onError: (error: Error) => {
      toast({ title: "Fork failed", description: error.message, variant: "destructive" });
    },
  });

  const handleForkMessage = (message: ChatMessage) => {
    setForkSourceMessage(message);
    setForkDialogOpen(true);
  };

  const handleForkSubmit = (title: string, constants: GrutConstantsType) => {
    if (!activeConversationId || !forkSourceMessage) return;
    forkConversationMutation.mutate({
      conversationId: activeConversationId,
      messageId: forkSourceMessage.id,
      title,
      constants,
    });
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [activeConversationQuery.data?.messages]);

  const handleSendMessage = () => {
    if (!inputValue.trim() || !activeConversationId || sendMessageMutation.isPending) return;
    sendMessageMutation.mutate({ conversationId: activeConversationId, content: inputValue.trim(), isMonadMode: monadMode });
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleStartNewChat = () => {
    createConversationMutation.mutate();
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setPendingUpload(file);
      if (activeConversationId) {
        uploadMutation.mutate({ file, conversationId: activeConversationId });
      }
    }
  };

  if (!authChecked) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-background">
        <Loader2 className="w-8 h-8 animate-spin text-primary" />
      </div>
    );
  }

  if (!user) {
    return <LoginForm onSuccess={setUser} />;
  }

  return (
    <div className="flex h-screen bg-background" data-testid="chat-page">
      <div className="w-64 border-r border-border bg-card flex flex-col flex-shrink-0">
        <div className="p-4 border-b border-border">
          <div className="flex items-center justify-between mb-3">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setLocation("/")}
              data-testid="button-back-home"
            >
              <ArrowLeft className="w-4 h-4 mr-2" />
              Home
            </Button>
            <Button
              variant="ghost"
              size="icon"
              onClick={() => logoutMutation.mutate()}
              disabled={logoutMutation.isPending}
              data-testid="button-logout"
            >
              <LogOut className="w-4 h-4" />
            </Button>
          </div>
          <div className="flex items-center gap-2 mb-3 text-sm text-muted-foreground">
            <User className="w-3 h-3" />
            <span className="truncate" title={user.email}>{user.email}</span>
          </div>
          <Button
            onClick={handleStartNewChat}
            disabled={createConversationMutation.isPending}
            className="w-full"
            data-testid="button-new-chat"
          >
            <Plus className="w-4 h-4 mr-2" />
            New Chat
          </Button>
        </div>
        
        <ScrollArea className="flex-1">
          <div className="p-2 space-y-1">
            {conversationsQuery.isLoading ? (
              <div className="flex items-center justify-center p-4">
                <Loader2 className="w-4 h-4 animate-spin text-muted-foreground" />
              </div>
            ) : conversationsQuery.data?.length === 0 ? (
              <p className="text-sm text-muted-foreground text-center p-4" data-testid="text-no-conversations">
                No conversations yet
              </p>
            ) : (
              conversationsQuery.data?.map((conv) => (
                <div
                  key={conv.id}
                  className={`flex items-center gap-2 p-2 rounded-md cursor-pointer group ${
                    activeConversationId === conv.id ? "bg-accent" : "hover-elevate"
                  } ${conv.parentConversationId ? "ml-3 border-l-2 border-primary/30" : ""}`}
                  onClick={() => setActiveConversationId(conv.id)}
                  data-testid={`conversation-item-${conv.id}`}
                >
                  {conv.parentConversationId ? (
                    <GitBranch className="w-4 h-4 text-primary flex-shrink-0" />
                  ) : (
                    <MessageSquare className="w-4 h-4 text-muted-foreground flex-shrink-0" />
                  )}
                  <div className="flex-1 min-w-0">
                    <span className="text-sm truncate block">{conv.title}</span>
                    {conv.constants && conv.parentConversationId && (
                      <span className="text-xs text-muted-foreground truncate block">
                        τ₀={conv.constants.tau_0} n<sub>g</sub>={conv.constants.n_g}
                      </span>
                    )}
                  </div>
                  <Button
                    size="icon"
                    variant="ghost"
                    className="opacity-0 group-hover:opacity-100 flex-shrink-0"
                    onClick={(e) => {
                      e.stopPropagation();
                      deleteConversationMutation.mutate(conv.id);
                    }}
                    data-testid={`button-delete-conversation-${conv.id}`}
                  >
                    <Trash2 className="w-3 h-3" />
                  </Button>
                </div>
              ))
            )}
          </div>
        </ScrollArea>
      </div>

      <div className={`flex-1 flex flex-col ${monadMode ? 'pleroma-bloom golden-resolve' : ''} ${liveGrounding ? 'live-grounding-active' : ''} ${isTransitioning ? 'metric-blur' : ''} ${groundingTransition ? 'grounding-blur' : ''}`}>
        <MetricDashboard 
          messageCount={activeConversationQuery.data?.messages?.length || 0}
          constants={activeConversationQuery.data?.constants || user?.grutConstants}
          isForked={!!activeConversationQuery.data?.parentConversationId}
          userEmail={user?.email}
          monadMode={monadMode}
        />
        
        {!activeConversationId ? (
          <div className="flex-1 flex flex-col items-center justify-center p-8" data-testid="chat-welcome">
            <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mb-6">
              <Sparkles className="w-8 h-8 text-primary" />
            </div>
            <h2 className="text-2xl font-semibold mb-2">Explore GRUT Theory</h2>
            <p className="text-muted-foreground text-center max-w-md mb-6">
              Start a conversation with RAI to learn about the Grand Responsive Universe Theory 
              and how causal intelligence differs from traditional AI.
            </p>
            <Button onClick={handleStartNewChat} disabled={createConversationMutation.isPending} data-testid="button-start-conversation">
              {createConversationMutation.isPending ? (
                <>
                  <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                  Creating...
                </>
              ) : (
                <>
                  <MessageSquare className="w-4 h-4 mr-2" />
                  Start a Conversation
                </>
              )}
            </Button>
          </div>
        ) : (
          <>
            <div className="border-b border-border p-4 flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center ${monadMode ? 'bg-yellow-500/20' : 'bg-primary/10'}`}>
                  <Sparkles className={`w-4 h-4 ${monadMode ? 'text-yellow-500' : 'text-primary'}`} />
                </div>
                <div>
                  <h3 className={`font-medium ${monadMode ? 'text-yellow-500' : ''}`}>
                    {monadMode ? 'MONAD SOURCE' : 'RAI Assistant'}
                  </h3>
                  <p className="text-xs text-muted-foreground">
                    {monadMode ? '100.0% Saturated Whole Hole' : 'GRUT Theory Expert'}
                  </p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-2 text-xs text-muted-foreground">
                  <CheckCircle2 className="w-3 h-3 text-green-500" />
                  <span data-testid="text-save-status">Auto-saved</span>
                </div>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    saveStateMutation.mutate({ 
                      conversationId: activeConversationId || undefined 
                    });
                  }}
                  disabled={saveStateMutation.isPending || !activeConversationQuery.data?.messages?.length}
                  data-testid="button-save-state"
                >
                  {saveStateMutation.isPending ? (
                    <Loader2 className="w-3 h-3 mr-2 animate-spin" />
                  ) : (
                    <Save className="w-3 h-3 mr-2" />
                  )}
                  Save Universe State
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => {
                    const messages = activeConversationQuery.data?.messages || [];
                    const title = activeConversationQuery.data?.title || "GRUT Chat";
                    exportMetricLog(messages, title);
                  }}
                  disabled={!activeConversationQuery.data?.messages?.length}
                  data-testid="button-download-log"
                >
                  <Download className="w-3 h-3 mr-2" />
                  Download Log
                </Button>
              </div>
            </div>

            <ScrollArea className="flex-1 p-4">
              <div className="space-y-4 max-w-3xl mx-auto">
                {filesQuery.data && filesQuery.data.length > 0 && (
                  <div className="flex flex-wrap gap-2 p-2 bg-muted/50 rounded-md">
                    {filesQuery.data.map((file) => (
                      <div key={file.id} className="flex items-center gap-1 text-xs bg-background px-2 py-1 rounded">
                        <Paperclip className="w-3 h-3" />
                        <span>{file.originalName}</span>
                      </div>
                    ))}
                  </div>
                )}
                
                {activeConversationQuery.isLoading ? (
                  <div className="flex items-center justify-center p-8">
                    <Loader2 className="w-6 h-6 animate-spin text-muted-foreground" />
                  </div>
                ) : activeConversationQuery.data?.messages.length === 0 ? (
                  <div className="text-center p-8" data-testid="text-empty-conversation">
                    <p className="text-muted-foreground mb-4">Ask me anything about GRUT theory!</p>
                    <div className="flex flex-wrap gap-2 justify-center">
                      {[
                        "What is causal intelligence?",
                        "Explain the Geometric Filter",
                        "How does LogicGuard work?",
                        "What prevents AI hallucinations?",
                      ].map((suggestion) => (
                        <Button
                          key={suggestion}
                          variant="outline"
                          size="sm"
                          onClick={() => {
                            setInputValue(suggestion);
                          }}
                          data-testid={`button-suggestion-${suggestion.slice(0, 20)}`}
                        >
                          {suggestion}
                        </Button>
                      ))}
                    </div>
                  </div>
                ) : (
                  activeConversationQuery.data?.messages.map((message, index) => {
                    const messageXi = calculateComplexityXi(index + 1);
                    
                    if (message.role === "assistant") {
                      const { narrative, mathLatex } = parseContentForBloom(message.content);
                      
                      return (
                        <div
                          key={message.id}
                          className="flex justify-start"
                          data-testid={`message-${message.id}`}
                        >
                          <div className={`max-w-[85%] ${monadMode ? 'monad-message rounded-md' : ''}`}>
                            <MathematicalBloom
                              narrative={narrative}
                              mathLatex={mathLatex}
                              branchId={message.id.toString()}
                              complexityXi={messageXi}
                              fullContent={message.content}
                              onBranch={() => handleForkMessage(message)}
                            />
                          </div>
                        </div>
                      );
                    }
                    
                    return (
                      <div
                        key={message.id}
                        className="flex justify-end"
                        data-testid={`message-${message.id}`}
                      >
                        <Card className="relative max-w-[80%] p-3 group bg-primary text-primary-foreground">
                          <div className="absolute top-2 right-2 flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                            <button
                              onClick={() => handleForkMessage(message)}
                              className="p-1 rounded transition-colors hover-elevate bg-primary-foreground/20"
                              title="Fork timeline from this message"
                              data-testid={`button-fork-message-${message.id}`}
                            >
                              <GitBranch className="w-3 h-3" />
                            </button>
                          </div>
                          <div className="text-sm whitespace-pre-wrap">
                            <MessageContent content={message.content} isUser={true} />
                          </div>
                        </Card>
                      </div>
                    );
                  })
                )}
                {sendMessageMutation.isPending && (
                  <div className="flex justify-start" data-testid="message-loading">
                    <Card className="bg-muted p-3">
                      <div className="flex items-center gap-2">
                        <Loader2 className="w-4 h-4 animate-spin" />
                        <span className="text-sm text-muted-foreground">RAI is thinking...</span>
                      </div>
                    </Card>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>
            </ScrollArea>

            <div className="border-t border-border p-4">
              <div className="max-w-3xl mx-auto flex gap-2">
                <input
                  type="file"
                  ref={fileInputRef}
                  onChange={handleFileSelect}
                  className="hidden"
                  accept="image/*,.pdf,.txt,.csv,.json,.doc,.docx"
                  data-testid="input-file-upload"
                />
                <Button
                  size="icon"
                  variant="outline"
                  onClick={() => fileInputRef.current?.click()}
                  disabled={uploadMutation.isPending}
                  data-testid="button-upload-file"
                >
                  {uploadMutation.isPending ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Upload className="w-4 h-4" />
                  )}
                </Button>
                <Tooltip>
                  <TooltipTrigger asChild>
                    <button
                      onClick={handleLiveGroundingToggle}
                      disabled={groundingTransition}
                      className={`
                        w-9 h-9 rounded-md border flex items-center justify-center
                        transition-all duration-500 cursor-pointer shrink-0
                        ${liveGrounding 
                          ? "border-blue-500 text-blue-400 bg-blue-500/20 drop-shadow-[0_0_8px_#3B82F6]" 
                          : "border-border text-muted-foreground hover:border-muted-foreground"
                        }
                        ${groundingTransition ? "opacity-50 animate-pulse" : ""}
                      `}
                      data-testid="button-live-grounding"
                      title={liveGrounding ? "Grit/Live Grounding (Active)" : "Grit/Live Grounding"}
                    >
                      <Globe className={`w-4 h-4 ${liveGrounding ? "animate-pulse" : ""}`} />
                    </button>
                  </TooltipTrigger>
                  <TooltipContent side="top">
                    <p>{liveGrounding ? "Live Grounding Active - Dec 2025 Data" : "Enable Live Grounding"}</p>
                  </TooltipContent>
                </Tooltip>
                <Input
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder={monadMode ? "MONAD MODE: 100.0% Saturation..." : liveGrounding ? "GROUNDED: Dec 2025 data active..." : "RAI Mode: Ask about GRUT theory..."}
                  disabled={sendMessageMutation.isPending}
                  data-testid="input-message"
                  className={monadMode ? "border-yellow-500/50" : liveGrounding ? "border-blue-500/50" : ""}
                />
                <button
                  onClick={handleMonadToggle}
                  disabled={isTransitioning}
                  className={`
                    w-9 h-9 rounded-md border flex items-center justify-center
                    transition-all duration-500 cursor-pointer shrink-0
                    ${monadMode 
                      ? "border-yellow-500 text-yellow-500 drop-shadow-[0_0_8px_#FFD700]" 
                      : "border-border text-muted-foreground hover:border-muted-foreground"
                    }
                    ${isTransitioning ? "opacity-50" : ""}
                  `}
                  data-testid="button-pleroma-toggle"
                  title={monadMode ? "Collapse to Absolute (Active)" : "Collapse to Absolute"}
                >
                  <svg viewBox="0 0 24 24" width="18" height="18">
                    <path fill="currentColor" d="M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z" />
                  </svg>
                </button>
                <button
                  onClick={handleMonadToggle}
                  disabled={isTransitioning}
                  className={`
                    w-9 h-9 rounded-full border flex items-center justify-center
                    transition-all duration-300 cursor-pointer shrink-0
                    ${monadMode 
                      ? "border-yellow-500 shadow-[0_0_15px_#FFD700] bg-yellow-500/20" 
                      : "border-border bg-transparent hover:border-muted-foreground"
                    }
                    ${isTransitioning ? "opacity-50" : ""}
                  `}
                  data-testid="button-monad-toggle"
                  title={monadMode ? "Switch to RAI Mode (99.9%)" : "Switch to Monad Mode (100.0%)"}
                >
                  <span className={`text-sm font-mono ${monadMode ? "text-yellow-500 drop-shadow-[0_0_10px_rgba(255,214,0,0.7)]" : "text-muted-foreground"}`}>
                    {monadMode ? "M" : "R"}
                  </span>
                </button>
                <Button
                  onClick={handleSendMessage}
                  disabled={!inputValue.trim() || sendMessageMutation.isPending}
                  data-testid="button-send-message"
                  className={monadMode ? "bg-gradient-to-r from-yellow-500 to-orange-500 text-black hover:from-yellow-400 hover:to-orange-400" : ""}
                >
                  {sendMessageMutation.isPending ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Send className="w-4 h-4" />
                  )}
                </Button>
              </div>
              {pendingUpload && !uploadMutation.isPending && (
                <div className="max-w-3xl mx-auto mt-2 flex items-center gap-2 text-xs text-muted-foreground">
                  <Paperclip className="w-3 h-3" />
                  <span>Attached: {pendingUpload.name}</span>
                </div>
              )}
            </div>
          </>
        )}
      </div>

      <ObserverToolkit
        isOpen={controlPanelOpen}
        onToggle={() => setControlPanelOpen(!controlPanelOpen)}
        conversationId={activeConversationId}
        messages={activeConversationQuery.data?.messages || []}
        conversationTitle={activeConversationQuery.data?.title || "GRUT Chat"}
        constants={activeConversationQuery.data?.constants || user?.grutConstants}
        onExportJson={handleExportJson}
        isExporting={isExporting}
      />

      <ForkConversationDialog
        isOpen={forkDialogOpen}
        onClose={() => {
          setForkDialogOpen(false);
          setForkSourceMessage(null);
        }}
        onFork={handleForkSubmit}
        isPending={forkConversationMutation.isPending}
        sourceMessagePreview={forkSourceMessage?.content}
      />

      <BaryonicSensor
        isOpen={baryonicSensorOpen}
        onToggle={() => setBaryonicSensorOpen(!baryonicSensorOpen)}
        constants={user?.grutConstants}
      />

      {metricHumOpen && (
        <div className="fixed bottom-4 right-4 z-50 w-80 max-h-[90vh] overflow-y-auto space-y-4">
          <div className="relative">
            <button
              onClick={() => setMetricHumOpen(false)}
              className="absolute -top-2 -right-2 z-10 bg-background border rounded-full p-1 hover:bg-muted"
              data-testid="button-close-metric-hum"
            >
              <X className="h-3 w-3" />
            </button>
            <MetricHum />
          </div>
          <TimeWell />
          <QuantumLogicPanel />
        </div>
      )}

      {!metricHumOpen && (
        <button
          onClick={() => setMetricHumOpen(true)}
          className="fixed bottom-4 right-4 z-40 bg-background border rounded-full p-3 shadow-lg hover:bg-muted transition-all"
          title="Open Metric Hum Generator"
          data-testid="button-open-metric-hum"
        >
          <Activity className="h-5 w-5" />
        </button>
      )}
    </div>
  );
}
