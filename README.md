# Bluue AI Skills

Open-source AI agent skills created by Bluue.

## Skills

### bluue-minimal-doodle

Turns people, works, concepts, events, places, objects, products, and brands into sparse black-and-white marker doodles with ample negative space and a small number of meaningful symbols.

It supports:

- direct image generation through an available image-generation tool
- prompt-only output
- people, works, concepts, events, places, objects, products, and brands
- optional reference images and independent variants
- automatic visual QA and focused regeneration

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
