# Router

The router turns a raw social-content request into a compact execution plan. It does not write the final post.

## 1. Resolve the request

Extract only what is actually present or safely implied:

- `task`
- `topic`
- `platform`
- `format`
- `audience`
- `user_angle`
- `language`
- `locale`
- `tone`
- `source_material`
- `length`
- `must_include`
- `must_avoid`

Normalize platform aliases:

- `twitter`, `tweet` → `x`
- `ig`, `ins` → `instagram`
- `red`, `小红书` → `xiaohongshu`
- `抖音` → `douyin`
- `shorts` → `youtube_shorts` when YouTube is implied

Do not collapse different products merely because their formats are similar. TikTok, Douyin, Reels, YouTube Shorts, and Xiaohongshu have overlapping short-form patterns but different audience conventions.

## 2. Classify the task

Choose one primary task:

- `create`
- `rewrite`
- `optimize`
- `reply`
- `commentary`
- `repurpose`
- `summarize`
- `educate`
- `promote`
- `brainstorm`
- `thread`
- `script`

Examples:

- “写一条关于 Apple 折叠屏的 X” → `create`
- “把这篇 LinkedIn 改成 X” → `repurpose`
- “这句开头更有钩子” → `optimize`
- “回复这个 Reddit 评论” → `reply`
- “把这份报告转成三条社媒内容” → `summarize` + `create`

## 3. Context score

Score 0–10:

- topic clear: +1
- platform clear: +2
- audience clear: +2
- angle/opinion clear: +2
- facts/source material supplied: +1
- tone clear: +1
- format/length clear: +1

Interpretation:

- 0–3: sparse
- 4–6: partial
- 7–8: strong
- 9–10: execution-ready

A low score means more internal enrichment may be useful. It does not automatically mean “ask the user.”

## 4. Freshness score

- 0: evergreen
- 1: mildly time-sensitive
- 2: current entity/product/company/topic
- 3: recent event/news/market/release/regulation

Strong freshness cues include:

- latest / recent / today / this week / new
- launch / announced / release / market / price
- 最新 / 最近 / 今天 / 发布 / 上线 / 市场 / 价格 / 政策
- mới nhất / gần đây / hôm nay / ra mắt
- 最新 / 発表 / 本日
- 최신 / 발표 / 오늘

Freshness >= 2 normally triggers research unless the user supplied sufficient current evidence.

## 5. Research intent

If research is required, record one or more purposes:

- `fact_verification`
- `latest_development`
- `supporting_evidence`
- `statistics`
- `competitive_context`
- `public_discussion`
- `source_discovery`

Do not search broadly without a purpose.

## 6. Language resolution

Delegate final language selection to `references/multilingual.md`.

The router should record:

- `input_language`
- `requested_output_language`
- `locale` when explicit
- `source_language`
- `code_switch_allowed`
- `bilingual_requested`

Do not output two languages merely because the input contains two languages.

## 7. Ask-or-execute rule

Ask only when all three are true:

1. the missing choice materially changes the deliverable,
2. there is no safe default,
3. the user cannot reasonably correct the choice after seeing a result.

Examples worth asking:

- user says “post this” but no source content is available
- platform identity is essential and cannot be inferred
- requested voice depends on an unknown real-person identity

Examples to infer:

- default X length
- likely tech audience for an Apple hardware topic
- neutral informed tone
- no hashtags

## 8. Build the execution plan

Typical sparse current-topic request:

`context-enrichment → research → angle-discovery → platform-adapter → writer → review`

Detailed current-topic request with angle:

`research → platform-adapter → writer → review`

Evergreen rewrite:

`platform-adapter if needed → writer → review`

Repurpose:

`platform-adapter → repurpose → review`

Hook-only:

`hook-optimizer → review`

Return an internal plan and update state. Do not expose it unless requested.
