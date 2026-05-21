# 工作流状态 — {{FEATURE_NAME}}

- 功能：{{FEATURE_NAME}}
- 工作流目录：`{{WORKFLOW_DIR}}`
- 来源 PRD：`{{SOURCE_PRD}}`
- 当前阶段：{{CURRENT_PHASE}}
- 检查点状态：{{CHECKPOINT_STATUS}}
- 最后更新：{{CREATED_AT}}

## 契约原则

AI Dev Workflow 拥有阶段契约、状态、门禁和 artifact 位置。`requirements-analyst`、gstack-style review、`superpowers` 等能力提供者负责方法和详细产出，但不能替代 workflow contract。

## 阶段

| 阶段 | Artifact | 状态 | Provider |
|---|---|---|---|
| 00 输入整理 | `00_INTAKE.md` | {{PHASE_00_STATUS}} | ai-dev-workflow |
| 01 需求工程 | `01_REQUIREMENTS.md` + `requirements/` | {{PHASE_01_STATUS}} | requirements-analyst |
| 02 产品与工程评审 | `02_TECHNICAL_DESIGN.md` | {{PHASE_02_STATUS}} | gstack-style review |
| 03 原型 | `03_PROTOTYPE.md` + `prototype/` | {{PHASE_03_STATUS}} | requirements-driven prototype generation |
| 04 实现 | `04_IMPLEMENTATION.md` | {{PHASE_04_STATUS}} | superpowers |
| 05 验证与评审 | `05_REVIEW.md` | {{PHASE_05_STATUS}} | superpowers + optional gstack |

## 详细产物

### 需求

- `requirements/discovery.md`
- `requirements/sort.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/clarification.md`
- `requirements/validation.md`
- `requirements/prd.md`
- `requirements/open-questions.md`
- `requirements/traceability.md`

## 决策

- 暂无。

## 开放问题

- [ ] 确认是否继续进入 01 需求工程。

## 下一步

{{NEXT_ACTION}}
