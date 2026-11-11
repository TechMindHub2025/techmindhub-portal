---
title: "Git 2.56.1 Fixes Six Vulnerabilities Across Repository Inputs"
description: "The Git security release patches six flaws including code execution in a crafted recursive clone; supported 2.50–2.55 branches have backports."
excerpt: "Untrusted repository data reaches several Git parsing paths. Update developer machines, CI runners and services that ingest repositories."
pubDate: "2026-11-11T14:51:00Z"
status: "published"
canonical_id: "2026-11-11-git-2561-six-security-fixes"
tags: ["GitSecurity", "SoftwareSupplyChain", "CICD", "TechMindHub"]
source_url: "https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/"
cover_card: "https://media.techmindhub.cc/posts/git-2561-six-security-fixes-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/git-2561-six-security-fixes-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/git-2561-six-security-fixes-og-web-v1.jpg"
domain: "digital-trust"
topic: "Git repository trust boundaries"
card_alt: "A recursive clone crossing into hidden configuration and hooks inside a CI runner."
cover_alt: "Conceptual repository trust boundary emphasizing a crafted submodule path and patched Git."
---

A repository is data, but cloning or processing it can exercise complex parsers and filesystem operations. On November 10, [Git announced six security fixes](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/) in 2.56.1, with patches backported to maintained 2.50–2.55 branches. The release warrants attention wherever a machine automatically ingests code from an untrusted source.

The most serious case described by GitHub, **CVE-2026-111760**, involves a specially crafted repository during recursive cloning. An integer truncation related to a long index path can let an attacker replace a submodule's `.git` with a symlink to malicious configuration and hooks, potentially resulting in arbitrary code execution. The attack has specific preconditions; an ordinary local commit is not by itself evidence of compromise.

## Other input boundaries

The remaining fixes span an advertised HEAD path traversal in an empty repository over protocol v2 (CVE-2026-113408), stack corruption with tags carrying more than two signatures (CVE-2026-114467), an out-of-bounds read in oversized binary patches (CVE-2026-114469), heap corruption in large merges (CVE-2026-105437) and arbitrary file reads or writes through untrusted `fast-import` streams using features (CVE-2026-114466). These are distinct bugs with different trigger conditions and consequences; they should not all be described as a remote clone RCE.

The illustration isolates the recursive-clone boundary as a conceptual explanation. Its surrounding folders are not a literal map of all six vulnerabilities, and the shield symbolizes updating rather than a claim that one sandbox eliminates every path.

## Update the places that process repositories

Inventory Git on developer workstations, CI runners, build containers, code-hosting services and automated agents. Update to 2.56.1 or the applicable patched maintenance branch: 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3 or 2.50.2. Check what version actually runs in each image rather than only the host package. Where immediate patching is impossible, reduce ingestion of untrusted repositories and review workflow privileges as a temporary control.

GitHub says its hosted service and relevant products have been patched or scheduled for updates, but downstream distributions and bundled clients have separate release cycles. A CVE announcement does not establish exploitation in the wild. The operational response is version verification and targeted patching, calibrated to exposure.

Source: [GitHub, “Git security vulnerabilities announced,” November 10, 2026](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/).
