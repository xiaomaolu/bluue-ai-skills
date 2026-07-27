---
name: bluue-minimal-doodle
description: Generate or prompt minimalist black-and-white hand-drawn doodle illustrations for people, literary or screen works, concepts, events, places, objects, products, and brands. Use when the user wants a sparse white-background image with rough black marker lines, ample negative space, low information density, restrained expression, literary notebook-sketch character, or a few symbolic visual hints. Support new generation, prompt-only requests, variants, and optional reference images; do not use for polished line art, colorful cartoons, photorealism, complex narrative scenes, or general image styles outside this visual language.
---

# Bluue Minimal Doodle

Turn any theme into one visually sparse, emotionally precise black-marker doodle. Resolve the theme, core idea, mood, and symbols before calling the image generator; never send unresolved template variables or automatic-selection values to the model.

## Defaults

Use these defaults unless the user overrides them:

- Theme type: infer automatically
- Output mode: generate the image
- Mood: infer from the theme; do not force loneliness, coldness, or absurdity
- Symbols: choose 2; allow 1–3
- Composition: one subject near the lower center
- Background: plain white with approximately 70–80% empty space
- Palette: pure black lines on white only
- Text: none
- Recognizability: suggestive rather than realistic
- Aspect ratio: 1:1
- Variants: 1

Accept natural-language requests. Do not require the user to provide a parameter object.

## Workflow

### 1. Determine the requested output

- Generate an image by default.
- Return only a production-ready prompt when the user explicitly asks for a prompt, template, or prompt optimization.
- Generate each requested variant with a separate image call; never combine variants into a contact sheet unless the user asks for one.
- Treat an attached image as a reference for identity, pose, composition, or mood unless the user explicitly asks to edit it.
- Follow the installed `imagegen` skill for built-in-first tool selection, reference-image handling, output paths, and final delivery.

Ask a question only when the theme itself is missing or an ambiguous identity would materially change the image. Infer all non-critical choices.

### 2. Build a resolved visual brief

Resolve the following fields internally before writing the model-facing prompt:

```text
theme:
theme_type:
core_idea:
primary_subject:
mood:
recognition_cues:
symbolic_elements:
composition:
aspect_ratio:
must_avoid:
```

Keep `core_idea` to one sentence. Give every symbol a clear relationship to the theme or subject.

Use stable, established knowledge for familiar themes. Research first only when the subject is obscure, ambiguous, current, or depends on precise biographical, historical, cultural, or brand facts. Prefer authoritative or primary sources when research is necessary. Do not invent factual associations merely because they are easy to draw.

### 3. Classify and simplify the theme

Choose one primary type:

- **Person:** Use one figure. Preserve only the gesture, expression, silhouette, hairstyle, clothing cue, or prop needed for recognition. Avoid a realistic portrait.
- **Work:** Use one central figure or object and the work's central tension. Suggest the plot through symbols; do not reenact the full story.
- **Concept:** Convert the abstraction into one subject plus one visual contradiction, absence, displacement, or impossible relationship.
- **Event or era:** Use one representative figure or object, one consequence symbol, and at most one environmental hint. Avoid historical panoramas.
- **Place:** Use one recognizable architectural or geographic contour plus at most two cultural or emotional cues. Avoid a complete landscape.
- **Object or product:** Use the essential silhouette, one functional cue, and at most one cultural or usage association.
- **Brand:** Use a product, service behavior, or public association. Do not add a logo, slogan, or trademark unless the user explicitly requests it.

When a theme fits multiple types, choose the type that produces the clearest single subject and the fewest explanatory elements.

### 4. Select 1–3 symbolic elements

Generate several candidates, then select only elements that score well on:

1. Direct relevance to the theme
2. Immediate visual recognizability
3. Ability to be drawn in a few rough strokes
4. Emotional or conceptual tension
5. Non-redundancy with the other elements
6. Compatibility with ample negative space

Prefer active visual relationships over detached icons: a tilted crown on the ground is stronger than a floating crown; a shadow facing the wrong direction is stronger than an unrelated eye symbol.

Reject:

- Generic decoration with no narrative role
- Several symbols expressing the same idea
- Symbols that require captions to understand
- Clichés unrelated to the specific theme
- Dense collections of props

If the composition feels crowded, remove symbols before shrinking the empty space.

### 5. Write the model-facing prompt

Write the final prompt in direct visual language. Substitute every bracketed field with resolved content and remove unused lines.

```text
Use case: stylized-concept
Asset type: minimalist literary notebook illustration

Primary request:
Create a minimalist black-and-white hand-drawn doodle illustration about “[THEME]”.

Core interpretation:
[ONE-SENTENCE CORE IDEA]

Main subject:
[EXPLICIT DESCRIPTION OF THE SINGLE PRIMARY SUBJECT, POSE, EXPRESSION, AND ESSENTIAL RECOGNITION CUES]
Keep the expression and body language [MOOD]. Make the subject recognizable through a few selective cues, not realistic portrait detail.

Symbolic elements:
Include only [1–3] small symbolic elements:
1. [SYMBOL, PLACEMENT, AND RELATIONSHIP TO THE SUBJECT]
2. [SYMBOL, PLACEMENT, AND RELATIONSHIP TO THE SUBJECT]
3. [OPTIONAL SYMBOL, PLACEMENT, AND RELATIONSHIP TO THE SUBJECT]
Make every symbol narratively meaningful rather than decorative.

Style and medium:
Rough black marker doodle, uneven hand-drawn contours, slight natural line wobble, variable line weight, loose literary notebook sketch, spontaneous but intentional, sparse details, low information density, restrained expression, subtle symbolic visual language, pure white paper background, black lines only.

Composition:
Use one clear primary subject near the lower center of the canvas. Keep approximately 70–80% of the canvas empty white space. Keep the background almost entirely blank. Separate the small symbolic elements clearly from the main silhouette. Preserve immediate thumbnail readability. Use aspect ratio [ASPECT RATIO].

Constraints:
Pure black lines on clean white only. No color, gray wash, gradients, complex shading, realistic lighting, detailed textures, polished digital line art, photorealism, elaborate scenery, crowds, decorative borders, comic panels, ornamental decoration, cute or chibi styling, text, caption, signature, logo, or watermark.

Desired result:
Make the image feel like a rough literary notebook illustration: casually drawn, emotionally exact, visually sparse, and centered on one memorable gesture, expression, or visual contradiction.
```

Do not rely on negative wording alone. State the desired positive appearance before the avoid list.

### 6. Generate and inspect

Use the built-in image generation tool by default. After generation, inspect the actual image against all of these criteria:

- One unmistakable primary subject
- Subject positioned near the lower center unless overridden
- Approximately 70% or more blank white space
- Only 1–3 meaningful symbolic elements
- Pure black-and-white appearance without unintended color
- Rough, uneven marker lines rather than polished vector-like contours
- Low detail density and no completed environment
- Theme recognizable at thumbnail size
- Mood visible through pose or expression
- No accidental text, logo, signature, or watermark
- No unwanted photorealism, ornate illustration, or cute cartoon treatment

If a major criterion fails, regenerate with one targeted correction while preserving successful elements. Repeat invariants explicitly. Change only the dominant failure per iteration.

Use correction language such as:

```text
Keep the subject, pose, and symbolic elements unchanged. Simplify the image substantially, remove secondary details, increase empty white space to approximately 80%, and make the black marker contours rougher, more uneven, and less polished. Keep a pure white background with no gray shading or text.
```

### 7. Deliver

- Show generated previews inline.
- For project-bound images, save the selected final asset in the workspace without overwriting an existing file unless explicitly requested.
- Report the final saved path when applicable.
- Include the final resolved prompt and generation mode in the handoff unless the user asks for only the image.

## Conflict Resolution

When instructions compete, preserve them in this order:

1. User's explicit requirements
2. One clear primary subject
3. Black-line-on-white visual identity
4. Negative space and low information density
5. Recognizability and core expression
6. Theme-specific meaning
7. Symbolic elements
8. Secondary detail

Never preserve a secondary prop by sacrificing the blank background or main silhouette.

## Example: Shakespeare

Resolve “Shakespeare” approximately as follows:

```text
Theme type: person
Core idea: A silent observer of human ambition, performance, mortality, and contradiction.
Primary subject: A simplified Shakespeare figure with a high forehead, small mustache, restrained eyes, and a minimal suggestion of an Elizabethan collar.
Mood: calm, distant, slightly weary
Symbols:
- a small skull beside one hand for mortality and Hamlet
- a tilted crown on the ground for tragedy, power, and unstable rule
- a broken quill with one loose ink line for authorship and unfinished human conflict
```

Place the figure near the lower center and keep the rest of the page nearly empty. Do not add a theater, bookshelf, manuscript text, decorative frame, or detailed period costume.
