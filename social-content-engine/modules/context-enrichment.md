# Context Enrichment

Context enrichment fills useful gaps without inventing a persona.

## Priority order

Use information in this order:

1. current user request
2. current conversation
3. explicit saved preferences or persona
4. user-supplied URL/file/image/source
5. current research
6. platform defaults

Higher-priority information wins.

## Safe inferences

Usually safe:

- default platform format
- default length range
- likely broad audience category
- neutral tone
- information density
- research need
- language based on explicit request or current conversation
- whether a hook is important
- whether a CTA is optional
- whether hashtags are low-value

Mark uncertain inferences with internal confidence. Do not clutter the visible result with confidence labels.

## Do not infer

Never fabricate:

- personal experience
- attendance at an event
- product ownership or usage
- job title or employer
- professional credentials
- financial positions
- political identity
- private relationships
- first-hand knowledge
- demographic identity
- “I tested this for months” style claims

A user saying “我的心得” permits first-person framing around supplied experience, but it does not permit invented duration, results, or statistics.

## Sparse prompt workflow

For a prompt such as:

> Apple 折叠屏，写个 X

Enrich internally to something like:

- topic: Apple foldable device
- platform: X
- likely audience: consumer tech / Apple / product audience
- content goal: topical commentary
- tone: informed, conversational
- angle: missing
- current context: missing
- freshness: high
- research: required

Then research and discover an angle before writing.

## User goal inference

Prefer functional goals:

- inform
- explain
- react
- teach
- persuade
- promote
- start discussion
- summarize
- share experience

Avoid over-interpreting emotional or ideological intent.

## Platform defaults

Use platform defaults as a floor, not a template. A LinkedIn post can be short; a Reddit post can be concise; an X post can be technical. The topic and audience still matter.

## Language and locale

When the user writes in one language but asks for another output language, preserve the underlying meaning and tone rather than translating surface syntax.

If the user provides a bilingual brand vocabulary, glossary, or preferred spellings, preserve them.

For Vietnamese, Chinese, Japanese, Korean, or mixed-language prompts, consult `references/multilingual.md`.

## When to ask

Prefer a concise question only when the missing choice creates materially different outputs.

Example:

> “帮我回复这个人”

If the referenced message is unavailable, ask for it.

Do not ask:

> “你的目标受众是谁？你的语气是什么？你的 CTA 是什么？”

when reasonable defaults are available.
