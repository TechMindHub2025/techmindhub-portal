"""Offline release-gate and idempotency tests; no GitHub writes or network."""

import unittest

from async_merge import (
    APIError,
    MergeError,
    TransportError,
    checks_passed,
    event_target,
    merge_approved,
    merge_uuid,
    preflight,
    pr_url,
)


SHA = "a" * 40
UUID = "12345678-1234-1234-1234-123456789abc"
RUN_URL = (
    "/repos/TechMindHub2025/techmindhub-portal/actions/workflows/publication-checks.yml/runs"
    f"?event=pull_request&head_sha={SHA}&per_page=100"
)


def pr(*, merged=False, head=SHA, author="TechMindHub2025", state="open", draft=False):
    return {
        "merged": merged,
        "state": state,
        "draft": draft,
        "user": {"login": author},
        "base": {"ref": "main"},
        "head": {"sha": head, "repo": {"full_name": "TechMindHub2025/techmindhub-portal"}},
    }


def review(*, state="APPROVED", commit=SHA, submitted="2026-11-16T10:00:00Z"):
    return {
        "id": 1,
        "state": state,
        "commit_id": commit,
        "submitted_at": submitted,
        "user": {"login": "AR1314"},
    }


def runs(number=71, conclusion="success"):
    return {"workflow_runs": [
        {
            "name": "Publication checks",
            "head_sha": SHA,
            "status": "completed",
            "conclusion": conclusion,
            "pull_requests": [{"number": number}],
        }
    ]}


class FakeGitHub:
    def __init__(self, number=71, reviews=None, check_runs=None, pr_states=None, put_result=None, statuses=None):
        self.number = number
        self.reviews = [review()] if reviews is None else reviews
        self.check_runs = runs(number) if check_runs is None else check_runs
        self.pr_states = [pr()] if pr_states is None else pr_states
        self.put_result = (202, {"status": "pending", "details": {"uuid": UUID}}) if put_result is None else put_result
        self.statuses = [(200, {"status": "merged", "details": {"sha": "b" * 40}})] if statuses is None else statuses
        self.calls = []
        self.pr_reads = 0
        self.status_reads = 0

    def call(self, method, path, body=None):
        self.calls.append((method, path, body))
        if method == "GET" and path == pr_url(self.number):
            result = self.pr_states[min(self.pr_reads, len(self.pr_states) - 1)]
            self.pr_reads += 1
            return 200, result
        if method == "GET" and "/reviews?" in path:
            return 200, self.reviews
        if method == "GET" and path == RUN_URL:
            return 200, self.check_runs
        if method == "PUT" and path.endswith("/merge-async"):
            if isinstance(self.put_result, Exception):
                raise self.put_result
            return self.put_result
        if method == "GET" and f"/merge-async/{UUID}" in path:
            result = self.statuses[min(self.status_reads, len(self.statuses) - 1)]
            self.status_reads += 1
            return result
        raise AssertionError(f"Unexpected API call: {method} {path}")

    @property
    def puts(self):
        return [call for call in self.calls if call[0] == "PUT"]


class AsyncMergeTests(unittest.TestCase):
    def test_ready_preflight_is_bound_to_reviewed_sha_and_this_pr_ci(self):
        self.assertEqual(preflight(FakeGitHub(), 71), ("ready", SHA))

    def test_dry_run_never_submits(self):
        api = FakeGitHub()
        self.assertIn("dry run", merge_approved(api, 71, dry_run=True))
        self.assertEqual(api.puts, [])

    def test_refuses_missing_review_without_submitting(self):
        api = FakeGitHub(reviews=[])
        self.assertIn("awaiting AR1314", merge_approved(api, 71))
        self.assertEqual(api.puts, [])

    def test_refuses_stale_or_dismissed_review(self):
        stale = FakeGitHub(reviews=[review(commit="c" * 40)])
        self.assertIn("awaiting AR1314", merge_approved(stale, 71))
        dismissed = FakeGitHub(reviews=[review(), {**review(state="DISMISSED", submitted="2026-11-16T12:00:00Z"), "id": 2}])
        self.assertIn("awaiting AR1314", merge_approved(dismissed, 71))

    def test_refuses_failed_or_wrong_pr_ci(self):
        failed = FakeGitHub(check_runs=runs(conclusion="failure"))
        self.assertIn("awaiting successful", merge_approved(failed, 71))
        wrong = FakeGitHub(check_runs=runs(number=70))
        self.assertFalse(checks_passed(wrong, 71, SHA))
        self.assertIn("awaiting successful", merge_approved(wrong, 71))

    def test_refuses_untrusted_author_and_fork(self):
        bad_author = FakeGitHub(pr_states=[pr(author="stranger")])
        with self.assertRaisesRegex(MergeError, "author"):
            merge_approved(bad_author, 71)
        forked = pr()
        forked["head"]["repo"]["full_name"] = "stranger/fork"
        with self.assertRaisesRegex(MergeError, "External fork"):
            merge_approved(FakeGitHub(pr_states=[forked]), 71)

    def test_async_202_polls_and_confirms_merged_pr(self):
        api = FakeGitHub(pr_states=[pr(), pr(merged=True)], statuses=[
            (200, {"status": "pending", "details": {"uuid": UUID, "merge_method": "squash", "merge_action": "direct_merge", "expected_head_sha": SHA, "bypass_rules": False}}),
            (200, {"status": "merged", "details": {"sha": "b" * 40}}),
        ])
        self.assertEqual(merge_approved(api, 71, sleep=lambda _: None, interval=0), "merged")
        self.assertEqual(len(api.puts), 1)
        self.assertEqual(api.puts[0][2], {"sha": SHA, "merge_method": "squash", "merge_action": "direct_merge", "bypass_rules": False})

    def test_409_resumes_matching_pending_uuid_without_duplicate_put(self):
        api = FakeGitHub(
            put_result=APIError(409, {"status": "pending", "details": {"uuid": UUID, "expected_head_sha": SHA, "merge_method": "squash"}}),
            pr_states=[pr(), pr(merged=True)],
        )
        self.assertEqual(merge_approved(api, 71), "merged")
        self.assertEqual(len(api.puts), 1)

    def test_409_mismatch_refuses_to_resume(self):
        api = FakeGitHub(put_result=APIError(409, {"details": {"uuid": UUID, "expected_head_sha": "c" * 40}}))
        with self.assertRaisesRegex(MergeError, "different PR head"):
            merge_approved(api, 71)

    def test_unknown_write_timeout_is_not_resubmitted(self):
        api = FakeGitHub(put_result=TransportError("timeout"), pr_states=[pr(), pr()])
        with self.assertRaisesRegex(MergeError, "outcome unknown"):
            merge_approved(api, 71)
        self.assertEqual(len(api.puts), 1)

    def test_resume_uuid_polls_without_put(self):
        api = FakeGitHub(pr_states=[pr(), pr(merged=True)])
        self.assertEqual(merge_approved(api, 71, resume_uuid=UUID), "merged")
        self.assertEqual(api.puts, [])

    def test_poll_timeout_does_not_resubmit(self):
        api = FakeGitHub(statuses=[(200, {"status": "pending", "details": {"uuid": UUID}})])
        with self.assertRaisesRegex(MergeError, "still pending"):
            merge_approved(api, 71, attempts=2, interval=0, sleep=lambda _: None)
        self.assertEqual(len(api.puts), 1)

    def test_200_already_merged_requires_readback(self):
        api = FakeGitHub(put_result=(200, {"status": "merged"}), pr_states=[pr(), pr(merged=True)])
        self.assertEqual(merge_approved(api, 71), "merged")

    def test_extract_uuid_rejects_invalid_or_missing(self):
        self.assertIsNone(merge_uuid({"status": "pending"}))
        self.assertIsNone(merge_uuid({"details": {"uuid": "not-a-uuid"}}))
        self.assertEqual(merge_uuid({"details": {"uuid": UUID}}), UUID)

    def test_release_event_filters_and_manual_dry_run(self):
        approve = {"review": {"state": "approved", "user": {"login": "AR1314"}}, "pull_request": {"number": 71}}
        self.assertEqual(event_target(approve, "pull_request_review"), ([71], None, False))
        approve["review"]["user"]["login"] = "stranger"
        self.assertEqual(event_target(approve, "pull_request_review"), ([], None, False))
        workflow = {"workflow_run": {"name": "Publication checks", "event": "pull_request", "conclusion": "success", "pull_requests": [{"number": 71}]}}
        self.assertEqual(event_target(workflow, "workflow_run"), ([71], None, False))
        manual = {"inputs": {"pr_number": "71", "resume_uuid": UUID, "dry_run": "true"}}
        self.assertEqual(event_target(manual, "workflow_dispatch"), ([71], UUID, True))


if __name__ == "__main__":
    unittest.main()
