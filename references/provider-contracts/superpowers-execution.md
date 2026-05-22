# superpowers Execution Contract

`superpowers` 在本 workflow 中负责把已批准的设计和原型转成纪律化实现：先计划、再执行、最后验证。

## 适用阶段

- 04 实现：写实现计划、拆分任务、TDD / 小步执行、记录证据。
- 05 验证与评审：完成前验证、请求 review、整理测试与风险证据。

## 输入

04 阶段必须读取：

- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- 已批准的 `prototype/`（如存在）
- `01_REQUIREMENTS.md`
- `requirements/` 下详细需求产物
- 现有代码结构和测试体系

05 阶段必须读取：

- `04_IMPLEMENTATION.md`
- 实现 diff
- 相关测试结果
- 需求、设计和原型 artifact

## 子能力

| 子能力 | 用途 | 主要输出位置 |
|---|---|---|
| pre-plan sanity check | 轻量确认 01/02/03 是否足以进入实现计划，只发现 blocker，不重新 brainstorming | `04_IMPLEMENTATION.md` |
| writing-plans | 将设计拆成可执行步骤、文件路径、命令和检查点 | `implementation/IMPLEMENTATION_PLAN.md` |
| test-driven-development | 先定义失败测试或验证场景，再实现 | `04_IMPLEMENTATION.md` |
| executing-plans | 按计划小步执行，记录偏差和结果 | `04_IMPLEMENTATION.md` |
| subagent-driven-development | 对可并行/可隔离任务使用子代理，但主 artifact 仍由 workflow 汇总 | `04_IMPLEMENTATION.md` |
| verification-before-completion | 完成前运行测试/build/lint/手工 QA 并记录证据 | `04_IMPLEMENTATION.md` / `05_REVIEW.md` |
| requesting-code-review | 请求或模拟代码评审，记录发现和处理结果 | `05_REVIEW.md` |

## 04 阶段输出要求

04 阶段默认不重新执行完整 `brainstorming`。01/02/03 已经负责需求澄清、方案发散/评审、决策确认和原型验证。04 只允许做轻量 pre-plan sanity check：读取既有产物，确认是否有仍阻塞实现计划的 open decisions；若无 blocker，直接进入 `writing-plans`。

必须形成两个层次的产物：

```text
implementation/IMPLEMENTATION_PLAN.md  # superpowers writing-plans 的权威深度计划
04_IMPLEMENTATION.md                   # workflow 摘要、门禁、执行证据和索引
```

`implementation/IMPLEMENTATION_PLAN.md` 必须保留完整 planning 深度，不得被压缩进 `04_IMPLEMENTATION.md` 的摘要表格。它至少包含：

- 实现计划：任务、目标、涉及文件、依赖、预期结果。
- 小步执行单元：每个任务必须拆成可单独执行/验证的步骤，而不是只写模块大纲。
- 测试优先顺序：每个可测试任务必须写明「先写/调整哪个测试或验证场景 → 预期失败/待验证 → 实现哪些文件 → 运行哪些命令确认通过」。
- 测试计划：新增/修改测试、手工验证场景、允许不写测试的例外理由。
- 执行检查点：每一步完成条件和验证方式。
- 文件级变更计划：预计创建/修改的文件和原因。
- 命令计划：每个执行单元对应的安装、测试、构建、lint、运行或人工验证命令；不要只在文末列总体验证命令。
- 失败处理：关键命令失败时如何诊断、回退或标记 blocker。
- 风险与回滚/恢复说明：如何撤销或降级风险变更。
- 追踪关系：每个执行单元对应哪些需求 / AC、设计决策和原型页面。

推荐执行单元格式：

```markdown
### Step <n>: <目标>

- Traceability: US-xxx / AC-xxx / E-x / prototype/pages/<page>.html
- Files: <预计创建或修改的文件>
- Test/verification first: <先写或先运行的测试/验证；没有自动测试时说明人工验证>
- Expected initial result: <预期失败、待补实现或基线通过>
- Implementation: <具体实现动作>
- Commands: `<可复现命令>`
- Pass criteria: <通过标准>
- Failure handling: <失败处理或 blocker 记录方式>
```

`04_IMPLEMENTATION.md` 必须记录：

- pre-plan sanity check 结论和 blocker。
- 指向 `implementation/IMPLEMENTATION_PLAN.md` 的索引和摘要。
- 执行日志：实际变更、偏差、阻塞项。
- 验证命令：命令、结果、失败处理。
- 变更文件清单。
- 追踪关系更新：实现任务对应哪些需求。

默认门禁：只写计划，不直接实现；除非用户明确批准或要求无人值守执行。

## 05 阶段输出要求

必须在 `05_REVIEW.md` 中形成：

- 需求覆盖证据。
- 原型覆盖证据（适用时）。
- 测试/build/lint 证据。
- 手工 QA 证据（适用时）。
- 代码评审发现和处理结果。
- 剩余风险和发布建议。

## 失败条件

出现以下任一情况，不应声明完成：

- 04 阶段重新展开完整 brainstorming，覆盖或推翻已批准的 01/02/03 决策，但没有明确人工要求。
- 没有 `implementation/IMPLEMENTATION_PLAN.md` 深度计划就直接改代码，且事后无法还原计划和证据。
- 将 superpowers writing-plans 的深度内容压缩成 `04_IMPLEMENTATION.md` 的摘要表格，导致小步执行单元、测试优先顺序、文件级计划、命令、检查点、风险或追踪关系缺失。
- `implementation/IMPLEMENTATION_PLAN.md` 只有模块大纲，没有每个执行单元的 test/verification-first 步骤、命令、通过标准和失败处理。
- 核心行为没有测试或验证证据，且没有明确例外批准。
- 测试/build/lint 失败但未记录原因和处理方式。
- 代码变更无法追踪回需求或设计决策。
- 发现阻塞问题但仍标记为 Ready。

## 使用提示

调用 superpowers 时，把它作为执行纪律提供者，而不是让它改写 workflow。深度计划写入 `implementation/IMPLEMENTATION_PLAN.md`；执行和验证证据回填到 `04_IMPLEMENTATION.md` / `05_REVIEW.md`。
