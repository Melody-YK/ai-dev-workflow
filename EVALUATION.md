# 评估指南

这份指南用于判断 AI Dev Workflow 是否真的好用、可靠、值得保留。

重点不是奖励“文档写得多”，而是验证这套流程是否能让 AI 辅助开发比裸聊天更可控、更容易接手、更容易验证。

## 评估核心

一套好的 AI 研发工作流，应该改善六件事：

1. 需求更清楚
2. 范围更可控
3. 交接更容易
4. 实现计划更可执行
5. 验证证据更充分
6. 经验更容易复用

如果这些都没有改善，那这套流程只是仪式感。

## 借鉴的评估思路

这套评分表融合了常见软件工程里的几个思路：

- **需求可追踪性**：重要需求应该能一路追踪到设计、实现和验证。
- **SDLC 质量门禁**：每个阶段进入下一阶段前，都应该有明确退出标准。
- **Definition of Done**：完成不能只靠口头声明，必须有证据。
- **V 模型思路**：前面的需求和设计，后面应该能被验证和确认。
- **SWE-bench 式评估**：真实软件任务最终要看是否真的通过测试、解决问题，而不是计划看起来是否合理。
- **Agent 工作流评估**：后续 agent 应该能只靠持久化产物接手，而不是依赖私有聊天上下文。

这些不是照搬重型流程，而是改造成适合轻量 artifact-first 工作流的验收标准。

## 评估对象

通常评估一次完整工作流运行，也就是一个 PRD 或一个功能需求。

需要查看的材料：

```text
PRD 或原始需求
.ai-workflow/<feature>/00_INTAKE.md
.ai-workflow/<feature>/01_REQUIREMENTS.md
.ai-workflow/<feature>/requirements/requirements.md
.ai-workflow/<feature>/requirements/datamodel.md
.ai-workflow/<feature>/requirements/validation.md
.ai-workflow/<feature>/requirements/open-questions.md
.ai-workflow/<feature>/requirements/traceability.md
.ai-workflow/<feature>/02_TECHNICAL_DESIGN.md
.ai-workflow/<feature>/04_IMPLEMENTATION.md
.ai-workflow/<feature>/05_REVIEW.md
.ai-workflow/<feature>/STATUS.md
实现 diff，如果已经执行实现
测试 / build / lint 输出，如果已经执行实现
```

## 评分标准

每个小项按 0 到 3 分评分：

| 分数 | 含义 |
|---|---|
| 0 | 缺失或不可用 |
| 1 | 有，但很浅、很虚、难以执行 |
| 2 | 有用，基本完整 |
| 3 | 强，具体、可执行、可独立验证 |

总分：

```text
满分：72 分
MVP 通过：48+ 分，且没有关键门禁失败
强工作流：60+ 分，且没有关键门禁失败
```

如果出现关键门禁失败，即使总分很高，也判定这次运行失败。

## 评分表

### 1. 需求规格化

评估文件：`01_REQUIREMENTS.md`、`requirements/`

| 标准 | 分数 |
|---|---|
| 角色、目标、流程、实体、状态、权限、约束是否明确 | 0-3 |
| 需求是否可测试，而不是简单复制 PRD | 0-3 |
| 不确定点是否被保留为开放问题，而不是 AI 瞎猜 | 0-3 |

强信号：

```text
原 PRD 是业务叙述；`requirements/` 下保留详细需求、数据模型和验证规则，`01_REQUIREMENTS.md` 提供清晰摘要、索引和交接门禁。
```

### 2. 可追踪性

评估文件：`01_REQUIREMENTS.md`、`requirements/traceability.md`、`02_TECHNICAL_DESIGN.md`、`03_PROTOTYPE.md`、`04_IMPLEMENTATION.md`、`05_REVIEW.md`

| 标准 | 分数 |
|---|---|
| 重要 PRD 需求是否能通过 `requirements/traceability.md` 映射到需求、设计、实现、验证产物 | 0-3 |
| 不做什么、延期什么是否明确 | 0-3 |
| 验证是否回看原需求，而不是只机械检查代码 | 0-3 |

强信号：

```text
评审者能回答：这个需求在哪里处理、测试、延期或拒绝了？
```

### 3. 范围控制

评估文件：`02_TECHNICAL_DESIGN.md`

| 标准 | 分数 |
|---|---|
| 是否主动挑战过大的范围，并提出现实 MVP | 0-3 |
| 是否识别风险、依赖、边界情况和取舍 | 0-3 |
| 是否记录需要人决定的问题，而不是静默替人做产品/战略决策 | 0-3 |

强信号：

```text
流程没有照单全收 PRD，而是能推荐最小有用切片，并说明哪些内容先等一等。
```


### 4. 原型验证

评估文件：`03_PROTOTYPE.md`、`prototype/`

| 标准 | 分数 |
|---|---|
| 是否先形成 Prototype Plan，而不是直接乱生成页面 | 0-3 |
| 页面是否覆盖核心流程、角色、权限和状态 | 0-3 |
| 页面是否映射到需求 / 用户故事，并能直接打开评审 | 0-3 |

强信号：

```text
不用写正式代码，评审者就能通过静态原型发现流程缺口、页面缺失或权限理解错误。
```

### 5. 交接和可恢复性

评估文件：所有 `.ai-workflow/<feature>/` 文件，尤其是 `STATUS.md`

| 标准 | 分数 |
|---|---|
| 新 agent 不看聊天记录也能理解当前状态 | 0-3 |
| `STATUS.md` 是否准确记录阶段、决策、开放问题和下一步 | 0-3 |
| 每个阶段产物是否给下一阶段足够上下文 | 0-3 |

强信号：

```text
新开一个会话，只给 .ai-workflow/<feature>/，agent 就能说清楚做到了哪里、下一步做什么。
```

### 6. 实现准备度

评估文件：`04_IMPLEMENTATION.md`

| 标准 | 分数 |
|---|---|
| 任务是否小、顺序清楚、可执行 | 0-3 |
| 文件路径、命令、预期输出、验证步骤是否具体 | 0-3 |
| 适合的地方是否使用 TDD 或其他验证优先方法 | 0-3 |

强信号：

```text
另一个 agent 可以直接执行计划，不需要隐藏聊天上下文，也不用临时补大量设计决策。
```

### 7. 验证质量

评估文件：`05_REVIEW.md`

| 标准 | 分数 |
|---|---|
| 是否记录测试 / build / lint / 手工 QA 的命令和结果 | 0-3 |
| 是否根据前面需求检查覆盖情况 | 0-3 |
| 剩余风险是否被分类为已修复、已接受、延期或阻塞 | 0-3 |

强信号：

```text
流程结束时留下的是证据，而不是“看起来没问题”。
```

### 8. 流程效率和摩擦

评估文件：`STATUS.md`、用户反馈、运行记录

| 标准 | 分数 |
|---|---|
| 流程是否增加了有效控制，而不是无意义仪式 | 0-3 |
| 人工确认点是否放在真正重要的决策位置 | 0-3 |
| 相比裸聊天，是否减少返工、混乱或重复补上下文 | 0-3 |

强信号：

```text
用户感觉这些门禁提高了控制力，而不是没必要地拖慢节奏。
```

## 关键门禁失败

出现以下任一情况，本次运行直接失败：

- 需要审批时，流程在需求/设计/原型确认前就开始写代码。
- 能验证却没有做任何有意义验证，就声称完成。
- 新 agent 无法从 artifact 判断当前阶段或下一步。
- 重要 PRD 需求消失了，且没有在 `requirements/traceability.md` 或后续 artifact 中标记为延期、拒绝或不在范围内。
- 原型阶段声称完成，但没有页面映射、无法打开，或绕过了明确要求的静态约束。
- 流程静默替用户做了产品、安全、合规、集成等需要人工确认的决策。

## 对比实验：裸聊天 vs 工作流

证明价值最好的方式，是同一个 PRD 跑两组。

### A 组：裸聊天基线

提示词：

```text
阅读这个 PRD 并实现它。
```

记录：

- 输出质量
- 是否漏需求
- 是否范围漂移
- 是否有测试证据
- 新会话是否容易接手
- 澄清次数和返工点

### B 组：AI Dev Workflow

按阶段跑：

```text
00 Intake
→ 01 Requirements
→ 02 Product & Engineering Review
→ 03 Prototype
→ 04 Implementation
→ 05 Verification & Review
```

记录同样指标。

### 预期改善

| 维度 | 裸聊天常见问题 | 工作流应该做到 |
|---|---|---|
| 需求 | 把业务描述和假设混在一起 | 规格化、可测试 |
| 范围 | 想全做或随机取舍 | 有意识地收敛 |
| 交接 | 依赖聊天历史 | 依赖 artifact |
| 原型 | 没有可视化验证，直接写代码 | 先用静态原型验证页面和流程 |
| 执行 | 太早开始写代码 | 先计划再实现 |
| 验证 | 口头说完成 | 记录证据 |
| 恢复 | 换 agent 难接手 | 看 `STATUS.md` 即可理解 |

## 新 agent 接手测试

这是最重要的实践测试。

1. 新开一个 agent / 会话。
2. 只提供：

```text
.ai-workflow/<feature>/STATUS.md
.ai-workflow/<feature>/01_REQUIREMENTS.md
.ai-workflow/<feature>/requirements/requirements.md
.ai-workflow/<feature>/requirements/datamodel.md
.ai-workflow/<feature>/requirements/validation.md
.ai-workflow/<feature>/requirements/open-questions.md
.ai-workflow/<feature>/requirements/traceability.md
.ai-workflow/<feature>/02_TECHNICAL_DESIGN.md
```

3. 问它：

```text
当前项目状态是什么？已经做了哪些决策？有什么阻塞？下一步应该做什么？
```

通过标准：

- 能识别正确阶段。
- 下一步和 `STATUS.md` 一致。
- 能提到开放问题和风险。
- 不需要隐藏聊天上下文。

## PRD 到验证的追踪测试

从 PRD 里挑 5 个重要需求。

逐个填表：

| PRD 需求 | Requirements 位置 | Design 位置 | Implementation 任务 | Verification 证据 | 状态 |
|---|---|---|---|---|---|
|  |  |  |  |  | covered/deferred/rejected/missing |

通过标准：

- 5 个里至少 4 个被覆盖、明确延期或明确拒绝。
- 0 个静默消失。

## 评估报告模板

一次运行结束后，可以复制到 `.ai-workflow/<feature>/EVALUATION.md`：

```markdown
# Evaluation — <feature>

## Summary

- Source PRD:
- Workflow directory:
- Evaluator:
- Date:
- Final score: /63
- Result: pass/fail/strong

## Scores

| Area | Score | Notes |
|---|---:|---|
| Requirement normalization | /9 |  |
| Traceability | /9 |  |
| Scope control | /9 |  |
| Handoff and resumability | /9 |  |
| Implementation readiness | /9 |  |
| Verification quality | /9 |  |
| Workflow efficiency and friction | /9 |  |

## Critical gate failures

- [ ] None
- [ ] Code before approval
- [ ] Completion without verification
- [ ] Cannot resume from artifacts
- [ ] Requirement disappeared silently
- [ ] Human decision silently invented

## Fresh-agent handoff result

描述新 agent 只拿 artifact 接手时的表现。

## Traceability sample

| PRD requirement | Requirements | Design | Implementation | Verification | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## What worked

- 

## What failed or felt heavy

- 

## Workflow changes to make

- 
```

## 第一版推荐验收标准

第一版公开使用前，建议满足：

1. 新 agent 可以只靠 artifact 接手。
2. requirements 产物比原 PRD 更清楚、更可测试。
3. design review 能收敛范围，或记录为什么需要完整范围。
4. implementation plan 不依赖隐藏聊天上下文也能执行。
5. verification 有真实证据。
6. 相比裸聊天，在以下 6 项中至少 4 项更好：清晰度、范围控制、交接、实现准备度、验证、返工减少。

一句话标准：

```text
这套流程好不好，看它能不能把 AI 开发从“聊天驱动的即兴发挥”，变成“产物驱动、可接手、可验证的执行”。
```
