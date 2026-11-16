# Asynchronous, review-gated publication merge

The regular TechMind Hub release contract remains unchanged: the publisher
prepares a PR; Andrew approves the final PR head through `AR1314`; the
publication checks must pass; only then may the PR merge into protected `main`.
Images must already be uploaded and verified in R2. Social posting is manual.

## What changed

`.github/workflows/async-merge.yml` runs trusted
`scripts/async_merge.py` from `main` when either:

- `AR1314` submits an approval on a PR, or
- the `Publication checks` workflow succeeds for a PR.

Both triggers are needed because CI and human approval can arrive in either
order. An ineligible or not-yet-ready PR exits without merging. The workflow
uses the repository's `GITHUB_TOKEN` with narrowly defined permissions, and
never checks out the untrusted PR head.

This workflow is scoped to a non-draft PR from `TechMindHub2025` in the same
repository, targeting `main`. It requires an `AR1314` approval of the **exact
current head SHA**, plus a successful `Publication checks` run associated with
the **same PR and SHA**. GitHub's existing ruleset remains the final authority.
There is no bypass mode: `bypass_rules` is always `false`.

## Asynchronous operation and duplicate protection

The script uses GitHub's 2026-03-10 REST API:

- `PUT /repos/{owner}/{repo}/pulls/{number}/merge-async` with an expected head
  SHA, `merge_method: squash`, `merge_action: direct_merge` and no bypass.
- HTTP 202 returns a merge request UUID; the script polls
  `GET /repos/{owner}/{repo}/pulls/{number}/merge-async/{uuid}`.
- HTTP 409 means a request is already pending. Resume polling **only if** its
  metadata matches the expected head, merge method and protection policy.
- HTTP 200 is successful only when GitHub reports `merged` **and** a fresh PR
  read confirms `merged: true`. `enqueued` is not counted as merged.
- A timeout after submission is ambiguous. **Do not automatically submit a
  second merge request**; the script reads PR state once and stops if the
  outcome remains unknown.

All merge jobs are serialized by one GitHub Actions concurrency group targeting
`main`, with `cancel-in-progress: false`. GitHub's own per-PR async request ID
is the durable deduplication mechanism. Polling is bounded; a still-pending
request reports its UUID and stops without resubmission. A subsequent merge
attempt receives the existing request's UUID if GitHub still has it pending.

## Manual recovery / dry run

Open **Actions → Async merge approved publication → Run workflow** on `main`.
Enter a PR number. By default `dry_run = true`, which only checks review and CI
without issuing a merge request. To release an already approved PR, set
`dry_run = false` after checking the current head and approval.

If a previous async request returned a UUID but timed out while polling, enter
the **same UUID** under `resume_uuid` and set `dry_run = false`. This executes
only the status query, not another merge submission.

If a submit call itself timed out and no UUID was received, inspect the PR and
GitHub status. Re-run only after the service has recovered; the endpoint may
return 409 with the existing UUID, which the script checks before resuming.
Never work around this state by force-pushing `main`, dropping branch protection
or creating multiple equivalent release PRs.

GitHub may accept the merge request asynchronously and later reject the actual
merge due to rules, a newer head or failed checks. The workflow reports that
as a failed release; it does not bypass or silently retry the rejected merge.

## Deployment and limitations

Successful merge triggers the **existing** `Deploy Astro to GitHub Pages`
workflow via `push` to `main`. The async merge workflow does not claim that
the GitHub Pages deployment or live images have been verified. The release
owner still performs live QA after deployment.

Only the new workflow **after it reaches `main`** can automatically handle new
approval and CI events. Existing approved PRs, including #70 and #71 from the
November 16 GitHub incident, do not automatically re-trigger upon installation;
the manual workflow dispatch is the supported recovery path. Do not install
this by bypassing the active `protect-main` ruleset.

Tests: `npm run test:merge` (offline mocks of approvals, CI, 202, 409, timeouts,
stale reviews, polling and idempotence); included in `npm run validate`.

Primary reference:
https://docs.github.com/en/rest/pulls/pulls?apiVersion=2026-03-10
