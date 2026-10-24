# TechMind Hub — instructions for every session

Before editing, read [editorial/README.md](editorial/README.md) and
[editorial/VISUAL-CANON.md](editorial/VISUAL-CANON.md). These versioned documents,
the palette registry and the current repository are the project reference; do
not reconstruct decisions from chat memory or superseded drafts.

## Scope and decisions

- Communicate with Andrew in Russian; publish editorial content in English.
- Follow the existing canon for routine publication work. A new subject may have
  its own composition within it. Agree changes to the canon, article order,
  storage, hosting or publishing workflow with Andrew before implementing them.
- Do not bundle unrelated visual or architecture changes into a content PR.
- Use the existing external GitHub Pages repository. Do not move this site to a
  different host or register a replacement project as part of routine editing.
- Explain any requested exception in the PR, with the agreement that authorises
  it. Do not weaken a check just to make an accidental regression pass.

## Established publication rules

- Article order: title/metadata → one declared infographic → article text.
  The template renders `cover_hero`; do not repeat it in Markdown.
- No public production notes, “Illustration summary”, Download controls or
  duplicate article exports. Keep concise useful alt text.
- Use the built-in image generator for covers and editorial infographics. Pair
  them through the brief, shared motif and registered domain palette; make
  separate compositions. Inspect cover text at 352px and 260px. Sources, author
  names, research IDs and decorative 01/02 markers stay off the artwork.
- Code, Markdown and editorial briefs go in GitHub. Publication images go in
  Cloudflare R2 `tmh-assets/posts/`, served by `https://media.techmindhub.cc`.
  No image binaries or image Base64 in publication code. Andrew uploads ordinary
  versioned image files manually; verify public URLs before release.
- External HTTP(S) links open a new tab with `noopener noreferrer`. Internal,
  fragment, mail and telephone links keep their normal behaviour.
- Use primary sources, distinguish reported findings from our assessment and
  do not invent claims. Andrew publishes social copy manually; Substack is not
  part of the regular pipeline.

## Validation and release

- Run `npm ci` when dependencies need installing, then `npm run validate`.
  This builds the site, tests the publication guard and checks generated HTML.
- Inspect Home, archive, affected tag pages and every changed article on desktop
  and mobile. For a shared template change, inspect all published articles.
  Check image loading, thumbnail readability and actual external-link behaviour.
  Attach screenshots when a PR changes the rendered product.
- Use the PR template; mark inapplicable items with a reason, not a false tick.
- Prepare a separate branch and PR. Andrew (`AR1314`) approves the final head in
  GitHub. Do not self-approve, bypass review or change repository protections.
  If the head changes after review, obtain approval of the new head.
- Merge only after that approval and successful checks. Then verify the GitHub
  Pages deployment and live pages. Do not claim deployed changes from local QA.

Approved examples and check coverage: [editorial/REFERENCE.md](editorial/REFERENCE.md).
