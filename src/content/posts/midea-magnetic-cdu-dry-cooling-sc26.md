---
title: "Midea Pairs a Magnetic CDU with Dry Cooling for AI Data Centers"
description: "The SC26 modular cooling concept combines outdoor dry coolers, free cooling and compressor assistance. Its water and energy tradeoffs still need site-level data."
excerpt: "A cooling-tower-free design moves the engineering question from water supply to climate-dependent mechanical power."
pubDate: "2026-11-25T07:03:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/midea-magnetic-cdu-dry-cooling-sc26-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/midea-magnetic-cdu-dry-cooling-sc26-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/midea-magnetic-cdu-dry-cooling-sc26-og-web-v1.jpg"
card_alt: "Conceptual modular cooling unit linked to an outdoor dry cooler beside a data center."
cover_alt: "Conceptual dry cooler rejects heat from a data center liquid loop, with free cooling and compressor-assisted operating modes."
canonical_id: "2026-11-25-midea-magnetic-cdu-dry-cooling-sc26"
tags: ["DataCenters", "LiquidCooling", "ThermalEngineering", "WaterUse", "TechMindHub"]
source_url: "https://www.prnewswire.com/news-releases/certainty-for-every-token-midea-debuts-at-sc26-with-modular-prefabricated-cooling-solutions-to-accelerate-ai-compute-deployment-302946893.html"
domain: "infrastructure"
topic: "Modular dry cooling"
---

Liquid-cooled AI racks still need somewhere to reject their heat. In a hot climate, removing an evaporative cooling tower changes the balance of water use, compressor work and outdoor equipment. Midea's [November 20 SC26 announcement](https://www.prnewswire.com/news-releases/certainty-for-every-token-midea-debuts-at-sc26-with-modular-prefabricated-cooling-solutions-to-accelerate-ai-compute-deployment-302946893.html) describes a prefabricated architecture centered on a **magnetic CDU and outdoor dry coolers**. The company says it has supplied batches for an unnamed Southeast Asian cloud data-center project, but does not publish a site-level operating dataset.

## Two ways to reject heat

When outdoor air is cool enough for the required supply temperature, dry coolers can reject heat without evaporating water. As ambient temperature rises, a magnetic-bearing compressor provides mechanical assistance. The supplier claims a **20–45 °C** supply-liquid range over year-round operation. This is a stated capability envelope, not a guarantee that every temperature in that range is available at every load and ambient condition.

The illustration above separates the closed IT coolant loop from outdoor air. It is a conceptual explanation, not a plumbing diagram of the manufacturer's equipment. The compressor changes the thermodynamic cost of heat rejection; it cannot make hot air equivalent to a cool ambient heat sink. For a specific campus, engineers must map wet-bulb and dry-bulb weather distributions, design heat load, approach temperature, allowable coolant temperature and required redundancy. Part-load hours can matter more than a single peak rating.

## Prefabrication and the commissioning boundary

Midea says the cooling source, distribution and control can be factory assembled and commissioned as a module. It reports faster delivery and reduced floor space relative to its chosen conventional comparison. These are manufacturer claims without a published denominator, independent commissioning schedule or side-by-side design basis. Integrating modules at the factory can reduce work on site, but interconnections, water quality, controls, power, monitoring and failover still have to be tested at the facility.

A dry cooler can eliminate the water consumed by an evaporative tower in this heat-rejection path. It may instead increase electricity use during hot hours when the compressor runs. A rigorous comparison would report annual cooling energy and water use, COP under specified ambient and load conditions, whole-site PUE and WUE, and resilience when one module is unavailable. Until those data are available, the useful story is the architecture and its tradeoff, not a proven efficiency improvement for every tropical data center.

Source: [Midea announcement at SC26, November 20, 2026](https://www.prnewswire.com/news-releases/certainty-for-every-token-midea-debuts-at-sc26-with-modular-prefabricated-cooling-solutions-to-accelerate-ai-compute-deployment-302946893.html).
