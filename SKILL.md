---
name: run
description: Orchestrate a lightweight, artifact-driven AI development workflow from PRD/intake through requirements analysis, product/engineering review, static prototype generation, implementation planning, build, and verification. Use when the user wants to run requirements-analyst, review-pack or optional external garrytan/gstack review, and superpowers together in a controlled workflow, create .ai-workflow artifacts, generate a requirements-driven prototype, or test an AI development process on a PRD.
---

# AI Dev Workflow

运行一套可控、以 artifact 为核心的 AI 研发工作流。

这个 skill 是一个 **orchestrated workflow package**：它不替代 `requirements-analyst`、外部 `garrytan/gstack` 或 `superpowers` 的能力；内置 `review-pack` 只是紧凑评审 provider，不等同完整 gstack。workflow 负责阶段状态机、provider routing、产物位置、强制 gate、失败修复循环和人工门禁。

开始或恢复工作前先读取 `references/orchestration.md`。不要只靠本文件正文记忆阶段规则。


## Language and user-visible output

Auto-detect the primary language from the user's request and source PRD. Use that language for **all** user-visible replies and generated artifact content unless the user explicitly asks otherwise.

For Chinese PRDs or Chinese user instructions:

- final phase summaries must be in Chinese;
- checkpoint / clarification questions must be in Chinese;
- artifact headings, labels, table headers, status notes, and handoff prompts must be in Chinese;
- do not switch to English just because provider skills, templates, filenames, or examples are English;
- English technical identifiers such as file paths, API operation IDs, enum values, and command names may remain English.

Before replying to the user at a phase boundary, check the reply language. If it does not match the user's language, rewrite it before sending.

## 核心规则

**阶段之间只通过文件交接。**

不要把聊天记录当成唯一事实来源。每个阶段的重要输入、输出、决策、开放问题和下一步，都必须写入 `.ai-workflow/<feature-slug>/` 里的 artifact。能力提供者可以替换，但 workflow artifact contract 保持稳定。

**workflow 自己负责流程纪律。** 用户提示词很短不代表可以自创流程或自动跑到底。除非用户明确要求 unattended / continuous / guided-auto，默认人工门禁必须生效。即使用户只给 PRD 路径，也必须使用本 skill 的标准 artifact、状态机和 gate；不得用 `02_REVIEW.md`、`02_STATUS.md`、`04_PLAN.md` 等临时文件替代标准阶段 artifact。

Provider skills 只是能力提供者：`requirements-analyst` 不能改写 01 的 artifact contract，`gstack` 不能改写 02 的 artifact contract，`superpowers` 不能改写 04/05 的 artifact contract。所有 provider-native 产出必须映射回 workflow 指定位置。

硬停点：01 如果存在阻塞澄清问题，必须先问用户；03 原型完成后必须等用户确认；04 implementation plan 通过后必须等用户批准，才能写 backend/frontend 实现代码。

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
│   ├── api.yaml                # required when API boundary exists
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
6. 将 `STATUS.md` 设置为 phase `01_REQUIREMENTS`。
7. 默认模式：checkpoint 设为 `WAITING_FOR_HUMAN_CONFIRMATION`，暂停并询问用户是否继续运行 `01 Requirements`。
8. `guided-auto` / continuous 模式：不要在 00 后做“是否继续”的确认门禁；checkpoint 设为 `AUTO_CONTINUE_TO_01` 或等价状态，并立即进入 01 的需求澄清/问答环节。如果有阻塞开放问题，直接提出 decision brief；如果没有阻塞问题，直接运行 01 Requirements。

除非用户明确要求 unattended / continuous / guided-auto run，否则不要在初始化后自动进入需求分析。即使用户要求连续推进，每个阶段边界仍然必须更新 `STATUS.md`。

## 阶段路由

| Phase | 目标 | 主要能力 | 默认工具 / skill |
|---|---|---|---|
| 00 Intake | 捕获原始请求、上下文和约束 | Intake normalization | This orchestrator |
| 01 Requirements | 生成需求阶段摘要，并保留详细 requirements artifacts | Requirements analysis | `requirements-analyst` |
| 02 Product & Engineering Review | 挑战范围，形成产品 / 工程设计 | Product / architecture review | `gstack-adapter` over external `garrytan/gstack`; `review-pack` degraded fallback |
| 03 Prototype | 生成需求驱动的静态原型 | Prototype planning + static HTML/CSS generation | `requirements-analyst` prototype approach |
| 04 Implementation | 编写实现计划并纪律化执行 | TDD execution | `superpowers`: writing-plans, subagent-driven-development or executing-plans |
| 05 Verification & Review | 用证据证明结果可用 | Verification / review / QA | `superpowers` verification + optional `gstack-adapter` over external `garrytan/gstack`; `review-pack` degraded fallback |

决策使用哪个能力时，读取：

- `references/orchestration.md`
- `references/phase-routing.md`
- `references/capability-contracts.md`
- `references/artifact-spec.md`

相对路径都以本 skill 目录为根目录解析。

## Provider availability preflight

进入任何依赖外部能力的阶段前，必须先确认首选 provider 是否可用，并把结果写入 `STATUS.md` 的 Provider health / 阶段状态。

规则：

- 01 首选 `requirements-analyst`；02 首选真实外部 `garrytan/gstack` via `gstack-adapter`；04/05 首选 superpowers。
- 先运行或等价执行 `scripts/check_providers.py`，将结果写入 `STATUS.md` Provider health。
- 如果首选 provider 可用，使用它，并保留 provider-native 深度产物。
- 如果首选 provider 不可用，先判断 bundled provider 的 fidelity tier：
  - `providers/requirements-analyst/SKILL.md`：应作为 `BUNDLED_SOURCE_SLICE` 使用，必须加载其真实 steering/templates 才能算发挥该子能力。
  - `providers/gstack-adapter/SKILL.md`：仅当真实外部 `garrytan/gstack` 安装且对应 slice 实际运行时才是 `ADAPTER_FULL`。
  - `providers/review-pack/SKILL.md`：当前是 `COMPACT_FALLBACK`，不等同完整 `garrytan/gstack`；不能把它的输出当成 gstack full capability。
  - `providers/superpowers-adapter/SKILL.md`：优先作为 `ADAPTER_FULL` 映射外部 superpowers；外部 superpowers 不可用时只是 fallback/degraded。
- 如果既没有首选 provider，也没有足够 fidelity 的 bundled provider，不能只在正文里随口说明后继续；必须暂停提示用户安装/启用 provider，或明确请求用户接受降级。
- fallback/adapter mode 仍必须满足 workflow artifact contract；如果达不到同等深度，不得把阶段标记为 DONE，只能标记为 `DONE_DEGRADED` / `NEEDS_REVIEW` / `BLOCKED`。
- `STATUS.md` 中的 Provider 列必须反映真实执行者，例如 `ai-dev-workflow fallback (requirements-analyst unavailable)`，不得继续写首选 provider 造成误导。
- 如果用户要求 guided-auto，provider 不可用属于需要确认的运行条件；除非 fallback policy 已明确允许，否则应暂停询问。

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

### Guided-auto clarification protocol

如果用户要求 `guided-auto` / 连续推进模式，agent 应自动越过普通“是否继续下一阶段”的门禁；但遇到需要人确认的开放问题时，必须主动提问，而不是把问题只写进 artifact 后继续推进。00 Intake 完成后不得要求用户先确认“是否进入 01”；应直接进入 01 的问答澄清或需求分析。

提问规则：

- 将相关开放问题合并成一组 decision brief，避免一问一答打断过多。
- 每个问题必须给出**动态生成**的可选项；选项数量按问题复杂度决定，不固定为 2/3/4 个。
- 每个问题必须包含一个自由表达选项，例如“其他 / 自定义：请直接描述你的规则或偏好”。
- 对每个选项说明适用场景、优点、代价/风险和对后续阶段的影响。
- 可以给推荐项，但必须说明推荐理由；不得把推荐项当成人工确认。
- 用户回复后，必须把选择和自由文本写入 `requirements/clarification.md`、`requirements/open-questions.md`、`STATUS.md`，并在需要时同步 `requirements/traceability.md`。
- 如果用户一次性回答多个问题，按回答继续；如果只回答部分问题，只追问仍阻塞下一阶段的问题。

当需要用户选择方案时，必须生成 decision brief，而不是只列选项。每个选项都必须有说明：适用场景、优点、缺点/代价、对后续阶段的影响。推荐项可以额外写推荐理由，但非推荐项不能留空或显示 `No preview available`。

## Quality gates

质量门禁必须通过 `scripts/orchestrate.py gate <workflow-dir> <phase>` 或等价 validator 命令记录。不要只在回复里说“已通过”。

推荐流程：

```bash
python3 <skill-root>/scripts/orchestrate.py mark-running <workflow-dir> 01
python3 <skill-root>/scripts/orchestrate.py gate <workflow-dir> 01
```

如果 gate 失败，按 `references/orchestration.md` 的 forced gate loop 修复并重跑；最多 3 次后停止并标记具体 `NEEDS_*` / `BLOCKED_*` 状态。

进入下一阶段前检查：

- 必需 artifact 已存在。
- artifact 中没有未处理的 `TBD`，除非已列入 Open Questions。
- 关键 decisions 已记录在 `STATUS.md`。
- 本阶段 consumed inputs 和 produced outputs 已写清楚。
- 下一阶段有明确 handoff prompt。
- `01_REQUIREMENTS.md` 只做摘要、索引和门禁；详细需求产物应保存在 `requirements/`，不要被压扁进单一文件。
- `requirements/requirements.md` 必须是 provider-native 的完整需求分析文档，质量应接近直接运行 `requirements-analyst` 的输出；如果它只有几张简表，不得把 01 阶段标记为 DONE。
- `02_TECHNICAL_DESIGN.md` 只做摘要、决策和门禁；review-pack 多角色深度评审应保存在 `reviews/product-review.md`、`reviews/engineering-review.md`、`reviews/security-risk-review.md`、`reviews/qa-review.md`，不要被压扁进单一文件。
- 进入 implementation 前，prototype 已被批准，或明确记录为 skipped。
- 如果生成了 prototype，页面必须能直接打开，并且页面到 requirements / user stories 的映射完整。
- 01/02/03 要求 full-fidelity，不只看 provider availability。01 完成前必须通过 `--gate 01-full`；02 完成前必须通过 `--gate 02-full`；03 进入 04 前必须通过 `--gate 03-full`。如果 gate 失败，不能宣称“满血 requirements-analyst / gstack / prototype”，应标记 `NEEDS_*_DEPTH` 或 `DONE_DEGRADED`。
- 01 不能把 `clarification.md` / `open-questions.md` 当装饰文件。凡是 `open-questions.md` 仍有待确认/待定/needs human decision 的阻塞问题，或者 `clarification.md` 记录了“采用/默认/建议/推荐”的决策但没有明确用户/人工确认来源，`01-full` 必须失败并停在需求澄清，不能进入 02。
- 02 不只是写 review summary。gstack 评审后必须回填 `requirements/traceability.md` 主矩阵的设计列，把核心/MUST需求映射到具体模块、API、状态流转、权限/安全控制和评审决策；只追加“评审决策追溯”小节但主矩阵仍是 `TBD` 不算通过。
- 不得自我批准 prototype。`03-full` 可以证明原型产物完整，但如果状态仍写着 `awaiting human approval`、`待确认`、`待人工确认` 等，必须停在 03 等用户确认，不能把“用户已批准原型”勾上后进入 04。
- 04 进入执行前必须通过 `scripts/validate_artifacts.py <workflow-dir> --gate 04-plan`，然后停下来等待用户明确批准执行；guided-auto、inline execution、Claude/agent 自批都不算批准。04 进入 05 前必须通过 `--gate 04-complete`。如果代码已改但 04 artifact 仍是模板、空表或 `TBD`，或缺少明确人工执行批准，标记 `BLOCKED_ARTIFACT_DRIFT`，不要继续。
- 05 完成前必须通过 `scripts/validate_artifacts.py <workflow-dir> --gate 05-complete`。如果证据缺失或命令失败未处理，发布建议必须是 `Blocked`，不能输出 Ready / 全流程通过。

基础结构检查：

```bash
scripts/validate_artifacts.py <workflow-dir>
```

prototype 生成后使用：

```bash
scripts/validate_artifacts.py <workflow-dir> --require-prototype-files
```

04/05 阶段完成门禁：

```bash
scripts/validate_artifacts.py <workflow-dir> --gate 01-full
scripts/validate_artifacts.py <workflow-dir> --gate 02-full
scripts/validate_artifacts.py <workflow-dir> --gate 03-full
scripts/validate_artifacts.py <workflow-dir> --gate 04-plan
scripts/validate_artifacts.py <workflow-dir> --gate 04-complete
scripts/validate_artifacts.py <workflow-dir> --gate 05-complete
```

## Output style

用户可见汇报必须使用用户的主要语言；中文 PRD / 中文指令场景下，阶段完成摘要、阻塞问题和下一步都必须用中文输出。

汇报要简洁，默认包括：

- 创建 / 更新了哪些文件
- 当前 phase
- blockers 或 open decisions
- 用户可以批准的明确 next action

不要把大量中间推理塞进回复；把可恢复上下文写进 artifact。
