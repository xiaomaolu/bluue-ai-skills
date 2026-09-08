# Bluue AI Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

Bluue 创建的开源 AI Agent Skills。

## Skills

### social-content-engine

一个面向 AI Agent 的多语言、跨平台社媒内容引擎。以一个 Skill Bundle 安装，内部完成任务路由、短上下文补全、实时研究、内容角度发现、平台适配、写作、跨平台改写、Hook 优化、风格学习与最终质检。

核心能力：

- 用户只提供几个词时，会先补充必要上下文，再生成内容
- 仅在主题具有时效性或事实需要验证时触发搜索，减少无意义 Research
- 支持 X、LinkedIn、Instagram、Threads、Reddit、Facebook、TikTok/抖音、YouTube、小红书、微博、Telegram/Discord，并提供未知平台的通用适配层
- 重点适配英语、简体中文、繁体中文、越南语、日语、韩语，同时可使用模型支持的其他语言
- 跨语言场景优先重新创作表达，不默认逐句直译
- 区分官方事实、已确认信息、媒体报道、传闻、分析、观点和社区信号
- 避免虚构第一人称经历、职业身份、投资持仓和使用体验
- 使用内容角度评分、平台原生化适配、有限重试和 Review Quality Gate
- 内置多语言 AI 套话检查与测试用例

示例：

```text
使用 $social-content-engine 写一条关于 Apple 折叠屏的 X。
```

```text
使用 $social-content-engine 写一篇 LinkedIn，面向金融机构合规团队，解释 AI governance 为什么正在从政策走向运营控制。
```

```text
使用 $social-content-engine 把这篇英文 LinkedIn 改写成自然的越南语 Facebook 内容，不要逐句翻译。
```

完整架构见 [`social-content-engine/README.md`](./social-content-engine/README.md)。

### bluue-minimal-doodle

将人物、作品、概念、事件、地点、物体、产品和品牌转化为极简涂鸦插画。它是一个 Skill，内含一种默认风格和一个可选风格分支。

支持：

- 通过可用的图像生成工具直接生成图片
- 仅输出提示词
- 人物、作品、概念、事件、地点、物体、产品和品牌等主题
- 默认黑白粗糙文学草图风格
- 可选粗线扁平风格，并严格控制为一种强调色
- 参考图和多个独立变体
- 自动视觉质检与针对性重新生成

#### 风格变体

只需安装 `bluue-minimal-doodle`。两种风格属于同一个 Skill 内部的变体。

| 用户想要的效果 | 风格 |
|---|---|
| 黑白文学草图、粗糙马克笔线条、大量留白 | `rough-literary` |
| 平滑粗轮廓、扁平黑色块、更大的主体、一种强调色 | `bold-flat-accent` |
| 没有指定风格 | `rough-literary` |

视觉示例：

| `rough-literary` — 默认 | `bold-flat-accent` — 可选 |
|---|---|
| <img src="./assets/examples/rough-literary-prediction-market.png" alt="rough-literary 风格的预测市场插画" width="480"> | <img src="./assets/examples/bold-flat-accent-bike-sharing.png" alt="bold-flat-accent 风格的共享单车插画" width="480"> |

### bluue-infographic-series

将长篇内容、研究报告、结构化笔记、概念、流程和数据转译为单张高质量信息图，或一组风格统一的系列信息图。

核心能力：

- 用户提供了长篇内容时，默认保留原文语言；没有明确源语言时使用英文
- 默认尺寸为 9:16，用户可以覆盖为其他比例
- 自动判断内容更适合数据、科普、总结、流程或一般信息图结构
- 长内容优先拆成多张，避免一张图塞入过多信息
- 同一系列锁定一套主视觉，允许每张使用不同构图，避免模板重复
- 可以克制地使用图形、形状、Icon、图表、照片、拼贴、纹理和插画元素
- 支持简约、暗黑数据、杂志、拼贴、包豪斯、复古、装饰艺术、朋克、酸性、日式、粗野主义、现代奢华等多种风格方向
- 系列主色调保持克制，避免无意义的多色堆叠
- 把文字准确度作为交付门槛，尤其关注名称、日期、数字、单位、法律与技术术语、多语言内容
- 当纯生图难以保证关键文字准确时，优先使用 HTML / SVG / Canvas 等确定性排版方案

示例：

```text
使用 $bluue-infographic-series 把这篇研究报告整理成 5 张 9:16 系列信息图。保留原文语言，使用统一的杂志编辑风格，每张只讲一个重点。
```

### bluue-ui-design

一个基于 Bluue 克制型界面偏好的产品 UI 设计、实现、修改与审查 Skill。

它会帮助 Agent：

- 保留现有产品系统、真实内容和用户授权范围
- 优先处理对齐、可读的信息密度与清晰层级
- 按主级、二级和三级功能组织连续任务流，避免把所有能力堆在一个界面
- 减少重复描述文案与框套框结构
- 避免默认蓝紫色、无依据渐变、统一大圆角与大间距、模板化首屏、假文案、等权卡片网格和阴影堆砌等 AI/SaaS 模板特征
- 将这些模式作为按场景判断的设计偏好，而不是机械禁令，并保留有意建立的品牌系统与权威参考
- 实现真实交互，并在渲染后的桌面端与移动端中验证结果
- 每个可测试版本完成后，简要总结颜色、排版、布局与风格

适用于 Figma 或截图还原、视觉优化、内容替换、本地化、响应式 UI 与产品界面质检。

## 安装

克隆仓库：

```bash
git clone https://github.com/xiaomaolu/bluue-ai-skills.git
```

将需要的 Skill 复制到 Codex Skills 目录。

### PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\social-content-engine" -Destination "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-minimal-doodle" -Destination "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-infographic-series" -Destination "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-ui-design" -Destination "$env:USERPROFILE\.codex\skills\"
```

### macOS / Linux

```bash
cp -R ./bluue-ai-skills/social-content-engine ~/.codex/skills/
cp -R ./bluue-ai-skills/bluue-minimal-doodle ~/.codex/skills/
cp -R ./bluue-ai-skills/bluue-infographic-series ~/.codex/skills/
cp -R ./bluue-ai-skills/bluue-ui-design ~/.codex/skills/
```

## 许可证

MIT