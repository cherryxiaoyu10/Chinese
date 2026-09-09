# BASE-05 核验记录

核验项目：项目台账与配套 Skill 已接入并可操作。

- 台账覆盖 BASE、P0–P8 共 10 个阶段，覆盖 71 个任务。
- `skills/chinese-literature-card-game-studio/SKILL.md` 已要求开发前读取台账、验收后更新台账。
- 全局与项目副本的 Studio Skill、台账 Skill 内容一致。
- 台账工具的正常/异常行为测试通过：依赖阻断、修订号冲突、验收证据篡改检测、阶段门角色校验和视图一致性。
- `management/project-ledger.json` 通过 Schema、DAG、阶段门、历史和证据校验；`docs/PROJECT_LEDGER.md` 由工具生成。

核验方式：`python3 skills/game-project-ledger/scripts/test_ledger.py`、台账 `validate`、副本比对。

附加工具输出保存在 `qa/evidence/BASE-05-tool-tests.txt`。
