# Bluue AI Skills

Open-source AI agent skills created by Bluue.

## Skills

### bluue-minimal-doodle

Turns people, works, concepts, events, places, objects, products, and brands into minimalist doodle illustrations. It ships as one skill with one default style and one optional style branch.

It supports:

- direct image generation through an available image-generation tool
- prompt-only output
- people, works, concepts, events, places, objects, products, and brands
- a default black-and-white rough literary style
- an optional bold flat style with exactly one controlled accent color
- optional reference images and independent variants
- automatic visual QA and focused regeneration

## Style variants

Install only `bluue-minimal-doodle`. The two styles are internal variants of the same skill, not separate skills.

### Visual comparison

| `rough-literary` — default | `bold-flat-accent` — optional |
|---|---|
| <img src="./assets/examples/rough-literary-prediction-market.png" alt="Prediction market in the rough-literary style" width="480"> | <img src="./assets/examples/bold-flat-accent-bike-sharing.png" alt="Bike sharing in the bold-flat-accent style" width="480"> |
| Rough black marker lines, high negative space, black and white, small symbolic elements. | Smooth thick outlines, deliberate solid-black shapes, a larger action group, and one controlled accent color. |

### Which style should I choose?

| What the user wants | Style |
|---|---|
| Black-and-white literary sketch, rough marker lines, lots of empty space | `rough-literary` |
| Thick smooth outlines, flat black shapes, larger characters or objects, one accent color | `bold-flat-accent` |
| No style specified | `rough-literary` |
| Only “add some color” or “use a brand color” is specified | Choose a style explicitly; color alone does not switch branches |

The skill should not ask about style on every request. It uses the default immediately unless the request is visually ambiguous. When a color request could materially change the rendering, use this concise clarification:

```text
This skill has two styles: rough-literary is the default black-and-white literary sketch; bold-flat-accent uses smooth thick outlines and one accent color. Which one do you want? If unspecified, I will use rough-literary.
```

Users can also use natural-language aliases:

- “black-and-white literary sketch” or “黑白文学草图” → `rough-literary`
- “bold flat single-accent style” or “粗线单色扁平风格” → `bold-flat-accent`

### rough-literary

This is the default. If the user does not choose a style, the skill produces a sparse black-and-white rough-marker literary doodle with ample negative space.

```text
Use $bluue-minimal-doodle to create an illustration about prediction markets.
```

The same request can be explicit:

```text
Use $bluue-minimal-doodle with style_variant rough-literary to illustrate Shakespeare.
```

### bold-flat-accent

This optional branch uses smooth thick black outlines, deliberate solid-black shapes, a larger subject, and zero or one controlled accent color.

```text
Use $bluue-minimal-doodle with style_variant bold-flat-accent to illustrate bike sharing. Use warm orange as the only accent color and keep it below 15% of the image.
```

Brand-color example:

```text
Use $bluue-minimal-doodle with style_variant bold-flat-accent to illustrate Lululemon. Use accent_policy brand, one accent color only, and no logo or text.
```

Color alone does not activate the optional branch. Select `bold-flat-accent` explicitly when its full visual treatment is wanted.

## Install

Clone the repository:

```bash
git clone https://github.com/xiaomaolu/bluue-ai-skills.git
```

Copy the skill into your Codex skills directory.

PowerShell:

```powershell
Copy-Item -Recurse -LiteralPath ".\bluue-ai-skills\bluue-minimal-doodle" -Destination "$env:USERPROFILE\.codex\skills\"
```

macOS or Linux:

```bash
cp -R ./bluue-ai-skills/bluue-minimal-doodle ~/.codex/skills/
```

Invoke it with:

```text
Use $bluue-minimal-doodle to create a minimalist doodle about prediction markets.
```

## License

MIT
