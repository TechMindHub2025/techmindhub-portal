---
title: "Agile Deliberation: Defining a Category with Its Difficult Cases"
description: "Google Research studies an interactive way to build image classifiers for subjective categories. The engineering challenge is eliciting a human definition before optimizing the model."
excerpt: "When a category has a gray area, a longer prompt is not necessarily a better specification. Borderline images can reveal what the reviewer actually means."
pubDate: "2026-11-05T14:10:00Z"
status: "published"
canonical_id: "2026-11-05-agile-deliberation-subjective-boundaries"
tags: ["HumanAIInteraction", "ComputerVision", "ActiveLearning", "AgenticAI", "TechMindHub"]
source_url: "https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas/"
cover_card: "https://media.techmindhub.cc/posts/agile-deliberation-subjective-boundaries-card-web-v1.webp"
cover_hero: "https://media.techmindhub.cc/posts/agile-deliberation-subjective-boundaries-infographic-web-v1.webp"
cover_og: "https://media.techmindhub.cc/posts/agile-deliberation-subjective-boundaries-og-web-v1.jpg"
domain: "ai"
topic: "Human-defined visual categories"
card_alt: "Illustrated reviewer examining ambiguous food images in a lavender gallery, with the phrase Define the Gray Area."
cover_alt: "Conceptual illustration of a reviewer refining a subjective image category through positive and negative examples, borderline images and evaluation."
---

Imagine an image classifier asked to identify a “healthy food.” A person can often make a judgment about a particular photograph, yet struggle to write a rule that covers every pastry, prepared meal and ingredient. Different reviewers may also disagree for defensible reasons. An instruction such as “classify healthy foods” leaves the model to supply its own unstated definition. Google Research's [November 4, 2026 account of Agile Deliberation](https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas/) addresses this specification problem by asking people to examine the cases where a category's boundary is hardest to articulate.

This is a research method for subjective visual classification, not a general agent that resolves human ambiguity in every setting. The underlying research appeared earlier at CVPR 2026; November 4 is the date of Google's public explanation. That distinction matters when interpreting it as evidence of a new product launch.

## The specification is discovered through examples

The process begins with concept scoping. A user describes the intended category and supplies or judges positive and negative examples. Rather than treating the initial wording as a finished rule, Agile Deliberation retrieves images near the uncertain boundary and invites further decisions. A vision-language model helps identify candidate examples. The system then uses the feedback to refine a classifier, including automatic prompt optimization. The important loop is between human judgment, selected cases and a revised operational definition.

Borderline examples are unusually valuable because easy examples tell us little about the boundary. A classifier and reviewer will probably agree that an unmistakable whole apple belongs in many healthy-food categories. A sweetened fruit drink, fortified snack or meal with mixed ingredients is more revealing. Each disagreement can expose a hidden criterion: nutritional content, processing, serving size, marketing language or what the reviewer considers the unit of classification.

That does not mean every borderline image is equally informative. A visually confusing photograph can generate uncertainty because the pixels are poor, not because the concept is disputed. A careful implementation should separate ambiguity in the category from uncertainty about what the image depicts. It should also record the actual wording of a revised criterion and the decisions that motivated it, so a later reviewer can understand why the classifier changed.

## What the study observed

Google reports 18 interactive sessions of approximately 90 minutes, covering two subjective tasks: healthy food and pay-to-play content. In the studied comparisons, participants using Agile Deliberation produced classifiers that performed better than the selected zero-shot and other baselines, while reporting lower effort, stress and fatigue than manual deliberation. The paper and blog describe increased consistency between participants and the resulting models. These are author-reported results from a small, task-specific study, not an independently replicated performance guarantee across moderation, medicine or scientific imaging.

The comparison should be read with its denominator in view. An improvement over a zero-shot instruction can show that interactive clarification helps relative to a weak initial specification. It does not establish that the resulting classifier meets an application-specific error budget or that its labels agree with a diverse population of reviewers. Nor does an easier 90-minute interaction establish that the ongoing cost of maintaining a production taxonomy is low.

The code release makes the approach inspectable and enables further experiments. It does not by itself establish production readiness. Access controls, sensitive images, reviewer disagreement, versioned decisions and monitoring after deployment remain separate system responsibilities.

## Engineering a defensible decision boundary

For a team building a subjective classifier, the first design choice is whose judgment counts. A single expert, a group of moderators and an affected community can define materially different boundaries. A user interface should allow genuine disagreement to be represented, rather than forcing consensus through the model's output. One practical design is to distinguish cases with a stable agreed label, cases requiring escalation and cases where policy remains unresolved. A classifier can then abstain when the available evidence does not justify a binary answer.

Next comes the evaluation set. An interactive session may repeatedly revisit similar examples; evaluating only on those selected examples would reward fitting the conversation. Reserve images that were not used during concept iteration, stratify them by likely disagreement and assess false positives and false negatives separately. Compare several plausible prompt and model baselines, preserve the model version and repeat with different reviewers. If the target population changes, revisit the definition rather than assuming a prompt remains valid indefinitely.

The image in this article uses food examples to explain the loop. Its specific examples and decision criteria are illustrative, not the study's published dataset or a recommendation for nutrition classification. In a safety-sensitive domain, the cost of an erroneous label must be specified before a system can choose a threshold or a fallback.

There is also a governance question: when a reviewer changes the category, is that a correction to a model or a policy change? The answer may require a recorded rationale, a second reviewer and a migration plan for previously classified items. An automated prompt optimizer can find wording that reproduces judgments, but it cannot decide whether the judgments are legitimate for the people affected by the system.

## Our assessment

Agile Deliberation points toward a useful division of work. A machine can search a large image space for informative cases, while a human supplies the meaning of a disputed category. The engineering benefit is a more explicit, testable specification, particularly when writing a longer prompt merely hides unresolved choices. The next evidence needed is broader replication across domains and reviewers, plus measurements of stability when the data and policy change. Until then, its strongest claim is a promising method for discovering a decision boundary, not a universal answer to ambiguous human concepts.

## Sources

- [Google Research, Agile Deliberation, November 4, 2026](https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas/)
- [Agile Deliberation research code](https://github.com/google-research/google-research/tree/master/agile_deliberation)
