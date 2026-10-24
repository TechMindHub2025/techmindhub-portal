# TechMind Hub

Astro site published to https://techmindhub.cc through GitHub Pages.

Start with [AGENTS.md](AGENTS.md), the [publishing workflow](editorial/README.md)
and the [visual canon](editorial/VISUAL-CANON.md). The
[approved reference](editorial/REFERENCE.md) records examples and check coverage.

## Development and validation

Use Node 20 and Python 3 (standard library only).

```sh
npm ci
npm run dev
```

Before review:

```sh
npm run validate
```

This builds the site, tests the publication guard against known regressions, and
checks every generated HTML page. `npm run check:publication` can recheck an
existing build. PR checks also reject publication image binaries in the diff;
the Pages workflow validates before uploading its deployment artifact.

Code, article Markdown and editorial briefs live here. Publication images live
in Cloudflare R2; do not add them to the repository or embed them as Base64.
Andrew approves the final PR head in GitHub before release. See the publishing
workflow for image upload, factual review, visual QA and deployment verification.
