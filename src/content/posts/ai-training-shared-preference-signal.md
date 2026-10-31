---
title: "OpenAI and Google Back a Shared Signal for AI Training Preferences"
description: "A proposed robots.txt policy token could let publishers express a training preference to multiple AI providers. Implementation is still ahead, and the Internet-Draft is not an adopted standard."
excerpt: "A shared training preference could reduce publisher coordination work, but providers still need to carry that preference through retrieval, dataset preparation and training."
pubDate: "2026-10-31"
status: "published"
canonical_id: "2026-10-31-ai-training-shared-preference-signal"
tags: ["AIGovernance", "OpenWeb", "AITraining", "WebStandards", "TechMindHub"]
source_url: "https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/"
cover_card: "https://media.techmindhub.cc/posts/ai-training-shared-preference-signal-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/ai-training-shared-preference-signal-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/ai-training-shared-preference-signal-og-web-v1.jpg"
domain: "digital-trust"
topic: "AI training preferences"
card_alt: "A website sends one amber robots.txt preference signal toward two abstract AI providers."
cover_alt: "Conceptual flow from website paths to a shared robots.txt policy read by two providers; training preference is distinguished from crawl restriction."
---

On October 30, 2026, [OpenAI](https://openai.com/index/helping-websites-express-ai-training-preferences/) and [Google](https://developers.google.com/search/blog/2026/10/ai-training-control) announced plans to support a shared way for websites to express whether their content should be used for generative AI training. They intend to read a common signal in `robots.txt`, a file website operators already use to express crawler-related rules. This is a plan for future implementation: OpenAI aims to add support in the coming months, while Google targets 2027.

The [individual Internet-Draft](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/) proposes a policy token, `__usage_ai-training`, used in a `User-Agent` group with familiar `Allow` and `Disallow` path rules. A website could express a preference for its entire site or particular paths. A participating provider would interpret the token as a content-use preference, rather than requiring the publisher to maintain an equivalent instruction for each company. The document is an active individual draft, **not an IETF-endorsed or adopted standard**.

That distinction matters for today's configuration. OpenAI says its existing crawler controls will continue to apply. Google says that, when `Google-Extended` is not explicitly specified, it plans to interpret an opt-out through the common token as if the publisher had disallowed `Google-Extended`. An explicit provider-specific setting can still tailor treatment. Implementation details and precedence should be checked against each provider's documentation when support arrives.

## Usage and access are different decisions

The draft defines AI training as using an asset to modify the learned parameters of a generative model. Its policy token concerns that use. It **does not itself instruct a crawler to stop downloading** a page; ordinary crawler rules continue to govern crawling preferences separately. An operator seeking both outcomes must evaluate both types of control.

Our assessment is that a common signal could reduce the coordination cost for publishers. Expressing one broad choice across participating providers is easier to review than an expanding collection of vendor-specific tokens. But the harder implementation work happens after retrieval: a provider needs to associate the observed preference with the content it collected, retain the relevant rule context through dataset preparation and apply it at training time.

That chain needs records if a disagreement is to be investigated. Which `robots.txt` version applied when an asset was retrieved? Which path rule matched? How was it carried into later datasets? The draft's description of a machine-readable preference cannot by itself demonstrate that a provider's data pipeline acted on it.

For website operators, the useful immediate step is to inventory existing crawler and provider-specific rules and decide which pages require different treatment. Follow implementation announcements before assuming the new token has taken effect. The next meaningful milestone is consistent, documented behaviour across providers, including precedence, scope and a way to resolve mismatches between a publisher's stated preference and observed use.

## Sources

- [OpenAI announcement](https://openai.com/index/helping-websites-express-ai-training-preferences/)
- [Google Search Central announcement](https://developers.google.com/search/blog/2026/10/ai-training-control)
- [Machine-Readable Training Preference Signal, individual Internet-Draft](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/)
