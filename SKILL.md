---
name: ai-dev-workflow
description: Orchestrate a lightweight, artifact-driven AI development workflow from PRD/intake through requirements analysis, product/engineering review, static prototype generation, implementation planning, build, and verification. Use when the user wants to run requirements-analyst, gstack, and superpowers together in a controlled workflow, create .ai-workflow artifacts, generate a requirements-driven prototype, or test an AI development process on a PRD.
---

# AI Dev Workflow

运行一套轻量、可控、以 artifact 为核心的 AI 研发工作流。

这个 skill 是一个编排器：它不替代 `requirements-analyst`、`gstack` 或 `superpowers` 的能力，而是负责阶段路由、产物管理、上下文交接和人工门禁。

## 核心规则

**阶段之间只通过文件交接。**

不要把聊天记录当成唯一事实来源。每个阶段的重要输入、输出、决策、开放问题和下一步，都必须写入 `.ai-workflow/<feature-slug>/` 里的 artifact。能力提供者可以替换，但 workflow artifact contract 保持稳定。

默认工作目录：

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── requirements/
│   ├── reverse.md              # optional
│   ├── discovery.md
│   ├── sort.md
│   ├── requirements.md
│   ├── datamodel.md
│   ├── clarification.md
│   ├── validation.md
│   ├── prd.md
│   ├── api.yaml                # optional
│   ├── open-questions.md
│   └── traceability.md
├── 02_TECHNICAL_DESIGN.md
├── 03_PROTOTYPE.md
├── prototype/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── pages/
├── 04_IMPLEMENTATION.md
├── 05_REVIEW.md
└── STATUS.md
```

## 何时使用

当用户提供 PRD、原始需求、功能想法，或想验证一套 AI 辅助研发流程时使用。

适合的场景：

- 把 PRD 拆成可执行、可验证的研发阶段。
- 先做 requirements analysis，再做 product / engineering review。
- 先生成静态 prototype 验证页面、流程、角色和状态，再进入 implementation。
- 让后续 agent 只靠 artifact 接手，不依赖隐藏聊天上下文。
- 比较 artifact-first workflow 和裸聊天实现的效果差异。

不适合的场景：

- 用户只想快速问答，不需要持久化 artifact。
- 用户明确要求直接改一个很小的 bug，不需要完整流程。
- 项目没有 PRD / 需求上下文，且用户也不想补充 intake。

## 启动工作流

开始一个新 feature workflow 时，先完成 **00 Intake**，不要直接写需求分析、技术设计或实现计划。

必须使用 workflow 定义的 artifact contract：

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── requirements/
├── 02_TECHNICAL_DESIGN.md
├── 03_PROTOTYPE.md
├── 04_IMPLEMENTATION.md
├── 05_REVIEW.md
└── STATUS.md
```

推荐直接运行初始化脚本：

```bash
python3 <skill-root>/scripts/init_workflow.py \
  --project-root <project-root> \
  --source-prd <source-prd> \
  --feature <feature-name>
```

如果不能运行脚本，才手动从 `<skill-root>/assets/templates/` 复制模板；手动创建时也必须保持上述文件名和目录结构。

启动步骤：

1. 识别 source PRD 或 intake text。
2. 从产品 / 功能名称生成 `feature-slug`。
3. 初始化 `.ai-workflow/<feature-slug>/` 下的标准 artifact。
4. 只填写 `00_INTAKE.md` 和必要的 `STATUS.md` 初始化状态。
5. 在 `00_INTAKE.md` 中保留原始 PRD 路径/来源、摘要、已知约束、初始假设和开放问题。
6. 将 `STATUS.md` 设置为 phase `01_REQUIREMENTS`，checkpoint `WAITING_FOR_HUMAN_CONFIRMATION`。
7. 暂停并询问用户是否继续运行 `01 Requirements`。

除非用户明确要求 unattended / continuous run，否则不要在初始化后自动进入需求分析。即使用户要求连续推进，每个阶段边界仍然必须更新 `STATUS.md`。

## 阶段路由

| Phase | 目标 | 主要能力 | 默认工具 / skill |
|---|---|---|---|
| 00 Intake | 捕获原始请求、上下文和约束 | Intake normalization | This orchestrator |
| 01 Requirements | 生成需求阶段摘要，并保留详细 requirements artifacts | Requirements analysis | `requirements-analyst` |
| 02 Product & Engineering Review | 挑战范围，形成产品 / 工程设计 | Product / architecture review | `gstack` concepts: office-hours, plan-ceo-review, plan-eng-review |
| 03 Prototype | 生成需求驱动的静态原型 | Prototype planning + static HTML/CSS generation | `requirements-analyst` prototype approach |
| 04 Implementation | 编写实现计划并纪律化执行 | TDD execution | `superpowers`: writing-plans, subagent-driven-development or executing-plans |
| 05 Verification & Review | 用证据证明结果可用 | Verification / review / QA | `superpowers` verification + optional `gstack` review/qa |

决策使用哪个能力时，读取：

- `references/phase-routing.md`
- `references/capability-contracts.md`
- `references/artifact-spec.md`

相对路径都以本 skill 目录为根目录解析。

## Prototype rules

默认 Prototype 是 **Level 1 static prototype**。

### Level 1：默认原型

- 只使用静态 HTML + CSS。
- 直接用浏览器打开 `prototype/index.html`，不需要 server。
- 不使用 JavaScript。
- 不使用 CDN。
- 不接 backend / API。
- 不使用 build tools。
- 不使用 CSS frameworks。
- 先写 `Prototype Plan`，再逐页生成。
- `prototype/index.html` 是导航入口和页面地图。
- 其他 HTML 页面统一放在 `prototype/pages/`。
- 每个页面都必须映射到 requirements / user stories。

### Level 2：可选交互原型

只有在用户明确批准时，才允许升级到 Level 2。

Level 2 也只能使用少量 vanilla JavaScript 来模拟关键交互，不允许演变成生产级前端实现。

### 原型边界

Prototype 是 **decision artifact**，不是 shadow product。

原型阶段应该验证：

- 页面结构
- 用户路径
- 信息优先级
- 关键状态
- 角色 / 权限差异
- 主要异常、空状态和边界情况

原型阶段不应该实现：

- 真实后端 API 调用
- 完整业务逻辑
- 完整权限系统
- 完整状态管理
- 生产级组件封装
- 像素级视觉还原
- 可上线代码结构

如果某个能力主要服务“上线运行”，默认不进入 prototype 核心。
如果某个能力主要服务“产品 / 交互 / 工程决策”，才允许进入 prototype。

所有 mock data、假交互、不可用按钮和未覆盖能力，都必须在 `03_PROTOTYPE.md` 或页面中明确标注。

## Human gates

除非用户明确要求 unattended run，否则每个阶段结束后都要暂停并等待确认：

- 00 之后：确认 normalized intake。
- 01 之后：确认 requirements 和 unresolved questions。
- 02 之后：确认 design decisions 和 prototype scope。
- 03 之后：确认 prototype approval 或修改意见。
- 04 planning 之后：确认是否执行实现。
- 05 之后：确认 accept / rework / retro。

不要静默替用户做产品、安全、合规、集成、商业取舍等需要人工确认的决策。

当需要用户选择方案时，必须生成 decision brief，而不是只列选项。每个选项都必须有说明：适用场景、优点、缺点/代价、对后续阶段的影响。推荐项可以额外写推荐理由，但非推荐项不能留空或显示 `No preview available`。

## Quality gates

进入下一阶段前检查：

- 必需 artifact 已存在。
- artifact 中没有未处理的 `TBD`，除非已列入 Open Questions。
- 关键 decisions 已记录在 `STATUS.md`。
- 本阶段 consumed inputs 和 produced outputs 已写清楚。
- 下一阶段有明确 handoff prompt。
- `01_REQUIREMENTS.md` 只做摘要、索引和门禁；详细需求产物应保存在 `requirements/`，不要被压扁进单一文件。
- `requirements/requirements.md` 必须是 provider-native 的完整需求分析文档，质量应接近直接运行 `requirements-analyst` 的输出；如果它只有几张简表，不得把 01 阶段标记为 DONE。
- `02_TECHNICAL_DESIGN.md` 只做摘要、决策和门禁；gstack-style 多角色深度评审应保存在 `reviews/product-review.md`、`reviews/engineering-review.md`、`reviews/security-risk-review.md`、`reviews/qa-review.md`，不要被压扁进单一文件。
- 进入 implementation 前，prototype 已被批准，或明确记录为 skipped。
- 如果生成了 prototype，页面必须能直接打开，并且页面到 requirements / user stories 的映射完整。

基础结构检查：

```bash
scripts/validate_artifacts.py <workflow-dir>
```

prototype 生成后使用：

```bash
scripts/validate_artifacts.py <workflow-dir> --require-prototype-files
```

## Output style

汇报要简洁，默认包括：

- 创建 / 更新了哪些文件
- 当前 phase
- blockers 或 open decisions
- 用户可以批准的明确 next action

不要把大量中间推理塞进回复；把可恢复上下文写进 artifact。
