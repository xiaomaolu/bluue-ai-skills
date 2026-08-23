# Social Content Engine

A multilingual, cross-platform social-content skill bundle for AI agents.

It is installed as **one discoverable skill** (`social-content-engine`) and uses internal modules for routing, context enrichment, research, angle discovery, platform adaptation, writing, review, repurposing, hooks, and style learning.

## Why this structure

A user may provide only:

> Apple foldable, write an X post.

The engine should not immediately produce generic copy. It can:

1. detect sparse context
2. determine freshness
3. research current information
4. find a specific angle
5. adapt it to X
6. write in the requested language
7. review factual and language quality

For a detailed brief, the pipeline becomes shorter and preserves the user’s decisions.

## Languages

The engine is language-agnostic and includes stronger locale rules for:

- English
- Simplified Chinese
- Traditional Chinese
- Vietnamese
- Japanese
- Korean

It supports bilingual and cross-language repurposing when requested.

## Platforms

Built-in profiles:

- X / Twitter
- LinkedIn
- Instagram
- Threads
- Reddit
- Facebook
- TikTok
- Douyin
- Instagram Reels
- YouTube Shorts
- YouTube long-form
- Xiaohongshu / RED
- Weibo
- Telegram / Discord
- generic fallback for unknown platforms

## Internal modules

- `modules/router.md`
- `modules/context-enrichment.md`
- `modules/research.md`
- `modules/angle-discovery.md`
- `modules/platform-adapter.md`
- `modules/writer.md`
- `modules/review.md`
- `modules/hook-optimizer.md`
- `modules/repurpose.md`
- `modules/style-profile.md`

## Key references

- `references/state-schema.md`
- `references/multilingual.md`
- `references/platforms.md`
- `references/source-policy.md`
- `references/anti-slop.md`
- `references/error-codes.md`
- `references/test-cases.md`

## Example prompts

```text
Use $social-content-engine to write an X post about Apple's foldable iPhone.
```

```text
使用 $social-content-engine 写一篇 LinkedIn，面向金融机构合规团队，解释 AI governance 为什么正在从政策走向运营控制。
```

```text
Use $social-content-engine to turn this English LinkedIn post into natural Vietnamese Facebook copy. Do not translate literally.
```

```text
使用 $social-content-engine 把这段内容改成 Reddit 帖子，更像真实参与者，少一点品牌感。
```

## Design principles

- sparse prompt → more internal enrichment
- rich prompt → less inference
- current topic → research first
- one useful angle beats many generic options
- platform-native beats one universal template
- transcreation beats literal translation
- explicit user choices beat defaults
- no invented personal experience
- review routes problems back to the correct module
- bounded retries prevent agent loops
