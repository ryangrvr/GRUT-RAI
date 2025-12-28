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
  LogOut, Upload, CheckCircle2, Paperclip, User, Lock
} from "lucide-react";
import type { ChatConversation, ChatMessage, ChatFileUpload } from "@shared/schema";
import { useToast } from "@/hooks/use-toast";

interface AuthUser {
  id: string;
  username: string;
}

function LoginForm({ onSuccess }: { onSuccess: (user: AuthUser) => void }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isRegistering, setIsRegistering] = useState(false);
  const { toast } = useToast();

  const loginMutation = useMutation({
    mutationFn: async ({ username, password }: { username: string; password: string }) => {
      const response = await apiRequest("POST", "/api/auth/login", { username, password });
      return await response.json();
    },
    onSuccess: (data) => {
      onSuccess(data.user);
      toast({ title: "Welcome back!", description: `Logged in as ${data.user.username}` });
    },
    onError: (error: Error) => {
      toast({ title: "Login failed", description: error.message, variant: "destructive" });
    },
  });

  const registerMutation = useMutation({
    mutationFn: async ({ username, password }: { username: string; password: string }) => {
      const response = await apiRequest("POST", "/api/auth/register", { username, password });
      return await response.json();
    },
    onSuccess: (data) => {
      onSuccess(data.user);
      toast({ title: "Welcome!", description: `Account created for ${data.user.username}` });
    },
    onError: (error: Error) => {
      toast({ title: "Registration failed", description: error.message, variant: "destructive" });
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (isRegistering) {
      registerMutation.mutate({ username, password });
    } else {
      loginMutation.mutate({ username, password });
    }
  };

  const isPending = loginMutation.isPending || registerMutation.isPending;

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-background p-4">
      <Card className="w-full max-w-md p-6 space-y-6">
        <div className="text-center">
          <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
            <Sparkles className="w-8 h-8 text-primary" />
          </div>
          <h1 className="text-2xl font-bold">GRUT RAI Chat</h1>
          <p className="text-muted-foreground mt-2">
            {isRegistering ? "Create an account to continue" : "Sign in to access the chat"}
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="username">Username</Label>
            <div className="relative">
              <User className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <Input
                id="username"
                type="text"
                placeholder="Enter username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="pl-10"
                required
                data-testid="input-username"
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="password">Password</Label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <Input
                id="password"
                type="password"
                placeholder="Enter password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="pl-10"
                required
                data-testid="input-password"
              />
            </div>
          </div>

          <Button type="submit" className="w-full" disabled={isPending} data-testid="button-login">
            {isPending ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                {isRegistering ? "Creating account..." : "Signing in..."}
              </>
            ) : (
              isRegistering ? "Create Account" : "Sign In"
            )}
          </Button>
        </form>

        <div className="text-center space-y-3">
          <Button
            variant="ghost"
            onClick={() => setIsRegistering(!isRegistering)}
            className="text-sm"
            data-testid="button-toggle-auth-mode"
          >
            {isRegistering ? "Already have an account? Sign in" : "Need an account? Register"}
          </Button>

          <div className="bg-muted/50 rounded-md p-3 text-sm">
            <p className="font-medium mb-1">Demo Credentials:</p>
            <p className="text-muted-foreground">Username: <code className="bg-muted px-1 rounded">demo</code></p>
            <p className="text-muted-foreground">Password: <code className="bg-muted px-1 rounded">grut2025</code></p>
          </div>
        </div>
      </Card>
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
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const { toast } = useToast();

  useEffect(() => {
    fetch("/api/auth/me", { credentials: "include" })
      .then((res) => {
        if (res.ok) return res.json();
        throw new Error("Not authenticated");
      })
      .then((data) => setUser(data.user))
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
    mutationFn: async ({ conversationId, content }: { conversationId: string; content: string }) => {
      const response = await apiRequest("POST", `/api/chat/${conversationId}/message`, { content });
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
      <div className="w-64 border-r border-border bg-card flex flex-col">
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
            <span>{user.username}</span>
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
            <div className="border-b border-border p-4 flex items-center justify-between gap-3">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
                  <Sparkles className="w-4 h-4 text-primary" />
                </div>
                <div>
                  <h3 className="font-medium">RAI Assistant</h3>
                  <p className="text-xs text-muted-foreground">GRUT Theory Expert</p>
                </div>
              </div>
              <div className="flex items-center gap-2 text-xs text-muted-foreground">
                <CheckCircle2 className="w-3 h-3 text-green-500" />
                <span data-testid="text-save-status">Auto-saved</span>
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
    </div>
  );
}
