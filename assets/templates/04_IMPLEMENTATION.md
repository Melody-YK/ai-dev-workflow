# 04 实现 — {{FEATURE_NAME}}

## 目的

用 superpowers-style 执行纪律完成实现计划、测试优先执行和证据记录。

默认门禁：先写计划，不直接实现；除非用户明确批准或要求无人值守执行。

## 输入

- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- 已生成并批准的 `prototype/`（如适用）
- `01_REQUIREMENTS.md`
- `requirements/discovery.md`
- `requirements/sort.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/clarification.md`
- `requirements/validation.md`
- `requirements/prd.md`
- `requirements/open-questions.md`
- `requirements/traceability.md`
- 现有代码结构和测试体系

## Provider contract

- 默认 provider：superpowers-style execution。
- 参考契约：`references/provider-contracts/superpowers-execution.md`。
- superpowers 只提供计划、TDD、执行和验证纪律；AI Dev Workflow 拥有阶段产物、状态和门禁。
- 04 阶段默认不重新执行完整 brainstorming。01/02/03 已负责需求澄清、方案评审、决策确认和原型验证；04 只允许做轻量 pre-plan sanity check，用于发现仍阻塞实现计划的 open decisions。
- 若 pre-plan sanity check 无阻塞项，必须直接进入 superpowers writing-plans 风格的实现计划。
- `implementation/IMPLEMENTATION_PLAN.md` 是 04 阶段的权威深度实现计划；`04_IMPLEMENTATION.md` 只作为 workflow 摘要、门禁、执行证据和索引。不得把深度计划压缩成下方摘要表格。
- 深度计划必须拆成小步执行单元。每个单元应包含 Traceability、Files、Test/verification first、Expected initial result、Implementation、Commands、Pass criteria、Failure handling。

## 详细产物索引

- `implementation/IMPLEMENTATION_PLAN.md` — superpowers writing-plans 风格的完整实现计划（小步执行单元、文件级改动、TDD/验证优先策略、每步命令、检查点、失败处理、风险、回滚和追踪关系）。

## Pre-plan sanity check

_只检查是否存在阻塞 implementation planning 的未决事项；不要重新发散需求、重做方案 brainstorming 或推翻已批准的 01/02/03 决策。_

| 检查项 | 结论 | 阻塞项 / 处理方式 |
|---|---|---|
| 01/02/03 是否已批准 |  |  |
| 技术栈/架构关键决策是否足够进入计划 |  |  |
| 原型是否提供页面/流程实现依据 |  |  |
| 是否存在必须先问用户的 blocker |  |  |

## 实现计划

_摘要索引。完整计划必须写入 `implementation/IMPLEMENTATION_PLAN.md`，不要在此处压缩替代。_

| 步骤 | 目标 | 涉及文件 | 依赖 | 完成条件 | 状态 |
|---|---|---|---|---|---|
| 1 |  |  |  |  | planned |

## 测试计划

_优先定义失败测试或可验证场景，再实现。若不写测试，必须记录例外理由和人工批准。_

| 场景 / 需求 | 测试类型 | 测试文件 / 命令 | 预期结果 | 状态 |
|---|---|---|---|---|
|  | unit / integration / e2e / manual |  |  | planned |

## 执行检查点

_每个检查点都应能被命令、测试或文件检查验证。_

| 检查点 | 验证方式 | 通过标准 | 状态 |
|---|---|---|---|
|  |  |  | pending |

## 执行日志

_实现过程中持续更新，记录实际变更、偏差、阻塞和处理结果。_

| 时间 | 操作 | 结果 | 偏差 / 备注 |
|---|---|---|---|
|  |  |  |  |

## 验证命令

_实现过程中填写。命令必须可复现，结果必须明确。_

| 命令 | 目的 | 结果 | 证据 / 日志 |
|---|---|---|---|
|  |  | pending |  |

## 变更文件

_实现过程中填写。_

| 文件 | 变更说明 | 对应需求 / 设计 |
|---|---|---|
|  |  |  |

## 回滚 / 恢复说明

_说明如何撤销、降级或隔离高风险变更。_

## 追踪关系更新

_记录实现任务如何对应到需求。必要时更新 `requirements/traceability.md`。_

## 阻塞项

- 暂无。

## 审批决策

- 计划审批状态：TBD
- 执行审批状态：TBD
- 审批人：
- 决策说明：

## 完成检查清单

- [ ] 设计已批准
- [ ] 原型已评审，或已明确跳过
- [ ] 实现计划已批准
- [ ] 已阅读需求详细产物
- [ ] 已先定义测试/验证场景，或例外已获批准
- [ ] 实现按计划完成，偏差已记录
- [ ] 验证命令已运行并记录结果
- [ ] 变更文件清单已填写
- [ ] 回滚/恢复说明已填写
- [ ] traceability 已按需更新
