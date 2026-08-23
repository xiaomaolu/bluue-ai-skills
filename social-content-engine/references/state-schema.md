# Shared State Schema

Use a compact shared state. Modules should update only their owned fields.

```json
{
  "request": {
    "raw": "",
    "task": "create",
    "topic": "",
    "platform": null,
    "format": null,
    "input_language": null,
    "output_language": null,
    "locale": null,
    "bilingual_requested": false,
    "code_switch_allowed": false
  },
  "context": {
    "score": 0,
    "audience": null,
    "user_angle": null,
    "tone": null,
    "goal": null,
    "source_material": [],
    "must_include": [],
    "must_avoid": [],
    "missing": []
  },
  "freshness": {
    "score": 0,
    "research_required": false,
    "time_range": null,
    "research_purposes": []
  },
  "research": {
    "status": "not_started",
    "facts": [],
    "developments": [],
    "numbers": [],
    "competitive_context": [],
    "social_signals": [],
    "unknowns": [],
    "sources": []
  },
  "strategy": {
    "candidate_angles": [],
    "selected_angle": null,
    "angle_confidence": null,
    "supporting_fact_ids": []
  },
  "platform": {
    "profile": null,
    "recommended_length": null,
    "information_density": null,
    "structure": [],
    "hook_behavior": null,
    "evidence_budget": null,
    "cta_behavior": null,
    "formatting_rules": [],
    "avoid": []
  },
  "style_profile": {
    "applied": false,
    "language_specific": {},
    "platform_specific": {},
    "general": {}
  },
  "draft": {
    "version": 0,
    "mode": "direct",
    "content": null
  },
  "review": {
    "score": null,
    "approved": false,
    "issues": [],
    "next_action": null,
    "cycles": 0
  }
}
```

## Claim object

Recommended research claim shape:

```json
{
  "id": "fact_1",
  "claim": "",
  "type": "official",
  "confidence": "high",
  "source_tier": "A",
  "source_title": "",
  "source_url": "",
  "published_at": null,
  "usable_as_fact": true
}
```

## Candidate angle object

```json
{
  "id": "angle_1",
  "type": "implication",
  "thesis": "",
  "novelty": 0,
  "specificity": 0,
  "evidence": 0,
  "audience_fit": 0,
  "platform_fit": 0,
  "total": 0
}
```

## Field ownership

| Module | Fields |
|---|---|
| router | `request`, `context.score`, `freshness` |
| context enrichment | `context` |
| research | `research` |
| angle discovery | `strategy` |
| platform adapter | `platform` |
| style profile | `style_profile` |
| writer / repurpose / hook | `draft` |
| review | `review` |

Explicit user constraints are immutable unless the user changes them.
