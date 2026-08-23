---
name: social-content-engine
description: Create, rewrite, optimize, research, repurpose, reply to, and review multilingual social content across X/Twitter, LinkedIn, Instagram, Threads, Reddit, Facebook, TikTok/Douyin, YouTube, Xiaohongshu, Weibo, Telegram/Discord, and unfamiliar platforms through a generic fallback. Use for social posts, threads, captions, short-video scripts, comments, replies, content angles, cross-platform adaptation, and sparse prompts that need context enrichment. Research current topics when freshness matters, preserve explicit user choices, avoid invented personal experience, and return platform-native writing in the requested language or locale.
---

# Social Content Engine

Turn a social-content request into a publishable result through a compact internal pipeline. Treat this directory as one installable skill bundle with modular internal capabilities. The user should not need to know or invoke the modules separately.

The central rule is:

> The less context the user supplies, the more useful internal work the skill should perform before writing. A short prompt is never a reason to produce generic filler.

## Defaults

Unless the user overrides them:

- Task: infer from the request
- Output count: one strongest result
- Output language: resolve with [references/multilingual.md](references/multilingual.md)
- Platform: infer only when explicit or strongly implied; otherwise use the generic adapter
- Research: only when freshness, factual precision, or requested evidence requires it
- Angle: select one specific angle internally; do not dump many near-duplicates
- Tone: natural, specific, restrained, platform-native
- Personal experience: never invent
- Hashtags: omit unless useful for the destination platform or requested
- CTA: optional; never force one
- Review cycles: maximum 2
- Research retry: maximum 1
- Angle retry: maximum 1
- Writer retry: maximum 2

## Supported tasks

Normalize the primary task to one of:

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

Secondary intents may coexist, such as `create + promote` or `repurpose + translate`.

## Supported platforms

Read [references/platforms.md](references/platforms.md) when a platform-specific result is requested.

Built-in profiles include:

- X / Twitter
- LinkedIn
- Instagram
- Threads
- Reddit
- Facebook
- TikTok / Douyin / Reels
- YouTube Shorts / long-form
- Xiaohongshu / RED
- Weibo
- Telegram / Discord
- Generic / unknown social platform

If the requested platform is missing, use the generic profile and infer only observable format requirements. Do not pretend to know undocumented platform conventions.

## Workflow

### 1. Route the request

Read [modules/router.md](modules/router.md).

Resolve:

- task
- topic
- platform
- format
- audience
- user angle
- language / locale
- tone
- supplied facts or sources
- must-include items
- must-avoid items
- context score
- freshness score
- whether research is required

Create or update the shared state described in [references/state-schema.md](references/state-schema.md).

### 2. Enrich sparse context when useful

Read [modules/context-enrichment.md](modules/context-enrichment.md) when the context score is low or a meaningful field is missing.

Infer safe defaults. Do not manufacture identity, first-hand experience, credentials, ownership, investment positions, or strong beliefs.

Ask a question only when the unresolved choice would materially change the result and cannot be safely inferred. Prefer execution over questionnaires.

### 3. Research only when needed

Read [modules/research.md](modules/research.md) and [references/source-policy.md](references/source-policy.md) when:

- freshness score is 2 or 3
- the user asks for latest/current/news/data/sources
- factual precision materially affects the post
- the angle depends on a recent event, product, company, market, regulation, public figure, statistic, or social discussion

Use available search/retrieval tools. The skill is provider-agnostic. Tavily, Exa, Brave, official APIs, native web search, Reddit search, X APIs, or other available tools may be used according to their strengths.

Do not run research for a pure rewrite, shortening request, tone edit, or evergreen creative task unless facts need verification.

### 4. Discover a useful angle

Read [modules/angle-discovery.md](modules/angle-discovery.md) when the user has not supplied a strong thesis or when the current angle is generic.

Prefer an angle that is:

- specific to this subject
- supported by evidence
- useful to the audience
- native to the platform
- difficult to reuse unchanged for an unrelated topic

### 5. Adapt to the platform

Read [modules/platform-adapter.md](modules/platform-adapter.md) and the relevant section of [references/platforms.md](references/platforms.md).

Preserve the thesis and facts. Adapt structure, density, pacing, tone, formatting, CTA behavior, and evidence budget.

### 6. Write

Read [modules/writer.md](modules/writer.md).

The writer should use the prepared brief instead of restarting strategy. Keep one main thesis per short post unless the requested format requires more.

### 7. Review

Read [modules/review.md](modules/review.md), [references/anti-slop.md](references/anti-slop.md), and [references/error-codes.md](references/error-codes.md).

Approve, lightly revise, or route the draft back to the correct module. Never enter an unlimited rewrite loop.

### 8. Return the result

Default visible output:

- one publishable result
- sources only when they materially help, are requested, or claims require attribution
- no internal scores, routing JSON, or hidden workflow unless the user asks

When uncertainty is meaningful, state it naturally in the content or a concise note.

## Fast paths

### Pure rewrite / tone / shortening

Use:

`router → platform-adapter if needed → writer → review`

Skip research and angle discovery when the source content already contains the needed facts and thesis.

### Cross-platform repurpose

Read [modules/repurpose.md](modules/repurpose.md).

Use:

`router → platform-adapter → repurpose → review`

Reuse validated facts and thesis. Do not simply shorten or reformat the source.

### Hook-only optimization

Read [modules/hook-optimizer.md](modules/hook-optimizer.md).

Trigger when:

- the user explicitly asks for a hook/opening
- review returns `WEAK_HOOK`

Generate up to three internally distinct hooks and expose only the best one unless the user requests options.

### Style learning

Read [modules/style-profile.md](modules/style-profile.md) when explicit user edits, preferences, or repeated corrections are available.

Learn abstract style rules, not copied phrases. Never infer sensitive attributes.

## Multilingual behavior

Always read [references/multilingual.md](references/multilingual.md) when:

- input and output languages differ
- the user asks for bilingual or multilingual output
- the content uses code-switching
- research sources are in another language
- the destination market has locale-specific conventions
- the target language is Chinese, Vietnamese, Japanese, Korean, or another language where literal English structures often sound unnatural

Do not translate a finished English draft sentence by sentence unless the user explicitly asks for literal translation. Prefer transcreation from the underlying brief and angle.

## State ownership

Each module owns a limited part of the shared state:

| Module | Primary fields it may modify |
|---|---|
| Router | `request`, routing fields, `context.score`, `freshness` |
| Context enrichment | `context`, `audience`, safe defaults |
| Research | `research` |
| Angle discovery | `strategy` |
| Platform adapter | `platform` |
| Writer / repurpose / hook | `draft` |
| Review | `review`; may return a corrected draft only for light revisions |
| Style profile | `style_profile` |

Do not silently overwrite explicit user decisions from another module.

## Safety and factual integrity

- Attribute reports, rumors, forecasts, and community claims correctly.
- Distinguish official facts from reports and opinions.
- Never create fake citations, fake quotes, fake metrics, fake user experiences, or fake social proof.
- Do not present incomplete social-web search as a complete archive.
- For regulated, financial, legal, health, political, or brand-sensitive topics, prefer the `precision` writing mode and stronger sources.
- Treat social posts as evidence of what a person or community said, not proof that the underlying claim is true.

## Output quality

Every final piece should normally contain at least one of:

- concrete information
- a specific observation
- a meaningful implication
- a useful comparison
- a defensible opinion
- a clear user benefit

Generic enthusiasm alone is insufficient.

## Internal test suite

Use [references/test-cases.md](references/test-cases.md) when modifying the skill. The suite covers sparse prompts, multiple languages, current topics, repurposing, Reddit voice, product content, and platform fallback.
