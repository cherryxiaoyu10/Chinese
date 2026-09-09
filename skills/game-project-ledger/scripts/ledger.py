#!/usr/bin/env python3
"""Project ledger CLI; Python 3 stdlib only. JSON is authoritative; Markdown is derived."""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timezone

STATUSES = {"pending": "未开始", "in_progress": "开发中", "in_review": "待验收",
            "accepted": "已验收", "blocked": "阻塞", "needs_rework": "待返工"}
KINDS = {"task", "gate", "baseline"}
ROLES = {"producer-director", "gameplay-lead", "content-lead", "art-audio-lead",
         "tech-quality-lead", "lead-game-designer", "combat-card-designer",
         "map-event-designer", "economy-meta-designer", "curriculum-designer",
         "content-data-curator", "narrative-writer", "pixel-artist-animator",
         "ui-ux-designer", "audio-feedback-designer", "tech-lead",
         "gameplay-engineer", "tools-pipeline-engineer", "qa-playtest-analyst"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(root, value):
    require(isinstance(value, str) and value.strip(), "证据路径不能为空")
    require(not Path(value).is_absolute(), "产物/证据须使用项目相对路径")
    p = (root / value).resolve()
    require(p.is_relative_to(root), "产物/证据不能位于项目之外")
    require(p.is_file(), "产物/证据文件不存在：" + value)
    return p


def string_list(value, name, nonempty=True):
    require(isinstance(value, list) and (value or not nonempty), name + " 必须是列表")
    require(all(isinstance(x, str) and x.strip() for x in value), name + " 包含空值")


def review_check(root, task, review, recorded=False):
    require(isinstance(review, dict), "已验收任务缺少验收记录")
    require(review.get("task_id") == task["id"], "验收记录任务 ID 不匹配")
    require(review.get("result") == "pass", "只有通过的验收记录可以关闭任务")
    require(review.get("role") in ROLES, "验收角色无效")
    require(review.get("mode") in {"self_check", "peer_review", "user_review"}, "验收方式无效")
    require(isinstance(review.get("reviewer"), str) and review["reviewer"].strip(), "缺少实际验收者")
    require(isinstance(review.get("summary"), str) and review["summary"].strip(), "缺少验收结论")
    if task["kind"] == "gate":
        require(review["role"] == "producer-director", "阶段门由 producer-director 收口")
    checks = review.get("checks", [])
    require(isinstance(checks, list) and len(checks) == len(task["acceptance"]), "须逐条覆盖所有验收标准")
    require(all(isinstance(c, dict) and type(c.get("criterion")) is int for c in checks), "验收条目格式错误")
    require(sorted(c["criterion"] for c in checks) == list(range(1, len(checks) + 1)), "验收标准编号遗漏或重复")
    for c in checks:
        require(c.get("result") == "pass" and c.get("detail"), "存在未通过或未说明的标准")
        p = artifact(root, c.get("evidence"))
        if recorded:
            require(c.get("sha256") == digest(p), "验收证据已改变，需重开或恢复历史证据：" + c["evidence"])
    if recorded:
        p = artifact(root, review.get("source_file"))
        require(review.get("source_sha256") == digest(p), "验收记录文件已改变：" + review["source_file"])


def validate(root, data, verify_evidence=True):
    require(data.get("schema_version") == 1, "不支持的台账 schema_version")
    require(type(data.get("revision")) is int and data["revision"] >= 0, "revision 无效")
    require(data.get("project_id") and data.get("title"), "缺少项目标识")
    require(isinstance(data.get("history"), list), "history 必须为列表")
    stages = data.get("stages", [])
    require(stages and len({s["id"] for s in stages}) == len(stages), "阶段为空或重复")
    stage_ids = {s["id"] for s in stages}
    tasks = data.get("tasks", [])
    require(tasks and len({t["id"] for t in tasks}) == len(tasks), "任务为空或 ID 重复")
    index = {t["id"]: t for t in tasks}
    for t in tasks:
        require(re.fullmatch(r"[A-Z][A-Z0-9]*-(?:[0-9]{2,}|GATE)", t["id"]), "任务 ID 格式错误")
        require(t.get("stage_id") in stage_ids, "任务引用未知阶段")
        require(t.get("kind") in KINDS and t.get("status") in STATUSES, "任务类型/状态无效")
        require(t.get("owner") in ROLES, "任务负责人无效")
        require(t.get("title") and t.get("source"), "任务缺少标题或来源")
        for k in ("acceptance", "deliverables"):
            string_list(t.get(k), k)
        string_list(t.get("dependencies"), "dependencies", False)
        require(len(set(t["dependencies"])) == len(t["dependencies"]), "依赖重复")
        require(all(d in index and d != t["id"] for d in t["dependencies"]), "依赖不存在或自依赖")
        string_list(t.get("artifacts"), "artifacts", False)
        if t["status"] in {"in_progress", "in_review", "accepted"}:
            require(all(index[d]["status"] == "accepted" for d in t["dependencies"]), "前置依赖未验收：" + t["id"])
        if t["status"] in {"in_review", "accepted"}:
            require(t["artifacts"], "待验收任务缺少产物")
            for a in t["artifacts"]:
                artifact(root, a)
        if t["status"] == "blocked":
            require(t.get("blocker"), "阻塞任务缺少原因")
        if t["status"] == "accepted" and verify_evidence:
            review_check(root, t, t.get("review"), recorded=True)
    visiting, visited = set(), set()

    def visit(tid):
        require(tid not in visiting, "依赖形成循环：" + tid)
        if tid in visited:
            return
        visiting.add(tid)
        for dep in index[tid]["dependencies"]:
            visit(dep)
        visiting.remove(tid)
        visited.add(tid)

    for tid in index:
        visit(tid)
    for stage in stages:
        gate = stage.get("gate_task_id")
        if gate is not None:
            require(gate in index and index[gate]["kind"] == "gate" and index[gate]["stage_id"] == stage["id"], "阶段门无效")
            required = {t["id"] for t in tasks if t["stage_id"] == stage["id"] and t["id"] != gate}
            require(required <= set(index[gate]["dependencies"]), "阶段门未覆盖本阶段所有任务")
    revisions = [h.get("revision") for h in data["history"]]
    require(revisions == list(range(1, data["revision"] + 1)), "历史 revision 不连续")
    return index


def phase_status(stage, tasks):
    if all(t["status"] == "accepted" for t in tasks):
        return "已验收" if stage.get("gate_task_id") else "已交付"
    if any(t["status"] == "blocked" for t in tasks):
        return "有阻塞"
    gate = next((t for t in tasks if t["id"] == stage.get("gate_task_id")), None)
    if gate and all(t["status"] == "accepted" for t in tasks if t is not gate):
        return "待阶段验收"
    return "进行中" if any(t["status"] != "pending" for t in tasks) else "未开始"


def esc(value):
    return str(value).replace("|", "／").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def render(data):
    tasks = data["tasks"]
    index = {t["id"]: t for t in tasks}
    dev = [t for t in tasks if t["stage_id"] != "BASE"]
    accepted = sum(t["status"] == "accepted" for t in dev)
    lines = ["# 《文脉尖塔》项目台账", "", "> 由台账工具生成，请通过配套 Skill 更新；JSON 为唯一状态来源。", "",
             f"- 修订号：{data['revision']}；更新时间：{data['updated_at']}",
             f"- 开发与阶段门任务已验收：{accepted}/{len(dev)}（等权任务计数，不是工时完成率）",
             "- 基础文档交付单独统计，不代表 MVP、Demo 或产品验收通过。",
             "- [状态数据](../management/project-ledger.json) · [周期计划](PROJECT_PLAN.md) · [台账 Skill](../skills/game-project-ledger/SKILL.md)", "",
             "## 阶段总览", "", "|阶段|计划窗口|状态|已验收/任务总数|收口人|", "|---|---|---|---:|---|"]
    for stage in data["stages"]:
        items = [t for t in tasks if t["stage_id"] == stage["id"]]
        count = sum(t["status"] == "accepted" for t in items)
        lines.append(f"|{esc(stage['id'] + ' ' + stage['name'])}|{esc(stage['planned_window'])}|{phase_status(stage, items)}|{count}/{len(items)}|{stage['owner']}|")
    ready = [t for t in tasks if t["status"] in {"pending", "needs_rework"} and all(index[d]["status"] == "accepted" for d in t["dependencies"])]
    active = [t for t in tasks if t["status"] in {"in_progress", "in_review", "blocked"}]
    lines += ["", "## 当前任务与可开始项", ""]
    for t in active:
        lines.append(f"- **{t['id']} {STATUSES[t['status']]}**：{esc(t['title'])}；执行者：{esc(t.get('assignee') or '未登记')}；阻塞：{esc(t.get('blocker') or '无')}")
    if not active:
        lines.append("- 当前没有进行中、待验收或阻塞任务。")
    lines += ["", "满足前置依赖的任务（不代表已开工）：", ""]
    lines.extend(f"- {t['id']}：{esc(t['title'])}" for t in ready)
    for stage in data["stages"]:
        lines += ["", f"## {stage['id']} {stage['name']}", "", "|编号|任务|状态|负责人|前置任务|", "|---|---|---|---|---|"]
        items = [t for t in tasks if t["stage_id"] == stage["id"]]
        for t in items:
            lines.append(f"|{t['id']}|{esc(t['title'])}|{STATUSES[t['status']]}|{t['owner']}|{', '.join(t['dependencies']) or '无'}|")
        for t in items:
            lines += ["", "<details>", f"<summary>{t['id']} 验收标准与证据</summary>", "", f"来源：{esc(t['source'])}", "", "预期交付：" + "；".join(map(esc, t["deliverables"])), ""]
            lines.extend(f"{i}. {esc(c)}" for i, c in enumerate(t["acceptance"], 1))
            if t["artifacts"]:
                lines += ["", "实际产物：" + " · ".join(f"[{esc(a)}](../{a})" for a in t["artifacts"])]
            if t.get("review"):
                r = t["review"]
                lines += ["", f"验收：{esc(r['reviewer'])} / {r['role']} / {r['mode']}；[记录](../{r['source_file']})", "", esc(r["summary"])]
            lines += ["", "</details>"]
    lines += ["", "## 最近状态变更", "", "|修订|时间|任务|动作|执行者|说明|", "|---:|---|---|---|---|---|"]
    for h in data["history"][-20:]:
        lines.append(f"|{h['revision']}|{h['at']}|{h['task_id']}|{h['action']}|{esc(h['actor'])}|{esc(h['note'])}|")
    lines += ["", "完整变更历史保存在状态数据的 `history` 字段。", ""]
    return "\n".join(lines)


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".ledger-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", required=True, help="项目根目录，台账必须已存在")
    p.add_argument("command", choices=["status", "show", "validate", "render", "start", "submit", "accept", "block", "reopen", "add", "edit"])
    p.add_argument("task_id", nargs="?")
    p.add_argument("--actor")
    p.add_argument("--expected-revision", type=int)
    p.add_argument("--note", default="")
    p.add_argument("--artifact", action="append", default=[])
    p.add_argument("--review", help="项目相对路径的验收记录 JSON")
    p.add_argument("--task-file", help="项目相对路径的新增/修订任务 JSON")
    a = p.parse_args()
    root = Path(a.root).expanduser().resolve()
    ledger_path = root / "management/project-ledger.json"
    view_path = root / "docs/PROJECT_LEDGER.md"
    require(ledger_path.is_file(), "项目没有台账；不要在错误目录自动初始化")
    lock_path = root / "management/.ledger.lock"
    mutation = a.command not in {"status", "show", "validate", "render"}
    lock_fd = None
    try:
        if mutation or a.command == "render":
            try:
                lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            except FileExistsError:
                raise ValueError("台账正在更新或上次进程中断。检查锁文件中的 PID；不得直接覆盖并发写入。")
            os.write(lock_fd, str(os.getpid()).encode())
        data = load(ledger_path)
        index = validate(root, data, verify_evidence=(a.command != "reopen"))
        if a.command == "validate":
            require(view_path.is_file() and view_path.read_text(encoding="utf-8") == render(data), "Markdown 视图过期；运行 render 重建")
            print("PASS: schema, DAG, evidence hashes, history, phase gates, view")
            return
        if a.command == "render":
            atomic_write(view_path, render(data))
            print("已重建 docs/PROJECT_LEDGER.md")
            return
        if a.command == "status":
            print(json.dumps({"revision": data["revision"], "stages": [{"id": s["id"], "name": s["name"], "status": phase_status(s, [t for t in data["tasks"] if t["stage_id"] == s["id"]])} for s in data["stages"]],
                              "active": [t["id"] for t in data["tasks"] if t["status"] in {"in_progress", "in_review", "blocked"}],
                              "ready": [t["id"] for t in data["tasks"] if t["status"] in {"pending", "needs_rework"} and all(index[d]["status"] == "accepted" for d in t["dependencies"])]}, ensure_ascii=False, indent=2))
            return
        require(a.task_id, "需要任务 ID")
        if a.command == "show":
            require(a.task_id in index, "未知任务")
            print(json.dumps({"revision": data["revision"], "task": index[a.task_id]}, ensure_ascii=False, indent=2))
            return
        require(a.actor and a.actor.strip(), "状态更新需要实际执行者 --actor")
        require(a.expected_revision == data["revision"], f"修订号冲突；重新读取台账（当前 {data['revision']}）后再操作")
        before = copy.deepcopy(data["tasks"])
        if a.command == "add":
            require(a.task_id not in index, "任务 ID 已存在")
            task = load(artifact(root, a.task_file))
            require(task["id"] == a.task_id and task["status"] == "pending", "新任务必须 ID 匹配且 pending")
            require(not task.get("review") and not task.get("artifacts"), "新任务不能伪造验收或产物")
            data["tasks"].append(task)
            stage = next((s for s in data["stages"] if s["id"] == task["stage_id"]), None)
            require(stage is not None, "新增任务引用未知阶段")
            if stage.get("gate_task_id"):
                gate = index[stage["gate_task_id"]]
                require(gate["status"] in {"pending", "needs_rework"}, "新增阶段任务前先重开阶段门")
                gate["dependencies"].append(task["id"])
        else:
            require(a.task_id in index, "未知任务")
            task = index[a.task_id]
            status = task["status"]
            if a.command == "start":
                require(status in {"pending", "needs_rework", "blocked"}, "任务不可重复开工；已在开发中应继续当前任务")
                task.update(status="in_progress", assignee=a.actor, blocker=None)
            elif a.command == "submit":
                require(status == "in_progress", "只有开发中任务可提交验收")
                require(a.artifact, "提交验收需要 --artifact 文件")
                for f in a.artifact:
                    artifact(root, f)
                task.update(status="in_review", artifacts=list(dict.fromkeys(a.artifact)))
            elif a.command == "accept":
                require(status == "in_review", "只有待验收任务可以接受")
                review_path = artifact(root, a.review)
                review = load(review_path)
                review_check(root, task, review)
                for c in review["checks"]:
                    c["sha256"] = digest(artifact(root, c["evidence"]))
                review.update(source_file=a.review, source_sha256=digest(review_path), accepted_at=now())
                task.update(status="accepted", review=review, blocker=None)
            elif a.command == "block":
                require(status in {"in_progress", "in_review", "needs_rework"}, "只有已启动任务可登记阻塞")
                require(a.note.strip(), "阻塞必须说明缺少什么及解除条件")
                task.update(status="blocked", blocker=a.note)
            elif a.command == "reopen":
                require(status != "pending" and a.note.strip(), "重开需要已启动任务与原因")
                affected = {a.task_id}
                while True:
                    more = {t["id"] for t in data["tasks"] if affected.intersection(t["dependencies"])}
                    if more <= affected:
                        break
                    affected |= more
                for t in data["tasks"]:
                    if t["id"] in affected and t["status"] != "pending":
                        t.update(status="needs_rework", review=None, blocker=None, updated_at=now())
            elif a.command == "edit":
                require(status in {"pending", "needs_rework"} and a.note.strip(), "修订条件/依赖前先重开，并说明范围依据")
                patch = load(artifact(root, a.task_file))
                allowed = {"title", "owner", "dependencies", "acceptance", "deliverables", "source"}
                require(set(patch) <= allowed, "不可通过 edit 改状态、ID 或验收证据")
                task.update(patch)
        task["updated_at"] = now()
        data["revision"] += 1
        data["updated_at"] = now()
        old = {t["id"]: t for t in before}
        changes = [{"id": t["id"], "before": old.get(t["id"]), "after": copy.deepcopy(t)} for t in data["tasks"] if old.get(t["id"]) != t]
        data["history"].append({"revision": data["revision"], "at": data["updated_at"], "task_id": a.task_id,
                                "action": a.command, "actor": a.actor, "note": a.note, "changes": changes})
        validate(root, data)
        atomic_write(ledger_path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        atomic_write(view_path, render(data))
        print(json.dumps({"revision": data["revision"], "task": task["id"], "status": task["status"], "affected": [c["id"] for c in changes]}, ensure_ascii=False))
    finally:
        if lock_fd is not None:
            os.close(lock_fd)
            lock_path.unlink()


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        sys.exit(1)
