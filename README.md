# Bluue AI Skills

[**English**](./README.md) | [简体中文](./README.zh-CN.md)

Open-source AI agent skills created by Bluue.

## Skills

### social-content-engine

A multilingual, cross-platform social-content engine for AI agents. It is installed as one skill bundle and internally handles routing, sparse-context enrichment, research, angle discovery, platform adaptation, writing, repurposing, hooks, style learning, and final quality review.

Highlights:

- works with sparse prompts instead of immediately producing generic copy
- researches current topics only when freshness or factual precision requires it
- supports X, LinkedIn, Instagram, Threads, Reddit, Facebook, TikTok/Douyin, YouTube, Xiaohongshu, Weibo, Telegram/Discord, plus a generic platform fallback
- supports English, Simplified/Traditional Chinese, Vietnamese, Japanese, Korean, and other model-supported languages
- transcreates across languages instead of defaulting to literal translation
- separates facts, reports, rumors, opinions, and community signals
- avoids invented first-person experience and fake authority
- uses angle scoring, platform-native adaptation, bounded retries, and a review quality gate
- includes multilingual anti-slop rules and evaluation cases

Examples:

```text
Use $social-content-engine to write an X post about Apple's foldable iPhone.
```

```text
使用 $social-content-engine 写一篇 LinkedIn，面向金融机构合规团队，解释 AI governance 为什么正在从政策走向运营控制。
```

```text
Use $social-content-engine to turn this English LinkedIn post into natural Vietnamese Facebook copy. Do not translate literally.
```

See [`social-content-engine/README.md`](./social-content-engine/README.md) for architecture and supported workflows.

### bluue-minimal-doodle

Turns people, works, concepts, events, places, objects, products, and brands into minimalist doodle illustrations. It ships as one skill with one default style and one optional style branch.

It supports:

- direct image generation through an available image-generation tool
- prompt-only output
- people, works, concepts, events, places, objects, products, and brands
- a default black-and-white rough literary style
- an optional bold flat style with exactly one controlled accent color
- optional reference images and independent variants
- automatic visual QA and focused regeneration

#### Style variants

Install only `bluue-minimal-doodle`. The two styles are internal variants of the same skill.

| What the user wants | Style |
|---|---|
| Black-and-white literary sketch, rough marker lines, lots of empty space | `rough-literary` |
| Thick smooth outlines, flat black shapes, larger characters or objects, one accent color | `bold-flat-accent` |
| No style specified | `rough-literary` |

Visual examples:

| `rough-literary` — default | `bold-flat-accent` — optional |
|---|---|
| <img src="./assets/examples/rough-literary-prediction-market.png" alt="Prediction market in the rough-literary style" width="480"> | <img src="./assets/examples/bold-flat-accent-bike-sharing.png" alt="Bike sharing in the bold-flat-accent style" width="480"> |

### bluue-ui-design

A product UI design, implementation, revision, and audit skill built around Bluue's restrained interface preferences.

It helps agents:

- preserve the existing product system, real content, and authorized scope
- prioritize alignment, readable density, and clear information hierarchy
- organize primary, secondary, and tertiary functions into coherent task flows instead of crowding one surface
- reduce redundant explanatory copy and frame-within-frame composition
- use icons purposefully, keep colors restrained, and avoid unnecessary shadows or gradients
- build real interactions and verify desktop and mobile results in the rendered interface
- report a concise color, typography, layout, and style summary after each reviewable version

Use it for Figma or screenshot implementation, visual refinement, content replacement, localization, responsive UI, and product-interface QA.

## Install

Clone the repository:

```bash
git clone https://github.com/xiaomaolu/bluue-ai-skills.git
```

Copy the skill you want into your Codex skills directory.

### PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\social-content-engine" -Destination "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-minimal-doodle" -Destination "$env:USERPROFILE\.codex\skills\"
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-ui-design" -Destination "$env:USERPROFILE\.codex\skills\"
```

### macOS / Linux

```bash
cp -R ./bluue-ai-skills/social-content-engine ~/.codex/skills/
cp -R ./bluue-ai-skills/bluue-minimal-doodle ~/.codex/skills/
cp -R ./bluue-ai-skills/bluue-ui-design ~/.codex/skills/
```

## License

MIT
