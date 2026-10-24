import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import rehypeExternalLinks from './src/lib/rehype-external-links.mjs';

export default defineConfig({
  site: 'https://techmindhub.cc',
  integrations: [mdx()],
  markdown: {
    rehypePlugins: [[rehypeExternalLinks, { site: 'https://techmindhub.cc' }]],
  },
  output: 'static',
});
