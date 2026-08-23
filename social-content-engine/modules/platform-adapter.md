# Platform Adapter

Convert a universal content brief into destination-platform writing requirements. Do not invent facts or a new personal stance.

Read the relevant platform profile in `references/platforms.md`.

## Preserve

- core thesis
- verified facts
- claim confidence
- user intent
- explicit tone
- explicit language/locale
- must-include / must-avoid rules

## Adapt

- length
- pacing
- paragraph shape
- opening behavior
- information density
- evidence budget
- CTA behavior
- hashtags
- title/headline usage
- spoken vs written rhythm
- community norms

## Platform-native test

Ask:

> If the platform name were hidden, would the structure still feel like it belongs there?

If the answer is “this looks like a LinkedIn post pasted into Reddit,” adapt again.

## Unknown platform fallback

When the requested platform has no built-in profile:

1. infer from the user’s requested format
2. use a concise generic social profile
3. avoid undocumented claims about character limits or algorithms
4. preserve readable paragraphs
5. use one clear thesis
6. make CTA optional
7. omit hashtags unless requested

## Multilingual adaptation

Platform conventions and language conventions interact.

Examples:

- Chinese Xiaohongshu may tolerate different title/caption structures than English Instagram.
- Vietnamese Facebook copy should sound locally conversational rather than translated from English corporate copy.
- Japanese business LinkedIn copy may require more restrained assertion than an English X post.
- Reddit communities may prefer English even when the user asks questions in another language; follow the user’s requested destination language.

Always follow explicit user instructions over profile defaults.

## Output brief

Return internally:

- platform
- format
- target language / locale
- recommended length
- information density
- structure
- hook behavior
- evidence budget
- tone adjustments
- CTA behavior
- formatting rules
- platform-specific avoid list
