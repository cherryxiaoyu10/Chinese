---
name: game-project-ledger
description: 读取并维护游戏项目阶段、任务依赖、负责人、验收标准和证据台账。适用于使用游戏 Studio 开发项目时，在开发前登记任务、在验收后更新状态，并生成可审阅的项目进度视图。
metadata:
  short-description: 游戏项目阶段与验收台账
---

# 游戏项目台账

本 Skill 让项目台账成为开发协作的状态来源。它不替项目负责人做产品决策，也不把“有文件”自动判定为“已验收”。

## 适用项目

当当前项目包含 `management/project-ledger.json` 时使用。若项目没有台账，应先说明缺少台账；只有用户明确要求建立台账时，才初始化它。不要在错误目录自动创建或覆盖台账。

## 与游戏 Studio 的联动

`chinese-literature-card-game-studio` 每次开发任务必须按以下顺序调用本 Skill：

1. 读取 `management/project-ledger.json`，运行 `status` 和 `validate`。
2. 根据任务目标匹配一个或多个现有任务 ID；没有合适任务时，先由对应分类负责人提交新增任务定义。
3. 检查所有前置任务是否为 `accepted`；满足后将任务标为 `in_progress`，记录实际执行者。
4. 开发过程中只修改任务涉及的产物，并在任务完成后提交 `in_review`，登记项目相对路径的产物文件。
5. 由分类负责人收口，按每一条验收标准准备通过/不通过证据，写入独立的验收记录 JSON；只有证据文件存在且内容可复核时才执行 `accept`。
6. 验收完成后立即重新运行 `validate`，检查 JSON、依赖图、阶段门、验收证据哈希和 Markdown 视图。
7. 将台账 JSON、生成的 `docs/PROJECT_LEDGER.md`、产物和验收记录一起提交版本库，并在任务汇报中给出任务 ID、修订号、验收者和证据路径。

如果验收失败，使用 `block`（外部依赖或等待决策）或 `reopen`（需求/实现需要返工）；不要把失败任务改成 `accepted`。`reopen` 会把所有依赖它的已启动任务标为 `needs_rework`，防止下游继续使用失效产物。

## 状态与收口规则

- `pending`：未开始；`in_progress`：开发中；`in_review`：等待验收；`accepted`：证据逐条通过；`blocked`：有明确阻塞原因；`needs_rework`：验收不通过或上游重开。
- 前置任务必须全部 `accepted` 才能开始或提交验收。
- 阶段门任务的负责人必须是 `producer-director`；阶段门依赖该阶段所有任务，全部任务通过后才可提交阶段验收。
- 验收记录必须包含实际验收者、Studio 角色、验收方式、逐条检查、证据路径、结论和摘要。证据路径必须是项目内相对路径。
- 自动检查只能证明结构、可复现规则和文件证据；玩法乐趣、教学准确性和视觉可读性仍需要相应负责人或制作人的人工判断。
- `revision` 是乐观并发版本号。每次修改必须带读取到的 `--expected-revision`，冲突时重新读取台账，不覆盖他人的更新。

## CLI

脚本位于 `scripts/ledger.py`，只使用 Python 3 标准库。所有命令显式传入项目根目录：

```bash
python3 skills/game-project-ledger/scripts/ledger.py --root . status
python3 skills/game-project-ledger/scripts/ledger.py --root . validate
python3 skills/game-project-ledger/scripts/ledger.py --root . show P1-01
python3 skills/game-project-ledger/scripts/ledger.py --root . start P1-01 --actor gameplay-engineer --expected-revision 0
python3 skills/game-project-ledger/scripts/ledger.py --root . submit P1-01 --actor gameplay-engineer --expected-revision 1 --artifact game/README.md
python3 skills/game-project-ledger/scripts/ledger.py --root . accept P1-01 --actor gameplay-lead --expected-revision 2 --review qa/acceptance/P1-01.json
python3 skills/game-project-ledger/scripts/ledger.py --root . block P1-01 --actor gameplay-engineer --expected-revision 3 --note '等待 Godot 导出模板；解除条件：模板可用'
python3 skills/game-project-ledger/scripts/ledger.py --root . reopen P1-01 --actor gameplay-lead --expected-revision 4 --note '试玩发现验收标准需要返工'
python3 skills/game-project-ledger/scripts/ledger.py --root . render
```

`accept` 前需要先把独立的验收记录 JSON 放入项目目录。验收记录的格式和字段说明见 [references/ledger-schema.md](references/ledger-schema.md)。

## 台账文件

- `management/project-ledger.json`：唯一可编辑的状态、依赖、任务、产物、验收记录和完整变更历史。
- `docs/PROJECT_LEDGER.md`：由 JSON 生成的人类可读视图，不手工修改。
- `qa/acceptance/`：验收证据和验收记录，文件名应包含任务 ID；已被验收记录引用的证据不可覆盖，修改后必须产生新文件并重新验收。

## 汇报格式

任务完成后报告：

```text
任务 ID / 阶段：
状态与台账修订号：
实际产物：
验收者与方式：
逐条证据：
阻塞或遗留：
下一可开始任务：
```
