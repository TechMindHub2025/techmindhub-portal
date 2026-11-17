---
title: "An 800 V DC Power Rack Beside Existing AI Infrastructure"
description: "nVent's MAVERICK concept converts existing facility AC into 800 V DC in a separate rack beside IT equipment. The architecture raises new protection and staged-retrofit questions."
excerpt: "Moving conversion into an adjacent rack may simplify one retrofit boundary, but efficiency, protection and cost need a complete system comparison."
pubDate: "2026-11-17T13:13:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/nvent-maverick-800vdc-power-rack-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/nvent-maverick-800vdc-power-rack-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/nvent-maverick-800vdc-power-rack-og-web-v1.jpg"
card_alt: "Conceptual separate power rack receiving AC and feeding an adjacent AI server rack by DC bus."
cover_alt: "Conceptual boundary between existing AC supply, an adjacent conversion rack and an 800 V DC IT rack."
canonical_id: "2026-11-17-nvent-maverick-800vdc-power-rack"
tags: ["DataCenters", "PowerDistribution", "DirectCurrent", "ACDCConversion", "TechMindHub"]
source_url: "https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx"
domain: "infrastructure"
topic: "800 V DC distribution"
---

Where should AC-to-DC conversion happen in a high-density AI facility? In its [SC26 portfolio announcement](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx), nVent presented the **MAVERICK 800 VDC Power Rack**: a separate rack designed to receive existing facility AC supply and deliver 800 V DC beside IT racks. The company positions this as a way to introduce a DC distribution architecture without redesigning the entire building power system at once.

This is a **trade-show architecture showcase**, not a documented installation or independent efficiency comparison. Its interest lies in the conversion boundary. An adjacent rack can concentrate conversion equipment, protection and controls near the load, while leaving an upstream AC distribution path in place. That may define a smaller retrofit scope than changing every facility bus, but it does not eliminate the need to study the AC supply or the DC interface.

## Voltage changes the protection problem

For the same transmitted power, higher voltage generally means lower current, which can reduce conductor losses for a specified run. The system-level result depends on converter efficiency, cable lengths, conductor sizes, load sharing and operating point. A simple comparison of 800 V with a lower-voltage bus is not enough to calculate energy savings or total cost.

DC fault behaviour deserves particular attention. Unlike an AC waveform, a DC current has no periodic natural zero crossing to assist interruption. Isolation devices, fault detection, earthing or grounding strategy, arc management and selectivity must be matched to the proposed topology. A fault in one downstream rack should not silently compromise an entire row through a shared distribution path. The engineering review also needs to cover safe maintenance and how the power rack interacts with upstream UPS and downstream server input requirements.

The physical separation shown in the concept makes staged commissioning possible to examine: install a conversion rack, test its AC input and DC output, connect one compatible IT rack, then evaluate expansion. At each stage, measure input and output power, cable temperature, fault response, transient behaviour and conversion losses at realistic load. These are **suggested acceptance tests**, not published MAVERICK test results.

## What has not been demonstrated publicly

nVent has not provided an independent efficiency or TCO comparison for this rack in the announcement. A nearby power rack may reduce one category of facility rework while increasing floor-space, service or protection demands elsewhere. The outcome depends on the actual building and IT equipment. Nor does a SC26 presentation establish commercial deployment, long-term reliability or compatibility with every existing AC topology.

The useful takeaway is an architectural question: **can conversion be moved close to an AI load while preserving a safe, selective and economically sound power path?** MAVERICK proposes one boundary for that experiment. The answer requires a complete electrical study and measured operating evidence.

## Source

- [nVent: expanded liquid cooling and power portfolio at SC26, November 16, 2026](https://investors.nvent.com/press-releases/press-release-details/2026/nVent-Features-Expanded-Liquid-Cooling-and-Power-Portfolio-at-SC26/default.aspx)
