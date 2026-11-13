---
title: "GitHub Actions Is Retiring ARM32 Jobs on Hosted Linux and Windows Runners"
description: "The December 8 deadline calls for an audit of native AArch32 execution, action runtimes and alternative test environments."
excerpt: "The hosted-runner change affects ARM32 execution, not the possibility of producing ARM32 binaries by cross-compilation."
pubDate: "2026-11-13T15:31:00Z"
status: "published"
canonical_id: "2026-11-13-github-actions-arm32-hosted-retirement"
tags: ["GitHubActions", "ARM32", "CICD", "EmbeddedDevelopment", "TechMindHub"]
source_url: "https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/"
cover_card: "https://media.techmindhub.cc/posts/github-actions-arm32-hosted-retirement-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/github-actions-arm32-hosted-retirement-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/github-actions-arm32-hosted-retirement-og-web-v1.jpg"
domain: "software"
topic: "ARM32 CI migration"
card_alt: "An embedded development bench and CI pipeline branch from hosted ARM32 execution toward a separately tested alternative."
cover_alt: "A conceptual checklist separates hosted-runner ARM32 execution, Node 24 action runtime and ARM32 target binaries, then tests an alternative path."
---

A CI pipeline can build for a processor without running on that processor. That distinction matters in [GitHub's November 12 retirement notice](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/): GitHub-hosted Actions runners on Linux and Windows will end support for **ARM32 job execution by December 8, 2026**. The change includes native AArch32 user-space execution on those hosted runners.

GitHub links the retirement to its move away from Node.js 20. Node.js 24 does not support ARM32. The separate [Node 20 retirement notice](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/) says Actions runners already use Node 24 for JavaScript actions and that self-hosted ARM32 runners are no longer supported. December 8 is therefore a deadline for the remaining hosted-runner execution path described in the newer notice, **not a future date for the entire Node runtime transition**.

## Three layers to inventory

First, identify where a workflow executes: the architecture and operating system of its runner. Second, inspect JavaScript actions and their runtime requirements. Third, distinguish the architecture of the *artifact* being built from the architecture needed to execute tests. A Linux x86-64 runner might cross-compile an ARM32 binary without running ARM32 user-space code. Native or integration tests of that binary still need a suitable environment.

This makes a repository-wide search for an ARM32 label only a starting point. Teams should inspect matrices, containers, scripts, emulators, toolchains, third-party actions and the runners on which tests actually execute. Record any dependency on AArch32 execution within the hosted job. Test the replacement pipeline before the deadline with representative binaries, ABI dependencies and the same validation gates used for releases.

## Choosing a path

Possible approaches include cross-compiling on a supported runner and testing on dedicated devices or another eligible environment. The right arrangement depends on required operating system behavior, toolchain, emulator fidelity, performance and access to hardware. Moving a build step alone does not establish that an end-to-end ARM32 workflow is reproducible.

GitHub's brief notice does not prescribe a universal replacement or quantify the number of affected projects. It concerns hosted Linux and Windows ARM32 job execution and must not be read as the end of ARM32 software development. The earlier Node 24 change also limits what can be inferred about self-hosted runner support. Each team needs to verify its actual runner and test architecture rather than assume a particular workaround will pass.

Sources: [GitHub Changelog, November 12, 2026](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/) and [Node 20 retirement notice](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/).
