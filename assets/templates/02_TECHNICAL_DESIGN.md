# 02 产品与工程评审 — {{FEATURE_NAME}}

## 目的

挑战需求范围，收敛本轮交付范围，并形成可实现的技术设计。

本阶段使用 review-pack 作为多角色评审能力：产品、工程、安全/风险、QA。

本文件是 02 阶段的 workflow 级摘要、决策和门禁 artifact；不要把多角色评审压扁在本文件里。深度评审必须先写入 `reviews/`，再汇总到本文件。

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
- 来源 PRD：`{{SOURCE_PRD}}`
- 现有代码结构 / 技术约束（如存在）

## Provider contract

- 默认 provider：review-pack（compact internal provider；不等同完整 garrytan/gstack）。
- 参考契约：`references/provider-contracts/review-pack.md`。
- review-pack 只提供 review 能力；AI Dev Workflow 拥有阶段产物、状态和门禁。外部 garrytan/gstack 仅在已安装并明确选择时作为增强 provider。

## 评审产物索引

02 阶段必须先生成或更新：

```text
reviews/
├── product-review.md
├── engineering-review.md
├── security-risk-review.md
└── qa-review.md
```

| Artifact | 状态 | 用途 |
|---|---|---|
| `reviews/product-review.md` | 计划中 | 产品范围、用户价值、非目标、产品风险和人工决策 |
| `reviews/engineering-review.md` | 计划中 | 架构、数据模型、状态机、API / 集成、工程取舍 |
| `reviews/security-risk-review.md` | 计划中 | 权限、审计、数据保护、滥用场景、阻塞风险 |
| `reviews/qa-review.md` | 计划中 | 验收覆盖、测试路径、回归风险、证据要求 |

## Executive summary

_在深度 review notes 完成后填写。用 5-8 条写清楚本阶段最重要的判断、阻塞项和推荐下一步。_

## 产品评审摘要

_从 `reviews/product-review.md` 汇总。检查用户价值、业务目标、角色/流程完整性、范围是否过大，以及本轮交付边界。_

### 推荐本轮交付范围

_由产品评审填写。_

### 不做什么

_明确本轮不做、延期或拒绝的需求，并说明原因。_

### 产品风险

_记录价值、体验、流程、角色、运营或 adoption 风险。_

## 工程评审摘要

_从 `reviews/engineering-review.md` 汇总。检查架构、数据模型、状态流转、接口、迁移、可维护性和实现复杂度。_

### 架构设计

_由工程评审填写。_

### 数据模型方向

_引用 `requirements/datamodel.md`，并说明必要调整或取舍。_

### 状态流转

_记录关键状态、转换条件、异常路径和权限边界。_

### API 与集成

_记录接口、第三方依赖、内部服务、数据同步或事件机制。_

#### API contract review

如果本轮包含前后端、client/server、服务间或外部 HTTP 边界，02 必须审查并冻结 `requirements/api.yaml`。不能只写“API 已对齐”。

| 检查项 | 结论 | 证据 / 处理方式 |
|---|---|---|
| `requirements/api.yaml` 是否存在，或明确 not-applicable |  |  |
| 本轮交付 API 是否覆盖核心流程和异常路径 |  |  |
| 每个 operation 是否包含 method/path/auth/request/response/status/traceability |  |  |
| 前端页面/原型是否能映射到 API operation |  |  |
| 延期、mock、外部集成和内部-only API 是否已标记 |  |  |

### 工程取舍

_记录为什么选择当前方案，以及被拒绝的备选方案。_

## 安全 / 风险评审摘要

_从 `reviews/security-risk-review.md` 汇总。检查权限、审计、数据安全、滥用场景、合规风险和上线风险。_

| 风险 | 影响 | 概率 | 缓解方式 | 负责人 | 状态 |
|---|---|---|---|---|---|
|  |  |  |  |  | open |

## QA / 测试策略摘要

_从 `reviews/qa-review.md` 汇总。引用 `requirements/validation.md`，说明自动化测试、手工 QA、回归范围和关键验收路径。_

| 场景 | 验收标准 | 测试方式 | 证据位置 | 状态 |
|---|---|---|---|---|
|  |  |  |  | planned |

## 追踪关系更新

_记录重要需求在本评审中被接受、调整、延期或拒绝的情况。必要时更新 `requirements/traceability.md`。_

| 需求 | 评审结论 | 影响 | traceability 更新状态 |
|---|---|---|---|
|  | accepted / changed / deferred / rejected |  | pending |

## 需要人工决策的问题

每个需要人工选择的问题都必须写成 decision brief。不要只给推荐项写理由；所有选项都必须可读、可比较。

| 问题 | 选项 | 适用场景 | 优点 | 缺点 / 代价 | 对后续阶段影响 | 推荐 |
|---|---|---|---|---|---|---|
| TBD | 选项 A |  |  |  |  | ✅ /  |
| TBD | 选项 B |  |  |  |  |  |
| TBD | 选项 C |  |  |  |  |  |

## 审批决策

- 状态：TBD
- 审批人：
- 决策说明：

## 完成检查清单

- [ ] `reviews/product-review.md` 已完成，并有明确产品结论
- [ ] `reviews/engineering-review.md` 已完成，并有明确工程推荐方案
- [ ] `reviews/security-risk-review.md` 已完成，并有权限/审计/数据风险结论
- [ ] `reviews/qa-review.md` 已完成，并有核心验收路径和证据要求
- [ ] 产品评审摘要已完成，本轮交付范围明确
- [ ] 不做什么已记录
- [ ] 工程方案足够具体，可进入实现计划
- [ ] 数据模型、状态流转、API / 集成已记录
- [ ] 若存在 API 边界，`requirements/api.yaml` 已经 review/修订/冻结为 04 的实现合同
- [ ] 安全、权限、审计或合规风险已检查
- [ ] QA / 测试策略覆盖核心验收标准
- [ ] 对需求的任何变更已反映到需求产物或追踪说明中
- [ ] 需要人工决策的问题已记录
