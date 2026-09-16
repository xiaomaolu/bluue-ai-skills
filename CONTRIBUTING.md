# Contributing to Bluue AI Skills

Thanks for helping improve Bluue AI Skills. Contributions should make an agent skill more useful, reliable, or easier to maintain without expanding its scope unnecessarily.

## Before you start

- Check existing issues and pull requests before proposing the same change.
- Open an issue first for a new skill, a major behavioral change, or a repository-wide convention.
- Keep pull requests focused. Unrelated skill changes should be submitted separately.

## Repository structure

Each installable skill lives in a top-level directory whose name matches the `name` in its `SKILL.md` frontmatter.

```text
skill-name/
|-- SKILL.md
|-- agents/       Optional UI metadata
|-- scripts/      Optional deterministic helpers
|-- references/   Optional guidance loaded when needed
`-- assets/       Optional files used in generated output
```

Use supporting directories only when they materially improve the skill. Keep the main `SKILL.md` focused on routing, essential workflow, and non-obvious constraints.

## Adding or changing a skill

1. Use a lowercase, hyphen-separated directory name and the same value for the frontmatter `name`.
2. Include concise `name` and `description` fields in YAML frontmatter. Keep descriptions specific enough to distinguish when the skill should be used.
3. Remove scaffold placeholders and link every required reference from `SKILL.md` or another discoverable resource.
4. Preserve existing `agents/openai.yaml` policy and dependency fields unless the change specifically requires updating them.
5. Put repeatable operations in `scripts/`, conditional detail in `references/`, and output resources in `assets/`.
6. Update both `README.md` and `README.zh-CN.md` when adding, renaming, or removing a public skill.
7. Do not commit secrets, private data, generated credentials, or assets without redistribution rights and attribution where required.

## Validate locally

The repository validator mirrors the structural checks used by the Codex skill creator and also requires each skill name to match its directory.

```bash
python -m pip install -r requirements-validation.txt
python -X utf8 scripts/validate_skills.py
```

The same validation runs automatically for pull requests, version tags, and pushes to `main`.

For changed scripts, also run the script's relevant behavior checks. Structural validation does not prove that a skill makes good decisions, so manually review its scope, references, examples, and failure boundaries.

## Pull request checklist

- Explain the real request or maintenance problem the change addresses.
- Describe user-visible behavior changes and any intentionally unchanged behavior.
- Keep instructions scoped and avoid generic advice the agent already knows.
- Confirm new references are linked and new assets have appropriate provenance.
- Include the local validation result and any focused behavioral evidence.
- Update both repository READMEs when the public skill catalog changes.

## Releases

Maintainers create releases from a green `main` branch using semantic version tags such as `v0.1.0`. Release notes should identify added or materially changed skills and maintenance tooling. Contributors should not change repository versioning in a feature pull request unless requested by a maintainer.
