# Style System

Use this reference when selecting or extracting a visual direction for one infographic or a series.

## Core rule

A series may use varied compositions, but it must keep one coherent art direction. Lock the visual grammar before generating the first frame.

## Style families

### Minimal
Traits: high whitespace, strong hierarchy, restrained geometry, low decoration, neutral palette with one accent.
Best for: summary, data, product, corporate research.
Risk: can become generic if every frame is only cards and text.

### International / Swiss-derived
Traits: grid-led composition, bold typography, asymmetric balance, disciplined alignment, red/blue/black or similarly restrained accents.
Best for: data, research, systems, timelines.
Risk: excessive typographic austerity can weaken explanatory warmth.

### Dark Data / Dark Tech
Traits: near-black or deep navy ground, luminous accent, large numbers, fine charts, subtle glow, minimal chrome.
Best for: fintech, AI, trading, performance, technology.
Risk: uncontrolled glow and gradients quickly reduce sophistication.

### Editorial / Magazine
Traits: strong headline scale, asymmetric columns, image-text interplay, pull quotes, rules, captions, magazine pacing.
Best for: reports, summaries, thought leadership, case studies.
Risk: too much body copy can turn the frame into a page screenshot.

### Collage
Traits: clipped photography, paper layers, cut shapes, editorial fragments, strong crop logic.
Best for: culture, brand stories, social commentary, general topics.
Risk: texture and imagery can overpower data and text.

### Skeuomorphic
Traits: controlled material depth, physical surfaces, tactile objects, labels that feel embedded in real objects.
Best for: finance products, tools, objects, product explainers.
Risk: decorative realism can hurt clarity.

### Line Art / Diagrammatic
Traits: fine lines, outlined icons, arrows, nodes, technical annotations, restrained fill.
Best for: process, systems, explainers, architecture.
Risk: too many small labels reduce mobile readability.

### Illustration
Traits: one coherent illustration language carrying explanation, supporting labels integrated around it.
Best for: science, education, concepts, consumer topics.
Risk: illustration detail can become the subject instead of the information.

### Bauhaus
Traits: circles, bars, geometric modules, primary or tightly controlled colors, strong rhythm.
Best for: summary, process, conceptual visual systems.
Risk: decorative geometry without semantic purpose.

### Punk
Traits: rough typography, torn paper, aggressive contrast, photocopy texture, irregular placement.
Best for: cultural themes, strong opinion, campaign-like communication.
Risk: poor readability and inconsistency across frames.

### Retro
Traits: period typography, halftone, limited inks, poster composition, analog texture.
Best for: historical, nostalgic, consumer, culture.
Risk: fake vintage detail can overwhelm evidence.

### Art Deco
Traits: elegant symmetry, geometric ornament, dark luxury palette, metallic or cream accents.
Best for: premium finance, history, luxury, event summaries.
Risk: ornament must stay sparse.

### Flat
Traits: simple shapes, crisp icons, minimal depth, high clarity.
Best for: explainers, education, process.
Risk: can feel generic if icon-heavy.

### Acid Graphic
Traits: fluorescent accent, stretched type, liquid or warped forms, unconventional composition.
Best for: experimental culture, youth content, expressive general topics.
Risk: use only when the subject and audience can support it.

### Japanese Graphic Design
Traits: strong negative space, disciplined type, subtle asymmetry, restrained color, selective graphic motifs.
Best for: summary, concept, product, editorial.
Risk: avoid superficial cultural motifs unless relevant.

### Brutalist
Traits: raw grid, heavy type, hard edges, exposed structure, monochrome or one sharp accent.
Best for: technology, critical analysis, bold summaries.
Risk: can become visually hostile or dense.

### Luxury Modern
Traits: refined spacing, large type, quiet gradients or surfaces, premium neutral palette, precise alignment.
Best for: finance, brand, executive summaries, premium products.
Risk: avoid empty decoration with no informational role.

## Content-type routing

Use these as recommendations, not fixed rules:

| Content type | Strong defaults |
|---|---|
| data | dark data, minimal, international, editorial |
| explainer | line art, illustration, flat, Japanese, Bauhaus |
| summary | editorial, minimal, international, luxury modern |
| process | diagrammatic, international, Bauhaus, minimal, brutalist |
| general | editorial, collage, retro, punk, acid, luxury modern |

## Semantic primitives before icons

Choose the visual structure from the meaning before choosing an icon set. The primary graphic should expose how the information behaves:

| Meaning | Prefer |
|---|---|
| time, state change, continuous monitoring | timeline, event stream, pulse, state transition |
| ownership, dependency, ecosystem | topology, weighted edges, nested nodes, clusters |
| anomaly, risk, alert intensity | threshold line, outlier points, range band, halo, signal stem |
| process, handoff, approval | path, lanes, gates, directional sequence |
| hierarchy, control, containment | scale, position, nesting, spatial containment |
| comparison, performance | aligned bars, dots, slopes, intervals, split fields |

This is especially important for finance, compliance, AI, and technology subjects. Avoid turning them into a generic cyber dashboard made of glowing rings, stock line icons, and UI chrome. Prefer report-grade diagrams, disciplined hairline geometry, restrained markers, and visible relationships.

Before adding an icon, test it:

1. Does the literal object matter to the message?
2. Would the category or function be ambiguous without it?
3. Does it communicate faster than the timeline, topology, threshold, path, hierarchy, or comparison already present?

If the answer is no, remove it. Do not use an icon library as default decoration.

Avoid stock people, buildings, documents, shields, warning triangles, checkmarks, robot heads, and AI brains unless the literal object is necessary. Do not enclose every symbol in a circle, card, or glow ring. A circle is justified when it encodes state, cycle, orbit, percentage, or another meaningful relationship—not merely because it makes the element look like an interface button.

When an icon is necessary, keep it small and secondary, and use one custom-feeling family with consistent geometry, stroke, corner behavior, and abstraction. The diagram must remain understandable through its relationships even if the icons are hidden.

## Reference-image extraction

When the user supplies references, extract the design logic instead of copying surface details mechanically.

Resolve:

```text
background family:
headline treatment:
body typography character:
primary alignment:
grid:
negative space:
accent palette:
chart style:
visual primitive priority:
icon style or none:
forbidden stock motifs:
image treatment:
material / texture:
border / radius behavior:
recurring motif:
density:
```

Then create a style lock from those attributes.

## Series color discipline

Normally use:

- 1 background family
- 1 text / neutral family
- 1 accent family
- optional second encoded data color

A family can contain several tints and shades. Do not interpret “one accent family” as literally one hex everywhere.

## Composition diversity

Within a locked series style, vary dominant structures:

- typography-led hero
- data-led chart
- diagram-led explainer
- image-led editorial split
- comparison
- process path

Do not make every slide a three-card or four-card layout.

## Style lock QA

Before generating later frames, verify:

- same palette logic
- same type character
- same line weight
- same visual-primitive logic
- same icon family or the same deliberate no-icon policy
- same chart language
- same image treatment
- same texture level
- same overall contrast
- same degree of minimalism or expressiveness

Also verify that diagrams encode real relationships or states, that stock-icon shorthand has not replaced the information architecture, and that repeated circular containers carry meaning rather than decoration.

A frame that looks independently attractive but belongs to a different design universe is a failure.
