import { useState, useRef, useEffect } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { useLocation } from "wouter";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Card } from "@/components/ui/card";
import { apiRequest, queryClient } from "@/lib/queryClient";
import { ArrowLeft, Send, Loader2, MessageSquare, Trash2, Plus, Sparkles } from "lucide-react";
import type { ChatConversation, ChatMessage } from "@shared/schema";

export default function ChatPage() {
  const [, setLocation] = useLocation();
  const [activeConversationId, setActiveConversationId] = useState<string | null>(null);
  const [inputValue, setInputValue] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const conversationsQuery = useQuery<ChatConversation[]>({
    queryKey: ["/api/chat"],
  });

  const activeConversationQuery = useQuery<ChatConversation>({
    queryKey: ["/api/chat", activeConversationId],
    enabled: !!activeConversationId,
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
    mutationFn: async ({ conversationId, content }: { conversationId: string; content: string }) => {
      const response = await apiRequest("POST", `/api/chat/${conversationId}/message`, { content });
      return await response.json() as { userMessage: ChatMessage; assistantMessage: ChatMessage };
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["/api/chat", activeConversationId] });
      setInputValue("");
    },
  });

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [activeConversationQuery.data?.messages]);

  const handleSendMessage = () => {
    if (!inputValue.trim() || !activeConversationId || sendMessageMutation.isPending) return;
    sendMessageMutation.mutate({ conversationId: activeConversationId, content: inputValue.trim() });
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

  return (
    <div className="flex h-screen bg-background" data-testid="chat-page">
      <div className="w-64 border-r border-border bg-card flex flex-col">
        <div className="p-4 border-b border-border">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setLocation("/")}
            className="mb-3 w-full justify-start"
            data-testid="button-back-home"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Back to Home
          </Button>
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
                  }`}
                  onClick={() => setActiveConversationId(conv.id)}
                  data-testid={`conversation-item-${conv.id}`}
                >
                  <MessageSquare className="w-4 h-4 text-muted-foreground flex-shrink-0" />
                  <span className="text-sm truncate flex-1">{conv.title}</span>
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

      <div className="flex-1 flex flex-col">
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
            <div className="border-b border-border p-4 flex items-center gap-3">
              <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
                <Sparkles className="w-4 h-4 text-primary" />
              </div>
              <div>
                <h3 className="font-medium">RAI Assistant</h3>
                <p className="text-xs text-muted-foreground">GRUT Theory Expert</p>
              </div>
            </div>

            <ScrollArea className="flex-1 p-4">
              <div className="space-y-4 max-w-3xl mx-auto">
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
                  activeConversationQuery.data?.messages.map((message) => (
                    <div
                      key={message.id}
                      className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
                      data-testid={`message-${message.id}`}
                    >
                      <Card
                        className={`max-w-[80%] p-3 ${
                          message.role === "user"
                            ? "bg-primary text-primary-foreground"
                            : "bg-muted"
                        }`}
                      >
                        <p className="text-sm whitespace-pre-wrap">{message.content}</p>
                      </Card>
                    </div>
                  ))
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
                <Input
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="Ask about GRUT theory..."
                  disabled={sendMessageMutation.isPending}
                  data-testid="input-message"
                />
                <Button
                  onClick={handleSendMessage}
                  disabled={!inputValue.trim() || sendMessageMutation.isPending}
                  data-testid="button-send-message"
                >
                  {sendMessageMutation.isPending ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Send className="w-4 h-4" />
                  )}
                </Button>
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
