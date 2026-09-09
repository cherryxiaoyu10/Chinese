# 项目台账数据与验收记录格式

## 台账顶层

```json
{
  "schema_version": 1,
  "project_id": "chinese",
  "title": "文脉尖塔",
  "revision": 0,
  "updated_at": "2026-09-09T00:00:00Z",
  "source_documents": ["docs/PRD.md", "docs/TDD.md", "docs/PROJECT_PLAN.md"],
  "stages": [],
  "tasks": [],
  "history": []
}
```

每个任务必须包含 `id`、`title`、`stage_id`、`kind`、`owner`、`status`、`dependencies`、`source`、`acceptance`、`deliverables`、`artifacts`、`review`、`blocker`、`assignee` 和 `updated_at`。状态更新只由 `scripts/ledger.py` 完成，避免手工改 JSON 破坏依赖图或历史。

## 验收记录

验收记录应放在项目相对路径 `qa/acceptance/<TASK-ID>.json`，内容示例：

```json
{
  "task_id": "P1-01",
  "reviewer": "gameplay-lead",
  "role": "gameplay-lead",
  "mode": "peer_review",
  "result": "pass",
  "summary": "每条标准均有可复核证据。",
  "checks": [
    {"criterion": 1, "result": "pass", "evidence": "qa/evidence/P1-01-run.md", "detail": "固定种子运行结果可复现。"}
  ]
}
```

`accept` 会记录验收记录自身和每份证据的 SHA-256。若证据被覆盖，`validate` 会失败；应重新提交新的证据并走返工验收。`source_file`、`source_sha256`、`accepted_at` 由工具写入，不应由 Agent 预填。

## 状态含义

- `accepted` 是该任务的交付物符合已登记验收标准，不等于整个阶段或产品通过。
- 阶段门只有在阶段内所有任务 accepted 后，才可由 `producer-director` 验收。
- 用户要求的产品取舍、教学质量和体验判断必须在验收摘要中明确由人工负责，不能由文件存在性替代。
