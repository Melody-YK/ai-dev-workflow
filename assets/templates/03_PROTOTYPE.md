# 03 原型 — {{FEATURE_NAME}}

## 目的

在正式实现前，创建需求驱动的静态原型，用于验证用户流程、页面结构、角色、权限和核心体验。

## 输入

- `01_REQUIREMENTS.md`
- `requirements/requirements.md`
- `requirements/datamodel.md`
- `requirements/validation.md`
- `02_TECHNICAL_DESIGN.md`
- 来源 PRD：`{{SOURCE_PRD}}`

## 输入消费证据

_本阶段必须明确说明需求、设计和评审结论如何影响原型页面。不能只列文件名。_

| 输入 artifact | 已消费内容 | 对 03 原型的影响 | 证据位置 |
|---|---|---|---|
| `requirements/requirements.md` |  |  |  |
| `requirements/clarification.md` / `open-questions.md` |  |  |  |
| `02_TECHNICAL_DESIGN.md` / `reviews/` |  |  |  |

## 原型级别

默认：Level 1 静态原型。

- Level 1：仅 HTML + CSS，通过链接进行页面跳转，不使用 JavaScript。
- Level 2：可选交互原型，仅在用户明确批准时使用少量 vanilla JavaScript。

## 原型约束

默认遵循 `requirements-analyst` 的原型方法：

- 纯静态文件。
- 可直接在浏览器打开 `prototype/index.html`。
- 只使用相对链接。
- 只使用本地 CSS。
- 不使用 CDN。
- 不接后端。
- 不使用构建工具。
- 不使用 CSS 框架。
- 除非明确批准 Level 2，否则不使用 JavaScript。

## 原型边界

Prototype 是决策产物，不是 shadow product。

原型应该验证页面结构、用户路径、信息优先级、关键状态、角色/权限差异、空/错状态和核心 UX 决策。

原型不应该实现真实后端调用、完整业务逻辑、完整权限系统、完整状态管理、生产级组件封装、像素级视觉还原或可上线代码结构。

## 原型计划

_生成页面前先填写。_

| # | 页面 | 来源需求 / 流程 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | `index.html` | 导航入口 | 原型入口和页面地图 | 计划中 |

## 页面到需求映射

_在原型计划/生成过程中填写。必要时更新 `requirements/traceability.md`。_

| 页面 | 需求 / 用户故事 | 覆盖流程 | 备注 |
|---|---|---|---|
|  |  |  |  |

## 生成文件

预期结构：

```text
prototype/
├── index.html
├── css/
│   └── style.css
└── pages/
    └── <flow-page>.html
```

## Mock 数据

_生成过程中填写。_

## 原型范围外

_生成前填写。_

## 评审反馈

_相关方/用户评审后填写。_

## 审批决策

- 状态：TBD
- 审批人：
- 决策说明：

## 完成检查清单

- [ ] 生成页面前已评审原型计划
- [ ] `prototype/index.html` 已存在
- [ ] `prototype/css/style.css` 已存在
- [ ] 非 index 页面都位于 `prototype/pages/`
- [ ] 页面使用可信 mock 数据
- [ ] 页面能映射回需求 / 用户故事
- [ ] mock 数据、假交互、不可用按钮和未覆盖能力已显式标注
- [ ] 原型无需 server/build step 即可打开
- [ ] 进入实现计划前，用户已批准原型
