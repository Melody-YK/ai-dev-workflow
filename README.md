# AI Dev Workflow

AI Dev Workflow 是一个轻量、可控、以阶段产物交接为核心的 AI 研发工作流编排器。

它把一个 PRD 或原始需求，拆成一条清晰的研发链路：

```text
PRD → Requirements → Product & Engineering Review → Implementation → Verification
```

这套流程的重点不是“让 AI 一口气自动做完所有事”，而是让每个阶段都有明确输入、明确输出、人工确认点和可验证证据。

## 为什么需要它

直接让 AI 根据 PRD 写代码，很容易出现几个问题：

- 需求还没澄清就开始实现
- PRD 里重要内容被漏掉
- AI 自己扩大或缩小范围
- 中途换 agent 后无法接手
- 最后只说“完成了”，但没有测试证据
- 过程都埋在聊天记录里，难复盘、难版本管理

AI Dev Workflow 试图解决这些问题：

```text
用固定 artifact 文件承载上下文，
用阶段门禁控制节奏，
用评估标准验证流程是否真的有效。
```

## 核心原则

- **产物优先**：阶段输出必须写入文件，而不是只留在聊天记录里。
- **人工门禁**：关键阶段默认暂停，等待人确认后再继续。
- **能力编排**：按能力组织流程，而不是绑定某个固定工具。
- **可替换 skill**：`requirements-analyst`、gstack-style review、`superpowers` 是默认选择，但不是硬依赖。
- **先小后大**：第一版只做最小可用流程，不急着引入复杂状态机。

## 默认工作流

```text
00 Intake
01 Requirements
02 Product & Engineering Review
03 Implementation Planning & Build
04 Verification & Review
```

默认生成的工作目录：

```text
.ai-workflow/<feature-slug>/
├── 00_INTAKE.md
├── 01_REQUIREMENTS.md
├── 02_TECHNICAL_DESIGN.md
├── 03_IMPLEMENTATION.md
├── 04_REVIEW.md
└── STATUS.md
```

这些文件就是不同阶段、不同 agent、不同 skill 之间的交接接口。

## 阶段分工

| 阶段 | 目的 | 默认能力 |
|---|---|---|
| 00 Intake | 收集原始需求，初始化工作流产物 | `ai-dev-workflow` |
| 01 Requirements | 把 PRD 转成明确、可测试的需求规格 | `requirements-analyst` |
| 02 Product & Engineering Review | 审范围、定 MVP、审架构、识别风险 | gstack-style review |
| 03 Implementation | 写实现计划，按 TDD 或验证优先方式实现 | `superpowers` |
| 04 Verification & Review | 用测试、构建、评审和 QA 证明确实完成 | `superpowers` + 可选 gstack QA/review |

## 快速开始

用一个 PRD 初始化工作流：

```bash
python3 scripts/init_workflow.py \
  --project-root "/path/to/project" \
  --source-prd "/path/to/project/PRD.md" \
  --feature "feature-name"
```

示例：

```bash
python3 scripts/init_workflow.py \
  --project-root "/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test" \
  --source-prd "/Users/melody/Desktop/tbd和superpowers/interview-requirements-power-test/PRD.md" \
  --feature "operation-ticket-management"
```

校验 artifact 是否完整：

```bash
python3 scripts/validate_artifacts.py "/path/to/project/.ai-workflow/<feature-slug>"
```

查看当前状态：

```bash
python3 scripts/status.py "/path/to/project/.ai-workflow/<feature-slug>"
```

## 推荐使用方式

第一版建议一阶段一阶段跑，不建议一上来无人值守自动跑完。

推荐节奏：

```text
初始化 00 Intake
→ 人确认
→ 跑 01 Requirements
→ 人确认
→ 跑 02 Product & Engineering Review
→ 人确认
→ 跑 03 Implementation Planning
→ 人确认是否执行
→ 跑 04 Verification & Review
→ 根据 EVALUATION.md 评分复盘
```

这样可以清楚观察每个阶段到底有没有提升质量。

## 如何判断它是否有效

不要只看生成了多少文档，而要看它是否做到：

1. 需求比原 PRD 更清楚、更可测试。
2. 设计阶段能主动收敛范围，而不是照单全收。
3. 新 agent 只看 `.ai-workflow/<feature>/` 就能接手。
4. 实现计划具体到文件、命令、测试和预期结果。
5. 最终完成有测试 / build / lint / QA 证据。
6. 相比裸聊天，返工更少、状态更清楚、交付更稳。

详细评分标准见：

```text
EVALUATION.md
```

## 仓库结构

```text
ai-dev-workflow/
├── SKILL.md
├── README.md
├── USAGE.md
├── EVALUATION.md
├── references/
│   ├── workflow-overview.md
│   ├── capability-contracts.md
│   ├── phase-routing.md
│   └── artifact-spec.md
├── assets/templates/
└── scripts/
```

## 当前状态

这是一个早期 MVP，目标是先通过真实 PRD 跑完整链路，验证这套 artifact-first、human-gated、capability-based 的 AI 研发流程是否真的比裸聊天更稳定。

## License

MIT
