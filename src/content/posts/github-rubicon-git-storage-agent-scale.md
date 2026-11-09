---
title: "Project Rubicon: Why GitHub Separated Git Objects from Reference Consensus"
description: "GitHub reports 5,000 concurrent agents and 7,200 pushes per second to one repository in internal testing. Its new storage design separates immutable packs from atomic reference updates."
excerpt: "Git objects can be stored independently; branch pointers cannot be changed without agreement. Project Rubicon builds an architecture around that distinction."
pubDate: "2026-11-09T14:30:00Z"
status: "published"
canonical_id: "2026-11-09-github-rubicon-git-storage-agent-scale"
tags: ["Git", "DistributedSystems", "AIAgents", "GitHub", "CloudInfrastructure", "TechMindHub"]
source_url: "https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/"
cover_card: "https://media.techmindhub.cc/posts/github-rubicon-git-storage-agent-scale-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/github-rubicon-git-storage-agent-scale-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/github-rubicon-git-storage-agent-scale-og-web-v1.jpg"
domain: "infrastructure"
topic: "Git storage at agent scale"
card_alt: "Many independent Git branch paths approach a small reference coordination point above a broad field of stored packs."
cover_alt: "Conceptual Rubicon architecture showing durable immutable packs, a separate Ref-CAS metadata transaction, replaceable virtual replicas and background compaction."
---

Thousands of automated contributors can change the load profile of a single repository. A human team may produce a manageable sequence of pushes; many AI agents can simultaneously create branches, upload packs and trigger CI reads. In [its November 5 engineering account](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/), GitHub says internal testing of Project Rubicon supported 5,000 concurrent agents and 7,200 pushes per second to one repository while continuing to serve reads with low latency. Those are infrastructure workload results, not evidence that thousands of agents can usefully collaborate on one software design.

The architectural idea is more instructive than the headline throughput. Git objects are immutable and identified by content. Independent writers can store different objects without ordering every write through a shared lock. References such as branch names are mutable: two pushes racing to move the same reference require a decision about which expected old value is still valid. GitHub has separated the large object path from that small coordination problem.

## What needs agreement?

In the new design, a push reaches a virtual replica through GitHub's routing layer, Spokes. The replica indexes the incoming pack and uploads it to Azure Blob Storage first. It then commits a transaction through Ref-CAS, GitHub's replicated reference compare-and-swap service. That transaction updates the appropriate references **and the pack manifest**, the list of packs making up the repository. The ordering matters: a committed reference should point only to objects that have already become durable. The infographic is a conceptual account of these paths, not a vendor deployment diagram.

Ref-CAS commits by quorum and checks the expected prior value of each reference touched by a transaction. Different agents usually push to different branches, so their reference updates can proceed without conflicting. If two writes target the same branch pointer, one can commit and the other must handle the changed value. Coordination is therefore scoped to the mutable state that actually needs it, not to every byte of the repository.

This is more precise than saying that only references are stored in Ref-CAS. GitHub also keeps the pack manifest there, while packs, indexes and other large immutable data live in Blob Storage. The important boundary is between durable object data and the small atomic metadata update that makes it visible.

## Reads and maintenance after the split

Virtual replicas serve requests using local caches, but the cache is replaceable. On a read, a replica checks its reference version with Ref-CAS. If it is current, the version check can return without retransmitting the reference set. If it is behind, it receives current reference and pack information and fetches the packs it needs from Blob Storage. GitHub can add replicas for a busy repository without treating each replica's disk as the authoritative copy.

Every push adds another pack. A design that scales writes but allows pack count to grow indefinitely would slowly make reads more expensive. Rubicon therefore moves compaction and garbage collection to separate background workers. Workers lease shards, combine packs, check that a compacted output contains the same objects, publish the replacement and retire inputs later. Maintenance can scale independently of the request-serving replicas.

GitHub describes two earlier reference-storage approaches that exposed the trade-off. A single conditional-write blob kept reads simple but serialized writes; sharding references over many blobs improved write concurrency while forcing readers to check multiple segments. Ref-CAS is a dedicated replicated log intended to keep both reference updates and version checks practical under high concurrency. The underlying engineering problem is not merely storage capacity; it is where agreement is unavoidable and how much work each reader must do to observe it.

## What the benchmark does and does not show

The 5,000-agent and 7,200-push figures come from GitHub's internal tests. The article does not provide an independent benchmark protocol or a general service-level guarantee for arbitrary repositories. A push rate is not a code-quality measure, nor does it tell us how branch conflicts, review queues, CI capacity or human oversight would behave if thousands of agents worked on related changes.

The rollout is incremental. GitHub presents partial replicas, fetching individual objects without full packs, and other improvements as future work. It would be premature to describe those capabilities as already deployed for every repository. What the reported architecture does establish is a useful distributed-systems lesson: keep immutable data on a broad scalable path, and make the narrow mutable state explicit enough to coordinate correctly.

Source: [GitHub Engineering, November 5, 2026](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/).
