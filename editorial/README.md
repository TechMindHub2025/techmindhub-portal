# TechMind Hub publishing workflow

Last confirmed with Andrew: October 24, 2026.

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
- The current manual upload prefix is `posts/`. Use absolute HTTPS image URLs in article metadata and download links.
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

The page already supplies the full title and description. Do not reproduce the whole article inside a thumbnail. Match the established navy, cyan, white and amber visual palette. A large export is not evidence of thumbnail readability: inspect the actual small previews.

## Sources and review

- Prefer primary sources and distinguish their findings from TechMind Hub's assessment.
- Do not invent performance figures, deployments, benchmark results or social profile URLs.
- Build the site and check the article body, local links, metadata and media URLs before requesting release approval. Inspect the feed card and live page after deployment.

## Public article presentation

Andrew confirmed removal of both public Download links on October 24, 2026. Do not add article Markdown or infographic Download buttons/links to public articles. Keep editable article sources and social text in GitHub for Andrew. Publication images remain public through R2; removing a link does not make an image private. Do not create duplicate Markdown exports under `public/` for new articles. This policy does not change bucket permissions.
