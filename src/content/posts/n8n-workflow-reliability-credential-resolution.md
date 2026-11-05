---
title: "n8n 2.46.5: Why Workflow Reliability Depends on Credential and Data Resolution"
description: "A patch to credential lookup, named properties on arrays and migration-report visibility exposes three distinct ways an automation can look healthy while behaving unexpectedly."
excerpt: "The n8n release corrects specific lookup and expression paths. Its engineering value lies in testing the boundaries between stored configuration, runtime data and operational reports."
pubDate: "2026-11-05T10:42:39Z"
status: "published"
canonical_id: "2026-11-05-n8n-workflow-reliability-credential-resolution"
tags: ["Automation", "DeveloperTools", "WorkflowReliability", "TechMindHub"]
source_url: "https://github.com/n8n-io/n8n/releases/tag/n8n%402.46.5"
cover_card: "https://media.techmindhub.cc/posts/n8n-workflow-reliability-credential-resolution-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/n8n-workflow-reliability-credential-resolution-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/n8n-workflow-reliability-credential-resolution-og-web-v1.jpg"
domain: "software"
topic: "Workflow configuration boundaries"
card_alt: "Amber editorial workflow scene with a credential key entering one node, an array of data continuing through the flow and an engineer observing it."
cover_alt: "Conceptual automation scene linking scoped credential lookup, a named property on an array and the filtered visibility of archived workflows in a migration report."
---

An automation can fail without a dramatic crash. A selection list may not load because a node cannot find a credential; an expression may quietly evaluate to `undefined`; a migration report may count workflows that no longer run. Each symptom sits at a different layer, yet all three can make an operator misread the state of a larger process. [n8n 2.46.5](https://github.com/n8n-io/n8n/releases/tag/n8n%402.46.5), released on November 4, 2026, provides a useful small case study in these boundaries.

The release notes list a fix to credential resolution during node parameter loading, a fix for named array keys in expressions, and changes to migration-report visibility and loading feedback. The notes do **not** identify a specific exploitable vulnerability or publish a security advisory for these fixes. Calling the release a security patch in that stronger sense would go beyond the evidence. The concrete question is how stored permissions, data representation and operator-facing reports are translated into behavior.

## Loading a parameter can require a credential

Many workflow nodes obtain available fields or resources from a remote service while an editor configures them. An operator may be choosing a database table or API resource before the workflow is run. That apparently simple list can depend on the node's credential, the project holding the workflow and the caller's permission to use it.

The [credential-resolution change](https://github.com/n8n-io/n8n/pull/42755) brings dynamic node parameter loading, the MCP node resource explorer, credential tests and credential probes onto a common lookup in `CredentialsFinderService`, with an option for the relevant callers. It also extends role-scope filtering. The developers' test description includes a project editor loading a list through a project credential and an instance owner opening a node in a project they do not belong to. These are specific intended behaviors, not a claim that every credential path has been redesigned.

The same change stops two read-only editor components, `ParameterInput` and `ResourceMapper`, from fetching remote options or mapper fields. A preview that only displays a past execution does not need a fresh request to an external service. There is a visible trade-off: where remote options normally map a stored value to a friendly label, the read-only view can show the stored value instead. That is useful to explain to an operator before a label change is misdiagnosed as corrupted data.

Our assessment is that the acceptance test should separate three contexts: editing a node with an authorized project credential, viewing it without write access and executing the workflow. Observe which context makes a remote parameter request, which identity is used and what a missing or revoked credential looks like. The release documents the shared lookup and reduced read-only fetching; it does not make the credential's external service available or prove a user's intended authorization policy.

## An array can have a property beyond its indexes

The expression fix is unusually specific. The [change description](https://github.com/n8n-io/n8n/pull/42970) gives an example in which an item's `json` value is an array with an additional named property:

```js
const json = Object.assign([{ role: 'assistant' }], { sessionId: 'session-1' });
```

The property `sessionId` belongs to the array object, not to its first element. Before the fix, an expression such as `{{ $json.sessionId }}` could yield the expected value in the legacy or native evaluation path but `undefined` in isolated evaluation using `vm` or QuickJS. The developers describe separate causes: a lazy proxy served indexed array keys without the named key, while a QuickJS bridge copied host data through JSON serialization, which discards named array properties. In one reported case a Data Table filter consequently received an empty value.

The patch makes the cited direct-property expressions return the named value across those engines. It has a documented limit: an expression returning the **whole array**, such as `{{ $json }}`, may still lose named properties in the isolated paths. That broader result-transfer issue was left for separate work. Treating this release as a universal normalization of array behavior would therefore be incorrect.

This matters because a visual workflow often hides a JavaScript representation detail. A node can display an array of messages, and a colleague may assume metadata is stored on each item or in an object beside the array. The actual runtime value can differ. A reproducible regression fixture should include the source node, its output shape, the exact expression and the downstream operation. Test both a direct property read and any whole-array pass-through your workflow uses. If the input schema is under your control, placing metadata in an explicit object field may be easier for different consumers to understand; that is an engineering design choice, not a requirement imposed by this patch.

## A report's default filter changes its meaning

The [migration-report change](https://github.com/n8n-io/n8n/pull/42995) hides archived workflows from the default view. Its description says archived workflows are still scanned and retain their findings, owner and “won't fix” decisions. A filter on a rule's detail page can reveal them. The overview counts and CSV export exclude archived workflows by default because archived workflows do not run. A separate release change adds a message when the report takes a long time to load.

These adjustments concern what an operator sees, not a claim that the migration engine has been fixed or that an archived workflow is automatically safe to restore. A smaller “affected” total after an upgrade might reflect the new reporting scope even if no workflow was repaired. The operator should record whether archived workflows were included when comparing reports across versions. Before restoring an archived workflow, inspect its retained findings and re-evaluate the relevant migration requirements.

## A practical regression plan

For a team upgrading n8n, the most useful test set is deliberately mixed. Include a node whose remote options use a project credential, a read-only execution preview, an expression reading a named array property, a workflow that passes the entire array onward, and an archived workflow with a known migration finding. Record the expected value or request in each context. Compare the result with the release's precise behavior, and do not infer a fix for the whole-array case from the direct-property test.

The larger engineering lesson is about observability at translation points. A stored secret reference must resolve under the right authority; a data property must survive the chosen expression engine; and a report must state which workflows its totals include. A successful run or a clean overview is useful evidence only when those boundaries are understood.

## Sources

- [n8n 2.46.5 release notes](https://github.com/n8n-io/n8n/releases/tag/n8n%402.46.5)
- [Credential lookup change and test scope](https://github.com/n8n-io/n8n/pull/42755)
- [Named array-key expression change and its remaining limit](https://github.com/n8n-io/n8n/pull/42970)
- [Archived-workflow migration-report change](https://github.com/n8n-io/n8n/pull/42995)
