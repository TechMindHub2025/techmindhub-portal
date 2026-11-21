---
title: "AWS STS Adds Scoped Credentials for Agents: Permission Within Permission"
description: "GetScopedCredentials derives a narrower temporary session from an existing one, giving delegated work a bounded identity without a new role per task."
excerpt: "A scope-down policy intersects the existing session permissions; it cannot grant what the original session lacks."
pubDate: "2026-11-21T08:08:00Z"
status: "published"
canonical_id: "2026-11-21-aws-sts-scoped-credentials-agents"
tags: ["AWS", "IAM", "AgentSecurity", "LeastPrivilege", "TechMindHub"]
source_url: "https://aws.amazon.com/blogs/security/scope-down-permissions-of-existing-sessions-using-aws-sts-getscopedcredentials/"
cover_card: "https://media.techmindhub.cc/posts/aws-sts-scoped-credentials-agents-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/aws-sts-scoped-credentials-agents-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/aws-sts-scoped-credentials-agents-og-web-v1.jpg"
domain: "digital-trust"
topic: "Scoped agent credentials"
card_alt: "Two permission areas intersect between a human operator and an AI agent."
cover_alt: "The permitted scope of a derived AWS session is shown as the intersection of its original rights and a restrictive policy."
---

An agent that can call cloud APIs should not automatically inherit every permission of the process that started it. AWS's [November 20 technical guide](https://aws.amazon.com/blogs/security/scope-down-permissions-of-existing-sessions-using-aws-sts-getscopedcredentials/) introduces STS `GetScopedCredentials`, an API for deriving temporary credentials from an existing temporary session. The new effective permissions are the **intersection** of the parent session's permissions and a supplied scope-down policy. That operation can narrow authority but cannot enlarge it.

## Delegation at execution time

Consider an orchestration service with permission to read several S3 buckets. One sub-agent needs to inspect a single dataset; another needs to write a result to a specific prefix. The service can issue separately scoped temporary credentials for each task without maintaining a dedicated IAM role for every combination. The application should still choose a restrictive parent role, check the policy it constructs and avoid handing credentials to code that does not need them.

This is an identity boundary, not a general-purpose sandbox. It does not restrict arbitrary local file operations, prevent an agent from mishandling data it is authorized to read, or repair an overly broad parent policy. A compromised parent session may retain its original authority. Revocation strategy, expiry, logging and the provenance of task instructions remain part of the design.

## Constraints worth testing

At launch, AWS documents limits including **2,048 characters** for the scope-down policy and restrictions on successive scoping. Teams should test their policy size, session chain, denied calls and audit trail before deploying this in a multi-tenant workflow. A useful acceptance test asks whether a derived credential can perform only its intended operation while both access to unrelated resources and attempts to widen permission fail.

Source: [AWS Security Blog, November 20, 2026](https://aws.amazon.com/blogs/security/scope-down-permissions-of-existing-sessions-using-aws-sts-getscopedcredentials/).
