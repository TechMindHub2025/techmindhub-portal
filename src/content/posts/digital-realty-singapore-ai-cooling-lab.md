---
title: "Testing a 150 kW AI Rack Before It Reaches Production"
description: "Digital Realty's Singapore SIN11 Innovation Lab offers a multi-vendor environment for testing high-density racks, liquid-cooling paths, power systems and facility controls before deployment."
excerpt: "A 150 kW-plus rack rating describes what the lab supports, not an independently published endurance result or facility efficiency figure."
pubDate: "2026-11-17T13:16:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/digital-realty-singapore-ai-cooling-lab-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/digital-realty-singapore-ai-cooling-lab-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/digital-realty-singapore-ai-cooling-lab-og-web-v1.jpg"
card_alt: "Liquid-cooled test rack with blue and copper coolant lines and a monitoring display."
cover_alt: "Conceptual SIN11 rack test environment showing alternative liquid-cooling paths and facility power and monitoring systems."
canonical_id: "2026-11-17-digital-realty-singapore-ai-cooling-lab"
tags: ["DataCenters", "LiquidCooling", "RackDensity", "Commissioning", "TechMindHub"]
source_url: "https://www.globenewswire.com/news-release/2026/11/17/3404269/0/en/digital-realty-innovation-lab-dril-launches-in-singapore-enabling-asia-pacific-enterprises-to-validate-and-scale-ai-ready-infrastructure.html"
domain: "infrastructure"
topic: "High-density rack validation"
---

Before installing a high-density AI rack in a production hall, an operator needs evidence that the rack, liquid loop, facility water, electrical supply and monitoring systems behave together. Digital Realty [announced the opening](https://www.globenewswire.com/news-release/2026/11/17/3404269/0/en/digital-realty-innovation-lab-dril-launches-in-singapore-enabling-asia-pacific-enterprises-to-validate-and-scale-ai-ready-infrastructure.html) of an Innovation Lab inside its operating **SIN11 data center in Singapore** on November 17. It describes the facility as a multi-vendor testing environment for AI-ready infrastructure, with support for **liquid-cooled rack densities of 150 kW and above**.

The announcement lists chilled-water cooling, liquid-to-liquid and liquid-to-air configurations, a distributed redundant design with parallel UPS, dual diverse fiber entries, and building and electrical power monitoring through BMS and EPMS. Those elements make the lab more than a showroom for a server rack: they expose interfaces between IT equipment and the facility systems that must carry its load.

## A rack rating is an interface test, not a result

The useful engineering question is how a particular combination of equipment performs under a defined heat load. A liquid-to-liquid configuration transfers heat across a heat exchanger into an available facility water path. A liquid-to-air option rejects heat to air and can have a different dependence on room airflow and final heat rejection. These are alternative integration paths, not proof that the same rack simultaneously follows both. Either approach must establish compatible fluid temperatures, flow rates, pressure losses, leak detection, controls and service procedures.

At approximately 150 kW per rack, small mismatches between equipment specifications and the installed distribution system can become consequential. An acceptance plan should identify the rack's actual liquid capture fraction and remaining air-side load; test pump and fan transitions; verify sensor placement and alarm delivery; and record the behaviour after loss of a cooling or electrical component. UPS parallelism and redundant elements must be tested against common controls, headers and maintenance states before a resilience claim is justified.

BMS and EPMS are also part of the test boundary. They should correlate thermal, electrical and workload events with usable timestamps. A system that can dissipate heat in a steady-state demonstration may still fail a restart, workload step or planned isolation procedure. Multi-vendor testing is valuable precisely because a supplier's component rating does not certify the interfaces between suppliers.

## What remains unmeasured publicly

**150 kW-plus is the supported rack-density specification stated by Digital Realty**, not a published independent load-test record for every configuration. The announcement does not provide an independently verified PUE or WUE, a long-duration failure rate, a common baseline for alternative cooling paths or detailed acceptance reports. The date the lab opened is stated, but the release does not establish a completed production rollout for any customer equipment tested there.

The lab therefore provides a place to ask better deployment questions. Its significance will depend on the test protocols, measurements and failure cases applied to a specific rack and facility design, rather than the highest supported rack number alone.

## Source

- [Digital Realty: Innovation Lab opens in Singapore SIN11, November 17, 2026](https://www.globenewswire.com/news-release/2026/11/17/3404269/0/en/digital-realty-innovation-lab-dril-launches-in-singapore-enabling-asia-pacific-enterprises-to-validate-and-scale-ai-ready-infrastructure.html)
