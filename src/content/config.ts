// src/content/config.ts
import { defineCollection, z } from "astro:content";

const posts = defineCollection({
  type: "content",
  schema: z.object({
    // Core
    title: z.string(),
    description: z.string(),
    excerpt: z.string().optional(),

    // Accepts "2026-02-13" and coerces to Date
    pubDate: z.coerce.date(),

    // Visibility control
    status: z.enum(["published", "draft"]).default("draft"),

    // Stable ID for dedup / tracking across channels
    canonical_id: z.string().min(1),

    // Tags must be an array (even if 1 tag)
    tags: z.array(z.string()).default([]),

    // Source link (original / reference / permalink)
    source_url: z.string().url(),

    // Images (store in /public and reference by absolute path)
    cover_card: z.string().min(1),
    cover_hero: z.string().min(1),

    // Optional
    cover_alt: z.string().default(""),

    // Optional social links (bot can fill these later)
    social: z
      .object({
        linkedin: z.string().url().optional(),
        facebook: z.string().url().optional(),
      })
      .optional(),
  }),
});

export const collections = { posts };
