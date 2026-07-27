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
