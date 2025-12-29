import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card } from "@/components/ui/card";
import { 
  Plus, Minus, Copy, Check, Share2, GitBranch, 
  ChevronDown, ChevronUp, Sigma, BookOpen
} from "lucide-react";
import { 
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import { useToast } from "@/hooks/use-toast";

interface MathematicalBloomProps {
  narrative: string;
  mathLatex?: string;
  branchId: string;
  complexityXi?: number;
  onCopy?: (content: string) => void;
  onShare?: (branchId: string) => void;
  onBranch?: (branchId: string) => void;
  className?: string;
  fullContent?: string;
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

function extractMathFromContent(content: string): { narrative: string; mathBlocks: string[] } {
  const mathBlocks: string[] = [];
  let narrative = content;
  
  const latexBlockRegex = /\\\[([\s\S]*?)\\\]/g;
  const dollarBlockRegex = /\$\$([\s\S]*?)\$\$/g;
  
  let match;
  
  latexBlockRegex.lastIndex = 0;
  while ((match = latexBlockRegex.exec(content)) !== null) {
    mathBlocks.push(match[1].trim());
    narrative = narrative.replace(match[0], "");
  }
  
  dollarBlockRegex.lastIndex = 0;
  while ((match = dollarBlockRegex.exec(content)) !== null) {
    mathBlocks.push(match[1].trim());
    narrative = narrative.replace(match[0], "");
  }
  
  return { narrative: narrative.trim(), mathBlocks };
}

function CopyButton({ text, className = "", blockType = "text" }: { text: string; className?: string; blockType?: "code" | "latex" | "text" }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    const success = await copyToClipboardWithFallback(text);
    if (success) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
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

function renderTextWithInlineCode(text: string, startKey: number): { elements: JSX.Element[]; nextKey: number } {
  const inlineCodeRegex = /`([^`]+)`/g;
  const elements: JSX.Element[] = [];
  let lastIndex = 0;
  let key = startKey;
  let match;

  inlineCodeRegex.lastIndex = 0;
  while ((match = inlineCodeRegex.exec(text)) !== null) {
    if (match.index > lastIndex) {
      elements.push(<span key={key++}>{text.slice(lastIndex, match.index)}</span>);
    }
    elements.push(
      <code key={key++} className="px-1 py-0.5 rounded text-xs font-mono bg-muted">
        {match[1]}
      </code>
    );
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < text.length) {
    elements.push(<span key={key++}>{text.slice(lastIndex)}</span>);
  }

  return { elements, nextKey: key };
}

function NarrativeContent({ content }: { content: string }) {
  const parts: JSX.Element[] = [];
  let remaining = content;
  let keyIndex = 0;

  const codeBlockRegex = /```(\w*)\n?([\s\S]*?)```/g;

  const extractBlocks = (text: string): { type: string; content: string; start: number; end: number; raw: string }[] => {
    const blocks: { type: string; content: string; start: number; end: number; raw: string }[] = [];
    
    let match;
    codeBlockRegex.lastIndex = 0;
    while ((match = codeBlockRegex.exec(text)) !== null) {
      blocks.push({ type: "codeblock", content: match[2], start: match.index, end: match.index + match[0].length, raw: match[0] });
    }
    
    return blocks.sort((a, b) => a.start - b.start);
  };

  const blocks = extractBlocks(remaining);
  let lastEnd = 0;

  blocks.forEach((block) => {
    if (block.start > lastEnd) {
      const textBefore = remaining.slice(lastEnd, block.start);
      const { elements, nextKey } = renderTextWithInlineCode(textBefore, keyIndex);
      parts.push(...elements);
      keyIndex = nextKey;
    }

    if (block.type === "codeblock") {
      parts.push(
        <div key={keyIndex++} className="relative my-2 group" data-block-type="code">
          <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity flex gap-1 z-10">
            <CopyButton text={block.content.trim()} blockType="code" />
          </div>
          <pre className="p-3 rounded-md text-xs overflow-x-auto code-block-vacuum">
            <code className="font-mono">{block.content.trim()}</code>
          </pre>
        </div>
      );
    }

    lastEnd = block.end;
  });

  if (lastEnd < remaining.length) {
    const textAfter = remaining.slice(lastEnd);
    const { elements, nextKey } = renderTextWithInlineCode(textAfter, keyIndex);
    parts.push(...elements);
    keyIndex = nextKey;
  }

  if (parts.length === 0) {
    return <span>{content}</span>;
  }

  return <>{parts}</>;
}

export function MathematicalBloom({
  narrative,
  mathLatex,
  branchId,
  complexityXi = 0.5,
  onCopy,
  onShare,
  onBranch,
  className = "",
  fullContent = ""
}: MathematicalBloomProps) {
  const [isExpanded, setIsExpanded] = useState(false);
  const [copiedNarrative, setCopiedNarrative] = useState(false);
  const [copiedMath, setCopiedMath] = useState(false);
  const [shared, setShared] = useState(false);
  const { toast } = useToast();

  const xiPercent = (complexityXi * 100).toFixed(1);
  
  const getXiStatus = () => {
    if (complexityXi < 0.5) return "STABLE";
    if (complexityXi < 0.9) return "MODERATE";
    if (complexityXi < 1.0) return "WARNING";
    return "EXCEEDED";
  };

  const getXiColor = () => {
    if (complexityXi < 0.5) return "text-green-500";
    if (complexityXi < 0.9) return "text-yellow-500";
    if (complexityXi < 1.0) return "text-orange-500";
    return "text-red-500";
  };

  const handleCopyNarrative = async () => {
    const textToCopy = fullContent || narrative;
    const success = await copyToClipboardWithFallback(textToCopy);
    if (success) {
      setCopiedNarrative(true);
      setTimeout(() => setCopiedNarrative(false), 2000);
      toast({ title: "Copied to clipboard", description: "Full response copied" });
      onCopy?.(textToCopy);
    } else {
      toast({ title: "Copy failed", description: "Could not copy to clipboard", variant: "destructive" });
    }
  };

  const handleCopyMath = async () => {
    if (!mathLatex) return;
    const success = await copyToClipboardWithFallback(mathLatex);
    if (success) {
      setCopiedMath(true);
      setTimeout(() => setCopiedMath(false), 2000);
      toast({ title: "Math copied", description: "LaTeX content copied to clipboard" });
      onCopy?.(mathLatex);
    } else {
      toast({ title: "Copy failed", description: "Could not copy math", variant: "destructive" });
    }
  };

  const handleShare = async () => {
    const url = `${window.location.origin}/chat?branch=${branchId}`;
    const success = await copyToClipboardWithFallback(url);
    if (success) {
      setShared(true);
      setTimeout(() => setShared(false), 2000);
      toast({ title: "Link ready", description: "Share link copied to clipboard" });
      onShare?.(branchId);
    } else {
      toast({ title: "Share failed", description: "Could not generate link", variant: "destructive" });
    }
  };

  const handleBranch = () => {
    onBranch?.(branchId);
  };

  const hasMath = mathLatex && mathLatex.trim().length > 0;

  return (
    <div className={`relative ${className}`} data-testid={`bloom-${branchId}`}>
      <Collapsible open={isExpanded} onOpenChange={setIsExpanded}>
        <Card className="bg-muted overflow-visible">
          <div className="p-4 pb-2">
            <div className="flex items-start gap-2 mb-2">
              <BookOpen className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
              <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                Groot (Narrative)
              </span>
            </div>
            
            <div className="text-sm whitespace-pre-wrap pl-6" data-testid={`bloom-narrative-${branchId}`}>
              <NarrativeContent content={narrative} />
            </div>
          </div>

          {hasMath && (
            <CollapsibleContent className="overflow-hidden data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0">
              <div className="border-t border-border mx-4" />
              <div className="p-4 pt-3 bg-background/30">
                <div className="flex items-start gap-2 mb-2">
                  <Sigma className="w-4 h-4 text-primary mt-0.5 flex-shrink-0" />
                  <span className="text-xs font-medium text-muted-foreground uppercase tracking-wider">
                    Grit (Mathematical Extension)
                  </span>
                </div>
                
                <div 
                  className="pl-6 font-mono text-sm latex-block-vacuum p-3 rounded-md bg-card/50 border border-border/50 overflow-x-auto"
                  data-testid={`bloom-math-${branchId}`}
                >
                  {mathLatex}
                </div>
                
                <div className="flex items-center gap-2 mt-3 pl-6">
                  <Badge variant="outline" className="text-xs">
                    <span className="text-muted-foreground mr-1">Logic Guard:</span>
                    <span className={getXiColor()}>{getXiStatus()}</span>
                  </Badge>
                  <Badge variant="outline" className={`text-xs ${getXiColor()}`}>
                    <span className="text-muted-foreground mr-1">Xi:</span>
                    {xiPercent}%
                  </Badge>
                </div>
              </div>
            </CollapsibleContent>
          )}

          <div className="flex items-center justify-between gap-2 px-4 py-2 border-t border-border/50">
            {hasMath && (
              <CollapsibleTrigger asChild>
                <Button 
                  variant="ghost" 
                  size="sm" 
                  className="gap-1 text-xs"
                  data-testid={`bloom-toggle-${branchId}`}
                >
                  {isExpanded ? (
                    <>
                      <Minus className="w-3 h-3" />
                      <span>Collapse Grit</span>
                      <ChevronUp className="w-3 h-3" />
                    </>
                  ) : (
                    <>
                      <Plus className="w-3 h-3" />
                      <span>Expand Grit</span>
                      <ChevronDown className="w-3 h-3" />
                    </>
                  )}
                </Button>
              </CollapsibleTrigger>
            )}
            
            {!hasMath && <div />}

            <div className="flex items-center gap-1">
              <Button
                variant="ghost"
                size="sm"
                onClick={handleCopyNarrative}
                className="gap-1 text-xs"
                data-testid={`bloom-copy-narrative-${branchId}`}
              >
                {copiedNarrative ? (
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

              {hasMath && (
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={handleCopyMath}
                  className="gap-1 text-xs"
                  data-testid={`bloom-copy-math-${branchId}`}
                >
                  {copiedMath ? (
                    <>
                      <Check className="w-3 h-3 text-green-500" />
                      <span className="text-green-500">Copied</span>
                    </>
                  ) : (
                    <>
                      <Sigma className="w-3 h-3" />
                      <span>Copy Math</span>
                    </>
                  )}
                </Button>
              )}

              <Button
                variant="ghost"
                size="sm"
                onClick={handleShare}
                className="gap-1 text-xs"
                data-testid={`bloom-share-${branchId}`}
              >
                {shared ? (
                  <>
                    <Check className="w-3 h-3 text-green-500" />
                    <span className="text-green-500">Link Ready</span>
                  </>
                ) : (
                  <>
                    <Share2 className="w-3 h-3" />
                    <span>Share</span>
                  </>
                )}
              </Button>

              <Button
                variant="ghost"
                size="sm"
                onClick={handleBranch}
                className="gap-1 text-xs"
                data-testid={`bloom-branch-${branchId}`}
              >
                <GitBranch className="w-3 h-3" />
                <span>Branch</span>
              </Button>
            </div>
          </div>
        </Card>
      </Collapsible>
    </div>
  );
}

export function parseContentForBloom(content: string): { narrative: string; mathLatex: string | undefined } {
  const { narrative, mathBlocks } = extractMathFromContent(content);
  const mathLatex = mathBlocks.length > 0 ? mathBlocks.join("\n\n") : undefined;
  return { narrative: narrative || content, mathLatex };
}
