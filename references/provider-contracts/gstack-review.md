# gstack Review Contract

`gstack` 在本 workflow 中不是独立流程 owner，而是 02 / 05 阶段的多角色评审能力提供者。

## 适用阶段

- 02 产品与工程评审：在需求完成后，挑战范围、架构、风险和测试策略。
- 05 验证与评审：在实现完成后，做发布前风险复查、QA 复查和代码/架构复查。

## 输入

02 阶段必须读取：

- `01_REQUIREMENTS.md`
- `requirements/` 下全部详细需求产物
- 来源 PRD
- 现有代码结构 / 技术约束（如存在）

05 阶段必须读取：

- 实现 diff
- `04_IMPLEMENTATION.md`
- `05_REVIEW.md` 当前内容
- `02_TECHNICAL_DESIGN.md`
- `03_PROTOTYPE.md`
- `requirements/` 下详细需求产物

## 子能力

| 子能力 | 用途 | 主要输出位置 |
|---|---|---|
| Product review | 检查范围、用户价值、非目标、首批交付边界 | `02_TECHNICAL_DESIGN.md` |
| Engineering review | 检查架构、数据模型、状态流转、接口、迁移、可维护性 | `02_TECHNICAL_DESIGN.md` |
| Security / risk review | 检查权限、数据安全、审计、滥用场景、合规风险 | `02_TECHNICAL_DESIGN.md` / `05_REVIEW.md` |
| QA review | 检查验收场景、边界情况、手工 QA 路径和回归风险 | `02_TECHNICAL_DESIGN.md` / `05_REVIEW.md` |
| Release review | 检查上线/交付风险、回滚、监控、文档和剩余风险 | `05_REVIEW.md` |

## 02 阶段输出要求

必须在 `02_TECHNICAL_DESIGN.md` 中形成：

- 推荐本轮交付范围。
- 明确不做什么。
- 产品评审结论。
- 工程评审结论。
- 安全/风险评审结论。
- QA / 测试策略。
- 架构、数据模型、状态流转、API / 集成设计。
- 风险登记表：风险、影响、概率、缓解方式、负责人、状态。
- 需要人工决策的问题。

如果重要需求被接受、调整、延期或拒绝，必须更新 `requirements/traceability.md`，或在 `02_TECHNICAL_DESIGN.md` 中明确标记待更新。

## 05 阶段输出要求

必须在 `05_REVIEW.md` 中形成：

- 需求覆盖复查。
- 代码/架构复查发现。
- 安全/风险复查发现。
- QA 复查结果。
- 测试/build/lint/手工 QA 证据。
- 发布就绪度：Ready / Ready with accepted risks / Blocked。
- 剩余风险处理：fixed / accepted / deferred / blocked。

## 失败条件

出现以下任一情况，不应进入下一阶段：

- 范围仍然不清楚，无法形成实现计划。
- 关键权限、审计、数据安全或状态流转问题未决。
- 需求变更没有写回 traceability 或开放问题。
- 测试策略无法覆盖核心验收标准。
- 发布前存在 blocking 风险但未记录负责人和处理方式。

## 使用提示

调用 gstack-style review 时，明确要求它作为 reviewer，而不是重写 workflow artifact 格式。它可以输出分角色意见，但最终必须合并进 workflow 指定文件。
