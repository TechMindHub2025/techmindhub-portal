---
title: "Agents That Wait Without Running: Cloudflare's Pi 1.6 Runtime Change"
description: "Cloudflare Agents SDK 0.34.0 lets a Pi tool park until a signal, deadline or subagent result, allowing its Durable Object to hibernate while preserving state."
excerpt: "A waiting agent can retain its work without holding an active invocation."
pubDate: "2026-11-22T06:16:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/cloudflare-pi-agents-wait-without-running-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/cloudflare-pi-agents-wait-without-running-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/cloudflare-pi-agents-wait-without-running-og-web-v1.jpg"
card_alt: "A conceptual agent process waits at an event gate while its state remains stored."
cover_alt: "Conceptual sequence from a parked Pi tool to Durable Object hibernation and later resumption after a signal."
canonical_id: "2026-11-22-cloudflare-pi-agents-wait-without-running"
tags: ["AIAgents", "DurableObjects", "AgentRuntime", "Cloudflare", "TechMindHub"]
source_url: "https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/"
domain: "ai"
topic: "Durable agent execution"
---

An agent may spend more time waiting for an approval or another agent than generating its next answer. If that wait occupies a running invocation, the orchestration design ties up execution resources for no useful work. [Cloudflare's Agents SDK 0.34.0 update](https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/) upgrades `PiHarness` to Pi 1.6 and lets a tool **park** until a signal or deadline rather than returning a conventional result immediately.

While parked, the call holds no invocation and the Durable Object can hibernate. The application can later send `harness.signal()`; Pi runs the tool again when the signal arrives or the deadline passes. `submit()` and `continue()` can notify a waiting tool when another session settles. A `beforeTool` hook can also pause a tool before execution for human approval.

## The state has to survive the pause

This is more than adding a timer to a request. The agent must persist the transcript, queued input and enough information to resume the intended operation after its execution context disappears. Cloudflare's [Pi documentation](https://developers.cloudflare.com/agents/harnesses/pi/) describes the harness storing state in a Durable Object's SQLite database and waking the object when work returns. The update also allows root, created and forked sessions to start with an existing history, and can retain queued input across an abort.

The useful design boundary is between **durable state** and **active compute**. An approval flow can release its running invocation while the request remains pending; a subagent result becomes an event that wakes the right tool. Engineers still have to define timeouts, repeated signals, cancellation, idempotency and what happens when a resumed tool encounters a new failure.

Cloudflare does not provide a universal cost-saving figure. Hibernation during a wait does not make storage, wakeups, model calls or the rest of an application free. The Pi documentation also notes a compatibility constraint: once a conversation runs under Pi 1.6, rolling back to an SDK using Pi 1.5 can block subsequent tool calls and model requests. Migration and rollback planning therefore belong alongside any runtime-efficiency argument.

## Sources

- [Cloudflare: Agents SDK supports Pi 1.6, November 20, 2026](https://developers.cloudflare.com/changelog/post/2026-11-20-pi-harness-pi-1-6/)
- [Cloudflare: Pi harness documentation](https://developers.cloudflare.com/agents/harnesses/pi/)
