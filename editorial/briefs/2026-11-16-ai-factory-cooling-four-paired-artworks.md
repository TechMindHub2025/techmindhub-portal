# Four engineering analyses — paired artwork brief (November 16, 2026)

Scope: four independent pairs of generated artwork (feed cover and article infographic) for TechMind Hub. All imagery is **conceptual**, not a photographed installation, manufacturer schematic, standard-compliance certification or measured performance plot. Editorial sources and limitations appear in the articles, not on the images. R2 delivery follows `editorial/IMAGE-DELIVERY.md` with versioned `v1` filenames. Status: production draft; final artifacts require visual and technical inspection, R2 delivery, independent PR approval and live QA.

## Shared canon

- Primary domain: `infrastructure` for all four. Palette: Infrastructure blue `#426F94`, light surface `#EEF3F8`, neutral ink; secondary tones only to distinguish functions.
- Feed covers: distinct horizontal 16:9 compositions, one focal concept, short high-contrast English phrase (below), a small `TECHMIND HUB` text signature, restrained section label, safe margins. Inspect at 352×198 and 260×146.
- Infographics: separate vertical compositions near 4:5; one conceptual explanatory argument, restrained labels, legible at article width, no dense numerical plots. These are not enlarged covers.
- Never print authors, company/source citations, a URL, bibliography, numbered `01`/`02` badges, full article titles or faux manufacturer logos on the art.
- Original untouched PNG pair per story archived outside the R2 web ZIP. Three web exports per story: `-card-web-v1.webp`, `-infographic-web-v1.webp`, `-og-web-v1.jpg`.

## 1. Schneider Electric / Giga Computing — POD interfaces

- Slug: `schneider-gigabyte-vera-rubin-pod-infrastructure`
- Source: https://blog.se.com/datacenter/2026/11/13/gigabyte-and-schneider-electric-ai-factory-infrastructure-for-nvidia-vera-rubin-nvl72/
- Question: How does a rack-scale compute platform become a repeatable, testable POD-level facility design?
- One-sentence argument: Electrical, coolant, residual air and control boundaries must be specified together, with named failure domains.
- Motif: one AI rack cluster at the centre of a coordinated electrical feed, blue coolant network and subtle supervisory layer; not a literal Vera Rubin product drawing.
- Cover phrase (verbatim): `ONE POD, ONE SYSTEM`.
- Infographic title: `The POD Interface Contract`.
- Infographic exact labels: `Compute & Network`, `Power Delivery`, `Liquid Cooling`, `Residual Air`, `Controls`, `Failure Boundaries`.
- Palette: Infrastructure blue with a warm amber power accent and turquoise coolant accent.
- Cover alt: Conceptual AI POD rack cluster linked to facility power and blue coolant circuits under the words One Pod, One System.
- Hero alt: Conceptual POD interface map showing compute, power, liquid cooling, residual air, controls and their shared failure boundaries.
- Avoid: claiming measured uptime or reduced CAPEX; depicting unverified ports, rack geometry or NVIDIA/GIGABYTE trade dress.

## 2. Schneider Electric — cooling orchestration

- Slug: `schneider-cooling-orchestration-supervisory-control`
- Source: https://blog.se.com/datacenter/2026/11/11/cooling-orchestration-software-a-welcome-addition-to-ai-data-center-operations/
- Question: Where can supervisory optimization act without overriding safety-critical local controls?
- One-sentence argument: The plant can be coordinated using workload signals and bounded setpoints while local controllers preserve mandatory safe limits.
- Motif: a high-level supervisory control hub above a physically grounded cold-plate-to-heat-rejection chain; distinct local safety boundary.
- Cover phrase (verbatim): `CONTROL THE WHOLE LOOP`.
- Infographic title: `Supervisory Control, Local Safety`.
- Infographic exact labels: `Workload Signal`, `Supervisory Setpoints`, `Local CDU Control`, `Plant & Heat Rejection`, `Safety Limits`, `Fallback Mode`.
- Palette: Infrastructure blue, turquoise fluid lines, calm silver-grey controls surfaces.
- Cover alt: Conceptual thermal network and control node coordinating cooling hardware under the words Control the Whole Loop.
- Hero alt: Conceptual hierarchy of workload signals, supervisory setpoints, local CDU controls, heat rejection, safety limits and fallback mode.
- Avoid: fictional PUE/WUE percentages, fabricated charts or autonomously controlled unverified equipment.

## 3. Supermicro SC26 — direct-to-chip and rear-door

- Slug: `supermicro-sc26-hybrid-rack-cooling`
- Source: https://www.supermicro.com/en/event/sc26
- Question: Where do direct-to-chip liquid cooling and rear-door heat exchangers intercept rack heat?
- One-sentence argument: One extracts heat at the component; the other captures residual exhaust heat at the rack boundary, and both rely on a downstream facility sink.
- Motif: one rack depicted as two cutaway thermal pathways: copper/turquoise cold-plate loop inside, air-to-liquid rear-door coil behind.
- Cover phrase (verbatim): `TWO PATHS FOR HEAT`.
- Infographic title: `Two Different Heat-Capture Points`.
- Infographic exact labels: `Direct-to-Chip`, `Chip → Liquid`, `Rear-Door`, `Air → Liquid`, `Residual Air`, `Facility Heat Sink`.
- Palette: Infrastructure blue, cyan coolant, subtle warm air path.
- Cover alt: Conceptual server rack with two highlighted heat-removal paths under the words Two Paths for Heat.
- Hero alt: Conceptual comparison of heat moving from chips to cold plates versus exhaust air to a rear-door liquid exchanger.
- Avoid: generic claims that a rear door directly cools a GPU, unverified product-specific heat ratings or trade-show logos.

## 4. Singapore SS 726 — tropical operating risk

- Slug: `singapore-ss726-tropical-liquid-cooling-standard`
- Sources: https://www.enterprisesg.gov.sg/resources/media-centre/media-releases/2026/august/mr03826_singapore-launches-worlds-first-liquid-cooling-standard-for-data-centres-in-tropical-climates ; https://www.singaporestandardseshop.sg/Product/SSPdtDetail/2b7aa78a-36c9-4656-abc5-eb4dc1a6e431
- Question: What must stay under control when direct liquid cooling operates for years in a hot, humid environment?
- One-sentence argument: Reliable operation connects ambient/dew-point considerations to sealed-fluid chemistry, materials, commissioning and monitoring.
- Motif: conceptual tropical data hall with a blue sealed loop, an external humid environment and small monitoring details; no depiction of an official certification mark.
- Cover phrase (verbatim): `TROPICAL COOLING, REAL RISKS`.
- Infographic title: `Liquid Cooling in the Tropics`.
- Infographic exact labels: `Humidity & Dew Point`, `Fluid Quality`, `Materials`, `Leak Management`, `Commissioning`, `Monitoring`.
- Palette: Infrastructure blue with restrained desaturated tropical-green secondary accent; light editorial ground.
- Cover alt: Conceptual liquid-cooled data hall in a tropical setting under the words Tropical Cooling, Real Risks.
- Hero alt: Conceptual tropical liquid-cooling risk map covering ambient humidity, coolant quality, material choice, leaks, commissioning and monitoring.
- Avoid: implying the standard covers rear-door exchangers or two-phase designs, claiming certification/mandatory adoption or inventing proprietary clauses.
