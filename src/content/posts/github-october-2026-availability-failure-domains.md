---
title: "GitHub's October Incidents Expose the Failure Domains in Cloud Migration"
description: "GitHub's October 2026 availability report traces write-routing failures, retry cascades and a regional network disruption during its Azure expansion."
excerpt: "More capacity supported growing demand, but stale routing, shared links and regional dependencies still caused service degradation."
pubDate: "2026-11-13T08:54:00Z"
status: "published"
canonical_id: "2026-11-13-github-october-2026-availability-failure-domains"
tags: ["GitHub", "CloudReliability", "DistributedSystems", "IncidentAnalysis", "TechMindHub"]
source_url: "https://github.blog/news-insights/company-news/github-availability-report-october-2026/"
cover_card: "https://media.techmindhub.cc/posts/github-october-2026-availability-failure-domains-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/github-october-2026-availability-failure-domains-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/github-october-2026-availability-failure-domains-og-web-v1.jpg"
domain: "infrastructure"
topic: "Cloud migration and failure domains"
card_alt: "A control room looks over database routing and a regional network fault in a cloud infrastructure landscape."
cover_alt: "Two separate incident schematics show stale database write routing on October 7 and a regional network disruption affecting three zones on October 29."
---

Cloud migration can add capacity without removing every shared failure path. In its [October 2026 availability report, published November 12](https://github.blog/news-insights/company-news/github-availability-report-october-2026/), GitHub describes eight incidents of degraded service during a period of substantial Azure expansion. The incidents span October 5–30 and had different causes; they should not all be attributed to Azure or to the migration itself.

As of November 9, GitHub says **140 of 151 production services** and **32 of 50 MySQL primaries** were running in Azure Central US. It had more than doubled compute capacity across nine Kubernetes clusters there. The same report identifies write outages, monitoring gaps and network disruption as reasons to pair capacity with stronger isolation and tested recovery.

## A routing control plane can defeat healthy capacity

On October 7, GitHub experienced two separate write outages lasting about 10 and 9 minutes. During database-routing maintenance, a newly added machine carried old records naming retired database servers. When elected leader, it published settings that directed writes for core databases to those retired servers. Existing validation accepted the settings. An automated maintenance task then failed to honor a pause and triggered a second leader election with the same result.

Reads were largely unaffected, and GitHub says data already saved was not lost. The lesson is specific: leader election, configuration freshness and route validation form part of the write path. Additional database or compute capacity cannot help when the control plane publishes the wrong destination. GitHub reports tightening machine admission, retirement records, maintenance controls and routing validation.

Other episodes exposed different coupling. On October 5, partial network failure between a datacenter region and cloud-hosted databases caused Actions job-assignment calls to wait for timeouts; failover then loaded a healthy region beyond its spare capacity. On October 19, simultaneous reconnection attempts to cache servers saturated a shared datacenter-to-cloud link and affected other services. On October 21, an event-streaming overload spread as work moved between brokers, delaying pull request updates, workflows, webhooks and audit logs. These examples make retry behavior and dependency boundaries as important as raw capacity.

## The regional boundary

GitHub says an **October 29 Azure network disruption affected all three Central US availability zones** and at least 34,128 signed-in users. That does not mean every service in every zone went completely offline. It means a regional dependency can cross the isolation boundary that teams might expect from distributing instances among zones. GitHub planned an East US 3 traffic ramp beginning in the first week of December, subject to validation.

An operator can test these boundaries with fault injection and recovery drills: can a stale route be rejected before publication; can clients back off without a retry storm; does another region have enough independent capacity and working dependencies; and can database leadership and traffic actually move safely? These are engineering questions suggested by the incidents, not a claim that any one change guarantees availability.

This is GitHub's own retrospective, not an independent audit. Its fleet counts, incident metrics and planned mitigations describe GitHub's systems at particular times. They are not universal measurements of Azure reliability, and future regional recovery had not been demonstrated by the report.

Source: [GitHub availability report: October 2026, November 12, 2026](https://github.blog/news-insights/company-news/github-availability-report-october-2026/).
