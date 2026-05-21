# 05 验证与评审 — {{FEATURE_NAME}}

## 目的

证明实现满足需求，并具备交付/交接条件。

本阶段结合 superpowers verification-before-completion 和可选 gstack-style release / QA / risk review。所有结论必须有证据或明确标记为阻塞/例外。

## 输入

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
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `04_IMPLEMENTATION.md`
- 实现 diff

## Provider contract

- 默认 provider：superpowers verification + optional gstack review/QA/risk review。
- 参考契约：
  - `references/provider-contracts/superpowers-execution.md`
  - `references/provider-contracts/gstack-review.md`

## 需求覆盖情况

_评审时填写。使用详细需求产物；必要时将证据更新到 `requirements/traceability.md`。_

| 需求 | 实现位置 | 验证证据 | 状态 |
|---|---|---|---|
|  |  |  | pending |

## 原型覆盖情况

_适用时，将实现行为与已批准原型进行对比。_

| 原型页面 / 流程 | 实现位置 | 差异 | 状态 |
|---|---|---|---|
|  |  |  | pending |

## 测试 / build / lint 证据

_记录所有已运行命令。失败必须记录原因、处理方式和是否仍阻塞。_

| 命令 | 目的 | 结果 | 日志 / 证据 |
|---|---|---|---|
|  |  | pending |  |

## 手工 QA 证据

_适用时填写。_

| 场景 | 操作路径 | 结果 | 证据 |
|---|---|---|---|
|  |  | pending |  |

## 代码 / 架构评审发现

_记录 superpowers requesting-code-review 或 gstack engineering review 的发现。_

| 发现 | 严重度 | 处理方式 | 状态 |
|---|---|---|---|
|  | low / medium / high / blocking | fixed / accepted / deferred / blocked | open |

## 安全 / 风险复查

| 风险 | 严重度 | 处理方式 | 状态 |
|---|---|---|---|
|  | low / medium / high / blocking | fixed / accepted / deferred / blocked | open |

## 剩余风险

_评审时填写。所有剩余风险必须是 accepted / deferred / blocked 之一，并说明责任人或后续动作。_

## 发布就绪度

- 状态：TBD
- 建议：TBD
- 可选值：Ready / Ready with accepted risks / Blocked

## 追踪关系更新

_必要时将验证证据更新到 `requirements/traceability.md`。_

## 完成检查清单

- [ ] 已基于详细需求产物检查需求覆盖
- [ ] 已检查原型覆盖，或标记为不适用
- [ ] 已记录测试/build/lint 证据
- [ ] 已记录手工 QA 证据，或说明不适用
- [ ] 已完成代码/架构评审，或说明不适用
- [ ] 已完成安全/风险复查，或说明不适用
- [ ] 所有 blocking 问题已修复，或发布状态标记为 Blocked
- [ ] 必要时已将验证证据更新到 traceability
- [ ] 用户已接受结果
