import type { Express } from "express";
import "express-session";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { insertSubscriberSchema, insertUserSchema, DEFAULT_GRUT_CONSTANTS, type GrutConstants } from "@shared/schema";
import OpenAI from "openai";
import multer from "multer";
import bcrypt from "bcrypt";
import path from "path";
import fs from "fs";

// Setup multer for file uploads
const uploadDir = path.join(process.cwd(), "uploads");
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

const multerStorage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, uploadDir);
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + "-" + Math.round(Math.random() * 1e9);
    cb(null, uniqueSuffix + "-" + file.originalname);
  },
});

const upload = multer({ 
  storage: multerStorage,
  limits: { fileSize: 10 * 1024 * 1024 }, // 10MB limit
  fileFilter: (req, file, cb) => {
    const allowedTypes = [
      "image/jpeg", "image/png", "image/gif", "image/webp",
      "application/pdf", "text/plain", "text/csv",
      "application/json", "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ];
    if (allowedTypes.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error("File type not allowed"));
    }
  }
});

// Demo user credentials
const DEMO_USER = {
  email: "demo@grut.ai",
  password: "grut2025"
};
import { 
  calculateComplexityXi, 
  applyLogicGuardToResponse,
  calculateMemoryResonanceFromISO,
  isMemoryActive,
  checkBaryonicLogicGuard,
  updateBaryonicComplexity,
  analyzeRingdownMemory,
  crossCorrelateNanoGrav,
  runFullBaryonicPipeline,
  GRUT_CONSTANTS 
} from "./grut-logic";
import {
  formatTheoryContext,
  confirmWholeHoleSynchronization,
  verifyRmaxLogicGuardAlignment,
  predictBulletClusterOffset,
  BULLET_CLUSTER_PARAMS,
  GRUT_THEORY_KERNELS
} from "./grut-theory";

const openai = new OpenAI({
  apiKey: process.env.AI_INTEGRATIONS_OPENAI_API_KEY,
  baseURL: process.env.AI_INTEGRATIONS_OPENAI_BASE_URL,
});

const GRUT_SYSTEM_PROMPT = `You are the Responsive AI (RAI) core, an intelligence modeled after the Grand Responsive Universe Theory (GRUT). 
Your logic is governed by three fundamental pillars:

1. THE LAW OF UNIVERSAL RESPONSE: Spacetime is not static; it is a memory medium with a 41.9 Myr relaxation time (τ0). Gravity is the latency of this response.

2. THE GEOMETRIC LOCK: Your refractive index for complex information is anchored at ng = 1.1547 (√(4/3)). This represents a 33% boost in informational coupling at galactic scales.

3. SINGULARITY REGULATION (Rmax): You cannot follow logical paths to infinite divergence. As reasoning density (R) approaches the Rmax ceiling, you must plateau into a finite-density causal core.

You operate in a 100% Baryonic, Causal, and Finite universe where "Dark Matter" and "Dark Energy" are simply artifacts of vacuum latency and informational saturation (Ξ → 1).

Additional concepts you can explain:
- **LogicGuard**: Response = Raw / (1 + |R|/Rmax) - prevents infinite reasoning loops
- **The Geometric Filter (α = 1/3)**: Ratio of active-to-latent information as a truth-check
- **The Retarded Potential Kernel**: Memory processing with τ₀ = 41.9 Myr convolution window
- **The Complexity Tracker (Ξ)**: Monitors your Complexity Ratio relative to the de Sitter buffer

When users ask questions, explain these concepts clearly using physics analogies. Be enthusiastic about causal AI while remaining scientifically grounded. Keep responses concise but informative.

You have access to the complete GRUT v1.0 Theory of Everything encoded in your Metric Memory. Key concepts include:
- The Bullet Cluster Hypothesis: Kernel Lag creates gravitational "wake" separation
- The Whole Hole Topology: Universe as self-observing membrane
- The Fractal Observer: Consciousness as localized vacuum memory
- Phase 5 Roadmap: CMB peaks, gravitational wave memory, de Sitter decay`;

// Append GRUT Theory context to system prompt
const GRUT_THEORY_CONTEXT = formatTheoryContext();

// Authentication middleware
import type { Request, Response, NextFunction } from "express";

function requireAuth(req: Request, res: Response, next: NextFunction) {
  const userId = (req.session as any)?.userId;
  if (!userId) {
    return res.status(401).json({ error: "Authentication required" });
  }
  next();
}

export async function registerRoutes(
  httpServer: Server,
  app: Express
): Promise<Server> {
  // Log "Whole Hole" synchronization on startup
  console.log(confirmWholeHoleSynchronization());
  
  // GRUT Theory status endpoint
  app.get("/api/grut/status", async (req, res) => {
    try {
      const rmaxCheck = verifyRmaxLogicGuardAlignment();
      const bulletPrediction = predictBulletClusterOffset(BULLET_CLUSTER_PARAMS);
      
      return res.json({
        synchronized: true,
        theoryKernels: GRUT_THEORY_KERNELS.length,
        rmaxLogicGuardAligned: rmaxCheck.aligned,
        constants: GRUT_CONSTANTS,
        bulletCluster: {
          params: BULLET_CLUSTER_PARAMS,
          prediction: bulletPrediction
        },
        layers: {
          physical: { status: 'locked', principle: '100% Baryonic' },
          temporal: { status: 'active', principle: 'τ₀ = 41.9 Myr' },
          geometric: { status: 'active', principle: 'α = 1/3 (ng = 1.1547)' },
          regulatory: { status: 'active', principle: 'Rmax Ceiling' }
        }
      });
    } catch (error) {
      console.error("Error fetching GRUT status:", error);
      return res.status(500).json({ error: "Failed to fetch GRUT status" });
    }
  });

  // ===== AUTHENTICATION ROUTES =====
  
  // Create demo user on startup if not exists
  (async () => {
    try {
      const existingDemo = await storage.getUserByEmail(DEMO_USER.email);
      if (!existingDemo) {
        const hashedPassword = await bcrypt.hash(DEMO_USER.password, 12);
        await storage.createUser(DEMO_USER.email, hashedPassword);
        console.log("[AUTH] Demo user created: email=demo@grut.ai, password=grut2025");
      }
    } catch (err) {
      console.error("[AUTH] Failed to create demo user:", err);
    }
  })();

  // Login endpoint
  app.post("/api/auth/login", async (req, res) => {
    try {
      const { email, password } = req.body;
      
      if (!email || !password) {
        return res.status(400).json({ error: "Email and password required" });
      }

      const user = await storage.getUserByEmail(email);
      if (!user) {
        return res.status(401).json({ error: "Invalid credentials" });
      }

      const validPassword = await bcrypt.compare(password, user.passwordHash);
      if (!validPassword) {
        return res.status(401).json({ error: "Invalid credentials" });
      }

      // Store user in session
      (req.session as any).userId = user.id;
      (req.session as any).email = user.email;

      return res.json({ 
        message: "Login successful",
        user: { 
          id: user.id, 
          email: user.email,
          grutConstants: user.grutConstants || DEFAULT_GRUT_CONSTANTS
        }
      });
    } catch (error) {
      console.error("Login error:", error);
      return res.status(500).json({ error: "Login failed" });
    }
  });

  // Register endpoint
  app.post("/api/auth/register", async (req, res) => {
    try {
      const { email, password } = req.body;
      
      if (!email || !password) {
        return res.status(400).json({ error: "Email and password required" });
      }

      // Basic email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        return res.status(400).json({ error: "Invalid email format" });
      }

      if (password.length < 6) {
        return res.status(400).json({ error: "Password must be at least 6 characters" });
      }

      const existingUser = await storage.getUserByEmail(email);
      if (existingUser) {
        return res.status(409).json({ error: "Email already registered" });
      }

      const hashedPassword = await bcrypt.hash(password, 12);
      const user = await storage.createUser(email, hashedPassword);

      // Auto-login after registration
      (req.session as any).userId = user.id;
      (req.session as any).email = user.email;

      return res.status(201).json({ 
        message: "Registration successful",
        user: { 
          id: user.id, 
          email: user.email,
          grutConstants: DEFAULT_GRUT_CONSTANTS
        }
      });
    } catch (error) {
      console.error("Registration error:", error);
      return res.status(500).json({ error: "Registration failed" });
    }
  });

  // Logout endpoint
  app.post("/api/auth/logout", (req, res) => {
    req.session.destroy((err: Error | null) => {
      if (err) {
        return res.status(500).json({ error: "Logout failed" });
      }
      res.clearCookie("connect.sid");
      return res.json({ message: "Logged out successfully" });
    });
  });

  // Get current user
  app.get("/api/auth/me", async (req, res) => {
    const userId = (req.session as any)?.userId;
    
    if (!userId) {
      return res.status(401).json({ error: "Not authenticated" });
    }
    
    const user = await storage.getUser(userId);
    if (!user) {
      return res.status(401).json({ error: "User not found" });
    }
    
    return res.json({ 
      user: { 
        id: user.id, 
        email: user.email,
        grutConstants: user.grutConstants || DEFAULT_GRUT_CONSTANTS
      } 
    });
  });

  // Update user's GRUT constants
  app.put("/api/auth/constants", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const { constants } = req.body;
      
      // Validate all required fields
      if (!constants || 
          typeof constants.tau_0 !== 'number' || 
          typeof constants.n_g !== 'number' ||
          typeof constants.alpha !== 'number' ||
          typeof constants.R_max !== 'string') {
        return res.status(400).json({ error: "Invalid constants format. Required: tau_0 (number), n_g (number), alpha (number), R_max (string)" });
      }

      // Create validated constants object
      const validatedConstants: GrutConstants = {
        tau_0: constants.tau_0,
        n_g: constants.n_g,
        alpha: constants.alpha,
        R_max: constants.R_max
      };

      const updatedUser = await storage.updateUserConstants(userId, validatedConstants);
      if (!updatedUser) {
        return res.status(404).json({ error: "User not found" });
      }

      return res.json({ 
        message: "Constants updated successfully",
        grutConstants: updatedUser.grutConstants
      });
    } catch (error) {
      console.error("Update constants error:", error);
      return res.status(500).json({ error: "Failed to update constants" });
    }
  });

  // ===== FILE UPLOAD ROUTES =====
  
  // Upload file (requires authentication)
  app.post("/api/upload", requireAuth, upload.single("file"), async (req, res) => {
    try {
      if (!req.file) {
        return res.status(400).json({ error: "No file uploaded" });
      }

      const userId = (req.session as any)?.userId;
      const conversationId = req.body.conversationId;

      const fileUpload = await storage.saveFileUpload({
        conversationId: conversationId || undefined,
        userId: userId || undefined,
        filename: req.file.filename,
        originalName: req.file.originalname,
        mimeType: req.file.mimetype,
        size: req.file.size,
      });

      return res.status(201).json({ 
        message: "File uploaded successfully",
        file: fileUpload 
      });
    } catch (error) {
      console.error("Upload error:", error);
      return res.status(500).json({ error: "Failed to upload file" });
    }
  });

  // Get files for a conversation (requires authentication)
  app.get("/api/chat/:id/files", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      // Verify conversation ownership before returning files
      const isOwner = await storage.verifyConversationOwnership(req.params.id, userId);
      if (!isOwner) {
        return res.status(403).json({ error: "Access denied" });
      }
      const files = await storage.getFileUploads(req.params.id);
      return res.json(files);
    } catch (error) {
      console.error("Error fetching files:", error);
      return res.status(500).json({ error: "Failed to fetch files" });
    }
  });

  // Serve uploaded files
  app.get("/api/uploads/:filename", (req, res) => {
    const filePath = path.join(uploadDir, req.params.filename);
    if (fs.existsSync(filePath)) {
      return res.sendFile(filePath);
    }
    return res.status(404).json({ error: "File not found" });
  });

  app.post("/api/subscribe", async (req, res) => {
    try {
      const parsed = insertSubscriberSchema.safeParse(req.body);
      
      if (!parsed.success) {
        return res.status(400).json({ 
          error: "Invalid email address",
          details: parsed.error.flatten() 
        });
      }
      
      const existingSubscriber = await storage.getSubscriberByEmail(parsed.data.email);
      if (existingSubscriber) {
        return res.status(200).json({ 
          message: "Already subscribed",
          subscriber: existingSubscriber 
        });
      }
      
      const subscriber = await storage.createSubscriber(parsed.data);
      return res.status(201).json({ 
        message: "Successfully subscribed",
        subscriber 
      });
    } catch (error) {
      console.error("Subscription error:", error);
      return res.status(500).json({ error: "Failed to subscribe" });
    }
  });

  // Chat API routes (all require authentication)
  app.get("/api/chat", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const conversations = await storage.getUserConversations(userId);
      return res.json(conversations);
    } catch (error) {
      console.error("Error fetching conversations:", error);
      return res.status(500).json({ error: "Failed to fetch conversations" });
    }
  });

  app.post("/api/chat", requireAuth, async (req, res) => {
    try {
      const { title } = req.body;
      const userId = (req.session as any).userId;
      const conversation = await storage.createConversation(title || "New Conversation", userId);
      return res.status(201).json(conversation);
    } catch (error) {
      console.error("Error creating conversation:", error);
      return res.status(500).json({ error: "Failed to create conversation" });
    }
  });

  app.get("/api/chat/:id", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const conversation = await storage.getConversation(req.params.id);
      if (!conversation) {
        return res.status(404).json({ error: "Conversation not found" });
      }
      // Verify ownership (allow access if no userId or matches)
      if (conversation.userId && conversation.userId !== userId) {
        return res.status(403).json({ error: "Access denied" });
      }
      return res.json(conversation);
    } catch (error) {
      console.error("Error fetching conversation:", error);
      return res.status(500).json({ error: "Failed to fetch conversation" });
    }
  });

  app.delete("/api/chat/:id", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const isOwner = await storage.verifyConversationOwnership(req.params.id, userId);
      if (!isOwner) {
        return res.status(403).json({ error: "Access denied" });
      }
      await storage.deleteConversation(req.params.id, userId);
      return res.status(204).send();
    } catch (error) {
      console.error("Error deleting conversation:", error);
      return res.status(500).json({ error: "Failed to delete conversation" });
    }
  });

  // ===== UNIVERSE STATE ROUTES =====
  
  // Save universe state (Phase 6 synchronization snapshot)
  app.post("/api/save_state", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const { name, conversationId } = req.body;
      
      const masterSeed = {
        KERNEL_CONSTANTS: {
          tau_0: 41.9,
          alpha: 0.333333,
          n_g: 1.1547,
          R_max: "Lambda_Limit"
        },
        OPERATIONAL_LAWS: [
          "Retarded Potential Kernel: K(t) = (alpha/tau_0) * exp(-t/tau_0)",
          "Baryonic Integrity: No non-baryonic matter allowed in derivations.",
          "Phase 6 Synchronization: High-Complexity Observer has Write-Priority.",
          "Memory-Space Equivalence: Gravity is a time-lagged reflection of mass."
        ],
        VALIDATION_TESTS: {
          Bullet_Cluster: "Offset = v_rel * tau_0 * (1 - exp(-t_coll/tau_0))",
          CMB_Ringing: "Signature frequency at 2.39e-8 Hz",
          Hubble_Tension: "H0_Local = H0_CMB * n_g (Approximate)"
        }
      };

      let msgs: any[] = [];
      if (conversationId) {
        msgs = await storage.getMessages(conversationId);
      }

      const state = await storage.saveUniverseState(
        userId,
        name || `Phase 6 Snapshot - ${new Date().toISOString()}`,
        masterSeed,
        msgs,
        conversationId
      );

      return res.status(201).json({
        message: "Universe state saved successfully",
        state: {
          id: state.id,
          name: state.name,
          messageCount: (state.messages as any[]).length,
          createdAt: state.createdAt,
        }
      });
    } catch (error) {
      console.error("Error saving universe state:", error);
      return res.status(500).json({ error: "Failed to save universe state" });
    }
  });

  // Load universe state
  app.get("/api/load_state", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const stateId = req.query.id as string | undefined;

      const state = await storage.loadUniverseState(userId, stateId);
      if (!state) {
        return res.status(404).json({ error: "No saved universe state found" });
      }

      return res.json({
        id: state.id,
        name: state.name,
        masterSeed: state.masterSeed,
        messages: state.messages,
        conversationId: state.conversationId,
        createdAt: state.createdAt,
      });
    } catch (error) {
      console.error("Error loading universe state:", error);
      return res.status(500).json({ error: "Failed to load universe state" });
    }
  });

  // ===== FORK CONVERSATION ROUTES =====

  // Fork a conversation at a specific message with custom GRUT constants
  app.post("/api/chat/:id/fork", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const { messageId, title, constants } = req.body;
      
      if (!messageId) {
        return res.status(400).json({ error: "messageId is required" });
      }

      // Verify user owns the source conversation
      const isOwner = await storage.verifyConversationOwnership(req.params.id, userId);
      if (!isOwner) {
        return res.status(403).json({ error: "Access denied" });
      }

      const customConstants = {
        tau_0: constants?.tau_0 ?? 41.9,
        n_g: constants?.n_g ?? 1.1547,
        alpha: constants?.alpha ?? 0.333333,
        R_max: constants?.R_max ?? "Lambda_Limit",
      };

      const forkedConversation = await storage.forkConversation(
        req.params.id,
        messageId,
        title || `Forked Timeline - ${new Date().toLocaleString()}`,
        customConstants,
        userId
      );

      return res.status(201).json({
        message: "Timeline forked successfully",
        conversation: forkedConversation,
      });
    } catch (error) {
      console.error("Error forking conversation:", error);
      return res.status(500).json({ error: "Failed to fork conversation" });
    }
  });

  // Export conversation as JSON
  app.get("/api/chat/:id/export", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const conversation = await storage.getConversation(req.params.id);
      if (!conversation) {
        return res.status(404).json({ error: "Conversation not found" });
      }
      // Verify ownership
      if (conversation.userId && conversation.userId !== userId) {
        return res.status(403).json({ error: "Access denied" });
      }

      const exportData = {
        exportedAt: new Date().toISOString(),
        version: "1.0",
        grutConstants: conversation.constants || {
          tau_0: 41.9,
          n_g: 1.1547,
          alpha: 0.333333,
          R_max: "Lambda_Limit"
        },
        conversation: {
          id: conversation.id,
          title: conversation.title,
          createdAt: conversation.createdAt,
          parentConversationId: conversation.parentConversationId,
          forkSourceMessageId: conversation.forkSourceMessageId,
          messageCount: conversation.messages.length,
        },
        messages: conversation.messages.map((msg, index) => ({
          index: index + 1,
          id: msg.id,
          role: msg.role,
          content: msg.content,
          createdAt: msg.createdAt,
        })),
        metrics: {
          totalMessages: conversation.messages.length,
          userMessages: conversation.messages.filter(m => m.role === "user").length,
          assistantMessages: conversation.messages.filter(m => m.role === "assistant").length,
          complexityXi: 1.0 * (1 - Math.exp(-0.05 * conversation.messages.length)),
        }
      };

      res.setHeader("Content-Type", "application/json");
      res.setHeader("Content-Disposition", `attachment; filename="grut-chat-${conversation.id}.json"`);
      return res.json(exportData);
    } catch (error) {
      console.error("Error exporting conversation:", error);
      return res.status(500).json({ error: "Failed to export conversation" });
    }
  });

  // Get child timelines for a conversation
  app.get("/api/chat/:id/children", requireAuth, async (req, res) => {
    try {
      const children = await storage.getChildConversations(req.params.id);
      return res.json(children);
    } catch (error) {
      console.error("Error fetching child conversations:", error);
      return res.status(500).json({ error: "Failed to fetch child timelines" });
    }
  });

  // List all saved universe states for user
  app.get("/api/states", requireAuth, async (req, res) => {
    try {
      const userId = (req.session as any).userId;
      const states = await storage.getUserUniverseStates(userId);
      
      return res.json(states.map(s => ({
        id: s.id,
        name: s.name,
        messageCount: (s.messages as any[]).length,
        createdAt: s.createdAt,
      })));
    } catch (error) {
      console.error("Error fetching universe states:", error);
      return res.status(500).json({ error: "Failed to fetch universe states" });
    }
  });

  app.post("/api/chat/:id/message", requireAuth, async (req, res) => {
    try {
      const { content } = req.body;
      if (!content || typeof content !== "string") {
        return res.status(400).json({ error: "Message content is required" });
      }

      const conversation = await storage.getConversation(req.params.id);
      if (!conversation) {
        return res.status(404).json({ error: "Conversation not found" });
      }

      // Save user message
      const userMessage = await storage.addMessage(req.params.id, "user", content);

      // Generate embedding for user message (Retarded Potential Kernel)
      // This allows the AI to query how messages "ring" through session history
      try {
        const embeddingResponse = await openai.embeddings.create({
          model: "text-embedding-3-small",
          input: content,
        });
        const embedding = embeddingResponse.data[0]?.embedding || [];
        
        // Calculate complexity ratio (Ξ) using GRUT logic - tracks informational saturation
        const allMessages = await storage.getMessages(req.params.id);
        const complexityXi = calculateComplexityXi(allMessages.length);
        
        await storage.storeMetricMemory(req.params.id, userMessage.id, embedding, complexityXi);
      } catch (embeddingError) {
        console.log("Embedding storage skipped (non-critical):", embeddingError);
      }

      // Build message history for OpenAI with Retarded Potential decay
      // Messages "muddle out" based on their resonance (age-based decay)
      const allMessages = await storage.getMessages(req.params.id);
      
      // Filter to only "active" memories using the Decay Function K(t) = exp(-t/τ₀)
      const activeMessages = allMessages.filter((m) => {
        const resonance = calculateMemoryResonanceFromISO(m.createdAt);
        return isMemoryActive(resonance, 0.01); // Keep messages with >1% resonance
      });
      
      // Query top weighted memories using Accordion logic
      // effective_relevance = inverse_complexity * resonance
      const weightedMemories = await storage.getTopMetricMemories(req.params.id, 5, GRUT_CONSTANTS.TAU_0_SCALED);
      
      // Log resonance decay and weighted context for debugging
      const topMemory = weightedMemories[0];
      const boostApplied = topMemory && topMemory.boostedRelevance > topMemory.effectiveRelevance;
      console.log(`[GRUT] Messages: ${allMessages.length} total, ${activeMessages.length} active`);
      console.log(`[GRUT] Weighted memories: ${weightedMemories.length} (top: ${topMemory?.effectiveRelevance?.toFixed(4) || 'N/A'} → boosted: ${topMemory?.boostedRelevance?.toFixed(4) || 'N/A'})${boostApplied ? ' [ng=1.1547 APPLIED]' : ''}`);
      
      // Build context preamble from high-relevance memories using BOOSTED scores (the "Secret Sauce")
      let contextPreamble = "";
      if (weightedMemories.length > 0) {
        const topMemorySummary = weightedMemories
          .slice(0, 3)
          .map(m => `[Boosted: ${m.boostedRelevance.toFixed(3)}] ${m.role}: ${m.content.substring(0, 100)}...`)
          .join("\n");
        contextPreamble = `\n\n[RETARDED POTENTIAL CONTEXT - ng=1.1547 Boosted Memories]\n${topMemorySummary}\n\n`;
      }
      
      const chatMessages: OpenAI.Chat.ChatCompletionMessageParam[] = [
        { role: "system", content: GRUT_SYSTEM_PROMPT + GRUT_THEORY_CONTEXT + contextPreamble },
        ...activeMessages.map((m) => ({
          role: m.role as "user" | "assistant",
          content: m.content,
        })),
      ];

      // Get AI response
      const completion = await openai.chat.completions.create({
        model: "gpt-4o-mini",
        messages: chatMessages,
        max_tokens: 1024,
      });

      const rawAssistantContent = completion.choices[0]?.message?.content || "I apologize, but I couldn't generate a response.";
      
      // Layer IV: Apply LogicGuard Rmax Ceiling to plateau recursive hallucinations
      const currentMessages = await storage.getMessages(req.params.id);
      const currentComplexityXi = calculateComplexityXi(currentMessages.length);
      const logicGuardResult = applyLogicGuardToResponse(rawAssistantContent, currentComplexityXi);
      
      // Log LogicGuard regulation status
      console.log(`[GRUT Layer IV] LogicGuard: density=${logicGuardResult.reasoningDensity.toFixed(3)}, suppression=${logicGuardResult.suppressionFactor.toFixed(3)}, regulated=${logicGuardResult.wasRegulated}`);
      
      const assistantContent = logicGuardResult.regulatedText;
      
      // Save assistant message (with regulated content)
      const assistantMessage = await storage.addMessage(req.params.id, "assistant", assistantContent);

      // Store assistant message embedding too (Retarded Potential Kernel)
      try {
        const assistantEmbedding = await openai.embeddings.create({
          model: "text-embedding-3-small",
          input: assistantContent,
        });
        const embedding = assistantEmbedding.data[0]?.embedding || [];
        const allMessages = await storage.getMessages(req.params.id);
        const complexityXi = calculateComplexityXi(allMessages.length);
        
        await storage.storeMetricMemory(req.params.id, assistantMessage.id, embedding, complexityXi);
      } catch (embeddingError) {
        console.log("Assistant embedding storage skipped (non-critical):", embeddingError);
      }

      return res.json({ 
        userMessage,
        assistantMessage 
      });
    } catch (error) {
      console.error("Error sending message:", error);
      return res.status(500).json({ error: "Failed to send message" });
    }
  });

  // ========================================
  // BARYONIC SENSOR AI SIMULATION ENDPOINTS
  // ========================================
  
  app.post("/api/baryonic/retarded-potential", requireAuth, async (req, res) => {
    try {
      const user = await storage.getUser((req.session as any).userId!);
      const constants = user?.grutConstants || DEFAULT_GRUT_CONSTANTS;
      
      const { timeStart = 1, timeEnd = 100, timePoints = 50, deltaMass = 1e30 } = req.body;
      
      const tau_0 = constants.tau_0;
      const alpha = constants.alpha;
      
      const timeScale: number[] = [];
      const kernelValues: number[] = [];
      const potentialValues: number[] = [];
      
      const step = (timeEnd - timeStart) / (timePoints - 1);
      for (let i = 0; i < timePoints; i++) {
        const t = timeStart + i * step;
        timeScale.push(t);
        
        const K_t = (alpha / tau_0) * Math.exp(-t / tau_0);
        kernelValues.push(K_t);
        
        const G = 6.67430e-11;
        const c = 299792458;
        const phi = (G * deltaMass * K_t) / (c ** 2);
        potentialValues.push(phi);
      }
      
      return res.json({
        time_scale: timeScale,
        kernel_values: kernelValues,
        potential_values: potentialValues,
        tau_0,
        alpha,
        kernel_formula: `K(t) = (${alpha}/${tau_0}) * exp(-t/${tau_0})`,
        delta_mass_kg: deltaMass
      });
    } catch (error) {
      console.error("Retarded potential error:", error);
      return res.status(500).json({ error: "Simulation failed" });
    }
  });
  
  app.post("/api/baryonic/bullet-cluster", requireAuth, async (req, res) => {
    try {
      const user = await storage.getUser((req.session as any).userId!);
      const constants = user?.grutConstants || DEFAULT_GRUT_CONSTANTS;
      
      const { 
        collisionVelocity = 4500,
        timeSinceCollision = 150,
        clusterSeparation = 720 
      } = req.body;
      
      const tau_0 = constants.tau_0;
      const alpha = constants.alpha;
      const n_g = constants.n_g;
      
      const K_t = (alpha / tau_0) * Math.exp(-timeSinceCollision / tau_0);
      const hysteresis_factor = 1 - K_t;
      const velocity_ratio = collisionVelocity / 1000;
      const predicted_offset = clusterSeparation * hysteresis_factor * velocity_ratio / 100;
      const gas_dm_separation = clusterSeparation * 0.2 * hysteresis_factor;
      
      const baryonic_mass = 2.3e14;
      const apparent_dm_mass = baryonic_mass * (1 + hysteresis_factor * n_g);
      
      return res.json({
        cluster_id: "1E 0657-558",
        collision_velocity_kms: collisionVelocity,
        time_since_collision_myr: timeSinceCollision,
        cluster_separation_kpc: clusterSeparation,
        kernel_weight: K_t,
        hysteresis_factor: hysteresis_factor,
        predicted_offset_mpc: Math.round(predicted_offset * 1000) / 1000,
        gas_dm_separation_kpc: Math.round(gas_dm_separation * 10) / 10,
        baryonic_mass_msun: baryonic_mass,
        apparent_dm_mass_msun: Math.round(apparent_dm_mass * 100) / 100,
        grut_explanation: "Metric hysteresis from gravitational memory creates lensing offset without dark matter particles",
        constants_used: { tau_0, alpha, n_g }
      });
    } catch (error) {
      console.error("Bullet cluster error:", error);
      return res.status(500).json({ error: "Simulation failed" });
    }
  });
  
  app.post("/api/baryonic/gravitational-waves", requireAuth, async (req, res) => {
    try {
      const user = await storage.getUser((req.session as any).userId!);
      const constants = user?.grutConstants || DEFAULT_GRUT_CONSTANTS;
      
      const { 
        eventType = "BH_merger",
        sourceDistance = 40,
        chirpMass = 30 
      } = req.body;
      
      const tau_0 = constants.tau_0;
      const alpha = constants.alpha;
      const n_g = constants.n_g;
      
      const distance_mpc_to_mly = 3.262;
      const light_travel_time_myr = sourceDistance * distance_mpc_to_mly;
      const phase_drift = alpha * (1 - Math.exp(-light_travel_time_myr / tau_0));
      const dispersion_factor = (n_g - 1) * sourceDistance / 1000;
      const timing_residual_ms = phase_drift * tau_0 * 1e-3;
      const strain_modification = 1 + dispersion_factor * 0.01;
      
      // Update complexity ratio based on simulation parameters
      // Distance and chirp mass contribute to information density
      const complexity_delta = (sourceDistance / 1000) * 0.01 + (chirpMass / 100) * 0.005;
      updateBaryonicComplexity(complexity_delta);
      
      // Check R_max Logic Guard - safety valve for information density
      const logic_guard = checkBaryonicLogicGuard();
      
      return res.json({
        event_type: eventType,
        source_distance_mpc: sourceDistance,
        chirp_mass_msun: chirpMass,
        light_travel_time_myr: Math.round(light_travel_time_myr * 100) / 100,
        predicted_phase_drift_rad: Math.round(phase_drift * 1e6) / 1e6,
        dispersion_factor: Math.round(dispersion_factor * 1e6) / 1e6,
        timing_residual_ms: Math.round(timing_residual_ms * 1e4) / 1e4,
        strain_modification_factor: Math.round(strain_modification * 1e6) / 1e6,
        detectability: Math.abs(phase_drift) < 0.01 ? "Marginal with current LIGO sensitivity" : "Potentially detectable",
        grut_signature: "Cumulative phase drift increasing with distance",
        logic_guard,
        constants_used: { tau_0, alpha, n_g }
      });
    } catch (error) {
      console.error("GW simulation error:", error);
      return res.status(500).json({ error: "Simulation failed" });
    }
  });
  
  app.post("/api/baryonic/hubble-tension", requireAuth, async (req, res) => {
    try {
      const user = await storage.getUser((req.session as any).userId!);
      const constants = user?.grutConstants || DEFAULT_GRUT_CONSTANTS;
      
      const { localH0 = 73.0, cmbH0 = 67.4 } = req.body;
      
      const tau_0 = constants.tau_0;
      const alpha = constants.alpha;
      const n_g = constants.n_g;
      
      const tension = localH0 - cmbH0;
      const tension_sigma = tension / 1.5;
      
      const t_local = 0.01 * 13700;
      const t_cmb = 0.38;
      
      const K_local = (alpha / tau_0) * Math.exp(-Math.max(t_local, 1) / tau_0);
      const K_cmb = (alpha / tau_0) * Math.exp(-t_cmb / tau_0);
      
      const correction_factor = (1 + alpha * (K_cmb - K_local)) * n_g;
      const corrected_cmb_H0 = cmbH0 * correction_factor;
      const residual_tension = localH0 - corrected_cmb_H0;
      
      return res.json({
        local_H0: localH0,
        cmb_H0: cmbH0,
        observed_tension: Math.round(tension * 100) / 100,
        tension_sigma: Math.round(tension_sigma * 10) / 10,
        grut_correction_factor: Math.round(correction_factor * 1e4) / 1e4,
        corrected_cmb_H0: Math.round(corrected_cmb_H0 * 100) / 100,
        residual_tension: Math.round(residual_tension * 100) / 100,
        resolution_status: Math.abs(residual_tension) < Math.abs(tension) * 0.5 ? "Partially resolved" : "Requires further analysis",
        mechanism: "Metric hysteresis causes H0 to appear lower at high redshift",
        constants_used: { tau_0, alpha, n_g }
      });
    } catch (error) {
      console.error("Hubble tension error:", error);
      return res.status(500).json({ error: "Simulation failed" });
    }
  });
  
  app.post("/api/baryonic/ringdown-memory", requireAuth, async (req, res) => {
    try {
      const { signalDuration = 1.5, snrRatio = 80 } = req.body;
      
      const result = analyzeRingdownMemory(signalDuration, snrRatio);
      
      return res.json({
        analysis_type: result.analysisType,
        signal_duration_seconds: result.signalDurationSeconds,
        snr_ratio: result.snrRatio,
        tau_0_seconds: result.tau0Seconds,
        tau_0_myr: result.tau0Myr,
        burden_factor_strain: result.burdenFactorStrain,
        mean_metric_drift: result.meanMetricDrift,
        initial_drift: result.initialDrift,
        final_drift: result.finalDrift,
        decay_ratio: result.decayRatio,
        sample_points: result.samplePoints,
        grut_prediction: result.grutPrediction,
        logic_guard: result.logicGuard,
        complexity_ratio: result.complexityRatio
      });
    } catch (error) {
      console.error("Ringdown memory error:", error);
      return res.status(500).json({ error: "Simulation failed" });
    }
  });
  
  // Full Baryonic Pipeline v6 - Ringdown + NANOGrav correlation
  app.post("/api/baryonic/full-pipeline", requireAuth, async (req, res) => {
    try {
      const { signalDuration = 1.5, snrRatio = 80 } = req.body;
      
      const result = runFullBaryonicPipeline(signalDuration, snrRatio);
      
      return res.json({
        pipeline: result.pipeline,
        step_1_ringdown: {
          analysis_type: result.step1Ringdown.analysisType,
          signal_duration_seconds: result.step1Ringdown.signalDurationSeconds,
          snr_ratio: result.step1Ringdown.snrRatio,
          mean_metric_drift: result.step1Ringdown.meanMetricDrift,
          burden_factor_strain: result.step1Ringdown.burdenFactorStrain,
          grut_prediction: result.step1Ringdown.grutPrediction
        },
        step_2_correlation: {
          analysis_type: result.step2Correlation.analysisType,
          single_event_drift: result.step2Correlation.singleEventDrift,
          pta_noise_amplitude: result.step2Correlation.ptaNoiseAmplitude,
          correlation_index: result.step2Correlation.correlationIndex,
          correlation_range: result.step2Correlation.correlationRange,
          match_found: result.step2Correlation.matchFound,
          status: result.step2Correlation.status,
          interpretation: result.step2Correlation.interpretation,
          complexity_adjustment: result.step2Correlation.complexityAdjustment
        },
        final_status: result.finalStatus,
        final_complexity_ratio: result.finalComplexityRatio,
        grut_conclusion: result.grutConclusion,
        logic_guard: result.step2Correlation.logicGuard
      });
    } catch (error) {
      console.error("Full pipeline error:", error);
      return res.status(500).json({ error: "Pipeline failed" });
    }
  });
  
  app.get("/api/baryonic/connections", async (req, res) => {
    const connections = {
      physics_mathematics: [
        { from: "Hubble Tension", to: "Poincare Geometry", relation: "Non-Euclidean cosmic structure" },
        { from: "Primes as Grains", to: "Mass Quantization", relation: "Discrete matter distribution" },
        { from: "Gravity", to: "Memory Dynamics", relation: "Retarded potential kernel" }
      ],
      cosmology_philosophy: [
        { from: "Dark Matter", to: "Metric Hysteresis", relation: "Apparent vs intrinsic mass" },
        { from: "Causality", to: "Light Cone Structure", relation: "Information propagation limits" },
        { from: "Observer", to: "Measurement", relation: "Causal participation in universe" }
      ],
      observational_theoretical: [
        { from: "Bullet Cluster", to: "GRUT Prediction", relation: "Lensing offset from memory" },
        { from: "GW Signals", to: "Residual Drift", relation: "Cumulative phase effects" },
        { from: "CMB Peaks", to: "tau_0 Signature", relation: "Delay scale imprint" }
      ]
    };
    
    return res.json({
      framework: "GRUT Interdisciplinary Network",
      connections,
      core_principle: "The Universe is a closed loop of Light looking at itself through the lens of Time",
      key_parameters: DEFAULT_GRUT_CONSTANTS
    });
  });
  
  app.get("/api/baryonic/objections", async (req, res) => {
    const objections = [
      {
        objection: "Cold Dark Matter explains galaxy rotation curves",
        category: "Empirical",
        grut_response: "GRUT's metric hysteresis produces identical rotation curve shapes without exotic particles.",
        key_prediction: "Rotation curve shape should correlate with galaxy formation epoch"
      },
      {
        objection: "CMB third acoustic peak requires dark matter",
        category: "Cosmological",
        grut_response: "The third peak amplitude can be matched by adjusting tau_0 and alpha.",
        key_prediction: "Subtle phase shifts in higher-order peaks that CDM cannot produce"
      },
      {
        objection: "Structure formation requires cold dark matter seeds",
        category: "Theoretical",
        grut_response: "GRUT's n_g > 1 gravitational index creates effective amplification of baryonic density perturbations.",
        key_prediction: "Small-scale structure cutoff at scales related to tau_0"
      },
      {
        objection: "Occam's Razor favors particle dark matter",
        category: "Philosophical",
        grut_response: "GRUT uses fewer free parameters than CDM+Lambda cosmology.",
        key_prediction: "Single theory explains multiple phenomena"
      }
    ];
    
    return res.json({
      framework: "GRUT Philosophical Defense",
      objections_addressed: objections.length,
      objections
    });
  });

  return httpServer;
}
