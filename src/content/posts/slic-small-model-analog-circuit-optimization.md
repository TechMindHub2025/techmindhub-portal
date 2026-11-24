---
title: "Can a Small AI Model Design Analog Circuits? SLIC Tests the Simulator Loop"
description: "MIT, Analog Devices and IBM Research train a locally deployable model to iteratively optimize analog circuits against simulator feedback. The measured success has a defined benchmark scope."
excerpt: "A four-billion-parameter model learns from circuit simulations, but a passing simulated design is not fabricated silicon."
pubDate: "2026-11-25T07:05:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/slic-small-model-analog-circuit-optimization-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/slic-small-model-analog-circuit-optimization-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/slic-small-model-analog-circuit-optimization-og-web-v1.jpg"
card_alt: "Conceptual analog circuit and a small model connected in a simulation feedback loop."
cover_alt: "Conceptual flow from design targets through a small model and circuit simulator, with feedback for revision."
canonical_id: "2026-11-25-slic-small-model-analog-circuit-optimization"
tags: ["Semiconductors", "ElectronicDesignAutomation", "SmallModels", "CircuitSimulation", "TechMindHub"]
source_url: "https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123"
domain: "ai"
topic: "Analog circuit optimization"
---

Analog circuit design is a repeated negotiation among gain, bandwidth, power and area. Changing one transistor dimension can improve one specification while making another worse. MIT, Analog Devices and IBM Research describe [SLIC, Small LM Iterating on Circuits](https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123), as a way to train a compact language model for this kind of closed-loop optimization. The MIT account appeared on November 23; the [research manuscript](https://arxiv.org/abs/2611.13452) provides a more precise view of the tests.

## What the model actually changes

SLIC receives a structured representation of a circuit, target specifications, device parameters and the latest simulator measurements. It proposes relative changes to parameters such as transistor sizing and bias, runs another simulation, then uses the feedback to decide what to try next. Its training combines supervised examples with reinforcement learning guided by verifiable simulation outcomes. The researchers describe a roughly **four-billion-parameter** model that can run locally, a relevant property when proprietary process design kits cannot be sent to a hosted model.

This is parameter optimization within a specified circuit topology, rather than the automatic invention and physical validation of an entire chip. The released benchmark contains **41 amplifier topologies**. Under one in-distribution protocol, the authors report **87.1% Pass@1 within eight turns** across four design specifications; their held-out topology and cross-node results use different tests and should not be merged into one success rate. The MIT account says the small model came close to a frontier model on the tested circuit task. That is narrower than a general claim that small models beat frontier LLMs in engineering.

## Why feedback changes the economics

The useful unit of comparison is not parameter count alone. An engineer needs to know how many simulations, how much computation and human review are required to reach an acceptable circuit, and whether the process handles a genuinely new topology or process node. Local inference can also keep design inputs inside a controlled environment. These are plausible advantages of specialization, but operational cost and data-governance claims need a real deployment comparison.

The study reports transfer to previously unseen technology nodes, including a commercial process kit, under its evaluation conditions. A circuit that passes the authors' simulator-based targets has **not** thereby passed layout, parasitic extraction, process-voltage-temperature corners, fabrication and silicon measurement. Multi-block coordination and full chip validation remain separate engineering tasks. The central lesson is that a small model can learn a useful iterative policy when the environment returns measurable feedback; its limits are set by the design space and the quality of that feedback.

Sources: [MIT News, November 23, 2026](https://news.mit.edu/2026/ai-driven-technique-could-help-engineers-design-analog-chips-faster-and-less-expensive-1123) and [SLIC research paper](https://arxiv.org/abs/2611.13452).
