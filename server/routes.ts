import type { Express } from "express";
import { createServer, type Server } from "http";
import { storage } from "./storage";
import { insertSubscriberSchema } from "@shared/schema";

export async function registerRoutes(
  httpServer: Server,
  app: Express
): Promise<Server> {
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

  return httpServer;
}
