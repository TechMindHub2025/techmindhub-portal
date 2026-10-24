// src/content/config.ts
import { defineCollection, z } from "astro:content";
import domains from "../data/editorial-domains.json";

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

    // Publication images are hosted on Cloudflare R2.
    cover_card: z.string().min(1),
    cover_hero: z.string().min(1),

    // Optional
    cover_alt: z.string().default(""),
    card_alt: z.string().default(""),
    topic: z.string().optional(),
    domain: z.string().refine(id => domains.some(d => d.id === id), {message: "Unknown editorial domain; add it to src/data/editorial-domains.json first."}).optional(),

    // Optional social links (bot can fill these later)
    social: z
      .object({
        linkedin: z.string().url().optional(),
        facebook: z.string().url().optional(),
      })
      .optional(),
  }).superRefine((data, ctx) => {
    if (data.status !== "published") return;
    for (const key of ["domain", "topic", "card_alt", "cover_alt"] as const) {
      if (!data[key]?.trim()) {
        ctx.addIssue({ code: z.ZodIssueCode.custom, path: [key], message: "Published posts require this field under the visual canon." });
      }
    }
    for (const key of ["cover_card", "cover_hero"] as const) {
      try {
        const url = new URL(data[key]);
        if (url.protocol !== "https:" || url.host !== "media.techmindhub.cc" || url.username || url.password || !url.pathname.startsWith("/posts/") || url.pathname === "/posts/") throw new Error("Not a publication R2 URL");
      } catch {
        ctx.addIssue({ code: z.ZodIssueCode.custom, path: [key], message: "Published image must use https://media.techmindhub.cc/posts/<versioned-file>." });
      }
    }
    if (data.cover_card === data.cover_hero) {
      ctx.addIssue({ code: z.ZodIssueCode.custom, path: ["cover_hero"], message: "Cover and infographic need separate compositions and URLs." });
    }
  }),
});

export const collections = { posts };
