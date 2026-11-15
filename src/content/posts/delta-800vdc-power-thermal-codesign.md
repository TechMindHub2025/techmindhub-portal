---
title: "From Grid to Chip: The Engineering Trade-offs Behind 800 VDC AI Data Centers"
description: "Delta's SC26 portfolio links high-voltage DC distribution with megawatt-scale coolant delivery. The physics are compelling; the electrical, hydraulic and failure boundaries still need proof."
excerpt: "Higher voltage can reduce distribution current, but it does not eliminate conversion losses or cooling requirements. Delta's 2.5 MW CDU makes the co-design problem concrete."
pubDate: "2026-11-15T03:00:00Z"
status: "draft"
canonical_id: "2026-11-15-delta-800vdc-power-thermal-codesign"
tags: ["800VDC", "AIDatacenters", "LiquidCooling", "PowerDistribution", "CDU", "TechMindHub"]
source_url: "https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html"
cover_card: "https://media.techmindhub.cc/posts/delta-800vdc-power-thermal-codesign-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/delta-800vdc-power-thermal-codesign-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/delta-800vdc-power-thermal-codesign-og-web-v1.jpg"
domain: "infrastructure"
topic: "Power and thermal co-design"
card_alt: "A conceptual data-center power spine branches into a cooled compute rack, with the words Power Meets Cooling."
cover_alt: "Conceptual comparison of higher-voltage DC distribution, the coolant delivery loop and the protection and redundancy questions connecting them."
---

The energy entering an AI data center has two linked destinations: computation and heat. The more densely those computations are packed, the less credible it becomes to design the electrical distribution and liquid-cooling systems as unrelated purchases. Cable losses, power-conversion heat, pump energy, facility protection and the temperature of the coolant all influence the same operating envelope.

On November 11, 2026, Delta Electronics [announced its SC26 portfolio](https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html), including components intended for emerging 800 VDC and ±400 VDC distribution architectures. Among them is an 800 VDC-powered, 2.5 MW in-row liquid-to-liquid coolant distribution unit (CDU). The announcement is evidence of a vendor developing equipment for the transition; it is not evidence that those architectures have been deployed at scale or independently proved more efficient in operation.

The engineering significance is not a single larger pump. It is the decision to treat the route from the grid to the silicon, and the path carrying heat away from it, as one coupled system.

## Why raise the distribution voltage?

For a fixed power transfer, current decreases as voltage increases: `P = V × I` in the simplified DC case. A 2 MW load would draw approximately 5,000 A at 400 V or 2,500 A at 800 V, before allowing for conversion losses and the actual arrangement of conductors. If conductor resistance and path length were unchanged, the current-dependent resistive loss `I²R` would fall to one quarter at twice the voltage.

That is a useful physical comparison, not a prediction that an entire data center will save 75% of its electricity. A real assessment must count conversion stages, semiconductor losses, power-supply efficiency, busway geometry, protection devices and the energy consumed by cooling. It must also compare equivalent system boundaries and load profiles. **An improvement in one section of the distribution path is not an end-to-end efficiency result.**

The distinction between 800 VDC and ±400 VDC also matters. A bipolar ±400 V architecture has an 800 V potential between its positive and negative rails, but its relationships to earth, fault detection and isolation differ from a single 800 V rail. These are not interchangeable safety specifications.

NVIDIA's [800 VDC technical roadmap](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/) places megawatt-class racks in the emerging design target from 2027. That is a vendor roadmap, not an installed-base statistic. Any adoption decision still depends on coordinated designs across power equipment, rack loads, batteries, protection and operations.

## What the 2.5 MW CDU actually implies

Delta specifies a liquid-to-liquid, in-row CDU with **three 800 VDC, 25 kW hot-swappable pumps in a 3+0 configuration**, a stated flow of up to **3,850 L/min**, and **60 psi** pressure at the cited operating point. Its announcement describes a design intended for zero-downtime operation. These numbers provide a useful way to interrogate the thermal and hydraulic boundary—but they should not be interpreted as a published independent acceptance test.

For an illustrative water loop, assume the full 2.5 MW of heat is transported at the quoted flow, and approximate the fluid density as 1 kg/L and the heat capacity as 4.18 kJ/(kg·K). The required temperature rise would be:

`ΔT = 2,500 kW / [(3,850 / 60) kg/s × 4.18 kJ/(kg·K)] ≈ 9.3°C.`

The calculation is conditional. The stated flow may not be the flow through the exact thermal boundary represented by the 2.5 MW rating; a specified glycol mixture, different approach temperature or changing flow profile alters the result. The rated thermal capacity alone does not establish supply and return temperatures.

There is another useful boundary check. If 60 psi represents the **differential pressure across the pump duty point**, then `Δp × volume flow` is approximately **26.6 kW of ideal hydraulic power** at 3,850 L/min. That is a conditional calculation, not a measured electrical load: the release does not establish that its pressure figure is a pump differential head across that entire flow, or provide measured efficiencies at that point. The combined **75 kW motor nameplate capacity** is not the same thing as actual pump consumption.

Most importantly, **3+0 is not, by itself, N+1 redundancy**. Hot-swappable equipment can make a replacement faster, yet removing one of three duty pumps may reduce available flow and thermal capacity. To support a zero-interruption claim at a specified workload, an operator would need a published duty curve, surviving-pump capability, maintenance isolation strategy and demonstrated transient temperatures during a pump failure or replacement. The announcement does not establish those conditions.

## Cooling is spreading beyond the processors

Delta's release also describes a **double-sided liquid-cooling solution for Open Adapter Card architectures** intended to handle up to 3,000 W from computing components and 500 W from power components within a 40 mm cold-plate profile. This is a specific board-level solution; it does not mean every GPU now consumes 3 kW or that the design has been validated in a production cluster.

It is still an important signal. Power components, memory, networking devices and densely packaged electronics increasingly compete for the same available thermal margin. Moving converter heat to liquid cooling can reduce a local air-cooling bottleneck while transferring more of the total heat-rejection obligation to the fluid plant. An efficient electrical topology that increases the coolant system's parasitic power or leaves an uncooled hotspot may not improve system performance.

Delta separately lists a 200 kW in-rack CDU, a **2 MW** in-row Project Deschutes CDU with a specified **3°C approach temperature**, and a **60 kW per rack** liquid-to-air Project Brazos unit. These are distinct products and boundary conditions, not multiple measurements of the 2.5 MW 800 VDC CDU.

## What a credible deployment test would contain

Before treating this product family as a design baseline, an engineering team should ask for the following evidence at representative AI load:

- **Electrical:** metered power at facility input, downstream DC distribution and IT input, at several load levels; loss separation by converter, busway and rack stage.
- **Thermal:** heat removed at stated coolant flow, fluid composition and supply/return temperatures, including conversion and pump heat that enters the loop.
- **Hydraulic:** pressure/flow curves and motor consumption at the same duty point, plus available capacity after a pump is isolated.
- **Resilience:** protective-device coordination, DC arc and ground-fault response, battery transition, pump-failure transients and service procedures under load.
- **Operations:** a documented approach to leak containment, water quality, controls integration and fail-safe behaviour when communications are lost.

ASHRAE's [data-center engineering guidance](https://handbook.ashrae.org/handbooks/A23/SI/A23_Ch20/a23_ch20_si.aspx) treats power and cooling as interdependent facility services. That systems perspective is especially relevant here: a diagram with fewer conversion boxes or a CDU with a large nameplate does not establish a resilient AI factory.

The genuine direction signaled by Delta's SC26 announcement is **power-and-thermal co-design**. The outstanding question is how much of the theoretical benefit survives real load curves, fault scenarios and maintenance—and whether the operating data can be independently verified.

## Sources

- [Delta Electronics: SC26 power and cooling announcement, November 11, 2026](https://www.prnewswire.com/news-releases/delta-unveils-from-grid-to-chip-cooling-innovations-for-ai-infrastructure-and-for-new-800-vdc-400-vdc-architectures-at-sc26-302935999.html)
- [NVIDIA: 800 VDC architecture roadmap and engineering rationale](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [ASHRAE Handbook: Data Centers and Telecommunication Facilities](https://handbook.ashrae.org/handbooks/A23/SI/A23_Ch20/a23_ch20_si.aspx)
