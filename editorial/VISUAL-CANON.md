# TechMind Hub visual canon — v1.1

Approved direction with Andrew on October 24, 2026; revised the same day to require generated designer-led covers and editorial infographics, with sources retained in the article rather than on the images. Andrew authorised preparation of the complete three-publication replacement set. Publication still follows the normal R2 verification and human GitHub review workflow.

## One publication, one visual argument

Start with the article's central question and one visual metaphor. Design a cover and an explanatory image from the same brief. They share the main object or transformation, subject palette, typographic character and restrained TechMind Hub signature. They need different compositions and levels of detail. Never reduce an infographic into a thumbnail or merely recolour one generic composition across disciplines.

The cover identifies the idea; the inner illustration explains a mechanism, comparison, sequence or argument. Use photography, illustration, diagrams or a combination according to the subject. Do not force every story into an isometric device, card grid, robot, microscope or glowing brain.

## Direction and palette registry

`src/data/editorial-domains.json` is the single machine-readable registry for IDs, English labels, accent colours and light surfaces. It also supplies the public About-page palette key. Each article has one primary `domain`; tags describe additional subjects. `topic` remains the short, human-facing section label. Choose the primary domain by the article's central question, not the first technology mentioned: evaluation of agent safeguards belongs to `digital-trust`, even when AI is a tag.

| ID | Direction | Accent | Light surface |
| --- | --- | --- | --- |
| ai | AI & machine learning | #5958B2 | #F0EFFA |
| software | Software & developer tools | #80549E | #F5EFF8 |
| digital-trust | Security & digital trust | #966020 | #FBF3E6 |
| photonics | Photonics, physics & quantum | #267F9E | #EDF7FA |
| robotics | Robotics & automation | #AC5943 | #FAF0EB |
| infrastructure | Infrastructure, cloud & networks | #426F94 | #EEF3F8 |
| life-sciences | Life sciences & biotechnology | #39765E | #EEF6F0 |
| energy-environment | Energy, climate & environment | #6E793D | #F3F5E9 |
| space | Space & astronomy | #70558D | #F3EFF8 |
| materials | Materials & manufacturing | #956848 | #F7F1EB |

A family is a starting point, not a flat compulsory background. Use restrained gradients, neutral space, materials and subject-specific secondary tones. Keep at least one unmistakable family cue in both images. Dark regions or occasional dark scenes are allowed when the subject needs them. Keep text readable independently of the accent. Display a written domain/topic label; colour alone must never carry classification or meaning.

To add a direction: first check whether an existing family fits; add one stable unique ID with label/accent/surface to the registry; document the choice here; choose a palette distinct enough from its neighbours and inspect readable labels on its surface; build and review the public palette key and sample artwork. Never rename existing IDs casually or silently change their colours. Optional legacy metadata is tolerated; assign a valid domain to every new publication.

## Typography and cover text

Use a clean humanist sans-serif such as the site's system stack, with strong title weight and calm regular explanatory text. Establish a family resemblance through hierarchy, spacing and signature rather than identical layouts. Keep generous edge margins and an intentional focal point.

Default cover text: one meaningful English phrase of roughly 2–5 words. It may be a short question, concept or product name; it need not reproduce the full article title. Text-free covers are an intentional exception when the subject is self-explanatory. No paragraphs, terminal commands, tiny diagrams, unsupported promises or benchmark figures on covers. The full title and description remain in accessible HTML.

Use the exact English words from the reviewed brief. Inspect generated letters and symbols; do not accept almost-correct text. Keep the established logo unchanged if used; a small typographic TECHMIND HUB signature is sufficient. Do not invent a new logo for each article.

## Asset roles

| Role | Working format | Acceptance |
| --- | --- | --- |
| Cover | 16:9; target master 1200 x 675 or a larger native output near that ratio | Inspect at 352px and 260px; subject and short phrase must remain legible. |
| Article infographic | Usually 4:5; suggested 1200 x 1500 or a native output near that ratio | Readable explanatory structure, controlled copy; preserve essential information on the article's narrow layout. |
| Social link preview | 1200 x 630 | Export separately when crop safety is uncertain; never stretch a 16:9 image into this ratio. |
| Optional social adaptation | Platform-specific | Compose deliberately; do not squeeze the complete infographic into an unsuitable frame. |

For cover reuse in 1200 x 630, keep essential content inside a safe region of at least 6% from all edges and test the actual crop. Keep native generated output when its aspect ratio closely matches the target; do not stretch it to force pixel dimensions. Scale text and labels for their displayed size. A single large infographic may require an accessible text equivalent in the article. When too much material is needed, use two clear figures rather than smaller type.

## Accuracy and accessibility

- Separate artistic metaphors, conceptual functional diagrams and faithful apparatus diagrams. Label a concept as a concept. A glass panel on a cover must not become a claim about the actual apparatus.
- Every arrow must have a defined direction and meaning. Distinguish optical paths, electronic feedback and readout. Do not ask the image generator to invent precise apparatus diagrams or quantitative charts. These editorial infographics use conceptual artwork and reviewed explanatory text. If a story needs a precise technical figure, handle it as a separate source-grounded figure; do not silently substitute a code-made editorial image for the generated visual the user requested.
- Attribute reported findings to the authors; include task, scope and denominator with performance figures. Keep source links, author attribution, research identifiers and detailed scope in the article text. Do not print author names, arXiv IDs, DOIs, source URLs, bibliography blocks or source footnotes on editorial covers or infographics. Do not turn a task result into a universal superiority claim.
- Do not invent measured curves, numerical axes, laboratory photographs, equipment, guarantees or replication. Distinguish proposed evaluation criteria from findings.
- Write `card_alt` for the cover and `cover_alt` for the inner illustration. Long figure descriptions or text equivalents belong in the article. Never make the only explanation available as raster text.
- Check text contrast on the actual background, labels without relying on colour, spelling, units, source identifiers and mobile readability.

## Common production brief

Record: article slug and source links; primary domain and palette; central question; one-sentence visual argument; shared motif; exact cover phrase; inner-image explanation and exact labels; visual-metaphor/apparatus status; claims and limitations; alt text; role-specific sizes and crop safety; filenames and version; review status.

Production sequence: verify the article and sources → agree on the paired brief → make cover and inner figure → inspect them together and at small size → review facts and typography → export versioned ordinary image files → upload to R2 → verify public URLs → obtain Andrew's GitHub review of the final PR head → merge and check deployment. Andrew approved proceeding with all three publication pairs after the initial photonics review; prepare the full set together when that scope is explicitly requested.

## Generation and image text

Use the built-in image generator for the finished cover and editorial infographic. Build each pair from one reviewed brief and use the cover as a style/subject reference for the companion. Prior SVG-made editorial candidates are superseded for this release. Coding is used for the website, metadata and packaging, not as an unannounced substitute for generated publication art.

Keep the source bibliography, author attribution, IDs, source links and detailed caveats in the article. Image copy consists of the short cover phrase or infographic title, a small category label, useful explanatory headings/sentences and the restrained TECHMIND HUB signature. Do not add section numbers such as 01/02 or numbered decorative badges. Scientific figures required by the subject are distinct from decorative numbering; none are needed in this three-publication image set.

## Storage and release

Code, this canon, registry, article Markdown and text briefs belong in GitHub. Publication image binaries belong in Cloudflare R2 `tmh-assets/posts/`; never send large Base64 payloads through tool outputs or store them in article code. Keep source artwork and prompts with the review package when available. Do not add public Download controls or duplicate article exports. Do not overwrite live approved images while a new pair is under review.

The previous cover-only v3 ZIP and the first SVG photonics pilot are superseded. The prepared replacement set is `TechMindHub-Cloudflare-images-canon-v2.zip`: exactly six PNG files (one cover and one infographic per article), with no source/document files in the upload archive. Its exact names, sizes, hashes and public URLs are recorded in `editorial/releases/2026-10-24-canon-v2.json`. New article URLs and text equivalents must match that set. Keep PR #23 draft until the files are uploaded to R2 and their public URLs verified, then obtain Andrew's approval on the final PR head before merging. Retain previous R2 images until the new deployment is verified.
