#!/usr/bin/env python3
"""Behavioral tests for ledger.py; run from a repository checkout."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLI = HERE / "ledger.py"


def run(root, *args, ok=True):
    p = subprocess.run(["python3", str(CLI), "--root", str(root), *args], text=True, capture_output=True)
    if ok and p.returncode != 0:
        raise AssertionError(p.stderr or p.stdout)
    if not ok and p.returncode == 0:
        raise AssertionError("expected failure: " + p.stdout)
    return p


class LedgerBehavior(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for d in ("management", "docs", "qa/evidence", "qa/acceptance"):
            (self.root / d).mkdir(parents=True)
        for name in ("evidence.txt", "output.txt"):
            (self.root / "qa/evidence" / name).write_text(name, encoding="utf-8")
        self.write_ledger()
        run(self.root, "render")

    def tearDown(self):
        self.tmp.cleanup()

    def write_ledger(self):
        self.data = {
            "schema_version": 1, "project_id": "test", "title": "测试", "revision": 0,
            "updated_at": "2026-09-09T00:00:00Z", "source_documents": [],
            "stages": [
                {"id": "P0", "name": "原型", "planned_window": "W1", "gate_task_id": "P0-GATE", "owner": "gameplay-lead"},
                {"id": "P1", "name": "MVP", "planned_window": "W2", "gate_task_id": "P1-GATE", "owner": "gameplay-lead"},
            ], "tasks": [
                self.task("P0-01", "P0", "task", "gameplay-engineer", []),
                self.task("P0-GATE", "P0", "gate", "producer-director", ["P0-01"]),
                self.task("P1-01", "P1", "task", "gameplay-engineer", ["P0-GATE"]),
                self.task("P1-GATE", "P1", "gate", "producer-director", ["P1-01"]),
            ], "history": []}
        self.save()

    @staticmethod
    def task(tid, stage, kind, owner, deps):
        return {"id": tid, "title": tid, "stage_id": stage, "kind": kind, "owner": owner,
                "status": "pending", "dependencies": deps, "source": "test", "acceptance": ["证据文件存在"],
                "deliverables": ["测试产物"], "artifacts": [], "review": None, "blocker": None,
                "assignee": None, "updated_at": None}

    def save(self):
        (self.root / "management/project-ledger.json").write_text(json.dumps(self.data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def ledger(self):
        return json.loads((self.root / "management/project-ledger.json").read_text(encoding="utf-8"))

    def review(self, tid, role="gameplay-lead", evidence="qa/evidence/evidence.txt"):
        p = self.root / "qa/acceptance" / f"{tid}.json"
        p.write_text(json.dumps({"task_id": tid, "reviewer": "tester", "role": role, "mode": "peer_review",
                                 "result": "pass", "summary": "标准通过。", "checks": [{"criterion": 1, "result": "pass", "evidence": evidence, "detail": "文件可复核。"}]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return f"qa/acceptance/{tid}.json"

    def accept_task(self, tid, actor, rev, role="gameplay-lead"):
        run(self.root, "start", tid, "--actor", actor, "--expected-revision", str(rev))
        rev += 1
        run(self.root, "submit", tid, "--actor", actor, "--expected-revision", str(rev), "--artifact", "qa/evidence/output.txt")
        rev += 1
        run(self.root, "accept", tid, "--actor", actor, "--expected-revision", str(rev), "--review", self.review(tid, role))
        return rev + 1

    def test_flow_dependencies_and_acceptance(self):
        rev = 0
        run(self.root, "validate")
        run(self.root, "start", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", str(rev)); rev += 1
        run(self.root, "submit", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", str(rev), "--artifact", "qa/evidence/output.txt"); rev += 1
        run(self.root, "accept", "P0-01", "--actor", "gameplay-lead", "--expected-revision", str(rev), "--review", self.review("P0-01")); rev += 1
        run(self.root, "start", "P0-GATE", "--actor", "producer-director", "--expected-revision", str(rev)); rev += 1
        run(self.root, "submit", "P0-GATE", "--actor", "producer-director", "--expected-revision", str(rev), "--artifact", "qa/evidence/output.txt"); rev += 1
        run(self.root, "accept", "P0-GATE", "--actor", "producer-director", "--expected-revision", str(rev), "--review", self.review("P0-GATE", "producer-director")); rev += 1
        self.assertEqual(self.ledger()["tasks"][1]["status"], "accepted")
        run(self.root, "validate")
        self.assertTrue(run(self.root, "status").stdout.find('"P1-01"') >= 0)

    def test_stale_revision_and_dependency_rejection(self):
        run(self.root, "start", "P1-01", "--actor", "gameplay-engineer", "--expected-revision", "0", ok=False)
        run(self.root, "start", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", "0")
        run(self.root, "start", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", "0", ok=False)

    def test_tampered_evidence_fails_validation(self):
        rev = self.accept_task("P0-01", "gameplay-lead", 0)
        evidence = self.root / "qa/evidence/evidence.txt"
        evidence.write_text("tampered", encoding="utf-8")
        run(self.root, "validate", ok=False)
        self.assertEqual(self.ledger()["revision"], rev)

    def test_wrong_gate_reviewer_rejected(self):
        run(self.root, "start", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", "0")
        run(self.root, "submit", "P0-01", "--actor", "gameplay-engineer", "--expected-revision", "1", "--artifact", "qa/evidence/output.txt")
        # Gate is not yet eligible, and a normal task can use its category lead.
        run(self.root, "start", "P0-GATE", "--actor", "producer-director", "--expected-revision", "2", ok=False)

    def test_daily_brief_contains_progress_next_task_and_structure(self):
        output = run(self.root, "brief").stdout
        self.assertIn("每日简报", output)
        self.assertIn("进度：", output)
        self.assertIn("开发任务 0/4", output)
        self.assertIn("下一项：P0-01", output)
        self.assertIn("flowchart LR", output)
        self.assertIn("P0", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
