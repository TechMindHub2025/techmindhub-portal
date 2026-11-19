---
title: "Inside the Codex Sandbox: Defining What a Coding Agent Can Reach"
description: "OpenAI describes Codex filesystem permissions, network proxy controls and OS-specific enforcement. The sandbox is one layer in an agent security model."
excerpt: "The useful security boundary is the authority a launched command inherits across files, network and child processes."
pubDate: "2026-11-19T06:20:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/openai-codex-sandbox-architecture-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/openai-codex-sandbox-architecture-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/openai-codex-sandbox-architecture-og-web-v1.jpg"
card_alt: "Conceptual isolated agent workspace and controlled network aperture beneath the words Boundaries for Agents."
cover_alt: "Conceptual coding-agent workspace with separate file permission and network policy boundaries."
canonical_id: "2026-11-19-openai-codex-sandbox-architecture"
tags: ["DigitalTrust", "AIAgents", "Sandbox", "DeveloperSecurity", "TechMindHub"]
source_url: "https://openai.com/index/inside-the-codex-sandbox/"
domain: "digital-trust"
topic: "Coding agent sandbox permissions"
---

A coding agent can run build scripts, inspect files and call development tools. The relevant security question is what authority those commands and their descendants inherit. In a [November 18 technical account](https://openai.com/index/inside-the-codex-sandbox/), OpenAI described how Codex defines filesystem and network permissions and enforces them across macOS, Linux and Windows.

The default workspace-oriented profile allows useful project work while restricting access outside specified roots and limiting certain sensitive paths. Policies can give particular paths read or write access. Network access may be disabled, enabled directly, or sent through a policy-aware proxy with domain rules. This is a configured boundary: its protection depends on the chosen profile and how commands are launched.

## Execution boundary, not a model promise

The harness applies a permission profile when it launches a command, so an attempted file write or network call is checked by operating-system mechanisms rather than by the model's intention. OpenAI describes Seatbelt on macOS, Linux isolation including namespaces and seccomp, and Windows-specific enforcement. The network proxy shares policy logic while its connection to the sandbox differs by platform.

This distinction matters when an agent encounters untrusted repository scripts or dependencies. A prompt saying “do not read that directory” is not an access control. A file rule that actually denies the read is. A proxy that limits destinations can reduce the reach of network-capable commands, although teams still need to check how package managers, local services and tools behave under those rules.

The report also calls out a boundary in its own example: a stdio MCP server started by the harness is not automatically sandboxed, because its required access cannot always be inferred. It can instead be wrapped explicitly with the sandbox command and a purpose-built profile. That operational detail is important for organizations treating external tools as part of an agent's attack surface.

OpenAI's description is an architectural account, not an independent penetration test. Sandbox rules reduce potential damage but do not prove immunity to prompt injection, malicious packages, misconfiguration or permissions deliberately granted outside the boundary. Security review should test the actual profile and tool chain in use.

## Source

- [OpenAI: Inside the Codex sandbox, November 18, 2026](https://openai.com/index/inside-the-codex-sandbox/)
