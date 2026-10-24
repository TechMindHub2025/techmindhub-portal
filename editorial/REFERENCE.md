# Approved publication reference

Baseline confirmed with Andrew on 2026-10-24, after PR #24, main commit
`13d11581c8040d0b464fc53e6430830eaa28ea79`. This identifies an inspectable version,
not a requirement to freeze future article wording or copy one composition.

| Example | Domain | Live page |
| --- | --- | --- |
| Computing with Scattered Light | photonics | https://techmindhub.cc/posts/computing-with-scattered-light/ |
| Who Monitors the AI Monitor? | digital-trust | https://techmindhub.cc/posts/who-monitors-the-ai-monitor/ |
| Reproducible Python Still Needs Maintenance | software | https://techmindhub.cc/posts/uv-reproducible-python-maintenance/ |

The matching generated image pairs are identified in
`releases/2026-10-24-canon-v2.json`; prompts and exact artwork copy are in
`briefs/2026-10-24-generated-pairs.md`. Follow the current visual canon, using
these examples to assess the result. Read the source at the baseline commit if
a later revision makes comparison uncertain.

## Repeatable checks

Run `npm run validate` from the project root. Node builds Astro; Python 3's
standard library checks the output, with no additional Python packages.

The guard checks all generated HTML, including future publications:

- external HTTP(S) anchors have a new-tab target and both rel protections;
- published articles have one header, one infographic before the body, nonempty
  body text, no repeated hero, nonempty image alt text and R2 publication URLs;
- article controls contain no Download link/button or download attribute;
- known leaked “Illustration summary” captions and stray template delimiters
  do not appear as page text (scripts/styles are excluded);
- Home retains Latest, Topics, discussion section and footer;
- publication source contains no embedded image data URL, and `public/` contains
  no duplicate Markdown exports;
- published content metadata requires a registered domain, topic, alt text and
  separate R2 WebP card/infographic URLs and a dedicated JPEG `cover_og` through
  Astro's schema; generated OG/Twitter metadata must agree on that JPEG;
- PR diffs add or change no publication image binaries under `src/` or
  `public/posts/`. Existing historical files are not deleted by this policy.

The `Publication checks / Validate publication` PR job runs this command. The
Pages deployment workflow also validates before uploading the site artifact.
Adding a workflow does not itself make its status a required branch-protection
check; repository protections and human approval rules remain unchanged.

## Human review still required

Automation does not judge the quality of generated artwork, factual correctness,
mobile composition or public R2 availability. Review the exact image copy and
primary sources; inspect cover previews at 352px and 260px and article images on
a narrow viewport. Open the actual media URLs and click an external source.

For a visual change, attach desktop/mobile screenshots and cover previews to the
PR. For rules/checks-only changes, record which product files and output were
compared, including any differences, instead of adding unrelated screenshots.
After deployment, check the live Home, archive and affected articles.

## Changing the rules

Discuss proposed changes with Andrew first. Record the agreed change and reason
in the PR, update the relevant canon/workflow document and checks together, and
obtain Andrew's GitHub approval on the resulting final head. Do not silently
reinterpret an exception as the new default.
