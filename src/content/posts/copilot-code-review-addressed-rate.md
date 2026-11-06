---
title: "Measuring AI Code Reviews: From Suggestions to Developer Actions"
description: "GitHub's new repository-level Copilot code review counts distinguish comments evaluated at merge from developer responses. The addressed rate measures action, not defects fixed."
excerpt: "A review comment has little value merely because it exists. GitHub now counts how developers respond to Copilot's feedback, but the denominator and the meaning of 'addressed' demand care."
pubDate: "2026-11-06T16:10:00Z"
status: "published"
canonical_id: "2026-11-06-copilot-code-review-addressed-rate"
tags: ["Copilot", "CodeReview", "DeveloperTools", "EngineeringMetrics", "TechMindHub"]
source_url: "https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate/"
cover_card: "https://media.techmindhub.cc/posts/copilot-code-review-addressed-rate-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/copilot-code-review-addressed-rate-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/copilot-code-review-addressed-rate-og-web-v1.jpg"
domain: "software"
topic: "Code review measurement"
card_alt: "Purple editorial scene of a developer reviewing a pull request, with paths from a Copilot comment to applying, asking for a fix, editing and deferring a change; headed After the Comment."
cover_alt: "Conceptual review board separating Copilot pull request comments from human review, showing evaluation at merge and four ways a developer can address a comment."
---

A code review tool can produce a large number of comments without making the software better. Counting how many suggestions it generated tells a team that the tool was active; it does not show whether developers used the feedback, whether the comments were correct or whether a defect was prevented. GitHub's latest Copilot usage metrics move one step further along that chain of evidence. They measure responses to Copilot code review comments on merged pull requests.

The [November 5, 2026, GitHub announcement](https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate/) adds a `copilot_code_review` object to each repository row in enterprise and organization `repos-1-day` reports. It contains counts of comments evaluated and addressed, distributions of those counts, and a separate count of merged pull requests without a later human change request. The headline calculation is simple: addressed comments divided by evaluated comments. Its interpretation is considerably more demanding.

## The denominator begins at merge

The unit is a *Copilot code review comment on a pull request*, not every comment in a repository. Human comments, other review tools' comments and Copilot reviews inside an IDE are outside these counts. GitHub evaluates the qualifying comments when the pull request merges and attributes them to the merge day. A review written on Monday for a PR merged on Friday appears in Friday's report. A PR still open is not yet represented in these evaluated-comment counts.

That timing changes how a daily chart should be read. A sudden rise in evaluated comments might reflect a batch of old PRs merging, rather than a sudden change in review activity that morning. Likewise, comparing two repositories by calendar day without accounting for the size, age and mix of their merged PRs would conflate review behavior with merge cadence. This is an inference about analysis design from GitHub's definition, not a performance finding reported by GitHub.

The reports are scoped per repository. Where there is no Copilot code review activity for that day, GitHub supplies zero counts and empty breakdown arrays. When `total_comments_evaluated` is zero, a rate cannot be calculated by division; a dashboard should show it as unavailable rather than as a 0% response rate. That distinction prevents a day without an eligible denominator from looking like a day when developers ignored all feedback.

## What “addressed” actually records

GitHub counts an evaluated comment as addressed if the developer applies a suggested change, asks Copilot code review to make the fix, edits the code by hand, or replies that the fix will come in a later pull request. Ignored comments and comments that Copilot later found to be wrong remain evaluated but are not addressed. For example, 12 addressed comments among 20 evaluated comments would yield a 60% addressed rate; those numbers are illustrative, not observations from the release.

The inclusion of a promise to fix something later is consequential. Addressed means a recorded response under the product's rules. It does not establish that the promised follow-up happened, that a manual edit solved the issue, or that the original comment identified a real defect. Conversely, a developer might correctly reject an erroneous warning, lowering the addressed share without making the review process worse. An optimization target that rewards the ratio alone could pressure a team to acknowledge weak comments or avoid challenging them.

Existing `pull_requests.total_copilot_applied_suggestions` measures something narrower: ready-to-apply suggestions that someone actually applied. The new evaluated-comment count includes comments with no such ready-to-apply change, and its addressed count recognizes several other response types. These are different populations and behaviors; their totals should not be treated as alternative spellings of the same metric.

## Breakdowns add context, with accounting traps

Four arrays divide evaluated and addressed counts by severity, review tier, comment type and customization. Severity uses high, medium and low; tiers include lite, balanced and max. A comment type might be a bug, security concern or a repository-specific `custom` coding guideline. Customization indicates whether the review drew on custom instructions, a skill, an MCP server or none. This allows a team to ask more useful questions than “What was the single overall percentage?”

For instance, a low response to a particular class of comment could prompt a sample-based audit. Were the findings inaccurate, too difficult to act on, duplicated by other checks or simply deferred? An increase in the addressed share for a configured review setup could motivate a closer comparison, but it cannot by itself establish that the configuration caused the change. Different PRs, reviewers and tasks can shift the population.

The arrays are also not interchangeable partitions of the total. GitHub's [field reference](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics) explains that a comment without a recorded severity, tier or type appears in the overall totals but not that dimension's array. Those arrays can therefore sum to less than the total. A comment associated with multiple customizations appears under each of them, so the customization array can sum to more than the total. A reporting pipeline that insists every category adds up exactly, or sums customization categories into a new grand total, will produce a false discrepancy or double count.

## The human-review signal is separate

`total_merged_no_human_change_request_after_review` counts merged PRs that Copilot reviewed and for which no person requested changes *after Copilot's first review*. It is a PR count, whereas the addressed rate has comments as its denominator. A human change request after that point excludes the PR even if it was later dismissed or the PR was approved. One issued before the first Copilot review does not exclude it. The field can include bot-authored PRs, although GitHub says Copilot usually does not evaluate comments on those PRs for the addressed-comment measure.

This field might help a team investigate whether human reviewers still ask for changes following automated review. It is not a measure of human-review replacement, approval quality or the absence of defects. The time ordering is part of the definition, and the denominator of Copilot-reviewed merged PRs differs from the denominator of evaluated comments. Treating these as a single funnel would hide those differences.

## A defensible measurement practice

A useful dashboard can display the raw numerator and denominator next to the rate, annotate merge-day attribution, and distinguish human review from Copilot comment response. A team can inspect representative addressed, ignored and rejected comments, then compare them with the actual code changes and subsequent outcomes. Review time, rework and post-merge defects may provide additional context if measured consistently, but none is supplied as a causal result by this announcement.

Comparison should also respect repository and task mix. A library with narrow, repeatable fixes and a service with complex architecture changes offer different opportunities for a review tool. Severity and type distributions can help form cohorts; manual checking of a sample can test whether the categories and actions convey the meaning the team assumes. Any claim about time saved or bugs prevented would need an explicit study design and evidence beyond the response count.

Access is limited to enterprise owners, enterprise billing managers, organization owners and holders of the relevant custom metrics-view permission; the Copilot usage metrics policy must be enabled. Teams consuming the API should check authorization, field availability and zero-denominator handling before publishing a scorecard.

The new reporting is valuable because it asks what happens *after* an AI reviewer speaks. It provides evidence of a developer's interaction with a specific class of feedback. Its strongest use is as a starting point for inspecting review quality and workflow behavior, with the limits of each count visible to the people interpreting it.

## Sources

- [GitHub Changelog, “Usage metrics API adds code review details and addressed rate,” November 5, 2026](https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate/)
- [GitHub Docs, “Data available in Copilot usage metrics” — repository-level code review fields](https://docs.github.com/en/copilot/reference/copilot-usage-metrics/copilot-usage-metrics)
