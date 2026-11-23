---
title: "Sandia and RAVEL Ask Where an AI Workload Should Run"
description: "Project Quicksilver will compare distributed computing sites, cooling methods and network constraints to test power-aware workload placement. It has not yet published measured savings."
excerpt: "Moving a job can trade local power scarcity for network and completion-time costs."
pubDate: "2026-11-24T06:40:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/sandia-ravel-quicksilver-power-aware-workloads-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/sandia-ravel-quicksilver-power-aware-workloads-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/sandia-ravel-quicksilver-power-aware-workloads-og-web-v1.jpg"
card_alt: "Three computing sites connected across a landscape beneath the words Move the Workload."
cover_alt: "Conceptual choice among three computing sites using power, cooling, network and completion-time inputs."
canonical_id: "2026-11-24-sandia-ravel-quicksilver-power-aware-workloads"
tags: ["DataCenters", "WorkloadScheduling", "LiquidCooling", "HPC", "TechMindHub"]
source_url: "https://ravelinc.com/press/ravel-sandia-project-quicksilver/"
domain: "infrastructure"
topic: "Power-aware computing"
---

When one computing site runs short of electrical or cooling headroom, a scheduler may have another option: move an eligible workload to a different site. That sounds simple until data transfer, network delay, cooling efficiency and deadlines enter the same decision. [Project Quicksilver](https://ravelinc.com/press/ravel-sandia-project-quicksilver/), announced by RAVEL with Sandia National Laboratories on November 12 and presented at SC26, is designed to investigate that trade-off.

The proposed work spans **three Sandia sites** connected by a wide-area network. Its first phase compares air and immersion cooling, and the research plan includes varying network bandwidth while examining energy, total cost of ownership and time to completion. PUE and TUE can help describe facility and system-level energy use, but they must be interpreted with consistent boundaries and workload conditions. A site that looks efficient at the facility meter may still finish a data-intensive job more slowly because inputs and outputs travel farther.

## Placement is a constrained decision

A useful scheduler would need a current estimate of available power and cooling capacity, data location, transfer volume, network state, job urgency and the energy cost of each candidate execution site. It would also need to know which tasks are movable. Latency-sensitive services, regulated data or tightly coupled distributed jobs may have very different placement limits from a batch training run.

The research could illuminate whether workload mobility makes existing capacity more useful before a new facility or utility connection is built. That is an **engineering hypothesis**, not a demonstrated alternative to new infrastructure. Moving computation does not erase its energy demand, and an apparent local saving can be offset by cooling or network overhead elsewhere.

No measured energy or cost results are in the announcement. The strongest future evidence would compare the same completed jobs across placement strategies while reporting workload completion, metered energy, network traffic and cooling boundaries. Until then, Quicksilver is a structured experiment in where to compute, not a quantified efficiency claim.

## Source

- [RAVEL and Sandia, Project Quicksilver announcement, November 12, 2026](https://ravelinc.com/press/ravel-sandia-project-quicksilver/)
