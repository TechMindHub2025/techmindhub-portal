# Paired visual briefs — the infrastructure chain, November 15, 2026

Status: **editorial drafts; generation and owner review pending**. Three independent articles, six generated original artworks, nine R2 derivatives. The published website must not reference the planned paths until all nine R2 URLs return HTTP 200 and the final PR head has independent approval. Follow `editorial/VISUAL-CANON.md` and `editorial/IMAGE-DELIVERY.md` without alteration.

## Delta: From Grid to Chip

Article slug: `delta-800vdc-power-thermal-codesign`.

Sources: [Delta November 11 SC26 release](https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html), [NVIDIA 800 VDC engineering roadmap](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/).

Domain: **Infrastructure**, accent `#426F94`, light `#EEF3F8`, dark slate type, restrained cyan secondary highlight.

Question: Can higher-voltage distribution and megawatt liquid cooling be designed as one reliable facility system?

Shared metaphor: one architectural data-center cross-section with an electric DC power spine at the left and a liquid loop at the right, meeting around a high-density server row. Conceptual systems illustration, **not** an exact Delta installation or electrical diagram. No fictional circuit symbols, product branding or unrealistic arcs.

**Cover, 16:9:** exact major phrase **“Power Meets Cooling”**. Smaller category **“INFRASTRUCTURE”** and tiny **“TECHMIND HUB”**. Atmospheric but bright architectural cutaway; one unmistakable blue power flow, one contrasting cool fluid flow, both converging at a compute row. At 352px and 260px the phrase and one scene must remain legible. Crop-critical detail within central 90% for OG 1200×630 export. No extra numbers on cover.

**Infographic, 4:5:** exact title **“Power and Thermal Co-Design”**; smaller deck **“An 800 VDC architecture is a systems problem.”** Three large zones with visually continuous paths and only these headings and short text:

1. **“Electrical path”** — **“Voltage changes current and resistive loss.”**
2. **“Coolant path”** — **“Flow, temperature rise and pump work are linked.”**
3. **“Failure path”** — **“3+0 duty pumps do not establish N+1.”**

Optional one clear, subordinate annotation **“2.5 MW CDU — vendor announcement”**. Avoid diagrams of precise wiring, pump topology beyond the 3+0 label, arbitrary axes, efficiency percentages and invented benchmark results. Source attribution, equations and caveats belong in prose. Alt text per article frontmatter.

Originals: `delta-800vdc-power-thermal-codesign-card-original-v1.png` and `delta-800vdc-power-thermal-codesign-infographic-original-v1.png`. R2: `posts/delta-800vdc-power-thermal-codesign-{card-web-v1.webp,infographic-web-v1.webp,og-web-v1.jpg}` (role-specific base filenames; do not use braces in upload).

## Infomaniak: Heat Recovery Is Energy Accounting

Article slug: `infomaniak-bulle-datacenter-heat-reuse`.

Source: [Infomaniak / Gruyère Energie November 13 announcement](https://www.presseportal.ch/fr/pm/100057093/100943576).

Domain: **Energy & Environment**, accent `#6E793D`, light `#F3F5E9`, warm amber heat accents and soft off-white background.

Question: Where does the planned 28 GWh of district heat come from, and how can operators demonstrate that the heat is truly reused?

Shared metaphor: Bulle-inspired but **generic** Alpine town, elegant sectional view connecting an unbranded data-center building, a heat-pump station, underground insulated thermal pipe and occupied buildings. Express summer/winter constraint subtly in background, not via ungrounded seasonal metrics. Do not claim architectural fidelity to planned building.

**Cover, 16:9:** exact phrase **“Heat Beyond the Rack”**; category **“ENERGY & ENVIRONMENT”** and small **“TECHMIND HUB”**. Warm visible heat ribbon from servers toward buildings through a central heat-pump structure; clean, airy, not a greenwashing stock image. Keep the phrase large and crop-safe.

**Infographic, 4:5:** exact title **“When Server Heat Becomes Useful”**. Main visual is a clear *conceptual energy balance*, with **three directional inputs/outputs and explicit roles**, not a quantitative Sankey chart. Exact labels:

- **“Data center”** — **“2.5 MW IT power (planned)”**
- **“Recovered heat + heat-pump electricity”** — small explanatory line **“The heat pump adds energy.”**
- **“District heating”** — **“28 GWh/year (forecast)”**
- Bottom caution band **“A projection, not operating data.”**

Arrows: from server heat to heat pump; from separately depicted electricity into heat pump; heat pump to buildings. Any visual claim beyond the named labels prohibited. The article's simple annual energy comparison and carbon counterfactual are text facts, not image charts. Use generous spacing and legible labels on mobile. Alt text per frontmatter.

Originals: `infomaniak-bulle-datacenter-heat-reuse-card-original-v1.png`, `infomaniak-bulle-datacenter-heat-reuse-infographic-original-v1.png`. R2 files follow `<slug>-card-web-v1.webp`, `<slug>-infographic-web-v1.webp`, `<slug>-og-web-v1.jpg`.

## Gates: Hydraulics Inside 4U

Article slug: `gates-thermalcool-2100ss-cdu-hydraulics`.

Sources: [Gates November 12 announcement](https://www.gates.com/us/en/about-us/news.one.122768.html), [Gates technical datasheet](https://www.gates.com/content/dam/documents-library/flyers/thermalcool-data-centers-pumps-thermalcool-spec-sheet-2100ss-letter-na-en.pdf).

Domain: **Infrastructure**, accent `#426F94`, light `#EEF3F8`, more steel and precision-photographic detail than the Delta concept; same domain accent but unmistakably different silhouette and composition.

Question: Why does a pump's headline flow not determine the cooling capacity or redundancy of a complete rack CDU?

Shared metaphor: believable non-branded 4U-compatible pump module in a clean rack cross-section, two clearly routed coolant lines and an adjacent cold-plate cluster. This is a **conceptual device**, never claimed to be a faithful product photograph or real Gates CAD. Avoid invented model details.

**Cover, 16:9:** exact phrase **“Inside the Cooling Loop”**, small **“INFRASTRUCTURE”** and **“TECHMIND HUB”**. One compact industrial pump in focus with a deliberate line of blue coolant entering and warmer fluid leaving, visual mass low/right and title clear upper/left. Technical editorial photography styling, not neon sci-fi.

**Infographic, 4:5:** exact title **“A Pump Is Not a CDU”**; optional smaller deck **“The operating point matters.”** Three conceptual explanatory callouts, no invented numeric performance curve:

- **“Flow + pressure”** — **“Match the pump curve to circuit resistance.”**
- **“Heat carried”** — **“Flow × heat capacity × temperature rise.”**
- **“Redundancy”** — **“N+1 requires the system to survive a pump failure.”**

An understated fourth callout may read **“Motor heat returns to the liquid loop.”** No percentage or size on artwork. Main composition shows pump, cold plates and return pipes as visually distinct. Do not convert into fake engineered schematics or show an unverified specific Gates unit. Alt text per frontmatter.

Originals: `gates-thermalcool-2100ss-cdu-hydraulics-card-original-v1.png`, `gates-thermalcool-2100ss-cdu-hydraulics-infographic-original-v1.png`. R2 files follow `<slug>-card-web-v1.webp`, `<slug>-infographic-web-v1.webp`, `<slug>-og-web-v1.jpg`.

## Production and gate checklist

- [ ] Six independent generated PNG originals (three covers at ~16:9; three infographics at ~4:5), retained unchanged in separate original archive.
- [ ] Check legible text and exact spelling, arrows, claims, visual-pair consistency; owner approves artwork. Inspect card previews at 352px and 260px.
- [ ] Export three 800px-wide lossless resized WebP cards, three full-resolution lossless WebP infographics with exact decoded RGBA equality, and three centre-cropped 1200×630 quality-95 4:4:4 JPEG previews.
- [ ] Check image dimensions, hashes, actual OG crop and decoded pixel equality; record release manifest.
- [ ] Deliver `Originals-PNG` (6 originals) and `Cloudflare-Web` (9 derivatives) as separate archives; user uploads only the nine derivatives into R2 `tmh-assets/posts/`.
- [ ] Verify public HTTP 200 for every new R2 URL. Switch three posts from `draft` to `published` on the final article PR head, run `npm run validate`, inspect Home/archive/tags/article pages at desktop/mobile size.
- [ ] Obtain designated independent reviewer approval of exact final GitHub PR head, green checks, merge and inspect live GitHub Pages deployment.
- [ ] Only after live verification, use prepared manual social posts; never auto-publish external social content.
