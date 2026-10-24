# Publication image delivery

Agreed with Andrew on 2026-10-25: deliver original PNG artwork for his archive
and social work, and separate optimized files for the public R2 bucket. Artwork
continues to come from the image generator; delivery encoding is deterministic.

## Files per publication

| Role | Filename | Export |
| --- | --- | --- |
| Feed card | `<slug>-card-web-vN.webp` | 800px wide, original aspect ratio, no crop; lossless WebP after resizing |
| Article infographic | `<slug>-infographic-web-vN.webp` | Original pixel dimensions; lossless WebP, decoded pixels identical to the PNG |
| Social link preview | `<slug>-og-web-vN.jpg` | 1200×630, centre crop from the original cover; JPEG quality 95 with 4:4:4 chroma |

The cover resize changes its pixel grid. Lossless encoding then preserves that
resized result; do not describe it as identical to the full-size original.
The JPEG preview is also a derivative, not a lossless original. Inspect the crop
for every cover so no essential artwork or lettering is removed. The full-size
PNG pair stays unchanged in Andrew's originals archive.

Published frontmatter uses `cover_card`, `cover_hero` and `cover_og` for these three
R2 URLs. Alt text continues to describe the same artwork. OG and Twitter metadata
use the dedicated JPEG, rather than the small feed card or a deleted PNG.

## Production and packaging

1. Finish and review the generated PNG pair; keep its bytes unchanged.
2. Export the three delivery derivatives. WebP lossless with encoder effort 6
   is the current conservative profile. Native output dimensions are recorded,
   not stretched to force a ratio.
3. Decode the infographic and its PNG and compare the RGBA pixel buffers exactly.
   Compare the decoded card against the deterministic resized PNG result.
4. Inspect cards at 352px and 260px, article images on desktop/mobile and every
   social-preview crop. Record output hashes, dimensions and encoding settings.
5. Deliver two separate ZIPs: `Originals-PNG` for Andrew (two untouched PNGs per
   article) and `Cloudflare-Web` (three web derivatives per article, flat archive,
   no source files or working notes). Only Cloudflare-Web is uploaded to `posts/`.
6. Verify all new canonical R2 URLs, obtain Andrew's GitHub approval of the final
   head, then merge and verify the live site as usual.

The initial lossy WebP experiment achieved smaller sizes at quality 92, but that
was not pixel-preserving. This migration deliberately prioritizes exact pixels
for text-heavy infographics. Do not silently substitute that earlier lossy test
for the agreed lossless delivery profile.

## Migration and deletion

The six-publication migration is recorded in
`releases/2026-10-25-web-migration-v1.json`. Its upload ZIP contains 12 WebP images
and six JPEG social previews. The originals ZIP contains exactly 12 PNGs.

Keep the previous public PNGs while the PR is pending. After the new files load,
the approved PR deploys, and live pages/previews are verified, Andrew may remove
the superseded PNG objects. First ensure the originals archive is saved. Check
the built site for old image references, including OG/Twitter metadata. Historical
release records retain old URLs as provenance; they are not live page references.
Never delete branding or unrelated assets as part of this migration.
