import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

const origin = "https://techmindhub.cc";
const escapeXML = (value: string) => value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&apos;");

export const GET: APIRoute = async () => {
  const posts = (await getCollection("posts", ({ data }) => data.status === "published"))
    .sort((a, b) => +b.data.pubDate - +a.data.pubDate || a.slug.localeCompare(b.slug));
  const items = posts.map(post => {
    const url = `${origin}/posts/${encodeURIComponent(post.slug)}/`;
    return `<item>
      <title>${escapeXML(post.data.title)}</title>
      <link>${escapeXML(url)}</link>
      <guid isPermaLink="true">${escapeXML(url)}</guid>
      <pubDate>${post.data.pubDate.toUTCString()}</pubDate>
      <description>${escapeXML(post.data.description)}</description>
      <dc:creator>${escapeXML(post.data.author)}</dc:creator>
      ${post.data.tags.map(tag => `<category>${escapeXML(tag)}</category>`).join("\n")}
    </item>`;
  }).join("\n");
  return new Response(`<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="/feed.xsl"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>TechMind Hub</title>
  <link>${origin}/</link>
  <description>Source-linked analysis of AI, infrastructure, robotics and emerging technology.</description>
  <language>en</language>
  <atom:link href="${origin}/feed.xml" rel="self" type="application/rss+xml" />
  ${items}
</channel>
</rss>\n`, { headers: { "Content-Type": "application/rss+xml; charset=utf-8" } });
};
