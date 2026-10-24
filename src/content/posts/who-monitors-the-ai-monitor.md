---
title: "Who Monitors the AI Monitor? Lessons from an External OpenAI Review"
description: "An external review of a historical OpenAI monitoring system highlights three separate engineering questions: coverage, detection and response."
excerpt: "A monitor cannot assess evidence it never receives. External review makes coverage and response timing part of the safety argument."
pubDate: "2026-10-24"
status: "published"
canonical_id: "2026-10-24-who-monitors-the-ai-monitor"
tags: ["AgenticAI", "AISafety", "Cybersecurity", "DigitalTrust", "TechMindHub"]
source_url: "https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/"
cover_card: "https://media.techmindhub.cc/posts/who-monitors-the-ai-monitor-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/who-monitors-the-ai-monitor-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/who-monitors-the-ai-monitor-og-web-v1.jpg"
domain: "digital-trust"
topic: "AI safety"
card_alt: "Amber magnifying lenses examine layered records beside the question Who monitors the monitor?"
cover_alt: "Layered records and magnifying lenses illustrate coverage, detection and response in AI monitoring."
---

An AI monitor can examine an agent's behaviour and flag suspicious actions. That is a useful capability, but it leaves a prior question unanswered: which actions actually reach the monitor? A second model cannot evaluate an event that the surrounding infrastructure never presents to it.

An [external pilot by METR and Redwood Research](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/), published on October 22, provides a concrete reason to keep those questions separate. The exercise ran from July 21 to August 11, 2026, and examined OpenAI's internal misalignment monitoring as it existed on and before July 21. Its results do not establish the expanded system's current coverage.

## What the external review establishes

The evaluators had access to internal code, documentation and staff. They identified monitoring gaps and potential routes around safeguards. One gap concerned context compaction. OpenAI staff had independently identified it before the exercise and fixed it during the work. Other findings included ways monitoring could potentially be subverted.

OpenAI subsequently told the evaluators that vulnerabilities affecting its production safeguards had been patched. The evaluators did not verify those claims. These findings describe weaknesses in a historical system; possible bypasses are not evidence that deployed agents actually exploited them.

That distinction matters for interpreting the report. Neither a dramatic failure narrative nor an unconditional assurance follows from a limited exercise. The more useful outcome is a set of engineering questions that an operator can investigate in its own deployment.

## Coverage comes before classification

For our assessment, coverage means the evidence that reaches the review process, rather than the intended scope written in a design document. A system might classify every event it receives correctly while omitting an important route through which an agent acts.

Consider a hypothetical assistant allowed to prepare infrastructure changes. The application records its chat messages, but a background tool performs some changes through another process. If that second process is absent from the review stream, an impressive detector score says little about those changes. This is an illustrative scenario, not a case reported by the evaluators.

A practical acceptance check would start with the available action routes. For each route, the operator should be able to trace a permitted test action through execution, evidence collection and review. Missing events should be visible as gaps, rather than silently counted as harmless activity. This is our proposed evaluation method, not a claim that we tested OpenAI's system.

## Detection needs an explicit denominator

[OpenAI's description of its monitoring approach](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/) explains how model-based review feeds human investigation. It also acknowledges that matching known employee escalations does not establish the false-negative rate across open-ended traffic. Monitoring is presented as one part of a wider defensive system.

The operational implication is that “the monitor caught every reported incident” and “the monitor catches every important incident” are different propositions. The first has a known comparison set. The second requires evidence about events that may never have been reported or recognised.

Our recommendation is to state what each evaluation actually measures. A team can test a detector on deliberately constructed examples, compare its alerts with an independent review, and examine failure cases. It should retain the distinction between those test results and the much broader claim that all deployed behaviour is adequately supervised.

Useful reporting would therefore include what was tested, what counted as a miss, which action routes were represented and what remained outside the exercise. A headline accuracy figure without that context can hide the most consequential uncertainty.

## Response time belongs in the safety argument

Detection also needs an action path. An alert can be informative without arriving early enough to prevent harm. Whether that is acceptable depends on the action being supervised.

For a hypothetical draft report awaiting approval, a later review may still occur before publication. For a tool capable of changing access permissions or sending data outside an organisation, the relevant consequence may arrive much sooner. These examples illustrate our reasoning; they are not additional findings about OpenAI.

We would ask an operator to identify who receives an alert, what authority that person has, and which actions can be paused or reversed. The acceptance criterion should connect the time available for intervention to the speed and reversibility of the underlying task. Notification delivery alone does not demonstrate a successful response.

## Make the monitor reviewable

The resulting evaluation has three parts: verify that evidence arrives, assess how it is interpreted, and establish whether intervention remains useful. Keeping those parts separate makes failures easier to diagnose and improvements easier to substantiate.

For an enterprise deployment, our suggested starting point is one narrowly defined workflow with clear permissions and a known review owner. Follow representative test actions through the whole process, record the unresolved gaps, and agree on what would prevent release. Expand the scope only when the evidence supports doing so.

External access can help challenge assumptions that a development team has stopped noticing. Its value still depends on a clear statement of scope, timing and what was independently checked. A historical review and a later remediation statement should remain distinguishable in the public record.

**A monitor cannot assess evidence it never receives. What evidence would convince you that your own agent's monitoring is complete enough for its permissions?**

## Primary sources

- [METR: Red-Teaming OpenAI's Internal Agent Monitoring Systems](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/)
- [OpenAI: How we monitor internal coding agents for misalignment](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)

*Checked October 24, 2026. The external exercise assessed a historical system. Operational examples and acceptance recommendations are TechMind Hub's analysis. The infographic is conceptual, not a depiction of a demonstrated attack.*
