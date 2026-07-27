# Bold Flat Accent Variant

Read this file only after selecting `style_variant: bold-flat-accent`. Treat it as an optional rendering branch inside `bluue-minimal-doodle`, not as a separate skill and not as the default style.

## Contents

- [Purpose](#purpose)
- [Selection Guard](#selection-guard)
- [User-Facing Fields](#user-facing-fields)
- [Advanced Fields](#advanced-fields)
- [Composition Defaults](#composition-defaults)
- [Fixed Rendering Rules](#fixed-rendering-rules)
- [Model-Facing Prompt](#model-facing-prompt)
- [QA](#qa)
- [Example: Bike Sharing](#example-bike-sharing)

## Purpose

Create warm editorial doodles with a pure white background, thick smooth black outlines, large solid-black shapes, simplified rounded forms, one clear action, and exactly one controlled accent color.

Preserve the parent skill's theme analysis, factual research, image-tool workflow, independent variant generation, reference-image handling, and delivery rules.

## Selection Guard

Select this branch when the user:

- explicitly names `bold-flat-accent`; or
- clearly requests thick smooth outlines, flat black shapes, a large simplified subject, and one accent color as a combined visual language.

Do not select it for a color request alone. Do not merge it with the default rough-marker prompt.

## User-Facing Fields

Accept natural language or structured values. Infer unspecified values.

| Field | Values | Default |
|---|---|---|
| `accent_policy` | `none`, `auto`, `brand`, `custom` | `auto` |
| `accent_color` | one named color or hex value | infer; required for `custom` |
| `accent_coverage` | 5–25 percent | 12 |
| `subject_scale` | `compact`, `medium`, `large`, `auto` | `auto` |
| `framing` | `full-body`, `three-quarter`, `waist-up`, `close-up`, `object-centered`, `auto` | `auto` |
| `subject_position` | `center`, `lower-center`, `center-left`, `center-right`, `auto` | `auto` |
| `mood` | natural language or preset | `warm-restrained` |
| `primary_action` | one visually explicit action | infer |
| `primary_prop` | zero or one main interacting object | infer |
| `symbol_count` | 0–2 | 1 |
| `aspect_ratio` | any supported output ratio | 1:1 |
| `variant_count` | positive integer | 1 |

For `accent_policy`:

- `none`: keep pure black and white while retaining the bold flat branch.
- `auto`: choose one color that supports the theme and mood.
- `brand`: verify and use one representative brand color; do not add a logo or wordmark unless explicitly requested.
- `custom`: use the user's exact color.

Clamp `accent_coverage` to 5–25 percent unless the user explicitly overrides the branch aesthetic. Use the color in 2–4 localized flat shapes. Never introduce a second accent color.

## Advanced Fields

Infer these unless the user explicitly controls them:

| Field | Values | Default |
|---|---|---|
| `line_character` | `smooth-bold`, `soft-wobble`, `rough-bold` | `smooth-bold` |
| `line_weight` | `medium`, `bold`, `extra-bold` | `bold` |
| `fill_strategy` | `outline-only`, `balanced`, `black-mass` | `black-mass` |
| `shape_language` | `rounded`, `angular`, `mixed`, `auto` | `auto` |
| `expression_intensity` | `minimal`, `low`, `medium` | `low` |
| `accent_zones` | 2–4 named local regions or `auto` | `auto` |

Prefer a single action group over detached symbols. Let the primary action and prop carry the concept. Use extra symbols only when the theme remains unclear without them.

## Composition Defaults

- Use one primary subject or one tightly integrated subject-and-prop action group.
- Let the group occupy 65–85 percent of the frame.
- Use `large` for a waist-up person, `medium` for a full-body person or object, and `compact` only for an intentionally distant concept.
- Keep 15–35 percent clean white negative space.
- Use asymmetric balance when the subject looks toward or interacts with a prop.
- Keep the background completely blank.

## Fixed Rendering Rules

- Use a pure white background.
- Draw thick, smooth black contours with nearly uniform weight.
- Use large solid-black shapes for selected hair, clothing, or the primary prop.
- Use rounded simplified anatomy without chibi proportions.
- Keep facial features minimal and the expression restrained.
- Use exactly one accent color when `accent_policy` is not `none`.
- Use flat fills with no tone variation.
- Exclude gradients, gray wash, shadows, highlights, realistic lighting, texture, detailed environments, decorative patterns, text, signature, and watermark.
- Exclude logos, wordmarks, QR codes, and interface text unless explicitly requested.

## Model-Facing Prompt

Resolve every bracketed field before generation and remove unused lines.

```text
Use case: stylized-concept
Asset type: bold flat editorial doodle illustration

Primary request:
Create a minimalist illustration about “[THEME]”.

Core interpretation:
[ONE-SENTENCE CORE IDEA]

Main subject and action:
[ONE EXPLICIT SUBJECT, PRIMARY ACTION, RESTRAINED EXPRESSION, RECOGNITION CUES, AND OPTIONAL PRIMARY PROP]
Make the subject and prop one compact action group. Use simplified rounded anatomy and a clear silhouette rather than realistic detail.

Optional symbolic element:
[ZERO TO TWO SMALL INTEGRATED SYMBOLS WITH PLACEMENT AND MEANING]
Do not add detached decorative icons.

Style variant:
Bold-flat-accent editorial doodle. Use thick, smooth black outlines of nearly uniform weight, large clean shapes, very sparse internal detail, and solid-black masses in selected parts of the subject or prop. Keep the image calm and approachable but not chibi, childish, glossy, or photorealistic.

Color palette:
Use a pure white background, pure black outlines and fills, and [EXACTLY ONE ACCENT COLOR OR NO ACCENT]. Apply the accent only to [2–4 RESOLVED ACCENT ZONES], covering approximately [ACCENT COVERAGE] percent of the canvas. Use perfectly flat color with no gradients, shading, highlights, texture, or tone variation. Add no other colors and no gray.

Composition:
Use [FRAMING] framing with the subject at [SUBJECT POSITION]. Let the complete action group occupy approximately [SUBJECT SCALE PERCENT] percent of the frame. Keep 15–35 percent clean white negative space and leave the background completely blank. Preserve immediate thumbnail readability.

Constraints:
No complex scene, extra characters, detached decorative icons, text, caption, signature, watermark, logo, wordmark, QR code, readable interface, gradients, shadows, gray wash, texture, realistic lighting, thin delicate line art, sketch hatching, glossy vector effects, photorealism, or cute chibi styling.

Desired result:
A bold flat editorial doodle centered on one clear action, with strong black graphic weight, a controlled single-color accent, and an emotionally restrained subject.
```

## QA

Inspect the generated image for:

- one subject or tightly integrated subject-and-prop action group;
- one immediately readable action;
- subject occupancy between roughly 65 and 85 percent;
- pure white background;
- thick smooth near-uniform outlines;
- deliberate large solid-black areas;
- zero or one accent color according to `accent_policy`;
- accent coverage within the requested range and localized to 2–4 regions;
- flat color without gradients, shading, highlights, or gray;
- no more than two integrated symbols;
- no text, logo, wordmark, QR code, signature, or watermark;
- restrained expression and non-chibi proportions.

If a major criterion fails, preserve the successful subject, action, prop, and composition while correcting only the dominant failure:

```text
Keep the subject, action, prop, pose, and composition unchanged. Correct only the rendering: use a pure white background, thick smooth near-uniform black outlines, deliberate solid-black shapes, and exactly one perfectly flat accent color in the specified local regions. Remove every gradient, shadow, highlight, gray tone, texture, extra color, text, and logo.
```

## Example: Bike Sharing

```yaml
theme: bike sharing
style_variant: bold-flat-accent
accent_policy: custom
accent_color: "#FFB24D"
accent_coverage: 15
subject_scale: large
framing: full-body
subject_position: center
mood: quiet-focused
primary_action: using a blank phone to unlock a bicycle
primary_prop: one simplified shared bicycle
symbol_count: 1
aspect_ratio: "1:1"
variant_count: 1
```
