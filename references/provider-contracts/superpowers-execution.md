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
- `requirements/api.yaml`（若存在 API 边界）
- 现有代码结构和测试体系

05 阶段必须读取：

- `04_IMPLEMENTATION.md`
- 实现 diff
- 相关测试结果
- 需求、设计和原型 artifact
- `requirements/api.yaml`、后端 route inventory、前端/client API calls（若存在 API 边界）

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

## Fidelity tiers and source skills

Do not infer full superpowers fidelity from provider availability alone.

- `ADAPTER_FULL`: the host runtime actually invoked the native external superpowers skill, e.g. `superpowers:writing-plans`, `superpowers:subagent-driven-development`, `superpowers:executing-plans`, `superpowers:verification-before-completion`, or `superpowers:requesting-code-review`, and the output is mapped into workflow artifacts.
- `BUNDLED_SOURCE_SLICE`: native skill invocation was unavailable, but the source-derived files under `providers/superpowers-adapter/references/source-skills/` were loaded and followed.
- `COMPACT_FALLBACK` / `SUPERPOWERS_STYLE`: only summaries/contracts were followed. This must not be called full superpowers output.

Required source files by phase:

- 04 planning: `providers/superpowers-adapter/references/source-skills/writing-plans/SKILL.md`.
- 04 execution with subagents: `providers/superpowers-adapter/references/source-skills/subagent-driven-development/SKILL.md` plus its prompt files.
- 04 inline execution: `providers/superpowers-adapter/references/source-skills/executing-plans/SKILL.md`.
- Testable implementation work: `providers/superpowers-adapter/references/source-skills/test-driven-development/SKILL.md`.
- 05 verification: `providers/superpowers-adapter/references/source-skills/verification-before-completion/SKILL.md`.
- 05 review: `providers/superpowers-adapter/references/source-skills/requesting-code-review/SKILL.md`.

Phase artifacts must record `Superpowers fidelity`, `Planning source`, and the intended/used execution source. If this evidence is missing, the phase is at most `COMPACT_FALLBACK`.

## 04 阶段输出要求

04 阶段默认不重新执行完整 `brainstorming`。01/02/03 已经负责需求澄清、方案发散/评审、决策确认和原型验证。04 只允许做轻量 pre-plan sanity check：读取既有产物，确认是否有仍阻塞实现计划的 open decisions；若无 blocker，直接进入 `writing-plans`。

必须形成两个层次的产物：

```text
implementation/IMPLEMENTATION_PLAN.md  # superpowers writing-plans 的权威深度计划
04_IMPLEMENTATION.md                   # workflow 摘要、门禁、执行证据和索引
```

`implementation/IMPLEMENTATION_PLAN.md` 必须保留完整 planning 深度，不得被压缩进 `04_IMPLEMENTATION.md` 的摘要表格。它至少包含：

- Native writing-plans header: plan title, `For agentic workers: REQUIRED SUB-SKILL...`, `Goal`, `Architecture`, and `Tech Stack`.
- Task/checkbox shape from `writing-plans`: `### Task N`, exact `Files` section, and `- [ ] Step ...` entries.
- Bite-sized steps: tasks must be executable by an agent with little project context; avoid giant module buckets.
- No placeholders: no `TBD`, `TODO`, `implement later`, `add appropriate error handling`, `write tests for the above`, `similar to Task N`, or unexplained wildcard file plans as primary instructions.

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
- API 合同一致性：如果存在 API 边界，每个相关执行单元必须说明对应的 `requirements/api.yaml` operation，以及后端 route、前端/client call 和验证方式。
- 降级模式：如果 API-bearing 项目缺少 `requirements/api.yaml`，必须进入 `API_CONTRACT_DEGRADED`，先回填 baseline contract 或明确限制为 route parity；不得宣称完整 API contract parity。
- schema parity：API 检查必须覆盖 method/path、required fields、enum values、request/response shape、auth/role 和状态副作用。
- 语义风险：如果修复改变必填字段、权限归属、状态机或审批语义，必须记录 residual risk / decision needed。

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

### 04 gate enforcement

04 不允许出现“代码已经生成，但 `04_IMPLEMENTATION.md` 仍是模板”的状态。任何产品代码变更发生后，必须同步回填：

- 执行日志：实际做了什么、结果、偏差。
- 验证命令：运行了哪些命令、结果是什么、失败如何处理。
- 变更文件：创建/修改的关键文件和对应需求/设计。
- 回滚/恢复说明。
- 审批决策：计划审批和执行审批必须是明确状态，不得保留 `TBD`。

进入执行前必须能通过：

```bash
scripts/validate_artifacts.py <workflow-dir> --gate 04-plan
```

进入 05 前必须能通过：

```bash
scripts/validate_artifacts.py <workflow-dir> --gate 04-complete
```

如果 gate 失败，必须修正 artifact 或将 `STATUS.md` 标记为 `BLOCKED_ARTIFACT_DRIFT`，不能继续声称 04 完成。

## 05 阶段输出要求

05 阶段必须自己从 workflow artifacts 推导验证范围，不要求用户在提示词里重复验证清单。必须读取 01/02/03/04 产物、`implementation/IMPLEMENTATION_PLAN.md`、实现 diff 和当前代码。

必须在 `05_REVIEW.md` 中形成：

- 需求覆盖证据：对照 `requirements/`、验收标准、延期项和 traceability。
- 原型覆盖证据：对照 `03_PROTOTYPE.md` 和 `prototype/`，检查页面、流程、角色权限、状态和异常场景。
- 测试/build/lint/typecheck 证据：运行所有可用命令；无法运行时记录原因、影响和替代验证。
- API 合同一致性证据：若存在 API 边界，必须比较 `requirements/api.yaml`、后端 route inventory 和前端/client API calls。任何 mismatch 都要记录；阻塞核心页面/流程的 mismatch 不能标记 Ready。缺少 `api.yaml` 时必须标记 `API_CONTRACT_DEGRADED`，只能称为 API Route Parity。
- Browser / 前端 smoke 证据：若存在前端，必须按 `app-load-smoke`、`authenticated-page-smoke`、`core-flow-browser-smoke` 分级记录 network/console 结果。仅后端脚本通过不能证明前端可用。
- 核心路径与异常路径验证：至少覆盖建票、提交、三级审核、下令、执行、校验归档、驳回、作废、中止、越权访问；如不适用必须说明。
- 手工 QA 证据（适用时）。
- 代码/架构评审发现和处理结果。
- 安全/风险复查发现和处理结果。
- 问题清单：严重度、复现方式、影响范围、建议修复方案、处理状态。
- 剩余风险和发布建议：Ready / Ready with accepted risks / Blocked。
- 最终一致性扫描：完成前必须检查 `05_REVIEW.md`、`STATUS.md`、`requirements/traceability.md` 中是否残留与证据不匹配的 “Ready / 全流程通过 / 可正常使用 / API 合同一致 / API Contract Parity / TBD” 等措辞。

05 不应新增大功能；只允许验证、评审、证据记录和必要的小修复建议。

05 完成前必须能通过：

```bash
scripts/validate_artifacts.py <workflow-dir> --gate 05-complete
```

如果 gate 失败，不得给出 `Ready` 或“全流程通过”结论；发布建议必须是 `Blocked`，或者先补齐证据和一致性扫描。

## 失败条件

出现以下任一情况，不应声明完成：

- 04 阶段重新展开完整 brainstorming，覆盖或推翻已批准的 01/02/03 决策，但没有明确人工要求。
- 没有 `implementation/IMPLEMENTATION_PLAN.md` 深度计划就直接改代码，且事后无法还原计划和证据。
- 代码已经改动，但 `04_IMPLEMENTATION.md` 的执行日志、验证命令、变更文件或审批决策仍是空表 / `TBD`。
- 将 superpowers writing-plans 的深度内容压缩成 `04_IMPLEMENTATION.md` 的摘要表格，导致小步执行单元、测试优先顺序、文件级计划、命令、检查点、风险或追踪关系缺失。
- `implementation/IMPLEMENTATION_PLAN.md` 只有模块大纲，没有每个执行单元的 test/verification-first 步骤、命令、通过标准和失败处理。
- 05 阶段没有主动运行可用的 test / build / lint / typecheck，也没有说明无法运行的原因和影响。
- 05 阶段没有对照需求、原型和实现计划做覆盖检查。
- 存在 API 边界但没有做 API contract/backend route/frontend client 三方对账。
- API-bearing 项目缺少 `requirements/api.yaml`，但没有标记 `API_CONTRACT_DEGRADED` 或仍宣称完整 contract parity。
- API parity 只检查 path，不检查 request/response shape、required fields、enum values、auth/role 和状态副作用。
- 存在前端但只验证后端 API 脚本，没有 browser smoke / network / console 证据，却声明前端全流程可用。
- 核心行为没有测试或验证证据，且没有明确例外批准。
- 测试/build/lint 失败但未记录原因和处理方式。
- 代码变更无法追踪回需求或设计决策。
- 发现阻塞问题但仍标记为 Ready。

## 使用提示

调用 superpowers 时，把它作为执行纪律提供者，而不是让它改写 workflow。深度计划写入 `implementation/IMPLEMENTATION_PLAN.md`；执行和验证证据回填到 `04_IMPLEMENTATION.md` / `05_REVIEW.md`。
