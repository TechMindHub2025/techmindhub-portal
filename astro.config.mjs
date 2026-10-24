import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://techmindhub.cc',
  integrations: [mdx()],
  output: 'static',
});
