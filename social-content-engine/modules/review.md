# Review

Review acts as a quality gate. Fluent generic writing should not pass merely because it sounds polished.

## Score: 100

- insight: 20
- specificity: 15
- evidence / claim discipline: 15
- human voice: 15
- platform-native fit: 15
- hook: 10
- conciseness: 5
- originality: 5

Also run a target-language naturalness check. Language quality affects `human voice` and `platform-native fit`.

## Thresholds

- 85–100: approve
- 75–84: light revision
- 60–74: rewrite
- below 60: route to angle discovery or research

## Routing errors

Use `references/error-codes.md`.

Common routes:

- `GENERIC_ANGLE` → angle discovery
- `LOW_SPECIFICITY` → angle discovery or writer
- `WEAK_HOOK` → hook optimizer or writer
- `UNSUPPORTED_CLAIM` → research
- `AI_SLOP` → writer
- `PLATFORM_MISMATCH` → platform adapter + writer
- `TRANSLATIONESE` → writer with multilingual rules
- `FAKE_PERSONAL_CONTEXT` → remove immediately
- `TOO_LONG` → writer
- `SOURCE_MISMATCH` → research

## Tests

### Information test
Does the content teach, reveal, compare, or argue something concrete?

### Replaceability test
Could the topic name be replaced with an unrelated company/product while most of the post still works?

If yes, specificity is low.

### Deletion test
If a sentence disappears, does the post lose information, reasoning, personality, or rhythm?

If no, consider deleting it.

### Claim test
Are reports, rumors, forecasts, and opinions qualified correctly?

### Platform test
Does the content feel native to the requested platform?

### Language-native test
Would a fluent speaker plausibly write this without sounding translated from another language?

Check:

- unnatural word order
- literal idioms
- over-formal connectors
- inappropriate honorifics
- English punctuation habits copied into CJK text
- Vietnamese wording that feels machine-translated
- unnecessary bilingual repetition

## Light revision

Review may directly fix:

- one awkward sentence
- minor verbosity
- one slop phrase
- punctuation
- a small qualification

Review should not silently replace the thesis. Route back when strategy is the problem.

## Retry budget

Maximum:

- 2 total review cycles
- 2 writer attempts
- 1 angle retry
- 1 research retry

After the budget is exhausted, return the highest-quality safe version with a concise uncertainty note when needed.
