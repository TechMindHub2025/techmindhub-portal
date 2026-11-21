---
title: "The vCenter Authentication Bypass That Reached the Virtualization Control Plane"
description: "CVE-2026-123890 exposes an authentication boundary in VMware Directory Service; observed exploitation makes patch sequencing urgent."
excerpt: "The vulnerable management endpoint is the entry point. A disclosed session key can lead to a vCenter administrator session."
pubDate: "2026-11-21T08:07:00Z"
status: "published"
canonical_id: "2026-11-21-vmware-vcenter-srp-auth-bypass"
tags: ["VMware", "Virtualization", "CVE2026123890", "IncidentResponse", "TechMindHub"]
source_url: "https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere"
cover_card: "https://media.techmindhub.cc/posts/vmware-vcenter-srp-auth-bypass-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/vmware-vcenter-srp-auth-bypass-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/vmware-vcenter-srp-auth-bypass-og-web-v1.jpg"
domain: "digital-trust"
topic: "vCenter control-plane exposure"
card_alt: "An amber control-plane gate is breached among virtualized systems."
cover_alt: "A conceptual path links a reachable DCE/RPC endpoint, SRP-6a key exposure and a vCenter session bypass."
---

A virtualization management server is a high-value control plane: access can affect hosts and workloads far beyond the first vulnerable service. [Google Threat Intelligence and Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere) report observed exploitation of **CVE-2026-123890**, an authentication bypass in VMware Directory Service associated with the actor they track as ARMORY CASTLE. Broadcom's [security advisory](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495) rates the issue **9.8** on CVSS.

## From directory protocol to administrator session

The disclosed path involves a network-reachable DCE/RPC service and leakage of SRP-6a session-key material. The attacker can use that weakness to bypass an authentication step and obtain a vCenter session as `administrator@vsphere.local` under the documented conditions. The problem is in the management identity boundary, not a direct code-execution vulnerability in every guest VM.

The immediate response is to identify exposed and affected vCenter versions using Broadcom's version-specific matrix, install the corresponding fixes and examine relevant management and identity activity for signs of misuse. Broadcom lists no workaround in the advisory. Restricting management-network reachability is sensible defense in depth, but it does not replace patching. An investigation should consider unusual sessions, SSO material access and subsequent administrative actions rather than relying on the absence of guest-level alerts.

## Scope of the evidence

Google's report describes exploitation uncovered in its investigation, including activity dating back to September; the coordinated disclosure and fixes arrived on November 19, with advisory updates thereafter. An observed path to a privileged session is serious, but **a vulnerable vCenter does not prove that all of its virtual machines were accessed**. Network exposure, version, patch state and forensic evidence determine an individual organization's risk and response.

Sources: [Google Threat Intelligence](https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-vsphere) and [Broadcom's VMSA advisory](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495).
