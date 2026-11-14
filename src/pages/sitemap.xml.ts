import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

const origin = "https://techmindhub.cc";
const escapeXML = (value: string) => value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export const GET: APIRoute = async () => {
  const posts = await getCollection("posts", ({ data }) => data.status === "published");
  const staticPaths = ["/", "/posts/", "/deep-dives/", "/topics/", "/collections/", "/tags/", "/about/"];
  const tagPaths = [...new Set(posts.flatMap(post => post.data.tags))].map(tag => `/tags/${encodeURIComponent(tag)}/`);
  const entries = [
    ...staticPaths.map(path => ({ path, lastmod: undefined as string | undefined })),
    ...tagPaths.map(path => ({ path, lastmod: undefined as string | undefined })),
    ...posts.map(post => ({ path: `/posts/${encodeURIComponent(post.slug)}/`, lastmod: post.data.pubDate.toISOString().slice(0, 10) })),
    { path: "/collections/ai-infrastructure/", lastmod: undefined },
    { path: "/collections/engineering-reliability/", lastmod: undefined },
    { path: "/collections/ai-governance/", lastmod: undefined },
  ];
  const nodes = entries.map(({ path, lastmod }) => `<url><loc>${escapeXML(origin + path)}</loc>${lastmod ? `<lastmod>${lastmod}</lastmod>` : ""}</url>`).join("\n");
  return new Response(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${nodes}\n</urlset>\n`, {
    headers: { "Content-Type": "application/xml; charset=utf-8" },
  });
};
