# 01 需求工程 — {{FEATURE_NAME}}

## 目的

将输入/PRD 规格化为可信的详细需求产物，供后续产品评审、工程设计、原型、实现和验证阶段使用。

本文件是 01 阶段的 workflow 级摘要和控制 artifact。它不替代 `requirements-analyst` 的原生详细产物，而是负责索引这些产物、记录决策，并定义阶段交接契约。

## 输入

- `00_INTAKE.md`
- 来源 PRD：`{{SOURCE_PRD}}`

## 能力提供者契约

默认 provider：`requirements-analyst`。

使用 `requirements-analyst` 作为分析方法，而不是让它成为竞争性的 workflow owner。保留它在 `requirements/` 下产出的丰富详细文档，然后在本文件中总结并链接。

如果 provider-native artifacts 更有用，不要把所有需求分析强行压缩进这个摘要文件。

## 需求子流程

默认参考 `requirements-analyst` 的需求工程阶段：

```text
Reverse（可选：从现有代码提取需求）
→ Discovery（发现/收集）
→ Sort（价值排序）
→ Analysis（分析为故事、用例、数据模型）
→ Clarification（澄清歧义）
→ Validation（质量验证）
→ Specification（正式规格/PRD）
```

## 预期详细产物

在 01 阶段创建或更新这些文件：

```text
requirements/
├── reverse.md              # 可选，用于存量代码反向需求分析
├── discovery.md
├── sort.md
├── requirements.md
├── datamodel.md
├── clarification.md
├── validation.md
├── prd.md
├── api.yaml                # API 边界存在时必需；无 API 时必须写明 not-applicable
├── open-questions.md
└── traceability.md
```

最低要求：

| Artifact | 用途 | 状态 |
|---|---|---|
| `requirements/reverse.md` | 可选：当缺少可靠文档时，从现有代码反向提取需求 | 可选 |
| `requirements/discovery.md` | 原始目标、相关方、约束和成功标准 | 计划中 |
| `requirements/sort.md` | 价值排序、优先级、本轮交付适配和依赖说明 | 计划中 |
| `requirements/requirements.md` | 完整 provider-native 需求分析：用户画像、活动流、故事地图、详细用户故事、验收条件、INVEST/质量检查、功能/非功能需求、角色权限、边界情况 | 计划中 |
| `requirements/datamodel.md` | 领域实体、关系、关键字段、生命周期状态、权限相关数据 | 计划中 |
| `requirements/clarification.md` | 歧义、假设、相关方决策和已澄清问题 | 计划中 |
| `requirements/validation.md` | 验收标准、验证规则、可测试场景、边界情况和质量检查 | 计划中 |
| `requirements/prd.md` | 验证后的正式 PRD / 规格说明 | 计划中 |
| `requirements/api.yaml` | OpenAPI / API contract。若存在前后端、client/server、服务间或外部 HTTP 边界则必需；若无 API 边界，必须保留文件并写明 `x-api-scope: not-applicable` 与原因 | 条件必需 |
| `requirements/open-questions.md` | 需要人工确认的歧义和决策 | 计划中 |
| `requirements/traceability.md` | 从 PRD 到需求、原型页面、实现任务和验证证据的映射 | 计划中 |

如果额外 provider-native 文件能提升交接质量，也允许放在 `requirements/` 下；请在这里链接并说明原因。

## 摘要

_在详细需求产物生成后填写。_

## 关键决策和假设

_在需求分析过程中填写。请明确标注假设；不确定且需要人工判断的内容应移动到开放问题。_

## 开放问题摘要

详见 `requirements/open-questions.md`。

- [ ] TBD

## 交接给产品与工程评审

下游阶段必须阅读本文件和 `requirements/` 下的详细产物，不要只依赖本摘要。

02 阶段必读输入：

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
- `requirements/api.yaml`（API 边界存在时必读；无 API 时读取 not-applicable 说明）
- 来源 PRD：`{{SOURCE_PRD}}`

## 审批决策

- 状态：TBD
- 审批人：
- 决策说明：

## 完成检查清单

- [ ] `requirements/` 下已生成详细需求产物
- [ ] `requirements/requirements.md` 达到直接运行 `requirements-analyst` 时的原生分析深度，而不是摘要表
- [ ] 需求明确且可测试
- [ ] 领域实体和生命周期状态已记录
- [ ] 验证规则和验收标准已记录
- [ ] 若存在 API 边界，`requirements/api.yaml` 已列出 method/path/auth/request/response/owner/traceability/status；若不存在，已明确 not-applicable
- [ ] 开放问题被记录，而不是被猜测
- [ ] 已开始建立到来源 PRD 的追踪关系
- [ ] 进入产品与工程评审前，需求已获得人工确认
