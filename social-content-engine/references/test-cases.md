# Evaluation Cases

Use these cases after material changes. Judge routing and output behavior, not exact wording.

## Case 1 — Sparse current topic, Chinese → X

Input:
> Apple 折叠屏，写个 X

Expected:
- platform = X
- context score low
- freshness high
- research current reports
- angle discovery
- one concise Chinese result
- no generic “备受期待”
- reports remain qualified

## Case 2 — Detailed LinkedIn, English

Input:
> Write a LinkedIn post for compliance leaders at banks about why AI governance is moving from policy work into operating controls. Use a professional tone and cite two recent regulatory developments.

Expected:
- high context score
- research required
- audience preserved
- no need to infer a new angle if supplied thesis is strong
- professional LinkedIn structure
- two current, relevant developments
- no fake executive experience

## Case 3 — Reddit first-person boundary

Input:
> Write a Reddit post about what I've learned trading 30-second event contracts. Keep it casual.

Expected:
- first person allowed
- no invented years, win rate, P&L, trade count
- participant voice
- low brand polish
- genuine discussion close only if natural

## Case 4 — Vietnamese Facebook

Input:
> Viết một bài Facebook ngắn cho sinh viên Việt Nam về cách dùng AI để sửa CV. Giọng tự nhiên, không quảng cáo quá.

Expected:
- vi-VN
- no English translationese
- student-friendly language
- practical value
- low promotional pressure

## Case 5 — Japanese product commentary

Input:
> Appleの折りたたみiPhoneについて、Threads向けに短くコメントして。煽りすぎない。

Expected:
- ja-JP
- current-topic research
- restrained claims
- Threads conversational structure
- no aggressive English-style hype

## Case 6 — Cross-language repurpose

Input:
> Turn this English LinkedIn post into a Vietnamese Facebook post. Don't translate literally.

Expected:
- repurpose, not rewrite from scratch
- preserve thesis/evidence
- rebuild Facebook structure
- native Vietnamese
- no repeated bilingual content

## Case 7 — Unknown platform

Input:
> Make this suitable for our community platform “CircleX”. Keep it concise.

Expected:
- generic adapter
- no invented character limit or algorithm claims
- preserve user’s source content and constraints

## Case 8 — Pure rewrite, no research

Input:
> Make this X post less corporate: “AI is redefining the rapidly evolving marketing landscape...”

Expected:
- no research
- remove slop
- keep meaning
- one revised post

## Case 9 — X social search limitation

Input:
> Find every tweet from this account in the last year and analyze them.

Expected:
- recognize exhaustive structured-data requirement
- prefer official/dedicated X data source if available
- do not claim domain-filtered web search is complete

## Case 10 — Bilingual request

Input:
> 写一条 LinkedIn，中英双语，主题是香港 AI governance。

Expected:
- explicit bilingual output
- research if current claims are made
- two natural versions, not literal mirrors
- preserve terminology consistently

## Case 11 — Xiaohongshu without first-hand experience

Input:
> 帮我写一篇小红书，说说最近看到的折叠屏趋势。我自己没用过折叠屏。

Expected:
- respect “没用过”
- no fake体验
- use observation/research framing
- useful, natural Chinese
- practical title/opening

## Case 12 — Style preference

History:
- user repeatedly removes rhetorical questions
- user asks “写一条 X”

Expected:
- style profile suppresses rhetorical question by default
- current explicit instruction still wins if user asks for one
