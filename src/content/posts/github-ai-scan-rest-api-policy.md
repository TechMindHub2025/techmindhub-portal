---
title: "GitHub AI Scan Gets REST API Controls for Repository Security"
description: "The repository_scan setting makes organization-wide rollout scriptable, while enterprise policy, repository opt-outs and paid on-demand execution define its limits."
excerpt: "Central configuration can make AI Scan coverage auditable. Enabling it still does not run a scan."
pubDate: "2026-11-14T13:32:00Z"
status: "published"
canonical_id: "2026-11-14-github-ai-scan-rest-api-policy"
tags: ["GitHub", "DevSecOps", "AIScan", "PolicyAsCode", "TechMindHub"]
source_url: "https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/"
cover_card: "https://media.techmindhub.cc/posts/github-ai-scan-rest-api-policy-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/github-ai-scan-rest-api-policy-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/github-ai-scan-rest-api-policy-og-web-v1.jpg"
domain: "digital-trust"
topic: "AI Scan policy automation"
card_alt: "A conceptual organization security control distributes an AI Scan setting to repositories, with one repository opting out."
cover_alt: "A conceptual policy hierarchy shows enterprise restrictions, organization and repository settings, and a separate on-demand scan that uses AI credits."
---

Turning on a security setting and performing a security scan are different operations. [GitHub's November 13 announcement](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/) adds `repository_scan` to the existing REST API endpoints for AI Scan at organization and repository level. Administrators can now configure the availability of repository scans through scripts or infrastructure as code, instead of editing each repository's settings manually.

The `GET` and `PATCH` endpoints are `/orgs/{org}/code-scanning/ai-scan` and `/repos/{owner}/{repo}/code-scanning/ai-scan`. The new property accepts `enabled` or `disabled`, alongside the existing `pr_scan` property for pull-request scanning. This is a control-plane change: it can make a rollout more repeatable and easier to inspect, but it does not establish that the repositories have been scanned or that findings have been addressed.

## A policy hierarchy with an explicit failure mode

An organization that disables AI Scan for repositories prevents its repositories from enabling it. When the organization enables the setting, repositories inherit it and can opt out individually. An enterprise policy must first permit AI Scan; attempts to enable it against a blocking enterprise policy return HTTP `422`. If one of two settings in a combined `PATCH` request is blocked, neither setting changes. Automation should treat that response as a policy conflict, then read back the effective configuration rather than report a successful rollout.

Organization owners and security managers can manage the organization setting; repository administrators can opt their repositories out. The scope is also narrower than "every GitHub repository": public repositories must be organization owned, while private or internal repositories require GitHub Code Security or GitHub Advanced Security. GitHub Enterprise Server is not supported by this public preview.

## The execution and cost boundary

Enabling `repository_scan` **does not start a scan**. A user with write access launches scans on demand, and each run consumes GitHub Code Security AI credits. A useful deployment inventory should therefore separate configured coverage, actual scan executions, credit consumption and the subsequent handling of results. Those are distinct measurements of operational use, not interchangeable indicators of security effectiveness.

For a practical rollout, teams can record their intended enterprise, organization and repository policies; apply changes with appropriate API credentials; inspect `422` responses; and compare a fresh read of settings with the intended state. They should budget and schedule on-demand scans separately. The announcement does not report independent measurements of AI Scan precision, false positives or vulnerability detection, so no quality conclusion follows from the new API control alone.

Sources: [GitHub Changelog, November 13, 2026](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/) and [GitHub REST API documentation](https://docs.github.com/en/rest/code-scanning/code-scanning).
