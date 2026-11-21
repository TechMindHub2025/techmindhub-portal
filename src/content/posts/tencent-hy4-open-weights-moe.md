---
title: "Tencent Hy4 Opens Its Weights: What 770B Total and 49B Active Mean"
description: "Hy4 combines a very large mixture of experts with sparse routing. Public weights permit evaluation, but license terms and deployment costs remain decisive."
excerpt: "The total parameter count describes stored capacity; the active count describes one token path through a subset of experts."
pubDate: "2026-11-21T08:04:00Z"
status: "published"
canonical_id: "2026-11-21-tencent-hy4-open-weights-moe"
tags: ["OpenWeights", "MixtureOfExperts", "Inference", "TencentHy4", "TechMindHub"]
source_url: "https://github.com/Tencent-Hunyuan/Hy4"
cover_card: "https://media.techmindhub.cc/posts/tencent-hy4-open-weights-moe-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/tencent-hy4-open-weights-moe-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/tencent-hy4-open-weights-moe-og-web-v1.jpg"
domain: "ai"
topic: "Sparse MoE inference"
card_alt: "A sparse routing path selects a few expert tiles from a large model matrix."
cover_alt: "A conceptual expert matrix shows selected routes alongside the model specification of 770B total and 49B active parameters."
---

Tencent's [Hy4 repository](https://github.com/Tencent-Hunyuan/Hy4) and [model files](https://huggingface.co/tencent/Hy4) make the large mixture-of-experts system inspectable and deployable under the **Tencent Hy License**. The stated architecture has **770 billion total parameters** and about **49 billion active per token**. Tencent [introduced the model earlier in November](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/); the exact public-weight release time should not be conflated with that initial announcement.

## Sparse computation is not a small model

An MoE router selects a subset of experts for each token. This reduces active computation relative to using all 770B parameters for every token, but storage, distribution across devices and memory traffic still depend on the full model and its inference stack. Tencent documents Gated DeepSeek Sparse Attention and speculative-decoding components intended to improve serving efficiency. Actual latency and cost depend on batching, context length, network topology, precision, kernels and how much of the model must reside in accelerator memory.

The diagram shows an explanatory route through a matrix of experts; it is not a measured internal trace. A useful evaluation would report quality and throughput at a specified context length, concurrency, hardware count, memory use and power draw, then compare those with a smaller dense model or another MoE at equal task quality.

## What 'open' allows

Available weights do not imply that the training data, full training process and every deployment dependency are open. Teams should read the Tencent Hy License before commercial use and test the actual downloadable artifacts and inference software. Benchmark numbers in project documentation are primarily vendor-reported; independent reproduction is needed before treating them as a general price-performance result.

Sources: [Tencent Hy4 GitHub repository](https://github.com/Tencent-Hunyuan/Hy4), [model repository](https://huggingface.co/tencent/Hy4) and [Tencent's earlier announcement](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/).
