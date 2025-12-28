import { useState, useCallback } from "react";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Label } from "@/components/ui/label";
import { Badge } from "@/components/ui/badge";
import { useToast } from "@/hooks/use-toast";
import {
  Settings2,
  ChevronRight,
  FileDown,
  FileJson,
  ClipboardCopy,
  Code,
  FileText,
  Check,
  Loader2,
  Eye,
  Wrench,
  Sparkles,
  Copy,
  Download
} from "lucide-react";

interface ChatMessage {
  id: string;
  role: string;
  content: string;
  createdAt: string;
}

interface GrutConstants {
  tau_0: number;
  n_g: number;
  alpha: number;
  R_max: string;
}

interface ObserverToolkitProps {
  isOpen: boolean;
  onToggle: () => void;
  conversationId: string | null;
  messages: ChatMessage[];
  conversationTitle: string;
  constants?: GrutConstants;
  onExportJson: () => void;
  isExporting: boolean;
}

const DEFAULT_CONSTANTS: GrutConstants = {
  tau_0: 41.9,
  n_g: 1.1547,
  alpha: 0.333333,
  R_max: "Lambda_Limit"
};

function sanitizeForMarkdown(text: string): string {
  return text
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\|/g, "\\|");
}

function parseCodeBlocks(content: string): { type: string; content: string; language?: string }[] {
  const blocks: { type: string; content: string; language?: string }[] = [];
  const codeBlockRegex = /```(\w*)\n?([\s\S]*?)```/g;
  const latexBlockRegex = /\\\[([\s\S]*?)\\\]/g;
  const dollarBlockRegex = /\$\$([\s\S]*?)\$\$/g;
  const inlineLatexRegex = /\\\(([\s\S]*?)\\\)/g;

  let match;
  
  codeBlockRegex.lastIndex = 0;
  while ((match = codeBlockRegex.exec(content)) !== null) {
    blocks.push({ type: "code", content: match[2].trim(), language: match[1] || "text" });
  }
  
  latexBlockRegex.lastIndex = 0;
  while ((match = latexBlockRegex.exec(content)) !== null) {
    blocks.push({ type: "latex", content: match[1].trim() });
  }
  
  dollarBlockRegex.lastIndex = 0;
  while ((match = dollarBlockRegex.exec(content)) !== null) {
    blocks.push({ type: "latex", content: match[1].trim() });
  }
  
  inlineLatexRegex.lastIndex = 0;
  while ((match = inlineLatexRegex.exec(content)) !== null) {
    blocks.push({ type: "latex-inline", content: match[1].trim() });
  }

  return blocks;
}

function generateMarkdownMirror(
  messages: ChatMessage[],
  conversationTitle: string,
  constants: GrutConstants
): string {
  const now = new Date();
  const timestamp = now.toISOString();
  
  let markdown = `# GRUT Observer Log\n\n`;
  markdown += `> Exported via Observer Toolkit - Markdown Mirror\n\n`;
  markdown += `---\n\n`;
  
  markdown += `## Session Metadata\n\n`;
  markdown += `| Property | Value |\n`;
  markdown += `|----------|-------|\n`;
  markdown += `| Export Time | ${now.toLocaleString()} |\n`;
  markdown += `| Conversation | ${sanitizeForMarkdown(conversationTitle)} |\n`;
  markdown += `| Total Messages | ${messages.length} |\n`;
  markdown += `| User Messages | ${messages.filter(m => m.role === "user").length} |\n`;
  markdown += `| RAI Responses | ${messages.filter(m => m.role === "assistant").length} |\n\n`;
  
  markdown += `## GRUT Kernel Constants\n\n`;
  markdown += `| Constant | Symbol | Value | Description |\n`;
  markdown += `|----------|--------|-------|-------------|\n`;
  markdown += `| Vacuum Relaxation Time | τ₀ | ${constants.tau_0} Myr | Fundamental time constant |\n`;
  markdown += `| Refractive Index | n_g | ${constants.n_g} | Complexity refractive index |\n`;
  markdown += `| Geometric Lock | α | ${constants.alpha} | Geometric constraint (1/3) |\n`;
  markdown += `| Curvature Regulator | R_max | ${constants.R_max} | Maximum curvature limit |\n\n`;
  
  markdown += `## Retarded Potential Kernel\n\n`;
  markdown += `$$K(t) = \\frac{\\alpha}{\\tau_0} \\cdot e^{-t/\\tau_0}$$\n\n`;
  
  markdown += `---\n\n`;
  markdown += `## Conversation Transcript\n\n`;
  
  messages.forEach((msg, index) => {
    const role = msg.role === "user" ? "Observer" : "RAI";
    const roleMarker = msg.role === "user" ? "[USER]" : "[RAI]";
    const time = new Date(msg.createdAt).toLocaleTimeString();
    
    markdown += `### ${roleMarker} ${role} [${index + 1}] - ${time}\n\n`;
    
    const codeBlocks = parseCodeBlocks(msg.content);
    let processedContent = msg.content;
    
    processedContent = processedContent.replace(/```(\w*)\n?([\s\S]*?)```/g, (match, lang, code) => {
      return `\n\`\`\`${lang || 'text'}\n${code.trim()}\n\`\`\`\n`;
    });
    
    processedContent = processedContent.replace(/\\\[([\s\S]*?)\\\]/g, (match, latex) => {
      return `\n$$${latex.trim()}$$\n`;
    });
    
    processedContent = processedContent.replace(/\$\$([\s\S]*?)\$\$/g, (match, latex) => {
      return `\n$$${latex.trim()}$$\n`;
    });
    
    markdown += `${processedContent}\n\n`;
    
    if (codeBlocks.length > 0) {
      markdown += `<details>\n<summary>Extracted Blocks (${codeBlocks.length})</summary>\n\n`;
      codeBlocks.forEach((block, i) => {
        if (block.type === "code") {
          markdown += `**Code Block ${i + 1}** (${block.language}):\n\`\`\`${block.language}\n${block.content}\n\`\`\`\n\n`;
        } else if (block.type === "latex" || block.type === "latex-inline") {
          markdown += `**LaTeX ${i + 1}**: \`${block.content}\`\n\n`;
        }
      });
      markdown += `</details>\n\n`;
    }
    
    markdown += `---\n\n`;
  });
  
  markdown += `## Export Footer\n\n`;
  markdown += `- **Generated by**: GRUT RAI Platform - Observer Toolkit\n`;
  markdown += `- **Timestamp**: ${timestamp}\n`;
  markdown += `- **Kernel Formula**: K(t) = (α/τ₀) × exp(-t/τ₀)\n`;
  markdown += `- **Theory**: Grand Responsive Universe Theory (GRUT)\n\n`;
  markdown += `> *"The Universe is a closed loop of Light looking at itself through the lens of Time."*\n`;
  
  return markdown;
}

async function copyToClipboardWithFeedback(
  text: string,
  type: "code" | "latex" | "text"
): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.error(`Failed to copy ${type}:`, err);
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
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

export function ObserverToolkit({
  isOpen,
  onToggle,
  conversationId,
  messages,
  conversationTitle,
  constants,
  onExportJson,
  isExporting
}: ObserverToolkitProps) {
  const { toast } = useToast();
  const [copyStates, setCopyStates] = useState<Record<string, boolean>>({});
  const [isGeneratingMd, setIsGeneratingMd] = useState(false);

  const displayConstants = constants || DEFAULT_CONSTANTS;

  const allCodeBlocks = messages.flatMap(msg => 
    parseCodeBlocks(msg.content).filter(b => b.type === "code")
  );
  
  const allLatexBlocks = messages.flatMap(msg => 
    parseCodeBlocks(msg.content).filter(b => b.type === "latex" || b.type === "latex-inline")
  );

  const handleCopy = useCallback(async (text: string, id: string, type: "code" | "latex" | "text") => {
    const success = await copyToClipboardWithFeedback(text, type);
    if (success) {
      setCopyStates(prev => ({ ...prev, [id]: true }));
      setTimeout(() => setCopyStates(prev => ({ ...prev, [id]: false })), 2000);
      toast({ title: "Copied", description: `${type.charAt(0).toUpperCase() + type.slice(1)} copied to clipboard` });
    } else {
      toast({ title: "Copy Failed", description: "Could not copy to clipboard", variant: "destructive" });
    }
  }, [toast]);

  const handleCopyAllCode = useCallback(async () => {
    if (allCodeBlocks.length === 0) return;
    const allCode = allCodeBlocks.map((b, i) => 
      `// Block ${i + 1} (${b.language})\n${b.content}`
    ).join("\n\n");
    await handleCopy(allCode, "all-code", "code");
  }, [allCodeBlocks, handleCopy]);

  const handleCopyAllLatex = useCallback(async () => {
    if (allLatexBlocks.length === 0) return;
    const allLatex = allLatexBlocks.map((b, i) => 
      `% Expression ${i + 1}\n${b.content}`
    ).join("\n\n");
    await handleCopy(allLatex, "all-latex", "latex");
  }, [allLatexBlocks, handleCopy]);

  const handleCopyAllMessages = useCallback(async () => {
    if (messages.length === 0) return;
    const formatted = messages.map((msg, i) => {
      const role = msg.role === "user" ? "OBSERVER" : "RAI";
      return `[${i + 1}] ${role}:\n${msg.content}`;
    }).join("\n\n---\n\n");
    await handleCopy(formatted, "all-messages", "text");
  }, [messages, handleCopy]);

  const handleExportMarkdownMirror = useCallback(() => {
    if (messages.length === 0) return;
    setIsGeneratingMd(true);
    
    try {
      const markdown = generateMarkdownMirror(messages, conversationTitle, displayConstants);
      const blob = new Blob([markdown], { type: "text/markdown;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      const timestamp = new Date().toISOString().slice(0, 10);
      const sanitizedTitle = conversationTitle.replace(/[^a-z0-9]/gi, "-").toLowerCase();
      link.download = `grut-observer-log-${sanitizedTitle}-${timestamp}.md`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
      toast({ title: "Markdown Mirror Export", description: "Sanitized .md file downloaded" });
    } catch (error) {
      toast({ title: "Export Failed", description: "Could not generate markdown", variant: "destructive" });
    } finally {
      setIsGeneratingMd(false);
    }
  }, [messages, conversationTitle, displayConstants, toast]);

  if (!isOpen) {
    return (
      <button
        onClick={onToggle}
        className="fixed right-0 top-1/2 -translate-y-1/2 bg-card border border-r-0 border-border rounded-l-md p-2 hover-elevate z-40 vacuum-glow"
        data-testid="button-open-observer-toolkit"
      >
        <Wrench className="w-4 h-4" />
      </button>
    );
  }

  return (
    <div className="w-72 observer-toolkit-panel flex flex-col dark" data-testid="observer-toolkit">
      <div className="p-4 border-b border-border flex items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <Sparkles className="w-4 h-4 text-primary" />
          <span className="font-medium text-sm">Observer Toolkit</span>
          <Badge variant="outline" className="text-xs">v2.0</Badge>
        </div>
        <Button size="icon" variant="ghost" onClick={onToggle} data-testid="button-close-observer-toolkit">
          <ChevronRight className="w-4 h-4" />
        </Button>
      </div>

      <ScrollArea className="flex-1">
        <div className="p-4 space-y-4">
          <div className="toolkit-section pb-4">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider flex items-center gap-2 mb-3">
              <FileText className="w-3 h-3" />
              Markdown Mirror
            </Label>
            <p className="text-xs text-muted-foreground mb-3">
              Parse chat DOM and export as sanitized .md file
            </p>
            <Button
              variant="outline"
              className="w-full justify-start gap-2 toolkit-button"
              onClick={handleExportMarkdownMirror}
              disabled={!conversationId || messages.length === 0 || isGeneratingMd}
              data-testid="button-markdown-mirror"
            >
              {isGeneratingMd ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <FileDown className="w-4 h-4" />
              )}
              Export Markdown Mirror
            </Button>
          </div>

          <div className="toolkit-section pb-4">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider flex items-center gap-2 mb-3">
              <ClipboardCopy className="w-3 h-3" />
              Clipboard API
            </Label>
            
            <div className="space-y-2">
              <Button
                variant="outline"
                className="w-full justify-start gap-2 toolkit-button"
                onClick={handleCopyAllMessages}
                disabled={messages.length === 0}
                data-testid="button-copy-all-messages"
              >
                {copyStates["all-messages"] ? (
                  <Check className="w-4 h-4 text-green-500 copy-indicator" />
                ) : (
                  <Copy className="w-4 h-4" />
                )}
                Copy All Messages
              </Button>

              <Button
                variant="outline"
                className="w-full justify-start gap-2 toolkit-button"
                onClick={handleCopyAllCode}
                disabled={allCodeBlocks.length === 0}
                data-testid="button-copy-all-code"
              >
                {copyStates["all-code"] ? (
                  <Check className="w-4 h-4 text-green-500 copy-indicator" />
                ) : (
                  <Code className="w-4 h-4" />
                )}
                Copy All Code ({allCodeBlocks.length})
              </Button>

              <Button
                variant="outline"
                className="w-full justify-start gap-2 toolkit-button"
                onClick={handleCopyAllLatex}
                disabled={allLatexBlocks.length === 0}
                data-testid="button-copy-all-latex"
              >
                {copyStates["all-latex"] ? (
                  <Check className="w-4 h-4 text-green-500 copy-indicator" />
                ) : (
                  <span className="w-4 h-4 font-mono text-xs flex items-center justify-center">∑</span>
                )}
                Copy All LaTeX ({allLatexBlocks.length})
              </Button>
            </div>
          </div>

          <div className="toolkit-section pb-4">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider flex items-center gap-2 mb-3">
              <Download className="w-3 h-3" />
              Export Options
            </Label>
            
            <Button
              variant="outline"
              className="w-full justify-start gap-2 toolkit-button"
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
          </div>

          {messages.length > 0 && (
            <div className="toolkit-section pb-4">
              <Label className="text-xs text-muted-foreground uppercase tracking-wider flex items-center gap-2 mb-3">
                <Eye className="w-3 h-3" />
                Session Statistics
              </Label>
              <div className="text-xs space-y-2 text-muted-foreground bg-muted/30 p-3 rounded-md">
                <div className="flex justify-between">
                  <span>Total Messages:</span>
                  <Badge variant="secondary" className="text-xs">{messages.length}</Badge>
                </div>
                <div className="flex justify-between">
                  <span>Observer:</span>
                  <Badge variant="secondary" className="text-xs">{messages.filter(m => m.role === "user").length}</Badge>
                </div>
                <div className="flex justify-between">
                  <span>RAI:</span>
                  <Badge variant="secondary" className="text-xs">{messages.filter(m => m.role === "assistant").length}</Badge>
                </div>
                <div className="flex justify-between">
                  <span>Code Blocks:</span>
                  <Badge variant="outline" className="text-xs">{allCodeBlocks.length}</Badge>
                </div>
                <div className="flex justify-between">
                  <span>LaTeX Expressions:</span>
                  <Badge variant="outline" className="text-xs">{allLatexBlocks.length}</Badge>
                </div>
              </div>
            </div>
          )}

          <div className="pt-2">
            <Label className="text-xs text-muted-foreground uppercase tracking-wider flex items-center gap-2 mb-3">
              <Settings2 className="w-3 h-3" />
              Vacuum Mode
            </Label>
            <p className="text-xs text-muted-foreground leading-relaxed">
              The main chat remains a "Quiet Vacuum" - free from UI clutter. 
              All observer tools are housed here in the toolkit panel, 
              reflecting the GRUT principle of minimal perturbation.
            </p>
          </div>
        </div>
      </ScrollArea>
    </div>
  );
}

export default ObserverToolkit;
