# AI Dev Workflow 使用说明

这是一套轻量、可控、可替换的 AI 研发工作流，用来把一个 PRD 或原始需求，按阶段交给不同能力型 skill 处理，并通过固定 artifact 文件完成交接。

核心目标不是“自动化一切”，而是让每一步都有明确输入、输出、人工确认点和质量门禁。

AI Dev Workflow 定义稳定的阶段契约和 artifact 位置；`requirements-analyst`、gstack-style review、`superpowers` 等外部 skill 是能力提供者，可以保留有价值的原生产物，但必须写入 workflow 指定的位置。

## 1. 工作流定位

默认编排三个能力：

```text
requirements-analyst → gstack-style review → prototype generation → superpowers
```

它们的分工是：

| 阶段 | 负责什么 | 默认能力 |
|---|---|---|
| 00 Intake | 收集原始需求、建立工作目录 | ai-dev-workflow |
| 01 Requirements | 把 PRD 转成明确、可验证的需求规格 | requirements-analyst |
| 02 Product & Engineering Review | 审范围、审架构、审风险、定本轮交付范围 | gstack-style review |
| 03 Prototype | 生成需求驱动的静态 HTML/CSS 原型，验证页面、流程、角色和状态 | requirements-analyst prototype approach |
| 04 Implementation | 写实现计划、TDD 实现、记录验证 | superpowers |
| 05 Verification & Review | 测试、review、QA、发布前确认 | superpowers + optional gstack |

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
│   ├── api.yaml                # optional
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

这一阶段重点检查：

- 是否建议收敛本轮交付范围
- 哪些需求不做
- 架构是否清楚
- 数据模型方向是否合理
- 状态流转是否闭环
- 风险和测试策略是否明确

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

### Step 4：跑 Implementation Planning

对 agent 说：

```text
继续跑 04 Implementation Planning，先只写计划，不实现
```

输出：

```text
04_IMPLEMENTATION.md
```

这一阶段应该包含：

- 具体任务拆分
- 具体文件路径
- 测试优先步骤
- 每步验证命令
- 预期输出
- 是否需要人工确认

建议先审计划，再决定是否执行。

### Step 5：执行实现

确认计划后，对 agent 说：

```text
按 04_IMPLEMENTATION.md 执行实现
```

执行时要求：

- 优先 TDD
- 每个任务有验证命令
- 失败要记录 blocker
- 修改的文件要写入执行日志

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
- 测试 / build / lint 证据
- manual QA 证据
- code review 问题
- 已修复问题
- 剩余风险
- 是否建议交付

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

## 9. 判断这套工作流是否有效

测试时主要看这些问题：

1. `requirements/` 下的详细产物是否比原 PRD 更清晰、更可测试，且 `01_REQUIREMENTS.md` 是否做好摘要、索引和门禁？
2. `02_TECHNICAL_DESIGN.md` 是否能主动收敛范围，而不是照单全收？
3. `03_PROTOTYPE.md` 和 `prototype/` 是否能提前验证页面、流程、角色和状态？
4. `04_IMPLEMENTATION.md` 是否能让另一个 agent 不看聊天记录也能执行？
5. `05_REVIEW.md` 是否有真实证据，而不是“看起来完成了”？
6. `STATUS.md` 是否能让中途换 agent 也知道项目在哪里？

如果这些点成立，第一版流程就算跑通。

## 10. 后续可增强点

第一版故意保持简单。后续可以逐步加：

- `STATE.json`：机器可读状态
- slash command：一句话触发初始化/推进阶段
- artifact validator：检查 TBD、遗漏字段、状态不一致
- provider registry：把 requirements/gstack/superpowers 替换成任意同能力 skill
- retro 阶段：每次实现后沉淀工作流改进
