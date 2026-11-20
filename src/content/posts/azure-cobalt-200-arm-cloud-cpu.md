---
title: "Cobalt 200 Reaches Azure: The Workload Test for Custom Arm Cloud CPUs"
description: "Azure Cobalt 200 VMs are generally available on Arm Neoverse CSS V3. The reported performance gain over Cobalt 100 needs workload, pricing and portability context."
excerpt: "A faster custom CPU becomes an economic advantage only for workloads that move cleanly and cost less to run."
pubDate: "2026-11-20T06:12:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/azure-cobalt-200-arm-cloud-cpu-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/azure-cobalt-200-arm-cloud-cpu-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/azure-cobalt-200-arm-cloud-cpu-og-web-v1.jpg"
card_alt: "A conceptual Arm server processor among modular cloud racks."
cover_alt: "Conceptual Cobalt 200 VM evaluation through Arm64 portability, sizing, workload benchmarks and price and energy measurements."
canonical_id: "2026-11-20-azure-cobalt-200-arm-cloud-cpu"
tags: ["Semiconductors", "Arm64", "Azure", "CloudEconomics", "TechMindHub"]
source_url: "https://newsroom.arm.com/news/arm-microsoft-azure-cobalt-200"
domain: "infrastructure"
topic: "Custom Arm cloud CPUs"
---

Microsoft has made Azure virtual machines powered by its **Cobalt 200** processor generally available, according to [Arm's November 17 announcement](https://newsroom.arm.com/news/arm-microsoft-azure-cobalt-200). The custom CPU is built on Arm Neoverse Compute Subsystems V3. Arm relays Microsoft's claim of **up to 50% better CPU performance than Cobalt 100 VMs** and says its own workload testing produced similar improvements in cloud applications.

“Up to” matters. It is a result for particular comparisons and software conditions, not a prediction that every database, service or agent will run 50% faster. Nor does CPU throughput by itself determine the cost of a useful request.

## The engineering unit is a workload, not a chip

Custom silicon gives a hyperscaler more control over CPU design and its surrounding platform. A buyer, however, runs applications on priced VMs. The first questions are whether the application and its native dependencies work on **Arm64**, what VM shape delivers the needed memory and network resources, and whether latency and throughput improve under realistic concurrency. Compilation, containers, libraries, monitoring agents and deployment tooling can each affect portability.

Performance per watt is relevant to the operator's capacity planning, but customer economics also depend on VM price, utilization and operational effort. A meaningful migration comparison uses the same service-level objective and representative traffic, then measures cost per transaction or job alongside tail latency. If a workload is constrained by storage, network or software locks, a CPU improvement may have limited effect.

## A useful pilot

Choose one portable, CPU-sensitive service. Establish a Cobalt 100 or current production baseline with identical software and repeatable traffic. Compare the available Cobalt 200 VM sizes, application response times, CPU and memory utilization, and total VM spend. Include deployment and observability tooling in the trial. Only then extrapolate to a larger fleet.

The general availability milestone is concrete. Broad performance or savings across arbitrary applications remain unproven by the announcement, and independent workload benchmarks and current VM pricing are needed for a specific purchasing decision.

## Source

- [Arm: Azure Cobalt 200 VMs reach general availability, November 17, 2026](https://newsroom.arm.com/news/arm-microsoft-azure-cobalt-200)
