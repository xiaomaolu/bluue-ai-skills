# Social Research

Research supplies evidence and context. It does not write the final social post.

## 1. Define the research purpose

Select only what the draft needs:

- latest development
- fact verification
- useful statistics
- competitive context
- historical comparison
- public discussion
- community sentiment
- source discovery

If one authoritative source answers the question, stop.

## 2. Plan search queries

Simple topic: 1–2 queries.

Current or complex topic: 2–4 focused queries.

Do not turn a short social post into a deep-research project unless the user requests depth.

Example topic: Apple foldable device

- `Apple foldable iPhone latest reports` — recent development
- `Apple foldable display crease hinge supply chain` — product details
- `Apple foldable Samsung Huawei comparison` — competitive context

## 3. Multilingual search strategy

Read `references/multilingual.md`.

General rule:

- search the likely primary-source language
- add English for global topics when it may surface stronger reporting
- add the local language for local community sentiment or local regulations
- avoid translating proper nouns incorrectly
- deduplicate facts found through multiple languages

Example for a Vietnam-local topic:

- Vietnamese query for local sources
- English query only when global/company sources are likely relevant

Example for a Japanese company:

- Japanese query for primary/local coverage
- English query for international context

## 4. Provider-agnostic tool routing

Use whatever reliable tools are available.

Typical strengths:

- native web / Brave-style search: broad web/news discovery
- Tavily-style search: search + extraction + agent-friendly snippets
- Exa-style search: semantic/long-tail retrieval and content discovery
- official APIs: structured platform/account data when available
- Reddit-native search: community discussion
- X API or dedicated social-data source: structured X timelines/metrics

Do not treat domain-filtered web search of `x.com` as a complete Twitter/X dataset. It is discovery, not an exhaustive timeline or firehose.

## 5. Source tiers

Follow `references/source-policy.md`.

Use primary and high-quality sources for facts. Use social/community sources for sentiment and statements made by participants.

## 6. Claim taxonomy

Classify meaningful claims:

- `official`
- `confirmed`
- `reported`
- `rumor`
- `analysis`
- `opinion`
- `community_signal`

A report remains a report in the final draft.

Bad:

> Apple will release a foldable iPhone next year.

when the source only reports expectations.

Better:

> Apple is reportedly targeting...

## 7. Research object

Return only useful material:

### Facts
For each:

- claim
- claim type
- confidence
- source
- source tier
- publication date when relevant

### Recent developments
Only what affects the likely content angle.

### Useful numbers
Include units, time period, and source.

### Competitive context
Only comparisons that clarify the thesis.

### Public discussion
Recurring themes, not a cherry-picked single post presented as consensus.

### Unknowns
Material uncertainties.

### Sources
Deduplicated.

## 8. Stop conditions

Stop when:

- the central claim is supported
- the latest development is verified sufficiently for the post
- additional sources repeat the same information
- the evidence budget for the target platform is already filled

## 9. Research integrity

- Never invent a source.
- Never infer a complete trend from a few posts.
- Never treat likes/views from an unofficial scrape as authoritative unless the source supports them.
- Prefer the publication date of the source over the date a search engine indexed it.
- When sources disagree, preserve the disagreement or lower claim confidence.
