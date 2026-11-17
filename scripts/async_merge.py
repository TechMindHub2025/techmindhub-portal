#!/usr/bin/env python3
"""Fail-closed, asynchronous GitHub pull-request merge for TechMind Hub.

This runs on the trusted default branch after a human review and successful CI.
It never bypasses repository rules or checks out untrusted pull-request code.
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPOSITORY = "TechMindHub2025/techmindhub-portal"
AUTHOR = "TechMindHub2025"
REVIEWER = "AR1314"
BASE_BRANCH = "main"
CHECK_WORKFLOW = "Publication checks"
MERGE_METHOD = "squash"
API_VERSION = "2026-03-10"
UUID_RE = re.compile(r"^[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$")


class APIError(Exception):
    def __init__(self, status: int, body: dict):
        self.status = status
        self.body = body
        super().__init__(f"GitHub API HTTP {status}: {body.get('message', 'request failed')}")


class TransportError(Exception):
    """A transport error may mean that the write reached GitHub."""


class MergeError(Exception):
    pass


class GitHub:
    def __init__(self, token: str):
        self.token = token

    def call(self, method: str, path: str, body: dict | None = None) -> tuple[int, dict]:
        request = Request(
            f"https://api.github.com{path}",
            method=method,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": API_VERSION,
                "User-Agent": "TechMindHub-async-release-merge",
                "Content-Type": "application/json",
            },
        )
        try:
            with urlopen(request, timeout=20) as response:
                raw = response.read()
                return response.status, json.loads(raw) if raw else {}
        except HTTPError as exc:
            try:
                payload = json.loads(exc.read())
            except (ValueError, UnicodeDecodeError):
                payload = {"message": "Non-JSON GitHub error response"}
            raise APIError(exc.code, payload) from exc
        except (URLError, TimeoutError, OSError) as exc:
            # Never automatically replay a write after an ambiguous timeout.
            raise TransportError(f"GitHub transport error: {type(exc).__name__}") from exc


def details(payload: dict) -> dict:
    nested = payload.get("details")
    return nested if isinstance(nested, dict) else payload


def merge_uuid(payload: dict) -> str | None:
    data = details(payload)
    candidate = data.get("uuid") or payload.get("uuid")
    return candidate if isinstance(candidate, str) and UUID_RE.fullmatch(candidate) else None


def validate_existing_request(payload: dict, head_sha: str) -> None:
    """A 409 is resumable only when GitHub's pending request matches our intent."""
    data = details(payload)
    existing_sha = data.get("expected_head_sha") or data.get("sha")
    if existing_sha and existing_sha != head_sha:
        raise MergeError("Existing merge request targets a different PR head; stop.")
    if data.get("merge_method") not in (None, MERGE_METHOD):
        raise MergeError("Existing merge request uses another merge method; stop.")
    if data.get("merge_action") not in (None, "direct_merge"):
        raise MergeError("Existing merge request uses another merge action; stop.")
    if data.get("bypass_rules") is True:
        raise MergeError("Existing merge request bypasses protections; stop.")


def pr_url(number: int) -> str:
    return f"/repos/{REPOSITORY}/pulls/{number}"


def approved_head(api, number: int, sha: str) -> bool:
    page = 1
    all_reviews = []
    while True:
        _, reviews = api.call("GET", f"{pr_url(number)}/reviews?per_page=100&page={page}")
        all_reviews.extend(reviews)
        if len(reviews) < 100:
            break
        page += 1
    reviewers = [r for r in all_reviews if r.get("user", {}).get("login") == REVIEWER]
    if not reviewers:
        return False
    latest = max(reviewers, key=lambda r: (r.get("submitted_at") or "", r.get("id") or 0))
    return latest.get("state") == "APPROVED" and latest.get("commit_id") == sha


def checks_passed(api, number: int, sha: str) -> bool:
    url = (
        f"/repos/{REPOSITORY}/actions/workflows/publication-checks.yml/runs"
        f"?event=pull_request&head_sha={quote(sha)}&per_page=100"
    )
    _, response = api.call("GET", url)
    for run in response.get("workflow_runs", []):
        numbers = {p.get("number") for p in run.get("pull_requests", [])}
        if (
            run.get("name") == CHECK_WORKFLOW
            and run.get("head_sha") == sha
            and number in numbers
            and run.get("status") == "completed"
            and run.get("conclusion") == "success"
        ):
            return True
    return False


def preflight(api, number: int) -> tuple[str, str | None]:
    _, pr = api.call("GET", pr_url(number))
    if pr.get("merged"):
        return "already merged", None
    if pr.get("state") != "open" or pr.get("draft"):
        return "PR is closed or draft", None
    if pr.get("base", {}).get("ref") != BASE_BRANCH:
        raise MergeError("Target branch is not main.")
    if pr.get("head", {}).get("repo", {}).get("full_name") != REPOSITORY:
        raise MergeError("External fork PR is not eligible for automatic merge.")
    if pr.get("user", {}).get("login") != AUTHOR:
        raise MergeError("PR author is not the TechMind Hub publisher.")
    sha = pr.get("head", {}).get("sha")
    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise MergeError("Missing or invalid PR head SHA.")
    if not approved_head(api, number, sha):
        return "awaiting AR1314 approval of current head", None
    if not checks_passed(api, number, sha):
        return "awaiting successful Publication checks for this PR", None
    return "ready", sha


def poll_merge(api, number: int, uuid: str, sha: str, *, sleep=time.sleep, attempts=30, interval=10) -> str:
    for attempt in range(attempts):
        _, result = api.call("GET", f"{pr_url(number)}/merge-async/{uuid}")
        state = result.get("status")
        if state == "pending":
            validate_existing_request(result, sha)
            if attempt + 1 < attempts:
                sleep(interval)
            continue
        if state == "merged":
            _, pr = api.call("GET", pr_url(number))
            if not pr.get("merged"):
                raise MergeError(f"Merge reports success, but PR state not updated yet; inspect UUID {uuid}.")
            return "merged"
        if state == "enqueued":
            return "enqueued (not merged; verify queue and eventual PR status)"
        if state == "failed":
            raise MergeError(f"Async merge failed: {details(result).get('message', 'unknown reason')}")
        raise MergeError(f"Unknown async merge status {state!r}; inspect UUID {uuid}.")
    raise MergeError(f"Async merge still pending after polling; UUID {uuid}. Do not resubmit blindly.")


def merge_approved(api, number: int, *, resume_uuid: str | None = None, dry_run=False,
                   sleep=time.sleep, attempts=30, interval=10) -> str:
    status, sha = preflight(api, number)
    if status != "ready":
        return f"skipped: {status}"
    if dry_run:
        return f"dry run: approved and CI-passed PR #{number} at {sha}"
    if resume_uuid:
        if not UUID_RE.fullmatch(resume_uuid):
            raise MergeError("Invalid resume UUID.")
        return poll_merge(api, number, resume_uuid, sha, sleep=sleep, attempts=attempts, interval=interval)
    intent = {
        "sha": sha,
        "merge_method": MERGE_METHOD,
        "merge_action": "direct_merge",
        "bypass_rules": False,
    }
    try:
        code, response = api.call("PUT", f"{pr_url(number)}/merge-async", intent)
    except APIError as exc:
        if exc.status != 409:
            raise
        response = exc.body
        validate_existing_request(response, sha)
        code = 409
    except TransportError as exc:
        _, pr = api.call("GET", pr_url(number))
        if pr.get("merged"):
            return "merged (confirmed after ambiguous transport error)"
        raise MergeError(
            "Submission timed out; merge outcome unknown. No automatic resubmission. "
            "Inspect the PR and use a later controlled resume."
        ) from exc
    if code == 200:
        if response.get("status") == "merged":
            _, pr = api.call("GET", pr_url(number))
            if not pr.get("merged"):
                raise MergeError("GitHub reports merged but PR readback is not merged yet.")
            return "merged"
        if response.get("status") == "enqueued":
            return "enqueued (not merged; follow queue status)"
        raise MergeError("Unexpected 200 response; did not confirm merge.")
    if code not in (202, 409):
        raise MergeError(f"Unexpected async response {code}.")
    uuid = merge_uuid(response)
    if not uuid:
        raise MergeError(f"Async request returned HTTP {code} without a UUID; do not resubmit blindly.")
    return poll_merge(api, number, uuid, sha, sleep=sleep, attempts=attempts, interval=interval)


def event_target(event: dict, event_name: str) -> tuple[list[int], str | None, bool]:
    """Only trusted release signals can ask the script to consider a PR."""
    if event_name == "pull_request_review":
        review = event.get("review") or {}
        if review.get("state") != "approved" or review.get("user", {}).get("login") != REVIEWER:
            return [], None, False
        return [event["pull_request"]["number"]], None, False
    if event_name == "workflow_run":
        run = event.get("workflow_run") or {}
        if run.get("name") != CHECK_WORKFLOW or run.get("conclusion") != "success" or run.get("event") != "pull_request":
            return [], None, False
        return sorted({p["number"] for p in run.get("pull_requests", []) if isinstance(p.get("number"), int)}), None, False
    if event_name == "workflow_dispatch":
        inputs = event.get("inputs") or {}
        number = int(inputs["pr_number"])
        return [number], inputs.get("resume_uuid") or None, str(inputs.get("dry_run", "true")).lower() != "false"
    return [], None, False


def signal_pages_deploy(result: str, output_path: str | None) -> bool:
    """Request deployment only after GitHub confirms the PR is merged."""
    if result not in ("merged", "merged (confirmed after ambiguous transport error)"):
        return False
    if not output_path:
        raise MergeError("GITHUB_OUTPUT is required after a confirmed merge.")
    with open(output_path, "a", encoding="utf-8") as stream:
        stream.write("merged=true\n")
    return True


def main() -> int:
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY:
        raise MergeError("Wrong repository; merge disabled.")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise MergeError("GITHUB_TOKEN is required (never supply it as a CLI argument).")
    with open(os.environ["GITHUB_EVENT_PATH"], encoding="utf-8") as stream:
        event = json.load(stream)
    numbers, resume_uuid, dry_run = event_target(event, os.environ.get("GITHUB_EVENT_NAME", ""))
    if not numbers:
        print("No eligible PR in this event; no merge submitted.")
        return 0
    api = GitHub(token)
    for number in numbers:
        if number <= 0:
            raise MergeError("Invalid PR number.")
        result = merge_approved(api, number, resume_uuid=resume_uuid, dry_run=dry_run)
        print(f"PR #{number}: {result}")
        if signal_pages_deploy(result, os.environ.get("GITHUB_OUTPUT")):
            print("Confirmed merge: Pages deployment will be dispatched.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (APIError, MergeError, TransportError, ValueError, KeyError) as exc:
        print(f"Async merge stopped safely: {exc}", file=sys.stderr)
        sys.exit(1)
