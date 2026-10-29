---
title: "fx: Explore an API Response Before Writing the Transformation"
description: "fx 40 introduced live interactive JSON queries. Explore a response, preserve a useful JavaScript expression and test the schema assumptions before automating it."
excerpt: "Inspect a captured API response with fx, develop a live query and keep the expression as a repeatable transformation."
pubDate: "2026-10-29"
status: "published"
canonical_id: "2026-10-29-fx-explore-json-before-transform"
tags: ["OpenSource", "DeveloperTools", "JSON", "API", "SoftwareEngineering", "TechMindHub"]
source_url: "https://github.com/antonmedv/fx/releases/tag/40.0.1"
cover_card: "https://media.techmindhub.cc/posts/fx-explore-json-before-transform-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/fx-explore-json-before-transform-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/fx-explore-json-before-transform-og-web-v1.jpg"
domain: "software"
topic: "JSON investigation"
card_alt: "Abstract JSON tree next to a query window under the words Explore the Data."
cover_alt: "Conceptual progression from inspecting a JSON response to exploring a query and saving an expression."
---

An unfamiliar API response is easier to transform after its structure has been examined. The open-source terminal tool [fx](https://github.com/antonmedv/fx) offers an interactive JSON viewer and JavaScript expressions for processing that data.

The [fx release page](https://github.com/antonmedv/fx/releases) lists 40.0.1 on October 22, 2026. That maintenance release fixed rendering of Unicode characters in go-to-symbol matches and updated a Go dependency. The live interactive queries and key completion arrived in version 40.0.0 on October 5. They are not new features of 40.0.1.

With fx installed, open a saved response in a terminal:

```sh
fx response.json
```

Press `.` to open the [interactive query input](https://fx.wtf/getting-started). Results update as you type; Tab completes keys from the data. Press Enter to apply a query or Escape to return to the original document. In command-line mode, JavaScript expressions can make a useful discovery repeatable. For an illustrative response containing a `users` array with boolean `active` and string `name` fields:

```sh
fx response.json '.users.filter(x => x.active).map(x => x.name)'
```

Adapt the fields to the actual response. The command does not assert that any particular API has this schema.

## Turn exploration into a contract

Our engineering assessment is that interactive exploration shortens the path from seeing a document to asking a precise question about it. If an integration stops importing records, a captured response can show whether the expected collection exists, whether fields are absent and whether values changed type.

A successful extraction is still a limited observation. Ten returned records do not prove that the service should have returned ten. The query cannot establish completeness or validity without an independent expectation. Keep representative input and expected output next to a recurring transformation, including an empty array, missing fields and unexpected types.

Before using the expression in a production pipeline, decide what happens when input is incomplete, a schema changes or processing fails. A quick investigation and a supported integration have different failure requirements. fx provides a compact workspace for the first step and a clear expression to carry into the second.

## Sources

- [fx project and release 40.0.1](https://github.com/antonmedv/fx/releases/tag/40.0.1)
- [Getting started](https://fx.wtf/getting-started)
- [Interactive query reference](https://fx.wtf/query)
