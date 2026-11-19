---
title: "Pelagos: GPU Scale for Quantum Error-Correction Research"
description: "IBM and AMD released an open-source framework for evaluating quantum error-correction decoders at scale. An eight-GPU speedup applies to a decoding stage, not an entire quantum computer."
excerpt: "Future quantum fault tolerance needs classical decoding research, and evaluating decoders can itself be a large HPC workload."
pubDate: "2026-11-19T06:17:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/ibm-amd-pelagos-quantum-decoder-evaluation-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/ibm-amd-pelagos-quantum-decoder-evaluation-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/ibm-amd-pelagos-quantum-decoder-evaluation-og-web-v1.jpg"
card_alt: "Conceptual error-pattern streams spread across compute islands beneath the words Decoding at Scale."
cover_alt: "Sampled quantum error patterns distributed to GPU decoding campaigns for statistical evaluation."
canonical_id: "2026-11-19-ibm-amd-pelagos-quantum-decoder-evaluation"
tags: ["Photonics", "QuantumComputing", "HPC", "OpenSource", "TechMindHub"]
source_url: "https://newsroom.ibm.com/blog-pelagos-accelerates-quantum-error-correction-decoding-at-scale"
domain: "photonics"
topic: "GPU-accelerated quantum decoder evaluation"
---

A quantum error-correction decoder infers likely errors from measured syndromes. Before such a decoder can be trusted in a future fault-tolerant system, researchers must evaluate it against many sampled error patterns. That validation is a substantial **classical computing** workload.

On November 16, [IBM and AMD released Pelagos](https://newsroom.ibm.com/blog-pelagos-accelerates-quantum-error-correction-decoding-at-scale), an open-source, GPU-accelerated framework for large-scale decoder evaluation. IBM says the framework is built with Triton and supports AMD and NVIDIA GPU environments. It is a research tool for comparing decoder approaches, not an announcement of an operational fault-tolerant quantum machine.

## What eight GPUs accelerated

IBM describes tests on AMD Instinct MI300X and MI355X accelerators. In the reported configuration, the **GPU decoding stage** achieved up to roughly **7.5× speedup across eight GPUs** relative to a single-GPU run. This is a stage-specific scaling result. End-to-end experiment time also includes sample generation, data movement, orchestration and analysis, so it cannot be inferred from that ratio alone.

The work focuses on improving coordination within a multi-GPU node through process-level orchestration, parallel host operations and shared-memory techniques. For large studies, researchers need enough samples to estimate low logical error rates; throughput and reproducibility of the evaluation campaign become as important as the performance of one decoder invocation.

Pelagos complements the recently announced ORNL–IBM–AMD co-design platform, which brings quantum hardware and AMD-powered HPC closer together. The evaluation framework and the platform address related but distinct problems: assessing candidate decoders at scale versus operating a low-latency quantum-classical workflow.

The published numbers are from the project team. Open code helps others inspect and reproduce the approach, but independent comparative runs, workload definitions and full-system latency measurements remain necessary before transferring the reported speedup to other codes, decoders or hardware.

## Source

- [IBM and AMD: Pelagos accelerates quantum error-correction decoding at scale, November 16, 2026](https://newsroom.ibm.com/blog-pelagos-accelerates-quantum-error-correction-decoding-at-scale)
