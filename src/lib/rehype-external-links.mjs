/** Add native new-tab behaviour to external links while compiling Markdown/MDX. */
export default function rehypeExternalLinks({ site = 'https://techmindhub.cc' } = {}) {
  const ownHost = new URL(site).hostname;
  const internalHosts = new Set([
    ownHost,
    ownHost.startsWith('www.') ? ownHost.slice(4) : `www.${ownHost}`,
  ]);

  return (tree) => {
    const nodes = [tree];
    while (nodes.length) {
      const node = nodes.pop();
      const properties = node.properties;
      if (node.type === 'element' && node.tagName === 'a' && typeof properties?.href === 'string') {
        let url;
        try {
          url = new URL(properties.href, site);
        } catch {
          continue;
        }
        if ((url.protocol === 'https:' || url.protocol === 'http:') && !internalHosts.has(url.hostname)) {
          properties.target = '_blank';
          const existing = Array.isArray(properties.rel) ? properties.rel : String(properties.rel || '').split(/\s+/);
          properties.rel = [...new Set([...existing.filter(Boolean), 'noopener', 'noreferrer'])];
        }
      }
      if (Array.isArray(node.children)) nodes.push(...node.children);
    }
  };
}
