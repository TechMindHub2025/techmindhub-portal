---
title: "A Path Across Tenants: What Google's Dataform Fix Reveals About Workspace Isolation"
description: "Google fixed a critical path traversal in Dataform, BigQuery Studio and Colab Enterprise. The case illustrates how repository paths can cross a cloud tenant boundary."
excerpt: "A workspace path is part of the isolation boundary when cloud services connect files and Git repositories."
pubDate: "2026-11-22T06:15:00Z"
status: "published"
cover_card: "https://media.techmindhub.cc/posts/google-cloud-dataform-cross-tenant-path-traversal-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/google-cloud-dataform-cross-tenant-path-traversal-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/google-cloud-dataform-cross-tenant-path-traversal-og-web-v1.jpg"
card_alt: "Conceptual workspace folders separated by a tenant wall, with a file path crossing that wall."
cover_alt: "Conceptual comparison of intended tenant-specific Git workspace paths and a path that escapes into another tenant's repository."
canonical_id: "2026-11-22-google-cloud-dataform-cross-tenant-path-traversal"
tags: ["CloudSecurity", "MultiTenancy", "PathTraversal", "Dataform", "TechMindHub"]
source_url: "https://docs.cloud.google.com/dataform/docs/security-bulletins"
domain: "digital-trust"
topic: "Cloud workspace isolation"
---

Cloud development workspaces combine repository files, user-controlled paths and service identities. The paths that connect them are a security boundary. In [bulletin GCP-2026-084](https://docs.cloud.google.com/dataform/docs/security-bulletins), published November 19, Google disclosed a **critical path traversal** affecting Dataform, BigQuery Studio and Colab Enterprise. Google says an authenticated remote attacker could read private files and create arbitrary files across tenant repositories.

Google says it patched the vulnerability on **October 10, 2026**, and that customers need take no action. Its broader [Cloud Customer Care bulletin](https://docs.cloud.google.com/support/bulletins) reports no evidence of exploitation against Google Cloud workloads in its security telemetry. The disclosure describes a possible cross-tenant attack path, not an observed breach.

## Where the boundary failed

A Git-connected workspace has to translate requested files into paths belonging to a particular tenant and repository. Path traversal occurs when a path can resolve outside that intended scope. The dangerous operation is not simply reading a suspicious-looking filename; it is allowing a path chosen in one security context to refer to another tenant's resources. A fix must enforce the boundary after normalization and during the actual file operation, including creation paths. Google has not published enough implementation detail to describe the exact faulty code or the patch mechanism.

The authenticated prerequisite matters. It does not reduce the isolation requirement: cloud tenants routinely contain many legitimate authenticated users, and one tenant's access must not become another tenant's filesystem access. Cross-tenant file creation could also change subsequent repository operations, although the bulletin does not claim a demonstrated exploit chain beyond the stated read and write capabilities.

For operators, the immediate vendor action is complete. The wider engineering lesson is to test path handling where workspaces, Git integrations and service accounts meet: verify canonical paths, repository ownership and the identity used for every read and write. Those are design questions for comparable systems, not extra remediation steps Google has required for this incident.

## Source

- [Google Cloud: Dataform security bulletin GCP-2026-084, November 19, 2026](https://docs.cloud.google.com/dataform/docs/security-bulletins)
