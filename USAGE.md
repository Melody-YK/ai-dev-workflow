# AI Dev Workflow 使用说明

这是一套轻量、可控、可替换的 AI 研发工作流，用来把一个 PRD 或原始需求，按阶段交给不同能力型 skill 处理，并通过固定 artifact 文件完成交接。

核心目标不是“自动化一切”，而是让每一步都有明确输入、输出、人工确认点和质量门禁。

AI Dev Workflow 定义稳定的阶段契约和 artifact 位置；`requirements-analyst`、真实外部 `garrytan/gstack`/review-pack fallback、`superpowers` 等 provider 是能力提供者，可以保留有价值的原生产物，但必须写入 workflow 指定的位置。

## 1. 工作流定位

默认编排三个能力：

```text
requirements-analyst → gstack-adapter/external gstack → prototype generation → superpowers
```

它们的分工是：

| 阶段 | 负责什么 | 默认能力 |
|---|---|---|
| 00 Intake | 收集原始需求、建立工作目录 | ai-dev-workflow |
| 01 Requirements | 把 PRD 转成明确、可验证的需求规格 | requirements-analyst |
| 02 Product & Engineering Review | 审范围、审架构、审安全/风险、审 QA 策略、定本轮交付范围 | gstack-adapter over real garrytan/gstack；review-pack 仅 degraded fallback |
| 03 Prototype | 生成需求驱动的静态 HTML/CSS 原型，验证页面、流程、角色和状态 | requirements-analyst prototype approach |
| 04 Implementation | 写实现计划、TDD/验证先行、小步执行、记录证据 | superpowers |
| 05 Verification & Review | 完成前验证、代码/架构 review、QA/风险复查、发布前确认 | superpowers + optional gstack-adapter over real garrytan/gstack |
| API Contract Gate | `requirements/api.yaml`、后端 route、前端 client 三方对账；含必填字段/枚举/request-response schema；有前端时按等级记录 browser smoke | workflow contract |

## 2. 目录结构

初始化后，每个需求会生成一个独立目录：

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── requirements/
│   ├── reverse.md              # optional
│   ├── discovery.md
│   ├── sort.md
│   ├── requirements.md
│   ├── datamodel.md
│   ├── clarification.md
│   ├── validation.md
│   ├── prd.md
│   ├── api.yaml                # API 边界存在时必需
│   ├── open-questions.md
│   └── traceability.md
├── 02_TECHNICAL_DESIGN.md
├── 03_PROTOTYPE.md
├── prototype/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── pages/
├── 04_IMPLEMENTATION.md
├── implementation/
│   └── IMPLEMENTATION_PLAN.md
├── 05_REVIEW.md
└── STATUS.md
```

这些文件就是阶段之间的交接接口。

不要只依赖聊天上下文。下一阶段必须读取上一阶段 artifact。

## 3. 初始化一个工作流

在任意项目中执行：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/init_workflow.py \
  --project-root "/path/to/project" \
  --source-prd "/path/to/project/PRD.md" \
  --feature "feature-name"
```

示例：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/init_workflow.py \
  --project-root "/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test" \
  --source-prd "/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test/PRD.md" \
  --feature "operation-ticket-management"
```

生成目录：

```text
/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test/.ai-workflow/operation-ticket-management/
```

## 4. 查看状态

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/status.py \
  "/path/to/project/.ai-workflow/<feature-slug>"
```

或直接打开：

```text
.ai-workflow/<feature-slug>/STATUS.md
```

`STATUS.md` 记录：

- 当前阶段
- 每个阶段状态
- 等待人工确认的点
- 已做决策
- 开放问题
- 下一步动作

## 5. 校验 artifact 是否完整

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  "/path/to/project/.ai-workflow/<feature-slug>"
```

正常输出类似：

```text
OK 00_INTAKE.md
OK 01_REQUIREMENTS.md
OK 02_TECHNICAL_DESIGN.md
OK 03_PROTOTYPE.md
OK 04_IMPLEMENTATION.md
OK 05_REVIEW.md
OK STATUS.md
```

## 6. 推荐运行方式

### Step 0：初始化

输入：

- 原始 PRD
- 项目目录
- feature 名称

输出：

```text
00_INTAKE.md
STATUS.md
```

完成后暂停，让人确认是否继续。

### Step 1：跑 Requirements

对 agent 说：

```text
继续跑 01 Requirements
```

要求 agent 读取：

```text
.ai-workflow/<feature-slug>/00_INTAKE.md
PRD.md
```

输出：

```text
.ai-workflow/<feature-slug>/01_REQUIREMENTS.md
.ai-workflow/<feature-slug>/requirements/discovery.md
.ai-workflow/<feature-slug>/requirements/sort.md
.ai-workflow/<feature-slug>/requirements/requirements.md
.ai-workflow/<feature-slug>/requirements/datamodel.md
.ai-workflow/<feature-slug>/requirements/clarification.md
.ai-workflow/<feature-slug>/requirements/validation.md
.ai-workflow/<feature-slug>/requirements/prd.md
.ai-workflow/<feature-slug>/requirements/open-questions.md
.ai-workflow/<feature-slug>/requirements/traceability.md
```

`01_REQUIREMENTS.md` 是阶段摘要、索引和门禁文件；详细需求文档保留在 `requirements/` 目录。使用 `requirements-analyst` 的分析方法和丰富产物，但不要让它替换 workflow 的产物位置和交接规则。

01 要求满血 requirements-analyst 深度，而不是“摘要够用”。完成前 agent 必须运行并记录：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  .ai-workflow/<feature-slug> --gate 01-full
```

如果失败，01 不能标记 clean DONE；应继续扩展 provider-native artifacts，或明确标记 `DONE_DEGRADED`。

这一阶段重点检查：

- discovery 是否收集到角色、目标、约束和成功标准
- sort 是否给出优先级和本轮范围取舍
- analysis 是否覆盖角色、流程、实体、状态和权限
- clarification 是否保留/解决歧义，而不是瞎猜
- validation 是否给出可测试验收标准
- specification 是否形成正式 PRD 和 traceability

### Step 2：跑 Product & Engineering Review

对 agent 说：

```text
继续跑 02 Product & Engineering Review
```

要求 agent 读取：

```text
01_REQUIREMENTS.md
requirements/discovery.md
requirements/sort.md
requirements/requirements.md
requirements/datamodel.md
requirements/clarification.md
requirements/validation.md
requirements/prd.md
requirements/open-questions.md
requirements/traceability.md
PRD.md
现有代码结构
```

输出：

```text
02_TECHNICAL_DESIGN.md
```

02 要求满血 gstack-adapter 深度。完成前 agent 必须运行并记录：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  .ai-workflow/<feature-slug> --gate 02-full
```

如果失败，不能宣称“完整 gstack 评审已通过”；应继续调用/映射真实 gstack slice，或标记 `NEEDS_GSTACK_DEPTH` / `DONE_DEGRADED`。

这一阶段重点检查：

- 产品评审是否收敛本轮交付范围
- 哪些需求不做、延期或拒绝
- 工程评审是否给出清楚架构、数据模型、状态流转和 API / 集成设计
- 若存在 API 边界，`requirements/api.yaml` 是否已从可选草案升级为冻结合同
- 安全/风险评审是否覆盖权限、审计、数据安全、滥用场景和上线风险
- QA / 测试策略是否覆盖核心验收标准
- 需求变更是否写回 traceability 或开放问题

### Step 3：跑 Prototype

对 agent 说：

```text
继续跑 03 Prototype，先写 Prototype Plan，确认后再生成页面
```

要求 agent 读取：

```text
01_REQUIREMENTS.md
requirements/requirements.md
requirements/datamodel.md
requirements/clarification.md
requirements/validation.md
requirements/prd.md
02_TECHNICAL_DESIGN.md
PRD.md
```

输出：

```text
03_PROTOTYPE.md
prototype/index.html
prototype/css/style.css
prototype/pages/*.html
```

这一阶段重点检查：

- 页面是否覆盖核心用户流程
- 页面是否映射到需求 / 用户故事
- 角色、权限、状态是否能在页面上看出来
- mock data 是否真实可信
- 原型是否能直接用浏览器打开

默认只允许 HTML + CSS，不使用 JS、CDN、后端或构建工具。

进入 04 前必须运行并记录：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  .ai-workflow/<feature-slug> --gate 03-full
```

如果失败，先修 prototype approval、实际页面文件名和 traceability，不要进入 implementation。

### Step 4：跑 Implementation Planning

对 agent 说：

```text
继续跑 04 Implementation Planning，先只写计划，不实现
```

输出：

```text
04_IMPLEMENTATION.md
implementation/IMPLEMENTATION_PLAN.md
```

04 阶段默认不重新完整 brainstorming。01/02/03 已经负责需求澄清、方案评审、决策确认和原型验证。04 只做轻量 pre-plan sanity check：如果没有阻塞实现计划的 open decisions，就直接进入 superpowers writing-plans。

`implementation/IMPLEMENTATION_PLAN.md` 是权威深度实现计划，应该包含：

- 小步执行单元，而不是只写模块大纲
- 具体文件路径和文件级变更计划
- 每个执行单元的 TDD / 测试优先步骤或验证场景
- 每步命令、检查点、通过标准和失败处理
- 预期初始结果（例如先失败、待实现或基线通过）
- 风险、回滚 / 恢复说明
- 需求、AC、设计决策、原型页面到实现任务的追踪关系

`04_IMPLEMENTATION.md` 只做 workflow 摘要、门禁、执行证据和索引，不要把深度计划压缩成几张表。

建议先审 `implementation/IMPLEMENTATION_PLAN.md`，再决定是否执行。

进入执行前，agent 必须运行并记录：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  .ai-workflow/<feature-slug> --gate 04-plan
```

### Step 5：执行实现

确认计划后，对 agent 说：

```text
按 implementation/IMPLEMENTATION_PLAN.md 执行实现，并持续更新 04_IMPLEMENTATION.md 的执行日志和验证证据
```

执行时要求：

- 优先 TDD 或先定义可验证场景
- 每个任务有验证命令或检查点
- 偏离计划要写入执行日志
- 失败要记录 blocker 和处理方式
- 修改的文件要写入执行日志
- 必要时更新 `requirements/traceability.md`
- 进入 05 前必须通过 `--gate 04-complete`；如果代码已改但 04 仍是模板空表 / `TBD`，状态应标记 `BLOCKED_ARTIFACT_DRIFT`

### Step 6：跑 Verification & Review

对 agent 说：

```text
继续跑 05 Verification & Review
```

输出：

```text
05_REVIEW.md
```

这一阶段记录：

- requirements coverage
- prototype coverage（如适用）
- 测试 / build / lint 证据
- manual QA 证据
- code / architecture review 问题
- security / risk review 问题
- 已修复、接受、延期或阻塞的问题
- 剩余风险
- 发布就绪度：Ready / Ready with accepted risks / Blocked

完成前必须运行并记录：

```bash
python3 /Users/melody/.openclaw/workspace/ai-dev-workflow/scripts/validate_artifacts.py \
  .ai-workflow/<feature-slug> --gate 05-complete
```

如果 gate 失败，不能输出 Ready / 全流程通过；发布就绪度必须是 `Blocked`，或者先补齐缺失证据。

## Provider 不可用时怎么办

首选 provider（如 `requirements-analyst`、review-pack / external garrytan/gstack、superpowers）不是 workflow 自带保证可用的能力。运行每个阶段前应先做 provider availability preflight。

如果 provider 不可用：

1. 优先使用真实 provider 或 source-derived adapter：`requirements-analyst` steering、`providers/gstack-adapter/` over real gstack、`providers/superpowers-adapter/` over real superpowers；
2. 如果只有 compact fallback（如 `review-pack`），明确进入 `PROVIDER_DEGRADED`，不得冒充 full provider；
3. 如果没有可用 provider，暂停让用户安装/启用对应 skill/provider。

可先运行：

```bash
python3 scripts/check_providers.py --json
```

fallback 时必须更新 `STATUS.md`：

- Provider health
- 当前阶段状态
- 实际执行者 / fallback
- 质量风险和补偿检查

不要让 `STATUS.md` 继续显示不可用 provider，好像它真的执行过。

## 7. 阶段推进规则

默认每个阶段结束后都暂停。

推荐节奏：

```text
跑 01 → 人看 → 确认
跑 02 → 人看 → 确认
跑 03 plan → 人看 → 确认
执行 03 → 人看结果
跑 04 → 最终确认
```

如果你想无人值守，可以明确说：

```text
按工作流连续跑完，但每个阶段都更新 STATUS.md
```

但第一版测试不建议这样做。先看每个阶段产物质量。

## 8. 当前测试项目

当前已经初始化的测试项目：

```text
/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test
```

当前工作流目录：

```text
/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test/.ai-workflow/operation-ticket-management
```

当前源 PRD：

```text
/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test/PRD.md
```

当前阶段：

```text
01_REQUIREMENTS
```

下一步可以直接说：

```text
继续跑 01 Requirements
```



### guided-auto 的阶段推进语义

`guided-auto` 不是 full unattended，也不是每阶段都问“是否继续”。它的规则是：

- 普通阶段确认自动跳过，例如 00 后不再问“是否进入 01”。
- 遇到真实阻塞决策时，直接进入问答澄清环节。
- 澄清问题必须给动态选项、推荐理由和自定义输入选项。
- 用户回答后自动继续，除非仍有阻塞问题。
- 04 Planning → 04 Execution 仍是 hard stop，必须显式批准后才能写业务代码。

### Guided-auto 的澄清方式

如果使用 guided-auto，agent 应该在需要人工判断时主动提问，并给出动态选项：

- 选项数量不固定，按问题复杂度生成。
- 每个选项说明适用场景、优点、代价和后续影响。
- 每个问题都必须提供“其他 / 自定义”自由表达选项。
- 用户回答后，选择必须写入 `requirements/clarification.md`、`requirements/open-questions.md`、`STATUS.md`，必要时同步 `traceability.md`。

示例：

```text
首批交付范围怎么定？
A. 主流程 MVP（推荐）：建票→三级审核→下令→执行→收尾→归档；最快验证闭环，异常流程后续补齐。
B. 主流程 + 关键异常：包含驳回/作废/中止基础能力；更接近真实试用，但周期更长。
C. 全量 PRD：覆盖副本、三峡行云、断点续传等；适合正式项目，不适合首轮验证。
D. 其他 / 自定义：你可以直接描述希望的首批范围。
```

## 9. 判断这套工作流是否有效

测试时主要看这些问题：

1. `requirements/` 下的详细产物是否比原 PRD 更清晰、更可测试，且 `01_REQUIREMENTS.md` 是否做好摘要、索引和门禁？
2. `02_TECHNICAL_DESIGN.md` 是否能主动收敛范围，而不是照单全收？
3. `03_PROTOTYPE.md` 和 `prototype/` 是否能提前验证页面、流程、角色和状态？
4. `implementation/IMPLEMENTATION_PLAN.md` 是否保留了 superpowers writing-plans 的深度，能让另一个 agent 不看聊天记录也能执行？
5. `05_REVIEW.md` 是否有真实证据，而不是“看起来完成了”？
6. 若有前后端，是否完成 `api.yaml` ↔ backend routes ↔ frontend client calls 对账、schema/枚举/必填字段检查和分级 browser smoke？
7. 若缺 `api.yaml`，是否标记 `API_CONTRACT_DEGRADED` 且避免完整 contract parity 通过措辞？
8. `STATUS.md` 是否能让中途换 agent 也知道项目在哪里？

如果这些点成立，第一版流程就算跑通。

## 10. 后续可增强点

第一版故意保持简单。后续可以逐步加：

- `STATE.json`：机器可读状态
- slash command：一句话触发初始化/推进阶段
- artifact validator：检查 TBD、遗漏字段、状态不一致
- provider registry：把 requirements/review/superpowers 替换成任意同能力 skill
- retro 阶段：每次实现后沉淀工作流改进


### 语言一致性

Workflow 会根据用户输入和来源 PRD 自动判断主语言。中文 PRD 或中文指令场景下，阶段总结、澄清问题、下一步提示和 artifact 正文都应使用中文。Provider 内部说明或上游技能是英文时，也必须在映射到 workflow artifact 和最终回复时本地化；文件路径、命令、API operationId、枚举值等技术标识可以保留英文。
