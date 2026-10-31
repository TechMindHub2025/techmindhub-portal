---
title: "Sandman: Who Cleans Up When an AI Training Job Stops Waiting?"
description: "Amazon's Sandman preprint describes Kubernetes sandboxes for agent training. Its operational lesson is that a cancelled request does not end the resource's lifecycle."
excerpt: "A timed-out sandbox request may still create a pod. Ownership, reconciliation and confirmed deletion are essential when agent-training jobs retry at scale."
pubDate: "2026-10-31"
status: "published"
canonical_id: "2026-10-31-sandman-sandbox-lifecycle"
tags: ["AgenticAI", "Kubernetes", "AIInfrastructure", "DistributedSystems", "Engineering", "TechMindHub"]
source_url: "https://arxiv.org/abs/2610.39711"
cover_card: "https://media.techmindhub.cc/posts/sandman-sandbox-lifecycle-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/sandman-sandbox-lifecycle-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/sandman-sandbox-lifecycle-og-web-v1.jpg"
domain: "infrastructure"
topic: "Sandbox lifecycle"
card_alt: "Conceptual blue Kubernetes sandboxes with a late pod and a reconciliation path under the words Who Cleans Up."
cover_alt: "Conceptual sequence of request, timeout and retry, reconciliation of late sandboxes and confirmed deletion."
---

A [preprint submitted October 29, 2026](https://arxiv.org/abs/2610.39711) describes Sandman, a sandbox service Amazon built for agentic reinforcement-learning workloads on shared Kubernetes infrastructure. A training framework requests a task environment, executes commands and file operations over multiple tool calls, and releases the environment when finished. The engineering problem is not just starting a command: thousands of persistent environments need to be created, tracked and eventually reclaimed.

Each sandbox is an ordinary Kubernetes pod using the task's image with a small execution daemon. Sandman's provider owns a creation attempt until it hands over a usable pod or deletes it, even if the caller times out or cancels its wait. The authors report a controlled scale test with **11,858 concurrent tiny sandboxes**. Those pods had small resource requests and a cached image; the figure is a result for that configuration, not capacity for arbitrary workloads.

The paper describes internal model-development infrastructure, not a public service with an external service-level agreement. Its daemon, provider and pool are promised for open-source release, rather than already available as part of this report. The authors also accept containers' shared host kernel and explicitly do not claim isolation against a malicious co-tenant.

## A request can end before its pod does

Our engineering assessment starts with a timing gap. Imagine a worker asking for an environment. The Kubernetes API accepts the creation request, but the pod becomes ready after the worker's deadline. The worker retries. Unless something reconciles the first request, the cluster may now hold resources for two attempts while the caller thinks one failed.

This is not merely hypothetical failure framing. The paper records an incident in which cancelled creates leaked pods because cleanup caught errors but not cancellation; a subsequent direct create added further pods. The authors' ownership rule addresses that class of problem by keeping responsibility for the accepted creation until it is handed off or removed. It does not make the cost of waiting or temporary late pods disappear.

[Kubernetes owner references and cascading deletion](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) connect dependent objects to an owner and support cleanup when that owner is deleted. They do not automatically resolve an application timeout while the owner remains alive. The application has to decide whether a late pod should be handed to a waiting request, retained briefly, or deleted, and confirm the outcome.

A useful acceptance test interrupts acquisition before submission, after API acceptance and during deletion. After each interruption, reconcile the intended environments against actual pods, including pods that became ready after their callers stopped waiting. Record unresolved acquisitions, late resources, retries and deletions awaiting confirmation alongside startup latency.

Sandman illustrates why throughput and lifecycle accounting belong in the same evaluation. A system can start many sandboxes and still lose capacity to abandoned ones. At larger scale, operators need to explain which environments exist, who owns them and what will remove them.

## Sources

- [Sandman preprint and full text](https://arxiv.org/abs/2610.39711)
- [Kubernetes garbage collection and owner references](https://kubernetes.io/docs/concepts/architecture/garbage-collection/)
