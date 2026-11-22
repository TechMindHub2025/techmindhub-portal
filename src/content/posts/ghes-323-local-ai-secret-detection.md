---
title: "Secret Detection Without a Cloud Connection: What GHES 3.23 Proposes"
description: "GitHub Enterprise Server 3.23's release candidate adds a local CPU-based preview for unstructured-secret detection and broader malicious-package coverage."
excerpt: "An air-gapped appliance can run a secret-detection model locally, with preview and coverage limits."
pubDate: "2026-11-22T06:18:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/ghes-323-local-ai-secret-detection-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/ghes-323-local-ai-secret-detection-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/ghes-323-local-ai-secret-detection-og-web-v1.jpg"
card_alt: "Conceptual isolated enterprise server scans a credential pattern locally on its CPU."
cover_alt: "Conceptual local secret scanning inside a disconnected enterprise appliance, separate from package-advisory and update-cooldown controls."
canonical_id: "2026-11-22-ghes-323-local-ai-secret-detection"
tags: ["DigitalTrust", "GHES", "SecretScanning", "AirGapped", "SupplyChain", "TechMindHub"]
source_url: "https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate/"
domain: "digital-trust"
topic: "Local enterprise security scanning"
---

An air-gapped development environment cannot depend on a hosted model for every security check. In the [GitHub Enterprise Server 3.23 release candidate](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate/), GitHub introduces a **public preview** of AI detection for unstructured secrets. It says a self-contained, fine-tuned model runs on the appliance's **CPU**, without a GPU, hosted LLM or outbound connection. The feature is for enterprises using GitHub Secret Protection.

The distinction is operational. A local model keeps the scanning computation within the enterprise network, so a disconnected installation can use this capability without sending source material to an external model service. That does not establish how well the detector finds every secret, how many false positives it produces or what throughput an appliance can sustain under a particular repository workload. GitHub has not presented independent comparative measurements in this announcement.

## Three controls with different purposes

The release also broadens known-malicious-package information in the GitHub Advisory Database beyond npm to PyPI, Maven, RubyGems, NuGet, Go, Rust and Composer, using advisories from OpenSSF's malicious-packages repository. This is intelligence about **identified packages**, distinct from the local model's search for unstructured credentials.

Separately, Dependabot's default version-update behavior now waits until a package version has been on its registry for at least **three days** before opening an update pull request. A cooldown creates time for maintainers and researchers to flag a compromised or faulty release. It is neither a guarantee of detection nor a reason to delay an urgent, specifically needed security fix without assessment. Teams should examine how the default interacts with their update policies.

GHES 3.23 is a **release candidate**, not a general-availability release, and the secret-detection feature is itself in preview. A controlled evaluation should check detection quality, CPU cost, package coverage and upgrade behavior in the organization's actual environment. The engineering point is a more self-contained security workflow, with separate mechanisms for credentials, known malicious packages and update timing.

## Source

- [GitHub: Enterprise Server 3.23 release candidate, November 20, 2026](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate/)
