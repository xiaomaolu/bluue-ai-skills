# Review Error Codes

| Code | Meaning | Default route |
|---|---|---|
| `GENERIC_ANGLE` | Thesis is broadly reusable and weakly specific | angle-discovery |
| `LOW_SPECIFICITY` | Too many abstractions, too few concrete details | angle-discovery or writer |
| `WEAK_HOOK` | Opening lacks reason to continue | hook-optimizer or writer |
| `UNSUPPORTED_CLAIM` | Claim exceeds available evidence | research |
| `SOURCE_MISMATCH` | Source does not support the stated claim | research |
| `STALE_EVIDENCE` | Current claim relies on outdated evidence | research |
| `RUMOR_AS_FACT` | Report/rumor presented as confirmed | research + writer |
| `AI_SLOP` | Generic AI/marketing language dominates | writer |
| `PLATFORM_MISMATCH` | Structure feels native to another platform | platform-adapter + writer |
| `TOO_LONG` | Length/density exceeds the useful platform shape | writer |
| `TOO_THIN` | Content is too short to deliver the promised value | writer |
| `FAKE_PERSONAL_CONTEXT` | Invented user experience/identity | remove immediately |
| `TRANSLATIONESE` | Target-language text sounds translated | writer + multilingual rules |
| `LOCALE_MISMATCH` | Vocabulary/date/currency/formality mismatches locale | writer |
| `OVERRESEARCHED` | Too many facts obscure the thesis | writer |
| `ENGAGEMENT_BAIT` | Hook/CTA relies on empty bait | writer |
| `REPETITIVE` | Multiple sentences repeat the same function | writer |

## Severity

- `low`: can be fixed in light revision
- `medium`: writer revision normally needed
- `high`: route to research, angle, or platform module

## Review output shape

```json
{
  "score": 82,
  "approved": false,
  "issues": [
    {
      "code": "WEAK_HOOK",
      "severity": "medium",
      "note": "Opening repeats the topic without adding a claim."
    }
  ],
  "next_action": "hook-optimizer"
}
```
