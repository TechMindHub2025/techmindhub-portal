---
title: "PsiQuantum’s Optical Switch: Low Loss Is Only Part of the Network Design"
description: "PsiQuantum reports an 8×8 optical circuit-switching demonstrator. Its insertion loss and reconfiguration time matter alongside scheduling, complete-link losses and AI traffic patterns."
excerpt: "An optical switch can carry traffic over a set path and later change that path. Those are different timing and network-design questions."
pubDate: "2026-10-30"
status: "published"
canonical_id: "2026-10-30-psiquantum-optical-switch-network-design"
tags: ["SiliconPhotonics", "OpticalNetworking", "AIInfrastructure", "DataCenters", "Engineering", "TechMindHub"]
source_url: "https://www.psiquantum.com/news-import/psiquantum-unveils-optical-circuit-switch-technology-built-on-advanced-low-loss-silicon-photonics-platform"
cover_card: "https://media.techmindhub.cc/posts/psiquantum-optical-switch-network-design-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/psiquantum-optical-switch-network-design-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/psiquantum-optical-switch-network-design-og-web-v1.jpg"
domain: "photonics"
topic: "Optical network switching"
card_alt: "Conceptual photonic switching chip with luminous paths and the words Routing Light."
cover_alt: "Conceptual distinction between a carrying optical path, circuit reconfiguration and losses across a complete link."
---

An optical circuit can carry signals along a selected path without converting them to electrical signals inside that switching stage. The network still needs to decide when to change the path, where to send traffic that does not fit it and whether enough optical power reaches the receiver.

On October 28, 2026, [PsiQuantum unveiled](https://www.psiquantum.com/news-import/psiquantum-unveils-optical-circuit-switch-technology-built-on-advanced-low-loss-silicon-photonics-platform) an **8×8 optical circuit-switching demonstrator** based on its silicon photonics platform. The company reports typical laboratory results of **1.2 dB insertion loss** and **less than three milliseconds of reconfiguration time**, without optical amplification. Its [technical page](https://www.psiquantum.com/optical-circuit-switching) describes a device with no moving parts in which every input can reach every output. Samples are being shared with selected prospective customers, while commercial products remain forthcoming.

These are company-reported component measurements. They are not independently verified results from a running AI cluster, and an 8×8 demonstration does not establish the behaviour of a larger device or a network with multiple switching stages.

## Carrying a signal and changing its route

Our engineering assessment starts with a timing distinction. Once a circuit is established, traffic travels over that path. The reported sub-three-millisecond figure describes **reconfiguration**, not a delay added to every packet traversing a stable connection. An optical circuit switch does not replace the per-packet forwarding, buffering or inspection performed by an electronic packet switch.

The suitability of a circuit depends on traffic shape. A large transfer that can use one path for a substantial interval has a different scheduling problem from many short, unpredictable exchanges among destinations. A useful evaluation would measure how often the topology changes, how much traffic waits during transitions and how much of the workload can use the available circuits. The controller's decisions become part of network performance.

The switch also needs a plan for demand outside the current topology. That could involve electronic switching elsewhere in the network, a different circuit arrangement or a queue in an adjacent system. The right choice depends on the application and network architecture; the photonic component's loss number does not answer it.

## Budget the entire optical path

Insertion loss measures power lost through this component. A deployed link includes other components, fiber and connections, and losses can accumulate across stages. The receiver's requirements and operating margin determine whether the resulting path is reliable. PsiQuantum's reported 1.2 dB therefore addresses one important constraint, not the reach or reliability of a complete network.

An AI infrastructure comparison should hold traffic patterns constant and examine workload completion time, network power, disruption during reconfiguration and recovery from faults. It should also record the controller policy and the full optical budget. That separates a promising low-loss component from a proven improvement for a specific cluster.

PsiQuantum's demonstrator makes a possible connection between quantum-derived photonics manufacturing and AI networking concrete. The practical benefit will depend on the device, scheduling software and workload operating together.

## Sources

- [PsiQuantum announcement](https://www.psiquantum.com/news-import/psiquantum-unveils-optical-circuit-switch-technology-built-on-advanced-low-loss-silicon-photonics-platform)
- [Optical circuit switching technical page](https://www.psiquantum.com/optical-circuit-switching)
