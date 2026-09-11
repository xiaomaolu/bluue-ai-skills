---
name: bluue-infographic-series
description: Turn long-form content, reports, structured notes, concepts, processes, and data into polished infographic images or cohesive infographic series. Use when the user asks to summarize, visualize, explain, structure, or convert content into an infographic, visual brief, data poster, explainer, process graphic, or multi-image series. Default to 9:16, preserve source-language content when provided, otherwise use English, keep text sparse and accurate, classify the content as data/explainer/summary/process/general, and lock one coherent art direction per series while allowing varied compositions across frames.
---

# Bluue Infographic Series

Convert information into a readable visual system, then generate one image or a coherent series of images. The primary job is information architecture: decide what deserves visual space, how many frames are needed, what visual form fits each idea, and which style can carry the whole series without sacrificing readability.

Treat the image as a communication surface, not a container for the entire source. If the content is too dense, split it into more frames instead of shrinking text or stacking more modules.

## Defaults

Use these defaults unless the user overrides them:

- Output mode: generate images
- Aspect ratio: `9:16`
- Language priority: explicit user request → dominant language of supplied content → English
- Long-form output: series by default
- Short or focused output: single image when one frame can carry the message clearly
- Series length: usually 3–7 frames; use fewer or more when the material clearly demands it
- Content type: infer one primary type from `data`, `explainer`, `summary`, `process`, `general`
- Art direction: select one style for the entire series and lock it before generating frame 1
- Palette: restrained; normally one base, one neutral/text system, and one accent family
- Image density: one primary message per frame
- Text density: sparse; split rather than cram
- Visual assets: prefer data-native and relationship-native forms such as charts, topology, timelines, thresholds, paths, and spatial hierarchy; use icons only when they communicate faster than the native structure
- User questions: ask only when uncertainty would materially change the output

Accept natural-language requests. Do not require the user to provide a parameter object.

## Hard rules

1. **One frame, one message.** A frame may contain supporting evidence, but it must have one obvious takeaway.
2. **One series, one art direction.** Keep palette, typography logic, icon language, line weight, texture, chart styling, image treatment, and general visual grammar consistent across the full series.
3. **Do not overload the canvas.** If content does not fit at a readable size, create another frame.
4. **Text fidelity is a release gate.** Names, dates, percentages, units, labels, citations, and factual claims must match the resolved content brief.
5. **Do not invent data.** Use supplied or researched facts only. Clearly label illustrative values.
6. **Charts must be truthful.** Geometry, order, proportions, and units must correspond to the data.
7. **Visual decoration stays subordinate to comprehension.** Do not let texture, photography, collage, gradients, icons, or illustration compete with the message.
8. **Do not default to stock-icon shorthand.** Avoid icon-per-bullet layouts, rows of circular icon badges, and repeated avatar, building, document, shield, robot-head, AI-brain, checkmark, or warning-triangle symbols when the underlying system can be shown directly.
9. **Default to 9:16.** Use another ratio only when the user requests it or the target surface clearly requires it.
10. **Preserve language intentionally.** Do not translate supplied content unless the user asks or the output language is explicitly changed.
11. **Generate frames separately.** Never return a contact sheet or collage of the series unless the user explicitly asks for one.

## Workflow

### 1. Resolve the request

Determine:

```text
source_content:
source_language:
requested_language:
output_language:
audience:
communication_goal:
content_type:
single_or_series:
frame_count:
aspect_ratio:
requested_style:
reference_images:
brand_constraints:
critical_text:
critical_data:
```

Infer sensible values when the request already contains enough context.

Ask one concise batch of up to three questions only when an unresolved choice materially affects the result, for example:

- the source mixes languages and the intended output language is unclear
- two source figures conflict and both cannot be correct
- the user requests a brand-specific style but provides no usable brand reference
- the user explicitly wants a particular publishing surface whose dimensions materially change the composition
- the requested series length conflicts with the amount of content

Do not ask about defaults merely to confirm them.

### 2. Resolve language

Use this order:

1. User explicitly names a language → use it.
2. User supplies substantial source content in one dominant language → preserve that language.
3. User supplies only a topic, sparse notes, or language-neutral data → use English.
4. For mixed-language sources, preserve proper nouns in their established form and use the dominant requested language for explanatory copy.

Do not silently translate source quotations, product names, legal terms, or official titles.

### 3. Classify the content

Choose one primary type. Read [references/content-architecture.md](references/content-architecture.md) when the source is long, structurally complex, or clearly needs multiple frames.

#### `data`
Use when the message is driven by numbers, comparisons, change over time, ranking, distribution, or performance.

Prefer:
- hero number
- bar / column / line / area / dot / slope chart
- progress or allocation block
- comparative stat cards
- annotated trend

#### `explainer`
Use when the user needs to understand what something is, how it works, what its parts are, or why it matters.

Prefer:
- annotated object or concept diagram
- layered system map
- labeled illustration
- cause-and-effect sequence
- simple spatial relationship

#### `summary`
Use for reports, articles, research, meeting notes, strategic briefs, and “key takeaways.”

Prefer:
- one strong thesis
- 3–5 supporting takeaways
- one important number or evidence block
- editorial hierarchy

#### `process`
Use for steps, workflows, operating models, decision logic, timelines, or roadmaps.

Prefer:
- numbered stages
- path or staircase
- directional flow
- swimlane-lite structure
- before → during → after

#### `general`
Use when no stronger structural type dominates.

Prefer:
- editorial poster composition
- one thesis plus 2–4 supporting modules
- a visual metaphor or one controlled image element

A series may contain frames of different content types, but assign one dominant series narrative and one locked style.

### 4. Compress the source into a visual hierarchy

Extract only what earns space.

Prioritize:

1. core thesis or headline
2. one main takeaway per frame
3. critical numbers and labels
4. mechanisms, comparisons, relationships, or sequence
5. one or two representative examples when essential
6. final implication or action

Deprioritize:

- repeated background explanation
- long narrative transitions
- redundant examples
- ornamental quotations
- paragraphs that merely restate the title
- low-value detail that forces smaller type

For long content, produce an internal series map before image generation:

```text
Series thesis:
Frame 1 — role / message / hero visual
Frame 2 — role / message / hero visual
Frame 3 — role / message / hero visual
...
```

A common long-form arc is:

```text
1. Cover / central claim
2. Why it matters / context
3. Core mechanism / structure
4. Key data / comparison
5. Risks, boundaries, or implications
6. Takeaway / action / roadmap
```

Use this only when it fits the source. Do not force every series into the same sequence.

### 5. Control information density

Use readable text at phone size. Prefer fewer words and stronger hierarchy.

Recommended targets per 9:16 frame:

- Hero headline: about 3–10 words
- Subtitle: about 1–2 short lines
- Supporting modules: usually 2–4
- Card or label copy: one short sentence or phrase
- English prose: usually about 25–70 visible words total
- CJK prose: usually about 50–140 visible characters total
- Data labels may exceed these targets when they remain visually simple

These are density targets, not mechanical limits. When the frame becomes crowded, split it.

### 6. Select and lock the art direction

Read [references/style-system.md](references/style-system.md) when the user provides style references, asks for a specific style, or requests a series.

The supported style vocabulary includes, but is not limited to:

- minimal
- international / Swiss-derived
- dark data / dark tech
- editorial / magazine
- collage
- skeuomorphic
- line art / diagrammatic
- illustration
- Bauhaus
- punk
- retro
- art deco
- flat
- acid graphic
- Japanese graphic design
- brutalist
- luxury modern

Pick the style from the communication problem, the content type, and any reference images. Do not choose an expressive style purely for novelty when it weakens legibility.

Before generating frame 1, resolve a `series_style_lock`:

```text
style_name:
background_system:
primary_text_color:
accent_colors:
typography_character:
headline_scale:
grid_and_alignment:
card_shape_or_no_cards:
line_weight:
chart_language:
visual_primitive_priority:
icon_language_or_none:
forbidden_stock_motifs:
image_treatment:
texture_policy:
lighting_or_gradient_policy:
recurring_motif:
forbidden_drift:
```

Repeat these invariants in every frame prompt. Vary composition and content, not the identity of the series.

### 7. Keep the palette restrained

For most series:

- one dominant background family
- one primary text/neutral family
- one accent family
- optional second accent only when the data truly requires a second encoded category

Tints and shades of the locked colors are allowed. Avoid rainbow charts and unrelated accents.

When a reference image contains many colors, extract the controlling palette rather than copying every visible hue.

### 8. Build a text manifest before generation

Read [references/text-fidelity.md](references/text-fidelity.md) whenever the infographic contains important labels, figures, legal/financial terminology, non-English text, or more than a few text elements.

Create an internal exact-text manifest:

```text
CRITICAL — must appear exactly
- headline:
- primary number:
- unit:
- proper nouns:
- dates:
- legal / technical terms:

FLEXIBLE — may be compressed without changing meaning
- subtitle:
- supporting labels:
- explanatory phrases:
```

Do not ask the image model to improvise critical strings.

For high-stakes or text-dense work, prefer a deterministic typography path when available: generate the visual background / illustration / composition, then typeset exact text using HTML/SVG/Canvas or another deterministic renderer. Pure image generation is appropriate when the visible copy is sparse enough to verify reliably.

### 9. Choose the visual vocabulary

Start with the semantic structure of the information, not an icon library. Map the meaning to a native visual primitive:

- time, state change, and continuous monitoring → timeline, event stream, pulse, or state transition
- ownership, dependency, and ecosystems → topology, weighted edges, nested nodes, or clustered relationships
- anomaly, risk, and alert intensity → threshold line, outlier marks, range band, halo, or restrained signal stem
- process and handoff → path, lanes, gates, or directional sequence
- hierarchy and control → scale, position, nesting, or containment
- comparison and performance → aligned bars, dots, slopes, intervals, or split fields
- categories → restrained shapes, color encoding, or labels
- quantitative evidence → truthful charts with corresponding geometry, order, proportions, and units
- people, places, products, or documentary context → photography or illustration when the literal subject matters
- atmosphere → low-contrast texture or pattern only after the information structure is clear

Use an icon only when removing it would make the meaning slower to recognize or genuinely ambiguous. When icons are necessary:

- keep them secondary to the encoded structure and text
- construct one coherent icon family with the same geometry, stroke, corner logic, and abstraction level
- use a small icon as a functional label rather than as the main visual concept
- do not place every icon inside a circle, card, glow ring, or decorative badge unless that container encodes state, cycle, orbit, percentage, or another real relationship

Reject these default treatments: icon-per-bullet layouts; repeated stock people, buildings, documents, shields, warning triangles, checkmarks, robot heads, or AI brains; glowing circular badges; mixed pictogram metaphors; and decorative node clutter. If the first draft relies on them, replace them with the underlying timeline, topology, threshold, path, hierarchy, or comparison structure.

Prefer one dominant visual device per frame. Avoid decorating every module independently. In the model-facing prompt, name the positive replacement, not only the prohibition—for example, request an ownership topology with weighted edges instead of merely saying “no building icons.”

### 10. Write the model-facing prompt

Every frame prompt should contain five blocks:

```text
A. Series lock
Exact shared art direction, palette, typography character, icon/chart language, texture and image treatment.

B. Frame objective
The one thing the viewer should understand from this frame.

C. Exact text manifest
Only the text that should actually appear. Mark critical strings as exact.

D. Composition
Describe hierarchy, placement, visual path, chart/diagram form, negative space, and where supporting elements sit.

E. Constraints
9:16 unless overridden, strong mobile readability, restrained palette, no accidental text, no extra logos, no invented facts, no visual clutter, no unrelated decorative elements.
```

Do not send the whole source article to the image model when a short resolved brief is enough.

### 11. Generate frame by frame

Use the built-in image generation tool by default when it is available and appropriate.

- Generate each frame as an independent full image.
- Reuse the exact `series_style_lock` in every call.
- Keep typography, color, image treatment, icon style, chart treatment, and recurring motifs stable.
- Change framing and composition enough that the series does not feel like the same template repeated.
- If the user asks for one frame first, generate only that frame and preserve the resolved style lock for later frames.

When the user supplies one or more reference images, use them to infer composition language, color discipline, typography character, chart treatment, image treatment, density, and atmosphere. Capture the core visual logic; do not mechanically copy a reference layout.

### 12. Review every generated image

Inspect the actual output before delivery.

Check:

#### Content
- one clear takeaway
- correct headline and labels
- correct numbers, units, dates, names, and terminology
- no invented claims
- no missing critical data

#### Readability
- strong hierarchy at thumbnail size
- no tiny body text
- no crowded corners
- adequate contrast
- enough negative space
- chart labels readable without zooming excessively

#### Visual quality
- style matches the locked art direction
- palette remains controlled
- decorative elements stay subordinate
- diagrams encode relationships, sequence, thresholds, or hierarchy rather than merely decorating labels
- composition differs appropriately from adjacent series frames
- no generic dashboard feel unless the user explicitly requested it
- no stock-icon shorthand where a data-native or relationship-native form would communicate better
- no repeated circular icon containers unless the circle carries encoded meaning
- icons, if present, share one construction logic and remain secondary
- no unnecessary gradients, shadows, or cards

#### Series consistency
- same typography character
- same palette logic
- same visual-primitive, line, and icon-or-no-icon logic
- same image / illustration treatment
- same overall sophistication level

If one major criterion fails, regenerate or edit with one focused correction while preserving successful elements.

### 13. Text-fidelity gate

Do not deliver an image with a visible error in critical text when the error can be corrected.

If image generation repeatedly corrupts a critical string:

1. reduce the amount of visible text
2. shorten non-critical copy
3. regenerate with the exact manifest repeated clearly
4. switch to deterministic text overlay when available

Never solve text-density problems by shrinking type below comfortable mobile readability.

### 14. Deliver

For a single image:

- show the image
- briefly state the selected content type and style only when useful

For a series:

- deliver frames in sequence
- keep each image independent
- preserve the same style lock throughout
- do not restate all design rationale after every frame

If the user asks for the plan before generation, provide a concise frame map. If they ask to generate directly, do not require approval of the plan first.

## Conflict resolution

When instructions compete, preserve them in this order:

1. user's explicit requirements
2. factual and textual accuracy
3. readability
4. one-message-per-frame structure
5. series consistency
6. requested brand or reference-image constraints
7. content-type fit
8. visual style novelty
9. decorative detail

Never preserve decorative detail by sacrificing legibility or factual accuracy.
