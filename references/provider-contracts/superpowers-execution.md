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
| writing-plans | 将设计拆成可执行步骤、文件路径、命令和检查点 | `04_IMPLEMENTATION.md` |
| test-driven-development | 先定义失败测试或验证场景，再实现 | `04_IMPLEMENTATION.md` |
| executing-plans | 按计划小步执行，记录偏差和结果 | `04_IMPLEMENTATION.md` |
| subagent-driven-development | 对可并行/可隔离任务使用子代理，但主 artifact 仍由 workflow 汇总 | `04_IMPLEMENTATION.md` |
| verification-before-completion | 完成前运行测试/build/lint/手工 QA 并记录证据 | `04_IMPLEMENTATION.md` / `05_REVIEW.md` |
| requesting-code-review | 请求或模拟代码评审，记录发现和处理结果 | `05_REVIEW.md` |

## 04 阶段输出要求

必须在 `04_IMPLEMENTATION.md` 中形成：

- 实现计划：任务、目标、涉及文件、依赖、预期结果。
- 测试计划：新增/修改测试、手工验证场景、允许不写测试的例外理由。
- 执行检查点：每一步完成条件和验证方式。
- 执行日志：实际变更、偏差、阻塞项。
- 验证命令：命令、结果、失败处理。
- 变更文件清单。
- 回滚/恢复说明：如何撤销或降级风险变更。
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

- 没有实现计划就直接改代码，且事后无法还原计划和证据。
- 核心行为没有测试或验证证据，且没有明确例外批准。
- 测试/build/lint 失败但未记录原因和处理方式。
- 代码变更无法追踪回需求或设计决策。
- 发现阻塞问题但仍标记为 Ready。

## 使用提示

调用 superpowers 时，把它作为执行纪律提供者，而不是让它改写 workflow。计划、执行和验证证据都必须回填到 `04_IMPLEMENTATION.md` / `05_REVIEW.md`。
