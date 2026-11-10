---
title: "mailcow's Moovember 2026 Release: Securing Administration and Connecting Mail Identity"
description: "The self-hosted mail release fixes an authenticated administrator RCE, introduces mailbox groups and identity-provider sync, and changes migration APIs and request limits."
excerpt: "The mailcow update combines a security fix with a broader identity model. Operators should back up first and test their migration clients and size limits."
pubDate: "2026-11-10T21:11:00Z"
status: "published"
canonical_id: "2026-11-11-mailcow-moovember-2026-identity-security"
tags: ["SelfHosted", "EmailSecurity", "IdentityManagement", "OpenSource", "TechMindHub"]
source_url: "https://github.com/mailcow/mailcow-dockerized/releases/tag/2026-11"
cover_card: "https://media.techmindhub.cc/posts/mailcow-moovember-2026-identity-security-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/mailcow-moovember-2026-identity-security-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/mailcow-moovember-2026-identity-security-og-web-v1.jpg"
domain: "software"
topic: "Self-hosted mail and identity"
card_alt: "A self-hosted mail cabinet with an identity gate, mailbox drawers and a scoped key."
cover_alt: "Conceptual cutaway connecting an identity provider to mailbox groups while separating administrative access, scoped API keys and update preparation."
---

A self-hosted mail system has several overlapping boundaries: users sign in, administrators manage domains, applications use API keys, and migration jobs connect to external providers. The [mailcow Moovember 2026 release](https://github.com/mailcow/mailcow-dockerized/releases/tag/2026-11), published November 5, changes several of those boundaries at once. It is also an important security update.

The maintainers say it fixes, among other issues, a **remote-code-execution vulnerability exploitable by authenticated administrators and domain administrators**. That qualifier matters: the release note does not describe an unauthenticated attack. The maintainers recommend updating promptly and limiting access to those administrative accounts until an update is possible. They said details of the fixed issues would follow; the release notes do not yet provide enough information to assess their exploitability beyond the stated conditions. The release includes SOGo 5.12.13, an upstream security update.

## Identity becomes more explicit

Mailbox groups can act as distribution lists and grant access to shared mailboxes, calendars and address books. Members can span managed domains. A shared mailbox has no independent login; members reach it through the group. Domain administrators receive a specific group-management permission.

Groups and members can now synchronize from Keycloak or LDAP/Active Directory. There is an **optional, default-off offboarding behavior**: disabling or deleting a user at the identity provider can disable mailbox login while mail delivery continues. That distinction helps avoid treating access revocation and mailbox retention as the same operation, but it requires a locally reviewed policy for former users and shared resources.

API keys can have descriptions, read-only or read-write access, and individual IP allowlists. Migration sources can be reused across jobs; OAuth2/XOAUTH2 is supported for Microsoft 365 and Google migrations. These features can reduce reliance on shared credentials, provided operators actually assign narrower access and manage token lifecycles. Fail2ban now counts failed logins across IMAP, POP3, SMTP, Sieve, EAS and DAV, and the release adds a two-factor-authentication rate limit.

The cutaway illustration is a conceptual account of identity and authority boundaries, not a literal mailcow deployment or user interface. Its operational question is which external identities may reach which mailboxes and administrative functions after synchronization.

## An update that needs a migration plan

The maintainers explicitly call for a **backup before updating**. The `add/syncjob` API now requires `source_id` instead of embedded server fields. Existing jobs are migrated, but clients that create or read jobs through the API need changes. UI and API request bodies are limited to 64 MB. SOGo, EAS and DAV use `NGINX_MAX_BODY_SIZE` (default `128m`); operators with a larger Postfix message limit must align that setting or large webmail/ActiveSync sends can fail. Custom nginx locations also gain a 64 MB limit and may reject larger uploads with HTTP 413 unless explicitly configured.

Before rollout, inventory administrative and domain-admin accounts, sync-job API clients, custom nginx locations, message-size policy, identity-provider group mappings and API keys. Test a restored backup and representative mail flows in a staging environment where possible. The release documents features and fixes, but it does not establish that every existing integration will work unchanged, nor does it provide independent measurements of security improvement.

Source: [mailcow-dockerized release 2026-11, November 5, 2026](https://github.com/mailcow/mailcow-dockerized/releases/tag/2026-11).
