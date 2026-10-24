# TechMind Hub publishing workflow

Last confirmed with Andrew: October 24, 2026.

Start every session with [../AGENTS.md](../AGENTS.md). Approved examples, automated
check coverage and the rule-change process are in [REFERENCE.md](REFERENCE.md).
Run `npm run validate` before opening a PR. Use the repository PR template;
automation complements factual and visual review, not replaces it.

## Ownership and release

- Communicate with Andrew in Russian. Publish editorial content in English.
- Prepare content and source changes on a separate branch and open a pull request.
- Andrew reviews and submits GitHub approval from `AR1314`. The connected author account is `TechMindHub2025`; it cannot approve its own pull requests.
- Merge only after the required approval applies to the current PR head. Do not replace the human review, change repository protection, or treat chat approval as satisfying GitHub rules.
- After merge, verify the GitHub Pages deployment, live article, images and feed card.
- Andrew takes the approved materials and publishes them manually to social media. Do not send social posts without a separate instruction.
- Include `#TechMindHub` in social copy. Substack is outside the regular pipeline for now; do not automatically add its link.

## Media storage

- GitHub holds site code, article Markdown and social text.
- Publication images belong in the existing Cloudflare R2 bucket `tmh-assets` and are served from `https://media.techmindhub.cc`.
- The current manual upload prefix is `posts/`. Use absolute HTTPS image URLs in article metadata and article content.
- Upload images as ordinary files, not as multi-megabyte Base64 payloads passed through conversation/tool outputs.
- Use versioned filenames for changed images, for example `posts/<slug>-card-v2.png`, and retain the previous asset until the new release is verified.
- Upload and verify the public asset before merging a PR that references its new URL. Do not claim a working upload based only on the dashboard.
- Publish only deliberately public, reviewed files. Credentials, access keys, internal logs and private source material do not belong in the public bucket or published site.

## Image roles and acceptance

| Role | Format | Acceptance |
| --- | --- | --- |
| Feed card | 16:9; 1200 x 675 master | Review at 352 x 198 and approximately 260 x 146. One subject, a few large words, generous margins. No terminal commands, dense explanatory diagrams or fine print needed to understand the card. |
| Article / social infographic | Vertical 4:5 where appropriate | Explain the topic at readable full size. Preserve the approved image without arbitrary cropping. This is a separate composition from the feed card. |
| Social link preview | Prefer a dedicated 1200 x 630 version when needed | Check the actual preview crop. A feed card may be reused only when its essential content survives that crop. |

The page already supplies the full title and description. Do not reproduce the whole article inside a thumbnail. Use a light editorial base with subject-specific composition and palette; keep TechMind Hub recognisable through typography, spacing and small brand accents. Dark scenes are appropriate when they serve the subject, not as the default for every post. A large export is not evidence of thumbnail readability: inspect the actual small previews.

## Sources and review

- Prefer primary sources and distinguish their findings from TechMind Hub's assessment.
- External HTTP(S) links open in a new tab with `target="_blank"` and `rel="noopener noreferrer"`. Markdown/MDX links receive these attributes at build time via `src/lib/rehype-external-links.mjs`, including future posts. Keep relative links, fragments, `mailto:`/`tel:` and links on `techmindhub.cc` or `www.techmindhub.cc` in their normal context. External anchors authored directly in Astro templates must carry the same attributes. Check generated HTML across all pages before release; do not rely on client-side JavaScript for this behaviour.
- Do not invent performance figures, deployments, benchmark results or social profile URLs.
- Build the site and check the article body, local links, metadata and media URLs before requesting release approval. Inspect the feed card and live page after deployment.

## Public article presentation

Andrew confirmed removal of both public Download links on October 24, 2026. Do not add article Markdown or infographic Download buttons/links to public articles. Keep editable article sources and social text in GitHub for Andrew. Publication images remain public through R2; removing a link does not make an image private. Do not create duplicate Markdown exports under `public/` for new articles. This policy does not change bucket permissions.


## Visual canon

The approved direction and production rules live in [VISUAL-CANON.md](VISUAL-CANON.md). Use that document before preparing publication images. The shared palette registry is `src/data/editorial-domains.json`; add directions there rather than scattering colour rules across templates. Each article receives one primary `domain`, a short `topic` label and separate alt text for its cover and inner image.

The first paired review candidate is documented in [briefs/photonics-pilot.md](briefs/photonics-pilot.md). Andrew has now authorised all three generated publication pairs. The prior cover-only v3 ZIP and SVG pilot are superseded. The current upload archive is `TechMindHub-Cloudflare-images-canon-v2.zip`, containing exactly six PNGs; the release manifest records their exact names and public R2 URLs. Do not ask Andrew to upload previous archives as the final set. PR #23 was released after the six R2 URLs and Andrew's GitHub approval were verified. For future releases, verify image URLs before merging the human-approved final head. Sources and research IDs belong in article text; no numbered section markers or source footers on the generated images.

Home, Analysis and tag pages share `PostCard.astro`. Article order is title/metadata, the declared infographic, then the article body. The article template renders `cover_hero` exactly once before `<Content />`; do not add the same image again in the Markdown body. Keep `cover_alt` as a concise useful image description.

Do not publish working image explanations, production notes or an “Illustration summary” paragraph. Keep those details in editorial briefs. Scientific findings, limitations and source references still belong in the article where relevant to its argument. A general visual refresh must not silently change the established article order.

Before review, inspect the rendered Home and every changed article; shared template changes require all published articles: no stray template delimiters or closing tags should become text; Home must retain Latest, Topics, discussion links and footer; each article must show exactly one infographic before its first body paragraph. A successful build alone is not evidence that the rendered content is clean.
