---
title: "Prometheus 3.16: Making PromQL Query Cost Visible and Bounded"
description: "Prometheus 3.16 adds experimental query-cost estimation, actual cost reporting and configurable execution limits. The mechanism requires an explicit feature flag and careful rollout."
excerpt: "A PromQL query can fan out across more samples than its short expression suggests. New experimental controls expose and bound some of that work."
pubDate: "2026-11-09T14:28:00Z"
status: "published"
canonical_id: "2026-11-09-prometheus-316-query-cost-controls"
tags: ["Prometheus", "PromQL", "Observability", "Monitoring", "CloudInfrastructure", "TechMindHub"]
source_url: "https://github.com/prometheus/prometheus/releases/tag/v3.16.0"
cover_card: "https://media.techmindhub.cc/posts/prometheus-316-query-cost-controls-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/prometheus-316-query-cost-controls-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/prometheus-316-query-cost-controls-og-web-v1.jpg"
domain: "software"
topic: "PromQL resource budgets"
card_alt: "Purple time-series traces fan out across a monitoring landscape toward a conceptual resource-budget boundary."
cover_alt: "Conceptual comparison of narrow and broad PromQL workloads, followed by cost estimation, a configurable execution limit and actual cost reporting."
---

A PromQL expression can be short and still be expensive to execute. A broad metric selector may touch many series; a long range and nested subqueries can make the work much larger than the query's visible length suggests. In a shared monitoring service, one costly query can affect other users' experience. The problem is resource predictability, not simply query syntax.

[Prometheus 3.16.0](https://github.com/prometheus/prometheus/releases/tag/v3.16.0) introduces experimental query-cost estimation, actual cost reporting and configurable execution limits. The release was published on GitHub on November 5, 2026, although its release title says November 4. The functionality is enabled explicitly with `--enable-feature=query-cost`; it is not a default production policy for every installation.

## Three different questions about cost

An estimate before or around planning asks how much work a query is likely to require. A configured limit asks whether execution should be allowed to consume that budget. Actual-cost reporting asks what work the completed or stopped query really performed. These three quantities should not be collapsed into one precise prediction: data distribution, selector cardinality, range length and query shape can make actual work differ from the estimate. The infographic illustrates the distinctions, not a measured benchmark.

For operators, the value lies in making expensive requests inspectable and setting boundaries appropriate to their own workloads. An investigation dashboard may deliberately run wider queries than a frequent alert evaluation. A limit tuned only against a quiet development dataset may be too low for an incident, while a generous limit may offer little protection from unbounded queries. The release notes establish the existence of controls; they do not prescribe a universal safe threshold.

A cautious rollout starts with a representative inventory: alert rules, recording rules, dashboard panels, ad hoc investigation queries and API clients. Record the reported cost of typical and worst legitimate requests, including long historical windows and high-cardinality selectors. Evaluate a candidate budget against those workloads before using it to reject work. If a limit is crossed, the user needs an actionable error and an alternate way to narrow the query, rather than a silent loss of monitoring data.

## What else changes in 3.16

The release also adds an experimental `integral()` function behind a separate `promql-experimental-functions` flag. Smoothed and anchored vector selectors become stable and always on. A request can override PromQL Start Timestamp processing using the `X-Prometheus-Use-Start-Timestamps` header. These are separate changes; enabling query-cost does not imply enabling all experimental PromQL behavior.

Upgrade testing deserves attention beyond the headline feature. The release changes how subquery samples contribute to `TotalSamples` and related statistics, adjusts experimental search API behavior and stops exposing some deprecated Remote Write 2.0 queue metrics. A dashboard or automation that relies on the old measurements can change even if no one enables query-cost controls. Review the full release notes for the features in use, then test production-like queries and monitoring of the monitoring stack itself.

## The practical boundary

A query-cost limit is a way to constrain work, not a mechanism that makes a slow query fast. It also does not fix an underlying metric with uncontrolled label cardinality or eliminate the need for recording rules, retention decisions and thoughtful dashboard design. Because the mechanism is experimental, operators should validate its reporting semantics and error behavior against their own Prometheus deployment before using it as a multi-tenant guarantee.

Source: [Prometheus 3.16.0 release notes](https://github.com/prometheus/prometheus/releases/tag/v3.16.0).
