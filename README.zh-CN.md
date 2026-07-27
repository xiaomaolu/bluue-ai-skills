# Bluue AI Skills

[English](./README.md) | [**简体中文**](./README.zh-CN.md)

Bluue 创建的开源 AI Agent Skills。

## Skills

### bluue-minimal-doodle

将人物、作品、概念、事件、地点、物体、产品和品牌转化为极简涂鸦插画。它是一个 Skill，内含一种默认风格和一个可选风格分支。

支持：

- 通过可用的图像生成工具直接生成图片
- 仅输出提示词
- 人物、作品、概念、事件、地点、物体、产品和品牌等主题
- 默认的黑白粗糙文学草图风格
- 可选的粗线扁平风格，并严格控制为一种强调色
- 参考图和多个独立变体
- 自动视觉质检与针对性重新生成

## 风格变体

只需安装 `bluue-minimal-doodle`。两种风格是同一个 Skill 内部的变体，不是两个独立 Skill。

### 视觉对比

| `rough-literary` — 默认 | `bold-flat-accent` — 可选 |
|---|---|
| <img src="./assets/examples/rough-literary-prediction-market.png" alt="rough-literary 风格的预测市场插画" width="480"> | <img src="./assets/examples/bold-flat-accent-bike-sharing.png" alt="bold-flat-accent 风格的共享单车插画" width="480"> |
| 粗糙黑色马克笔线条、大量留白、纯黑白、少量象征元素。 | 平滑粗轮廓、明确的纯黑色块、更大的动作主体，以及一种受控的强调色。 |

### 应该选择哪种风格？

| 用户想要的效果 | 风格 |
|---|---|
| 黑白文学草图、粗糙马克笔线条、大量留白 | `rough-literary` |
| 平滑粗轮廓、扁平黑色块、更大的人物或物体、一种强调色 | `bold-flat-accent` |
| 没有指定风格 | `rough-literary` |
| 只说“加一点颜色”或“使用品牌色” | 应明确选择风格；仅指定颜色不会自动切换分支 |

Skill 不会在每次请求时都询问风格。除非需求在视觉上存在歧义，否则会直接使用默认风格。当颜色要求可能显著改变画面表现时，可使用这段简短提示：

```text
这个 Skill 有两种风格：rough-literary 是默认的黑白文学草图；bold-flat-accent 使用平滑粗轮廓和一种强调色。你想用哪一种？如果不指定，我将使用 rough-literary。
```

用户也可以使用自然语言别名：

- “black-and-white literary sketch”或“黑白文学草图” → `rough-literary`
- “bold flat single-accent style”或“粗线单色扁平风格” → `bold-flat-accent`

### rough-literary

这是默认风格。如果用户没有选择风格，Skill 会生成一幅稀疏、黑白、粗糙马克笔质感的文学涂鸦，并保留大量留白。

```text
使用 $bluue-minimal-doodle 为“预测市场”生成一幅插画。
```

也可以显式指定同样的风格：

```text
使用 $bluue-minimal-doodle，style_variant=rough-literary，为“莎士比亚”生成插画。
```

### bold-flat-accent

这个可选分支使用平滑粗黑轮廓、明确的纯黑色块、更大的主体，以及零种或一种受控的强调色。

```text
使用 $bluue-minimal-doodle，style_variant=bold-flat-accent，为“共享单车”生成插画。暖橙色作为唯一强调色，占画面不超过 15%。
```

品牌色示例：

```text
使用 $bluue-minimal-doodle，style_variant=bold-flat-accent，为 Lululemon 生成插画。accent_policy=brand，只使用一种强调色，不要 Logo 和文字。
```

仅指定颜色不会启用可选分支。如果需要完整的粗线扁平视觉表现，请显式选择 `bold-flat-accent`。

## 安装

克隆仓库：

```bash
git clone https://github.com/xiaomaolu/bluue-ai-skills.git
```

将 Skill 复制到 Codex Skills 目录。

PowerShell：

```powershell
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-minimal-doodle" -Destination "$env:USERPROFILE\.codex\skills\"
```

macOS 或 Linux：

```bash
cp -R ./bluue-ai-skills/bluue-minimal-doodle ~/.codex/skills/
```

使用示例：

```text
使用 $bluue-minimal-doodle 为“预测市场”生成一幅极简涂鸦插画。
```

## 许可证

MIT
