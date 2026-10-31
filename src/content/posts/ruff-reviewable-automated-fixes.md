---
title: "Ruff: Make Automated Code Changes Reviewable"
description: "Ruff separates inspection, safe automatic fixes and verification. A small rule set and reviewable diff help teams apply routine corrections without losing sight of behaviour."
excerpt: "A clean lint result confirms enabled checks passed. Automated fixes still need a reviewed diff and tests relevant to the changed behaviour."
pubDate: "2026-10-31"
status: "published"
canonical_id: "2026-10-31-ruff-reviewable-automated-fixes"
tags: ["Python", "OpenSource", "DeveloperTools", "CodeQuality", "SoftwareEngineering", "TechMindHub"]
source_url: "https://github.com/astral-sh/ruff/releases/tag/0.17.3"
cover_card: "https://media.techmindhub.cc/posts/ruff-reviewable-automated-fixes-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/ruff-reviewable-automated-fixes-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/ruff-reviewable-automated-fixes-og-web-v1.jpg"
domain: "software"
topic: "Reviewable code fixes"
card_alt: "Purple editorial code diff inspected with a magnifying glass under the words Review the Diff."
cover_alt: "Conceptual three-stage workflow for inspecting Ruff findings, reviewing an automatic fix and verifying relevant behaviour."
---

As of October 31, 2026, [Ruff's repository](https://github.com/astral-sh/ruff) lists version [0.17.3](https://github.com/astral-sh/ruff/releases/tag/0.17.3), with release notes dated October 26. Ruff is a maintained Python linter and formatter. Its useful operational distinction is that identifying a problem, rewriting a file and confirming the application still behaves correctly are separate steps.

With Ruff installed, start by inspecting a repository without changing its files:

```sh
ruff check .
ruff format --check .
```

The first command reports violations of enabled lint rules; the second checks formatting without rewriting files. The result depends on the project's configuration and Ruff version. Record both in the project so local runs and continuous integration use the same expectations.

For lint violations with available fixes, the next command applies fixes under the configured safety policy:

```sh
ruff check --fix .
```

By default, Ruff applies fixes classified as **safe**, intended to preserve runtime behaviour. Unsafe fixes require explicit opt-in and may change behaviour or remove comments. The distinction is concrete: [Ruff's documentation](https://docs.astral.sh/ruff/linter/) describes changing `list(...)[0]` to `next(iter(...))`. On an empty input, the exception changes from `IndexError` to `StopIteration`; a caller catching the former could then behave differently. That fix is classified as unsafe. Version 0.17.3 also fixes an incorrect f-string conversion in one lint rule; preview features remain separately opt-in.

## Make the changed behaviour visible

Our engineering assessment is to begin with a small, agreed rule set in an existing codebase. Run the read-only checks first, decide which findings belong to the intended change, then apply automatic fixes in a reviewable batch. Separate large formatting sweeps from application logic changes so a reviewer can find the altered behaviour.

Inspect the diff after every fix run. A safety classification describes the tool's intended transformation, not a proof that every application assumption has been preserved. Run tests relevant to the changed code path, especially where exception handling, string contents or data transformation are involved. If an unsafe fix is proposed, review it as a deliberate behaviour change and opt in only for that scoped case.

An automated gate can repeat the read-only checks for every pull request. That makes the configured expectations visible and consistent, but a passing result has a defined boundary: enabled lint and format checks passed. It cannot show that a business rule is correct, a dataset is complete or an integration covers every failure.

Ruff is most valuable when routine corrections are easy to repeat and the resulting changes remain easy to inspect. Reviewers can then devote their attention to decisions that require knowledge of the actual application.

## Sources

- [Ruff project](https://github.com/astral-sh/ruff)
- [Release 0.17.3](https://github.com/astral-sh/ruff/releases/tag/0.17.3)
- [Linter documentation and fix safety](https://docs.astral.sh/ruff/linter/)
