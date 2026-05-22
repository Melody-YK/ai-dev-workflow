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
- `requirements/api.yaml`（API 边界存在时）
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `04_IMPLEMENTATION.md`
- 实现 diff

## Provider contract

- 默认 provider：superpowers verification + optional gstack review/QA/risk review。
- 参考契约：
  - `references/provider-contracts/superpowers-execution.md`
  - `references/provider-contracts/gstack-review.md`


## 验证范围契约

05 阶段不依赖用户在提示词里手写验证清单。进入本阶段后，agent 必须主动读取 01/02/03/04 产物、`implementation/IMPLEMENTATION_PLAN.md` 和当前实现代码，并完成以下验证：

- 运行可用的 test / build / lint / typecheck；无法运行时必须说明原因和影响。
- 对照 `requirements/` 检查需求、验收标准和延期项覆盖情况。
- 对照 `03_PROTOTYPE.md` 和 `prototype/` 检查页面、流程、角色权限、状态和异常场景覆盖情况。
- 验证核心路径与异常路径：建票、提交、三级审核、下令、执行、校验归档、驳回、作废、中止、越权访问。
- 若存在 API 边界，必须执行 API parity review：`requirements/api.yaml` ↔ 后端 route inventory ↔ 前端/client API calls。任何不一致必须记录为 issue；阻塞核心页面/流程的 mismatch 不能标记 Ready。
- 若存在 API 边界但 `requirements/api.yaml` 缺失，必须进入 `API_CONTRACT_DEGRADED`：只能做 “API Route Parity（无独立 api.yaml 契约）”，并把缺失 contract 记录为 workflow artifact issue；不得宣称完整 API contract parity。
- API parity 不只检查 method/path，还必须检查 request/response shape、required fields、enum values、auth/role、状态转换副作用和前端实际调用 payload。
- 对前端应用必须执行 browser smoke / manual QA，并按证据等级标注：`app-load-smoke`（应用可加载）、`authenticated-page-smoke`（登录后页面可用）、`core-flow-browser-smoke`（核心流程交互可用）。仅后端 API 脚本通过，不能声明“前端全流程可用”。
- 记录问题的严重度、复现方式、影响范围、建议修复方案和处理状态。
- 不新增大功能；只允许验证、评审、证据记录和必要的小修复建议。

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

## API 合同一致性证据

_适用于任何 API 边界。若缺少 `requirements/api.yaml`，本节标题应改为 “API Route Parity（无独立 api.yaml 契约）”，并记录 `API_CONTRACT_DEGRADED`。_

| Contract operation / route | Request schema / enum / required fields | Backend route evidence | Frontend/client call evidence | 结果 | 问题 |
|---|---|---|---|---|---|
|  |  |  |  | pending |  |

## Browser / 前端 Smoke 证据

_适用于有前端的项目。记录证据等级、页面、操作、network/console 结果。不能用 app-load 证据证明核心流程可用。_

证据等级：

- `app-load-smoke`：dev server / production build 可打开，页面标题或 root app 渲染。
- `authenticated-page-smoke`：真实登录后访问关键页面，无阻塞 network/console 错误。
- `core-flow-browser-smoke`：真实浏览器执行核心业务流程，如登录→建票→审核→执行→归档。

| 等级 | 页面 / 流程 | 操作 | Network / Console 结果 | 结论 |
|---|---|---|---|---|
| app-load-smoke / authenticated-page-smoke / core-flow-browser-smoke |  |  | pending | pending |

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

## 业务语义风险 / 修复副作用

_如果修复改变了必填字段、权限归属、状态机、审批语义、数据保留或外部集成行为，必须在这里记录 residual risk / decision needed。_

| 变更 | 可能影响 | 处理方式 | 状态 |
|---|---|---|---|
|  |  | accepted / deferred / blocked / decision-needed | open |

## 剩余风险

_评审时填写。所有剩余风险必须是 accepted / deferred / blocked 之一，并说明责任人或后续动作。_

## 发布就绪度

- 状态：TBD
- 建议：TBD
- 可选值：Ready / Ready with accepted risks / Blocked

## 最终一致性扫描

_完成前必须跨 `05_REVIEW.md`、`STATUS.md`、`requirements/traceability.md` 扫描并修正过度乐观或降级不一致的措辞。_

需检查的词/短语包括但不限于：`Ready`、`全流程通过`、`可正常使用`、`API 合同一致`、`API Contract Parity`、`TBD`、旧 checklist 未完成项。

| 扫描项 | 结果 | 修正位置 |
|---|---|---|
|  | pending |  |

## 追踪关系更新

_必要时将验证证据更新到 `requirements/traceability.md`。_

## 完成检查清单

- [ ] 已基于详细需求产物检查需求覆盖
- [ ] 已检查原型覆盖，或标记为不适用
- [ ] 已记录测试/build/lint 证据
- [ ] 已记录手工 QA 证据，或说明不适用
- [ ] 若存在 API 边界，已完成 API contract/backend route/frontend client 三方对账；若缺 `api.yaml`，已标记 `API_CONTRACT_DEGRADED` 且未使用完整 contract parity 通过措辞
- [ ] 若存在前端，已按 app-load / authenticated-page / core-flow 等级记录 browser smoke 和 network/console 证据
- [ ] 已完成代码/架构评审，或说明不适用
- [ ] 已完成安全/风险复查，或说明不适用
- [ ] 所有 blocking 问题已修复，或发布状态标记为 Blocked
- [ ] 修复副作用 / 业务语义风险已记录，尤其是必填字段、权限、状态机和审批语义变化
- [ ] 已完成最终一致性扫描，`STATUS.md` 和 `traceability.md` 没有残留过度乐观结论
- [ ] 必要时已将验证证据更新到 traceability
- [ ] 用户已接受结果
