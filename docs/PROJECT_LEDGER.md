# 《文脉尖塔》项目台账

> 由台账工具生成，请通过配套 Skill 更新；JSON 为唯一状态来源。

- 修订号：15；更新时间：2026-09-09T11:07:22+00:00
- 开发与阶段门任务已验收：0/66（等权任务计数，不是工时完成率）
- 基础文档交付单独统计，不代表 MVP、Demo 或产品验收通过。
- [状态数据](../management/project-ledger.json) · [周期计划](PROJECT_PLAN.md) · [台账 Skill](../skills/game-project-ledger/SKILL.md)

## 阶段总览

|阶段|计划窗口|状态|已验收/任务总数|收口人|
|---|---|---|---:|---|
|BASE 基础准备与既有产物档案|已交付准备工作（待核验）|已交付|5/5|producer-director|
|P0 立项与范围冻结|第1周（计划）|未开始|0/8|producer-director|
|P1 技术预研 / 垂直原型|第1–2周（计划）|未开始|0/8|tech-quality-lead|
|P2 MVP|第3–5周（计划）|未开始|0/7|gameplay-lead|
|P3 增量期|第6–7周（计划）|未开始|0/7|producer-director|
|P4 Demo制作与内容冻结|第8周（计划）|未开始|0/6|producer-director|
|P5 集成冻结|第9周前半（计划）|未开始|0/5|tech-quality-lead|
|P6 优化期|第9–10周（计划）|未开始|0/6|tech-quality-lead|
|P7 验收器建设与验收|第11周（计划）|未开始|0/12|tech-quality-lead|
|P8 发布与复盘|第12周（计划）|未开始|0/7|producer-director|

## 当前任务与可开始项

- 当前没有进行中、待验收或阻塞任务。

满足前置依赖的任务（不代表已开工）：

- P0-01：锁定Slice A范围与规模
- P0-02：统一战斗时序、抽牌语义与首版状态规则
- P0-03：确定首批语文知识范围与题目审核模板
- P0-04：冻结像素窗口与占位资源规格
- P0-05：建立任务板、依赖清单、风险清单与Git约定
- P0-06：对齐验收阈值与固定种子口径
- P0-07：前移验收器与风险验证计划

## BASE 基础准备与既有产物档案

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|BASE-01|Studio与可调用Skill文档交付|已验收|producer-director|无|
|BASE-02|PRD与TDD草案交付|已验收|producer-director|无|
|BASE-03|Git远程基线交付|已验收|tech-quality-lead|BASE-01, BASE-02|
|BASE-04|项目周期计划草案交付|已验收|producer-director|BASE-02, BASE-03|
|BASE-05|项目台账与Skill联动交付|已验收|tech-quality-lead|BASE-04|

<details>
<summary>BASE-01 验收标准与证据</summary>

来源：项目既有产物核验

预期交付：Studio章程与可调用Skill文档

1. Studio章程文件存在且包含分类负责人、收口规则和工作流程。
2. 全局Skill目录存在可调用的 chinese-literature-card-game-studio/SKILL.md。

实际产物：[qa/evidence/BASE-01.md](../qa/evidence/BASE-01.md) · [AGENT.md](../AGENT.md) · [skills/chinese-literature-card-game-studio/SKILL.md](../skills/chinese-literature-card-game-studio/SKILL.md)

验收：project-agent / producer-director / self_check；[记录](../qa/acceptance/BASE-01.json)

基线交付已按登记标准逐条核验；不代表游戏功能阶段完成。

</details>

<details>
<summary>BASE-02 验收标准与证据</summary>

来源：项目既有产物核验

预期交付：PRD、TDD草案

1. docs/PRD.md和docs/TDD.md均存在且版本状态为Draft。
2. PRD目标、Slice A范围与TDD架构和测试策略可相互引用。

实际产物：[qa/evidence/BASE-02.md](../qa/evidence/BASE-02.md) · [docs/PRD.md](../docs/PRD.md) · [docs/TDD.md](../docs/TDD.md)

验收：project-agent / producer-director / self_check；[记录](../qa/acceptance/BASE-02.json)

基线交付已按登记标准逐条核验；不代表游戏功能阶段完成。

</details>

<details>
<summary>BASE-03 验收标准与证据</summary>

来源：项目既有产物核验

预期交付：Git仓库、远程main基线

1. 本地仓库存在main分支及首个项目提交。
2. origin远程指向用户指定的Chinese仓库且提交可追溯。

实际产物：[qa/evidence/BASE-03.md](../qa/evidence/BASE-03.md)

验收：project-agent / producer-director / self_check；[记录](../qa/acceptance/BASE-03.json)

基线交付已按登记标准逐条核验；不代表游戏功能阶段完成。

</details>

<details>
<summary>BASE-04 验收标准与证据</summary>

来源：项目既有产物核验

预期交付：项目周期计划草案

1. docs/PROJECT_PLAN.md覆盖MVP、增量期、Demo、优化期、验收器及补充阶段。
2. 计划任务、阶段门和技术依赖可被拆入项目台账。

实际产物：[qa/evidence/BASE-04.md](../qa/evidence/BASE-04.md) · [docs/PROJECT_PLAN.md](../docs/PROJECT_PLAN.md)

验收：project-agent / producer-director / self_check；[记录](../qa/acceptance/BASE-04.json)

基线交付已按登记标准逐条核验；不代表游戏功能阶段完成。

</details>

<details>
<summary>BASE-05 验收标准与证据</summary>

来源：项目既有产物核验

预期交付：项目台账、台账Skill及联动工具

1. 台账覆盖9阶段和PROJECT_PLAN中的所有计划任务。
2. Studio与配套Skill已联动且全局和项目副本一致。
3. 台账工具正常/异常路径测试通过且视图一致。

实际产物：[qa/evidence/BASE-05.md](../qa/evidence/BASE-05.md) · [qa/evidence/BASE-05-tool-tests.txt](../qa/evidence/BASE-05-tool-tests.txt) · [management/project-ledger.json](../management/project-ledger.json) · [docs/PROJECT_LEDGER.md](../docs/PROJECT_LEDGER.md)

验收：project-agent / producer-director / self_check；[记录](../qa/acceptance/BASE-05.json)

基线交付已按登记标准逐条核验；不代表游戏功能阶段完成。

</details>

## P0 立项与范围冻结

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P0-01|锁定Slice A范围与规模|未开始|producer-director|BASE-04|
|P0-02|统一战斗时序、抽牌语义与首版状态规则|未开始|gameplay-lead|BASE-04|
|P0-03|确定首批语文知识范围与题目审核模板|未开始|content-lead|BASE-04|
|P0-04|冻结像素窗口与占位资源规格|未开始|art-audio-lead|BASE-04|
|P0-05|建立任务板、依赖清单、风险清单与Git约定|未开始|tech-quality-lead|BASE-04|
|P0-06|对齐验收阈值与固定种子口径|未开始|producer-director|BASE-04|
|P0-07|前移验收器与风险验证计划|未开始|tech-quality-lead|BASE-04|
|P0-GATE|P0阶段门：负责人收口与制作人验收|未开始|producer-director|P0-01, P0-02, P0-03, P0-04, P0-05, P0-06, P0-07|

<details>
<summary>P0-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：Slice A范围说明

1. 形成8–10层、2普通敌人、1精英、1首领、12–16张卡、3–4件遗物、2–3事件、2类知识的范围记录。
2. 范围记录标明非目标内容不进入本版本。

</details>

<details>
<summary>P0-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：战斗规则收口记录

1. 明确抽牌/弃牌/回合结束顺序及知识检定插入点。
2. 明确意图生成与展示时序、状态结算顺序和三种首版状态规则。
3. PRD与TDD对“双重抽牌”等歧义形成一份已收口规则记录。

</details>

<details>
<summary>P0-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：首批知识范围、题目审核模板

1. 确定首批两类知识及每类的年级、难度、来源字段。
2. 审核模板要求题目具备唯一答案、解析、来源和审核状态。

</details>

<details>
<summary>P0-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：视觉规格表、可读性样例

1. 记录640×360逻辑画布、Nearest过滤、像素尺寸、色板、字体与占位资源规格。
2. 提供目标分辨率下文字可读性检查样例并记录不通过条件。

</details>

<details>
<summary>P0-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：任务板、依赖清单、风险清单、Git约定

1. 台账中每项计划任务都有唯一ID、负责人、依赖与验收标准。
2. 记录目录结构、分支和提交约定及阻断风险清单。

</details>

<details>
<summary>P0-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0；docs/PRD.md §13；docs/TDD.md §12

预期交付：验收阈值与固定种子口径记录

1. 明确7/10到达首领与6/10击败首领的关系、适用阶段和报告格式。
2. 明确PRD的20局流派测试与TDD的10种子测试不互相替代。
3. 形成制作人可审阅的验收阈值决策记录，未收口前禁止进入MVP开发。

</details>

<details>
<summary>P0-07 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0、阶段7；docs/TDD.md §12

预期交付：验收器前移计划、风险验证矩阵

1. 为内容、规则、固定种子、存档、无头启动和640像素可读性分别定义最早可执行验证点。
2. 记录“验收器过迟建设”风险及其在P1/P2的验证入口。
3. 计划明确未通过项阻止对应开发阶段门。

</details>

<details>
<summary>P0-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段0

预期交付：P0阶段决策包、验收证据和阶段结论

1. P0-01至P0-07均有负责人收口记录。
2. PRD/TDD规则与验收阈值冲突已形成决策记录，未决核心规则不得进入P1。

</details>

## P1 技术预研 / 垂直原型

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P1-01|固定Godot 4.4.x patch版本与导出模板|未开始|tech-quality-lead|P0-GATE|
|P1-02|建立Godot工程、Autoload、目录与InputMap|未开始|tech-quality-lead|P0-GATE, P1-01|
|P1-03|实现ContentRepository与三类最小数据加载|未开始|tech-quality-lead|P0-GATE, P1-02|
|P1-04|实现TurnStateMachine与基础战斗回合|未开始|gameplay-lead|P0-GATE, P1-03|
|P1-05|实现异步知识检定暂停与结果结算|未开始|content-lead|P0-GATE, P1-04, P0-02, P0-03|
|P1-06|建立最小战斗UI、调试日志与固定种子|未开始|tech-quality-lead|P0-GATE, P1-04, P0-04, P0-06|
|P1-07|建立预研阶段烟雾验收入口|未开始|tech-quality-lead|P0-GATE, P1-06, P0-07|
|P1-GATE|P1阶段门：负责人收口与制作人验收|未开始|tech-quality-lead|P1-01, P1-02, P1-03, P1-04, P1-05, P1-06, P1-07, P0-GATE|

<details>
<summary>P1-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：引擎版本记录、导出模板记录

1. project.godot记录具体Godot patch版本和导出模板版本。
2. 无编辑器启动检查能识别版本不匹配。

</details>

<details>
<summary>P1-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：可启动Godot工程骨架

1. project.godot、Autoload、TDD目录结构和InputMap action可加载。
2. 640×360 viewport和目标缩放配置可在启动时读取。

</details>

<details>
<summary>P1-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：ContentRepository、最小数据集

1. 可加载1张卡、1个敌人、3道题和3个效果命令。
2. 内容校验失败能报告文件、字段和错误等级。

</details>

<details>
<summary>P1-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：TurnStateMachine、CombatState原型

1. 抽牌、3费用、出牌、结束回合、敌人意图和胜负可完整运行。
2. 非法状态转换被拒绝并写入日志。

</details>

<details>
<summary>P1-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：QuestionContext、QuestionService、答题弹窗原型

1. 答对、答错、超时各只结算一次并恢复玩家回合。
2. 本场最多2次检定额度可验证，重复answered/timed_out信号被忽略。

</details>

<details>
<summary>P1-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：最小战斗UI、战斗日志、固定种子入口

1. 战斗关键状态和敌人意图在UI可见，日志含抽牌和意图结果。
2. 同一种子与相同输入产生相同抽牌和意图。

</details>

<details>
<summary>P1-07 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1；docs/TDD.md §12

预期交付：预研烟雾测试、首份战斗日志

1. 无头启动可进入战斗并完成一场胜负。
2. 题目弹窗不会卡死回合；固定种子结果可重复。

</details>

<details>
<summary>P1-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段1

预期交付：P1阶段决策包、验收证据和阶段结论

1. 可启动工程从启动到胜负完整运行。
2. 固定种子和异步答题暂停的烟雾验收通过。

</details>

## P2 MVP

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P2-01|实现卡牌基础效果、状态、升级与消耗堆|未开始|gameplay-lead|P1-GATE, P1-06, P0-02|
|P2-02|实现奖励三选一、跳过与金币恢复奖励|未开始|gameplay-lead|P1-GATE, P2-01|
|P2-03|实现普通敌人、精英、首领与意图策略|未开始|gameplay-lead|P1-GATE, P1-06, P0-02|
|P2-04|实现8–10层地图与节点路由|未开始|gameplay-lead|P1-GATE, P1-06|
|P2-05|实现Slice A卡牌、遗物、事件与两类题库|未开始|content-lead|P1-GATE, P2-01, P2-03, P2-04, P0-03|
|P2-06|实现RunState、节点存档、失败复盘与错题展示|未开始|tech-quality-lead|P1-GATE, P2-04, P2-05|
|P2-GATE|P2阶段门：负责人收口与制作人验收|未开始|gameplay-lead|P2-01, P2-02, P2-03, P2-04, P2-05, P2-06, P1-GATE|

<details>
<summary>P2-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：卡牌效果与状态系统

1. 攻击、防御、技能、能力和问答卡类别至少各有一条可执行路径。
2. 升级、消耗堆及状态效果有规则测试证据。

</details>

<details>
<summary>P2-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：奖励流程、奖励数据

1. 胜利后生成3张不同奖励候选并支持选择或跳过。
2. 奖励快照由固定种子复现。

</details>

<details>
<summary>P2-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：敌人和首领数据、意图策略

1. 2个普通敌人、1个精英、1个首领可战斗并显示意图。
2. 首领至少有可读的阶段变化与策略。

</details>

<details>
<summary>P2-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：Slice A地图生成与路线

1. 地图可生成普通战斗、精英、事件、商店、休息、未知和首领节点。
2. 路线连通且首领前节点满足规则，运行种子可重建。

</details>

<details>
<summary>P2-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：Slice A内容数据包

1. 交付12–16张卡、3–4件遗物、2–3个事件和2类已审核题目。
2. 所有内容通过Schema、引用、审核状态和文本长度校验。

</details>

<details>
<summary>P2-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：RunState、SaveService Slice A、Review页面

1. 节点结算、战斗结束、事件选择和商店离开可恢复存档。
2. 失败结算展示错题、解析和复习标签。

</details>

<details>
<summary>P2-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段2

预期交付：P2阶段决策包、验收证据和阶段结论

1. 玩家能完成Slice A路线并获得奖励、存档和复盘。
2. 固定种子门槛按P0-06收口口径执行且无阻断级流程缺陷。

</details>

## P3 增量期

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P3-01|增加第三类知识类型与新卡牌流派|未开始|content-lead|P2-GATE, P2-05|
|P3-02|增加4–6张卡牌|未开始|gameplay-lead|P2-GATE, P2-05, P3-01|
|P3-03|增加2–3件遗物、2个事件与1种敌人行为|未开始|gameplay-lead|P2-GATE, P2-03, P2-04|
|P3-04|补齐题库去重、审核状态与错误提示|未开始|content-lead|P2-GATE, P2-05|
|P3-05|依据日志调整数值与首领阶段|未开始|gameplay-lead|P2-GATE, P2-02, P2-03, P2-06|
|P3-06|制作基础像素资源与战斗反馈音效|未开始|art-audio-lead|P2-GATE, P0-04, P2-01|
|P3-GATE|P3阶段门：负责人收口与制作人验收|未开始|producer-director|P3-01, P3-02, P3-03, P3-04, P3-05, P3-06, P2-GATE|

<details>
<summary>P3-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：第三知识类型、新流派卡牌

1. 第三类知识题可从数据加载并进入战斗或事件决策。
2. 新增流派至少有一条可验证的构筑收益。

</details>

<details>
<summary>P3-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：增量卡牌数据

1. 4–6张新增卡牌能被奖励、商店或事件引用。
2. 每张卡有基础、升级、知识标签和审核状态。

</details>

<details>
<summary>P3-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：增量遗物、事件、敌人行为

1. 新增遗物、事件和敌人行为可在一局中触发。
2. 每项新增内容至少改变一种卡牌或路线决策。

</details>

<details>
<summary>P3-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：题库去重报告、审核校验

1. 重复题目能被识别并报告。
2. 未审核或引用无效内容在发布校验中被阻断且提示可定位。

</details>

<details>
<summary>P3-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：平衡变更记录、参数版本

1. 费用、伤害、奖励概率和首领阶段变更都有前后数据记录。
2. 固定种子测试结果和变更理由可追溯。

</details>

<details>
<summary>P3-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：基础像素资源包、反馈音效

1. 主角、敌人、卡牌图标和反馈音效可在战斗路径中加载。
2. 资源通过原创性与规格检查。

</details>

<details>
<summary>P3-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段3

预期交付：P3阶段决策包、验收证据和阶段结论

1. 新增内容可运行且旧存档与旧卡牌不被破坏。
2. 每项新增系统有可验证玩法收益和内容审核证据。

</details>

## P4 Demo制作与内容冻结

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P4-01|打通15–25分钟Demo展示路径|未开始|producer-director|P3-GATE, P2-06, P3-05|
|P4-02|替换关键占位资源|未开始|art-audio-lead|P3-GATE, P3-06, P4-01|
|P4-03|完成标题、设置、音量、字体与无障碍提示|未开始|art-audio-lead|P3-GATE, P2-06, P0-04|
|P4-04|锁定Demo内容并登记新增需求|未开始|producer-director|P3-GATE, P4-01, P4-02, P4-03|
|P4-05|录制演示视频与已知问题说明|未开始|producer-director|P3-GATE, P4-04|
|P4-GATE|P4阶段门：负责人收口与制作人验收|未开始|producer-director|P4-01, P4-02, P4-03, P4-04, P4-05, P3-GATE|

<details>
<summary>P4-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：Demo体验路径构建

1. 从启动、教学、地图、战斗、奖励、首领到复盘可连续完成。
2. 新玩家不依赖开发者口头解释即可完成首场战斗。

</details>

<details>
<summary>P4-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：Demo关键视觉资源

1. 主角、首领、核心敌人、地图背景、卡牌边框和主要特效已接入。
2. 关键资源保持原创性并符合像素规格。

</details>

<details>
<summary>P4-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：Demo菜单与可访问性设置

1. 标题页、设置页、音量控制和字体大小可用。
2. 倒计时、错误提示和无障碍选项在目标分辨率无截断。

</details>

<details>
<summary>P4-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：内容冻结清单、下一版本清单

1. Demo内容清单有版本号和冻结时间。
2. 冻结后的新需求均进入下一版本清单而不改写本版本范围。

</details>

<details>
<summary>P4-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：Demo视频、版本说明草稿

1. 提供3–5分钟演示视频。
2. 已知问题说明包含严重度、复现步骤和影响范围。

</details>

<details>
<summary>P4-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段4

预期交付：P4阶段决策包、验收证据和阶段结论

1. 15–25分钟Demo路径可重复完成。
2. 关键UI无截断遮挡且内容冻结清单生效。

</details>

## P5 集成冻结

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P5-01|冻结数据Schema、事件名、存档格式与输入action|未开始|tech-quality-lead|P4-GATE, P4-04, P2-06|
|P5-02|建立阻断级问题修复规则|未开始|tech-quality-lead|P4-GATE, P5-01|
|P5-03|生成内容、资源、构建号与Git tag候选清单|未开始|tech-quality-lead|P4-GATE, P5-01, P5-02|
|P5-04|产出独立Release Candidate并保留回归板|未开始|tech-quality-lead|P4-GATE, P5-03|
|P5-GATE|P5阶段门：负责人收口与制作人验收|未开始|tech-quality-lead|P5-01, P5-02, P5-03, P5-04, P4-GATE|

<details>
<summary>P5-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段5

预期交付：集成冻结接口清单

1. 冻结清单包含Schema、事件名、存档格式和InputMap action版本。
2. 候选构建中接口变更会被拒绝或记录为阻断问题。

</details>

<details>
<summary>P5-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段5

预期交付：冻结期修复规则、例外记录

1. 冻结期只允许崩溃、数据错误、阻断流程和明显可读性修复。
2. 每次例外修改有任务ID和回归证据。

</details>

<details>
<summary>P5-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段5

预期交付：候选构建元数据清单

1. 内容清单、资源清单、构建号和tag候选互相可追溯。
2. 候选构建关联commit、随机种子和测试报告。

</details>

<details>
<summary>P5-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段5

预期交付：Release Candidate、回归任务板

1. 无编辑器环境可启动候选构建。
2. 候选构建放入独立目录并保留对应回归任务板。

</details>

<details>
<summary>P5-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段5

预期交付：P5阶段决策包、验收证据和阶段结论

1. 唯一候选构建、接口冻结清单和可追溯元数据齐备。
2. 无编辑器环境可启动且冻结期规则生效。

</details>

## P6 优化期

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P6-01|测量战斗帧时间、切换、内存与加载|未开始|tech-quality-lead|P5-GATE, P5-04|
|P6-02|优化卡牌、题目与意图输入反馈|未开始|art-audio-lead|P5-GATE, P5-04, P6-01|
|P6-03|修复存档恢复、缩放、字体与焦点导航|未开始|tech-quality-lead|P5-GATE, P5-04, P0-04|
|P6-04|优化固定种子首领难度与奖励分布|未开始|gameplay-lead|P5-GATE, P0-06, P3-05, P6-01|
|P6-05|扫描慢加载、重复题目与无效引用|未开始|content-lead|P5-GATE, P3-04, P6-01|
|P6-GATE|P6阶段门：负责人收口与制作人验收|未开始|tech-quality-lead|P6-01, P6-02, P6-03, P6-04, P6-05, P5-GATE|

<details>
<summary>P6-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：性能基线报告

1. 记录战斗常态帧时间、场景切换、内存和加载基线。
2. 指标报告标明采样环境与构建号。

</details>

<details>
<summary>P6-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：输入反馈优化构建

1. 卡牌悬停、拖拽、题目弹窗和意图动画反馈可响应。
2. 优化后不改变规则结算结果。

</details>

<details>
<summary>P6-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：稳定性与可读性修复

1. 存档恢复、窗口缩放、字体溢出和焦点导航均有回归记录。
2. 关键UI不出现截断、遮挡或仅靠颜色传达状态。

</details>

<details>
<summary>P6-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：难度与奖励优化记录

1. 参数调整有固定种子前后对比。
2. 调整未突破已收口的阶段验收阈值。

</details>

<details>
<summary>P6-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：全量扫描报告

1. 全量扫描能输出慢加载资源、重复题目和无效引用清单。
2. 阻断项在进入验收器前归零或有明确复现任务。

</details>

<details>
<summary>P6-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段6

预期交付：P6阶段决策包、验收证据和阶段结论

1. 性能、可读性、存档和固定种子优化有前后指标。
2. 目标帧率与场景切换指标达到TDD要求或记录经接受的例外。

</details>

## P7 验收器建设与验收

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P7-01|实现内容Schema与引用验收器|未开始|tech-quality-lead|P6-GATE, P3-04, P6-05|
|P7-02|实现战斗规则自动测试器|未开始|tech-quality-lead|P6-GATE, P2-01, P2-02, P2-04|
|P7-03|实现知识检定与无障碍自动测试|未开始|content-lead|P6-GATE, P1-05, P4-03|
|P7-04|实现固定种子跑局模拟器|未开始|tech-quality-lead|P6-GATE, P0-06, P2-04, P2-06|
|P7-05|实现存档、checksum与迁移验收|未开始|tech-quality-lead|P6-GATE, P2-06, P5-01|
|P7-06|实现无头启动与关键流程烟雾测试|未开始|tech-quality-lead|P6-GATE, P5-04|
|P7-07|实现640×360可读性与焦点导航检查|未开始|art-audio-lead|P6-GATE, P0-04, P6-03|
|P7-08|执行人工新玩家与教学体验验收|未开始|content-lead|P6-GATE, P4-01, P4-03|
|P7-09|执行路线、奖励与构筑可行性试玩|未开始|gameplay-lead|P6-GATE, P0-01, P3-05, P7-04|
|P7-10|执行原创性与内容准确性复核|未开始|content-lead|P6-GATE, P2-05, P4-02|
|P7-11|汇总验收报告并提交版本决策包|未开始|tech-quality-lead|P6-GATE, P7-01, P7-02, P7-03, P7-04, P7-05, P7-06, P7-07, P7-08, P7-09, P7-10, P0-06|
|P7-GATE|P7阶段门：负责人收口与制作人验收|未开始|tech-quality-lead|P7-01, P7-02, P7-03, P7-04, P7-05, P7-06, P7-07, P7-08, P7-09, P7-10, P7-11, P6-GATE|

<details>
<summary>P7-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：tools/validate_content.gd及报告

1. 校验Schema、引用、审核状态、文本长度和题目唯一答案。
2. 错误报告包含文件、字段、等级和修复建议。

</details>

<details>
<summary>P7-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：tests/test_runner.gd及规则测试

1. 覆盖效果、状态、伤害、抽牌、费用、奖励和地图连通性。
2. godot --headless测试入口可返回失败状态。

</details>

<details>
<summary>P7-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：知识检定自动测试

1. 覆盖答对、答错、超时、取消倒计时和每场2次上限。
2. 重复答题信号不会产生重复结算。

</details>

<details>
<summary>P7-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：tools/simulate_runs.gd及模拟报告

1. 10个固定种子可批量运行并导出到达首领、击败首领、奖励和知识正确率。
2. 模拟结果含运行种子、构建号和阈值判定。

</details>

<details>
<summary>P7-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：存档验收测试与迁移夹具

1. 覆盖写入、读取、checksum、备份恢复和schema迁移。
2. 损坏存档被拒绝并可恢复上一份备份。

</details>

<details>
<summary>P7-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：构建启动检查与烟雾测试

1. 无头构建可从主菜单进入战斗、完成战斗并回到地图。
2. 发布构建在无编辑器环境启动失败时返回可定位错误。

</details>

<details>
<summary>P7-07 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：可读性与焦点验收报告

1. 目标分辨率下文字无截断、遮挡，地图节点、卡牌、题目选项和奖励按钮焦点可达。
2. 状态信息同时有文字或图标标签。

</details>

<details>
<summary>P7-08 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：人工试玩清单与记录

1. 试玩记录证明新玩家60秒内理解费用、抽牌、意图和结束回合。
2. 答题反馈包含错题解析且不会把战斗变成连续答题。

</details>

<details>
<summary>P7-09 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：平衡与构筑试玩报告

1. 试玩记录覆盖三类关键节点差异和奖励构筑意义。
2. 20局内部测试记录三种初始流派各至少一条可行路线。

</details>

<details>
<summary>P7-10 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：内容准确性与原创性复核表

1. 题目答案、解析、年级、来源字段完整且由内容负责人复核。
2. 角色剪影、卡牌版式、图标、字体、按钮、背景和特效通过原创性检查。

</details>

<details>
<summary>P7-11 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：统一验收报告、阻断缺陷表、版本决策包

1. 自动验收全绿、人工验收无阻断项，剩余问题均有记录和接受结论。
2. 报告明确是否达到已收口的7/10、6/10阈值。

</details>

<details>
<summary>P7-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段7

预期交付：P7阶段决策包、验收证据和阶段结论

1. 自动验收全绿且人工验收无阻断项。
2. 阈值、内容准确性、可读性、原创性与存档证据齐全。

</details>

## P8 发布与复盘

|编号|任务|状态|负责人|前置任务|
|---|---|---|---|---|
|P8-01|打包Windows与macOS Demo|未开始|tech-quality-lead|P7-GATE, P7-11|
|P8-02|创建版本tag并记录校验和|未开始|tech-quality-lead|P7-GATE, P8-01|
|P8-03|发布版本说明、已知问题与复现方式|未开始|producer-director|P7-GATE, P7-11, P8-01|
|P8-04|记录试玩反馈、错题标签、卡牌使用率与失败节点|未开始|content-lead|P7-GATE, P7-08, P7-09|
|P8-05|召开Studio复盘并记录取舍决策|未开始|producer-director|P7-GATE, P8-03, P8-04|
|P8-06|将下一版本需求回写PRD/TDD变更清单|未开始|producer-director|P7-GATE, P8-05|
|P8-GATE|P8阶段门：负责人收口与制作人验收|未开始|producer-director|P8-01, P8-02, P8-03, P8-04, P8-05, P8-06, P7-GATE|

<details>
<summary>P8-01 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：Windows/macOS发布包

1. Windows和macOS包可在无编辑器环境启动。
2. 包内版本号、构建号和内容校验结果可追溯。

</details>

<details>
<summary>P8-02 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：Git tag、发布包校验和

1. 创建v0.1.0-demo或v0.1.0-mvp之一并记录选择依据。
2. 发布包校验和与tag commit一致。

</details>

<details>
<summary>P8-03 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：版本说明、已知问题清单

1. 版本说明包含功能范围、已知问题、严重度和复现步骤。
2. 说明链接到对应验收报告和构建号。

</details>

<details>
<summary>P8-04 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：试玩反馈数据表

1. 反馈表记录玩家意见、错误题标签、卡牌使用率和失败节点。
2. 数据字段可关联运行种子或试玩局次。

</details>

<details>
<summary>P8-05 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：Studio复盘决策记录

1. 复盘明确保留、删除、延后的系统。
2. 每项决策有依据、负责人和后续版本归属。

</details>

<details>
<summary>P8-06 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：PRD/TDD下一版本变更清单

1. 下一版本需求形成带优先级和来源的变更清单。
2. 变更不以口头形式留在代码中，且可回溯到复盘决策。

</details>

<details>
<summary>P8-GATE 验收标准与证据</summary>

来源：docs/PROJECT_PLAN.md §4 阶段8

预期交付：P8阶段决策包、验收证据和阶段结论

1. 发布包可下载启动、完成Demo、查看复盘并恢复存档。
2. 下一版本范围与变更清单已记录。

</details>

## 最近状态变更

|修订|时间|任务|动作|执行者|说明|
|---:|---|---|---|---|---|
|1|2026-09-09T11:07:21+00:00|BASE-01|start|producer-director||
|2|2026-09-09T11:07:21+00:00|BASE-01|submit|producer-director||
|3|2026-09-09T11:07:22+00:00|BASE-01|accept|producer-director||
|4|2026-09-09T11:07:22+00:00|BASE-02|start|producer-director||
|5|2026-09-09T11:07:22+00:00|BASE-02|submit|producer-director||
|6|2026-09-09T11:07:22+00:00|BASE-02|accept|producer-director||
|7|2026-09-09T11:07:22+00:00|BASE-03|start|producer-director||
|8|2026-09-09T11:07:22+00:00|BASE-03|submit|producer-director||
|9|2026-09-09T11:07:22+00:00|BASE-03|accept|producer-director||
|10|2026-09-09T11:07:22+00:00|BASE-04|start|producer-director||
|11|2026-09-09T11:07:22+00:00|BASE-04|submit|producer-director||
|12|2026-09-09T11:07:22+00:00|BASE-04|accept|producer-director||
|13|2026-09-09T11:07:22+00:00|BASE-05|start|producer-director||
|14|2026-09-09T11:07:22+00:00|BASE-05|submit|producer-director||
|15|2026-09-09T11:07:22+00:00|BASE-05|accept|producer-director||

完整变更历史保存在状态数据的 `history` 字段。
