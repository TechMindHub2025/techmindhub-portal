---
title: "What a 2.3 MW Modular CDU Must Prove at the Facility Boundary"
description: "nVent's CX121 targets megawatt-scale liquid cooling with a maximum stated operating performance of 2.3 MW. Its modular design brings flow, temperature and redundancy questions into focus."
excerpt: "A vendor heat-duty rating is a starting point; delivered cooling depends on fluid conditions, rack demand, facility heat rejection and failure behaviour."
pubDate: "2026-11-17T13:15:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/nvent-cx121-modular-cdu-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/nvent-cx121-modular-cdu-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/nvent-cx121-modular-cdu-og-web-v1.jpg"
card_alt: "Conceptual modular coolant distribution unit with parallel modules and supply and return lines."
cover_alt: "Conceptual separation of rack and facility cooling loops across a modular coolant distribution unit."
canonical_id: "2026-11-17-nvent-cx121-modular-cdu"
tags: ["DataCenters", "LiquidCooling", "CDU", "ThermalEngineering", "TechMindHub"]
source_url: "https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx"
domain: "infrastructure"
topic: "Modular coolant distribution"
---

As rack heat loads rise, a coolant distribution unit becomes a critical interface between IT cooling circuits and the building's heat-rejection system. At SC26, [nVent introduced its modular CX121 CDU](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx), stating a maximum operating performance of **2.3 MW**. The company is accepting pre-orders and expects production in **late 2026**. This is a product announcement, not a report that 2.3 MW installations have completed independent field testing.

The engineering question behind the headline capacity is where the heat goes and under what operating conditions that maximum is achievable. A CDU transfers energy between a technology-cooling loop serving equipment and a facility loop that must reject it. In a separated-loop design, a heat exchanger maintains the boundary between fluid circuits; pumps, filters, valves, sensors and controls determine how much usable flow reaches individual racks.

## Design around conditions, not one power number

Thermal duty depends on mass flow, heat capacity and temperature rise: `Q ≈ mass flow × specific heat × ΔT`. The exact duty also depends on inlet temperatures and the approach temperature of the heat exchanger. A published maximum in MW cannot on its own tell a designer the delivered cooling at a warmer facility-water supply temperature, a particular rack return temperature or a chosen redundancy mode. The necessary performance curves and design point need to be checked against the proposed plant.

Modularity can permit staged capacity or maintenance, but a set of parallel modules does not automatically constitute independent fault domains. Shared headers, control power, water chemistry and facility heat rejection can disable multiple modules together. Commissioning should exercise a module-out condition, pump switchover, a partially isolated rack branch and facility-side flow loss while recording temperatures at the most constrained cold plate. Operators also need to know whether a standby module has sufficient capacity **at the required temperatures**, not merely that it can start.

nVent's same SC26 release also discusses a **liquid-to-air CDU for OCP Project Brazos**, intended to make liquid cooling possible without a facility water connection. That is a separate offering and a different heat-rejection boundary. It should not be treated as a feature or a tested configuration of the CX121.

## Evidence for a retrofit decision

For an existing air-cooled hall, the scope is more than the CDU cabinet: it includes piping and service clearances, floor loading, leak management, controls integration, air-side residual heat and the ultimate heat sink. A comparison with the existing plant should use the same IT load, ambient conditions and redundancy requirement, including pump and fan energy. It should distinguish a facility-water loop from a liquid-to-air route.

The 2.3 MW figure is a **manufacturer's maximum stated operating performance**. Independent test data, site-specific efficiency and long-term reliability were not supplied in this announcement. Pre-orders and planned production are not evidence of production deployments. CX121 is therefore a useful design prompt for modular liquid-cooling architecture, with its economic and operational case still to be established at a documented operating point.

## Source

- [nVent: expanded liquid cooling and power portfolio at SC26, November 16, 2026](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx)
