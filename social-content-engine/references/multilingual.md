# Multilingual and Locale Policy

The engine should work in any language supported by the underlying model. These rules give stronger defaults for English, Simplified Chinese, Traditional Chinese, Vietnamese, Japanese, and Korean while preserving a generic fallback for other languages.

## 1. Resolve output language

Use this priority:

1. explicit requested output language
2. explicit destination locale
3. explicit instruction to preserve source language
4. established language of the current content task
5. current user language
6. source-material language
7. platform default only when the platform clearly implies one

Do not automatically return bilingual content because the prompt is bilingual.

Return bilingual/multilingual output only when requested or clearly required by the product workflow.

## 2. Record language separately from locale

Examples:

- `zh-CN`
- `zh-TW`
- `en-US`
- `en-GB`
- `vi-VN`
- `ja-JP`
- `ko-KR`

Locale affects:

- punctuation
- spelling
- date format
- currency
- units
- formality
- terminology

## 3. Transcreate, do not mechanically translate

For social writing:

`brief + angle + evidence → target-language draft`

is preferred over:

`English draft → sentence-by-sentence translation`

Literal translation often preserves the wrong rhythm, connectors, joke structure, and CTA style.

## 4. Proper nouns and terminology

Preserve conventional names:

- brands
- products
- tickers
- handles
- protocol names
- technical abbreviations

Use the locally established translation when one clearly exists.

Do not create a new translation for a brand or product.

## 5. Research across languages

Search query language should follow source likelihood.

### Global topic
Use English plus the most relevant local language when useful.

### Local regulation / local company / local event
Search the local language first. Add English only for international context or official English versions.

### Social sentiment
Search the language actually used by the target community.

Do not merge distinct local conversations into one “global sentiment” claim.

## 6. Code-switching

Use code-switching only when:

- the user does it deliberately
- the audience naturally uses those terms
- technical/product vocabulary is more natural untranslated

Avoid decorative English inserted into otherwise natural Chinese/Vietnamese/Japanese/Korean copy.

## 7. Language-specific notes

### English

Prefer:

- plain verbs
- compact claims
- natural contractions when tone permits
- fewer corporate abstractions

Avoid overusing:

- “landscape”
- “leverage”
- “game-changing”
- “redefine”
- “in today’s world”

### Simplified Chinese (`zh-CN`)

Prefer:

- direct topic entry
- concrete nouns
- shorter connectors
- natural Chinese sentence order
- platform-specific internet language only when appropriate

Avoid imported English structures such as:

- “对于 X 而言，关键在于……”
- excessive “与此同时 / 值得注意的是 / 从某种意义上说”
- headline-like abstraction in every sentence
- translating “This is less about A and more about B” mechanically

Use Chinese punctuation.

### Traditional Chinese (`zh-TW` / `zh-HK`)

Use locally appropriate vocabulary where the locale is known. Do not blindly convert Simplified Chinese characters while preserving Mainland-specific wording.

### Vietnamese (`vi-VN`)

Prefer:

- natural conversational Vietnamese
- locally normal pronouns only when audience relationship is clear
- concise sentence flow for social content
- English technical/product terms when they are commonly used

Avoid:

- overly formal translated bureaucratic phrasing
- literal English noun stacks
- forced pronouns when relationship is unknown

### Japanese (`ja-JP`)

Prefer:

- appropriate restraint
- natural Japanese information order
- formality matched to platform
- fewer aggressive English-style claims unless the user wants that voice

Avoid literal translations of English rhetorical hooks.

### Korean (`ko-KR`)

Prefer:

- natural Korean sentence endings
- platform-appropriate formality
- concise claims
- conventional English product/technical terms when common

Avoid translated English corporate filler.

## 8. Cross-language repurpose

When changing both language and platform:

1. extract thesis
2. preserve evidence
3. adapt platform
4. adapt locale
5. write fresh in target language
6. run native-language review

## 9. Bilingual output

When requested:

- avoid duplicating labels on every sentence
- preserve equivalent meaning, not identical syntax
- keep platform limits in mind
- if one language is primary, present it first
- do not mix two languages inside one post unless requested

## 10. Numbers, dates, currency, and units

Preserve exact values from sources.

Adapt presentation only when safe:

- `US$` vs `$`
- `RMB` / `人民币` / `¥` where unambiguous
- date order by locale
- decimal/thousands separators

Never silently convert currency without an explicit exchange rate.
